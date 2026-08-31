# Independent exact-byte audit: mixed SNC wall blowup reduction

Date: 31 August 2026. Reviewer: /root/p081_weighted_repair_fresh.
Candidate author: /root.

## 1. Verdict and independence

PASS, conditional on the exact local premise L and all-vertical premise V.
I found no unresolved substantive gap in the full stated mixed-SNC reduction
and no required candidate correction. The optional represented source-cell
interpretation additionally assumes R and L, Sections 6-7. This verdict is
not production verification, integration permission, or a resolution of P21.3.

I did not author the candidate, contribute its blowup outline, or edit its
proof. Root originated the reduction. The V author supplied a separate
advisory geometric check, which I have not substituted for this review.
I previously independently audited L, R, and earlier reduced-wall results;
those earlier reviews are disclosed provenance, not new acceptance of the
premises here. In particular I do not claim that reading V's complete note
and checking its interface independently verifies its entire proof.

The exact frozen 223-line research note and complete source ledger were read.
The full V note and its ledger were read to check the input scope, and the
precise L/R dependencies were pinned. The new algebra, iteration, ordinary
domains, parameter comparison, compact tests, normalization, example, and
limitations were checked rather than accepted from previous pass labels.

## 2. Frozen bytes and mechanical checks

Candidate directory:

/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260831/p213_mixed_snc_wall_blowup_reduction_20260831

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| RESEARCH_NOTE.md | 22508 | 9463a10f2918a01a214c458052a50c5604293a6e4192f7c5aa1c91234c7e1120 |
| SOURCE_LEDGER.md | 4353 | dbde85d634fd9d9d248f5118202564a134fc4ce5df22b32451aa191bac0f956a |
| freeze.mjs | 4553 | dc246f9ebd766a760bd6eaa233f21e6a468e752e48825b0b5ed3ba191ec70c39 |
| MANIFEST.json | 3617 | 34049f77811973f0e9d074bc7d8d88ae9f5aa4e586b3590d75b388f856f607fb |
| SHA256SUMS | 2135 | 3c9e1f7536e2f57345c665297876c08f05d746292dfa0852eb74e2cb4fc8b036 |

All 9 candidate manifest entries, all 10 checksum entries, and the five
announced pins matched independently. There are 17 unique displayed equation
tags. The three authored candidate files contain no byte below 32 except
tab/LF and no DEL. These facts establish byte identity and basic hygiene,
not mathematical truth or typesetting quality.

The candidate's freeze script was read, not invoked with a write option.
The independent read-only verifier and its initial output are preserved as
verify.mjs and INPUT_CHECKS.json. No frozen file, live chapter, inventory,
production service, or git state was changed.

## 3. Exact conditional interfaces

L is the local finite-projection note with SHA-256
3001c94985c0d3e60f184ffd9f0e9591775ea026a98cd20ee538005edac11b7a.
Its Sections 2-5 provide an actual finite flat projection of degree m for a
bounded formal-unit equation, proper tropical inverse images, a constant
coefficient for the given original-field positive closed current, and
canonical coefficient m[L:K]. Retained exponents may be zero. They do not
require the whole source to be a product or reduced semistable tube.

The substitution before the blowups is m=N_0, coefficient field K_p,
and retained exponents (N_1,...,N_{n-1},N_p). After the blowups it is the
same omitted multiplicity N_0 and the transformed positive selected
multiplicities. K_p/K is unramified of degree d_p in both uses. No unknown
current is base-changed or reinterpreted as a K_p-current.

V is the all-vertical note with SHA-256
d9e57c21c276edb40bc7619562b7f0a782cdc7a7eb05a04dd0b0cf0770dc9ea9.
Its statement covers an integral proper flat regular original-DVR model
with smooth generic fibre, strict SNC special-fibre support and arbitrary
positive multiplicities, a whole connected proper residual curve cut out
by n distinct vertical components, and a positive closed (0,0) current on
the entire ordinary curve tube. It gives the principal-divisor functional,
residue-degree proportionality and the omitted-component factors.

