import { v4 as uuid } from 'uuid';

export const processPayment = async ({ amount, method, metadata }) => {
  // In production integrate with Razorpay/Stripe/etc.
  await new Promise((resolve) => setTimeout(resolve, 300));
  return {
    id: uuid(),
    status: 'paid',
    amount,
    method,
    reference: `PAY-${Date.now()}`,
    metadata,
    processedAt: new Date().toISOString(),
  };
};
