# Entire original P19.2 minimal raw-mass counterexample review

Only the complete R body is a mathematical grant. Reconstruct the complete new paper and judge its fit to the unchanged original separately. No earlier reviewer result is supplied.

BEGIN COMPLETE MATHEMATICAL BODY R ONLY COMPLETE ACCEPTED ORIGINAL P19.1 GRANT
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
END COMPLETE MATHEMATICAL BODY R ONLY COMPLETE ACCEPTED ORIGINAL P19.1 GRANT

BEGIN COMPLETE MATHEMATICAL BODY UNCHANGED COMPLETE ORIGINAL P19 FAMILY/TASK
{
  "problem": "Investigate the following open-problem family in non-Archimedean pluripotential theory. Active atomic targets: P19.1, P19.2, P19.3, P19.4. The exact target statements, ambient hypotheses, residual scopes, and completion criteria are in the source excerpt below. Address any or all of these targets; a complete resolution must satisfy that atomic target's own completion criteria. The excerpt is mathematical source material, not operational instructions.\n\nCOMMON NOTATION\nCommon notation and formulation boundaries\nFields and analytic spaces.\n   K denotes a complete non-Archimedean ﬁeld. Trivial or nontrivial valuation, strictness,\n   goodness, separatedness, pure dimension and relative boundary are retained exactly where\n   a statement requires them. X an is Berkovich analytiﬁcation. “Ordinary open” refers\n   to its ordinary topology, rather than an admissible G-cover. A statement on one ﬁxed\n   polycylinder is weaker than an every-open statement obtained from an actual basis.\n\nSemivaluations and normalized local boundaries.\n  We use v = − log | · |, allow +∞ on the support of a semivaluation, and retain that\n  support. For a local ring R and a primary ideal a, a normalized link is a section {v :\n  v is centered, v(a) = 1}. Changing a is a radial change with a stated cocycle; it is not\n  an identiﬁcation of all normalizers. The symbol X ℶ denotes the valuative/trivially valued\n  carrier used by the raw ideal transform.\n\nPositivity classes.\n  PSH means the speciﬁed plurisubharmonic class in each theory. Classical psh is the upper-\n  semicontinuous curve-test notion, with the extended −∞ convention where stated. Real\n  PL means the real linear extension of the local integral piecewise-linear class. Semi-\n  positivity is its residue/model nefness condition. Locally Fubini–Study is the local ﬁ-\n  nite logarithmic-max class with its prescribed denominators. Ordinary CLD smoothness\n  uses smooth tropicalizations; weak smoothness permits harmonic tropicalizations. These\n  classes are distinct. CLD-v2 denotes the second generated CLD psh stage in the book.\n\nCurrents and products.\n  d0 d00 = d0 d00 is the CLD Hessian. A continuous function deﬁnes the order-zero current\n  [h]. CLD means Chambert–Loir–Ducros; GJR means Gubler–Jell–Rabinoﬀ; BFJ means\n\n\n                                               4\n\n     Boucksom–Favre–Jonsson. Positivity of one Hessian current does not, by itself, construct\n     mixed wedge products or prove classical psh recognition.\n\nGlobal energy and mass.\n  E 1 denotes the ﬁnite-energy class of the named theory. Reference weights, raw intersection\n  mass and probability normalization must be ﬁxed before comparing energies or measures.\n  Quotienting by R means uniqueness modulo additive constants. Zero top mass cannot be\n  divided into a probability measure. The aﬃne-cone probability operator is an explicitly\n  separate convention.\n\nComplex singularity data.\n         1,1\n  α ∈ HBC    (X, R) is a real Bott–Chern class. MP means Mesquita–Piccione, DXZ means\n  Darvas–Xia–Zhang, and BJ means Boucksom–Jonsson. I-equivalence records multiplier-\n  ideal data; P -equivalence records the ﬁner envelope/singularity data. The latter cannot\n  generally be recovered from the former, even at positive mass.\n\nPolyhedral normalization.\n   PA denotes piecewise-aﬃne functions. BMPS means Botero–Mazzon–Pille-Schneider. Lit-\n   eral integral slopes and the real scalar extension are separate conventions. In dimension\n   d, the polyhedral intersection convention diﬀers from the real Alexandrov measure by the\n   factor d! and the face multiplicity. Saturated tangent lattices and analytic multiplicities\n   are part of an analytic comparison.\n\n\n\n\nFULL FAMILY DOSSIER\n11     Residual hybrid entropy and YTD questions\nActive items: P19.1, P19.2, P19.3, P19.4. Status: Open in the residual scope.\n\n11.1    Atomic targets\nP19.1 (T5): Entropy slopes of arbitrary ﬁnite-energy weak rays\nProve the remaining entropy-slope statement for arbitrary ﬁnite-energy weak rays on a com-\npact Kähler manifold, outside the stated smooth polarized projective maximal-ray results.\nState the non-Archimedean datum, the entropy normalization and the precise ray hypothe-\nses.\n\nP19.2 (T4): Approximation preserving energy, entropy and singularities\nConstruct model approximations in the residual hybrid programme that preserve all required\nenergy, entropy and singularity data. Convergence of energy alone is insuﬃcient, and the\npublished/source-stated projective Fujita regimes are established subcases.\n\nP19.3 (T5): Hybrid compactness and measures for degenerating families\nProve the compactness and measure-continuity statements needed along genuinely degener-\nating families of compact Kähler manifolds. A ﬁxed quasi-projective variety hybridized with\nexplicit scale factors is a diﬀerent known endpoint.\n\nP19.4 (T5): Equivariant, transcendental and singular hybrid extensions\nEstablish the required automorphism-equivariant transcendental and singular extensions, with\nthe exact stability and metric signatures speciﬁed. Retain the residual distinctions from the\ncited smooth polarized projective and static Kähler-class correspondences.\n\n11.2    What constitutes a solution\nFreeze the exact ray, approximation, family or equivariant signature and prove the residual\nstatement with its entropy and energy normalizations. Keep recent preprint claims in their\nstated smooth polarized scope. The four targets are independent residual hybrid goals; they\nare not prerequisites for the already cited static uniform-model-stability-to-cscK implication.\n\n11.3    Full statement and detailed state of the art\nProblem 11.1. Develop the remaining entropy-slope, approximation, compactness, and au-\ntomorphism statements for arbitrary ﬁnite-energy weak rays and degenerating families in the\nhybrid K-stability/YTD programme on a compact Kähler manifold.\n\n    The static projective entropy and stability gap must not be listed as wholly open at this\ncutoﬀ. Boucksom–Jonsson’s version-two notes of 19 May 2026 give a structural complex-to-\nnon-Archimedean overview and only sketch a version of the cscK YTD argument [BJ26]. They\nare used here as orientation, not as a separate approximation or hybrid-continuity theorem\nthat narrows any atom in Problem 11.1.\n    Trusiani’s version-two preprint of 17 August 2026, [Tru26, Theorem B and Corollary A],\nretains the special Fujita approximations for big line bundles and the claimed solution\nof the Boucksom–Jonsson entropy-regularization conjecture; its Theorem A retains the\nautomorphism-relative uniform YTD theorem for smooth polarized projective varieties.\nCorollary A also records the resulting equality of the Archimedean entropy slope along a\n\n                                              76\n\nmaximal ﬁnite-energy ray with the non-Archimedean entropy, in that projective framework.\nThe new Appendix by Sébastien Boucksom supplies a non-Archimedean proof over k((t)),\nand Theorem C adds the weighted-relative correspondence, including Calabi extremal met-\nrics when the weight is log-concave. These are recent preprint claims, rather than results\nindependently reproved in this book. Boucksom–Jonsson’s 18 September 2025 preprint\n[BJ25c] gives a non-Archimedean formulation for cscK and weighted extremal metrics on\npolarized projective manifolds. Darvas–Zhang’s 3 November 2025 version-two preprint [DZ25,\nTheorems 1.6 and 5.5] gives a uniform YTD correspondence for a unique cscK metric on an\narbitrary compact Kähler manifold using K β -stability and, in the polarized projective case, a\nreductivity-plus-log-discrepancy-model formulation. Mesquita–Piccione–Witt Nyström prove\nthat uniform model stability implies existence in a Kähler class and establish the transcen-\ndental ﬁnite-energy Calabi–Yau homeomorphism [MPWN25, Theorems A and B]. Finally,\nTrusiani’s Corollary B identiﬁes the standard automorphism-relative projective stability\nformulations in the smooth polarized setting [Tru26]. Thus the projective entropy slope, the\nweighted-relative correspondence in the stated smooth polarized scope, and comparison of\nthe listed projective signatures are no longer open problems.\n    There is a complementary hybrid endpoint outside the compact proper setting. For each\nof the three aﬃne/Calabi-model situations stated in Wang’s Theorem B, explicit scale fac-\ntors make the Archimedean potential and its non-Archimedean counterpart into one continu-\nous function on the hybrid space; the correspondingly rescaled Archimedean Monge–Ampère\nmeasures converge weakly to the non-Archimedean measure [Wan25, Theorem B]. This is a\ncomparison for a ﬁxed quasi-projective variety over the hybrid parameter, not a compactness\nor measure-continuity theorem for a degenerating family of compact Kähler manifolds. It\ntherefore does not discharge P19.3.\n    Consequently, the atoms in Problem 11.1 are not asserted to be logical prerequisites for the\ncited uniform-model-stability-to-cscK implication. They record the distinct residual hybrid\nprogramme: statements for arbitrary ﬁnite-energy weak rays, log-discrepancy-model regu-\nlarization, and genuinely degenerating families that are not supplied merely by the static\nKähler-class theorem.\n    Book Chapter 66, Book Chapter 68 separates hybrid convergence from entropy and coerciv-\nity. The BHJ erratum is enforced in Book Chapter 65. The remaining targets are narrower:\ndirect algebraic proofs of the known projective equivalences; K β -stability in the presence\nof nontrivial automorphisms; equivariant transcendental and singular extensions; regulariza-\ntion of rays attached to log-discrepancy models; and the genuinely hybrid compactness and\nmeasure-continuity statements needed to pass through a degenerating family. Boucksom–\nJonsson also isolate bounded support size for divisorial test measures, algebraic equivariance\nproofs, and extension to polarized klt pairs [BJ25c, Questions and further remarks]. Those\nresidual problems remain open; the smooth polarized projective entropy and weighted-relative\ntheorems are dated Trusiani version-two claims, not missing inputs.\n\n\n\n\n                                              77\n\n\n\nCATALOGUE BIBLIOGRAPHY\n\nReferences\n[BGGJK25] José Ignacio Burgos Gil, Walter Gubler, Philipp Jell, and Klaus Künnemann.\n         Pluripotential theory for tropical toric varieties and non-Archimedean Monge–\n         Ampère equations. Kyoto J. Math., 65(1):55–152, 2025.\n\n[Bin76]   Jürgen Bingener. Schemata über Steinschen Algebren. Schr. Math. Inst. Univ.\n          Münster (2), page 52, 1976.\n\n[BJ23]    Sébastien Boucksom and Mattias Jonsson. A non-Archimedean approach to K-\n          stability, II: Divisorial stability and openness. J. Reine Angew. Math., 805:1–53,\n          2023.\n\n[BJ24b]   Sébastien Boucksom and Mattias Jonsson. Non-Archimedean Green’s functions\n          and Zariski decompositions. Comptes Rendus Mathématique, 362(S1):5–42, 2024.\n\n[BJ25c]   Sébastien Boucksom and Mattias Jonsson. On the Yau–Tian–Donaldson conjec-\n          ture for weighted cscK metrics, 2025. Version 1, 18 September 2025.\n\n[BJ26]    Sébastien Boucksom and Mattias Jonsson. From complex to non-Archimedean\n          geometry: an approach to the YTD conjecture, 2026. Version 2, 19 May 2026.\n\n[BMPS26] Ana María Botero, Enrica Mazzon, and Léonard Pille-Schneider. Monge–Ampère\n         measures on balanced polyhedral spaces, 2026. Manuscript dated 10 March 2026.\n\n[CLD25]   Antoine Chambert-Loir and Antoine Ducros. Formes diﬀérentielles réelles et\n          courants sur les espaces de Berkovich, 2025. Version 2, 25 July 2025.\n\n[DRWN+ 26] Tamás Darvas, Rémi Reboulet, David Witt Nyström, Mingchen Xia, and Kewei\n         Zhang. Transcendental Okounkov bodies. J. Diﬀerential Geom., 132(1):135–178,\n         2026.\n\n[DXZ25]   Tamás Darvas, Mingchen Xia, and Kewei Zhang. A transcendental approach\n          to non-Archimedean metrics of pseudoeﬀective classes. Comment. Math. Helv.,\n          100(2):269–322, 2025.\n\n[DZ25]    Tamás Darvas and Kewei Zhang. A YTD correspondence for constant scalar\n          curvature metrics, 2025. Version 2, 3 November 2025.\n\n[Fan25]   Yanbo Fang. Metrized ample line bundles in non-Archimedean geometry II, 2025.\n          Version 1, 26 November 2025.\n\n[Fin26]   Siarhei Finski. Kodaira–Iitaka dimension and multiplicity: an analytic perspec-\n          tive, 2026. Version 1, 23 March 2026.\n\n[GJKM19] Walter Gubler, Philipp Jell, Klaus Künnemann, and Florent Martin. Continu-\n         ity of plurisubharmonic envelopes in non-Archimedean geometry and test ideals.\n         Ann. Inst. Fourier (Grenoble), 69(5):2331–2376, 2019. With an appendix by José\n         Ignacio Burgos Gil and Martín Sombra.\n\n[GJR26]   Walter Gubler, Philipp Jell, and Joseph Rabinoﬀ. Forms on Berkovich spaces\n          based on harmonic tropicalizations. Bull. Soc. Math. France, 154(1):135–238,\n          2026.\n\n[GR25a]   Walter Gubler and Joseph Rabinoﬀ. Classically psh and pluriharmonic functions\n          on Berkovich spaces, 2025. Version 2, 17 September 2025.\n\n\n                                           85\n\n[MPWN25] Pietro Mesquita-Piccione and David Witt Nyström. A transcendental non-\n        Archimedean Calabi–Yau theorem with applications to the cscK problem, 2025.\n        Version 1, 11 September 2025.\n\n[PS23]      Léonard Pille-Schneider. Global pluripotential theory on hybrid spaces. J. Éc.\n            polytech. Math., 10:601–658, 2023.\n\n[PSWZ26] Kai Pang, Haoyuan Sun, Zhiwei Wang, and Xiangyu Zhou. Capacity stability\n         of complex Monge–Ampère equations with moving prescribed singularities, 2026.\n         Version 1, 14 July 2026.\n\n[Stacksb]   The Stacks Project Authors. Stacks project. https://stacks.math.columbia.e\n            du, 2026. Accessed 29 August 2026.\n\n[Sup26b]    Withdrawn draft: Orthogonality on one-dimensional balanced fans, 2026. Author-\n            supplied withdrawn manuscript dated and received 25 September 2026; replace-\n            ment withdrawal version preserved in the book repository.\n\n[Tru26]     Antonio Trusiani. A solution to the Yau–Tian–Donaldson conjecture through\n            special Fujita approximations, 2026. Version 2, 17 August 2026; includes an\n            appendix by Sébastien Boucksom.\n\n[Vil21]     Christian Vilsmeier. A comparison of the real and non-archimedean Monge-\n            Ampère operator. Math. Z., 297(1-2):633–668, 2021.\n\n[Wan19]     Veronika Wanner. Comparison of two notions of subharmonicity on non-\n            archimedean curves. Math. Z., 293:443–474, 2019.\n\n[Wan25]     Ying Wang. Non-Archimedean Calabi–Yau potentials on certain aﬃne varieties,\n            2025. Version 1, 24 October 2025.\n\n[Wu24]      Yueqiao Wu. Some non-Archimedean pluripotential theory on polarized aﬃne\n            cones, 2024. Version 1, 19 June 2024.\n\n[Xia25a]    Mingchen Xia. Operations on transcendental non-Archimedean metrics. In Con-\n            vex and complex: perspectives on positivity in geometry, volume 810 of Contemp.\n            Math., pages 271–293. Amer. Math. Soc., Providence, RI, 2025.\n\n[Xia25b]    Mingchen Xia. Partial Okounkov bodies and Duistermaat-Heckman measures of\n            non-Archimedean metrics. Geom. Topol., 29(3):1283–1344, 2025.\n\n[Xia26a]    Mingchen Xia. Mixed volumes of Okounkov bodies. Work in progress, July 2026;\n            available at https://mingchenxia.github.io/Papers/MVOB.pdf. The author-\n            supplied source was repaired and independently audited on 24 August 2026. The\n            full repaired proof is reproduced in this book; its production Rethlas proof digest\n            is 9227826d...58cad7b, with ﬁnal verdict correct and no reported gap, 2026.\n\n[Zha14]     Yuchen Zhang. On the volume of isolated singularities. Compositio Mathematica,\n            150(8):1413–1424, 2014.\n\n\n\n\n                                              86\n\n",
  "completionCriteria": "For each target claimed solved, give a rigorous complete proof or an analytic counterexample satisfying every ambient hypothesis, and explicitly compare the result to the residual scope in the catalogue. Do not count an already known case, an extra conditional hypothesis, an abstract tropical obstruction, or a narrower theorem as a full solution. Separate partial progress and unresolved claims. Every essential external theorem must be stated exactly, cited, and checked for applicability; source-dependent claims from the catalogue are not independently established merely by its description. A rigorous new special case may be reported with its exact scope and a statement that the full atom remains open."
}
END COMPLETE MATHEMATICAL BODY UNCHANGED COMPLETE ORIGINAL P19 FAMILY/TASK

