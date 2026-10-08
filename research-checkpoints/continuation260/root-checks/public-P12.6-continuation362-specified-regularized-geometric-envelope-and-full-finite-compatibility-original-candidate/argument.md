# Complete new P12.6 argument

Only entire qualified G331 and G345 are imported correctness grants. All other mathematical packets and verdicts are data. The full proofs follow.

## n1

Supports: G331, G345

\section{Framework, actual geometric pullback, and quotient topology}
\textit{Supports: G331, G345.}

Let $R$ be an excellent reduced local ring, $\mathfrak a$ a proper primary ideal, and $X_R=\{v:v(\mathfrak a)=1\}$ its ENTIRE centered real-semivaluation section. Supports are arbitrary primes below the marked maximal ideal. For a finite reduced algebra $B$, use its whole finite semilocal section $X_B$ with gauge $\mathfrak aB$. All operations below take place there before decomposing into closed-center pieces. If the reduction has dimension zero, the section is empty. Nilpotents are invisible; products below use reduced top degree.

The two imported results are precisely entire qualified G331 and G345. The former constructs a geometric core on actual PRIMARY blowups: actual negative effective finite REAL exceptional Cartier presentations with nonnegative degrees on every contracted proper integral curve. Its uniform class $C_R$ equals the uniform ideal class; its completion $D_R$ consists of actual infima of decreasing $C_R$-nets, including bottom. It proves positive $C,D$ descent under every reduced finite injection exactly for functions constant on EVERY restriction fibre. It supplies compactness, gauge cocycles, normal-domain norm kernels with full fibre support, and the normalization conductor quotient. G345 supplies independently supported Cartier products on bounded $D_R$, arity $\dim R-1$, ordinary OPEN locality, uniform weak continuity, and bounded decreasing NET continuity with a prescribed $D_R$ limit. Neither grant supplies the new finite-map or envelope conclusions here. Their full statements, proofs, source ledgers, corrections and scopes accompany this paper unchanged. Smooth specialization throughout means their CLOSED smooth affine algebraically closed characteristic-zero BFJ scope, plus direct DVR/empty cases.

Finite pullback is geometric already on the core. If $I$ is primary, the degreewise surjection
\[
\operatorname{Rees}_R(I)\otimes_R B\longrightarrow \operatorname{Rees}_B(IB)
\]
puts $\operatorname{Bl}_{IB}B$ as a closed subscheme of the finite base change of $\operatorname{Bl}_I R$. Thus the actual source model is finite over the base model. This assertion is made for the GLOBAL finite semilocal $B$, not for an individual localization $B_q$, which need not be finite as an $R$-module. The Rees algebra is reduced. Each surviving positive-dimensional component has generic point outside the exceptional fibre: a component mapped entirely to the closed point is zero-dimensional and contributes no centered boundary. An exceptional Cartier equation, invertible outside that fibre, is nonzero on each surviving generic component and therefore regular on the reduced source. Its pullback is an actual effective Cartier divisor. For a contracted integral curve mapping to a curve, numerical pullback degree is the image degree times its full function-field degree, with the appropriate closed residue-field conversion; if its image is a point, the degree is zero. These are numerical intersections on proper FIELD curves, not degrees on global Chow classes. Negative effectivity and curve-nefness therefore pull back. Evaluation uses the valued quotient field $\operatorname{Frac}(B/Q)$ and the lattice with generic trivialization; restricting that lattice recovers the pulled-back base evaluation on EVERY support. Common product-primary refinements preserve these identities. Ideal comparison and the two authorized completions then give pullback on $C,D$ without arbitrary-model cofinality.

Every finite map factors through $A=R/\ker(R\to B)$, which is reduced. Restriction $X_B\to X_A$ is a compact surjective quotient by support-quotient valuation extension (G331); $X_A$ is literally the closed subset $v(\ker)=\infty$ of $X_R$. For injections write $\rho:X_B\to X_R$. Normalization is the full quotient: finite conductor value gives singleton fibres; infinite conductor value gives equality of restrictions through $S/\mathfrak c\to R/\mathfrak c$. Lower-dimensional and vertical points are retained.

Here is a topological lemma needed for the SPECIFIED regularization. For a bounded-above extended function $F$ on compact Hausdorff $X$, write
\[
F^*(x)=\inf_{U\ni x}\sup_{z\in U}F(z).
\]
For a continuous surjection $\rho:Y\to X$ of compact Hausdorff spaces,
\[
(F\circ\rho)^*(y)\le F^*(\rho y),\qquad
F^*(x)=\max_{\rho y=x}(F\circ\rho)^*(y).                 \tag{1}
\]
The first inequality follows by pulling back neighborhoods. The USC function on the compact nonempty fibre attains its maximum, including the all-bottom case. To prove the opposite inequality, take any finite $t$ larger than that maximum. Each fibre point has an open neighborhood $O_y$ on which $F\circ\rho<t$. A finite union $O$ covers the fibre. The image of compact $Y\setminus O$ is closed and misses $x$; its complement $U$ is a neighborhood with $\rho^{-1}U\subset O$. Surjectivity gives $F<t$ on $U$, hence $F^*(x)\le t$. Arbitrarily small such thresholds prove (1), including maximum $-\infty$. No openness is used. If $\rho$ is OPEN, every $\rho(O_y)$ is a neighborhood of $x$, so the same neighborhood definition gives the stronger pointwise equality
\[
(F\circ\rho)^*=F^*\circ\rho.                          \tag{2}
\]

A useful independent openness criterion is the following. Suppose there is a positive kernel $\kappa_x$ of finite mass, supported on the ENTIRE fibre, such that $Th(x)=\int h\,d\kappa_x$ is continuous for EVERY real continuous $h$ on $Y$. For open $O\subset Y$ and $y\in O$, compact-Hausdorff normality supplies a nonnegative continuous cutoff supported in $O$ and positive at $y$. Full support gives $Th(\rho y)>0$. Its positive locus is an open neighborhood contained in $\rho(O)$. These neighborhoods cover $\rho(O)$, proving openness. Full support and all continuous tests are essential; no lower bound for individual weights is assumed.

If the target is a normal local domain and EVERY minimal source component dominates it, sum G331's norm kernels for those domain quotients, with generic inseparable lengths included. Every source fibre point occurs on at least one such component and has positive weight there. Restriction of a continuous source function is continuous on its component, so the sum is continuous on all tests and has full support. Consequently this finite boundary map is open. Vertical components invalidate this argument: their points cannot be discarded merely because their generic/top-degree weight is zero.

## n2

Supports: G331, n1

\section{Reduced finite-flat kernels and positive fibre maxima}
\textit{Supports: G331, n1.}

