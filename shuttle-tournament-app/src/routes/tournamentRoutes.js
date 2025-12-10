import { Router } from 'express';
import { z } from 'zod';
import { v4 as uuid } from 'uuid';
import { listTournaments, addTournament, updateTournament } from '../data/store.js';
import { requireAuth } from '../middleware/auth.js';

const router = Router();

const tournamentSchema = z.object({
  name: z.string().min(3),
  sport: z.string().default('Badminton'),
  level: z.enum(['Beginner', 'Amateur', 'Professional']).default('Amateur'),
  startDate: z.string(),
  endDate: z.string(),
  entryFee: z.number().int().nonnegative(),
  maxPlayers: z.number().int().positive(),
  facilityId: z.string().optional(),
});

const statusSchema = z.object({
  status: z.enum(['open', 'closed', 'completed', 'cancelled']),
});

router.get('/', requireAuth(['admin', 'facility', 'user']), (req, res) => {
  const tournaments = listTournaments();
  if (req.user.role === 'facility') {
    return res.json(tournaments.filter((t) => t.facilityId === req.user.facilityId));
  }
  return res.json(tournaments);
});

router.post('/', requireAuth(['admin', 'facility']), (req, res) => {
  const parseResult = tournamentSchema.safeParse(req.body);
  if (!parseResult.success) {
    return res.status(400).json({ message: 'Invalid payload', issues: parseResult.error.flatten() });
  }

  const payload = parseResult.data;
  const facilityId = req.user.role === 'facility' ? req.user.facilityId : payload.facilityId;
  if (!facilityId) {
    return res.status(400).json({ message: 'facilityId is required for admin-created tournaments' });
  }

  const tournament = {
    id: uuid(),
    ...payload,
    facilityId,
    status: 'open',
    registeredCount: 0,
    createdBy: req.user.id,
    createdAt: new Date().toISOString(),
  };

  addTournament(tournament);
  return res.status(201).json(tournament);
});

router.patch('/:id/status', requireAuth(['admin', 'facility']), (req, res) => {
  const parseResult = statusSchema.safeParse(req.body);
  if (!parseResult.success) {
    return res.status(400).json({ message: 'Invalid status payload', issues: parseResult.error.flatten() });
  }

  try {
    const updated = updateTournament(req.params.id, () => ({ status: parseResult.data.status }));
    return res.json(updated);
  } catch (error) {
    return res.status(404).json({ message: error.message });
  }
});

export default router;
