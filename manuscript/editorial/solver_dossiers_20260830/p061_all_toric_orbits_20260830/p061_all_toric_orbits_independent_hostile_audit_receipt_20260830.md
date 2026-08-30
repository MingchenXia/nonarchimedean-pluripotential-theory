# Independent hostile-audit receipt: P06.1 all toric orbits

Date: 30 August 2026  
Audit role: independent hostile mathematical audit  
Disposition: research-only; no production Rethlas call was made

## Exact audited bytes

- Statement: `p061_all_toric_orbits_statement_20260830.tex`  
  SHA-256: `05bda70eb1cf7ebbcc95d1831feadd946afa168f64a7298171381b9f1e865e60`
- Proof: `p061_all_toric_orbits_proof_20260830.tex`  
  SHA-256: `21c44c47a91a28469fb91a6c00569ed56d12699bae9c956c68c33ad493825b03`

For identification only, the accompanying dossier audited with those files was
`p061_all_toric_orbits_dossier_20260830.md`, SHA-256
`f88eaa16cfeff0ee66f00a336ac10e24d49b0b1acf06a2cf844ca78ec77dad4a`.

## Verdict

**PASS.**  The exact statement and proof bytes above have **0 critical
findings and 0 mathematical gaps**.  No counterexample was found within the
stated hypotheses.  The argument does not use a simplicial alteration, proper
descent, rigid-point density, or a product-topology shortcut.

## Obligations checked

### 1. Ordinary-open product tube

- The section is defined by a genuinely `K`-rational point, so evaluation has
  values in `K` and gives the bounded retraction
  `A completed-tensor B -> B` used in the proof.
- For a kernel element, finite tensors are dense.  Subtracting the evaluated
  tensor keeps the approximation arbitrarily close and makes every first
  factor vanish at the rational point.
- Nontriviality of the absolute value supplies strict rational neighbourhoods
  on which finitely many such factors are uniformly small.
- Upper and lower basic-open inequalities are both preserved.  In the lower
  inequalities the perturbation is strictly smaller than the evaluated term,
  so the ultrametric equality, not an Archimedean estimate, gives the desired
  inclusion.
- Thus the proof produces an actual affinoid product inside an ordinary open
  neighbourhood; it does not assume that the underlying Berkovich product has
  the ordinary product topology.

### 2. Weighted transverse toric domains

- Full dimensionality and strong convexity imply that every nonzero element
  of `S=rho^vee intersect M` has strictly positive pairing with the chosen
  integral interior vector.
- Finite generation of `S` reduces the displayed infinite family of bounds to
  finitely many strict Weierstrass bounds.  Rescaling is compatible with all
  monoid relations.
- The domains are nested strict affinoid neighbourhoods of the rational fixed
  point.  Their intersection is exactly that point.
- Compactness of the first domain and the nested-closed-set argument prove
  cofinality among ordinary neighbourhoods; no first-countability assumption
  is used.

### 3. Every completed-residue-field fibre

- For an arbitrary Berkovich parameter point `b`, the analytic fibre is the
  scalar extension of the weighted toric domain to `H(b)`.
- Extending the function first to `H(b)` and then pulling it back along the
  canonical `H(b)`-rational lift of `b` is legitimate by the cited scalar
  extension and functoriality assertions for classical pluriharmonicity.
- The fibre algebra is exactly the semigroup Tate algebra
  `H(b)<S>` after the displayed integral rescaling.  It remains strict over
  `H(b)` because the radii come from `|K^times|`.
- A nonzero convergent semigroup series attains its Gauss norm at a
  coefficient.  Hence it can be normalized to norm one.  The product of two
  nonzero reductions is nonzero in
  `tilde(H(b))[S]`, which embeds in the group algebra
  `tilde(H(b))[M]`.  This proves multiplicativity of the Gauss norm.
- The Gauss norm is therefore the supremum norm and the canonical reduction is
  the integral domain `tilde(H(b))[S]`.  The Shilov boundary consists of its
  single semigroup Gauss point.
- The maximum and minimum of the pulled-back pluriharmonic function occur at
  this one point, so they are equal and the function is constant on the whole
  analytic fibre.
- The analytic fibre over `b` identifies with the full topological fibre of
  the projection.  Since `b` was arbitrary, this proves pointwise
  factorization through the parameter, including all non-rigid product
  points.

### 4. Orbit principal-open product decomposition

- Every analytic point has a unique torus-orbit face via its scheme-theoretic
  support.
- `N_tau=N intersect span_R(tau)` is saturated, hence admits a lattice
  complement.
- Rationality of the dual face supplies an integral relative-interior element
  `q`.  It vanishes on `tau` and is strictly positive on every ray outside
  `tau`.
- Localizing at `chi^q` gives exactly
  `{m in M : m restricted to tau is nonnegative}`: adding a sufficiently large
  multiple of `q` corrects all finitely many inequalities outside `tau` and
  leaves those on `tau` unchanged.
- Under any chosen lattice splitting this monoid is the direct sum of the
  dual monoid of `tau` in its saturated span and the character lattice of the
  complementary torus.  Therefore the asserted algebraic product chart is
  exact.
- The check includes `tau=0`, `tau=sigma`, non-full-dimensional `sigma`,
  positive-dimensional orbits, and nonsimplicial faces.  In the transverse
  lattice, `tau` is full-dimensional and has the rational torus-fixed point
  required by the parameterized proposition.

### 5. Passage to real-PL and harmonicity

- The parameter factor is an affinoid domain of a split torus and hence
  quasi-smooth.  The already verified quasi-smooth P06.1 result makes the
  factor real-PL.
- Pullback stability and sheafiness yield real-PL regularity near every point
  and then on the whole ordinary open subspace.
- Classical pluriharmonicity gives classical psh for both signs.  The cited
  comparison for real-PL functions makes both signs semipositive, which is the
  asserted Gubler--Jell--Rabinoff harmonicity.

### 6. Split fans and nonsplit forms

- Affine toric charts cover a split toric variety, so the affine conclusion
  glues by sheafiness.
- For a finite analytic extension splitting the variety, scalar extension
  preserves classical pluriharmonicity and inverse images of ordinary opens
  remain ordinary open.
- The split theorem applies upstairs and the cited ground-field descent for
  real-PL functions returns the conclusion over `K`.  The original function
  and its negative are still classically psh, so harmonicity follows from the
  same comparison theorem downstairs.

## Noncritical presentation notes

The proof is already complete.  Three optional reader-facing additions would
only make implicit standard facts explicit: mention the closed immersion
defined by finite monoid generators when introducing the weighted affinoids;
cite the standard identification of an analytic fibre with the corresponding
topological fibre; and state that rationality of the dual face supplies the
integral relative-interior point.  None is a missing mathematical step.

## Scope firewall

This receipt validates only the following scope of the frozen bytes:

- ordinary open analytic subspaces of arbitrary split toric varieties;
- every orbit, including positive-dimensional orbits of nonsimplicial cones
  and cones that are not full-dimensional;
- actual analytic local product models consisting of a full-dimensional
  split affine toric fixed-point factor and a quasi-smooth factor; and
- varieties which become split toric after the finite analytic field
  extension used in the statement.

It does **not** validate or assert the theorem for a general toroidal space, a
genuine log-etale chart, an arbitrary analytic domain at a relative-boundary
point, a nonsplit local model without a splitting analytic extension, or an
arbitrary nonproduct singular analytic germ.  It supplies no descent through
a proper toric modification or a general nonflat alteration.  Those cases
remain outside this packet.
