# Exact scoped status

{
  "id": "P02.4",
  "status": "partial",
  "exact_result": "Arbitrary-target decreasing ordinary CLD-smooth psh sequences on specified countably dense-field curve sectors, including finite unibranch algebraic normalization; all targets on saturated proper-projective-fibre products; a classical boundary spike obstructing every local continuous sequence for uncountable residue field, with an explicit ordinary smooth positive-form sequence for that spike when the residue field is countable. The full original characterization is not solved.",
  "proof_file": "P02.4-argument.md",
  "concrete_gaps": [
    "All arbitrary noninvariant classical psh sheaf germs on nonsaturated higher-dimensional charts; saturated-domain constancy does not cover them.",
    "A sharp geometric necessary-and-sufficient range for every target, beyond the proved sufficient curve sector and particular boundary-spike obstruction.",
    "Boundaryless curves with nonzero residual Picard harmonic quotient; failure of harmonic ordinary smoothness has not been proved to obstruct approximation.",
    "General multibranch or nonalgebraic singular curves and synchronization/descent of ordinary smooth approximants under general finite normalization.",
    "Arbitrary-target sequence extraction over fields without a countable dense subset.",
    "Non-algebraically-closed bases and strict scalar descent; constructed sequences are compatible with all scalar pullbacks but no general descent theorem is proved.",
    "General overlap gluing of independently constructed tropical-chart approximants; overlaps here use actual globally defined functions on one fixed neighborhood."
  ]
}


# Entire final proof

# P02.4: ordinary CLD-smooth decreasing regularization

The original characterization is not solved. We give a stage-one ordinary Chambert--Loir--Ducros (CLD) construction for every arbitrary classical plurisubharmonic (psh) target on specified smooth curves over fields with a countable dense subset, and extend the germ statement through finite unibranch normalization. A quantitative shift makes independently smoothed lisse terms decrease on one fixed ordinary neighborhood. We also treat all targets on saturated products with proper projective fibres, without claiming this treats all sheaf germs on those higher-dimensional spaces. At an actual analytic boundary we construct a classical psh spike which cannot even be a local pointwise limit of a sequence of continuous functions when the residue field is uncountable. For this particular spike, countability of the residue field is also sufficient, by an explicit ordinary smooth psh sequence. None of these results gives the requested sharp characterization of all spaces.

# Scope, definitions, and checked published premises

Only P02.4 is addressed. The required target is a decreasing *sequence* of finite ordinary CLD-smooth psh functions on one fixed ordinary open neighborhood, converging pointwise to an arbitrary classical psh function with values in $\mathbb R\cup\{-\infty\}$. Continuity, finiteness, or torus invariance of the starting function is not imposed in the curve theorems. The word classical has exactly the curve-test meaning in [GR, Definition 4.1]: for every analytic field extension and every analytic curve mapping into the extension of the space, the pullback is subharmonic. The subharmonic definition allows the identically $-\infty$ function; on a connected smooth strictly analytic boundaryless curve it agrees with Thuillier's definition or the identically $-\infty$ case, by [GR, 3.4.2 and 4.1.2].

Ordinary smooth functions are represented on *ordinary open* charts by smooth functions of finitely many logarithms of invertible analytic functions. This is the ordinary-open assertion of the actual saved CD v2, [CD, Proposition 15.1.1(b), Corollary 15.1.2]. An ordinary smooth psh function has $\mathrm d'\mathrm d''f\geq0$ as a smooth $(1,1)$-form. In that saved v2 the smooth stage is $\operatorname{Psh}_{X,0}$, the first decreasing-sequence stage is $\operatorname{Psh}_{X,1}$, and these are defined in Lemma 8.1.4; Definition 8.1.13 calls the latter locally approachable. Proposition 8.1.5 preserves stages under pullback. It does not collapse stage two to stage one. On boundaryless spaces these smooth functions also have positive $\mathrm d'\mathrm d''[f]$ currents by [CD, §8.3, Proposition 8.3.1]; the boundaryless hypothesis in that section is indispensable and is retained here.

The following exact published inputs were read, with their literal proofs retained in the accompanying source extracts.

1.  Thuillier's Theorem 3.4.2 [Thu] gives a decreasing *family/net* of finite lisse subharmonic functions on each relatively compact ordinary open subset of a smooth strictly analytic curve. Its proof uses finite subsets of the non-rigid locus and harmonic interpolation. It does not give the arbitrary-target sequence needed here.

2.  Wanner's standing field in [Wan] is complete, algebraically closed, and nontrivially valued. Lemma 5.2 says: on a smooth proper algebraic curve $C$ satisfying $H_C\subset C^\infty$, a lisse function on a strictly affinoid $Y$ that is subharmonic on $Y\setminus\partial Y$ admits continuous approximants on $Y$, ordinary smooth and psh on that same interior, converging uniformly on $Y$. They can be chosen decreasing. Her Corollary 5.4 verifies the harmonic-smoothness premise if the residue field is algebraic over a finite field, or $C=\mathbb P^1$, or $C$ is a Mumford curve. The corollary's target itself is *finite continuous*; our arbitrary-target claim below uses Lemma 5.2, not an unqualified invocation of that corollary.

3.  GJR Proposition 15.11 [GJR] has the conclusion "a decreasing net of weakly smooth psh functions" on relatively compact opens of a rig-smooth boundaryless curve over a nontrivially valued field. The proof first reduces to one lisse term and constructs a sequence for that term. This does not extract a sequence from the original net. Harmonic neighborhoods in that proof provide weak, and not automatically ordinary, smoothness.

4.  [GR, Propositions 3.5 and 4.2] gives sheafiness, field extension, and analytic pullback of subharmonic and classical psh functions; finite surjective maps also detect these properties. In particular Proposition 3.5(3) applies to a USC curve function subharmonic on the analytic interior, including its arbitrary boundary values. The proof explicitly treats the new interior components over a boundary point after scalar extension. Theorem 6.1 gives the local maximum principle at analytic interior points. The ordinary-smooth/classical comparison is the published argument in [GR, 1.2], reducing curve tests to Wanner's continuous comparison on smooth curve neighborhoods; it is not an unpublished book premise.

Thuillier uses the all-domain site $X_G$ and the strictly analytic rigid site $X_R$ separately ([Thu, 2.1.7]); Definition 3.2.1 extends lisse functions to $X_G$. His Proposition 3.2.4 gives the skeletal description on compact *strict* domains. GJR 15.8--15.9 likewise imposes strict domains and the indicated vertex/value-group restrictions. We never infer strict real-PL membership for all-domain lisse functions. We never replace weakly smooth by ordinary smooth. No real-PL or Fubini--Study conclusion is needed in this argument.

# Two elementary lemmas with quantitative bounds

**Lemma 1** (Countable extraction). *Let $Z$ be second countable and let $(f_i)_{i\in I}$ be a decreasing net of continuous real functions on $Z$ with pointwise infimum $u:Z\to\mathbb R\cup\{-\infty\}$. There are indices $i_j$, increasing in the directed ordering, such that $f_{i_j}$ decreases pointwise to $u$.*

*Proof.* For every rational $q$, $\{u<q\}=\bigcup_i\{f_i<q\}$. A subspace of a second-countable space is second countable and hence Lindelof: choosing one covering open set for each basis element contained in a covering open set gives a countable subcover. Thus choose countably many indices for each $q$ covering $\{u<q\}$. List the union of all selected indices as $a_j$, padding a finite list if necessary. Recursively take $i_j$ dominating $i_{j-1}$ and $a_j$. Then $f_{i_j}\geq u$ and the sequence decreases. If $u(z)<q$, some selected $f_{a_k}(z)<q$, so eventually $f_{i_j}(z)<q$. All rational $q>u(z)$ show the limit is $u(z)$, and all rational $q$ handle $u(z)=-\infty$. If no indices need selecting, the conclusion is trivial. We did not claim the chosen indices are cofinal in the entire directed set. ◻

**Lemma 2** (Strict affinoids over separable fields). *If $K$ has a countable dense subset, every strictly $K$-affinoid space is second countable.*

*Proof.* Choose a countable dense subring of $K$ by adjoining a countable dense subset to its prime ring. The polynomials with these coefficients are a countable dense subset of $K\langle T_1,\ldots,T_N\rangle$. Their images give a countable dense subset $A_0$ of any strict affinoid quotient $A$, with a submultiplicative quotient Banach norm. Every bounded multiplicative seminorm $x$ on $A$ satisfies $|a(x)|\leq\|a\|$: apply boundedness to $a^n$ and take $n$-th roots. The ultrametric inequality gives $\bigl||a(x)|-|b(x)|\bigr|\leq\|a-b\|$ uniformly in $x$. Every evaluation $|a|$ is consequently a uniform limit of evaluations $|b|$ for $b\in A_0$. The topology on $\mathcal M(A)$ is therefore induced by countably many real-valued evaluations. Rational intervals for those coordinates and their finite intersections give a countable base. ◻

**Lemma 3** (One-stage smoothing with a fixed interstage gap). *Suppose $h_j:Y\to\mathbb R$ decreases pointwise to $u$, and for each $j\geq1$ a finite smooth psh $s_j$ on the same $V\subset Y$ satisfies $\|s_j-h_j\|_V\leq\epsilon_j$, where $\epsilon_j=2^{-j}$. Then $$v_j=s_j+4\epsilon_j$$ is smooth psh on $V$, tends pointwise to $u|_V$, and $$\begin{aligned}
 h_j+3\epsilon_j&\leq v_j\leq h_j+5\epsilon_j,\\
 v_j-v_{j+1}&\geq(h_j-h_{j+1})+
 4(\epsilon_j-\epsilon_{j+1})-\epsilon_j-\epsilon_{j+1}
 \geq\epsilon_j/2>0.
\end{aligned}$$*

*Proof.* Adding a constant preserves smoothness and $\mathrm d'\mathrm d''$-positivity. The displayed bounds follow directly from the error inequalities and $\epsilon_{j+1}=\epsilon_j/2$. At a finite target value the error tends to zero, and at a $-\infty$ value the upper bound tends to $-\infty$. All inequalities are pointwise on one fixed $V$. In particular this directly produces stage-one approximants; no stage-two closure argument is used. ◻

# Arbitrary targets on a concrete curve sector

<a id="thm:curves"></a>
**Theorem 4**. *Let $K$ be complete, algebraically closed and nontrivially valued, with a countable dense subset. Let $C$ be a smooth proper algebraic curve satisfying one of the following concrete sufficient conditions:*

1.  *$\widetilde K$ is algebraic over a finite field;*

2.  *$C=\mathbb P^1_K$;*

3.  *$C$ is a Mumford curve.*

*For every ordinary open $W\subset C^\mathrm{an}$, every arbitrary classical psh $u:W\to\mathbb R\cup\{-\infty\}$, and every $x\in W$, there is a strictly affinoid neighborhood $Y\subset W$ of $x$, with ordinary open interior $V=Y\setminus\partial Y$, and a sequence of finite ordinary CLD-smooth psh functions $v_j$ on $V$ decreasing pointwise to $u|_V$. The construction is compatible with restriction, ordinary chart overlaps, and pullback to every analytic extension field. If $u$ is finite continuous, convergence is locally uniform; that extra conclusion is not asserted for an arbitrary target.*

*Proof.* Work in a connected ordinary neighborhood of $x$ in $W$. If the target is identically $-\infty$ there, take $v_j=-j$. Otherwise it is subharmonic in Thuillier's sense by [GR, 3.4.2 and 4.1.2]. Choose a relatively compact ordinary open $W'$ containing $x$ with closure in $W$. Thuillier's Theorem 3.4.2 gives a decreasing net of finite lisse subharmonic functions $f_i$ on $W'$ with infimum $u$. Choose one strictly affinoid neighborhood $Y$ of $x$ contained in $W'$. Such neighborhoods exist on these good strictly analytic algebraic curves; their boundaries are finite and their interiors are ordinary open.

All $f_i|_Y$ are continuous. The second-countability and extraction lemmas produce one decreasing sequence $h_j=f_{i_j}|_Y$ with infimum $u|_Y$. This is the only countable extraction in the proof and its hypothesis has been proved from the field condition. No continuity of $u$ is used.

For every $j$, $h_j$ is lisse on the strictly affinoid $Y$ and subharmonic on the *same* $V=Y\setminus\partial Y$. The geometric conditions in the theorem give $H_C\subset C^\infty$ by the checked proof of Wanner Corollary 5.4 and Thuillier Theorem 2.3.21. Apply Wanner Lemma 5.2 to $h_j$ on $Y$. Select one of its continuous approximants $s_j$ with $\|s_j-h_j\|_Y\leq2^{-j}$. It is ordinary smooth and psh on $V$. Wanner's construction uses harmonic pieces, which are ordinary smooth under $H_C\subset C^\infty$, and convex regularized maxima on the connecting annuli; its equalities with the original term near the gluing boundaries establish ordinary-open gluing. Positivity is the positivity in Lemma 5.2, not an inference from the word smooth.

Apply the fixed-gap lemma to obtain $v_j=s_j+4\cdot2^{-j}$. This is a single decreasing sequence of ordinary smooth psh functions on $V$, with gap at least $2^{-j-1}$ and pointwise limit $u$, including all permitted $-\infty$ values and discontinuities. On a compact subset where the target is finite continuous, Dini's theorem gives uniform convergence.

Each $v_j$ is a globally defined function on $V$. Its ordinary chart representatives consequently agree as functions and as the induced forms on intersections. We did not construct unrelated sequences on different charts and then assume they agree. Restricting the sequence to any ordinary open subset preserves all inequalities and its limit. The field-extension and positivity details are supplied in the next section and apply to these particular globally defined terms. ◻

The field hypothesis is a sufficient hypothesis, not a claimed necessary one; the familiar field $\mathbb C_p$ is an example. The theorem treats all classical psh sheaf germs on ordinary opens of the specified curves, rather than only finite continuous global functions. Wanner's harmonic-smoothness conditions have not been proved necessary for approximation.

# Ordinary pullbacks, scalar extension, and finite unibranch descent

