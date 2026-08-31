# Source and scope ledger: original-field model adaptation

Date: 31 August 2026. Author: `/root/p082_independent_reaudit`.

## Primary theorem texts checked directly

### CLD, arXiv:1204.6277v2 (25 July 2025)

Primary version: <https://arxiv.org/abs/1204.6277v2>.

Local PDF `/private/tmp/CLD25.pdf`, SHA256 `5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719`; local text `/private/tmp/CLD25.txt`, SHA256 `021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e`.

- Section 11.1.11, printed p.302, gives the affine analytification by seminorms and its exhaustion by affinoid balls; together with the completed-residue-field definition this supports the density proof used in Section 2.
- Lemma 12.2.3 and its proof, pp.334-335, use strict approximation at a point and ordinary shrinking to obtain exact equality of tropical maps. Its own statement concerns analytic functions; the algebraic rational variant is justified explicitly in the note.
- Proposition 18.4.5, proof pp.521-522, explicitly replaces analytic local units by algebraic units using density of the rational function field at the full-dimensional point. This is source precedent, not a claim of novelty for Section 2.
- Section 15.5.1, Proposition 15.5.4 and proof, pp.426-427, distinguish ordinary from G-local descriptions and exploit exact norm preservation by close approximation. They were read as a source-topology check, not used to turn a formal cover into an ordinary cover.
- Corollary 15.2.5 gives compact ordinary smooth cutoffs. The finite partition used here is constructed explicitly.
- Lemma 7.1.13 and Proposition 15.2.1 are the fixed-bidimension support input for current transport under proper modifications. The two first-derivative degrees are checked explicitly; the unqualified differential sentence in 7.1.12 is NOT imported.

### Temkin: embedded desingularization, exact characteristic restriction

Michael Temkin, *Functorial desingularization over Q: boundaries and the embedded case*, arXiv:0912.2570v2, 6 September 2016. Primary theorem texts read directly at <https://arxiv.org/pdf/0912.2570v2>, especially printed pp.2-5, Theorems 1.1.3, 1.1.6, 1.1.11, 1.1.13 and 1.1.18, including surrounding definitions/qualifications.

Theorems 1.1.6 and 1.1.3 give regularity and strictly monomial total boundary transforms for noetherian quasi-excellent schemes OVER Q. The note uses them only when R contains Q, hence in residue characteristic zero. The source's 'strictly monomial' output retains divisor multiplicities. Theorem 1.1.11 is the weaker principalization statement, not a stronger transverse-centre algorithm. Theorem 1.1.13 extends resolution to formal and analytic categories, but is not used to globalize this packet's model data. Crucially, Theorem 1.1.18 explicitly requires a finite DVR extension before the normalized base change becomes regular strictly semistable. None is treated as original-field reduced semistable domination.

No local copy or byte hash of this web-read PDF is invented. The stable versioned primary URL and exact theorem locators identify the source. No source PDF visual inspection is claimed in this task.

### Temkin: altered local uniformization

Michael Temkin, *Altered local uniformization of Berkovich spaces*, arXiv:1503.05729v2, 6 October 2016. Primary text checked at <https://arxiv.org/pdf/1503.05729v2> and in the existing local extraction `/private/tmp/temkin_altered_local_1503.05729.txt`.

Read the introduction and exact Theorems 3.1.3, 3.3.1 and 3.4.1 with their surrounding conventions. The first is affine rig-smooth formal algebraization; the latter results use a finite extension plus a rig-etale/quasi-etale covering. They do not provide a proper birational modification of the original analytic space. A future-research observation in the introduction is not substituted for a theorem. The local source PDF/text hashes are recorded in the manifest.

### GRW: direction and field of the skeleton comparison

Walter Gubler, Joseph Rabinoff and Annette Werner, *Skeletons and tropicalizations*, arXiv:1404.7044v3, 28 February 2016; primary version <https://arxiv.org/abs/1404.7044v3>.

