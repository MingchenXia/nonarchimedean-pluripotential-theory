# Index diacritics polish, 6 October 2026

The generation wrapper now displays **Kołodziej argument** and **refined
Hodge–Poincaré polynomial** with the correct diacritics. Makeindex display
aliases retain the original sort keys; the active mathematical TeX sources
and bibliography do not change.

The baseline is the 4,426-page sequential/K3 edition, work commit
`f1148fc680c4897aa70e4397bcefa2c3ff89c6be`. Main remains
`00957114db21b627e97369563032ceda9cea09c7`. The two spellings were found
and deferred during that edition's complete index reading.

## Change and preservation

Only `manuscript/editorial/tools/make_book_index.py` changes in the build
configuration. Existing Monge–Ampère and Stokes normalization is retained.
The two additional display aliases are raw lines 365 and 641, with page
arguments 1823 and 3943. Their original sort fields and encapsulation are
preserved, as are **all 778 ordered page arguments** and all other
previously normalized keys.

The raw index is byte-identical to the baseline, SHA-256
`10bda73dc8b55694efff986e5624732a3c8090314d0a478f6cb2ceed67992547`.
The normalized index has 28 changed raw entries: the preceding 26 and
these two additions. It has SHA-256
`bb9f6997c37d03fac56b79fedc591305cadde266a6bed4bd12d014117f112728`.
The wrapper has SHA-256
`94c6a494dc0fffc1ee22fd7bd0a965eea951b6fd005c5a7f78367c1efe46bdf1`.
The latexmk configuration and gitignore retain their bytes.

All **425 active TeX inputs**, both bibliographies, **108 protected inputs**,
native catalogue source/PDF, **84 preceding frozen manifests** and **145
preceding exports** are preserved. Canonical statuses, historical receipts,
the BJ22 Siu/envelope boundary and the open native editor are unchanged.
No original theorem, primary-source page audit, model call or verification
receipt is added.

## Build, comparison and actual reading

The final book remains **4,426 pages**, with 20,565,901 bytes and SHA-256
`7ad7be8f51d47cf30f90918a62cc15e8cacaea5c029d4643f74909e699ebe867`.
Compilation, references, bibliography, index, navigation and the canonical
inventory pass. There are zero unresolved references/citations, missing
characters, overfull boxes, TeX/package/pdfTeX warnings or rerun requests.
The 954 underfull boxes equal the baseline count.

The index accepts **778 entries**, rejects none and reports no warnings.
Its 777 page groups and 424 numerical destinations resolve. Navigation
retains **22,099 named destinations, 47,241 internal links, 171 URL links,
2,578 contents entries and six parts**, with no invalid destinations.
The closure retains 12,914 unique labels, 409 cited entries and 703
bibliography keys.

A comparison of complete extracted text on **every physical PDF page**
finds a difference only on **page 4401**, which contains the two corrected
displays. All other **4,425 page texts** are byte-identical to the preceding
export. This automated comparison is not a new whole-book rereading.

All **twelve selected final pages** were read as complete extracted text
and displayed in **six sheets**: physical page 69 and pages 4397–4407.
This covers the contents destinations, complete index and bibliography
transition. The corrected glyphs and their links are readable. The matching
review PDF has SHA-256
`88adfcd778a5e2ea07a2283865a0a489edaf50d64ebdf69ac7777234bdbbef85`.
The frozen all-true view manifest has SHA-256
`1dfd97432f766bac379c192dc77540dce9ceed5d383ccbe4e22affd4ea72330c`;
the final reading record has SHA-256
`217f78d1bdc0a13d7111914f140b12d2db118c99ead6df8bfe7fbc12afbbb151`.
The release gate pins each selected image/text, the preceding byte
preservation and the final PDF.

Preserve immutable book/review/source artifacts and the current closure
ledger, verify all source archive member bytes, fetch main and work,
push work and update the draft PR. No fresh isolated archive compilation
is claimed. Then continue exact-primary-source research and integrate
incoming author progress under the standing GitHub authorization.
