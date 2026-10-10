# Bergman extremal and constant-scalar-curvature rigidity

Date: 7 October 2026. Baseline and fetched `origin/work`:
`edbb03f9f4e8b1f01fd82057f5d2b8195648e35e`; fetched `origin/main`:
`00957114db21b627e97369563032ceda9cea09c7`.

Peter Ebenfelt and Soumya Ganguly, *Rigidity of Extremal and cscK
Bergman Metrics on Pseudoconvex Domains*, exact arXiv:2610.04590v1,
submitted 3 October 2026 at 15:26:18 UTC, prove an equivalence of
extremal, constant-scalar-curvature and Kähler--Einstein Bergman metrics
under a local strongly pseudoconvex boundary hypothesis. This review
reads all 37 main pages and 64 selected dependency pages: 101 distinct
exact-source/page pairs in 53 displayed sheets. Two PDFs are fully read;
six files have partial selections. Twenty-four scoped records and twenty
elementary diagnostics retain the dimension-two cancellation, the separate
MA and harmonic indicial roots, ACH metric scaling and the noncompact
Carleman cutoff order.

The main argument is unrefuted by this scoped review. It is an attributed
source audit, not a complete external proof-chain certificate or an original
new theorem. Auxiliary presentation and normalization issues in adjacent
sources below do not constitute counterexamples to the EG main theorem.
The local boundary hypothesis does not itself identify the domain with a
ball, solve the compact cscK problem, or repair general non-Archimedean
Siu decomposition or envelope closure.

## Exact acquired sources and actual reading

Cached files and immutable acquisition/reading records are under
`source_material/Ebenfelt_Ganguly_Bergman_rigidity_sources_20261007/`.

| Exact file | Actual PDF pages read | PDF SHA-256 |
| --- | --- | --- |
| Ebenfelt--Ganguly 2610.04590v1, 37 pages | All 1--37 | `6dea6b1b295ede00830cb21ee5a07906fa353f2b70914c622c73a1b887a0062d` |
| Hsiao--Huang--Li 2604.05542v2, 41 pages | 1, 5--6, 11--16, 35--38; thirteen pages | `18ec1ce2719d089a76621438da71a64c75726dcedb304b3738d74a317f895cd0` |
| Li--Liu 2609.24853v1, 11 pages | All 1--11 | `af43e080b5974589d4c7501b08e28ba3e99f4eefdce3c0727b1e1d8513e3cecb` |
| Graham, Compositio Mathematica 64(2) (1987), 133--155; 24 returned pages including wrapper | 1--4, 9--14, 20--23; fourteen pages | `e7ab83ad3042eeef98997495ded00f59f42c3212df6033e4718e03b935e8b827` |
| Guillarmou--Sá Barreto, author-linked 38-page ACH copy | 1, 3--5, 7--9; seven pages | `df6cd7b02e8d53c2001c4318a972cc399e21dbeb9a94088b6395642c75d1e5ef` |
| Lee--Melrose, Acta Mathematica 148 (1982), 159--192; scanned 34-page journal copy | 1--3, 31--34; seven pages | `8c8e1d34ac9fc73891e52bcb98a19732e7e245cf792ad2cc7f9a4de69cade6ad` |
| Huang--Xiao, J. reine angew. Math. 770 (2021), 183--203; published 21-page copy, DOI 10.1515/crelle-2020-0012 | 1, 5--7; four pages | `306f34b340a93c4fb766bf38c67e814ad7780d8c15692b99e24655d7c60e2cc7` |
| Hörmander IV, 2009 Classics reprint of the 1994 edition; scanned 362-page public-library copy, DOI 10.1007/978-3-642-00136-9 | 1, 3--5, 246--249; eight pages | `426f2c303f61e3bffbd22048b59f30775f0be76184b19e3751174bdf02baebbb` |

HHL v2 was submitted 1 September 2026 at 07:39:50 UTC; its v1 was
submitted 7 April. Li--Liu v1 was submitted 21 September 2026 at
16:30:04 UTC. The latter's rendered April 2026 draft date is not an
arXiv priority date. Graham actual page 2 is printed 133; Lee--Melrose
actual page 1 is printed 159; Huang--Xiao actual page 6 is printed 188;
Hörmander actual page 247 is printed 237. These offsets are not interchanged.
The GSB author file is not asserted identical to the 55-page published
edition. The acquired Hörmander later reprint is distinct from EG's cited
1985 edition. OCR for the scanned Hörmander selection is controlled by
the displayed images; its preserved acquisition text file remains empty.

