# CLD hypothesis corrections and clean whole-book build

Date: 1 September 2026.
Source comparison base: 8f62a8eb0487f9045d3a38209b4337ee7c274041.

## Mathematical changes

The Chapter 16 paragraph on CLD Corollary 8.6.7 no longer supplies a hypothesis absent from the printed statement or claims that arbitrary smooth multipliers preserve closed Bedford--Taylor currents. The proved locally constant case is unchanged. The replacement explains the closedness obstruction by the existing Leibniz rule.

The harmonic-chart positivity corollary now retains the skeletal Bedford--Taylor hypothesis of the compatibility theorem actually used. Its conclusion is written directly as positivity and closedness of dd((F composed with f)T). Smooth convex target approximation is followed by order-zero multiplication and weak continuity of the current differentials. The proof does not identify G-smooth approximants with ordinary smooth psh approximants. The harmonic continuity proposition explicitly retains ordinary CPsh membership of the differentiated potentials and follows from the previously proved continuity theorem. The broader source assertion is not presented as established by this argument.

Chapter 19's canonical-metric theorem is not weakened. Its positivity proof now uses the integral parlinear Raynaud coordinates and their negatives, whose zero curvature implies ordinary pshness by the existing residual-nef theorem. Finite maxima of affine functions and the explicit quadratic tangent-plane error give the convex quadratic pullback. The affine difference between the full metric weight and its homogeneous quadratic part is also included. Two uses of an algebraically closed-field comparison theorem are replaced by the applicable residual-nef theorem. This is a detailed proof of an existing CLD result, not a new general regularization theorem.

Root checked the primary CLD text at Sections 8.5--8.7, 8.11, 18.8.8--18.8.9 and 19.3.1, the actual source of the old references, and the relevant Chapter 17 residual criterion. A separate independent reviewer checked the precise final Chapter 16 and Chapter 19 bytes and their affected downstream references. This source/correctness review is not production Rethlas verification of a new research result. No new Chapter 72 research theorem is promoted and no open-problem item is retired.

The frozen independent review is preserved byte-for-byte in the sibling directory `p213_ch16_bt_multiplier_harmonic_source_independent_audit_20260901`. Its `AUDIT_REPORT.md` has SHA256 `f37d6fbc4b08ff4d6fab09b1fca8856804be9b363695d23bffa848eacff350b6`; its `AFTERPATCH_ADDENDUM.md` has SHA256 `d4a0d43b1ec1bc30e682a9016fa674faca863f4978f625a6b65c2ba418c5a48f`. Root read both reports and the source ledger in full, compared the complete reviewed live diff, and checked the archive and input identities. `ARCHIVE_QA.json` records the mechanical preservation checks. The audit notes a nonblocking source-citation-range imprecision at Chapter 16 line 1559; it is retained as an explicit future editorial item rather than changing the already reviewed and built source silently.

The scoped 23-file commit contains only the two corrected chapters, README, the build/preservation record and the exact independent audit. The staged whitespace check passes outside the frozen `EXACT_CHANGED_PASSAGES.md` and `REVIEWED.diff`. The latter retain their line-numbered blank-line spaces and literal diff context spaces by design; the all-file check reports those archival-format warnings. They were not stripped, since doing so would change the reviewed evidence and its checksums. No generated PDF or unrelated working-tree file is staged.

Final source identities:

- Chapter 16: 223897 bytes, SHA256 41333978fbce28644d1f63aac6431f763dd3f3cc1dd792faf1b20b43ab3a9e83.
- Chapter 19: 210866 bytes, SHA256 4d59d219eec46bea029d6d131e6f55c110a7fbf4c3f30be9dcf4147a4c5a6652.
- All 205/198 label definitions and all 60/130 existing eqref calls in those respective chapters are preserved in order. The new internal references use cref/Cref. The Chapter 72 source and atomic inventory are byte-identical to the comparison base.

## Build and visual QA

The first complete build, in `/private/tmp/nappt_cld_hypothesis_repair_20260901_45pIZg`, succeeded. During the full adjacent-page review root made the affine part of the metric weight explicit. That final mathematical clarification was incorporated into a second exclusive clean 216-file snapshot, `/private/tmp/nappt_cld_hypothesis_repair_20260901_LvcVnD`. The previous snapshot and PDF were not relabelled as final.

The final `latexmk -silent -pdf -interaction=nonstopmode -halt-on-error book.tex` completed with exit code 0. All 216 current live TeX-source/dependency hashes match the final snapshot after compilation. The final PDF has 3476 pages, 16611038 bytes, and SHA256 dd0aba9532b258b83af57a84c42d6209f1f9c90f9ba9511e3e2cca442530fc00. Its author metadata is empty. The title and acknowledgements source inputs were not changed.

Final logs have no TeX errors, undefined references or citations, multiply-defined labels, missing characters or overfull boxes. BibTeX has no warnings or errors; its diagnostic counter `warning$ -- 0` is not itself a warning. There remain 1018 underfull-box notices and the existing svmono class-name notice. This is not a warning-free or whole-book correctness/perfection claim.

Following the PDF skill, root rendered and read the complete changed passages and transitions: physical pages 793--794, 870--871, 891--892 and 1205--1207 (printed labels 725--726, 802--803, 823--824 and 1137--1139). After the final clarification, all nine final pages were rendered again. Seven render files were byte-identical to the images already inspected; final pages 1206--1207 were visually inspected again. No clipping, overlap, unreadable equations or broken references were found in this scoped check.

`finalize_build.mjs` validates the final source, PDF, log and rendering identities and publishes the current PDF only after preserving the former current PDF as a separately named backup. The stable output remains `output/pdf/Non-Archimedean_Pluripotential_Theory_current.pdf`. The older release PDF and `manuscript/book.pdf` are untouched. Generated PDFs and temporary renders remain outside Git under the existing repository policy; the source snapshot and QA record are versioned.
