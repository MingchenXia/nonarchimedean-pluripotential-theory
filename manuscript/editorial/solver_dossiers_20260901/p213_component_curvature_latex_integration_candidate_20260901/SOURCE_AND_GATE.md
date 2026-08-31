# Component-curvature LaTeX integration candidate

Date: 1 September 2026. Author/adapter: /root/p213_skeletal_hostile.
Status: SCRATCH ONLY. No live chapter, bibliography, frozen predecessor, Git state, production service, or production settings are changed by this packet.

## Exact gate

The original Markdown submission for run 20260831T203725Z_6a6a732dcebd returned the mathematical verdict "correct", with zero critical errors and zero gaps. Its statement/proof binding is recorded by the original submission packet and the root audit. This does NOT presently constitute clean production authorization: the execution log records an MCP memory_init call requiring approval under approval_policy=never, followed by a local-helper invocation of the same operation (log lines 2080–2103). Root has stopped live promotion and is addressing that approval-path issue separately. This candidate neither retries nor works around it.

The LaTeX below is a rewritten, source-dependent presentation, NOT the identical bytes of that Markdown proof. Its mathematical scope has been author-checked against the original independently reviewed targets (I) and Section 4.1, including all three sufficient cases. That is not a new independent audit or a new production verdict on the LaTeX. Root review and any required exact-final proof submission remain gates. The adapter previously suggested the common-curvature domination refinement and therefore does not claim independence for that argument.

Production2, the full-CPsh weighted/polar argument, is NOT an input to any file inserted by candidate.patch. A later corollary using it must be a separate amendment, not a retroactive reading of this version.

## Insertion plan and dependency direction

INSERTION_PLAN.json pins the current DURABLE book, not the older scratch chapters. candidate.patch has portable a/manuscript/... and b/manuscript/... headers. It consists exclusively of four insertions into three files:

1. Ch14: an explicit imported-source item immediately before the existing end of the prerequisite list. This is necessary because the chapter says no other statement is used without proof.
2. Ch14: the complete new subsection after the proof of prop:current-cycle-closed and before Fibre integration. At that point integration currents, proper pushforward, order-zero positive coefficients, the canonical fundamental cycle and Stokes have all been established.
3. Ch72: a short comparison paragraph after the existing curve-component discussion and before the higher-dimensional Hessian-regular-basis paragraph. It changes no problem, atom count, old label, old equation, or old assertion.
4. Bibliography: the Ducros article entry, whose key is absent in the baseline.

The references to Ch16's function-class/induction discussion are reader guidance. The new proof states its own minimal-sheaf positivity argument and imports CLD Lemma 8.5.5 directly; it does not depend on the later book polar proof. There is no logical circle Ch14 -> new Ch16 nullity -> Ch14. The integration location is an optional consequence of the Ch14 calculus, not a new prerequisite for the fundamental-cycle proof.

## Scope ledger

- Field: every complete non-Archimedean K, including trivial valuation; no DVR, characteristic-zero or perfectness assumption.
- Space: good, separated, usual-strict, boundaryless, pure n>=1; normality and reducedness are NOT assumed.
- Components: actual reduced analytic components over K, with positive generic multiplicities m_i in canonical integration. No geometric base change, normalization current pullback, or nilpotent-weight erasure.
- A: a single ordinary approximating neighborhood works for the entire sequence; direct local smooth uniform approximation, not the full CPsh closure. The decreasing-subsequence proof is supplied.
- First assertion: canonical curvature equality iff equality against every component current for u,v in A.
- Second assertion: arbitrary CPsh u,v, but with the explicit coefficient-measure crossing-nullity of their COMMON curvature.
- Three sufficient cases: one of the given potentials lies locally in A; the common curvature has a local A-potential; or the common curvature is zero.
- Crossings can be divisorial. All support and measure arguments are compact-local. They use individual total-variation nullity, not cancellation of signed masses.
- Ordinary restriction: all actual localizations in the proof are ordinary. An application to a different ordinary open satisfying the displayed ambient hypotheses uses that open's own components. The text does not assert that usual strictness passes to every ordinary open over a trivially valued field.
- Excluded: unconditional general-CPsh analytic nullity, scalar-current classification, the earlier target (II), arbitrary-current/all-bidegree Bedford–Taylor independence, and retirement of P21.3.