Let $R\to B$ be finite locally free of rank $d>0$, with both rings reduced. Over the local base choose a basis. Multiplication by $h=\sum T_jg_j$, with $g_j$ finite $R$-module generators of a $B$-ideal $J$, has characteristic polynomial
\[
\det(t-m_h)=t^d+\sum_{i=1}^d(-1)^ic_i(T)t^{d-i}.
\]
Let $C_i(J)$ be the coefficient ideal of $c_i(T)$ and $N(J)=C_d(J)$. Changing basis conjugates the matrix. Changing generators substitutes linear forms in $T$ in both directions, proving ideal independence. The determinant on the top exterior power proves arbitrary base-change compatibility; replacing $h$ by a product proves norm multiplicativity. This is the full immediate Stacks 0BD2 CURRENT 31.18.6 construction at a finite locally free morphism; its exterior-power proof was checked. For $J\supset\mathfrak a^NB$, add base elements $x\in\mathfrak a^N$ redundantly. The pure coefficient $x^d$ is in $N(J)$, so $N(J)$ contains a boundary power and is unit-or-primary.

For ANY base support $P$, first enter the valued field $K=\operatorname{Frac}(R/P)$. The fibre algebra $B\otimes_RK$ can be NONREDUCED even though $B$ is reduced. In a finite normal field extension splitting its residue fields, it becomes Artinian local factors of lengths $l_j$, residue equal to that field, with $\sum l_j=d$. Multiplication on a factor is its residue scalar plus a nilpotent map; thus
\[
\det(t-m_h)=\prod_j(t-h_j)^{l_j}.
\]
Generic inseparability and all special-fibre nilpotent lengths are included. Extend the base valuation to the integral closure in the splitting field and evaluate the residue homomorphisms $B\to K_j$ there. These give centred lifts $w_j$, and
\[
v(N(J))=\sum_j l_jw_j(J).                              \tag{3}
\]
Indeed the minimum coefficient value of a polynomial is multiplicative: quotient its support, divide by a coefficient of least finite value, and reduce to nonzero residue polynomials whose product is nonzero. Apply this Gauss argument to the determinant factorization. Boundary powers ensure finite ideal values here.

The measures $\kappa_v=\sum l_j\delta_{w_j}$ have mass $d$. Their integrals on every bounded ideal gauge are fixed by (3). The ideal-difference lattice is dense in ALL real continuous source functions: it contains constants, separates points via $(b)+\mathfrak a^N B$, and has the identity
\[
\min\{v(I)-v(J),v(K)-v(H)\}=v(IH+KJ)-v(JH).
\]
Center separation is by semilocal boundary ideals. Compact lattice approximation proves density (G331), so equal masses imply choice independence on all tests and hence as measures. Conversely any lift has a support over $P$; its residue field embeds into a splitting field, and extending that particular lift makes it appear in the Dirac sum with positive length. Choice independence therefore proves FULL fibre support and fibre cardinality at most $d$. First (3), then density with fixed mass, proves continuity on every continuous test. The openness criterion in n1 applies.

Define $\tau H(v)=\int H\,d\kappa_v$. It sends $-w(J)/q$ to $-v(N(J))/q$, preserves $C$, and sends an actual decreasing $C$-representation to a decreasing $C$-representation of the trace. A finite positive sum commutes with decreasing nonpositive extended nets: for finite limits approximate each of finitely many terms at one common index; if one limit is bottom its positive weight forces bottom. Thus $\tau$ preserves $D$, including partial bottom. No integration theorem for an arbitrary measurable net is used.

There is also a direct positive maximum. Put $m=\min_{\rho w=v}w(J)$. Then
\[
m=\min_{1\le i\le d}v(C_i(J))/i.                      \tag{4}
\]
All roots of multiplication by a generator have value at least $m$, so each degree-$i$ coefficient has value at least $im$, proving one inequality. Choose a generator attaining $m$ at a fibre point. Evaluating its characteristic equation there, if every nonleading coefficient had value $>im$, the leading root power would be uniquely least-valued, contradicting the equation. Hence some coefficient value is at most $im$. A specialized coefficient is an $R$-linear combination of the family coefficients, proving the reverse inequality in (4). This proof tolerates cancellation and inseparable roots.

The ideals $C_i$ need not be primary. Let $L=\sup_X v(C_d)/d<\infty$, choose an INTEGER $N>dL$, and replace every $C_i$ by the genuinely unit-or-primary $C_i+\mathfrak a^N$. Values are truncated at $N$; because $m\le L$ and $N/i>L$, the minimum in (4) is unchanged. Therefore
\[
\rho_{\max}(-w(J)/q)=\max_i\{-v(C_i+\mathfrak a^N)/(qi)\}\in C_R. \tag{5}
\]
The maximum is 1-Lipschitz in uniform norm, so it preserves $C$. On a finite fibre, maximum commutes with a decreasing net: if each limiting value is below a finite threshold, directedness gives one index with every value below it. Thus it preserves ACTUAL $D$ limits as well.

For a normal-domain target without vertical components, the same maximum theorem follows independently from G331's kernels. On each domain quotient take the integral closure in a finite normal splitting field. The maximum of the finitely many embedding pullbacks of a $C$ or $D$ source function belongs to that class upstairs. The full-support kernel shows that its value is exactly the full fibre maximum and is independent of the splitting-field lift. G331's positive FULL-fibre descent puts that maximum downstairs in $C,D$. Take the maximum across the finitely many dominating source components. Every point is covered, so this is the full maximum. Finite-fibre decreasing passage is exactly the preceding argument. This proves both openness AND geometric maximum preservation in the normal/no-vertical and reduced finite-flat cases; topology alone would not prove positivity.

## n3

Supports: G331, n1, n2

\section{The specified whole-section regularized operator}
\textit{Supports: G331, n1, n2.}

Let $\phi:X_R\to[-\infty,+\infty)$ be USC and bounded above, with partial bottom allowed. Define, on the ENTIRE compact section,
\[
p_R\phi=\sup\{u\in D_R:u\le\phi\},\qquad E_R\phi=(p_R\phi)^*.
\]
Bottom is a competitor. Nonpositivity and the USC obstacle give
\[
p_R\phi\le E_R\phi\le\min(\phi,0).                    \tag{6}
\]
There is no positivity assumption in the definition. Exactly
\[
E_R\phi\in D_R\ \Longleftrightarrow\ \text{the competitors have an actual greatest }D_R\text{ member}. \tag{7}
\]
If positive, (6) makes $E$ a competitor, hence $E=p$. Conversely a greatest member equals $p$, is USC, and therefore equals its regularization. This includes the all-bottom case.

For finite continuous $f$, the raw suprema using $C$ and $D$ are equal. If $u\in D$ is below $f$, an actual representation $g_\alpha\downarrow u$ has, for each $\epsilon>0$, one term $g_\alpha<f+\epsilon$ everywhere: continuous strict-test open sets cover the compact section, and directedness selects a common index. Then $g_\alpha-\epsilon\in C$ is below $f$ and above $u-\epsilon$. Let $\epsilon$ decrease. This does NOT claim that every USC obstacle has this reduction. The common raw supremum $p$ is LSC and finite, since a sufficiently negative constant is below $f$. Thus
\[
E_Rf\in D_R\ \Longleftrightarrow\ p_Rf\text{ is continuous},
\quad\text{and then } E_Rf=p_Rf\in C_R.                \tag{8}
\]
For the forward implication use (7), which makes the LSC $p$ USC. For the reverse, choose a $C$ competitor within $\epsilon$ of $p$ at each point; continuity of $p$ and those competitors gives open neighborhoods. A finite subcover and finite maxima yield a $C$ competitor uniformly within $\epsilon$ of $p$. Uniform closure proves $p\in C$. On a reduced curve the granted geometric class is the full nonpositive branch orthant, so $E\phi=\min(\phi,0)$ on the finite section. Empty sections have their unique empty function. Equations (7)--(8) give a selected positive domain, not universal existence of positive envelopes. At the qualified smooth BFJ scope, G331 identifies $D$ with the full canonical BFJ all-semivaluation class with bottom adjoined. Consequently this is exactly the USC supremum of that SAME class; any smooth envelope with this signature and an actual greatest competitor agrees by (7). A published fixed-skeleton nef-divisor envelope has a narrower obstacle signature; no assertion of general smooth USC-obstacle existence is inferred from it.

