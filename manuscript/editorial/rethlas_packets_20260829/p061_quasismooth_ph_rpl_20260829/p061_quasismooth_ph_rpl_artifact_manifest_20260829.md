# P06.1 artifact manifest

Freeze date: 29 August 2026

This manifest records the exact mathematical core, independent audit,
production-verification evidence, and live-integration record for P06.1.
The verified statement and proof retain the exact bytes checked by the
production service.

## SHA-256 ledger

| File | Bytes | SHA-256 |
|---|---:|---|
| `README.md` | 550 | `1cdfcbdc65e5a988fe915c9b8a4406a96084aa870fefe7927d6f71d2e1cfbf8c` |
| `p061_quasismooth_ph_rpl_statement_20260829.tex` | 1977 | `0b1b4d161e3b85d342d7be88234a8ed27bfe74be4d24a639ff0456373a7a39e9` |
| `p061_quasismooth_ph_rpl_source_aware_proof_20260829.tex` | 9556 | `fdc6abcc4988644656892172fbdbda4178cb86ca710fd0122a90947e598b0b8b` |
| `p061_quasismooth_ph_rpl_production_problem_20260829.md` | 5323 | `2db9c297e35ce93953f7eb3b67bed13f298818efba6352d6248818de8e78c919` |
| `p061_quasismooth_ph_rpl_primary_source_ledger_20260829.md` | 8547 | `38f8c6060a3584428795ddcd6dc0ec192315cd592d08513c2b0f31e55503c0df` |
| `p061_quasismooth_ph_rpl_hostile_scope_audit_20260829.md` | 6184 | `a9e499c9be6da120e75bb07128c996255244c5e81e058a46b79f8ad62cc6ad9b` |
| `p061_quasismooth_ph_rpl_compile_20260829.tex` | 2005 | `261031e01991071abe7ac10a78e3374e65a8dcf539fa182f649056e2a434cb1c` |
| `p061_quasismooth_ph_rpl_compile_20260829.pdf` | 238339 | `e5afb3ee20c52c99978f574bc3f1f722a0b317be14a3e6fb4fcbdb79de059716` |

## Production evidence

| File | Bytes | SHA-256 |
|---|---:|---|
| `p061_quasismooth_ph_rpl_rethlas_receipt_20260829.md` | 2662 | `208435e4e5a809709e428267cbd36b78f7d40e7dc6bf961d8c48c1fad0687026` |
| `p061_quasismooth_ph_rpl_run_20260829/request.json` | 12467 | `2bb46b0881e5b42bfabeb33aa6c29ab158572819b25b60d96e7d169f619eb761` |
| `p061_quasismooth_ph_rpl_run_20260829/response.json` | 820 | `2ee6f3ed4f7242b0988ae8a79c8a574a75377e339c2c6965cf3d1b8e55ffce7e` |
| `p061_quasismooth_ph_rpl_run_20260829/headers.json` | 183 | `f083873a81abae3c18ecca18bee7c8bcfafebb461756233684b77cfe00c0039b` |
| `p061_quasismooth_ph_rpl_run_20260829/service_result/manifest.json` | 1361 | `055e0f05f57a9943641df1c29077fcc6f06bae3758a290189c6398c79c0a1e3e` |
| `p061_quasismooth_ph_rpl_run_20260829/service_result/verification.json` | 964 | `5a773bd005f7992c0d19afd1929ea0149816596a612c669c681b1fc31311aad0` |
| `p061_quasismooth_ph_rpl_run_20260829/item_round/log.md` | 441 | `d36dba197d1c632abc23f4603ae9b4f6dff0ebbe6b3bfa59b67a2acda37626e1` |
| `p061_quasismooth_ph_rpl_run_20260829/item_round/process_guard.json` | 558 | `9e86a1bb869e6ecdfe0f54f30afa1ab084cfce91b86a3f5aeaca86558956eb6c` |
| `p061_quasismooth_ph_rpl_run_20260829/item_round/process_child_guard.json` | 359 | `27de866df1cb54a11935b90ed7cd0dd48537a9302e3265188a7a75535fa464c4` |
| `p061_quasismooth_ph_rpl_run_20260829/item_round/verification.json` | 917 | `a570c7aba22b5361535f777b1e0aebf0ba19f05f66a64893cf463b102a223a5b` |
| `p061_quasismooth_ph_rpl_run_20260829/busy_attempt1_request.json` | 12467 | `37f74b6a44ace9b6e5c86061eb1f84dc61fbf1dcd7d2361713b8a2102ff4005c` |
| `p061_quasismooth_ph_rpl_run_20260829/busy_attempt1_response.json` | 41 | `776da9afe958a1c91fb5ec0edbb658e22fc67e37bde3e8ecb212eabc1d3a82d9` |
| `p061_quasismooth_ph_rpl_run_20260829/busy_attempt1_headers.json` | 182 | `ce9f0e8542913a21a587b4cad40ae97f1fa82fc2561b745a5ec75b976db050b6` |

