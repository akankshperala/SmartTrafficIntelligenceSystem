"""
Queue Analytics

Computes queue length for every road.
"""

from core.state.city_state import CityState
from core.models.road_analytics import RoadAnalytics


class QueueAnalytics:

    # Vehicles below this speed are considered queued
    QUEUE_SPEED_THRESHOLD = 2.0  # m/s (~7.2 km/h)

    @staticmethod
    def compute(city: CityState,
                analytics: dict[str, RoadAnalytics]):

        # Reset queue counts
        for road_metrics in analytics.values():

            road_metrics.queue_length = 0
            road_metrics.stopped_vehicles = 0

        # Process every vehicle
        for vehicle in city.vehicles:

            road_id = vehicle.edge

            if road_id.startswith(":"):
                continue

            if road_id not in analytics:
                continue

            road_metrics = analytics[road_id]

            # Queue
            if vehicle.speed <= QueueAnalytics.QUEUE_SPEED_THRESHOLD:

                road_metrics.queue_length += 1

            # Completely stopped
            if vehicle.speed <= 0.1:

                road_metrics.stopped_vehicles += 1