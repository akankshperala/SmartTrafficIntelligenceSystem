"""
Movement Model

Represents a traffic movement at a junction.
Example:
North -> South
West -> East
"""

from dataclasses import dataclass


@dataclass
class Movement:

    id: str

    junction_id: str

    from_road: str

    to_road: str

    vehicle_count: int

    average_speed: float

    average_waiting_time: float

    queue_length: int

    signal_phase: int

    def __str__(self):

        return (
            f"Movement("
            f"{self.from_road} -> {self.to_road}, "
            f"vehicles={self.vehicle_count}, "
            f"queue={self.queue_length}, "
            f"speed={self.average_speed:.2f})"
        )