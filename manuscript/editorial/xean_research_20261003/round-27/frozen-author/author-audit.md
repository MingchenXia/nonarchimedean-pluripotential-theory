# Author audit: P15.2 relative bounded fibration scope

This is an author self-audit, not an independent model verdict. The proof is in `P15.2-argument.md`; the standalone paper contains its entire theorem and proof. The supplied route is Xean native Codex `gpt-6.1-sol`/`xhigh`, as recorded in the copied operator settings. No additional model call is made. Configuration metadata is not itself a mathematical verification.

| Claim or suspected failure | Checked antecedents and resolution |
| --- | --- |
| Singular or dimension-jumping fibres might contribute an extra transverse term | The pushforward of closed positive `omega^m` has degree zero and is closed globally, hence is one positive constant distribution on connected B. This precludes a separate term on critical values. The constant is identified on any regular fibre only after the global proof. |
| Disconnected generic fibres might change calibration | Fibre integration sums all components. Connected fibres are not an assumption of the operator theorem. |
| Pullback/projection for arbitrary singular currents | Not asserted. On a base chart the local potential is bounded psh. Smooth decreasing approximants compose on the entire inverse image, including critical points. Properness allows pushforward of local convergence. The smooth formula passes to the bounded BT limit. |
| Multiplication of weakly convergent measures by discontinuous phi | Not performed. First prove equality of the pushforward top-degree Borel measures; then use the definition of measure pushforward with the bounded Borel weight phi. |
| Horizontal wedges of degree greater than nu | Smooth local approximants are pullbacks of base forms, so the wedges vanish before passing to the decreasing BT limit. No pointwise rank claim for nonsmooth currents is used. |
| Mixed mass after replacing potentials | Bounded BT recursion makes each dd^c difference dd^c(v S). Its compact integral is zero. All replacement backgrounds used are positive or semipositive. This yields every exact cohomological mixed mass used in the estimate. |
| Integration by parts for nonsmooth potentials | Smooth tests need only the recursion/distribution identity. Energy uses exactly BEGZ Theorem 1.14 with A empty, positive closed BT bidimension-(1,1) current, and globally bounded quasi-psh differences. No unbounded exceptional-set argument is required. |
| Loss of one epsilon power in the error | The explicit polynomial has theta times (theta+epsilon omega)^(n-1). Because theta^(nu+1)=0, its first possible exponent is n-1-(nu-1)=m. The scaled error is O(delta), requiring no epsilon-relative rate. |
| Arbitrary non-descending perturbative potentials | A and D need only be positive BT currents with bounded global potentials; no descent appears in the mixed difference estimate. |
| Critical values in lower-order remainders | Remainders are positive pushforward measures whose total masses are computed cohomologically. Smoothness of those pushforwards is unnecessary. |
| Energy differentiation for bounded potentials | Along affine bounded psh segments the functional is a finite polynomial by multilinearity. Differentiate the polynomial and use checked bounded integration by parts. General infinite-dimensional differentiable paths are not claimed. |
| Auxiliary class dependence | Each class has its own positive c_omega. The theorem's limits after this calibration equal the same base objects. It neither treats c_omega as class independent nor relies only on cohomologous representatives. |
| Moving auxiliary paths | Smooth convergence to a Kähler limit bounds all finite cohomological coefficients and keeps c away from zero. No derivatives in epsilon or rates are used. Degenerate limits are excluded. |
| Base-reference changes | Subtract h from phi and h composed with pi from u. The currents coincide exactly. The energy correction follows from the bounded relative cocycle. |
| Minimal singularity claim | A semipositive background admits potential 0. Compact quasi-psh functions are bounded above, so every bounded potential is minimal; minimality against 0 also bounds a minimal potential below. No richer unbounded P-type is retained. |
| Original target | A supplied fibration with alpha=pi^*[beta] is an extra hypothesis. No carrier construction for all pseudoeffective classes, minimum-reference theorem, unbounded extension, or original-carrier independence is proved. Original P15.2 remains open. |

The essential published BT, integration-by-parts, and nef-volume statements are written explicitly in the proof, with citations and applicability checks. BEGZ's omitted general multilinearity proof and the printed convergence wording of Lemma 1.5 are not imported. Primary text defects are retained verbatim in the Markdown appendix and source files.

Small finite arithmetic diagnostics check coefficients and exponents; two successful TeX passes check the document build. Neither establishes the analytic proof. The self-audit finds no unresolved indispensable step within the stated bounded supplied-fibration scope. This is an unverified author draft labelled partial, with candidate false.
