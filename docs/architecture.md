# Architecture

## Overview

The system is designed as an explainable diagnostic pipeline rather than a monolithic black-box model.

```text
DataFlash Log
    ↓
Log Ingestion Layer
    ↓
Normalization & Parameter Context Extraction
    ↓
Evidence Extraction
    ↓
Hybrid Diagnosis Engine
    ├── Rule-Based Signals
    ├── Retrieval Over Labeled Cases
    └── ML-Assisted Ranking
    ↓
Structured Diagnostic Report
```

## 1. Log Ingestion Layer

### Responsibilities
- load ArduPilot DataFlash logs,
- parse selected message families,
- preserve timestamps and event order,
- expose raw and normalized representations.

### Design Notes
The ingestion layer must remain deterministic and testable. It should not contain diagnosis logic.

## 2. Normalization & Parameter Context Extraction

### Responsibilities
- align values to a consistent internal format,
- attach relevant parameter context,
- define analysis windows,
- prepare inputs for evidence extraction.

### Design Notes
This layer should produce a stable intermediate representation so later diagnostic logic can evolve independently.

## 3. Evidence Extraction

### Responsibilities
- compute summary metrics,
- identify threshold crossings,
- detect suspicious intervals,
- derive feature vectors or evidence descriptors,
- preserve references to original log segments.

### Design Notes
Evidence must stay traceable to raw log content. Every downstream diagnosis should be backed by identifiable evidence.

## 4. Hybrid Diagnosis Engine

The diagnosis engine combines three complementary mechanisms.

### 4.1 Rule-Based Signals
Best for:
- obvious safety or failure signatures,
- interpretable threshold-based checks,
- high-confidence known patterns.

### 4.2 Retrieval Over Labeled Cases
Best for:
- similarity to known incident patterns,
- explainable comparison with curated examples,
- retrieving supporting precedent.

### 4.3 ML-Assisted Ranking
Best for:
- prioritizing likely candidates,
- combining multiple weak signals,
- generating calibrated confidence estimates.

### Design Goal
The engine should output ranked hypotheses rather than a single unexplained label.

## 5. Structured Diagnostic Report

### Required Fields
- log metadata,
- analysis scope/window,
- top diagnosis candidate,
- alternative candidates,
- supporting evidence,
- parameter context,
- confidence score,
- recommended next checks.

### Design Goal
The report must be understandable to a technically literate reviewer and suitable for future machine-readable export.

## 6. Separation of Concerns

The architecture should preserve the following boundaries:
- parser logic does not perform diagnosis,
- evidence extraction does not decide final conclusions,
- report generation does not invent unsupported evidence,
- learned ranking does not replace explicit rule evidence where high-confidence rules exist.

## 7. Extension Path

After the MVP, the architecture should support:
- additional failure classes,
- richer labeled datasets,
- stronger retrieval indexing,
- improved calibration,
- optional web UI or service API,
- future integration with existing tooling.
