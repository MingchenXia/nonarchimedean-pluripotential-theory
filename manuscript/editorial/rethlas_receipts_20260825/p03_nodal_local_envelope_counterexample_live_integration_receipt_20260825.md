# P03 nodal local-envelope counterexample: exact-live integration receipt

Date: 25 August 2026

## Production verdict

- Run: `20260825T094005Z_10ac70696f69`
- Item: `pi_31f95353b7e94f3cb98b09b6`
- Model: `gpt-5.6-sol`
- Reasoning effort: `xhigh`
- Verification status / verdict: `final / correct`
- Checked items: `1 / 1`
- Critical errors / gaps: `0 / 0`
- Adaptive round: `0`
- Process and child guards: `completed / completed`
- Proof digest:
  `21fc22e5b1f3b3084f29df412a57485131e46ca160cf168db18da8a3e2559fc7`
- Item context digest:
  `b161c4d9f792e1f6eedf5d5fbcbbc1705c7b53beefdd1e05d5711fdc46ffb90b`

The verifier accepted the construction of the branch-detecting
semipositive real-PL minorants, the use of the affinoid maximum principle,
the exact raw and regularized envelopes, and the deductions of non-pshness
and discontinuity.

## Exact submitted and returned bytes

| artifact | SHA-256 |
|---|---|
| exact statement | `10ac70696f69b1ed18ae1522c0b065fe9240d8f921b9db258201c9e8a7b509e1` |
| exact proof | `21fc22e5b1f3b3084f29df412a57485131e46ca160cf168db18da8a3e2559fc7` |
| combined candidate | `e46a8c4449d6a636361aafa95257c67c6b56426e24d8fa46d2adffcbb0845eab` |
| request | `9ede30e4244eec02e889377b276b48030d75431324a2b2a04c254dd000e13dc1` |
| API response | `c8ac792474289be20183a6e2c3f8822f0c0bca335cc6f31f07e0bd1004b583bc` |
| HTTP headers | `872d72a5249b0b3b4e8d1f028abc68b647bafec5136fc92d1f889450090cdf8d` |

The returned proof digest equals the exact proof SHA-256.  After integration,
Chapter 15 lines 3750--3802 compare byte-for-byte with the exact statement,
and lines 3804--3976 compare byte-for-byte with the exact proof.

## Preserved production artifacts

| artifact | SHA-256 |
|---|---|
| aggregate manifest | `dbce79d62ecf129b91f3632256410827f87ad35e778adb7084a45192ae8f6ddb` |
| aggregate verification | `1536e76cac0a31acea172d397b084a819e439bd3dba6fa02db9ebf147b7bc72c` |
| item verification | `18c426cfb63d59b2c42357c7272c24c1c2b0d242e79ad2f7814095981a568663` |
| item log | `bc56ee5984fe0226795258bbc165db4f0661fdcd2efbaa00682eeb34430c3c54` |
| process guard | `a4d763a0930c6433891b3f641bf9960592d12ff1100ded704d5ee04b5a9ddec0` |
| child guard | `9e92521951fcb84e523bc71ad06c4424ce8ff548d73ffd795ff9e6cb9a483d0a` |

## Mathematical scope

The theorem disproves, in the unrestricted local setting, the assertions
that usc regularization of the raw local-FS/semipositive-real-PL envelope is
classically psh, CLD-v2 psh, or continuous.  The obstacle is continuous and
finite, and the domain is a reduced strict nodal affinoid curve.  The
already-usc raw-envelope theorem remains valid.  No positive classification
for normal or analytically unibranch domains is asserted.

The three unconditional universal assertions are disproved.  The sharper
P03.1--P03.3 classification atoms remain open, beginning with normal and
analytically unibranch domains.  At this integration stage the live inventory
contains 16 Chapter 72 problem environments, 17 book-wide, and 58 active
atoms.

## Exact-current live file ledger

| live file | SHA-256 |
|---|---|
| `README.md` | `24639111fed82847d6f23d0a6629432e77f0533cf58effa0866ee8bb49ea6fc0` |
| `RESEARCH_QUESTION_LEDGER.md` | `1482ee5c57076b1ea8450de93e0e848c8316afed66589209eae53e063b7a7631` |
| `manuscript/appendices/appL_provenance.tex` | `6ab1b0c9bd725c876545bd74860efa10840a086bf456517294ba0b8cb96de9bd` |
| `manuscript/editorial/chapter_status.md` | `8762ed8233796c394d0b8a9a92b4bfd410d3a90dce608c744c2fbed6991fca3f` |
| `manuscript/editorial/major_open_problem_program.md` | `5b642243da7814f5ddde22c93cf3015d61e66e9d0e0f8d062003092b44b18b5d` |
| `manuscript/editorial/mathematical_revision_log.tex` | `be61d71886554cb44d5147af1ed487d1ce73302e7d1d7cad799765e371df6900` |
| `manuscript/editorial/open_problem_atomic_inventory_20260824.md` | `3f38b379194413aea61134a6386a0be6cdcfa5023df30c1939279e2cda83ad76` |
| `manuscript/editorial/rethlas_r3_report.md` | `9418f2e5ddd8447f88419f4222b2a72cae410d09edbef306576dbb28ec6c702b` |
| `manuscript/editorial/rethlas_verified_results.md` | `9d14cafa0ca7bf26a293de06e2ce62fabe6e15f1b6b0f5b5d835ba267bccc5ab` |
| `manuscript/editorial/theorem_provenance.md` | `416cb6d170bcadf57c691c523e50780bf98d7a3a842f2a66e56d790f56c51284` |
| `manuscript/parts/part2/ch15_poincare_lelong.tex` | `128bb1b4dc3bfc590e1860922b377340bcddff477c8e99c7b81e088769670c15` |
| `manuscript/parts/part6/ch70_local_valuative_psh.tex` | `fddd7c7ac8619b3251dc45d7a5e16c4ed15d8a32153cbbdb45c6e638ffed920c` |
| `manuscript/parts/part6/ch72_major_open_problems.tex` | `4494f7e3cc787fb3e4d51d363992901066ed5ac9cc035683a3a786ac44b10561` |
| `output/open_problem_packets/local_fs_envelope.md` | `26702c2f512e7029f7b19271517682060b5c8fbe1d8bb1160cd344895b1a5275` |
| `output/open_problem_packets/reference_pack_manifest.tsv` | `0013bb4e02fdc762faf2fabdced32fb9ddb0caaf9f988b9473a5fbc322fd112f` |

## Static gates

- Exact live statement and proof byte comparisons: passed.
- Literal problem environments: Chapter 71 has 1, Chapter 72 has 16,
  hence 17 book-wide.
- Active inventory: 58 atoms, with tier counts
  `T1=0`, `T2=9`, `T3=15`, `T4=17`, `T5=17`.
- No exercise environment and no optional name on theorem-like environments.
- The obsolete active label `prob:frontier-local-envelope` is absent; the
  sharper active label `prob:frontier-unibranch-local-envelope` occurs once
  in source and is emitted by the converged build.
- The new proposition has no optional name; internal prose references use
  `\Cref`, while equation references remain `\eqref`.
- `git diff --check`: passed before the whole-book build.

The whole-book PDF and log hashes are recorded separately in
`manuscript/editorial/current_source_build_20260825.md`.  This receipt does
not enlarge the production-verified scope or assert novelty or priority.