For either map class in n2, and every such extended USC obstacle,
\[
p_B(\phi\circ\rho)=p_R\phi\circ\rho.                \tag{9}
\]
One inequality is pullback. For the other, take a source $D$ competitor; its full fibre maximum is a downstairs $D$ function below $\phi$, dominating that competitor on each lift. This proves the raw equality for all supports and partial-bottom patterns. The map is open by n1--n2, so (2) gives the actual SPECIFIED regularized identity
\[
E_B(\phi\circ\rho)=E_R\phi\circ\rho.                \tag{10}
\]
This is an equality of functions even outside the positive domain. Full positive descent proves exact equivalence of their positive domains; for finite continuous obstacles (8) also identifies both positive outputs with $C$. We have used positive maxima AND openness, not merely ideal extrema or a raw supremum. No normal-target assertion with vertical components is made.

For an arbitrary reduced finite INJECTION define the constrained upstairs envelope by taking only FULL-fibre-constant $D_B$ competitors below $\phi\circ\rho$, then ordinary upstairs USC regularization; denote it $E_{B,\mathrm{fib}}$. G331's completed positive descent identifies its raw supremum with $p_R\phi\circ\rho$. Applying compact quotient formula (1) proves the exact general rule
\[
E_R\phi(x)=\max_{\rho y=x}E_{B,\mathrm{fib}}(\phi\circ\rho)(y). \tag{11}
\]
In particular downstairs positivity holds exactly when $E_{B,\mathrm{fib}}$ is BOTH in $D_B$ AND constant on EVERY fibre. Indeed positive downstairs output equals the raw supremum by (7), whose pullback is USC and makes the constrained regularization equal to it. Conversely a positive fibre-constant constrained regularization descends positively by G331; it is below $\phi$ and above $p_R\phi$, so equality follows. The fibre condition cannot be dropped after regularization.

The unconstrained source envelope dominates the constrained one. Thus the universal comparison is
\[
\rho^*E_R\phi\le M_{\mathrm{fib}} E_B(\phi\circ\rho),  \tag{12}
\]
where $M_{\mathrm{fib}}H(y)=\max_{\rho z=\rho y}H(z)$. Without openness this does not imply $\rho^*E_R\phi\le E_B$. If $E_B$ is positive, equality $E_B=\rho^*E_R$ holds exactly when $E_B$ is FULL-fibre constant: descent of its greatest competitor proves sufficiency, and necessity is immediate. If both envelopes are positive, pulled downstairs output is a source competitor, giving that pointwise inequality; equality still requires full constancy. For normalization, ``full'' means the entire conductor quotient, including nonminimal supports and all lower-dimensional points. These are operator statements, rather than definitions of another order completion.

## n4

Supports: G331, n1, n3

\section{Entire all-field node calculation: regularization reverses one lift inequality}
\textit{Supports: G331, n1, n3.}

Over ANY field $k$, take
\[
R=k[x,y,z]_{(x,y,z)}/(xy),\quad S=A_1\times A_2,
\quad A_1=k[x,z]_{(x,z)},\quad A_2=k[y,z]_{(y,z)}.
\]
The normalizations are the two regular planes. With $T=k[z]_{(z)}$, restriction at $x=0,y=0$ gives $R=A_1\times_T A_2$. Local denominators can be lifted with the same nonzero constant term, proving the localized fibre product as well. $S$ is generated as an $R$-module by its two idempotents, and the conductor is $\mathfrak c=(x,y)$: a conductor element must have zero common residue in $T$, and that condition suffices. Hence $R/\mathfrak c=T$, $S/\mathfrak c=T\times T$. There is exactly one nontrivial full boundary fibre: $w_1$ killing $x$ on $A_1$ and $w_2$ killing $y$ on $A_2$, both restricting to $\operatorname{ord}_z$ on $T$. Call its base point $v_0$. All other fibres are singletons. Gauge is $\mathfrak m$.

The bounded finite continuous obstacle is
\[
f(v)=-1-1/v(y),\qquad1/\infty=0.
\]
Normalized values have $v(y)\ge1$. On $A_1$ the obstacle is $-1$, and on $A_2$ it lies in $[-2,-1]$. If $o_i$ is ordinary regular order on plane $i$, every normalized valuation $w$ has $w(J)\ge o_i(J)$ for primary ideals: $J\subset\mathfrak m_i^{o_i(J)}$ and $w(\mathfrak m_i)=1$. This gives $u(w)\le u(o_i)$ for every $u\in C_{A_i}$, and then for every actual $D$ limit, including bottom. At $o_2$, $f=-2$. Thus the unconstrained source envelope is the ACTUAL $C_S$ function
\[
p_S(f\circ\rho)=E_S(f\circ\rho)=(-1,-2).              \tag{13}
\]
The constants are semilocal primary profiles (use $\mathfrak m_1\times\mathfrak m_2^2$), and are below the obstacle. The upper bounds just proved show they are greatest $D$ competitors.

For each integer $N\ge2$ put $\alpha=1/(N-1)$ and
\[
h_{1,N}(w)=-(1-\alpha)-\alpha\min\{w(x),Nw(z)\}.
\]
This is a $C_{A_1}$ profile using the proper PRIMARY ideal $(x,z^N)$, since $\min(w(x),w(z))=1$ implies the displayed minimum is at least one. It is at most $-1$, and at $w_1$ it equals $-2$. Pair it with constant $-2$ on $A_2$. The tuple agrees on the ENTIRE shared fibre, so G331 descends it to a $C_R$ competitor for $f$. At every first-plane point off $w_1$, $w(x)<\infty$; otherwise the quotient is the one-dimensional regular $T$, whose normalized section is the singleton $w_1$. At such a point the displayed profile tends to $-1$ as $N\to\infty$. On the whole second plane every downstairs $D$ competitor is at most $-2$ by regular order domination. Therefore, pointwise and using both raw $C$ and $D$ suprema,
\[
p_R f=-1\text{ on the first plane off }v_0,
\qquad p_R f=-2\text{ on the whole second plane, including }v_0. \tag{14}
\]

