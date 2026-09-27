# Source provenance — Wikimedia Commons Z13 cipher image (accepted, primary-source-tier)

**Status: ACCEPTED.** This closes the "primary-scan-direct-view gate" repeatedly named as open in
`knowledge-base/state.md`'s Z13 repeat-pattern entries — this is this project's first own direct view of
the actual Z13 cipher glyphs, not a secondary paraphrase or an ASCII transcription taken on trust.

- **Origin:** `https://commons.wikimedia.org/wiki/File:Zodiac-name-cipher.png`, direct file URL
  `https://upload.wikimedia.org/wikipedia/commons/b/b3/Zodiac-name-cipher.png`. Per the file's own
  Wikimedia Commons metadata: `ImageDescription` = "Cipher claiming to be Zodiac's name",
  `DateTimeOriginal` = 1970-04-20 (the date of the original letter), `Credit` = "This image has been
  extracted from another file" (the source scan is indexed on Wikisource as
  `Zodiac-name-and-bomb.djvu`), `Artist` = "Zodiac killer" (per the file's own attribution field),
  license = public domain (US, published 1931–1977 without a copyright notice). Uploaded/extracted
  2019-01-20 per the file history.
- **Retrieved:** 2026-09-27, via direct HTTPS `curl` to the raw `upload.wikimedia.org` file URL (not a
  WebSearch summary, not a secondary paraphrase).
- **File and checksum (SHA-256):**
  - `z13-cipher-original.png` — `caf00fe7c7cb9643bf602b808bde6f2b0a4147433ecebe8829933ad63388008f`
    (450×28 px, 2018 bytes, genuine PNG confirmed via `file`)
- **Content note (purely structural, no suspect-related content)**: this image contains only the
  13-character cipher glyph sequence itself, immediately following the letter's "My name is—" line. No
  other part of the 1970 letter, and no suspect-identification content of any kind, is included in this
  cropped extraction or discussed in the analysis it supports.

## What was verified by direct visual inspection

Viewed the image directly (via local upscaling for legibility, not OCR or automated transcription). The
13-position sequence, read left to right: **A, E, N, [circled crosshair/target symbol — unique, appears
once], [circled pinwheel/segmented symbol — call it "glyph-P"], K, glyph-P (same pattern as position 5),
M, glyph-P (same pattern again), [hook/shepherd's-crook shape — unique, appears once], N, A, M.**

This **directly confirms**, by independent visual inspection of the primary source rather than trusting a
secondary transcription, the repeat-pattern structure already on record in this project's own
`knowledge-base/state.md` (sourced there from a directly-fetched Wikisource page, itself one tier below
this): position 1 = position 12 (`A` = `A`); position 3 = position 11 (`N` = `N`); positions 5, 7, and 9
all share the same glyph (`glyph-P`, the circled pinwheel/segmented symbol); position 8 = position 13
(`M` = `M`). See `logs/2026-09-27-sq3-z13-primary-source-direct-view.md` for the full disclosure and what
this does and does not settle.
