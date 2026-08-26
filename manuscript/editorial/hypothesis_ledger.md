# Hypothesis ledger

## Base-field regimes

| Code | Field assumptions | Principal use |
|---|---|---|
| K0 | complete non-Archimedean field | Berkovich foundations, metrics |
| KD0 | complete discretely valued, residue characteristic zero | original BFJ regularization/MA theory |
| KDA | KD0 plus algebraizability over a function field | original BFJ existence theorem |
| KMIX | mixed characteristic plus resolution and embedded resolution inputs | conditional later MA theorem |
| KT | algebraically closed trivially valued field | foundational BJ theory and supplied envelope theorem |
| C | complex numbers with compact Kähler geometry | DXZ/Xia/MP/MPWN |

## Space regimes

| Code | Space assumptions |
|---|---|
| SmProj | smooth projective variety |
| RegProj | regular projective variety |
| NormProj | normal integral projective variety |
| UniProj | integral projective unibranch variety |
| RedProj | reduced, possibly reducible projective scheme |
| KMan | compact Kähler manifold |
| KSpace | reduced irreducible unibranch compact Kähler space |

## Positivity regimes

| Code | Positivity datum |
|---|---|
| AmpL | ample line bundle |
| NefL | nef line bundle/model line bundle |
| BigL | big line bundle |
| NumR | arbitrary real numerical class |
| Kah | Kähler cohomology class |
| Big11 | big real \((1,1)\)-class |
| Psef11 | pseudoeffective real \((1,1)\)-class |

## Regularity regimes

| Code | Potential/metric class |
|---|---|
| Model | model/formal metric or model function |
| PL | piecewise linear metric/function |
| SmoothCLD | smooth CLD metric/function |
| C0PSH | continuous psh metric/function |
| BddPSH | bounded psh function |
| PSH | arbitrary singular psh function |
| E1 | finite Monge--Ampère energy |

## Rule for theorem statements

Every major theorem must make its field, space, positivity, and regularity
regime recoverable from the statement itself. Margin codes may summarize
hypotheses but never replace prose.

## Current source-boundary firewalls

- **GK delta-metrics (Ch. 18).**  For a piecewise smoothly metrized line
  bundle, the global piecewise smooth Chern form and the canonical residual
  generalized delta-form of codimension one exist without assuming ordinary
  delta-metricity.  Ordinary delta-metricity additionally requires the
  facewise Hessian to extend from the tropical cycle to an ambient
  bidegree-\((1,1)\) superform with piecewise smooth coefficients.  The
  residual form is unique by the universal algebraic-pullback property of
  GK Proposition 9.8, not by injectivity into currents on one fixed open
  set.  After intersecting an ambient coefficient form with a
  codimension-\(c\) tropical cycle, its ambient bidegree is
  \((c+1,c+1)\), while its relative bidegree remains \((1,1)\).
- **BJ closure package (Chs. 34--35).** The repaired closure theorem is an
  imported `BJ22` package in the trivially valued projective regime. Its
  decreasing-net and moving-class clauses require the exact source hypotheses;
  scalar multiplication is stated only for (a>0). A zero coefficient omits
  the summand and never forms (0(-\infty)). The 22 August integration is
  source-audited, but its Rethlas receipt remains pending.
- **DXZ--BJ versus MP (Ch. 71).** The literal raw multiplier-ideal formula on
  all semivaluations is retained only for a pseudoeffective
  (mathbf Q)-line-bundle class on a smooth projective manifold. The
  real-Néron--Severi assertion is the source's directed-limit identification.
  The MP comparison remains Kähler, (mathcal I)-maximal, and finite-energy;
  it is neither a full-cone identification nor a replacement of
  (P)-equivalence by (mathcal I)-equivalence.
- **Trusiani v2 (17 August 2026).** Its smooth polarized projective and
  weighted-relative statements remain dated preprint claims under their
  displayed automorphism-relative hypotheses. They do not enlarge the
  compact-Kähler, singular, hybrid-continuity, bounded-support, or
  direct-algebraic residual questions.
