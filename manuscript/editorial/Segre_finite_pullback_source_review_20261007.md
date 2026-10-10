# Finite pullbacks, Segre invariants and integral dependence: source review

Date: 7 October 2026. Baseline `work`
`e2215a59606ea21f803af759de0c03a29a74063c`; observed `main`
`00957114db21b627e97369563032ceda9cea09c7`.

Zbigniew Jelonek, Victor Hugo Jorge Pérez and Raimundo Nonato Araújo dos
Santos, *Finite holomorphic pullbacks, Segre numbers, and generic Lê
numbers*, arXiv:2610.07528v1, submitted 5 October 2026 at 23:51:22 UTC,
was read completely. Twelve related/dependency PDFs were read in explicit
scopes, including the complete published 2026 article *Segre classes and
integral dependence* by Yairon Cid-Ruiz. The total is **131 distinct
source/page pairs in 70 individually displayed sheets**. Every pair has
complete selected-text reading, matching-image inspection and a sequential
note. Five PDFs are complete readings; eight are partial. No reading
attestation is reused. Downloaded files, metadata inspection and proof
reading are recorded separately.

The suitable connection is to Appendix C's integral closure and Rees
valuations, Appendix F's intersection numbers, and Appendix H's complex
comparison material. The published global numerical criterion requires
an ample polarization and nested ideals. Finite pullback supplies a
different comparison: exact scaling at the top index and inequalities at
other indices. Ideal inclusion supplies only a lexicographic comparison.
The componentwise Jacobian and generic-Lê conjectures are equivalent
formulations of one frontier, not two independently solved problems.

This source-only checkpoint preserves the 4,509-page book, all 425 active
inputs, 108 protected inputs, 112 preceding frozen manifests and 190
frozen exports. The native catalogue/editor and canonical atomic statuses
are unchanged. No new book compilation or final-book reading is claimed.
No original result, independent-model receipt, general BJ22 Theorem 6.21
repair, or solved-status promotion is admitted. Reading the displayed
proofs does not recursively certify their cited foundations.

## Exact reading scopes

All locators below are physical PDF pages. The manifest supplies full
SHA-256 identities, acquisition URLs, text/image identities and notes.

| Exact source | Pages actually read | Complete PDF? |
| --- | --- | --- |
| Jelonek--Jorge Pérez--Araújo dos Santos, 2610.07528v1 | 1--17 | yes |
| Achilles--Manaresi, 2006 author PDF | 1--4, 7--13 of 28 | no |
| Cid-Ruiz--Polini--Ulrich, author PDF dated 28 June 2025 | 1--5, 15--26 of 33 | no |
| Jelonek--Tibăr, published Math. Ann. 361 (2015), 1049--1054 | 1--6 | yes |
| Giraldo--Roeder, 1911.00628v1 | 1--11 | yes |
| Jelonek, 2301.08989v1 | 1--3 | yes |
| Sabbah, published J. Singularities 18 (2018), 238--247 | 1--3 of 10 | no |
| Wells, published Pacific J. Math. 53 (1974), with cover | 2--13 of 23 | no |
| Stacks, frozen de Rham chapter PDF | 40--44 of 69 | no |
| Gaffney--Gassler, alg-geom/9611002v1 | 1--9, 23--25 of 32 | no |
| Massey, 1410.3312v2 | 18--23 of 32 | no |
| Massey, 2406.11758v1 | 5--9 of 15 | no |
| Cid-Ruiz, published Math. Ann. 395 (2026), article 101 | 1--23 | yes |

The last article has DOI `10.1007/s00208-026-03532-3`, was accepted
18 June and published online 6 July 2026. Its arXiv metadata records
2512.08863v1 on 9 December 2025 and v2 on 18 June 2026. Neither arXiv PDF
was acquired or read; the admitted theorem numbers refer to the published
23-page file. Likewise, the June 2025 CPRU author PDF is not identified
with the uninspected arXiv:2405.07000v1 or a journal edition. CPRU has
three authors, including Claudia Polini.

