# P14.2 raw ideal-valuative transform: exact-byte adversarial audit

Date: 2026-08-31. Reviewer: `/root/p082_independent_reaudit`.

Verdict: **PASS for the precise frozen mathematical statements.** No critical error or unresolved substantive proof gap was found. The proof establishes upper semicontinuity on all semivaluations in the stated topology, including nonzero support, and an explicit decreasing sequence of bounded continuous finite-ideal expressions. The full compact-Kähler pseudoeffective DXZ corollary is retained, not replaced by a projective or divisorial special case.

This is a mathematical/source/assembly audit, not production verification or permission to retire an inventory item. No production call, live manuscript edit, or inventory change was made. The production approval gate is unchanged. No novelty or priority claim is made.

## 1. Frozen objects and provenance

Candidate directory:

`/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260831/p142_raw_transform_usc_research_20260831`

| Object | SHA-256 |
| --- | --- |
| `statement.tex` | `488868dc2b2d1d62b23864970f8bf36acc0a6c7c85d27eaf66e6a9ed7120c949` |
| `proof.tex` | `bf991c724e138626fbd8fcd4fc6f613d7979f3bf75a3614c569a1ff3c7d21e21` |
| `example.tex` | `7010c2a461de6f2ed1fb7c1f0170c6eaa8aed38b88492ea919f8b0c1eea49f6f` |
| `MANIFEST.json` (20 entries) | `c677e7a289d9b957d2269cb7b68da4dfcfa89faa4a761a15e8fd8b6dc65e5a87` |

The root supplied the finite-mesh mechanism and the stronger explicit continuous sequence and authored the frozen principal text. This reviewer tested the argument adversarially, checked the primary interfaces, and suggested before freezing that the finite lattice expressions be described in **negative** ideal coordinates. The exact frozen statement contains that correction. Thus the reviewer is independent of the principal authorship, but is not an independent originator of the proposed mechanism. Earlier curve/model-density/analytic-fiber work by this reviewer is not used as an input. Neither the author's source report nor a parent's acceptance assertion was treated as proof.

The complete current statement, proof, example, source report, assembly files, source-label extraction, and recorded build status were read. `check_exact_packet.mjs` is a separate read-only checker; neither author freeze script was executed. The candidate has not been altered by this review.

## 2. Abstract topological lemma

The exact assumptions are essential and sufficient: a finite real endpoint c, a family a_tau in [0,+infinity] on an arbitrary topological space, lower semicontinuity for each fixed parameter, and monotonicity a_s <= a_t for s <= t. There is no hidden compactness, metrizability, sequential convergence, continuity in tau, concavity, or finiteness of the ideal values.

For N >= 1 the floor c-N and N^2 left endpoints cover precisely [c-N,c) with intervals of length 1/N. The candidate never evaluates the family at the potentially inadmissible endpoint c. The nonnegative range controls every parameter below the floor. For the remaining parameters, the left-point order a_left <= a_tau gives the correct inequality

`tau - a_tau <= left - a_left + 1/N`.

The direction is not interchangeable with right sampling. It remains valid when either ideal quantity is infinite: only a finite number minus positive infinity occurs. The sandwich G_N <= max(c-N,F) <= G_N+1/N is therefore valid at every point. Each G_N is a bounded finite-valued upper-semicontinuous function. The exact identity F = inf_N(G_N+1/N), not an unsupported assertion that arbitrary suprema of upper-semicontinuous functions are upper semicontinuous, finishes the proof. Arbitrary infima are upper semicontinuous by the union formula for strict sublevel sets.

At a point with F=-infinity, every level contributes -infinity, G_N=c-N, and the same infimum tends to -infinity. At a point with F=c the top interval remains covered from the left. Neither endpoint case requires a limiting value of the family at c. The argument even applies to an empty ambient space vacuously.

Every dense parameter subset gives the same supremum: choose points immediately to the left of a parameter with a finite contribution and use monotonicity, then let the parameter error tend to zero. If there is no finite contribution, both suprema equal -infinity. This proves the stated dense-subset result, not just a statement at divisorial valuations or continuity points.

## 3. Ideal evaluation, asymptotic limit, and order

