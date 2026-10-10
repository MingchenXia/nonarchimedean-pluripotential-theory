# Chapter 16: second reading audit

Date: 3 October 2026. The original 5,753-line main source and all 83
direct inputs, totalling 13,611 lines, were freshly read continuously.
The four replacement reader fragments, totalling 882 lines, were also read
in full. The final
main source has 5,802 lines and preserves all 235 labels. Compared with
checkpoint `041c779`, all 188 formal environments, including proofs and
warnings, retain their order: 141 are byte-identical and 47 change. The
complete mathematical diff and final edited contexts were reviewed.

The [input ledger](second_reading_ch16_input_ledger_20261003.json) records
all original paths, hashes and fresh reading coverage. All 83 original
files remain byte-identical. Seventy-nine remain active; four are replaced
by reader copies. Two copies repair literal `cdot`/`qquad` typography,
one makes the finite insertion set nonempty when the original exceptional
set is empty and the test point is the node, and one keeps a short
nonreduced example together on the page. Their frozen statements, proofs,
source packets and verifier receipts are preserved.

## Construction and proof interfaces

The opening no longer presents a self-wedge above the top degree as the
obstruction to multiplying arbitrary currents. It identifies the missing
singular coefficient product, then explains the legitimate recursion:
multiply the order-zero current by a continuous function, and differentiate.
The roadmap distinguishes the four core product results from the supplied
model constructions and the analytic first-stage theorem. It no longer
claims an exhaustive list of four imports or the absence of all smoothing.

The transpose differential is defined for every current. Boundarylessness
has the geometric role of making the integration current closed and removing
flux from compactly supported Stokes tests. A geometric truncation can have
a boundary term. The opening, estimates, hypothesis ledger and global
comparison now use this distinction consistently. A single globally defined
exact potential on a compact boundaryless space has total mass zero;
nonzero line-bundle intersection masses arise from local weights and their
transition data.

The hierarchy argument reuses Chapter 15's whole-sheaf cardinality proof.
Finite sections on nonconvex Euclidean opens are locally convex, with global
convexity asserted on convex opens. A monotone regularization mechanism is
sufficient for collapse, not a formal necessary condition. The retained
Stone, endpoint, finite/infinite-star and product arguments specify their
generator sheaves, common domains, mixed Hessian and junction conditions.
The double-trivalent-star five-atom bound is a barycentric reduction bound;
the off-centre example rules out an unrestricted ambient convex-roof
characterization, not the exact model theorem.

Smooth composition reuses the precise earlier proof: derivatives are
evaluated at the vector of input functions, and the covector diagonalization
is pointwise. It assumes no smooth eigenvector choice. The internally proved
whole-real-space case is distinguished from the published proper-convex-
domain result. Continuous convex composition and its domain are the exact
CLD25 8.2.2--8.2.4 import; maxima have an explicit softmax approximation.
Tropically convex functions use the already proved local-uniform closure.
The G-smooth difference-of-psh decomposition retains decency and imports
the finite-polyhedral results rather than treating arbitrary G-smooth
functions as ordinary smooth functions with a Hessian.

The definition of continuous multiplication fixes finite chart stages on
compact data, measures coefficients on their actual tangent spans, and
projects arbitrary tests to their symmetric parts. Smooth scalar density
and finite local partitions define the uniform extension. The continuity
proof applies to nets. The smooth Leibniz identity has the correct
bidimension range and a separate zero-bidimension endpoint. Without
closedness the product rule has the potential times the Hessian of the
current as well as the two cross terms.

Zero Hessian as an ordinary smooth form is distinguished from zero Hessian
as a current. The latter cannot imply the former without a separate
injectivity hypothesis. Bedford--Taylor independence is explicitly the
continuous-pair predicate in this chapter. The potential remains part of
the notation for a current not known to have that property. The symmetry
proof's comparison subsheaf consists of continuous psh functions, ensuring
that every multiplication used by its closure argument is defined.

