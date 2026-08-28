# P17.1 weighted Philippon--Gauss continuity: monograph staging audit

Date: 28 August 2026

Status: **staged, compiled, and visually checked; not integrated into the live
mathematical text**.

## Scope and verification boundary

This packet adapts the independently verified proof blueprint for the analytic
continuity input isolated from Pille--Schneider Question 4.9.  It does not solve
that question, and P17.1 remains open.

The archived generation result received an independent production Rethlas
verdict `correct`, with zero critical errors and zero gaps.  The exact monograph
adaptation below has not yet received its required second exact-byte verdict.
An attempted second submission was stopped by the account usage gate on 28
August 2026.  No alternative or indirect submission was attempted.  The files
must remain outside the live chapters until that second verdict is `correct`
with zero critical errors and zero gaps.

## Exact staged bytes

- statement:
  `manuscript/parts/part6/fragments/ch66_weighted_philippon_gauss_statement.tex`

  SHA-256
  `0ead6bffba18801464f854e22a1d6e67a18d4590803a00e8ce002df2b1a9cf85`
- proof:
  `manuscript/parts/part6/fragments/ch66_weighted_philippon_gauss_proof.tex`

  SHA-256
  `f358e6c377c9bfc16c3e9c013c12e1ac5e98855528a3da65df9c96ee01aba13d`
- isolated compile harness:
  `manuscript/editorial/rethlas_packets_20260828/`
  `p171_weighted_philippon_gauss_monograph_compile_20260828.tex`

  SHA-256
  `58f92f042cec61f90293e02e96c405a1969bddb35af9c4148f73518e6898c10d`
- isolated compile PDF:
  `manuscript/editorial/rethlas_packets_20260828/`
  `p171_weighted_philippon_gauss_monograph_compile_20260828.pdf`

  SHA-256
  `fa20c6e96598268b5418a4f2e60bff29e93ce191e605a97f6951fabc56724f23`

The PDF has 5 pages and 221097 bytes.

## Hostile mathematical audit

The adaptation retains the proof architecture and all hypotheses of the
verified blueprint.  In particular:

1. The statement assumes that the coefficient tuple is nowhere zero.  The
   final failure test explains why this cannot be discarded.
2. The local analytic algebra is denoted consistently by `A_V`; the character
   in the statement and the character used in the proof both have source
   `A_V`.
3. The proof identifies `rho = 0` with the non-Archimedean locus and constructs
   the Archimedean character from Ostrowski normalization and the real or
   complex Gelfand--Mazur argument.
4. Choice independence is not assumed: uniqueness up to complex conjugation
   is proved, and conjugation invariance of Philippon's functional is used
   explicitly.
5. Continuity on the Archimedean locus is proved with nets and finite-type
   character compactness, rather than by an unjustified sequential argument.
6. The D'Andrea--Krick--Sombra inequalities give the uniform comparison with
   the maximum coefficient norm.  The bound used here is deliberately
   harmlessly larger after translating their block-size convention.
7. Zhang's coefficient-space continuity is reduced from equal block sizes and
   degrees by an explicit padding map.  Degree zero is treated separately.
8. The exact identity with the weighted maximum and the uniform comparison
   imply the boundary estimate `|Phi-M| <= C rho`; this supplies continuity
   across the non-Archimedean boundary.
9. Homogeneity is checked on both loci.  The frame-change computation has the
   required minus sign and therefore defines an additive line-bundle metric.
10. The closing tests cover the hybrid Gauss boundary, real characters,
    arbitrary real weights, a vanishing coefficient, and the degree-zero frame
    sign.

The proof uses `eqref`-compatible equation labels, writes the exponential
constant as `\mathrm e`, and introduces no optional conventional theorem name.

## Compile and visual audit

The isolated document was compiled with the book bibliography databases by
the sequence `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`.  The final log has no
LaTeX error, undefined reference, undefined citation, overfull box, or
underfull box.  Text extraction contains no `??` or `[?]` placeholder.

All five pages were rendered at 144 dpi and inspected.  The statement, proof,
equations, references, page numbers, margins, and page breaks are legible and
unclipped.  Hyperlink borders are hidden in the inspection PDF.  No visual
defect remains.

## Integration gate

Before live integration, submit the exact statement and proof bytes recorded
above to production Rethlas.  If any byte changes, recompute the hashes and
submit the changed bytes instead.  Integrate only after a second verdict
`correct` with zero critical errors and zero gaps, then compile and visually
audit the full monograph again.
