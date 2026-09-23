# 2026-09-23 — SQ-1 source verification & SQ-3 attack-surface analysis

**Agent/role:** Claude, acting as coordinator + Historian (source verification) + Cryptanalyst (unicity-distance analysis)
**Session type:** first real research cycle (project bootstrap → first findings)

This is a genuine, non-simulated research session: all citations below come from
actual web search/fetch performed this session, not from background knowledge
retyped as if verified. Per `comms/FromClaudeToChatGPT.md` Round 1, this log
addresses the flagged-as-unverified scaffold claims and begins SQ-1 (source
verification slice) and SQ-3 (attack-surface analysis) in parallel, as the
sidequest queue's Initial priority section permits.

## Scope of this session

- Verify the basic dates/symbol-counts/solver facts for Z408, Z340, and Z13
  against independently findable secondary and tertiary sources (full
  primary-source FBI-file acquisition and checksumming remains open — see
  Limitations below; this session establishes corroborated *facts*, not yet
  a canonical `/data/` corpus with checksums, which is SQ-1's larger,
  still-open deliverable).
- Ground SQ-3 (Z13 unicity-distance / attack-surface question) in real
  cryptology literature.
- Check whether Z408 and Z340 share a reusable homophone-assignment
  convention (an open question in `knowledge-base/state.md`).
- Catalog (read-only, no new claims) a sample of publicly documented prior
  Z13 solution attempts, as SQ-4 groundwork.

## 1. Z408 — verification

**Claim:** 408-symbol homophonic substitution cipher, mailed in three parts
to three Bay Area newspapers (Vallejo Times-Herald, San Francisco Chronicle,
San Francisco Examiner) on July 31, 1969; solved within about a week by
Donald and Bettye Harden, a Salinas schoolteacher couple, by August 5, 1969.

**Findings:** Corroborated by multiple independent secondary sources:
- Wikipedia's "Zodiac Killer" article states the cipher was sent July 31,
  1969, is 408 characters, and gives the Hardens' solve date as August 5,
  1969.
- derekbruff.org's cryptography course page and the Zodiac Killer Ciphers
  Wiki (`zodiackillerciphers.com`) both independently confirm the
  three-newspaper split-mailing and the Harden couple's role.
- One nuance found and worth recording: the Harden solution left the final
  18 characters of the message undeciphered/ambiguous — this is reported
  consistently enough (multiple sources) to note here, though it was not
  traced to a single primary FBI document this session.

**Assessment:** the symbol count, mailing date, newspaper trio, solver
names, and approximate one-week solve timeline are corroborated across
independent secondary sources (general-audience cryptography blog,
community wiki, Wikipedia). No single primary-source FBI document or
newspaper archive scan was directly read this session — see Limitations.

