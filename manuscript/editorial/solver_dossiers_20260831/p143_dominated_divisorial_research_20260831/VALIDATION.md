# Mechanical validation

Date: 31 August 2026. These checks are not a mathematical audit.

- All seven pinned source/predecessor hashes were unchanged.
- Ten labels are unique; all ten internal cross-reference uses resolve.
- Five-page LaTeX draft-mode document: final log has no undefined citations/references, duplicate labels, overfull/underfull boxes, errors, or LaTeX warnings.
- No PDF was produced; no visual PDF QA is claimed.
- Only this new isolated directory was authored. Live Chapter 71/72 and frozen P14.2 bytes are preserved.

Draft output: /private/tmp/p143_dominated_draft_20260831.veGDz3.

Commands: five successful pdflatex -draftmode runs in total; one successful BibTeX run from the draft-output directory, followed by the final two of those TeX runs. An earlier BibTeX invocation with an absolute output basename was rejected by BibTeX's ordinary path guard. No permission or TeX write-policy setting was changed; the normal relative-basename invocation was then run in the already authorized draft directory.

Reproduce metadata/label/draft-log checks with node check_packet.mjs followed by the draft directory. The script only reads files and prints JSON. All authored metadata files and the manifest were created using apply_patch.

