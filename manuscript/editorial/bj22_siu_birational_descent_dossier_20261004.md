# Resolution, horizontal approximation, and the normal Siu endpoint

Date: 4 October 2026. Baseline: `1799399`.
This elaborates the resolution/descent route in the
[repair-route ledger](bj22_siu_repair_routes_dossier_20261004.md).
It is a targeted analysis of published inputs and missing approximation
requirements, outside the active TeX closure. Critical Siu division on
arbitrary normal varieties is still unresolved. No division proof, theorem
counterexample, solved problem or independent production-model receipt is
claimed.

## The exact normal descent task after smooth division

For this route only, let the field be algebraically closed, trivially valued
and of characteristic zero. Let `X` be normal, integral and projective, and
let \(\pi:Y\to X\) be a projective resolution with `Y` smooth. Given
\(\alpha\in N^1(X)\), an effective rational Cartier divisor `D`, and
\[
 \psi\in\operatorname{PSH}_{\mathrm{hom},X}(\alpha),
 \qquad \psi\le\ell_D:=\log|s_D|,
 \qquad \beta:=\alpha-[D],
\]
pullback gives a homogeneous \(\pi^*\alpha\)-psh function on `Y`.
BJGreen24 Proposition 17, in its independently established smooth
characteristic-zero envelope regime, provides the division residual there.
The safe global formulation is a function
\[
 u_Y\in\operatorname{PSH}_{\mathrm{hom},Y}(\pi^*\beta),
 \qquad u_Y+\pi^*\ell_D=\pi^*\psi.
\]
Both summands in this identity take values in
\(\mathbb R\cup\{-\infty\}\); it does not define a difference
\(-\infty-(-\infty)\). The divisorial identity supplied by division
extends to this additive identity by psh determination.

The remaining task is to produce
\(u_X\in\operatorname{PSH}_{\mathrm{hom},X}(\beta)\) whose
divisorial trace pulls back to that of `u_Y`. The birational identification
of divisorial valuations fixes that trace. If the psh extension exists,
determination identifies its pullback with `u_Y` and gives
\(u_X+\ell_D=\psi\) on every analytic point. Determination supplies
uniqueness; it does not supply this existence step.

This route has deliberately narrower field scope than \(\mathrm{(SD)}_k\)
in the book. Resolving this characteristic-zero descent task would not,
by itself, discharge the input for arbitrary fields or in positive
characteristic.

## What almost birational invariance actually descends

BJ22 Theorem 4.32 supplies a fixed ample class \(\omega_X\) and an
ideal-section function \(h=\log|\mathfrak b|\le0\), where `pi` is
realized as the blowup of a generically trivial ideal. Its statement is
\[
 \operatorname{PSH}_Y(\pi^*\gamma)+\pi^*h
 \subseteq\pi^*\operatorname{PSH}_X(\gamma+\omega_X)
 \quad\text{for every }\gamma\in N^1(X).
\]
Apply this to \(\varepsilon^{-1}u_Y\) and
\(\gamma=\varepsilon^{-1}\beta\), and multiply by
\(\varepsilon>0\). The resulting descended function satisfies
\[
 \varphi_\varepsilon\in
 \operatorname{PSH}_X(\beta+\varepsilon\omega_X),
 \qquad
 \pi^*\varphi_\varepsilon
   =u_Y+\varepsilon\pi^*h.
\]
For a divisorial valuation, `h` is finite and nonpositive. Thus
\(\varphi_\varepsilon\) **increases** as
\(\varepsilon\downarrow0\). The order propagates from divisorial
points by BJ22 Theorem 4.22. Reindexing does not turn this into the
decreasing approximation required by Definition 4.1 and Theorem 4.5.

Fixing \(\varepsilon_0>0\), the tail with
\(0<\varepsilon\le\varepsilon_0\) lies in
\(\operatorname{PSH}_X(\beta+\varepsilon_0\omega_X)\).
This allows an increasing-limit argument only when the needed envelope
property of that **base-space** class has an independent justification.
The target `beta` need not be nef, so small buffered classes need not be
ample. Knowing only ample-class envelopes is not automatically enough for
this general division task.

The error is also not uniformly small on the full analytic space. Where
\(\pi^*h=-\infty\), its positive multiples remain \(-\infty\),
even as \(\varepsilon\downarrow0\). A raw global pointwise limit
cannot be silently identified with the psh extension of the limiting
divisorial trace. The earlier two-branch example exhibits precisely this
distinction for section-defined residuals.

The published proof has a typographical class omission in its final
general-case line: it has just constructed
\(\varphi_m\in\operatorname{PSH}(L_m+H)\), with
\(c_1(L_m)\to\gamma\), but prints
\(\varphi\in\operatorname{PSH}(\gamma)\).
The decreasing/class-closure step gives
\(\operatorname{PSH}(\gamma+c_1(H))\), in agreement with the
stated theorem. All class buffers above follow that stated theorem;
the omitted `+H` is not treated as exact descent.

## Why Lemma 5.13 cannot complete this repair

BJ22 Lemma 5.13 assumes classes
\(\beta_m>\beta\), with \(\beta_m\to\beta\), for which the
envelope property already holds on **`X`**. It produces functions
\(\varphi_m\) with
\[
 \pi^*\varphi_m=u_Y+\varepsilon_m\pi^*h,
 \qquad\varepsilon_m\downarrow0.
\]
For every fixed index `m0`, their tail is increasing in
\(\operatorname{PSH}_X(\beta_{m_0})\). The proof explicitly invokes
Theorem 5.11 to obtain a psh limit of the divisorial trace. This is the
step that uses envelopes. Independent envelopes on the smooth variety
`Y` do not satisfy the displayed hypothesis on `X`.

