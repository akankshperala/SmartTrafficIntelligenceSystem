"""
Vehicle Tracker

Tracks the last REAL road of every vehicle.
Internal SUMO edges (:) are ignored.
"""


class VehicleTracker:

    def __init__(self):

        self.previous_edges = {}

    def update(self, city):

        for vehicle in city.vehicles:

            edge = vehicle.edge

            # Ignore SUMO internal edges
            if edge.startswith(":"):
                continue

            self.previous_edges[vehicle.id] = edge

    def previous_edge(self, vehicle_id):

        return self.previous_edges.get(vehicle_id)