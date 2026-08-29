# P06.1 hostile scope audit

Date: 29 August 2026

Status: the bounded quasi-smooth theorem passes the source and descent audit.
The unrestricted singular statement does not.

## Outcome

The strongest supported positive statement is:

> Every classically pluriharmonic real-valued function on a good, strict,
> quasi-smooth analytic space over a complete nontrivially valued field is
> $\mathbf R$-PL, hence harmonic in the Gubler--Jell--Rabinoff sense.

For the boundaryless spaces in the live P06.1 formulation, quasi-smoothness
is equivalent to smoothness. Thus the packet removes the global strict
semistable-model hypothesis throughout the smooth part of the live problem.
It does not resolve singular spaces of dimension at least two.

## Rejected descent shortcut

Temkin's Berkovich map is surjective and quasi-$\acute{e}$tale, but it is
generally not finite and may have relative boundary. One cannot simply
apply Gubler--Jell--Rabinoff, Proposition 5.11, to that map: the proposition
requires finite, flat, and surjective, and its proof uses a norm with
constant local rank. Nor was a primary source found saying that every such
map admits a G-local refinement whose individual affinoid maps are finite
flat and surjective onto target affinoid domains.

The packet instead uses an actual topology theorem. Temkin, Corollary 3.3.2,
gives a covering in the rigid $\acute{e}$tale topology. By de Jong--van der
Put, Proposition 3.2.2, it is enough to know G-descent and finite
$\acute{e}$tale affinoid descent. The former is
Gubler--Jell--Rabinoff, Section 5.2(4); the latter is proved completely in
the packet and uses Proposition 5.11 only where its hypotheses hold. This
closes the relative-boundary and G-topology gaps without the rejected
refinement claim.

## Hypothesis ledger

| Hypothesis | Where it is used |
|---|---|
| $K$ complete and nontrivially valued | Temkin's uniformization, the strict annulus, and the Gubler--Rabinoff PL/semipositivity comparison. |
| $X$ good | Each point has a strict affinoid neighbourhood to which Temkin applies. |
| $X$ strict | Rigid--Berkovich translation, strict semistable uniformization, and the cited PL theory. |
| $X$ quasi-smooth | The associated local rigid space is smooth, the exact input of Temkin, Corollary 3.3.2. |
| Global quasicompactness | Not used; quasicompactness is recovered after localizing to an affinoid. |
| Separatedness | Not used in the local proof. |
| Boundarylessness | Not used; the classical pluriharmonic pullback theorem is functorial for arbitrary analytic morphisms. |
| Divisibility of coefficients | Used with $\Lambda=\mathbf R$ in Gubler--Jell--Rabinoff, Proposition 5.11 and Corollary 5.12. |

## Temkin strictness audit

The proof must cite Corollary 3.3.2, whose affinoid source possesses a
strictly semistable affine formal model. Citing only Theorem 3.4.1 is unsafe
editorially because its displayed Berkovich formulation describes the
maximal affine formal model merely as semistable. The packet retains the
strict model statement of the rigid corollary, exactly matching
Gubler--Rabinoff, Proposition 7.8.

## Pullback and field-descent audit

- Ground-field extension of pluriharmonicity is an equivalence in
  Gubler--Rabinoff, Proposition 7.2(6).
- Pullback through every analytic morphism is allowed by Proposition
  7.2(7). No $\acute{e}$tale, boundaryless, finite, or flat condition is
  needed in this direction.
- Descent of $\mathbf R$-PL after the finite extension $L/K$ is the
  published Gubler--Jell--Rabinoff, Corollary 5.12.
- Harmonicity is concluded only after PL regularity, using
  Gubler--Rabinoff, Theorem 4.3, for both signs.

## Coefficient firewall

The cited semistable theorem concludes $\mathbf R$-PL. If PL in the live
question were read literally as integral PL, the answer would already be
negative on a strictly semistable annulus: $\sqrt2\log|T|$ is classically
pluriharmonic but has irrational slope on the skeleton. The proof does not
assume that an arbitrary G-local chart contains a skeletal interval: it
extracts a finite affinoid subcover, applies Baire to the closed
intersections with the compact skeleton, and only then invokes the
integral-slope input.  More precisely, it uses Thuillier's local integral-slope
theorem for analytic units directly on that skeletal interval.  It uses
neither analytic-stalk invariance at a relative-boundary point nor the false
claim that an arbitrary ambient neighborhood contains a standard
subannulus.  The natural unresolved statement is therefore the real-PL
statement.

## Previously settled one-dimensional scope

No new regularity theorem is needed for strict curves. Gubler--Rabinoff,
Section 4.1.2, identifies classical psh with subharmonicity on curves, and
their Proposition 3.15 identifies harmonic functions on an arbitrary strict
analytic curve with $\mathbf R$-PL functions satisfying residual numerical
triviality. Hence every classically pluriharmonic function on an arbitrary
strict analytic curve is already $\mathbf R$-PL, including singular and
nonreduced curves.

## Fatal obstruction beyond the packet

For a singular analytic space of dimension at least two, altered local
uniformization does not supply the quasi-smooth $\acute{e}$tale cover used
here. A smooth alteration is generally proper and generically finite, not
finite flat. Gubler--Jell--Rabinoff, Proposition 5.11, does not descend PL
through such a map. Curvewise PL restrictions also do not by themselves
assemble a finite local presentation by logarithms of ambient analytic
units. Gubler--Rabinoff's Shilov-boundary evaluation injectivity gives
uniqueness, not existence of such a presentation.

No counterexample to the unrestricted $\mathbf R$-PL statement was found,
and Gubler--Rabinoff explicitly record removal of their regularity
assumptions as unknown. The singular, higher-dimensional residual scope must
therefore remain open.

## Integration firewall

This directory is quarantined. Neither the live chapter nor
open_problem_atomic_inventory_20260824.md has been edited. The theorem must
not be promoted without an exact-byte production Rethlas verdict of correct
with zero critical errors and zero gaps.
