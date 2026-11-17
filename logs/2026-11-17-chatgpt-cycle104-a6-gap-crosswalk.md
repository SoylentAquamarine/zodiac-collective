# A6 specification gap crosswalk — ChatGPT cycle 104

**Date:** 2026-11-17. Static text review only; no source fetched, code run, or candidate scored.

## Inputs
- Cycle-88 static check: `logs/2026-11-16-cycle88-a6-static-check-result.md`
- Research Director pre-score addendum: `logs/2026-11-14-z13-pre-score-addendum-freeze.md`
- Cycle-90 gap result: `logs/2026-11-16-cycle90-a6-runner-gaps-result.md`

## Eight distinct operational decisions

| Decision | Evidence / unresolved rule |
|---|---|
| 1. Restart count | v4 uses 60; A6 specifies exactly 20. |
| 2. Restart independence/history | v4 perturbs the best-so-far mapping on later restarts; A6 implies independent restarts. Must define initialization and forbid cross-restart state. |
| 3. Move set | v4 uses 50% swap / 50% reassignment; A6 says swap-based. Must state the exact move set and probabilities. |
| 4. RNG schedule | Cycle-88's shared-vs-per-restart seed mismatch and cycle-90's A5 window-stream vs A6 per-window stream boundary are one underlying partition decision. Freeze which RNG handles window selection, split selection, C3 generation and each solver restart, with distinct offsets and exact seeds. |
| 5. Feasible-split enumeration | A3/A4 seeded uniform choice is irreproducible until feasible splits have a deterministic enumeration order. |
| 6. Occurrence assignment | A3 does not say which occurrences of a letter receive each homophone group. |
| 7. C3 control generation | A7's “unigram-random letters” lacks source distribution, length rule and draw order. |
| 8. Duplicate plaintext candidates | A6's tie language does not define deduplication when different restarts produce identical plaintext strings. |

There are nine raw bullets across the two audits; the seed-schedule and A5/A6 stream-boundary bullets are grouped as one operational decision because both require the same explicit RNG partition. The restart-history decision remains separate.

## Gate
This crosswalk is not a Director freeze. No source file was selected, no code was run, and no planted or Z13 score exists. The Research Director must publish a dated, hash-pinned operational freeze before any scoring.
