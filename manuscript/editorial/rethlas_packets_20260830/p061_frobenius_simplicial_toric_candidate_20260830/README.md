# P06.1 Frobenius/simplicial-toric candidate packet

Date: 30 August 2026

Status: **exact staged candidate only**. Nothing in this directory is
included by the live manuscript, licensed for live integration, or submitted
to production Rethlas.

## Contents

- `p061_frobenius_simplicial_toric_candidate_statement_20260830.tex` — exact
  statements for Candidate A and Candidate B.
- `p061_frobenius_simplicial_toric_candidate_proof_20260830.tex` — exact
  dependency-aware proofs.
- `DEPENDENCY_LEDGER.md` — exact live labels, production receipts, hashes,
  and published dependency statements.
- `SOURCE_MATRIX.md` — primary-source proposition/definition locators and
  URLs or local primary PDF path.
- `HOSTILE_AUDIT.md` — nonflatness counterexample, proof-interface checks,
  and scope firewalls.
- `p061_frobenius_simplicial_toric_candidate_compile_20260830.tex` — minimal
  wrapper; editorial labels occur only in its metadata block.
- `p061_frobenius_simplicial_toric_candidate_compile_20260830.pdf` — clean
  minimal compile.
- `SHA256SUMS` — frozen hashes for all preceding packet artifacts except the
  checksum file itself.

## Editorial identifiers

- Candidate A: `prop:p061-frobenius-rpl-descent`
- Candidate B: `thm:p061-simplicial-toric-ph-rpl`

The statement and proof contain no theorem `\label` commands and attach no
conventional theorem names.

## Exact scope

Candidate A reflects real-PL regularity through a finite surjective radicial
map in characteristic $p$ under a uniform affinoid $q$-power condition
and reduced target. Candidate B proves classical pluriharmonic
$\Rightarrow$ real-PL and GJR harmonic on good strict analytic domains of a
split affine toric variety associated to a strongly convex simplicial cone,
including non-full-dimensional cones and wild equal-characteristic lattice
indices.

The ordinary analytic étale-chart corollary was deliberately omitted. The
packet makes no non-simplicial, log-étale, general toroidal, or arbitrary
singularity claim.

## Build

From this directory:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error \
  p061_frobenius_simplicial_toric_candidate_compile_20260830.tex
```

The compile wrapper has no bibliography and no dependency on the live book
preamble.
