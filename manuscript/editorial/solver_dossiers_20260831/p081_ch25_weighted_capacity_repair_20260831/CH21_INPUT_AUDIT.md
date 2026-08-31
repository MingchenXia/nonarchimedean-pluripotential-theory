# Ch21 curve-input audit and bounded Ch25 repair

Date: 31 August 2026. Author-side source audit, not an independent or production verdict.
No live source or earlier frozen dossier was edited.

## Exact reviewed sources

The complete source ledger is SOURCE_HASHES.json. Principal hashes:

- Live Ch21: 477db8e896633bcf5f89c8738e16e0afa8eaac55f36042c1d263b683daed72b3.
- Live Ch20: 531024045204686aaf0fc12ff0e825bf67367551cd310a26c956740b4d164baa.
- Live Ch25: 47c5c5897173168f9d5e21cbb7bdd86338ccf4e72b466f84acea917ea2b25fad.
- Candidate Ch26 graph section: 32162fefceffa938272c9e7230206496538c5a52290083d6573f3d1faf31ff31.
- Candidate Ch31 revised2 curve section: eafd97355fda0739ec1135b36b247c43a6816ac754e4d154d9acf9168bae4b5d.

Read the complete Ch21 curve proposition and proof (1770–1915), the definition and
skeletal closure discussion (350–435), model-skeletal input (749ff, including its
proof in the earlier review), and uniform/max stability (1935–2050ff).
Also read Ch22 decreasing regularization and its proof (2855–2970), Ch24 model
integration by parts and proof (815–867), bounded extension statement and defining
weak-limit construction (1561ff), and continuous-uniform proposition and proof
(2061–2125). Read the complete candidate Ch26 graph section, the complete
elementary Ch31 weighted Green lemma/proof, and Ch23's envelope-regularity
statement/proof/dependency explanation (1435–1558). This is a bounded interface
audit, not a fresh independent audit of every deep BFJ input.

## R1 — Missing weights in the Ch21 curve test and flux

Ch21:1808–1860 cites the unit-weight equation eq:graph-laplacian while the standing
residue field need not be algebraically closed. Each node contributes its degree
over k. Both endpoint flux terms must carry the SAME c_e=[kappa(z_e):k].
Vertex constant-field degrees are not a substitute for this edge weight.

The Ch25 replacement defines the weighted operator explicitly and derives its
model formula from the FIRST algebraic identity eq:ch20-curve-laplacian, with
the multiplicity factor b_i retained. It does not use the defective unweighted
graph identification later in that Ch20 proposition.

## R2 — False graph-theoretic reason for single-point attachment

Ch21:1839–1843 says that a component of the complement of a connected subgraph
attaches at one point merely because it is a graph. In a triangle, take one
closed edge as the connected subgraph. The remaining open two-edge path has
closure meeting it at BOTH endpoints. Single-point attachment for appropriate
skeletal refinements is a geometric statement, not this graph-theoretic fact.

The Ch25 proof avoids attached-branch combinatorics entirely. It uses ordinary
common domination only to evaluate the algebraic model intersection pairing.

## R3 — Rational divisors, real models, and nonreduced refinements

Ch21:1865–1873 turns a real model restriction into a vertical Q-Cartier divisor
without a rationality hypothesis. Even on a unit edge, an irrational real
multiple of a nonconstant rational model function has irrational vertex values,
whereas values of Q-model functions at original-field divisorial points are
rational under v(pi)=1.

Furthermore, arbitrary rational subdivisions need not be reduced semistable:
blowing up the node xy=pi inserts the midpoint with exceptional multiplicity two.
The original-field valuation at that midpoint has v(x)=1/2. It cannot be the
normalized valuation of a multiplicity-one component on a reduced regular model,
whose value on x is integral. An arbitrary model carrying such data therefore
cannot be made a higher REDUCED semistable original-K model by domination.

The Ch25 construction uses D=sum b_i a_i E_i on regular SNC node subdivisions,
allowing b_i>1 and arbitrary real a_i. A preliminary fixed node subdivision also
satisfies the manuscript's irreducible-strata indexing convention, while retaining
the underlying graph and retraction. No field extension is introduced.

## R4 — The final all-model net in Ch21 is not proved by that argument