The 2024 Ebenfelt--Xiao chapter, DOI 10.1007/978-3-031-69702-9_6,
was not acquired as a PDF: the publisher attempt returned HTML. Its
MA variation and local curvature/logarithmic-flatness inputs therefore
remain externally attributed. The separate Graham *Scalar boundary
invariants and the Bergman kernel* chapter, original Christoffers
invariant calculation, original Fefferman/kernel parametrix inputs,
Hörmander III Theorem 18.6.8, Biquard--Herzlich half-ball estimate and
the unpublished EG--Sha--Xiao finite-type input were not read here.
No partial selection is promoted to a complete proof-chain reading.

Main reading SHA-256:
`47f8188359959f22e6365076a2cdbb75b277b3a3a3b7a1d660e11f1fe7c78fee`.
Dependency reading SHA-256:
`5c0185b3bd5539474adfa2ac25791f48e91c620eb5b772e5a74ed4b18e8cf51d`.

## Scoped records

**BS01 — Version and reading scope.** All 37 EG and 11 Li--Liu pages
were actually read as complete selected text with matching images.
The other six PDFs retain exact partial page scopes. Every reading flag
was set only after display and an actual reading note. Acquisition,
metadata inspection and text scouting are not proof reading.

**BS02 — The bounded-domain hypothesis.** EG Theorems 1.1--1.3 use
a bounded connected pseudoconvex domain in C^n, n>=2, with at least
one C-infinity strongly pseudoconvex boundary point. No globally smooth
or globally strongly pseudoconvex boundary is assumed. The scalar is
-n and Ricci form is minus the Bergman form in the source convention.

**BS03 — Local-to-global and unbounded scope.** EG Theorem 1.5 starts
with an extremal or cscK Bergman metric on a collar at such a point,
including possibly unbounded domains. Its conclusion concerns the
kernel-positive locus. The proof clears denominators before real-analytic
propagation on the connected ambient domain; it does not assume the
kernel-positive locus is connected or that the kernel is positive everywhere.

**BS04 — Kernel and metric normalization.** For Euclidean-volume
diagonal kernel K, g=partial bar-partial log K, G=det g and B=G/K,
the ball constant is Cn=(n+1)^n*pi^n/n!. Set v=K^(-1/(n+1)) and
u=log(B/Cn). With positive-inside defining functions and the augmented
determinant J, B=(n+1)^n J(v), and Scal+n=-Delta_complex u.
The complex Laplacian is g^{alpha bar beta}u_(alpha bar beta).

**BS05 — Book conventions.** The book uses dd^c=i partial bar-partial/(2pi).
Taking omega_book=dd^c log K=omega_source/(2pi) gives book Ricci
=-omega_book and scalar=-n. The determinant constant for this rescaled
coefficient matrix gains (2pi)^(-n). Using the unscaled source form
with the book Ricci convention instead gives scalar -n/(2pi).

**BS06 — Boundary orders.** The full polyhomogeneous expansion gives
u and Scal+n of order r^2 for n>=3, but order r^4 in dimension two.
Tangential inverse metric has order r; normal and mixed terms have
order r^2. A finite Hölder estimate alone does not give the all-orders
expansion or flatness required later.

**BS07 — The two-dimensional cancellation.** EG uses c0=2/pi^2,
phi=c0+r^3 a and psi=-3c0 eta1+O(r), with the separate unread
Graham kernel-invariant chapter as a cited input. For
v=Cr+r^4 alpha+r^4 beta log r+O_phg(r^7), beta=C eta1+O(r),
J(v)=C^3 J(r)-4C^2 beta r^3 J(r)+O_phg(r^4).
Read Graham equation (4.11), actual 22/printed 153, gives
J(r)=1+4 eta1 r^3+O(r^4). The r^3 terms cancel. This is stronger
than discarding the logarithmic term as an unspecified error.

**BS08 — Extremal reduction.** The source extremal vector field is the
(1,0) gradient of scalar curvature. Its boundary coefficients tend to
zero. Local boundary uniqueness for holomorphic functions on transverse
one-variable slices and the identity theorem make it vanish. This
reduces extremal to cscK before the harmonic u argument.

**BS09 — Smooth localization and MA resonance.** HHL Theorem 1.1 and
the selected localization proof support a smooth diagonal kernel error.
It induces delta v=r^(n+2)a plus higher terms. The MA leading variation
for adding a r^m has coefficient m(n+2-m), which vanishes at m=n+2.
The logarithmic variation adds the constant n+2-2m. Localization must
be passed through this critical cancellation rather than differentiated
as an arbitrary same-order remainder.

