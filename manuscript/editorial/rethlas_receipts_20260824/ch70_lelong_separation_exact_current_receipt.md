# Chapter 70 generalized-Lelong separation candidate

> **Controlling disposition, 25 August 2026.**  The frozen theorem and proof
> recorded in this receipt were subsequently integrated as
> `thm:local-generalized-lelong-separation`; the former Chapter 72 environment
> and atom P10.1 were retired.  The production gate controls the frozen
> pre-integration bytes identified below, not a post-integration byte-identical
> extraction of the live TeX.  The older disposition language in this receipt
> is retained as dated audit history.

Date: 24 August 2026.  Live-manuscript disposition: **not yet integrated**.

## Exact frozen objects

- Statement packet:
  `manuscript/editorial/rethlas_packets_20260824/ch70_lelong_separation_candidate_statement.tex`.
  Size: 641 bytes.  SHA-256:
  `ef8316d19c121710280984d8954fefb9e9c14ce8737a4b9aef658c4c5120546e`.
- Source-aware proof packet:
  `manuscript/editorial/rethlas_packets_20260824/ch70_lelong_separation_candidate_source_aware_proof.tex`.
  Size: 9,306 bytes.  SHA-256:
  `57355a05bf4be050dfe54755eaf989ae3725782fc94b14dd9296b75e06e4dedd`.
- Solver dossier:
  `manuscript/editorial/solver_dossiers_20260824/lelong_separation_candidate.md`.
- Atomic question: P10.1, live label
  `prob:frontier-lelong-separation`.

The frozen theorem asserts literal pointwise equality of BFJ valuative
transforms.  It does not assert equality of the original psh germs, bounded
equivalence, equality only quasi-everywhere, or equality modulo constants.

## Production Rethlas result

- Service: isolated local production Rethlas.
- Model: `gpt-5.6-sol`.
- Reasoning effort: `xhigh`.
- Run: `20260824T140127Z_ef8316d19c12`.
- Started at: `2026-08-24T14:01:27.277166+00:00`.
- Process-guard deadline: `2026-08-24T14:59:46.287633+00:00`.
- Proof item: `pi_3114f2ee2498f163b2c41e7c`.
- Status/verdict: `final` / `correct`.
- Checked items: 1.
- Adaptive rounds: 1 (round 0 only).
- Expanded proof items requested: 0.
- Critical errors: 0.
- Gaps: 0.
- Return code: 0; output status: `validated`.
- Elapsed verifier time: 280.102 seconds.
- Billed verifier tokens: 118.
- Aggregate context digest:
  `6ff684659d53fda31a05bd3bedf13e24d72b5462a608a01d832f23c1f0990aa2`.
- Adaptive context digest:
  `e996e92eb8c5ce1b634343e20e577dc86a971b69d8fdcbd80cb4f5024b9e87eb`.
- Item context digest:
  `096ac53277f3273d23c30554c437d77702248776601ae57e61e92eacb057a55f`.
- Command digest:
  `09ac35864f120f455ead167a152058a83a7e58cfbbce888cab8a5f1591312f8d`.
- Aggregate manifest: 1,361 bytes; SHA-256
  `308247624877e1765afbedecb50d09216a6f71a25e76cd66a7cdbeab88f1553f`.
- Aggregate verification JSON: 964 bytes; SHA-256
  `cd5f534923561f72659f162224c3f033c9b55c5357673ca1d2ddd0b6674f80dc`.
- Round-zero verification JSON SHA-256:
  `6cbb34bdfaed5af6984c050139a660e5b84430466c21a09c88463edbbf4c4de2`.
- Round-zero log SHA-256:
  `50e5f7d4733c88f6ab911a16271851ba20417f023de4457e6dd9fcd9fe7e11fc`.
- Process-guard JSON SHA-256:
  `2d2ba0da88aad415f662f48858fb73d50e6b48aa4b879182f9eea5b58f399601`.
- Child-process-guard JSON SHA-256:
  `07f417c5d3d8a9474bbcffcad0727729fe210da0ca8f46451a9bdb674c9e7aad`.
- Archived exact response:
  `ch70_lelong_separation_exact_current_response_20260824.json`, 964 bytes,
  SHA-256
  `cd5f534923561f72659f162224c3f033c9b55c5357673ca1d2ddd0b6674f80dc`.

The authoritative run artifacts are under
`Rethlas_arxiv191209719_20260824/agents/verification/results/`
in the sibling Rethlas workspace.  The aggregate directory is
`20260824T140127Z_ef8316d19c12`; the round directory is
`20260824T140127Z_ef8316d19c12__0001_pi_3114f2ee2__round_0`.

