This directory contains an unverified partial research deliverable for original P16.7. The original target remains unresolved here; `candidate=false`.

- `P16.7-paper.tex`: full standalone paper, with complete proofs of the partial claims and explicit original-scope limitations.
- `whole-proof.md`: whole proof companion generated from the complete paper body.
- `source-application-ledger.md`: exact applications, hypothesis checks, proof-reading coverage, recursive foundations and missing primary evidence.
- `scope-and-verdict.json`: original completion verdict and coverage of each required quantifier.
- `sources/`: unchanged task/manifests and preserved whole applied primary CLD source; whole GR v1 preserved for scope reconnaissance.
- `evidence/`: literature retrieval outputs, actual-page images, bounded exact diagnostics, lexical checks, environment and SHA-256 inventory.

From this directory run:

```sh
python scripts/prepare_evidence.py
python scripts/diagnostics.py
python scripts/build_artifacts.py
```

The first command requires the original immutable packet in its preserved parent location and copies only authorized data/text/PDF files. The other two use this directory and Python's standard library. No supplied code is executed. TeX compilation is omitted because the user reserves compilation to ROOT. The diagnostic is a finite exact calculation, not an analytic theorem verifier.

The main partial findings are a proper smooth analytic quotient with an exact integral-period obstruction, genuine bounded mixed CLD products and comparison, a bounded potential with an atom outside the canonical skeleton, and a completely explicit separable product-measure equation with energy and circle-envelope orthogonality. The rigid-point counterexample concerns only the proposed restricted dual-energy construction. Actual nonalgebraizability and the full all-support analytic finite-energy theory are not claimed proved.
