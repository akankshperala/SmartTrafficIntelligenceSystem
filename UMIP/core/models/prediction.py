"""
Prediction Model
"""

from dataclasses import dataclass


@dataclass
class Prediction:

    road_id: str

    predicted_density: float = 0.0

    predicted_queue: float = 0.0

    predicted_speed: float = 0.0

    predicted_travel_time: float = 0.0

    prediction_horizon: float = 60.0

    confidence: float = 0.0

    def __str__(self):

        return (
            f"Prediction(\n"
            f"  road={self.road_id},\n"
            f"  density={self.predicted_density:.2f},\n"
            f"  queue={self.predicted_queue:.2f},\n"
            f"  speed={self.predicted_speed:.2f},\n"
            f"  travel_time={self.predicted_travel_time:.2f},\n"
            f"  horizon={self.prediction_horizon:.0f}s,\n"
            f"  confidence={self.confidence:.2f}\n"
            f")"
        )