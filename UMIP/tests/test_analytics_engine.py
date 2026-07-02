from simulator.traci_manager import TraCIManager
from simulator.simulation import Simulation

from analytics.analytics_engine import AnalyticsEngine


manager = TraCIManager()

manager.start()

# Let vehicles enter the network
for _ in range(50):

    manager.step()

simulation = Simulation()

city = simulation.update()

engine = AnalyticsEngine()

traffic = engine.compute(city)

print()

print("=" * 80)

for road in traffic.analytics.values():

    if road.congestion_index > 0:

        print(road)

print("=" * 80)

manager.close()