Ch21:1897–1902 takes the reconstruction net over determining models and calls
every retraction psh by the just-proved semistable assertion. The cofinal models
in the general BFJ definition are SNC and can have nonreduced special fiber;
reduced semistable original-K models are not cofinal. The final inference needs
an SNC retraction argument, not a silent switch in model category.

The Ch25 proposition proves exactly the bounded statement needed there for the
given semistable skeleton, without importing prop:ch21-curve-retraction.
It does NOT repair the full singular/all-SNC Ch21 retraction assertion.

## R5 — Broader real-model maximum defect in an upstream Ch21 input

Live Ch20:1917–1975, prop:ch20-model-max, says that actual real model functions
D(X)_R=colim Div_0(model)_R are stable under finite maxima. Its last step invokes
rational approximation and closedness on a common finite-dimensional space.
That assertion is false over the original DVR.

Concrete diagnostic: on a unit-weight segment with parameter s in [0,1] and
reference measure delta_0+delta_1, the affine potentials 0 and s-a, with a an
irrational number in (0,1), are real psh model functions. Their pointwise maximum
max(0,s-a) has a corner at the irrational point s=a. No original-field model has
a divisorial vertex there: values of s at divisorial points are rational.
After SNC domination, each actual real model function restricts to a finite
real-linear combination of piecewise affine functions whose breakpoints have
rational coordinates, and therefore cannot have this corner.
The maximum can be a continuous BFJ-psh function without being an actual real
model function.

Ch21's proof of itm:ch21-stab:max invokes this false actual-model maximum
assertion around 2030. The BFJ maximum-closure theorem is not disproved; its
real-model approximation proof needs repair. The ordinary uniform-closure item
used directly by the present Ch25 construction is formal from the defining
uniform closure and does not invoke maxima. Nevertheless the larger manuscript
prerequisite graph for decreasing regularization/envelope results must account
for R5. The present repair treats the correctly stated standard BFJ regularization
and bounded operator as inputs; it does not certify all upstream manuscript
proofs. Root was notified before freezing this dossier.

## Dependency direction, with the exact limitation

The direct argument runs as follows:

1. Ch20's algebraic intersection formula + Ch24's model measure and IBP give
   rational-coordinate skeletal test identities.
2. Ch21's defining uniform closure gives continuity on the fixed SNC skeleton.
   Ch22's standard decreasing regularization + Dini give uniform convergence
   there for a bounded psh limit; Ch24 gives weak convergence of bounded MA.
3. The elementary Ch31 Green kernel and interpolation of continuous values show
   that the rational-coordinate tests identify the finite distributional Laplacian.
4. ONLY the sufficiency direction of the candidate Ch26 real-form graph lemma
   turns this positive graph measure into a continuous BFJ-psh pullback with the
   desired MA measure.
5. Taking all normalized bounded competitors gives P_Gamma=Q_Gamma and the
   capacity formula.

The Ch26 lemma's sufficiency proof constructs positive real model approximants
from positive atomic graph measures, uses Ch21 uniform closure and Ch24 uniform
MA continuity, and uses the elementary Ch31 kernel. It does not use Ch25 capacity,
Ch26 finite-energy theory, Ch28 dual energy, or the Ch31 analytic line-bundle
existence theorem. Ch22 regularization uses Ch23's general envelope theorem,
whose displayed dependency route is base ideals/multiplier ideals, NOT the later
curve-capacity section. Thus the new forward reference creates no capacity cycle,
conditional on the stated standard BFJ input theorems. This acyclicity check is
not a blanket certification of the existing proofs; R5 remains a separate gate.

## Other boundaries left unchanged

The subsequent Thuillier relative-capacity subsection is not rewritten here.
Its statements identifying quasimonomial points using all semistable original-
field models and its unweighted operator references at original Ch25:3146,
3153, 3329 and 3394 need a separate scope/source audit. The present artifact makes
no assertion that those all-field statements have been repaired.

Later Ch29 numerical examples using the same segment formulas must use resistance
coordinates or the explicit unit-weight example. Root owns their integration
audit. The Ch28 uniqueness consumer of eq:ch25-curve-ma needs the separate
original-field SNC proof already being prepared by root; it is not repaired by
preserving this label alone.
