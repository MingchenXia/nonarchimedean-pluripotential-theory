# P06 exact-live Chapter 18/19 integration receipt

Date: 25 August 2026 (Asia/Shanghai)

Status: integrated and statically checked; the root coordinator retains the
final full-book build gate.

## Controlling production objects

| Live result | Run | Item | Statement SHA-256 | Proof SHA-256 | Verdict |
|---|---|---|---|---|---|
| real-PL zero-current converse | `20260825T061351Z_655e7f503e5d` | `pi_eea98ea0a54108cae4e076be` | `655e7f503e5db0cee8e0c94fdc765b6923aeebb7b89c7b5b98ad7827fa6e2421` | `7ad130bab1d9dd61ecbac818005c4b80fe405c3d9710a6bb588fea6fa30a856a` | `final/correct`, 0/0 |
| failure of ordinary CLD-smooth harmonic approximation | `20260825T055907Z_b5c8f0719b60` | `pi_d80993bb01a748f0422ae6a5` | `b5c8f0719b606707b8055f0ead8c1baa96b5d9732cccf51a0e86ec02c5e64f24` | `ba402983b6d88c03437c79af66dfd541c5a37b89c0bb2a6a67438ac84120565b` | `final/correct`, 0/0 |

Both requests decoded byte-identically to their frozen statement/proof files,
and all four frozen objects compared byte-identically with the live theorem
and proof slices after every repair.

## Live and ledger snapshots

| File | Lines | Bytes | SHA-256 |
|---|---:|---:|---|
| `../../parts/part2/ch18_delta_forms.tex` | 4010 | 193469 | `13fec80e99ef6db9a22b7578270262919491aa0c92da96bdc802ea540a7035a1` |
| `../../parts/part2/ch19_cld_examples.tex` | 4151 | 199631 | `9fb098c3a68002378b31f2f59d159b7a671077497b144ef0dea22aeaf104c7c7` |
| `../../parts/part6/ch72_major_open_problems.tex` | 2276 | 112618 | `8192b31a8b168751aa283f43eee5cae9a5c0dbe801d1a65b3fd11dba2dbd56e0` |
| `../../appendices/appL_provenance.tex` | 1355 | 61067 | `9eb8cc1c28282d923d57e7cc9ffce602e2faac73a36cd22907b70abb10b7be7c` |
| `../../../RESEARCH_QUESTION_LEDGER.md` | -- | -- | `8a443bb5368c6700262ca09502e0e4d6e007ed5246010aac63aae17db1e415ea` |
| `../major_open_problem_program.md` | -- | -- | `354f1cbc75072a2a9218038f358b6a6515ac023b2eebdef613b17c842eb3fe1e` |
| `../open_problem_atomic_inventory_20260824.md` | -- | -- | `8e1d267a21aecc8adff2900933e0f74e695992c707e009b16911001db6e99517` |
| `../rethlas_verified_results.md` | -- | -- | `2b99ed4fa955fd949ff149d13d892dfff3ee6786ea3999e9092340780f02aae8` |
| `../rethlas_open_problem_attempts.md` | -- | -- | `e774369474888f63ae79e249862ecd5b91c72c076c569372776db12c75c52385` |
| `../theorem_provenance.md` | -- | -- | `f0b20e9e1cdcd7be4c61490e47e33a0b8d92c250892b006eac2074d0d23f247f` |

These whole-file hashes are integration snapshots, not substitutes for the
content-addressed theorem/proof hashes, and may change under unrelated later
book edits.

## Problem accounting and scope

The live manuscript contains 18 formal `problem` environments.  The atomic
inventory contains 59 rows marked active `[Tn; open]` and one preserved
retired P11 row.  P06.3 remains one of the 59 active atoms, re-scoped to
ordinary CLD-smooth psh regularization.  No problem or atom was removed by
the harmonic counterexample.

The real-PL theorem does not cover arbitrary continuous higher-dimensional
functions.  The Chapter 19 counterexample does not cover psh approximants.
No novelty or priority claim is made.

## Checks

- `git diff --check`: passed.
- Each new theorem and equation label occurs exactly once.
- Citation keys `CLD25`, `GJR26`, `GR25Classical`, `Thu05`, and `Wanner19`
  are present in the live bibliography.
- The combined exact-packet minimal compile passed and produced six pages.
- A focused live compile of Chapters 18, 19, 72 and Appendix L passed with
  exit code zero.  Its PDF SHA-256 is
  `9d7cc6edd35fd6808015e8fbe4b012af63bffb03f9a90aa4fcf5913705159df4`;
  its log SHA-256 is
  `d2a0b70680dca4b8b779aee37d72f9fe63e4bf36f3f558781a9981813730fd97`.
  The log contains no TeX error, undefined control sequence, emergency stop,
  fatal error, multiply defined label, duplicate destination, or undefined
  citation.  Cross-references to omitted chapters are expected in this
  focused slice.

All stale, aborted, and rejected P06 runs remain preserved and explicitly
non-controlling in the two production receipts.
