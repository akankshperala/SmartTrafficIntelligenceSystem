"""
City Builder
"""

from core.state.city_state import CityState


class CityBuilder:

    def build(self, raw_state):

        city = CityState()

        city.vehicles = raw_state.vehicles

        city.roads = raw_state.roads

        city.signals = raw_state.signals

        city.junctions = raw_state.junctions

        city.approaches = raw_state.approaches

        city.movements = raw_state.movements

        return city