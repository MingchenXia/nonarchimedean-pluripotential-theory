# Final hostile audit of the Chapter 55 integration of Xia Conjecture 8.8

Date: 2026-08-24

Release addendum: after this human integration audit, the exact current metric
theorem passed source-aware production run
`20260824T054849Z_57635bfa07f4`, and the exact current line-bundle
specialization passed `20260824T061508Z_17bf73c6b37c`.  Each returned final
`correct`, zero critical errors, and zero gaps.  The frozen hashes below remain
the human-audit snapshot; the two exact-current receipts control the installed
theorem blocks.

Audited target:
`manuscript/parts/part5/ch55_okounkov_dh.tex`, beginning at line 618.

Controlling proof object:
`manuscript/editorial/solver_dossiers_20260824/xia_conjecture_8_8_repaired_proof_packet.md`.

Controlling proof-object SHA-256:
`9227826d7ba5c641c5fe32cc4daae9acbb3b57274dcc1b356ba8beadd58cad7b`.

Current whole-Chapter-55 SHA-256 at the end of this audit:
`16272c77c90c89079fcf2ea2cb72cdaaec08a7d586e8cc3d23fdf700746b3540`.

Current SHA-256 of lines 618--1292, the integrated mixed-volume section through
its status paragraph:
`8f1a3e52f15895118ae03d48a4551e4a0b5c1e9b829d2bab6779f8d54eee4062`.

## Verdict

**PASS.** No must-fix mathematical defect remains in the Chapter 55
integration of the repaired proof.  The chapter reproduces the load-bearing
content of the controlling proof object, preserves its hypotheses, and does
not strengthen its conclusion beyond the positive-ideal-volume projective
domain.

The provenance-only edit made during this audit, recording the separate
source-level production-Rethlas receipt for repaired `main.tex` (SHA-256
`5746eb011417caecfa876c05c6c74fb548e2ae9d086c1441189bbcad02a96594`),
does not alter any mathematical statement or proof step and therefore does not
change this verdict.  The chapter correctly keeps the proof-object receipt
`9227826d...58cad7b` as the controlling mathematical receipt.

## Requested hostile checks

### 1. General valuations

The supremum is explicitly taken over every surjective valuation
\(\mathbf C(X)^\times\to\mathbf Z^n_{\mathrm{lex}}\) trivial on constants,
not merely over flag valuations.  The one-dimensional-leaf argument is valid:
surjectivity gives rational rank \(n\), Abhyankar's inequality forces residue
transcendence degree zero, and algebraic closedness of \(\mathbf C\) makes the
residue field equal to \(\mathbf C\).  This justifies both the leaf count and
the graded-field identification used in the degeneration.  The lower bound is
allowed to use the flag valuation supplied by Wilms because that valuation is
a member of this larger family; the upper bound is proved for every member of
the family.

### 2. Finite-level degeneration

The chapter uses only the required inclusion
\(Q=\operatorname{in}_{\mathsf A}(I)\subseteq J\), in the direction that
makes the toric variety a component of the special fibre.  It does not assume
a finite Khovanskii basis or the generally false equality \(Q=J\).  Scalar
realization of the matrix initial ideal preserves every multihomogeneous
piece.  Passing to `MultiProj` removes only irrelevant torsion and preserves
the eventual multigraded Hilbert polynomial.  Since the toric closure and the
special fibre both have dimension \(n\), the toric closure is a
top-dimensional component, and positivity of component multiplicities and
nefness of the factor hyperplane classes give the inequality in the correct
direction.

The one-dimensional-\(W_i\) branch is separated before the boundary-incidence
argument.  In the remaining case each factor imposes one independent
hyperplane condition, so a general \(n\)-tuple avoids the boundary.  The full
value lattice condition removes any lattice-index factor from the
Bernstein--Kushnirenko count.

### 3. Movable upper bound

The common-degree lattice argument is complete.  Surjectivity provides
rational functions of values \(e_j\); the degree-zero fraction field of the
section ring of one big divisor writes them as ratios of homogeneous sections
of a common degree; products with common denominators produce section pairs
whose value differences are exactly \(e_j\).  Passing to a common multiple of
that degree and of a birational degree preserves these unit differences at
every later divisible level.  The symmetric-power subsystem makes each
degree-level map, hence the joint map, birational.

