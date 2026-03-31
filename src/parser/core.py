from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .models import FlightEvent, ParameterSnapshot, ParsedLog


class ParserError(Exception):
    """Raised when an input file cannot be parsed by the current skeleton."""



def parse_log_file(path: str | Path) -> ParsedLog:
    """Parse a log file into a normalized ParsedLog structure.

    Current scope of the skeleton:
    - accepts JSON input that already resembles a normalized export,
    - validates core fields,
    - converts the input into dataclasses.

    This is deliberate. A full DataFlash parser should be added only after the
    project decides which upstream ArduPilot/pymavlink path it wants to use.
    """
    path = Path(path)
    if not path.exists():
        raise ParserError(f"Input file does not exist: {path}")

    if path.suffix.lower() != ".json":
        raise ParserError(
            "The initial parser skeleton only supports .json exploratory inputs. "
            "Add a dedicated DataFlash adapter in a later iteration."
        )

    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ParserError(f"Invalid JSON input: {exc}") from exc

    return _from_payload(payload=payload, source_path=str(path))



def _from_payload(payload: dict[str, Any], source_path: str) -> ParsedLog:
    parameters = [
        ParameterSnapshot(
            name=str(item["name"]),
            value=item.get("value"),
            source=str(item.get("source", "log")),
        )
        for item in payload.get("parameters", [])
    ]

    events = [
        FlightEvent(
            timestamp_s=float(item["timestamp_s"]),
            event_type=str(item["event_type"]),
            severity=str(item.get("severity", "info")),
            message=str(item.get("message", "")),
            raw=dict(item.get("raw", {})),
        )
        for item in payload.get("events", [])
    ]

    return ParsedLog(
        source_path=source_path,
        vehicle_type=str(payload.get("vehicle_type", "unknown")),
        firmware=str(payload.get("firmware", "unknown")),
        parameters=parameters,
        events=events,
    )
