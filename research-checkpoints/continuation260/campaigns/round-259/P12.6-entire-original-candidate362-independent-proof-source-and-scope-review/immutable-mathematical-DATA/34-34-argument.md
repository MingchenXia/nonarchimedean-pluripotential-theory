# Complete local argument and qualifications

\section{n1. Exact geometric setting and primary-model pullback}
\paragraph{Supports.} Entire qualified G331 and G345.

Let $(R,\mathfrak m)$ be excellent and reduced and let $\mathfrak a$ be proper primary. Write $X_R=\{v:v(\mathfrak a)=1\}$ for the centred real semivaluations, with EVERY prime support strictly below $\mathfrak m$. A finite reduced algebra $B$ uses the finite disjoint union of sections at its closed centres $q$ above $\mathfrak m$, in gauge $\mathfrak aB_q$. Lower-dimensional positive centres remain; dimension-zero centres have empty sections. A general germ is first reduced.

The geometric meaning is fixed by G331: actual negative effective finite real Cartier presentations on directed ACTUAL primary blowups, having nonnegative degrees on every contracted proper integral curve. Its uniform continuous class is $C$, its actual decreasing-$C$-net completion is $D$. G331 PROVES their ideal comparisons and full finite-injection positive descent. We use that comparison theorem, not a definition of geometric positivity by ideals. Neither arbitrary proper-model cofinality nor an arbitrary supremum/increasing closure is granted. G345 supplies a geometric positive Radon product $\mu_R$ on bounded $D_R$, of arity $p=\dim R-1$, its supported Cartier pairing, dense primary moments, ordinary OPEN locality, uniform weak and bounded decreasing-NET continuity with specified $D$ limit. Its primary measures have one gauge factor, and normalization has CLOSED residue degrees. Both grants retain precisely smooth affine CLOSED algclosed characteristic-zero BFJ specialization, direct DVR/empty cases, and no literal CLD/classical radial identification, energy, or envelope-regularity theorem. The mandatory Keeler, Izumi, SH quotient and reader-history qualifications are unchanged in the appendices.

For a primary $I$ the multiplication maps $I^r\otimes_R B\to(IB)^r$ are surjective and compatible with products. Thus the actual source Rees algebra is a graded quotient of the base-changed Rees algebra. Relative Proj gives
\[
 \operatorname{Bl}_{IB}(B)\hookrightarrow\operatorname{Spec}B\times_R\operatorname{Bl}_I(R).
\]
It is a CLOSED immersion, followed by a finite map to the base model. Equality with base change is not asserted without flatness. The reduced source blowup has the surviving component generic points outside its primary closed fibre. A positive-dimensional source component cannot map wholly to $\mathfrak m$, since then it would be finite over $R/\mathfrak m$ and zero-dimensional. The blowup of zero on a dimension-zero component is empty. Consequently any base exceptional effective Cartier equation is a unit at every surviving source generic point, hence a nonzerodivisor on the reduced source model. Each actual effective constituent pulls back effectively.

A contracted integral source curve maps finitely to an integral base curve; a finite map cannot contract a positive-dimensional integral scheme to a point. For base residue field $k$, the pullback degree equals the image degree times the full function-field degree. Its intrinsic degree over $\kappa(q)$ is that $k$-degree divided by $[\kappa(q):k]>0$. Thus every curve-nef test survives. For a source point with support $Q$, pull the invertible lattice with generic trivialization to the valuation ring of $\operatorname{Frac}(B/Q)$. Composition gives the base valued centre and the same lattice value. This proves geometric evaluation pullback on all supports; it presumes no map from a total quotient ring to a nonminimal support quotient. Ideal restriction, uniform limits and actual decreasing representations then preserve $C,D$.

For an injection, G331 gives a compact surjective restriction $\rho$ and
\[
 \rho^*K_R=\{H\in K_B:H\text{ constant on EVERY full fibre}\},\qquad K=C,D. \tag{1}
\]
This includes nonminimal, conductor-infinite, mixed-zero and partial-bottom fibres. For normalization $S$, finite conductor value gives a singleton and infinite value gives exactly the quotient identification through $S/\mathfrak c\to R/\mathfrak c$. The finite stratum is open, the infinite stratum closed.

For a noninjection, $A=R/\ker(R\to B)$ is reduced and $X_A$ is the closed exact image $\{v:v(\ker)=\infty\}$ in $X_R$. The injection $A\hookrightarrow B$ satisfies (1). The restriction $K_R\to K_A$ preserves actual representations, but need not be onto (n4). Ambient missed points have empty fibres. On extended nonpositive functions the unrestricted fibre supremum has empty value $-\infty$ and infimum has empty value zero; these order conventions assert no geometric membership. An empty source can pull a nonbottom base function to the unique empty function. Bottom is retained in $D$ but excluded from bounded product inputs.


\section{n2. Raw envelopes: the universal compatibility statement}
\paragraph{Supports.} G331 and n1.
For $K=C,D$ and a bounded finite obstacle $f$ put
\[
 P_R^Kf(v)=\sup\{u(v):u\in K_R,\ u\le f\}.
\]
A negative reference constant lies below $f$, so this is a finite nonpositive function. No class membership or upper-semicontinuous regularization is part of this notation.

For an injection constrain the upstairs competitors to be constant on ALL $\rho$-fibres and denote the resulting supremum by $P_{B,\mathrm{fib}}^K$. Equation (1) gives an order bijection of the actual competitor sets, so evaluation at any $w$ proves
\[
 P_{B,\mathrm{fib}}^K(f\rho)=\rho^*P_R^Kf,\qquad
 P_B^K(f\rho)\ge\rho^*P_R^Kf. \tag{2}
\]
This uses proved geometric positivity descent. The constrained raw envelope belongs to $K_B$ exactly when $P_R^Kf$ belongs to $K_R$: use pullback in one direction and full descent of the fibre-constant function in the other. Moreover, IF $P_B^K(f\rho)\in K_B$, then equality of the unrestricted envelope in (2) is equivalent to its full-fibre constancy. Indeed descend that admissible envelope to $h\in K_R$; surjectivity makes $h\le f$, and the competitor property gives the reverse inequality. Necessity follows from being a pullback. No unknown raw supremum is used as an admissible competitor.

For a noninjection (2) is exact over $A=R/\ker$, with obstacle $f|_{X_A}$. The unrestricted inequality from $R$ still holds, but it cannot identify $P_A^K(f|_{X_A})$ with $(P_R^Kf)|_{X_A}$. N4 disproves that extra identity even when both envelopes are positive and continuous. All these raw identities are proved without solving the separate P12.3 existence/regularity target.


\section{n3. A full conductor-infinite normalization obstruction}
\paragraph{Supports.} G331, n1 and n2.
Work over $k=\mathbb C$ and let
\[
 R=k[x,y,z]_{(x,y,z)}/(xy),\quad S=A_1\times A_2,
 \quad A_1=k[x,z]_{(x,z)},\quad A_2=k[y,z]_{(y,z)},\quad T=k[z]_{(z)}.
\]
These are excellent polynomial localizations; $(xy)=(x)\cap(y)$ proves reduction. Restriction identifies $R=A_1\times_T A_2$: subtract a common line residue from a compatible pair, leaving $xa(x,z)$ and $yb(y,z)$, which lift independently. Denominators with nonzero constant lift to local units. The projections to both factors are onto, so the two idempotents generate $S$ as an $R$-module. Both factors are normal with the component fraction fields. Any integral element in the total fraction ring lies in both normal factors, proving $S$ is the finite normalization. Multiplication by $(1,0)$ forces the common residue of a conductor element to vanish; zero common residue is also sufficient. Hence
\[
 \mathfrak c=(x,y),\quad \mathfrak cS=xA_1\times yA_2,
 \quad R/\mathfrak c=T,\quad S/\mathfrak c=T\times T.
\]
Use $\mathfrak a=\mathfrak m$. The full upstairs boundary has two clopen plane sections. The only conductor-infinite downstairs point is $v_0$ factoring through $T$ as $\operatorname{ord}_z$. Its support $(x,y)$ is NONMINIMAL. Its complete fibre consists of $w_1$ killing $x$ on $A_1$ and $w_2$ killing $y$ on $A_2$, both inducing $\operatorname{ord}_z$. This is the full fibre because a lift killing the conductor factors through the normalized DVR section of $T$. Finite conductor fibres are singletons by $w(s)=v(cs)-v(c)$ for finite-valued conductor $c$.

