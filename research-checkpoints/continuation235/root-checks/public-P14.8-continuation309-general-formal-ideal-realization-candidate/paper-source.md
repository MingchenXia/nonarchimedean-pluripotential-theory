# Complete author TeX source (source-derived Markdown)

This fenced copy is the full mathematical argument, not a typeset conversion.

```tex
\documentclass[11pt]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern,amsmath,amssymb,amsthm,mathtools}
\usepackage[margin=1in]{geometry}
\usepackage[hidelinks]{hyperref}
\usepackage{longtable,array}
\newcommand{\ddc}{\frac{i}{2\pi}\partial\bar\partial}
\newcommand{\I}{\mathcal I}
\newcommand{\A}{\mathcal A}
\newcommand{\OO}{\mathcal O}
\newcommand{\PSH}{\operatorname{PSH}}
\newcommand{\supp}{\operatorname{supp}}
\newcommand{\ord}{\operatorname{ord}}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}
\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{remark}[theorem]{Remark}
\title{Formal multiplier-ideal arrays and finite norm certificates\\
\large A geometric and integral realization criterion in a pseudoeffective class}
\author{Independent author draft for original P14.8}
\date{8 October 2026}
\begin{document}
\maketitle
\begin{abstract}
For a connected compact K\"ahler manifold and a fixed smooth closed
real $(1,1)$-form $\theta$, we give an infinite witness criterion for
an arbitrary array of nonzero coherent ideals, indexed by all real
$c>0$, to equal $\I(cu)$ for some $\theta$-psh function $u$.
Witnesses are finite holomorphic ideal norms with specified geometric
smooth terms and finite maximum gluing, vanishing curvature loss,
and a uniform integral test involving only finite maxima and bounded
weights. The decreasing upper tails recover a realization, with no
mass assumption. Necessity is proved by local weighted Bergman spaces:
we prove exact ideal generation, a finite relative kernel reduction,
and fixed-cover gluing using exact local potentials of $\theta$.
The reconstructed raw function depends on the witness. A direct
Cantor construction on $\mathbf P^1$ preserves the failure of raw
mass and representative recovery from ideal data. We also exhibit
and separately correct an exponent-direction error in the frozen
book data. This is an author claim of the formal-data alternative,
subject to independent review, using explicitly stated published
ordinary complex-analytic theorems. It is not an acceptance decision
or a claim that all those theorems were checked in their original
primary editions.
\end{abstract}
\tableofcontents

\section{Problem, conventions, and the type of answer}
Let $X$ be connected and compact K\"ahler of complex dimension $n\geq1$,
let $\omega$ be K\"ahler, and let $\theta$ be a smooth closed real
$(1,1)$-form representing a pseudoeffective class. Write
$dd^c=(i/2\pi)\partial\bar\partial$. A $\theta$-psh function has its
canonical upper semicontinuous representative, satisfies
$\theta+dd^cu\geq0$, and is not identically $-\infty$.
Our ideal convention is
\begin{equation}\label{eq:ideal}
 \I(cu)_x=\{f\in\OO_{X,x}: |f|^2e^{-cu}\text{ is locally integrable}\}.
\end{equation}
Integration uses a fixed smooth strictly positive volume $dV$; its
choice does not change local integrability. In tests a representative
of a germ must be holomorphic on a neighborhood of the closure of the
coordinate ball being used. The zero germ is always included.

Our input is the full array $(\A_c)_{c\in\mathbf R_{>0}}$ of nonzero
coherent ideal sheaves. This fixes the index convention rather than
silently identifying integer and real data. A separate integer-index
version follows by restricting the test, but we make no assertion
that arbitrary integer formal arrays determine a real extension.
The witness scales may be fixed in advance as $m_j=2^j$, $j\geq1$.

The question is existence of a realization of arbitrary formal data,
not recovery of a specified raw potential. We do not define
``admissible'' as existence of a target psh function. The witness
class and every test below are specified without such a target.
There is no finite decision procedure claim. The main content of the
reverse implication is the exact regularization interface in
Section~\ref{sec:R}; mere analytic singularities of unspecified
ideals would not suffice.

\section{Declared analytic inputs and evidence boundaries}\label{sec:inputs}
The following are ordinary published analytic inputs, not caller
grants or conclusions inferred from production histories.
Their exact specializations are recorded because they carry real
analytic content.
\begin{enumerate}
\item[(H)] \textbf{H\"ormander's weighted solution theorem.}
On a bounded pseudoconvex domain $D\subset\mathbf C^n$, if $W$ is
psh, possibly singular, with
$i\partial\bar\partial W\geq i\partial\bar\partial|z|^2$, then a
$\bar\partial$-closed $(0,1)$-form $a$ with
$\int_D|a|^2e^{-W}<\infty$ has a solution $\bar\partial h=a$ with
$\int_D|h|^2e^{-W}\leq\int_D|a|^2e^{-W}$, with the Euclidean
norm convention. The usual singular-weight version is obtained by
psh approximation, exhaustion and weak $L^2$ limits. This is the
specialization of the weighted $L^2$ theorem of
H\"ormander~\cite{H65,H90}; we require it for smooth compactly
supported data and weights equal to a psh weight plus a logarithmic
point pole and a fixed strictly psh quadratic.
\item[(O)] \textbf{Point Ohsawa--Takegoshi extension.}
For a Euclidean ball $D$, a compact $K\Subset D$, a psh weight $W$
on $D$, and $x\in K$ with $W(x)>-\infty$, there exists
$F\in\OO(D)$, $F(x)=1$, such that
\[
 \int_D|F|^2e^{-W}\leq C(D,K,n)e^{-W(x)}.
\]
The constant is independent of $W$ and $x$. This is the point
specialization (or iteration along coordinate slices) of
\cite{OT87}. The point-pole interpretation at $W(x)=-\infty$
will only be the trivial inequality $0\leq K_W(x)$.
\item[(N)] \textbf{Multiplier-ideal coherence.}
For a nontrivial psh weight $v$ on a domain, the ideal of holomorphic
germs integrable against $e^{-v}$ is a nonzero coherent analytic
ideal. Smooth locally bounded changes of weight leave it unchanged.
This is Nadel's coherence theorem~\cite{N90}; the invariance is also
immediate from comparison of the weights.
\item[(C)] \textbf{Coherent analytic modules on Stein domains.}
A coherent ideal's holomorphic sections are closed in the
compact-open topology. For a finite tuple of global generators of
a coherent ideal $J$ on a Stein domain $V$, the map
$\OO(V)^s\longrightarrow J(V)$ is surjective. The latter is Cartan
theorem B applied to the coherent kernel. The spaces in this assertion
are Fr\'echet spaces, $J(V)$ with the induced closed-subspace topology;
the continuous linear surjection is open. We use the same assertions
on a product of balls. Coherence and Cartan B are the ordinary analytic
sheaf inputs described in Grauert--Remmert~\cite{GR84} and
Narasimhan~\cite{Nar66}; openness is the Banach--Fr\'echet open mapping
theorem. No norm estimate uniform in a changing ideal is assumed.
\end{enumerate}
We also use local smooth potentials for a closed smooth real $(1,1)$
form, the elementary mean-value inequality for psh functions, the
canonical psh representative of an $L^1$ distribution with positive
$dd^c$, and the algebraic Artin--Rees and Nakayama lemmas in the
Noetherian local ring $\OO_{X,x}$. The relevant envelope and monotone
arguments are given below, rather than assuming continuity of
multiplier ideals under limits.

Two further published inputs are used only for an obstruction example
and the source correction: subadditivity
$\I(v+w)\subset\I(v)\I(w)$ for psh weights~\cite{DEL00}, and strong
openness $\I(v)=\bigcup_{\delta>0}\I((1+\delta)v)$~\cite{GZ15}.
For quasi-psh weights one adds a smooth local psh correction first;
bounded changes leave ideals unchanged. Neither theorem is needed
for the main realization proof or its necessity construction.

The bound DPS primary is arXiv math/0006205v2, 10 October 2000,
not an asserted byte-identical publisher 2001 version. Its whole
Section 2.2 through Remark 2.2.13 was read in literal newline
records 404--775, including all four proof steps. The available
text directly exhibits the use of (H), (O), and coherent-ideal
closedness; it does not contain the full original proofs of those
inputs. Bibliographic entries give identities, not theorem
verification. Our proof below supplies the new interface arguments;
the deeper ordinary inputs remain explicitly imported. Primary
source closure for (H), (O), (N), and (C) is not claimed.

\section{Finite formulas and the certificate}\label{sec:certificate}
Here is a concrete class of permitted finite norm formulas. Choose
a finite coordinate-ball atlas, with nested balls
\[
 B_a^0\Subset B_a^1\Subset B_a^2\Subset B_a^3,
 \qquad \bigcup_a B_a^0=X,
\]
and specified known smooth local potentials $\rho_a$ with
$dd^c\rho_a=\theta$ on a neighborhood of $\overline{B_a^3}$.
These are geometric data fixed independently of an unknown target.
Choose specified smooth barriers $\beta_a$ on $B_a^1$, and finite
constants $L,A$. A basic formula at integer scale $m$ is
\begin{equation}\label{eq:finite}
 \Phi_m(x)=\max_{a:x\in B_a^1}
 \left\{\frac1m\log\sum_{\ell=1}^{s_{m,a}}|g_{m,a,\ell}(x)|^2
       -\rho_a(x)+\frac{L\beta_a(x)+A}{m}\right\}.
\end{equation}
The tuple $g_{m,a,\ell}$ is finite, holomorphic on $B_a^3$, and
generates exactly $\A_m$ on a neighborhood of
$\overline{B_a^2}$, not merely an ideal of the same zero set.
For gluing one requires that branches at patch boundaries can be
omitted on a neighborhood, or that the branches extend and agree
there. This is an explicit condition on the known branches; the
necessity construction proves a strict domination version.

Finite sums, maxima, and specified smooth Hermitian ideal norms with
their explicit chart transition formulas are equivalent permitted
presentations. In particular the globally agreeing case $L=A=0$
is allowed. The geometric smooth functions must be given as known
data with a formula or specified geometric construction; an
arbitrary unknown locally bounded or quasi-psh correction is not
an allowed quantified witness. Section~\ref{sec:R} proves necessity
in the rigid subclass \eqref{eq:finite}, with $\rho_a,\beta_a,L,A$
fixed once for the geometry. Thus enlarging the class to unspecified
corrections is unnecessary.

Every such formula has local ideal-norm type
\[
 \Phi_m=\frac1m\log\sum|h_\ell|^2+b,
\]
where $h$ is any finite local generating tuple of $\A_m$, and the
correction $b$ is a specified finite expression from the displayed
branches and smooth terms. It is locally bounded off the zero set
and extends boundedly across it. Indeed two tuples generating the
same coherent ideal have bounded ratios of their squared norms on
smaller relatively compact sets: express each tuple holomorphically
in terms of the other. Maximum gluing preserves that comparison.
At a common zero all branches take $-\infty$; define the bounded
correction there by any bounded extension. Equality of singular
functions is unaffected. No regularity of that bounded extension
is used as a hidden curvature premise.

\begin{definition}\label{def:cert}
A finite norm certificate for $\A$ is a sequence of permitted
formulas $\Phi_j=\Phi_{m_j}$, $m_j=2^j$, together with finite $B$
and $\epsilon_j\downarrow0$, satisfying the explicitly asserted
current and supremum inequalities
\begin{equation}\label{eq:curv}
 \theta+dd^c\Phi_j\geq-\epsilon_j\omega,
 \qquad -B\leq\sup_X\Phi_j\leq B.
\end{equation}
No decrease of the individual $\Phi_j$ is required. Set the known
finite maximum $H_{j,N}=\max_{j\leq k\leq N}\Phi_k$.
For every $x$, every real index $c>0$, and every holomorphic germ
$f$ at $x$, impose
\begin{equation}\label{eq:test}
 f\in\A_{c,x}\quad\Longleftrightarrow\quad
 \begin{gathered}
 \text{there exist a coordinate ball }x\in U\Subset X
 \text{ and }C<\infty\text{ such that}\\
 \text{for all }j\geq1\text{ and integers }R\geq1,\qquad
 \lim_{N\to\infty}\int_U|f|^2
       \min\{R,e^{-cH_{j,N}}\}\,dV\leq C.
 \end{gathered}
\end{equation}
The representative of $f$ is holomorphic near $\overline U$.
The constant and ball may depend on $x,c,f$, but not on $j,R$.
\end{definition}
For each fixed $j,R$ the $N$ limit exists: its nonnegative
integrands decrease and are bounded by $R|f|^2\in L^1(U)$.
At $H=-\infty$ the truncated weight is $R$. At a simultaneous zero
of $f$ it is multiplied by zero. Untruncated products are defined
by these caps, removing the expression $0\cdot\infty$; polar
sets have volume zero in any case.

\begin{theorem}[Formal-data realization criterion]\label{thm:main}
Under the stated ordinary analytic inputs, the full real array
$\A$ equals $(\I(cu))_{c>0}$ for some $u\in\PSH(X,\theta)$
if and only if it has a finite norm certificate in
Definition~\ref{def:cert}. From any certificate one obtains a
realization by
\begin{equation}\label{eq:reconstruct}
 \Psi_j=\left(\sup_{k\geq j}\Phi_k\right)^*,
 \qquad u=\lim_{j\to\infty}\Psi_j.
\end{equation}
The limit is nontrivial, is $\theta$-psh, and realizes every index,
not just the witness scales. Different certificates can give
different raw $u$. No positive top nonpluripolar mass is needed.
\end{theorem}

\section{Sufficiency: envelopes, noncollapse, and integration}\label{sec:suff}
We give the analytic details of \eqref{eq:reconstruct}.
\begin{lemma}[Countable envelope, including its almost everywhere identity]
Let $p_N$ increase, be $\eta$-psh for one smooth closed $\eta$,
be locally uniformly bounded above, and have a locally integrable
lower bound $p_1$. Then $s=\sup_Np_N$ is locally integrable,
$s^*$ is $\eta$-psh, and $s=s^*$ almost everywhere.
\end{lemma}
\begin{proof}
On a coordinate ball write $\eta=dd^c\rho$. Local upper bounds
and $p_1\in L^1$ dominate $|p_N|$, so dominated convergence gives
$p_N\to s$ in local $L^1$. Distributional positivity passes to
the limit. Let $v$ be its canonical $\eta$-psh representative.
Each $p_N\leq v$ almost everywhere, hence everywhere: add $\rho$
and recover values by limits of averages of psh functions. Thus
$s\leq v$ and $s^*\leq v$. Conversely the canonical value of
$v+\rho$ is a limit of averages of $s+\rho$, bounded by local
suprema; as the radius shrinks this gives $v\leq s^*$. Hence
$s^*=v=s$ almost everywhere. Smooth local potentials reconcile
the representatives on overlaps.
\end{proof}

\begin{lemma}[Decreasing noncollapse]
Suppose $p_j$ decrease on connected compact $X$, are
$(\theta+\epsilon_j\omega)$-psh, satisfy $p_j\leq B$, and
$\sup_Xp_j\geq-B$. Then their pointwise limit is nontrivial,
$\theta$-psh, and $p_j\to p$ in $L^1(X)$.
\end{lemma}
\begin{proof}
The compact sets $K_j=\{p_j\geq-B-1\}$ are nonempty and
nested. Their intersection contains $x_0$, so $p(x_0)>-\infty$.
All $p_j$ have the common lower curvature bound
$-(\theta+\epsilon_1\omega)$. Add a fixed smooth local potential
of this form to obtain decreasing psh functions on each ball.
We recall why the usual decreasing-sequence dichotomy gives the
required $L^1$ conclusion. For psh functions bounded above by $M$
with a common lower value at a point, the sub-mean inequality
bounds the integral of $M-v_j$ on a ball centered there. Such
an integral bound propagates along a chain of overlapping balls:
on a fixed positive-volume relatively compact overlap it supplies
a point, possibly depending on $j$, with a common lower value;
the sub-mean inequality on a ball about that point bounds the
negative part on a fixed smaller ball of the next chart. Distances,
volumes and smooth local-potential differences are bounded in a
finite chain. A finite connected cover therefore gives uniform
local $L^1$ bounds. Equivalently, this proves the local dichotomy
``decreasing psh limit is psh or identically $-\infty$'' and
propagates its nontrivial branch from $x_0$.

Now $M-v_j$ increases and has bounded integral. Monotone convergence
gives a locally integrable limit and $L^1$ convergence. The pointwise
limit is upper semicontinuous. Passing the sub-mean inequalities to
the limit and using the canonical average representative shows
that the pointwise and distributional psh limits agree. Positivity
of $\theta+\epsilon_j\omega+dd^cp_j$ passes in distributions to
$\theta+dd^cp\geq0$. Compactness globalizes $L^1$ convergence.
This argument uses only sequences, not an unproved net selection.
\end{proof}
For precision in the propagation argument, choose a finite chain of
small chart balls whose successive centers have distance less than a
quarter of a chosen radius, with a much larger ball still contained in
the chart. A quarter-radius ball about the next center lies inside
the preceding half-radius ball. An integral bound on this smaller
overlap, with fixed positive volume, supplies a point $y_j$ where the
next chart's psh function is uniformly bounded below; smooth potential
differences on the overlap are bounded. A radius-$r$ ball about $y_j$
contains the next half-radius ball and stays in the larger chart ball.
The sub-mean inequality therefore bounds its negative-part integral.
At a chart transition take the overlap compactly inside both charts
and repeat with smaller radii. Only finitely many transitions are
needed. All radii and volumes are fixed independently of $j$, so
the resulting constants are uniform. This spells out the usual
decreasing-sequence dichotomy used in the lemma.

For fixed $j$, every $H_{j,N}$ is
$(\theta+\epsilon_j\omega)$-psh: add a local smooth potential and
take the maximum of finitely many psh functions. The preceding
envelope lemma, with lower bound $\Phi_j$, proves that $\Psi_j$
has the same curvature bound and agrees almost everywhere with the
raw supremum. The $\Psi_j$ decrease and
$\sup_X\Psi_j\geq\sup_X\Phi_j\geq-B$. The noncollapse lemma
therefore constructs the asserted $u$.

Fix $c,f,U$. The capped $N$ integrands are dominated by
$R|f|^2$, so dominated convergence, followed by the almost
everywhere identity, gives
\begin{equation}\label{eq:Nlimit}
 \lim_N\int_U|f|^2\min\{R,e^{-cH_{j,N}}\}\,dV
 =\int_U|f|^2\min\{R,e^{-c\Psi_j}\}\,dV.
\end{equation}
Monotone convergence as integer $R\to\infty$ gives the uncapped
integral, possibly infinite. Since $\Psi_j\downarrow u$,
monotone convergence a second time yields
\begin{equation}\label{eq:integralidentity}
 \sup_{j,R}\lim_N\int_U|f|^2\min\{R,e^{-cH_{j,N}}\}\,dV
 =\int_U|f|^2e^{-cu}\,dV.
\end{equation}
This identity includes infinite values. It proves
$\I(cu)_x=\A_{c,x}$ for every $c$ by precisely the local-ball
quantifiers in \eqref{eq:test}. No interchange of an intersection
of ideals with a decreasing limit, and no strong openness, is used.

\section{Exact regularization interface R}\label{sec:R}
We now prove the reverse implication rather than importing it from
the final equisingular DPS theorem.
\begin{theorem}[Finite ideal norms with exact upper-tail limit]\label{thm:R}
For every $u\in\PSH(X,\theta)$, there are finite formulas
\eqref{eq:finite}, at every sufficiently large integer $m$ (indeed
at every positive integer after enlarging harmless constants),
whose local generating ideals are exactly $\I(mu)$ and such that
\[
 \Phi_m\geq u,\qquad
 \theta+dd^c\Phi_m\geq-\frac{C_0}{m}\omega,
 \qquad -B\leq\sup_X\Phi_m\leq B.
\]
For any increasing unbounded integer sequence, their upper-tail
envelopes decrease exactly to $u$, at finite and polar points alike.
The formula uses only finite holomorphic tuples and specified
geometry. The target $u$ is used to prove existence of those tuples,
and does not appear in the certificate tests.
\end{theorem}

\subsection{Exact generation by a weighted Hilbert space}
Let $D$ be a coordinate ball, $v=u+\rho$ psh there, and
\[
 \mathcal H_m(D,v)=\{F\in\OO(D):
          \|F\|_m^2=\int_D|F|^2e^{-mv}\,d\lambda<\infty\}.
\]
Its members have germs in $I=\I(mv)=\I(mu)$.
\begin{lemma}\label{lem:generate}
The germs of members of $\mathcal H_m(D,v)$ generate exactly $I$
at every point of $D$. On any smaller closed concentric ball,
a finite family of members generates $I$ on a neighborhood of that
closed ball.
\end{lemma}
\begin{proof}
Fix $x$. By (N), $I_x$ is a finite module over the Noetherian local
ring $\OO_x$. Artin--Rees supplies an integer $q\geq0$ with
\[
 I_x\cap\mathfrak m_x^{q+1}\subset\mathfrak m_x I_x.
\]
For a local germ $g\in I_x$, shrink its representative domain so
that $\int|g|^2e^{-mv}<\infty$, and take a smooth cutoff $\chi$
supported there and equal to one near $x$. Apply (H) on $D$ to
$\bar\partial(\chi g)$ and the weight
\[
 W=mv+(n+q)\log|z-x|^2+|z|^2.
\]
This weight is psh and has the required strict Hessian lower bound.
The data are supported away from $x$, so their weighted norm is
finite. Obtain $h$ with $\bar\partial h=\bar\partial(\chi g)$.
It is holomorphic near $x$. Since $v$ is locally bounded above,
weighted integrability forces $\ord_xh\geq q+1$; a Taylor term of
degree $k$ would give a radial power integral finite only if
$k>q$. Also $h\in I_x$ and $h\in L^2(e^{-mv})$, since the added
factors in the weight are bounded above on the bounded domain.
Then $F=\chi g-h$ is in $\mathcal H_m$, and
$F_x\equiv g\pmod{\mathfrak m_xI_x}$.

Do this for a finite set of generators of $I_x$. Nakayama gives
generation by the resulting global $F$ germs. By coherence, the
cokernel of the finite generated subideal in $I$ vanishes on a
neighborhood of $x$. Finitely many such neighborhoods cover the
smaller closed ball; combining the finite tuples proves the claim.
This also proves that ``all weighted sections'' generate the ideal,
without replacing exact generation by containment in it.
\end{proof}

\subsection{Finite relative reduction of a Bergman kernel}
The diagonal Bergman kernel is
\[
 K_m(z)=\sum_{\ell\geq1}|f_{m,\ell}(z)|^2
       =\sup_{\|F\|_m\leq1}|F(z)|^2
\]
for an orthonormal basis of $\mathcal H_m$. Mean values bound the
evaluation and its derivatives on compact subsets, because $v$
has a finite local upper bound. Thus evaluation is norm-continuous
in $z$, $K_m$ is continuous, and the kernel series converges
normally on products of compact subsets (use Cauchy--Schwarz and
the uniform convergence of its diagonal tails).

\begin{lemma}\label{lem:finite}
For $E\Subset D$ a smaller closed concentric ball and any
$\delta>0$, one can choose a finite orthonormal tuple from
$\mathcal H_m$, generating exactly $I$ near $E$, whose sum $P_m$
satisfies
\begin{equation}\label{eq:relative}
 P_m\leq K_m\leq(1+\delta)P_m\quad\text{on }E.
\end{equation}
No bound on the number of generators is asserted.
\end{lemma}
\begin{proof}
Choose a concentric Stein ball $V$ with $E\Subset V\Subset D$
on which a finite Hilbert-space tuple generates $I$, using
Lemma~\ref{lem:generate} on a slightly larger closed ball. Put
that tuple's finite-dimensional span first in an orthonormal basis;
call its first $s$ members $f_1,\ldots,f_s$. A constant change of
basis preserves exact ideal generation. On
$V\times\overline V$ (the second factor means the conjugate complex
domain), the coherent ideal
\[
 J=p_1^{-1}I\cdot p_2^{-1}\overline I\,\OO_{V\times\overline V}
\]
is generated by the $s^2$ products $f_a(z)f_b^*(w)$, where
$f_b^*(w)=\overline{f_b(\bar w)}$ is holomorphic.
For $N\geq s$, the holomorphic kernel tail
\[
 T_N(z,w)=\sum_{\ell>N}f_\ell(z)f_\ell^*(w)
\]
belongs to $J(V\times\overline V)$: finite partial tails belong
to $J$, and closedness in (C) preserves membership under normal
convergence. Moreover $T_N\to0$ in its induced Fr\'echet topology.

By Cartan B, the coefficient map
$\OO(V\times\overline V)^{s^2}\to J(V\times\overline V)$ is
surjective and open. Consequently, for all sufficiently large $N$
there are coefficients $a_{ab,N}$ for $T_N$ with
\[
 \sup_{E\times\overline E}|a_{ab,N}|<\delta/s.
\]
This follows directly by applying openness to the neighborhood
defined by these finitely many compact seminorm bounds; it assumes
no uniform division estimate in $m$.
On the conjugate diagonal $w=\bar z$,
\[
 0\leq K_m-P_N
 \leq\frac\delta s\Big(\sum_{a=1}^s|f_a|\Big)^2
 \leq\delta\sum_{a=1}^s|f_a|^2\leq\delta P_N.
\]
Here $P_N=\sum_{\ell\leq N}|f_\ell|^2$. The first $s$ functions
already generate $I$, so adding the others leaves it unchanged.
This proves \eqref{eq:relative}, including points where both sides
vanish. Merely obtaining $K_m\leq C_mP_N$ with an uncontrolled
$C_m$ would not prove the theorem; the relative bound is the
essential improvement.
\end{proof}

\subsection{Exact smooth potentials and fixed-cover overlap estimates}
Fix the nested finite cover from Section~\ref{sec:certificate} and
put $v_a=u+\rho_a$. Use weighted kernels on $B_a^3$.
Set $Q_{m,a}=m^{-1}\log K_{m,a}-\rho_a$.
\begin{lemma}\label{lem:overlap}
There is a geometric $C\geq1$, independent of $u,m$, such that
on $\overline{B_a^2}\cap\overline{B_b^2}$
\begin{equation}\label{eq:overlap}
 C^{-1}K_{m,a}e^{-m\rho_a}
 \leq K_{m,b}e^{-m\rho_b}
 \leq C K_{m,a}e^{-m\rho_a}.
\end{equation}
The inequalities include zero values. Thus the finite sums in
Lemma~\ref{lem:finite}, taken with $\delta=1$, have corrected
logarithms $q_{m,a}=m^{-1}\log P_{m,a}-\rho_a$ differing by at
most $D/m$, $D=\log(2C)$, on finite-valued overlap points, and
obey the corresponding extended inequalities everywhere.
\end{lemma}
\begin{proof}
For an overlap point $x$, take a ball of fixed uniformly positive
radius about $x$ inside $B_a^3\cap B_b^3$; compactness of the
inner overlaps gives uniform choices. On that ball,
$\rho_b-\rho_a$ is pluriharmonic. There is a holomorphic $t$
with $\operatorname{Re}t=\rho_b-\rho_a$.
For $F\in\mathcal H_m(B_a^3,v_a)$ and a cutoff $\chi=1$ near
$x$ supported in the common ball, solve on $B_b^3$
\[
 \bar\partial h=\bar\partial(\chi F e^{mt/2})
\]
using the weight
$W=mv_b+n\log|z_b-z_b(x)|^2+|z_b|^2$.
The cutoff derivatives, the pole factor on their support, and
coordinate volume comparisons have uniform bounds. Crucially,
\[
 |F e^{mt/2}|^2 e^{-mv_b}=|F|^2e^{-mv_a}
\]
on the support, an exact identity rather than a Taylor estimate
with fixed curvature error. The weighted solution has norm at
most a geometric multiple of $\|F\|_{m,a}$, and the point pole
forces $h(x)=0$. Thus
$F_b=\chi Fe^{mt/2}-h\in\mathcal H_m(B_b^3,v_b)$ has
$F_b(x)=F(x)e^{mt(x)/2}$ and
$\|F_b\|_{m,b}^2\leq C\|F\|_{m,a}^2$.
Taking evaluation suprema gives the left inequality of
\eqref{eq:overlap}; interchange $a,b$ for the right. All added
weight factors are bounded above on the destination ball, so its
uncorrected weighted norm is controlled. Constants are independent
of $m$ because the holomorphic exponential cancels the smooth
potential difference exactly and is not differentiated by
$\bar\partial$. Finite relative reduction changes the ratio by
at most $2$, giving $D$.
\end{proof}

This use of closedness of $\theta$ is deliberate. It proves a
fixed-cover statement for our problem, without invoking the
DPS Step 3 almost decrease for varying covers or arbitrary
continuous lower forms.

\subsection{Upper and lower estimates and explicit gluing}
By (O), on $\overline{B_a^2}$
\[
 K_{m,a}(x)\geq C_{O,a}^{-1}e^{mv_a(x)}.
\]
With finite reduction at $\delta=1$, this implies
$q_{m,a}\geq u-m^{-1}\log(2C_{O,a})$. Choose
$C_O\geq1$ for all patches and $A=\log(2C_O)$.
The inequality extends trivially to $u(x)=-\infty$.
The mean-value upper bound, for a small coordinate radius $r$,
is
\begin{equation}\label{eq:upper}
 q_{m,a}(x)\leq
 \sup_{|z_a(y)-z_a(x)|<r}u(y)+M_\rho r
 +\frac{\log C'+2n\log(1/r)}m.
\end{equation}
Indeed apply the mean-value inequality to $|F|^2$, bound its
unweighted integral by $e^{m\sup v_a}\|F\|_m^2$, take the
evaluation supremum, and subtract $\rho_a(x)$.
Smooth local potentials have a common derivative bound on the
finite cover. Shrinking $r$ if necessary makes the numerator
positive. The estimate holds uniformly at nearby points.

Choose the radii so that $B_a^0$ has radius at most half that of
$B_a^1$, and put
$\beta_a=1-|z_a|^2/(r_a^1)^2$. It is nonnegative on $B_a^1$,
zero at its boundary, and at least $3/4$ on $B_a^0$.
Take $L=4(D+1)$. Use the formula \eqref{eq:finite} with these
finite $P_{m,a}$ and constants. Near a boundary of $B_a^1$,
some core $B_b^0$ is available, and
\[
 q_{m,b}+L\beta_b/m\geq
 q_{m,a}+L\beta_a/m+(L/2-D)/m
\]
after taking a sufficiently small neighborhood. Hence that
boundary branch may be discarded there. At a common ideal zero
both sides are $-\infty$, but the extended comparison still
shows branch domination on the whole neighborhood; no subtraction
of two infinities is used. This proves valid global finite maximum
gluing.

Locally $\theta+dd^cq_{m,a}=m^{-1}dd^c\log P_{m,a}\geq0$.
Let $C_\beta$ bound the negative Hessians of all the known barriers
relative to $\omega$. Finite maxima preserve the common lower
curvature bound, so
\[
 \theta+dd^c\Phi_m\geq-(LC_\beta/m)\omega.
\]
The tuples have exactly $\I(mu)$, and the finite-max comparisons
prove the same local ideal type for the glued function.
The positive shift $A/m$ gives $\Phi_m\geq u$.
Taking a fixed small $r$ in \eqref{eq:upper} gives a uniform
upper bound depending on $\sup_Xu$ and geometry; the lower
supremum bound follows from $\Phi_m\geq u$.

\subsection{Exact upper-tail equality, including the polar locus}
Fix $x$ and small $r$. By uniform equivalence of the finitely many
coordinate distances, \eqref{eq:upper} and the bounded barriers
imply, for all nearby $y$ and all $m$,
\[
 \Phi_m(y)\leq \sup_{B(x,C_1r)}u+C_2r+
 \frac{C_3+2n\log(1/r)+A+L}{m}.
\]
For an upper tail starting at $m_j$, take the supremum over $m_k$,
then upper semicontinuous regularization in $y$. It follows that
\[
 \lim_j\Psi_j(x)\leq \sup_{B(x,C_1r)}u+C_2r.
\]
Let $r\downarrow0$. Upper semicontinuity gives the right side
tending to $u(x)$, even when $u(x)=-\infty$: for every finite
$T$ a sufficiently small ball has $u<T$.
The opposite inequality holds pointwise because every
$\Phi_m\geq u$. Therefore $\Psi_j\downarrow u$ exactly.
This is stronger than convergence almost everywhere or in $L^1$,
and it does not assume any monotonicity of the individual norms.
Theorem~\ref{thm:R} is proved.

For $\A_c=\I(cu)$ the constructed sequence satisfies
\eqref{eq:curv} with $\epsilon_j=(LC_\beta+1)/m_j$.
Identity~\eqref{eq:integralidentity}, now for the known exact
upper-tail limit $u$, gives \eqref{eq:test}. This proves necessity
and completes Theorem~\ref{thm:main}.

\section{Why the criterion is noncircular, and what it retains}
The initial data consist of ideals and geometry. Certificate
existence quantifies over finite tuples of holomorphic functions
generating those ideals, real constants, and a countable sequence
of the displayed finite formulas. It does not quantify over a
psh target or an unspecified psh/bounded correction. Its tests
use known finite maxima, capped integrals, current inequalities,
and scalar bounds. The $N$ limit can also be written as the
infimum of its known finite-$N$ integrals. The pointwise psh
limit appears only in the proved output construction.

This is a witness characterization, comparable in logical form
to analytic moment or approximation criteria. Its substantive
necessity theorem restricts the witnesses to a rigid formula
class using fixed geometric smooth terms. It is not an effective
finite algebraic axiom system, and does not certify source closure
merely by renaming an order completion. A proposed definition
allowing a correction equal to an unknown realization would be
tautological; it is explicitly excluded. Holomorphic coefficients
and norms in an existence proof may depend on a chosen realization,
just as witnesses normally do, while the tests applied to a
supplied witness require only that witness and the input ideals.

Additive constants cannot be recovered from the array. A realization
may be normalized afterwards by $u-\sup_Xu$, leaving every ideal
unchanged. There is no claim that this normalized raw output is
independent of the certificate. In particular applying a canonical
$\I$-envelope theorem would be a separate theorem application,
not an inference from the construction here.

The ideal map is monotone under pointwise order: $u\leq v$ gives
$\I(cu)\subseteq\I(cv)$ directly from integration. Scaling gives
$\I(c(tu))=\I((ct)u)$; correspondingly real-index reindexing
$\A^{(t)}_c=\A_{tc}$ is realizable in $t\theta$ whenever $\A$
is realizable in $\theta$. This supplies homogeneity in the named
pseudoeffective setting, not a comparison of raw outputs from
different certificates. A smooth change $u\mapsto u+h$ changes
the background to $\theta-dd^ch$ and leaves ideals unchanged.
The analytic approximation and its curvature loss have been proved
above. The precise operator comparison is the identity between
the integral membership operator and the multiplier-ideal operator
at every real index. No new DXZ--MP, energy or Monge--Amp\`ere
comparison is inferred.

\section{Explicit certificates and incompatible arrays}\label{sec:examples}
\subsection{Smooth unit ideals}
If $\theta\geq0$, the function $u=0$ realizes $\A_c=\OO_X$.
Its global unit norm is the finite formula $\Phi_j=m_j^{-1}\log1=0$,
with zero correction and zero loss. If a known smooth $h$ satisfies
$\theta+dd^ch\geq0$, its ideals are also units. The general rigid
construction applies to $h$; it does not insert an unknown $h$
into the admissibility test.
On $\mathbf P^1$ with
$\omega=dd^c\log(1+|z|^2)$ an explicitly finite chart formula for
zero, using $\rho=\log(1+|z|^2)$, is
\[
 \frac1m\log\sum_{\ell=0}^m
   \binom m\ell |z|^{2\ell}-\rho
 =\frac1m\log(1+|z|^2)^m-\rho=0.
\]
The tuple includes $1$, hence generates the unit ideal. The
corresponding chart at infinity gives the same function.

\subsection{Divisorial logarithms and exact integer jumps}
Let $D=\{0\}\subset\mathbf P^1$, and
\[
 G(z)=\log|z|^2-\log(1+|z|^2),\qquad
 \omega+dd^cG=\delta_0,\quad\sup_XG=0.
\]
For $0\leq a\leq1$, $u=aG$ is $\omega$-psh and
\begin{equation}\label{eq:divarray}
 \A_c=\OO_X(-\lfloor ac\rfloor D).
\end{equation}
For a nonzero germ of order $k$ at $0$, bounded smooth factors
leave convergence of the radial integral unchanged:
\[
 2\pi\int_0^t r^{2k-2ac+1}\,dr<\infty
 \quad\Longleftrightarrow\quad k>ac-1
 \quad\Longleftrightarrow\quad k\geq\lfloor ac\rfloor.
\]
Equality $k=ac-1$ diverges logarithmically. Thus the jump at an
integer belongs to the larger exponent ideal, not the earlier one.

Write $q_m=\lfloor am\rfloor$. The finite tuple
\[
 g_{m,\ell}(z)=\sqrt{\binom{m-q_m}{\ell}}\,z^{q_m+\ell},
 \quad 0\leq\ell\leq m-q_m
\]
generates exactly $(z^{q_m})$, and its corrected norm is
\[
 \frac1m\log\sum_\ell|g_{m,\ell}|^2-\rho
   =\frac{q_m}{m}G.
\]
In the infinity coordinate $w$, use
$\sqrt{\binom{m-q_m}{\ell}}w^\ell$; this tuple includes $1$
and gives $-(q_m/m)\log(1+|w|^2)$, the same global function.
Hence $\Phi_j=(q_{m_j}/m_j)G$ is a finite prescribed-ideal norm
with no curvature loss. Along dyadic scales $q_m/m$ increases
to $a$, so $\Phi_j\downarrow aG$; at $0$ the equality holds
after the first positive $q_m$. Formula~\eqref{eq:integralidentity}
proves all-index compatibility, with exactly the threshold
\eqref{eq:divarray}. For $a=1$ all $\Phi_j=G$.

\subsection{Zero top mass}
In the preceding $a=1$ example, the ordinary positive current is
$\delta_0$. Off its pole it vanishes. The one-dimensional
nonpluripolar product, computed from truncations on $\{G>-k\}$,
is therefore zero. Thus this is an explicit certificate with
zero top mass in a positive K\"ahler class. Independently, on
$\mathbf P^1$ with background $\theta=0$, $u=0$ and unit ideals
give another zero-mass example. No measure is divided by its mass.

\subsection{Elementary formal failures}
All the following ideals are nonzero and coherent on $\mathbf P^1$.
\begin{enumerate}
\item \textbf{Index monotonicity failure.}
Take $\A_c=\OO(-D)$ for $0<c<1$, and $\A_c=\OO$ for $c\geq1$.
For a locally normalized $u\leq0$, integrability at a larger
exponent implies it at a smaller exponent. Hence realizable
arrays satisfy $\A_d\subseteq\A_c$ for $d>c$.
The indicated array violates this at $c=1/2,d=1$.
\item \textbf{Subadditivity failure.}
Take units for $c<1$ and $\OO(-D)$ for $c\geq1$.
Then $\A_2=(z)$ at $0$, while $\A_1^2=(z^2)$.
The required inclusion $\A_2\subseteq\A_1^2$ fails. This uses
the disclosed DEL subadditivity theorem after the smooth local
psh reduction, not its incorrect reverse.
\item \textbf{Threshold failure despite monotonicity and subadditivity.}
Take $\A_c=\OO(- (\lceil c\rceil-1)D)$.
The exponent is nondecreasing and satisfies
$\lceil c+d\rceil-1\geq(\lceil c\rceil-1)+(\lceil d\rceil-1)$,
so the two preceding algebraic constraints hold. But $1\in\A_1$
at $0$ and $1\notin\A_{1+\delta}$ for every $\delta>0$.
Strong openness forbids this. This example isolates the right-hand
threshold requirement missed by a purely left-continuous rule.
\end{enumerate}
By sufficiency none of these arrays can pass the full certificate
test. These obstructions are necessary conditions, not a proposed
finite sufficient list.

\section{Raw representatives and mass still do not descend}\label{sec:cantor}
We give an independent version of the Cantor obstruction that does
not import the frozen capacity criterion. Put $\ell_0=1$,
$\ell_k=e^{-4^k}$ for $k\geq1$, and inside each level-$k$
interval put the next two intervals at its endpoints, of length
$\ell_{k+1}$. There are $2^k$ disjoint intervals at level $k$.
Their intersection $F$ carries the Bernoulli probability $\mu$
giving each level-$k$ interval mass $2^{-k}$. It has no atoms,
and $F$ has planar area zero. For $x\in F$, the level-$k$
interval containing $x$ consists of points within distance
$\ell_k$ of $x$ and has $\mu$-mass $2^{-k}$. The layer-cake
identity for $-\log|x-p|$ gives
\[
 \int-\log|x-p|\,d\mu(p)
 \geq\sum_{k\geq1}(4^k-4^{k-1})2^{-k}=+\infty.
\]
Bounded chordal correction terms do not affect the divergence.

Use squared chordal Green functions
$G_p(z)=\log(|z-p|^2/((1+|z|^2)(1+|p|^2)))$ and define
$V(z)=\int G_p(z)\,d\mu(p)$. These functions are nonpositive;
their negative parts have uniformly finite area integrals by
rotation invariance of Fubini--Study measure. Fubini therefore
defines an $L^1$ function, and yields
$\omega+dd^cV=\mu$. Its canonical usc representative agrees
with the integral: the latter is usc by the reverse Fatou inequality
for a common upper bound, and the local sub-mean inequality passes
under integration. It is finite and smooth off $F$, and equals
$-\infty$ on $F$ by the preceding divergence. This also proves
that $F$ is polar without a separate capacity theorem.

For $0\leq s\leq1$, put $u_s=sV$ (with $u_0=0$).
Then $\omega+dd^cu_s=(1-s)\omega+s\mu$. We prove directly that
$\I(cu_s)=\OO$ for every $c>0$. Near any $x$, choose a small
coordinate disk whose doubled disk has $\mu$-mass
$\beta<1/(cs)$ when $cs>0$; nonatomicity makes this possible.
The contribution from its complement is bounded below on the
smaller disk. For the local measure, normalized to mass one,
Jensen gives
\[
 \exp\left(-cs\int\log|z-p|^2\,d\mu_{\rm near}(p)\right)
 \leq\frac1\beta\int|z-p|^{-2cs\beta}
                         d\mu_{\rm near}(p).
\]
The right-hand side has finite area integral uniformly in $p$
because $cs\beta<1$. If $\beta=0$, the local contribution is
absent. Smooth coordinate corrections are harmless. This proves
the required local exponential integrability without an appeal
to a divisorial reconstruction theorem.

For $s>0$, the finite locus is exactly $X\setminus F$. On it
$u_s$ is smooth and the current is $(1-s)\omega$; the truncation
definition of the degree-one nonpluripolar product therefore gives
\[
 \langle\omega+dd^cu_s\rangle=(1-s)\omega,
 \qquad M_\omega(u_s)=1-s.
\]
For $s=0$ the mass is one. All these functions have the same
full real ideal array. Consequently neither a raw representative
nor its raw nonpluripolar mass is a function of that array; one
class contains every mass in $[0,1]$. The present certificate
construction can select different representatives using different
norm tuples, consistent with this obstruction. The conclusion
about the distinct $P$-envelopes, when needed, still requires the
separate positive-mass $P$-envelope mass-preservation theorem;
we do not assume that theorem to establish the direct raw-mass
obstruction here.

\section{A frozen source error and its independent correction}\label{sec:defect}
The full frozen book proposition and proof
\texttt{prop:ch51-qes-preserves-i}, literal LF 2013--2059, are
preserved locally unchanged. Its displayed ideal formula has
the union over $\lambda'<\lambda$. Test it with
$u_j=u=\log|z|^2$ on a disk. At $\lambda=1$, radial integration
above gives $\I(u)=(z)$, whereas each $0<\lambda'<1$ gives
$\I(\lambda'u_j)=\OO$. Its proposed right side is $\OO$.
This is an actual mathematical counterexample, independent of
historical review assertions. The global $G$ example supplies
a constant decreasing sequence in the Fubini--Study class, with
vanishing loss and gentle type $(1/m,(z^m))$ at every integer $m$.
For $\lambda'>\lambda$ it has the required eventual ideal
inclusions, so the usual approximation hypotheses do not exclude
the test.

Under the precise hypotheses $u_j\downarrow u$,
$\I(\lambda'u_j)\subseteq\I(\lambda u)$ for all sufficiently
large $j$ whenever $\lambda'>\lambda$, and strong openness, the
correct formula at stalks is
\begin{equation}\label{eq:corrected}
 \I(\lambda u)=
 \bigcup_{\lambda'>\lambda}\bigcap_j\I(\lambda'u_j).
\end{equation}
Indeed membership in an intersection on the right puts a germ
in one sufficiently late ideal, hence in $\I(\lambda u)$.
Conversely strong openness places a germ of $\I(\lambda u)$ in
$\I(\lambda'u)$ for some $\lambda'>\lambda$, and $u\leq u_j$
places it in every $\I(\lambda'u_j)$. This proves the corrected
conditional assertion only. It does not authenticate every
claim of that frozen proposition or its preceding regularization
prose. In particular the proof's mention of a constant zero
approximation to a nonzero Cantor potential is not compatible
with a definition that also requires pointwise decrease to that
potential. We use neither assertion in the main proof.

\section{DPS normalization and the scope of the author claim}
DPS uses the weight $e^{-2\varphi}$ and the operator
$i\partial\bar\partial$. For our $u$ set $\varphi=u/2$.
Then
\[
 2m\varphi=mu,\qquad
 i\partial\bar\partial\varphi=\pi dd^cu,\qquad
 \pi\theta+i\partial\bar\partial\varphi
       =\pi(\theta+dd^cu).
\]
Thus a DPS curvature loss $\varepsilon\omega$ for this last
current corresponds to a book-normalized loss
$(\varepsilon/\pi)\omega$. For a local exact potential $\rho$,
the Hilbert weight in our proof is $e^{-m(u+\rho)}$, namely
the DPS local weight at $\varphi_{\rm loc}=(u+\rho)/2$,
and doubling its $1/(2m)$ kernel logarithm produces $1/m$.
This fixes both the ideal identity and the curvature factor.

The whole DPS Theorem 2.2.1 produces smooth-away-analytic-set
equisingular approximants. Remark 2.2.2 says that the final
step destroys logarithmic poles. Step 1 supplies the local
weighted kernels, Step 2 a finite coherent reduction sufficient
for its integral argument, Step 3 dyadic almost decrease for
one fixed cover, and Step 4 upper tails while the error/cover
changes. None of those final approximants is silently substituted
for our finite prescribed-ideal norms. Our necessity proof uses
exact potentials of the closed background and a separate finite
relative reduction, and does not assume varying-cover almost
decrease.

The theorem is an author solution claim for the arbitrary-formal-data
alternative of original P14.8, in the explicitly stated geometric
and integral witness sense. It requires independent review of
the arguments, especially the finite Fr\'echet division step and
the exact-potential gluing. The imported deep theorems are ordinary
published analytic premises, not a new unproved regularization
grant. There is no claim of complete original-primary validation
of all of them: absent original texts for (H), (O), (N), and (C)
are a source-evidence limitation. If that stronger validation is
a required gate, this submission remains a candidate at that gate.
It does not solve an all-semivaluation reconstruction alternative,
create a new terminal DXZ interval, or change the separate open
targets P14.1, P14.4, P14.5, and P14.6. No acceptance count is
changed, and P16.4 is untouched.

\appendix
\section{Evidence and reproducibility}
All long source bodies and rendered primary pages remain in the
local \texttt{LOCALONLY/} directory. Literal LF means
\texttt{text.split('\string\n')}; form feeds remain inside records.
For files ending in a newline, record counts include the final
empty record; this explains one-record differences from the
supplied bindings. The source coverage and application ledger
give version, hashes, units and exact scope; a hash is not a
mathematical proof or a claim of full PDF visual reading.

The author's finite checks verify rational threshold arithmetic,
dyadic floor inequalities, binomial norm identities at exact
rational points, and the explicit incompatible arrays. These
are finite results supplementing continuum proofs, not a solver
for the criterion. Only the author's programs are executed.
TeX is compiled with shell escape disabled, and the inspected
source has no file inclusions, shell primitives or external
bibliography execution. Initial truncation warnings, if any,
and the actual build receipts are retained separately from the
saved mathematical claims. Rerun instructions are in
\texttt{rerun.md}; hashes of delivered artifacts are in
\texttt{artifactbindings.json}.

\begin{thebibliography}{99}
\bibitem{DPS00} J.-P. Demailly, T. Peternell and M. Schneider,
\emph{Pseudo-effective line bundles on compact K\"ahler manifolds},
arXiv math/0006205v2, 10 October 2000. Bound original PDF/text;
publisher byte identity is not asserted.
\bibitem{D92} J.-P. Demailly, \emph{Regularization of closed positive
currents and intersection theory}, J. Algebraic Geom. 1 (1992), 361--409.
\bibitem{H65} L. H\"ormander, \emph{$L^2$ estimates and existence
theorems for the $\bar\partial$ operator}, Acta Math. 113 (1965), 89--152.
\bibitem{H90} L. H\"ormander, \emph{An introduction to complex
analysis in several variables}, third edition, North-Holland, 1990.
The DPS key [H\"or66] refers to the book, whereas the frozen book
bibliography's key Hor66 denotes the 1965 article.
\bibitem{OT87} T. Ohsawa and K. Takegoshi, \emph{On the extension
of $L^2$ holomorphic functions}, Math. Z. 195 (1987), 197--204.
\bibitem{N90} A. Nadel, \emph{Multiplier ideal sheaves and K\"ahler--Einstein
metrics of positive scalar curvature}, Ann. of Math. 132 (1990), 549--596.
\bibitem{GR84} H. Grauert and R. Remmert, \emph{Coherent analytic
sheaves}, Springer, 1984.
\bibitem{Nar66} R. Narasimhan, \emph{Introduction to the theory of
analytic spaces}, Lecture Notes in Mathematics 25, Springer, 1966.
\bibitem{DEL00} J.-P. Demailly, L. Ein and R. Lazarsfeld,
\emph{A subadditivity property of multiplier ideals}, Michigan
Math. J. 48 (2000), 137--156.
\bibitem{GZ15} Q. Guan and X. Zhou, \emph{Effectiveness of Demailly's
strong openness conjecture and related problems}, Invent. Math.
202 (2015), 635--676.
\end{thebibliography}
\end{document}

```
