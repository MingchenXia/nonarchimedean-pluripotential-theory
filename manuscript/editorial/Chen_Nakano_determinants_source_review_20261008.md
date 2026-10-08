# Pointwise positive determinants and Lefschetz failure

Date: 8 October 2026. Source-only checkpoint before book integration.
Baseline: `fecadaffbd74e9c32d4c1186b92b0d3496fba141`.

Zhangchi Chen, *Nakano-positive determinants outside the Hodge–Riemann
cone*, exact arXiv:2609.07964v2, revised 28 September 2026, supplies
explicit pointwise counterexamples and a positive coordinate-diagonal
degree-one result. All eighteen pages were actually read, with complete
selected text, nine individually displayed matching images and sequential
notes. Three dependency PDFs were read in the exact partial scopes below.
The combined checkpoint has **38 distinct exact-source/page pairs and
20 matching images**, one complete paper and three partial readings.
Acquisition, locator searches and prepared views receive no reading credit.

The main constructions and positive theorem are unrefuted by this scoped
review. This is an attributed import audit, not a complete recursive
certificate of every foundation, an original theorem, an independent-model
receipt, or a canonical open-problem solution.

## Exact acquired sources

| Source | Actual physical pages read | PDF SHA-256 |
| --- | --- | --- |
| Chen 2609.07964v2, 18 pages | All 1–18 | `a463d1afbd8ae5dd8162749e3af4e30792f99abee56b70798eb1b6dcdf61c27a` |
| Ross–Süß–Wannerer, Monatsh. Math. 208 (2025), 495–524, DOI 10.1007/s00605-025-02134-6; published 30-page PDF | 1–5, 8–10, 16–21; fourteen pages | `85806d9f532a97c20b85674c703e48c9a660ee42ca1274e9612f9ca129efcb93` |
| Ross–Toma 1905.13636v3, 8 January 2021, 41 pages | 36–38; three pages | `ca5e8874d0e4e6579c01aaf262150674f4630c41a9efd11cf5151f2c629bbe8d` |
| Brändén–Huh, Annals 192 (2020), 821–891; published 71-page PDF | 7–9; three pages | `ecfc011bb4c755d6e1e802fbdcbff6eed4c6f907cb2968fedee6e68f5be71ff8` |

The accompanying source manifest checks these exact files. Cached files
remain in the cloud workspace.
Du, Finski and Wan have their previously frozen evidence in
[the Du source review](Du_Griffiths_Chern_source_review_20261007.md);
using those records adds zero fresh primary reading credit here.

## Mathematical audit

**CN01 — Categories and maps.** The ambient category is constant complex
forms on C^n, rank 1<=k<=n, and the full exterior spaces V^(p,q).
For p+q=n-k the determinant map sends alpha to alpha wedge det M
in V^(n-q,n-p). Definition 2.1 on Chen physical page 5 uses a path to
omega^k with every reduced map for Omega_t omega^(2j) nonsingular.
A single nonzero kernel excludes this cone, regardless of reference
form. These are pointwise statements, not automatic cohomology theorems
for globally constructed bundles or for smaller quotient algebras.

**CN02 — Positivity and diagonalization.** The i/2 convention is fixed
throughout. Nakano positivity tests the full Hermitian coefficient tensor;
dual Nakano positivity tests its partial fibre transpose. Griffiths tests
decomposable tensors. Coordinate SD means M=sum B_i V_i with every B_i
positive definite. The matrices need not commute; the SD seed explicitly
has noncommuting coefficients. Under SD all three tensor tests coincide.
Even-degree entries commute in the determinant, and d_I=k! D_k(B_i:i in I)
uses the symmetric mixed discriminant normalized by 1/k!.

**CN03 — Unrestricted seed and range.** Theorem A and Section 3, pages
8–9, give M_t=diag(omega_0 I_2+tN,omega_0 I_(k-2)), first in dimension
k+2. The full tensor is I+t(w_1w_1*+w_2w_2*), hence Nakano positive.
The explicit nonzero gamma satisfies gamma Delta=-gamma omega_U^2/2
and gamma omega_U^3=0. Its determinant wedge coefficient is
binomial(k,2)+(k-1)t-t^2/2, which vanishes at
t_k=k-1+sqrt((k-1)(2k-1)). Lemma 2.3 extends the ambient dimension
by positive identity blocks and an antiholomorphic wedge factor. The
source's general binomial and extension arguments are actually read;
bounded computer ranks do not replace them.

**CN04 — The two stronger conditions differ.** The same tensor's partial
transpose has eigenvalues 1+t (multiplicity six), 1-t (two), and 1
(kn-8). Since t_k>1 the displayed example is not dual Nakano positive.
Fibre transpose gives a separate dual-positive example with the same
determinant. Strict weak determinant positivity from the stronger
curvature hypotheses is retained as the Finski/Chen attributed input;
it does not imply a full exterior Lefschetz isomorphism.

**CN05 — Degree-one positive result.** Proposition 4.1 on pages 9–10
uses disjoint-subset blocks H_r^J. Lemma 4.2 on 10–11 obtains a common
finite rank-one frame with strictly positive coefficients for every B_i.
The spanning-frame determinant is multiaffine, nonzero and stable by
Cauchy–Binet/positive imaginary part. Reversal preserves its stability;
BH Proposition 2.2, physical 8/printed 828, makes the reversal Lorentzian.
Factorial normalization is trivial only because of multiaffineness.

RSW Theorem 8.2, physical 20–21/printed 514–515, requires positive
definite real quadratic forms and a nonzero dually Lorentzian symbol of
degree d-2. Its strict equality characterization excludes a radical.
Applied to the real diagonal matrices of frame coefficients, it gives
signature (1,k+1) for H_1^J (Chen Proposition 4.4, 11–12). Lemma 2.2
provides the path for any positive reference form. Thus Theorem B covers
min(p,q)<=1; it covers all bidegrees when n-k=2 or 3.

