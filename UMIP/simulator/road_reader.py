"""
Road Reader

Reads road information from SUMO.
"""

import traci


class RoadReader:

    def read(self):

        roads = []

        for edge in traci.edge.getIDList():

            if edge.startswith(":"):
                continue

            lane_id = f"{edge}_0"

            roads.append({

                "id": edge,

                "from": traci.edge.getFromJunction(edge),

                "to": traci.edge.getToJunction(edge),

                "length": traci.lane.getLength(lane_id),

                "speed_limit": traci.lane.getMaxSpeed(lane_id),

                "lane_count": traci.edge.getLaneNumber(edge),

                "vehicle_count": traci.edge.getLastStepVehicleNumber(edge),

                "mean_speed": traci.edge.getLastStepMeanSpeed(edge),

                "occupancy": traci.edge.getLastStepOccupancy(edge),

            })

        return roads