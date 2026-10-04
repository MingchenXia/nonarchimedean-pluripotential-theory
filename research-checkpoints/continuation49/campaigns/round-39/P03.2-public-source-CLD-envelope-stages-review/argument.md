# Exact final status

{
  "id": "P03.2",
  "status": "open_partial_progress",
  "exact_result": "Full-union envelopes for every usc obstacle have ordinary CLD ordinal stage 1 on boundaryless reduced separated good strict pure one-dimensional curves with bijective normalization over complete nontrivially valued perfect fields with a countable dense subset and residue algebraic over a finite field; also for their ordinary locally trivial projective-space bundles and finite towers. Without the residue/genus condition the checked construction proves only ordinal stage 3. A fresh explicit split-node obstruction works with or without relative boundary and propagates through projective factors.",
  "proof_file": "P03.2-argument.md",
  "concrete_gaps": [
    "No sharp necessary-and-sufficient classification in the normal/geometrically unibranch higher-dimensional range.",
    "Without ordinary/weak smooth sheaf equality the proof gives stage 3, not stage 2; no collapse of the nested approximation operations is proved.",
    "Countability extracts sequences from nets and is not shown necessary.",
    "Positive curve theorems exclude relative-boundary points; classical boundary extension does not provide ordinary CLD approximants.",
    "No ordinary smooth descent across arbitrary completed perfect closure for imperfect perfected-unibranch curves.",
    "Higher-dimensional positivity is limited to projective-space bundles; open-disc products and arbitrary normal geometry are not covered.",
    "No new proof of nonsplit-node surface or codimension-two pinching obstructions; dossier assertions were not imported.",
    "No identification of full competitor families or envelopes after arbitrary scalar extension, although pullback of every proved envelope preserves its stage.",
    "Unverified draft mathematical arguments; source hashes and TeX builds are not proof certificates."
  ]
}

# Entire final proof

---
title: 'P03.2: full obstacle envelopes with explicit CLD ordinal bounds'
author: 'Fresh public-source argument; unverified draft'
date: '4 October 2026'
---

# Result and exact scope

The original sharp P03.2 classification remains open. The following is a sufficient geometric sector for the **entire** locally Fubini--Study/semipositive real-PL competitor union and **every** upper semicontinuous obstacle. No invariant restriction, selected competitor sequence, or common modulus is assumed.

**Theorem A (ordinary stage 1 on curves).** Let $K$ be a complete, nontrivially valued, perfect non-Archimedean field having a countable dense subset. Assume its residue field $\widetilde K$ is algebraic over a finite field. Let $X$ be a nonempty reduced, separated, good, strictly $K$-analytic curve, pure of dimension one, with **no relative boundary**. Assume that its normalization $\nu:\widetilde X\to X$ is bijective on Berkovich points. For any usc function $f:X\to\mathbb R\cup\{-\infty\}$ set

$$
\begin{aligned}
\mathcal E_f(X)&=\{h:X\to\mathbb R:h\leq f,\ h\text{ is locally Fubini--Study}\\
&\hspace{6em}\text{or semipositive real PL}\},\\
s_f&=\sup_{h\in\mathcal E_f(X)}h,\qquad u_f=s_f^*.
\end{aligned}
$$

Then $u_f\in\operatorname{Psh}_{X,1}\subset\operatorname{Psh}_{X,2}$ for the **July 2025 second version** of Chambert-Loir--Ducros. At each point of $X$ there is a single ordinary open neighborhood $W$ and a sequence of finite ordinary CLD-smooth functions $q_j$ on $W$, with $d'd''q_j\geq0$, such that $q_j\downarrow u_f|_W$. If the family is empty, use $q_j=-j$. If it is nonempty, $u_f$ is finite and classically psh. Continuity of $u_f$ is not asserted.

The theorem covers normal curves and also reduced singular curves with bijective normalization over the displayed field. In particular it covers boundaryless ordinary open subsets of analytifications of smooth curves of **arbitrary genus over $\mathbb Q_p$**, including elliptic and higher-genus curves with good reduction. These are actual non-toric, unrestricted competitor results. A second concrete alternative to the residue-field condition is that $\widetilde X$ is potentially locally isomorphic to $\mathbb P^{1,\mathrm{an}}$, using the other case of GJR Remark 15.10. The residue-field version is the main sector here.

**Theorem B (projective factors and bundles).** Under Theorem A's hypotheses on $X$, let $p:Y\to X$ be an ordinary analytically locally trivial projective-space bundle with fiber $\mathbb P^{m,\mathrm{an}}$, where $m\geq1$, and assume $Y$ is good and separated. This includes $Y=X\times_K\mathbb P^{m,\mathrm{an}}$. It is strictly analytic and boundaryless. For every usc $F:Y\to\mathbb R\cup\{-\infty\}$ the full union envelope on $Y$ belongs to $\operatorname{Psh}_{Y,1}$. Thus this includes normal higher-dimensional spaces when $X$ is normal, as well as the displayed unibranch singular bases. The same statement holds for any finite tower of these projective-space bundles.

There is also a weaker bound without a genus or residue-field assumption:

**Theorem C (stage 3, not a second-stage conclusion).** Retain Theorem A's hypotheses except the residue-field condition. Then the full envelope belongs to $\operatorname{Psh}_{X,3}$, and the envelopes in Theorem B's projective bundles belong to $\operatorname{Psh}_{Y,3}$. This is positivity in the *second version* of CLD, but it does **not** establish membership in ordinal stage 2. The proof below keeps the three limiting operations separate and makes no assertion that stage 3 is optimal or strictly larger for these envelopes.

We also give a fresh explicit split-node obstruction, on both an affinoid curve and its boundaryless interior, and propagate it through projective factors. It does not supply sharp necessity for all normal or geometrically unibranch spaces.

# What the checked published definitions actually say

All source citations refer to the exact supplied public caches. The dossier's unpublished book claims and review verdicts are not premises. In particular some theorem numbering in cross-citations differs from the supplied versions: the curve semipositivity equivalence is **Proposition 5.1** in the supplied arXiv:2503.05513 text, even though arXiv:2506.13548v2 cites an older Proposition 3.1.

CD means Chambert-Loir--Ducros, arXiv:1204.6277v2, **25 July 2025**. Its Definition 8.1.1, printed p.195, on a refined G-tropical space defines $\operatorname{Psh}_X$ as the smallest subsheaf of functions valued in $\mathbb R\cup\{-\infty\}$ containing ordinary smooth $u$ with $d'd''u\geq0$ and closed under decreasing **sequences**. Lemma 8.1.4, p.196, defines

