# Completion invariance and a formal Frobenius lifting mechanism

Unverified mathematical draft, 9 October 2026. The original P12.3 is unchanged and is not declared solved. This paper proves completion invariance for the independently geometric **completed** cones in the entire qualified G331 grant, gives a complete compact-Hausdorff Jensen argument, and proves a formal trace-discriminant lifting theorem. It does not assume the native271/386 verdict as a theorem. All supplied programs remain inert data.

## 1. Full semivaluations under completion

Let $(R,\mathfrak m)$ be a Noetherian local ring, $\widehat R$ its $\mathfrak m$-adic completion, and $\mathfrak a$ a proper $\mathfrak m$-primary ideal. Semivaluations have values in $[0,\infty]$, are nonnegative on the ring, and have $0<v(\mathfrak m)<\infty$. No restriction on their prime support is made. Write $X_R=\{v:v(\mathfrak a)=1\}$. Choose $r$ with $\mathfrak m^r\subset\mathfrak a$; then $d=v(\mathfrak m)\ge 1/r$ on $X_R$.

For $v$ set $|f|_v=\exp(-v(f))$, with $\exp(-\infty)=0$. This is a multiplicative nonarchimedean seminorm with values in $[0,1]$. If $F\in\widehat R$, choose compatible representatives $f_N\in R$ modulo $\widehat{\mathfrak m}^N$. For $M\ge N$ their difference belongs to $\mathfrak m^N$: this uses the standard exact completion quotient $R/\mathfrak m^N\simeq\widehat R/\widehat{\mathfrak m}^N$. Thus
\[
 |f_M-f_N|_v\le e^{-Nd},\qquad
 \big||f_M|_v-|f_N|_v\big|\le e^{-Nd}.
\]
The second assertion follows directly from the ultrametric inequality: if the two norms differ, their larger value is at most the norm of their difference. Define $|F|_{\widehat v}=\lim_N|f_N|_v$. The limit is independent of representatives, and
\[
 \big||F|_{\widehat v}-|f_N|_v\big|\le e^{-Nd}\le e^{-N/r}. \tag{1}
\]
Representatives for $F+G$ and $FG$ can be chosen as sums and products of representatives. Taking real limits proves the ultrametric inequality and multiplicativity; $|0|=0$ and $|1|=1$. Define $\widehat v(F)=-\log|F|_{\widehat v}$, retaining the value infinity when the norm is zero. In particular this constructs, rather than removes, all infinite values and all nonzero supports. Units of $\widehat R$ have unit representatives and value zero. The same finite generators of $\mathfrak m$ show $\widehat v(\widehat{\mathfrak m})=d$, and similarly $\widehat v(\mathfrak a\widehat R)=1$.

Conversely every normalized centred semivaluation on $\widehat R$ satisfies (1), since $F-f_N\in\widehat{\mathfrak m}^N$. Its restriction has the same primary normalization and uniquely determines it. Restriction is therefore a bijection. Each completed norm evaluation is a uniform limit, on $X_R$, of continuous jet norm evaluations by (1). The map $t\mapsto e^{-t}$ identifies the compact extended interval $[0,\infty]$ with $[0,1]$. Hence every completed valuation evaluation is continuous in the extended-value topology. Both restriction and extension are continuous in the pointwise topologies, proving
\[
 E:X_R\overset\sim\longrightarrow X_{\widehat R} \tag{2}
\]
is a homeomorphism. No separability, normality, excellence, coefficient field, or metric on the link has entered this proof. Empty links cause no exception.

## 2. Exact primary descent and the geometric comparison gate

Every $\widehat{\mathfrak m}$-primary ideal $J$ contains $\widehat{\mathfrak m}^N$ for some $N$. Choose finite generators $F_1,\ldots,F_s$ and jets $f_i\in R$ modulo that power. Since $F_i-f_i\in J$, each $f_i$ belongs to $I=J\cap R$. Together with $\mathfrak m^N$, these elements generate an ideal $I'$ of $R$ satisfying $I'\widehat R=J$. Faithful flatness of completion gives $I'\widehat R\cap R=I'$, so $I'=I$. Thus $J=I\widehat R$. Conversely a primary ideal of $R$ extends to a primary ideal, as its finite-length quotient completes to itself, and contracts exactly. Units correspond too. The proof uses only primary ideals, and makes no assertion of descent for arbitrary ideals.

