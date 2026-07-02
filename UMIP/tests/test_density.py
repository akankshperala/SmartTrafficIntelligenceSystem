from analytics.density import DensityAnalytics
from core.models.road import Road

road = Road(
    id="R1",
    from_junction="A",
    to_junction="B",
    length=300,
    lane_count=3,
    speed_limit=13.9,
    vehicle_count=18,
    mean_speed=9,
    occupancy=41
)

print(DensityAnalytics.compute(road))