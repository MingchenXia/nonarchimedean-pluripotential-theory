# Remaining full-book overflows — 22 September 2026

## Changes

The eight overflows remaining after the Chapter 18 font-scope
correction are resolved. Seven displays now break at an equality
or between a geometric definition and its parameter conditions.
One frozen Chapter 15 proof is included inside a local group with
one em of emergency paragraph stretch.

The displays are in Chapters 9 (contraction), 14 (pushforward and J),
18 (two live parameter declarations and an imported tower statement),
50 (layer-cake calculation), and 70 (principal-ideal profile definitions).
No mathematical symbols, assumptions, inequalities, conclusions or
formula labels are changed in this layout pass.

The two external sources remain unchanged. The book now includes
layout editions of the interleaved-polyannulus statement and the
conductor-ideal source in
[typesetting_20260922](typesetting_20260922/). Each edition identifies
its controlling original path and SHA-256. The originals continue to
be the mathematical verification objects; this typesetting check is
not represented as a new mathematical production-verification run.

The two live Chapter 18 statements are also preserved byte for byte
before their display reflow in that directory. Their proofs are
unchanged. The exact Chapter 15 proof bytes remain unchanged, as do
the author-supplied CURVE_PSH.tex and Chapter 71.

## Equivalence and build checks

Every display substitution was checked for equality after removing
only the inserted aligned/gathered environment delimiters, alignment
markers, line-break commands and whitespace. This comparison retains
all mathematical commands, signs, words, delimiters and punctuation.
The two complete source editions and the two complete live statements
were compared again after application. Source and edition checksums,
and the normalized block checksums, are recorded in
[the manifest](typesetting_20260922/layout_manifest.json).

The temporary full-book trace has no horizontal or vertical overflow
and still reports standard 10/12-point body type at all 186 include
boundaries. The final production build has 3,913 pages and
18,564,712 bytes, with zero horizontal or vertical overflows and
zero unresolved references or citations.

All eight repaired locations were rendered and visually inspected:
physical pages 380, 633, 788, 1325, 1336, 1349, 3072 and 3522
(printed 312, 565, 720, 1257, 1268, 1281, 3004 and 3454).
The formula continuations and their tags fit within the text block.

The input closure remains 389 TeX files and 11,486 unique labels;
the two editions replace two original inputs in that closure.
There are no missing inputs, duplicate labels, dangling references or
structural defects. The inventory remains 46 active atoms in 14
environments, with tiers (0,5,8,16,17). The source diff is
whitespace-clean. This is a layout check, not a claim that all
mathematical or editorial issues in the book have been resolved.

PDF SHA-256:
`b8697b8d77a14725856d1563e36f210f4d7377d23bb8189e2ce3a11da9c56af9`

The visual pass exposed a separate pre-existing issue in Chapter 14:
the statement of Proposition 14.8.1 says pushforward commutes with J
without a dimension qualification, while its proof computes the sign
(-1)^(dim Y-dim X). The next mathematical pass will reconcile that
statement and proof and check the dependent formulations.
