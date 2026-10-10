# Complete weak geodesic lines: source and integration audit

Date: 5 October 2026. Baseline work commit:
`413a9208a05c6ad0e6c84b0b4fd13cb00ff27ac8`.

## Scope and reading

This checkpoint imports established complex Kähler results into Chapter 65
and records their scope in Appendix L. It does not admit an original
general theorem or an independent production-model receipt. The cloud-only
instruction and the instruction to ignore Xean remain in effect. No local
model or subscription process is started. The existing native catalogue
editor remains open; this is an unrelated book edit.

The controlling primary file is Tamás Darvas and Nicholas McCleerey,
*Lines in the space of Kähler metrics*, **Mathematische Annalen 396,
article 36 (2026)**, DOI **10.1007/s00208-026-03573-8**. Its first actual
page records publication on **15 September 2026**, receipt on 2 May,
revision on 3 July and acceptance on 28 August 2026. The publisher file
was obtained with HTTP 200, has **25 pages, 412,504 bytes**, and SHA-256
`6514e8bc5dc38b30d16204333c8d1b7a948f11ae30c34933513cabf83476ef2f`.
The returned URL includes the publisher's cookie query, but the downloaded
bytes are the actual PDF. The licence page records CC BY 4.0.

All **1,483** lines of the published extracted text were read, in
inclusive ranges 1–300, 301–600, 601–900, 901–1200 and 1201–1483,
including references. Twenty actual primary pages were inspected:
**1–6, 8, 10–11, 13–23**. They were rendered into ten two-page contact
sheets, then viewed one sheet per successful cloud `view_image` call.
An earlier four-image response was truncated; it is not counted as
inspection. No claim is made that every actual PDF page was viewed.

The arXiv metadata identifies **2507.17375v3**, revised **29 August 2026**.
The separately acquired arXiv PDF has **24 pages, 401,841 bytes**, SHA-256
`77c4f6e20dd7ea0a7d737dbd31a4fd9d9089d61521c08c027233a8087343ad4c`.
Only extracted line ranges **350–470, 668–810, 837–920, 1004–1100**
were read from its 1,266 lines. This is selected comparison, not a full
arXiv reading or an identity certificate for the two versions.

The ignored cache is `source_material/geodesic_lines_20261005/`.
Acquisition records preserve their initial false reading/import fields;
the later `reading_progress.json` records completed reading separately.
Primary web metadata and PDF-opening tool responses are saved in the
same cache. Web search snippets and author-page lists are discovery aids,
not theorem proofs. The published source controls every new book locator.

## Imported statements and exact restrictions

1. **Theorems 1.1 and 4.1, published pages 3 and 14–16.** For a compact
   complex Kähler manifold, a Kähler class and `1 <= p < infinity`,
   Legendre transform over all real time identifies weak finite-p-energy
   lines with finite-p-energy test lines of zero nonpluripolar top mass
   on the strict interior of their finite slope interval. The line's
   complexification is psh; the p=1 metric identity alone is insufficient.
   Test lines are concave and upper semicontinuous, not necessarily
   decreasing. The inverse Legendre sign is plus.
2. **Proposition 3.7, pages 13–14.** Maximal test lines correspond to
   geodesic turns, meaning both outgoing half-rays are geodesic. The
   zero-mass requirement is what yields geodesicity across all intervals.
   The singularity envelope has singularity type first and obstacle second.
3. **Remark 4.2, pages 16–17.** Endpoint zero mass is available for bounded
   test lines only when the interval has positive length. A vertical
   translation line `u_t=a+ct` has a one-point dual with mass V, so a
   universal zero-mass endpoint condition is not used.
4. **Section 1 and Theorem 4.1 proof.** Finite slope support makes every
   weak finite-p-energy line time-Lipschitz. One bounded endpoint makes
   all times bounded. Thus completeness of E^p does not make every
   bounded-to-unbounded segment extendible to an entire weak line.
5. **Corollary 5.2, pages 17–19, and Remark 1.5, page 5.** On a projective
   manifold with an ample polarization, n+1 divisor potentials with empty
   common intersection give a Lipschitz max line and a smooth log-sum
   line. Their potential difference lies between zero and log(n+1) at
   every real time. They are parallel; known weak-geodesic distance
   convexity makes their distance constant. Smoothness does not imply
   strictly positive curvature. The source's no-vector-field examples
   therefore do not discard strict positivity in the cited rigidity setting.
6. **Theorems 1.6 and 6.1, pages 5 and 21–22.** A bounded line V has a
   unique parallel bounded line from bounded a exactly when the pointwise
   equality `a = sup_tau P[hat v_tau](a)` holds. In that case these envelopes
   are its test line. The equality is not silently usc-regularized. This
   contrasts with ray transport, which permits each finite-energy base.

The book metric is the published metric divided by `V^(1/p)`. This
constant does not alter constant-speed identities, convexity, bounded
parallel distance or uniqueness. No energy-slope formula from this source
is a new import. No extension to a merely big class or to non-Archimedean
complete lines is asserted. The existing quantization assumptions A2–A4
and the separate long-time approximation boundary retain their scope.

## Literal auxiliary displays excluded from the import

The following are checks of printed formulas against their own conventions,
not independently admitted counterexamples to the published main theorems.

- **Page 8, energy definition.** The printed display lacks both the integral
  and the usual `1/(n+1)` factor. With constants `u=c`, the sum without that
  factor would be `(n+1)c`, whereas formula (13) gives slope c for a vertical
  translation ray. The book retains its already defined energy normalization
  and does not copy this definition.
