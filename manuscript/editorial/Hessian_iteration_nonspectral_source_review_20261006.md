# Local Hölder subsolutions, iteration and non-spectral Hessian equations

This source review follows the regularization/capacity checkpoint. Three
exact PDFs have been read completely, including proofs, figures and
references: 63 physical pages displayed in 32 sheets. It distinguishes
local boundary estimates from compact mass normalization, and a recent
non-spectral analytic framework from its proposed later applications.
No new theorem or active TeX is admitted at this checkpoint.

## Acquired editions and limits of the reading

| Source | Exact acquired edition | Physical pages |
| --- | --- | --- |
| Rémi Delloque, *On Polynomial Complex Hessian Equations I: Non-Linear Non-Spectral Elliptic Hessian Equations on Riemannian Manifolds* | [2610.06529v1](https://arxiv.org/abs/2610.06529v1), 5 October 2026, 15:34:20 UTC | All 40; sheets 01–20 |
| Vincent Guedj, Sławomir Kołodziej and Ahmed Zeriahi, *Hölder continuous solutions to Monge–Ampère equations* | [Author-posted PDF](https://www.math.univ-toulouse.fr/~zeriahi/GKZ06-PLMS.pdf) bearing math/0607314v1; arXiv metadata dates v1 to 13 July 2006, 15:45:46 UTC | All 10; sheets 21–25 |
| Sławomir Kołodziej and Ngoc Cuong Nguyen, *A remark on the Hölder regularity of solutions to the complex Hessian equation* | [2407.13130v2](https://arxiv.org/abs/2407.13130v2), 4 April 2025, 01:56:08 UTC | All 13; sheets 26–32 |

The respective PDF SHA-256 values are:

```
604988e0137cb67bc38dfb5c70d81e26c6b83f8963c161450df67b5059b4e476
3e4403f7cee8bbf4c08b80da09deb359f3880da6c551b0ac3d6d8c632e1cf800
22a5250a1f77be1caf463423e8a0c93cdc914480e332863c38a2c76ac37fb3ea
```

The complete extracted-text SHA-256 values are:

```
4e356db9dd483de7a8f67c77fc4a1676e22be0098e40518cb4beee09008928b8
497bdb01ef1267b21e94c6bdd36051039d82487c5e20a3f96fc4b50597fcc641
59052c6c1c9edc279756ac537add9c8866260846d846faae5425d89f2b886d64
```

Delloque's font-extraction warning is retained; the matching rendered
pages and all six figures were inspected. The author-posted GKZ file is
not certified as byte-identical to the arXiv PDF, or as the eleven-page
BLMS 40 (2008), 1070–1080 journal article. The journal article remains
unread here. The JFA 289 (2025), 111005 publication of Kołodziej–Nguyen is
also metadata only; this review reads the thirteen-page v2 preprint.
No issue found in the early GKZ file is automatically attributed to its
later published proof.

The original iteration dependency remains unacquired: Kołodziej,
*Equicontinuity of families of plurisubharmonic functions with bounds on
their Monge–Ampère masses*, Math. Z. 240(4) (2002), 835–847,
[DOI 10.1007/s002090100401](https://doi.org/10.1007/s002090100401).
Exact Crossref metadata was obtained. The publisher PDF request returned
HTTP 200 HTML with a cookie interstitial, rather than a PDF. Its response
is retained with hash
`a93b58970bf805acb2c2fb0137c5f7b77e604cb7eff3478c73351257394d7770`.
This is not a reading of its Lemma 4.3. The exact p/n stability exponent
identified in the preceding Dinew–Kołodziej review remains a source gate.

## What the local Hölder argument contributes

Kołodziej–Nguyen consider a bounded strictly m-pseudoconvex domain in
complex Euclidean space, 1≤m<n. A positive Radon measure is dominated
by the Hessian measure of a bounded Hölder continuous m-subharmonic
subsolution. The boundary data are Hölder continuous. Their Theorem 1.1
gives a Hölder solution without assuming finite total measure. A Radon
measure is locally finite; its mass can diverge as the boundary is
approached. Example 1.2 uses the ordinary barrier −(−rho)^alpha, 0<alpha<1,
whose Hessian mass is infinite near the boundary.

The reduction to zero boundary subsolution uses a homogeneous envelope;
that reduction can lower the Hölder exponent. It is not permission to
use the original alpha without checking the boundary theorem. The
compact quasi-m-subharmonic problem is explicitly discussed separately
on page 3. This domain theorem does not remove the curvature or mass
conditions from the compact results already treated in Chapter 68.

The proof localizes its constants. On Omega_epsilon, an extended
subsolution agrees with phi−epsilon; near the boundary it is glued to a
multiple of rho/epsilon. The extension has a Hölder constant of order
epsilon^{-1}. Its mixed total masses grow as negative powers of epsilon.
Theorem 2.1 derives superlinear capacity domination. The small-capacity
optimization takes

```
alpha1=(p−1)/(2m+alpha),  alpha0=alpha*alpha1,
epsilon=capacity(K)^alpha1.
```

The exponent p must be in a range actually supported by the cited
volume–capacity estimate. The proof prints 1<p<n/m, whereas the cited
Dinew–Kołodziej Proposition 2.1 supplies p<n/(n−m). A safe nonempty
intersection is 1<p<min(n/m,n/(n−m)). This review does not certify the
larger printed range.

Proposition 3.3 compares functions agreeing outside Omega_epsilon;
Theorem 3.5 transfers an ordinary L1 difference to a measure-weighted
one, retaining epsilon^{-(m+1)}. The induction uses correctly typed
mixed measures (ddc phi_epsilon)^k wedge beta^{n−k} in (3.8). Its
integration-by-parts remainder is controlled in absolute value. The
constant contains comparison norms, which must remain controlled when
the proof is used for a family of functions.

Lemma 3.6 needs only local trace mass: bounded subharmonicity gives
integral_{Omega_delta} Delta u ≤ C||u||_infinity/delta. The Jensen error
then has ordinary L1 size O(delta), rather than the O(delta^2) available
with finite total Laplacian mass. This explains how the proof proceeds
despite infinite boundary mass.

Boundary barriers supply the collar error O(epsilon^alpha). With the
localized stability and transfer estimates, the final displayed bound
on page 12 is

```
sup(hat(u)_delta−u) ≤ C epsilon^alpha
                      + C delta^(alpha2*alpha3)/epsilon^(3m+1).
alpha4=alpha*alpha2*alpha3/(3m+1+alpha).
```

The positive exponents and constants depend on the preceding inputs.
The cited boundary argument of Nguyen 2020, Benali–Zeriahi's explicit
erratum, and the published mean/sup regularization references must be
checked before importing that quantitative chain into active TeX.

## Early GKZ file: comparison and regularization scope

Theorems A and B retain different assumptions. The gradient-energy
route uses square-integrability of the gradient of the homogeneous
solution; the Laplacian-mass route uses finite total Laplacian mass of
that homogeneous solution. Their strict exponent bounds are respectively
min(alpha,2/(nq+2)) and min(alpha,2/(nq+1)). Theorem 1.1 also retains the
comparison function's supremum norm in its stability constant.

Four literal diagnostics were checked against this exact early file.
They concern the boundary order in Lemma 1.3, arbitrary-function collar
gluing in Proposition 2.1, passage from translation L2 bounds to an L2
bound for a pointwise supremum, and the determinant in Example 4.3.
The diagonal model |z1|^alpha |z2|^2 has determinant zero away from
z1=0; adding the usual factor 1+|z2|^2 changes that calculation.

The collar counterexample is the bounded continuous psh function
−(1−|z|^2)^{1/4} on the unit ball, with zero smooth boundary values and
alpha=1/2. At distance delta from the boundary, its sup regularization
approaches zero, while u is −(2delta−delta^2)^{1/4}. Subtracting any fixed
C delta^{1/2} leaves an upward interior jump at the gluing surface.
This tests the stated arbitrary-u proposition. It is not asserted to
have an Lp>1 Monge–Ampère density, and does not refute the main existence
or Hölder theorem.

Other proof steps needing an exact published-source check are the
construction of a lower barrier versus a genuine measure subsolution,
the claimed monotonicity of the glued approximation, and the region of
integration in the mean/sup conversion. The valid energy-order identity
for smooth ordered psh functions with the same boundary is retained.
The true superlinear De Giorgi recursion is not confused with the
nonextinguishing recursion found in the earlier Dat review. Its finite
extinction scale still depends on the initial level or an established
uniform capacity bound.

## Non-spectral preprint: assumptions before applications

Delloque constructs a concave operator F_I by shifting each matrix
along a positive identity direction until it meets a smooth, closed,
elliptic convex fiber hypersurface. The construction has F_I(A−tI)=
F_I(A)−t. Its subsolution region records bounded intersections with
positive matrix directions. Guan's alternative separates a quantitative
subsolution gain from uniform ellipticity of the linearization.

The analytic estimates use the additional almost-spectral Definition
2.15, with nine structural constants. Theorem 1 retains the lower
linear hyperplane family H0, subsolution constants delta and R, and
the structural tuple. Theorem 2 has a further compatibility condition:
for every smooth u and h, membership Hess(u)−h Id in H forces the
integral of h against the Riemannian volume to vanish. This is a strong
extra hypothesis, not an automatic analogue of cohomological
Monge–Ampère mass normalization. Theorem 3 uses an ordered family of
hypersurfaces and a parameter chosen by continuity. Its endpoint and
subsolution assumptions also remain explicit.

The introduction describes a three-part project involving polynomial
complex Hessian equations and later cohomological criteria. Part I
does not itself prove a general numerical criterion for that project.
Its initial bidegree convention for the gamma coefficients also needs
alignment with the displayed equation. Neither the proposed later
criteria nor unrestricted non-spectral estimates are imported here.

Five literal diagnostics identify issues in the present analytic proof:

1. Lemma 2.8 uses the wrong tangent inequality for a concave function
   and omits subtraction of the base point. The correctly directed
   upper bound is compatible with the required finite limsup; the
   lemma is not thereby refuted.
2. Positivity of the vertical component of a unit normal in the total
   bundle does not imply that its pairing with the vertical identity
   is at least one. Later estimates can instead control the horizontal
   and vertical components together.
3. Definition 2.15 bounds B and its first derivative, but not its second
   derivative. Equation (23) contains d2 B and mixed dB terms; the
   subsequent computation omits them. On a flat two-torus, take
   f(lambda)=trace(lambda)−1 on the trace-positive cone, G=0 and
   B=−cos(Kx) Id/K. A fixed tuple (1,2,2,1,1,1,1/4,1,1/4) works for
   K≥2. At x=0 and A=diag(10,1+2/K−10), the tangent vector (e1,0)
   has −d2 F_I=−K, while ||A|| remains bounded. Thus the literal
   Lemma 2.16(4) constant cannot depend only on that tuple. A
   homogeneous tangent statement also needs ||xhat||^2. This tests a
   structural lemma on arbitrary fiber jets, not the main a priori
   estimate for solutions under a corrected structural hypothesis.
4. The lemma uses the descending eigenbasis of A; the proof switches
   to a basis diagonalizing B+A. Noncommuting symmetric A and B show
   why those bases cannot simply be identified. A perturbation
   argument would have to be supplied.
5. Lemma 4.2 prints plus-shift germs for the level F_I=h, although
   membership in H requires A−h Id. The correct shifted germs use
   B−h Id and G(x,A−h Id). Correcting the sign does not certify the
   accompanying derivative estimates.

The C2 argument additionally needs consistent diagonal correction terms
and a matrix quadratic-form completion, rather than an entrywise
inequality multiplied by an arbitrary positive semidefinite matrix.
The Evans–Krylov step must state a uniformly elliptic extension or
localization of the operator, and keep its coefficient dependence.
No full corrected proof or main-theorem counterexample is claimed.

## Admission and next source checks

Fourteen recorded diagnostics comprise four GKZ, five Kołodziej–Nguyen
and five Delloque checks. They have differing scope: a literal false
statement, a missing proof implication, or a citation-range mismatch
is identified as such. They do not certify repairs of the complete
external chains. No original result, production model call or
verification receipt is claimed.

The next useful input is Nguyen's published 2020 boundary/subsolution
paper, together with the Benali–Zeriahi erratum and the exact mean/sup
regularization source. After those gates, a scoped Chapter 68 explanation
can compare infinite local boundary mass with compact normalizers.
Delloque's almost-spectral proof remains outside active TeX while the
structural gates above are unresolved.

The checked 4,398-page book, all 425 active inputs, 108 protected
inputs, fourteen generated files, seventy preceding frozen manifests,
124 preceding exports, native catalogue and all 42 canonical problem
statuses remain byte-identical. The general Siu/closure boundary is
unchanged. No unchanged-book rebuild, fresh book PDF review or native
compile is claimed. Fetch both main and work at publication checkpoints;
integrate incoming author progress when present, and publish this review
on work with the existing draft PR.
