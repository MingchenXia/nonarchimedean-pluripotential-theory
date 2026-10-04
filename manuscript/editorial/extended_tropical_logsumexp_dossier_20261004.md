# An explicit strict-support function on extended tropical space

Date: 4 October 2026. This is a worked convex-analysis reconstruction for
the local strict-support ingredient in Wu,
[arXiv:2609.27610v1](https://arxiv.org/abs/2609.27610v1), Lemma 6.6.
It uses the classical log-sum-exp/entropy identity and gives the boundary
and rational-PL details explicitly. It is a research dossier outside the
active TeX closure, with no independent production-model receipt, general
envelope theorem, critical Siu proof or open-problem solution.

The source's printed strict comparison is `chi(t') > l(t)`. Since
`l(t)=chi(t)`, requiring this for every distinct pair would give both
`chi(t')>chi(t)` and `chi(t)>chi(t')`. That literal comparison is impossible.
The reconstruction below uses **`chi(t') > l_t(t')`**, the supporting-plane
comparison used by the source's subsequent proof of Lemma 6.7.
This correction is explicit; the printed statement is not silently
treated as a proved lemma.

## Function, domain and elementary bounds

Let \(T=\mathbf R\cup\{+\infty\}\), with its usual extended topology,
and let \(k\ge1\). Set \(\beta=\log(k+1)>0\), and define
\[
 \chi_k(t)=\frac1\beta
  \log\left(1+\sum_{j=1}^k e^{-\beta t_j}\right),
 \qquad e^{-\beta(+\infty)}=0.
\]
This is a finite continuous function on all of \(T^k\). With
\(f(t)=\max(0,-t_1,\ldots,-t_k)\), the maximum of the \(k+1\)
nonnegative exponential terms bounds their sum from below, and
\(k+1\) times that maximum bounds it from above. Hence
\[
                       f\le\chi_k\le f+1.
\]
In particular \(\chi_k(+\infty,\ldots,+\infty)=0\). The case
\(k=0\), if needed, is the one-point space with function zero.

## Supports at finite points and at boundary faces

Fix \(t\in T^k\), let \(J=\{j:t_j<+\infty\}\), and write
\[
 Z=1+\sum_{j\in J}e^{-\beta t_j},\qquad
 p_0=Z^{-1},\qquad
 p_j=Z^{-1}e^{-\beta t_j}\ (j\in J),\quad p_j=0\ (j\notin J).
\]
These are probabilities with \(p_0>0\) and \(p_j>0\) exactly for
\(j\in J\). Define the extended affine support
\[
 \ell_t(x)=\chi_k(t)-\sum_{j\in J}p_j(x_j-t_j).
\]
Its coefficients are nonpositive. It is finite and affine on a
neighbourhood of \(t\) in which all coordinates in \(J\) remain finite;
it ignores the coordinates infinite at \(t\). Globally it may take
\(-\infty\) where an active coordinate becomes infinite. It is therefore
not asserted to belong to the source's **globally finite-valued**
`Aff_R(T^k)`. All global comparisons below use this explicitly extended
support; its restriction near the contact point is an ordinary finite
affine support. No zero times infinity is needed because inactive terms
are omitted.

For \(x\in T^k\), form the analogous probabilities \(q_0,q_1,\ldots,q_k\).
If every \(x_j\), \(j\in J\), is finite, direct substitution gives
\[
 \chi_k(x)-\ell_t(x)
   =\frac1\beta\sum_{j:p_j>0}p_j\log\frac{p_j}{q_j}.
\]
If some active \(x_j\) is infinite, the left side and the corresponding
relative-entropy expression are both \(+\infty\), with the usual
positive-mass/zero-denominator convention. There is no cancellation of
two infinite values.

For finite relative entropy, \(\log r\le r-1\) gives
\[
 \sum_{j:p_j>0}p_j\log\frac{q_j}{p_j}
 \le \sum_{j:p_j>0}q_j-1\le0.
\]
Equality requires \(q_j=p_j\) for every active index, including zero,
and all remaining \(q_j=0\). Thus equality holds exactly when \(q=p\),
equivalently \(x=t\), since \(q_j/q_0=e^{-\beta x_j}\).
Consequently \(\ell_t(t)=\chi_k(t)\), and
\[
                   \chi_k(x)>\ell_t(x)\quad(x\ne t).
\]
This also proves the genuinely touching local convexity condition at
every boundary face, with no extraneous contact constant.

## A uniform positive gap outside every contact neighbourhood

Let \(D(p\Vert q)=\sum_{p_j>0}p_j\log(p_j/q_j)\) and
\(H(p)=-\sum_{p_j>0}p_j\log p_j\). If \(D(p\Vert q)\le R\), then
each active probability satisfies
\[
                  q_j\ge \exp\bigl(-(R+H(p))/p_j\bigr)>0.
\]
Indeed, every other summand is at least \(p_i\log p_i\), because
\(q_i\le1\); isolating the \(j\)-th summand gives the displayed bound.
In particular, \(q_0\) stays bounded away from zero. The probability
map identifies \(T^k\) with the part of the closed simplex where
\(q_0>0\), allowing zero values for the other coordinates.
Relative entropy is lower semicontinuous there. Each fixed sublevel
is therefore compact: its closure stays in \(q_0>0\) and preserves
the positive lower bounds at all active indices.

The gap \(d_t=\chi_k-\ell_t=D(p\Vert q)/\beta\) has a unique zero at
\(t\). For an open neighbourhood \(V\) of \(t\), the compact set
\(\{d_t\le1\}\setminus V\) has positive minimum if nonempty.
If empty, the gap is greater than one outside \(V\).
Taking a smaller positive number in either case gives
\[
             \ell_t<\chi_k-\delta\quad\hbox{on }T^k\setminus V
\]
for some \(\delta>0\). This supplies the separation property without
importing an uninspected extended-tropical compactness lemma.

## Global rational PL approximations, including infinite coordinates

Let \(\Delta_k\) be the probability simplex with coordinates
\(r_0,\ldots,r_k\), and use \(0\log0=0\). The entropy identity is
\[
 \chi_k(t)=\max_{r\in\Delta_k}
 \left\{-\sum_{j=1}^k r_jt_j+\frac{H(r)}\beta\right\}.
\]
At infinite coordinates the admissible face has \(r_j=0\) there;
other terms are \(-\infty\). The identity follows from the same
relative-entropy calculation, with maximizer \(r=p(t)\).

Take successive barycentric subdivisions of the standard simplex.
They have rational vertices, include every original vertex, preserve
every coordinate face, and their meshes tend to zero. The continuous
function \(H/\beta\) is uniformly continuous on the closed simplex.
Given \(\varepsilon>0\), choose a subdivision so fine that on each
cell, for \(r=\sum_v\lambda_vv\),
\[
 0\le \frac{H(r)}\beta-
        \sum_v\lambda_v\frac{H(v)}\beta<\varepsilon.
\]
The first inequality is entropy concavity; the second follows from
uniform continuity because all cell vertices are close to \(r\).
The linear term is exactly its barycentric interpolation. Consequently
\[
 g(t)=\max_v\left\{-\sum_{j=1}^k v_jt_j+\frac{H(v)}\beta\right\}
 \quad\hbox{satisfies}\quad 0\le\chi_k-g<\varepsilon
\]
uniformly on all of \(T^k\), not just on bounded finite-coordinate sets.
Face preservation gives the same argument when some coordinates are
infinite. Approximate the finitely many constants \(H(v)/\beta\)
from below by rationals with an arbitrarily small common error. Keep
the original simplex vertices' constants zero. The resulting maximum
has rational coefficients and constants, retains the terms
\(0,-t_1,\ldots,-t_k\), and remains a finite continuous convex function.

It also satisfies the source's finite-open-cover PL requirement.
For each set \(A\) of finite coordinates, retain only terms supported
in \(A\). On the open set where those coordinates are finite and every
other term is strictly below their finite maximum, the function is the
maximum of finitely many ordinary rational affine functions.
Every point belongs to the set for its finite coordinates, since all
discarded terms are \(-\infty\) there. These at most \(2^k\) open
sets cover \(T^k\). Near an infinite-coordinate face the maximum thus
depends only on finite coordinates, as required.

Choose rational \(\varepsilon_i=2^{-i}\) and such maxima \(g_i\) with
\(0\le\chi_k-g_i<\varepsilon_i/4\). Then
\[
 u_i=g_i+\varepsilon_i,\qquad
 \chi_k+3\varepsilon_i/4<u_i\le\chi_k+\varepsilon_i.
\]
Since \(\varepsilon_{i+1}=\varepsilon_i/2\), one has
\(u_{i+1}<u_i\) everywhere, and \(u_i\searrow\chi_k\) uniformly
on all of \(T^k\). Thus the claimed rational-PL approximation does
not rely on an unproved interchange of limits at infinite coordinates.

## What this reconstructs, and what it leaves open

For algebraic coordinates \(f_1,\ldots,f_k\) on an affine variety,
pullback replaces \(-t_j\) by \(\log|f_j|\). Each rational-slope term
is a rational multiple of the logarithm of a monomial in the \(f_j\),
plus a rational constant: choose a positive integer \(m\) clearing that
term's slopes, and use the polynomial \(\prod_j f_j^{m v_j}\) with
coefficient \(1/m\). If the \(f_j\) generate the coordinate ring,
the original simplex vertices retain the terms \(\log|f_j|\) with
coefficient one and the constant term. Thus the polynomial list can
include the generators themselves, rather than only their powers.
Zero monomials on the variety may be discarded; the constant term
keeps the maximum finite. Each pullback of \(u_i\) then satisfies the
actual affine FS definition 3.15(1), which permits separate positive
rational coefficients on its polynomial terms.

Let \(F=\max(0,\log|f_1|,\ldots,\log|f_k|)\), itself an affine FS
function. The explicit bounds give
\(F\le\chi_k\circ\operatorname{Trop}\le F+1\).
Consequently this special pullback satisfies **both** the printed lower
growth bound in Definition 3.15(2) and the upper bound used for weakly
psh functions in Definition 6.1(2). Its explicit decreasing FS
approximants also establish its regularizable membership. No change of
the printed growth convention is needed for this particular function.
This does not reconcile the two growth conventions for arbitrary
functions in the later comparison proof.

This supplies a direct candidate reconstruction of the **corrected**
strict-support lemma and its special rational-PL ingredient.
It does not verify every statement in APW26b, the source's general
tropical-PL approximation lemma, the singular-stratum norm and Runge
arguments, descent on non-countable ground fields, or Theorem 7.1.
The independent proof and all definition interfaces of that larger
claim remain separate tasks. Existing Siu conditional statements and
the book's 42-atom inventory are unchanged.