**BS10 — Adjacent HHL adjoint and defining-function wording.** The
stated adjoint in HHL (2.18) has correct cutoff order, but the explanation
(2.19) swaps factors relative to it and pairs on G without specifying
restriction for a general Omega input. An exact noncommuting fixture
records the distinction. Actual page 36 uses a positive-inside defining
function while calling it strongly plurisubharmonic. On the ball this
has the opposite complex tangential Levi sign. These passages are not
silently imported as general operator or sign identities.

**BS11 — Adjacent Laplacian coefficients.** HHL actual page 37, (7.16),
prints 2a(n-2); Li--Liu actual page 6, (2.13), prints m(n-m)a.
With the standard complex Bergman Laplacian and positive-inside r,
the unit-ball coefficients are respectively 2a(2-n)/(n+1) and
m(m-n)a/(n+1). The nonzero cases actually used by their vanishing
inductions remain nonzero. This normalization diagnostic is not a
counterexample to the claimed conclusions.

**BS12 — Adjacent Li--Liu conventions.** Its (2.6) prints MA coefficient
m(m-n-2), opposite to BS09 in the inserted positive-r convention;
the critical exponent remains n+2. Actual page 7 defines
theta=i(partial r-bar-partial r)/2 but writes the horizontal metric
with -dtheta(X,JY). For the standard complex structure on the ball,
dtheta(X,JX)>0, so that literal sign is negative. No reversed complex
structure convention was located. The introduction's flatness shorthand
for J rather than J-Cn is corrected in its actual Theorem 2.1.

**BS13 — Harmonic resonance is different.** Under cscK, Delta u=0.
The boundary indicial polynomial is lambda(lambda-n)/(n+1), with
simple roots zero and n. Full polyhomogeneity eliminates positive
leading exponents other than n and rules out nonconstant leading log
polynomials there. Once u has order strictly beyond n, all coefficients
vanish. The harmonic root n is not the MA critical perturbation n+2.

**BS14 — Higher-dimensional spherical boundary step.** For n>=3,
u=O(r^n)=o(r^2) removes the weight-two curvature term and gives local
sphericity via the source's attributed EX2024 input. Read Huang--Xiao
Proposition 2.1, actual 6/printed 188, states the corresponding
phi coefficient as cn||A22^0||^2 with cn nonzero; its original
Christoffers proof was not read. In n=2 that weight-two coefficient
vanishes identically, so it cannot provide this higher-dimensional step.

**BS15 — Actual MA expansion and its limits.** Read Lee--Melrose
Theorem 8.18, actual 32/printed 190 and following proof, supplies
the actual Cheng--Yau all-orders conormal/log expansion. Earlier
weighted/conormal results remain dependencies. Its negative defining
function phi0 and potential -log(-phi0) must be translated before
using EG's positive-inside r. Lee--Melrose's earlier Theorem 6.21
is unrelated to BJ22 Theorem 6.21.

**BS16 — Flat obstruction does not imply sphere.** Graham Theorem 2.11
locates the free smooth boundary coefficient; Proposition 2.16 makes
all MA logarithmic coefficients flat when the first obstruction vanishes.
Proposition 4.14, actual 22--23/printed 153--154, constructs nonspherical
real-analytic strongly pseudoconvex examples with zero obstruction.
Thus the actual EG sphere step precedes the needed enhanced flatness;
it cannot be replaced by an unsupported converse for MA logarithms.

**BS17 — From formal cancellation to flat harmonic u.** In n>=3,
local sphericity and localized smooth MA/kernel inputs raise u to order
n+2, past the harmonic root. In n=2 the already established r^4
order is past root two. The all-orders harmonic expansion then makes
u and the required scaled derivatives flat. This is not deduced solely
from a finite boundary regularity class.

**BS18 — Real ACH normalization.** Set x=sqrt(r), g_R=2Re(g), and
ghat=g_R/[2(n+1)]. EG uses unit radial ds with s=-log(geodesic x).
GSB's metric and Li--Liu's 2g_R/(n+1) are four times ghat. The
Theta fields are x partial_x, xY and x^2 T; horizontal and Reeb metric
growth are e^(2s) and e^(4s), and volume grows as e^(2ns).

