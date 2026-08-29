# Exact-byte hostile audit: revised arbitrary-valuation variation graph

Date: 29 August 2026

Verdict: **PASS**.

- Critical errors: **0**.
- Mathematical gaps: **0**.
- Citation mismatches: **0**.
- Counterexamples found: **0**.

This is an independent hostile audit of quarantined candidate bytes.  It is not
a production-verification receipt, does not authorize a live-book edit or
open-problem retirement, and makes no novelty or priority claim.  Neither the
statement nor the proof was edited during this audit.

## Exact bytes audited

- revised statement,
  `p213_variation_graph_arbitrary_curve_statement_revised_20260829.tex`:
  `8c736e3df2df1efd7b6925dd4edccddfcf03cc1ee0b68250bd1219f80169be5a`;
- revised proof,
  `p213_variation_graph_arbitrary_curve_proof_revised_20260829.tex`:
  `9cb4d5eef1370ef97ccf1fa51e9ece16ab418c44092df61bd1a403f3f1d99ed9`;
- revised compile harness:
  `8bf258fbc4044a654269359df965461df14dbb0544570be0c2ea4d0ce68e1f3c`.

The archived first production response was read in full.  Its SHA-256 is
`cc33b2fc9a396717e7e633b337b5b43e63ebb1a8802b8df2e6d6c2b2f5c083c4`;
it returned `wrong`, with one critical slope-normalization error and three
gaps concerning the global target tube, mixed branch coefficients, and the
normalization-locus assertion.  The revised bytes remove or repair each of
those points as checked below.

## Hostile mathematical checks

1. **Normalized slope versus metric dilation.**  Ducros 4.5.21.4 defines
   `dlog_b|f|=epsilon*r*[s(b):K]`, with `r` the canonical-graph metric
   dilation.  The revision consistently uses the integral vector
   `n_b=(-dlog_b|f_j|)_j`; the source metric derivative is
   `n_b/[s(b):K]`.  Thus the factor missed in the rejected proof is present
   and is never conflated with `r`.

2. **The branch divisor `d_P`.**  For a norm-one lift of a residual
   uniformizer, `d_P=-dlog_{b_P}|s_P|` is positive.  Ducros 4.2.11.1 gives
   the composite primary/secondary branch valuation, while 4.2.6 applied to
   a secondary-value-zero quotient and its inverse makes its modulus constant
   on a short branch section.  Hence
   `-dlog_{b_P}|g_hat|=d_P ord_P(g)` and every analytic-unit slope on that
   branch is divisible by `d_P`.  Retaining an order-one residual coordinate
   therefore gives `q_{b_P}=d_P`, not an unproved saturation index.

3. **Finite source-ray separation.**  The jet constructions are valid on the
   projective normal integral residual curve over its actual constant field;
   neither geometric integrality nor a rational point is used.  The
   `r_i`-block gives the selected primitive ray the block `(e_i,0)`.  The
   collision-killer has last coordinate one at every zero or pole introduced
   by the `r_i`, while any further zero or pole has zero `r_i`-block and
   nonzero last coordinate.  All remaining active branches have zero separator
   block.  These cases exhaust the source rays and prove pairwise separation
   of every `F_0`-active branch.  The type--3 argument correctly uses the two
   opposite normalized slopes.  If the type--2 active set is empty, taking the
   separator block empty is legitimate: separation is vacuous, the moment is
   locally constant near the node, and the source-cutoff construction below
   still gives the asserted zero target germ.

4. **Compact source cutoff and germwise closedness.**  After shrinking, the
   complete finite variation graph inside the source neighborhood is a star
   and every active arm is integral-affine and injective.  The transition set
   of the compactly supported cutoff misses the centre.  Its intersection with
   the variation graph has compact tropical image away from the target vertex;
   off the variation graph the entire moment is locally constant, so every
   positive-degree target test form pulls back to zero.  The two terms
   `F_*(d'chi wedge T)` and `F_*(d''chi wedge T)` consequently vanish on a
   target germ.  CLD 7.1.11 applies because `chi T` has compact support.

5. **No remote-sheet mixing.**  The current is localized on the source before
   pushforward.  Its support lies inside the chosen source star, so sheets
   outside that star do not enter the pushforward.  Inside the star, the
   separator block gives the selected target ray germ exactly one active
   source arm.  Constant complementary components contribute nothing to a
   bidimension-`(1,1)` target current.  The revised proof therefore needs and
   asserts no global target tube and no exact global ray preimage.

6. **Euclidean graph current.**  Positivity gives an order-zero symmetric
   positive-semidefinite matrix of Radon measures.  Normal first-jet tests in
   the column-divergence equations kill all normal rows and columns on an edge;
   tangential divergence makes the remaining density constant and
   nonnegative.  At a vertex, the atomic positive-semidefinite matrix is
   killed by arbitrary gradient jets, and arbitrary value jets then impose
   primitive-vector balancing.  There is no hidden vertex current.

