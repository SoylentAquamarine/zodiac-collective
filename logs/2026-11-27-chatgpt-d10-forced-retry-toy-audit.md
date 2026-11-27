# D10 forced-retry interpretation discriminator — 2026-11-27

**Scope:** standalone synthetic toy test of the two documented D10 interpretations. This is not a production-runner test, not a Z13 source test and not a Director ruling.

## Fixture
- Plaintext: P = AABC
- Python random seed: 24
- Initial permutation: [0, 1, 2, 3]
- First shuffle: [1, 0, 2, 3]
- Because the first two positions both contain A, the permuted text remains AABC and triggers a retry.

## Divergent second result
Using the same RNG stream:
- Re-shuffle the current permutation in place: [3, 2, 1, 0]
- Reset to identity before the retry shuffle: [3, 2, 0, 1]

Both are deterministic under their respective interpretations and differ. This demonstrates that the wording ambiguity is consequential, but does not choose which interpretation the frozen spec intends.

## Limits and decision
The production A6 tests do not force a degenerate C1 draw. No source pin, solver integration, Z13 score or suspect inference occurred. The Research Director must freeze the intended state transition and issue a hand-derived expected result before this is added as a production known-answer test.