The continuous obstacle on the ENTIRE section is
\[
 f(v)=-1-1/v(y),\qquad 1/\infty=0.
\]
Here $v(y)\in[1,\infty]$, and reciprocal is continuous on that compact extended interval. Thus $-2\le f\le-1$. It is constant $-1$ on the first plane and $-1-1/w(y)$ on the second, agreeing at the shared fibre.

The regular graded ring of $A_2$ is $k[y,z]$, so $o_2=\operatorname{ord}_{(y,z)}$ is a valuation, normalized, with $f(o_2)=-2$. For EVERY proper primary $J$, writing $d=o_2(J)$ gives $J\subset(y,z)^d$ and hence $w(J)\ge o_2(J)$ for EVERY normalized $w$. Unit ideals satisfy the same inequality. Negation, nonnegative real sums, uniform limits and actual decreasing infima yield
\[
 u(w)\le u(o_2)\quad\hbox{for EVERY }u\in C_{A_2}\text{ or }D_{A_2}. \tag{3}
\]
Thus every second-plane competitor is at most $-2$ everywhere. Constant $-2$ attains that bound; the first-plane envelope is $-1$. The simultaneous choice is the genuine single boundary-power ideal
$J=(x,z)\times(y,z)^2$, containing $(\mathfrak aS)^2$. Its negative profile is $(-1,-2)$, and G331 makes it geometric. Therefore the ENTIRE upstairs $C$ and $D$ envelopes are this admissible continuous tuple. Any base competitor pulls to the second plane, so (3) bounds its value at $v_0$ by $-2$. Constant $-2$ downstairs gives
\[
 P_R^Cf(v_0)=P_R^Df(v_0)=-2,\qquad
 P_S^K(f\rho)(w_1)-P_R^Kf(v_0)=1. \tag{4}
\]
No downstairs global envelope-membership claim is needed. It is not asserted constantly $-2$: $(x,y^2,yz,z^2)$ gives a competitor with first-plane ordinary-order value $-1$ and value $-2$ at $v_0$.

The fibre maximum of $(-1,-2)$ is $-2$ at second-plane monomial points $w_M(y)=M,w_M(z)=1$ but $-1$ at $v_0$. Polynomial lowest-$y$ exponents, with unit denominators, show $w_M\to w_2$ pointwise. Thus that maximum is discontinuous; its second-plane restriction violates (3), so is not even $D$. Direct tensor calculation gives
$S\otimes_R A_1=A_1\times T$ and $S\otimes_R S=A_1\times T\times T\times A_2$. The vertical $T$ components have nonempty boundaries but no field dominating a plane fraction field. They cannot be suppressed in full descent. This is a geometric conductor-infinite obstruction distinct from the curve mixed-zero literal radial obstruction and from the continuous degree-trace obstruction.


\section{n4. Positive envelopes at both ends of a noninjective counterexample}
\paragraph{Supports.} G331, G345, n1 and n2.
For EVERY field $k$, take $R=k[x,y]_{(x,y)}$, $Q=R/(xy)$, gauge $\mathfrak m=(x,y)$. $R$ is excellent normal regular of dimension two, $Q$ excellent reduced of dimension one. Its finite normalization has two DVR centres with residue degree one. The FULL $X_Q$ has exactly
\[
 w_x(x)=1,w_x(y)=\infty;\qquad w_y(x)=\infty,w_y(y)=1.
\]
Restriction is injective on these points, with closed two-point image in $X_R$. It is not onto: $o=\operatorname{ord}_{\mathfrak m}$ is a further point with support zero. The graded-domain argument makes $o$ a valuation.

On ALL $X_R$ let $f=-1/v(x)$, with reciprocal at infinity zero. Since $v(x)\ge1$, this is continuous bounded in $[-1,0]$. It has values $-1$ at $o,w_x$ and zero at $w_y$. As in (3), $J\subset\mathfrak m^{o(J)}$ gives $u(v)\le u(o)$ for EVERY $C_R,D_R$ potential on EVERY support. Thus an obstacle competitor is at most $-1$ everywhere. The genuine primary profile $-v(\mathfrak m)=-1$ attains it:
\[
 P_R^Cf=P_R^Df=-1\quad\hbox{on FULL }X_R. \tag{5}
\]
On $Q$, the genuine primary ideals $J_N=(x^N,y)Q$ give profiles $-w(J_N)/N=(-1,-1/N)$, uniformly converging on the full two-point link to $h=(-1,0)$. G331 comparison gives $h\in C_Q\subset D_Q$. It is the obstacle itself, hence
\[
 P_Q^C(f\rho)=P_Q^D(f\rho)=(-1,0). \tag{6}
\]
Equations (5)--(6) have positive continuous geometric envelopes on BOTH ends and an exact gap one at $w_y$. This failure is not an envelope-existence gap.

There is no $D_R$ extension of $h$: a value zero at $\rho w_y$ forces identically zero by G331's normal zero dichotomy, contradicting the value at $\rho w_x$. Fibre constancy on an injective boundary map is therefore insufficient for positive extension when the ring map is noninjective. Factoring through the exact image $Q$ makes the residual injection an identity; it gives no extension to $R$.

Each ideal $J_N$ lifts to the primary $R$ ideal $(x^N,y)$, but its ambient profile $g_N=-\min(v(x),v(y)/N)$ violates $f$ at $o$ for $N>1$. The $g_N$ increase pointwise to zero where $v(y)<\infty$, and to $-1$ where $v(y)=\infty$. Monomial valuations $(v(x),v(y))=(1,M)$ tend to $\rho w_x$; the limit function is zero along them and $-1$ at the endpoint. It is not USC, hence not $D_R$. Increasing closure cannot repair extension.

For a primary $\mathfrak b$, transport by $T(v)=v/v(\mathfrak b)$ and divide functions and obstacles by the same positive factor. This is an order bijection of competitors, so transports (5)--(6). In homogeneous notation $f_{\mathfrak b}(w)=-w(\mathfrak m)^2/w(x)$ and the ambient envelope is $-w(\mathfrak m)$. At the transported $y$ branch the gap is $1/\operatorname{ord}_y(\mathfrak bQ)>0$, one function factor.

G345 gives $\mu_R(-1)=\delta_o$ by degree one of the exceptional $\mathbb P^1$, but $\mu_Q()=\delta_{w_x}+\delta_{w_y}$ by zero-arity DVR Cartier degrees. The former assigns zero to the closed image; the latter has mass two. These have different arities. The quotient has zero fixed ambient degree-two contribution, while its intrinsic degree-one reference is nonzero. This is consistent with n5, not a failure of fixed-ambient projection.


