"""
Signal Reader

Reads traffic light information from SUMO.
"""

import traci


class SignalReader:

    def read(self):

        signals = []

        for tls_id in traci.trafficlight.getIDList():

            signals.append({

                "id": tls_id,

                "phase": traci.trafficlight.getPhase(tls_id),

                "phase_name": traci.trafficlight.getPhaseName(tls_id),

                "duration": traci.trafficlight.getPhaseDuration(tls_id),

                "next_switch": traci.trafficlight.getNextSwitch(tls_id),

                "controlled_lanes": traci.trafficlight.getControlledLanes(tls_id),

                "controlled_links": traci.trafficlight.getControlledLinks(tls_id),

            })

        return signals