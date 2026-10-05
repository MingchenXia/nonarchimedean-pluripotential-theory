Source-contained audit packet for new100 only. No current research102 output is supplied.


BEGIN MATHEMATICAL DATA: Complete NEW unreviewed proof100
---
title: "One continuous factor in generated Bedford–Taylor calculus"
subtitle: "Bounded Borel multipliers, a larger compatible-current class, and the unresolved original P21.3"
author: "Research draft; no independent verification claimed"
date: "5 October 2026"
geometry: margin=1in
fontsize: 11pt
header-includes:
  - \setlength{\emergencystretch}{3em}
---

# Result and unchanged question

**Original P21.3 is not solved here.** This paper reconstructs the bounded-generated-potential argument and the proposed mixed symmetry from primary ordinary CLD calculus. It proves a further consequence: differentiation by a **locally bounded, possibly discontinuous generated-Psh potential** preserves the continuous-pair Bedford–Taylor property. This consequence does not require continuity of that differentiating potential. Continuity of the original test pair supplies the continuous factor in the symmetry theorem. We also prove a limited obstruction to a fixed convolution regularizer on actual split-torus coordinates. We obtain neither an exhaustion of arbitrary currents nor an analytic counterexample.

Throughout, $K$ is any complete non-Archimedean field, including a trivially valued field. The space $X$ is good, separated, strict, boundaryless, and pure of analytic dimension $n\geq2$. All opens are **ordinary** opens. Put $D=\mathrm d'\mathrm d''$. A current $T$ of bidegree $(p,p)$ is ordinary CLD, **middle-positive**, and satisfies both $\mathrm d'T=\mathrm d''T=0$. Except where stated otherwise, $0\leq p\leq n-1$. We retain the canonical calibration, singularities, nilpotents, and actual generic component lengths. Write $[f]=f\delta_X$, where $\delta_X$ is the canonical integration current. The original assertion is

$$
 \text{for every }W\subset X,\ T,\ U,V\in\operatorname{Psh}(W)\cap C(W),
 \qquad D[U]=D[V]\ \Longrightarrow\ D(UT)=D(VT).                 \tag{Q}
$$

Here $U,V$ are finite real continuous sections of the **generated** Psh sheaf, as defined below. No equality $\operatorname{Psh}\cap C=\operatorname{CPsh}$ is assumed. A negative answer to (Q) would require an actual analytic space in this scope, a separately admissible pair, its upstairs canonical curvature equality, an allowed current, and a compact ordinary smooth test detecting a nonzero difference. Nothing in the diagnostic example below supplies such data.

The main statements proved are:

1. For every locally bounded real generated-Psh $u$, the Borel ordinary product $uT$ exists, and $D(uT)$ is middle-positive and doubly closed, including every sheafified ordinal stage.
2. If $p\leq n-2$, $u$ is locally bounded real generated Psh, and $v$ is finite continuous generated Psh, then
   $$D\bigl(uD(vT)\bigr)=D\bigl(vD(uT)\bigr).                    \tag{S}$$
3. If $S$ already satisfies (Q) on all subopens, then so does $D(vS)$ for **any locally bounded real generated-Psh $v$**, in the allowed output degree. Smooth positive closed factors and weak positive limits also preserve this property.

These are ordinary-current statements for all original fields and analytic hypotheses. Statement 3 constructs a range of compatible currents; it does not identify that range with all positive closed currents.

# Exact primary premises and applicability

The sole mathematical primary text used in the proofs below is [CLD], *Formes différentielles réelles et courants sur les espaces de Berkovich*, arXiv:1204.6277v2, 25 July 2025. The following are the precise imported facts. Full selected statements and pertinent printed proofs are retained in `P21.3-primary-evidence.md`, with inclusive one-based LF intervals, version, and hashes. These imported calculus theorems are external premises, not foundational theorems independently reproved here. The complete primary text was copied from the explicitly bound read-only public file; only selected passages were read.

**P0: analytic and ordinary-local scope.** Analytic spaces have compact-neighbourhood bases; good analytic spaces have affinoid-neighbourhood bases; ordinary opens are analytic domains [11.1.7]. A topologically separated pure $n$-dimensional analytic space has its canonical calibrated level-$n$ tropical structure, compatible with analytic-domain restriction [15.7.1–2]. A good Hausdorff analytic space is locally holomorphically separated and hence locally differentially separated [15.2.2–4]. On such a space compact supports admit smooth cutoffs, finite nonnegative smooth localization, and uniform approximation of compact continuous scalars by compact smooth scalars [15.2.5–9]. Global paracompactness is not required for these compact-support assertions. The hypotheses apply to each original ordinary open, in either valuation regime. Boundarylessness is retained when invoking Stokes.

**P1: generated functions.** Definition 8.1.1 defines Psh as the smallest ordinary subsheaf of functions valued in $\mathbb R\cup\{-\infty\}$ containing smooth functions of positive smooth Hessian and closed under decreasing sequential limits. Lemma 8.1.4 describes the sheafified ordinal construction. We reconstruct stabilization, upper semicontinuity, and the bounded-final-function steps rather than relying on the printed proof's extraneous integrability qualification. Definition 8.1.7 instead generates CPsh inside continuous functions by uniform sequential closure. The printed reverse recognition in 8.1.11 is not used.

**P2: middle positivity.** Every compact symmetric smooth $(q,q)$ test is a difference of two compact middle-positive tests, provided its support is contained in a paracompact locally differentially separated open [6.5.2]. The statement explicitly includes compact supports on almost-good analytic spaces; good suffices here. Middle-positive currents are symmetric and nonnegative on middle-positive complementary tests; positivity is ordinary-local [7.2.1–4]. Positive smooth factors preserve middle-positive currents [7.2.7(b)], since wedges of middle-positive forms are middle-positive [1.2.12, 1.10.3, 3.5.5]. This is not a replacement by strongly positive tests. A current and its negative cannot both be middle-positive unless the current is zero [7.2.3; also proved below using the decomposition].

**P3: coefficient measures.** On a locally differentially separated level-$n$ space, positive scalar currents correspond to unique positive Radon measures [7.2.8]. For middle-positive $T$ and a positive complementary smooth form $\eta$, the associated coefficient measure satisfies
$$\int g\,d\mu_{T,\eta}=\langle T,g\eta\rangle$$
for compact smooth scalars $g$, and has compact support when $\eta$ does [7.2.11]. Borel multiplication is stated in 7.2.12. Its order-zero justification for the middle cone is reconstructed below; the strongly-positive spanning inference in the broader wording of 7.2.9 is not imported.

**P4: chart topology and finite-dimensional domination.** In Euclidean coordinates the middle cone of symmetric $(q,q)$ superforms is the positive-semidefinite signed coefficient matrix cone on the $q$th exterior power [1.2.6–7]; positivity on polyhedral spaces is tested on tangent faces [1.10.1]. Compact moment images are finite polyhedral sets [12.2.4]. We use only polyhedrality, not its printed claim that every moment image has dimension equal to that of the source: a constant moment already disproves that clause. Test topology is the inductive topology for fixed compact supports and fixed moment presentations, with cellwise coefficient seminorms [7.1.1–3]. Compact smooth localization reduces continuity to such a chart. Compact analytic neighbourhoods can be finite unions of affinoids, so no assertion that one arbitrary compact support lies in a single affinoid is needed.

