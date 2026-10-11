# SQ-2 — Z408 reproduction attempt: a real, honest negative result

Precommitment: `logs/2026-10-11-sq2-z408-reproduction-selfreview.md` (frozen before this ran).
Script: `data/scripts/sq2_z408_hillclimb_solver.py`. Full result:
`data/derived/sq2-z408-hillclimb-result.md`.

## Result

60 random restarts, 12,000 hill-climbing iterations each, 112.5 seconds total wall-clock time.
Best quadgram log-likelihood found: -4000.06. **Per-character accuracy against the known
plaintext, compared only after the search was fully complete: 18.87% (77/408).**

## Outcome vs. prediction

The stated prediction ("most likely above 80% per-character accuracy, possibly a clean full
solve") **was wrong**. This is a real, honest negative result from a first, unrefined
implementation, reported exactly as it came out — not re-tuned after seeing the number, per
this check's own precommitted discipline.

**Not nothing, though**: 18.87% is meaningfully above the ~3.8% a uniform-random 26-letter
assignment would score by chance, so the search did find *some* real structure — it converged
on a bad local optimum, not pure noise.

## Diagnosis (reported as a plausible explanation, not independently confirmed by further runs)

Inspecting the decoded output (`ESENANESSTSTREERSEHESE...`) shows a telltale failure pattern:
the hill-climber appears to have converged on an assignment that over-represents very common
short English sequences (E, S, T, R and bigrams like "ES," "RE," "TE") rather than recovering
the actual symbol-to-letter mapping. With 54 unique ciphertext symbols mapping onto only 26
letters (roughly 2 symbols per letter on average), a search that only ever reassigns one
symbol to a new random letter (never swapping which letters two symbols currently hold) can
get trapped in a state where piling many symbols onto the few highest-frequency English
letters scores deceptively well under a quadgram model, without ever being forced to explore
the swap-based moves that would unwind that imbalance. This is a plausible, named account of
the failure mode, not independently verified by a follow-up diagnostic run this cycle.

## What remains open, not attempted this cycle

A revised solver with swap-based moves (exchanging which letter two already-assigned symbols
hold, not just reassigning one symbol to a fresh random letter) and/or a frequency-informed
initialization (seeding the most frequent ciphertext symbols toward English's own most frequent
letters, e.g. E/T/A/O/I/N, before hill-climbing) are both named, concrete next steps — not run
here, since making a new design decision immediately after seeing this run's own result would
be exactly the kind of outcome-directed re-tuning this project's discipline exists to prevent.
Either would need its own fresh precommitment.

## Decision

SQ-2 is no longer entirely unstarted — a first, disclosed, honestly-reported attempt now
exists, including a real tooling limitation worth having on record before anyone points a
similar method at Z13, which is exactly SQ-2's own stated purpose ("validate tooling... before
trusting any method on Z13"). This result is itself useful evidence: a naive hill-climbing
implementation is not automatically sufficient, even on a cipher with a fully known answer key
and a real academic reference corpus — a caution worth remembering if a future cycle is ever
tempted to run an unvalidated method directly against Z13's own unsolved ciphertext.
