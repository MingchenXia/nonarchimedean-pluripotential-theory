# Chapter 54: construction and independence of the analytic trace

Audit date: 23 September 2026.

## Scope and mathematical correction

Theorem 54.5.1 now has a proof with an explicit common target background.
The former introduction described the positive-mass part of the d_S space
as complete without stating the uniform positive lower mass bound required
by the cited completeness theorem. The revised text records that hypothesis
before using it.

For a quasi-equisingular approximation phi_j, write rho for the
normalization map followed by inclusion and r_j = rho^* phi_j.
The ambient lower curvature bounds admit one Kähler form Omega with
Omega + ddc phi_j >= 0 for every j. On the normalization choose an
intrinsic Kähler form kappa and set Theta = rho^* Omega + kappa.
The proof checks

    Theta + ddc r_j >= kappa,
    integral <(Theta + ddc r_j)^m> >= integral kappa^m > 0.

The lower bound is independent of j. The analytic pole sets and the
singular locus of the normalization have zero smooth volume, so the
purely smooth term in the non-pluripolar expansion is retained.
The pullback rho^* Omega is only used as a semipositive form;
the intrinsic summand kappa supplies strict positivity.

Generic Lelong number zero makes every analytic restriction nontrivial.
The approximation convention now includes decreasing convergence,
uniform curvature bounds and the precise multiplier-ideal inclusion.
The dimension-zero case is treated separately: restrictions of the
approximants are finite constants, all with zero d_S-distance, even
when the original function takes the value -infinity at that point.

Existence is obtained from the decreasing normalized model envelopes
P_Theta[r_j] and their uniform mass bound. It is not inferred from
pointwise convergence of r_j, whose pointwise limit can be identically
-infinity.

For two approximations, existence is proved first for each one in the
same background. Quasi-equisingular comparison then gives indices
k(j) >= j tending to infinity and

    r_k(j) <= (1-eta_j) s_j + C_j,   eta_j -> 0.

Restriction preserves the additive comparison constants. The scaling
bound d_S(s_j,(1-eta_j)s_j) <= C eta_j has C depending only on the
fixed target and background. Closedness of P-order in d_S yields one
order between the limits; reversing the roles gives P-equivalence.
This proof does not assume that the maximum of two independently
chosen analytic approximants has a common analytic coefficient.

Positive-mass d_S closure gives I-goodness. Change of background is
justified by the exact convergence theorem. Equality of the ambient
multiplier ideals at the dyadic scales gives equal canonical
restricted singularity types at every stage, proving dependence on
the ambient I-class. The finer output P-class is retained.

The second mathematical pass checked the direction of singularity
comparison, the cofinal subsequence, every uniformity dependency,
the zero-dimensional case, source/target positivity, and the use of
positive mass before invoking analytic closure.
It also made the second input's membership in D_Y explicit.
The neighboring calculus statement is kept with its formulas, and its
reference to the preceding proof now describes diagonal approximation
comparison rather than an unspecified uniform restriction estimate.

## Primary sources and their scope

