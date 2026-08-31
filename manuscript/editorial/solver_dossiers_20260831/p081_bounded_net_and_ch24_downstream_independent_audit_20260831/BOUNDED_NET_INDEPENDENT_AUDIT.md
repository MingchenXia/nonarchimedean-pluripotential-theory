# Exact-byte downstream review: bounded model-net normalization

Date: 2026-08-31. Reviewer: `/root/p082_independent_reaudit`.

## Verdict and limits

**PASS for the two new replacement proofs, conditional on the explicitly identified upstream inputs.** No unresolved substantive error was found in the compact cofinal-tail normalization, bounded-energy extension argument, coefficientwise polynomial passage, or weak pushforward argument. This is not approval of all of Chapters 26 and 30, an integration authorization, a production receipt, or a new-priority claim.

The reviewed author packet is `../p081_bounded_model_net_normalization_repair_20260831`. Its closed integration gate is preserved. In particular, the final Chapter 30 finite-minima descent argument and the separate actual-real-model maximum clause in its pullback lemma remain excluded and unresolved. The distinct Chapter 21 general-SNC retraction issue is not addressed by this review.

## Provenance

The reviewer did not author these p081 replacement fragments and directly read their exact proofs, editing instructions, source interfaces, and relevant surrounding arguments. The review did not use the parent's sibling technical audit as evidence of acceptance. It is nevertheless not a blind independent discovery of every idea: the reviewer previously diagnosed the invalid clipping/minimum normalization and suggested the compact cofinal-tail route. The present review independently checks the author's actual downstream implementation, particularly its energy chronology and limit passages.

The reviewer also contributed to the separate Chapter 20 real-model maximum diagnosis and fixed-form rational-density repair. Those results are declared upstream inputs, not advertised here as freshly independently re-proved. The bounded-net replacement itself does not require taking real model maxima.

## Exact reviewed bytes

| Artifact in author packet | SHA-256 |
| --- | --- |
| `MANIFEST.json` | `dd2a97d28da10305eab36272cad26a210d2a10b13dd50bb504efe8d9b45184b8` |
| `patched/ch26_energy.tex` | `e37465c226a13e766ed2eecce014913fca3e5cdc2002e1766c151c83c73c6a74` |
| `patched/ch30_functoriality.tex` | `02fa119b5732e3270989e3fddc0aa431add6eb04b27c40c208de9b3411ed2e28` |
| `ch26_bounded_energy_replacement.tex` | `c8c3726d0eedd6d3d7bdea91a82ff13661cde8dac246e8a9fcd395622c86708c` |
| `ch30_bounded_projection_replacement.tex` | `7c684d99bd2efe525d8eef019e419a492a0038f1d6f4b97ad9d5baeadcadf005` |

The exact editing bases are the weighted Chapter 26 parent, SHA `8552d7b5e4c5c58cf48e94db28bf44f3286af4f997adf3f4716cee52d8f26d28`, and live Chapter 30, SHA `61957fd06cf4cd24833cd5d7d698b9aa8640d9d094ca7d8237a235be395bf951`. The live Chapter 26 combined-patch base has SHA `242f10b4c8be9e90bc457f897999f00d24d011a6c1b564436fe9c3a82f8d3d3d`. The previously authored graph replacement remains byte-identical, SHA `32162fefceffa938272c9e7230206496538c5a52290083d6573f3d1faf31ff31`.

The packet's `SOURCE_HASHES.json` records nine exact source files. Every recorded size and hash was checked. These historical live-source hashes identify the review inputs; they are not instructions that live files must remain unchanged forever.

## 1. Scope and the compact-tail argument

Chapter 26 retains its standing semipositive reference form omega with ample generic numerical class. Thus the zero potential used in the bounded-energy formula is psh. No extra algebraic-closure hypothesis is introduced. The BFJ framework used here is the chapter's smooth projective, complete discretely valued, residue-characteristic-zero setting; this is not a statement over every complete valued field.

If continuous model functions phi_alpha decrease pointwise to bounded phi, every phi_alpha is at least phi. Hence the lower bound is automatic. Set B = sup(phi) + 1. The open sets {phi_alpha < B} cover the compact analytic space. A finite subcover and one common upper index alpha_0 give phi_alpha < B everywhere for every alpha >= alpha_0. That tail is directed and cofinal and converges to the same phi. The proof neither takes a minimum with B nor translates the approximating functions. It does not infer uniform convergence to a potentially discontinuous limit. This argument works for arbitrary directed nets, not merely sequences.

The same reasoning works for finitely many independently chosen nets by first taking one tail for each and then taking their finite product. No countable diagonal, smallest index, or order-complete index set is needed.

## 2. Chapter 26: existence and independence

The unchanged proposition is `prop:bounded-energy-identities`. Its Step 1 defines the bounded energy by the finite formula

    E_omega(phi) = (1/(n+1)) sum_j integral phi MA_omega(phi^j, 0^(n-j)).

Each summand of the model formula converges by the earlier Chapter 24 weighted bounded Monge--Ampere continuity theorem, with weight phi_alpha and slots phi_alpha or zero. All weights and slots are bounded psh on a common tail. The measures are positive of fixed finite mass, so the displayed bounded integrals are finite. This proves the limit and the formula without presupposing energy monotone continuity.

