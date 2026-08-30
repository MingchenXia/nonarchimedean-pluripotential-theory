# Dependency ledger

Date: 30 August 2026

Status: exact staging metadata only. This packet is not included by the live
manuscript and has not been submitted to production Rethlas.

## Wrapper identifiers

The candidate results have no `\label` commands in the frozen statement or
proof. The compile wrapper records only these editorial identifiers:

- Candidate A: `prop:p061-frobenius-rpl-descent`
- Candidate B: `thm:p061-simplicial-toric-ph-rpl`

No conventional theorem name, novelty claim, or priority claim is attached.

## Dependency graph

```text
D3 + D4 ----------------------------> Candidate A
Candidate A + D1 + D2 + D3 + D5
            + D6 + D7 + internal
            lattice/Frobenius proof -> Candidate B
```

All lattice, semigroup-ring, characteristic decomposition, radiciality,
affinoid `q`-power, Reynolds-projector, and non-full-dimensional arguments are
proved in the candidate proof itself.

## D1 — production-verified quasi-smooth P06.1 input

Exact live label: `thm:p061-quasismooth-ph-rpl`.

Statement used: if $K$ is complete and nontrivially valued and $X$ is a
good strict quasi-smooth $K$-analytic space, then every classically
pluriharmonic real function on $X$ is real-PL and GJR harmonic. There is no
global quasicompactness, separatedness, or boundarylessness hypothesis.

Frozen packet:

- `manuscript/editorial/rethlas_packets_20260829/`
  `p061_quasismooth_ph_rpl_20260829/`
- statement: `p061_quasismooth_ph_rpl_statement_20260829.tex`
- proof: `p061_quasismooth_ph_rpl_source_aware_proof_20260829.tex`
- statement SHA-256:
  `0b1b4d161e3b85d342d7be88234a8ed27bfe74be4d24a639ff0456373a7a39e9`
- proof SHA-256:
  `fdc6abcc4988644656892172fbdbda4178cb86ca710fd0122a90947e598b0b8b`
- production run: `20260829T043457Z_0b1b4d161e3b`
- item: `pi_7cd35ebd843cf80a7cd696bb`
- verdict: `correct`, zero critical errors, zero gaps.

Only the quasi-smooth theorem is used here; the rigid-étale lemma and annular
counterexample in the same frozen statement are not dependencies of this
candidate.

## D2 — production-verified finite constant-group descent

Exact live label: `prop:p061-finite-group-rpl-descent-candidate`.

Statement used: let a finite constant group $G$ act analytically on a
separated strict affinoid $Y$, with analytic categorical quotient
$q:Y\to X=Y/G$. If a continuous real function $g$ on $X$ has real-PL
pullback, then $g$ is real-PL. No flatness, étaleness, freeness,
reducedness, normality, or restriction on the group order in the ground or
residue field is assumed.

Frozen packet:

- `manuscript/editorial/rethlas_packets_20260830/`
  `p061_finite_quotient_gdescent_audit_20260830/`
- statement: `p061_gdescent_candidate_statement_20260830.tex`
- proof: `p061_gdescent_candidate_proof_20260830.tex`
- statement SHA-256:
  `e1daa4b3e3efd64fcc8f0ce05b9c1d5d6cb69b28686b939b48535fc56b0ccc07`
- proof SHA-256:
  `a6c24d1686c726dc72aebe55a1e83eb8d4fe1ed4025d4a8d7166da59123ce30e`
- production run: `20260829T235341Z_e1daa4b3e3ef`
- verdict: `correct`, zero critical errors, zero gaps.

The candidate proof separately verifies that the split prime-to-$p$
restriction over each target affinoid is the analytic categorical quotient
required by D2.

## D3 — published real-PL and harmonic definitions

Walter Gubler, Philipp Jell, and Joseph Rabinoff, *Forms on Berkovich spaces
based on harmonic tropicalizations*, BSMF 154 (2026), 135–238,
DOI `10.24033/bsmf.2919`.

Exact portions used:

- Definition 5.1: a real-PL function is G-locally a finite real linear
  combination of logarithms of analytic units.
- §5.2(3): restriction to a strictly analytic domain preserves real-PL.
- §5.2(4): real-PL functions form a sheaf for the G-topology and hence the
  analytic topology.
- Definition 7.2: an R-PL function is harmonic exactly when it and its
  negative are semipositive at every point.

Official primary PDF:
`https://smf.emath.fr/system/files/filepdf/GUBLER_JELL_RABINOFF.pdf`.

## D4 — rational refinement and finite analytic base change

Two foundational inputs are used.

1. Gerritzen–Grauert: every affinoid domain of a strict affinoid space has a
   finite cover by rational domains. Exact primary locator: Michael Temkin,
   *A new proof of the Gerritzen–Grauert theorem*, Theorem 1.1 and the
   explicit consequence in the introduction; the paper identifies the
   classical locator as BGR 7.3.5/1.
   `https://math.huji.ac.il/~temkin/papers/Gerritzen_Grauert.pdf`.
2. Affinoid fibre products and finite morphisms: for affinoids, the fibre
   product algebra is the completed tensor product; a finite morphism pulls
   back every target affinoid to an affinoid with finite algebra. Exact
   locators: Michael Temkin, *Introduction to Berkovich analytic spaces*,
   Fact 4.1.16 and Definition 4.2.5.
   `https://berkovich-2010.imj-prg.fr/lecture-notes/Temkin-lecture-notes.pdf`.

The only completion issue needed here is also proved directly: a tensor
product which is finite over an affinoid algebra is already complete because
finite submodules of finite affinoid modules are closed.

## D5 — published classical pluriharmonic functoriality

Walter Gubler and Joseph Rabinoff, *Classically psh and pluriharmonic
functions on Berkovich spaces*, arXiv:2506.13548v2.

Exact portions used:

- Proposition 7.2(6): a real function is classically pluriharmonic if and
  only if its scalar pullback along an analytic extension field is.
- Proposition 7.2(7), forward direction: arbitrary analytic pullback
  preserves classical pluriharmonicity.

Local primary PDF:

- `manuscript/editorial/rethlas_packets_20260830/`
  `p031_perfected_unibranch_curve_envelope_20260830/sources/`
  `Gubler_Rabinoff_2506.13548v2.pdf`
- SHA-256:
  `83ca9a19394f44bb2e4e1aa316de95938f311acd53a00fe250fa0f605184b726`

Official URL: `https://arxiv.org/pdf/2506.13548v2`.

## D6 — published scalar descent for real-PL functions

Gubler–Jell–Rabinoff, Corollary 5.12: if $X$ is good and strict,
$K'/K$ is the completion of an algebraic extension, and the coefficient
group is divisible, then a real function on $X$ is PL with those
coefficients if and only if its scalar pullback to $X_{K'}$ is. Candidate
B applies this with the divisible group $\mathbf R$ and a finite, hence
complete, extension $L/K$.

Primary source and URL are those in D3.

## D7 — published classical psh/semipositivity comparison

Gubler–Rabinoff, Theorem 4.3: over a nontrivially valued field, an R-PL
function on a good strict analytic space is semipositive if and only if it is
classically psh. Candidate B applies this to both $h$ and $-h$, then uses
D3, Definition 7.2.

Primary source, local PDF, hash, and URL are those in D5.

## Excluded dependencies

The proof does **not** use GJR Proposition 5.11 (finite-flat PL descent), a
trace or norm, perfectness of $K$, a constant presentation of the
$p$-primary diagonalizable factor, ordinary analytic étale descent,
log-étale comparison, or any non-simplicial toric uniformization.
