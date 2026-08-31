# Pedagogy and consistency findings for the isolated Ch29/Ch31 replacements

31 August 2026. Author-side reading pass, separate from the independent mathematical audit. No live chapter, frozen packet, assembled replacement, or gate file was changed. The edits and examples below are proposals only; they are not independently accepted mathematical additions and must follow the existing review and production gates if adopted.

## Scope and exact source bytes

Read the two replacement fragments completely, in their actual proof-dependency order, together with the relevant full-Ch31 transition to examples and the Ch23 paragraphs that refer to the transported proof labels. This is not a full reread of Chapters 23, 29, and 31 or a replacement for their mathematical audit.

Assembly base directory:

`/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260831/p081_ch29_ch31_weighted_full_scope_isolated_repair_20260831/`

| Source relative to that directory | SHA256 |
|---|---|
| ch29_curve_replacement.tex | 63d8d6d5c2136579bc9a4990dda7a3bbf1975c2f07dd7ca39310bd10f5dc6a53 |
| ch31_curve_replacement.tex | 3d49d8265f23e1d07a0af48b1338bf152ace015f24304f2bf206abfc8e755b51 |
| patched/ch29_continuity.tex | 2aaf15684366f0dbcc37c41967c55a4b981135262a1f915fc6434d7c83457304 |
| patched/ch31_bfj_examples.tex | 9a9776e369759250cc28bff06adf1ec2cedf2d653222914a6be9d958600e09e2 |
| combined.patch | 222498b15baf85e1d52ca50f61d4aa9dc37716ca3f593b2f6433b096e02a496a |
| MANIFEST.json | 0e0f870b5f1aa6208b72ae9512915923a05c8b74b8b506b44d2861069b44afb3 |

Other inspected sources:

- `/private/tmp/nappt_p071_20260827/manuscript/parts/part3/ch23_bfj_envelopes.tex`: SHA256 f311c1dc6f375f98d09e5a076997ebe8c7e5ce836f3efbb686b48afabd87a228.
- `/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260831/p081_weighted_curve_green_reference_audit_20260831/CH29_CH31_REPAIR.md`: SHA256 5a57ffab048f90191f16f72148129a6021d733fba6ddc320c8d81feb1c72f22a. Its section C already proposes the nonsplit blowup diagnostic expanded below.

## Main recommendation

Retain the detailed chord construction, the tent-test proof of continuous harmonic uniqueness, and the finite-maximum approximation arguments: these already give the elementary explanations a graduate reader needs. The most useful additions are a nonsplit normalization example and a short proof roadmap, together with three concrete consistency fixes. There is no pedagogical reason to enlarge the theorem scopes or suppress the existing gates.

## 1. Add the missing nonsplit degree/weight example

Location: after the degree-normalization paragraph in the proof of `lem:ch31-curve-ma-affine` (fragment lines 140-155), or immediately after that proof.

The abstract formulas give the correct distinctions, but the assembled text does not illustrate them. Moreover, the next numerical examples explicitly assume split charts and c_e=1 (full proposed Ch31 lines 656-661). A reader can therefore finish the examples without seeing why the nonsplit factors are necessary.

Proposed paragraph, subject to mathematical review:

Let R be a complete discrete valuation ring with residue field k, normalized by -log|pi|=1. Choose a closed point p of P1_k with finite separable residue field k'/k of degree r>1, and blow up P1_R at p. The generic fibre remains P1_K, hence is geometrically connected. The special fibre consists of the strict transform D, isomorphic to P1_k, and the exceptional component E, isomorphic to P1_k'. They meet at one node with residue field k'. The skeleton is an interval of length one, with edge weight c_e=r.

Consider the vertical line bundle O(E), whose generic fibre is trivial. Its component restrictions have the following degrees:

| Component | Restriction | Degree over its constant field | Degree over k |
|---|---|---:|---:|
| D, with constant field k | O_D(p) | r | r |
| E, with constant field k' | O_{P1_k'}(-1) | -1 | -r |

The corresponding model potential has endpoint values F(v_D)=0 and F(v_E)=1. Its outgoing slopes are +1 at v_D and -1 at v_E, so the weighted slope formula gives

