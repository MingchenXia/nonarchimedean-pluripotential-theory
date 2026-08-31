# Isolated Part III consumer patch proposal

No live file was edited by this subagent. The six live files were read into an exact frozen baseline; every edited chapter below is an isolated snapshot. Root owns integration and final approval. This packet does not claim the envelope conjecture over arbitrary nontrivially valued fields in arbitrary dimension.

## Three different gates

1. **01_source_scope.patch** is the source-supported narrowing/removal patch. It can be reviewed independently of the new real-class theorem. It replaces the old generic-nef Ch23 statement with the published ample-line-bundle metric theorem (GJKM Theorem 1.1), preserves its label, distinguishes Q-model functions from the unchanged real-model/full-PSH definitions, removes unsupported scope language, and corrects the finite-normal attribution. It changes six chapters. Its initial applicability check passed. This is the patch already sent to root for possible integration today.
2. **02_pending_envelope.patch** applies after stage 1. It integrates the exact mathematical content of the independently audited revised1 real-class candidate, with a documented label-only mapping, into Ch23 and uses it in the Ch29 envelope half. It retains positive-degree **real** model forms; it does not reduce them to one integral line bundle. Degree zero requires an actual Q-model competitor. Production approval of the exact envelope candidate remains a gate controlled by root.
3. **03_accepted_positive_solution.patch is DRAFT ONLY, not ready for application under the full current field generality.** It provides the requested proposed Green-potential proof for Ch29/31, using the accepted positive-degree Ch17 comparison downstream. It avoids rational-mass-implies-rational-slope and never calls the final nonatomic Green potential lisse. However, preparing the exact diff exposed residue-degree edge weights omitted by the older Ch31 unweighted graph conventions, and a common semistable reference-model issue for the arbitrary-field Ch29 paragraph. Those interfaces must be audited before applying this stage. The accepted Ch17 approximation theorem does not by itself settle them. No arbitrary-field weighted Green proof is claimed here.

**ALL_PROPOSED_CHANGES.patch is also draft-only**, because it includes stage 3. Do not apply it as a completed mathematical repair.

Stage 1 alone is not the complete Part III repair: the old detailed Ch29 envelope proof and old Ch29/31 graph approximation arguments remain until their separately gated replacements are integrated. In particular, some old Theorem 3.1 references inside the unmodified Ch29 proof remain after stage 1. This is intentional staging, not an endorsement of those arguments.

## Files and reproducibility

- `baseline/`: byte-identical copies of the six source chapters from the recorded hash snapshot.
- `01_source_scope/`, `02_pending_envelope/`, `03_accepted_positive_solution/`: cumulative **isolated** chapter snapshots.
- `build_proposals.mjs`: authored, guarded mechanical generator; it writes only within this isolated dossier. On subsequent runs it reads the frozen baseline, not newly edited live chapters. It checks all six baseline hashes and the two frozen envelope-candidate hashes before generating diffs.
- `EDIT_LEDGER.json`: exact named edit operations grouped by gate.
- `REVIEW_CHECKLIST.md`: mathematical/source gates, old labels, remaining exclusions.
- `VALIDATION.json` and `MANIFEST.json`: mechanical checks and exact file hashes.

The stage-2 envelope source is the sibling dossier
`p081_part3_curve_envelope_scope_repair_candidate_20260831/revised1`.
Its statement SHA-256 is `944fc4672a83bf038b068af1a70da1563b4950752ee1eb5ae89ee2f4b2db0b30`;
proof SHA-256 is `bd98ca99d636a1f40872412e2ababc7f44a5ccb5416b31bcbd83b957515031d6`.
The only integration transformations are
`thm:isolated-real-class-curve-model-envelope` to `thm:ch23-gjkm-curves`
and the equation-label prefix `eq:isolated-` to `eq:ch23-curve-`.
The proof itself is not shortened or replaced by a citation to its own conclusion.

No full-book compile or production submission is claimed. `git apply --check` is a read-only applicability check, not a mathematical or typesetting verdict.
