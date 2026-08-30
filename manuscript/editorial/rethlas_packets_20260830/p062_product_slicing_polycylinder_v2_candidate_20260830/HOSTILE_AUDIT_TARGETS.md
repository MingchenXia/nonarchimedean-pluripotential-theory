# Fail-closed hostile-audit targets for v2

Any failure below blocks promotion. Auditors must inspect the exact v2
bytes and must not transfer a verdict from either the failed v1 packet or
the repair blueprints.

## Exact fibre test extension

1. Verify that a point `y` of the analytic fibre and the corresponding
   total-space point have canonically the same completed residue field.
   Check the affinoid `C completed_tensor_A H(x)` argument, including both
   density inclusions.
2. Verify that goodness applies to the total space `Y_0`, so that the
   ambient `kappa_{Y_0}(y)` is dense in this common completed residue field.
   Density of the base `kappa(x)` is not being substituted here.
3. Check that strict pointwise approximation of every fibre moment value
   persists on a fibre neighbourhood and gives exact equality of norms by
   the ultrametric inequality. Check also that the representing ambient
   germs are units after shrinking.
4. Check the literal local identity `Phi_y|_F=varphi`, including the domain
   of the real smooth function in the ambient tropical chart.
5. Check the use of CLD Corollary 15.2.9: the fibre support is compact and
   closed in the Hausdorff total space, the finite ambient open cover is in
   scope, and every `theta_i` has compact support contained in `W_i`.
6. Check extension by zero of `theta_i Phi_i`, exact equality both on and
   off `supp(varphi)`, and compact support implying support proper over the
   affinoid base.

## Continuous-multiplier slicing

7. Check that CLD Proposition 6.5.2(b) applies to the compactly supported
   symmetric form `d'd'' Phi`, and that restrictions of the two positive
   forms to all one-dimensional fibres remain positive.
8. Check that Theorem 16.3.3(d) makes the positive fibre masses continuous
   and bounded on the chosen compact base, yielding the displayed uniform
   total-variation estimate.
9. Check both sides of the projection formula under uniform approximation
   of `h`, including compact supports, bidegrees, and signs.
10. Check that top bidegree of `alpha` annihilates every horizontal and
    mixed Leibniz term in `d'd''(Phi pi^*alpha)`.
11. Check that the base is literally in the very-rich scope required for
    injection of continuous functions into `(0,0)` currents.

## Annulus and polyannulus steps

12. Check that `{|P|<s^d}` lies in `{|T|=s}` and that its polynomial map to
    the open target disc is finite flat of full degree.
13. Recheck the graded single-fibre calculation at `t=s`, including lower
    initial terms, inseparable degree, and the proper-neighbourhood trace
    limit approaching the target boundary Gauss point.
14. Check that local rigid-point density suffices on the strict open
    annulus.
15. For each coordinate fibre over a possibly nonrigid base point, verify
    that the one-dimensional annulus theorem compares the given point with
    the corresponding one-variable Gauss point at the same radius.
16. Check the iterated formula
    `max_nu |a_nu| prod_j s_j^{nu_j}` first for Laurent polynomials, then
    for analytic Laurent series on compact subannuli. At intermediate
    stages audit the completed residue-field coefficients and nesting of
    maxima.
17. Check that equality of seminorms on compact subannuli identifies a
    unique analytic endpoint independent of order, and that Banach
    approximation proves continuity of the multivariate Gauss section in
    the Berkovich topology.
18. Check that disc-coordinate constancy genuinely descends `h` to the
    annulus product and that the Gauss identity gives a continuous
    factorization `h=phi o F`.
19. Check the final joint-affinity test: compact support, bidegrees,
    split-torus Fubini, cancellation of the positive disc mass, vanishing
    of every mixed distributional Hessian, and the endpoint-density step.

The scope remains standard strict polycylinders and their stated endpoint
closures. It does not establish current pullback under arbitrary scalar
extension or uniformize arbitrary analytic germs.
