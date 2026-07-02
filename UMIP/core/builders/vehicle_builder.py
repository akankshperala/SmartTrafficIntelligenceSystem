"""
Vehicle Builder
"""

from core.models.vehicle import Vehicle


class VehicleBuilder:

    def build(self, raw_vehicles):

        vehicles = []

        for v in raw_vehicles:

            vehicles.append(

                Vehicle(

                    id=v["id"],

                    edge=v["edge"],

                    lane=v["lane"],

                    speed=v["speed"],

                    waiting_time=v["waiting"],

                    position=v["position"]

                )

            )

        return vehicles