# Critical division with an independent near-critical envelope input

Date: 5 October 2026. Baseline: `ef8379320f5af80cb56fe836f2cdc6c641ae656f`.
Status: a dependency calculation outside active TeX, using the book's
existing strict division and imported basic psh properties. No new
independent production-verifier receipt, general Siu repair, or solved
Chapter 72 atom is claimed. The calculation does not independently
reprove numerical-class closedness; the separate
[abstract diagonal-lemma diagnostic](bj22_abstract_diagonal_lemma_diagnostic_20261005.md)
records why that input must not be confused with a fresh proof of every
abstract closure statement in BJ22.

## The exact extra hypothesis

Work in the usual trivially valued, algebraically closed setting. Let
`X` be normal, integral and projective, let `alpha` be a real numerical
class, let `D` be an effective rational Cartier divisor, and write
`ell_D = log|s_D|`. Suppose

\[
 \psi\in\operatorname{PSH}_{\rm hom}(X,\alpha),\qquad
 \psi\leq\ell_D.
\]

Fix an ample class `A`. The required independently supplied envelope
input is a sequence of classes

\[
 \beta_m=\alpha-[D]+\varepsilon_m A,\qquad
 \varepsilon_m>0,\quad\varepsilon_m\longrightarrow0,
\]

each satisfying the envelope property on this same `X`. The argument
uses the closedness of the set of psh numerical classes of a fixed
function, BJ22 (PSH2a)/Theorem 4.5, together with the sum, scaling and
divisorial-determination properties recorded in Chapter 34. These are
identified source inputs, not conclusions established by this note.

This is a near-critical hypothesis. A single larger ample class with an
envelope property does not supply this sequence. Nor does a weak limit
in that larger class automatically lie in the limiting critical class.
The following proof explicitly keeps the classes aligned.

## Strict division first, then increasing closure in a fixed class

If `D=0`, the residual is `psi` and no argument is needed. Assume `D` is
nonzero. For rational `q` with `0<q<1`, we have

\[
 \psi\leq\ell_D=q^{-1}\ell_{qD},\qquad q^{-1}>1.
\]

Apply the separate strict fixed-coefficient theorem
`thm:ch35-homogeneous-siu` to the divisor `qD`. It gives a uniquely
defined residual

\[
 r_q\in\operatorname{PSH}_{\rm hom}(X,\alpha-q[D]),
 \qquad r_q+q\ell_D=\psi
 \quad\text{on all of }X^{\rm an}.
\]

This identity defines the residual by section division and closure,
including at proper support. On divisorial points all values are finite,
so there we may write

\[
 r_q=\psi-q\ell_D,\qquad
 r_{q'}-r_q=-(q'-q)\ell_D\geq0\quad(q'>q).
\]

Divisorial comparison, BJ22 Theorem 4.22, then gives the same increasing
order on the whole analytification. It applies to a psh function and an
usc comparison function, so the two functions need not start in the
same numerical class. Homogeneous normalization gives `r_q<=0`.

For a fixed `m`, openness of the ample cone gives a threshold `q_m<1`
such that

\[
 \beta_m-(\alpha-q[D])
   =\varepsilon_m A-(1-q)[D]\in\operatorname{Amp}(X)
 \qquad(q_m<q<1).
\]

No nefness of `D` is asserted. The small multiple of its fixed numerical
class is absorbed by `epsilon_m A`. Constants are psh in a nef class
(BJ22 (4.3)), and addition adds classes (Theorem 4.7(i)). Consequently
the tail of `(r_q)` is contained in the **fixed** space
`PSH(X,beta_m)`. It is increasing and bounded above by zero.

The independently assumed envelope property for `beta_m` and BJ22
Theorem 5.11(iii) supply a limit `r^(m)` in this fixed psh space. The
topology here is pointwise convergence on divisorial valuations. Hence

\[
 r^{(m)}(v)=\psi(v)-\ell_D(v)
 \qquad(v\in X^{\rm div}).
\]

The limit remains homogeneous. Indeed the scaling action
`(lambda . u)(v)=lambda u(v/lambda)` preserves the fixed psh class
(Theorem 4.7(ii)), and sends divisorial valuations to divisorial
valuations. Each `r_q` is invariant under this action. Its divisorial
limit has the same invariance, which extends to all points by Theorem
4.22. This does not invoke homogeneous compactness Corollary 6.22.

Every `r^(m)` has the same divisorial values. Applying Theorem 4.22
in both directions shows that these psh functions coincide everywhere,
even though their classes differ. Write their common extension as `r`.
The **fixed-function** numerical-class closedness (PSH2a) now gives

\[
 r\in\bigcap_m\operatorname{PSH}_{\rm hom}(X,\beta_m)
 \quad\Longrightarrow\quad
 r\in\operatorname{PSH}_{\rm hom}(X,\alpha-[D]).
\]

Finally `r+ell_D` is `alpha`-psh by the sum rule, because `ell_D` is
`[D]`-psh. Its divisorial values agree with `psi`. Theorem 4.22 gives
the additive identity on all of `X^an`. At a point supported in `D`,
`ell_D=-infinity` and both sides are minus infinity; no subtraction of
two infinite values defines `r`. Uniqueness follows by finite
cancellation on divisorial points and determination. The converse
uses `r<=0`, so `r+ell_D<=ell_D`.

## Established regimes and remaining boundaries

The published BJ addendum (2024), Theorem A, supplies all the `beta_m`
envelopes when `X` is smooth and either the characteristic is zero or
`dim X<=2`. The field is algebraically closed and trivially valued and
the variety is projective, as in that source. Subject to the identified
basic closure inputs, the calculation above spells out the division
consequence in those regimes. It is a reorganization of the fixed-`q`
and envelope-limit route of BJ Green-functions Proposition 17, not a
new priority claim. For a normal projective curve over this field,
smoothness follows from normality and perfection of the field.

This does not supply independently known envelopes for singular normal
surfaces, arbitrary normal varieties, or all smooth varieties in higher
positive characteristic. In particular it cannot be used to prove the
same general envelopes by first assuming them in the `beta_m` classes.
Wu's recent normal-envelope theorem retains the unacquired and printed
source concerns already recorded in the current-literature audit; its
abstract does not discharge this hypothesis here. Corollary 6.22 is
not used, and no general compactness is assumed without an envelope input.

## Reading and admission scope

Fresh readings include the complete strict theorem/proof at Chapter 35
source lines 2550–2667; BJ22 text 2875–3180 (definitions, numerical
closure statement, printed diagonal proof and sum/scaling rules),
3286–3330 (divisorial determination), 3707–3788 (envelopes and
compactness), and 4130–4310 (homogeneous regularization and its proof).
The addendum's standing scope and Theorem A were checked at 55–88.
The Green-functions proof at 610–715 and its actual page 13 were
checked earlier in this same continuation and reused with that date.

Seven additional actual BJ22 pages (physical 61–66 and 70) and three
actual book pages (2250–2252) were viewed. Same-session earlier views
of BJ22 79–80 and 91–92 and addendum 2–3 are separately identified in
the [downstream scope manifest](siu_downstream_scope_manifest_20261005.json).
These targeted checks do not amount to fresh independent verification
of every antecedent or a full reading of these primary papers. The
diagonal lemma's unrestricted extended-real formulation is being
diagnosed separately. No exact-current verifier receipt is manufactured
for either this calculation or the book's imported closure block.

All active TeX inputs, the 4,255-page book PDF, catalogue source/PDF and
42 problem statuses are preserved at this research checkpoint.
