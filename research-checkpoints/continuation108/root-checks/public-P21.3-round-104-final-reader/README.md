P21.3 remains unresolved. This packet proves two reductions of the arbitrary-current step: an exact fixed-neighborhood exhaustion criterion and an exact scalar criterion with compact positive mass normalization. It establishes neither the missing density nor the scalar test certificates for general equal-curvature pairs, and contains no analytic counterexample.

- [Standalone paper](P21.3-paper.pdf) and [LaTeX source](P21.3-paper.tex).
- [Argument and literal primary evidence](P21.3-argument.md).
- [Exact status and remaining gaps](status.json).
- [Two canonical proof notes](notes.json), with the scalar criterion supported by the dual criterion.
- [External premises](premises.json), [frozen CLD passage bindings](source-manifest.json), and [public literature passage bindings](literature-bindings.json).
- [Finite integrity-check result](logs/verification.json) and [environment](environment.json).

Run `bash reproduce.sh` from this directory. The script preserves and checks the original input, reconstructs the argument and note register, and builds the paper with the already installed Pandoc and pdfTeX. It verifies URL-selected web passages as well as literal CLD source slices. It does not perform a mathematical audit.

The exact input bytes are in `input-original.json`; `task-original.json` preserves the parsed task, and `assignment-original.txt` preserves the exact assignment string. Public literature searches are selected, not exhaustive. The BGJKK PDF inspected here is the identified 2021 v1 preprint; no audit of its 2025 published revision is asserted.
