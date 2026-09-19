# P06.2 polyannulus slope exact sequence v66: build report

## Integrated result and scope firewall

Proposition `prop:p062-polyannulus-slope-exact-sequence` identifies the
globally realizable parallel slopes of continuous zero-current functions as
the kernel of contraction with the zero-current radiance class.  It records
the natural exact sequence
\[
0\longrightarrow\mathscr P_W(W)\longrightarrow\mathscr Z(Y)
\longrightarrow H^0(W,\mathbb V_{\pi,\mathbf R}^{\vee})
\longrightarrow\check H^1(W,\mathscr P_W).
\]
The injectivity and vanishing consequences are integrated in Chapter 18, its
chapter synthesis and comparison table, and the detailed and summary P06.2
entries in Chapter 72.  The result retains the v64/v65 local
curve--polyannulus product hypotheses.  It does not trivialize the integral
local system, produce analytic annular coordinates, or settle arbitrary
analytic germs or nonproduct annular fibrations.  P06.2 therefore remains
active.

## Frozen verification history

1. The initial packet returned `wrong` with zero critical errors and two
   dependency-packaging gaps.  Item
   `pi_c4688dc5e6e4c4e79ff4385a`; proof digest
   `a8f0f97e04a2b15a8ceee1769380200d3049a03a4c19efe542532ada070273e8`.
2. The repaired packet returned `correct` with zero critical errors and
   zero gaps.  Item `pi_aabbd7138966aebdea2e7d0a`; proof digest
   `8deb5a42fb2210dc3202964d87f7cecbaf57211ccf6746093a5042ff876ebadc`.
3. The pre-layout second-pass packet returned `correct` with zero critical
   errors and zero gaps.  Item `pi_c7e21a8b160c7d9b03b50d58`; the proof
   digest is unchanged.
4. The controlling polished packet, after the page-level wording and display
   repair, returned `correct` with zero critical errors and zero gaps.  Item
   `pi_2956b458517b66c3aab40649`; statement digest
   `e8d4ed82a6806be8f5120c563a105b09d5eb37cca8af35b2861593c80fbc3790`;
   proof digest
   `8deb5a42fb2210dc3202964d87f7cecbaf57211ccf6746093a5042ff876ebadc`.

The statement and proof reconstructed byte-for-byte from the controlling
request have these same two digests.

## Build and audit

- The first complete v66 build reached the final part of the book but ended
  with a transient `pdflatex: book: Input/output error`; no TeX fatal error
  preceded it.  A clean retry completed.
- After the final page-level repair, `latexmk` converged successfully:
  3341 pages and 17,706,660 bytes.
- The strict Mingchen audit passed both without and with the two project
  bibliographies: zero errors and zero warnings.
- The reference audit found 359 files in the build closure, 11,338 labels,
  zero multiply defined labels, and zero dangling references.
- The final log has no undefined citations or references and no stale-rerun
  request.  The former 19.16943 pt v66 opening-display overflow is gone.
  The 22.43497 pt warning immediately after the v66 proof belongs to the
  pre-existing display at Chapter 18 source line 5342; its rendered page was
  inspected and is not clipped.
- The open-problem inventory audit passed with 46 active atomic questions,
  14 formal problem environments, and tier totals
  `T1=0, T2=5, T3=8, T4=16, T5=17`.
- `git diff --check` passed.

## Page inspection

Every rendered page in the following ranges was inspected at 120 dpi:

- physical pages 1294--1298 (printed pages 1226--1230): the v66 statement,
  proof, preceding v65 transition, and following corollary transition;
- physical pages 1329--1331 (printed pages 1261--1263): Chapter 18 synthesis;
- physical pages 1362--1364 (printed pages 1294--1296): Chapter 18 comparison
  table;
- physical pages 3156--3158 (printed pages 3088--3090): detailed P06.2 status;
- physical pages 3184--3186 (printed pages 3116--3118): Chapter 72 current
  results, item 19.

No added text is clipped or crosses a margin.  Proposition 18.8.30 begins on
printed page 1227 (physical page 1295).

## SHA-256 ledger

### Live packet and integration files

- `STATEMENT_LIVE.tex`:
  `e8d4ed82a6806be8f5120c563a105b09d5eb37cca8af35b2861593c80fbc3790`
- `PROOF_LIVE.tex`:
  `8deb5a42fb2210dc3202964d87f7cecbaf57211ccf6746093a5042ff876ebadc`
- `AUDIT_LIVE.md`:
  `d7b90e0043727cac82ea84f58a4f02a3d15978370e02eed63f4704c76b054bc3`
- `SOURCES_LIVE.md`:
  `db5078cdeef7ae0ab0d8d2a6dcaa9cdcdea0e0056d633ecb23cc94fff4c630fc`
- `ch18_delta_forms.tex`:
  `ccb21392b5219a239555d3c9c87fdff01124f822b191e16f81466e472d3189c3`
- `ch72_major_open_problems.tex`:
  `ac55d24c3f099ef94f4e1b3553503d9565f5e5433c9146c396c3d6271f7d6a98`
- `open_problem_atomic_inventory_20260824.md`:
  `28b03c196e3e936b634e84215ddcbe1213c54f4d13ae4e06a028e8b4235474d3`
- `book.pdf`:
  `c24e19851936f2d5aa7b7c9053e0ec3d625398458eb310e40d000a539ea1c6bf`
- `book.log`:
  `050b1d335f27bf6395abde0a1f922a0e0136378bb4e5294d2d0523816991c694`

### Archived verifier transport

- initial request:
  `8a25abbf8d9788ea207c482b7da696cdb4af341e2aecc1f9c35d6406198d559b`
- initial response:
  `a24c91b47fefbb83f8213fe1bff903f37e2cfa7901787e1acdb3d793e51e0a0f`
- initial headers:
  `746e93bc82b16f9fdbde7f7e3d4b5da6a4f0bf01d9d3c871831a74c5afd25558`
- repaired request:
  `11651e0731be0d6637e4e16c6d6b51a6a7292dc10d103fa65177e09a03e938d9`
- repaired response:
  `b8762b7d1bdbac6402f1bf2c2d0d0889f1144c4e36a3c7e56637f8ec360e66ec`
- repaired headers:
  `adac56245587a1a3928e78f4b4567dddbb3234be08c1a4028faea9865a221a40`
- pre-layout final request:
  `9d83d2063e4ede95c07e5005e15d888e343ab9e0c3940e924e3453b11791ad0f`
- pre-layout final response:
  `7ea9a2f021cccd5146c0426442da3cbebe9aba50a3e98b4e22f2feebf31c555b`
- pre-layout final headers:
  `63c6c65571ee8f8448f2068742998c74d3129c0b71ff1494686f63cdb61287e7`
- polished request:
  `f70d9eff258866ce6b5813ad62c67d8cbf945bad9506e1205061cf81336ea811`
- polished response:
  `1bd0b7b4ff6ab395a98d580808a0541b5f4d3815461c26329726c0205ce5e7b5`
- polished headers:
  `ec6123bd851e250a01f24e587b51a937f7cf49003e0e4e5d725b7047b66fd4f1`