**P5: ordinary differential calculus.** Forms have compatible restriction, products, pullback and Leibniz rules [3.3.10–12]. Ordinary currents form a sheaf [7.1.6–7]. Their differentials are continuous for weak convergence and satisfy
$$ (\mathrm d')^2=(\mathrm d'')^2=0,\quad
\mathrm d''\mathrm d'=-\mathrm d'\mathrm d'',\quad DJ=JD,\quad
\langle DR,\alpha\rangle=\langle R,D\alpha\rangle                 \tag{2}
$$
[7.7.1–5]. For smooth $s$ and symmetric doubly closed $T$, $D(sT)=Ds\wedge T$ [8.5.3–4]. This assertion is used with actual compatible degrees, independently of the printed bidegree/bidimension indexing in 8.5.3. Multiplication by a smooth doubly closed even-degree form commutes with the differentials, by the same Leibniz rule in duality. Both closedness equations are checked.

**P6: canonical integration.** $\delta_X=[1]$ is positive and doubly closed on the original boundaryless space [15.7.1, 7.7.4; positivity of the canonical calibration is used in 5.8.1–5]. For a pure closed analytic subspace the integration current equals its associated analytic cycle current, with actual generic lengths [16.6.3]. No nilreduction is substituted in our construction.

**P7: weak multiplication, reconstructed.** Lemma 8.5.1 states: if positive currents $T_j\to T$ weakly and continuous functions $u_j\to u$ locally uniformly, then $u_jT_j\to uT$. Its full statement and proof were read. We give the middle-cone proof, including the fixed-function net variant, in Lemma 2. We do not apply it to a discontinuous multiplier.

**P8: torus coordinates, diagnostic only.** [12.1.1–5] describes the analytic split torus, its Laurent characters, and their functorial tropicalizations. In the diagnostic we fix $K=\mathbb Q_2$ and $X=(\mathbf G_{m,K}^2)^{\mathrm{an}}$, a good separated strict smooth boundaryless surface. The explicitly displayed Laurent monomial changes are analytic automorphisms. Their effect on logarithmic coordinates follows directly by multiplicativity. No theorem about arbitrary current ascent, descent, classification, or density is imported.

# Middle-positive Borel products and two different limits

**Lemma 1 (ordinary Borel product).** If $T$ is middle-positive, every locally bounded real Borel $b$ defines an ordinary symmetric order-zero current $bT$. It agrees with smooth multiplication and ordinary restriction. For a compact symmetric complementary test $\beta$, there is a canonical finite signed Radon measure $\mu_{T,\beta}$, linear in $\beta$ and supported in $\operatorname{supp}\beta$, such that
$$ \langle bT,\beta\rangle=\int b\,d\mu_{T,\beta}.               \tag{3}$$
If $b_j\downarrow b$ with a common finite absolute bound on each compact, then $b_jT\to bT$ weakly. Also, for locally uniform nets of continuous functions $b_a\to b$ and a **fixed** $T$, $b_aT\to bT$ weakly.

*Proof.* Write $\beta=\eta_1-\eta_2$ with compact middle-positive tests, and set $\mu_{T,\beta}=\mu_{T,\eta_1}-\mu_{T,\eta_2}$. Two decompositions give the same integral against compact smooth scalars, hence against compact continuous scalars by P0, hence the same signed Radon measure. This proves independence and linearity. Scalars supported away from $\operatorname{supp}\beta$ pair to zero. Smooth density within that open shows the signed measure vanishes there, proving its intrinsic support assertion. Use the symmetric projection for general tests; the antisymmetric part pairs to zero.

It remains to prove ordinary-current continuity for Borel $b$. After compact nonnegative smooth localization, consider tests $\rho f^*a$ in one moment chart. Choose a compact analytic neighbourhood $C$ of $\operatorname{supp}\rho$ within the chart, using finitely many affinoid neighbourhoods if necessary. Its moment image $P$ has a finite cellular subdivision. Let $q=n-p$ be the complementary test degree and fix a Euclidean metric in the moment target. The form
$$\Theta=\sum_i\mathrm d'x_i\wedge\mathrm d''x_i$$
has $\Theta^q$ positive definite on the exterior power of every tangent face of dimension at least $q$. On smaller faces every $(q,q)$ restriction is zero. With $a$ symmetric, finitely many tangent spaces give a fixed constant $c$ such that
$$c\|a\|_{P,0}\Theta^q+a\geq0,\qquad
  c\|a\|_{P,0}\Theta^q-a\geq0.                               \tag{4}$$
Here the norm is the maximum of the cellwise coefficient norms in fixed face coordinates. On each face this is the operator-norm bound against the fixed positive-definite matrix; take the maximum over the finitely many faces. For $q=0$ use $\Theta^0=1$. These are middle-cone inequalities, without decomposability of the exterior vectors.

Pull back and multiply by $\rho\geq0$. Positive coefficient measures give
$$|\mu_{T,\rho f^*a}|\leq c\|a\|_{P,0}\mu_{T,\rho f^*\Theta^q}.$$
Indeed both signed inequalities against the measure on the right hold; the positive and negative parts on a Hahn decomposition give the total variation inequality. Consequently
$$ |\langle bT,\rho f^*a\rangle|
 \leq c\|b\|_{\operatorname{supp}\rho}\|a\|_{P,0}
          \langle T,\rho f^*\Theta^q\rangle.                   \tag{5}$$
The factor depending on $b$ is finite. The symmetric projection is continuous, and P4's localized topology now proves order-zero continuity for all tests. If $b\geq0$, its pairings with positive tests are nonnegative. Restriction compatibility follows by extending compact tests by zero and comparing their coefficient measures against smooth scalars; uniqueness of the measures gives the result. Smooth multiplication agrees by construction.

For the decreasing limit use the two finite positive measures of a fixed test decomposition. On their compact support let $g_j=b_j-b\downarrow0$, with $0\leq g_j\leq M$. For $\epsilon>0$ the sets $E_j=\{g_j\geq\epsilon\}$ decrease to the empty set. Countable additivity and finiteness give $\mu(E_j)\to0$, and
$$0\leq\int g_j\,d\mu\leq\epsilon\mu(C)+M\mu(E_j).$$
Let $j\to\infty$ and then $\epsilon\to0$. This proves the required measure convergence for each positive coefficient. For the locally uniform net use instead
$$ |\langle(b_a-b)T,\beta\rangle|
 \leq\|b_a-b\|_C\langle T,\eta_1+\eta_2\rangle.              \tag{6}$$
The compact $C$ and constant do not depend on the index. No assertion about bounded pointwise convergence of arbitrary nets is made. $\square$

**Lemma 2 (continuous multiplier on varying currents).** Let $S_a\to S$ weakly be a net of positive ordinary currents, whose limit is an ordinary current. For fixed continuous real $v$, $vS_a\to vS$ weakly. The limit is positive. The same conclusion holds for continuous $v_a\to v$ locally uniformly.

*Proof.* Positivity and symmetry pass by evaluation on fixed tests. For a compact symmetric test $\beta=\eta_1-\eta_2$, weak convergence gives convergence, hence an **eventual** bound, of $\langle S_a,\eta_1+\eta_2\rangle$. One does not need all indices of a net to have bounded masses. With $C$ the union of the supports, approximate $v$ uniformly on $C$ by smooth $g$. To obtain $g$, multiply $v$ by a compact cutoff equal to one near $C$, then apply P0. We have
$$
\begin{split}
|\langle vS_a-vS,\beta\rangle|
 &\leq\epsilon\langle S_a,\eta_1+\eta_2\rangle
       +|\langle S_a-S,g\beta\rangle|
       +\epsilon\langle S,\eta_1+\eta_2\rangle.
\end{split}                                                    \tag{7}
$$
First take the weak limit for fixed $g$, then let $\epsilon\to0$. The symmetric projection handles arbitrary tests. For varying $v_a$, the extra error is bounded by $\|v_a-v\|_C\langle S_a,\eta_1+\eta_2\rangle$, which tends to zero on that same eventual tail. This proves precisely the claimed net variant of 8.5.1. $\square$

The distinction is essential: in Lemma 1 the positive coefficient measures belong to **one fixed current**; in Lemma 2 the currents vary and the multiplier is continuous. For example on $\mathbb R$, $\delta_{1/j}\to\delta_0$ but multiplication by $\mathbf1_{\{0\}}$ does not commute with this weak limit. This elementary measure example is only a warning about the limit operation; it is not an analytic P21.3 counterexample and its indicator is not asserted to be generated Psh.

**Lemma 3 (smooth-factor identities).** A smooth doubly closed form $\gamma$ of even total degree commutes with current differentiation. For positive $T$ and locally bounded Borel $b$,
$$b(T\wedge\gamma)=(bT)\wedge\gamma                           \tag{8}$$
whenever $T\wedge\gamma$ is positive; the same identity extends by differences of positive currents. In particular it applies to positive smooth Hessians and positive smooth decorations.

*Proof.* Differential commutation follows by applying the ordinary form Leibniz rule to $\gamma\wedge\alpha$ in differential duality, since both first derivatives of $\gamma$ vanish. For (8), the coefficient measure of a test $\alpha$ for $T\wedge\gamma$ is the coefficient measure of $\gamma\wedge\alpha$ for $T$. This equality follows first against smooth scalars and then from uniqueness of signed coefficient measures. Integration of $b$ proves (8). Differences are legitimate: equality of positive-current decompositions implies equality of every signed coefficient measure, so Borel multiplication of a current expressible as a finite difference of positive currents is independent of its such decomposition. $\square$

# Every sheafified ordinal, with bounded final sections

Let $\mathcal P_0$ be the sheaf of smooth positive-Hessian functions. Let $\mathcal P_{\xi+1}$ consist of sections which **ordinary-locally** are decreasing limits of sequences in $\mathcal P_\xi$. At a limit $\lambda$, membership means ordinary-local membership in an earlier $\mathcal P_\xi$, $\xi<\lambda$. These are sheaves and they increase: constant sequences keep earlier sections, and earlier ranks embed in limit stages.

Each stage consists of upper-semicontinuous functions. At a successor $u=\inf_j u_j$, the set $\{u<a\}=\bigcup_j\{u_j<a\}$ is open. Upper semicontinuity is local, giving the limit step. A finite section is consequently Borel. No countability of $X$ is needed for real-valued Borel measurability.

The construction stabilizes and exhausts Psh. All pairs (open, section of the ambient function sheaf on it) form a set. Strict increases at every successor through ordinals beyond the cardinal successor of this set are impossible. Once $\mathcal P_\kappa=\mathcal P_{\kappa+1}$, the successor operation is fixed, and subsequent limit stages add nothing because these are sheaves. This stationary sheaf contains the smooth generators and every decreasing sequential limit on a fixed open: that limit belongs to rank $\kappa+1=\kappa$. Minimality gives Psh inside it, while every stage is inside Psh by induction and locality. We impose no integrability qualification absent from Definition 8.1.1.

All assertions below are simultaneous on every ordinary open, with the current restricted to that open. No flattening of the sheafified construction into one decreasing smooth sequence is claimed.

**Theorem 1 (bounded generated positivity).** For every locally bounded real $u\in\operatorname{Psh}(W)$ and every original positive doubly closed $T$, $D(uT)$ is middle-positive and doubly closed.

*Proof.* Induct on the rank of $u$, for all opens. At rank zero, $D(uT)=Du\wedge T$, positive by P2. At a successor choose an ordinary neighbourhood $N$ on which $u_j\in\mathcal P_\xi(N)$ decrease to the final $u$. Since $u_j\geq u$ and the stages never allow $+\infty$, each $u_j$ is finite everywhere on $N$. The locally bounded final $u$ bounds every predecessor below. Upper semicontinuity bounds the finite $u_j$ locally above, so each predecessor is locally bounded and the inductive assertion applies.

On any compact $C\subset N$ a finite cover of the local bounds gives
$$a\leq u\leq u_j\leq u_1\leq b\quad\hbox{on }C,\quad j\geq1. \tag{9}$$
Thus Lemma 1 gives $u_jT\to uT$ weakly, using the fixed coefficient measures of $T|_N$. Equation (2) gives $D(u_jT)\to D(uT)$. Positive pairings and symmetry pass to the limit. Restriction compatibility and ordinary locality give positivity on $W$.

At a limit rank, each point has an ordinary neighbourhood with membership in some earlier rank; boundedness restricts there. Apply the earlier assertion and current locality. Stabilization proves the assertion for all locally bounded real generated sections. The differential identities give $\mathrm d'D(uT)=\mathrm d''D(uT)=0$. For $p=n-1$ its tests are scalars, and for $p=0$ they have degree $(n-1,n-1)$; both endpoints are included. All measures and differential identities are those of the original calibrated analytic space. $\square$

The same theorem may be used successively: for locally bounded real generated potentials $f_1,\ldots,f_m$ and $m\leq n-p$, an ordered recursion $T_0=T$, $T_k=D(f_kT_{k-1})$ defines positive doubly closed currents of degrees $(p+k,p+k)$. The last current may have top degree. No symmetry between arbitrary discontinuous factors is inferred from this ordered construction.

If both $h$ and $-h$ are locally bounded generated Psh, Theorem 1 makes $D(hT)$ and its negative positive. Positive-test decomposition and symmetry force $D(hT)=0$. This is a sufficient two-sign condition. For $h=U-V$, the given memberships of $U,V$ and the equation $D[h]=0$ have not supplied it.

# Mixed symmetry with one continuous factor

**Theorem 2.** Suppose $0\leq p\leq n-2$. Let $v$ be a finite continuous generated-Psh section and $u$ any locally bounded real generated-Psh section on $W$. Then (S) holds as an identity of actual ordinary currents.

*Proof.* Theorem 1 makes both inner currents positive and doubly closed. Their Borel products are well-defined by Lemma 1. Fix $v,T$ and induct on the rank of $u$, simultaneously on all subopens.

If $u$ is smooth, $Du$ is a smooth positive doubly closed form. P5 and Lemma 3 give
$$
 D(uD(vT))=Du\wedge D(vT)
          =D\bigl((vT)\wedge Du\bigr)
          =D\bigl(v(T\wedge Du)\bigr)
          =D(vD(uT)).                                         \tag{10}
$$
Here the middle differentiation is on currents, and does not differentiate $v$ as a smooth function.

At a successor restrict to $N$ carrying $u_j\downarrow u$ of the preceding stage. The bounded-final selection (9) makes every $u_j$ locally bounded. The induction gives
$$D(u_jD(vT))=D(vD(u_jT)).                                   \tag{11}$$
For the left-hand side, apply Lemma 1 with the **fixed positive** current $D(vT)$; its finite coefficient measures and (9) give $u_jD(vT)\to uD(vT)$ weakly. For the right-hand side, Lemma 1 with the fixed $T$ gives $D(u_jT)\to D(uT)$. These are all positive by Theorem 1. Lemma 2 applies with the **continuous** multiplier $v$, so $vD(u_jT)\to vD(uT)$. Continuity of $D$ proves the desired equality on $N$, and ordinary locality gives it on $W$.

At a limit rank use earlier-rank membership on each ordinary neighbourhood, then locality. Stabilization concludes the proof. Predecessors may be discontinuous; they were neither replaced by continuous predecessors nor recognized as CPsh. The varying-current step never multiplies by a discontinuous function. $\square$

**Corollary 2.1 (at most one discontinuous factor).** In the ordered recursion following Theorem 1, suppose all $m$ potentials are continuous except possibly one locally bounded real generated-Psh potential. Then the result is independent of their permutation, for every original $T$ and $m\leq n-p$.

*Proof.* Any adjacent interchange has at least one continuous factor and is (S) applied to its inner positive closed current. The complementary degree allows the two differentiations. Applying subsequent outer operations to equal positive currents preserves equality, even when that one remaining outer potential is Borel. Adjacent transpositions generate all permutations. $\square$

This is permutation independence, not dependence only on canonical curvatures for arbitrary $T$. In particular $m=1$ yields no new relation-preservation assertion.

**Corollary 2.2 (signed continuous difference).** If $h=U-V$ with $U,V$ finite continuous generated Psh and $v$ finite continuous generated Psh, then
$$D(hD(vT))=D\bigl(vD(hT)\bigr).                             \tag{12}$$
The right-hand product is defined as a difference of products with the positive currents $D(UT)$ and $D(VT)$; Lemma 3 makes this definition independent of such a positive decomposition. Subtract the two instances of (S) to prove the formula. No generated-Psh membership of either sign of $h$ is assumed.

# A larger class of compatible currents

Call a positive doubly closed $S$ on $W$ **pair-compatible** when it satisfies (Q) on every ordinary subopen of $W$. This term abbreviates a precise property; it is not a classification of positive currents. The base $\delta_X|_W$ is pair-compatible because $U\delta_X=[U]$ and $V\delta_X=[V]$.

**Theorem 3 (bounded-potential closure).** Pair-compatible currents are preserved by addition and nonnegative scalar multiplication in a fixed degree, ordinary restriction and local gluing, weak positive limits in a fixed degree, and wedge with a smooth middle-positive doubly closed form in any permitted degree. If $S$ has degree $(p,p)$ with $p\leq n-2$ and $v$ is **any locally bounded real generated-Psh section**, then $D(vS)$ is also pair-compatible of degree $(p+1,p+1)$.

*Proof.* Addition, scaling and restriction are immediate by linearity. For an ordinary cover, restrict any pair and use the current sheaf to prove the equality; positivity and closedness are local as well. If $S_a\to S$ weakly as positive currents, the limit is positive and both closedness equations pass to the limit. On any subopen and for a fixed continuous pair, Lemma 2 gives $US_a\to US$ and $VS_a\to VS$. The differential passes to the limit. Restriction preserves the assumed weak convergence because tests extend by zero.

For a smooth positive doubly closed decoration $\gamma$, $S\wedge\gamma$ is positive and closed. Lemma 3 gives
$$D\bigl(h(S\wedge\gamma)\bigr)=D(hS)\wedge\gamma=0$$
for every admissible continuous difference $h$. Degrees are restricted to $p+\deg\gamma\leq n-1$.

For the final assertion work on an arbitrary subopen $O\subset W$, with an admissible continuous pair $U,V$ there. Theorem 1 gives positivity and closedness of $D(vS)$, $D(US)$ and $D(VS)$. Apply Theorem 2 with the bounded, possibly discontinuous factor $u=v|_O$ and **continuous factor** $U$, and then with continuous factor $V$. This gives
$$
 D(UD(vS))=D(vD(US)),\qquad
 D(VD(vS))=D(vD(VS)).                                        \tag{13}
$$
Pair compatibility of $S$ says $D(US)=D(VS)$ as positive currents. Their Borel products with the same locally bounded $v$ are therefore equal by Lemma 1. Equation (13) proves pair compatibility of $D(vS)$ on $O$. Since $O$ was arbitrary, the property is genuinely every-open. No limit involving a discontinuous multiplier on varying currents has been used. $\square$

This last argument strengthens the continuous-differentiating-factor closure proposed in the supplied unreviewed draft. It is obtained by orienting the one-continuous-factor identity with $U,V$ as the continuous factors. In particular the property persists through ordered differentiations by several locally bounded discontinuous generated potentials; this does **not** interchange two discontinuous factors or extend the original pair condition to discontinuous pairs.

One can now form local cones from $\delta_X$ by these operations and weak positive closure, with degree fixed at each limit. All their members are actual ordinary positive doubly closed compatible currents. The assertion about this cone is a mathematical closure theorem. It does not mean that an arbitrary original current lies in it, locally or globally.

# Investigation of arbitrary-current regularization

The preceding calculus makes exhaustion a substantive next target: show that every original current locally lies in the weak positive closure of the compatible currents just constructed. The following small geometric calculation identifies a failure of one particularly rigid way of attempting that step.

**Proposition 4 (no fixed mollifier natural under both monomial shears).** Let $\mu$ be a compactly supported positive probability measure on $\mathbb R^2$. Define the scalar translation convolution
$$K_\mu f(x)=\int f(x-z)\,d\mu(z),\qquad f\in C_c^\infty(\mathbb R^2).$$
Suppose the same operator commutes with pullback by both
$$ A(x,y)=(x+y,y),\qquad B(x,y)=(x,x+y).$$
Then $\mu=\delta_0$. Thus no nontrivial compactly supported smooth probability mollifier has these two commutation properties. These changes occur on the actual analytic surface $X=(\mathbf G_{m,\mathbb Q_2}^2)^{\mathrm{an}}$ as monomial automorphisms.

*Proof.* Commutation with $A$ gives, at $x=0$,
$$\int f(-Az)\,d\mu(z)=\int f(-z)\,d\mu(z)$$
for all compact smooth $f$. Smooth density determines finite Radon measures, so $A_*\mu=\mu$. Similarly $B_*\mu=\mu$. Their invertibility implies their supports and all positive and negative iterates preserve the compact support. If $(x,y)$ belongs to this support, then $A^k(x,y)=(x+ky,y)$ belongs for every integer $k$. Compactness forces $y=0$. Likewise $B^k(x,0)=(x,kx)$ forces $x=0$. The probability measure is supported on $\{0\}$, proving the assertion.

The Laurent monomial maps
$$ (z_1,z_2)\longmapsto(z_1z_2,z_2),\qquad
   (z_1,z_2)\longmapsto(z_1,z_1z_2)$$
have monomial inverses and are analytic automorphisms of that torus. On $(\log|z_1|,\log|z_2|)$ they induce exactly $A,B$. This is an actual analytic-coordinate obstruction to using one unchanged scalar convolution kernel under both coordinate descriptions. $\square$

This proposition has deliberately limited force. A regularizer may transform its kernel with coordinates, depend on the finite collection of moments to be controlled, or use a directed system of such collections. Proposition 4 excludes none of these possibilities, and does not imply that a compatible analytic current regularization is impossible. The underlying torus is already in familiar positive geometric ranges. It supplies no pair or product defect. Extending convolution to coefficients of forms or currents would first have to resolve its coordinate dependence, and then support on the moment image, face positivity, both differential equations, chart nullity, and compatibility with every further analytic-unit moment. Our proof constructs no such extension.

There is a separate elementary failure in a proposed positive partition-of-unity gluing of chartwise regularizations. If $R_i$ are doubly closed currents and $\rho_i$ smooth nonnegative scalars with $\sum_i\rho_i=1$ near a compact support, then
$$\mathrm d'\Bigl(\sum_i\rho_iR_i\Bigr)
    =\sum_i\mathrm d'\rho_i\wedge R_i,$$
and analogously for $\mathrm d''$. The right-hand side is zero if the $R_i$ agree on overlaps, but the partition identity alone does not make it zero. For example on Euclidean $\mathbb R^2$, take the closed positive $(0,0)$ currents $R_1=[1]$, $R_2=2[1]$ and $\rho_1=\rho$, $\rho_2=1-\rho$ with nonconstant smooth $0<\rho<1$. Their glued function current is $[2-\rho]$, which is not first-closed. This is a calculus obstruction to that gluing operation, not an analytic counterexample to (Q). No correction preserving positivity and both closedness equations has been constructed here.

Neither scalar smooth density nor the middle-positive coefficient bound (5) supplies the missing closed-current approximation. Equation (5) controls evaluation of a **given** current; it does not change its coefficients into closed smooth analytic forms. A strong-current restriction map also supplies no positive closed lift of every ordinary current and no identification of a restricted strong product with the Borel product (3).

# The exact unproved analytic step and comparison with the residual scope

The concrete sufficient exhaustion statement left unproved is:

> For every original $K,X,p$, every ordinary $W$, every allowed positive doubly closed current $T$, and every $x\in W$, there is one ordinary neighbourhood $N\subset W$ and a net of actual positive doubly closed currents of degree $(p,p)$ on $N$, each obtained locally from the original canonical integration current by the operations of Theorem 3, converging weakly to $T|_N$ against **all** ordinary compact smooth tests, including every analytic-unit moment refinement.

Theorem 3 would imply (Q) from this statement. We have not proved it, and the hypothesis is not a reformulation of positivity or a consequence of scalar density. It may be stronger than necessary. A direct preservation theorem for arbitrary $T$, or a valid generating construction for both signs of $U-V$ on one fixed ordinary neighbourhood, could instead resolve the original problem. In that latter route, Theorem 1 and pointedness would apply. Neither construction has been found here.

Mixed symmetry itself stops short of the target: for arbitrary $T$, equation (12) still contains $D(hT)$ on its right-hand side. Knowing $D[h]=0$ identifies $D(h\delta_X)$, not $D(hT)$. Using (12) to declare the latter zero would assume the original assertion. Likewise equal canonical curvatures of separately generated $U,V$ do not give equal curvatures of their unrelated decreasing predecessors. Our induction proves positivity and the correctly oriented symmetry, but does not preserve an arbitrary signed relation at predecessor ranks.

The catalogue's granted strict real-PL theorem restricts the function class and excludes trivial valuation; the granted pure-curve recognition is intrinsically one-dimensional. Neither is used as a premise of the above higher-dimensional proofs. An ordinary ambient curvature equation has not been restricted to arbitrary curves or ascended under arbitrary analytic scalar extensions. Semistable-model existence, classical recognition of a general difference, and ordinary harmonic approximation on a fixed neighbourhood are not assumed. A specified-open cover and an actual ordinary-open basis remain distinct. Every local closure assertion here is proved by restricting to the very subopen carrying the pair, not by turning a chart cover into a basis.

Thus the new bounded-differentiating-factor closure retains all fields, every original ordinary open, singularities, nilpotents, middle positivity, and every permitted degree **within a constructed-current class**. It does not remove arbitrary-current quantification. No counterexample in the original separately admissible continuous pair class has been produced. The unchanged universal statement (Q) remains unproved in this work; `candidate=false`.

# Reproducibility and evidence limits

The artifacts are:

- Frozen input bytes: `input-original.json`.
- Exact task extraction: `task-original.json`.
- Exact assignment extraction: `assignment-original.txt`.
- Readable proof core: `P21.3-core.md`.
- Proof with literal primary evidence: `P21.3-argument.md`.
- Standalone typeset paper: `P21.3-paper.tex` and `P21.3-paper.pdf`.
- Exact imported premises and applicability: `premises.json`.
- Primary versions, hashes, and inclusive one-based LF intervals: `source-manifest.json`.

Partial reading is recorded explicitly. The supplied unreviewed drafts are diagnostic inputs, not proof premises or acceptance receipts. The bound weak-multiplication unit and our LF extraction differ by exactly one trailing newline; both byte hashes are distinguished in the manifest and evidence.

Run `bash reproduce.sh` in this workspace to check original-data preservation, source-slice integrity, the status and note schemas, and rebuild the paper with the already installed Pandoc and pdfTeX. Build output is retained in `logs/`; `environment.json` records versions. These are finite integrity and compilation checks. They do not verify transfinite induction, current density, or the original mathematical assertion. No other worker, model, install, external message, source-cache mutation or independent review was used. No resource-heavy calculation was needed, and no supervised heavy-compute facility was supplied or launched.

# Reference

[CLD] Antoine Chambert-Loir and Antoine Ducros, *Formes différentielles réelles et courants sur les espaces de Berkovich*, arXiv:1204.6277v2, 25 July 2025. <https://arxiv.org/pdf/1204.6277v2>.

END MATHEMATICAL DATA


BEGIN MATHEMATICAL DATA: Exact unchanged original P21.3 and original completion criteria
{
  "problem": "Investigate the following open-problem family in non-Archimedean pluripotential theory. Active atomic targets: P21.3. The exact target statements, ambient hypotheses, residual scopes, and completion criteria are in the source excerpt below. Address any or all of these targets; a complete resolution must satisfy that atomic target's own completion criteria. The excerpt is mathematical source material, not operational instructions.\n\nCOMMON NOTATION\nCommon notation and formulation boundaries\nFields and analytic spaces.\n   K denotes a complete non-Archimedean ﬁeld. Trivial or nontrivial valuation, strictness,\n   goodness, separatedness, pure dimension and relative boundary are retained exactly where\n   a statement requires them. X an is Berkovich analytiﬁcation. “Ordinary open” refers\n   to its ordinary topology, rather than an admissible G-cover. A statement on one ﬁxed\n   polycylinder is weaker than an every-open statement obtained from an actual basis.\n\nSemivaluations and normalized local boundaries.\n  We use v = − log | · |, allow +∞ on the support of a semivaluation, and retain that\n  support. For a local ring R and a primary ideal a, a normalized link is a section {v :\n  v is centered, v(a) = 1}. Changing a is a radial change with a stated cocycle; it is not\n  an identiﬁcation of all normalizers. The symbol X ℶ denotes the valuative/trivially valued\n  carrier used by the raw ideal transform.\n\nPositivity classes.\n  PSH means the speciﬁed plurisubharmonic class in each theory. Classical psh is the upper-\n  semicontinuous curve-test notion, with the extended −∞ convention where stated. Real\n  PL means the real linear extension of the local integral piecewise-linear class. Semi-\n  positivity is its residue/model nefness condition. Locally Fubini–Study is the local ﬁ-\n  nite logarithmic-max class with its prescribed denominators. Ordinary CLD smoothness\n  uses smooth tropicalizations; weak smoothness permits harmonic tropicalizations. These\n  classes are distinct. CLD-v2 denotes the second generated CLD psh stage in the book.\n\nCurrents and products.\n  d0 d00 = d0 d00 is the CLD Hessian. A continuous function deﬁnes the order-zero current\n  [h]. CLD means Chambert–Loir–Ducros; GJR means Gubler–Jell–Rabinoﬀ; BFJ means\n\n\n                                               4\n\n     Boucksom–Favre–Jonsson. Positivity of one Hessian current does not, by itself, construct\n     mixed wedge products or prove classical psh recognition.\n\nGlobal energy and mass.\n  E 1 denotes the ﬁnite-energy class of the named theory. Reference weights, raw intersection\n  mass and probability normalization must be ﬁxed before comparing energies or measures.\n  Quotienting by R means uniqueness modulo additive constants. Zero top mass cannot be\n  divided into a probability measure. The aﬃne-cone probability operator is an explicitly\n  separate convention.\n\nComplex singularity data.\n         1,1\n  α ∈ HBC    (X, R) is a real Bott–Chern class. MP means Mesquita–Piccione, DXZ means\n  Darvas–Xia–Zhang, and BJ means Boucksom–Jonsson. I-equivalence records multiplier-\n  ideal data; P -equivalence records the ﬁner envelope/singularity data. The latter cannot\n  generally be recovered from the former, even at positive mass.\n\nPolyhedral normalization.\n   PA denotes piecewise-aﬃne functions. BMPS means Botero–Mazzon–Pille-Schneider. Lit-\n   eral integral slopes and the real scalar extension are separate conventions. In dimension\n   d, the polyhedral intersection convention diﬀers from the real Alexandrov measure by the\n   factor d! and the face multiplicity. Saturated tangent lattices and analytic multiplicities\n   are part of an analytic comparison.\n\n\n\n\nFULL FAMILY DOSSIER (original LaTeX source from the catalogue's controlling chapter; exact referenced proof inputs remain in the local source repository)\n\\subsection{The residual Bedford--Taylor problem}\n\nThe two original realization questions have been settled and retired.  The\nfull unbounded cross cannot literally be the image of a harmonic\ntropicalization whose source is compact, by\n\\cref{prop:verified-cross-compact-obstruction}.  Conversely,\n\\cref{prop:verified-cross-analytic-realization} constructs a reduced\nboundaryless analytic curve with a proper noncompact tropicalization onto\nthe cross, exhausted by compact harmonic-tropicalization charts, and an\neffective cycle whose current has weights \\((2,2,1,1)\\).  That construction\nrealizes the psh approximants and the defect after proper pushforward, but\nthe two curvature currents are unequal before pushforward.  It therefore\ndoes not answer the analytic Bedford--Taylor question upstairs.\n\nThe normal-curve theorem\n\\cref{prop:p213-normal-curve-arbitrary-valuation-current-revised} settles the\nordinary current problem on every connected good separated normal\nboundaryless pure analytic curve over a complete non-Archimedean field,\npossibly trivially valued: every positive closed current of bidegree\n\\((0,0)\\) is \\(c\\delta_Y\\).  It requires neither strictness nor a smoothness\nhypothesis and gives the full CLD Bedford--Taylor predicate.\n\nThe componentwise theorem\n\\cref{prop:p213-componentwise-arbitrary-valuation} settles the displayed\ncontinuous-pair problem for every good separated strict boundaryless pure\none-dimensional analytic space over either valuation regime, without\nreducedness or a smoothness hypothesis on component normalizations.  If\n\\((X_i)_i\\) are the irreducible components of \\(X_{\\mathrm{red}}\\), every\npositive closed current of bidegree \\((0,0)\\) has the unique locally finite\nexpression\n\\[\n                         T=\\sum_i c_i\\delta_{X_i},\n                         \\qquad c_i\\geq0.\n\\]\nNilreduction preserves the ordinary CLD calculus and current topology while\nthe fundamental integration current retains generic component\nmultiplicities.  The two local estimates\n\\cref{lem:p21p3-componentwise-normal-rigid-zero-atom,%\nlem:p213-trivial-gauss-rigid-zero-atom} prevent cancellation at conductor\nand component-intersection points in the nontrivial and trivial valuation\nregimes, respectively.\n\nA separate comparison now applies in every dimension $n\\geq1$ and over\nevery complete non-Archimedean field:\n\\Cref{cor:ch16-cpsh-component-curvature} proves on every ordinary open\nthat equal canonical curvatures of an arbitrary continuous\n$\\operatorname{CPsh}$ pair are equal against every reduced analytic\ncomponent current.  Generic nonreduced multiplicities are retained, and\ndivisorial component intersections are allowed.  Its input is the\nordinary-local full-$\\operatorname{CPsh}$ analytic-nullity theorem, not a\nclassification of arbitrary positive closed currents.  Its linear companion\n\\Cref{cor:ch16-cpsh-component-diagonal-current} therefore covers every\nnonnegative component-diagonal current\n\\(\\sum_i c_i\\delta_{W_i}\\) on the same ordinary open.  Its smooth-factor\nextension \\Cref{cor:ch16-cpsh-smooth-component-current} also covers every\nfixed smooth positive closed decoration\n\\(\\bigl(\\sum_i c_i\\delta_{W_i}\\bigr)\\wedge\\gamma\\) in bidegree\n\\((q,q)\\), \\(0\\leq q\\leq n-1\\).  This remains a component-diagonal\ncurrent with a prescribed smooth factor: it neither treats a general\npositive closed current nor supplies a variable or singular\npositive-bidegree factor.  More generally,\n\\Cref{cor:ch16-cpsh-weak-component-current} covers the weak limits, with\n\\(q\\) fixed, of finite nonnegative sums of such smooth-component currents.\nThis is a stated weak-approximability condition, not a density theorem for\npositive closed currents.  Its local counterpart\n\\Cref{cor:ch16-cpsh-local-weak-component-current} permits the component\nfamilies and the approximating nets to vary over an ordinary open cover.  It\nis still a stated local weak-approximability condition; it does not claim\nthat an arbitrary positive closed current admits such a cover.\n\n\n\nThere is now also a higher-dimensional local positive result.  Suppose that\na good topologically separated pure boundaryless analytic space has a\ngenuine basis of ordinary open sets on which every continuous function with\nzero CLD Hessian is ordinary CLD-smooth with zero smooth Hessian.  Then\n\\cref{prop:p213-hessian-regular-basis-v2-candidate} shows that every positive\n\\(\\mathrm d'\\)- and \\(\\mathrm d''\\)-closed CLD current has\ncontinuous-pair Bedford--Taylor independence.  By\n\\cref{cor:p213-polycylinder-basis-v2-candidate}, the hypothesis holds when\nthe basis members are standard strict open polycylinders.  On one such\npolycylinder, \\cref{prop:p213-fixed-polycylinder-v2-candidate} gives the\nsame identity for pairs defined on the whole polycylinder, without claiming\nthe every-open predicate.\n\nThere is a further nonproduct basis range.  If every ordinary point\nneighbourhood belongs to a basis of boundaryless strict finite towers of\nlocally trivial standard open-polydisc bundles over a standard strict\nendpoint polycylinder, then\n\\cref{cor:p213-endpoint-tower-basis-bt} gives continuous-pair\nBedford--Taylor independence for every positive closed CLD current.  The\nendpoint-tower classification makes the equal-curvature difference an\nordinary CLD-smooth zero-Hessian function, so the proof uses the local smooth\npluriharmonic criterion rather than any pullback of the current.  It requires\nan actual ordinary-open basis of the displayed boundaryless towers and does\nnot cover a single chart in an otherwise arbitrary germ, annular fibres, or\nfibrations without the stated local product charts.\n\nThe endpoint base now also supports proper and mixed fibres.  In\n\\cref{thm:p213-endpoint-mixed-tower-classification}, each stage may be a\nlocally trivial standard strict open-polydisc bundle, a projective-space\nbundle, a smooth proper split-toric bundle, or---over an algebraically\nclosed field---a proper smooth connected curve bundle, in any finite order.\nEvery continuous zero-current function\non the entire top-level space is the pullback of a unique logarithmic-affine\nfunction on the endpoint polycylinder, hence is ordinary CLD-smooth with\nzero smooth Hessian.  The whole-space, cover, and basis consequences\n\\cref{cor:p213-endpoint-mixed-tower-bt,cor:p213-endpoint-mixed-tower-cover-bt,cor:p213-endpoint-mixed-tower-basis-bt}\ntherefore give Bedford--Taylor independence for arbitrary positive closed\nordinary CLD currents in the corresponding scopes.  The cover proof first\nglobalizes the smooth zero-Hessian difference and does not invoke current\nsheaf gluing outside its stated hypotheses.  Projective, split-toric, and\nproper-curve stages retain the exact local holomorphic-separation and\nparacompactness requirements of their descent theorems.\n\nThis narrows the higher-dimensional residual; it does not turn a\npolycylinder cover into a basis and does not settle arbitrary analytic\ngerms.\n\nThere is now a second, genuinely fibred basis range controlled by the\nresidual geometry of a curve rather than by an explicit polycylinder\nformula.  For a smooth proper curve over an algebraically closed complete\nnontrivially valued field,\n\\cref{prop:p213-residual-picard-smooth-curve} proves that a continuous\nzero-current function is ordinary CLD-smooth with zero smooth Hessian\nexactly when its type--\\(2\\) residual slope classes vanish in\n\\(\\operatorname{Pic}^0(C_x)\\otimes_{\\mathbf Z}\\mathbf R\\).  Thus vanishing\nof these groups at every type--\\(2\\) point removes the ordinary-smooth\nobstruction completely.  This includes the cases in which the residue field\nis algebraic over a finite field and in which the base is a Mumford curve.\n\nThe exact descent through locally trivial standard strict open-polydisc,\nprojective-space, smooth proper split-toric, and proper smooth connected\ncurve bundles may then be iterated in any finite order.  The resulting\ntheorem\n\\cref{thm:p213-residual-picard-mixed-tower} makes every continuous\nzero-current function on the whole top-level tower an ordinary CLD-smooth\npullback with zero smooth Hessian.  Hence\n\\cref{cor:p213-residual-picard-mixed-tower-bt} gives whole-space\ncontinuous-pair Bedford--Taylor independence against every positive closed\nCLD current; the cover and basis versions\n\\cref{cor:p213-residual-picard-mixed-tower-cover-bt,cor:p213-residual-picard-mixed-tower-basis-bt}\ngive the corresponding local and every-open conclusions.  Projective,\nsplit-toric, and proper-curve stages retain the locally holomorphically\nseparated and paracompact base hypotheses of their descent theorems, and no nonsmooth\ncurrent is pulled back.  A single mixed-tower chart inside an unrelated\nopen set is still insufficient, and no assertion is made beyond the\ndisplayed residual-Picard bases.\n\nThe residual-Picard range now also admits locally twisted annular geometry\nat the bottom.  In\n\\cref{thm:p213-residual-picard-open-polycylinder-mixed-tower}, the bottom\nspace is an analytically locally trivial bundle over the same curve domain\nwhose fibres are finite products of standard strict open annuli and,\noptionally, standard strict open discs; any finite mixed tower of the four\nexact bundle types may then be placed above it.  Every continuous\nzero-current function on the top is ordinary CLD-smooth with zero smooth\nHessian.  Indeed, on each bottom chart its annular part is a sum of a\nresidual-Picard-smooth curve function and locally constant multiples of the\nsmooth affine functions $\\log|T_i|$, while the disc factors and all later\nstages are handled by exact descent and pullback.  Consequently,\n\\cref{cor:p213-residual-picard-open-polycylinder-mixed-tower-bt,cor:p213-residual-picard-open-polycylinder-mixed-tower-cover-bt,cor:p213-residual-picard-open-polycylinder-mixed-tower-basis-bt}\ngive the whole-space, specified-cover, and every-open basis versions of\nBedford--Taylor independence against arbitrary positive closed ordinary CLD\ncurrents.  Neither integral annular monodromy nor the zero-current radiance\nclass is required to vanish, because ordinary smoothness is checked\nchartwise.  Accordingly, the theorem produces no global logarithmic\ncoefficient formula and still requires the displayed local product charts\nand the residual-Picard hypothesis.\n\nThe annular stages may now also occur at arbitrary levels among the four\nexact bundle types.  In\n\\cref{thm:p213-residual-picard-curve-local-interleaved-tower}, one analytic\nopen cover of the residual-Picard curve base makes every base-changed tower\na finite interleaving of globally coordinated standard strict\nopen-polyannulus products with standard strict open-polydisc,\nprojective-space, smooth proper split-toric, and proper smooth connected\ncurve bundles.  The annular radii, coordinates, and product trivializations\nmay vary with the member of the cover and need not agree on overlaps.  The\ninterleaved coefficient formula is therefore used only locally: its curve\ncoefficient is ordinary CLD-smooth by the residual-Picard criterion, while\nevery logarithmic annular term and all of its later pullbacks are ordinary\nCLD-smooth with zero smooth Hessian.  Hence every continuous zero-current\nfunction on the top is ordinary CLD-smooth with zero smooth Hessian.  The\nwhole-space, specified-cover, and every-open basis consequences are\n\\cref{cor:p213-residual-picard-curve-local-interleaved-tower-bt,cor:p213-residual-picard-curve-local-interleaved-tower-cover-bt,cor:p213-residual-picard-curve-local-interleaved-tower-basis-bt}.\nThis removes the restriction that all annular geometry occur at the bottom,\nbut gives no global logarithmic coefficient formula and retains both the\ncurve-local tower charts and the residual-Picard hypothesis.\n\nThe common-cover requirement can be replaced by a genuinely stage-local\ncondition.  \\Cref{prop:p062-stage-local-polyannulus-smooth-rigidity-transfer}\nshows that\nan analytically locally trivial finite strict open-polyannulus bundle\npreserves ordinary CLD-smooth zero-Hessian regularity and first-current\nrigidity whenever each member of its chosen trivializing cover already has\nthe corresponding zero-current regularity and rigidity.  Applying this at\nannular levels and the exact descent theorem at the other levels gives\n\\cref{thm:p213-residual-picard-stage-local-annular-tower}: annular charts may\nnow live over arbitrary intermediate bases and need not descend from one\ncover of the residual-Picard curve.  Its whole-space, specified-cover, and\nevery-open basis Bedford--Taylor consequences are\n\\cref{cor:p213-residual-picard-stage-local-annular-tower-bt,cor:p213-residual-picard-stage-local-annular-tower-cover-bt,cor:p213-residual-picard-stage-local-annular-tower-basis-bt}.\nNo compatibility of annular coordinates or global logarithmic coefficient\nformula is used.  The stage-local hypotheses cannot be recovered from the\ncorresponding whole-space conclusions in general.  Indeed,\n\\Cref{prop:p213-zero-current-smoothness-not-open-hereditary} constructs a\nsmooth proper surface $X=(\\mathbf P^1_K)^{\\mathrm{an}}\\times_KD^{\\mathrm{an}}$\non which every global continuous zero-current function is constant, while\nan ordinary product open $\\Omega\\subset X$ carries a continuous\nzero-current function which is not ordinary CLD-smooth.  The concrete\ngood-reduction elliptic instance is\n\\Cref{cor:p213-good-reduction-elliptic-open-nonheredity}.  Moreover,\n$X\\to(\\mathbf P^1_K)^{\\mathrm{an}}$ is itself the proper smooth curve-bundle\nstage allowed by the mixed exact-tower theorem.  Thus the failure occurs on\nan exact intermediate base, not merely on an unrelated space, and the\nstage-local chart assumptions are genuinely necessary for this route.\nThis strictly sharpens the boundary of the verified residual-geometric\nclass but neither proves nor disproves P21.3.\n\nThere is also a verified source-scoped split-toric subcase, including toric\nboundary strata.  On an open set of the form\n\\(V=\\operatorname{trop}^{-1}(O)\\) for extended tropicalization in a split\ntoric variety, the\nproposition\n\\(\\cref{prop:p213-invariant-split-toric-continuous-pairs-candidate}\\) gives\ncontinuous-pair Bedford--Taylor independence for every positive closed CLD\ncurrent when the difference of the finite continuous psh potentials is\ninvariant under the maximal compact torus.  The proof uses the\ninvariant-function correspondence and function-current pushforward\ncalculation of \\cite[(5.5) and Proposition~5.3.10(iv)]{BGJKK25}; finite\ncontinuity along the compactified normal rays forces the zero-Hessian\ndifference to be smooth at the boundary.  The exact stored two-individually\ninvariant-potential statement and proof passed the controlling local\nindependent verifier run with final verdict \\texttt{correct}, zero critical\nerrors, and zero gaps (item \\texttt{pi\\_96813b21562d920cf411c5a0}).  The\npresent difference-invariant strengthening is a direct book-level reuse of\nthat proof: its tropical factorization, pushforward, and boundary-ray steps\nuse only the difference.  More precisely, its multiplier identity requires\nonly a finite continuous pair with equal current Hessian and invariant\ndifference; the psh hypothesis is retained in the displayed consequence\nsolely because P21.3 asks about psh pairs.  This neither treats pairs with noninvariant\ndifference, nonsplit tori, arbitrary toroidal charts, nor general analytic\ngerms.  Scalar extension alone does not enlarge this P21.3 subcase:\nthe available base-change results identify only specified form/measure degrees\nin the CLD calculus, or the top-degree Monge--Amp\\`ere measures of continuous\nsemipositive line-bundle metrics on projective varieties\n\\cite[Propositions~15.3.1--15.3.2]{CLD25};\n\\cite[Proposition~8.4.2]{BGJKK25}.\nThey do not construct, or give faithful descent for, an arbitrary positive\nclosed CLD current and its mixed current\n\\(\\mathrm d'\\mathrm d''(uT)\\).  Thus the scalar-stable potential statements\nin P06.1/P06.2 do not by themselves yield an algebraic-split-form P21.3\ncorollary for an arbitrary positive closed current.  There is nevertheless\none paired scalar-stable class.  If the current is locally\nweak-form-approximable and the difference satisfies the analytic-local\nalgebraic-split equivariant tower hypotheses after the displayed scalar extension, then\n\\Cref{cor:p213-algebraic-split-scalar-stable-weak-form-bt} gives the\nBedford--Taylor equality.  The scalar-stable condition is used only to make\nthe downstairs difference weakly smooth and weakly harmonic; its constant\napproximation net and the weak-form closure bridge then control the ordinary\norder-zero product.  This neither supplies current ascent or descent nor\napplies to an arbitrary positive closed current or an arbitrary continuous\nzero-current difference.\nThere is, however, a genuine nonproduct extension at the original split\nlevel.  On every finite tower of equivariant locally trivial standard strict\nopen-polydisc bundles over such a split-toric base, the exact bundle descent\nmakes an invariant equal-curvature difference the pullback of an invariant\nzero-current base function.  The boundary-ray argument makes that base\nfunction ordinary CLD-smooth with zero Hessian, and CLD-form pullback\npreserves this property through the tower.  Therefore\n\\Cref{cor:p213-invariant-toric-open-polydisc-tower-bt} gives\ncontinuous-pair Bedford--Taylor independence for every positive closed CLD\ncurrent and every finite continuous psh pair whose difference is invariant\non a boundaryless top-level tower of dimension at least two.  It requires the\nactual split base, an action on every tower level, and equivariance of every\nbundle map; it neither treats pairs with noninvariant difference nor descends\narbitrary currents through an algebraic-splitting extension.\nThis conclusion is local in the spatial variable.  For one specified open\nset, an ordinary cover by such boundaryless split-toric equivariant towers,\nwith the difference invariant for the action on each member, already gives\nthe equality by\n\\Cref{cor:p213-invariant-toric-open-polydisc-tower-cover-bt}; no basis of the\nambient space is needed.  A basis of actual towers gives the corresponding\nconclusion simultaneously for every open set by\n\\Cref{cor:p213-invariant-toric-open-polydisc-tower-basis-bt}.  Neither\ncriterion turns unrelated local charts into a global toric action or a global\ninvariance condition.  The same cover-versus-basis distinction holds for the\nendpoint-tower criteria\n\\Cref{cor:p213-endpoint-tower-cover-bt,cor:p213-endpoint-tower-basis-bt}.\n\nThe additional supplied proof\n\\Cref{thm:supplied-p213-polycylinder-rigidity} establishes zero-Hessian\nrigidity and continuous-pair multiplication on full products of open disks\nand annuli over an algebraically closed nontrivially valued field. This\nis an established positive range of P21.3; arbitrary ordinary open domains\nand the remaining field and singularity scopes below stay open.\n\n\\begin{problem}\n\\label{prob:frontier-cross-fan-upstairs}\nLet \\(K\\) be a complete non-Archimedean field, let \\(n\\geq2\\), and let \\(X\\)\nbe a good separated strict boundaryless pure \\(n\\)-dimensional\n\\(K\\)-analytic space.  Determine whether every positive\n\\(\\mathrm d'\\)- and \\(\\mathrm d''\\)-closed CLD current \\(T\\) of bidegree\n\\((p,p)\\), \\(0\\leq p\\leq n-1\\), has the following property: for every open\n\\(W\\subseteq X\\) and all continuous psh functions \\(U,V\\) on \\(W\\),\n\\begin{equation}\n                  \\mathrm d'\\mathrm d''[U]\n                  =\\mathrm d'\\mathrm d''[V]\n \\label{eq:p21p3-post-nonreduced-residual-equal-curvature}\n\\end{equation}\nimplies\n\\begin{equation}\n \\mathrm d'\\mathrm d''\\bigl(U\\,T|_W\\bigr)\n =\\mathrm d'\\mathrm d''\\bigl(V\\,T|_W\\bigr).\n \\label{eq:p21p3-post-nonreduced-residual-bt}\n\\end{equation}\nIf this fails, construct a counterexample.  A counterexample could provide an\nanalytic weighted-gluing defect before tropical pushforward.\n\\end{problem}\n\nNo one-dimensional case remains inside the displayed ambient hypotheses.\nIndeed, \\cref{prop:p213-componentwise-arbitrary-valuation} treats either\nvaluation, arbitrary reducibility and nilpotent structure, and normalizations\nwith no smoothness assumption.  Non-good, non-separated, non-strict, and\nboundary cases lie outside the displayed problem rather than forming hidden\nresidual atoms.  Within dimension at least two, spaces with the strict-open\npolycylinder basis of\n\\cref{cor:p213-polycylinder-basis-v2-candidate} are also removed from the\nresidual scope, as are fixed-domain pairs on one standard strict open\npolycylinder.  The invariant split-toric family, including its toric boundary\nstrata, of\n\\cref{prop:p213-invariant-split-toric-continuous-pairs-candidate} is likewise\nremoved.  The atom remains open for general spaces in the displayed ambient\nclass.\n\n\nThe problem uses the book's continuous-potential convention.  Literal\n\\cite[Definition~8.6.2]{CLD25} quantifies over the full CLD psh class, which\nmay include discontinuous functions.  The normal-curve theorem establishes\nthat stronger statement, while the reducible and nonreduced componentwise\ntheorem establishes the continuous-pair predicate used here.  The remaining\ndiscontinuous-potential question in the latter setting is neither asserted to\nbe equivalent to the displayed problem nor separately counted here.  Thus\nP21.3 remains one genuinely open residual T2 atom, now only in analytic\ndimension at least two and outside the verified basis, fixed-domain, and\ninvariant split-toric regimes above.  The book-wide inventory remains\n12 open problem environments and 42 active atomic questions, with\ntier totals $0/3/7/15/17$ for T1 through T5.\n\nThe four-punctured smooth-curve obstruction remains useful as a warning about\nthe method.  Its coarse tropical weights \\((2,2,1,1)\\) violate refined\nbalancing after a third analytic unit is appended, so a coarse tropical\npushforward cannot replace analytic classification.  The well-defined\nresidual atom is precisely the continuous-pair CLD question in the ranges\nnot covered by\n\\cref{prop:p213-componentwise-arbitrary-valuation,%\ncor:p213-polycylinder-basis-v2-candidate,%\nprop:p213-fixed-polycylinder-v2-candidate,%\nprop:p213-invariant-split-toric-continuous-pairs-candidate}.  Equality only after a\nnoninjective tropical pushforward does not decide it.\n\nThere is an exact sufficient route for the remaining analytic question.  Put\n\\(h=U-V\\).  If, locally on \\(W\\), the continuous zero-Hessian function\n\\(h\\) is a locally uniform limit of smooth functions \\(h_j\\) satisfying\n\\(\\mathrm d'\\mathrm d''h_j=0\\), then\n\\Cref{cor:ch16-local-pluriharmonic-criterion} gives\n\\(\\mathrm d'\\mathrm d''(hT)=0\\), hence the required equality for every\npositive closed \\(T\\).  Thus the unresolved continuous-pair problem is\nconcentrated at higher-dimensional gluing loci where the displayed smooth\npluriharmonic approximation is not known.  Merely knowing\n\\(\\mathrm d'\\mathrm d''[h]=0\\) does not supply the approximants\n(\\Cref{cor:ch16-local-pluriharmonic-criterion}); the abstract cross-fan shows why\ncellwise affine data alone cannot replace them.  Nor do the bare real-PL or\nGJR-harmonic conclusions occurring in P06.1/P06.2: that G-local,\nweakly smooth regularity does not provide ordinary CLD-smooth zero-Hessian\napproximants.  Indeed,\n\\Cref{prop:ch19-cld-smooth-harmonic-nonregularization} gives an integral PL\nweakly smooth harmonic function on a curve with no locally uniform ordinary\nCLD-smooth harmonic approximation.  This obstructs this approximation route,\nnot the separately proved one-dimensional P21.3 classification.  This bridge\nis related to, but is not identified with, P06.2.\nAt the level of strong currents there is nevertheless a formal compatibility:\n\\Cref{prop:ch18-strong-harmonic-compatibility} gives\n\\(\\mathrm d'\\mathrm d''(h\\wedge S)=0\\) for a weakly smooth zero-Hessian\n$h$ and a closed strong current $S$.  This is deliberately not used to\nsettle P21.3.  The latter uses the order-zero ordinary product $hT$; even\nwhen an ordinary current $T$ has a strong lift, its equality with the\nrestriction of $h\\wedge S$ requires a separate compatibility argument, as\nspelled out in \\Cref{warn:ch18-strong-not-ordinary-bt}.\nThere is now one genuine ordinary-current bridge inside this distinction.\nIf $T$ is locally weak-form-induced in the sense of\n\\Cref{def:ch18-weak-form-induced-current}, and the difference $h=U-V$ is a\nweakly smooth zero-Hessian function, then\n\\Cref{prop:ch18-weak-form-induced-bt} proves the required equality.  Its\nproof identifies the order-zero product $hT$ with the restriction of the\nstrong product by uniform ordinary-smooth approximation on compact supports\nand the $C^0$ continuity of weakly smooth integration.  It covers neither an\narbitrary strong lift nor an arbitrary positive closed current, and it still\nassumes weak smoothness of $h$; it is therefore a current-and-pair subcase,\nnot a resolution of the remaining gluing problem.\nThe bridge now persists through two natural but explicitly conditional\nclosures.  If the ordinary current is locally a weak limit of positive closed\nlocally weak-form-induced currents, and $h$ is locally a uniform limit of\nweakly smooth zero-Hessian functions, then\n\\Cref{prop:ch18-weak-form-closure-bt} gives the same ordinary-current\nequality.  The proof first passes the form-induced identity along the current\nnet and then along the function net, using the order-zero\nmultiplication-continuity lemma at each step.  It is not a density theorem\nfor arbitrary positive closed CLD currents or arbitrary continuous\nzero-Hessian differences, so it narrows a paired closure class without\nremoving the unresolved higher-dimensional gluing step.\nThe exact P06.2\nproper-full-rank moment classification supplies this bridge for a genuine\npairwise subcase: if $h$ has such a factorization locally, then\n\\Cref{cor:ch18-local-proper-full-rank-moment-bt} gives the required equality\nfor every positive closed current.  P06.2 supplies no such local\nfactorization for an arbitrary $h$, however, so this new exclusion is a\ncondition on a pair of potentials rather than a resolution of the\nhigher-dimensional gluing problem.\n\n\n\nCATALOGUE BIBLIOGRAPHY\n\nReferences\n[BGGJK25] José Ignacio Burgos Gil, Walter Gubler, Philipp Jell, and Klaus Künnemann.\n         Pluripotential theory for tropical toric varieties and non-Archimedean Monge–\n         Ampère equations. Kyoto J. Math., 65(1):55–152, 2025.\n\n[Bin76]   Jürgen Bingener. Schemata über Steinschen Algebren. Schr. Math. Inst. Univ.\n          Münster (2), page 52, 1976.\n\n[BJ23]    Sébastien Boucksom and Mattias Jonsson. A non-Archimedean approach to K-\n          stability, II: Divisorial stability and openness. J. Reine Angew. Math., 805:1–53,\n          2023.\n\n[BJ24b]   Sébastien Boucksom and Mattias Jonsson. Non-Archimedean Green’s functions\n          and Zariski decompositions. Comptes Rendus Mathématique, 362(S1):5–42, 2024.\n\n[BJ25c]   Sébastien Boucksom and Mattias Jonsson. On the Yau–Tian–Donaldson conjec-\n          ture for weighted cscK metrics, 2025. Version 1, 18 September 2025.\n\n[BJ26]    Sébastien Boucksom and Mattias Jonsson. From complex to non-Archimedean\n          geometry: an approach to the YTD conjecture, 2026. Version 2, 19 May 2026.\n\n[BMPS26] Ana María Botero, Enrica Mazzon, and Léonard Pille-Schneider. Monge–Ampère\n         measures on balanced polyhedral spaces, 2026. Manuscript dated 10 March 2026.\n\n[CLD25]   Antoine Chambert-Loir and Antoine Ducros. Formes diﬀérentielles réelles et\n          courants sur les espaces de Berkovich, 2025. Version 2, 25 July 2025.\n\n[DRWN+ 26] Tamás Darvas, Rémi Reboulet, David Witt Nyström, Mingchen Xia, and Kewei\n         Zhang. Transcendental Okounkov bodies. J. Diﬀerential Geom., 132(1):135–178,\n         2026.\n\n[DXZ25]   Tamás Darvas, Mingchen Xia, and Kewei Zhang. A transcendental approach\n          to non-Archimedean metrics of pseudoeﬀective classes. Comment. Math. Helv.,\n          100(2):269–322, 2025.\n\n[DZ25]    Tamás Darvas and Kewei Zhang. A YTD correspondence for constant scalar\n          curvature metrics, 2025. Version 2, 3 November 2025.\n\n[Fan25]   Yanbo Fang. Metrized ample line bundles in non-Archimedean geometry II, 2025.\n          Version 1, 26 November 2025.\n\n[Fin26]   Siarhei Finski. Kodaira–Iitaka dimension and multiplicity: an analytic perspec-\n          tive, 2026. Version 1, 23 March 2026.\n\n[GJKM19] Walter Gubler, Philipp Jell, Klaus Künnemann, and Florent Martin. Continu-\n         ity of plurisubharmonic envelopes in non-Archimedean geometry and test ideals.\n         Ann. Inst. Fourier (Grenoble), 69(5):2331–2376, 2019. With an appendix by José\n         Ignacio Burgos Gil and Martín Sombra.\n\n[GJR26]   Walter Gubler, Philipp Jell, and Joseph Rabinoﬀ. Forms on Berkovich spaces\n          based on harmonic tropicalizations. Bull. Soc. Math. France, 154(1):135–238,\n          2026.\n\n[GR25a]   Walter Gubler and Joseph Rabinoﬀ. Classically psh and pluriharmonic functions\n          on Berkovich spaces, 2025. Version 2, 17 September 2025.\n\n\n                                           85\n\n[MPWN25] Pietro Mesquita-Piccione and David Witt Nyström. A transcendental non-\n        Archimedean Calabi–Yau theorem with applications to the cscK problem, 2025.\n        Version 1, 11 September 2025.\n\n[PS23]      Léonard Pille-Schneider. Global pluripotential theory on hybrid spaces. J. Éc.\n            polytech. Math., 10:601–658, 2023.\n\n[PSWZ26] Kai Pang, Haoyuan Sun, Zhiwei Wang, and Xiangyu Zhou. Capacity stability\n         of complex Monge–Ampère equations with moving prescribed singularities, 2026.\n         Version 1, 14 July 2026.\n\n[Stacksb]   The Stacks Project Authors. Stacks project. https://stacks.math.columbia.e\n            du, 2026. Accessed 29 August 2026.\n\n[Sup26b]    Withdrawn draft: Orthogonality on one-dimensional balanced fans, 2026. Author-\n            supplied withdrawn manuscript dated and received 25 September 2026; replace-\n            ment withdrawal version preserved in the book repository.\n\n[Tru26]     Antonio Trusiani. A solution to the Yau–Tian–Donaldson conjecture through\n            special Fujita approximations, 2026. Version 2, 17 August 2026; includes an\n            appendix by Sébastien Boucksom.\n\n[Vil21]     Christian Vilsmeier. A comparison of the real and non-archimedean Monge-\n            Ampère operator. Math. Z., 297(1-2):633–668, 2021.\n\n[Wan19]     Veronika Wanner. Comparison of two notions of subharmonicity on non-\n            archimedean curves. Math. Z., 293:443–474, 2019.\n\n[Wan25]     Ying Wang. Non-Archimedean Calabi–Yau potentials on certain aﬃne varieties,\n            2025. Version 1, 24 October 2025.\n\n[Wu24]      Yueqiao Wu. Some non-Archimedean pluripotential theory on polarized aﬃne\n            cones, 2024. Version 1, 19 June 2024.\n\n[Xia25a]    Mingchen Xia. Operations on transcendental non-Archimedean metrics. In Con-\n            vex and complex: perspectives on positivity in geometry, volume 810 of Contemp.\n            Math., pages 271–293. Amer. Math. Soc., Providence, RI, 2025.\n\n[Xia25b]    Mingchen Xia. Partial Okounkov bodies and Duistermaat-Heckman measures of\n            non-Archimedean metrics. Geom. Topol., 29(3):1283–1344, 2025.\n\n[Xia26a]    Mingchen Xia. Mixed volumes of Okounkov bodies. Work in progress, July 2026;\n            available at https://mingchenxia.github.io/Papers/MVOB.pdf. The author-\n            supplied source was repaired and independently audited on 24 August 2026. The\n            full repaired proof is reproduced in this book; its production Rethlas proof digest\n            is 9227826d...58cad7b, with ﬁnal verdict correct and no reported gap, 2026.\n\n[Zha14]     Yuchen Zhang. On the volume of isolated singularities. Compositio Mathematica,\n            150(8):1413–1424, 2014.\n\n\n\n\n                                              86\n\n\n\nATOMIC TARGETS AND FAMILY COMPLETION CRITERIA FROM THE ATTACHED CATALOGUE\nP21.3 (T2): Bedford–Taylor independence for continuous equal-curvature pairs\nFor a complete non-Archimedean ﬁeld and a good separated strict boundaryless pure n-\ndimensional analytic space, n ≥ 2, decide whether every positive d0 - and d00 -closed CLD\n(p, p)-current, 0 ≤ p ≤ n − 1, has Bedford–Taylor independence on every ordinary open for\ncontinuous psh pairs with equal Hessian currents. The full quantiﬁed equations appear below.\nA negative answer must give an analytic counterexample in this scope, not just a defective\nabstract tropical pushforward.\n\nProve the quantiﬁed every-open, every-current continuous-pair assertion, or supply an analytic\ncounterexample with all ambient hypotheses. A ﬁxed polycylinder, a cover of one speciﬁed\nopen and a genuine ordinary-open basis give diﬀerent conclusions. Weak approximability is a\nsuﬃcient condition, not a density theorem for arbitrary currents.",
  "completionCriteria": "For each target claimed solved, give a rigorous complete proof or an analytic counterexample satisfying every ambient hypothesis, and explicitly compare the result to the residual scope in the catalogue. Do not count an already known case, an extra conditional hypothesis, an abstract tropical obstruction, or a narrower theorem as a full solution. Separate partial progress and unresolved claims. Every essential external theorem must be stated exactly, cited, and checked for applicability; source-dependent claims from the catalogue are not independently established merely by its description. A rigorous new special case may be reported with its exact scope and a statement that the full atom remains open."
}

END MATHEMATICAL DATA


BEGIN MATHEMATICAL DATA: All nine precise external primary premises and literal bindings
[
  {
    "id": "P0",
    "exact_statement_and_applicability": "**P0: analytic and ordinary-local scope.** Analytic spaces have compact-neighbourhood bases; good analytic spaces have affinoid-neighbourhood bases; ordinary opens are analytic domains [11.1.7]. A topologically separated pure $n$-dimensional analytic space has its canonical calibrated level-$n$ tropical structure, compatible with analytic-domain restriction [15.7.1–2]. A good Hausdorff analytic space is locally holomorphically separated and hence locally differentially separated [15.2.2–4]. On such a space compact supports admit smooth cutoffs, finite nonnegative smooth localization, and uniform approximation of compact continuous scalars by compact smooth scalars [15.2.5–9]. Global paracompactness is not required for these compact-support assertions. The hypotheses apply to each original ordinary open, in either valuation regime. Boundarylessness is retained when invoking Stokes.",
    "source_version": "CLD arXiv:1204.6277v2, 25 July 2025",
    "primary_url": "https://arxiv.org/pdf/1204.6277v2",
    "evidence": [
      {
        "id": "ordinary-domain",
        "path": "sources/cld-ordinary-domain.txt",
        "url": "https://arxiv.org/pdf/1204.6277v2",
        "version": "25 July 2025",
        "inclusive_one_based_LF": [
          14983,
          15012
        ],
        "sha256": "6efe2fa15d3425138409717a7512d91909e0b03be4f3c3e56e267d4bcdfefabd",
        "source_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085"
      },
      {
        "id": "analytic-calculus",
        "path": "sources/cld-analytic-calculus.txt",
        "url": "https://arxiv.org/pdf/1204.6277v2",
        "version": "25 July 2025",
        "inclusive_one_based_LF": [
          22105,
          22126
        ],
        "sha256": "960861bd1391008caa52be28ee8a788b6bdc3df269d765f603121a8bab0af320",
        "source_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085"
      },
      {
        "id": "cutoffs-density",
        "path": "sources/cld-cutoffs-density.txt",
        "url": "https://arxiv.org/pdf/1204.6277v2",
        "version": "25 July 2025",
        "inclusive_one_based_LF": [
          21619,
          21696
        ],
        "sha256": "aba28489aa7c1e770af13b87e11c77fbca731f95eb5bc41afb637b378d66ed45",
        "source_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085"
      }
    ]
  },
  {
    "id": "P1",
    "exact_statement_and_applicability": "**P1: generated functions.** Definition 8.1.1 defines Psh as the smallest ordinary subsheaf of functions valued in $\\mathbb R\\cup\\{-\\infty\\}$ containing smooth functions of positive smooth Hessian and closed under decreasing sequential limits. Lemma 8.1.4 describes the sheafified ordinal construction. We reconstruct stabilization, upper semicontinuity, and the bounded-final-function steps rather than relying on the printed proof's extraneous integrability qualification. Definition 8.1.7 instead generates CPsh inside continuous functions by uniform sequential closure. The printed reverse recognition in 8.1.11 is not used.",
    "source_version": "CLD arXiv:1204.6277v2, 25 July 2025",
    "primary_url": "https://arxiv.org/pdf/1204.6277v2",
    "evidence": [
      {
        "id": "generated-psh",
        "path": "sources/cld-generated-psh.txt",
        "url": "https://arxiv.org/pdf/1204.6277v2",
        "version": "25 July 2025",
        "inclusive_one_based_LF": [
          9729,
          9781
        ],
        "sha256": "fa2e29bcb98fd26a55598c0dc4c67b162d19d4b1780b39f2a49bdfc7e4373830",
        "source_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085"
      },
      {
        "id": "generated-cpsh-diagnostic",
        "path": "sources/cld-generated-cpsh-diagnostic.txt",
        "url": "https://arxiv.org/pdf/1204.6277v2",
        "version": "25 July 2025",
        "inclusive_one_based_LF": [
          9797,
          9863
        ],
        "sha256": "5ef01dd5ed01e2349c223afadbb34c535cb304dce255f10115f25edccd4899da",
        "source_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085"
      }
    ]
  },
  {
    "id": "P2",
    "exact_statement_and_applicability": "**P2: middle positivity.** Every compact symmetric smooth $(q,q)$ test is a difference of two compact middle-positive tests, provided its support is contained in a paracompact locally differentially separated open [6.5.2]. The statement explicitly includes compact supports on almost-good analytic spaces; good suffices here. Middle-positive currents are symmetric and nonnegative on middle-positive complementary tests; positivity is ordinary-local [7.2.1–4]. Positive smooth factors preserve middle-positive currents [7.2.7(b)], since wedges of middle-positive forms are middle-positive [1.2.12, 1.10.3, 3.5.5]. This is not a replacement by strongly positive tests. A current and its negative cannot both be middle-positive unless the current is zero [7.2.3; also proved below using the decomposition].",
    "source_version": "CLD arXiv:1204.6277v2, 25 July 2025",
    "primary_url": "https://arxiv.org/pdf/1204.6277v2",
    "evidence": [
      {
        "id": "positive-decomposition",
        "path": "sources/cld-positive-decomposition.txt",
        "url": "https://arxiv.org/pdf/1204.6277v2",
        "version": "25 July 2025",
        "inclusive_one_based_LF": [
          7359,
          7381
        ],
        "sha256": "7d7b6d6687db0b922b6e69a1011a9dcb0a2d112c41d65200901f1efd7275db83",
        "source_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085"
      },
      {
        "id": "middle-positivity",
        "path": "sources/cld-middle-positivity.txt",
        "url": "https://arxiv.org/pdf/1204.6277v2",
        "version": "25 July 2025",
        "inclusive_one_based_LF": [
          7918,
          7981
        ],
        "sha256": "7e8a9c9f610a102901ed491e3e572f9b96528cf24e5f8733f1d4f3d419801332",
        "source_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085"
      },
      {
        "id": "positive-wedges",
        "path": "sources/cld-positive-wedges.txt",
        "url": "https://arxiv.org/pdf/1204.6277v2",
        "version": "25 July 2025",
        "inclusive_one_based_LF": [
          1026,
          1040
        ],
        "sha256": "568f9d32c940d6a28332eff16ffcf4a0fb4a1ac468e9645dab1f2e1948c7ca85",
        "source_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085"
      },
      {
        "id": "face-positive-wedges",
        "path": "sources/cld-face-positive-wedges.txt",
        "url": "https://arxiv.org/pdf/1204.6277v2",
        "version": "25 July 2025",
        "inclusive_one_based_LF": [
          2685,
          2699
        ],
        "sha256": "755005874cbbd0719c56e04d0023943714d304b960d55d46188c1267bd2c9571",
        "source_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085"
      },
      {
        "id": "geometric-positive-wedges",
        "path": "sources/cld-geometric-positive-wedges.txt",
        "url": "https://arxiv.org/pdf/1204.6277v2",
        "version": "25 July 2025",
        "inclusive_one_based_LF": [
          4074,
          4081
        ],
        "sha256": "af2ae2b53d2b5093ec220554a5e109e67790222e7b7ce1255d4d6b93d0107534",
        "source_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085"
      }
    ]
  },
  {
    "id": "P3",
    "exact_statement_and_applicability": "**P3: coefficient measures.** On a locally differentially separated level-$n$ space, positive scalar currents correspond to unique positive Radon measures [7.2.8]. For middle-positive $T$ and a positive complementary smooth form $\\eta$, the associated coefficient measure satisfies\n$$\\int g\\,d\\mu_{T,\\eta}=\\langle T,g\\eta\\rangle$$\nfor compact smooth scalars $g$, and has compact support when $\\eta$ does [7.2.11]. Borel multiplication is stated in 7.2.12. Its order-zero justification for the middle cone is reconstructed below; the strongly-positive spanning inference in the broader wording of 7.2.9 is not imported.",
    "source_version": "CLD arXiv:1204.6277v2, 25 July 2025",
    "primary_url": "https://arxiv.org/pdf/1204.6277v2",
    "evidence": [
      {
        "id": "positive-scalar-measures",
        "path": "sources/cld-positive-scalar-measures.txt",
        "url": "https://arxiv.org/pdf/1204.6277v2",
        "version": "25 July 2025",
        "inclusive_one_based_LF": [
          7983,
          8011
        ],
        "sha256": "089af75e6237f117a1ff411156580da33c01951d926d14ecc613c1bf86f77060",
        "source_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085"
      },
      {
        "id": "ordinary-product",
        "path": "sources/cld-ordinary-product.txt",
        "url": "https://arxiv.org/pdf/1204.6277v2",
        "version": "25 July 2025",
        "inclusive_one_based_LF": [
          8054,
          8076
        ],
        "sha256": "f647601926c2311a3319b181f2567f487f9a88ce4870332c75ecc8bb5f3156d4",
        "source_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085"
      }
    ]
  },
  {
    "id": "P4",
    "exact_statement_and_applicability": "**P4: chart topology and finite-dimensional domination.** In Euclidean coordinates the middle cone of symmetric $(q,q)$ superforms is the positive-semidefinite signed coefficient matrix cone on the $q$th exterior power [1.2.6–7]; positivity on polyhedral spaces is tested on tangent faces [1.10.1]. Compact moment images are finite polyhedral sets [12.2.4]. We use only polyhedrality, not its printed claim that every moment image has dimension equal to that of the source: a constant moment already disproves that clause. Test topology is the inductive topology for fixed compact supports and fixed moment presentations, with cellwise coefficient seminorms [7.1.1–3]. Compact smooth localization reduces continuity to such a chart. Compact analytic neighbourhoods can be finite unions of affinoids, so no assertion that one arbitrary compact support lies in a single affinoid is needed.",
    "source_version": "CLD arXiv:1204.6277v2, 25 July 2025",
    "primary_url": "https://arxiv.org/pdf/1204.6277v2",
    "evidence": [
      {
        "id": "middle-matrix",
        "path": "sources/cld-middle-matrix.txt",
        "url": "https://arxiv.org/pdf/1204.6277v2",
        "version": "25 July 2025",
        "inclusive_one_based_LF": [
          885,
          975
        ],
        "sha256": "7ac6fc20a19b2e92f75e58b56564ddba33b24b1dd86814f5a3068e7978c50da1",
        "source_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085"
      },
      {
        "id": "face-positivity",
        "path": "sources/cld-face-positivity.txt",
        "url": "https://arxiv.org/pdf/1204.6277v2",
        "version": "25 July 2025",
        "inclusive_one_based_LF": [
          2634,
          2651
        ],
        "sha256": "3aaef6a90762b10edb0574cb40377ab1f036d24da0e2db4d0552ece7f5e7f481",
        "source_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085"
      },
      {
        "id": "current-topology",
        "path": "sources/cld-current-topology.txt",
        "url": "https://arxiv.org/pdf/1204.6277v2",
        "version": "25 July 2025",
        "inclusive_one_based_LF": [
          7654,
          7736
        ],
        "sha256": "a2b017a29233edf025a43ad188ab9833bce6acb54ef9d924c5e32cc4f7e92a25",
        "source_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085"
      },
      {
        "id": "compact-moment-image",
        "path": "sources/cld-compact-moment-image.txt",
        "url": "https://arxiv.org/pdf/1204.6277v2",
        "version": "25 July 2025",
        "inclusive_one_based_LF": [
          16836,
          16840
        ],
        "sha256": "d4d28c1f1c639600b5d079cd31ebe2411e60f94e19dd8c40b1544e9ef40e4125",
        "source_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085"
      },
      {
        "id": "chart-images",
        "path": "sources/cld-chart-images.txt",
        "url": "https://arxiv.org/pdf/1204.6277v2",
        "version": "25 July 2025",
        "inclusive_one_based_LF": [
          3685,
          3701
        ],
        "sha256": "27ede4644fa7140bd001a864d8f0804469ceb8bd833aa7af77d322c5105da01c",
        "source_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085"
      }
    ]
  },
  {
    "id": "P5",
    "exact_statement_and_applicability": "**P5: ordinary differential calculus.** Forms have compatible restriction, products, pullback and Leibniz rules [3.3.10–12]. Ordinary currents form a sheaf [7.1.6–7]. Their differentials are continuous for weak convergence and satisfy\n$$ (\\mathrm d')^2=(\\mathrm d'')^2=0,\\quad\n\\mathrm d''\\mathrm d'=-\\mathrm d'\\mathrm d'',\\quad DJ=JD,\\quad\n\\langle DR,\\alpha\\rangle=\\langle R,D\\alpha\\rangle                 \\tag{2}\n$$\n[7.7.1–5]. For smooth $s$ and symmetric doubly closed $T$, $D(sT)=Ds\\wedge T$ [8.5.3–4]. This assertion is used with actual compatible degrees, independently of the printed bidegree/bidimension indexing in 8.5.3. Multiplication by a smooth doubly closed even-degree form commutes with the differentials, by the same Leibniz rule in duality. Both closedness equations are checked.",
    "source_version": "CLD arXiv:1204.6277v2, 25 July 2025",
    "primary_url": "https://arxiv.org/pdf/1204.6277v2",
    "evidence": [
      {
        "id": "form-leibniz",
        "path": "sources/cld-form-leibniz.txt",
        "url": "https://arxiv.org/pdf/1204.6277v2",
        "version": "25 July 2025",
        "inclusive_one_based_LF": [
          3769,
          3803
        ],
        "sha256": "172d214bed8f4a1ffbfd19dcf120345ce08abbc69c0b70160a6af23832c8eff0",
        "source_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085"
      },
      {
        "id": "current-sheaf",
        "path": "sources/cld-current-sheaf.txt",
        "url": "https://arxiv.org/pdf/1204.6277v2",
        "version": "25 July 2025",
        "inclusive_one_based_LF": [
          7756,
          7818
        ],
        "sha256": "0d1a24130ba9c326713dcafecb5aa9a83678fb264cbd51fe4d1005de11869d48",
        "source_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085"
      },
      {
        "id": "current-differentials",
        "path": "sources/cld-current-differentials.txt",
        "url": "https://arxiv.org/pdf/1204.6277v2",
        "version": "25 July 2025",
        "inclusive_one_based_LF": [
          9309,
          9381
        ],
        "sha256": "a396b6b027f3375f6aa7b3e89bac0319a21ad2c96f44971acb018cec52648801",
        "source_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085"
      },
      {
        "id": "smooth-multiplier",
        "path": "sources/cld-smooth-multiplier.txt",
        "url": "https://arxiv.org/pdf/1204.6277v2",
        "version": "25 July 2025",
        "inclusive_one_based_LF": [
          10283,
          10326
        ],
        "sha256": "364ca08767840b4b45382d42e9e0a5b18b7f7c1b2daf978615413b9a1b5cc985",
        "source_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085"
      }
    ]
  },
  {
    "id": "P6",
    "exact_statement_and_applicability": "**P6: canonical integration.** $\\delta_X=[1]$ is positive and doubly closed on the original boundaryless space [15.7.1, 7.7.4; positivity of the canonical calibration is used in 5.8.1–5]. For a pure closed analytic subspace the integration current equals its associated analytic cycle current, with actual generic lengths [16.6.3]. No nilreduction is substituted in our construction.",
    "source_version": "CLD arXiv:1204.6277v2, 25 July 2025",
    "primary_url": "https://arxiv.org/pdf/1204.6277v2",
    "evidence": [
      {
        "id": "analytic-calculus",
        "path": "sources/cld-analytic-calculus.txt",
        "url": "https://arxiv.org/pdf/1204.6277v2",
        "version": "25 July 2025",
        "inclusive_one_based_LF": [
          22105,
          22126
        ],
        "sha256": "960861bd1391008caa52be28ee8a788b6bdc3df269d765f603121a8bab0af320",
        "source_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085"
      },
      {
        "id": "current-differentials",
        "path": "sources/cld-current-differentials.txt",
        "url": "https://arxiv.org/pdf/1204.6277v2",
        "version": "25 July 2025",
        "inclusive_one_based_LF": [
          9309,
          9381
        ],
        "sha256": "a396b6b027f3375f6aa7b3e89bac0319a21ad2c96f44971acb018cec52648801",
        "source_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085"
      },
      {
        "id": "generic-lengths",
        "path": "sources/cld-generic-lengths.txt",
        "url": "https://arxiv.org/pdf/1204.6277v2",
        "version": "25 July 2025",
        "inclusive_one_based_LF": [
          23434,
          23459
        ],
        "sha256": "52dbd2e0b2cf6d2c6220cb31fdf4683247d2c282b0b8055f6a2bf8735129d742",
        "source_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085"
      },
      {
        "id": "top-measures",
        "path": "sources/cld-top-measures.txt",
        "url": "https://arxiv.org/pdf/1204.6277v2",
        "version": "25 July 2025",
        "inclusive_one_based_LF": [
          6733,
          6808
        ],
        "sha256": "c727f9481e602256f7ccc91d7e23516abbf75077de67409d2e46c9956100005f",
        "source_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085"
      }
    ]
  },
  {
    "id": "P7",
    "exact_statement_and_applicability": "**P7: weak multiplication, reconstructed.** Lemma 8.5.1 states: if positive currents $T_j\\to T$ weakly and continuous functions $u_j\\to u$ locally uniformly, then $u_jT_j\\to uT$. Its full statement and proof were read. We give the middle-cone proof, including the fixed-function net variant, in Lemma 2. We do not apply it to a discontinuous multiplier.",
    "source_version": "CLD arXiv:1204.6277v2, 25 July 2025",
    "primary_url": "https://arxiv.org/pdf/1204.6277v2",
    "evidence": [
      {
        "id": "weak-multiplier",
        "path": "sources/cld-weak-multiplier.txt",
        "url": "https://arxiv.org/pdf/1204.6277v2",
        "version": "25 July 2025",
        "inclusive_one_based_LF": [
          10257,
          10281
        ],
        "sha256": "0eec1c45dfec34af7fb8e231160cc24fd3ef9b8f6dc1185fb8eedd1905483114",
        "source_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085"
      }
    ]
  },
  {
    "id": "P8",
    "exact_statement_and_applicability": "**P8: torus coordinates, diagnostic only.** [12.1.1–5] describes the analytic split torus, its Laurent characters, and their functorial tropicalizations. In the diagnostic we fix $K=\\mathbb Q_2$ and $X=(\\mathbf G_{m,K}^2)^{\\mathrm{an}}$, a good separated strict smooth boundaryless surface. The explicitly displayed Laurent monomial changes are analytic automorphisms. Their effect on logarithmic coordinates follows directly by multiplicativity. No theorem about arbitrary current ascent, descent, classification, or density is imported.",
    "source_version": "CLD arXiv:1204.6277v2, 25 July 2025",
    "primary_url": "https://arxiv.org/pdf/1204.6277v2",
    "evidence": [
      {
        "id": "torus-coordinates",
        "path": "sources/cld-torus-coordinates.txt",
        "url": "https://arxiv.org/pdf/1204.6277v2",
        "version": "25 July 2025",
        "inclusive_one_based_LF": [
          16493,
          16575
        ],
        "sha256": "f45158e6456b76c10f89688528b986df3a51a16988d2d6d6ce157bbf925e4667",
        "source_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085"
      }
    ]
  }
]

END MATHEMATICAL DATA


BEGIN MATHEMATICAL DATA: All27 literal pertinent CLD primary statement and proof units
# Literal selected primary evidence

Primary version: CLD arXiv:1204.6277v2, 25 July 2025. The frozen full text SHA256 is `64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085`.

The full primary was copied, not read in full. LF coordinates are one-based, inclusive, using UTF8 decoding followed by split("\n"). Each unit is a literal source slice with one trailing newline. The extracted text contains PDF line-wrap and typography artifacts. Hashes identify bytes and are not mathematical acceptance.

The explicitly bound raw weak-multiplier unit is preserved separately in `sources/cld-weak-multiplier-bound.txt`, SHA256 `0448ea1b480496814c9d81b4a5443f7d6efbb05b91582305b117704008184860`. It equals the selected LF text without the one added trailing newline.

## ordinary-domain

Primary: <https://arxiv.org/pdf/1204.6277v2>. LF 14983–15012; unit SHA256 `6efe2fa15d3425138409717a7512d91909e0b03be4f3c3e56e267d4bcdfefabd`.

```text
11.1.7. — À partir des espaces affinoïdes, Berkovich définit dans [9] la catégorie des
espaces k-analytiques par un procédé de recollement un peu délicat qu’il serait trop
long de décrire ici en détail ; nous allons tout de même rappeler quelques faits. Suivant
Berkovich, si X est un espace topologique et si (Xi ) est une famille de parties de X,
nous dirons que les Xi constituent
                           S         un G-recouvrement de X si tout point x de X possède
un voisinage de la forme i∈J Xi où J est fini et où x ∈ Xi pour tout i ∈ J. Si l’on
ne s’astreint à recoller que des espaces strictement affinoïdes, on obtient la classe des
espaces strictement k-analytiques.
   Soit X un espace k-analytique. C’est en particulier un espace topologique dont tout
point possède une base de voisinages compacts (mais X n’est pas nécessairement lo-
calement compact puisqu’un espace topologique localement compact est par définition
séparé, et que ce n’est pas forcément le cas de X). L’espace X possède par ailleurs une
classe distinguée de partie compactes, ses domaines affinoïdes (si X = M (A ), les do-
maines affinoïdes de X sont précisément ceux décrits au 11.1.5 ci-dessus). Un domaine
analytique de X est une partie de X qui est G-recouverte par les domaines affinoïdes
qu’elle contient. Tout domaine affinoïde de X est un domaine analytique de X ; plus
généralement, tout compact de X qui est une union finie de domaines analytiques de
X est un domaine analytique. Et tout ouvert de X (et notamment X lui-même) est un
domaine analytique. En particulier, tout point x de X possède un voisinage compact
qui est une réunion finie de domaines affinoïdes contenant x. Les espaces définis dans [8]
sont ceux qui sont qualifiés de bons dans [9], c’est-à-dire ceux dont tout point admet un
voisinage affinoïde (et donc une base de voisinages affinoïdes.) Tout domaine analytique
de X est une partie localement fermée de X : l’intersection d’une famille finie de do-
maines analytiques est un domaine analytique ; la réunion d’une famille localement finie
de domaines analytiques fermés est un domaine analytique.
   Tout domaine analytique V de X hérite d’une structure canonique d’espace analy-
tique, et d’un morphisme V ,→ X dont l’application sous-jacente est l’inclusion. Tout
morphisme f : Y → X se factorisant ensemblistement par V se factorise en fait unique-
ment par la structure analytique de V .
```

## analytic-calculus

Primary: <https://arxiv.org/pdf/1204.6277v2>. LF 22105–22126; unit SHA256 `960861bd1391008caa52be28ee8a788b6bdc3df269d765f603121a8bab0af320`.

```text
Théorème 15.7.1. — Soit X un espace analytique purement de dimension n, topolo-
giquement séparé. Muni de son bord ∂(X) au sens de la théorie des espaces analytiques,
l’espace G-tropical affiné et calibré de niveau n associé à X est un espace tropical de
niveau n.

Démonstration. — Vérifions les conditions de la définition 6.6.2.
  L’intérieur Int(X) de X est localement holomorphiquement séparé (15.2.2) ; il est donc
localement différentiellement séparé (corollaire 15.2.4). Il est décent (proposition 12.4.7)
car il est sans bord, donc bon, donc presque bon. Il est très riche (théorème 12.11.1) et
harmonieux (théorème 15.6.1).
  Et il résulte du corollaire 12.9.14 que Σ ∩ ∂X est n-négligeable pour toute partie
paralinéaire Σ de X, de même que Σ∩∂(V /X) pour tout domaine V de X car ∂(V /X) ⊂
∂V .
  On munit ainsi tout espace analytique X, topologiquement séparé, et purement de
dimension n, d’une structure d’espace tropical de niveau n.
              § 15.7. L’ESPACE TROPICAL ASSOCIÉ À UN ESPACE ANALYTIQUE              433

15.7.2. — Soit X un espace analytique topologiquement séparé, purement de dimen-
sion n et soit V un domaine de X. Le domaine V est muni de deux façons, a priori
distinctes, d’une structure d’espace tropical de niveau n, soit comme espace analytique,
soit comme domaine de l’espace tropical X. La formule ∂(V ) = (∂(X) ∩ V ) ∪ ∂(V /X)
montre que ces deux structures coïncident.
```

## generic-lengths

Primary: <https://arxiv.org/pdf/1204.6277v2>. LF 23434–23459; unit SHA256 `52dbd2e0b2cf6d2c6220cb31fdf4683247d2c282b0b8055f6a2bf8735129d742`.

```text
Proposition 16.6.3. — Soit Y un sous-espace analytique fermé de X, purement de
dimension p. On a δY = δ[Y ] .

Démonstration. — Notons j l’immersion   R de     Y dans X. Soit ω une (p, p)-forme à support
                                              ∗
compact sur X. On a donc ⟨δY , ω⟩ = Y j ω, ce qui permet de supposer que Y = X.
  Soit (Xi ) la famille des composantes irréductibles de X et, pour tout i, soit mi la
multiplicité de X le long de Xi . Soit X ′ l’ouvert de Zariski de X constitué des points qui
sont situés sur une unique composante irréductible de X ; il contient le support de ω.
Pour tout i, posons Xi′ = X ′ ∩ Xi ; c’est un ouvert de X et l’on a
                             Z            Z              Z
                                                       1
                                     ω=            ω=        ω,
                              Xi,red          ′
                                            Xi,red    mi Xi′
                                                              ′
en vertu de la proposition 15.4.3 appliquée à l’immersion de Xi,red dans Xi′ , dont le degré
calibré est 1/mi (proposition 13.3.7). Alors, on a
              Z      Z        XZ          X Z               X Z
   ⟨δX , ω⟩ =    ω=      ω=          ω=        mi      ω=       mi        ω = ⟨δ[X] , ω⟩,
              X       X′       i   Xi′       i
                                                      ′
                                                     Xi,red       i   Xi,red


comme il fallait démontrer.
```

## generated-psh

Primary: <https://arxiv.org/pdf/1204.6277v2>. LF 9729–9781; unit SHA256 `fa2e29bcb98fd26a55598c0dc4c67b162d19d4b1780b39f2a49bdfc7e4373830`.

```text
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
```

## generated-cpsh-diagnostic

Primary: <https://arxiv.org/pdf/1204.6277v2>. LF 9797–9863; unit SHA256 `5ef01dd5ed01e2349c223afadbb34c535cb304dce255f10115f25edccd4899da`.

```text
Définition 8.1.7. — On note CPshX le plus petit sous-faisceau du faisceau CX des
fonctions continues sur X tel que pour tout ouvert U de X, l’ensemble CPshX (U ) vérifie
les propriétés :
   i) Il contient les fonctions lisses u sur U telles que d′ d′′ u ⩾ 0 ;
                        § 8.1. FONCTIONS PLURISOUSHARMONIQUES                          197

  ii) Il est stable par limite uniforme.
  On note CPshX ce sous-faisceau ; ses sections sont appelées des fonctions continues
plurisousharmoniques (cpsh).
Lemme 8.1.8. — Pour tout ordinal α, on définit par récurrence transfinie un sous-
faisceau CPshX,α par les conditions suivantes :
   a) On définit CPshX,0 comme le faisceau des fonctions lisses u telles que d′ d′′ u ⩾ 0 ;
   b) Si α est un ordinal, on définit CPshX,α+1 comme le sous-faisceau des fonctions
sur X qui sont localement limites uniforme de fonctions de CPshX,α ;
   c) Si α est un ordinal limite, on définit CPshX,α comme le sous-faisceau des fonctions
sur X qui appartiennent localement à un CPshX,β pour β < α.
La famille ordinale (CPshX,α ) est une famille croissante de sous-faisceaux de CPshX qui
vaut CPshX pour α assez grand.
Démonstration. — La démonstration est analogue à celle du lemme 8.1.4 en remplaçant
partout « limite décroissante » par « limite uniforme ».

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
```

## positive-decomposition

Primary: <https://arxiv.org/pdf/1204.6277v2>. LF 7359–7381; unit SHA256 `7d7b6d6687db0b922b6e69a1011a9dcb0a2d112c41d65200901f1efd7275db83`.

```text
Proposition 6.5.2. — Soit ω une forme de type (p, p) et symétrique sur X, à coef-
ficients dans G dont le support est contenu dans un ouvert paracompact et localement
différentiellement séparé de X.
   a) Il existe des formes positives ω1 et ω2 sur X, à coefficients dans G , telles que
ω = ω1 − ω2 .
   b) Si, de plus, le support de ω est compact, les formes ω1 et ω2 peuvent être choisies
à support compact.
   L’hypothèse sur le support de ω est notamment réalisée lorsque X est localement
différentiellement séparé et paracompact. Dans le cas des espaces analytiques, elle sera
également réalisée si le support de ω est compact et si l’espace X est presque bon.
Démonstration. — Soit U un voisinage ouvert paracompact et localement différentielle-
ment séparé du support de ω. Dans le second cas, on s’arrange en outre pour que U soit
relativement compact dans X, ce qui est possible car X possède une base d’ouverts qui
sont dénombrables à l’infini.
   Soit (fi , Pi ) une famille de cartes tropicales, de sorte que fi soit un moment sur un
ouvert Vi de X et Pi un polytope compact contenant fi,trop (Vi ), et, pour tout i, soit αi
une forme sur Pi telle que ω|Vi = fi∗ αi . Il existe alors une famille localement finie (λi ) de
fonctionsP lisses sur X, subordonnée au recouvrement (U ∩Vi )i∈I telles que 0 ⩽ λi ⩽ 1 pour
tout i et λi est identiquement égale à 1 au voisinage du support de ω (corollaire 6.2.8).
Pour tout i, choisissons des formes positives  P αi,1 ∗et αi,2 sur Pi telles
                                                                       P que       αi = αi,1 − αi,2
(proposition 1.10.2). Posons alors ω1 =           λi fi αi,1 et ω2 =      λi fi∗ αi,2 ; ce sont des
formes lisses et positives telles que ω = ω1 − ω2 .
```

## middle-positivity

Primary: <https://arxiv.org/pdf/1204.6277v2>. LF 7918–7981; unit SHA256 `7e8a9c9f610a102901ed491e3e572f9b96528cf24e5f8733f1d4f3d419801332`.

```text
  Soit X un espace tropical de niveau n.
Définition 7.2.1. — Soit p un entier. Un courant S de bidimension (p, p) est dit
faiblement positif, respectivement positif, respectivement fortement positif, s’il est sy-
métrique et si pour toute forme α ∈ Acp,p (X) qui est fortement positive, respectivement
positive, respectivement faiblement positive, on a ⟨S, α⟩ ⩾ 0.
7.2.2. — Les trois notions de positivité pour les formes de type (0, 0) et (n, n) coïn-
cident ; il en est donc de même pour les courants. Comme les différentes notions de
positivité coïncident pour les formes symétriques de type (1, 1) et (n − 1, n − 1), il en
est de même pour les courants symétriques.
Remarque 7.2.3. — Soit T un courant tel que T et −T sont positifs ; démontrons
que T = 0. Soit ω une forme lisse à support compact sur X ; prouvons que ⟨T, ω⟩ = 0.
Si ω est antisymétrique, cela découle de la symétrie de T ; supposons donc que ω est
symétrique. Il existe aussi des formes positives α1 et α2 , lisses à support compact telles
que ω = α1 − α2 (proposition 6.5.2). Par linéarité, on peut donc supposer que ω est
positive. Mais alors, ⟨T, ω⟩ est à la fois positif (T est positif) et négatif (−T est positif),
donc nul.
Lemme 7.2.4. — Supposons que l’espace tropical X soit localement différentiellement
séparé. Les courants de bidimension (p, p) positifs ( resp. faiblement positifs, resp. for-
tement positifs) forment un sous-faisceau du faisceau Dp,p (X) des courants de bidimen-
sion (p, p).
Démonstration. — Soit S un courant de bidimension (p, p) sur X.
   Supposons que S soit positif. Soit U un ouvert de X. Pour toute forme ω sur U , de
type (p, p), positive et à support compact, le prolongement par 0 de ω est une forme
positive à support compact sur X. Il en résulte que S|U est positif.
   Soit maintenant (Ui ) un recouvrement ouvert de X tel que S|Ui soit positif pour tout i ;
démontrons que S est positif. Soit ω une forme de type (p, p) sur X, positive et à support
compact. Reprenons la preuve que les faisceaux forment un courant (proposition 7.1.7).
Il existe une famille finie (φi ) de fonctions lisses, positives et à support compact sur X
                                  § 7.2. COURANTS POSITIFS                                 161
                                                                              P
telle que pour tout i, le support de φi soit contenu dans P Ui , et telle que   φi soit égale
à 1 au voisinage du support de ω. On a de plus ⟨S, ω⟩ = ⟨S, φi ω⟩ ⩾ 0. Pour tout i, on
a a ⟨S, φi ω⟩ ⩾ 0, car φi ω est une forme positive dont le support est compact et contenu
dans Ui . Cela démontre que S est positif.
   Appliqué à chaque ouvert de X, cet argument démontre que les courants positifs de bi-
dimension (p, p) forment un sous-faisceau du faisceau des courants de bidimension (p, p).
Les cas des courants faiblement positifs et fortement positifs se démontrent de même.

Lemme 7.2.5. — Supposons que X soit localement différentiellement séparé. Soit T un
courant sur X. On suppose que pour tout ouvert U de X, toute forme tropicale ω sur U
qui est positive ( resp. faiblement positive, resp. fortement positive) et toute fonction lisse
positive ρ dont le support est compact et contenu dans U , on a ⟨T, ρω⟩ ⩾ 0. Alors T est
positif ( resp. fortement positif, resp. faiblement positif ).
Démonstration. — On traite le cas des formes positives, les deux autres sont analogues.
Soit ω une forme lisse positive à support compact sur X ; démontrons que ⟨T, ω⟩ ⩾ 0.
Pour tout x ∈ X, soit Ux un voisinage ouvert de X sur lequel ω est tropicale. Soit
                                                                       que, pour tout x ∈ X,
(λx )x∈X une famille à support fini de fonctions lisses positives telleP
le support de λx soit compact et contenu dans Ux , et telle que   P      λx soit égale à 1 au
voisinage du support de ω (corollaire 6.2.8). On a alors ω = x∈X λx ω. Par hypothèse,
⟨T, λx ω⟩ ⩾ 0 pour tout x. Donc ⟨T, ω⟩ ⩾ 0.

7.2.6. — L’image directe d’un courant positif (resp. faiblement positif, fortement po-
sitif) par un morphisme topologiquement propre d’espaces tropicaux est de même type.
Cela résulte du fait que la même propriété vaut pour l’image inverse des formes (§3.5.2).
Lemme 7.2.7. — Soit α une forme lisse symétrique sur X et soit T un courant symé-
trique sur X.
   a) Supposons que la forme α soit fortement positive. Alors, si T est positif ( resp.
faiblement positif, resp. fortement positif ), il en est de même de T ∧ α.
   b) Supposons que la forme α soit positive. Si T est positif, le courant T ∧ α est positif.
   c) Supposons que la forme α soit faiblement positive. Si T est fortement positif, le
courant T ∧ α est faiblement positif.
Démonstration. — Ces assertions découlent des propriétés de positivité d’un produit de
deux formes (prop. 3.5.5).
```

## positive-scalar-measures

Primary: <https://arxiv.org/pdf/1204.6277v2>. LF 7983–8011; unit SHA256 `089af75e6237f117a1ff411156580da33c01951d926d14ecc613c1bf86f77060`.

```text
Proposition 7.2.8. — Soit X un espace tropical de niveau n, localement différentiel-
lement séparé.
  a) Toute mesure de Radon positive µ sur X induit, par restriction à Ac (X), un courant
positif [µ] d’ordre 0.
  b) L’application µ 7→ [µ] ainsi définie est une bijection continue de l’espace des me-
sures de Radon positives sur X sur l’espace des courants positifs de bidimension (0, 0)
sur X.
Démonstration. — a) Soit µ une mesure de Radon positive sur X ; démontrons que
la forme linéaire [µ] est un courant ; ce sera alors un courant positif. Soit K une partie
compacte de X et soit D un jeu de cartes couvrant sur X. Il suffit de démontrer que
la restriction de [µ] à l’espace AD,K
                                  0,0
                                      (X) est continue pour sa topologie C 0 . Soit ∥µ∥K
162                  CHAPITRE 7. COURANTS SUR UN ESPACE TROPICAL

la norme de µ sur K : pour toute fonction continue à support compact sur K, on a
|µ(f )| ⩽ ∥µ∥K ∥f ∥K . Cette inégalité vaut a fortiori pour toute fonction de AD,K (X) et
entraîne la continuité voulue.
   b) Cette implication est injective car l’espace des fonctions lisses à support compact
est dense dans l’espace des fonctions continues à support compact (corollaire 6.2.6).
   Il reste à prouver qu’elle est surjective. Soit S un courant positif de bidimension (0, 0)
sur X. Soit K une partie compacte de X. Soit λ une fonction lisse et positive, à support
compact sur X, qui vaut 1 au voisinage de K. Pour toute fonction lisse f sur X dont
le support est contenu dans K, on a −∥f ∥K λ ⩽ f ⩽ ∥f ∥K λ. Comme S est positif, il en
résulte l’inégalité
                                     |S(f )| ⩽ ∥f ∥K S(λ).
Par suite, S est continu lorsque l’espace des fonctions lisses à support compact est muni
de la topologie de la convergence compacte. Par densité, S s’étend en une forme linéaire
positive sur Cc (X), c’est-à-dire en une mesure de Radon positive.
```

## ordinary-product

Primary: <https://arxiv.org/pdf/1204.6277v2>. LF 8054–8076; unit SHA256 `f647601926c2311a3319b181f2567f487f9a88ce4870332c75ecc8bb5f3156d4`.

```text
7.2.11. — Soit X un espace tropical de niveau n, localement différentiellement séparé.
Soit p un entier naturel et soit T un courant positif (resp. faiblement positif, resp.
fortement positif) de bidimension (p, p).
   Soit ω une forme positive (resp. fortement positive, resp. faiblement positive) de bide-
gré (p, p). Le courant T ∧ω est positif, de bidimension (0, 0) ; d’après la proposition 7.2.8,
il est donc associé à une unique mesure µTω sur X. Cette mesure applique une fonction
lisse à suppport compact u sur ⟨uT, ω⟩. Lorsque ω est à support compact, cette mesure
est à support compact. Lorsque ω est positive, cette mesure est positive.
Exemple 7.2.12. — Soit X un espace tropical de niveau n, localement différentiel-
lement séparé. Soit p un entier naturel et soit T un courant positif (resp. faiblement
positif, resp. fortement positif) de bidimension (p, p). Soit u une fonction borélienne et
localement bornée sur X. L’application ω 7→ µTω (u) est une forme linéaire sur Acp,p (X)
que nous noterons uT .
   Lorsque u est positive, cette forme linéaire uT est positive, donc est un courant positif
(resp. faiblement positif, resp. fortement positif) sur X.
   Lorsque u est une fonction borélienne et localement bornée arbitraire, on l’écrit u =
u − u− , où u+ = sup(u, 0) et u− = sup(−u, 0), comme différence de deux fonctions
  +

positives boréliennes localement bornées sur X. Comme uT = u+ T − u− T , c’est un
courant sur X, d’ordre 0.
   Cette notation est compatible avec celle déjà introduite lorsque u est une fonction
lisse puisque l’on a alors ⟨uT, ω⟩ = ⟨T, uω⟩ = µTω (u).
```

## current-sheaf

Primary: <https://arxiv.org/pdf/1204.6277v2>. LF 7756–7818; unit SHA256 `0d1a24130ba9c326713dcafecb5aa9a83678fb264cbd51fe4d1005de11869d48`.

```text
7.1.6. Propriété de faisceau. — Soit T un courant sur X. Soit U un ouvert de X
et soit j l’immersion de U dans X. Comme l’opération j! de prolongement par 0 des
formes à support compact sur U est une application linéaire continue (prop. 6.4.5),
l’application α 7→ ⟨T, j! α⟩ est un courant T |U sur X qu’on appelle restriction de T à U .
Si T est d’ordre ⩽ r, il en est de même de T |U .
   L’application U 7→ Dp,q (U ) est ainsi un préfaisceau, et pour tout entier r, les courants
d’ordre ⩽ r en forment un sous-préfaisceau.
   Pour tout courant T et tout ouvert U , on a JT |U = (JT )|U .

Proposition 7.1.7. — Supposons que l’espace tropical X soit localement différentiel-
lement séparé. Le préfaisceau Dp,q sur X est un faisceau de A 0,0 -modules. Pour tout
entier r, le sous-préfaisceau des courants d’ordre ⩽ r en est un sous-faisceau.

   En particulier, l’ordre d’un courant est une notion locale.
Démonstration. — Soit (Ui ) un recouvrement ouvert d’un ouvert U de X, pour tout i,
soit Si un courant sur Ui tels que la restriction à Ui ∩ Uj des courants Si et Sj coïncident,
pour tous i, j. Démontrons qu’il existe un unique courant S sur U dont la restriction
à Ui est égale à Si .
   Soit ω une (p, q)-forme à support compact sur U . Soit (φi ) une famille finie de fonctions
lissesPà support compact sur U telle que le support de φi est contenu dans Ui P          et telle
que φi soit égale à 1 au voisinage du support de ω (corollaire 6.2.8). On a ω =             φi ω,
et seuls un nombre fini de termes de cette somme sont non nuls. Si S est un courant    P   sur U
dont la restriction à Ui est égale à Si , on a donc nécessairement ⟨S, ω⟩ = ⟨Si , φi ω⟩,
d’où l’unicité d’un courant S vérifiant les conditions requises.
   Soit (φ′i ) une seconde famille finie de fonctions lisses
                                                         P ′ à support compact sur U telle
                        ′
que le support de φi soit contenu P dans      Ui et que      φj soit égale à 1 au voisinage du
                                          ′
support de ω. On a aussi ω = i,j φj φi ω, si bien que
               X                 X                  X                   X
                  ⟨φ′j ω, Sj ⟩ =  ⟨φ′j φi ω, Sj ⟩ =   ⟨φ′j φi ω, Sj ⟩ =   ⟨φi ω, Si ⟩,
              j                i,j                i,j                  i

où la deuxième égalité découle de la condition de coïncidence des courants Si .
PIl existe donc une unique application S de l’espace Ac (U ) dans R telle que ⟨S, P
                                                             p,q
                                                                                       ω⟩ =
   ⟨Si , φi ω⟩ pour tout famille (φi ) de fonctions lisses à support compact telle que   φi
soit égale à 1 au voisinage du support de ω. Cette application est linéaire.
   Démontrons que c’est un courant sur U . Soit K une partie compacte de U . Considérons
alors une famille finie (φi ) de fonctions lisses à support compact dont la somme est égale
à 1 au voisinage de K et telle que le support de φi soit contenu dans Ui . Pour tout i,
l’application ω 7→ φi ω de AKp,q (U ) dans Acp,q (Ui ) est continue, donc la forme P
                                                                                   linéaire ω 7→
⟨Si , φi ω⟩ sur AK (U ) est continue. Pour tout ω ∈ AK (U ), on a ⟨S, ω⟩ = i ⟨Si , φi ω⟩.
                 p,q                                         p,q
158                 CHAPITRE 7. COURANTS SUR UN ESPACE TROPICAL

Par suite, la restriction de S à AKp,q (U ) est continue. Cela prouve que S est continue ;
c’est donc un courant sur U .
   Soit ω une (p, q)-forme dont le support est compact et contenu dans Uj ; soit (φi )
une famille comme ci-dessus. Pour tout i, le support de φi ω est contenu dans Ui ∩ Uj ,
donc ⟨Si , φi ω⟩ = ⟨Sj , φi ω, Si ⟩. Alors,
                                    X                X
                        ⟨S, ω⟩ =       ⟨Si , φi ω⟩ =   ⟨Sj , φi ω⟩ = ⟨Sj , ω⟩
         P
puisque φi est égal à 1 au voisinage du support de ω. Cela démontre que la restriction
à Uj du courant S est égale à Sj et conclut la démonstration que les courants forment
un faisceau.
   Avec les notations qui précèdent, l’ordre de S est ⩽ r si les Si sont tous d’ordre ⩽
r. Cela entraîne que courants d’ordre ⩽ r forment un sous-faisceau du faisceau des
courants.
```

## current-differentials

Primary: <https://arxiv.org/pdf/1204.6277v2>. LF 9309–9381; unit SHA256 `a396b6b027f3375f6aa7b3e89bac0319a21ad2c96f44971acb018cec52648801`.

```text
  Soit X un espace tropical de niveau n.
7.7.1. — L’application linéaire d′ de Acp,q (X) dans Acp+1,q (X) est continue (prop. 3.7.13).
On note b′ sa transposée de Dp+1,q (X) dans Dp,q (X). Si T est un courant d’ordre ⩽ r,
alors b′ T est un courant d’ordre ⩽ r + 1.
   On définit de même b′′ : Dp,q+1 (X) → Dp,q (X) comme la transposée de l’application d′′ .
   Il résulte de la définition de la topologie des espaces de courants que ces applications
linéaires b′ et b′′ sont continues.
   Par dualité, la relation d′′ ω = J d′ J−1 ω entraîne l’égalité
(7.7.1.1)                                   b′′ = Jb′ J−1 .
                          § 7.7. CALCUL DIFFÉRENTIEL SUR LES COURANTS                  187

  On a aussi les relations (b′ )2 = 0, (b′′ )2 = 0, et b′ b′′ = −b′′ b′ .
7.7.2. — Soit ω une G-forme de type (p, q) sur X et soit [ω] le courant de bidegré (p, q)
qui lui est associé. Pour toute forme α ∈ Acn−p−1,n−q (X), on a

                              d′ (ω ∧ α) = d′ ω ∧ α + (−1)p+q ω ∧ d′ α.

La formule de Stokes (proposition 5.11.1) entraîne alors l’égalité
            Z ∂         Z               Z                        Z
                             ′               ′
                ω∧α=       d (ω ∧ α) =      d ω ∧ α + (−1)   p+q
                                                                   ω ∧ d′ α,
                 X               X                   X                      X

autrement dit
                                     [d′ ω] = [ω]∂ + (−1)p+q+1 b′ [ω].
Si l’on définit l’opérateur d′ de D p,q (X) dans D p+1,q par

(7.7.2.1)                                   d′ = (−1)p+q+1 b′ ,

il vient alors

(7.7.2.2)                                 d′ [ω] = [d′ ω] − [ω]∂ .

Lorsque X est sans bord et ω est une forme sur X, le courant [ω]∂ est nul, et l’on a

(7.7.2.3)                                     d′ [ω] = [d′ ω].
7.7.3. — De même, on pose

(7.7.3.1)                                  d′′ = (−1)p+q+1 b′′ .

On en déduit que les relations du lemme 1.3.6 sont encore valides sur les espaces de
courants :

(7.7.3.2)                              d′′ = J d′ J−1 = −J−1 d′ J
(7.7.3.3)                                   (d′ )2 = (d′′ )2 = 0
(7.7.3.4)                                    d′′ d′ = − d′ d′′
(7.7.3.5)                                    d′ d′′ J = J d′ d′′ .

  Soit ω une G-forme de type (p, q). On a

                     d′′ [ω] = J d′ J−1 [ω] = J d′ [J−1 ω] = J[d′ J−1 ω] − J[J−1 ω]∂
                           = [J d′ J−1 ω] − J[J−1 ω]∂ ,

de sorte que

(7.7.3.6)                              d′′ [ω] = [d′′ ω] − J[J−1 ω]∂ .

En outre, si X est sans bord et ω est une forme, alors Jω est également une forme, donc
on a

(7.7.3.7)                                    d′′ [ω] = [d′′ ω].
188                  CHAPITRE 7. COURANTS SUR UN ESPACE TROPICAL

7.7.4. — Supposons que l’espace X est sans bord. Comme le courant d’intégration δX
est égal à [1], il est d′ et d′′ -fermé.

Lemme 7.7.5. — Pour tout courant S ∈ Dp,q (X) et toute forme α ∈ Acp,q (X), on a

                                   ⟨d′ d′′ S, α⟩ = ⟨S, d′ d′′ α⟩.

Démonstration. — En effet, d′ d′′ S = ((−1)p+q+2 b′ )((−1)p+q+1 b′′ )S = − b′ b′′ S est
l’image de S par le transposé de − d′′ d′ = d′ d′′ .
```

## cutoffs-density

Primary: <https://arxiv.org/pdf/1204.6277v2>. LF 21619–21696; unit SHA256 `aba28489aa7c1e770af13b87e11c77fbca731f95eb5bc41afb637b378d66ed45`.

```text
15.2.2. Séparation holomorphe. — On dira qu’un espace analytique X est holo-
morphiquement séparé si pour tout couple (x, y) de points de X avec x ̸= y il existe une
fonction analytique f sur X telle que |f (x)| =
                                              ̸ |f (y)|. Un tel espace est topologiquement
séparé.
  Si X est un espace holomorphiquement séparé, il en va trivialement de même de tout
domaine analytique de X.
  Tout espace affinoïde est par définition holomorphiquement séparé ; en conséquence,
tout domaine analytique d’un espace affinoïde est holomorphiquement séparé.
  Un espace analytique sera dit localement holomorphiquement séparé s’il est topologi-
quement séparé et si chacun de ses points possède un voisinage analytique holomorphi-
quement séparé.
  Un espace analytique topologiquement séparé qui est bon, ou plus généralement dont
tout point possède un voisinage isomorphe à un domaine analytique d’un espace affi-
noïde, est localement holomorphiquement séparé. C’est en particulier le cas d’un espace
analytique topologiquement séparé sans bord.

Lemme 15.2.3. — Soit X un espace k-analytique holomorphiquement séparé. L’an-
neau des fonctions lisses sur X sépare les points.

Démonstration. — Soit x, y des points distincts de X. Par définition de la séparation
holomorphe, il existe une fonction analytique f sur X telle que |f (x)| =     ̸ |f (y)|.
  Supposons ces deux valeurs non nulles ; soit φ une fonction C ∞ à support compact
sur R valant 0 au voisinage de log|f (x)| et 1 au voisinage de log|f (y)|. La fonction
φ ◦ log|f |, définie sur l’ouvert d’inversibilité de f , est lisse ; prolongeons-la par 0 sur X
tout entier. Comme φ est à support compact, la fonction obtenue est nulle au voisinage
de l’ensemble des zéros de f ; elle est donc lisse et prend des valeurs différentes en x et y.
  Si f (x) = 0, on a alors f (y) ̸= 0 et on raisonne de même à partir d’une fonction φ à
support compact valant 1 au voisinage de log|f (y)|.
  Le cas où f (y) = 0 est analogue par symétrie.

Corollaire 15.2.4. — Soit X un espace k-analytique localement holomorphiquement
séparé. L’espace G-tropical affiné X est localement différentiellement séparé. En parti-
culier, le faisceau des fonctions lisses sur X sépare localement les points.
424 CHAPITRE 15. FORMES DIFFÉRENTIELLES RÉELLES EN GÉOMÉTRIE ULTRAMÉTRIQUE

Corollaire 15.2.5. — Soit X un espace analytique localement holomorphiquement sé-
paré. Soit K une partie compacte de X et soit U un voisinage ouvert de K. Il existe
une fonction lisse sur X qui vaut 1 au voisinage de K et dont le support est compact et
contenu dans U .
Démonstration. — Comme X est localement différentiellement séparé, c’est une consé-
quence du corollaire 6.2.4.

Théorème 15.2.6 (Stone–Weierstraß). — Soit X un espace analytique localement
holomorphiquement séparé et soit U un ouvert de X. Soit f une fonction continue à
valeurs réelles sur X dont le support est compact et contenu dans U . Soit a et b des
nombres réels tels que a ⩽ f ⩽ b. Pour tout ε > 0, il existe une fonction lisse g sur X
dont le support est compact, contenu dans U , telle que |f (x) − g(x)| < ε pour tout x ∈ X
et telle que a ⩽ g ⩽ b.
Démonstration. — Comme X est localement différentiellement séparé, c’est une consé-
quence du théorème 6.2.5.

Corollaire 15.2.7. — Soit X un espace analytique localement holomorphiquement sé-
paré.
  a) L’ensemble des fonctions lisses à support compact sur X est dense dans l’es-
pace Cc (X) des fonctions continues à support compact sur X, muni de la topologie limite
inductive des espaces de fonctions à support dans un compact donné.
  b) L’ensemble des fonctions lisses à support compact sur X est dense dans l’es-
pace C (X) des fonctions continues sur X muni de la topologie de la convergence uniforme
sur tout compact.
Démonstration. — Comme X est localement différentiellement séparé, c’est une consé-
quence du corollaire 6.2.6.

Proposition 15.2.8 (Partitions de l’unité lisses). — Soit X un espace analytique
localement holomorphiquement séparé, paracompact. Soit (Ui )i∈I un recouvrement ouvert
de X. Il existe une partition de l’unité subordonnée à (Ui ) formée de fonctions lisses
sur X.
Démonstration. — Comme X est localement différentiellement séparé, cela résulte de la
proposition 6.2.7.

Corollaire 15.2.9. — Soit X un espace analytique localement holomorphiquement sé-
paré et soit F une partie fermée de X qui est dénombrable à l’infini (par exemple, com-
pacte). Soit (Ui )i∈I un recouvrement de K par des ouverts de X. Il existe une famille
localement finie (θi ) de fonctions lisses sur X, à support
                                                          P compact, positives, telle que
pour tout i, le support de θi soit contenu dans Ui et que   θi vaille 1 au voisinage de F .
Démonstration. — Comme X est localement différentiellement séparé, cela résulte du
corollaire 6.2.8.
```

## form-leibniz

Primary: <https://arxiv.org/pdf/1204.6277v2>. LF 3769–3803; unit SHA256 `172d214bed8f4a1ffbfd19dcf120345ce08abbc69c0b70160a6af23832c8eff0`.

```text
3.3.10. — Le faisceau GXG := GX0,0G est un faisceau en R-algèbres et les faisceaux GXp,qG
sont des GXG -modules. Leur somme directe GX∗,∗G = p,q GXp,qG est un faisceau en algèbres
                                                   L

bigraduées commutatives : si ω est de type (p, q) et ω ′ de type (p′ , q ′ ), alors
                                                    ′     ′
                                ω ′ ∧ ω = (−1)(p+p )(q+q ) ω ∧ ω ′ .
3.3.11. — Le G-préfaisceau Gpf∗,∗ est naturellement muni d’un opérateur J qui s’étend
au faisceau GX∗,∗G . Ce sont des morphismes d’algèbres. On dit qu’une section ω de GXp,qG
est symétrique si p = q et si Jω = ω.
    Soit H une classe de coefficients telles que les dérivées partielles des fonctions de G
existent et appartiennent à H . On dispose alors d’opérateurs différentiels d′ et d′′ de
Gpf∗,∗ dans Hpf∗,∗ ; ils induisent des opérateurs différentiels de GX∗,∗G dans HX∗,∗
                                                                                  G
                                                                                     , caractérisés
par les relations
                               d′ f ∗ α = f ∗ d′ α, d′′ f ∗ α = f ∗ d′′ α,
                                 § 3.4. NULLITÉ DES G-FORMES                             81

pour toute carte G-tropicale (f : U → E, P ) et toute forme α de type (p, q) à coeffi-
cients dans G sur P . Les différentielles vérifient la règle de Leibniz : si ω et ω ′ sont
respectivement de type (p, q) et (p′ , q ′ ), on a
(3.3.11.1)               d′ (ω ∧ ω ′ ) = d′ ω ∧ ω ′ + (−1)p+q ω ∧ d′ ω ′ ,
et de même pour d′′ (ω ∧ ω ′ ).
   Si G ⊂ C 2 , ces opérateurs vérifient d′ d′ = d′′ d′′ = 0.
3.3.12. — Cette construction est fonctorielle. Plus précisément, si f : Y → X est un
morphisme d’espaces G-tropicaux, on dispose de morphismes de faisceaux
                                     f ∗ : GX∗,∗G → f∗ (GY∗,∗
                                                           G
                                                              )
sur XG qui sont des morphismes d’anneaux gradués, commutent aux dérivations d′ et
d′′ (lorsqu’elles existent) et à l’opérateur J.
   Lorsque le contexte rend évident le morphisme f , on se permettra parfois de noter
ω|Y l’image dans GYp,q G
                         (Y ) d’une G-forme ω ∈ GXp,qG .
```

## weak-multiplier

Primary: <https://arxiv.org/pdf/1204.6277v2>. LF 10257–10281; unit SHA256 `0eec1c45dfec34af7fb8e231160cc24fd3ef9b8f6dc1185fb8eedd1905483114`.

```text
Lemme 8.5.1. — Soit (Tn ) une suite de courants positifs et soit (un ) une suite de
fonctions continues. On suppose que la suite (Tn ) converge vers un courant T et que la
suite (un ) converge localement uniformément vers une fonction u. On a un Tn → uT .
206                      CHAPITRE 8. THÉORIE DE BEDFORD–TAYLOR

Démonstration. — On peut raisonner localement et supposer que (un ) converge uni-
formément vers u. Soit ε > 0 et soit v une fonction lisse telle que ∥u − v∥ ⩽ ε ; on
écrit
                 un Tn − uT = (un − v)Tn + v(Tn − T ) + (v − u)T.
Soit ω une forme lisse à support compact, et soit α, β des formes lisses positives à support
compact telles que ω = α − β. Comme Tn est positif, on a
      |⟨(un − v)Tn , ω⟩| ⩽ |⟨(un − v)Tn , α⟩| + |⟨(un − v)Tn , β⟩| ⩽ ∥un − v∥⟨Tn , α + β⟩.
Comme v est lisse, le second terme
                                 ⟨v(Tn − T ), ω⟩ = ⟨Tn − T, vω⟩
tend vers 0 quand n tend vers +∞. Enfin, comme T est positif,
                             |⟨(v − u)T, ω⟩| ⩽ ∥v − u∥⟨T, α + β⟩.
Cela démontre que
               lim sup|⟨un Tn − uT, ω⟩| ⩽ 2∥u − v∥⟨T, α + β⟩ ⩽ 2ε⟨T, α + β⟩.
                  n

Comme ceci vaut pour tout ε, on a
                                    lim⟨un Tn , ω⟩ = ⟨uT, ω⟩.
                                      n

Cela prouve que un Tn → uT .
```

## smooth-multiplier

Primary: <https://arxiv.org/pdf/1204.6277v2>. LF 10283–10326; unit SHA256 `364ca08767840b4b45382d42e9e0a5b18b7f7c1b2daf978615413b9a1b5cc985`.

```text
8.5.2. — Soit T un courant de bidegré (p, p) sur X qui est positif et fermé. L’hypothèse
que T est fermé signifie d′ T = 0 et d′′ T = 0. Par définition d’un courant positif, le
courant T est symétrique ; ainsi, chacune de ces annulations entraîne l’autre.

Lemme 8.5.3. — Soit S un courant fermé symétrique de bidegré (p, p), soit q un entier
tel que q ⩽ p − 1 et soit α une forme lisse symétrique de type (q, q). On a
                                  d′ d′′ (α ∧ S) = (d′ d′′ α) ∧ S.

Démonstration. — Soit β une forme lisse de type (p − q − 1, p − q − 1) ; démontrons que
l’on a
                         ⟨d′ d′′ α ∧ S, β⟩ = ⟨α ∧ S, d′ d′′ β⟩.
Comme les courants d′ d′′ α ∧ S et α ∧ S sont symétriques, on peut supposer que β est
symétrique. Par définition, on a
              ⟨d′ d′′ α ∧ S, β⟩ − ⟨α ∧ S, d′ d′′ β⟩ = ⟨S, d′ d′′ α ∧ β − α ∧ d′ d′′ β⟩.
Or, on a

  d′ (α d′′ β − d′′ α ∧ β) = d′ α ∧ d′′ β + α d′ d′′ β − d′ d′′ α ∧ β + d′′ α ∧ d′ β.
De plus, on démontre comme dans la preuve du lemme 1.5.10, la forme de type (p, p)
                                    d′ α ∧ d′′ β + d′′ α ∧ d′ β
est antisymétrique. Sa valeur sur le courant symétrique S est donc nulle. Comme S est
fermé, cela entraîne l’égalité voulue.
                               § 8.6. COURANTS DE BEDFORD–TAYLOR                                            207

8.5.4. — Soit T un courant de bidegré (p, p) sur X qui est positif et fermé. Soit u une
fonction psh (continue) sur X. Comme est T est positif, on peut former le courant uT
(exemple 7.2.12) et considérer le courant d′ d′′ (uT ). Si u est lisse, le lemme 8.5.3 entraîne
que l’on a
                   d′ d′′ (uT ) = d′ d′′ (u ∧ T ) = d′ d′′ u ∧ T = T ∧ d′ d′′ (u),
car T est fermé.
  En géométrie complexe, cette remarque est la base de la construction, par Bedford–
Taylor [6], de produits de courants. Nous allons utiliser la même méthode dans ce
contexte. Pour poursuivre la construction, il faut garantir que le courant d′ d′′ (uT ) est
encore positif. C’est le cas si T est positif et u est psh lisse et, plus généralement, si u
est psh en vertu du lemme suivant.
Lemme 8.5.5. — Soit T un courant de bidegré (p, p) sur X, positif et fermé. Pour
toute fonction continue psh u, le courant d′ d′′ (uT ) est positif et fermé.
Démonstration. — Pour tout ouvert U de X, soit P(U ) l’ensemble des fonctions conti-
nues u sur U telles que d′ d′′ (uT |U ) soit un courant positif. Le préfaisceau P ainsi défini
est un sous-faisceau de CX . Si u est psh lisse, on d′ d′′ (uT ) = d′ d′′ (u) ∧ T , donc u appar-
tient à P. Si (un ) est une suite de fonctions de P(U ) qui converge uniformément vers
une fonction u, la suite de courants (un T |U ) converge vers uT |U , donc d′ d′′ (uT |U ) est
limite de la suite de courants (d′ d′′ (un T |U )). Ces courants étant positifs par hypothèse, le
courant d′ d′′ (uT |U ) est positif et u appartient à P(U ). Cela entraîne que le faisceau P
contient le faisceau CPshX , ce qu’il fallait démontrer.
```

## bt-definition-and-closures

Primary: <https://arxiv.org/pdf/1204.6277v2>. LF 10347–10408; unit SHA256 `d6ddcecc24ddb7e5d63f49f8c320e5dd419e2d24b2846e9fbd6025c0f60f1a21`.

```text
8.6.1. — Soit u et v des fonctions psh telles que h = u − v est lisse. Alors on a
d′ d′′ (uT ) = d′ d′′ (hT ) + d′ d′′ (vT ) = d′ d′′ (h) ∧ T + d′ d′′ (vT ), car h est lisse. En particulier,
si d′ d′′ h = 0, on en déduit que d′ d′′ (uT ) = d′ d′′ (vT ). Nous ne savons pas si cette égalité
208                       CHAPITRE 8. THÉORIE DE BEDFORD–TAYLOR

persiste en général, c’est-à-dire sans supposer que h est lisse. Cela nous conduit à poser
la définition suivante.

Définition 8.6.2. — On dit qu’un courant positif fermé T est de Bedford–Taylor si
pour tout ouvert U de X et pour tout couple (u, v) de fonctions psh sur U telles que
d′ d′′ (u) = d′ d′′ (v), on a d′ d′′ (uT |U ) = d′ d′′ (vT |U ).

  Si c’est le cas, il est légitime de noter d′ d′′ (u) ∧ T le courant d′ d′′ (uT ). On s’autorisera
cependant cette notation même si T n’est pas de Bedford–Taylor. Cet abus de notation
sera relativement sans danger car tous les courants que nous construisons dans ce texte
sont de Bedford–Taylor.

Proposition 8.6.3. — Soit (Ui ) un recouvrement ouvert de X tel que T |Ui est de
Bedford–Taylor pour tout i ; alors T est de Bedford–Taylor.

Démonstration. — En effet, soit u, v des fonctions psh sur un ouvert V de X telles que
d′ d′′ (u) = d′ d′′ (v) ; l’égalité de courants d′ d′′ (uT ) = d′ d′′ (vT ) sur V résulte de sa validité
sur chacun des Ui ∩ V . On en déduit que les courants de Bedford–Taylor forment un
sous-faisceau du faisceau des courants positifs fermés.

Exemple 8.6.4. — Le courant δX est de Bedford–Taylor.
 En effet, uδX = [u] donc d′ d′′ (uδX ) = d′ d′′ ([u]) = d′ d′′ u.

Proposition 8.6.5. — Si α est une forme lisse positive fermée et T est de Bedford–
Taylor, alors il en est de même du courant T ∧ α.

Démonstration. — Soit en effet des fonctions u, v psh telles que d′ d′′ (u) = d′ d′′ (v) ; si α
est une forme lisse à support compact, on a
                       d′ d′′ (u(T ∧ α)) = d′ d′′ (uT ∧ α) = d′ d′′ (uT ) ∧ α.
De même, d′ d′′ (v(T ∧ α)) = d′ d′′ (vT ) ∧ α. Comme T est un courant de Bedford–Taylor,
on a d′ d′′ (uT ) = d′ d′′ (vT ), d’où d′ d′′ (uT ) ∧ α = d′ d′′ (vT ) ∧ α. Cela démontre l’égalité
requise.

Proposition 8.6.6. — Soit (Tk ) une suite de courants de Bedford–Taylor qui converge
faiblement vers un courant T . Le courant T est de Bedford–Taylor.

Démonstration. — Le courant T est positif fermé. Si u est une fonction psh, on a
d′ d′′ (uT ) = lim d′ d′′ (uTk ) (lemme 8.5.1). Il en résulte que T est un courant de Bedford–
Taylor.

Corollaire 8.6.7. — Soit T un courant de Bedford–Taylor et soit u une fonction conti-
nue positive. Le courant uT est de Bedford–Taylor.

Démonstration. — Cela se déduit de la proposition par approximation locale par une
fonction lisse.

Proposition 8.6.8. — Soit T un courant de Bedford–Taylor. Pour toute fonction conti-
nue psh u, le courant d′ d′′ (uT ) est de Bedford–Taylor.
                           § 8.7. THÉORIE DE BEDFORD–TAYLOR : ITÉRATION                                             209

Démonstration. — Soit u une fonction psh sur X. Soit P le sous-préfaisceau de CX tel
que, pour tout ouvert U , P(U ) soit l’ensemble des fonctions continues f sur U telles
que d′ d′′ (f T ) soit un courant de Bedford–Taylor ; c’est un faisceau. Si f est lisse psh,
alors d′ d′′ (f T ) = d′ d′′ (f ) ∧ T , qui est de Bedford–Taylor, puisque T l’est, de sorte que P
contient les fonctions lisses psh. Ce faisceau est également stable par limites uniformes
(lemme 8.5.1). Par suite, P contient le faisceau des fonctions psh. En particulier, le
courant d′ d′′ (uT ) est de Bedford–Taylor.
```

## middle-matrix

Primary: <https://arxiv.org/pdf/1204.6277v2>. LF 885–975; unit SHA256 `7ac6fc20a19b2e92f75e58b56564ddba33b24b1dd86814f5a3068e7978c50da1`.

```text

1.2.6. — Expliquons comment la notion de positivité d’une (p, p)-forme symétrique ω
peut s’interpréter en termes de positivité d’une forme bilinéaire qω sur Λp V canonique-
ment associée à ω.
   Pour tout k ∈ N, posons σk = (−1)k(k−1)/2 . Fixons un élément non nul λ de Λn V ∗ .
Par définition les (n, n)-formes positives sont les multiples positifs de σn λ ∧ J(λ).
   On associe à ω une application bilinéaire sur Λn−p (V ∗ ) à valeurs dans An,n (V ) par la
formule (α, β) 7→ ω ∧ α ∧ Jβ.
   Rappelons aussi que le choix de λ fournit un isomorphisme v 7→ φv entre Λp V et
  n−p ∗
Λ V . Pour v ∈ Λp V , φv est la (n − p)-forme sur V donnée par φv (w) = ⟨λ, v ∧ w⟩
pour tout w ∈ Λn−p V . Il en résulte une application bilinéaire bω sur Λp (V ) à valeurs
dans An,n (V ) : pour v, w ∈ Λp V , on a
                                       bω (v, w) = ω ∧ φv ∧ Jφw .
  Par ailleurs, puisqu’elle appartient à Λp V ∗ ⊗ Λp V ∗ , ω « est » une forme bilinéaire qω
sur Λp V , symétrique puisque l’on a supposé que ω est symétrique. Explicitement, si
ω = α ⊗ β, pour α, β ∈ Λp V ∗ , on a
                                        qω (v, w) = ⟨α, v⟩⟨β, w⟩.
  Pour tous v, w ∈ Λp V , on a
(1.2.6.1)                       bω (v, w) = (−1)p(n−p) qω (v, w)λ ∧ Jλ.
Pour démontrer cette formule, on peut se donner une base (e1 , . . . , en ) de V et la base
duale (x1 , . . . , xn ) de V ∗ . On note eI = ei1 ∧ · · · ∧ eip si I = {i1 , . . . , ip } et i1 < · · · < ip ;
on définit d′ xI de manière analogue. On peut aussi supposer que λ = d′ x1 ∧ · · · ∧ d′ xn
et ω = d′ xI ⊗ d′′ xJ , où I, J sont des parties à p éléments de {1, . . . , n}. Si I est une
partie à p éléments de {1, . . . , n}, notons εI la signature de la permutation de {1, . . . , n}
qui est croissante et d’image I sur {1, . . . , p} et est croissante sur {p + 1, . . . , n}. Si K
et L sont des parties à n − p éléments de {1, . . . , n}, on a
                                      (
                                        (−1)p(n−p) εI εJ λ ∧ Jλ si K = ∁I et L = ∁J,
           ω ∧ d′ xK ∧ J d′ xL =
                                        0                            sinon.
En outre, φeK = εK d′ x∁K , si bien que
                                (
                                 (−1)p(n−p) λ ∧ Jλ si I = K et J = L,
                bω (eK , eL ) =
                                 0                 sinon.
                                § 1.2. SUPERFORMES POSITIVES                                  25

Enfin,                                                      (
                                                             1 si I = K et J = L,
               qω (eK , eL ) = ⟨d′ xI , eK ⟩⟨d′ xJ , eL ⟩ =
                                                             0 sinon,
d’où la formule annoncée.
   En outre, les formules précédentes entraînent que les signes de ces diverses formes sont
reliées par les équivalences suivantes :
La forme ω est positive au sens de la définition 1.2.3 ;
⇔ L’application bilinéaire (α, β) 7→ ω ∧ α ∧ Jβ est de signe σn−p ;
⇔ L’application bilinéaire bω est de signe σn−p ;
⇔ La forme bilinéaire qω est de signe σn−p (−1)p(n−p) σn = σp .
   Enfin, si f : W → V est une application linéaire, on a qf ∗ ω = qω ◦ (f, f ).
   Nous dirons qu’une (p, p)-forme symétrique est définie positive si la forme bilinéaire
symétrique σp qω est définie positive.
Lemme 1.2.7. — Soit ω ∈ Ap,p (V ) une forme symétrique de type (p, p), soit
(x1 , . . . , xn ) une base de V et soit
                                                X
                               ω = (−1)p(p−1)/2   ωI,J d′ xI ∧ d′′ xJ
                                               I,J

la décomposition de ω dans la base correspondante de Ap,p (V ). Alors, les quatre propriétés
suivantes sont équivalentes :
   a) La forme ω est positive ( resp. définie positive) ;
   b) La matrice symétrique (ωI,J ) (indexée par les parties à p éléments de {1, . . . , n})
est positive ( resp. définie positive) ;
   c) Il existe une base (αI ) de Λp V ∗ et une famille (cI ) de nombres réels positifs ou nuls
( resp. strictement positifs), indexées par les parties à p éléments de {1, . . . , n}, telles
que                                             X
                              ω = (−1)p(p−1)/2     cI αI ∧ J(αI ).
                                                     I

Démonstration. — L’équivalence des assertions (1) et (2) résulte de la discussion qui
précède le lemme et de ce qu’avec les notations introduites, la matrice (ωIJ ) est celle de
la forme bilinéaire (−1)p(p−1)/2 qω dans la base duale de la base (d′ xI )I de Λp V ∗ . Celle des
propriétés (2) et propriétés (3) découle de la diagonalisation des formes quadratiques.

Corollaire 1.2.8. — L’ensemble des formes positives dans Ap,p (V ) est le cône convexe
fermé engendré par les formes du type (−1)p(p−1)/2 α ∧ Jα, où α parcourt l’ensemble des
formes de type (p, 0).
Démonstration. — Le lemme précédent montre que les formes positives sont contenues
dans ce cône. Inversement, si α ∈ Ap,0 (V ) est une forme de type (p, 0) et β est une
(n − p, 0)-forme, la formule
     (−1)p(p−1)/2 α ∧ Jα ∧ (−1)(n−p)(n−p−1)/2 β ∧ Jβ = (−1)n(n−1)/2 (α ∧ β) ∧ J(α ∧ β)
montre que (−1)p(p−1)/2 α ∧ Jα est une forme positive, d’où l’autre inclusion.

Corollaire 1.2.9. — La condition de positivité est auto-duale : une forme α, symé-
trique de type (p, p), est positive si et seulement si α ∧ β est positive pour toute forme
positive β de type (n − p, n − p).
26 CHAPITRE 1. SUPERFORMES SUR UN ESPACE VECTORIEL RÉEL (D’APRÈS LAGERBERG)

Démonstration. — Cela résulte immédiatement du corollaire précédent.

Corollaire 1.2.10. — Les trois notions de positivité coïncident pour les formes de
```

## positive-wedges

Primary: <https://arxiv.org/pdf/1204.6277v2>. LF 1026–1040; unit SHA256 `568f9d32c940d6a28332eff16ffcf4a0fb4a1ac468e9645dab1f2e1948c7ca85`.

```text
Proposition 1.2.12 (cf. [92], Lemma 2.1). — Soit ω1 , . . . , ωs des formes sur V et
posons ω = ω1 ∧ · · · ∧ ωs .
  a) Si les ωj sont toutes fortement positives, alors ω est fortement positive.
  b) Si les ωj sont toutes positives, alors ω est positive.
  c) Si les ωj sont toutes faiblement positives et si au plus une d’entre elle n’est pas
fortement positive, alors ω est faiblement positive.

Démonstration. — Par récurrence, l’assertion b) découle de la caractérisation du cône
des formes positives et de la formule
        (−1)p(p−1)/2 α ∧ Jα ∧ (−1)q(q−1)/2 β ∧ Jβ = (−1)r(r−1)/2 (α ∧ β) ∧ J(α ∧ β),
où α, β sont des formes de type (p, 0) et (q, 0) respectivement, et r = p + q.
   Pour démontrer les assertions a) et c), il suffit par récurrence de prouver que si une
forme β est fortement positive, alors α ∧ β est de même nature que α. On peut supposer
que β est de la forme β1 ∧ Jβ1 ∧ · · · ∧ βm ∧ Jβm , où les βj sont des formes de type (1, 0).
La preuve est alors directe.
```

## current-topology

Primary: <https://arxiv.org/pdf/1204.6277v2>. LF 7654–7736; unit SHA256 `a2b017a29233edf025a43ad188ab9833bce6acb54ef9d924c5e32cc4f7e92a25`.

```text
7.1.1. — On appelle courant de bidimension (p, q) sur X une forme linéaire continue
sur l’espace Acp,q (X) des formes lisses de type (p, q) à support compact, lorsque cet
espace est muni de la topologie induite par la topologie C ∞ sur l’espace des formes lisses
à support compact définie au paragraphe 6.4.1
  On dit qu’un courant est d’ordre ⩽ r s’il est continu pour la topologie C r sur l’espace
des formes (il est alors d’ordre ⩽ s pour tout s ⩾ r).
  On notera ⟨S, α⟩ l’image de la forme α par le courant S.
  On note Dp,q (X) l’ensemble des courants de bidimension (p, q). On le munit de la
topologie de la convergence simple.
  On posera aussi D p,q = Dn−p,n−q et on dira que c’est l’espace des courants de bide-
gré (p, q).
Remarque 7.1.2. — Explicitons la condition de continuité dans la définition d’un
courant. L’espace Acp,q (X) est la limite inductive des espaces AD,K    p,q
                                                                            (X), où D parcourt
l’ensemble des jeux de cartes tropicales couvrants sur X et K l’ensemble des parties
compactes de X. Par définition, une forme linéaire sur l’espace Acp,q (X) est continue si
et seulement si sa restriction à chaque sous-espace AD,K    p,q
                                                                (X) est continue.
   Fixons une telle donnée (D, K). L’espace AD,K (X) est muni de la topologie induite de
                                                    p,q

ADp,q (X), laquelle est définie par les classes de semi-normes ∥·∥W,r associées aux domaines
compacts W d’une carte g de D et à un entier r. (Pour fixer une semi-norme dans
chaqque classe, il faut choisir une décomposition cellulaire de g(W ) et des systèmes de
coordonnées affines sur chaque cellule.)
   La continuité de S sur cet espace AD,K  p,q
                                               (X) signifie donc qu’il existe un nombre réel c,
un entier r et une famille finie (Wi ) de domaines de compacts de X, où pour tout i, Wi est
contenu dans le domaine d’une carte de D, tels que, pour toute forme lisse ω ∈ AD,K    p,q
                                                                                           (X),
on ait
                                    |⟨S, ω⟩| ⩽ c sup∥ω∥Wi ,r .
                                                 i
156                 CHAPITRE 7. COURANTS SUR UN ESPACE TROPICAL

  Comme l’espace tropical X est riche, la construction faite dans la remarque 5.2.9
fournit une description squelettique de la continuité de S : il existe un nombre réel c,
un entier r et une partie squelettique compacte Σ de X telle que, pour toute forme lisse
ω ∈ AD,K
       p,q
           (X), on ait
                                   |⟨S, ω⟩| ⩽ c∥ω|Σ ∥Σ,r ,
où ∥·∥Σ,r est une norme C r standard sur Σ.
   On peut résumer cette discussion en disant qu’un courant possède un ordre relatif à
tout jeu de cartes couvrant et toute partie compacte de X. L’ordre construit dépend de
la partie compacte considérée, comme dans le cas des distributions réelles.
   On prendra garde que l’ordre construit dépend également du jeu de cartes considéré.
On peut en effet construire un courant sur un espace tropical compact pour lequel ces
ordres ne sont pas majorés.

Lemme 7.1.3. — Supposons que X soit localement différentiellement séparé. Soit B
un jeu de cartes sur X tel que tout jeu de cartes couvrant sur X admet un raffinement
couvrant formé de cartes appartenant à B. Soit S une application linéaire de Acp,q (X)
à valeurs dans espace vectoriel topologique localement convexe E. Soit r un élément
de N ∪ {+∞}. Pour que S soit continue pour la topologie C r il faut et il suffit que
pour toute carte tropicale f définie sur un ouvert U de X appartenant à la base U et
toute fonction ρ sur U , lisse, positive et à support compact, la restriction à Afp,q (U ) de
l’application linéaire ω 7→ S(ρω) soit continue pour la topologie C r .

Démonstration. — Soit D = (fi : Ui → Ei ) un jeu de cartes couvrant sur X et soit
K une partie compacte de X ; il s’agit de prouver que la restriction de S à l’espace
AD,K
   p,p
       (X) est continue pour sa topologie C ∞ (resp. C r ). Par hypothèse, il existe un
jeu de cartes D ′ , couvrant, formé de cartes de B qui raffine le jeu D. Cela permet de
supposer que les cartes de D appartiennent à laSbase d’ouverts U . On choisit une partie
finie I de l’ensemble des indices i telle K ⊂ i∈I Int(Ui ). Soit (λi )i∈I une famille de
fonctions lisses et positives sur X tellesPque pour tout i, le support de λi soit compact
et contenu dans Int(Ui ), et telles que Pi∈I λi soit égale à 1 au voisinage P de K. Pour
toute forme ω ∈ AD,K p,q
                         , on a donc ω = ( i∈I λi )ω, de sorte que S(ω) = i∈I S(λi ω). Il
suffit ainsi de prouver que chacune des applications linéaires ω 7→ S(λi ω) est continue
sur AD,K .
   Soit i ∈ I. L’application de restriction à Ui induit une application de AD,K     p,q
                                                                                        (X)
dans Afi (Ui ) ; cette application est continue pour les topologies C . Par hypothèse,
         p,q                                                             m

l’application linéaire α 7→ S(λi α) est continue sur Afp,q  i
                                                              (Ui ), pour la topologie C ∞
(resp.. C r ). La composée de ces applications linéaires est donc continue.

7.1.4. — Soit T un courant de bidimension (p, q) ; il découle de la proposition 6.4.6
```

## compact-moment-image

Primary: <https://arxiv.org/pdf/1204.6277v2>. LF 16836–16840; unit SHA256 `d4d28c1f1c639600b5d079cd31ebe2411e60f94e19dd8c40b1544e9ef40e4125`.

```text
Théorème 12.2.4. — Soit X un espace k-analytique compact et soit f : X → T un
moment. Le sous-espace compact ftrop (X) est un polyèdre de Ttrop de dimension dim(X).
   L’assertion a été établie par Berkovich dans le cas où X est G-localement algébrisable,
cf. [11], cor. 6.2.2. Pour le cas général, on pourra se reporter à [46], §3.30, ou à [50],
th. 3.2.
```

## chart-images

Primary: <https://arxiv.org/pdf/1204.6277v2>. LF 3685–3701; unit SHA256 `27ede4644fa7140bd001a864d8f0804469ceb8bd833aa7af77d322c5105da01c`.

```text
  Dans ce paragraphe, on fixe une classe de coefficients G .
3.3.1. — Soit X un espace G-tropical.
    Les cartes G-tropicales sur les domaines de X forment une catégorie essentiellement
petite, un morphisme d’une carte G-tropicale (f : X → E, P ) dans une autre (f ′ : X →
E ′ , P ′ ) étant une application affine q : E → E ′ tel que f ′ = q ◦ f et q(P ) ⊂ P ′ .
    Cette catégorie a un objet final pour lequel E = {0} et P est un point. Elle est
filtrante : si (f : X → E, P ) et (f ′ : X → E ′ , P ′ ) sont deux cartes G-tropicales sur X,
alors (f × f ′ : X → E × E ′ , P × P ′ ) est une carte G-tropicale sur X qui domine les deux
cartes G-tropicales données.

Remarque 3.3.2. — Soit X un espace G-tropical compact et soit (f : X → E, P ) une
G-carte tropicale sur X.
  a) L’ensemble f (X) est un sous-espace paralinéaire compact de E contenu dans P
(théorème. 12.2.4) et la carte donnée se factorise par (f : X → E, f (X)). On dira parfois,
par abus, que f est une carte G-tropicale sur X.
  b) Pour toute décomposition cellulaire (Pi ) de f (X), la famille (f −1 (Pi )) est un G-
recouvrement fini de X par des domaines compacts dont l’image par f est une cellule.
```

## geometric-positive-wedges

Primary: <https://arxiv.org/pdf/1204.6277v2>. LF 4074–4081; unit SHA256 `af2ae2b53d2b5093ec220554a5e109e67790222e7b7ce1255d4d6b93d0107534`.

```text
Proposition 3.5.5. — Soit X un espace G-tropical, soit ω1 , . . . , ωr des G-formes
sur X, et soit ω = ω1 ∧ · · · ∧ ωr .
  a) Si les ωj sont fortement positives, alors ω est fortement positive.
  b) Si les ωj sont positives, alors ω est positive.
  c) Si les ωj sont faiblement positives et si au plus une d’entre elles n’est pas fortement
positive, alors ω est faiblement positive.

Démonstration. — Cela découle de la proposition 1.10.3.
```

## face-positive-wedges

Primary: <https://arxiv.org/pdf/1204.6277v2>. LF 2685–2699; unit SHA256 `755005874cbbd0719c56e04d0023943714d304b960d55d46188c1267bd2c9571`.

```text
Proposition 1.10.3. — Soit P un sous-espace paralinéaire d’un espace affine V et soit
ω1 , . . . , ωs des formes sur P ; posons ω = ω1 ∧ · · · ∧ ωr .
   a) Si les ωj sont toutes fortement positives, alors ω est fortement positive.
   b) Si les ωj sont toutes positives, alors ω est positive.
   c) Si les ωj sont toutes faiblement positives et si au plus une d’entre elle n’est pas
fortement positive, alors ω est faiblement positive.
Démonstration. — Par hypothèse, les formes ωj sont restrictions de formes au voisi-
nage,de P . L’assertion se déduit donc cellule par cellule de la proposition 1.2.12.

1.10.4. — Soit P un sous-espace paralinéaire d’un espace affine V et soit n = dim(P ).
Les notions de formes faiblement positives, positives et fortement positives coïncident en
bidegrés (0, 0) et (n, n) ; pour les formes symétriques, elles coïncident en bidegrés (1, 1)
et (n − 1, n − 1).
   Cela se démontre par inspection cellule par cellule.
Définition 1.10.5. — Soit V un espace affine de dimension finie et soit P une partie
```

## face-positivity

Primary: <https://arxiv.org/pdf/1204.6277v2>. LF 2634–2651; unit SHA256 `3aaef6a90762b10edb0574cb40377ab1f036d24da0e2db4d0552ece7f5e7f481`.

```text

Définition 1.10.1. — Soit V un espace affine de dimension finie sur R et soit P
un sous-espace paralinéaire de V . Soit ω une forme de type (p, p) sur P . On dit que ω
est positive ( resp. faiblement positive, resp. fortement positive) si pour toute cellule C
                                                                   −→
contenue dans P et tout point x ∈ C, l’élément ω|C (x) de Ap,p (⟨C⟩) est une (p, p)-forme
                                                                                       −→
positive ( resp. faiblement positive, resp. fortement positive) sur l’espace vectoriel ⟨C⟩ au
sens de la définition 1.2.3.
   Compte tenu du lemme 1.2.11 et de la compatibilité des morphismes d’évaluation à
la restriction à une sous-cellule, il suffit de vérifier cette condition pour toute cellule
maximale d’une décomposition cellulaire de P .
   En particulier, ce sont des notions G-locales : soit α ∈ FPp,p (P ) et soit (Pi ) un G-
recouvrement de P , pour que α soit positive, il faut et il suffit que α|Pi soit positive pour
tout i. Comme P est paracompact (c’est un sous-espace de Rn !), l’assertion se déduit
de la proposition 2.2.13 qui affirme l’existence d’une décomposition cellulaire adaptée
au G-recouvrement (Pi ). Les cas des formes faiblement positives et fortement positives
sont analogues.
```

## mixed-symmetry-diagnostic

Primary: <https://arxiv.org/pdf/1204.6277v2>. LF 10470–10481; unit SHA256 `f925445e54e0432f008a517798735ca2c5bf78eda6f665bf0f4ffeade3b22da3`.

```text
Proposition 8.7.4. — Soit T un courant positif fermé. Soit u1 , . . . , um des fonctions
psh et soit σ une permutation de {1, . . . , m} ; on a
d′ d′′ (u1 ) ∧ d′ d′′ (u2 ) ∧ · · · ∧ d′ d′′ (um ) ∧ T = d′ d′′ (uσ(1) ) ∧ d′ d′′ (uσ(2) ) ∧ · · · ∧ d′ d′′ (uσ(m) ) ∧ T.
Démonstration. — Soit v une fonction psh sur X. Soit P le sous-faisceau de CPshX
formé des fonctions psh u telles que d′ d′′ (u d′ d′′ (vT )) = d′ d′′ (v d′ d′′ (uT )). Si u est lisse,
on a
      d′ d′′ (u d′ d′′ (vT )) = d′ d′′ (u) ∧ d′ d′′ (vT ) = d′ d′′ (vT ∧ d′ d′′ (u)) = d′ d′′ (v d′ d′′ (uT )),
de sorte que ce faisceau P contient les fonctions lisses. Il est stable par limites uniformes.
Par suite, il contient le faisceau des fonctions psh.
  Cela entraîne l’assertion voulue lorsque m = 2.
  Le cas où σ est la transposition échangeant deux entiers successifs en découle immé-
diatement. Le cas général s’en déduit car σ est composée de telles transpositions.
```

## torus-coordinates

Primary: <https://arxiv.org/pdf/1204.6277v2>. LF 16493–16575; unit SHA256 `f45158e6456b76c10f89688528b986df3a51a16988d2d6d6ce157bbf925e4667`.

```text
12.1.1. Convention. — Dans la suite de ce travail, nous travaillerons très régulière-
ment avec les analytifiés An,an et Gn,an
                                      m   des k-schémas An et Gnm , et seulement excep-
tionnellement avec ces schémas eux-mêmes. Aussi écrirons-nous désormais, afin d’alléger
l’écriture, An et Gnm au lieu de An,an et Gn,an
                                           m . Il sera donc considéré par défaut que A
                                                                                        n

et Gnm sont des espaces analytiques ; si nous avons besoin de travailler par endroit avec
les schémas correspondants, nous le préciserons explicitement.
12.1.2. — Dans ce travail, le groupe multiplicatif et ses puissances jouent un rôle
fondamental. Rappelons que l’anneau des fonctions algébriques sur Gnm est l’anneau
A = k[T1±1 , . . . , Tn±1 ] des polynômes de Laurent à coefficients dans k en des indétermi-
nées T1 , . . . , Tn ; l’espace analytique Gnm est l’ensemble des semi-normes multiplicatives
sur cet anneau qui étendent la valeur absolue de k. L’espace Gnm est un ouvert de Zariski
dense de An : c’est le lieu des points en lesquels aucune fonction coordonnée ne s’annule.
                                                                 n
Pour tout polyrayon r = (r1 , . . . , rn ) le point ηr de de A     (défini à l’exemple 11.1.12)
                     n
                                                                    aI T I 7→ max|aI |rI sur l’an-
                                                                P
appartient à Gm . Il correspond à la norme multiplicative
neau des polynômes de Laurent. Si le corps k a besoin d’être rappelé nous écrirons ηk,r
au lieu de ηr .
   Pour éviter le recours à un choix explicite de coordonnées, nous adopterons la conven-
tion suivante : nous appellerons tore (de dimension n) tout groupe analytique isomorphe
à une puissance Gnm du groupe multiplicatif ; nos tores sont donc implicitement supposés
déployés.
12.1.3. — Rappelons que toute fonction analytique inversible sur Gnm est un monôme,
c’est-à-dire de la forme aT1m1 . . . Tnmn , où a ∈ k ∗ et (m1 , . . . , mn ) ∈ Zn est un vecteur
appelé exposant. (En dimension 1, cet énoncé est le lemme 9.7.1/1 de [20], le cas général
en découle par récurrence.) C’est en particulier une fonction algébrique.
   Le morphisme Gnm → Gm induit par une telle fonction est un homomorphisme de
groupes analytiques si et seulement si a = 1.
330          CHAPITRE 12. PARTIES SQUELETTIQUES D’UN ESPACE ANALYTIQUE

  Soit T un tore. L’ensemble X(T ) des caractères de T , c’est-à-dire des morphismes de
groupes analytiques de T vers Gm , est un groupe abélien.
  On déduit de ce qui précède que tout isomorphisme de T avec Gnm induit un iso-
morphisme de X(T ) avec Zn ; on en déduit aussi que si T et T ′ sont deux tores, tout
morphisme d’espaces k-analytiques de T vers T ′ est affine, i.e. composé d’un morphisme
de groupes analytiques et d’une translation ; c’est donc un morphisme de groupes si et
seulement si il envoie l’origine de T sur l’origine de T ′ . Pour cette raison, lorsque nous
évoquerons un morphisme entre tores qui n’est pas nécessairement un morphisme de
groupes analytiques, nous le qualifierons de morphisme affine.
12.1.4. Tropicalisations. — On considère le groupe abélien R×            + comme un R-espace
vectoriel, via l’exponentiation. Par ailleurs, le choix d’une base de logarithmes permet de
l’identifier à l’espace R. On fixe une fois pour toutes un tel isomorphisme log : R×       + → R.
Dans ce texte, il n’y a pas d’intérêt particulier à choisir le logarithme néperien ; en
particulier, nous n’aurons jamais à dériver cet isomorphisme, vu comme fonction d’une
variable réelle. L’utilisation de cet isomorphisme log présentera pour nous deux intérêts :
elle nous permettra d’utiliser la géométrie paralinéaire sous sa forme standard, plutôt
que sa variante multiplicative ; et elle donnera lieu à un formalisme apparenté à celui de
la géométrie complexe, dans lequel les logarithmes de fonctions holomorphes inversibles
jouent un rôle majeur.
   Soit T un tore. Nous noterons Ttrop le R-espace vectoriel Hom(X(T ), R×      + ), que l’on peut
identifier à (R× + )n
                      une fois choisie une trivialisation de T , ou à Rn
                                                                         via l’isomorphisme    log
choisi. L’espace vectoriel Ttrop est appelé tropicalisation du tore T .
   Étant donné un point t de T , l’application qui applique un caractère φ ∈ X(T ) sur
l’élément |φ(t)| est un élément de Ttrop noté trop(t). L’application trop : T → Ttrop ainsi
définie est continue.
   La formation de Ttrop est fonctorielle : tout morphisme affine f : T → T ′ entre tores
                                                   ′
induit une application affine ftrop : Ttrop → Ttrop    telle que le diagramme

                                                   f
                                          T   ←         → T′
                                          ←




                                                          ←→
                                          →




                                                  ftrop   ′
                                         Ttrop   ←     → Ttrop

```

## top-measures

Primary: <https://arxiv.org/pdf/1204.6277v2>. LF 6733–6808; unit SHA256 `c727f9481e602256f7ccc91d7e23516abbf75077de67409d2e46c9956100005f`.

```text
5.8.1. — Soit ω ∈ FXn,n  G
                           (X), soit Σ une partie squelettique fermée de X qui supporte
fortement ω. Par la construction du §4.5.5, en accouplant la restriction ω|Σ à Σ de la
forme ω et le n-calibrage µΣ de Σ, on obtient une forme-volume n-dimensionnelle ω̃Σ
sur Σ, et donc une forme-volume n-dimensionnelle sur X au sens du §5.6. D’après la
proposition 4.5.8 et la définition d’un support fort, cette forme-volume sur X ne dépend
pas du choix de Σ ; on la note ω   e . Elle est positive si ω est une forme positive, car le
calibrage canonique est positif (lemme 14.3.4).
Lemme 5.8.2. — Soit ω ∈ FXn,n     G
                                    (X). On suppose qu’il existe une partie squelettique
fermée de X qui supporte fortement ω. Pour tout domaine analytique Y de X, il existe
une partie squelettique fermée de Y qui supporte fortement ω|Y et l’on a l’égalité ω|
                                                                                   g Y =
ω̃|Y de formes-volume n-dimensionnelles sur Y .
Démonstration. — Soit Σ une partie squelettique fermée de X qui supporte fortement ω.
Alors, T = Σ ∩ Y est une partie squelettique fermée de Y qui supporte fortement ω|Y .
De plus, on a
      ω|Y = ⟨(ω|Y )|T , µT ⟩      par définition de ω|
      g                                             g Y

            = ⟨ω|T , µT ⟩                  d’après (3.3.14)
            = ⟨(ω|Σ )|T , (µΣ )|T ⟩        d’après (3.3.14) et la définition d’un calibrage
            = ⟨ω|Σ , µΣ ⟩|T = ω
                              e |Y
parce que l’accouplement entre (n, n)-formes et calibrages est un morphisme de faisceaux
sur le site XG . Le lemme est ainsi démontré.

Proposition 5.8.3. — Il existe un unique morphisme de faisceaux FXn,n            G
                                                                                    → VXnG
sur XG , noté ω 7→ ω e , qui prolonge l’application définie en (5.8.1) lorsque ω possède
un support fort. Ce morphisme est FX0,0G -linéaire. Si ω est une G-forme positive, la
forme-volume ωe est positive. Si ω est à coefficients dans une classe G , il en va de même
de la forme-volume ωe.
Démonstration. — Compte tenu du lemme 5.8.2, la première assertion résulte de ce que
toute forme sur un domaine paracompact possède un support fort, et que tout domaine
est G-recouvert par ses domaines paracompacts. Les autres propriétés découlent alors
de la construction.

5.8.4. — Explicitons cette construction lorsque ω est tropicale. Soit f : X → E une
carte G-tropicale et soit α une (n, n)-forme sur un sous-espace paralinéaire de E conte-
                                         (n)
nant f (X) telle que ω = f ∗ α. Alors, Σf est un support fort de ω (lemme 5.3.4) et on
                                         (n)
a l’égalité de formes-volume sur Σf            :
                                                ∗
(5.8.4.1)                                ω̃ = ⟨ftrop α, µΣ(n) ⟩.
                                                            f

Si, de plus, la carte G-tropicale f est agréable, la proposition 4.5.8 entraîne alors que
(5.8.4.2)                       ftrop,∗ (ω̃) = ⟨α, f∗ µΣ(n) ⟩ = ⟨α, µΠf ⟩.
                                                        f
                                   § 5.9. MESURES DE BORD                                  137

 5.8.5. — Soit ω une forme de type (n, n) sur XG à coefficients tropicalement boréliens.
 Nous venons de lui associer une forme-volume n-dimensionnelle ω̃. Nous noterons alors
 ωBor la mesure de Borel sur X associée à ω̃ par la construction du §5.7.1.
   Nous dirons que ω est localement intégrable si cette mesure est localement finie, et
 que ω est intégrable si cette mesure est finie. Lorsque ω est localement intégrable, nous
 noterons ωRad la mesure de Radon associée à ω̃ ; on a |ωRad | = ωBor . Lorsque ω est une
 G-forme positive, la mesure ωRad est positive.         R           R
   Si f est une fonction borélienne sur X, on notera X f |ω| et X f ω les intégrales de f
Rcontre les mesures ωBor et ωRad lorsqu’elles existent. Cela définit en particulier l’intégrale
  X
    ω pour toute G-forme de type (n, n) à support compact qui est localement intégrable
(par exemple lisse).
   Les G-formes localement intégrables constituent un sous-espace vectoriel de F n,n (XG )
contenant les G-formes lisses. Les G-formes intégrables en sont un sous-espace vectoriel
qui contient les G-formes lisses à support compact.
5.8.6. — Soit u une fonction localement intégrable sur X et soit ω une G-forme lisse
de type (n, n) sur X. Alors, u est localement intégrable par rapport à la mesure ωBor ,
de sorte que uωRad est une mesure de Radon sur X.
   L’application (u, ω) 7→ uωRad est bilinéaire ; elle induit une application linéaire de
Lloc
   1
     (XG ) ⊗ A n,n (XG ) dans l’ensemble des mesures de Radon sur X. Cette application
se factorise par L1loc (XG ) ⊗ A n,n (XG ). On la notera bien sûr α 7→ αRad .
```

END MATHEMATICAL DATA


BEGIN MATHEMATICAL DATA: Original source versions and exact coordinates
{
  "source": {
    "path": "sources/cld-v2-full.txt",
    "read_only_origin": "/workspace/research/root-checks/public-P21.3-round-95-final-reader/sources/cld-full.txt",
    "sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085",
    "version": "arXiv:1204.6277v2, 25 July 2025",
    "whole_source_read": false
  },
  "units": [
    {
      "id": "ordinary-domain",
      "path": "sources/cld-ordinary-domain.txt",
      "url": "https://arxiv.org/pdf/1204.6277v2",
      "version": "25 July 2025",
      "inclusive_one_based_LF": [
        14983,
        15012
      ],
      "sha256": "6efe2fa15d3425138409717a7512d91909e0b03be4f3c3e56e267d4bcdfefabd",
      "source_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085"
    },
    {
      "id": "analytic-calculus",
      "path": "sources/cld-analytic-calculus.txt",
      "url": "https://arxiv.org/pdf/1204.6277v2",
      "version": "25 July 2025",
      "inclusive_one_based_LF": [
        22105,
        22126
      ],
      "sha256": "960861bd1391008caa52be28ee8a788b6bdc3df269d765f603121a8bab0af320",
      "source_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085"
    },
    {
      "id": "generic-lengths",
      "path": "sources/cld-generic-lengths.txt",
      "url": "https://arxiv.org/pdf/1204.6277v2",
      "version": "25 July 2025",
      "inclusive_one_based_LF": [
        23434,
        23459
      ],
      "sha256": "52dbd2e0b2cf6d2c6220cb31fdf4683247d2c282b0b8055f6a2bf8735129d742",
      "source_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085"
    },
    {
      "id": "generated-psh",
      "path": "sources/cld-generated-psh.txt",
      "url": "https://arxiv.org/pdf/1204.6277v2",
      "version": "25 July 2025",
      "inclusive_one_based_LF": [
        9729,
        9781
      ],
      "sha256": "fa2e29bcb98fd26a55598c0dc4c67b162d19d4b1780b39f2a49bdfc7e4373830",
      "source_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085"
    },
    {
      "id": "generated-cpsh-diagnostic",
      "path": "sources/cld-generated-cpsh-diagnostic.txt",
      "url": "https://arxiv.org/pdf/1204.6277v2",
      "version": "25 July 2025",
      "inclusive_one_based_LF": [
        9797,
        9863
      ],
      "sha256": "5ef01dd5ed01e2349c223afadbb34c535cb304dce255f10115f25edccd4899da",
      "source_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085"
    },
    {
      "id": "positive-decomposition",
      "path": "sources/cld-positive-decomposition.txt",
      "url": "https://arxiv.org/pdf/1204.6277v2",
      "version": "25 July 2025",
      "inclusive_one_based_LF": [
        7359,
        7381
      ],
      "sha256": "7d7b6d6687db0b922b6e69a1011a9dcb0a2d112c41d65200901f1efd7275db83",
      "source_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085"
    },
    {
      "id": "middle-positivity",
      "path": "sources/cld-middle-positivity.txt",
      "url": "https://arxiv.org/pdf/1204.6277v2",
      "version": "25 July 2025",
      "inclusive_one_based_LF": [
        7918,
        7981
      ],
      "sha256": "7e8a9c9f610a102901ed491e3e572f9b96528cf24e5f8733f1d4f3d419801332",
      "source_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085"
    },
    {
      "id": "positive-scalar-measures",
      "path": "sources/cld-positive-scalar-measures.txt",
      "url": "https://arxiv.org/pdf/1204.6277v2",
      "version": "25 July 2025",
      "inclusive_one_based_LF": [
        7983,
        8011
      ],
      "sha256": "089af75e6237f117a1ff411156580da33c01951d926d14ecc613c1bf86f77060",
      "source_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085"
    },
    {
      "id": "ordinary-product",
      "path": "sources/cld-ordinary-product.txt",
      "url": "https://arxiv.org/pdf/1204.6277v2",
      "version": "25 July 2025",
      "inclusive_one_based_LF": [
        8054,
        8076
      ],
      "sha256": "f647601926c2311a3319b181f2567f487f9a88ce4870332c75ecc8bb5f3156d4",
      "source_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085"
    },
    {
      "id": "current-sheaf",
      "path": "sources/cld-current-sheaf.txt",
      "url": "https://arxiv.org/pdf/1204.6277v2",
      "version": "25 July 2025",
      "inclusive_one_based_LF": [
        7756,
        7818
      ],
      "sha256": "0d1a24130ba9c326713dcafecb5aa9a83678fb264cbd51fe4d1005de11869d48",
      "source_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085"
    },
    {
      "id": "current-differentials",
      "path": "sources/cld-current-differentials.txt",
      "url": "https://arxiv.org/pdf/1204.6277v2",
      "version": "25 July 2025",
      "inclusive_one_based_LF": [
        9309,
        9381
      ],
      "sha256": "a396b6b027f3375f6aa7b3e89bac0319a21ad2c96f44971acb018cec52648801",
      "source_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085"
    },
    {
      "id": "cutoffs-density",
      "path": "sources/cld-cutoffs-density.txt",
      "url": "https://arxiv.org/pdf/1204.6277v2",
      "version": "25 July 2025",
      "inclusive_one_based_LF": [
        21619,
        21696
      ],
      "sha256": "aba28489aa7c1e770af13b87e11c77fbca731f95eb5bc41afb637b378d66ed45",
      "source_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085"
    },
    {
      "id": "form-leibniz",
      "path": "sources/cld-form-leibniz.txt",
      "url": "https://arxiv.org/pdf/1204.6277v2",
      "version": "25 July 2025",
      "inclusive_one_based_LF": [
        3769,
        3803
      ],
      "sha256": "172d214bed8f4a1ffbfd19dcf120345ce08abbc69c0b70160a6af23832c8eff0",
      "source_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085"
    },
    {
      "id": "weak-multiplier",
      "path": "sources/cld-weak-multiplier.txt",
      "url": "https://arxiv.org/pdf/1204.6277v2",
      "version": "25 July 2025",
      "inclusive_one_based_LF": [
        10257,
        10281
      ],
      "sha256": "0eec1c45dfec34af7fb8e231160cc24fd3ef9b8f6dc1185fb8eedd1905483114",
      "source_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085"
    },
    {
      "id": "smooth-multiplier",
      "path": "sources/cld-smooth-multiplier.txt",
      "url": "https://arxiv.org/pdf/1204.6277v2",
      "version": "25 July 2025",
      "inclusive_one_based_LF": [
        10283,
        10326
      ],
      "sha256": "364ca08767840b4b45382d42e9e0a5b18b7f7c1b2daf978615413b9a1b5cc985",
      "source_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085"
    },
    {
      "id": "bt-definition-and-closures",
      "path": "sources/cld-bt-definition-and-closures.txt",
      "url": "https://arxiv.org/pdf/1204.6277v2",
      "version": "25 July 2025",
      "inclusive_one_based_LF": [
        10347,
        10408
      ],
      "sha256": "d6ddcecc24ddb7e5d63f49f8c320e5dd419e2d24b2846e9fbd6025c0f60f1a21",
      "source_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085"
    },
    {
      "id": "middle-matrix",
      "path": "sources/cld-middle-matrix.txt",
      "url": "https://arxiv.org/pdf/1204.6277v2",
      "version": "25 July 2025",
      "inclusive_one_based_LF": [
        885,
        975
      ],
      "sha256": "7ac6fc20a19b2e92f75e58b56564ddba33b24b1dd86814f5a3068e7978c50da1",
      "source_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085"
    },
    {
      "id": "positive-wedges",
      "path": "sources/cld-positive-wedges.txt",
      "url": "https://arxiv.org/pdf/1204.6277v2",
      "version": "25 July 2025",
      "inclusive_one_based_LF": [
        1026,
        1040
      ],
      "sha256": "568f9d32c940d6a28332eff16ffcf4a0fb4a1ac468e9645dab1f2e1948c7ca85",
      "source_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085"
    },
    {
      "id": "current-topology",
      "path": "sources/cld-current-topology.txt",
      "url": "https://arxiv.org/pdf/1204.6277v2",
      "version": "25 July 2025",
      "inclusive_one_based_LF": [
        7654,
        7736
      ],
      "sha256": "a2b017a29233edf025a43ad188ab9833bce6acb54ef9d924c5e32cc4f7e92a25",
      "source_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085"
    },
    {
      "id": "compact-moment-image",
      "path": "sources/cld-compact-moment-image.txt",
      "url": "https://arxiv.org/pdf/1204.6277v2",
      "version": "25 July 2025",
      "inclusive_one_based_LF": [
        16836,
        16840
      ],
      "sha256": "d4d28c1f1c639600b5d079cd31ebe2411e60f94e19dd8c40b1544e9ef40e4125",
      "source_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085"
    },
    {
      "id": "chart-images",
      "path": "sources/cld-chart-images.txt",
      "url": "https://arxiv.org/pdf/1204.6277v2",
      "version": "25 July 2025",
      "inclusive_one_based_LF": [
        3685,
        3701
      ],
      "sha256": "27ede4644fa7140bd001a864d8f0804469ceb8bd833aa7af77d322c5105da01c",
      "source_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085"
    },
    {
      "id": "geometric-positive-wedges",
      "path": "sources/cld-geometric-positive-wedges.txt",
      "url": "https://arxiv.org/pdf/1204.6277v2",
      "version": "25 July 2025",
      "inclusive_one_based_LF": [
        4074,
        4081
      ],
      "sha256": "af2ae2b53d2b5093ec220554a5e109e67790222e7b7ce1255d4d6b93d0107534",
      "source_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085"
    },
    {
      "id": "face-positive-wedges",
      "path": "sources/cld-face-positive-wedges.txt",
      "url": "https://arxiv.org/pdf/1204.6277v2",
      "version": "25 July 2025",
      "inclusive_one_based_LF": [
        2685,
        2699
      ],
      "sha256": "755005874cbbd0719c56e04d0023943714d304b960d55d46188c1267bd2c9571",
      "source_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085"
    },
    {
      "id": "face-positivity",
      "path": "sources/cld-face-positivity.txt",
      "url": "https://arxiv.org/pdf/1204.6277v2",
      "version": "25 July 2025",
      "inclusive_one_based_LF": [
        2634,
        2651
      ],
      "sha256": "3aaef6a90762b10edb0574cb40377ab1f036d24da0e2db4d0552ece7f5e7f481",
      "source_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085"
    },
    {
      "id": "mixed-symmetry-diagnostic",
      "path": "sources/cld-mixed-symmetry-diagnostic.txt",
      "url": "https://arxiv.org/pdf/1204.6277v2",
      "version": "25 July 2025",
      "inclusive_one_based_LF": [
        10470,
        10481
      ],
      "sha256": "f925445e54e0432f008a517798735ca2c5bf78eda6f665bf0f4ffeade3b22da3",
      "source_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085"
    },
    {
      "id": "torus-coordinates",
      "path": "sources/cld-torus-coordinates.txt",
      "url": "https://arxiv.org/pdf/1204.6277v2",
      "version": "25 July 2025",
      "inclusive_one_based_LF": [
        16493,
        16575
      ],
      "sha256": "f45158e6456b76c10f89688528b986df3a51a16988d2d6d6ce157bbf925e4667",
      "source_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085"
    },
    {
      "id": "top-measures",
      "path": "sources/cld-top-measures.txt",
      "url": "https://arxiv.org/pdf/1204.6277v2",
      "version": "25 July 2025",
      "inclusive_one_based_LF": [
        6733,
        6808
      ],
      "sha256": "c727f9481e602256f7ccc91d7e23516abbf75077de67409d2e46c9956100005f",
      "source_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085"
    }
  ],
  "bound_primary_units": [
    {
      "path": "sources/cld-weak-multiplier-bound.txt",
      "read_only_origin": "/workspace/research/campaigns/round-100/P21.3-original-mixed-symmetry-and-arbitrary-current-research/CLD-weak-multiplier-LF10257-10281.txt",
      "sha256": "0448ea1b480496814c9d81b4a5443f7d6efbb05b91582305b117704008184860",
      "inclusive_one_based_LF": [
        10257,
        10281
      ],
      "normalization_difference": "The ordinary LF slice adds exactly one trailing newline."
    }
  ]
}

END MATHEMATICAL DATA


BEGIN MATHEMATICAL DATA: Complete canonical new100 notes, not grants
{
  "kind": "notes",
  "notes": [
    {
      "id": "n1",
      "summary": "Reconstructed middle-positive Borel multiplication and positivity at every generated-Psh ordinal stage: locally bounded u gives positive doubly closed D(uT). This proves separate-product positivity, not P21.3 independence.",
      "detailedSummary": "The reconstruction uses compact middle-positive test decomposition, intrinsic signed coefficient Radon measures, and exterior-power matrix domination on finite moment presentations. A locally bounded final generated-Psh section bounds all decreasing predecessors below; upper semicontinuity supplies compact upper bounds. Fixed-measure convergence handles successors, ordinary locality handles limit ranks, and cardinal stabilization exhausts generated Psh. All original fields, degrees, singularities and generic multiplicities are retained. Reverse CPsh recognition and continuous predecessors are unnecessary. An arbitrary equal-curvature difference has not been given a two-sign generating construction.",
      "text": "Unverified research proof. Let K be any complete non-Archimedean field, including trivial valuation, and X good, separated, strict, boundaryless and pure of dimension n>=2. On every ordinary open W, let T be an ordinary middle-positive (p,p)-current, 0<=p<=n-1, satisfying d'T=d''T=0. Write D=d'd''. The proved statement is that every locally bounded real generated-Psh u has an ordinary Borel product uT and D(uT) is middle-positive and doubly closed.\n\nThe exact external ordinary-calculus inputs are CLD arXiv:1204.6277v2, 25 July 2025: compact neighbourhoods and ordinary analytic domains (11.1.7); calibrated analytic-domain compatibility (15.7.1–2); good Hausdorff implies local holomorphic/differential separation, with compact smooth cutoffs, localization and scalar density (15.2.2–9); compact symmetric tests are differences of compact middle-positive tests in this almost-good scope (6.5.2); positive scalar currents and positive complementary forms give unique Radon coefficient measures (7.2.8, 7.2.11); middle positivity is the signed positive-semidefinite matrix condition on exterior powers and is checked on tangent faces (1.2.6–7, 1.10.1); fixed-support chart topology is cellwise (7.1.1–3); compact moment images are polyhedral (only that part of 12.2.4); ordinary currents form a sheaf and have weakly continuous differentials with square-zero, anticommutation and duality identities (7.1.6–7, 7.7.1–5); and D(sT)=Ds wedge T for smooth s and doubly closed T (8.5.3–4). Positive smooth factors preserve middle positivity (7.2.7(b)). The original hypotheses provide this scope on every ordinary open. Neither the erroneous printed moment-dimension clause nor reverse Psh/CPsh recognition is used.\n\nFor a symmetric complementary compact test beta=eta1-eta2, define mu_beta=mu_eta1-mu_eta2 using its middle-positive decomposition. Competing decompositions agree against smooth compact scalars, hence against continuous compact scalars by density, so they define the same signed Radon measure. This establishes linearity. Density within the complement of supp beta shows the signed measure is supported in supp beta. Define <bT,beta>=integral b dmu_beta for locally bounded Borel b, using the symmetric projection for arbitrary tests.\n\nTo prove that this functional is an ordinary order-zero current, localize to rho f*a in one moment chart, with rho nonnegative compact smooth. Choose a compact analytic neighbourhood C of supp rho inside the chart, using a finite union of affinoids if needed. Its moment image has finitely many tangent faces. For complementary degree q=n-p, fix Euclidean Theta=sum dx_i' wedge dx_i''. Theta^q is positive definite on each qth exterior tangent space; both restrictions vanish on faces of dimension below q. Thus one constant c for this finite presentation gives c||a||_(P,0)Theta^q +/- a>=0 for every symmetric presented a. Positive coefficient measures imply |mu_(rho f*a)|<=c||a||_(P,0)mu_(rho f*Theta^q), hence\n|<bT,rho f*a>|<=c||b||_(supp rho)||a||_(P,0)<T,rho f*Theta^q>.\nFor q=0 use the scalar bound. Chart topology and finite localization prove order-zero continuity without strongly-positive spanning. Coefficient-measure uniqueness also proves ordinary restriction compatibility and agreement with smooth multiplication.\n\nIf b_j decreases to b with common compact bounds, apply the fixed positive coefficient measures. For g_j=b_j-b decreasing to zero, 0<=g_j<=M, the sets E_j={g_j>=epsilon} decrease to the empty set. Finiteness gives mu(E_j)->0, while integral g_j<=epsilon mu(C)+M mu(E_j). Taking j to infinity and then epsilon to zero proves b_jT->bT weakly. Locally uniform nets against fixed T converge by the separate bound ||b_a-b||_C<T,eta1+eta2>. No bounded-pointwise-convergence assertion for arbitrary nets is made.\n\nReconstruct generated Psh from Definition 8.1.1 and Lemma 8.1.4: smooth positive-Hessian generators at rank zero, ordinary-local decreasing sequential limits at successors, and ordinary-local earlier-rank membership at limits. These are increasing sheaves. Upper semicontinuity follows at successors from {inf_j u_j<a}=union_j{u_j<a}, and is local at limits; finite sections are Borel. All open/section pairs form a set, so an equal-successor stage exists by cardinality. That stationary sheaf contains the generators and is decreasing-sequentially closed, hence is the minimal Psh sheaf. No extraneous integrability condition is inserted.\n\nInduct simultaneously on every open and rank for locally bounded real final sections. Smooth u gives D(uT)=Du wedge T>=0. At a successor u_j decreases to u locally. Each predecessor is finite because u_j>=u and the stages allow no +infinity. The final u bounds every predecessor locally below; finite upper-semicontinuous u_j are locally bounded above. On each compact C there are fixed a,b with a<=u<=u_j<=u1<=b. Every predecessor therefore qualifies for induction even if discontinuous. Fixed-measure convergence gives D(u_jT)->D(uT), and positivity and symmetry pass to the limit. At limit ranks use earlier membership locally and the ordinary current sheaf. Stabilization proves all stages. Differential identities give both closedness equations. Scalar tests at p=n-1 and degree (n-1,n-1) tests at p=0 are included. The canonical calibration and generic lengths have not been changed.\n\nOrdered differentiation by m locally bounded generated potentials is consequently positive and doubly closed for m<=n-p. If h and -h themselves are locally bounded generated Psh, D(hT) and its negative are positive; positive-test decomposition and symmetry force zero. The original assumptions on h=U-V have not supplied these two memberships.\n\nComplete arguments and exact primary premises are in P21.3-argument.md and P21.3-paper.tex/PDF. Literal evidence, LF intervals and hashes are in P21.3-primary-evidence.md, premises.json and source-manifest.json. The frozen CLD text hash is 64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085; the full text was not read in full. Rerun bash reproduce.sh. Integrity checks and compilation do not establish mathematical acceptance.\n\nArtifacts: /workspace/research/campaigns/round-100/P21.3-original-mixed-symmetry-and-arbitrary-current-research/artifacts/codex-RcZhes",
      "support": []
    },
    {
      "id": "n2",
      "summary": "Mixed symmetry holds in the reconstructed argument for arbitrary original T with one continuous generated-Psh factor and one locally bounded generated-Psh factor. It does not settle signed curvature relations.",
      "detailedSummary": "For p<=n-2, v continuous generated Psh and u locally bounded real generated Psh, D(uD(vT))=D(vD(uT)). The left successor limit uses fixed positive D(vT) coefficient measures; the right uses positive D(u_jT) and continuity of v. All sheafified ranks are treated. Adjacent swaps give permutation independence with at most one discontinuous factor. The signed continuous-difference identity still contains D(hT), which canonical D[h]=0 does not identify.",
      "text": "Unverified research proof using n1. Retain all original ambient hypotheses, ordinary middle positivity and canonical multiplicities. Suppose 0<=p<=n-2, u is locally bounded real generated Psh, and v is finite continuous generated Psh. Both inner differentiated currents are positive doubly closed by n1, so the products in D(uD(vT))=D(vD(uT)) are actual ordinary currents.\n\nFirst reconstruct continuous multiplication on varying currents. If positive S_a->S weakly, positivity and symmetry pass on fixed tests. For compact symmetric beta=eta1-eta2, the masses <S_a,eta1+eta2> converge, hence are eventually bounded even for a net. Approximate continuous v uniformly on the compact union by smooth g, using a cutoff and the scalar density stated in n1. The error is at most epsilon<S_a,eta1+eta2>+|<S_a-S,g beta>|+epsilon<S,eta1+eta2>. First take the current limit for fixed g, then epsilon to zero. Thus vS_a->vS. Locally uniform varying continuous v_a also works by the additional bound ||v_a-v||_C<S_a,eta1+eta2>. This reconstructs CLD v2 Lemma 8.5.1 and its fixed-function net variant. It assumes neither a bound on all net indices nor a discontinuous multiplier.\n\nA smooth doubly closed even-degree form gamma commutes with current differentiation by ordinary Leibniz duality. Also b(T wedge gamma)=(bT) wedge gamma for locally bounded Borel b whenever the currents involved are positive: their coefficient measures agree on smooth scalar tests and hence identically. The construction extends independently to finite differences of positive currents by uniqueness of signed coefficient measures.\n\nFix v,T and induct on u's sheafified rank, simultaneously on every ordinary subopen. For smooth u, Du is a positive smooth doubly closed form, and\nD(uD(vT))=Du wedge D(vT)=D((vT) wedge Du)=D(v(T wedge Du))=D(vD(uT)).\nThis differentiates currents, not v as a smooth function.\n\nAt a successor take u_j decreasing to the locally bounded final u. The selection proved in n1 makes every predecessor locally bounded, with fixed compact bounds. The inductive equality holds for each u_j. Fixed-measure convergence for the fixed positive D(vT) gives u_jD(vT)->uD(vT). Separately, fixed-T convergence gives D(u_jT)->D(uT), all positive. Since v is continuous, the varying-current multiplication result gives vD(u_jT)->vD(uT). Weak continuity of D proves the equality. Limit ranks use earlier membership locally; ordinary locality and stabilization finish the proof. No continuous predecessors or CPsh recognition are used.\n\nFor m<=n-p factors with at most one discontinuous locally bounded generated factor, every adjacent swap has a continuous factor, so the theorem applies to its inner positive closed current. Outer operations preserve equality of positive currents. Adjacent transpositions give permutation independence. This does not interchange two arbitrary discontinuous factors.\n\nFor h=U-V with continuous generated U,V and continuous generated v, subtraction gives D(hD(vT))=D(vD(hT)); the right side is the difference of products with positive D(UT) and D(VT). Knowing D[h]=0 identifies D(h delta_X), not D(hT). The identity therefore retains the original unknown term.\n\nTheorem 2 and its corollaries are in P21.3-argument.md and P21.3-paper.tex/PDF. Full CLD weak-multiplication evidence is LF10257–10281. The exact bound raw unit is sources/cld-weak-multiplier-bound.txt, hash 0448ea1b480496814c9d81b4a5443f7d6efbb05b91582305b117704008184860. The normalized slice adds one trailing newline and has hash 0eec1c45dfec34af7fb8e231160cc24fd3ef9b8f6dc1185fb8eedd1905483114. Rerun bash reproduce.sh. These proofs are not independently accepted.\n\nArtifacts: /workspace/research/campaigns/round-100/P21.3-original-mixed-symmetry-and-arbitrary-current-research/artifacts/codex-RcZhes",
      "support": [
        "n1"
      ]
    },
    {
      "id": "n3",
      "summary": "New closure: D(vS) preserves continuous-pair compatibility for every locally bounded generated-Psh v, including discontinuous v. Arbitrary-current exhaustion remains unproved.",
      "detailedSummary": "Orient mixed symmetry with the bounded differentiating v as the potentially discontinuous factor and the original U,V as continuous factors. Compatibility of S identifies the positive currents D(US)=D(VS), so their Borel products with v agree. This proves compatibility of D(vS) on every subopen. Smooth positive closed factors and weak positive limits also preserve compatibility. The resulting constructed-current class retains all original fields and ambient hypotheses, but no density theorem identifies it with arbitrary positive closed currents.",
      "text": "Unverified research proof using n1 and n2. Call a positive doubly closed S on W pair-compatible when every ordinary O subset W and every finite continuous generated-Psh U,V with D[U]=D[V] satisfy D(US)=D(VS). This is the original pair property for S, not a classification. Canonical delta_X is pair-compatible because U delta_X=[U]. It is positive by calibrated integration and doubly closed by boundaryless Stokes (CLD v2 15.7.1, 5.8.1–5, 7.7.4); these hypotheses apply to the original pure boundaryless space and its ordinary opens. Actual generic lengths are retained.\n\nThe new result is closure under D(vS) for any locally bounded real generated-Psh v, possibly discontinuous, when p<=n-2. On an arbitrary subopen carrying an admissible pair, n1 gives positive closed D(vS), D(US), D(VS). Apply n2 with potentially discontinuous u=v and continuous factor U, then with continuous factor V. It gives\nD(UD(vS))=D(vD(US)), and D(VD(vS))=D(vD(VS)).\nCompatibility of S identifies the positive currents D(US)=D(VS). Their actual Borel products with the same v agree by n1's intrinsic coefficient-measure construction. Therefore the desired products against D(vS) agree. The subopen was arbitrary, so this is an every-open property. No discontinuous multiplier passes through weak convergence on varying currents. This strengthens the supplied unreviewed proposal, which restricted the differentiating potential to be continuous.\n\nAddition and nonnegative scaling preserve compatibility by linearity. Ordinary locality follows by restricting each pair and using the current sheaf. Weak positive nets preserve it: continuous U,V multiply S_a->S weakly by n2, then D passes to the limit. Positivity and both closedness equations pass on fixed tests. For a smooth middle-positive doubly closed decoration gamma, the wedge is positive closed and the smooth-factor identity gives D(h(S wedge gamma))=D(hS) wedge gamma=0. Require p+degree(gamma)<=n-1. None of these arguments needs global paracompactness or nontrivial valuation.\n\nStarting from delta_X, these operations construct actual compatible currents, including ordered differentiation by several locally bounded discontinuous generated potentials. This does not prove permutation symmetry of two discontinuous factors or compatibility for discontinuous pairs.\n\nThe exact analytic exhaustion left unproved is: for every original K,X,p,W,T and x in W, find one ordinary neighbourhood N and a net of actual positive doubly closed degree-p currents on N, locally constructed from canonical delta_X by these operations, converging to T|N against all compact ordinary smooth tests and every analytic-unit moment refinement. Such an exhaustion would settle the original assertion by the proved weak closure and ordinary locality. No exhaustion follows from scalar smooth density, coefficient estimates, symmetry, or the definition of compatibility. A direct arbitrary-current preservation theorem, a valid fixed-neighbourhood construction for both signs of a general equal-curvature difference, or an admissible analytic counterexample is still needed.\n\nNeither an ambient curvature restriction to arbitrary curves nor ascent under transcendental scalar extension is assumed. There is no asserted strong-current lift or product bridge. The granted strict real-PL and pure-curve results are not counted as universal coverage. This is a genuine closure theorem, rather than a formal annihilator restatement, but it leaves arbitrary-current quantification unresolved.\n\nTheorem 3 and the unchanged target and missing analytic statement are in P21.3-argument.md and P21.3-paper.tex/PDF. status.json has exactly id,status,exact_result,proof_file,concrete_gaps, with status partial. Original inputs, source evidence, hashes, environment and build logs are preserved. Rerun bash reproduce.sh. Original P21.3 remains unresolved; candidate=false.\n\nArtifacts: /workspace/research/campaigns/round-100/P21.3-original-mixed-symmetry-and-arbitrary-current-research/artifacts/codex-RcZhes",
      "support": [
        "n1",
        "n2"
      ]
    },
    {
      "id": "n4",
      "summary": "A fixed compact probability convolution kernel commuting with both split-torus monomial shears must be delta_0. This diagnoses one rigid regularization attempt; the original atom remains unresolved.",
      "detailedSummary": "Two actual analytic monomial automorphisms induce the shears A(x,y)=(x+y,y) and B(x,y)=(x,x+y). A single convolution kernel commuting with both pullbacks is invariant under both shears. Compact support and their iterates force its support to be zero. Transformed kernels and directed finite-presentation regularization are not excluded. Partition-of-unity gluing can separately lose closedness. Neither diagnostic supplies an admissible analytic counterexample. The paper builds and finite provenance checks pass, without mathematical acceptance.",
      "text": "Independent elementary diagnostic. Fix X=(G_m,Q2^2)^an, a good separated strict smooth boundaryless analytic surface. The monomial maps (z1,z2)->(z1z2,z2) and (z1,z2)->(z1,z1z2) have monomial inverses. In logarithmic coordinates they induce A(x,y)=(x+y,y) and B(x,y)=(x,x+y). CLD arXiv:1204.6277v2, 12.1.1–4 supplies the analytic-torus and functorial character/tropicalization setup; only these explicit maps are used.\n\nLet mu be a compactly supported positive probability measure on R^2 and K_mu f(x)=integral f(x-z) dmu(z). Commutation with pullback by A, evaluated at zero for every compact smooth f, gives integral f(-Az) dmu(z)=integral f(-z) dmu(z), hence A_*mu=mu by uniqueness of Radon measures from smooth tests. Likewise B_*mu=mu. The compact support is invariant under these invertible shears. If (x,y) belongs to it, all A^k(x,y)=(x+ky,y) belong to it, so compactness forces y=0. Then all B^k(x,0)=(x,kx) belong to it, forcing x=0. Thus mu=delta_0. No nontrivial compact smooth probability mollifier has both fixed-kernel commutation properties.\n\nThis excludes only one unchanged scalar kernel. Coordinate-transformed kernels, kernels adapted to finite moment collections and directed compatible systems remain possible. The proposition proves no impossibility of analytic current regularization. It supplies no potentials, canonical curvature relation or defective product; the torus is already in established positive geometric ranges.\n\nA separate Leibniz calculation shows why nonnegative partitions alone cannot glue closed regularizations: d'(sum rho_i R_i)=sum d'rho_i wedge R_i for closed R_i, and sum rho_i=1 does not cancel this expression without compatibility. On Euclidean R^2, R1=[1], R2=2[1], rho1=rho and rho2=1-rho with nonconstant 0<rho<1 give the positive but non-first-closed current [2-rho]. The differential rule is CLD v2 3.3.10–12 and 7.7.1–5. This is a failure of that gluing operation, not an analytic P21.3 counterexample.\n\nThe full original every-field, every-open, every-current continuous-pair assertion remains unproved in this work. No negative construction with separately admissible finite continuous generated-Psh U,V, upstairs canonical Hessian equality, an allowed positive doubly closed current and a detecting compact smooth test was obtained.\n\nProposition 4 and the gluing calculation are in P21.3-argument.md and P21.3-paper.tex/PDF. Rerun bash reproduce.sh. Observed build evidence: the command exited 0, both pdfTeX passes completed, and pdfinfo reported an 11-page PDF produced by pdfTeX-1.40.26. The final audit passed original-input preservation, exact task/assignment hashes, 27 literal primary slices and full-source hash, the bound weak-multiplier bytes and newline distinction, nine premise records, exact status keys, four backward-supported notes with candidate=false, shear-power transcription for k=0,...,100, and the PDF header. Logs and environment details are retained locally. These are finite observations, not verification of the infinite mathematical arguments or a density theorem. No independent reviewer, other worker/model, install, network acquisition, external message, source mutation or heavy computation was used. candidate=false.\n\nArtifacts: /workspace/research/campaigns/round-100/P21.3-original-mixed-symmetry-and-arbitrary-current-research/artifacts/codex-RcZhes",
      "support": []
    }
  ],
  "candidate": false,
  "workspace": "/workspace/research/campaigns/round-100/P21.3-original-mixed-symmetry-and-arbitrary-current-research/artifacts/codex-RcZhes"
}

END MATHEMATICAL DATA


BEGIN MATHEMATICAL DATA: Documentary reading boundaries, not grants
{
  "canonical_result": "/workspace/research/root-checks/P21.3-round100-canonical-native-result-20261005.json",
  "sha256": "5acc3feabf2d62829164e7766b31b50e963700bf317d47221b09bcfe503fb224",
  "whole_canonical_notes_root_read": true,
  "whole254_LF_core_root_read": true,
  "all9_standalone_external_premise_records_root_read": true,
  "all27_literal_source_unit_bindings_reproduced": true,
  "all27_primary_bodies_root_read": false,
  "whole_TeX_root_read": false,
  "original_task_and_assignment_bytes_equal": true,
  "artifact_input_json_values_equal": true,
  "artifact_input_bytes_equal": false,
  "frozen_input_sha256": "caedf33a5e9455b4aadb44fde3b1f04c6400c94aa6055413ca51ad18a8a35331",
  "artifact_input_sha256": "e31c3295df8bb3bc7cd0e2be9c274eee67475c8a6f529c8300e25aa79400c61c",
  "bound_weak_multiplier_and_single_newline_difference_verified": true,
  "independent_mathematical_review_performed": false,
  "candidate": false,
  "original_closed": false,
  "new_scoped_paper_accepted": false
}

END MATHEMATICAL DATA