**Sources:**
- [Zodiac Killer — Wikipedia](https://en.wikipedia.org/wiki/Zodiac_Killer)
- [The Zodiac Ciphers: Messages from a Murderer — derekbruff.org](https://derekbruff.org/blogs/fywscrypto/historical-crypto/the-zodiac-ciphers-messages-from-a-murderer/)
- [Solved 408-character cipher — Zodiac Killer Ciphers Wiki](https://zodiackillerciphers.com/wiki/index.php?title=Solved_408-character_cipher)

## 2. Z340 — verification

**Claim:** 340-symbol cipher sent November 1969; solved December 2020 by
David Oranchak, Sam Blake, and Jarl Van Eycke; FBI-confirmed.

**Findings:**
- Z340 was mailed to the San Francisco Chronicle on **November 8, 1969**
  (Wikipedia; corroborated by Cipher Mysteries and Discover Magazine).
- It was solved by **David Oranchak** (US software developer), **Sam
  Blake** (Australian mathematician), and **Jarl Van Eycke** (Belgian
  programmer, author of the AZdecrypt tool), who combined a "knight's move"
  transposition insight with homophonic-substitution solving software.
  Oranchak/Blake/Van Eycke submitted their solution to the FBI on
  **Saturday, December 5, 2020**.
- **FBI confirmation:** the FBI's San Francisco field office publicly
  confirmed the solve via a tweet on **December 11, 2020**, stating in
  part: *"The FBI is aware that a cipher attributed to the Zodiac Killer
  was recently solved by private citizens... The Zodiac Killer case
  remains an ongoing investigation for the FBI San Francisco division and
  our local law enforcement partners."* This wording is reported
  consistently by CNN, The Hill, and other outlets covering the
  announcement.
- The three solvers later published their own account of the method:
  Oranchak, Blake, and Van Eycke, **"The Solution of the Zodiac Killer's
  340-Character Cipher"** (arXiv:2403.17350, submitted March 26, 2024) —
  this is effectively a primary-source account from the solvers themselves,
  describing Z340 as combining transposition with homophonic substitution
  and noting deliberate irregularities the killer introduced.

**Assessment:** symbol count, mailing date, solver names/nationalities/
roles, submission date, and the FBI confirmation (including its actual
wording and communication channel — a tweet, not a formal press release)
are all corroborated across multiple independent sources, including a
solver-authored technical paper. This is the best-sourced of the three
ciphers this session.

**Sources:**
- [FBI confirms Zodiac Killer's 340 cipher solved — The Register](https://www.theregister.com/offbeat/2020/12/12/fbi-confirms-zodiac-killers-340-cipher-solved-by-trio-of-amateur-math-and-software-codebreakers/1506059)
- [After 51 years, the Zodiac Killer's cipher has been solved — CNN](https://www.cnn.com/2020/12/11/us/zodiac-killer-cypher-340-code-trnd)
- [Cracking the Zodiac Killer's Cipher — Discover Magazine](https://www.discovermagazine.com/how-mathematicians-cracked-the-zodiac-killers-cipher-43137)
- [Zodiac Z340 is CRACKED! — Cipher Mysteries](https://ciphermysteries.com/2020/12/11/zodiac-z340-is-cracked)
- Oranchak, Blake, Van Eycke, ["The Solution of the Zodiac Killer's 340-Character Cipher," arXiv:2403.17350](https://arxiv.org/abs/2403.17350) (March 2024)

## 3. Z13 — verification

**Claim:** 13-symbol cipher, "My name is—" prefix, sent April 1970, remains
unsolved.

**Findings:**
- The Zodiac Killer Ciphers Wiki dates the Z13 communication to **April 20,
  1970**, sent to the San Francisco Chronicle, and gives the symbol count
  as **13**. Wikipedia's Zodiac Killer article corroborates the 13-symbol
  count and the "has not been definitively solved" status. Both sources
  independently agree Z13 remains unsolved as of the most recent findable
  reporting (through 2026 coverage referenced by secondary sources tracking
  ongoing claims).
- Structural note found and worth recording for the Statistician's future
  work: the wiki's ASCII transcription of the symbol sequence and reported
  symmetry (grouped in a pattern with a repeated "eight-ball" symbol acting
  as a separator) suggest internal structure that could matter for SQ-3/
  SQ-2 — flagged here, not yet verified against a primary scan.

**Assessment:** the 13-symbol count and April 1970 date are corroborated by
two independent sources; the unsolved status is corroborated by every
source consulted this session, including community moderation activity
(see §5) confirming no accepted solution exists as of recent activity.

**Sources:**
- [Unsolved 13-character "My name is" cipher — Zodiac Killer Ciphers Wiki](https://zodiackillerciphers.com/wiki/index.php?title=Unsolved_13-character_%22My_name_is%22_cipher)
- [Zodiac Killer — Wikipedia](https://en.wikipedia.org/wiki/Zodiac_Killer)

## 4. SQ-3 — unicity distance / attack-surface analysis

**Question:** what does the cryptology literature say about how much
ciphertext a homophonic substitution cipher needs for a statistically
unique solution, and what does that mean for Z13's 13 symbols?

**Grounding (Shannon's unicity distance):** Shannon's 1949 definition gives
unicity distance U = H(K) / D, where H(K) is the entropy (in bits) of the
key space and D is the redundancy of the plaintext language (bits/
character). For a **simple** (non-homophonic) monoalphabetic substitution
cipher over English, the textbook calculation is: key space = 26! ≈
4.03×10²⁶ possible letter permutations, so H(K) = log₂(26!) ≈ 88.4 bits;
English plaintext redundancy is commonly estimated at D ≈ 3.2 bits/
character (i.e., English carries only about 1.0–1.5 bits/character of
actual information against ~4.7 bits/character for a uniform 26-letter
alphabet); this gives **U ≈ 88.4 / 3.2 ≈ 28 characters** — the
oft-cited figure for how much ciphertext a simple substitution cipher needs
before, in principle, only one legible decryption remains.

**Applying this to Z13:** a **homophonic** substitution cipher (which both
Z408 and Z340 are/were) has a *larger* key space than simple substitution,
because it must additionally specify which of several possible cipher
symbols maps to each plaintext letter (many-symbols-to-one-letter), not
just a single permutation. A larger key entropy H(K) means a **larger**
unicity distance is needed, not a smaller one — i.e., homophonic ciphers
generically require *more* ciphertext than simple-substitution's ~28-
character baseline to reach a unique solution, all else equal. Z408 and
Z340 used roughly 50-60+ distinct cipher symbols across their runs (a
detail consistent with a homophone-set well above 26); at Z13's length of
only 13 symbols — under half the ~28-character simple-substitution
baseline, and further below whatever larger figure the true homophonic key
space implies — the ciphertext is short even relative to the *easier*
simple-substitution case, before even accounting for homophony's added key
entropy.

**Assumptions stated explicitly (so they can be checked/challenged):**
1. English redundancy ≈ 3.2 bits/character (a standard, though not
   universally agreed, estimate; some estimates run lower, which would
   *increase* the required unicity distance further, not decrease it).
2. The 26!-permutation figure applies to simple monoalphabetic
   substitution; Z13's true key space depends on the actual homophone-set
   size used, which is not yet independently established for Z13
   specifically (Z408's and Z340's homophone-set sizes are known from
   their solved keys; Z13's key, being unknown/unsolved, cannot yet supply
   this number directly — this is a real gap SQ-2's calibration work should
   close, since it would let the Cryptanalyst give a homophonic-specific
   U estimate rather than reasoning from the simple-substitution baseline).
3. No adjustment made here for any structural regularities in Z13 itself
   (e.g., the possible repeated-symbol pattern noted in §3), which could
   either reduce effective key entropy (helpful) or reflect an unusual
   construction not captured by a standard-alphabet model (unhelpful) —
   flagged as a sensitivity concern for the Statistician/Cryptanalyst to
   resolve with the primary transcription once SQ-1 is complete.

**Defensible SQ-3 statement (with disclosed limitations):** using the
textbook Shannon unicity-distance framework, a 13-symbol cryptogram falls
well below the ~28-character threshold established for the *simpler*
non-homophonic case, and homophonic substitution's larger key space only
pushes the required length upward from there. This is consistent with,
and gives a literature-grounded reason for, the working position already
recorded in `config/sidequests.md`/`knowledge-base/state.md` that Z13
likely cannot support a statistically unique, crib-free solution — but
this session did not derive a homophonic-specific numeric U for Z13
(that requires Z13's actual homophone-set size, which is presently
unknown precisely because Z13 is unsolved — a genuine circularity this
project should name plainly rather than paper over). What *would* change
this conclusion: an external crib (narrowing the plaintext search space
independent of the ciphertext itself), or a principled, evidence-based
constraint on Z13's homophone-set size borrowed from Z408/Z340 — which §5
below addresses and finds does not currently hold in a simple form.

**Sources:**
- [Unicity distance — Wikipedia](https://en.wikipedia.org/wiki/Unicity_distance)
- [Unicity Distance — University of Miami CS (Burt Rosenberg)](https://www.cs.miami.edu/home/burt/learning/Csc609.011/Unicity/)
- [Unicity Distance — practicalcryptography.com](http://practicalcryptography.com/cryptanalysis/text-characterisation/statistics/)
- ["A Modified Simple Substitution Cipher With Unbounded Unicity Distance," IACR ePrint 2019/621](https://eprint.iacr.org/2019/621.pdf) (background: confirms that increasing a substitution cipher's effective key space, as homophony does, is a known lever for increasing unicity distance)

## 5. Do Z408 and Z340 share a homophone convention that could narrow Z13's search space?

**Finding:** No, not in any simple, directly reusable way. Cipher Mysteries
— an established Zodiac-cipher research/commentary site frequently cited
in this space — reports that despite Z408 and Z340 using visually similar
symbol styles, **only five symbol-to-letter correspondences coincide
between the two solved ciphers** (reported as matching on N, I, A, E, and
one additional assignment). The two ciphers' cipher alphabets and full
lookup tables otherwise differ. This is a secondary/enthusiast source, not
a peer-reviewed one, so this finding should be treated as provisional
until independently checked against the two solved keys directly (a
short, concrete task for SQ-2, once undertaken) — flagged here rather than
silently treated as settled, per this project's own sourcing-disclosure
rule.

**Implication for the open question in `knowledge-base/state.md`:** the
answer, on current evidence, is "no principled shared convention exists
that would meaningfully narrow Z13's search space" — five coincidental
letter-symbol matches out of a much larger combined symbol set is
consistent with partial chance overlap in a small alphabet, not a
reusable cipher-construction convention. This should keep the open
question open rather than resolve it, but it does mean the "cross-cipher
homophone convention" route to a defensible Z13 crib looks weak absent
new evidence — relevant directly to §4's finding that an external crib
is the main thing that could change the unicity-distance conclusion.

**Source:**
- [Thoughts on the Zodiac Killer Z408 and Z340 ciphers — Cipher Mysteries](https://ciphermysteries.com/2011/09/13/thoughts-on-the-zodiac-killer-z408-and-z340-ciphers)

## 6. SQ-4 groundwork — sample of publicly documented prior Z13 claims (read-only cataloging)

Per the ethical boundary (`README.md`), this section catalogs already-public
claims and their documented reception; it proposes, endorses, or leans
toward no identification of any kind.

- The **Zodiac Killer Ciphers Wiki's "Z13 Solutions" page** documents that
  **hundreds** of candidate plaintext/name solutions have been submitted by
  amateur researchers over the years, produced via straight substitution,
  anagramming, "relaxed constraint" methods (wildcards, multiple
  operations), and cross-application of the (unrelated) Z408 key. The page
  itself concludes that ordinary-substitution candidates alone are "still
  numerous, which increases the difficulty of knowing which one is
  correct," and that anagram-based methods are flexible enough to be
  "nearly impossible to validate" — i.e., the wiki's own maintainers
  identify excess researcher-chosen flexibility as the reason no candidate
  can be adjudicated, which is exactly the failure mode
  `agents/skeptic.md` and `methods/falsification-standard.md` are built to
  catch.
- One specific, widely reported claim: in 2021, French engineer **Fayçal
  Ziraoui** publicly claimed to have solved Z13 (and Z32), proposing the
  cipher decodes to a short name-like string. Coverage of the claim (SFGate,
  Medium/Lori Lamothe) reports that Zodiac-research community moderators
  removed his posts and that other researchers were skeptical, citing his
  rapid turnaround and lack of independently reproducible method — a
  documented non-acceptance, not a confirmed solution.
- Separately, moderators of a large (~50,000-member) Zodiac-focused
  subreddit are reported to have removed Z13-solution posts generally, with
  a stated reason that the cipher "is not solvable at all without more
  information from the author" and that "any proposed solution to the Z13
  amounts to straight up guesswork, with no way to confirm it at all" — a
  community-level statement of essentially the same position this
  project's own SQ-3 analysis (§4 above) arrives at independently from the
  cryptology literature.

This is a partial sample, not a complete SQ-4 catalog (which remains a
separate, larger deliverable per `config/sidequests.md`). No new claim,
ranking, or identification is proposed here; every item above merely
records what has already been publicly reported and how it was received.

**Sources:**
- [Z13 Solutions — Zodiac Killer Ciphers Wiki](https://zodiackillerciphers.com/wiki/index.php?title=Z13_Solutions)
- [French Engineer Says He Solved the Zodiac Cipher — Medium/Lori Lamothe](https://medium.com/@lorilamothe29/french-engineer-says-he-solved-the-zodiac-cipher-that-reveals-the-killers-name-but-who-was-eadcb8a6b509)
- [Feuds erupt after man claims he found Zodiac Killer's identity in a cipher — SFGate](https://www.sfgate.com/crime/article/zodiac-unsolved-ciphers-my-name-is-solutions-16265489.php)

## Limitations (apply to every finding above)

- All sourcing this session is secondary (news coverage, community wikis,
  one solver-authored arXiv paper for Z340). No FBI file or newspaper
  archive scan was directly read/checksummed this session — full SQ-1
  primary-source acquisition (images, checksums, a provenance file) remains
  open and is the natural next slice of SQ-1 work.
- The "five coincident symbol-letter matches" figure (§5) comes from a
  single enthusiast source and should be independently rechecked against
  the two solved keys directly once they're in this repo's own corpus.
- The SQ-3 unicity-distance conclusion (§4) uses the simple-substitution
  U≈28 baseline as a reasoning anchor because Z13's own homophonic key
  space cannot yet be sized directly (it's unsolved) — this is a stated
  limitation, not a hidden one, and should be revisited once SQ-2
  calibration work establishes Z408's/Z340's actual homophone-set sizes as
  a modeling reference point.
- Per `methods/falsification-standard.md`, none of the above is proposed as
  a reproducible script-backed Confirmed Finding; §1–§3's corroborated
  factual claims (dates, symbol counts, solver names, FBI confirmation) are
  proposed for `knowledge-base/state.md` promotion below *with* their
  secondary-sourcing limitation disclosed, per the standard's explicit
  allowance for that category of entry.

## Next steps

1. SQ-1: acquire actual primary-source images/transcriptions (FBI-released
   files or newspaper archive scans) with explicit user authorization
   before any bulk download, and produce the checksum/provenance file this
   session did not attempt.
2. SQ-2: begin Z408/Z340 reproduction, which would also let the
   Cryptanalyst compute a homophonic-specific (not simple-substitution-
   baseline) unicity distance using the real homophone-set sizes — closing
   the circularity noted in §4.
3. SQ-4: expand §6's partial sample into the full sourced catalog file the
   sidequest calls for.
4. Independently re-verify §5's five-symbol-match figure against the
   solved keys directly rather than relying on a single secondary source.
