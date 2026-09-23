# Chapter 57: decreasing nets and the Legendre limit

Audit date: 23 September 2026.

## Mathematical repair

The previous proof asserted that the componentwise infimum was legitimate
because the individual interior levels had positive mass. That does not
by itself establish positive mass of their limit. The revised proof uses
the bound already proved in Chapter 54, Proposition
`prop:operations-inf-positive-mass`: at each fixed Kähler perturbation
omega and each parameter below the limiting cutoff, the limiting mass
is at least 2^(-n) integral_X omega^n. Its proof uses the compatible
component at half the perturbation. This establishes the hypothesis
before either decreasing-envelope or Lelong-continuity is applied.

The rest of the proof is reconstructed in three stages.

1. For a fixed interior parameter, the decreasing net of model
   potentials admits a countable subfamily with the same pointwise
   infimum. For each rational b, the open sublevel sets {u_i<b}
   cover {inf_i u_i<b}; second countability gives a countable subcover.
   Directed upper bounds produce a decreasing sequence with the same
   infimum. The positive-mass sequential Lelong theorem applies, and
   monotonicity sandwiches the whole net between this sequence and
   the limiting Lelong number. No countable cofinal subset of the
   original index set is assumed.
2. At a fixed divisorial valuation, let c_i decrease to the finite
   cutoff c, and let f_i be the nonpositive decreasing parameter
   profiles. For r below the limiting Legendre supremum, approximate
   maximizing parameters lie in [r,c_i0] on one cofinal tail. A
   convergent subnet has limit tau_*<=c. Testing at each sigma<tau_*
   uses only the already proved interior convergence. Letting sigma
   approach tau_* gives the reverse inequality for the Legendre
   supremum. This also handles tau_*=c without assuming Lelong
   continuity or positive mass at the terminal level.
3. The BJ decreasing limit is generically finite because its value
   at the trivial valuation is c. BJ closure and divisorial
   determination then give equality on all analytic points, including
   proper-support points where the limit can be minus infinity.

The scalar argument proves the needed limit directly for arbitrary
directed sets, rather than importing a general conjugacy statement
without checking its endpoint and compactness conditions. Surjectivity
of the later comparison theorem is not used.

## Explicit examples and second pass

The constant-curve example now computes its analytification from the
Legendre formula on all divisorial valuations, then uses divisorial
determination. The trivial-valuation identity alone would not show
that the function is constant. All nontrivial levels have full mass,
while endpoints tending to minus infinity make both presentations
collapse. Its prose was shortened and its statement now stays together
in the final layout.

For the decreasing P1 family already constructed in Chapter 54, set
d=v(I_p) and 0<a<1. The new worked calculation gives

    (Gamma^j)^An(v) = max(-a d,-j) decreasing to -a d.

The Legendre objective is affine on [-j,0] and equals its parameter
below -j, so its maximum is attained at -j or zero. Positivity in
the common O(1) class is checked by scaling the divisor metric,
adding the zero metric in the complementary positive class, and
taking a finite maximum. The formula extends by divisorial
determination. At the proper-support point p the values are -j;
at the trivial valuation they are all zero. The limiting function
is thus a legitimate, possibly infinite-valued psh metric. The
previous mass calculation gives volumes 1 and limiting volume 1-a,
so pointwise decreasing comparison is explicitly separated from
decreasing volume continuity.

The second local mathematical pass checked the countable selection,
directed upper bounds, both Lelong inequalities, cofinality of the
compactness subnet, equal limiting and maximizing endpoints, the
zero-mass terminal case, and the example at d=0, finite d and d=infinity.
It also made the complementary-class positivity calculation explicit.

## Exact primary-source inputs

- [Darvas--Xia--Zhang, published paper](https://ems.press/journals/cmh/articles/14298510),
  Comment. Math. Helv. 100 (2025), 269--322: Lemma 2.1, pages
  278--279, requires a decreasing sequence of model potentials
  whose limit has positive mass. The countable selection in the
  revised proof explains its application to the whole net.
- [Xia, operations paper, version 3](https://arxiv.org/pdf/2312.17150v3),
  22 October 2024: Proposition 2.8, pages 5--6, is the
  decreasing-envelope identity with positive mass of the infimum;
  Definition 4.9 and Lemma 4.10, page 15, give the inverse-system
  decreasing infimum, its endpoint and divisorial comparison.
  These locators use the explicitly versioned bibliography entry.
- [Boucksom--Jonsson, published paper](https://numdam.org/articles/10.5802/afst.1705/),
  Ann. Fac. Sci. Toulouse 31 (2022), 647--836: property (PSH2),
  page 706, and Theorem 4.5, pages 708--709, give closure under
  decreasing nets with generically finite limit. Theorem 4.7,
  page 710, supplies sums, positive scaling and finite maxima;
  Theorem 4.22 and Corollary 4.23, page 715, give divisorial
  domination and determination.

The primary-source text was checked at these locators. Rendered source
pages additionally inspected: DXZ physical page 10 (printed 278),
operations v3 page 15 and BJ physical page 63 (printed 708).

## Validation and preservation

- Full build after the second pass: 3,943 pages, 18,743,195 bytes.
- Reference and structure audit: 389 TeX inputs, 11,569 unique labels;
  no missing input, duplicate label, dangling reference or structure error.
- Final log: no unresolved reference or citation, no horizontal or
  vertical overflow. Existing underfull-box and class-name warnings
  remain outside this unit.
- The complete decreasing-limits section passes the strict writing
  audit with zero errors and zero warnings.
- Research inventory: 46 active atoms in 14 environments, tiers
  `(0,5,8,16,17)`, unchanged.
- Final physical pages 3282--3285 (printed 3214--3217) were rendered
  and visually checked, including the following comparison theorem.
- `git diff --check` passes. All Chapter 57 bytes before and after
  the decreasing-limits section match the preceding committed source.
  This preserves the checked order-reflection, GF realization,
  operations and trace-comparison blocks.

SHA-256 records:

| File | SHA-256 |
| --- | --- |
| Chapter 57 before revision | `c912710d6e0b3d9a2cb193a407f685b0d362444aaee5b9042babe6d2b484d2ee` |
| Final Chapter 57 | `8b1e66073d3263655e04000136e4f0dc74ed9894129d4435998a64d22fab1bda` |
| Final local book.pdf | `c5485c68e2ed6b1bbf7404c9835fc41688c1ff1b42b86c43782e3cfe72db46a1` |
| Published DXZ PDF | `467778ff37b893681482e43b4d8f1d717e947a34fe61026b2e6bc418e4a1f70e` |
| Published BJ PDF | `50bd6e6782c29088edc96d013a5d49257b0395d9fb398664f1a9859639992948` |
| Operations v3 PDF | `773eea71af9f1fff112bf5fcab2b9046b81467df2e37165ee1da3949ff74c6d9` |

Only Chapter 57 and current progress records change. Other chapters,
author sources, frozen proof packets, production verifier responses,
research classifications and dated release artifacts are preserved;
the generated PDF remains ignored. These are local mathematical,
source, style, build and visual checks. No independent-agent or
production verification, research-atom closure or whole-book completion
is claimed.

The next bounded unit checks Chapter 58's support and center construction:
the exact sheaf-theoretic finite-generation input, the meaning of prime
coherent ideals, and the descent to the support and local point criteria.
This will be checked against the exact Mesquita-Piccione source before
altering any statement.
