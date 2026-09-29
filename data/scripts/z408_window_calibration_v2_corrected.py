import random, math, statistics, re, hashlib

REF_TEXT_PATH = 'data/external-sources/gutenberg-1342-2026-09-29/pride_prejudice.txt'
CIPHER_PATH = 'data/external-sources/azdecrypt-doranchak-2026-09-27/z408-cipher.txt'
PLAIN_PATH = 'data/external-sources/azdecrypt-doranchak-2026-09-27/z408-solved.txt'

# --- Step 1: derive real unigram + bigram frequencies from a fetched public-domain text ---
with open(REF_TEXT_PATH, encoding='utf-8') as f:
    raw = f.read()
with open(REF_TEXT_PATH, 'rb') as f:
    ref_hash = hashlib.sha256(f.read()).hexdigest()

letters_only = re.sub(r'[^A-Za-z]', '', raw).upper()
print("Reference text SHA256:", ref_hash)
print("Reference text total letters used for frequency derivation:", len(letters_only))

uni_counts = {}
for ch in letters_only:
    uni_counts[ch] = uni_counts.get(ch, 0) + 1
uni_total = sum(uni_counts.values())
UNI_LOGP = {ch: math.log(c / uni_total) for ch, c in uni_counts.items()}
# smoothing for any letter unseen (shouldn't happen with this much text, but be safe)
for ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    if ch not in UNI_LOGP:
        UNI_LOGP[ch] = math.log(0.5 / uni_total)

bi_counts = {}
for i in range(len(letters_only) - 1):
    bg = letters_only[i:i+2]
    bi_counts[bg] = bi_counts.get(bg, 0) + 1
bi_total = sum(bi_counts.values())
# add-1 smoothing over all 676 possible bigrams so unseen bigrams aren't -inf
BI_LOGP = {}
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
smoothed_total = bi_total + 676
for a in alphabet:
    for b in alphabet:
        bg = a + b
        BI_LOGP[bg] = math.log((bi_counts.get(bg, 0) + 1) / smoothed_total)

print("Distinct unigrams seen:", len(uni_counts), "/ 26")
print("Distinct bigrams seen:", len(bi_counts), "/ 676")
print("Self-check: unigram probs sum to", round(sum(math.exp(v) for v in UNI_LOGP.values()), 4))

def uni_score(letters):
    return sum(UNI_LOGP[ch] for ch in letters)

def bi_score(letters):
    s = ''.join(letters)
    return sum(BI_LOGP[s[i:i+2]] for i in range(len(s)-1))

# --- Step 2: load and self-check Z408 cipher/plaintext (same as v1) ---
with open(CIPHER_PATH) as f:
    cipher = f.read().replace('\n','').replace(' ','')
with open(PLAIN_PATH) as f:
    plain = f.read().replace('\n','').replace(' ','')
assert len(cipher) == len(plain) == 408

true_map = {}
for c, p in zip(cipher, plain):
    if c in true_map:
        assert true_map[c] == p
    else:
        true_map[c] = p
decoded_full = ''.join(true_map[c] for c in cipher)
assert decoded_full == plain
print("Self-check: Z408 true mapping consistent and reproduces full plaintext. OK.")

# --- Step 3: corrected calibration -- unrestricted (collision-permitting) null, both scorers ---
random.seed(20260929)
window_starts = [10, 80, 150, 220, 290, 360]
N = 5000

print()
print("=== CORRECTED CALIBRATION (unrestricted null, real empirical freq tables) ===")
results = []
for start in window_starts:
    end = start + 13
    c_window = cipher[start:end]
    p_window = plain[start:end]
    distinct_syms = sorted(set(c_window))
    n_classes = len(distinct_syms)

    true_decoded = [true_map[c] for c in c_window]
    assert ''.join(true_decoded) == p_window
    true_uni = uni_score(true_decoded)
    true_bi = bi_score(true_decoded)

    alt_uni, alt_bi = [], []
    for _ in range(N):
        # UNRESTRICTED: each symbol independently random, collisions allowed
        rand_map = {s: random.choice(alphabet) for s in distinct_syms}
        decoded = [rand_map[c] for c in c_window]
        alt_uni.append(uni_score(decoded))
        alt_bi.append(bi_score(decoded))

    def rank_and_pct(true_val, alts):
        all_vals = sorted(alts + [true_val], reverse=True)
        rank = all_vals.index(true_val) + 1
        pct = 100 * (1 - (rank - 1) / len(all_vals))
        return rank, len(all_vals), round(pct, 2)

    uni_rank, uni_n, uni_pct = rank_and_pct(true_uni, alt_uni)
    bi_rank, bi_n, bi_pct = rank_and_pct(true_bi, alt_bi)

    results.append({
        'start': start, 'window_plain': p_window, 'n_classes': n_classes,
        'uni_true': round(true_uni,3), 'uni_alt_mean': round(statistics.mean(alt_uni),3),
        'uni_rank': f"{uni_rank}/{uni_n}", 'uni_pct': uni_pct,
        'bi_true': round(true_bi,3), 'bi_alt_mean': round(statistics.mean(alt_bi),3),
        'bi_rank': f"{bi_rank}/{bi_n}", 'bi_pct': bi_pct,
    })

for r in results:
    print(r)
