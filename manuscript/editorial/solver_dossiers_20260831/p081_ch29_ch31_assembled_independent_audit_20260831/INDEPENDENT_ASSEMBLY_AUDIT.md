# Independent audit of the assembled Ch29/Ch31 replacements

Date: 31 August 2026. Auditor: independent subagent `p213_skeletal_hostile`.
This is an audit record, not a manuscript replacement, production submission,
or assertion that the book has been repaired.

## Verdict and exact scope

The frozen first assembly has one insufficiently explicit proof step in the
real-form reverse positivity argument. The newly frozen `revised2` repairs
that step without restricting the theorem to a single line-bundle Chern
class. Its new local-potential argument and both new worked examples have
been checked below. No unresolved mathematical gap was found in the revised2
Ch29/Ch31 fragments, conditional on the previously accepted interfaces of
P063, the corrected positive-degree P081 theorem, and the separately audited
real-class rational-model envelope packet.

This is NOT an acceptance of integration into the present book. Two broader
Ch23 callers require their own BFJ real-model argument, and the currently
unweighted Ch26/Ch28 energy identities are false for nonsplit semistable
models. They are not repaired by preserving a label in Ch31. Production
verification and a rebased full-book compile remain additional gates.

The equation theorem's arbitrary-field scope is an actual GIVEN proper
strictly semistable formal model over the original complete nontrivially
valued field, a positive-degree line bundle on a smooth proper geometrically
connected curve, and a positive measure of matching mass supported on that
finite skeleton. The reference constructed without a given model reference
is Thuillier-lisse, not declared rational formal. No arbitrary nonskeletal
measure continuity theorem is proved.

The real-form criterion concerns an actual real numerical closed model form
on its determining model and an actual rational model function with the
asserted skeletal factorization. The envelope uses rational model
competitors. It is not silently identified with either the real linear span
of model functions or the all-PSH envelope. The degree-zero branch requires
an actual rational model competitor. None of these conclusions solves the
general envelope problem or retires the open P21.3 rigidity problem.

## Frozen artifacts checked

All paths below are relative to
`manuscript/editorial/solver_dossiers_20260831/` unless stated otherwise.

First assembly, in
`p081_ch29_ch31_weighted_full_scope_isolated_repair_20260831/`:

- `ch29_curve_replacement.tex`: SHA256
  `63d8d6d5c2136579bc9a4990dda7a3bbf1975c2f07dd7ca39310bd10f5dc6a53`.
- `ch31_curve_replacement.tex`: SHA256
  `3d49d8265f23e1d07a0af48b1338bf152ace015f24304f2bf206abfc8e755b51`.
- `MANIFEST.json`: SHA256
  `0e0f870b5f1aa6208b72ae9512915923a05c8b74b8b506b44d2861069b44afb3`.

Revised2, in that directory's `revised2/` subdirectory:

- `ch29_curve_replacement.tex`: SHA256
  `3760582c91ed79994f0d6817adfecd08a80eb720ff12c27b39b11966893b1d0c`.
- `ch31_curve_replacement.tex`: SHA256
  `eafd97355fda0739ec1135b36b247c43a6816ac754e4d154d9acf9168bae4b5d`.
- `MANIFEST.json`: SHA256
  `c36b29ce080d0269955f58f3dd8069561338c75afafe49657c4e2f1e229176ec`.
- `fragments_from_frozen.patch`: SHA256
  `f2c9dab13229dddd4e6c13ff1411ed600da03e998299264d00d3c436a1455959`.

Every one of the first manifest's 25 recorded entries and revised2
manifest's 35 recorded entries was independently rehashed and size-checked:
zero mismatches. This includes their recorded live bases and mathematical
inputs. The accompanying audit manifest records additional source and
consumer bytes. The complete first fragments were read (742 and 413 lines),
and the complete revised2 fragment difference and its gate/ledger were read.
The initial GATE.md and ASSEMBLY_AUDIT.md were read, not treated as proof.

