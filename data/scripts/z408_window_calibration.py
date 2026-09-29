import random, math, statistics

CIPHER_PATH = 'data/external-sources/azdecrypt-doranchak-2026-09-27/z408-cipher.txt'
PLAIN_PATH = 'data/external-sources/azdecrypt-doranchak-2026-09-27/z408-solved.txt'

with open(CIPHER_PATH) as f:
    cipher = f.read().replace('\n','').replace(' ','')
with open(PLAIN_PATH) as f:
    plain = f.read().replace('\n','').replace(' ','')

assert len(cipher) == len(plain) == 408

# Build the TRUE cipher-symbol -> plaintext-letter mapping, and verify it's consistent
# (every occurrence of a cipher symbol maps to the same plaintext letter)
true_map = {}
for c, p in zip(cipher, plain):
    if c in true_map:
        assert true_map[c] == p, f"Inconsistent mapping for symbol {c!r}: {true_map[c]} vs {p}"
    else:
        true_map[c] = p

print("Self-check: true mapping is internally consistent across all 408 positions. OK.")
print("Distinct cipher symbols overall:", len(true_map))

# Self-check: decoding the full ciphertext with true_map reproduces the plaintext exactly
decoded_full = ''.join(true_map[c] for c in cipher)
assert decoded_full == plain
print("Self-check: full-text decode via true_map exactly reproduces known plaintext. OK.")

# Standard published English letter frequencies (percent), fixed before any run
FREQ = {
    'E':12.70,'T':9.10,'A':8.20,'O':7.50,'I':7.00,'N':6.70,'S':6.30,'H':6.10,
    'R':6.00,'D':4.30,'L':4.00,'C':2.80,'U':2.80,'M':2.40,'W':2.40,'F':2.20,
    'G':2.00,'Y':2.00,'P':1.90,'B':1.50,'V':1.00,'K':0.80,'J':0.15,'X':0.15,
    'Q':0.10,'Z':0.07,
}
total = sum(FREQ.values())
LOGP = {k: math.log(v/total) for k, v in FREQ.items()}
print("Self-check: frequency table sums to", round(total,2), "(should be ~100)")

def score(decoded_letters):
    return sum(LOGP[ch] for ch in decoded_letters)

# Pick 6 non-overlapping 13-character windows spread across the 408-character cipher
random.seed(20260929)  # fixed seed, declared before any result is seen
window_starts = [10, 80, 150, 220, 290, 360]  # spread roughly evenly, fixed in advance

results = []
for start in window_starts:
    end = start + 13
    if end > 408:
        continue
    c_window = cipher[start:end]
    p_window = plain[start:end]
    distinct_syms = sorted(set(c_window))
    n_classes = len(distinct_syms)

    true_decoded = [true_map[c] for c in c_window]
    assert ''.join(true_decoded) == p_window
    true_score = score(true_decoded)

    # Generate N random alternative mappings: each distinct symbol -> a distinct random letter (no repeats),
    # i.e. simple substitution over the n_classes symbols actually present, matching the "no-homophony" case
    N = 2000
    alt_scores = []
    for _ in range(N):
        letters = random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ', n_classes)
        rand_map = dict(zip(distinct_syms, letters))
        decoded = [rand_map[c] for c in c_window]
        alt_scores.append(score(decoded))

    all_scores = alt_scores + [true_score]
    all_scores_sorted = sorted(all_scores, reverse=True)
    rank = all_scores_sorted.index(true_score) + 1  # 1 = best
    percentile = 100 * (1 - (rank - 1) / len(all_scores))

    results.append({
        'start': start, 'window_plain': p_window, 'n_classes': n_classes,
        'true_score': round(true_score, 3),
        'alt_mean': round(statistics.mean(alt_scores), 3),
        'alt_stdev': round(statistics.stdev(alt_scores), 3),
        'rank_out_of': len(all_scores), 'rank': rank, 'percentile': round(percentile, 2),
    })

print()
for r in results:
    print(r)
