#!/usr/bin/env python3
"""
Homophonic-substitution unicity-distance calibration, using Z408's
documented (real, solved) homophone-count distribution and Z340's
partially-documented total symbol count, as reference points for Z13's
attack-surface question (config/sidequests.md SQ-3).

Method (multinomial key-space model): for a homophonic substitution
cipher that assigns N total distinct cipher symbols across the 26
plaintext letters using a known/typical count profile n_1..n_26 (summing
to N) approximating English letter-frequency shape -- the standard
construction rationale for a homophonic cipher designed to flatten
ciphertext letter frequency, and the standard treatment for this cipher
class in the cryptology literature on unicity distance -- the key-space
entropy is:

    H(K) = log2( N! / (n_1! * n_2! * ... * n_26!) )

i.e. the number of distinct ways to partition N labeled (distinct-shaped)
symbols into 26 labeled groups of the given prescribed sizes. Unicity
distance is then U = H(K) / D, with D = English plaintext redundancy in
bits/character (D ~= 3.2 bits/char, the same estimate already adopted in
logs/2026-09-23-sq1-sq3-source-and-attacksurface.md for direct
comparability).

This is run alongside two other reference values for context:
- the simple (non-homophonic) monoalphabetic baseline, H(K) = log2(26!);
- a naive, unconstrained upper bound treating each of the N symbols as
  independently choosing among 26 letters with no shape constraint,
  H(K) = N * log2(26) = log2(26^N).

Data provenance and disclosed limitations: see the companion log entry
logs/2026-09-23-sq3-homophonic-unicity-calibration.md for full sourcing,
including that direct WebFetch access to the secondary-source pages that
report Z408's per-letter homophone-count distribution and Z340's total
symbol count was blocked by this session's network egress policy; the
figures below were obtained via the WebSearch tool's own synthesized
answer (which cites specific pages) rather than a directly read/quoted
primary or secondary document. Z408's distribution is treated as
real/documented (subject to that disclosed sourcing caveat). Z340's
per-letter distribution is NOT documented from this session's research
(only the total symbol count, 63, and two anchor points -- E has 7
symbols, T has 4 -- were found) -- the Z340 multinomial figure below uses
a MODELED, frequency-proportional distribution as an illustrative stand-in
and must not be treated as Z340's real key.
"""

import math


def log2fact(n: int) -> float:
    """log2(n!) via the log-gamma function (exact for our purposes)."""
    return math.lgamma(n + 1) / math.log(2)


def multinomial_entropy_bits(counts: dict) -> float:
    n_total = sum(counts.values())
    return log2fact(n_total) - sum(log2fact(n) for n in counts.values())


# --- Z408: documented homophone-count distribution (see log for sourcing) ---
Z408_DISTRIBUTION = {
    "E": 7,
    "T": 4, "A": 4, "O": 4, "I": 4, "N": 4, "S": 4,
    "L": 3, "R": 3,
    "D": 2, "F": 2, "H": 2,
    "B": 1, "C": 1, "G": 1, "K": 1, "M": 1, "P": 1,
    "U": 1, "V": 1, "W": 1, "X": 1, "Y": 1,
    "J": 0, "Q": 0, "Z": 0,
}

# --- Z340: only the total (63) and two anchor points (E:7, T:4) are
# documented from this session's research; the rest is a MODELED
# frequency-proportional allocation, clearly not real key data. ---
Z340_TOTAL_SYMBOLS = 63
ENGLISH_LETTER_FREQ_PCT = {
    "E": 12.70, "T": 9.06, "A": 8.17, "O": 7.51, "I": 6.97, "N": 6.75,
    "S": 6.33, "H": 6.09, "R": 5.99, "D": 4.25, "L": 4.03, "C": 2.78,
    "U": 2.76, "M": 2.41, "W": 2.36, "F": 2.23, "G": 2.02, "Y": 1.97,
    "P": 1.93, "B": 1.49, "V": 0.98, "K": 0.77, "J": 0.15, "X": 0.15,
    "Q": 0.10, "Z": 0.07,
}

D_BITS_PER_CHAR = 3.2  # English redundancy estimate, per prior log entry


def modeled_frequency_proportional_distribution(n_total: int) -> dict:
    """Illustrative only -- NOT documented Z340 key data. Allocates N
    symbols across letters proportional to standard English letter
    frequency, largest-remainder rounding to hit the exact total."""
    total_freq = sum(ENGLISH_LETTER_FREQ_PCT.values())
    raw = {k: n_total * v / total_freq for k, v in ENGLISH_LETTER_FREQ_PCT.items()}
    floor_alloc = {k: math.floor(v) for k, v in raw.items()}
    remaining = n_total - sum(floor_alloc.values())
    by_remainder = sorted(
        ENGLISH_LETTER_FREQ_PCT.keys(),
        key=lambda k: (raw[k] - math.floor(raw[k])),
        reverse=True,
    )
    i = 0
    while remaining > 0:
        floor_alloc[by_remainder[i % len(by_remainder)]] += 1
        remaining -= 1
        i += 1
    return floor_alloc


def main():
    n408 = sum(Z408_DISTRIBUTION.values())
    assert n408 == 54, f"Z408 distribution should sum to 54, got {n408}"

    h_408_multinomial = multinomial_entropy_bits(Z408_DISTRIBUTION)
    h_simple = log2fact(26)
    h_408_naive = n408 * math.log2(26)

    print("=== Z408 (real, documented homophone-count distribution) ===")
    print(f"N (total distinct symbols) = {n408}")
    print(f"H(K) multinomial (known count-profile)      = {h_408_multinomial:.2f} bits "
          f"-> U = {h_408_multinomial / D_BITS_PER_CHAR:.1f} chars")
    print(f"H(K) simple substitution baseline (26!)      = {h_simple:.2f} bits "
          f"-> U = {h_simple / D_BITS_PER_CHAR:.1f} chars")
    print(f"H(K) naive unconstrained upper bound (26^N)  = {h_408_naive:.2f} bits "
          f"-> U = {h_408_naive / D_BITS_PER_CHAR:.1f} chars")

    print()
    print("=== Z340 (total N documented; per-letter distribution MODELED, not real) ===")
    z340_modeled = modeled_frequency_proportional_distribution(Z340_TOTAL_SYMBOLS)
    h_340_modeled = multinomial_entropy_bits(z340_modeled)
    h_340_naive = Z340_TOTAL_SYMBOLS * math.log2(26)
    print(f"N (total distinct symbols, documented) = {Z340_TOTAL_SYMBOLS}")
    print(f"Modeled distribution (frequency-proportional, illustrative only): {z340_modeled}")
    print(f"H(K) modeled multinomial                     = {h_340_modeled:.2f} bits "
          f"-> U = {h_340_modeled / D_BITS_PER_CHAR:.1f} chars")
    print(f"H(K) naive unconstrained upper bound (26^N)  = {h_340_naive:.2f} bits "
          f"-> U = {h_340_naive / D_BITS_PER_CHAR:.1f} chars")

    print()
    print("=== Z13 comparison ===")
    print("Z13 total symbols = 13 (documented, see prior log entry).")
    print(f"13 is {13 / (h_408_multinomial / D_BITS_PER_CHAR) * 100:.0f}% of the Z408-calibrated "
          f"homophonic unicity distance (~{h_408_multinomial / D_BITS_PER_CHAR:.0f} chars), "
          f"and {13 / (h_simple / D_BITS_PER_CHAR) * 100:.0f}% of the simple-substitution "
          f"baseline (~{h_simple / D_BITS_PER_CHAR:.0f} chars).")


if __name__ == "__main__":
    main()