Local PDF `/private/tmp/grw1404.7044v3_p213_residual.pdf`, SHA256 `f7a909a8508032d8e2e0a0c6f9cd14b06f36cfa465c3e83fa5d40be6033678ad`; text `/private/tmp/grw1404.7044v3_p213_residual.txt`, SHA256 `851b1820299b758f96db87f37da1ce786b6d169597dc9bebb0f5e3208b1079af`.

Section 1.1 explicitly assumes an algebraically closed complete nontrivially valued field. Definition 3.1 and Sections 3.2-3.6 specify horizontal coordinate divisors and explain DVR base change. Proposition 9.4 and Theorem 9.5, printed pp.33-34, tropicalize an already given semistable skeleton faithfully by chosen rational functions; they are not a realization theorem for every prescribed moment over an original non-algebraically-closed K. The local pair equations are used only to make the obstruction's hypothetical strict-pair condition explicit. No algebraically closed theorem is silently transplanted to a DVR field.

### Stacks Project, current primary statements

- Tag 0F41, Theorem 38.33.8: <https://stacks.math.columbia.edu/tag/0F41>. Separated finite type morphisms to a quasi-compact quasi-separated scheme admit compactification. Applied to X -> Spec(R); K=R[1/pi] makes this finite type. The note separately proves that the scheme-theoretic closure of the integral open X has generic fibre X and is flat over R.
- Section 29.20, especially Lemma 29.20.7: <https://stacks.math.columbia.edu/tag/0HA6>. Finite type schemes over a complete noetherian local ring are excellent.
- Tag 0BBQ, Lemma 72.3.3: <https://stacks.math.columbia.edu/tag/0BBQ>. The isomorphism locus of a proper birational morphism with reduced source contains codimension-one normal target points. Its scheme reference is Lemma 33.17.3. This is used to prove persistence of the multiplicity-two exceptional divisor, not merely asserted from a picture of a blowup.

The two obstruction calculations are elementary local equations and valuation orders, with their exact disproved statements limited in Section 4. They do not claim that every moment necessarily forces the example's model, or that nonreduced SNC support cannot be achieved.

## Exact frozen research inputs and revalidation

The entire residual-wall note, its obstruction/source ledgers, and the entire generic common-moment note were read. Before analysis all sixteen residual-wall checksum entries and all thirteen generic common-moment checksum entries passed. The frozen residual-wall statement is REDUCED strictly semistable, despite the shorter historical directory name. Its nonreduced extension is not an input theorem.

The generic common-moment note is authored by this diagnostic's author. A later independent conditional audit exists, but it is not a proof of the new model-capture hypotheses. Its displayed R premise remains explicit. Historical inputs and primary local files are pinned by the new manifest; no historical byte was changed.

The parent contributed the new research question, requested the ordinary-locality and mixed-component-wall distinctions, and proposed the nonreduced finite-flat radial-box subproblem. During this investigation the parent froze a separate finite-projection candidate, `../p213_nonreduced_tube_finite_projection_research_20260831/RESEARCH_NOTE.md`, SHA256 `3001c94985c0d3e60f184ffd9f0e9591775ea026a98cd20ee538005edac11b7a`. Its exact hash and stated boundaries were checked for the status update in Section 7; its proof was NOT independently audited here. Before this ledger's freeze its separate independent audit reported PASS, with the individual-cell interpretation conditional on R: `../p213_nonreduced_tube_finite_projection_independent_audit_20260831/INDEPENDENT_EXACT_BYTE_AUDIT.md`, SHA256 `9251b5571386ca23c5e5d6bb5d307559340460a200e8c63a7cffe200d9b54159`. Only the verdict and byte pins were read for this status update. The finite-projection result is not a dependency of this note's resolution claims. Its additional unramified-DVR generic-Gauss argument concerns individual source coefficients under R, not only aggregate pushforward. The global nonreduced residual-wall extension is separate work in progress. No production acceptance is inferred from that audit.

This note supplies a bounded diagnostic and elementary/source-backed reductions. No current slicing, alteration pullback, field extension, live edit, git action or production submission occurred. No PDF render or visual QA was performed in this task; the source texts and theorem hypotheses, not PDF layout, were inspected.
