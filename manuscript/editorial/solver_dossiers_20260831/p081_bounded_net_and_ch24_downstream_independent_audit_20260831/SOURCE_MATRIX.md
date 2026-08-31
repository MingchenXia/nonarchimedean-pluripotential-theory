# Source and dependence matrix for the two downstream reviews

Date: 2026-08-31. This ledger records sources actually inspected and distinguishes their use from fresh theorem certification. The two reports in this directory review exact p081-authored downstream fragments; they do not independently re-prove the reviewer's earlier Chapter 20 density route.

## A. Primary BFJ bounded Monge--Ampere source

Authors: Sebastien Boucksom, Charles Favre, Mattias Jonsson. Title: *Solution to a non-Archimedean Monge--Ampere equation*. Primary arXiv identifier: [1201.0188](https://arxiv.org/abs/1201.0188). The local PDF bears arXiv:1201.0188v1, 30 December 2011, and has 47 pages. Its later PDF creation metadata is not treated as a different mathematical version.

- Exact local PDF: `/Users/mingchen/Projects/Yethlas/tmp/BFJ_MA_1201.0188.pdf`.
- PDF SHA-256: `4c29d91987477baf9baa4dfdd0b901ae1cd8910746012fd6285ab9a90bbf3f3a`.
- Read-only layout extraction: `/private/tmp/BFJ_MA_1201.0188_downstream_audit_20260831.txt`.
- Text SHA-256: `4a7e7bb3a11660fbcce5e32ee5a4aafd411668eb5585b3105073d4e8b8c0f4a1`.
- Inspected: title/abstract and section structure; Section 2.1, pages 8--9; Section 3, pages 16--18, including Theorem 3.1, its surrounding hypotheses, Corollary 3.3, and the beginning of the construction.
- Visual QA: PDF pages 16 and 17 were rendered and viewed in full. These confirm the arbitrary real theta, ample generic class, bounded psh, and decreasing-net clauses. Images are temporary source-inspection aids, not output artifacts or candidate-PDF QA.

| Source locator | Exact usable interface | Scope firewall |
| --- | --- | --- |
| Section 2.1 | Complete discretely valued ground field, residue characteristic zero; smooth projective integral algebraic variety and its analytification. | No algebraic closure of the ground field is imposed by this standing setup. This is not an arbitrary-field extension. |
| Section 3 opening | A real closed model form theta with ample generic numerical class. | Does not require theta itself to be semipositive; convenient positive-reference presentations are a separate gauge choice. |
| Theorem 3.1 | Positive bounded Monge--Ampere measures of the fixed total mass and weighted continuity when all bounded psh entries decrease in bounded nets. | The additional function-field condition in the main existence theorem is not imposed on this Section 3 bounded-operator theorem. |
| Following Theorem 3.1 | Affinity in each entry and formal expansion to the relevant differences. | Signed products are handled by finite multilinear expansion, not by declaring a signed weight psh. |
| Corollary 3.3 | The Dirichlet pairing on differences of bounded psh functions has the stated negative-semidefinite sign. | Supports the bounded variation interpretation; it does not authorize differentiation of arbitrary nonpolynomial net limits. |

No GJKM degree-zero claim, real-model-maximum closure claim, or arbitrary-valued-field regularization theorem is used in these reports.

## B. Book interfaces inspected directly

All paths below are relative to `/private/tmp/nappt_p071_20260827`. Exact source files and hashes are also bound by the author packets' `SOURCE_HASHES.json`, whose entries were independently checked. Their unchanged labels are preferable to unstable line numbers for future use.

| Source | Inspected interface | Use and independence limit |
| --- | --- | --- |
| `manuscript/parts/part3/ch24_bfj_ma.tex`, `eq:ch24-standing` and following reference-change discussion | Real theta, ample generic class, complete-DVR/residue-zero standing scope; change of reference. | Confirms no accidental theta-semipositivity restriction in Chapter 24/30. Not a new audit of all reference-change theory. |
| Same, scalar mixed-pairing construction preceding `thm:ch24-energy-extension` | The model-intersection scalar pairing and its construction precede and do not assume the Chapter 26 energy functional. | Checks the chronology needed for Chapter 26 Step 4. |
| Same, `lem:ch24-psh-difference`, `lem:ch24-sandwich`, `thm:ch24-energy-extension` | Dense span of psh model tests and weighted scalar monotone extension. | Read relevant proofs and their use; do not replace the stated hypotheses by arbitrary continuous psh-difference decompositions. |
| Same, `thm:bounded-ma-extension`, including full proof and Step 6 | Positive Radon measure, fixed mass, weighted bounded-net continuity, and weak convergence against arbitrary continuous tests. | Used in bounded energy and Chapter 30 weak pushforward. Primary Theorem 3.1 provides a separately inspected published-source interface. Full unrelated Chapter 24 claims are not thereby certified. |
| Same, `prop:ch24-continuous-uniform` | Uniformly convergent continuous psh inputs give weakly convergent MA measures. | Its model estimate/bounded-operator proof precedes the repaired strict-maximum/comparison arguments, avoiding that circularity. |
| Weighted parent `p081_weighted_energy_consumers_repair_20260831/patched/ch26_energy.tex` | Standing semipositive omega; model energy cocycle, translation, Taylor and first/second variation identities; concavity and sandwich discussion. | Supplies the finite-polynomial identities and ensures zero is psh. The unconditional sandwich follows from the model concavity argument, so no ordering of approximants is required. |
| `manuscript/parts/part3/ch30_functoriality.tex` | Model divisor pullback, curvature pullback, nef pullback, and finite-degree model projection formula. | Only these items are used. The same chapter's incorrect actual-real-model maximum clause and final finite-minima descent paragraph are excluded, not silently assumed. |
| `manuscript/parts/part1/ch05_skeleta.tex` and `ch06_metrics.tex` | Normalized vertical-divisor vertex values, affine restriction on faces, common SNC determination, component measure formula. | Supports the exact strict-vertex and support arguments. Special-fiber multiplicity b_E is retained. |

The downstream proofs' topological passages were checked directly: compact cofinal tails, compact finite-intersection arguments, extension by zero of compactly supported continuous tests on an open subspace, Radon uniqueness, weak pushforward by continuous maps, and continuity from below for a fixed finite measure. They need no metrizability or sequence-only substitute for a net.

## C. Declared upstream Chapter 20/21 dependency

The Chapter 24 packet freezes these original upstream artifacts:

| Artifact in `p081_ch20_ch21_real_model_max_repair_20260831` | SHA-256 |
| --- | --- |
| `rational_approximation.tex` | `f857bbc52b34d75e9dcd3047fa0b55c79a052d7377732ce61f8d7038984b1572` |
| `patched/ch20_model_forms.tex` | `7b287229f071aceeaa8396a8ea00bd6f6d70a566f67bdd452fc72bd2281fb586` |
| `patched/ch21_bfj_psh.tex` | `957e2a2d16ff85c036aa42c1647aa055f56767fb9973a02b34d4853899d39310` |

The usable interfaces are rational model-maximum closure for fixed real theta; fixed-theta rational approximation of real theta-psh model functions when the generic class is ample; and uniform psh stability. The real density theorem is not invoked outside its ample-generic scope. In particular, real model functions are not claimed to form a lattice.

The reviewer contributed to this diagnostic/repair route and previously reviewed its original and revised1 assemblies. That is disclosed, not counted as an independent new proof here. The source hashes above identify the exact upstream bytes frozen by the current Chapter 24 author packet; later editorial revisions are not silently substituted. A separate genuinely independent review and the production gate remain the appropriate acceptance mechanisms.

## D. Mechanical checks and exact-byte boundary

`check_packets.mjs` is an independently authored read-only verifier. It checks the two expected manifest hashes, all 33 manifest entries, all 17 source entries, exact unique replacement assembly, unchanged statements and ordered labels, absence of duplicate labels/control bytes, the preserved weighted graph fragment, matching incremental/combined patches, and read-only patch applicability. It never applies a patch or writes a candidate file.

Bounded-net packet: 16 manifest records, nine source records, two replacement spans, 250 Chapter 26 labels and 224 Chapter 30 labels. Locality packet: 17 manifest records, eight source records, five replacement spans and 179 Chapter 24 labels. All checks passed. Author validators were additionally read and run without mutation.

The source review used the PDF skill for primary-theorem inspection. No candidate PDF was produced in this audit. Author draft-mode compilation records are frozen mechanical evidence only, not independently claimed visual acceptance. All new audit files are isolated in this sibling directory. No live manuscript, frozen candidate, production state, or inventory status was changed.
