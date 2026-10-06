# Finite generation, common fans and the base-locus erratum

Source-only checkpoint, 6 October 2026. Baseline work commit:
`fd92cb712fb91916102a44cef5cebd4e3d78dd12`; main:
`00957114db21b627e97369563032ceda9cea09c7`.

The complete seven-page [ELMNP erratum, 2309.16722v1](https://arxiv.org/abs/2309.16722v1),
submitted 20 September 2023 at 22:21:25 UTC, and the complete
[published original](https://aif.centre-mersenne.org/articles/10.5802/aif.2225/)
were read as full extracted text and displayed as original page images.
The original PDF has 35 physical pages: a publisher cover and printed
pages 1701--1734. Thus the fresh reading is **42 physical pages in 22
sheets**, including covers, references and addresses. The erratum repairs
the proof of Proposition 4.7; it does not announce a counterexample to
that proposition or invalidate the independent definitions in Section 1.

## Corrected result and quantifiers

The controlling statement is erratum Proposition 1.1. Its category is an
integral reduced variety of finite type over an algebraically closed field
of arbitrary characteristic. Let N be a finite-rank free abelian group,
S a finitely generated saturated subsemigroup, C its real cone, and
a_m a coherent S-graded ideal system with a_0=O_X. Assume its sheaf of
Rees algebras is finitely generated over O_X.

There exists a smooth fan Delta with support C such that **for every
smooth refinement Delta' there exists a positive integer d** satisfying,
on each cone of Delta' with primitive ray basis e_1,...,e_s,

    overline(a_{d sum_i p_i e_i})
       = overline(product_i a_{d e_i}^{p_i}),  p_i >= 0 integral.

The integer is chosen for the selected refinement. Smoothness gives
integral nonnegative ray coordinates. Both integral-closure bars are
essential; an equality of unclosed ideals is not the imported conclusion.
The source's initial reduction to the saturated nonzero support and its
trivial zero-ideal cones are retained. No asymptotic valuation is assigned
a finite value by taking an infimum over an empty set.

The original induction does not establish termination when refining
codimension-one cones introduces new codimension-one cones. The
replacement avoids that recursion through a common fan for **all** cost
vectors, hence for all centered discrete valuations simultaneously.

## Linear programming and the valuation chain

Erratum Lemma 2.1 fixes rational generators v_i and permits arbitrary
nonnegative real costs alpha_i. For a rational vector v in C,

    phi_alpha(v) = min {sum_i lambda_i alpha_i:
                       lambda_i in Q_>=0, sum_i lambda_i v_i=v}.

The rational feasible polyhedron gives an attained rational optimizer
even when the costs are irrational. Allowing real lambda does not change
the value on rational v. The resulting function is homogeneous and
subadditive, hence convex. Linear-programming duality gives the support
function of Q(alpha)={gamma:<v_i,gamma><=alpha_i}.

For strictly positive costs Q(alpha) is full-dimensional, with the origin
in its interior. Its normal fan has support C; its rays come from the
fixed finite list of nonzero v_i. There are finitely many such fans, and
their common refinement works independently of alpha. Continuity in the
cost vector extends the conclusion to alpha_i=0. The argument allows
lower-dimensional C and uses strongly convex cones in the fan. This is
the normal-fan proof, independent of the two misprints in Remark 2.3.

Finite generation supplies finitely many generating degrees m_i over a
finite affine cover. For a centered discrete valuation nu, their costs
nu(a_{m_i}) are finite and nonnegative. The asymptotic order on the
nonzero support equals the above minimum with v_i=m_i. Each ray's
one-dimensional Rees algebra is finitely generated; a suitable Veronese
gives exact powers along that ray. After selecting the smooth fan, take
d to be a common multiple of these finitely many **ray** integers. For
m=sum p_i e_i the source proof becomes

    nu(a_{dm}) <= sum p_i nu(a_{de_i})
                = sum p_i nu_a(de_i) = nu_a(dm) <= nu(a_{dm}).

The product inclusion has degree dm. Equality for every centered
discrete valuation yields equality of integral closures by
Swanson--Huneke Proposition 6.8.2. One need not choose d simultaneously
for every lattice vector m. The original Lemma 4.8 was read for the
finite generation of the ray subalgebra. The cited Bourbaki Veronese
proposition, Ewald smooth-refinement theorem and Barvinok duality theorem
remain standard imported antecedents; their exact editions were not
freshly read here, and the full external chain is not certified.

## Thirteen source diagnostics

The frozen diagnostic record has thirteen entries: the acknowledged
inductive gap, nine literal formula/scope errors, and three guards on
attainment, ambient category and historical open questions. These are
source diagnostics, not new book theorems or independent model receipts.

| ID | Exact source | Finding and retained boundary |
| --- | --- | --- |
| D01 | Original Proposition 4.7; erratum p.1 | Termination of the old induction was not established; the corrected proof replaces it. |
| D02 | Erratum Remark 2.3, p.4 | The printed scalar relation sum b_i lambda_i=0 must be the vector relation sum b_i v_i=0. With v_i=e_i, lambda=(1,1), b=(1,-1), the printed scalar relation changes target (1,1) to (0,2). |
| D03 | Erratum Remark 2.3, p.4 | Outside the support of the relation, keep lambda_i instead of setting it to zero. For v=(e_1,e_2,e_1), lambda=(1,1,1), b=(1,0,-1), the printed update loses the e_2 coordinate. |
| D04 | Erratum p.6 after (7) | The product lies in a_{dm}, not a_m. The finitely generated example a_even=R, a_odd=(x) in k[x], with d=2, disproves only the printed unscaled inclusion. The displayed valuation chain has the correct degree. |
| D05 | Original Example 1.11, physical p.9 / printed p.1708 | Supp(N), not Supp(E), lies in Null(P). On P^2, D=2H=A+E with A=E=H and N=0 disproves the printed containment. The surface identity survives. |
| D06 | Original Definition 2.9, physical p.17 / printed p.1716 | A nontrivial discrete valuation requires a proper center. The generic center X would force its valuation ring to be k(X). Big-divisor base-locus applications use proper centers. |
| D07 | Original Proposition 3.1 proof, physical p.20 / printed p.1719 | Its second displayed equality must be <=. On x+y>0, f=max(0,-y), x_1=(39/10,-1), x_2=(4,-1), the two values are 1 and 11/10. The required inequality follows from the zero-valued basis and subadditivity. |
| D08 | Original Lemma 3.3, physical p.21 / printed p.1720 | Preserve the displayed infimum; the prose word minimum alone does not establish attainment. No nonattainment counterexample is claimed. |
| D09 | Original physical p.25 / printed p.1724; Example 1.27 | The assertion about no isolated unstable rays/section points lacks a dimension restriction. On Bl_P(P^2), the positive H ray is the only unstable ray inside the big cone; its section point is isolated. The source's own example supplies this check. |
| D10 | Original physical p.32 / printed p.1731, before (4.3) | Distinguish zero and unit base ideals. A basepoint-free O(1) on P^1 has volume one; the printed rule assigning zero moving intersection to b=O_X would give zero. Use the zero ideal for the no-sections case. |
| D11 | Original physical p.33 / printed p.1732, Proposition 4.13 | The ray subscript in (dagger) must use d e_i, consistently with its following resolution; the grading quantifier is N^r, not N^n. Keep both closure bars. |
| D12 | Original Proposition 4.7 versus erratum setup | The corrected proof explicitly treats varieties. It does not by itself certify the original parenthetical arbitrary-Noetherian-scheme scope; that broader statement is not refuted here. |
| D13 | Original Remark 1.13, physical p.10 / printed p.1709 | A question open in 2006 is not automatically current. No new canonical problem is inferred from the historical wording. |

The two Remark 2.3 failures have separate rational witnesses: the first
violates the vector constraint, and the second still fails with a valid
vector relation. Retaining untouched coordinates repairs that reduction.
The independent normal-fan proof and corrected Proposition 1.1 are not
refuted. The original irrational example in Section 3 remains a warning
against dropping finite generation; no universal polyhedral conclusion
is inferred for arbitrary graded systems.

## Reused dependencies and current book usage

The exact Swanson--Huneke author PDF has 463 pages and SHA-256
`a12705f066aee67648768bc37b58a37c661907dc3918a71974c1441bc551a18b`.
Its title page and physical pages 153--156 were reread and displayed in
three sheets. They were already read in the
[Appendices A--C audit](appendices_ABC_quality_audit_20261002.md), so
these are five reused pages and zero fresh unique pages. Proposition
6.8.2 and Theorem 6.8.3 allow rank-one discrete valuations for Noetherian
domains/rings; Proposition 6.8.10 preserves an ideal's valuation under
integral closure. No full-book reading is claimed.

Eleven previously read actual PDF pages of restricted-volumes
`math/0607221v2` are reused: 1 and 6--15. That prior record distinguishes
actual PDF reading from incomplete extracted-text rereading. It is not
a fresh full-text reading of this 38-page preprint or of the distinct
2009 journal edition. Together, dependencies contribute sixteen reused
physical pages; the review's total source coverage is 58 unique selected
physical pages, of which 42 are fresh.

Chapter 40's off-base-locus remark uses the augmented base locus and the
BJ addendum off-locus equality, and explicitly keeps this route separate
from its main smooth proof. Original Definition 1.2 and Proposition 1.5
were read in Section 1 and are independent of Proposition 4.7's corrected
induction. Chapter 46 cites restricted-volumes v2 Definition 2.6 and
Theorem 2.13 in its dominated Fujita discussion. This is a separate
paper and interface; it is not the faulty old Proposition 4.7 proof.
Chapter 27's restricted-volume imports are also distinguished from the
2006 finite-generation proposition.

## Preservation and continuation

All 425 active inputs, both bibliography files, fourteen generated book
files, 108 protected verification/status inputs, 76 prior frozen
manifests and 133 exports are byte-preserved. The preceding 4,407-page
book and its source package remain the current edition. No fresh book
build or book-page review is claimed for this source-only checkpoint.
The open native catalogue source, PDF and editor are untouched; no
native compilation is needed. The canonical inventory stays at 42
atoms in twelve families, with statuses 0/3/7/15/17. General
non-Archimedean Siu/closure remains conditional at the existing BJ22
proof boundary.

The next scoped integration is an attributed finite-generation
discussion near Appendix C's graded ideals, with the common fan,
Veronese choice and integral-closure boundary explicit, and an Appendix
L source note. It will not turn arbitrary envelope algebras into
finitely generated ones or resolve a canonical open problem. Routine
fetches of main and work found no incoming commits; work-branch
publication uses the standing authorization and existing platform checks.
