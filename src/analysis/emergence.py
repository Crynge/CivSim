"""Emergence detection using statistical change-point analysis."""

import numpy as np
from scipy import stats
from dataclasses import dataclass, field
from typing import List


@dataclass
class EmergenceEvent:
    type: str
    tick: int
    p_value: float
    effect_size: float
    description: str = ""


class EmergenceDetector:
    """Detect emergent behavior using Mann-Whitney U change-point detection."""

    def __init__(self, history: list):
        self.history = history
        self.window_size = 20

    def detect(self) -> List[EmergenceEvent]:
        events = []
        if len(self.history) < self.window_size * 2:
            return events

        for metric in ["agent_count"]:
            values = [s.get(metric, 0) for s in self.history]
            for i in range(self.window_size, len(values) - self.window_size):
                before = values[i - self.window_size:i]
                after = values[i:i + self.window_size]
                stat, p = stats.mannwhitneyu(before, after, alternative='two-sided')
                if p < 0.05:
                    events.append(EmergenceEvent(
                        type=f"change_{metric}",
                        tick=i,
                        p_value=p,
                        effect_size=abs(np.mean(after) - np.mean(before)) / (np.std(before) + 1e-8),
                    ))

        return events

    def specialization_index(self, agent_roles: list) -> float:
        """Calculate the Herfindahl-Hirschman Index for role specialization."""
        total = len(agent_roles)
        if total == 0:
            return 0.0
        counts = {}
        for role in agent_roles:
            counts[role] = counts.get(role, 0) + 1
        return sum((c / total) ** 2 for c in counts.values())
