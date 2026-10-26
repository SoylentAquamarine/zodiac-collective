#!/usr/bin/env python3
"""Reproduce PR #11 scores with a second corpus. Usage: script <path to 2852-0.txt>
Precommitment: logs/2026-10-26-sq2-pr11-second-corpus-reproduction-selfreview.md."""
import math, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import sq2_z408_hillclimb_solver_v4 as v4
R = v4.ROOT
raw = Path(sys.argv[1]).read_text(encoding="utf-8", errors="replace")
def letters(s): return re.sub(r"[^A-Z]", "", s.upper())
a = raw.index("*** START OF"); b = raw.index("*** END OF")
corpora = {"whole": letters(raw), "markers": letters(raw[a:b])}
truth = "".join(v4.PLAIN_PATH.read_text().splitlines())
def block(p): return re.search(r"```\n([A-Z]+)\n```", Path(p).read_text()).group(1)
texts = {"truth": truth, "v3": block(R/"data/derived/sq2-z408-hillclimb-v3-result.md"),
         "v4": block(R/"data/derived/sq2-z408-hillclimb-v4-result.md")}
for name, corpus in corpora.items():
    print(f"corpus {name}: letters={len(corpus)}")
    for n in (1, 2, 3, 4):
        if n == 4:
            lp, fl = v4.build_quadgram_model(corpus)
            sc = {k: sum(lp.get(t[i:i+4], fl) for i in range(len(t)-3)) for k, t in texts.items()}
        else:
            cnt, ctx = {}, {}
            for i in range(len(corpus)-n+1):
                g = corpus[i:i+n]; cnt[g] = cnt.get(g, 0)+1; ctx[g[:-1]] = ctx.get(g[:-1], 0)+1
            sc = {k: sum(math.log((cnt.get(t[i:i+n], 0)+0.5)/(ctx.get(t[i:i+n-1], 0)+13)) for i in range(len(t)-n+1)) for k, t in texts.items()}
        print(f"  order {n}: " + "  ".join(f"{k}={v:.1f}" for k, v in sc.items()) + f"  truth-v3={sc['truth']-sc['v3']:.1f} best={max(sc, key=sc.get)}")
