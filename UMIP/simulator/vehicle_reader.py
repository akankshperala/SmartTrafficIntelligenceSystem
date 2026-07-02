"""
Vehicle Reader

Reads live vehicle information from SUMO.
"""

import traci


class VehicleReader:

    def read(self):

        vehicles = []

        for vehicle_id in traci.vehicle.getIDList():

            vehicles.append({

                "id": vehicle_id,

                "type": traci.vehicle.getTypeID(vehicle_id),

                "edge": traci.vehicle.getRoadID(vehicle_id),

                "lane": traci.vehicle.getLaneID(vehicle_id),

                "route": traci.vehicle.getRoute(vehicle_id),

                "speed": traci.vehicle.getSpeed(vehicle_id),

                "max_speed": traci.vehicle.getAllowedSpeed(vehicle_id),

                "waiting": traci.vehicle.getWaitingTime(vehicle_id),

                "position": traci.vehicle.getPosition(vehicle_id),

                "distance": traci.vehicle.getDistance(vehicle_id),

                "angle": traci.vehicle.getAngle(vehicle_id),

            })

        return vehicles