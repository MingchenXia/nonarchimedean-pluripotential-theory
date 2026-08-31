# Independent exact-byte audit of the initial Ch25 weighted-capacity packet

31 August 2026. Auditor: p213_skeletal_hostile.

## Verdict and explicit conditions

The new core pushforward argument, exact graph competitor equality, weighted
segment formulas, real/irrational-corner attainment, degree-two node
calculation, and half-open ancillary calculation have no mathematical gap
found in this bounded review, CONDITIONAL on the named standard BFJ inputs
and the candidate Ch26 graph-to-BFJ sufficiency lemma.

The initial complete packet is NOT ready for a scope-complete acceptance:
its two ancillary nonuniformity paragraphs do not establish their intended
fixed-(C,theta) quantifier. A required correction and a complete fixed-pair
construction are recorded below. There are also two smaller wording
clarifications: non-rational versus nonsplit node, and coincidence with full
mass versus point/tube capacity equality. Root has been notified and is
authoring a separate revised1; no future bytes are covered by this report.

Independence boundary: I did NOT author the Ch25 repair, but I DID author
its Ch26 graph-lemma dependency. This audit expressly EXCLUDES independent
verification of that Ch26 input. Its exact statement is treated conditionally;
root reviewed it separately, and its own production gate remains. I also
do not certify the unresolved upstream actual-real-model maximum arguments
in Ch20/Ch21. Those gates are not erased by verifying this downstream proof.

## Exact initial bytes and mechanical checks

Author directory:
p081_ch25_weighted_capacity_repair_20260831 under
/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260831.

- MANIFEST.json, 5318 bytes, SHA256
  163dbea4048d2299f49dd7b506b47c4dbaeb8e79e4b287a27375a214d207fb87.
- ch25_curve_replacement.tex, 17122 bytes, SHA256
  de250281d1e66be5b69dd31b16e7a30cdbafd4ad6b0b374e5bb8389316de196b.
- ancillary_consistency_edits.tex, 3212 bytes, SHA256
  a83c0030d05bfe91b58d558b1c40165aed51139352033119f19afd3785a016f5.
- patched/ch25_capacity.tex, 200063 bytes, SHA256
  bc939ba01e4763debb7d73b4d6681592ea70229a7c42814c8c59384b3b4cb1ce.
- chapter.patch, 37922 bytes, SHA256
  7322750e9740a345ea3df785ecb18e595247e494f0ae2403dae324123e324cc6.

All 26 author manifest entries (15 artifacts and 11 inputs) were
independently size-checked and rehashed, with zero mismatches. A separate
read-only reconstruction verified all eleven assembly substitutions, each
matching once, and the core fragment's exact inclusion. The complete patch
was read. An independently generated unified diff equals chapter.patch
byte-for-byte, and git apply --check passes without application.

All 210 original labels remain; the only three additions are
eq:ch25-weighted-skeletal-test, eq:ch25-resistance-coordinate, and
ex:ch25-nonsplit-capacity. There are no duplicate labels.
After inspecting validate_repair.mjs completely and confirming its read-only
operations, I also ran it: all eighteen external label references resolve.
Reference existence is not substituted for a hypothesis or proof check.
The exact checks and source hashes are in VALIDATION.json.

## Required ancillary correction: fixed-pair nonuniformity

Frozen proposed full chapter lines 753--760 and 3663--3677 conclude that
the positive capacities of divisorial points have no uniform positive
lower bound. Their demonstration uses endpoint masses (1,1) on symmetric
chains whose length tends to infinity.

Those displayed computations are correct for each chain. But changing the
chain while preserving reference mass one at both ends changes the reference
data unless an additional common construction is supplied. Thus they prove
nonuniformity across examples, not by themselves nonuniformity over the
divisorial points of ONE fixed (C,theta). The intended stronger assertion is
true, but the exact initial justification leaves that quantifier unproved.
This is a required correction, not merely a stylistic objection.

A fixed-pair repair was derived by this auditor and sent to root:

