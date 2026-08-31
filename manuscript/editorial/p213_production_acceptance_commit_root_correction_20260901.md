# Commit-root correction for the production-acceptance archive

Date: 1 September 2026.

This note corrects only the interpretation of the frozen commit-selection
metadata in
`solver_dossiers_20260901/p213_production_acceptance_preservation_20260901`.
No file in that frozen archive is modified.

The archive's `MAP.json` declares
`/Users/mingchen/Projects/Yethlas` as `repository_root`, whereas the actual Git
top level is
`/Users/mingchen/Projects/Yethlas/nonarchimedean_pluripotential_theory`.
Consequently, the 28 paths in its `COMMIT_PATHS.json` and
`COMMIT_PATHS.nul` are relative to the declared parent directory, not to the
actual Git top level.  Passing them unchanged to `git add` would prepend the
book-directory name twice and select no intended file.

For the scoped archival commit, each frozen entry is therefore resolved
against the declared `repository_root`, required to be an existing ordinary
file, and then converted with `path.relative` against the actual Git top
level.  The conversion rejects an empty path, an absolute result, `..`, or a
result beginning with `../`; it also rejects duplicates.  All 28 entries pass.
The resulting paths begin with `manuscript/`, and the 22 preserved-object
paths agree exactly with the `mapped_path` entries in `MAP.json`.  The other
six paths are the wrapper's own preservation and selection metadata.

The frozen inputs used for this correction have the following SHA256
identities:

- `MAP.json`:
  `eb275bdd1bf6c9d06e9611dce2bce5587d470d33222a975b9f4a116a62a3b4d2`;
- `COMMIT_PATHS.json`:
  `89c3f4fd157cd793cd60ad6328bab85779aebad29edcf28bd119283af2c0c278`;
- `COMMIT_PATHS.nul`:
  `8df0c41ae7dc4e95497a9a37f647c76c1fa2af15df1aedea1620d7bc71796f8a`.

This is a path-selection correction only.  It does not alter the archived
mathematical assessments or their execution-compliance exception, certify a
production gate, or promote any candidate theorem to the live manuscript.
