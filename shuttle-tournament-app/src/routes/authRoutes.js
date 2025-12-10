import { Router } from 'express';
import { z } from 'zod';
import { findUserByEmail } from '../data/store.js';
import { encodeToken } from '../utils/token.js';
import { requireAuth } from '../middleware/auth.js';

const router = Router();

const loginSchema = z.object({
  email: z.string().email(),
  password: z.string().min(4),
});

router.post('/login', (req, res) => {
  const parseResult = loginSchema.safeParse(req.body);
  if (!parseResult.success) {
    return res.status(400).json({ message: 'Invalid credentials payload', issues: parseResult.error.flatten() });
  }

  const { email, password } = parseResult.data;
  const user = findUserByEmail(email);

  if (!user || user.password !== password) {
    return res.status(401).json({ message: 'Invalid email or password' });
  }

  const token = encodeToken({ id: user.id, role: user.role, name: user.name, facilityId: user.facilityId });
  return res.json({
    token,
    user: {
      id: user.id,
      role: user.role,
      name: user.name,
      email: user.email,
      facilityId: user.facilityId,
    },
  });
});

router.get('/me', requireAuth(), (req, res) => {
  res.json({ user: req.user });
});

export default router;