## Exact primary-source locators

The source audited byte-for-byte was the official PRIMS PDF of
S. Boucksom, C. Favre, and M. Jonsson, *Valuations and plurisubharmonic
singularities*, PRIMS **44** (2008), 449--494:

<https://www.kurims.kyoto-u.ac.jp/~prims/pdf/44-2/44-2-18.pdf>

The downloaded PDF has 46 pages, 449,192 bytes, and SHA-256
`c7e8757e1e63ad0989f3fa3619094abc9352429dd7572116e0f65c0cd5a2033a`.
The following are printed-page locators, not viewer-page guesses.

- Theorem A, including condition (4): pp. 450--451; the expectation that
  (4) implies the other conditions is on p. 451.
- The explicit statement that `(4) => (1)` remains open: p. 456.
- Section 1.2, the identification
  `Div(pi) = NS(X_pi/X)_R`, uniqueness from numerical class, and the
  Cartier/Weil inverse systems: pp. 458--459.
- Proposition 1.14, including exact generation of the integral PA/Cartier
  group by `log|a|` for primary ideals: p. 466.
- Propositions 2.2 and 2.4, relative nefness and trace monotonicity: p. 469.
- Definition 2.8, the infimum-over-retractions extension: p. 470.
- Proposition 3.11, equivalence of nef Weil divisors and formal psh
  functions and continuity on each simplex: p. 474.
- Proposition 4.6, the Monge--Ampere/intersection identity: p. 482.
- Proposition 4.9, the atomic formula and the explicit observation that the
  intersection is finite when all but at most one input are Cartier: p. 483.
- Theorem 5.1: p. 485.
- Proposition 5.6: p. 486.
- Lemma 5.10: p. 487.
- Theorem B: statement on p. 455; proof on pp. 490--492.

For the sole non-BFJ global input, the source-aware packet uses the standard
Hodge--Riemann consequence that
`(L_1,L_2) -> L_1 L_2 H^{n-2}` has signature `(1,rho-1)` on
`N^1` for a smooth projective complex `n`-fold and ample `H`.  An exact
author-hosted locator is C. Voisin, *On the cohomology of algebraic
varieties*, Section 2.2.1 and Theorem 2.12, printed p. 11:

<https://webusers.imj-prg.fr/~claire.voisin/Articlesweb/template.pdf>

The audited 28-page PDF has 299,554 bytes and SHA-256
`26b374e2710a9223100aee4a414c4377b4b38cd7de7d42cf95d129f41823748e`.
For `H^{1,1}_R`, Theorem 2.12 makes the primitive hyperplane negative
definite and the line `R[H]` positive; restriction to the Neron--Severi
space gives precisely the form used in the packet.  The ampleness passage
`L` relatively ample and `M` ample implies
`L tensor f^*M^a` ample for `a >> 0` is also Stacks Project, Tag `0892`.

## Why primary-ideal tests determine every mixed Cartier intersection

This is an exact algebraic span argument; no density or continuity claim is
used.

1. For every `m`-primary ideal `a=(f_j)`, the analytic weight
   `phi_a=log max_j |f_j|` has isolated pole and
   `exp(phi_a)=max_j|f_j|` is locally Lipschitz.  BFJ Lemma 5.10 therefore
   makes it a permitted tame weight, and its b-divisor is `Z(a)`.
2. With one nef Weil input `W` and Cartier inputs `C_1,...,C_{n-1}`, the
   quantity
   `I_W(C_1,...,C_{n-1})=W_pi (C_1)_pi...(C_{n-1})_pi`
   is independent of the common determination by the projection formula.
   It is symmetric and multilinear in the Cartier slots.  BFJ Proposition
   4.9 expressly permits this one-Weil-input situation.
3. Equality of generalized Lelong numbers and Theorem B give the diagonal
   identity
   `Lambda(Z(a),...,Z(a))=0` for every primary `a`, where
   `Lambda=I_{Z(u)}-I_{Z(v)}`.
4. Products remain primary and
   `Z(product_i a_i^{k_i})=sum_i k_i Z(a_i)`.  Hence the homogeneous
   polynomial
   `P(t)=Lambda(sum t_i Z(a_i),...,sum t_i Z(a_i))`
   vanishes at every point of the positive integral lattice.  It is the zero
   polynomial, so every polarized mixed coefficient vanishes.
5. BFJ Proposition 1.14 is stronger than density: the integral Cartier
   b-divisor group is generated by the `Z(a)` themselves.  Every real
   Cartier b-divisor lies on one finite model, whose exceptional-prime basis
   is integral, and hence is a finite real linear combination of these
   generators.  Multilinearity therefore extends the mixed vanishing to
   arbitrary real Cartier inputs exactly.

