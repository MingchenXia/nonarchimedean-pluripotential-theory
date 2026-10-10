# BJ22 Lemma 4.6: an extended-real diagonal-closure diagnostic

Date: 5 October 2026. Baseline: `ef8379320f5af80cb56fe836f2cdc6c641ae656f`.
Status: explicit research construction outside active TeX, awaiting
independent admission. This is a diagnostic for the literal **abstract**
Lemma 4.6, not a counterexample to BJ22 Theorem 4.5, its algebraic
Fubini–Study specialization, or the Siu theorem. No priority claim,
new verifier receipt or solved book problem is made.

## The printed assertion being checked

The controlling source is Boucksom–Jonsson, *Global pluripotential theory
over a trivially valued field* (2022), DOI
[10.5802/afst.1705](https://doi.org/10.5802/afst.1705), printed pages
708–709, physical pages 63–64 of the cached published PDF. The statement
and complete printed proof were freshly read in the interval 2970–3070
of the extracted text, and both actual pages were viewed.

Lemma 4.6 assumes a compact space `K`, a set `S`, continuous families
`F_s` of functions `K -> R union {-infinity}` stable under addition of
real constants, and a map `rho:S->T` to a metrizable space. For `t` in
`T`, let `Ftilde_t` consist of usc pointwise limits of decreasing nets
`f_a in F_(s_a)` with `rho(s_a)->t`. The asserted conclusion says that
if `g_i in Ftilde_(t_i)` decrease to an usc `g` and `t_i->t`, then
`g in Ftilde_t`. The printed formulation does not require the stage
functions to be finite valued or their pole sets to be compatible.

Chapter 34 already warns that ordering arbitrary inner nets and adding
constants does not resolve common minus-infinity values. Its basic
closure theorem is explicitly a source import without an exact-current
production receipt. The construction below makes that abstract issue
concrete; it is not an independent proof or refutation of the psh
specialization imported there.

## A compact, metrizable test space and admissible families

Let

\[
 K=\mathbf N_{>0}\cup\{\infty\}
\]

be the one-point compactification of the discrete positive integers.
Every finite integer is isolated, and neighbourhoods of `infinity`
contain all but finitely many integers. This is a compact Hausdorff
metrizable space, homeomorphic to `{0} union {1/n:n>=1}` by sending
`infinity` to zero and `n` to `1/n`.

Take `S=N_(>0)`, `T=R` with its usual metric and `rho(i)=1/i`. For
positive integers `i,j`, define

\[
 f_{i,j}(k)=
 \begin{cases}
 -\infty,&k=i,\\
 -j,&k<i,\\
 0,&k>i\text{ or }k=\infty.
 \end{cases}
 \qquad
 F_i=\{f_{i,j}+c:j\geq1,\ c\in\mathbf R\}.
\]

Use the usual extended-real topology, equivalently the topology under
the homeomorphism `exp:R union {-infinity} -> [0,infinity)`. Each
`f_(i,j)+c` is continuous: every finite point is isolated, and the
function is identically `c` outside the finite set `{1,...,i}`, so it
is continuous at `infinity` as well. Its pole set is **exactly `{i}`**.
The family `F_i` is stable under adding every real constant, since such
a translation only changes `c`. Thus all the printed family hypotheses
are satisfied.

## The first closure contains a decreasing outer sequence

For a fixed `i`, the sequence `(f_(i,j))_(j>=1)` decreases pointwise to

\[
 g_i(k)=
 \begin{cases}
 -\infty,&k\leq i,\\
 0,&k>i\text{ or }k=\infty.
 \end{cases}
\]

It stays in the single family `F_i`, so its parameter is constantly
`rho(i)=1/i`. The limit `g_i` is continuous by the same finite-exception
argument. Hence

\[
 g_i\in\widetilde F_{1/i}.
\]

The outer sequence `(g_i)` decreases pointwise to

\[
 g(k)=
 \begin{cases}
 -\infty,&k\in\mathbf N_{>0},\\
 0,&k=\infty.
 \end{cases}
\]

This function is usc: for every real level at most zero its upper level
set is the closed singleton `{infinity}`, and at a positive level the
set is empty. It is not identically minus infinity. The outer
parameters `t_i=1/i` tend to zero. The printed conclusion would therefore
place `g` in `Ftilde_0`.

## No decreasing stage net can approach parameter zero

In fact `Ftilde_0` is empty. Suppose a decreasing net has terms
`h_a in F_(s_a)`. Choose any index `a_0` and write `i_0=s_(a_0)`.
The value `h_(a_0)(i_0)` is minus infinity. For every `a>=a_0`,
decreasingness forces

\[
 h_a(i_0)\leq h_{a_0}(i_0)=-\infty.
\]

Since a member of `F_(s_a)` has exactly the pole `{s_a}`, this requires
`s_a=i_0` for every `a>=a_0`. Thus the parameter is constantly
`rho(s_a)=1/i_0` on a cofinal tail. It cannot converge to zero in `R`.
The argument covers arbitrary directed nets, all choices of the inner
indices `j` and all real translations `c`; passing from sequences to
nets or choosing larger constants cannot remove the obstruction.

Consequently the explicit data satisfy the printed hypotheses, give
`g_i in Ftilde_(t_i)` with `g_i decreasing to g` and `t_i->0`, but
provide no element of `Ftilde_0`. This contradicts the unrestricted
abstract conclusion. It does not construct line bundles, algebraic
sections or psh functions on a projective variety.

## The failure in the printed diagonal proof

Equation (4.5) infers a strict inequality after adding different positive
constants. At a point where the reference minimum is minus infinity,
the new value is also minus infinity, and

\[
 -\infty+\varepsilon_3=-\infty
   =-\infty+\varepsilon_1.
\]

The strict comparison does not follow. In the next exponential step,
the limiting difference can then be zero rather than negative, so the
sets `{h_j<0}` need not cover the compact space. In the constructed
families, any reference pole freezes the admissible family label on
all later comparable indices. This shows why the problem is more than
an omitted choice of the numerical error tolerance.

## A valid finite-valued restriction

If every stage family instead consists of **finite-valued continuous**
functions, the printed compactness argument at this step is valid.
Given two reference stages and `epsilon_3<min(epsilon_1,epsilon_2)`,
their minimum plus the respective constants is finite at every point.
The decreasing outer limit satisfies the required strict comparison
against this finite reference, even where its own value is minus
infinity. The exponential differences are continuous, decrease to a
strictly negative function pointwise, and their negative open sets
cover `K`. Compactness gives a common inner stage below both references.
The metric-error requirement can be imposed at a later inner index,
and the remaining cofinal bookkeeping in the printed proof applies.

One further convergence detail must be stated explicitly. At a point
where the desired limit `g(x)` is minus infinity, an estimate of the
form `f(x)<g(x)+delta` is impossible, even for finite-valued stages.
Use an arbitrary finite real threshold `R` instead: first choose an
outer index with `g_i(x)<R-1`, then an inner index and a sufficiently
small positive error with `f_(i,j)(x)+epsilon<R`. Every later flattened
index retains this inequality. Since `R` is arbitrary, the flattened
limit at `x` is minus infinity. At a finite value of `g(x)`, the ordinary
`g(x)+delta` estimate applies. Both choices can also impose the metric
error bound by increasing the inner index. This completes the
finite-valued restriction at all points without arithmetic that treats
minus infinity as a finite number.

This restriction does not cover arbitrary generically finite
Fubini–Study functions: base-point-free presentations are finite valued,
while a presentation with a base locus has genuine minus-infinity
points. Likewise a fixed pole set alone is not an established
replacement hypothesis here. Any algebraic repair must explain the
compatibility of actual sections and poles, or use another argument for
the psh closedness theorem; the finite-valued restriction cannot silently
be applied to the larger family.

## Consequences for the ongoing research

The [near-critical envelope calculation](independent_envelope_critical_division_followup_20261005.md)
uses the book's imported **numerical-class closedness for a fixed psh
function**, not the unrestricted abstract statement as a freshly
established lemma. It remains a calculation under those identified
inputs. The construction here neither disproves that psh property nor
provides its missing independent proof. It also does not refute the
independently published envelope theorems in their established regimes.

The next source task is to look for a corrected diagonal argument in the
actual algebraic Fubini–Study setting, without assuming critical Siu
division or the envelope property being proved. The distinction must
remain explicit in any later integration. No active TeX, book or
catalogue PDF, bibliography entry, historical receipt or 42-atom status
is changed by this research draft.
