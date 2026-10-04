import random, math, re, statistics

REF_TEXT_PATH = 'data/external-sources/gutenberg-1342-2026-09-29/pride_prejudice.txt'

with open(REF_TEXT_PATH, encoding='utf-8') as f:
    raw = f.read()
letters_only = re.sub(r'[^A-Za-z]', '', raw).upper()
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# unigram
uni_counts = {}
for ch in letters_only:
    uni_counts[ch] = uni_counts.get(ch, 0) + 1
uni_total = sum(uni_counts.values())
UNI_LOGP = {ch: math.log(c / uni_total) for ch, c in uni_counts.items()}
UNI_P = {ch: uni_counts.get(ch, 0) / uni_total for ch in alphabet}

# bigram (for scoring, add-1 smoothed) and bigram transition probs (for generation, add-1 smoothed)
bi_counts = {}
for i in range(len(letters_only) - 1):
    bg = letters_only[i:i+2]
    bi_counts[bg] = bi_counts.get(bg, 0) + 1
bi_total = sum(bi_counts.values())
smoothed_total = bi_total + 676
BI_LOGP = {}
for a in alphabet:
    for b in alphabet:
        bg = a + b
        BI_LOGP[bg] = math.log((bi_counts.get(bg, 0) + 1) / smoothed_total)

# transition probability P(next | current), add-1 smoothed, for generation
TRANS_P = {}
for a in alphabet:
    row_total = sum(bi_counts.get(a + b, 0) for b in alphabet) + 26
    TRANS_P[a] = {b: (bi_counts.get(a + b, 0) + 1) / row_total for b in alphabet}

print("Self-check: unigram sums to", round(sum(UNI_P.values()), 4))
for a in alphabet[:3]:
    print(f"Self-check: transition row for {a} sums to", round(sum(TRANS_P[a].values()), 4))

def uni_score(s):
    return sum(UNI_LOGP[ch] for ch in s)

def bi_score(s):
    return sum(BI_LOGP[s[i:i+2]] for i in range(len(s) - 1))

# Z13's exact partition, in position order 1..13 (1-indexed), with each entry's "class id"
PARTITION_BY_POS = {
    1: 'A', 12: 'A',
    3: 'B', 11: 'B',
    5: 'C', 7: 'C', 9: 'C',
    8: 'D', 13: 'D',
    2: 'E', 4: 'F', 6: 'G', 10: 'H',
}
assert set(PARTITION_BY_POS.keys()) == set(range(1, 14))

def weighted_choice(dist, rng):
    letters = list(dist.keys())
    weights = list(dist.values())
    return rng.choices(letters, weights=weights, k=1)[0]

def generate_true_sequence(rng):
    class_letter = {}
    seq = [None] * 14  # 1-indexed
    prev_letter = None
    for pos in range(1, 14):
        cls = PARTITION_BY_POS[pos]
        if cls in class_letter:
            letter = class_letter[cls]  # forced repeat
        else:
            if prev_letter is None:
                letter = weighted_choice(UNI_P, rng)
            else:
                letter = weighted_choice(TRANS_P[prev_letter], rng)
            class_letter[cls] = letter
        seq[pos] = letter
        prev_letter = letter
    return ''.join(seq[1:14])

def generate_alt_sequence(rng):
    class_letter = {}
    seq = [None] * 14
    for pos in range(1, 14):
        cls = PARTITION_BY_POS[pos]
        if cls not in class_letter:
            class_letter[cls] = rng.choice(alphabet)
        seq[pos] = class_letter[cls]
    return ''.join(seq[1:14])

SEED = 20261004
rng = random.Random(SEED)
N_TRIALS = 20
N_ALTS = 2000

results = []
for trial in range(N_TRIALS):
    true_seq = generate_true_sequence(rng)
    assert len(true_seq) == 13
    # verify partition compliance
    for pos in range(1, 14):
        cls = PARTITION_BY_POS[pos]
        for pos2 in range(1, 14):
            if PARTITION_BY_POS[pos2] == cls:
                assert true_seq[pos-1] == true_seq[pos2-1]

    true_uni = uni_score(true_seq)
    true_bi = bi_score(true_seq)

    alt_uni_scores, alt_bi_scores = [], []
    for _ in range(N_ALTS):
        alt = generate_alt_sequence(rng)
        alt_uni_scores.append(uni_score(alt))
        alt_bi_scores.append(bi_score(alt))

    def rank_pct(val, alts):
        all_vals = sorted(alts + [val], reverse=True)
        rank = all_vals.index(val) + 1
        pct = 100 * (1 - (rank - 1) / len(all_vals))
        return rank, len(all_vals), round(pct, 2)

    ur, un, up = rank_pct(true_uni, alt_uni_scores)
    br, bn, bp = rank_pct(true_bi, alt_bi_scores)
    results.append({'trial': trial, 'seq': true_seq, 'uni_rank': f"{ur}/{un}", 'uni_pct': up, 'bi_rank': f"{br}/{bn}", 'bi_pct': bp})

print()
for r in results:
    print(r)

uni_pcts = [r['uni_pct'] for r in results]
bi_pcts = [r['bi_pct'] for r in results]
print()
print("Unigram percentile: mean =", round(statistics.mean(uni_pcts),2), "median =", round(statistics.median(uni_pcts),2), "min =", min(uni_pcts), "max =", max(uni_pcts))
print("Bigram percentile:  mean =", round(statistics.mean(bi_pcts),2), "median =", round(statistics.median(bi_pcts),2), "min =", min(bi_pcts), "max =", max(bi_pcts))
