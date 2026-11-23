"""A6 production runner, GENERATOR HALF (length-13 windows only). Implements D5, D6, D9-D15 window
selection, plant/C1/C2/C3 construction, symbol labelling, manifest and fail-closed assertions.
Does NOT run the solver, does NOT score, does NOT fetch or read any real source. Cipher-only.
Frozen specs: logs/2026-11-18-a6-operational-freeze.md (D1-D8), 2026-11-23-a6-addendum-d9-d12-freeze.md,
2026-11-23-a6-addendum-d13-d15-freeze.md, 2026-11-14-z13-pre-score-addendum-freeze.md (A1-A8)."""
import hashlib, json, random, re
from collections import Counter
from pathlib import Path

BASE_SEED = 20261113
TARGET13 = (3, 2, 2, 2, 1, 1, 1, 1)
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
RESTARTS = 20
CAND_CAP = 100_000
C3_CAP = 1000
C1_CAP = 100

class FailClosed(Exception): pass

def require_source_pin(pin_path, text):
    """Assertion 5. Requires a pin file and verifies the actual normalized-text bytes."""
    if not pin_path:
        raise FailClosed("source-pin path required: runner must abort (assertion 5)")
    p = Path(pin_path)
    if not p.is_file():
        raise FailClosed("source-pin file absent: runner must abort (assertion 5)")
    pin_text = p.read_text(encoding="utf-8")
    match = re.search(r"(?im)^\\s*normalized_text_sha256\\s*[:=]\\s*([0-9a-f]{64})\\s*$", pin_text)
    if not match:
        raise FailClosed("source-pin lacks normalized_text_sha256 (assertion 5)")
    if not re.fullmatch(r"[A-Z]+", text):
        raise FailClosed("normalized text must be non-empty A-Z (assertion 5)")
    actual = hashlib.sha256(text.encode("ascii")).hexdigest()
    if actual != match.group(1):
        raise FailClosed("SHA-256 of loaded normalized text does not match source pin (assertion 5)")
    return actual

def partitions(n, maxpart=None):
    maxpart = maxpart or n
    if n == 0: yield (); return
    for k in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - k, k): yield (k,) + rest

def first_occurrence_order(window):
    seen = []
    for ch in window:
        if ch not in seen: seen.append(ch)
    return seen

def feasible_splits(window, target):
    """D5/D13: tuples of per-letter descending partitions, letters in first-occurrence order,
    in lexicographic order of the tuple; keep those whose merged multiset equals target."""
    counts = Counter(window); order = first_occurrence_order(window)
    per = [sorted(partitions(counts[c])) for c in order]
    tgt = sorted(target, reverse=True); out = []
    def rec(i, chosen, remaining):
        if i == len(order):
            if not remaining: out.append(tuple(chosen))
            return
        for part in per[i]:
            rem = list(remaining); ok = True
            for s in part:
                if s in rem: rem.remove(s)
                else: ok = False; break
            if ok: rec(i + 1, chosen + [part], rem)
    rec(0, [], tgt)
    return out

def build_class_structure(window, split, gen):
    """D6 + D13. Returns (symbol_per_position, group_sizes). One shuffle per distinct letter in
    first-occurrence order; groups in descending size; groups numbered in processing order;
    labels = gen.sample(range(54), c) as the LAST draw."""
    order = first_occurrence_order(window); group_positions = []
    for letter, part in zip(order, split):
        occ = [i for i, c in enumerate(window) if c == letter]
        gen.shuffle(occ); pos = 0
        for size in sorted(part, reverse=True):
            group_positions.append(sorted(occ[pos:pos + size])); pos += size
    c = len(group_positions)
    S = gen.sample(range(54), c)
    sym = [None] * len(window)
    for g, ps in enumerate(group_positions):
        for p in ps: sym[p] = S[g]
    return sym, [len(g) for g in group_positions], S

def mult_vector(sym): return tuple(sorted(Counter(sym).values(), reverse=True))