Monomial valuations $w_M(x)=M,w_M(z)=1$ converge to $w_1$ on EVERY polynomial and local denominator: transverse terms gain unbounded value, the surviving $z$ polynomial has its ordinary order, and denominators with nonzero constant have value zero. This works in every characteristic. First-plane values in (14) therefore raise the regularization at $v_0$ to $-1$. Away from $v_0$ on the second plane the image of the compact first plane is closed and absent, so a neighborhood avoids it. Consequently
\[
E_R f=-1\text{ on the entire first plane including }v_0,
\qquad E_R f=-2\text{ on the second plane off }v_0.    \tag{15}
\]
Its pullback is USC on each plane (a raised value at the closed point $w_2$ on the second), hence the function is USC by the compact quotient. But it is NOT in $D_R$: its restriction to $A_2$ has value $-1$ at $w_2$ and $-2$ at $o_2$, violating the proved domination inequality. At the second lift,
\[
\rho^*E_R f(w_2)=-1>-2=E_S(f\circ\rho)(w_2).          \tag{16}
\]
This is a genuine gap ONE for the SPECIFIED regularized operator, not merely the raw envelope.

The constrained upstairs raw supremum is the pullback of (14). Its ordinary regularization is $(-1,-2)$: on the first plane $w_1$ is raised to $-1$, whereas the second is constantly $-2$. Thus $E_{S,\mathrm{fib}}$ is positive and continuous but NOT fibre constant. Its full fibre maximum is exactly (15), verifying (11) at every point and the necessity of BOTH positivity and fibre constancy. On the generic branches the degree-one trace of (13) has incompatible limits $-1$ and $-2$ at the shared point, so an unrestricted continuous degree trace cannot be fabricated. In base change,
$S\otimes_R S=A_1\times T\times T\times A_2$;
the two vertical $T$ components are real parts of the support/fibre geometry and must remain.

## n5

Supports: G331, G345, n1, n3, n4

\section{Literal closed images and a normal target with vertical components}
\textit{Supports: G331, G345, n1, n3, n4.}

For a noninjective finite map factor through $A=R/\ker\to B$ as in n1. Restriction of ideals, uniform limits and actual decreasing representations gives maps $C_R\to C_A$, $D_R\to D_A$. It does not give surjectivity. If $E_R\phi$ is positive, its restriction is an intrinsic competitor, so
\[
(E_R\phi)|_{X_A}\le E_A(\phi|_{X_A}).                 \tag{17}
\]
The positivity hypothesis is needed for this reasoning; arbitrary nonpositive regularizations are not competitors. No ambient extension or restriction equality follows from a closed boundary embedding.

An all-field counterexample has positive CONTINUOUS envelopes at both ends. Put $R=k[x,y]_{(x,y)}$, $Q=R/(xy)$, and gauge $\mathfrak m$. The two curve points are $w_x(x)=1,w_x(y)=\infty$ and $w_y(x)=\infty,w_y(y)=1$. Let $f=-1/v(x)$, continuous in $[-1,0]$. On the regular surface the ordinary order $o$ satisfies $u(v)\le u(o)$ for every $C,D$ function, by the same primary-ideal argument as n4. Since $f(o)=-1$, every competitor is at most $-1$ everywhere; constant $-1$ is a competitor. Thus $p_Rf=E_Rf=-1\in C_R$.

Downstairs on $Q$, the genuine proper primary profiles $-v((x^N,y))/N$ equal $(-1,-1/N)$ and converge uniformly to $(-1,0)$. Thus the restriction of $f$ is itself in $C_Q$, and
\[
E_Q(f|_{X_Q})=(-1,0).
\]
The gap in (17) at $w_y$ is exactly ONE. No $D_R$ extension of this tuple exists: G331's normal zero dichotomy says a $D$ function with value zero at any point on a normal local branch is identically zero, contradicting its value $-1$ at $w_x$. This proves an actual extension obstruction, not just different ideal presentations. The ambient lifts of those quotient profiles increase to the function $0$ where $v(y)<\infty$ and $-1$ where $v(y)=\infty$. It is not USC, since monomial $(v(x),v(y))=(1,M)$ tends to $w_x$. No increasing closure is available.

The intrinsic arities must stay distinct. G345 gives $\mu_R(-1)=\delta_o$ (surface, one input) and $\mu_Q()=\delta_{w_x}+\delta_{w_y}$ (curve, zero inputs). As a finite $R$-module $Q$ has zero ambient degree-two contribution, but that does not erase its intrinsic reference measure or boundary points.

Finally take the NORMAL target $R$ above and the finite reduced INJECTION
\[
R\longrightarrow B=R\times Q,\qquad r\longmapsto(r,\bar r).
\]
Its source envelope for the pulled obstacle is the actual $C_B$ tuple $(-1,(-1,0))$, whereas $E_Rf=-1$. Both are positive continuous, with gap ONE at the vertical lift $w_y$. The source point $w_y$ is isolated on the clopen finite curve section, but its image is not open in $X_R$: monomial values $(M,1)$ approach it. Hence the boundary map is not open. The full fibre maximum is zero at that base point and $-1$ elsewhere; it is not continuous and cannot be in $D_R$ by normal zero dichotomy. The dominating normal-domain trace ignores the vertical generic weight but consequently lacks full fibre support. Normality ALONE cannot replace the no-vertical hypothesis of n1--n3. This example and n4 retain all support and lower-dimensional points and prevent an invented universal compatibility theorem.

## n6

Supports: G331, G345, n1

\section{Full geometric finite projection with varying top-component degrees}
\textit{Supports: G331, G345, n1.}

Write $n=\dim R\ge1$, $p=n-1$. For a finite reduced $R$-algebra $B$ and each closed center $q$ over $\mathfrak m$, let $f_q=[\kappa(q):\kappa(\mathfrak m)]$. Define the AMBIENT product notation
\[
\mu_B^{[R]}(H_1,\ldots,H_p)=
\sum_{\dim B_q=n} f_q\,\mu_{B_q}(H_1|_q,\ldots,H_p|_q).
\]
Lower-dimensional centers have zero ambient degree-$n$ contribution; their points and intrinsic lower-arity products remain. For each top-dimensional minimal prime $P$ of $R$, let $K_P=\operatorname{Frac}(R/P)$ and
$d_P=\dim_{K_P}(B\otimes_R K_P)$; missing components have degree zero. Let $j_P:X_{R/P}\hookrightarrow X_R$ be the literal supported closed section. For every bounded actual $D_R$ tuple,
\[
\rho_*\mu_B^{[R]}(\rho^*u_1,\ldots,\rho^*u_p)
=\sum_{\dim R/P=n}d_P\,j_{P,*}\mu_{R/P}(j_P^*u_1,\ldots,j_P^*u_p). \tag{18}
\]
For a noninjective map $\rho$ here is restriction to its exact image followed by the inclusion. It is meaningful on the whole section, with all supports retained. No scalar degree is used unless the $d_P$ are constant; if all top $d_P=d$, the reduced component formula gives exactly $d\mu_R(\boldsymbol u)$.

First reconstruct the geometric projection. Use the actual finite PRIMARY source models from n1, and common product-primary refinements for the input cores and test. All pulled effective equations stay regular on surviving reduced components. Give the base $\operatorname{Spec}R$ the dimension function $\delta(P)=\dim R/P$; excellence supplies universal catenarity, and its finite-type transcendence-degree extension is the setting of complete Stacks 02QL Situation 42.7.1. Each top component of the model has $\delta$-dimension $n$. On a source integral top component dominating the base integral component with finite function-field degree $\delta_Q$, the proper dominant map has equal $\delta$-dimension. Complete Stacks 0AYA 42.26.3 gives the ACTUAL divisor-cycle equality
\[
f_*[f^*E]_{n-1}=\delta_Q[E]_{n-1}.                   \tag{19}
\]
This equality precedes all Chow quotients. The full field degree includes inseparability. Its recursive norm/divisor foundation 42.18.1 is disclosed ordinary published background, not an independently reread proof or a resolution theorem.

