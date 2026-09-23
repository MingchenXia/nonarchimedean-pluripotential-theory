# Chapter 54: trace calculus and decreasing continuity

Audit date: 23 September 2026.

## Scope

This unit replaces the short proof of Proposition 54.5.1 by a reconstruction
of the approximation and limiting arguments. It also replaces the local
increasing-sequence sketch by a global projective example. The existing
statement and cross-reference labels are retained.

The domain D_Y is closed under sums, positive scaling and finite maxima:
generic Lelong numbers add, scale and take minima. Thus the old conditional
phrase about membership of the sum in D_Y was unnecessary.

For sums and maxima, the canonical dyadic approximants have one rational
analytic coefficient. Their product and sum ideals give analytic types for
the sum and maximum, respectively. Commutation with restriction alone is
not a proof: one must first check that the resulting approximations are
quasi-equisingular. The revised proof does this using the d_S approximation
criterion, continuity of addition and maximum, the I-envelope identities,
and closure of I-good potentials under those operations.

For positive real scaling, rational coefficients lambda_k increase to
lambda. After normalizing the approximants to be nonpositive,
lambda_k a_k decreases to lambda phi and remains analytic. Small-scaling
estimates and change of scale in the background give the required d_S
limits in both source and target. An irrational multiple of a rational
analytic coefficient is not silently declared analytic.

## Decreasing continuity

The hypothesis is a decreasing net in one common psh class, convergence
in d_S, and zero generic Lelong number for the limiting singularity type.
It does not require the original inputs to be I-good or the raw pointwise
limit to equal the chosen d_S-limit representative.

Closedness of P-order makes every earlier input belong to D_Y. For a
sequence, compatible canonical rows admit a diagonal eta_j with two
separate errors less than 1/j: an ambient error to the I-envelope of the
j-th input, and a restricted error to its trace. Continuity of the
I-envelope makes eta_j converge to the limiting I-envelope. The normalized
model envelopes P_Omega[eta_j] decrease pointwise to that envelope, remain
analytic with the same bounded singularity types, and satisfy the
multiplier-ideal criterion for quasi-equisingularity. Their restrictions
therefore converge to the limiting trace. The second diagonal error
completes the proof.

The ambient and target backgrounds are fixed before taking these limits.
The target is rho^* Omega + kappa, retaining the preceding construction's
uniform positive mass bound. The sequence proof is upgraded to nets by
choosing ordered indices retaining a fixed positive target-distance gap
while the ambient distance tends to zero.

## Increasing counterexample

On P2 let f_l = log(|Z_l|^2 / sum |Z_i|^2), l = 1,2, and
phi_j = max(f_1, f_2/j). These globally defined weights are nonpositive;
omega_FS + ddc f_l is the hyperplane current. Thus phi_j is globally
omega_FS-psh and increasing, with regularized supremum zero, and converges
to zero in d_S. Its only analytic pole is at H_1 intersect H_2.

On Y = H_2 every restriction equals f_1|Y. Constant approximation sequences
for analytic potentials identify these restricted types with their traces.
In the background 2 omega_FS|Y the non-pluripolar mass of the trace is 1,
while the mass of the trace of zero is 2. This proves failure of increasing
continuity by the mass-continuity theorem. The positive target background
avoids relying on a zero-mass example, and the exact global weights remove
the unspecified bounded errors in the former local sketch.

The second mathematical/prose pass rechecked the ideal inclusion direction,
the order of rational scaling, all approximation criteria, the two diagonal
errors, the distinction between ordinary bounded equivalence and
P-equivalence, and the global psh, domain and mass assertions in the
example. The zero-dimensional case is stated separately after checking
domain membership for every net input. The diagonal starts with k_0 = 0
and satisfies k_j >= max(j,k_(j-1)), so its cofinality is explicit.

## Primary sources

The author's [final lecture manuscript](https://mingchenxia.github.io/Lectures/SGPT_final.pdf),
dated 18 July 2026, supplies the following exact inputs:

- Theorem 1.6.2, page 33: canonical dyadic approximants.
- Propositions 3.2.10--3.2.11, pages 127--128: bounded analytic types of
  envelopes and the I-envelope identities for the operations.
- Lemma 6.2.3, pages 216--217: the uniform small-scaling estimate.
- Lemma 6.2.6, pages 223--224: convergence after positive scaling of the
  potential and its background; no exact d_S homogeneity formula is needed.
- Proposition 6.2.4, page 224, and Theorem 6.2.2, pages 225--226:
  continuity of maximum and addition.
- Propositions 6.2.5--6.2.6, pages 225 and 227: closed P-order and
  convergence of decreasing model envelopes.
- Theorem 6.2.3, page 227: continuity of the I-envelope on the positive-mass
  part. This is distinct from Theorem 6.2.4 on Lelong numbers.
- Theorem 6.2.6, pages 230--231: the multiplier-ideal consequence of
  d_S-convergence.