The actual MP/Chapter 58 topology makes each coherent ideal evaluation continuous with values in [0,+infinity] in the order topology. Nonnegativity is built into the ideal spectrum; it also follows from the ideal-semiring relation I+O=O. Inclusion reverses ideal values and products add them, including infinite values. No boundedness on divisorial valuations or extension from a dense subset is used.

On a complex manifold multiplier ideals of quasi-psh functions are coherent. DEL00 Theorem 2.6(ii) applies locally to the analytic weights; bounded smooth changes do not change multiplier ideals. Its normalization uses exp(-2 phi), so one applies it to half the candidate potential, whose convention is exp(-phi). This yields exactly the subadditive ideal inclusion used in the proof, with no algebraicity or projectivity assumption.

The resulting b_m is a nonnegative extended-real superadditive sequence. If b_q is infinite, all b_m with m >= q are infinite (m=q is immediate, m=q+r follows from superadditivity). Otherwise m=kq+r and b_r >= 0 imply b_m >= k b_q, so the liminf dominates every b_q/q. Comparing to the supremum proves the Fekete identity even when the supremum is infinite. There is no unjustified division or subtraction of infinities.

For each fixed tau, the supremum of the continuous functions m^{-1}v(I(m Gamma_tau)) is lower semicontinuous. Decreasing quasi-psh levels give I(m Gamma_t) contained in I(m Gamma_s) for s <= t by local integrability; consequently their asymptotic ideal values increase with tau. This is the exact order required by the mesh lemma. No strong-openness claim or continuity of multiplier ideals in tau is needed for this monotonicity step.

The manifold hypothesis is retained. This review does not assert a singular-complex-space multiplier-ideal theorem. The assumption excluding a level identically -infinity on a connected component keeps the weights within the ordinary quasi-psh convention; no extra positivity of a background class is required by the elementary theorem.

## 4. Explicit continuous sequence

Every finite A_{tau,M} is continuous into the extended positive half-line. Subtraction from a finite tau gives a continuous function into an extended negative half-line. Taking the outer maximum with the finite floor removes -infinity and produces an ordinary real-valued continuous function. Finite min/max and positive rational rescaling are legitimate operations here. In particular, the phrase 'negative ideal evaluations' in the frozen statement correctly expresses tau-A as a finite minimum of translated negative evaluations.

The displayed bounds c-N+1/N <= B_{N,M} <= c+1/N are valid, though the upper estimate can be sharpened to c. They are bounds for each approximant independent of v; compactness is not being invoked.

As M increases, each A increases to its defining supremum. A maximum over finitely many decreasing extended-real terms commutes with the limit: below any fixed real threshold, a single index works for all finitely many terms once all their limits are below that threshold. Retaining the floor handles the case where every ideal term tends to -infinity. Thus B_{N,M} decreases in M to G_N+1/N. The mesh sandwich gives both B_{N,M} >= F and inf_{N,M} B_{N,M}=F.

The finite squares 1 <= N,M <= k exhaust the countable pair index set. Their finite minima f_k are bounded continuous functions decreasing to this double infimum. No sequence is extracted from a net on an arbitrary nonmetrizable space; the sequence is explicitly constructed. Its existence reflects the countable multiplier indices and the special monotone-level structure, not a false general assertion about all upper-semicontinuous functions on compact Hausdorff spaces.

The proof correctly denies positivity of these expressions. In particular, a finite minimum does not become MP-psh or semipositive merely because its constituents involve coherent ideals. The stronger approximation claim therefore does not silently settle the positive-approximation or image problems.

## 5. Full inverse-system corollary

The source DXZ Definition 3.3 and preceding test-curve definitions supply a perturbation component with a common finite terminal parameter and decreasing genuine interior quasi-psh levels. Choosing a component requires no potential of positive mass in the unperturbed class.

The exact transition replaces a level by its I-envelope. Published DX22 Section 2.4 explicitly has compact-Kähler, arbitrary real pseudoeffective scope, despite the paper's projective introduction. Its Proposition 2.18(ii) preserves I-equivalence, defined by all positive-real multiplier ideals, hence preserves every positive integer multiplier ideal needed here. This is equality of ideal sheaves, not merely equality of divisorial evaluations.