The pullback assertion here concerns ordinary smooth functions with positive $\mathrm d'\mathrm d''$ forms, and not arbitrary positive currents. If $g:Z\to V$ is analytic, an ordinary open chart $$v_j=\phi_j(-\log|a_1|,\ldots,-\log|a_r|),\qquad a_i\in\mathcal O^\times,$$ pulls back to the same smooth real function of the invertible functions $a_i\circ g$. Thus it is ordinary smooth. Differentials commute with pullback, and pullback preserves smooth $(1,1)$-positivity by the linear algebra of [CD, Lemma 1.2.11] and the ordinary tropical-chart construction; equivalently the smooth case of CD Proposition 8.1.5. This proves $\mathrm d'\mathrm d''(g^*v_j)=g^*(\mathrm d'\mathrm d''v_j)\geq0$. This is an application to forms; we do not invoke a pullback operation for arbitrary currents.

For an analytic extension $L/K$ and $\pi:V_L\to V$, the charts pull back to invertible $a_{i,L}$ on the ordinary opens $\pi^{-1}(U)$ and the same $\phi_j$. To justify positivity without assuming that this particular representing Hessian is positive on all of the ambient real space, apply CD Lemma 6.5.1 to the positive ordinary form $\mathrm d'\mathrm d''v_j$. It supplies an ordinary neighborhood $U$, a tropical chart $f$, and a positive form $\alpha$ on a paralinéaire set $P$ containing $f(U)$, with $\mathrm d'\mathrm d''v_j=f^*\alpha$. Refining the chart by Proposition 15.1.1(b) expresses its coordinates as affine combinations of logarithms of analytic units. Those coordinates therefore pull back under scalar extension as well. The image of $f_L=f\circ\pi$ lies in the same $P$, and the positive-linear-pullback test gives $f_L^*\alpha\geq0$. Since differentials commute with this chart pullback, $\mathrm d'\mathrm d''(v_j\circ\pi)=f_L^*\alpha$. This proves positivity even when $L$ has new residue directions; it is not a harmonic-smoothness assertion about all functions over $L$. We obtain ordinary smooth psh $v_{j,L}=v_j\circ\pi$ and $$v_{j,L}-v_{j+1,L}\geq2^{-j-1},\qquad
 \lim_jv_{j,L}(y)=u(\pi(y)).$$ No second countability of $V_L$ is needed. The comparison in [GR, 1.2] makes these smooth psh functions classical; its field-compatible curve test agrees with the positive-form pullback argument. On boundaryless domains, CD §8.3 also gives their positive currents. Successive analytic extensions give exactly the same composed functions. Equality on overlaps is preserved by taking preimages, so the scalar and overlap assertions are actual equalities, not new choices of approximants. This does *not* prove that every new classical psh target over $L$ comes by descent from $K$, or that ordinary smoothness descends along an arbitrary scalar extension.

<a id="thm:unibranch"></a>
**Theorem 5** (A singular unibranch curve sector). *Let $K$ satisfy the field assumptions of Theorem [4](#thm:curves). Let $D$ be an integral proper algebraic curve whose finite normalization $\nu:C\to D$ is bijective on geometric points and whose smooth proper normalization $C$ satisfies one of that theorem's three conditions. Then every arbitrary classical psh sheaf germ on $D^\mathrm{an}$ has a decreasing ordinary CLD-smooth psh sequence on one fixed ordinary neighborhood. The asserted sequences have the same restriction and scalar compatibility as above. In particular this applies to cuspidal proper curves with normalization $\mathbb P^1$.*

*Proof.* On the smooth locus use Theorem [4](#thm:curves) through the normalization isomorphism. The exceptional locus of a normalization of an integral proper algebraic curve is a finite set of closed points; over this $K$ those are $K$-rational rigid points. Around a singular point $x$, remove the other exceptional points. There is exactly one point $x'$ over $x$, and $\nu$ is an isomorphism away from $x$. The analytic finite map is closed and surjective. It is now bijective on the underlying neighborhood, so it is a homeomorphism there. Indeed, outside $x$ it is an isomorphism, and the fibre over $x$ has just the one analytic point $x'$.

Let $u$ be the target on an ordinary neighborhood $W$ of $x$. Then $\widetilde u=u\circ\nu$ is classical psh by GR Proposition 4.2(6). Construct the curve sequence $\widetilde v_j$ on an ordinary neighborhood $V'$ of $x'$ by Theorem [4](#thm:curves). Finiteness and closedness of $\nu$ give an ordinary neighborhood $N\subset W$ of $x$ such that $\nu^{-1}(N)\subset V'$: remove the closed image of the complement of $V'$ in $\nu^{-1}(W)$. Descend the functions via the homeomorphism to finite continuous functions $v_j$ on this single fixed $N$.

Every ordinary CLD-smooth function is locally constant at a $K$-rational rigid point. To see this, use an ordinary chart with finitely many local invertible functions $a_i$. On a sufficiently small neighborhood, $|a_i-a_i(x')|<|a_i(x')|$ for every $i$, by analytic continuity and $a_i(x')\ne0$. Hence all $|a_i|$ are constant there, so is the represented smooth function. Therefore $\widetilde v_j$ is constant on some open neighborhood of $x'$, whose image under the homeomorphism is open at $x$. Its descended $v_j$ is constant on that neighborhood, and is ordinary smooth elsewhere by the analytic isomorphism. This is ordinary-open descent, not general descent of smooth forms along a finite map.

On the constant neighborhood $\mathrm d'\mathrm d''v_j=0$; off $x$ its $\mathrm d'\mathrm d''$ form is nonnegative by the isomorphism with the normalization. These opens cover $N$, so $v_j$ is smooth psh. For classical positivity one can also apply the finite-surjective detection statement GR Proposition 4.2(6) to $\nu^{-1}(N)\to N$. The functions agree on the intersections by their global definition. Their inequalities, interstage gaps and limits are those of $\widetilde v_j$, so $v_j\downarrow u|_N$. Their scalar pullbacks are ordinary smooth psh and converge to $u_L|_{N_L}$ by the preceding chart argument; this does not require a new assertion about normalization commuting with every scalar extension. ◻

The one-point fibre is essential to this proof. With several branches, separately chosen smooth sequences can have different constant values near the preimages of the node at every finite stage. Agreement only of their limits does not permit their descent. No claim is made for arbitrary multibranch singularities, general finite maps, or strict scalar descent over a non-algebraically-closed base field.

# All targets on a noninvariant saturated higher-dimensional sector

<a id="prop:saturated"></a>
**Proposition 6**. *Under the smooth curve hypotheses of Theorem [4](#thm:curves), let $U\subset C^\mathrm{an}$ be ordinary open, $m\geq1$, and let $X=U\times_K(\mathbb P^m_K)^\mathrm{an}$ with projection $p$. For every arbitrary classical psh function $u$ defined on this entire saturated $X$, and each $z\in U$, there is an ordinary neighborhood $V$ of $z$ and a sequence of finite ordinary smooth psh functions on the single ordinary open $p^{-1}(V)$ decreasing to $u|_{p^{-1}(V)}$. There is no torus-invariance or continuity assumption on $u$.*

*Proof.* For $z\in U$, the analytic fibre is $(\mathbb P^m_{\mathcal H(z)})^\mathrm{an}$. Apply scalar extension and analytic pullback, GR Proposition 4.2(5,6), to see that $u$ restricts to a classical psh function on this fibre. Projective space analytification is compact, connected and boundaryless. A USC function into $\mathbb R\cup\{-\infty\}$ on it is either identically $-\infty$ or has a finite attained maximum $M$: local finite upper bounds give a global bound by compactness, and nested closed upper-level sets give attainment. In the latter case its maximum locus is nonempty and closed. At every point of that locus GR Theorem 6.1 applies, since the whole fibre is boundaryless, so the locus is open. Connectedness implies that the function is constant. Thus $u$ is constant on every proper fibre, including the entirely $-\infty$ fibres.

Choose a $K$-rational point $o\in\mathbb P^m(K)$ and its analytic section $s:U\to X$. Set $w=u\circ s$. It is USC and classical psh by analytic pullback, hence subharmonic on the curve $U$. Fibrewise constancy gives the equality of functions $u=w\circ p$, including infinite values. Apply Theorem [4](#thm:curves) to $w$ at $z$ on a fixed $V$. Its smooth psh terms $w_j$ pull back to ordinary smooth psh $w_j\circ p$ by the ordinary pullback proof above, and $$w_j\circ p-w_{j+1}\circ p\geq2^{-j-1},\qquad
 w_j\circ p\downarrow w\circ p=u.$$ The identically $-\infty$ case uses $-j$ instead. The entire inverse image $p^{-1}(V)$ is one ordinary open neighborhood of every point over $z$. The global formula establishes overlap agreement. After every analytic extension it remains the same formula with $p_L$ and the pulled-back $w_j$; its positivity and decreasing convergence remain valid. The products here are boundaryless, so the smooth current is positive as well. ◻

This is an assertion about *all targets on saturated domains*. It is not the assertion that every sheaf germ on $X$ has been regularized. A target initially defined only on a nonsaturated affine chart cannot be restricted to a whole proper fibre, and the preceding maximum-principle argument is unavailable. No extension of that target to the saturated domain has been proved. Consequently this proposition does not establish the original P02.4 local sheaf property for these higher-dimensional spaces. It does give a noninvariant higher-dimensional sufficient sector with arbitrary, possibly discontinuous or $-\infty$-valued, targets in the specified domain of definition.

# A sharp sequence obstruction at an actual analytic boundary

Let $K$ now be any complete algebraically closed nontrivially valued field; no dense-countability assumption is imposed. Write $D=\mathcal M(K\langle T\rangle)$, let $\eta$ be its Gauss point, and fix $A>0$. Define $$u(\eta)=A,\qquad u(x)=0\quad(x\ne\eta).$$ The singleton $\{\eta\}$ is closed in the Hausdorff disc, so $u$ is USC. The analytic boundary of this closed disc is exactly $\{\eta\}$ and $u=0$ on $\operatorname{Int}(D)$. GR Proposition 3.5(3), with its scalar-compatible boundary proof, says $u$ is subharmonic on $D$. GR 4.1.2 makes it classically psh. This step verifies the actual starting class, rather than just exhibiting a topological USC function.

For each $\alpha\in\widetilde K$, choose a representative $a_\alpha\in K^\circ$ and set $$D_\alpha=\{x\in D:|T-a_\alpha|(x)<1\}.$$ These are nonempty pairwise disjoint ordinary open residue discs, and partition $D\setminus\{\eta\}$. One elementary verification of the last assertion is as follows. If every $|T-a_\alpha|(x)=1$, every nonzero polynomial, factored over the algebraically closed $K$, has its Gauss norm at $x$: roots in $K^\circ$ give factors of norm one and roots outside $K^\circ$ give their constant dominating absolute value. Approximate Tate series uniformly by polynomials to conclude that $x$ is the Gauss seminorm. Conversely $|T-a_\alpha|(x)<1$ singles out exactly that residue class by the ultrametric inequality.

Every ordinary neighborhood of $\eta$ contains all but finitely many *whole* $D_\alpha$. Indeed a basic neighborhood uses finitely many evaluations of Tate series $f$. Normalize a nonzero $f$ by its Gauss norm; its reduction is a nonzero polynomial over $\widetilde K$, since its coefficients tend to zero. Outside the finitely many roots of that reduction, $|f|$ is its Gauss norm throughout the corresponding residue disc. For a direct verification, translate by $a_\alpha$: if its reduced value there is nonzero, the constant term has full norm, while all nonconstant terms times $(T-a_\alpha)^n$ have strictly smaller norm at every point of that open disc. Thus any finite collection of such evaluations agrees with its value at $\eta$ outside finitely many directions. This proves the neighborhood assertion.

<a id="thm:obstruction"></a>
**Theorem 7** (Uncountable residual boundary obstruction). *If $\widetilde K$ is uncountable, the above classical psh $u$ is not a pointwise limit of *any sequence of finite continuous functions* on any ordinary neighborhood of $\eta$ in $D$. In particular $D$ fails the original decreasing ordinary CLD-smooth psh property at $\eta$.*

*Proof.* Suppose continuous $v_j:N\to\mathbb R$ converge pointwise to $u|_N$, where $N$ is an ordinary neighborhood of $\eta$. Discard finitely many indices so that $v_j(\eta)>3A/4$. For each remaining $j$, continuity gives an ordinary neighborhood $N_j\subset N$ of $\eta$ on which $v_j>A/2$. By the preceding neighborhood assertion, there is a finite set $E_j\subset\widetilde K$ such that $D_\alpha\subset N_j$ for $\alpha\notin E_j$. Choose $\alpha\notin\bigcup_jE_j$, possible by uncountability, and its rigid point $a_\alpha$. All $v_j(a_\alpha)>A/2$, but $u(a_\alpha)=0$, a contradiction. Decreasingness and psh positivity were not even needed. ◻

**Corollary 8** (Higher-dimensional failures). *For the same $K$ with uncountable residue field and any $m\geq1$, $D\times_K(\mathbb P^m_K)^\mathrm{an}$ fails P02.4 at $(\eta,o)$ for any $K$-rational $o$.*

*Proof.* The pullback $p^*u$ under projection is classical psh by GR Proposition 4.2(6). If continuous, in particular ordinary smooth, approximants existed on a neighborhood $N$ of $(\eta,o)$, restrict them to the analytic section $D\times\{o\}$. Its inverse image of $N$ is an ordinary neighborhood of $\eta$, and its target is exactly $u$. Theorem [7](#thm:obstruction) forbids even a continuous sequence there. These are good strictly analytic spaces with a genuine analytic boundary; the obstruction is not a purported residue-Picard obstruction on a boundaryless curve. ◻

<a id="prop:countable-spike"></a>
**Proposition 9** (Sharpness for this spike). *If $\widetilde K$ is countable, the same spike admits a decreasing sequence of finite ordinary CLD-smooth functions with nonnegative $\mathrm d'\mathrm d''$ form on the *entire fixed closed disc* $D$. Thus, for this target, countability of the residue field is both necessary and sufficient. These are the ordinary smooth stage-zero psh functions of CD.*

*Proof.* Enumerate $\widetilde K$ and choose representatives $a_1,a_2,\ldots$. (The residue field of an algebraically closed field is infinite, so no finite-list issue arises.) Choose a nonzero nonnegative smooth bump $\beta$ supported in $(-1,-1/2)$. Set $$c=\frac{A}{\int_{-1}^{-1/2}(-t)\beta(t)\,dt},\qquad
 \chi(s)=c\int_{-\infty}^s(s-t)\beta(t)\,dt.$$ Then $\chi$ is finite smooth convex nondecreasing, $\chi(s)=0$ for $s\leq-1$, $\chi(0)=A$, and $0\leq\chi(s)\leq A$ for $s\leq0$. Put $P_j(T)=\prod_{i=1}^j(T-a_i)$ and $$v_j(x)=\chi\bigl(j\log|P_j(x)|\bigr),
 \quad\text{with }v_j(x)=0\text{ if }P_j(x)=0.$$ On the ordinary open locus $P_j\ne0$, this is a smooth function of the logarithm of an invertible analytic function. Near a zero, the open set $|P_j|<e^{-1/j}$ has $v_j=0$, so this extension is ordinary smooth there as well. These ordinary open sets cover $D$ and their functions agree on intersections. On the nonzero locus, write $\ell=j\log|P_j|$; the logarithm of a unit is affine in an ordinary tropical chart, so $$\mathrm d'\mathrm d''v_j=\chi''(\ell)\,\mathrm d'\ell\wedge\mathrm d''\ell\geq0.$$ It vanishes on the constant neighborhoods of zeros. Hence the functions are smooth psh in the CD stage-zero positive-form sense. Positive currents are also obtained on their analytic interiors, but CD §8.3 is not cited to assert an unqualified current statement at the boundary.

On $D$ every $\log|T-a_i|\leq0$. On the common nonzero locus, $$(j+1)\log|P_{j+1}|-j\log|P_j|
 =\sum_{i\leq j}\log|T-a_i|+(j+1)\log|T-a_{j+1}|\leq0.$$ Monotonicity of $\chi$, together with the zero values when a factor vanishes, proves $v_{j+1}\leq v_j$. At $\eta$ every factor has norm one, so $v_j(\eta)=A$. If $x\ne\eta$, choose $i$ with $|T-a_i|(x)=r<1$. For $j\geq i$ with no vanishing factor, $j\log|P_j(x)|\leq j\log r\to-\infty$. Thus $v_j(x)$ is eventually exactly zero; a vanishing factor gives the same conclusion immediately. Therefore $v_j\downarrow u$ on this one fixed domain.

After an arbitrary analytic extension $L/K$, the identical polynomials, cutoff neighborhoods and positive Hessian formula give ordinary smooth psh $v_{j,L}$. Pointwise composition gives $v_{j,L}\downarrow u\circ\pi_{L/K}$. If $\widetilde L$ is uncountable, this is not a contradiction: the target is the spike on the full inverse image $\pi_{L/K}^{-1}(\eta)$, not the singleton-Gauss spike on $D_L$. For example new residue directions over $L$ can map entirely to the old Gauss point. The two targets must not be identified. ◻

The "if and only if" just proved concerns this one spike, not all classical psh functions on all discs with countable residue field. In particular it does not supply a sharp characterization for the original arbitrary-target problem at analytic boundaries.

# Residue Picard/genus effects do not prove a failure of approximation

In the precise semistable type-two setup of Thuillier Theorem 2.3.21 and Lemma 2.3.22, the latter identifies $$H_{C,x}/F_{C,x}\simeq\operatorname{Pic}^0(C_x)\otimes_{\mathbb Z}\mathbb R,$$ where $C_x$ is the proper geometrically connected residual component and $F$ is generated by logarithms of local analytic units. GJR Remark 15.10 identifies $F$ with the ordinary smooth harmonic functions. Thus a nonzero quotient implies some harmonic germ is not ordinary smooth. It does not assert that the germ cannot be a decreasing limit of ordinary smooth *psh*, nonharmonic functions. Wanner Remark 5.5 explicitly leaves ordinary approximation on such curves unknown in that paper.

If the residual component is rational, $\operatorname{Pic}^0=0$. If the algebraically closed residue field is algebraic over a finite field, every Jacobian point is defined over some finite field and belongs to its finite group of rational points, hence is torsion. Thus its tensor with $\mathbb R$ is zero even when the residual genus is positive. Positive residual genus alone is not an obstruction. The actual PDF at printed page 59 says "est de cardinal fini" in the algebraic-finite-field bullet; we do not use that stronger sentence about the entire group, which need not be finite. The elementary pointwise torsion argument above is the needed justification. Direct PDF inspection confirmed the Picard quotient, the theorem's two conditions, and that GJR 15.11 really says a net.

We have proved neither necessity of $H_C\subset C^\infty$ for approximation nor removal of it. In particular the genuine boundary counterexample in the preceding section must not be reinterpreted as a residue-genus counterexample on smooth boundaryless curves.

# Remaining exact original obligations and reproducible evidence

The exact original P02.4 remains open in this draft. The results here do not characterize higher-dimensional good strict analytic spaces for all classical psh sheaf germs. Unresolved obligations include:

1.  arbitrary noninvariant targets on nonsaturated higher-dimensional ordinary charts and a geometric criterion covering all such targets;

2.  a sharp positive/failure range beyond the displayed curve sector and the displayed residual-cardinality boundary spike;

3.  boundaryless curves with $H/F\ne0$, without turning one nonsmooth harmonic germ into an unproved approximation obstruction;

4.  arbitrary multibranch or nonalgebraic singular curves, and ordinary smooth descent and synchronization along general finite normalization;

5.  nonseparable fields in the arbitrary-target positive curve theorem, where its explicit net-to-sequence extraction no longer applies;

6.  non-algebraically-closed bases and strict scalar descent. Existing scalar compatibility here concerns pullbacks of the constructed sequence, not descent of independently constructed sequences;

7.  compatibility needed to glue approximants from unrelated local tropical charts. Here all asserted overlaps come from actual globally defined terms on one neighborhood, not from a general gluing theorem.

This is a mathematical argument based on checked published premises, not an exhaustive finite search or computational proof. Executable checks only validate retained inputs, source bytes, arithmetic of the explicit interstage estimates, and document generation. They do not establish mathematical correctness of the new arguments.

All files are in the fresh working directory. The original bytes are retained in `input.json` and `input-original.json`; the assignment and task are retained in `assignment-original.txt` and `task-original.json`. The full proof is in `P02.4-argument.md` and embedded in this standalone `P02.4-paper.tex`. The seven authorized source PDF/extract pairs, their supplied and actual hashes, selected literal statements and complete proofs, exact application checks, and direct PDF inspection records are listed in `source-extracts/source-provenance.json`. There was no reading of earlier campaign workspaces or unpublished book sources, no network use, no installation, no subagent or other-model invocation, and no runtime changes or heavy computation.

Rerun from this directory with

    python3 verify_sources.py
    python3 build_and_check.py

The second script invokes the existing `pandoc` to render the same standalone proof into Markdown and the existing `pdflatex` twice, with `-interaction=nonstopmode`, `-halt-on-error`, and `-file-line-error`. Actual return codes, warnings, error lines and complete transcripts are retained in `checks.json`, `build-diagnostics.json`, and `build/`. The environment versions are retained in `environment.json`. The PDF is a reading artifact; successful builds and matching hashes do not certify any theorem.

# Published sources

- **GR**: W. Gubler and J. Rabinoff, *Classically psh and pluriharmonic functions on Berkovich spaces*, saved public arXiv:2506.13548v2, especially 3.4--3.5, 4.1--4.2, 6.1. <https://arxiv.org/pdf/2506.13548v2>.

- **GRPL**: W. Gubler and J. Rabinoff, public arXiv:2503.05513, saved supplied version; PL and piecewise smooth foundations checked, not used as arbitrary ordinary smooth regularization. <https://arxiv.org/pdf/2503.05513>.

- **Thu**: A. Thuillier, thesis, 2005, saved tel-00010990v1, especially 2.1.7, 2.3.21--2.3.22, 3.2.1--3.2.4, 3.4.2. <https://theses.hal.science/tel-00010990v1/document>.

- **GJR**: W. Gubler, P. Jell and J. Rabinoff, *Forms on Berkovich spaces based on harmonic tropicalizations*, saved public arXiv:2111.05741, 15.8--15.11. <https://arxiv.org/pdf/2111.05741>.

- **Ber**: V. G. Berkovich, *Etale cohomology for non-Archimedean analytic spaces*, Publ. Math. IHES 78 (1993), 5--161, supplied public cache. <https://www.numdam.org/item/PMIHES_1993__78__5_0/>.

- **CD**: A. Chambert-Loir and A. Ducros, *Formes differentielles reelles et courants sur les espaces de Berkovich*, actual saved public arXiv:1204.6277v2. Numbering here refers to that supplied v2, not the older numbering used in Wanner. <https://arxiv.org/pdf/1204.6277v2>.

- **Wan**: V. Wanner, *Comparison of two notions of subharmonicity on non-Archimedean curves*, saved public arXiv:1801.04713v3; standing terminology, Lemma 5.2, Corollary 5.4, Remark 5.5. <https://arxiv.org/pdf/1801.04713v3>.



# All actual native canonical fields and support

[
  {
    "id": "n1",
    "summary": "Arbitrary classical psh targets admit decreasing ordinary CLD-smooth psh sequences on specified curves over countably dense fields, including finite unibranch algebraic normalization. This is a sufficient curve sector, not a characterization.",
    "detailedSummary": "Let K be complete, algebraically closed, nontrivially valued, and have a countable dense subset. For smooth proper C, assume its residue field is algebraic over a finite field, or C is P1, or C is Mumford. Every arbitrary classical psh target on an ordinary open subset of C admits ordinary smooth psh approximants decreasing on one fixed ordinary neighborhood, including discontinuities and permitted minus-infinity values. The proof extracts a sequence from Thuillier’s lisse net on a second-countable strictly affinoid domain, applies Wanner Lemma 5.2 separately to its terms, and enforces a quantitative decreasing gap. A finite unibranch normalization permits ordinary smooth descent because each smooth term is constant near the rational preimage of the singularity. Scalar compatibility concerns pullbacks of constructed sequences; general scalar descent, multibranch synchronization, and necessity of the hypotheses remain unresolved.",
    "text": "Claim and published premises. Let K be complete, algebraically closed, nontrivially valued, with a countable dense subset. Let C be smooth proper algebraic, and suppose either the residue field is algebraic over a finite field, C=P1, or C is Mumford. Every arbitrary classical psh u:W→R∪{−∞} on an ordinary open W⊂C^an has, near each point, a decreasing sequence of finite ordinary CLD-smooth psh functions on one fixed ordinary neighborhood. GR arXiv:2506.13548v2, 3.4.2 and 4.1.2, identifies the starting class on connected smooth strictly analytic curves with Thuillier subharmonic functions or the identically −∞ case. Thuillier Theorem 3.4.2 supplies a decreasing net of finite continuous lisse subharmonic functions. Wanner’s standing field assumptions are exactly the field assumptions above except countable density. Her Lemma 5.2, under H_C⊂C∞, uniformly smooths each lisse subharmonic function on a strictly affinoid Y by continuous functions on Y which are ordinary smooth and psh on Y\\∂Y. Her Corollary 5.4 verifies H_C⊂C∞ under the three displayed conditions; its own target is finite continuous, so it is not invoked directly for arbitrary u.\n\nCountable extraction. On a second-countable space Z, let continuous f_i decrease as a net to u. For rational q, {u<q}=⋃_i{f_i<q}. Each such open subspace is Lindelöf, so select countably many indices covering it. Enumerate all selected indices over all rational q and recursively choose indices dominating the preceding choice and the next selected index. The resulting terms decrease, remain above u, and eventually lie below every rational q>u(z). This proves pointwise convergence, including u(z)=−∞. The chosen indices need not be cofinal in the original directed set.\n\nWhy the countability hypothesis holds here. A strictly affinoid algebra A is a quotient of K〈T1,…,TN〉. Polynomials over a countable dense subring give a countable dense subset A0. For every bounded multiplicative seminorm x, |a(x)|≤||a||, by applying boundedness to powers. Therefore ||a(x)|−|b(x)||≤||a−b|| uniformly in x. All evaluation functions are uniform limits of evaluations from A0. Their rational interval inverse images and finite intersections form a countable base for M(A).\n\nConstruction on a fixed neighborhood. Take a relatively compact ordinary open W′ around x inside W and one strictly affinoid neighborhood Y⊂W′ of x. Restrict Thuillier’s net to Y and apply the extraction argument to obtain h_j↓u on Y. Put V=Y\\∂Y, an ordinary open neighborhood of x. Apply Wanner Lemma 5.2 to each h_j on this same Y, obtaining a continuous s_j on Y, ordinary smooth and psh on V, with ||s_j−h_j||_Y≤ε_j=2^(−j). Define v_j=s_j+4ε_j. Then h_j+3ε_j≤v_j≤h_j+5ε_j and\nv_j−v_(j+1)≥h_j−h_(j+1)+4(ε_j−ε_(j+1))−ε_j−ε_(j+1)≥ε_j/2>0.\nThus v_j↓u on the single fixed V. At a minus-infinity value the upper bound tends to minus infinity. For an identically minus-infinity neighborhood use v_j=−j. Local uniform convergence is asserted only for finite continuous targets, by Dini’s theorem.\n\nOrdinary regularity, positivity, and compatibility. Wanner’s lemma uses ordinary smooth harmonic pieces under H_C⊂C∞ and convex regularized maxima on annuli, with agreement near the gluing boundaries. The positivity conclusion is supplied by that lemma. Adding constants preserves it. The actual saved CD v2 uses ordinary open charts in Proposition 15.1.1(b); its smooth stage is Psh_0, its first decreasing-sequence stage is Psh_1 in Lemma 8.1.4, and smooth pullback is covered by Proposition 8.1.5. These functions have nonnegative d′d″ forms and, on the boundaryless neighborhoods here, positive d′d″[v_j] currents by CD §8.3 and Proposition 8.3.1. Ordinary chart representatives agree because each v_j is one globally defined function on V.\n\nFor every analytic extension L/K, the same smooth real chart functions applied to the pulled-back analytic units represent v_j∘π on ordinary opens of V_L. CD Lemma 6.5.1 gives local positive tropical representatives of d′d″v_j. Their pulled-back images remain in the same paralinéaire support, and CD Lemma 1.2.11 preserves their positivity under linear pullback. Thus the scalar pullbacks are ordinary smooth psh. Their gaps remain ≥2^(−j−1), and their pointwise limit is u∘π. No countability of L is required, and no independently constructed sequences must be synchronized.\n\nUnibranch extension. Let D be an integral proper algebraic curve with finite normalization ν:C→D bijective on geometric points, where C satisfies the conditions above. Near a singular point x remove the other finitely many singularities. There is one rational rigid point x′ over x, and ν is an isomorphism elsewhere. The finite closed bijection is a homeomorphism. Pull u back to C and construct the preceding sequence on V′ around x′. Closedness supplies one ordinary N around x with ν^(−1)(N)⊂V′. Descend the sequence by the homeomorphism. Every ordinary smooth function is constant near a rational rigid point: in an ordinary chart, finitely many invertible a_i satisfy |a_i−a_i(x′)|<|a_i(x′)| on a sufficiently small neighborhood, so all |a_i| are constant. Each descended term is consequently constant near x and smooth by the isomorphism elsewhere. Its d′d″ form is zero on the constant neighborhood and nonnegative elsewhere. Global descent preserves its gaps and limit. Scalar pullback then follows from the preceding chart argument. This includes cuspidal proper curves with normalization P1.\n\nLimitations. The field and harmonic-smoothness conditions are sufficient, not proved necessary. Multibranch normalization can give different constant values on different preimages at every stage; limit agreement does not justify descent. No general finite smooth descent or strict scalar descent is claimed. All-domain lisse functions were not identified with strict real-PL functions, and weak smoothness was not substituted for ordinary smoothness.\n\nThe complete argument is retained in P02.4-argument.md and embedded in standalone P02.4-paper.tex. Literal premises, proofs, and application checks are retained in source-extracts/source-provenance.json. Rerun from the supplied workspace with python3 verify_sources.py and python3 build_and_check.py. This is an unverified mathematical draft using checked published foundations; execution does not certify its correctness.\n\nArtifacts: /workspace/research/campaigns/round-44/P02.4-public-source-decreasing-ordinary-smooth/artifacts/codex-QKCSac",
    "support": []
  },
  {
    "id": "n2",
    "summary": "All arbitrary classical psh targets on saturated products of a permitted curve with proper projective fibres have decreasing ordinary smooth psh approximants. This does not establish regularization of nonsaturated higher-dimensional sheaf germs.",
    "detailedSummary": "Under n1’s smooth curve hypotheses, every classical psh function defined on the entire saturated domain U×P^m analytification is constant on each proper fibre. A rational section identifies it with a subharmonic target on U, so n1’s ordinary smooth sequence pulls back on a fixed saturated neighborhood. The starting target need not be continuous, finite, or torus invariant. The conclusion depends on having whole proper fibres in the domain of definition; it does not cover arbitrary targets initially defined on smaller nonsaturated charts.",
    "text": "Let K and the smooth proper curve C satisfy n1, let U⊂C^an be ordinary open, and let X=U×_K(P^m_K)^an with m≥1 and projection p. For every arbitrary classical psh u defined on all of this saturated X, each z∈U has an ordinary neighborhood V such that u|p^(−1)(V) is a decreasing limit of finite ordinary CLD-smooth psh functions on that one fixed ordinary open.\n\nProof. The fibre over z is (P^m_H(z))^an. GR v2 Proposition 4.2(5,6) makes the restriction of u classical psh there. This fibre is compact, connected, and boundaryless. If the restriction is not identically −∞, upper semicontinuity and compactness give a finite attained maximum M. Its maximum locus is nonempty and closed. GR Theorem 6.1 applies at every point of this locus because the entire fibre is an analytic interior; the locus is therefore open. Connectedness implies that u is constant on the fibre. The identically −∞ case is already constant.\n\nChoose a rational point o of P^m and its section s:U→X. The function w=u∘s is classical psh by analytic pullback, hence subharmonic on the curve, and fibre constancy proves the actual equality u=w∘p, including −∞ values. Apply n1 to w at z. Pull its terms w_j back to w_j∘p on p^(−1)(V). Ordinary smoothness and positive d′d″ forms follow from the proved ordinary chart pullback argument. The same quantitative gaps and pointwise convergence are preserved. In the identically −∞ case use constants −j. The products are boundaryless, so the smooth currents are positive as well.\n\nEach term is globally given by the projection formula. Ordinary chart overlaps therefore agree, and after every analytic extension the formula is exactly w_j,L∘p_L. This proves the asserted scalar compatibility without choosing new approximants over the extension.\n\nScope. This treats all targets on the specified saturated domains and permits noninvariant, discontinuous, or −∞-valued targets. A target on a nonsaturated affine chart need not extend to whole proper fibres. The fibre maximum argument cannot be applied to it, and no such extension theorem was proved. Consequently this result does not establish the original higher-dimensional local sheaf characterization.\n\nThe full proof and this limitation appear in P02.4-argument.md and P02.4-paper.tex; the maximum-principle source proof and exact application checks are retained in source-extracts/source-provenance.json. Rerun commands are python3 verify_sources.py and python3 build_and_check.py from the supplied workspace.\n\nArtifacts: /workspace/research/campaigns/round-44/P02.4-public-source-decreasing-ordinary-smooth/artifacts/codex-QKCSac",
    "support": [
      "n1"
    ]
  },
  {
    "id": "n3",
    "summary": "A classical psh Gauss-boundary spike on a closed disc admits no local continuous sequence when the residue field is uncountable. For this particular spike, countable residue is sufficient via an explicit decreasing ordinary smooth positive-form sequence.",
    "detailedSummary": "Over a complete algebraically closed nontrivially valued field, set u=A>0 at the Gauss point of the closed unit disc and zero elsewhere. GR’s exact boundary proposition verifies that this USC function is classically psh, including scalar compatibility. Every neighborhood of the Gauss point contains all but finitely many whole residue discs. An uncountable collection of such directions defeats any pointwise continuous sequence on any fixed neighborhood. The obstruction also transfers to higher-dimensional products by an analytic section. When the residue field is countable, enumerated residue representatives and a smooth convex cutoff of j log|∏(T−a_i)| give actual decreasing ordinary CLD-smooth psh approximants on the entire fixed disc. This equivalence concerns the spike, not every target or a complete boundary characterization.",
    "text": "Let K be complete, algebraically closed, and nontrivially valued. Put D=M(K〈T〉), let η be its Gauss point, and fix A>0. Define u(η)=A and u(x)=0 for x≠η. Since {η} is closed, u is upper semicontinuous. The analytic boundary of D is {η}, and u is zero on Int(D). GR arXiv:2506.13548v2 Proposition 3.5(3), whose literal scalar-compatible proof was checked, says u is subharmonic on D. GR 4.1.2 makes it classical psh. Thus the example belongs to the actual original starting class.\n\nResidue directions. For each α in the residue field choose a representative a_α∈K° and let D_α={|T−a_α|<1}. These nonempty disjoint ordinary open discs partition D\\{η}. Indeed, if a point has |T−a_α|=1 for every residue class, factor polynomials over K to see that its polynomial evaluations are the Gauss norms; approximation of Tate series by polynomials makes the point η. The ultrametric inequality gives uniqueness of the residue direction otherwise.\n\nEvery ordinary neighborhood of η contains all but finitely many whole D_α. A basic neighborhood uses finitely many Tate-series evaluations. A nonzero normalized series has a nonzero polynomial reduction because its coefficients tend to zero. Away from the finitely many roots of that reduction its absolute value is its Gauss norm throughout the corresponding residue disc. To verify this, translate by a_α: the constant term has full norm, while every nonconstant term multiplied by (T−a_α)^n has smaller norm on that disc. Thus finitely many evaluations exclude only finitely many directions.\n\nFailure for uncountable residue. Suppose finite continuous v_j on an ordinary N containing η converge pointwise to u. Discard finitely many indices so that v_j(η)>3A/4. Continuity gives an ordinary neighborhood N_j⊂N of η with v_j>A/2. Each N_j contains every whole residue disc outside a finite exception set E_j. If the residue field is uncountable, choose α outside the countable union of E_j. At its rigid representative a_α all remaining v_j exceed A/2, contradicting u(a_α)=0. Neither decreasingness nor positivity was needed. In particular D fails P02.4 at its actual analytic boundary.\n\nHigher-dimensional failure. On D×(P^m_K)^an, the projection pullback of u is classical psh by GR Proposition 4.2(6). Any continuous approximating sequence near (η,o), with o rational, restricts along the analytic section D×{o} to such a sequence near η. The preceding contradiction applies. These are good strictly analytic examples in every positive dimension of this product family.\n\nExplicit countable-residue construction. Enumerate the residue field and choose representatives a_1,a_2,… . Choose a nonzero nonnegative smooth bump β supported in (−1,−1/2), and define\nc=A/[∫(−t)β(t)dt],  χ(s)=c∫_(−∞)^s(s−t)β(t)dt.\nThen χ is smooth, convex, nondecreasing, zero for s≤−1, and χ(0)=A. Put P_j=∏_(i≤j)(T−a_i) and v_j=χ(j log|P_j|), taking value zero at zeros of P_j. Away from zeros this is an ordinary smooth function of the logarithm of an analytic unit. On {|P_j|<exp(−1/j)} it is identically zero, proving ordinary smooth extension at zeros. These ordinary open representations agree on their overlaps.\n\nWriting ℓ=j log|P_j| on the nonzero locus gives d′d″v_j=χ″(ℓ)d′ℓ∧d″ℓ≥0; on the constant neighborhoods it is zero. Thus these are ordinary CLD-smooth stage-zero psh functions. Current positivity is also valid on their boundaryless interiors; no unqualified boundary-current inference from CD §8.3 is made.\n\nAll log|T−a_i|≤0 on D. Consequently\n(j+1)log|P_(j+1)|−j log|P_j|=∑_(i≤j)log|T−a_i|+(j+1)log|T−a_(j+1)|≤0.\nMonotonicity of χ proves v_(j+1)≤v_j, also at zeros. At η every v_j=A. For x≠η choose i with r=|T−a_i|(x)<1. For j≥i, either P_j(x)=0 or j log|P_j(x)|≤j log r→−∞, so v_j(x) is eventually exactly zero. Hence v_j↓u on the entire fixed D.\n\nEvery analytic scalar extension preserves the polynomials, ordinary cutoff charts, positive Hessian formula, and decreasing inequalities. The pulled-back sequence converges to u∘π. If the new residue field is uncountable, this target is supported on the entire fibre π^(−1)(η), not just the new Gauss singleton, so there is no contradiction with the obstruction.\n\nSharpness and limits. Countability of the residue field is necessary and sufficient for this spike to admit the displayed ordinary smooth positive-form sequence. No characterization of all classical psh targets on countable-residue discs follows. This is an actual boundary obstruction, independent of harmonic ordinary-smoothness or residue-genus claims.\n\nThe complete proof and source application checks are retained in P02.4-argument.md, P02.4-paper.tex, and source-extracts/source-provenance.json. Rerun commands: python3 verify_sources.py and python3 build_and_check.py from the supplied workspace.\n\nArtifacts: /workspace/research/campaigns/round-44/P02.4-public-source-decreasing-ordinary-smooth/artifacts/codex-QKCSac",
    "support": []
  },
  {
    "id": "n4",
    "summary": "The requested proof artifacts and two clean TeX builds are complete. Exact source checks distinguish weakly smooth nets, ordinary stages, and residue-Picard effects. The full original P02.4 characterization remains open.",
    "detailedSummary": "The implementation retained the original input bytes and requested documents, verified all seven supplied PDF/extract hash pairs, saved 24 literal extracts with application checks, and directly inspected decisive primary-PDF pages. Both final TeX passes exited successfully without warnings or layout diagnostics. These are integrity and execution observations, not mathematical verification. The supplied GJR statement is a weakly smooth net; Wanner’s published corollary has finite-continuous and field/curve restrictions. The residue Picard quotient measures failure of harmonic ordinary smoothness but does not prove failure of decreasing psh approximation. The original remains unresolved for arbitrary nonsaturated higher-dimensional germs, sharp general geometry, general singularities, nonseparable fields, strict scalar descent, and general overlap gluing.",
    "text": "Implementation observations. The supplied input and its preserved original are byte-identical: 17,853 bytes, SHA-256 652325686be7e1d70fcf06d990bc0fda4e7990d7a79b2922f3176b411867898c. The assignment text is preserved exactly, and the separately retained task has identical JSON content. All seven authorized primary-source PDF/extract pairs matched their supplied hashes. Twenty-four selected literal extracts retain the pertinent statements and complete selected proofs, with precise application checks. Direct inspection of actual PDF pages confirmed that GJR Proposition 15.11 says a decreasing net of weakly smooth psh functions and confirmed Thuillier’s Picard quotient and exact theorem conditions.\n\nResidue-Picard limitation. In Thuillier’s proper geometrically connected semistable type-two setup, H_x/F_x≃Pic^0(C_x)⊗_Z R. GJR Remark 15.10 identifies F with ordinary smooth harmonic functions. A nonzero quotient establishes existence of a harmonic germ that is not ordinary smooth. It does not rule out decreasing ordinary smooth nonharmonic psh approximants. Positive residual genus alone does not imply a nonzero quotient: over an algebraic closure of a finite field, each Jacobian point is defined over some finite field and is torsion. The actual Thuillier PDF contains a stronger sentence asserting finiteness of the entire group; that sentence was not used. The elementary pointwise torsion argument gives the needed conclusion. Neither the positive hypotheses of n1 nor a proposed Picard failure range has been proved sharp.\n\nArtifacts. The requested files are input.json, byte-identical input-original.json, assignment-original.txt, task-original.json, P02.4-argument.md, standalone P02.4-paper.tex, and P02.4-paper.pdf. Source excerpts, PDF inspection images, hashes, and application checks are indexed in source-extracts/source-provenance.json. Environment details are in environment.json. Programs are verify_sources.py and build_and_check.py. Commands and outputs are retained in source-verification-output.txt, build-check-output.txt, checks.json, build-diagnostics.json, and build/. Rerun from the supplied workspace with python3 verify_sources.py followed by python3 build_and_check.py.\n\nBuild evidence. The existing pdfTeX installation reports TeX Live 2025/dev/Debian. Each of the two final pdflatex passes used -interaction=nonstopmode -halt-on-error -file-line-error and exited 0. Both final logs report no warnings, no errors, and no overfull or underfull boxes. The resulting PDF has 10 pages and 340,845 bytes. Exact-rational diagnostic samples also verify the displayed interstage arithmetic; the general identity is proved algebraically in n1. None of these checks establishes mathematical correctness.\n\nRemaining original obligations. Results n1–n3 are partial. They do not regularize all arbitrary noninvariant classical psh sheaf germs on nonsaturated higher-dimensional charts. They do not establish a general sharp necessary-and-sufficient geometric range, settle boundaryless curves with nonzero harmonic Picard quotient, synchronize multibranch normalization, extract arbitrary-target sequences without the positive countability hypothesis, prove strict scalar descent over general bases, or glue independently constructed chart sequences. The saturated-domain assertion n2 must retain its domain-of-definition restriction. No unpublished book premise, preceding campaign work, additional model, subagent, installation, runtime change, network operation, or heavy computation was used.\n\nThe retained status.json has exactly id, status, exact_result, proof_file, concrete_gaps, with status partial. The entire original P02.4 target and its sharp requested range are not solved; candidate remains false.\n\nArtifacts: /workspace/research/campaigns/round-44/P02.4-public-source-decreasing-ordinary-smooth/artifacts/codex-QKCSac",
    "support": [
      "n1",
      "n2",
      "n3"
    ]
  }
]

# Published source versions and application checks

{
  "sources": [
    {
      "public_source": "https://arxiv.org/pdf/2506.13548v2",
      "pdf": "/workspace/research/shared-sources/GR-2506.13548v2-20261004.pdf",
      "pdf_sha256": "83ca9a19394f44bb2e4e1aa316de95938f311acd53a00fe250fa0f605184b726",
      "literal_extract": "/workspace/research/shared-sources/GR-2506.13548v2-20261004.txt",
      "extract_sha256": "3a221b86116604c950db07e4c60ab184701f0624deebabd92502e5c81871436b",
      "origin": "Published primary mathematical source, not generated research.",
      "pdf_actual_sha256": "83ca9a19394f44bb2e4e1aa316de95938f311acd53a00fe250fa0f605184b726",
      "extract_actual_sha256": "3a221b86116604c950db07e4c60ab184701f0624deebabd92502e5c81871436b",
      "selected_literal_extracts": [
        {
          "file": "source-extracts/GR-ordinary-psh-classical-comparison.txt",
          "first_line": 84,
          "last_line": 112,
          "sha256": "8dde73079a3acb62b810c4cf5d9e682582f43d78fe15585d8f03e86c96bb39f0"
        },
        {
          "file": "source-extracts/GR-curve-definition-properties.txt",
          "first_line": 453,
          "last_line": 546,
          "sha256": "e052fbc3333209ef58059a97c00c7ad39970105e77aefb1d03dce50d7a32d6b4"
        },
        {
          "file": "source-extracts/GR-boundary-proof.txt",
          "first_line": 669,
          "last_line": 782,
          "sha256": "40ef74f339a775d33bc81510b2e33493df288dae8b3b271324c34104b6dcebd5"
        },
        {
          "file": "source-extracts/GR-classical-definition-pullbacks.txt",
          "first_line": 1108,
          "last_line": 1185,
          "sha256": "426751f6f98f31f0429322f5b34a9d84a42ed4bb81294f526977ab3c73898d19"
        },
        {
          "file": "source-extracts/GR-local-maximum-proof.txt",
          "first_line": 1618,
          "last_line": 1653,
          "sha256": "e1d6f6e655b46c390302cb4f18b5d0be892c2ff693b461f7f8b5fbc237050c69"
        }
      ]
    },
    {
      "public_source": "https://arxiv.org/pdf/2503.05513",
      "pdf": "/workspace/research/shared-sources/GR-2503.05513-20261004.pdf",
      "pdf_sha256": "2ac2d4bd2016c1692271b1a124013585c903288f5d182081dcdaaf824095eb1b",
      "literal_extract": "/workspace/research/shared-sources/GR-2503.05513-20261004.txt",
      "extract_sha256": "5871a9252fb70f2faf39187e2baf341a42f20412ee66fdc2706b97df90ccba0c",
      "origin": "Published primary mathematical source, not generated research.",
      "pdf_actual_sha256": "2ac2d4bd2016c1692271b1a124013585c903288f5d182081dcdaaf824095eb1b",
      "extract_actual_sha256": "5871a9252fb70f2faf39187e2baf341a42f20412ee66fdc2706b97df90ccba0c",
      "selected_literal_extracts": [
        {
          "file": "source-extracts/GR-PL-curve-comparison.txt",
          "first_line": 798,
          "last_line": 846,
          "sha256": "7590418482ef77bd76436a3fec655ab02637eba28613789efd8963fee5be9732"
        },
        {
          "file": "source-extracts/GR-piecewise-smooth-positivity.txt",
          "first_line": 1250,
          "last_line": 1278,
          "sha256": "9b913516f02be562aa16a8e0ba1beff8b1b21e46c0fc875240352453ecc8ae97"
        }
      ]
    },
    {
      "public_source": "https://theses.hal.science/tel-00010990v1/document",
      "pdf": "/workspace/research/shared-sources/Thuillier-tel-00010990v1.pdf",
      "pdf_sha256": "9c57da951e8dca2676d762e9e8c6ace302675938d72434a5b0390f15af7ea29a",
      "literal_extract": "/workspace/research/shared-sources/Thuillier-tel-00010990v1.txt",
      "extract_sha256": "e82226b3dde6a8088c35e1481bfd43f64bb69ee309b5cfda92c8c927a7885570",
      "origin": "Published primary mathematical source, not generated research.",
      "pdf_actual_sha256": "9c57da951e8dca2676d762e9e8c6ace302675938d72434a5b0390f15af7ea29a",
      "extract_actual_sha256": "e82226b3dde6a8088c35e1481bfd43f64bb69ee309b5cfda92c8c927a7885570",
      "selected_literal_extracts": [
        {
          "file": "source-extracts/Thuillier-all-domain-strict-sites.txt",
          "first_line": 1428,
          "last_line": 1465,
          "sha256": "ae917b650da536a449174bb558a12d489b3e279beece9859ce6efdb963fd6470"
        },
        {
          "file": "source-extracts/Thuillier-Picard-proof.txt",
          "first_line": 3587,
          "last_line": 3722,
          "sha256": "83877341e393ce36adaf5706b714223ced2c97fe265c317b6d8e1a9313dd5be2"
        },
        {
          "file": "source-extracts/Thuillier-lisse-domains.txt",
          "first_line": 4105,
          "last_line": 4217,
          "sha256": "85e5be442e5cc5709ad398f87f6675e8fc14cf14c769558220b2b9400b753ab3"
        },
        {
          "file": "source-extracts/Thuillier-regularization-proof.txt",
          "first_line": 5284,
          "last_line": 5317,
          "sha256": "89bbcb9696c5b82297723cf1be8ebdd8b59a72fd44214f9e719a900ef3c26dfe"
        },
        {
          "file": "source-extracts/Thuillier-scalar-proof.txt",
          "first_line": 5353,
          "last_line": 5375,
          "sha256": "18700086516f2d0ef12a010716768f653cc4ccf8d401d1475490ee7a994c2926"
        }
      ]
    },
    {
      "public_source": "https://arxiv.org/pdf/2111.05741",
      "pdf": "/workspace/research/shared-sources/GJR-2111.05741.pdf",
      "pdf_sha256": "572d51c9f8907dbb814684f7d136612243c0e0b70cddbe6759bb686f0bcfbd42",
      "literal_extract": "/workspace/research/shared-sources/GJR-2111.05741.txt",
      "extract_sha256": "57dfcae1d8dfc25d5ef217f34fabe9e80b679ec2956db1bced3b31bc9afdf8d3",
      "origin": "Published primary mathematical source, not generated research.",
      "pdf_actual_sha256": "572d51c9f8907dbb814684f7d136612243c0e0b70cddbe6759bb686f0bcfbd42",
      "extract_actual_sha256": "57dfcae1d8dfc25d5ef217f34fabe9e80b679ec2956db1bced3b31bc9afdf8d3",
      "selected_literal_extracts": [
        {
          "file": "source-extracts/GJR-15.9-15.11-proofs.txt",
          "first_line": 4047,
          "last_line": 4118,
          "sha256": "c84f7ad7b54253b8f9ea4e2aabb61728c8a620fee0d9c221fccf6f6a9dc5314f"
        }
      ]
    },
    {
      "public_source": "https://www.numdam.org/item/PMIHES_1993__78__5_0/",
      "pdf": "/workspace/research/shared-sources/Berkovich-PMIHES-1993-78-5.pdf",
      "pdf_sha256": "bd864c89ed8b6e8f27a90f459837221549db75afa75554ab51414e17771066af",
      "literal_extract": "/workspace/research/shared-sources/Berkovich-PMIHES-1993-78-5.txt",
      "extract_sha256": "694ba4de951bb7e40c73fa4057e4bed5ce073757690ac7379bb1cbbabaf62c1d",
      "origin": "Published primary mathematical source, not generated research.",
      "pdf_actual_sha256": "bd864c89ed8b6e8f27a90f459837221549db75afa75554ab51414e17771066af",
      "extract_actual_sha256": "694ba4de951bb7e40c73fa4057e4bed5ce073757690ac7379bb1cbbabaf62c1d",
      "selected_literal_extracts": []
    },
    {
      "public_source": "https://arxiv.org/pdf/1204.6277v2",
      "pdf": "/workspace/research/shared-sources/CD-1204.6277v2-20261004.pdf",
      "pdf_sha256": "5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719",
      "literal_extract": "/workspace/research/shared-sources/CD-1204.6277v2-20261004.txt",
      "extract_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085",
      "origin": "Published primary mathematical source, not generated research.",
      "pdf_actual_sha256": "5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719",
      "extract_actual_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085",
      "selected_literal_extracts": [
        {
          "file": "source-extracts/CD-positive-pullback-proof.txt",
          "first_line": 994,
          "last_line": 1025,
          "sha256": "1d86b1e8df981ee4d13eef5c4370f68bf5205aa2c4692a7b798e1063496e40d3"
        },
        {
          "file": "source-extracts/CD-ordinary-positive-representative-proof.txt",
          "first_line": 7337,
          "last_line": 7356,
          "sha256": "da079656b0def2185f9118bd79a575baf01ae64b13dfdef5d3dd81b63129e111"
        },
        {
          "file": "source-extracts/CD-stage-0-stage-1-pullback.txt",
          "first_line": 9724,
          "last_line": 9792,
          "sha256": "e9a136ea4ce39e81cfe61b494ad984a5a707878239b91975dece2414fd4aa804"
        },
        {
          "file": "source-extracts/CD-uniform-sequence-proof.txt",
          "first_line": 9817,
          "last_line": 9864,
          "sha256": "bc9d59b7481367591459bfcaf29a614acbff52794b2aef0d83c2e4c99a566f03"
        },
        {
          "file": "source-extracts/CD-convex-composition-proof.txt",
          "first_line": 9885,
          "last_line": 9928,
          "sha256": "a8a96e8b8d70b292ca5c22092ec171c57d50a13e736f8facd8e8b3fd211113e9"
        },
        {
          "file": "source-extracts/CD-current-positivity-boundaryless.txt",
          "first_line": 9993,
          "last_line": 10025,
          "sha256": "093970c4788240a553f038f54b7fe3f115135c6e3617ae6615b9e587ca6e6cde"
        },
        {
          "file": "source-extracts/CD-ordinary-open-chart-proof.txt",
          "first_line": 21540,
          "last_line": 21578,
          "sha256": "c449a34bead62422ac74bd57523a9aa9851781c7974cbf232aa7c7194df993d4"
        },
        {
          "file": "source-extracts/CD-scalar-integration-proof.txt",
          "first_line": 22153,
          "last_line": 22170,
          "sha256": "1aab07414d553f58b5933b43559ec5213dcd78d9ec200f44fdc5fddcae05541a"
        }
      ]
    },
    {
      "public_source": "https://arxiv.org/pdf/1801.04713v3",
      "pdf": "/workspace/research/shared-sources/Wanner-1801.04713v3-20261004.pdf",
      "pdf_sha256": "8df4a1af5dce69c1ef3a6bad2169997b5d72f8c7ced5f95d8a7dcd33ae6dd1b7",
      "literal_extract": "/workspace/research/shared-sources/Wanner-1801.04713v3-20261004.txt",
      "extract_sha256": "e83a0516614296bc5720c6af22845255031671293dfab9acd05b12284984798f",
      "origin": "Published primary mathematical source, not generated research.",
      "pdf_actual_sha256": "8df4a1af5dce69c1ef3a6bad2169997b5d72f8c7ced5f95d8a7dcd33ae6dd1b7",
      "extract_actual_sha256": "e83a0516614296bc5720c6af22845255031671293dfab9acd05b12284984798f",
      "selected_literal_extracts": [
        {
          "file": "source-extracts/Wanner-field-conventions.txt",
          "first_line": 166,
          "last_line": 181,
          "sha256": "7e7a64f852582ca131711f616fa993fd28bf93abb93752976689d2cd4a873b02"
        },
        {
          "file": "source-extracts/Wanner-lisse-regularization-net.txt",
          "first_line": 250,
          "last_line": 269,
          "sha256": "2790a8875b959ded58f498f041f31a8f62a41dfd4e6153f2e16dd89885c36b7e"
        },
        {
          "file": "source-extracts/Wanner-5.2-proof-5.4-proof-5.5.txt",
          "first_line": 1628,
          "last_line": 1778,
          "sha256": "e73610df0e98c758936d97b0cbacb5a1ef555607c06894dbab1bb2beaa98f525"
        }
      ]
    }
  ],
  "application_checks": [
    {
      "claim": "arbitrary classical curve target -> Thuillier subharmonic or -infinity",
      "source": "GR v2 Definition 3.4, 3.4.2 and 4.1.2",
      "application": "Only on connected smooth strictly analytic boundaryless curve neighborhoods. The identically -infinity case uses constant approximants."
    },
    {
      "claim": "lisse regularization",
      "source": "Thuillier Theorem 3.4.2, literal proof retained",
      "application": "Provides a net, not a sequence. Restrict its continuous terms to one strictly affinoid Y inside the relatively compact open supplied by the theorem."
    },
    {
      "claim": "ordinary smoothing of a lisse term",
      "source": "Wanner Lemma 5.2, complete literal proof retained",
      "application": "K is complete, algebraically closed and nontrivially valued; C smooth proper algebraic; H_C subset ordinary C-infinity. Each selected finite lisse term on the same strictly affinoid Y is subharmonic on Y minus boundary. Obtain a continuous approximant on Y, ordinary smooth and psh on that same interior, uniformly within epsilon_j."
    },
    {
      "claim": "verified concrete sufficient H_C conditions",
      "source": "Wanner Corollary 5.4 proof; Thuillier Theorem 2.3.21 proof",
      "application": "Residue field algebraic over a finite field, or C=P1, or C Mumford. Corollary 5.4 itself only treats finite continuous functions; arbitrary-target extension is proved here using the net and countability."
    },
    {
      "claim": "weakly smooth regularization limitation",
      "source": "GJR Proposition 15.11 and its proof",
      "application": "The conclusion is a decreasing NET of WEAKLY smooth psh functions. The last proof sentence obtains a sequence for a fixed lisse term, not for the original net. Not used as an ordinary smooth regularization theorem."
    },
    {
      "claim": "strict versus all-domain site",
      "source": "Thuillier 2.1.7, Definition 3.2.1, Proposition 3.2.4; GJR 15.8-15.9",
      "application": "Do not infer strict R-PL membership from all-domain lisse membership. The curve argument uses Wanner Lemma 5.2 directly on a strictly affinoid domain, never such a PL identification."
    },
    {
      "claim": "ordinary smoothness and smooth positivity",
      "source": "saved CD v2 Proposition 15.1.1(b), Corollary 15.1.2; Lemma 8.1.4(a); Proposition 8.1.5; Lemma 1.2.11",
      "application": "Use ordinary OPEN charts and local invertible analytic functions. Stage 0 is d-prime d-double-prime >=0; pullback preserves this form positivity. CD Lemma 6.5.1 gives positive tropical representatives, whose pulled images lie in the same paralinéaire support, including after scalar extension. Stage 2 is not substituted for stage 1."
    },
    {
      "claim": "current positivity",
      "source": "saved CD v2 section 8.3 assumption and Proposition 8.3.1; Stokes section 7.7",
      "application": "Assert positive currents on the boundaryless curve interiors and boundaryless proper-fibre products only. Boundary-spike approximants have nonnegative d-prime d-double-prime as forms; no unqualified boundary current positivity assertion is made."
    },
    {
      "claim": "classical boundary spike and pullback",
      "source": "GR v2 Proposition 3.5(3), full proof; 4.1.2; Proposition 4.2(5,6)",
      "application": "A USC spike at the sole boundary point of the disc is zero on its interior, hence classically psh including all analytic field extensions. Pullback to a product is classical psh. This is not a harmonic nonsmoothness argument."
    },
    {
      "claim": "proper fibre constancy",
      "source": "GR v2 Theorem 6.1, full proof",
      "application": "Apply over H(z) to P^m: compact, connected and boundaryless. USC functions attain their maximum; the finite maximum locus is nonempty, closed, and open by Theorem 6.1. Then use a rational section to descend all targets on the saturated domain."
    },
    {
      "claim": "normalization application",
      "source": "GR v2 Proposition 4.2(6); CD ordinary charts",
      "application": "New proof is limited to a finite normalization which is an isomorphism away from one K-rational singular point and has exactly one point over it. Closed bijection -> homeomorphism. Each ordinary smooth term is constant near the rational preimage, so descends as ordinary smooth; no general smooth descent along finite maps is claimed."
    },
    {
      "claim": "Picard/genus limitation",
      "source": "Thuillier Theorem 2.3.21/Lemma 2.3.22; GJR Remark 15.10; Wanner Remark 5.5",
      "application": "Under the precise semistable type-2 setup H_x/F_x = Pic^0(C_x) tensor_Z R. This measures failure of harmonic ordinary smoothness, not failure of decreasing psh approximation. Positive genus alone does not imply nonzero quotient."
    }
  ],
  "pdf_visual_checks": [
    {
      "source": "https://theses.hal.science/tel-00010990v1/document",
      "pdf_page_one_based": 72,
      "image": "source-extracts/Thuillier-PDF-p72.png",
      "fresh_text": "source-extracts/Thuillier-PDF-p72-fresh-pdf-text.txt",
      "review": "Direct visual inspection confirms H_x/F_x = Pic^0(C_x) tensor_Z R, in the geometrically connected proper semistable type-2 setup; theorem conditions are residue field algebraic over a finite field or geometric local P1."
    },
    {
      "source": "https://theses.hal.science/tel-00010990v1/document",
      "pdf_page_one_based": 73,
      "image": "source-extracts/Thuillier-PDF-p73.png",
      "fresh_text": "source-extracts/Thuillier-PDF-p73-fresh-pdf-text.txt",
      "review": "Direct visual inspection confirms the Picard quotient and the torsion criterion. The PDF really says the group is finite in its final bullet; that stronger claim is not used. The needed torsion assertion follows because each individual point is defined over a finite field and belongs to its finite rational-point group."
    },
    {
      "source": "https://arxiv.org/pdf/2111.05741",
      "pdf_page_one_based": 80,
      "image": "source-extracts/GJR-PDF-p80.png",
      "fresh_text": "source-extracts/GJR-PDF-p80-fresh-pdf-text.txt",
      "review": "Direct visual inspection confirms Proposition 15.11 says decreasing net of weakly smooth psh functions, not a sequence and not ordinary smooth."
    }
  ]
}

## https://arxiv.org/pdf/2506.13548v2 84--112

   To get regularization by smooth psh functions in the sense of Chambert-Loir and Ducros
or to define a Monge–Ampère measure for psh functions, additional hypotheses as in
[CD25] might be needed, but that is not the subject of this paper.

1.1. Subharmonic functions on arbitrary k-analytic curves. In Section 3, we define
subharmonic functions on any k-analytic curve X to be the elements of the following
subsheaf of the sheaf of upper semicontinuous functions on X with range [−∞, ∞).
It is the smallest subsheaf that is functorial with respect to pullback, stable under base
change, and agrees with Thuillier’s subharmonic functions on smooth k-analytic curves.
We will show in Proposition 3.5 that subharmonic functions satisfy the properties (1)–(3)
as in the complex case, and the local maximum principle on the interior Int(X ) = X \ ∂ X .

1.2. Plurisubharmonic functions on k-analytic spaces. We define classically plurisub-
harmonic functions on k-analytic spaces as the elements of the smallest subsheaf of the
sheaf of upper semicontinuous functions with range [−∞, ∞) that is functorial with
             CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES              3

respect to pullback, stable under base change, and agrees with the above defined sheaf
of subharmonic functions on k-analytic curves. In Section 4, we will show that classically
psh functions satisfy properties (1)–(3).
   We use the terminology classically psh to distinguish from the psh functions introduced
by Chambert-Loir and Ducros in [CD25]. Note that psh functions are classically psh.
Indeed, psh functions are upper semi-continuous and the definition is functorial, so we
are reduced to the case of a smooth analytic curve C. We have to see that a psh function
is subharmonic. By base change, we may assume that k is algebraically closed and non-
trivially valued, see Proposition 3.5(7). Since subharmonic functions are stable under
decreasing limits, and the psh functions are defined by a transfinite regularization process
from smooth psh functions, it is enough to show that a smooth psh function on C is
subharmonic. This follows from a result of Wanner [Wan19, Theorem 4.7].


## https://arxiv.org/pdf/2506.13548v2 453--546

  In this section, we generalize Thuillier’s theory [Thu05] of subharmonic functions from
smooth strictly analytic curves to arbitrary k-analytic curves.
3.1 (k-Analytic Curves). By a k-analytic curve we mean a separated k-analytic space of
pure dimension 1. We gather the following facts about k-analytic curves:
   (1) A k-analytic curve is good, i.e., every point has an affinoid neighborhood. [Duc24,
        Proposition 3.3.7]
   (2) A k-analytic curve is paracompact. [Duc24, Théorème 4.5.10]
   (3) If X is an affinoid k-analytic curve, then ∂ X coincides with the Shilov boundary
        of X . [Thu05, 2.1.2]
An analytic domain in a k-analytic curve (for example, an open subset) is again a k-
analytic curve.
3.2 (Thuillier’s Harmonic Functions). Thuillier [Thu05, §2.3] defines a sheaf of harmonic
functions on a smooth, strictly k-analytic curve for a non-trivially valued k, roughly as
follows. If X is affinoid, then a continuous function h: X → R is harmonic if, after passing
to a finite, separable field extension, it coincides with the composition of a harmonic
function on a skeleton of X (in the sense of graph theory) with the retraction to the
skeleton. If X is smooth, then a harmonic function on an open subset of X is defined to be
a continuous function whose restriction to every strictly affinoid subdomain is harmonic.
3.3 (Thuillier’s Subharmonic Functions). For a non-trivally valued k, Thuillier [Thu05,
Définition 3.1.5] defines a subharmonic function on a smooth, strictly k-analytic curve X
to be an upper semicontinuous function u: X → R ∪ {−∞} that is not identically −∞
on any connected component of X and that satisfies the following property: for every
strictly k-affinoid domain U ⊂ X and every harmonic function h: U → R, if u ≤ h on ∂ U
then u ≤ h on U.
  Now we extend this definition to the case of non-smooth curves. The idea is that a
function should be subharmonic if it pulls back to a subharmonic function along any
morphism from a smooth curve. However, an inseparable curve over an imperfect field
does not admit any non-constant morphisms from a smooth curve, so one has to allow
an extension of scalars as well. We also consider the constant function −∞ to be sub-
harmonic, following Demailly [Dem85] in the complex case.
Definition 3.4 (Subharmonic functions). Let X be a k-analytic curve and let u: X →
R ∪ {−∞} be an upper semicontinuous function. We say that u is subharmonic provided
that, for every non-trivially valued analytic extension field k′ /k, every smooth, connected,
strictly k′ -analytic curve Y , and every morphism Y → X k′ , the composition
                                        πk′ /k     u
                              Y −→ X k′ −→ X −→ R ∪ {−∞}
             CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES              11

is either subharmonic on Y in the sense of [Thu05, Définition 3.1.5], or is identically −∞.
3.4.1. If X is a smooth, connected, strictly k-analytic curve over a non-trivially valued k,
then an upper semicontinuous function u: X → R ∪ {−∞} is subharmonic in our sense
if and only if it is either subharmonic in Thuillier’s sense or is identically −∞. Indeed, if
u is subharmonic in our sense then one can take k = k′ and Y = X to see that it is either
subharmonic in Thuillier’s sense or is identically −∞. Conversely, if u is identically −∞
then it is clearly subharmonic in our sense, and if u is subharmonic in Thuillier’s sense
then it is subharmonic in our sense by [Thu05, Proposition 3.1.14 and Corollaire 3.4.5].
3.4.2. As a special case of (3.4.1), if X is a smooth, connected, strictly k-analytic curve
over a non-trivially valued k, then a function u: X → R (taking finite values) is subhar-
monic in our sense if and only if it is subharmonic in Thuillier’s sense.
  Here we collect the basic properties of subharmonic functions, which we will prove
over the course of this section.
Proposition 3.5. Let X be a k-analytic curve and let u: X → R ∪ {−∞} be an upper
semicontinuous function.
   (1) (Sheafiness) The subharmonic functions form a sheaf on X .
   (2) (Analytic functions) If f ∈ Γ (X , OX ) then log | f | : X → R ∪ {−∞} is subharmonic.
   (3) (Boundaries) If u is subharmonic on Int(X ), then u is subharmonic on X .
   (4) (Cone Property) If u1 , u2 : X → R ∪ {−∞} are subharmonic and λ1 , λ2 ∈ R≥0 then
       λ1 u1 + λ2 u2 and max{u1 , u2 } are subharmonic.
   (5) (Limits) The infimum of a decreasing net of subharmonic functions is subharmonic.
   (6) (Maximum Principle) If u is subharmonic and u attains a local maximum at x ∈
       Int(X ), then u is constant in a neighborhood of x.
   (7) (Extension of scalars) Let k′ /k be an analytic extension field. Then u is subharmonic
       if and only if u ◦ πk′ /k : X k′ → R ∪ {∞} is subharmonic.
   (8) (Functoriality) Let Y be a k-analytic curve and let f : Y → X be a morphism. If u
       is subharmonic then u ◦ f is subharmonic, and the converse holds if f is finite and
       surjective.
   (9) (Finite Values) If u is subharmonic and u(x) = −∞ for a non-rig-point x ∈ X ,
       then u ≡ −∞ on the irreducible component of Int(X ) ∪ {x} containing x.
  Let us make some remarks regarding the content of Proposition 3.5.
3.5.1. If U ⊂ X is an open subset then U is again a k-analytic curve, so it makes sense
to speak of subharmonic functions on U. It is immediate from the definition that a sub-
harmonic function on X restricts to a subharmonic function on U. Hence subharmonic
functions form a presheaf on X . Proposition 3.5(1) asserts that this presheaf is a sheaf.
3.5.2. The maximum principle (Proposition 3.5(6)) is [Thu05, Proposition 3.4.10] in the
smooth, strictly analytic case.
3.5.3. In the situation of Proposition 3.5(7), it is immediate from Definition 3.4 that
u ◦ πk′ /k is subharmonic when u is subharmonic. This is the difficult direction in the
smooth, strictly analytic case: see [Thu05, Corollaire 3.4.5]. This result is hidden in the
12                                 W. GUBLER AND J. RABINOFF

fact that Definition 3.4 essentially recovers Thuillier’s definition of subharmonicity in that
case 3.4.1.
3.5.4. In the situation of Proposition 3.5(8), it is immediate from Definition 3.4 that u◦ f
is subharmonic when u is subharmonic. The remark in 3.5.3 applies to a lesser extent in
this case: see [Thu05, Proposition 3.1.14].
3.5.5. For any x ∈ X , the subset Int(X )∪{x} is open in X . This is obvious if x ∈ Int(X ), and
if x ∈ ∂ X then it follows from the fact that ∂ X is discrete in X . In particular, Int(X ) ∪ {x}
is again a k-analytic curve, so it makes sense to speak of its irreducible components
in Proposition 3.5(9). Irreducible components can only meet at rig-points (their inter-
sections are Zariski-closed), so a non-rig-point x is contained in a unique irreducible
component of Int(X ) ∪ {x}; this is implicit in Proposition 3.5(9).
3.5.6. Proposition 3.5(9) implies that if u is subharmonic and u(x) = −∞ for a non-rig-
point x ∈ X , then u ≡ −∞ in a neighborhood of x.
3.6. In order to extend Thuillier’s results, we will pass from a k-analytic curve to a


## https://arxiv.org/pdf/2506.13548v2 669--782

  We will use the following lemma in the proofs of Proposition 3.5(3,9). If X is a k-
analytic space and k′ /k is an analytic extension field, then π−1
                                                               k′ /k
                                                                     (x) = M (H (x)⊗
                                                                                   b k k′ )
has a finite Shilov boundary for any Abhyankar point x ∈ X by [Duc24, 3.2.14]; we
denote this boundary by x [k′ ] .

Lemma 3.10. Let X be a k-analytic curve and let k′ /k be an analytic field extension. Then
for all x ∈ ∂ X we have (∂ X k′ ) ∩ π−1
                                     k′ /k
                                           (x) = x [k′ ] .

Proof. Replacing X by an affinoid neighborhood of x, we may assume that X = M (A )
is affinoid. By a result of Ducros [Duc12, Lemme 3.1], there exists a morphism g : X →
B1 (0, s) for some s ∈ R>0 such that x ∈ g −1 (ηs ), where ηs is the maximal point of B1 (0, s).
                CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES                                 15

This is discussed in detail in Section 6. Consider the commutative square

                                                          g′
                                                           → B1k′ (0, s)
                                                      ←
                                               X k′




                                                ←




                                                                  ←
                                           πk′ /k                   πk′ /k




                                                                 →
                                               →
                                                          g → B (0, s).
                                                      ←        1
                                                X

Since ∂ B1k′ (0, s) contains (only) its maximal point ηs,k′ , we have (g ′ )−1 (ηs,k′ ) ⊂ ∂ X k′
by (2.11.4) (which is an equality because B1k′ (0, s) is separated). The morphism g is an
Abhyankar presentation of x in the sense of [Duc24, 3.2.12.2], so by Proposition 3.2.13
of ibid, we have x [k′ ] = (g ′ )−1 (ηs,k′ ) ∩ π−1
                                                k′ /k
                                                      (x) ⊂ (∂ X k′ ) ∩ π−1
                                                                         k′ /k
                                                                               (x).
   For the reverse inclusion, let x ∈ (∂ X k′ ) ∩ πk′ /k (x), and suppose that x ′ ∈
                                        ′                   −1
                                                                                         / x [k′ ] . Since
∂ X k′ is the Shilov boundary of X k′ = M (A ⊗         b k k ), by [Ber90, Corollary 2.4.5] there exist
                                                            ′

f ∈ A⊗   b k k and ϵ > 0 such that | f | attains its maximum value at x ′ and such that
              ′

                          
                            y ∈ X k′ | f ( y)| > | f (x ′ )| − ϵ ⊂ X k′ \ x [k′ ] .

In particular, the restriction of f to π−1
                                        k′ /k
                                              (x) does not attain its maximum value on x [k′ ] ,
which cannot happen. Thus x ∈ x [k′ ] , so (∂ X k′ ) ∩ π−1
                                 ′
                                                         k′ /k
                                                               (x) ⊂ x [k′ ] .             □

Proof of Proposition 3.5(3). Suppose that u is subharmonic on Int(X ). Let k′ /k be an
analytic extension field with k′ non-trivially valued, let Y be a smooth, connected, strictly
k′ -analytic curve, and let f : Y → X k′ be a morphism. We must prove that u ◦ πk′ /k ◦
f is subharmonic in Thuillier’s sense or is identically −∞. Since ∂ Y = ;, it follows
from 2.11(4) that f (Y ) ⊂ Int(X k′ ). If πk′ /k ◦ f (Y ) ⊂ Int(X ) then u◦πk′ /k ◦ f is subharmonic
in Thuillier’s sense or is identically −∞ because u is subharmonic on Int(X ). Suppose
then that πk′ /k ◦ f ( y) = x ∈ ∂ X for some y ∈ Y , so that f ( y) ∈ Int(X k′ ) ∩ π−1                 k′ /k
                                                                                                             (x).
    We claim that πk′ /k (x)∩Int(X k′ ) is both open and closed in Int(X k′ ). By [Duc24, Propo-
                         −1

sition 5.3.4], if U is a connected component of π−1               k′ /k
                                                                        (X \ {x}), then the closure of U in
X k′ is contained in πk′ /k (X \ {x}) ∪ x [k′ ] . Let U be the connected component of X k′ \ x [k′ ]
                            −1                                ′

containing U. The above shows that U is closed in U ′ . Since U is open in X (an analytic
space is locally connected [Ber93, Remark 1.2.4(iii)] and hence its connected compo-
nents are open [Sta21, Lemma 04ME]), it is open in U ′ , so U = U ′ since U ′ is connected.
Hence π−1  k′ /k
                 (X \ {x}) is a union of connected components of X k′ \ x [k′ ] , so the same is
true of πk′ /k (x) \ x [k′ ] . Since X k′ \ x [k′ ] is itself a k-analytic space as x [k′ ] is a finite set, its
           −1

connected components are open, so we conclude that π−1                       k′ /k
                                                                                   (x) \ x [k′ ] is open and closed
in X k′ \ x [k′ ] . Since x ∈ ∂ X , we have (πk′ /k (x)) ∩ ∂ X k′ = x [k′ ] by Lemma 3.10, which
                                                         −1

shows Int(X k′ ) ⊂ X k′ \ x [k′ ] and π−1   k′ /k
                                                  (x) \ x [k′ ] = π−1 k′ /k
                                                                            (x) ∩ Int(X k′ ). We conclude that
πk′ /k (x) \ x [k′ ] is both open and closed in Int(X k′ ), as claimed.
  −1

    Since Y is connected, f (Y ) ⊂ Int(X k′ ), and f ( y) ∈ Int(X k′ ) ∩ π−1            k′ /k
                                                                                              (x), we deduce from
the above claim that f (Y ) ⊂ Int(X k′ )∩πk′ /k (x). Hence πk′ /k ◦ f is constant, so u◦πk′ /k ◦ f
                                                      −1

is constant. It follows that u is subharmonic in Thuillier’s sense or is identically −∞. □


## https://arxiv.org/pdf/2506.13548v2 1108--1185

Definition 4.1 (Classically Plurisubharmonic Functions). Let X be a k-analytic space and
let u: X → R ∪ {−∞} be an upper semicontinuous function. We say that u is classically
plurisubharmonic or classically psh provided that, for every analytic extension field k′ /k,
every k′ -analytic curve Y , and every morphism f : Y → X k′ , the function u◦πk′ /k ◦ f : Y →
R ∪ {−∞} is subharmonic on Y in the sense of Definition 3.4.
4.1.1. Any class of psh functions should respect extension of scalars and should be stable
under pullback, so the conditions in Definition 4.1 are necessary. In complex analysis,
this condition (without the extension of scalars) is the definition of plurisubharmonicity,
which is why we call the notion “classically psh”.
4.1.2. If X is a k-analytic curve, then a function u: X → R∪{−∞} is classically psh if and
only if it is subharmonic. Indeed, if u is classically psh then taking k′ = k and Y = X in
Definition 4.1 shows that u is subharmonic, and if u is subharmonic then it is classically
psh by Proposition 3.5(7,8).
4.1.3. In Definition 4.1, one can assume that Y is a connected, smooth, strictly k′ -analytic
curve: this follows from Definition 3.4.
  Classically psh functions satisfy the basic properties of subharmonic functions on curves.
Proposition 4.2. Let X be a k-analytic space.
   (1) (Sheafiness) The classically psh functions form a sheaf on X .
   (2) If f ∈ Γ (X , OX ) then log | f |: X → R ∪ {−∞} is classically psh.
   (3) (Cone Property) If u1 , u2 : X → R∪{−∞} are classically psh and λ1 , λ2 ∈ R≥0 then
       λ1 u1 + λ2 u2 and max{u1 , u2 } are classically psh.
   (4) (Limits) The infimum of a decreasing net of classically psh functions is classically
       psh. For arbitrary pointwise limits, we refer to Theorem 6.5.
   (5) (Extension of Scalars) Let k′ /k be an analytic extension field. A function u: X →
       R ∪ {−∞} is classically psh if and only if u ◦ πk′ /k : X k′ → R ∪ {−∞} is classically
       psh.
   (6) (Functoriality) Let Y be a k-analytic space and let f : Y → X be a morphism. If
       u: X → R ∪ {−∞} is classically psh then u ◦ f is classically psh, and the converse
       holds if f is finite and surjective.
Proof. Properties (1,3,4) follow immediately from Proposition 3.5(1,4,5). For Proposi-
tion 4.2(2), we consider an analytic function f on X . As | f | is continuous, we deduce
22                                  W. GUBLER AND J. RABINOFF

that log | f | is a continuous function with values in R ∪ {−∞} and hence it is upper semi-
continuous. Then Proposition 4.2(2) follows from Proposition 3.5(2).
    To prove Proposition 4.2(5), it is clear from the definitions that if u is classically psh,
then u ◦ πk′ /k is classically psh for every analytic extension field k′ /k. To prove the con-
verse, we assume that k′ /k is an analytic extension field and that u′ := u ◦ πk′ /k is a
classically psh function on X k′ . Since the morphism πk′ /k is closed and surjective 2.9,
it is clear that u is upper semicontinuous. Let k′′ /k be an analytic extension field and
let f : Y → X k′′ be a morphism over k′′ from a k′′ -analytic curve Y . We have to show
that u ◦ πk′′ /k ◦ f is subharmonic. As in the proof of Proposition 3.5(7), we consider
a simultaneous analytic extension field K of k′ and k′′ . It follows from the above that
u ◦ πK/k = u′ ◦ πK/k′ is classically psh and hence u ◦ πK/k ◦ f K is subharmonic. We con-
clude from the commutative diagram (3.10.1) that u ◦ πK/k ◦ f K = u ◦ πk′′ /k ◦ f ◦ πK/k′′ is
subharmonic and hence u ◦ πk′′ /k ◦ f is subharmonic by Proposition 3.5(7).
    Likewise, the proof of Proposition 4.2(6) follows the same lines as the proof of Propo-
sition 3.5(8). Again, it follows from the definitions if u is a classically psh function on X ,
then u ◦ f is a classically psh function on Y . Conversely, we assume that u ◦ f is a clas-
sically psh function for a finite surjective morphism f : Y → X . Since finite morphisms
are proper and hence closed, we deduce from upper semicontinuity of u ◦ f and from
surjectivity of f that u is upper semicontinuous. It remains to show that u ◦ πk′ /k ◦ g is
subharmonic for any analytic extension field k′ /k and any morphism g : Z → X k′ from a
connected k′ -analytic curve Z. Setting W := Z ×X k′ Yk′ , we get a morphism g ′ : W → Yk′
from f by base change with respect to f ′ : Yk′ → X k′ as in (3.10.2). Since u ◦ f is classi-
cally psh, it follows from Proposition 4.2(5) that u ◦ πk′ /k ◦ f ′ = u ◦ f ◦ πk′ /k is classically
psh. The morphism f is finite and surjective, hence the same holds for f ′ . We con-
clude that the base change f ′′ : W → Z of the morphism f ′ is finite and surjective. The
k′ -analytic space W has irreducible components of dimension 1 and maybe isolated irre-
ducible components of dimension 0. Removing the latter, we obtain a k′ -analytic curve
W ′ as an open and closed subset of W . Since Z is a connected k′ -analytic curve and f ′′
is a finite surjective map from W onto Z, we get an induced finite surjective morphism
W ′ → Z. Indeed, as W ′ is also Zariski-closed in W , we deduce from finiteness of f ′′ that
f ′′ (W ′ ) is a Zariski-closed subset in Z of dimension 1 and hence f ′′ (W ′ ) = Z as Z is a
connected k′ -analytic curve. Since the inclusion W ′ → W is obviously finite, the com-
position W ′ → Z is also finite. In the following, we replace W by W ′ , which preserves
the commutativity of the diagram (3.10.2) and has the advantage that W is a k′ -analytic
curve. It follows that u ◦ πk′ /k ◦ f ′ ◦ g ′ = u ◦ πk′ /k ◦ g ◦ f ′′ is subharmonic on W . The
morphism of k′ -analytic curves f ′′ : W → Z is finite and surjective, so we deduce from
Proposition 3.5(8) that u ◦ πk′ /k ◦ g is subharmonic.                                           □

  In the paper [GR25], we have studied semipositive R-PL functions on a good strictly
k-analytic space over a non-trivially valued non-archimedean field k. This turns out to
be the same as an R-PL function that is classically psh, as we now show.

Theorem 4.3. Suppose that the valuation on k is nontrivial. Let X be a good, strictly k-
analytic space and let h: X → R be an R-PL function. Then h is semipositive if and only if h
is classically psh.


## https://arxiv.org/pdf/2506.13548v2 1618--1653

local maximum principle holds for classically psh functions, and then we will show a
global maximum principle in the affinoid case; more specifically, that that a classically
psh function takes its global maximum at a Shilov point.
Theorem 6.1 (Local Maximum Principle). Let X be a k-analytic space and let u be a clas-
sically psh function on X . If u has a local maximum at x ∈ Int(X ), then u is locally constant
at x.
Proof. We may replace X by a connected, Hausdorff open neighborhood of x in Int(X ) to
assume that X is connected and boundaryless and that u attains a global maximum at x.
Let R = u(x). Let Γ be a connected, overconvergent analytic curve in X containing x. We
claim that u ≡ R on Γ . Consider the set Γu=R = {z ∈ Γ | u(z) = R}. This set is closed in Γ
by upper semicontinuity of u, so since Γ is connected, it suffices to show that Γu=R is open
in Γ .
   By 5.1.3, there exist an analytic extension field k′ /k, a compact, separated strictly k′ -
analytic space C of dimension at most 1, a separated strictly k′ -analytic space C ′ of dimen-
sion at most 1, and morphisms ψ: C → C ′ and ϕ ′ : C ′ → X k′ , such that ψ(C) ⊂ Int(C ′ )
and πk′ /k ◦ ϕ(C) = Γ , where ϕ = ϕ ′ ◦ ψ. The composition u ◦ πk′ /k ◦ ϕ ′ is subharmonic
on 1-dimensional connected components of C ′ because u is classically psh.
   Let y ∈ Γu=R , let z ∈ C be a point lying over y, and let z ′ = ψ(z) ∈ Int(C ′ ), so that
R = u ◦ πk′ /k ◦ ϕ ′ (z ′ ) = u ◦ πk′ /k ◦ ϕ(z). If {z ′ } is a connected component of C ′ then clearly
u ◦ πk′ /k ◦ ϕ ′ ≡ R in a neighborhood of z ′ . Otherwise, the connected component of z ′
in C ′ is a strictly k′ -analytic curve, in which case u ◦ πk′ /k ◦ ϕ ′ ≡ R in a neighborhood
of z ′ by Proposition 3.5(6) (here we use z ′ ∈ Int(C ′ )). Taking the ψ-inverse image of
such a neighborhood, we see that u ◦ πk′ /k ◦ ϕ ≡ R in a neighborhood of z. Applying
this argument to each z ∈ (πk′ /k ◦ ϕ)−1 ( y), we construct an open set V ⊂ C containing
(πk′ /k ◦ ϕ)−1 ( y) such that u ◦ πk′ /k ◦ ϕ|V ≡ R.
   The complement C \ V is a closed subset of the compact space C, so it is a compact
subset of C that is disjoint from (πk′ /k ◦ ϕ)−1 ( y). Its image is a compact subset of X that
does not meet y, so there is an open neighborhood W of y such that (πk′ /k ◦ϕ)−1 (W ) ⊂ V .
              CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES                     31

It follows that u ≡ R on W ∩ Γ . This proves that Γu=R is open in Γ . As remarked above,
this yields u ≡ R on Γ .
   Let y ∈ X be any point. By Theorem 5.4, there is a connected, overconvergent analytic
curve Γ in X containing x and y. We showed above that u ≡ R on Γ , so that u( y) = R.
As y was arbitrary, we have u ≡ R on X .                                              □



## https://arxiv.org/pdf/2503.05513 798--846

neighborhood U of z in W , a point z ∈ W with reduction η, and a d-dimensional Zariski-
closed subspace Y ⊂ U with z ∈ Y . It follows that centdim(X , z) ≤ d, and equality holds
by Remark 4.2.                                                                            
     ON SEMIPOSITIVE PIECEWISE LINEAR FUNCTIONS IN NON-ARCHIMEDEAN ANALYTIC GEOMETRY         15

                             5. SEMIPOSITIVE R-PL FUNCTIONS
   Let k be a non-trivially valued non-Archimedean field. We consider a good, strictly
k-analytic space X . We refer to 2.5 for the definition of PL functions. Recall from the in-
troduction that an R-PL function u: X → R is called semipositive at x ∈ X if the associated
residue line bundle Lu (x) ∈ Pic(red(X , x))R is nef, where we refer to [GJR21, 6.16–6.19]
for residue line bundles. Equivalently, there is a strictly affinoid neighbourhood U of x
such that u = hL for a formal k◦ -model (U, L) of (U, OU ) with L nef [GJR21, Proposition
7.1].
   We will show first that for an R-PL function on a smooth curve, semipositivity is the
same as subharmonicity in the sense of Thuillier’s thesis [Thu05, Définition 3.1.5]. Re-
call that Thuillier defines a subharmonic function on a smooth k-analytic curve X as a
semicontinuous function u: X → R ∪ {−∞} which is not identically −∞ on any con-
nected component of X and which has the property that for every harmonic function h
on a strictly affinoid domain U of X with u|∂ U ≤ h|∂ U , we have u|U ≤ h.

Proposition 5.1. Let X be a smooth, strictly k-analytic curve and let u: X → R be an R-PL
function. Then u is subharmonic at x ∈ X in the sense of Thuillier if and only if Lu (x) is nef.

Proof. First we treat the case when k is algebraically closed. As explained in 2.5, there
exists a compact strictly analytic neighborhood U of x in X , a formal k◦ -model U of U,
and a formal model L of OU such that u|U = hL . Since k is algebraically closed, we may
assume that the special fiber Us is reduced, which implies that U is covered by formal
affines of the form Spf(A ◦ ) for a strictly k-affinoid algebra A [GJR21, §2.4]. It follows
from [Ber90, Proposition 2.4.4] that for every irreducible component Y of Us , there is a
unique point ξY ∈ U reducing to the generic point of Y . In the formalism of real valued
forms and currents on Berkovich spaces [CD12], it is well known that d′ d′′ [u]|U is the
discrete measure on U supported on the points ξY of U for Y an irreducible component
of Us , with multiplicity at ξY equal to degL (Y ). See [CD12, §6.9] for a more general
statement. Wanner showed that subharmonicity of u on U is equivalent to the positivity
of the current d′ d′′ [u]: see [Wan19, Theorems 1 and 2] and use the fact that X is locally
algebraic [vdP80]. Thus Ls is nef if and only if u is subharmonic on U. Suppose that u is
subharmonic at x. Shrinking U, we may assume that u is subharmonic on U. This implies
that Ls is nef, so it follows from [GJR21, Proposition 7.1] that Lu (x) is nef. Conversely, if
Lu (x) is nef, then by [GJR21, Proposition 7.1], we may shrink U so that Ls is nef, which
as above implies that u is subharmonic on U.
   It remains to show that subharmonicity of u at x and numerical effectivity of Lu (x)
can be checked after extending scalars to the completion of an algebraic closure K =
(k)∧ . By [GJR21, Proposition 7.6(2)], one can check that Lh (x) is nef after base change
to K. The same is true for subharmonicity: this follows directly from Thuillier’s definition
and the fact that the base change of a harmonic function remains harmonic [Thu05,
Proposition 2.3.18].                                                                       

  Our next goal is a characterisation of semipositive R-PL functions by restriction to
subcurves as in the complex case. We need the following characterization of boundary


## https://arxiv.org/pdf/2503.05513 1250--1278

24                                W. GUBLER AND J. RABINOFF

non-negative smooth weight functions. It follows from 7.2 that f ′ is weakly tropically
psh.                                                                                 
7.5. Let X be a good strictly analytic space over k. Recall that Chambert–Loir and Ducros
[CD12] introduced (real valued) smooth (p, q) forms on X by using pull-backs of smooth
Lagerberg forms with respect to smooth tropicalization maps and a sheafification process.
This leads to a bigraded sheaf of smooth forms on X with natural differentials d′ and d′′ .
   Replacing smooth Lagerberg forms by piecewise smooth Lagerberg forms, the same
process leads to a bigraded sheaf of piecewise smooth forms on X with differentials d′P
and d′′P . More explicitly, in an affinoid neighborhood U of a point of x, a piecewise smooth
form is equal to the pullback of a piecewise smooth Lagerberg form α under a smooth
tropicalization map ϕtrop : U → Rn . See [GJR21, Section 10] for more details.
   The piecewise smooth forms of bidegree (0, 0) are special continuous functions which
we call piecewise smooth functions. It is clear that every R-PL function is a piecewise
smooth function where we choose all the ωi ’s above to be affine functions.
7.6. Chambert-Loir and Ducros introduce currents on a separated good strictly analytic
space X as a dual notion to smooth forms [CD12, Section 4]. These also form a bigraded
sheaf with natural differentials d′ and d′′ . For any continuous function h: X → R, there is
an associated current [h] defined by integrating h against compactly supported smooth
forms, as explained in [CD12, §5.4]. The function h is called plurisubharmonic (or psh
for short) if d′ d′′ [h] is a positive current. See [CD12, §5.5] for details.
  Note that plurisubharmonicity is a local property, so it is defined even without assuming
X to be separated.
  By [GJR21, Theorem 7.14], a semipositive R-PL function is a plurisubharmonic piece-
wise smooth function in this sense.
     We prove now the maximum principle for piecewise smooth psh functions.
Theorem 7.7. Let X be a good strictly analytic space over K and let h be a piecewise smooth
psh function on X . If h has a local maximum at x ∈ X \ ∂ X , then h is locally constant at x.


## https://theses.hal.science/tel-00010990v1/document 1428--1465

Les sites XG et XR .
   La dénition des espa es k-analytiques présentée dans [3℄ et étendue dans [4℄ est telle que la
notion de domaine anoïde dans un espa e k-analytique soit bien dénie (exa tement omme
la notion de sous-polytope d'un polyèdre).
   De manière générale, une partie Y d'un espa e k-analytique X est un domaine k-analytique
si elle admet un re ouvrement lo alement ni par des domaines k-anoïdes. Le G-site de X
20



est la atégorie XG dont les objets sont les domaines k-analytiques de X et les morphismes les
in lusions, munie de la topologie de Grothendie k pour laquelle les familles ouvrantes sont
les re ouvrement pouvant être ranés en un re ouvrement lo alement ni par des domaines
k-anoïdes. La orrespondan e
                                           V 7→ AV ,
où V est un domaine k-anoïde de X et AV est l'algèbre de V , se prolonge en un fais eau
OX sur le G-site XG de X , le fais eau stru tural de X .
   Notons |X| l'espa e topologique sous-ja ent à X ainsi que le site anoniquement asso ié ;
tout point de X admettant un système fondamental de voisinages formé par des domaines
k-analytiques ompa ts, tout ouvert de |X| est la réunion d'une famille lo alement nie de
domaines k-anoïdes et détermine don un objet de XG . On dénit ainsi une è he
                                      πX : XG → |X| ;
 'est un morphisme de sites.
   Un domaine stri tement k-analytique est une partie de X admettant un re ouvrement
lo alement ni par des domaines stri tement k-anoïdes. Lorsque X est un espa e stri tement
k-anoïde (au sens de [4℄, 'est-à-dire tel que tout point admette un système fondamental
de voisinages formé de domaines stri tement k-analytiques ompa ts), nous appelerons site
rigide de X et noterons XR , la sous- atégorie pleine de XG dont les objets sont les domaines
stri tement k-analytiques, munie de la topologie de Grothendie k induite.
Remarque 2.1.7.  Le préfais eau
                                       Y ; C0 (|Y |, R)
sur le site XG est un fais eau : en eet, une fon tion ϕ sur un espa e topologique X est
 ontinue s'il existe un re ouvrement lo alement ni de X par des fermés F tels que ϕ|F soit
 ontinue.
Convention.        Étant donné un espa e k-analytique X , un ouvert (resp. fermé ) de X sera
toujours une partie ouverte (resp. fermée) de l'espa e topologique |X| sous-ja ent à X .
Morphismes nis et plats.
   Soient p : Y → X un morphisme ni et plat d'espa es k-analytiques et x un point de


## https://theses.hal.science/tel-00010990v1/document 3587--3722

Théorème 2.3.21.  Soit X une ourbe stri tement k -analytique lisse. Le fais eau de R-
                                                                                                 ×
ve toriels engendré par les germes de fon tions log |f |, f étant un germe de se tion de OX        ,
est un sous-fais eau de HX ; le quotient est un fais eau gratte- iel sur |X| et il est nul si l'une
des deux onditions suivantes est vériée :
58



      le orps e
               k est algébrique sur un orps ni ;
      la ourbe X ⊗  ca est lo alement isomorphe à P1 .
                  b kk                               a        k
Démonstration. Soit FX le sous-fais eau de CX asso ié au préfais eau sur |X| faisant orres-
pondre à un ouvert U le sous-espa e ve toriel de C0 (U, R) engendré par les fon tions log |f |,
               ×
f ∈ Γ(U, OX      ) ; 'est un sous-fais eau de HX en vertu de la proposition pré édente. Les germes
de FX et HX oïn ident en tout point x de X de type (1), (3) ou (4) :
     si x est de type (1) ou (4), e point admet un système fondamental de voisinages k-
       anoïdes ayant un unique point de Shilov et les se tions de FX et HX sont don
        onstantes au voisinage de x ;
     si x est de type (3), e point admet un système fondamental de voisinages k-anoïdes
       ayant exa tement deux points de Shilov ; les espa es ve toriels FX,x et HX,x sont alors
       de dimension 2, engendrés par les germes de la fon tion onstante 1 et de la fon tion
       log |f |, f étant une se tion quel onque de OX au voisinage de x telle que |f | ne soit pas
       lo alement onstante en x.
    Soient maintenant x ∈ X un point de type (2), k′ une extension nie galoisienne de k et x′ un
point de X ′ = X⊗k k′ au-dessus de x : l'égalité FX ′ ,x′ = HX ′ ,x′ implique l'égalité FX,x = HX,x .
En eet, si V est un voisinage stri tement k-anoïde de x dans X , V ′ est la omposante
 onnexe de x′ dans V ⊗k k′ , et f ′ ∈ A×                                                        ×
                                                    V ′ , la norme f de f est un élément de AV tel que
                                                                              ′
                      ′
p∗ |f ||V ′ = |f ′ |[k :k] ; si une fon tion h ∈ H(V ) est telle que p∗ h|V ′ soit une ombinaison linéaire
de fon tions log |f |, f ∈ A×                                                                           ×
                                    V ′ , 'est don une ombinaison linéaire de fon tions log |f |, f ∈ AV .
Cette remarque préliminaire permet de supposer que X est isomorphe à la bre générique
d'une S - ourbe simplement semi-stable X et que le point x orrespond à une omposante
irrédu tible propre et géométriquement onnexe Cx de Xs .
Lemme 2.3.22.  Ave les notations en vigueur, l'espa e ve toriel HX,x /FX,x est anoni-
quement isomorphe à l'espa e ve toriel Pic0 (Cx ) ⊗Z R.
Démonstration. Soit V un voisinage stri tement k-anoïde de X . Il existe une extension
galoisienne nie k′ de k et un é latement admissible q : X ′ → X ⊗S Spf(k′ ◦ ) tel que V ⊗k k′
soit isomorphe à la bre générique du s héma formel induit par X ′ sur un ouvert U de Xs′ . La
 omposante irrédu tible Cx de Xs étant supposée géométriquement onnexe, il y a un unique
point x′ ∈ X ⊗k k′ au-dessus de x, orrespondant à la omposante irrédu tible Cx ⊗ek ke′ de
X ⊗S Spf(S ′ ) et, elle- i étant propre et lisse, le morphisme q induit un isomorphisme de la
 omposante irrédu tible de X ′ asso iée à x′ sur Cx ⊗ek ke′ .
                                                               ′
    À toute fon tion h ∈ H(V ) = H(V ⊗k k′ )Gal(k /k) orrespond naturellement un R-diviseur
div(h) sur la ke′ - ourbe Cx ⊗ek ke′ , vue omme omposante irrédu tible de Xs′ : en eet, l'ensemble
Tx′ S(X ′ ) est anoniquement identié à l'ensemble des points singuliers de Xs′ appartenant à
Cx ⊗ek ke′ et, notant x      et le point orrespondant à l'élément t de Tx′ S(X ′ ), on pose :
                                                          X
                                            div(h) =             λx,t (h)[e
                                                                          xt ].
                                              t∈Tx′ S(X ′ )

La ondition d'harmoni ité de h en x′ équivaut à la ondition
                                            deg div(h) = 0.
   Le groupe de Galois Gal(k′ /k) opère naturellement sur la ke′ - ourbe Cx ⊗ek ke′ et son a tion
est transitive sur haque bre du morphisme anonique Cx ⊗ek ke′ → Cx ; puisque h est, par
hypothèse, invariante sous Gal(k′ /k), ela implique que le R-diviseur div(h) sur Cx ⊗ek ke′
des end en un R-diviseur de degré 0 sur sur Cx , en ore noté div(h).
                                                                                                59



  Nous obtenons ainsi une appli ation linéaire div : HX,x → Div(Cx ) ⊗Z R s'insérant dans
une suite
                  0       /R      / HX,x   div   / Div(Cx ) ⊗Z R deg   /R     / 0,

laquelle est exa te. Seule la surje tivité de div sur le sous-espa e des R-diviseurs de degré 0
requiert une démonstration. Soit
                                              X
                                        D=        n(e
                                                    x)[ex]
                                             e∈|D|
                                             x

un R-diviseur de degré 0 sur Cx ; soit I l'Idéal (admissible) dénissant le sous-s héma fermé
réduit Z = |D|∩(Xs −Sing(Xs )) dans Xs et soit q : X ′ → X son é latement. Puisque X est lisse
aux points de Z , X ′ est en ore une S - ourbe simplement semi-stable et on note Y l'ouvert de
X ′ obtenu en retirant, à ha une des omposantes irrédu tibles du diviseur ex eptionnel de X ′ ,
un point fermé disjoint (du transformé stri t) de X . La S - ourbe Y est simplement semi-stable
et Yη est un voisinage de x dans X = Xη . L'ensemble Tx S(Y) s'indentie anoniquement à
une partie nie de l'ensemble des points fermés de Cx et nous avons fait e qu'il fallait pour
que
                                         |D| ⊂ Tx S(Y).
Considérons alors une fon tion ane par mor eaux H sur S(Y) telle que, pour tout polytope
entier P ⊂ S(Y) de dimension un orrespondant à un élément t ∈ Tx S(Y),
- λx,t (H) = 0 si x  / |D|,
                  et ∈
- λx,t (H) = n(e
               xt ) si x
                       et ∈ |D|.
   Une telle fon tion H est harmonique au point x en vertu de la nullité du degré de D ; elle
est don harmonique sur un voisinage de x dans S(Y) et la fon tion h = τY∗ H sur X est par
 onséquent harmonique au voisinage de x dans X . L'identité
                                           div(h) = D
est vériée par onstru tion et nous avons ainsi établi l'exa titude de la suite onsidérée
 i-dessus.
  Soit Pr(Cx ) le groupe des diviseurs prin ipaux sur Cx . On dispose d'une autre suite exa te

                                  /R       / FX,x    div   / Pr(Cx )   / 0,
                           0
                                            ×
 ar, pour tout germe log |f | ∈ FX,x , f ∈ OX,x , le diviseur de la fon tion harmonique N log |f |
s'identie à elui de la fon tion méromorphe induite par f N /α sur Cx , où N est un entier
supérieur à 1 tel que |f (x)|N ∈ |k× | et α est un élément de k tel que |f (x)|N = |α|. Il en
résulte un isomorphisme d'espa es ve toriels réels
                                                 ∼
                                HX,x /FX,x −→ Pic0 (Cx ) ⊗Z R,
 e qui a hève la preuve du lemme.                                                                2
   Terminons la démonstration du théorème. Le fais eau HX /FX est un fais eau gratte- iel
dont le support est un ensemble dis ret de points de type (2) ; sa nullité équivaut à la propriété
suivante : pour tout point x ∈ X ⊗k c ka de type (2), le groupe de Pi ard Pic0 (Cx ) de la e   ka -
                                                                   g , est de torsion. Il y a au
 ourbe irrédu tible, propre et lisse Cx , de orps des fon tions κ(x)
moins deux onditions impliquant ette propriété :
    le orps ek est algébrique sur un orps ni : Pic0 (Cx ) est l'ensemble des e  ka -points d'un
     e
     ka -s héma en groupes de type ni et don est de ardinal ni ;
60



      pour tout point x ∈ X ⊗k k ca de type (2), la eka - ourbe irrédu tible, propre et lisse de
                           g est rationnelle  de manière équivalente, X ⊗
        orps des fon tions κ(x)                                             b kb
                                                                               ka est lo alement
       isomorphe à Pba (si X est irrédu tible et propre, 'est une ourbe de Mumford ).
                     1
                     k
                                                                                              2
                                                                                              61


## https://theses.hal.science/tel-00010990v1/document 4105--4217

     Dans e qui suit, X désigne une ourbe stri tement k-analytique lisse.
Définition 3.2.1.  Soit Ω ⊂ X un ouvert.
   (i ) Une fon tion réelle ϕ ∈ C (Ω, R) est dite lisse s'il existe un re ouvrement lo alement
                           0

ni V de Ω par des domaines k-anoïdes Y tel que ϕ|Y ∈ H(Y ). L'ensemble des fon tions
lisses sur Ω est un sous-espa e ve toriel de C0 (Ω, R), noté A0 (Ω).
   (ii ) On désigne par A1 (Ω) l'espa e ve toriel des mesures réelles sur Ω dont le support est
un sous-ensemble lo alement ni de I(Ω). Les éléments de A1 (Ω) seront appelés formes lisses
(sur Ω).

  (iii ) Le sous-espa e ve toriel de A0 (Ω) (resp. A1 (Ω)) onstituté des fon tions (resp. me-
sures) dont le support est ompa t se note A0c (Ω) (resp. A1c (Ω)).

   La orrespondan e Ω 7→ A0 (Ω) est un sous-fais eau du fais eau CX
                                                                  0 des germes de fon tions

réelles ontinues sur X .
   La dénition du fais eau A0X s'étend d'elle même au G-site XG de X : il sut, pour tout
objet V de XG , de dénir A0 (V ) omme le sous-espa e ve toriel de C0 (V, R) onstitué des
fon tions ϕ ontinues sur V qui satisfont à la ondition suivante : tout point x ∈ V possède
un voisinage k-anoïde W ⊂ V tel que ϕ|W ∈ H(W ). Désignant par A0X le fais eau ainsi
déni sur XG et notant π : XG → |X| le morphisme de sites anonique, l'identité
                                         A0X = π∗ A0X
est évidente. La proposition suivante l'est tout autant.

Proposition 3.2.2.  L'homomorphisme            anonique de préfais eaux HX → A0X sur le site
XG identie A0X au fais eau asso ié à HX .

Remarque 3.2.3
     1. La proposition pré édente répond à la question soulevée par le point 2 de la remarque
        2.3.11.
                                                                                              69



  2. Pour toute extension nie galoisienne k′ /k, l'homomorphisme anonique
                                                           ′
                                   A0X → (A0 X⊗k k′ )Gal(k /k)
     est un isomorphisme de fais eaux sur XG .

 La proposition suivante n'est guère surprenante, ompte tenu de la onstru tion du fais eau
HX .
Proposition 3.2.4.  Une fon tion réelle ϕ sur un ouvert Ω ⊂ X est lisse si et seulement
s'il existe, pour tout domaine stri tement k-analytique ompa t Y ⊂ Ω, une extension nie
(séparable ) k′ /k et une Spf(k′ ◦ )- ourbe simplement semi-stable Y telles que :
    Yη = Y ⊗k k ′ ;
    la fon tion Φ = (ϕ ⊗ 1)|S(Y) appartienne à l'espa e A0 (S(Y)) ;
    ϕ|Y ⊗k k′ = Φ ◦ τY .
Démonstration. Soit Y ⊂ X un domaine stri tement k-analytique ompa t.
   Étant données une extension nie galoisienne k′ /k et une Spf(k′ ◦ )- ourbe simplement semi-
stable Y de bre générique Y ⊗k k′ , onsidérons une fon tion Φ ∈ A0 (S(Y)) et notons S la
réunion du support de la mesure ddc Φ et du bord de Shilov Γ(Yη ) de Yη . Quelle que soit la
 omposante onnexe c de S(X ) − S , la restri tion de Φ au domaine polyédral c appartient
à l'espa e H(c) et la fon tion Φ|c ◦ τY = (Φ ◦ τY )|τ −1 (c) sur le domaine k-analytique τY−1 (c)
                                                      Y
de Y ⊗k k′ appartient à H(τY−1 (c)) ; en vertu de la proposition pré édente, ela implique
Φ ◦ τY ∈ A0 (Y ⊗k k′ ). La ondition de l'énon é est don susante.
   Considérons ré iproquement une fon tion ϕ ∈ A0 (Y ) et un re ouvrement ni V de Y par
des domaines k-anoïdes V tels que ϕ|V ∈ H(V ) ; par appli ation du point (ii) du lemme
2.2.22, il existe une extension nie (séparable) k′ /k et une Spf(k′ ◦ )- ourbe simplement semi-
stable Y , de bre générique Y ⊗k k′ , dont le squelette S(Y) ontient l'ensemble Γ des points de
Shilov des domaines k′ -anoïdes V ⊗k k′ , V ∈ V . Désignons par Φ la restri tion de ϕ′ = ϕ ⊗ 1
au squelette S(Y) de Y . Les bres de la rétra tion τY sont des domaines k′ -anoïdes dont le
bord de Shilov est réduit à un point ; la fon tion ϕ′ , étant harmonique sur Y ⊗k k′ − Γ, est
par suite onstante haque bre de τY en vertu du prin ipe du maximum et
                                          ϕ′ = Φ ◦ τY .
Vérions enn l'appartenan e de Φ à l'espa e A0 (S(Y)) : quel que soit le polytope entier
P ⊂ S(Y) − Γ dont le bord est formé de points de type (2), W = τY−1 (P ) est un domaine
stri tement k-anoïde dans Y tel que ϕ′|W ∈ H(τY−1 (P )) ( orollaire 2.3.14) ; on a don Φ|P =
(ϕ′|W )|P ∈ H(P ) et la fon tion ontinue Φ est bien ane par mor eaux sur S(Y).              2
   La proposition 3.2.2 peut maintenant être pré isée de manière à donner une nouvelle dé-
nition du fais eau A0X sur le G-site XG de X . Étant donné un domaine k-analytique V ⊂ X ,
 onvenons de désigner par R log |OX (V )× | le sous-espa e ve toriel réel de C0 (V, R) engendré
par les fon tions de la forme log |f |, f ∈ OX (V )× . La orrespondan e
                                       ×
                               R log |OX | : V 7→ R log |OX (V )× |

est un sous-préfais eau de A0X sur XG puisque R log |OX (V )× | ⊂ H(V ) pour tout domaine
k-anoïde V ⊂ X .
                                                                   ×
Proposition 3.2.5.  L'homomorphisme              anonique R log |OX | → A0X identie A0X au
                                        ×
fais eau asso ié au préfais eau R log |OX |.
70



Démonstration. Soit FX le fais eau sur XG asso ié au préfais eau R log |OX× |. Quelle que
                                                                                   ×
soit l'extension galoisienne nie k′ /k, la norme Nk′ /k : (pk′ )∗ (OX ⊗k k′ )× → OX induit un
homomorphisme Nk′ /k : (pk )∗ FX⊗k k → F tel que
                             ′        ′

                                           1
                                   f=              Nk′ /k (f ⊗ 1)
                                        [k′ : k]
pour toute se tion f de F , pk′ désignant la proje tion anonique de X ⊗k k′ sur X . Il sut don
de prouver qu'une se tion ϕ de A0X provient de FX après passage à une extension galoisienne
nie de k.
    Soient Y ⊂ X un domaine k-analytique ompa t et ϕ une fon tion dans A0X (Y ). Il existe par
hypothèse un re ouvrement ni V de Y par des domaines k-anoïdes V tels que ϕ|V ∈ H(V )
et, omme dans la démonstration pré édente, on peut trouver une extension galoisienne nie
k′ /k et une Spf(k′ ◦ )- ourbe simplement semi-stable Y dont la bre générique est un voisinage
de Y ⊗k k′ dans X ⊗k k′ et dont le squelette S(Y) ontient l'ensemble Γ de tous les points de
Shilov des domaines k-anoïdes V ⊗k k′ , V ∈ V .
    Considérons alors une dé omposition élémentaire D de S(Y) telle que Γ ⊂ D[0] (on rappelle
que D[0] est l'ensemble des 0-fa es des polytopes gurant dans D ). Quel que soit le polytope
Q ∈ D , τ −1 (Q) est un domaine k-anoïde et, par onstru tion,
                           ϕ|Q ∈ H(τ −1 (Q)) = R log |OX (τ −1 (Q))|.
                                                                                              2
Remarque 3.2.6.  Cette proposition est à rappro her des onsidérations de 2.3.4.
3.2.2. Un résultat de densité.


## https://theses.hal.science/tel-00010990v1/document 5284--5317

X du ourant de degré 0 qu'elle détermine.
   Une fon tion sous-harmonique sur une surfa e de Riemann est, lo alement, l'enveloppe in-
férieure d'une famille dé roissante de fon tions sous-harmoniques lisses ([19℄, Theorem 2.5.5).
Cette assertion est également vraie dans un ontexte non ar himédien, la démonstration en
étant qui plus est élémentaire.
Théorème 3.4.2.  Soient Ω un ouvert d'une           ourbe stri tement k-analytique lisse X et
u ∈ SH(Ω). Pour tout ouvert relativement ompa t Ω′ ⊂ Ω, la restri tion de u à Ω′ est
l'enveloppe inférieure d'une famille dé roissante de fon tions sous-harmoniques lisses.
Démonstration. On peut supposer que l'ouvert relativement ompa t Ω′ ⊂ Ω est de la forme
Y − ∂Y , Y ⊂ X étant un domaine k-analytique ompa t.
   Étant donné un sous-ensemble ni S ⊂ I(Y ) ontenant ∂Y , dé oule des propositions 3.1.19
et 3.1.20 l'existen e d'une unique fon tion uS appartenant à A0 (Y ), harmonique sur Y − S
et oïn idant ave u sur S .
90



   La sous-harmoni ité de u sur Y − S implique l'inégalité u|Y ≤ uS ; par suite, pour tout
sous-ensemble ni S ′ de I(Y ) ontenant S , uS majore uS ′ sur le bord S ′ de Y − S ′ et uS ′ ≤
uS , en vertu du prin ipe du maximum (proposition 3.1.1) appliqué aux fon tions uS et uS ′ ,
harmoniques sur Y − S ′ . La famille (uS )S est don dé roissante.
   La fon tion lisse uS est sous-harmonique sur Y −∂Y . Soient en eet V ⊂ Y −∂Y un domaine
k-anoïde et h une fon tion dans H(V ) qui majore uS sur ∂V . Puisque u|Y ≤ uS , h majore
a fortiori u sur ∂V , et don sur tout V par sous-harmoni ité ; omme u et uS oïn ident sur
S , il s'ensuit que h majore u sur le bord S ′′ = (S ∩ V ) ∪ ∂V de l'ouvert V − S ′′ . Une nouvelle
appli ation du prin ipe du maximum aux fon tions harmoniques h|V −S ′′ et (uS )|V −S ′′ fournit
alors l'inégalité
                                               uS ≤ h
sur V .
   La famille (uS )S  S par ourant l'ensemble ltrant des parties nies de I(Y ) ontenant
∂Y  est minorée en tout point de I(X) ; son enveloppe inférieure u est don une fon tion
sous-harmonique sur X (proposition 3.1.8). La démonstration s'a hève en invoquant le lemme
3.4.1 : les fon tions sous-harmoniques u et u|Y −∂Y , trivialement égales sur I(Y ) − ∂Y , sont
identiques.                                                                                  2


## https://theses.hal.science/tel-00010990v1/document 5353--5375

  Ce i établit la positivité de la forme lisse ddc ϕ.                                             2

Corollaire 3.4.5.  Soient X          une ourbe stri tement k-analytique lisse, K/k une ex-
tension non ar himédienne et pK : X ⊗    b k K → X la proje tion anonique ; étant donnée une
fon tion sous-harmonique u sur X , la fon tion p∗K u est sous-harmonique sur X ⊗    b kK.
Démonstration. Puisqu'il est loisible de raisonner lo alement, nous pouvons, en vertu du
théorème 3.4.2, supposer que u est l'enveloppe inférieure d'une famille (ϕλ ) de fon tions sous-
harmoniques lisses. La fon tion pK ∗u est alors l'enveloppe inférieure de la famille de fon tions
lisses p∗K ϕλ et il sut don de traiter le as d'une fon tion sous-harmonique lisse.
   Soit u une fon tion sous-harmonique lisse et vérions que la mesure ddc p∗K u est positive.
La formule
                                   ddc p∗K u = pK ′ /K ∗ ddc p∗K ′ u
pour toute extension non ar himédienne K ′ /K (théorème 3.2.10) permet d'agrandir K à loisir.
Considérons un domaine stri tement k-anoïde Y ⊂ X et une extension nie k′ /k telle que
Y ⊗k k′ soit isomorphe à la bre générique d'une Spf(k′ ◦ )- ourbe simplement semi-stable Y
et que la fon tion p∗k′ u s'é rive sous la forme U ◦ τ , ave U ∈ A0 (S(Y)) (proposition 3.2.4) ;
la sous-harmoni ité de u implique elle de U puisque ddc U = ddc u (théorème 3.2.10). Soient
maintenant K ′ une extension non ar himédienne de k oiant K et k′ et p : S(Y)K ′ → S(Y)
l'appli ation induite par la proje tion anonique de X ⊗   b k K ′ sur X ⊗k k′ . La fon tion p∗ U est
sous-harmonique sur S(Y)K et il en est par onséquent de même pour p∗K ′ u = p∗ U ◦ τK ′ .
    Comme mentionné au début de la démonstration, la sous-harmoni ité de p∗K ′ u implique
  elle de p∗K u.                                       2                                          2



## https://arxiv.org/pdf/2111.05741 4047--4118


15.8. Let X be a compact rig-smooth curve over K with strictly semistable model X. As
in 15.2, the skeleton S(X) is viewed as a weighted metric graph with boundary. Let U
be a subgraph of Σ := S(X) with vertices contained in Σ(Λ), then τ−1 (U) is a compact
strictly analytic domain in X .
80                              W. GUBLER, P. JELL, AND J. RABINOFF

Proposition 15.9. With the notation above, let f : U → R be a piecewise (Z, Γ )-linear
harmonic function as in 15.1. Then h := f ◦ τ: τ−1 (U) → R is Z-harmonic.
Proof. Replacing U be a subdivision, we may assume that f is affine (Z, Γ )-linear on each
edge. The vertices of U induce a subdivison of S(X) and hence 15.3 yields a canonical
formal K ◦ -model X′ of X over X. By 15.4, we get a canonical open formal subscheme Y′ of
X′ with generic fiber Y = τ−1 (U). It follows from 5.6 and 15.4 that h is piecewise linear,
so by definition, it is Z-harmonic if and only if it is harmonic. After a finite, separable
extension of the ground field, the graph U becomes a skeleton of Y with respect to some
strictly semistable model (see Remark 5.3.6 in [GJR21]). Thus h is harmonic in the sense
of Thuillier, so by Proposition 15.7, it is harmonic in the sense of Definition 7.2.     
Remark 15.10. Let X be a smooth curve (that is, a rig-smooth curve without boundary),
let H be the sheaf of harmonic functions on X , and let F be the subsheaf of R-vector
spaces generated by the germs log | f | for local invertible analytic functions f . Then Thuil-
lier [Thu05, 2.3.4] has shown that F might be a strict subsheaf of H , with equality when
X is potentially locally isomorphic to P1,an or when K e is algebraic over a finite field. It was
shown in [Wan16, 5.2, 5.3] that F is the kernel of d′ d′′ : A0,0 sm
                                                                    → A1,1
                                                                         sm
                                                                             and that F is the
sheaf of smooth harmonic functions on X . The latter follows also by Proposition 10.17.
We conclude that there is a non-smooth harmonic function on an open subset of X if and
only if the inclusion F ⊂ H is strict. If F = H , then every harmonic tropicalization
map is a smooth tropicalization map, and Asm = A.
  Wanner’s regularization theorem [Wan19, Corollary 5.4], obtained for Mumford curves
or in case of an algebraic residue field over a finite field, can now be generalized as fol-
lows (compare Remark 15.10).
Proposition 15.11. Let X be a smooth curve (a rig-smooth curve without boundary) over
a non-trivially valued non-Archimedean field K, and let f be a subharmonic function on X
as defined in [Thu05, 3.1.2]. Then for any relatively compact open subset U of X , there is
a decreasing net of weakly smooth psh functions f i on U converging pointwise to f |U .
Proof. By Thuillier’s regularization theorem [Thu05, Théorème 3.4.2], there is a decreas-
ing net of piecewise R-linear subharmonic functions on U converging pointwise to f , so
we may assume that f is piecewise R-linear. (Note that piecewise R-linear functions are
called lisse in [Thu05, Definition 3.2.1].) As in the proof of [Thu05, Theorem 3.4.2],
we may assume that U = Y \ ∂ Y for a compact strictly analytic domain Y of X . By
[Thu05, Proposition 3.2.4], there is a finite Galois extension K ′ /K such that Y has a
strictly semistable model Y over the valuation ring of K ′ and such that f = F ◦ τ for a
piecewise R-linear function F on the skeleton S(Y), where τ: Y → S(Y) is the retraction.
Since the subharmonic functions over K are the Galois-invariant subharmonic functions
over K ′ and the same holds for weakly smooth functions, it is enough to prove the claim
over K ′ , so we may assume K = K ′ .
   Now we can follow Wanner’s arguments [Wan19, Lemma 5.2]. Note that the curvature
ddc ( f |U ) is a discrete measure on U; we denote by S its support. In what follows, we
allow subdivisions of Σ := S(Y) at arbitrary points in Σ (not just type-II points); we do
not claim that the subdivision is the skeleton of a formal model of U. By subdividing the
              FORMS ON BERKOVICH SPACES BASED ON HARMONIC TROPICALIZATIONS                 81

skeleton, we may assume that Σ contains S, that F is affine on the edges of Σ, and that
the points of S are vertices of Σ. For a point x ∈ S, let Σ x be the union of all edges of
Σ containing x. By further subdividing Σ, we may assume that Σ x ∩ S = {x}. Since x
is in the support of ddc ( f |U ), the weighted sum of outgoing slopes of F in x is positive.
Then there is a harmonic function G x ≤ F on Σ x , affine on each edge of Σ x , and with
F ( y) = G x ( y) if and only if y = x. For ǫ > 0 sufficiently small, the regularized maximum
mǫ as defined in [Wan19, 4.6] leads to a function
                      fǫ := mǫ/2 (G x ◦ τ + ǫ, f ) = mǫ/2 (G x + ǫ, F ) ◦ τ
on τ−1 (Σ x ) which agrees with f over a neighbourhood of the boundary of Σ x and agrees
with G x ◦ τ + ǫ over a neighbourhood of x in Σ x . We conclude that the functions fǫ ,
for varying x S∈ S, can be glued to get a function fǫ defined on Y which agrees with f
on V := Y \ x∈S τ−1 (Px ) for suitable compact neighbourhoods Px of x in relint(Σ x ).
Since f is harmonic on U ∩ V by omitting S, we see that fǫ is harmonic on U ∩ V and
on a neighbourhood of S. Since the regularized maximum of two affine functions on a
segment is a convex smooth function, we see that fǫ is a smooth psh function over the
interior of each edge of any Σ x . Overall, it follows that fǫ is a weakly smooth psh function
on U. In the proof of [Wan19, Lemma 5.2], Wanner extracted from the functions fǫ a
decreasing sequence which converges pointwise to f , which proves the proposition. 


## https://arxiv.org/pdf/1204.6277v2 994--1025


Lemme 1.2.11. — Soit ω une forme symétrique de type (p, p) sur V . Soit W un espace
vectoriel réel et f : W → V une application linéaire.
  a) Si ω est positive ( resp. faiblement positive, resp. fortement positive), il en est de
même de la forme f ∗ ω sur W .
  b) Si f est surjective et si f ∗ ω est positive ( resp. faiblement positive, resp. fortement
positive), il en est de même de ω.
Démonstration. — Commençons par l’assertion 1). Le cas des formes fortement positives
est évident, celui des formes faiblement positives résulte de la proposition 1.2.5, tandis
que celui des formes positives découle de l’interprétation de la positivité en termes de
formes bilinéaires (§1.2.6).
   Venons-en à l’assertion 2) ; on suppose donc f surjective. Le cas des formes faiblement
positives résulte de la proposition 1.2.5 et du fait que toute application affine g : U → V
se relève à W .
   En ce qui concerne les formes positives et fortement positives, on choisit un isomor-
phisme W ≃ V ⊕ V ′ modulo lequel f est la première projection. Si f ∗ ω est positive, la
forme bilinéaire η qu’elle induit sur Λp W est positive (§1.2.6) ; comme η est le prolon-
gement par 0 de la forme bilinéaire η ′ induite par ω sur le sommande Λp V de Λp W , la
forme η’ est positive, et ω est positive en vertu là encore de §1.2.6.
   Si f ∗ ω est fortement positive, elle s’écrit sous la forme
                   X
                      ai αi,1 ∧ J(αi,1 ) ∧ αi,2 ∧ J(αj,2 ) ∧ . . . ∧ αi,ni ∧ J(αi,ri ),
où les αi,j sont de type (1, 0) et les ai strictement positifs. Comme f ∗ ω est égale au pro-
longement par 0 de la forme ω vue comme vivant dans le sommande Ap,p (V ) de Ap,p (W ),
il vient
              X
         ω=       ai αi,1,V ∧ J(αi,1,V ) ∧ αi,2,V ∧ J(αj,2,V ) ∧ . . . ∧ αi,ni ,V ∧ J(αi,ri ,V ),
                                  § 1.2. SUPERFORMES POSITIVES                                      27

où le V en indice indique la projection sur le sommande A1,0 (V ). Ainsi, ω est fortement
positive.



## https://arxiv.org/pdf/1204.6277v2 7337--7356





                             § 6.5. FORMES POSITIVES

  Soit X un espace G-tropical affiné. Soit G une classe de coefficients.

Lemme 6.5.1. — Soit ω une forme de type (p, p) et symétrique sur X qui est positive
en tant que G-forme ( resp. faiblement positive, resp. fortement positive). Pour tout
point x ∈ X, il existe une carte tropicale f définie sur un voisinage U de x à valeurs dans
un espace affine E, et une forme positive α ( resp. faiblement positive, resp. fortement
positive) sur un sous-espace paralinéaire de E contenant f (U ), telle que ω|U = f ∗ α.

Démonstration. — Soit x un point de X. Soit V un voisinage domanial compact de x
sur lequel ω est tropicale ; soit f : V → E une carte tropicale qui tropicalise ω et soit α
une forme sur un sous-espace paralinéaire de E contenant f (V ) tels que ω|V = f ∗ α.
D’après le lemme 3.5.3, la restriction à f (V ) de α est positive (resp. faiblement positive,
resp. fortement positive). Il suffit donc de prendre pour carte tropicale la restriction à V̊
de f et pour forme α sa restriction à f (V ).


## https://arxiv.org/pdf/1204.6277v2 9724--9792



              § 8.1. FONCTIONS PLURISOUSHARMONIQUES

  Soit X un espace G-tropical affiné.
Définition 8.1.1. — On note PshX le plus petit sous-faisceau du faisceau des fonctions
sur X, à valeurs dans R ∪ {−∞}, tel que pour tout ouvert U de X, l’ensemble PshX (U )
vérifie les propriétés :
  i) Il contient les fonctions lisses u sur U telles que d′ d′′ u ⩾ 0 ;
  ii) Il est stable par limite décroissante de suites.
Ses sections sont appelées des fonctions plurisousharmoniques (psh).
Lemme 8.1.2. — Pour tout ouvert U de X, l’ensemble des fonctions psh sur U est un
cône convexe formé de fonctions semi-continues supérieurement ; il contient les fonctions
constantes.
  La démonstration est identique à celle du lemme 1.10.6.
Démonstration. — Les fonctions constantes sont lisses et psh.
  Les fonctions semi-continues supérieurement u telles que λu soit psh, pour tout nombre
réel positif λ, forment un sous-faisceau de PshX qui vérifie les conditions (i) et (ii), donc
est égal à PshX . Cela prouve que pour tout ouvert U de X, l’ensemble PshX (U ) est un
sous-cône de l’ensemble des fonctions semi-continues supérieurement sur U .
  Démontrons que si u et v sont des fonctions psh sur un ouvert U de X, il en est de
même de u + v.
  Supposons d’abord que u soit lisse. Les fonctions f telles que f + u soit psh forment
un sous-faisceau de PshU qui contient les fonctions lisses psh et est stable par limite
décroissante ; il contient donc toutes les fonctions psh sur U . En particulier, u + v est
psh lorsque u est lisse.
  Dans le cas général, les fonctions f telles que f + v soit psh forme un sous-faisceau
de PshU qui contient les fonctions lisses psh d’après le premier cas traité et est stable
par limite décroissante ; il contient donc toutes les fonctions psh sur U ; par suite, u + v
est psh.
196                    CHAPITRE 8. THÉORIE DE BEDFORD–TAYLOR

Remarque 8.1.3. — Cette définition est inspirée par le théorème de [67] en analyse
complexe qui affirme que dans ce contexte, une fonction psh sur un espace de Stein est
limite d’une suite décroissante de fonctions psh lisses.
   Dans le présent travail, nous considérerons surtout des fonctions psh continues.
   Par ailleurs, rappelons que si une suite décroissante de fonctions continues converge
simplement vers une fonction continue, elle converge même localement uniformément
(théorème de Dini), puisqu’un espace tropical est localement compact.
Lemme 8.1.4. — Pour tout ordinal α, on définit par récurrence transfinie un sous-
faisceau PshX,α du faisceau des fonctions sur X par les conditions suivantes :
   a) On définit PshX,0 comme le faisceau des fonctions lisses u telles que d′ d′′ u ⩾ 0 ;
   b) Si α est un ordinal, on définit PshX,α+1 comme le sous-faisceau des fonctions sur X
qui sont localement limites décroissantes de fonctions de PshX,α ;
   c) Si α est un ordinal limite, on définit PshX,α comme le sous-faisceau des fonctions
sur X qui appartiennent localement à un PshX,β pour β < α.
La famille ordinale (PshX,α ) est une famille croissante de sous-faisceaux de PshX qui
vaut PshX pour α assez grand.
Démonstration. — Par récurrence transfinie, il résulte de la définition de PshX , que
PshX,α ⊂ PshX pour tout ordinal α. La construction montre que cette famille de sous-
faisceau est croissante. Elle est nécessairement stationnaire, par un argument de cardinal.
Soit α un ordinal à partir duquel la famille est constante et démontrons que PshX ⊂
PshX,α . Il suffit pour cela de démontrer que PshX,α vérifie les deux conditions de la
définition de PshX . Il est évident que PshX,α contient les fonctions lisses u telles que
d′ d′′ u ⩾ 0, qui appartiennent au sous-faisceau PshX,0 . Soit maintenant U un ouvert de X
et (un ) une suite décroissante de fonctions de PshX,α (U ) qui converge simplement vers
une fonction localement intégrable u et démontrons que u ∈ PshX,α (U ). Par construction,
on a u ∈ PshX,α+1 (U ) ; par définition de α, on a donc u ∈ PshX,α (U ).

Proposition 8.1.5. — Soit f : Y → X un morphisme d’espaces G-tropicaux affinés.
Pour toute fonction psh u sur X, la fonction u ◦ f sur Y est psh. Plus précisément, pour
tout ordinal α tel que u appartient à PshX,α , la fonction u ◦ f appartient à PshY,α .
Démonstration. — Compte tenu du lemme 8.1.4, il suffit de démontrer la seconde asser-
tion. On procède par récurrence sur α. Le cas α = 0 résulte de ce que pour toute fonction
psh lisse u, la fonction u ◦ f est psh lisse. L’assertion découle alors de la construction
par récurrence des faisceaux PshX,α et PshY,α .

Remarque 8.1.6. — En géométrie complexe, on pourrait définir une hiérarchie ordi-
nale analogue des faisceaux de fonctions psh, mais leur théorie établit que cette hiérarchie


## https://arxiv.org/pdf/1204.6277v2 9817--9864


Proposition 8.1.9. — Soit (fn ) une suite de fonctions de X dans R qui converge
localement uniformément vers une fonction f . Si les fn sont psh, alors f est psh.
Démonstration. — Comme les fonctions constantes sont psh, l’assertion découle du
lemme suivant.

Lemme 8.1.10. — Soit X un ensemble et soit (fn ) une suite de fonctions de X dans R
qui converge uniformément vers une fonction f . La suite (fn + 2∥f − fn ∥∞ ) converge
uniformément vers f et admet une sous-suite qui est décroissante.
Démonstration. — Puisque ∥f − fn ∥∞ tend vers 0, il est clair que la suite (fn +
2∥f − fn ∥∞ ) converge uniformément vers f . L’assertion est évidente s’il existe une
infinité d’entiers n tels que ∥f − fn ∥∞ = 0. On peut donc supposer que ∥f − fn ∥ > 0
pour tout n. Soit n un entier. Puisque (fn ) converge uniformément vers f , il existe
m > n tel que ∥fm − f ∥∞ < ∥f − fn ∥∞ /3. Des inégalités fm ⩽ f + ∥fm − f ∥∞ et
f − ∥fn − f ∥∞ ⩽ fn , on déduit que
fm +2∥fm − f ∥∞ ⩽ f +3∥fm − f ∥∞ ⩽ fn +3∥fm − f ∥∞ +∥fn − f ∥∞ ⩽ fn +2∥fn − f ∥∞ .
Le lemme s’en déduit.

Proposition 8.1.11. — On a CPshX = CX ∩ PshX : les fonctions continues plurisous-
harmoniques sont les fonctions continues (à valeurs réelles) qui sont plurisousharmoni-
ques. Plus précisément, pour tout ordinal α, on a CPshX,α = CX ∩ PshX,α .
Démonstration. — Compte tenu des lemmes 8.1.4 et 8.1.8, il suffit de vérifier la seconde
assertion. Prouvons cette égalité par récurrence transfinie. Les cas de l’ordinal 0 et
d’un ordinal limite sont évidents. Il suffit donc de prouver que pour tout ordinal α,
une fonction continue u définie sur un ouvert U est localement limite décroissante de
fonctions de CPshX,α si et seulement si elle est localement limite uniforme de telles
fonctions.
  Soit U un ouvert de X et soit (un ) une suite décroissante de fonctions de CPshX,α (U )
qui converge simplement vers une fonction continue u sur U . Le théorème de Dini assure
que la convergence est uniforme sur toute partie compacte de U . Comme U est localement
198                    CHAPITRE 8. THÉORIE DE BEDFORD–TAYLOR

compact, la convergence est localement uniforme, si bien que la fonction u appartient
à CPshX,α+1 .
   Soit U un ouvert de X et soit u une fonction continue sur U qui est localement limite
décroissante d’une suite de fonctions de CPshX,α . Soit (Ui ) un recouvrement ouvert de U
tel que u|Ui soit limite décroissante d’une suite de fonctions de CPshX,α (Ui ). D’après ce
qui précède, u|Ui appartient à CPshX,α+1 (Ui ). Par la propriété de faisceau, u appartient
à CPshX,α+1 (U ).
   Soit U un ouvert de X et soit (un ) une suite de fonctions de CPshX,α (U ) qui converge
uniformément vers une fonction continue u sur U . D’après le lemme précédent, il existe
une sous-suite de la suite (un +2∥un − u∥) qui converge uniformément, et en décroissant,
vers u. Elles appartiennent à CPshX,α , donc à PshX,α , par l’hypothèse de récurrence, si
bien que u appartient à CX ∩ PshX,α+1 .
   Soit U un ouvert de X et soit u une fonction continue sur U qui est localement limite
uniforme d’une suite de fonctions de CPshX,α . D’après ce qui précède, u appartient
localement à CX ∩ PshX,α+1 , donc est une section de ce faisceau sur l’ouvert U .



## https://arxiv.org/pdf/1204.6277v2 9885--9928

Définition 8.1.13. — On dit qu’une fonction psh sur un ouvert de X est localement
approchable si c’est une section du faisceau PshX,1 .



                        § 8.2. CONVEXITÉ TROPICALE

  Soit X un espace G-tropical affiné.

Proposition 8.2.1. — Soit u1 , . . . , un des fonctions psh sur X. Soit Ω un ouvert
convexe de Rn et soit g : Ω → R une fonction lisse, convexe, croissante par rapport
                                   § 8.2. CONVEXITÉ TROPICALE                                      199

à chaque variable. On suppose que (u1 (x), . . . , un (x)) ∈ Ω pour tout x ∈ X. Alors, la
fonction u : x 7→ g(u1 (x), . . . , un (x)) sur X est psh.
  Plus précisément, si α est un ordinal tel que pour tout i, ui appartient PshX,α , la
fonction u appartient à PshX,α .

Démonstration. — On raisonne par récurrence sur α.
   Supposons d’abord α = 0, c’est-à-dire que toutes les uj sont lisses. Alors u est lisse et
l’on a
                     X ∂ 2g                                            X ∂g
          d′ d′′ u =               (u1 , . . . , un ) d′ ui ∧ d′′ uj +        ◦ u · d′ d′′ uj .
                     i,j
                         ∂y i ∂y j                                     j
                                                                         ∂y j

Puisque g est convexe, le premier terme est une forme positive, en vertu de
l’exemple 3.5.4. Puisque g est croissante par rapport à chaque variable, (∂g/∂yj ) ◦ u
est une fonction positive sur X ; par hypothèse, les (1, 1)-formes d′ d′′ uj sont positives ;
par suite, le second terme est également positif. Cela démontre que d′ d′′ u est une
(1, 1)-forme lisse positive, si bien que la fonction u est donc psh. Elle appartient donc
à PshX,0 .
   Supposons maintenant α > 0.
   Supposons que α soit un ordinal limite. Soit x un point de X ; il existe un voisinage
ouvert U de x et un ordinal β < α tels que uk |U ∈ PshX,β (U ) pour tout k. L’hypothèse
de récurrence entraîne que g(u1 , . . . , un )|U = g(u1 |U , . . . , un |U ) appartient à PshX,β , donc
à PshX,α . Il s’ensuit que u appartient à PshX,α .
   Supposons maintenant que α soit le successeur d’un ordinal β. Soit x un point de X ;
il existe un voisinage ouvert U de x et, pour tout k ∈ {1, . . . , n}, une suite décrois-
sante (vk,m ) de fonctions de PshX,β (U ) qui converge vers uk |U . Commme g est continue
et croissante par rapport à chaque variable, la suite (g(v1,m |U , . . . , un,m |U ))m converge
en décroissant vers g(u1 , . . . , un )|U . Par l’hypothèse de récurrence, ces fonctions appar-
tiennent à PshX,β . Par suite, g(u1 , . . . , un ) appartient à PshX,α .


## https://arxiv.org/pdf/1204.6277v2 9993--10025

f (U ) et une fonction convexe convexe v sur P tel que u|U = f ∗ v.
  Une fonction tropicalement convexe est psh.
                         § 8.3. FONCTIONS PSH ET COURANTS POSITIFS                             201

             § 8.3. FONCTIONS PSH ET COURANTS POSITIFS

 Soit X un espace tropical de niveau n. On suppose que X est sans bord ; en particulier,
X est localement différentiellement séparé, très riche et décent.

Proposition 8.3.1. — Soit u une fonction sur X à valeurs dans R∪{−∞}, localement
intégrable.
  a) Si u est plurisousharmonique, le courant d′ d′′ [u] est positif.
  b) Si u est lisse, elle est plurisousharmonique si et seulement si le courant d′ d′′ [u] est
positif.

Démonstration. — Pour tout U , notons P(U ) l’ensemble des fonctions localement inté-
grables u sur U telles que le courant d′ d′′ [u] sur U soit positif. Il est immédiat que
P est un sous-faisceau du faisceau des fonctions localement intégrables (à valeurs
dans R ∪ {−∞}) qui contient les fonctions lisses psh. Vérifions qu’il est également
stable par limite décroissante. Soit (un ) une suite décroissante de fonctions localement
intégrables sur un ouvert U de X qui converge simplement vers une fonction u locale-
ment intégrable sur U . Soit ω une (n, n)-forme lisse et à support compact       R sur U . Si ω est
positive,
      R    le théorème de  convergence      monotone  entraîne que  la  suite  (   un ω) converge
vers uω. Comme ω est différence de deux formes positives à support compact, cette
convergence est encore vérifiée. Cela démontre que la suite de courants ([un ]) converge
vers le courant [u]. Si de plus d′ d′′ [un ] ⩾ 0 pour tout n, alors d′ d′′ [u] ⩾ 0 par passage à
la limite. Par conséquent, P contient CPshX . Cela démontre l’assertion a).
   Supposons maintenant que u est lisse. Si u est plurisousharmonique, alors d′ d′′ [u] est
positif d’après a). Supposons inversement que le courant d′ d′′ [u] soit positif. Comme
c’est le courant associé à la forme lisse d′ d′′ u, cette forme est positive, d’après le corol-
laire 7.3.10. La fonction u appartient donc à CPshX (U ) par définition de ce cône.



## https://arxiv.org/pdf/1204.6277v2 21540--21578




                   § 15.1. FORMES ET FONCTIONS LISSES

Proposition 15.1.1. — Soit X un espace k-analytique topologiquement séparé, consi-
déré comme espace G-tropical affiné.
   a) Soit ω une G-forme de type (p, q) sur X. Il existe un G-recouvrement (Vi ) de X et,
