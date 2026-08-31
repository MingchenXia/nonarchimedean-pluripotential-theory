# Mechanical validation only

Date: 31 August 2026. No mathematical or production verdict is implied.

The standalone source was compiled with three `pdflatex -draftmode` passes and one intervening BibTeX pass. Every command exited successfully. Initial unresolved citations were resolved by BibTeX and the subsequent passes. The final log has no undefined reference or citation, LaTeX warning, overfull box, underfull box, or error. It reports five draft pages. No PDF was created, rendered, or visually inspected.

Draft directory: `/private/tmp/p143_nef_closure_draft_20260831.lqoL92/`.

Build command from this dossier:

`pdflatex -draftmode -interaction=nonstopmode -halt-on-error -output-directory=/private/tmp/p143_nef_closure_draft_20260831.lqoL92 main.tex`

The BibTeX command was `bibtex main`, run in the draft directory with `BIBINPUTS` set to this candidate directory followed by the normal search-path separator. No TeX permission setting was changed.

`check_packet.mjs` is read-only and checks:

- 12 unique internal labels and 20 references, all resolved;
- all three citation keys against the local bibliography;
- sizes and SHA-256 hashes of all seven pre-existing source/dependency inputs;
- absence of a PDF and final draft warnings;
- after freezing, every `MANIFEST.json` entry against its exact bytes.

`CHECKS.json` records the pre-freeze checker result, so its `manifest` field is null. The manifest is written last to avoid a circular self-hash. A subsequent read-only run checks its entries without rewriting the frozen report.

This dossier contains newly authored sources, not a replacement of any live chapter. There is therefore no live-chapter patch. All predecessor candidates and audits remain unchanged. Independent review and the existing production gate remain outstanding.
