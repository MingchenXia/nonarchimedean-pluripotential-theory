# Source-aware review checklist

## Stage 1: source-supported narrowing/removal

- [ ] Confirm GJKM published Theorem 1.1, p. 2334: ample line bundle, smooth projective curve, continuous semipositive metric envelope; not generic-nef degree-zero model existence.
- [ ] Confirm GJKM §§2.2–2.8, pp. 2338–2340: Q-model functions, arbitrary real closed model forms, actual-competitor envelope. The live `def:ch23-model-envelope` and `eq:ch23-model-envelope` remain the original real-span definition; unadorned `P_theta` remains raw all-PSH supremum.
- [ ] Confirm GJKM Proposition 2.11, p. 2341: finite **normal** field extension, real theta, Q-model envelope. Neither arbitrary alterations nor raw all-PSH comparison is imported.
- [ ] Verify stage 1's temporary `thm:ch23-gjkm-curves` statement is precisely the positive polarized source theorem with the harmless extra geometric-connectedness hypothesis.
- [ ] Check modified summaries do not silently claim all singular-PSH regularization, orthogonality, or finite-energy measure theory from a metric-envelope theorem.
- [ ] Check Ch31 unsupported nonskeletal-measure solvability/continuity is removed, without replacing it by a new general existence assertion.
- [ ] Full-book compile the root-approved changes, especially the enlarged scope tables. This subagent only checked patch applicability and labels.

Exact old labels/loci handled by stage 1 (line numbers are the original frozen live snapshot):

| Chapter | Old labels and lines |
|---|---|
| Ch22 | Curve paragraph 3217–3225 following `prop:ch22-multiplier-interface` references; no theorem label removed |
| Ch23 | `def:ch23-model-envelope`, `eq:ch23-model-envelope` (232–257, definitions preserved); `thm:ch23-gjkm-curves` (3051–3073, safe source specialization); `sec:ch23-later-alterations` (3214–3218); `sec:ch23-atlas` curve row (3278–3282); provenance (3463–3467) |
| Ch27 | `rem:ch27-curve-base-change` (1920–1937); curve paragraph (3418–3434); scope table (3498–3502); dimension warning (3538–3544); provenance (4414–4416) |
| Ch28 | `sec:ch28-scope` table (275–276); “whole package” paragraph (2253–2256); chronology (3573–3578) |
| Ch29 | `sec:ch29-later-curves` table (2063); `thm:curves-arbitrary-field-continuity` statement (2072–2079); `rem:ch29-curve-source` (2209–2218); `rem:ch29-curve-nef-ample` (2227–2235); `sec:ch29-atlas` (2533–2537); E2 scope (3119–3121); provenance (3315–3323) |
| Ch31 | `sec:ch31-curve-setup` (239–260); orientation (174–178); `rem:ch31-curve-solution-scope` (509–512); hypothesis-removal table (3537–3540); provenance (3793–3796) |

## Stage 2: pending real-class envelope integration

- [ ] Root has accepted the strict production result for the exact revised1 statement/proof hashes, not merely the independent audit. At creation of this proposal, that production gate was pending.
- [ ] Verify the inserted Ch23 content differs from the frozen candidate only by the documented label mapping.
- [ ] Confirm all theta coefficients remain real. The numerical form `theta+dd^c phi` is real even though every competitor phi is rational-model. No arbitrary real normalization is called Q-model.
- [ ] Check the positive-margin rational-bend proof, common semistable domination, actual-competitor retraction, and finite-definition/real-nef-reflection/finite-normal descent source interfaces against the independent audit.
- [ ] Degree zero has the actual-competitor hypothesis and exact `psi+min(f-psi)` formula; the empty case remains minus infinity.
- [ ] Ch29's metric theorem is a specialization to an ample line bundle; the stronger real-class statement lives in Ch23. Neither theorem is silently identified with raw all-PSH or the finite real model span.
- [ ] Preserve the four old Ch29 equation labels: `eq:curve-envelope-contraction`, `eq:curve-envelope-retraction`, `eq:curve-slope-criterion`, `eq:curve-chord-supremum`. The proposed patch retains them and explicitly locates the unweighted graph calculation over the completed algebraic closure.
- [ ] Retarget consumers of `prop:ch27-curve-orthogonality`, `cor:ch27-curve-orthogonality-global`, and `rem:ch23-model-dependence` only after checking their separate real-model/raw-envelope comparison. This patch does not prove that comparison merely by changing the curve theorem.
- [ ] Verify GJKM19, GM19, and BL85 bibliography keys exist. They were found in the current `NonArchimedean.bib`; no bibliography mutation is proposed.

