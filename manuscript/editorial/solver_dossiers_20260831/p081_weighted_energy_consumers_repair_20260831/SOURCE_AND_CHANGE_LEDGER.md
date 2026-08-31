# Source interfaces and bounded changes

Date: 31 August 2026. AUTHOR CANDIDATE; independent root review and
production verification remain gates. No live chapter has been changed.

## Frozen input boundary

- Live Ch26 SHA256:
  `242f10b4c8be9e90bc457f897999f00d24d011a6c1b564436fe9c3a82f8d3d3d`.
- Live Ch28 SHA256:
  `1bb59ce13a77fb7c6a2153f77e20eae7a340d84e727f2a76bb314c10c14b56a5`.
- The separate independent assembly audit was completed BEFORE authoring
  these files: sibling `p081_ch29_ch31_assembled_independent_audit_20260831/INDEPENDENT_ASSEMBLY_AUDIT.md`,
  SHA256 `59038867a7128f6361620623e42da19a9f64a2cded08d6832bef6cb69cb556c9`;
  its manifest SHA256 is
  `802cd27894a614c1dc746160ffee6c9fee92fc8d8388e30595abd88e50853c17`.
  That audit diagnoses the old discrepancy; it does not accept this repair.
- Elementary graph input: `lem:ch31-green-kernel` and its complete proof in
  sibling `p081_ch29_ch31_weighted_full_scope_isolated_repair_20260831/revised2/ch31_curve_replacement.tex`,
  SHA256 `eafd97355fda0739ec1135b36b247c43a6816ac754e4d154d9acf9168bae4b5d`.
  This graph lemma does not depend on any Ch26/Ch28 energy theorem or any
  analytic equation/envelope theorem. The O(E) example there is cited only
  for comparison of signs; the new O(-E) example is computed in full here.

The analytic Ch31 line-bundle solution proposition is NOT an input. It would
not alone establish the real-form or merely-connected-curve hypotheses here.

## Exact existing interfaces used

The final manifest hashes the exact source files. These are bounded
interfaces, not independent certification of entire input chapters.

1. Ch05 `lem:model-function-affine` and `prop:vertical-divisor-affine-iso`:
   rational vertical divisors on SNC models. Real linearity gives the real
   formula; the proof explicitly constructs D=sum b_i a_i E_i, without
   asserting rational slopes or coefficients from arbitrary real values.
2. Ch20 `eq:ch20-curve-laplacian`, FIRST algebraic identity: regular models,
   arbitrary positive component multiplicities, real vertical divisors,
   actual intersection degrees. Multiplication by b_i gives curvature mass.
   The nearby old unweighted graph prose is not an input.
3. Ch24 `eq:model-mixed-measure`: mass is b_i times component degree.
   `prop:model-integration-by-parts` permits real model test functions.
   `prop:ch24-continuous-uniform` supplies uniform-to-weak continuity for
   continuous BFJ-psh functions in the original real-form setting.
4. Ch21 `thm:ch21-stability`, item `itm:ch21-stab:unif`: uniform closure.
   The converse uses decreasing BFJ regularization and Dini for a continuous
   psh function. The line-bundle-specific continuous-Zhang statement is not
   used to narrow the real-class argument.
5. Ch26 `eq:model-energy` and `eq:ch26-energy-lipschitz`: model energy and
   uniform energy continuity. Strong derivative convergence is separately
   proved; uniform function convergence is not mistaken for energy convergence.
6. Ch28 `prop:ch28-dual-energy-of-ma` applies after the construction produces
   an actual continuous BFJ-psh solution. Bounded functions belong to E1 by
   `itm:ch26-e1:bounded`. No envelope differentiation is used.

The new proof stays over the original discretely valued BFJ field.
Normalized original edges have length one. Node blowups insert mediant
primitive valuation vectors, preserving adjacent determinant one. This
gives every rational point by the Euclidean algorithm and subedge length
1/(b_i b_j). Closed nodes are blown up over their own residue fields;
inserted nodes retain that field. Nonreduced SNC fibers are permitted.
Positive mass b_i times component degree is equivalent to nefness since
b_i>0. No scalar extension or rational metric approximation is needed.

The book's regular semistable convention has smooth components and reduced
SNC fiber. For ordinary self-nodes with two branches defined over the node
residue field, the proof explains preliminary node blowups: an exceptional multiplicity-two vertex
subdivides the loop at its midpoint, leaving the metric graph and retraction
unchanged. These are not smooth-point blowups that can attach branches.

