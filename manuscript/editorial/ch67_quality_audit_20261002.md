# Chapter 67 completion audit

Date: 2 October 2026.

Base: local Chapter 66 commit 71c174d.

Scope: parts/part6/ch67_functoriality_trace.tex, under the sequential
quality programme. The whole-book completion goal continues; independent
Chapter 72 research remains paused. Historical releases, receipts and
checksum ledgers are preserved.

## Mathematical and expository review

The entire chapter was read. All eleven formal assertions were checked
with their proofs or exact imported interfaces. The chapter has thirty
labelled reusable environments, eleven proof environments and 86 labels.
All eight examples and ten remarks were reviewed. The introduction fixes
connected smooth complex spaces, the trace domain and raw Monge--Ampere
mass. Ordinary complex norm weights have curvature ddc(2h) in the book's
squared-potential convention. Sections and source notes have semantic labels.

The repairs and checks include the following:

- Birational Lelong numbers use unscaled ord_E and the Siu coefficient;
  no boundedness of the remaining singular potential is asserted. The
  multiplier transformation formula for arbitrary quasi-psh weights now
  uses the Jacobian L2 identity, normal Hartogs extension and proper local
  integrability. It no longer assumes a log resolution of arbitrary
  singularities. Nonnegative infinite integrals are allowed. Nonpluripolar
  pullback is proved off the exceptional analytic pair; a smooth trace-mass
  bound proves that its pushforward gives zero mass on the exceptional image.
- The new blowup example computes the Jacobian, Lelong coefficient and
  multiplier ideal, including integer jumping thresholds. Full-mass
  invariance fixes the minimal-potential volume interface. The former
  no-inverse remark was mathematically false for a pulled-back class:
  positive currents in that class do descend, by constancy on connected
  compact fibres and bounded local psh extension. Its historical label is
  preserved, with a corrected title and proof. Currents in arbitrary
  upstairs classes, such as the exceptional divisor class, remain different.
- Finite pushforward keeps generic degree, raw versus probability mass,
  and the continuous semipositive domain. The non-Archimedean model proof
  uses the whole special-fibre cycle of the normalized graph, with scheme
  multiplicities and residue degrees. The branched P1 example computes
  the pulled-back density, angular degree and raw mass, with no branch atoms.
- The determinant norm uses base-field dimension of the local Artin
  algebra, including its residue degree. Its frame-change and zero-section
  formulas are proved by a maximal-ideal filtration. Continuity for an
  arbitrary continuous weight is proved through proper fibre neighborhoods
  and finite-flat spectral clusters with constant total local rank. The
  radicial and coalescing-fibre examples distinguish geometric points,
  nilpotent length, residue degree, continuous frames and singular sections.
  Nonflat descent uses the strict transform over a projective flattening,
  not the entire fibre product.
- The historical base-change unit ledger is retained. A new explicit
  valuation-function calculation writes D_m phi(v)=m phi(v/m), as in
  published BHJ Section 6.3. It distinguishes that action from pointwise
  multiplication of a fixed function and from a fixed-unit valued-field
  pullback. The affine P1 calculation tests the valuation argument as
  well as the metric value.
- Literal restriction, image ideals and analytic trace remain distinct.
  The analytic-restriction proposition now states the rational-coefficient
  hypothesis used by the cited source; the constant approximation then
  meets every quasi-equisingular condition. Real-coefficient terminology
  in Chapter 51 alone is not used to widen this interface. The zero-Lelong
  pole example computes all multiplier integrals and uses the explicit
  compact P1 construction for a global trace example. Pointwise limits of
  restricted truncations and d_S-limits of their classes are distinguished
  from the separate increasing-family mass counterexample.
- The product proof preserves a uniform Kähler lower bound during
  quasi-equisingular approximation. It proves smooth-projection multiplier
  pullback by Fubini, fixes the generic trace-domain point, and identifies
  the restricted d_S-limit as P_alpha[psi]_I by the exact positive-mass
  approximation theorem. Equality with the input P-class is asserted only
  for I-good data. The rational logarithmic product example computes
  nonpluripolar mass 2(1-a), although the class has self-intersection 2.
- The retraction proof first compares currents with a smooth positive
  form, then tests its tangent vectors and obtains a uniform lower bound
  by compactness. It never evaluates a singular current pointwise. The
  domain-saturation proof treats Y=X separately, then divisors and smooth
  higher-codimension centres. Its I-to-P output uses the supplied trace
  uniqueness theorem. Unibranch trace and the general fixed-class Dirichlet
  problem remain explicit boundaries. The final checklist references each
  precise theorem rather than adding a broader functoriality claim.

House inline mathematics is used throughout. There are no double-dollar
displays, unfinished markers, duplicate labels, unlabelled reusable
environments or environment-balance errors. The converted finite-descent
boundary remark retains its historical ex: label to preserve references.

## Direct primary-source interfaces

