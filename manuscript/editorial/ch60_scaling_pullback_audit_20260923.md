# Chapter 60: rational scaling and finite pullback

Date: 23 September 2026.
Baseline: `143d22995184d555a969f6dabb980610475763b1`.
Scope: the scaling action, the non-maximum parts of
`prop:mp-model-psh-stability`, and two worked examples immediately after
its proof. The earlier model definitions, the entire maximum argument,
and all text from `thm:mp-model-closedness` onward retain their baseline
bytes. No research question is promoted or retired.

## Mathematical reconstruction

The previous proof passed from integer base change to rational scaling in
one sentence, without first constructing a PL representative of the rationally
scaled function. Its final pullback sentence did not specify the domain
manifold or construct a model above the source. The revised proof supplies
those steps and the positivity needed to remain in the chapter's Kähler
category.

1. **PL construction before nef descent.** For q=a/b>0 and a generator
   m^(-1) max_j(log|a_j|+k_j), the scaled function is
   (bm)^(-1) max_j(log|a_j^b|+a k_j). The unit-sum condition is preserved
   under these ideal powers, so the maximum stays finite on every character,
   including proper-support characters. Linearity, the composition law and
   the reciprocal action give an automorphism of PL and its real span for
   rational q. The action on valuations fixes the trivial valuation; its
   action on functions multiplies the value there by q.
2. **Integral base change and its normalization.** The reduced main
   component of the base change t=s^m is normalized and resolved equivariantly.
   It is projective over X times P1, compact Kähler, and a product away from
   the central fibre. A fractional flag sum a_j t^(lambda_j) pulls back to
   sum a_j s^(m lambda_j), proving the potential formula on the whole spectrum.
   The background remains alpha because the map on X is the identity.
3. **Reflection of nefness after resolution.** The resulting map is proper
   and surjective but need not be finite. Pullback of almost-semipositive
   smooth representatives proves preservation. For reflection, each cycle Z
   in a downstairs central component is dominated by a component of its full
   inverse image. After resolution, the pushforward of a suitable power of a
   Kähler form is c[Z], c>0. Projection formula and the nef class upstairs
   give all Demailly–Păun linear tests downstairs. The finite-union criterion
   and the unchanged noncentral fibres finish the argument. The zero-dimensional
   case requires no positive-dimensional test. Model independence then proves
   chi is alpha-psh if and only if m·chi is alpha-psh.
4. **Rational descent.** The PL function chi=(a/b)·phi already has a model
   by item 1 and the PL/Cartier correspondence. The identity
   b·chi=a·phi, integer preservation and integer reflection imply relative
   nefness of chi. This does not assume the conclusion in constructing the
   downstairs representative.
5. **Finite pullback.** The statement now specifies a connected compact
   Kähler source manifold Y. No surjectivity or equal-dimension assumption
   is added. For each cycle Z in Y, finite generic degree gives
   integral_Z(f*omega)^dimZ = degree(Z/f(Z)) integral_f(Z)omega^dimZ > 0.
   The path f*alpha+t[kappa_Y] and the Kähler-cone component theorem show
   f*alpha is Kähler, even though the pulled-back form can degenerate at
   ramification. Ideal pullback preserves finite PL maxima. The reduced
   graph component in the model fibre product, followed by normalization
   and equivariant resolution, gives a source model and a morphism F.
   Flag evaluation proves phi_(F*D)=f*phi, and the class identity transfers
   relative nefness component by component. The divisor pulls back because
   the graph is not contained in its vertical support.

The rational and real constant-translation domains are retained. The
maximum argument, its squared-norm convention, and the imported
analytic-cycle closedness argument are unchanged. Equation tags
60.5b–60.5d are inserted without renumbering existing manually tagged formulas.

## Examples and exceptional cases

For phi(v)=-min{v(I_p),1} on P1, rational scaling moves the ray breakpoint
to q and is represented by the flag I_p^b+(t^a), divided by b. For rational
q>1, pointwise q phi instead has degree 1-q on the strict central component
of the original blowup. Thus 2·phi is alpha-psh whereas 2 phi is not.

An irrational q produces a function outside even PL_R: every coherent
ideal on the smooth curve has integral order at p, so a rational PL
function has finitely many rational breakpoints on s ord_p. A finite real
linear combination cannot create an irrational breakpoint. The values at
the trivial character and the character supported at p are explicitly
included. This is a direct calculation in the existing model class, not
a claim about the later completed psh space.

