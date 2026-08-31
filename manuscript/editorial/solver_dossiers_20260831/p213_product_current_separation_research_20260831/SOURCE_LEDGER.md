# Exact sources and dependency boundary

Date: 31 August 2026. Packet author: `/root/p082_independent_reaudit`.

## Primary source version and direct reading

Antoine Chambert-Loir and Antoine Ducros, *Formes differentielles reelles et courants sur les espaces de Berkovich*, arXiv:1204.6277v2, revised 25 July 2025, 608 pages. The primary arXiv record was checked in this task: <https://arxiv.org/abs/1204.6277v2>.

- PDF: `/private/tmp/CLD25.pdf`, SHA-256 `5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719`.
- Extracted text: `/private/tmp/CLD25.txt`, SHA-256 `021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e`.

The exact source passages, and their limits, are as follows.

| Passage | Use and limitation |
| --- | --- |
| Section 7.1.11, p.159 | Properness/compact support is required for pushing a current to a target. The new note checks compact inverse images explicitly; it does not use a nonproper pushforward. |
| Sections 7.2.6, 7.2.8-7.2.9, pp.161-162 | Positive scalar distributions have order-zero/Radon control in the stated locally separated setting. The new proof also gives the cutoff bound and Euclidean constant-distribution argument directly. |
| Corollary 7.2.10 and Section 7.3.1, pp.163-164 | Nonnegative smooth functions times the canonical integration current are positive currents. Section 5's examples are such currents and are explicitly shown not to be closed. |
| Remark 14.4.3, p.410 | An F-analytic space viewed over a finite base subfield k has canonical calibration multiplied by [F:k]. The statement permits ramified finite extensions. It does not assert ordinary-open covering sheets. |
| Proposition 15.1.1(b), p.421, with proof p.422 | Ordinary smooth forms have local moment descriptions on ordinary open sets. Part (a)'s G-covering formulation is not substituted for part (b). |
| Section 15.2.2, p.423 | A good, topologically separated analytic space is locally holomorphically separated, the relevant hypothesis for smooth source cutoffs. |
| Corollaries 15.2.5 and 15.2.9; Proposition 15.2.8, p.424 | Compactly supported ordinary source cutoffs and partitions of unity. Corollary 15.2.9 is applied only to the compact support of one test form. Its printed free letter K in the cover clause is understood via the F of its statement and underlying Corollary 6.2.8. |
| Corollary 6.2.8, p.143, complete proof | Source form of the compact-support partition statement; read to check the previous locator and its hypotheses. |

The complete rendered pages 410, 421, and 424 were inspected visually in this task at 1500-pixel page resolution. These show the finite-degree formula, the ordinary-open clause, and the exact cutoff/partition statements without extraction ambiguity. Complete source text of the adjacent proof page 422 and the relevant pp.159, 161-164, 423 was read; the prior residual-functional audit had also visually inspected pp.159, 161-162, and 409-410. Scratch renders are in `/private/tmp/p213_product_separation_source_qa.4ASAtm/`; they are not authored deliverables. The source PDF was neither edited nor re-exported.

The PDF skill influenced the source-verification step only: full relevant page images were checked instead of relying solely on text extraction. No PDF artifact was authored.

## Henselian coefficient field and elementary new algebra

The Stacks Project, Lemma 10.153.7 (tag 04GK), primary page <https://stacks.math.columbia.edu/tag/04GK>, complete statement and proof read directly in this task. Finite etale algebras over a henselian local ring correspond to finite etale residue algebras. This supplies R_p for the finite separable residue extension kappa(p)/k. The stronger completed-ring/tube statement is an explicit argument in the frozen product proof, not an unsupported consequence of this lemma alone.

The new power series P(T)^N=1+T is proved coefficient by coefficient in the note, using only that N is a unit of R. This avoids invoking the characteristic-zero binomial formula in positive or mixed characteristic. Eisenstein irreducibility gives [K_p(pi^(1/N)):K_p]=N. The analytic isomorphism is written in both directions and checked on closed subannuli. No source theorem asserting N ordinary sheets is used or needed.

The cutoff identity B_T(p,N)=N b_T(p), the mixed-coordinate obstruction, and the conditional source-cell reduction are new arguments authored in this research note. They are not attributed as printed theorems of CLD or Stacks. No novelty or production-acceptance claim is made.

## Exact frozen local inputs

All local paths below are relative to `/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260831/` unless absolute.

| Input | SHA-256 | Role |
| --- | --- | --- |
| `p213_residual_curve_functional_interface_research_20260831/statement.tex` | `5ad73a96dd4e41296003e2824711cf7d6301aa489fdc67ed11a2158682d135fc` | Product geometry; definitions of b_T(p); prior principal relation. |
| `p213_residual_curve_functional_interface_research_20260831/proof.tex` | `209ce1db0b33f460952e7c423c09baa58ab2f6cdc14a3d55b9310ddcbde9b224` | Completed-ring/tube construction, scalar collar distributions, prior divisor-functional proof. |
| `p213_residual_curve_functional_interface_research_20260831/MANIFEST.json` | `175b64dfd4e08ad59dcb561928ab50172194e04af264c4641b49c8dcc0359278` | Frozen parent packet identity, not a production receipt. |
| `p213_residual_curve_functional_interface_independent_audit_20260831/INDEPENDENT_EXACT_BYTE_AUDIT.md` | `177d0ca3454b6f73caedf81fe4eaa34f674a712460ace16409b36115892f2359` | This author's earlier bounded independent audit; provenance disclosed. |
| `p213_skeletal_packets_20260831/skeletal_representation/statement.tex` | `5c06cd6f091e5964a16c07b3efddd2104fed938447605f4f9b19ff8dfea01f1a` | The explicit conditional premise (R), including arbitrary source multipliers and no lower-cell residual. |
| `p213_skeletal_packets_20260831/skeletal_representation/proof.tex` | `27a344a15fa7d22b2e88c07837aacfca0c978758c5bae5871c5af2d30e47999a` | Read completely to identify the proposed interface, not independently accepted in this task. |

The new note never invokes (R) to construct B_T(p,N), prove closedness identity (9), or compute canonical degree. It invokes (R) only when interpreting the scalar coefficient as an individual source-cell coefficient and when proving the conditional separation reduction (14).

There is no import of GRW's algebraically closed field scope, no current pullback through a finite field extension, no assumed slicing theorem, no universal Radon domination, no broad polycylinder-basis statement, and no full-product/P21.3 conclusion.

## Freeze checks

The principal frozen source hashes above were checked before authoring and are included in SHA256SUMS for an exact end check. The authored files are UTF-8 Markdown; a byte scan checks that they contain no C0 control bytes except tab, LF, or CR. No compile result or source-generated PDF is claimed for this packet. A successful checksum verification is only a preservation check, not a mathematical acceptance claim.
