"""Core simulation engine with async agent lifecycle."""

from dataclasses import dataclass, field
from typing import Optional
import asyncio
import time


@dataclass
class SimulationConfig:
    num_agents: int = 100
    world_size: tuple = (100, 100)
    tick_interval_ms: int = 50
    max_ticks: int = 1000
    seed: Optional[int] = None


class Civilization:
    """Main simulation orchestrator."""

    def __init__(self, config: SimulationConfig):
        self.config = config
        self.agents = {}
        self.history = []
        self.current_tick = 0
        self.running = False

    def add_agent(self, agent):
        self.agents[agent.agent_id] = agent

    def population_snapshot(self) -> dict:
        return {
            "tick": self.current_tick,
            "agents": [
                {"id": a.agent_id, "name": a.name, "role": a.role, "position": list(a.position) if hasattr(a, 'position') else [0, 0]}
                for a in self.agents.values()
            ],
            "agent_count": len(self.agents),
        }

    def run(self):
        """Generator-based simulation loop."""
        self.running = True
        while self.current_tick < self.config.max_ticks and self.running:
            self.current_tick += 1
            for agent in self.agents.values():
                if hasattr(agent, 'tick'):
                    agent.tick()
            self.history.append(self.population_snapshot())
            yield self.current_tick

    def stop(self):
        self.running = False
