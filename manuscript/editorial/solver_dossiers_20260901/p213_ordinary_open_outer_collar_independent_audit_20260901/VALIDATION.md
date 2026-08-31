# Validation and preservation record

Date: 1 September 2026.

The complete frozen note, source ledger, author validation and manifest
were read after the final author pins were announced. All 13 candidate
manifest entries and 14 checksums match. Historical L checks match
8 manifest/9 checksum entries; historical V checks match 15/16.
All four announced pins match, with 26 distinct equation tags and no
forbidden controls in the five candidate files.

The initial independent verifier run failed with ENOENT for
RESEARCH_NOTE.md because it treated V's relative manifest paths as
process-relative. Only the new verifier was fixed to resolve each
path against its owning manifest/checksum directory. The complete
rerun is preserved in INPUT_CHECKS.json. No input repair was made.

The mathematical verdict is full-scope PASS under the exact stated
input boundaries: L for the geometric properness/canonical-degree
part of the current consequence; V actual-model geometry only;
R unused. No required correction was found. The optional finite
phi-support ordering explanation is recorded in the report.

The PDF skill was used for read-only CLD page 302 inspection.
The full page was viewed; the render exited zero with no warning.
SOURCE_QA.json preserves its evidence. Only the owned scratch PNG
and its empty temporary directory were removed.

All authored files were created in this new audit directory with
apply_patch. There was no live or frozen edit, git action, production
call, permission bypass, TeX compile, or new PDF artifact.

The audit manifest covers seven new audit files and the candidate's
thirteen entries plus its manifest and checksum file: twenty-two
entries in total. The audit checksum file also covers the audit
manifest. The read-only verifier rechecks these after freeze.