Thus the proof never assumes that arbitrary real linear combinations of
analytic weights are tame, never approximates a Cartier divisor by ideal
divisors, and never polarizes singular currents.

## Line-by-line compactification and Hodge-index audit

Let `pi:Y->X` be a BFJ modification and `E_i` its exceptional primes over
the smooth point.

1. BFJ modifications are projective, birational, smooth, and unchanged off
   the point.  Embed `Y` relatively projectively, close its graph over a
   smooth projective compactification of `X`, and resolve only the boundary
   and singular locus.  This gives
   `bar pi:bar Y->bar X` with both spaces smooth projective and with the
   original map unchanged near the exceptional fibre.
2. Choose a `bar pi`-ample Cartier divisor `bar A`.  Its relative numerical
   class near the fibre has a unique exceptional real representative `A` by
   BFJ Section 1.2.  Relative ampleness is numerical, so `A` is `pi`-ample.
   The argument needs a real Cartier b-divisor, not an integral effective
   divisor.
3. Choose an ample Cartier divisor `B` on `bar X` and replace it by a large
   multiple.  Stacks Tag `0892` gives
   `H=bar A+bar pi^*B` ample on `bar Y`.
4. If `D,C` are supported on the exceptional fibre, all cycles obtained by
   intersecting them with further divisors remain supported over the point.
   In the telescoping expansion of
   `D C (bar A^{n-2}-A^{n-2})`, the factors other than `bar A-A` cut out a
   one-cycle in that fibre; `bar A-A` has degree zero on it because the two
   classes are relatively numerically equivalent.  In the binomial expansion
   of `D C H^{n-2}`, every term containing `bar pi^*B` vanishes because this
   pullback has degree zero on every fibre one-cycle.  Thus, term by term,
   `D C H^{n-2}=D C bar A^{n-2}=D C A^{n-2}`.
5. The Hodge--Riemann bilinear relations give signature `(1,rho-1)` for
   `q_H(L,M)=L M H^{n-2}` on `N^1(bar Y)_R`.
6. The vector `bar pi^*B` has positive `q_H`-square.  Indeed, intersect
   `n-2` sufficiently general members of a multiple of `H`; on the resulting
   surface the square of the pullback of the ample class `B` is positive.
7. Every local exceptional divisor `D` is orthogonal to `bar pi^*B` for
   `q_H`, because `bar pi^*B|_D` is pulled back from the single image point
   and is numerically trivial.
8. The orthogonal complement of a positive vector in a real form of
   signature `(1,rho-1)` is negative definite.  Hence `q_H` is negative
   definite on the numerical span of the `E_i`.
9. There is no coefficient-space kernel: global numerical triviality implies
   relative numerical triviality, and BFJ Section 1.2 identifies the latter
   exceptional class with zero only for the zero exceptional divisor.
10. Combining steps 4 and 8--9 proves that
    `Q_A(D,C)=D C A^{n-2}` is negative definite on the actual coefficient
    space `direct_sum_i R E_i`.  In dimension two this is the usual
    exceptional-curve matrix; for the blowup of a smooth point in any
    dimension, `A=-E` and `E^2 A^{n-2}=-1`, fixing the sign.

The separation step is then finite-dimensional: mixed vanishing with
`(C,A,...,A)` says `Q_A(Z(u)_pi-Z(v)_pi,C)=0` for every `C`, so the trace
difference is zero.  This holds on every model.  BFJ Proposition 3.11 and
Definition 2.8 then give pointwise equality on every quasimonomial simplex
and on all normalized valuations, respectively.

## Proposed live insertion, pending inspection

Insert a theorem with a non-eponymous label such as
`thm:local-generalized-lelong-separation` in
`manuscript/parts/part6/ch70_local_valuative_psh.tex` immediately after
equation `eq:local-generalized-lelong` and its normalization audit, presently
after line 608 and before the section
`sec:local-cld-gauss-shell`.  Give the complete proof there, using `\cref`
for internal references and preserving all existing `\eqref` calls.

Only after that theorem and its exact live proof have been reverified should
the live problem environment `prob:frontier-lelong-separation` in Chapter 72
be replaced by a resolved-history paragraph, P10.1 be removed from the active
inventory, and the research ledger, theorem-provenance ledger, verified-result
ledger, and Appendix L be updated.  No live chapter was changed in producing
this receipt.

## Novelty firewall

The exact proof has passed mathematical verification, but the literature
search performed for this dossier is not a priority search.  Until a broader
comparison is completed, describe the result only as a dated book-level
derivation, not as a first proof in the literature.
