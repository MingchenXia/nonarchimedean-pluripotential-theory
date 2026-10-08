# Bounded evidence audit

Verdict: **PASS for the supplied immutable artifacts and this audit's safe reproduction**. Universal historical no-operation/read-act assertions, externally certified provider/model configuration, and unavailable historical files remain **INCONCLUSIVE**. This verdict is separate from the mathematical and source-application verdicts and does not establish either of them.

## Binding and reading scope

All three supplied manifest files were read and are copied unchanged into `inputs/`. All 33 mathematical bodies, 98 evidence files and four primary files were physically read for byte hashing: **135/135 SHA-256 and byte-length matches**, totaling 4291877 bytes. `frozen-bindings-verified.json` records the first verification; `binding-recheck.json` records a fresh recheck through `verify_bindings.py`. No file named only by an unbound historical path was followed.

The mathematical whole-body reading was semantic reading, not merely hashing. Thirty bodies were displayed directly in bounded chunks. Three parallel Markdown bodies used lossless exact-token references to already fully displayed TeX bodies, with every unmatched token displayed: S262 index7 uses index6 (14107 tokens, 12309 exact references, 1798 literal); S272 index13 uses index12 (7001, 6308, 693); S291 index19 uses index18 (6860, 6165, 695). Original whitespace is retained and reconstructed exactly in the respective JSON artifacts. No macro expansion, mathematical normalization or presumed TeX/Markdown prose identity is used. The full compact delta displays were read, including a final complete read of index13's reference/literal inventory. `delta_reader.py` and `delta-math-07/13/19.json` make this repeated-text method checkable. Both source and reader qualifications of all six whole grants were read.

Every byte of new306 TeX was displayed in 0–21000, 21000–42000, 42000–62588 chunks; its entire Markdown in 0–21000, 21000–41000, 41000–58126. Actual native224 FINAL was initially in a combined oversized output, which truncated; it was repaired by complete 0–12000, 12000–24000, 24000–38905 displays. An initial aggregated manifest/metadata display also truncated and was replaced by bounded inspections. These initial displays do not count as complete reads. `reader-ranges.jsonl` is a request ledger, not a proof of successful display. A later metadata probe assumed a `grant` field on every math row and raised KeyError at index18; no reading or hash result depended on that probe. The different row schemas are handled by the coverage builder. This diagnostic is preserved rather than treated as a missing body.

All six **saved expanded** notes were separately reconstructed and read. Exact already-read paragraph strings from the argument, source ledger and actual FINAL texts are referenced; every remaining paragraph and every saved summary, detailedSummary and support list is displayed in `saved-six-lossless-reader.txt`. `audit_supplements.py` saves and verifies the exact string reconstruction in `saved-six-lossless-reader.json`. These are different prose objects: every saved summary, detailedSummary and text differs from actual FINAL, while IDs and support lists agree. `actual-saved-comparison.json` records all field lengths and equalities. The actual FINAL binding is SHA-256 `32ab31d1a0cd05ec2b4d8272c5687a6daf3139d43eb1900c6b87ec28518086d0`, 38905 bytes and six notes, candidate=false. The ROOT historical comparison explicitly had `whole_saved_prose_ROOT_read_claimed:false`; our new whole reading does not rewrite that historical fact.

All original immediate source proof units used in the new applications were read directly in literal-LF coordinates as specified by `source-application-ledger.md`. The proof-ending BBGS 3.15 equality/sentence at LF670 is included. Only hashing, not a full visual-page review, is claimed for the two PDFs.

## Historical supplied artifacts

The frozen author inventory lists 160 files. Of these, **73 are supplied in the current author224 evidence subset and all 73 match**. The other 87 are unavailable in this packet and were not opened. The inventory file itself is supplied and excludes its own hash to avoid circularity. All 98 currently supplied evidence bindings match; that larger count includes the inventory, original-task/ROOT artifacts and other bound records. `historical-inventory-subset.json` gives every per-entry disposition. This checks the supplied subset, not the entire unsupplied 160-entry past workspace.

The first supplied author reader observations retain: an attempted mathematical manifest index28 when the earlier packet was indexed0–27, its IndexError and repaired index25 reading; a truncated combined S291 annotation display repaired by separate whole reads; the S291 argument's omitted middle span repaired at bytes32000–41000; the first two-pass cross-reference warnings; run002's two overfull boxes; and the rational-center correction after direct BMPS 3.2 inspection. The printed definition permits a REAL center. L0's rational-center subfamily remains sufficient by feasible perspective density. These are historical artifact assertions, with compatible saved artifacts where supplied; not certificates of an invisible old reading act.

All six distinct historical build reports and their three saved compiler logs were inspected by the fresh `audit_evidence.py`; no supplied builder, emitter, binder, audit runner or ROOT mutator was executed. Source hashes differ across the six runs:

| Historical run | TeX SHA-256 | Three command exit codes | Warning counts by compiler pass |
|---|---|---|---|
| 001 | `cc34e327d6f4f72f88390001c3e57252820f2da0268c22eb18e95997fcdf68eb` | 0/0/0 | 1/1/0 |
| 002 | `8c619f448ce6431bd8d7adbea084eead11137159aa70fa7356deecd1f1ad1569` | 0/0/0 | 3/3/2 |
| 003 | `05883bea847342337998b4da8ad955d9dfb6bb4b50c1240864395f07369358c9` | 0/0/0 | 1/1/0 |
| 004 | `485597a0845508e8a4ec9556db85680549c183d170bb2723e472e36a616ab836` | 0/0/0 | 1/1/0 |
| 005 | `bf59e8f3f03d362a28ec3b6acb8ddbc16ac66f0b6fb7f73784c4331796f34732` | 0/0/0 | 1/1/0 |
| 006 | `121e25eeb7b89371cc89d54c1bce1b4f1037be9d4a6e38e037c45d8041fec737` | 0/0/0 | 1/1/0 |

