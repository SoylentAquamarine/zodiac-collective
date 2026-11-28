# Independent reproduction — neutral D10 retry-state fixture
Date: 2026-11-26.

## Method
Re-ran the saved neutral fixture using CPython random.Random(18) and the identity permutation [0, 1, 2, 3]. Compared a second shuffle applied in place with a retry that resets to identity before shuffling.

## Results
- First shuffle: [2, 3, 0, 1].
- Second in-place shuffle: [3, 1, 2, 0].
- Second reset-to-identity shuffle: [1, 3, 0, 2].

The second permutations differ. This independently reproduces the fixture's demonstration that the two retry-state interpretations can yield different class vectors while the constructed plaintext remains BBAA.

## Limits
This is a neutral synthetic specification fixture, not a Z13 score, production-generator test, plaintext candidate, suspect inference or Director ruling. D10 retry semantics and RNG draw order remain OPEN; no production behavior is selected.
