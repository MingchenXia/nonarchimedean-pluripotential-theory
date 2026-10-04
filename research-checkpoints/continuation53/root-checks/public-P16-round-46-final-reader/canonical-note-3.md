ID: n3

SUMMARY:
Delivered the complete partial argument, standalone 12-page paper, preserved inputs, source provenance and actual two-pass build diagnostics. Exact finite-tree checks passed. Six concrete obligations remain for general P16.4; execution and hashes are not mathematical certification.

DETAILED SUMMARY:
The implementation assignment is delivered with status=partial and candidate=false. Preserved byte-identical input-original.json, assignment-original.txt and task-original.json. Both final pdfLaTeX runs returned zero; the second had no warning, error or overfull box. Rational checks covered one five-node branched tree and five ray truncations, not all analytic cases. Remaining obligations concern actual unbounded mixed operators, potential compactness, envelope/obstacle replacements, unbounded differentiation, comparison/injectivity, and any ground-field descent.

SUPPORT:
["n1", "n2"]

TEXT:
The deliverable is partial. The original P16.4 has not been proved; candidate=false.

For the original axis, the intended retained geometric setting is a smooth geometrically connected projective algebraic n-fold, an ample line bundle L, and the other endpoint characteristic hypotheses, including residue characteristic zero in the nontrivial BFJ sector. The field should be complete real-valued non-Archimedean without a discreteness restriction; measures should have unrestricted support. The raw mass is V=(L^n)>0. For a continuous semipositive reference h₀, continuous raw energy is E(u)=(1/(n+1))∑_{j=0}^n ∫u c₁(L,h₀+u)^j∧c₁(L,h₀)^{n−j}; the intended measure condition is μ≥0, μ(X^an)=V and sup_{v continuous psh}(E(v)−∫v dμ)<∞. A definition of its extended energy space and a completion of test measures do not establish the equation.

Six concrete gaps remain in this submission:
1. Identify actual unbounded psh potentials and prove approximation-independent, positive, full-raw-mass genuine mixed Monge–Ampère measures for their finite-energy class in the general nondiscrete field setting.
2. Supply normalized potential compactness and extraction of actual finite-energy maximizing metrics, beyond compactness/completeness of measures.
3. Supply envelope/obstacle regularity or a proved alternative and connect available synthetic orthogonality to actual unbounded potentials and their operator.
4. Prove integrability, approximation and energy differentiation for that actual operator, including obstacle variations against all continuous tests if using a variational proof.
5. Prove finite-energy comparison/domination or equivalent injectivity estimates sufficient for uniqueness modulo constants.
6. Prove every proposed field-extension/descent assertion preserving the ample datum, raw mass, psh metrics, finite energy, derivatives and comparison. No such descent from n2 is asserted.

These are gaps of this deliverable, not a theorem of impossibility or a comprehensive literature claim. The explicit one-dimensional inversion in n2 cannot be promoted to arbitrary smooth projective varieties by formal completion or normalization.

Retained artifacts: `input.json` and byte-identical `input-original.json`; `assignment-original.txt`; `task-original.json`; `P16.4-argument.md`; standalone `P16.4-paper.tex`; `P16.4-paper.pdf`; `source-extracts/source-provenance.json` and 21 literal extracts with selected original-PDF page renders; `status.json`; `environment.json`; `checks.json`; `artifact-manifest.json`; and actual commands, stdout, stderr and separate first/second TeX logs in `build/`. The status file has exactly id,status,exact_result,proof_file,concrete_gaps.

Rerun from the supplied workspace:
`python3 audit_sources.py`
`python3 finite_tree_checks.py`
`python3 build_deliverable.py`
The final command also reruns the lightweight checks, regenerates standalone TeX with the existing pandoc, and invokes the existing pdfLaTeX twice with shell escape disabled. Original PDF rendering commands are retained in `source-extracts/render-commands.json`.

Observed checks: all supplied source hashes matched; the original input bytes were identical; task and assignment contents were preserved. The exact-arithmetic program passed nine check groups on one five-node branched rational tree with d=2 and ray truncations N=1,2,3,10,100. It independently compared the kernel matrix with a weighted graph Laplacian and returned I(μ)=616699/198450, E(u)=−616699/396900, projection energy 571619/198450, directional derivative 948301/793800 and comparison cutoff integral −6313/302400. These are specified finite observations, not exhaustive verification over trees or analytic fields.

Both final pdfLaTeX builds returned zero and produced a 12-page PDF. The second log had no LaTeX warning, error or overfull box. The engine was pdfTeX 3.141592653-2.6-1.40.26, TeX Live 2025/dev/Debian; Python was 3.12.14. No installation, network retrieval, external model, worker, subagent or resource-heavy computation was used. Successful execution, hashes and PDF compilation do not establish mathematical correctness. The mathematical result remains an unverified partial-proof draft.

Artifacts: /workspace/research/campaigns/round-46/P16.4-public-source-arbitrary-field-finite-energy-equations/artifacts/codex-cC7tVd
