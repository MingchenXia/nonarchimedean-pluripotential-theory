# P21.3 rigid-exception extension: exact source and scope audit

Date: 29 August 2026

Status: **staging only; not a live-book theorem; not production-Rethlas
verified; P21.3 remains active.**  The statement and proof in this directory
must not be promoted, cited as established, or used to change the open-problem
inventory until their exact bytes receive a production `correct` verdict with
zero critical errors and zero gaps.

## Exact candidate scope

- `K` is complete and nontrivially valued.
- `X` is nonempty, connected, good, separated, strict, normal,
  one-dimensional, and boundaryless.
- `E` is a locally finite set of rigid points.
- `Y=X\E` is assumed rig-smooth.
- The current is positive and separately `d'`- and `d''`-closed, of
  bidegree `(0,0)`.
- The Bedford--Taylor conclusion is only for continuous CLD-psh pairs with
  equal curvature currents.

No claim is made for a trivially valued field, a non-good or non-strict
curve, a curve with boundary, a nonnormal curve, a nonrigid exceptional
point, a non-locally-finite exceptional set, a complement that is not
rig-smooth, discontinuous psh potentials, or dimension at least two.

## Production-verified imported dependency

The only new analytic classification input is the already live and
production-verified proposition
`prop:p21p3-gfc-smooth-rigidity`: on a connected good separated strict
rig-smooth boundaryless curve over an arbitrary complete nontrivially valued
field, every positive `d'`- and `d''`-closed CLD current of bidegree `(0,0)`
is a unique nonnegative constant multiple of the integration current.

Exact live dependency bytes:

- reduced statement:
  `c9f27245f5608b772385167c84bfe9e836fc9f4b164477a578b6c26712e35b21`;
- reduced proof:
  `01ab07fdacedfe95e1d764656a071a88395f5d0766115fd0a67164e3162410af`.

They are the files
`manuscript/editorial/rethlas_packets_20260828/p21p3_curve_rigidity_arbitrary_field_reduced_statement_live_20260828.tex`
and
`manuscript/editorial/rethlas_packets_20260828/p21p3_curve_rigidity_arbitrary_field_reduced_proof_live_20260828.tex`.
Their controlling reduced production run is
`20260828T042906Z_f2a1c1b9f2a3`, model `gpt-5.6-sol`, reasoning `xhigh`,
verdict `correct`, zero critical errors, zero gaps, with seventeen passed
statement records and nineteen passed primary-source records.  The exact
receipt is
`manuscript/editorial/rethlas_packets_20260828/p21p3_curve_rigidity_arbitrary_field_live_rethlas_receipt_20260828.md`,
SHA-256
`afe4e1f458d3725fa1c4fecb3e682d0b53bc86abf1166b7b4817028d9fce7fdd`.

The present candidate uses only the smooth rigidity proposition from that
dependency.  It does not import any rejected or conditional P21.3 packet and
does not use the reduced normalization theorem to bypass the missing
rig-smoothness at `E`.

## Primary-source checks

### Ducros, *La structure des courbes analytiques*

Primary PDF:
`/private/tmp/p21_bridge_sources/ducros_curve.pdf`, SHA-256
`b514eaa16c0a531880672956d08ee75a4026d75f61303446044468937c9342ad`.
Extracted text:
`/private/tmp/p21_bridge_sources/ducros_curve.txt`, SHA-256
`7707c5384c328933e1aec337135fee4867527b58b0097ca16dcecb7685e07e19`.

- Theorem 3.5.1 (printed page 190): every analytic curve is a graph.
- Section 1.3.5 (printed page 27): a connected graph is connected by
  injective arcs.
- Section 1.3.12 (printed page 30): a point lying on an open interval
  traced in a graph is pluribranch; in particular, every interior point of
  an injective arc is pluribranch.
- Proposition 3.5.2 (printed pages 190--191): at a rigid point, the cardinal
  of the set of branches equals the cardinal of the inverse image in the
  normalization.  Therefore a rigid point on a normal analytic curve is
  unibranch.  Only this cardinal equality, rather than a canonical
  identification, is used.

These four statements prove that deleting `E` does not disconnect `X`: an
injective arc between two points outside `E` cannot contain a point of `E`
in its interior, because that point would be simultaneously pluribranch and
unibranch.

### Chambert-Loir--Ducros, *Formes differentielles reelles et courants sur
les espaces de Berkovich*, version 2

Primary PDF:
`/private/tmp/p21_bridge_sources/cld25.pdf`, SHA-256
`5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719`.
Extracted text:
`/private/tmp/p21_bridge_sources/cld25.txt`, SHA-256
`021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e`.

