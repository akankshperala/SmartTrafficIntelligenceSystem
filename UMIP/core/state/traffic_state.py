"""
Traffic State

Central state shared by the Analytics Engine
and LangGraph agents.
"""

from dataclasses import dataclass, field

from core.models.road_analytics import RoadAnalytics
from core.models.incident import Incident
from core.models.prediction import Prediction
from core.models.signal_decision import SignalDecision


@dataclass
class TrafficState:

    # Road Analytics
    analytics: dict[str, RoadAnalytics] = field(default_factory=dict)

    # Predictions
    predictions: dict[str, Prediction] = field(default_factory=dict)

    # Events / Incidents
    events: dict[str, Incident] = field(default_factory=dict)

    # System Health
    health: dict = field(default_factory=dict)

    # AI Decisions
    decisions: dict[str, SignalDecision] = field(default_factory=dict)

    # Explainability
    explanations: dict = field(default_factory=dict)