# Independent bounded audit of the Ch20 weighted intersection correction

Date: 31 August 2026. Auditor: `p213_skeletal_hostile`.
This records the completed independent read-only review. It neither edits
the frozen author packet nor certifies future revised1 bytes.

## Verdict and boundary

No mathematical gap was found in the exact replacement proposition and
proof identified below. The correction preserves the general algebraic
identity on a regular curve model and supplies the missing residue degrees
in the reduced semistable graph interpretation. Its degree-weighted graph
formula is not an assertion that the unweighted Chapter 8 operator applies
unchanged over an arbitrary residue field.

This verdict is limited to the replacement and the changed normalization
sentences exposed by the complete chapter diff. It is NOT an acceptance
of the entire copied Ch20 chapter. The unchanged general nonreduced
edge-length statement in the adjacent remark was not independently
reproved. The separate numerical example near live line 3055 still requires
a rational-node/unit-weight assumption. Immediate Ch24/Ch25 consumers also
need the corrections recorded below. Production and a coordinated full-book
build remain gates; no production submission or live edit occurred here.

## Exact six manifest entries

The frozen author directory is
`manuscript/editorial/solver_dossiers_20260831/p081_ch20_weighted_intersection_repair_20260831/`
inside `/private/tmp/nappt_p071_20260827`.
Its `MANIFEST.json` has SHA256
`19f5733e949b668d6f6ec6bb8679d30dc527c6817d283fc65d897608af332cd1`.
All SIX entries were rehashed and size-checked independently, with zero
mismatches:

1. Live input `manuscript/parts/part3/ch20_model_forms.tex`, 171620 bytes:
   `531024045204686aaf0fc12ff0e825bf67367551cd310a26c956740b4d164baa`.
2. Author `curve_laplacian_replacement.tex`, 3632 bytes:
   `2e801b386646260e7a6d96a11bc1303dfa3c7149b32931bbfceeda8d27782c7d`.
3. Author `GATE.md`, 1187 bytes:
   `70341d414c919db4fb0b1c55768e247e841a320d829732dd74545ae881d2a114`.
4. Author `assemble.mjs`, 3098 bytes:
   `cb133f04a0232abc29490003e2e1d4eed26268ccc1c084ed1555c8cb6ef754ca`.
5. Author `patched/ch20_model_forms.tex`, 172270 bytes:
   `42f0c9dd4e957d7038c8bfb3d7c9742c5e5d023d732a219748c6906f447e1b7d`.
6. Author `chapter.patch`, 7677 bytes:
   `366291dacf77d3383265eaefcb0467b78a2573586c78c8e170d01a41d1b8b3fb`.

The complete fragment, complete chapter diff, GATE, manifest, and assembly
script were read. The assembly script was inspected, not executed: it writes
author artifacts. A separate read-only check found all 208 original labels
retained, 209 proposed labels, no missing or duplicate labels, and a passing
`git apply --check` without applying the patch. Hashes and syntax checks are
not substitutes for the mathematical audit.

## Mathematical check of the replacement

Let the regular model's special fiber be sum_i b_i E_i, and write
D=sum_i b_i u_i E_i. Since the special fiber is principal,
sum_j b_j(E_j.E_i)=0. Subtracting u_i times this row-sum relation gives

    (D.E_i) = sum_{j != i} b_j(E_j.E_i)(u_j-u_i).

The total sum with coefficient b_i is zero, either by intersection with
the principal special fiber or by symmetry. For distinct components,
the local intersection multiplicities are nonnegative. The identities
extend real-linearly; there is no rational-divisor assumption. Multiplication
by b_i gives the symmetric coefficients b_i b_j(E_i.E_j). This also explains
why component degree and curvature mass cannot be interchanged on a
nonreduced model.

On the reduced regular semistable model, a transverse closed node z has
local intersection length one over kappa(z). Intersection degree over the
base residue field k is consequently [kappa(z):k]. Hence

    (E_i.E_j) = sum_{z in E_i intersection E_j} [kappa(z):k],  i != j.

The node annulus has modulus length one under the existing normalization
-log|pi|=1, understood on an etale node chart. This does not replace the
node's residue field by k. A model function determined on this model has
constant slope u_j-u_i on the corresponding edge, so its outgoing mass at
i is sum_e c_e partial_e phi_D, with c_e=[kappa(z_e):k]. The preceding
intersection formula identifies this with D.E_i. There are no interior
breakpoints for this determined model function. Thus the displayed measure
identity is complete. Both incidences are included for any loop; a function
determined by its original component values is constant on such a loop.

The proof does not use an invalid inference from positive scalar pushforward
to componentwise positivity. Nor does it claim that every model function is
determined on a reduced semistable model over the original field. Its general
algebraic assertion and its reduced semistable interpretation have separate,
explicit hypotheses. The signs agree with the outgoing-slope convention:
an interior convex corner contributes positive weighted mass.

Thuillier Remark 1.2.4 explicitly identifies the weights of the graph edges
coming from nodal reductions with the residual degrees of the singular
points. Section 2.2.3, at printed page 41, defines exactly that positive
integer weight for the skeleton. These passages were read in the local
primary-source text; the weighted-source interface was previously checked
in the complete weighted-packet audit. Source PDF SHA256:
`fc947ea783e4680741ec23d6b9586f69e17081b9fc3b0a8d507ca9f7a3eb7a1c`;
layout text SHA256:
`9612f1cd9b4478e4bfafd9a5a7490dd670854043b0df65ce67cd84c73be204cf`.