Massey 1410.3312v1 was acquired but remains unread. The subsequent
selected reading uses v2 of 13 November 2015. The Stacks HTML tag was
downloaded but the actual theorem reading uses the frozen chapter PDF.
Its dynamic compilation is pinned by bytes, not an invented edition date.
A Giraldo--Roeder author-site URL and an incorrect Stacks PDF URL returned
404; these ordinary acquisition failures are neither successful readings
nor automatic-approval rejections. The Giraldo--Roeder journal edition
was not acquired; the known published citation does not establish byte
identity with the completely read v1.

## Local algebra and finite pullback gates

**S01 -- Ambient Jacobian and indexing.** Main paper Sections 2--3,
pp.3--7, use smooth local analytic rings of equal ambient dimension and a
finite germ of degree `d`, hence a finite flat/free extension. Jacobian
ideals are taken in the ambient ring, not in the hypersurface quotient.
For `g o F=u h^r`, with reduced `g,h` and unit `u`, the chain rule gives
`J_h subset F*J_g` when `r=1`, and the product ideal
`h^(r-1) J_h subset F*J_g` for higher multiplicity. Removing a unit is
an integral-closure assertion, not a literal equality of Jacobian ideals.
The arc proof of Lemma 2.6 uses `f` integral over `m J_f`, Leibniz and
the inverse unit.

Achilles--Manaresi index `c_i` by dimension; their top double-cumulative
polynomial has terms `c_i u^i v^(n-i)/(i!(n-i)!)`. The main paper writes
`e_j=c_(n-j)`, so its top Segre index is `e_n=c_0`. CPRU instead index
by codimension. Their `(c_0,...,c_n)` corresponds to the main paper's
`(e_0,...,e_n)`, not its dimension-indexed `(c_0,...,c_n)`.

**S02 -- Support and association.** Achilles--Manaresi Theorem 3 is at
physical p.8 / printed p.352. With `q=dim R/I`, the multiplicities vanish
outside `n-ell(I)<=i<=q`, and the highest possible `c_q` has the stated
association formula. Equimultiplicity leaves only `c_q`; an m-primary
ideal leaves only `c_0`. Positivity claims in the paper involving
Cohen--Macaulay/domain hypotheses are not broadened to arbitrary rings.
The special length formula for j-multiplicity in Theorem 4, p.13, has
its SCM/G_d assumptions and its displayed quotient; it is not a generic
length-of-primary-quotient formula.

**S03 -- Lexicographic inclusion.** Main Theorem 2.7 imports CPRU
Corollary 6.5, physical p.25 of the June 2025 author PDF. For nested
ideals in an equidimensional universally catenary local ring, the Segre
tuple decreases lexicographically. Theorem 6.3, pp.23--24, obtains a
single comparison and uses equality to control the next residual height.
This mechanism does not give all inequalities simultaneously. The
middle tuple in Corollary 6.5's proof has a visible inconsistent ring
argument in one coordinate; it is recorded as a proof-display typo,
not evidence of a stronger theorem or a false result. CPRU Theorem 6.6
uses integral closure, while Theorem 6.7 has its additional order and
generic-G-parameter hypotheses.

Achilles--Manaresi Remark 4, p.9, has nested-ideal examples with opposite
movement in different coordinates. Those examples show why lexicographic
information is weaker; they are not counterexamples made from finite
pullbacks of reduced hypersurface Jacobians. Equal radicals are also not
the same as a reduction or equality of integral closures.

**S04 -- Generic cycles.** CPRU Setup 5.1, p.15, and pp.16--22 use the
Rees blowup, exceptional `Proj gr_I R`, polar residuals and proper generic
cuts. Generic G-parameters satisfy the stated BiProj dimension condition.
The polar/Segre/residual relation and its equality case retain that
condition. Gaffney--Gassler pp.1--9 similarly distinguish general proper
cuts from choices yielding generic minimum numerical values. Generic
cycles can move even when their numbers are constant. All local lengths,
field degrees and support components in cycle pushforward are retained.

