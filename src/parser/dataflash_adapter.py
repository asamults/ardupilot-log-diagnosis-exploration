from __future__ import annotations

from pathlib import Path

from .core import ParserError, parse_log_file
from .models import ParsedLog


class DataFlashAdapter:
    """Format adapter boundary for future ArduPilot DataFlash parsing.

    Current behavior is intentionally conservative:
    - JSON inputs are delegated to the existing exploratory parser,
    - DataFlash-like suffixes are recognized,
    - actual binary DataFlash translation is not yet implemented.

    This keeps the repository honest: the adapter boundary exists and is tested,
    but the project does not pretend to support real DataFlash ingestion before
    the message-family extraction policy is defined.
    """

    DATAFLASH_SUFFIXES = {".bin", ".log", ".dflog"}
    JSON_SUFFIXES = {".json"}

    def can_handle(self, path: str | Path) -> bool:
        suffix = Path(path).suffix.lower()
        return suffix in self.JSON_SUFFIXES | self.DATAFLASH_SUFFIXES

    def parse(self, path: str | Path) -> ParsedLog:
        path = Path(path)
        suffix = path.suffix.lower()

        if suffix in self.JSON_SUFFIXES:
            return parse_log_file(path)

        if suffix in self.DATAFLASH_SUFFIXES:
            raise ParserError(
                "DataFlash ingestion is not implemented in this exploratory stub yet. "
                "Add a dedicated pymavlink-backed translation layer before parsing "
                f"binary logs: {path.name}"
            )

        raise ParserError(
            f"Unsupported log format for DataFlashAdapter: {path.suffix or '<no extension>'}"
        )
