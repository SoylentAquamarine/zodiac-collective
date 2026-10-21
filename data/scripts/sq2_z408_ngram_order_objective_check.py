#!/usr/bin/env python3
"""Score true Z408 plaintext vs v3/v4 degenerate decodes under n-gram orders 1-4 built from the on-file
Pride & Prejudice corpus. Precommitment: logs/2026-10-21-sq2-z408-ngram-order-objective-check-selfreview.md."""
import math, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import sq2_z408_hillclimb_solver_v4 as v4
R = v4.ROOT
corpus = v4.letters_only_text(v4.CORPUS_PATH)
truth = "".join(v4.PLAIN_PATH.read_text().splitlines())
def block(p):
    return re.search(r"```\n([A-Z]+)\n```", Path(p).read_text()).group(1)
texts = {"truth": truth,
         "v3 decode": block(R / "data/derived/sq2-z408-hillclimb-v3-result.md"),
         "v4 decode": block(R / "data/derived/sq2-z408-hillclimb-v4-result.md")}
def model(n):
    cnt, ctx = {}, {}
    for i in range(len(corpus) - n + 1):
        g = corpus[i:i+n]; cnt[g] = cnt.get(g, 0) + 1; ctx[g[:-1]] = ctx.get(g[:-1], 0) + 1
    return cnt, ctx
def score(t, n, cnt, ctx):
    s = 0.0
    if n == 4:
        lp, fl = v4.build_quadgram_model(corpus)
        return sum(lp.get(t[i:i+4], fl) for i in range(len(t) - 3))
    for i in range(len(t) - n + 1):
        g = t[i:i+n]
        s += math.log((cnt.get(g, 0) + 0.5) / (ctx.get(g[:-1], 0) + 0.5 * 26))
    return s
print(f"corpus letters={len(corpus)}")
for n in (1, 2, 3, 4):
    cnt, ctx = model(n)
    sc = {k: score(t, n, cnt, ctx) for k, t in texts.items()}
    rank = sorted(sc, key=sc.get, reverse=True)
    print(f"order {n}: " + "  ".join(f"{k}={v:.1f}" for k, v in sc.items()) + f"  | best={rank[0]}")