Fix C=P1_K and theta from the standard O(2) model, so
MA_theta(0)=2 delta_q at the Gauss point q. For each integer N>=1, blow up
successively the smooth rational special-fiber point in the T=0 direction.
The resulting regular reduced model has a chain Gamma_N=[0,N] with N
unit-weight, unit-modulus edges. Its terminal component represents
v_N=zeta_{0,|pi|^N}. These are refinements of models of the same C, and theta
is always the pullback of the same initial model form. Its reference masses
are (2,0), not (1,1) at moving endpoints.

The potential f_N(s)=-s/N on this chain belongs to [-1,0]. Its pullback is
a rational model function, with signed curvature
-(1/N) delta_q+(1/N) delta_vN. Hence

    MA_theta(f_N o p_N)
      =(2-1/N) delta_q+(1/N) delta_vN >= 0.

The endpoint formula read from the v_N-end gives the tube upper bound
min(2,1/N)=1/N. The displayed model puts this amount at v_N itself.
Monotonicity and this exact competitor show

    Cap_theta({v_N})=Cap_theta(p_N^{-1}({v_N}))=1/N -> 0

for the SAME fixed curve and SAME fixed reference form. Smooth-point
blowups in this illustration add the longer chain; this does not conflict
with the node-only subdivisions used in the core fixed-skeleton proof.
Root, not this auditor, is responsible for the frozen source revision.
Any review of that revision should retain this derivation's provenance.

## Core scope and fixed graph

The original BFJ hypotheses are explicitly retained: a complete normalized
DVR with residue characteristic zero, a smooth CONNECTED projective curve,
a semipositive REAL closed model form of ample generic class, and a GIVEN
semistable model determining it. No geometric-connectedness or rational
reference-class assumption is added.

The component convention is smooth components meeting in ordinary nodes.
The text explicitly removes the residue-rational restriction from the
earlier Ch08 presentation; its new degree weights, not the old unweighted
Ch08 formula, are used. Regularizing a thickness-m node gives a unit-edge
chain over the node residue field. The optional fixed node subdivision
separates multiple strata for the manuscript's SNC indexing convention
without changing the underlying graph/retraction. It may introduce
multiplicity-two or higher components. No arbitrary model is claimed to
admit reduced semistable domination.

The local SNC subdivision and vertex-value arguments need no geometric
connectedness. The connectedness of the graph follows from the connected
proper curve/model, for example by the proper formal-functions argument
already present in Ch20. This use does not require an algebraically closed
residue field. The all-SNC density assertion from Ch05 is not needed for
the core test interpolation; only density of rational points in this
fixed finite graph is used.

The measure mu0 retains its original reduced component masses, and the
reference has degree zero on newly inserted exceptional components. Thus
the setup's component-degree description agrees with the actual model
measure even after the stated preliminary node subdivisions.

## Model test identity without semistable cofinality

The model-level construction immediately before the proposition retains
the right multiplicities:

    D=sum_i b_i a_i E_i,
    b_i(D.E_i)=sum_j b_i b_j(E_j.E_i)(a_j-a_i).

For node subdivisions of a normalized unit semistable edge, adjacent
primitive valuation vectors have determinant one. Their normalized
positions differ by 1/(b_i b_j). The intersection degree at the associated
closed node is c_e, inherited on its subdivided edges. Therefore the
right side is the residue-weighted outgoing slope sum. The left side is
exactly the signed curvature atom. This is the specific node-subdivision
calculation, not a blanket reliance on an unproved metric-length formula
for arbitrary nonreduced models.

Any finite rational set of breakpoints can be inserted by the usual
successive primitive-vector sums, terminating by the Euclidean algorithm.
Blowing up the closed node works over its own residue field and defines
the operation over K. Real vertex values give a real Cartier divisor on
the regular model; rational vertex values give a rational divisor.
No rationality of theta or of the real coefficients is inferred.

For an arbitrary real theta-psh model function psi, the auxiliary
t=T o p for a rational-breakpoint real PL test T has signed measure
ddc t=iota_*Delta T. A common model for psi,t,theta is sufficient for
algebraic integration by parts. It need not be reduced semistable or
have a skeleton on which psi factors. Thus

    integral T d(p_*MA(psi)-mu0)
       =integral t ddc psi
       =integral psi ddc t
       =integral psi|Gamma dDelta T.

