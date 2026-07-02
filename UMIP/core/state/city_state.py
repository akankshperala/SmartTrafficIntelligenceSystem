"""
City State

Represents the complete digital twin of the traffic network.
"""

from dataclasses import dataclass, field


@dataclass
class CityState:

    vehicles: list = field(default_factory=list)

    roads: list = field(default_factory=list)

    signals: list = field(default_factory=list)

    junctions: list = field(default_factory=list)

    approaches: list = field(default_factory=list)

    movements: list = field(default_factory=list)

    current_step: int = 0

    simulation_time: float = 0.0

    def __str__(self):

        return (
            f"CityState("
            f"vehicles={len(self.vehicles)}, "
            f"roads={len(self.roads)}, "
            f"signals={len(self.signals)}, "
            f"junctions={len(self.junctions)}, "
            f"approaches={len(self.approaches)}, "
            f"movements={len(self.movements)})"
        )