- Formula (11.4.1.3): the boundary-composition identity.  Since an open
  immersion has empty relative boundary, an open subspace of a boundaryless
  analytic space is boundaryless.
- Section 15.2.2 and Corollary 15.2.4 (printed page 424): every good
  separated analytic space is locally holomorphically separated and hence
  locally differentially separated.  This verifies the separation
  hypothesis used below for the order-zero theorem and continuous
  multiplication of positive currents.
- Section 7.1.6 (printed pages 152--153): restriction of currents to an open
  subset is defined by extension by zero of compactly supported test forms.
  Sections 7.7.1--7.7.3 give the local differential operations and their
  compatibility with restriction.
- Proposition 3.3.6 (printed page 80): the support of a `(p,q)` form on a
  G-tropical space is contained in the locus of tropical dimension at least
  `max(p,q)`.
- Proposition 15.2.1(a) (printed page 423): on an analytic space, the
  preceding statement gives
  `Supp(alpha) subset {x : d_K(x) >= max(p,q)}`.
  A rigid point has `d_K(x)=0`: by Section 11.1.10, rigidity means that
  `H(x)/K` is finite, and both the residue-transcendence and rational-rank
  terms in formula (11.2.3.1) are zero.  This includes finite inseparable
  extensions.  Hence every smooth `(1,1)` test form vanishes on a
  neighborhood of every rigid point and its support misses `E`.
- Proposition 7.2.9 and Example 7.2.12: positive currents have order zero and
  can be multiplied by continuous functions on a locally differentially
  separated space.
- Section 7.3.1 defines the integration current.  Together with restriction
  in Section 7.1.6, it gives `delta_X|Y=delta_Y`.  Corollary 7.2.10 defines
  `[h]` for every locally integrable function `h`, while Example 7.2.12
  defines multiplication of a positive current by a locally bounded Borel
  function.  For continuous `h`, these definitions and Section 7.3.1 give
  directly, on every compactly supported top-degree test form `alpha`,
  `<h(delta_X|W),alpha> = integral_W h alpha = <[h],alpha>`.  No appeal to
  the narrower tropical-coefficient construction in Section 7.3.4 is made.

The support-vanishing step is stronger than an atom estimate: it identifies
the entire test space in bidimension `(1,1)` across `E`.  Consequently, once
`T-c delta_X` vanishes on `Y`, it vanishes on every compactly supported
`(1,1)` test form on `X`.

## Logical dependency ledger

1. Local finiteness plus Hausdorffness makes `E` closed, so `Y` is open.
2. Open-subspace inheritance and CLD (11.4.1.3) give all geometric
   hypotheses on `Y` except connectedness; CLD 15.2.2 and 15.2.4 supply the
   local differential-separation hypothesis for currents.
3. Ducros 3.5.1, 1.3.5, 1.3.12, and 3.5.2 prove `Y` is nonempty and
   connected by injective arcs.
4. The production-verified rig-smooth proposition gives
   `T|_Y=c delta_Y`.
5. CLD 3.3.6 and 15.2.1(a) show every compactly supported `(1,1)` test form
   on `X` has support in `Y`; therefore `T=c delta_X` on `X`.
6. For continuous psh `u,v`, multiplication by the classified current gives
   `d'd''((u-v)T)=c(d'd''[u]-d'd''[v])`, proving continuous-pair
   Bedford--Taylor independence.

## Hostile scope checks

- A nonrigid exceptional point can be pluribranch and can disconnect the
  curve; it is excluded.
- A nonnormal rigid point can have several points above it in the
  normalization and therefore several branches; normality is consumed
  exactly in the Ducros 3.5.2 step.
- Local finiteness is consumed to prove that `E` is closed and `Y` is an open
  analytic subspace.  No claim is made when `E` accumulates in `X`.
- The argument does not pull currents through a field extension.
- No current is multiplied by a cutoff.
- No zero-atom statement is substituted for the CLD `(1,1)` test-form
  vanishing; the latter is the precise removability mechanism here.
- The proof does not identify different notions of psh and does not address
  the possibly discontinuous clause of CLD Definition 8.6.2.

## Promotion gate

Before promotion, freeze exact statement and proof hashes, submit those
exact bytes together with the exact imported dependency to production
Rethlas (`gpt-5.6-sol`, `xhigh`), require `correct` with zero critical errors
and zero gaps, archive the request/response/headers and service evidence,
compile the intended live placement, and run an independent hostile audit.
Until then there is no change to Chapter 16, Chapter 72, the atomic
inventory, or any provenance ledger.
