# MVP Scope

## Objective

The MVP will deliver a standalone diagnostic prototype for ArduPilot flight logs.

The goal is not to solve all UAV failure diagnosis problems. The goal is to provide a **narrow, explainable, and testable first version** that can identify a small number of high-value failure classes with evidence-backed output.

## In Scope

### 1. Log Input
- ArduPilot DataFlash logs
- structured ingestion of selected message families
- preservation of timestamps and event ordering

### 2. Parameter Context
- extraction of relevant parameter values
- parameter-state association with analyzed log windows

### 3. Diagnostic Output
- top candidate root cause
- ranked alternative hypotheses
- supporting evidence
- confidence estimate
- recommended next checks or corrective actions

### 4. MVP Failure Classes
Initial support should target a limited number of interpretable categories:
- vibration-related instability
- EKF/estimator faults or divergence indicators
- GPS quality or positioning anomalies
- power/battery-related anomalies
- tuning/control instability

### 5. Diagnostic Method
The MVP will use a hybrid strategy:
- rule-based diagnostics for obvious or high-confidence signatures,
- retrieval over labeled known issue patterns,
- ML-assisted ranking for candidate root-cause prioritization.

## Out of Scope

The MVP should explicitly avoid the following:
- full coverage of all ArduPilot failure modes,
- end-to-end black-box diagnosis without evidence,
- deep UI integration as a first milestone,
- real-time onboard diagnosis,
- autonomous remediation,
- unsupported claims of production readiness.

## User of the MVP

The initial user is assumed to be:
- a developer,
- an advanced hobbyist,
- a tester,
- a maintainer,
- or a technically literate operator who already works with ArduPilot logs.

The MVP is meant to reduce investigation time, not replace expert judgment.

## Success Criteria

The MVP is successful if it can:
1. accept a log and produce a structured diagnostic report,
2. identify a small set of common issues with usable accuracy,
3. provide evidence that a reviewer can inspect,
4. distinguish between strong and weak confidence cases,
5. document limitations clearly.

## Delivery Standard

All MVP components should be designed so they can later be extended without rewriting the entire pipeline.

That means:
- stable internal representations,
- explicit evidence mapping,
- versioned schema where appropriate,
- clear separation between ingestion, evidence extraction, diagnosis, and reporting.