Each equality has the stated measure spaces and inclusion map. There is
no branch-attachment argument, no omitted residue factor, and no inference
that positive scalar pushforward reflects componentwise positivity.

## Rational tests and the bounded limit

The rational-test uniqueness argument is valid and avoids a subtle false
shortcut: uniform approximation of arbitrary T would not by itself control
Delta T. Instead, for a continuous w annihilating all these tests, interpolate
its exact values on a finite rational subdivision by T. The atomic support
of Delta T is at those vertices, hence integral w dDelta T equals
integral T dDelta T, which is

    -sum_e (c_e/length_e) (w(v_e)-w(w_e))^2.

Every coefficient is positive. Connectedness forces one value at all
vertices; a nested refining sequence with dense rational vertices and
continuity gives one constant on the graph. A point graph is immediate.

The elementary Ch31 Green lemma supplies a continuous normalized potential
for the finite zero-mass measure p_*MA(psi)-mu0 and satisfies ALL PL tests.
Subtracting it from psi|Gamma invokes the preceding uniqueness argument.
This proves the full distributional measure identity, not only identities
on an insufficient test set.

For bounded u, decreasing real-model BFJ regularization is used as a named
input. Restricting to a tail makes it uniformly bounded above and below.
The fixed SNC graph presentation permits clause (2) of the BFJ definition:
u|Gamma is finite and continuous. Dini for nets applies on this one compact
graph. There is no assumed countable cofinal model sequence.

The bounded MA theorem gives weak measure convergence on the analytic
curve. Continuous pushforward preserves weak convergence. For each fixed
test T, uniform convergence of restrictions controls the integral against
the fixed finite signed measure Delta T. The Green/interpolation argument
then gives

    mu0+Delta(u|Gamma)=p_*MA(u) >= 0.

Only at this stage is the CONDITIONAL Ch26 sufficiency lemma invoked to
make (u|Gamma) o p a continuous BFJ-psh function with the claimed analytic
measure. This is a matching application of its hypotheses, not an independent
verification of that lemma in this audit.

## All competitors and all Borel sets

The admissible family U_theta consists of ALL BFJ-psh u with -1<=u<=0.
The pushforward proposition proves its restrictions lie in Q_Gamma.
Conversely, a continuous graph f in the indicated range with positive
mu0+Delta f has total mass V: testing the distributional Laplacian against
the constant one gives mass zero. Conditional Ch26 sufficiency then gives
an actual continuous BFJ competitor f o p. It restricts to f and obeys the
same bounds. Therefore P_Gamma=Q_Gamma is genuinely equality, not merely
density of a rational competitor subfamily.

The measures have already been proved equal before evaluating a Borel
set. Since p is continuous and iota embeds Gamma as a compact closed subset,
both p^{-1}(A) and iota(A) are Borel for Borel A. Thus the capacity formula
is valid for every Borel A; it does not pass to a weak limit on A.

In fact these same facts also imply
Cap_theta(iota(A))=Cap_theta(p^{-1}(A)): monotonicity gives one inequality,
and retracting any admissible u gives the reverse one. Consequently the
unchanged later sentence that a "coincidence is an artefact of the short
edge" should explicitly mean coincidence with full mass V, not equality of
point and tube capacities. This is a recommended wording clarification.

## Resistance coordinates and exact optimizers

For dx=ds/c_e, one has c_e f_s'=f_x'. Edgewise integration by parts becomes
the ordinary x-coordinate identity, and at a junction the jump of f_x'
is exactly the weighted outgoing flux. Thus varying conductances cannot
be suppressed in modulus coordinates, but can be combined through the
specified resistance coordinate. The total length in the formulas is
sum_e length_e/c_e.

With endpoint reference masses m0,m1, graph positivity is equivalent to
convexity and f'(0+)>=-m0, f'(ell-)<=m1. These bounds make the derivatives
finite; the endpoint atoms and interior distributional second derivative
in eq:ch25-segment-measure sum to V.

For the left endpoint, convexity and the range bound force
f'(0+)<=min(m1,1/ell). The displayed affine function
-1+min(m1,1/ell)x meets every constraint and attains the upper bound.