- **Page 10, Theorem 2.3 proof.** The approximation decreases with j, so
  `j>k` gives `psi^(u_j) <= psi^(u_k)`. The literal displayed order in the
  Cauchy-distance sentence is reversed. It is not used as an order input.
- **Page 11, Lemma 3.2 bound.** A two-sided time bound uses the maximum
  of the absolute values of both slope endpoints. The book retains these
  absolute values; the printed maximum of the signed endpoints alone
  cannot bound both time directions.
- **Page 14, first paragraph of Proposition 3.7 proof.** The envelope
  arguments in the first sentence are reversed relative to maximality.
  The subsequent expression `P[hat u_tau](u_0)=hat u_tau` is the convention
  used in the book.
- **Page 15, equation (18).** The signed negative-time energy slope is not
  imported as a literal display.
- **Page 16, the strengthening after equation (20).** Its almost-everywhere
  mass identity need not hold at the sole slope of a pure vertical
  translation: both half-ray dual masses there equal V. The source's
  stated continuity intervals fail to cover that one point when the
  slope interval collapses. The book states the strict-interior criterion
  and treats the collapsed interval separately; it does not import this
  strengthening.
- **Page 19, alternate local-coordinate calculation.** A positive local
  metric uses the logarithm in its curvature, a max of log squared norms
  has no extra outside logarithm, and squared-norm time uses `e^(z/2)`
  for an `e^t` coefficient. The book gives the named-source smooth
  construction with its own explicit convention and does not copy the
  malformed alternate local display. The main Corollary 5.2 Legendre
  argument remains the controlling anchor.

The published Corollary 5.2 proof correctly cites Witt Nyström's
mass-monotonicity reference [55]; the selected arXiv passage uses a
different reference number [56]. The published locator controls this
import. The product example on page 20 has the expected piecewise
coefficients and is not classified as an error. The polar-Cantor
construction and the general volume-diamond equality question on page 16
are not imported as results or resolved problems.

No proof step relies on a measure being concentrated on an arbitrary
uncountable intersection of contact sets. A countable dense set of times
and pointwise convex continuity are needed if that proof mechanism is
expanded. The current book records the known correspondence rather than
presenting a new independent general proof.

## Integration and preservation

Chapter 65 adds one section with three subsections and five equations
in the existing manual sequence **65.49–65.53**. Appendix L adds one
provenance section. The
bibliography appends one published entry and preserves its old bytes as
a prefix. Existing formal environments and proofs in the changed active
TeX files are compared byte for byte against the baseline. No theorem,
proposition, lemma, corollary or proof environment is added.

The 425-file active source closure, 108 protected analytic inputs,
all 42 complete atomic inventory statuses, and the standalone 86-page
catalogue are checked against the preceding frozen checkpoint. The
catalogue source, PDF and editor are not changed or recompiled. Earlier
frozen research manifests and exported PDF/ZIP files remain immutable.
There is no Siu division or general closure repair and no new independent
production-model receipt. A fresh cloud full-book build, reference and
inventory checks, navigation and index checks, and actual book-page
inspection are recorded in the new integration manifest after completion.

Publication uses the authorized `work` branch by a normal fast-forward
update. Main is unchanged and PR #2 remains a draft. Incoming author
commits are fetched before publication and retained. The user has already
authorized ordinary GitHub permissions; no new permission question is
needed within this scope.

## Completed build and scoped actual-page review

The fresh cloud `latexmk` build completed with **4,290 pages**,
**19,959,872 bytes**, PDF SHA-256
`e23854ff079e11588a416a755db4b1a3e9ad69eb685482ce21b94df33acd6d66`.
TeX errors, LaTeX/package warnings, pdfTeX warnings, unresolved references
or citations, rerun requests and overfull boxes are all zero. The existing
**954 underfull-box diagnostics** are unchanged. There are **12,628 unique
labels**, **606 bibliography keys** and **309 cited entries**. The index
accepts **743 entries**, rejects none and has no warnings. Its 742 page
groups resolve to 404 valid numeric destinations. All **21,544 named
destinations**, **46,446 internal links**, 163 external URL links and
2,470 table-of-contents entries pass the destination checks; all six part
headings remain present.

Sixteen actual final book PDF pages were viewed individually through eight
contact sheets: **1, 59, 67, 3463–3467, 3567, 4057–4059, 4281–4283, 4290**.
This covers the cover, affected contents, complete new section and its
neighbours, the complex-distance cross-reference, complete new provenance
entry, protected Appendix M opening, new reference and final bibliography
page. Formula numbers 65.49–65.53, the all-real-time infimum, inverse plus
sign, strict-interior mass condition, collapsed interval example,
squared-norm time factor and pointwise obstacle equality were inspected.
No further active-source repair was needed after this build. This is a
scoped fresh page review, not another whole-book rereading.

The source gates preserve **423 of 425** active TeX inputs byte for byte,
all **49** pre-existing formal environments/proofs in the two changed
TeX files, every one of the **108** protected analytic inputs, old label
order, previous bibliography bytes and all **42** complete atomic status
rows. The catalogue source and PDF are byte preserved. New gate records
are `/tmp/geodesic_lines_source_gates_v1_20261005.json` and
`/tmp/geodesic_lines_release_gates_v1_20261005.json`; no previous frozen
manifest, source-closure record or exported PDF/ZIP was regenerated.
