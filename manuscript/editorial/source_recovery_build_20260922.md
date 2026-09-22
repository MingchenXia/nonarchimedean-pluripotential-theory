# Author-source recovery and full build — 22 September 2026

## Recovered input

The author supplied the missing `CURVE_PSH.tex` in the current task.
It has been copied byte for byte into the exact path already included by
Chapter 70:

`editorial/solver_dossiers_20260911/p122_curve_ideal_psh_functoriality_20260911/CURVE_PSH.tex`

The file has 1,324 lines and SHA-256
`9142aac73c5af7e4e715b3313def5ed56fae4e63e1ac8a53d0419df7d2194be9`.
Its 43 labels include all eight formerly missing targets. This records
recovery of the supplied source, not a reconstructed substitute proof or
a new mathematical certification of its contents.

## Full current-source build

After restoration and the concurrent Chapter 46 pairing corrections,
`latexmk -pdf -interaction=nonstopmode -halt-on-error book.tex`, run from
`manuscript/`, completed successfully. It ran pdfLaTeX, BibTeX and
MakeIndex until the generated files stabilized.

- PDF: `manuscript/book.pdf`, 3,403 pages, 17,981,610 bytes.
- PDF SHA-256: `a98fdd959a269dae94f17b561127a9f3401539900b80252417d72f61eace5cb6`.
- Source graph: 389 TeX inputs; 11,475 unique labels; zero missing inputs,
  duplicate labels, dangling references or per-file structural defects.
- Final log: no unresolved reference or citation. The class-path warning
  for `style/svmono` remains; it does not prevent compilation.
- Layout: 38 overfull horizontal boxes and no overfull vertical box.
  These are recorded as further editorial work, not a clean-layout claim.
  The log reports no overfull box while reading the recovered file.
- Research inventory: 46 active atoms in 14 formal environments;
  tiers (0,5,8,16,17), unchanged.
- Chapter 71 was not edited; its SHA-256 remains
  `05ce1967cb4d083613bcb72dae1c23ebbc60156840f9fa3555caba32d85ad634`.

The exact 395 local production inputs (the 389 TeX files plus class,
bibliography style, index style, two databases and latexmk configuration)
are recorded in
[the source checksum ledger](full_build_source_sha256_20260922_recovery.txt).
That ledger has SHA-256 `eb25884105197b5ce85d487aebe86c6900179fc233ef1f67cf93513defc7cd94`.
The PDF checksum identifies this particular build; PDF timestamps can
change its bytes on a subsequent otherwise equivalent build.

Physical pages 3095, 3098, 3101 and 3106 of the full PDF were rendered and
inspected. They show the restored completion theorem, generic-norm
descent, variable-degree example and radial cusp/multinode discussion.
The inspected pages have readable formulas and no clipping or overlaps.
This sample is not a visual audit of all 3,403 pages.

The dated release PDF, archive and historical release receipts have not
been overwritten. The present receipt establishes recovery of full
current-source compilation; the continued mathematical and layout audit
remains active.