For every such ideal, $\widehat v(I\widehat R)=v(I)$, because its finite generators are in $R$ and all coefficients upstairs have nonnegative value. Consequently (2) identifies, exactly, every unit-or-primary profile, every finite nonnegative real combination of negative profiles, and their finite continuous uniform closures.

Now assume $R$ is excellent. Reduction commutes with completion: the completed reduction is reduced by the geometrically regular formal-fibre property, and the extended nilradical is nilpotent. Complete Noetherian local rings are excellent; completion of an excellent normal local ring is normal, using its normal formal fibres. These are ordinary completion/excellence facts at precisely these hypotheses, not conclusions about arbitrary nonexcellent rings. Alternatively restrict throughout to an excellent reduced $R$ whose completion is excellent reduced; the elementary conclusions of Sections 1--2 do not need these permanence facts.

The full G331 theorem applies **separately** to $R_{\mathrm{red}}$ and $\widehat R_{\mathrm{red}}$. On each it defines actual negative effective real Cartier presentations on actual primary blowups, tests their degrees on every contracted integral proper curve, and proves
\[
 C_{\mathrm{geom}}=\overline{Q_{\mathrm{primary}}}^{\|\cdot\|_\infty},
 \qquad D_{\mathrm{geom}}=\{\inf_i h_i:h_i\in C_{\mathrm{geom}},\ h_i\downarrow\}.
\]
The preceding exact profile transport therefore proves
\[
 E^*C_{\mathrm{geom},\widehat R}=C_{\mathrm{geom},R},\qquad
 E^*D_{\mathrm{geom},\widehat R}=D_{\mathrm{geom},R}. \tag{3}
\]
For the second equality transport the actual directed set and every term of each decreasing representation in both directions. There is no nested-net flattening, arbitrary infimum closure, or increasing completion step. Equation (3) is geometric positivity transport **because** of the independent G331 comparison on both rings. The topological primary statement alone would not prove it.

This proves equality of the completed geometric cones. It does not assert that their raw Cartier cores, their Cartier divisor groups, or their whole model categories are equivalent. No completed exceptional Cartier divisor has been assumed to descend. For context only, $\operatorname{Bl}_I(R)\times_R\widehat R=\operatorname{Bl}_{I\widehat R}(\widehat R)$ follows from flatness and the raw Rees algebra. Its full closed fibre is unchanged. Pulling back actual effective Cartier presentations preserves regular equations and their fibre-curve degrees. This supplies a direct core inclusion, but the reverse completed-cone equality in (3) comes from the proved comparison. Normality of arbitrary base-changed normal models and cofinal resolution are not needed by this route.

## 3. Envelopes, gauges, Jensen measures, and conductor after completion

For **any** function $f$ on $X_R$, including signed continuous, upper semicontinuous, and extended obstacles, form the raw supremum over $D$ minorants, with the empty-supremum convention $-\infty$. Transport of (3) gives the pointwise equality
\[
 E^*p_{\widehat R}(f\circ E^{-1})=p_R(f). \tag{4}
\]
The same equality holds for raw $C$ suprema. Homeomorphisms preserve both semicontinuous regularizations, continuity, and the existence of a greatest or maximal positive minorant. Thus (4) transfers their **existence and properties**, and does not assume these properties universally exist. In particular the continuous-envelope property CE is equivalent for $R$ and $\widehat R$.

All primary gauges descend by Section 2. For a second primary ideal $\mathfrak b$, the common ray formula is $v\mapsto v/v(\mathfrak b)$ and $u_{\mathfrak b}(v/v(\mathfrak b))=u_{\mathfrak a}(v)/v(\mathfrak b)$. The denominator is finite positive continuous with a bounded inverse. Completion preserves it exactly, so (2)--(4) commute with this cocycle.

For completeness, normalization/conductor also commute at the level needed here. Let $R$ be excellent reduced and $S$ its finite normalization, with local centres $q$ over $\mathfrak m$. There is a regular conductor element $c$; $S_c=R_c$. The finite algebra $S\otimes_R\widehat R$ is the product of the completed $S_q$: the $\mathfrak mS$-adic and the Jacobson-radical-adic topologies are equivalent in a finite semilocal algebra, and the completed Artinian decompositions give this product. Each $S_q$ is excellent normal, so each completion is normal. Flatness keeps $c$ regular, and after inverting it the product algebra agrees with $\widehat R_c$. It is consequently finite, normal, and birational over the reduced $\widehat R$, and is its normalization. This proves the assertion without a smooth-model base change claim.

