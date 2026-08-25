# P06.3: ordinary CLD-smooth harmonic regularization on curves

## Production disposition

The corrected exact packet passed guarded production Rethlas run
`20260825T045723Z_331edb5358e4`, item
`pi_b86fec7e60fb3e22e3bafaae`, with model `gpt-5.6-sol` at `xhigh`:
`final/correct`, zero critical errors, and zero gaps.  The exact proof digest
is `6f2bc79ba25bf254d2f0ec20f6459bf593b0ad376ef9d40a750f0b7ea709fd6f`.

Round 1, `20260825T044433Z_331edb5358e4`, was `final/wrong` solely because
the source paragraph pointed to the wrong CLD subsection.  Its rejection,
logs, manifest, and completed process guards are preserved.  The corrected
round uses CLD 3.1.7 and 3.4.7 and Wanner Definitions 3.9--3.12.

No live chapter or ledger has yet been edited.  The result controls only the
literal ordinary-CLD-smooth **harmonic** target; the ordinary-CLD-smooth psh
regularization problem remains open and must retain an open atom.

## Exact interpretation

Three assertions had been conflated in the live discussion.

1. GJR26 Proposition 15.11 gives a decreasing net of **weakly smooth psh**
   functions for every subharmonic function on a relatively compact open
   subset of a rig-smooth boundaryless curve.
2. Wanner19 Corollary 5.4 gives decreasing **ordinary CLD-smooth psh**
   approximation only when the residue field is algebraic over a finite
   field, or the proper curve is `P1` or a Mumford curve. Remark 5.5 says
   that ordinary CLD-smooth psh approximability is unknown on the curves
   where smooth harmonic germs do not exhaust all harmonic germs.
3. The literal third question in `prob:frontier-pluriharmonic` asks for
   ordinary CLD-smooth **harmonic** approximants. This is strictly narrower
   than either psh regularization statement and is false.

## Counterexample mechanism

Use the GJR26 Section 17 genus-3 curve. At the type-2 theta vertex `P`, the
residual curve is an elliptic curve `E`, and the harmonic coordinate
`Ttilde_1` has residual class `[z]-[x] != 0` in `Pic^0(E) tensor R`, with
`x` non-torsion. It is weakly smooth harmonic but not ordinary CLD-smooth.

Non-smoothness alone is not enough. The closure obstruction is obtained by
fixing a compact three-armed affinoid star around `P`. Every harmonic
function on a surrounding open star restricts to Thuillier's harmonic space
on the compact inner star.  Model-independence of that space makes it factor
through the chosen three-arm semistable retraction, so it is constant in all
other tangent directions and affine on each of the three fixed arms.
Thus its residual divisor at `P` lies in the finite-dimensional space of
degree-zero divisors supported on the same three residue points. An ordinary
CLD-smooth harmonic function has a real-principal residual divisor. The
intersection of the real-principal divisors with this finite-dimensional
fixed-support space is a closed linear subspace.

Local uniform convergence controls the three slopes by endpoint values, so
it forces coefficientwise convergence of residual divisors. The nonzero
Picard class therefore cannot be a locally uniform limit of ordinary
CLD-smooth harmonic functions. A decreasing pointwise net converging to the
continuous harmonic function converges uniformly on each compact substar by
the net version of Dini's theorem, giving the same contradiction.

## Hostile checks

- Varying tropical charts do not evade the obstruction: the argument uses
  the intrinsic residual divisor at `P` and a fixed analytic star.
- Moving tangent directions do not evade it: harmonicity and the fixed
  three-arm semistable retraction kill slopes in every other residual
  tangent direction.
- The principal-divisor condition is not used in an infinite-dimensional
  topology. It is intersected first with the three-point divisor space,
  where it is a closed finite-dimensional linear subspace.
- Nets, not only sequences, are covered by the compactness proof of Dini's
  theorem.
- The argument fails deliberately for psh approximants: their nonzero
  curvature can move and concentrate, so uniform convergence need not
  control endpoint derivatives.

## Source audit

- Wanner arXiv:1801.04713v3 source-archive SHA-256:
  `041d4032e4dba67dc8677981a0f40ac0230ad3404460ea05bd22f7e86d641686`.
- GJR arXiv:2111.05741v3 source-archive SHA-256:
  `58f64063539ade89ada2be28a7b9e4ceae7f0b2beb3786d70cac062645a31789`.
- Previously audited CLD v2 PDF SHA-256:
  `5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719`.

The exact source-aware statement and proof are frozen in
`rethlas_packets_20260825/p06_cld_smooth_harmonic_regularization_counterexample_{statement_exact,source_aware_proof_exact}_20260825.tex`.
No live chapter, problem ledger, or inventory file has been edited.

The separate hostile audit records the repaired outer-star/inner-star
boundary issue, the exact source chain, and the minimal compilation.

## Exact-live global-model addendum, 25 August 2026

The live theorem is now installed.  Its proof replaces the merely local
lift by the global model function constructed in the proof of GJR
Proposition 17.4, then restricts to short value-group-rational outer and
inner three-arm affinoids.  It also uses Thuillier Proposition 2.3.3 for the
fixed-model harmonic space.  The exact-live statement and proof passed run
`20260825T055907Z_b5c8f0719b60`, item
`pi_d80993bb01a748f0422ae6a5`, final `correct`, zero critical errors and zero
gaps.  Their SHA-256 values are `b5c8f0719b60...` and `ba402983b6d8...`.
The earlier source-aware pass and premature local-lift live pass are
historical, not controlling.  P06.3 remains open for ordinary CLD-smooth psh
regularization; the authoritative counts stay 18/59.
