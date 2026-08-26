# P09.2 product--Gauss live-integration receipt — 26 August 2026

## Scope and mathematical disposition

This receipt controls the exact live integration of a book-level solution to
the remaining Gubler--Jell--Rabinoff ordinary delta-metricity question.  It
proves two statements.

1. Let a split algebraic torus act on an algebraic variety, and let
   `h` be an equivariant locally integral piecewise-affine map to the
   cocharacter space.  If `F` has nondegenerate quadratic Hessian, the metric
   with weight `F(h)` is an ordinary Gubler--Künnemann delta-metric if and
   only if every tropical coordinate of `h` is CLD-smooth.
2. For an abelian variety with split Raynaud uniformization and an ample
   rigidified line bundle, the normalized cubical metric is ordinary delta
   if and only if the residual Raynaud extension is isotrivial.  Constant
   rescaling preserves this status.  Hence no cubical metric on an ample
   line bundle in non-isotrivial mixed reduction is ordinary delta.

The second statement answers P09.2 negatively, including its ample symmetric
formulation, and retires the atom.  It does not classify every individual
nonample cubical line bundle or enlarge ordinary delta-metrics to the
weakly-smooth category.  No novelty or priority claim is made.

## Controlling production verification

The exact statement and proof passed production Rethlas run
`20260826T055627Z_b68659fba1be`, item
`pi_75c74fac9a98efc3719b9773`, using `gpt-5.6-sol` at `xhigh`.  The final
disposition is `correct`, with 1/1 item checked, zero critical errors, and
zero gaps.  The item completed with return code zero in 1,296.053 seconds;
the validated verifier log reports 182 tokens used.

The exact packet hashes are:

| file | SHA-256 |
|---|---|
| `p09p2_product_gauss_statement_20260826.tex` | `b68659fba1be78b30345c112c637d38f41372dc70526fef8ecad6a450f7cbf47` |
| `p09p2_product_gauss_proof_20260826.tex` | `3bfc656409c96a2be52161798efffe726657a3e0b2d2831a5f25a795e8c4d262` |
| `p09p2_product_gauss_compile_20260826.tex` | `872612f94feed2730dbb5549804c0ac9ff8e247c6204dee0bc98fa67e79415a5` |
| `p09p2_product_gauss_compile_20260826.pdf` | `c62d0f6bd5763fd119c697250c75a2cbcb30bd5110c38c9d98f13dab03cfcf6f` |
| `request.json` | `f69482fd4e5f7e59089d29282578993df917ead260ad13ca8133005d1197b856` |
| `response.json` | `4ad13be952db51d53829be0d2fe5bc09a0bb134bdce226e3560672924b7c4eda` |
| `headers.json` | `9a7c03f36bc2ed24ec53e6bd3af19494f9b8cfcf2de7af727cc608b3b0b7d9e9` |

The copied run artifacts are preserved under
`p09p2_product_gauss_run_20260826/`.  Their hashes are:

| artifact | SHA-256 |
|---|---|
| `aggregate/manifest.json` | `2ca504ee1a1e39c7e75de89770488a959e0710aad6bb6a02d4b814118abd0233` |
| `aggregate/verification.json` | `4497ecb2166d4fea8c60b9c1df847cd5d17e8565c3d88aa92267688c90f1a6d0` |
| `item/log.md` | `37b90e05bee09521b21eb4041a661ca86de594a5fb5888e187d04d8e5cf1297d` |
| `item/process_child_guard.json` | `5ffa51f9a885fe1ae40ad1016ee20886986c4e66fea094ea53db5225e0179658` |
| `item/process_guard.json` | `b17d46eca99235de9068d456244a7da54f6592b1e67e24363bee8f4982ea13ad` |
| `item/verification.json` | `fce0b157a775fb39b6ffa33b8c8da30af2d67abee08c82b6115eb60079cb034a` |

The aggregate proof digest is
`3bfc656409c96a2be52161798efffe726657a3e0b2d2831a5f25a795e8c4d262`.
The item context digest is
`5752b133720d3866ba4af587df46a18a556d6d61ebc32877b38203ec4fc14f6f`.
The audited verifier checkout was at Git commit
`60ca1e612f9779466621094efccb474fb4d22432`.  The production code hashes
were `88692d76...` for `server.py`, `e0827870...` for `proof_context.py`,
`0adabc3a...` for `contracts.py`, `17313bce...` for
`process_supervisor.py`, and `a2e3a367...` for the verifier instructions;
their full values are preserved in the audited service record and run
manifest.

