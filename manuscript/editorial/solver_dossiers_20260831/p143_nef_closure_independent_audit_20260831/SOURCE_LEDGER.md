# Exact primary-source ledger for the conditional nef audit

Date: 31 August 2026. Reviewer: `/root/p082_independent_reaudit`.

This ledger accompanies the exact-byte conditional mathematical audit. It distinguishes existing source interfaces from the new conditional deduction. It is not blanket recertification of the source papers or a fresh audit of the full Kähler comparison.

## 1. Xia: prime and full inverse systems

Mingchen Xia, *Operations on transcendental non-Archimedean metrics*, arXiv:2312.17150v3, version dated 22 October 2024. Primary URL: <https://arxiv.org/abs/2312.17150v3>; primary HTML opened during this audit: <https://arxiv.org/html/2312.17150v3>.

- PDF: `/Users/mingchen/Projects/Yethlas/tmp/pdfs/xia23operations.pdf`.
- PDF SHA-256: `773eea71af9f1fff112bf5fcab2b9046b81467df2e37165ee1da3949ff74c6d9`.
- Duplicate PDF `/Users/mingchen/Projects/Yethlas/tmp/Xia23Operations.pdf` has the same hash.
- Text: `/Users/mingchen/Projects/Yethlas/tmp/pdfs/xia23operations.txt`.
- Text SHA-256: `c75572e06a2df8cb9dbd76726678a52db5e79587ec568df41f4886e3e4ee8005`.

| Exact locator | Interface and scope checked |
| --- | --- |
| Section 2.2, Definition 2.3, printed p.5 | On smooth X the I-envelope is normalized by competitors at most zero and integer multiplier-ideal data. Equality of all those ideals determines a normalized I-model potential. |
| Definition 2.7, p.5 | I-equivalence is independent of the chosen sufficiently positive form; the text cites DX22 Theorem 2.13. This supports representative and transition compatibility, not a mass assertion. |
| Section 3.2, Definition 3.2, pp.8-9 | Reduced irreducible unibranch compact Kähler setting. The prime space has normalized I-model, decreasing, concave levels on a half-line with finite endpoint. Positive mass is an additional condition defining a distinct subspace. Connected smooth compact Kähler X meets the scope. |
| Remark 3.3, p.9 | Terminal value is the infimum of the preterminal levels, and later levels are identically minus infinity. The candidate's raw formula uses only preterminal levels. |
| Definition 3.5 and (3.4), pp.9-10 | Transition is normalized I-envelope in the larger form. The inverse limit is in sets and uses the reversed ordering on positive perturbations. Components have a common endpoint. |
| Lemma 3.7, p.10 | Both displayed natural maps among the positive-mass inverse system, the full space, and the inverse system of full spaces are bijections. The proof selects a component at an intermediate half perturbation and a final full perturbation. Read directly, not inferred from the algebraic comparison. |
| Equation (3.5), p.10 | Natural injections of full spaces under a Kähler perturbation. The candidate's restriction-to-total-components formula agrees with this construction. |
| Definition 3.9, p.11 | Limiting mass is obtained as the perturbation decreases to zero. Used only for the zero-class diagnostic, not to build or identify a boundary-class positive-mass curve. |
| Lemma 3.10, p.11 | Recovery from an unperturbed positive-mass curve requires positive limiting mass. This hypothesis is not assumed in the candidate, and the lemma is not used as a recovery input. |
| Section 4 standing hypotheses, p.12; Definition 4.1 and Lemma 4.2, p.13 | Compact Kähler scope, componentwise order, and its compatibility with full-space injections. The candidate's componentwise order proof does not require extending a purely algebraic theorem to transcendental classes. |

The displayed prime marks and domains matter. An isolated prime curve need not have positive mass. The candidate's flattening proof merely selects existing prime components; it never substitutes a vanishing-mass boundary object into Lemma 3.10.

## 2. Darvas-Xia-Zhang: representative change and ideal invariance

Tamás Darvas, Mingchen Xia, Kewei Zhang, *A transcendental approach to non-Archimedean metrics of pseudoeffective classes*, arXiv:2302.02541v3, 17 July 2024. Primary URL: <https://arxiv.org/abs/2302.02541v3>.

- PDF: `/private/tmp/dxz23.pdf`.
- PDF SHA-256: `7fede7c413e396008217a4a4c9638776dbdd7cacff90fdd463bf5ae48220246c`.
- Text: `/private/tmp/dxz23.txt`.
- Text SHA-256: `7d5a061d240096139e6302c2b4da2e9c125a8839730fc90909c1488baa446244`.

Directly checked:

- Introduction, pp.2-3: the positive-mass projective-limit presentation and the explicit identification of the spaces for theta and theta+ddc h. The candidate treats this cohomological identification as existing input. It does not use the following rational-line-bundle comparison theorem for a transcendental nef class.
- Section 2.1, envelope-of-singularity-type paragraph: I-envelope normalization and multiplier-ideal formulation.
- Section 3.3, equations (39)-(41), p.22: transition-envelope invariance of the ideal data, citing DX22 Proposition 2.18(ii), and the endpoint value at the trivial valuation. This section's algebraic target is not imported into the transcendental conclusion; only the envelope invariance interface is used.

