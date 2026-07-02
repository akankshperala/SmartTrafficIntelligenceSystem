"""
Incident Model
"""

from dataclasses import dataclass


@dataclass
class Incident:

    id: str

    type: str

    road_id: str

    severity: str

    confidence: float

    description: str

    timestamp: float

    resolved: bool = False

    def __str__(self):

        return (
            f"Incident(\n"
            f"  id={self.id},\n"
            f"  type={self.type},\n"
            f"  road={self.road_id},\n"
            f"  severity={self.severity},\n"
            f"  confidence={self.confidence:.2f},\n"
            f"  resolved={self.resolved}\n"
            f")"
        )