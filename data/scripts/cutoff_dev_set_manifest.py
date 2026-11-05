#!/usr/bin/env python3
"""Deterministic cutoff-development manifest, disjoint from the benchmark (no scoring).
Precommit: logs/2026-11-05-cutoff-dev-set-freeze-precommit.md
usage: cutoff_dev_set_manifest.py SRC BENCHMARK_MANIFEST OUT"""
import hashlib, json, random, re, sys
SRC, BENCH, OUT = sys.argv[1:4]
SEED = 20261106; LENGTHS = [13, 100, 340, 408]; N = 50; BUF = 1000
SRCSHA = "81300b79e8a8d65ac530a97578417d06137e3bbc90622a10a65e5036183d2500"
assert hashlib.sha256(open(SRC, "rb").read()).hexdigest() == SRCSHA
raw = open(SRC, encoding="utf-8", errors="replace").read()
a = raw.index("*** START OF THE PROJECT GUTENBERG EBOOK 1342 ***"); a = raw.index("\n", a)
b = raw.index("*** END OF THE PROJECT GUTENBERG EBOOK 1342 ***")
body = re.sub(r"[^a-z]", "", raw[a:b].lower())
bm = json.load(open(BENCH)); assert bm["source_sha256"] == SRCSHA and bm["body_letters"] == len(body)
bench = [(i["offset"], i["offset"] + i["len"]) for i in bm["items"]]
rng = random.Random(SEED); h = lambda s: hashlib.sha256(s.encode()).hexdigest()
freq = {}
for c in body: freq[c] = freq.get(c, 0) + 1
letters = sorted(freq); weights = [freq[c] for c in letters]
used = []
def ok(s, e):
    if any(not (e + BUF <= u or s >= v + BUF) for u, v in bench): return False
    return all(e <= u or s >= v for u, v in used)
items = []
for L in LENGTHS:
    for i in range(N):
        while True:
            s = rng.randrange(0, len(body) - L)
            if ok(s, s + L): break
        used.append((s, s + L)); w = body[s:s + L]
        sh = list(w); rng.shuffle(sh); sh = "".join(sh)
        rd = "".join(rng.choices(letters, weights, k=L))
        items.append(dict(len=L, idx=i, offset=s, sha256_true=h(w), sha256_c1_shuffle=h(sh), sha256_c2_reverse=h(w[::-1]), sha256_c3_unigram_random=h(rd)))
out = dict(seed=SEED, buffer_letters=BUF, source_sha256=SRCSHA, benchmark_manifest_file="known-answer-benchmark-manifest.json", body_letters=len(body), n_per_length=N, lengths=LENGTHS, items=items)
json.dump(out, open(OUT, "w"), indent=1)
print(len(items), "items; manifest sha256", hashlib.sha256(open(OUT, "rb").read()).hexdigest())
