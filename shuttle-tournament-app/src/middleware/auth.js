import { decodeToken } from '../utils/token.js';

export const requireAuth = (allowedRoles = []) => (req, res, next) => {
  const header = req.headers.authorization || '';
  const token = header.replace('Bearer ', '').trim();
  const payload = decodeToken(token);

  if (!payload) {
    return res.status(401).json({ message: 'Unauthorized' });
  }

  if (allowedRoles.length && !allowedRoles.includes(payload.role)) {
    return res.status(403).json({ message: 'Forbidden' });
  }

  req.user = payload;
  return next();
};
