# Chapter 60: radial limits and multiplier-ideal regularization

Date: 23 September 2026.
Baseline: `dba6a5b4d624fc1fd9208250d50d3733fe7129c4`.
Scope: the beginning of Section 60.5 through the radial-limit theorem
and the new logarithmic-cutoff example in `parts/part5/ch60_mp_psh.tex`.
All preceding text and all text from the converse/maximal-ray paragraph
onward retain their baseline bytes. This is a reconstruction of an
established assertion using explicitly cited analytic inputs; no research
atom is retired.

## Proof and normalization

The growth correction and squared-norm conventions are preserved.
Joint pullback-omega positivity, removable extension, the signed number
nu_v(U), independence of the growth constant, central multiplicity b_E,
and the affine ray U_s=c s are checked before the construction.

The new flag-expansion lemma proves the finite expansion of an invariant
coherent ideal containing tau^N. Modulo tau^N, Fourier projectors for
the Nth roots of unity separate the N coefficient ideals. Coherence and
the increasing inclusions follow from direct summands and multiplication
by tau. The ideal is the unit ideal off the central fibre and therefore
extends to the compactified product. N=1 is included. This also explains
why rotation invariance suffices for the global flag construction.

The regularized-flag lemma uses V<=0 and V>=k log|tau|^2 on a product
disc. Direct integrability gives tau^(mk) in I(mV), so the associated
model functions are defined on the entire spectrum. The exact singularity
type of W_m is (1/m) log|I(mV)|^2+O(1), locally at each fixed m; no
uniform bounded remainder as m varies is asserted. Smooth local weight
changes preserve the ideal, Bergman generators generate it on smaller
balls, and the gluing formula preserves that ideal singularity type.
This is not a claim that I(mW_m)=I(mV) or that weak convergence preserves
multiplier ideals.

Demailly's curvature operator is i partial-barpartial/pi and his weight
is exp(-2m phi). Taking phi=V/2 and W_m twice the source approximant
gives the book's coefficient 1/m with dd^c=i partial-barpartial/(2pi).
The local/glued regularization has curvature error -epsilon_m Omega,
where Omega=p1^*omega+dd^c|tau|^2. This includes a disc direction and
cannot be absorbed solely by multiplying p1^*omega. Adding the smooth
term epsilon_m |tau|^2 removes the disc part without changing the ideal
type. The resulting potential is lambda p1^*omega-psh for all sufficiently
large m, for each fixed lambda>1. The threshold can depend on the weight,
lambda and smaller product disc. The ideals and model functions are
independent of lambda. No equivariance of the glued weights is needed
for the relative positivity argument.

On a smooth snc resolution I(mV) O_Y=O_Y(-F_m), subtracting [F_m]/m
leaves a positive current with locally bounded potentials in
lambda alpha_Y-[F_m]/m near the central fibre. Positivity across the
divisor follows by bounded psh extension. Bounded potentials can be
restricted to each smooth central component. Their Bergman regularizations
have unit multiplier ideals and hence are smooth, with arbitrarily small
negative curvature error; this proves nefness on the components. Other
fibres have class lambda alpha. This uses the chapter's previously checked
componentwise criterion for relative nefness. Dimension zero is also
covered, with vacuous positivity conditions on point components.

For V^(k)=max(V,k log|tau|^2), subadditivity gives decreasing dyadic
model functions h_(k,2^ell) in [-k,0]. The existing Chapter 51 valuative
multiplier-ideal estimate gives the explicit bound

`0 <= h_(k,m)(v)+min(rho(v),k) <= A_E/(m b_E)`.

Here rho(v)=nu_E(V o mu)/b_E and A_E is the discrepancy of the smooth
product, not a discrepancy on X silently substituted for it. The model
and E are fixed while m tends to infinity. The estimate is pointwise in
the divisorial valuation, not uniform over all such valuations. Thus
h_k(v)=max(-rho(v),-k). Rational division by lambda_j=1+1/j gives
positivity in alpha, using h_k<=0 for monotonicity and the lower bound
-k for noncollapse. Then k tends to infinity; monotonicity holds on
the entire spectrum by ideal inclusion. The value at the trivial
valuation prevents total collapse. Real translation by the growth slope
and divisorial uniqueness finish the argument. No diagonal interchange
of these limits is assumed.

For U_s=-c s with c>=0, the new example computes
I(mV^(k))=(tau^floor(m min(c,k))). The condition on a nonnegative
integral vanishing order r is r>m min(c,k)-1, including integral
thresholds. This gives the exact dyadic limits and demonstrates why a
fixed k<c gives -k instead of -c. The case c=0 has unit ideals.