At a top exceptional generic point the reduced local ring is one-dimensional. Embed it into the sum of its component domains; the cokernel is finite length. Multiplication by the regular Cartier equation has kernel and cokernel of equal length on that cokernel. Therefore its Cartier-divisor length is the sum of component Cartier lengths. Thus reduced generic component weights in (19) are one, while every supported Cartier thickness is still included. On the closed fibre, these cycles are proper over residue FIELDS. Complete Stacks 0BEL 33.45.7 applies numerically there to pulled line bundles, with residue-field dimensions retained. When the supported Cartier scheme is only over an Artinian quotient of $R$ (including mixed characteristic), filter by powers of $\mathfrak m$: the coherent layers are proper over $\kappa(\mathfrak m)$, Euler characteristics add, and all local generic thickness lengths add. This is G345's independently supported Euler/Koszul construction, not an application of a FIELD lemma to a mixed-characteristic thickening. Equations (19) and numerical projection therefore prove the supported Cartier pairing version of (18), including all $f_q$.

The input divisor evaluations are the support-quotient lattices of n1. G345 identifies its geometric core measure with these pairings and proves representation independence through an ACTUAL fixed-primary section-image comparison on one common model. Thus this geometric calculation does not assume that uniform convergence of arbitrary Cartier functions implies intersection convergence; neither arbitrary proper-model cofinality nor a Cartier determination of a traced non-Cartier function is needed.

For clarity, here is the complete algebraic verification and the passage to all bounded inputs. For primary $I_1,\ldots,I_r$ put $P_s=\prod I_i^{s_i}$. Complete current Swanson--Huneke 17.4.1--3 supplies the eventual length polynomial and the degree-$n$ form
\[
H_M(s)=\sum_{|a|=n}\frac{e_R(I_1^{[a_1]},\ldots,I_r^{[a_r]};M)}{a_1!\cdots a_r!}s^a,
\]
zero when $\dim M<n$. We use its full defining setup and immediate proof at arbitrary Noetherian local hypotheses, not a coefficient inequality inferred from domination. For $0\to M_1\to M_2\to M_3\to0$, the multigraded intersection module
$\bigoplus_s(P_sM_2\cap M_1)$ is a submodule of the finite multi-Rees module of $M_2$. Finite homogeneous generation (the full 17.1.6 Artin--Rees argument) gives a common vector $c$ with
\[
P_sM_1\subset P_sM_2\cap M_1\subset P_{s-c}M_1
\]
for large coordinatewise $s$. The outside length polynomials have the same top form, since they differ by a constant shift. On every positive rational ray their difference has lower order. Squeezing the middle quotient gives the same top form on every such ray, hence the same homogeneous polynomial by polynomial identity. The ACTUAL exact quotient sequence then gives $H_{M_2}=H_{M_1}+H_{M_3}$. This independently reconstructs the application of 17.4.4; reduction modulo $P_s$ was never assumed left exact.

A finite module has a finite prime filtration. Indeed choose an element with maximal annihilator, which is prime (if $ab$ kills it and $b$ does not, the annihilator of $b$ times that element is strictly larger unless $a$ was already there). Repeat on the quotient; the ascending submodule chain terminates by Noetherianity. Apply top-form additivity to the factors. At a top minimal $P$, $R_P$ is a field because $R$ is reduced. The number of factors supported there is the localized dimension $\dim_{K_P}B\otimes_RK_P=d_P$; all other factors have smaller dimension. Consequently
\[
H_B=\sum_{\dim R/P=n}d_PH_{R/P},\qquad H_R=\sum_{\dim R/P=n}H_{R/P}. \tag{20}
\]
The finite generic algebra is a product of fields, so $d_P$ is the sum of their FULL field degrees, with inseparability.

For every primary product, the finite Artinian quotient $B/P_sB$ decomposes into its closed-center local factors. Composition series give exactly
\[
\ell_R(B/P_sB)=\sum_q f_q\,\ell_{B_q}(B_q/P_sB_q).    \tag{21}
\]
No separable-degree replacement is allowed. Comparing top forms in (20)--(21) proves every mixed ideal moment in (18), matching the preceding geometric projection. For rational primary profiles use G345's exact moments, divide by the input denominators, and test on every ideal gauge $v(J)$. Ideal-difference lattice density on the ENTIRE section and the reference mass identify the Radon measures. Uniform rational approximation proves (18) on $C$ via weak uniform continuity. For bounded $D$ inputs take actual decreasing $C$ representations with their common bound. Every quotient/pullback representation decreases to its specified $D$ limit by G331. G345's decreasing NET theorem applies on every factor, and continuous compact pushforward plus the finite sums passes each fixed continuous test to the limit. No arbitrary measurable-net convergence is invoked.

For normalization, each top generic $d_P=1$, so (18) is precisely the full closed-residue-weighted conductor pushforward. Compatible upstairs bounded tuples descend positively by G331, and their measures push along the FULL quotient, adding all identified masses. On curves $p=0$ the actual reference measure is
$\sum_q f_q\operatorname{ord}_q(\mathfrak a)\delta_{\operatorname{ord}_q/\operatorname{ord}_q(\mathfrak a)}$;
normal DVR freeness/parameter length gives the curve finite-map formula. Dimension zero is empty with zero measure. If the original algebra was nonreduced, (18) applies to its reduction and its reduced generic degrees; nilpotent generic rank is additional data, not boundary-determined. SH17.4.7's literal unquotiented colon length is not used: the valid finite term is the annihilator in the CURRENT quotient by preceding parameters, derived from 17.4.6 and confirmed on the source page.

## n7

Supports: G331, G345, n1, n2, n6

\section{One arbitrary source slot and its full conductor-admissible domain}
\textit{Supports: G331, G345, n1, n2, n6.}

Assume $n\ge2$. First let $A$ be an excellent normal local domain and $B$ a finite domain extension with fields $K\subset L$, degree $d$. Take a finite normal splitting extension $M/K$, integral closure $E$ of $A$ in it, and $G=\operatorname{Aut}_K M$. Write $e=[M:L]$. If $T$ is G331's unnormalized norm trace, the complete embedding factorization with generic inseparable lengths gives on EVERY support
\[
\rho_E^*(TH)=\frac d{|G|}\sum_{g\in G} g^*\pi^*H,     \tag{22}
\]
where $\pi:X_E\to X_B$. Embeddings of $L$ are a transitive $G$-orbit; the stabilizer count and the purely inseparable length make the factor $d/|G|$. Even if several embeddings produce the same supported lift, their lengths remain. The kernel choice independence and full support in G331 make (22) a function identity. Trace preserves $C,D$ and boundedness as finite positive sums, not via an unproved completion flattening.

