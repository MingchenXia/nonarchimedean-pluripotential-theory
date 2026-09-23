# Chapter 59 dual-complex retractions and inverse limits

Date: 23 September 2026.
Baseline: `30bb6685d4ef88d1bad064d4297f7923e363af40`.
Scope: the normalized dual-complex construction, retraction lemma,
inverse-limit theorem and following net-convergence argument in Section 59.4.
The standing base X is a connected compact Kahler manifold. Models are taken
in the existing cofinal directed system of projective snc models.

## Findings and reconstruction

The old construction retained only component weights when asserting
continuity of the retraction. Distinct connected components of one boundary
intersection can have the same index set, so those weights need not
distinguish points of the dual complex. The old proof also evaluated a
character on X directly on ideals of a model, without a definition for
proper-support characters, and called its geometric center a point.
Transition compatibility was imported without checking the intersection
component. The inverse-limit proof then used separation by a PL lattice on
the limit without proving the needed separation/refinement statement.

The revised finite complex keeps a simplex for every connected intersection
component. Its face is glued to the unique containing component of the
smaller intersection. Vertices have weights 1/b_i. An invariant ideal a on
the model that is the unit ideal off the central fiber defines an effective
vertical Cartier b-divisor F_a on its normalized blowup. The previously
proved PL/Cartier correspondence gives the continuous function u_a=phi_F_a.
The coefficient formula recovers b_G^{-1} ord_G(a) at a normalized vertical
prime G. This defines the finite model-ideal values without extending a
proper-support character to arbitrary local holomorphic germs. The sign
is positive; the flag logarithm would correspond to -F_a instead.

For each closed stratum Z, the monomial value h_Z of its ideal equals the
minimum of the relevant component weights on a simplex whose stratum is
contained in Z, and zero otherwise. The formulas agree on faces. Component
ideals distinguish unequal weights, and an intersection-component ideal
distinguishes equal weights on different strata. The finite map H=(h_Z)
therefore embeds the compact complex with closed image in Euclidean space.

At a divisorial point, a normalized vertical prime on a common dominating
model has an irreducible analytic center C. The positive boundary indices
and the unique component containing C determine its monomial retraction.
For every Z, the condition C contained in Z is equivalent to its smallest
boundary stratum being contained in Z; this checks all ideal values, not
just the divisorial coordinates. The continuous vector (u_I_Z) lands in
the closed image H(Delta) on the dense divisorial locus, hence everywhere.
Composing with H inverse constructs the retraction, including characters
of proper support. Density is used only after the earlier PL/Cartier
correspondence and its independent injectivity proof.

Rational monomial points are realized by invariant ordinary blowups of
boundary strata. Connectedness of C* preserves each stratum and the
resulting prime, while the value 1 on t fixes its factor as 1/b_G.
The retraction recovers these rational points; continuity and their density
give p i=id. This proves injectivity of restriction to X and surjectivity
of p without assuming either. The product-model complex is one point,
mapped to the trivial valuation, also covering dim X=0.

For a domination, the matrix in mu^* E_i=sum a_ij E'_j has nonnegative
integer entries and b'_j=sum b_i a_ij. The matrix gives the weights, and the
smallest stratum containing the image gives the component label. Local
boundary monomials verify both the face gluing and compatibility at
divisorial centers. Density extends compatibility to all characters.
The retractions R=i p satisfy R_X R_Y=R_X for Y dominating X, as required
by the existing measure-retraction proof in Chapter 61.

The explicit surface example starts with the two graphs z and -z on
P1 x P1, then blows up the first curve in the central fiber and the strict
transform of the second. At each of their two transverse intersections,
the equations t=uv and the blowup of (u,z) give the charts t=zsv and t=uv.
The final fiber H+E+F is snc, with all multiplicities one. E intersect F
has two disjoint P1 components, giving distinct dual edges with vertices
E,F. Their midpoints have the same component weights (0,1/2,1/2), but
the ideal of one component has values 1/2 and 0. This is a calculation
within the already established model construction, not a research claim.

Aff_Q is explicitly defined to be affine on each original simplex with
rational vertex values. The fixed-model correspondence is
D=sum d_i E_i -> f_D(w)=sum d_i w_i, with f_D(xi_i)=d_i/b_i and inverse
coefficients b_i f(xi_i). It commutes with pullback, and the construction
gives phi_D=f_D composed with p at every character. Consequently PL
separation proves injectivity of the inverse-limit map. For a compatible
tuple, the closed nonempty retraction fibers have the finite intersection
property: a section on a common dominating model supplies each finite
intersection. Compactness proves surjectivity. Finally every PL function
is eventually unchanged on R_X(v); uniform PL density proves convergence
of the net R_X(v) to v. No countable cofinal subsystem is assumed.

