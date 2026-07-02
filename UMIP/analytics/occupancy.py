"""
Occupancy Analytics

Computes lane occupancy.
"""

from core.state.city_state import CityState
from core.models.road_analytics import RoadAnalytics


class OccupancyAnalytics:

    @staticmethod
    def compute(
        city: CityState,
        analytics: dict[str, RoadAnalytics]
    ):

        for road in city.roads:

            if road.id not in analytics:
                continue

            analytics[road.id].occupancy = road.occupancy