pour tout i, un moment fi : Vi → Ti sur Vi , une forme αi de type (p, q) sur une partie
                                                                 ∗
paralinéaire de Ti,trop contenant fi,trop (Vi ) tels que ω|Vi = fi,trop αi .
   b) Soit ω une forme de type (p, q) sur X. Il existe un recouvrement ouvert (Vi ) de X
et, pour tout i, un moment fi : Vi → Ti sur Vi , une forme αi de type (p, q) sur une partie
                                                                 ∗
paralinéaire de Ti,trop contenant fi,trop (Vi ) tels que ω|Vi = fi,trop αi .
422 CHAPITRE 15. FORMES DIFFÉRENTIELLES RÉELLES EN GÉOMÉTRIE ULTRAMÉTRIQUE

Démonstration. — On ne traite que le cas des G-formes, l’autre est analogue. Par hy-
pothèse, il existe un G-recouvrement (Wi ) de X et, pour tout i, une application parali-
néaire gi sur Wi à valeurs dans un espace affine Rni , une forme βi de type (p, q) sur une
partie paralinéaire de Ei contenant gi (Wi ), tels que ω|Wi = gi∗ βi pour tout i. Par défini-
tion d’une application paralinéaire, il existe pour tout i un G-recouvrement (Vi,j ) de Wi
et, pour tout j, un moment fi,j sur Vi,j , à valeurs dans le tore Gnmi un nombre rationnel
ai,j et un élément ci,j ∈ Rni tels que gi,j = ai,j fi,j,trop + ci,j . Notons pi,j : Rntrop
                                                                                        i
                                                                                           → Rni
