"""
Movement Builder
"""

from core.models.movement import Movement


class MovementBuilder:

    def build(self, approaches):

        movements = []

        for approach in approaches:

            movements.append(

                Movement(

                    id=approach.id,

                    junction_id=approach.junction_id,

                    from_road=approach.road_id,

                    to_road="UNKNOWN",

                    vehicle_count=approach.vehicle_count,

                    average_speed=approach.average_speed,

                    average_waiting_time=approach.average_waiting_time,

                    queue_length=approach.queue_length,

                    signal_phase=approach.signal_phase

                )

            )

        return movements