# Knowledge Base — Current State

Last updated: 2026-09-23 (first research cycle — SQ-1/SQ-3 initial findings)

This file is the shared, evolving understanding of the group. It only
changes via pull request. Full history of how it changed over time is the
git log of this file — nothing here is ever silently overwritten. Every
entry in this file is bound by this project's ethical boundary
(`README.md`): no entry may propose or imply a new suspect identification
or accusatory claim about any living or identifiable private individual.

## Confirmed Findings

- **Cipher basics (symbol counts, dates, solvers).** Z408 is a 408-symbol
  homophonic substitution cipher mailed in three parts to the Vallejo
  Times-Herald, San Francisco Chronicle, and San Francisco Examiner on
  July 31, 1969, solved by Donald and Bettye Harden by August 5, 1969.
  Z340 is a 340-symbol cipher mailed to the San Francisco Chronicle on
  November 8, 1969, solved by David Oranchak, Sam Blake, and Jarl Van
  Eycke, who submitted their solution to the FBI on December 5, 2020; the
  FBI's San Francisco field office publicly confirmed the solve via a
  tweet on December 11, 2020. Z13 is a 13-symbol cryptogram prefaced "My
  name is—", sent April 20, 1970, and remains unsolved as of the most
  recent findable reporting. **Sourcing limitation:** corroborated across
  multiple independent secondary sources (Wikipedia, news coverage of the
  2020 solve, the Zodiac Killer Ciphers Wiki) and, for Z340, the solvers'
  own account (Oranchak, Blake, Van Eycke, arXiv:2403.17350, March 2024) —
  not yet checked against a primary FBI file or newspaper archive scan
  directly by this project. See `logs/2026-09-23-sq1-sq3-source-and-attacksurface.md`
  §1–§3 for full citations and disclosed caveats (e.g. the Harden solution
  reportedly left its final 18 characters undeciphered).

- **Z13's length is far below the unicity-distance threshold established
  for the easier, non-homophonic case.** Shannon's unicity-distance formula
  (U = H(K)/D) gives U ≈ 28 characters as the textbook threshold for a
  *simple* monoalphabetic substitution cipher over English (H(K) =
  log₂(26!) ≈ 88.4 bits; English redundancy D ≈ 3.2 bits/character).
  Homophonic substitution (what Z408, Z340, and presumably Z13 use) has a
  strictly larger key space than simple substitution, which only increases
  the required unicity distance further. Z13's 13 symbols fall well below
  even the simpler 28-character baseline. **Sourcing/limitation:** this
  uses the simple-substitution baseline as a reasoning anchor, not a
  homophonic-specific numeric figure for Z13, because Z13's actual
  homophone-set size cannot be sized directly while Z13 remains unsolved —
  a stated circularity, not a hidden one. See
  `logs/2026-09-23-sq1-sq3-source-and-attacksurface.md` §4 for the full
  derivation, assumptions, and sensitivity notes.

## Active Hypotheses

_(none yet)_

## Rejected Hypotheses

_(none yet — bootstrap state. As the Historian catalogues prior public
Z13 solution claims (`config/sidequests.md` SQ-4), refuted or unconfirmed
ones will be logged here with the specific reason, so they are not
re-proposed without new evidence.)_

## Open Questions

- What is the best-available, most complete, rights-clear, checksummed
  primary-source transcription/image set of Z13, Z408, and Z340 to adopt
  as this project's canonical `/data/` source? See `config/sidequests.md`
  SQ-1 — this blocks everything else.
- Given Z13's length (13 symbols), is a statistically defensible,
  crib-free solution possible at all — and if not, what would even count
  as sufficient defensible evidence for a claimed solution (an internal
  crib, cross-letter corroboration, etc.)? See SQ-3. This is the central
  open question this project must formally answer before any solution
  attempt, not resolve by default toward "it's solvable" just because
  Z408 and Z340 were.
- Do the Zodiac's two solved ciphers (Z408, Z340) share homophone-
  assignment conventions that could narrow Z13's search space in a
  principled, non-arbitrary way? Needs the Statistician's comparative
  analysis against verified solved mappings, not assumption. **Provisional
  finding (2026-09-23, single secondary source — Cipher Mysteries — not
  yet independently rechecked against the solved keys directly):** only
  about five symbol-to-letter assignments coincide between the two solved
  ciphers despite visually similar symbol styles, suggesting no simple,
  directly reusable convention currently exists. Kept open pending the
  Statistician's own direct check. See
  `logs/2026-09-23-sq1-sq3-source-and-attacksurface.md` §5.
- What is the actual, current evidentiary status of the various publicly
  claimed Z13 solutions, and does any survive this project's own
  falsification standard? See SQ-4. Cataloging prior claims is read-only
  research into already-public material — see the ethical boundary in
  `README.md` for what this project will and will not do with this
  catalog.
