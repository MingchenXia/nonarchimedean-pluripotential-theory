# P14.8 smoke-infrastructure repaired source stage: independent hostile audit

Date: 2026-09-01

## Binary verdict

`FAIL_NOT_READY_FOR_FINAL_PATH_SMOKE`.

No final path may be installed from this candidate.  No smoke, production
submission, live-book integration, inventory retirement, or git operation was
performed by this audit.

## What remained correct

The byte boundary is otherwise exact.  The authored top manifest has SHA-256
`bea75f18d2b5f765d07439c19189fa203b7a7f772a7dff9cd09c1d1d65721a30`;
the 44-row release-stage manifest has SHA-256
`4c2a6c9d61966aeac3f0c5c27284a0746d1a8bcc4520340016247947f9c9accc`.
The old and new release inventories are equal.  Exactly the declared five
substantive paths changed and the other 39 rows are byte-identical.  All 31
fixed sources, release pins, service, MCP, schemas, catalog,
canonical-reference code, and smoke MCP are unchanged.  The statement and
proof remain respectively
`9cd8fe1533c99d9d2de9e351610da4b7843d156a523d97344032cf75e3953715`
and
`adb2cac53f227dad668b30e054e278af0f0ac2644a597879fdb99e569dabbfd9`.

The four executable repairs are substantively sound under static hostile
inspection.  Stdout and stderr are split; stdout is strict JSONL; stderr uses
anchored full-line matching for only the observed state-database and
shell-snapshot cleanup warnings; the optional-stdin banner is not allowlisted;
a real PTY slave is supplied as stdin; the process is polled before and after
the bounded `ps` scan; and the terminal cache-horizon bridge still requires a
fully bound pre-horizon live sample and transcript-bound MCP completion before
the terminal observation.  Twenty-eight additional independent mutations of
the stream, warning, identity, role, cadence, and horizon evidence were all
rejected.  The exact failed final-smoke artifacts replay under the repaired
validators after only the declared mechanical stream separation, banner
omission, path rebinding, and observation-state additions.

None of those positive facts overrides the binary failure below.

## Blocking defect 1: the authored tree was not read-only

At the start of this audit all seven directories were mode `0755` and all 67
regular files were mode `0644`.  Thus the candidate described as
"frozen/read-only" allowed creation and deletion of entries in its child
directories as well as direct modification of every regular file.  The earlier
158-test passes were consequently passes on a writable source tree, not on the
claimed frozen boundary.

Root subsequently applied only the missing directory metadata freeze, changing
all seven directories to `0555` without changing a single byte or manifest
hash.  All 67 files remain `0644`.  The present audit checker pins that exact
post-freeze state so that this failure cannot be hidden by a later mode change.

## Blocking defect 2: the test harness fails on a genuinely read-only tree

Once the directories were correctly `0555`, the complete correct-venv suite
failed reproducibly with exactly six `PermissionError` errors:

1. `test_extra_source_is_rejected_pre_start`;
2. `test_mcp_independently_rejects_mutated_source_before_server_start`;
3. `test_mcp_independently_rejects_mutated_static_catalog_before_server_start`;
4. `test_missing_source_is_rejected_pre_start`;
5. `test_static_catalog_mutation_and_missing_file_fail_closed_pre_start`;
6. `test_symlinked_source_is_rejected_pre_start`.

The common cause is precise.  These tests use `shutil.copytree` to create a
throwaway mutation candidate.  `copytree` preserves the source directory modes,
so a copy made from a `0555` source still has `0555` directories.  The test then
tries to add, rename, unlink, or create an artifact path inside that temporary
copy and fails before exercising the intended release-pin assertion.

Two direct independent post-freeze runs returned `FAILED (errors=6)` after
14.600 and 14.941 seconds.  Two further runs made by the frozen independent
checker returned the identical six-error inventory after 12.844 and 13.369
seconds.  The authored top checker also propagated the same failure on its
first internal pass.  By contrast, two pre-freeze independent runs passed in
17.723 and 16.555 seconds; those are retained only as evidence that writable
directory modes masked the harness defect and are not admissible release
evidence.

## Required sibling repair

Create a new sibling; do not alter or promote this failed candidate.

1. In the mutation-test helper, immediately after copying the release into a
   temporary directory, make only that throwaway copy writable: directories
   `0755` and regular files `0644`, without following symlinks.  All mutations
   must remain confined to that temporary copy.
2. Keep the audited source tree itself frozen: every directory `0555`, data
   file `0444`, and executable script `0555` only where execution permission is
   actually required.
3. Make the source-stage checker assert those modes, and ensure the final-path
   installation workflow creates its smoke-output location in a deliberately
   writable installation copy without relaxing the frozen source.
4. Re-run all 158 tests twice from the fully frozen source using the pinned
   verification Python.  Then obtain a new independent hostile audit before
   installing a final path or consuming the one-smoke budget.

The repair must not change the P14.8 statement, proof, fixed sources, pinset,
runtime service/MCP, catalog, schemas, warning allowlists, PTY strategy, or any
identity/role/cadence/TTL gate.