## Stage 3: exact obstruction before arbitrary-field application

The proposed solution proof has the correct intended dependency order:
finite real graph Green construction -> continuous local psh metric with prescribed positive skeletal curvature -> **positive-degree** `thm:p081-corrected-curve-comparison` -> uniform Q-nef approximation. It does not use the envelope theorem to prove itself, does not infer rational slopes from rational masses, and does not call the nonatomic integrated potential lisse.

However, the present draft must not be applied as an arbitrary-field proof until these points are closed:

- [ ] **Residue-degree weights.** GJKM Proposition 3.7, pp. 2344–2345, includes weights `w_x(nu)=[k(p_nu):k]`. Ch31's setup currently writes an unweighted outgoing-slope sum and unweighted graph energy while its standing hypotheses do not require an algebraically closed residue field. The draft's unweighted Green kernel directly proves the weight-one/split graph calculation, not by itself the nonsplit arbitrary-field assertion. Either audit a complete weighted Green construction and update all affected graph identities, or make a separately approved exact split-model scope explicit. Do not quietly erase the field generality or treat the weights as one.
- [ ] **Common reference model.** In Ch29 the given measure is supported on a specified strict semistable skeleton. The proof must justify putting a reference model metric of L and the support on a common suitable skeleton over the stated field, or carry out finite-extension/measure descent with its exact conventions. The envelope proof's completed-algebraic-closure descent does not automatically descend prescribed measures.
- [ ] **Local lisse approximation.** The finite atomic approximation can have real masses and real slopes. Verify the local curve slope/Thuillier–CLD psh interface at the chosen type-II breakpoints. Do not replace this by the invalid assertion that a global real graph function necessarily lies in the real span of Q-model functions.
- [ ] **Positive Ch17 gate.** Use only the accepted positive-degree clause of `thm:p081-corrected-curve-comparison`, for the actual line bundle L and a continuous metric already shown locally psh. The degree-zero clause or generic nefness cannot fill a missing positivity or model-existence step.
- [ ] **Curvature continuity/source comparison.** In Ch31's original BFJ regime, `thm:ch21-continuous-zhang` and `prop:ch24-continuous-uniform` identify the resulting metric/potential and measure. Outside that regime, check the curve-specific formal/Thuillier/CLD comparison rather than transporting every BFJ definition automatically.

Exact proof consumers are `prop:graph-ma-solution` in Ch31 (old proof 453–498), and the MA half of `thm:curves-arbitrary-field-continuity` in Ch29 (old lines 2162–2201). The existing Ch31 graph-kernel lemma and numerical constants have not been completely re-audited by this consumer-patch task.

## Remaining scope that must not disappear

- The arbitrary-dimensional envelope problem over a general complete nontrivially valued field is not solved by any patch here.
- There is no claim that every positive measure on a curve has a continuous potential; skeletal support remains.
- There is no automatic transfer of arbitrary-field singular-PSH regularization, full finite-energy measure theory, or orthogonality.
- The finite real span of Q-model functions is not assumed closed under finite maxima, and its envelope is not declared equal to the Q-model envelope at degree zero.
- Source/scope removals may be integrated before stage 2, but they do not certify the remaining old detailed proof paragraphs. The root's release/build record should keep that incompleteness visible.
