# Chapter 53 completion audit

Date: 1 October 2026

Base: local Chapter 52 commit `63710e7`.

Scope: `parts/part5/ch53_transcendental_metrics.tex`, under the sequential
quality programme. Chapter 54 is next; the whole-book goal continues.
Independent Chapter 72 research remains paused.

## Mathematical and expository review

The full source, assertions, examples, conventions and source note were
reviewed. Thirteen formal assertions have proofs or exact analytic imports:
four lemmas, four propositions, two corollaries and three theorems.
All 23 reusable environments have labels. There are 62 labels, including
seven section labels.

The principal repairs are:

- The transition construction explicitly allows a semipositive difference
  of Kähler forms, including zero. The reversed perturbation order,
  countable cofinal sequence and componentwise order are stated. A new
  corollary proves that evaluation at one component reflects order and
  determines a compatible family uniquely; it does not assert that an
  arbitrary curve at one perturbation extends.
- Smooth change of representative translates a potential and then takes
  its normalized ideal envelope. The current and multiplier ideals are
  unchanged by the translation, but the envelope need not be pointwise
  unchanged. Inverse and cocycle properties use uniqueness of the
  normalized representative, with the exact background-change source.
- Transition mass equality requires ideal-goodness of positive initial and
  interior ideal-model levels. Its source and background independence are
  explicit. General ideal envelopes can raise raw mass. The mixed-term
  expansion supplies both monotonicity and an exact equality criterion
  for two comparable perturbations.
- Positive-volume recovery now proves decrease and noncollapse of the
  normalized approximants, identifies the recovered mass by the exact
  variable-background model-mass theorem, propagates its positive lower
  bound by concavity, proves ideal-model normalization and constructs the
  initial level and closed endpoint. Positive-mass continuity of divisorial
  Lelong numbers then recovers every original component. A liminf estimate
  alone is no longer used as identification of the recovered mass.
- The homogeneous construction is proved to have positive mass at every
  perturbation, even when its unperturbed input has zero mass. Its limiting
  ideal envelope is identified by a divisorial sandwich. Model-mass
  continuity applies at zero as well as positive volume; divisorial
  continuity is invoked only with positive mass.
- The boundary-class example uses the homogeneous-volume theorem and
  the nonbig-class mass bound. The product-of-curves example explicitly
  identifies its perturbed level as zero. The rigid negative-curve example
  chooses a Hermitian metric with the specified curvature and preserves
  the squared-norm Lelong--Poincaré convention.
- Birational invariance has an explicit imported extension to smooth
  semipositive forms with positive top integral. That index category is
  not directed. Pullback and descent are constructed and their composites
  checked through the extended components. Volume preservation uses a
  mass comparison and smooth perturbation polynomial, without claiming
  cofinality of degenerate pullback forms among Kähler forms.
- The opening distinguishes zero volume of the unperturbed class or metric
  from positive mass of each perturbed component. Legacy inline delimiters
  have been converted, and the operations preprint version is identified.

## Direct source interfaces

Three primary PDFs were read at the relevant statements and proofs.
Twenty-one source pages were rendered and inspected.

| Source and checked version | Principal interfaces | Physical pages inspected |
| --- | --- | --- |
| Xia, supplied snapshot dated 18 July 2026, matching the historical source pin | Proposition 3.1.12; Corollary 6.1.3 and Proposition 6.1.3; Theorem 7.1.1 and Example 7.1.2; Proposition 9.3.2; Section 13.1, especially Lemma 13.1.2, Proposition 13.1.5 and Corollary 13.1.1 | 112--113, 215, 249--250, 253--254, 320, 438--443 |
| Xia, arXiv 2312.17150 v3, 22 October 2024 | Lemmas 2.10, 3.8 and 3.10; Section 4.8 | 6, 9--11, 20 |
| Darvas--Xia--Zhang, published CMH 100 (2025), 269--322, DOI 10.4171/cmh/586 | Definition 3.3, the inverse limit, transition cocycle and component order | 22--23 |

PDF SHA-256 values, in that order:

1. `c816eea5f06822021fa8dd75b70f82724ee47e6dcd6830729f5ecc109296b706`
2. `773eea71af9f1fff112bf5fcab2b9046b81467df2e37165ee1da3949ff74c6d9`
3. `467778ff37b893681482e43b4d8f1d717e947a34fe61026b2e6bc418e4a1f70e`

The Xia lecture and DXZ PDFs are reused from the ignored Chapter 51 and 52
caches. The operations v3 PDF was obtained from its versioned arXiv PDF URL
and is in `source_material/ch53_audit_20261001`. The subsequently published
2025 operations chapter has a separate bibliography entry; numbered v3
locators are not presented as newly checked published-page locators.

## Calculation and verification

The symbolic and exact-rational supplement passes 2,172 checks. It checks
mixed-mass expansion and deficit inequalities in dimensions 1--8,
concavity's determinant lower bound for positive diagonal currents, and
the product-of-curves and divisor-supported zero-volume normalizations.
These checks support the algebraic computations; analytic envelope and
extension theorems remain the explicitly cited source inputs.

Scoped reviews before and after rendering find no unlabelled reusable
environments, proofless assertions, duplicate labels, nesting errors,
legacy inline delimiters, double-dollar displays or TODO/FIXME/TBD markers.
The legacy writing-audit executable is unavailable; its warning counts
are not claimed.

The reference checker passes: 425 inputs, 12,059 labels, no missing inputs,
duplicate labels, dangling references or structural defects. All six
checker regression tests pass. The inventory remains 42 atoms in twelve
environments, tiers T1=0, T2=3, T3=7, T4=15, T5=17. Post-render scoped and
reference checks and `git diff --check` pass.

The full `latexmk -pdf -interaction=nonstopmode -halt-on-error book.tex`
build succeeds with workspace-local TeX Live 2025. The final PDF has
4,114 pages and 19,209,755 bytes, SHA-256
`55f5e6d99974ce8144800bf9f3f45bc253b4751bd8ac408e49ff252babeed7e7`.
Final chapter source SHA-256:
`2daafa04b32ef1001de6afab55d2e8483c1f83d201d4a0f92a2e8da25387da2d`.
There are no unresolved references or citations, missing glyphs, rerun
requests or fatal errors. Chapter 53 has zero overfull boxes and zero
LaTeX/package warnings. Nineteen overfull boxes elsewhere and thirteen
duplicate PDF destinations in Chapter 70 remain recorded.

All fourteen final chapter pages, physical 3049--3062 (printed 2981--2994),
were inspected at detail size. Physical 3062 is intentionally blank.
Both adjoining pages 3048 and 3063 were inspected. The earlier render
was scanned throughout and its recovery, homogeneous-volume and
birational proof pages inspected at detail size. No reviewed clipping,
overlap, bad glyph, formula overflow or hierarchy defect remains.

This is a direct editorial/source audit, not an independent-agent verifier
verdict. Generated PDFs are local review artifacts. Frozen releases,
dated checksum ledgers and research atoms are unchanged. Verified work
remains local pending explicit remote-push approval.