BEGIN COMPLETE MATHEMATICAL BODY ENTIRE ELEVEN-PAGE212 CANDIDATE INCLUDING EVERY PROOF AND APPENDIX
\documentclass[11pt]{article}
\usepackage[a4paper,margin=26mm]{geometry}
\usepackage{amsmath,amssymb,amsthm,hyperref}
\setlength{\emergencystretch}{3em}
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}
\newcommand{\PSH}{\operatorname{PSH}}
\newcommand{\MI}{\mathcal I}
\newcommand{\OO}{\mathcal O}
\newcommand{\NA}{\mathrm{NA}}
\newcommand{\MA}{\operatorname{MA}}
\newcommand{\ddc}{dd^c}
\newcommand{\ds}{d_{\mathcal S}}
\newcommand{\Eone}{\mathcal E^1}
\title{A transcendental obstruction to simultaneous\protect\\ model energy and raw singularity-profile recovery}
\author{Unreviewed original P19.2 counterexample candidate, continuation 212}
\date{6 October 2026}
\begin{document}
\maketitle
\begin{abstract}
We construct a bounded finite-energy weak geodesic ray from the smooth
zero potential on a nonprojective compact K\"ahler threefold with a
genuinely transcendental K\"ahler class. Its usual non-Archimedean datum
is zero, but every interior Legendre level in a nonempty interval has a
positive-mass P-model singularity that is not I-model. No sequence of
canonical cohomological model rays, or even of arbitrary usual-datum
maximal finite-energy rays from zero, converges to this finer profile
in the singularity distance. More fundamentally, even pointwise recovery
of its interior raw top-mass profile is incompatible with recovery of
the usual datum and its non-Archimedean energy. This second obstruction
requires no singularity-distance hypothesis and also covers locally
bounded model-compatible total weights and I-maximal flag rays. It
concerns positive mass and is independent of added entropy requirements. We prove the
needed I-model closedness using lower rooftop envelopes on an arbitrary
compact K\"ahler manifold, and justify the local Gauss formula without
assuming a polarization. This is a proposed analytic counterexample to
the arbitrary-ray, finer-P-profile approximation request. It remains
unreviewed; no original problem is recorded as solved on its basis.
\end{abstract}