**S05 -- Finite Hilbert--Samuel bounds.** Main Section 3 compares a proper
ideal `Q` and its flat extension: the multiplicity at the target is no
larger than that of the extended ideal at the source and the latter is
at most `d` times the former. Its graph-cut argument needs proper
dimension drops. The common-open generic cuts must be chosen compatibly
at every stage; source split components and their multiplicities cannot
be discarded. Theorem 3.4 gives the two-sided bounds for all `e_j` and
exact factor `d` only for `e_n`. The divisor ideal under
`F(u,v)=(u,v^d)` illustrates why the other coordinates need not scale
by `d`. Neither equal radicals nor an ambient-degree rescaling replaces
the source maximal-ideal multiplicity calculation.

## Milnor, trace and slicing gates

**S06 -- All multiplicities in the isolated case.** Main Theorem 4.2,
pp.8--9, compares isolated Milnor numbers for all `r`, with irreducible
reduced target and source equations. Its cyclic
intermediate algebra `A[z]/(z^r-g)` is a domain and has rank `r`, with
the remaining finite degree `delta=d/r`. The topological argument uses
a proper source domain inside the Milnor fibre and a pullback injection
with characteristic-zero coefficients. It neither identifies that
domain with the entire Milnor fibre nor establishes integral-coefficient
homology surjectivity. Jelonek's completely read 2301.08989v1 already
contains an isolated irreducible version of this comparison.

The `r=1` chain-rule inclusion is between m-primary ideals in the
isolated case and gives the stronger `mu(h)>=d mu(g)` in Corollary 4.3.
For `r>1`, the extra divisor in `h^(r-1)J_h` makes this argument invalid;
no factor `d/r` is inserted into the higher-multiplicity conclusion.

**S07 -- Differential trace has a source signature.** Main Section 4's
Brieskorn route localizes over the smooth cyclic parameter cover before
using trace, projection and commutation with the differential. Branch
cancellation and normal/codimension-two extension are distinct steps.
Sabbah's published pp.1--3 recall the isolated free rank-`mu` Brieskorn
lattice, citing Brieskorn and Sebastiani; they do not prove those original
theorems. In the nonisolated case the raw quotient can have torsion and
must not be treated as the same free lattice.

Wells Theorem 3.1, physical p.10 / printed p.289, and the selected proof
on pp.12--13 concern proper surjective maps of equal-dimensional smooth
complex manifolds. The injection is for complex de Rham/Dolbeault
cohomology; no compactness or Kähler premise is silently added, and no
integral-coefficient extension is claimed. In the frozen Stacks chapter,
Lemma 19.2 (0FLB), pp.41--42, requires finite syntomic morphisms, and
Proposition 19.3 (0FLC), pp.42--44, gives the corresponding de Rham
compatibility. Section 19 (0FK6), beginning p.40, explicitly does not
offer unrestricted finite-flat differential traces on singular targets.
Its singular quotient example is not asserted to be finite locally free.
These results do not authorize a trace on arbitrary singular-origin
Brieskorn forms.

**S08 -- Smoothness descent is already known.** Main Theorem 4.5,
pp.9--10, concerns descent of smoothness of the reduced image. The
completely read Giraldo--Roeder v1 supplies the known theorem and its
forward hypersurface-to-foliation/Koszul route, pp.6--8. Proposition 4.3,
pp.8--10, uses nearby points and a pencil of translated affine
hyperplanes, with separate transversality, smooth ambient preimage and
reduced target-slice requirements. The main paper says a linear system
of hyperplanes with no base points; it does not require all hyperplanes
to pass through the origin. Such an additional reading would introduce
an unjustified base point.

Jelonek--Tibăr Lemma 2.5, physical p.5 / printed p.1053, is the general
complete-intersection nonsingularity lemma needed here, despite that
article's global title. It is not an unrelated citation. The main
slicing argument must retain the scheme complete-intersection and
reducedness qualifications. Giraldo--Roeder's reverse foliation
construction uses a trace first integral; nonconstancy is not a general
automatic property of trace. This reservation is not used to deny the
forward route establishing the known smoothness theorem.

