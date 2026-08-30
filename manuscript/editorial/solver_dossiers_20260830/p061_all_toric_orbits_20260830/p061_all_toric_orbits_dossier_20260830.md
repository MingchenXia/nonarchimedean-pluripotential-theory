# P06.1: all torus orbits of a split toric variety

Research-only dossier, 30 August 2026.  It is not a live-book input and
has not been sent to production Rethlas.  No novelty or priority claim is
made.

## Result isolated

The packet proves a parameterized strengthening of the already verified
toric-fixed-point theorem.  Near the fixed section of a product
`(full-dimensional affine toric cone) × Y`, every classically
pluriharmonic function is pulled back from `Y`.  The proof tests every
actual Berkovich fibre over its completed residue field.  The weighted
semigroup affinoid in that fibre has canonical reduction
`\widetilde{\mathscr H(y)}[S]`, an integral domain, and hence singleton
Shilov boundary.  The affinoid maximum--minimum principle forces fibrewise
constancy.

Every orbit of an arbitrary split affine toric variety has a principal
open neighbourhood

`X_tau × T`

where `tau` is full-dimensional in its saturated span, `X_tau` is viewed at
its torus-fixed point, and `T` is a split torus.  Applying the parameterized
statement and the verified quasi-smooth P06.1 theorem on `T` proves
classically pluriharmonic implies real-PL at every orbit, without
simpliciality.  Fan gluing gives arbitrary split toric varieties.  Finite
scalar extension plus GJR ground-field descent gives every toric form which
becomes split over a finite analytic field extension.

## Exact dependency audit

- Gubler--Rabinoff, *Classically psh and pluriharmonic functions on
  Berkovich spaces*, arXiv:2506.13548v2, local PDF SHA-256
  `83ca9a19394f44bb2e4e1aa316de95938f311acd53a00fe250fa0f605184b726`.
  The packet uses Proposition 7.2(6),(7), Proposition 7.3, and Theorem 4.3
  in their stated directions.
- Gubler--Jell--Rabinoff, *Forms on Berkovich spaces based on harmonic
  tropicalizations*, audited PDF SHA-256
  `572d51c9f8907dbb814684f7d136612243c0e0b70cddbe6759bb686f0bcfbd42`.
  The packet uses Definition 5.1, Section 5.2(4), Lemma 5.4(1), Corollary
  5.12, and Definition 7.2.
- The rational-section tube statement/proof already passed production with
  exact SHA-256
  `96b246d6f6032bce38751095935525a67456c6753e006e7b188778bc945e50bc`
  and
  `6f6158b5253922539f81e42ab9e6d9e2c48a6b3c8b727e4157351b9591baabe5`.
  The present packet repeats the needed ordinary-open part so that its
  logical core is self-contained.
- The toric fixed-point statement/proof already passed production with
  exact SHA-256
  `edbe69950a0a9c81ca2fd9077a58be96ec6bdb6c27ce9cf2524da5bf653a5ab6`
  and
  `531e326b4aeb19067fcb88af2f6eb6477a169587d71a3249103777c9131cf8f4`.
  The present proof strengthens it by proving singleton Shilov boundary
  after scalar extension to every completed residue field and applying it
  fibrewise.
- The quasi-smooth P06.1 statement/proof used on the orbit torus have
  exact SHA-256
  0b1b4d161e3b85d342d7be88234a8ed27bfe74be4d24a639ff0456373a7a39e9
  and
  fdc6abcc4988644656892172fbdbda4178cb86ca710fd0122a90947e598b0b8b.

## Independent research audit

An independent hostile audit of the exact statement and proof returned
PASS, with no counterexample, fatal gap, or hidden hypothesis.  It checked
the completed-residue-field fibres, geometric singleton Shilov boundary,
ordinary-open tube, all face extremes and non-full-dimensional cones,
the exact localized-monoid product chart, and finite scalar descent.
Its three optional exposition suggestions (closed immersion for the
affinoid domain, analytic/topological fibre identification, and rational
relative-interior positivity) have been incorporated into the frozen text.
This is a research audit only, not production Rethlas verification.

## Hostile checks

1. **No product-topology shortcut.**  The open-tube lemma is proved using
   upper and lower inequalities in the Berkovich topology and a completed
   tensor-product kernel estimate.
2. **No rigid-point density.**  Fibrewise constancy is proved over
   `\mathscr H(b)` for every `b` in the parameter affinoid.
3. **Geometric Shilov issue.**  Singleton Shilov boundary is reproved after
   every analytic extension, using the domain
   `\widetilde{\mathscr H(b)}[S]`.
4. **No simplicial cover.**  The orbit chart is an exact localization of
   monoids.  It works for a non-simplicial face because the transverse cone
   is merely full-dimensional in its saturated span.
5. **No false descent along a proper modification.**  No toric resolution,
   alteration, normalization, or nonflat finite descent occurs.
6. **Actual scope.**  The theorem concerns ordinary open analytic
   subspaces.  It does not assert the result at a relative-boundary point of
   an arbitrary analytic domain unless that domain has the displayed local
   product chart.

## Fail-closed residual boundary

This packet does **not** prove P06.1 for a general toroidal or log-etale
chart.  A genuine log-etale chart need not be an analytic local
isomorphism to the product in the proposition.  The fibrewise argument
needs an actual analytic projection whose transverse fibres are the
weighted cone affinoids.  Pullback along a log-etale or ordinary etale map
does not supply such a projection, and the currently verified PL descent
theorems do not descend an arbitrary PL function through a proper toric
modification or a general nonflat alteration.

The next minimal atom is therefore:

> Let `q: X -> Z × Y` be an ordinary etale (or strict log-etale) chart,
> with `Z` a full-dimensional split affine toric cone, and let `x` lie over
> the fixed stratum.  Prove that, after an etale cover of a neighbourhood of
> `x`, the chart admits a product projection with singleton-Shilov
> transverse fibres; or construct a classically pluriharmonic function
> showing that this relative product assertion is false.

Until that local-product assertion is proved, the general toroidal/log-etale
claim must remain open.  The arbitrary nonproduct singular analytic germ
residual is unchanged.
