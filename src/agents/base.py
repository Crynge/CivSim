"""Agent core — perceive-deliberate-act cycle with memory and social systems."""


class AgentCore:
    """Base agent class with perceive-deliberate-act lifecycle."""

    def __init__(self, agent_id: str, name: str, role: str = "settler"):
        self.agent_id = agent_id
        self.name = name
        self.role = role
        self.position = [0, 0]
        self.health = 100
        self.energy = 100
        self.age = 0
        self.memory = MemoryStore()
        self.relationships = {}
        self.beliefs = {}
        self.goals = []

    def perceive(self, env):
        return {}

    def deliberate(self, perception):
        return "idle"

    def act(self, action, env):
        pass

    def tick(self):
        self.age += 1
        self.energy = max(0, self.energy - 1)
        if self.energy < 20:
            self.health = max(0, self.health - 1)

    def __repr__(self):
        return f"<Agent {self.agent_id}: {self.name} ({self.role})>"


class MemoryStore:
    """Tiered memory: episodic, semantic, procedural."""

    def __init__(self):
        self.episodic = []  # Recent experiences
        self.semantic = {}  # Facts derived from reflection
        self.procedural = {}  # Skills

    def remember(self, experience: dict):
        self.episodic.append(experience)
        if len(self.episodic) > 100:
            self.episodic.pop(0)

    def reflect(self):
        if len(self.episodic) > 20:
            recent = self.episodic[-20:]
            themes = [e.get("type") for e in recent if e.get("type")]
            for theme in set(themes):
                count = themes.count(theme)
                if count > 5:
                    self.semantic[f"frequent_{theme}"] = {"theme": theme, "count": count}

    def recall(self, query: str) -> list:
        return [e for e in self.episodic if query in str(e)]
