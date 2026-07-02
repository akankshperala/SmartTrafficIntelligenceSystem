"""
Throughput Analytics
"""


class ThroughputAnalytics:

    @staticmethod
    def compute(city, analytics):

        for road in analytics.values():

            road.throughput = road.departure_rate