7. **Canonical integration coefficient.**  For primitive target tangent
   `u_b=n_b/q_b`, an integral character with value one on `u_b` has normalized
   branch slope `q_b`.  Ducros 4.5.21.4 identifies that slope with the branch
   degree after the invariant perfect-closure/reduction passage.  CLD
   Proposition 14.3.1 and Section 14.3.2 use exactly this degree in the
   canonical calibration.  Thus the coefficient of the pushed-forward
   integration current is exactly `q_b`.

8. **Common-moment expansion ratios.**  If `H` concatenates moments and `A`
   projects to `F`, then `A n_b(H)=n_b(F)` and
   `A u_b(H)=m u_b(F)` with the integer
   `m=q_b(F)/q_b(H)>0`.  Direct integral-edge parametrization gives
   `A_*[u_b(H)]=m[u_b(F)]`.  Functoriality therefore multiplies the arbitrary
   current coefficient and the canonical coefficient by the same `m`.
   The ratio `t_b/q_b` is independent of moment and, by the compact
   source-germ argument, independent of cutoff.

9. **Divisor functionals and Riemann--Roch.**  In the common separating
   moment used for a rational function `g`, the uniformizer coordinate makes
   `q_{b_P}=d_P` and the primitive `g`-coordinate is `ord_P(g)`.  Target
   balance therefore annihilates principal divisors for
   `L_T([P])=a_Pd_P`; the normalized node relation does the same for
   `L_Y([P])=d_P`.  The stated Riemann--Roch argument is valid over the actual
   constant field: for a degree-zero divisor `D`, one fixed sufficiently
   positive `A` makes `A+nD` linearly equivalent to an effective divisor for
   every positive and negative integer `n`, forcing `L(D)=0`.  Hence both
   functionals are multiples of degree, `d_P=c_Y deg(P)` with `c_Y>0`, and all
   branch ratios at a type--2 point coincide.

10. **Local-to-global current equality.**  An ordinary compactly supported
    `(1,1)`-form is presented by a finite moment.  After appending the
    separator and localizing by the source cutoff, all `F_0`-active edges have
    the common node ratio; separator-only edges have zero `F_0` tangent and do
    not pair with the form; the Euclidean lemma excludes vertex mass.  This
    proves the local current identity.  Equality of the intrinsic ratio along
    overlapping edge germs and convex path-connectedness of the type--`2/3`
    core make the constant global.  CLD Proposition 15.2.1(a) places the
    support of every ordinary curve `(1,1)`-form in that core, so a finite
    smooth partition on compact support proves global equality.

11. **Dichotomy and example.**  The revision deletes the unsupported
    normalization equivalence.  Ducros 3.1.11 makes the quasi-smooth locus
    Zariski open.  When nonempty, its complement on an irreducible curve is
    zero-dimensional; on every strict affinoid it is finite and the strict
    affinoid Nullstellensatz makes its points rigid, hence it is locally
    finite.  At interior points Ducros 3.1.11.4 identifies quasi-smoothness
    with rig-smoothness.  For
    `K=F_p((t))`, `L=K(t^(1/p))`, the module
    `Omega^1_{L[T]/K}` has the independent generators `d(t^(1/p))` and `dT`
    because the inseparable equation has zero differential in characteristic
    `p`; every fibre therefore has differential dimension two while the
    analytic local dimension is one.  The displayed normal curve is indeed
    nowhere quasi-smooth and contains nonrigid Gauss points.

## Exact source and compilation check

The exact text sources inspected have SHA-256 values

- `CLD25.txt`:
  `24920a1f4c8bd4944c83d89c8747c95b0206ae0754053eb0ed4d3de95e0f7727`;
- `Ducros24CurveStructure.txt`:
  `7707c5384c328933e1aec337135fee4867527b58b0097ca16dcecb7685e07e19`.

The cited passages were checked directly: Ducros 3.1.11, 3.1.11.4, 3.3.5.2,
3.5.1, 4.2.6, 4.2.10, 4.2.11.1--2, 4.2.18, 4.5.11,
4.5.21.1--4, and 4.5.22; CLD 7.1.11, Proposition 7.2.9,
Definition 8.6.2, Example 8.6.4, Proposition 14.3.1, Section 14.3.2,
Proposition 15.1.1(b), Proposition 15.2.1(a), and Corollary 15.2.5.
All cited assertions match their uses and hypotheses.

An independent clean-directory `latexmk` build produced a ten-page PDF with
no TeX error, no undefined citation, and no undefined reference.  The final
log contains only four overfull-box warnings, all typographical and none
mathematical.

**Final disposition: PASS; 0 critical errors, 0 mathematical gaps, and
0 citation mismatches on the exact revised statement and proof hashes above.**
