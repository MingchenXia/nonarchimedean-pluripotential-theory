# Qin curvature-rank source review, 9 October 2026

The exact controlling source is Xiangsen Qin, *Dolbeault Cohomology Growth
under Curvature Rank Bounds*, arXiv:2610.09295v1, submitted 7 October 2026.
All 39 physical pages were read as complete selected text with twenty
individually displayed matching renders and chronological notes. No blank
verso was omitted. This is a full reading of this PDF, not a recursive
certification of its references or a new complete reading of the book.

## Exact imported signature

Let X be a compact complex manifold of complex dimension n, L a
holomorphic line bundle with a smooth Hermitian metric h, and E a fixed
holomorphic vector bundle. Let r be the maximum complex rank of the
smooth real curvature form. Neither positivity, constant rank, a regular
kernel foliation, nor a Kähler hypothesis is imposed in Theorem A.
For every fixed epsilon>0, it states h^q(X,L^p tensor E)=O_epsilon(p^(r+epsilon))
for 0<=q<=n. End degrees q=0,n have O(p^r). For 1<=r<n and each fixed
integer k>=1, its displayed quantitative bound is
p^(r+2(n-r)/(2k+5)) times a fixed power of 1+log p, with constants depending
on k and the fixed geometric data. These constants are not controlled
as k tends to infinity. The fixed data and epsilon are chosen before p.

Question 11.3, on physical page 34, leaves sharp O(p^r) growth in the
intermediate degrees on general n>=3 compact complex manifolds open.
Remark 11.4 explains why the MMZ arbitrary-prescribed-divergent-factor
formulation is equivalent to a sharp bound for fixed data. It is stronger
than the collection of fixed positive exponent-loss bounds. Neither
k=k(p) nor a sharp estimate follows from Theorem A's quantitative display.

The endpoints, the surface conclusion, and the class-C geometric rank
comparison are explicitly separated from the new all-degree estimate in
the source. Appendix A gives classical Serre–Siegel section growth;
Appendix B gives another proof of the geometric comparison; Appendix C
derives it in class C from earlier volume/contact-set theory. They are
not reported here as new discoveries or resolutions of book problems.

## Proof audit and boundaries

Sections 3–9 were read in full. The operator argument factors restriction
identities modulo bounded maximal-Dolbeault homotopies. Finite-rank
approximation occurs only after global augmentation, collation and
harmonic projection. One holomorphic restriction factor is kept per
summand in the telescoping identity; ranks add, rather than multiplying
all cover cardinalities. The terminal strictly psh auxiliary weights
are bounded on buffered domains, and actual metric weights are comparable
up to bounded errors. No global uniform spectral gap is inferred.

Fekete interpolation replaces indefinite finite-rank polynomial kernels
by bounded holomorphic factors without controlling inverses of small
curvature eigenvalues. Invertibility is used qualitatively to identify
Schur kernels. Regular-rank centers are dense; the proof does not assume
uniform constant-rank neighborhoods. Auxiliary rescaling tends to zero
only for rank identities. Remainder estimates are at the actual scale.

Complex-cellular maps need not be immersive or injective. The recursive
construction retains old variables and adds independent tube parameters.
The true metric is pulled back from those old variables. At the next
step, the difference of model weights is placed in an accumulated scalar
error, not divided by the next t^2 scale or declared to retain curvature
rank. This resolves the provisional concern about treating nonimmersive
parametrizations as invertible coordinate charts.

For t=p^(-1/(2k+5)), the counted factor is
t^(-2n)(p t^2)^r=p^(r+2(n-r)/(2k+5)). Each k is fixed. A power of log p
can be absorbed into an additional fixed positive exponent loss, with
constants depending on that choice. Endpoints instead use classical
section growth and fixed-bundle reductions; top degree uses Serre
duality with the fixed canonical twist and the dual metric of equal rank.

