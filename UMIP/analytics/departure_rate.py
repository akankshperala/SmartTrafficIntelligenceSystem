"""
Departure Rate Analytics
"""

import traci


class DepartureRateAnalytics:

    @staticmethod
    def compute(city, analytics):

        for road in analytics.values():
            road.departure_rate = 0

        for edge in traci.edge.getIDList():

            if edge.startswith(":"):
                continue

            if edge not in analytics:
                continue

            # Approximation: vehicles present on the edge this step
            analytics[edge].departure_rate = traci.edge.getLastStepVehicleNumber(edge)