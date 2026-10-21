#!/usr/bin/env python3
"""Post-hoc diagnostic (not precommitted as an experiment; disclosed as such): is Z408 solver failure a
search failure or an objective failure? Scores the TRUE plaintext and v3's/v4's found decodes under
the quadgram-only objective (v1-v3) and the quadgram+unigram-KL objective (v4). Known plaintext is used
here only for this diagnostic, after all search runs finished."""
import math, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import sq2_z408_hillclimb_solver_v4 as v4
R = v4.ROOT
corpus = v4.letters_only_text(v4.CORPUS_PATH)
lp, fl = v4.build_quadgram_model(corpus)
for L in v4.LETTERS:
    v4.CORPUS_UNI[L] = max(corpus.count(L) / len(corpus), 1e-6)
truth = "".join(v4.PLAIN_PATH.read_text().splitlines())
def block(path):
    t = Path(path).read_text()
    m = re.search(r"```\n([A-Z]+)\n```", t)
    return m.group(1)
d3 = block(R / "data/derived/sq2-z408-hillclimb-v3-result.md")
d4 = block(R / "data/derived/sq2-z408-hillclimb-v4-result.md")
def quad(t):
    return sum(lp.get(t[i:i+4], fl) for i in range(len(t) - 3))
v4.LAMBDA = 1.0
for name, t in [("truth", truth), ("v3 decode", d3), ("v4 decode", d4)]:
    print(f"{name:10s} quadgram-only={quad(t):9.1f}  v4-objective={v4.score_text(t, lp, fl):9.1f}")
