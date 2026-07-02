"""
Waiting Time Analytics

Computes average waiting time for every road.
"""

from core.state.city_state import CityState
from core.models.road_analytics import RoadAnalytics


class WaitingAnalytics:

    @staticmethod
    def compute(
        city: CityState,
        analytics: dict[str, RoadAnalytics]
    ):

        total_wait = {}
        vehicle_count = {}

        # Initialize
        for road in analytics:

            total_wait[road] = 0.0
            vehicle_count[road] = 0

        # Collect waiting times
        for vehicle in city.vehicles:

            road = vehicle.edge

            if road.startswith(":"):
                continue

            if road not in analytics:
                continue

            total_wait[road] += vehicle.waiting_time
            vehicle_count[road] += 1

        # Compute average
        for road in analytics:

            if vehicle_count[road] > 0:

                analytics[road].waiting_time = (
                    total_wait[road] /
                    vehicle_count[road]
                )

            else:

                analytics[road].waiting_time = 0.0