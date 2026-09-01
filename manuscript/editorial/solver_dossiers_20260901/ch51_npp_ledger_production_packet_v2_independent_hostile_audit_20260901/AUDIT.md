# Independent hostile audit: repaired Chapter 51 source-closed packet v2

## Verdict

**PASS — packet source-closure gate only.**  The exact frozen packet
`/private/tmp/ch51_npp_ledger_comprehensive_production_packet_v2_repaired_authored_20260901`
is ready to be attached to a separately audited final-path release.  No
packet blocker survived this audit.

This verdict does **not** audit a runtime, authorize installation, run a
smoke, submit a production request, certify a production response, edit the
live manuscript or inventory, or perform a git operation.  The packet itself
correctly leaves `release_stage` null.  Its runtime/smoke blocker is a
separate release-stage gate.

## Immutable envelope

I independently parsed the top SHA ledger and strict JSON manifest.  The
packet contains 32 regular files (31 rows plus `SHA256SUMS`) and six
directories.  The exact envelope hashes are

- `SHA256SUMS`: `4b0e713319c99a2a0d2d7d157d089e974b231b4656ed57759f0039c28dfa20a5`;
- `MANIFEST.json`: `af8f5d6763bc35ee04afc0b8e430f2d4bdba48551a9c712542058fed26a534f7`.

Every manifest size and hash and every SHA-ledger row matches the actual
bytes.  All directories have mode `0555`; all regular files have mode
`0444`.  There are no symlinks, special files, cache directories, bytecode,
editor temporaries, or duplicate JSON keys.

The authored checker was run twice and returned
`PASS_REPAIRED_CH51_SOURCE_CLOSED_PACKET_AUTHORED_ONLY` twice.  The five-test
authored suite was independently run twice; both runs completed with five
tests, zero failures, and zero errors.

## Preservation of the audited target

The v1 top SHA is
`145f6305a0ea847c176e1cd55d8da46977d8c2545c873d792a6c1ba5f7a18d71`.
Direct byte comparisons against that frozen packet show equality for all ten
substantive preserved files: both target fields, both `source_exact` files,
all three PDFs, and all three normalized text derivatives.  In particular,

- `STATEMENT.tex` and `LOCAL_CONSTRUCTION_REPLACEMENT.tex` both have hash
  `9ff17ccf6ecafdaedf746e8472671bbd9436cf5661667e27815e1a1d39698575`;
- `PROOF.tex` and `LEDGER_REPLACEMENT.tex` both have hash
  `187ef5530c9baf375cab4d15108a4447f3ddb3cc4c0b2780a7bf8d7cd2f33d70`.

Thus v2 repairs provenance and line-addressing metadata without changing the
independently audited mathematical target.

## Independent PDF and LF-only reproduction

I invoked actual `pdftotext -layout INPUT.pdf -` independently for each
pinned PDF.  Each raw derivative ends in byte `0x0c`, not `0x0a`; each
bundled text is exactly the raw derivative followed by one byte `0x0a`.

| source | raw bytes | raw SHA-256 | bundled SHA-256 |
|---|---:|---|---|
| BEGZ | 163107 | `890173e309165984432e7326d13b7e096662cc805fbc19045a297f12211254c7` | `8bc1801705532fc32a2e8b5d0dcd8d19ec6c3b4efdeab36fc945264e0fad0a91` |
| Bedford--Taylor | 83498 | `716a2e1012a35ab6811873bc9f84d981627b7d6f4d9e6e4c8d48b0b525460d8b` | `247b69c13c392e1b05b3ae964059270b0dae47cecdee889648afd13ed28910d4` |
| DDNL | 140674 | `c46d0c5d9ef56e4788337baef00e53bd099f130cf13913cd94b1ba19e9c5004f` | `cd1cc5bacbfc6b0ec023cceaf751d22a8484cfe38ae8bac531b1f5d99a321df7` |

Plain `pdftotext` was also reproduced as a negative control.  Its hashes are,
respectively, `51410bdb...`, `b90db94a...`, and `58e5cd14...`, all different
from the frozen layout derivatives.  This directly confirms the corrected
extraction declaration rather than merely comparing two metadata fields.

The independent line decoder removes the required final LF and splits the
remaining bytes only at `0x0a`.  It never calls `splitlines`; every `0x0c`
remains within its LF line.  The resulting counts are 2651, 1778, and 2308
LF lines, retaining 54, 40, and 38 form-feed bytes.  In all three derivatives
the last addressed line is the terminal form-feed itself.

Using this decoder, I recomputed all thirteen inclusive routed byte ranges,
adding LF after every selected line.  All thirteen SHA-256 values match.
The three critical anchors also match both their exact line hashes and their
readable prefixes:

- BEGZ Definition 1.1: LF line 211;
- Bedford--Taylor Theorem 6.9: LF line 1107;
- DDNL Theorem 1.1: LF line 81.

`SOURCE_ROUTES.json` contains neither `splitlines` metadata nor any parallel
runtime line-number field.  Its sole line domain is one-based, inclusive,
LF-only addressing.

## DDNL import and internal partition

The import is exactly `PROOF.tex` lines 317--327.  DDNL lines 62--65 define
“(u) less singular than (v)” by (v\leq u+C); lines 74--86 state
Theorem 1.1 with the corresponding mass inequality from the less singular
tuple to the more singular tuple.  The target explicitly cites that theorem
and, for (p<n), adjoins (n-p) smooth Kähler entries with zero potential.
The orientation and specialization are correct.

The internally supplied blocks are local lines 1--150 and proof lines
51--316 and 328--420.  Imported and internal proof ranges are disjoint and
their union is exactly proof lines 51--420.  Proof lines 1--50 are the theorem
statement, so their absence from the proof-argument partition is deliberate,
not a gap.

## Prior FAIL provenance

The copied v1 FAIL dossier has top SHA
`173fc76c8dbe077eaa61fa60d89c1d586d2405bf01bc238bcf92f5415aff0a19`;
all of its internal hashes reproduce.  It records three blockers:

1. misdeclared extraction mode;
2. divergent LF/runtime line numbering;
3. reuse of a known-failed final-path smoke runner.

This v2 packet repairs the first two and binds them by executable checks.
The third is correctly excluded: there is no runtime in this packet, and the
request says a separately repaired and audited stage is still required.  The
prior FAIL explicitly did not reject the mathematical target.

## Hostile mutation audit

Seven independent throwaway copies were mutated.  Both the independent gate
and the authored packet checker rejected every copy:

| mutation | independent rejection gate |
|---|---|
| `pdftotext -layout` changed to plain `pdftotext` | extraction mode |
| LF separator changed from `0x0a` to `0x0c` | line-addressing contract |
| `runtime_line_numbering: str.splitlines()` injected | forbidden route metadata |
| routed range hash replaced | external range table |
| BEGZ anchor content changed in place | exact anchor bytes |
| `STATEMENT.tex` byte changed | target/source pin |
| DDNL imported range changed from 317 to 316 | claim partition |

The mutation suite is rerun by this dossier's checker and compared with
`HOSTILE_MUTATION_RESULTS.json`.

## Reproduction

Run

```text
python3 -B check_audit.py
```

from this dossier.  The terminal success token is
`PASS_INDEPENDENT_CH51_PACKET_V2_HOSTILE_AUDIT`.
