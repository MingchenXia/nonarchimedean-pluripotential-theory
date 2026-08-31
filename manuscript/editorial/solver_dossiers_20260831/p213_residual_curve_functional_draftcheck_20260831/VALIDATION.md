# Frozen residual-curve functional source: draft-only validation

Date: 31 August 2026. Builder: `/root/p081_weighted_repair_fresh`.

The frozen statement, proof and bibliography compile successfully through the new `main.tex` wrapper. Three `pdflatex -draftmode` passes and one BibTeX pass all exited zero. The final draft log contains no undefined references or citations, LaTeX warnings, errors, overfull boxes, or underfull boxes. Its only expected output notice says that draft mode is enabled and no output PDF is being changed. The draft spans five pages. No PDF was produced or visually inspected.

## Frozen inputs

The wrapper reads the original statement and proof in place using absolute paths. BibTeX reads the original bibliography through the `BIBINPUTS` search path; no source copy or substitution is used.

| Frozen file | SHA-256 |
| --- | --- |
| `statement.tex` | `5ad73a96dd4e41296003e2824711cf7d6301aa489fdc67ed11a2158682d135fc` |
| `proof.tex` | `209ce1db0b33f460952e7c423c09baa58ab2f6cdc14a3d55b9310ddcbde9b224` |
| `sources.bib` | `5e1184530fa73441223b7ad051e826013bb5afbdddc887c41f2e3b3a478bf288` |
| Parent `MANIFEST.json` | `175b64dfd4e08ad59dcb561928ab50172194e04af264c4641b49c8dcc0359278` |

Source directory:

`/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260831/p213_residual_curve_functional_interface_research_20260831/`

All four direct inputs and all 13 entries of the parent manifest were rehashed after the build and match. Hashing the parent sources is a byte-preservation check, not a new primary-source or mathematical audit. No frozen input, live manuscript, inventory, or earlier packet was edited. No git or production action was taken.

## Wrapper and command evidence

The first wrapper worked without repair. It supplies the standard AMS proposition/proof environments, mathematical symbols, hyperlinks and cleveref support, with A4 geometry and 28 mm margins. It preserves the sources' own `eqref` commands and all five labels. Six internal references resolve. `CLD25` is cited and resolves. `GRW16` is present in the frozen bibliography but not cited by these two inputs; this is not a bibliography error, and no artificial citation was added.

From this new dossier, the command sequence was:

1. `pdflatex -draftmode -interaction=nonstopmode -halt-on-error main.tex`
2. `BIBINPUTS=/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260831/p213_residual_curve_functional_interface_research_20260831: bibtex main`
3. Repeat the first command twice.

The ordinary initial unresolved references/citations disappear on the final pass. All four command outputs are preserved as `run1.out` through `run4.out`; `main.log`, `main.aux`, `main.bbl`, `main.blg` and `main.out` preserve the final generated evidence. No TeX permission policy was changed. Exact command exit codes are in `BUILD.json`.

`check_frozen_inputs.mjs` is read-only. It verifies the direct inputs, parent-manifest entries, references/citation keys, final warning state, and absence of a PDF. After freezing it also checks every local manifest entry. `CHECKS.json` was recorded before the local manifest existed and therefore has a null `manifest` field; the subsequent full manifest check does not rewrite that frozen evidence.

## Integration-only style notes and remaining gate

The frozen proof writes the exponential constant in ordinary math italic at lines 46 (`e^{-delta_p}`) and 171 (`e^{-a_p}`). At eventual authorized integration these constants should use roman styling, such as `\mathrm{e}`. These are style findings, not TeX failures, and the proof was not changed.

This dossier provides syntax/reference and byte-preservation evidence only. It is not an independent mathematical verdict, production verification, or authorization to integrate or retire any research question. The original mathematical and production gates remain unchanged.
