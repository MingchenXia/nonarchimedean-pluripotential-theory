# Exact-byte downstream review: Chapter 24 real-input locality

Date: 2026-08-31. Reviewer: `/root/p082_independent_reaudit`.

## Verdict, independence, and gate

**PASS for the new real-input maximum/locality/comparison replacement proofs, conditional on their declared upstream inputs.** No substantive unresolved mathematical gap was found. In particular, the proof never requires the actual maximum of two real model functions to remain a real model function. The real theta and real model-input statements are preserved.

The author packet is `../p081_ch24_real_maximum_locality_repair_20260831`. This is a scoped mathematical and assembly review, not acceptance of the entire Chapter 24, a production receipt, an integration authorization, or a claim of new priority. The author packet's closed gate remains unchanged. Distinct Chapter 21 general-SNC/retraction issues and final Chapter 30 descent issues are outside this review.

The reviewer did not author these p081 replacement proofs and read their exact text and relevant source arguments directly. The parent's technical audit was not used as acceptance evidence. The reviewer previously diagnosed the real-model maximum issue and helped develop the separate Chapter 20 rational-maximum/fixed-form rational-density route. Accordingly, those upstream results are imported here with explicit provenance and are not represented as independently re-proved in this turn. The fresh downstream review checks the SNC restriction argument, the fixed-positive-gap limit passage, and the comparison proof using those inputs.

## Exact reviewed bytes

| Artifact in author packet | SHA-256 |
| --- | --- |
| `MANIFEST.json` | `408c1c750c116696e2d43a3466038e84e14ab48e37cb6f5995fec5e501eb6185` |
| `patched/ch24_bfj_ma.tex` | `b831435e0e66562d10d368f359792c017c53160b0acf4e895b4d23f0d7c6238d` |
| `maximum_principle_replacement.tex` | `d9256a72b68105d51ac1811084f651483becea94255cb357e8a982cec9318ab7` |
| `open_locality_replacement.tex` | `8c047156184f4b16dd7bc1a407ae611d8019be3914f016de001b46afd64e7ac8` |
| `comparison_replacement.tex` | `09884d75b082515f164482f87c6da2e917b0ced5dc8f6a201dd6c668c7be51b1` |
| `ancillary_consistency_edits.tex` | `abeccafccaadefb2217928c53db2d61ad9488e0452c32fa3c6c5ecc647095af7` |

The editing base is the full Chapter 24 in `../p081_ch20_ch22_ch24_unit_weight_followup_20260831/patched/`, SHA `391930d26a49779b10a96ac7e381fefade0677642669e7a20e93c7902e660eae`. The combined-patch live base is SHA `6fba68089c9ed14700f6944e8409b7b477d91478ec3eee5fcabe6c6b5b152916`. All eight records in the candidate's `SOURCE_HASHES.json` were checked against their exact files.

## 1. Scope and imported interfaces

The standing setting is smooth connected projective X over a complete discretely valued field of residue characteristic zero, dimension at least one. Theta is an arbitrary real closed model form with ample generic numerical class; theta itself is not newly assumed semipositive. The chapter's reference-change/gauge convention permits the bounded-MA construction to be presented with a convenient positive reference without narrowing this real-theta statement.

The exact new proof uses three distinct facts:

1. Rational theta-psh model functions are closed under maximum, at a fixed real theta; this input does not require generic ampleness merely to take a rational maximum.
2. Under the chapter's ample-generic-class hypothesis, a real theta-psh model function is uniformly approximable by rational theta-psh model functions at the same theta. This is the separately gated Chapter 20 density input.
3. Uniform limits of continuous psh functions are psh, and the continuous/bounded Monge--Ampere operator is continuous for uniform convergence. The relevant operator construction precedes the repaired maximum/comparison arguments and does not require them.

The proof does not rationally approximate theta, replace the input by an ample theta, or silently claim fixed-form rational density for arbitrary nonample classes.

## 2. Rational strict maximum on a common SNC model

For rational inputs phi and psi, their maximum sigma is a rational theta-psh model function by input 1. Choose one common regular SNC model determining theta and all three functions. Their restrictions are affine on every face of its skeleton and are given at vertices by the normalized vertical-divisor coefficients.

At a vertex x_E with phi(x_E) > psi(x_E), let F meet E. The corresponding edge has positive length. If the order reversed strictly at x_F, max(phi,psi) would have an interior corner on that edge, contradicting its affinity on the chosen common model. Thus phi(x_F) >= psi(x_F), and sigma equals phi on the edge. This includes the equality endpoint case. An edge for any connected component of an intersection suffices; no algebraically closed residue field or unique-edge assumption is used.

Consequently, the vertical divisor D_sigma - D_phi has zero coefficient along E and every component meeting E. Its support is disjoint from E. After clearing its rational denominators, the resulting Cartier divisor has trivial associated line bundle on a neighborhood of E. Its restriction is numerically zero; dividing by the denominator gives the same conclusion for the rational divisor. The real restriction of theta is unaffected. Therefore the component intersection numbers, including the special-fiber multiplicity factor b_E, agree. The strict-set atomic identity follows because both model measures are supported on the common model's divisorial vertices.

