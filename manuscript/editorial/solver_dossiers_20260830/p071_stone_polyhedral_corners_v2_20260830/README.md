# P07.1 Stone × polyhedral-corner candidate, source-repaired v2

Date: 30 August 2026

This sibling release repairs only the exact-source provenance of the frozen
v1 candidate.  Its two principal mathematical files are byte-for-byte copies
of v1:

- `statement.tex`:
  `b46b8e22fa8b3f8f64dcf8ae24d164b905dbe8d9035e37c3ede23321717cc002`;
- `proof.tex`:
  `37a3b6a12f6ddd2a3038dd926dfe8120d8955756efe64608fbd2a37b33c01efb`.

No mathematical statement, hypothesis, proof step, label, or comment was
changed.  The v1 exact-byte hostile audit found zero critical mathematical
errors and zero proof gaps, but fail-closed the combined release because the
PDF fingerprint recorded in its source ledger did not match the PDF then
present at the recorded path.

V2 replaces that stale fingerprint by a reproducible chain:

1. the actual CLD PDF at `/private/tmp/CLD25_1204.6277.pdf`;
2. its SHA-256;
3. the command `pdftotext -layout`;
4. a regenerated extraction;
5. byte-for-byte equality of that extraction with the navigation text
   `/private/tmp/CLD25.txt` used in the source audit.

See `SOURCE_AND_OBLIGATION_MATRIX.md` and
`INDEPENDENT_EXACT_SOURCE_RECHECK_20260830.md` for the complete chain and
source ranges.  `RELEASE_MANIFEST.md` binds the release artifacts.

This remains a quarantined candidate.  It is not a live-book input, has not
been submitted to production Rethlas, does not claim novelty or priority, and
does not retire P07.1.
