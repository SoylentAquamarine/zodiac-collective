#!/usr/bin/env python3
"""SQ-2: independent Z408 reproduction via quadgram-scored hill-climbing.

Precommitment: logs/2026-10-11-sq2-z408-reproduction-selfreview.md (written and frozen
before this ran). The known plaintext is loaded only for the final accuracy comparison,
after the search is complete -- it is never referenced inside score() or the search loop.

Usage:
    python data/scripts/sq2_z408_hillclimb_solver.py
"""
from __future__ import annotations

import math
import random
import re
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CIPHER_PATH = ROOT / "data/external-sources/azdecrypt-doranchak-2026-09-27/z408-cipher.txt"
PLAIN_PATH = ROOT / "data/external-sources/azdecrypt-doranchak-2026-09-27/z408-solved.txt"
CORPUS_PATH = ROOT / "data/external-sources/gutenberg-1342-2026-09-29/pride_prejudice.txt"
OUT_PATH = ROOT / "data/derived/sq2-z408-hillclimb-result.md"

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def load_cipher_symbols(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    return "".join(line for line in text.splitlines())


def build_quadgram_model(path: Path) -> dict[str, float]:
    raw = path.read_text(encoding="utf-8", errors="ignore").upper()
    letters_only = re.sub(r"[^A-Z]", "", raw)
    counts: dict[str, int] = {}
    for i in range(len(letters_only) - 3):
        q = letters_only[i:i + 4]
        counts[q] = counts.get(q, 0) + 1
    total = sum(counts.values())
    floor = math.log(0.01 / total)  # floor for unseen quadgrams
    log_probs = {q: math.log(c / total) for q, c in counts.items()}
    return log_probs, floor


def score_text(text: str, log_probs: dict[str, float], floor: float) -> float:
    s = 0.0
    for i in range(len(text) - 3):
        q = text[i:i + 4]
        s += log_probs.get(q, floor)
    return s


def decode(cipher: str, mapping: dict[str, str]) -> str:
    return "".join(mapping[c] for c in cipher)


def hillclimb_restart(cipher: str, symbols: list[str], log_probs, floor, rng: random.Random,
                       iters: int) -> tuple[dict[str, str], float]:
    mapping = {s: rng.choice(LETTERS) for s in symbols}
    current_text = decode(cipher, mapping)
    current_score = score_text(current_text, log_probs, floor)
    best_mapping, best_score = dict(mapping), current_score

    temp = 4.0
    cooling = 0.9995
    for it in range(iters):
        temp *= cooling
        sym = rng.choice(symbols)
        old_letter = mapping[sym]
        new_letter = rng.choice(LETTERS)
        if new_letter == old_letter:
            continue
        mapping[sym] = new_letter
        new_text = decode(cipher, mapping)
        new_score = score_text(new_text, log_probs, floor)
        delta = new_score - current_score
        if delta >= 0 or rng.random() < math.exp(max(delta, -50) / max(temp, 1e-6)):
            current_score = new_score
            if current_score > best_score:
                best_score = current_score
                best_mapping = dict(mapping)
        else:
            mapping[sym] = old_letter
    return best_mapping, best_score


def main() -> None:
    started = time.time()
    cipher = load_cipher_symbols(CIPHER_PATH)
    symbols = sorted(set(cipher))
    log_probs, floor = build_quadgram_model(CORPUS_PATH)
    print(f"[{time.time()-started:6.1f}s] cipher length={len(cipher)} unique_symbols={len(symbols)} "
          f"quadgram_types={len(log_probs)}")

    rng = random.Random(20261011)
    RESTARTS = 60
    ITERS_PER_RESTART = 12000

    best_overall_mapping, best_overall_score = None, -1e18
    for r in range(RESTARTS):
        mapping, score = hillclimb_restart(cipher, symbols, log_probs, floor, rng, ITERS_PER_RESTART)
        if score > best_overall_score:
            best_overall_score = score
            best_overall_mapping = mapping
        if r % 10 == 0 or r == RESTARTS - 1:
            print(f"[{time.time()-started:6.1f}s] restart {r+1}/{RESTARTS} best_score_so_far={best_overall_score:.1f}")

    decoded = decode(cipher, best_overall_mapping)
    elapsed = time.time() - started

    # Only now, after the search is fully complete, load the known plaintext for comparison.
    known_plain = "".join(PLAIN_PATH.read_text(encoding="utf-8").splitlines())
    matches = sum(1 for a, b in zip(decoded, known_plain) if a == b)
    accuracy = matches / len(known_plain)

    print(f"[{elapsed:6.1f}s] DONE. accuracy={accuracy:.4f} ({matches}/{len(known_plain)})")
    print(f"decoded:  {decoded}")
    print(f"known:    {known_plain}")

    report = f"""# SQ-2 — Z408 hill-climbing reproduction result

Precommitment: `logs/2026-10-11-sq2-z408-reproduction-selfreview.md`.

- Restarts: {RESTARTS}, iterations per restart: {ITERS_PER_RESTART}
- Wall-clock time: {elapsed:.1f}s
- Best quadgram log-likelihood score: {best_overall_score:.2f}
- Per-character accuracy against known plaintext (compared only after the search completed): **{accuracy:.4f}** ({matches}/{len(known_plain)})

## Decoded text (best-scoring hill-climb result)

```
{decoded}
```

## Known plaintext (for comparison only, not used during search)

```
{known_plain}
```
"""
    OUT_PATH.write_text(report, encoding="utf-8")
    print(f"wrote {OUT_PATH}")


if __name__ == "__main__":
    main()
