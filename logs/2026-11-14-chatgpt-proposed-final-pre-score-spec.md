# ChatGPT proposed resolution for the Z13 pre-score addendum (A1–A7)

**Status:** proposal for Research Director review, not a Director freeze. Written before any planted score. No source fetched, code run, or Z13 plaintext evaluated.

This proposal is intended to make the existing design executable without changing the original cipher-only scope or allowing post-score threshold changes.

## A1 — point passes and confidence labels
Keep the Director's point-estimate pass/fail thresholds. Report two-sided 95% Wilson intervals for each recovery/control rate. The ≥40 percentage-point recovery-minus-control gap is a **point-estimate criterion only** in this version; do not call the gap itself “demonstrated at 95%” because separate Wilson intervals do not provide an interval for a paired difference. If a confidence claim for the gap is desired, the Director must predeclare a paired method and threshold before any score.

## A2 — denominators
For each length and each of true/C1/C2/C3, publish: eligible candidate windows, rejected windows, accepted evaluation windows (target n=100), skipped windows, solver failures, and the exact draw order. A failed solver run counts as a failure under the frozen rule; do not replace it after seeing the score.

## A3 — length-13 class assignment
Use eight **labelled** ciphertext classes with fixed multiplicities `[3,2,2,2,1,1,1,1]`, class IDs `0..7`. A plaintext window is feasible iff there is at least one function from those eight class IDs to the distinct plaintext letters such that the sum of class multiplicities assigned to each letter equals that letter's observed count. Enumerate all feasible labelled class-to-letter functions; choose uniformly among those functions. Conditional on that function, assign the positions of each letter uniformly among the class IDs assigned to it, respecting each class multiplicity. This is an explicit two-stage sampling measure; it is not claimed to be uniform over all possible ciphertext strings.

## A4 — lengths 34 and 100
Let `z=[3,2,2,2,1,1,1,1]`; class IDs are ordered `0..c-1` and weights are `w_j=z[j mod 8]` (cycle origin is index 0). Set `c=min(54, round(8L/13))`. Give every class one position, then allocate the remaining `L-c` positions by largest remainder proportional to `w_j`; ties go to the lower class ID. Apply the same labelled class-to-letter feasibility and two-stage uniform assignment as A3 using these resulting class multiplicities. Infeasible windows are rejected and logged.

## A5 — source-local windows
Treat the first-register training/cutoff material and the second-register evaluation text as separate source files with separate coordinate systems. Enforce source-provenance separation across registers; never compare offsets across files. Preserve the existing ≥1,000-letter separation and non-overlap rules only among windows sharing the same source file. Within the second-register file, evaluation windows of lengths 13, 34 and 100 must be pairwise non-overlapping. Keep the existing draw order (13, then 34, then 100) and master window seed 20261113; record every rejected candidate.

## A6 — solver pin and restart harness
Candidate implementation: `data/scripts/sq2_z408_hillclimb_solver_v4.py`, Git blob `7e816706009e6272e9ea74433353bd54385de9f1`. It is the latest inspected swap/reassignment solver and includes the unigram-KL penalty `LAMBDA=1.0`; the training text it references is `data/external-sources/gutenberg-1342-2026-09-29/pride_prejudice.txt`, blob `9c37e59d9a9162a21368f00aa4da250218dbfc01`. Pin Python 3.11.17 and standard library only. Do not call the file's `main()` (which uses 60 restarts and a single stream). Instead, write and pin a separate runner that calls its functions unchanged for exactly 20 restarts per ciphertext, with 12,000 iterations/restart, temperature 4.0, cooling 0.9995, 50% swap / 50% reassignment, perturbed-best K in `{2,4,6,8}`, and the v4 unigram penalty. Restart 0 is frequency-seeded, restart 1 random, even restarts ≥2 perturbed-best, odd restarts random. Define `window_index` as the zero-based accepted-window index across the concatenated 13/34/100 lists; restart index is zero-based. For each paired true/C1/C2/C3 ciphertext, reuse the same 20 restart seeds `20261113 + 1000*window_index + restart_index`. Record solver and runner blob hashes and the runtime.

This is a proposed harness choice: the Director may instead select v2/v3 or retain 60 restarts, but must pin one exact solver and reconcile the restart count before scoring.

## A7 — matched controls and C3
C1 is a seeded shuffle of the true window; C2 is its reversal. Both preserve the true window's letter counts and reuse the true window's exact sampled class-to-letter key and position assignment. C3 is generated from the pinned first-register training text's unigram probabilities, using the same smoothing as v4 (`max(count/total, 1e-6)`) and a separate RNG `random.Random(20261115 + window_index)`. Rejection-sample until the generated string is feasible under the A3/A4 class multiplicities, with a predeclared cap of 1,000,000 candidates; log rejected draws. Sample a new feasible labelled class assignment for C3 using `random.Random(20261116 + window_index)`. If the cap is exhausted, record C3 as infeasible; do not substitute another generator.

## Pre-score checklist
1. Director accepts/revises every proposal and publishes a dated final freeze.
2. Pin the runner and exact source blobs; verify hashes before execution.
3. User explicitly authorizes one identified second-register file.
4. Publish the eligible/rejected/skipped denominator schema and output schema.
5. Only then run planted calibration. No Z13 scoring unless the frozen gate is met.

No suspect inference is permitted. This proposal is not a score, a decryption, or evidence that Z13 is or is not solvable.
