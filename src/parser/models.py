from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class FlightEvent:
    """A normalized event extracted from a flight log."""

    timestamp_s: float
    event_type: str
    severity: str = "info"
    message: str = ""
    raw: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class ParameterSnapshot:
    """A parameter value observed before or during a flight."""

    name: str
    value: Any
    source: str = "log"


@dataclass(slots=True)
class ParsedLog:
    """Structured result produced by the parser skeleton.

    This is intentionally small and stable so it can be reused by
    retrieval, classification, and report-generation layers later.
    """

    source_path: str
    vehicle_type: str = "unknown"
    firmware: str = "unknown"
    parameters: list[ParameterSnapshot] = field(default_factory=list)
    events: list[FlightEvent] = field(default_factory=list)

    def summary(self) -> dict[str, Any]:
        return {
            "source_path": self.source_path,
            "vehicle_type": self.vehicle_type,
            "firmware": self.firmware,
            "parameter_count": len(self.parameters),
            "event_count": len(self.events),
            "event_types": sorted({event.event_type for event in self.events}),
        }