The prior weighted revised1 statement/proof hashes are respectively
`010711e1a42f4d3ad16ab9b7eb6233a585a1e410ddc420b8b6d70cf0c7c4fc71`
and `30af723c7f07a201ffe4e7a57227867a612cd4cf425fff800babb1db3f18ee3d`.
The prior real-class envelope revised1 statement/proof hashes are
`944fc4672a83bf038b068af1a70da1563b4950752ee1eb5ae89ee2f4b2db0b30`
and `bd98ca99d636a1f40872412e2ababc7f44a5ccb5416b31bcbd83b957515031d6`.
Their earlier independent audits are explicit mathematical inputs here,
not substitutes for checking their assembly or a claim of production status.

## R1: reverse positivity for a real model form

In the first Ch31 fragment, lines 172--184 pass from weighted original-field
inequalities to upstairs componentwise nefness using real linearity,
base change, and nefness reflection. Those words do not by themselves
establish the needed intermediate positivity. Ordinary pushforward adds
masses in a fiber; nonnegativity of the sum alone does not establish the
sign of each lifted mass. Nefness reflection applies only AFTER upstairs
nefness has actually been established.

The criterion itself is supported by published GJKM Proposition 3.7 with
the arbitrary-K, real-form hypotheses in its preceding Section 3.6. It is
not a false statement. Nevertheless the assembled attempt to explain the
source's compressed base-change step needed a complete argument, especially
because a real model form need not be the Chern class of one line bundle.

Revised2 Ch31 lines 182--268 supply the following sufficient argument.
On the actual determining model write theta as a finite real sum
`sum_i r_i c1(M_i,metric_i)` of model line-bundle classes. On simultaneous
local frames put `H=sum_i r_i(-log||e_i||)+F o p`. Formal weights are
Thuillier-lisse by clearing tensor denominators and using analytic unit
logarithms on a strict-affinoid G-cover. The actual skeletal model function
is also lisse. Real linearity proves the equality of SIGNED local curvature
measures to the original weighted graph measure, even for negative or
irrational coefficients. It does not assert positivity term by term.

If that measure is positive, the WHOLE H is subharmonic by Thuillier
Theorem 3.4.12(ii). Corollary 3.4.5 preserves this under scalar pullback
to the completed algebraic closure. On a common strictly semistable model
actually determining all pulled-back metrics and the function, their
real-linear component formula identifies each individual component degree
with its curvature coefficient. These coefficients are nonnegative.
Only now is real numerical nefness reflected to K by the already proved
degree/projection-formula argument. This avoids the aggregation fallacy.

Frame changes add harmonic real unit logarithms. Another representative of
the same numerical class has the same component degrees and thus the same
curvature current; local differences are harmonic by Thuillier Lemma
3.3.12. A global function or a single actual metrized line bundle is not
needed. The forward direction pulls back nefness, reads positive upstairs
curvature, and uses ordinary scalar pushforward only to preserve positivity.
No positivity is inferred from individual terms of a positive sum.

Resolution: R1 is closed for the exact revised2 fragment. The argument does
not justify applying the criterion to an arbitrary BFJ-psh function lacking
the actual rational-model/factorization hypotheses.

## R2: transported labels are not transported hypotheses

The current live Ch23 references have a different competitor class.
Its raw envelope is over all PSH functions (lines 194--205). Its real-model
envelope uses D(X)_R (lines 233--265), not the rational-model envelope.
The fixed-model envelope in lines 2311--2335 likewise uses real model
functions. These distinctions must survive repairs.

1. In Ch23 lines 2851--2873, the explicit-example proof starts with an
   arbitrary PSH competitor and invokes `eq:curve-slope-criterion` at line
   2865. The replacement label is a criterion for an actual rational model
   function with a specified factorization. It cannot directly discharge
   this call. A BFJ real-model and limit/retraction bridge is needed within
   Ch23's existing discretely valued characteristic-zero regime.
2. In Ch23 lines 2886--2905, `rem:ch23-model-dependence` treats real chords
   as admissible and concludes equality with the all-PSH envelope. The new
   rational-model theorem expressly does not identify arbitrary real chords
   with rational model functions or its envelope with all-PSH. This caller
   also needs its own BFJ real-model argument; narrowing the old conclusion
   to the new rational-model theorem would not preserve its scope.
3. Ch27 lines 1885--1898 depends on that Ch23 fixed-model/full-envelope
   equality and an old Ch29 proof pointer. It must receive the repaired
   Ch23 theorem and an accurate pointer, not inherit an unproved equality.

