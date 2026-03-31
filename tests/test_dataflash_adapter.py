from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.parser.core import ParserError
from src.parser.dataflash_adapter import DataFlashAdapter


class DataFlashAdapterTests(unittest.TestCase):
    def setUp(self) -> None:
        self.adapter = DataFlashAdapter()

    def test_can_handle_known_suffixes(self) -> None:
        self.assertTrue(self.adapter.can_handle("flight.bin"))
        self.assertTrue(self.adapter.can_handle("flight.log"))
        self.assertTrue(self.adapter.can_handle("flight.json"))
        self.assertFalse(self.adapter.can_handle("flight.txt"))

    def test_parse_json_delegates_to_core_parser(self) -> None:
        payload = {
            "vehicle_type": "plane",
            "firmware": "ArduPlane 4.5-dev",
            "parameters": [{"name": "ARSPD_USE", "value": 1}],
            "events": [
                {
                    "timestamp_s": 3.0,
                    "event_type": "STALL_WARNING",
                    "severity": "warning",
                    "message": "airspeed low",
                }
            ],
        }

        with tempfile.TemporaryDirectory() as tmp_dir:
            path = Path(tmp_dir) / "normalized-log.json"
            path.write_text(json.dumps(payload), encoding="utf-8")

            parsed = self.adapter.parse(path)

        self.assertEqual(parsed.vehicle_type, "plane")
        self.assertEqual(parsed.summary()["event_types"], ["STALL_WARNING"])

    def test_parse_dataflash_stub_raises_clear_error(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            path = Path(tmp_dir) / "flight.bin"
            path.write_bytes(b"not yet supported")

            with self.assertRaises(ParserError) as ctx:
                self.adapter.parse(path)

        self.assertIn("DataFlash ingestion is not implemented", str(ctx.exception))


if __name__ == "__main__":
    unittest.main()
