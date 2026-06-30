"""Governance systems — proposal, voting, ratification."""

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class Proposal:
    id: str
    title: str
    description: str
    proposer: str
    votes: Dict[str, bool] = field(default_factory=dict)
    ratified: bool = False


class GovernanceSystem:
    """PBFT-style consensus protocol for agent governance."""

    def __init__(self, civilization):
        self.civ = civilization
        self.proposals: List[Proposal] = []
        self._counter = 0

    def propose(self, title: str, description: str) -> Proposal:
        self._counter += 1
        proposal = Proposal(
            id=f"prop-{self._counter}",
            title=title,
            description=str(description),
            proposer="system",
        )
        self.proposals.append(proposal)
        return proposal

    def vote(self, proposal_id: str, votes: Dict[str, bool]) -> Dict[str, bool]:
        proposal = next(p for p in self.proposals if p.id == proposal_id)
        proposal.votes.update(votes)
        return votes

    def ratify(self, proposal_id: str) -> bool:
        proposal = next(p for p in self.proposals if p.id == proposal_id)
        votes = list(proposal.votes.values())
        if len(votes) == 0:
            return False
        approval = sum(votes) / len(votes)
        proposal.ratified = approval > 0.5
        return proposal.ratified
