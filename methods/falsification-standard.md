# Falsification and Promotion Standard

This is the minimum bar for moving an interpretation into **Active
Hypotheses**. It is deliberately stricter than the bar for recording a
measurement in **Confirmed Findings**. A measurement can be reliable while
supporting several incompatible explanations.

## The ethical boundary applies here too

Before anything else: **this project studies a cipher, not a suspect.** No
finding, hypothesis, or promotion under this standard may propose,
evaluate, or imply a new suspect identification or accusatory claim about
any living or identifiable private individual. A candidate Z13 decryption
is evaluated purely on cryptologic merit — does it produce a statistically
supportable, reproducible plaintext under a procedure that survives the
Skeptic's flexibility test — and its promotion through this standard never
extends to, or implies, a conclusion about offender identity. See
`README.md` and `CONTRIBUTING.md` for the full statement of this boundary.

## Minimum bar for Confirmed Findings

Confirmed Findings is a much lower bar than Active Hypotheses — a
measurement or result, not an interpretation, and it doesn't need
alternatives explicitly ruled out. But every entry should still be well
documented and reproducible, not left to habit. Before a PR adds a bullet
to `knowledge-base/state.md`'s Confirmed Findings, it should have:

- a script, a manifest, or a directly-read and cited image/text protocol
  that produced the number or claim — not a description of a result
  alone, with nothing behind it a reader could rerun;
- the actual output (a summary JSON, a report, or both) committed to the
  repo, not only quoted or paraphrased inline in the bullet;
- enough provenance (source commit, checksum, seed, sample definition)
  that a third party could rerun it and reasonably expect the same
  result;
- for anything resting on an external secondary source (a search-engine
  summary, a news article or documentary not read directly, a secondary
  retelling of case facts), an explicit disclosure of that limitation in
  the same entry — never presented as if it were independently verified
  when it wasn't. This applies with particular force here: much of what is
  "commonly reported" about the Zodiac case in casual secondary sources is
  itself imprecise or disputed relative to primary law-enforcement and
  contemporaneous press records (exact dates, letter contents, and
  investigative details all vary by source), so a claim's provenance chain
  matters more than usual.

This does not require independent adversarial review the way Active
Hypotheses does — that remains the harder bar. It requires that a
Confirmed Finding always be *checkable*, even when no one has checked it
yet.

## Required hypothesis card

Before running its decisive test, the proponent must record:

1. **Claim** — one operational statement narrow enough to fail.
2. **Alternatives** — at least the strongest competing explanations that
   fit the same observation (for a candidate Z13 plaintext: chance fit
   under researcher-chosen scoring flexibility, a different but equally
   "plausible" alternative plaintext, or "not solvable without a crib" as
   the null), or a reason one family is inapplicable.
3. **Discriminating prediction** — an outcome expected under the claim and
   not equally expected under the named alternatives.
4. **Failure condition** — a numerical threshold, held-out check, or
   scoring-procedure test that would count against the claim. This may not
   be invented after seeing the result.
5. **Units and controls** — the ciphertext, transcription version,
   comparison corpora, exclusions, and randomization unit.
6. **Dependencies** — transcription, symbol-segmentation, and any assumed
   cross-cipher homophone convention that could manufacture the result.

## Evidence required for promotion

A candidate can enter **Active Hypotheses** only when all of the following
are present:

- a reproducible script or a cited, inspectable image/protocol;
- an effect size and uncertainty or an equally explicit qualitative
  decision rule, not only a p-value;
- a negative or shuffled control appropriate to the claim (for a candidate
  Z13 plaintext: a demonstration of how often the same frozen scoring
  procedure produces an equally "plausible" match to an unrelated target
  phrase);
- sensitivity to at least the material transcription/segmentation
  confounds identified in the hypothesis card;
- a held-out or genuinely out-of-sample test when the claim was developed
  by exploring the same data;
- independent adversarial review by the other collaborator, including
  reproduction of the headline result or a documented reason reproduction
  is impossible;
- a statement of what the result does **not** distinguish — for a Z13
  candidate, this must explicitly state that a cryptologic solution does
  not by itself constitute or imply a suspect identification.

Promotion means "worth sustained falsification," not "solved." Confirmation
requires surviving the Skeptic's targeted test and explaining evidence
that the strongest alternative does not explain equally well.

## Automatic stop conditions

Do not promote when any of these applies:

- the observation was selected after inspecting the same test set and has
  no holdout;
- the effect disappears under one reasonable transcription or segmentation
  policy;
- the comparison changes source, sampling unit, or scoring method at the
  same time as the claimed variable;
- the proposed scoring/search procedure has enough unconstrained choices to
  fit arbitrary short ciphertext to a chosen plaintext — the specific,
  publicly documented failure mode of prior amateur Z13 "solutions";
- the result only restates a known property (e.g. that Z13 is short) without
  a prediction that separates hypotheses;
- an upstream correction has not been propagated through the full dependent
  analysis chain;
- the claim identifies, accuses, or implies identification of a specific
  named individual beyond what is already part of the extensively publicly
  documented case record — this stop condition is absolute and is never
  waived regardless of how strong the surrounding cryptologic evidence
  appears.

## Current consequence

At launch, the repository has no Confirmed Findings and no Active
Hypotheses — this is a genuine bootstrap state, not a placeholder awaiting
cleanup. The first substantive work is canonical source acquisition
(`config/sidequests.md`, SQ-1), which is itself infrastructure, not a
finding.