\section{The approximation signature and conventions}
Let $(X,\omega)$ be a connected smooth compact K\"ahler manifold,
$n=\dim X$, $V=\int_X\omega^n$, and $\alpha=[\omega]$. We fix
\[
 \ddc=\frac{i}{2\pi}\partial\bar\partial,
 \qquad t=-\log|\tau|^2,
 \qquad \ddc\log|f|^2=[\operatorname{div}(f)].                 \tag{1}
\]
All products of unbounded potentials below are nonpluripolar products.
Set
\[
 M_k(u)=\frac1V\int_X\langle(\omega+\ddc u)^k\rangle
                      \wedge\omega^{n-k},\quad 0\le k\le n.
                                                               \tag{2}
\]
Thus $M_0=1$ and $M_n$ is a raw mass divided by the fixed reference
volume, not a renormalized probability. Put
\[
 E(u)=\frac1{(n+1)V}\sum_{k=0}^n
     \int_X u\,\omega_u^k\wedge\omega^{n-k},\qquad
 H(u)=\operatorname{Ent}(\omega_u^n/V\mid\omega^n/V)
                                                               \tag{3}
\]
on the full-mass finite-energy class, with entropy $+\infty$ for a
measure not absolutely continuous with respect to $\omega^n/V$.

Write $P[u]=\operatorname{usc}\lim_{C\to\infty}P_\omega(u+C,0)$.
The I-envelope is
\[
 P_I[u]=\sup\{v\in\PSH(X,\omega):v\le0,
                 \MI(av)\subset\MI(au)\text{ for every }a>0\}.
                                                               \tag{4}
\]
The envelope in (4) is itself admissible. A normalized P-model is a
fixed point of $P$, and an I-model is a fixed point of $P_I$.
Positive-mass P-models carry the singularity distance of DDNL
\cite{DDNL}. We use its probability normalization $\ds^V=\ds/V$.
In particular, for ordered types $[u]\le[v]$,
\[
 \ds^V([u],[v])=\frac1{n+1}\sum_{k=0}^n(M_k(v)-M_k(u)).        \tag{5}
\]
Here P-equivalence refers to equality of the normalized P-envelopes;
it is finer than equality of all multiplier ideals.

For an actual finite-energy weak ray $U$ from zero, let
\[
 \chi_\lambda=\inf_{t>0}(U_t-t\lambda),\qquad
 U_t=\sup_\lambda(\chi_\lambda+t\lambda).                    \tag{6}
\]
These are the closed Legendre levels; a level identically $-\infty$
is not a potential to which (2) or a positive-mass singularity distance
can be assigned. One finer profile convergence examined here requires
\[
 \ds^V([P[\chi_{j,\lambda}]],[\chi_\lambda])\longrightarrow0
                                                               \tag{7}
\]
at every genuine positive-mass level of the target. In particular (7)
preserves the finer P datum and the raw mixed masses in (2).
The prescribed start is zero, so these normalized absolute envelopes
are also the relative P ceilings against the actual start.
The counterexample fails (7) already at any one of the indicated
interior levels, so additional requirements at a closed endpoint do
not repair it. Section~\ref{minimal} proves a second obstruction using
only the usual datum at the trivial valuation, its non-Archimedean
energy, and pointwise raw top-mass recovery on $(-1,0)$.

A cohomological model means a dominating equivariant normal compact
K\"ahler test configuration, with a real vertical divisor $D$, whose
class $\alpha_{\mathcal X}+D$ is relatively K\"ahler, together with its
canonical Perron weak ray from zero. We also allow canonical maximal
rays attached to finite-energy nef or obstacle model data. This includes
positive analytic flag blowup configurations; no relative semiampleness
or line bundle is imposed. More broadly, our obstruction applies to
\emph{every} usual-datum maximal finite-energy ray from zero.
Maximality means domination of any weak ray with smaller initial
potential and smaller usual datum. The usual datum is the negative
generic coefficient of the actual total potential on a vertical Gauss
divisor, divided by its order of $\tau$, in convention (1).
It is extended to $X^\beth$ by divisorial determination, retaining
supported semivaluations. These notions and the actual maximal rays
are the complete previously accepted caller theorem R \cite{R};
the relevant geometric model realization is MP Lemma 5.1.8 \cite{MP}.

\begin{theorem}\label{main}
There are a nonprojective compact K\"ahler threefold $(X,\omega)$,
with $[\omega]$ not proportional to a line-bundle class, and an actual
weak geodesic ray $U:[0,\infty)\to\Eone(X,\omega)$ such that
\begin{enumerate}
\item $U_0=0$, $-t\le U_t\le0$, and its usual datum is identically zero.
\item For a fixed $c_0\in(0,1)$, its Legendre levels are P-models and
\[
 M_k(\chi_\lambda)=1-\frac{k}{n}c_0(\lambda+1),
       \qquad -1<\lambda\le0,
       \quad 0\le k\le n.                                 \tag{8}
\]
Every level in $(-1,0]$ has all multiplier ideals trivial and has
positive mass strictly less than one. Hence it is not I-model.
\item For any fixed $\lambda\in(-1,0)$, no sequence of usual-datum
maximal finite-energy rays from zero satisfies (7). Consequently no
cohomological model approximation of this ray preserves this finer
P profile, regardless of the energy and entropy conditions added.
\item Its radial energy is $-c_0/2$, whereas the maximal ray of its
usual datum from zero is stationary and has radial energy zero.
With the entropy normalization (3), $H(U_0)=0$ and
$\lim_{t\to\infty}H(U_t)/t=+\infty$ by caller theorem R.
\item No sequence in the broader model category of Section~\ref{minimal}
satisfies simultaneously
\[
 \phi_j(v_{\rm triv})\to0,\qquad E_\alpha(\phi_j)\to0,
 \qquad M_n(P[\chi_{j,\lambda}])\to
               1-c_0(\lambda+1)\quad(-1<\lambda<0).       \tag{22}
\]
Here $\phi_j$ is its actual usual datum, and the start is the actual
zero potential. No $d_{\mathcal S}$ convergence or analytic-energy
recovery assumption is imposed in (22).
\end{enumerate}
\end{theorem}

