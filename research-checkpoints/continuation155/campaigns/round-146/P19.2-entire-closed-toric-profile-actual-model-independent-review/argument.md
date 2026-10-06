# Complete unreviewed mathematical manuscript

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
\author{Research candidate for a restricted case of Problem P19.2}
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
part of the construction. This is an unreviewed theorem candidate in
one toric branch, with zero analytic starting point; it is not a solution
of the full residual hybrid approximation problem.
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
$a_i$ on \emph{all} of them, with sum exactly $c_j$, arbitrarily close
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
of $g_j$, include both $x=0$ and $x=1$. For a common denominator $M$
the sections are
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
is $b\delta_0+\omega$ on the outer region, with no interface atom;
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
Legendre biconjugacy recovers $u_t$. Thus the ray is maximal in
the standard test-curve correspondence, with datum (5).

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
The present paper has no independent acceptance and changes no
original-problem completion count.

\begin{thebibliography}{9}
\bibitem{stacks} The Stacks Project, tags
\href{https://stacks.math.columbia.edu/tag/0B5Y}{0B5Y},
\href{https://stacks.math.columbia.edu/tag/09MS}{09MS}, and
\href{https://stacks.math.columbia.edu/tag/0D2S}{0D2S}:
ampleness on proper curves, nilpotent thickenings, and relative ampleness.
\bibitem{levels} Standard analytic Legendre correspondence for closed
$P$-maximal test curves and maximal weak geodesic rays; the explicit
levels and their envelopes are proved here. A future independent
review must check this correspondence in the stated normalization.
\end{thebibliography}
\end{document}


# Supplementary exact finite arithmetic, not a universal proof

{
  "classification": "Root exact finite arithmetic observations for candidate189; not a universal proof or acceptance certificate.",
  "candidate_tex_sha256": "665c5860b98944730214e3a9d174e5f8b1e8dd15db61f3f25d2a8f7de03add8c",
  "original_closed": false,
  "rows": [
    {
      "target_slopes": [
        "1/5",
        "2/3",
        "3/2",
        "7/4",
        "5"
      ],
      "rays": [
        [
          0,
          1
        ],
        [
          1,
          5
        ],
        [
          1,
          4
        ],
        [
          1,
          3
        ],
        [
          1,
          2
        ],
        [
          2,
          3
        ],
        [
          1,
          1
        ],
        [
          3,
          2
        ],
        [
          5,
          3
        ],
        [
          7,
          4
        ],
        [
          2,
          1
        ],
        [
          3,
          1
        ],
        [
          4,
          1
        ],
        [
          5,
          1
        ],
        [
          1,
          0
        ]
      ],
      "ordinary_blowups": [
        {
          "left": [
            0,
            1
          ],
          "right": [
            1,
            0
          ],
          "inserted": [
            1,
            1
          ]
        },
        {
          "left": [
            0,
            1
          ],
          "right": [
            1,
            1
          ],
          "inserted": [
            1,
            2
          ]
        },
        {
          "left": [
            0,
            1
          ],
          "right": [
            1,
            2
          ],
          "inserted": [
            1,
            3
          ]
        },
        {
          "left": [
            0,
            1
          ],
          "right": [
            1,
            3
          ],
          "inserted": [
            1,
            4
          ]
        },
        {
          "left": [
            0,
            1
          ],
          "right": [
            1,
            4
          ],
          "inserted": [
            1,
            5
          ]
        },
        {
          "left": [
            1,
            2
          ],
          "right": [
            1,
            1
          ],
          "inserted": [
            2,
            3
          ]
        },
        {
          "left": [
            1,
            1
          ],
          "right": [
            1,
            0
          ],
          "inserted": [
            2,
            1
          ]
        },
        {
          "left": [
            1,
            1
          ],
          "right": [
            2,
            1
          ],
          "inserted": [
            3,
            2
          ]
        },
        {
          "left": [
            3,
            2
          ],
          "right": [
            2,
            1
          ],
          "inserted": [
            5,
            3
          ]
        },
        {
          "left": [
            5,
            3
          ],
          "right": [
            2,
            1
          ],
          "inserted": [
            7,
            4
          ]
        },
        {
          "left": [
            2,
            1
          ],
          "right": [
            1,
            0
          ],
          "inserted": [
            3,
            1
          ]
        },
        {
          "left": [
            3,
            1
          ],
          "right": [
            1,
            0
          ],
          "inserted": [
            4,
            1
          ]
        },
        {
          "left": [
            4,
            1
          ],
          "right": [
            1,
            0
          ],
          "inserted": [
            5,
            1
          ]
        }
      ],
      "central_multiplicities": [
        1,
        5,
        4,
        3,
        2,
        3,
        1,
        2,
        3,
        4,
        1,
        1,
        1,
        1
      ],
      "weights": [
        "1/117",
        "2/117",
        "1/39",
        "4/117",
        "5/117",
        "2/39",
        "7/117",
        "8/117",
        "1/13",
        "10/117",
        "11/117",
        "4/39",
        "1/9"
      ],
      "actual_divisor_coefficients": [
        "-7/9",
        "-454/585",
        "-901/1170",
        "-34/45",
        "-577/390",
        "-2491/3510",
        "-3541/1755",
        "-1928/585",
        "-7987/1755",
        "-8677/7020",
        "-10837/7020",
        "-949/540",
        "-1009/540"
      ],
      "actual_component_degrees": [
        "2/9",
        "1/585",
        "1/234",
        "1/117",
        "2/117",
        "5/351",
        "2/39",
        "7/234",
        "8/351",
        "1/52",
        "10/117",
        "11/117",
        "4/39",
        "1/9"
      ],
      "mass": "1",
      "energy": "-774727/1642680",
      "entropy": "1009/540",
      "endpoint_raw_mass": "2/9",
      "all_degrees_strictly_positive": true,
      "adjacent_determinants_one": true,
      "actual_monomial_min_orders_verified": true,
      "intersection_energy_equals_roof_area": true
    },
    {
      "target_slopes": [
        "3/7",
        "4/9",
        "9/2"
      ],
      "rays": [
        [
          0,
          1
        ],
        [
          1,
          3
        ],
        [
          2,
          5
        ],
        [
          3,
          7
        ],
        [
          4,
          9
        ],
        [
          1,
          2
        ],
        [
          1,
          1
        ],
        [
          2,
          1
        ],
        [
          3,
          1
        ],
        [
          4,
          1
        ],
        [
          9,
          2
        ],
        [
          5,
          1
        ],
        [
          1,
          0
        ]
      ],
      "ordinary_blowups": [
        {
          "left": [
            0,
            1
          ],
          "right": [
            1,
            0
          ],
          "inserted": [
            1,
            1
          ]
        },
        {
          "left": [
            0,
            1
          ],
          "right": [
            1,
            1
          ],
          "inserted": [
            1,
            2
          ]
        },
        {
          "left": [
            0,
            1
          ],
          "right": [
            1,
            2
          ],
          "inserted": [
            1,
            3
          ]
        },
        {
          "left": [
            1,
            3
          ],
          "right": [
            1,
            2
          ],
          "inserted": [
            2,
            5
          ]
        },
        {
          "left": [
            2,
            5
          ],
          "right": [
            1,
            2
          ],
          "inserted": [
            3,
            7
          ]
        },
        {
          "left": [
            3,
            7
          ],
          "right": [
            1,
            2
          ],
          "inserted": [
            4,
            9
          ]
        },
        {
          "left": [
            1,
            1
          ],
          "right": [
            1,
            0
          ],
          "inserted": [
            2,
            1
          ]
        },
        {
          "left": [
            2,
            1
          ],
          "right": [
            1,
            0
          ],
          "inserted": [
            3,
            1
          ]
        },
        {
          "left": [
            3,
            1
          ],
          "right": [
            1,
            0
          ],
          "inserted": [
            4,
            1
          ]
        },
        {
          "left": [
            4,
            1
          ],
          "right": [
            1,
            0
          ],
          "inserted": [
            5,
            1
          ]
        },
        {
          "left": [
            4,
            1
          ],
          "right": [
            5,
            1
          ],
          "inserted": [
            9,
            2
          ]
        }
      ],
      "central_multiplicities": [
        1,
        3,
        5,
        7,
        9,
        2,
        1,
        1,
        1,
        1,
        2,
        1
      ],
      "weights": [
        "1/72",
        "1/36",
        "1/24",
        "1/18",
        "5/72",
        "1/12",
        "7/72",
        "1/9",
        "1/8",
        "5/36",
        "11/72"
      ],
      "actual_divisor_coefficients": [
        "-11/12",
        "-395/216",
        "-1477/540",
        "-509/140",
        "-5071/5670",
        "-36349/45360",
        "-64699/45360",
        "-88639/45360",
        "-107539/45360",
        "-57077/11340",
        "-117619/45360"
      ],
      "actual_component_degrees": [
        "1/12",
        "1/216",
        "1/180",
        "1/168",
        "1/162",
        "5/144",
        "1/12",
        "7/72",
        "1/9",
        "1/8",
        "5/72",
        "11/72"
      ],
      "mass": "1",
      "energy": "-5058227/6531840",
      "entropy": "117619/45360",
      "endpoint_raw_mass": "1/12",
      "all_degrees_strictly_positive": true,
      "adjacent_determinants_one": true,
      "actual_monomial_min_orders_verified": true,
      "intersection_energy_equals_roof_area": true
    },
    {
      "target_slopes": [
        "13/17",
        "17/13"
      ],
      "rays": [
        [
          0,
          1
        ],
        [
          1,
          2
        ],
        [
          2,
          3
        ],
        [
          3,
          4
        ],
        [
          13,
          17
        ],
        [
          10,
          13
        ],
        [
          7,
          9
        ],
        [
          4,
          5
        ],
        [
          1,
          1
        ],
        [
          5,
          4
        ],
        [
          9,
          7
        ],
        [
          13,
          10
        ],
        [
          17,
          13
        ],
        [
          4,
          3
        ],
        [
          3,
          2
        ],
        [
          2,
          1
        ],
        [
          1,
          0
        ]
      ],
      "ordinary_blowups": [
        {
          "left": [
            0,
            1
          ],
          "right": [
            1,
            0
          ],
          "inserted": [
            1,
            1
          ]
        },
        {
          "left": [
            0,
            1
          ],
          "right": [
            1,
            1
          ],
          "inserted": [
            1,
            2
          ]
        },
        {
          "left": [
            1,
            2
          ],
          "right": [
            1,
            1
          ],
          "inserted": [
            2,
            3
          ]
        },
        {
          "left": [
            2,
            3
          ],
          "right": [
            1,
            1
          ],
          "inserted": [
            3,
            4
          ]
        },
        {
          "left": [
            3,
            4
          ],
          "right": [
            1,
            1
          ],
          "inserted": [
            4,
            5
          ]
        },
        {
          "left": [
            3,
            4
          ],
          "right": [
            4,
            5
          ],
          "inserted": [
            7,
            9
          ]
        },
        {
          "left": [
            3,
            4
          ],
          "right": [
            7,
            9
          ],
          "inserted": [
            10,
            13
          ]
        },
        {
          "left": [
            3,
            4
          ],
          "right": [
            10,
            13
          ],
          "inserted": [
            13,
            17
          ]
        },
        {
          "left": [
            1,
            1
          ],
          "right": [
            1,
            0
          ],
          "inserted": [
            2,
            1
          ]
        },
        {
          "left": [
            1,
            1
          ],
          "right": [
            2,
            1
          ],
          "inserted": [
            3,
            2
          ]
        },
        {
          "left": [
            1,
            1
          ],
          "right": [
            3,
            2
          ],
          "inserted": [
            4,
            3
          ]
        },
        {
          "left": [
            1,
            1
          ],
          "right": [
            4,
            3
          ],
          "inserted": [
            5,
            4
          ]
        },
        {
          "left": [
            5,
            4
          ],
          "right": [
            4,
            3
          ],
          "inserted": [
            9,
            7
          ]
        },
        {
          "left": [
            9,
            7
          ],
          "right": [
            4,
            3
          ],
          "inserted": [
            13,
            10
          ]
        },
        {
          "left": [
            13,
            10
          ],
          "right": [
            4,
            3
          ],
          "inserted": [
            17,
            13
          ]
        }
      ],
      "central_multiplicities": [
        1,
        2,
        3,
        4,
        17,
        13,
        9,
        5,
        1,
        4,
        7,
        10,
        13,
        3,
        2,
        1
      ],
      "weights": [
        "31/3840",
        "31/1920",
        "31/1280",
        "31/960",
        "31/768",
        "31/640",
        "217/3840",
        "31/480",
        "93/1280",
        "31/384",
        "341/3840",
        "31/320",
        "403/3840",
        "217/1920",
        "31/256"
      ],
      "actual_divisor_coefficients": [
        "-31/32",
        "-14849/7680",
        "-6665/2304",
        "-577127/46080",
        "-7543571/783360",
        "-7617351/1131520",
        "-4332343/1131520",
        "-15518197/16972800",
        "-18395617/4243200",
        "-32834611/4243200",
        "-22038179/1980160",
        "-22104581/1523200",
        "-66830203/19801600",
        "-103722187/44553600",
        "-218234699/178214400"
      ],
      "actual_component_degrees": [
        "1/32",
        "31/7680",
        "31/5760",
        "31/5120",
        "31/16320",
        "31/9984",
        "31/5760",
        "217/19200",
        "31/480",
        "93/5120",
        "31/2688",
        "341/38400",
        "31/4160",
        "403/11520",
        "217/3840",
        "31/256"
      ],
      "mass": "1",
      "energy": "-97465003439/195526656000",
      "entropy": "218234699/178214400",
      "endpoint_raw_mass": "1/32",
      "all_degrees_strictly_positive": true,
      "adjacent_determinants_one": true,
      "actual_monomial_min_orders_verified": true,
      "intersection_energy_equals_roof_area": true
    }
  ]
}
