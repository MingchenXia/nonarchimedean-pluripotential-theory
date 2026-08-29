# P17.1 finite-level reduction: exact-live byte audit

Date: 29 August 2026

Verdict: **PASS**.

An independent read-only audit compared the exact-live files with the
independently and production-verified revised3 files.  In each file only the
three-line provenance header differs: lines 1 and 3 change, while the date on
line 2 is identical.  From line 4 through end of file the pairs are
byte-identical.  Thus no statement, proof, citation, label, `cref`, or `eqref`
content changed.

- exact-live statement SHA-256:
  `9be78feb5c4b76ae9f8ec7ec05d26dbaffebab602993dec7b37dcc8668819f81`;
- exact-live proof SHA-256:
  `ebb4c34fc1d06909ff2dfc7c0c0d918d1d548222b092e1b5e0472d2eecc4b603`;
- statement body SHA-256, from line 4 through EOF:
  `26e687f575f75253b472089cb688ec203b85421b76bb0483e62065270dd4a4f0`;
- proof body SHA-256, from line 4 through EOF:
  `5ff272ba1d9bb3da9147e83b1f172338caf0c8fca1c52f5d2034475096bc5d9d`.

A standalone two-pass build completed with no warning, error, unresolved
reference or citation, or overfull box.  Its auxiliary file was byte-identical
to the revised3 harness auxiliary file.