Consequently, citing exact birational descent in Lemma 5.13 while trying
to prove the base-space envelope theorem through critical Siu division
is circular on these inputs. This diagnosis does not assert that exact
descent on normal varieties is false.

## The section observation and its missing approximation input

Under \(\pi_*\mathcal O_Y=\mathcal O_X\), the projection formula gives
\[
 H^0(Y,m\pi^*M)=H^0(X,mM)
\]
for a line bundle `M` on `X`; rational line bundles are handled by
sufficiently divisible `m`. Hence a generically finite Fubini--Study
function made from sections of the **exact pullback** \(\pi^*M\)
is the pullback of a Fubini--Study function for `M`, with the same weights.
This is an elementary section observation, not a new general descent
theorem.

It isolates a useful sufficient approximation input: a decreasing
Fubini--Study net for `u_Y` consisting of exact pullbacks of rational line
bundles \(M_i\) on `X`, with \(c_1(M_i)\to\beta\).
The descended section functions then decrease, since the analytic map is
surjective. Their limit is generically finite, is constant on every fiber
by construction, and satisfies the base-space psh definition. This input
would give the required extension without an increasing-limit step.
It has **not** been established for the residuals at issue.

BJ22 Theorem 4.15 does not supply it:

- Part (i) provides arbitrary rational line bundles on `Y` approaching
  \(\pi^*\beta\), with an ample class difference on `Y`. It does not
  require these line bundles to be pullbacks from `X`.
- Part (ii), when the class is nef, makes the approximating line bundles
  ample on `Y`; it still does not make them horizontal.
- Part (iii) gives fixed-class Fubini--Study regularization when the class
  itself is **ample**. The pullback of an ample line bundle under a
  morphism contracting a curve is not ample: its intersection with that
  curve is zero.

The last point has an immediate numerical boundary check. If `C` is a
contracted curve and `A_Y` is ample, then
\[
 (\pi^*M)\cdot C=0,\qquad
 (\pi^*M+\varepsilon A_Y)\cdot C
       =\varepsilon A_Y\cdot C>0.
\]
Thus an arbitrarily small ample class error can prevent an approximating
class from being a pullback at every positive stage. Closeness in
\(N^1(Y)\) is not the horizontal approximation requirement. The
semiample or big-and-nef nature of a pullback does not change the ample
hypothesis printed in part (iii).

Nor is bare fiber constancy a substitute for this approximation input.
For a proper quotient map, a fiber-constant usc function descends as an
usc function: its closed upper-level sets are compact, and their images
are closed upper-level sets downstairs. This topological observation
does not prove psh membership in Definition 4.1. Constancy on algebraic
closed-point fibers alone also does not establish constancy on every
analytic fiber over a valued completed residue field.

## Source scope and the next admissible test

The published BJ22 extracted text was freshly read at lines
1680--1748, 2890--3015, 3048--3138, 3185--3275,
3360--3445 and 3700--3810. Eight selected actual pages
36, 65--66, 68, 72--73 and 80--81 were viewed in four contact sheets.
These display the section pushdown proof, morphism/decreasing-closure
properties, exact ample-class regularization hypothesis, almost birational
invariance proof, and the complete envelope-dependent descent argument.
BJGreen24 Proposition 17's complete proof was reread at lines 590--716;
the earlier same-byte actual page 13 view is reused explicitly. The 2024
addendum's independent smooth all-class envelope proof retains its prior
audit. This is not a fresh audit of all primary-paper antecedents.

A useful next test must therefore construct horizontal decreasing
approximants for these residuals, or establish psh descent by a different
method independent of the base-space envelopes. Any proposed construction
must retain the real target class, handle poles through additive identities
on every analytic point, and explain how its class errors descend. The
book's conditional normal assembly and all 42 active atom statuses remain
unchanged until those inputs have been supplied and verified.

## Bounded public-author follow-up

At 22:50--22:51 UTC, two relevant arXiv author queries returned ten
Piquerez entries and one Lyuhui Wu entry. The latter is the already
checked [2609.27610](https://arxiv.org/abs/2609.27610), submitted
23 September 2026. Neither APW26a nor APW26b was returned by these
bounded queries. This does not establish that those manuscripts are
unavailable elsewhere or absent from arXiv under different metadata.
Their primary proofs remain unacquired.

An initial query for **Yueqiao** Wu returned five affine-cone and related
entries. That is a different author from **Lyuhui** Wu, explicitly named
in 2609.27610 and in its APW bibliography. The initial response is
preserved, but excluded from the APW search evidence; the corrected
Lyuhui query and its response have a separate receipt.

The Piquerez result list also identifies two related background candidates:
[2405.05718](https://arxiv.org/abs/2405.05718), *Homological smoothness
and Deligne resolution for tropical fans*, and
[2405.05014](https://arxiv.org/abs/2405.05014), *Tropical
Feichtner--Yuzvinsky and positivity criterion for fans*. Their returned
abstracts concern tropical duality, fan cohomology and positivity. No
primary proofs or current version histories were read in this lookup,
and neither is substituted for the missing tropical Monge--Ampere input.
They are possible later background directions, with no manuscript import
at this checkpoint. Search headings, abstracts and submission dates are
metadata, not proof verification.
