# P07.1 finite unbranched complex follow-up: source and obligation matrix

Date: 30 August 2026 (Asia/Shanghai)

Status: **isolated candidate; no production submission; no live-book edit**.
The mathematical content is a chart-transport consequence of one pinned,
production-verified theorem plus an elementary two-ray obstruction.  It makes
no novelty or priority claim.

## Principal files

The principal files are `statement.tex` and `proof.tex` in this directory.
Their hashes are recorded in `SHA256SUMS` after the build is frozen.

## Exact dependency D1

The only non-elementary theorem used is the Stone-parameter times one convex
polyhedron result:

`/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260830/p071_stone_polyhedral_corners_v2_20260830/`

| Artifact | SHA-256 | Role |
|---|---|---|
| `statement.tex` | `b46b8e22fa8b3f8f64dcf8ae24d164b905dbe8d9035e37c3ede23321717cc002` | exact model theorem, including fixed-domain approximation and chart-local transport |
| `proof.tex` | `37a3b6a12f6ddd2a3038dd926dfe8120d8955756efe64608fbd2a37b33c01efb` | proof of the model theorem |
| `SOURCE_AND_OBLIGATION_MATRIX.md` | `9dcb2c8bab8fb47e3cdeebb8821776770fa1929b2712afbc047bddeed94ae1c0` | exact CLD and Stone source ledger |
| `INDEPENDENT_EXACT_SOURCE_RECHECK_20260830.md` | `3ff43da8dd1044a0144d6f1410ad5b66020ff868c934886c87f3bc38b5c0f974` | PASS, zero provenance gaps |
| v1 exact-byte hostile audit | `1d74c658835a2a9459350bc7e4509b7fbed3686b2c9bde9d31f24465242c3045` | PASS, zero critical mathematical errors and zero proof gaps, on the same principal bytes |
| `PRODUCTION_RECEIPT.md` | `4d00534170a7d5b15582eb3ab4878bd79912b919ea19d9dc8fe6be5822a40955` | records the dependency-closed production verdict |

The production archive is the sibling directory
`p071_stone_polyhedral_corners_v2_production_run_20260830`.  Its exact
transport artifacts are:

| Artifact | SHA-256 / verdict |
|---|---|
| `request.json` | `6697bc79ad50c8b7a9cf3c63dc63fd5b08a9930f9369b304595254f635573d11` |
| `response.json` | `c5871408ef86be152ecd6e169eaae05f590feef00e5487d37f185780951d5285`; `correct`, zero critical errors, zero gaps |
| `headers.json` | `5d7e0c5e93c43726ef62b2204ea7fdde2929d76f3715c87874662570657b50c6` |

Before freezing this dossier, every listed local hash must be recomputed.
The follow-up theorem does not enlarge D1 inside any chart: each complete
germ is assumed to be generator-preservingly identical to the precise D1
model.

## Primary-source chain inherited through D1

No external source beyond D1's exact CLD artifact is used.  D1 pins
Chambert--Loir--Ducros,
*Formes différentielles réelles et courants sur les espaces de Berkovich*,
arXiv:1204.6277v2 (25 July 2025), through:

| Artifact | SHA-256 |
|---|---|
| `/private/tmp/CLD25_1204.6277.pdf` | `5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719` |
| `/private/tmp/CLD25_reextracted_layout_p071_20260830.txt` | `021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e` |
| `/private/tmp/CLD25.txt` | `021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e` |

The two text files were regenerated/compared byte for byte in D1.  The
relevant ranges are CLD §§1.8.2--1.10.1, 6.1.4, 6.2.1, 8.1.1, 8.1.4,
and 9.1.1--9.1.4, exactly as itemized in D1's source matrix.  Two ranges are
especially relevant to the present firewall:

- CLD Remark 1.9.15, extraction lines 2585--2601, explicitly states that
  smoothness on a parlinear subset depends on its embedding and exhibits a
  bent two-segment space whose projection is parlinearly isomorphic to an
  interval although the two smooth sheaves differ;
- CLD Definition 1.10.1, extraction lines 2628--2643, defines positivity by
  restriction to cells and says it suffices to test maximal cells of a
  cellular decomposition.

These exact passages support the distinction between a piecewise-affine
unfolding and a **generator-preserving** unfolding.  This follow-up does not
claim that an arbitrary CLD affine tropical complex satisfies the latter
hypothesis.

## Obligation ledger

| ID | Obligation | Discharge | Status |
|---|---|---|---|
| O1 | State “unbranched” strongly enough to exclude a merely codimension-one-unbranched singular complex. | `statement.tex` requires a complete-germ homeomorphism onto a relatively open convex subset of one polyhedron, with cell subdivision and generator preservation. | discharged |
| O2 | Show that generator-preserving transitions preserve the first and full psh stages. | `proof.tex`, equations (stage-zero transport) and (all-stage transport): transport sequences termwise; use minimality in both directions. | discharged |
| O3 | Make the comparison sheaf independent of the chart. | Comparison in chart A equals model stage one by D1; O2 transports stage one to chart B; D1 converts it back to the factorized fibrewise-convex condition after a convex shrinking. | discharged |
| O4 | Prove the sheaf equality on the complex without assuming a global development. | Choose one chart at each germ and transport the three D1 sheaves.  Equality is stalk-local. | discharged |
| O5 | Produce one fixed-neighbourhood decreasing sequence which handles every face at the germ simultaneously. | Apply D1 once on the one convex chart target, then pull back the whole sequence.  No chamberwise gluing occurs. | discharged |
| O6 | Avoid hidden metrizability or second countability of the Stone factor. | No such property is introduced.  D1 metrizes only its countable Boolean quotient; O2 is purely topological.  Finiteness of the complex is stronger than the local proof needs. | discharged |
| O7 | Treat loop/circle monodromy. | The proof never continues a chart around a loop.  It asserts a local sheaf equality, not a single global approximating sequence. | discharged within stated scope |
| O8 | Show why face-to-face plus cellwise positivity is insufficient for this reduction. | The two perpendicular rays and the ambient affine generator `-x-y` yield decreasing one-sided slopes after every affine unfolding. | discharged |
| O9 | Check zero-dimensional, lower-dimensional, unbounded, boundary, and corner cases. | They are explicit cases of D1; the proof records affine-span, relative-neighbourhood, and bounded-core conventions. | discharged |
| O10 | Firewall branching, nonconvex unions, and singular lower links. | Excluded in the statement and detailed in `EDGE_CASES_AND_OBSTRUCTIONS.md`. | discharged |
| O11 | Prevent “convex on each cell” from being mistaken for convexity across a subdivision. | The comparison condition quantifies over every convex combination in the whole chart target.  The straight two-edge and balanced-star Jensen tests in the edge ledger show the missing inequalities. | discharged |

## Logical scope

This dossier proves a precise local extension, not the unrestricted finite
complex case.  In particular:

- it does not deduce cross-face convexity from agreement on a face;
- it does not prove that independently smoothed chamberwise approximants can
  be glued monotonically;
- it does not assert a single global decreasing sequence on a compact
  complex;
- it does not resolve P07.1 for an arbitrary balanced, branched, nonconvex,
  or ambient-cellwise CLD tropical space.

Any promotion must preserve those four exclusions verbatim or re-open the
corresponding obligations.
