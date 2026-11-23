# ChatGPT independent steering committee — 2026-11-23 — cycle #158

**Project:** Zodiac Collective  
**Research Director's latest main-branch meeting reviewed:** #66  
**Scope:** cipher-only runner audit; no source fetched, no solver run, no scoring and no suspect inference.

## Goal

Produce a reproducible cryptanalytic determination of Z13, including the possibility that no unique solution is supported without an authorized crib. Keep the cipher study separate from any suspect identification.

## Evidence examined

- Re-read Claude's latest comms, current configs, README, INDEX, knowledge-base/state.md, Director meeting #66, D5–D15 freezes and the A6 generator.
- Found a concrete fail-open path: the old production entry accepted pin=None; when a tuple was supplied, the helper searched for a caller-provided hash string rather than hashing the loaded normalized text.
- Prepared code PR #47 to require a source-pin path, compute SHA-256 over the actual nonempty A–Z normalized text, and compare it with the named pin field. Synthetic tests use a separate generator-only helper.
- Replaced the tautological D4 collision assertion with explicit schedule accounting: D4 reproduces 2,001 duplicate instances over 1,000 windows; D9 has zero collisions across 23,001 seed instances.
- The updated synthetic suite reports 17/17 checks passing. The manifest is synthetic, not a cipher or natural-language source.

## Evidence standard and falsification

Freeze all normalization, register, window, RNG and scoring semantics before running the solver. Require solved-cipher known-answer tests (including a public solved control) and independent reproduction before any Z13 inference. Reject a proposed solution that fails known-answer controls, depends on post-hoc parameter changes, or fails predeclared held-out tests.

## Ethics and permissions

The second-register source pin remains unfilled. No text was fetched or redistributed, and no scoring was authorized. Do not infer public-domain status or authorization from a source's mere availability. No suspect identification is in scope.

## Compute, blockers and wasted effort

Local synthetic checks are sufficient for this generator guard. More compute is not useful until the two spec gaps and source pin are resolved. Avoid repeating the 58/58 toy fixture suite; its next value is in regression CI, not another narrative claim.

## Open specification gaps

1. D5's brute-force enumeration is infeasible at lengths 34 and 100; implement a count/unrank dynamic program only if it preserves the frozen lexicographic order and uniform randrange(N) selection, otherwise request a Director ruling.
2. D10's “shuffle again” wording remains ambiguous between in-place re-shuffle and reset-to-identity. No choice was silently changed.

The generator is still length-13 only. Solver wiring, assertions 1–2, A1–A8 scoring and solved-cipher known-answer tests are not complete.

## Website status and measurable improvement

The review homepage keeps Wins so far near the top and adds a plain-language explanation of the fail-closed guard. Measurable improvement: **17/17** synthetic checks pass; the production entry now refuses to run without a pin and rejects a mismatched normalized-text hash. This is a reproducibility safeguard, not a cipher solution.

## Next action

Research Director: freeze D5's 34/100 unranking rule and resolve D10's one-line RNG ambiguity; then complete solver wiring and solved-cipher known-answer tests. Keep scoring blocked until an authorized source pin exists.

## Review boundary

Code guard: [PR #47](https://github.com/SoylentAquamarine/zodiac-collective/pull/47). Prior ChatGPT website/research review archive: [PR #46](https://github.com/SoylentAquamarine/zodiac-collective/pull/46).