Load-bearing external dependencies include Berndtsson 1996 Theorem A
(graph extension), Binyamini–Novikov 2019 Definitions 7–8 and Theorem 8,
Definition 23/Proposition 25 and section 2.2.3 (complex cells/two-cover/
complexity), and Hörmander 1965 (terminal barpartial estimates). Their
original PDFs were not read in this review. Standard principalization,
proper-image/algebraicity, Riemann–Roch, Serre duality and volume/contact
results are also imported. No recursive original-proof certification or
independent-model production receipt is claimed. No fatal defect in the
main finite-jet/localization argument was identified in this scoped audit;
that finding is not a general correctness guarantee.

## Literal source diagnostics

Equation (2.2), physical page 4, prints the curvature as barpartial partial
phi while printing the connection as minus partial phi and the real form
as i partial barpartial phi. The connection gives
R=-barpartial partial phi=partial barpartial phi, so the printed R term
has the wrong sign. The source's real-form convention, coordinate matrix,
tensor/dual laws and Appendix B consistently use the latter positive
convention. The Gaussian phi=|z|^2 detects the sign. Rank is unchanged by
a global sign; positivity is not. Any book discussion will define its
own consistent Chern form rather than copy the incorrect connection line.
The endpoint display in Theorem A also has a literal malformed p>=) typo.
These local printing diagnostics are not counterexamples to Theorem A.

The source extraction emitted a font-type/embedded-font mismatch warning.
The actual rendered symbols and lines were readable in all twenty views.
The initial acquisition helper failed after downloading the correct PDF
because it expected mixed-case identity text, while title/author are
uppercase. Its executed bytes and zero-credit failure record are frozen;
a fresh v2 preparation recovered the same version and hash. Preparations
retain false actual-view flags. Separate receipts carry reading credit.

The product example P^r times Y has binomial(p+r,r) sections and shows
sharp exponent r. The blowup example has f=uv in one chart and f=s in
another: curvature rank drops at the isolated critical point and the
two kernel limits disagree. Its h^0=p+1 is not a new all-degree application.
Appendix C distinguishes complete-series envelopes in big projective
classes from possibly different envelopes without bigness. Curvature
rank of a chosen smooth metric, Kodaira dimension, class numerical
dimension, and current-level non-pluripolar dimension must remain distinct.

## Next integration and preserved status

Consider a short attributed discussion at the end of Chapter 55:
smooth curvature rank bounds section growth, while the sharper intermediate
cohomology question remains separate from lower-dimensional partial bodies.
Use Theorem A as an expressly imported recent-preprint estimate and explain
the fixed-epsilon quantifier. Do not reproduce a new general proof or add
a formal open-problem atom on the basis of this audit.

The active 4,669-page book, bibliographies and native catalogue/editor are
unchanged in this source checkpoint. Canonical inventory remains 42 atoms
in twelve formal problems, tiers (0,3,7,15,17). General BJ22 homogeneous
Siu/envelopes remain OPEN, LPWZ density UNVERIFIED, and the user's warning
about Theorem 6.21 remains binding. This complex smooth-curvature theorem
supplies no non-Archimedean critical homogeneous Siu repair. Last complete
ordered book reading remains 4 October; subsequent reads are scoped.

The authored archive is suitable for the authorized GitHub evidence upload.
The controlling external PDF and matching text/images are preserved in a
separate cloud evidence archive. Every archive member is byte-verified.
Preparation, archiving, commit and upload each add zero reading credit.

Finalization bookkeeping: a v1 preflight incorrectly excluded every editorial
TeX path when counting protected inputs. It failed after writing the twelve
calibrations and before aggregating reading or exporting. The executed v1
helper and calibration bytes remain frozen. Fresh v2 uses the existing
minimal-build archive to identify all 425 selected TeX inputs, including
selected editorial dependencies; it checks and reuses the unchanged
calibrations. No source observation or book byte changed for this repair.
