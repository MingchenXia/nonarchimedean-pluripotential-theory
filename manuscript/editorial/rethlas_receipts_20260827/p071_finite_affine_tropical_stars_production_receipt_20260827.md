# P07.1 finite ambient-induced real-affine stars: production receipt

**Date:** 27 August 2026
**Local archive label:** `20260827T103835Z_c8131b22d800`
**Model:** `gpt-5.6-sol`
**Reasoning effort:** `xhigh`
**Verdict:** `correct`
**Critical errors:** `0`
**Gaps:** `0`

The direct production endpoint assigned neither a run identifier nor an item
identifier.  The label above is only the local archive address formed from
the request time and statement digest; no endpoint identifier is inferred or
invented.

## Exact mathematical bytes

| Artifact | SHA-256 |
|---|---|
| Frozen statement | `c8131b22d8002212e31cd526095317734a2b67be5d47f1387e5ee6bc041af5e3` |
| Frozen proof | `921e8b46690e69cbacea66bf86cbcdf628e7dbc95651f526d62cc6d755d7cbcf` |
| Standalone compiled PDF | `2c5b0caa18db6b9e8154cc77b56847e1724f0a5424dfc5ad53eb577278e71712` |
| Compile driver | `cb3a4457b56148bb0196c020e7f6be9707a0537820c2a2696206b0eb5078d434` |
| Compile log | `226aa6ddfe8b9831213a18673f473bc4d46df28bce737c4200291ea5ee290a64` |
| Frozen manifest | `e30250a237db993530214118ab1142309e4833f64fc57bdc33cc2951adc5827c` |

The standalone wrapper compiled the exact statement and proof to five pages.
Its log has no TeX error, unresolved reference or citation, rerun request, or
box warning.

## Exact request and response

| Artifact | SHA-256 |
|---|---|
| Endpoint request | `ac68faee9ddb39bd3a30373e193196fc0a25431477a34e5c9cea6b49947299ed` |
| Endpoint headers | `2d161b58dbf027d6e9461e11cb0008b582425f0adb2d1ad29318d4c43398d17e` |
| Endpoint response | `4f9a8b82e6eb7134cf76a5eac5ac0313db8f0e6cca082d369976db04ec115cfe` |

The archived request contains the complete exact statement and proof.  The
response says that the proof is correct and records successful checks of the
sheaf-local Jensen argument, ambient tangent supports, the finite/polar branch
dichotomy, exclusion of polar rays from nonnegative zero relations, nested
chordal majorants, the proved Farkas alternative, common affine minorants,
regularized-max smoothing with a common ambient germ, the exact monotonicity
budget on one fixed neighbourhood, and chartwise descent.

## Independent audits

Three independent pre-integration audits passed on the same frozen bytes.
They separately recomputed the proof and its numerical error ledger, checked
the statement against the CLD generator and hierarchy definitions, and
mapped every live-book scope and provenance change.  No critical error or gap
was found.

The source audit also detected and repaired an older Chapter 10 overstatement:
for a general balanced one-star, ambient slope germs form the annihilator of
the full relation space, not necessarily the whole hyperplane defined by one
chosen balancing relation.  The verified proof already uses all nonnegative
relations and is unaffected by that correction.

## Exact scope

The theorem concerns a finite set of pairwise distinct positive rays in a
finite-dimensional real vector space with the ambient-induced smooth,
branchwise-convex stage-zero sheaf.  It characterizes the generated psh sheaf
by branch convexity and every junction Jensen inequality, proves collapse at
the first sequential stage, and constructs decreasing smooth approximants on
one fixed neighbourhood.  It uses no lattice, rationality, weight, balancing,
calibration, harmony, or boundary designation.

This is a finite real-affine-star theorem, not an assertion about every object
called a tropical cycle or tropical boundary.  It does not automatically
cover positive-sedentarity charts, constant-near-endpoint smooth structures,
infinite-valence stars, or higher-dimensional faces.  The toric sedentary
case remains controlled by the separate toric theorem.  Consequently P07.1
and P07.2 remain active, and the inventory stays at sixteen formal problem
environments and fifty-five atoms.
