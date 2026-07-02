"""
Vehicle Model
"""

from dataclasses import dataclass


@dataclass
class Vehicle:
    id: str
    edge: str
    lane: str
    speed: float
    waiting_time: float
    position: tuple

    def __str__(self):

        return (
            f"Vehicle("
            f"id={self.id}, "
            f"edge={self.edge}, "
            f"lane={self.lane}, "
            f"speed={self.speed:.2f}, "
            f"waiting={self.waiting_time:.2f})"
        )