l’application affine t 7→ at + ci,j ; on a donc gi,j = pi,j ◦ fi,j,trop , de sorte que
                                               ∗
                                     ω|Vi,j = fi,j,trop (p∗i,j βi ).

L’assertion en résulte.


Corollaire 15.1.2. — Une fonction u sur X est lisse au voisinage d’un point x s’il
existe un voisinage U de x dans X, des fonctions inversibles f1 , . . . , fn sur U et une
fonction φ sur Rn au voisinage de (f1,trop (x), . . . , fn,trop (x)) telle que u = φ ◦ ftrop sur U .

  Dans la suite du texte, nous travaillerons essentiellement avec ce type de cartes (G)-
tropicales.


## https://arxiv.org/pdf/1204.6277v2 22153--22170




                         § 16.1. QUELQUES FORMULES

Proposition 16.1.1. — Soit X un n-un espace k-analytique, soit K une extension
complète de k et soit p : XK → X le morphisme de changement de base. On a les
                                            ∂        ∂
égalités de courants p∗ (δXK ) = δX et p∗ (δX K
                                                ) = δX .

Démonstration. — Pour la première relation, il s’agit de démontrer que pour toute forme
lisse ω de type (n, n), à support compact, on a XK p∗ ω = X ω ; c’est la formule 15.3.1.
                                               R           R

   La seconde se prouve de même en utilisant la formule 15.3.2.