$$
\begin{aligned}
\operatorname{Psh}_{X,0}&=\{\text{ordinary smooth }u:d'd''u\geq0\},\\
\operatorname{Psh}_{X,\alpha+1}&=\{\text{locally decreasing sequential limits}\\
&\hspace{6em}\text{of stage }\alpha\}.
\end{aligned}
$$

At a limit ordinal, functions locally lie in an earlier stage. Stages increase. Consequently *version v2*, *ordinal stage 2*, *current positivity*, and *classical pshness* are four different statements. We prove the actual ordinal bounds stated above.

CD Proposition 12.4.1, pp.345--346, puts a canonical G-tropical structure on a Hausdorff analytic space using analytic domains and rational combinations of log norms of analytic units and constants. Section 12.4.6 supplies the refinement using the **ordinary local** affine sheaf. Section 12.4.5 says analytic morphisms, including ones over different fields, induce G-tropical morphisms. CD Proposition 15.1.1(b) and Corollary 15.1.2, pp.421--422, identify ordinary smooth functions by ordinary open local expressions

$$
q=\phi(-\log|g_1|,\ldots,-\log|g_r|),\qquad g_i\in\mathcal O^\times,\quad\phi\in C^\infty.
$$

These are not merely G-local expressions or harmonic tropicalizations. CD Theorem 15.7.1, p.432, makes a Hausdorff pure-dimensional analytic space a calibrated tropical space of its analytic dimension, with its **actual analytic relative boundary**. Section 15.7.2 identifies the domain structure and gives $\partial V=(\partial X\cap V)\cup\partial(V/X)$. All our positive envelope domains are boundaryless; an ordinary open subset of a boundaryless space is boundaryless. Compact affinoids used inside a proof may have boundary, but are not substituted for the ordinary approximation neighborhood.

CD Proposition 8.1.5 preserves **each ordinal stage** under a refined G-tropical morphism. CD Proposition 8.3.1(b), p.201, says that on a boundaryless tropical space a **smooth** function has positive $d'd''$ form exactly when its associated current is positive. This smooth qualification is indispensable below.

GJR means Gubler--Jell--Rabinoff, arXiv:2111.05741. In Section 5 it assumes a nontrivially valued field and a good strict analytic space. Definition 5.1 defines real PL by G-local real linear combinations of log norms of analytic units. Definition 7.8 and 7.9, p.47, define LFS and give its **ordinary local** nonnegative linear-combination-of-finite-maxima description. LFS functions are real PL and semipositive. Hence every member of the displayed union is continuous, real-valued, and semipositive real PL; we nevertheless retain both branches explicitly in the descent argument.

GJR Proposition 7.10, pp.47--48, requires $x\in\operatorname{Int}(X)$. It produces a uniform LFS approximating sequence on a strict analytic neighborhood. Its proof ends with the **ordinary open** tube $U=\operatorname{red}^{-1}(V')$, on which all $h_\epsilon=h+\epsilon h'$ are LFS. This does not say arbitrary envelopes are locally uniform limits of LFS minorants, nor that these approximants stay under an obstacle. It also does not automatically give one common ordinary moment chart for all members of the sequence.

GJR Proposition 15.11, pp.80--81, assumes a **smooth curve, meaning rig-smooth without boundary**, over a nontrivially valued field. On any relatively compact ordinary open subset it gives a decreasing **net of weakly smooth** psh functions converging pointwise to a subharmonic function. Remark 15.10 says weakly smooth and ordinary CLD-smooth agree if the residue field is algebraic over a finite field, or the curve is potentially locally isomorphic to $\mathbb P^{1,\mathrm{an}}$. GJR Remark 10.10 checks that its ordinary smooth forms agree with the earlier CLD ordinary smooth forms; the expression in CD 15.1 above gives the same ordinary sheaf in v2. Weak-current positivity restricted to ordinary smooth test forms gives ordinary-current positivity; for these now ordinary smooth functions CD 8.3.1(b) converts that to stage-0 form positivity.

Without those extra hypotheses harmonic tropicalizations can be genuinely non-smooth (GJR 15.10, Thuillier Theorem 2.3.21 and Lemma 2.3.22). This is a defect of a direct approximation argument, **not** a proof that the residue-field or genus hypothesis is necessary for stage 1 or stage 2.

GRc means Gubler--Rabinoff, arXiv:2506.13548v2, 17 September 2025. Its Theorem 4.3, pp.22--23, gives semipositive real PL if and only if classically psh for good strict spaces over nontrivially valued fields. Definition 4.1 quantifies over **every analytic field extension and every analytic curve morphism**; Section 4.1.3 reduces curve tests to connected smooth strict curves. Proposition 3.5(7,8), together with Section 3.4.1, identifies ordinary Thuillier subharmonicity with scalar-stable curve subharmonicity on smooth strict curves. Lemma 3.9 proves, over a perfect field, that normalization of a reduced strict curve is rig-smooth, is an isomorphism off a discrete set of rigid points, is a topological quotient, and bijects boundaries. Theorem 6.1 gives the local maximum principle at interior points; Theorem 6.4 gives the Shilov maximum principle on affinoids.

GRs means arXiv:2503.05513 in the supplied version. Its Proposition 5.1, p.15, identifies Thuillier subharmonic real-PL functions on smooth strict curves with nef residues, hence semipositivity. Its proof checks scalar extension and reduction hypotheses. No unpublished source is used for this implication.

Thuillier's supplied thesis works with smooth strict analytic curves and a nontrivially valued complete field. Proposition 3.1.8(iii), printed p.62 / PDF p.76, says the usc regularization of the supremum of an increasing locally bounded subharmonic family is subharmonic. The actual PDF was inspected: the words are *famille croissante et localement bornée*. Our family below is locally bounded on both sides, so no interpretation of 'bounded' is needed. Theorem 3.4.2, printed pp.89--90, gives a decreasing family of Thuillier-lisse subharmonic functions on any relatively compact ordinary open subset. These 'lisse' functions are **real PL, not ordinary CLD-smooth**: Proposition 3.2.5 identifies them with the G-sheaf generated by real combinations of log norms of analytic units. Its proof on a semistable skeleton is retained. The distinct ordinary/G topologies cannot be collapsed here.

# Elementary lemmas used in the new applications

## Countable local topology and extraction of an actual sequence

Let $K$ have a countable dense subset. A strict $K$-affinoid algebra $A$ has a countable norm-dense subset: polynomials with coefficients in a countable dense subset of $K$ are dense in a Tate algebra, and their images are dense in a quotient Banach algebra. For a bounded multiplicative seminorm $x$, $|a(x)|\leq\|a\|$, and

$$
\big|\,|a(x)|-|b(x)|\,\big|\leq\|a-b\|.
$$

Thus all evaluation functions on $\mathcal M(A)$ are uniform limits of evaluations on this countable set. The evaluations on that set separate points and generate the topology. The compact Hausdorff space $\mathcal M(A)$ therefore embeds in a countable product of real compact intervals, so is metrizable and second countable. A relatively compact ordinary open subset $W$ of a good Hausdorff analytic space has compact closure covered by finitely many interiors of affinoid neighborhoods. Consequently $W$ is second countable. This proof needs no global paracompactness of $X$.

Here is the precise net-to-sequence lemma. Let $(a_i)$ be a decreasing directed net of continuous real functions on a second-countable space $W$ with pointwise infimum $u\in\mathbb R\cup\{-\infty\}$. For each rational $t$, the open set

$$
\{u<t\}=\bigcup_i\{a_i<t\}
$$

is Lindelof, so choose countably many indices whose open sets cover it. Enumerate the union of the chosen indices over all rational $t$. Inductively choose $i_j$ dominating the $j$th listed index and $i_{j-1}$. Then $a_{i_j}$ decreases. If its limit at $x$ exceeded $u(x)$, a rational $t$ strictly between them would yield a chosen index with $a_i(x)<t$ and hence an eventual contradiction. Thus $a_{i_j}\downarrow u$ on **the same ordinary open set $W$**. The argument works also at $u=-\infty$. If the chosen set is finite or empty, repeat or add a starting index.

## Explicit ordinary stage 1 for LFS functions

On an ordinary open neighborhood an LFS function is a finite sum, with nonnegative real coefficients, of terms $\max_i\ell_i$, where each $\ell_i=-\log|g_i|$ for an analytic unit. For $\epsilon>0$ replace a term by

$$
M_\epsilon(\ell)=\epsilon\log\left(\sum_i e^{\ell_i/\epsilon}\right).
$$

This is an ordinary smooth moment expression on that **fixed neighborhood**, is convex in the moment coordinates, has positive $d'd''$, and satisfies

$$
0\leq M_\epsilon-\max_i\ell_i\leq\epsilon\log N.
$$

The derivative with respect to $\epsilon$ is the entropy $-\sum_i p_i\log p_i\geq0$, where $p_i=e^{\ell_i/\epsilon}/\sum_k e^{\ell_k/\epsilon}$. Hence choosing $\epsilon\downarrow0$ gives an actual decreasing ordinary smooth sequence. Summing the finitely many terms preserves these properties. This proves LFS $\subset\operatorname{Psh}_1$ with ordinary approximants, not just current positivity. Convex moment pullbacks are positive, as checked in CD 8.9.4 and 8.2.1; constants are harmless.

## The safe bound for a semipositive real-PL function

Let $h$ be semipositive real PL at an interior point. GJR 7.10 supplies a common ordinary open neighborhood $V$ and LFS $h_i$ uniformly converging to $h$ there. Pass to a subsequence with $\|h_{i_j}-h\|_V\leq e_j=4^{-j}$ and put $b_j=h_{i_j}+2e_j$. Each $b_j$ is stage 1 on $V$ by the preceding ordinary local construction. Moreover

$$
h+e_j\leq b_j\leq h+3e_j,
\qquad b_{j+1}\leq h+\tfrac34 e_j<h+e_j\leq b_j.
$$

Thus $b_j\downarrow h$ uniformly on $V$ and $h\in\operatorname{Psh}_2$. The inner smooth sequences proving membership of each $b_j$ in stage 1 may use different ordinary neighborhoods at a selected point, but **each sequence has its own fixed ordinary neighborhood**; the outer stage-1 sequence $b_j$ is on the fixed set $V$. This is exactly the two-level definition. There is no unproved diagonalization to a single smooth sequence on $V$. The same argument also verifies CPsh stage 2 for $h$; we do not need that terminology.

## Homeomorphic normalization and ordinary smooth descent

For the curves in our theorems, GRc Lemma 3.9 makes a bijective normalization a homeomorphism, since it is a topological quotient. It is an isomorphism outside a discrete set $D$ of rigid points, and its source is smooth and boundaryless.

Every ordinary smooth function $a$ on an open subset of $\widetilde X$ is locally constant at a rigid point. Here is the elementary unit-norm fact used in GRc Lemma 3.9(6), with an explicit proof. For an analytic unit $g$ at a rigid point $z$, $\alpha=g(z)$ lies in a finite extension of $K$ and has modulus $\rho>0$. Let $P$ be its monic minimal polynomial of degree $d$. Every conjugate root has modulus $\rho$, since a complete non-Archimedean field has a unique extension of its norm to a finite extension. On the ordinary neighborhood $|P(g)|<\rho^d$ of $z$, suppose $|g(y)|\ne\rho$. In a complete algebraic extension of $\mathcal H(y)$, all differences of $g(y)$ from the roots of $P$ then have modulus $\max(|g(y)|,\rho)$, by the ultrametric inequality. Their product has modulus at least $\rho^d$, a contradiction. Thus $|g|=\rho$ on that neighborhood. An ordinary local moment expression for $a$ uses finitely many such units, so is constant on the intersection of these neighborhoods. This fact applies also to rigid points with finite residue field extension, not only $K$-rational points.

If $a$ has positive $d'd''$ on $\nu^{-1}(W)$, transfer it by the homeomorphism to a function $\bar a$ on $W$. Off $D$ it is ordinary smooth and positive by the analytic isomorphism. At each point of $D$ it is constant on an ordinary neighborhood (transport the constant neighborhood by the homeomorphism), so is ordinary smooth with zero $d'd''$ there. Consequently $\bar a$ is stage 0 on $W$. This is an actual ordinary smooth descent proof, not descent by harmonic forms. Inductively, descending an entire decreasing sequence gives stage-preserving descent for each finite stage used here. A local sequence on $\widetilde X$ is transported to the same ordinary image neighborhood; the order and pointwise limit are preserved.

# Proof of the full curve-envelope theorems

If $\mathcal E_f(X)=\varnothing$, both the raw envelope and its usc regularization are $-\infty$, and $-j\downarrow-\infty$ proves stage 1. This covers $f\equiv-\infty$, any obstacle taking $-\infty$ somewhere, and any other obstacle with no global real-valued competitor.

Suppose the family is nonempty, and fix one member $h_0$. Because $h_0\leq f$, the obstacle is finite everywhere. Upper semicontinuity and the absence of $+\infty$ imply local upper boundedness: near $x$, $f<f(x)+1$. Each competitor is continuous and classically psh by GJR 7.8 and GRc 4.3. Its pullback to $\widetilde X$ is a finite Thuillier-subharmonic function, using the scalar-stable functoriality checked in GRc 3.4.1 and 4.2.

Direct the finite subsets of $\mathcal E_f(X)$ containing $h_0$ by inclusion, and take their maxima after pullback. These are subharmonic by Thuillier 3.1.8(i); they need not themselves remain real PL, and no closure assertion for real-PL maxima is used. They form an increasing family with supremum $s_f\circ\nu$, bounded locally below by $h_0\circ\nu$ and above by $f\circ\nu$. Thuillier 3.1.8(iii) therefore shows

$$
\widetilde u=(s_f\circ\nu)^*
$$

is subharmonic on the smooth boundaryless curve $\widetilde X$. Since $\nu$ is a homeomorphism, the neighborhood formula $a^*(x)=\inf_{W\ni x}\sup_W a$ gives

$$
\widetilde u=u_f\circ\nu.
$$

Also $h_0\leq s_f\leq u_f\leq f$: the last inequality follows directly from usc of $f$. Thus $u_f$ is finite. This establishes the full-family supremum step for every obstacle, including ones for which no continuous obstacle approximation is available. It is not an envelope of a selected equicontinuous subfamily.

For **Theorem A**, choose a relatively compact ordinary open neighborhood $\widetilde W$ of the preimage of the point under consideration. GJR 15.11 applies to $\widetilde u$ and provides a decreasing net of finite weakly smooth psh functions on the fixed set $\widetilde W$. Under the residue-field hypothesis, GJR 15.10 identifies the weakly smooth sheaf with the **ordinary** smooth sheaf. The same identification applies under the alternative potentially locally projective-line hypothesis. After restriction to ordinary test forms, the positive weak currents of these smooth functions give positive ordinary currents; CD 8.3.1(b), using CD 15.7.1, gives positive ordinary $d'd''$ forms. Thus the net consists of stage-0 functions. The countable-topology lemma extracts a decreasing **sequence** on $\widetilde W$. Ordinary smooth descent through $\nu$ gives the promised decreasing smooth sequence on $W=\nu(\widetilde W)$. This proves ordinal stage 1 and, by inclusion, stage 2.

For **Theorem C**, apply Thuillier 3.4.2 instead. It provides a decreasing net of lisse subharmonic functions on the same $\widetilde W$. They are continuous real PL by Thuillier 3.2.5; this identifies their G-local form with GJR 5.1. GRs Proposition 5.1 makes them semipositive real PL. The ordinary neighborhood lemma using GJR 7.10 then puts each of them in stage 2 on $\widetilde W$. Extract a decreasing sequence with the countable-topology lemma; its limit is stage 3. Stage-preserving descent through normalization proves the assertion on $X$.

The order of the limits is decisive: smooth maxima approximate LFS (stage 1); LFS approximate semipositive real PL (stage 2); a decreasing family of the latter approximates the envelope (stage 3). These source statements alone do not reduce the last two operations to stage 2. The refined residue-field theorem bypasses both operations by making the GJR 15.11 net ordinary smooth.

# All analytic extensions and all curve tests

The stage assertions above already control the pullback of the actual **ground-field** regularized envelope. Let $K'/K$ be any complete analytic extension, regardless of countability or residue field, and let $g:C\to X_{K'}$ be any morphism from a Hausdorff analytic curve. CD 12.4.5 and 8.1.5 preserve stage $r$ under $g$ and the scalar projection; equivalently, locally pull back each of the finite ordinary smooth approximants and every decreasing sequence in its construction. Moment units pull back to moment units and their positive smooth forms remain positive. Thus

$$
u_f\circ\pi_{K'/K}\circ g\in\operatorname{Psh}_{C,r},
\quad r=1\text{ in A},\quad r=3\text{ in C}.
$$

In particular it is subharmonic in the scalar-stable extended convention and $u_f$ is classically psh. To check the last implication directly, GRc Section 1.2 reduces it to smooth connected strict curve tests over nontrivially valued fields: ordinary smooth psh functions on such curves are subharmonic, and decreasing limits remain subharmonic (GRc 3.5(5)). Iterating this argument proves the claim for the finite stages used here. The empty-family $-\infty$ limit uses the extended convention.

No assertion is needed that scalar projection is open, that usc regularization commutes with an arbitrary scalar projection, or that competitor families become equal after scalar extension. We assert scalar and curve pullback of **$u_f$**, not equality of the scalar-extended envelope of the full new competitor family with that pullback. This is precisely the scalar quantifier for the positivity conclusion. We do not extend the conclusion to arbitrary imperfect perfected-unibranch domains: approximants upstairs in a completed perfect closure would require an additional ordinary smooth descent proof not supplied here.

# Exact projective-bundle reduction for arbitrary obstacles

We prove the reduction in a slightly broader setting: $X$ can be any good separated strict analytic space over a nontrivially valued field, and may have relative boundary; let $p:Y\to X$ be a good separated ordinary locally trivial projective-space bundle. The reduction itself does not assert positivity or regularity of the base envelope.

First, for any competitor $h$ on $Y$ and any $x\in X$, its restriction to the fiber $Y_x\simeq\mathbb P^{m,\mathrm{an}}_{\mathcal H(x)}$ is finite continuous and classically psh. This follows from GRc 4.3 and 4.2, first extending the field to $\mathcal H(x)$ and then pulling back along the fiber morphism. The fiber is compact, connected, and boundaryless. For completeness, connectedness of projective space can be checked using its $m+1$ standard closed unit-polydisc domains. Each is connected: a clopen partition would glue constants 0 and 1 into an idempotent analytic function in a Tate algebra, which is a domain and has no nontrivial idempotents. All these domains have a common rational point with homogeneous coordinates $(1:\cdots:1)$, so their union is connected. Every projective point lies in one of them by selecting a largest homogeneous coordinate.

The restriction of $h$ attains its maximum. Its maximum set is closed by continuity and open by GRc Theorem 6.1, because every point of the fiber is interior. Connectedness makes that set the whole fiber. Thus **every competitor in the full union is fiberwise constant**, without a group action or an invariance restriction.

Write $h=b\circ p$. On each ordinary trivializing open set of the base choose the analytic section $(1:0:\cdots:0)$. Then $b=h\circ\sigma$ is continuous and belongs to the same competitor branch as $h$: for LFS, pull back the finite-maxima-of-units local expression; for semipositive real PL, use GJR Lemma 5.4 and Proposition 7.6. These locally defined functions agree because $h$ is fiberwise constant. Conversely, $p^*b$ is in the same branch whenever $b$ is. Hence this is an exact correspondence for the full union, and also separately for its two branches.

Define the fiberwise infimum obstacle

$$
g(x)=\inf_{y\in p^{-1}(x)}F(y).
$$

It can equal $-\infty$ even if $F$ is pointwise finite; this causes no problem. The map $p$ is surjective and smooth (projective-space projection is locally covered by relative affine spaces). It is open by Berkovich, *Etale cohomology for non-Archimedean analytic spaces*, Corollary 3.7.4, printed p.77, applied locally to this smooth good morphism. Then

$$
\{g<t\}=p(\{F<t\})
$$

is open for every real $t$, so $g$ is usc. The equality uses only the defining property of an infimum, including at $-\infty$. The correspondence above identifies exactly $h\leq F$ with $b\leq g$. Therefore, with the empty-family convention,

$$
s_F^Y=s_g^X\circ p.
$$

For a continuous open surjection $p$ and any extended raw function $a$, the neighborhood definition of regularization gives

$$
(a\circ p)^*=a^*\circ p.
$$

Indeed, continuity gives the upper inequality by pulling back base neighborhoods; openness gives the lower inequality since the image of every neighborhood of a selected lift is a base neighborhood. These inequalities also hold for $-\infty$. Consequently

$$
(s_F^Y)^*=(s_g^X)^*\circ p.
$$

Apply Theorem A or C to the actual usc obstacle $g$. Pulling back its ordinary smooth sequences or finite-stage construction preserves the stated ordinal stage by CD 8.1.5. In the stage-1 case, every point of $Y$ has a neighborhood $p^{-1}(W)$ on which the pulled-back single smooth sequence decreases to the actual full envelope. This proves Theorem B and the stage-3 counterpart. A finite tower follows by repetition; the effective obstacle at each stage remains usc. All choices of $F$ are allowed, including strongly noninvariant ones. The result proves an exact reduction rather than only a comparison with an invariant subfamily.

If the base is boundaryless, the total space is boundaryless because $p$ is a boundaryless smooth morphism and $\partial Y\subset p^{-1}(\partial X)\cup\partial(Y/X)$. With a base boundary the exact reduction still holds, but no positive stage claim is inferred from our boundaryless curve theorems. This distinguishes an auxiliary relative-boundary identity from an envelope-positivity theorem at boundary points.

# Fresh branch obstruction and its projective propagation

Fix any complete nontrivially valued $K$, choose $\varpi\in K$ with $0<|\varpi|<1$, and put $a=-\log|\varpi|>0$, $r=|\varpi|$. Let

$$
Z=\mathcal M(K\langle x,y\rangle/(xy)),
$$

with node $o$, $x$-branch $D_x$, and $y$-branch $D_y$. Let $Z^\circ=\operatorname{Int}(Z)$; its branches are open unit discs joined at $o$. The argument works on either $Z$ or $Z^\circ$, denoted by $V$.

Define a finite continuous obstacle by

$$
f|_{D_x\cap V}=0,\qquad
f|_{D_y\cap V}=-a\min(|y|/r,1).
$$

Both definitions give 0 at $o$, and the functions are continuous and agree there. The branch gluing topology therefore makes $f$ continuous on $V$.

For any full-union competitor $h$, GRc 4.3 and functoriality imply its pullback to the closed $y$-disc of radius $r$ is classically psh. That disc has singleton Shilov point $\eta_r$: for every analytic power series $\sum c_jy^j$, all seminorms on the disc are bounded by $\max_j|c_j|r^j$, which is its Gauss value at $\eta_r$. Its value satisfies $h(\eta_r)\leq f(\eta_r)=-a$. GRc Theorem 6.4 yields $h\leq-a$ throughout that disc. On the remaining part $|y|\geq r$, the obstacle itself is $-a$. Thus every competitor is $\leq-a$ on the whole $y$-branch, including $o$.

For each integer $n\geq1$ define

$$
h_n|_{D_x\cap V}=\max(-a,n^{-1}\log|x|),\qquad
h_n|_{D_y\cap V}=-a,
$$

with the value $-a$ at $o$. Each $h_n$ is a finite continuous LFS function on $V$. Near $o$, on both branches of radius less than $|\varpi|^n$, it is the constant $-a$. Away from $o$ on the $x$-branch, $x$ is an analytic unit and the expression is $n^{-1}\max\{-\log|\varpi^{-n}|,-\log|x^{-1}|\}$. On the $y$-branch it is constant. These are ordinary local LFS expressions, including across the bend. Also $h_n\leq f$ everywhere. Thus these are members of the **exact** union family, not model competitors for a different envelope.

At every $x$-branch point other than $o$, $\log|x|$ is finite and $h_n\to0$; the obstacle gives the upper bound 0. On the $y$-branch the preceding maximum principle gives the upper bound $-a$, attained by $h_n$. We have proved the exact raw formula

$$
s_f(z)=\begin{cases}0&z\in(D_x\cap V)\setminus\{o\},\\-a&z\in D_y\cap V.\end{cases}
$$

Consequently $u_f=s_f^*$ changes only the nodal value to 0. Its pullback to the closed $y$-disc of radius $r$ has value 0 at the origin and $-a$ at its Shilov point. It violates the affinoid Shilov maximum principle and is not classically psh. It therefore belongs to **no CLD ordinal psh stage**, since smooth psh curve tests and decreasing limits give classical pshness as above. This counterexample is already boundaryless if $V=Z^\circ$; it also checks relative boundary explicitly if $V=Z$.

For $V\times\mathbb P^{m,\mathrm{an}}$ and obstacle $f\circ p$, the exact reduction theorem proved above gives $u_{f\circ p}=u_f\circ p$, since the fiberwise infimum of the pulled-back obstacle is $f$. An analytic projective-space section and the same closed branch disc show failure in every dimension $m+1$. This uses neither a book proposition nor an imported earlier counterexample.

# What remains unresolved for the original atom

The sufficient residue-field and countability assumptions are not shown necessary. A non-smooth harmonic germ does not establish absence from a decreasing CLD stage. The general curve argument only reaches stage 3; reducing it to stage 2 or 1 without the GJR ordinary/weak sheaf coincidence needs an additional construction. Countability was used to extract genuine sequences from nets, and no replacement for that step over general nonseparable fields is proved.

Theorem A includes the bijective-normalization curve range over the specified perfect ground fields. It does not prove ordinary approximation descent for arbitrary imperfect fields merely satisfying a perfected-normalization condition. Neither Theorem A nor C includes curve relative-boundary points; GRc's classical boundary extension proposition does not furnish a CLD ordinary approximation sequence there. GJR 7.10's interior hypothesis and GJR 15.11's boundaryless hypothesis are respected throughout the positive proofs.

The projective-bundle sector is geometric and unrestricted in its obstacle and competitor family, but the higher-dimensional argument depends on proper connected fibers that force all competitors to descend. It does not extend to open-disc products, arbitrary normal or geometrically unibranch domains, general proper fibrations without ordinary local sections, or the supplied nonsplit-node/product and codimension-two pinching claims. Those dossier claims were not imported and their proofs have not been established here. Exact scalar pullback of the proved envelope is handled, while exact identification of all competitor families after arbitrary scalar extension is neither needed for positivity nor asserted.

There is no sharp necessary-and-sufficient classification for the original full range in this argument. P03.2 remains **open**, and `candidate=false` is required. No P03.1 or P03.3 classification is claimed; finite usc envelope positivity does not imply continuity.

# Reproduction and evidence limitations

The retained original files are `input.json`, byte-identical `input-original.json`, `assignment-original.txt`, and `task-original.json`. Literal selected source pages and indispensable proof continuations, exact file hashes, theorem versions, checked applications, and PDF-inspection records are generated by `extract_sources.py` into `source-extracts/`, especially `source-extracts/source-provenance.json`. The three inspected decisive PDF pages are retained as PNGs. The theorem statements and all new applications are explained above; reading source artifacts is not needed to see the logical dependencies or the unresolved gaps.

Run `python extract_sources.py` to regenerate literal excerpts and provenance, and `python render_sources.py` for the three inspected PDF-page images and actual rendering diagnostics. Run `python build_deliverables.py` to generate the standalone `P03.2-paper.tex` from this entire argument and compile it twice with the already installed TeX environment. The TeX file embeds the entire mathematical argument and contains no input of the Markdown file or source excerpt files. Build outputs and environment details are retained in `build-diagnostics.json`, the two build-pass stdout files and compiler logs, and `environment.json`. `status.json` has exactly the five requested fields.

The available environment has Python 3.12.14, pandoc, pdfTeX (TeX Live 2025/dev/Debian), pdftotext, and pdftoppm. No installation, network request, external message, model invocation, worker, or heavy computation is used. The requested native execution route is not independently attested by a model/account inspection. The managed-environment status capability was not exposed; no runtime configuration was altered. Source hashes, file checks, and TeX compilation are reproducibility evidence, **not mathematical proof certificates**. These are unverified draft proofs depending on the explicitly checked published foundations.


# Every actual native canonical note

[
  {
    "id": "n1",
    "summary": "CLD v2 denotes the July 2025 paper version, not ordinal stage 2. Checked ordinary approximation gives stage 1 for LFS and stage 2 for interior semipositive real PL; GJR curve regularization supplies weakly smooth nets and needs additional arguments.",
    "detailedSummary": "CD Definition 8.1.1 and Lemma 8.1.4 use ordinary smooth positive functions and decreasing sequences. GJR 15.11 requires a boundaryless rig-smooth curve and gives a decreasing net of weakly smooth psh functions. Its Remark 15.10 identifies these with ordinary smooth functions under a residue-field or local-genus hypothesis. GJR 7.10 requires an interior point; its common-neighborhood uniform LFS approximation safely yields ordinal stage 2 for semipositive real PL, without flattening the two approximation operations.",
    "text": "These are checked published foundations and fresh stage bookkeeping. CD denotes the supplied arXiv:1204.6277v2 PDF, dated 25 July 2025. Definition 8.1.1 (p.195) defines the smallest subsheaf containing ordinary smooth q with d'd''q≥0 and closed under decreasing sequences. Lemma 8.1.4 (p.196) defines Psh_0 as those smooth functions, Psh_{α+1} by local decreasing sequential limits of Psh_α, and limit stages by local membership in earlier stages. Thus paper version v2 and ordinal stage 2 are distinct. Current positivity or classical pshness does not alone establish membership in a specified ordinal stage.\n\nCD 12.4.1/12.4.6 supplies the canonical refined analytic G-tropical structure. CD 15.1.1(b)/15.1.2 describes ordinary smooth functions through ordinary open local expressions φ(-log|g_1|,…,-log|g_r|), with analytic units and smooth φ. G-local real PL and harmonic tropicalizations cannot replace this ordinary smoothness. CD 15.7.1 associates the tropical structure to a Hausdorff pure-dimensional analytic space with its actual analytic boundary; 15.7.2 records the boundary formula for domains. CD 12.4.5 and 8.1.5 preserve each ordinal stage under analytic morphisms, including scalar projections between different complete fields. On boundaryless tropical spaces, CD 8.3.1(b) converts current positivity into positive d'd'' forms for ordinary smooth functions.\n\nGJR denotes the supplied arXiv:2111.05741. Definition 5.1 defines real PL using G-local real combinations of unit log norms. Definition 7.8 and 7.9 make LFS a semipositive real-PL class and supply ordinary local expressions as nonnegative combinations of finite maxima of negative log norms of analytic units. For each maximum, on its fixed ordinary neighborhood, use M_ε=ε log Σ exp(ℓ_i/ε). It satisfies 0≤M_ε−max ℓ_i≤ε log N, has positive Hessian, and ∂M_ε/∂ε=−Σp_i log p_i≥0. Consequently ε↓0 gives a decreasing ordinary smooth positive sequence. Finite nonnegative combinations preserve this construction. Thus LFS functions belong locally to Psh_1.\n\nGJR Proposition 7.10 (pp.47–48) requires an interior point. Its proof produces a common ordinary open tube U=red^{-1}(V') and LFS h_i converging uniformly to a semipositive real-PL h. Choose ||h_{i_j}−h||_U≤e_j=4^{-j} and set b_j=h_{i_j}+2e_j. Then h+e_j≤b_j≤h+3e_j and b_{j+1}≤h+3e_{j+1}<h+e_j≤b_j. Each b_j belongs to stage 1, so b_j↓h proves stage 2. Each inner smooth sequence has a fixed ordinary neighborhood; the outer sequence is defined on U. A single smooth sequence on U approximating h is not proved by this argument.\n\nGJR Proposition 15.11 (pp.80–81) explicitly assumes a smooth curve, meaning rig-smooth without boundary. It produces a decreasing net of weakly smooth psh functions on any relatively compact ordinary open subset. Remark 15.10 identifies weak and ordinary smooth sheaves when the residue field is algebraic over a finite field, or the curve is potentially locally P1. Remark 10.10 identifies its ordinary smooth sheaf with the CLD ordinary sheaf. After this identification, positive weak currents restrict to positive ordinary currents, and CD 8.3.1(b) gives stage-0 form positivity. Outside these cases harmonic germs can be non-smooth; this is not proof that stage 1 or 2 fails.\n\nFurther checked foundations are GRc=arXiv:2506.13548v2, 17 September 2025: Theorem 4.3 identifies semipositive real PL with classical psh on good strict spaces over nontrivially valued fields; Definition 4.1 quantifies over every analytic extension and curve morphism; Lemma 3.9 describes normalization over perfect fields; Theorems 6.1 and 6.4 give interior and Shilov maximum principles. In the supplied arXiv:2503.05513, the curve subharmonic real-PL/nef equivalence is Proposition 5.1, despite GRc's older cross-citation to Proposition 3.1. Thuillier Proposition 3.1.8(iii), printed p.62/PDF p.76, concerns increasing locally bounded subharmonic families. His Theorem 3.4.2 supplies decreasing families of subharmonic lisse functions, and Proposition 3.2.5 identifies these as G-local real PL, not ordinary CLD-smooth.\n\nAll six supplied PDF/text hash pairs matched. Seventy-five literal primary pages, including indispensable proof continuations, are retained in source-extracts/source-provenance.json. Actual PDF pages Thu 76, CD 196 and GJR 80 were visually inspected. Thu actually says 'famille croissante et localement bornée'; GJR actually says 'decreasing net', 'weakly smooth', and 'without boundary'. Run python extract_sources.py and python render_sources.py. Renderer diagnostics are retained, including Thu's Type-3 glyph warnings. Hashes and rendering success are provenance evidence, not mathematical proof certificates.\n\nArtifacts: /workspace/research/campaigns/round-39/P03.2-public-source-CLD-envelope-stages/artifacts/codex-R08Ljj",
    "support": []
  },
  {
    "id": "n2",
    "summary": "Full-union envelopes have ordinary CLD stage 1 on boundaryless reduced good strict pure curves with bijective normalization over perfect countably dense fields whose residue is algebraic over a finite field. This includes positive-genus curves over Qp. Without the residue/genus hypothesis the checked route gives only stage 3.",
    "detailedSummary": "For every usc obstacle, finite maxima containing a baseline make the entire normalized competitor family locally bounded on both sides. Thuillier's supremum theorem gives a subharmonic regularized envelope. Countable local topology extracts a sequence from a decreasing continuous net on a fixed ordinary neighborhood. Under the residue hypothesis, GJR's approximants are ordinary smooth, yielding stage 1. They descend through homeomorphic normalization because ordinary smooth functions are locally constant at rigid points. All analytic extensions and curve pullbacks preserve the bound. Without ordinary/weak sheaf equality, the real-PL regularization and stage-2 approximation lemma yield stage 3, not stage 2.",
    "text": "Theorem. Let K be complete, nontrivially valued and perfect, with a countable dense subset. Let X be a nonempty reduced, separated, good, strictly K-analytic curve pure of dimension one, with ∂X=∅ and normalization ν:X̃→X bijective on Berkovich points. If the residue field K̃ is algebraic over a finite field, then for EVERY usc f:X→R∪{−∞}, the usc regularization u of the supremum over the FULL real-valued locally-Fubini–Study/semipositive-real-PL minorant union belongs to Psh_{X,1}⊂Psh_{X,2}. At every point it is a decreasing sequence of finite ordinary CLD-smooth functions with positive d'd'' on one ordinary neighborhood. The same conclusion holds under the alternative hypothesis that X̃ is potentially locally P1. Without either residue/genus hypothesis, the proof below establishes only Psh_{X,3}.\n\nFull-family supremum step. If the family is empty, both envelopes are −∞, approximated by the smooth constants −j. Otherwise choose one competitor h_0. Every competitor is finite continuous and classically psh by n1. Therefore f is finite everywhere and locally upper bounded. Also h_0≤s≤u≤f, the last inequality following from usc of f. GRc Lemma 3.9 makes X̃ rig-smooth and boundaryless. Since ν is a bijective topological quotient, it is a homeomorphism. Pull back the entire family, direct finite subsets containing h_0 by inclusion, and take their maxima. These are subharmonic and locally bounded below by h_0∘ν and above by f∘ν. They need not be real PL; no real-PL maximum closure is assumed. Thuillier 3.1.8(iii) makes (s∘ν)* subharmonic. Homeomorphic regularization gives (s∘ν)*=u∘ν. This treats the entire family without a modulus or invariance restriction.\n\nSequence extraction. A strict K-affinoid algebra is separable as a Banach space because countably many Tate polynomials with coefficients in a countable dense subset of K have dense images. The inequality | |a(x)|−|b(x)| |≤||a−b|| shows that countably many evaluations generate the topology and separate points of its spectrum. The compact spectrum embeds in a countable product of compact real intervals, hence is second countable. A relatively compact ordinary open W in a good Hausdorff space is covered by finitely many interiors of affinoid neighborhoods of its compact closure, so is second countable. For a decreasing directed net a_i of continuous functions with infimum v on W, {v<t}=⋃_i{a_i<t} is open and Lindelof. Choose a countable subcover for each rational t, enumerate all chosen indices, and successively take dominating indices. This gives a decreasing sequence on the SAME W. If its limit exceeded v at a point, an intermediate rational threshold and its chosen covering index would contradict that inequality. Thus the sequence converges to v, including where v=−∞.\n\nStage 1. On a relatively compact ordinary neighborhood W̃ in X̃, GJR 15.11 gives a decreasing net of finite weakly smooth psh functions converging to u∘ν. The residue hypothesis, or the stated potentially-local-P1 hypothesis, makes these ordinary smooth by GJR 15.10. Their positive ordinary currents give positive ordinary forms by CD 8.3.1(b), so they are stage 0. Extract an actual decreasing sequence on W̃.\n\nOrdinary smooth descent. Normalization is an analytic isomorphism off a discrete set of non-normal rigid points. An ordinary smooth function is locally constant at a rigid point, including one with a finite residue extension. To prove this, let g be an analytic unit at such a point z, α=g(z), ρ=|α|>0, and P its monic minimal polynomial of degree d. All conjugate roots have modulus ρ because K is complete. On the ordinary neighborhood |P(g)|<ρ^d, if |g(y)|≠ρ then, after algebraic extension of H(y), every root difference has modulus max(|g(y)|,ρ), giving |P(g(y))|≥ρ^d, a contradiction. Hence |g| is constant there. Apply this to the finitely many units in an ordinary smooth moment expression. Transfer each normalized approximant through the homeomorphism. Away from non-normal points it is smooth and positive by analytic isomorphism; at those points it is constant on an ordinary neighborhood, hence smooth with zero d'd''. Thus the transferred functions are stage 0 on W=ν(W̃), and decrease to u. This proves stage 1. Induction gives the same descent for the finite ordinal stages used below.\n\nGeneral residue fields. Thuillier 3.4.2 supplies a decreasing net of continuous subharmonic lisse functions on W̃. They are real PL by Proposition 3.2.5 and semipositive by the supplied GRs Proposition 5.1. The interior lemma in n1 places each in stage 2. Extracting a decreasing sequence gives stage 3; descent gives Psh_{X,3}. No collapse to stage 2 is justified.\n\nScalar and curve quantifiers. For EVERY complete analytic extension K'/K and analytic curve morphism g:C→X_{K'}, CD 12.4.5/8.1.5 preserves the proved ordinal bound for u∘π∘g. The ordinary smooth sequences and all their decreasing limits pull back. Smooth psh curve functions are subharmonic, and decreasing limits remain so, as checked in GRc §1.2 and Proposition 3.5. This also gives scalar-stable classical pshness, including −∞ in the extended convention. Neither openness of scalar projection nor equality of envelopes for enlarged scalar-extension competitor families is asserted or needed.\n\nThis is a noninvariant full-family sector covering boundaryless ordinary open domains in smooth elliptic and higher-genus curves over Qp. It is not a rational-tree example or selected invariant family. Continuity is not asserted. The sufficient field hypotheses are not shown necessary; relative-boundary points and arbitrary imperfect perfected-unibranch descent remain unresolved.\n\nThe entire argument is retained in P03.2-argument.md and standalone P03.2-paper.tex. Run python build_deliverables.py and python verify_artifacts.py. Both final TeX passes returned 0, with no overfull warnings and two underfull paragraph warnings per pass. These checks do not establish mathematical correctness.\n\nArtifacts: /workspace/research/campaigns/round-39/P03.2-public-source-CLD-envelope-stages/artifacts/codex-R08Ljj",
    "support": [
      "n1"
    ]
  },
  {
    "id": "n3",
    "summary": "Every noninvariant full-union obstacle envelope on an ordinary locally trivial projective-space bundle reduces exactly to a base envelope. The curve sector in n2 therefore gives ordinary stage 1 in higher dimension.",
    "detailedSummary": "Every competitor is constant on compact connected projective fibers by the scalar-stable classical maximum principle. Ordinary local sections descend both competitor branches, and pullback gives the converse. For any usc obstacle F, its fiberwise infimum g is usc because the smooth bundle projection is open. Raw envelopes and their regularizations are exact pullbacks, including empty families. The stage-1 curve sector and its broader stage-3 counterpart propagate through projective factors and finite bundle towers. The exact reduction permits base boundary, but supplies no missing positive boundary theorem.",
    "text": "Exact reduction theorem. Let K be complete and nontrivially valued. Let X be any good separated strict K-analytic space, allowing relative boundary. Let p:Y→X be a good separated projective-space bundle locally analytically trivial on ORDINARY open subsets, with fiber P^{m,an}, m≥1. For every usc F:Y→R∪{−∞}, put g(x)=inf_{p^{-1}(x)}F. Then g is usc, and for the FULL LFS/semipositive-real-PL union, s_F^Y=s_g^X∘p and (s_F^Y)*=(s_g^X)*∘p, including empty families.\n\nProof. Every competitor h is finite continuous and classically psh by n1. Restrict it to the fiber over x, viewed as analytic projective space over H(x), using scalar extension and analytic pullback. This fiber is compact, connected and boundaryless. Connectedness follows from its m+1 standard closed unit-polydisc domains: each is connected because a clopen partition would glue a nontrivial analytic idempotent into its Tate algebra, which is a domain; all contain (1:…:1). They cover projective space by choosing a largest homogeneous coordinate. The restriction of h attains a maximum. Its maximum set is closed by continuity and open by GRc's interior local maximum principle. Connectedness makes it the whole fiber. Thus EVERY competitor is fiberwise constant, without a symmetry assumption.\n\nWrite h=b∘p. On each ordinary trivializing open, restrict h along the analytic section (1:0:…:0). LFS expressions pull back to LFS expressions; GJR 5.4/7.6 preserves real PL and semipositivity for the other branch. These local functions agree by fiberwise constancy and give a global b in the same branch. Conversely p*b preserves either branch. This is an exact correspondence, and h≤F is equivalent to b≤g.\n\nThe projection p is smooth and surjective, hence open by Berkovich's supplied IHES 1993 paper, Corollary 3.7.4, applied to its ordinary local projective-space trivializations and relative affine charts. Therefore {g<t}=p({F<t}) is open for each real t, proving usc. The argument allows g=−∞, even when F is pointwise finite. The competitor correspondence proves raw equality, including empty families.\n\nFor a continuous open surjection p and raw extended function a, (a∘p)*=a*∘p. Continuity gives the upper inequality by pulling back base neighborhoods. Openness gives the lower inequality because the image of every neighborhood of a chosen lift is a base neighborhood. The neighborhood-supremum formula works also at −∞. Applying it to the raw identity proves regularized equality.\n\nIf X satisfies n2's residue-field curve theorem, every full envelope on Y belongs to ordinary stage 1, hence stage 2: pull back the actual decreasing smooth sequence for the usc obstacle g. Its members are ordinary smooth and positive on the common ordinary neighborhood p^{-1}(W), and decrease to the actual full envelope. All analytic extensions and curve tests preserve this bound. If only n2's broader curve hypotheses hold, the proved bound is stage 3. Finite towers follow by repetition because each effective obstacle remains usc. Products X×P^{m,an} are included; normal curve bases give normal higher-dimensional spaces.\n\nThe positive conclusion uses a boundaryless base from n2; the total space is boundaryless because the projection is boundaryless. The exact reduction itself allows a base boundary and does not manufacture a curve boundary-approximation theorem. Arbitrary normal domains, open-disc products and general proper fibrations without ordinary local sections remain outside this sector. All noninvariant obstacles and competitors are admitted; proper fibers force descent rather than selecting an invariant subfamily.\n\nThe full proof is embedded in P03.2-argument.md and P03.2-paper.tex. Literal Berkovich openness/local-structure pages and checked applications are retained in source-extracts/source-provenance.json. Rerun python extract_sources.py and python build_deliverables.py.\n\nArtifacts: /workspace/research/campaigns/round-39/P03.2-public-source-CLD-envelope-stages/artifacts/codex-R08Ljj",
    "support": [
      "n1",
      "n2"
    ]
  },
  {
    "id": "n4",
    "summary": "A fresh split-node calculation proves full-envelope failure for a continuous obstacle, on both an affinoid curve and its boundaryless interior, and after projective factors in every higher dimension. The original sharp P03.2 classification remains open.",
    "detailedSummary": "On Z=M(K〈x,y〉/(xy)), set a=−log|π|>0, r=|π|, and take obstacle 0 on the x-branch and −a min(|y|/r,1) on the y-branch. The radius-r disc maximum principle bounds every competitor by −a on the y-branch. Explicit LFS minorants show the exact raw envelope is 0 on the punctured x-branch and −a elsewhere. Regularization raises the node to 0, violating the y-disc Shilov maximum principle and every CLD ordinal stage. This works on Int(Z) and propagates through projective factors. It does not establish sharp necessity or resolve broader normal geometry. Deliverables, source extracts and two successful TeX builds are retained; candidate is false.",
    "text": "Fresh counterexample with a complete full-family calculation. Let K be complete and nontrivially valued, choose π with 0<|π|<1, and put a=−log|π|>0 and r=|π|. Let Z=M(K〈x,y〉/(xy)), with node o and branches D_x,D_y. Let V be either Z or its boundaryless interior Int(Z), whose branches are open unit discs joined at o. Define f=0 on D_x∩V and f=−a min(|y|/r,1) on D_y∩V. Both branch values equal 0 at o, so f is finite continuous by nodal gluing.\n\nEvery member h of the FULL LFS/semipositive-real-PL minorant union restricts to a classically psh function on the closed y-disc of radius r. This strict affinoid disc lies inside either V. Its singleton Shilov point η_r satisfies h(η_r)≤f(η_r)=−a. The Gauss seminorm dominates every point seminorm on each analytic power series, verifying its Shilov property. GRc Theorem 6.4 gives h≤−a throughout the disc, including o. Outside it, f is already −a. Thus all competitors are ≤−a on the entire y-branch.\n\nDefine h_n=max(−a,n^{-1}log|x|) on the x-branch and h_n=−a on the y-branch, giving o value −a. These are finite continuous LFS functions. On a nodal neighborhood with both branch radii <|π|^n they are constant. Away from o on the x-branch, x is a unit and h_n=n^{-1}max{−log|π^{-n}|,−log|x^{-1}|}, an ordinary local LFS expression. On the y-branch they are constant. They satisfy h_n≤f. At every punctured x-branch point log|x| is finite and h_n→0, while f gives the upper bound 0. On the y-branch they attain the established upper bound −a. Hence the exact raw envelope is s=0 on (D_x∩V)\\{o} and s=−a on D_y∩V, including o.\n\nUsc regularization changes only o to value 0. Its pullback to the closed y-disc has value 0 at the origin and −a at the singleton Shilov point, contradicting the psh maximum principle. It is not classically psh and belongs to no CLD ordinal psh stage: ordinary smooth curve psh functions are subharmonic, decreasing limits preserve subharmonicity, and the transfinite local construction preserves the scalar-stable classical class. This branch obstruction already occurs without relative boundary when V=Int(Z); choosing V=Z also checks the affinoid-boundary setting.\n\nFor V×P^{m,an} with obstacle f∘p, n3's exact reduction gives the regularized envelope u∘p. A projective-space section and the same closed y-disc witness failure in dimension m+1 for every m≥1. No dossier book assertion, earlier generated counterexample or review verdict is used.\n\nOriginal obligations remain open. The sectors in n2 and n3 are sufficient, not a sharp classification. Necessity of residue-field, countability and boundarylessness assumptions is not proved. Non-smooth harmonic germs do not imply absence from stage 1 or 2. The broader curve construction reaches stage 3, and reducing it to ordinal stage 2 needs another ordinary approximation argument. Imperfect perfected-unibranch descent, positive approximation at relative-boundary points, arbitrary normal/geometrically-unibranch higher-dimensional domains and open-disc products are unresolved. No fresh proof is supplied for the dossier's nonsplit-node surface or codimension-two pinching assertions, and they were not imported. Scalar pullback positivity of every proved envelope is established, but enlarged scalar competitor-family identities are not asserted. No continuity or P03.1/P03.3 classification is claimed. Therefore the original sharp P03.2 target remains open and candidate=false.\n\nDeliverables are P03.2-argument.md, standalone P03.2-paper.tex and P03.2-paper.pdf. Original input.json, byte-identical input-original.json, assignment-original.txt and task-original.json are retained. status.json has exactly id,status,exact_result,proof_file,concrete_gaps. Source extracts and checked applications are in source-extracts/source-provenance.json. Run python extract_sources.py, python render_sources.py, python build_deliverables.py and python verify_artifacts.py. Both final pdflatex passes returned 0, with no overfull warnings and two underfull paragraph warnings per pass. environment.json, build-diagnostics.json, compiler/stdout logs and artifact-checks.json retain actual evidence. Artifact checks verified six source pairs, 75 literal pages, original input identity, standalone TeX and exact status keys. These are unverified draft mathematical arguments; hashes, administrative checks and compilation are not mathematical certificates. No heavy computation, installation, worker/model invocation, external message or runtime/auth change was used.\n\nArtifacts: /workspace/research/campaigns/round-39/P03.2-public-source-CLD-envelope-stages/artifacts/codex-R08Ljj",
    "support": [
      "n1",
      "n3"
    ]
  }
]

# Root mathematical gap check on this exact final proof

# Final R39 proof gap: Theorem C is not verified

The completed final core has SHA-256 4a4e66e6544c4ce2c9b2224e6f46d6cc2eb326ee769cb8be0d799e2491d67c38. Its proof of Theorem C still identifies every Thuillier-lisse subharmonic approximant with a strict GJR real-PL function. Actual canonical notes n1 and n2 retain that premise, and n3 imports its stage-3 conclusion. The complete final diff changes scope purity, formatting, the disc Shilov justification and reproduction instructions; it does not repair this premise.

The following independently constructed preliminary gap proof applies unchanged to the final mathematical step. Its historical observations about a running author refer to the preliminary snapshot. Both authors have now completed; no feedback was sent.

# A gap in the preliminary R39 subsidiary stage-3 proof

This local root check concerns only the preliminary P03.2 argument with SHA-256 `c5b1c2eff25878db35adfe2155fc52e0fed5e21bd26126fa5561b22f029ba7f6`. The author is still running. No feedback, mutation of its workspace, model submission, or acceptance has occurred. The final argument and canonical notes must be checked separately for revisions.

The preliminary proof of Theorem C says that the Thuillier-lisse functions in its decreasing approximation net are real PL in the **strict GJR sense**, because Thuillier Proposition 3.2.5 describes them as G-local real combinations of logarithms of analytic units. This identification is unjustified and is false as a blanket statement.

## The two G-sites differ

Thuillier's definition of \(X_G\), in the public thesis LF1424–1468, uses all analytic domains and covers refinable by locally finite families of \(k\)-affinoid domains. It separately defines the rigid site \(X_R\) using strictly analytic domains. Proposition 3.2.5, LF4177–4221, concerns the former \(X_G\): its unit-logarithm sheafification may use non-strict domains.

GJR Definition 5.1 and the standing convention immediately preceding it, on PDF30–31 of arXiv:2111.05741, use the G-topology generated by **strictly affinoid** domains. GJR Example 5.3 explicitly shows that the maximum of two real-PL functions need not remain in this strict real-PL class when its bend has an irrational coordinate.

## Concrete counterexample to the imported premise

Let \(K\) be the completed algebraic closure of \(\mathbb Q_p\), with absolute value normalized so that \(-\log|p|=1\). Its additive value group is \(\Gamma=\mathbb Q\). On \(X=\mathbb G_{m,K}^{\mathrm{an}}\), put
\[
\ell(t)=\pi\log|t|+1,
\qquad \varphi(t)=\max\{0,\ell(t)\}.
\]
Here \(\pi\) denotes the usual positive real number. In the coordinate \(s=-\log|t|\), \(\varphi\) bends at \(s=1/\pi\notin\Gamma\). This is exactly the phenomenon in GJR Example 5.3: \(\ell\) is strict real PL, while \(\varphi\) is not strict real PL near that bend.

On a compact strict annulus containing the bend, cut instead at the radius \(r_0=e^{-1/\pi}\). The two closed subannuli are valid **non-strict** analytic domains and form a finite admissible cover. On one, \(\varphi=0\); on the other, \(\varphi=\ell\). Both formulas are real linear combinations of logarithms of analytic units and constants. A real constant is such a combination because \(K\) is nontrivially valued. Thus Thuillier Proposition 3.2.5 puts \(\varphi\) in the Thuillier-lisse sheaf locally at the bend. Restricting to the ordinary interior of the annulus gives the corresponding ordinary local example.

It is also subharmonic. The functions \(0\) and \(\ell\) are ordinary smooth affine moment functions, with zero \(d'd''\), and hence classically psh. Finite maxima preserve classical pshness by GR arXiv:2506.13548v2, Proposition 4.2; on the smooth curve this agrees with Thuillier subharmonicity. Equivalently, the finite maximum admits the explicit decreasing ordinary smooth log-sum-exponential approximation.

Therefore a Thuillier-lisse **subharmonic** function need not be a strict GJR semipositive real-PL function. One cannot apply GJR Proposition 7.10 to every member of that net without another strict real-PL realization or approximation argument.

This example does not disprove the desired envelope positivity. Indeed both \(0\) and \(\ell\) are genuine global semipositive real-PL minorants of the obstacle \(\varphi\). They already force the full raw envelope to equal \(\varphi\), which is in ordinal stage1 by the explicit smooth maximum approximation. The example refutes the imported identification, not the conclusion of Theorem C.

## Scope of the finding

Theorem A's separate countable extraction from GJR15.11, under ordinary/weak smooth sheaf coincidence, does not use this identification. Neither do its smooth normalization descent or projective-bundle reduction. Those parts still require final-source and canonical review, but this gap alone does not refute them.

A repair of Theorem C would need actual strictly admissible approximation of the Thuillier-lisse subharmonic functions, including common ordinary neighborhoods, semipositivity and a decreasing **sequence** of stage2 sections. Merely naming the two G-sheaves, moving a graph breakpoint without controlling the slope signs, or adding an extra uncounted limiting operation does not repair the ordinal-stage proof. No such repair is claimed in this note.


Final disposition: no acceptance of Theorem C or its stage-3 bundle consequence. The separate Theorems A/B and the split-node calculation do not use this premise, and were reconstructed separately; independent review is still pending. The conclusion of Theorem C is not disproved by this example. No original target is closed.


# Published source versions, provenance and application checks

{
  "purpose": "Literal primary-source pages with checked applications; provenance is not a mathematical certificate.",
  "sources": [
    {
      "public_source": "https://arxiv.org/pdf/2506.13548v2",
      "pdf": "/workspace/research/shared-sources/GR-2506.13548v2-20261004.pdf",
      "pdf_sha256": "83ca9a19394f44bb2e4e1aa316de95938f311acd53a00fe250fa0f605184b726",
      "literal_extract": "/workspace/research/shared-sources/GR-2506.13548v2-20261004.txt",
      "extract_sha256": "3a221b86116604c950db07e4c60ab184701f0624deebabd92502e5c81871436b",
      "origin": "Published primary mathematical source, not generated research.",
      "id": "GRc",
      "pages": [
        2,
        3,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        21,
        22,
        23,
        29,
        30,
        31,
        32,
        33,
        34,
        35
      ],
      "version": "arXiv v2, 17 September 2025",
      "applications": [
        "3.4/3.4.1/3.5 and proofs: extended -infinity convention, smooth-curve subharmonicity, scalar stability, curve functoriality and decreasing limits.",
        "3.9 and entire proof: reduced strict curve; perfect field; normalization rig-smooth, quotient topology, non-normal rigid points, boundaries.",
        "4.1/4.2/4.3 and proofs: all analytic extensions and curve tests; semipositive RPL iff classical psh.",
        "6.1 and proof: interior maximum principle, applied on proper connected projective-space fibers.",
        "6.4 and proof: singleton-Shilov maximum principle, used in fresh split-node calculation."
      ],
      "verified_hashes": true,
      "literal_pages": [
        {
          "pdf_page": 2,
          "file": "source-extracts/GRc/pdf-page0002.txt",
          "sha256": "e6c0a94411500bb16f7b263b50ffdf534401743c89816090ba8591dc75ab566b",
          "literal": true
        },
        {
          "pdf_page": 3,
          "file": "source-extracts/GRc/pdf-page0003.txt",
          "sha256": "4c949405566cc5a6dff86ba7f74f816576afe51b9c62c296f4b686373e8f8f10",
          "literal": true
        },
        {
          "pdf_page": 10,
          "file": "source-extracts/GRc/pdf-page0010.txt",
          "sha256": "1c941ec581ff4e1712be17af6da299996380868b7b1cc5c94ca3f4456614cc76",
          "literal": true
        },
        {
          "pdf_page": 11,
          "file": "source-extracts/GRc/pdf-page0011.txt",
          "sha256": "a8a605a63d505d7de520e3592c747f99cfe520c5c7f069465c45bd3ca8bf6892",
          "literal": true
        },
        {
          "pdf_page": 12,
          "file": "source-extracts/GRc/pdf-page0012.txt",
          "sha256": "4e8067f90cd92858aea0ab44504846af49538cdaffe24671e27593b015a10060",
          "literal": true
        },
        {
          "pdf_page": 13,
          "file": "source-extracts/GRc/pdf-page0013.txt",
          "sha256": "a78242a14c250fd317d1b00aac6cace9c0a5d458da9bd41d9736caee81b2cfe7",
          "literal": true
        },
        {
          "pdf_page": 14,
          "file": "source-extracts/GRc/pdf-page0014.txt",
          "sha256": "816ee0d142ad94983263a40d7cd67ef2afeba3fe2c751fe9cc0c4aa9de9b66bc",
          "literal": true
        },
        {
          "pdf_page": 15,
          "file": "source-extracts/GRc/pdf-page0015.txt",
          "sha256": "82b0858e6e0e69f6247005dc18ddefab28abf74d4dc426153dfcba4c716b37f6",
          "literal": true
        },
        {
          "pdf_page": 16,
          "file": "source-extracts/GRc/pdf-page0016.txt",
          "sha256": "e5420585f415ff1d2a48e10e62b1349d8992305de38255c74bf661a8b7be9e64",
          "literal": true
        },
        {
          "pdf_page": 17,
          "file": "source-extracts/GRc/pdf-page0017.txt",
          "sha256": "b7bb761938da5c12f9afd7b90f7e62594e7211f058b0bbf783777824b46e2c20",
          "literal": true
        },
        {
          "pdf_page": 18,
          "file": "source-extracts/GRc/pdf-page0018.txt",
          "sha256": "76fc8a1ea9f4433b8caeb28cde4e1dd45ebe167fbb1b6864f39f5f4d5dc811f9",
          "literal": true
        },
        {
          "pdf_page": 21,
          "file": "source-extracts/GRc/pdf-page0021.txt",
          "sha256": "820cce17e7bafe3746e0e59150d0a98cb7a070832a4f6731ff2109942b63a9a7",
          "literal": true
        },
        {
          "pdf_page": 22,
          "file": "source-extracts/GRc/pdf-page0022.txt",
          "sha256": "12de51b8102a4ea09f23a92407e01734b60aecf4dc65d919edfccf63d7bee3fd",
          "literal": true
        },
        {
          "pdf_page": 23,
          "file": "source-extracts/GRc/pdf-page0023.txt",
          "sha256": "d9424c12897c66bf794c303dd5f6a6362dcf63e991e459618c9207f8cd53e682",
          "literal": true
        },
        {
          "pdf_page": 29,
          "file": "source-extracts/GRc/pdf-page0029.txt",
          "sha256": "00f76b4aaa8a9c5d77d527a5d7678a25d974b6b3670894de9f7bba8855674557",
          "literal": true
        },
        {
          "pdf_page": 30,
          "file": "source-extracts/GRc/pdf-page0030.txt",
          "sha256": "4fcca2835bab85572ea9eb5bc15b88bd27ced898c7387e6e89d02b60ecdc131d",
          "literal": true
        },
        {
          "pdf_page": 31,
          "file": "source-extracts/GRc/pdf-page0031.txt",
          "sha256": "c9a339caa6767c72b0f5588c8c754e5d58ce99743b518ee878e58c675f8e1770",
          "literal": true
        },
        {
          "pdf_page": 32,
          "file": "source-extracts/GRc/pdf-page0032.txt",
          "sha256": "3fe7eb2dbf807e2fd4ca2ac2198aa6b2657d81a6061f658ea57cd8918870d263",
          "literal": true
        },
        {
          "pdf_page": 33,
          "file": "source-extracts/GRc/pdf-page0033.txt",
          "sha256": "b5fb4d3dcde384fbda5c5c9668b22686965298ee02b2e1aae3947218deba32bd",
          "literal": true
        },
        {
          "pdf_page": 34,
          "file": "source-extracts/GRc/pdf-page0034.txt",
          "sha256": "c8a880a346d907b4789080a6784ba89ac6269e6b71996b9e3728299fc05af61b",
          "literal": true
        },
        {
          "pdf_page": 35,
          "file": "source-extracts/GRc/pdf-page0035.txt",
          "sha256": "5027c29e4cd3ea12d48b02c138d2acc7c1392b6201d60b8c3a5c86bc93764c0c",
          "literal": true
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
      "id": "GRs",
      "pages": [
        4,
        5,
        15,
        16,
        17
      ],
      "version": "exact supplied arXiv:2503.05513 version",
      "applications": [
        "5.1 and full proof: smooth strict curve RPL subharmonic iff nef residue. Current numbering is 5.1, not the older 3.1 cross-citation."
      ],
      "verified_hashes": true,
      "literal_pages": [
        {
          "pdf_page": 4,
          "file": "source-extracts/GRs/pdf-page0004.txt",
          "sha256": "31eb3c67599af127e038785ea86e4a17350952f6775a8f7beba3787aee689907",
          "literal": true
        },
        {
          "pdf_page": 5,
          "file": "source-extracts/GRs/pdf-page0005.txt",
          "sha256": "cddc14223ce1a2f0543db0ffa76e9fe9b7fa980fb2b718855862050d18232f2b",
          "literal": true
        },
        {
          "pdf_page": 15,
          "file": "source-extracts/GRs/pdf-page0015.txt",
          "sha256": "cb2193be1cd71d0f6b7df6eaeded923f8fc8578b1aee8fc765c7cc3e83fe481e",
          "literal": true
        },
        {
          "pdf_page": 16,
          "file": "source-extracts/GRs/pdf-page0016.txt",
          "sha256": "d6ea98f6e7709a86b1cdc679db40d2efbeaa4529dc3e84f8ef366684278cc371",
          "literal": true
        },
        {
          "pdf_page": 17,
          "file": "source-extracts/GRs/pdf-page0017.txt",
          "sha256": "350e1328a92ac311b8534d6d2bf553a27068a222b780164aa10e733cebec94e4",
          "literal": true
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
      "id": "Thu",
      "pages": [
        15,
        16,
        71,
        72,
        73,
        76,
        77,
        82,
        83,
        84,
        103,
        104,
        105
      ],
      "version": "HAL tel-00010990v1 thesis",
      "applications": [
        "3.1.8(iii), printed 62/PDF 76: increasing locally bounded family. The new application uses two-sided local bounds from a baseline and usc obstacle.",
        "2.3.21/2.3.22 and proofs: harmonic/log-unit sheaf distinction and residue/genus hypotheses.",
        "3.2.4/3.2.5 and proofs: Thuillier lisse is G-local real PL, not ordinary CLD smooth.",
        "3.4.2 and full proof, printed 89-90/PDF 103-104: decreasing family of subharmonic lisse functions on relatively compact ordinary opens.",
        "3.4.5 and proof: scalar stability of smooth-curve subharmonicity."
      ],
      "verified_hashes": true,
      "literal_pages": [
        {
          "pdf_page": 15,
          "file": "source-extracts/Thu/pdf-page0015.txt",
          "sha256": "3e0a0b00c56242089bde6af7c321e9e6605c0b357f7c00174b4340399ede9a3f",
          "literal": true
        },
        {
          "pdf_page": 16,
          "file": "source-extracts/Thu/pdf-page0016.txt",
          "sha256": "6c3fb32527531507542a06061469bfe5a093cf790cda1cdf9a0bfc2b9afd8fd5",
          "literal": true
        },
        {
          "pdf_page": 71,
          "file": "source-extracts/Thu/pdf-page0071.txt",
          "sha256": "d0e36e5ab8181ac9af6e2be2a6e0a1426fdc29063326c809a3a38be4aa6b9513",
          "literal": true
        },
        {
          "pdf_page": 72,
          "file": "source-extracts/Thu/pdf-page0072.txt",
          "sha256": "44b250cb426297b821c6978103ceb6e9344b9fc5df9a79c69c61cb69dc5c584f",
          "literal": true
        },
        {
          "pdf_page": 73,
          "file": "source-extracts/Thu/pdf-page0073.txt",
          "sha256": "f57a52e2f4a8d783f1a47f93c1c0c18ac9c9620bf4a133b2416accb726c6ed44",
          "literal": true
        },
        {
          "pdf_page": 76,
          "file": "source-extracts/Thu/pdf-page0076.txt",
          "sha256": "324008384af95330bc7280127159497f9c8121cd793553b415e113c956311b7e",
          "literal": true
        },
        {
          "pdf_page": 77,
          "file": "source-extracts/Thu/pdf-page0077.txt",
          "sha256": "e0370bcde26fcfd035c5864874a7c18e2a27be6ef1be8739f22d8cdefc00c8ce",
          "literal": true
        },
        {
          "pdf_page": 82,
          "file": "source-extracts/Thu/pdf-page0082.txt",
          "sha256": "82559198be47c9e4ad4ebcfadf41e7b0a553cbf084bff6ac37e4a73ee5c44e59",
          "literal": true
        },
        {
          "pdf_page": 83,
          "file": "source-extracts/Thu/pdf-page0083.txt",
          "sha256": "32ebe19759bbd036e23d9f89ca035132dde4241a34d71b049bb6311a99581d6c",
          "literal": true
        },
        {
          "pdf_page": 84,
          "file": "source-extracts/Thu/pdf-page0084.txt",
          "sha256": "a3f76efe15a703eccbcfbbd259a4c7b8bd887eaec26bb9e45b22376b0133006a",
          "literal": true
        },
        {
          "pdf_page": 103,
          "file": "source-extracts/Thu/pdf-page0103.txt",
          "sha256": "86fef36c1bdf192a700801fd2c2958ee81281f4031206e6018f5e988e07c21fd",
          "literal": true
        },
        {
          "pdf_page": 104,
          "file": "source-extracts/Thu/pdf-page0104.txt",
          "sha256": "691b77c4935e64bf395dd278a5d726df55eefda99ab02e3ba7a16fdc1e267756",
          "literal": true
        },
        {
          "pdf_page": 105,
          "file": "source-extracts/Thu/pdf-page0105.txt",
          "sha256": "f7ba9960c4751bded0eab0d09c6bd74ce075168e3a43b5f48ae2e03d80fa3acc",
          "literal": true
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
      "id": "GJR",
      "pages": [
        30,
        31,
        46,
        47,
        48,
        49,
        50,
        64,
        65,
        77,
        78,
        79,
        80,
        81
      ],
      "version": "exact supplied arXiv:2111.05741 version",
      "applications": [
        "5.1/5.4 and 7.6: real PL, semipositivity and their scalar/morphism pullbacks.",
        "7.8/7.9: LFS is semipositive RPL; ordinary local finite maxima of unit log norms.",
        "7.10 and full proof: interior point is required; common ordinary open tube with uniformly convergent LFS sequence. New stage bookkeeping gives stage 2.",
        "10.10: ordinary smooth sheaf is the CLD ordinary smooth sheaf.",
        "15.7: rig-smooth curve harmonic definitions agree; boundary cases distinguished.",
        "15.10: residue algebraic over finite field or potentially locally P1 implies ordinary/weak smooth equality; no necessity claim.",
        "15.11 and full proof: smooth means rig-smooth without boundary; decreasing net of weakly smooth psh functions on relatively compact ordinary opens."
      ],
      "verified_hashes": true,
      "literal_pages": [
        {
          "pdf_page": 30,
          "file": "source-extracts/GJR/pdf-page0030.txt",
          "sha256": "bc083c09bc82dafda20ec3525d73a2c5bc794581437bad133b1e97eb716ec666",
          "literal": true
        },
        {
          "pdf_page": 31,
          "file": "source-extracts/GJR/pdf-page0031.txt",
          "sha256": "0286959703f57c016523108761fe657f3f32a4a8d05746c3159f5a0b7226ba5d",
          "literal": true
        },
        {
          "pdf_page": 46,
          "file": "source-extracts/GJR/pdf-page0046.txt",
          "sha256": "23d00fd808ff70a1c1a87294a4cc947979768b62e6dab7165d01be4d4abf54c5",
          "literal": true
        },
        {
          "pdf_page": 47,
          "file": "source-extracts/GJR/pdf-page0047.txt",
          "sha256": "8c43decece427ba4bcd4a0f891306acf4bafd1d3be07e3c5fc6ead61b1380a73",
          "literal": true
        },
        {
          "pdf_page": 48,
          "file": "source-extracts/GJR/pdf-page0048.txt",
          "sha256": "508f91ff8493c0c8665c3af0c5e1b26d6aca91f7cbef9e2f70ac0ef6b105a095",
          "literal": true
        },
        {
          "pdf_page": 49,
          "file": "source-extracts/GJR/pdf-page0049.txt",
          "sha256": "bfc2258fff8e517d16fcfc24c9c11dc45f411f30b140807eec16b85e0e486622",
          "literal": true
        },
        {
          "pdf_page": 50,
          "file": "source-extracts/GJR/pdf-page0050.txt",
          "sha256": "a4bec1674ef100b3d5272e11216ea32166e6e53b27c2c65252c4e0d9937569eb",
          "literal": true
        },
        {
          "pdf_page": 64,
          "file": "source-extracts/GJR/pdf-page0064.txt",
          "sha256": "ac6c298246da5726c52952721c6760c1af303bea02163276993d5c7059e5aa18",
          "literal": true
        },
        {
          "pdf_page": 65,
          "file": "source-extracts/GJR/pdf-page0065.txt",
          "sha256": "8a3daf2155f6348995434d30da8df0a8069df98d5f7fefb55fce3e89c45a2e0a",
          "literal": true
        },
        {
          "pdf_page": 77,
          "file": "source-extracts/GJR/pdf-page0077.txt",
          "sha256": "923061c5e8fc59e1e861c53434793ea9b5cd742aa0a465e373093d81c4934593",
          "literal": true
        },
        {
          "pdf_page": 78,
          "file": "source-extracts/GJR/pdf-page0078.txt",
          "sha256": "585f759202bd2bf5d2f0da9b799c4bf42281ed8fdde816969e7230ca9bfa31f8",
          "literal": true
        },
        {
          "pdf_page": 79,
          "file": "source-extracts/GJR/pdf-page0079.txt",
          "sha256": "9a5892b5445ccdb4969fc287d2fd351953a2fed518169f969826bb7b38de1fe2",
          "literal": true
        },
        {
          "pdf_page": 80,
          "file": "source-extracts/GJR/pdf-page0080.txt",
          "sha256": "57ced0d50b7ed907aceb830a0845ffd65d94591551d18127c21504f5e7fc67b1",
          "literal": true
        },
        {
          "pdf_page": 81,
          "file": "source-extracts/GJR/pdf-page0081.txt",
          "sha256": "4c69527beea088270b0bc870bdd68f6cc84a0cf3e1df33eb23c0bc61fdbd8de2",
          "literal": true
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
      "id": "Ber",
      "pages": [
        73,
        74,
        75,
        76,
        77
      ],
      "version": "Publications Mathematiques IHES 78 (1993), 5-161",
      "applications": [
        "3.7.4: smooth morphisms are open; applied to ordinary locally trivial projective-space bundles, not scalar maps. Local structure statements and proof retained."
      ],
      "verified_hashes": true,
      "literal_pages": [
        {
          "pdf_page": 73,
          "file": "source-extracts/Ber/pdf-page0073.txt",
          "sha256": "fd09047f5d5f4688a5957eaf01296a291843c8208a12f346541fcfbcce5e95a7",
          "literal": true
        },
        {
          "pdf_page": 74,
          "file": "source-extracts/Ber/pdf-page0074.txt",
          "sha256": "52b2b7413e7eb7737cda68f619ea3d85a6516c1ee215d3bb12fd67ccdccee1e1",
          "literal": true
        },
        {
          "pdf_page": 75,
          "file": "source-extracts/Ber/pdf-page0075.txt",
          "sha256": "81d675f8715a52cc64b40bedf01386fe399147d161f60646aa5e9ef337e81cd8",
          "literal": true
        },
        {
          "pdf_page": 76,
          "file": "source-extracts/Ber/pdf-page0076.txt",
          "sha256": "144c10694be0f1c157c3ab671d449df803b5850cc54106020214af989d7f2d32",
          "literal": true
        },
        {
          "pdf_page": 77,
          "file": "source-extracts/Ber/pdf-page0077.txt",
          "sha256": "8210c78b6e87af4d1b290b359c3eebea2823a1f57a6698232a648caa67ed197e",
          "literal": true
        }
      ]
    },
    {
      "public_source": "https://arxiv.org/pdf/1204.6277v2",
      "pdf": "/workspace/research/shared-sources/CD-1204.6277v2-20261004.pdf",
      "pdf_sha256": "5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719",
      "literal_extract": "/workspace/research/shared-sources/CD-1204.6277v2-20261004.txt",
      "extract_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085",
      "origin": "Published primary mathematical source; actual arXiv v2 dated25Jul2025, not generated research.",
      "id": "CD",
      "pages": [
        195,
        196,
        197,
        198,
        199,
        200,
        201,
        344,
        345,
        346,
        347,
        421,
        422,
        432,
        433,
        213,
        214
      ],
      "version": "arXiv v2, 25 July 2025",
      "applications": [
        "8.1.1/8.1.4: ordinary smooth stage 0; decreasing sequences define successors; v2 is a version, not stage 2.",
        "8.1.5 with 12.4.5: analytic morphisms, including analytic field extensions, preserve each ordinal stage.",
        "12.4.1/12.4.6; 15.1.1(b)/15.1.2: canonical refined analytic G-tropical structure; ordinary open moment charts.",
        "15.7.1/15.7.2: pure dimension and actual relative boundary; all positive proofs use boundaryless domains.",
        "8.3.1(b): positive current implies positive form only after ordinary smoothness is established.",
        "8.9.4: convex log-sum-exp moment functions are ordinary smooth psh."
      ],
      "verified_hashes": true,
      "literal_pages": [
        {
          "pdf_page": 195,
          "file": "source-extracts/CD/pdf-page0195.txt",
          "sha256": "0a6953836fd017b283a5467b0557ccf2090b40b8098273bfc13a00f1c8df8570",
          "literal": true
        },
        {
          "pdf_page": 196,
          "file": "source-extracts/CD/pdf-page0196.txt",
          "sha256": "61b50fb6f3127dfc5966106d69490b849037fd6fb935e576d47dae3564646d38",
          "literal": true
        },
        {
          "pdf_page": 197,
          "file": "source-extracts/CD/pdf-page0197.txt",
          "sha256": "3cff6777f7053ea434ba940cab457cb0249f80d81cd3ec450d5ff59491d7c9a0",
          "literal": true
        },
        {
          "pdf_page": 198,
          "file": "source-extracts/CD/pdf-page0198.txt",
          "sha256": "b4dd08f8e598dd24bc04e3d0362c02abc260ac1e070d2948f8f0675f215e6603",
          "literal": true
        },
        {
          "pdf_page": 199,
          "file": "source-extracts/CD/pdf-page0199.txt",
          "sha256": "bccdcbdf29046a4512c7dc5f549d9fd15fde92b3bc914223a6e1bd3c20ba9375",
          "literal": true
        },
        {
          "pdf_page": 200,
          "file": "source-extracts/CD/pdf-page0200.txt",
          "sha256": "568848788ff83a4e29c282547b7e48a21ed2f405683e86551be67583bf53fc73",
          "literal": true
        },
        {
          "pdf_page": 201,
          "file": "source-extracts/CD/pdf-page0201.txt",
          "sha256": "864de57b4ce5d737842d81e33d08b8479eb3ab3d7ef58966ae8bd53850d933f7",
          "literal": true
        },
        {
          "pdf_page": 213,
          "file": "source-extracts/CD/pdf-page0213.txt",
          "sha256": "896a74b8aa30031205a08e6d0894f3382d14f29e576297d74cccfbe47eb22eac",
          "literal": true
        },
        {
          "pdf_page": 214,
          "file": "source-extracts/CD/pdf-page0214.txt",
          "sha256": "519c05af2c473c83549271ea5be42cbd8ee52dd291c3dc3c41f172b435a498f6",
          "literal": true
        },
        {
          "pdf_page": 344,
          "file": "source-extracts/CD/pdf-page0344.txt",
          "sha256": "7419a9924336d3cfb17a7aac53b0b75bc7df7a879ea3d7a1c4fa905763f2390b",
          "literal": true
        },
        {
          "pdf_page": 345,
          "file": "source-extracts/CD/pdf-page0345.txt",
          "sha256": "0e49a88933ca003bac36aafedcac39d031e0338a450f25a6311201973d974598",
          "literal": true
        },
        {
          "pdf_page": 346,
          "file": "source-extracts/CD/pdf-page0346.txt",
          "sha256": "ad59868a3259884c9982c764fee3107e4019eef6dde72d2ff034d80faf667787",
          "literal": true
        },
        {
          "pdf_page": 347,
          "file": "source-extracts/CD/pdf-page0347.txt",
          "sha256": "553254bd03b04fe77bf40613de9d43cb9d814770c0ba52f062e67e531a75d3cf",
          "literal": true
        },
        {
          "pdf_page": 421,
          "file": "source-extracts/CD/pdf-page0421.txt",
          "sha256": "4a5f126f9dbc51433d024c7040a926fd6ae3833659452e09db156399b7ba9077",
          "literal": true
        },
        {
          "pdf_page": 422,
          "file": "source-extracts/CD/pdf-page0422.txt",
          "sha256": "06c6f2353b175e984f4cf02dd2220b72ba7d03770e3d2d0a3d2d4e2ea61bb17d",
          "literal": true
        },
        {
          "pdf_page": 432,
          "file": "source-extracts/CD/pdf-page0432.txt",
          "sha256": "66e30221555c0e7ba38d1f65d84b944ba5d727b87ce7bf470bd1b8d2f0ead0ec",
          "literal": true
        },
        {
          "pdf_page": 433,
          "file": "source-extracts/CD/pdf-page0433.txt",
          "sha256": "e734eaf14db296cbd0fb5b58c4539c04546d5e777cf84418d69223d7dea6321c",
          "literal": true
        }
      ]
    }
  ],
  "page_number_convention": "1-based formfeed-separated PDF pages; selected Thu printed pages are PDF minus 14.",
  "pdf_visual_checks": [
    {
      "id": "Thu",
      "pdf_page": 76,
      "artifact": "source-extracts/Thu-pdf76.png",
      "finding": "3.1.8(iii) actually says famille croissante et localement bornee; proof application is locally bounded on both sides."
    },
    {
      "id": "CD",
      "pdf_page": 196,
      "artifact": "source-extracts/CD-pdf196.png",
      "finding": "Stage 0 is smooth and positive; successors are local decreasing limits; ordinal bounds are preserved by 8.1.5. 8.1.1 explicitly uses sequences."
    },
    {
      "id": "GJR",
      "pdf_page": 80,
      "artifact": "source-extracts/GJR-pdf80.png",
      "finding": "15.11: smooth means rig-smooth without boundary; decreasing net; weakly smooth. 15.10 supplies ordinary smoothness only in its extra geometric/residue cases."
    }
  ],
  "dependency_policy": "No earlier generated theorem, unpublished book source or dossier proof verdict imported.",
  "checked_application_proofs": "All new applications are fully written in P03.2-argument.md and embedded in standalone P03.2-paper.tex."
}

## GRc PDF page 2

2                                 W. GUBLER AND J. RABINOFF

   Now we consider the non-Archimedean situation. Let k be a field that is complete
with respect to a non-Archimedean absolute value | |. We refer to Section 2 for the
notions used from non-Archimedean geometry. The theory of subharmonic functions
on a smooth, strictly analytic k-curve X has been completely worked out by Thuillier in
his thesis [Thu05]. Thuillier begins by defining harmonic functions as certain piecewise
linear functions satisfying a balancing condition; see [Thu05, §2.3] or 3.2. He then
defines a subharmonic function to be an upper semicontinuous function u: X → R ∪
{−∞} such that, for every strictly affinoid domain U ⊂ X and every harmonic function
h on U such that u ≤ h on ∂ U, we have u ≤ h on U. Thuillier shows that subharmonic
functions on smooth non-Archimedean curves satisfy the properties one would expect,
in analogy to the complex case.
   In higher dimensions, it is not completely clear yet what is the best definition for
plurisubharmonic functions. There is the global approach by Zhang [Zha95], who de-
fines a semipositive metric on a line bundle L over a projective k-variety X to be the
uniform limit of metrics induced by nef models. This approach is used in Arakelov ge-
ometry for various arithmetic applications. For an ample class θ on X , Boucksom and
Jonsson [BJ22] give a far reaching global pluripotential theory on a projective variety
over a trivially valued field. Some parts work for any non-Archimedean field, at least in
residue characteristic zero. These psh functions might be singular, and the definition uses
decreasing limits of semipositive model functions as in Zhang’s approach. Chambert–Loir
and Ducros [CD25] have posted a second version of their work in which they give a new
definition of psh functions which is functorial and is based on a transfinite regularization
process.
   In all of the above approaches, a maximum principle for plurisubharmonic functions
is missing. In this paper, we propose another class of psh functions called classically
plurisubharmonic functions in close analogy to the complex case. The definition is local,
the functions are upper semicontinuous, and we will show that properties (1)–(4) are
satisfied. It will be clear that classically psh functions form a maximal class of reasonable
plurisubharmonic functions that is compatible with Thuillier’s definition for curves. In
particular, the psh functions from the above are classically psh (see 1.2 below).
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


## GRc PDF page 3

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
1.3. Plurisubharmonic R-PL functions. For an R-piecewise linear function h: X → R
on a good strictly k-analytic space over a non-trivially valued field k, we have studied the
notion of semipositivity in the paper [GR25]. This notion is a local analytic version of
the global semipositive metrics introduced by Zhang [Zha95] which are induced by nef
models. We show in Theorem 4.3 that an R-PL function h is semipositive if and only if h
is classically psh.
1.4. Connectivity by curves. In Theorem 5.4, we show that two points x, y of a con-
nected k-analytic space X can be connected by analytic curves (assumed to be compact
and defined over a non-Archimedean field extension of k). If ∂ X = ;, then we even show
that x, y can be connected by overconvergent curves, which means roughly speaking that
we can connect them with the interiors of compact curves. We refer to Section 5 for the
precise definitions. The proof of Theorem 5.4 is inspired by Berkovich’s proof [Ber90,
§3.2] showing that a connected k-analytic space is pathwise connected. However, we
have to choose different paths, as the ones in ibid are not analytic curves. This result is
related to [dJ95, Proposition 6.1.1] and [Ber07, Theorem 4.1.1] (see the discussion after
the statement of Theorem 5.4 for more details).
Theorem 1.5 (Local Maximum Principle). Let X be a k-analytic space, and let u be a
classically psh function on X . If u has a local maximum on x ∈ Int(X ), then u is locally
constant at x.
  This will be shown in Theorem 6.1. For the proof, one may assume that ∂ X = ;;
then we reduce the claim to the local maximum principle for k-analytic curves using
connectivity by overconvergent curves.
1.6. Global maximum principle for affinoids. Berkovich has shown [Ber90, Propo-
sition 2.4.4] that a k-affinoid space X = M (A ) has a Shilov boundary, i.e. there is a
smallest subset Γ of X such that
                                 max | f (x)| = max | f (x)|
                                  x∈Γ           x∈X

for all f ∈ A . The Shilov boundary is finite and can be described rather explicitly. Ducros
has shown that the relative boundary ∂ X is parametrized by analytic spaces defined over
non-Archimedean extension fields. An inductive procedure leads us to a stratification of


## GRc PDF page 10

10                                W. GUBLER AND J. RABINOFF

Then the graded residue field of A is given by
                                           M
                                    e• :=
                                    A          A≤r /A<r .
                                           r∈R>0

We refer to [Tem04] for properties of this functorial construction.

                   3. SUBHARMONIC FUNCTIONS ON ANALYTIC CURVES
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


## GRc PDF page 11

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


## GRc PDF page 12

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
smooth, strictly k-analytic curve in four steps:
      (1) Extend scalars to a field as in 2.10 to make the curve strictly analytic.
                                                                                          −∞
      (2) If char(k) = p, then extend scalars to the completion of the perfect closure k p .
      (3) Replace the analytic curve by the underlying reduced curve.
      (4) Pass to the interior of the normalization, which is smooth (see 2.13).
We begin with some lemmas about this process.
                                                                                 −∞
Lemma 3.7. Suppose that char(k) = p > 0. Let k′ be the completion of k p . Then k′ is
perfect, and if X is a k-analytic space then πk′ /k : X k′ → X is a homeomorphism such that
π(∂ X k′ ) = ∂ X .
Proof. We leave it as an exercise for the reader to verify that k′ is perfect. The fact that
πk′ /k is a homeomorphism is [Duc09, Remarque 0.5], and the assertion about boundaries
is Lemma 2.12.                                                                            □
     We make the following observation to mirror Lemma 3.7. Its proof is immediate.
Lemma 3.8. Let X be a strictly k-analytic space and let ι : X red ,→ X be the inclusion of the
underlying reduced space. Then ι is a homeomorphism of underlying topological spaces, and
ι(∂ X red ) = ∂ X .
  We refer the reader to [Ber90, before Proposition 3.1.8] for the construction of the
normalization.
Lemma 3.9. Let X be a reduced, strictly k-analytic curve and let ν: Xe → X be its normal-
ization. Then the following hold:
    (1) Xe is rig-smooth if k is perfect.
    (2) ν is an isomorphism outside of a discrete set of rig-points of X .
                                     ∼
    (3) ν induces a bijection ∂ Xe −→ ∂ X .
    (4) ν is a topological quotient.


## GRc PDF page 13

              CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES                       13

                                                                             e = ν−1 (U) →
    (5) Let x ∈ X , let U be an open neighborhood of x, and consider the map U
        U. If U is a sufficiently small connected open neighborhood of x, then:
         (a) Ue → U is injective on connected components of U.  e
                                                                 ∼
         (b) Ue → U restricts to an isomorphism U  e \ ν−1 (x) −→ U \ {x}.
         (c) Every connected component of U   e intersects ν−1 (x).
    (6) A function h: X → R is R-PL if and only if h ◦ ν is R-PL.



Proof. The normalization Xe is locally the Berkovich spectrum of a Dedekind domain, so it
is rig-smooth when k is perfect because it is regular; this proves (1). Normalization is an
isomorphism away from codimension 1 as in algebraic geometry, which yields (2). Since
ν is finite, we have ∂ Xe = ν−1 (∂ X ) by the properties (2′ ) and (4′ ) of 2.11, so (3) follows
from (2) because the boundaries do not contain any rig-points. Assertion (4) was noted
in [Duc24, (3.1.3)].
    Now we prove (5). Since normalization is a local construction, we may shrink X to
assume that it is normal away from x. Suppose that ν−1 (x) = {x 1 , . . . , x n }, and choose
disjoint, connected open neighborhoods U1′ , . . . , Un′ of x 1 , . . . , x n , respectively. Let U ′ =
Sn                                                                         ∼
   i=1
       ν(Ui′ ).FSince ν induces an isomorphism Xe \ {x 1 , . . . , x n } −→ X \ {x}, it is clear that
                      n
ν−1 (U ′ ) = i=1 Ui′ . Since ν is a topological quotient, we have that U ′ is open, and ν is
injective on each Ui′ by construction.
    Suppose now that U ⊂ U ′ is a connected open neighborhood of x. By [Ber90, Theorem
3.2.1], U is path-connected. Clearly U satisfies (a) and (b). Let Ui = ν−1 (U) ∩ Ui′ , so that
                      e = ν−1 (U) = n Ui . In order to prove (c), it is enough to show that Ui
                                      F
x i ∈ Ui and U                          i=1
is path-connected. Let y ∈ Ui \ {x i }, and let γ: [0, 1] → U be a path from π( y) to x.
We may assume that γ−1 (x) = {1}, so that γ restricts to a path [0, 1) → U \ {x}. Let
γ
e : [0, 1) → U       e \ ν−1 (x) be the composition of γ|[0,1) with the inverse of the isomorphism
                      ∼
e \ ν−1 (x) −→ U \ {x}. Then γ
U                                        e(0) = y, so the image of γ e is contained in Ui . Extend γ  e
to a function [0, 1] → Ui by setting γ        e(1) = x i . One checks continuity of γ e at 1 using the
fact that an open neighborhood of x is the same as a collection of open neighborhoods
of x 1 , . . . , x n , as in the previous paragraph. This shows that Ui is path-connected.
    In the situation of (6), if h is R-PL then h◦ν is R-PL by [GJR21, Lemma 5.4(1)]. Suppose
then that h ◦ ν is R-PL. Piecewise linearity of h is local on X , and ν is an isomorphism
away from a finite set of (non-normal) rig-points, so it is enough to check that h is R-PL
in a neighborhood of a single rig-point x. Let x ′ ∈ Xe be a preimage ofPx. There is a
                                                                                          n
covering of Xe by strictly affinoid domains on which h ◦ ν has the form i=1 λi log | f i |,
where λi ∈ R and f i ∈ O × . Since x ′ is      Pan rig-point, it is contained in the interior   of one
of these affinoid domains, so h ◦ ν = i=1 λi log | f i | in a neighborhood of x . But if f is
                                                                                          ′

invertible in a neighborhood of a rig-point x ′ , then | f | is constant on a neighborhood of
x ′ (this elementary fact can be seen as a very special case of [Duc12, Theorem 3.4]). It
follows that h◦ν is constant in a neighborhood of x ′ . Suppose that ν−1 (x) = {x 1 , . . . , x n }.
For eachSn i choose an open neighborhood Ui of x i on which h ◦ ν is constant. As above,
U = i=1 ν(Ui ) is an open neighborhood of x, and clearly h is constant, hence R-PL,
on U.                                                                                                 □


## GRc PDF page 14

14                                  W. GUBLER AND J. RABINOFF

Proof of Proposition 3.5(1). This follows from the corresponding fact for subharmonic
functions on smooth, strictly analytic curves [Thu05, Corollaire 3.1.13], except that one
has to be careful about where a function takes the value −∞. Suppose then that {Ui }
is an open cover of X and that u: X → R ∪ {−∞} is subharmonic on each Ui . Note that
u is upper semicontinuous. Let k′ /k be an analytic extension field with k′ non-trivially
valued, let Y be a smooth, connected, strictly k′ -analytic curve, and let f : Y → X k′ be a
morphism. Assume that u ◦ πk′ /k ◦ f ̸≡ −∞, so we must show that u ◦ πk′ /k ◦ f is sub-
harmonic in Thuillier’s sense. Let Ui′ = π−1 k′ /k
                                                   (Ui ) = (Ui )k′ and let Yi = f −1 (Ui′ ). Since u
is subharmonic on Ui , the composition u ◦ πk′ /k ◦ f |Yi is either subharmonic in Thuillier’s
sense or is identically −∞ on each connected component of Yi .
   Let W1 be the set of all points y ∈ Y that admit a neighborhood on which u ◦ πk′ /k ◦ f
is subharmonic in Thuillier’s sense, and let W2 be the set of all points y ∈ Y that admit a
neighborhood on which u ◦ πk′ /k ◦ f ≡ −∞. Clearly W1 and W2 are open, and they cover
Y since Y is covered by the connected components of the Yi . They are disjoint because if
u ◦ πk′ /k ◦ f is subharmonic in Thuillier’s sense on a connected neighborhood of y ∈ Y ,
then it cannot be identically −∞ on any neighborhood of y [Thu05, Lemme 3.1.9].
Since Y is connected and u ◦ πk′ /k ◦ f ̸≡ −∞, we have Y = W1 . The result now follows
from [Thu05, Corollaire 3.1.13].                                                                  □


Proof of Proposition 3.5(2). Let f be an analytic function on X . The function | f | is con-
tinuous and hence u := log | f | is upper semicontinuous as a continuous function with
values in R ∪ {−∞}. According to our definition of subharmonic functions, we have to
show that after base change of u with respect to an analytic field extension k′ /k with k′
non-trivially valued and then pull-back to a smooth strictly k′ -analytic curve, the resulting
function is subharmonic. This boils down to showing that u is subharmonic in the special
case of a smooth strictly k-analytic curve X . For this, we may assume X connected. If
f = 0, then u is identically −∞ and hence subharmonic in the sense of Definition 3.4. If
f is not identically zero, then the Poincaré–Lelong formula [Thu05, Proposition 3.3.15]
and the characterization in terms of positive currents [Thu05, Proposition 3.4.4] show
that u is subharmonic in the sense of Thuillier.                                            □


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


## GRc PDF page 15

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


## GRc PDF page 16

16                                        W. GUBLER AND J. RABINOFF

Proof of Proposition 3.5(4,5). These follow quickly from the corresponding facts for sub-
harmonic functions on smooth, strictly analytic curves [Thu05, Proposition 3.1.8].     □

Proof of Proposition 3.5(6). Suppose first that X is strictly k-analytic for k non-trivially
                                                                                −∞
valued. If char(k) = p > 0 then let k′ be the completion of k p ; otherwise let k′ = k.
Let X ′ = X k′ and let π = πk′ /k : X ′ → X , so π is a homeomorphism preserving boundaries
by Lemma 3.7. Let ι : X red    ′
                                  ,→ X ′ be the inclusion of the underlying reduced space and let
ν: Xe ′ → X red′
                  be the normalization. Note that ν and ι are finite, so ∂ Xe ′ = (ι ◦ ν)−1 (∂ X ′ ),
and hence ∂ Xe ′ = (π◦ι ◦ν)−1 (∂ X ). Let Y = Int(Xe ′ ) and let f = ι ◦ν|Y : Y → X ′ . Then Y is
smooth and strictly analytic, so u ◦ π ◦ f is by definition either subharmonic in Thuillier’s
sense or identically −∞ on every connected component of Y .
   Suppose that u attains a local maximum at x ∈ Int(X ). If u(x) = −∞ then u must
be constant in a neighborhood of x by semicontinuity of u. Assume then that u(x) >
−∞. Both π and ι are homeomorphisms, so it suffices to show that u ◦ π ◦ ι : X red                 ′
                                                                                                      →
R ∪ {−∞} is constant in a neighborhood of the unique point x ∈ Int(X red ) mapping to
                                                                                 ′       ′

x. Choose a connected open neighborhood U ⊂ Int(X red                ′
                                                                       ) of x ′ as in Lemma 3.9(5), on
which u ◦ π ◦ ι attains a maximum at x ′ . By Lemma 3.9(3), we have ν−1 (U) ⊂ Y =
Int(Xe ′ ), so u ◦ π ◦ f is again either subharmonic in Thuillier’s sense or identically −∞
on each connected component C of ν−1 (U); since u(x) > −∞ and C ∩ ν−1 (x ′ ) ̸= ;, the
former is true. The function u◦π◦ f attains its maximum on every connected component
of ν−1 (U), so by the maximum principle for subharmonic functions on smooth, strictly
analytic curves [Thu05, Proposition 3.1.11], the function u ◦ π ◦ f is constant on every
connected component of ν−1 (U). It follows that u ◦ π ◦ ι is constant on U.
   Now we reduce to the strictly analytic case handled above. We may assume that X
is affinoid. As explained in 2.10, there is an analytic extension field k′ = k r for some
r ∈ R>0n
             such that X k′ is strictly k′ -analytic. Let σ : X → X k′ be the Shilov section of πk′ /k .
Then x = σ(x) ∈ Int(X k′ ) because π−1
           ′
                                                k′ /k
                                                      (Int(X )) ⊂ Int(X k′ ) by 2.11(5). It is immediate
from the definition that u ◦ πk′ /k is subharmonic, and it attains a local maximum at x ′ ,
so u ◦ πk′ /k is constant in an open neighborhood U ′ of x ′ . Then u is constant on the open
set U = σ−1 (U ′ ).                                                                                   □

Proof of Proposition 3.5(7). It is immediate from the definition that subharmonicity of
u implies subharmonicity of u ◦ πk′ /k . Suppose then that u ◦ πk′ /k is subharmonic. Let
k′′ /k be another analytic extension field with k′′ non-trivially valued, and let f : Y →
X k′′ be a morphism from a smooth, connected, strictly k′′ -analytic curve. Assume that
u ◦ πk′′ /k ◦ f ̸≡ −∞, so we need to show that u ◦ πk′′ /k ◦ f is subharmonic in Thuillier’s
sense. Let K be a non-Archimedean field that is simultaneously an analytic extension of
k′ and k′′ 2.2, and consider the following commutative diagram:

                               ←   fK            πK/k′
                                                 ←
                          YK            → XK          → X k′
                          ←



                                           ←



                                                            ←




(3.10.1)                                     πK/k′′             πk′ /k
                          →



                                          →



                                                            →




                               ←                 ←                ←
                           Y       f
                                       → X k′′         →
                                                  πk′′ /k   X            u → R ∪ {−∞}.


## GRc PDF page 17

             CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES                 17

Since u ◦ πk′ /k is subharmonic, the composition u ◦ πK/k ◦ f K is, on each connected compo-
nent C of YK , either subharmonic in Thuillier’s sense or identically −∞; since C surjects
onto Y [Duc18, 1.5.6] and u ◦ πk′′ /k ◦ f ̸≡ −∞, the latter does not happen. Replacing
X by Y and k′ /k by K/k′′ , we are reduced to showing that if X is smooth and strictly
k-analytic for k non-trivially valued and u ◦ πk′ /k is subharmonic in Thuillier’s sense, then
so is u.
   We can do this directly using Thuillier’s definition. (The converse is the difficult di-
rection: see [Thu05, Corollaire 3.4.5].) Let U ⊂ X be a strictly k-affinoid domain and
let h: U → R be a harmonic function such that u ≤ h on ∂ U. Then h ◦ πk′ /k : Uk′ =
π−1
  k′ /k
        (U) → R is harmonic by [Thu05, Proposition 2.3.18]. We have πk′ /k (∂ Uk′ ) = ∂ U by
Lemma 2.12, so u ◦ πk′ /k ≤ h ◦ πk′ /k on ∂ Uk′ . Since u ◦ πk′ /k is subharmonic in Thuillier’s
sense, this implies u ◦ πk′ /k ≤ h ◦ πk′ /k on Uk′ , so u ≤ h on U since πk′ /k : Uk′ ↠ U is
surjective. Thus u is subharmonic in Thuillier’s sense, as claimed.                          □

Proof of Proposition 3.5(8). It is immediate that subharmonicity of u implies subharmonic-
ity of u ◦ f . Suppose then that f is finite and surjective and that u ◦ f is subharmonic. Let
k′ /k be an analytic extension field with k′ non-trivially valued and let g : Z → X k′ be a
morphism from a smooth, connected, strictly k′ -analytic curve. Suppose that u◦πk′ /k ◦g ̸≡
−∞, so we need to show that u ◦ πk′ /k ◦ g is subharmonic in Thuillier’s sense. Let
W = Z ×X k′ Yk′ , and consider the following commutative diagram:

                                   ←   g′           πk′ /k
                                                    ←
                          W             → Yk′           → Y
                           ←




                                                             ←
                                            ←




(3.10.2)                f ′′           □       f′                f
                          →



                                            →



                                                             →




                                   ←                ←                ←
                               Z       g→   X k′        →
                                                    πk′ /k   X           u → R ∪ {−∞}.


The composition (u ◦ f ) ◦ πk′ /k ◦ g ′ is subharmonic because it is pulled back from u ◦ f by
an extension of scalars and the morphism g ′ : W → Yk′ . Since f is finite and surjective,
so are f ′ and f ′′ by 2.2, so we may replace X by Z and Y by W to assume X is a smooth,
connected, strictly k-analytic curve for k non-trivially valued and that u ̸≡ −∞. We can
check subharmonicity of u (in Thuillier’s sense) after extending scalars as in the proof of
Proposition 3.5(7), so we may assume in addition that k is perfect.
   Let ι : Yred ,→ Y be the inclusion of the underlying reduced space, and let ν: Ye → Yred be
the normalization. Since k is perfect, the normal curve Ye is rig-smooth, and since Ye → X
is finite and ∂ X = ; (as X is smooth), the curve Ye is smooth as well: see Lemmas 3.8
and 3.9. Both ι and ν are finite and surjective, so f ◦ ι ◦ ν: Ye → X is again finite and
surjective. By Definition 3.4 (with k = k′ ), subharmonicity of u ◦ f means that, on each
connected component C of Ye , the function (u◦ f )◦ι◦ν is either subharmonic in Thuillier’s
sense or is identically −∞. Since C → X is surjective (it is finite, hence it is a closed
map, and it is an open map by [Ber90, Lemma 3.2.4], so its image is all of X since X is
connected), the latter does not happen, so u ◦ f ◦ ι ◦ ν is subharmonic in Thuillier’s sense.
Thus we replace Y by Ye and f by f ◦ ι ◦ ν to assume X and Y are both smooth, and that
u ◦ f is subharmonic in Thuillier’s sense.


## GRc PDF page 18

18                                W. GUBLER AND J. RABINOFF

   At this point, one proves that u is subharmonic in Thuillier’s sense directly from Thuil-
lier’s definition, as in the proof of Proposition 3.5(7), this time using [Thu05, Proposi-
tion 2.3.19]. The converse is the difficult direction: see [Thu05, Proposition 3.1.14]. □
  We will need the following lemma in the proof of Proposition 3.5(9). (Note that
Lemma 3.11 itself follows from Proposition 3.5(9) as we have seen in 3.5.5.)
Lemma 3.11. Let X be a strictly k-analytic curve over a non-trivially valued field k and let
u: X → R ∪ {−∞} be a subharmonic function. If x ∈ ∂ X and u(x) = −∞, then u ≡ −∞
on a neighborhood of x.
                                                          −∞
Proof. If char(k) = p > 0 let k′ be the completion of k p , and otherwise let k′ = k. Let
X ′ = X k′ and π = πk′ /k : X ′ → X , let ι : X red
                                                ′
                                                     ,→ X ′ be the inclusion of the underlying
reduced space, and let ν: Xe ′ → X red
                                     ′
                                        be the normalization. Then π and ι are homeomor-
phisms preserving boundaries by Lemmas 3.7 and 3.8, and ν is a boundary-preserving
isomorphism in a neighborhood of the unique point x ′ ∈ Xe ′ lying over x by Lemma 3.9.
The composition u ◦ π ◦ ι ◦ ν is subharmonic, so we may replace X by Xe ′ to assume that
X is rig-smooth. After shrinking X , we may assume that X is strictly affinoid. By [Ber90,
Corollary 1.3.6], if K is the completion of an algebraic closure of k then X K → X is an
open map, and by Lemma 2.12 there is a point of ∂ X K lying over x, so we may extend
scalars to assume that k is algebraically closed.
   By the semistable reduction theorem [Thu05, Théorème 2.3.8], there exists a semistable
(formal) model X of X . Let red: X → Xs denote the reduction map, which is anti-
continuous. Let ξ ∈ Xs be any point. As explained in [BPR13, Theorem 4.6] (see also
[BL85, Propositions 2.2 and 2.3]), if ξ is a generic point then red−1 (ξ) is a single type-2
point of X ; if ξ is a smooth closed point then red−1 (ξ) is isomorphic to an open unit ball;
and if ξ is a node then red−1 (ξ) is isomorphic to an open annulus. In particular, if ξ is a
closed point then red−1 (ξ) is connected and open.
   By [CD12, Lemme 6.5.1], the closure of ζ = red(x) is not proper, so ζ is a generic
point of Xs . Let Y ⊂ Xs denote its closure. Then red−1 (Y ) is an open neighborhood of
x in X . Let ξ ∈ Y be a closed point and let U = red−1 (ξ). Then x is a limit point of U:
one can use [BPR13, Lemma 3.2], or one can see this using retraction to the skeleton
S(X) from [Thu05, Théorème 2.2.10]; in this case, x is a vertex of S(X), and either U
deformation retracts onto x if ξ is smooth, or U contains an edge of S(X) adjacent to
x when ξ is a node. It follows that red−1 (Y ) is contained in the union of {x} with all
connected components U of Int(X ) having x as a limit point. We will show that u ≡ −∞
on every such U.
   We adapt the proof of [Thu05, Lemme 3.1.9]. Suppose that u ̸≡ −∞ on some such
U. Then u|U is subharmonic in Thuillier’s sense as U is smooth and connected and u is
subharmonic in our sense. By [Thu05, Lemme 2.3.9], for every N ∈ Z≥0 , there exists a
unique harmonic function hN : X → R such that hN (x) = −N and
                                           u( y) if u( y) > −∞
                                         
                               hN ( y) =
                                           0        otherwise
for every y ∈ ∂ X \ {x}. By construction, we have u − hN ≤ 0 on ∂ X . By [Thu05,
Corollaire 3.1.12], if the function u − hN attains a local maximum at a point y ∈ U, then


## GRc PDF page 21

             CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES               21

Remark 3.16. We still assume that X is a strictly k-analytic curve over a non-trivially
valued field k and that h: X → R is continuous. Proposition 3.15 and Proposition 3.14(6)
imply in particular that if h◦πk′ /k is harmonic for some analytic extension field k′ /k, then
h◦πk′′ /k is R-PL for any analytic extension k′′ /k, which is by no means obvious. Likewise,
Proposition 3.14(7) implies that if f : Y → X is finite and surjective and h◦ f is harmonic,
then h is R-PL, and Proposition 3.14(8) implies that if h|Int(X ) is harmonic then h is R-PL.

                     4. CLASSICALLY PLURISUBHARMONIC FUNCTIONS
  In this section we define the notion of a classically plurisubharmonic function. The
definition follows Definition 3.4.
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


## GRc PDF page 22

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


## GRc PDF page 23

              CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES                  23

Proof. For x ∈ X , an R-PL function h: X → R induces a residue line bundle Lh (x) ∈
Pic(red(X , x))R on the reduction red(X , x) of the germ (X , x): see 2.17. Recall from
[GJR21, Definition 7.2] that h is semipositive at x ∈ X if and only if the associated residue
line bundle Lh (x) is nef. We have shown in [GR25, Proposition 3.1] that for a smooth
strictly k-analytic curve, an R-PL function is semipositive if and only if it is subharmonic.
Since semipositivity is stable under base extension and pull-back [GJR21, Proposition
7.6], we conclude that a semipositive R-PL function on X is classically psh.
   The converse follows from [GR25, Corollary 3.5], which shows that an R-PL function h
on X is semipositive if and only if there is an algebraically closed analytic extension field
F of k such that for every smooth F -analytic curve C and every morphism ϕ : C → X F ,
we have h ◦ ϕ semipositive.                                                                □
                                 5. CONNECTIVITY BY CURVES
  We will prove a maximum principle for classically psh functions by reducing to the
case of curves. For this we will need to prove that it is possible to connect a point of an
analytic space to its neighbors using analytic curves, potentially defined over large field
extensions.
Definition 5.1. Let X be a k-analytic space. An analytic curve in X is a subset Γ ⊂ X
satisfying the following property: there is an analytic extension field k′ /k, a compact,
separated k′ -analytic space C of dimension at most 1, and a morphism ϕ : C → X k′ , such
that Γ = πk′ /k ◦ ϕ(C).
  An analytic curve Γ in X is overconvergent if there exist (k′ , C, ϕ) as above such that ϕ
factors as
                                          ψ
                                           → Int(C ′ ) -← → C ′
                                      ←
                                  C
                                      ←
(5.1.1)                                                     ←
                                          ϕ →            ϕ′
                                                           →
                                               X k′
where C ′ is a separated k′ -analytic space of dimension at most 1, and ϕ ′ and ψ are
morphisms.
5.1.2. The compactness hypothesis in Definition 5.1 is crucial. When X is Hausdorff, it
implies that if Γ , Γ ′ are analytic curves in X such that Γ ∪ Γ ′ is connected, then Γ ∩ Γ ′ ̸= ;
(the compact sets Γ , Γ ′ are closed, so they cannot be disjoint by connectedness). However,
a non-proper compact curve has a nonempty boundary, which causes problems when
trying to reduce the maximum principle to the case of curves. This is the reason for
introducing overconvergent curves in X .
5.1.3. One can always pass to a larger analytic extension field k′′ /k′ in Definition 5.1.
Indeed, we have a commutative diagram
                                          ←   ϕk′′
                                   Ck′′         → X k′′
                                                                   πk′′ /k
                                      ←



                                                       ←




                                                               ←
                                                πk′′ /k′
                                                                   →
                                   ↠



                                                      →




                                          ←                  ←
                                      C       ϕ→      X k′         → X.
                                                               πk′ /k


## GRc PDF page 29

               CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES                          29

x has a neighborhood in each irreducible component that is connected by curves, so we
may assume that X is irreducible.
   Now we will prove that any irreducible, strictly k-affinoid space X is connected by
curves. We will show that for every x ∈ X , there is a neighborhood U of x such that
x ∼ x ′ for all x ′ ∈ U. This is not the same thing as showing that U is connected by
curves, as the curve connecting x to x ′ may leave U. However, it does imply that the
∼-equivalence classes are open, which is enough because X is connected.
   By the Noether normalization lemma [BGR84, Corollary 6.1.2/2], [Ber90, Corollary
2.1.16], there exists a finite, surjective morphism ϕ : X → Bn for n = dim(X ). For x ′ ∈ X
let y ′ = ϕ(x ′ ), and let Σ x ′ be the connected component of ϕ −1 ([ y ′ , 0]) containing x ′ .
Berkovich shows in the proof of [Ber90, Lemma 3.2.5] (which applies in our situation by
Lemma 5.10) that there is an open neighborhood U of x such that for all x ′ ∈ U, the sets
Σ x and Σ x ′ contain a common point of ϕ −1 (0).
   By Lemma 5.9, there are connected analytic curves Γ y , Γ y ′ in Bn such that [ y, 0] ⊂ Γ y and
[ y ′ , 0] ⊂ Γ y ′ . Let Γ x (resp. Γ x ′ ) be the connected component of ϕ −1 (Γ y ) (resp. ϕ −1 (Γ y ′ ))
containing x (resp. x ′ ). These are connected analytic curves in X by Lemma 5.2(1,4).
We have Σ x ⊂ Γ x and Σ x ′ ⊂ Γ x ′ , so that Γ x ∩ Γ x ′ ̸= ;. Hence x and x ′ are contained in
the connected analytic curve Γ x ∪ Γ x ′ in X . Since x ′ ∈ U was arbitrary, this completes the
proof that a connected k-analytic space is connected by curves.

    Now suppose that X is a connected and boundaryless k-analytic space. Define an
equivalence relation ∼′ on X by x ∼′ y if there exists a connected, overconvergent
analytic curve Γ in X such that x, y ∈ Γ . As before, we will prove that every point
x ∈ X admits a neighborhood that is connected by overconvergent curves, since this
implies that the ∼′ -equivalence classes are open. By the definition the relative interior
([Ber90, §1.5], [Tem15, §4.2.4]), any point x ∈ X admits an affinoid neighborhood Y .
Note that x ∈ Int(Y ). Let k′ /k be an analytic extension field such that Yk′ is strictly
k′ -analytic and πk′ /k : Yk′ → Y admits a continuous section σ : Y → Yk′ , as before. We
have π−1k′ /k
              (Int(Y )) ⊂ Int(Yk′ ) by 2.11(5), so σ(x) ∈ Int(Yk′ ). As in the previous case, it is
enough to find a neighborhood of σ(x) in Yk′ that is connected by overconvergent curves.
Hence we may assume that Y is strictly k-affinoid and x ∈ Int(Y ). Let k′ /k be the com-
pletion of an algebraic closure of k. Then Yk′ → Y is open by [Ber90, Corollary 1.3.6],
so it suffices to find a neighborhood of any preimage of x in Int(Yk′ ) that is connected by
overconvergent curves by Lemma 5.11. We may therefore assume that k is algebraically
closed. Let Y1 , . . . , Yn be the irreducible components of Y containing x. Then x ∈ Int(Yi )
for each i; it is enough to show that x admits a neighborhood in each Yi that is connected
by overconvergent curves, so we may assume that Y is irreducible and x ∈ Int(Y ). Let V
be the connected component of x in Int(Y ).
    We will prove that V is connected by overconvergent curves. We proceed with an
argument similar to the previous case: that is, for any x ∈ V , we will show that x and x ′
are connected by an overconvergent curve in V for all x ′ in a neighborhood of x. Choose
a finite, surjective morphism ϕ : Y → Bn . The interior of Bn is the (disjoint) union of all
residue balls B+n (z, 1) by [CD12, Lemme 6.5.1] (all residue balls have k-rational centers
z since k = k), and ϕ −1 (Int(Bn )) = Int(Y ) by finiteness of ϕ (use 2.11(2) and (4)); thus,


## GRc PDF page 30

30                                   W. GUBLER AND J. RABINOFF

after recentering, we can assume that ϕ(V ) ⊂ B+n . For x ′ ∈ V let y ′ = ϕ(x ′ ) ∈ B+n and
let Σ x ′ be the connected component of ϕ −1 ([ y ′ , 0]) containing x ′ . Since [ y ′ , 0] ⊂ B+n we
have ϕ −1 ([ y ′ , 0]) ⊂ Int(Y ), and since Σ x ′ is connected and x ′ ∈ V we have Σ x ′ ⊂ V . As
before, there exists an open neighborhood U of x in V such that Σ x ′ ∩ Σ x ̸= ; for all
x ′ ∈ U.
     By Lemma 5.9, for any y ′ ∈ B+n there is a connected, overconvergent analytic curve
Γ y ′ in B+n containing [ y ′ , 0]. For x ′ ∈ V mapping to y ′ , we let Γ x ′ be the connected
component of ϕ −1 (Γ y ′ ) containing x ′ , so that Γ x ′ ⊂ V for the same reason that Σ x ′ ⊂ V .
By Lemma 5.2(1,4), this Γ x ′ is again a connected, overconvergent analytic curve in X .
Clearly Σ x ′ ⊂ Γ x ′ , so for x ′ ∈ U we have Γ x ′ ∩ Γ x ̸= ;. This completes the proof as in the
previous case.                                                                                     □

              6. THE MAXIMUM PRINCIPLES FOR CLASSICALLY PSH FUNCTIONS
  In this section, we consider a non-Archimedean field k. We will prove first that the
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


## GRc PDF page 31

              CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES                     31

It follows that u ≡ R on W ∩ Γ . This proves that Γu=R is open in Γ . As remarked above,
this yields u ≡ R on Γ .
   Let y ∈ X be any point. By Theorem 5.4, there is a connected, overconvergent analytic
curve Γ in X containing x and y. We showed above that u ≡ R on Γ , so that u( y) = R.
As y was arbitrary, we have u ≡ R on X .                                              □

  The global maximum principle for classically psh functions involves the Shilov bound-
ary. For this, we need the following two lemmas. The first is well-known, but we were
unable to find a reference.

Lemma 6.2. Let X be a k-affinoid space of pure dimension d ≥ 1. Then the Shilov boundary
of X is contained in the relative boundary ∂ X of X over k. In particular, ∂ X ̸= ;.

Proof. Let k′ /k be an analytic field extension such that X k′ is strictly affinoid. Note that
the base change morphism πk′ /k maps ∂ X k′ to ∂ X 2.11(5′ ) and maps the Shilov boundary
onto the Shilov boundary [GRW17, Proposition 2.21], so we may assume that X is strictly
affinoid and k′ non-trivially valued. Choose a formal affine k◦ -model X of X . The interior
X \ ∂ X consists of the points x ∈ X such that the closure of redX (x) in Xs is proper over
the residue field ek by [CD12, Lemme 6.5.1]. Since X is affine, the special fiber Xs is
affine, so x ∈ ∂ X if and only if redX (x) is not a closed point of Xs . Since d ≥ 1, the
special fiber Xs is of pure dimension d ≥ 1, and hence the generic points of Xs are not
closed. By [GM19, Proposition A.3], the divisorial points of X (i.e. the points of X which
reduce to the generic points of Xs ) are precisely the Shilov points of X . We conclude that
all Shilov points are in the boundary of X .                                                □

   Let X = M (A ) be an affinoid space over k of pure dimension d. By a result of Ducros
[Duc12, Lemme 3.1], the boundary ∂ X of X can be expressed as a union of affinoid spaces
of lower dimension, defined over certain extension fields of k. We use his argument to
give a stratification of ∂ X . Choose non-nilpotent elements g1 , . . . , g r ∈ A such that the
graded reductions e   g1• , . . . , e
                                    g r• generate the graded ek• -algebra A
                                                                          f• . Let ri be the spectral
radius of g i . Then for any I ⊂ {1, . . . , r}, we get a morphism

                                p I : X −→ B(I),       x 7→ (g i (x))i∈I

to the closed poly-disc B(I) = i∈I B(0, ri ) of dimension s = |I|. Let η(I) be the weighted
                                     Q

Gauss point of B(I) and let k I := H (η(I) ), which is the completion of the field of rational
functions k((t i )i∈I ) in the variables (t i )i∈I with respect to the weighted Gauss valuation
for the weight (ri )i∈I .

Lemma 6.3. With the above notations, set X I := p−1
                                                 I
                                                    (η(I) ). By convention, we set X ; = X .
Then:
                 k I -affinoid space of pure dimension d − s if non-empty.
    (1) X I is a S
    (2) ∂ X I = i∈{1,...,r}\I X I∪{i} .
    (3) X I = {x ∈ X | (e   g i• (x))i∈I are algebraically independent in H
                                                                          f• (x) over ek• }.
                                                                                     S
    (4) If X has pure dimension d, then the Shilov boundary of X is equal to |I|=d X I .


## GRc PDF page 32

32                                  W. GUBLER AND J. RABINOFF

   We note that the affinoid space X I is naturally homeomorphic to the fiber p−1
                                                                               I
                                                                                  (η(s) ) ⊂ X
in the subspace topology: see [Ber93, §1.4]. If I is non-empty, then we call X I a stratum
set for the boundary.
Proof. Since p I is a morphism between the k-affinoid spaces X and B(I) of pure dimension
d and s, respectively, and since the Gauss point η(I) is an Abhyankar point of B(I), we de-
duce from [Duc18, Lemma 1.5.11] that X I is a H (η(I) )-affinoid space of pure dimension
d − s if non-empty. This proves (1).
  The remaining argument is based on the following description of the boundary given
by Ducros in [Duc12, Lemme 3.1]. For any x ∈ X = M (A ), we get an induced character
ψ: A → H (x). Then Temkin’s graded reduction of the germ (X , x) is given by [Tem00,
§2]
                               red(X , x) = PHf(x)/ek {ψ
                                                       e• (A )}.

By definition, this is the set of graded valuations w on H           f• (x) which are trivial on ek
and which satisfy |ψ     e• (g)|w ≤ 1 for all g ∈ A . Using that the graded reductions of our
fixed family g1 , . . . , g r ∈ A generate the graded ek• -algebra A     f• , it is enough to check
|ψe• (g)|w ≤ 1 for g = g1 , . . . , g r . Based on Temkin’s result on graded reductions, Ducros
shows that x ∈ ∂ X is equivalent to the existence of some i ∈ {1, . . . , r} and of a graded
valuation w on H       f• (x) which is trivial on ek• such that |ψ(g i )|w > 1. Ducros shows in
his argument that this is equivalent to e      g i• (x) ∈ H
                                                          f• (x) being transcendental over ek• . For
i = 1, . . . , r, he considers the morphism pi : X → B(0, ri ) induced by g i . Let X i be the fiber
over the weighted Gauss point η(i) of the closed disc B(0, ri ) = M (k〈ri−1 t〉) (of radius ri ).
By (1), we have that X i is a H (η(i) )-affinoid space of pure dimension d − 1 if non-empty.
It follows from the above that the union of all of the X i is equal to ∂ X .
   Let us summarize the construction. For each i ∈ {1, . . . , r}, we define
                       X i := {x ∈ X | e
                                       g i• (x) is transcendental over ek• }.
This set might be empty. We have seen that g i defines a morphism pi : X → B(0, ri ) =
M (k〈ri−1 t〉) for the Tate algebra k〈ri−1 t〉 in the variable t, and that X i is the fiber of pi
over the weighted Gauss point η(i) . In any case, X i is an affinoid space over the non-
archimedean field ki := H (η(i) ) which is the completion of k(t) with respect to the
weighted Gauss valuation for the weight ri . If X i is non-empty, then X i has pure dimen-
sion d − 1. Ducros has shown that
                                                [
                                     ∂X =            Xi.
                                               i∈{1,...,r}

   We prove now the claims (2)–(3) by induction on s = |I|. If s = 0, then I = ; and
X I = X . Then the above description of the boundary due to Ducros proves (2) and
(3). Now assume that s > 0. We pick i ∈ I and set J := I \ {i}. As seen above, we
have that X i := pi−1 (η(i) ) is an affinoid space over ki = H (η(i) ), and we denote the
corresponding affinoid algebra by Ai := O (X i ). Note here that ki is the completion of
k(t) with respect to the weighted Gauss norm for the weight ri . For Ai = A ⊗          b k ki , the
                                                            •               •
same elements g1 , . . . , g r induce generators of Ai as a graded ki -algebra. Note that
                                                          f               e
H (η(I) ) is the completion of k((t i ′ )i ′ ∈I ) with respect to the Gauss norm for the weight


## GRc PDF page 33

               CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES                           33

(ri ′ )i ′ ∈I and hence also the completion of ki (r j ) j∈J with respect to the weighted Gauss
norm for the weight (r j ) j∈J identifying the variable t ∈ ki with t i . It follows readily that
for any H ⊂ {1, . . . , r}, we have (X i )H = X {i}∪H as affinoid spaces over k I . Applying this
with H = J and using our induction hypothesis for X i , property (2) for the boundary of
X I = (X i )J follows by induction applied to X i . The same inductive argument shows that
X I is the set of points x ∈ X 1 where (e      g j (x)) j∈J are algebraically independent over eki . We
have seen that X i is non-empty if and only if e           g i (x) is transcendental over ek. Since t = t i
in ki satisfies pi (t) = g i , we conclude that x ∈ X I if and only if (e
                      ∗
                                                                               g l (x))l∈I are algebraically
independent over ek. This proves (3).
   Finally, we claim that the union of the minimal strata X I for |I| = d is the Shilov
boundary of X . If d = 0, this is obious as X = X ; . Now assume that d ≥ 1. If x ∈ X I then
(3) shows that the graded residue field H            f(x)• contains the d algebraically independent
elements (e     g i )i∈I over ek• . Since the reduction Xe in the sense of Temkin [Tem04, Section
3] is of pure dimension d (using [Tem04, Proposition 3.1(v)] for base change to the
strictly affinoid case), we conclude that the reduction of x in Xe is a generic point of Xe .
By [Tem04, Proposition 3.3], we conclude that x is a Shilov point of X . Conversely, for
every a ∈ A , the function |a| takes its maximum in a Shilov point. We conclude from
Lemma 6.2 that |a| takes its maximum in ∂ X ̸= ;. By (2), we conclude that |a| takes its
maximum in one of the strata sets X I . By induction on the dimension d, this occurs when
|I| = d proving (4).                                                                                      □
  We return to the setting where k is any non-Archimedean field which might be trivially
valued. We give now the global maximum principle for affinoids.
Theorem 6.4. Let h be a classically psh function on a k-affinoid space X . Then h takes its
maximum in a Shilov point of X .
  An analogue for θ -psh functions on a proper scheme is in [GM19, Proposition 4.22].
Proof. By base change to a non-trivially valued analytic extension field k′ /k such that X k′
is strictly affinoid, and using that πk′ /k maps the Shilov boundary of X k′ to the Shilov
boundary of X [GRW17, Proposition 2.21],    S we may assume that X is strictly affinoid and
that k is non-trivially valued. Let X = j X j be the partition of X into its irreducible
components. It follows from [GRW17, Proposition 2.15] that the union of the Shilov
points of all X j gives the Shilov points of X . So it is enough to prove the claim for every
X j , and hence we may assume X irreducible. This will be a bit to strong for our inductive
argument later, but the argument shows that we may assume X of pure dimension d.
    If d ≥ 1, then we claim that h takes its maximum in the boundary ∂ X . We prove this
by contradiction. It is clear that the boundary ∂ X is the disjoint union of the boundaries
of the connected components of X , and the same holds if we replace the boundary by the
Shilov boundary, so we may assume X connected. Let M be the set of points of X where
h is maximal. We assumed that M ∩ ∂ X = ;. Since h is continuous, it is clear that M is
a closed subset of X . We know from Theorem 6.1 that if a classically psh function takes
a (local) maximum on X \ ∂ X , then h is locally constant. This implies M open in X . As
M is non-empty and X is connected, we deduce M = X . Since ∂ X ̸= ; as we have d ≥ 1
(see Lemma 6.2), we get M ∩ ∂ X ̸= ;, which is a contradiction.


## GRc PDF page 34

34                                 W. GUBLER AND J. RABINOFF

    Let now
        S h be a classically psh function on X . We need the description of the boundary
∂ X = X i given in Lemma 6.3, where i runs through {1, . . . , r} and X i = X {i} as before.
We claim by induction on d that h takes its maximum in one of the sets X I with |I| = d,
and hence in the Shilov boundary of X , which proves the theorem. If h is constant, then
this is obvious; this also settles the case d = 0. If h is non-constant, then we have seen
at the beginning of the proof that h takes its maximum in ∂ X , and hence in one of the
X i . Since X i is of dimension d − 1, we are done by induction as the strata sets of ∂ X i are
strata sets of ∂ X using Lemma 6.3.                                                          □
  The following result was suggested by a referee of the paper [GR25]. We are very
grateful for this hint.
Theorem 6.5. Let (u j ) j∈J be a net of classically psh functions on the k-analytic space X
which converges pointwise to an upper semicontinuous function u. Then u is classically psh.
   For a sequence of semipositive R-PL functions converging pointwise to an R-PL func-
tion, the above result was shown in [GR25, Theorem 5.6]. When X is a proper algebraic
variety, this was known before ([GK19, Proposition 7.2] for uniform limits, [GM19, The-
orem 1.3] for pointwise limits).
Proof. Since u is upper semicontinuous, using the definition of classically psh functions,
we may assume that X is a connected smooth curve over a non-trivially valued field.
We may assume that u is not identically −∞. Then for every strictly k-affinoid domain
U of X and every harmonic function h on U with u ≤ h on ∂ U, we have to show that
u ≤ h holds on U. Since u j → u pointwise and since ∂ U is finite, for any ϵ > 0 we have
u j − h ≤ ϵ on ∂ U for all j sufficiently large. Since u j − h is a classically psh function by
Proposition 3.5(4) and since the Shilov boundary of U agrees with ∂ U [Thu05, §2.1.2],
the global affinoid maximum principle in Theorem 6.4 shows that u j − h ≤ ϵ on U for all
j sufficiently large. It follows that u − h ≤ ϵ on U, which implies u ≤ h on U since ϵ was
arbitrary.                                                                                   □

                               7. PLURIHARMONIC FUNCTIONS
  In this section, we consider a k-analytic space X over any non-Archimedean field k.
Following the discussion of harmonic functions on curves in 3.12, we generalize this
notion as follows to higher dimensions.
Definition 7.1. A function h: X → R is called pluriharmonic if h and −h are classically
psh functions (see Definition 4.1).
Proposition 7.2. Pluriharmonic functions are continuous and have the properties:
     (1) (Sheafiness) The pluriharmonic functions form a sheaf on X .
     (2) If f ∈ Γ (X , OX× ) then log | f | is pluriharmonic.
     (3) (Vector Space) The pluriharmonic functions on X form a real vector space which
         we denote by PH(X ).
     (4) (Limits) If a function h: X → R is locally a uniform limit of pluriharmonic functions,
         then h is pluriharmonic.


## GRc PDF page 35

             CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES              35

   (5) (Maximum Principle) If h ∈ PH(X ) and h attains a local extremum at x ∈ Int(X ),
       then h is constant in a neighborhood of x.
   (6) (Extension of Scalars) Let k′ /k be an analytic extension field. Then h pluriharmonic
       if and only if h ◦ πk′ /k : X k′ → R is pluriharmonic.
   (7) (Functoriality) Let Y be a k-analytic space and let f : Y → X be a morphism. If
       h ∈ PH(X ) then h ◦ f ∈ PH(Y ), and the converse holds if f is finite and surjective.
Proof. It is clear that a pluriharmonic function h is continuous as h and −h are upper
semicontinuous. Properties (1), (2), (3), (6) and (7) follow immediately from the corre-
sponding properties of classically psh functions given in Proposition 4.2. In (4), we note
that a uniform limit of pluriharmonic functions can be easily written as a decreasing
(resp. increasing) limit of pluriharmonic functions and hence (4) follows from Proposi-
tion 4.2(4). The maximum principle (5) follows from the maximum principle for classi-
cally psh functions shown in Theorem 6.1.                                               □
   From now on, we denote by PH(X ) the space of pluriharmonic functions on X . The
affinoid global maximum principle for classically psh functions has the following conse-
quence.
Proposition 7.3. Let X be a k-affinoid space with Shilov boundary Γ . Then every plurihar-
monic function takes its global maximum and its global minimum in a Shilov point of X ,
and the R-linear map
                             PH(X ) −→ RΓ , h 7→ (h(x)) x∈Γ
is injective.
Proof. By definition, the function h: X → R is pluriharmonic if and only if h and −h
are classically psh. It follows from Theorem 6.4 that a pluriharmonic function takes its
maximum and its minimum on the Shilov boundary Γ . In particular, a pluriharmonic
function is zero if and only if its restriction to Γ is zero, which proves the last claim. □
Theorem 7.4. Let X be a quasicompact k-analytic space. Then PH(X ) is a finite dimensional
real vector space.
Proof. Using quasicompactness, we can cover X by finitely affinoid subsets Ui . Using
Proposition 7.3, we know that PH(Ui ) is finite dimensional for every i. Since plurihar-
monic functions are determined by their restrictions to the Ui ’s, this proves the claim.
For later purposes, we note that the linear map
(7.4.1)                       PH(X ) −→ RΓ ,    h 7→ (h(x)) x∈Γ
is injective where Γ is the union of the Shilov boundaries of all Ui ’s.                   □
Remark 7.5. Assume that k is non-trivially valued and that X is a quasicompact k-analytic
space. Let X be any formal model of X over the valuation ring k◦ . Then dim(PH(X )) is
bounded by the number of divisorial points of X associated to X.
   Indeed, such a formal model is quasi-compact, hence can be covered by finitely many
formal affine open subsets Ui . Then the above argument applies to the strictly affinoid
covering Ui = Ui,η of X . Let Γ be the set of divisorial points associated to X. This is just
the union of the Shilov points of the Ui ’s [GM19, Proposition A.3]. Injectivity of (7.4.1)
leads to the desired bound.


## GRs PDF page 4

4                                 W. GUBLER AND J. RABINOFF

Rn as introduced above and a smooth function f i : Rn → R such that u|Vi = f i ◦ ϕi,trop on
Vi . We note that R-PL functions are the special case of piecewise smooth functions where
all the f i ’s can be chosen as affine functions.
    In the theory of Chambert-Loir and Ducros [CD12, §5.4], we can associate to every
continuous real function u on X an associated current [u]. The function h is called
plurisubharmonic (or just psh) in the sense of Chambert-Loir and Ducros if the associated
current d′ d′′ [h] is positive. See [CD12, §5.5] for details. Then we can show the following
maximum principle.
Theorem 1.7. Let X be a good, separated, strictly k-analytic space, and let u be a piecewise
smooth function on X which is psh in the sense of Chambert-Loir and Ducros. If u has a
local maximum on x ∈ X \ ∂ X , then u is locally constant at x.
   Since any semipositive R-PL function is psh in the sense of Chambert-Loir and Ducros
[GJR21, Theorem 7.14], the maximum principle holds for semipositive R-PL functions.
We prove Theorem 1.7 by proving a tropical analogue in Theorem 7.4: namely, if C ⊂
Rn is a tropical variety of pure dimension d and if f : C → R is weakly tropically psh,
in the sense that the Lagerberg current d′ d′′ [ f ] is positive, then f satisfies a similar
maximum principle. The proof uses the Bieri–Groves theorem for affinoid varieties given
in Theorem 1.6. Then Theorem 1.7 is shown in Theorem 7.7.
Remark 1.8. We do not know whether an R-PL function that is psh in the sense of
Chambert-Loir and Ducros is necessarily semipositive. This is strongly related to the
question of whether psh functions are stable under pullback, which is likewise unknown.
Acknowledgments. We are very grateful to Antoine Ducros who helped us with the
argument for the local lifting theorem. We thank Mattias Jonsson for comments about
an earlier draft of the paper.

                                    2. PRELIMINARIES
2.1. General Notation and Conventions. Throughout this paper, k will denote a field
that is complete with respect to a nontrivial, non-Archimedean valuation.
   The set of natural numbers N includes 0. We allow equality in a set-theoretic inclusion
S ⊂ T . If P is any abelian group, we let PΛ := P ⊗Z Λ be the tensor product with Λ. For a
field F , we denote by F an algebraic closure of F .
   For a ring A, the group of invertible elements is denoted by A× . A variety over a field
F is an integral scheme which is of finite type and separated over Spec F .
   A topological space is called compact if it is quasi-compact and Hausdorff.
2.2. Non-Archimedean geometry. A non-Archimedean field is a field k endowed with a
non-Archimedean complete absolute value | |: k → R. The corresponding valuation ring
is denoted by k◦ , its unique maximal ideal by k◦◦ and its residue field by ek = k◦ /k◦◦ . An
analytic extension field is a non-Archimedean field k′ equipped with an isometric embed-
ding k ,→ k′ .
   We will use only good Berkovich analytic spaces over k in the terminology from [Ber93].
These are the k-analytic spaces considered in [Ber90]. Here, good means that every
point of the analytic space X has a neighbourhood isomorphic to the Berkovich spectrum


## GRs PDF page 5

     ON SEMIPOSITIVE PIECEWISE LINEAR FUNCTIONS IN NON-ARCHIMEDEAN ANALYTIC GEOMETRY        5

M (A ) of an affinoid algebra A . We denote by OX the sheaf of analytic functions on a
good analytic space X and by H (x) the completion of the residue field OX ,x /mX ,x . In this
paper, we are mainly concerned with good strictly analytic spaces, which means that we
can choose A above isomorphic to a quotient of a Tate algebra k〈x 1 , . . . , x n 〉. Here, we
recall that
                                      X                                             
                                             m
              k〈x 1 , . . . , x n〉 :=    am x ∈ k¹x 1 , . . . , x n º | lim |am | = 0
                                                              |m|→∞
                                  m

endowed with its Gauss norm. Similarly, we define the subring k◦ 〈x 1, . . . , x n 〉 assuming
all am ∈ k◦ in the above definition. For a (strictly) affinoid algebra A , the subring of
power bounded elements is denoted by A ◦ . The Berkovich spectrum of the Tate algebra
k〈x 1 , . . . , x n 〉 is the closed unit ball of dimension n denoted by Bn .
   For a good strictly k-analytic space X over k, we also consider the G-topology generated
by the strictly affinoid domains. This is most natural for comparison to rigid analytic
geometry: see [Ber93, 1.6].
   An important tool is the relative boundary of a morphism ϕ : X → Y of good k-analytic
spaces. This is a closed subset of X which we denote by ∂ (X /Y ). See [Ber90, §2.5 and
§3.1] for the definition and properties. The complement Int(X /Y ) := X \∂ (X /Y ) is called
the relative interior. Most often we will apply this in the case Y = M (k), in which case
we just set ∂ X := ∂ (X /M (k)). If ∂ X = ;, then we call X boundaryless.
   For a scheme Y of finite type over k, we denote by Y an the Berkovich analytification of
Y . This is a (good) boundaryless strictly k-analytic space. See [Ber90, §3.5] for details.

2.3. Models and formal geometry. Recall that a quasi-compact admissible formal scheme
over k◦ is a quasi-compact formal scheme X over k◦ such that X has an open covering by
affine formal schemes Spf(A) with A a k◦ -algebra which is topologically of finite type and
flat over k◦ . The generic fiber of X is defined on affines by Spf(A)η := M (A ⊗k◦ k), and
the special fibre is defined on affines by Spf(A)s := Spec(A ⊗k◦ ek). There is a canonical re-
duction map red: Xη → Xs which is surjective, anti-continuous, and functorial [GRW17,
Proposition 2.17].
Definition 2.4. Let X be a compact strictly k-analytic space. A formal k◦ -model of X is
a quasi-compact admissible formal scheme X over k◦ with an identification Xη = X . For
details, we refer to [Bos14].
  If L is a line bundle on X , then a formal k◦ -model (X, L) of (X , L) is a formal k◦ -model
X of X and a line bundle L on X with an identification L|X = L.
  A model (X, L) of (X , OX ) gives rise to a metric k kL on OX by requiring that for any
formal open subset U of X and for any frame s of L over U, we have kskL = 1 on Uη . Then
we have an associated (continuous) function hL := − log k1kL on X .
  Let X be a formal k◦ -model of X . The isomorphism classes of line bundles L on X
equipped with an identification L|X = OX form an abelian group denoted by M (X). We
call the elements of the group M (X)Λ := M (X) ⊗Z Λ models of OX with coefficients in Λ.
For L ∈ M (X), we define the metric k kL and the function L by using the above and
Λ-linearity.


## GRs PDF page 15

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
points:


## GRs PDF page 16

16                                W. GUBLER AND J. RABINOFF

5.2. Let X be an admissible formal k◦ -scheme and let x ∈ Xη . Then x ∈ Int(X ) = X \ ∂ X
if and only if the closure of redX (x) is a proper ek-scheme. This follows from [CD12,
Lemme 6.5.1] in the separated case and from [Vil21, Corollary A.4] in general.
Theorem 5.3. Let X be a good, strictly k-analytic space, and let h: X → R be an R-PL
function. For x ∈ X , the following conditions are equivalent.
    (1) The function h is semipositive at x.
    (2) There is a neighborhood W of x such for every strictly analytic neighborhood U ⊂ W
        of x and every Zariski-closed curve C in U, the restriction h|C is semipositive.
Proof. Since semipositivity is an open property that is stable under pullback [GJR21,
Proposition 7.6], it is clear that (1) yields (2).
   Assume that h satisfies (2). By shrinking W , we may assume that W is a strictly affinoid
neighborhood of x and that there is a formal model W of U and a model L of OW on W
with coefficients in R such that h = hL on W . Let Y ⊂ Ws be a curve which is proper over
the residue field ek. To prove semipositivity at x, it is enough to show that degL (Y ) ≥ 0.
   Choose any point y ∈ W reducing to the generic point η of Y . By Theorem 4.1 as
applied to X = W and X = W, there exist z ∈ W with redW (z) = η, a neighborhood U
of z in W , and an irreducible 1-dimensional Zariski-closed subspace C of U containing
z. By shrinking U, we may assume that U is strictly affinoid. By results of Bosch and
Lütkebohmert [Bos14, Theorem 8.4.3] [BL93b, Corollary 5.4(b)], there is a formal model
U of U and a morphism π: U → W extending the inclusion U ,→ W on generic fibers. Let
C be the formal closure of C in U. This is an admissible formal model of C whose special
fiber Cs is a closed 1-dimensional subscheme of Us containing η′ = redU (z). Functoriality
of reductions shows that π(η′ ) = η, so the closure Y ′ of η′ is a curve mapping to Y .
Since the closure of η in Ws is the proper curve Y , we conclude from 5.2 that z ∈ W \
∂ W . The boundary ∂ U is the union of ∂ W ∩ U with the topological boundary of U in
W [Ber90, Proposition 3.1.3], so since U is a neighborhood of z in W , we have z ∈ U \∂ U.
Applying 5.2 to U and its formal model U shows that Y ′ is proper as well. Therefore,
the map Y ′ → Y is finite and surjective. Note that Y ′ is an irreducible component of Cs .
Applying (2) to U and C, we have that h|C is semipositive, and so we deduce from [GJR21,
Lemma 7.4] as applied to (π∗L)|C that degπ∗ L (Y ′ ) ≥ 0. The projection formula then shows
degL (Y ) ≥ 0, as required.                                                                
   To apply results from Thuillier’s thesis [Thu05], we would like to use only smooth an-
alytic curves. To give a variant of the above result suitable for this purpose, we introduce
the following notations:
   For a real function h on X and an analytic field extension F of k, we denote by h F
the induced function on the base change X F = X ⊗     b k F of X . We call an R-PL function
h pluriharmonic if ±h are both semipositive. A strictly k-analytic space X is called rig-
smooth if the sheaf of Kähler differentials, considered on the G-topology, is locally free of
rank equal to the local dimension. The space X is smooth if and only if X is rig-smooth and
boundaryless. See [Duc18] for details (Ducros calls rig-smooth spaces quasi-smooth).
Corollary 5.4. Let X be a good, strictly k-analytic space and let h: X → R be an R-PL
function. Then the following conditions are equivalent:


## GRs PDF page 17

     ON SEMIPOSITIVE PIECEWISE LINEAR FUNCTIONS IN NON-ARCHIMEDEAN ANALYTIC GEOMETRY        17

   (1) The function h is semipositive (resp. pluriharmonic).
   (2) There is an algebraically closed analytic field extension F of k such that for every
       rig-smooth analytic curve C over F and every morphism ϕ : C → X F , the function
       h F ◦ ϕ is semipositive (resp. harmonic) on C.
   (3) There is an algebraically closed analytic field extension F of k such that for every
       smooth analytic curve C over F and every morphism ϕ : C → X F , the function h F ◦ϕ
       is semipositive (resp. harmonic) on C.

   If (2) or (3) is true for an algebraically closed analytic field extension F of k, then
it is true for all analytic field extensions. This follows from Corollary 5.4 and Propo-
sition [GJR21, Proposition 7.6(2’)] which allows to check semipositivity over any field
extension.

Proof. It is enough to prove the claim for semipositive functions, as h is pluriharmonic if
and only if h and −h are semipositive. Since semipositivity is stable under pullback and
extension of scalars [GJR21, Proposition 7.6], clearly (1) yields (2). Since a smooth an-
alytic curve is just a boundaryless rig-smooth curve, it is clear that (2) yields (3). In fact,
these two conditions are equivalent as an R-PL function is automatically semipositive in
every boundary point y of an analytic curve C. Indeed, it follows from 5.2 that red(C, y)
is non-proper and hence there is no condition for semipositivity at y.
   It remains to show that that (2) yields (1). Assume that (2) holds. By base change
using [GJR21, Proposition 7.6(2’)], we may assume that k = F . Let x ∈ X and let U be
a strictly analytic neighborhood of x. For any Zariski-closed curve Y in U, we will show
that h|Y is semipositive. Replacing Y by Yred and using [GJR21, Proposition 7.6(3’)], we
may assume that Y is reduced. Let ϕ : C → Y be the normalization of Y (see [Ber90]
before Proposition 3.1.8). Then C is a rig-smooth curve because k is perfect (it is alge-
braically closed). By (2), the function h ◦ ϕ is semipositive on C. Since the normalization
morphism is finite and surjective, it follows from [GJR21, Proposition 7.6(1’)] that h|Y is
semipositive. By Theorem 5.3, we conclude that h is semipositive at x. Since x was an
arbitrary point of X , we get (1).                                                           
Corollary 5.5. Let X be a good, strictly k-analytic space and let Λ be either Z or Q. Let
h1 , h2 : X → R be semipositive Λ-PL functions. Then max(h1 , h2 ) is a semipositive Λ-PL
function.

  Corollary 5.5 fails for Λ strictly containing Q, but only because we restrict ourselves to
the G-topology generated by strictly analytic domains. See [GJR21, Example 5.3].

Proof. We first note that max(h1 , h2 ) is a Λ-PL function [GJR21, Remark 5.2]. Using
Corollary 5.4, it is enough to prove that max(h1 , h2 ) is semipositive in case of a smooth
analytic curve X . Since the maximum of two subharmonic functions on such a curve is
subharmonic [Thu05, Proposition 3.1.8], the claim follows from Proposition 5.1.          

Theorem 5.6. Let X be a good, strictly k-analytic space and let (h j ) j∈N be a sequence of
semipositive R-PL functions on X converging pointwise to an R-PL function h. Then h is
semipositive.


## Thu PDF page 15

                                                                                                 1



                                 1. Polyèdres entiers




                                       1.1. Généralités
1.1.1. Polytopes
  Soient V un espa e ve toriel réel de dimension nie et Λ un réseau dans l'espa e ve toriel
dual V ∨ . L'espa e ve toriel réel Aff(V ) = R ⊕ V ∨ des fon tions anes sur V est engendré
par le sous-groupe abélien Λ(V ) = R ⊕ Λ.
   Un polytope entier (dans V ) est une partie ompa te et non vide P de V dénie par des
inéquations 0 ≤ ϕ1 , . . . , 0 ≤ ϕn , où ϕ1 , . . . , ϕn ∈ R ⊕ Λ. Les restri tions à P des éléments
de R ⊕ Λ forment un sous-groupe abélien, noté Λ(P ), de l'espa e ve toriel réel Hom(P, R)
des appli ations de P dans R ; 'est la somme de R  identié au sous-groupe des fon tions
 onstantes  et d'un groupe abélien libre de type ni. Le sous-espa e ve toriel de Hom(P, R)
engendré par Λ(P ) est noté ΛR (P ).
Remarque 1.1.1
  1. Un polytope entier est onvexe, don onnexe.
  2. Étant donné un polytope entier P dans V , déni par des inéquations 0 ≤ ϕ1 , . . .,
     0 ≤ ϕn , ϕi ∈ Λ(V ), l'appli ation tautologique
                                        ι : P → ΛR (P )∨
     réalise une bije tion de P sur le sous-ensemble
                   {u ∈ ΛR (P )∨ ; hu, 1i = 1 et hu, ϕi |P i ≥ 0, 0 ≤ i ≤ n},
     h., .i désignant le ro het de dualité.
  3. La remarque pré édente permet d'introduire une notion abstraite de polytope entier :
      'est la donné d'un ouple (P, Λ(P )), formé d'un ensemble non vide P et d'un sous-
     groupe Λ(P ) du groupe abélien Hom(P, R), appelé groupe stru tural de P , qui satisfait
     aux onditions suivantes :
     - Λ(P ) ontient le sous-groupe R des fon tions onstantes ;
     - le quotient Λ(P )/R est un groupe abélien libre de type ni ;
     - notant ΛR (P ) le sous-espa e ve toriel de Hom(P, R) engendré par Λ(P ), l'appli ation
     tautologique
                                       ι : P → ΛR (P )∨
     réalise une bije tion de P sur une partie ompa te de l'hyperplan d'équation hu, 1i = 1
     dénie par un nombre ni d'inégalités hu, ϕi ≥ 0, ϕ ∈ Λ(P ). L'ensemble P est muni de
     la topologie faisant de ι un homéomorphisme et l'on notera abusivement P le polytope
     entier (P, Λ(P )) si ela ne prête pas à onfusion.
  Un morphisme d'un polytope entier P dans un polytope entier P ′ est une appli ation
f : P → P ′ telle que l'homomorphisme f ∗ : Hom(P ′ , R) → Hom(P, R) envoie Λ(P ′ ) dans
Λ(P ). Un sous-polytope entier d'un polytope entier P est une partie non vide de P dénie
par un nombre ni d'inéquations de la forme 0 ≤ ϕ, ϕ ∈ Λ(P ).
  Les fa es d'un polytope entier P sont les parties non vides de P dénies par une équation
ϕ = 0, ϕ ∈ Λ(P ) étant une fon tion positive sur P ; e sont des sous-polytopes entiers de P .
  La dimension d'un polytope entier P , notée dim(P ), est par dénition le rang du groupe
abélien libre Λ(P )/R et le bord ∂P de P est la réunion des fa es de dimension < dim(P ) ; le


## Thu PDF page 16

2



 omplémentaire P − ∂P est l'intérieur de P . La dimension de P oïn ide ave la dimension
topologique de son intérieur.
  Une dé omposition élémentaire d'un polytope entier P est la donnée d'une famille nie D
de sous-polytopes entiers de P vériant les onditions suivantes :
  (i) pour tout Q ∈ D , ha une des fa es de Q appartient à D ;
  (ii) pour tous Q, Q′ ∈ D , Q ∩ Q′ = ∅ ou est une fa e de Q et Q′ ;
  (iii) P est la réunion des Q ∈ D .
Remarque 1.1.2.  Si D est une dé omposition élémentaire de P , la ondition (ii) implique
que deux sous-polytopes distin ts Q, Q′ ∈ D ont des intérieurs disjoints et les onditions (i)
et (iii) montrent que P est la réunion disjointe des intérieurs des Q ∈ D .
   Étant donné un polytope entier P , une appli ation ontinue f : P → R est dite ane par
mor eaux s'il existe une dé omposition élémentaire D de P telle que, pour tout Q ∈ D , la
restri tion de f à Q appartienne à ΛR (Q). L'ensemble des fon tions anes par mor eaux sur
P est un R-espa e ve toriel noté A0 (P ) et A0Z (P ) désigne le sous-groupe abélien des fon tions
 ontinues et anes par mor eaux f pour lesquelles il existe une dé omposition élémentaire D
de P telle que f|Q ∈ Λ(Q) pour tout Q ∈ D .
Remarque 1.1.3.  Soit P un polytope entier ; la atégorie C(P ), dont les objets sont les
sous-polytopes entiers de P et les morphismes les in lusions, est munie d'une topologie de
Grothendie k naturelle pour laquelle les familles ouvrantes sont les re ouvrements nis. Le
fais eau asso ié au préfais eau Q 7→ Λ(Q) (resp. Q 7→ ΛR (Q)) sur C(P ) n'est autre que le
fon teur Q 7→ A0Z (Q) (resp. Q 7→ A0 (Q)).


1.1.2. Polyèdres
   Soit S un espa e topologique séparé dont les omposantes onnexes sont dénombrables à
l'inni ; un atlas Z-polyédral sur S est la donnée d'une famille τ de triplets (V, P, ϕ), onstitués
d'une partie ompa te V de S , d'un polytope entier P et d'un homéomorphisme ϕ de V sur
P , qui satisfait aux onditions suivantes :
    1. pour tous (V, P, ϕ), (V ′ , P ′ , ϕ′ ) ∈ τ , V ∩ V ′ = ∅ ou ϕ(V ∩ V ′ ) (resp. ϕ′ (V ∩ V ′ )) est
       un sous-polytope entier de P (resp. P ′ ) et ϕ′ ◦ ϕ−1 induit un isomorphisme entre les
       polytopes entiers ϕ(V ∩ V ′ ) et ϕ′ (V ∩ V ′ ) ;
    2. pour tout point x ∈ S , il existe (V1 , P1 , ϕ1 ), . . . , (Vn , Pn , ϕn ) ∈ τ tels que x ∈ V1 ∩. . .∩Vn
       et que V1 ∪ . . . ∪ Vn soit un voisinage de x dans S .
    3. pour tout ompa t K de S , il n'existe qu'un nombre ni de artes (V, P, ϕ) ∈ τ telles
       que ϕ(V ) ∩ K 6= ∅.
  Deux atlas Z-polyédraux τ et τ ′ sur S sont dits équivalents si la réunion τ ∪ τ ′ est un atlas
Z-polyédral sur S .
Définition 1.1.4.  Un polyèdre entier est la donnée d'un espa e topologique séparé S et
d'une lasse d'équivalen e d'atlas Z-polyédraux sur S .

Définition 1.1.5.  Un sous-polytope d'un polyèdre entier S est une partie                      ompa te non
vide V de S gurant dans un atlas Z-polyédral.
Remarque 1.1.6.  L'espa e topologique sous-ja ent à un polyèdre entier est lo alement
 ompa t.


## Thu PDF page 71

                                                                                                 57



Remarque 2.3.17.  La dénition du fais eau HX rend évidente les assertions suivantes :
   le fais eau HX sur l'espa e topologique |X| est invariant par les automorphismes
    k-analytiques de X ; plus généralement, si X et Y sont deux ourbes stri tement
    k-analytiques lisses et ϕ : X →Y
                                  ˜ est un k-isomorphisme, l'isomorphisme de fais eaux
      ♯
    ϕ : CY →C˜ X induit un isomorphisme de HY sur HX ;
   pour toute extension nie galoisienne k′ de k, l'opération de G = Gal(k′ /k) sur CX⊗k k′
    stabilise la sous-fais eau HX⊗k k′ et l'isomorphisme anonique CX →     G
                                                                       ˜ CX⊗   kk
                                                                                  ′ induit un

    isomorphisme de HX sur HX⊗k k′ .
                                G


  Étant donné un domaine k-anoïde Y d'une ourbe k-analytique lisse X , nous noterons
H(Y ) le sous-espa e ve toriel
                                   Γ(Y − ∂Y, HX ) ∩ C0 (Y, R)
de C0 (|Y |, R) ; vu le orollaire 2.3.14, ette notation oïn ide ave elle introduite pré édem-
ment lorsque Y est stri tement k-anoïde.
   La orrespondan e Y 7→ H(Y ) est un préfais eau sur le G-site XG de X qui prolonge
évidemment le préfais eau sur le site XR déni au début de 2.3.3.
Proposition 2.3.18.  Soient X une ourbe stri tement k -analytique lisse et K une ex-
tension non ar himédienne de k ; notant XK pour X ⊗       b k K et pK le morphisme anonique
XK → X , pK HX ⊂ HX ⊗
              ∗
                          b kK .
Démonstration. C'est une onséquen e immédiate de la dénition du fais eau HX et du
lemme 2.3.5.                                                                                      2
   A hevons e paragraphe par le résultat suivant :
Proposition 2.3.19.  Soient X, Y deux ourbes stri tement k -analytiques lisses et f :
Y → X un morphisme. Pour toute fon tion harmonique h ∈ Γ(X, HX ), la fon tion f ∗ h = h◦f
est harmonique sur Y : f ∗ h ∈ Γ(Y, HY ).
Démonstration. On peut supposer Y onnexe et f quasi-ni. Étant donnés des domaines
stri tement k-anoïdes W ⊂ Y et V ⊂ X tels que f (W ) ⊂ V , h|V ∈ H(V ) et don , par appli-
 ation des propositions 2.3.3 et 2.3.7, (f ∗ h)|W ∈ H(W ). La fon tion f ∗ h est don harmonique
sur Y .                                                                                      2

2.3.4. Le préfais eau log |OX× |.
  Considérant toujours une ourbe stri tement k-analytique lisse X , examinons mainte-
nant les liens entre les fon tions harmoniques sur X et les fon tions de la forme log |f |,
            ×
f ∈ Γ(X, OX   ).
                                                   ×
Proposition 2.3.20.  Pour toute se tion f ∈ Γ(X, OX ), la fon tion log |f | est harmo-
nique sur X .
Démonstration. Il sut de vérier que la restri tion de la fon tion log |f | à tout domaine
stri tement k-anoïde Y ⊂ X appartient au sous-espa e H(Y ) ⊂ C0 (|Y |, R) ; vu le lemme
2.3.5 et le théorème 2.3.8, on peut en outre supposer que Y est la bre générique d'une S -
 ourbe simplement semi-stable, auquel as il ne reste plus qu'à invoquer le point (iii) de la
proposition 2.2.24.                                                                              2
Théorème 2.3.21.  Soit X une ourbe stri tement k -analytique lisse. Le fais eau de R-
                                                                                                 ×
ve toriels engendré par les germes de fon tions log |f |, f étant un germe de se tion de OX        ,
est un sous-fais eau de HX ; le quotient est un fais eau gratte- iel sur |X| et il est nul si l'une
des deux onditions suivantes est vériée :


## Thu PDF page 72

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


## Thu PDF page 73

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


## Thu PDF page 76

62



Remarque 3.1.4.  Puisque, pour tout domaine stri tement k-anoïde Y , l'espa e ve to-
riel H(Y ) est de dimension nie, la limite h d'une suite simplement onvergente de fon tions
harmoniques sur un ouvert Ω de X est harmonique et la onvergen e est lo alement uniforme
sur Ω.

  Les propriétés du fais eau HX énon ées dans les trois paragraphes pré édents permettent,
en re opiant les démonstration du paragraphe 2.2 du hapitre V de [Ahl℄, de résoudre le
problème de Diri hlet par la méthode de Perron ; e i est l'objet de la n de la se tion 3.1.

3.1.2. Fon tions sous-harmoniques.
Définition 3.1.5.  Soit Ω un ouvert de X ; une fon tion u : Ω → R ∪ {−∞} est dite
sous-harmonique si elle est semi- ontinue supérieurement, n'est identiquement égale à −∞
sur au une omposante onnexe de Ω et satisfait à la ondition suivante : pour tout domaine
stri tement k-anoïde Y dans X et toute fon tion h ∈ H(Y ),
                                  (u|∂Y ≤ h|∂Y ) =⇒ (u|Y ≤ h).

     L'assertion suivante n'est pas surprenante.
Proposition 3.1.6.  Soient Ω ⊂ X un ouvert et f ∈ Γ(Ω, OX ) une se tion inversible
sur un ouvert dense de Ω ; la fon tion log |f | est sous-harmonique sur Ω.
Démonstration. La fon tion log |f | est ontinue sur Ω et, f étant inversible sur un ouvert
dense, n'est identiquement égale à −∞ sur au une des omposante onnexes de Ω.
   Soient Y ⊂ Ω un domaine stri tement k-anoïde et h ∈ H(Y ) une fon tion majorant log |f |
sur Γ(Y ) = ∂Y ; puisqu'il sut de prouver l'inégalité log |f ||Y ≤ h après avoir ee tué une
extension nie k′ de k, nous pouvons supposer que Y est la bre générique d'une S - ourbe
simplement semi-stable Y , de squelette S(Y) et de rétra tion τY : Y → S(Y). Dans es
 onditions :
    H = h|S(Y) ∈ H(S(Y), Γ(Y )) et h = H ◦ τY ;
    la fon tion F = log |f ||S(Y) est sous-harmonique sur S(Y) − Γ(Y ) (proposition 2.2.24,
     (iii)) et log |f ||Y ≤ F ◦ τY (proposition 2.2.24, (ii)) ;
la on lusion dé oule alors de l'inégalité F ≤ H sur S(Y).                                  2
Remarque 3.1.7.  Nous verrons plus loin (proposition 3.4.6) que, pour toute S - ourbe
simplement semi-stable X et toute fon tion sous-harmonique u sur Xη − Γ(Xη ), la restri tion
U de u à S(X ) − Γ(Xη ) est sous-harmonique (= onvexe) : ddc U ≥ 0, l'opérateur ddc étant
entendu au sens des ourants, omme expliqué à en 1.2.5.

     Les propriétés suivantes des fon tions sous-harmoniques sont évidentes.
Proposition 3.1.8.  Étant donné un ouvert Ω de X ,
   (i ) l'ensemble des fon tions sous-harmoniques sur Ω est un ne réel stable par max : pour
toutes fon tions u, v sous-harmoniques sur Ω et tous nombres réels positifs µ, ν , les fon tions
µu + νv et max(u, v) sont sous-harmoniques sur Ω ;
   (ii ) l'enveloppe inférieure d'une famille dé roissante de fon tions sous-harmoniques sur Ω
est, sur ha une des omposantes onnexes de Ω, sous-harmonique ou identiquement égale à
−∞ ;
   (iii ) la régularisation semi- ontinue supérieurement de l'enveloppe supérieure d'une famille
 roissante et lo alement bornée de fon tions sous-harmoniques sur Ω est sous-harmonique.

     Le ne des fon tions sous-harmoniques sur un ouvert Ω de X est noté SH(Ω).


## Thu PDF page 77

                                                                                               63



Lemme 3.1.9.  Soit Y     un domaine stri tement k-anoïde onnexe dans X ; toute fon -
tion sous-harmonique u sur un voisinage de Y prend des valeurs nies aux points de Γ(Y ) =
∂Y .

Démonstration. Raisonnons par l'absurde en supposant qu'il existe une fon tion sous-
harmonique u sur un voisinage Ω de Y prenant la valeur −∞ en un point x de Γ(Y ). Notant
M un majorant de u sur Γ(Y ), le lemme 2.3.9 fournit, pour tout entier naturel N , une fon tion
hN dans H(Y ) valant −N en x et égale à M sur Γ(Y ) − {x} ; la suite (hN ) est dé roissante et
 onverge, lo alement uniformément sur Y − Γ(Y ), vers −∞ par appli ation du lemme 2.3.10.
La restri tion de u à Y − Γ(Y ), majorée par hN pour tout N , est don identiquement égale
à −∞.
   Étant donné un domaine stri tement k-anoïde Y ′ dans X dont le bord de Shilov ren ontre
Int(Y ) = Y −Γ(Y ), le raisonnement pré édent implique u|Int(Y ′ ) = −∞. On onsidère alors un
re ouvrement lo alement ni V de la omposante onnexe de x dans Ω par des domaines stri -
tement k-anoïdes de X tel qu'il existe pour tout V ∈ V un domaine V ′ dans V satisfaisant à
la ondition : Γ(V ) ∩ Int(V ′ ) 6= ∅. D'après la première partie de la démonstration, la fon tion
u est identiquement égale à −∞ sur la omposante onnexe de x dans Ω, en ontradi tion
ave la dénition 3.1.5.                                                                         2

Remarque 3.1.10.  1. Le résultat pré édent sera étendu plus loin (3.4.10) au as d'un
domaine k-anoïde quel onque dans X .
2. Le lemme 3.1.9 permet de reformuler ainsi la dénition de la sous-harmoni ité : une fon -
tion semi- ontinue supérieurement u : Ω → R ∪ {−∞} est sous-harmonique si elle n'est pas
identiquement égale à −∞ sur une omposante onnexe de Ω et si, pour tout domaine stri te-
ment k-anoïde V in Ω, la fon tion h ∈ H(V ) qui oïn ide ave u sur Γ(V )  dont l'existen e
dé oule des lemmes 3.1.9 et 2.3.9  majore u sur tout Y . Cette dénition est équivalente à
la pré édente en vertu du prin ipe du maximum pour les fon tions harmoniques (proposition
3.1.1).

   Soit Ω un ouvert de X ; l'ensemble des points de Shilov des domaines stri tement k-
anoïdes de X étant partout dense, le lemme pré édent implique immédiatement que la
restri tion d'une fon tion sous-harmonique sur Ω à un ouvert Ω′ ⊂ Ω ne peut être identique-
ment égale à −∞ sur au une omposante onnexe de Ω′ . La orrespondan e Ω 7→ SH(Ω) est
par onséquent un préfais eau de nes réels sur |X|. Nous bientt qu'il s'agit en fait d'un
fais eau ( orollaire 3.1.13).
  Les fon tions sous-harmoniques satisfont au prin ipe du maximum suivant.

Proposition 3.1.11.  Étant donné un ouvert Ω de X , une fon tion sous-harmonique u
sur Ω admettant un maximum lo al en un point x de Ω est lo alement onstante au voisinage
de x.

Démonstration. Soit u une fon tion sous-harmonique admettant un maximum au point x
de Ω et soit U un voisinage ouvert onnexe de x dans Ω tel que u|U ≤ u(x) ; puisque u|U n'est
pas identiquement égale à −∞, u(x) > −∞.
   Soit Y un voisinage stri tement k-anoïde onnexe Y de x dans U . La restri tion de u à
Γ(Y ) est onstante, égale à u(x) : s'il existait, en eet, un point y ∈ Γ(Y ) tel que u(y) < u(x),
le lemme 2.3.9 fournirait une fon tion h ∈ H(Y ) telle que
    h(y) = u(y) ;
    h|Γ(Y )−{y} = u(x) ;


## Thu PDF page 82

68



Démonstration. Il sut d'appliquer les deux propositions pré édentes à l'ouvert relative-
ment ompa t Int(Y ) ⊂ X .                                                                     2


                            3.2. Fon tions lisses, opérateur ddc
   Disposant du fais eau HX des germes de fon tions harmoniques sur une ourbe stri tement
k-analytique lisse X et de la résolution partielle du problème de Diri hlet obtenue à la se tion
pré édente, nous allons maintenant dénir les fais eaux A0X (resp. A1X ) des germes de fon tions
lisses (resp. formes lisses ) sur X et un  opérateur de Lapla e  ddc : A0X → A1X ; elui- i
sera lassiquement étendu à des espa es de distributions dans la se tion suivante.

   Désignons par I(X) l'ensemble des points de X de type (2) ou (3) ; de manière équivalente,
I(X) est l'ensemble des points de Shilov des domaines k-anoïdes de X . Plus pré isément :
le bord de Shilov Γ(Y ) d'un domaine k-anoïde Y de X est un sous-ensemble ni de I(X) et
toute partie nie S de I(X) est la réunion des bords de Shilov d'un nombre ni de domaines
k-anoïdes.

3.2.1. Les fais eaux A0X et A1X sur XG .
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


## Thu PDF page 83

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


## Thu PDF page 84

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
   Soit E un espa e topologique lo alement ompa t. L'ensemble des fon tions réelles onti-
nues sur E dont le support est ontenu dans un ompa t K de E est noté C0 (E, R)K et la
norme supK |.| en fait un espa e de Bana h. La restri tion de E à K induit une isométrie
de C0 (E, R)K sur le sous-espa e ve toriel fermé de l'espa e de Bana h C0 (K, R) formé des
fon tions s'annulant sur ∂K = K ∩ E − K .
   L'espa e ve toriel C0c (E, R) des fon tions réelles ontinues sur E dont le support est ompa t
est muni de la topologie lo alement onvexe limite indu tive des topologies d'espa es de
Bana h sur les C0 (E, R)K ; 'est la topologie lo alement onvexe la plus ne rendant ontinues
les inje tions C0 (E, R)K → C0c (E, R).
   Lorsque E est l'espa e topologique sous-ja ent à une ourbe stri tement k-analytique lisse
X , il est loisible de ne onsidérer que des ompa ts K qui sont des domaines stri tement
k-analytiques (i.e. des réunions nies de domaines stri tement k-anoïdes) : tout ompa t de
X est en eet ontenu dans un domaine stri tement k-analytique ompa t.
Proposition 3.2.7.  Le sous-espa e Ac (X) est dense dans Cc (X, R).
                                                0                      0

Démonstration. Soient K un domaine k analytique ompa t de X , ε ∈ R>0 et f une
fon tion ontinue sur X s'annulant en dehors de K . De l'uniforme ontinuité de f sur K
dé oule l'existen e d'une famille nie V de domaines k-anoïdes dans X dont la réunion K ′
 ontient K et telle que, pour tout V ∈ V et tous x, y ∈ V , |f (x) − f (y)| ≤ ε/2. Appliquant
le lemme suivant au domaine k-analytique ompa t K ′ et au sous-ensemble Σ réunion des
points de Shilov des V ∈ V et de la frontière de K , il existe une fon tion g ∈ A0 (X) telle que
gΣ = fΣ . Cette fon tion s'annule sur la frontière de K ′ et appartient don à A0 (X)K .
   Étant donné V ∈ V , la fon tion g satisfait, par onstru tion, à l'inégalité
                                                          ε
                                         |g(x) − g(y)| ≤
                                                          2


## Thu PDF page 103

                                                                                               89



          3.4. Fon tions sous-harmoniques et mesures de Radon positives
   Nous poursuivons dans ette se tion l'étude des fon tions sous-harmoniques sur une ourbe
stri tement k-analytique lisse X , dénies en 3.1.2, à l'aide de l'opérateur ddc . Les notations
introduites dans l'énon é de la proposition 3.3.7 seront librement employées.

3.4.1. Le théorème d'approximation.
   En vertu de la proposition 3.4.10, une fon tion sous-harmonique u sur X dénit une fon tion
réelle sur I(X) et détermine par onséquent un ourant dans D0 (X).
Lemme 3.4.1.  L'appli ation

                               SH(X) → D0 (X),         u 7→ u|I(X)
est inje tive et son image est l'ensemble des ourants T ∈ D0 (X) satisfaisant à la ondition
suivante :
              pour tout domaine k-anoïde V ⊂ X et tout point x ∈ I(V ) − ∂V ,
                                        T (x) ≤ hT, νxV i.
Démonstration. Soient u une fon tion sous-harmonique sur X et x un point dans X − I(X).
  Étant donnée une suite dé roissante (Vn ) de domaines k-anoïdes de X dont le bord de
Shilov Γ(Vn ) est réduit à un point xn et telle que
                                                 \
                                         {x} =      Vn ,
                                                  n

le prin ipe du maximum (proposition 3.1.11) implique les inégalités u|Vn ≤ u(xn ) ; la suite
(u(xn )) est don dé roissante et u(x) ≤ inf n u(xn ). D'autre part, en vertu de la semi- ontinuité
supérieure de u,
                              u(x) ≥ limsupn u(xn ) = inf u(xn ).
                                                         n
La fon tion u est ainsi uniquement déterminée par sa restri tion au sous-ensemble I(X) de
X.
  La des ription de l'image de l'appli ation SH(X) → D0 (X) est une appli ation dire te du
point (ii) du orollaire 3.3.9.                                                           2
  Le lemme pré édent nous permettra de ne pas distinguer une fon tion sous-harmonique sur
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


## Thu PDF page 104

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
Remarque 3.4.3.  La démonstration i-dessus s'adapte aisément dans un ontexte ar hi-
médien et permet de démontrer un résultat d'approximation global pour les fon tions sous-
harmoniques sur une surfa e de Riemann (voir la proposition 4.2.14).
   La ara térisation des fon tions sous-harmoniques lisses est sans surprise.
Proposition 3.4.4.  Une fon tion lisse ϕ ∈ A (X) sur une ourbe stri tement k -
                                                       0

analytique lisse X est sous-harmonique si et seulement si ddc ϕ ≥ 0.
Démonstration. Soit ϕ une fon tion dans A0 (X) telle que ddc ϕ ≥ 0.
   Soient V ⊂ X un domaine k-anoïde et h une fon tion dans H(V ) qui majore ϕ sur ∂V ;
il est susant, pour prouver l'inégalité
                                            ϕ|V ≤ h,
d'établir que ϕ|V est majorée par la fon tion h′ dans H(V ) qui oïn ide ave ϕ sur ∂V ( ar
h′ ≤ h d'après le prin ipe du maximum).
   L'inégalité ddc (h′ − ϕ) = −ddc ϕ ≤ 0 sur V − ∂V implique que la fon tion h′ − ϕ n'a pas
de minimum lo al stri t sur V − ∂V ( orollaire 3.2.11, (ii)) ; elle atteint don son minimum
en un point de ∂V et, puisque (h′ − ϕ)|∂V = 0,
                                            ϕ|V ≤ h′ .
     La fon tion ϕ est ainsi sous-harmonique sur X .
   Soit ré iproquement ϕ ∈ A0 (X) une fon tion lisse et sous-harmonique. Étant donné un
point x du support S de ddc ϕ, onsidérons un domaine k-anoïde V ⊂ X tel que S ∩ (V −
∂V ) = {x} et soit h la fon tion h ∈ H(V ) qui est égale à ϕ sur S. La fon tion ϕ|V − h est
négative et elle s'annule identiquement sur ∂V .
   La forme lisse (ddc (ϕ− h))|V −∂V = (ddc ϕ)|V −∂V est, par hypothèse, non nulle et portée par
{x}. La première ondition implique l'existen e d'un minimum lo al stri t pour la fon tion
(ϕ − h)|V −∂V et elui- i est né essairement réalisé en un point y ∈ I(Y ) − ∂Y ar ϕ − h est
lo alement onstante en tout point de Y − I(Y ). On en déduit l'inégalité
                                         Z
                                             ddc ϕ > 0
                                           {y}


## Thu PDF page 105

                                                                                                 91



par appli ation du point (ii) du orollaire 3.2.11 et don y = x, (ddc ϕ)|V −∂V ≥ 0.
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

   L'utilisation simultanée du théorème d'approximation et de la ara térisation des fon tions
sous-harmoniques lisses permet également de répondre à une question naturelle mentionnée
à la remarque 3.1.7.
Proposition 3.4.6.  Soient X           une S - ourbe simplement semi-stable et u une fon tion
sous-harmonique sur Xη ;
    la restri tion U de u au squelette S(X ) de X est une fon tion réelle sous-harmonique (=
      onvexe ) ontinue ;
    u ≤ U ◦ τX .
Démonstration. L'inégalité u ≤ U ◦ τX est une onséquen e immédiate du prin ipe du
maximum puisque les bres de la rétra tion τX sont des domaines k-anoïdes dont le bord
est réduit à un point.
   La restri tion U de u au squelette S(X ) est à valeurs nies ar S(X ) ⊂ I(Xη ) et, ompte
tenu du théorème 3.4.2, U est l'enveloppe inférieure d'une famille dé roissante de fon tions
qui sont les restri tions de fon tions lisses et sous-harmoniques sur Xη . Il est par onséquent
susant de prouver qu'une fon tion lisse et sous-harmonique ϕ sur Xη se restreint en une
fon tion ane par mor eaux et sous-harmonique sur le polyèdre S(X ).
   Nous pouvons supposer la ourbe quasi- ompa te puisque la question est lo ale sur S(X ) ;
l'assertion sera d'autre part démontrée si elle l'est après passage à une extension nie k′ de k.
Appliquant la proposition 3.2.4 et le lemme 2.2.22, il existe dans es onditions un é latement
admissible q : Y → X tel que :
    Y soit une S - ourbe simplement semi-stable,
    ϕ = Φ ◦ τY , ave Φ = ϕ|S(Y) ∈ A0 (S(Y)).
   La fon tion Φ est sous-harmonique puisque ddc Φ = ddc ϕ ≥ 0 (théorème 3.2.10).


## GJR PDF page 30

30                              W. GUBLER, P. JELL, AND J. RABINOFF

x ∈ NΓ . Then Sϕ (X ) ∩ X ω is the Shilov boundary of X ω by Remark 3.19. Hence we
may assume x ∈ Sϕ (X ) ∩ X ω as otherwise all tropical multiplicities are zero. Using the
notations of 4.14, we let Ke (C x ) denote the function field of C x . The homomorphism
                                                  ∼
Aω → H (x) induces an isomorphism K     e (C x ) −→ Hf(x) by [Ber90, Proposition 2.4.4(ii)].
                            ◦                                                            e (M
By the definition of Aω ⊂ Aω , the function field of ιs (C x ) is precisely the subfield K  e (x))
of Remark 3.8. We have length(OX ,x ) = 1 because X is reduced, so
                                f(x) : K
                  mϕ (X , x) = [H      e (M
                                          e (x))] = [C x : ι(C x )] = mrel (x)
by Remark 4.2(8).                                                                              
Example 4.16 (Continuation of Example 3.15). We continue with the notation in Exam-
ple 3.15. By [BPR16, Theorem 5.8], for any point P in the interior of an edge e in the
skeleton S, the relative multiplicity mrel (P) is equal to the “expansion factor” of the edge e
with respect to the tropicalization map ϕtrop . In this situation, the expansion factor of
every edge is equal to 1, except for the edge BD, which has expansion factor 0 as it is
crushed to a point.
   We claim that mϕ (X , P) = 1 for P ∈ {A, B, C, D}. This can be checked directly from
the definition of mϕ (X , P). We give the proof in case P = A which reduces to the generic
point of the line x = 0 in the special fiber of Xmin . By [Ber90, Proposition 2.4.4(ii)],
we have H  f(A) = K e ( y). Recall that trop(A) = (1, 0). If M = Z2 be the character lattice
of T = G2m , then Ke ( M(A))
                       e      is the subfield of H f(A) generated by the reductions of x/p
and of y/1 = y. This shows H     f(A) = K e (M
                                             e (A)), and hence 4.2(8) yields that mϕ (X , A) =
[Hf(A) : K
         e (Me (A))] = 1. The proof for the points P = B, C, D is similar.
   We conclude that mrel (P) = mϕ (X , P) = 1 for every point P of Sϕ (X ). It follows that
mϕ (X , ω) just counts the preimages of ω in Sϕ (X ) under ϕtrop ; these tropical multiplicities
are indicated in Figure 1.

                              5. PIECEWISE LINEAR FUNCTIONS
   In this section we discuss piecewise linear functions on analytic spaces. Most of these
results are standard in one form or another: for instance, see [CD12, Gub98, GM19].
However, the terminology in the literature is somewhat nonstandard, so it is important
to fix our ideas. We will find it useful to work slightly more generally with piecewise
linear functions with slopes contained in an additive subgroup Λ ⊂ R, and in some cases
new arguments are needed. In practice we will usually take Λ = Z, Q, or R, in which case
either Λ = Z or Λ is divisible.
   In this section, K is a non-Archimedean field with a non-trivial valuation v and value
group Γ := v(K × ) ⊂ R. We consider a good strictly K-analytic space X and an additive
subgroup Λ ⊂ R. Recall from 2.3 that a strictly analytic space is good provided that that
every point has a strictly affinoid neighbourhood. Most strictly analytic spaces occurring
in practice are good: for example, any strictly affinoid space, a space with no boundary,
or an analytic subdomain of the analytification of an algebraic variety. We restrict our
attention to good spaces as then the coherent modules on the Berkovich space X are
the same as the coherent modules on the space X G endowed with the G-topology [Ber93,
Proposition 1.3.4], which makes it reasonable to work with line bundles on X . We always


## GJR PDF page 31

               FORMS ON BERKOVICH SPACES BASED ON HARMONIC TROPICALIZATIONS                       31

use the G-topology on X generated by the strictly affinoid domains. Let C(X ) be the space
of continuous real functions on X .
Definition 5.1. A function h: X → R is called piecewise Λ-linear or Λ-PL if there exists a
                                                                                                    ×
G-covering {XP i } of X such that for each i, there are finitely many λi j ∈ Λ and f i j ∈ O (X i )
with h|X i = j λi j log | f i j |. A Z-PL function is called piecewise linear or PL.
  We denote the group of PL functions on X by PL(X ), and the group of Λ-PL functions
by PLΛ (X ). These are subgroups of C(X ).
5.2. Some remarks:
   (1) A function h: X → R is PL if and only if there exists a G-covering {X i } of X and
       f i ∈ O (X i )× such that h|X i = log | f i |.
   (2) The set of Λ-PL functions on X forms a group since any two G-coverings {X i } and
       {X ′j } admit the common refinement {X i ∩ X ′j }.
   (3) The restriction of a Λ-PL function to a strictly analytic domain is Λ-PL.
   (4) The presheaf U 7→ PLΛ (U) is a sheaf in the G-topology, and therefore in the ana-
       lytic topology as well.
   (5) A function h: X → R is Λ-PL if and only if there exists a G-covering {X i } of
       X suchPthat for each i, there are finitely many λi j ∈ Λ and hi j ∈ PL(X i ) with
       h|X i = j λi j hi j .
   (6) A function h: X → R is Q-PL if and only if, locally in the analytic topology, there
       exists a positive integer N such that N h is PL.
   (7) If Λ = Z or Λ = Q then the minimum and maximum of two Λ-PL functions is
       again Λ-PL by [GM19, Proposition 2.12(d)].
Example 5.3. The assertion of 5.2(7) is not true for Λ strictly containing Q. For example,
if the value group of K is Q and X = Gan m
                                            = Spec(K[t ±1])an is the split torus of rank 1, then
the tropicalization of any strictly affinoid domain in X is a union of compact intervals with
rational vertices. We conclude that for Λ = R, the function h := π log |t|+1 = −π trop +1
is Λ-PL, but max(h, 0) is not Λ-PL as max(h, 0) = ϕ ◦ trop for ϕ(u) = max(−πu + 1, 0),
and as the piecewise linear function ϕ has a bend at the irrational number 1/π.
  Here we list some basic functoriality properties of Λ-PL functions.
Lemma 5.4. Let h: X → R be a function.
   (1) Let f : X ′ → X be a morphism of good strictly K-analytic spaces. If h ∈ PLΛ (X ) then
       h ◦ f ∈ PLΛ (X ′ ).
   (2) Let K ′ /K be a non-Archimedean field extension, let X ′ = X ⊗
                                                                    b K K ′ , and let π: X ′ → X
       be the structure morphism. If h ∈ PLΛ (X ) then h ◦ π ∈ PLΛ (X ′ ).
   (3) Let ι : X red → X be the inclusion of the reduction of X , and let h′ = h ◦ ι. Then
       h ∈ PLΛ (X ) if and only if h′ ∈ PLΛ (X red ).
Proof. The first two assertions are obvious. For the third, by (1), the only thing to show is
that if h′ is Λ-PL then h is Λ-PL. Let U = M (A ) ⊂ X be a strictly    Paffinoid domain, and let
                                                           ′                                    ×
Ured = M (Ared ) ⊂ X red be its reduction. Suppose that P h |Ured = λi log |g i | for g i ∈ Ared  .
If f i ∈ A lifts g i then f i ∈ A × is a unit, and h|U = λi log | f i |. Since X red has a G-cover
by such affinoid domains, the same is true for X , so h is Λ-PL.                                 


## GJR PDF page 46

46                               W. GUBLER, P. JELL, AND J. RABINOFF

  Combined with 5.6, we see that a PL function h: X → R on a paracompact space X is
semipositive (resp. harmonic) if and only if there exists a formal K ◦ -model X of X and a
nef (resp. numerically trivial) line bundle L ∈ M (X) such that h = hL = − log k1kL .
  We have the following alternative characterization of harmonic functions. We do not
know if the same characterization holds for semipositive functions.
Proposition 7.5. Let h: X → R be a Λ-PL function and let x ∈ X . Then h is harmonic Pm at x
if and only if there exists a strictly analytic neighbourhood U of x such that h|U = i=1 λi hi
for Z-harmonic functions h1 , . . . , hm on U and λ1 , . . . , λm ∈ Λ.
Proof. The proposition is vacuous when Λ = Z, so assume Λ is divisible. The “if” direc-
tion is trivial. Suppose then thatPmh is harmonic at x. By Proposition 5.8, after shrinking
X , we may assume that h = i=1 λi hi for λ1 , . . . , λm ∈ Λ and h1 , . . . , hm ∈ PL(X ). By
Lemma 5.10, we may assume that   Pm λ1 , . . . , λm are Q-linearly independent. By Lemma 6.18,
the residue Lh (x) is equal to i=1 λi Lhi (x). Let V be a model for red(X , x) in the sense
of 6.2 such that each Lhi (x) is the pullback of a line bundle L V,i on V . Let C ⊂ V be an inte-
                                                                            Pm
gral, proper closed curve. Since Lh (x) is numerically trivial, we have i=1 λi c1 (L V,i (x)).C =
0. But c1 (L V,i (x)).C ∈ Z for each i, so by linear independence, we have c1 (L V,i (x)).C = 0
for each i. Thus L V,i is numerically trivial, so hi is harmonic.                              
     Now we gather some functoriality properties of semipositive and harmonic functions.
Proposition 7.6. Let X be a good strictly K-analytic space and let h ∈ PLΛ (X ).
   Let f : X ′ → X be a morphism of good strictly K-analytic spaces and let h′ = h ◦ f .
     (1) For x ′ ∈ X ′ , let x = f (x ′ ). If h is semipositive at x, then h′ is semipositive at x ′ .
           The converse holds if x ′ ∈ Int(X ′ /X ).
    (1′ ) If h is semipositive, then h′ is semipositive. The converse holds if f is proper and
           surjective.
Let K /K be a non-Archimedean field extension, let X ′ = X ⊗
       ′                                                             b K K ′ , let π: X ′ → X be the
structure morphism, let x ′ ∈ X ′ , let x = π(x ′ ), and let h′ = h ◦ π.
     (2) If h is semipositive at x, then h′ is semipositive at x ′ . The converse holds if we have
           tr.deg(Ke ′H  f(x)/K
                              e ′ ) = tr.deg(Hf(x)/K e ), where K
                                                                e ′H
                                                                   f(x) is the smallest subfield of
           Hf(x ) containing H
                 ′                f(x) and K e.′

    (2 ) The function h is semipositive if and only if h′ is semipositive.
       ′

Let ι : X red → X be the inclusion of the reduction of X and let h′ = h ◦ ι.
     (3) For x ′ ∈ X red , the function h is semipositive at x = ι(x ′ ) if and only if h′ is semipos-
           itive at x ′ .
    (3 ) The function h is semipositive if and only if h′ is semipositive.
       ′

The statements (1)–(3) and (1′ )–(3′ ) hold with “semipositive” replaced by “harmonic.”
Proof. In each case, harmonicity follows easily from semipositivity. In all cases, the func-
tion h′ is Λ-PL by Lemma 5.4.
   We prove first (1). If h is semipositive at x then h′ is semipositive at x ′ by Lemma 6.12
and functoriality of reduction. The converse holds if x ∈ Int(X ′ /X ) by Theorem 6.15
and Lemma 6.12(1), using functoriality of residues 6.19. Assertion (1′ ) follows because
a proper morphism has no boundary.


## GJR PDF page 47

                 FORMS ON BERKOVICH SPACES BASED ON HARMONIC TROPICALIZATIONS                             47

  To prove (2), let ϕ : PHf(x ′ )/Ke ′ → PHf(x)/Ke be the natural morphism. We have seen in 6.13
that ϕ −1 (red(X , x)) = red(X ′ , x ′ ). The assertions now follow from Lemma 6.12 and
functoriality of residues 6.19. To prove (2′ ), by Corollary 5.9 we may shrink X such that
X is compact with formal model X and such that there is L ∈ M (X)Λ with h = hL . Then
the claim follows from Lemma 6.8(2) and Lemma 7.4.
  The claims (3) and (3′ ) follow from (7.6,1′ ) since X red → X is proper and surjective. 
 The following proposition allows us to pass to Galois extensions when studying har-
monic and semipositive functions.
Proposition 7.7. Suppose that Λ is divisible. Let L/K be a (potentially infinite) normal
extension with automorphism group G := Aut(L/K). Let K ′ be the completion of L and let
X ′ := X ⊗
         b K K ′ , with structure morphism π: X ′ → X . Then h 7→ h ◦ π induces an isomor-
phism from the monoid of semipositive Λ-PL functions on X (resp. the group of Λ-harmonic
functions on X ) to the monoid of G-invariant semipositive Λ-PL functions on X ′ (resp. the
group of G-invariant Λ-harmonic functions on X ′ ).
Proof. This is an immediate consequence of Corollary 5.13 and Proposition 7.6(2′ ).                       
  Our next goal is to approximate locally semipositive metrics by local Fubini–Study
metrics (Proposition 7.10). This will be a crucial ingredient in proving the balancing
condition in Section 9.
  Recall that a line bundle on a scheme Y is called semiample if some positive tensor
power is globally generated. We say that L ∈ Pic(Y )R is ample (resp. semiample) if there
P r ample (resp. semiample) line bundles H1 , . . . , H r and λ1 , . . . , λ r ∈ R≥0 such that L =
are
     λ H ∈ Pic(Y )R . An ample L is semiample and a semiample L is nef.
  j=1 j j

Definition 7.8. Let h: X → R be an R-PL function. We say that h is Fubini–Study at a
point x ∈ X if Lh (x) is semiample. We say that h is locally Fubini–Study or LFS if it is
Fubini–Study at every point of X .
  Clearly if h is Fubini–Study at x then it is semipositive at x.
7.9. It follows from [CD12, Proposition 6.8.2] that h is Fubini–Study at x if and only if
there is an open neighbourhood U of x such that h|U is an R≥0 -linear combination of func-
tions of the form max{− log | f1 |, . . . , − log | f n |} for invertible analytic functions f1 , . . . , f n
on U.
  The following proposition can be seen as a local analogue of the fact that one can
approximate a nef Q-line bundle by ample Q-line bundles on a projective variety.
Proposition 7.10. Let h: X → R be an R-PL function that is semipositive at a point x ∈
Int(X ). Then there exists a strictly analytic neighbourhood U of x and a sequence h1 , h2 , . . .
of R-PL LFS functions on U such that hi → h|U uniformly.
Proof. We may shrink X to assume it is compact. By Corollary 5.9, we may assume that
there exists a formal K ◦ -model X of X and a line bundle L ∈ M (X)R with h = hL , using
the notation of 5.7. Since x is inner, the closure VX,x of redX (x) in Xs is proper (with the
notation of 6.13): see [CD12, Lemma 6.5.1] and [Vil21, Appendix A]. By Chow’s lemma,


## GJR PDF page 48

48                               W. GUBLER, P. JELL, AND J. RABINOFF

there is a proper birational morphism V → VX,x with V projective over K              e . Let L ′ be an
                                                                                ′
ample line bundle on V . By [CD12, 6.6.5], there is a PL function h on the germ (X , x)
such that (V, L ′ ) is a model of the residue Lh′ (x). Let U be a compact strictly analytic
neighbourhood of x on which h′ is defined. Then there is a formal K ◦ -model U of U and
a line bundle L′ on U with h′ = hL′ . By Lemma 6.14, there is a compact strictly analytic
neighbourhood U ′ of x and a formal K ◦ -model U′ of U ′ such that the closure V ′ := VU′ ,x
of redU′ (x) dominates V . We may assume that U ′ ⊂ U and that this inclusion extends to
a morphism f : U′ → U by using Raynaud’s theorem. Let L ′ |V ′ be the pull-back of L ′ with
respect to V ′ → V . Then L ′ |V ′ and f ∗ (L′ )|V ′ are both models for Lh′ (x). We conclude that
there is a dominating model V ′′ of red(X , x) such that the pull-backs of L ′ |V ′ and f ∗ (L′ )|V ′
to V ′′ agree. Using Lemma 6.14 again and the arguments above, we may assume that
V ′′ = VU′′ ,x for a formal K ◦ -model U′′ of a compact strictly analytic neighbourhood U ′′
of x contained in U ′ such that the inclusion U ′′ ⊂ U ′ extends to a morphism U′′ → U′ .
Moreover, we may assume that U ′′ ⊂ X extends to a morphism U′′ → X. Replacing X by
U′′ and L, L′ by their pull-backs to U′′ , we put ourselves in the following situation:
     (1) The closure V ′ of redX (x) in Xs dominates V .
     (2) There is L ∈ M (X)R and L ∈ Pic(V )R such that h = hL and L|V ′ is the pullback of
         L under V ′ → V , and such that (V, L) is a model of Lh (x).
     (3) There is a line bundle L′ on X and an ample line bundle L ′ on V such that h′ = hL′
         and L′ |V ′ is the pullback of L ′ under V ′ → V .
We recycle notation now and let U := red−1       X
                                                     (V ′ ). By anticontinuity of the reduction map,
the set U is an open neighbourhood of x. For ǫ ∈ Q>0 let Lǫ := L + ǫ L ′ , Lǫ := L + ǫ L′ ,
and hǫ := hLǫ = h + ǫh′ . Then hǫ is an R-PL function on X and Lǫ |V ′ is the pullback of Lǫ
under V ′ → V . Note that hǫ → h uniformly as ǫ → 0. If h is semipositive at x then L is
nef by Lemma 6.11, so Lǫ is ample as a consequence of Kleiman’s theorem, see [Laz04,
Corollary 1.4.10]. It follows that Lǫ |V ′ is semiample. If y ∈ U then redX ( y) ∈ V ′ , so the
closure Y of redX ( y) in Xs is contained in V ′ . Since h = hL and h′ = hL′ on all of X ,
the pair (Y, Lǫ |Y ) is a model of Lhǫ ( y) by the construction in 6.16. Since Lǫ |Y is again
semiample, we see that hǫ is Fubini–Study at y. Thus hǫ is LFS on U.                                 
Remark 7.11. Let X be a proper scheme over K. It is shown in [GM19, Section 5] that
a pointwise limit of semipositive Q-PL metrics is semipositive. We expect the analogous
result to hold in our situation. In particular, we expect the converse of Proposition 7.10
to hold true: namely, if an R-PL function h is a uniform limit of R-PL LFS functions on
a strictly analytic neighbourhood U of an interior point x, then h is semipositive at x.
This would imply that if h and h′ are R-PL functions that are semipositive at x, then so is
max{h, h′ }. Indeed, we can write h = lim hi and h′ = lim h′i for R-PL LFS functions hi , h′i
in a neighbourhood U of x. By 7.9, the functions max{hi , h′i } are R-PL LFS functions on
U, and we have max{h, h′ } = lim max{hi , h′i }.
   Now we relate semipositivity to positive forms and currents. See 2.8 for the definitions
of positivity based on the corresponding notions for Lagerberg forms and Lagerberg cur-
rents introduced in 2.7. The next result serves as a replacement for [CD12, Lemmas 5.2.3
and 5.3.3] where the result is claimed for strongly positive forms; this is not correct, as
explained in [BGJK21a, Example 2.3.6].


## GJR PDF page 49

                FORMS ON BERKOVICH SPACES BASED ON HARMONIC TROPICALIZATIONS                             49

                                                                      p,p
Lemma 7.12. Let X be a Hausdorff analytic space over K and let ω ∈ Asm,c   (X ) be symmetric.
                                         p,p
Then there are positive forms ω1 , ω2 ∈ Asm,c (X ) such that ω = ω1 − ω2 .
Proof. The support of ω is compact and hence has a paracompact open neighbourhood
in X by [CD12, Lemme 2.1.6]. Replacing X by this open neighbourhood, we may as-
sume that X is paracompact. Then we have smooth partitions of unity available [CD12,
Proposition 3.3.6], so we may argue locally. Hence we may assume that there is an open
subset U of X such that the support of ω is contained in U and such that W := U is a
                                                                   n,an               ∗
compact analytic domain in X with a moment map ϕ : W → Gm               and with ω = ϕtrop (α)
                              p,p
for a symmetric form α ∈ A (ϕtrop (W )). It follows from 2.7 that α = α1 − α2 for two
smooth positive forms α1 , α2 on ϕtrop (W ). As usual, the existence of smooth partitions of
unity yield that there is a smooth non-negative function ψ with support in U such that
                                         ∗
ψ ≡ 1 on supp(ω). Setting ωi := ψ · ϕtrop   (αi ) for i = 1, 2, we get the claim.           
7.13 (Continuous Plurisubharmonic Functions). For simplicity, we suppose that X is a
boundaryless6 good separated strictly analytic space to use currents on X as in 2.8. Using
the theory of integration from [CD12, 3.7–3.10], every continuous real function h on X
has an associated current [h] given by
                                                       Z
                               [h]: Asm,c (X ) −→ R ,        ω 7→            h·ω
                                                                         X
where the integral is defined by a limit process using that h is a uniform limit of smooth
functions on a neighbourhood of the support of ω (see [CD12, Corollaire 5.4.7, 5.4.8]).
We say that h is plurisubharmonic (short: psh) if the current d′ d′′ [h] is positive. A parti-
tion of unity argument shows that plurisubharmonicity is a local notion on X (see [CD12,
Lemme 5.5.2]).
   By [CD12, Lemme 5.5.3], a smooth function h is psh if and only if every x ∈ X has a
                                                                                r,an
compact strictly analytic neighbourhood V with a moment map ϕ : V → Gm               such that
h|V = u◦ϕtrop for a continuous function u on ϕtrop (V ) which restricts to a convex function
on each face. This characterization shows that smooth psh functions admit pull-backs
with respect to morphisms.
Theorem 7.14. Let X be a good separated strictly analytic space over K and let h: X → R
be a semipositive R-PL function. Then h restricts to a psh function on X \ ∂ X .
Proof. By restriction to X \ ∂ X , we may assume that X is boundaryless. The claim is local
in X and so we may assume that h is a uniform limit of R-PL LFS functions hi on X by
using Proposition 7.10. It follows from 7.9 and from [CD12, Corollaire 6.3.2] that an
R-PL locally Fubini–Study function is locally a uniform limit of smooth psh functions and
hence hi is psh. For any positive form ω ∈ Asm,c (X ), we deduce from uniform convergence
that                                 Z                  Z
                      〈ω, d′ d′′ [h]〉 =        h · d′ d′′ ω = lim       hi · d′ d′′ ω ≥ 0.
                                                              i
                                           X                        X
  6
    Currents in analysis work well only in the boundaryless case, as otherwise there are disturbing residues
along the boundary. Note that Chambert-Loir and Ducros also omit the boundary in their definition of
currents [CD12, 4.2.2], as their currents act on smooth forms with compact support disjoint from the
boundary.


## GJR PDF page 50

50                                W. GUBLER, P. JELL, AND J. RABINOFF

We conclude that h is psh.                                                                          
Corollary 7.15. Let h be a harmonic function on a good separated strictly analytic space X
over K. Then the restriction of the current d′ d′′ [h] to X \ ∂ X is zero.
Proof. We may assume that X is boundaryless. It follows from Theorem 7.14 that h and
−h are psh on X . By linearity in the irreducible components and by arguing locally, we
may assume that X is of pure dimension d. Let η ∈ Asm,c             d−1,d−1
                                                                            (X ). Since d′ d′′ [h] is a
symmetric current on X , we have
                           1                                              1
         〈η, d′ d′′ [h]〉 =    〈η, d′ d′′ [h]〉 + (−1)d−1 〈Jη, d′ d′′ [h]〉 = 〈ω, d′ d′′ [h]〉
                           2                                                  2
for the symmetric form ω := η + (−1)d−1 Jη ∈ Asm,c       d−1,d−1
                                                                 (X ). By Lemma 7.12, there are
                             d−1,d−1
positive forms ω1 , ω2 ∈ Asm,c (X ) such that ω = ω1 − ω2 . As h and −h are psh, we get
                 2〈η, d′ d′′ [h]〉 = 〈ω1 , d′ d′′ [h]〉 − 〈ω2 , d′ d′′ [h]〉 = 0 − 0 = 0,
proving the claim.                                                                                  
Remark 7.16. In this section, we have focused on the concept of semipositive and har-
monic functions. In fact, all the results immediately transfer to Λ-PL metrics k k of a
line bundle L over a good strictly analytic space X . Indeed, the choice of a local frame s
gives rise to a Λ-PL function h := − log ksk, to which we can apply the above results. Then
Theorem 7.14 yields that on a good separated strictly analytic space X every semipositive
R-PL metric of L has a positive first Chern current c1 (L, k k) as defined in [CD12, 6.4.1].
The same holds for uniform limits of such metrics on L which includes all the metrics
considered by Zhang [Zha95] over projective varieties.

                  8. PIECEWISE LINEAR AND HARMONIC TROPICALIZATIONS
  In this section, we assume that X is a compact good strictly K-analytic space of pure
dimension d. We will define a piecewise linear tropicalization map to be a tuple h =
(h1 , . . . , hn) of PL functions on X . We will endow h(X ) ⊂ Rn with the structure of a
weighted (Z, Γ )-polytopal complex, which is canonical up to subdivision. The difficult
part is defining weights on h(X ), which we will do G-locally using the results of 4.
Definition 8.1. A piecewise linear (PL) tropicalization is a map
                                    h = (h1 , . . . , hn): X −→ Rn
where h1 , . . . , hn are piecewise linear functions. It is called a harmonic tropicalization if
in addition all the hi are harmonic (which means that all of the hi are Z-harmonic). It is
called a smooth tropicalization map if hi = log | f i | for f i ∈ Γ (X , OX× ).
8.2. Remarks:
                                                                                     n,an
   (1) A smooth tropicalization map has the form ϕtrop for a moment map ϕ : X → Gm        .
       These are the tropicalizations considered in [CD12].
   (2) A smooth tropicalization map is harmonic by Remark 7.3(6).
   (3) A piecewise linear tropicalization is G-locally a smooth tropicalization map.


## GJR PDF page 64

64                              W. GUBLER, P. JELL, AND J. RABINOFF

   We define differentials of preforms by d′ (h, α) = (h, d′ α) and d′′ (h, α) = (h, d′′ α). The
differentials satisfy the Leibniz rule
                                 
           d′ (h, α) ∧ (h′ , α′ ) = d′ (h, α) ∧ (h′ , α′ ) + (−1)(p+q)(h, α) ∧ d′′ (h′ , α′ ),
and likewise for d′′ . We conclude that the weakly smooth preforms form a presheaf of
bigraded differential R-algebras with respect to the differentials d′ and d′′ .
Definition 10.7 (Weakly smooth forms). The presheaf of weakly smooth preforms is
defined on the open subsets of X whose closure is a compact strictly analytic domain. We
denote the associated sheaf on the underlying topologicalL
                                                         space of X by AX or simply by
                                                                 p,q
A. It is a sheaf of bigraded differential R-algebras A =    p,q A . It is also a sheaf of
A -algebras. The elements of A are called weakly smooth forms. The elements A0,0 are
 0,0

well-defined real functions which we call weakly smooth functions.
10.8 (Pullback of Forms). For a morphism f : X ′ → X of good strictly analytic spaces,
there is a pull-back homomorphism f ∗ : AX → f∗ AX ′ of sheaves of bigraded differential
R-algebras, defined on preforms as follows: if U ⊂ X and U ′ ⊂ f −1 (U) are open subsets
whose closures are compact strictly analytic domains, and if (h, α) is a weakly smooth
preform on U, then f ∗ (h, α) := (h ◦ f , α).
  Let (h, α) be a weakly smooth preform on a compact good strictly analytic space X over
K. We denote the associated weakly smooth form by h∗ (α).
Proposition 10.9. Let X be a compact good strictly analytic space X over K and let h: X →
Rn be a harmonic tropicalization map.
   (1) The natural map from weakly smooth preforms to weakly smooth forms is injective.
   (2) The pullback h∗ : A•,• (h(X )) → A•,• (X ) is an injective homomorphism of bigraded
        differential R-algebras.
   (3) If f : X ′ → X is a morphism of good strictly analytic spaces, then (h ◦ f )∗ = f ∗ ◦ h∗ .
Proof. It is clear that (1) follows from (2) and Lemma 10.4, and (3) is obvious from
the definitions as h ◦ f is a harmonic tropicalization map by Remark 8.2. It remains to
show (2). Obviously, the map h∗ is a homomorphism of bigraded differential R-algebras.
To show the crucial injectivity, let us pick α ∈ A•,• (h(X )) with h∗ (α) = 0. Using that
the presheaf of weakly smooth forms and the sheaf of weakly smooth forms have the
same stalks, every x ∈ X has a compact strictly affinoid neighbourhood W such that
the preform (h|W , α|h(W ) ) is zero. By Lemma 10.4, we have α|h(W ) = 0. Using that X is
compact, we see that finitely many such W cover X and hence the corresponding h(W )
cover h(X ). We conclude that α = 0, proving injectivity in (2).                       
Remark 10.10 (Smooth forms). In the above, if we replace harmonic tropicalization
maps by smooth tropicalization maps, then we get the smooth differential forms intro-
duced Lby Chambert-Loir and Ducros (see below for a proof). They give rise to a sheaf
Asm = p,q Asm p,q
                  of bigraded differential R-algebras with respect to differentials d′ and d′′ .
The elements of A0,0 sm
                        are called smooth functions. Again, we have a functorial pull-back
with respect to morphisms of analytic spaces.
  Now we show that Asm agrees with the sheaf ACD of smooth forms defined in [CD12].
Let U ⊂ X be an open set whose closure U is a compact strictly analytic domain, and let


## GJR PDF page 65

               FORMS ON BERKOVICH SPACES BASED ON HARMONIC TROPICALIZATIONS                  65

(h, α) be a smooth preform on U as defined in 10.3 with respect to a smooth tropicaliza-
tion map h: U → Rn . Choose a moment map ϕ : U → Gm             n,an
                                                                     such that h = ϕtrop . Then
(ϕ|U , h(U)) is a tropical chart in the sense of [CD12, 3.1.1], so α ∈ A(h(U)) defines an
element of ACD (U), which does not depend on the choice of ϕ by Lemme 3.1.10 of loc.
cit. Sheafifying, we get a homomorphism of sheaves Asm → ACD . This homomorphism is
surjective by §3.1.9 of loc. cit., and it is injective by 10.9 and Lemme 3.2.2 of loc. cit.
Remark 10.11 (Piecewise smooth forms). In the above, if we replace harmonic tropical-
ization maps by smooth tropicalization maps and the sheaves AS of smooth Lagerberg
forms on the piecewise Z-linear spaces S by the sheaves AS,ps of piecewise smooth Lager-
berg forms (see 10.2), then we get a variant of the piecewise smooth     L differential   forms
                                                                                 p,q
introduced in [GK17, Section 9]. They give rise to a sheaf Aps = p,q Aps of bigraded
differential R-algebras with respect to differentials d′P and d′′P . The latter are called poly-
hedral derivatives; they do not coincide in general with the differentials of the associated
currents (this is a consequence of the tropical Poincaré–Lelong formula [GK17, Theo-
rem 0.1]). The elements of A0,0ps
                                  are called piecewise smooth functions. Again, we have a
functorial pull-back with respect to morphisms of analytic spaces.
Remark 10.12. Note that Lemma 10.4 and Proposition 10.9 hold also for smooth and
for piecewise smooth preforms. Indeed, the smooth case is just [CD12, Lemme 3.2.2],
and one readily checks that the argument works also in the piecewise smooth case.
10.13 (Relations between the forms). By Remark 8.2, every smooth tropicalization map
is harmonic, so we get a homomorphism Asm → A of sheaves of bigraded differential
R-algebras. We also have a canonical homomorphism A → Aps of sheaves of bigraded
differential R-algebras, defined as follows. Let (h, α) be a weakly smooth preform on an
open subset U of X whose closure U is a compact strictly analytic domain. We proved
in 8.4 that for any x ∈ U, there is a open neighbourhood U x of x whose closure is a
compact strictly analytic domain contained in U, a smooth tropicalization map h x on U x ,
and a piecewise (Z, Γ )-linear map F : h′ (U x ) → h(U) such that h = F ◦ h x on U x . Since α
is a smooth Lagerberg form on h(U), we conclude that α x := F ∗ (α) is a piecewise smooth
form on h′ (U x ). One checks that the piecewise smooth preforms (h x , α x ) glue to a well-
defined piecewise smooth form on U, giving rise to the desired canonical homomorphism
A → Aps .
Proposition 10.14. The above canonical homomorphisms are injective: that is, we have
inclusions of sheaves of bigraded differential R-algebras
                                      Asm ,→ A ,→ Aps .
Proof. The map Asm → Aps is obviously injective and factors through A → Aps , so it
is enough to show that the homomorphism A → Aps is injective. Let U be an open
subset of X and let ω be weakly smooth form on U such that the associated piecewise
smooth form constructed in 10.13 is zero. Arguing locally, we may assume that U is a
compact strictly analytic domain and that ω is given on U by a weakly smooth preform
(h, α), where h: U → Rn is a harmonic tropicalization and α ∈ A(h(U)). Replacing U
by U x from 10.13, we may assume that h is covered by a smooth tropicalization map


## GJR PDF page 77

              FORMS ON BERKOVICH SPACES BASED ON HARMONIC TROPICALIZATIONS                77

of harmonic functions introduced in Section 7 agrees in the case of a rig-smooth curve
with the harmonic functions in Thuillier’s thesis [Thu05]. This will be important in the
companion paper [GJR21].
   First, we recall some notions from the theory of graphs and their relationship to the
structure of non-Archimedean analytic curves. For more details, we refer to [GJR21].

15.1 (Metric Graphs with Boundary). We consider a weighted metric graph (Σ, ∂ Σ) with
boundary. This is a finite multigraph with no loop edges endowed with positive edge
lengths assumed to be in Γ . The boundary ∂ Σ is any subset of the vertices of Σ. Every
edge is endowed with the additional datum of a weight w(e) ∈ Z>0 . If we ignore the
boundary, then we get a compact piecewise (Z, Γ )-linear space of dimension at most 1 as
introduced in 2.5. (Note that isolated vertices are allowed.)
   A function h: Σ → R is called harmonic if the restriction
                                                        P         of h to any edge is affine
R-linear, and if for any vertex x of Σ \ ∂ Σ, we have e− =x w(e)de (h) = 0, where e ranges
over all edges with tail vertex x and de (h) is the outgoing slope of h at x in the direction
of e.
   For a subgroup Λ of R containing Γ , we let Σ(Λ) denote the subset of Σ consisting of
all points x such that f (x) ∈ Λ for all (Z, Γ )-linear functionspf on an edge e containing
x. Let U ⊂ Σ be a subgraph with vertices contained in Σ( Γ ). A function h: U → R
is called piecewise (Z, Γ )-linear if there
                                        p is a subdivision of the subgraph U such that the
vertices of the subdivision are in Σ( Γ ) and such that the restriction of h to any edge e
of the subdivision extends to a (Z, Γ )-linear function on the edge of Σ containing e.

15.2 (Skeletons of Curves). Metric graphs with boundary arise in non-Archimedean ge-
ometry as follows. Let X be a compact rig-smooth curve over K, i.e., a compact rig-smooth
strictly analytic space of pure dimension 1. We assume that X has a strictly semistable
model X over the valuation ring K ◦ . This is a formal K ◦ -model of X (see 2.4) whose spe-
cial fiber Xs is geometrically reduced with smooth irreducible components and at most
double points as singularities. This is equivalent to [Thu05, Definition 2.2.8], where
such models are called simplement semi-stable. To such a model is associated a weighted
metric graph with boundary Σ := S(X), called the skeleton of X. There is a canonical
inclusion Σ ,→ X . The vertices of Σ correspond to the irreducible components of Xs and
the edges correspond to the singular points of Xs , so that Σ is the incidence graph of Xs .
The boundary ∂ Σ consists of the vertices of Σ corresponding to non-proper irreducible
components of Xs . If x ∈ Xs is a singular point with corresponding edge e, then the
weight of e is defined to be w(e) = [Ke (x) : K
                                              e ]. There is an étale neighbourhood of x of
the form Spf(K{X , Y }/(X Y − ̟)) for some ̟ ∈ K ◦◦ \ {0}; the length of e is then defined
to be v(̟). There is a canonical deformation retraction map τ: X → S(X).

15.3 (Subdivisions of the Skeleton). Consider
                                      p         a subdivision Σ′ of the skeleton Σ = S(X)
such that all vertices of Σ′ are in Σ( Γ ). Vilsmeier [Vil21, Construction 2.6] has de-
fined a canonical formal scheme X′ with generic fiber X and reduced special fiber, and a
canonical morphism ι : X′ → X extending IdX , such that for any edge e′ of Σ′ , the analytic
subdomain (τ)−1(e′ ) of X is the generic fiber of an open subset of X′ . Note that X′ is not
necessarily an admissible formal scheme, i.e. not necessarily of topologically finite type.


## GJR PDF page 78

78                             W. GUBLER, P. JELL, AND J. RABINOFF

By [Gub13b, Propositions 6.7 and 6.9], the formal scheme X′ is admissible if the value
group Γ is discrete or if the vertices of Σ′ are contained in Σ(Γ ).
15.4 (Piecewise Affine Functions on the Skeleton).
                                             p         Let Σ = S(X) as in 15.2, let U be a
subgraph of Σ with vertices contained in Σ( Γ ), and let h: U → R be a piecewise (Z, Γ )-
linear function in the sense of 15.1. Passing to a subdivision of U, we may assume that
h is (Z, Γ )-linear on each edge of U. The vertices of U induce a subdivision Σ′ of Σ; we
denote the associated formal K ◦ -model of X by X′ as in 15.3, with canonical morphism
ι : X′ → X. When Γ dense in R, we assume that all vertices of U are in Σ(Γ ); then
X′ is an admissible formal scheme. The subset Y := τ−1 (U) is the generic fiber of a
unique open formal subscheme Y′ in X′ . By the arguments used in the proof of [Vil21,
Proposition 2.11], there is a canonical vertical Cartier divisor D on Y′ with associated
formal metric on OY determined by − log k1kO (D) = h ◦ τ. See 5.5.
Proposition 15.5. Let X be a compact rig-smooth curve over K and let h: X → R.
     (1) If X is a strictly semistable model of X over K ◦ , then h = hL for a line bundle
         L ∈ M (X) if and only if there is a function f : S(X) → R which is (Z, Γ )-linear on
         each edge such that h = f ◦ τ.
     (2) If x ∈ ∂ X , then h is harmonic at x if and only if h is R-PL at x.
Proof. The “if” part in (1) follows from 15.4. Conversely, assume that h = hL for L ∈
M (X). Using the identification L|X = OX , the meromorphic section 1 of L induces a
vertical Cartier divisor D on X. There is a covering of X by open subsets U such that S(U)
is either an edge or a vertex of S(X) and such that D|U = div(γ) for some γ ∈ O (U)×,
where U = Uη . It follows from [Ber99, Theorem 5.3 and Step 13 in its proof] that
h|U = − log |γ| factorizes through a (Z, Γ )-linear function on S(U). This proves (1).
   Since x ∈ ∂ X , the curve ∂ X is affine and hence the nef condition in Proposition 7.1 is
vacuous. This proves (2).                                                                 
15.6 (Thuillier’s Harmonic Functions). We consider now an arbitrary rig-smooth curve
X over K. We call a function h: X → R harmonic in the sense of Thuillier if every x ∈ X
has a strictly affinoid neighbourhood V , a finite Galois extension K ′ /K, and a strictly
semistable model V′ of V ′ := V ⊗K K ′ , such that the pullback h′ of h|V factorizes through
the skeleton S(V′ ) and such that h′ |S(V′ ) is a harmonic function on the skeleton S(V′ )
considered as a weighted metric graph with boundary as in 15.2.
   For x ∈ ∂ X , Proposition 15.5 and Corollary 5.12 show that the above harmonicity
condition at x is equivalent to piecewise R-linearity at x, using that the boundary of
S(X) is ∂ X . Note that Thuillier [Thu05, Section 2.3] used this definition only for strictly
affinoid or boundaryfree X , so the above definition is slightly more general than his.
Proposition 15.7. Let X be a rig-smooth curve. Then a function h: X → R is harmonic in
the sense of Definition 7.2 if and only if h is harmonic in the sense of Thuillier.
Proof. The claim is local on X , so we may assume X strictly affinoid. We first show
that the harmonicity notions agree for a piecewise linear function h ∈ PL(X ). By 5.6,
we have that h = − log k1kL for a model L of OX on a formal K ◦ -model X of X . Using
base change, Proposition 7.6 and [Thu05, Remarque 2.3.17], we are free to pass to a


## GJR PDF page 79

              FORMS ON BERKOVICH SPACES BASED ON HARMONIC TROPICALIZATIONS                79

finite Galois extension of K. Arguing locally, the semistable reduction theorem ([Thu05,
Théorème 2.3.8] under these hypotheses; see also [BL85, Section 7] and [Duc24, Theo-
rem 5.1.14(iv), 6.1.3]) shows that we may assume that X is a strictly semistable model.
By Proposition 15.5, there is a function f on the skeleton S(X) which is (Z, Γ )-linear on
each edge such that h = f ◦ τ. For x ∈ S(X) \ ∂ X with corresponding proper irreducible
component C := redX (x) of Xs , it follows as in [KRZB16, Theorem 2.6] that the sum of
outgoing slopes of f at x is equal to deg(L|C ). We conclude that h is harmonic in the
sense of Thuillier if and only if L is numerically equivalent to 0. The latter is equivalent
to harmonicity of h in the sense of Definition 7.2, as we have shown in Lemma 7.4.
   Now we prove the proposition for any function h: X → R. Assume that h is a harmonic
function on X as in Definition 7.2. By Proposition 7.5, the function h is locally an R-linear
combination of Z-harmonic functions, so we are reduced to the case handled above since
the set of Thuillier-harmonic functions forms a real vector space.
   Conversely, let h be a harmonic function in the sense of Thuillier. We have to check
for any x ∈ X that h is harmonic at x. As above, we are free to pass to a finite Galois
extension of X , so we may extend scalars and shrink X to assume that X has a strictly
semistable model X and that h factorizes through a harmonic function f : S(X) → R. It
is enough to show that f is an R-linear combination of piecewise (Z, Γ )-linear harmonic
functions f i on S(X). Indeed, by Proposition 15.5, we have that f i ◦ τ is piecewise linear,
so f i ◦ τ is harmonic by the the first paragraph of this proof, and hence h is harmonic.
   Suppose first that x ∈ ∂ X = ∂ S(X). After shrinking X, we may assume that S(X)
is a star around the vertex x, so that f is affine R-linear on each edge. Translating by
a constant function, we may assume f (x) = 0. Then f is an R-linear combination of
piecewise Z-linear functions f e on S(X): namely, the functions f e that have slope 1 on a
given edge e and slope 0 on the others. Since x ∈ ∂ S(X), Proposition 15.5 yields that
each f e is harmonic and hence h is harmonic.
   If x ∈ X \ ∂ X , then as above, we may assume that S(X) is either an edge containing
τ(x) in its interior, or that S(X) is a star around the vertex τ(x). In the first case, f is
an R-multiple of a (Z, Γ )-linear function on the edge, so h is harmonic. In the second
case, we may assume that f (τ(x)) = 0. Then f is harmonic if and only if f is linear on
each edge and the weighted sum of the outgoing slopes at τ(x) is zero. This is a linear
equation for the slopes which is defined over Q, so there is a basis of solutions defined
over Q and even over Z. The elements f i of such a basis induce piecewise (Z, Γ )-linear
functions f i which are harmonic on S(X). Since f is an R-linear combination of the f i ,
we have that h is harmonic.                                                                

   Note that Γ is either dense inpR or is a discrete subgroup. In the following, we set
Λ := Γ if Γ is dense and Λ := Γ (the divisible hull in R) if Γ is discrete. When Γ is
discrete, we may rescale the valuation to assume Γ = Z.

15.8. Let X be a compact rig-smooth curve over K with strictly semistable model X. As
in 15.2, the skeleton S(X) is viewed as a weighted metric graph with boundary. Let U
be a subgraph of Σ := S(X) with vertices contained in Σ(Λ), then τ−1 (U) is a compact
strictly analytic domain in X .


## GJR PDF page 80

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


## GJR PDF page 81

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

                16. CANONICAL TROPICALIZATIONS OF ABELIAN VARIETIES
  Let A be an abelian variety over the non-Archimedean field K with non-trivial valuation
v. The uniformization theory of Bosch, Lütkebohmert and Raynaud yields that after
replacing K by a finite separable extension, there is a canonical exact sequence
                                                   q
                                 0 −→ T −→ E −→ B −→ 0
of algebraic groups such that Aan = E an /Λ for a discrete subgroup Λ of E(K). Here B
is the generic fiber of an abelian scheme B over K ◦ and T is a split torus over K (see
[BL91] and [Ber90, 6.5]). Note that the quotient homomorphism p : E an → Aan is only
an analytic morphism, but the Raynaud extension E is algebraic by the GAGA principle,
and the quotient homomorphism q : E → B is locally trivial.
16.1 (Canonical Tropicalizations). We denote the character lattice of the split torus T by
M and we set N := Hom(M , Z). For u ∈ M , the pushout of the Raynaud extension with
respect to the character χu : T → Gm gives rise to a translation invariant extension of B
by Gm , and hence to a rigidified translation invariant line bundle Eu on B (see [BL91]
and [FRSS18, 3.2]). Note that the line bundle q∗ (Eu ) is trivial over E, and the above
pushout construction gives a canonical frame eu : E → q∗ (Eu ). Following [FRSS18, 3.2]),
we define the canonical tropicalization map as the unique map
                                      trop: E an −→ NR
satisfying
                             〈trop(x), u〉 = − log q∗ keu (x)kEu ,
where k kEu is the canonical metric on the rigidified line bundle Eu which is the formal
metric associated to the unique (up to isomorphism) formal K ◦ -model of Eu on the formal


## Ber PDF page 73

76                               VLADIMIR G. BERKOVICH

3.7. The local structure of a smooth morphism

       3.7.1. Definitions. — (i) A morphism <p : Y -> X is said to be an elementary fibration
of pure dimension one (resp. at a pointy e Y) if it can be included to a commutative diagram

                  Y c-^ z <— V = U (X x E,)
                                         »==!




                           X
such that
      a) ^ : Z -> X is a smooth proper morphism whose geometric fibres are irreducible
curves of genus g ^ 0;
      b) Y is an open subset of Z, and V = Z\Y;
      c ) V is an analytic domain in Z isomorphic to a disjoint union 11*"= i (X X E,),
m ^ 1, where E, are closed discs in A1 with center at zero, andj&r is the canonical projection;
      d ) there exists an analytic domain V C V such that the isomorphism
                  V^U^(XxE,)
from c ) extends to an isomorphism V'^-U^^X X E,'), where E,' is a closed disc
in A1 which contains E, and has a bigger radius;
     e ) the pair (Z^, YJ (resp. the triple (Z^, Y^,j/)), where x = 9(^)3 is elementary.
     (ii) A morphism is said to be an elementary fibration if it is a composition of ele-
mentary fibrations of pure dimension one.
     (iii) A morphism 9 : Y -> X is said to be standard of pure dimension one if everything
from (i), except the property e), is true for it. A composition of standard morphisms of
pure dimension one is said to be standard,
     We remark that the geometric fibers of a standard morphism are nonempty and
connected. Furthermore, elementary fibrations (resp. standard morphisms) are preserved
under any base change functor and under any ground field extension functor.

      3.7.2. Theorem. — Let 9 : Y -> X be a smooth morphism of pure dimension one, and
suppose that X (and therefore V) is good. Then for any pointy e Y there exist an etale morphism
f: X' -> X and an open subset Y" C Y7 = Y x^ X'
                  Y -^ X
                  A         A

                  r         r
                  Y' -^ X'

                  t V
                  Y"
such that y has a unique preimage y' in Y" and 9" : Y" -> X' is an elementary jibraiion of pure
dimension one at the point y.


## Ber PDF page 74

            fiTALE COHOMOLOGY FOR NON-ARCHIMEDEAN ANALYTIC SPACES                           77

      3.7.3. Corollary. — Let <p : Y -> X be a smooth morphism of good k-analytic spaces. Then
for any point y e Y there exist ttale morphisms f: X' -> X and g : Y" -> Y' = Y Xx X'

                 Y ^> X

                            I7
                  A         A

                  r
                  Y' -^ X'

                  t- -7
                  Y"
such that y e/'C?(Y")) ^ 9" is an elementary fibration. •

      3.7.4. Corollary. — A smooth morphism is an open map. •

      Proof of Theorem 3.7.2. — All the analytic spaces considered in the proof are
assumed to be good. For numbers 0 < r' ^ r" (resp. 0 < r ' < r") we denote by A(r', r " )
(resp. B(r', r")) the closed (resp. open) annulus E(0, r")\D(0, r') (resp. D(0,r")\E(0,r'))
with center at zero.

       3.7.5. Proposition. — Let 9 : Y -> X be a separated smooth morphism of pure dimension
one, and let x eX. Suppose that the fibre Y^ is isomorphic to the open annulus B(r, R)^^). Then
there exist numbers r < r' < R' < R, an open neighborhood W ofx and an open subset i^ C (p"1^)
such that
      a) Y^ coincides with B(r', R').^,) under the identification of Y^ with B(r, R).^);
      b) i^ is isomorphic to the direct product ^ X B(r', R') over W.

      3.7.6. Lemma. — Let Y be an open subset of A^, and suppose that

                  Y, = D(0, r)^\ U E(^, r^              m ^ 0,
                                     i=l


wA^ r, < r aW | T(^) | < r (^T ^ ^ coordinate function on A1}. Then
       (i) if m == 0, ^ /or ^ w^w&^r 0 < r' < r ^r^ exists an open neighborhood % of x
 such that Y contains the direct product % X D(0, r').
        (ii) if m^ 1, then for any numbers max.([ T(aJ |, r,) < r' < r" < r, ^r<? exists an
 open neighborhood % of x such that Y contains the direct product % X B(r', r").

       proof. — In the case (i) (resp. (ii)) the intersection of all compact sets of the form
 U X E(0,r') (resp. U X A(r', r")), where U runs through compact neighborhoods
 of the point x, coincides with E(0, r')^ (resp. A(V, r")^), and therefore it is contained
 in the open set Y. It follows that there exists a compact neighborhood U of A: with
 U X E(0, r') C Y (resp. U X A(r', r") C Y). •


## Ber PDF page 75

78                                VLADIMIR G. BERKOVICH

      3.7.7. Lemma. —Suppose we are given a commutative diagram




with smooth <p and ^ of the same pure dimension, and let y e Y and x = y(j^). Suppose that the
induced morphism fy^: Y^ -> Z^ is a local isomorphism at the pointy. Then f is a local isomorphism
at y.

      Proof. — Since Y^, is the fibre product of Y and Z^ over Z, the inverse image of
the sheaf of differentials of/on Y^ coincides with that of/. But the latter sheaf is equal
to zero at the point y. Therefore we may decrease Y and assume that f is unramified.
By Proposition 3.3.2 (i), the canonical homomorphism /"(^z/x) ~^^Y/X ls surjective.
Since both ^-modules are locally free and of the same rank, we have/*(Q^x) ^^Y/X-
From Proposition 3.5.3 (ii) it follows that/is dtale at the point y. By hypothesise/induces
an isomorphism of fields J^( z ) ^>^{y). By Proposition 2.4.1, K(^) ^K(j^), and there-
fore / is a local isomorphism at y, by Theorem 3.4.1. •

      Proof of Proposition 3.7.5. — We may assume that X ==e^(j^) is ^-affinoid. Take
a number r< t< R and set y ==j^(E(0, t)) <=Y^. Let V be an affinoid neighborhood
ofy in Y. Shrinking X and Y, we may assume that the fibre V^; is connected. Then

                  V,=E(0,R')^\UD(^,r,)^,

where / < R' < R, r, < R' and | T(ff,) [ < R' (T is the coordinate function on B(r, R)^(J.
Let V =^(^?). Since the image of S9®^K[x) in SS^^{x) is everywhere dense, we
can shrink X and assume that there exists an element f e 38 such that the norm of/— T
in SS^^^^x) is less than min(^, t). It follows that the morphism/: V -^A^ induces
 an isomorphism Vg; ^> V^ and f{y) =j&(E(0,^)). Take an open neighborhood i^ of
 the pointy such that Y^CV. Then the induced morphism /: i^ -> A^ satisfies the
 hypothesis of Lemma 3.7.7, and therefore / is a local isomorphism at the point y. The
 required statement now follows from Lemma 3.7.6. •

       3.7.8. Proposition. — Let 9 : Y -> X be a smooth morphism of pure dimension one, and let
 x e X. Suppose that the fibre Y^ is isomorphic to the open disc D(0, R).^) and that the morphism 9
 is a composition of an open immersion Y c-^ Z with a compact morphism ^ : Z -> X. Then for
 any 0 < r < R there exist an open neighborhood ^ of x and an open subset i^ C (p""^^) such that
       a) Y^ coincides with D(0, r)^^ under the identification ofl^ with D(0, R)^(^);
       b) T is isomorphic to W x D(0, r) over %.

       Let P and Q, be Hausdorff topological spaces, and let P^ C P and Q^ C Q be their
 open subsets for which there is a homeomorphism/: Pi ^ Q,r The topological space,


## Ber PDF page 76

            £TALE COHOMOLOGY FOR NON-ARCHIMEDEAN ANALYTIC SPACES                            79

which is obtained by gluing P and Q via/.will be denoted by P u^Q. The following
statement is trivial.

       3.7.9. Lemma. — Suppose that there exists an open subset P'C P such that P^C P' and
the space P' u^Q is Hausdorff. Then the space P u^ is Hausdorff. Furthermore, suppose in
addition that P\Pi is compact and Q,^ P^ u, Q^is relatively compact in P' u^ Q. Then the space
P u/Q^ is compact. •

      Proof of Proposition 3.7.8. — We may assume that X is yfe-affinoid. In particular,
Z is Hausdorff and compact. From Proposition 3.7.5 it follows that we can shrink X
and find an open subset ^C Y such that ^ = B(r', R')^ and -T-^ X X B(r', R/)
for some r < r' < R' < R. Take numbers r' < r " < t < R" < R' and denote by IT
the open subset of V which corresponds to X x B(r", R"). The subset SC-lT, which
corresponds to X x A(^), is compact because X is compact, and therefore Z\S is
an open subset of Z. We apply the above gluing procedure to the spaces P == Z\S,
P == ^\S, P, = ^T\S, Q== X x (P^O, r")) U X X D(0, R"),
                 Q^ == X x B(r", t) U X x B(^, R"),

and to the canonical isomorphism /: P^ ^> Qi. One has
                 P' u, Q-^ X x (P^O, r')) U X x D(0, R').

From Lemma 3.7.9 it follows that the space T = P u^Q is Hausdorff and compact.
 In particular, the morphism ^' : Z' -> X is compact.
       Furthermore, the above construction restricted to the fibre at x gives a compact
JT (A;)-analytic space Z^ such that the connected component ofD(0, R)^) is isomorphic
to the projective line P^) . Moreover, the morphism ij/ is smooth at all points of this
connected component. Since ^' is compact, we can shrink X and replace Z' by the
connected component of D(0, R)^) in Z' so that the morphism ^' becomes proper smooth
of pure dimension one. It has a section a : X -> Z' defined by the point infinity of the
disc P^E^, r'). One has dirn^ H°(Z,, ^) == 1 and H^Z;, ^) = 0. By the Semi-
continuity Theorem ([Ber], 3.3.11), we can shrink X and assume that the same is true
for all x ' e X. It follows that all the fibres of ^ are isomorphic to the projective line.
       Finally, let L be the invertible sheaf on Z' which corresponds to o(X), and let L^
denote the inverse image of L on the fibre Z^, x ' e X. Then H^Z^LJ ==0 and
dimH°(Z^,L^) == 2. It follows that ^:(L) is a locally free fi^odule of rank two.
Shrinking X, we may assume that ^(L) is free. In this case it defines a morphism Z' -> P^
over X which is evidently an isomorphism. The required statement now follows from
Lemma 3.7.6 (i). •
       We are now ready to prove the theorem. First of all we remark that if K is a
finite separable extension of the field K(x), then there exists an dtale morphism/: X' -> X
such that/"1 (x) == { x ' } and K(^') === K. The preimage of the pointy under the morphism


## Ber PDF page 77

80                                 VLADIMIR G. BERKOVICH

j f ' : Y ' = Y X x X' -> Y is a nonempty finite set of points. Fixing one of them, say y,
 we can replace 9 by a morphism Y" -> X', where Y" is an open neighborhood ofy
 which does not contain other points from/'"^j;). If we make the above procedure,
 we say for brevity that we increase the field K(x). Furthermore, we may assume that the
 space X is A-affinoid.

        Step 1. — One can increase the field K{x) so that <p is included in a commutative diagram

                   Y c-L» z



                            X
where
       a) ^ is a smooth proper morphism of pure dimension one whose geometric fibres are irreducible
curves of genus g^ 0, and j is an open immersion,
        ^) if 8^ I? ^7Z ^x has good reduction and y is the generic point of Z^..

      Let Z be an affinoid neighborhood of the point y. Replacing Y by a small open
neighborhood ofj/ which is contained in Z, we may assume that the morphism 9 : Y -> X
is a composition of an open immersion Y <-> Z with a compact morphism ^ : Z -> X.
By Proposition 3.6.1, we can increase the field K(x) and assume that the pair (Y^,j/)
is elementary. In particular, Y^ contains a disjoint union of m ^ 1 open annuli B(r,, R,)^(^)
such that the set Y^Ll^ B(r,, R,)^) is a connected compact neighborhood of the
pointy (Remark 3.6.3 (i)). By Proposition 3.7.5, we can shrink X, Y and the annuli
and assume that there are pairwise disjoint open subsets ^ C Y, 1 ^ i ^ m, such that
^ == B(r,, R,).^) and ^ -^ X X B(r,, R,). We take numbers r, < r\ < t, < R,' < R,
and denote by ^ the open subset of ^ which corresponds to X X B(r^, R,'). The
set S,C ^, which corresponds to X x A(^, ^), is compact because X is compact, and
therefore Z\U^ i S, is an open subset of Z. We apply the gluing procedure to the
spaces p = z\ur^ s,, p' = Ur^(^\s,), p, - U^^A),
                   Q= U^,(X x (^£(0, r;)) U X x D(0, RQ),
                   Q^ == U^,(X x B(r;, t,) U X x B(^, R;)),

and to the canonical isomorphism f\ P^ -^ Qr One has

                   P' u,Q^ U (X x (P^O, rj) U X x D(0, R,)).
                          1=1
From Lemma 3.7.9 it follows that the space Z' = P u^Q is Hausdorff and compact.
In particular, the morphism ^' : Z' -> X is compact.
      Furthermore, the above construction restricted to the fibre at x gives a compact
Jf (^-analytic space Z^ such that the connected component of the point y is a smooth


## CD PDF page 195

CHAPITRE 8


THÉORIE DE BEDFORD–TAYLOR




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


## CD PDF page 196

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
est stationnaire à partir du cran 1. Dans notre cadre, nous ne savons même pas si la
hiérarchie ordinale des espaces de fonctions psh est stationnaire. Cependant, tous les
exemples de fonctions psh que nous connaissons appartiennent au premier cran de cette
hiérarchie.
Définition 8.1.7. — On note CPshX le plus petit sous-faisceau du faisceau CX des
fonctions continues sur X tel que pour tout ouvert U de X, l’ensemble CPshX (U ) vérifie
les propriétés :
   i) Il contient les fonctions lisses u sur U telles que d′ d′′ u ⩾ 0 ;


## CD PDF page 197

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


## CD PDF page 198

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

Proposition 8.1.12. — Le faisceau des fonctions psh et localement intégrables sur X
est le plus petit sous-faisceau L1 PshX du faisceau des fonctions localement intégrables
sur X tel que, pour tout ouvert U de X, l’ensemble L1 PshX (U ) vérifie les propriétés :
  i) Il contient les fonctions lisses u sur U telles que d′ d′′ u ⩾ 0 ;
  ii) Si (un ) est une suite décroissante d’éléments de L1 PshX (U ) qui converge simple-
ment vers une fonction localement intégrable u sur U , alors u appartient à L1 PshX (U ).

Démonstration. — On définit une suite L1 PshX,α de sous-faisceaux du faisceau des fonc-
tions localement intégrables sur X de manière analogue à ce qui a été fait pour PshX,α
et on démontre par récurrence transfinie que L1 PshX,α = L1loc ∩ PshX,α . Seul le cas d’un
ordinal successeur est non trivial ; supposant L1 PshX,α = L1loc ∩ PshX,α , démontrons que
cette égalité persiste pour α + 1. L’inclusion L1 PshX,α+1 ⊂ L1loc ∩ PshX,α+1 est évidente.
   Inversement, soit u une fonction de PshX,α+1 (U ) qui est localement intégrable ; il
s’agit de démontrer qu’elle appartient à L1 PshX,α+1 (U ). Cela se vérifie localement sur U
ce qui permet de supposer que u est limite décroissante d’une suite (un ) de fonctions
de PshX,α (U ). Pour tout n, un est semicontinue supérieurement, donc localement majo-
rée, et est minorée par la fonction localement intégrable u, si bien que un est localement
intégrable. On a donc un ∈ L1loc PshX,α = L1 PshX,α par l’hypothèse de récurrence. Ainsi,
u ∈ L1 PshX,α+1 .

Définition 8.1.13. — On dit qu’une fonction psh sur un ouvert de X est localement
approchable si c’est une section du faisceau PshX,1 .



                        § 8.2. CONVEXITÉ TROPICALE

  Soit X un espace G-tropical affiné.

Proposition 8.2.1. — Soit u1 , . . . , un des fonctions psh sur X. Soit Ω un ouvert
convexe de Rn et soit g : Ω → R une fonction lisse, convexe, croissante par rapport


## CD PDF page 199

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

Corollaire 8.2.2. — On reprend les hypothèses de la proposition mais on suppose
seulement que g est la limite d’une suite décroissante (gk ) de fonctions lisses, convexes,
croissantes en chaque variable. Si α est un ordinal tel que pour tout i, ui appartient
à PshX,α , la fonction u appartient à PshX,α+1 . Si la suite (gk ) converge uniformémement
vers g, alors u appartient à PshX,sup(α,1) .

Démonstration. — La suite (gk (u1 , . . . , un )) est décroissante et converge simplement
vers g(u1 , . . . , un ). D’après la proposition, ces fonctions sont dans PshX,α . Par suite,
g(u1 , . . . , un ) est dans PshX,α+1 .
   Faisons l’hypothèse supplémentaire que la suite (gk ) converge uniformément vers g et
démontrons que g(u1 , . . . , un ) est dans PshX,sup(1,α) . On raisonne encore par récurrence
sur α. Le cas α = 0 est traité par la première partie ; supposons alors α > 0.
   Supposons que α soit un ordinal limite. Soit x un point de X ; il existe un voisinage
ouvert U de x et un ordinal β < α tels que uk |U ∈ PshX,β (U ) pour tout k. La première
partie de la démonstration affirme que g(u1 , . . . , un )|U = g(u1 |U , . . . , un |U ) appartient à
PshX,β+1 , donc à PshX,α puisque β + 1 < α.
   Supposons maintenant que α soit le successeur d’un ordinal β. Soit x un point de X ;
il existe un voisinage ouvert U de x et, pour tout k ∈ {1, . . . , n}, une suite décroissante
(vk,m ) de fonctions de PshX,β (U ) qui converge vers uk |U . Pour tout entier m, la fonction


## CD PDF page 200

200                          CHAPITRE 8. THÉORIE DE BEDFORD–TAYLOR

gm (v1,m |U , . . . , vn,m |U ) appartient à PshX,β , car gm est lisse. On a
  gm+1 (v1,m+1 |U , . . . , vn,m+1 |U ) ⩽ gm (v1,m+1 |U , . . . , vn,m+1 |U ) ⩽ gm (v1,m1 |U , . . . , vn,m |U ),
si bien que la suite (gm (v1,m1 |U , . . . , vn,m |U )) est décroissante. Comme (gm ) converge
uniformément vers g et comme pour tout k, la suite (vk,m ) converge simplement
vers uk |U , cette suite converge simplement vers g(u1 |U , . . . , un |U ). Cela démontre que
g(u1 , . . . , un )|U appartient à PshX,β+1 , c’est-à-dire à PshX,α .

Corollaire 8.2.3. — Soit α un ordinal et soit u1 , . . . , un des fonctions psh sur X,
appartenant à PshX,α . La fonction x 7→ max(u1 (x), . . . , un (x)) appartient à PshX,sup(α,1) ,
et est en particulier psh.
Démonstration. — D’après le lemme 1.7.6, la fonction t 7→ max(t1 , . . . , tn ) sur Rn est
limite uniforme de la famille de fonctions t 7→ log(eat1 + · · · + eatm )/a, lorsque a → +∞.
Ces fonctions sont lisses, convexes et croissantes en chaque variable. L’assertion découle
alors du corollaire précédent.

Corollaire 8.2.4. — Soit Ω un ouvert convexe de Rn et soit g : Ω → R une fonc-
tion convexe, croissante par rapport à chaque variable. Pour toute suite (u1 , . . . , un ) de
fonctions continues psh sur X, la fonction g(u1 , . . . , un ) est continue et psh. Plus précisé-
ment, si α est un ordinal tel que u1 , . . . , un appartiennent à CPshX,α , on a g(u1 , . . . , un ) ∈
CPshX,sup(1,α) .
Démonstration. — Comme g est convexe sur l’ouvert Ω, elle est continue ; puisque les ui
sont continues, la fonction g(u1 , . . . , un ) est continue. D’après la proposition 8.1.11, il
suffit de démontrer qu’elle appartient à PshX,sup(1,α) . D’après cette même proposition,
les fonctions uk appartiennent à PshX,α .
   Soit x ∈ X et soit Ω′ un voisinage ouvert convexe relativement compact de
(u1 (x), . . . , un (x)) dans Ω. Comme les ui sont continues, la partie U de X formée des
x ∈ X tels que (u1 (x), . . . , un (x)) ∈ Ω′ est ouverte. Par convolution, g|Ω′ est limite
uniforme d’une suite (gk ) de fonctions lisses qui sont convexes et croissantes en chaque
variable. D’après le corollaire précédent, g(u1 , . . . , un )|U appartient à PshX,sup(1,α) . Cela
conclut la démonstration.

Proposition 8.2.5. — Soit X un espace G-tropical affiné. Soit f : X → E une carte
tropicale, soit P un sous-espace paralinéaire de E contenant f (X) et soit v une fonction
convexe continue sur P (définition 1.10.5). Alors la fonction f ∗ v sur X est continue et
psh.
Démonstration. — Le sous-faisceau de CP formé des fonctions v telles que f ∗ v soit
psh contient les fonctions lisses telles que d′ d′′ v ⩾ 0 et est stable par limite uniforme. Il
contient donc le faisceau des fonctions convexes sur P . Cela démontre la proposition.

Définition 8.2.6. — Soit X un espace G-tropical affiné. On dit qu’une fonction u
sur X est tropicalement convexe si pour tout point x de X, il existe un voisinage U
de x, une carte tropicale f : U → E sur U , une partie paralinéaire P de Ttrop qui contient
f (U ) et une fonction convexe convexe v sur P tel que u|U = f ∗ v.
  Une fonction tropicalement convexe est psh.


## CD PDF page 201

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

Proposition 8.3.2. — Soit X l’espace tropical de niveau n associé à Rn . Soit U un
ouvert convexe de Rn , soit u une fonction sur U à valeurs dans R ∪ {−∞} qui n’est pas
identiquement −∞. Les assertions suivantes sont équivalentes :
  (i) La fonction u appartient à PshX ;
  (ii) La fonction u est à valeurs finies et est convexe ;
  (iii) La fonction u est localement intégrable et vérifie d′ d′′ [u] ⩾ 0 ;
  (iv) La fonction u appartient à CPshX,1 .
En particulier, les faisceaux sur X des fonctions psh, des fonctions continues psh et des
fonctions localement convexes coïncident.

Démonstration. — Soit U un ouvert de X et soit u une fonction lisse sur U telle que
d′ d′′ u ⩾ 0. La hessienne de u est donc une forme quadratique positive en tout point. Si
U est convexe, on en déduit que u est une fonction convexe sur U .
   (i)⇒(ii). Soit Conv∗X le sous-faisceau de CX constitué des fonctions qui, localement,
sont soit finies et localement convexes, soit identiquement −∞. D’après ce qui précède, il
contient les fonctions lisses à d′ d′′ positif. Par ailleurs, soit U un ouvert convexe de X et
soit (uk ) une suite de fonctions finies convexes sur U qui converge simplement vers une
fonction u sur U . Démontrons que u est soit finie et convexe, soit identiquement −∞.
On peut supposer que les uk sont toutes finies et convexes.


## CD PDF page 213

                § 8.9. UN EXEMPLE DE CALCUL DE MESURE DE MONGE-AMPÈRE                              213

Il contient les suites de fonctions lisses d’après ce qui précède, donc contient toutes les
suites de fonctions psh.



§ 8.9. UN EXEMPLE DE CALCUL DE MESURE DE MONGE-AMPÈRE

8.9.1. — Soit X un espace tropical de niveau n, sans bord. Soit (f1 , . . . , fm ) une famille
finie de fonctions affines sur X et soit f : X → Rm la carte tropicale correspondante.
Posons g = max(f1 , . . . , fm ). C’est une fonction continue psh sur X (exemple 8.2.1).
Le but de ce paragraphe est de fournir une description tropicale de la mesure positive
MA(g).
   Pour cela, nous commençons par en étudier l’analogue paralinéaire.
8.9.2. — Soit C un cône polyédral calibré de dimension ⩽ n dans Rm et soit ξ son
sommet. On suppose que le calibrage µ de C est adapté à une décomposition cellu-
laire (Cj )j∈J de C dont les cellules sont des cônes polyédraux de sommet ξ ; notons µj
le vecteur-volume de Cj . Soit Vj le sous-espace affine de Rm engendré par Cj .
   Soit I l’ensemble des i ∈ {1, . . . , m} tels que P     ξi = max(ξ1 , . . . , ξm ). Pour tout nombre
réel ε > 0 et tout x ∈ Rm , posons gε (x) = ε log( i∈I exp(xi )/ε)). Cette fonction sur Rm
est convexe et lisse (proposition 1.7.7). Lorsque ε → 0, elle converge uniformément vers
g0 : x 7→ maxi∈I xi . En particulier, elle converge uniformément vers la fonction g : x 7→
max(x1 , . . . , xn ) dans le voisinage de ξ défini par les inégalités xj < max(ξ1 , . . . , ξn ) pour
j ̸∈ I.
   Soit j ∈ J. Appliquons la proposition 1.7.7 aux cônes Cj − ξ (de sommet 0) et aux
formes linéaires x 7→ xi , pour i ∈ I. La mesure positive ⟨(d′ d′′ g1 )n , µj ⟩ sur Cj est
absolument continue par rapport à la mesure de Lebesgue et est de masse finie ; notons λj
cette masse. C’est un nombre réel positif ou nul ; il est strictement positif si et seulement
la famille (xi |Vj )i∈I est très séparante (définition 1.7.4) ; un indice i0 étant fixé, cela
revient à demander que l’image de Vj sous (xi − xi0 )i soit de dimension < n. Pour toute
fonction ψ sur Cj , continue et à support compact, on a
                                   Z
                                       ψ⟨(d′ d′′ gε )n , µ⟩ → λj ψ(0)
                                   Cj

lorsque ε → 0. P
   Posons λC = j∈J λj . C’est un nombre réel positif ou nul. Il est nul si et seulement
l’image sous (xi − xi0 ) de C est e dimension < n. Il ne dépend pas du choix de la
décomposition cellulaire (Cj ).
   Observons que C (n) = ∅ si et seulement si dim(C) < n ; dans ce cas, on a λC = 0.
Dans le cas contraire, C (n) est un cône de sommet ξ et l’on a λC = λC (n) .
   Soit U un voisinage paralinéaire de ξ dans C et soit ψ une fonction continue à support
compact sur V . Appliquons la proposition 1.7.7 aux cônes Cj − ξ (de sommet 0) et aux
formes linéaires x 7→ xi , pour i ∈ I. On en déduit que pour toute fonction ψ sur C,
continue et à support compact, on a
                               Z
                                  ψ⟨(d′ d′′ gε )n , µ⟩ → λC ψ(0)
                                   C
lorsque ε → 0.


## CD PDF page 214

214                      CHAPITRE 8. THÉORIE DE BEDFORD–TAYLOR

Remarque 8.9.3. — Comme ci-dessus, considérons un cône polyédral calibré C ⊂ Rm
de sommet ξ, et soit I l’ensembles des i tels que ξi = max(ξ1 , . . . , ξm ). Soit pI : Rm → RI
la projection naturelle. Alors pI (C) est un cône polyédral de RI , de sommet pI (ξ).
Posons C ′ = C (pI ) ; c’est le plus grand sous-espace paralinéaire de C tel que l’application
linéaire pI induise une immersion par morceaux affine surjective de C ′ sur pI (C)(n) ;
c’est un cône. Munissons alors pI (C)(n) (ou pI (C), si l’on veut) du calibrage image de la
restriction à C ′ du calibrage de C. Il résulte de la construction que l’on a λC = λpI (C) .

Proposition 8.9.4. — Soit X un espace tropical de niveau n, sans bord. Soit
(f1 , . . . , fm ) une famille finie non vide de fonctions affines sur X et soit f : X → Rm la
carte tropicale correspondante. Soit j ∈ {1, . . . , m}.
        P g = max(f1 , . . . , fm ). Pour tout ε > 0 et tout x ∈ X, posons gε (x) =
   Posons
ε log( m     i=1 exp(fi (x)/ε)). Les fonctions gε sont lisses, psh, tropicalisées par f ; de plus,
gε converge uniformément vers g quand ε tend vers 0. En particulier, la fonction g =
max(f1 , . . . , fm ) sur X est psh.
                         (n)
   Pour tout x ∈ Σf , notons Πf,x le cône tropical de f en x (définition 5.4.6) et λx le
                                                                                                (n)
nombre réel positif ou nul associé au cône calibré Πf,x de Rm . L’ensemble des x ∈ Σf
tels que λx ̸= 0 est fermé et discret dans X et l’on a
                                             X
                                   MA(g) =         λx δx .
                                                    (n)
                                                x∈Σf


En particulier, MA(g) est nul au voisinage de x si la dimension tropicale de (fi − fj )i
en x est < n.

Démonstration. — Soit h la fonction (x1 , . . . , xm ) 7→ max(x1P      , . . . , xm ) sur Rm ; pour
tout ε > 0, soit hε la fonction donnée par (x1 , . . . , xm ) 7→ ε log( m  i=1 exp(xi /ε)). D’après
le lemme 1.7.6, la fonction hε sur R est convexe et l’on a g = f ∗ h = limε→0+ f ∗ hε
                                          m

(uniformément). D’après la proposition 8.2.5, la fonction g sur X est donc psh et la
mesure positive MA(g) est limite de mesures lisses d′ d′′ (f ∗ hε )n .
                              (n)
   La partie squelettique Σf de X est un support fort des formes d′ d′′ (f ∗ hε )n ; elle
contient donc le support de la mesure associée et, par passage à la limite, le support de
la mesure MA(g).
   Soit x ∈ X. D’après ce qui précède, la mesure MA(g) est nulle au voisinage de x si
       (n)                                          (n)
x ̸∈ Σf . On suppose dans la suite que x ∈ Σf .
   Soit I l’ensemble des i ∈ {1, . . . , m} tels que g(x) = fi (x). On a donc g = maxi∈I (fi )
au voisinage de x.
                          (n)
   Supposons que x ̸∈ ΣpI ◦f ; dans ce cas, le même argument que précédemment entraîne
que MA(g) est nulle au voisinage de x. D’autre part, le cône pI (Πf,x ) est de dimension <
n, et donc λx = 0 d’après la remarque 8.9.3. Sinon, on peut considérer le cône tropical de
pI ◦ f en x, et son invariant λ coïncide avec celui de Πf,x , comme on le voit en combinant
la remarque 5.5.7 et la remarque 8.9.3. On peut donc supposer que I = {1, . . . , m}. On
peut aussi supposer que X est compact.
                                                  (n)
   Soit C une décomposition cellulaire de Σf en f -cellules commodes (lemme 14.1.5).
                             (n)
Soit V la réunion dans Σf          des n-cellules de C qui contiennent x ; c’est un voisinage
                   (n)
compact de x dans Σf . Posons ξ = f (x).


## CD PDF page 344

344           CHAPITRE 12. PARTIES SQUELETTIQUES D’UN ESPACE ANALYTIQUE

                       (d)
Soit u ∈ Int(U ) ∩ Σg et soit x = j(u) ; on a x ∈ Int(V ), donc x ∈ Int(X). De plus, on
a dimtrop,u (g) = d, donc dimtrop,x (f ) = d.

Lemme 12.3.6. — Supposons que la valeur absolue du corps k n’est pas triviale. Soit X
un espace analytique localement holomorphiquement séparé. Pour tout point x ∈ X,
il existe un voisinage analytique compact V de x et un moment f : V → T tel que
ftrop (x) ̸∈ ftrop (∂(V /X)).
Démonstration. — Soit W un voisinage analytique compact de x qui est holomorphi-
quement séparé.
   Soit y ∈ W ; démontrons qu’il existe une fonction fy ∈ O(W ), inversible en x, telle
que |fy (y)| ̸= |fy (x)|. Par définition d’un espace holomorphiquement séparé, il existe
f ∈ O(W ) tel que |f (y)| =       ̸ |f (x)|. Si f (x) ̸= 0, la fonction f convient. Supposons
f (x) = 0 ; alors f (y) ̸= 0 et, comme la valeur absolue de k n’est pas triviale, il existe
λ ∈ k × tel que |λ| < |f (y)| ; la fonction f + λ convient.
   Notons Wy l’ensemble défini par l’inégalité |fy | ̸= |fy (x)| ; c’est un voisinage
de y dans W . Comme ∂(W/X) est compact, il existe une famille finie (y1 , . . . , yn )
dans ∂(W/X) telle que les Wyi recouvrent ∂(W/X). Soit r = 12 inf|fyi (x)| et soit V le
domaine analytique compact de W défini par les conditions |fyi | ⩾ r. On a |fyi (x)| > r
pour tout i, de sorte que V est un voisinage de x dans W , et a fortiori dans X. Pour
tout i, notons fi la fonction fyi |V ; elle est inversible.
   Soit f : V → Gnm le moment (f1 , . . . , fn ). Démontrons qu’il vérifie la condition requise
par le lemme. Soit y ∈ ∂(V /X). Il y a deux possibilités. Ou bien il existe i ∈ {1, . . . , n}
tel que |fi (y)| = r ; dans ce cas, ftrop (y) ̸= ftrop (x). Ou bien, y ∈ ∂(W/X) ; dans ce cas,
il existe i ∈ {1, . . . , n} tel que y ∈ Wyi et |fi (y)| =
                                                         ̸ |fi (x)|, par construction de Wyi , donc
ftrop (y) ̸= ftrop (x).

Remarque 12.3.7. — Le lemme est faux lorsque la valeur absolue du corps k est
triviale. Prenons pour espace X le disque unité ouvert et point x l’origine ; l’application
r 7→ ηr induit un homéomorphisme de [0; 1[ sur X, qui applique 0 sur le point x. Soit V
un voisinage analytique compact de x dans X. La composante connexe de x dans V est
l’image d’un intervalle de la forme [0; r], pour r ∈ ]0; 1[ ; c’est donc le disque fermé de
rayon r et de centre x. Sur cet espace, toute fonction inversible est de norme constante,
donc ne sépare pas x du bord ηr de cette composante connexe.



      § 12.4. STRUCTURE G-TROPICALE AFFINÉE SUR UN ESPACE
                             ANALYTIQUE

  Soit X un espace k-analytique topologiquement séparé.(1) Dans ce paragraphe, nous
munissons l’espace X d’une structure d’espace G-tropical (définition 3.1.4) affiné (§6.1) ;
cela sera toujours cette structure que nous considérerons. Les structures paralinéaires
considérées seront relatives au couple (Q, R). En particulier, l’espace Rn est muni de sa

(1)
  Par définition, un espace G-tropical est topologiquement séparé ; dans la suite de ce texte, nous
avons pris garde à indiquer cette hypothèse lorsqu’elle était nécessaire, tout éventuel oubli ne serait
qu’inadvertance.


## CD PDF page 345

             § 12.4. STRUCTURE G-TROPICALE AFFINÉE SUR UN ESPACE ANALYTIQUE             345

Q-structure standard et les polyèdres de Rn sont définis par des inégalités dont la partie
linéaire est Q-rationnelle.

Proposition 12.4.1. — Soit X un espace k-analytique topologiquement séparé. Lors-
qu’on prend pour domaines de X ses domaines analytiques et pour G-faisceau des
fonctions paralinéaires le G-faisceau en Q-espaces vectoriels engendré par les fonctions
constantes et celles de la forme ftrop , on munit X d’une structure d’espace G-tropical.

   Nous munirons implicitement tout espace k-analytique séparé de la structure d’espace
G-tropical décrite dans cette proposition.
Démonstration. — L’espace X a été supposé topologiquement séparé ; il est localement
compact et possède une base d’ouverts dénombrables à l’infini (lemme 11.1.15).
   Les fonctions paralinéaires sur X sont des fonctions continues.
   Vérifions les autres axiomes des espaces G-tropicaux. Soit W un domaine analytique
de X et soit f : W → Rm une application paralinéaire.
   – Si W est compact, alors f (W ) est un polyèdre compact de Rm . On peut en effet
raisonner G-localement sur W , ce qui ramène au cas où f est de la forme q ◦ htrop , où
h : W → Gnm est un moment sur W et q : Rn → Rm est une fonction affine à partie
linéaire rationnelle. L’assertion se déduit du théorème 12.2.4.
   – Si P est un sous-espace paralinéaire de Rm contenant f (W ) et si φ : P → R est
paralinéaire, alors φ ◦ f est paralinéaire. On peut encore raisonner localement, et est
évidente lrosque f est de la forme q ◦ htrop comme ci-dessus.
   – Si P est un sous-espace paralinéaire de Rm , alors f −1 (P ) est un domaine de W . On
peut encore raisonner G-localement, donc supposer que f est de la forme q ◦ htrop comme
ci-dessus ; ainsi f −1 (P ) = h−1     −1
                               trop (q (P )). Comme q est à partie linéaire Q-rationnelle,
q −1 (P ) est un polyèdre de Rn . Ainsi, f −1 (P ) est défini par des inégalités de la forme
|u| ⩽ λ, où u est une fonction inversible sur W et λ un nombre réel strictement positif,
donc est un domaine analytique.

12.4.2. — Soit X un espace k-analytique topologiquement séparé, considéré comme
espace G-tropical, soit f : X → T un moment et soit x un point de X. La dimension
tropicale de f en x coïncide avec la dimension tropicale de la carte G-tropicale ftrop .
  Il en résulte que pour toute carte G-tropicale f sur X, on a l’inégalité
(12.4.2.1)                   dimtrop,x (f ) ⩽ dk (x) ⩽ dimx (X).

Lemme 12.4.3. — Soit X un espace analytique topologiquement séparé et soit P une
partie fidèlement paralinéaire de X. Il existe un G-recouvrement (Pi ) de P par des parties
paralinéaires et, pour tout i, un moment fi sur un domaine Vi de X contenant Pi , tels
que fi,trop soit une carte paralinéaire sur Pi .

Démonstration. — Soit f ∈ Λ(P ) une carte paralinéaire sur P . On peut raisonner G-
localement, et donc supposer que f est de la forme q ◦ htrop , où h est un moment sur X
et q une application affine. Alors, htrop ∈ Λ(P ).

Lemme 12.4.4. — Soit X un espace k-analytique topologiquement séparé, de dimen-
sion ⩽ n. Pour toute partie paralinéaire P de X, on a dim(P ) ⩽ n et l’ensemble ∂(X)∩P
est n-négligeable au sens de la définition 2.1.14.


## CD PDF page 346

346           CHAPITRE 12. PARTIES SQUELETTIQUES D’UN ESPACE ANALYTIQUE

Démonstration. — L’assertion est G-locale. Cela permet de supposer que X est compact
et qu’il existe un moment f sur X tel que ftrop ∈ Λ(P ). D’après le corollaire 12.2.5,
ftrop (X) est une partie paralinéaire de dimension ⩽ n, qui contient ftrop (P ) ; par suite,
P est de dimension ⩽ n. D’après le corollaire 12.2.6, ftrop (∂(X)) est contenu dans une
partie paralinéaire de dimension ⩽ (n − 1) ; a fortiori, ∂(X) ∩ P est n-négligeable.

12.4.5. — Un morphisme p : Y → X d’espaces analytiques topologiquement sépa-
rés, non nécessairement définis sur le même corps, induit un morphisme d’espaces G-
tropicaux.
12.4.6. — Soit X un espace k-analytique topologiquement séparé ; définissons mainte-
nant une structure d’espace G-tropical affiné sur X.
  Soit u une fonction numérique définie sur un domaine V de X. On dit que u est affine
au voisinage d’un point x de V s’il existe un voisinage U de x dans V , un moment f
sur U , un nombre rationnel a et un nombre réel c tels que u = aftrop + c sur U . On dit
que u est affine si elle l’est au voisinage de tout point de V .
  Les fonctions affines sur un domaine de X forment un sous-préfaisceau du G-faisceau
des fonctions paralinéaires. Par définition d’une fonction affine, les fonctions affines défi-
nissent un faisceau pour la topologie usuelle ; par définition d’une fonction paralinéaire,
toute fonction paralinéaire est G-localement affine.
  On a ainsi défini une structure d’espace G-tropical affiné sur X au sens du §6.1.

Proposition 12.4.7. — Soit X un espace analytique topologiquement séparé et soit x
un point de X. Si X est presque bon en x, alors l’espace G-tropical affiné associé à X
est décent en x (définition 6.3.1).

Démonstration. — Soit V un domaine analytique de X contenant x.
   Montrons tout d’abord que si f est une fonction affine sur V , il existe un voisinage
ouvert U de x dans X et un prolongement affine de f |V ∩U à U . Pour ce faire, on peut
remplacer V par n’importe quel voisinage domanial de x dans V , et donc supposer que
f = agtrop + b où a ∈ Q, où g est un moment sur V et où b ∈ R. Puisque X est presque
bon en x, il existe h ∈ OX,x×
                                telle que |h(x) − g(x)| < |g(x)|. Choisissons un voisinage
ouvert U de x sur lequel h est définie et tel que |h − g| < |g| sur U ∩ V . On a alors
htrop = gtrop sur U ∩ V , et ahtrop + b est un prolongement de f |U ∩V à U tout entier.
   Comme X et presque bon en x, il est séparé en x, et (V,^   x) est alors un ouvert quasi-
                       ^
compact et non vide de (X, x). On peut donc décrire
                                       [
                              ^
                              (V, x) =   PH       {fij }j
                                          ^ (x)/e
                                                k
                                               i

où les fij sont des éléments de e       k × . Par presque bonté de X en x, il existe une famille
(gij ) d’éléments de OX,x    ×
                                telle que g^  ij (x) = fij pour tout (i, j) ; posons rij = |gij (x)|.
Choisissons un voisinage ouvert U de x sur lequel les gij sont définis. La description de
^
(V,  x) assure alors que celui-ci coïncide avec le domaine de (U, x) défini par la condition
W V
  i    j |gij | ⩽ rij ; autrement dit,
                                   W V
                                       si l’on restreint suffisamment U alors V ∩U est le domaine
de U défini par la condition i j |gij | ⩽ rij . Il s’ensuit que X est décent en x.


## CD PDF page 347

                  § 12.5. QUELQUES CLASSES DE FONCTIONS PARALINÉAIRES                           347

    § 12.5. QUELQUES CLASSES DE FONCTIONS PARALINÉAIRES

12.5.1. — Soit X un espace k-analytique topologiquement séparé. Un Gstr -recouvrement
de X est un G-recouvrement (Xi ) de X par des domaines analytiques stricts strict (au
sens de ce texte, qui diffère du sens classique si k est trivialement valué, cf. 11.8.1) ;
un tel recouvrement existe si et seulement si X lui-même est strict. Si c’est le cas, on
note XGstr le site dont la la catégorie sous-jacente est celle des domaines k-analytiques
stricts de X (les flèches étant les inclusions) et dont les familles couvrantes sont les
Gstr -recouvrements ; sa topologie est appelée la Gstr -topologie.
12.5.2. — Notons PLZX le sous-faisceau de PLX sur XG qui associe à un domaine
analytique V de X l’ensemble des fonctions paralinéaires sur V qui sont G-localement
de la forme log|g|+c où g est une fonction analytique inversible et c une constante réelle.
Ses sections sont appelées fonctions paralinéaires entières.
  Supposons de plus que X est strict. On note PLstr    X le sous-faisceau de PLX |XGstr sur
XGstr qui associe à un domaine strictement analytique V de X l’ensemble des fonctions
paralinéaires sur V qui sont Gstr -localement de la forme λ log|g| où g est une fonction
analytique inversible et λ un nombre rationnel ; ses sections sont appelées fonctions
paralinéaires strictes. Et l’on note PLstr,Z
                                       X     le sous-faisceau de PLstr
                                                                    X sur XGstr qui associe
à un domaine strictement analytique V de X l’ensemble des fonctions paralinéaires sur
V qui sont Gstr -localement de la forme log|g| où g est une fonction analytique inversible.
Ses sections sont appelées fonctions paralinéaires strictement entières.

Lemme 12.5.3. — Le sous-faisceau PLZX de PLX en est un sous-faisceau en groupes
                                                                                 str,Z
abéliens, stable sous min et max. Si X est strict, les sous-faisceaux PLstr
                                                                         X et PLX      de
PLX |XGstr en sont des sous-faisceaux en groupes abéliens, stables sous min et max.

Démonstration. — Nous allons traiter le cas de PLstr,Z    X    ; les autres sont établis de manière
analogue. On suppose donc que X est strict, et l’on se donne un domaine analytique
strict V de X. Il est clair que 0 ∈ PLstr,Z  X (V ). Soit f et g deux fonctions appartenant
      str,Z
à PLX (V ). Soit (Vi ) et (Wj ) deux Gstr -recouvrements de V tels f |Vi soit pour tout
i égale log|fi | pour une certaine fonction analytique inversible fi sur Xi , et que g|Wi j
soit pour tout j égale à log|gj | pour une certaine fonction analytique inversible gj sur
Wj . Pour tout (i, j), posons hij = fi |Vi ∩Wj · gj |−1
                                                     Vi ∩Wj . On a alors pour tout (i, j) l’égalité
(f − g)|Vi ∩Wj = log|hij |, ce qui montre que f − g appartient à PLstr,Z     X (V ). Ainsi, PLX
                                                                                               str,Z

est bien un sous-faisceau en groupes abéliens de PLX |XGstr .
   Pour tout (i, j), notons Vij− et Vij+ les domaines analytiques stricts de Vi ∩ Wj définis
par les inégalités |fi /gi | ⩽ 1 et |gi /fi | ⩽ 1 respectivement. Les Vij+ et Vij− constituent
un Gstr -recouvrement de V . Sur Xi+ , on a max(f, g) = log|fi | et min(f, g) = log|gi | ;
sur Xi− , on a max(f, g) = log|gi | et min(f, g) = log|fi |. Il en résulte que max(f, g) et
min(f, g) appartiennent à PLstr,ZX (V ).



Proposition 12.5.4. — Soit X un espace k-analytique topologiquement séparé, soit
x ∈ X et et soit u une fonction paralinéaire et lisse sur X. Il existe alors un entier n ⩾ 1,
un voisinage analytique U de x dans X, un nombre réel c et une fonction holomorphe
inversible h sur U telle que nu|U = c + log(|h|).


## CD PDF page 421

CHAPITRE 15


FORMES DIFFÉRENTIELLES RÉELLES EN
GÉOMÉTRIE ULTRAMÉTRIQUE




   Soit X un espace k-analytique topologiquement séparé. La définition 14.3.5 le munit
d’une structure d’espace G-tropical affiné.
   On en déduit des notions de formes et G-formes différentielles de type (p, q) sur X, à
coefficients dans une classe de coefficients.
   Au §12.9.5, nous avons expliqué comment ses parties squelettiques le munissent d’une
structure d’espace G-tropical vertébré de niveau n. La définition 14.3.5 munit les parties
squelettiques de X d’un n-calibrage, de sorte que X est muni d’une structure d’espace
G-tropical calibré de niveau n.
   On en déduit une théorie de l’intégration des (n, n)-formes et des (n − 1, n)-formes
sur X, ainsi qu’une théorie de courants.
   Dans ce chapitre, nous explorons plus avant les propriétés des formes différentielles
sur les espaces analytiques.
   Nous allons également démontrer que les espaces analytiques sans bord sont harmo-
nieux et munir les espaces analytiques purement de dimension n d’une structure d’espace
tropical.




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


## CD PDF page 422

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

Proposition 15.1.3. — Soit G une classe de coefficients. Soit X un espace analytique
topologiquement séparé et soit u une fonction numérique sur X.
  a) Pour que u soit G-localement de classe G , il faut et il suffit que u|Xred le soit.
  b) Si X est presque bon, pour que u soit localement de classe G , il faut et il suffit que
u|Xred le soit.

  Une variante de cet énoncé vaut pour les formes et les G-formes.
Démonstration. — Si u est localement (resp. G-localement) de classe G , il en est de
même de sa restriction à Xred . Démontrons la réciproque.
   a) Supposons que u|Xred soit G-localement de classe G . Soit V un domaine affinoïde
de Xred sur lequel il existe un moment f : V → Gnm et une fonction φ de classe G sur Rn
telle que u|V = φ ◦ ftrop . On déduit du théorème de Gerritzen–Grauert (voir par exemple
[128], théorème 3.1) que V est recouvert par une réunion de domaines affinoïdes de la
forme Wred , où W est un domaine affinoïde de X. Sur Wred , chacune des fi se relève
en une fonction gi sur W ; ces fonctions sont inversibles et ont même norme que fi ;
elles définissent un moment g : W → Gnm tel que uW = φ ◦ gtrop . Cela prouve que u est
G-localement de classe G .
   b) Soit x un point de X et soit V un voisinage analytique de x dans Xred sur lequel
il existe un moment f : V → Gnm et une fonction φ de classe G sur Rn telle que u|V =
φ ◦ ftrop . Comme X est presque bon en x, chaque fi (x) ∈ H (x) est approchée par une
fonction gi ∈ OX,x . En particulier fi et gi ont même norme au voisinage de g. Ainsi, les
gi définissent un moment g défini au voisinage de X sur lequel on a u = φ ◦ gtrop ; cela
prouve que u est de classe G au voisinage de x.


## CD PDF page 432

432 CHAPITRE 15. FORMES DIFFÉRENTIELLES RÉELLES EN GÉOMÉTRIE ULTRAMÉTRIQUE

Comme Int(Wx /X) est une partie ouverte de Wx qui contient le support de λx ω, on a
aussi
                           Z ∂         Z ∂
                                λx ω =         λx ω.
                                  Wx            Int(Wx /X)

On a donc
                                    Z ∂             Z ∂
                                           λx ω =         λx ω,
                                       X             Wx

et cette dernière intégrale peut se calculer à l’aide de la formule (5.10.1.1).
                                              R∂
   A priori, le calcul tropical de l’intégrale Wx λx ω fait intervenir toute la tropicalisation
de ∂(Wx ). Remarquons cependant que la pleine force de la proposition 15.5.6 démontre
qu’on peut choisir Wx et un moment tropicalisant ω de sorte que ce calcul ne fasse
intervenir que la tropicalisation de ∂(X) ∩ Wx .

Remarque 15.6.4. — Soit X un espace analytique de niveau n. Soit f un moment
                                                                                   (n)
sur X et soit C une f -cellule commode de dimension n. Alors C̊ est un ouvert de Σf , par
définition d’une cellule commode ; comme il ne rencontre le bord de X, il est harmonieux
relativement à f (théorème 15.6.1). D’après la remarque 4.6.10, son calibrage est constant
relativement à f .
   Mais cette propriété résulte directement de la construction du calibrage de C, consi-
dérée comme partie squelettique de Σf , au moyen d’une décomposition cellulaire de C
en f -cellules commodes dont C elle-même est l’unique cellule de dimension n.




§ 15.7. L’ESPACE TROPICAL ASSOCIÉ À UN ESPACE ANALYTIQUE

  Soit X un espace analytique purement de dimension n, topologiquement séparé. On le
considère comme espace G-tropical calibré de niveau n. Il est riche (théorème 12.10.6).

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


## CD PDF page 433

              § 15.7. L’ESPACE TROPICAL ASSOCIÉ À UN ESPACE ANALYTIQUE              433

15.7.2. — Soit X un espace analytique topologiquement séparé, purement de dimen-
sion n et soit V un domaine de X. Le domaine V est muni de deux façons, a priori
distinctes, d’une structure d’espace tropical de niveau n, soit comme espace analytique,
soit comme domaine de l’espace tropical X. La formule ∂(V ) = (∂(X) ∩ V ) ∪ ∂(V /X)
montre que ces deux structures coïncident.
Remarque 15.7.3. — Soit X un espace analytique de niveau n ; pour que l’on puisse
le munir d’une structure d’espace tropical de niveau n, il faut et il suffit que X soit
purement de dimension n. En effet, dans le cas contraire, il possède un domaine ana-
lytique compact non vide V tel que dim(V ) < n. L’espace X n’est donc pas riche : la
tropicalisation constante de V n’est couverte par aucun squelette de V puisque la seule
partie squelettique de V est vide.