## Generic Lê numbers and exact frontier

**S09 -- One-dimensional singular loci.** Main Section 5, pp.10--12,
combines Jacobian inclusion, lexicographic monotonicity and finite bounds.
At fixed singular-locus dimension, the first potentially nonzero
coordinate is controlled. Equimultiplicity can reduce the tuple to that
coordinate. Theorem 5.5's stronger `c_0` bound needs equality of the
preceding `c_1`; a strict first-coordinate increase supplies no separate
control of the later coordinate. Corollary 5.6 retains its sufficient
equality/equimultiplicity/nonramification hypotheses.

**S10 -- Prepolar is weaker than generic.** The intrinsic transverse
cycle is the sum of transverse Milnor numbers times curve components.
For an admissible first coordinate, its intersection can have excess
`delta>=0`; both `lambda^1` and `lambda^0` then increase by the same
excess. Massey 1410.3312v2 pp.18--23 defines the cycles and properness
requirements; Theorem 4.1 supplies the Euler-characteristic convention
for the source's ambient `n+1`. This is converted explicitly before
comparison with the main paper's ambient `n`. Main Example 7.4 compares
admissible coordinate systems with different excess; even the identity
map refutes an arbitrary-coordinate comparison, not the generic-number
conjecture. Zero excess must be checked on the relevant target/source,
not imposed by relabelling any prepolar coordinate as generic.

**S11 -- Perturbation is not automatic pullback comparison.** Massey
2406.11758v1 Theorem 3.5, pp.7--8, concerns one germ with defined Lê
numbers, a sufficiently suitable power and a coefficient outside a
finite exceptional set. Its dimension-drop formula and its
`lambda^0` bound have explicit equality thresholds. The main paper's
large-power equality gives a lexicographic consequence only if the
additional comparison of perturbed isolated Milnor numbers is supplied.
A pulled-back linear coordinate can be nonlinear and critical at the
source; the isolated theorem cannot be applied without that check.

**S12 -- Higher multiplicity and cycles.** Main Proposition 6.1 and
Corollary 6.2, pp.13--14, need compatible smooth finite transversal
slices and the stated coverage. Passage from transverse Milnor
comparison to a generic Lê number further needs the equality identifying
the pulled cut with the source cycle multiplicity. It is not automatic
under arbitrary ramification. For the product cusp, transverse Milnor
number increases from 2 to 6 under the displayed ramified map. A map
ramified only in the singular-locus direction has positive degree and
unchanged tuple `(0,2,0)`; this prevents a blanket degree-factor rule.
The factor `h^(r-1)` also creates a positive divisor coordinate and
prevents interpreting its multiplicity sequence as a rescaled `J_h`.

**S13 -- Examples and conjecture deduplication.** Main Example 7.3,
p.15, has transverse number 1 on both sides and polar intersection
numbers 8 and 24; the displayed first coordinate has zero excess in
both computations. The source's irreducibility assertion remains
source-attributed; no new irreducibility proof is claimed. Conjectures
8.1 and 8.2, p.16, ask respectively for componentwise Segre and generic
Lê comparison for finite pullbacks with irreducible reduced target and
reduced source support, including arbitrary pullback multiplicity. The
paper identifies them as equivalent. Conjecture 8.3 is the weaker
lexicographic frontier under the same assumptions. The isolated cases
and multiplicity-one
lexicographic theorem do not settle those stronger statements. These
remain source-attributed directions, not new canonical atomic entries.

## Published global integral-dependence criterion

**G01 -- Ample and nested.** Cid-Ruiz Theorem A / Theorem 4.3,
pp.1--2 and 12--14, assumes an equidimensional projective scheme over a
field, an ample line bundle `L`, and nested closed subschemes `W subset Z`
with `I_Z subset I_W`. It equates integral dependence with the relevant
equality of Segre classes, equality after pushforward to the ambient
Chow group, and equality of all `L`-Segre degrees. Nonreduced schemes
are included. Superscript `s^i` is codimension `i`, distinct from AM's
dimension index. There is no claim for unrelated ideals or arbitrary
Chow classes with equal degrees.

