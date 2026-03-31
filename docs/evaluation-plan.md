# Evaluation Plan

## Evaluation Objective

The purpose of evaluation is to determine whether the prototype provides **useful and evidence-backed diagnostic assistance**.

The goal is not only classification accuracy. The system must also provide diagnostic outputs that are interpretable, appropriately calibrated, and operationally useful.

## Evaluation Dataset

The evaluation set should contain curated flight-log cases with known or strongly supported outcomes.

Each case should include:
- case identifier,
- log source or reference,
- known or expert-supported issue label,
- relevant parameter context,
- diagnostic notes,
- optional severity level,
- expected evidence regions where available.

## Initial Evaluation Tasks

### 1. Root-Cause Candidate Ranking
Measure whether the correct diagnosis appears:
- as top-1,
- within top-3,
- within top-k candidates.

### 2. Evidence Quality
Assess whether the evidence cited by the system is:
- relevant,
- traceable to the log,
- consistent with the predicted issue.

### 3. Confidence Quality
Assess whether confidence values behave sensibly:
- high confidence for strong evidence,
- lower confidence for ambiguous cases,
- explicit uncertainty where evidence is weak.

### 4. False Positive Behavior
Test selected normal or non-target logs to estimate how often the system incorrectly reports a failure class.

## Metrics

Recommended initial metrics:
- Top-1 accuracy
- Top-3 accuracy
- Precision for supported failure classes
- False positive rate on normal cases
- Evidence relevance score (manual review rubric)
- Confidence calibration notes

## Review Rubric for Evidence Quality

For each report, review:
1. Did the report identify the correct or plausible issue?
2. Was the cited evidence actually present in the log?
3. Were alternative hypotheses reasonable?
4. Did the confidence level match the ambiguity of the case?
5. Were suggested next steps technically useful?

## MVP Evaluation Standard

The MVP will be considered useful if:
- it performs credibly on a narrow set of target failure classes,
- it produces evidence-backed reports,
- it avoids excessive confident misclassification,
- and it clearly marks uncertainty when diagnosis is ambiguous.

## Known Limitations

Evaluation in early stages may be constrained by:
- limited labeled data,
- inconsistent case documentation,
- unequal class coverage,
- ambiguity in real-world root-cause interpretation.

These limitations should be documented explicitly rather than hidden.

## Next Evaluation Milestones

1. define a small labeled benchmark set,
2. implement baseline rule-only evaluation,
3. add retrieval-based comparison,
4. test ML-assisted ranking,
5. compare hybrid pipeline against rule-only baseline.