## https://arxiv.org/pdf/1801.04713v3 166--181



Terminology. In this paper, let K be an algebraically closed field endowed with a com-
plete, non-archimedean, non-trivial absolute value | |. We write val(K × ) := − log |K × |
and R := {x ∈ K | |x| ≤ 1} with maximal ideal m ⊂ R and residue field K   e := R/m. By
suitably normalizing the absolute value | |, we may assume that Z, and so Q, is contained
in val(K × ). A variety over K is an irreducible separated reduced scheme of finite type
over K and a curve is a 1-dimensional variety over K.

Acknowledgements. The author would like to thank Walter Gubler for very carefully
reading drafts of this work and for the helpful discussions. The author is also grateful
to Philipp Jell for providing a simplification of the proof of Proposition 4.4 and further
useful comments. Finally, the author would like to thank the referee for their very precise
report and helpful suggestions.




## https://arxiv.org/pdf/1801.04713v3 250--269

Proposition 2.6. Let X, X ′ be smooth algebraic curves, ϕ : (X ) → X an be a mor-
phism of K-analytic spaces and W be an open subset of X an . If f : W → R is a subhar-
monic function on W , then ϕ∗ f is a subharmonic function on ϕ−1 (W ).
Proof. See [Thu05, Proposition 3.1.14].                                                    
  In the following, we define the class of lisse functions using the characterization in
