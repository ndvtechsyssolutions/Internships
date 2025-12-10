import { Router } from 'express';
import { z } from 'zod';
import { v4 as uuid } from 'uuid';
import {
  listRegistrations,
  listTournaments,
  addRegistration,
  addPayment,
  updateTournament,
} from '../data/store.js';
import { requireAuth } from '../middleware/auth.js';
import { processPayment } from '../services/paymentService.js';
import { syncRegistrationToZoho } from '../services/zohoClient.js';

const router = Router();

const registrationSchema = z.object({
  tournamentId: z.string(),
  playerName: z.string().min(3),
  email: z.string().email(),
  contactNumber: z.string().min(8),
  category: z.string().min(3),
  paymentMethod: z.enum(['upi', 'card', 'cash']).default('upi'),
});

router.get('/', requireAuth(['admin', 'facility']), (req, res) => {
  const registrations = listRegistrations();
  if (req.user.role === 'facility') {
    const tournaments = listTournaments().filter((t) => t.facilityId === req.user.facilityId);
    const facilityTournamentIds = new Set(tournaments.map((t) => t.id));
    return res.json(registrations.filter((reg) => facilityTournamentIds.has(reg.tournamentId)));
  }
  return res.json(registrations);
});

router.post('/', requireAuth(['user']), async (req, res) => {
  const parseResult = registrationSchema.safeParse(req.body);
  if (!parseResult.success) {
    return res.status(400).json({ message: 'Invalid registration payload', issues: parseResult.error.flatten() });
  }

  const payload = parseResult.data;
  const tournament = listTournaments().find((t) => t.id === payload.tournamentId);

  if (!tournament) {
    return res.status(404).json({ message: 'Tournament not found' });
  }

  if (tournament.status !== 'open') {
    return res.status(400).json({ message: 'Tournament not open for registrations' });
  }

  if (tournament.registeredCount >= tournament.maxPlayers) {
    return res.status(400).json({ message: 'Tournament slots are full' });
  }

  const payment = await processPayment({
    amount: tournament.entryFee,
    method: payload.paymentMethod,
    metadata: { tournamentId: tournament.id, userId: req.user.id },
  });
  addPayment(payment);

  const registration = {
    id: uuid(),
    tournamentId: tournament.id,
    userId: req.user.id,
    playerName: payload.playerName,
    email: payload.email,
    contactNumber: payload.contactNumber,
    category: payload.category,
    paymentStatus: payment.status,
    paymentReference: payment.reference,
    createdAt: new Date().toISOString(),
  };

  addRegistration(registration);
  updateTournament(tournament.id, (current) => ({ registeredCount: current.registeredCount + 1 }));

  try {
    await syncRegistrationToZoho(registration, tournament);
  } catch (error) {
    console.error('Zoho sync failed', error.message);
  }

  return res.status(201).json({ registration, payment });
});

export default router;