For the comparison of two approximating nets, fix alpha and epsilon > 0. The sets

    F_beta = {phi'_beta >= phi_alpha + epsilon}

are compact, decrease with beta, and have empty intersection because phi <= phi_alpha. The finite-intersection property and directedness imply eventual emptiness. Model energy monotonicity and the constant-translation identity then compare the two limits with an epsilon times volume error. Taking the limits in the stated order and then swapping the nets is valid. The shifted function is only a comparison majorant; no claim is made that translating the approximants preserves the original limit. Real constant translations are legitimate in the chapter's real-model convention.

Step 1 already identifies the intrinsic bounded formula, but the extra independence argument is consistent and not circular.

## 3. Chapter 26: cocycle, sandwich, and variations

For two bounded endpoints, the product of their bounded cofinal tails is a valid common index set. The model cocycle integrals involve signed weights psi_beta - phi_alpha and mixed measures whose slots decrease. Splitting the signed weight into its two bounded psh terms permits the stated weighted continuity theorem to be applied separately. Multilinearity and finite sums then justify the limit.

The model sandwich inequality needed for arbitrary endpoints is available from the chapter's model concavity argument; its accompanying discussion explicitly gives the inequality without requiring phi <= psi. The author does not need ordered model approximants to ordered endpoints. This detail matters because independent decreasing approximants need not preserve an order relation between their limits.

The variation passage is coefficientwise, not an unsupported interchange of derivatives and net limits. With u = psi - phi, the model energy along phi + t u is a polynomial of degree at most n+1. Its coefficients are finite linear combinations of integrals of signed bounded psh differences against mixed bounded Monge--Ampere products, after expanding dd^c u as omega_psi - omega_phi. Each coefficient therefore converges by the preceding weighted argument. A finite family of converging coefficients gives convergence of the polynomials and their first and second derivatives. This validates the stated variation formulas and concavity on the admissible segment. At endpoints the derivatives have the corresponding one-sided meaning; any other compact admissible segment can be treated by choosing its bounded psh endpoints. There is no differentiation of an arbitrary limiting family of functions in t.

## 4. Chapter 26: chronology of Step 4

For a decreasing net of bounded psh functions phi_gamma with bounded limit phi, choose an index gamma_0. The tail has lower bound inf(phi) and upper bound sup(phi_gamma_0). Apply the bounded formula already established in Step 1 separately to each phi_gamma and phi. Chapter 24 weighted continuity then passes every summand to the limit. The inequalities already obtained in Step 3 supply energy monotonicity, so the convergence is decreasing.

The chronological input is the Chapter 24 bounded Monge--Ampere theorem, not the Chapter 26 energy assertion being proved. The relevant Chapter 24 scalar-pairing construction and bounded-MA extension occur earlier and explicitly do not assume the Chapter 26 energy functional. No model approximation from below, decreasing diagonal construction, or desired energy-limit assertion is used in Step 4.

## 5. Chapter 30: bounded projection and weak pushforward

The unchanged statement `thm:ch30-finite-bounded-projection` concerns a finite surjective map of degree d between the standing smooth projective spaces and n bounded theta-psh inputs. The theta input remains real; its generic class is ample. Finite pullback preserves the needed generic ampleness.

One decreasing model net is chosen for each input. The compact-tail argument and finite product yield bounded nets with exactly the original limits. Pullback preserves those inequalities and limits. The proof uses the model-divisor, curvature, and nef-pullback parts of the cited model pullback calculus, not its separately defective claim that an actual maximum of real model functions must be a real model function.

The earlier bounded-MA theorem, specifically the weak convergence established in Step 6 of its proof, gives convergence of the measure nets on both spaces. The model projection formula gives f_* mu_Y,alpha = d mu_X,alpha. For arbitrary h continuous on X, h composed with f is continuous on Y, so weak convergence gives the same equality for the bounded limits. This is the correct topological pushforward argument and preserves the degree d factor.

The updated `rem:ch30-test-function` correctly distinguishes weighted convergence for bounded psh weights from weak convergence against arbitrary continuous tests. The latter follows from the upstream dense linear span of psh model tests and uniform mass bounds; it does not assert that every continuous function itself is a difference of two psh functions.

## 6. Primary-source and assembly checks

The primary BFJ Monge--Ampere manuscript, arXiv:1201.0188v1, was read directly in Section 2.1 and Section 3. Its Theorem 3.1 gives positive bounded-MA measures and weighted convergence along decreasing bounded nets for an arbitrary real closed form with ample generic class. The function-field assumption attached to its main Monge--Ampere existence theorem is not a hypothesis of this bounded-operator theorem. PDF pages 16 and 17 were rendered and visually inspected to verify this scope and the theorem's actual text. Details and exact source hashes are in `SOURCE_MATRIX.md`.

The independent read-only checker `check_packets.mjs` verified all 16 manifest entries and all nine source entries, reconstructed both full chapters from their two uniquely occurring old/new spans, and compared the result byte-for-byte. The theorem/proposition statements are unchanged. Ordered label lists are unchanged: 250 labels in Chapter 26 and 224 in Chapter 30, with no duplicates or TeX control bytes. The weighted Chapter 26 graph fragment remains present unchanged. The excluded Chapter 30 finite-minima paragraph remains present rather than being silently certified or repaired.

Freshly generated incremental and combined diffs match the saved patches. `git apply --check` passes for the combined patch; no patch was applied. Both author validators were read and run as non-mutating checks. Their archived draft-mode compilation records are mechanical evidence only. This audit did not compile a candidate PDF, and no candidate-PDF visual approval is claimed.

## Final disposition

The scoped replacement proofs are mathematically coherent with the declared upstream bounded-MA and model-calculus inputs. They remove the identified normalization errors without weakening the real input statements. There is no additional repair request for these exact fragments. The production and integration gates, excluded downstream defects, and separate upstream review obligations remain unchanged.
