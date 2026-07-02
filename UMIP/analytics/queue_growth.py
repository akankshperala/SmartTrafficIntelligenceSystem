"""
Queue Growth Analytics
"""


class QueueGrowthAnalytics:

    @staticmethod
    def compute(analytics, previous_analytics):

        if previous_analytics is None:
            return

        for road_id, road in analytics.items():

            if road_id not in previous_analytics:
                continue

            road.queue_growth = (

                road.queue_length -

                previous_analytics[road_id].queue_length

            )