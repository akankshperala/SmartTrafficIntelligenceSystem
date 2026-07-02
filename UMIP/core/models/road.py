"""
Road Model
"""

from dataclasses import dataclass


@dataclass
class Road:
    # Static properties
    id: str
    from_junction: str
    to_junction: str
    length: float
    lane_count: int
    speed_limit: float

    # Dynamic properties (updated every simulation step)
    vehicle_count: int
    mean_speed: float
    occupancy: float

    def __str__(self):

        return (
            f"Road(\n"
            f"  id={self.id},\n"
            f"  from={self.from_junction},\n"
            f"  to={self.to_junction},\n"
            f"  length={self.length:.2f},\n"
            f"  lanes={self.lane_count},\n"
            f"  speed_limit={self.speed_limit:.2f},\n"
            f"  vehicles={self.vehicle_count},\n"
            f"  mean_speed={self.mean_speed:.2f},\n"
            f"  occupancy={self.occupancy:.2f}%\n"
            f")"
        )