# D10 forced-retry neutral fixture — cycle #179

**Date:** 2026-11-26 01:55 ET  
**Status:** synthetic specification fixture only; not Z13 evidence.

## Question
The Director's D10 rule says to shuffle again with the same generator when C1 is degenerate, but does not say whether the current permutation is shuffled in place again or reset to identity before the next shuffle. Production code currently re-shuffles in place and labels the interpretation OPEN.

## Reproduction
Use a four-position synthetic plaintext and a nonuniform class vector:

- P = ABAB
- C = [0, 1, 2, 3]
- D10 base = 5, so the C1 generator is Random(base + 13) = Random(18).

First shuffle: [2, 3, 0, 1]. The resulting plaintext remains ABAB, so the retry condition is met.

Second attempt:
- In-place interpretation: [3, 1, 2, 0] → plaintext BBAA; class vector [3, 1, 2, 0].
- Reset-to-identity interpretation: [1, 3, 0, 2] → plaintext BBAA; class vector [1, 3, 0, 2].

Both interpretations produce the same C1 plaintext but different C1 class vectors. The distinction therefore affects the joint permutation control even when the visible string is identical.

## Reproduction code
```python
import random

P = "ABAB"
C = [0, 1, 2, 3]

g = random.Random(18)
pi = list(range(4))
g.shuffle(pi)
assert pi == [2, 3, 0, 1]
assert "".join(P[i] for i in pi) == P

g.shuffle(pi)                 # in-place retry
in_place = pi[:]

g2 = random.Random(18)
pi2 = list(range(4))
g2.shuffle(pi2)
pi2 = list(range(4))          # reset before retry
g2.shuffle(pi2)
reset = pi2[:]

assert in_place == [3, 1, 2, 0]
assert reset == [1, 3, 0, 2]
assert "".join(P[i] for i in in_place) == "BBAA"
assert "".join(P[i] for i in reset) == "BBAA"
assert [C[i] for i in in_place] != [C[i] for i in reset]
```

## Limits and decision
This fixture demonstrates the specification difference; it does not choose which interpretation is intended. It does not run the production generator, use a real source, score Z13, or identify a suspect. No production code was changed.

**Director decision required:** freeze whether retry preserves the current permutation or resets to identity, then add the selected behavior as a forced-retry known-answer fixture. Do not integrate the solver or score Z13 until D10 is frozen and the separate source/validation gates clear.
