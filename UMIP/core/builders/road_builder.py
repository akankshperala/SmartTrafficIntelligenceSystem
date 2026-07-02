"""
Road Builder
"""

from core.models.road import Road


class RoadBuilder:

    def build(self, raw_roads):

        roads = []

        for road in raw_roads:

            roads.append(

                Road(

                    id=road["id"],

                    from_junction=road["from"],

                    to_junction=road["to"],

                    length=road["length"],

                    lane_count=road["lane_count"],

                    speed_limit=road["speed_limit"],

                    vehicle_count=road["vehicle_count"],

                    mean_speed=road["mean_speed"],

                    occupancy=road["occupancy"]

                )

            )

        return roads