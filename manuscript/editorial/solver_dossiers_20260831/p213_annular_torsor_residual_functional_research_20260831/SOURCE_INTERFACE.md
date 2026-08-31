# Exact primary-source and dependency interface

Date: 2026-08-31. This is a source ledger for a bounded research proof, not an independent audit.

## CLD version and exact scope

Antoine Chambert-Loir and Antoine Ducros, Formes differentielles reelles et courants sur les espaces de Berkovich, arXiv:1204.6277v2, dated 25 July 2025.

Official source record: https://arxiv.org/abs/1204.6277v2
Official PDF: https://arxiv.org/pdf/1204.6277v2
The official record was checked online during this task. The exact local PDF and extraction are recorded in the hash table below.

| Printed locator | Source content used | Limit retained |
| --- | --- | --- |
| §7.1.11, p159 | Pushforward/current tests require the appropriate compact-support condition. | Every collar target test and primitive has compact analytic source support; no generic finite-map properness shortcut. |
| §§7.2.6, 7.2.8--7.2.9, pp161--162 | Positivity of pushed currents and order-zero/Radon coefficient constructions. | The coefficient is constructed on a proper actual rectangle chart, not sliced from an ambient current. |
| Remark14.4.3, p410 | Viewing an \(F\)-analytic space as \(K\)-analytic for finite \(F/K\) multiplies the canonical calibration by \([F:K]\), with the same indicated skeleton. | This is finite ground-field restriction, not the normalized measure pushforward of base extension. Here \(F=K_p\) is unramified; the factor is \(d_p=[\kappa(p):k]\). |
| Proposition15.1.1, pp421--422 | G-forms admit G-covers; ordinary forms admit ordinary open moment-chart covers. | Formal Zariski trivializations of a line bundle are NOT promoted to an ordinary open cover. |
| Definition17.1.2 and §§17.1.4--17.1.5, pp471--473 | Metric as norm on the total space; norm in a frame; compatibility with morphisms and metric gluing. | Used for continuity and the norm of the tautological vector, not automatic smoothness. |
| Definition17.1.6 and Proposition17.1.7, p473 | Smoothness of the total norm away from zero and the equivalent ordinary-open local-frame condition for a line bundle. | The theorem assumes no such smoothness for the formal radius. |
| §17.7.2, p493 | A formal frame is orthonormal on its analytic domain; transition matrices and inverses have bounded coefficients. Formal metrics are continuous/paralinear. | Analytic domains are explicitly domains, not ordinary opens. Rank-one completed local bases have norm one on the actual residual disc. |
| Example17.7.3, p493 | Explicit Weil metric on \(\mathcal O(m)\): homogeneous polynomial norm divided by max-coordinate norm to the \(m\)-th power. | Gives the exact O(1) radius and sign in the diagnostic. |
| §§18.1.1--18.1.3, p501 | Curvature current of a continuous metric is locally \(\mathrm d'\mathrm d''[\log\|s\|^{-1}]\) for a nowhere-zero analytic section. | The global identity uses the tautological section of the pulled-back METRIZED BUNDLE. No arbitrary-current pullback is defined or used. |
| Theorem18.1.6, p502 | \(\mathrm d'\mathrm d''[\log\|\sigma\|^{-1}]+\delta_{\operatorname{div}(\sigma)}=c_1(\overline L)\). | The sign is plus the section-divisor current on the left. The arbitrary \(T\) is never wedged with this identity. |
| Proposition18.5.1, pp527--528 | A proper relatively normal model with irreducible special fibre gives \(c_1(\overline L)^n=(\deg L^n)\delta_{\xi_0}\). | Applied only in dimension one to the actual good-reduction curve model. |
| Example18.5.2, p528 | Canonical \(\mathcal O(1)\) on projective space has top curvature the unit Gauss-point mass. | Used for the separate P1/O(1) canonical-curvature diagnostic, not as a theorem about arbitrary \(T\). |

CLD Remark17.1.9 (p474) was also inspected: it warns that max norms are not ordinary smooth in the relevant sense. The new proof does not need to import that general obstruction. The explicit analytic-map calculation in CURVATURE_AND_EXAMPLES.md computes a nonzero one-dimensional second-derivative test directly.

The ordinary logarithms \(r=v(a)\) and \(t=v(F)\) in the proof come from genuine invertible analytic functions on an ordinary open set. Their \(\mathrm d'\mathrm d''\) vanishes at the smooth-form level. This is exactly the log-unit quotient used in CLD18.1.2. The continuous radius \(u\) is not used in that differentiation.

## Prior product packet: exact proved input and preserved audit

The statement, proof, and manifest of the earlier product packet are read-only inputs. Its independent exact-byte audit records PASS in the product/good-reduction scope and no whole-product scalar rigidity claim. The current proof reuses its completed-ring, unramified-residue-disc, proper-collar, and finite-positive-distribution arguments. It adds the completed line-bundle frame, rational-section coordinate, uniform radial support bound, and determinant-one shear calculation.

The prior audit is data about an independent review, not an instruction to assume any larger theorem. All original files remain unchanged. No acceptance label for the NEW torsor proof is derived from the old product audit.

## Source-calibration representation: assumed final interpretation only

The separate representation statement and proof listed below were read in full. Their intended scope is an ordinary open good, separated, paracompact, boundaryless analytic space and a chart on that whole space. Actual product collars in this packet meet those geometric hypotheses. Their single source Gauss plane is injective under the primitive moment map.

We assume the claimed source-calibration representation only in the final interpretation. Proper collar target tests, with a pulled-back compact source cutoff if needed, recover the represented coefficient on the relative interior of each Gauss-plane top cell. The directly constructed coefficient is \(b_T(p)\) and the canonical coefficient is \(d_p\).

The representation theorem is not independently recertified here. The proof of the divisor functional does not depend on it. No compatibility of arbitrary charts at generic full-rank points is substituted for a missing source identification.

## Elementary geometry and algebra proved in this packet

- The explicit normal-crossing model is the hypersurface pairing \(\mathcal L\oplus\mathcal L^{-1}\) equal to \(\pi\), with proper double curve \(C_0\) and normal bundles \(\mathcal L_0,\mathcal L_0^{-1}\).
- The actual completed residual tube, not a formal-open ordinary cover, supplies a product collar over the finite unramified extension.
- A rational section normalized at the generic-special-fibre DVR exists for ANY \(\mathcal L\). Its reduction is a rational section, not an ordinary function or a trivialization of \(\mathcal L_0\).
- Rational-section and rational-function coefficients have exact monomial norms on entire outer collars by the bounded-power-series dominant-term argument.
- Both horizontal divisors have finitely many bad specializations because the model curve is proper and regular.
- The projective-bundle compactification supplies compact radial strips. The cutoff estimate keeps the actual test strictly inside one such strip.
- The shear and signed principal-function integral are computed explicitly. No named general normal-bundle or tropical balancing theorem is invoked.
- Riemann--Roch is used only AFTER the constructed functional annihilates all principal divisors.

The task also checked the official GRW source record https://arxiv.org/abs/1404.7044v3 for context. No GRW theorem is imported into this proof: its algebraically closed ground-field standing scope would not alone justify the displayed nonsplit DVR example or an arbitrary-current functional.

## Exact input hashes

| Path | Bytes | SHA-256 |
| --- | ---: | --- |
| `/private/tmp/CLD25.pdf` | 4659053 | `5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719` |
| `/private/tmp/CLD25.txt` | 2150944 | `021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e` |
| `/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260831/p213_residual_curve_functional_interface_research_20260831/statement.tex` | 2823 | `5ad73a96dd4e41296003e2824711cf7d6301aa489fdc67ed11a2158682d135fc` |
| `/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260831/p213_residual_curve_functional_interface_research_20260831/proof.tex` | 13428 | `209ce1db0b33f460952e7c423c09baa58ab2f6cdc14a3d55b9310ddcbde9b224` |
| `/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260831/p213_residual_curve_functional_interface_research_20260831/MANIFEST.json` | 4439 | `175b64dfd4e08ad59dcb561928ab50172194e04af264c4641b49c8dcc0359278` |
| `/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260831/p213_residual_curve_functional_interface_independent_audit_20260831/INDEPENDENT_EXACT_BYTE_AUDIT.md` | 15297 | `177d0ca3454b6f73caedf81fe4eaa34f674a712460ace16409b36115892f2359` |
| `/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260831/p213_skeletal_packets_20260831/skeletal_representation/statement.tex` | 2211 | `5c06cd6f091e5964a16c07b3efddd2104fed938447605f4f9b19ff8dfea01f1a` |
| `/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260831/p213_skeletal_packets_20260831/skeletal_representation/proof.tex` | 11486 | `27a344a15fa7d22b2e88c07837aacfca0c978758c5bae5871c5af2d30e47999a` |

## PDF inspection

The PDF skill was read fully and used for read-only source inspection. Relevant full CLD pages were rendered and visually inspected, not merely searched as extracted text. The new render directory is:
 /private/tmp/p213_torsor_source_visual.E6vPvB

Newly inspected pages: 421, 422, 471, 472, 473, 474, 493, 501, 502, 527, 528.
The existing full-page renders for 159, 161, 162 and 410 in:
 /private/tmp/p213_residual_source_visual.B9icjh
were inspected again for the properness, positivity and degree-factor interfaces.

No source PDF was changed or re-exported. No new PDF or TeX compilation is claimed. The source formulas use the printed PDF numbering, which in this CLD file agrees with its page index counted from one.