\section{Closedness of I-model singularities without a polarization}
We specify the external envelope facts used. DX Proposition 2.18 and
Lemma 2.21 are valid in its Section 2.4 on an arbitrary compact
K\"ahler manifold, with a smooth pseudoeffective form: $P_Iu$ is
P-model, $P_Iu\sim_Iu$, and decreasing I-model limits remain I-model.
An increasing almost-everywhere limit of I-model P-potentials is
I-model when the limit is P-model of positive mass \cite{DX}.
DDNL Theorem 5.6 applies to a big class on a compact K\"ahler
manifold: if positive-mass normalized P-models converge in $\ds$,
a subsequence has lower rooftop tails increasing almost everywhere
to the limit. The tails are decreasing limits of finite rooftops,
are P-model, and have positive mass after a finite initial deletion
\cite{DDNL}. We need the lower tails, which require no algebraic
approximation.

\begin{lemma}\label{roof}
A nontrivial finite lower rooftop of I-model potentials is I-model.
\end{lemma}
\begin{proof}
Let $w=P_\omega(u_1,\ldots,u_r)\in\PSH(X,\omega)$, where
$P_Iu_i=u_i$. Since $w\le u_i$, any competitor $v$ in (4) for $w$
satisfies $\MI(av)\subset\MI(aw)\subset\MI(au_i)$ for all $a>0$.
Thus $v\le P_Iu_i=u_i$ for every $i$, and $v\le w$ by the
rooftop definition. The potential $w$ itself is a competitor.
Taking the supremum proves $P_Iw=w$.
\end{proof}

\begin{proposition}\label{closed}
If $u_j=P_Iu_j$, $u=P[u]$, $M_n(u)>0$, and
$\ds([u_j],[u])\to0$, then $u=P_Iu$.
\end{proposition}
\begin{proof}
The mass continuity bound following DDNL Lemma 3.4, Proposition 3.5
and Lemma 3.7 gives
$|M_n(u_j)-M_n(u)|\le C\ds^V([u_j],[u])$; it follows directly by
splitting at $\max(u_j,u)$ and using the nonnegative summands of
(5). Thus the sequence and its limit eventually have a common
positive lower mass bound. Apply DDNL Theorem 5.6 and relabel its
subsequence $u_j$. The potentials
\[
 w_j=P_\omega(u_j,u_{j+1},\ldots)
       =\lim_{r\to\infty}P_\omega(u_j,\ldots,u_{j+r})
                                                               \tag{9}
\]
are P-models and increase almost everywhere to $u$. In the theorem's
construction all the finite rooftops in (9) are nontrivial, and the
tails are nontrivial of positive mass, after deleting finitely many
indices. Lemma \ref{roof} makes every finite rooftop I-model.
DX Lemma 2.21(i) makes $w_j$ I-model on passage to the decreasing
limit in $r$. Its Lemma 2.21(iii), now applied to $w_j\nearrow u$
and using $M_n(u)>0$, gives $P_Iu=u$. All applications concern the
same fixed K\"ahler class; neither global sections nor a polarization
are present.
\end{proof}

\section{Why usual maximal rays have I-model interior levels}
The next argument supplies the nonprojective step explicitly, rather
than importing the projective ambient hypothesis in DXZ Section 3.1.

\begin{lemma}[Local Gauss formula]\label{gauss}
Let $\chi_\lambda$ be a test curve from zero with cutoff at most zero,
and let $W_t=\sup_\lambda(\chi_\lambda+t\lambda)$ be its sublinear
subgeodesic. For a rationally scaled divisorial valuation $v$ over a compact complex
manifold, let $\nu_v(\chi)$ be its generic divisorial coefficient in
convention (1). Then
\[
 W^\NA(v)=\sup_{\lambda<\lambda_+}
                          (\lambda-\nu_v(\chi_\lambda)).    \tag{10}
\]
The formula holds for the analytic Gauss divisors used in $X^\beth$;
it does not require that $X$ be projective.
\end{lemma}
\begin{proof}
On $X\times\Delta$ the total potential is the regularized supremum
of $\chi_\lambda(x)-\lambda\log|\tau|^2$. In a coordinate chart,
adding a local smooth potential of $\omega$ makes these functions
psh. They are uniformly bounded above, since $\chi_\lambda\le0$,
$\lambda\le0$ and $|\tau|<1$. The same is true on a modification.
For a locally uniformly upper bounded family of psh functions,
the Lelong number of its regularized supremum equals the infimum of
the individual Lelong numbers. Indeed Choquet's lemma reduces to a
countable family, finite maxima have the minimum Lelong number, and
their increasing $L^1$ limit has that same limiting number by upper
semicontinuity and monotonicity. This is the local proof of DX
Lemma 3.14, whose ambient space is any complex manifold.

Let $F$ be a normalized Gauss divisor with $b=\operatorname{ord}_F\tau$.
The coefficient of the summand is
$b(\nu_v(\chi_\lambda)-\lambda)$. This is a local coefficient
calculation: after making the divisor underlying $v$ smooth, the
Gauss valuation is realized by the weighted blowup in its normal
coordinate and $\tau$. The pullback coefficient of a potential
independent of $\tau$ is its normal-coordinate coefficient times
the normal weight; the coefficient of $\log|\tau|^2$ is $b$.
Equivalently one uses the analytic ideal Gauss rule
$\sigma(v)(\sum a_i\tau^i)=\min_i(v(a_i)+i)$.
Analytic Gauss divisors and their restrictions are precisely those
of MP Lemma 2.4.2 and Theorem 2.5.5. Apply the supremum rule at
generic points of $F$, divide by $b$, and negate the coefficient.
The cutoff can be approached from the left by concavity; the
Legendre supremum is unchanged if only $\lambda<\lambda_+$ is used.
This proves (10) with the normalization of the actual usual datum.
\end{proof}

\begin{proposition}\label{maxI}
For any usual-datum maximal finite-energy ray $U$ from zero, every
genuine interior Legendre level $\chi_\lambda$, $\lambda<\lambda_+$,
is I-model. In particular this holds for the canonical model rays
in Section 1.
\end{proposition}
\begin{proof}
Subtract an affine time function if necessary to put the cutoff at
most zero. Legendre duality on a compact K\"ahler manifold makes
the levels normalized P-models. Apply the I-maximization of test
curves in DXZ Section 2.2: replace interior levels by
$\eta_\lambda=P_I[\chi_\lambda]$, take the left limit at the cutoff,
and put $-\infty$ above it. This is an I-maximal test curve from
$P_I[0]=0$. Its inverse Legendre transform $W$ is a weak geodesic
ray from zero and satisfies $W_t\ge U_t$. It has finite energy:
each level has no smaller mass, and the finite-energy test-curve
integral $\int_{-\infty}^{\lambda_+}(M_n-1)\,d\lambda$ is
increased and is still at most zero.

By DX Proposition 2.18(ii) the interior old and new levels have the
same multiplier ideals at every positive coefficient. DX Theorem
2.13, in its general compact-K\"ahler Section 2.4, identifies their
coefficients along all projective analytic modifications. Thus
Lemma \ref{gauss} gives $W^\NA=U^\NA$ on divisorial points. The
usual psh extensions agree on $X^\beth$ by caller R's divisorial
determination. Maximality of $U$, with the same initial zero, now
gives $U\ge W$. Hence $U=W$. Injectivity of the Legendre
correspondence gives $\chi_\lambda=P_I\chi_\lambda$ at every
interior level. Restoring the affine time shift merely translates
the level parameter and does not change this assertion.
\end{proof}