**BS19 — The geodesic defining function.** Read GSB Lemma 3.1,
author-copy actual page 8, solves the local smooth noncharacteristic
eikonal equation with prescribed boundary conformal factor. Its local
H1 normalization is enough here; scattering hypotheses H2--H4 are
not imported. For g=4d rho^2/rho^2+h/rho^2 the dual of d rho/rho
is (rho/4)partial_rho. The author's subsequent rho partial_rho shorthand
omits this factor, while the stated 4X_rho/rho flow is consistent.

**BS20 — The bent end and uniform charts.** EG chooses a compact
boundary patch and a smooth positive delta tending to zero at its edge,
phi=-log delta, then s>S+phi and tau=s-S-phi. The inequality
e^(-s)<=e^(-S)delta controls differentiated lateral cutoffs. Scaled
horizontal/Reeb charts may cross the artificial end boundary while
remaining in the ambient collar. Uniform coefficient bounds and the
complete tau-level geometry are necessary for globalization.

**BS21 — The local Carleman input.** The read Hörmander reprint
Theorem 28.2.3, actual 247/printed 237, assumes the full-symbol
inequality (28.2.6), not only positivity on the characteristic set.
EG obtains it using the positive tangential Hessian near that set and
|p|^2 domination away. For the conjugated Laplacian the bracket is
4gamma[Hess tau(xi#,xi#)+gamma^2 Hess tau(N,N)]. The theorem's
compact local estimate and unread Fefferman--Phong input must not be
described as an already global noncompact end theorem.

**BS22 — Globalization and cutoff order.** Uniform quadratic partition
and commutator absorption give gamma^3||e^(gamma tau)w||^2 plus
gamma||e^(gamma tau)grad w||^2 bounded by the conjugated equation.
Lateral cutoffs chi(delta/epsilon) have uniformly controlled scaled
derivatives. Flatness and volume growth give tail integrability only
after choosing a decay order M>n+gamma. Remove the radial cutoff
R to infinity at fixed gamma, then send gamma to infinity; reversing
these limits is unsupported. This forces u=0 on a collar.

**BS23 — Analytic continuation and nondegeneracy.** On the initial
collar B=Cn. Clearing denominators gives det H=Cn K^(2n+1) for
H=K K_(alpha bar beta)-K_alpha K_bar beta. Both sides are real analytic
on the ambient connected domain. On {K>0}, Gram/Cauchy--Schwarz
gives semipositive g and the positive determinant gives strict positivity.
EG Proposition 7.1 also cites an unpublished finite-D'Angelo-type
preprint for a local nondegeneracy assertion; that wider finite-type
input has not been independently certified here.

**BS24 — Integration and research boundary.** Appendix H can explain
this boundary-normalized rigidity and its two distinct indicial scales;
Chapter 68 can link it as a noncompact analytic comparison. The stronger
global smoothly bounded strongly pseudoconvex ball theorem requires
the separately attributed Huang--Xiao/global uniformization hypotheses.
We do not infer compact cscK implies KE, non-Archimedean analytic
continuation, general Siu decomposition or envelope closure. Weakly
pseudoconvex/finite-type extensions and weaker asymptotic hypotheses
are source-scoped literature directions, not solved canonical atoms.

## Diagnostics and preservation

All twenty exact elementary checks BC01--BC20 pass. Their immutable
v2 record SHA-256 is
`239fd0ffbb96ac6d2ed065e49426d6a9c719322dde94966d89fd77c00d6cc28a`.
They check unit-ball Hessians, determinants and indicial coefficients,
logarithmic cancellation, conventions, the Poisson-bracket factor,
tail integrability, denominator powers and cutoff/adjoint order.
They supplement source reading rather than certify the complete theorem.

An initial helper transposed its holomorphic/antiholomorphic matrix-inverse
rank-one term. Its exact inverse assertion failed; the original helper and
failure record remain preserved, and a new v2 helper uses the consistent
row/column orientation. This was a diagnostic-helper error, not a source
error. Acquisition text and PDF bytes were not overwritten.

This source-only checkpoint preserves all 425 active inputs, 108 protected
inputs, both bibliographies, the checked 4,469-page book/index, 100 preceding
frozen manifests and 172 prior exports. The native catalogue source/PDF
and open editor are unchanged. No original theorem, independent model
call, production receipt, Xean run, canonical-status change or BJ22 repair
is added. GitHub publication uses an ordinary work-branch push and the
existing draft PR. The next step is attributed integration followed by
compilation and fresh matching rendered-page reading.