Apply (18) to $E/A$ (degree $ed$) and $E/B$ (degree $e$). Closed residue weights multiply in a field tower, so the two ambient measure conventions agree. Automorphisms of $E/A$ preserve its geometric operator: for ideals this is equality of primary quotient lengths, then density and both continuities give it for bounded $D$. The remaining inputs $\rho_E^*u_i$ are $G$ invariant. Linearity in exactly ONE source slot in (22), followed by automorphism covariance, gives
\[
\rho_*\mu_B^{[A]}(H,\rho^*u_2,\ldots,\rho^*u_p)
=\mu_A(TH,u_2,\ldots,u_p).                            \tag{23}
\]
Explicitly (18) applied to the right side first multiplies it by $ed$; expanding (22) gives $d$ times the push of the $E$ product with $\pi^*H$; the $E/B$ formula turns that into $de$ times the left side. Cancel $ed>0$. Thus there is no extra degree multiplying (23). For $p=1$ there are no remaining inputs. For a reduced arbitrary source over normal $A$, decompose its ambient product into dominating domain minimal components by n6 and sum their traces. Vertical components are lower-dimensional and give zero ambient top degree, but remain in all spaces and descent conditions.

This trace also has geometric divisorial meaning without assuming a finite Cartier determination. At an excellent DVR on an auxiliary normalized PRIMARY model, its integral closure in $L$ is finite torsion-free, hence free of rank $d$. If $\pi$ is its parameter, length of the quotient by $\pi$ gives $d=\sum e_jf_j$. For a nonzero regular $g$, Smith normal form identifies the determinant valuation with the cokernel length of multiplication, namely $\operatorname{ord}N(g)=\sum f_j\operatorname{ord}_j(g)$. Both formulas include inseparability and use a DVR, not a defectless formula for arbitrary real valuations. On a section with order $b$ the trace coefficient is $b^{-1}\sum f_j\operatorname{ord}_{Z_j}D_H$. These are the proper Weil divisor pushforward coefficients on that auxiliary model. The actual geometric product identity (23) was proved by n6 and the group formula; a traced function need not be Cartier on a finite model.

Now let $R\hookrightarrow B$ be ANY reduced finite injection, and let $S$ be the finite normalization of $R$. Form
\[
C=(B\otimes_R S)_{\mathrm{red}}.
\]
Both $B\to C$ and $S\to C$ are injections: integral surjectivity on spectra persists after base change, its kernel lies in every prime, and the rings are reduced. On EVERY normal local center $S_i$, pull $H$ to $C$ and sum the preceding normal-domain traces over all minimal $C_i$ components dominating $S_i$. Denote this tuple by $T^\nu H$. It belongs to $C_S$ or $D_S$ for the corresponding source input. Empty sums are zero. Declare $H$ admissible exactly when this tuple is constant on EVERY $X_S\to X_R$ fibre. This includes conductor-infinite quotient supports, lower-dimensional centers and mixed-zero patterns, even when their ambient measure weight is zero. G331 then supplies a UNIQUE positive descent $T_RH$.

For bounded admissible $H$ the full ONE-slot identity is
\[
\rho_*\mu_B^{[R]}(H,\rho^*u_2,\ldots,\rho^*u_p)
=\mu_R(T_RH,u_2,\ldots,u_p).                          \tag{24}
\]
Proof: apply (23) on each top normal $S_i$ and weight by its closed residue degree. G345's normalization formula identifies the right side. On each top minimal component of $B$, its contraction is a top minimal component of $R$ by the finite dimension formula. Normalization $S$ is generically just that base field, so $C/B$ has generic degree ONE there. Formula (18) turns the sum of the left sides into the left side of (24). The $C$ closed residue weights agree whichever route is used, since full field dimensions multiply. Lower components contribute zero at this ambient degree but were still required in admissibility. This is a genuine arbitrary-source-slot product theorem; it is stronger than all-input pullback and not a grant from either prior manuscript.

Reduced finite-flat maps make admissibility automatic. Base change $B\otimes_RS$ is finite free on each normal domain branch. Its generic algebra is reduced, being a localization of the reduced $B$. A nilpotent dies generically and therefore vanishes by torsion-freeness; hence this base change is already reduced. Flat going-down (complete Stacks 00HS 10.39.19, whose localization/faithfully-flat proof was checked) makes every minimal source prime contract to a minimal target prime. There are no vertical components. Determinant family base change identifies $T^\nu H$ with the pullback of $\tau H$ from n2, first on coefficient ideal gauges at EVERY support, then on all continuous functions by density, and finally on $D$ by finite-fibre actual decreasing passage. Thus full admissibility holds for every bounded $D_B$ input, $T_R=\tau$, and (24) is the canonical determinant ONE-slot projection. No special-fibre Artinian length is dropped.

For a NONINJECTIVE map, apply this trace theorem intrinsically after the literal factorization through $A=R/\ker$, at arity $\dim A-1$. No ambient $R$ positive extension of the resulting trace is implied. The ambient all-pulled projection still has (18), while n5 proves why an unrestricted ambient extension would be false.

## n8

Supports: G331, G345, n1, n2, n3, n5, n6, n7

\section{Towers, exactly one gauge factor, and sharp trace limitations}
\textit{Supports: G331, G345, n1, n2, n3, n5, n6, n7.}

For a finite tower $R\to B\to F$, top generic degrees satisfy
\[
d_P(F)=\sum_{Q\mid P}[K_Q:K_P]h_Q,
\]
where $h_Q$ is the upper-stage generic degree and every field degree is full. Localizing the finite reduced algebras at $P$ makes them products of fields, proving this identity by vector-space dimension. Closed residue degrees also multiply. Applied to the actual cycles and to (18), this proves the unnormalized ALL-pulled product tower rule, without constant degree or equidimensionality.

Normal-domain traces compose by a single splitting field: group top embeddings by their restriction to the intermediate field. Every intermediate embedding extends; field and separable degrees multiply, hence generic inseparable multiplicities multiply too. One chosen supported valuation lift gives the same Dirac sum, and choice independence makes the equality valid on all supports. For the full conductor trace (24), composition requires BOTH intermediate admissibilities: $H$ must descend after its trace to $B$, and that result must be admissible over $R$. To check the normalization identity, a minimal top source component dominating a minimal $R$ component contracts to a unique minimal $B$ component, by integral incomparability; conversely each such dominating chain is active for the composite. The integral closures of $R/P$ and of its finite domain intermediate algebra in the SAME top field coincide: an element integral over the first is integral over the second, and integrality over the second implies integrality over the first by transitivity. Thus the normal branch diagrams use the same field rings. Grouping embeddings proves the identity there on every supported section, including the lower branch centers. The two assumed FULL descents give equality downstairs by uniqueness, and imply direct admissibility. Direct admissibility alone supplies neither intermediate descent.

