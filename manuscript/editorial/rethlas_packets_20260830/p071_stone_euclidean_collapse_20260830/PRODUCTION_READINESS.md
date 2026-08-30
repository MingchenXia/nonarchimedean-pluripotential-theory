# Production-readiness audit

Date: 2026-08-30

This audit does not alter the frozen mathematical candidate and does not
submit it to Rethlas.

## 1. Exact principal bytes

| role | file | SHA-256 |
|---|---|---|
| statement | `statement.tex` | `dfd8c7cc9d6d26f50260707975ff62d4f292627f084400bcd37b32253c876cdc` |
| proof | `proof.tex` | `9316e1a9df86c73a68ec099d3254e451ceaaac17a15c2a92441ad44961d863f6` |

Both files end in exactly one newline.  Consequently the dependency-aware
materialization performed by `submit_rethlas_packet.py` retains each
principal file as one byte-for-byte contiguous block.

The independent exact-byte audit is
`INDEPENDENT_EXACT_BYTE_AUDIT.md`, SHA-256
`a7a88e7e8703d4a915fe174c008ed45ef2c01d344aa18ddd3f3966495d27d58e`.
It records `PASS`, zero critical errors, and zero unresolved gaps.

Other packet inputs presently available for a source-aware request are:

| file | SHA-256 |
|---|---|
| `SOURCE_AND_OBLIGATION_MATRIX.md` | `8b5a03f47f3442e62da160cf5b079027f9c5a6aacf289120cab5cbfe9dfcbebd` |
| `HOSTILE_BOUNDARY_AUDIT.md` | `d1a99f69942ab9cb67b76e63d05d3a302e4dc4487c74e6b5bf6cf3c509b8e9ef` |
| `README.md` | `5a0b5b8019b54e52e5380eb8309623cb981a90ae00d85f1d5367dee5f9de36c6` |
| `SHA256SUMS` | `21535bd1533feaf4b34ec4be348077267aff82a399f48de0d883265c46de9dad` |

The existing `SHA256SUMS` predates the independent audit and this readiness
file.  It correctly binds the frozen principal bytes and the original four
packet files, but it is not a complete manifest of every later audit file.
This is an archival observation, not a mathematical dependency failure.

## 2. Dependency closure

### Mathematical closure

**Verdict: closed relative to the cited CLD source; no cross-packet theorem
dependency is present.**

Every newly asserted topological or convex-analytic step is proved in the
packet.  The proof does not invoke any theorem, lemma, label, or notation
defined in another research-candidate packet.  In particular, it does not
depend on the fixed-core flattening packet or on any earlier partial P07.1
candidate.

The only imported mathematical source is:

> Antoine Chambert-Loir and Antoine Ducros, *Formes differentielles reelles
> et courants sur les espaces de Berkovich*, arXiv:1204.6277v2,
> 25 July 2025 (`CLD25`).

The exact imported interfaces and navigation positions in the extraction
`/private/tmp/CLD25.txt`, SHA-256
`021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e`,
are:

| source locus | extraction line | use |
|---|---:|---|
| Section 1.8.2 | 2165 | standing `(Q,R)` parlinear parameters |
| Sections 3.1.1--3.1.3 | 3414, 3417, 3437 | topology, domains, G-sheaf and parlinear axioms |
| Definition 3.5.1 and Example 3.5.4 | 3997, 4040 | positivity and the Hessian test |
| Section 6.1.1 | 7030 | affine refinement axioms |
| Definition 6.2.1 | 7069 | smooth functions/forms |
| Definition 8.1.1 | 9723 | generated psh sheaf and decreasing limits |
| Lemma 8.1.4 and Definition 8.1.13 | 9757, 9879 | first transfinite stage and locally approachable functions |
| Proposition 8.3.2 | 10020 | Euclidean psh/convex comparison |
| Sections 9.1.1--9.1.4 | 11236, 11250, 11266, 11273 | product G-tropical and affine structures |

A durable copy of the official 608-page v2 source is already elsewhere in
the worktree at
`manuscript/editorial/rethlas_packets_20260829/p213_trivially_valued_curve_candidate_audit_20260829/sources/CLD25.pdf`,
SHA-256
`f659b1fd1423baba9552c03e4738f59e5ee985df0bbf671c8ce9d9718a5d0629`.
The bibliography key is present in
`manuscript/bibliography/NonArchimedean.bib` at the entry `CLD25`.

### Internal-reference closure

**Verdict: closed.**  A mechanical union-of-files check finds no
`\eqref`, `\ref`, or `\cref` target missing from the combined
`statement.tex` followed by `proof.tex`.  There are no external theorem
labels.  The single citation key, `CLD25`, exists in the book bibliography.

## 3. Standalone status

The word *standalone* has three relevant meanings here.

1. **Standalone as a production mathematical candidate: YES, relative to
   the published CLD interfaces just listed.**  The exact statement and
   proof can be sent without any other candidate theorem.