def select_windows(text, n_windows, L=13, target=TARGET13):
    """D14 for one length. Returns accepted [(start, w)], rejected count. Stream = Random(BASE_SEED)."""
    stream = random.Random(BASE_SEED); accepted = []; rejected = 0; tries = 0
    while len(accepted) < n_windows:
        tries += 1
        if tries > CAND_CAP: raise FailClosed("candidate cap reached (D14)")
        start = stream.randrange(0, len(text) - L + 1)
        if any(start < s + L and s < start + L for s, _ in accepted): rejected += 1; continue
        if not feasible_splits(text[start:start + L], target): rejected += 1; continue
        accepted.append((start, len(accepted)))
    return accepted, rejected

def unigram_weights(text):
    cnt = Counter(text); return [cnt[ch] for ch in ALPHABET]

def make_window(text, start, w, weights, target=TARGET13):
    P = text[start:start + sum(target)]
    n = len(P); base = BASE_SEED + w * 1000
    plant_gen = random.Random(base + 7)
    splits = feasible_splits(P, target)
    split = splits[plant_gen.randrange(len(splits))]
    C, sizes, S = build_class_structure(P, split, plant_gen)
    rec = {"w": w, "start": start, "P": P, "plant_C": C, "plant_S": S, "split_index": splits.index(split), "N": len(splits)}
    # D10 C1
    g1 = random.Random(base + 13); pi = list(range(n)); g1.shuffle(pi); tries = 1
    while pi == list(range(n)) or "".join(P[i] for i in pi) == P:
        if tries >= C1_CAP: raise FailClosed("C1 degenerate after 100 shuffles")
        g1.shuffle(pi); tries += 1          # in-place re-shuffle: OPEN reading, see result log
    rec["c1_pi"] = pi; rec["c1_P"] = "".join(P[i] for i in pi); rec["c1_C"] = [C[i] for i in pi]
    # D11 C2
    rec["c2_P"] = P[::-1]; rec["c2_C"] = C[::-1]; rec["c2_degenerate"] = (P == P[::-1])
    # D12 C3
    g3 = random.Random(base + 11); draws = 0
    while True:
        draws += 1
        if draws > C3_CAP: raise FailClosed("C3 redraw cap reached (D12)")
        L3 = "".join(g3.choices(ALPHABET, weights=weights, k=n))
        sp3 = feasible_splits(L3, target)
        if sp3: break
    split3 = sp3[g3.randrange(len(sp3))]
    C3, sizes3, S3 = build_class_structure(L3, split3, g3)
    rec.update({"c3_P": L3, "c3_C": C3, "c3_S": S3, "c3_redraws": draws - 1, "c3_split_index": sp3.index(split3)})
    # assertions 3, 9, 11
    assert mult_vector(C) == tuple(target), "A3 plant vector"
    for k, cc in (("c1", rec["c1_C"]), ("c2", rec["c2_C"]), ("c3", C3)):
        assert mult_vector(cc) == tuple(target), f"assertion 9 {k}"
    assert len(set(S)) == len(S) and all(0 <= s < 54 for s in S) and len(set(S3)) == len(S3), "assertion 11"
    return rec

def seed_schedule(w):
    base = BASE_SEED + w * 1000
    return [base + 7, base + 11, base + 13] + [base + 100 + r for r in range(RESTARTS)]

def generate_manifest(text, n_windows=100):
    """Generator-only helper for synthetic tests; it does not authorize a real-source run."""
    acc, rejected = select_windows(text, n_windows)
    weights = unigram_weights(text)
    assert [w for _, w in acc] == list(range(n_windows)), "assertion 12 indices"
    spans = sorted(s for s, _ in acc); assert all(b - a >= 13 for a, b in zip(spans, spans[1:])), "assertion 12 overlap"
    seeds = [BASE_SEED] + [s for _, w in acc for s in seed_schedule(w)]
    assert len(seeds) == len(set(seeds)), "assertion 8 duplicate seed"
    wins = [make_window(text, st, w, weights) for st, w in acc]
    return {"n_windows": n_windows, "rejected_candidates_len13": rejected, "n_seeds": len(seeds), "windows": wins}

def run(text, n_windows=100, pin_path=None):
    """Production entry point. Assertion 5 is mandatory; synthetic tests use generate_manifest()."""
    require_source_pin(pin_path, text)
    return generate_manifest(text, n_windows)

def manifest_bytes(m): return json.dumps(m, sort_keys=True, separators=(",", ":")).encode()
