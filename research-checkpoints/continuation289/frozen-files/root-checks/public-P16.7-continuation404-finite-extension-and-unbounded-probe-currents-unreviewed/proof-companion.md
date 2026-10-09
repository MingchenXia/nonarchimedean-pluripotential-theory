# Complete independent proof companion

This is the complete authored mathematical body, including old-chain reconstruction, new finite-extension and unbounded-probe proofs, and the scoped residual. The TeX below is preserved exactly from proof-companion.tex. External-source readings and deeper conventional dependencies are in the separate exact ledger. No old note is a correctness grant.

```latex
\section{Scope, carrier, and external foundations}
This is an independent scoped proof draft for the unchanged original P16.7.
No supplied verdict, note, program, or compilation is a correctness premise.
We retain only
\[
 K=\mathbf C((s)),\quad |s|=e^{-1/8},\quad t=s^8,\qquad
 Y=(\mathbf G_{m,K}^{2})^{\mathrm{an}},\quad
 X=Y/\Lambda,\quad \Lambda=\langle(t,2),(3,t)\rangle.
\]
Put $x_i=-\log|z_i|$, $\rho=\frac12(x_1^2+x_2^2)$ and
$\theta=d'd''\rho$. Periods change $\rho$ by affine functions, so $\theta$
is global. Products and integration below use the CLD orientation and raw mass,
never probability normalization. The mass is $\int_X\theta^2=2$.
The factor two is the real two-dimensional Hessian-to-wedge factor, with
saturated coordinate lattice of multiplicity one. The tropical fundamental
rectangle is $[0,1]^2$ and its Gauss section has multiplicity one.

Here are the conventional foundations used, with their actual application scopes.
CLD v2, 8.1.7--8.1.8, defines the minimal sheaf of continuous psh functions
containing smooth psh functions and closed under local uniform limits.
CLD 8.5.1 permits multiplication of order-zero currents by continuous functions
and gives continuity for continuous coefficients against convergent positive
currents. CLD 8.5.3 gives multiplication of smooth closed forms with closed
currents; 8.5.5 gives positivity of the continuous psh Hessian construction;
8.5.6 is its projection formula. CLD 8.7.1, 8.7.2, 8.7.4, 8.7.5 give,
respectively, the generated continuous products, symmetry/closedness,
continuity under local uniform convergence, and projection. CLD 8.8.1,
8.8.4--8.8.5 give the corresponding difference-of-psh calculus.
The compact-Hausdorff Riesz representation theorem is also used in its precise
ordinary form: a positive linear functional on $C(X,\mathbf R)$ of finite
value on 1 is integration against a unique finite Radon measure. Its hypotheses
are checked by common mass two and uniform density below. The elementary
distribution fact that a continuous function with zero second distributional
derivative is affine is used on real intervals. These conventional functional
foundations are named accurately, not claimed freshly wholly source-audited.
These CLD theorems concern continuous functions in the named generated sheaf,
not an unspecified locally bounded or finite-energy class.
CLD 7.2.8 identifies top positive currents with Radon measures; 7.2.9 says
positive functionals on compact smooth forms are order-zero currents;
7.2.11 supplies their coefficient measure interpretation.
Smooth cutoffs and partitions are CLD 6.2, and boundaryless compact Stokes
is CLD 5.11.1. We do not use the incorrect arbitrary-multiplier closedness
in the displayed argument of 8.6.7.

CLD 16.7.3 is Poincare--Lelong for a meromorphic function on a good analytic
space: $d'd''[\log|F|]=\delta_{\operatorname{div}(F)}$, with divisor
multiplicities. We use it on smooth torus charts and reduced principal curves.
CLD 7.7.8 says proper pushforward commutes with the differentials.
CLD 14.4.3 says that calibration over $K$ of a space over a finite field $L$
is $[L:K]$ times its calibration over $L$.
CLD 15.3.1, with 16.1.1, gives normalized pushforward of the fundamental
current under scalar extension: $\pi_*\delta_{Z_L}=\delta_Z$ when the two
sides are integrated over their respective ground fields. Thus it is
$[L:K]\delta_Z$ when the source is viewed over $K$ instead.
We use finite extensions only, so $\pi$ is proper.
The Gauss section, norm and torus integration used below are CLD 12.1 and
15.7.1, with coordinate lattice degree one on $\mathbf G_m$.

Analytic geometry foundations are: Tate acyclicity and coherent gluing on an
admissible cover (Van der Put 2.14--2.16, whose proof invokes Kiehl);
the rational-domain presentation
$A\langle r_i^{-1}T_i\rangle/(g_0T_i-g_i)$ (Van der Put 2.1--2.2);
the strict Tate Nullstellensatz, in particular that maximal residues of a strict
$K$-affinoid algebra are finite extensions of $K$; and unique extension of
a complete absolute value to a finite field extension.
Conrad--Temkin 4.2.3--4.2.4 gives flat quasi-finite descent of closed analytic
subspaces and separatedness. Ducros 2.1.3--2.1.4 gives the no-boundary
regularity used on torus charts. Gruson IV.5 Theorem 1 says $SK_0=0$ for
products of closed rational-radius discs and unit circles over a discretely
valued field; its determinant consequence trivializes line bundles there.
Regular local rings are UFDs (Stacks 0AG0); flat localizations preserve the
local denominator/pole construction. Stacks 0ENA, 0END, 0EN6, 0BB1 and 086U
are used for function fields, reducedness/integrality, and analytification.
Their applications below concern a smooth integral proper algebraic space,
not a possibly reducible scheme.
Deeper Tate/Weierstrass, Kiehl, Gruson's cited algebraic inputs, regular-local
commutative algebra, semistable reduction and Thuillier potential theory are
named conventional foundations, not newly proved or recursively wholly audited.
The separate reading ledger records which exact immediate source proofs were
actually read. Whole books have not been read or used as grants.

\subsection{Geometry and nonalgebraizability}
Tropical translations of $\Lambda$ are exactly $\mathbf Z^2$. Rectangles of
widths less than one give ordinary open injective quotient charts. On bounded
tropical boxes only finitely many deck graphs meet, and each graph is closed.
A finite collection of injective charts covers the compact image of
$x^{-1}([0,1]^2)$. The associated finite atlas map and its product are flat
quasi-finite maps with finite fibres; descent of the closed deck relation
therefore gives a closed diagonal. This does not apply quasi-finite descent
to the infinite-sheeted map $Y\to X$. Thus $X$ is compact Hausdorff,
separated, good, strict, smooth, boundaryless, connected and pure of dimension
two, hence proper. Strict affinoid neighborhoods use rational radii; taking
roots of defining inequalities realizes rational bounds although $|K^*|$
is discrete.

For completeness we reconstruct the obstruction to algebraization.
Let $P_m=\{|s|^m\le |z_i|\le |s|^{-m}\}$.
The unit circle in either coordinate and the adjacent filled disc have trivial
Picard group by Gruson's determinant consequence. Induct on the number of annulus factors in a mixed product of discs,
circles and annuli. To remove one annulus factor, cover the filled disc by
that annulus and its inner disc; their intersection is the inner circle
(rescaled to a unit circle). The intersection and the filled product have
one fewer annulus factors, so their line bundles are trivial by induction.
Glue the given bundle on the annulus product to the trivial bundle on the
inner-disc product, using a frame on the intersection. Tate/Kiehl coherent
gluing produces a bundle on the filled product, whose trivial frame restricts
to the original bundle. The zero-annulus case is Gruson. Thus
$\operatorname{Pic}(P_m)=0$.
A unit $b$ on $P_m$ has affine Gauss log norm: both that norm and its negative
are convex. Consequently its dominant Laurent exponent is constant and
\[
 b=b_\alpha z^\alpha(1+g),\qquad
 \|g\|_{P_j}\le |s|^{m-j}\quad(j<m).
\]
This follows by comparing every other coefficient with the dominant coefficient
at all extreme radii of $P_m$; at $P_j$ every different exponent gains at
least $|s|^{m-j}$. Adjusting frames successively on the exhaustion $P_m$,
removing scalar monomials and multiplying the resulting $1+g$ factors, gives
convergent transition products on every $P_j$. Hence
$\operatorname{Pic}(Y)=0$. The same estimate makes every global unit on $Y$
a scalar monomial.

A line bundle pulled back from $X$ has deck factors $c_1z^{h_1},c_2z^{h_2}$.
Write $h_1=(A,B)$ and $h_2=(C,D)$. Commutation gives
$t^C2^D=3^At^B$, whence $C=B$ by valuation and $A=D=0$ by multiplicative
independence of 2 and 3. Thus $h_1=(0,k),h_2=(k,0)$.
If $k\ne0$, take $\lambda=\lambda_1\lambda_2^{\operatorname{sgn}k}$ and
$h=(k\operatorname{sgn}k,k)$. Then $v(\lambda^h)=2|k|>0$.
An equivariant Laurent series satisfies
\[
 a_{m+jh}=a_m c^j\lambda^{-jm-hj(j+1)/2}.
\]
For $a_m\ne0$ its coefficient valuations go to minus infinity quadratically,
contradicting convergence on every compact polyannulus. There is no nonzero
section. If $k=0$, the two equivariance equations permit at most one exponent;
a nonzero section is a nowhere-zero monomial and all sections are proportional.
For a meromorphic function on $X$, its pole ideal is locally invertible by
regular local factoriality. Its pullback line bundle on $Y$ is trivial; the
numerator and the pole frame become equivariant sections of the same bundle.
The preceding alternatives force their ratio to be constant. Therefore
$\Gamma(X,\mathcal M_X)=K$. If $X$ were the analytification of a proper
algebraic space, smoothness and connectedness would give an integral smooth
algebraic space of dimension two. Its function field, of transcendence degree
two over $K$, embeds in $\Gamma(X,\mathcal M_X)$, a contradiction.
This is a genuine nonalgebraizable carrier with positive raw mass two.

\section{All-stage bounded calculus}
Let $\C$ consist of actual continuous real functions $a$ on $X$ such that
$\rho+a$ belongs locally to the entire minimal continuous CLD psh sheaf.
Set $T_a=\theta+d'd''[a]$. The source products give
\[
 B(a,b)=\theta\wedge T_b+d'd''(aT_b),\qquad
 \MA(a)=B(a,a).
\]
They are positive Radon measures, symmetric, closed, local, and of mass two.
Convex combinations and maxima stay in $\C$: prove these operations for
smooth psh functions by convex smoothing, then use local uniform closure
and minimality separately in the two slots. This proves them at every stage,
not just at the first approximable stage.

\subsection{Green pairing without an unjustified regularization theorem}
For a fixed positive closed $(1,1)$ current $T$, complete compact smooth
$(1,0)$ forms for the pairing $\int\alpha\wedge J\beta\wedge T$ after
quotienting its null space. Smooth compactly supported functions have
$Q_T(f,g)=\int d'f\wedge d''g\wedge T$. Local continuous psh functions
have strong gradients in this Hilbert space, as follows.
Take cutoffs $0\le\chi\le\eta\le1$, with $\eta=1$ near
$\operatorname{supp}\chi$, and a uniform-convergent smooth psh sequence
$f_j$ on a neighborhood of $\operatorname{supp}\eta$.
For $L_T f=d'd''(fT)$, Stokes gives
\[
 Q_{\chi T}(f_j-f_k,f_j-f_k)
 =\tfrac12\int(f_j-f_k)^2d'd''\chi\wedge T
       -\int\chi(f_j-f_k)L_T(f_j-f_k).
\]
If $\|f_j\|\le B$ there and $\epsilon=\|f_j-f_k\|$, positivity and
$\int\eta L_Tf_j=\int f_jd'd''\eta\wedge T$ bound the right side by
\[
 \tfrac12\epsilon^2\|d'd''\chi\wedge T\|_{\rm TV}
 +2B\epsilon\|\chi\|_\infty\|d'd''\eta\wedge T\|_{\rm TV}.
\]
The gradients are Cauchy. Their limit is unique: against compact smooth
one-forms integration by parts identifies it with the distributional derivative
of the uniform limit. This same estimate works for already constructed strong
gradients. Retain these cutoff and Green identities as part of the constructed class.
They survive its uniform closure: positive $L_Tf_j$ have uniformly bounded
mass on a smaller cutoff, so multiplication by a uniformly converging
continuous coefficient passes to the limit; strong gradients pass the Hilbert
pairings to the limit. Diagonal smooth approximants supply the strong-gradient
definition for that limit. The resulting class of continuous functions with
these identities, strong gradients and positive $L_T$ is a sheaf containing
smooth psh functions and closed under local uniform limits. Minimality puts the entire generated psh sheaf in this class.
Partitions of unity and the bounded multiplier product rule glue the gradients;
a difference of continuous psh functions has the difference gradient.
On compact boundaryless $X$ this gives
\[
 Q_T(f,g)=-\int f\,d'd''(gT)=Q_T(g,f),\qquad
 |Q_T(f,g)|^2\le Q_T(f,f)Q_T(g,g).
\]
Here $f,g$ are continuous dpsh functions, or a smooth test function in one
slot. This argument supplies the Green identities needed below without
assuming a single smooth approximation for every generated function.

Define the cubic energy
\[
 E(a)=\tfrac13\int a\,[\MA(0)+B(a,0)+\MA(a)].
\]
Green, product symmetry and Stokes give $E(0)=0$, $E(a+c)=E(a)+2c$,
\[
 \frac d{dq}E((1-q)a+qb)=\int(b-a)\MA((1-q)a+qb),
\quad
 \frac {d^2}{dq^2}E((1-q)a+qb)
 =-2Q_{T_{(1-q)a+qb}}(b-a,b-a).
\]
Thus $E$ is increasing and concave, and
\[
 E(a)-E(b)=\tfrac13\int(a-b)[\MA(a)+B(a,b)+\MA(b)].             \tag{1}
\]
Locality of products and $\max(a,b-\epsilon)$, whose mass is two, give
bounded comparison on strict inequality sets by letting $\epsilon\downarrow0$.
Equality contacts are not silently assigned either local measure.
\section{Canonical generated energy and actual operators}
Let $\G$ be the set of actual pointwise limits $u=\inf_j u_j$ of decreasing
sequences $u_j\in\C$ with $\inf_jE(u_j)>-\infty$.
These are USC functions, allowed to have poles. No equivalence of functions
modulo measure-zero sets is built into the definition.
If a USC sequence $g_j\downarrow g$ satisfies $g<a$ everywhere for a continuous
$a$ on compact $X$, the increasing open sets $\{g_j<a\}$ cover $X$, hence
some $g_j<a$ globally. Call this strict compact dominance.
For two continuous decreasing presentations of the same $u$, apply it to
$u<a_j+\epsilon$ in both directions. Monotonicity of bounded energy and
$E(a+\epsilon)=E(a)+2\epsilon$ imply that their energy limits agree.
The same proof establishes order monotonicity for generated energy
$E(u)=\lim E(u_j)$. The identically minus-infinity limit is impossible:
strict dominance by each negative constant would force energies to minus
infinity. Convex combinations and finite maxima have continuous decreasing
presentations and finite lower energy bounds by concavity and monotonicity.

On every finite simplex of convex combinations of specified presentations,
$E$ is a polynomial of degree at most three. Evaluating at a finite unisolvent
set of simplex points shows that convergence of energies implies convergence
of every coefficient. The limiting polynomial is intrinsic, because each
point is itself a generated potential and has its canonical energy.
This is a finite-dimensional interpolation argument, not interchange of an
unbounded derivative and a pointwise limit.
For $v\in\C$, set
\[
 P_j(q)=E((1-q)u_j+qv),\qquad R_j(q)=E(qu_j).
\]
Bounded first variation yields
$\int v\MA(u_j)=P_j'(0)+R_j'(1)$; thus these moments converge canonically.

The linear span $\mathcal D$ of $\C$ is uniformly dense in $C(X)$.
Different tropical classes are separated by small smooth periodic perturbations
of $\rho$. Distinct seminorms in the same tropical fibre differ on a Laurent
polynomial $A$. On an injective box $|x_i-a_i|<r<1/2$, put
$\rho_a=|x-a|^2/2$, choose $\delta<r^2/4$, and choose $\epsilon>0$
small enough to glue by zero
\[
 \max\{\rho_a,\delta+\epsilon(\log|A|-b)\}-\rho_a.              \tag{2}
\]
Here $b$ can be chosen so the two specified values are separated. The function
is continuous even at $A=0$, since there it equals zero on a neighborhood;
convex smoothing on $A\ne0$ proves its generated positivity.
The span is a vector lattice. With common positive scale $c$,
\[
 \max\{c(p-q),c(r-s)\}
 =2c\max\{(p+s)/2,(r+q)/2\}-c(q+s).
\]
Here is that lattice density argument explicitly. For any continuous target
$F$ and $\epsilon>0$, point separation and constants give, for each pair
$p,q$, an element agreeing with $F$ at both points. For fixed $p$, finitely
many neighborhoods of $q$ cover $X$ where their elements exceed
$F-\epsilon$. Their maximum exceeds $F-\epsilon$ everywhere and equals
$F(p)$ at $p$, hence is below $F+\epsilon$ near $p$. Finitely many such
neighborhoods of $p$ cover $X$; the minimum of the corresponding maxima
is within $\epsilon$ of $F$ everywhere and belongs to the lattice. Common positive mass two extends the moment convergence
from $\mathcal D$ to all continuous tests. Riesz representation gives an
actual positive Radon measure $\MA(u)$ of mass two, for EVERY continuous
decreasing presentation of $u$. Polarization, equivalently coefficients of
$\MA((u+v)/2)$, gives the positive canonical mixed measure $B(u,v)$.

For a positive Radon measure $\mu$ of mass two define its FULL bounded dual by
\[
 E^*(\mu)=\sup_{a\in\C}\{E(a)-\int a\,d\mu\}.               \tag{3}
\]
No support restriction appears in (3). If $u\le0$ is generated, then
\[
 \int(-u)\,d\mu\le E^*(\mu)-E(u).                          \tag{4}
\]
Indeed apply (3) to $u_j$, then monotone convergence. Constants also show why
mass two is required. Formula (4) proves presentation convergence in
$L^1(\mu)$ and gives $\mu$-null poles whenever the dual is finite.
Bounded tangency gives
$E^*(\MA(a))=E(a)-\int a\MA(a)$ for $a\in\C$.

There is no circular appeal to unbounded self-integrability.
The coefficient $D_u=\lim_j\int u_j\MA(u_j)=\lim R_j'(1)$ is finite.
Taking coefficient limits in bounded tangency gives
$E^*(\MA(u))\le E(u)-D_u<\infty$. Only now may (4) be used for this measure.
For $k\ge j$, (1) gives
\[
 0\le\int(u_j-u_k)\MA(u_k)\le3(E(u_j)-E(u_k)).               \tag{5}
\]
First let $k\to\infty$, using the continuous test $u_j$, coefficient convergence
for the self term, and its newly proved integrability; then let $j\to\infty$.
It follows that
\[
 D_u=\int u\MA(u),\qquad
 E^*(\MA(u))=E(u)-\int u\MA(u).
\]
For $u\le0$, $E(u)\ge-C$, its cubic coefficients give
$\int u\MA(u)\ge3E(u)$ and therefore $E^*(\MA(u))\le2C$.

For clarity, the moving-moment argument has three distinct parts.
For bounded $w$ and generated $u$, the coefficient of $q$ in
$E(pu+qw)$ at $(p,q)=(1,0)$ is $\int w\MA(u)$ by the preceding bounded-test
construction. Next let a continuous decreasing presentation $w_l\downarrow w$
be generated. Energy at every simplex point converges to energy of the
actual convex combination; interpolation gives coefficient convergence.
Finite dual of $\MA(u)$ gives $\int w_l\MA(u)\to\int w\MA(u)$.
Finally make the same interpolation for simultaneous decreasing generated
families $u_j\downarrow u$, $v_j\downarrow v$ whose energies converge.
It yields
\[
 \MA(v_j)\rightharpoonup\MA(v),\quad
 \int u_j\MA(v_j)\to\int u\MA(v),\quad
 \int u\MA(v_j)\to\int u\MA(v).                            \tag{6}
\]
The last assertion uses the fixed-$u$ coefficient argument, not weak convergence
against an unbounded test. Subtracting the last two assertions proves
$\int|u_j-u|\MA(v_j)\to0$. Mixed assertions follow by polarization and
$B(a,b)\le2\MA((a+b)/2)$. For continuous decreasing presentations, energy
convergence is already canonical; for decreasing generated families it will
follow from the countable closure theorem below.

\subsection{Comparison, locality and clamps on actual Borel sets}
The bounded product identities pass to generated strict sets without asserting
that these sets are open. For bounded Lipschitz tests of $u_j-v_j$, first
replace the moving difference by $u-v$ using (6); replace that difference by
fixed continuous approximants $u_l-v_l$ using the fixed-slot moment convergence;
then use weak convergence at fixed $l$ and let $l\to\infty$.
Lipschitz ramps converge to strict-set indicators at levels carrying no mass.
Only countably many levels are bad for the finitely many measures involved,
so approach zero through good levels. This proves
\[
 \MA(v)\{u<v\}\le\MA(u)\{u<v\},\qquad
 \mathbf1_{\{u>v\}}\MA(\max(u,v))
   =\mathbf1_{\{u>v\}}\MA(u).                              \tag{7}
\]
The same argument and polarization give mixed maximum locality.
Borel restrictions of a finite Radon measure on compact Hausdorff $X$ are
Radon; continuous-test equality therefore identifies the restrictions.
For $u\le0$, put $u^A=\max(u,-A)$. This is generated, even if discontinuous.
Then $\mathbf1_{\{u>-A\}}\MA(u^A)=\mathbf1_{\{u>-A\}}\MA(u)$.
If $E(u)\ge-C$, (4) and $E^*(\MA(u^A))\le2C$ give discarded mass
at most $3C/A$. The entire contact set $u=-A$ is excluded.
Mixed clamp restrictions have discarded mass at most
$2(2C_u+C_v)/A+2(C_u+2C_v)/B$ on the complement of
$\{u>-A,v>-B\}$. These are actual generated products; they do not identify
bounded discontinuous clamps with the preexisting continuous CLD operator.

\section{Constrained countable decreasing closure}
\begin{theorem}
If $u_k\in\G$ decreases pointwise and $L=\inf_kE(u_k)>-\infty$, its actual
pointwise infimum $u$ belongs to $\G$, and $E(u_k)\downarrow E(u)$.
It has a single continuous decreasing presentation, also at its poles.
\end{theorem}
\begin{proof}
Choose presentations $f_{k,j}\in\C$ with $f_{k,j}\downarrow u_k$.
Enumerate ALL inner terms as $h_1,h_2,\ldots$; their pointwise infimum is $u$.
Let $\epsilon_n=2^{-n}$ and $r_n=\sum_{\ell>n}\epsilon_\ell=2^{-n}$.
Choose $k_n\ge\max(n,k_{n-1})$ such that
$u_{k_n}<h_m+\epsilon_n$ globally for every $m\le n$.
Each bound follows from strict compact dominance for the decreasing USC outer
sequence, because $u\le h_m<h_m+\epsilon_n$. Taking finitely many bounds
is legitimate. Choose an inner term $v_n=f_{k_n,j_n}$ satisfying these bounds
and, for $n>1$, $v_n<v_{n-1}+\epsilon_n$ globally. Indeed
$u_{k_n}\le u_{k_{n-1}}\le v_{n-1}$, so strict compact dominance applies
to this additional continuous upper bound as well.
Then $a_n=v_n+r_n\in\C$ is decreasing, since
$\epsilon_n+r_n=r_{n-1}$. It dominates $u$ and, for fixed $m$, is eventually
below $h_m+\epsilon_n+r_n$. Consequently $\inf_na_n=\inf_mh_m=u$,
including where that infimum is minus infinity. Monotonicity gives
$E(a_n)\ge E(u_{k_n})\ge L$, so $u\in\G$.
For any continuous presentation $b_j\downarrow u$ and any $\epsilon>0$,
strict compact dominance gives $u_k<b_j+\epsilon$ globally for late $k$.
Hence $\lim_kE(u_k)\le E(b_j)+2\epsilon$; let $j\to\infty$ and
$\epsilon\downarrow0$. The reverse inequality is order monotonicity.
\end{proof}
This is not a net, cofinality, or energy-sublevel compactness theorem.
It now justifies (6) for every energy-bounded decreasing generated family.
A countable directed family has a decreasing cofinal choice, with the same
pointwise infimum. If $u_i\le0$, $\sum_i\lambda_i\le1$, and
$\sum_i\lambda_i|E(u_i)|<\infty$, the finite sums (with the remaining
coefficient assigned to zero) decrease and have energies bounded below by
concavity. The theorem gives their actual generated sum and energy continuity.
No convergence of a nonordered variational family is deduced.
\section{All-test control and bounded pointwise uniqueness}
For $a,b,w\in\C$ set $f=a-b$, $g=(a+b)/2$, $h=w-g$ and
\[
 I(a,b)=\int(a-b)[\MA(b)-\MA(a)].
\]
The actual bounded Green calculus gives
\[
 I=Q_{T_a}(f,f)+Q_{T_b}(f,f)\ge0,
\qquad
 Q_{T_w}(f,f)-Q_{T_g}(f,f)
   =Q_{T_a}(f,h)-Q_{T_b}(f,h).                              \tag{8}
\]
The second identity is the symmetric transgression
$-\int f\,d'd''f\wedge d'd''h$, not pullback of a current.
Cauchy--Schwarz gives
\[
 Q_{T_w}(f,f)\le I/2+
 \sqrt{I\,[Q_{T_a}(h,h)+Q_{T_b}(h,h)]}.                     \tag{9}
\]
Shift $a,b,w$ separately to be nonpositive and choose a common $C$ with
$E(a),E(b),E(w)\ge-C$. Constants do not affect (8).
By (4), $\int(-p)\MA(q)\le3C$ for these functions, and mixed moments are
at most $6C$. Since $|h|\le-w+(-a-b)/2$, its absolute MA moments are
at most $6C$ and its mixed moments at most $12C$.
Expanding $Q_{T_a}(h,h)=-\int h\,d'd''h\wedge T_a$ bounds it by
$12C+3C+6C=21C$; the same holds for $b$. Thus
\[
 Q_{T_w}(a-b,a-b)\le I(a,b)/2+\sqrt{42C I(a,b)}.             \tag{10}
\]
For $u,v\in\G$ with equal actual MA measures, take continuous presentations
$u_j,v_j$. Moving and fixed moments (6) give $I(u_j,v_j)\to0$, hence
$Q_{T_w}(u_j-v_j,u_j-v_j)\to0$ for EVERY fixed $w\in\C$.
Degeneracy of $\theta$ on residue bidiscs prevents replacing this by a
constancy assertion from $Q_\theta$ alone.

\subsection{Divisor identity for a bounded continuous defect}
If $a,b\in\C$ have equal MA, (10) and Green against any compact smooth
scalar test give $d'd''((a-b)T_w)=0$ for every $w\in\C$.
Write $d=a-b$. On a smaller injective torus box and for a Laurent polynomial
$A$, let $\psi_N=\chi(\log|A|+N)$, where $\chi$ is smooth convex
nondecreasing, zero on $(-\infty,0]$, and $\chi(q)=q-c$ for $q\ge1$.
It is globally smooth, including at zeros of $A$.
Choose a convex-cap weight
\[
 w_N=\max\{\rho_a,\delta+\epsilon_N\psi_N\}-\rho_a
\]
which vanishes on a tropical boundary collar. In the inner box
$\rho_a<\delta/2$ it has $T_{w_N}=\epsilon_Nd'd''\psi_N$.
Therefore $d'd''(d\,d'd''\psi_N)=0$ there.
On the support of a compact smooth top-degree test, zeros of $A$ are absent
from its full-dimensional support. Its compact support has $|A|$ bounded
away from zero, so $\psi_N-N$ eventually equals $\log|A|-c$ there.
Poincare--Lelong gives positive-current convergence
$d'd''\psi_N\to\delta_{\operatorname{div}A}$ locally.
CLD 8.5.1 permits the continuous multiplier $d$ in this limit; consequently
\[
 d'd''(d\,\delta_{\operatorname{div}A})=0.                  \tag{11}
\]
This uses continuity and boundedness of $d$ in an essential way.

For a local principal holomorphic function $F$, work on a strict rational
domain $V$ in a compact polyannulus. Present
$\mathcal O(V)=A\langle r_i^{-1}T_i\rangle/(g_0T_i-g_i)$;
$g_0$ is a unit on $V$ with positive minimum norm.
Truncate a representative Tate series and approximate its finitely many
coefficients and $g_i$ by Laurent polynomials. Approximate $g_0$ by $q$
with error below its minimum norm. Substituting $T_i=g_i/g_0$ and choosing
errors small enough for the finite truncated expression yields
$F_n=A_n/Q_n\to F$ uniformly on $V$, with Laurent numerators and unit
Laurent denominators. The denominators stay controlled; none acquires a
zero on $V$. On each compact full-dimensional smooth test support avoiding
$F=0$, the equality $|F_n|=|F|$ is eventually exact. Hence their log currents
converge there. Poincare--Lelong identifies the positive divisor currents;
unit denominators contribute no divisor. Apply (11) and the continuous
multiplier theorem to conclude (11) for EVERY local principal holomorphic
divisor. This does not prove integrability of an unbounded defect on divisors.

\subsection{Coordinate curves, finite Galois averaging, and Gauss rays}
We give the full bounded uniqueness route, needing only coordinate curves.
Let $P\in K[z_1]$ be irreducible with nonzero constant term and
$L=K[z_1]/(P)$. Characteristic zero makes $P$ separable. The principal
curve $C_P=\{P(z_1)=0\}\subset Y$ is reduced smooth, is $\mathbf G_{m,L}$
viewed over $K$, and its closed immersion $j$ is proper with divisor
multiplicity one. Pullback of a continuous generated psh function belongs to
the corresponding curve sheaf: this holds for smooth generators, is local,
and survives uniform limits, so minimality applies at every stage.
Thus $d|_{C_P}$ is continuous dpsh and its Laplacian is a signed Radon
measure. Projection and push-differentiation turn (11) into
\[
 j_*d'd''[d|_{C_P}]=0.
\]
A closed embedding has injective pushforward on scalar signed Radon measures:
a measure is determined on its closed image, and compact continuous tests
extend locally to the ambient locally compact Hausdorff space.
Its curve Laplacian is therefore zero. Its $K$ calibration is $[L:K]$
times its $L$ calibration, so it is also zero over $L$.

Here is the field-change step independently of any pullback of currents.
For a finite Galois extension $E/L$, let $\pi:\mathbf G_{m,E}^{\rm an}
\to\mathbf G_{m,L}^{\rm an}$. Pull back the continuous dpsh function $h$,
and form its Laplacian upstairs. This is a signed Radon measure $\nu$,
not a formal pullback of the downstairs current. It is Galois invariant by
naturality of function pullback and differentiation. Projection and normalized
fundamental pushforward give $\pi_*\nu=d'd''[h]=0$.
For any analytic point $x$, $\mathcal H(x)\otimes_LE$ is a finite etale
algebra, a product of complete fields. The Galois group acts transitively
on the factors, since its invariants are $\mathcal H(x)$ and a proper union
of orbits would give a nontrivial invariant idempotent. Unique extension of
the complete valuation gives exactly one point per factor. Thus every fibre
is a single Galois orbit. The finite proper map is the topological quotient.
Average a compact continuous test over the finite group; the average descends
to a compact continuous test downstairs. Invariance of $\nu$ and
$\pi_*\nu=0$ imply every test integral is zero. Hence $\nu=0$.
The push has factor one over varying ground fields; viewing the source over
$L$ instead would have the factor $[E:L]$. No infinite extension is used.

If $h$ is bounded continuous dpsh on $\mathbf G_{m,E}^{\rm an}$ and
$d'd''[h]=0$, set $H_0(q)=h(\eta_{0,e^{-q}})$ on $\mathbf R$.
Torus integration with degree-one lattice gives, for every compact smooth
$\varphi$, $\int H_0(q)\varphi''(q)dq=0$.
A continuous distribution with zero second derivative is affine; boundedness
makes it constant. For $a\in E^*$ use the annulus coordinate $z-a$ on
$0<r<|a|$. The same calibration proves
$H_a(q)=h(\eta_{a,e^{-q}})$ is affine on the corresponding halfline,
and boundedness again makes it constant. As $r\downarrow0$ these points
converge to $a$; as $r\uparrow|a|$ they converge to
$\eta_{a,|a|}=\eta_{0,|a|}$. Continuity identifies $h(a)$ with the same
constant on the central Gauss ray.
Every closed rigid point over $L$ becomes rational over a finite Galois normal
closure of its finite residue extension, so the preceding argument proves
its value equals this constant downstairs. Closed rigid points are dense:
every ordinary open set contains a strict rational neighborhood in a strict
affinoid domain, and a nonempty such algebra has a maximal ideal with finite
residue field by the strict Tate Nullstellensatz. Continuity therefore makes
$h$ constant on the whole curve.

At a rigid point $(a,b)$ of $Y$, the vertical curve given by the minimal
polynomial of $a$ connects its value to the rigid point $(a,1)$.
The horizontal curve $z_2=1$, by the same argument, has constant defect.
All rigid values of $d$ on $Y$ are equal; strict-affinoid density and continuity
make $d$ constant on $Y$ and therefore on $X$.
We have proved bounded CONTINUOUS uniqueness modulo constants on the actual
specified $X$. This corrects the old current400 residual phrase saying that
bounded uniqueness was still open. It proves no bounded-discontinuous or
unbounded generated uniqueness theorem.

\section{Classical recognition and the precise Shilov gate}
The applied GR v2 source is the paragraph in Section 1.2 that smooth CLD psh
functions are classically psh, using Wanner and smooth pullback; it is not a
formal theorem numbered 1.2. Wanner's actual continuous equivalence is
Corollary 4.8, combining Theorems 4.5 and 4.7, on open subsets of a smooth
proper algebraic curve over an algebraically closed complete nontrivially
valued field. GR uses this on the tested curves; it is not directly invoked
for a nonalgebraizable surface. GR 4.2 gives the affinoid maximum principle;
6.1 supplies decreasing closure (with the extended minus-infinity convention);
6.4 supplies upper semicontinuous regularization and its Hartogs upper control,
under its stated boundedness hypotheses. Their immediate proofs were read.
A uniform sequence can be replaced by a decreasing sequence by taking a
subsequence with errors $2^{-j}$ and adding $3\cdot2^{-j}$.
Minimality and decreasing closure consequently give classical recognition of
ALL continuous generated weights and of their actual decreasing limits,
on every curve test and every field extension in that definition.
This is classical recognition, not construction of extended mixed products
from one positive Hessian.

For a USC classically psh local weight $q$ and an actual affinoid neighborhood
basis $A$ at a point $x$, the maximum principle and USC give
\[
 q(x)=\inf_{A\ni x}\max_{\xi\in\Gamma_A}q(\xi).             \tag{12}
\]
One inequality is the maximum principle; for the other shrink $A$ into
$\{q<q(x)+\epsilon\}$. If $q(x)=-\infty$, shrink into $\{q<-N\}$ for
arbitrary $N$. Thus values on ALL the varying Shilov boundaries determine
actual USC weights, including poles. A dense set alone does not do this.
The finite-boundary cover argument, with small oscillation of a continuous
obstacle on each affinoid, gives Hartogs UPPER control. It gives neither
lower tails nor actual representatives of nonordered limiting families.
\section{New progress: finite scalar extension for the generated operator}
\begin{theorem}\label{finite}
Let $F/K$ be finite, $\pi:X_F\to X$, and use the respective-ground-field
CLD calibrations on the two spaces. The same torus quotient and curvature
construction over $F$ has classes $\C_F,\G_F$ and raw mass two.
For $u,v\in\G$,
\[
 u\circ\pi\in\G_F,\quad E_F(u\circ\pi)=E_K(u),\quad
 \pi_*B_F(u\circ\pi,v\circ\pi)=B_K(u,v).                   \tag{13}
\]
In particular (13) holds for MA, for every continuous decreasing presentation,
and for the finite mixed moments of pulled-back generated functions.
If $F/K$ is Galois and $\MA_K(u)=\MA_K(v)$, then
$\MA_F(u\circ\pi)=\MA_F(v\circ\pi)$ as actual measures upstairs.
\end{theorem}
\begin{proof}
The quotient atlas and $\rho$ are defined by the same Laurent formulas over
$F$. The compact fundamental polyannulus and finite-atlas construction
commute with finite scalar extension, giving $X_F=Y_F/\Lambda$ and a proper
finite scalar map. The Green argument, bounded products, density of bounded
caps, polynomial interpolation and countable closure above use these local
torus charts and compactness, so reconstruct the same actual classes and
operators over $F$. They do not require nonalgebraizability over $F$.
Pullback preserves smooth psh generators and local uniform convergence;
minimality proves $\pi^*\C\subset\C_F$ at all stages.

For bounded $a,b$, the proper projection formula for continuous dpsh products
applies to these functions, not to an arbitrary current pullback.
One may view $X_F$ over $K$: its fundamental current pushes to
$[F:K]\delta_X$. Calibration of ALL its integrals of the pulled-back forms
and their generated products over $K$ is $[F:K]$ times calibration over $F$,
by 14.4.3. Divide the same-field projection equality by this nonzero degree.
It gives
$\pi_*B_F(a\pi,b\pi)=B_K(a,b)$ and also the coefficient-weighted equality
for every continuous function pulled back from $X$.
The three terms of the cubic energy therefore give
$E_F(a\pi)=E_K(a)$. This derivation retains the degree in the intermediate
same-field expression rather than confusing it with the varying-field rule.

A continuous decreasing presentation $u_j$ pulls back pointwise to $u\pi$,
with the same energies. Thus it is a presentation in $\G_F$ and its canonical
energy is the same. For every continuous test downstairs, proper pushforward
and weak convergence of the bounded mixed products give (13).
Finiteness and equality of moments follow either from the generated moment
construction or from the pushforward identity and ordinary integration of
the actual Borel functions; poles have zero mixed mass by (4) and polarization.

For Galois $F/K$, the products of pulled-back bounded functions are invariant
under the finite semilinear Galois action. Locally this action preserves the
absolute value, the coordinate moment functions, their calibration and the
smooth calculus. It preserves smooth generators and their uniform closure;
naturality of continuous products then gives invariance. Weak convergence
preserves it for generated MA and mixed measures.
The fibre argument using $\mathcal H(x)\otimes_KF$ given above applies to
ANY analytic point of $X$. Hence fibres are single Galois orbits and $\pi$
is a proper quotient map. If two invariant measures have the same pushforward,
their invariant signed difference integrates a test just as it integrates its
finite Galois average. That average descends to a continuous test downstairs.
Their difference is zero. Applying (13) proves the last assertion.
\end{proof}
No assertion is made that the full dual (3) of an arbitrary measure pulls
back unchanged: $\C_F$ includes tests that need not descend.
No infinite field extension, pullback of arbitrary currents, or general
upstairs equation theory is used.

\section{New progress: domination of probes and an unbounded defect current}
\begin{lemma}\label{dom}
Fix $w\in\C$. For every compactly supported smooth symmetric $(1,1)$ form
$\alpha$ on $X$, the signed coefficient measure
$\mu_{\alpha,w}=\alpha\wedge T_w$ satisfies
\[
 |\mu_{\alpha,w}|\le\sum_{i=1}^m c_i B(p_i,w)
 \le\sum_{i=1}^m2c_i\MA((p_i+w)/2)                         \tag{14}
\]
for finitely many $p_i\in\C$ and finite $c_i>0$.
Every analytic moment used by $\alpha$ is allowed; the lemma is not confined
to the reference tropicalization. The antisymmetric part of a general probe
pairs to zero with the symmetric $T_w$, by the $J$ symmetry of top-degree
integration, so symmetric probes suffice to define the entire coefficient
current.
\end{lemma}
\begin{proof}
Cover the support by finitely many small injective tropical boxes. Within each,
choose an ordinary smaller neighborhood compactly contained in a strict
rational domain of a compact polyannulus, on which a finite list of analytic
units $g_1,\ldots,g_m$ presents the smooth form.
Smooth nonnegative cutoffs subordinate to these neighborhoods decompose
$\alpha$ into finitely many compactly supported pieces $\alpha_i$.
The form has symmetric coefficient matrix in the $d'\log|g_j|,
 d''\log|g_j|$ coordinates; its coefficients are bounded on a compact
neighborhood of the support.

Use the rational-domain approximation already proved, now on each analytic
unit $g_j$. Its minimum norm on that compact domain is positive.
Choose a Laurent rational approximant $A_j/Q_j$ with unit denominator and
uniform error strictly smaller than that minimum. The ultrametric inequality
gives EXACTLY $|g_j|=|A_j/Q_j|$ everywhere on the domain; in particular
$A_j$ is a unit there too. On its interior,
\[
 \log|g_j|=\log|A_j|-\log|Q_j|.
\]
This is equality of smooth moment functions, so it preserves their first
forms and all the coefficient representations of $\alpha_i$.
Let $H_\ell$ be the finite list of all these Laurent numerators and denominators.
Their log norms lie in finite intervals on a compact neighborhood of
$\operatorname{supp}\alpha_i$.
Choose smooth convex nondecreasing scalar functions $\Phi_\ell$ which vanish
below a lower cutoff, have $\Phi_\ell''\ge1$ on those intervals, and are
affine above an upper cutoff. Put
$\Psi=\sum_\ell\Phi_\ell(\log|H_\ell|)$.
It is globally smooth and psh on the injective tropical box: near a zero of
an $H_\ell$ its summand is locally constant zero, and away from zeros the
log norm is smooth pluriharmonic. It is nonnegative and bounded above on
the whole box, because Laurent polynomial norms are uniformly bounded above
on its compact tropical closure. On the chosen compact neighborhood,
\[
 d'd''\Psi\ \ge\ \sum_\ell
 d'\log|H_\ell|\wedge d''\log|H_\ell|.                     \tag{15}
\]
The elementary symmetric-matrix inequality bounds both $\alpha_i$ and
$-\alpha_i$ by a finite multiple of the right side of (15): differences of
two moment gradients cost at most twice the sum of their squares, and the
bounded coefficient matrix costs its finite operator norm. In dimension two,
all the positivity conventions agree for $(1,1)$ forms; no higher-degree
cone interior is being asserted.

Write $\rho_a=|x-a|^2/2$ in this box. Shrink the compact support neighborhood
so $\rho_a<\delta/2$, and choose $\delta$ strictly below the minimum of
$\rho_a$ on a tropical boundary collar. Choose $\epsilon>0$ so small that
$\delta+\epsilon\sup\Psi<\rho_a$ on that collar. Then
\[
 p_i=\max\{\rho_a,\delta+\epsilon\Psi\}-\rho_a,
\]
extended by zero, is in $\C$ and satisfies
$T_{p_i}=\epsilon d'd''\Psi$ near the support. Both
$c_iT_{p_i}+\alpha_i$ and $c_iT_{p_i}-\alpha_i$ are positive there for
large enough finite $c_i$; outside the support they are positive because
$T_{p_i}$ is positive. Near the support $T_{p_i}=\epsilon d'd''\Psi$ is SMOOTH,
so wedging either positive smooth form with the positive $T_w$ preserves
positivity. Away from the support the desired measure is the positive
continuous product $B(p_i,w)$. Locality therefore gives signed-measure inequalities
$-c_iB(p_i,w)\le\alpha_i\wedge T_w\le c_iB(p_i,w)$.
Total variation is bounded by this positive dominating measure. Sum the
pieces and use
$B(p_i,w)\le2\MA((p_i+w)/2)$, which follows by expanding the positive
square. This proves (14).
\end{proof}

\begin{theorem}\label{unbounded}
For EVERY $u\in\G$ and fixed $w\in\C$, the coefficient product $uT_w$
is a well-defined order-zero current obtained by integrating the actual
function $u$ against each coefficient measure. Every continuous decreasing
presentation $u_j\downarrow u$ converges to it in coefficient $L^1$ and
weakly as currents. If $u,v\in\G$ and $\MA(u)=\MA(v)$, then
\[
 d'd''(uT_w-vT_w)=0\qquad\hbox{for EVERY fixed }w\in\C.    \tag{16}
\]
This is an unbounded current identity, not pointwise uniqueness.
\end{theorem}
\begin{proof}
Every MA measure on the right of (14) has finite FULL dual by the proved
bounded tangency, so (4), after shifting $u$ by a constant, proves
$u\in L^1(|\mu_{\alpha,w}|)$ and
$\int|u_j-u|d|\mu_{\alpha,w}|\to0$. Its poles are null for all those
coefficient measures. Define the product separately for each actual function;
there is no subtraction of two infinite point values.
Since $u$ has a finite upper bound $b$, the functional
$\alpha\mapsto\int(b-u)\alpha\wedge T_w$ is finite, linear, and positive
on positive compact smooth $(1,1)$ forms. CLD 7.2.9 makes it order zero.
Subtracting it from $bT_w$ constructs $uT_w$. The coefficient convergence
above proves current convergence of $u_jT_w$ to this product.

Choose continuous decreasing presentations $u_j,v_j$ with uniform lower
energy bounds and put $f_j=u_j-v_j$.
Equations (6) and (10) give $Q_{T_w}(f_j,f_j)\to0$.
For every compact smooth scalar test $\varphi$, Green and Cauchy--Schwarz give
\[
 |\langle d'd''(f_jT_w),\varphi\rangle|
 =|Q_{T_w}(f_j,\varphi)|
 \le Q_{T_w}(f_j,f_j)^{1/2}Q_{T_w}(\varphi,\varphi)^{1/2}
 \longrightarrow0.
\]
The fixed smooth test has finite second factor. Differentiation commutes with
weak current convergence. Passing to the coefficient-current limit proves
(16). This proof covers ALL local smooth moment probes through Lemma
\ref{dom}, not just those depending on $x_1,x_2$.
\end{proof}

\subsection{A precise limit that remains unjustified}
The caps in the bounded divisor proof vary with $N$. The constants $c_i$ in
(14), and the dual energies of their dominating measures, depend on the cap
and need not be bounded in that limit. Thus (16) cannot currently be passed
to $d'd''((u-v)\delta_D)=0$ for a divisor $D$. Neither existence of a divisor
restriction nor uniform integrability for this limit has been proved.
The continuous multiplier theorem 8.5.1 does not apply to $u-v$ at its poles.
This identifies a specific remaining obstacle in the extension of bounded
coordinate-curve uniqueness to the actual unbounded domain.

There is a useful conditional point estimate which does not cross that obstacle.
If a bounded test $w$ has $\MA(w)\{\xi\}=c>0$, then for $u\le0$,
$E(u)\ge-C$, (4) gives
\[
 -u(\xi)\le\frac{E^*(\MA(w))+C}{c}<\infty.                \tag{17}
\]
No real positive atom at EVERY full-dimensional Abhyankar/Shilov point has
been constructed here. Nor does the fact that $c\delta_\xi$ is a component
of one finite-dual measure imply that $2\delta_\xi$ itself has finite full
dual. Formula (17) is consequently a conditional estimate, not a claimed
point-capacity theorem or separated energy compactness.
\section{Scoped audit verdict and unchanged original residual}
The independent reconstruction finds no identified gap in the constrained
current400 countable closure argument or the bounded-continuous
ROOT398--399 uniqueness argument
in the scopes proved above, under the explicitly named conventional foundations.
The new results are finite scalar-extension preservation, invariant upstairs
MA equality, domination of arbitrary compact smooth moment probes, and (16)
for the actual unbounded generated domain. These are mathematical proof drafts,
not consequences of program execution or previous positive verdicts.
A source label is corrected: Wanner's equivalence is Corollary 4.8, and the
GR smooth-recognition input is an unnumbered Section 1.2 paragraph.
The old bounded-uniqueness residual is superseded only for $\C$.

The ORIGINAL target remains: construct the finite-energy operator and its
existence-and-uniqueness theory on genuinely nonalgebraizable analytic spaces,
with an explicit positivity datum and necessary compactness, envelope and
comparison replacements. For the retained carrier and datum here, the original
remaining gates are all still imposed:
\begin{enumerate}
\item An adequate actual analytic finite-energy domain/recognition or completion
for nonordered variational limits. Countable downward closure does not supply it.
\item Separated normalized energy-sublevel compactness in a specified topology,
with lower-tail control and actual generated representatives. Upper/Shilov
control and finite moments alone do not prove it.
\item Actual envelopes and orthogonality, or a proved replacement sufficient
for variational maximization and all required variations.
\item Existence for EVERY positive Radon raw-mass-two measure with finite FULL
bounded dual (3), with arbitrary support, or a different explicit noncircular
sufficient energy class justified against the literal completion criteria.
Eligibility cannot be restricted to measures already equal to $\MA(u)$.
\item Full actual pointwise uniqueness modulo constants throughout the adequate
unbounded finite-energy domain. Identity (16) does not prove it, and does not
justify a divisor restriction or capacity removal at every Shilov boundary.
\end{enumerate}
No single-skeleton, radial, finitely atomic, inverse Banach, zero-mass, or
abstract functional-representative substitute has been introduced.
No full original P16.7 solution or analytic counterexample is claimed.
No P16.1--P16.6 target is claimed solved. The candidate flag is false.

\section{Execution and identity evidence}
Only newly authored ordinary data-processing scripts were executed.
The 27 current mathematical bindings have zero byte/hash mismatches.
For each of the five actual FINAL notes, all five fields (id, summary,
detailedSummary, text, support) agree with the expanded JSON; the corresponding
text occurs once in the complete companion. The campaign-result text adds
only its recorded artifact-path tail. Actual FINAL, expanded fields and
campaign-result retention were saved separately without rewriting them.
An independently written character renderer proves exact identity of the
70,066-byte supplied standalone TeX with the supplied main plus complete
companion rendering, preserving mathematical spans and escaping prose/code.
That identity is a finite data check, not an additional independent reading
or mathematical proof. The entire unique mathematical bodies were read in
bounded untruncated chunks; duplicate bodies were identified as duplicates.
Initial overly large emissions were truncated and are not credited as complete
reads. Complete bounded rereads or exact duplicate identities replace them.

The rerun scripts are \texttt{audit\_packet.py}, \texttt{verify\_rendering.py},
\texttt{check\_source\_units.py}, \texttt{read\_data.py},
\texttt{build\_deliverable.py} and
\texttt{check\_deliverable.py}. They use the Python standard library only.
Run \texttt{python audit\_packet.py}, \texttt{python verify\_rendering.py},
\texttt{python check\_source\_units.py},
\texttt{python build\_deliverable.py}, then
\texttt{python check\_deliverable.py} from the artifact directory.
Bounded reading is rerun with
\texttt{python read\_data.py PATH START END}; offsets are characters, not bytes.
All actually used frozen data needed by these checks are also passively
snapshotted under \texttt{LOCALONLY-rerun-inputs}, indexed by original path
and hash in \texttt{LOCALONLY-rerun-input-index.json}. This retains 91 files
and 6,193,657 bytes without importing or executing them. The own
\texttt{local\_inputs.py} resolver prefers these local snapshots.
The environment is Python 3.12.14, Linux 6.18.44 x86\_64, glibc 2.41.
No supplied program was executed/imported; no compilation, publication,
additional model/campaign, agent, runtime/authentication/proxy/CA change, or
active-campaign mathematics inspection was performed.
No resource-heavy compute was needed or launched; no operator-provided
supervised heavy-compute facility was available among callable tools.
Full primary carriers, literal units, pixels, and whole-book contexts remain
LOCALONLY. Their exact bindings and reading receipts are retained locally.

\begin{thebibliography}{99}
\bibitem{CLD} A. Chambert-Loir and A. Ducros, \emph{Formes differentielles reelles
et courants sur les espaces de Berkovich}, v2, 25 July 2025. The applied literal
units and calibrations are fixed in the local primary ledger.
\bibitem{GR} W. Gubler and J. Rabinoff, \emph{Classically psh and pluriharmonic
functions on Berkovich spaces}, v2, 17 September 2025, Sections 1.2, 4, 6, 7.
\bibitem{Wanner} V. Wanner, \emph{Comparison of two notions of subharmonicity on
non-archimedean curves}, arXiv:1801.04713v3; Math. Z. 293 (2019), 443--474.
\bibitem{Gruson} L. Gruson, \emph{Fibres vectoriels sur un polydisque ultrametrique},
1968, IV.5 Theorem 1.
\bibitem{VdP} M. van der Put, \emph{Rigid analytic spaces}, 1975--1976,
Sections 1 and 2; ordinary Tate/Weierstrass foundations as disclosed above.
\bibitem{CT} B. Conrad and M. Temkin, \emph{Non-archimedean analytification of
algebraic spaces}, Theorem 2.3.1, Lemmas 4.2.3--4.2.4.
\bibitem{Ducros} A. Ducros, \emph{Families of Berkovich spaces}, 2.1.3--2.1.4.
\bibitem{Stacks} The Stacks Project, Tags 0AG0, 086U, 0BB1, 0EN6, 0ENA, 0END.
\end{thebibliography}
```