A common component compares any two perturbations, and their endpoint is the same. Therefore their ideals at every sampled level coincide. All asymptotic values, the raw supremum, and the finite expressions A, B and f coincide at every semivaluation. This verifies the full perturbation-independent conclusion, including zero-volume unperturbed classes. No ample line bundle, rationality, nefness, bigness, divisorial density, positive unperturbed mass, or non-Archimedean envelope property is inserted.

The Chapter 71 imported labels encode precisely the independently checked ideal and transition interfaces; they do not import the desired upper-semicontinuity conclusion circularly. The older manuscript says this conclusion is not yet proved there. The candidate supplies a new elementary argument for it rather than assuming it.

## 6. Infinite-support example

The local multiplier-ideal calculation for psi=lambda log|z|^2 is correct with the candidate convention exp(-m psi): a germ of integer order q is integrable exactly when q-m lambda > -1, equivalently q >= floor(m lambda). This includes the integer borderline correctly. Smooth metric factors do not change the ideal, and away from p the ideal is the unit ideal.

For finite v(m_p), dividing the floor exponent by m and taking the limit gives lambda v(m_p). If v(m_p)=+infinity, eventually the exponent is positive, hence all sufficiently late ideal values are infinite; zero exponents at early indices give the unit ideal and value zero. No expression 0 times infinity is required. Such support semivaluations genuinely exist: the trivial seminorm at the closed point p gives value infinity on ideals vanishing at p and zero on the others. The displayed F=c-lambda v(m_p) and the possibility F=-infinity are therefore substantive, not vacuous formal cases.

## 7. Source, assembly, and visual checks

`SOURCE_LEDGER.md` gives exact live-source hashes, local primary PDF/text hashes, theorem locators and scope, web-only published sources, and the limits of the visual checks. The primary MP, DXZ, and Xia Operations PDFs were read at the stated versions. The specified MP/DXZ/Xia pages were rendered and visually inspected. DX22 and DEL00 published primary text was read through the web reader; no local hash or completed visual inspection is claimed for those two sources. Xia's projective comparison theorem is explicitly not a substitute for the full-scope topological proof.

The read-only checker verifies all 20 candidate manifest entries, the four principal frozen hashes, all seven recorded parent inputs, the two source auxiliary files, the six exact imported label records, all 14 internal labels and three imported labels, cited bibliography keys, and absence of forbidden control bytes in TeX. These checks are assembly evidence, not mathematical evidence.

The frozen BUILD.json records a successful final standalone **draft-mode** pass with no warnings, no PDF, and four resolved bibliography keys. The final log and bibliography were inspected; earlier auxiliary-import/BibTeX path errors remain in the packet as history. The final successful normal relative-basename BibTeX invocation did not relax a protection. This reviewer did not rerun the author build or claim a candidate-PDF visual audit: no candidate PDF was produced. No full-book compile claim follows.

The candidate bibliography cites the published MP/DXZ papers, while the local source locators independently checked here are the explicitly hashed arXiv versions. This is a source-version precision note, not a mathematical gap in the verified interfaces. It should not be rewritten as a claim that the published pagination was visually checked.

## 8. Final scope and limitations

Unresolved substantive errors: none found in the exact packet. Pre-freeze literal issue: the allowable-coordinate wording has been corrected to negative ideal evaluations. No residual correction request remains for the principal text.

The result addresses the entire P14.2 upper-semicontinuity signature and more precisely produces the displayed decreasing continuous sequence. It does not establish MP positivity or positive approximation, a Monge--Ampere/energy theory, the image characterization, the equivalence of P- and I-sensitive theories, or a general nontrivially valued envelope theorem. It does not retire P14.3--P14.8 or any other open atom. Integration and any P14.2 retirement remain subject to the separate production and editorial gates.

The exact mathematical verdict binds only the hashes in Section 1. Later edits require a new exact-revision check. The source ledger and `SHA256SUMS` bind this report and its read-only checker; later drift of historical live inputs should be reported as drift, not retroactively described as mathematical failure of the frozen theorem.
