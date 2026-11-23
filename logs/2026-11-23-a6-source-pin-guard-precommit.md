# Precommit: A6 production-runner source-pin guard audit — 2026-11-23

**Scope:** code integrity only; cipher-only; no suspect inference. No source retrieval, no scoring, no solver execution.

## Question
Does the current generator actually enforce frozen assertion 5 at the production entry point, and does assertion 8 cover every generator seed created by D9–D14?

## Precommitted checks
1. Calling the production entry point without a source-pin path must abort before window generation.
2. A pin whose normalized-text SHA-256 differs from the loaded A–Z text must abort.
3. A matching pin must pass the integrity gate.
4. The D4-as-written reference schedule over w=0..999 must reproduce 2,001 duplicate seed instances; the D9 schedule plus split/C1/C3 streams must have zero collisions.
5. Existing D5 hand cases, D6/D7 properties, deterministic manifest and plant/control multiplicity checks must remain unchanged.
6. Do not resolve D10's in-place-vs-reset re-shuffle ambiguity, D5's 34/100 enumeration strategy, text normalization, source selection or any scoring rule.

## Known limitations
The generator currently advertises length-13-only scope. This cycle will not claim D14's full 13/34/100 production pipeline or solver integration. The second-register source pin remains unfilled, so no real-source run is possible.

## Planned implementation
Separate the synthetic-test helper from the production entry point. Make production run() require a pin file and compare the actual SHA-256 of the normalized A–Z text with a named field in that file. Expand assertion 8 to include the window-selection, split, C1, C3 and restart streams. Replace the tautological D4 reference test with explicit schedule accounting.

A development test was run before this precommit while prototyping. The formal result below will be a fresh run against the published branch contents after this precommit commit.
