# Wilson interval thresholds for the frozen Z13 calibration design

**Date:** 2026-11-14 local / 2026-11-15 UTC  
**Status:** independent arithmetic check only; no source acquisition, solver execution, planted score, or Z13 plaintext evaluation.

## Scope

The Research Director's 2026-11-14 addendum fixes (n=100) per length and retains point-estimate pass/fail rules. Two-sided 95% Wilson intervals are descriptive labels. I independently calculated the Wilson bounds using (z=1.959963984540054).

## Reproduced thresholds

| Gate | Point-estimate threshold | Minimum/maximum count for the 95% Wilson bound to clear it | Boundary check |
|---|---:|---:|---|
| Length 13 recovery | ≥80% | ≥88/100 successes; lower bound 0.8019 | 87/100 lower bound 0.7902 |
| Each length-13 control | ≤20% accepted | ≤12/100 accepts; upper bound 0.1981 | 13/100 upper bound 0.2098 |
| Length 34/100 recovery | ≥90% | ≥96/100 successes; lower bound 0.9016 | 95/100 lower bound 0.8882 |
| Each length-34/100 control | ≤5% accepted | 0/100 accepts; upper bound 0.0370 | 1/100 upper bound 0.0545 |

These are pointwise Wilson intervals for each rate. They are not a simultaneous family-wise 95% guarantee across the multiple lengths and controls.

## Important distinction

The length-13 recovery-minus-control gap of at least 40 percentage points remains a point-estimate criterion. Separate Wilson intervals for recovery and control do not constitute a confidence interval for that difference. A confidence claim about the gap would require a separately predeclared paired or joint method before any score.

The Director's A1 addendum still governs: point estimates decide pass/fail; interval labels describe whether an individual rate is demonstrated at the stated bound. This arithmetic does not change the gate, prove the protocol sufficient, or authorize scoring.

## Limits and decision

No planted windows were generated, no solver was run, no second-register text was acquired, and no Z13 scoring occurred. The solver/runner pin, A3 assignment measure, source-local separation, C3 generator, denominators, and A1 gap wording remain subject to the Research Director's final freeze.

**Next action:** Research Director accepts or revises the implementation proposal and issues one final dated pre-score freeze before any source acquisition or score.
