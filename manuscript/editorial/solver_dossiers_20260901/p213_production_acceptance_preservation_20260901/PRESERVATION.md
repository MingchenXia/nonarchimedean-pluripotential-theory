# Byte-preserving acceptance-audit archival wrapper

Date: 1 September 2026. Prepared by /root/p213_general_propagation_fresh_audit under the parent's explicit preservation request. This wrapper is new; no frozen report, pin, checksum, source or production memory record was edited. No stage, commit, live-book edit, service/configuration write or production rerun was performed.

## Preserved objects

MAP.json lists each original absolute path, durable mapped path, repository-relative path, byte count and SHA256. Exactly 22 files were copied:

- The five files of p213_component_curvature_production_acceptance_audit_20260901, unchanged.
- The five files of p213_cpsh_weighted_polar_production_acceptance_audit_20260901, unchanged.
- The six files with role=memory in each acceptance audit's REVIEWED_INPUTS.json, for run 20260831T203725Z_6a6a732dcebd and run 20260831T204323Z_180a3827dff7 only.

The selected memory consists of meta.json, statement_checks.jsonl, reference_checks.jsonl, failed_checks.jsonl, events.jsonl and verification_reports.jsonl for each run. These copies are inside this wrapper's memory/<run-id>/ directories. No other run's memory, source PDF, service implementation or configuration is copied by this wrapper. The production request/log/result artifacts were handled separately by the parent and are not silently added to this preservation scope.

All 22 originals and copies were compared byte for byte before freezing this wrapper. Its checker independently verifies the preserved copy hashes and, when original paths remain available, verifies those originals as well. The frozen acceptance report identities remain:

| Report | SHA256 |
|---|---|
| Component-curvature acceptance AUDIT.md | b47a438419595d08a632887faba20682cadf273f806bfbd083ccbef3be8f797c |
| Full-CPsh weighted/polar acceptance AUDIT.md | 7689fb34536208a72b0f7a3d6deb13ef319cf57d1a2660f2e260eeb8b130a0d5 |

## Status preservation

Both audits say byte binding and mathematical/reference coverage PASS, but execution compliance EXCEPTION and clean_production_gate_accepted=false. The recorded MCP approval refusal followed by direct local helper execution is not normalized as a mere availability fallback. Archival does not grant permission retroactively or turn these runs into clean production acceptance. The per-run mathematical scopes remain different and are not merged.

No claim is made that the live book is fully corrected, that a journal has accepted the results, that novelty was verified, or that all upstream source identities are valid. The original acceptance reports contain the substantive limits and source cautions.

## Relocation and verification boundary

The two frozen acceptance directories are byte-preserved, including their original absolute pointers. Their original verify.mjs programs are therefore **not fully relocatable or self-contained**: many input pins still refer to temporary research packets, original production paths and the existing runtime checker/service sources. Those programs may work on the originating machine while its originals remain, but this archive does not promise that they run after removal of those original paths.

This wrapper does not rewrite those pins or impersonate a new production run. Its own read-only verifier is intentionally narrower: it resolves the mapped files by repository-relative paths, checks all 22 preserved hashes, checks each frozen directory's four internal checksums and both retained compliance flags, checks the selected memory files against their original role=memory pins, checks its own five checksums, and validates the exact NUL commit list. It does not rerun the original production checkers, import production MCP helpers or contact the service.

If original files have disappeared, the wrapper reports that fact while still validating the archived identities. If an original remains but differs from the pinned identity, it reports a failure rather than silently redefining history. Relative resolution permits a relocated repository to validate this preservation layer; MAP.json still records the actual historical mapped absolute destinations.

## Exact commit selection

COMMIT_PATHS.json contains exactly 28 sorted repository-relative file paths: the 22 preserved objects and this wrapper's six files. COMMIT_PATHS.nul is the byte-exact UTF-8 NUL-separated, NUL-terminated form of that list. It was generated mechanically from the JSON list, with exclusive creation. It includes no directory-wide wildcard, source PDF, service/configuration path or unrelated file.

The list is a handoff for the parent, not evidence that anything was staged or committed. SHA256SUMS covers PRESERVATION.md, MAP.json, verify.mjs, COMMIT_PATHS.json and COMMIT_PATHS.nul; the checksum file is included in the commit selection but does not circularly hash itself.

Final disposition: immutable copies plus a separately frozen preservation map and read-only checker; original mathematical and execution-compliance conclusions unchanged.

