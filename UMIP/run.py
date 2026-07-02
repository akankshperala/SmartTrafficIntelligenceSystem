"""
UMIP Entry Point
"""

from pathlib import Path
import subprocess
import sys

from simulator.traci_manager import TraCIManager
from simulator.simulation import Simulation
from core.cache.vehicle_tracker import VehicleTracker
from analytics.analytics_engine import AnalyticsEngine


def generate_routes():

    script = (
        Path(__file__).parent
        / "network"
        / "maps"
        / "grid_3x3"
        / "scripts"
        / "generate_routes.py"
    )

    print("=" * 80)
    print("Generating Routes...")
    print("=" * 80)

    subprocess.run(
        [sys.executable, str(script)],
        check=True
    )


def main():

    print("=" * 80)
    print("UMIP")
    print("=" * 80)

    generate_routes()

    manager = TraCIManager()

    simulation = Simulation()

    analytics = AnalyticsEngine()

    tracker = VehicleTracker()
    try:

        manager.start()

        print("\n✓ SUMO Started\n")

        first_step = True

        while manager.running():

            manager.step()

            city = simulation.update()

            traffic = analytics.compute(
                city,
                tracker
            )

            tracker.update(city)

            if first_step:

                print("✓ First simulation step completed")

                first_step = False

            if city.current_step % 50 == 0:

                print("=" * 80)

                print(f"Simulation Step : {city.current_step}")

                print(city)

                print()

                print("=" * 80)
                print("Top 5 Congested Roads")
                print("=" * 80)

                top_roads = sorted(
                    traffic.analytics.values(),
                    key=lambda road: road.congestion_index,
                    reverse=True
                )

                for road in top_roads[:5]:

                    print(road)

                print("=" * 80)

    finally:

        manager.close()

        print("\nSimulation Finished")


if __name__ == "__main__":
    main()