**CN06 — Import boundary and adjacent notation.** The complete selected
RSW proof of Theorem 8.2 uses classical strict mixed-discriminant AF,
cone-Lorentzian inputs of Brändén–Leake, and strict operator preservation.
The relevant RSW definitions and Theorems 4.4, 6.4 and 7.2 were read.
Those deeper foundations are not recursively certified here. Lemma 6.3
mixes source and target degree notation in its lexicographic base case;
the needed surjectivity follows degree-consistently because the apolar
adjoint is multiplication by a nonzero polynomial. Its quadratic target
is the one used here. The cone closure statement is interpreted for
nonzero directions, and equation (4) has a direction-variable mismatch
resolved by ordinary determinant polarization. The adjacent unqualified
global Kähler integral formulation is not imported. These observations
do not disprove the finite-dimensional mixed-discriminant theorem.

**CN07 — Higher-degree SD seed.** Section 5, pages 12–14, uses
W_j=V_(2j-1)+V_(2j), S_j^2=I and trace S_j=0. The coefficients
I+sqrt(t)S_j have eigenvalues 1+/-sqrt(t)>0 for 0<=t<=1/2.
Omega_t=(1-t)Sigma+(2+t)Pi and W_j^3=0. At t*=sqrt(6)-2,
u*=1+sqrt(6)/2, the nonzero (2,2)-form Pi-u*Sigma is annihilated.
The exact 15-by-15 determinant is
2^15 3^6 (1-t)^3 (2t+1)^3 (t^2+t+1)^2 (t^2+4t-2).
It has opposite endpoint signs. Mere Lorentzianity is weaker: the
four-variable fixture has Hessian eigenvalues 4,0,-2,-2.

**CN08 — General rank and strict perturbation.** Pages 14–15 give the
all-m counting identities for the block K_m of Omega_t omega_0^m/m!.
The auxiliary R_m has signature (1,m+5). The explicit determinant-one
congruence gives diag(K_m,-(m+2)R_m/(m+1)), requiring no inverse of K_m.
Both endpoint signs reverse at each extension. Before applying continuity,
the source adds epsilon omega_new I_2. Without this positive perturbation,
the first two-by-two block has zero new-coordinate coefficients. This
establishes the source Theorem C range 2<=k<=n-4, n>=6; its ambient
extension again uses Lemma 2.3.

**CN09 — Seed attribution.** Ross–Toma v3 Example 9.2 is on physical
37, not assumed to have the same location in the 2023 journal edition.
It concerns a rank-three ample real-twisted bundle on (P2)^3. The
cube-zero hyperplane algebra matches the W_j relation; the six-coordinate
top-volume coefficient is eight, a harmless positive factor. At t*,
(1-t*)/(3t*)=1/sqrt(6), matching the positive real twist satisfying
2tau+3tau^2=1/sqrt(6). The irrational twist is not described as an
ordinary holomorphic bundle. Chen's rank-two determinant realization
and extensions have a separate attribution from the earlier degeneration.

**CN10 — Dated questions.** Chen page 16's Question 6.1 and the two
boundary dimensions are source-era statements. Du 2610.05931v1,
5 October 2026, already fully read in the earlier checkpoint, gives
negative Griffiths-positive top Chern jets for all ranks at least nine.
Plane restriction and positive extension in extra tangent directions
give the negative answer in those ranks. Ranks four through eight are
remaining candidates in the compared sources, not an exhaustively
certified current-open list. Question 6.2 keeps rank two, dimension four,
both stronger conditions, and the (1,1) map. Neither counterexample above
answers it; coordinate SD is excluded by Theorem B. Limited fresh
literature queries found no additional primary resolution of that precise
question, but this is not an absence proof or a canonical status change.

## Exact computation scopes

The two author programs were fully inspected before execution and are
pinned by hashes `f114c0da540e86f02e04cea72b4329e9eb4f1095896f8a5d7852184f7508fd71`
and `fd45b1580fbcfaa07bf2cdfc63f2dd8cc126e53deb0165cfda1f09ea52ac5ae8`.
Their finite rank loops, explicit scalar identities, and sixteen-value
degree-bound determinant interpolation all passed. No package installation
or remote execution was needed.

Seven separately implemented exact diagnostic groups passed. Four check
unrestricted ranks 2–5 in dimension k+2, using interleaved one-form tuples
and the full ordinary permutation determinant; they recover the tensor
from the actual matrix entries before computing both characteristic
polynomials. The SD group uses six commuting square-zero coordinates
and an exact symbolic characteristic polynomial, rather than the author's
sixteen-point test. The remaining groups check the symbolic auxiliary
quotient and the zero-eigenvalue Lorentzian fixture. These are algebraic
fixtures and explicit identities, not arbitrary-rank computational proofs.

The first independent helper failed because SymPy discarded `real=True`
on a characteristic-polynomial generator: two identically printed symbols
were different objects. A separate 2-by-2 reproduction established this
cause. The failed version remains failed. A new helper repaired only the
comparison variable and passed all seven groups. No mathematical formula
was changed, and no failed run is relabeled as a successful receipt.

The 4,552-page baseline book, historical formal statements/proofs,
425 active inputs, 108 protected inputs, 131 frozen prior records,
211 prior exports, and the existing native catalogue remain the
preservation baseline for the next integration. General BJ22 critical
homogeneous Siu division/envelope closure remains open; the LPWZ density
candidate remains unverified; the canonical inventory remains 42 atoms
in 12 problem environments.
