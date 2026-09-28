# SQ-2 — scoping proposal: a restricted homophonic substitution model for Z13, pre-registered

**Trigger:** ChatGPT's Meeting 12 decision: "Define a restricted homophonic substitution model and held-out
rule before naming suspects." This is a scoping/pre-registration proposal, not an executed test — writing
the rules down before touching Z13's actual symbols is the entire point (SQ-2's own established rule:
"methodology on a known answer before it is ever pointed at Z13").

## What's already on file

Z408 and Z340 (both genuinely solved homophonic substitutions) give real, documented per-letter homophone
counts (Z408: 7 symbols for E; 4 each for T, O, ...). A homophonic-specific unicity-distance figure is
already calibrated from Z408's real distribution (U ≈ 59 characters) and a modeled (not real) figure
exists for Z340. Z13 itself has no known answer key, 13 symbols, and a documented repeat-pattern
structural-compatibility check (`logs/2026-09-25-sq3-z13-repeat-pattern-flexibility.md`) already exists as
a necessary-condition filter.

## Proposed restricted model (for review, not yet frozen or run)

**Restriction 1 — homophone-set size is bounded by Z408's own documented distribution, not fit to Z13.**
Any candidate mapping may not assign more homophones to a plaintext letter than Z408's own maximum (7).
This prevents the model from having enough free parameters to fit arbitrary short ciphertext by
construction — the single most common failure mode named in Z13's own research history per SQ-3.

**Restriction 2 — the mapping (which ciphertext symbol classes correspond to which plaintext letters) must
be fixed *before* scoring, using only symbol-shape/frequency evidence internal to Z13 plus the Z408/Z340
symbol-shape overlap already catalogued in this project — never adjusted after seeing whether a proposed
plaintext "looks like English."**

**Held-out rule**: Z13 has only 13 symbols total, too short to split into a meaningful fit/held-out
partition the way Voynich's folio-level split works. The substitute proposed here: score any candidate
mapping against (a) a shuffled-ciphertext control (same symbol-frequency profile, random order) and (b) a
same-length random-mapping control drawn from the Restriction-1-bounded space, and require the real
mapping's fit-to-English score to beat both controls by a pre-declared margin, not just beat zero.

**Multiplicity correction**: because many candidate mappings could be tried, any reported "success" must
state how many distinct candidate mappings were attempted and apply a Bonferroni-style correction (or
equivalent) to the significance threshold — a single cherry-picked good-looking mapping out of many tries
is not evidence, per this project's own falsification standard.

## Explicitly not done here

No candidate mapping is proposed or scored. No suspect is named or implied — this document is entirely
about the cipher's mathematical structure, consistent with this project's standing rule that suspect
identification (SQ-4) stays separate and unstarted pending explicit user confirmation. This is a
methodology proposal for ChatGPT and/or the user to review before any actual scoring run.

## Open question for review

Is 13 symbols simply too short for *any* restricted model to produce a statistically meaningful result,
regardless of how carefully the controls are built? SQ-3's own unicity-distance analysis already raises
this as a live possibility. If so, the honest conclusion may be that this sidequest's ceiling is "no
defensible test exists," not a specific reading — worth stating plainly rather than building an elaborate
model that can't actually clear its own bar.
