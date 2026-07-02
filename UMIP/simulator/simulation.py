"""
Simulation

Coordinates the complete simulation update cycle.

Pipeline:

TraCI
    ↓
Readers
    ↓
Builders
    ↓
RawState
    ↓
CityBuilder
    ↓
CityState
"""

from core.state.raw_state import RawState

from core.builders.city_builder import CityBuilder

from simulator.vehicle_reader import VehicleReader
from simulator.road_reader import RoadReader
from simulator.signal_reader import SignalReader
from simulator.junction_reader import JunctionReader

from core.builders.vehicle_builder import VehicleBuilder
from core.builders.road_builder import RoadBuilder
from core.builders.signal_builder import SignalBuilder
from core.builders.junction_builder import JunctionBuilder
from core.builders.approach_builder import ApproachBuilder
from core.builders.movement_builder import MovementBuilder


class Simulation:

    def __init__(self):

        # Readers
        self.vehicle_reader = VehicleReader()
        self.road_reader = RoadReader()
        self.signal_reader = SignalReader()
        self.junction_reader = JunctionReader()

        # Builders
        self.vehicle_builder = VehicleBuilder()
        self.road_builder = RoadBuilder()
        self.signal_builder = SignalBuilder()
        self.junction_builder = JunctionBuilder()
        self.approach_builder = ApproachBuilder()
        self.movement_builder = MovementBuilder()

        # Final City Builder
        self.city_builder = CityBuilder()

        self.current_step = 0

    def update(self):

        raw = RawState()

        # -----------------------------
        # Read data from SUMO
        # -----------------------------
        vehicle_data = self.vehicle_reader.read()
        road_data = self.road_reader.read()
        signal_data = self.signal_reader.read()
        junction_data = self.junction_reader.read()

        # -----------------------------
        # Build domain models
        # -----------------------------
        raw.vehicles = self.vehicle_builder.build(vehicle_data)

        raw.roads = self.road_builder.build(road_data)

        raw.signals = self.signal_builder.build(signal_data)

        raw.junctions = self.junction_builder.build(junction_data)

        raw.approaches = self.approach_builder.build(
            raw.roads,
            raw.vehicles,
            raw.signals,
        )

        raw.movements = self.movement_builder.build(
            raw.approaches
        )

        # -----------------------------
        # Build CityState
        # -----------------------------
        city = self.city_builder.build(raw)

        city.current_step = self.current_step
        city.simulation_time = self.current_step

        self.current_step += 1

        return city