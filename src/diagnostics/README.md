# Diagnostics Module

This directory is reserved for evidence extraction, rule logic, retrieval logic, and ML-assisted ranking.

## Intended Responsibilities
- define supported failure classes,
- extract diagnostic evidence,
- rank candidate root causes,
- generate confidence-aware outputs.

## Important Constraint
Diagnosis must remain evidence-backed. This layer must not generate conclusions that cannot be traced to extracted signals, labeled cases, or explicit model outputs.