This is a support-and-restriction argument. It does not assert that intersection coefficients involving real theta are integers, and it does not replace b_E by one.

## 3. Passage from rational to real inputs

Fixed-theta density gives rational phi_m and psi_m with common uniform error epsilon_m tending to zero. Their rational maxima sigma_m converge uniformly to the continuous function sigma = max(phi,psi), with the same error bound. Uniform psh stability makes sigma psh. The continuous-uniform operator gives weak convergence of all required measures; no model determination of sigma is claimed.

Let U = {phi > psi}, and choose a continuous test h with compact support K contained in U. If K is nonempty, the gap delta = min_K(phi - psi) is strictly positive. Once 2 epsilon_m < delta, K is contained in {phi_m > psi_m}. The rational strict identity can therefore be tested against the same fixed h for all sufficiently large m. Taking weak limits yields equality against h on U.

The topology is valid without metrizability. U is an open locally compact Hausdorff subspace of the compact Hausdorff analytic space; a continuous function compactly supported in U extends by zero. Equality against these tests identifies the two Radon measures restricted to U. The argument never passes weak convergence through a moving characteristic function or assumes that weak convergence alone identifies the mass of an arbitrary strict set.

Thus the unchanged real-input `prop:model-maximum-principle` is justified, with the left-hand measure understood as the bounded/continuous psh operator when the maximum is not a model function.

## 4. Open mixed locality and real numerical restrictions

The unchanged `cor:ch24-model-locality-open` allows real model functions. Put all of its finitely many inputs and theta on one common regular SNC model. If x_E belongs to the open set of equality, that set contains a positive initial segment of every edge incident to x_E. The difference of the corresponding affine functions vanishes on that initial segment and hence on the entire edge. Its values vanish at E and every neighboring F.

The resulting real vertical-divisor difference is a finite real linear combination of components disjoint from E. On a regular model each such component is Cartier and its associated line bundle restricts trivially to E. Taking real linear combinations of their numerical classes is legitimate and gives zero in the real numerical divisor space of E. There is no nonexistent line bundle O(D) attached to an arbitrary real divisor. The theta classes are the same on both sides, and their real intersection products coincide. The formula with b_E therefore gives equality of mixed atoms at every vertex in the open set, proving the asserted measure locality.

This part needs no rational approximation and no rationality of theta or of the input vertical-divisor coefficients. Nonreduced special-fiber multiplicities are retained.

## 5. Comparison from strict locality and fixed mass

For epsilon > 0, sigma_epsilon = max(phi, psi - epsilon) is continuous theta-psh, possibly not a model function. Its positive measure has mass V. On U_epsilon = {phi < psi - epsilon}, the strict maximum identity gives the measure of psi. On W_epsilon = {phi > psi - epsilon}, it gives the measure of phi. Constant shifts do not change the latter measures.

These two open sets are disjoint, so positivity and total mass imply

    mu_psi(U_epsilon) <= V - mu_phi(W_epsilon)
                          = mu_phi({phi <= psi - epsilon})
                          <= mu_phi({phi < psi}).

Taking epsilon = 1/m makes U_epsilon increase to {phi < psi}. Continuity from below is applied only to the single fixed finite measure mu_psi. This proves the unchanged `prop:ch24-model-comparison`. No equality of contact-set masses, no model status of sigma_epsilon, and no moving-measure limit is assumed.

## 6. Ancillary text and limitations

The revised locality introduction correctly permits real intersection coefficients and distinguishes the rational model stage from the real limiting stage. The contact-mass remark correctly says that strict-set identities leave contact-set redistribution undetermined; positive contact mass need not represent an excess of total mass.

The scope ledger also flags inherited informal wording farther in a model example about a component's degree. The repaired proofs retain the full b_E-weighted intersection formula and do not rely on that wording. This review does not certify every inherited example or all subsequent bounded locality/capacity results.

## 7. Exact assembly and visual/source checks

The independent checker verified all 17 author-manifest records and eight source records, reconstructed the exact full Chapter 24 from five unique replacements, and checked the saved incremental and combined diffs against freshly computed diffs. The three mathematical statements are unchanged. All 179 ordered labels are preserved, with no duplicates or control bytes. Earlier weighted-parent changes are unchanged outside those five spans. The combined patch passes read-only `git apply --check`; it was not applied.

The author validator was read and run as a non-mutating assembly check. Archived draft-mode records are intact, but this review did not produce or visually inspect a candidate PDF. Primary-source PDF pages 16 and 17 of BFJ's arXiv:1201.0188v1 were visually checked for the bounded-operator scope. The direct source/interface ledger is `SOURCE_MATRIX.md`.

## Final disposition

The new rational-stage support proof, real numerical restriction argument, positive-gap localization, and mass comparison are valid with the stated inputs. No change is requested to these exact proof fragments. The full real-input statements survive; no blanket closure of real model functions under maximum survives or is needed. Upstream and production gates are unchanged.
