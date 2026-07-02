"""
Junction Model
"""

from dataclasses import dataclass


@dataclass
class Junction:

    id: str
    x: float
    y: float
    incoming_roads: list
    outgoing_roads: list

    def __str__(self):

        return (
            f"Junction("
            f"id={self.id}, "
            f"x={self.x:.1f}, "
            f"y={self.y:.1f}, "
            f"in={len(self.incoming_roads)}, "
            f"out={len(self.outgoing_roads)})"
        )