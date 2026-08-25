# P11 projective-space Radon--Riesz counterexample: exact-live integration receipt

Date: 25 August 2026

## Exact-current production verdict

- Run: `20260825T051642Z_049da6197deb`
- Item: `pi_062d99c623958fae25885125`
- Model: `gpt-5.6-sol`
- Reasoning effort: `xhigh`
- Verification status: `final`
- Verdict: `correct`
- Checked items: 1 of 1
- Critical errors: 0
- Gaps: 0
- Adaptive round: 0
- Wrapper return code: 0
- Wrapper guard: `completed`
- Child guard: `completed`
- HTTP result: `200 OK`
- HTTP date: `Tue, 25 Aug 2026 05:16:41 GMT`
- Request deadline: `2026-08-25T06:45:00+00:00`
- Guard deadline: `2026-08-25T06:15:01.564269+00:00`
- Guard command SHA-256:
  `8b1f087634f4ac7af96cd6cf547c259f969f13bd8f4253a8295024daa808dc47`

The production verifier accepted the exact extracted live theorem and proof.
Its item report confirms that the transverse-initial-form specialization
proves pointwise weak convergence, the section-order computations give both
exhaustion values, and the degree-one hyperplanes give the uniform strong
distance lower bound.  The exact-current claim is confined to the theorem
and complete proof in Chapter 49; later editorial-only changes did not alter
those bytes.

## Exact submitted live bytes

| artifact | lines | bytes | SHA-256 |
|---|---:|---:|---|
| `p11_bj_radon_riesz_pn_live_statement_exact_20260825.tex` | 33 | 1190 | `049da6197deb627f55e5e469a246dce53154e121eb0a1b8206806ae8ec395518` |
| `p11_bj_radon_riesz_pn_live_theorem_proof_exact_20260825.tex` | 138 | 5601 | `d6e40fa3adedaccecc6a3af1f7258ee29b803ac9443a430e234be2a9571c9aa1` |
| `p11_bj_radon_riesz_pn_live_source_aware_request_20260825.json` | 5 | 7447 | `b021f7464d067b120a63649f4c3036d83cbc2bf0c8df341cd3e82fd3da3a75f8` |

The request strings were compared byte-for-byte with the extracted TeX
files before submission.  After all integration work, live Chapter 49 lines
2485--2517 still compare byte-for-byte with the exact statement, and lines
2485--2622 still compare byte-for-byte with the exact theorem-and-proof file.
The returned proof digest is exactly
`d6e40fa3adedaccecc6a3af1f7258ee29b803ac9443a430e234be2a9571c9aa1`.
The run context digest is
`291b41293f52596c8c16d9f0ead7984392a87d12316cfed51bce67e146a38ba7`,
the adaptive context digest is
`456009c025275665f059ee8db5c9143d0e7c1e69dbca94e3f02d1f3af698e2a0`,
and the item context digest is
`ce4856316e985a0edf4c5dc2387d1ca8f7fd7f6e8198da56ce1b00e9c2514cbf`.

## Preserved production artifacts

| artifact | SHA-256 |
|---|---|
| API response | `0167f0764596b707671d4928398a76aa157761addd46f1b5d7aaa38227db0331` |
| HTTP headers | `222fc723abf6d6377d580a5523cb014e0ce6d89098054f685ee68691ab1ae86e` |
| run manifest | `1e7a720b9c365bdacf830832af7128d901281d03524b87c24f308acd10f01074` |
| run verification | `ceea440dae3055e8cfb220605d4a9b4fde6973b1bc3d5f5aeb5e7e1add072796` |
| item verification | `a261e5915d1fb593ed68faf0e4a9dd012cb71e883ac686a820054866cd716d3a` |
| item log | `c7276f1c1e412deeb12cb6fa2203b6381e04ed0d63c09925680edee72ba64e67` |
| wrapper guard | `c183fe48d10cec203f7a8669e7c5cd8efa6babd44dc5ffb9587f9d0704ff9d79` |
| child guard | `1e17f955be628f450f5d39651e9df7656372bee1d454ad6b2ea9fbd9bbd0629e` |

The copied manifest, verification, item-log, and guard artifacts were
compared byte-for-byte with the verifier result files.

## Mathematical scope and history

The integrated theorem answers Boucksom--Jonsson Question 11.16 negatively
on `P^n` for every `n >= 2`, over an algebraically closed trivially valued
field of arbitrary characteristic.  The center is a linear line
`C = P^1`.  For `n >= 3` the weak limit is the exceptional valuation of the
blowup along `C`; for `n = 2` it is `ord_C`.  The moving point-blowup
valuations and their limit all have `T_{O(1)} = 1`, while their strong
distance is at least one.  The fixed-dual-complex positive theorem remains
valid: the moving centers escape every one fixed model complex.

The generalized frozen packet had already passed production run
`20260825T044839Z_326e2035bbb9`, item
`pi_9e222887262acc5d9fbc740a`, with final `correct`, zero errors, and zero
gaps.  The repaired `P^2` run remains a verified baseline.  The first `P^2`
run and its rejected proof remain preserved and quarantined; neither is used
by the live theorem.  No novelty or priority claim is made.

