"""
Speed Analytics

Computes average road speed.
"""

from core.state.city_state import CityState
from core.models.road_analytics import RoadAnalytics


class SpeedAnalytics:

    @staticmethod
    def compute(
        city: CityState,
        analytics: dict[str, RoadAnalytics]
    ):

        for road in city.roads:

            if road.id not in analytics:
                continue

            analytics[road.id].mean_speed = road.mean_speed