# Abstract closure with a fixed pole and a fixed limit function

Date: 5 October 2026. Baseline: `14da2a0d6a4370341054935b960c1afd8e6a32f7`.
Status: a strengthened abstract counterexample candidate outside active
TeX, pending independent admission. This concerns the literal hypotheses
of BJ22 Lemma 4.6. It does not refute the algebraic psh Theorem 4.5,
its numerical-class consequence (PSH2a), or the Siu theorem. No priority,
new verifier receipt or solved book problem is claimed.

The [first diagnostic](bj22_abstract_diagonal_lemma_diagnostic_20261005.md)
used stage poles to freeze family labels. The following variant shows
that requiring one common pole set, a continuous extended-real outer
limit, or even a constant outer function net does not by itself repair
the unrestricted abstract assertion.

## Compact data satisfying the printed hypotheses

Take `K=[0,1]`, `S=N_(>0)`, `T=R` with its usual metric and
`rho(i)=a_i=1/i`. Define `log 0=-infinity`. For positive integers `i,j`
put

\[
 f_{i,j}(x)=\max\{\log x,a_i\log x-j\},\qquad
 F_i=\{f_{i,j}+c:j\geq1,\ c\in\mathbf R\}.
\]

Every stage has precisely the same pole set `{0}` and is finite on the
dense open complement `(0,1]`. It is continuous in the extended-real
topology because

\[
 \exp(f_{i,j}(x)+c)=e^c\max\{x,e^{-j}x^{a_i}\}
\]

is continuous on the whole compact interval, including zero. Each
family is stable under addition of every real constant. The unshifted
stages have value zero at `1` and supremum zero.

For each fixed `i`, increasing `j` gives a decreasing sequence with

\[
 f_{i,j}\searrow g,\qquad g(x)=\log x.
\]

At every positive `x`, the second term eventually lies below `log x`;
at zero both terms always have value minus infinity. The function `g`
is continuous as an extended-real function, is finite on `(0,1]` and
is not identically minus infinity. The inner numerical parameter is
constantly `a_i`, so `g in Ftilde_(a_i)` for every positive integer `i`.

Take the outer net to be the **constant sequence of functions** `g_i=g`
and the parameters `t_i=a_i->0`. Thus all the outer hypotheses in the
literal Lemma 4.6 hold; its conclusion would place `g` in `Ftilde_0`.

## The first closure at parameter zero is empty

Let `(h_b)` be any decreasing net with `h_b in F_(s_b)`. Fix an index
`b_0`. A stage with label `i` has, for all sufficiently small positive
`x`, the exact form

\[
 h(x)=a_i\log x+b_i
\]

Here `b_i=-j+c` for `i>1`, whereas `b_1=c` because the function for
`i=1` is simply `log x+c`. If a later stage had
`a_(s_b)<a_(s_(b_0))`, then at sufficiently small positive `x`,

\[
 h_b(x)-h_{b_0}(x)
   =(a_{s_b}-a_{s_{b_0}})\log x+C
   \longrightarrow+\infty\quad(x\longrightarrow0^+),
\]

for a finite real constant `C`. This contradicts decreasingness.
Consequently every `b>=b_0` satisfies

\[
 \rho(s_b)=a_{s_b}\geq a_{s_{b_0}}>0.
\]

The parameter cannot converge to zero. This argument includes arbitrary
directed nets, all real translations and all choices of the stage
integer `j`. Hence `Ftilde_0` is empty, despite the fixed function `g`
belonging to every `Ftilde_(1/i)`.

The obstruction persists with an identical closed pole set for every
stage and every inner and outer limit. It is the order of vanishing
near that pole: a finite translation cannot make a smaller logarithmic
slope lie below a larger one throughout a punctured neighbourhood.
The constant outer sequence also shows that numerical-parameter
closedness for a fixed function is not an automatic conclusion under
the printed **abstract** family hypotheses.

## Why this is not an algebraic psh counterexample

The data do not assign functions to actual rational line bundles with
their actual numerical classes. That missing relation is essential.
For example, on `P^1` the analogous potentials

\[
 \max\{\ell_p,a_i\ell_p-j\},\qquad \ell_p=\log|s_p|,
\]

can be placed in the common class `[O(1)]`: both summands belong to
that class after adding the appropriate nef zero class to the smaller
one, and the maximum is a same-class operation. Along `t ord_p`, their
initial slope at `t=0` is `-1`. For `i>1` it is strictly more negative
than `-a_i`. BJ22 Example 4.13 requires
degree at least one for such a normalized curve potential. Thus
for `i>1`, relabeling these functions by the smaller classes `a_i[O(1)]` would
not satisfy the algebraic psh hypotheses. The abstract parameter map
`rho(i)=a_i` is not an admissible line-bundle-class identification in
that curve example. The published curve characterization is used only
to clarify this failed realization; no general psh theorem is refuted.

The finite-valued-stage restriction reconstructed in the earlier note
is unaffected: the stages here have a genuine pole. The
[direct GF reconstruction](direct_gf_regularization_followup_20261005.md)
also remains distinct: it begins with an already decreasing net of
actual GF stages in actual converging classes. None of these abstract
examples supplies the missing general algebraic closure proof or a
critical Siu residual. This draft remains outside active TeX and changes
none of the 42 problem statuses. The separate Chapter 34 wording
correction is recorded with its own source and build audit; it does not
admit this construction as a new book result.

## Source and admission boundary

The controlling statement and printed proof remain BJ22 published
physical pages 63–64, printed pages 708–709, freshly read and viewed
earlier in this same continuation. The curve statement is Example 4.13,
printed page 712, freshly checked at text 3160–3190 within the larger
regularization/comparison reading already recorded. No fresh full paper
reading or independent production-model verification is claimed. This
strengthened construction remains a research candidate outside active
TeX and has not been promoted to a new book result.
