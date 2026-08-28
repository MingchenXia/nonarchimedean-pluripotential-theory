# P17.1 relative-resultant staging audit

Date: 28 August 2026

Status: frozen staging candidate.  This packet is not part of the live
manuscript, does not retire P17.1, and has not received production Rethlas
verification.

## Candidate scope

The candidate constructs a Ducrot intersection-line resultant for a flat
projective family with nonempty pure-dimensional fibres and finite locally
free quotient systems
\[
f^*E_i\twoheadrightarrow L_i
\]
whose \(L_i\) are relatively ample.  It proves the line formula, local norm
description, symmetry, locally Noetherian base change, and incidence
detection at points of fibre-local depth at most one.  It also treats the
relative-dimension-zero rank-one endpoint.

This is an algebraic auxiliary result only.  It does not prove continuity of
mixed Monge--Ampère integrals over a general integral Banach ring and hence
does not solve P17.1.

## Rejected overstatements and repairs

1. The first formulation allowed arbitrary basepoint-free semiample systems.
   Ducrot's definition of a relative regular sequence requires a nonempty
   final intersection.  Associated-point avoidance does not exclude a unit
   section.  Relative ampleness is the firewall used in the frozen candidate.
2. The first depth proof treated bad linear subspaces as fixed over the
   original residue field.  They vary with the preceding parameters.  The
   frozen proof projects to the used factors, passes to the fibre over their
   image, and obtains two independent codimension-one conditions in two
   unused projective factors.
3. The semiample \(\mathbf P^1\times\mathbf P^1\) example only disproves an
   all-point semiample extension.  It does not disprove a possible stronger
   all-point theorem under the ample hypotheses.
4. Local-cohomology extension is stated with the sheaves
   \(\mathcal H_Z^i\), and the proof explicitly records the pointwise depth
   criterion, openness of the regular locus, expected purity after nonempty
   Cartier cuts, and finiteness in relative dimension zero.

## Independent pre-Rethlas audits

An independent hostile mathematical audit found no counterexample or
blocking proof gap in the frozen statement and proof.  In particular it
checked mixed-degree positivity, the corrected fibre-depth argument, norm
gluing, local-cohomology extension, incidence detection, arbitrary locally
Noetherian base change, symmetry, and the rank-one endpoint.

A separate primary-source audit checked Ducrot's arXiv preprint
alg-geom/9712010:

- Proposition 6.1.1 supplies intersection-line base change, symmetry,
  relative-dimension-zero norms, Cartier restriction, and commuting
  two-section restrictions.
- Corollary 6.1.2 supplies the norm identification after a relative regular
  sequence.
- Lemma 6.3.1 supplies the projection calculation with the positive
  \(+d_i\) exponent.
- Lemmas 6.3.2--6.3.3, the unnumbered paragraph following Definition 6.3.4,
  and Lemmas 6.3.5--6.3.6 are used only as proof templates.  Their
  quotient-system analogues and base-change naturality of the resultant
  section are reproved in the packet.

These audits are not substitutes for the required production
gpt-5.6-sol/xhigh Rethlas verdict.

## Compilation and visual inspection

p171_basepoint_free_relative_resultant_compile_20260828.tex compiles with
latexmk in PDF mode with nonstop interaction and halt on error.

- Output: 6 A4 pages, 290783 bytes.
- PDF Author metadata: empty.
- Log scan: no overfull or underfull boxes, undefined references, LaTeX or
  package warnings, multiply defined labels, emergency stops, or fatal
  errors.
- All six rendered pages were inspected at 150 dpi.  No clipping, overlap,
  missing glyphs, black boxes, or margin defects were found.

## Frozen SHA-256 manifest

~~~text
beba5a7c1c1e938ab774aac5fbe0d44a294da9efa022b340169b55a161effc45  p171_basepoint_free_relative_resultant_statement_20260828.tex
cbb2391527ed48fde34cb95e005b21ae52961b1caa1b41b8a98736f14ffe9f9c  p171_basepoint_free_relative_resultant_source_aware_proof_20260828.tex
8786890a9ccbed379f406db7c4ee8cc9c04992961c1cd63b6d53bbe6148455c5  p171_basepoint_free_relative_resultant_problem_20260828.md
ab0523381a42f137fb24f993df77223d7d6dcc8536040d990ddcf2a9e64da77f  p171_basepoint_free_relative_resultant_hostile_audit_20260828.md
479ff542f9cd02c57c25eb631ef3787b91b4a34fa05275b3501eeaa30830fcd1  p171_basepoint_free_relative_resultant_compile_20260828.tex
493e70599abfa0486d9299b3bbb10f98e5d28b91090941dc277aebc9137a999f  p171_basepoint_free_relative_resultant_compile_20260828.pdf
~~~

Any edit to the theorem or proof invalidates this manifest and requires a
fresh hostile audit, compile/visual pass, and exact-byte Rethlas submission.
