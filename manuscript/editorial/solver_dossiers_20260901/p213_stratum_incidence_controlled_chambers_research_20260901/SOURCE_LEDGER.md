# Source and conditional-interface ledger

Date: 2026-09-01. Author: /root/p213_skeletal_hostile.
This is authored research documentation, not an independent audit or production acceptance.

## 1. Primary sources actually checked

The Stacks primary pages below were read on 1 September 2026. No hash is invented for an online page. The BFJ source was read as the pinned local extracted text; its PDF is hashed for provenance only, and no new PDF rendering or visual comparison is claimed.

| Primary source | Exact source statement used | Role and limits |
|---|---|---|
| [Stacks Section 33.47, tag 0FD4](https://stacks.math.columbia.edu/tag/0FD4), Situation 33.47.2 and Lemma 33.47.3 | For a smooth scheme and a basepoint-free system giving an immersion, smooth hyperplane sections occur on a nonempty parameter open. | Section 3 uses finitely many such opens for actual smooth closed strata over the original infinite perfect field. Avoidance of finite closed points is an additional elementary open condition. No geometric irreducibility or rationality of intersection points is claimed. |
| [Stacks Lemma 33.48.3, tag 0FD9](https://stacks.math.columbia.edu/tag/0FD9) | A regular section of an ample invertible sheaf on a connected proper scheme, with depth at least two at closed points, has connected zero scheme. | Section 2 applies it successively to REGULAR complete intersections of dimension at least two. The arbitrary-field graph lemma does not equate regular with smooth over an imperfect field. |
| [Stacks Section 33.44, tag 0AYQ](https://stacks.math.columbia.edu/tag/0AYQ), Definition 33.44.1 and Lemmas 33.44.9, 33.44.12, 33.44.14 | Degree is computed over the base field; a nonzero regular section represents an effective divisor of its degree, and ampleness on a proper curve is equivalent to positive degree. | These statements supply a nonempty finite zero set on each descent curve. Closed points can have any finite residue degree. No point is replaced by a rational or geometric point. |
| [Stacks Section 10.160, tag 0323](https://stacks.math.columbia.edu/tag/0323), Theorem 10.160.8 and Lemma 10.160.10 | Coefficient rings for complete local rings; a complete regular local ring with a chosen residue coefficient field is a formal power-series ring in a regular parameter system. | Section 9 uses the characteristic-zero coefficient field and the actual component generators. The special-fibre equation is a genuine unit times the component powers. No root of the unit is extracted. |
| [Stacks Section 10.153, tag 04GE](https://stacks.math.columbia.edu/tag/04GE), Definition 10.153.1 and Lemmas 10.153.7, 10.153.9 | Simple residual roots lift uniquely in a Henselian ring; complete local rings are Henselian; finite étale extensions lift across the residue map. | The finite separable residue extension at a closed point is embedded compatibly in the completed local ring. Its coefficient DVR is unramified. This is a description of the given tube as a K-analytic space, not scalar pullback of T. |
| [BFJ arXiv:1201.0187v2](https://arxiv.org/abs/1201.0187v2), Section 1.1, Definition 1.1; Section 2.4; Lemma 3.5(ii), Proposition 3.6(iii); Theorem 3.15 | Complete DVR with residue characteristic zero, connected projective generic variety; a determined vertical real divisor's model function is fixed by retraction. Higher SNC models fix old skeletal points. The subdivision theorem produces a normal vertically Q-factorial model. | These source checks fix conventions and prevent two invalid shortcuts: general ideal inequalities cannot replace equality for a determined function, and Theorem 3.15 alone does not imply regularity of a subdivision model. The companion, not this note, supplies actual saturation and global blowups. |

The local BFJ spans checked were text lines 245–286 (printed pp.6–7), 400–455 (pp.9–10), 583–613 (p.13), and 764–800 (pp.16–17). The source explicitly permits non-algebraically-closed residue fields. Its extra irreducible-intersections convention is separate from SNC support and from actual connected-stratum indexing.

Local source pins:

- /private/tmp/BFJ_singular_1201.0187_audit_20260831.txt: 175006 bytes, SHA256 df3fa71656240742234907514956389d2f2533e20bb89cd877bd235a922e5f1f.
- /private/tmp/BFJ_singular_1201.0187_audit_20260831.pdf: 768011 bytes, SHA256 8b684713055b9147de0d3379ad925c58f031bafe10a77e769a2791cdaa128270.

No graph-connectivity assertion is attributed to BFJ or Stacks: the old-boundary-count argument, positive-vertex normalization and rooted finite assembly are written and proved in this note.

## 2. Frozen companion implementing the model interface

The sibling file

    ../p213_saturated_open_model_propagation_research_20260901/RESEARCH_NOTE.md

is authored by /root/p082_independent_reaudit and is now frozen at SHA256 a77fe9f80d2da71d1c9c81163955808736b38508f49da76f0cf8ad8d81fdbefc. Its source ledger is d0ea96a28f565e4c8f3089d10195ef85a1850fe6151966cdeec294979f05038d; its manifest is 0b3abe46b75019f87f2e8a7206ccd6b98f729ff9c59caacdc9bfac4665f4be91; its checksums file is a4c098c28a90097c8d4ad3c18afa5549b35826aaa4a67d52c46e4f925cdadc49.

The complete readable draft and the frozen source ledger were inspected for interface compatibility, not independently certified here. The exact mapping is:

- Its Sections 2–3: a rational model function and a common same-generic-X SNC model give a saturated ordinary V with closure inside W.
- Its Sections 5–8: original-field global horizontal cuts, both actual Rees charts, regularity/SNC, whole strict E and proper-curve/zero-point preservation supply (A1) and (A2).
- Its Sections 9.1–9.2: every new top chamber contains the pivot E and exceptional vertices copy g(E), supplying (A3).
- Its Section 9.3: an old edge has an actual top bridge containing its two endpoints after augmentation; if both endpoint values are positive, the whole closed bridge chamber is positive.
- Its Section 10: actual connected-stratum blowups and coordinate subdivisions supply the separate geometric hypothesis under which this note's Section 8 preserves a chain.

The companion's actual model theorem is stated for n>=2. This note's graph and CONDITIONAL model-interface arguments allow n=1, but no n=1 instance is silently imported from that companion. All combined current consequences here are explicitly n>=2.

The interface is not circular: (A1)–(A3) contain no claim that a star's top-chamber graph is connected. The companion's actual model construction does not invoke the graph lemma to prove regularity, existence or preservation. Our Sections 2 and 6 supply connectivity once that independently checkable model geometry is available.

## 3. L/O/Q/displayed-R are conditional research inputs

All exact paths, bytes and hashes are in INPUT_PINS.json. Its records also pin the source manifests and checksum files, so drift can be detected. Historical independent audit status does not turn any of these premises into production acceptance in this packet.

- L: ../../solver_dossiers_20260831/p213_nonreduced_tube_finite_projection_research_20260831/RESEARCH_NOTE.md, SHA256 3001c94985c0d3e60f184ffd9f0e9591775ea026a98cd20ee538005edac11b7a. Used for finite projection of the specified analytic hypersurface, properness, connected target comparison, and canonical omitted-multiplicity times coefficient-field degree. L by itself does NOT identify a general model tube with that hypersurface.
- O: ../../solver_dossiers_20260831/p213_ordinary_open_outer_collar_research_20260831/RESEARCH_NOTE.md, SHA256 f629a77106d023763c7b99626c1ec1f8f449164f3749de475bf18bb0661e1d5b. Its Section 2 supplies actual-model/formal-tube identification, conditional on its stated earlier geometric sources. Its ordinary-W theorem supplies all-source shallow collars, compact principal-divisor tests and lambda(p)=c[κ(p):k] on a WHOLE proper curve. The source assumes n>=2 and positive selected vertical multiplicities. We do not apply a whole-tube current theorem to T defined only on W.
- Q: ../p213_proper_target_open_comparison_20260901/RESEARCH_NOTE.md, SHA256 35d4ae59a167025ef595aa50a45101619ed1aef586be39abebca1486c62857ec. Used on the full inverse image of an arbitrary connected ordinary target-open set. The identical compact form, not just its tropical support, compares Q and O.
- Displayed R: ../../solver_dossiers_20260831/p213_skeletal_packets_20260831/skeletal_representation/statement.tex, SHA256 5c06cd6f091e5964a16c07b3efddd2104fed938447605f4f9b19ff8dfea01f1a. ONLY eq:p213-source-cell-formula is assumed on actual coordinate domains and with its compact source multipliers. The companion proof file is pinned solely for provenance. No stronger chart separation or compatibility theorem is assumed without statement.

The author wrote earlier product/normal-bundle/wall and point-retaining packets and audited some of these inputs historically. That history is disclosed, not presented as fresh independent verification here. No earlier authored proof is self-certified by this ledger.

## 4. Explicit exclusions and pre-freeze clarifications

The source-cell access packet that may replace X by a proper generic modification Y is not an input of this note. A common model in the same-generic-X projective BFJ system is required wherever saturation is used. Root is separately developing a new original-projective-X anchoring argument; it is NOT imported here.

The pre-freeze text was clarified as follows, before any final candidate hash was issued:

1. At the fresh reviewer's request, Section 9 now states n>=2, matching O, while pure graph results retain n>=1.
2. The author expanded the completed-ring presentation into a coefficient-field/Hensel/actual-parameter argument.
3. The author distinguished regular from smooth over imperfect k in the arbitrary-field graph lemma; the proof uses only regularity, and the actual model scope is characteristic zero.
4. At the fresh reviewer's request, whole model-tube identification is attributed to O Section 2/model geometry, while L is attributed only its analytic finite-projection conclusions.

These are recorded transparently. The reviewer did not author a replacement proof or develop the graph argument. Final independent scrutiny is still required on the frozen bytes.

No full P21.3 conclusion, arbitrary-moment anchor, general non-projective field/space extension, production submission, PDF compilation, live edit or git operation is part of this packet.