The map z -> z^d, for positive integer d, pulls I_0 back to I_0^d and
alpha to d alpha. The pulled-back potential is -min{d v(I_0),1}, with
slope -d and breakpoint 1/d on the ray. Pullback and rational scaling
commute, with value -min{d v(I_0),q}. The cases d=1 and q=1 reduce to
the identity, and all minima remain well-defined at infinite ideal values.

## Exact primary sources

- Mesquita-Piccione, [arXiv:2409.06221v2](https://arxiv.org/html/2409.06221v2),
  Proposition 4.1.4, printed p. 33. The exact 18 September 2025 version
  was rechecked, and that page rendered and inspected. Its short descent
  argument is expanded; its unrestricted wording about reflection of nefness
  by holomorphic maps is not repeated. PDF SHA-256:
  `9eb2ea7686a5962ebc11c5eacd23b0cb3dcb081e27ac48292933f291fc82cb23`.
- Boucksom–Jonsson, [published AFST PDF](https://afst.centre-mersenne.org/item/10.5802/afst.1705.pdf),
  Lemma 2.34, p. 687, and Proposition 3.6 with proof, pp. 693–694.
  All three pages were rendered and inspected. They verify the direction
  and normalization of the scaling action, integer reflection, and the
  graph-model pullback construction in the algebraic case. PDF SHA-256:
  `50bd6e6782c29088edc96d013a5d49257b0395d9fb398664f1a9859639992948`.
- Demailly–Păun, [published Annals PDF](https://annals.math.princeton.edu/wp-content/uploads/annals-v159-n3-p05.pdf),
  Theorem 0.1, p. 1248, and Theorem 4.3(iii), p. 1267. Both pages were
  rendered and inspected for their exact compact Kähler hypotheses. The
  already checked finite-union criterion remains Proposition 3.3(ii),
  pp. 1262–1263. PDF SHA-256:
  `0fa73d0742f6990e14dd15b6b19dd49b2c3a1b7db69c89785cca98e8edc9c41f`.

No bibliography entry or frozen source locator is changed. The new MP
locator names the checked author version, not an uninspected theorem
number in the published article.

## Second pass and validation

After the first successful complete build (3,969 pages, 18,890,504 bytes),
physical pages 3341–3345 were inspected. The second full statement-to-proof
pass rechecked the finite PL expressions, reciprocal action, properness
and surjectivity of the resolved map, inverse-image cycle choice, compact
Kähler resolutions, strict positivity of the pushforward coefficient,
non-surjective finite maps, zero-dimensional cases and all curve endpoints.
It added the explicit smooth-representative pullback estimate, specified
reduced graph components and integer exponents, and kept the base-change
formula with its introducing sentence. The full build and visual checks
were repeated after these changes.

- Final full build: **3,969 pages, 18,890,747 bytes**.
- Reference/input audit: 390 TeX inputs, 11,607 unique labels; no missing
  input, duplicate label, dangling reference or per-file structure defect.
- Final log: no unresolved reference/citation, multiply defined label,
  rerun request, horizontal overflow or vertical overflow. Existing underfull
  and class warnings remain.
- Bibliography-aware strict changed-block audit: zero errors, one reviewed
  warning for the deliberately cited exact author version. Strict mode exits
  1 on that warning; no clean whole-chapter or whole-book style claim is made.
- Exact inventory: PASS, 45 active atoms in 14 environments,
  tiers (0,5,8,15,17).
- Final physical pages 3341–3348 were rendered and inspected, covering all
  changed text and its boundaries. This is a scoped visual review.
- `git diff --check`: PASS.

Final Chapter 60 SHA-256:
`de33ec47022706e8c21f028a2217ec43dbda9e0618274e5e38460f0c1573f3b7`.
Final live PDF SHA-256:
`67e147d0360e416675334d1c85eb0e3f14a265d991c4334d9d9c83a345888724`.

The P12.1 fragment retains SHA-256
`8d9f9bd9edb057b95773479279bbdabb3240319e4cb56f6f15cb2bd923fb4380`.
Its source integration and author provenance are unchanged. Chapters 58,
59 and 61, the bibliography, all author sources including CURVE_PSH.tex,
the research inventory, frozen statements/proofs, verifier receipts and
dated releases retain their baseline bytes. The live PDF is the ignored
build product. No independent-agent or production-verifier pass is claimed.

Next: audit the model Monge–Ampère and mixed-intersection sections,
including multiplicities, model independence, the Zariski inequality and
the deformation-to-the-normal-cone example. The whole-book audit is ongoing.
