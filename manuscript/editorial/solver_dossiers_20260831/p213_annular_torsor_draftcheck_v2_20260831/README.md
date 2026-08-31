# Wrapper-only retry of the torsor draft check

The first attempt is preserved in the adjacent
`p213_annular_torsor_draftcheck_20260831` directory. Its statement/proof pass
completed, and BibTeX completed, but the next TeX pass stopped on the literal
underscore in `SOURCE_INTERFACE.md` in the frozen bibliography's note.

This retry adds only the standard `underscore` package to the standalone
wrapper. No frozen statement, proof, example, bibliography, source ledger,
or audit is changed. At eventual book integration the filename should be
properly escaped or typeset as a path; the unescaped note is a real
standalone bibliography typography defect, not a mathematical gap.

`BUILD.json` records the actual retry outcome and warnings. The builder uses
draft mode only, creates no PDF, and hashes the examples without claiming
to have typeset their Markdown. The resulting manifest freezes the wrapper,
commands and generated evidence. The read-only command `node build.mjs --check`
rechecks both mathematical inputs and this dossier.
