# Execution — revised Z408 solver: real improvement, still a degenerate decode

Precommitment: `logs/2026-10-12-sq2-z408-revised-solver-selfreview.md` (frozen before this
ran). Script: `data/scripts/sq2_z408_hillclimb_solver_v2.py`. Full result:
`data/derived/sq2-z408-hillclimb-v2-result.md`.

## Result

60 random restarts (alternating frequency-seeded and random-start), 12,000 hill-climbing
iterations each, 50% swap moves / 50% reassign moves, 122.0 seconds total wall-clock time. Best
quadgram log-likelihood found: -4003.9. **Per-character accuracy against the known plaintext:
25.74% (105/408)**, up from the first attempt's 18.87% (77/408).

## Outcome vs. prediction

The stated prediction was "meaningfully above 18.87%, most likely in the 40%-70% range." **The
actual result (25.74%) is a real, measurable improvement over the first attempt — confirming
both changes (swap moves, frequency-informed seeding) help — but falls well short of the
predicted range.** Reported exactly as it came out, not reframed as a bigger win than it is.

**The decode is still visibly degenerate**: the best-scoring output
(`ESENINESSANTREERSESENEASEETENSERANOTASETASRERERAS...`) remains dominated by the same small
set of high-frequency English letter sequences (E, S, T, R, N) as the first attempt, just less
severely. This means the diagnosed failure mode from last cycle (piling too many ciphertext
symbols onto a handful of common letters) was only partially addressed by these two fixes, not
resolved.

## Honest interpretation

This is genuine, disclosed progress on SQ-2's own stated purpose (validating tooling before
ever trusting it on Z13) — and genuine, disclosed evidence that this family of fixes, while
real and directionally correct, is not sufficient on its own to reach a clean reproduction of a
historically-solved cipher at this length with this implementation. Quadgram-scored hill-
climbing with these move types is evidently harder to get right in practice than the
"standard, published technique" framing from the first attempt's precommitment suggested —
real published Z340/Z408 solvers typically use larger restart counts, longer per-restart
iteration budgets, and often additional refinements (e.g. bigram-informed proposal
distributions, simulated-annealing schedules tuned specifically to this problem class, or
hybrid local-search/genetic approaches) beyond the two changes tested here.

## What remains open, not attempted this cycle

A further-revised design (e.g., substantially more restarts/iterations, or a qualitatively
different proposal mechanism) would need its own fresh precommitment — not decided here,
consistent with this project's own discipline against chaining same-session re-tuning attempts
after seeing a result. Whether this specific solver implementation can reach a genuine
reproduction at all, versus needing a fundamentally different algorithm, is itself now a more
informed open question than it was before this cycle.

## Decision

SQ-2 now has two independent, honestly-reported data points (18.87%, 25.74%) rather than one.
Both results are useful, disclosed evidence about this implementation's real limits — not
treated as a step toward forcing a solve, and not hidden because they're unflattering.
