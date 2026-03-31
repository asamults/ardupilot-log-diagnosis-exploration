from __future__ import annotations

import argparse
import json
import sys

from .core import ParserError, parse_log_file



def build_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Parse an exploratory ArduPilot log export into a normalized summary."
    )
    parser.add_argument("--input", required=True, help="Path to exploratory JSON log file")
    parser.add_argument(
        "--pretty",
        action="store_true",
        help="Pretty-print the parsed summary as indented JSON.",
    )
    return parser



def main() -> int:
    args = build_argument_parser().parse_args()

    try:
        parsed = parse_log_file(args.input)
    except ParserError as exc:
        print(f"parser error: {exc}", file=sys.stderr)
        return 2

    if args.pretty:
        print(json.dumps(parsed.summary(), indent=2))
    else:
        print(json.dumps(parsed.summary(), separators=(",", ":")))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
