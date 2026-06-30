"""Role emergence experiment — 60 agents with statistical significance."""

from civsim import Civilization, SimulationConfig, AgentCore


def main():
    config = SimulationConfig(
        num_agents=60,
        world_size=(100, 100),
        tick_interval_ms=50,
        max_ticks=1000,
    )

    civ = Civilization(config)

    roles = ["settler", "trader", "builder", "farmer", "explorer"]
    for i in range(config.num_agents):
        agent = AgentCore(
            agent_id=f"agent-{i}",
            name=f"Citizen {i}",
            role=roles[i % len(roles)],
        )
        civ.add_agent(agent)

    results = {"ticks": [], "specialization": []}
    for tick in civ.run():
        if tick % 50 == 0:
            snapshot = civ.population_snapshot()
            from civsim.analysis import EmergenceDetector
            detector = EmergenceDetector(civ.history)
            spec = detector.specialization_index([a["role"] for a in snapshot["agents"]])
            results["ticks"].append(tick)
            results["specialization"].append(spec)
            print(f"Tick {tick}: Specialization index = {spec:.4f}")

    print(f"\nExperiment complete. {config.num_agents} agents, {config.max_ticks} ticks.")
    print(f"Final specialization index: {results['specialization'][-1]:.4f}")


if __name__ == "__main__":
    main()