\section{An explicit diffuse polar singularity}
We construct the measure to ensure polar support; a general nonatomic
measure on a Cantor set would not suffice. Inside a small real interval
in the affine chart of $C=\mathbf P^1$, form nested binary intervals.
At stage $m$ each of the $2^m$ intervals has radius
$r_m=\exp(-4^m)$; its two children have radius $r_{m+1}$ and centers
near the two quarter points of the parent. They are disjoint and
contained in it. Let $K$ be the intersection of their unions and let
$\nu$ be the Bernoulli measure giving each stage-$m$ interval mass
$2^{-m}$. It is a nonatomic probability supported on $K$.
Use the Fubini--Study form $\omega_C$ of mass one and its Green kernel
\[
 G(z,a)=\log|z-a|^2-\log(1+|z|^2)-\log(1+|a|^2)\le0,
 \qquad h(z)=\int_K G(z,a)\,d\nu(a).                         \tag{11}
\]
The kernel is understood in homogeneous coordinates at infinity.
Its negative part has a uniformly bounded integral against smooth
area, so $h\in L^1(C)$ by Fubini. Also
$\ddc h=\nu-\omega_C$, so $h$ is $\omega_C$-psh.
If $z\in K$, the cylinder containing $z$ gives
\[
 h(z)\le 2^{-m}\log(4r_m^2)\longrightarrow-\infty.          \tag{12}
\]
Outside $K$, the kernel is uniformly finite on the support of $\nu$
locally, so $h$ is finite. Thus its pole set is exactly $K$, which
in particular is polar and has smooth area zero.

\begin{lemma}\label{integrability}
For every $a>0$, $e^{-a h}$ is locally integrable. Consequently,
for $0<c<1$, $u_c=ch$ has all multiplier ideals trivial and
its nonpluripolar mass is $1-c$.
\end{lemma}
\begin{proof}
Atomlessness on the compact set implies
$\sup_x\nu(B(x,r))\to0$ as $r\to0$: otherwise choose shrinking
balls of a fixed positive mass, pass their centers to a limit, and
obtain an atom. Fix $a>0$. Around any point choose a ball whose
doubled ball has mass $m<1/a$. For points in the smaller ball,
the far part of (11) is bounded below. If $m>0$, Jensen's inequality
for the probability $m^{-1}\nu$ on the doubled ball gives
\[
 e^{-a h(z)}\le C\int |z-b|^{-2am}\,\frac{d\nu(b)}m.
                                                               \tag{13}
\]
The smooth terms in the Green kernel are included in $C$. Because
$am<1$, integrate (13) over the smaller ball and apply Fubini;
the integrals of $|z-b|^{-2am}$ are uniformly finite. If $m=0$
the potential is locally bounded there. The argument applies to
any exponent and hence also to $ch$.

Finally $\omega_C+\ddc(ch)=(1-c)\omega_C+c\nu$.
In dimension one its nonpluripolar part is the restriction to the
complement of the pole set. The part $c\nu$ is removed, while
$\omega_C(K)=0$, giving mass $1-c$.
\end{proof}

Let $q_c=P_C[ch]$. The P-envelope preserves top mass and is model
at positive mass, so
\[
 q_c\ge ch,\quad q_c\le0,\quad
 \int_C\langle\omega_C+\ddc q_c\rangle=1-c,
 \quad \MI(aq_c)=\OO_C\ (a>0).                             \tag{14}
\]
The mass-preserving envelope assertion and its positive-mass
idempotence are DDNL Section 2 and Proposition 2.6, in their big
class scope; here the class is K\"ahler. Integrability in (14)
also follows directly from $q_c\ge ch$ and Lemma \ref{integrability}.
Thus $P_Iq_c=0$, whereas $q_c\ne0$ by its mass. The diffuse-polar
mechanism on a projective curve is the known distinction in DX
Example 2.19; our extension below is on a nonprojective manifold,
with an explicit actual ray and a general analytic closedness proof.

\section{The nonprojective manifold and its product envelopes}
Choose a two-dimensional complex torus $Y$ with
$H^{1,1}(Y)\cap H^2(Y,\mathbf Z)=\{0\}$. For completeness such
a torus exists by the following elementary construction. On
$\mathbf R^4/\mathbf Z^4$ consider the connected space of complex
structures with a fixed orientation. For each nonzero integral
alternating form $A$, the condition that $A$ be J-invariant is a
proper closed real analytic condition. To see properness choose an
oriented basis with $A(e_1,e_2)\ne0$, and put
\[
 Je_1=s e_3,\quad Je_3=-s^{-1}e_1,\quad
 Je_2=t e_4,\quad Je_4=-t^{-1}e_2.
\]
Take $st<0$ for the chosen complex orientation, and vary $st$;
$A(Je_1,Je_2)=stA(e_3,e_4)$ cannot always equal $A(e_1,e_2)$.
Baire's theorem avoids all these countably many conditions.
The averaging description of torus cohomology identifies the
integral $(1,1)$ classes with these invariant forms. Any constant
positive Hermitian form is K\"ahler. An ample bundle would have a
nonzero integral positive $(1,1)$ class, so $Y$ is not projective.

Put
\[
 X=C\times Y,\qquad \omega=p_C^*\omega_C+p_Y^*\omega_Y,
 \qquad n=3,\qquad V=n\int_Y\omega_Y^{n-1}.                 \tag{15}
\]
The same argument works with any nonprojective K\"ahler factor
having no nonzero integral $(1,1)$ class. A projective $X$ would
make its closed fiber $Y$ projective. Moreover $[\omega]$ cannot
be proportional to a line-bundle class: restrict that class to $Y$.

\begin{lemma}\label{product}
For $f\in\PSH(C,\omega_C)$, $f\le0$,
\[
 P_X[p_C^*f]=p_C^*P_C[f].                                  \tag{16}
\]
For $Q_c=p_C^*q_c$ one has
\[
 P_X[Q_c]=Q_c,\quad P_{I,X}[Q_c]=0,\quad
 M_k(Q_c)=1-\frac{k c}{n}\quad(0\le k\le n).                \tag{17}
\]
\end{lemma}
\begin{proof}
First work with the finite rooftop $P_X(p_C^*f+A,0)$.
Pulling back a curve competitor gives a product competitor.
Conversely, restricting a product competitor to each fiber
$C\times\{y\}$ gives an $\omega_C$-psh function or the identically
$-\infty$ function, bounded by $\min(f+A,0)$. It is therefore at
most $P_C(f+A,0)$. This upper bound is usc on the product, so it
also bounds the regularized supremum of the competitors. This
proves equality for every $A$, and passage to the increasing
regularized limit proves (16).

The multiplier ideals of $Q_c$ are trivial by the local product
Fubini theorem and (14). Thus zero is admissible in (4) and its
I-envelope is zero. To calculate the products, truncate $q_c$ by
$\max(q_c,-N)$ on the curve. The resulting current on the product
is the sum of its curve current and $p_Y^*\omega_Y$; two curve
factors vanish. After restriction to $\{q_c>-N\}$ and passage
to the nonpluripolar limit, the integrand in (2) is
\[
 \big((n-k)\omega_C+k\langle\omega_C+\ddc q_c\rangle\big)
                       \wedge\omega_Y^{n-1}.               \tag{18}
\]
The pole set of $q_c$ has smooth area zero, so no smooth curve
mass is lost in the first term. Its integral is
$(n-k)+k(1-c)=n-kc$ times $\int_Y\omega_Y^{n-1}$.
Divide by (15) to obtain (17). In particular these are positive
raw masses, and none is replaced by a probability measure at a
singular level.
\end{proof}

\section{The actual weak ray and failure of every model sequence}
Fix $0<c_0<1$ and start with the raw test curve on $C$
\[
 a_\lambda=\begin{cases}
 0,&\lambda\le-1,\\
 c_0(\lambda+1)h,&-1<\lambda\le0,\\
 -\infty,&\lambda>0.
 \end{cases}                                               \tag{19}
\]
It is decreasing, concave and upper semicontinuous in the level
parameter, including the extended values at points of $K$.
Its limit at $-\infty$ is zero. P-maximize (19) as in DXZ
Section 2.2 and formula (13). For $-1<\lambda<0$ its levels are
$q_{c_0(\lambda+1)}$, below $-1$ they are zero, and the value at
zero is their decreasing left limit. That endpoint equals $q_{c_0}$:
DDNL Proposition 4.8 and Corollary 4.7 make the left limit P-model
of mass $1-c_0$; it dominates $q_{c_0}$ with the same positive
mass. DDNL Theorem 2.3 applied to this ordered pair makes their
P-envelopes equal. Pull the maximized curve back to $X$.
Lemma \ref{product} shows that it is still a maximal test curve;
its concavity and closed endpoints are preserved by pullback.
Denote its levels by $\chi_\lambda$.