\[
             \Delta_\Gamma F=r\delta_{v_D}-r\delta_{v_E}.
\]

This matches the two degrees over k. In particular, the two endpoints can have different constant fields, yet both slope terms use the same node residue degree r. The unit Diracs do not themselves carry an additional hidden degree factor. The total curvature mass is zero, matching the trivial generic line bundle.

End the paragraph by saying explicitly: this is a signed-curvature normalization check; O(E) is not nef, and no semipositive degree-zero conclusion is being made. It also explains why geometric connectedness of the generic curve does not force c_e=1.

A useful optional closing sentence is that splitting k'/k produces r weight-one edges upstairs, whose ordinary pushforward reproduces the original weight r. This is an illustration of the scalar-normalization formula, not a replacement for its proof.

## 2. Put the rational-model versus all-PSH distinction before the theorem

Location: just before `thm:ch29-real-class-curve-model-envelope`, and keep the existing final scope sentence at fragment lines 42-45.

The distinction is already present, but currently the reader encounters it after both conclusions. In a chapter where P_theta may elsewhere denote an all-PSH envelope, that is too late. The qualifier real can also be misread as enlarging the competitor space.

Proposed introductory text:

> In the following statement, real describes the coefficients of the closed model form theta; rational describes the model functions allowed as competitors. The symbol P_theta^{D_Q} always means exactly the displayed rational-model supremum. It is not being identified with an envelope over the real span of model functions or over all singular psh functions.

Keep the superscript D_Q in all displayed formulas and in the transition from this theorem to the metric-envelope assertion. Do not shorten it to the ambient chapter's P_theta unless a local notation declaration repeats the competitor class.

A small further clarification after the degree-zero assertion would help: equality to zero in Z^{1,1} is equality of the relevant numerical model class, not an assertion about the pointwise vanishing of an arbitrarily chosen differential-form representative. The mathematical auditor should confirm this wording against the book's precise definition of Z^{1,1}.

## 3. Make the real proof-dependency direction visible

Location: before the real-class theorem, or at the start of the equation proof around Ch29 fragment lines 481-485.

A reader following page order meets the Ch29 equation theorem before its elementary graph lemma in Ch31; the Ch31 affine lemma then cites Ch29's measure dictionary before the graph lemma is printed. The proof direction is legitimate as described by the assembly, but the current page order makes it look more circular than it is.

Proposed roadmap:

> The model-envelope argument and the equation argument have different inputs. The former uses the explicit rational chord construction and finite normal descent. For the latter, one may first read the elementary weighted Green lemma in Chapter 31; its proof uses only the weighted outgoing-slope definition, not the analytic assertions preceding it. Combining that lemma with the original-field point-reference metric gives the continuous current solution. Rational model approximation is a later, separate step. The model-reference proposition in Chapter 31 is a specialization of the completed equation theorem, not an input to it.

Also explicitly distinguish the two approximation procedures where Step 2 ends:

- Real atomic measures give real piecewise affine potentials and a continuous positive-curvature limit.
- Steps 3-4 construct rational formal approximants by comparison and descent; the atomic potentials are not asserted to be those approximants.

This avoids a reader unconsciously restoring the discarded rational-mass-to-rational-slope inference.

## 4. Correct the subdivision-length sentence

Location: `rem:ch31-lengths`, fragment lines 74-75.

Current wording says subdivision leaves the analytic edge length unchanged on the subdivided pieces. Literally, an individual new piece has a shorter length, so the sentence can be read incorrectly.

Replace it by:

> A subdivision preserves the analytic length coordinate. The lengths of the new pieces sum to the original edge length, and every new piece inherits the original conductance.

This is a wording correction, not a proposed new mathematical claim. Keep resistance length ell_e/c_e explicitly separate from analytic modulus length.

For additional clarity, after the first conductance formula explain that c_e is the edge weight in the differential energy, whereas c_e/ell_e is the coefficient of (a_v-a_w)^2 in the finite vertex matrix. A one-line calculation of the slope (a_w-a_v)/ell_e makes the reciprocal resistance length immediately intelligible.

## 5. Remove a genuine notation collision and introduce the local weights

