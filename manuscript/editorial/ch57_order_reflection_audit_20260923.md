# Chapter 57: order reflection and rational valuation rays

Audit date: 23 September 2026.

## Mathematical changes

The order-reflection proof now works on the precise divisorial test set
of Chapter 32: positive rational multiples of prime orders, together
with the full-support trivial valuation. It no longer applies the
divisorial Legendre formula directly after an arbitrary real rescaling
of a valuation. The forward implication also explicitly uses BJ
divisorial domination to pass from the test set to all analytic points.

### Interior inversion and endpoints

The new lemma studies the profile f_v(tau)=-v(Gamma_tau) for tau<c,
where c is the terminal parameter. Generic Lelong numbers make this
profile finite, nonpositive, decreasing and concave. Its scalar dual
B_v(t)=sup_(sigma<c)(f_v(sigma)+t sigma) is finite for t>0: a fixed
interior parameter gives a finite lower bound, and tc is an upper bound.
It is therefore continuous on the positive half-line.

The limiting dual parameter t=0 is also checked. The inequalities
f_v(sigma_0)+t sigma_0 <= B_v(t) <= B_v(0)+tc give right continuity
at zero after taking the supremum over sigma_0. A supporting affine
function at any interior tau has slope -t with t>=0. If t=0,
positive t approaching zero recovers the same value. Thus the infimum
over t>0 recovers the interior profile, and continuity allows the
infimum to be taken over positive rational t. On these parameters,
B_v(t)=t Gamma^An(t^(-1)v) by homogeneity of each individual level.

The terminal level does not increase this supremum, because it lies
below every earlier level. In the order proof, comparison at v_triv
first orders the two terminal parameters. Inversion then compares the
interior profiles; the valuative multiplier-ideal criterion and the
normalized I-envelopes compare the interior potentials. Finally the
closed potential profiles of Chapter 52 recover their endpoints by
decreasing limits. This includes equal terminal parameters and
zero-mass terminal levels. No continuity of generic Lelong numbers
at a zero-mass endpoint is assumed, and no model-envelope argument
is applied there without checking its hypotheses.

### Why unscaled prime orders are insufficient

The new P1 example uses two Fubini--Study metrics of O(2):

- F=max(log|x^2|+1, log|xy|+1, log|y^2|);
- G=max(log|x^2|+1, log|y^2|).

With d=v(I_(x=0)), comaximality gives F=max(0,1-d) and
G=max(0,1-2d) on every semivaluation, including proper supports.
They agree at the trivial valuation and at every unscaled prime
order on the smooth curve: both are 0 at ord_(x=0) and 1 at every
other ord_q. At (1/2)ord_(x=0), however, their values are 1/2 and 0.
All sections have degree two, their common zero loci are empty, and
the weights are integers, so both are actual Fubini--Study metrics
in the same class. This is an explicit check that the rational
valuation rays used by the inversion proof cannot be omitted.

### Dependent operations proof

The rescaling identity is now proved by rescaling the test-curve
parameter, using (lambda Gamma)_tau=lambda Gamma_(tau/lambda).
This calculation is different from rescaling the valuation. For
irrational lambda, the extension is constructed as lambda Gamma^An
in the real numerical BJ class lambda c1(L), using BJ Theorem 4.7;
divisorial domination gives uniqueness. No general comparison theorem
for arbitrary transcendental classes is inferred from this argument.

The maximum identity retains the concavification and model projection
in the source operation. The arbitrary-supremum proof now uses finite
joins on the test-curve side and the least-upper-bound property of
the BJ usc envelope. The terminal-parameter bound supplies a uniform
upper bound on all analytic points via the maximum principle. The
order isomorphism then identifies the least upper bounds. A raw
levelwise supremum of an arbitrary family is not silently treated
as a concave test curve.

## Primary-source checks

