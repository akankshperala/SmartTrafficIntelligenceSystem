"""
Signal Decision Model
"""

from dataclasses import dataclass


@dataclass
class SignalDecision:

    junction_id: str

    current_phase: str

    next_phase: str

    green_duration: float

    priority: str

    reason: str

    timestamp: float

    def __str__(self):

        return (
            f"SignalDecision(\n"
            f"  junction={self.junction_id},\n"
            f"  current={self.current_phase},\n"
            f"  next={self.next_phase},\n"
            f"  green={self.green_duration:.1f}s,\n"
            f"  priority={self.priority}\n"
            f")"
        )