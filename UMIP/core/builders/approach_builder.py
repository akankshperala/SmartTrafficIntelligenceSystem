"""
Approach Builder
"""

from core.models.approach import Approach


class ApproachBuilder:

    def build(self, roads, vehicles, signals):

        approaches = []

        signal_map = {}

        for signal in signals:

            signal_map[signal.id] = signal.phase

        for road in roads:

            road_vehicles = []

            for vehicle in vehicles:

                if vehicle.edge == road.id:

                    road_vehicles.append(vehicle)

            vehicle_count = len(road_vehicles)

            if vehicle_count == 0:

                avg_speed = 0

                avg_wait = 0

                queue = 0

            else:

                avg_speed = sum(v.speed for v in road_vehicles) / vehicle_count

                avg_wait = sum(v.waiting_time for v in road_vehicles) / vehicle_count

                queue = len([v for v in road_vehicles if v.speed < 0.5])

            approaches.append(

                Approach(

                    id=road.id,

                    junction_id=road.to_junction,

                    road_id=road.id,

                    direction="UNKNOWN",

                    vehicle_count=vehicle_count,

                    average_speed=avg_speed,

                    average_waiting_time=avg_wait,

                    queue_length=queue,

                    signal_phase=signal_map.get(road.to_junction, -1)

                )

            )

        return approaches