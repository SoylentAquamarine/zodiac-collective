#!/usr/bin/env python3
"""Chance-level permutation-test baseline for the Z408/Z340 5-of-47
homophone-coincidence count, per
logs/2026-09-27-sq3-homophone-chance-baseline-selfreview.md.

Rebuilds both solved keys directly from the verified source
(data/external-sources/azdecrypt-doranchak-2026-09-27/), restricts to the
47 symbols shared between the two ciphers' alphabets, then runs a
permutation test: how many coincidences would occur if Z340's 47 letters
(in symbol order) were randomly shuffled, preserving Z340's own real
per-symbol letter-frequency distribution exactly?

Usage:
    python methods/scripts/homophone_chance_baseline.py
"""

from __future__ import annotations

import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "data" / "external-sources" / "azdecrypt-doranchak-2026-09-27"
OUT_JSON = ROOT / "data" / "derived" / "homophone-chance-baseline-summary.json"
N_SHUFFLES = 10000
SEED = 20260927


def load_grid(path: Path) -> str:
    return "".join(line.rstrip("\n") for line in path.read_text(encoding="utf-8").splitlines() if line.strip())


def build_key(cipher_path: Path, plain_path: Path) -> dict[str, str]:
    cipher = load_grid(cipher_path)
    plain = load_grid(plain_path)
    key: dict[str, str] = {}
    for c, p in zip(cipher, plain):
        key[c] = p
    return key


def main() -> None:
    z408_key = build_key(SRC / "z408-cipher.txt", SRC / "z408-solved.txt")
    z340_key = build_key(SRC / "z340-cipher.txt", SRC / "z340-solved-transposed.txt")

    common = sorted(set(z408_key) & set(z340_key))
    z408_letters = [z408_key[s] for s in common]
    z340_letters = [z340_key[s] for s in common]
    n = len(common)
    observed = sum(1 for a, b in zip(z408_letters, z340_letters) if a == b)

    print(f"shared symbols: {n}, observed coincidences: {observed}")

    rng = random.Random(SEED)
    counts = []
    shuffled = list(z340_letters)
    for _ in range(N_SHUFFLES):
        rng.shuffle(shuffled)
        c = sum(1 for a, b in zip(z408_letters, shuffled) if a == b)
        counts.append(c)

    mean_null = sum(counts) / len(counts)
    p_le_observed = sum(1 for c in counts if c <= observed) / len(counts)
    p_ge_observed = sum(1 for c in counts if c >= observed) / len(counts)
    from collections import Counter
    dist = Counter(counts)

    print(f"null mean (over {N_SHUFFLES} shuffles): {mean_null:.3f}")
    print(f"P(null coincidences <= {observed}): {p_le_observed:.4f}")
    print(f"P(null coincidences >= {observed}): {p_ge_observed:.4f}")
    print(f"null distribution (count -> frequency): {sorted(dist.items())}")

    summary = {
        "design_log": "logs/2026-09-27-sq3-homophone-chance-baseline-selfreview.md",
        "n_shared_symbols": n,
        "observed_coincidences": observed,
        "n_shuffles": N_SHUFFLES,
        "seed": SEED,
        "null_mean": mean_null,
        "p_le_observed": p_le_observed,
        "p_ge_observed": p_ge_observed,
        "null_distribution": {str(k): v for k, v in sorted(dist.items())},
    }
    OUT_JSON.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {OUT_JSON}")


if __name__ == "__main__":
    main()
