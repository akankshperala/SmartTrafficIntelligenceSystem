"""
Congestion Analytics

Computes a congestion index between 0 and 1.
"""

from core.models.road_analytics import RoadAnalytics


class CongestionAnalytics:

    @staticmethod
    def compute(
        analytics: dict[str, RoadAnalytics]
    ):

        for road in analytics.values():

            density_score = min(road.density * 200, 1.0)

            queue_score = min(road.queue_length / 20, 1.0)

            waiting_score = min(road.waiting_time / 30, 1.0)

            speed_score = 1.0 - min(road.mean_speed / 13.89, 1.0)

            road.congestion_index = (

                0.35 * density_score +

                0.30 * queue_score +

                0.20 * waiting_score +

                0.15 * speed_score

            )