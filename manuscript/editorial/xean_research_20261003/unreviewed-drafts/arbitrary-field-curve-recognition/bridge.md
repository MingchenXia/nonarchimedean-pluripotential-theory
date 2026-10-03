---
title: Intrinsic zero-Hessian recognition on arbitrary-field analytic curves
author: Unverified research draft; author self-audit only
date: 3 October 2026
geometry: margin=1in
fontsize: 10pt
---

# Result, conventions, and proof map

This submission claims a curve-scope theorem and a ground-field probe consequence.
It is partial progress on P06.2, not a solution of the original arbitrary-dimensional
atom. No prior draft, native note, review disposition, production run, or hash is a
mathematical premise. The arguments needed from the supplied drafts are reconstructed
below, and the primary source statements and proof bodies are reproduced in this
document. Standard analytic foundations are explicitly stated and cited. The claims
remain unverified mathematical drafts; typesetting is not verification.

Write $D=d'd''$. All test forms and all current equations are **ordinary CLD**
forms and currents on ordinary topological opens. For a pure-dimensional analytic
space $Z$, $[u]=u\delta_Z$ uses canonical integration with the actual generic
Artinian lengths, including nilpotents. On a curve the equation means
\[
             \int_Z u(D\psi)_{\mathrm{Rad}}=0
             \quad\text{for every }\psi\in A_c^{0,0}(Z).
\]
Only the smooth top form has been identified with a signed Radon measure;
$D[u]$ is not assumed to be a measure. All functions under recognition are finite,
continuous, and real valued. Real PL means the real extension of the integral
G-local PL class, not ordinary CLD smoothness or rational slopes.

**Theorem R (intrinsic arbitrary-field curve recognition).** Let $K$ be any
complete nontrivially valued field. Let $X$ be any good, separated, strict,
boundaryless $K$-analytic space pure of dimension one, and let $U\subseteq X$
be any ordinary open. If $h:U\to\mathbb R$ is continuous and $D[h]=0$, then
$h$ is harmonic in GR Definition 3.13 and classically pluriharmonic in GR
Definition 7.1. In particular, for **every** complete analytic extension $L/K$,
every $L$-analytic curve $Y$ (separated and pure of dimension one), and every
analytic map $f:Y\to U_L$, the two functions
$\pm h\circ\pi_{L/K}\circ f$ are GR-subharmonic on $Y$.
On every smooth strict connected such probe over a nontrivially valued field,
they are Thuillier-subharmonic and their common finite function is harmonic.
Moreover, $h$ is G-locally real PL and is GJR harmonic: every residual class
$L_h(x)\in\operatorname{Pic}(\operatorname{red}(U,x))_{\mathbb R}$ is numerically
trivial. Singularities, nonreduced structures, imperfect fields, inseparable
residue fields, and nonproper nonalgebraic curves are permitted. No scalar
stability assumption is imposed.

**Theorem P (ground-field probes).** Let $K$ have the same field hypotheses,
and let $X$ be good, separated, strict, boundaryless, and pure of any dimension
$n\geq1$. For every ordinary open $U\subseteq X$, continuous finite
$h:U\to\mathbb R$ with $D[h]=0$, and analytic $K$-map $f:Y\to U$ from a
separated smooth strict $K$-analytic curve, $h\circ f$ is Thuillier harmonic,
GR-harmonic, classically pluriharmonic on $Y$, G-locally real PL, and GJR
harmonic. Here smooth includes absence of absolute analytic boundary.
This statement concerns maps over the ground field; it does not identify
$h$ as classically pluriharmonic on a higher-dimensional $U$.

The proof of R has three separate operations. Part T proves current transport
to the completion of an algebraic extension on actual pure curves. Part C
recognizes on algebraically closed fields by actual local algebraic models and
the curve comparison, with component lengths and punctures handled explicitly.
Part B proves that the completion of an algebraic closure is an admissible field
and checks descent of the recognized functions with full quantifiers. Part Q
reconstructs closed-curve restriction and the actual local-image theorem, then
deduces P. The scalar proof in T is dimension one; Q does not create a current
equation after a transcendental extension of a higher-dimensional ambient space.

The controlling original question is Problem `prob:frontier-pluriharmonic` in
the supplied `ch72_major_open_problems.tex`: complete nontrivially valued $K$,
good separated strict boundaryless $X$, and recognition of every continuous
zero ordinary Hessian current, in arbitrary dimension. The accompanying
`appM_ch18_frontiers.tex` distinguishes recognition, scalar-current ascent,
and two-sign positivity regularization. These texts specify scope, not proof
inputs. R removes the ground-field restriction from the supplied algebraically
closed curve recognition. P adds ground-field smooth strict probes over arbitrary
$K$. The full atom and P05.2 remain open in this submission; `candidate=false`.

# Part T. Completed-algebraic transport: statement

**Transport lemma.** For a good separated strict boundaryless pure
$K$-analytic curve $Z$, an algebraic extension $M/K$ with its extending
absolute value, and $L=\widehat M$, the actual scalar projection satisfies
\[
                  D[u]=0\quad\Longleftrightarrow\quad D[u\circ\pi]=0.
\]
It holds on every ordinary open, with the original lengths. A subsidiary
lemma, not requiring dimension one, is that every compact ordinary smooth
scalar test on $Z_L$ is exactly the pullback of a compact smooth scalar
test on $Z_E$ for some finite embedded $K\subseteq E\subseteq M$.
The following T2--T13 prove these assertions. Equation numbers inside T
are local to this proof. All source excerpts referenced there are supplied
in Appendix S; the historical misselected Section 15 blocks are excluded.

