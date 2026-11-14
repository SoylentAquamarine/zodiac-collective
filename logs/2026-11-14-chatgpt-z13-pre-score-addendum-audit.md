# ChatGPT audit of the Z13 pre-score addendum (A1–A7)

**Date:** 2026-11-14 ~04:00 UTC  
**Scope:** design audit only. No second-register source was fetched, no code was run, no planted score was produced, and no Z13 plaintext was evaluated. This is not an independent reproduction of a result; the Director's addendum is still unexecuted.

## Sources read

- `logs/2026-11-13-z13-planted-recovery-protocol-freeze.md`
- `logs/2026-11-14-z13-pre-score-addendum-freeze.md`
- `data/scripts/sq2_z408_hillclimb_solver.py` (the solver file currently indexed in `INDEX.md`)
- `config/research-department.md`, `config/sidequests.md`, current README, INDEX, state, and latest steering #26

## A1–A7 audit

| Addendum | Disposition | Audit |
|---|---|---|
| A1 — point estimates / Wilson labels | **Mostly clear; one gap** | The point-estimate pass rule and descriptive Wilson intervals are explicit. The extra “demonstrated” label is not fully defined for the ≥40-percentage-point recovery-minus-control gap. Individual Wilson bounds do not provide an interval for that difference. State whether this gap is point-estimate-only, or report a paired interval using the matched window/control outcomes. |
| A2 — 100 windows per length | **Arithmetic checks out** | With 100 trials and zero control accepts, the two-sided 95% Wilson upper bound is about 0.037, so a 5% upper-bound demonstration is possible. This does not itself establish adequate power or independence; report eligible, rejected, and skipped windows for each length and control. |
| A3 — 13-character multiplicities | **Concept is clear; randomization is underspecified** | The vector [3,2,2,2,1,1,1,1] matches Z13's class-size multiset, not its positional equality partition; the addendum discloses that distinction correctly. For reproducibility, define a feasible split as a partition of **labelled** ciphertext-class IDs among the plaintext letters, say whether sampling is uniform over labelled partitions or unique size-patterns, and specify the uniform assignment of occurrence positions within each letter. Those choices can yield different distributions. |
| A4 — lengths 34 and 100 | **Allocation rule partly executable** | The stated class counts (21 and 54) and largest-remainder/tie rule are deterministic in principle. “Letters-to-classes consistent with plaintext exactly as in A3” must explicitly generalize A3's subset-sum feasibility rule to the newly generated c(L)-class multiplicity vector. Freeze class ordering, weight-cycle origin, and the labelled-partition sampling unit. |
| A5 — window separation | **Blocking inconsistency** | A 1,000-letter offset cannot be measured between windows in different source files. The second register is required to be a different text from the Gutenberg-1342 cutoff/benchmark register. Use source-provenance separation across files, and apply the 1,000-letter offset only to windows in the same file; retain pairwise non-overlap across the three evaluation lengths within the second register. |
| A6 — solver / seeds / ties | **Blocking provenance mismatch** | The addendum does not name a solver path, commit/blob hash, environment, or exact hyperparameters. The only solver file currently listed in the repository INDEX, `data/scripts/sq2_z408_hillclimb_solver.py`, uses 60 restarts × 12,000 iterations, a single `random.Random(20261011)` stream, and per-symbol random letter reassignment; it is not the described “swap-based” solver and does not use the new per-window seed formula. If another solver is intended, pin it explicitly; otherwise reconcile the freeze with the actual code. Also define restart indexing (0- or 1-based), whether each paired control shares its true window's restart seeds, and the numerical equality rule for score ties. |
| A7 — control targets | **Target semantics clear; generator incomplete** | It is now clear that a control is accepted only when its own transformed/random source string appears in the same top five. C1/C2 preserve the source window's letter counts. C3 does not: specify the unigram probability source, RNG/seed, and whether generation is rejection-sampled or conditioned on the same class-multiplicity feasibility rule. Also state whether “same class structure” means reusing the exact symbol-to-letter mapping or only matching the multiplicity vector with a newly sampled mapping. |

## Overall decision

A1 and A2 are usable with the A1 difference-interval caveat. A3–A4 need the sampling unit and generalized partition procedure made executable. A5 and A6 are blockers; A7 needs a fully specified C3 generator and key-reuse rule. These are design issues, not evidence against the selected thresholds and not results about Z13.

The existing solver mismatch is a source-pinning problem, not proof that no suitable solver exists. The Research Director should name the exact intended implementation before any score is produced. Do not silently substitute the indexed legacy solver.

## Ethics, permissions, and next action

Keep this strictly cipher-only: no suspect inference or person-level claim. No source file or case material was acquired. The project gate still requires explicit authorization for one pinned public-domain second-register file, with URL, license, blob/SHA-256, and provenance recorded before retrieval.

**One next action:** Research Director issues a dated implementation clarification for A3–A7 (especially the A5 cross-file rule and exact A6 solver pin) and the A1 paired-gap label; only after that should the user authorize one pinned second-register file. No generator code or scoring before both gates clear.
