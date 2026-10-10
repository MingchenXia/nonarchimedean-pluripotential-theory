# Index spelling and preserved source bindings

Date: 6 October 2026 UTC. Baseline work commit:
`e1cfce7c8f490df573984f189c0f5196b3bb0c86`; main:
`00957114db21b627e97369563032ceda9cea09c7`.

The generated index now consistently uses **Monge–Ampère** and
**Stokes’ formula**. The previously split Monge–Ampère equation headings
are merged, including skeletal factorization; both analytic and
polyhedral Stokes entries share a heading. Mathematical source files,
formal statements, proofs, source locators and canonical statuses are
unchanged.

## Build change

`editorial/tools/make_book_index.py` processes a derived copy of
`book.idx` before invoking the existing MakeIndex style. The latexmk
configuration calls this wrapper. It changes 25 unaccented Monge–Ampère
keys and one Stokes key, leaving all **773 ordered page arguments**
and the original raw index bytes intact. A generated JSON ledger records
each key rewrite and both input hashes. The derived index and ledger
are ignored build products. Python 3 is already used by the book's
editorial tools; no new package or index style is required.

Some index commands occur inside formal mathematical environments.
Normalizing the generated keys preserves **all 425 active TeX inputs**
and their historical source bindings. All **108 protected inputs**,
both bibliography files, **80 prior frozen manifests** and **139 prior
exports** remain byte-identical. The 42-atom inventory remains in tiers
0/3/7/15/17. The native catalogue source/PDF and open editor are unchanged;
neither is recompiled or reopened. No primary-source reading, original
result, model call or verifier receipt is claimed.

## Matching build and page review

The final book has **4,417 pages**, 20,523,384 bytes, SHA-256
`6659448ecfb0a315839c2d0f60efd6d6169da98a642ece56088f0b3ab320eac2`.
Compilation has no TeX errors, LaTeX/package/pdfTeX warnings, missing
characters, overfull boxes, unresolved references/citations or rerun
requests. The existing underfull-box count remains 954. References pass
with 12,894 unique labels and no missing inputs, duplicate labels or
dangling references. Bibliography checks retain 400 cited entries among
695 keys, with no BibTeX warnings. The three previously recorded
duplicate-publication pairs are not edited in this checkpoint.

The index accepts 773 entries with no rejections or warnings. Its
1,026 generated lines have 772 page groups and 422 distinct valid numeric
destinations. PDF navigation retains 22,056 named destinations, 47,183
internal links, 171 URL links, 2,574 contents entries and six parts, with
no invalid internal links.

All **12 matching physical pages in six sheets** were read as complete
selected text and displayed as page images:

    69, 4389–4399.

This covers the contents entry, the entire ten-page index and the first
bibliography page. Accents, merged headings, subentries, columns and
transitions are readable. Comparing extracted text on **all 4,417
physical pages** against the preceding dynamics export finds differences
only on pages **4390, 4391, 4392, 4394–4398**. The other 4,409 page texts
are byte-identical. This is a full page-text comparison, not a new
whole-book reading or visual comparison. The existing Hodge–Poincare and
Kolodziej index spellings lie outside the two variants corrected here.

Frozen release gate SHA-256:
`9bb57049ab9d7644d30a51a62dfd1235f7712a7cbc660e48c0343ab1c131e18b`.
Frozen reading:
`f663b7266a5884b02b6824c4960bb236093ec68719001d4927ac38ba3bd3e122`.
All six actual-view flags are frozen in manifest
`6434ece3bfc07a7fe165c7a3281be8153b8fd23442b336d5d7f657d787242f93`.

Export the full book, matching twelve-page review and active source ZIP
under `/workspace/book-completion-drafts/research-integration/`. The
archive includes the new wrapper and build configuration; each member
is compared byte-for-byte to the current source, including all active
TeX inputs and both bibliographies. No fresh isolated archive build is
claimed. Fetch main and work, publish normally to work and update the
existing draft PR under standing authorization. Continue with actual
reading of the acquired K3 and Favre–Gong papers, checking author updates
and exact editions before any integration.