Locations: Ch29 fragment line 558 and the scalar-weight equation at line 678; Step 2 near lines 529-544.

Step 3 defines F as the completed algebraic closure, but F later denotes a graph function in p_*Delta_{c'}(F o p)=Delta_c F. Reserve a distinct symbol, for example Omega, for the completed field throughout Steps 3-5, leaving F for graph functions. Make the corresponding substitutions in L_F, u_F, theta_F, and the field-extension prose. The envelope proof's C_K notation can remain local to its separate proof, or be harmonized in a future unfrozen revision.

The test-current estimate uses h_j and h without first naming them. Add:

> On a fixed local frame e, write h_j=-log||e||_q+U_j o tau and h=-log||e||_q+U o tau for the local weights.

Then the displayed norm estimate has a completely explicit subject.

Two smaller fixes can be bundled with this:

- Replace the node parameter a in xy=a by alpha, and the integral thickness in xy=pi^a by n, so the two meanings are not adjacent.
- At the start of `prop:graph-ma-solution`, write Fix q in Gamma. The preceding graph lemma fixes q abstractly, but the specialization should identify its own normalization point.

## 6. Retarget argument-specific downstream references

Location: current live Ch23 lines 2864-2873 and 2888-2893, inspected read-only.

These paragraphs point to the proof of `thm:curves-arbitrary-field-continuity` for the detailed retraction and chord argument. In the new assembly, the detailed chord argument is instead in the proof of `thm:ch29-real-class-curve-model-envelope`; the metric theorem delegates its envelope clause to it.

For the chord-proof reference, use the new real-class theorem label. For the retraction reference, cite the precise argument/source used there, including GJKM Proposition 3.8, rather than promising a direct branch-slope proof inside the metric theorem. Do not globally replace every reference to the old theorem: its actual metric-envelope and equation conclusions retain that label.

The broader fixed-model-envelope assertion in the surrounding Ch23 paragraph still needs the mathematical assembly audit's scope decision. This pedagogy pass does not endorse that assertion merely because the labels resolve.

## 7. Explain the two meanings of smoothness/lisse at the first use

Location: Ch29 Curvature conventions and the point-reference proof near line 399.

A graduate reader trained in ordinary differential geometry can reasonably be puzzled that a Dirac mass is called a lisse 1-form. Add a short terminology sentence using Thuillier's Definition 3.2.1:

> Thuillier-lisse is not the same as ordinary CLD-smooth. In Thuillier's test complex, lisse 1-forms are locally finite real combinations of Dirac masses at type-2 and type-3 points, and real piecewise affine skeletal pullbacks are lisse functions.

In the point-reference proof, mention that T+log|f_e| is first a current; current regularity identifies it with a lisse function after the divisor singularities cancel. No continuity of either summand is presumed separately.

The sentence Each U_j is piecewise affine can also be expanded by one clause: mu_j is finitely atomic, so U_j is a finite linear combination of the kernel functions g_q(.,y). This is enough; no additional approximation theorem is needed there.

## 8. Optional graph-only illustration of rational masses versus slopes

This is useful but less important than the nonsplit example. If included, label it as a finite graph calculation, without asserting realization over a particular field.

Take two vertices q,y joined by edges of lengths 1 and sqrt(2), both with weight one. Orient both edges from q to y and solve Delta u=delta_y-delta_q with u(q)=0. Continuity requires a common endpoint value A=u(y), while the mass at q gives

\[
 A+\frac{A}{\sqrt2}=-1.
\]

Thus A=sqrt(2)-2, and the two slopes are sqrt(2)-2 and 1-sqrt(2), both irrational. The atomic masses are nevertheless integers. This makes the invalid arithmetic inference fail in the smallest graph with a cycle. It is not a failure of the continuous solution theorem, and it is not needed for its proof.

## Adoption boundary

The report proposes no source substitution, theorem weakening, candidate acceptance, production submission, or gate removal. If the parent adopts any proposal, create new revision bytes, retain this source snapshot, and route the changed mathematics/examples through the existing independent and production workflow. In particular, neither the nonsplit example nor the optional two-edge example should be described as independently checked on the strength of this pedagogical calculation alone.