[Thu05, Proposition 3.2.4]. Note that we can replace compact strictly analytic domains
by strictly affinoid domains looking at the proof of [Thu05, Proposition 3.2.4] and using
[Thu05, Proposition 3.2.2].
Definition 2.7. Let W be an open subset of X an . A function f : W → R is called lisse
if for every strictly affinoid domain Y ⊂ W , there exists a strictly semistable formal
R-curve Y such that Y = Y η and f |Y = F ◦ τY for a piecewise affine function F on S(Y).
Proposition 2.8. Let W be an open subset of X an and f a subharmonic function on
W . For every relatively compact open subset W ′ of W , there is a decreasing net hfj i of
lisse subharmonic functions converging pointwise to f on W ′ .
Proof. See [Thu05, Théorème 3.4.2].                                                        
Definition 2.9. Let W be an open subset of X an and f : W → R be a lisse function on
W , then we denote by ddc f the unique real measure on W that
6                                         V. WANNER




## https://arxiv.org/pdf/1801.04713v3 1628--1778

   To obtain a monotone regularization theorem in the setting of Chambert-Loir and
Ducros for certain X, e.g. for the projective line or a Mumford curve, we use the monotone
regularization theorem in Thuillier’s setting. Hence, we first need to show that every
point has an open neighborhood such that every lisse subharmonic, and so psh, function
is globally psh-approximable on it, i.e. it is the uniform limit of smooth psh functions.
Recall the definition of the sheaf C ∞ of smooth functions on X an from Definition 3.12.
The key tool of this step is to use that for certain X every lisse function f with ddc f = 0 is
automatically smooth (cf. [Thu05, Théorème 2.3.21]). These functions are the harmonic
functions and the corresponding sheaf is denoted by HX (cf. Definition 2.10). Note that
in general, every smooth function f with d′ d′′ f = 0 is harmonic.
Lemma 5.2. Let X be a smooth proper algebraic curve such that the sheaf HX of har-
monic functions on X an is a subsheaf of the sheaf C ∞ of smooth functions on X an .
Then every lisse function f : Y → R on a strictly affinoid domain Y of X an which is
subharmonic on the interior W := Y \∂Y of Y is globally psh-approximable on W . More
precisely, there is a monotone decreasing sequence of continuous functions fk on Y that
are smooth and psh on W , and converge uniformly to f on Y .
Proof. Since f is lisse, we can find a strictly semistable model Y such that f = F ◦ τY
on Y for a piecewise affine function F on S(Y). We construct continuous functions on
Y converging uniformly to f that are smooth and psh on W using techniques as in the
proof of Theorem 4.7.
   Let S be the set of points in S(Y)\∂Y that are contained in the support of the discrete
