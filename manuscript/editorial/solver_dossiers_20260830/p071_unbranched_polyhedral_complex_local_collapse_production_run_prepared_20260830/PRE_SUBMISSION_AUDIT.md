# P07.1 generator-convex complex: production pre-submission audit

Date: 30 August 2026 (Asia/Shanghai)

## Gate status

**PREPARED; NOT SUBMITTED.**  The offline assembler opened no socket, the
Rethlas endpoint was not invoked, and no response or header archive has been
created.  The live manuscript was not edited.

## Frozen principal and exact dependency

The principal bytes were read without modification from
`p071_unbranched_polyhedral_complex_local_collapse_candidate_20260830`:

- statement: `2bc8574fecdc46ecafc1e41f24608c6db60cb9e48f696204ef503a83bed0625e`;
- proof: `ab3348d8d0dc31c4c661e1358f8b70894eff83890a3c6d6abc412810dea4ca30`.

Their independent exact-byte audit has SHA-256
`1f0abda081c5ddcd0eaf9ac11a895af2e6b1b6eaace2fadebd9cb8281a4fd4e2`
and verdict PASS, with zero critical mathematical errors, proof gaps,
definition/type gaps, or source gaps.

The sole theorem dependency is the exact frozen Stone-parameter times convex
polyhedron result:

- statement: `b46b8e22fa8b3f8f64dcf8ae24d164b905dbe8d9035e37c3ede23321717cc002`;
- proof: `37a3b6a12f6ddd2a3038dd926dfe8120d8955756efe64608fbd2a37b33c01efb`.

Its source matrix and independent exact-source recheck have SHA-256 values
`9dcb2c8bab8fb47e3cdeebb8821776770fa1929b2712afbc047bddeed94ae1c0`
and `3ff43da8dd1044a0144d6f1410ad5b66020ff868c934886c87f3bc38b5c0f974`.
Its production response has SHA-256
`c5871408ef86be152ecd6e169eaae05f590feef00e5487d37f185780951d5285`
and reports verdict `correct`, zero critical errors, and zero gaps.

All nine entries in each frozen dossier's `SHA256SUMS` were recomputed
successfully.  All separately pinned audit, receipt, request, response, and
header hashes in `assemble_prepared_packet.py` were also recomputed.  The
principal source matrix and final independent audit bind the exact model
statement, proof, and production response.  There is no second manuscript
theorem dependency and no new external citation in the principal proof.

## Materialized production fields

The ordered statement inputs are the model statement followed by the frozen
principal statement.  The ordered proof inputs are the model proof followed by
the frozen principal proof.  Materialization uses exactly the current
`submit_rethlas_packet.py` rule: remove terminal newline characters from each
input, join adjacent inputs by two newline characters, and append one final
newline.

The resulting fields are:

| Field | Bytes | SHA-256 |
|---|---:|---|
| `statement.materialized.tex` | 10,476 | `e163679c6f1140eb3452e9f052f89f8895b7b1d300e081f6149feec099d47ac7` |
| `proof.materialized.tex` | 26,472 | `1505aa473b3092f80d26bde3e8e947c709b138992370599645948ed510e39400` |

Each of the four source files occurs exactly once in its materialized field.
The frozen principal statement and proof are the unique terminal byte
substrings of their respective fields.  Importing the production helper and
calling its own `materialize` function on the ordered sources reproduced both
files byte for byte.

`request.prepared.json` has SHA-256
`8b4486b42d899820ba7287827d75b1baf77e461e3fa77ecd539e866d112143ca`.
Its decoded `statement` and `proof` fields equal the two materialized byte
strings exactly.  Its deadline is deliberately `null`; it must never be sent
as if it were a completed request.  The actual helper call below supplies a
fresh ISO-8601 deadline and writes separate `request.json`, `response.json`,
and `headers.json` archives.

## Compile, reference, and visual audit

The semantic dependency-closed harness compiled cleanly with
`latexmk -pdf -interaction=nonstopmode -halt-on-error` in three passes.  The
result is a ten-page letter-size PDF:

- `compile.tex`: `864424a7c171a7ca3180c9a81b0f4406227b4f226b9bce8d79b14a2d0b68882f`;
- `compile.pdf`: `c6b5a0b7709cd83b39adf8445835b9eafad28b5ed1a8fedb6c5da7e7d731e032`;
- `compile.log`: `b354bd2f37e6f7bfada54f5ee70c99a073ed79affd4bff03db640816d91717bb`.

The final log has no TeX error, package warning, undefined reference or
citation, multiply defined label, overfull box, or underfull box.  A direct
scan found 33 labels, all unique, and 33 cross-references, all resolved.

All ten pages were rendered at 110 dpi and inspected.  The title, two theorem
blocks, proofs, equations, lists, margins, page breaks, proof endings, and page
numbers are legible and aligned.  There is no clipping, overlap, missing
glyph, black rectangle, or malformed reference.  The temporary page renders
were removed after inspection.

## Safe production command

First rerun the offline fail-closed preflight from the repository root:

```sh
/Users/mingchen/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 manuscript/editorial/solver_dossiers_20260830/p071_unbranched_polyhedral_complex_local_collapse_production_run_prepared_20260830/assemble_prepared_packet.py
```

Only after the currently active production request has released the endpoint,
submit the exact prepared mathematical fields with:

```sh
/Users/mingchen/Documents/ChatGPT/Yethlas/runtime/rethlas-arxiv191209719-venv-20260824/bin/python manuscript/editorial/tools/submit_rethlas_packet.py manuscript/editorial/solver_dossiers_20260830/p071_unbranched_polyhedral_complex_local_collapse_production_run_prepared_20260830/statement.materialized.tex manuscript/editorial/solver_dossiers_20260830/p071_unbranched_polyhedral_complex_local_collapse_production_run_prepared_20260830/proof.materialized.tex manuscript/editorial/solver_dossiers_20260830/p071_unbranched_polyhedral_complex_local_collapse_production_run_prepared_20260830/request.json manuscript/editorial/solver_dossiers_20260830/p071_unbranched_polyhedral_complex_local_collapse_production_run_prepared_20260830/response.json manuscript/editorial/solver_dossiers_20260830/p071_unbranched_polyhedral_complex_local_collapse_production_run_prepared_20260830/headers.json --endpoint http://127.0.0.1:8107/verify --timeout-seconds 3300
```

After the call, require that the decoded request fields retain the two hashes
above and that the response is final `correct` with zero critical errors and
zero gaps.  A production receipt and transport `SHA256SUMS` should be created
only after those conditions hold.
