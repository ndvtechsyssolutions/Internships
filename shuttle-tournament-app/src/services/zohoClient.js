import axios from 'axios';

const {
  ZOHO_ACCESS_TOKEN,
  ZOHO_DATA_CENTER = 'com',
  ZOHO_TOURNAMENT_MODULE = 'Leads',
} = process.env;

export const syncRegistrationToZoho = async (registration, tournament) => {
  if (!ZOHO_ACCESS_TOKEN) {
    console.warn('Zoho access token missing. Skipping CRM sync.');
    return { skipped: true, reason: 'Missing token' };
  }

  const baseUrl = `https://www.zohoapis.${ZOHO_DATA_CENTER}/crm/v2/${ZOHO_TOURNAMENT_MODULE}`;
  const payload = {
    data: [
      {
        Last_Name: registration.playerName || registration.email?.split('@')[0] || 'Tournament Player',
        Email: registration.email,
        Phone: registration.contactNumber,
        Description: `Tournament: ${tournament.name} | Category: ${registration.category}`,
        Lead_Source: 'Shuttle Tournament Portal',
        Amount: tournament.entryFee,
        Custom_Tournament_Id: tournament.id,
        Status: registration.paymentStatus,
      },
    ],
    trigger: ['workflow'],
  };

  try {
    const response = await axios.post(baseUrl, payload, {
      headers: {
        Authorization: `Zoho-oauthtoken ${ZOHO_ACCESS_TOKEN}`,
      },
    });
    return response.data;
  } catch (error) {
    console.error('Zoho CRM sync failed', error.response?.data || error.message);
    throw new Error('Zoho CRM sync failed');
  }
};