## Exact sources and remaining inputs

Demailly, *Regularization of closed positive currents and intersection
theory*, J. Algebraic Geom. 1 (1992), 361–409, is cited through the existing
`Dem92reg` entry. The
[author's PDF](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/regularization.pdf)
was checked at Proposition 3.1, Lemmas 3.5–3.6, the gluing proof and
Proposition 3.7. Author-PDF pages 13–17 were read and visually inspected;
these page numbers are not journal page numbers. The finite-cover gluing
proof supplies uniform estimates on the smaller compact product. The
source's introduction also explicitly describes its local application on
relatively compact subsets. The local original `/Users/mingchen/Downloads/regularization.pdf`
retains SHA-256
`3dbc4cb1d915168cfc00d23da74acf1a53fdc1c0ed4a2d7ede85e2b6d159dc90`.
This direct inspection supersedes the access limitation recorded in the
22 September radial-normalization audit, which remains unmodified.

The exact Mesquita-Piccione source is the
[18 September 2025 author version](https://arxiv.org/html/2409.06221v2),
Section 5.1.1, Lemma 5.1.3 and Theorem 5.1.4. Printed pages 45–46
were read, rendered and inspected. Its fixed cutoff does not justify
convergence to untruncated divisorial numbers; the already present cutoff
exhaustion is preserved and now tested by the explicit example. PDF SHA-256:
`9eb2ea7686a5962ebc11c5eacd23b0cb3dcb081e27ac48292933f291fc82cb23`.
The revised block uses the exact `MPTropicalV2` entry. No bibliography
entry changed.

Multiplier-ideal coherence, subadditivity and the divisorial approximation
estimate retain their Chapter 51 source dependencies. Demailly's analytic
regularization theorem is precisely identified and applied, not reproved
in full. Its pointwise and local L1 convergence is not used in place of
the separate valuative estimate. The general maximal-ray existence,
sequential approximation and mixed-slope inputs after this block retain
their previous explicit status. No new independent-agent or production
verifier receipt is claimed.

## Two passes and validation

The first full build produced 3,979 pages (18,941,197 bytes), with no
unresolved reference/citation or layout overflow. Physical pages
3365–3369 were rendered and visually inspected. The second complete
statement/proof/source/notation pass checked finite flag coherence,
the two curvature operators, the exact ideal singularity type, the sign
of the residual divisor, restriction to central components, all three
limiting parameters, noncollapse and integral floor endpoints. It clarified
local ideal generators, recalled the dimension, made the source-to-book
curvature conversion explicit, specified the disc where the discrepancy
is computed, and spelled out the residual-current subtraction.

The final full build and visual inspection of physical pages 3365–3370
are complete. This is a scoped review, not an all-page visual audit.

- Full build: PASS, **3,979 pages, 18,942,365 bytes**.
- Reference/input check: **390 TeX files, 11,637 unique labels**; no
  missing input, duplicate label, dangling reference or structural defect.
- Final log: no unresolved reference/citation, multiply-defined label,
  rerun request or horizontal/vertical overflow. Existing class/underfull
  warnings remain.
- Scoped strict house audit: zero errors and one reviewed exact-author-version
  arXiv warning. Strict mode returns 1; no warning-free strict pass is claimed.
- Inventory: PASS, **45 active atoms / 14 environments**, tiers
  **(0,5,8,15,17)**.
- Surrounding Chapter 60 text is byte-identical to the baseline.
- `git diff --check`: PASS.

Final Chapter 60 SHA-256:
`97597d2e7fca2001634b8db246a43495c225fbc19dd6ea2327f17b78c4b57500`.
Final live PDF SHA-256:
`ec2121a640902748c0c3a4b3feb5e354099c726949cdec795e41ab3fb26e67d2`.

P12.1's fragment retains SHA-256
`8d9f9bd9edb057b95773479279bbdabb3240319e4cb56f6f15cb2bd923fb4380`.
The supplied normalized-links PDF and archived copy both retain SHA-256
`71f5e0d50bdcbf493cb96a869e2db03a78bd591b3eba2f797da5a23f6253daaa`.
The supplied CURVE_PSH.tex retains SHA-256
`9142aac73c5af7e4e715b3313def5ed56fae4e63e1ac8a53d0419df7d2194be9`.
All 45 active atoms, P12.2–P12.6, supplied originals, bibliography,
frozen packets, verifier receipts and dated releases are unchanged.
The live PDF remains an ignored build product. The next unit is the
maximal-ray order/existence argument and the test-curve correspondence.
