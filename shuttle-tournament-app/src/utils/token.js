import crypto from 'crypto';

const secret = process.env.APP_TOKEN_SECRET || 'shuttle-secret';

const base64Url = (input) => Buffer.from(input).toString('base64url');
const fromBase64Url = (input) => Buffer.from(input, 'base64url').toString('utf-8');

export const encodeToken = (payload) => {
  const header = base64Url(JSON.stringify({ alg: 'HS256', typ: 'JWT-lite' }));
  const body = base64Url(JSON.stringify(payload));
  const signature = crypto.createHmac('sha256', secret).update(`${header}.${body}`).digest('base64url');
  return `${header}.${body}.${signature}`;
};

export const decodeToken = (token) => {
  if (!token) return null;
  const [header, body, signature] = token.split('.');
  if (!header || !body || !signature) return null;
  const expected = crypto.createHmac('sha256', secret).update(`${header}.${body}`).digest('base64url');
  if (expected !== signature) return null;
  try {
    return JSON.parse(fromBase64Url(body));
  } catch (error) {
    return null;
  }
};
