# P21.3 normal rigid-point zero atom: hostile audit

Date: 29 August 2026

Status at the time of this source audit: **quarantine candidate**.  The
subsequent exact-byte gates are recorded in the addendum below.

## Strongest defensible formulation reached

The candidate does not assume that the curve is rig-smooth, globally
normal, or globally boundaryless. It assumes only:

- a chosen pure one-dimensional open neighborhood `Omega` of `y`;
- `y` rigid and interior;
- ordinary normality of `O_{X,y}`;
- good/separated/strict local analytic geometry; and
- continuity and CLD-psh positivity of `u`.

The current is formed on
`Omega^circ = Omega intersect Int(X/K)`, not on a neighborhood that may
contain analytic boundary points.  This is necessary because positivity of
`d'd''(u delta)` uses the closed integration current of a boundaryless
space.  Since `y` is interior, this restriction loses no germ at `y`.

This is stronger than replacing “rig-smooth curve” by “normal curve”: only
the single local ring is required to be normal. It is also the strongest
form justified by the checked finite-flat radial proof without adding a
normalization-pushforward theorem for nonnormal unibranch points.

## Hidden hypotheses in the older one-line reduction

### One-dimensionality is not contained in normality

Tag 00PD requires a *one-dimensional noetherian* normal local domain.
Goodness gives noetherianity. Rigidity plus local pure dimension one gives
Krull dimension one through CLD (11.5.5.1). Omitting either check would make
the invocation of Tag 00PD invalid.

### Ordinary regularity is not rig-smoothness

Over an imperfect field, a regular/normal analytic curve need not be
geometrically regular and hence need not be rig-smooth. The proof uses the
DVR property of the ordinary local ring only. No scalar extension and no
geometric-regularity assertion occurs.

### Module-flatness is not automatically analytic flatness

CLD's analytic flatness is designed to survive analytic base change. The
statement “the finite local algebra is torsion-free over a DVR, hence flat”
establishes ordinary module-flatness but is not by itself a citation for
analytic flatness.  The candidate closes this gap directly.  Finiteness at
`y` makes the local algebra finite over the target DVR; injectivity and the
source-domain property make it torsion-free, hence finite free and
module-flat.  The point lies in the relative interior, so CLD Remark 11.4.7
then upgrades local-ring flatness to analytic flatness.  Only after that
separate theorem is CLD Section 11.6.3 invoked to obtain the compact finite
flat tube of constant degree and singleton central fibre.

### The interior hypothesis is consumed

CLD Lemma 11.6.5(a) requires the point to lie in the relative interior of
the coordinate map. Boundary composition supplies this from
`y in Int(X/K)`. At an analytic boundary point the finite-tube argument is
not justified and the statement makes no claim.

### Strictness and nontrivial valuation are consumed

The proof needs a cofinal sequence of admissible radii tending to zero in a
strict coordinate disc. The present audit does not replace that step by a
polyradius extension or a descent argument. The trivially valued and
non-strict cases remain outside the statement.

### Continuity is consumed

The estimate uses `sup_Q |u|<infinity` on one fixed compact tube. A psh
function with a logarithmic pole can carry a point mass, so the proof cannot
be extended to arbitrary discontinuous psh functions by the same argument.

## Sign, degree, and calibration audit

- `rho_r>=0`, so `chi_r>=0` and
  `H_r mu({y}) <= integral chi_r dmu` is valid.
- The transpose sign for `d'd''` is positive by CLD Lemma 7.7.5.
- The derivative `q_r''=rho_r'` has one sign on each of the two disjoint
  transition bands, and its total absolute integral is `2`.
- The calibrated pushforward is applied separately on those two bands.
  Finite flat degree `d` includes all sheets and residue-field factors;
  there is no tacit assumption that `y` is `K`-rational or that the residue
  extension is separable.
- CLD Lemma 13.3.8 identifies the calibrated degree with the finite-flat
  degree `d`; Proposition 14.4.2 then supplies the calibrated pushforward.
  Neither result requires rig-smoothness of the source.
- The final inequality should be read with an absolute value before the
  total-variation estimate; the proof states that explicitly.

## Scope not crossed

The packet proves no global current classification. It makes no assertion
for a nonnormal or merely unibranch rigid point, for a nonrigid point, for a
boundary point, in dimension at least two, or for discontinuous psh
functions. A further extension through normalization would require a
separate exact theorem showing the needed compatibility of CLD psh
functions, integration currents, and `d'd''` with finite normalization; no
such theorem is smuggled into this packet.

## Audit conclusion

No unresolved mathematical gap was found inside the printed hypotheses
after expanding the analytic-flatness step. The remaining gate is
independent hostile review of the exact bytes and production Rethlas
verification. Therefore the correct current status is **candidate**, not
proved-for-the-book.

## Subsequent exact-byte addendum

The statement and proof were frozen at SHA-256
`469024d04e8eb5e08900b9caea6480057398c743ca0b46076b524f2109cf80ac`
and
`661100a4b25e82297c5b2b2712775e9c9501c337d619a64280f2d49922a4bcc2`.
An independent line-by-line hostile audit returned final `PASS`.  Production
Rethlas service-evidence run `20260829T060048Z_469024d04e8e`, item
`pi_0d4235a44db2b33950f8dd55`, then returned final `correct`, zero critical
errors, and zero gaps.  This addendum supersedes only the pre-verification
status sentence; it does not enlarge any hypothesis or conclusion audited
above.  Live-book integration remains a separate build and placement gate.