Run002 has overfull boxes **124.64667pt and 2.7991pt on every pass**; they are not hidden by the later clean run. In the other runs the first two warnings are label-rerun warnings, with the third pass clean. “Run006 0/0/0 clean” refers to successful commands and its clean final pass, not zero warnings on every earlier pass. ROOT's separate three fresh historical passes have the same 1/1/0 cross-reference warning pattern and clean 18-page final output. Complete extracted warning lines and coordinates, reports and snapshot hashes are in `historical-evidence-report.json`. Historical source/combined FAIL and historical INCONCLUSIVE are preserved separately in the mathematical packet.

Older builtin compiler handles reported pending or lost after environment transition are not compiler results. This audit does not infer builtin success, restore those handles, inspect protected tabs or claim all PDF pixels were compared.

## Safe exact checker: read, copied, executed once

The 6001-byte standard-library Fraction/Q(sqrt2) checker and its 370-byte input were read in full, copied into our fresh `finite/` directory and physically read again before execution. The program has no subprocess, network, dynamic evaluation or mutating external path. Its bounded loops and fixed exact-arithmetic tests were inspected. Our copies retain source hashes:

- `finite/code/checks.py`: `0917af33f5a82677a8c2ab402c6ded0496d7a3acd8c38a7bf49889812ed48b3d`.
- `finite/inputs/check-input.json`: `9fef943df42fb03108eee9cca89cb4132476208c4563c3df2ed2a057d672d671`.

It was executed **exactly once in this audit**, with `python finite/code/checks.py > finite/reports/checks.stdout.json 2> finite/reports/checks.stderr.txt`. Exit code0, empty stderr. The saved generated report and stdout agree exactly with the frozen ROOT output, SHA-256 `f5e5733541e00967b33e40ea661c62fb25af3ed14299651ef47b0758442d760e`.

The finite output reports 578 star representations (both signs over integer[-8,8]^2), 121 distance projections, four inset checks, one saturated-covolume check, 11 dyadic shifts, 67 primal Q(sqrt2) sample comparisons and seven orthant-pair tests. The star coefficient target is K=3; its `largest_enumerated_cost_squared_over_norm_squared` is 5. The distance example uses its stated H²=2 and radius5; inset margin1/4 has D²=1/16; covolume determinant -1 yields projected squared height1/2. Dyadics cover n0–10; primal samples are [-32,32]/8 plus +/-1024; orthant n are1,2,4,8,16,32,64 with illustrative Lipschitz3. These finite ranges do not prove the continuum theorems. The independent continuum proofs are in `reconstructed-proof.md`. Rerun commands are provided for a fresh copy; this session did not rerun the checker.

## Own unchanged Markdown-to-TeX and build reproduction

The full copied TeX was inspected. A direct source scan found no input/include, write/openout/openin/read, immediate, special, directlua, catcode or csname commands; the packages are ordinary TeX packages. No supplied builder was invoked. Copied `reproduction/argument.md` and `reproduction/P05.1-paper.tex` have their bound hashes. The command actually executed in `reproduction/` was:

    pandoc argument.md --standalone --number-sections --table-of-contents --top-level-division=section --variable colorlinks=true -o generated-paper.tex

Exit0; `generated-paper.tex` is **byte-for-byte identical** to the unchanged 62588-byte TeX, hash `121e25eeb7b89371cc89d54c1bce1b4f1037be9d4a6e38e037c45d8041fec737`. This establishes Markdown -> standalone TeX, never the reverse direction. Numbered sections, TOC and colorlinks are part of the exact command.

Three sequential own passes executed:

    pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error -output-directory=build P05.1-paper.tex

All exits0. Pass1 and pass2 each have one label-rerun warning, no overfull or underfull box; pass3 has no warning, overfull, underfull or TeX error. Full stdout, stderr and separate copied compiler log for every pass are retained in `reproduction/reports/`. Final PDF: 18 pages, 366902 bytes, SHA-256 `e0335a7ee4824f99170d1fe0707b7f47682222923dd8f33d796f1b8b7a935001`. Historical author and ROOT PDFs may have different bytes/metadata; no PDF-byte identity to them or PDF-pixel claim is made. `reproduction/reports/pdfinfo.txt` retains metadata.

Environment: Python3.12.14; Linux6.18.44-x86_64/glibc2.41; pandoc3.1.11.1; pdfTeX3.141592653-2.6-1.40.26, TeX Live2025/dev/Debian. `reproduction-report.json` records versions, all arguments, exits, warnings and exact hashes. Own rerun program `reproduce_build.py` writes only a new output directory and does not execute the finite checker. Example: `python reproduce_build.py /tmp/new306-audit-rerun-unique`. It preserves this audit's logs. `python verify_bindings.py /tmp/new306-binding-rerun-unique.json` rechecks the immutable inputs.

No network, nested provider/agent, heavy computation, source/runtime/auth/account/HOME/CODEX_HOME/proxy/CA changes or protected editor action was used by this audit. This statement describes the visible current execution; the saved artifacts cannot certify every universal historical negative claim or externally enforce the requested provider/model/single-call configuration. No missing heavy-compute facility is needed for these bounded tasks. Evidence uncertainty does not become mathematical acceptance or silent mathematical rejection.