For a positive measure on the graph, positive atomic approximations at
rational positions produce REAL piecewise affine Green solutions. Their
vertex values need not be rational. The explicit real-divisor calculation
makes them actual real nef model functions. Weak atomic approximation gives
uniform potentials, and the additional estimate

    D(U_j-U_k) = -integral (U_j-U_k) d(mu_j-mu_k)
               <= 2 V ||U_j-U_k||_infinity

proves strong weighted L2 derivative convergence, absolute continuity of
the limit, and integration by parts. This repairs the old unsupported
derivative-energy passage for a nonatomic measure.

## Changes and preserved scope

The Ch26 graph fragment adds that real-BFJ bridge, corrects the two existing
energy equations with residue weights, proves the continuous finite-measure
extension, and includes a complete semipositive O(-E) counterexample.
The curve is only smooth connected projective; omega remains an arbitrary
real semipositive closed model form of ample generic class.

The Ch28 stability fragment defines the existing D_Gamma as weighted energy.
All old total-modulus-length bounds and labels are retained, with an optional
stronger resistance-length bound. The dual estimate is algebraically
expanded to avoid an inverse length when the graph is a point. The proof
includes the finite-energy step and full seminorm argument. Refinements
distinguish subdivisions from attached branches. Base change distinguishes
extension of the fixed absolute value from renormalizing a discrete valuation.

The Ch28 dual-energy fragment keeps the proposition/equation/remark labels
and proves the weighted identity for arbitrary positive measures on the
finite skeleton, including nonatomic ones, in the full real-form scope.
Its continuity passage uses strong derivative convergence, not uniform
convergence alone. The Green-kernel citation names the actual graph lemma.

Additional bounded edits in the full proposed copies:

- Ch26 introductory Dirichlet discussion and dictionary display weights.
- The triangle-gauge, two-vertex, and four-component numerical examples
  explicitly state their unit residue weights; their numbers are unchanged.
- The two-vertex admissibility sentence now reads -m_0 <= b-a <= m_1,
  exactly its two nonnegative masses. The old absolute-value bound was only
  a symmetric sufficient subregion when m_0 differs from m_1.
- Ch28 introductory/synthesis references use the real-BFJ bridge rather than
  the narrower analytic Ch31 proposition. The introduction specifies the
  fixed-skeleton problem, not arbitrary curve measures.
- The affected graph step in Ch28 uniqueness first uses harmonic tent tests
  before the weighted derivative integral; continuity alone does not provide it.
- Ch28's numerical examples remain explicitly unit-weight. The old claim
  that the sharper factor 1/2 fails under refinement is removed: it remains
  valid on every fixed refined weighted graph.

All 414 old labels are retained; six new labels are added. No general theorem
is restricted to split nodes, rational classes, one line bundle, or geometric
connectedness. V is the degree of the real generic numerical class, not an
undeclared line bundle L. All changed full-copy bytes are visible in the diff.

## Cross-reference and integration boundary

The changed labels have consumers primarily inside Ch26/Ch28 and in Ch29/Ch31
curve examples. Explicit split examples keep their numerical values. Ch31
revised2 already displays weighted general energy. Ch29/Ch31 are owned by
another author and are not edited here. The read-only validator maps every
external core reference to an exact live or frozen proposed source file.

Root separately owns the Ch20 graph-sentence correction: E_i.E_j is a sum
of residue degrees, not a bare number of nodes. The old bad graph prose is
not used here, but must be repaired for coherent integration. Ch23 envelope
transport is separate as well. The earlier retraction inputs of the existing
Ch28 uniqueness proof are not globally reaudited by this bounded repair;
only its affected graph step is changed. Full copied chapters preserve
unrelated original prose and are not blanket mathematical endorsements.

No disputed GJKM Proposition 3.1 or 3.10 is used. There is no new conclusion
about arbitrary complete fields, nonskeletal continuity, the general envelope
property, or the open P21.3 problem.

## Mechanical checks only

The validator is read-only: fixed live hashes, old labels, duplicate labels,
exact fragment inclusion, external references, exact diff, and git apply
--check without application. Draft compilation uses explicit mechanical
external-label placeholders, NOT mathematical input statements. No PDF,
visual QA, full-book compile, production submission, or permission workaround
is claimed. A fresh ledger-write review timeout was reported to root; root
authorized exactly one ordinary same-tool retry, not any older blocked work.
No loop description for a conjugate-branch node is asserted.
