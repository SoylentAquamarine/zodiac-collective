# D10 forced-retry discriminator — 2026-11-28

**Purpose:** produce a compact, hand-checkable synthetic fixture that forces the A6 C1 retry path and distinguishes in-place re-shuffle from reset-to-identity behavior. This is not a production test, solver run, source input or Z13 score.

## Pinned production context
- Production generator blob: `ac8023afec1e2931af5b45c46f94f01c213dc269`.
- Existing test blob: `34321b848fc53183ee349c067c24b93ece644ccd`.
- Production C1 RNG seed schedule for window 0: base `20261113`, C1 seed `20261126`.
- Production code currently shuffles the current permutation in place on retry. Existing tests do not force a degenerate retry.

## Fixture
- Synthetic length-13 input: `AAAAAAAAACAAA`.
- First shuffle: `[3,11,10,6,8,5,2,4,1,9,0,12,7]`.
- The sole `C` remains at index 9, so the shuffled text is unchanged and the retry condition fires.
- In-place second draw: `[4,11,3,8,9,7,12,2,0,10,1,6,5]`.
- Reset-to-identity second draw: `[7,1,0,4,9,12,11,6,10,2,8,3,5]`.

## Reproduction
Run:

```sh
python3 data/scripts/a6_d10_retry_discriminator.py
```

Expected: PASS; both paths retry exactly once and produce different final permutations.

## Decision boundary
The fixture demonstrates that the two plausible semantics are observably different under the production seed schedule. It does **not** choose which semantics are intended. The Research Director must freeze retry state, RNG consumption order and cap, then select the expected production known-answer output before Z13 scoring.
