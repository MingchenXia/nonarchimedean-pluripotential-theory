# Internal validation and freeze boundary

Date: 2026-09-01. Author: /root/p213_skeletal_hostile.
Status: authored internal checks; not an independent mathematical verdict, production acceptance or P21.3 solution.

## Mathematical self-checks

1. The graph vertices and curves are actual connected closed intersections, never just subsets of a component-name list. All residue fields are retained. In Section 2, SNC gives regularity; perfectness is needed only for the later smooth Bertini/model realization.
2. At a zero-stratum exactly d boundary components meet. Removing one old component leaves a proper regular integral curve; an unused ample color has a nonzero restriction and positive degree. At a zero of that section the SNC component count excludes every additional component, so the old count decreases by exactly one.
3. Connectedness of the successive ample intersections is not inferred from geometric irreducibility. It follows from the exact depth hypothesis of Stacks 0FD9. The d=1 empty intersection is the whole proper curve.
4. The positive-vertex denominator is strictly positive on the strict superlevel. The normalized map and straight homotopy agree across faces, including parallel cells with the same vertex labels. No purity or codimension-one connectivity is assumed.
5. The finite assembly processes parents before children. A child's actual bridge chamber already exists when its augmented star is connected. Subsequent augmentations preserve the earlier complete proper-curve witnesses; no late bridge is silently added to an earlier star.
6. New chambers belong to the pivot star by the explicit (A3) model input. Every pivot in the chosen old graph component is positive, and new exceptional vertex values copy the pivot. Original chambers with only partially positive interiors are handled by the positive-vertex retraction, not by assuming every original vertex is positive.
7. Every used wall has a nonempty relative-open superlevel. Positive independent normal weights exist by avoiding countably many proper rational hyperplanes. The chosen monomial point is centered at the generic point of a whole proper residual curve.
8. Finite subdivision preservation uses a polygonal path inside each convex positive chamber part avoiding codimension-two faces; positive subdivided wall pieces join adjacent chamber chains. This argument is conditional on an actual regular SNC model subdivision and does not misstate BFJ 3.15.
9. The model calculation is on the ENTIRE closed-point tube. Characteristic zero supplies compatible coefficient fields, Hensel supplies the finite residue lift, and the chosen component equations remain the regular parameters. The formal relation is linear in pi; no unit root is taken.
10. Actual model-tube identification is an O Section 2/model-geometry input. L then gives the finite projection and canonical degree. These roles are not reversed. Section 9 is restricted to n>=2, exactly the frozen O range.
11. The maximal-chamber target is a convex ordinary open halfspace slice, and its entire inverse image lies in V. Q is applied to T there, not on a larger domain where T is undefined.
12. At a wall, the SAME actual local parameters and target support define the same compact source form in Q and O. O's principal-divisor functional is on the entire proper curve, with all closed-point residue degrees. The normalized coefficient is b_p/(N_0 d_p), and changing the omitted normal gives the factor N_j/N_0 in both current and canonical coefficients.
13. No arbitrary analytic moment is anchored by these graph arguments. No current is extended from W, pulled back by a residue/scalar extension, or declared scalar on all tests. The generic modification issue for older access packets and the new original-X anchor remain external.

## Exact-byte checks actually run before freeze

The read-only command is:

    /Users/mingchen/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node check_packet.mjs

It uses only filesystem reads and hashing. Its literal scope-marker checks are not a substitute for proof review.

The initial successful run after all mathematical clarifications verified:

- 17 pinned input/source records, zero mismatches.
- L: all 8 manifest records and 9 checksum lines, zero mismatches.
- O: all 13 manifest records and 14 checksum lines, zero mismatches.
- Q: all 8 manifest records and 9 checksum lines, zero mismatches.
- Model companion A: all 13 manifest records and 14 checksum lines, zero mismatches.
- 13 exact scope markers, all present.
- All four then-existing authored files had zero unwanted ASCII control characters. This validation file is included in the final repeat.

The finalized mathematical note at this stage is 29890 bytes, SHA256 30d3d66a465dd51e488fa7f4b440aa2d083fc1640bd331fa61a1472acab5df34. It includes all four transparent pre-freeze clarifications listed in SOURCE_LEDGER.md. No subsequent mathematical edit is planned after the manifest is issued.

The final MANIFEST.json pins these five authored files plus the 17 input/source files (22 entries). SHA256SUMS additionally pins the manifest (23 lines). The same checker verifies both once present. Its own-file and input checks are reproducible without writing any file or regenerating a candidate.

## Independence and provenance

Root proposed the broad route and the explicit barycentric normalization. The present author developed the old-boundary-count graph proof and rooted-order assembly and wrote their detailed conditional current interface. /root/p082_independent_reaudit separately authored the actual model construction; coordinating interfaces is not an independent audit of it.

The assigned fresh reviewer requested two source-interface clarifications before freeze: the n>=2 bound and attribution of model-tube identification. The author independently corrected regular-versus-smooth terminology over imperfect fields and expanded the completed-ring algebra. The reviewer did not author the graph proof or replacement mathematics.

A fresh exact-byte audit is still required. Historical passes of L/O/Q or earlier source packets are not promoted to production acceptance here. No live theorem, frozen predecessor, bibliography, chapter, or git object is modified. No production submission, PDF compile or visual verification is claimed.