The supplied chapter_trace.tex, chapter_pshfunctions.tex and
chapter_comp.tex were read without alteration. Numbered locators were
checked against the author's
[final lecture manuscript](https://mingchenxia.github.io/Lectures/SGPT_final.pdf),
dated 18 July 2026:

- Definition 1.6.4 and Theorem 1.6.2, page 33: approximation convention
  and the canonical dyadic multiplier-ideal types.
- Proposition 1.6.3, page 34: comparison of two approximations with
  an arbitrarily small loss in the coefficient.
- Proposition 6.2.2, page 208: zero d_S-distance and P-equivalence.
- Corollary 6.2.7, pages 215--216: completeness with a uniform mass
  bound and the decreasing model-envelope construction.
- Lemma 6.2.3, pages 216--217: the uniform small-scaling estimate.
- Corollary 6.2.9, pages 221--222: change of background.
- Proposition 6.2.5, page 225: closedness of P-order.
- Theorem 7.1.1, pages 234--235: analytic closure and I-goodness.
- Propositions 8.1.1--8.1.2, pages 259--261, and Proposition 8.2.1,
  pages 263--264: independence, I-goodness and input I-class dependence.
- Appendix B.3, pages 504--505: the normal/unibranch target calculus.
  This does not provide ambient Demailly regularization on a general
  singular space; the ambient manifold remains smooth.

Physical source pages 49--50, 231--232, 237, 241, 250, 275, 277, 279
and 521 were rendered and inspected. The remaining locators were
checked in the source text.

The accepted manuscript
[Darvas--Xia, arXiv:2403.08259v2](https://arxiv.org/abs/2403.08259v2),
13 March 2026, was downloaded and checked independently of the lecture
pagination. Definition 3.1 and Lemmas 3.2--3.4, pages 10--12, concern
a smooth submanifold and the fixed-background construction under a
Kähler-current lower bound. Those pages were rendered and inspected.
They are cited through the separate key DXTraceV2.
The existing DX24 entry is unchanged; locators elsewhere in the book
have not been silently reassigned to another edition.

The author's current publication list and DOI metadata identify the
published paper in Transactions of the American Mathematical Society,
2026, [DOI 10.1090/tran/9785](https://doi.org/10.1090/tran/9785).
The journal full text and MathSciNet record were unavailable through
the attempted access paths. The new citation therefore explicitly
identifies the accepted arXiv version actually checked, rather than
claiming to have checked published pagination.

## Validation and preservation

The final full build succeeds with 3,935 pages and
18,685,291 bytes. The 389-file TeX closure has 11,536 unique
labels, with no missing input, duplicate label, dangling reference or
structural defect. The final log has no unresolved references or
citations and no horizontal or vertical overflows; the pre-existing
class-name warning remains.

The actual edited prose and proof pass the strict writing audit with
zero errors and zero warnings. Physical pages 3225--3231 and the new
bibliography entry on page 3929 were rendered and inspected after the
second pass. After the final layout repair, pages 3225--3227 and 3929
match the inspected rasters byte for byte; pages 3228--3231 were
re-inspected. The adjacent calculus statement and its formulas remain
on one page, and the next section opens with its theorem.

The active inventory remains 46 atoms in 14 formal environments,
with tiers (0,5,8,16,17).

PDF SHA-256: 6c2d5ea998af71c63fb6062e77ec9ca28577d4cb1e54af8103ce8ca83dff70fa

Chapter 54 SHA-256: 7bf5f12d2ca804a666ab25df60ec9ebc91c4974b0633d173801a4de94a0e69b3

Both CURVE_PSH.tex copies retain SHA-256
9142aac73c5af7e4e715b3313def5ed56fae4e63e1ac8a53d0419df7d2194be9.
Chapter 62 retains SHA-256
3e868c8797ca563a1654e46bdd704272188bfce54edb9639d909434f1d7fff36.

Source PDF SHA-256:
c816eea5f06822021fa8dd75b70f82724ee47e6dcd6830729f5ecc109296b706

Accepted trace-paper PDF SHA-256:
5d6f43d96be101f6aa1a3ddbdd92b5bc49131a0deabbf199e03111d6c0fbaa3c

Read-only author-source SHA-256 values:

- chapter_trace.tex: d51549235a0fc017197d47f71cd6faf21a1c607ce11895da3f31f7f621774d9f
- chapter_pshfunctions.tex: 22718016825490fb84d8f53af1c3b5214cfb6765a31f6d570dbb8a59a3fba34b
- chapter_comp.tex: c8cb2b9c6cbcc9a1b6965f23802eaed6891fcc23b965163a37a227e53497f7cb

Only Chapter 54, its new version-specific bibliography entry, and
current editorial progress records were changed. Supplied author
sources, both CURVE_PSH.tex copies, frozen proof packets, production
verifier records, research classifications and dated release artifacts
were preserved. The current PDF is an ignored local build artifact.
This is a local mathematical/source/style/build/visual audit, not an
independent-agent or production Rethlas verification.
No research-frontier theorem or atom closure is claimed.

The next bounded audit concerns the analytic trace calculus:
compatible approximations for sums, positive real scaling and maxima,
and the exact I-goodness, common-class and convergence hypotheses in
the sequential and net continuity statements.
