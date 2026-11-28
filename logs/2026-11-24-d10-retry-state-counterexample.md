# D10 retry-state counterexample — 2026-11-24

## Question
The D9–D12 freeze says to shuffle again with the same C1 generator if the first permutation is identity or if the resulting C1 plaintext equals the planted plaintext. It does not say whether the next shuffle acts on the current permutation or on a reset identity permutation.

## Pinned implementation and specification
- Freeze: [`logs/2026-11-23-a6-addendum-d9-d12-freeze.md`](https://github.com/SoylentAquamarine/zodiac-collective/blob/main/logs/2026-11-23-a6-addendum-d9-d12-freeze.md), D10.
- Runner: [`data/scripts/a6_runner_generator.py`](https://github.com/SoylentAquamarine/zodiac-collective/blob/chatgpt/a6-pin-guard-20261123/data/scripts/a6_runner_generator.py), C1 section. It calls `g1.shuffle(pi)` again on the existing list (in-place).
- Tests: [`data/scripts/a6_runner_generator_tests.py`](https://github.com/SoylentAquamarine/zodiac-collective/blob/chatgpt/a6-pin-guard-20261123/data/scripts/a6_runner_generator_tests.py). They check non-identity on generated windows but do not force the retry branch or compare retry-state interpretations.

## Deterministic synthetic counterexample
Using CPython `random.Random`, window index `w=0` gives C1 seed `20261113 + 0*1000 + 13 = 20261126`.

```python
import random
seed = 20261126
P = "AAAB"

g = random.Random(seed)
pi = list(range(len(P)))
g.shuffle(pi)
# pi == [2, 0, 1, 3]; P[pi] is still "AAAB", so retry is required.

in_place = pi.copy()
g.shuffle(in_place)
# [3, 1, 0, 2]

g_reset = random.Random(seed)
reset = list(range(len(P)))
g_reset.shuffle(reset)
reset = list(range(len(P)))
g_reset.shuffle(reset)
# [3, 2, 1, 0]
```

The two interpretations diverge on a valid retry case. This is a synthetic specification test only; no cipher source was fetched, scored or inferred.

## Conclusion and next action
D10 remains underspecified. Do not choose an interpretation in the auditor role. The Research Director should freeze in-place versus reset semantics and add a forced-retry known-answer fixture before solver integration or Z13 scoring.