## Sources and scope limits

The exact source checked is Mesquita-Piccione,
[arXiv:2409.06221v2](https://arxiv.org/abs/2409.06221v2), 18 September 2025,
Section 3.1.1, Theorem 3.1.1, Lemma 3.1.2 and equations (3.1.2)--(3.1.4).
PDF pages 28--31 were read and visually inspected. The source PDF SHA-256 is
`9eb2ea7686a5962ebc11c5eacd23b0cb3dcb081e27ac48292933f291fc82cb23`.
The book supplies the model-ideal construction, retains the stratum labels
through continuity and domination, and replaces the tropical-Gelfand
surjectivity step with the compact finite-intersection argument. The
coefficient convention uses the normalized vertices explicitly.

The exact-version bibliography entry MPTropicalV2 is unchanged. The earlier
publisher-PDF access limitation remains: these locators are not claimed to
have been checked in the published MP24 version. The bibliography-aware
changed-block audit's one arXiv-only warning was reviewed against that
limitation. The following projective comparison paragraph, including its
BJ22 citation, is outside this unit and preserved byte for byte; no fresh
audit of that paragraph is claimed.

## Second pass and validation

The first complete build and visual review were followed by a second local
mathematical/source pass. It rechecked face formulas, ideal signs, the
dense-subset extension, rational realization, stratum labels under
domination, the repeated-edge example, vertex normalization and the finite
intersection argument. It made the equivalence C contained in Z iff W
contained in Z explicit, added the product-model and zero-dimensional
case, and displayed the identity p_X i_Y=r_YX before the retraction
composition used by Chapter 61. Short formulas and the final ideal values
in the example were incorporated into their sentences to avoid separation
from their introductions across pages.
The complete build and rendered-page review were then repeated.

The final build has 3,957 pages and 18,820,548 bytes. The reference/input
check passes for 389 TeX inputs and 11,580 unique labels, with no missing
inputs, duplicate labels or dangling references. The four former item
labels had only local references; replacing that enumeration and adding
the worked-example label accounts for the net loss of three labels.
The final log has no unresolved references or citations and no horizontal
or vertical overflow. Existing underfull-box and class warnings remain.
Final physical pages 3325--3331 (printed 3257--3263) were rendered and inspected, including both
boundaries. `git diff --check` passes.

The strict changed-block house-style audit has zero errors and warnings.
The whole-chapter audit still reports 144 legacy errors: 141 inline-math
delimiter reports, two unlabeled examples and the existing MP24 compound-name
label report. Its eight warnings concern legacy titles and a chapter-label
prefix, plus three bibliography entries (including the exact-version
MPTropicalV2 warning addressed above). The
baseline had 198 errors and 13 warnings; removing the old optional lemma
title and four item labels accounts for the warning reduction. A clean
whole-chapter house-style audit is not claimed.

Chapter 59 before the dual-simplex preparation and from the projective
comparison paragraph onward is byte-identical to the baseline. Chapters
58 and 61, the bibliography, author-supplied and restored CURVE_PSH.tex,
research packets, verifier receipts and dated releases are unchanged.
The inventory remains 46 active atoms in 14 formal environments, tiers
(0,5,8,16,17). The generated live PDF is ignored and is not a new release.
No independent-agent audit, production-verifier pass, new research theorem
or research-atom closure is claimed.

Final SHA-256:

- Chapter 59: `0fa0593001af79763e1b461c32f0aaed73788e871aec4ebea17763c896a133a4`.
- Unchanged bibliography: `f77736549ed82a38bc6db488b2527629b2cb2ebf5b47475f3c94e08e0e068219`.
- Generated live PDF: `df4708d982a84f3168e219cd3617824b97fdf5b10a15ae32025f458035ff0ad9`.
- Supplied and restored CURVE_PSH.tex: `9142aac73c5af7e4e715b3313def5ed56fae4e63e1ac8a53d0419df7d2194be9`.

Next: audit the log-discrepancy extension, its behavior under retraction,
the total-versus-reduced normalization and its Gauss comparison, with
exact source locators and checks on the adjacent examples.