- [Darvas--Xia--Zhang, published article](https://ems.press/journals/cmh/articles/14298510),
  Comment. Math. Helv. 100 (2025), 269--322: Theorem 3.12(i), page
  294, starts with positive rational scaling; Theorem 3.14, page
  297, passes to the pseudoeffective inverse system. The revised
  proof supplies the scalar continuity, inversion and endpoint steps.
  Lemma 2.1, pages 278--279, requires positive mass of the limiting
  model potential for its Lelong-number continuity statement; that
  hypothesis is not imposed on the terminal level in this proof.
- [Boucksom--Jonsson, published article](https://numdam.org/articles/10.5802/afst.1705/),
  Ann. Fac. Sci. Toulouse 31 (2022), 647--836: Theorem 4.7, page
  710, supplies real numerical scaling; Theorem 4.22 and Corollary
  4.23, page 715, supply divisorial domination and psh determination.
- [Xia, operations paper, arXiv version 3](https://arxiv.org/pdf/2312.17150v3),
  22 October 2024: Remark 3.3, page 9, is the potential-level closed
  endpoint convention; Corollary 4.8, page 14, is the divisorial
  maximum identity; Definition 4.12, page 16, uses finite joins for
  an arbitrary supremum; Definition 4.14 and Lemma 4.17, page 17,
  give parameter rescaling and the addition/rescaling identities.

Rendered source pages inspected in this unit: DXZ physical page 26
(printed 294), operations v3 pages 14 and 17. The other locators were
checked in primary-source text; BJ's statements were also read in
the preceding Gauss audit. No secondary source is used for these
theorem scopes.

The second local mathematical pass checked the supporting-line case
t=0, density of positive rationals, both directions of each order
inequality, equal and unequal terminal parameters, zero terminal mass,
the proper-support values in the example, the O(2) section degrees,
the real target class under rescaling, and the least-upper-bound
argument for arbitrary families.

## Validation and preservation

- Final full build: 3,941 pages, 18,737,162 bytes.
- Reference/structure audit: 389 TeX inputs and 11,566 unique labels;
  no missing inputs, duplicate labels, dangling references or
  structural errors.
- No unresolved references or citations and no horizontal or vertical
  overflow in the final log. Existing underfull-box and class-name
  warnings remain outside this unit.
- Strict style check of the complete changed lemma, proposition,
  example and operations theorem/proof: zero errors and zero warnings.
- Inventory passes: 46 active atoms in 14 environments, with tiers
  `(0,5,8,16,17)`; no research classification is changed.
- Final physical pages 3278--3280 and 3284--3285 (printed 3210--3212
  and 3216--3217) were visually checked. The inverse formula, endpoint
  argument, example and operations proof are legible and unclipped.
- `git diff --check` passes. Only Chapter 57 and the current progress
  records are included in this unit; the generated PDF is ignored.

SHA-256 records:

| File | SHA-256 |
| --- | --- |
| Chapter 57 before revision | `ff9b83be7e33b029118246d029ed120b7ee99adac4a5a9a0b7ea1414b8a6585f` |
| Final Chapter 57 | `c912710d6e0b3d9a2cb193a407f685b0d362444aaee5b9042babe6d2b484d2ee` |
| Final local book.pdf | `255864f85333bfdf4aab31706c5e274120baf873f3ed959ccfe29b3e96926f3b` |
| Preserved Chapter 56 | `8d9cd1f51c87deb1cac4743fd3237da0d268d5c533a8c78d92b395ad1e121959` |
| Published DXZ PDF | `467778ff37b893681482e43b4d8f1d717e947a34fe61026b2e6bc418e4a1f70e` |
| Published BJ PDF | `50bd6e6782c29088edc96d013a5d49257b0395d9fb398664f1a9859639992948` |
| Operations v3 PDF | `773eea71af9f1fff112bf5fcab2b9046b81467df2e37165ee1da3949ff74c6d9` |
| Both supplied and restored CURVE_PSH.tex | `9142aac73c5af7e4e715b3313def5ed56fae4e63e1ac8a53d0419df7d2194be9` |

The previously checked GF realization and trace-comparison portions
of Chapter 57 retain their exact bytes; this was checked against the
pre-edit file. Other chapters, frozen comparison interfaces, author
sources, production verifier records, research classifications and
dated release artifacts are preserved. These are local mathematical,
source, style, build and visual checks. No independent-agent or
production Rethlas verification, new research-atom closure or whole-book
completion is claimed.

The next bounded unit checks Chapter 57's decreasing-net comparison:
the uniform positive-mass bound in a common larger class, the exact
Lelong-continuity hypotheses, and compactness of maximizing parameters
before any Legendre supremum/infimum interchange. The terminal
noncollapse condition and distinction from volume continuity remain
explicit.