**G02 -- Numerical proof and its imports.** Section 3, pp.3--10, uses
generic Vogel residual/retained cycles over a purely transcendental
extension. Classes descend through the stated Chow-group isomorphism;
the generic cycles themselves need not be defined over the initial
field. The van Gastel triangular relation includes the special
codimension-zero convention. Twisted Rees blowups retain the pullback
line-bundle shift in `O(1)`. Vogel cycles are effective, while Segre
components can have signs. Proposition 3.11 and Corollary 3.13 relate
residual degrees to the top Snapper polynomial coefficients.

Setup 4.1, p.11, chooses one sufficiently positive power of `L` making
both ideals globally generated and the polarization very ample. Lemma
4.2 converts equal Segre degrees to equal Vogel and residual degrees.
Theorem 4.3's converse bounds the ideal-power quotient growth using
Proposition 4.4, whose complete displayed proof was read on pp.14--18.
Claims 4.5--4.6 use a closed point on the dependence obstruction, a local
Hilbert--Samuel polynomial, and multigraded cohomology vanishing on a
second twisted blowup to obtain strictly positive normalized growth
when the Rees extension is not finite. The argument cites
Kleiman--Thorup, multigraded vanishing and Fulton; those original
foundations have not been recursively read. The book may give an
attributed proof roadmap, not present this audit as an independent new
proof of their inputs.

**G03 -- A verified source counterexample to big-nef substitution.**
Published Example 4.7, pp.18--19, first blows up a point in projective
three-space and then a line in its exceptional plane. On the resulting
smooth threefold, `L` is the composite pullback of `O(1)`, hence big and
nef. The second exceptional divisor `E` and `kE`, `k>=2`, have distinct
integral-closure ideals but all their `L`-Segre degrees are zero. The
first two degrees vanish by contraction/dimension; the last needs the
normal-bundle computation `deg E^3=-deg c_1(N)=0`, from the normal exact
sequence with end bundles `O_P1(1)` and `O_P1(-1)`. No splitting of that
sequence is asserted. Contraction alone does not kill a zero-cycle's
ordinary degree. This is a published, attributed example, not an original
counterexample produced by the present work.

**G04 -- Stabilization at the homogeneous vertex.** Section 5,
pp.19--21, defines Aluffi's Segre zeta function by extending a homogeneous
ideal to all larger projective spaces; its rationality is imported in
Theorem 5.1. Corollary 5.2 says that for nested homogeneous ideals
`I subset J`, equality of zeta functions is equivalent to integral
dependence. Its converse uses a projective dimension exceeding both
generator counts, Theorem A, equality of saturated integral closures,
the cited associated-prime height bound to remove saturation, and
faithfully flat contraction. Extracted text loses the integral-closure
bars in pp.20--21; the displayed images retain them. A single original
projective Segre class can omit the homogeneous vertex, so the stabilized
criterion must not be replaced by that weaker datum.

## Admission and continuation

Admit the global ample criterion, its precise big-nef counterexample,
and the distinctions between integral closure, local multiplicity,
finite degree and generic slicing. A limited complex Appendix H
connection may describe the known isolated and lexicographic finite
pullback results and the accurately deduplicated open frontier. Provide
exact-version provenance in Appendix L and bridges from Appendices C/F.
Do not introduce a new theorem transferring these statements to arbitrary
non-Archimedean singularities, nef b-divisor intersections or BJ22 Siu
division. A new original generalization would require its own proof and
the prescribed independent-model receipt.

The following integration must preserve historical formal statements and
proofs, run the required repository build, and read the matching affected
final pages with complete text and individually displayed images. This
source checkpoint supplies none of those final-book claims. Continue
cloud-only work and inspect GitHub for incoming author changes before
publication, using an expected-head update without a force push.