The initial busy response did not dispatch a model and is preserved only as
operational history.  The controlling production result is run
`20260829T043457Z_0b1b4d161e3b`, item
`pi_7cd35ebd843cf80a7cd696bb`, final `correct`, with zero critical errors and
zero gaps.

## Integration record

| File | Bytes | SHA-256 |
|---|---:|---|
| `p061_quasismooth_ph_rpl_live_integration_map_20260829.md` | 4444 | `5bdb120415e9bdbfff5b28d3641572ae2e4cdf42078bdc7c9ea13bea384aa3d6` |
| `p061_quasismooth_ph_rpl_ch18_insertion_20260829.tex` | 2010 | `1329d236be4384a4a0d3a81f67afe6f24ed0018338e22e0d03688d365105d2fb` |
| `p061_quasismooth_ph_rpl_ch18_ancillary_updates_20260829.tex` | 2787 | `83761a5b88c648a56d6e847b43adfe86f70d40a58646d38c0785329934ff20e2` |
| `p061_quasismooth_ph_rpl_ch72_narrowing_20260829.tex` | 3083 | `0c3df24f9ee0e19a1a0f54e195a4f35ade1e1b86a762319a55c84ec5b9b0390c` |
| `p061_quasismooth_ph_rpl_inventory_narrowing_20260829.md` | 1730 | `a746a6d3e9d44a5008798a6b9b3bd33a145fbaf31272724a6a268e56853c7ace` |
| `p061_quasismooth_ph_rpl_appL_narrowing_20260829.tex` | 3970 | `c1f465811fd7596dd6ccdf458c6e632f470858169b3281f147a6aa170589caab` |
| `p061_quasismooth_ph_rpl_bibliography_additions_20260829.bib` | 723 | `d9df7072fdc6404670c9a6a9e6eee6b5f73fbede3800f6504be08e40d4a9146d` |

The inspected primary-source PDF hashes are recorded separately in
`p061_quasismooth_ph_rpl_primary_source_ledger_20260829.md`.
The manifest's own hash is omitted from its table by construction and is
reported in the packet handoff.

## Standalone compile

Run from this directory:

```text
latexmk -g -pdf -interaction=nonstopmode -halt-on-error p061_quasismooth_ph_rpl_compile_20260829.tex
```

- `latexmk` 4.70b.
- pdfTeX 3.141592653-2.6-1.40.22 (TeX Live 2021).
- Exit status 0; all targets up to date after the final forced rebuild.
- No LaTeX or package warnings, overfull or underfull boxes, undefined
  references, multiply defined labels, or fatal errors in the final log.
- No optional theorem names occur. There is no differential notation in the
  packet, so the requested `\mathrm d` convention is vacuous.

## PDF diagnostics

- PDF 1.5, four A4 pages, 595.276 by 841.89 points, 238339 bytes.
- Unencrypted; no forms, JavaScript, images, page rotation, or suspect
  objects.
- Sixteen Type 1 font entries; every font is embedded and subset.
- Ghostscript null-device validation exited 0.
- Poppler text extraction exited 0 and retained all theorem, proof, and
  bibliography text.
- Poppler rendered all four pages at 144 dpi. Visual inspection found no
  clipping, overlap, missing glyphs, broken cross-references, or illegible
  text.

## Quarantine check

The P06.1 statement and proof were frozen before any P06.1 live promotion.
Concurrent P06.2 integration changes may already be present in the live
chapter and inventory; they are outside this packet and do not alter any
hash in the ledger above.