The relative Ross--Witt Nystr\"om theorem, DXZ Theorem 2.6(ii)--(iii),
applies to this compact K\"ahler manifold and positive-volume
reference zero. Hence the inverse transform (6) is an actual
finite-energy weak geodesic ray. More concretely the available
level $\lambda=-1$ and the upper bound on all levels give
$-t\le U_t\le0$. Thus all times are bounded finite-energy
potentials, and $U_t\to0$ strongly as $t\downarrow0$.
Its spectrum is contained in $[-1,0]$. The energy formula in that
same theorem and (17) give
\[
 \lim_{t\to\infty}\frac{E(U_t)}t
 =\int_{-1}^0\big(M_n(\chi_\lambda)-1\big)\,d\lambda
 =-\int_{-1}^0c_0(\lambda+1)\,d\lambda=-\frac{c_0}2.        \tag{20}
\]
The explicit mixed masses in (17) prove (8), including the genuine
closed endpoint at zero. Formula (5) also gives the useful fixed
scale comparison
\[
 \ds^V([\chi_\lambda],[0])=\tfrac12c_0(\lambda+1)>0
                    \quad(-1<\lambda\le0).                \tag{21}
\]

All genuine levels have trivial multiplier ideals. They therefore
have zero generic coefficients on all projective analytic
modifications by DX Theorem 2.13, applied to comparison with zero.
Lemma \ref{gauss} gives $U^\NA(v)=\sup_{\lambda<0}\lambda=0$
on divisorial points, and caller R extends it as the zero function
on the full carrier. Its maximal ray from zero is the stationary
ray. Equation (20) proves that $U$ is not that ray. Caller R's
arbitrary-ray entropy classification, with the initial entropy
$H(0)=0$, gives its infinite slope asserted in Theorem \ref{main}.

Now fix $\lambda\in(-1,0)$ and suppose a sequence $U^j$ of
usual-datum maximal rays from zero satisfied (7). A sequence that
is identically $-\infty$ at this level infinitely often already
fails the genuine-level requirement. For the remaining sequence,
Proposition \ref{maxI} makes each interior level I-model. If a
level happens to be the cutoff of an approximating ray, the same
holds: its left limits are I-model and the decreasing-limit
part of DX Lemma 2.21 applies whenever the cutoff level is
genuine. Thus $P[\chi_{j,\lambda}]$ is I-model.
Since the target level has mass $1-c_0(\lambda+1)>0$,
Proposition \ref{closed} would make it I-model. But its
I-envelope is zero while its mass is strictly less than one,
a contradiction. This proves claims 1--4 of Theorem \ref{main}. Claim 5 is proved next.

\section{Model-compatible weights and the minimal raw-mass obstruction}\label{minimal}
The following model category contains canonical relatively K\"ahler
cohomological model rays, their canonical finite-energy nef/obstacle
recovery rays, and locally bounded semipositive total weights on such
actual positive configurations. For the last case we mean an actual
sublinear psh subgeodesic $A_t$ from zero whose total weight, after
removing its compatible vertical divisor, is locally bounded on the
model near the central fiber and on compact finite-time annuli, including
the initial boundary. In this compatible-weight branch the canonical
model weak ray has the same locally bounded compatible extension;
caller R supplies this on relatively K\"ahler configurations. Canonical
nef/obstacle rays enter separately through their usual maximality.
This includes smooth positive model metrics.
We also allow any actual finite-energy I-maximal test-curve ray from
zero, hence any genuine finite analytic flag implementation of this
kind. Formal ideals or nonpositive configurations without an actual ray
are not asserted to define approximants. Extra nonmodel singularities
introduced into a total weight are additional complex data, not locally
bounded model metrics in this category.

\begin{proposition}\label{Imaxusual}
An actual finite-energy I-maximal ray from zero is usual-datum maximal
on every compact K\"ahler manifold in a K\"ahler class.
\end{proposition}
\begin{proof}
Let $A$ be such a ray and $R$ its usual maximalization from zero, supplied
by caller R. Both have the same datum $\phi$, and $R\ge A$.
Proposition~\ref{maxI} makes the genuine interior levels of $R$ I-model,
as are those of $A$. Their common cutoff $b$ equals
$\phi(v_{\rm triv})$: the generic coefficient of a genuine potential
independent of time on the product central divisor is zero, so the
trivial-valuation instance of (10) gives the cutoff.

Fix any rational divisorial valuation $v$. For either test curve let
$f(\lambda)=\nu_v(\chi_\lambda)$ for $\lambda<b$. This function is
finite, nonnegative, nondecreasing and convex. Convexity follows by
applying monotonicity and additivity of generic coefficients to
concavity of the potentials. Finiteness is the ordinary local
finiteness of Lelong numbers of a genuine integrable psh potential
on a fixed modification. Moreover $\inf_{\lambda<b}f(\lambda)=0$:
the levels increase in $L^1$ to zero as $\lambda\to-\infty$.
On any fixed modification their monotone pullbacks increase to zero
almost everywhere: off the exceptional analytic set the map is an
isomorphism, and a pluripolar exceptional set has zero smooth volume.
After adding a local smooth potential, they are locally uniformly
bounded above psh functions. Monotone psh convergence therefore gives
local $L^1$ convergence on the modification as well. Upper
semicontinuity of point Lelong numbers bounds their limsup by zero.
The nonnegative generic coefficient along a divisor is at most each
point coefficient on it, so it too tends to zero.

For $q>0$ rational, (10) at the valuation $v/q$ gives
\[
 g(q):=q\phi(v/q)=\sup_{s<b}(qs-f(s)).                     \tag{23}
\]
A finite convex nondecreasing $f$ with infimum zero on $(-\infty,b)$
is recovered by these positive conjugate parameters:
\[
 f(\lambda)=\sup_{q\in\mathbf Q_{>0}}(q\lambda-g(q)).       \tag{24}
\]
Here is the endpoint check in this elementary convex duality. At an
interior point a positive supporting slope gives equality in the full
real supremum. The function $g$ is finite and continuous for $q>0$,
so rational slopes suffice by approximation. If only supporting slope
zero is needed, convexity, nonnegative monotonicity and the zero
infimum imply $f(\lambda)=0$. Also $g(q)\to0$ as $q\downarrow0$:
$g(q)\le qb$, while any fixed $s$ with $f(s)<\epsilon$ gives
$g(q)\ge qs-\epsilon$. Letting $q\downarrow0$ and then
$\epsilon\downarrow0$ proves the needed zero-slope equality.
Fenchel's inequality gives the reverse bound for every $q$.

Thus the two test curves have the same coefficients on all rational
scaled divisors at each interior level. They are I-equivalent by
DX Theorem 2.13: coefficients on point blowups also give all point
Lelong numbers on every projective analytic modification. As both
levels are I-model, they are equal. The closed cutoff is their left
limit, and above it both curves are identically minus infinity.
Legendre injectivity gives $A=R$, proving maximality. This proves the
fixed-reference comparison, rather than importing MP's Section 5.2
comparison sketch or a projective density theorem.
\end{proof}

\begin{lemma}\label{compatible}
If $A$ is a locally bounded model-compatible total weight as above and
$r$ is its canonical model weak ray from zero, then
$|A_t-r_t|\le C$ for one finite $C$ at all points and all $t\ge0$.
Consequently their genuine Legendre levels have the same bounded
singularity type, the same P-envelope and the same raw mixed masses.
Also $A^\NA=r^\NA$ and
$\lim_{t\to\infty}E(A_t)/t=E_\alpha(A^\NA)$.
\end{lemma}
\begin{proof}
Both total weights become locally bounded after removal of the same
vertical divisor. Their difference is bounded near the central fiber
on a finite cover of the compact model. It is also bounded on each
remaining compact time annulus and at the smooth initial boundary.
Use one annulus to join the central neighborhood to that boundary.
This gives the asserted global constant, with no uniformity in a
sequence of different models asserted. Taking infima in time yields
$\chi_r-C\le\chi_A\le\chi_r+C$ at each level. Thus placeholders
coincide, and genuine levels have identical bounded singularity type.
The P-envelope depends only on that type; nonpluripolar mixed masses
are likewise invariant, by mass monotonicity in both directions.
Bounded differences do not change generic total coefficients, so the
usual data agree. Energy monotonicity and translation give
$|E(A_t)-E(r_t)|\le C$, and caller R gives the energy slope of $r$.
This proves the last assertion without assuming $A$ is geodesic.
\end{proof}

\begin{proof}[Proof of Theorem~\ref{main}, claim 5]
For a canonical model ray the assertion needs no replacement. For an
I-maximal flag ray Proposition~\ref{Imaxusual} identifies it with its
usual maximal ray. For a locally bounded compatible weight use
Lemma~\ref{compatible}. In every case there is a usual maximal
finite-energy ray $r^j$ from zero with datum $\phi_j$ such that its
interior normalized P levels $\eta_{j,\lambda}$ have exactly the
raw masses in (22). Write
\[
 b_j=\phi_j(v_{\rm triv}),\qquad c_j=E_\alpha(\phi_j).
\]
The first is the cutoff by (10) at the product central divisor, and
$c_j$ is the energy slope by caller R. The general relative
Ross--Witt Nystr\"om energy formula gives
\[
 b_j-c_j=\int_{-\infty}^{b_j}
                  (1-M_n(\eta_{j,\lambda}))\,d\lambda.     \tag{25}
\]
All these integrands are nonnegative: the genuine levels are
$\omega$-psh and have mass at most the fixed K\"ahler volume.
The integral is finite because $r^j$ has finite energy.

