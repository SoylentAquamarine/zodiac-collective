#!/usr/bin/env python3
"""Synthetic D10 retry discriminator; does not import or modify production code.

Run:
    python3 data/scripts/a6_d10_retry_discriminator.py

The fixture forces the first shuffled permutation to preserve a 13-character
string because its sole C remains at index 9. It records both plausible retry
semantics; it does not choose which one the Research Director must freeze.
"""
import json
import random

P = "AAAAAAAAACAAA"
BASE_SEED = 20261113
C1_SEED = BASE_SEED + 13
RETRY_CAP = 100


def run(mode):
    rng = random.Random(C1_SEED)
    permutation = list(range(len(P)))
    rng.shuffle(permutation)
    first = permutation.copy()
    tries = 1
    while permutation == list(range(len(P))) or "".join(P[i] for i in permutation) == P:
        if tries >= RETRY_CAP:
            raise RuntimeError("C1 degenerate after retry cap")
        if mode == "reset":
            permutation = list(range(len(P)))
        elif mode != "inplace":
            raise ValueError(mode)
        rng.shuffle(permutation)
        tries += 1
    return {"mode": mode, "first": first, "final": permutation, "tries": tries}


inplace = run("inplace")
reset = run("reset")
assert inplace["first"] == reset["first"]
assert inplace["tries"] == reset["tries"] == 2
assert "".join(P[i] for i in inplace["first"]) == P
assert inplace["final"] == [4, 11, 3, 8, 9, 7, 12, 2, 0, 10, 1, 6, 5]
assert reset["final"] == [7, 1, 0, 4, 9, 12, 11, 6, 10, 2, 8, 3, 5]
assert inplace["final"] != reset["final"]
print(json.dumps({
    "input": P,
    "base_seed": BASE_SEED,
    "c1_rng_seed": C1_SEED,
    "inplace": inplace,
    "reset": reset,
    "status": "PASS: alternatives diverge; no semantics selected",
}, indent=2))