\section{n5. General-degree projection of the already geometric bounded products}
\paragraph{Supports.} G331, G345 and n1.
Let $n=\dim R\ge1$, $p=n-1$. Define the ambient measure from the G345 operators, BEFORE introducing module forms:
\[
 \mu_B^{[R]}(\boldsymbol H)=\sum_{\dim B_q=n} f_q\mu_{B_q,\mathfrak aB_q}(\boldsymbol H|_q),
 \qquad f_q=[\kappa(q):\kappa(\mathfrak m)].
\]
There are $p$ slots everywhere in this expression. Smaller centres have zero ambient contribution, not their different-arity intrinsic product. Their points remain in $X_B$. For top minimal $P$ put $K_P=\operatorname{Frac}(R/P)$, $d_P(B)=\dim_{K_P}(B\otimes_RK_P)$ and $j_P:X_{R/P}\to X_R$.

\paragraph{Geometric projection first.}
Take core inputs on one actual primary model $Y$ and an effective exceptional Cartier test $E$, passing to a common primary refinement for any test. N1 gives a finite actual source model. Its reduced top components dominate the corresponding integral top target components, with finite function-field degrees $[L:K_P]$. Excellence makes the base universally catenary and $\delta(p)=\dim R/p$ a dimension function: saturated chains to the maximal ideal and catenarity give a drop of one on immediate specializations. On finite-type models use the residue transcendence-degree extension. The component maps are proper dominant integral, of equal $\delta$-dimension $n$. Complete Stacks 42.26.3 therefore gives the ACTUAL cycle equality
\[
 h_*\operatorname{div}(h^*s)=[L:K_P]\operatorname{div}(s), \tag{7}
\]
BEFORE any Chow equivalence. Its proof trivializes the bundle and uses the norm/divisor identity with $N(g)=g^{[L:K_P]}$ for a base function. The full degree includes inseparability. That recursive norm/divisor lemma is disclosed published background; it is not a birational degree-one grant.

G345's supported divisor cycle on a reduced model is the sum over its integral top components, with all local Cartier thickness weights retained. Smaller components cannot supply a closed-fibre prime of dimension $p$: their primary exceptional Cartier fibre has dimension at most their dimension minus one. On each integral proper closed-fibre prime complete Stacks 33.45.7 multiplies numerical pulled intersections by its residue function-field degree, or gives zero if image dimension drops. All these primes are proper over the residue FIELD. The Artinian Cartier thickening is handled by G345's $\mathfrak m$-filtration, not by assuming a coefficient field. Intrinsic $\kappa(q)$ degrees convert to base $k$ degrees by $f_q$ because cohomology dimensions multiply by that field dimension. Thus (7), numerical projection and the supported pairing give the core measure projection against every Cartier test with exactly those generic and CLOSED residue weights. Effective differences and real multilinearity extend all tests. This is geometric projection of independently defined operators; no multiplicity definition of a new product is being substituted.

\paragraph{Complete coefficient identification and extension.}
For finite $R$-modules let $H_M$ be the degree-$n$ part of the eventual multi-primary quotient-length polynomial, with the factorial convention of complete current SH17.4.1--4. Modules of dimension below $n$ have $H_M=0$. For an exact sequence, the multigraded Rees intersection submodule is finite over its Noetherian multi-Rees algebra. Homogeneous generators bounded by a vector $c$ give
\[
 I^sM_1\subset I^sM_2\cap M_1\subset I^{s-c}M_1\quad(s\gg0).
\]
The outside quotient polynomials have the same degree-$n$ form. The middle length is the difference of the eventual $M_2,M_3$ polynomials by the exact quotient sequence. Along every positive rational ray divide by its parameter to power $n$; the squeeze proves equality of forms, hence $H_{M_2}=H_{M_1}+H_{M_3}$. This proves the new use of SH17.1.6/17.4.4 and makes no coefficient inequality from polynomial domination.

A finite prime filtration exists: an element with annihilator maximal among nonzero element annihilators has prime annihilator (if $ab$ annihilates it but $a$ does not, apply maximality to its product by $a$). It supplies $R/Q$ in the module; repeat in the quotient. Noetherianity terminates the ascending submodules. A filtration factor of dimension $n$ must have top minimal $Q$, since a strict smaller prime extends an $n$-chain. Reduced $R_P$ is the field $K_P$; localization counts the $R/P$ factors, each of length one. Consequently
\[
 H_B=\sum_{\dim R/P=n}d_P(B)H_{R/P}. \tag{8}
\]
The generic algebra is a reduced localization of $B$, finite and zero-dimensional over $K_P$, so a product of finite fields. Thus $d_P$ is the sum of FULL field degrees, or zero when absent; there is no nonreduced generic length.

For every primary product $L$, its finite Artinian quotient gives the exact identity
\[
 \ell_R(B/LB)=\sum_q f_q\ell_{B_q}(B_q/LB_q). \tag{9}
\]
Every composition factor at $q$ is $\kappa(q)$ as an $R$-module. Finite dimension theory gives $\dim B_q\le n$. Combining (8)--(9) proves the selected degree-$n$ coefficients, including repeated, unused and unit labels with the qualified G345 conventions. Taking $p$ rational input profiles and one test $v(J)$, and dividing by the input denominators, G345's geometric moments and (7) identify
\[
 \rho_*\mu_B^{[R]}(\rho^*\boldsymbol u)
 =\sum_{\dim R/P=n}d_P(B)j_{P,*}\mu_{R/P}(j_P^*\boldsymbol u). \tag{10}
\]
For $J=\mathfrak a$ the moments give finite mass. The G331 ideal-difference lattice is uniformly dense on FULL $X_R$, including the truncated tests $v((g)+\mathfrak a^N)=\min(v(g),N)$ testing arbitrary supports. Thus equality holds as Radon measures. Uniform rational approximation proves it for $C$ tuples. For bounded $D$ tuples choose their ACTUAL decreasing $C$ representations; a lower bound $-M$ on their known limits bounds all terms by $[-M,0]$. Pullback and quotient restriction preserve these representations and known domain membership. Apply G345 prescribed-limit net continuity on the finite product index set, then fixed continuous-test pushforward and finite sums. This proves (10) without measurable-net monotone convergence or unproved completion closure.

Applying the same argument to $R$ gives its component decomposition with coefficients one, for ANY bounded tuple on $R$. More generally that decomposition on $B$ applies to arbitrary source tuples. If every $d_P=d$, (10) is $d\mu_R$. Normalization has $d_P=1$ and gives the exact closed-residue weighted conductor rule; compatible tuples descend by G331, so their measures push through the FULL quotient with masses added on identified fibres. No conductor point is deleted or declared zero capacity.

For $n=1$ (10) has no potential slots; its curve reference is $\sum_q[\kappa(q):k]\operatorname{ord}_q(\mathfrak a)\delta_{\operatorname{ord}_q/\operatorname{ord}_q(\mathfrak a)}$. For $n=0$ the boundary and measure are empty, with no negative arity. A lower-dimensional exact image has zero ambient degree while retaining its intrinsic operator (n4). Units have zero test moments; a zero input annihilates positive arity. Bottom and zero ideals are outside bounded inputs; zero scalar is the actual zero function, not $0\cdot(-\infty)$.


