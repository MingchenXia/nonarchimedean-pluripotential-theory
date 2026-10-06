# Determinantal capacity and relative bounds

Date: 6 October 2026. Baseline work commit
`d993f336dcf0ae5cbff8fa5f4c0d2f76edb41152`; explicitly fetched
`origin/main` remains `00957114db21b627e97369563032ceda9cea09c7`.

## Scope and reading route

Chapter 68 now places a source-checked discussion of determinant subsolutions,
relative big-class bounds and polynomial determinant capacity immediately
after its fixed-Kähler-class Orlicz discussion. The transition explains how a
matrix increment bound feeds an auxiliary Monge–Ampère comparison. A balanced
partial-trace example makes the distinction between positivity and uniform
determinant ellipticity concrete. Appendix L records editions, proof inputs,
regularity boundaries and the older viscosity comparison correction.

The material is identified as known results and a worked known example.
There are no new formal theorem/proposition/lemma/corollary environments,
original mathematical claims, independent model calls or new verifier receipts.
The requested `gpt-6.1-sol xhigh` original-result gate is not invoked by this
known-result import. Earlier receipts are not extended by this checkpoint.

## Controlling source and actual reading

Hao Fang, Biao Ma and Jinyang Wu, *Determinantal capacity and L-infinity-Estimates*,
arXiv:2609.24078v1, submitted 21 September 2026 at 04:04:33 UTC. Official
metadata identifies Analysis of PDEs as the primary subject. The acquired PDF
has 41 actual pages, 626105 bytes, SHA-256
`e8c89c7add6efe239ffaf1cbf3c6297918cc583d52e5b6cb6656c10ca6ddf8d4`.
Its extracted text has SHA-256
`ab8645133edd897747cbb61afbf0b3bc305d29b94fec9da37bd544367402586d`.
All 2254 newline-indexed rows were read in fourteen complete output ranges;
the 2294 `splitlines()` fragments are a different counting convention because
form feeds split internally. All 41 actual pages were displayed in 21 sheets,
including references and the ABP appendix. The complete reading record is
`source_material/determinantal_capacity_20261006/full_reading_v1_20261006.json`,
SHA-256 `b6b92752f98aa50c021cd5e0aa4ac344fcbebbf6b7d3ca1497a004d9c072a0ea`.
Historical acquisition/admission fields remain historical; they are not rewritten
to suggest that a source reading was an independent mathematical verification.

Load-bearing locators in this version:

- Definitions 2.1, 2.2 and 2.4, pages 5–6: admissible fibers, the separate
  trace bound, and determinant increment ellipticity.
- Definitions 2.7 and 2.9–2.11, pages 7–9: determinant subsolutions,
  upper-test interpretation, stability and paired local regularization.
- Proposition 3.2, pages 9–10: reduction for supersolutions; smooth admissible
  supersolutions need only a continuous viscosity determinant subsolution.
- Theorem 3.4, page 10, proof pages 12–16: relative estimate, auxiliary mass,
  comparison, weighted moment and finite-extinction iteration.
- Proposition 3.5 and Lemma 3.6, page 11: big-class auxiliary solutions,
  ample-locus continuity and uniform normalized exponential integrability.
- Lemmas 3.7–3.9, pages 12–14: local comparison and strict buffer.
- Theorem 3.15, pages 17–18: normalized smooth solutions and singular references.
- Corollary 3.19, page 19; Remark 3.20, page 20: semipositive families with
  a volume lower bound, and the unimported sharper Orlicz refinement.
- Definitions 4.4–4.5, page 21; Proposition 4.10, page 22; Corollary 4.14,
  pages 23–24: recursive conic condition, top part and reference increments.
- Theorems 5.12, 5.15 and 5.17, pages 29–32; Example 5.19, page 33:
  subspace rank, uniform scalar capacity, equivalence and partial traces.

## Selected dependencies and the comparison correction

Sixty-five selected actual pages from nine source files were displayed in
39 image sheets or individual-page views. The record is
`source_material/determinantal_dependencies_20261006/selected_reading_v1_20261006.json`,
SHA-256 `3edf3848d45cafb16b38da04217803f2e15b481edc613409af92b8545c8d940a`.
Together with the main paper these give 106 freshly displayed source pages.
This is a selected dependency review, not a blanket audit of all references.

Fang–Ma, arXiv:2604.27755v2, revised 18 May 2026, was inspected on
actual pages 1, 40, 43–46 and 50. Version 3, revised 29 September 2026,
was inspected on 1, 22–23, 42, 45–48, 52 and 66. Page 66 was a tangential
search hit and is not used for the import. The recursive criterion,
directional-derivative closure and Theorem 11.2 agree on the relevant inspected
pages of the two versions. The capacity paper predates v3. Theorem 11.2's
internal reference to “Theorem 5.21” actually refers to Lemma 5.21;
the ledger records the actual type. No full reading of either long version
is claimed. Brändén–Huh's published Annals 192 (2020), 821–891 PDF was
inspected on actual pages 1 and 20–24, including Definition 2.18,
Lemmas 2.20–2.22 and Theorem 2.23's support proof. The PDF formula has
`c^{|alpha|}` in the generalized Rayleigh definition; flattened extraction
does not authenticate that exponent.

