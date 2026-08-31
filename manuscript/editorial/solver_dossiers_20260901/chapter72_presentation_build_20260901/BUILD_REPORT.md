# Chapter 72 presentation-only revision and clean build

Date: 1 September 2026.

## Change and mathematical boundary

Two historical verification-record blocks (142 source lines) were moved from the Bedford--Taylor subsection of Chapter 72 to `manuscript/editorial/chapter72_bedford_taylor_verification_archive_20260901.md`. No mathematical sentence, hypothesis, equation, problem environment or cross-reference was changed by that relocation. The base revision is `7bd98db93381af527abeb04f5148118bf0950aae`.

The original chapter SHA-256 was `bf3d77f44406913325d358a312a1371d52fa488d5606378b5b419707fe593570`; the revised chapter is `584f00b14baeec1dbe78641b34f0d7e889e1a6cf4ebe82cef927df2c915e2115`. A mechanical whole-file reconstruction and independent read-only review by `/root/p213_skeletal_hostile` confirmed only the two deletions, with all 14 problem bodies and all 285 combined label/cref/Cref/eqref tokens unchanged. In particular all 47 eqref calls are retained.

The reviewer found two archival formatting details: the first closing Markdown fence needed its own line, and the initial line locators counted adjacent blank lines. These were corrected without touching the live chapter or the mathematical contents of either archived block. The final archive SHA-256 is `7e9972d246f967ce68bf1bb0ac1af7888d06a61395d01045cbfb797b36582b1a`.

This is not a new proof review or a Rethlas gate. Historical verification assertions remain historical; moving them does not independently revalidate them. The new local-access research remains outside the live mathematical text. No atom is retired. The README's current inventory was synchronized to 51 editorial atoms in 14 problem environments, with tiers 0/5/12/17/17; older dated milestones were preserved.

## Clean source build

The mechanical `prepare_build.mjs` snapshots local source files and recursively follows literal TeX inputs, including accepted theorem bodies stored in editorial directories. It does not copy the whole research tree or unrelated reference PDFs.

An initial 112-file snapshot omitted those editorial inputs; its clean build correctly stopped at a missing Chapter 14 input and produced no PDF. The script was corrected to follow the actual input graph. The resulting 216-file snapshot is `/private/tmp/nappt_ch72_presentation_20260901_ItfrwR`; all snapshot-file bytes still match the corresponding current live inputs after compilation. `SOURCE_SNAPSHOT.json` records these inputs. Its recorded archive hash predates the Markdown-only fence/line-locator correction; the archive is not a TeX build input, and its final hash is recorded above.

Command: `latexmk -silent -pdf -interaction=nonstopmode -halt-on-error book.tex`, with the project's latexmkrc, BibTeX and MakeIndex. The completed process returned exit code 0. The final output contains 3,476 pages and 16,606,124 bytes. Its SHA-256 is `d7b7bbff8e567f4156e4cc201df8979813cd3b952c70658317bce75d658b0b4d`.

Final-log checks:

- no missing inputs, TeX errors, undefined references, undefined citations, or multiply-defined labels;
- zero overfull boxes;
- 1,018 underfull-box notices remain across the existing manuscript, so this is not a warning-free or whole-book typographic-perfection claim;
- the standard class-name notice (`style/svmono` versus `svmono`) remains;
- BibTeX reported no warnings or errors.

## Visual inspection and output

Following the PDF skill, root rendered and inspected the complete changed subsection and its transition pages: physical pages 3290-3293, labelled 3222-3225. Equations (72.35)-(72.36), Problem 72.4.3, cross-references, headers, footers and the transition to Section 72.5 are legible, with no clipping or overlap found. This is a visual check of these pages, not all 3,476 pages.

The title page was inspected and PDF metadata has an empty author. The actual acknowledgements page (physical page 7, label ix) was inspected and contains only its heading. A first locator selected physical page 9, which is the contents; this was recognized and corrected before the acknowledgements check was recorded. No body text was added to the acknowledgements.

The new current PDF is saved separately as `output/pdf/Non-Archimedean_Pluripotential_Theory_current.pdf`; the older release PDF and `manuscript/book.pdf` are left untouched. Generated PDFs remain excluded from Git under the existing repository policy. The source revision and these reproducibility records are committed separately from the previous research archive.
