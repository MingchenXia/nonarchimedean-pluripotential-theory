# P17.1 post-P21.3 research-lane manifest

Date: 29 August 2026

Status: quarantined; not a live-book input; P17.1 remains open.

## Exact hashes

~~~text
3ad32111cfa564815c91dfa9aad30070495611b9f59bb677e2d0050820e38dfb  p171_closed_immersion_reduction_statement_20260829.tex
f43c83f12b738b60f26e534989552805d812126bfb3b4a9fdfc177eb9b020e13  p171_closed_immersion_reduction_proof_20260829.tex
77c48309e0a56f0c7281933eb463f156a1ac35f9bf2fa22cc9c089ca8b18f183  research_memo_20260829.md
c609c772b64f18518e51b6d7df02c0163b4cf3cd1552699791f30a10fd0f4835  p171_closed_immersion_reduction_compile_20260829.tex
23e25b16183bc9c8dcfaea30016de87ee14b8d6184a73f6f6c3b22d275844240  p171_closed_immersion_reduction_compile_20260829.pdf
~~~

## Compile and visual audit

The isolated wrapper compiled with PDF LaTeX through latexmk in nonstop mode
with halt on error. The final log contains no warning, undefined reference,
undefined citation, overfull box, underfull box, multiply defined label,
emergency stop, or fatal error. The output has three A4 pages and empty
Author metadata.

All three pages were rendered at 120 dpi and inspected. No clipping,
overlap, missing glyph, black box, or margin defect was found.

## Verification gate

The statement and proof have **not** been submitted for an exact-byte
production Rethlas run. No mathematical claim in them is verified for live
integration. Any byte change requires recomputing the manifest; any live
integration requires a production verdict of correct with zero critical
errors and zero gaps.
