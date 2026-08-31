# Eight frozen dossiers: durable byte preservation

This sibling records only mechanical copying and validation. It changes no mathematical, audit, production, or runtime status. No live book file, frozen source dossier, Git index or commit, or production endpoint is modified.

The eight exact source/destination directory pairs and original source bases are in ORIGIN_MAP.json. All ordinary files OWNED by each selected source directory are copied, including its own tmp/pdfs PNG evidence. No external CLD PDF/text or unselected dependency tree is copied. Directory symlinks, special files, unexpected existing target files, and differing existing target bytes are rejected. Identical existing target bytes can be retained; no target is overwritten.

The authored scripts were created through apply_patch. preserve.mjs performs only the expressly requested bulk byte-copy operation and mechanically generates its checksum records and binary NUL path table. Use its plan mode before copy. The copy mode is one-shot: it refuses an existing preservation output rather than replacing frozen records.

Commands from this directory:

    node preserve.mjs plan
    node preserve.mjs copy
    node verify_relocated.mjs

The last command is read-only. It validates every archived owned byte, complete directory membership, all original own manifest entries and checksum lines, and direct file/source pins serialized in the archived JSON metadata. It resolves each original frozen relative path against the ORIGINAL container directory, not the new archive directory. For example, ../../../../../CLD25.pdf is recorded as /private/tmp/CLD25.pdf, not naively interpreted under the durable checkout.

A dependency originally inside the scratch worktree can use an already existing durable mirror only when its exact hash and optional byte count match. Otherwise the explicit original absolute dependency remains required. Source-based historical Chapter 14 context pins are validated against their exact named Git blob or the explicitly recorded unique substitution of the frozen first candidate into that blob. Both resulting byte counts and hashes must match. They are not silently compared with a later live revision or rewritten. EXTERNAL_REFERENCES.json records each external pin occurrence, original base, raw spelling, original absolute resolution, durable candidate, chosen validation method, and checked hashes.

COPIED_FILES.json lists EVERY archived owned path and SHA-256. PRESERVATION_RECORD.json gives counts and exclusions. COMMIT_PATHS.nul is a sorted, unique, repository-relative NUL-terminated list containing only the eight archived directories' own files and this preservation sibling's own files. It is a handoff list, not permission to stage or commit. This task invokes no staging or committing command.

The new MANIFEST.json and SHA256SUMS cover all archived owned files plus the preservation records/scripts. The copied frozen manifests and original checkers are byte-identical to their sources. Original embedded checkers are NOT claimed to be directly relocatable: some intentionally embed scratch absolute paths or historical live-file context. The wrapper verifies direct archived identities without pretending that it reruns a complete original mathematical audit or recursively validates every unselected dependency graph.

Original primary sources outside the checkout remain external prerequisites. The archive is durable for the selected owned artifacts; it is not a self-contained distribution of the literature PDFs or of the entire historical dependency tree. Root separately handles runtime/request/receipt preservation and final book/PDF build reports; none are included here unless already owned by one of the expressly selected frozen dossier directories.
