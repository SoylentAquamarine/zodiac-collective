#!/usr/bin/env python3
"""SQ-2: Z408 reproduction attempt v3 -- perturbed-best-injection ("basin hopping") restarts.

Precommitment: logs/2026-10-12-sq2-z408-v3-basin-hopping-selfreview.md (written and frozen
before this ran). The known plaintext is loaded only for the final accuracy comparison, after
the search is complete.

Isolated change from v2 (data/scripts/sq2_z408_hillclimb_solver_v2.py): restart strategy only.
Restarts 1-2 are identical to v2 (frequency-seeded, then random). Restarts 3-60 alternate
between a fresh random restart (as v2) and a "perturbed-best" restart that starts from the best
mapping found so far across all completed restarts, with K random symbol-letter reassignments
applied first (K drawn from {2,4,6,8}, fixed before running). Quadgram model, move mix,
annealing schedule, and restart/iteration counts are all unchanged from v2.

Usage:
    python data/scripts/sq2_z408_hillclimb_solver_v3.py
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
OUT_PATH = ROOT / "data/derived/sq2-z408-hillclimb-v3-result.md"

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
PERTURB_K_CHOICES = (2, 4, 6, 8)


def load_cipher_symbols(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    return "".join(line for line in text.splitlines())


def letters_only_text(path: Path) -> str:
    raw = path.read_text(encoding="utf-8", errors="ignore").upper()
    return re.sub(r"[^A-Z]", "", raw)


def build_quadgram_model(letters_only: str) -> tuple[dict[str, float], float]:
    counts: dict[str, int] = {}
    for i in range(len(letters_only) - 3):
        q = letters_only[i:i + 4]
        counts[q] = counts.get(q, 0) + 1
    total = sum(counts.values())
    floor = math.log(0.01 / total)
    log_probs = {q: math.log(c / total) for q, c in counts.items()}
    return log_probs, floor


def build_unigram_rank(letters_only: str) -> list[str]:
    counts = {L: 0 for L in LETTERS}
    for ch in letters_only:
        counts[ch] += 1
    return sorted(LETTERS, key=lambda L: -counts[L])


def frequency_informed_seed(cipher: str, symbols: list[str], letter_rank: list[str]) -> dict[str, str]:
    sym_freq = {s: cipher.count(s) for s in symbols}
    symbols_by_freq = sorted(symbols, key=lambda s: -sym_freq[s])
    mapping = {}
    for i, s in enumerate(symbols_by_freq):
        mapping[s] = letter_rank[i % 26]
    return mapping


def perturb_mapping(mapping: dict[str, str], symbols: list[str], k: int, rng: random.Random) -> dict[str, str]:
    new_mapping = dict(mapping)
    chosen = rng.sample(symbols, min(k, len(symbols)))
    for sym in chosen:
        new_mapping[sym] = rng.choice(LETTERS)
    return new_mapping


def score_text(text: str, log_probs: dict[str, float], floor: float) -> float:
    s = 0.0
    for i in range(len(text) - 3):
        q = text[i:i + 4]
        s += log_probs.get(q, floor)
    return s


def decode(cipher: str, mapping: dict[str, str]) -> str:
    return "".join(mapping[c] for c in cipher)


def hillclimb_restart(cipher: str, symbols: list[str], log_probs, floor,
                       rng: random.Random, iters: int, initial_mapping: dict[str, str]) -> tuple[dict[str, str], float]:
    mapping = dict(initial_mapping)
    current_text = decode(cipher, mapping)
    current_score = score_text(current_text, log_probs, floor)
    best_mapping, best_score = dict(mapping), current_score

    temp = 4.0
    cooling = 0.9995
    for it in range(iters):
        temp *= cooling
        do_swap = rng.random() < 0.5

        if do_swap:
            s1, s2 = rng.sample(symbols, 2)
            if mapping[s1] == mapping[s2]:
                continue
            old1, old2 = mapping[s1], mapping[s2]
            mapping[s1], mapping[s2] = old2, old1
        else:
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
            if do_swap:
                mapping[s1], mapping[s2] = old1, old2
            else:
                mapping[sym] = old_letter
    return best_mapping, best_score


def letter_freq_profile(text: str) -> dict[str, float]:
    counts = {L: 0 for L in LETTERS}
    for ch in text:
        if ch in counts:
            counts[ch] += 1
    n = max(len(text), 1)
    return {L: counts[L] / n for L in LETTERS}


def main() -> None:
    started = time.time()
    cipher = load_cipher_symbols(CIPHER_PATH)
    symbols = sorted(set(cipher))
    corpus_letters = letters_only_text(CORPUS_PATH)
    log_probs, floor = build_quadgram_model(corpus_letters)
    letter_rank = build_unigram_rank(corpus_letters)
    print(f"[{time.time()-started:6.1f}s] cipher length={len(cipher)} unique_symbols={len(symbols)} "
          f"letter_rank={''.join(letter_rank)}")

    rng = random.Random(20261012)
    RESTARTS = 60
    ITERS_PER_RESTART = 12000

    best_overall_mapping, best_overall_score = None, -1e18
    restart_log = []
    for r in range(RESTARTS):
        if r == 0:
            strategy = "freq-seeded"
            initial = frequency_informed_seed(cipher, symbols, letter_rank)
        elif r == 1:
            strategy = "random"
            initial = {s: rng.choice(LETTERS) for s in symbols}
        elif r % 2 == 0:
            k = rng.choice(PERTURB_K_CHOICES)
            strategy = f"perturbed-best(k={k})"
            initial = perturb_mapping(best_overall_mapping, symbols, k, rng)
        else:
            strategy = "random"
            initial = {s: rng.choice(LETTERS) for s in symbols}

        mapping, score = hillclimb_restart(cipher, symbols, log_probs, floor, rng, ITERS_PER_RESTART, initial)
        restart_log.append((r, strategy, score))
        if score > best_overall_score:
            best_overall_score = score
            best_overall_mapping = mapping
        if r % 10 == 0 or r == RESTARTS - 1:
            print(f"[{time.time()-started:6.1f}s] restart {r+1}/{RESTARTS} strategy={strategy} "
                  f"best_score_so_far={best_overall_score:.1f}")

    decoded = decode(cipher, best_overall_mapping)
    elapsed = time.time() - started

    known_plain = "".join(PLAIN_PATH.read_text(encoding="utf-8").splitlines())
    matches = sum(1 for a, b in zip(decoded, known_plain) if a == b)
    accuracy = matches / len(known_plain)

    v1_profile_note = letter_freq_profile(decoded)
    top5 = sorted(v1_profile_note.items(), key=lambda kv: -kv[1])[:5]
    top5_str = ", ".join(f"{L}:{p:.3f}" for L, p in top5)

    perturbed_best_scores = [s for (r, strat, s) in restart_log if strat.startswith("perturbed-best")]
    random_scores = [s for (r, strat, s) in restart_log if strat == "random"]

    print(f"[{elapsed:6.1f}s] DONE. accuracy={accuracy:.4f} ({matches}/{len(known_plain)})")
    print(f"decoded:  {decoded}")
    print(f"known:    {known_plain}")
    print(f"top5 decoded-letter freq: {top5_str}")

    report = f"""# SQ-2 — Z408 hill-climbing reproduction result v3 (perturbed-best-injection restarts)

Precommitment: `logs/2026-10-12-sq2-z408-v3-basin-hopping-selfreview.md`.

- Restarts: {RESTARTS} (restart 1 freq-seeded, restart 2 random, restarts 3-{RESTARTS} alternating
  perturbed-best / random), iterations per restart: {ITERS_PER_RESTART}
- 50% swap moves / 50% reassign moves (unchanged from v2)
- Wall-clock time: {elapsed:.1f}s
- Best quadgram log-likelihood score: {best_overall_score:.2f}
- Per-character accuracy against known plaintext (compared only after the search completed): **{accuracy:.4f}** ({matches}/{len(known_plain)})
- v1 accuracy (blind restarts): 0.1887 (77/408)
- v2 accuracy (swap moves + frequency seeding, no history reuse): 0.2574 (105/408)
- Top-5 most frequent letters in the v3 best decode: {top5_str}
- Mean best-score across {len(perturbed_best_scores)} perturbed-best restarts: {sum(perturbed_best_scores)/max(len(perturbed_best_scores),1):.1f}
- Mean best-score across {len(random_scores)} plain-random restarts (this run): {sum(random_scores)/max(len(random_scores),1):.1f}

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
