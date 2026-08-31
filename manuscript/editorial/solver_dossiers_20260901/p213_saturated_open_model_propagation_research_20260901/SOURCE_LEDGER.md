# Exact source and dependency ledger

Date: 1 September 2026. Author: /root/p082_independent_reaudit.
This ledger accompanies the bounded saturation/model-augmentation note, not a production theorem.

## Primary sources actually inspected

| Source and version | Exact locations checked | Use and excluded inference |
|---|---|---|
| Boucksom--Favre--Jonsson, Singular semipositive metrics in non-Archimedean geometry, arXiv:1201.0187v2, 21 January 2014; local PDF and text below | Section 1.1, Definition 1.1, Section 2.4, Definition 2.1, Proposition 2.2, Corollary 2.3; Theorem 3.1, Definition 3.4, Lemma 3.5(ii), Proposition 3.6(iii); Section 3.3; Proposition 3.12(ii), Corollary 3.13 | Complete DVR, residue characteristic zero, smooth connected PROJECTIVE scope. Rational model-function density and common SNC models. The exact equality for a DETERMINED divisor, as opposed to the separate ideal-function inequality, is the essential support argument. Section 3.3 gives the actual local monomial construction. |
| Berkovich, Smooth p-adic analytic spaces are locally contractible, Inventiones Mathematicae 137 (1999), 1--84, DOI 10.1007/s002229900914; official author PDF | Introduction, definition of local contractibility p.1; Section 9 opening and Theorem 9.1 p.74 | Nontrivially valued complete field and strict analytic spaces locally embeddable in smooth spaces. Gives the path P in an ordinary connected W. Does not authorize pulling a current through the alterations in the theorem's proof. |
| Stacks, Section 33.47, tag 0FD4, Situation 33.47.2 and Lemma 33.47.3 | Full source statements and the smooth-hyperplane argument | A basepoint-free system inducing an immersion has a nonempty open of smooth cuts over the ORIGINAL field. Finite simultaneous conditions are imposed in a k-parameter space; characteristic zero makes k infinite. |
| Stacks, Lemma 33.48.3, tag 0FD9 | Full statement and proof | A regular ample section of a connected proper scheme with depth at least two at closed points has connected zero locus. Used on smooth successive intersections. No geometric connectedness or k-rational closed points assumed. |
| Stacks, Section 31.33, tag 01OF | Lemmas 31.33.2, .4, .5, .7, .9, .13 | Actual Rees charts, identity outside the center, identity of the blowup of a Cartier divisor, integrality and projectivity. Regularity/SNC of the particular charts is computed in the note, not inferred just from properness. |
| Stacks, Section 41.21, tag 0CBN | Definition 41.21.1 and Lemma 41.21.2 | SNC support means regular coordinate divisors and regular proper intersections. Actual connected components are retained in all incidence statements. |

Primary links: [BFJ arXiv version](https://arxiv.org/abs/1201.0187v2), [Berkovich author PDF](https://www.wisdom.weizmann.ac.il/~/vova/Inven_1999_137_contra.pdf), [Stacks Bertini](https://stacks.math.columbia.edu/tag/0FD4), [Stacks connected ample section](https://stacks.math.columbia.edu/tag/0FD9), [Stacks blowups](https://stacks.math.columbia.edu/tag/01OF), [Stacks SNC support](https://stacks.math.columbia.edu/tag/0CBN).

The Stacks and Berkovich primary pages were read on 2026-09-01. Berkovich was read through the tool's primary-PDF text extraction; no new PDF visual comparison is claimed. No local byte hash is invented for that web PDF.

## Local primary-source pins

- BFJ PDF: /private/tmp/BFJ_singular_1201.0187_audit_20260831.pdf; 768011 bytes; SHA-256 8b684713055b9147de0d3379ad925c58f031bafe10a77e769a2791cdaa128270.
- BFJ extracted text: /private/tmp/BFJ_singular_1201.0187_audit_20260831.txt; 175006 bytes; SHA-256 df3fa71656240742234907514956389d2f2533e20bb89cd877bd235a922e5f1f.
- The read text ranges include lines 235--290, 390--625 and 625--724. These ranges cover the field and projective scope, density, equality, domination, local monomial construction and the contrasting inequality.

BFJ's stronger irreducible-intersections convention is not silently imposed on the immediate ample-cut models. The source's Section 1.1 allows further connected-stratum blowups; the note gives the local toroidal subdivision formula. BFJ Theorem 3.15 is NOT used as if it automatically produced a regular model.

## Frozen research interfaces and precise roles

INPUT_PINS.json records exact principal bytes. All the following were rehashed during this turn.

- Source-cell access v2: ../p213_source_cell_residual_curve_access_v2_20260901/RESEARCH_NOTE.md; SHA-256 177d7ea0e2f5fd1cde5e9539b4cd88ce90623a1ee78202f9050b08cb00130d96. Its manifest is c912270c7f14e791bea153775c628fb3f75d02b53dce327c91e92f04d738afb6. The entire note was read. It supplies a bounded endpoint-comparison template under its hypotheses. It may alter the generic variety birationally and is NOT identified with the same-generic-X model system of BFJ without further work.
- L: ../../solver_dossiers_20260831/p213_nonreduced_tube_finite_projection_research_20260831/RESEARCH_NOTE.md; SHA-256 3001c94985c0d3e60f184ffd9f0e9591775ea026a98cd20ee538005edac11b7a. Conditional only in the current interface: entire finite proper coordinate tube, positive omitted multiplicity, canonical degree including residue degree.
- O: ../../solver_dossiers_20260831/p213_ordinary_open_outer_collar_research_20260831/RESEARCH_NOTE.md; SHA-256 f629a77106d023763c7b99626c1ec1f8f449164f3749de475bf18bb0661e1d5b. Author's earlier work, separately audited historically. Here it is an explicit conditional input for ordinary-W compact primitives and the principal-divisor relation. The new note does not re-audit or self-certify it.
- Q: ../p213_proper_target_open_comparison_20260901/RESEARCH_NOTE.md; SHA-256 35d4ae59a167025ef595aa50a45101619ed1aef586be39abebca1486c62857ec. Conditional only in the current interface: full inverse image of a connected target-open subset, and source-multiplier comparison under displayed R.
- Displayed R: ../../solver_dossiers_20260831/p213_skeletal_packets_20260831/skeletal_representation/statement.tex; SHA-256 5c06cd6f091e5964a16c07b3efddd2104fed938447605f4f9b19ff8dfea01f1a. Only its displayed source-cell formula is assumed where stated. No acceptance of its full proof or a local-affine-separation theorem is asserted.

No L/O/Q/R premise is used in the saturation proof, ample-section existence, Rees chart calculation or finite old-incidence preservation.

## Authorship and companion boundary

Root proposed the global propagation investigation and highlighted the full-saturation issue. This author developed the saturation proof and actual model-star implementation, including the old-curve preservation and copied exceptional values. The author previously wrote O and related capture diagnostics; those are disclosed inputs, not independently re-proved facts here.

The companion author /root/p213_skeletal_hostile separately develops the ample-boundary incidence graph and positive-vertex finite-polyhedral assembly. The shared geometric interfaces were exchanged for consistency. This note is NOT labeled an independent audit of that companion, and no mutable companion file is imported into its manifest. A later exact-byte assembly/review must pin both packages.

The methods used here are elementary applications of BFJ model approximation, Berkovich topology, ample sections and coordinate blowups. No priority or novelty claim is made. Production and whole-current rigidity remain outside the packet.
