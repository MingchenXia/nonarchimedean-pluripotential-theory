# P03 invariant split-toric LFS-only minorant envelope — source ledger

Status: source-scoped positive refinement of the invariant toric P03
companion.  It identifies the raw envelope of **only** invariant locally
Fubini--Study minorants on an interior Euclidean tropical ball for a finite
continuous invariant obstacle.  It neither admits noninvariant competitors
nor treats arbitrary upper-semicontinuous obstacles, so none of P03.1--P03.3
is retired.

## Claim-to-source map

| Step | Source / direct argument | Scope control |
| --- | --- | --- |
| Local convex minorant envelope is finite, continuous, and convex | Local specialization of the proof of `prop:p033-invariant-toric-real-pl-envelope` | The obstacle is finite and continuous; one finite convex minorant is inherited from the global P03 companion. |
| Invariant LFS minorant descends to convex data | Gubler--Jell--Rabinoff, Definition 7.8, Sections 7.9 and 7.14; Burgos Gil--Gubler--Jell--Künnemann, Theorem 5.3.11 | Finiteness, maximal-compact-torus invariance, a good separated strictly analytic boundaryless ball inverse image, and the dense split torus are essential. |
| Finite support maxima for the local convex envelope | Elementary compactness of supporting affine functions on the exhausting closed balls | Supports are used only on compact subsets of the open ball. |
| Character-lattice minorants | Direct rounding below, using one nonzero value-group element and a common denominator for each finite family | The fixed Euclidean ball is bounded; no density of the value group is assumed. |
| LFS normal form | Gubler--Jell--Rabinoff, Section 7.9 | Torus characters are invertible on the whole dense split torus. |

Primary sources: J. I. Burgos Gil, W. Gubler, P. Jell, and K. Künnemann,
*Pluripotential theory for tropical toric varieties and non-Archimedean
Monge--Ampère equations*, Kyoto J. Math. 65 (2025),
doi:10.1215/21562261-2024-0010; and W. Gubler, P. Jell, and J. Rabinoff,
*Forms on Berkovich spaces based on harmonic tropicalizations*, Bull. Soc.
Math. France 154 (2026), 135--238, doi:10.24033/bsmf.2919.

## Deliberate boundaries

1. The result is a local interior-ball statement and assumes that its inverse
   image is good, separated, strictly analytic, and boundaryless.  It does
   not assert a global LFS minorant approximation on an arbitrary noncompact
   tropical chamber.
2. It identifies the invariant LFS-only family.  It does not turn the full
   noninvariant local-FS/semipositive-real-PL competitor family into an
   invariant one.
3. The obstacle is finite and continuous.  No conclusion is drawn for an
   arbitrary upper-semicontinuous obstacle or for a singular toric boundary.