The conductor is $\operatorname{Ann}_R(S/R)$. Annihilators of a finite module commute with this flat base change: choose finitely many generators, express the annihilator as the kernel of the map $R\to M^{\oplus s}$, $a\mapsto(am_1,\ldots,am_s)$, and use exact flat tensoring. Therefore $\widehat{\mathfrak c}=\mathfrak c\widehat R$. The semilocal version of Section 1 identifies the normalization links and commutes with restriction. The finite-value conductor singleton stratum and the infinity-value quotient-fibre stratum are preserved, including their full nonminimal supports. G331's full-fibre-constant $C,D$ descent then agrees across completion. No conductor value has been divided to obtain a uniform error.

If $J_x(C)$ denotes the subprobability Jensen set of Section 4, then pushforward by $E$ gives exactly $J_{E(x)}(C_{\widehat R})$. Indeed both the mass condition and every Jensen inequality transport through (3). Pushforward is a homeomorphism in the weak topology because continuous tests transport through a homeomorphism. Closed graph, upper and lower hemicontinuity, and the exact dual formula all transfer. This reduces the arbitrary excellent completion problem to the corresponding complete ring; it does not turn a complete ring into an algebraic germ of finite type over a field.

## 4. Complete Jensen theorem on compact Hausdorff spaces

Let $X$ be nonempty compact Hausdorff and $C\subset C(X,\mathbb R)$ a norm-closed convex cone of nonpositive functions, containing every negative constant and stable under finite maxima. Define $p_C(f)=\sup\{h\in C:h\le f\}$ for $f\in C(X,\mathbb R)$. A sufficiently negative constant is a competitor; hence $p_C(f)$ is finite bounded. It is lower semicontinuous. Negative shifting gives $\|p_C(f)-p_C(g)\|_\infty\le\|f-g\|_\infty$. If $D$ consists of actual decreasing $C$-nets, compact directed strict covers show its raw envelope agrees with this one: for $h_i\downarrow h\le f$, some $h_i<f+\varepsilon$ on all of $X$, and $h_i-\varepsilon\in C$ is a minorant. This is valid for nonmetrizable $X$ and arbitrary nets.

Put
\[
 J_x=\{\mu\ge0:\mu(X)\le1,\ h(x)\le\int h\,d\mu\ (h\in C)\}.
\]
Positive functionals and Radon measures are identified by the compact-Hausdorff Riesz theorem. The positive subprobability dual ball is weak-* compact; the inequalities make $J_x$ closed convex, and $\delta_x\in J_x$. The joint graph is closed since every $h$ is continuous. Its ambient product is compact, so this graph gives upper hemicontinuity: a contrary net of measures outside an open neighbourhood of $J_x$ has a converging subnet in that closed complement, contradicting the graph. This does not give lower hemicontinuity.

We prove the exact formula, including its signs:
\[
 p_C(f)(x)=\min_{\mu\in J_x}\int f\,d\mu. \tag{5}
\]
Consider the convex cone $W=\{(g,t):\exists h\in C,\ h\le g,\ t\le h(x)\}$ in $C(X)\times\mathbb R$. If $t>p_C(f)(x)$, the Lipschitz estimate places $(f,t)$ outside the norm closure of $W$. Hahn--Banach separation of a point from a closed convex cone supplies a continuous linear form $L(g,t)=\mu(g)-\alpha t$ nonnegative on $W$ and negative at $(f,t)$. Pairs $(r,-s)$ with $r\ge0,s\ge0$ belong to $W$, so $\mu$ is positive and $\alpha\ge0$. If $\alpha=0$, pairs $(-a,-a)$ force $-a\mu(X)\ge0$; positivity forces $\mu=0$, contradicting strict separation. Thus $\alpha>0$. Divide by $\alpha$. The same negative-constant pairs give $\mu(X)\le1$, and pairs $(h,h(x))$ give all Jensen inequalities. Separation gives $\int f\,d\mu<t$. Conversely each Jensen measure satisfies $h(x)\le\int h\,d\mu\le\int f\,d\mu$ for all competitors. Letting $t\downarrow p_C(f)(x)$ proves (5), with attainment by compactness. The mass bound is at most one, not necessarily one. In the cone of all nonpositive functions the zero measure is allowed and ensures the zero envelope of a positive obstacle; $\delta_x$ gives a negative obstacle at $x$.

