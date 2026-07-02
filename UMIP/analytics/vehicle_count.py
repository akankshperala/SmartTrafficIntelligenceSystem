"""
Vehicle Count Analytics
"""

from core.state.city_state import CityState
from core.models.road_analytics import RoadAnalytics


class VehicleCountAnalytics:

    @staticmethod
    def compute(
        city: CityState,
        analytics: dict[str, RoadAnalytics]
    ):

        for road in city.roads:

            if road.id not in analytics:
                continue

            analytics[road.id].vehicle_count = road.vehicle_count