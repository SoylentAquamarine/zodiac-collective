#!/usr/bin/env python3
"""Deterministic known-answer benchmark manifest (no scoring). Precommit: logs/2026-11-05-known-answer-benchmark-freeze-precommit.md"""
import hashlib, json, random, re, sys
SRC = sys.argv[1]; OUT = sys.argv[2]
SEED = 20261105; LENGTHS = [13, 100, 340, 408]; N = 50
raw = open(SRC, encoding="utf-8", errors="replace").read()
assert hashlib.sha256(open(SRC, "rb").read()).hexdigest() == "81300b79e8a8d65ac530a97578417d06137e3bbc90622a10a65e5036183d2500"
a = raw.index("*** START OF THE PROJECT GUTENBERG EBOOK 1342 ***"); a = raw.index("\n", a)
b = raw.index("*** END OF THE PROJECT GUTENBERG EBOOK 1342 ***")
body = re.sub(r"[^a-z]", "", raw[a:b].lower())
rng = random.Random(SEED)
h = lambda s: hashlib.sha256(s.encode()).hexdigest()
freq = {}
for c in body: freq[c] = freq.get(c, 0) + 1
letters = sorted(freq); weights = [freq[c] for c in letters]
used = []  # (start,end)
def free(s, e): return all(e <= u or s >= v for u, v in used)
items = []
for L in LENGTHS:
    for i in range(N):
        while True:
            s = rng.randrange(0, len(body) - L)
            if free(s, s + L): break
        used.append((s, s + L)); w = body[s:s + L]
        sh = list(w); rng.shuffle(sh); sh = "".join(sh)
        rv = w[::-1]
        rd = "".join(rng.choices(letters, weights, k=L))
        items.append(dict(len=L, idx=i, offset=s, sha256_true=h(w), sha256_c1_shuffle=h(sh), sha256_c2_reverse=h(rv), sha256_c3_unigram_random=h(rd)))
out = dict(seed=SEED, source_sha256="81300b79e8a8d65ac530a97578417d06137e3bbc90622a10a65e5036183d2500", body_letters=len(body), n_per_length=N, lengths=LENGTHS, items=items)
json.dump(out, open(OUT, "w"), indent=1)
print(len(items), "items; body letters", len(body), "; manifest sha256", hashlib.sha256(open(OUT, "rb").read()).hexdigest())
