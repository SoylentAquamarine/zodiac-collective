import re, math, random, json, sys, collections
raw = open(sys.argv[1], encoding='utf-8').read()
s = raw.index("To Sherlock Holmes she is always THE woman.")
e = raw.index("End of the Project Gutenberg EBook", s)
body = raw[s:e]
lines = [l for l in re.split(r'\r?\n', body)
         if not re.match(r'^\s*ADVENTURE [IVXLC]+\. .*$', l) and not re.match(r'^\s*[IVXLC]+\.\s*$', l)]
CC = re.sub(r'[^A-Z]', '', "\n".join(lines).upper())
truth = re.sub(r'[^A-Z]', '', open('data/external-sources/azdecrypt-doranchak-2026-09-27/z408-solved.txt').read().upper())
assert len(truth) == 408
def model(tr):
    cnt = collections.Counter(); ctx = collections.Counter()
    for i in range(len(tr)-3):
        ctx[tr[i:i+3]] += 1; cnt[tr[i:i+4]] += 1
    def score(x):
        return sum(math.log((cnt[x[i:i+4]]+0.5)/(ctx[x[i:i+3]]+13)) for i in range(len(x)-3))/(len(x)-3)
    return score
def ent(x):
    c = collections.Counter(x); n = len(x)
    return -sum(v/n*math.log2(v/n) for v in c.values())
def pct(a, p):
    b = sorted(a); return b[min(len(b)-1, max(0, round(p/100*(len(b)-1))))]
A = [chr(65+i) for i in range(26)]
ctrl = [(x, x*408) for x in A] + [(x+y, (x+y)*204) for x in A for y in A if x != y]
def run(frac, lo, hi):
    cut = int(len(CC)*frac); sc = model(CC[:cut]); K = CC[cut:]
    W = [K[i:i+408] for i in range(0, len(K)-407, 408)]
    ws = [sc(w) for w in W]; wh = [ent(w) for w in W]
    b = dict(sLo=pct(ws,lo), sHi=pct(ws,hi), hLo=pct(wh,lo), hHi=pct(wh,hi))
    def ok(x):
        s_, h_ = sc(x), ent(x)
        return s_, h_, b['sLo']<=s_<=b['sHi'], b['hLo']<=h_<=b['hHi']
    t = ok(truth); acc = [i for i,x in ctrl if (lambda r: r[2] and r[3])(ok(x))]
    eo = sum(1 for i,x in ctrl if (lambda r: r[2] and not r[3])(ok(x)))  # score ok, entropy bad
    so = sum(1 for i,x in ctrl if (lambda r: r[3] and not r[2])(ok(x)))
    rng = random.Random(1)
    sh = 0
    for _ in range(20):
        a = list(truth); rng.shuffle(a); r = ok(''.join(a)); sh += r[2] and r[3]
    return dict(n=len(W), cutoffs=b, truth=t, accepted=acc, entOnlyReject=eo, scoreOnlyReject=so,
                bothReject=len(ctrl)-len(acc)-eo-so, verdict="PASS" if not acc and t[2] and t[3] else "FAIL", shuf_typical=sh)
out = dict(lenCC=len(CC), primary=run(.7,1,99), p5p95=run(.7,5,95), s6040=run(.6,1,99))
print(json.dumps(out, indent=1))
