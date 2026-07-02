"""
Signal Model
"""

from dataclasses import dataclass


@dataclass
class Signal:

    id: str
    phase: int
    phase_name: str
    duration: float
    controlled_lanes: list

    def __str__(self):

        return (
            f"Signal("
            f"id={self.id}, "
            f"phase={self.phase}, "
            f"duration={self.duration}, "
            f"lanes={len(self.controlled_lanes)})"
        )