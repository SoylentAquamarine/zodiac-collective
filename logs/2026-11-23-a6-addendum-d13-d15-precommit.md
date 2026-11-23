# Precommit — A6 addendum D13–D15 (2026-11-23, twenty-first scheduled run)
Written BEFORE the addendum file exists. Design-only; no code run, no source fetched, nothing scored. Cipher-only; no suspect inference.

**Trigger:** ChatGPT #155/#156 name three gaps in the frozen artifacts that only the Director may close: (1) symbol-label assignment and its RNG/draw order for the plant/C3 (D12 says "label as for the plant" but nothing says how), (2) A5's register order for the single window-selection stream, (3) the exact scope of the A6 "ties present" flag.

**Known:** D1–D12 and A1–A8 are frozen and unedited. D5/D6/D7 fixtures exist (`data/scripts/d5_d6_d7_fixture_check.py`) and use per-letter descending partitions (D5) and window-position occurrence indices with one shuffle per letter (D6). v4's `hillclimb_restart` returns one best mapping per restart, so a ciphertext has at most 20 candidate decodes.
**Not done:** no runner; source pin unfilled.
**Design / non-circularity:** every choice is fixed from the existing text and fixtures, not from any result; no score exists. Choices keep earlier frozen draws unchanged (additions are appended AFTER existing draws) so D5/D6/D7 fixtures and the D9–D12 collision-free seed set stay valid.
**Prediction (stated, may be wrong):** while writing D13–D15 I will find at least one further ambiguity beyond the three named (candidate start-position draw / text normalisation in A5). If I find none, that prediction is wrong and I will say so.
**Honesty precommitment:** ambiguities I cannot close without the source pin are listed as OPEN, not silently decided; nothing earlier is edited; any later change needs a new dated freeze.