The transformation below meets all those hypotheses. Any unselected
horizontal components left in the larger boundary B are harmless: V
requires SNC special-fibre support, not the absence of all horizontal
divisors on the model.

R is not used for the functional identity. Its statement/proof pins are
5c06cd6f091e5964a16c07b3efddd2104fed938447605f4f9b19ff8dfea01f1a
and 27a344a15fa7d22b2e88c07837aacfca0c978758c5bae5871c5af2d30e47999a.
Only the final interpretation invokes R together with L's additional
generic-Gauss single-source-point argument. Finite flat degree by itself
does not identify arbitrary source-cell coefficients.

## 4. Completed presentation and parameter independence

Candidate Sections 2-3, especially lines 78-97, pass.

The SNC intersection has the expected codimension and is regular. Its
connected components are disjoint integral schemes. The selected vertical
component makes the curve a k-scheme; properness descends from the model,
and perfectness of k makes this regular curve smooth. Geometric
connectedness is neither needed nor inserted.

At a closed point p, there are at most n+1 boundary branches in the
(n+1)-dimensional regular local ring. Thus there can be only one additional
vertical factor, recorded by w and N_p. Dividing pi by precisely the
vertical parameter powers gives a unit: no horizontal factor belongs in
the divisor of pi.

The separable residue extension gives the unramified coefficient DVR R_p.
Its map into the completed local ring lifts the specified residue map and
is injective since pi is nonzero. Successive parameter approximation gives
the power-series surjection; no coefficient field in mixed characteristic
has been assumed. Regularity and dimension survive completion.

The degree-one monomial case really is covered. In the source regular
local ring, pi and X_0 are independent cotangent directions. If N_0=1
and every other exponent is zero, the linear class of the defining
equation is pi minus a nonzero scalar times X_0, not zero. Otherwise the
monomial has degree at least two and its linear class is absent. Quotienting
by this nonzero linear class is regular of dimension n+1. A surjection
onto the completed regular local ring of the same dimension has zero
kernel. This does not extract a root of the deformation unit.

The completed presentation induces the whole special-formal tube via the
completion-to-tube interface inherited from V. The new zero-exponent
entries do not change that construction. Removing horizontal zero loci
and w=0 when N_p=0 is essential to the finite-projection domain.

For a different curve parameter when N_p=0, write

\[
 w'=wV(w)+\sum_i x_iA_i.
\]

