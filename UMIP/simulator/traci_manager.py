"""
TraCI Manager

Responsible for:
- Starting SUMO
- Managing the TraCI connection
- Advancing the simulation
- Closing SUMO safely

This is the only class that should communicate directly with TraCI.
"""

import traci

from simulator.config import SUMO_GUI, SUMO_CONFIG


class TraCIManager:

    def __init__(self):
        binary = "sumo-gui" if SUMO_GUI else "sumo"

        self.cmd = [
            binary,
            "-c",
            SUMO_CONFIG,
        ]

        self.connected = False

    def start(self):
        """
        Start the SUMO simulation.
        """

        if self.connected:
            print("TraCI is already connected.")
            return

        try:
            traci.start(self.cmd)
            self.connected = True
            print("✓ Connected to SUMO")

        except Exception as e:
            print(f"Failed to start SUMO: {e}")
            raise

    def step(self):
        """
        Advance the simulation by one step.
        """

        if not self.connected:
            raise RuntimeError("TraCI is not connected.")

        traci.simulationStep()

    def running(self):
        """
        Returns True while vehicles remain in the simulation.
        """

        if not self.connected:
            return False

        return traci.simulation.getMinExpectedNumber() > 0

    def close(self):
        """
        Close the TraCI connection safely.
        """

        if not self.connected:
            return

        try:
            traci.close()
            print("✓ SUMO closed successfully")

        finally:
            self.connected = False