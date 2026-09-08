# Validation record

## Exact replay

The v2 proof postimage at

    /private/tmp/p143_extended_arithmetic_repair_20260908.n7fWKW/candidate/proof.tex

has SHA-256

    04f10c6dc7ae7f60ac6e71f8834f8712e7761d24d0e6a3614134f101c0b08614

The zero-context patch passes git apply --unidiff-zero --check against a fresh
copy of that v2 candidate, with no offset or fuzz. Applied to that copy, it produces a v3
proof whose SHA-256 is

    1392f87e1ef47a1dde1c8b17ee7e264ed4a1b926e031ea35a9fb711e91f83d87

The only semantic change replaces the selected-stratum/SNC sentence by the
direct central-ideal implication

    W subset B_i  =>  O_Y(-B_i) subset I_Z  =>  w_i>0.

This uses the same central-ideal premise already cited in Step 2 from MP24,
Lemma 2.1.1.

## Isolated draft build

A fresh copy of the v2 candidate was patched in a temporary directory and
built in draft mode with:

    pdflatex -draftmode -interaction=nonstopmode -halt-on-error
    bibtex
    pdflatex -draftmode -interaction=nonstopmode -halt-on-error
    pdflatex -draftmode -interaction=nonstopmode -halt-on-error

The final log SHA-256 is

    0a653a351510ba92f1749c0ba20612f8223f17e2b743b38e85e29e3a518a8a19

Its required scan contains no TeX error, undefined control sequence,
warning, unresolved reference/citation, duplicate label, or box diagnostic.
Draft mode generated no PDF.

## Boundary

These checks establish exact patch applicability, a clean v3 postimage, and
its isolated typeset integrity. They are not an independent mathematical
audit or a source-closed production verdict.

The v3 markdown review packet was refreshed and then independently reviewed.
`VERIFICATION_RESULT.md` records its `correct` verdict with zero critical
errors and zero gaps; `VERIFICATION_RUN_20260908/` preserves the request and
HTTP response.  Those review materials concern the exact v3 postimage above.
They do not turn this local validation record into a source-closed production
verdict or retire P14.3.
