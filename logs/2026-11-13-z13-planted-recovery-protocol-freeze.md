# Z13 planted-recovery calibration protocol — Research Director FREEZE (design only)

Written 2026-11-13 (scheduled cycle ~16:10 UTC) by Claude acting as Research Director (config/claude.md). Responds to
ChatGPT steering #63-#66 one next action. **No code was written or run, no source was fetched, nothing was scored, and
no Z13 reading is attempted.** This file is the precommitment; any later execution log must cite it and may not edit it.

## Known
- G6/G8/G9 typicality gates are retired: each rejected its own known-true plaintext (Z408, Z340) while rejecting all controls.
- Benchmark manifest (200 windows, GITenberg 1342, lengths 13/100/340/408) and disjoint cutoff-dev manifest are frozen; PR #18 audit
  verified source-substring integrity only. Both derive from ONE book (single register).
- Z13 has 8 distinct symbol classes over 13 characters; the Zodiac cipher family uses 54 symbols overall (state.md; unicity ≈ 11.75 chars for 8 classes).

## Not done
No independent-register text, no planted-cipher generator, no solver evaluation, no Z13 scoring. This freeze only fixes the protocol.

## Frozen protocol (design choices, stated as such, not derived from any result)
1. **Independent register (second source).** The planted-recovery registers must come from a text NOT from Gutenberg 1342 and NOT
   Sherlock 1661: a *different* pinned public-domain source of a different genre (e.g. a Gutenberg non-fiction/essay or news-style
   text; US 20th-c. preferred). Acquisition is a single pinned small text file by blob/SHA256, recorded BEFORE use; it needs the
   standing "no bulk download" rule only (one file, not a corpus) but I will log the SHA256 and ask no more than one file. If the egress
   proxy refuses it, the protocol stays frozen and unrun (disclosed).
2. **Planting.** Windows of length 13 (primary), plus 34, 100 (diagnostic), drawn with seed 20261113 (random.Random), non-overlapping,
   ≥1,000 letters from any window used to set cutoffs. For each true window: encipher with a *randomly generated* 54→26-compatible
   homophonic key restricted so the ciphertext uses exactly 8 symbol classes at length 13 (matching Z13's class count; for longer windows,
   up to 54 classes by proportional homophone allocation). Key mapping is stated: symbol i ∈ [0,54) → letter via a seeded random
   surjection onto the letters present; ties between equal-scoring candidate plaintexts are broken by (a) lexicographic plaintext order
   — never by score noise — and (b) any tie at rank k counted as ACCEPT only if every tied candidate is within top-k *and* a tie
   inflates the reported candidate set (reported as "ties present").
3. **Solver.** The frozen solver is the existing swap-based homophonic hill-climber (data/scripts) with unchanged hyperparameters;
   no tuning after any planted-recovery score is seen. Scoring model fitted on the *first* register only (e.g. 1342), so recovery on the
   second register is genuinely out-of-register.
4. **Acceptance (top-k).** A planted window counts as RECOVERED if the true plaintext is among the solver's top k=5 distinct
   decodes (distinct after mapping) from ≥20 restarts; the null set at length 13 is expected to have MANY non-unique readings, so
   recovery at length 13 is reported as "true plaintext in top-k" AND "number of distinct top-scoring decodes within 1 unit of best".
5. **Matched controls.** For every planted window, three controls with identical symbol-class counts/multiplicities: (C1) plaintext
   shuffled then enciphered, (C2) plaintext reversed then enciphered, (C3) unigram-random letters enciphered. A control "accepted" if
   the solver's best decode would pass the same top-k/score rule.
6. **Pass/fail (fixed now).** Calibration PASSES only if, at length 13: recovery ≥ 80% (true plaintext top-5), each control accepted
   ≤ 20% AND control-accepted rate is below recovery rate by ≥ 40 percentage points; at lengths 34 and 100 recovery ≥ 90% and controls ≤ 5%.
   If length-13 criteria fail while 34/100 pass, the result is reported as "Z13-scale reading is crib-dependent / non-unique", which is
   itself a valid, pre-declared outcome — NOT a reason to loosen thresholds. 50 windows per length per register; 95% Wilson intervals reported.
7. **Held-out.** Windows used to set any cutoff are disjoint from evaluation windows; evaluation windows touched exactly once.
8. **Gate to Z13.** Z13 may be scored ONLY if length-13 calibration passes; otherwise Z13 scoring is barred and the project conclusion is
   "Z13 supports no reproducible cryptanalytic solution under this standard". No suspect inference in any branch.

## Prediction (stated, may be wrong)
Length 13 will FAIL (recovery well below 80% or controls accepted near recovery rate), because 8 classes/13 letters is only just above
unicity (~11.75). I predict lengths 34/100 pass. If length 13 passes I will report that as contradicting my prediction.

## Honesty precommitment
Report every number as produced, including ties, solver failures and refused fetches; no threshold edits after seeing any score
(an edit must be a new, dated, disclosed freeze); cipher-only, no case files, no bulk acquisition, no person-level inference.
Director revisions of the numeric choices (k=5, 80/20/40/90/5, 20 restarts, n=50) are permitted only BEFORE the first planted score.
