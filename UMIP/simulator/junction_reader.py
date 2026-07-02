"""
Junction Reader

Reads junction information from SUMO.
"""

import traci


class JunctionReader:

    def read(self):

        junctions = []

        for junction_id in traci.junction.getIDList():

            x, y = traci.junction.getPosition(junction_id)

            junctions.append({

                "id": junction_id,

                "x": x,

                "y": y,

                "incoming": traci.junction.getIncomingEdges(junction_id),

                "outgoing": traci.junction.getOutgoingEdges(junction_id),

            })

        return junctions