measure ddc F . Consider in the following a point x in S. Then ddc F > 0 in an open
neighborhood of x because f is subharmonic. The considered point x is either of type
II or III. If x is of type II, we may assume x to be a vertex of S(Y) and we denote by
ex,1 , . . . , ex,n the adjacent edges in S(Y) and by xi the second endpoint of ex,i . If x is of
type III, x is contained in the interior of an edge ex with endpoints x1 and x2 and we
denote by ex,1 and ex,2 the segments [x1 , x] and [x, x2 ] of ex . By blowing up Y, we may
assume that no xi belongs to S and that F restricted to every ex,i is affine.
S In both situations, type II or III, we can find a piecewise affine function Gx on Γx :=
  i=1,...,n ex,i such that
       i) Gx (x) = F (x),
      ii) Gx < F on Γx \{x},
     iii) ddc Gx = 0 in a neighborhood of x, and
     iv) (Gx )|ex,i is affine for every i = 1, . . . , n.
Choose εx,i > 0 with F (xi ) − Gx (xi ) > 2εx,i . Then there is a point yi ∈ (x, xi ) such
that F (yi ) = Gx (yi ) + εx,i , F < Gx + εx,i on [x, yi ) and F > Gx + εx,i on (yi , xi ].
Since S has only finitely many points and corresponding adjacent edges, we can set
ε0 := minx∈S,i εx,i . Then for every x ∈ S, every ex,i = [x, xi ], and every 0 < ε ≤ ε0 the
following inequalities
(5.1)            Gx (x) + ε − F (x) > ε/2,      F (xi ) − (Gx (xi ) + ε) > ε/2
hold.
   For every x ∈ S, the set Vx := (τY−1 (Γ◦x )) is an open neighborhood of x in W and by