\section{n6. Normal-domain full orbits, envelopes and one arbitrary trace slot}
\paragraph{Supports.} G331, G345, n1, n2 and n5.
Let $A$ be excellent normal local domain, $A\subset B$ finite domain, $K\subset L$ their fraction fields and $d=[L:K]$. G331 supplies the coefficient norm ideal $\mathcal N(J)$ for a boundary-power $B$ ideal, from $N_{L(T)/K(T)}(\sum T_jg_j)$, and a choice-independent finite kernel $\eta_v$ of mass $d$ and FULL fibre support satisfying
$v(\mathcal N(J))=\int w(J)d\eta_v$. Its complete proof retains generic inseparable multiplicities and polynomial coefficient minima after quotient by every support. It extends every fibre point to a common field closure to show positive occurrence, then uses dense source gauge differences to prove kernel choice independence and full support. We use the entire result, not a rank-one defectless $ef$ formula. It sends $C_B$ to $C_A$, and finite nonpositive sums along an actual decreasing representation give actual $D_A$ representations. Write $TH=\int H\,d\eta_v$.

Choose a finite NORMAL splitting field $M/K$ containing $L$, including inseparable roots, and let $E$ be the finite integral closure of $A$ in $M$. $G=\operatorname{Aut}_K(M)$ preserves $E$. Every embedding of $L$ into $M$ extends to an automorphism of $M$: extend it to the algebraic closure, whose image of a normal splitting field is itself; purely inseparable choices are unique. There are $r=[L:K]_{\rm sep}$ restrictions, each $|G|/r$ times, whereas the norm has multiplicity $d/r$. Thus for $\pi:X_E\to X_B$, $\rho_E:X_E\to X_A$,
\[
 \rho_E^*TH=\frac d{|G|}\sum_{g\in G}g^*\pi^*H. \tag{11}
\]
This does not replace $[M:K]$ by $|G|$. For $E/A$ its kernel is $[M:K]/|G|$ times the orbit of any lift. G331 FULL support makes every fibre exactly that orbit on ALL supports. Every $B$ fibre point lifts to $E$ by the finite injection lifting theorem. These statements follow first for ideal profiles from coefficient minima, then by dense differences on continuous functions and finite decreasing sums on $D$.

The finite orbit maximum of $\pi^*H$ is in the same $C$ or $D$ class, is fibre constant, and descends positively. Its value is exactly $\mathcal MH(v)=\max_{\rho w=v}H(w)$. Thus $\mathcal M(C_B)\subset C_A$ and $\mathcal M(D_B)\subset D_A$. Alternatively for $D$ an actual decreasing $C_B$ representation and FINITE fibres give maxima decreasing to the maximum by choosing one common index for all fibre points, using finite thresholds at bottom. If $H\le f\rho$, then $\mathcal MH\le f$ and $H\le\rho^*\mathcal MH$. Competitor suprema prove
\[
 P_B^K(f\rho)=\rho^*P_A^Kf\quad(K=C,D) \tag{12}
\]
without membership assumptions. It transfers membership when either side is in its class. For a reduced source over normal $A$, the same maximum proof works when EVERY minimal component dominates $A$: restrict to its domain quotients and take a finite maximum. All supports kill at least one minimal prime. Vertical components invalidate this argument; n3 supplies them explicitly after normalized base change.

For $n=\dim A\ge2$, bounded $H\in D_B$ and $u_2,\ldots,u_p\in D_A$, $p=n-1$, we prove
\[
 \rho_*\mu_B^{[A]}(H,\rho^*u_2,\ldots)=\mu_A(TH,u_2,\ldots). \tag{13}
\]
Let $e=[M:L]$, $D_0=[M:K]=ed$. N5 applied to $E/B$ gives
$\pi_*\mu_E^{[A]}(\pi^*H,\rho_E^*\boldsymbol u)=e\mu_B^{[A]}(H,\rho^*\boldsymbol u)$ with residue towers. Automorphisms of $E$ preserve the G345 operator: on ideal tuples this follows from quotient-length isomorphisms and transformed tests, then dense tests, uniform approximation and prescribed-limit bounded nets. They permute centres with equal residue degrees. Hence all orbit-transformed selected-slot products have the SAME pushforward to $A$. By multilinearity in ONE slot, (11) gives
\[
 \rho_{E,*}\mu_E^{[A]}(\rho_E^*TH,\rho_E^*\boldsymbol u)
 =d\,\rho_{E,*}\mu_E^{[A]}(\pi^*H,\rho_E^*\boldsymbol u).
\]
The left side is $ed\mu_A(TH,\boldsymbol u)$ by (10), the right is $de\rho_*\mu_B^{[A]}(H,\rho^*\boldsymbol u)$. Cancel $ed>0$. There is NO extra degree multiplying (13), since $T$ is unnormalized. For $p=1$ there are no remaining inputs. For $n=1$ there is no selected slot and only the zero-arity (10); $n=0$ is empty.

For any reduced finite source over normal $A$, sum traces over its dominating minimal domain quotients. N5's component decomposition for arbitrary source tuples and one-slot linearity prove (13) for this sum. Vertical components have dimension below $n$, hence zero ambient product, but remain in the spaces and descent conditions; this sum trace is not asserted full-support on vertical fibres.

