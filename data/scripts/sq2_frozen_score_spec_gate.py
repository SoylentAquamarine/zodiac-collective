#!/usr/bin/env python3
"""Frozen score spec F + gates G1-G4. Precommitment: logs/2026-10-27-sq2-frozen-score-spec-gate-selfreview.md"""
import math, random, re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
raw = (ROOT/"data/external-sources/gutenberg-1342-2026-09-29/pride_prejudice.txt").read_text(encoding="utf-8", errors="replace")
a = raw.index("*** START OF"); b = raw.index("*** END OF")
C = re.sub(r"[^A-Z]", "", raw[a:b].upper())
cnt, ctx = {}, {}
for i in range(len(C)-3):
    g = C[i:i+4]; cnt[g] = cnt.get(g, 0)+1; ctx[g[:3]] = ctx.get(g[:3], 0)+1
def lp(g): return math.log((cnt.get(g, 0)+0.5)/(ctx.get(g[:3], 0)+13))
def score(t): return sum(lp(t[i:i+4]) for i in range(len(t)-3))
def block(p): return re.search(r"```\n([A-Z]+)\n```", Path(p).read_text()).group(1)
truth = "".join((ROOT/"data/external-sources/azdecrypt-doranchak-2026-09-27/z408-solved.txt").read_text().splitlines())
v3 = block(ROOT/"data/derived/sq2-z408-hillclimb-v3-result.md"); v4 = block(ROOT/"data/derived/sq2-z408-hillclimb-v4-result.md")
print(f"corpus letters={len(C)} truth={len(truth)} v3={len(v3)} v4={len(v4)}")
s = {k: score(t) for k, t in dict(truth=truth, v3=v3, v4=v4).items()}
print({k: round(v, 1) for k, v in s.items()}, "per-letter", {k: round(s[k]/len(t), 3) for k, t in dict(truth=truth, v3=v3, v4=v4).items()})
print("G1", "PASS" if s["truth"] > s["v3"] and s["truth"] > s["v4"] else "FAIL")
n = min(len(truth), len(v3)); w = n//4; wins = 0
for k in range(4):
    st, sv = score(truth[k*w:(k+1)*w]), score(v3[k*w:(k+1)*w]); wins += st > sv
    print(f" window {k}: truth={st:.1f} v3={sv:.1f}")
print(f"G2 truth wins {wins}/4 ->", "PASS" if wins >= 3 else "FAIL", f"(window={w}, lengths truth={len(truth)} v3={len(v3)})")
rng = random.Random(408); beat = 0
for _ in range(20):
    l = list(truth); rng.shuffle(l); beat += s["truth"] > score("".join(l))
print(f"G3 truth beats {beat}/20 shuffles ->", "PASS" if beat == 20 else "FAIL")
costs = sorted(((lp(truth[i:i+4]), i, truth[i:i+4], cnt.get(truth[i:i+4], 0)) for i in range(len(truth)-3)))[:15]
print("G4 costliest truth quadgrams (logp, pos, quad, corpus count):")
for c in costs: print(f"  {c[0]:.2f} {c[1]} {c[2]} {c[3]}  ctx: {truth[max(0,c[1]-3):c[1]+8]}")
unseen = sum(1 for i in range(len(truth)-3) if truth[i:i+4] not in cnt); unseen3 = sum(1 for i in range(len(v3)-3) if v3[i:i+4] not in cnt)
print(f"unseen quadgrams: truth {unseen}, v3 {unseen3}")