## Independent mathematical and source gates

Four independent gates preceded the production run.

- The hostile audit checked the relative-Gauss specialization, common-cell
  lineality, nondegenerate-Hessian contraction, analytic-local invariance,
  and passage from ample symmetric to arbitrary ample rigidified bundles.
- The proof audit found one real-direction quantifier gap in an earlier
  version.  The frozen proof repairs it by defining relative Gauss points for
  all `w` in the real cocharacter space and using constant `K`-sections only
  at value-group-rational weights.  The repaired exact bytes passed the
  follow-up audit.
- The primary-source audit checked Gubler Proposition 7.2, Gubler--Künnemann
  Definition 9.9 and Proposition 9.15, and the exact CLD Raynaud locators.
  Its final-scope addendum records that Gubler's algebraization theorem does
  not require `X` to be smooth.
- The novelty-scope audit found no later primary source asserting the
  assembled product--Gauss conclusion.  The book nevertheless makes no
  novelty or priority claim.

The controlling audit hashes are:

| audit | SHA-256 |
|---|---|
| `p09p2_product_gauss_hostile_audit_20260826.md` | `2f15b1b73a8c86fc63edd29cffb73e63873ddadbb58590eee3b6aac5af21da5e` |
| `p09p2_product_gauss_novelty_scope_audit_20260826.md` | `4b2e88a11862eff4ad1bba54ef3ea6adc3d3df93d1ceac12e446a7bf03ce5d24` |
| `p09p2_product_gauss_primary_source_audit_20260826.md` | `5bbc55cf21a59a4205ae89a626864c2a49bc0352bfe3dd8945a7c52a544c60de` |
| `p09p2_product_gauss_primary_source_audit_20260826.tex` | `57f276ffffa97a0b48f384f9586cc584b274b9c7f0e9055ec08d0eedc04781d1` |
| `p09p2_cld_smooth_pl_bridge_audit_20260826.tex` | `d596f6f99e78d4bbe13c23858130b79db8b2b8658c453300926b16aab4b7b941` |

## Live integration and inventory retirement

Chapter 19 inputs the frozen statement and proof directly, after the
canonical positivity theorem.  Surrounding exposition supplies the chart
and notation bridge without changing verified bytes.  The warning, exact
scope remark, mixed-reduction example, limitation table, dictionary, source
notes, and conclusion now distinguish the historical GJR open question from
the book's negative resolution.  Chapter 72 removes the corresponding
`problem` environment and records the result, proof mechanism, source
boundary, and production receipt.

The internal label `thm:p09p2-product-gauss-candidate` is deliberately
retained as a legacy key because it belongs to the production-verified
statement bytes.  The rendered theorem has no optional or conventional name,
and neither the label nor the frozen pre-verification comments appear in the
book.  Renaming the key would require a separate exact-live verification and
would add no mathematical content.

The active inventory is now 16 formal problem environments and 56 atoms,
with tier counts `T1=0`, `T2=8`, `T3=14`, `T4=17`, and `T5=17`.  The dated
25 August partial-reduction receipt remains intact as history.

## Build, static, source-closure, and visual gates

The post-integration whole-book build converged at 3,149 pages.  Its PDF has
SHA-256
`85883cbdcc85be99ce88b62cb8e2ab0a67c0848071585a91fdf1f1e4bd1406fb`;
the final log has SHA-256
`0d3b9d316da10c9752dc519b71749e462d6dafc745d059624c4777a64cf30f83`
and contains no TeX error, undefined reference or citation, duplicate label
or destination, rerun request, BibTeX warning, or overfull box.

The refreshed 111-file closure is
`editorial/current_source_closure_p09p2_20260826.sha256`, with ledger
SHA-256
`80b962ed85a732950b777f7225eab8b1c88f64eea075bcd7fd5b793c3e1aac9f`.
Every entry passed `shasum -a 256 -c`, and comparison with the converged
`book.fls` found no omitted repository-local authoring input.

PDF pages 952--958 and 963, together with pages 2968--2969, were rendered at
130 dpi and inspected.  They cover the complete theorem and proof, the clean
transition to the canonical measure, the mixed-reduction example, and the
Chapter 72 retirement record.  No clipping, overlap, malformed display,
missing glyph, broken hierarchy, or unreadable line occurs.  Full build and
visual evidence is recorded in
`editorial/current_source_build_p09p2_20260826.md`.
