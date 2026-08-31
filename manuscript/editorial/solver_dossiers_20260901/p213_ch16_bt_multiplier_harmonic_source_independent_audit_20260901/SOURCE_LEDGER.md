# Exact source and dependency ledger

Date: 2026-09-01. Only primary CLD text and the specified existing manuscript inputs are used for mathematical source comparison. This is an ordinary-CLD current/CPsh audit; weakly smooth forms and delta-form cohomology are not substituted for that theory.

## Primary source

Antoine Chambert-Loir and Antoine Ducros, *Formes différentielles réelles et courants sur les espaces de Berkovich*, July 2025 revision, local text `/private/tmp/CLD25.txt`.

- 2150944 bytes.
- SHA256 `021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e`.
- Printed page numbers below are the source's page numbers. Text line numbers refer only to these exact bytes.
- The current task inspected this text, not a newly rendered PDF. The frozen predecessor has its own PDF/source-QA record; that record is not a claim of PDF inspection in this task.

| Locator | Printed pages / exact text lines | Interface and audit finding |
| --- | --- | --- |
| §3.1.3; §3.3.1–3.3.4 | p.74, lines 3437–3454; pp.79–80, lines 3680–3710 | A parlinear map to an affine space is a G-tropical chart; products of charts are permitted. This justifies the bounded-star cross-fan diagnostic within the abstract category, not an analytic realization. |
| Definition 7.8.2, Remark 7.8.3 | p.190, lines 9509–9522 | Harmonic means locally real combinations of harmonic PL functions. An arbitrary continuous distributional kernel is not silently identified with this sheaf. |
| Lemma 8.5.1 | p.205, lines 10252 onward | Continuous multipliers and weakly converging positive currents; used with fixed T in the corrected corollary. Book's full proof read at Ch16:1189–1250. |
| Lemma 8.5.5 | pp.206–207, lines 10308–10320 | Ordinary continuous CPsh functions give positive closed one-factor products for any positive closed T. The proof uses sheaf/uniform closure, not a fixed ordinary smoothing theorem. |
| §8.6.1; Definition 8.6.2 | pp.207–208, lines 10345–10359 | Bedford–Taylor includes positivity and closedness and adds independence from psh potentials with the same curvature. |
| Example 8.6.4; Propositions 8.6.5, 8.6.6 | p.208, lines 10367–10385 | Integration is BT; smooth **positive closed** factors and weak limits preserve BT. None asserts arbitrary smooth multiplication preserves closedness. |
| Corollary 8.6.7 | p.208, lines 10387–10392 | Printed unrestricted positive continuous multiplier assertion; the proof's smooth-approximation step does not preserve closedness. No added “fT is closed” condition occurs in the literal statement. |
| Proposition 8.6.8 | pp.208–209, lines 10394–10404 | One-factor construction for ordinary CPsh preserves BT. This is a legitimate stability input, unlike arbitrary multiplication. |
| Proposition 8.7.2 | pp.209–210, lines 10427–10443 | Joint continuity with ordinary CPsh inner potentials. Correct interface for revised Ch16 harmonic-continuity proposition. |
| Proposition 8.7.3 | p.210, lines 10446–10466 | Broader harmonic-chart continuity proof explicitly uses Corollary 8.11.3 for positivity. It is not an independent justification of the missing hypothesis there. |
| Proposition 8.11.1 | pp.220–222, lines 10999–11130 | Explicitly skeletal **Bedford–Taylor** T; commutation with harmonically tropicalized G-forms. Read full proof and compared its normal-slope use. |
| Corollary 8.11.2 | p.222, lines 11132–11148 | Skeletal current locally a difference of BT currents; G-smooth harmonic factors. It is a **Corollary**, not a Proposition. |
| Corollary 8.11.3 | p.223, lines 11152–11161 | Prints arbitrary positive closed T and dpsh conclusion; invokes the preceding result without its hypotheses. Smooth convex target approximation alone does not justify the continuous dpsh conclusion. |
| Proposition 17.8.4 | pp.497–498, lines 25509–25534 | Separated boundaryless analytic X, strictly integral PL metric and nef residual bundle imply local psh. No algebraic-closedness hypothesis on K is imposed. Raynaud formal metrics meet the strict hypothesis. |
| Corollary 18.8.8 | p.541, lines 27970–27978 | Boundaryless analytic X and integral PL metric: local psh, positive current and residual nefness equivalent. The source proves this using 18.8.4 and 17.8.4. |
| Corollary 18.8.9 | pp.541–542, lines 27980–28033 | Nontrivial K; boundaryless analytic X; strictly PL harmonic coordinates. Correct published convex-pullback result for Ch19. General arbitrary-triangulation interpolation step in (c) is not used in the repaired book argument. |
| Proposition 19.3.1 and proof | pp.557–558, lines 28795–28876 | Nontrivially valued abeloid/canonical positivity; proof explicitly cites 18.8.8 for formal part and 18.8.9 for convex tropical part. Exact source direction agrees with the repaired Ch19 proof. |

