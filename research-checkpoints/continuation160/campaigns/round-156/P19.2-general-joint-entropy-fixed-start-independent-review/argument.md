# Entire unreviewed mathematical manuscript

\documentclass[11pt]{article}
\usepackage[a4paper,margin=25mm]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathrsfs,hyperref}
\setlength{\emergencystretch}{3em}
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newcommand{\MA}{\operatorname{MA}}
\newcommand{\Ent}{\operatorname{Ent}}
\newcommand{\Ric}{\operatorname{Ric}}
\newcommand{\NA}{\mathrm{NA}}
\newcommand{\PSH}{\operatorname{PSH}}
\title{Joint entropy recovery at a prescribed finite-entropy start\\
\large Partial progress on the unchanged original P19.2}
\author{Research draft; no claim of a complete solution}
\date{6 October 2026}
\begin{document}
\maketitle
\begin{abstract}
Working with the four complete mathematical grants in the input, we
prove a joint entropy/time recovery theorem for maximal weak rays on
every fixed smooth compact K\"ahler manifold. The actual finite-entropy
initial potential is retained and can be unbounded and nonmodel.
Strong convergence of non-Archimedean data, entropy recovery, finite-time
lower semicontinuity, and recession slopes suffice: no uniform mixed
pairing error estimate is needed. A convex chord argument treats the
cohomological correction as a difference of convex contracted energies.
There is also a joint divergence theorem for infinite non-Archimedean
entropy. These conclusions improve the general fixed-start mechanism
recorded in grant S, but construct neither closed relative P-profile
recovery nor approximations of arbitrary nonmaximal rays. The entire
original P19.2 is not solved, and no full-scope analytic obstruction
is proved. All results are unverified drafts relative to the stated
caller grants.
\end{abstract}

\section{The unchanged task and the result obtained}
The exact original P19.2 is: construct model approximations in the
residual hybrid programme preserving all required energy, entropy and
singularity data; energy convergence alone is insufficient, and the
published/source-stated projective Fujita regimes are established
subcases. The full supplied assignment additionally retains arbitrary
actual finite-energy weak rays, their actual prescribed singular starts,
closed finer P data, and raw mixed masses, including genuine zero-mass
and identically minus-infinite levels as distinct data. It requires
the original carrier with supported semivaluations, discrepancy factors,
actual positive models or flag configurations, general compact
K\"ahler/transcendental classes, and the joint entropy/time normalization.
It expressly does not permit an argument about one maximalization
mechanism to be counted as universal model-approximation nonexistence.

We preserve this task rather than replacing it with our theorem's
signature. The complete original input, task and assignment are frozen
as local artifacts, with the native notes list empty. Our theorem is
restricted to the maximal branch with a finite-entropy actual start.
It does not assert convergence of entropy at a fixed positive time,
or of any prescribed closed P-profile. The new claim is joint
entropy/time recovery in this general fixed-manifold maximal branch.
The original atom therefore remains unresolved.

\section{Conventions, carrier, and actual models}
Let $X$ be connected, smooth and compact K\"ahler, of dimension $n\ge1$.
Fix a K\"ahler form $\omega$, $\alpha=[\omega]$,
$V=\int_X\omega^n$ and $\mu_0=\omega^n/V$. Throughout,
\[
 dd^c=\frac{i}{2\pi}\partial\bar\partial,\qquad
 t=-\log|\tau|^2,\qquad dd^c\log|f|^2=[\operatorname{div}(f)].
 \tag{1}
\]
For $u\in\mathcal E^1(X,\omega)$ use the complete finite-energy
extensions of
\[
 E(u)=\frac1{(n+1)V}\sum_{k=0}^n
  \int_X u\,\langle\omega_u^k\rangle\wedge\omega^{n-k},\quad
 \MA(u)=V^{-1}\langle\omega_u^n\rangle,\quad
 H(u)=\Ent(\MA(u)\mid\mu_0).
 \tag{2}
\]
These are full probability conventions: $E(0)=0$, $E(u+c)=E(u)+c$,
and entropy is infinite without absolute continuity. Here
$\omega_u=\omega+dd^cu$, and brackets denote nonpluripolar products.
An actual weak ray is strongly continuous at time zero and is the
canonical finite-energy weak geodesic on every finite interval.
Its total potential is $U(x,\tau)=u_{-\log|\tau|^2}(x)$.

The non-Archimedean carrier is the original full $X^\beth$ in the
trivially valued theory of the grants. Values $+\infty$ on the support
of a semivaluation are retained. The usual datum is obtained from
the generic divisorial coefficients of the actual total potential,
after an affine time normalization where required. It is not assigned
by a pointwise quotient of an infinite value by time.

An actual relatively K\"ahler model in this paper is a smooth
equivariant proper modification
$\rho:\mathcal Y\to X\times\mathbf P^1$, trivial away from the central
fiber, with a vertical real divisor $D$ and relatively K\"ahler class
$\mathcal A=\rho_X^*\alpha+[D]$. The construction imported from R
produces such geometric models, not just formal PL functions.
In a general transcendental class this is cohomological data;
there need not be a rational line bundle. We do not call a merely
nef or log-discrepancy class semiample.

On a central Gauss component $F$, put $b_F=\operatorname{ord}_F(\tau)$.
The model datum is $f_D(v_F)=D_F/b_F$, with compatibility sign
$U+\log|s_D|^2=O(1)$ for bounded compatible model weights.
The component formulas are
\[
 \MA_\alpha(f_D)=\frac1V\sum_F b_F(\mathcal A^n\cdot F)\delta_{v_F},
 \qquad E_\alpha(f_D)=\frac{\mathcal A^{n+1}}{(n+1)V},
 \qquad H_\alpha(\psi)=\int_{X^\beth}A_X\MA_\alpha(\psi).
 \tag{3}
\]
The compactification in (3) is trivialized near infinity as in R.
The top measure has total mass one. On an SNC model the discrepancy
factor on $F$ is $(\kappa_F+1-b_F)/b_F$, where $\kappa_F$ is the
relative canonical coefficient. Thus neither nonreduced central
multiplicities nor discrepancy factors are discarded. Strong limits,
energies, and mixed pairings in (3) are those of grant R.

For a prescribed start $w$ write $r(w,\psi)$ for its actual maximal
ray. The model datum does not make this ray's residual weight bounded
when $w$ is unbounded. We keep $w$ exactly, rather than replacing it
with a model initial potential.

\section{Exact premises and new source application}
The complete caller bodies R, T, C and S, and only those bodies, are
grants. Their historical verdicts are not premises. The following
specific consequences of R are used.
\begin{enumerate}
\item For every actual $w\in\mathcal E^1$ and
$\psi\in\mathcal E^{1,\NA}(\alpha)$, $r(w,\psi)$ exists, is ordered
in both arguments, and has
$E(r(w,\psi)_t)=E(w)+tE_\alpha(\psi)$. Its usual datum is $\psi$.
Strong convergence $\psi_j\to\psi$ with the same $w$ gives bounded-time
$d_1$ convergence of the maximal rays.
\item For maximal rays with a finite-entropy slice,
$\lim_{t\to\infty}H(r_t)/t=H_\alpha(\psi)$, including $+\infty$.
When $H(w)$ and $H_\alpha(\psi)$ are finite, every finite-time
entropy is finite. An arbitrary nonmaximal actual ray has infinite
entropy slope, and its maximalization has positive energy defect.
\item Fixed smooth cohomological contracted energies have calibrated,
finite recession slopes on maximal rays. These slopes are strongly
continuous in $\psi$. Energy and the standard finite-energy
comparison/decreasing-geodesic foundations are also granted.
\item When $H_\alpha(\psi)<\infty$, there are actual relatively
K\"ahler model data $\eta_j\to\psi$ strongly with
$H_\alpha(\eta_j)\to H_\alpha(\psi)$ (R, equation (16)).
This construction does not grant finer P-profile recovery.
\end{enumerate}
We do not independently reprove R or its external theorem chain.
T supplies its zero-start one-branch $\mathbf P^1$ result only;
C its finite-entropy absolute-endpoint example on $\mathbf P^n$,
$n\ge2$, only; S its scoped singular-start models, relative lemma,
closed-level calculations and stated general mechanism only. These
three are used below to delimit scope, not to expand the main theorem.
The ledger supplied inside S is historical source data and has not
been treated as our own reading record.

One primary source is newly applied: the published
Berman--Darvas--Lu paper \cite{BDL}. On a connected compact K\"ahler
manifold its Proposition 4.4 says that the contracted energy
$\mathrm{AM}_\gamma$, for a smooth closed real $(1,1)$ form $\gamma$,
extends $d_1$-continuously to $\mathcal E^1$ and is bounded on
$d_1$-bounded sets. Proposition 4.5 gives its convexity for smooth
positive $\gamma$ along weak geodesics with bounded Laplacian.
Theorem 4.7, at twist zero and $p=1$, gives $d_1$ lower
semicontinuity and geodesic convexity of the extended Mabuchi functional.
The complete statement/proof units for these applications were read;
literal source coordinates and precise convention conversion are
recorded in the appendix. No projectivity occurs in these statements.

The source uses $i\partial\bar\partial$. Set $v=u/(2\pi)$ with the
same background $\omega$; the currents and probability measures coincide.
Its distance is $d_{1,\mathrm{BDL}}=d_1/(2\pi)$,
$\mathrm{AM}(v)=E(u)/(2\pi)$, and for the same smooth form $\gamma$,
\[
 T_\gamma(u):=\frac1V\sum_{k=0}^{n-1}
  \int_Xu\,\gamma\wedge\langle\omega_u^k\rangle
                     \wedge\omega^{n-1-k}
 =2\pi n\,\mathrm{AM}_\gamma(v).                    \tag{4}
\]
Consequently these continuity and convexity assertions keep their
sign and domain. To extend the bounded-geodesic convexity in
Proposition 4.5 to an arbitrary finite-energy segment, decrease smooth
endpoints to its endpoints. The canonical geodesics decrease and
converge in $d_1$ at each time by the granted R foundations.
Apply Proposition 4.4 at each time to their contracted energies.
Taking the limit of the convexity inequalities proves convexity
of $T_\gamma$ for the desired segment. This argument explicitly
uses the finite-energy extension and does not extrapolate the
bounded statement without proof.

Put $\Ric(\omega)=-dd^c\log\omega^n$ and
$\overline S=nV^{-1}\int_X\Ric(\omega)\wedge\omega^{n-1}$. Define
\[
 M(u)=H(u)+G(u),\qquad
 G(u)=T_{-\Ric(\omega)}(u)+\overline S E(u).           \tag{5}
\]
The source's Ricci form and mean scalar are $2\pi$ times ours.
Using (4) in its untwisted formula gives exactly (5), with entropy
coefficient one. Thus $M$ is lower semicontinuous and convex in
our convention. This fixes both probability and squared-log time
normalizations rather than importing an uncalibrated slope.

\section{The convex chord argument}
\begin{lemma}[Finite recession recovery]\label{convex}
Let $f_j:[0,\infty)\to\mathbf R$ be finite convex functions with
$f_j(0)\to a\in\mathbf R$. Let $f$ be finite convex with $f(0)=a$.
Suppose for every $T>0$, $\liminf_j f_j(T)\ge f(T)$,
and
\[
 \ell_j=\lim_{t\to\infty}f_j(t)/t\to\ell
           =\lim_{t\to\infty}f(t)/t\in\mathbf R.
\]
Then $f_j(t_j)/t_j\to\ell$ for every $j\to\infty$ and
$t_j\to\infty$.
\end{lemma}
\begin{proof}
Convexity makes $(f_j(t)-f_j(0))/t$ nondecreasing and bounded above
by $\ell_j$. For $t\ge T>0$,
\[
 \frac{f_j(0)}t+\frac{f_j(T)-f_j(0)}T
 \le\frac{f_j(t)}t\le\frac{f_j(0)}t+\ell_j.          \tag{6}
\]
Along any joint sequence the upper bound tends to $\ell$ and the
lower bound has liminf at least $(f(T)-a)/T$. Let $T\to\infty$.
The two bounds coincide. The same proof applies to any subsequence
of indices, so the asserted quantifier is genuinely joint.
\end{proof}

\begin{lemma}[Infinite recession lower recovery]\label{infinite}
Keep $f_j$ finite convex with $f_j(0)\to a$.
Let $f:[0,\infty)\to\mathbf R\cup\{+\infty\}$ be extended convex,
with $f(0)=a$, $\liminf_j f_j(T)\ge f(T)$ at every $T>0$, and
$\lim_{t\to\infty}f(t)/t=+\infty$.
Then $f_j(t_j)/t_j\to+\infty$ for every joint sequence.
No convergence assumption on $\ell_j$ is needed.
\end{lemma}
\begin{proof}
Use the lower bound in (6). If $f(T)=+\infty$ at some fixed $T$,
it already implies divergence along the joint sequence. Otherwise
all $f(T)$ are finite, and $(f(T)-a)/T$ is arbitrarily large for
large $T$. First fix such a $T$, take the joint liminf, and then
let $T$ increase. This gives divergence to $+\infty$.
\end{proof}

Neither lemma proves $f_j(T)\to f(T)$. The finite lemma uses only
a one-sided inequality at a fixed time. It also gives no uniform
additive $O(1)$ recession remainder.

\section{Joint cohomological slopes}
For a smooth closed form $\gamma$ write $L_\gamma(\psi)$ for the
calibrated recession slope of $T_\gamma(r(w,\psi)_t)$ supplied by R.
It is finite, independent of the chosen finite-energy start, and
strongly continuous in $\psi$. For a model $f_D$ its exact
intersection expression is
\[
 L_\gamma(f_D)=\frac{\mathcal A^n\cdot\rho_X^*[\gamma]}V.
 \tag{7}
\]
This is the contracted mixed-energy slope, not a probability
renormalization of a raw level mass.

\begin{proposition}\label{cohomological}
Let $\psi_j\to\psi$ strongly in $\mathcal E^{1,\NA}(\alpha)$,
keep any $w\in\mathcal E^1$ fixed, and put
$r_j=r(w,\psi_j)$, $r=r(w,\psi)$.
For every smooth closed real $(1,1)$ form $\gamma$ and every joint
$j\to\infty$, $t_j\to\infty$,
\[
 \frac{T_\gamma(r_{j,t_j})}{t_j}\longrightarrow L_\gamma(\psi),
 \qquad
 \frac{G(r_{j,t_j})}{t_j}\longrightarrow G_\alpha(\psi),\quad
 G_\alpha=L_{-\Ric(\omega)}+\overline S E_\alpha.      \tag{8}
\]
\end{proposition}
\begin{proof}
Assume first that $\gamma\ge0$. Its contracted energy is a finite
convex function along each finite-energy ray, by Section 3.
At any fixed $T$, R gives $r_{j,T}\to r_T$ in $d_1$.
Proposition 4.4 after (4) gives
$T_\gamma(r_{j,T})\to T_\gamma(r_T)$.
Initial values are all $T_\gamma(w)$. Their finite recession
slopes converge by R's strongly continuous calibrated pairing.
Lemma \ref{convex} therefore proves the first limit.

For any signed $\gamma$ choose a fixed $c>0$ sufficiently large
that $\gamma+c\omega\ge0$. Write
$\gamma=(\gamma+c\omega)-c\omega$ and apply the preceding
argument to both terms. Linearity proves the assertion for
signed forms. This decomposition is fixed in $j$ and $t$.
Finally, energy is affine:
$E(r_{j,t})/t=E(w)/t+E_\alpha(\psi_j)$.
Strong energy convergence and (5) give the second limit.
No estimate depending on a time-varying $d_1$ ball or an unnormalized
relative $J$ is used.
\end{proof}

\section{The new maximal-branch entropy theorem}
\begin{theorem}[Joint entropy recovery with the actual start retained]
\label{entropy}
Fix the general smooth compact K\"ahler manifold and conventions
of Section 2. Let $w\in\mathcal E^1$ satisfy $H(w)<\infty$.
Suppose $\psi_j\to\psi$ strongly in
$\mathcal E^{1,\NA}(\alpha)$, with $H_\alpha(\psi_j)<\infty$.
Set $r_j=r(w,\psi_j)$ and $r=r(w,\psi)$.
\begin{enumerate}
\item If $H_\alpha(\psi)<\infty$ and
$H_\alpha(\psi_j)\to H_\alpha(\psi)$, then for every joint
$j\to\infty$, $t_j\to\infty$,
\[
 \frac{H(r_{j,t_j})}{t_j}\longrightarrow H_\alpha(\psi).
 \tag{9}
\]
Equivalently, for every $\epsilon>0$ there exist $J,T$ such that
$|H(r_{j,t})/t-H_\alpha(\psi)|<\epsilon$ for all $j\ge J,t\ge T$.
\item If $H_\alpha(\psi)=+\infty$, then every joint sequence
satisfies $H(r_{j,t_j})/t_j\to+\infty$, without an additional
assumption on $H_\alpha(\psi_j)$'s limit.
\end{enumerate}
In both cases energy recession is recovered jointly, and
$r_{j,t}\to r_t$ in $d_1$ uniformly on bounded time intervals.
The start is exactly $w$, including when it is unbounded and nonmodel.
\end{theorem}
\begin{proof}
For each $j$, grant R gives finite entropy at every finite time,
the entropy recession $H_\alpha(\psi_j)$, and calibrated
cohomological recession $G_\alpha(\psi_j)$.
Thus $f_j(t):=M(r_{j,t})$ is finite convex and has finite slope
\[
 m_j=H_\alpha(\psi_j)+G_\alpha(\psi_j),\qquad f_j(0)=M(w)<\infty.
 \tag{10}
\]
At fixed $T$, bounded-time recovery and lower semicontinuity give
\[
 M(r_T)\le\liminf_j M(r_{j,T}).                         \tag{11}
\]
In the finite branch, R gives finite-time entropy for $r$ and
$\lim_{t\to\infty}M(r_t)/t
=m:=H_\alpha(\psi)+G_\alpha(\psi)$.
Entropy recovery and strong mixed-slope continuity give $m_j\to m$.
Apply Lemma \ref{convex} to (10)--(11). This proves the joint limit
of $M(r_{j,t_j})/t_j$. Subtract the independent joint limit (8).
The result is (9), with entropy coefficient one.

In the infinite branch, R's entropy classification and finite
cohomological recession give $M(r_t)/t\to+\infty$ as an extended
limit. $M(r_t)$ might be infinite at some finite times, which is
allowed in Lemma \ref{infinite}. Equation (11) and that lemma
give $M(r_{j,t_j})/t_j\to+\infty$. The joint correction (8) is
finite, so the same conclusion holds for entropy.

The energy assertion is the exact identity
\[
 \frac{E(r_{j,t_j})-E(w)}{t_j}=E_\alpha(\psi_j)\to E_\alpha(\psi).
 \tag{12}
\]
Bounded-time $d_1$ recovery is the granted R maximal-ray continuity.
The uniform-tail formulation in the finite branch is equivalent
to (9): failure would select $j_k\ge k,t_k\ge k$ violating it.
This completes the proof.
\end{proof}

\begin{proposition}[Actual model-sequence consequence]\label{models}
For every fixed actual $w\in\mathcal E^1$ with $H(w)<\infty$ and
$\psi\in\mathcal E^{1,\NA}(\alpha)$ with finite entropy,
there are actual relatively K\"ahler model data $\eta_j$ for which
the maximal rays from this unchanged $w$ have bounded-time $d_1$
recovery, energy-slope recovery and every joint entropy/time limit
in Theorem \ref{entropy}. No projectivity is assumed.
\end{proposition}
\begin{proof}
Take the exact model recovery in grant R, equation (16), retaining
its real cohomological model meaning. It gives strong convergence
and NA entropy convergence. Apply Theorem \ref{entropy}.
This application adds a joint analytic conclusion to that recovery;
it does not add a closed relative boundary theorem to R's model
construction. The model starts are not asserted to be model functions.
\end{proof}

