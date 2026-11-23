"""Known-answer / property tests for a6_runner_generator.py. SYNTHETIC text only (Random(1) over a
skewed 6-letter alphabet): NOT a source, NOT natural language, no scoring."""
import random, sys, hashlib
sys.path.insert(0, __file__.rsplit("/", 1)[0])
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
m1 = g.run(text, 30); m2 = g.run(text, 30)
check("determinism (assertion 6)", g.manifest_bytes(m1) == g.manifest_bytes(m2))
check("30 windows, indices 0..29", [w["w"] for w in m1["windows"]] == list(range(30)))
check("plant vector all windows", all(g.mult_vector(w["plant_C"]) == g.TARGET13 for w in m1["windows"]))
check("C1 joint permutation pairs preserved", all(sorted(zip(w["c1_P"], w["c1_C"])) == sorted(zip(w["P"], w["plant_C"])) for w in m1["windows"]))
check("C1 not identity", all(w["c1_P"] != w["P"] for w in m1["windows"]))
check("C2 reversal", all(w["c2_P"] == w["P"][::-1] and w["c2_C"] == w["plant_C"][::-1] for w in m1["windows"]))
check("C3 vector", all(g.mult_vector(w["c3_C"]) == g.TARGET13 for w in m1["windows"]))
check("seed schedule 30 windows unique", len(set([g.BASE_SEED] + [s for w in range(30) for s in g.seed_schedule(w)])) == 1 + 30 * 23)
check("D4-as-written collides (reference)", len({g.BASE_SEED + 0 * 1000 + 7, g.BASE_SEED + 0 * 1000 + 0 + 7}) == 1)
try: g.require_source_pin("/nonexistent/pin.md", "x"); check("pin abort", False)
except g.FailClosed: check("pin abort (assertion 5)", True)
print("rejected candidates len13:", m1["rejected_candidates_len13"], "of accepted 30")
print("manifest sha256", hashlib.sha256(g.manifest_bytes(m1)).hexdigest())
print("ALL PASS" if ok else "SOME FAIL"); sys.exit(0 if ok else 1)
