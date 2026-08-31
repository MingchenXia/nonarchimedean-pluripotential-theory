# Source interface and provenance

Date: 31 August 2026. This ledger separates primary inputs, elementary geometry proved in the packet, and the explicitly assumed source representation.

## Primary CLD input

Chambert-Loir--Ducros, arXiv:1204.6277v2, dated 25 July 2025.

- Primary record: https://arxiv.org/abs/1204.6277v2
- Primary PDF: https://arxiv.org/pdf/1204.6277v2
- Local PDF: /private/tmp/CLD25.pdf
- PDF bytes: 4659053; SHA-256: 5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719
- Local text: /private/tmp/CLD25.txt
- Text bytes: 2150944; SHA-256: 021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e

Checked exact passages:

| Passage | Printed page | Use and restriction |
|---|---:|---|
| Section 7.1.11 | 159 | Pushforward requires topological properness, or properness on the current's support. The collar tropical maps in this packet have compact inverse images of compact target sets, proved directly. |
| Section 7.2.6 | 161 | Proper pushforward preserves positivity. The packet also verifies positivity of its scalar functional directly. |
| Proposition 7.2.8 and proof | 161--162 | Positive distributions and Radon measures; the local bound used in the packet is explicit. |
| Proposition 7.2.9 | 162 | Order-zero control from positivity. No general-current slicing theorem is inferred. |
| Proposition 14.4.2 | 409--410 | Finite-map pushforward of canonical calibrations with the calibrated degree. |
| Remark 14.4.3 | 410 | Viewing an \(F\)-analytic space as a \(K\)-analytic space multiplies its canonical calibration by \([F:K]\). This is the controlling original-field normalization here. |

Do not confuse the last assertion with CLD Proposition 14.3.6, which compares scalar extension using the new base field's normalization. In the present proof the \(K_p\)-polyannulus is itself viewed as a \(K\)-analytic source; its coefficient is \(d_p=[K_p:K]\), not one.

The standard torus calibration is one in primitive coordinates. The packet's finite extension is unramified, so \([K_p:K]=[\kappa(p):k]\) and the coordinate lattice is unchanged. Neither defect nor ramification is being suppressed by an arbitrary-field claim.

## Primary GRW comparison, not an arbitrary-current theorem

Gubler--Rabinoff--Werner, Skeletons and tropicalizations, arXiv:1404.7044v3, dated 28 February 2016.

- Primary record: https://arxiv.org/abs/1404.7044v3
- Primary PDF: https://arxiv.org/pdf/1404.7044v3
- Local PDF: /private/tmp/grw1404.7044v3_p213_residual.pdf
- PDF bytes: 679624; SHA-256: f7a909a8508032d8e2e0a0c6f9cd14b06f36cfa465c3e83fa5d40be6033678ad
- Local extracted text: /private/tmp/grw1404.7044v3_p213_residual.txt
- Text bytes: 219817; SHA-256: 851b1820299b758f96db87f37da1ce786b6d169597dc9bebb0f5e3208b1079af

Printed p. 1, Section 1.1 assumes the ground field algebraically closed, complete, and nontrivially valued. Printed p. 23, Theorem 6.9 is the slope formula for the rational function on the skeleton of a strictly semistable pair. The principal-divisor/intersection identity (6.10.2) in its proof is on printed p. 24.

Those passages support the geometric role of proper residual curves and principal-divisor degree zero. They do not construct a positive divisor functional from an arbitrary CLD current. They also do not directly apply to the nonsplit real-residue example over \(\mathbf R((\pi))\). No such application is claimed: the tube, lift, source cutoff, degree, and current test in this dossier are given explicitly.

The PDF's actual theorem locator is Theorem 6.9. Some generated HTML links display equation-style numbering in the corresponding heading; the PDF locator controls.

## Elementary geometry proved here rather than imported outside scope

The proof supplies:

- the completed-ring calculation \(R_p[[w_p]]\), using perfect residue field, henselian lifting, and smoothness;
- the actual open disc tube over \(K_p\), and compactness of closed polyannuli;
- lifting every \(f\in k(C_0)^\times\) through the generic special-fibre DVR;
- dominance of the first nonzero reduced coefficient on whole outer collars;
- finiteness of the bad residual points from the horizontal divisor of a rational lift on the proper model;
- an explicit global smooth source cutoff and cancellation of all its differential error terms.

No claim is made that an arbitrary quasi-smooth twofold or arbitrary semistable stratum has this product geometry.

## Prior research inputs: data and one conditional interpretation

The prior obstruction note is:
 /private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260831/p213_calibrated_chart_rigidity_research_20260831/OBSTRUCTION_NOTE.md

Bytes 15137; SHA-256 b27c56591db85bfef79e8e34b47637a06bd7df8f9d065b46b5303c64cfd61b86. Section 7 posed the missing interface; Section 6 contained the elementary divisor-functional implication used only after the analytic construction here.

The separate source representation remains an assumed research input, not certified by this packet:

- /private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260831/p213_skeletal_packets_20260831/skeletal_representation/statement.tex
  Bytes 2211; SHA-256 5c06cd6f091e5964a16c07b3efddd2104fed938447605f4f9b19ff8dfea01f1a
- /private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260831/p213_skeletal_packets_20260831/skeletal_representation/proof.tex
  Bytes 11486; SHA-256 27a344a15fa7d22b2e88c07837aacfca0c978758c5bae5871c5af2d30e47999a

Both files were read completely. The sole use is the final interpretation: on the one injective source Gauss plane of an actual product collar, the directly constructed \(b_T(p)\) equals the represented source coefficient. The current tests and principal-divisor relation are established without this input.

## Source inspection

The PDF skill was read and used for read-only inspection. CLD printed pages 159, 161, 162, 409, 410 and GRW printed pages 1, 23, 24 were rendered and inspected as whole pages. Temporary render directory:
 /private/tmp/p213_residual_source_visual.B9icjh

All those page renders completed and were legible. GRW rendering emitted a font-cache warning, but no failed render. No source PDF was edited or re-exported. No PDF output is authored by this packet.

