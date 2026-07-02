"""
Arrival Rate Analytics
"""

import traci


class ArrivalRateAnalytics:

    @staticmethod
    def compute(city, analytics):

        for road in analytics.values():
            road.arrival_rate = 0

        for edge in traci.edge.getIDList():

            if edge.startswith(":"):
                continue

            if edge not in analytics:
                continue

            # Vehicles entering this edge during the last step
            analytics[edge].arrival_rate = len(
                traci.edge.getLastStepVehicleIDs(edge)
            )