On a simultaneous resolution the moving parts are nef and lie below the
pullbacks of the divisors.  The projection formula gives the finite-level
mixed degree, and BFJ09 Propositions 2.12--2.13 give its upper bound by the
movable product.  Dividing by \(k^n\), Hausdorff convergence of the normalized
finite-level hulls and continuity of mixed volume yield the claimed bound for
every valuation.

### 4. Uniform \(d_S\) control

The false two-inclusion convex sandwich from the supplied source is not used.
Both intermediate bodies lie between the same inner and outer bodies, giving
all four inclusions.  The John-ellipsoid normalization is uniform because the
inner bodies have a common positive volume lower bound and the Minkowski sum
of the outer bodies has a common volume upper bound.  Independent translations
of the four bodies for each argument do not change mixed volume, and the
determinants of the normalizing maps are bounded above and below.  Blaschke
selection, strict volume monotonicity for full-dimensional convex bodies, and
continuity of mixed volume therefore prove the stated uniform conclusion.

The potential sandwich supplies the two comparisons with the moving term and
then proves the two missing comparisons with the limit.  For a fixed tail,
closure of the \(P\)-preorder under simultaneous \(d_S\)-limits yields
\(\eta_j\preceq_Pu\preceq_P\psi_j\); normalization and modelness convert these
relations into the required pointwise inequalities.  The finite diagonal
subsequence is explicit.  Diagonal body volumes are valuation-independent,
and Minkowski superadditivity plus containment in the ordinary body of
\(L_1\otimes\cdots\otimes L_n\) supplies the required uniform outer-volume
bound.  Thus the proof establishes uniform convergence of the mixed-volume
values, without claiming uniform Hausdorff convergence of bodies.

### 5. Rational analytic singularities

The rational coefficient is stated before divisor arithmetic is used.  On a
common log resolution the residual classes are rational, nef, and big, and
the partial body is translated by the valuation of the effective divisor.
Translation invariance reduces the upper bound to the movable upper bound.
For the reverse inequality, the residual nef classes are perturbed to ample
rational classes, Wilms supplies a flag that may depend on \(\varepsilon\),
and multiplication by the canonical section of the effective divisor proves
the body inclusion.  No attainment of the supremum is inferred.

### 6. \(\mathcal I\)-envelope reduction

Positive Cao/ideal volume is not confused with positive raw mass of the
original potential.  The proof first replaces
\(\varphi_i\) by \(u_i=P_{\theta_i}[\varphi_i]_{\mathcal I}\).  This preserves
every partial body by \(\mathcal I\)-equivalence and preserves the left side
by the definition of the mixed metric volume.  Maximality of the
\(\mathcal I\)-envelope and the model-envelope competitor argument show that
\(u_i\) is an ordinary model potential; its raw mass is exactly the positive
ideal volume.  The rational-analytic Kähler-current approximants converge in
\(d_S\).  Mixed non-pluripolar mass continuity handles the left side, while
the valuation-uniform result handles the supremum on the right.

## Scope and exclusion firewall

The final theorem retains all necessary scope restrictions: smooth connected
projective \(X\), big line bundles, and positive multiplier-ideal volume in
every entry.  The text explicitly leaves the zero-volume and transcendental
extensions open and explicitly declines to claim a maximizing valuation.

The proof chain contains no citation to, quotation from, or dependency on
arXiv:1710.09731.  The final safeguard sentence saying that no Deligne-pairing
Riemann--Roch formula is used is an exclusion statement, not a mathematical
dependency.

## Non-blocking presentation observations

Two one-line facts are implicit but standard and do not constitute gaps:

1. in the uniformity proof, the summed potential has positive volume because
   its raw non-pluripolar self-mass contains positive pure terms (and ideal
   volume dominates raw mass), so its partial body is defined before
   superadditivity is invoked; and
2. in the analytic case, a Kähler current with rational analytic
   singularities leaves a nef and big residual class on a log resolution
   (indeed the standard source gives the stronger Kähler-class conclusion).

Expanding either sentence could help a reader, but neither is a must-fix and
neither changes the PASS verdict.
