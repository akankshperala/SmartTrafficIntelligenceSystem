"""
Approach Model

Represents one incoming way of a junction.
"""

from dataclasses import dataclass


@dataclass
class Approach:

    id: str

    junction_id: str

    road_id: str

    direction: str

    vehicle_count: int

    average_speed: float

    average_waiting_time: float

    queue_length: int

    signal_phase: int

    def __str__(self):

        return (
            f"Approach("
            f"{self.id}, "
            f"vehicles={self.vehicle_count}, "
            f"queue={self.queue_length}, "
            f"speed={self.average_speed:.2f})"
        )