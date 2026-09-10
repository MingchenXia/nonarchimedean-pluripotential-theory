# P14.3 V5 current exact-live source audit

This is a local integrity audit, not a new theorem or a production verifier receipt.
It binds the accepted conditional V3 packet to the listed current live sources.

## chapter71_finite_energy_and_p143 — lines 1038–1272

```text
\begin{theorem}\label{thm:pseff-kahler-finite-energy-link}
There is a bijection
\[
 \mathcal E^{1,\NA}_{\mathrm{DXZ}}(X,\omega)
 \xrightarrow{\ \sim\ }
 \mathcal E^1_{\mathrm{MP}}(\alpha).
\tag{71.39}\label{eq:pseff-finite-energy-bijection}
\]
It sends a test curve \(\Gamma\) to the MP potential \(\phi\) determined
on rational divisorial points by
\[
 \phi(p^{-1}\ord_E)
 =\mathfrak T_\Gamma(p^{-1}\ord_E),
 \qquad E\text{ prime},\quad p\in\mathbf Q_{>0}.
\tag{71.40}\label{eq:pseff-finite-energy-divisorial-link}
\]
Equivalently, both sides encode the same maximal radial asymptotic data.
For any chosen \(u_0\in\mathcal E^1(X,\omega)\),
\Cref{thm:mp-maximal-ray} selects the unique maximal representative with
initial value \(u_0\).  The radial and non-Archimedean energies agree under
\eqref{eq:pseff-finite-energy-bijection}.
\end{theorem}

\begin{proof}
By \cite[Theorem~3.17]{DXZ23}, inverse Legendre transform is a bijection
from finite-energy \(\mathcal I\)-maximal test curves to the corresponding
finite-energy rays emanating from \(V_\omega=0\), and it identifies radial
energy with DXZ non-Archimedean energy.  Applying the radial construction
of \cite[Theorem~5.1.4 and Section~5.2]{MP24} gives an element of
\(\mathcal E^1_{\mathrm{MP}}(\alpha)\).  Conversely,
\cite[Theorem~5.1.7]{MP24}, restated as
\Cref{thm:mp-maximal-ray}, applied with initial value \(0\), supplies the
maximal ray whose Ross--Witt Nystr\"om transform recovers the DXZ test
curve.  This proves \eqref{eq:pseff-finite-energy-bijection}.  A different
initial value changes the maximal representative, not its radial
non-Archimedean data.

For \(v=p^{-1}\ord_E\), \cite[Theorem~5.1.4 and Section~5.2]{MP24}
defines the MP value as the negative generic Lelong number of the
complexified ray and identifies it with the associated DXZ divisorial
potential.  Equation \eqref{eq:pseff-divisorial-analytification} identifies
that potential with \(\mathfrak T_\Gamma(v)\).  The convention comparison
preceding the theorem shows that the two source normalizations give the
same coefficient.  This proves
\eqref{eq:pseff-finite-energy-divisorial-link}.  Uniqueness of the MP psh
extension follows from \cite[Theorem~4.3.8]{MP24}.  Finally, equality of
energies is the last assertion of \cite[Theorem~3.17]{DXZ23}, together
with the MP slope formula \cite[Theorem~5.3.4]{MP24}.
\end{proof}

\begin{remark}\label{rem:pseff-finite-energy-raw-function}
The theorem characterizes the MP potential by the divisorial restriction
of the raw ideal-valuative transform.  It does not assert, on a general
compact K\"ahler manifold, that the two functions have already been proved
equal at every nondivisorial point.  The next subsection supplies that
equality in the finite-energy K\"ahler domain only.
\end{remark}

\subsection{Domination-preserving divisorial approximation}

Ordinary density of rational divisorial valuations does not control the
ideal order needed by the raw transform.  The following refinement does.
Write \(q\preceq v\) when
\[
 q(\mathfrak a)\leq v(\mathfrak a)
 \qquad\text{for every coherent ideal }\mathfrak a\subseteq\mathcal O_X.
\tag{71.41a}\label{eq:p143-ideal-order}
\]
Here \(X^{\divis}\) follows the convention of
\cite[Definition~2.3.1]{MP24}: it contains the trivial semivaluation \(0\),
as well as the nonnegative rational multiples of divisor orders on proper
bimeromorphic models.  Thus the zero-weight case below is part of the same
divisorial locus, rather than an exception to the statement.

\begin{theorem}\label{thm:p143-dominated-divisorial-density}
For every \(v\in X^{\bethan}\),
\[
 v\in\overline{\{q\in X^{\divis}:q\preceq v\}}.
\tag{71.41b}\label{eq:p143-dominated-divisorial-density}
\]
Equivalently, there is a net \((q_\lambda)\) of rational divisorial
points with \(q_\lambda\preceq v\) and \(q_\lambda\to v\) in the
pointwise topology on coherent ideals.  This includes semivaluations with
proper support and with value \(+\infty\) on a nonzero ideal.

Consequently, let \(\alpha\) be a K\"ahler class, let
\(F:X^{\bethan}\to[-\infty,c]\) be upper semicontinuous and antitone for
\eqref{eq:p143-ideal-order}, and let \(\phi\in\PSH_{\mathrm{MP}}(\alpha)\).
If \(F=\phi\) on \(X^{\divis}\), then \(F=\phi\) on all of
\(X^{\bethan}\).
\end{theorem}

\begin{proof}
Let \(\pi:Y\to X\) be a proper bimeromorphic morphism of connected
compact K\"ahler manifolds.  Pullback induces a continuous map
\(\pi^{\bethan}:Y^{\bethan}\to X^{\bethan}\).  Its image is closed,
because \(Y^{\bethan}\) is compact and \(X^{\bethan}\) is Hausdorff.  It
contains \(X^{\divis}\) by birational invariance of divisorial valuations
\cite[Remark~2.3.2]{MP24}; hence it equals \(X^{\bethan}\) by
\Cref{thm:mp-divisorial-density}.  In particular every \(v\) has a lift
\(\widetilde v\in Y^{\bethan}\).

We first record a domination construction on a simple-normal-crossing
model.  Let \(B_1,\ldots,B_k\) be distinct smooth SNC divisors on \(Y\)
with \(\widetilde v(\mathcal O_Y(-B_i))>0\), and choose finite rational
numbers
\[
 0<a_i\leq\widetilde v(\mathcal O_Y(-B_i)).
\tag{71.41c}\label{eq:p143-dominated-weights}
\]
Let \(Z\) be the central variety of \(\widetilde v\).  By
\cite[Lemma~2.1.1]{MP24}, its ideal \(\mathcal I_Z\) is maximal among
coherent ideals of positive value, so \(Z\subseteq B_i\) for every
\(i\).  Let \(W\) be the connected component of
\(B_1\cap\cdots\cap B_k\) containing \(Z\).  The monomial valuation
\(q\) along \(W\) with weights \((a_i)\) is independent of the point of
\(W\) by \cite[Proposition~2.3.4]{MP24}, and belongs to \(Y^{\divis}\)
by \cite[Remark~2.3.5]{MP24}.

We claim that \(q\preceq\widetilde v\).  For \(s>0\), set
\[
 \mathfrak c_s=
 \sum_{\substack{\beta\in\mathbf Z_{\geq0}^k\\
                   \sum_i a_i\beta_i\geq s}}
 \mathcal O_Y\left(-\sum_i\beta_iB_i\right).
\tag{71.41d}\label{eq:p143-monomial-ideal}
\]
After deleting redundant generators, this is a finite coherent sum: its
exponent set is upward closed, and each minimal exponent has
\(\beta_i\leq\lceil s/a_i\rceil\).  In extended-real order,
\[
 \widetilde v(\mathfrak c_s)
 =\min_{\beta}\sum_{i:\,\beta_i>0}
       \beta_i\widetilde v(\mathcal O_Y(-B_i))
 \geq\min_{\beta}\sum_i\beta_i a_i\geq s.
\tag{71.41e}\label{eq:p143-monomial-value-bound}
\]
The restriction to positive exponents avoids any expression
\(0\cdot(+\infty)\).

Let \(\mathfrak j\) be a nonzero coherent ideal and take
\(0<s<q(\mathfrak j)\).  In SNC coordinates transverse to \(W\), the
condition \(q(\mathfrak j)>s\) says exactly that every transverse Taylor
coefficient of weighted degree less than \(s\) vanishes identically along
\(W\).  There are only finitely many such exponents, and therefore
\(\mathfrak j\subseteq\mathfrak c_s\) on a neighbourhood of \(W\).
Put \(Q=(\mathfrak j+\mathfrak c_s)/\mathfrak c_s\) and
\(\mathfrak k=\operatorname{Ann}(Q)\).  Then \(\mathfrak k\) is the
unit ideal near \(W\) and \(\mathfrak k\mathfrak j\subseteq
\mathfrak c_s\) globally.  It has \(\widetilde v(\mathfrak k)=0\): a
positive value would force \(\mathfrak k\subseteq\mathcal I_Z\), which
is impossible near \(Z\subseteq W\).  Thus
\[
 \widetilde v(\mathfrak j)
 =\widetilde v(\mathfrak k\mathfrak j)
 \geq\widetilde v(\mathfrak c_s)\geq s.
\]
Letting \(s\uparrow q(\mathfrak j)\) proves the claim; the cases
\(q(\mathfrak j)=0\) and \(\mathfrak j=0\) are immediate.

Now fix finitely many nonzero coherent ideals
\(\mathfrak a_1,\ldots,\mathfrak a_\ell\) on \(X\).  Simultaneous
analytic principalization yields a proper modification \(\pi:Y\to X\),
with \(Y\) smooth compact K\"ahler, such that
\[
 \mathfrak a_j\mathcal O_Y=
 \mathcal O_Y(-D_j),\qquad
 D_j=\sum_{i=1}^r d_{ji}B_i,qquad d_{ji}\in\mathbf Z_{\geq0},
\tag{71.41f}\label{eq:p143-simultaneous-principalization}
\]
where the distinct \(B_i\) form an SNC divisor.  Lift \(v\), and put
\(w_i=\widetilde v(\mathcal O_Y(-B_i))\).  Retain exactly the indices
with \(w_i>0\), choose rational \(a_i\) as in
\eqref{eq:p143-dominated-weights}, and give the other components weight
zero.  If no index is retained, take \(q_Y=0\); otherwise the preceding
construction gives a rational divisorial \(q_Y\preceq\widetilde v\).  In
both cases,
\(q_X:=\pi^{\bethan}(q_Y)\in X^{\divis}\) and \(q_X\preceq v\).
For every \(j\),
\[
 v(\mathfrak a_j)=\sum_{i:\,d_{ji}>0}d_{ji}w_i,\qquad
 q_X(\mathfrak a_j)=\sum_{i:\,d_{ji}>0}d_{ji}a_i.
\tag{71.41g}\label{eq:p143-principalized-values}
\]
Indeed, a zero-weight component cannot contain \(W\): otherwise
\(\mathcal O_Y(-B_i)\subseteq\mathcal I_Z\), forcing \(w_i>0\).
Its monomial value is consequently zero, as used in the second formula.

For every finite positive \(w_i\), let \(a_i\) increase rationally to
\(w_i\); for \(w_i=+\infty\), let \(a_i\) tend to infinity.  The finite
sums in \eqref{eq:p143-principalized-values} then converge in
\([0,+\infty]\).  More explicitly, direct the pairs \((S,N)\), where
\(S\) is a finite set of nonzero coherent ideals and \(N\geq1\), by
inclusion in the first coordinate and the usual order in the second.  For
each pair, principalize the ideals in \(S\) and choose the displayed
weights so that every finite value on \(S\) is approximated from below
within \(1/N\), while every infinite value on \(S\) exceeds \(N\).
The resulting rational divisorial point \(q_{S,N}\preceq v\) belongs to
each corresponding basic pointwise neighbourhood.  Hence
\((q_{S,N})\) converges to \(v\), with no order relation required between
two separately chosen divisorial points.

For the final statement, choose the dominated net.  Antitonicity and
divisorial agreement give
\(F(v)\leq F(q_\lambda)=\phi(q_\lambda)\).  Upper semicontinuity of
\(\phi\) gives \(F(v)\leq\phi(v)\), also when \(\phi(v)=-\infty\), by
testing each finite upper threshold.  Conversely,
\cite[Theorem~4.3.8]{MP24} applied to the upper-semicontinuous function
\(F\) promotes the divisorial inequality \(\phi\leq F\) to all of
\(X^{\bethan}\).  Hence \(F=\phi\).
\end{proof}

\begin{corollary}\label{cor:p143-all-point-kahler-comparison}
Let \(\alpha\) be a K\"ahler class and let
\(\Gamma\in\mathcal E^{1,\NA}_{\mathrm{DXZ}}(X,\omega)\).  If \(\phi\)
is its corresponding MP finite-energy potential under
\eqref{eq:pseff-finite-energy-bijection}, then
\[
 \mathfrak T_\Gamma(v)=\phi(v)
 \qquad(v\in X^{\bethan}).
\tag{71.41h}\label{eq:p143-all-point-kahler-comparison}
\]
\end{corollary}

\begin{proof}
By \Cref{thm:p142-raw-transform-usc}, \(\mathfrak T_\Gamma\) is upper
semicontinuous.  If \(q\preceq v\), every multiplier-ideal evaluation at
\(q\) is at most its evaluation at \(v\).  The defining formula
\eqref{eq:pseff-test-curve-transform} therefore gives
\(\mathfrak T_\Gamma(q)\geq\mathfrak T_\Gamma(v)\).  The divisorial
identity \eqref{eq:pseff-finite-energy-divisorial-link} now lets us apply
\Cref{thm:p143-dominated-divisorial-density}, proving
\eqref{eq:p143-all-point-kahler-comparison}.
\end{proof}

```

