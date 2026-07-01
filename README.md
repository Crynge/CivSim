[![CI](https://github.com/Crynge/CivSim/actions/workflows/ci.yml/badge.svg)](https://github.com/Crynge/CivSim/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-purple)](LICENSE)

# CivSim

**Multi-agent civilization simulation for emergent social behavior.**

In the beginning, there were agents. They traded, governed, built cultures, and sometimes went to war. CivSim is a generative agent framework that simulates entire societies to study how norms, governance, and civilization emerge from simple rules.

---

## The World

```
                              ╱  Trade Routes  ╲
                            ╱                    ╲
                  ┌───────▼──┐              ┌───────▼──┐
                  │  Hamlet  │◄────────────►│  Village │
                  │  (pop 8) │   Resource    │ (pop 15) │
                  └───────┬──┘   Exchange    └───────┬──┘
                          │                          │
                    ╱─────┼─────╲              ╱─────┼─────╲
                  ╱       │       ╲          ╱       │       ╲
         ┌───────▼──┐    ╱         ╲ ┌───────▼──┐    ╱         ╲
         │  Market  │  ╱  Conflict  ╲ │  Temple  │  ╱  Alliance   ╲
         │ Square   │◀╲   Zone      ╱►│  (faith  │◀╲   Treaty     ╱►
         └──────────┘  ╲            ╱  └──────────┘  ╲            ╱
                        ╲──────────╱                  ╲──────────╱
```

## What Can Emerge?

| Phenomenon | Description | Observed? |
|---|---|---|
| Trade networks | Agents specialize and exchange resources | ✅ |
| Social hierarchy | Status differentiation through wealth accumulation | ✅ |
| Legal systems | Codified rules enforced by collective punishment | ⚠️ Partial |
| Religious institutions | Shared beliefs that influence economic decisions | ✅ |
| Democratic governance | Voting on resource allocation and leadership | ⚠️ Partial |
| Warfare | Coordinated conflict over territory | ✅ |

## Quick Start

```bash
pip install civsim

# Run a basic simulation
civsim run --world-size 50 --agents 200 --steps 1000

# Headless mode (no UI)
civsim run --headless --output results.json

# Web dashboard
civsim dashboard --port 5000
```

```python
from civsim.simulation import World

world = World(
    width=100, height=100,
    agents=500,
    resources=["food", "wood", "gold", "iron"],
    seed=42,
)

for epoch in range(100):
    world.step()
    if epoch % 10 == 0:
        print(f"Epoch {epoch}: {world.report()}")
```

## Modules

```
src/
├── simulation/
│   └── core.py           # World engine and step loop
├── agents/
│   ├── base.py           # Agent physiology and needs
│   └── governance.py     # Collective decision-making
├── analysis/
│   └── emergence.py      # Pattern detection in simulation data
├── api/
│   └── server.go         # Go-based simulation API
└── web/
    └── server.ts         # TypeScript dashboard server
```

## Analysis

```python
from civsim.analysis.emergence import detect_patterns

patterns = detect_patterns(world.history)
for p in patterns:
    print(f"{p.type}: significance={p.score:.2f}, since_step={p.since}")
```

## Visualization

Start the web dashboard for real-time 3D visualization of agent movement, resource flows, and emergent structures.
