import { Router } from 'express';
import { requireAuth } from '../middleware/auth.js';
import { listPayments, listTournaments } from '../data/store.js';

const router = Router();

router.get('/', requireAuth(['admin', 'facility']), (req, res) => {
  const payments = listPayments();
  if (req.user.role === 'facility') {
    const facilityTournamentIds = new Set(
      listTournaments()
        .filter((t) => t.facilityId === req.user.facilityId)
        .map((t) => t.id),
    );
    return res.json(payments.filter((payment) => facilityTournamentIds.has(payment.metadata?.tournamentId)));
  }
  return res.json(payments);
});

export default router;