Finite-flat determinant traces compose everywhere. At a base support, first split the Artinian fibre algebra of $B$. On a local factor of length $l$ with split residue field, filter by a composition series. The upper algebra is flat over that factor, so tensoring each layer is exact and each layer is its residue-fibre algebra. Splitting the latter into factors of lengths $m_j$ gives total lengths $lm_j$. The composed positive kernels therefore have exactly the direct fibre weights, including all nonreduced special-fibre and inseparable lengths. This proves the tower on every support and on extended nonpositive $D$ functions by finite sums. Determinant norm transitivity also follows generically from field norms and then as a global family polynomial: the reduced base injects into its product of generic fields, so equality of coefficients there is equality in the base. Constant ranks multiply; normalized constant-rank averages consequently compose. Normalized varying-rank averages do not.

The all-field varying-rank example is $A=k[[t]]$, $B=A\times A$, and $F=A\times k[[s]]$, where $t=s^2$ in the second component. The Laurent series parity decomposition proves $[k((s)):k((s^2))]=2$ even in characteristic two. On synchronized sections, direct trace weights are $(1,2)$, total degree three; iterated componentwise normalized averages have weights $(1/2,1/2)$. For $H=(0,-1)$, direct average is $-2/3$, iterated average $-1/2$, and both unnormalized traces are $-2$. On a FINITE branch link, equality of normalized kernels in a branch-surjective tower requires the next-stage generic degree to be constant across each intermediate fibre: comparison of its positive point weights proves necessity, while pulling that common degree out proves sufficiency.

There cannot be a theorem with several arbitrary independently traced source slots. Take the smooth three-dimensional $R=k[x,y,z]_{(x,y,z)}$ and $B=R\times R$, diagonal finite flat of rank two. The actual $C_B$ potentials $H=(-1,0)$ and $V=(0,-1)$ have zero product on both components, since each has a zero input. But $\tau H=\tau V=-1$, and $\mu_R(-1,-1)$ has mass one. Separate normalized traces give base mass $1/4$, still nonzero. This exact counterexample fixes the ONE-slot scope of (23)--(24).

For another base primary ideal $\mathfrak b$, let $t(v)=v_{\mathfrak a}(\mathfrak b)>0$ and $T(v)=v/t(v)$. This is a homeomorphism and $t,t^{-1}$ are bounded continuous. Transport every degree-one function AND obstacle by
\[
u_{\mathfrak b}(Tv)=u_{\mathfrak a}(v)/t(v),\qquad
\phi_{\mathfrak b}(Tv)=\phi_{\mathfrak a}(v)/t(v).
\]
Competitors correspond by G331. Multiplication by a positive continuous factor commutes with USC regularization of nonpositive functions: at finite upper limit use a uniform local bound and continuity of the factor; at bottom, any finite threshold is eventually below a sufficiently negative bound times a locally positive lower bound. This neighborhood argument proves the extended case. Hence both raw and SPECIFIED regularized envelopes obey the same cocycle, including their positive domains. Kernels, fibre extrema and full conductor conditions commute because every lift has the same base gauge. For products G345 gives exactly
\[
\mu_{\mathfrak b}(\boldsymbol u_{\mathfrak b})
=T_*[t\,\mu_{\mathfrak a}(\boldsymbol u_{\mathfrak a})]. \tag{25}
\]
For ideal moments the factor cancels the test rescaling; atomically it changes $\operatorname{ord}_Z(\mathfrak a)$ to $\operatorname{ord}_Z(\mathfrak b)$. Thus there is ONE measure factor, not $t^{n-1}$; all finite-map identities commute with it.

For a separate source primary gauge $\mathfrak c$, put $\lambda(w)=w(\mathfrak aB)$ on $X_{B,\mathfrak c}$ and $\rho_{\mathfrak c}(w)=w|_R/\lambda(w)$. The synchronized source point is $w/\lambda(w)$. A synchronized potential $H_{\mathfrak aB}$ corresponds to
$H_{\mathfrak c}(w)=\lambda(w)H_{\mathfrak aB}(w/\lambda(w))$;
a pulled-back input is $\lambda(w)u(\rho_{\mathfrak c}w)$. Therefore
\[
\rho_{\mathfrak c,*}[\lambda\,\mu_{B,\mathfrak c}(\boldsymbol H_{\mathfrak c})]
=\rho_{\mathfrak aB,*}\mu_{B,\mathfrak aB}(\boldsymbol H_{\mathfrak aB}). \tag{26}
\]
The arbitrary traced slot must be evaluated as $H_{\mathfrak c}(w)/\lambda(w)$ on the corresponding synchronized fibre BEFORE trace. This is the precise separate-source rule; tracing the unconverted slot is incorrect. Nonprimary gauges give only the finite positive partial domain, which need not be compact, and are outside these whole-section envelope statements.

## n9

Supports: G331, G345, n1, n2, n3, n4, n5, n6, n7, n8

\section{Whole-original scope and noncircularity assessment}
\textit{Supports: G331, G345, n1, n2, n3, n4, n5, n6, n7, n8.}

The exact original atom asks compatibility of independently geometric singular psh cones, envelopes and Monge--Ampere products with finite maps, normalization and conductor descent. Family 6.2 separates cone, envelope existence/regularity, bounded products, energy, and map compatibility as distinct targets; family 6.3 says construct when possible. The present assignment fixes the operator $E=(\sup_{D,u\le\phi}u)^*$ on the ENTIRE compact section. We assess that operator rather than substitute raw suprema, fixed-skeleton obstacles, or a new analytic positivity predicate.

The new compatibility package covers every reduced finite map as follows. Actual core pullback is independently geometric (n1), and the full completed positive injection/conductor descent is the qualified G331 theorem, with its actual comparison proof and source scopes retained. The specified operator is defined on ALL bounded-above extended USC obstacles. Its positive domain is exactly (7), with the concrete finite-continuous criterion (8). On normal targets with no vertical components and on reduced finite-flat maps, (10) gives exact regularized equality and exact positive-domain equivalence for the entire obstacle range. For arbitrary injections, (11)--(12) and their positivity/fibre-constancy equivalence give the full constrained quotient/conductor rule. Normalization is one such injection, with every conductor fibre present. Noninjective maps factor through their literal closed image; (17) is the justified positive restriction rule, and n5 disproves equality and extension with actual positive continuous outputs. Thus the noninjective and vertical cases have precise conclusions rather than being silently excluded.

Bounded geometric products have the full arbitrary-finite ambient projection (18), with varying reduced top degrees, primary-model geometry, inseparability and all closed residue weights. The one arbitrary source slot has the exact full conductor-admissible theorem (24), canonical on reduced finite-flat maps and normal-domain dominating traces. Tower and gauge rules are proved, with the exact hypotheses and counterexamples in n8. Positive envelopes can be inserted into these products whenever they are bounded; their membership is supplied by (7) or (8), not assumed from regularization. Ordinary open locality and prescribed-limit decreasing-net continuity are G345, not reinvented or enlarged. On curves the envelope and zero-arity reference product are explicit; in dimension zero both boundaries and measures are empty. Smooth specialization is precisely the full qualified BFJ scope already established by the two grants, with the new finite identities proved here rather than cited as singular BFJ results.

