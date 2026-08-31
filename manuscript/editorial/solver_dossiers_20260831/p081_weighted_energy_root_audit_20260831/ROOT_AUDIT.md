# Root review of the weighted Ch26/Ch28 energy repair

31 August 2026. Reviewer: root. The frozen principal fragments were authored
by p213_skeletal_hostile; root assigned the correction and reviewed the
completed argument rather than authoring those fragments. This technical
review is not production Rethlas verification or a full-book certificate.

## Verdict and boundary

No substantive gap was found in the three principal replacements, with the
explicit BFJ and elementary graph interfaces below. They preserve the
original discretely valued, residue-characteristic-zero field, the real
semipositive reference form with ample generic class, and a smooth connected
curve, without adding geometric connectedness or split-node hypotheses.

Exact principal hashes:

- Ch26 graph: `32162fefceffa938272c9e7230206496538c5a52290083d6573f3d1faf31ff31`.
- Ch28 stability: `1e7c4a23b1e8bf775f7dfd35502784f906dfb348f3ac496e423cdd3d97d608fd`.
- Ch28 dual energy: `a13394d75406bfe9f94e390ad223354aa28f2e4e78501874944b3f5b8454bfcd`.

The surrounding full-copy Ch28 uniqueness proof still asserted cofinality
of reduced semistable models over the original field. Its corrected
Dirichlet line alone did not fix that independent defect. Root has authored
a separate, not-yet-independently-accepted SNC intersection proof in
`p081_ch28_curve_uniqueness_snc_repair_20260831`. This review therefore does
not accept the complete parent chapter. Ch21/Ch25 retraction repairs and
the independent/production/assembly gates remain outstanding.

## Algebraic realization and real-form scope

On a regular model every real vertical divisor is real Cartier. The values
a_i on components of multiplicity b_i are represented by sum b_i a_i E_i.
The real extension of Ch05's affine-divisor formula is literal linearity,
not an assertion that arbitrary real values define a rational divisor.

On an original reduced SNC edge, successive node blowups give primitive
valuation vectors; adding adjacent vectors preserves determinant one.
The normalized coordinates have difference 1/(b_i b_j), so the subedge
length has exactly the factor needed to identify curvature mass
b_i(D.E_i) with weighted outgoing slopes. The closed-node residue degree
is retained on the subdivisions. The construction allows nonreduced SNC
models, and does not assert cofinality of reduced semistable models.
The optional self-node paragraph is expressly limited to split branches
over the node residue field, and is not needed under the book's SNC
definition of regular semistability.

The pulled-back real reference has degree zero on new exceptional
components. Positive model masses are equivalent to nonnegative component
degrees, because b_i is positive. For a curve model this is precisely
relative nefness. Thus the construction genuinely provides real BFJ model
functions for the original form, not only metrics on one chosen line bundle.

## Arbitrary graph measures and the derivative limit

Positive finite atomic measures of fixed mass supported at rational edge
positions approximate every positive Radon measure on the finite graph.
Their masses need not be rational. The elementary weighted Green lemma
produces piecewise affine potentials with those breakpoints and uniform
convergence of the normalized potentials. The above construction makes
each an actual real nef model function. Uniform BFJ closure and the
continuous BFJ measure operator give the asserted analytic measure.

The additional estimate

    D(U_j-U_k) = -integral (U_j-U_k) d(mu_j-mu_k)
               <= 2 V ||U_j-U_k||_infinity

makes derivatives Cauchy in the finite direct sum of weighted L2 spaces.
Passing to the limit in the edgewise fundamental theorem of calculus proves
absolute continuity of the limit and identifies its derivative. It proves
energy convergence as well as function convergence. This is sufficient for
the non-atomic extension and for differences of two solutions.

For the converse, rational-coordinate real PL tests are uniformly dense.
Uniform model approximation and model integration by parts identify the
distributional graph Laplacian with the pushforward of the BFJ measure.
The uniqueness of the elementary Green solution then identifies the actual
skeletal function and the full analytic measure. No line-bundle-specific
promotion, scalar-pushforward positivity inference, or curve-envelope input
is hidden in this step.

## Energy, stability, and numerical checks

The book's dimension-one model energy is unnormalized by V. It therefore
equals integral u dmu0 minus one half of the weighted derivative energy.
Uniform energy continuity and the separately proved strong derivative
convergence justify the formula for continuous graph solutions.

Weighted Cauchy--Schwarz along an edge-simple path gives the stated bound
with total resistance length sum ell_e/c_e. Since every residue weight is
at least one, this implies the old total-modulus-length bounds. A zero-mass
measure may be paired with the function after subtracting the midpoint of
its range, giving the stronger factor 1/2 used in the proof. Supremum-zero
normalization makes the difference change sign or vanish somewhere, so its
uniform norm is at most its oscillation. The seminorm triangle inequality
then yields the dual-energy bound. The point-graph case is treated without
division by zero. Subdivision and the attachment of new branches are
correctly distinguished, as are fixed-absolute-value base change and
renormalization of a discrete valuation.

The dual-energy formula follows from the existing variational identity at
an actual bounded BFJ solution; it does not require a new maximizer theorem.
Zero energy forces a constant by absolute continuity and connectedness.
The Green double integral is legitimate for a finite signed measure and a
bounded continuous kernel. Its minus sign agrees with outgoing slopes.

For the degree-two blowup example, O(-E) changes component degrees by
(-2,2), its vertex values are (0,-1), and the reference O(2) gives masses
(2,0). The new nef metric has masses (0,2), energy -1, and dual energy 1.
The omitted-weight answers -1/2 and 1/2 are indeed wrong. The corrected
two-vertex admissibility interval -m0 <= b-a <= m1 is also exact; the old
symmetric absolute-value interval need not exhaust the nef region.

## Interfaces checked and mechanical evidence

The complete three fragments, change ledger, validator, changed ancillary
diff hunks, and the following bounded source interfaces were read:
Ch05 affine model functions and SNC cofinality/density; Ch20 standing
hypotheses and vertical intersection formula; Ch21 uniform BFJ closure;
Ch24 model masses, model integration by parts and continuous uniform
approximation/measure convergence; Ch26 energy Lipschitz continuity;
Ch28 dual energy at a Monge--Ampere measure; and the complete elementary
weighted Green lemma in Ch31 revised2. These are mathematical input
interfaces, not independent certification of every surrounding chapter.

The author validator was inspected and rerun read-only. It verifies all
414 old labels, six added labels, exact fragment inclusion, matching full
diff, external label availability, and git apply --check. The frozen log
records only a draft-mode fragment compile using reference placeholders.
It is not a full-book compile, PDF-layout review, or mathematical proof.
The separate local checker rehashes every manifest input/output and records
the exact audit inputs. No live source or frozen parent is changed.
