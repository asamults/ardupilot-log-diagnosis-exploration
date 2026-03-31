# Parser Module

This directory is reserved for log ingestion and normalization code.

## Intended Responsibilities
- read DataFlash logs,
- expose selected message families,
- preserve timestamps,
- normalize values into stable internal structures,
- support parser-level tests.

## Important Constraint
The parser layer must remain deterministic and free of diagnosis logic.
