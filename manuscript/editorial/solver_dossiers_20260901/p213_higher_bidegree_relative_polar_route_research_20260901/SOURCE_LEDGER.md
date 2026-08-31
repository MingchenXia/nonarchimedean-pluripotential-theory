# Source ledger and proof boundaries

Date: 1 September 2026. Candidate-only; not production verified.

## Exact primary source

Antoine Chambert-Loir and Antoine Ducros, *Formes différentielles réelles et courants sur les espaces de Berkovich*, arXiv:1204.6277v2, revised 25 July 2025, 608 pages.
Primary version page checked this turn: https://arxiv.org/abs/1204.6277v2 .
The local source text was read directly; no source theorem is inferred from a search snippet.

- PDF: /private/tmp/CLD25.pdf, SHA256 5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719.
- Text: /private/tmp/CLD25.txt, SHA256 021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e.

Only these primary bytes supply the analytic-calculus theorems in the note. The sibling research packets are provenance/context, not independent acceptance of the new relative estimate.

| Primary location | Exact use | Retained boundary |
|---|---|---|
| CLD 1.2.13; 6.5.2; proof of 7.2.9 | Positive smooth majorants on finite ordinary presentations; bounded coefficients are dominated by a power of the ordinary quadratic Hessian. | Does not assert a globally fixed trace measure, a full-rank chart at every point, or a current pullback. |
| CLD 7.2.9, printed p.162 | A symmetric positive linear functional on ordinary compact tests is a continuous order-zero current. | Used to prove continuity of the convergent fiber series; not merely presumed from pointwise limits of arbitrary distributions. The functional here is positive, stronger than the source's weak positivity requirement. |
| CLD 7.2.11--7.2.12, p.163; 7.2.7 | Coefficient Radon measures, continuous scalar multiplication, and wedge with smooth positive forms. | No scalar measure is substituted for a bidegree-(p,p) current without wedging an appropriate test form. |
| CLD 7.3.10; 8.3.1(b), pp.168,201 | A smooth function whose associated Hessian current is zero has zero smooth Hessian. | Smooth functions only; not a regularity theorem for all continuous distributionally harmonic functions. |
| CLD 7.7 and 8.5.3--8.5.4 | Differentiation by transposition; closed-current smooth product rule; compact integration by parts. | Actual test degrees are checked in the note rather than copying the inconsistent bidegree/range wording of 8.5.3. No unqualified zero-extension commutation from 7.1.12. |
| CLD 8.1.7--8.1.8, pp.196--197 | Full continuous CPsh minimal-subsheaf uniform closure and separate-variable closure arguments. | Never replaced by a single stage-one approximation sequence. |
| CLD 8.5.1, pp.205--206 | Positive weakly converging currents can be multiplied by locally uniformly converging continuous functions. | For signed energy expressions, the proof first splits them into finitely many positive converging currents with bounded masses. |
| CLD 8.5.5, p.207 | dd(uS) is positive closed for full-CPsh u and positive closed S. | No Bedford--Taylor independence assumption on S; this is the crucial valid starting point. |
| CLD 8.4.2--8.4.3, pp.203--205 | Motivation for the compact barrier and exponential energy cancellation. | The new estimate is proved directly for an arbitrary bidimension-(1,1) base Q and full CPsh. It is NOT the printed theorem: V must be smooth near a larger common compact, and the scalar derivative factor is one, not two. The safe integer a>=4 permits C^2 coefficient approximation. |
| CLD 8.6.1--8.6.2, pp.207--208 | Identifies the actual source open question. | This note restricts to the continuous-pair predicate; no claim about every discontinuous psh function. |
| CLD 8.6.3--8.6.6, p.208; 8.6.8, pp.208--209 | Locality, canonical-current case, smooth closed wedge, positive weak limits, and CPsh curvature closure. | These statements are re-proved in the continuous scope used. Corollary 8.6.7 is excluded because arbitrary continuous multiplication does not preserve closedness. |
| CLD 8.8.1 and 8.8.4--8.8.5, pp.211--212 | Local dpsh decompositions and the distinction between potential-based products and independence from their Hessian currents. | Squares/products and energy positivity are proved from minimal CPsh closure; no circular use of independence for an arbitrary base current. |
| CLD 15.2.1(b), p.423 | Top-degree form SUPPORT on a pure analytic space avoids a closed analytic subset of smaller analytic dimension. | Used intrinsically on each flag member for its own top degree, and on X for dd(beta) of degree (2,2). Not a blanket statement for lower-degree test forms. |
| CLD 15.2.4--15.2.5, pp.423--424 | Ordinary differential separation and compact smooth source cutoffs. | Source supports remain in ordinary opens; G-opens are not silently substituted. |
| CLD 16.6.3, p.459 | Integration on a pure closed subspace retains its actual generic multiplicities. | Flag currents are not silently reduced with multiplicity one. |
| CLD 16.7.3--16.7.4, p.460 | Poincare--Lelong for regular meromorphic functions, and zero Hessian for the logarithm of an analytic unit. | Regularity is explicit. No derivative commutation across zero sets is borrowed from 7.1.12; the truncations converge before differentiation. |
| CLD 16.9.1--16.9.4, pp.467ff. | Context for analytic compact-sublevel barriers and logarithmic poles. | The note supplies its barrier and truncation construction. The source's canonical first-stage polar result is NOT applied to arbitrary T or to the full CPsh hierarchy. |

