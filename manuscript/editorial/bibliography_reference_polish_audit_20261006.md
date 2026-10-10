# Reference precision, proper-name titles and duplicate citations

Date: 6 October 2026. Baseline work:
`829fe7b75c8e56c40fd5639647f6e383652ffa83`.
Baseline main: `00957114db21b627e97369563032ceda9cea09c7`.

Four Chapter 51 citation commands now cite Nad90 once instead of
both Nad89 and Nad90. The records describe the same 1990 Annals
paper; no theorem or proof input is replaced. Six title fields protect
proper names from BibTeX case conversion. The existing bibliography
database retains all 709 keys and distinct source/version notes.

## Identity and final citation handling

The [official Nadel article record](https://annals.math.princeton.edu/1990/132-3/p04)
confirms Alan Michael Nadel, Annals 132(3), 549–596 (1990),
DOI 10.2307/1971429. Both database entries have that identity;
the apparent 1989 date occurs only in the old key name. The four
active commands occur in the coherence proof, interface register and
source/history notes. Their final display is Nad90. The unused Nad89
record remains available for the frozen historical chapter source.

The six title fields are Dem93, BB22MTPublished,
GuedjTrusiani25LocalPublished, Liu18VolumeV5,
DruelGuenanciaPaun24Published and FMSV24ChowSeries.
Only brace protection changes: Monge–Ampère, Moser–Trudinger,
Kähler–Einstein, Fano and Hilbert–Poincaré retain their case.
All other fields, title wording, years and versions retain baseline bytes.
The [exact GL25 arXiv metadata](https://arxiv.org/abs/2502.02313v2)
use the transliteration Kolodziej in that title, which is preserved.

The scoped six-key usage ledger gives the final active command counts:

| Key | Active commands | Handling |
| --- | ---: | --- |
| Nad89 | 0 | Database alias retained for history. |
| Nad90 | 4 | One published reference per command. |
| Temkin2015Berkovich | 5 | Active historical proof binding preserved. |
| Temkin12Introduction | 3 | Active historical proof binding preserved. |
| LXZ22 | 11 | Original citations and metadata preserved. |
| LiuXuZhuang22ThresholdsPublished | 2 | Published layout and locators preserved. |

Both Temkin keys occur in active historical proof packets. Their
identical published metadata do not authorize rewriting those packets
or rebinding historical verification receipts. This checkpoint retains
both rendered entries and both original database records.

The [official LXZ publication record](https://annals.math.princeton.edu/2022/196-2/p02)
confirms the common published article identity. Nevertheless, actual
reading of Chapter 50 found an explicit February 2022 preprint binding
for Theorem 1.6; the newer key controls a checked sixty-page published
layout and different explicit locators in Chapter 68 and Appendix L.
A candidate merge into a newly asserted published entry was reversed
before publication. All original LXZ citation commands and both
database records retain baseline bytes. Resolving the older entry's
preprint-versus-published metadata is separate unfinished work; this
checkpoint does not certify that the numbering is interchangeable.

The superseded candidate had four actually read/displayed pages in
two sheets. Its successful candidate gates and partial-reading record
remain separately frozen. Those views do not count as matching-final
v2 reading. Metadata checks, search results and publication abstracts
are not claimed as fresh research-proof or primary-page audits.

## Source and historical preservation

Only Chapter 51 changes among the 425 active TeX inputs. Its exact
baseline-to-final transform is the four Nadel citation edits. All
83 formal blocks and 31 proof blocks retain their text and order after
that exact citation map; literal byte preservation of the whole edited
chapter is not claimed. All 424 other active inputs retain their bytes.
Both bibliography key sets retain all 709 keys; only six title fields
change. No bibliography record is deleted or new source edition added.

All 108 protected inputs, 3,665 tracked historical packet/dossier files,
87 preceding frozen manifests, 151 preceding exports and native
catalogue source/PDF retain their bytes. The open native editor is
unchanged. The 42-atom canonical inventory, twelve Chapter 72
environments and tiers `(0,3,7,15,17)` are unchanged. There is no
original theorem, model call, new production receipt, historical
receipt scope extension or general BJ22 Siu/envelope closure repair.

## Required build, navigation and matching-final reading

Required `scripts/validate-manuscript.sh` completes with exit zero,
including references, canonical inventory, six existing checker tests
and the full book build. There are 12,930 unique labels, 414 cited
entries and 709 bibliography keys. Final compilation has zero TeX,
package/pdfTeX warning, missing character, overfull box, unresolved
reference/citation or rerun request. The 954 underfull boxes equal baseline.

All generated index products and its wrapper/configuration retain
baseline bytes. The index accepts 781 entries, rejects none and has
no warning; its 425 distinct numeric destinations resolve. Navigation
verifies 22,132 named destinations, 47,280 internal links, 171 URL
links, 2,583 contents entries and six parts with no invalid link or
destination. The complete contents and pagination are unchanged.

The final book has 4,432 pages, 20,592,807 bytes, SHA-256
`3c6b6034f95f2dea150dcfd9feae4f426bb22e436efb3c6c9f648e1c2f54d94a`.
Comparing extracted text on every physical page with the preceding
immutable local-maximality export finds fifteen changed page texts:
`3072, 3114, 3119, 3121, 4413, 4419, 4422, 4424, 4426--4432`.
The other 4,417 page texts are identical. This comparison is not a
new whole-book rereading.

All 25 selected matching final pages were read as complete text and
actually displayed in thirteen sheet views: the four changed chapter
pages, physical 4412 at the index transition, and every bibliography
page 4413–4432. Titles, final Nadel display, retained version notes
and link targets are checked. The full-page image selection and
actually-viewed flags are preserved in the immutable release manifest.

Final release gate SHA-256:
`8776dbcedd9be5acde73a9aff502c294c33ce67d469cd4aee1f770adc7e57a7e`.
Final reading record SHA-256:
`77b2706b63d89b374afb6bfe56d7c87d15a91028f2dfa95ef38814165e49cc00`.
Twenty-five-page review PDF SHA-256:
`37b1637a235a53a9458ddc675158b0b262b544c8e71e228d45d6af45d25f491c`.

The current source closure contains 427 TeX/bibliography hashes.
Immutable book/review/source exports retain prior releases. Every
archive member is byte-compared with its current source; no fresh
isolated archive compilation is claimed. Fetch main and work, preserve
incoming author changes, push normally and update the existing draft PR
under standing GitHub authorization. Continue the acquired exact v1
Hessian/null-Lagrangian paper and its actual comparison hypotheses.