We conclude that this is a complete CORRECTED finite-map/conductor compatibility answer for the exact P12.6 at the specified independently geometric operator. This conclusion is NOT inferred merely from a false stronger universal assertion: n1--n8 provide actual positive transfer domains, the exact general constrained operator, the full product projection, the conductor ONE-slot theorem, and all gauge/tower/closed-image rules. The original wording does not demand universal positivity of every USC-regularized envelope; that existence/regularity problem is separately P12.3 and is indeed false on the node for this unrestricted domain. The package therefore gives compatibility whenever this specified operator is geometric, exact recognition and transfer of that domain, and sharp failure rules outside it. No residual P12.6 operator obligation is retained within those explicitly justified domains. A demand for universal normalization equality would be disproved by n4, but that counterexample alone is not our completion argument.

The following remain OUTSIDE this solution, without being relabelled as completed: determining or establishing positive envelopes for all obstacles at general normal singular germs (P12.3 beyond the selected domain), capacity/finite energy/unbounded product calculus (P12.5), arbitrary-proper-model cofinality, generic nilpotent intersection ranks, plurifine locality, and literal classical/CLD radial identification. The nodal mixed-zero radial obstruction is preserved. No new surface theorem is used as a grant. Universal continuous degree traces and multiple independently traced slots are false in the stated examples. A contrary interpretation demanding one of these additional operators would leave that precise additional obligation open; it would not be established by our scope decision. The original atom and family are retained literally for independent assessment.

Noncircularity: only full G331 and G345 are correctness supports. Every 348/349/351/352/356/358 proof, prior candidate, acceptance label and reviewer verdict was treated as DATA, not as a theorem. The proofs above reconstruct their required finite-map mathematics; no supplied script was executed or imported. New primary applications have complete immediate statement/proof reading and explicit recursive ordinary published background. Hashes, finite diagnostics and artifact success do not certify the mathematical claims. The final candidate flag is a new draft claim requiring independent review, not acceptance, publication or catalogue closure. Protected P16.4 remains OPEN UNCHANGED.

## n10

Supports: G331, G345, n1, n2, n3, n4, n5, n6, n7, n8, n9

\section{Deliverable evidence and complete exact P12.6 draft claim}
\textit{Supports: G331, G345, n1, n2, n3, n4, n5, n6, n7, n8, n9.}

Relative to the ENTIRE qualified G331 and G345, we claim the complete exact original P12.6 finite-map/conductor compatibility package assessed in n9, for the SPECIFIED whole-section USC-regularized geometric operator and bounded geometric products. This is a new unverified mathematical draft claim, not an inherited acceptance or catalogue action. The claim includes actual geometric pullback; open normal/no-vertical and reduced finite-flat regularized equality with exact positive-domain equivalence for bounded-above extended USC obstacles; arbitrary-injection constrained FULL-conductor regularization and its necessary-and-sufficient positivity/constancy criterion; the universal fibre-MAX comparison; literal closed-image restriction with positive-at-both-ends obstructions; full varying-degree ambient product projection; conductor-admissible ONE arbitrary source slot and its automatic determinant-flat specialization; and the exact tower and one-factor gauge rules. N4 proves the all-field entire node calculation and regularized inequality reversal; n5 preserves normal-target vertical and noninjective failures. These negative conclusions remain part of the theorem.

No P12.6 compatibility obligation is retained at this corrected specified scope. General P12.3 positive-envelope existence/regularity beyond the selected domain and P12.5 energy/unbounded products remain separate unresolved targets. No arbitrary-proper-model cofinality, original nonreduced generic rank, plurifine locality, universal continuous trace, several arbitrary trace slots, or literal classical/CLD radial identity is asserted. The exact BFJ CLOSED affine algebraically closed characteristic-zero scope, PRIMARY/all-support/reference/bounded prescribed-D-limit qualifications and literal SH17.4.7 CURRENT quotient-annihilator correction are mandatory. Protected P16.4 remains OPEN UNCHANGED.

The NEW standalone paper is P12.6-paper.tex, containing all ten new proof-bearing sections and all fourteen complete qualified grant components unchanged in literal appendices. It is accompanied by argument.md, whole-source-application-ledger.md, whole-proof-coverage.md, exact-scope.md, original-scope-and-noncircularity-decision.md, acceptance-decision.json, native-notes.json, actual-FINAL.json, and sections/n1.tex through sections/n10.tex. The actual FINAL and expanded native note fields agree in this new delivery; old actual and expanded fields were read separately and their differences retained. All support lists use only G331/G345 or earlier fully stated local notes. Prior ROOT/native manuscripts and verdicts are DATA, and their full required proofs were read and independently reconstructed.

Own \texttt{audit\_inputs.py} checked 89 bound files: 48 mathematical DATA, 37 private primary counterparts, and four complete book-context files; all sizes and SHA-256 values matched. The entire original task/family was read. Full proof-body reading included the 47797-byte completed255 proof, the 27569-byte 356 proof, all required 352/348/349/351 arguments, all actual and expanded 253/255 note fields, complete scope/source/coverage/decision records, and the full qualified grants. Exact duplicate bodies were identified rather than falsely described as fresh rereading; display truncations were repaired. The fresh primary ledger distinguishes immediate units actually read, PDFs/counterparts byte checked, one freshly viewed page, and disclosed recursive ordinary published background. Complete primary bodies and the source-page image remain LOCALONLY.

The owned standard-library \texttt{bounded\_checks.py} exhaustively evaluated only the finite Cartesian inputs in bounded-input.json. For characteristics 0,2,3,5, one to three factors with root orders 1--4 and Artinian lengths 1--3, it performed 7536 coefficient-minimum and 7536 PRIMARY-truncation arithmetic checks. For N=2--40 it checked 351 normalized rational-weight node profiles and 39 conductor endpoints. Four tower arithmetic cases and one two-slot arithmetic contrast complete 15467 observations, with zero failures. Direct and iterated varying-rank averages were -2/3 and -1/2, with common unnormalized trace -2. These checks verify only finite polynomial/profile arithmetic, not the universal geometric interpretation or any proof. The exact gap ONE and mass counterexamples are proved in n4--n5,n8; output annotations are not independently computed Monge--Ampere measures.

The environment recorded in evidence/input-audit.json and evidence/bounded-checks.json is Python 3.12.14 on Linux x86_64, standard library only. The owned source rendering command was pdftoppm -f 370 -singlefile -scale-to 1600 -png on the explicitly bound Swanson--Huneke PDF, with output LOCALONLY/source-pixels/SH-370.png; its pixels were viewed to confirm the literal omitted quotient. No supplied program was executed/imported, no additional agent/model/native job was created, no network/source acquisition or account/runtime/proxy/CA mutation occurred, and no other ACTIVE campaign, publication, catalogue, editor or tab was accessed. No supervised heavy-compute service was exposed; none was needed and no heavy local computation was launched. Compilation and independent acceptance remain with ROOT; no successful PDF or formal verification is claimed.

Rerun locally: python \texttt{audit\_inputs.py}; python \texttt{bounded\_checks.py}; python \texttt{inspect\_source.py}; python \texttt{build\_delivery.py}; python \texttt{final\_audit.py}. Programs, finite inputs, outputs, exact bindings, environment and owned artifact hashes are retained here. Execution and hash consistency establish rerunnability only. Candidate=true means solely that this last fully supported note claims the complete exact original P12.6 answer at the corrected operator scope assessed independently in n9; it does not mean acceptance or closure of the other family atoms.