## Exact source interfaces

The exact source/submission/audit/receipt hashes are in INPUTS.json. In particular the submitted statement is 6a6a732dcebd3fd62f1f01fc4f50d985941f4d43c2bc409709956de194b777f5 and proof is b0d74bf26276199f4e03da2ef18b78698ecf4cda93ede2a576df0a73b3116255.

1. CLD, arXiv:1204.6277v2, 25 July 2025, Definitions 8.1.7 and 8.1.13/Lemma 8.1.8: distinct uniform-closure sheaf and local approachability. The direct sequence is an explicit stronger sufficient class, not a hierarchy-collapse argument.
2. CLD Lemma 8.5.5: positivity of dd(wQ) for a continuous CPsh w and positive separately closed Q, in full minimal-sheaf scope. Continuous multiplication/positive-current continuity and the proper pushforward identity use Sections 7.2, 8.5 and 15.2, including Proposition 8.5.6.
3. CLD Corollary 16.9.4 (printed pp. 466–467): analytic nullity for locally approachable continuous potentials. The proof imports only its one-potential case and does NOT enlarge its hypothesis to full CPsh. The weighted estimate behind that cited source is an external known theorem, not silently re-proved here.
4. CLD Sections 13.5.2, 16.6.1–3 and the already repaired live book fundamental-cycle theorem: delta_X=sum_i m_i delta_i. Canonical generic lengths remain visible.
5. Ducros, Les espaces de Berkovich sont excellents, Ann. Inst. Fourier 59(4) (2009), 1443–1552, Section 4, especially Theorem 4.20 and 4.21–4.24: G-local finiteness and actual analytic-component/dimension geometry. In a good space compact supports meet only finitely many components, using finitely many affinoid neighborhoods. This is a source-dependent corollary of that geometry and CLD nullity; no novelty or priority claim is made.

Primary records:
- https://arxiv.org/abs/1204.6277v2
- https://www.numdam.org/item/AIF_2009__59_4_1443_0/
- https://www.numdam.org/article/AIF_2009__59_4_1443_0.pdf

The Ducros bibliography metadata was checked against the official Numdam article record: DOI 10.5802/aif.2470. No bibliography key was invented for an uncited theorem.

## Proof adaptation map

The definition and sequence paragraph correspond to submitted PROOF Section 1. The geometry, canonical weights, pullback of FUNCTIONS/forms, and signed-coefficient pushforward correspond to Section 3. The explicit positive-versus-signed nullity conversion retains Section 2's relevant source consequence; the source's nontrivial weighted theorem is imported rather than expanded into a new proof. The first equivalence is Section 4. The positive weighted sums, domination, support and three sufficient cases are precisely Section 4.1.

The LaTeX supplies labelled equations and item references, makes the full-sheaf positivity reason explicit, and names the proper-pushforward/current-versus-measure distinctions. Those explanatory rewrites are the reason exact-final review is still required. No material source assertion is replaced by the older scalar classification.

## Mechanical checks and their limits

check.mjs is read-only. It checks input hashes, unique insertion anchors, exact in-memory patch application, baseline recovery by removing only the inserted bytes, preservation of old labels/reference tokens/problem environments, all new book references and bibliography keys, and the manifest when present. It never applies a patch or writes the book.

The syntax_check wrapper compiles only these snippets with the existing notation and external Ch14/Ch16 auxiliary labels. The commands use pdflatex -draftmode, so no PDF is generated and no visual-layout or full-book compilation claim is made. The final log and BibTeX log are preserved as syntax evidence. The wrapper is not part of the proposed book patch.

Run:
    node check.mjs
from this directory (use the bundled absolute Node path if node is unavailable). The read-only baseline checks intentionally fail if the book or pinned inputs have changed; rebase by creating a new candidate, not by editing this frozen one.
