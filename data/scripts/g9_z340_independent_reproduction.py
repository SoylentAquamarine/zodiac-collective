#!/usr/bin/env python3
"""Independent re-implementation of ChatGPT's G9 protocol (config/chatgpt.md, 64a75e2).
Usage: g9_z340_independent_reproduction.py 1661.txt z340-solved.txt  (pinned files, not committed)."""
import sys, re, math, json, hashlib
import numpy as np
def blob(b): return hashlib.sha1(b"blob %d\0" % len(b) + b).hexdigest()
raw_b = open(sys.argv[1], "rb").read(); tr_b = open(sys.argv[2], "rb").read()
assert blob(raw_b) == "70349ec04e577406123e9d89af4863cd610ccc1e"
assert blob(tr_b) == "74aa9b7c3bb925015938a685f17c1a5505cf40f2"
raw = raw_b.decode("utf8")
s = raw.index("To Sherlock Holmes she is always THE woman."); e = raw.index("End of the Project Gutenberg EBook", s)
lines = [l for l in raw[s:e].split("\n") if not re.match(r"^\s*ADVENTURE [IVXLC]+\. .*$", l.rstrip("\r")) and not re.match(r"^\s*[IVXLC]+\.\s*$", l.rstrip("\r"))]
clean = lambda x: re.sub(r"[^A-Z]", "", x.upper())
CC = clean("\n".join(lines)); truth = clean(tr_b.decode("utf8"))
assert len(CC) == 431195 and len(truth) == 340
enc = lambda x: np.frombuffer(x.encode(), dtype=np.uint8).astype(np.int64) - 65
def model(train):
    c = enc(train); k = (c[:-3]*26 + c[1:-2])*26 + c[2:-1]
    cnt = np.bincount(k*26 + c[3:], minlength=26**4).astype(float); ctx = np.bincount(k, minlength=26**3).astype(float)
    return np.log((cnt + .5) / (np.repeat(ctx, 26) + 13))
def score(lp, x):
    c = enc(x); return lp[((c[:-3]*26 + c[1:-2])*26 + c[2:-1])*26 + c[3:]].mean()
def ent(x):
    n = np.bincount(enc(x), minlength=26); p = n[n > 0]/len(x); return float(-(p*np.log2(p)).sum())
def pct(v, p):
    b = sorted(v); return b[min(len(b)-1, max(0, int(math.floor(p/100*(len(b)-1) + .5))))]
A = [chr(65+i) for i in range(26)]
ctrl = [(x, x*340) for x in A] + [(x+y, (x+y)*170) for x in A for y in A if x != y]
def run(frac, lo, hi):
    cut = math.floor(len(CC)*frac); lp = model(CC[:cut]); K = CC[cut:]
    W = [K[i:i+340] for i in range(0, len(K)-339, 340)]
    ws = [score(lp, w) for w in W]; wh = [ent(w) for w in W]
    b = dict(sLo=pct(ws, lo), sHi=pct(ws, hi), hLo=pct(wh, lo), hHi=pct(wh, hi))
    def v(x):
        sc, h = float(score(lp, x)), ent(x); so = b["sLo"] <= sc <= b["sHi"]; ho = b["hLo"] <= h <= b["hHi"]
        return dict(s=float(sc), h=h, sOK=bool(so), hOK=bool(ho), typical=bool(so and ho))
    acc = [i for i, x in ctrl if v(x)["typical"]]; tv = v(truth)
    # mulberry32 Fisher-Yates seed 340 (to match the PR's shuffle draws)
    st = [340 & 0xFFFFFFFF]
    def rng():
        st[0] = (st[0] + 0x6D2B79F5) & 0xFFFFFFFF; a = st[0]
        t = ((a ^ (a >> 15)) * (1 | a)) & 0xFFFFFFFF
        t = ((t + (((t ^ (t >> 7)) * (61 | t)) & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ t
        return ((t ^ (t >> 14)) & 0xFFFFFFFF)/4294967296
    sh = dict(typical=0, sOK=0, hOK=0)
    for _ in range(20):
        a = list(truth)
        for i in range(len(a)-1, 0, -1):
            j = int(rng()*(i+1)); a[i], a[j] = a[j], a[i]
        r = v("".join(a)); sh["typical"] += r["typical"]; sh["sOK"] += r["sOK"]; sh["hOK"] += r["hOK"]
    return dict(nWindows=len(W), cutoffs=b, truth=tv, degAccepted=len(acc), shuffles20=sh,
                G9="PASS" if not acc and tv["typical"] else "FAIL")
print(json.dumps(dict(lenCC=len(CC), primary=run(.7, 1, 99), sens_P5_P95=run(.7, 5, 95), sens_60_40=run(.6, 1, 99)), indent=1))
