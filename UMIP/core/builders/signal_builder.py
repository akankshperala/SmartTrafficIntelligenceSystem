"""
Signal Builder
"""

from core.models.signal import Signal


class SignalBuilder:

    def build(self, raw_signals):

        signals = []

        for s in raw_signals:

            signals.append(

                Signal(

                    id=s["id"],

                    phase=s["phase"],

                    phase_name=s["phase_name"],

                    duration=s["duration"],

                    controlled_lanes=s["controlled_lanes"]

                )

            )

        return signals