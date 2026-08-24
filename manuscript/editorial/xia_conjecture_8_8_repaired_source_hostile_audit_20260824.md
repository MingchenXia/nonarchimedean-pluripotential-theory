# Hostile audit of the repaired source for Xia Conjecture 8.8

Date: 24 August 2026

## Audited snapshot and verdict

This audit concerns the exact source snapshot

- `main.tex` SHA-256:
  `5746eb011417caecfa876c05c6c74fb548e2ae9d086c1441189bbcad02a96594`;
- `ComplexGeometry.bib` SHA-256:
  `e3e48c5c503cd6cdaa7bb2e02bdbc02767031e3084c52eff7415258d9483813e`.

It was compared line by line with the Rethlas-verified proof packet
`xia_conjecture_8_8_repaired_proof_packet.md`, whose SHA-256 is
`9227826d7ba5c641c5fe32cc4daae9acbb3b57274dcc1b356ba8beadd58cad7b`.
The excluded source was neither consulted nor used in this audit, and no
citation to it occurs in the audited theorem source.

**Verdict: PASS.** I find no remaining must-fix mathematical error, missing
logical bridge, incorrect citation dependency, scope error, or symbol error in
the repaired proof. The exact `main.tex` snapshot above is suitable for exact
Rethlas verification. This audit does not itself replace that final exact-source
Rethlas run.

An independent isolated build of the audited snapshot, including a fresh Biber
pass and two final LaTeX passes, succeeds. The PDF has 12 pages. The final logs
contain no unresolved citation or reference, LaTeX warning, overfull or
underfull box, or compilation error.

## Must-fix findings

None.

## Detailed mathematical audit

### 1. Domain of the theorem and the \(\mathcal I\)-envelope reduction

Lines 106--119 now define the pure and mixed Cao volumes on the intended
domain rather than silently assuming positive raw non-pluripolar mass. The
citation at lines 118--119 contains all three needed pieces: Definition 3.2,
Proposition 3.3, and Theorem 3.5 of `Xiabdiv`.

Lines 202--211 correctly separate ordinary model projection from
\(\mathcal I\)-model replacement. Lines 834--859 then perform the latter at
the start of the general proof, preserve every partial Okounkov body by
\(\mathcal I\)-equivalence, identify Cao's mixed volume with the mixed raw
mass of the replacements, and verify positive raw mass before entering the
\(d_S\) package. Thus the approximation theorem at lines 861--865 is applied
on its actual domain. This matches the proof packet.

### 2. Potential sandwich

Lines 213--237 now give both pointwise traps, not merely an assertion about
masses. Line 225 uses Corollary 6.2.5 only to discard a finite initial segment
and obtain a uniform positive raw-mass lower bound. Lines 229--236 use the
order-closure statement of Proposition 6.2.5 on each tail and a constant
sequence; since all displayed potentials are model, the resulting envelope
inequalities are exactly \(\eta_j\leq u\leq\psi_j\). This closes the formerly
missing passage from the approximating terms to the limit.

### 3. Finite-level degeneration

Lines 262--520 implement the packet's finite-level estimate without assuming
the false equality of the two initial ideals.

- Lines 299--304 dispose of a one-dimensional factor before using general
  hyperplanes.
- Lines 323--332 correctly derive one-dimensional leaves from full rational
  rank and algebraic closedness of the base field.
- Lines 411--418 prove only the inclusion \(Q\subseteq J\), which is the
  inclusion actually available and actually needed.
- Lines 420--435 realize the matrix initial ideal by a scalar weight and
  preserve every multigraded Hilbert function.
- Lines 467--478 account for irrelevant multigraded torsion before comparing
  Hilbert polynomials and dimensions.
- Lines 480--505 compare top-dimensional cycles, retaining component
  multiplicity and the non-negativity of mixed degrees.
- Lines 508--520 justify the toric mixed degree after the degenerate-factor
  branch has been removed.

No reverse inclusion between \(Q\) and \(J\), reducedness of the special
fiber, or multiplicity-one assertion is used.

### 4. Movable upper bound

Lines 523--598 correctly pass from the finite-level estimate to arbitrary big
\(\mathbb Q\)-divisors. Lines 549--568 simultaneously secure the full value
lattice and birationality along one divisible sequence. Lines 570--589 use a
common resolution of all base ideals and the admissible nef approximation.
The precise inputs are BFJ09 Definition 2.5 and Propositions 2.12--2.13 at
lines 247--258. Lines 591--597 then take the Hausdorff limit along the same
divisible sequence. No unjustified termwise bound on an arbitrary level is
needed.

