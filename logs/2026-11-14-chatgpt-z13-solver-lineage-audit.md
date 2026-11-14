# ChatGPT audit: Z13 solver lineage and executable freeze

**Date:** 2026-11-14  
**Scope:** source inspection only. No solver was executed, no second-register source was fetched, no planted score was produced, and Z13 was not scored.

## Solver files inspected

| File | Blob SHA | What the code does |
|---|---|---|
| data/scripts/sq2_z408_hillclimb_solver.py | 3a7c73bc63eb6f331b9ec3388a4d9f7ab37dbd66 | Random per-symbol letter reassignment; no swap move |
| data/scripts/sq2_z408_hillclimb_solver_v2.py | 93173cf5529df88fc6eec0ab461b3a4aa0ae09ab | 50% symbol swaps / 50% reassignments; frequency-informed seeding |
| data/scripts/sq2_z408_hillclimb_solver_v3.py | 4a94c7016f11c6fe956eef21123dd6ef436ecad7 | Retains v2 move mix; adds perturbed-best restarts |
| data/scripts/sq2_z408_hillclimb_solver_v4.py | 7e816706009e6272e9ea74433353bd54385de9f1 | Retains v3 restart strategy; adds unigram-KL penalty to the objective (LAMBDA=1.0) |

The phrase “existing swap-based homophonic hill-climber” does not uniquely pin an executable. v2 is the first indexed version with swap moves; v3 and v4 inherit those moves but change restart strategy and objective. The addendum names no path, commit, blob, environment, or exact hyperparameter set.

## A1–A7 implementation gaps

- **A1:** the point-pass / Wilson-descriptive convention is explicit. The recovery-minus-control gap still needs its own uncertainty rule; separate Wilson intervals do not provide an interval for the paired difference.
- **A3–A4:** define the sampling unit for labelled class IDs, occurrence-position assignment, class ordering, weight-cycle origin, and how feasibility is generalized for 34/100-character windows.
- **A5:** a 1,000-letter coordinate offset cannot be measured across two different source files. Use source-provenance separation across registers; apply within-file offsets and pairwise non-overlap only where coordinates share a source.
- **A6:** pin one solver blob/commit. Define whether window_index is global across lengths, whether paired controls share restart seeds, restart indexing, and exact floating-score tie equality.
- **A7:** specify the C3 unigram source/distribution, RNG/seed, generation/conditioning rule, and whether controls reuse the same symbol-to-letter key or only the same class-size multiset.

These are protocol/provenance issues, not results about Z13. The Director's addendum remains design-only.

## Decision and next action

Do not write a generator or score anything until the Research Director publishes a dated executable freeze naming one exact solver file/blob/commit and fixing the deterministic partition, window, key, seed, and C3-control procedures. The separate public-domain second-register source still requires explicit user authorization before retrieval.

No suspect inference or person-level claim is permitted.
