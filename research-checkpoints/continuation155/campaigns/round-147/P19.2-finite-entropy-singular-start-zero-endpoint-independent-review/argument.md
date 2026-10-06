# Whole NEW unreviewed counterexample manuscript

\documentclass[10pt]{article}
\usepackage[a4paper,margin=26mm]{geometry}
\usepackage{amsmath,amssymb,amsthm,hyperref}
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}{Lemma}
\newcommand{\ddc}{dd^c}
\newcommand{\MA}{\operatorname{MA}}
\newcommand{\PP}{\mathbf P}
\title{A finite-entropy initial singularity can erase an absolute zero-mass endpoint}
\author{An unreviewed supporting candidate for Problem P19.2}
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
It is bounded on each finite time annulus. On the blowup over the
affine time chart its total current is $g^*\omega_{\rm FS}$, whose
$(n+1)$st power vanishes.
It therefore solves the actual homogeneous geodesic equation.
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
this unreviewed supporting candidate changes no completion count.
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


# Sole exact theorem grant: COMPLETE original P19.1 mathematical body

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