2. **Standalone as a completely source-free proof: NO.**  It deliberately
   imports the definitions and structural product/positivity facts from
   `CLD25`.  This is normal source dependence, not a missing unpublished
   lemma.  For a maximally source-aware production payload, prepend
   `SOURCE_AND_OBLIGATION_MATRIX.md` and the two audits to the proof field.

3. **Standalone as a naked compilable LaTeX document: NO.**  The two frozen
   files are fragments rather than a document.  A minimal wrapper needs
   `amsmath`, `amssymb`, and `mathrsfs`, together with the
   `NonArchimedean.bib` bibliography.  A three-pass `pdflatex`/`bibtex`
   check with precisely those dependencies completed with exit code zero,
   no unresolved cross-references, no undefined citations, and no undefined
   control sequences.  The compile artifacts were kept outside the
   worktree in `/private/tmp/p071_readiness_compile_20260830/`.

The Rethlas endpoint consumes statement/proof text rather than a compilable
LaTeX document, so item 3 is not a production blocker.

## 4. Production-request material

The repository submission helper is
`manuscript/editorial/tools/submit_rethlas_packet.py`, SHA-256
`93915b234fa73c96983b6406f95a41d468438caaa07cfa19321f786badd6f9c5`.
It constructs a UTF-8 JSON request containing exactly `statement`, `proof`,
and a live verification deadline, then archives the response and safe
headers.

For source-aware production, the intended dependency order is:

1. `SOURCE_AND_OBLIGATION_MATRIX.md`;
2. `HOSTILE_BOUNDARY_AUDIT.md`;
3. `INDEPENDENT_EXACT_BYTE_AUDIT.md`;
4. the frozen `proof.tex` principal block.

The corresponding invocation, to be run only when production submission is
authorized by the parent workflow, is:

```text
/Users/mingchen/Documents/ChatGPT/Yethlas/runtime/rethlas-arxiv191209719-venv-20260824/bin/python
manuscript/editorial/tools/submit_rethlas_packet.py
manuscript/editorial/rethlas_packets_20260830/p071_stone_euclidean_collapse_20260830/statement.tex
manuscript/editorial/rethlas_packets_20260830/p071_stone_euclidean_collapse_20260830/proof.tex
manuscript/editorial/rethlas_packets_20260830/p071_stone_euclidean_collapse_20260830/production_run_20260830/request.json
manuscript/editorial/rethlas_packets_20260830/p071_stone_euclidean_collapse_20260830/production_run_20260830/response.json
manuscript/editorial/rethlas_packets_20260830/p071_stone_euclidean_collapse_20260830/production_run_20260830/headers.json
--proof-dependency manuscript/editorial/rethlas_packets_20260830/p071_stone_euclidean_collapse_20260830/SOURCE_AND_OBLIGATION_MATRIX.md
--proof-dependency manuscript/editorial/rethlas_packets_20260830/p071_stone_euclidean_collapse_20260830/HOSTILE_BOUNDARY_AUDIT.md
--proof-dependency manuscript/editorial/rethlas_packets_20260830/p071_stone_euclidean_collapse_20260830/INDEPENDENT_EXACT_BYTE_AUDIT.md
--endpoint http://127.0.0.1:8107/verify
--timeout-seconds 3300
```

These lines are displayed separately for readability; an actual shell
invocation must join them as arguments to one command.

## 5. Missing files and references

### Required before claiming production verification

- `production_run_20260830/request.json` is absent.
- `production_run_20260830/response.json` is absent.
- `production_run_20260830/headers.json` is absent.
- Consequently there is no production receipt, service-log binding, or
  production verdict yet.

These files should be created by the submission helper at submission time;
a request with a fabricated or stale deadline should not be prebuilt.

### Optional hardening, not a blocker for submission

- The packet does not contain its own copy of the CLD PDF or a compact exact
  source-excerpt file.  The full primary PDF is available at the durable
  worktree path recorded above, and the source matrix gives exact loci.  If
  production policy requires every cited source passage inside the request
  payload, a dedicated exact CLD excerpt dependency must first be created
  and hashed.  Existing project production practice accepts the source
  matrix plus primary-source pinpoints.
- There is no standalone compile wrapper in the packet.  This is irrelevant
  to the text-based verifier and to later live-book inclusion.
- `SHA256SUMS` does not list the later independent audit or this readiness
  audit.  A post-production archival manifest may add them without changing
  the frozen statement/proof.

No citation key is missing, no internal reference is unresolved, and no
unpublished mathematical dependency needs to be supplied.

## 6. Readiness verdict

**READY FOR SOURCE-AWARE PRODUCTION SUBMISSION, BUT NOT YET PRODUCTION
VERIFIED.**

The exact principal bytes are frozen, internally closed, independently
audited, and free of cross-packet proof dependencies.  The only absent
required artifacts are precisely the request/response/header archives and
receipt that must be generated by the production call itself.  This audit
made no such call and did not edit `statement.tex` or `proof.tex`.