## Existing diagnostics actually read

All paths below are under the durable manuscript/editorial/solver_dossiers_20260901 unless stated otherwise. Their hashes are in INPUT_PINS.json.

- chapter72_propagation_preservation_20260901/CHECKPOINT.md: completed conditional four-family work is not full current compatibility or higher-bidegree rigidity.
- p213_common_constant_propagation_diagnostic_20260901/DIAGNOSTIC.md: a fixed moment can have disconnected maximal-rank source families, while new connecting cells of a concatenation project with rank drop.
- p213_two_cluster_positive_transport_research_v2_20260901/RESEARCH_NOTE.md: actual-source compact tests compare four specified coordinate families, under L/O/Q and displayed R. This scope is retained and not reused as an all-current theorem.
- p213_common_constant_cohomology_source_diagnosis_20260901/SOURCE_DIAGNOSIS.md and SOURCE_LEDGER.md: ordinary versus weak forms, missing closed-extension issue, two-sided CPsh criterion, and source cautions.
- p213_cpsh_weighted_polar_research_20260901/RESEARCH_NOTE.md: its energy construction for arbitrary S suggested the present relative-base adaptation. This investigator did not author that predecessor; its proof mechanism is acknowledged, not presented as fresh independent validation or as a primary published theorem.
- p213_component_curvature_production_packet_20260901/STATEMENT.md: component curvature is not arbitrary higher-bidegree T.
- Durable Chapter 69, prop:verified-cross-fan: the elementary slope model reused in the sharpened energy/trace diagnostic. The higher-bidegree product and domination consequences are computed explicitly here.

The current Chapter 72 problem was read in the durable file parts/part6/ch72_major_open_problems.tex. This changing file is context, not a frozen theorem dependency; the exact displayed target is reproduced in the note. Its hash at reading is recorded separately from frozen input identities.

## Source exclusions

- No all-moment scalar representation R, residual-curve L/O/Q theorem, or scalar classification is an input.
- No weakly-smooth current extension is used; ordinary closedness on additional weak primitives is not assumed.
- CLD 8.11.3 is not used to declare harmonic-tropical convex functions T-psh for an arbitrary T. Its preceding proof interface requires Bedford--Taylor compatibility.
- Mere membership in a larger harmonic sheaf does not supply the full ordinary-CPsh pair required by (1.1). Conversely, a continuous difference of two CPsh functions is not automatically itself CPsh.
- No positive-current restriction or slice on an analytic subspace is postulated. Only functions and smooth forms are restricted; currents are pushed forward by proper closed immersions.
- No common tropical target, coarse pushforward, or density of a selected source family proves an upstairs equality.
- No regularization/density theorem for every positive closed current is invoked.
- The exact original-field fiber example is not a Bedford--Taylor counterexample.

