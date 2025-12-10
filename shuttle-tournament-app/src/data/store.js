import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const dbPath = path.join(__dirname, 'db.json');

const readDb = () => {
  const raw = fs.readFileSync(dbPath, 'utf-8');
  return JSON.parse(raw);
};

const writeDb = (data) => {
  fs.writeFileSync(dbPath, JSON.stringify(data, null, 2));
};

export const getSnapshot = () => readDb();

export const findUserByEmail = (email) => {
  const db = readDb();
  return db.users.find((user) => user.email === email);
};

export const listTournaments = () => {
  const db = readDb();
  return db.tournaments;
};

export const findUserById = (id) => {
  const db = readDb();
  return db.users.find((user) => user.id === id);
};

export const addTournament = (tournament) => {
  const db = readDb();
  db.tournaments.push(tournament);
  writeDb(db);
  return tournament;
};

export const updateTournament = (tournamentId, updater) => {
  const db = readDb();
  const targetIndex = db.tournaments.findIndex((tour) => tour.id === tournamentId);
  if (targetIndex === -1) {
    throw new Error('Tournament not found');
  }
  const current = db.tournaments[targetIndex];
  const updates = updater(current) || {};
  db.tournaments[targetIndex] = {
    ...current,
    ...updates,
  };
  writeDb(db);
  return db.tournaments[targetIndex];
};

export const addRegistration = (registration) => {
  const db = readDb();
  db.registrations.push(registration);
  writeDb(db);
  return registration;
};

export const addPayment = (payment) => {
  const db = readDb();
  db.payments.push(payment);
  writeDb(db);
  return payment;
};

export const listRegistrations = () => {
  const db = readDb();
  return db.registrations;
};

export const listFacilities = () => {
  const db = readDb();
  return db.facilities;
};

export const listPayments = () => {
  const db = readDb();
  return db.payments;
};
