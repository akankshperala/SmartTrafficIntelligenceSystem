"""
Raw Simulation State
"""

from dataclasses import dataclass, field


@dataclass
class RawState:

    vehicles: list = field(default_factory=list)

    roads: list = field(default_factory=list)

    signals: list = field(default_factory=list)

    junctions: list = field(default_factory=list)

    approaches: list = field(default_factory=list)

    movements: list = field(default_factory=list)

    detectors: list = field(default_factory=list)