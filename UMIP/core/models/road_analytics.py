"""
Road Analytics Model

Stores all computed analytics for a single road.
"""

from dataclasses import dataclass


@dataclass
class RoadAnalytics:

    # Identity
    road_id: str

    # ------------------------
    # Traffic Metrics
    # ------------------------

    density: float = 0.0
    vehicle_count: int = 0
    mean_speed: float = 0.0
    occupancy: float = 0.0
    waiting_time: float = 0.0

    # ------------------------
    # Flow Metrics
    # ------------------------

    arrival_rate: float = 0.0
    departure_rate: float = 0.0
    throughput: float = 0.0

    # ------------------------
    # Behavior Metrics
    # ------------------------

    queue_length: int = 0
    stopped_vehicles: int = 0
    queue_growth: float = 0.0
    blocked: bool = False
    congestion_index: float = 0.0
    def __str__(self):

        return (
            f"RoadAnalytics(\n"
            f"  road={self.road_id},\n"
            f"  congestion={self.congestion_index:.2f},\n"
            f"  density={self.density:.4f},\n"
            f"  vehicles={self.vehicle_count},\n"
            f"  queue={self.queue_length},\n"
            f"  stopped={self.stopped_vehicles},\n"
            f"  waiting={self.waiting_time:.2f},\n"
            f"  speed={self.mean_speed:.2f},\n"
            f"  occupancy={self.occupancy:.2f},\n"
            f"  arrival={self.arrival_rate},\n"
            f"  departure={self.departure_rate},\n"
            f"  throughput={self.throughput},\n"
            f"  blocked={self.blocked}\n"
            f")"
        )