There is the exact equivalence
\[
 \text{CE for all continuous signed }f
 \quad\Longleftrightarrow\quad x\mapsto J_x\text{ is weak lower hemicontinuous}. \tag{6}
\]
If lower hemicontinuity holds, a weak neighbourhood of a minimizing measure where $\int f$ is less than $p_C(f)(x)+\varepsilon$ meets every nearby fibre. This proves upper semicontinuity of $p_C(f)$, while its raw supremum already gives lower semicontinuity.

Conversely suppose CE holds and lower hemicontinuity fails at $x$. There is $\mu_0\in J_x$ and a weak neighbourhood $U$ of it missed by fibres along a net $x_i\to x$. Choose finitely many continuous tests $f_1,\ldots,f_s$ and a Euclidean ball of radius $\varepsilon>0$ around $y_0=(\int f_j\,d\mu_0)_j$ whose inverse image is contained in $U$. The compact convex projections $K_i=(\int f_j\,dJ_{x_i})_j$ avoid this ball. A closest point $z_i$ to $y_0$ exists, and the elementary squared-distance derivative at the minimizer gives, for $a_i=(z_i-y_0)/\|z_i-y_0\|$,
\[
 a_i\cdot(y-y_0)\ge\varepsilon\quad(y\in K_i).
\]
Take a subnet with $a_i\to a$ in the finite-dimensional unit sphere. All projected points are uniformly bounded, since the measures have mass at most one. Therefore for $f=\sum a_j f_j$ and all sufficiently late indices, every $\mu\in J_{x_i}$ satisfies $\int f\,d\mu\ge\int f\,d\mu_0+\varepsilon/2$. Formula (5) then contradicts continuity at $x$, since $p_C(f)(x)\le\int f\,d\mu_0$. This uses a subnet, not a sequential compactness assumption on $X$ or on its measure space.

When $p_C(f)$ is continuous it belongs to $C$: local continuous competitors approximating it from below have a finite subcover, and their maximum is a uniform approximant in $C$. It belongs to $D$ iff it is continuous, because $D$ is upper semicontinuous and the raw supremum is lower semicontinuous. A maximal $D$ minorant is greatest by taking maxima with arbitrary minorants; it equals the raw supremum. These equivalences show exactly what (6) still needs to prove for the general geometric cone.

## 5. Normal uniform negativity and what it does not settle

Use precisely G331's normal-domain inequality: for each normalized centred divisorial $\nu$ there is $A_\nu>0$, independent of $g\in C$ and $v\in X$, such that $g(\nu)\ge A_\nu g(v)$. Its source qualifications, nonunit treatment and all-support density are part of the entire grant. If $f\ge0$, zero is a competitor and $p_C(f)=0$. Otherwise $f<0$ on a nonempty open set; divisorial density gives $\nu$ with $f(\nu)<0$. Every competitor satisfies
\[
 g(v)\le g(\nu)/A_\nu\le f(\nu)/A_\nu<0.
\]
Taking the supremum proves $p_C(f)$ is uniformly strictly negative. This does not make it upper semicontinuous and does not prove (6). In particular a mixed-zero nonnormal profile or an increasing energy spike is not a normal continuous-obstacle counterexample. Sections 1--3 transport this exact dichotomy, rather than enlarge it, to excellent normal completions.

## 6. Formal roots and a trace-discriminant multiplier

Let $k$ be perfect of characteristic $p>0$, $A=k[[x_1,\ldots,x_d]]$, and $q=p^e$. Grouping exponents modulo $q$, with coefficient $q$th roots in $k$, proves uniquely
\[
 A^{1/q}=\bigoplus_{0\le\alpha_i<q} A\,x^{\alpha/q}. \tag{7}
\]
Indeed a series root is $\sum_\alpha x^{\alpha/q}\sum_\beta a_{q\beta+\alpha}^{1/q}x^\beta$; disjoint exponent classes give uniqueness. These are finite sums of formal series, so no unsupported interchange of infinite sums is involved. Rooting a finite $A$-module generating list for $R$ also makes $R^{1/q}$ finite over $A^{1/q}$ and hence finite over $R$. This proves actual Frobenius finiteness at the displayed hypotheses, not a Jacobian multiplier theorem.

