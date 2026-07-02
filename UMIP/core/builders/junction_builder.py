"""
Junction Builder
"""

from core.models.junction import Junction


class JunctionBuilder:

    def build(self, raw_junctions):

        junctions = []

        for j in raw_junctions:

            junctions.append(

                Junction(

                    id=j["id"],

                    x=j["x"],

                    y=j["y"],

                    incoming_roads=j["incoming"],

                    outgoing_roads=j["outgoing"]

                )

            )

        return junctions