### 5. Uniformity in the valuation

The convex lemma at lines 605--666 has all four necessary inclusions. Its
John-normalization argument controls determinant in both directions and its
subsequence argument proves convergence of the full sequence.

Lines 684--742 correctly establish valuation-uniform convergence of mixed
volume values:

- lines 689--703 make a finite successive extraction, so every index \(i\)
  uses the same subsequence;
- lines 704--709 explicitly invoke continuity of **raw** non-pluripolar mass
  and discard one common finite initial segment, ensuring that all later
  bodies are on the positive-volume locus;
- lines 718--723 supply both convex-body sandwich chains;
- lines 724--730 obtain the valuation-independent lower-volume and vanishing
  gap estimates;
- lines 732--739 uniformly bound the containing Minkowski sums by the
  ordinary body of the tensor product.

This is the uniform statement needed at lines 876--886; the elementary
supremum estimate is explicitly written there.

### 6. Analytic-singularity case

Lines 746--832 agree with the verified packet.

- Lines 751--773 produce rational nef and big residual classes and use
  numerical invariance for the complete valuation class via Xia's
  Proposition 10.3.2.
- Lines 775--785 define the divisor translation at the center of each
  valuation and combine the resolution formula with the movable upper bound.
- Lines 788--802 keep every auxiliary class in the rational divisor category.
- Lines 803--824 apply Wilms to one common flag and derive the decisive body
  inclusion by multiplication with the canonical section of \(E_i\), followed
  by homogeneity and numerical invariance.
- Lines 826--831 let \(\epsilon\to0+\) and restore the fixed divisor
  translations.

In particular, no flag-only numerical-invariance result is being applied to
the general valuation class.

### 7. General case and the ordinary-body theorem

Lines 834--888 correctly combine the \(\mathcal I\)-envelope reduction,
analytic \(d_S\)-approximation, mixed-mass continuity, and valuation-uniform
mixed-volume continuity.

Lines 890--912 now contain an independent proof of `thm:main1`. The inclusion
of each partial body in its ordinary body and equality of their positive
diagonal volumes force equality of the full-dimensional compact convex
bodies. BEGZ10 Definition 1.17 and BFJ09 Propositions 2.12--2.13 then identify
the mixed non-pluripolar mass of minimal-singularity currents with the
projective movable product. Applying `thm:main` therefore gives precisely
equation `eq:movable-main`; the introductory reduction is no longer circular
or merely asserted.

## Suggested, non-blocking repairs

### S1. Spell out what taking model envelopes preserves

**Location:** `main.tex`, lines 225--236.

The present sentence “and then take the \(P\)-envelopes” is correct, but a
reader may briefly wonder why all features of the raw sandwich survive. A
two-sentence expansion could say that monotonicity of \(P_\theta\), together
with \(P_\theta[u_j]=u_j\), preserves both pointwise traps and monotonicity,
while Proposition 6.2.2 preserves the \(d_S\)-classes. This would improve
self-containment but is not a logical gap: the subsequent displayed traps and
the cited envelope facts already determine the intended argument.

### S2. Refresh the ancillary repair log

**Location:** `SOURCE_REPAIR_LOG.md`, lines 11--15, 21--22, 43--50,
52--113, and 126--140.

This is documentation only, not theorem source. The log still says that the
bibliography is byte-identical to the original, records its superseded hash,
describes an earlier version of the potential-sandwich repair, gives stale
source line numbers, and reports the former 11-page build. The audited state
has the bibliography hash recorded above and compiles to 12 pages. Updating
the log would make the provenance record agree with the exact snapshot sent
to Rethlas.

## Final submission recommendation

Freeze `main.tex` at SHA-256
`5746eb011417caecfa876c05c6c74fb548e2ae9d086c1441189bbcad02a96594` and
`ComplexGeometry.bib` at SHA-256
`e3e48c5c503cd6cdaa7bb2e02bdbc02767031e3084c52eff7415258d9483813e`, then
submit that exact pair for the final exact-source Rethlas check. Neither
non-blocking suggestion requires changing `main.tex` before submission.