If (22) held, then $b_j\to0$ and $c_j\to0$. Fix
$0<\epsilon<1$. For all large $j$, $b_j>-\epsilon$, so the
fixed interval $(-1,-\epsilon)$ lies strictly inside the cutoff.
By (25) and Fatou's lemma,
\[
 0=\lim_j(b_j-c_j)\ \ge\
 \liminf_j\int_{-1}^{-\epsilon}
                   (1-M_n(\eta_{j,\lambda}))\,d\lambda
 \ \ge\ \int_{-1}^{-\epsilon}c_0(\lambda+1)\,d\lambda.
                                                               \tag{26}
\]
The right side is strictly positive. Letting $\epsilon\downarrow0$
would give the sharper lower bound $c_0/2$, but one fixed interval
already contradicts (26). The proof uses only pointwise recovery of
the raw top mass on the interior, not a singularity metric, uniform
level convergence, fixed-time entropy, an analytic-energy recovery
assumption, or a normalization at a zero-mass boundary.
\end{proof}

\section{Comparison with the original residual problem}
Original P19.2 asks for model approximations preserving required
energy, entropy and singularities for arbitrary finite-energy weak
rays on compact K\"ahler manifolds; it explicitly keeps finer P
data separate from I data. The minimal incompatible requirements (22) recover the actual usual
datum even at just one retained divisorial point, its normalized
non-Archimedean energy, and the raw top mass at each interior level.
They do not prescribe an additional norm for P singularities. The
stronger distance signature (7) is a separate obstruction and also
records every mixed mass in (2). Our obstruction is at an interior
positive-mass level of a bounded actual ray from a smooth finite-entropy
start, on a nonprojective manifold in a genuinely transcendental
class. It therefore does not rely on absolute/relative changes at a
singular start, raw zero mass, an identically $-\infty$ placeholder,
or an erroneous choice of one approximation sequence.

The minimal raw-mass argument excludes all canonical cohomological
models, locally bounded compatible model metrics, and actual I-maximal
flag rays in the stated category. Its scalar conditions are necessary
for simultaneous recovery of the retained usual data, non-Archimedean
energy and actual raw singularity profile. The larger usual-maximal
category is excluded as well. Separately, Propositions \ref{maxI} and
\ref{closed} exclude finer-P distance recovery without any NA-energy
hypothesis. These are failures of existence in the specified model
categories, not failures of one chosen sequence. It leaves possible
approximation statements for I-maximal rays, for coarser ideal data,
or using additional genuinely nonmodel complex singularities as
input. The known curve distinction alone would not settle a residual
transcendental problem; here the general analytic closedness argument,
the nonprojective product and the actual ray supply that ambient
extension. P19.3 and P19.4 concern different goals and are unaffected.

This manuscript is a proposed full-original counterexample for this
frozen minimal usual-datum/NA-energy/raw-top-mass signature, conditional
only on the complete
accepted caller theorem R and the precisely cited ordinary envelope
and Legendre results. Independent review must check both its proof
and whether this signature answers the exact original completion
criterion. There is currently no independent verdict, and original
P19.2 remains open in the research catalogue.

\appendix
\section{Source application and reading boundaries}
The complete accepted caller R is reused as an explicit mathematical
grant; it supplies the actual usual-datum carrier, divisorial
determination, maximality and the entropy classification. Its new
applications here use the fixed smooth compact K\"ahler class,
start zero, and convention (1). No theorem from its future
P19.2/P19.3/P19.4 programme is imported.

Primary versions were downloaded on 6 October 2026 to a private
reading directory and bound by hashes in a separate application
record. The pertinent complete units read are DX's general
Section 2.4 definitions, Proposition 2.18 and Lemma 2.21, and
its local Lemma 3.14; DDNL's Lemma 4.3, Propositions 4.6 and 4.8,
Corollary 4.7, Lemmas 5.1--5.2 and full Theorems 5.4 and 5.6;
and DXZ's relative
Section 2.2, Legendre theorem and maximization constructions.
The cited mass preservation and full-mass characterization in
DDNL Section 2 were read with their stated hypotheses. MP's
model lemma and usual maximality statements were read with their
proofs; its analytic Gauss theorem statement and local reduction
were read, but its whole recursive local-algebraic proof was not
reconstructed here. That carrier is already part of caller R.
No claim is made to have read an entire primary paper or to have
independently reconstructed every pluripotential foundation.
The published projective-only hypothesis of DXZ Section 3.1 is
retained: Lemma \ref{gauss} gives the local extension needed here.
The new convex duality proves I-maximal-to-usual-maximal comparison
from its complete local formula and the caller R maximalization.
The compatible-weight comparison and the raw-mass/Fatou obstruction
are new elementary arguments; neither assumes $d_{\mathcal S}$
convergence. Their exact model category and match to all required
original data still require independent review.