Berman–Demailly's author PDF was checked on pages 1–7, including
Theorem 1.4 and its proof. Boucksom's published 2004 PDF was checked
on actual 1 and 14–16, including Theorem 3.17 on printed 59–60.
The existing BEGZ arXiv v2 was reused by exact bytes and checked on
1–3, 31–33 and 40–43. Its Theorem 3.1 is on actual 32, with outline on
33; page 31 is preparatory material. Theorem 4.1 and estimate proof are on
40–43. This is not the separately published edition. The published DDGHKZ
2014 PDF was reused by exact bytes and checked on actual 1, 4 and 23–25:
Theorem D is local Hölder continuity in the ample locus of an arbitrary
big class, under its probability and Lp hypotheses.

The original EGZ 2011 author-hosted published PDF was checked on actual
1, 5–7 and 11–16. Proposition 1.5 gives the bounded psh/pluripotential–viscosity
equivalence for nonnegative density. Proposition 2.10, actual 14,
printed 1072, requires strictly positive density. Its old global comparison
proof is not reused as a proof for a general big class. The six-page
arXiv:1610.03087v1 erratum was read and displayed in full. Official submission
is 7 October 2016, while the PDF internally displays 16 July 2018; these
metadata are kept distinct. Lemma 1.2 requires strict local psh positivity
and allows nonnegative continuous densities. Its Theorem 1.1 compares on
the ample locus, extending globally under the displayed continuity condition.
The main capacity proof's analytic-singularity perturbation provides the strict
buffer at the relevant maximum, after localization to the ample locus.
The GZ 2017 book was not acquired and its exact numbered locators are not
claimed independently cleared. No defect in the capacity theorem is inferred
from this unacquired reference; neither is it silently marked verified.

## Mathematical interfaces and boundaries

The determinant density is `exp(gamma)/V_chi`, where `V_chi` is big-class
volume. It need not be a probability density and is not the earlier relative
entropy. Auxiliary right-hand sides have the exact raw mass `V_chi`.
Strict exponents `q>n`, or `q>np'`, remain explicit. The qualitative
`Lp0`, `p0>1`, hypothesis supplies each auxiliary solution; its norm does
not become an unstated quantitative datum. Extended continuity, the proper
closed singular set, divergence of U on that set, and the relative L1 input
are retained. The separate infinite-density extension in Theorem 3.14 is not
imported. Weak supersolutions require paired local regularizability;
regularizing only the potential does not supply it.

The semipositive-family consequence uses real continuous gamma_j,
continuous U_j with supremum zero, a fixed upper background bound, positive
volume lower bound and uniform entropy/L1 data. It omits a pointwise positive
lower bound for the forms, but gives no Hessian estimate and no zero-volume
limit. The separate trace lower bound supplies the smooth solution's Green
L1 control. It is not automatic for every polynomial operator.

Conic Gårding positivity and recursive derivative nesting are explicit;
positivity on positive matrices alone is insufficient. The first-derived
region allows some nonadmissible references. Homogeneous capacity positivity
is equivalent to every complex subspace rank inequality. Uniformity over
unitary bases uses a positive coefficient in the nth power and continuity
on the compact unitary group. Pointwise positivity of an infimum alone is
not presented as sufficient. The partial-trace example has capacity one
exactly when `a/m=b/k`; determinant-one anisotropic scaling gives zero
capacity otherwise. It is a computation of the cited known example.
Subspace slope semistability is distinct from variety K-stability, and this
matrix capacity is distinct from pluripotential capacity of subsets.

The main paper's J-equation, dHYM and inverse-sigma applications were read
but not imported: their separate existence/barrier dependencies are outside
this checkpoint. No endpoint Orlicz refinement, arbitrary Hermitian extension,
singular-space transfer, original priority claim, Siu division or general
non-Archimedean closure repair is asserted. The 42 canonical statuses and
the separate open toric entropy candidate remain unchanged.

## Build, layout and preservation

The first 4372-page build completed without compiler or reference errors.
One determinant increment equivalence was 41.88219pt too wide. Its matrix
quantifiers were moved to the adjacent prose, preserving the mathematical
signature. First-build log, source gate, draft and diagnostic image are
retained; the corrected second build and final-page review control release.
Final build, navigation, page review, export and exact byte checks are recorded
in the accompanying integration manifest and artifact ledger.

The corrected build has 4,372 pages, with zero compiler errors, overfull
boxes, missing glyphs, unresolved references, package/PDF warnings or pending
reruns. Its 954 nonfatal underfull diagnostics match the preceding build.
The 367 used bibliography entries, 763 accepted index entries, 21,876 named
destinations and 46,928 internal links pass their checks. All 41 selected
final pages were actually displayed and reread: both changed contents
pages, the new discussion and its transitions, provenance and all index
and bibliography pages. An oversized image batch was redisplayed in smaller
batches before being counted. No fresh whole-book rereading is claimed.

Only Chapter 68 and Appendix L change among the 425 active TeX inputs;
the other 423 and all 108 protected M–N inputs remain byte-identical.
All 46 existing formal assertion/proof blocks in the edited files remain
byte-identical. The addition gives twelve semantic labels, six distinct
equation tags and three index entries. Four version-specific bibliography
entries bring used citations to 367 and bibliography keys to 662.
All 49 earlier manifests (47 integration and two source-only reviews)
and 97 earlier external exports remain byte-identical. No old helper or
frozen manifest is rerun or replaced. The native open-problem catalogue
source/PDF retain exact bytes, its editor remains open, and no fresh
catalogue compilation or review is claimed.

GitHub synchronization uses the author's standing authorization, including
the latest instruction to handle routine GitHub permissions without waiting.
The existing draft PR is updated after the checked work-branch push;
no merge or force push is part of this checkpoint.
