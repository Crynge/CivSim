// CivSim Web Dashboard — 3D visualization and simulation control

import express from 'express';

const app = express();
app.use(express.json());

let simState = {
  running: false,
  tick: 0,
  agents: 100,
  fps: 60,
};

app.get('/api/v1/simulation/status', (_req, res) => {
  res.json(simState);
});

app.post('/api/v1/simulation/start', (_req, res) => {
  simState.running = true;
  res.json({ status: 'started' });
});

app.post('/api/v1/simulation/pause', (_req, res) => {
  simState.running = false;
  res.json({ status: 'paused' });
});

app.get('/api/v1/agents', (_req, res) => {
  const agents = Array.from({ length: simState.agents }, (_, i) => ({
    id: `agent-${i}`,
    name: `Citizen ${i}`,
    role: ['settler', 'trader', 'builder', 'farmer'][i % 4],
    position: [Math.random() * 100, Math.random() * 100],
    health: 80 + Math.random() * 20,
    energy: 60 + Math.random() * 40,
  }));
  res.json({ agents, total: agents.length });
});

app.get('/api/v1/analysis/emergence', (_req, res) => {
  res.json({
    events: [
      { type: 'role_specialization', tick: 340, p_value: 0.003, effect_size: 0.87 },
      { type: 'trade_network', tick: 520, p_value: 0.008, effect_size: 0.72 },
      { type: 'governance_formation', tick: 680, p_value: 0.002, effect_size: 0.93 },
    ],
  });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`CivSim Dashboard on http://localhost:${PORT}`);
});