## chapter72_p143_boundary — lines 3376–3402

```text
is proved.  The domination-preserving rational-divisorial approximation in
\Cref{thm:p143-dominated-divisorial-density}, combined with the P14.2
upper-semicontinuity theorem and the existing divisorial comparison, now
identifies the literal raw transform with the corresponding MP potential at
every semivaluation in the finite-energy K\"ahler domain; see
\Cref{cor:p143-all-point-kahler-comparison}. Its source inputs,
extended-value arithmetic, and draft build are reproducibly checked.  The
frozen V3 source-bound packet embeds immutable excerpts of MP24 and DXZ23,
with their full-file hashes.  Following its initial review, the same frozen
statement and proof received a production review by \texttt{gpt-5.6-sol} at
\texttt{xhigh}, with final verdict \texttt{correct}, zero critical errors,
and zero gaps (\texttt{pi\_75b42272e15105bb6be0525c}).  Its exact archived
HTTP receipt and strict protocol audit are recorded in
\nolinkurl{solver_dossiers_20260909/p143_v3_source_bound_packet_20260909/}
\nolinkurl{PRODUCTION_RECEIPT_SOL_20260909.md}.  This verifies exactly the
conditional dominated-approximation and all-point comparison packet:
P14.2 upper semicontinuity and the Chapter~71 finite-energy divisorial
normalization remain explicitly named premises.  This finite-energy result
neither establishes general MP positivity at arbitrary nondivisorial points
nor retires P14.3.
The historical local V4 exact-live audit in
\nolinkurl{solver_dossiers_20260909/p143_v3_source_bound_packet_20260909/}
\nolinkurl{LIVE_SOURCE_AUDIT_V4_20260909} records then-current Chapter~71
lines, the accepted V3 packet, and this boundary by local hashes and a range
checker.  It is a local integrity gate, not a replayable release pin or a
production verifier receipt; the production receipt above likewise does not
alter the P14.3 status.
```

## inventory_p143_boundary — lines 1229–1245

```text
- **P14.3** `[T4; open; source-bound conditional theorem verified]` Decide
  MP positivity at those semivaluations.  The Chapter 71
  domination-preserving rational-divisorial theorem and its finite-energy
  K\"ahler corollary recover the all-point comparison from P14.2 upper
  semicontinuity and divisorial agreement.  Its frozen V3 source-bound
  packet embeds hashed MP24 and DXZ23 excerpts.  After its initial review,
  the same frozen V3 files passed an isolated `gpt-5.6-sol` / `xhigh`
  production review: final `correct`, zero critical errors, and zero gaps
  (`pi_75b42272e15105bb6be0525c`).  Its archived HTTP receipt and strict
  protocol audit are in `p143_v3_source_bound_packet_20260909/`
  `PRODUCTION_RECEIPT_SOL_20260909.md`.  It verifies only the conditional
  bridge: P14.2 upper semicontinuity and the finite-energy divisorial
  normalization are explicit premises.  The general MP-positivity problem
  remains open.  The historical local V4 exact-live audit records
  then-current Chapter 71 source ranges, the frozen V3 packet, and this
  live-open boundary; it is a local integrity check, rather than a
  replayable release pin or production verifier receipt.
```
