"""
Density Analytics

Computes road density for every road in the city.
"""

from core.state.city_state import CityState
from core.models.road_analytics import RoadAnalytics


class DensityAnalytics:

    @staticmethod
    def compute(city: CityState, analytics: dict[str, RoadAnalytics]):

        for road in city.roads:

            if road.id not in analytics:

                analytics[road.id] = RoadAnalytics(
                    road_id=road.id
                )

            road_metrics = analytics[road.id]

            road_metrics.vehicle_count = road.vehicle_count

            road_metrics.mean_speed = road.mean_speed

            road_metrics.occupancy = road.occupancy

            if road.length <= 0 or road.lane_count <= 0:

                road_metrics.density = 0.0

            else:

                road_metrics.density = (

                    road.vehicle_count /

                    (road.length * road.lane_count)

                )