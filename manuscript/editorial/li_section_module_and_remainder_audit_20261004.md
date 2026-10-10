# Section-module and analytic-remainder follow-up audit

Date: 4 October 2026. Two conditional geometric/analytic derivations
continue the general hybrid-limit research route outside the active book.
The checked 4,244-page book, its TeX and bibliography, its frozen artifacts
and all 42 problem statuses are unchanged. No independent model verdict,
new finite calculation or principal general CY theorem is claimed.

## Fixed-degree section space and formal faithfulness

The [section-module derivation](research_dossiers/li_geometric_section_module_20261004.md)
works over a supplied flat projective finite-presentation model over
\(R=\mathbb C\{t\}\), with an invertible model line bundle, an ample
generic restriction, and its projective analytic germ realization. Smooth
connected complex fibres and a regular SNC chart are explicit. Derived
cohomology and proper analytic/coherent comparison remain imports.

Perfect derived cohomology makes the module of sections finite. Model
flatness makes it torsion free; over the DVR it is free. Flat localization
and field completion identify its convergent and formal generic section
spaces. This does not infer ordinary \(H^0\) base change at zero from
arbitrary derived base change.

For actual complex fibres, finite model, section and cohomology data
descend to a finite type coefficient algebra. Flatness descends at a finite
stage. A finite complex, its field splitting, the section-basis cycles
and the inverse matrices involve finitely many meromorphic germs. On
one common punctured disc they give the full holomorphic section basis.
The germ ring itself has no complex-algebra evaluation at a fixed nonzero
parameter: the unit \(t-t_*\) would evaluate to zero. The proof therefore
does not identify that actual fibre with a nonexistent base change of
\(\operatorname{Spec}\mathbb C\{t\}\).

Generic ampleness gives global generation at large degrees. The evaluation
cokernel is killed by a finite power of \(t\), so finite germ realization
gives global generation off zero. The model line bundle need not be ample
on the central fibre. A rational model permits a divisible degree sequence;
the FS and diagonal arguments need only degrees tending to infinity.

Local Taylor coefficients are functions on one common connected transverse
polydisc \(W\), so their ring is \(\mathcal O(W)\), not arbitrary germs
whose evaluation at a different transverse point would be undefined.
For the formal faithfulness proof, choose enough evaluation points on one
small connected fibre inside the chart to make the section evaluation
matrix invertible. Each point lies on a path \(z_i=a_i\xi\), with
\(t=\xi^{\sum b_i}\). The resulting determinant is a nonzero convergent
germ. These path substitutions are defined on the whole coordinatewise
lower-bounded formal Laurent algebra. They exclude any new formal-field
linear relation, proving injection of the entire completed section space.
Convergent independence alone is not substituted for this argument.

The paths are an auxiliary field extension for this independence proof;
they do not assert semistable reduction or replace the original parameter
in the hybrid theorem. Repeated components, a vertex chart and zero
transverse dimension are included.

## Convergent-series remainder and coefficient-uniform absorption

The [remainder derivation](research_dossiers/li_convergent_chamber_remainder_20261004.md)
starts with convergent meromorphic sections on a fixed chart and a compact
interior chamber margin. A finite leading-gap bound is supplemented by
an infinite-tail estimate: if \(x_i\geq\delta>0\), the valuation
difference is bounded below by \(\delta|\beta|-B_0\). Cauchy coefficient
bounds then sum a uniformly convergent geometric series, giving
\(C e^{-\eta T}\) times the leading monomial weight.

The leading coefficient function may vanish. It is not used as a
denominator. Multiplying by the frame norm transports the pointwise bound
without assuming that frame is bounded at the central fibre. Full-core
comparison uses the explicit meromorphic reference relation: a vertical
monomial times a bounded positive unit. The section weight includes that
frame factor, rather than silently discarding it.

For arbitrary coefficient tuples, finite-dimensional Cauchy–Schwarz gives
an exponentially small L2 error relative to the sum of squared monomial
weights. The norm triangle inequality absorbs this error into a separately
supplied positive Fourier/Gram lower bound. This derives the local analytic
remainder input from actual convergence and the fixed chamber margin.
It does not supply raw-volume bounds, Fourier orthogonality or the
probability mass of the selected generic region by itself.

## Controlling sources and fresh scope

The existing cached Stacks primary texts were fully read. Their exact
statement and short displayed proof scopes are:

- Tag 0B91, Lemma 36.30.4: proper finite-presentation morphism, a perfect
  complex and flat map, or a finite-presentation sheaf flat over the base;
  perfect derived pushforward commuting with arbitrary base change.
- Tag 05LY, Lemma 32.10.4: a finite-presentation sheaf over finite-presentation
  inverse-system schemes; flatness over the target descends to a finite
  stage. The standing inverse-system assumptions are retained. Its earlier
  referenced algebra/limit proofs are not all newly checked.

These are cached 2 October source bytes. No fresh live-version claim,
HTML download or complete Stacks-chapter certification is made.

The cached Bingener PDF is a 44-page retyping hosted at
`https://mingchenxia.github.io/LaTeX/Bingener.pdf`, with a title page dated
January 1976. It is not silently identified with the 52-page printed
publication listed in the bibliography. Its extraction was freshly read
in ranges 1–65, 625–850, 880–1080 and 1270–1435: 658 distinct lines.
This is not a full fresh reading or all-antecedent verification.
Six actual pages were newly rendered and inspected: 1, 17, 19, 22, 28
and 29. Physical and printed page numbers differ by one in these proof
passages:

- Theorem (4.2), physical 17 / printed 16: proper direct-image comparison.
- Projective proof passage, physical 19 / printed 18: reduction to twists
  of projective space and coherent resolutions.
- Proper cohomology consequence in the proof of (4.6), physical 22 /
  printed 21: cohomology over a Stein compactum and analytic germ limits.
- Corollaries (5.3)–(5.4), physical 28–29 / printed 27–28: proper coherent
  equivalence and the line-bundle/Picard comparison.

Chapter 59, lines 320–400, and its existing source audit were read for
the projective-germ interface. That audit remains a historical record;
its old source-reading claims are not widened. Li arXiv:2505.11087v1,
lines 470–650, was freshly revisited for the original section-space,
Taylor-expansion and fixed-degree hybrid conventions; its earlier complete
source reading and render manifest remain fixed.

## Application and admission limits

Under the supplied projective model category and cited imports, the
section-module and local expansion conditions now have explicit reductions,
and convergence supplies the leading remainder on compact interior
chambers. The positive reference/blowup model presentation, CY volume and
generic-mass comparisons, uniform Skoda and the dyadic measure/Fourier
scope still have to match the intended degeneration. In particular the
analytic dyadic proof's reduced-SNC condition has not been removed merely
because the module and pointwise remainder proofs allow multiplicities.

No uniform degree radius, chamber-wall/boundary remainder estimate,
nonprojective analytic comparison, singular/disconnected generic extension
or new ordinary central base-change theorem is claimed. New theorem
promotion requires the repository's independent exact-current verification
record; none is created here. The [manifest](li_section_module_and_remainder_manifest_20261004.json)
pins this follow-up, its sources and prior checkpoints. Research and normal
work-branch publication continue in the cloud.
