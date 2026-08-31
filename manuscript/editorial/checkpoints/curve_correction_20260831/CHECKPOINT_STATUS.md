# Curve correction source checkpoint

31 August 2026. This is a source-correction milestone, not a completed book
or a solution of the general nontrivially valued envelope property.

The source manifest records 76 exact files relative to base commit
`c50fa622b822d31122e283be1d1864e2e414b085`. The actual TeX recorder has
104 distinct editorial inputs; exactly four were not already tracked at
that base, and all four accepted statement/proof files are included.
Independent and production evidence for the corrected curve comparison
and Tate obstruction is included. Historical draft snapshots are preserved;
the stage-2 and stage-3 proposals are explicitly pending, not approved live
mathematics. Chapter 29/31 proof warnings remain until the full replacements
have passed their required checks.

A durable local source-overlay archive was created at
`/Users/mingchen/Projects/Yethlas/book_checkpoints/curve_correction_20260831_sources.tar.gz`.
Its SHA-256 is
`eacf93de575242a9f9d14585fa39ff67430739315a68cc50360f1f44d68d5f12`.
Reading the archive directly confirmed every one of the 76 source hashes
and found no missing source or manifest file. It also contains the file
list and source manifest, plus 78 ordinary macOS AppleDouble metadata
entries. Those metadata entries explain why a strict 78-total-member check
initially failed; they do not replace or alter the 78 intended data files.
This overlay assumes the recorded base commit. It is not a full standalone
repository archive, and it does not include the PDF or later research packets.

The last book build has 3476 pages; the exact PDF and bounded visual-check
scope are recorded in the root correction checkpoint. All source files
retain the empty author and acknowledgments convention. No source checksum
or model verdict is presented as a formal proof-assistant certificate.

`git diff --cached --check` reports preserved blank lines at the end of the
frozen Tate statement/proof and space-only context lines in archived patch
files. These bytes are deliberately unchanged because they are covered by
the existing exact-source records. The live editorial changes themselves
passed the whitespace check before those archival files were staged.

This status file records the completed local archive step. Commit, remote
push, and durable repository synchronization must be verified separately;
their success is not inferred from the archive.
