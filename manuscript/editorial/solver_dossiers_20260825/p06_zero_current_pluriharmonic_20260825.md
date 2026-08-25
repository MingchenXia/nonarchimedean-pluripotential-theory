# P06.2 solver dossier: zero CLD current and pluriharmonicity

**Status:** narrowed.  The real-PL case is solved by a production-verified
argument.  The arbitrary continuous case remains open in higher dimension;
the smooth proper curve case is published.

The verified result was subsequently integrated as
`prop:ch18-real-pl-zero-current-harmonic`, with the continuous smooth-proper-
curve consequence recorded as `cor:ch19-continuous-zero-current-harmonic`
and the residual higher-dimensional continuous problem retained in
`prob:frontier-pluriharmonic`.

## Exact live question audited

Chapter 72 asks whether a continuous function `h` with
`d'd''[h]=0` is classically pluriharmonic, or harmonic where that notion is
defined.  Its warning is correct: an arbitrary CLD current has no general
pullback to the curve probes in the definition of classical psh, and
cell-interior affinity alone does not establish balancing at faces.

Three regularity levels must remain separate:

1. arbitrary continuous functions;
2. real PL functions;
3. weakly smooth functions.

GJR Proposition 10.17 already treats level 3 when the equality is an
equality of weakly smooth forms.  The production-verified packet now treats
level 2 when the equality is an equality of CLD currents.  It does not
treat level 1.

## Result now available for integration

Let `K` be complete and nontrivially valued.  Let `X` be a good, separated,
boundaryless, strictly `K`-analytic space, pure of dimension `n >= 1`.  If
`h` is real PL and

```text
d'd''[h] = 0
```

as a CLD current, then `h` is GJR harmonic and classically
pluriharmonic.  Equivalently, `L_h(x)` is numerically trivial for every
`x`.

The exact accepted statement and proof are frozen in
`../rethlas_packets_20260825/p06_real_pl_zero_current_skeletal_round2_*`.
The controlling receipt is
`../rethlas_receipts_20260825/p06_real_pl_zero_current_skeletal_round2_production_receipt.md`.
The subsequent live-chapter installation and focused compile are recorded in
`../rethlas_receipts_20260825/p06_real_pl_zero_current_live_integration_receipt.md`.

## Why the accepted proof works

Locally write `h = sum lambda_i h_i`, where the `h_i` are integral PL and
the `lambda_i` are Q-linearly independent.  CLD Example 7.5.3 and Theorem
8.10.3 realize each `d'd''[h_i]` as a skeletal current.  On a common
refinement of the canonical analytic skeleton, its codimension-one
calibrations have integer coefficients in primitive lattice normalization.
The zero current has zero calibration.  Q-linear independence therefore
forces every integral summand calibration to vanish.

To recover the full analytic current, refine once more by the moment map
tropicalizing each arbitrary test form.  CLD Definition 7.5.1 and Remark
7.2.5 then evaluate the current directly against a compactly supported
analytic cutoff times that chart form.  No current pullback and no target
boundary cutoff occur.  CLD Theorem 18.8.4 with `d=1` turns vanishing of
each integral curvature current into numerical triviality; GJR
Proposition 7.1/Definition 7.2 and GR Theorem 4.3 finish the argument.

## Rejected route that must remain quarantined

Production round 1, run `20260825T031243Z_1603e0a83037`, item
`pi_ef4b8ab22822f1ccc0242d30`, returned `final/wrong`.  It tried to use the
boundary-separation step from the proof of GJR Proposition 9.6 to represent
an arbitrary complementary test form by a target form compactly supported
in `G(U) minus G(boundary U)`.  The cited construction separates a chosen
full-dimensional Abhyankar point; it does not establish the required
statement for the entire support of an arbitrary test form.  This is
already false as a formal use of the source in dimension one, where a
compactly supported `(0,0)` test function can contain rigid points.

All round-1 response, verification, log, and guard files are preserved
under `../rethlas_receipts_20260825/p06_real_pl_zero_current_round1_*`.

## Published continuous curve scope

For an algebraically closed complete nontrivially valued field, a smooth
proper algebraic curve `C`, and an open `W` in `C^an`, Wanner Theorem 4.7
and Corollary 4.8 identify positivity of `d'd''[u]` for a continuous `u`
with Thuillier subharmonicity.  Hence `d'd''[h]=0` makes both `h` and `-h`
subharmonic, so `h` is Thuillier harmonic.  GJR Proposition 15.7 identifies
this with GJR harmonicity on a rig-smooth curve, and the real-PL comparison
then gives classical pluriharmonicity.  This published scope is already
recorded in Chapter 19 and the R3 source report.

Do not silently enlarge this to singular curves, arbitrary base fields, or
higher-dimensional spaces.  Such enlargements require separate descent,
normalization, or current-pullback arguments.

## Remaining open scope

The following is not resolved by the accepted packet:

> On a higher-dimensional good separated strict boundaryless analytic
> space, does every continuous function `h` satisfying
> `d'd''[h]=0` have to be classically pluriharmonic?

The obstruction is no longer the real-PL coefficient problem.  It is a
regularity/recovery problem: current vanishing for an arbitrary continuous
function supplies neither an integral skeletal calibration nor a legitimate
pullback of the current to all analytic curves.  A successful proof would
need a regularization theorem, a local potential theorem placing `h` in the
weakly smooth or PL class, or an independent curve-test recovery theorem.

## Production ledger

- Round 1: `final/wrong`, run `20260825T031243Z_1603e0a83037`, proof digest
  `143681464cd8fc40882f4e2fbdc806d5555cdbcb544559ad6deebcb7cb5ba1f4`.
- Round 2: `final/correct`, run `20260825T032958Z_3a27f19be958`, item
  `pi_f2130d5e31ef3d5934410c10`, proof digest
  `c37af7bb8acbc388056f90ca97009f80b30cbea36ebaf10927400ef29364cbda`.
- Model and scrutiny for both: `gpt-5.6-sol` / `xhigh`.
- No novelty or priority claim is made.

## Exact-live repair addendum, 25 August 2026

The preceding accepted-packet discussion is historical.  A live audit found
that the integrated proof needed one common G-local tropicalization before
choosing the strict affinoid, rational rather than asserted integral
calibrated coefficients, a source-side cutoff, and the localized test
decomposition from CLD Corollary 6.2.8 and Lemma 7.2.5.  Exact-live
intermediate run `20260825T055921Z_655e7f503e5d` rejected the order of the
common-chart construction and an undeclared internal comparison reference.
Both were repaired.  The current v4 proof passed run
`20260825T061351Z_655e7f503e5d`, item
`pi_eea98ea0a54108cae4e076be`, final `correct`, zero critical errors and zero
gaps.  Its statement/proof SHA-256 values are `655e7f503e5d...` and
`7ad130bab1d9...`.  This exact-live run alone controls the current theorem;
all earlier runs remain preserved and non-controlling for the current bytes.
