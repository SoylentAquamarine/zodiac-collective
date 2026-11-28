# D10 retry discriminator — independent reproduction — 2026-11-28

**Scope:** synthetic AABC window only; no source text, solver integration, Z13 scoring or suspect inference.

Production generator: `data/scripts/a6_runner_generator.py`, blob `ac8023afec1e2931af5b45c46f94f01c213dc269`.
Production tests: `data/scripts/a6_runner_generator_tests.py`, blob `34321b848fc53183ee349c067c24b93ece644ccd`.

## Independent reproduction

Using Python's `random.Random(24)` with a four-position permutation:

- First shuffle: `[1, 0, 2, 3]`
- Second shuffle in place: `[3, 2, 1, 0]`
- Second shuffle from identity using the same advanced RNG state: `[3, 2, 0, 1]`

The two interpretations produce different permutations. The production generator currently uses the in-place interpretation after a degenerate C1 draw. The checked-in production test file has no forced-degenerate retry fixture.

## Conclusion

The toy demonstrates that the specification ambiguity is consequential. It does not determine which interpretation the Research Director intends and does not test the production retry branch.

**Next:** Director freezes RNG state/draw order/retry cap and supplies a hand-derived expected permutation; then add a production forced-retry known-answer fixture before any Z13 scoring.
