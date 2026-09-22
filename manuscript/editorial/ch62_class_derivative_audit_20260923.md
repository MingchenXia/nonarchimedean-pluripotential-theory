# Chapter 62: class derivatives at a fixed measure — 23 September 2026

## Correction and resulting argument

The previous proof of Theorem 62.5.1 said to write the dual energy
as an intersection number and differentiate the background class.
That sentence omitted which measure is fixed. The model intersection
identity directly differentiates potential energy at a fixed model
function. Identifying the result with the derivative of dual energy
at a fixed measure is a separate theorem.

The revision now cites the exact two published inputs:

- Theorem 3.1 of Boucksom--Jonsson identifies the finite-energy
  measure spaces and strong topologies for different positive classes.
  Thus a fixed measure remains in the domain near alpha.
- Proposition 4.5 constructs the continuous twisted-energy functional;
  Theorem 4.8 identifies it with the class derivative of dual energy
  with that same measure fixed.

The ordinary model energy calculation differentiates both the
intersection numerator and the volume denominator. The latter yields
-n alpha^(n-1).K_X / V times E_alpha, namely s E_alpha with the
frozen normalization. The calculation does not require the fixed model
function to stay psh for every nearby class. The finite-energy identity
then uses the already recorded decreasing-net extension of the
continuous twisted functional, without differentiating a limit.
Infinite entropy is harmless because the derivative term is finite.
The quasi-symmetry argument for comparison with J is unchanged.

The valuative ratio formulation now accounts for zero energy.
The strong quasi-metric identifies its sole zero with the trivial
Dirac measure. That measure has zero dual energy for every Kähler
class and zero reduced entropy, so its beta invariant is zero.
Omitting the zero denominator therefore loses no stability condition.

## A calculation distinguishing the two derivatives

Homogeneity gives E_(a alpha)^vee(mu) = a E_alpha^vee(mu) for every
fixed finite-energy probability measure and a > 0. The proof takes
the variational supremum after the bijection psi -> a psi.

On P1 with degree-one alpha, take u of slope -1/2 on the segment
from the trivial valuation to ord_0, constant thereafter and zero
on every other branch. Then

    MA_alpha(u) = (delta_triv + delta_ord_0)/2,
    E_alpha(u) = -1/8,       E_alpha^vee(MA_alpha(u)) = 1/8.

At a > 1/2, keeping u fixed changes its probability measure to

    nu_a = (1 - 1/(2a)) delta_triv + (1/(2a)) delta_ord_0.

For mu = MA_alpha(u), the two quantities are

    E_(a alpha)^vee(mu) = a/8,
    E_(a alpha)^vee(nu_a) = 1/(8a).

Their derivatives at a = 1 are +1/8 and -1/8.
Thus moving the Monge--Ampère measure can reverse the sign.

A separate exact rational-arithmetic calculation checked the
example on Bl_(0,0)(P1 x P1), using H.F = 1, E.E = -1 and the
other basis products zero. For B_a = aH-E/2, the intersections
with the central components F-E and E give the two masses above.
B_a^2/(2a) gives the energy. The optimizer for the fixed measure
is represented by -aE/2 and gives a/8. Values at a = 3/4, 1,
5/4 and 2, and both exact difference quotients, agree.
This is a direct check of an illustrative curve calculation, not
a new research-frontier result.

## Sources and second pass

The published [author offprint](http://sebastien.boucksom.perso.math.cnrs.fr/publis/BJ_synthetic.pdf)
of Boucksom--Jonsson, Contemporary Mathematics 810 (2025), 159--208,
DOI 10.1090/conm/810/16207, was checked at Theorem 3.1,
pages 187--188; equations (4.2) and (4.11) and Proposition 4.5,
pages 191--193; and Theorem 4.8 with its proof, pages 195--197.
The rendered page 195 confirms the fixed-measure statement.
The offprint SHA-256 is
`4ecf20801f0871223ddfc1ea3e09927904affaab75bb5e195bfe55a2b0f09498`.

[MPWN25, arXiv version 1](https://arxiv.org/html/2509.09442v1),
Theorem 10.0.1 and its proof, supplies the analytic-model application.
The corrected scalar-curvature coefficient and the normalized model
stability scope are retained from their earlier audits.
The differentiability theorem remains an explicit source input;
no new proof or independent research gate for it is claimed.

The second pass checked which variable is fixed, the derivative of
the normalizing volume, class independence of the measure domain,
the finite-energy hypothesis in the scaling example, infinite
entropy, and the zero-energy ratio case. It made finite energy
explicit in the example and replaced a ray parameter that shadowed
the standing scalar-curvature symbol. Visual review also found a
short warning title separated from its text; a local minipage
keeps the existing warning together.

## Validation and preservation

The revised section and zero-energy addition pass the strict writing
audit with zero errors and zero warnings. The complete source
closure has 389 TeX files and 11,509 labels, with no missing input,
duplicate label, dangling reference or structural defect.
The active inventory check remains 46 atoms in 14 environments,
with tiers (0,5,8,16,17).

The initial and second-pass full builds passed. After the local
warning layout correction, the final full PDF has 3,923 pages and
18,620,627 bytes, with no unresolved reference or citation and no
horizontal or vertical overflow. Physical pages 3355--3359
(printed pages 3287--3291) were rendered and inspected in the final
PDF. The short warning is now intact on one page.
The source diff is whitespace-clean.

PDF SHA-256:
`d42e2aeb7ebe766c10db17e1b9b5c5aded9650d2a3850d7971bf3d5e8e2533b6`

Chapter 62 SHA-256:
`0377e6d6aea74a09c56fdf369c0b4ca7fde1d3e72613fbf4dfbb88a9a5445e6a`

The frozen factor-n block retains SHA-256
`204ca71038019e4ca4b24aba3b89e54965ef8586fe433a511619e4a54933ee25`.
The author's CURVE_PSH.tex is byte-identical to the supplied download
and retains SHA-256
`9142aac73c5af7e4e715b3313def5ed56fae4e63e1ac8a53d0419df7d2194be9`.
No other chapter source, frozen research packet, verifier record,
bibliography database or dated release artifact was changed.
The current generated PDF remains an ignored local build artifact.
