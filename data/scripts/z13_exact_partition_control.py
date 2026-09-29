import random, math, re, statistics

REF_TEXT_PATH = 'data/external-sources/gutenberg-1342-2026-09-29/pride_prejudice.txt'

with open(REF_TEXT_PATH, encoding='utf-8') as f:
    raw = f.read()
letters_only = re.sub(r'[^A-Za-z]', '', raw).upper()
uni_counts = {}
for ch in letters_only:
    uni_counts[ch] = uni_counts.get(ch, 0) + 1
uni_total = sum(uni_counts.values())
UNI_LOGP = {ch: math.log(c / uni_total) for ch, c in uni_counts.items()}
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letters_weighted = list(alphabet)
weights = [uni_counts.get(ch, 0) for ch in alphabet]

print("Self-check: unigram probs sum to", round(sum(math.exp(v) for v in UNI_LOGP.values()), 4))
assert abs(sum(math.exp(v) for v in UNI_LOGP.values()) - 1.0) < 1e-9

# Z13's exact equality partition (1-indexed positions, per this project's own documented pattern)
PARTITION = [
    {1, 12}, {3, 11}, {5, 7, 9}, {8, 13},  # multi-position classes
    {2}, {4}, {6}, {10},                    # singleton classes
]
all_positions = set()
for cls in PARTITION:
    all_positions |= cls
assert all_positions == set(range(1, 14)), "partition must cover all 13 positions exactly once"
assert sum(len(c) for c in PARTITION) == 13
print("Self-check: partition covers all 13 positions exactly once. OK. Classes:", len(PARTITION))

def expand_to_string(class_letters):
    # class_letters: dict {frozenset(class): letter} -> build 13-char string
    s = [None] * 14  # 1-indexed, index 0 unused
    for cls, letter in class_letters.items():
        for pos in cls:
            s[pos] = letter
    return ''.join(s[1:14])

def uni_score(s):
    return sum(UNI_LOGP[ch] for ch in s)

random.seed(20260929)
N = 2000

true_scores = []
for _ in range(N):
    class_letters = {frozenset(cls): random.choices(letters_weighted, weights=weights, k=1)[0] for cls in PARTITION}
    s = expand_to_string(class_letters)
    assert len(s) == 13
    true_scores.append(uni_score(s))

wrong_scores = []
for _ in range(N):
    class_letters = {frozenset(cls): random.choice(alphabet) for cls in PARTITION}
    s = expand_to_string(class_letters)
    assert len(s) == 13
    wrong_scores.append(uni_score(s))

print()
print("=== Exact-partition generative control ===")
print("Frequency-drawn ('true-like') scores: mean =", round(statistics.mean(true_scores),3), "stdev =", round(statistics.stdev(true_scores),3))
print("Uniform-drawn ('wrong') scores:        mean =", round(statistics.mean(wrong_scores),3), "stdev =", round(statistics.stdev(wrong_scores),3))

# What fraction of "wrong" draws score >= the median "true-like" draw?
true_scores_sorted = sorted(true_scores)
median_true = true_scores_sorted[len(true_scores_sorted)//2]
frac_wrong_beat_median_true = sum(1 for w in wrong_scores if w >= median_true) / len(wrong_scores)
print("Median true-like score:", round(median_true,3))
print("Fraction of wrong-draws scoring >= median true-like score:", round(frac_wrong_beat_median_true,4))

# Overlap check: what fraction of the two distributions overlap (simple range check)
print("True-like score range:", round(min(true_scores),3), "to", round(max(true_scores),3))
print("Wrong score range:", round(min(wrong_scores),3), "to", round(max(wrong_scores),3))