For a closed interior interval [a,b], including a=b, its mass is
f'(b+)-f'(a-), so atoms at BOTH boundary points are included. Convexity,
endpoint constraints, and range [-1,0] give exactly the two stated minima.
The three-piece optimizer has slopes -alpha,0,beta, minimum -1, and endpoint
values at most zero. Its interior masses are alpha delta_a+beta delta_b;
they add when a=b. It is therefore an exact graph optimizer.

For irrational corners its pullback is an actual continuous BFJ competitor
by the conditional graph lemma, NOT necessarily an actual real model
function. No weak-limit-on-a-singleton argument or rational-slope assertion
is used. The limiting cases m0=0 or m1=0 also satisfy the displayed proof.

## Degree-two node and half-open ancillary example

The blowup of P1_R at x^2+1 over R=real formal power series has
D.E=2, E^2=-2, and D^2=-2 as intersection degrees over the real residue
field. Its components have multiplicity one. The restrictions of O(E)
are O_D(z) and O_P1_C(-1), with degrees +2 and -2. Thus -E has degrees
(-2,+2), normalized vertex values (0,-1), and curvature
-2 delta_D+2 delta_E. The O(2) reference has degrees (2,0); twisting by -E
gives (0,2), hence nefness and mass 2 at E. The capacity of that point and
its tube is therefore 2 by the exact competitor and the total-mass bound.
The c=2, modulus=1, resistance=1/2 calculation is consistent.

The node is non-rational over the real residue field; its two branches
are defined over its own residue field C. Calling it "nonsplit" risks
confusing residual degree with nonsplitting of branches. The mathematical
example is correct; the heading should preferably say non-rational.

For the explicitly unit-weight [0,4] example, the half-open set [0,2)
has mass 1+f'(2-). Convexity gives f'(2-)<=1/2. The proposed function,
constant -1 up to 2-epsilon and then affine to zero at 4, is convex,
normalized, and has endpoint slopes within [-1,1]. Its atom at
2-epsilon lies inside the set and has mass 1/(2+epsilon); the atom at
zero contributes 1. These exact admissible masses approach 3/2.
This proves the supremum without falsely invoking the closed-interval
formula or claiming convergence of measures on a half-open set.
No assertion of attainment for this half-open set is made.

The later one-edge/four-edge examples and their consumers explicitly
inherit unit residue weights. Their displayed table entries and the
comparison example's masses were checked in the new context. The
fundamental-estimate and comparison inequalities are not reproved as
general theorems by this ancillary audit.

## Dependency gates and excluded material

The full CH21_INPUT_AUDIT.md was read. Its R5 issue is real: over the
original normalized DVR, max(0,s-a) with irrational a has an irrational
corner and need not be an ACTUAL real model function, even though each
input is a real model function. BFJ psh maximum closure is not thereby
disproved, but the existing Ch20/Ch21 proof route needs repair.
Standard BFJ regularization and bounded MA are conditional correctly
stated inputs here; this audit does not approve every existing manuscript
proof used to derive them.

The Ch26 sufficiency input uses model positivity, uniform closure,
continuous MA, and elementary Green theory, not capacity. The Ch31
elementary Green proof was reread completely; it uses finite weighted
linear algebra, energy, a bounded continuous kernel, and its own continuous
uniqueness argument, not the later analytic equation/existence theorem.
Thus the forward dependency is acyclic conditional on those input packages.
The new Ch25 proof does not import the defective Ch21 curve retraction
argument or the false cofinality of reduced semistable models.

The later Thuillier relative-capacity subsection, proposed lines
3232--3580 approximately, is EXCLUDED. Its complete byte block up to
Worked examples is unchanged by assembly. The all-field/quasimonomial
scope and unweighted references identified in the author ledger remain
for separate review; preserving those pages and labels does not verify them.

No live manuscript or frozen source was edited. No production call, full-book
compile, PDF generation, or general-envelope/open-problem retirement occurred.
The required ancillary revision, independent review of the Ch26 dependency
by another reviewer, upstream real-model/max repairs, production permission,
and coordinated integration remain separate gates.
