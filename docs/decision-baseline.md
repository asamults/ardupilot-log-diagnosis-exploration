# Decision Baseline

## Purpose

This document defines the Day 1 decision baseline for the repository.

Its purpose is to remove ambiguity around the project and to make further work
measurable. The repository is currently an exploratory technical project, not a
commercial product and not a production-ready ArduPilot subsystem.

The immediate goal is to determine whether this project deserves deeper
investment after a 7-day validation cycle.

## Project Statement

The project explores an AI-assisted diagnostic workflow for ArduPilot flight-log
analysis.

The intended system should:

- ingest flight-log-derived data,
- identify candidate anomaly or failure patterns,
- produce structured diagnostic output,
- provide evidence and confidence,
- support faster debugging and triage.

## Problem

ArduPilot flight logs contain useful evidence for diagnosing failures,
misconfigurations, estimator issues, GPS anomalies, and operator-visible faults.

However, the diagnostic process is often:

- manual,
- knowledge-intensive,
- repetitive,
- difficult for less experienced users.

This creates a gap between available telemetry/log evidence and practical,
repeatable diagnosis.

## Primary User

The primary user for the exploratory MVP is:

**A technically capable ArduPilot user, developer, or operator who wants faster
initial triage of flight-log issues.**

This is not yet a beginner-only product and not yet a commercial fleet platform.

## User Pain

The primary pain is not “lack of AI.”

The real pain is:

- slow first-pass triage,
- repeated manual inspection of similar failure patterns,
- difficulty narrowing likely root causes quickly,
- lack of structured initial reports.

## MVP Definition

The MVP is **not** a general AI diagnostic platform.

The MVP is:

1. a parser-driven normalized input path,
2. a narrow set of interpretable failure classes,
3. a baseline diagnostic layer,
4. a structured report with:
   - candidate root cause,
   - supporting evidence,
   - confidence,
   - suggested next step.

## Day 1 Scope Decision

The repository will currently optimize for:

- clarity,
- narrow scope,
- explainability,
- testability,
- incremental delivery.

The repository will **not** optimize for:

- broad feature coverage,
- production deployment,
- UI polish,
- large-scale ML training,
- commercial packaging.

## In Scope for the 7-Day Cycle

- parser architecture clarity,
- explicit MVP boundaries,
- baseline diagnosis path,
- structured sample outputs,
- evidence-oriented reporting,
- early community-facing technical credibility.

## Out of Scope for the 7-Day Cycle

- full binary DataFlash ingestion,
- broad anomaly taxonomy,
- model training at production quality,
- live integration with GCS tools,
- paid-product packaging,
- commercialization claims.

## Key Assumptions

### Assumption 1
A narrow, explainable diagnostic baseline is more useful at this stage than a
broad but opaque AI approach.

### Assumption 2
A useful first version can exist without a trained end-to-end model.

### Assumption 3
Community or mentor feedback will be a meaningful signal for whether the
project deserves deeper investment.

## Validation Questions

By Day 7, this project must answer the following:

1. Is the user/problem definition still credible?
2. Is the MVP technically realistic without uncontrolled scope expansion?
3. Does the project produce useful diagnostic outputs?
4. Is there any meaningful external signal that this work matters?
5. Does the project have strong portfolio or GSoC value even if product value
   remains uncertain?

## Green Signals

The project should be continued only if at least some of the following appear:

- meaningful mentor or community feedback,
- clear MVP scope with no major ambiguity,
- working baseline diagnosis path,
- structured outputs that look practically useful,
- clear portfolio or application value.

## Red Signals

The project should not be scaled if the following dominate:

- no meaningful external response,
- expanding scope without clearer value,
- no convincing baseline without “future AI magic,”
- outputs that are vague and not evidence-based,
- weak strategic value relative to time invested.

## Current Day 1 Position

Current repository status:

- exploratory parser exists,
- tests pass,
- CLI works,
- DataFlash adapter boundary exists as a stub,
- project scope is still early and must remain constrained.

## Decision Rule

At the end of Day 7, the project will be classified as one of:

- **Continue** — worth deeper technical investment,
- **Freeze** — keep as GSoC/portfolio artifact,
- **Pivot** — useful direction, but not as a standalone product.

## Day 1 Deliverable

The Day 1 deliverable is a repository with an explicit written baseline and a
narrow, reviewable scope.