All coefficients are bounded and V has norm one. Choose every normal
valuation larger than rho and 0<v(w)<delta<rho. Then the w term strictly
dominates all error terms, so the two w-valuations coincide. Conversely,
if 0<v(w')<delta with the same normal bounds, v(w) cannot be at least
delta; it must lie in the same collar and the equality follows. This
converse excludes both horizontal zero loci from the support of the
comparison test.

The normal slice is genuinely nonempty. For example choose rho>0 with
2rho sum_i N_i<ell, take the included normal valuations near 2rho, and
choose the omitted valuation through the norm equation. The horizontal
normal valuations can also be finite near 2rho. The omitted valuation
is then greater than rho; w is free in the small collar because N_p=0.
The condition on the omitted coordinate is an open target condition
through the same norm equation, not an extra source-sheet selection.
A compact smooth test inside this slice has identical entire support
and identical ordinary pullback in both parameter systems. This
establishes the stated independence at fixed omitted D_0.

## 5. The global center, regular charts, and correct section

Candidate Section 4, lines 101-130, passes.

The center is the complete connected component Z of V intersect H
containing C, not a neighbourhood of a generic point of C. It is a
closed regular codimension-two subscheme, proper over k. No third
boundary component contains it: that would contradict the expected
codimension of a triple SNC intersection. The center contains pi in
its ideal locally and is therefore admissible; the blowup is an
isomorphism on the generic fibre.

The first Rees chart is exactly A[t]/(x-yt), with no extraneous
y-torsion. The cancellation argument in line 108 is valid because
x is a nonzerodivisor modulo y, and y is a nonzerodivisor in A[t].
It proves y-saturation of the ideal, hence injection into localization
at y and identification with A[x/y]. The second chart is analogous.

The regularity check is not restricted to rational closed points.
Localize the polynomial ambient ring above any point of Z. Its quotient
by (x,y) is a localization of (A/(x,y))[t], hence regular, and x,y
are independent regular normal parameters. Thus the nonzero cotangent
class x minus t-bar times y can be eliminated. At t=0 the new boundary
parameters are y,t and the unchanged other boundary parameters; at a
unit t only y and the other boundary parameters remain. This works
after arbitrary residue-field extension and along a positive-dimensional
center. The second chart gives the other half. Consequently the full
reduced total transform of B is SNC, not merely the two named divisors.

The chosen section is always the one meeting the strict transform of V:

\[
 E=(y=0),\qquad \widetilde V=(t=0),\qquad
 E\cap\widetilde V\simeq Z.
\]

The strict transform of H meets the other, disjoint section. Component
equations change by units, so t changes by a unit ratio and t=0 glues
globally. No trivialization of the two normal line bundles is required.

A third component has a third regular equation z and does not contain
Z. Its strict transform retains equation z; one can check this by
y-saturation modulo z in the same chart. Restriction to the chosen
section is exactly its old restriction to Z. Intersecting the remaining
n-2 selected components therefore preserves the entire selected
intersection over Z scheme-theoretically. Its component C' is the whole
proper curve C, not a punctured curve. Since every new selected
intersection point lies on E and on the strict transform of V, there
is no additional component outside this section that can attach to C'.

Substitution x=yt makes the exceptional multiplicity N_0 and leaves
the distinguished strict-transform multiplicity N_0 unchanged. All
other multiplicities remain as written. Integrality, projectivity over
the old model, and torsion-freeness over the DVR give the required new
proper flat integral model.

## 6. Iteration and all closed points

Candidate Section 5 passes, including h=0.

There is exactly one step per selected horizontal slot. The strict
transform of D_0 remains distinguished. Every step removes one
selected horizontal and replaces it by a vertical exceptional component
of multiplicity N_0, while preserving C and the SNC hypothesis. An
eliminated horizontal's strict transform is disjoint from the chosen
curve; all later curves map into that curve, so it cannot reappear.

Near every p, not merely a generic residual point, the chosen charts give

\[
 x_i^+=x_i\ (i\ge1),\qquad w^+=w,\qquad
 x_0=\left(\prod_{i\in I}x_i\right)x_0^+ .
\]

The equations of the other components, including an extra vertical
component at p, are unchanged under the relevant strict transforms.
The substitution keeps the formal unit bounded with unit constant
coefficient. The curve isomorphism preserves p, its residue field and
its coefficient-DVR lift. There is no hidden splitting of p into
ordinary-open K-analytic sheets.

If there are no selected horizontals, the construction is the identity,
Q_p^+=Q_p and the conclusion is precisely the V interface. For h>0
the construction is finite without any prescribed-radius Euclidean
algorithm, root extraction or residue-characteristic restriction.

## 7. Whole ordinary tubes and exact full inverse image

Candidate Section 6 is the essential support step and passes.

The blowups have an actual generic-fibre isomorphism. Compatibility
of reduction and the complete curve map gives X_{C^+} contained in
X_C. Both tubes are ordinary open. Thus T^+ is the restriction of the
same original K-current to the entire final tube. There is no
modification pullback or zero-extension of an arbitrary current.

For a final point, the displayed retained-coordinate identities imply
that all old parameters have norm less than one. The final equation
and norm-one unit give

\[
 N_0v(x_0^+)=
 \ell-\sum_{i\ge1}N_i u_i-N_0\sum_{i\in I}u_i-N_ps>0.
\]

Every selected coordinate is nonzero, since its final multiplicity is
positive. The w puncture is made when necessary. The point therefore
belongs to the old P_p above Q_p^+.

Conversely start with ANY point of old P_p above Q_p^+. All denominators
in x_0/prod_{i in I}x_i are nonzero. The same equation makes the final
quotient have norm less than one. If J is an initial set of processed
horizontal slots, then exactly

\[
 v\left(x_0/\prod_{i\in J}x_i\right)
   =v(x_0^+)+\sum_{i\in I\setminus J}u_i>0 .
\]

Thus every intermediate lift belongs to the chosen strict-V chart and
reduces to its zero section, not just to an unspecified exceptional
point. The retained parameters reduce to those of p. The final point
reduces to the unique p^+ corresponding to p. The quotient maps are
actual analytic functions and the inverse identification comes from
the blowup charts. This proves the full analytic-domain identity
P_p^+=q_p^{-1}(Q_p^+); it does not select a skeleton or a fibre sheet.

Q_p^+ is a nonempty open full-dimensional weighted polyhedron: choose
all positive coordinates sufficiently small. Its compact subsets remain
compact in Q_p. By L the entire inverse images are compact, and the
identity just proved places these same compacts in the ordinary open
final tube. Neither a p-uniform collar nor an assertion that this
smaller target meets an arbitrarily prescribed patch is needed.

## 8. Coefficient transfer, V, and normalization

Candidate Section 7 passes.

Choose a smooth target test of integral one supported compactly in Q_p^+.
Its zero extension to Q_p is smooth. The old pullback is supported in the
ENTIRE inverse image of that compact; this is the same compact as for the
new pullback. The two moments, ordinary differential forms and coordinates
are literally identical there. Compact extension of these TEST forms to
X_C is legitimate, so pairing with T or with its restriction T^+ gives
the same number. This proves b_0(p)=b_0^+(p^+) without a Jacobian factor.

This is a comparison of already constant proper pushforward coefficients.
It does not derive individual source coefficients from a positive
aggregate. Nor does it insert a source cutoff whose derivatives need
to be controlled. The compact target pullback itself is the test.

The final selected components are all vertical with positive multiplicity;
the new special-fibre support is SNC; the model is proper, integral,
regular and flat; and C^+ is a whole proper connected component of their
intersection. Its generic fibre is the original smooth generic fibre.
T^+ is defined on the whole tube. These verify every V hypothesis.
The curve isomorphism identifies function fields, all closed points,
orders of a rational function and degrees over k. Thus V's principal
divisor identity and proportionality transfer to every original p.
Non-geometric connectedness does not change these identifications.

The canonical coefficient remains N_0d_p by L. For a different selected
VERTICAL omitted component D_j, the actual affine relation between
coordinate moments has absolute determinant N_j/N_0. A top (n,n) form
pulls back with the square of this determinant while Lebesgue integration
changes with its absolute value, leaving the factor N_j/N_0. The
weighted target domains are in bijection and the source is the same
punctured tube. A horizontal omitted component has N_j=0 and gives
no invertible coordinate change; it is explicitly excluded.

Under the additional R plus L Sections 6-7 premises, the original
unramified K_p/K and uniformizer hypotheses remain available. The
optional source-cell ratio is then c_0/N_0 as stated. The note does
not strengthen R or replace its single-source-point hypothesis by
finite flatness alone.

## 9. Example, limitations, and disposition

The product example in Section 8 passes. On P^1_R times P^1_R with
horizontal z=0, pi=z t is the correct strict-V chart. The old punctured
target is u,s>0; the final one is 0<u<ell, s>0. Both selected final
components are vertical of multiplicity one, with their whole
intersection isomorphic to P^1_k. A compact strip test compares the
constant on the entire original quadrant. It does not cover u>=ell
or z=0, exactly as the example says.

No required amendment or mathematical obstruction was found. The
candidate's remaining limitations must remain explicit:

- whole modelled curve-tube support is an assumption, not a consequence
  of knowing T on a prescribed ordinary open W;
- the smaller tube can miss a prescribed analytic cell or source patch;
- existence of a suitable original-field model capturing an arbitrary
  wall is not proved;
- a common moment can still have rank-drop cells, and unrelated controlled
  tubes are not shown to have a common scalar;
- there is no identification of T on every ordinary test form, no
  higher-bidegree conclusion, and no full P21.3 retirement.

The source ledger accurately separates familiar algebraic ingredients,
the new written reduction, exact conditional analytic premises and
project gates. No priority or publication claim is justified by this
audit. The separate production gate remains untouched.
