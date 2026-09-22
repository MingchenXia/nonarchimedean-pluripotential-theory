# Chapters 47–49: atoms, support and capacity — 22 September 2026

## The excluded capacity argument

The former proof of `cor:ch49-mass-in-lin` applied the
Alexander–Taylor set-height inequality to the pointwise height T_omega,
asserting Cap*({T_omega > N}) <= n/N. Chapter 48 already distinguishes
the set height from the infimum of pointwise heights. Their minimax
orders cannot be exchanged.

The new `ex:ch49-uniform-tail-capacity` disproves this capacity estimate
on P1. For m > R distinct branches, use the bounded model potential
with profile -min(t/m,1) on each selected branch and zero elsewhere.
Its initial slopes sum to -1, so it is psh; it takes values in [-1,0].
Its normalized measure is the average of the m atoms at m ord_(p_i),
all of height m > R. The capacity test has full mass in {T_omega > R},
so both its ordinary and outer capacities equal 1 for every R > 0.
This does not disprove full mass on the linear-growth locus for a fixed
finite-energy measure on a curve: the testing measures vary with R.

## Conclusions actually retained

The corrected corollary proves that every atom of a finite-energy
measure is a linear-growth point. Each other point is pluripolar and
has a finite-energy psh pole witness, so it has zero mass.
Purely atomic measures therefore have full mass on the locus.

The full-mass conclusion is also proved for a smooth projective curve.
The complement consists of proper-support endpoints and is Borel.
Every compact subset of these endpoints is finite, since the disjoint
open branches form an open cover with one endpoint in each branch.
The compact subsets have zero mass, and Radon inner regularity applies.
For any Radon probability measure, finite integral of T_omega gives
another sufficient condition by the elementary tail bound M/N.

A general full-mass claim in arbitrary dimension is no longer asserted
on the basis of the invalid proof. No opposite general theorem is
claimed either. The integration arguments use finite collections of
integrable psh constituents and do not require that claim.

## Dependent uses

- Chapter 47 now obtains nonpluripolarity from the explicit imported
  finite-energy witness theorem, instead of misattributing full support
  to BJ Proposition 7.19. Its atom and additional-support statements
  point to the corrected Chapter 49 corollary.
- The divisorial sup bound for I in Chapter 47 now extends the two
  ordered psh inequalities to the entire analytification by divisorial
  determination. Integrability then gives the bound almost everywhere
  for both probability measures.
- Chapter 48's endpoint-set example uses finiteness of compact subsets
  of the endpoint set and vanishing of endpoint atoms. It no longer
  invokes an unsupported general support theorem.
- Chapter 48's explanation of its quantitative nonpluripolarity argument
  is synchronized with the new Chapter 47 source-input explanation.

The primary background is the published
[Boucksom–Jonsson paper](https://afst.centre-mersenne.org/item/10.5802/afst.1705.pdf):
Example 4.13 for the curve criterion; Corollary 7.48 for pole witnesses;
and the set-height inequality, Theorem 13.14, already recorded in
Chapter 48. The tail counterexample is a direct model computation.
No research problem is retired, and the research statements and proofs
elsewhere in Chapter 49 are not altered by this pass.

## Second pass and validation

The second reading checked the profiles at the proper-support endpoints,
the sum of initial slopes, every atomic weight, the exact test height,
the distinction between one measure and a varying family, Borelness of
the linear-growth locus, and the Radon inner-regularity argument.
The modified references and the uses of the former support claim in
Chapters 46–49 were searched and checked.

The rewritten core blocks have zero errors in the Mingchen style audit
and two warnings for retained historical `itm:` labels. Those labels
are preserved for existing cross-references. This is not a strict
zero-warning result or a style certification of the legacy chapters.
Two preliminary extracted audit files contained duplicate or incomplete
snippets; the reported core-block check uses complete, unique current
blocks. The manuscript's own structural checker has no such defect.

The Chapter 47–49 scoped build grew from 255 to 256 pages. Both scoped
builds have no unresolved reference, citation or overfull box.
Physical pages 87, 170 and 200–202 of the final scoped PDF were inspected:
the polar-set explanation, compact-endpoint argument, revised corollary
and tail example have no clipping or overlapping formulas.

The subsequent full build completed with pdfLaTeX, BibTeX and MakeIndex:

- 3,403 pages, 17,983,960 bytes.
- PDF SHA-256:
  `dd8677dbfd03604152f9561ed67388e5a76a954e130076e65e4c4d68544e5d3a`.
- 389 TeX inputs, 11,476 labels; no missing input, duplicate label,
  dangling reference or per-file structural defect.
- No unresolved citation or reference in the final log.
- 38 horizontal overflows and no vertical overflow, as in the recovery
  build; the pre-existing class-path warning remains.
- Inventory unchanged: 46 active atoms, 14 formal environments,
  tiers (0,5,8,16,17).

Relative to the 395-file
[recovery checksum ledger](full_build_source_sha256_20260922_recovery.txt),
only the following production-input hashes changed:

- `manuscript/parts/part4/ch47_bj_finite_energy.tex`: `e2f6475fddd6e87347a0ddaf9afcfe6edfba53f1c39512ca4580a953c227caef`.
- `manuscript/parts/part4/ch48_strong_topologies.tex`: `0f0075e0f9a59e987e0586e4d356bb0ffa348dae3b9bd6d6c944ca16281fa9c9`.
- `manuscript/parts/part4/ch49_linear_growth.tex`: `d99ad612bab4d9dd07fac2d15a8e9c1151c72e79e2790ec0b4adcdd6b5880f54`.

All other production inputs, including the author's restored curve
source and Chapter 71, still match that ledger. The dated historical
release artifacts are preserved.