## Adjacent nonreduced remark: what was and was not checked

The new reminder that the curvature coefficient is b_i(D.E_i), with
residue degrees also retained, agrees with Ch24's defining model measure
and the algebraic identity above. This part checks.

The preexisting general claim about edge length 1/(b_i b_j) on an arbitrary
regular nonreduced model is preserved by the author and is expressly outside
this packet's reproving scope. This audit does not turn that unchanged
claim into an independently established theorem. In particular, the checked
reduced semistable calculation must not be cited as a blanket justification
of arbitrary nonreduced metric normalization. Rational node subdivisions
of a fixed semistable edge have an additional determinant-one calculation,
but that is a separate, explicitly proved special situation in the authored
energy packet, not a proof of the general adjacent remark.

## Separate Ch20 numerical consumer

Live Ch20 lines 3055--3065 say that a reduced two-component fiber with one
closed node has intersection matrix [-1,1;1,-1] and D^2=-(u_1-u_2)^2.
This is only the unit-residue-degree case. If the single node has degree r
over k, the correct matrix is r[-1,1;1,-1], and the square is
-r(u_1-u_2)^2. Merely counting one closed node does not force r=1.

The same-scope numerical repair is to declare that this particular example's
node is k-rational, or equivalently has residue weight one. The general
proposition must not be restricted to unit weights. Root is preparing an
isolated revised1; no future or changed bytes are covered by this report.

## Immediate Ch24 consumers

The current Ch24 source SHA256 is
`6fba68089c9ed14700f6944e8409b7b477d91478ec3eee5fcabe6c6b5b152916`.

- Lines 902--903 should say the residue-weighted sum of outgoing slopes.
  The sign conclusion is unchanged because every weight is positive.
- Lines 908--911 use the two-component numerical matrix. Once that example
  explicitly chooses a rational node, its unit-weight square is correct.
- The model uniqueness proof at lines 2515--2539 retains the actual
  intersection coefficients. In its reduced semistable scope b_E=1, so the
  stated summation proves the conclusion. Were that proof extended to a
  nonreduced model, one would multiply the vertex equation by b_E f(x_E)
  to obtain the symmetric weights b_E b_F(E.F). Such an extension is not
  silently inferred from the current statement.

No new gap was found in these bounded algebraic model-measure interfaces.
This is not an audit of the entire Ch24 chapter.

## Ch25: unresolved normalization and determining-model issues

The current Ch25 source SHA256 is
`47c5c5897173168f9d5e21cbb7bdd86338ccf4e72b466f84acea917ea2b25fad`.

1. Lines 2837--2844 call the unweighted `eq:graph-laplacian` a weighted
   Laplacian. The outgoing terms in lines 2885, 2891--2892 and 2898 omit
   c_e. A corrected proof must carry the same edge residue weight on both
   incidences so the branch flux cancels. Cancellation does not excuse
   omitting weights in the original or surviving terms.
2. Lines 2859--2863 assume that every model function is determined on a
   higher semistable model over the original DVR. This is false if
   semistable means reduced. Nonreduced SNC models cannot simply be omitted.
3. The segment calculation from lines 2991ff suppresses valence-two vertices
   and uses unweighted derivative formulas. For its intended numerical
   unit-weight example, that must be stated. For a general weighted chain,
   the correct resistance coordinate depends on all weights; suppression
   does not turn different weights into one.

An explicit test for the second issue is already available on P1_K with a
rational node of modulus length one. Take a nef reference with masses
delta_0+delta_1 and the piecewise affine potential with values
(0,-1/2,0) at (0,1/2,1). Blowing up the node inserts an exceptional component
F of multiplicity two. The real model potential of -F has exactly those
values, and its signed curvature is -delta_0+2 delta_{1/2}-delta_1.
The resulting model metric is nef and its curvature is 2 delta_{1/2}.
For example the reference is obtained by first blowing up a rational
special point of the standard P1 model and twisting the pullback of O(2)
by minus its exceptional component; the reference degrees are (1,1).

At the new midpoint, the original annular coordinate has valuation 1/2.
A divisorial point of a reduced original-K model has multiplicity one, so
its valuation of every nonzero rational function is integral. The midpoint
therefore cannot be a component point of any reduced semistable model over
K. Since the potential's signed curvature has nonzero mass there and a
determining reduced model's curvature is supported at its component points,
no such reduced model can determine this potential. A field extension or
a nonreduced model is substantive, not a harmless unstated refinement.

A possible original-field repair is to use model integration by parts with
tests pulled back from the original skeleton. This identifies the weighted
distributional measure on the skeleton directly with the pushed-forward
positive model measure, without an arbitrary higher semistable determining
model. The real-divisor graph bridge in the separate energy proposal can
then construct the retracted BFJ solution. For bounded functions, decreasing
model regularization and uniform convergence on the fixed skeleton provide
the limiting step. This is a proposed repair route, not a certification of
unwritten Ch25 replacements or a proof supplied by retaining an old label.

## Remaining gates

The forthcoming Ch20 revised1 and any Ch24/Ch25 changes require their own
exact-byte recheck. The present frozen Ch20 parent packet remains unchanged.
No production verification, live patch application, full-book compile,
general envelope conclusion, or open-problem retirement is asserted.