Now let $R$ be a complete normal domain finite over $A$, with $L=\operatorname{Frac}R$ finite separable over $K=\operatorname{Frac}A$. Choose a $K$-basis $e_1,\ldots,e_n$ of $L$ with $e_i\in R$. Let $G=(\operatorname{Tr}_{L/K}(e_i e_j))$ and $\Delta=\det G$. The entries belong to $A$: they are in $K$ and integral over $A$, which is normal. The separable trace pairing is nonsingular, so $0\ne\Delta\in A$. This follows, for instance, after extending to a splitting field, where the embedding matrix gives the ordinary nonsingular separable trace form; no nonzero value of $\operatorname{Tr}(1)$ is assumed.

Purely inseparable $K^{1/q}/K$ is linearly disjoint from the separable extension $L/K$. Hence $L\otimes_K K^{1/q}\simeq L^{1/q}$ and the same $e_i$ remain a basis over $K^{1/q}$. For $z\in R^{1/q}$, each trace $\operatorname{Tr}_{L^{1/q}/K^{1/q}}(ze_j)$ is integral over $A^{1/q}$ and in $K^{1/q}$, hence belongs to the normal $A^{1/q}$. Solving the linear trace equations with the adjugate matrix gives
\[
 \Delta R^{1/q}\subset\sum_i A^{1/q}e_i\subset A^{1/q}[R]. \tag{8}
\]
Crucially $\Delta$ is independent of $q$. The multiplication map $P=A^{1/q}\otimes_A R\to L^{1/q}$ is injective: $A^{1/q}$ is finite free over $A$, $R$ is torsion-free over $A$, and its generic map is the preceding field isomorphism. Its image is $A^{1/q}[R]$. By (7), $P$ is a finite free **$R$-module** even if $R$ is not free over $A$ and is not Cohen--Macaulay.

For any $R$-linear map $\varphi:T=R^{1/q}\to R$, (8) gives an $R$-linear $T\to P$, $z\mapsto\Delta z$. Let $B=R\otimes_k T$ and $S=R\otimes_k R$. The module $P\otimes_k T$ is finite free over $B$. Multiplication $B\to T$ is a surjective $B$-linear map, with $T$ given its multiplication action. Thus multiplication $P\otimes_k T\to T$ lifts, by the elementary free-module lifting property, to a $B$-linear map $\Psi:P\otimes_k T\to B$. Compose
\[
 T\otimes_k T\xrightarrow{\Delta\otimes1}P\otimes_k T
 \xrightarrow\Psi R\otimes_k T
 \xrightarrow{1\otimes\varphi}R\otimes_k R. \tag{9}
\]
Every arrow is $S$-linear and its diagonal restriction is $z\mapsto\varphi(\Delta z)=\Delta\varphi(z)$. This proves a full compatible diagonal lift of $\Delta\varphi$, for every $e$. In the $F_*^eR$ notation the source precomposition is multiplication by $\Delta^q$, since $F_*r\leftrightarrow r^{1/q}$; it is not multiplication by $\Delta$. This distinction prevents an invalid Frobenius scalar manipulation.

For the following completed-diagonal assertion additionally assume that $k$ maps isomorphically to the residue field of $R$, as in the intended coefficient-field setting. A finite set of maximal-ideal generators gives a presentation $R=k[[u]]/I$: successive homogeneous corrections represent every element modulo each maximal-ideal power, and completeness takes their series limit. The same construction is continuous for the $(\mathfrak m\otimes1,1\otimes\mathfrak m)$ topology and extends to completed tensor products: each map is $S$-linear and hence sends the $N$th adic submodule into the $N$th one. The completion of $S$ is the Noetherian ring $k[[u,v]]/(I(u),I(v))$. Grouping exponents in the two variable blocks, and then quotienting by the roots of the two defining ideals, identifies its root module with the completed tensor product of the two root modules. The original and root-adic topologies are cofinal, since taking a $q$th power multiplies each monomial degree by $q$. Multiplication and all maps in (9) extend uniquely, and the commuting diagonal identity persists on the dense algebraic tensor submodules. More explicitly the kernel of root multiplication is carried into the kernel of ordinary multiplication; this is compatibility with the full root of the diagonal ideal, not just its ordinary extended ideal. This conclusion does not rely on Noetherianity of the uncompleted $R\otimes_kR$, or on exactness of completion over that possibly non-Noetherian ring. The free lift itself can equivalently be made over $\widehat B$: complete the finite free module $P\otimes T$ and lift its finite basis along $\widehat B\to T$.