- Corollary 7.1.2, page 238, and Proposition 7.2.1, pages 239--240:
  the quasi-equisingular approximation criterion and I-good operations.
- Propositions 8.2.1--8.2.2 and Example 8.2.1, pages 263--266:
  the trace calculus, decreasing-net theorem and local increasing example.
- Corollaries 6.2.4--6.2.5, page 210: increasing d_S-convergence and
  continuity of non-pluripolar mass.
- Appendix B.3, pages 504--505: the normal-target calculus. Approximation
  and multiplier ideals in the proof remain on the smooth ambient X.

Physical source pages 243, 246, 280, 281 and 282 were rendered and inspected;
other listed locators were checked in the source text. The supplied author
files chapter_trace.tex, chapter_comp.tex, chapter_Igood.tex,
chapter_envelopes.tex and chapter_pshfunctions.tex were read without editing.

The accepted version [Darvas--Xia, arXiv:2403.08259v2](https://arxiv.org/abs/2403.08259v2),
13 March 2026, is cited with the existing DXTraceV2 key:

- Lemma 3.9(i), page 13: input I-order and order of normalized traces.
- Lemma 3.10, page 14: the sum identity in I-class and scaling of normalized
  traces under the stated Kähler-current hypotheses.
- Lemma 3.12, pages 15--16: a common strictly positive curvature margin and
  decreasing pointwise convergence of I-envelopes.
- Example 3.13, page 16: the increasing local pattern used in the global
  realization above.

The accepted paper's fixed-background statement is not cited as if it
directly asserted the broader decreasing-net formulation. The latter's
precise source and additional envelope/diagonal inputs are identified.
No existing bibliography entry or supplied reference-source file was changed.

## Validation and preservation

The final full build succeeds with 3,937 pages and 18,696,150 bytes.
The build log has no unresolved references or citations, duplicate labels,
or horizontal or vertical overflow. Existing class-name and underfull-box
warnings remain outside this unit.

The reference/structure check passes for 389 TeX inputs and 11,540 unique
labels, with no missing inputs, duplicate labels or dangling references.
The scoped strict writing audit passes with zero errors and zero warnings.
The research inventory passes unchanged: 46 active atoms in 14 formal
environments, with tiers (0,5,8,16,17). Whitespace/diff checks pass.

Final physical book pages 3227--3231 (printed 3159--3163) were rendered
and visually inspected, including the preceding proof and following
section boundary. The statement stays with its formulas; the proof,
diagonal estimates and complete increasing example are readable without
clipping or orphaned section headings.

PDF SHA-256: ae27a70b48df239c4adff4d96ff5d6780805695df870e398a07ca3a3efd36a01

Chapter 54 SHA-256: 468dff9e85488802e59c6bb7663e2d61c674fa7b60d5652d2f29bd8e23c55981

Final lecture PDF SHA-256: c816eea5f06822021fa8dd75b70f82724ee47e6dcd6830729f5ecc109296b706

Accepted trace-paper PDF SHA-256: 5d6f43d96be101f6aa1a3ddbdd92b5bc49131a0deabbf199e03111d6c0fbaa3c

Read-only author-source SHA-256 values:

- chapter_trace.tex: d51549235a0fc017197d47f71cd6faf21a1c607ce11895da3f31f7f621774d9f
- chapter_pshfunctions.tex: 22718016825490fb84d8f53af1c3b5214cfb6765a31f6d570dbb8a59a3fba34b
- chapter_comp.tex: c8cb2b9c6cbcc9a1b6965f23802eaed6891fcc23b965163a37a227e53497f7cb
- chapter_Igood.tex: 93f94eea4f761c0e3c414bc70b84911ca6aa646cec229ac6caf8461cae7e81cd
- chapter_envelopes.tex: 9b3757bb28b898c90361f2928dbbff1b580a0c674a2f6e009823658126ec969b

Chapter 51 retains SHA-256
829d6d72530cda573f80cdde61ee3c72e41959600632774ae6a6b2402330e356.
Chapter 62 retains SHA-256
3e868c8797ca563a1654e46bdd704272188bfce54edb9639d909434f1d7fff36.
Both CURVE_PSH.tex copies remain byte-identical with SHA-256
9142aac73c5af7e4e715b3313def5ed56fae4e63e1ac8a53d0419df7d2194be9.

The current README build counts were reconciled with this build; its
previous header still displayed the pre-trace-construction counts.
The current continuation and chapter-status records were updated.
No dated build receipt was rewritten.

Only Chapter 54 and current editorial records were changed. Frozen proof
packets, verifier responses, supplied sources, research classifications,
and dated release artifacts remain unchanged. The PDF is an ignored local
build artifact. These are local mathematical/source/style/build/visual
checks, not an independent-agent or production Rethlas verification.
No research-frontier theorem or atom closure is claimed.

The next bounded unit is the passage from analytic trace classes to the
non-Archimedean trace: the levelwise domain, concavity, upper-semicontinuous
regularization, endpoint and Kähler-perturbation compatibility.