The sign in the candidate's normalized representative change was independently checked. Adding ddc h to the background requires subtracting h from the potential, followed by re-enveloping. Smooth bounded factors do not alter local integrability. Consequently this change preserves the raw function, rather than adding an arbitrary function on the ideal spectrum.

## 3. Additional published envelope source

Tamás Darvas and Mingchen Xia, *The closures of test configurations and algebraic singularity types*, Advances in Mathematics 397 (2022), 108198. Primary published PDF, read with the web PDF text tool:

<https://research.chalmers.se/publication/528300/file/528300_Fulltext.pdf>

Section 2.4, printed p.19, explicitly sets the scope to a compact Kähler manifold and a smooth representative of a pseudoeffective class. The relevant interface is Proposition 2.18(ii), printed pp.21-22: the normalized I-envelope is I-equivalent to its argument and is idempotent. The proof uses Choquet approximation and strong openness, with no positive-mass premise in that assertion. The local multiplier-ideal condition and its valuative characterization in Theorem 2.13/Corollary 2.16 support the I-order formulation used to check normalization and curve concavity. The packet does not import a projective finite-energy quantization result from this paper.

This source was read online; no local PDF copy, new hash, or successful visual rendering of its pages is claimed in this audit. Its contribution is the envelope interface just stated, not the conditional Kähler or nef comparison theorem.

## 4. Mesquita-Piccione: same-model monotonicity

Pietro Mesquita-Piccione, *A non-Archimedean theory of complex spaces and the cscK problem*, arXiv:2409.06221v2, 18 September 2025. Primary URL: <https://arxiv.org/abs/2409.06221v2>.

- PDF: `/private/tmp/mp24.pdf`.
- PDF SHA-256: `9eb2ea7686a5962ebc11c5eacd23b0cb3dcb081e27ac48292933f291fc82cb23`.
- Text: `/private/tmp/mp24.txt`.
- Text SHA-256: `0445ccf2c4474b6576a8053d0c7c038ffbd72c2ab27bb3d5704b90dd0e5beb62`.

| Exact locator | Safe interface used |
| --- | --- |
| Section 4.1, (4.1.1), p.32; Definition 4.1.2, p.33 | A model function represented by vertical D is positive precisely when gamma_X+D is relatively nef. Changing the Kähler class by a nef class preserves positivity of that same D. Pullback of a nef class is used only in the forward direction. |
| Definition 4.3.1, p.39 | An MP-psh function is a nontrivial pointwise decreasing net limit of positive model functions in the fixed Kähler class. The identical net works after adding a nef class. |

No MP definition in a non-nef boundary class is silently invoked. The target of the candidate is an intersection of established Kähler-class cones. The separately named fixed-nef-model completion is an auxiliary definition in the diagnostics, and only its inclusion in that intersection is justified.

The proof does not use MP maximum closure, a maximum of real model functions, or a minimum of psh models. Thus the unrelated model-max issues do not enter this same-model monotonicity argument.

## 5. Conditional Kähler packet and dependency direction

Directory: `../p143_kahler_truncation_research_20260831/`.

| File | SHA-256 |
| --- | --- |
| `statement.tex` | `befc29fb89ff79fe90172d03b1fe088e5f19ebf2ca28aedbd4c83cd05f008100` |
| `proof.tex` | `1ef28983e1ac242f9a23080e24ced0c21531899f56ab29a96312f4ce79757652` |
| `MANIFEST.json` | `f5e70b72c09601f27d2210391d8f72935bc37564481be9a5818c19f8926c0b8b` |

The dependency's full statement was read to match its interface: actual-function order isomorphism on all semivaluations for every Kähler class, with no finite-energy restriction. The proof and listed predecessor audit were hashed for preservation, not freshly audited. The nef proof assumes that comparison; it does not prove it from its own conclusion.

Logical order:

1. Existing prime/full systems, I-envelope transitions, representative identification, and order.
2. Explicitly conditional full Kähler raw comparison.
3. Unique inverse images in each Kähler perturbation force coherence.
4. The expanded set-theoretic diagonal reconstructs the nef DXZ object.
5. Existing MP same-model positivity gives auxiliary-form independence and only the fixed-nef-model inclusion.

No step supplies fixed-boundary-class model approximants or handles a non-nef pseudoeffective class.

## 6. Source visual QA and mechanical boundary

The PDF skill was read completely and used for source inspection only. No candidate PDF was created or modified.

Rendered source pages in disposable directory `/private/tmp/p143_nef_source_qa.rRMXlK/`:

- Xia: complete printed pp.5, 8, 9, 10, 11, 13.
- MP: complete printed pp.33 and 39.
- DXZ: complete printed p.3.

All nine renderings were opened and visually inspected. The key prime notation, arrow direction, intermediate perturbation, normalization, domain endpoints, and model-positivity definitions were legible and consistent with the text reading. This is source-formula QA, not an audit of candidate page layout.

The existing candidate draft log `/private/tmp/p143_nef_closure_draft_20260831.lqoL92/main.log` has 14839 bytes and SHA-256 `3760204cb0d5f800024c3318d400f594d9abc99e0bea241542104c4c50580df8`. The read-only post-freeze checker reports no warnings/errors, 12 internal labels, 20 resolved references, three citation keys, and no PDF. Independent byte/control-byte checks also passed. Mechanical checks are kept separate from the conditional mathematical verdict.
