#!/usr/bin/env python3
"""
Independent-source verification attempt for Z408's homophone-count
distribution (config/sidequests.md SQ-3; Steering Committee Meeting #1
action item: "recheck the ... homophone ... figure against the solved
keys directly" rather than relying on a WebSearch-synthesized answer).

This script does NOT establish a new Z408 homophone-count distribution.
It documents a NEGATIVE result: a candidate directly-fetched third-party
source was tested for internal consistency and FAILED, so it was
rejected rather than adopted. See the companion log entry
logs/2026-09-25-sq3-z408-source-verification-attempt.md for full context,
what other sources were tried this session, and why this project did not
proceed further into a related repository this session.

Source tested: github.com/enRaved/ZodiacKillerCipher (a third-party,
non-official hobby/student repo implementing a Hidden-Markov-Model
attack on Z408). Two files were fetched directly via HTTPS this session
(not via a WebSearch summary) and are committed verbatim in this repo at
data/external-sources/enraved-zodiackillercipher-2026-09-25/, with their
fetch-time SHA-256 checksums recorded in this repo's log entry and below:

  Zodiac.c  sha256=ee64096de67e8b2404752f4ebc5703d20861d05ed96f1e1fe0fb5cf445d5e6ce
  Z408.txt  sha256=615041837f8a212a0767f2f5d6d28e5a0287fab5d70a8a05c53a0c2d6012eafc

Method: a genuine homophonic substitution cipher, by construction, maps
every occurrence of the same ciphertext symbol to the SAME plaintext
letter throughout the message. Zodiac.c embeds (a) an `observationSequence`
array of 408 integers (1-53), claimed to be the Z408 ciphertext symbols in
reading order, and (b) a `zodiacMappings` string of 390 characters, which
independently matches the well-established, widely publicly documented
real Z408 plaintext ("i like killing people because..." -- see
logs/2026-09-23-sq1-sq3-source-and-attacksurface.md Sec 1), with the
final 18 characters of the real 408-symbol cipher (reported elsewhere as
left undeciphered by the Hardens) represented as a separate 18-entry
"filler" tail in the code (see T=390 and its comment in Zodiac.c). If
`observationSequence` really were the correctly-ordered real ciphertext,
zipping its first 390 entries against the 390-character plaintext string
must assign each distinct symbol number to exactly one letter, with zero
exceptions. This script performs that check against the actual committed
source file (not a hand-transcribed excerpt), so it is exactly
reproducible.

Sanity check (a plaintext-content check, not a cipher-structure claim):
the embedded 390-character `zodiacMappings` string visibly matches the
extremely widely and independently corroborated real Z408 opening line.
This is a plausible reason to trust the *plaintext* string but is NOT
evidence that the accompanying `observationSequence` array is a correct,
correctly-ordered transcription of the real ciphertext symbols -- that is
exactly what this script tests, and finds is NOT supportable.
"""

import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
SOURCE_DIR = HERE.parent.parent / "data" / "external-sources" / "enraved-zodiackillercipher-2026-09-25"


def load_observation_sequence() -> list[int]:
    text = (SOURCE_DIR / "Zodiac.c").read_text()
    m = re.search(r"observationSequence\[T\]\s*=\s*\{([^}]*)\}", text, re.S)
    if not m:
        raise ValueError("Could not find observationSequence array in Zodiac.c")
    return [int(x.strip()) for x in m.group(1).split(",") if x.strip()]


def load_zodiac_mappings() -> str:
    text = (SOURCE_DIR / "Zodiac.c").read_text()
    m = re.search(r'zodiacMappings\[390\]\s*=\s*"([^"]*)"', text)
    if not m:
        raise ValueError("Could not find zodiacMappings string in Zodiac.c")
    return m.group(1)


def main() -> None:
    seq = load_observation_sequence()
    plain = load_zodiac_mappings()

    print(f"observationSequence length = {len(seq)} (expect 408)")
    print(f"zodiacMappings length      = {len(plain)} (expect 390)")
    print(f"zodiacMappings[:40]        = {plain[:40]!r}")

    seq_used = seq[:len(plain)]
    seq_filler = seq[len(plain):]
    print(f"Trailing 'filler' symbols not checked (per T=390 comment in "
          f"Zodiac.c, these correspond to the real cipher's final 18 "
          f"reportedly-undeciphered characters): {seq_filler}")

    symbol_to_letter: dict[int, str] = {}
    mismatches = []
    for i, (s, l) in enumerate(zip(seq_used, plain)):
        if s in symbol_to_letter:
            if symbol_to_letter[s] != l:
                mismatches.append((i, s, symbol_to_letter[s], l))
        else:
            symbol_to_letter[s] = l

    print(f"\nDistinct symbols among the checked {len(seq_used)} entries: "
          f"{len(symbol_to_letter)}")
    print(f"Internal-consistency mismatches (same symbol -> different "
          f"letter at a later position): {len(mismatches)} out of "
          f"{len(seq_used)} pairs checked "
          f"({100 * len(mismatches) / len(seq_used):.1f}%)")
    if mismatches:
        print("First 10 mismatches (position, symbol, first-seen-letter, "
              "this-occurrence-letter):")
        for row in mismatches[:10]:
            print("  ", row)

    print()
    if mismatches:
        print("RESULT: FAIL. A genuine homophonic-substitution ciphertext "
              "cannot exhibit this behavior -- each distinct symbol must "
              "decode to exactly one letter everywhere it appears in a "
              "real substitution cipher. This source's "
              "`observationSequence` is therefore NOT usable as an "
              "independently-verified re-derivation of Z408's real "
              "symbol-to-letter key or homophone-count distribution, "
              "despite its plaintext string matching the well-corroborated "
              "real Z408 message. REJECTED -- do not cite this source's "
              "derived homophone counts in knowledge-base/state.md.")
    else:
        print("RESULT: PASS (no internal-consistency violations found).")


if __name__ == "__main__":
    main()