Four PDFs and forty selected physical pages were read in text and visually
inspected. These are direct interface checks, not independent verification
of every imported deep theorem.

| Source and version | Interfaces checked | Physical PDF pages |
| --- | --- | --- |
| BEGZ, arXiv:0812.3674v2, 9 September 2010; cover date 1 December 2009 | Nonpluripolar construction and locality; zero pluripolar mass; Remark 1.7 modification rule; Proposition 1.12 minimal pullback and the following connected-fibre descent assertion | 1, 5--8, 13 |
| Xia, supplied Singularities in global pluripotential theory snapshot updated 18 July 2026 | Rational analytic singularities and quasi-equisingular definition; Corollary 7.1.2 positive-mass approximation; birational QE pullback; complete trace independence and P-class uniqueness interfaces; Proposition 8.2.1 I-input/P-output, Proposition 8.2.2 decreasing nets, increasing counterexample and restricted-image-ideal inclusion | 1, 48--50, 254--255, 274--283 |
| Darvas--Xia, accepted arXiv:2403.08259v2, 13 March 2026 | Rational analytic definition and uniform positivity; trace construction, mass floor and approximation independence; Example 3.7 analytic restriction; Lemmas 3.9--3.10 and the distinct increasing counterexample | 1, 7--14, 16 |
| BHJ17, cached published AIF 67 (2017), 743--841 PDF | Equation (6.1), base-change action in Section 6.3 equation (6.2), positivity, normalized model MA, Gauss units, degree-one homogeneity of E/J and comparison conventions | 1, 59--60, 64--68 |

The supplied Xia source gives the general background-independent P-class
interface. The accepted trace article is not treated alone as proving all
of that stronger interface. The current BEGZ proof check uses its dated
preprint; no fresh publisher-PDF verification is claimed. The historical
product audit and convention audit were consulted on their relevant chapter
scopes. Superseded solver-dossier material is not a new verification receipt.
No disputed BHJ19 result is used.

Source SHA-256 values (cached files are not staged):

- BEGZ v2: `43097be8459edfd948929fade34367fa7bbd0fe691d9cba1a4f27a11181214cd`.
- Xia supplied snapshot: `c816eea5f06822021fa8dd75b70f82724ee47e6dcd6830729f5ecc109296b706`.
- Darvas--Xia v2: `5d6f43d96be101f6aa1a3ddbdd92b5bc49131a0deabbf199e03111d6c0fbaa3c`.
- BHJ17 published PDF: `edfd3b1506b49cf42ae85014d731bd9d86af5ed248134397cd562fba70c6f60e`.

## Example supplement

The supplement passes 6,021 exact checks and 1,518 numerical checks in
24 families. It includes an independently computed rational Jacobian,
radial multiplier thresholds, nilpotent multiplication determinants,
radicial characteristic-p determinant identities, residue towers,
raw/probability/squared-weight conversion, base-change dilation and radial
units, product intersection-ring mass, transverse Gram positivity,
branched-cover radial and angular integrals, coalescing norms and frame
logarithms, and log-log multiplier integrals. Numerical work uses 100
decimal digits. These computations supplement the worked proofs and do not
test the general imported theorems.

## Build, render and final gates

Three changed-source full builds pass. The final PDF has 4,148 pages and
19,351,391 bytes. Main source SHA-256:
`7c18b065bd99509c075ad2a3fe7f8e4dfeb2812cb0f05d7ae28261ee75e40e0f`.
PDF SHA-256:
`7a5490a852a2328493dd256d37bd41d9fc88ab6b2c5350b1dedcf704f0703baf`.
There are no unresolved references/citations, missing glyphs, rerun requests
or fatal errors. Chapter 67 has zero overfull boxes and LaTeX/package
warnings. Eighteen inherited overfull boxes elsewhere and thirteen duplicate
PDF destinations in Chapter 70 remain recorded for the whole-book pass.

All sixteen physical chapter pages 3445--3460 (printed 3375--3390) and
adjoining physical pages 3444 and 3461 were visually inspected. All six
second-build changed images were checked. The final source-note spillover
was repaired and physical page 3460 reinspected; final pages 3454 and 3457
match the inspected second-build images byte for byte. The other fifteen
final chapter/seam images match the inspected first-build images byte for
byte at the same render resolution. No reviewed layout defect remains.

After rendering, the scoped structure/convention audit passes. Project
references pass for 425 inputs and 12,333 labels, with no missing inputs,
duplicate labels or dangling references. All six reference-checker tests
pass. The open-problem inventory remains 42 atoms in twelve environments,
tiers (0,3,7,15,17). Git diff --check and the staged whitespace gate pass.
The unavailable legacy house audit is replaced by this manual and scoped
review. This direct audit claims no new independent verifier verdict.

The final chapter/seam review PDF is
/workspace/book-completion-drafts/Chapter_67_Final3_Review_2026-10-02.pdf.
Chapter 68 is next. Work remains local pending explicit remote-push approval.
