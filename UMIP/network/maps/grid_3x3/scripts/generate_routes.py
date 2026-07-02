"""
Generate routes for the current SUMO network.
"""

from pathlib import Path
import subprocess
import os
import sys

# grid_3x3 folder
ROOT = Path(__file__).resolve().parent.parent

NETWORK = ROOT / "generated" / "network.net.xml"

ROUTES_DIR = ROOT / "routes"
ROUTES_DIR.mkdir(exist_ok=True)

TRIPS = ROUTES_DIR / "trips.trips.xml"
ROUTES = ROUTES_DIR / "routes.rou.xml"


def get_sumo_home():

    sumo_home = os.environ.get("SUMO_HOME")

    if not sumo_home:
        raise RuntimeError("SUMO_HOME is not set.")

    return Path(sumo_home)


def generate():

    if not NETWORK.exists():
        raise FileNotFoundError(f"Network not found:\n{NETWORK}")

    sumo_home = get_sumo_home()

    random_trips = (
        sumo_home /
        "tools" /
        "randomTrips.py"
    )

    if not random_trips.exists():
        raise FileNotFoundError(
            f"randomTrips.py not found:\n{random_trips}"
        )

    print("=" * 60)
    print("Generating Routes...")
    print("=" * 60)

    subprocess.run(

        [

            sys.executable,

            str(random_trips),

            "-n",
            str(NETWORK),

            "-o",
            str(TRIPS),

            "-r",
            str(ROUTES),

            "--seed",
            "42",

            "--period",
            "2",

            "--fringe-factor",
            "5",

            "--validate"

        ],

        check=True

    )

    print("\n✓ Route generation complete")
    print(TRIPS)
    print(ROUTES)


if __name__ == "__main__":
    generate()