The theorem closes the general joint-entropy gap of the specific
finite-entropy maximal recovery mechanism recorded in S, Section 5.
It does so by convexity rather than the mixed-pairing normalization
argument that S left unproved. No $O(1)$ uniform remainder is asserted.
This conclusion is separate from S's explicit radial formula, which
has the stronger uniform additive remainder in its precise scope.

\section{What the proof does not recover}
For a ray from its actual $w$, define the closed Legendre levels and
relative ceiling by
\[
 \chi_u(\lambda)=\inf_{t\ge0}(u_t-t\lambda),\qquad
 \mathscr P_w[h]=\left(\lim_{C\to\infty}P_\omega(h+C,w)\right)^*.
 \tag{13}
\]
Grant S proves recognition $\mathscr P_w[\chi_u(\lambda)]
=\chi_u(\lambda)$ whenever this is a genuine psh level. It uses
Perron comparison, not NA maximality. The case $-\infty$ is only
a placeholder convention. A ceiling against $w$ is distinct from
an absolute ceiling against zero. An I-envelope uses multiplier-ideal
data and cannot be substituted for this finer P-envelope.

For genuine levels use the raw mixed masses
\[
 M_k(h)=\frac1V\int_X\omega^{n-k}\wedge
                 \langle\omega_h^k\rangle,\qquad 1\le k\le n.
 \tag{14}
\]
No probability division by a zero mass is performed. A genuine
zero-mass level is still a potential and can have finer P data;
an identically minus-infinite placeholder has no current or
singularity metric. Only the explicit zero extension of the
positive-degree numbers (14), where stated, is used at that boundary.

The strong model sequence of Proposition \ref{models} need not be
ordered in a way controlling (13), and the argument uses only one
fixed time at a time. It supplies no interchange of an index limit
with the infimum over the entire half-line. The recognition lemma
is not a density or convergence theorem for relative ceilings.
Even when decreasing rays provide pointwise decreasing levels,
that statement alone is not a mixed nonpluripolar mass continuity
theorem at arbitrary singularities.

The grant boundaries illustrate these gaps accurately. T controls
all closed levels in its finite-height, zero-start, one-branch curve
domain. Its bad roof sequence for the trivial target diagnoses a
failed implication; the product sequence still recovers that target.
C changes an absolute zero-mass endpoint to $-\infty$ under a
finite-entropy singular starting-point change on $\mathbf P^n$,
$n\ge2$. It does not obstruct relative recovery retaining $w$.
S constructs actual rational relatively ample hyperplane blowup
models retaining one such unbounded start. Its genuine relative
endpoints descend to $-\infty$, with all positive-degree raw
mixed masses tending to zero, and its entropy estimate is joint.
That finite-dimensional radial family does not approximate arbitrary
data or arbitrary starts. The present theorem extends its general
joint-entropy mechanism, not its closed relative P-profile formula.

Finally, let $u$ be an actual nonmaximal ray from $w$ with usual
datum $\psi$, energy slope $c_u$, and
$\delta=E_\alpha(\psi)-c_u>0$. Grant R gives
\[
 d_1(r(w,\psi)_t,u_t)=t\delta.                         \tag{15}
\]
Strongly converging maximal model data in Proposition \ref{models}
converge at bounded times to $r(w,\psi)$, not $u$; energy's
$1$-Lipschitz property also gives, at each $j$,
\[
 \liminf_{t\to\infty}\frac{d_1(r(w,\eta_j)_t,u_t)}t
 \ge |E_\alpha(\eta_j)-c_u|\longrightarrow\delta.
 \tag{16}
\]
This is exactly a limitation of this maximal-ray mechanism.
It is not a proof that every permissible model or flag approximation
fails. We neither delete the arbitrary-ray branch nor manufacture a
universal obstruction from (16).

\section{Precise remaining gaps and comparison with the catalogue}
To settle the entire unchanged original P19.2, still missing here are:
\begin{enumerate}
\item A simultaneous model construction for arbitrary prescribed
finer P data and arbitrary finite-energy starts, with closed
relative levels retained on general compact K\"ahler manifolds.
\item General convergence of those actual relative ceilings and
all raw mixed masses in the required closed-level topology,
distinguishing genuine zero-mass data from $-\infty$ placeholders.
\item An approximation mechanism for arbitrary nonmaximal actual
weak rays preserving the actual ray and energy slope, rather than
replacing it by its maximalization.
\item The entropy requirements outside this finite-initial-entropy
maximal signature, including the requested fixed-time entropy
recovery. Strong $d_1$ convergence was used for lower
semicontinuity only, and proves no entropy continuity.
\item Residual log-discrepancy-model regularization in the required
generality and with the additional P data, with actual positivity
proved and no unjustified relative semiampleness assumption.
\end{enumerate}
The catalogue's published/source-stated smooth polarized special
Fujita regimes and the assignment's zero-start polarized
log-discrepancy-model recovery remain established subcases.
They do not supply the missing items by description alone.
Our reliance on the caller R grant allows a general smooth compact
K\"ahler maximal theorem without replacing the class by a polarization.
It does not resolve the original residual scope. P19.1 is granted,
and P19.3/P19.4 remain separate future targets; none is claimed here.
No rigorous full-scope analytic counterexample has been obtained.
Accordingly the requested completion flag is \texttt{candidate=false}.

\appendix
\section{Literal source coordinates and reproducible record}
The full supplied bodies were read in the input and extracted exactly
from its assignment; their literal coordinates in this run are
line numbers in the extracted files. The applications of R are
its Section 3 calibrated mixed slopes, equation (16), Sections 6--9
maximal-ray continuity, entropy classification and defect.
The relevant explicit assertions occur at local R lines 199--201,
467--507, 511--543 and 551--654. S's fixed-start recovery and
mechanism limitations are local S lines 459--507. These are fresh
local coordinates and are distinct from historical source layouts.

The primary BDL source is the published 44-page PDF,
Geometry \& Topology 21 (2017), 2945--2988, DOI
10.2140/gt.2017.21.2945, at the URL in the bibliography.
Returned layout lines were retained verbatim in JSON source records.
The complete units used here are Proposition 4.4 statement/proof
1852--1938 (context and product identification 1778--1948),
Proposition 4.5 statement/proof 2004--2085, and Theorem 4.7
statement/proof 2165--2307. Twist condition (3) was read at
490--506; untwisted and contracted conventions at 79--127,
1784--1834 and 508--532. The source ledger lists all returned
ranges, rather than claiming to have read the entire PDF.
The new applications use only smooth forms, twist zero and $p=1$;
their recursive pluripotential foundations are supplied by the
explicit caller R grant where invoked. There is no new application
to singular twisting currents or a degenerating family.

The native input SHA256 is
\begin{center}\small\texttt{6c5215d5d5a93a37fd3c786246f832218}\\
\texttt{e158d9be2e7b6fddcc711b5213a93f7}.
\end{center}
The original and frozen copy are byte-identical (157756 bytes).
The exact task is in \path{task-original.json}, the exact assignment
in \path{assignment-original.txt}, and the full grants in
\path{supplied/}. The source-application ledger is
\path{source-applications.json}; gaps are in
\path{remaining-gaps.json}; environment details in
\path{environment.json}. This paper is \path{paper.tex},
with compiled \path{paper.pdf} and build logs.
From this directory rerun:
\begin{verbatim}
python prepare_input.py
python create_ledger.py
python check_recession.py
python build_paper.py
python validate_deliverables.py
\end{verbatim}
The check program exhaustively verifies finitely many rational chord
inequalities and model identities, and displays scalar limitations.
Its scalar examples are not analytic counterexamples to P19.2.
Arithmetic and compilation do not certify any analytic proof.
Public primary retrieval was read through the available web tool;
a direct local curl failed because its proxy connection was unavailable.
That failure, the successful returned reading record, and exact URLs
are retained. No agents or campaigns were launched; no other campaign,
credentials, account, authentication, or runtime configuration was
accessed or changed. No operator-provided relevant supervised compute
service was exposed, and no heavy computation was needed or launched.

