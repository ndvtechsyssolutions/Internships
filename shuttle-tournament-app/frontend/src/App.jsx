import { useEffect, useMemo, useState } from 'react';
import './App.css';
import { apiRequest, getApiBase } from './api';

const defaultTournamentForm = {
  name: '',
  sport: 'Badminton',
  level: 'Amateur',
  startDate: '',
  endDate: '',
  entryFee: 1500,
  maxPlayers: 32,
  facilityId: '',
};

const defaultRegistrationForm = {
  tournamentId: '',
  playerName: '',
  email: '',
  contactNumber: '',
  category: '',
  paymentMethod: 'upi',
};

function App() {
  const [auth, setAuth] = useState({ user: null, token: null });
  const [loginForm, setLoginForm] = useState({ email: '', password: '' });
  const [tournamentForm, setTournamentForm] = useState(defaultTournamentForm);
  const [registrationForm, setRegistrationForm] = useState(defaultRegistrationForm);
  const [tournaments, setTournaments] = useState([]);
  const [registrations, setRegistrations] = useState([]);
  const [payments, setPayments] = useState([]);
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState('');
  const [error, setError] = useState('');

  const isAdmin = auth.user?.role === 'admin';
  const isFacility = auth.user?.role === 'facility';

  const sortedTournaments = useMemo(
    () => [...tournaments].sort((a, b) => new Date(a.startDate) - new Date(b.startDate)),
    [tournaments],
  );

  useEffect(() => {
    if (auth.token) {
      fetchTournaments();
      if (isAdmin || isFacility) {
        fetchRegistrations();
        fetchPayments();
      }
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [auth.token, isAdmin, isFacility]);

  const fetchTournaments = async () => {
    try {
      const data = await apiRequest('/api/tournaments', { token: auth.token });
      setTournaments(data);
      if (!registrationForm.tournamentId && data.length) {
        setRegistrationForm((prev) => ({ ...prev, tournamentId: data[0].id }));
      }
    } catch (err) {
      console.error(err);
      setError(err.message);
    }
  };

  const fetchRegistrations = async () => {
    if (!auth.token) return;
    try {
      const data = await apiRequest('/api/registrations', { token: auth.token });
      setRegistrations(data);
    } catch (err) {
      console.error(err);
      setError(err.message);
    }
  };

  const fetchPayments = async () => {
    if (!auth.token) return;
    try {
      const data = await apiRequest('/api/payments', { token: auth.token });
      setPayments(data);
    } catch (err) {
      console.error(err);
      setError(err.message);
    }
  };

  const handleLogin = async (event) => {
    event.preventDefault();
    setLoading(true);
    setError('');
    setMessage('');
    try {
      const result = await apiRequest('/api/auth/login', {
        method: 'POST',
        body: { ...loginForm },
      });
      setAuth({ user: result.user, token: result.token });
      setMessage(`Welcome ${result.user.name}`);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleCreateTournament = async (event) => {
    event.preventDefault();
    setLoading(true);
    setError('');
    setMessage('');

    const payload = {
      ...tournamentForm,
      entryFee: Number(tournamentForm.entryFee),
      maxPlayers: Number(tournamentForm.maxPlayers),
    };

    try {
      await apiRequest('/api/tournaments', {
        method: 'POST',
        body: payload,
        token: auth.token,
      });
      setTournamentForm(defaultTournamentForm);
      setMessage('Tournament created');
      fetchTournaments();
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleRegister = async (event) => {
    event.preventDefault();
    setLoading(true);
    setError('');
    setMessage('');
    try {
      await apiRequest('/api/registrations', {
        method: 'POST',
        body: registrationForm,
        token: auth.token,
      });
      setRegistrationForm(defaultRegistrationForm);
      setMessage('Registration successful. Payment captured & synced to Zoho.');
      fetchTournaments();
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleStatusChange = async (tournamentId, status) => {
    setLoading(true);
    setError('');
    setMessage('');
    try {
      await apiRequest(`/api/tournaments/${tournamentId}/status`, {
        method: 'PATCH',
        body: { status },
        token: auth.token,
      });
      setMessage('Tournament status updated');
      fetchTournaments();
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const logout = () => {
    setAuth({ user: null, token: null });
    setRegistrations([]);
    setPayments([]);
    setTournaments([]);
    setMessage('');
    setError('');
  };

  if (!auth.token) {
    return (
      <main className="app-shell">
        <header>
          <h1>Shuttle Tournament Portal</h1>
          <p>Admin · Facility · Player workflows in one place</p>
        </header>
        <section className="panel">
          <h2>Login</h2>
          <p className="helper">Demo creds: admin@shuttlehq.io / admin123</p>
          <form onSubmit={handleLogin} className="form-grid">
            <label>
              Email
              <input
                type="email"
                value={loginForm.email}
                onChange={(e) => setLoginForm({ ...loginForm, email: e.target.value })}
                required
              />
            </label>
            <label>
              Password
              <input
                type="password"
                value={loginForm.password}
                onChange={(e) => setLoginForm({ ...loginForm, password: e.target.value })}
                required
              />
            </label>
            <button type="submit" disabled={loading}>
              {loading ? 'Logging in...' : 'Login'}
            </button>
          </form>
          {error && <p className="error">{error}</p>}
        </section>
      </main>
    );
  }

  return (
    <main className="app-shell">
      <header>
        <div>
          <h1>Shuttle Tournament Portal</h1>
          <p>
            Signed in as {auth.user?.name} ({auth.user?.role}) · API {getApiBase()}
          </p>
        </div>
        <button type="button" onClick={logout} className="text-button">
          Logout
        </button>
      </header>

      {(message || error) && (
        <div className={`toast ${message ? 'success' : 'error'}`}>{message || error}</div>
      )}

      <section className="grid">
        <div className="panel">
          <h2>Upcoming Tournaments</h2>
          <table>
            <thead>
              <tr>
                <th>Name</th>
                <th>Sport</th>
                <th>Level</th>
                <th>Dates</th>
                <th>Fee</th>
                <th>Slots</th>
                <th>Status</th>
                {(isAdmin || isFacility) && <th>Actions</th>}
              </tr>
            </thead>
            <tbody>
              {sortedTournaments.map((tournament) => (
                <tr key={tournament.id}>
                  <td>{tournament.name}</td>
                  <td>{tournament.sport}</td>
                  <td>{tournament.level}</td>
                  <td>
                    {tournament.startDate} → {tournament.endDate}
                  </td>
                  <td>₹{tournament.entryFee}</td>
                  <td>
                    {tournament.registeredCount}/{tournament.maxPlayers}
                  </td>
                  <td>{tournament.status}</td>
                  {(isAdmin || isFacility) && (
                    <td>
                      <select
                        onChange={(e) => handleStatusChange(tournament.id, e.target.value)}
                        defaultValue=""
                      >
                        <option value="" disabled>
                          Update
                        </option>
                        <option value="open">Open</option>
                        <option value="closed">Closed</option>
                        <option value="completed">Completed</option>
                        <option value="cancelled">Cancelled</option>
                      </select>
                    </td>
                  )}
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        {(isAdmin || isFacility) && (
          <div className="panel">
            <h2>Create Tournament</h2>
            {isAdmin && <p className="helper">Admins must pick a facility ID</p>}
            <form className="form-grid" onSubmit={handleCreateTournament}>
              <label>
                Name
                <input
                  value={tournamentForm.name}
                  onChange={(e) => setTournamentForm({ ...tournamentForm, name: e.target.value })}
                  required
                />
              </label>
              <label>
                Sport
                <select
                  value={tournamentForm.sport}
                  onChange={(e) => setTournamentForm({ ...tournamentForm, sport: e.target.value })}
                >
                  <option>Badminton</option>
                  <option>Pickleball</option>
                </select>
              </label>
              <label>
                Level
                <select
                  value={tournamentForm.level}
                  onChange={(e) => setTournamentForm({ ...tournamentForm, level: e.target.value })}
                >
                  <option>Beginner</option>
                  <option>Amateur</option>
                  <option>Professional</option>
                </select>
              </label>
              <label>
                Start Date
                <input
                  type="date"
                  value={tournamentForm.startDate}
                  onChange={(e) => setTournamentForm({ ...tournamentForm, startDate: e.target.value })}
                  required
                />
              </label>
              <label>
                End Date
                <input
                  type="date"
                  value={tournamentForm.endDate}
                  onChange={(e) => setTournamentForm({ ...tournamentForm, endDate: e.target.value })}
                  required
                />
              </label>
              <label>
                Entry Fee (₹)
                <input
                  type="number"
                  value={tournamentForm.entryFee}
                  onChange={(e) => setTournamentForm({ ...tournamentForm, entryFee: e.target.value })}
                  min={0}
                  required
                />
              </label>
              <label>
                Max Players
                <input
                  type="number"
                  value={tournamentForm.maxPlayers}
                  onChange={(e) => setTournamentForm({ ...tournamentForm, maxPlayers: e.target.value })}
                  min={2}
                  required
                />
              </label>
              {isAdmin && (
                <label>
                  Facility Id
                  <input
                    value={tournamentForm.facilityId}
                    onChange={(e) => setTournamentForm({ ...tournamentForm, facilityId: e.target.value })}
                    required
                  />
                </label>
              )}
              <button type="submit" disabled={loading}>
                {loading ? 'Saving...' : 'Create Tournament'}
              </button>
            </form>
          </div>
        )}

        {auth.user?.role === 'user' && (
          <div className="panel">
            <h2>Register & Pay</h2>
            <form className="form-grid" onSubmit={handleRegister}>
              <label>
                Tournament
                <select
                  value={registrationForm.tournamentId}
                  onChange={(e) =>
                    setRegistrationForm({ ...registrationForm, tournamentId: e.target.value })
                  }
                  required
                >
                  <option value="" disabled>
                    Choose
                  </option>
                  {sortedTournaments
                    .filter((t) => t.status === 'open')
                    .map((tournament) => (
                      <option key={tournament.id} value={tournament.id}>
                        {tournament.name} · ₹{tournament.entryFee}
                      </option>
                    ))}
                </select>
              </label>
              <label>
                Player Name
                <input
                  value={registrationForm.playerName}
                  onChange={(e) => setRegistrationForm({ ...registrationForm, playerName: e.target.value })}
                  required
                />
              </label>
              <label>
                Email
                <input
                  type="email"
                  value={registrationForm.email}
                  onChange={(e) => setRegistrationForm({ ...registrationForm, email: e.target.value })}
                  required
                />
              </label>
              <label>
                Contact Number
                <input
                  value={registrationForm.contactNumber}
                  onChange={(e) =>
                    setRegistrationForm({ ...registrationForm, contactNumber: e.target.value })
                  }
                  required
                />
              </label>
              <label>
                Category
                <input
                  value={registrationForm.category}
                  onChange={(e) => setRegistrationForm({ ...registrationForm, category: e.target.value })}
                  placeholder="e.g. Men's Doubles"
                  required
                />
              </label>
              <label>
                Payment Method
                <select
                  value={registrationForm.paymentMethod}
                  onChange={(e) =>
                    setRegistrationForm({ ...registrationForm, paymentMethod: e.target.value })
                  }
                  required
                >
                  <option value="upi">UPI</option>
                  <option value="card">Card</option>
                  <option value="cash">Cash</option>
                </select>
              </label>
              <button type="submit" disabled={loading}>
                {loading ? 'Processing...' : 'Pay & Register'}
              </button>
            </form>
          </div>
        )}

        {(isAdmin || isFacility) && (
          <div className="panel">
            <h2>Recent Registrations</h2>
            <table>
              <thead>
                <tr>
                  <th>Player</th>
                  <th>Tournament</th>
                  <th>Category</th>
                  <th>Payment</th>
                </tr>
              </thead>
              <tbody>
                {registrations.map((registration) => {
                  const tournament = tournaments.find((t) => t.id === registration.tournamentId);
                  return (
                    <tr key={registration.id}>
                      <td>{registration.playerName}</td>
                      <td>{tournament?.name || registration.tournamentId}</td>
                      <td>{registration.category}</td>
                      <td>{registration.paymentStatus}</td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
        )}

        {(isAdmin || isFacility) && (
          <div className="panel">
            <h2>Payments</h2>
            <table>
              <thead>
                <tr>
                  <th>Reference</th>
                  <th>Amount</th>
                  <th>Method</th>
                  <th>Status</th>
                </tr>
              </thead>
              <tbody>
                {payments.map((payment) => (
                  <tr key={payment.id}>
                    <td>{payment.reference}</td>
                    <td>₹{payment.amount}</td>
                    <td>{payment.method}</td>
                    <td>{payment.status}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </section>
    </main>
  );
}

export default App;
