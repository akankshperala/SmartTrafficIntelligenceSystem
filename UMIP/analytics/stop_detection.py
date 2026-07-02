"""
Stop Detection Analytics
"""


class StopDetectionAnalytics:

    STOP_TIME_THRESHOLD = 30.0

    @staticmethod
    def compute(city, analytics):

        for road in analytics.values():

            road.blocked = False

        for vehicle in city.vehicles:

            if vehicle.waiting_time >= StopDetectionAnalytics.STOP_TIME_THRESHOLD:

                if vehicle.edge in analytics:

                    analytics[vehicle.edge].blocked = True