Other checked callers include Ch08, Ch19, Ch22, Ch23, Ch26, Ch27, Ch28 and
Ch30 at the labels recorded by the cross-reference search. The explicit
split projective-line/Tate graph computations remain valid in their stated
unit-weight settings. Statements explicitly restricted to the published
ample rational-model continuity theorem are not invalidated. This is a
bounded changed-region and consumer audit, not an audit of every theorem in
those entire chapters.

Resolution: revised2 correctly flags these callers as a separate gate; it
does not repair them. Root is preparing the separate Ch23 replacement.

## R3: an existing Ch23 approximation-loop gap and its exact repair

In `prop:ch23-model-vs-psh-envelope`, Step 2 at live Ch23 lines 730--734
first approximates psi on a fixed skeleton Delta_Z by chi, enlarges Z to
determine chi, and says to repeat the approximation after enlargement.
The second chi need not be determined on the enlarged Z. No termination
or compatibility argument is supplied for this repetition.

There is a direct same-scope repair requiring NO new approximation theorem.
Keep the originally chosen Z fixed. Ch21
`lem:ch21-model-skeletal-properties`, lines 749--760, gives
`chi <= chi o p_Z` for any theta-psh model chi when Z determines theta;
equality is not required. If chi approximates psi from within epsilon on
Delta_Z, the original estimates yield, for every x':

    chi(x') <= chi(p_Z(x'))
             < psi(p_Z(x')) + epsilon
             <= f(p_Z(x')) + epsilon
             < f(x') + 2 epsilon.

Thus chi minus 2 epsilon is the required real-model competitor under f.
The distinguished point x remains on the original skeleton, so the lower
estimate at x in Step 4 is unchanged. This recovers the original 4 epsilon
comparison. No factorization of chi and no iterative enlargement is used.
The full relevant Ch23 proof and the stated Ch21 lemma/proof were checked.

Resolution: the repair is valid as a proposed argument, but this report does
not certify unexamined future Ch23 bytes or change the live proof.

## R4: the live Ch26/Ch28 energy formulas omit residue weights

Ch26 `prop:ch26-graph-energy`, lines 3393--3427, allows a general regular
semistable curve model. Its formula uses unweighted modulus-length energy
`integral |u'|^2 ds`, although its integration-by-parts citation now points
to the weighted `eq:graph-dirichlet-sign`. Ch28 lines 2740--2753 define the
same unweighted energy and lines 2813--2820 and 2922--2963 reuse it for
stability and dual energy. Ch31's newly weighted introduction cites the
still unweighted Ch26 proposition. This is a mathematical discrepancy,
not merely a notation mismatch.

Here is an explicit semipositive counterexample already inside the old
discretely valued residue-characteristic-zero setting. Let
`K=R((pi))`, `-log|pi|=1`, and blow up `P1_{R[[pi]]}` at the smooth special
closed point defined by `x^2+1`. Its residue field is C. The regular strictly
semistable special fiber consists of the strict transform D and exceptional
E=P1_C, both of multiplicity one, meeting at a degree-two node. Its skeleton
is one edge of modulus length one and residue weight two.

Take L=O(2), the pulled-back reference model O(2), and u the model potential
of O(-E). The reference masses are `(2,0)` at `(v_D,v_E)`. The exceptional
normal bundle satisfies `O(E)|_E=O_{P1_C}(-1)`, of degree -2 over R, while
`O(E)|_D=O_D(p)` has degree +2. Hence O(-E) has component degrees `(-2,+2)`.
Its endpoint potential values are `(0,-1)` and its outgoing weighted
Laplacian is `-2 delta_{v_D}+2 delta_{v_E}`. The modified O(2) model has
degrees `(0,2)`, so it is nef; its curvature is `2 delta_{v_E}`.

The dimension-one energy identity therefore gives

    E(u) = (1/2)(integral u dmu_0 + integral u dmu_u) = -1.

The printed unweighted graph formula gives -1/2 instead. Likewise
`E^vee(mu_u)=E(u)-integral u dmu_u=1`, whereas half the unweighted graph
energy gives 1/2. The O(-E) sign here is intentional: revised2's pedagogical
O(E) table has the opposite signs and is a signed-curvature example, not a
nef example.

The correct differential energy is
`D_c(u)=sum_e c_e integral_e |u'|^2 ds` with modulus lengths unchanged.
The natural resistance length for estimates is `ell_e/c_e`, not a change
of the analytic slope convention. For residue weights c_e>=1, the old
total modulus-length bound can also be retained as a weaker bound because
`sum ell_e/c_e <= sum ell_e`. Any repaired proof must say which is used.
Ch28's further claim that every semistable refinement is only subdivision
is too strong: attached branches may occur. Its unconditional assertion
that finite base change multiplies analytic lengths by ramification index
also ignores the distinction between an extended absolute value and a
renormalized one, and possible splitting. These descriptions require
correction with the formulas.

Resolution: this remains an integration-blocking live consumer defect.
The separately requested Ch26/Ch28 author repair will have its own directory,
input hashes, gate and independent root review. It is not part of this
independent assembly verdict.

## Revised2 additional checks and dependency direction

The new nonsplit example uses O(E), not O(-E). At a degree-r node of the
blowup of a smooth special point, its component degrees over the base residue
field are (+r,-r), its endpoint potentials are (0,1), and its weighted
Laplacian agrees. The exceptional component's own constant-field degree
is -1, so omitting the base-field degree factor would be wrong. The local
chart pi=t z and the frame t^{-1} give these signs. An unramified residue
splitting produces r weight-one edges whose ordinary pushforward gives
the original factor r. This example was checked without claiming that its
degree-zero model metric is nef.

For the new two-edge abstract graph of lengths 1 and sqrt(2), unit weights,
and equation Delta U=delta_y-delta_q, the endpoint value sqrt(2)-2 and
slopes sqrt(2)-2 and 1-sqrt(2) satisfy continuity and both vertex equations.
Integral masses do not force rational slopes. No unsupported realization
over a specified field is asserted.

The subdivision wording now preserves the analytic coordinate and says
the new lengths sum to the old length, retaining each inherited weight.
The model-reference proposition now explicitly fixes its normalizing q.
The real atomic approximants are identified as finite linear combinations
of Green kernels, not incorrectly called rational formal metrics.
Nonatomic limits are continuous, not automatically lisse.

The envelope proof uses its own strict-margin rational construction and
finite-normal descent; it does not depend on the weighted equation. The
equation first uses the elementary graph Green lemma and the point-reference
construction. Its rational-formal promotion applies P063 and corrected
positive P081 only over the completed algebraic closure, then descends
actual approximants using the finite-definition/model-independence/nefness
reflection inputs and finite-normal envelope descent, including inseparable
extensions. The Ch31 model-reference proposition is downstream. The graph
lemma itself does not depend on that proposition. No circular analytic
existence argument was found.

Neither disputed GJKM Proposition 3.1 nonemptiness nor Proposition 3.10 is
used to prove the new real-class theorem or promotion. The degree-zero
Tate obstruction remains compatible with the stated actual-competitor
requirement and is not presented as an ample-envelope counterexample.

## Primary sources and mechanical limits

Published GJKM Section 3.5--3.8 was checked in full in the local source text;
the complete printed pages 2341--2346 were visually inspected from the PDF,
including the actual arbitrary-K and real-form hypotheses of 3.6--3.7,
rational model-function condition of 3.5, retraction claim of 3.8, and the
finite-normal/purely inseparable descent context. The source PDF SHA256 is
`6ab4515546f428a7af02268064566b363ca00fa375e268ca661038489d98ab69`.

Thuillier's weighted graph/current and scalar-pullback results, CLD model
curvature normalization, and GM model independence/finite definition/nefness
reflection are the exact source interfaces read in the prior weighted
audit. Their source bytes are recorded in this report's manifest. This
audit uses those already checked interfaces, not new citations to a
secondary summary. The revised2 proof invokes them with the original-field
hypotheses specified above.

The author records draft-mode fragment compilation only. No revised2 PDF
was produced and no full-book compile was performed in this audit. Exact
hashes, syntax checks, and retained labels do not establish mathematical
acceptance or correct semantic transport. No production tool was called,
no permission workaround was attempted, and no live chapter was edited.