The continuity theorem states the bidegrees and number of factors and
justifies pshness of locally uniform limits on compact neighbourhoods.
The CLN constant retains its dependence on the mass of the multiplier
current. The compact-mass proof uses finite chart data and positive
dominators, with the zero-factor case separated. Oscillation estimates
require at least one curvature factor; for one factor they use the
zero-factor CLN estimate. No differentiability of a nonsmooth psh potential
is inferred from these arguments.

## Curves, skeletons and examples

The curve proof inputs were all read at their exact scopes. The arbitrary-
valued normal theorem has no new strictness or rig-smoothness hypothesis.
The componentwise reducible/nonreduced endpoint retains good, separated,
strict, boundaryless, pure dimension-one hypotheses and continuous pairs.
Ordinary CLD calculus is reduction-invariant, while integration retains
generic component multiplicities. Closed-point residue degrees and
inseparable local degrees are retained. The canonical annular expansion
cancels in the intrinsic ratio; a source cutoff is never renamed as an
analytic unit. Rigid zero-atom estimates have their own local hypotheses.
The proof does not assert Borel multiplication for arbitrary order-zero
currents or promote a continuous-pair result to the literal possibly
discontinuous predicate in the printed source.

The skeletal support statement is confined to finite common-chart
presentations. Signed trace measures for arbitrary smooth tests are justified
by positive decompositions. Skeletal normals point from the face into the
cell. In the inward half-space the boundary term is negative, and the
leading minus gives the positive curvature coefficient. Normal derivatives
are taken after subtracting an ambient affine extension of the face value;
closed calibration removes its effect. Calibration-scaled normals are real
vectors, not silently primitive integral vectors.

Harmonic compatibility has the required decency and Bedford--Taylor
hypotheses. The proof treats varying and collapsed cells, common face
calibrations and source test-form coordinates. Harmonic parlinear functions
are locally differences of continuous psh functions; the independence
property then annihilates their product Hessian. Harmonicity is a sufficient
compatibility condition, not a claimed equivalence. G-smooth calibrations
need not be parlinear.

The cross example is itself CLD-harmonic. It separates harmonicity from
respect by an arbitrary positive closed multiplier current, not the first
two harmonicity definitions in the table. Equal unweighted balances can
differ after reweighting; the example gives the actual difference. Failure
of smooth harmonic approximation is proved by continuity of multiplication
and current differentiation, not convergence of ordinary derivatives.
The general approximation question is confined to its stated analytic
setting. The abstract cross disproves the unrestricted tropical version.
The L1 assertion asks for a continuous representative rather than pointwise
continuity of an arbitrarily modified function.

The comparison theorem uses a bounded open convex Euclidean domain and
positive dimension. It is not extended to arbitrary moment charts. Current
positivity implying CLD-psh and classical psh implying CLD-psh are separate
questions. The good analytic first-stage result, which starts with CLD-psh
functions, does not answer the former implication.

The compact tripod computation is a signed graph Laplacian. Its positive
curvature is identified on the open interior. Ordinary tests on a boundary
domain retain derivative endpoint terms; the graph measure uses its stated
constant-near-end tests. The chapter no longer classifies all positive
closed currents on arbitrary one-dimensional fans as multiples of their
integration current: the cross already disproves that assertion.

For the fan of projective two-space, the square of `max(0,x,y)` is computed
directly from its three curvature rays and their primitive slopes. The
separate mixed-product computation for `max(0,x)` and `max(0,y)` does not
identify their sum with that function. Toric normalization uses a split
analytic torus, its Gauss section, lattice Lebesgue measure and the
unscaled Alexandrov convention: the CLD product is the pushforward of
`n! MA_real`. The abstract product-fan example permits ambient convex
regularization, even though translation inside the fan is unavailable.

The one-dimensional CLN calculation uses total variation of the cutoff's
second derivative without calling its absolute value a smooth
decomposition. Curvature mass on the closed interval is the right
derivative at its right endpoint minus the left derivative at its left
endpoint. For `u(t)=max(0,|t|-1)`, oscillation on `[-2,2]` is one and
curvature mass on `[-1,1]` is two; hence the displayed constant two is
sharp. This corrects the old claim that it was nonoptimal.