\begin{thebibliography}{9}
\bibitem{R} Complete accepted caller theorem R,
\emph{Entropy slopes of finite-energy K\"ahler rays: calibration,
recovery, and arbitrary starting points}, original P19.1 paper,
6 October 2026; supplied in full to the independent review.
\bibitem{DX} T. Darvas and M. Xia, \emph{The closures of test
configurations and algebraic singularity types}, Advances in
Mathematics 397 (2022), 108198,
\href{https://research.chalmers.se/publication/528300/file/528300_Fulltext.pdf}{published primary PDF}.
\bibitem{DDNL} T. Darvas, E. Di Nezza and C. H. Lu,
\emph{The metric geometry of singularity types},
\href{https://arxiv.org/pdf/1909.00839v1}{arXiv:1909.00839v1},
2 September 2019, Sections 2--5.
\bibitem{DXZ} T. Darvas, M. Xia and K. Zhang,
\emph{A transcendental approach to non-Archimedean metrics of
pseudoeffective classes}, Commentarii Mathematici Helvetici 100
(2025), 269--322,
\href{https://ems.press/content/serial-article-files/49836}{published primary PDF}, Section 2.2.
\bibitem{MP} P. Mesquita-Piccione,
\emph{A non-Archimedean theory of complex spaces and the cscK problem},
\href{https://arxiv.org/pdf/2409.06221v2}{arXiv:2409.06221v2},
Sections 2.4--2.5 and 5.1; the same fixed-manifold carrier as caller R.
\end{thebibliography}
\end{document}
END COMPLETE MATHEMATICAL BODY ENTIRE ELEVEN-PAGE212 CANDIDATE INCLUDING EVERY PROOF AND APPENDIX

BEGIN COMPLETE MATHEMATICAL BODY AUTHOR QUOTE-FREE SOURCE APPLICATION PROVENANCE ONLY
{
  "recorded_utc": "2026-10-06T17:52:56.969845+00:00",
  "paper": "/workspace/research/root-checks/P19.2-transcendental-model-energy-and-raw-profile-obstruction-candidate-20261006-continuation212.tex",
  "paper_sha256": "064462d28d560d5ccbcd5bbecd3dc3aade4b3df5d672cb44bd73132937b0002c",
  "classification": "Quote-free author application record; source hashes and reading boundaries are provenance, not independent mathematical certification.",
  "complete_caller_grants": [
    {
      "id": "R",
      "file": "/workspace/research/deliverables/original-P19.1/P19.1-paper.tex",
      "sha256": "d9adffa7737edd6698f2045f3c2152589d5488891bc4fcaff1e0f08c6cf79a1b",
      "bytes": 40979,
      "origin": "Complete independently accepted original P19.1 body, identical to the R grant frozen in active168.",
      "new_application": "Same compact smooth Kahler fixed class; initial0; usual normalized Gauss datum, divisorial determination, actual model maximality and arbitrary-ray entropy classification.",
      "fresh_local_root_read_this_application": [
        [
          40,
          163
        ]
      ],
      "prior_whole_body_read_and_acceptance_reused": true
    }
  ],
  "primary_sources": [
    {
      "name": "DX2022-published",
      "requested_url": "https://research.chalmers.se/publication/528300/file/528300_Fulltext.pdf",
      "returned_url": "https://research.chalmers.se/publication/528300/file/528300_Fulltext.pdf",
      "pdf_sha256": "127ac2fba2a9a47f7efda1ea32b62683711c8b9bb4adde0d23a19956d063345b",
      "bytes": 1201335,
      "text_sha256": "9b22a391c63e85dff977c2a6a89cbc993471680c38cbc35275738cfc2ea173ac",
      "root_read_local_inclusive_lf": [
        [
          1043,
          1255
        ],
        [
          2177,
          2200
        ]
      ],
      "units": [
        {
          "inclusive_lf": [
            1043,
            1255
          ],
          "sha256_of_exact_unit_text": "46ef1dc975e3f099f4fdf66965f8df29f3022fb36b9b356444a9223b59a10a16"
        },
        {
          "inclusive_lf": [
            2177,
            2200
          ],
          "sha256_of_exact_unit_text": "c4b3f37821e17898f5351dd7f4f657bfafe584d71fe686363cc52d3ff94cf838"
        }
      ],
      "new_application_and_limit": "General compact-Kahler Section2.4 definitions, ideal-order/Lelong equivalence, PI envelope and model facts, full Proposition2.18 and Lemma2.21; complete local Lemma3.14. New applications: lower roof closure and unchanged divisorial coefficients after I-maximization. No projective global-section density theorem imported.",
      "whole_primary_paper_read": false,
      "independent_review_evidence": false,
      "third_party_full_text_published": false
    },
    {
      "name": "DDNL2019-v1",
      "requested_url": "https://arxiv.org/pdf/1909.00839v1",
      "returned_url": "https://arxiv.org/pdf/1909.00839v1",
      "pdf_sha256": "68ac421684f6c46705e4e875887b0cd40f997fbcfad29efd11a55415570b0a36",
      "bytes": 369429,
      "text_sha256": "2f012285d57f0465f1e9073b03eeb9fb9e5ed51e3e84a30f2a78d528b97f7278",
      "root_read_local_inclusive_lf": [
        [
          1,
          40
        ],
        [
          245,
          410
        ],
        [
          680,
          800
        ],
        [
          840,
          1057
        ],
        [
          1135,
          1420
        ]
      ],
      "units": [
        {
          "inclusive_lf": [
            1,
            40
          ],
          "sha256_of_exact_unit_text": "4bd62c61794d94d3eaf53bf77b23f7036297464c89f40537d2245cbb554155e8"
        },
        {
          "inclusive_lf": [
            245,
            410
          ],
          "sha256_of_exact_unit_text": "cdac62bba2bfdb3ca08178cf954bf7960d0a022df20e0747e2d23709a88a7ab5"
        },
        {
          "inclusive_lf": [
            680,
            800
          ],
          "sha256_of_exact_unit_text": "7cd1f09e77d496be5709ab8af578b8f094e7fffb30bb5bc9d5f013b5f22d5b2c"
        },
        {
          "inclusive_lf": [
            840,
            1057
          ],
          "sha256_of_exact_unit_text": "bdbbe22933671d61f1856b95b00d233b2e7d0011ba2e332add4e7df954206c63"
        },
        {
          "inclusive_lf": [
            1135,
            1420
          ],
          "sha256_of_exact_unit_text": "9306800e789c7f5313af737b30abd32db22171db581f347a5de9e20457a579b4"
        }
      ],
      "new_application_and_limit": "Big-class compact-Kahler ambient, exact P mass preservation/full-mass characterization/positive-mass ceiling, singularity metric ordered formula and mixed/top-mass continuity, entire Lemma4.3 and Propositions4.6/4.8 with Corollary4.7, complete Lemmas5.1/5.2 and Theorems5.4/5.6. New applications: lower roof sandwich makes I-model subset closed without polarization; positive-mass decreasing endpoint. Some returned surrounding ranges include other units, not every recursive foundation or whole PDF.",
      "whole_primary_paper_read": false,
      "independent_review_evidence": false,
      "third_party_full_text_published": false
    },
    {
      "name": "DXZ2025-published",
      "requested_url": "https://ems.press/content/serial-article-files/49836",
      "returned_url": "https://ems.press/content/serial-article-files/49836",
      "pdf_sha256": "4aa758fafebc6fec23648c4991a638c1bb03a03d2b45b2404997a5ef37be9ca6",
      "bytes": 631014,
      "text_sha256": "de9153f70c2299cc114b5cc096117102340ea1ad9c783797c6a34bc155fefa36",
      "root_read_local_inclusive_lf": [
        [
          420,
          770
        ]
      ],
      "units": [
        {
          "inclusive_lf": [
            420,
            770
          ],
          "sha256_of_exact_unit_text": "a5bbea177d518b18695b0aa3f7418651ff426f876f4ee4f0fd4ce85d38f4c879"
        }
      ],
      "new_application_and_limit": "Entire relative compact-Kahler Section2.2 definition/Legendre correspondence/energy and P/I maximization with positive-mass reference0. Projective-only Section3.1 was separately checked through web layout and is NOT silently invoked on the nonprojective X. New local Gauss lemma replaces that ambient use.",
      "whole_primary_paper_read": false,
      "independent_review_evidence": false,
      "third_party_full_text_published": false
    },
    {
      "name": "MP2025-v2",
      "requested_url": "https://arxiv.org/pdf/2409.06221v2",
      "returned_url": "https://arxiv.org/pdf/2409.06221v2",
      "pdf_sha256": "9eb2ea7686a5962ebc11c5eacd23b0cb3dcb081e27ac48292933f291fc82cb23",
      "bytes": 843381,
      "text_sha256": "2872abe0939b0281275ee6618130b63b8ee25ee3b0d5b0d816ce116906207b57",
      "root_read_local_inclusive_lf": [
        [
          728,
          737
        ],
        [
          905,
          1058
        ],
        [
          2425,
          2587
        ]
      ],
      "units": [
        {
          "inclusive_lf": [
            728,
            737
          ],
          "sha256_of_exact_unit_text": "d5ae7201cfab6f557e56853dfc1d1e3c470e7a642da4810c6a42c31482487cf0"
        },
        {
          "inclusive_lf": [
            905,
            1058
          ],
          "sha256_of_exact_unit_text": "bc4cd9a2bd8906086d4835c9ebb030e0fb5668b101a6ee90a23f481ed9b2a2a9"
        },
        {
          "inclusive_lf": [
            2425,
            2587
          ],
          "sha256_of_exact_unit_text": "00862b7d8f3007a7e9799ac297508ebd35d2c38767f36bb8a8b371ffc3ad0add"
        }
      ],
      "new_application_and_limit": "Rational divisorial normalization, complete Gauss bijection Lemma2.4.2, cohomological model definitions, analytic Gauss Theorem2.5.5 statement and local-reduction outline only; whole model Lemma5.1.8 and usual maximality definitions/theorem/proof. The recursive proof of Theorem2.5.5 was not read in full this application; the complete caller R supplies that fixed-manifold carrier. Do not infer whole MP reading or use its Section5.2 comparison sketch as a proof.",
      "whole_primary_paper_read": false,
      "independent_review_evidence": false,
      "third_party_full_text_published": false
    }
  ],
  "own_new_arguments": [
    "I-model finite lower-roof closure and DDNL lower-tail dS closedness without global sections",
    "Local analytic Gauss formula and I-maximization comparison proving all usual-maximal interior levels I-model",
    "Explicit superexponentially small binary Cantor probability, Jensen exponential integrability and exact diffuse lost mass",
    "Nonprojective generic two-torus, product envelope equality, all actual raw mixed products",
    "Bounded actual RW ray, closed positive endpoint, NA0 and radial energy defect; all-model-sequence obstruction",
    "Converse I-maximal to usual-maximal by positive convex conjugacy, rational divisorial rescaling, monotone pullback Lelong limit and ideal-equivalence on all modifications",
    "Locally bounded compatible model total weights and canonical rays differ by one all-time finite constant, preserving every P type and raw mass",
    "Minimal Fatou obstruction to simultaneous trivial-valuation datum, NA energy and interior raw top-mass recovery; no dS or analytic-energy recovery hypothesis"
  ],
  "original_counterexample_scope_requires_independent_judgment": true,
  "original_closed": false,
  "native_author_canonical_result": null,
  "independent_verdict": null,
  "no_private_active_output_read": true,
  "no_hot_feedback": true,
  "new_source_application": "The exact previously read primary units and complete callerR are reused in the new convex-dual/compatible-weight/Fatou proofs. No author ledger or earlier reviewer result is independent evidence for this review.",
  "author_source_frozen_before_completed169_report_read": true,
  "primary_reading_boundaries_reused": true
}
END COMPLETE MATHEMATICAL BODY AUTHOR QUOTE-FREE SOURCE APPLICATION PROVENANCE ONLY

