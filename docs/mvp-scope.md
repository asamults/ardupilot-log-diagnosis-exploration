# MVP Scope

## Objective

The purpose of v1 is to demonstrate a narrow, explainable, technically honest
diagnostic workflow for ArduPilot-related log analysis.

v1 is not intended to be a full diagnostic platform.

## Core v1 Outcome

Given a normalized input log fixture, the system should be able to:

1. parse the input,
2. inspect selected events and parameter context,
3. produce a small structured diagnostic report,
4. state a likely issue class,
5. attach explicit evidence and a confidence estimate.

## Primary v1 Input Path

The current v1 input path is:

**Normalized JSON fixtures**

Reason:
- deterministic,
- testable,
- fast to iterate,
- suitable for early diagnostic logic,
- avoids pretending that full DataFlash support already exists.

## v1 Failure Classes

The first version is intentionally limited to three failure classes:

### 1. GPS Anomaly
Representative signals:
- GPS-related warning events,
- glitch-like indicators,
- degraded location confidence markers.

### 2. EKF Warning / Estimator Instability
Representative signals:
- EKF-related warning events,
- estimator health degradation indicators,
- inconsistent navigation-state evidence.

### 3. Explicit Error / Failsafe Indicator
Representative signals:
- explicit error or failsafe-like event markers,
- severe system warnings,
- events that clearly indicate abnormal flight-state handling.

## v1 Output Format

The v1 output format is:

**Structured JSON diagnostic report**

The report should contain:

- input source,
- candidate diagnosis,
- evidence list,
- confidence,
- suggested next step,
- optional alternative hypothesis.

## v1 Diagnostic Strategy

The first version will use:

- parser-normalized inputs,
- deterministic evidence extraction,
- rule-based baseline logic,
- explicit report generation.

Machine learning is not required for v1 success.

## In Scope

- normalized parser inputs,
- diagnostic baseline for selected classes,
- structured report output,
- unit tests,
- sample reports,
- explicit documentation of assumptions.

## Out of Scope

- broad anomaly taxonomy,
- production-quality ML training,
- live ArduPilot integration,
- complete DataFlash parsing,
- GUI/dashboard work,
- commercial packaging.

## Success Criteria

v1 is successful if:

- it supports at least the selected failure classes,
- output is deterministic,
- output includes evidence,
- tests pass,
- repository state is clear enough for review by mentor/community.

## Failure Criteria

v1 is not successful if:

- diagnosis depends on vague AI-generated text,
- evidence is absent,
- scope expands beyond the selected classes,
- input format becomes unstable,
- the repository makes unsupported claims.

## Next Step After v1

Only after v1 is stable should the project consider:

- broader event coverage,
- richer parameter-state interpretation,
- retrieval over labeled examples,
- optional ML-assisted ranking,
- future DataFlash-backed parsing.
