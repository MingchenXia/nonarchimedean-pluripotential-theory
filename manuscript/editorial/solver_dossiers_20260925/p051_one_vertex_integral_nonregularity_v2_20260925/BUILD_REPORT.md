# Build report

Final local release checks, 26 September 2026:

- scoped Mingchen-writing audit: 0 errors, 1 reviewed arXiv-only warning;
- minimal packet: 2 pages, 133,909 bytes, SHA-256
  `cb16f5666c66ca48889cdd775a81af760073299ed7fae02ed77a3dabf01fc7ed`;
- reference graph: 415 files, 11,864 labels, 0 missing inputs, 0 duplicate
  labels, 0 dangling references, and clean per-file structure;
- reference-checker tests: 6 passed;
- inventory: 42 active atoms, 12 formal environments, tiers
  `(0,3,7,15,17)`;
- full book: 4,090 pages, 19,465,527 bytes, SHA-256
  `1aced01d8f8c57975d09a6ed9d1b8510a44d651c42a3f773213faf969f413717`;
- full-book critical-warning scan: clean; 13 inherited Chapter 70 duplicate
  destinations remain;
- visual inspection: both minimal pages and final-book physical pages
  3797--3800 are clean.

The supplied withdrawn PDF is preserved byte for byte and is not treated as
a positive source.  No new model-verifier run or verdict is claimed.