Line windows are intended to locate whole passages; source objects, rather than a line alone, identify the exact interface. No full source is quoted into this dossier.

## Existing manuscript proof dependencies

All full paths, byte sizes and hashes are in `INPUT_HASHES.json`. Ch16/19 before and after hashes are also in `AUDIT_REPORT.md`.

1. Ch15 `prop:ch15-psh-cone`, lines 1875 onward: ordinary psh is a cone containing constants. The sum argument and signs were checked. `prop:ch15-uniform-limit`, lines 2444 onward: local uniform closure. Its use in the repair is on a fixed neighbourhood.
2. Ch16 `cor:ch16-max-psh`, lines 1006 onward: finite maxima of ordinary continuous psh functions are continuous psh. `lem:continuous-times-positive-current`, lines 1189 onward: read both proofs. `lem:ch16-cpsh-induction`: its warning explicitly says sheaf closure is not a fixed-neighbourhood ordinary smoothing theorem.
3. Ch16 `thm:cld-bt-continuity`: read its statement and induction. The positivity of the intermediate currents uses ordinary CPsh inner factors. The root now retains exactly this hypothesis.
4. Ch16 `thm:bt-harmonic-compatibility`, revised lines 3735 onward: explicit skeletal BT condition and locally-difference variant. This audit checks the hypothesis transfer and the fixed-T application; it does not recertify every upstream source-skeletal theorem.
5. Ch16 `ex:ch16-cross-fan`, revised lines 3996 onward: existing explicit unit and weighted slope computations. It supplies the old abstract-corollary diagnostic without new analytic claims.
6. Ch17 `thm:ch17-psh-residual-nef`, lines 1688–1740: full statement and proof read. The actual Raynaud inputs are strictly integral PL, separated and boundaryless, so the cited primary analytic theorem has its stated hypotheses.
7. Ch18 `thm:gk-formal-positivity-comparison`, lines 2884 onward: algebraically closed complete nontrivially valued K is explicit. Its full statement, proof and hypothesis remark were read to diagnose the old Ch19 mismatch. That theorem need not be changed for this repair.
8. Ch19 Raynaud construction, `thm:abelian-harmonic-tropicalization`, `prop:ch19-tau-coordinates`, metric decomposition and canonical-positivity proof: checked the actual integral PL/formal source of the coordinates and the full affine part of the weight. No G-smooth-to-ordinary-smooth implication is used by the replacement.

## Reference coverage versus proof coverage

The complete active literal TeX inclusion closure and all nine selected-label occurrences are archived in `ACTIVE_REFERENCE_INVENTORY.json`. All actually included editorial inputs were searched. The scan is complete for literal commands in this book, with the recorded parameterized include-macro body excluded. It does not execute arbitrary TeX or claim a build pass. Downstream theorem proofs outside the stated audit targets are not all freshly audited merely because their reference sites were enumerated.

## Provenance and source caution

The predecessor `p213_common_constant_cohomology_source_diagnosis_20260901` was authored by this auditor. Its source warnings were background for this task, not an independent proof dependency. The additional analytic source route 18.8.9 is now explicitly recorded here without modifying that frozen predecessor.

The revised book's two-sided-coordinate argument is an application of the already published formal-positivity equivalence and the book's elementary cone/max/uniform closure facts. It is not a newly promoted theorem about all harmonic functions or arbitrary positive closed currents.
