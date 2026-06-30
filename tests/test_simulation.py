"""Tests for CivSim core simulation."""

import pytest
from civsim import Civilization, SimulationConfig
from civsim.agents.base import AgentCore, MemoryStore


class TestCivilization:
    def test_create_with_config(self):
        config = SimulationConfig(num_agents=10, max_ticks=5)
        civ = Civilization(config)
        assert civ.config.num_agents == 10

    def test_add_agent(self):
        config = SimulationConfig(num_agents=1, max_ticks=5)
        civ = Civilization(config)
        agent = AgentCore("test-1", "Test Agent", "settler")
        civ.add_agent(agent)
        assert len(civ.agents) == 1

    def test_run_simulation(self):
        config = SimulationConfig(num_agents=5, max_ticks=10)
        civ = Civilization(config)
        for i in range(5):
            civ.add_agent(AgentCore(f"agent-{i}", f"Agent {i}", "settler"))
        ticks = list(civ.run())
        assert len(ticks) == 10


class TestMemoryStore:
    def test_remember_and_recall(self):
        mem = MemoryStore()
        mem.remember({"type": "gather", "resource": "food"})
        mem.remember({"type": "trade", "resource": "gold"})
        results = mem.recall("food")
        assert len(results) == 1

    def test_reflect(self):
        mem = MemoryStore()
        for _ in range(30):
            mem.remember({"type": "gather"})
        mem.reflect()
        assert len(mem.semantic) > 0
