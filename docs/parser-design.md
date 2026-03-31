# Parser Design

## Goal

The parser layer converts raw flight-log inputs into a small, stable, deterministic
internal representation that downstream components can consume.

The parser is **not** responsible for diagnosis, ranking, retrieval, or report
writing. It must only ingest, normalize, and validate data.

## Current Scope

The current repository supports a deliberately small exploratory path:

- JSON-based normalized example inputs,
- conversion into internal dataclasses,
- deterministic summaries,
- parser-level unit tests.

This scope is intentionally narrow. It provides a stable engineering base before
committing to a full DataFlash ingestion strategy.

## Target Internal Representation

The current normalized structures are:

- `ParsedLog`
- `FlightEvent`
- `ParameterSnapshot`

This model is intentionally compact because later stages will need a predictable
contract for:

- heuristic diagnostics,
- retrieval against labeled cases,
- classifier inputs,
- structured report generation.

## Design Constraints

### 1. Deterministic behavior
Given the same input, the parser must produce the same output.

### 2. No diagnosis logic
The parser must not guess root causes. It may expose warnings about malformed
or incomplete input, but it must not classify or rank failures.

### 3. Explicit failure modes
Unsupported formats and malformed payloads must fail with clear parser errors.
Silent fallback behavior is not acceptable.

### 4. Stable normalized schema
Downstream layers should not depend on raw upstream log peculiarities.
The parser layer should absorb input-specific complexity and output a stable
shape.

### 5. Traceability
Where possible, parsed artifacts should preserve enough source context for later
reporting and evidence generation.

## Planned Input Paths

### Path A — Normalized JSON exploratory input
This is the current implementation path.

Use case:
- rapid iteration on schema,
- early testing of downstream components,
- fixture-based unit tests.

### Path B — DataFlash adapter
The next practical ingestion target is an adapter for ArduPilot DataFlash logs.
That adapter should:

- detect DataFlash-style file extensions,
- validate that the file can be handled,
- use an explicit upstream parsing dependency,
- transform upstream records into the same normalized dataclasses.

At this stage, the repository includes only a stub for that adapter. This is
intentional: full DataFlash support should only be implemented once the exact
message families and extraction policy are agreed.

## Proposed Adapter Boundary

The repository should keep format-specific logic behind a format adapter layer.

Proposed shape:

- `core.py` — normalized JSON entry point and shared parser errors
- `dataflash_adapter.py` — DataFlash-specific detection and future translation
- `models.py` — normalized dataclasses only

This separation keeps the project modular and testable.

## Error Model

All parser failures should raise `ParserError` with messages that help the user
or developer distinguish between:

- missing input file,
- unsupported file type,
- invalid JSON payload,
- unavailable optional parser dependency,
- malformed normalized structure.

## Near-Term Parser Milestones

### Milestone 1
- keep JSON path stable,
- document schema assumptions,
- add adapter stub and tests.

### Milestone 2
- add optional `pymavlink`-backed DataFlash reader,
- map selected message families into normalized events,
- preserve parameter context.

### Milestone 3
- expose parser metadata useful for diagnosis,
- support richer fixture coverage,
- document extraction policy for supported event classes.