\begin{thebibliography}{9}
\bibitem{R} Caller grant R, complete supplied mathematical body,
\emph{Entropy slopes of finite-energy K\"ahler rays: calibration,
recovery, and arbitrary starting points}, 6 October 2026.
\bibitem{T} Caller grant T, complete supplied mathematical body,
\emph{Preserving the closed singularity profile in actual toric
model approximation}, 6 October 2026; exact zero-start curve scope.
\bibitem{C} Caller grant C, complete supplied mathematical body,
\emph{A finite-entropy initial singularity can erase an absolute
zero-mass endpoint}, 6 October 2026; $\mathbf P^n$, $n\ge2$.
\bibitem{S} Caller grant S, complete supplied mathematical body,
\emph{Retaining a singular start in model approximation:
relative P ceilings and an explicit collapsing boundary},
6 October 2026; explicit radial scope and general stated lemmas.
\bibitem{BDL} R. Berman, T. Darvas and C. H. Lu,
\emph{Convexity of the extended K-energy and the large time behavior
of the weak Calabi flow}, Geometry \& Topology 21 (2017), 2945--2988,
\href{https://msp.org/gt/2017/21-5/gt-v21-n5-p08-s.pdf}{published primary PDF},
Propositions 4.4--4.5 and Theorem 4.7.
\end{thebibliography}
\end{document}


# Author source application ledger, proof data only

{
  "status": "PARTIAL; candidate=false; unverified draft",
  "grant_policy": "Only complete caller bodies R, T, C, S within their exact stated mathematical scopes. Historical verdicts, hashes and S source ledger are not independent premises.",
  "supplied": [
    {
      "id": "R",
      "file": "supplied/R.tex",
      "version": "Complete supplied body dated 6 October 2026",
      "read_scope": "Entire complete body read in the input and extracted verbatim.",
      "mathematical_premises": [
        "Connected smooth compact Kahler X, n>=1, any Kahler class, actual finite-energy weak rays strongly continuous at zero.",
        "Actual usual datum on full supported-semivaluation carrier; maximal rays from any actual w in E1; order, energy affinity E(r(w,psi)_t)=E(w)+t E_alpha(psi).",
        "Entropy slope H_infty=H_alpha for maximal rays with a finite-entropy slice; nonmaximal rays have infinite entropy slope.",
        "Calibrated fixed smooth cohomological contracted-energy slopes are finite, independent of w, and strongly continuous in usual NA datum.",
        "Strong NA recovery by actual relatively Kahler model data with converging entropy when target H_alpha is finite.",
        "Bounded-time d1 continuity of maximal-ray construction for strong NA data; finite-energy geodesic comparison/decreasing continuity and energy foundations.",
        "For finite H(w) and finite H_alpha(psi), finite-time entropy is finite; extended Mabuchi convexity and supporting energy identities."
      ],
      "literal_local_coordinates": {
        "mixed_slopes": [
          194,
          242
        ],
        "model_recovery": [
          461,
          478
        ],
        "joint_bounded_time": [
          480,
          509
        ],
        "finite_entropy": [
          511,
          543
        ],
        "arbitrary_ray_defect_and_slope": [
          551,
          654
        ]
      },
      "not_supplied": [
        "Arbitrary finer P-profile model density",
        "Nonmaximal model approximation",
        "Fixed-time entropy continuity under strong convergence",
        "Universal nonexistence"
      ]
    },
    {
      "id": "T",
      "file": "supplied/T.tex",
      "version": "Complete supplied body dated 6 October 2026",
      "read_scope": "Entire complete body in input.",
      "exact_scope": "Zero-start one-branch P1 O(1), finite-height decreasing convex roofs; actual relatively ample rational models, all closed P levels and uniform entropy remainder.",
      "application": "Scope comparison only; its bad roof diagnostic is not a universal obstruction.",
      "excluded": [
        "Arbitrary singular start",
        "General Kahler classes",
        "Arbitrary nonmaximal rays"
      ]
    },
    {
      "id": "C",
      "file": "supplied/C.tex",
      "version": "Complete supplied body dated 6 October 2026",
      "read_scope": "Entire complete body in input.",
      "exact_scope": "CPn n>=2 radial full-mass finite-energy finite-entropy singular start, actual bounded nef hyperplane blowup datum, absolute endpoint change to identically minus infinite.",
      "application": "Scope comparison and distinction between genuine zero-mass level and placeholder.",
      "excluded": [
        "Obstruction to relative recovery retaining w",
        "Universal model nonexistence"
      ]
    },
    {
      "id": "S",
      "file": "supplied/S.md",
      "version": "Complete supplied body with the three caller clarifications, dated 6 October 2026",
      "read_scope": "Entire complete body in input.",
      "exact_scope": "General genuine-level relative-ceiling lemma; CPn n>=2 explicit relatively ample rational hyperplane blowup models retaining the one unbounded radial finite-H start; closed relative levels, raw mixed masses and uniform joint entropy; general maximal recovery/mechanism limit.",
      "application": "Identify the fixed-start mechanism strengthened by the new convex argument, retain correct boundary/scope distinctions.",
      "literal_local_coordinates": {
        "relative_lemma": [
          94,
          132
        ],
        "general_mechanism": [
          460,
          507
        ],
        "original_gaps": [
          608,
          637
        ]
      },
      "excluded": [
        "Arbitrary relative-profile model density",
        "General all-ray conclusion",
        "Grant expansion from the historical source ledger"
      ]
    }
  ],
  "primary": [
    {
      "id": "BDL",
      "url": "https://msp.org/gt/2017/21-5/gt-v21-n5-p08-s.pdf",
      "version": "Published Geometry & Topology 21 (2017) 2945-2988; DOI 10.2140/gt.2017.21.2945; publication 15 August 2017; 44 PDF pages.",
      "essential": true,
      "exact_applications": [
        {
          "unit": "Proposition 4.4",
          "statement": "For a smooth closed real (1,1) form gamma, AM_gamma extends via decreasing approximation to a d1-continuous functional E1 -> R, bounded on d1-bounded subsets.",
          "full_statement_proof_layout": [
            1852,
            1938
          ],
          "context_and_product_identification": [
            1778,
            1948
          ],
          "domain_check": "Our X is connected smooth compact Kahler and every slice is in E1. gamma is smooth closed; no projectivity."
        },
        {
          "unit": "Proposition 4.5, only smooth positive twisting form",
          "statement": "For smooth closed positive gamma (taking beta=gamma,f=0 in condition (3)), AM_gamma is convex along bounded-Laplacian weak geodesic segments.",
          "full_statement_proof_layout": [
            2004,
            2085
          ],
          "domain_check": "Used for smooth endpoint approximants. Extension to finite-energy segments is proved in the paper using granted R decreasing geodesics and Proposition 4.4. The bounded source statement is not silently applied to unbounded endpoints."
        },
        {
          "unit": "Theorem 4.7, twist zero and p=1",
          "statement": "The formula for extended untwisted Mabuchi is the greatest d1-lower-semicontinuous extension to E1, and it is convex along finite-energy E1 geodesics.",
          "full_statement_proof_layout": [
            2165,
            2307
          ],
          "domain_check": "Twist zero satisfies (3) with beta=0,f=0. Only lower semicontinuity/convexity is used; no entropy continuity asserted."
        }
      ],
      "literal_convention_units": [
        [
          79,
          127
        ],
        [
          490,
          506
        ],
        [
          508,
          532
        ],
        [
          1784,
          1834
        ]
      ],
      "coordinate_conversion": "BDL potential v=u/(2pi), same omega. Currents/probability measures coincide; d1_BDL=d1/(2pi), AM(v)=E(u)/(2pi), T_gamma(u)=2pi*n*AM_gamma(v). Ric_BDL=2pi Ric, scalar_BDL=2pi scalar, so K_BDL(v)=H(u)+T_{-Ric}(u)+scalar*E(u) exactly.",
      "records": [
        "sources/bdl-open.json",
        "sources/bdl-find.json",
        "sources/bdl-units-1.json",
        "sources/bdl-units-2.json"
      ],
      "returned_layout_ranges": {
        "bdl-open.json": [
          [
            0,
            423
          ]
        ],
        "bdl-units-2.json": [
          [
            490,
            590
          ],
          [
            2003,
            2189
          ],
          [
            2207,
            2415
          ]
        ],
        "bdl-find.json": [
          [
            229,
            234
          ],
          [
            837,
            858
          ],
          [
            1533,
            1546
          ],
          [
            1590,
            1603
          ],
          [
            1639,
            1651
          ],
          [
            1723,
            1764
          ],
          [
            2003,
            2030
          ],
          [
            2055,
            2085
          ],
          [
            2145,
            2153
          ],
          [
            2223,
            2320
          ],
          [
            2394,
            2440
          ],
          [
            2446,
            2451
          ],
          [
            2569,
            2581
          ],
          [
            2810,
            2821
          ],
          [
            2837,
            2844
          ],
          [
            2851,
            2870
          ]
        ],
        "bdl-units-1.json": [
          [
            1723,
            2054
          ],
          [
            2086,
            2090
          ],
          [
            2125,
            2269
          ]
        ]
      },
      "not_claimed": "No complete recursive primary reproof or whole-PDF reading; ordinary finite-energy background is the explicit caller R premise where invoked. No singular-current or family application."
    }
  ],
  "new_proofs": [
    "Convex chord recovery with one-sided fixed-time lower convergence and converging finite recession slopes.",
    "Extended infinite-recession joint lower recovery, including a target infinite at a fixed finite time.",
    "Joint contracted-energy recovery by splitting a fixed signed smooth form into two positive forms and applying convex recovery.",
    "Joint entropy/time recovery by applying convex recovery to Mabuchi and subtracting the independently recovered cohomological correction.",
    "Actual fixed-w model-sequence consequence using only the exact granted R model recovery."
  ],
  "negative_conclusions": [
    "No fixed-time entropy convergence",
    "No closed relative P-profile model construction",
    "No arbitrary nonmaximal-ray approximation",
    "No full-scope counterexample",
    "Full original P19.2 remains unresolved"
  ],
  "verification_boundary": "Compilation and small exhaustive rational checks do not certify analytic correctness."
}


BEGIN COMPLETE MATHEMATICAL GRANT R exact original P19.1
\documentclass[11pt]{article}
\usepackage[a4paper,margin=26mm]{geometry}
\usepackage{amsmath,amssymb,amsthm,hyperref}
\newcommand{\MA}{\operatorname{MA}}
\newcommand{\NA}{\mathrm{NA}}
\newcommand{\Ent}{\operatorname{Ent}}
\newcommand{\Ric}{\operatorname{Ric}}
\newcommand{\PSH}{\operatorname{PSH}}
\newcommand{\Vol}{\operatorname{Vol}}
\newcommand{\J}{\mathcal J}
\newcommand{\Jac}{\operatorname{Jac}}
\newcommand{\ord}{\operatorname{ord}}
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\title{Entropy slopes of finite-energy K\"ahler rays:\\
calibration, recovery, and arbitrary starting points}
\author{}
\date{6 October 2026}
\begin{document}
\maketitle
\begin{abstract}
This paper classifies entropy slopes of actual finite-energy weak
geodesic rays on a smooth compact K\"ahler manifold. It uses squared-log
time and divisor coefficients consistently. The finite branch
is the non-Archimedean entropy for a maximal ray having a finite-entropy
slice. Other rays have infinite slope. A stationary bounded potential
with singular Monge--Amp\`ere measure explains why a condition on slices
is necessary even for maximal rays. The new steps are a calibrated
log-canonical volume argument, a direct entropy bound for model rays,
special-Fujita entropy recovery with a local discrepancy repair, and
joint continuity in the initial potential and the usual datum.
The complete original P19.1 statement and its source applications
passed independent Xean native Codex review134 with gpt-6.1-sol
and xhigh reasoning. The proof concerns P19.1; the other three
residual hybrid targets are separate.
\end{abstract}

\section{The statement and its conventions}
Let $X$ be a connected smooth compact K\"ahler manifold of dimension
$n\geq1$, let $\omega$ be a K\"ahler form, and put
$\alpha=[\omega]$, $V=\int_X\omega^n$, and $\mu_0=\omega^n/V$.
Throughout this paper
\[
 dd^c=\frac{i}{2\pi}\partial\bar\partial,
 \qquad t=-\log|\tau|^2,
 \qquad dd^c\log|f|^2=[\operatorname{div}(f)].                 \tag{1}
\]
Use the entire finite-energy extension of
\[
 E(u)=\frac1{(n+1)V}\sum_{j=0}^n
          \int_Xu\,\omega_u^j\wedge\omega^{n-j},\qquad
 \MA(u)=\omega_u^n/V,\qquad \omega_u=\omega+dd^cu.
\]
Thus $E(0)=0$ and $E(u+c)=E(u)+c$. Set
$H(u)=\Ent(\MA(u)\mid\mu_0)$, using full probability entropy:
$H=\int\rho\log\rho\,d\mu_0$ for $\MA(u)=\rho\mu_0$,
and $H=+\infty$ otherwise. Changing the smooth positive reference
probability changes $H$ by a uniformly bounded term.

An actual weak ray $u:[0,\infty)\to\mathcal E^1(\omega)$ is strongly
continuous also at zero; on each finite interval it is the canonical
pluripotential weak geodesic. In particular it has affine energy and
linear upper growth. Its total potential is
$U(x,\tau)=u_{-\log|\tau|^2}(x)$ on $X\times\Delta^*$.

Its usual non-Archimedean datum is taken from generic divisorial
coefficients of this actual total potential. Specifically, for a
vertical Gauss divisor $F$ with $b_F=\ord_F(\tau)$, its value is minus
the coefficient of $U$ in the logarithm-square convention, divided by
$b_F$. Addition of an affine function of time is first allowed
to make $U$ locally bounded
above. Restore the same shift in the datum afterwards. Divisorial
determination extends this prescription to the compact analytic
semivaluation space $X^\beth$; supports of semivaluations are retained.
For a vertical real divisor $D$ on a dominating equivariant model it is
the familiar function
$f_D(v_F)=\ord_F(D)/b_F$, with compatibility
$U+\log|s_D|^2=O(1)$.

Write $\MA_\alpha(\phi)$ for the probability non-Archimedean operator
and
\[
 H_\alpha(\phi)=\int_{X^\beth}A_X\,\MA_\alpha(\phi),
 \qquad A_X(v_{\rm triv})=0.
\]
Maximality always refers to the usual datum and the specified actual
initial potential: the maximal ray dominates every ray with smaller
datum and smaller initial potential.

\begin{theorem}[Original P19.1 entropy classification]
For every actual weak ray as above its usual datum
$\phi$ belongs to $\mathcal E^{1,\NA}(\alpha)$. The extended limit
$H^\infty(u)=\lim_{t\to\infty}H(u_t)/t$ exists, and
\[
 H^\infty(u)=
 \begin{cases}
 H_\alpha(\phi),&u\text{ is maximal and some }H(u_{t_0})<\infty,
                    \quad t_0\geq0,\\
 +\infty,&\text{otherwise}.
 \end{cases}                                                \tag{2}
\]
There is no projectivity, rationality, automorphism restriction, or
smoothness requirement on $u_0$. In particular every ray from a smooth
potential has the stated maximal/nonmaximal dichotomy.
\end{theorem}
If the first branch has $H_\alpha(\phi)=+\infty$, its value in (2) is
also $+\infty$. Thus the distinction of branches concerns the proof
and the possible finite value, rather than a claim that maximality
implies finite entropy.

\section{Precise external foundations}
The following fixed-manifold theorems are the external inputs. They
are stated as mathematical results, not granted by a historical verdict.
Their original proof chains and the source applications were checked
in the complete independent review; the precise mathematical
hypotheses remain part of each application.
\begin{enumerate}
\item Mesquita--Piccione--Witt Nystr\"om [MPWN], in a smooth compact
K\"ahler class, give the probability Calabi--Yau homeomorphism on
$\mathcal E^{1,\NA}$, its supporting energy inequalities, divisorial
determination, and strong topology. Their Lemma5.0.5 gives
$\int|\phi_j-\phi|\MA_\alpha(\psi)\to0$ for each fixed finite-energy
$\psi$ when $\phi_j\to\phi$ weakly with bounded $J$.
Their Theorem5.2.2 identifies strong convergence by the normalized
energy quasi-distance. Their Propositions9.1.3 and9.1.5 give the
positive-product entropy and volume-energy formulas used in Section5.
The constructive Theorem9.2.1 gives strong and entropy recovery by
envelopes $P_\alpha(f_j)$ of PL obstacles, not yet by relatively
K\"ahler model potentials.
\item Mesquita--Piccione [MP], Theorems5.1.4 and5.1.7, give the usual
datum, its psh extension, and the order-preserving maximal ray from
every $w\in\mathcal E^1(\omega)$. The energy slope of a maximal ray is
its non-Archimedean energy. The mixed pairing estimate in Lemma5.3.2
and the approximation proof of Theorem5.3.4 supply the singular mixed
slope argument reconstructed with (1) in Section3. We do not import
an uncalibrated printed entropy coefficient.
\item Trusiani [T], TheoremB, Lemmas3.4--3.5 and Section5, give
vertical equivariant special K\"ahler Fujita approximation on a smooth
dominating big configuration. Its precise conclusions are listed in
Section5. Its analytic Rees discrepancy input is supplied instead by
the complete local proof in AppendixA. The ordinary regularization,
uniform positivity estimates, and positive-product orthogonality
remain the other stated analytic foundations of that construction.
TheoremA's automorphism assumption does not occur in this input.
\item Sj\"ostr\"om Dyrefelt [SD], Lemma4.6, constructs the actual
model weak ray from any smooth initial potential, with locally bounded
complex Hessian after removal of its compatible divisor. We use this
regularity statement, not its printed time-dependent slope constant.
Section4 proves the model entropy slope directly.
\item Berman--Darvas--Lu [BDL], Lemma3.1 and Theorems4.7/1.2,
give smooth $d_1$ approximation with converging entropy, and the
$d_1$ lower semicontinuous geodesically convex extended Mabuchi
functional. Darvas [D], Theorem5.5 with the $L^1$ weight, gives
$I_1(a,b)\leq C d_1(a,b)$, where
$I_1(a,b)=\int|a-b|(\MA(a)+\MA(b))$.
The supporting inequalities, ordered $d_1$ identity, energy affinity,
mutual finite-energy integrability and decreasing energy continuity
are used in their usual finite-energy compact-K\"ahler domains.
\item The local equisingularity input in Li [L], Lemma3.1, says that
for a ray and its maximalization with the same datum,
$\exp(b(\widehat U-U))$ is locally integrable near the central fiber
for every $b>0$. Its proof uses the valuative description of analytic
multiplier ideals and local Bergman regularization from
Ohsawa--Takegoshi, rather than a polarized positivity assumption.
The precise compact-K\"ahler transport is [MP], Proposition6.3.1.
Section8 describes this local application and then gives the complete
entropy/energy argument; it does not assume the desired dichotomy.
\end{enumerate}
In [BDL] and [D] the operator is $i\partial\bar\partial$.
Taking their potential to be $u/(2\pi)$ with background $\omega$
identifies currents and probability measures; energy and $d_1$ scale
by $1/(2\pi)$. Their Ricci form is $2\pi\Ric(\omega)$, so their
contracted-energy expression becomes exactly the functional in (12)
below. This checks entropy approximation, convexity and lower
semicontinuity without changing the full probability entropy.

\section{Calibrated mixed slopes and log-canonical test volumes}
On a smooth SNC dominating model $\rho:\mathcal Y\to X\times\mathbf P^1$
write $B=\sum b_iE_i$ and
\[
 C_{\mathcal Y}=K_{\mathcal Y/(X\times\mathbf P^1)}+B_{\rm red}-B.
                                                               \tag{3}
\]
The associated PL test is
$f_C=A_X\circ r_{\mathcal Y}$, since at a vertical Gauss component
its value is $(a_i+1-b_i)/b_i$. These are Gauss components on
equivariant models; no assertion about an arbitrary nonequivariant
restriction of a total-space divisor is needed.

\begin{lemma}[Calibrated model test pairing]
If $r$ is a maximal finite-energy ray from any finite-energy initial
potential and $\Psi$ is smoothly compatible with a real vertical
divisor $C$ in convention (1), then
\[
 \lim_{t\to\infty}\frac1t\int_X\Psi_t\MA(r_t)
     =\int_{X^\beth} f_C\MA_\alpha(\phi).                 \tag{4}
\]
The corresponding calibrated energy and twisted-energy slopes hold,
and are strongly continuous functions of $\phi$ for fixed smooth
cohomological inputs.
\end{lemma}
\begin{proof}
First consider smoothly compatible weights on one smooth compact
model. Remove their vertical divisors to obtain smooth representatives
of the total classes $\rho_X^*\alpha_i+D_i$. On a punctured fiber,
integration by parts gives the usual Deligne mixed pairing identity:
its base $dd^c$ is the pushforward of the product of these smooth
representatives. Integrate on $\mathbf P^1$ minus a disk of radius
$r$, using metrics constant near infinity. In (1) the boundary flux
is exactly the derivative in $t=-\log r^2$. Indeed
$dd^cF=(4\pi)^{-1}\Delta F\,dA$, and the inner boundary flux is
$-rF_r/2=F_t$. The integral tends to the intersection of the total
classes. Thus the slope equals that intersection, with no factor two.
Multilinearity gives (4) for model weights.

For singular maximal slots take decreasing relatively K\"ahler
model data $\phi_m\searrow\phi$ and decreasing smooth initial
potentials $w_m\searrow w$. Order gives $r_m\geq r$ and
\[
 d_1(r_{m,t},r_t)=E(w_m)-E(w)
                      +t\{E_\alpha(\phi_m)-E_\alpha(\phi)\}.
                                                               \tag{5}
\]
The mixed energy estimate of [MP], Lemma5.3.2, bounds a pairing
difference by a constant times $d_1(r_{m,t},r_t)^q$ times the
remaining $J$ bounds to power $1-q$, where $q=2^{-n}>0$.
The $J$ bounds are $O(t+1)$ uniformly on this decreasing tail.
Divide by $t$, take the time limit first, and then let $m$ increase.
Equation (5) and decreasing energy continuity make the error zero.
Replace the singular slots one at a time and use polarization.
Fixed signed smooth forms and PL tests are differences of positive
model inputs on a common dominating model; the pairing and estimate
are multilinear. The fixed model representation and initial constants
do not change this limiting argument. This is precisely the singular
approximation argument in [MP], with its model boundary constant
calibrated above. Strong continuity of the resulting non-Archimedean
pairings is the finite-energy mixed-pairing continuity in [MPWN].

An additional dictionary checks the same calibration: [MP] uses
$dd^c_L=i\partial\bar\partial/\pi$, logarithm weights and
$s=-\log|\tau|$. Use its background $2\omega$ and the same potential
$u_{2s}$. Its currents are twice ours and its datum is $2\phi$ in
class $2\alpha$. Probability measures are unchanged, and its test
datum is $2f_C$. Normalized mixed slopes are doubled in $s$;
division by $t=2s$ cancels the factor. We use this dictionary only for
the mixed pairing, not to import a printed Mabuchi entropy coefficient.
\end{proof}

\begin{lemma}[Log-canonical fiber volume]
There is a smooth positive fiber volume $\mu_{\mathcal Y,t}$ on the
generic fiber such that, for
$\Psi_t=\log(\mu_{\mathcal Y,t}/\mu_0)$,
$\Psi+\log|s_{C_{\mathcal Y}}|^2$ extends smoothly on the model and
\[
 \int_X\mu_{\mathcal Y,t}\leq C(1+t)^n\qquad(t\geq1).       \tag{6}
\]
If $\Omega$ is a fixed smooth positive form on the model, then
$\Omega|_{\mathcal Y_t}^n\leq C'\mu_{\mathcal Y,t}$ for small
nonzero $\tau$.
\end{lemma}
\begin{proof}
Put $L_{\log}=K_{\mathcal Y/\mathbf P^1}+B_{\rm red}-B$ and
equip it with a smooth Hermitian metric. On a noncentral fiber it is
the canonical bundle, and the metric defines the stated fiber volume.
Here is both the compatibility and the growth calculation.
Near a central SNC stratum choose coordinates with
$\tau=z_0^{b_0}\cdots z_p^{b_p}$; absorb a nowhere zero unit into
one coordinate. A relative canonical frame, choosing $z_0$ as the
dependent coordinate, is
$z_0\,dz_1\wedge\cdots\wedge dz_n/(b_0\tau)$.
Multiplication by the local equation of $B-B_{\rm red}$ gives the
log-canonical frame
\[
 \sigma_{\log}=b_0^{-1}
      \frac{dz_1}{z_1}\wedge\cdots\wedge\frac{dz_p}{z_p}
                    \wedge dz_{p+1}\wedge\cdots\wedge dz_n.
                                                               \tag{7}
\]
Our fiber volume is comparable to $|\sigma_{\log}|^2$, with smooth
positive factors bounded above and below on a smaller chart.
The pullback of the base fiber volume form has coefficient
$s_C$ against this frame, of order $a_i+1-b_i$ on $E_i$.
Therefore its ratio gives
$\Psi=-\log|s_C|^2+$ a smooth function, as asserted.

For the integral put $y_i=-\log|z_i|^2$. After choosing bounded
polydisks and shifting fixed constants, $y_i\geq0$ and
$\sum_{i=1}^p b_i y_i\leq t+O(1)$. In these independent variables
the radial logarithmic volume in (7) is a constant times
$dy_1\cdots dy_p$, with compact angular and free-coordinate factors.
There are only finitely many branches for $z_0$. Its integral is
$O((1+t)^p)$, and $p\leq n$. A finite cover of the central fiber
and a partition of unity prove (6). No reduced-fiber replacement
of the multiplicities $b_i$ was made.

Finally, on a fiber
$dz_0=-z_0\sum_{i=1}^p(b_i/b_0)dz_i/z_i$.
Wedges of $n$ ambient coordinate differentials, expressed against
(7), have bounded coefficients: each contains the requisite products
of $z_i$, or the bounded factor $z_0$ if it uses $dz_0$.
A smooth ambient metric has bounded coefficients in these coordinates,
so its top fiber volume is at most a fixed multiple of (7).
The same finite cover proves the last claim.
\end{proof}

\begin{proposition}[Entropy lower bound for maximal rays]
For every maximal ray, from any finite-energy initial potential,
\[
 \liminf_{t\to\infty}H(r_t)/t\geq H_\alpha(\phi).          \tag{8}
\]
\end{proposition}
\begin{proof}
For a fixed SNC model its $\Psi_t$ is smooth and bounded on each
fixed noncentral fiber. Entropy duality gives
\[
 H(r_t)\geq\int_X\Psi_t\MA(r_t)
                  -\log\int_Xe^{\Psi_t}\,d\mu_0.
\]
Equations (4) and (6) yield the lower bound by
$\int(A_X\circ r_{\mathcal Y})\MA_\alpha(\phi)$.
Take the supremum over the dominating SNC models. The discrepancy
integrals increase to
\[
 \int_{X^\beth}A_X\MA_\alpha(\phi),
\]
by the retraction definition and monotone integral theorem
in [MP]. This proves (8), including the value $+\infty$.
\end{proof}

\section{A direct entropy slope for actual model rays}
Let $\eta=f_D$ be the potential of a smooth relatively K\"ahler
configuration and let $r$ be its actual ray from a smooth potential.
Resolve further if necessary so that the central support is SNC;
pullback retains locally bounded complex Hessian. [SD], Lemma4.6,
states that after removal of $-\log|s_D|^2$ the total ray has this
regularity. Thus on this one compact model, for a smooth K\"ahler
form $\Omega$, its positive residual current satisfies
$0\leq T\leq C\Omega$ almost everywhere near the central fiber.
On each punctured fiber its Bedford--Taylor measure consequently obeys
\[
 \MA(r_t)\leq C_1\Omega_t^n\leq C_2\mu_{\mathcal Y,t}.     \tag{9}
\]
For clarity, this determinant domination follows by local convolution
of a potential with bounded Hessian, identification of its almost
everywhere determinant, and Bedford--Taylor continuity. Constants
depend on this fixed model and initial potential, which suffices here.
Writing $g_t=\MA(r_t)/\mu_{\mathcal Y,t}$ gives $0\leq g_t\leq C_2$.
The negative part of $g_t\log g_t$ is integrable by (6), so
\[
 H(r_t)=\int_X\log g_t\MA(r_t)+\int_X\Psi_t\MA(r_t)
       \leq\log C_2+\int_X\Psi_t\MA(r_t).                 \tag{10}
\]
For each fixed $t$ both densities are relative to smooth positive
volumes; the decomposition is valid with the usual zero-density
convention. Equations (4), (8) and (10) prove the calibrated identity
\[
 H^\infty(r)=H_\alpha(\eta).                               \tag{11}
\]
This proves the model result without a printed uncalibrated slope
formula and retains all nonreduced central multiplicities.

Define the cohomological Mabuchi expression
\[
 M(u)=H(u)+G(u),\quad
 G=T_{-\Ric(\omega)}+\overline S E,\quad
 T_\chi(u)=\frac1V\sum_{j=0}^{n-1}
  \int_Xu\,\chi\wedge\omega_u^j\wedge\omega^{n-1-j},       \tag{12}
\]
where $\Ric=-dd^c\log\omega^n$ and
$\overline S=n\int\Ric\wedge\omega^{n-1}/V$.
Differentiation of the entropy gives
$\dot H=nV^{-1}\int\dot u(\Ric\omega-\Ric\omega_u)
\wedge\omega_u^{n-1}$; differentiation of $T_\chi$ gives the
same pairing with $n\chi$. This fixes its entropy coefficient as one.
Let $G_\alpha$ be its non-Archimedean mixed pairing expression.
The calibrated mixed lemma gives
$G^\infty(r)=G_\alpha(\eta)$, so (11) implies
$M^\infty(r)=H_\alpha(\eta)+G_\alpha(\eta)$.

\section{Special Fujita approximation and entropy recovery}
Fix an SNC model $\mathcal X$ and a PL obstacle $f_D\geq1$ such that
$\Gamma=\rho_X^*\alpha+D$ is big, and put $\psi=P_\alpha(f_D)$.
The exact special-Fujita data from [T], TheoremB, Lemmas3.4--3.5
and its vertical construction in Section5 are smooth equivariant
modifications $p_k:\mathcal Y_k\to\mathcal X$ and effective vertical
real divisors $E_k$ with
\[
 \beta_k=p_k^*\Gamma-E_k\text{ K\"ahler},\quad
 \beta_k^{n+1}\to\Vol(\Gamma),\quad
 \beta_k^nK_{\mathcal Y_k/\mathcal X}\to0,\quad
 \beta_k^np_k^*\xi\to\langle\Gamma^n\rangle\xi            \tag{13}
\]
for each fixed smooth real closed $(1,1)$ class $\xi$ on $\mathcal X$.
The dimension of this application is $n+1$. The canonical error in
(13) is part of specialness, and does not follow from volume
convergence alone. Central translations make the class big as required
without changing its generic fiber or its entropy.

For precision, the local estimate used in [T], Proposition4.1, is
$k_F\leq (n+1)(v_F(\mathfrak a)-v_F(\J(\mathfrak a)))$ at
the actual normalized analytic blowup of a coherent ideal on a
smooth $(n+1)$-fold. AppendixA proves this estimate locally and even
its stronger exceptional version. It replaces the companion proof's
normal-injectivity assertion. The other steps of (13) are the source's
analytic regularization with ideals
$\J(kV_\theta)\mathcal O(-k_0E)$, its uniform positivity loss,
and orthogonality followed by Lemmas3.4--3.5.
In this vertical application orthogonality of the central non-K\"ahler
locus follows by the global/restricted central product identity
[MPWN], Proposition9.1.2, and vanishing of restricted positive volume on
the non-K\"ahler locus, as specified in [T], Remark5.1.
These are exact fixed-class positive-product inputs. No preservation
of arbitrary additional complex singularity data or genuinely
degenerating family is asserted.

Let $B=\mathcal X_0$ and $B_k=p_k^*B$. Canonical transitivity gives
\[
 C_{\mathcal Y_k}=p_k^*C_{\mathcal X}+\Delta_k,\qquad
 \Delta_k=K_{\mathcal Y_k/\mathcal X}
                         +(B_k)_{\rm red}-p_k^*B_{\rm red},
 \qquad 0\leq\Delta_k\leq K_{\mathcal Y_k/\mathcal X}.    \tag{14}
\]
Here is the coefficient proof, including nonreduced $B$. A strict
transform has coefficient zero. At an exceptional prime let
$a=\ord_F K_{\mathcal Y_k/\mathcal X}$ and
$m=\ord_F p_k^*B_{\rm red}\geq1$. The coefficient is $a+1-m$.
The SNC logarithmic top form pulls back with at most one simple
normal pole: repeated $ds/s$ factors wedge to zero.
Consequently $a+1-m\geq0$. The upper bound follows from $m\geq1$.
All exceptional centers in (13) are vertical.

The approximants
$\eta_k=f_{p_k^*D-E_k}$ are actual relatively K\"ahler model
potentials. Effectivity gives $\eta_k\leq f_D$ and hence
$\eta_k\leq\psi$. The exact model/envelope formulas in [MPWN] give
\[
 E_\alpha(\eta_k)=\frac{\beta_k^{n+1}}{(n+1)V}
       \longrightarrow\frac{\Vol(\Gamma)}{(n+1)V}=E_\alpha(\psi),
 \quad
 H_\alpha(\eta_k)=\frac{\beta_k^n C_{\mathcal Y_k}}V
       \longrightarrow\frac{\langle\Gamma^n\rangle C_{\mathcal X}}V
                    =H_\alpha(\psi).                       \tag{15}
\]
Indeed positivity and (14) bound the extra entropy contribution by
$\beta_k^nK_{\mathcal Y_k/\mathcal X}\to0$; the fixed-class
convergence in (13) handles $C_{\mathcal X}$.

Ordered energy convergence implies strong convergence here. In the
convention of [MPWN],
\[
 J(a,b)=E_\alpha(a)-E_\alpha(b)
                  +\int(b-a)\MA_\alpha(a).
\]
For $b=\eta_k\leq a=\psi$,
$0\leq J(\psi,\eta_k)\leq E_\alpha(\psi)-E_\alpha(\eta_k)\to0$.
Normalize both suprema to zero, use Theorem5.2.2 and quasi-symmetry
of the energy distance, and then use (15) to restore the removed
constants. This proves unnormalized strong convergence too.

For an arbitrary $\phi\in\mathcal E^{1,\NA}(\alpha)$ with
$H_\alpha(\phi)<\infty$, [MPWN], constructive Theorem9.2.1, gives
strongly converging $\psi_j=P_\alpha(f_j)$ with
$H_\alpha(\psi_j)\to H_\alpha(\phi)$.
Represent each PL obstacle on an actual SNC dominating model;
translate it centrally to the range above and undo the translation
afterwards. Apply (15) to each $j$ and take a diagonal with strong
quasi-distance and entropy error at most $1/j$. This gives
\[
 \eta_j\in\mathcal H_\alpha,\qquad
 \eta_j\to\phi\text{ strongly},\qquad
 H_\alpha(\eta_j)\to H_\alpha(\phi).                       \tag{16}
\]
Every $\eta_j$ is an actual smooth relatively K\"ahler configuration
on the same generic fiber. The energy, all fixed divisorial values,
and entropy converge. This is a statement about the usual datum on
a fixed smooth manifold; the separate original P19.2 requirements
are not asserted in full.

\section{Joint continuity of the actual maximal-ray construction}
Suppose $\eta_j\to\phi$ strongly non-Archimedean and
$w_j\to w$ in analytic $d_1$. Put
$\lambda_j=\max(\eta_j,\phi)$ and $a_j=\max(w_j,w)$.
The full supporting inequality and [MPWN], Lemma5.0.5, give
\[
 0\leq E_\alpha(\lambda_j)-E_\alpha(\phi)
      \leq\int|\eta_j-\phi|\MA_\alpha(\phi)\to0.          \tag{17}
\]
Similarly the analytic supporting inequality and [D], Theorem5.5,
give
\[
 0\leq E(a_j)-E(w)
      \leq\int|w_j-w|\MA(w)\leq C d_1(w_j,w)\to0.        \tag{18}
\]
Let $r_j,r$ be the maximal rays of $(w_j,\eta_j),(w,\phi)$ and
$s_j$ the maximal ray of $(a_j,\lambda_j)$. Order preservation
gives $s_j\geq r_j,r$. The ordered $d_1$ identity and maximal
energy affinity then yield
\[
 \begin{split}
 d_1(r_{j,t},r_t)
 &\leq 2E(a_j)-E(w_j)-E(w)\\
 &\quad+t\{2E_\alpha(\lambda_j)
                          -E_\alpha(\eta_j)-E_\alpha(\phi)\}\to0.
 \end{split}                                                \tag{19}
\]
The convergence is uniform on bounded time intervals. This uses an
actual common upper maximal ray, and does not call the pointwise
maximum of two rays a geodesic.

\section{Maximal rays with a finite-entropy initial potential}
Let $r$ be maximal from $w$ with $H(w)<\infty$.
If $H_\alpha(\phi)=+\infty$, (8) already proves the required equality.
Otherwise choose (16), and use [BDL], Lemma3.1 with untwisted
entropy, to choose smooth $w_j$ with
$d_1(w_j,w)\to0$ and $H(w_j)\to H(w)$.
Its proof truncates the target density, smooths with converging
entropy, solves the smooth complex Monge--Amp\`ere equation, and
uses entropy compactness and uniqueness to recover $w$ up to a
constant. Thus it applies to the entire finite-entropy $\mathcal E^1$
initial domain, not just bounded potentials.

The $G$ terms in (12) are $d_1$ continuous, so
$M(w_j)\to M(w)<\infty$. The actual model rays $r_j$ from $w_j$
have the slope proved in Section4. Convexity, at each finite time,
therefore gives
\[
 M(r_{j,t})\leq M(w_j)
                   +t\{H_\alpha(\eta_j)+G_\alpha(\eta_j)\}.
\]
Use (19), lower semicontinuity, (16), and strong continuity of the
fixed mixed pairings, in that order. It follows that
\[
 M(r_t)\leq M(w)+t\{H_\alpha(\phi)+G_\alpha(\phi)\}.       \tag{20}
\]
In particular $H(r_t)$ is finite for all finite $t$, since $G(r_t)$
is finite. Divide (20) by $t$ and subtract the calibrated finite
$G$ slope in Section3. This proves
$\limsup H(r_t)/t\leq H_\alpha(\phi)$. With (8),
\[
 H^\infty(r)=H_\alpha(\phi)\quad\text{when }H(w)<\infty.   \tag{21}
\]
This argument fixes time before passing through the approximation.
It uses no assertion of entropy continuity along arbitrary strong
sequences.

\section{Arbitrary rays and nonmaximality}
For an arbitrary ray remove a sufficiently large affine function
so that $u_t\leq0$. Linear upper growth permits this without an
assumption that the supremum is affine. Entropy and measures are
unchanged. Its usual datum is psh and nonpositive.
Let $\phi^k=\max(\phi,-k)$. The maximal ray of $\phi^k$ from
the same $u_0$ dominates $u$. Hence energy affinity gives
\[
 E_\alpha(\phi^k)\geq E(u_1)-E(u_0)>-\infty.
\]
Decreasing continuity proves $\phi\in\mathcal E^{1,\NA}$.
Its maximalization $\widehat u$ from $u_0$ dominates it.
Write $c_u=E(u_1)-E(u_0)$ and
$\delta=E_\alpha(\phi)-c_u\geq0$. Ordered energy gives
\[
 d_1(\widehat u_t,u_t)=t\delta.
                                                               \tag{22}
\]
Thus $u$ is maximal exactly when $\delta=0$.

Here the datum construction is the usual multiplier-regularization
construction, not an assigned datum. In applying the proof of [MP],
Theorem5.1.4, to an unbounded datum, a fixed time cap must be
replaced by increasing caps. On a dyadic regularization degree $m$
use the flag ideal $\J(mU)+(\tau^{m^2})$; its normalized value is
$\max(-v(\J(mU))/m,-m)$ on a Gauss divisor. Subadditivity gives
dyadic decrease, and the valuation estimates for local Bergman
regularization give the actual limiting coefficients. The caps tend
to $-\infty$, so no datum below a fixed constant is discarded.
The local regularization positivity losses tend to zero; the closed
psh class and divisorial determination in [MP] give its psh extension.
This specifies the necessary cap in the imported regularization
argument without altering the intended datum.

The extended slope exists on this whole domain. Write
$E(u_t)=E(u_0)+c_u t$ after the upper normalization. For a smooth
positive $\chi\leq C\omega$ the negative-potential energy sum gives
\[
 0\leq-T_\chi(u_t)\leq C(n+1)\{-E(u_0)-c_u t\}.
\]
Positive twisted energy is convex along weak geodesics, so its slope
exists and is finite. Write any fixed smooth real closed form as a
difference of two positive forms. All the $G$ slopes are therefore
finite. If no slice has finite entropy, $H(u_t)=+\infty$ identically
and its extended slope is $+\infty$. If a slice does have finite
entropy, convexity of $M=H+G$ from that time gives its extended
asymptotic slope, even if its later values become infinite. Subtract
the finite $G$ slope to obtain the extended entropy slope.

For completeness the local input and energy argument for a nonmaximal
ray are spelled out. The total potentials $U,\widehat U$ have the
same usual divisorial singularities. Their analytic multiplier ideals
coincide: apply the valuative criterion to the invariant flag ideals
on an equivariant resolution. Precisely, Boucksom--Favre--Jonsson
[BFJ], Theorem5.5, identifies the valuative multiplier ideal with
$\J_+(U)$; the strong openness theorem of Guan--Zhou [GZ],
Theorem1.1, gives $\J_+(U)=\J(U)$. Thus equality of valuative
transforms gives equality of the ordinary analytic multiplier ideals,
with no extra openness assumption. Noncentral singularities have trivial
ideals because each slice is finite energy. Local Bergman
regularization of this common ideal supplies, for each integer $m$,
a local potential $B_m=m^{-1}\log\sum|f_i|^2$ with
$B_m\geq\widehat U-C_m/m$ after harmless smooth local backgrounds.
By definition $\sum|f_i|^2e^{-mU}$ is locally integrable. Therefore
\[
 e^{m(\widehat U-U)}
          \leq e^{C_m}\sum|f_i|^2e^{-mU}
\]
is locally integrable. On a finite cover of the compact central fiber
this proves integrability for every real $b>0$, since
$\widehat U-U\geq0$ and $m$ can be arbitrarily large.
This is the analytic-local proof of [L], Lemma3.1, as transported by
[MP], Proposition6.3.1. The inputs here are local multiplier
valuation and Bergman estimates on smooth complex manifolds; no
global algebraic line bundle or Nadel vanishing enters this argument.

Put $Z_b(t)=\int_Xe^{b(\widehat u_t-u_t)}d\mu_0$. In time (1),
the total integral near the central fiber is a constant times
$\int_T^\infty Z_b(t)e^{-t}dt<\infty$.
Thus there are $t_j\to\infty$ with $Z_b(t_j)\leq e^{t_j}$.
The measurable Gibbs inequality, with truncation if necessary, gives
\[
 \begin{split}
 H(u_{t_j})&\geq b\int_X(\widehat u_{t_j}-u_{t_j})\MA(u_{t_j})
                                      -\log Z_b(t_j)\\
 &\geq b\{E(\widehat u_{t_j})-E(u_{t_j})\}-t_j
       =(b\delta-1)t_j.
 \end{split}                                                \tag{23}
\]
The second inequality is the full energy supporting inequality.
The Gibbs inequality is valid for a measurable nonnegative test
because its bounded truncations satisfy the probability relative
entropy inequality, followed by monotone convergence; finite-energy
mutual integrability also makes the displayed supporting integral
well-defined. If $\delta>0$, existence of the extended slope and
(23) give $H^\infty(u)\geq b\delta-1$ for each $b>0$.
Letting $b$ grow proves $H^\infty(u)=+\infty$.

\section{Time shifts, infinite-entropy starts, and completion}
Suppose now that $u$ is maximal and $H(u_{t_0})<\infty$ for some
$t_0\geq0$. Its tail $v_s=u_{t_0+s}$ has the same usual datum:
rescaling the puncture coordinate by the fixed nonzero constant
$e^{-t_0/2}$ leaves all normalized generic coefficients unchanged.
Its energy slope is $c_u=E_\alpha(\phi)$. Its maximalization from
$u_{t_0}$ has that same slope, so (22) proves that this tail is
maximal. Equation (21) applied to the tail proves (2); its time
translation does not change the slope at infinity. Nonmaximal rays
were treated in (23), and rays without a finite-entropy slice were
treated before it. This completes the classification.

The slice condition cannot be removed. Here is an explicit bounded
example needing no approximation theorem. On $\mathbf P^1$ take
$\omega=dd^c\log(1+|z|^2)$ and
\[
 w(z)=\log\max(1,|z|^2)-\log(1+|z|^2).
\]
It is bounded, continuous, and $\omega$-psh. Its Monge--Amp\`ere
measure is the probability angular measure on $|z|=1$, since the
radial derivative of $\log\max(1,|z|^2)$ jumps there. It is
singular relative to $\omega$, so $H(w)=+\infty$. The constant
ray $w_t=w$ is an actual finite-energy weak ray: its total current
is pulled back from the curve and has square zero, and comparison
gives the weak geodesic on every finite annulus. Its bounded total
potential has usual datum zero, energy slope zero, and therefore is
maximal by (22). But $H^\infty(w)=+\infty$ while
$H_\alpha(0)=0$. Formula (2) includes it exactly.

There is also a nonzero slope calibration. With the same reference
on $\mathbf P^1$, put
$u_t=\log((|z|^2+e^{-t})/(1+|z|^2))$.
The total local potential is $\log(|z|^2+|\tau|^2)$, so its
complex Hessian has rank one and it gives the actual model ray.
Writing $a=e^{-t}$ and $y=|z|^2$,
$\MA(u_t)=a\,dy/(y+a)^2$ with the uniform angular factor, and
direct integration gives
\[
 E(u_t)=-t/2,\quad
 H(u_t)=t-2+\frac{2te^{-t}}{1-e^{-t}}.
\]
The blowup of $(z,\tau)=(0,0)$ has $D=-F$, datum values $-1$
and $0$ on the exceptional and strict components, respectively,
Monge--Amp\`ere component masses $1$ and $0$, and
$\MA_\alpha(f_D)=\delta_{\ord_0}$.
Thus $E_\alpha(f_D)=-1/2$ and $H_\alpha(f_D)=1$.
This checks a positive discrepancy and a nonzero energy. Keeping
the same $dd^c$ and using $-\log|\tau|$ would double both analytic
slopes and would fail the formulas used in this paper.

Original P19.1 asks for arbitrary finite-energy weak rays on a compact
K\"ahler manifold beyond smooth polarized maximal-ray subcases,
with explicit datum, normalization and ray hypotheses. Statement (2)
covers this domain, including nonsmooth and infinite-entropy initial
potentials, and specifies the otherwise necessary exceptional
behavior. The whole original scope and supporting proof chain
passed independent review134. There is no claim to the extra singularity
requirements of P19.2, family compactness of P19.3, or equivariant
programme of P19.4.

\appendix
\section{A local analytic repair of the Rees discrepancy bound}
Let $Z$ be any smooth complex manifold of dimension $N\geq1$,
$\mathfrak a\ne0$ a coherent ideal, and $p:Y\to Z$ its normalized
analytic blowup. At a prime divisor $F$, let $v=\ord_F$ and let
$k_F$ be the order of the pullback of a nonvanishing base top form
against a nonvanishing top form at its smooth generic point.
This defines the relative canonical Weil coefficient without a
$\mathbf Q$-Cartier assumption on $K_Y$.

\begin{proposition}
For every prime $F$ on $Y$,
$k_F\leq N(v(\mathfrak a)-v(\J(\mathfrak a)))$.
For every exceptional prime the stronger $k_F+1$ bound holds.
\end{proposition}
\begin{proof}
For an ideal $\mathfrak b=(f_0,\ldots,f_q)$ define
$\Jac_1(\mathfrak b)=(f_j,\partial f_j/\partial x_i)$.
This ideal is coordinate and generator independent by the chain
and product rules. Suppose first that $F$ is a Rees prime with
$m=v(\mathfrak b)>0$, and set $\ell=v(\Jac_1(\mathfrak b))\leq m$.
Choose $f_0$ of order $m$ generating the pulled-back ideal at the
generic point. Its ratios $r_j=f_j/f_0$ are regular there.

The finite normalization map to the ordinary blowup, on its usual
chart embedded by base coordinates and generator ratios, has full
tangential rank $N-1$ at a general smooth point of $F$.
Indeed its restricted image has dimension $N-1$, and in
characteristic zero a generically finite map between those reduced
smooth loci has full rank. Choose $N-1$ functions $q_i$ from these
coordinates and ratios whose restricted differentials are independent.
Write $p^*f_0=s^m h$, where $s=0$ defines $F$ and $h$ is a unit.
Then $d(p^*f_0)\wedge dq_1\wedge\cdots\wedge dq_{N-1}$ has exact
order $m-1$. On the base the coefficients of $df_0$ have order at
least $\ell$, while
\[
 d(f_j/f_0)=(f_0df_j-f_jdf_0)/f_0^2
\]
has coefficient orders at least $\ell-m$.
Coordinate differentials also have this lower bound since
$\ell-m\leq0$. The base determinant therefore has order at least
$\ell+(N-1)(\ell-m)=m-N(m-\ell)$. Pulling back its base top form
adds $k_F$. Comparison of orders yields
\[
 k_F+1\leq N(m-\ell).                                    \tag{24}
\]
This uses the tangential rank of finite normalization with generator
ratios, not normal rank of the map to the base.

If $\mathfrak b$ has no divisorial factor, then
$\Jac_1(\mathfrak b)\subset\J(\mathfrak b)$.
Here is the complete exponent-one local proof, the specialization
of [ELSV], Theorem4.2(i) and Lemma4.3.
On a log resolution, a prime $P$ with ideal order $q$ and canonical
order $b$ requires the derivative order at least $q-b$.
Only $q-b>0$ matters. Its center has codimension $c\geq2$;
choose $x_1,\ldots,x_c$ vanishing on the smooth generic center.
Near $P=\{s=0\}$ the $f_j$ pull back as $s^q h$ and these
coordinates as $s h_i$. In the pullback of
$df_j\wedge\bigwedge_{i\ne l}dx_i$, at most one differential
uses $ds$, so its order is at least $q+c-2\geq q$.
The same order equals $v_P(\partial_lf_j)+b$.
Every derivative therefore satisfies the multiplier criterion.
Generators do too, since $\mathfrak b\subset\J(\mathfrak b)$.
The log-resolution formula proves the inclusion, with the
codimension condition retained.

Locally remove the integral divisorial factor:
$\mathfrak a=\mathfrak b\mathcal O(-G)$.
An invertible factor leaves the normalized blowup unchanged, and
the multiplier formula gives
$\J(\mathfrak a)=\J(\mathfrak b)\mathcal O(-G)$.
Thus the differences of orders are unchanged. At an exceptional
prime, $m=v(\mathfrak b)>0$ and
$\ell\geq v(\J(\mathfrak b))$; (24) proves the stronger bound.
At a nonexceptional prime $k_F=0$ and
$v(\mathfrak a)-v(\J(\mathfrak a))\geq0$.
In dimension one the ideal is locally invertible and only this
last case occurs. This treats every prime in the claimed analytic
scope with no global projectivity or vanishing theorem.
\end{proof}

\section{Source and verification boundaries}
This paper is root-authored. Complete source units actually read
in the working record include [MPWN] layout lines860--1166,
1420--1478 and1587--1832; [MP]2378--2738 and2735--2855;
[T]360--726; its companion2605.30063v2 lines569--692 and961--1028;
[SD]958--1003,1030--1095,1168--1290 and1340--1449;
[BDL]862--917; [D]1290--1548; [L]1300--1437;
and [ELSV]1000--1155. These are literal local layout coordinates,
not page numbers or a claim to have read every recursive source.
The complete paper, local discrepancy proof and calibrated transfer
steps passed independent review134 on 6 October2026. Its full
report,24 exact external premises and33 evidence bindings are
retained in the publication record. This is a source-aware model
reconstruction, not a formal proof certificate or a priority claim.
No third-party PDF or lengthy quotation is reproduced here.

\begin{thebibliography}{9}
\bibitem{MPWN}[MPWN] P. Mesquita-Piccione and D. Witt Nystr\"om,
\emph{A transcendental non-Archimedean Calabi--Yau theorem with
applications to the cscK problem},
\href{https://arxiv.org/pdf/2509.09442v1}{arXiv:2509.09442v1} (2025).
\bibitem{MP}[MP] P. Mesquita-Piccione,
\emph{A non-Archimedean theory of complex spaces and the cscK problem},
\href{https://arxiv.org/pdf/2409.06221v2}{arXiv:2409.06221v2}.
\bibitem{T}[T] A. Trusiani,
\href{https://arxiv.org/pdf/2609.31089v1}{arXiv:2609.31089v1}
(25 September 2026), TheoremB, Lemmas3.4--3.5 and Section5;
companion \href{https://arxiv.org/pdf/2605.30063v2}{2605.30063v2},
Proposition3.1 and AppendixA.1 distinguished.
\bibitem{SD}[SD] Z. Sj\"ostr\"om Dyrefelt,
\emph{K-semistability of cscK manifolds with transcendental
cohomology class},
\href{https://arxiv.org/pdf/1601.07659v2}{arXiv:1601.07659v2}, Lemma4.6.
\bibitem{BDL}[BDL] R. Berman, T. Darvas and C. H. Lu,
\emph{Convexity of the extended K-energy and the large time behavior
of the weak Calabi flow}, Geom. Topol.21 (2017), 2945--2988,
\href{https://msp.org/gt/2017/21-5/gt-v21-n5-p08-s.pdf}{published text}.
\bibitem{D}[D] T. Darvas,
\emph{The Mabuchi geometry of finite energy classes},
\href{https://arxiv.org/pdf/1409.2072v2}{arXiv:1409.2072v2}, Theorem5.5.
\bibitem{L}[L] C. Li, \emph{Geodesic rays and stability in the cscK
problem}, Ann. Sci. ENS55 (2022), 1529--1574,
\href{https://sites.math.rutgers.edu/~cl1412/papers/maximal.pdf}
{author-hosted primary text}, Lemma3.1 and Theorem1.2.
\bibitem{ELSV}[ELSV] L. Ein, R. Lazarsfeld, K. E. Smith and D. Varolin,
\emph{Jumping coefficients of multiplier ideals}, Duke Math. J.123(3)
(2004), 469--506,
\href{https://www.math.stonybrook.edu/~dror/paper-jump.pdf}
{author-hosted text}, Definition4.1, Theorem4.2(i), Lemma4.3.
\bibitem{BFJ}[BFJ] S. Boucksom, C. Favre and M. Jonsson,
\emph{Valuations and plurisubharmonic singularities},
\href{https://arxiv.org/pdf/math/0702487}{arXiv:math/0702487},
Theorem5.5 and Section5; the statement is for $\J_+$.
\bibitem{GZ}[GZ] Q. Guan and X. Zhou,
\emph{A proof of Demailly's strong openness conjecture},
\href{https://arxiv.org/pdf/1401.7158}{arXiv:1401.7158}, Theorem1.1.
\bibitem{Vu}[Vu] D.-V. Vu,
\href{https://arxiv.org/pdf/2307.15909}{arXiv:2307.15909}, Theorem1.1,
restricted positive volume on the non-K\"ahler locus.
\bibitem{Pop}[Pop] D. Popovici,
\href{https://comptes-rendus.academie-sciences.fr/mathematique/item/10.1016/j.crma.2003.11.011.pdf}
{C. R. Math. primary text}, Lemma1.2, fixed-chart regularization.
\end{thebibliography}
\end{document}

END COMPLETE MATHEMATICAL GRANT


BEGIN COMPLETE MATHEMATICAL GRANT T exact zero-start closed toric profile
\documentclass[11pt]{article}
\usepackage[a4paper,margin=26mm]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools,hyperref}
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}{Lemma}
\newcommand{\PP}{\mathbf P}
\newcommand{\ddc}{dd^c}
\newcommand{\NA}{\mathrm{NA}}
\newcommand{\MA}{\mathrm{MA}}
\newcommand{\FS}{\mathrm{FS}}
\title{Preserving the closed singularity profile in actual toric model approximation}
\author{A constructive one-branch model approximation theorem}
\date{6 October 2026}
\begin{document}
\maketitle
\begin{abstract}
For a nonnegative decreasing convex roof on $[0,1]$ with finite height,
we construct rational model approximations on actual smooth projective
models of $(\PP^1,\mathcal O(1))$. Every central component has positive
degree, including components introduced to resolve the fan. The
approximations recover energy and entropy, the entire closed $P$-level
singularity profile uniformly, and its endpoint even when its
nonpluripolar mass is zero. A uniform entropy remainder also gives a
joint model-index/time limit. Fixing the zero interval is an explicit
part of the construction. The complete theorem has passed independent review in this precise
one-branch signature, with zero analytic starting point. The full
residual hybrid approximation problem remains open.
\end{abstract}

\paragraph{Conventions and scope.}
We work over $\mathbf C$, with
$dd^c=(i/2\pi)\partial\bar\partial$,
$\rho=\log|z|^2$, $t=-\log|\tau|^2$, and
\[
 Q_0(\rho)=\log(1+e^\rho),\qquad
 \omega=dd^c Q_0,\qquad \int_{\PP^1}\omega=1.
\]
Entropy is relative to this probability volume. Non-Archimedean
metrics are over the trivially valued field $\mathbf C$.
The discrepancy of $v\operatorname{ord}_0$ is $v$.
Let $g:[0,1]\to[0,\infty)$ be continuous, convex, nonincreasing,
with $g(1)=0$. If $g\not\equiv0$, put
\[
 c=\inf\{x:g(x)=0\}\in(0,1],\qquad R=g(0).
\]
The case $g=0$ uses $c=R=0$. A finite roof height is essential to
the stated finite-entropy signature. No assertions are made about
arbitrary nonmaximal rays, a general K\"ahler class, or a degenerating
family with additional prescribed data.

\begin{theorem}\label{thm:main}
There exist roofs $g_j$ with rational breakpoints and rational slopes,
and rational $0\le c_j<1$, with the following properties.
\begin{enumerate}
\item Each $g_j$ is obtained from an actual smooth equivariant
projective modification of $\PP^1\times\PP^1$, equipped with an actual
relatively ample rational line bundle restricting to $\mathcal O(1)$
on a general fibre. Its zero interval is exactly $[c_j,1]$.
We have $c_j\to c$ and $\|g_j-g\|_\infty\to0$.
\item The normalized metrics
\[
 \varphi(v\operatorname{ord}_0)
   =\sup_{0\le x\le1}\{-xv-g(x)\},\qquad v\ge0,
\]
extended by zero on other branches, and the analogous $\varphi_j$,
satisfy $\sup\varphi_j=\sup\varphi=0$, uniform and strong convergence,
\[
 E^\NA(\varphi_j)\to -\int_0^1g(x)\,dx=E^\NA(\varphi),
 \qquad H^\NA(\varphi_j)\to R=H^\NA(\varphi).
\]
\item Their actual zero-start maximal weak rays are
\[
 u_t=\sup_{0\le x\le1}\{x\rho-F(x)-t g(x)\}-Q_0(\rho),
 \quad F(x)=x\log x+(1-x)\log(1-x),
\]
with the same formula for $u_{j,t}$. At every finite $t$ they are
bounded. If $\chi_\lambda$ and $\chi_{j,\lambda}$ denote their
Legendre test curves, then
\[
 \sup_{\lambda\le0}d_S(\chi_{j,\lambda},\chi_\lambda)\longrightarrow0,
 \qquad
 \sup_{\lambda\le0}
 \left|\int\omega_{\chi_{j,\lambda}}-
             \int\omega_{\chi_\lambda}\right|\longrightarrow0.
\]
Here all integrals are raw nonpluripolar masses; $d_S$ is the
one-dimensional singularity pseudometric with volume one.
In particular the endpoint mass is $1-c_j\to1-c$, including $c=1$.
\item For every $j,t>0$,
\[
 E(u_{j,t})=-t\int_0^1g_j(x)\,dx,
 \qquad -2\le H(u_{j,t})-t g_j(0)\le0.
\]
Consequently for arbitrary $j\to\infty$, $t_j\to\infty$,
$H(u_{j,t_j})/t_j\to R$. The energy slopes converge as well.
\end{enumerate}
\end{theorem}

\paragraph{1. Approximate the roof and its zero interval together.}
For $g\ne0$, convexity and absolute continuity give
\[
 v(x)=-g'_+(x)\ge0\quad\hbox{a.e.},\qquad
 g(x)=\int_x^1 v(s)\,ds,\qquad \int_0^1v=R.
\]
The function $v$ is nonincreasing and positive almost everywhere on
$(0,c)$, and vanishes on $(c,1)$. Indeed a flat positive portion of
$g$ would, by convexity, prevent it from subsequently decreasing to
zero. This also proves that $g$ is strictly decreasing on $[0,c]$.

Choose rational $c_j\in(0,1)$ tending to $c$. There are nonincreasing
rational step functions $v_j^0$, positive on $(0,c_j)$ and zero on
$(c_j,1)$, such that $\|v_j^0-v\|_{L^1}\to0$. Here is an elementary
construction, also valid when $v$ is unbounded near zero. Truncate
$v$ at a finite height; restrict it to $(0,c_j)$; and add a small
positive constant on that interval. The error from restriction
vanishes by absolute continuity of the integral as $c_j\to c$.
On a rational partition of $[0,c_j]$, interval averages give a
nonincreasing step function. Bounded monotone functions have arbitrarily
small $L^1$ step-approximation error. Round the finitely many averages
monotonically to positive rationals with arbitrarily small error.
Let truncation heights tend to infinity and all errors to zero.
Merge adjacent intervals with equal heights. Their rational lengths
are positive numbers $a_i^0$ and their distinct positive rational
heights are $v_i$; the lengths sum to $c_j$.

Put $g_j^0(x)=\int_x^1v_j^0$. Then
\[
 \|g_j^0-g\|_\infty\le\|v_j^0-v\|_1,
 \quad g_j^0(0)\to R,\quad \{g_j^0=0\}=[c_j,1].       \tag{1}
\]
The next step realizes these rational heights without accepting
zero-degree exceptional components on a resolution.

\paragraph{2. A smooth actual model with every component positive.}
Start with the quadrant spanned by $(0,1)$ and $(1,0)$ in the
$(\operatorname{ord}z,\operatorname{ord}\tau)$ lattice. Insert finitely
many primitive rays containing every $(p,q)$ with $p/q=v_i$.
The usual Euclidean algorithm, equivalently insertion of the sum
of adjacent primitive vectors of determinant one, constructs a
finite regular subdivision containing any finite list of positive
rational rays. Each insertion is the ordinary blowup of the
corresponding invariant intersection point over $\tau=0$.
Thus this is a sequence of actual blowups, not a formal fan datum.
It gives a smooth projective equivariant surface $\mathcal X$.

Write the final rays in increasing slope order as
\[
 n_0=(0,1),\quad n_i=(p_i,q_i)\ (1\le i\le r),
 \quad n_{r+1}=(1,0),\qquad v_i=p_i/q_i,
\]
where $p_{i+1}q_i-p_iq_{i+1}=1$.
There are finitely many extra rays. Choose positive rational weights
$a_i$ on every positive-slope ray $n_1,\ldots,n_r$, with sum exactly
$c_j$, arbitrarily close
in the first-moment transport sense to the original weights.
Explicitly, retain $(1-\delta)a_i^0$ at the original rays and distribute
$\delta c_j$ with positive rational weights over all final rays.
The coupling that fixes the retained mass gives
\[
 \int_0^{c_j}|\widetilde v_j-v_j^0|\,dx
 \le\delta\left(\int_0^{c_j}v_j^0\,dx
                    +c_j\max_i v_i\right).              \tag{2}
\]
Here $\widetilde v_j$ is the decreasing step function with heights
$v_i$ and interval lengths $a_i$ (ordered in decreasing height).
The inequality follows from the layer-cake formula: the $L^1$
distance of decreasing rearrangements is the area between their
distribution functions and is bounded by any coupling cost.
Choose $\delta$ rational small enough that (2) tends to zero.
Set $v_j=\widetilde v_j$ and $g_j(x)=\int_x^1v_j$. The zero interval
is still exactly $[c_j,1]$, and (1) still holds.

Let $F_0$ be the strict central fibre and $F_i$ the component
corresponding to $n_i$. Their actual multiplicities are $1,q_i$.
Set
\[
 d_0=0,\quad
 d_i=-\sum_k a_k\min(p_i,q_i v_k),\quad
 D=\sum_{i=1}^r d_iF_i,\qquad
 \mathcal L=p_X^*\mathcal O(1)+D.                         \tag{3}
\]
These are rational divisors and an actual rational line bundle.
The divisorial point of $F_i$ is $v_i\operatorname{ord}_0$.
The central chain has adjacent intersection one. If
$n_{i-1}+n_{i+1}=k_i n_i$, then $F_i^2=-k_i$.
Taking $d_{r+1}=0$ for the horizontal boundary, each summand of (3)
is linear across $n_i$ except its own corner. The determinant-one
identity therefore gives
\[
 D\cdot F_i=d_{i-1}+d_{i+1}-k_i d_i=\frac{a_i}{q_i},
 \qquad \mathcal L\cdot F_0=1-c_j>0.                     \tag{4}
\]
For example, the corner contribution at $i$ is
$a_i(p_{i+1}-q_{i+1}p_i/q_i)=a_i/q_i$.
At $F_0$ the first ray has $p_1=1$, hence $d_1=-c_j$,
which proves the second equality. The fibre over a nonzero parameter
has degree one. Every reduced component of every fibre has positive
degree. After clearing denominators, ampleness on proper curves,
invariance under nilpotent thickening, and fibrewise relative
ampleness (Stacks tags 0B5Y, 09MS, 0D2S) show that $\mathcal L$ is
relatively ample. The multiplicities $q_i$ have not been discarded.

\paragraph{3. Actual metric, mass, energy and entropy.}
The model metric of (3) is
\[
 \varphi_j(v\operatorname{ord}_0)
       =-\sum_i a_i\min(v,v_i)
       =\sup_x\{-xv-g_j(x)\},                           \tag{5}
\]
and is zero on the other branches. This is also directly checked
from monomial sections, so (5) is not being used as an inverse
definition of the geometric model. At the breakpoints $x=S_\ell$
of $g_j$, include both $x=0$ and $x=1$. Over the affine time chart
containing zero, for a common denominator $M$ the relative sections are
\[
 z^{Mx}\tau^{M g_j(x)}\quad (x=S_\ell),\qquad z^M.
\]
On $F_i$ their minimum order is
\[
 M\min_x\{p_i x+q_i g_j(x)\}=-M d_i.
\]
The regular fan resolves this monomial ideal; removing its actual
canonical vertical factor gives a locally bounded model metric
in the frames of $M\mathcal L$. On a general fibre its potential
is the maximum of the indicated affine functions, up to the
reference metric. Thus it has the actual datum (5).

From (4), with the actual central multiplicities, we obtain
\[
 \MA^\NA(\varphi_j)=(1-c_j)\delta_{\rm triv}
                         +\sum_i a_i\delta_{v_i\operatorname{ord}_0},
 \quad H^\NA(\varphi_j)=\sum_i a_i v_i=g_j(0).             \tag{6}
\]
Since all terms of $D$ are exceptional over the product,
\[
 E^\NA(\varphi_j)=\frac{D^2}{2}
   =-\frac12\sum_{i,k}a_i a_k\min(v_i,v_k)
   =-\int_0^1g_j(x)\,dx.                                \tag{7}
\]
For the last equality, use
$\int_0^{c_j}x v_j(x)\,dx
=\frac12\sum_{i,k}a_i a_k\min(v_i,v_k)$.
Uniform convergence of roofs implies uniform convergence of (5)
by its supremum formula. The limiting metric is genuine semipositive
as a uniform limit of genuine model metrics. It has strong convergence
as well: if $\epsilon_j=\|\varphi_j-\varphi\|_\infty$ and
$w_j=\max(\varphi_j,\varphi)$, monotonicity and translation of energy
give $d_1(\varphi_j,\varphi)\le2\epsilon_j$.

The limiting curve measure is $(1-c)\delta_{\rm triv}$ plus the
pushforward of $dx|_{(0,c)}$ by $x\mapsto v(x)\operatorname{ord}_0$.
This follows either from the distributional slope of (5), or from
the one-dimensional model intersection formula and the $L^1$
coupling used above. Its discrepancy integral is $\int v=R$.
There is no mass at infinite slope, since $v$ is integrable.
Equations (1), (6), (7) prove the stated NA limits.

\paragraph{4. The actual ray and all closed $P$-levels.}
For any of these roofs define $Q_t=\sup_x(x\rho-F(x)-tg(x))$.
It obeys $Q_0-tR\le Q_t\le Q_0$ and $Q_{t=0}=Q_0$.
In the variables $(\rho,\log|\tau|^2)$ this is convex and hence
toric plurisubharmonic. Strict convexity of $F$ gives a unique
maximizer $x$. Its gradient image lies in the graph $(x,g(x))$,
of two-dimensional measure zero. The real homogeneous
Monge--Amp\`ere measure therefore vanishes; equivalently the toric
complex homogeneous equation holds off the coordinate axes.
Boundedness on finite time annuli extends it across the axes,
which a bounded Bedford--Taylor product does not charge.
This proves that $u_t=Q_t-Q_0$ is an actual bounded weak ray.

For $0\le b\le1$ put
\[
 w_b(\rho)=\sup_{b\le x\le1}\{x\rho-F(x)\}-Q_0(\rho).
\]
For $0<b<1$, explicitly,
\[
 w_b=\begin{cases}
 b\log y-F(b)-\log(1+y),&y\le b/(1-b),\\
 0,&y\ge b/(1-b),
 \end{cases}\qquad y=|z|^2.                             \tag{8}
\]
Also $w_0=0$ and $w_1=\log y-\log(1+y)$.
The derivatives match at the interface. Its ordinary curvature
is $b\delta_0+\mathbf1_{\rm outer}\omega$, with no interface atom;
therefore its raw nonpluripolar mass is $1-b$.

These potentials are actual $P$-model envelopes. Indeed, for an
$\omega$-psh $h\le0$ with $h\le w_b+C$, subtract $b\log y$ from
$h+Q_0$ in the inner disk. The resulting subharmonic function is
bounded above at zero and extends there. The boundary inequality
and the maximum principle give $h\le w_b$ in the disk, and $h\le0$
outside. Taking the increasing envelope limit proves $P[w_b]=w_b$.
For $b=1$ the corresponding function extends to the compact sphere;
its upper limit at infinity is at most zero, so the same maximum
principle gives the assertion. The case $b=0$ is immediate.

Define the continuous extended inverse
\[
 b(s)=\begin{cases}
 c,&s=0,\\
 g^{-1}(s),&0<s<R,\\
 0,&s\ge R.
 \end{cases}                                            \tag{9}
\]
If $g=0$, take $b(s)=0$ for all $s\ge0$.
Convex duality with the constraint $g(x)\le s$ gives
\[
 \chi_\lambda:=\inf_{t\ge0}(u_t-\lambda t)
                  =w_{b(-\lambda)}\quad (\lambda\le0). \tag{10}
\]
For $s>0$ the constraint has a strict feasible point $x=1$, so
the elementary one-variable Lagrange duality has no gap.
For $s=0$, letting $t\to\infty$ restricts the supremum to
$\{g=0\}=[c,1]$, giving exactly $w_c$.
For $\lambda>0$ the infimum is $-\infty$.
These closed, parameter-concave curves have $P$-maximal levels;
Legendre biconjugacy recovers $u_t$; the maximal-test-curve
correspondence applies \cite{levels}, including the zero-mass endpoint.
The total weight differs by at most $\log2$ from
$\sup_x(x\rho+g(x)\log|\tau|^2)$, whose actual Gauss divisorial
orders give exactly (5). For the logarithmic-norm convention in
\cite{maximal}, use $s=-\log|\tau|$ and $U_s=u_{2s}/2$ with the
same background curvature. The energy calculation below gives
$E(U_s)=sE^{\rm NA}(\varphi)$, so the source's exact energy-defect
criterion proves NA maximality for the usual actual datum. Thus
P-maximal test levels and NA maximal rays are each justified.

Let $b_j$ be (9) for $g_j$. Uniform roof convergence and strict
decrease of $g$ prove $b_j(s)\to b(s)$ for $s>0$: at an interior
inverse value, bracket it by two points with strict inequalities;
at $s\ge R$, use $g(x)<R$ for every $x>0$.
At $s=0$ the needed statement is the separately imposed
$c_j\to c$. The functions $b_j$ are monotone, and $b$ is continuous
on a compact interval containing all their nonzero portions.
A finite grid and uniform continuity of $b$ turn this pointwise
convergence into
\[
 \sup_{s\ge0}|b_j(s)-b(s)|\longrightarrow0.              \tag{11}
\]
In dimension one the ordered mass formula gives
\[
 d_S(w_b,w_{b'})=\tfrac12|b-b'|.                         \tag{12}
\]
For instance, the mass of the maximum is $1-\min(b,b')$;
subtracting the average of the two masses gives (12).
This formula includes $b=1$, with zero raw mass.
Equations (8)--(12) prove uniform closed-profile recovery.
They also give the optional integrated identity
\[
 \int_{-\infty}^0 d_S(\chi_{j,\lambda},\chi_\lambda)\,d\lambda
 =\frac12\int_0^1|g_j(x)-g(x)|\,dx,
\]
by the area between the graphs of decreasing functions and their
extended inverses. Neither this integral identity nor energy
convergence alone would substitute for the endpoint condition.

\paragraph{5. Uniform analytic entropy and energy calibration.}
For a rational model roof, $v_j$ is constant, say $v_i$, on a
moment interval $I_i$ of length $a_i$. On its active radial region
the maximizing moment $x$ satisfies
\[
 \rho=\log\frac{x}{1-x}-t v_i.
\]
The radial Monge--Amp\`ere probability measure is $dx$ (with normalized
angular measure); on the intervening plateaus it has zero density.
The density relative to $\omega$ on $I_i$ is
\[
 e^{t v_i}(1-x+e^{-t v_i}x)^2.
\]
The outer interval $x>c_j$ has density one. First derivatives
match at every interface, so there is no curvature atom there.
Consequently
\[
 H(u_{j,t})=t\sum_i a_i v_i
    +2\sum_i\int_{I_i}\log(1-x+e^{-t v_i}x)\,dx.          \tag{13}
\]
Since $\log(1-x)\le\log(1-x+e^{-t v_i}x)\le0$,
and $\int_0^1\log(1-x)\,dx=-1$, (13) gives the uniform
remainder $-2\le H(u_{j,t})-tR_j\le0$.
There is no dependence on the fan, its multiplicities, or $c_j$.
Differentiation of bounded geodesic energy gives
\[
 \frac{d}{dt}E(u_{j,t})=
 \int\dot u_{j,t}\,\omega_{u_{j,t}}=-\int_0^1g_j(x)\,dx.
\]
The same formula applies to $g$, by bounded uniform approximation
at each fixed time. Since all starts have energy zero, it proves
the energy formula in the theorem and (7)'s time calibration.

\paragraph{What has and has not been obtained.}
If $g=0$, take the trivial product throughout. Otherwise the
construction treats every finite-height convex decreasing roof in
this one branch, including a zero-mass terminal level $c=1$.
It resolves all newly introduced components by positive weights
while keeping the prescribed zero interval. Thus it supplies an
existence construction in this fixed toric signature, rather than
another example of a sequence with a bad endpoint. Additional
analytic starting points, several toric branches, general K\"ahler
classes, and the full log-discrepancy-model hybrid regularization
signature of the original P19.2 require independent work.
The complete precisely scoped theorem has passed independent review.
It contributes one accepted supporting paper and changes no
original-problem completion count.

\begin{thebibliography}{99}
\bibitem{stacks} The Stacks Project, tags
\href{https://stacks.math.columbia.edu/tag/0B5Y}{0B5Y},
\href{https://stacks.math.columbia.edu/tag/09MS}{09MS}, and
\href{https://stacks.math.columbia.edu/tag/0D2S}{0D2S}:
ampleness on proper curves, nilpotent thickenings, and relative ampleness.
\bibitem{levels} J. Ross and D. Witt Nystr\"om,
\emph{Analytic test configurations and geodesic rays},
\href{https://arxiv.org/pdf/1101.1612}{Definition 5.1 and Theorem 6.8}:
maximal test curves with small unbounded locus.
\bibitem{maximal} R. Berman, S. Boucksom and M. Jonsson,
\emph{A variational approach to the Yau--Tian--Donaldson conjecture},
\href{https://arxiv.org/pdf/1509.04561}{Definition 4.2 and Corollary 6.7}:
usual total-potential datum and NA maximality by energy.
\bibitem{BJ} S. Boucksom and M. Jonsson,
\href{https://arxiv.org/pdf/1801.08229}{Singular semipositive metrics
in non-Archimedean geometry}, Section 2.2, Corollary 4.16,
Proposition 7.7, Definition 12.1 and Theorem A;
\href{https://arxiv.org/pdf/2107.11221}{Section 5.2 and Theorem 5.5}
for the NA $d_1$ topology.
\bibitem{BHJ} S. Boucksom, T. Hisamoto and M. Jonsson,
\href{https://www.math.nagoya-u.ac.jp/~hisamoto/papers/BHJ2_16.pdf}
{Uniform K-stability, Duistermaat--Heckman measures and singularities
of pairs}, Sections 2.3 and 2.6--2.7: model intersections and discrepancy.
\bibitem{toric} R. Berman and B. Berndtsson,
\href{https://arxiv.org/pdf/1207.6128}{Sections 2.1--2.2}:
convex and toric Monge--Amp\`ere with its dimension factorial.
\bibitem{BT} E. Bedford and B. A. Taylor,
\href{https://www.math.stonybrook.edu/~ebedford/PapersForM655/BTNewCapacity.pdf}
{A new capacity for plurisubharmonic functions}, Theorems 2.1 and 6.9.
\bibitem{nonpolar} S. Boucksom, P. Eyssidieux, V. Guedj and A. Zeriahi,
\href{https://arxiv.org/pdf/0812.3674}{Section 1.2}:
nonpluripolar products; T. Darvas, E. Di Nezza and C. H. Lu,
\href{https://arxiv.org/pdf/1909.00839}{Lemma 3.4}:
ordered singularity metric through zero mass.
\bibitem{energy} R. Berman, S. Boucksom, V. Guedj and A. Zeriahi,
\href{https://arxiv.org/pdf/0907.4490}{Section 2.1}:
bounded energy cocycle and first variation.
\end{thebibliography}
\end{document}

END COMPLETE MATHEMATICAL GRANT


BEGIN COMPLETE MATHEMATICAL GRANT C exact finite-H CPn absolute endpoint
\documentclass[10pt]{article}
\usepackage[a4paper,margin=26mm]{geometry}
\usepackage{amsmath,amssymb,amsthm,hyperref}
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}{Lemma}
\newcommand{\ddc}{dd^c}
\newcommand{\MA}{\operatorname{MA}}
\newcommand{\PP}{\mathbf P}
\title{A finite-entropy initial singularity can erase an absolute zero-mass endpoint}
\author{A finite-entropy counterexample to absolute endpoint invariance}
\date{6 October 2026}
\begin{document}
\maketitle
\begin{abstract}
On every complex projective space of dimension at least two, we construct
an unbounded full-mass finite-energy initial potential with finite
probability entropy. For an actual bounded nef non-Archimedean model datum,
the zero-start maximal ray has a nontrivial absolute $P$-model endpoint
of zero nonpluripolar mass, whereas the maximal ray from this singular
initial potential has identically minus-infinite zero level. Both rays
have entropy slope one and remain at one fixed finite $d_1$ distance.
The example rules out absolute endpoint invariance under arbitrary
finite-entropy initial-point changes. It does not rule out the entire
residual model approximation problem or assert a failure of relative
envelopes adapted to the prescribed initial potential.
\end{abstract}

\paragraph{Conventions and sole theorem premise.}
Let $X=\PP^n_{\mathbf C}$, $n\geq2$, $\omega=\omega_{\rm FS}$,
$\int_X\omega^n=1$, $\ddc=(i/2\pi)\partial\bar\partial$ and
$t=-\log|\tau|^2$. Set
\[
 E(u)=\frac1{n+1}\sum_{k=0}^n\int_Xu\,
        \langle\omega_u^k\rangle\wedge\omega^{n-k},\qquad
 H(u)=\operatorname{Ent}(\langle\omega_u^n\rangle\mid\omega^n).
\]
For full-mass $u$ these are probability conventions. The sole substantial
theorem premise is the complete established P19.1 mathematical theorem
in its fixed smooth compact K\"ahler signature, denoted $R$: for every
actual $w\in\mathcal E^1$ and $\phi\in\mathcal E^{1,\rm NA}$ the
actual maximal weak ray $r(w,\phi)$ exists, is ordered in both arguments,
has $E(r(w,\phi)_t)=E(w)+tE^{\rm NA}(\phi)$, and an actual weak ray
is maximal for its usual datum exactly when its energy defect vanishes.
A maximal ray with a finite-entropy slice has entropy slope
$H^{\rm NA}(\phi)$. The complete theorem body, not a historical verdict,
is the premise. It contains no prescribed endpoint invariance grant.

Write
\[
 \chi_u(\lambda)=\inf_{t\geq0}(u_t-t\lambda),\qquad
 P_\omega[v]=\left(\lim_{C\to\infty}P_\omega(v+C,0)\right)^*.
\]
An identically $-\infty$ level is assigned raw mass zero by convention;
it is not a finite-energy function and is assigned no singularity metric.
All $P$ ceilings here are absolute ceilings for the smooth background
$\omega$. No singular initial point is substituted for that background.

\begin{theorem}\label{main}
For every $n\geq2$ there exist a nonpositive
$w\in\mathcal E^1(X,\omega)$ with $H(w)<\infty$, singular only at
$p=[1:0:\cdots:0]$, and an actual bounded nef model datum $\phi$, with
\[
 E^{\rm NA}(\phi)=-\frac n{n+1},\qquad H^{\rm NA}(\phi)=1,
\]
such that $a=r(0,\phi)$ and $b=r(w,\phi)$ satisfy
\[
 \chi_a(0)=w_H=\log\frac{|Z_0|^2}{\sum_{i=0}^n|Z_i|^2},
 \quad P_\omega[w_H]=w_H,\quad
 \int_X\langle\omega_{w_H}^n\rangle=0,\qquad
 \chi_b(0)\equiv-\infty.                              \tag{1}
\]
For every finite time $d_1(a_t,b_t)=-E(w)$, and both entropy slopes
are one. In fact every finite-time entropy of both rays is finite.
\end{theorem}

\section{A full-mass isolated singularity of finite entropy}
In the affine chart $Z_0\ne0$, put $z_i=Z_i/Z_0$,
$\rho=\log\sum_{i=1}^n|z_i|^2$, $Q_0(\rho)=\log(1+e^\rho)$,
$\delta=1/3$, $\rho_B=-\log2$, and
$F(x)=x\log x+(1-x)\log(1-x)$. Set
\[
 C=1-\delta-F(\delta),\qquad
 Q(\rho)=
 \begin{cases}
 -(-\rho)^{1/3}+C,&\rho\leq-1,\\
 \delta\rho-F(\delta),&-1\leq\rho\leq\rho_B,\\
 Q_0(\rho),&\rho\geq\rho_B,
 \end{cases}
 \qquad w=Q-Q_0.                                      \tag{2}
\]
Both values and first derivatives match. The function $Q$ is convex
and increasing; thus its radial weight is psh in $\mathbf C^n$.
Outside a ball $w=0$, so (2) glues to a global $\omega$-psh function.
The middle line is a tangent to $Q_0$. For $L=-\rho\geq1$,
$Q'=\tfrac13L^{-2/3}>Q_0'(-L)$, because
$L^{2/3}e^{-L}/(1+e^{-L})$ decreases there and is less than $1/3$
at one. The difference $Q-Q_0$ increases to its nonpositive value
at $-1$. Consequently $w\leq0$ and $\sup w=0$.
Its sole pole is $p$, and $Q'(-\infty)=0$.

Here are explicit mass, energy and entropy calculations, rather than
an inference from zero Lelong number. For a radial total weight $Q$,
the radial distribution of its top Monge--Amp\`ere measure is
$d(Q'^n)$, with normalized angular measure. Its mixed distribution
with $k$ copies of $\ddc Q$ and $n-k$ of $\ddc Q_0$ is
\[
                    d\bigl(Q'^k Q_0'^{\,n-k}\bigr).     \tag{3}
\]
These formulas follow by expanding the radial and tangential Hessian
eigenvalues and polarizing. They also hold for the present $C^1$
piecewise smooth convex weight by smooth convex approximation.
Continuity of $Q'$ gives no interface mass. Since $Q'$ increases from
zero to one, the measure on $X\setminus\{p\}$ has total mass one.
Thus the nonpluripolar product has full mass.

On the inner region its exact radial top measure is
\[
 d\MA(w)=n\,3^{-n}\frac23 L^{-2n/3-1}\,dL,
 \qquad |w|=O(1+L^{1/3}).                              \tag{4}
\]
Their product is integrable for every $n\geq1$. All lower mixed
distributions in (3) have an additional factor exponentially decaying
as $e^{-(n-k)L}$, so every energy summand is absolutely finite.
This is also the genuine decreasing-truncation energy: for
$w_j=\max(w,-j)$ the interface lies at $L_j\asymp j^3$.
Its top radial boundary mass is at most $Q'(-L_j)^n$, and its
energy contribution is $O(jL_j^{-2n/3})=o(1)$.
Lower mixed terms have the extra exponential factors. On the inner
truncated region the reference mass is exponentially small. Hence
all the truncated energy integrals converge to those just computed,
and $w\in\mathcal E^1$ with finite $E(w)<0$.

The FS reference distribution is $d(Q_0'^n)$. On the inner region
the relative probability density $f$ therefore satisfies
\[
 f=\frac{Q'^{n-1}Q''}{Q_0'^{n-1}Q_0''},\qquad
 \log f=nL-\left(\frac{2n}{3}+1\right)\log L+O(1).
                                                               \tag{5}
\]
The entropy tail is bounded by a constant times
$\int_1^\infty L^{-2n/3}\,dL$, finite for every $n\geq2$.
The remaining regions have finite entropy; the affine middle region
has zero top density. The universal negative-entropy bound controls
the negative part. Thus $H(w)<\infty$. This dimension threshold
explains why the same radial isolated-pole example on a curve has
infinite entropy.

\section{An actual nef model and its usual datum}
Let $H=\{Z_0=0\}$, which does not contain $p$. Blow up the smooth
codimension-two center $H\times\{0\}$ in $X\times\PP^1$:
\[
 \pi:\mathcal X\longrightarrow X\times\PP^1,
 \qquad \mathcal L=\pi_X^*\mathcal O(1)-E.
\]
The ordinary ideal is locally $(Z_0,\tau)$. The sections
$Z_0,\tau Z_1,\ldots,\tau Z_n$ have exactly this base ideal in the
appropriate bundle frames over the affine time chart, with no other
base locus there. On the blowup over that chart their divided sections
generate $\mathcal L$ and define a morphism
$g:\mathcal X|_{\mathbf A^1}\to\PP^n$, with
$\mathcal L|_{\mathbf A^1}=g^*\mathcal O(1)$.
Away from time zero the compactified model is the trivial product
with its original pulled-back bundle. Thus the actual rational bundle
is relatively semiample and relatively nef on the whole base.
It is not asserted to be relatively ample.

The central components are the strict product fiber $F_0$ and $E$,
both of time multiplicity one. The restriction of $\mathcal L$ to
$F_0\simeq X$ is trivial, and its top intersection on $E$ is one.
Indeed $E=\PP(\mathcal O_H(-1)\oplus\mathcal O_H)$ in the quotient
conormal convention. For $h=c_1(\mathcal O_H(1))$ and
$\xi=c_1(\mathcal O_E(1))$, we have
\[
 \xi^2+h\xi=0,\quad \pi_*\xi=1,\quad
 \int_E(h+\xi)^n=\sum_{k=1}^n\binom nk(-1)^{k-1}=1.
\]
The divisorial point of $E$ is $\operatorname{ord}_H$, and the blowup
relative canonical coefficient is one. The discrepancy formula
$(\kappa+1-b)/b$ is therefore one. The genuine model probability
measure and entropy are
\[
 \MA^{\rm NA}(\phi)=\delta_{\operatorname{ord}_H},
                         \qquad H^{\rm NA}(\phi)=1.      \tag{6}
\]
On the entire original NA carrier the actual section metric is
\[
                    \phi(v)=-\min\{v(H),1\}\in[-1,0].   \tag{7}
\]
Here $v(H)$ is the local effective Cartier-divisor order, with value
$+\infty$ at supports contained in $H$. Off $H$ one generator is a
unit; on $H$ another projective coordinate is a unit. This proves
(7) for supported semivaluations as well as function-field valuations.

For completeness set $T=\pi_X^*c_1(\mathcal O(1))$. The projective
bundle relation above gives $T^nE=0$ and
$T^{n+1-r}E^r=-1$ for $2\leq r\leq n+1$.
Consequently
\[
 E^{\rm NA}(\phi)=\frac{(T-E)^{n+1}}{n+1}
 =-\frac1{n+1}\sum_{r=2}^{n+1}(-1)^r\binom{n+1}r
 =-\frac n{n+1}.                                      \tag{8}
\]
All component multiplicities, line bundles and fixed factors are actual.

\section{The zero-start ray and its rigid absolute endpoint}
The associated actual total potential is
\[
 a_t=\log\frac{|Z_0|^2+e^{-t}\sum_{i=1}^n|Z_i|^2}
                       {\sum_{i=0}^n|Z_i|^2}.          \tag{9}
\]
It is bounded on each finite time annulus. On the affine blowup chart
the extended total current is $[E]+g^*\omega_{\rm FS}$; after removal
of the exceptional fixed divisor its residual current is
$g^*\omega_{\rm FS}$. On the punctured family $[E]$ disappears
and the $(n+1)$st power vanishes. Thus the actual homogeneous
geodesic equation holds on its required domain.
Its datum is (7), by the divided-section compatibility. Bounded
geodesic energy is affine. At zero its derivative is minus the FS
average of $\sum_{i=1}^n|Z_i|^2/\sum_{i=0}^n|Z_i|^2$, hence
$E(a_t)=-nt/(n+1)$. Equation (8) and $R$'s actual energy-defect
criterion identify it with $r(0,\phi)$.

The ray decreases to $w_H$, which has ordinary curvature $[H]$.
Its nonpluripolar product is zero in every positive degree, in
particular its top raw mass is zero. Nevertheless it is a nontrivial
absolute $P$-model potential. To verify this directly, let
$h_0\leq0$ be any $\omega$-psh rooftop competitor below $w_H+C$.
Locally subtracting $\log|Z_0|^2$ from its total weight leaves a
psh function off $H$, bounded above there, hence with a psh extension.
Thus $\omega_{h_0}-[H]$ is a positive closed current of zero
cohomology class. Its integral against $\omega^{n-1}$ is zero,
so positivity makes it zero. On the compact connected $X$ this gives
$h_0=w_H+C'$; $\sup h_0\leq0$ forces $C'\leq0$.
Since $w_H$ itself is a competitor, $P_\omega[w_H]=w_H$.
The same reasoning proves the useful rigidity statement
\[
 h\in\operatorname{PSH}(X,\omega),\quad h\leq w_H+C
                      \quad\Longrightarrow\quad h=w_H+C'.       \tag{10}
\]

An optional direct entropy calibration also gives
\[
 H(a_t)=t+(n+1)\int_0^1n x^{n-1}
                     \log\bigl(x+e^{-t}(1-x)\bigr)\,dx,
 \qquad -\frac{n+1}{n}\leq H(a_t)-t\leq0.              \tag{11}
\]
Indeed its radial density relative to FS is
$e^{-nt}((1+r^2)/(1+e^{-t}r^2))^{n+1}$; use the transported
moment $x=e^{-t}r^2/(1+e^{-t}r^2)$, whose radial probability is
$n x^{n-1}dx$. This checks the probability and squared-log time.

\section{The singular-start ray loses its zero level}
The stationary ray $w$ has actual usual NA datum zero: on every
Gauss divisorial component centered at its pole, (2) is $O(t^{1/3})$
and hence has zero logarithmic-square coefficient; away from the
pole it is locally bounded. The canonical psh extension of those
divisorial data is zero. This uses the usual total-potential datum,
not pointwise division of the value $w(p)=-\infty$ by time.
Its energy slope is zero, so $R$ identifies $r(w,0)_t=w$.
Constant negative datum $-1$ gives $r(w,-1)_t=w-t$.
Order in both arguments and (7) imply
\[
                w-t\leq b_t=r(w,\phi)_t\leq w,
                \qquad b_t\leq a_t.                   \tag{12}
\]
At any point where $w$ is finite, the finite convex time function
$b_t$ is bounded above by $w$ and therefore is nonincreasing.
At $p$ all its values are $-\infty$. Its decreasing limit is
either a genuine $\omega$-psh function or identically $-\infty$.
If the limit were a nontrivial $h$, (9) and (12) would give
$h\leq w_H$ and $h\leq w$. Rigidity (10) makes
$h=w_H+C'$, finite at $p$, contradicting $w(p)=-\infty$.
Hence $\chi_b(0)=\inf_t b_t\equiv-\infty$, proving (1).

The ordered distance and exact energy identity in $R$ give
\[
 d_1(a_t,b_t)=E(a_t)-E(b_t)=-E(w)\quad\hbox{for every }t.          \tag{13}
\]
The singular ray is maximal and its initial entropy is finite, so
$R$ gives $H(b_t)/t\to H^{\rm NA}(\phi)=1$.
Every finite-time entropy is finite as well. Indeed this limit
supplies finite-entropy times tending to infinity. The finite-energy
Mabuchi functional is geodesically convex and is entropy plus
finite contracted energies \cite{BDL}. Its initial value and values
at those times are finite. Convexity makes its value finite at every
intermediate time; the contracted energies are finite on $\mathcal E^1$,
so entropy is finite there. The same assertion for $a$ follows from
(11). No entropy continuity under a varying initial point is asserted.

\section{What this example decides}
This is a finite-initial-entropy obstruction to absolute endpoint
invariance, even with bounded datum, finite discrepancy entropy,
constant finite ray distance and exact entropy-slope agreement.
Both zero-level raw masses are zero; those numbers do not identify
their $P$ data. A singularity metric is not applied to the identically
$-\infty$ level. The target model is nef and semiample; none of the
claims requires pretending it is relatively ample.

The example does not prove that no model sequence can recover a
prescribed singular-start ray or its relative endpoint. A sequence
retaining the singular initial potential is not excluded. Thus the
full unchanged original P19.2 existence problem remains open, and
this independently accepted supporting theorem changes no
original-problem completion count.
It strengthens the earlier curve diagnostic by replacing its
infinite initial entropy with a finite one in every dimension $n\geq2$.

\begin{thebibliography}{9}
\bibitem{R} Complete established P19.1 mathematical theorem,
\emph{Entropy slopes of finite-energy K\"ahler rays: calibration,
recovery, and arbitrary starting points}, 6 October 2026.
Used only in its full fixed smooth compact K\"ahler signature.
\bibitem{BDL} R. Berman, T. Darvas and C. H. Lu,
\emph{Convexity of the extended K-energy and the large time behavior
of the weak Calabi flow}, Geometry \& Topology 21 (2017), 2945--2988,
\href{https://msp.org/gt/2017/21-5/gt-v21-n5-p08-s.pdf}{Theorem 4.7}.
In its operator convention use potential $u/(2\pi)$; currents and
probability entropy agree. Only finite contracted energies and
geodesic convexity are used.
\end{thebibliography}
\end{document}

END COMPLETE MATHEMATICAL GRANT


BEGIN COMPLETE MATHEMATICAL GRANT S exact singular-start relative profile
---
title: "Retaining a singular start in model approximation"
subtitle: "Relative P ceilings and an explicit collapsing boundary"
author: "Independently reviewed supporting theorem"
date: "6 October 2026"
geometry: "margin=25mm"
fontsize: 11pt
header-includes:
  - '\usepackage{amsmath,amssymb,amsthm,mathrsfs}'
  - '\newtheorem{theorem}{Theorem}'
  - '\newtheorem{lemma}[theorem]{Lemma}'
  - '\newcommand{\MA}{\operatorname{MA}}'
  - '\newcommand{\PSH}{\operatorname{PSH}}'
  - '\newcommand{\NA}{\mathrm{NA}}'
---

## Status and original scope

**Independent review PASS for the theorem below; original P19.2 remains open.**
We prove a relative-envelope lemma and an explicit model approximation
theorem on every complex projective space of dimension at least two.
It retains exactly the unbounded finite-entropy initial potential in C,
computes every closed P level relative to that actual start, and recovers
energy and entropy. Its actual relatively ample rational models approach
C's nef hyperplane datum. Their genuine endpoints decrease to the actual
identically minus-infinite endpoint, with raw mixed masses tending to zero.
No singularity metric or probability measure is assigned to that datum.

R, T and C are the three supplied complete mathematical grants.
R supplies fixed smooth compact Kähler finite-energy foundations and
maximal-ray results. C supplies its initial potential and actual blowup
calculations. T is used only on its zero-start
$(\mathbf P^1,\mathcal O(1))$ domain to recheck a round140 diagnostic.
Historical verdicts expand none of their domains. Round140 is unreviewed
proof data, not a fourth grant.

## 1. Conventions and the unchanged missing signature

Let $(X,\omega)$ be connected, smooth, compact Kähler of dimension $n\ge1$,
$\alpha=[\omega]$, $V=\int\omega^n$, $\mu_0=\omega^n/V$. Set
\[
dd^c=\frac{i}{2\pi}\partial\bar\partial,\quad t=-\log|\tau|^2,\quad
dd^c\log|f|^2=[\operatorname{div}(f)].
\]
Use
\[
E(u)=\frac1{(n+1)V}\sum_{k=0}^n\int u\,
\langle\omega_u^k\rangle\wedge\omega^{n-k},\quad
\MA(u)=V^{-1}\langle\omega_u^n\rangle,\quad
H(u)=\operatorname{Ent}(\MA(u)\mid\mu_0).
\]
On $\mathcal E^1$, $E(0)=0$, $E(u+c)=E(u)+c$, and entropy is full
probability entropy, infinite without absolute continuity. An actual
weak ray is strongly continuous at zero and is the canonical
finite-energy geodesic on every finite interval. Its actual total
potential is $U(x,\tau)=u_{-\log|\tau|^2}(x)$.

On an actual smooth equivariant model a vertical divisor $D$ gives
$f_D(v_F)=D_F/b_F$, $b_F=\operatorname{ord}_F(\tau)$, with sign fixed
by $U+\log|s_D|^2=O(1)$ for bounded compatible model weights.
A singular-start ray need not have bounded residual weight; its usual
datum still comes from its actual divisorial coefficients.
The carrier is the original full $X^\beth$, including supported
semivaluations. NA entropy is $\int A_X\MA_\alpha(\phi)$ with R's
probability normalization.

For a prescribed start $w$ set
\[
\chi_u(\lambda)=\inf_{t\ge0}(u_t-t\lambda),\qquad
\mathscr P_w[h]=\left(\lim_{C\to\infty}P_\omega(h+C,w)\right)^*.
\tag{1}
\]
The roof is the usc supremum of psh competitors below both obstacles.
Set $\mathscr P_w[-\infty]=-\infty$ only as a placeholder. For a
genuine level define the raw mixed masses
\[
M_k(h)=V^{-1}\int\omega^{n-k}\wedge\langle\omega_h^k\rangle,
\qquad1\le k\le n.
\tag{2}
\]
At an identically minus-infinite boundary we explicitly extend only
these positive-degree numbers by zero; this does not define a current
or probability measure. For genuine levels $M_0=1$; it is not extended
to that placeholder.

The special theorem freezes actual levels and relative ceilings, all
masses (2), and decreasing extended convergence at a collapsing
boundary. Original P19.2 additionally requires arbitrary prescribed
finer P data, arbitrary actual weak rays, general compact Kähler
classes and residual log-discrepancy-model regularization. The theorem
does not replace that task. Raw masses cannot identify all zero-mass
P data, and multiplier-ideal I equivalence is no substitute.

## 2. The relative-envelope argument

\begin{lemma}\label{relative}
Let $u$ be an actual finite-energy weak ray from $w$. If
$\chi=\chi_u(\lambda)$ is a genuine $\omega$-psh potential, then
$\mathscr P_w[\chi]=\chi$. The minus-infinite case has the same
equality only in the placeholder convention. No NA maximality or
entropy assumption is used.
\end{lemma}

*Proof.* We have $\chi\le w$. Let $C>0$ and let $h$ be a psh
competitor satisfying $h\le w$ and $h\le\chi+C$.
For $T>t>0$, $v_s=\max(u_s,h+\lambda s)$ is a subgeodesic on $[0,T]$.
Its slices are finite energy: they lie above $u_s$ and below
finite-energy potentials plus constants. Its boundary upper values
are at most $w$ and $u_T+C$. The canonical geodesic between the latter
values is $u_s+Cs/T$, since adding an affine time constant preserves
the equation and Perron characterization. Comparison gives
$h+\lambda t\le u_t+Ct/T$. Let $T\to\infty$ and then take the
infimum over $t$. Thus $h\le\chi$. Each roof
$P_\omega(\chi+C,w)$ equals $\chi$, itself a competitor. Taking
the ceiling limit proves the claim. For $\chi=-\infty$ there is no
genuine competitor. \(\square\)

This statement explicitly assumes a genuine psh level; no general
minimum-principle theorem is imported. All levels below are proved
psh directly. If actual rays $u_j$ from the same $w$ decrease
pointwise to $u$, then
\[
\chi_{u_j}(\lambda)\downarrow\chi_u(\lambda)
\tag{3}
\]
at every level and point: $\inf_j\inf_t=\inf_t\inf_j$.
This includes infinite values, but proves no general mixed-mass or
entropy continuity. The absolute ceiling is
$P_\omega[h]=\mathscr P_0[h]$, a distinct obstacle. C rules out
its invariance under finite-entropy singular starting-point changes.
The lemma asserts no absolute invariance.

## 3. Retain C's actual initial potential

Work on $\mathbf P^n_{\mathbf C}$, $n\ge2$, with FS form and volume
one, $p=[1:0:\cdots:0]$, $H=\{Z_0=0\}$. In the affine chart of $p$
put $\rho=\log\sum_{i=1}^n|Z_i/Z_0|^2$, $Q_0=\log(1+e^\rho)$,
$\delta=1/3$, $F(x)=x\log x+(1-x)\log(1-x)$,
$C_*=2/3-F(\delta)$, and take exactly
\[
Q(\rho)=
\begin{cases}
-(-\rho)^{1/3}+C_*,&\rho\le-1,\\
\delta\rho-F(\delta),&-1\le\rho\le-\log2,\\
Q_0(\rho),&\rho\ge-\log2,
\end{cases}\qquad w=Q-Q_0.
\tag{4}
\]
C proves $w\le0$, $\sup w=0$, $w\in\mathcal E^1$, $H(w)<\infty$,
and that its sole pole is $p$. Its radial mixed distribution is
$d(Q'^kQ_0'^{\,n-k})$, with normalized angular measure and no
interface atom. These conclusions are used only in their $n\ge2$
scope.

Its conjugate is
\[
F_w(x)=
\begin{cases}
2/(3\sqrt{3x})-C_*,&0<x<\delta,\\
F(x),&\delta\le x\le1,
\end{cases}\qquad F_w(0)=+\infty.
\tag{5}
\]
The inner critical point is $\rho=-(3x)^{-3/2}$.
Both values at $\delta$ are $F(\delta)$, with left derivative $-1$
and right derivative $-\log2$, recording the affine interval of $Q$.
On the inner branch
\[
F'_w(x)=-(3x)^{-3/2},\qquad F''_w(x)=(2\sqrt3)^{-1}x^{-5/2}.
\tag{6}
\]
It is strictly convex and finite on $(0,1]$, but infinite at zero.
That feature retains the actual initial pole.

## 4. An explicit singular-start model approximation theorem

\begin{theorem}\label{main}
Blow up $H\times\{0\}$ in $\mathbf P^n\times\mathbf P^1$, with
exceptional divisor $E$. For rational $0<s<1$ put
\[
\mathcal L_s=T-sE,\quad T=\pi_X^*\mathcal O(1),\quad
\eta_s(v)=-s\min(v(H),1),\quad a=1-s.
\tag{7}
\]
These are actual relatively ample rational bundles. Both central
multiplicities are one and
\[
\begin{split}
\MA^{\NA}(\eta_s)&=a^n\delta_{\rm triv}
 +(1-a^n)\delta_{\operatorname{ord}_H},\\
e_s=E^{\NA}(\eta_s)&=(1-a^{n+1})/(n+1)-s,\\
h_s=H^{\NA}(\eta_s)&=1-a^n.
\end{split}\tag{8}
\]
The actual maximal weak ray from the unchanged $w$ is
\[
b_{s,t}=\sup_{0<x\le1}\{x\rho-F_w(x)-t(x-a)_+\}-Q_0(\rho).
\tag{9}
\]
For $s=1$ use C's nef datum $\phi$ and (9) with $a=0$; then
$b_{1,t}=Q(\rho-t)-Q_0$ and $b_1=r(w,\phi)$.

For $s_j=1-1/j$, $j\ge2$, the data decrease uniformly on the full
NA carrier to $\phi$, strongly and with converging energy and
entropy. All rays start at the identical $w$ and
\[
w-st\le b_{s,t}\le w,\quad E(b_{s,t})=E(w)+te_s,\quad
b_{s_j,t}\downarrow b_{1,t},\quad
d_1(b_{s_j,t},b_{1,t})=t(e_{s_j}-e_1).
\tag{10}
\]
For $0<d\le1$ put
\[
V_d=\sup_{0<x\le d}\{x\rho-F_w(x)\}-Q_0(\rho).
\tag{11}
\]
All closed levels with $\lambda\le0$ equal
$V_{d_s(\lambda)}$, $d_s(\lambda)=\min(1,1-s-\lambda)$.
The sole zero value $d=0$, at $s=1,\lambda=0$, denotes an
identically minus-infinite level. All levels with $\lambda>0$
are identically minus infinite. Each genuine $V_d$ equals its
actual relative ceiling, retains $w$ near $p$, has pole coefficient
$1-d$ at $H$ and raw masses $M_k(V_d)=d^k$.

Ceilings converge decreasingly at every level, including zero.
Uniformly for $\lambda\le0$,
\[
|M_k(\chi_{b_{s_j}}(\lambda))-M_k(\chi_{b_1}(\lambda))|\le k/j.
\tag{12}
\]
At zero, $V_{1/j}\downarrow-\infty$, with raw masses $j^{-k}$.
For $\lambda<0$ both levels are genuine and their singularity
pseudodistance is at most $n/(2j)$. No metric is assigned at the
target zero level.

All finite-time entropies are finite. For a finite $B_n\le0$
depending only on this start,
\[
H(w)+B_n\le H(b_{s,t})-th_s\le H(w)
\quad(0<s\le1,\ t\ge0).
\tag{13}
\]
Hence every joint $j_\ell,t_\ell\to\infty$ has
$H(b_{s_{j_\ell},t_\ell})/t_\ell\to1$, and energy slopes tend
to $-n/(n+1)$.
\end{theorem}


### 4.1. Actual geometry, factors and intersections

Over the affine time chart the sections $Z_0,\tau Z_1,\ldots,\tau Z_n$
generate the center ideal in $\mathcal O(1)$ frames. Locally it is
$\mathfrak a=(Z_0,\tau)$, and on the blowup it becomes $\mathcal O(-E)$.
Divided sections define $g:\mathcal X|_{\mathbf A^1}\to\mathbf P^n$
with $g^*\mathcal O(1)=T-E$. The graph $(\pi_X,g)$ is a closed
immersion into $X\times\mathbf P^n\times\mathbf A^1$: it is the
Rees-algebra closed immersion from those generators.
If $s=A/M$, $0<A<M$, then
$M\mathcal L_s=(M-A)T+A(T-E)$ is the pullback of
$\mathcal O(M-A,A)$. The positive projective powers and Segre
give a relative projective embedding. Away from zero the bundle
is the product $\mathcal O(M)$; ampleness is local on the base,
so the compactified bundle is relatively ample.

The actual fixed factor is $\mathfrak a^A$, with pullback
$\mathcal O(-AE)$; the additional bundle factor is $T^{M-A}$.
A bounded compatible model weight is $s$ times the divided-section
weight plus $1-s$ times the reference. It gives (7), including
$v(H)=+\infty$ on supported semivaluations in $H$.
Ray (9), with its pole at $p$, is not asserted to have a bounded
residual weight on that model.

C proves both central multiplicities are one, the relative canonical
divisor is $E$, and $T^nE=0$, $T^{n+1-r}E^r=-1$ for
$2\le r\le n+1$. Also $\mathcal L_s|_{F_0}=a\mathcal O(1)$.
Binomial expansion gives
$\mathcal L_s^nF_0=a^n$, $\mathcal L_s^nE=1-a^n$ and
$\mathcal L_s^{n+1}=1-a^{n+1}-(n+1)s$.
The exceptional discrepancy is $(1+1-1)/1=1$.
The actual model component formula gives (8), with probability
mass one. The uniform datum error is exactly $1-s$, including
supports. Bounded uniform psh convergence and energy convergence
give strong convergence using R's finite-energy foundations.

### 4.2. Actual weak ray and usual datum

Conjugacy at time zero gives $w$ in (9), while
$0\le(x-a)_+\le s$ gives its sandwich. Every slice is full mass
and finite energy. Its total radial weight is convex in
$(\rho,\log|\tau|^2)$ and increasing in $\rho$, hence psh.
On smooth active pieces the gradient in $(\rho,t)$ lies on
$(x,-(x-a)_+)$. Since $t=-\log|\tau|^2$, the gradient in
$(\rho,\log|\tau|^2)$ is $(x,(x-a)_+)$. Thus its Hessian determinant is zero.
The complex homogeneous determinant is that determinant times
a positive multiple of $Q_t'^{\,n-1}$.

To check weak geodesicity across the retained pole, use bounded
weights
\[
Q_m=m^{-1}\log\bigl(e^{mQ}+e^{m(Q_0-m)}\bigr).
\]
They are $C^1$ in the radial variable $\rho$, strictly convex and
increasing, with bounded global potentials; global $C^1$ regularity
at $p$ is not asserted. They have endpoint slopes zero and one, and decrease to $Q$.
The soft maximum decreases when its scale decreases and either
input decreases. Their conjugates $F_m=Q_m^*$ increase to $F_w$.
At zero $F_m(0)=m$. Replacing $F_w$ by $F_m$ in (9) gives bounded
rays decreasing to (9). Compactness of maximizing moments proves
convergence at fixed finite $\rho,t$. A moment tending to zero is
excluded since $F_m(x)\ge F_N(x)$ for every $m\ge N$, while
$F_N(0)=N$, and $N$ is arbitrary.

On compact sets away from $p$ and $H$ these bounded approximants
have locally bounded Hessian with matching first derivatives
across the finitely many interfaces. The corner $x=a$ produces
a plateau of constant moment, not a derivative discontinuity.
Their almost everywhere homogeneous determinant is zero.
Bedford--Taylor products of such potentials give zero there.
On finite annuli they are bounded across $p$ and $H$, and bounded
products do not charge these analytic sets. Thus they solve the
entire bounded homogeneous equation and are canonical geodesics
by comparison, using the bounded foundations retained in R.

The decreasing limit is the canonical finite-energy geodesic
on every finite interval. Indeed any competitor below its boundary
values is below all approximating boundary values, hence below
all approximating geodesics and their limit. Correct strong
boundary continuity follows from
$|b_{s,t}-b_{s,T}|\le s|t-T|$ wherever finite, with identical
poles, and the ordered energy/translation identities. Decreasing
finite-energy continuity applies since slices are bounded below
by $w-st$. Thus (9) is an actual ray, not an assigned subgeodesic.

At a generic Gauss divisor near $p$, $\rho=ht+O(1)$ with $h\le0$,
and the reference coefficient is zero. Near $H$ this holds with
$h=v(H)\ge0$ and reference coefficient $h$. Elsewhere the
weights are bounded at a generic point. The leading total
coefficient is
\[
\lim_{t\to\infty}t^{-1}\sup_{0<x\le1}
\{xht-F_w(x)-t(x-a)_++O(1)\}
=\sup_{0\le x\le1}\{xh-(x-a)_+\}.
\tag{14}
\]
For the upper bound use a finite lower bound for $F_w$.
For the lower bound fix $x>0$, take the time limit, then approach
a possible optimizer zero. No infinite value $F_w(0)$ is divided
by time. For $h\le0$ the supremum is zero. For $h\ge0$, subtracting
the reference coefficient gives $-sh$ for $h\le1$, and $-s$
for $h\ge1$. Thus the actual datum is (7). All generic Gauss
coefficients and R's divisorial determination identify it on
the full original carrier. The pointwise value $w(p)=-\infty$
is never divided by time.

The moment top probability is $n x^{n-1}dx$. Bounded geodesic
energy differentiation yields
\[
E'(b_{s,t})=-\int_a^1(x-a)n x^{n-1}dx
=(1-a^{n+1})/(n+1)-s=e_s.
\tag{15}
\]
Pass through the bounded approximants by decreasing finite-energy
continuity. Its actual energy slope equals its actual model energy.
R's zero energy-defect criterion identifies (9) with $r(w,\eta_s)$
and at $s=1$ with $r(w,\phi)$.
The roofs increase to $x$, so the rays decrease; ordered distance
and energy prove (10).

### 4.3. Every level and its relative ceiling

Put $q=-\lambda\ge0$. Minimization in time imposes
$(x-a)_+\le q$, hence $x\le\min(1,a+q)$.
For $q>0$ a strictly feasible $x>0$ exists. Elementary convex
duality gives (11). Directly, the derivative of the convex time
objective is $q-(x_t-a)_+$. If the unconstrained moment satisfies
the constraint, time zero minimizes; otherwise the optimizing
moment moves to the boundary, giving the constrained value.

For $q=0,a>0$, letting $t\to\infty$ penalizes moments outside
$[0,a]$, leaving the supremum on $(0,a]$. For $q=a=0$ the
weight is $Q(\rho-t)-Q_0$ and tends to $-\infty$ at every
finite $\rho$; its value at $H$ is $-t$, so the whole level is
identically minus infinite. This proves the closed boundary
without a false strict-feasibility argument. For $\lambda>0$
the bound $b_{s,t}\le w$ gives the same placeholder.

For $d>0$ the optimizer in (11) is $Q'(\rho)$ if at most $d$,
and otherwise is $d$. The constrained total weight is $Q$
on its inner region and $d\rho-F_w(d)$ on the outer region.
At a subgradient interface both descriptions match with matching
first derivatives. It is convex and increasing, defining a
genuine global psh potential. Near $p$ it is exactly the original
$w$; its coefficient along $H$ is $1-d$. Lemma \ref{relative}
gives equality of its actual relative ceiling with $V_d$.

Expanding the radial and tangential Hessian eigenvalues and
polarizing, as in C, its mixed nonpolar radial distribution is
$d(Q_d'^kQ_0'^{\,n-k})$. Matching slopes give no interface
measure. Endpoint values are zero at $p$ and $d^k$ at infinity;
the ordinary divisorial part on $H$ is excluded by the nonpolar
product. Hence $M_k(V_d)=d^k$.

As $d_j\downarrow d>0$, compactness of the moment optimizer
gives $V_{d_j}\downarrow V_d$. For $d_j\downarrow0$, (5) gives
$V_{d_j}\downarrow-\infty$ at finite $\rho$, with the pole on
$H$ persistent. Since $0\le d_{s_j}-d_1\le1/j$, the derivative
bound for $d^k$ proves (12). For two genuine ordered types,
DDNL Lemma 3.4 gives, in volume one,
\[
d_S(V_d,V_{d'})=\frac1{n+1}\sum_{k=1}^n((d')^k-d^k)
\le\frac n2(d'-d),\quad 0<d\le d'\le1.
\tag{16}
\]
The zero-degree terms cancel. This proves the uniform interior
metric assertion, never evaluated with the placeholder $d=0$.
The actual ceilings, not masses or (16), carry the boundary claim.

DDNL writes its currents as $\theta+i\partial\bar\partial u$.
Use its potential $V_d/(2\pi)$ with the same background $\omega$;
the currents and raw mixed masses then coincide. We pull back its
singularity pseudometric along this correspondence. Its mass
formula (16) is unchanged; no slope of an uncalibrated analytic
ray is imported.

### 4.4. A uniform entropy remainder

For almost every $x$ define
$p_w(x)=e^{F'_w(x)}/(1+e^{F'_w(x)})$.
It equals $(1+e^{(3x)^{-3/2}})^{-1}$ for $x<\delta$ and $x$
for $x>\delta$; the corner has zero moment measure.
On an active interval
$\rho=F'_w(x)+t\mathbf1_{x>a}$ and the probability is
$n x^{n-1}dx$. Plateaus carry zero top mass.

For $p(\rho)=e^\rho/(1+e^\rho)$ the relative FS density is
$x^{n-1}/(F''_w(x)p(\rho)^{n-1}p'(\rho))$.
For $x<a$ this is the initial density. For $x>a$, subtracting
the initial log density gives
$t+(n+1)\log(p_w(x)+e^{-t}(1-p_w(x)))$. Therefore
\[
H(b_{s,t})=H(w)+t(1-a^n)
+(n+1)\int_a^1 n x^{n-1}
\log(p_w(x)+e^{-t}(1-p_w(x)))dx.
\tag{17}
\]
Every measure here is a probability. Interfaces have no top
atoms; C gives initial log-density integrability. The new log
term is between $\log p_w$ and zero. Set
\[
B_n=(n+1)\int_0^1 n x^{n-1}\log p_w(x)dx>-\infty.
\tag{18}
\]
Near zero its negative integrand is $O(x^{n-5/2})$, integrable
for $n>3/2$. Elsewhere it is integrable. This proves all
finite-time entropy statements, (13), and the joint limit
without entropy continuity for arbitrary strong sequences.
The theorem follows. \(\square\)


## 5. General fixed-start recovery and the arbitrary-ray distinction

For a fixed smooth compact Kähler manifold, let $H(w)<\infty$
and $H_\alpha(\phi)<\infty$. R gives actual relatively Kähler
data $\eta_j\to\phi$ strongly, with converging NA entropy.
Keep $w$ exactly and put $u_j=r(w,\eta_j)$ and $u=r(w,\phi)$.
For $\lambda_j=\max(\eta_j,\phi)$, the actual common upper
maximal ray $r(w,\lambda_j)$ gives
\[
d_1(u_{j,t},u_t)\le t B_j,\quad
B_j=2E_\alpha(\lambda_j)-E_\alpha(\eta_j)-E_\alpha(\phi)\to0.
\tag{19}
\]
Indeed the supporting inequality bounds
$0\le E_\alpha(\lambda_j)-E_\alpha(\phi)
\le\int|\eta_j-\phi|\MA_\alpha(\phi)\to0$
by R's strong finite-energy foundations. This reconstructs
bounded-time $d_1$ recovery, energy-slope recovery and individual
entropy-slope recovery with the actual start retained.
Finite-time entropy is finite: R gives finite recession slope
for entropy plus finite contracted energies and finite initial
value; geodesic convexity excludes an infinite intermediate value.
This proves no fixed-time entropy continuity, joint entropy
limit, or closed P-profile continuity in general.

Round140's stronger general joint entropy proof needs uniform
mixed-pairing estimates. Primary MP Lemma 5.3.2 requires mean-zero
slots and the constant-invariant relative $J$, not $d_1$ after
arbitrary constant changes. Its finite-energy proof passes
through decreasing continuity. We checked that normalization
issue but do not grant or reprove all of round140's joint
argument. The new theorem obtains its joint limit directly
from (17).

For an arbitrary nonmaximal ray $u$ from $w$, R gives energy
slope $c_u$ and defect
$\delta=E_\alpha(\phi)-c_u>0$, with
$d_1(r(w,\phi)_t,u_t)=t\delta$. Since energy is 1-Lipschitz
for $d_1$, the particular mechanism $r(w,\eta_j)$ with
$E_\alpha(\eta_j)\to E_\alpha(\phi)$ satisfies
\[
\liminf_{t\to\infty}
 d_1(r(w,\eta_j)_t,u_t)/t
\ge |E_\alpha(\eta_j)-c_u|\longrightarrow\delta.
\tag{20}
\]
Its bounded-time limit is the maximalization, by (19), not $u$.
This is a mechanism limitation, not universal nonexistence.
Original P19.2's arbitrary-ray branch is not discarded.

## 6. Critical reconstruction of round140's endpoint diagnostic

Round140's bad sequence is valid within T's exact scope.
For $j\ge2$ use roof heights $1/i$, interval lengths
$a_i=j^{-3}$ for $i<j$,
$a_j=1-j^{-1}-(j-1)j^{-3}$, and $c_j=1-j^{-1}$.
The rays $(1,i)$ already form a regular blowup chain.
T's geometry specializes to central multiplicities $1,i$ and
\[
D_j=\sum_{i=1}^j\left(-\sum_{k=1}^j
 a_k\min(1,i/k)\right)F_i,\qquad
\mathcal L_j=p_X^*\mathcal O(1)+D_j.
\]
Their component degrees are $1-c_j$ and $a_i/i$, all positive.
For a common denominator $M$ the actual ideal has the roof-node
monomials $z^{Mx}\tau^{Mg_j(x)}$ and $z^M$; the chain resolves
it with fixed divisor factor $-MD_j$.
Thus the models are actual and relatively ample.

Their norm and entropy $R_j=\sum a_i/i$ tend to zero, as do
their energies $-\int g_j$. The entropy remainder lies in
$[-2,0]$. Every fixed negative level is eventually exactly zero.
Nevertheless the endpoint is T's $w_{c_j}$, raw mass $1/j$,
at distance $c_j/2$ from the trivial target's endpoint zero.
This is an implication failure, not an existence obstruction:
the product sequence works for the trivial target.

Round140's infinite-chain two-moment replacement has positive
finite coefficients when $1/N<R'/T'<1/m$. Its exact endpoint
quantifier differs from eventual equality at each fixed interior
parameter. The accompanying program checks the finite arithmetic;
we do not promote the unreviewed theorem beyond its zero-start,
one-chain, positive-endpoint scope. T already grants closed
finite-height zero-start profiles including zero mass, and no
additional-start extension.

The round140 curve warning has infinite initial entropy.
C is its finite-initial-entropy replacement in dimension at least
two. C changes absolute endpoint data even though both raw top
masses are zero. The new theorem constructs a sequence for
C's very singular start and its actual relative endpoint.
C therefore supplies no general approximation nonexistence theorem.

## 7. Source versions, read scopes and applications

The complete R, T, C and round140 mathematical bodies were read
in the prompt and extracted into the supplied directory. Historical
verdict sentences were not premises. Public primary retrievals
are saved under sources. Read scope means exactly returned layout
lines, not full PDFs or recursive foundations.
The source-application-ledger.json records premises, domains
and rejected transports.

**DDNL, primary arXiv:1909.00839v1, Lemma 3.4.** For ordered genuine
types in a big class, the pseudodistance is the sum of their
mixed nonpolar mass differences divided by $n+1$.
The statement at layout lines 1248--1267 and preceding energy
construction 977--1247 were read. Formula (16) applies in
volume one to ordered genuine $V_d$, $d>0$. This is the sole
new external metric theorem used in the explicit construction;
it is not applied to $-\infty$. The fetched first page identifies v1, 2 September 2019; the
versioned v1 URL was then read at the same lemma.

**DXZ, arXiv:2302.02541v3.** The relative ceiling uses
$\lim_C P_\theta(u+C,v)$; the I-envelope instead imposes
multiplier-ideal inclusions. Its displayed model-test definition
uses the absolute ceiling against $V_\theta$; model initial
limits follow from Lemma 2.7. We read the pertinent definitions
and Legendre units but apply no singular-start approximation or
entropy theorem from them. Replacing their model initial limit
by arbitrary unbounded $w$ is unjustified. Our lemma is direct.

**DZ, arXiv:2509.15173v2.** Formula (11) defines
$\mathcal L_\beta=\mathcal L+\beta^{-1}C$, which need not be
relatively semiample. Formula (65) and Remark 9.2 give its datum
as $P_\alpha(\phi_\mathcal L+\beta^{-1}A_X\circ r_\mathcal X)$.
Theorem 10.1, whose full proof at 4621--4742 was read, gives
chordal and radial entropy recovery for zero-start rays in the polarized
finite-radial-entropy domain. These units provide no prescribed
closed relative boundary or general transcendental extension.
They are scope comparisons, not premises of the explicit theorem.

**MP and MPWN, exact v2 and v1 listed in R.** We freshly read
MP's mean-zero mixed estimate and finite-energy proof to check
round140's normalization, and MPWN's constructive Theorem 9.2.1
proof to check that its recovery uses dual-complex measures,
the Calabi--Yau map and PL obstacles. This adds no decreasing
relatively Kähler sequence with controlled relative boundary.
R remains the theorem premise for (19)--(20); no independent
full reproof of its external chain is claimed.

No catalogue claim alone supplies a theorem. No other campaign's
contents were accessed. An initial directory listing of /tmp
exposed unrelated filenames only; none was opened or used.
All substantive local reads and writes are in this fresh directory.
No agents, campaigns, or heavy compute were launched, and no model,
account, authentication, proxy or runtime settings were changed.

## 8. Remaining gaps for the entire unchanged P19.2

The explicit theorem retains one unbounded finite-entropy start
and its complete relative closed profile, but is confined to a
radial hyperplane signature on projective space and maximal rays.
The original atom's completion criteria are unmet.

Indispensable unresolved work includes:

- A simultaneous construction for arbitrary prescribed finer P
  data and arbitrary finite-energy starts on general compact
  Kähler manifolds.
- General boundary and raw mixed-mass continuity, with
  nontrivial zero-mass and identically minus-infinite levels
  retained as distinct data.
- Arbitrary nonmaximal actual weak-ray approximation that
  retains the ray rather than maximalizing it.
- Exact log-discrepancy regularization and cohomological model
  meanings beyond the primary polarized domains, with the
  additional P data.
- Fixed-time entropy or genuinely hybrid measure-continuity
  conclusions required beyond the explicit radial construction.

No new completion of granted P19.1 or solution of P19.3/P19.4
is counted. Known polarized Fujita regimes remain established
subcases. The task and assignment are unchanged;
**candidate=false**.

## 9. Reproducibility and evidence

The original input and its frozen copy are byte-identical, with SHA256:

~~~text
8091f3850fac62aa854cddb44ccfffa97e2cde151d2995b3b1aa4dab52da5c4b
~~~

The exact decoded task and assignment are in task-original.json
and assignment-original.txt. From this directory rerun:

~~~text
python prepare_input.py
python check_models.py
python build_paper.py
python validate_deliverables.py
~~~

The extraction script retains complete supplied units and environment.
The check script separates exhaustive finite rational identities
from floating-point entropy observations. Build commands, outputs,
exit statuses and LaTeX logs are retained. Validation checks input
preservation and artifact structure. No relevant supervised
heavy-compute service was exposed; none was needed.
Arithmetic, quadrature and compilation do not certify analytic proofs.
All new arguments remain unverified research drafts.

## References

- R. Complete supplied entropy theorem, 6 October 2026.
- T. Complete supplied closed one-branch zero-start toric theorem,
  6 October 2026.
- C. Complete supplied finite-entropy absolute endpoint
  counterexample, 6 October 2026.
- Round140. Complete supplied unreviewed partial manuscript.
- T. Darvas, E. Di Nezza and C. H. Lu, *The metric geometry of
  singularity types*, [primary arXiv:1909.00839v1](https://arxiv.org/pdf/1909.00839v1),
  Lemma 3.4.
- T. Darvas, M. Xia and K. Zhang, *A transcendental approach to
  non-Archimedean metrics of pseudoeffective classes*,
  [arXiv:2302.02541v3](https://arxiv.org/pdf/2302.02541v3),
  relative definitions and Section 2.2; scope comparison.
- T. Darvas and K. Zhang, *A YTD correspondence for constant
  scalar curvature metrics*,
  [arXiv:2509.15173v2](https://arxiv.org/pdf/2509.15173v2),
  formula (11), Section 9, Theorem 10.1; scope comparison.
- P. Mesquita-Piccione, *A non-Archimedean theory of complex spaces
  and the cscK problem*,
  [arXiv:2409.06221v2](https://arxiv.org/pdf/2409.06221v2),
  Lemma 5.3.2; normalization check.
- P. Mesquita-Piccione and D. Witt Nyström, *A transcendental
  non-Archimedean Calabi--Yau theorem with applications to the cscK
  problem*, [arXiv:2509.09442v1](https://arxiv.org/pdf/2509.09442v1),
  proof of Theorem 9.2.1; scope comparison.

END COMPLETE MATHEMATICAL GRANT
