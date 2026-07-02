"""
Traffic Analytics Engine
"""

from core.models.road_analytics import RoadAnalytics
from core.state.traffic_state import TrafficState

from analytics.density import DensityAnalytics
from analytics.vehicle_count import VehicleCountAnalytics
from analytics.speed import SpeedAnalytics
from analytics.occupancy import OccupancyAnalytics
from analytics.queue import QueueAnalytics
from analytics.waiting import WaitingAnalytics
from analytics.congestion import CongestionAnalytics

from analytics.arrival_rate import ArrivalRateAnalytics
from analytics.departure_rate import DepartureRateAnalytics
from analytics.throughput import ThroughputAnalytics
from analytics.stop_detection import StopDetectionAnalytics


class AnalyticsEngine:

    def compute(self, city, tracker=None):

        traffic = TrafficState()

        # ---------------------------------------
        # Create analytics object for every road
        # ---------------------------------------

        for road in city.roads:

            traffic.analytics[road.id] = RoadAnalytics(
                road_id=road.id
            )

        # ---------------------------------------
        # Current State Analytics
        # ---------------------------------------

        DensityAnalytics.compute(
            city,
            traffic.analytics
        )

        VehicleCountAnalytics.compute(
            city,
            traffic.analytics
        )

        SpeedAnalytics.compute(
            city,
            traffic.analytics
        )

        OccupancyAnalytics.compute(
            city,
            traffic.analytics
        )

        QueueAnalytics.compute(
            city,
            traffic.analytics
        )

        WaitingAnalytics.compute(
            city,
            traffic.analytics
        )

        CongestionAnalytics.compute(
            traffic.analytics
        )

        # ---------------------------------------
        # Temporal Analytics
        # ---------------------------------------

        if tracker is not None:

            ArrivalRateAnalytics.compute(
                city,
                traffic.analytics
            )

            DepartureRateAnalytics.compute(
                city,
                traffic.analytics
            )

            ThroughputAnalytics.compute(
                city,
                traffic.analytics
            )

            StopDetectionAnalytics.compute(
                city,
                traffic.analytics
            )

        return traffic