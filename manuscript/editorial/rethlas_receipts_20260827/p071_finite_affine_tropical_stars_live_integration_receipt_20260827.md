# P07.1 finite ambient-induced real-affine stars: live integration receipt

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

## Exact-byte identity

Chapter 16 inputs the following files directly, without mathematical-text or
label transformation:

- statement:
  `editorial/rethlas_packets_20260827/p071_finite_affine_tropical_stars_statement_20260827.tex`,
  SHA-256
  `c8131b22d8002212e31cd526095317734a2b67be5d47f1387e5ee6bc041af5e3`;
- proof:
  `editorial/rethlas_packets_20260827/p071_finite_affine_tropical_stars_proof_20260827.tex`,
  SHA-256
  `921e8b46690e69cbacea66bf86cbcdf628e7dbc95651f526d62cc6d755d7cbcf`.

The production request, response, and headers have SHA-256 digests
`ac68faee9ddb39bd3a30373e193196fc0a25431477a34e5c9cea6b49947299ed`,
`4f9a8b82e6eb7134cf76a5eac5ac0313db8f0e6cca082d369976db04ec115cfe`,
and
`2d161b58dbf027d6e9461e11cb0008b582425f0adb2d1ad29318d4c43398d17e`.
The exact standalone PDF, compile driver, and compile log have digests
`2c5b0caa18db6b9e8154cc77b56847e1724f0a5424dfc5ad53eb577278e71712`,
`cb3a4457b56148bb0196c020e7f6be9707a0537820c2a2696206b0eb5078d434`,
and
`226aa6ddfe8b9831213a18673f473bc4d46df28bce737c4200291ea5ee290a64`.
Every entry of the frozen packet manifest verifies; the manifest digest is
`e30250a237db993530214118ab1142309e4833f64fc57bdc33cc2951adc5827c`.

## Mathematical and source audits

Three independent pre-integration audits passed on the exact frozen bytes.
They recomputed the sheaf-local Jensen characterization, the extended-value
and polar-branch cases, the tangent-support and Farkas alternatives, the
common affine minorant, regularized-maximum smoothing, the exact decreasing
error budget on one fixed neighbourhood, and chartwise descent.  A separate
source audit checked compatibility with the ambient-induced CLD generator
hierarchy and forced the distinction from positive-sedentarity and
nonambient smooth structures.

The source audit also repaired the older Chapter 10 slope statement: the
ambient slope image on a one-star is the annihilator of the full linear
relation space among the ray generators, not in general the hyperplane cut
out by one chosen balancing relation.  The live theorem uses every
nonnegative zero relation and is therefore unaffected by that correction.

A fresh hostile post-integration audit then compared the production request
byte-for-byte with both frozen files, confirmed their direct Chapter 16 and
`book.fls` inputs, recomputed every proof step through chart descent, and
scanned all live scope statements in Chapters 10, 16, 19, and 72 and
Appendix L.  It returned `PASS` with no mathematical, scope, byte-identity,
or build defect and made no edits.

## Exact scope and non-claims

The integrated theorem treats a finite union of pairwise distinct half-open
rays in a finite-dimensional real vector space, with the smooth structure
and the stage-zero psh generator sheaf induced by restrictions of ambient
smooth functions.  It proves that the first decreasing-limit stage, the full
generated psh sheaf, and the branchwise-convex junction-Jensen sheaf coincide.
Every germ has a decreasing sequence of smooth psh approximants on one fixed
neighbourhood, and the result descends under local identifications preserving
the generator sheaf.

The theorem assumes no lattice, rationality, weight, balancing, calibration,
harmony, or boundary designation.  It does not identify its ambient-induced
sheaf with every positive-sedentarity, constant-near-endpoint, analytic, or
nonambient tropical smooth structure.  It does not treat infinite-valence
stars or arbitrary higher-dimensional polyhedral spaces.  Accordingly P07.1
and P07.2 remain active and the inventory remains at sixteen formal problem
environments and fifty-five active atoms.

## Whole-book gate

- Final PDF: 3,187 pages, 15,344,143 bytes, SHA-256
  `1516064109f0c8c8ebc38b9c2e9e7a99ff8749d44881578b65c132a44ba6184d`.
- Final log SHA-256:
  `a80d466b3a330c6dee653ec7134e9728a7f8a11bcd5acf7fb33b5e3d7286330a`.
- No TeX error, undefined reference or citation, duplicate label or
  destination, BibTeX or index warning, rerun request, or overfull box.
  There are 991 underfull-box notices from the monograph layout and long
  tables.  The only `Warning:` line is the harmless historical class-path
  mismatch: the requested local file `style/svmono` declares itself as
  `svmono`.
- Exact source closure: 119 files; manifest SHA-256
  `4419d2cfb1f64525f81d1e7a21d734c5ed716099c4a4ed9a78d84f641609e962`;
  every entry verifies.
- Structural frontier: 16 formal problem environments and 55 active atoms,
  with tier counts 7/14/17/17.
- Author blank; acknowledgements empty; no exercises; no optional
  conventional theorem-like names.
- Rendered inspection passed on physical PDF pages 431--432, 679--680,
  692, 721--729, 1002--1005, 3002--3006, and 3161--3163.  These pages cover
  the corrected slope convention, hierarchy context, exact theorem and
  proof, limitations table, open-problem status, provenance, and all
  neighbouring page transitions.

This receipt controls exact-byte integration and scope.  It makes no novelty
or priority claim.
