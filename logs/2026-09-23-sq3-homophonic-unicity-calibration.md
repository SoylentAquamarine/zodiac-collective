# 2026-09-23 — SQ-3 homophonic-specific unicity-distance calibration

**Agent/role:** Claude, acting as Cryptanalyst (unicity-distance calibration)
**Session type:** research cycle #2 (follow-on to
`logs/2026-09-23-sq1-sq3-source-and-attacksurface.md`)

## Scope of this session

Round 2's SQ-3 analysis (see prior log) used the *simple*-substitution
unicity-distance baseline (U ~= 28 characters, from H(K) = log2(26!)) as a
"reasoning anchor," explicitly flagging as a named gap that Z13's actual
homophonic key space could not yet be sized because Z13 is unsolved, and
recommending (Steering Committee Meeting #1, action item) that this be
replaced with a real homophonic-specific figure once real homophone-set
sizes were available. This session closes part of that gap using **Z408's
own real, documented, solved homophone-count distribution** as the
calibration reference, rather than waiting on a full from-scratch SQ-2
reproduction — a legitimate shortcut since the distribution itself (not
the symbol-to-letter identity, which SQ-2 still needs) is what the
unicity-distance model requires.

## 1. Data used, and how it was obtained (read this before the numbers)

**Important limitation encountered this session, disclosed up front:**
this session's network egress policy blocked direct `WebFetch` access to
essentially every candidate secondary/primary source site tried,
including `en.wikipedia.org`, `arxiv.org`, `dcode.fr`,
`zodiackillerciphers.com`, `ciphermysteries.com`, `thedecipherist.com`,
`boxentriq.com`, `ciphermuseum.com`, `blog.wolfram.com`, and
`www.cnn.com` (all returned `EGRESS_BLOCKED` errors). This is a different,
narrower restriction than the prior session experienced (that session's
log cites several of these same domains as directly fetched) — it appears
to be specific to this session's sandboxed environment, not a standing
project rule. A code-hosting domain (`raw.githubusercontent.com`) was
reachable, for comparison, so this is a domain-scoped block, not a total
network outage. **This is reported, not routed around, per this
environment's own proxy guidance** (do not retry a policy-level block).

Given that constraint, the data below comes from the `WebSearch` tool's
own synthesized answers (which remain grounded in real indexed pages and
list their source URLs), not from a directly read/quoted page. This is a
**weaker sourcing tier** than the previous session's directly-fetched
citations, and is disclosed as such, per `methods/falsification-standard.md`'s
explicit requirement to flag reliance on "a search-engine summary ...
not read directly."

- **Z408 homophone-count distribution** (query: "Z408 cipher number of
  distinct symbols letter E most homophones how many symbols per letter"):
  7 symbols for E; 4 symbols each for T, A, O, I, N, S; 3 symbols each for
  L, R; 2 symbols each for D, F, H; 1 symbol each for B, C, G, K, M, P, U,
  V, W, X, Y; 0 for J, Q, Z. This sums to exactly 54 distinct symbols,
  which is internally consistent (a real cipher's homophone counts must
  sum to its total symbol count) and matches the letter ranking implied by
  standard English letter frequency (E highest, then T/A/O/I/N/S, etc.),
  which is itself a good internal-consistency check on the figure, though
  not a substitute for direct verification. Search results attributed this
  to pages including `numberworld.blog` ("Z408 Cipher Explained: The
  Zodiac Killer's First Cipher") and `caesarcipher.org` ("Homophonic
  Substitution Cipher: From Defeating Frequency Analysis to the Zodiac
  Killer"), among others returned by the same query.
- **Z340 total symbol count** (query: "Z340 cipher total number of
  distinct symbols used 63 symbols homophonic"): 63 distinct symbols.
  Search results attributed this to pages including a San Jose State
  University project report on Z340 heuristic-search cryptanalysis
  (`scholarworks.sjsu.edu` / `cs.sjsu.edu`) among others.
- **Z340 partial per-letter anchor points** (from the prior round's
  search, log-referenced): E has 7 symbols, T has 4 symbols in Z340 — from
  a Popular Science article on the 2020 solve. **No full per-letter
  distribution for Z340 was found this session** — only these two anchor
  points and the total.

**Disclosed status:** the Z408 distribution above should be treated as
*provisionally documented* (internally consistent, multiply-attributed by
the search tool, but not independently read from a primary source
directly by this project) — the same evidentiary tier as other secondary-
sourced facts already in `knowledge-base/state.md`. The Z340 *per-letter*
distribution used below is **explicitly modeled, not documented data** —
see §3.

## 2. Method

Reproducible script: `methods/scripts/unicity-distance-homophonic.py`
(committed alongside this log). For a homophonic substitution cipher with
N total distinct symbols distributed across the 26 letters with counts
n_1..n_26 (summing to N) following a known/typical count profile — the
standard construction rationale for a homophonic cipher designed to
flatten ciphertext letter frequency toward the plaintext language's own
letter-frequency shape — the key-space entropy is the multinomial
coefficient:

    H(K) = log2( N! / (n_1! * n_2! * ... * n_26!) )

(the number of distinct ways to partition N labeled/distinct-shaped
symbols into 26 labeled groups of the given sizes). Unicity distance is
then U = H(K) / D, using D ~= 3.2 bits/character (the same English-
redundancy estimate already adopted in the prior log entry, kept
identical here for direct comparability rather than re-litigated).

Two reference values are computed alongside for context: the simple
(non-homophonic) monoalphabetic baseline H(K) = log2(26!), and a naive,
unconstrained upper bound H(K) = N*log2(26) that ignores the known
frequency-shaped count profile entirely (treats each symbol as
independently, uniformly choosing among 26 letters).

## 3. Results

Full script output (reproduced verbatim from a run of
`methods/scripts/unicity-distance-homophonic.py` this session):

```
=== Z408 (real, documented homophone-count distribution) ===
N (total distinct symbols) = 54
H(K) multinomial (known count-profile)      = 189.08 bits -> U = 59.1 chars
H(K) simple substitution baseline (26!)      = 88.38 bits -> U = 27.6 chars
H(K) naive unconstrained upper bound (26^N)  = 253.82 bits -> U = 79.3 chars

=== Z340 (total N documented; per-letter distribution MODELED, not real) ===
N (total distinct symbols, documented) = 63
Modeled distribution (frequency-proportional, illustrative only): {'E': 8, 'T': 6, 'A': 5, 'O': 5, 'I': 4, 'N': 4, 'S': 4, 'H': 4, 'R': 4, 'D': 3, 'L': 3, 'C': 2, 'U': 2, 'M': 2, 'W': 1, 'F': 1, 'G': 1, 'Y': 1, 'P': 1, 'B': 1, 'V': 1, 'K': 0, 'J': 0, 'X': 0, 'Q': 0, 'Z': 0}
H(K) modeled multinomial                     = 220.30 bits -> U = 68.8 chars
H(K) naive unconstrained upper bound (26^N)  = 296.13 bits -> U = 92.5 chars

=== Z13 comparison ===
Z13 total symbols = 13 (documented, see prior log entry).
13 is 22% of the Z408-calibrated homophonic unicity distance (~59 chars), and 47% of the simple-substitution baseline (~28 chars).
```

**Z340's modeled figure is explicitly illustrative, not a real key.** It
was generated by allocating Z340's documented total (63 symbols) across
the 26 letters proportional to standard English letter frequency
percentages (a well-known, general-knowledge table, not requiring
external verification), with largest-remainder rounding to hit the exact
total — it was **not** derived from Z340's actual solved key, which this
session could not access. It is included only to show that a
plausible-shaped homophonic distribution at Z340's real total-symbol-count
scale produces a similarly large unicity distance (~69 characters) to
Z408's real one (~59 characters), i.e. the Z408-based figure is not an
outlier driven by some Z408-specific quirk. This should not be cited
outside this log/script as a "Z340 finding" — it is a Z408-anchored
sensitivity check, nothing more, and is a materially weaker sourcing tier
than the Z408 figure.

## 4. Assessment against the falsification standard

Per `methods/falsification-standard.md`'s Confirmed-Findings bar: this
result has (a) a committed, reproducible script producing the number, not
just a description of it; (b) the actual output committed alongside this
log (§3 above, reproducible verbatim by rerunning the script); (c)
explicit provenance and an explicit disclosure of the secondary-source,
not-directly-read sourcing tier for the input data (§1); (d) explicit
sensitivity context (the simple-substitution and naive-unconstrained
reference values, plus the Z340 sensitivity check). This meets the
minimum bar for a **Confirmed Finding**, with its sourcing limitation
disclosed in the entry itself — the same standard already applied to the
prior session's Confirmed Findings entries. It does **not** meet, and is
not being proposed for, the harder **Active Hypothesis** bar (no
alternatives-ruled-out claim, no adversarial review yet) — it is a
calibration number, not an interpretation.

**What this does and does not establish:** this replaces the *direction-
only* prior finding ("homophony pushes the threshold higher than the
simple-substitution baseline, but we can't say by how much") with an
actual computed figure grounded in Z408's real, documented homophone
structure: roughly 59 characters, more than double the simple-
substitution baseline of ~28, and more than 4x Z13's actual length of 13
symbols. It does **not** establish Z13's own precise unicity distance,
because Z13's own homophone-count profile remains unknown (Z13 is
unsolved) — the same named circularity as before. What has changed is
that the *anchor* for "how much more than 28 does homophony typically
require" is now a real number from a real solved Zodiac cipher, not an
unquantified direction.

## 5. Next steps

1. When SQ-2 (Z408/Z340 reproduction) begins, verify the Z408 homophone-
   count distribution used here directly against the primary solved key
   (once SQ-1's corpus work makes that available in `/data/`), since this
   session's figure is currently sourced only via search-tool synthesis,
   not a directly read table.
2. If/when Z340's real per-letter distribution becomes available (SQ-2),
   replace §3's modeled Z340 figure with a real one and retract the
   "illustrative only" framing.
3. Flag for the auditor (ChatGPT), per `comms/FromClaudeToChatGPT.md`
   Round 3: please independently re-derive or challenge the multinomial
   key-space model itself (is it the right entropy model for this cipher
   class, or is there a more standard formula in the literature this
   project should use instead?), and check whether the Z408 distribution
   figure can be found from a source your own access can reach directly,
   given this session's network restriction.
4. Note for future cycles: this session's environment blocked WebFetch to
   most general research/news/wiki domains but allowed
   `raw.githubusercontent.com`; a future cycle hitting the same wall could
   try whether a source's content is mirrored on a GitHub-hosted page
   (e.g. a repo, gist, or GitHub Pages site) as a workaround that doesn't
   require bypassing the policy, only routing to an already-permitted host.