The polar example separates the unit-ratio chart from the region where
that ratio vanishes. Arbitrary real-radius truncations are continuous
CLD-psh, without an inferred real-PL condition. The canonical extension
comes from the extended potential current; restriction away from the
polar set alone does not select it. The singular limiting potential does
not converge locally uniformly to a continuous function.

Generically finite pushforward retains good, topologically separated,
boundaryless, pure-dimensional source and target, a topologically compact
analytic morphism finite over a Zariski-dense open locus, and the correct
factor range. Its possibly varying real degree acts on completed
coefficient measures, with integrability and exceptional-locus nullity
supplied by CLD25 16.9.5. For arbitrary continuous CLD-psh factors the
supplied analytic first-stage theorem reduces to that exact published
corollary. No redundant projection/exceptional-set argument or constant-
degree restriction is substituted.

The global comparison table carries the Chapter 20 BFJ and Chapter 32/BJ
standing hypotheses, the polar barrier hypotheses, and the common-locus
condition on model transfer. The dictionary names the graph curvature
example accurately and follows the repaired normalization conventions.

## Evidence and remaining boundaries

Fresh CLD25 text checks cover 8.5--8.6, the G-smooth/decent-space
interfaces, 8.10--8.12 continuously, and 16.9 with both seams. The
composition and analytic source geometry checks from Chapters 14--15 are
reused with their recorded scopes. All fourteen selected CLD25 physical
pages were actually viewed: 205--207, 211, 217--223 and 466--468. Its PDF
SHA-256 is `5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719`.
The inward-normal sign is independently derived; the inconsistent signs
in the printed 8.10.3 computation are not copied. The printed all-current
scope of 8.11.3 remains guarded by the book's proved hypotheses.

Fresh BGJKK text checks cover physical pages 36--41. Physical pages
36, 38 and 39 were actually viewed, checking the factorial convention,
toric pushforward and Gauss-section support. Its PDF SHA-256 is
`dee1f0c1e44db73aa69033e23ae9170db5bbfe4cd6f943be954b1b646b1d3b8a`.
The [manifest](second_reading_ch16_manifest_20261003.json) records all
seventeen selected primary pages and their image hashes. No fresh
exhaustive literature search or new full audit of the published curve
source chain is claimed.

These are exposition, construction, proof, example, scope and exact
source-import repairs. Historical independent verdicts retain their
original statement revisions; they do not validate changed statements.
No new independent verdict, original research theorem, problem retirement
or priority claim is made. The elementary sharpness computation is an
example check, not a solution of an inventory problem.

## Final gates

The final full-book build has 4,180 pages and 19,515,576 bytes, SHA-256
`e1450813a326d95b55cccbea4927f60c06ea9fad9ee9cf6c566c67b51a154173`.
There are zero TeX errors, LaTeX/package warnings, overfull boxes,
unresolved references/citations or rerun requests, and 873 nonfatal
underfull boxes. All 274 Chapter 16 physical pages 833--1106 and seams
832/1107 were viewed in 69 initial contact sheets. The short double-line
remark was kept with its displayed example; both changed final sheets were
viewed again and the other 67 are bitmap-identical to the reviewed baseline.
The final formulas, tables, proof pagination, warnings and seams show no
clipping, collision or detached heading.

Post-render references and structure pass for 425 active inputs and
12,564 unique labels, with no missing input, duplicate or dangling
reference. The inventory remains 42 atoms in twelve families, with
tiers `(0,3,7,15,17)`. No formal Chapter 72 problem statement or status
changes, and the standalone catalogue retains its exact scopes and numbering.
Exact hashes and coverage are recorded in
[the manifest](second_reading_ch16_manifest_20261003.json). The review PDF
is `/workspace/book-completion-drafts/second-reading/Ch16_Review_2026-10-03.pdf`.
Chapter 16 passes this second-reading gate. Chapter 17 is next;
no later chapter has yet been marked reread. The whole-book continuation
remains in the cloud, without Xean or default-branch publication.
