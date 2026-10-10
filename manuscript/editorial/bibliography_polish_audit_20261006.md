# Bibliography author-name typography and citation ledger

Date: 6 October 2026. Baseline work commit:
`1e0695bd9c76cb012ab4ec9f537e8a9ee71ba735`.
Main: `00957114db21b627e97369563032ceda9cea09c7`.

Exactly two author-name fields change in ComplexGeometry.bib.
ELMNP05 now uses `Musta\c{t}\u{a}` rather than a caron on the final
letter. FN80 now uses `Forn{\ae}ss` rather than an unbraced control
sequence followed by a space. BibTeX previously introduced an actual
nonbreaking space in the surname and generated the label FsN80.
The final render gives Mustaţă, Fornæss and FN80.

The [author's own Michigan homepage](https://websites.umich.edu/~mmustata/)
confirms Mustaţă. The [official NTNU profile](https://www.ntnu.edu/employees/john.fornass)
confirms Fornæss. The [Springer article record](https://link.springer.com/article/10.1007/BF01349254)
confirms FN80's authors, title, volume 248, pages 47--72 and 1980 date;
its ASCII surname is a transliteration. The author-hosted older ELMNP
PDF itself has an anomalous caron in extracted text; the surname
correction is controlled by the author's homepage. Web-opened PDF
metadata and excerpts are not a full-paper reading. **Zero fresh
primary research pages** or new mathematical proof checks are claimed.

## Scoped usage ledger

The frozen ledger searches tracked TeX citation commands for eight
inspected keys and separately marks membership in the active closure.
This is not an exhaustive bibliography deduplication audit.

| Inspected keys | Active citation commands per key | Publication identity and handling |
| --- | ---: | --- |
| ELMNP05 | 2 | Corrected name; key and edition retained. |
| FN80 | 3 | Corrected name and generated display label; key retained. |
| Nad89 / Nad90 | 4 / 4 | Same 1990 Annals paper, 132(3), 549--596. Both appear in four active commands, including an existing proof, and in four commands in a frozen historical chapter. They are not separate 1989/1990 publications. |
| Temkin2015Berkovich / Temkin12Introduction | 5 / 3 | Same 2015 LNM 2119 chapter, 3--66, DOI 10.1007/978-3-319-11029-5_1. Both occur in active proof packets; one first-key occurrence is a protected input. The old key name does not establish a distinct 2012 controlling edition. |
| LXZ22 / LiuXuZhuang22ThresholdsPublished | 11 / 2 | Same 2022 Annals article, 196(2), 507--566, DOI 10.4007/annals.2022.196.2.2. The newer key retains its exact sixty-page published reading and locators. |

The three duplicate-publication pairs remain in this checkpoint.
Consolidation must retain the edition notes and source locators and
preserve historical proof artifacts. No proof citation, statement,
mathematical formula or publication year is changed here.

## Build and rendered review

The final book has **4,407 pages**, 20,480,920 bytes, SHA-256
`02ffc50905d301d4e878fea0d603e298e4e3d8faeba36af089ca31133ae5d107`.
A full page-by-page extracted-text comparison against the immutable
tau release identifies exactly five changed physical pages:
`717, 721, 846, 4397, 4398`. The full TOC and pagination are unchanged.

All five changed pages and all three FN80 chapter citations were
read and displayed, together with the entire final bibliography:
**22 pages in eleven sheets**, `717, 721, 846, 4389--4407`.
Complete selected text and original rendered page images were reviewed.
This is not a fresh reading of the whole book. The corrected names
are contiguous and legible; the three FN80 citations have resolving
bibliography targets. Publication and version notes remain intact.

References pass for 425 active inputs and 12,874 unique labels.
The bibliography has 686 unique keys and 391 cited entries, with no
BibTeX warnings. Compilation has zero TeX errors, package/PDF warnings,
missing glyphs, overfull boxes, undefined references or rerun requests.
The existing 954 underfull boxes are unchanged. Index checking accepts
767 entries, rejects none, and verifies all 420 numeric destinations.
All 47,116 internal links and 22,010 named destinations resolve;
171 URL links, 2,570 TOC entries and all six parts are present.

All 425 active TeX inputs and 108 protected inputs retain their exact
bytes. All citation commands, the other bibliography, 75 preceding
frozen manifests and 130 preceding exports are byte-preserved. The
canonical inventory remains 42 atoms in twelve families with tiers
`0/3/7/15/17`. The inactive entropy candidate remains OPEN. The native
catalogue source and its 86-page PDF are unchanged; its editor is
neither reopened nor freshly compiled here.

Baseline record SHA-256:
`4f7bef46fb574bae01e7f83ef17c4c1f5f26519f942047c1e81c2946d29f004e`.
Final gate SHA-256:
`ae1ef007b1fd8dbeb43723605ee4da70f0aea04c372384c6e93898aa8c2348c0`.
Reading record SHA-256:
`1b2b7951eb1ba822d12445a81aee49503dc4193ef33903119940cfd025c58943`.
Citation-ledger SHA-256:
`75c01709d89d9e35465c102a4c004e6610f116bdaa291cec128aa7771b20998a`.

The release manifest and artifact record pin the full book, a 22-page
review PDF and a source archive with all active inputs and both
bibliographies. Every source-archive member is byte-compared with its
saved source. No isolated archive compilation is claimed. Prior
frozen releases remain available without overwrite.

Routine main/work synchronization is already authorized. Publish this
checkpoint on work and keep the existing draft PR. No original theorem,
model call, production receipt, canonical solved status or general
Siu/closure repair is added. The author's homepage also points to
[2309.16722v1](https://arxiv.org/abs/2309.16722v1), an ELMNP erratum.
Only its metadata and abstract are checked so far. Next read that
correction and the actual antecedent before evaluating any effect on
the book's asymptotic-base-locus and restricted-volume discussion.