construction these sets are pairwise disjoint. We define for every 0 < ε ≤ ε0 the following
function on Y
                            (
                              m 2ε (Gx ◦ τY + ε, f ) on Vx for x ∈ S,
(5.2)                 fε :=                                 S
                              f                       on Y \ x∈S Vx ,
30                                       V. WANNER


where mε is the smooth maximum defined in (4.6) (see proof of Theorem 4.7). By (5.1)
and property iii) of mε/2 in (4.6), the defined function coincides with Gx ◦ τY + ε in an
open neighborhood of x and with f in an open neighborhood of xi , where xi is the other
vertex for an adjacent ex,i = [x, xi ]. Thus, fε is continuous on Y .
   We will later use functions of this form to construct our sequence, but first we show
thatSfε is smooth and psh on W . By construction, there is an open neighborhood W ′ of
W \ x∈S Vx such that fε coincides with f and f = F ◦ τY is harmonic on W ′ . Since we
required that HX is a subsheaf of C ∞ and every harmonic function is psh by Proposition
2.11 and Theorem 4.7, the function fε is a smooth psh function on W ′ .
   On the other hand, for every x ∈ S the constructed function fε coincides with the
harmonic function Gx ◦ τY + ε on an open neighborhood of x, and so it is locally smooth
and psh at x as well. It remains to consider fε on τY−1 ((x, xi )) for every x ∈ S and
every adjacent ex,i = [x, xi ]. Since f and Gx ◦ τY + ε are harmonic, and so smooth
and psh on τY−1 ((x, xi )), one can show as in Step 5 in the proof of Theorem 4.7 that
fε = m 2ε (Gx ◦ τY + ε, f ) is still smooth and psh on τY−1 ((x, xi )). Altogether, fε is a
smooth psh function on W .
   With the help of the function fε defined in (5.2), we construct now a monotonically
decreasing sequence (fk )k∈N of smooth psh functions converging uniformly to f on Y .
For every k ∈ N, we define εk > 0 recursively starting with ε0 from above, and set
fk := fεk . To do so, we need to consider the subsets
                            [n                                        εk o
                   Ωk :=        y ∈ Vx | |Gx (τY (y)) + εk − f (y)| <
                                                                      2
                          x∈S

on which fk does not necessarily coincide with max(Gx ◦ τY + εk , f ) for some x ∈ S. For
a given εk , we choose εk+1 such that 0 < εk+1 < εk /3. Then Ωk ∩ Ωk+1 = ∅ for every
k ∈ N and εk → 0 for k → ∞.
        S that the sequence fk converges pointwise to f and fk+1 ≤ fk on Y . If
  We show
y ∈ Y \ x∈S Vx , then all fk coincide with f , and so both assertions are trivial. We
therefore assume that y ∈ Vx for some x ∈ S. In the case of y ∈ τY−1 (x), we have

                      fk (y) = Gx (x) + εk = F (x) + εk = f (y) + εk ,

and so fk (y) ≥ fk+1 (y) and fk (y) converges to f (y) for k → ∞. Now we consider the case
y ∈ Vx \{τY−1 (x)}. Then we can find an εN small enough such that f (y) − (Gx (τY (y)) +
εN ) > εN /2. Hence, for every k ≥ N we have f (y) − (Gx (τY (y)) + εk ) > εk /2, and so

                          fk (y) = max(Gx ◦ τY + εk , f ) = f (y).

Thus, fk (y) converges clearly to f (y). Next, consider an arbitrary k ∈ N and show
fk (y) ≥ fk+1 (y). If y ∈
                        / Ωk ∪ Ωk+1 , then

     fk+1 (y) = max(Gx (τY (y)) + εk+1 , f (y)) ≤ max(Gx (τY (y)) + εk , f (y)) = fk (y)

since εk > εk+1 . If y ∈ Ωk , by the choice of εk+1 , we have y ∈
                                                                / Ωk+1 . Thus,

     fk+1 (y) = max(Gx (τY (y)) + εk+1 , f (y)) ≤ max(Gx (τY (y)) + εk , f (y)) ≤ fk (y),

where the last inequality is true by property ii) following (4.6). Finally, let y ∈ Ωk+1 ,
and so y ∈
         / Ωk . Then Gx (τY (y)) + εk ≥ f (y) as εk+1 < εk /3, and so

          fk (y) = max(Gx (τY (y)) + εk , f (y)) = Gx (τY (y)) + εk ≥ f (y) + εk /2
   COMPARISON OF TWO NOTIONS OF SUBHARMONICITY ON NON-ARCHIMEDEAN CURVES 31


as y ∈
     / Ωk . By property ii) following (4.6), εk+1 < εk /3 and the last inequality, we get
                     fk+1 (y) ≤ max(Gx (τY (y)) + εk+1 , f (y)) + εk+1 /4
                              ≤ max(Gx (τY (y)) + εk , f (y) + εk /2)
                              ≤ fk (y).
  Thus, the sequence fk of continuous functions converges pointwise to the continuous
function f on Y and fk+1 ≤ fk . Since Y is compact, fk converge uniformly by Dini’s
theorem. We have already seen above that every fk is smooth and psh on W .         
  Before we use this lemma to prove a monotone regularization theorem in the setting of
Chambert-Loir and Ducros for Mumford curves, we recall the definition of these curves.
Definition 5.3. A smooth proper curve X of genus g ≥ 1 over K is called a Mumford
curve if there is a semistable model X such that all irreducible components of the special
fibre are rational (cf. [Ber90, Theorem 4.4.1]).

Corollary 5.4. Let X be a smooth proper curve over K. If K    e is algebraic over a finite
field or X is the projective line or a Mumford curve, then every continuous psh function
f : W → R on an open subset W of X an is locally psh-approximable. More precisely, the
sequence of smooth psh functions can be chosen monotonically decreasing.
Proof. At first, note that in the given situation HX is a subsheaf of C ∞ on X an , which
is a consequence of [Thu05, Théorème 2.3.21] (see [Wan16, Corollary 5.3.21]). We ad-
ditionally use [Ber90, Theorem 4.4.1] in the case of a Mumford curve. Hence, we may
apply Lemma 5.2.
   To prove the corollary, we have to show that every point x in W has an open neigh-
borhood in W such that f is a uniform limit of smooth psh functions. The continuous
psh function f is subharmonic by Theorem 4.7, and we therefore can use Thuillier’s
monotone regularization theorem (see Proposition 2.8). We can find for every x ∈ W a
relatively compact neighborhood W ′ of x in W and a decreasing net hfj i of lisse subhar-
monic functions on W ′ converging pointwise to f . Let Y be a strictly affinoid domain
in W ′ having x in its interior Y ◦ . Then the decreasing net hfj i converges uniformly to
the continuous function f on the compact set Y by Dini’s theorem. Thus, one can con-
struct inductively a decreasing sequence of lisse subharmonic functions on W ′ converging
uniformly to f on Y and we write (fk )k∈N for this sequence.
   We have seen in Lemma 5.2 that each fk is the uniform limit of a decreasing sequence
of smooth psh functions on Y ◦ . Hence, we can choose a decreasing sequence of smooth
psh functions on Y ◦ converging uniformly to f .                                        
Remark 5.5. Note that there are curves such that the sheaf HX of harmonic functions
is not a subsheaf of the sheaf C ∞ of smooth functions on X an . A counter example of such
a curve can be constructed by the proof of [Thu05, Théorème 2.3.21] (see for example
[Wan16, Corollary 5.3.23]). For those curves we do not know whether every psh function
is locally psh-approachable.
