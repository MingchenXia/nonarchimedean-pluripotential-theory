# Regular polynomial automorphisms: hybrid source review

Source-only checkpoint, 6 October 2026. Baseline work commit:
`33529c4cdbbe51c432927679960a9e9eb3eaa34d`; main:
`00957114db21b627e97369563032ceda9cea09c7`.

The complete [Irokawa preprint, 2610.06821v1](https://arxiv.org/abs/2610.06821v1),
submitted 5 October 2026 at 17:56:42 UTC, was read in all **23 physical
pages**, including references. The complete earlier
[Hénon preprint, 2212.10851v2](https://arxiv.org/abs/2212.10851v2),
revised 18 August 2023 at 08:17:58 UTC, was read in all **22 physical
pages**; its abstract's page-count comment does not describe the actual
downloaded PDF. Complete selected text and corresponding original page
images were read for every entry below: **118 source/page pairs in 61
sheets**, comprising 85 pages from newly acquired PDFs and 33 freshly
reread pages from three previously cached PDFs. Acquisition, text
extraction, preparation and actual reading have separate frozen records.

This audit does not certify the new main convergence theorem or a full
repair of its proof. A counterexample to an intermediate covering claim
is given below. The older v2's total-Lyapunov formula has a counterexample
to the formula itself; this does not refute either paper's main measure
convergence statement.

## Editions and reading scope

| Primary file | Physical pages actually read and displayed | Edition boundary |
| --- | --- | --- |
| Irokawa 2610.06821v1 | 1–23, complete | New v1; PDF internal date 30 September 2026, submission 5 October |
| Irokawa 2212.10851v2 | 1–22, complete | August 2023 preprint, not the 2025 published proof |
| Kawaguchi, published Algebra & Number Theory PDF | 1–3, 8–16, 19–20 | 31 physical pages overall; publisher cover counted |
| Lee 1203.1224v2 | 1–3, 7–11, 14–22 | March 2012 v2, not a fresh reading of the 2013 publication |
| Guedj–Sibony, author-hosted Arkiv2002.pdf | 1, 10–13 | 30-page author manuscript, not the 37-page published layout |
| Favre 1611.08490v2, reused cached PDF | 13–14, 19–21, 25–27 | December 2017 v2; existing chapter audit is separate historical evidence |
| Boucksom–Eriksson, published BE21 PDF, reused | 60–64, 72–76 | Printed pagination is physical pagination minus one |
| Chambert-Loir–Ducros 1204.6277v2, reused | 133–136, 197–198, 207–213, 223–224 | 608-page French 2025 revision; old 2012 section numbers do not transfer |
| Chambert–Loir math/0304023v3 | 4–6, 10 | November 2004 preprint, not the published 2006 layout |

The first CLD selection concerns volume forms, not Bedford–Taylor theory.
It was actually read; eleven additional edition-aware pages close the
continuous-potential product interface. No full 608-page audit is claimed.
BE21 extraction reports annotation-dictionary syntax warnings; extraction
and original-page rendering succeed. No source PDF was altered.

The [publisher's Hénon record](https://link.springer.com/article/10.1007/s00209-025-03726-6)
confirms *Mathematische Zeitschrift* **310, article 41 (2025)**,
published 3 May 2025, DOI `10.1007/s00209-025-03726-6`. Its ordinary
public PDF endpoint redirects to subscription-preview HTML. The published
full text was **not obtained or read**. Consequently no claim is made
that the 2023 diagnostics persist in the published version, or that a
published correction has or has not settled them. Metadata and an
abstract cannot decide those questions.

## Dynamical and metric interfaces

The intended nonlinear category is a fixed-degree meromorphic family of
regular polynomial automorphisms of affine N-space, N at least two,
with both degrees at least two. Regularity means disjoint indeterminacy
loci of the forward and inverse projective extensions. Writing
`l_+ = dim I(f)+1` and `l_- = dim I(f^-1)+1`, the classical geometric
inputs give `l_++l_-=N` and `d_+^{l_-}=d_-^{l_+}`. Thus the balanced
iterates `f^{l_-}` and `f^{-l_+}` have the same degree. Meromorphic
coefficients with finite pole orders define the C((t)) map; arbitrary
essential singularities do not.

Continuous local escape potentials satisfy
`G_+ o f = d_+ G_+` and `G_- o f^-1 = d_- G_-`. Positive curvature
therefore has the same multiplication factors. For the prospective
mixed invariant measure, pullback by f contributes
`d_+^{l_-}/d_-^{l_+}=1`. This formal calculation does not create the
measure or prove its local rank properties.

Guedj–Sibony Lemma 2.12, author PDF page 13, proves the complex identity
for nonnegative continuous psh u,v with `(ddc u)^r=0` on `{u>0}` and
`(ddc v)^s=0` on `{v>0}`:

    (ddc max(u,v))^(r+s) = (ddc u)^r wedge (ddc v)^s.

The full printed proof was read. CLD25 Chapter 8 supplies the selected
continuous locally approachable Bedford–Taylor locality, symmetry and
local uniform convergence inputs: Lemma 8.5.5, Proposition 8.6.8,
Propositions 8.7.2 and 8.7.4, and Remark 8.8.9. These explain a formal
route after the non-Archimedean escape-rank statements have been proved
in that precise class. They do not themselves prove those statements
for every dynamical Green function. The 2023 v2 Remark 2.6 explicitly
leaves the non-Archimedean maximum/product identification open; the new
2026 v1 Theorem 4.4 claims to establish it. Its rank proof remains a
verification gate here, rather than a certified solution of a canonical
book problem or a declaration of the question's current published status.

On projective space a degree-D tuple determines a **relative metric
weight**, not an unnormalized affine escape potential. With a fixed
ordinary-norm reference rho and the source's max convention, the weight
is `D^-1 log max |sections| - rho`. Hybrid extension on a nonzero fibre
uses the positive factor `lambda(t)=log r/log|t|`. Tensor degree,
reference subtraction, curvature of the reference, semipositivity and
fibre multiplicities must all remain visible. BE21 only supplies positive
products for the indicated psh/nef classes; an arbitrary model metric
does not gain positivity by being a constant uniform-approximating
sequence. Chambert–Loir Definition 2.4, v3 page 5, explicitly retains
special-fibre multiplicities and tensor-degree denominators.

Projective hybrid convergence yields an affine conclusion only after a
support or tightness argument. The affine projection is not proper:
its complex fibres are noncompact affine spaces. A **closed** common
hybrid polydisc can be compact; an open polydisc is not compact merely
because it lies in a projective compactification. A compactly supported
cutoff must be retained when extending an affine test by zero.

## Twenty-nine exact source checks

These entries include literal errors, incomplete proof steps and scope
guards. Their classifications do not amount to an independent model
receipt, a new formal result, or a refutation of every cited theorem.
Grouped auxiliary misprints are subordinate to the same interface.

| ID | Exact edition and physical pages | Finding and retained boundary |
| --- | --- | --- |
| M01 | 2610 v1, 1, 10, 15 | The first two displays use reciprocal pullback factors; Section 4.3 uses the correct multiplying factors. Internal normalization error. |
| M02 | 2610 v1, 7, 9 | Proposition 3.5 omits lambda(t) on nonzero fibres, although page 7 includes it. A logarithm of the parameter norm has finite central value only after the scaling. |
| M03 | 2610 v1, 7–8 | The atomic model measure omits b_E despite the preceding nonreduced fibre decomposition. Reduced-fibre formulas cannot be extended with b_E suppressed. |
| M04 | 2610 v1, 8; BE21, 61–64, 72–75 | Proposition 3.4 omits the positivity hypotheses required by BE21's regularizable psh measure construction. Later globally generated approximants may meet them; an arbitrary model metric need not. |
| M05 | 2610 v1, 7; Favre v2, 14 | Chart ideal generators are called elements of the base ring A_r. A model ideal such as (t,x) needs a coordinate generator. Generator norms are taken on the appropriate formal model domains. |
| M06 | 2610 v1, 1, 10; Kawaguchi published, 3 | Nonlinear degree restrictions are needed for the stated indeterminacy-dimension balance; affine linear automorphisms are not covered by that balance. Scope guard. |
| M07 | 2610 v1, 11 | The homogeneous coordinate tuple is said to have no common zero away from the origin. A map fixing affine zero contradicts this literal assertion. Regularity supplies the needed assertion on S=0. |
| M08 | 2610 v1, 12–14 | V=B union U is confused with the escaping set U; the first-entry norm bound uses the wrong radius, and a rescaled iterate retains the wrong index. Lemma 4.8's recurrence also prints exponent n where d_+ is required. A continuity proof certificate is not obtained from these lines. |
| M09 | 2610 v1, 14; GS author PDF, 11–13 | A nonzero escape-coordinate tuple does not make its first coordinate invertible on the whole compact set. A product of two Hénon maps with one block fixed at zero witnesses this. The extra constant 1 in log max supplies an additional normalized function; dropping it requires a late-escape bound. Local charts and rank remain inputs to verify. |
| M10 | 2610 v1, 16; Kawaguchi published, 8–12 | Nullstellensatz certificate coefficients are asserted to be linear sums of map coefficients. Solving the coefficient system generally needs rational functions/nonzero minors. A uniform-degree meromorphic certificate requires its own argument. |
| M11 | 2610 v1, 18–19; Kawaguchi published, 19–20; Lee v2, 19–20 | Map-coefficient maxima alone do not give the asserted covering constants; the explicit family below disproves that covering. Certificate coefficients and complex monomial counts are missing, and diagonal membership does not replace forward invariance of the product domain for telescoping. |
| M12 | 2610 v1, 20 | The affine hybrid projection is incorrectly called proper. The later closed-polydisc argument is the appropriate compactness interface. |
| M13 | 2610 v1, 21 | Raw degree-D model functions are identified with degree-normalized affine escape approximants, omitting degree division and the reference potential. The good-reduction calculation below disproves the literal identification. |
| M14 | 2610 v1, 22 | The final projective test integral drops its affine cutoff. Use the extension by zero of chi times the affine test, with chi=1 on the common closed support. |
| M15 | Hénon v2, 6; 2610 v1, 13–15, 20 | The historical open maximum/product question and the new claimed answer require separate edition-aware status. Neither the old remark nor the new assertion is a certified current open/solved verdict here. |
| H01 | Hénon v2, 2–3, 19 | Theorem 1.2/equation (16) has the wrong sign in the total-Lyapunov scaling. The a(t)=t calculation below is a counterexample to this printed formula, not the main weak-convergence theorem. Published 2025 status unverified. |
| H02 | Hénon v2, 2, 19–21 | Oseledets concerns derivative products along the orbit, not one-step derivative eigenvalues. The first-exponent proof replaces the cocycle expression without justification. The displayed derivative has +a in place of -a, and the hybrid logarithmic factor is negative. Do not import this proof or first-exponent asymptotic. |
| H03 | Hénon v2, 4, 16–18 | On the backward escape region G_- includes minus the logarithm of the coefficient norm divided by d-1. Inverse iterates have leading coefficient a^(-(d^n-1)/(d-1)); they are not monic for general a. Their nonzero weighted leading term can still give the projective morphism. |
| H04 | Hénon v2, 5, 7–12 | The raw logarithm at a fixed zero is -infinity; log+ is needed. An absolute error bound has a potentially negative logarithm of the inverse coefficient norm on its right side, and the backward lower estimate reverses its coefficient sign. These lines are not a uniformity certificate. |
| H05 | Hénon v2, 6 | T_+ and T_- are defined with -ddc of psh escape potentials. The positive curvature convention requires +ddc. The new 2026 preprint uses the positive convention. |
| H06 | Hénon v2, 6 | The stated normalization of a general map (P(x)-a y,bx) uses c^d rather than c^(d-1)=leading(P), and the printed second coordinate of the conjugation produces b^2 x. The monic b=1 main setting must be separated from this general conjugation claim. |
| H07 | Hénon v2, 13; Favre v2, 14 | Infimum of generator logarithms does not define the ideal norm: generators (1,t) of the unit ideal give a different value from generator 1 alone. The appropriate formal-domain norm uses a maximum. |
| H08 | Hénon v2, 17–18 | The claimed normalized model-function/escape equality omits the Fubini–Study reference potential. The following metric-section calculation partly recovers the required cancellation. Retain the corrected metric interface. |
| H09 | Hénon v2, 2, 14, 18, 21 | Affine properness and open-polydisc compactness are false as stated. Restricting a projective weak limit to the affine part also needs tightness/common support. No first-countability assumption is introduced. |
| D01 | Favre v2, 13–14, 20–21, 26–27 | The selected formulas include unpowered ideals in a degree-matching sum, inf instead of max, missing b_E, and degree/metric mismatch. Correct lambda scaling and fixed-approximant CLN are read in the same edition. Earlier Chapter 66 corrections are preserved. |
| D02 | BE21 published, 61–64, 72–76 | FS closure, nef/psh regularization and positive/signed products have distinct hypotheses. Example 8.11 first passes to reduced special fibre. The monotonic-shift sentence needs a fast subsequence, already supplied in the book. These are interface guards, not a refutation of BE21. |
| D03 | Lee v2, 11, 15, 17–20 | Lemma 6.2 uses <= instead of strict degree drop and reverses composition order; identity maps disprove the literal equivalence. Individual good-reduction forward/backward equalities need a maximum, and raw-log, exponential/additive and product-height steps have the indicated normalization errors. Do not claim a full published proof audit. |
| D04 | CLD25 v2, 197–198, 207–213, 223–224 | The selected BT interfaces keep their precise class. Page 213's displayed softmax needs exp(x_i/epsilon), and the printed positive-rank inequality is reversed. These auxiliary displays are not used as a rank certificate. No verdict is given on the unneeded Corollary 8.6.7 multiplication wording. |
| D05 | GS author PDF, 10–13; CL v3, 4–6, 10 | The complex escape-rank/maximum identity and weighted model measure are read directly. Their ambient hypotheses, source layouts and tensor normalizations remain load-bearing; they do not settle the new non-Archimedean dynamical rank statement. |

## Reproducible local witnesses

For M11 let `f_t(x,y)=(y,t y^2-x)` for real `0<t<1/2`.
It and its inverse `(t x^2-y,x)` are regular degree-two polynomial
automorphisms. Here l_+=l_-=1. The maximum of 1 and the absolute
values of their coefficients is C(t)=1. The source's choices give
delta=epsilon=1. At z=(0,2), `||z||=2`, whereas
`||f_t(z)||=||f_t^-1(z)||=2 < delta ||z||^2=4`.
Also `||z||>epsilon^-1=1`. Thus z belongs to neither asserted V-set;
the asserted covering and diagonal-product membership fail with those
parameters. Kawaguchi's actual constants also control the homogeneous
Nullstellensatz certificates, which can require 1/t in this family.
This calculation neither disproves uniform convergence with correctly
chosen constants nor supplies the missing invariant-domain proof.

For M13 use the good-reduction map `H=(x^2-y,x)` over C((t)). The
combined forward/inverse homogenized degree-2^n sections, together
with S^(2^n), globally generate O(2^n) on the projective model. Their
vertical ideal is the unit ideal, so its raw model function is zero.
At the affine analytic point x=t^-1,y=0, the normalized escape
approximant is positive. It cannot be that raw model function. On this
model the reference local potential `rho_NA=log max(1,||z||)` restores
the identity `relative weight = local escape approximant - rho_NA`.
This is a normalization witness, not a failure of the corresponding
canonical Gauss measure.

For H01 set `H_t=(x^2-t y,x)`. Its Jacobian determinant is t.
The sum of the two complex Lyapunov exponents is therefore
`log|t|=-log|t|^-1`. In the v2's explicitly declared t-adic norm
`log|a|_r=log r`. Its printed leading term
`(log|t|^-1/log r) log|a|_r` instead equals **+log|t|^-1**.
The discrepancy is not little-o of log|t|^-1. The positive scaling
consistent with the determinant is division by **-log r**. This direct
check is confined to the downloaded 2023 v2; the 2025 published formula
has not been inspected.

## Admission and preservation

No active TeX, bibliography, canonical problem status, proof receipt,
native catalogue source/PDF or editor state changes at this checkpoint.
The preceding **4,411-page** book, generated files and exports remain
byte-identical. All 425 active inputs, 108 protected inputs, 78 prior
frozen manifests and 136 prior exports are pinned. Only README and the
research programme change among baseline tracked files; this audit and
its manifest are new. Reference, canonical-inventory and diff checks run;
no unchanged book is rebuilt or claimed freshly reread.

The next admitted explanation can connect balanced escape approximants
to projective hybrid metric continuity, with degree/reference scaling,
positivity, uniformity and closed-support hypotheses displayed. The
non-Archimedean rank and uniformity proof remain explicit source gates.
No first-Lyapunov result, new original theorem or unqualified solution of
the historical maximum/product question is admitted. The general BJ22
Theorem 6.21 Siu/envelope-closure issue remains separate and unresolved.
No original model call or independent verification receipt is claimed.

Main and work are fetched before publication. Publish this immutable
checkpoint normally on work and update the existing draft PR; do not
force-push or alter main. Continue the scoped mathematical integration
and primary-literature review afterwards.
