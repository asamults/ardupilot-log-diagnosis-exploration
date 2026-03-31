from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.parser.core import ParserError, parse_log_file


class ParseLogFileTests(unittest.TestCase):
    def test_parse_json_log_returns_summary_counts(self) -> None:
        payload = {
            "vehicle_type": "copter",
            "firmware": "ArduCopter 4.5-dev",
            "parameters": [
                {"name": "INS_GYRO_FILTER", "value": 20},
                {"name": "PSC_ACCZ_P", "value": 0.5},
            ],
            "events": [
                {
                    "timestamp_s": 0.5,
                    "event_type": "EKF_WARNING",
                    "severity": "warning",
                    "message": "variance high",
                },
                {
                    "timestamp_s": 1.3,
                    "event_type": "GPS_GLITCH",
                    "severity": "warning",
                    "message": "position jump detected",
                },
            ],
        }

        with tempfile.TemporaryDirectory() as tmp_dir:
            path = Path(tmp_dir) / "sample-log.json"
            path.write_text(json.dumps(payload), encoding="utf-8")

            parsed = parse_log_file(path)

        self.assertEqual(parsed.vehicle_type, "copter")
        self.assertEqual(parsed.firmware, "ArduCopter 4.5-dev")
        self.assertEqual(len(parsed.parameters), 2)
        self.assertEqual(len(parsed.events), 2)
        self.assertEqual(parsed.summary()["event_types"], ["EKF_WARNING", "GPS_GLITCH"])

    def test_non_json_input_raises_parser_error(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            path = Path(tmp_dir) / "sample.bin"
            path.write_bytes(b"not a json log")

            with self.assertRaises(ParserError):
                parse_log_file(path)


if __name__ == "__main__":
    unittest.main()