## 7. The remaining formal source gate

Equation (8) is a new complete-ring multiplier theorem under an actual finite **generically separable** normalization. Cohen normalization over a coefficient field alone is not asserted to be generically separable. No polynomial HH02 theorem was applied to a power-series algebra. Moreover $\Delta$ can vanish on a height-one locus even when $R$ is regular. For $R=k[[t,y_2,\ldots,y_d]]$, $A=k[[t^n,y_2,\ldots,y_d]]$ with $n>1$ prime to $p$, the trace basis $1,t,\ldots,t^{n-1}$ has discriminant a unit times $(t^n)^{n-1}$; the finite map ramifies on $t=0$. A normalized semivaluation can kill $t$ while another parameter supplies the primary normalization, giving $v(\Delta)=\infty$. Thus one cannot obtain the required uniform all-support primary bound from this single multiplier. This is an obstruction to this inference, not a counterexample to normal CE.

For a full isolated formal theorem one still needs a coherent ideal generated by **compatible** formal multipliers, unit at every regular point of each actual primary model, hence containing a primary power, and a BIG test-ideal product/restriction/subadditivity theorem on the appropriate completed diagonal with the exact all-map convention. Neither (7) nor (8)--(9) proves those statements. A continuous-Jacobian or Noether-different comparison with these actual hypotheses would suffice only after its compatibility and the BIG product/restriction statements are proved. Smolkin 3.12 concerns reduced equidimensional algebras essentially of finite type over a perfect field, not arbitrary complete rings; its uncompleted tensor setting is not silently replaced. The printed finite-field retraction is invalid, and is not used here.

CEMS Setting 2.1 is broader: it permits Noetherian F-finite normal schemes with dualizing complexes and the stated $F^!\omega\simeq\omega$ compatibility, including schemes essentially of finite type over an F-finite local base. Complete equicharacteristic perfect-residue rings are F-finite (their power-series presentations and (7) give finite Frobenius), so this source is **not** rejected merely for lack of field-finite-type hypotheses. Its big trace tails can apply once the actual dualizing data are chosen compatibly. The affine-base Koszul regularity argument also extends: for an ample globally generated $A$ on finite-dimensional projective $Y$ over a Noetherian affine base, the locally split Koszul complex of its generating sections and vanishings $H^i(MA^{-i})=0$, $1\le i\le\dim Y$, propagate the needed twists, give multiplication surjectivity, and, by high-twist Serre generation, generate $M$. No base-flatness is required. These facts locate the unresolved formal step in the compatible primary multiplier and subadditivity mechanism, rather than in mere Frobenius finiteness or projective coherent cohomology.

Consequently completion invariance is unconditional relative to entire G331, and formal discriminant lifting is proved with its displayed hypotheses. The full isolated excellent perfect-charp envelope theorem is not yet claimed. General Jensen lower hemicontinuity on nonisolated higher-dimensional normal germs, mixed or imperfect characteristic, nonclosed or nonalgebraic scope also remains unproved. A dual restatement, a nonnormal obstruction, failure of a discriminant estimate, and increasing energy/capacity spikes do not solve or negate the unchanged original.

## 8. Evidence and support boundary

Sections 1--3 and 5 use only the entire qualified G331; Section 4 is proved from the displayed functional axioms and ordinary Hahn--Banach/Riesz/Banach--Alaoglu foundations. Section 6 is a direct algebraic/formal proof, with ordinary separable-field trace and Noetherian completion background disclosed. B341/E350 remain retained in full as supplied qualified grants; no product or energy theorem is needed for the new completion or lifting statements. The independent native271 review and exact source reading boundary are separate companion documents. No old verdict, source receipt, hash or run is a correctness premise.

Rerun fresh evidence only: `python retain_and_identify.py`; `python audit_delivery.py`; `python finite_checks.py`; `python assemble_delivery.py`. Programs, exact inputs/outputs and environment are retained locally. The source is uncompiled; ROOT retains compilation and publication. Full source bodies, book contexts, and any pixels remain LOCALONLY. No supplied program, extra native/model call, agent, heavy compute, editor/tab/catalogue/publication/auth/proxy/runtime mutation was used. No supervised heavy-compute facility was supplied or needed.
