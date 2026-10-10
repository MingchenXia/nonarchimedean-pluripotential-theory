# Orlicz conditions and boundedness in a fixed Kähler class

This known-result checkpoint follows `7f39cc1`. It adds Chapter 68.10
and provenance L.40. The original toric class-perturbation candidate
remains a separate research-only OPEN submission. It is not an active
TeX input and neither its statement/proof digest nor production status
changes here.

## Primary sources and actual reading scope

Guedj–Lu, *Uniform estimates: from Yau to Kolodziej*,
[arXiv:2502.02313v2](https://arxiv.org/abs/2502.02313v2), revised
18 February 2025, has fourteen pages, 224,173 bytes and SHA-256
`58e551b3ca057c8eb921503f1b2b9e274dee9ae8efb484f8252736427ce104c2`.
Its complete 807-line extraction and all actual pages were read and
displayed in the earlier phase recorded before `4851791`. This import
reuses that complete reading; it does not claim a fresh acquisition or
second full reading. The official arXiv history was checked on 5 October
2026 and still lists v2 as the latest revision. The author's publication
pages identify the note as a preprint; no journal pagination is assigned.

The admitted inputs are the known compact Kähler Theorem A on actual
page 2, Definition 1.5/Example 1.6 on page 4, Lemma 2.2 on pages 6–7,
the Section 2.1 Step 3 calculation on page 7, and the Section 2.2 local
radial example and one-variable calculation on pages 8–9. The import
does not include all statements of the paper, particularly the fully
nonlinear Theorem B's dependence on its equation normalizer.

Kołodziej's original *The complex Monge–Ampère equation*,
Acta Mathematica 180 (1998), 69–117, DOI
[10.1007/BF02392879](https://doi.org/10.1007/BF02392879), was acquired
from the institutional archive of its publisher PDF. The actual 49-page
file has 2,107,638 bytes and SHA-256
`0fbdda7a0d029bb3c2c772bb955817ef02d459b4854fcd56e9f9a70712ca264e`.
Eight selected actual pages 5–6, 10–11 and 20–23 were freshly displayed,
corresponding to printed 73–74, 78–79 and 88–91. The text was read
selectively at the differential convention, condition (A), Orlicz
calculation and theorem/example anchors. No full paper rereading is
claimed. A preliminary unviewed selection used actual page 4 for a
convention printed on page 73; the corrected selection uses actual page 5.
The archive download filename does not change the publication year.

Load-bearing original anchors are condition (A) at actual 10–11/printed
78–79, Theorem 2.4.2 at actual 20/printed 88, doubling condition (2.5.3)
at actual 22/printed 90, and Theorem 2.5.2 with Example 1 at actual
23/printed 91. The last example already contains the logarithmic
order n and double-logarithmic order greater than n. It supplies
continuous solvability, rather than continuity being inferred from
an oscillation estimate.

## Category, mass and scaled Orlicz integrability

The ambient manifold is connected, smooth, compact and Kähler, with
fixed Kähler theta, positive volume V and fixed smooth positive probability
nu. The density F has integral one and the operator is raw MA/V.
The general a priori bound is stated for smooth positive F and a smooth
solution. Its constants include the fixed geometry, weight and an upper
bound on the Luxembourg norm. No collapsing-class, arbitrary-complex-
structure or general Hermitian uniformity is asserted.

Condition (K) is an asymptotic tail condition, not an expression involving
logarithms at zero. A convex admissible extension on a bounded interval
and a positive w(1) define the Luxembourg threshold. Membership allows
an integrable scaled weight; it does not imply an unscaled integral for
an arbitrary Young function. Choosing R greater than the norm bound gives
the auxiliary weight 1+w(t/R), integral at most 1+w(1), and its
normalization constant between (1+w(1))^(-1) and one. A shifted tail
function preserves reciprocal integrability after this rescaling.

## Known reduction with the intermediate factors retained

The explicit smooth calculation uses an auxiliary normalized potential
v with MA(v)=c weighted(F) nu and uniform Skoda control of exp(-alpha v)
in L^p for a fixed p>n. If weighted(t)>=kappa t log(t)^n
widehat_h(loglog t)^n, choose 0<a<1 and
D=(a c kappa)^(-1/n). The displayed convex derivative is
chi'(t)=D/[(B-alpha t) widehat_h(log(B-alpha t))], t<=0.
It increases, is at most one for large B, and has finite integral
(D/alpha) integral_logB^infinity 1/widehat_h. It produces a bounded
theta-psh competitor chi(v).

On the high-density set, log F>=-alpha v+B and monotonicity of chi'
give a MA(chi(v))>=F nu. On the complementary set retain
F<=exp(B) exp(-alpha v). Thus Lemma 2.2 applies with its coefficient
a<1, bounded competitor and a probability-normalized L^p remainder.
Its strictly positive auxiliary density supplies the smooth minimum
contradiction. The proposed lower barrier is strictly above the potential
at that minimum; the reversed printed inequality is not copied.

The source page 7's exp(-v) replacement is not copied either. The
change b(x)=-chi((B-exp x)/alpha) has derivative exp(x) chi'/alpha,
and chi'(0) uses widehat_h(log B). Those factors are explicitly retained.
These are identified elementary calculations inside the known estimate,
not a counterexample to the estimate or a new independently verified
result. The displayed proof calculation assumes smooth admissible weights;
the known general a priori assertion is cited with its original scope.

## Explicit moment, original theorem and radial boundary

For double-logarithmic power q>n, the integrated convex weight used in
the book has tail t(log t)^n(loglog t)^q. Its condition (K) function is
comparable to s^(q/n). The original condition (A) uses H(y) comparable
to (log y)^q and the integral dy/[y H(y)^(1/n)]. Setting s=log y
identifies the same requirement q>n. The explicit logarithmic weight
satisfies the original large-argument doubling condition. The probability
density conversion to theta^n/V multiplies it by a bounded positive
smooth function, whose integrability is preserved by doubling. This
clears the mass and reference-volume premises for continuous solvability
of the nonnegative rough-density equation by the original theorem.

In a Kähler class V_theta=0, so known boundedness supplies the finite
M0 used in the earlier modulus discussion. A merely big class still
retains that bound as a hypothesis. The August general uniform-estimate
argument is not imported through this classical calculation.

The local radial example concerns n>=2 and a smooth convex increasing
profile with zero limiting slope. Its unbounded triple-logarithmic profile
has finite moment at double-logarithmic order n-1. The stronger radial
calculation explicitly assumes log(e+F) comparable to the negative radial
logarithm, or equivalently the source's displayed one-variable weighted
integral. Its integration-by-parts boundary term is justified by the
weighted tail, and Hölder's second integral converges for q>n-1.
No compact gluing assertion is needed for this local test. The source's
Question 2.5 is described as a question of the checked 2025 version;
no general optimality answer or current canonical retirement is claimed.

Guedj–Lu use ddc_s=2 ddc_b, while the original Kołodziej convention is
ddc_s=4 pi ddc_b, checked on actual page 5/printed 73. Multiply the
compact class form by the respective factor and keep the potential:
raw top measures scale equally, leaving the normalized density unchanged.
Numerical geometry constants are not identified across conventions.

The canonical 42-problem inventory, general Siu/closure assertions,
non-Archimedean entropy comparisons, spectral laws and A2–A4 convergence
retain their scopes. This checkpoint adds known results and explicit
direct formal consequences, with zero independent model calls and no
extension of historical verification receipts.

## Final source and release checks

The final v3 build has 4,325 pages, 20,108,384 bytes and SHA-256
`9a22bb1115bbcaebdf96510585741b23f474949cdff337f5b8a8a2873d977c63`.
The first two builds exposed an overwide aligned weight definition;
three separate rows with their left edges aligned repair the layout
without changing the mathematics. Final TeX errors, LaTeX/package and
pdfTeX warnings, missing characters, unresolved references/citations,
rerun requests and overfull boxes are all zero. The 954 underfull
boxes are recorded, not represented as a zero-diagnostic build.

The closure still has 425 active TeX files, 423 unchanged. All 46
pre-existing formal blocks and proofs in the two edited TeX files
are byte-preserved; no formal environment is added. The twelve new
labels bring the unique total to 12,703. All prior bibliography bytes
are preserved; one new Guedj–Lu key brings the total to 624 and the
cited total to 329. The six manual equation tags are unique. The
reference checker and canonical inventory checker pass; all forty-two
complete status rows, 108 protected inputs and thirty-eight prior
frozen manifests retain their bytes. The original toric candidate
and its companion record retain their exact digests and OPEN status.

The index has 743 accepted entries, no rejected entries or warnings,
742 hyperpage groups and 404 valid distinct numeric destinations.
All 21,689 named destinations, 46,639 internal links, 163 URL links
and 2,508 contents entries have valid applicable PDF targets. All six
part roots remain. Twenty-four matching final-book pages were freshly
displayed, including the title, current contents, every new Chapter 68
and L.40 page with transitions, index boundaries, new and original
bibliography anchors and the last pages. This is a scoped release
review; it is not another complete reading of the 4,325-page book.

Fresh Orlicz-named full PDF, 24-page review PDF and complete source
archive are recorded separately, preserving prior releases. The
archive includes both toric research files explicitly as nonactive
research notes. No isolated archive compilation is claimed. The
86-page catalogue source/PDF and native editor remain unchanged.