The Cartier meaning can be checked without a defect assertion. At a target exceptional DVR $Z$ on a normalized primary model, its finite integral closure in $L$ is torsion-free, hence free of rank $d$. Reduction by a uniformizer gives $\sum_{Z'|Z}e_{Z'/Z}f_{Z'/Z}=d$. For integral $g$, Smith normal form makes the norm determinant order its cokernel length, which Artinian decomposition expresses as $\sum f_{Z'/Z}\operatorname{ord}_{Z'}g$. Multiplying a rational $g$ by a large uniformizer power and subtracting its finite norm order proves the same for local Cartier equations. Consequently at $\nu_Z=\operatorname{ord}_Z/b_Z$, $b_Z=\operatorname{ord}_Z\mathfrak a$,
\[
 TH(\nu_Z)=b_Z^{-1}\sum_{Z'|Z} f_{Z'/Z}\operatorname{ord}_{Z'}D_H
\]
for a source core on a common refinement. Its coefficients are proper Weil pushforward coefficients, unchanged at a dominating DVR under further birational refinements. No finite Cartier determination or arbitrary-model classification downstairs is claimed. The completed geometric potential and (13) are what is proved.


\section{n7. General reduced targets: the full conductor-admissible trace domain}
\paragraph{Supports.} G331, G345, n1, n5 and n6.
Let $R\hookrightarrow B$ be finite reduced, $S$ the finite normalization of $R$, and $C=(B\otimes_RS)_{\rm red}$. Both $S\to C$ and $B\to C$ are injections: integral surjective spectrum maps remain surjective after base change; their kernels are therefore in every prime, and reducedness kills them. This does NOT delete the vertical or lower components of $C$.

For a bounded $H\in D_B$ pull to $C$. On each normal local centre $S_i$, take the sum normal traces of its restrictions to the minimal domain components of $C_i$ that dominate $S_i$. Denote this $T_iH$. N6 proves each is a bounded positive geometric $D_{S_i}$ potential (continuous $C$ for $H\in C_B$). The finitely many generic degrees bound them. Vertical components have no invented generic degree. Define admissibility by the literal condition
\[
 (T_iH)_i\text{ is constant on EVERY full }X_S\to X_R\text{ fibre}. \tag{14}
\]
It includes the entire conductor-infinite quotient stratum, every nonminimal/lower-centre point and every normalization centre, including those contributing zero ambient measure. G331 then descends the tuple uniquely to $T_RH\in D_R$, or $C_R$ in the continuous case. Full constancy, not merely generic/divisorial compatibility, is needed.

For $n=\dim R\ge2$ and remaining bounded pulled inputs,
\[
 \rho_*\mu_B^{[R]}(H,\rho^*u_2,\ldots)
 =\mu_R(T_RH,u_2,\ldots)\quad\hbox{under (14)}. \tag{15}
\]
On each top $S_i$ use n6 for $C_i/S_i$ and multiply by the exact closed weight $[\kappa(S_i):k]$. The right-hand sum is G345 normalization of the descended tuple, hence the right side of (15). For the left, every top $B$ component lies above a top minimal $R$ prime: finiteness gives equal dimension and a nonminimal target prime would extend an $n$-chain. At this generic point $S$ is just $K_P$. Therefore $C/B$ has generic degree one on EVERY ambient top component. N5 for $C/B$ on the pulled source tuple turns its component sums into $\mu_B^{[R]}$. The two paths to $R$ have identical centre weights, since closed residue degrees multiply. All other components stay in the domain with zero ambient degree; this says nothing about mass/capacity at their identified image points. This proves (15) with a genuinely geometric source slot, not just an ideal trace.

This supplies the general one-slot identification absent from author253's manuscript, on an explicit trace-admissible domain. It is not a universal pushforward for incompatible potentials. N3 shows why full normalization compatibility cannot be dropped. A noninjective map first uses its exact-image quotient; no ambient positive extension is claimed, and n4 disproves such an assertion.


\section{n8. Reduced finite-flat determinant kernels, maxima and automatic descent}
\paragraph{Supports.} G331, G345, n1, n2, n5, n6 and n7.
Let $B$ be reduced finite locally free of positive constant rank $d$ over excellent reduced local $R$. It is free over $R$, faithfully flat and injective. Use a global semilocal boundary-power ideal $J\subset B$, choosing finite $R$-module generators $g_j$. Such ideals give dense rational profiles for the product of closed-centre classes by G331's Artinian jet gluing. Define $h=\sum T_jg_j$ and
\[
 \det(t\,1-m_h)=t^d+\sum_{i=1}^d(-1)^ic_i(T)t^{d-i},\qquad
 C_i(J)=(\text{coefficients of }c_i(T)),\quad \mathcal N_{\rm fl}(J)=C_d(J). \tag{16}
\]
For projective modules determinant means the induced scalar on the top exterior power. Local bases change matrices by conjugation, so the polynomials glue; determinants commute with arbitrary scalar extension. This is complete current Stacks 31.18.6 (0BD2), independently verified by the matrix construction. A replacement generating family effects linear substitution of variables and coefficient containment; reversing it proves independence of ALL coefficient ideals. Images of generators generate the image extended ideal after ANY base change, without claiming injectivity of the tensor of an ideal inclusion. If $J\supset\mathfrak a^NB$, redundantly add $x\cdot1_B$ for generators $x$ of $\mathfrak a^N$; pure norm coefficients are $x^d$. The norm coefficient ideal contains a primary boundary power (radical containment and Noetherianity), so is unit-or-primary. The lesser coefficient ideals need not be primary.

For any $v\in X_R$ with support $P$, use its valued field $K_v=\operatorname{Frac}(R/P)$. The $d$-dimensional algebra $F=B\otimes_RK_v$ may be NONREDUCED. Split all its residue fields in a finite normal extension $M/K_v$, and extend the valuation. After tensoring, the Artinian local factors have residue $M$ and full lengths $l_j$ with $\sum l_j=d$. Their maximal-ideal filtrations make multiplication by $h$ triangular with the residue scalar $\bar h_j=\sum T_i\bar g_{ij}$ repeated $l_j$ times. Therefore the extended characteristic polynomial is $\prod_j(t-\bar h_j)^{l_j}$. The lengths include both fibre nilpotence and inseparable splitting multiplicities.

The residue maps followed by this valuation give source points $w_j$. Integrality makes their values nonnegative; their base restriction is centred and primary gauge one, so their centres are closed above $\mathfrak m$. Polynomial Gauss minimum is multiplicative: after quotienting supports, divide by a least coefficient and reduce to nonzero residue polynomials, whose product is nonzero. Consequently
\[
 v(\mathcal N_{\rm fl}(J))=\sum_j l_jw_j(J). \tag{17}
\]
The associated positive finite measure has mass $d$. Its ideal moments and this mass determine it uniquely by the dense full semilocal gauge-difference lattice, so it is independent of field/lift choices. Every point $w$ in the restriction fibre has support corresponding to a residue field of $F$: indeed $B/Q$ is finite over $R/P$ and its quotient fraction field is that residue field. Embed it in $M$ and extend its valuation by G331's valuation lifting. The point occurs with positive length in that choice, hence in every choice by uniqueness. Thus the kernel $\eta_v^{\rm fl}$ has FULL fibre support, and fibres have at most $d$ points.

Set $\tau H(v)=\int H\,d\eta_v^{\rm fl}$. On dense continuous gauge differences (17) proves continuity; uniform approximation and mass $d$ prove it on every continuous test. On a rational potential it is $-v(\mathcal N_{\rm fl}(J))/q$, so maps $C_B$ to $C_R$ by G331 comparison. For an actual decreasing $C_B$ representation a finite sum of nonpositive terms commutes with the directed infimum: use simultaneous thresholds on the finitely many points, or any finite threshold for bottom. It produces an actual decreasing $C_R$ representation of $\tau H$, giving $D$ preservation including partial bottom. This full-support kernel is not a guessed defectless valuation-ring degree formula.

\paragraph{Direct characteristic-coefficient maximum.}
In the Gauss-valued field $M(T)$ let $m=\min_jw_j(J)$, finite because of a boundary power. Every $c_i(T)$ has Gauss value at least $im$. If all were strictly greater, substituting a root of value $m$ into its monic equation would make the leading term uniquely least-valued, impossible for a zero sum. Hence on EVERY support
\[
 \min_{\rho w=v}w(J)=\min_{1\le i\le d}v(C_i(J))/i. \tag{18}
\]
Zero coefficient ideals have value infinity. Set $L=\sup_{X_R}v(C_d(J))/d<\infty$ and choose integer $N>dL$. Then $N/i>L$ for all $i$, so replacing each coefficient ideal by the genuine ideal $C_i(J)+\mathfrak a^N$ leaves the minimum EXACTLY unchanged. Thus
\[
 \mathcal M(-w(J)/q)
 =\max_i[-v(C_i(J)+\mathfrak a^N)/(qi)]\in C_R. \tag{19}
\]
Common denominators and ideal sums make it a rational profile. The primary truncation is essential and no false coefficient-class assumption enters. Fibre maxima are 1-Lipschitz for uniform norm, so (19) extends to $C_B$. For an actual decreasing $C_B$ net the FINITE-fibre directed-threshold argument gives decreasing maxima with the exact limiting maximum, including all-bottom fibres. This is an actual $C_R$ representation, so $\mathcal M(D_B)\subset D_R$. The n6 competitor argument proves (12) for reduced finite-flat maps over arbitrary nonnormal $R$, with membership transfer if known, without arbitrary supremum closure or USC regularization.

\paragraph{Automatic full conductor admissibility and geometric trace slot.}
Base change to the normalization $S$. At every normal local $S_i$, $B_i'=B\otimes_RS_i$ is free of rank $d$. Its generic algebra is $B\otimes_RK_{P_i}$, a reduced localization of $B$. A nilpotent in $B_i'$ vanishes generically and hence is zero by torsion-freeness over the domain. Thus $B\otimes_RS$ is already reduced; no reduction loses rank. Complete Stacks 10.39.19 (00HS) gives flat going-down: localization makes a flat local map faithfully flat, which lifts a smaller target prime, so minimal source primes contract to minimal target primes. Thus there are no vertical minimal components over any $S_i$. The recursive localization/faithful-flat prime-surjectivity foundations are disclosed, not inferred from a label.

Determinant base change in (16) gives equality between the pullback of $\tau H$ to $S_i$ and the sum normal-domain traces over dominating $B_i'$ components, first on rational profiles by factoring the generic determinant into field norms, then by uniform and finite decreasing limits. This equality holds on ALL $S_i$ supports, including conductor-infinite ones. The trace tuple is therefore already the pullback of a downstairs $D$ or $C$ potential and satisfies n7's entire condition (14). Applying (15) gives
\[
 \rho_*\mu_B^{[R]}(H,\rho^*u_2,\ldots)=\mu_R(\tau H,u_2,\ldots). \tag{20}
\]
Equivalently the two normalization routes use generic degree one for $B\to B\otimes_RS$ on every source minimal component (going-down makes its target contraction minimal, where normalization changes no generic field), and exact multiplying residue weights. Lower-dimensional components remain with zero ambient degree, as in n7. This identifies the determinant trace with a geometric ONE-slot operator, not just a continuous function trace. Its normalized-primary-model coefficients are the Weil pushforward of n6; no Cartier determination is claimed.

Finite-flatness gives $d_P=d$ in n5. It does not permit the original rank of a nonreduced algebra to be used after reduction: $k[[t]][\epsilon]/(\epsilon^2)$ and its reduction have the same boundary but parameter lengths $2N$ and $N$. Genuine Cartier thickening lengths on REDUCED models remain included; generic nilpotent mass is not granted.


\section{n9. Towers, independent gauges, qualifications and original decision}
\paragraph{Supports.} G331, G345 and n1--n8.
For a finite tower $R\to B\to F$, over a top minimal $P$ write
$B\otimes_RK_P=\prod_Q L_Q$ and $h_Q=\dim_{L_Q}(F\otimes_BL_Q)$. Vector-space decomposition proves
\[
 d_P(F)=\sum_Q[L_Q:K_P]h_Q. \tag{21}
\]
Closed residue degrees multiply along closed-centre towers. These are the exact componentwise projection towers of (10), with zeros for absent components and full inseparable degrees. Constant ranks multiply; varying ranks are not replaced by a scalar.

Unnormalized traces on normal-domain towers with normal intermediate target compose on EVERY support. Choose one finite normal closure of all fields. Restrictions partition the embeddings of the largest field into intermediate embeddings and further embeddings; the purely inseparable multiplicities multiply. G331's full-support coefficient formula gives equality of the finite kernel sums, first on gauge differences and hence all continuous functions by density, then on $D$ by finite decreasing sums.

For general reduced injections, use n7 traces only under explicit intermediate admissibility: $H$ must have a full descended trace over $B$, and that result must have a full descended trace over $R$. On the normalization of each minimal $R$ component, its dominating source domain components have the indicated generic field extensions. Normalize those source components; this changes the generic field by degree one, and the normal-domain degree-one trace is exactly pullback on the whole fibre. More explicitly, if a minimal $B$ component $B/Q$ dominates $R/P$, the integral closure of $B/Q$ in its field $L_Q$ equals the integral closure of $R/P$ in $L_Q$: integrality of $B/Q$ over $R/P$ proves both containments by transitivity and the same monic equations. It contains the normalization of $R/P$ in $K_P$, and localization at its normal target centres partitions the closed source centres. Incomparability shows that any minimal $F$ component dominating $R/P$ passes through a unique minimal $B$ component over $P$; conversely each such dominating chain contributes to the composite. Thus the two intermediate normalization traces, restricted to these normal components, are the same full-support sums as their defining branch traces, with no appeal to equality merely at generic valuations. Normal field tower transitivity proves equality with the direct composite tuple on EVERY support of each normal $R$ centre. The equality also applies at lower-dimensional centres, irrespective of their zero ambient product. The iterated tuple is full-fibre constant by its assumed second admissibility; hence so is the direct tuple. Uniqueness of G331 descent gives $T_{F/R}H=T_{B/R}(T_{F/B}H)$. Direct admissibility alone does not imply either intermediate admissibility. This is not an unrestricted trace on incompatible tuples.

For reduced finite-flat towers determinant norms are transitive. On every minimal base field, decompose the finite reduced algebras into fields and use field-norm transitivity; reducedness makes this generic polynomial identity global on the base. The full-support kernels compose even at nonminimal supports: after splitting a support-field fibre, let a first Artinian factor have length $l$. Flatness identifies the successive maximal-ideal-layer quotients of the second free algebra with those of the first tensor its residue algebra. Multiplication therefore has the residue-algebra characteristic determinant repeated $l$ times. Each second residue length is multiplied by $l$, exactly the direct kernel length. Consequently all gauge moments and mass agree, density identifies kernels, and finite decreasing sums prove trace transitivity on $C,D$. Constant ranks $d,e$ give mass $de$. This is a proof of norm transitivity, not merely determinant basis independence.

Naive normalized towers fail when intermediate generic degrees vary. For EVERY characteristic let $A=k[[t]]$, $B=A\times A$, and $F=A\times k[[s]]$, mapping the second factor by $t=s^2$. These are reduced finite algebras; $[k((s)):k((t))]=2$ even in characteristic two, since Laurent exponent parity rules out $s\in k((t))$. In synchronized $t$ gauges the direct trace weights are $(1,2)$, total three. Direct average at values $(0,-1)$ is $-2/3$, while successive averages are $-1/2$. Unnormalized traces both equal $-2$. This is an exact all-characteristic algebraic example, not a finite sample claim.

Tracing several arbitrary product slots is false even flat. Let $R=k[x,y,z]_{(x,y,z)}$, $B=R\times R$ and $H=(-1,0)$, $V=(0,-1)$, genuine semilocal primary/unit profiles. Each source product of arity two has one zero input, hence is zero. But $\tau H=\tau V=-1$ and $\mu_R(-1,-1)$ has mass $e_R(\mathfrak m)=1$; normalized separate traces give mass $1/4$. Thus only ONE arbitrary slot, with the others pulled, has (13), (15), (20).

\paragraph{Exactly one gauge factor.}
For a base primary $\mathfrak b$, put $t(v)=v_{\mathfrak a}(\mathfrak b)$, $T(v)=v/t(v)$. Transport inputs by $u_{\mathfrak b}(Tv)=u_{\mathfrak a}(v)/t(v)$ and measures by
\[
 \mu_{\mathfrak b}=T_*[t\mu_{\mathfrak a}]. \tag{22}
\]
Every synchronized source lift has the same base denominator, so traces and maxima divide by it and all projections commute with (22). For an arbitrary separate source primary gauge $\mathfrak c$, let $w\in X_{B,\mathfrak c}$,
$\lambda(w)=w(\mathfrak aB)>0$ and $\rho_{\mathfrak c}(w)=w|_R/\lambda(w)$. The homogeneous pullback of $u$ is $\lambda(w)u(\rho_{\mathfrak c}w)$ and
\[
 \rho_{\mathfrak c,*}[\lambda\mu_{B,\mathfrak c}(\boldsymbol H_{\mathfrak c})]
 =\rho_{\mathfrak a,*}\mu_{B,\mathfrak aB}(\boldsymbol H_{\mathfrak a}). \tag{23}
\]
Indeed $w=w_{\mathfrak a}/w_{\mathfrak a}(\mathfrak c)$, so $\lambda=1/w_{\mathfrak a}(\mathfrak c)$ cancels the ONE G345 measure weight. In a trace slot the synchronized potential is $H_{\mathfrak a}(w/\lambda)=H_{\mathfrak c}(w)/\lambda$; therefore its trace is computed with $H_{\mathfrak c}/\lambda$, not with an unscaled slot. The other pulled slots satisfy the same homogeneous conversion, and (20) with (23) gives the exact independently gauged one-slot formula. There is no factor $\lambda^{n-1}$. Raw envelope competitors transport by the same order bijection, hence their suprema and both counterexample gaps transport. Successive gauge factors obey the intrinsic cocycle. Nonprimary ideals only have their positive-finite partial domains; no compact all-boundary theorem is asserted there.

\paragraph{Source correction retained.}
Literal SH17.4.7 prints the correction $\ell((x_1,\ldots,x_{d-1})M:_Mx_d)$ without quotienting the previous parameters. The finite correct term is
\[
 \ell(0:_{M/(x_1,\ldots,x_{d-1})M}x_d)
 =\ell\left(((x_1,\ldots,x_{d-1})M:_Mx_d)/(x_1,\ldots,x_{d-1})M\right).
\]
It follows by repeated complete 17.4.6 in the CURRENT quotient. The printed term can have infinite length. The exact PDF page 370, printed 356, was freshly rendered and viewed; the manuscript uses no new application of the false corollary. The grant qualification remains literal. All new source applications and their recursive-background boundaries are in the ledger and reproduced in this paper. No new Keeler/BFJ/Izumi application is inferred from old reading receipts.

\paragraph{Whole-proof versus whole-original decision.}
The author253 scoped proof is mathematically retained at its precise hypotheses; no counterexample to its stated positive results was found in this reconstruction. Its explicit $\texttt{candidate=false}$ history remains unchanged. The new manuscript adds n7's full conductor-admissible slot theorem, ALL of n4's quotient obstruction and the fully sourced determinant/going-down and tower/gauge qualifications. These are substantive additions, not a byte-identical republication. Source-body reading, duplicate matching, finite diagnostics and manuscript checks are separately reported; compilation is reserved to ROOT.

The exact P12.6 operator question is: for the independently geometric $C,D$ and bounded G345 product, which finite pullbacks, positive descents, envelope comparisons and trace-slot/projection laws survive on the FULL boundary, including normalization/conductor identifications? N1, n5--n8 answer the cone and bounded-product parts, and n2--n4,n6,n8 give universal corrected raw-envelope laws, sharp positive special hypotheses and unconditional no-go results. N7 supplies author253's remaining intended conductor-admissible one-slot identification. N4 resolves its proposed ambient extension issue NEGATIVELY. Arbitrary incompatible traces cannot descend universally; n3's normalization has branch traces $(-1,-2)$ at an identified fibre, already disproving that assertion.

Family 6.2 separates P12.3 existence/regularity from P12.6 compatibility, and 6.3 says construct when possible. We therefore DO NOT make solving all P12.3 or P12.5 a prerequisite for these finite-map theorems. Nor does one false strengthened normalization identity alone close the original. The precise residual issue is identification and compatibility of a SPECIFIED positive/regularized independently geometric envelope operator, beyond the raw competitor supremum and its conditional positivity transfer, in the remaining nonnormal/nonflat and closed-image settings. The grants select no such operator. A USC-regularized envelope, if intended, needs a justified regularization and a proof or obstruction for its pullback/descent; a finite quotient map need not transport neighborhood suprema as an open map. Our raw identities give no such theorem. The quotient counterexample is a genuine impossibility even when raw envelopes are positive at both ends, so that part is not an existence gap and is not listed as an unresolved extension theorem.

Accordingly the whole scoped mathematical proof verdict is PASS WITH THE STATED PUBLISHED-BACKGROUND AND SCOPE QUALIFICATIONS (a draft review judgment, not formal verification). The whole-original completion verdict is INCONCLUSIVE, $\texttt{candidate=false}$: no exact residual positive/regularized envelope calculus or complete negative classification of that remaining operator is proved. This is a narrower residual than author253's broad request for all envelope existence and arbitrary incompatible operator extension. All nilpotent-generic, unbounded-energy, arbitrary-model, plurifine and literal radial theories remain outside the grants; they are not silently counted as new P12.6 obligations. Smooth specialization remains exactly CLOSED affine algclosed characteristic zero BFJ plus DVR/empty cases. No catalogue or external acceptance is performed.


# Whole source-application and reading boundary

The only correctness grants are the ENTIRE qualified G331 and G345 received in the task, with their complete papers, annotations, source ledgers, scopes, G345 independent qualification ledger, acceptance metadata as history, and literal reader repair history. Their complete bodies and mandatory qualifications were read as supplied. The fourteen bound component copies are unchanged in attachments/. Nested repeated grant bodies are duplicates, not fresh independent source readings. No operator theorem is imported from G331; no arbitrary finite-map or envelope/energy theorem is imported from G345. The old published-history claims inside those grants remain qualifications, not claims that this reviewer freshly reread every historical source.

All author253/ROOT348/349/351 prose and book material are DATA. None appears in support lists. The entire original-task.json and ENTIRE family were read before scope selection. The entire 53,282-byte author253 proof.tex was displayed in sequential complete chunks. The complete 17,107-byte ROOT348, 23,720-byte ROOT349 and 11,247-byte ROOT351 were read. All seven actual FINAL notes, every summary/detailedSummary/text/support field, were read. For expanded n1--n6, complete proof bodies are exact contiguous substrings of the proof already read; metadata and every extra footer were separately read. Expanded n7, including its extra observation paragraph, was read completely. This is a complete content reading, not a second fresh reading of identical bytes. Evidence/expanded-field-comparison.json records which bodies repeat. The full author ledger, scope, coverage, original decision, acceptance and mandatory annotation were read. The 344,405-byte typeset paper contains the whole proof and fourteen whole component bodies; its header and all remaining bridge/appendix prose were separately displayed after those exact bodies were removed for comparison. That identity check establishes duplicate structure, not proof or an independent reading of every repeated byte.

The two small book packets and entire finite-transfer/conductor book fragment were read as context; every new mathematical consequence here is proved with the two grants and explicit background. The 96,986-byte chapter-70 file was integrity checked only; no fresh whole-chapter reading is claimed and no unused chapter result is a premise. No native254 mathematics was inspected and no feedback sent. No supplied script was executed/imported.

## Fresh complete immediate primary units

| Current bound source actually read | Application in this manuscript | Hypotheses and recursive boundary |
|---|---|---|
| Stacks 0BD2, complete current Lemma31.18.6 statement and proof, from whole small bound text | n8 projective-module determinant norm, basis independence and arbitrary base change | Positive finite locally free rank. The proof is the determinant construction and fibre vanishing; our coefficient-family and full-kernel extensions are proved separately. No old numbering substituted. |
| Stacks 00HS, complete Lemma10.39.19 statement and proof, from whole small bound text | n8 flat going-down, no vertical minimal components after normalization base change | Flat ring maps; localization is flat, a local flat map is faithfully flat, and faithfully flat maps lift primes. Those recursive elementary source units are disclosed background, not freshly all reread. |
| Current July2024 author Swanson--Huneke PDF/text: complete17.1.6 statement/sketch; complete17.4.1 setup,17.4.2 statement/proof,17.4.3 convention,17.4.4 statement/proof | n5 multigraded Artin--Rees, finite-module length forms and prime filtration | Noetherian local R, finite modules, proper primary labels. Degree is ambient dim R; lower-dimensional modules give zero. n5 independently proves homogeneous generation, squeeze on all positive rational rays and exact-sequence additivity. Source Hilbert/superficial/one-variable foundations are disclosed ordinary published background. |
| Same source complete17.4.6 and17.4.7 including its whole proof | n9 mandatory literal correction, no new application of the false printed term | Finite annihilator is in the CURRENT quotient, equivalently colon modulo previous parameters. Fresh PDF page370 (printed356) was rendered and viewed and confirms the literal omission. G345 qualification unchanged. |
| Stacks0AYA complete42.26.1--4 statements/proofs, especially whole42.26.3 | n5 GENERAL-degree actual divisor-cycle projection, before Chow equivalence | Proper dominant integral maps, equal delta-dimension, full finite field degree. The immediate proof uses42.18.1 norm/divisor and Nm(g)=g^degree. That recursive norm/divisor foundation is disclosed published background, not freshly fully read. Inseparability is retained; degree one is not substituted. |
| Stacks02QL entire Situation42.7.1 | n5 excellent universally catenary base dimension function | Delta(p)=dim R/p on the local base and residue transcendence-degree extension on finite-type models. Catenary dimension theory is ordinary background; nonpure components are handled at ambient degree. |
| Stacks0BEL entire33.45.1--13 statements/proofs | n1 curve degrees; n5 numerical projection33.45.7, numerical residue weights and supported leading terms | Proper schemes over a FIELD. Cartier thickenings in mixed characteristic use G345's m-filtration before field lemmas. Every generic length and closed residue-field dimension is retained. Proper coherent cohomology, projection formula and generic dimension theory inside the immediate proof are recursive ordinary background. |
| Stacks01OF complete31.33.1--9 immediate statements/proofs, with the source's31.33.10--14 context also displayed | n1 actual primary blowup, regular image ideal, reducedness, universal property; finite source Rees quotient | Actual reduced Noetherian germs. Our graded surjection proves CLOSED embedding under arbitrary finite maps. The source's31.33.3 base-change EQUALITY requires flatness. The initially truncated31.33.1--3 display was completely repaired separately. No arbitrary-model cofinality is inferred. |

The fresh source forms are the exact bound local text derivatives; matching HTML/PDF bytes is reproducibility. Only one new primary PDF page was visually read. No whole-PDF, fresh BFJ/Keeler/Izumi, or recursive whole EGA/Hironaka/Rees reading is claimed. Primary bodies and pixels stay LOCALONLY; they are not reproduced in the new public-facing proof files. The recorded pdftoppm command is in evidence/source-rendering.md.

## Independently reconstructed content and author differences

N1 actual finite PRIMARY geometry and all-support pullback. N2 full-fibre competitor bijection and positivity transfer without sup membership. N3 universal conductor-infinite exact gap one. N4 entire new351 positive-at-both-ends quotient counterexample, nonextension, non-USC limit, gauge and arity. N5 independently geometric varying-degree projection BEFORE module form comparison, then full coefficient and prescribed-limit net proof. N6 full-orbit normal maxima and unnormalized one-slot operator identity with inseparability. N7 new349's general FULL conductor-admissible one-slot theorem. N8 projective determinant family/base-change kernels with Artinian lengths, direct characteristic coefficient maxima with exact primary truncation, and automatic full admissibility. N9 trace/projection towers, normalized-degree and nonlinear counterexamples, independent source gauges, mandatory quotient correction and impartial original-scope decision.

The new paper adds n4 and n7, which are absent from author253's proof. It supplies explicit new0BD2/00HS applications missing from the author253 ledger and the independent-gauge/tower details. It narrows the author's broad remaining obligations: quotient extension and incompatible universal trace have negative answers, and conductor-admissible slot identification has a positive theorem. No mathematical change to the immutable author packet is made. No genuine error in the retained scoped author253 positive statements was found; the verdict is not inherited from its labels.

Ordinary additional foundations used are excellence of polynomial localizations/finite normalization, normal local DVRs, lying-over/incomparability and finite dimension theory, Noetherian prime filtrations, primary powers/CRT jet gluing as in G331, elementary real valuation extension from G331, algebraic normal closures and embeddings, Artinian filtrations, Smith normal form, tensor-flat exactness, compact-Hausdorff Riesz/density and actual directed-net threshold arguments. Each new use is proved or its exact published scope disclosed. No singular multiplier, envelope regularity, energy, arbitrary-model cofinality or nilpotent-generic mass is a hidden premise.

Rerun own programs only: python audit_inputs.py; python bounded_checks.py; python build_delivery.py; python final_audit.py. All 74 bound files matched current size/hash. Arithmetic 2201 cases had zero failures. These are observations, not verification of universal proofs. Compilation is reserved to ROOT. No heavy supervised facility was exposed; no resource-heavy computation was launched or needed.


# Exact theorem scope

Excellent local germs through reduction; arbitrary characteristic and residue field; FULL centered real semivaluation sections in any proper primary gauge. Every support remains, including conductor-infinite and lower-dimensional centres. Dimension zero is empty. Models are directed actual PRIMARY blowups and auxiliary finite normalizations, with actual negative-effective finite real Cartier presentations and all contracted-curve degrees. No arbitrary-proper-model cofinality or nonnormal Weil substitute.

C and actual decreasing-net D are the independently geometric qualified G331 classes. Finite pullback is checked geometrically on the actual source blowup CLOSED in base change. Every reduced finite INJECTION has exact positive full-fibre descent for C/D. Noninjections factor over the exact quotient image; positive ambient extension is false by n4, even for an injective boundary map.

Envelope notation is RAW competitor supremum for K=C or D and bounded finite obstacles. Universal constrained full-fibre equality, unrestricted inequality and conditional positivity transfer hold. Unrestricted equality holds for normal-domain finite extensions, normal targets with all source minimal components dominant, and reduced finite-flat maps. General normalization equality is false with exact conductor-infinite gap one (n3). Closed quotient restriction equality is false with positive continuous envelopes at both ends over every field (n4). No automatic USC regularization or arbitrary supremum class membership.

Products are G345 bounded D operators of arity dim R-1, with ordinary OPEN locality and uniform weak / bounded decreasing NET continuity for prescribed D limits. Ambient finite projection has varying generic field sums d_P, including inseparability and zero for absent components, and exact closed residue weights f_q. Lower components contribute zero ambient degree while retaining points. Curve intrinsic zero arity and lower-image different arity are distinguished. No generic nilpotent mass.

Exactly ONE arbitrary source potential slot has unnormalized trace projection, with other slots pulled, over normal domains and on the FULL conductor-admissible domain for general reduced injections. Branch trace sums use only generic dominating components but require constancy on EVERY normalization fibre, including infinite conductor/lower centres. Reduced finite-flat determinant traces are automatically admissible. Full-support Artinian lengths are retained at nonminimal support fibres. Multiple independently traced slots are generally false.

Unnormalized traces compose under explicit intermediate admissibility; reduced finite-flat determinant towers compose automatically. Projection towers use sums of full field-degree products and multiplying closed residue degrees. Normalized averages fail for varying intermediate component degrees. Potentials transform homogeneously; measures have exactly ONE primary factor, including separate source gauges and the precise rescaling of the trace slot. Nonprimary gauges only have partial domains.

Smooth specialization is exactly qualified BFJ CLOSED affine smooth germs over an algebraically closed characteristic-zero field, dimension>=2, plus direct DVR/empty cases. No fresh singular/positive-characteristic multiplier or resolution transfer. The literal mixed-zero classical/CLD radial obstruction remains. Energy, unbounded products, plurifine locality and arbitrary-model theories remain separate.

Whole scoped mathematical reconstruction: PASS with published-background/source qualifications, unverified draft. Whole exact original completion: INCONCLUSIVE, candidate=false, solely because a specified positive/regularized envelope operator's residual finite-map calculus is not identified beyond the proved raw/conditional/no-go package. This does not automatically require solving all P12.3. Neither grants nor counterexamples select the missing operator or prove all its required rules.
