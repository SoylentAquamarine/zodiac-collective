"""Spec-level reference for A6 D5/D6/D7 plus checks against hand values in
logs/2026-11-21-d5-d6-d7-fixtures.md. Toy windows only; not the planted-recovery runner."""
import itertools, random
from collections import Counter

def partitions(n, maxpart=None):
    maxpart = maxpart or n
    if n == 0: yield (); return
    for k in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - k, k): yield (k,) + rest

def feasible_splits(window, target):
    counts = Counter(window); order = []
    for ch in window:
        if ch not in order: order.append(ch)
    per = [sorted(partitions(counts[c])) for c in order]
    out = []
    for combo in itertools.product(*per):
        if sorted(s for p in combo for s in p) == sorted(target):
            out.append(combo)
    return sorted(out)

def assign(window, letter, split, rng):
    occ = [i for i, c in enumerate(window) if c == letter]
    rng.shuffle(occ); groups = []; pos = 0
    for size in sorted(split, reverse=True):
        groups.append(sorted(occ[pos:pos+size])); pos += size
    return groups

def c3(window_len, freqs, rng):
    letters = sorted(freqs); return ''.join(rng.choices(letters, weights=[freqs[l] for l in letters], k=window_len))

ok = True
def check(name, cond):
    global ok; ok &= bool(cond); print(("PASS " if cond else "FAIL ") + name)

s1 = feasible_splits("AABBC", [2,1,1,1])
check("F5-1 N==2", len(s1) == 2)
check("F5-1 order", s1 == [((1,1),(2,),(1,)), ((2,),(1,1),(1,))])
s2 = feasible_splits("AAAB", [2,1,1])
check("F5-2 N==1 and idx0", s2 == [((2,1),(1,))])
check("F5-3 N==0", feasible_splits("ABC", [2,1]) == [])
for seed in range(50):
    g = assign("AABBC", "A", (1,1), random.Random(seed))
    check(f"F6 seed{seed} partition" , sorted(x for gr in g for x in gr) == [0,1] and [len(x) for x in g] == [1,1]) if seed < 3 else None
    ok &= sorted(x for gr in g for x in gr) == [0,1]
gB = assign("AABBC", "B", (2,), random.Random(0)); check("F6 B single group", gB == [[2,3]])
check("F6 determinism", assign("AABBC","A",(1,1),random.Random(5)) == assign("AABBC","A",(1,1),random.Random(5)))
check("F7 forced BBBB all seeds", all(c3(4, {"A":0,"B":7,"C":0}, random.Random(s)) == "BBBB" for s in range(100)))
check("F7 len & alphabet", set(c3(30, {"A":1,"B":2,"C":3}, random.Random(1))) <= set("ABC") and len(c3(30,{"A":1,"B":2,"C":3},random.Random(1)))==30)
print("MACHINE-computed (not hand): F6 A-order seed20261113 ->", assign("AABBC","A",(1,1),random.Random(20261113)),
      "| C3 seed20261113 len8 ->", c3(8,{"A":1,"B":2,"C":3},random.Random(20261113)))
print("ALL PASS" if ok else "SOME FAIL")
