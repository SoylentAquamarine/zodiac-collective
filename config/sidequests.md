# Cryptanalysis-oriented sidequest queue

Sidequests are bounded, achievable pieces of work. Each must produce a
reusable artifact, answer a decision, or remove a named blocker. The lead
agent may reprioritize them, but should record why.

## SQ-1 — Canonical source corpus (blocking, start here)

**Purpose:** amateur secondary transcriptions of Z13's exact symbol shapes
vary in the wild, and this project's every downstream claim depends on
working from verified primary-source material rather than a convenient
retyped version. This sidequest is not optional groundwork — it blocks
every other sidequest and the entire Statistician/Cryptanalyst/Linguist
track.

**Scope:** pull verified, checksummed high-resolution images and
transcriptions of Z13, Z408, and Z340 from primary sources — documented
FBI-released files and original newspaper archive scans — the same way
`comms/` Round 1 of the sibling Voynich project evaluated and selected a
canonical transcription over alternatives. Record, for each source: origin,
license/rights, retrieval method, exact symbol-by-symbol transcription
with any ambiguity disclosed rather than silently resolved, and a checksum
once pulled. Do not bulk-download anything without explicit user
authorization — this is a standing rule across all sibling projects.

**Deliverables:** a source-comparison writeup, a provenance file once
sources are selected, and a normalization script with a full
ambiguity-audit trail once normalization begins.

**Stepping-stone value:** nothing downstream (frequency analysis,
cross-cipher homophone comparison, unicity-distance grounding, any solution
attempt) is reproducible or falsifiable without this.

**Laptop/worker-node work:** none yet — this stage is source discovery and
licensing/provenance research, not computation.

## SQ-2 — Solved-cipher reproduction (methodology calibration)

**Purpose:** validate tooling and homophonic-substitution-solving
methodology by reproducing known answers before trusting any method on
Z13, which has no known answer key.

**Scope:** using SQ-1's canonicalized corpus, independently reproduce the
Z408 solution (Donald and Bettye Harden's August 1969 solve) and the Z340
solution (David Oranchak, Sam Blake, and Jarl Van Eycke's December 2020
solve, FBI-confirmed) from scratch, without consulting the known plaintext
during the solving process. Document tooling, method, any point where the
known answer had to be consulted for debugging (and why, disclosed
plainly, since it breaks strict independence), and wall-clock/compute cost.

**Deliverables:** a reproducible solving script or documented manual
method, a written record of the reproduction process, and a direct
comparison between the reproduced solution and the historically documented
one.

**Stepping-stone value:** the direct analog of the sibling Voynich
project's Naibbe/Cardan-grille calibration controls and the Rongorongo
project's SQ-4 historical recovery benchmark — this validates the
methodology on a known answer before it is ever pointed at Z13.

**Laptop/worker-node work:** homophonic substitution search (hill-
climbing, simulated annealing, or equivalent), scoring-function
implementation and testing.

## SQ-3 — Z13 information-theoretic attack-surface analysis

**Purpose:** formally establish, before any solve attempt, whether 13
symbols of homophonic-substitution ciphertext can support a statistically
unique solution at all — this is itself a real deliverable, the direct
analog of how the Rongorongo project asks "what kind of system is this"
before assuming a decipherment path is even well-motivated.

**Scope:** using the cryptology literature on unicity distance, compute or
cite the expected unicity distance for a homophonic substitution cipher
over English at Z13's approximate parameters (alphabet/homophone-set size,
message length, per-character entropy of English), stating every
assumption explicitly and testing sensitivity to reasonable alternative
assumptions. Determine what, if anything, would need to be true (e.g. an
external crib narrowing the plaintext space, or a cross-cipher homophone
convention from SQ-... the Statistician's comparative work) for a
defensible solution to be possible at all.

**Deliverables:** a written analysis with cited sources, explicit
assumptions and sensitivity checks, and a clear statement of what would
count as sufficient defensible evidence for a claimed Z13 solution given
the finding.

**Stepping-stone value:** answers a genuinely prior question — attempting a
solution search before this is settled risks repeating the single most
common, well-documented failure mode in Z13's own research history
(constructing a plausible-looking fit to short ciphertext without
establishing the method could discriminate a real solution from noise).

**Laptop/worker-node work:** none required for the core analysis; optional
simulation work (e.g. measuring how often a frozen scoring procedure
produces a "plausible" match to an unrelated 13-character target phrase)
can run on a worker node once designed.

## SQ-4 — Prior-claims catalog

**Purpose:** document previously publicized claimed Z13 solutions and
identity theories, and the specific, named reason each was rejected or
remains unconfirmed, so this project doesn't re-tread debunked ground or
have its own eventual work compared unfavorably to a claim it never
checked.

**Scope:** catalog publicly claimed Z13 solutions (proposer, date, claimed
plaintext, and documented reason for rejection or non-confirmation —
evidentiary flaw, non-reproducibility, excess researcher-chosen
flexibility, failure to survive scrutiny, etc.) and publicly reported
named-suspect theories with their documented evidentiary status. This is
**read-only cataloging of already-public claims** — this sidequest does
not generate new claims, evaluate suspect identity, or produce any new
accusatory content, per the project's ethical boundary (`README.md`,
`CONTRIBUTING.md`).

**Deliverables:** a sourced catalog file, each entry citing where the claim
was originally made and where its rejection/non-confirmation was
documented.

**Stepping-stone value:** directly informs the Skeptic's flexibility test
(SQ-3's sibling concern) and prevents this project from re-proposing
already-debunked candidate plaintexts or already-rejected solution
methods.

**Laptop/worker-node work:** none — this is research and documentation
work.

## Initial priority

Start SQ-1 first — it is a hard blocker. Do not begin SQ-2 substantively
until primary-source transcriptions of Z408 and Z340 are canonicalized.
SQ-3 (attack-surface analysis) can begin in parallel with SQ-2, since it
depends only on Z13's length and general cryptology literature, not on
having already reproduced the solved ciphers — but no solution *attempt*
on Z13 (a later, separate step) should begin until both SQ-2 and SQ-3 are
substantially complete. SQ-4 can begin immediately and run in parallel with
everything else, since it is independent research and documentation work
that does not depend on the corpus pipeline.
