"""Known-answer / property tests for a6_runner_generator.py. SYNTHETIC text only (Random(1) over a
skewed 6-letter alphabet): NOT a source, NOT natural language, no scoring."""
import random, sys, hashlib, tempfile
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from pathlib import Path
import a6_runner_generator as g
ok = True
def check(n, c):
    global ok; ok &= bool(c); print(("PASS " if c else "FAIL ") + n)
# D5 hand values (from the committed fixtures)
check("D5 AABBC order", g.feasible_splits("AABBC", [2,1,1,1]) == [((1,1),(2,),(1,)), ((2,),(1,1),(1,))])
check("D5 AAAB", g.feasible_splits("AAAB", [2,1,1]) == [((2,1),(1,))])
check("D5 ABC N=0", g.feasible_splits("ABC", [2,1]) == [])
# D10/D11 hand case
P = "ABCDE"; C = [10, 11, 12, 13, 14]
check("D11 reverse", P[::-1] == "EDCBA" and C[::-1] == [14,13,12,11,10])
# synthetic text
r = random.Random(1); text = "".join(r.choices("ABCDEF", weights=[8,5,4,3,2,1], k=20000))
m1 = g.generate_manifest(text, 30); m2 = g.generate_manifest(text, 30)
check("determinism (assertion 6)", g.manifest_bytes(m1) == g.manifest_bytes(m2))
check("30 windows, indices 0..29", [w["w"] for w in m1["windows"]] == list(range(30)))
check("plant vector all windows", all(g.mult_vector(w["plant_C"]) == g.TARGET13 for w in m1["windows"]))
check("C1 joint permutation pairs preserved", all(sorted(zip(w["c1_P"], w["c1_C"])) == sorted(zip(w["P"], w["plant_C"])) for w in m1["windows"]))
check("C1 not identity", all(w["c1_P"] != w["P"] for w in m1["windows"]))
check("C2 reversal", all(w["c2_P"] == w["P"][::-1] and w["c2_C"] == w["plant_C"][::-1] for w in m1["windows"]))
check("C3 vector", all(g.mult_vector(w["c3_C"]) == g.TARGET13 for w in m1["windows"]))
check("seed schedule 30 windows unique", len(set([g.BASE_SEED] + [s for w in range(30) for s in g.seed_schedule(w)])) == 1 + 30 * 23)
d4 = [g.BASE_SEED]
for w in range(1000):
    base = g.BASE_SEED + w * 1000
    d4.extend([base + 7, base + 11])
    d4.extend(base + r for r in range(g.RESTARTS))
check("D4 reference has exactly 2,001 duplicate seed instances", len(d4) - len(set(d4)) == 2001)
d9 = [g.BASE_SEED] + [s for w in range(1000) for s in g.seed_schedule(w)]
check("D9 schedule has zero collisions over 1,000 windows", len(d9) == len(set(d9)))
try: g.run(text, 1); check("production run requires pin", False)
except g.FailClosed: check("production run requires pin", True)
with tempfile.TemporaryDirectory() as td:
    pin = Path(td) / "source-pin.md"
    pin.write_text("normalized_text_sha256: " + ("0" * 64) + "\n", encoding="utf-8")
    try: g.run(text, 1, str(pin)); check("production run rejects hash mismatch", False)
    except g.FailClosed: check("production run rejects hash mismatch", True)
    digest = hashlib.sha256(text.encode("ascii")).hexdigest()
    pin.write_text("normalized_text_sha256: " + digest + "\n", encoding="utf-8")
    valid = g.run(text, 1, str(pin))
    check("matching pin permits generator-only production entry", valid["n_windows"] == 1)
print("rejected candidates len13:", m1["rejected_candidates_len13"], "of accepted 30")
print("manifest sha256", hashlib.sha256(g.manifest_bytes(m1)).hexdigest())
print("ALL PASS" if ok else "SOME FAIL"); sys.exit(0 if ok else 1)