The authenticated Boucksom--Jonsson source PDF has SHA-256
`8d5975337f4ac88a475929ea6a436ec4a15d08715d5582bc0ba0eb3e07152c52`.

## Exact-current live file ledger

| live file | SHA-256 |
|---|---|
| `README.md` | `80bc856d8a611d6e5d9bf2f386665474e598e4c6d34959e2678fed99e2be396b` |
| `RESEARCH_QUESTION_LEDGER.md` | `451f81d9c7a25a387d1904b44002137c35043a2384ce69337270f7d58e4dafd3` |
| `manuscript/appendices/appL_provenance.tex` | `5eabe1d2ceeeab9d3cc2dd14113bd8dc65e59e0baacefb4dc8fee2bdd8e91811` |
| `manuscript/editorial/theorem_provenance.md` | `8308575c7915f181761785852fbb52d5663c4157aca44a2058cbfb120d499282` |
| `manuscript/editorial/rethlas_verified_results.md` | `ec20f6a01393a046b532f51b06e9156bb25991e65592059e5be1e85d3b55a853` |
| `manuscript/editorial/mathematical_revision_log.tex` | `171e04e9e551af76690f70e7a1de4d889d3a7c29db806bbd892192a624ec6db6` |
| `manuscript/editorial/major_open_problem_program.md` | `8d3c5512dab8e4e40aeb73ecb124cb7c1416461aa7e425a388de361239bb3910` |
| `manuscript/editorial/open_problem_atomic_inventory_20260824.md` | `23d91d3accf5028b0dab4946cfe88b3c5159bedf7498bc039f9f2b01e232b1a2` |
| `manuscript/editorial/chapter_status.md` | `14ad4f381a1e8277a9928af283b14457a38e92e84ece793552cb3f30f69d91ec` |
| `manuscript/editorial/part6_postexpansion_audit_20260824.md` | `2416ca0bdd43d0bc29d08262b6ddb14049d8ab2d35a685d617c5c614058da8b7` |
| `manuscript/editorial/rethlas_open_problem_attempts.md` | `b90c153a770a16c2e72d97672c2ec65d18495062a97e6ec0607ee7827c6cc947` |
| `manuscript/editorial/rethlas_r3_report.md` | `cfb9479d16945ab5b3929a56889a030da6f19057e9aa383f8b63e9aa8a7608ba` |
| `manuscript/parts/part4/ch49_linear_growth.tex` | `a0f3cf9d00ca5631e6b251d7d707bd0447d7b95434d570c58b6c008e32eacf43` |
| `manuscript/parts/part6/ch69_verified_extensions.tex` | `3f0d13906ac014362ae0415a10c39ff84118d4af4761ff6f4e1e94cd37bb1f02` |
| `manuscript/parts/part6/ch72_major_open_problems.tex` | `ce4bd882ca3be89245c372139b7e355dbf89d14a054c092394fb6d2e5a0bf753` |
| `output/open_problem_packets/bj_radon_riesz.md` | `d8795bd587fe50684a7bf45bcdb1cf49323c2393fde1851caa82ce086f98a843` |
| `output/open_problem_packets/reference_pack_unavailable_sources.txt` | `0caafd02f68f1b0c213acb4ad50ae8965b7f09be6eae80a62877240b3cd98384` |
| `output/open_problem_packets/reference_pack_manifest.tsv` | `27e801261fe6c2c4fba89e7e40a58ec3c989be11c41f4ecc20ddb428874099ea` |

## Build and static verification

- The exact-live two-page minimal TeX wrapper compiled cleanly.  Its PDF
  SHA-256 is
  `00aecea005434056d46a8b2132966f30d58bea35d31400445b7edbf7bff041cc`;
  its log SHA-256 is
  `c72347d42d5b0f2ee7c240605ab2e35f9da7a697112a87d22592181b20b35c9a`.
- The current whole book rebuilt successfully under `latexmk -pdf
  -interaction=nonstopmode -halt-on-error book.tex` and has 3119 pages.
  The PDF SHA-256 is
  `f696a63f54f605ebb6a44fdc1de5c07a45760aa1f6c4f314323df88f0d2c1e4b`;
  the log SHA-256 is
  `29c36801dd4f1b696845ca0af8cac12a957f22001aa1d2326020dc1c8b5bbc76`.
- The final whole-book log contains no fatal error, emergency stop,
  undefined reference, undefined citation, multiply defined label,
  duplicate destination, or overfull box.
- `git diff --check` is clean.  The formerly trailing whitespace in
  `output/open_problem_packets/bj_radon_riesz.md` is absent.
- Chapter 71 has one literal `problem` environment and Chapter 72 has 17,
  hence 18 book-wide.  The atomic inventory has 59 active atoms.
- The retired active label `prob:frontier-bj-radon-riesz` is absent.
- The Chapter 49 theorem has no optional theorem name and its complete proof
  is present.  Its new local cross-references use `\cref`, while equation
  references remain `\eqref`.

No commit or push was performed.  This receipt records an exact-current
integration and the final handoff state; it does not certify unrelated
concurrent edits in the shared worktree.
