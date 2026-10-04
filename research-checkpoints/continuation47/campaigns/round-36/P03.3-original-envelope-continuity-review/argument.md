# Exact abstract scope and explicit original limitations

{
  "id": "P03.3",
  "status": "partial",
  "exact_result": "Proved a finite connected metric-graph obstacle lemma with contact/harmonic complementarity; a compact harmonic-skeleton criterion yielding continuity of the raw envelope over an entire competitor class for every finite continuous obstacle, by comparison and uniform obstacle stability; and an exact arbitrary-obstacle reduction under a closed open surjection with compact fibres, a class-preserving section, and fibrewise-constant competitors. No new positive-dimensional analytic class is asserted to satisfy all the criterion's hypotheses. The literal sharp P03.3 classification is not proved.",
  "proof_file": "P03.3-argument.md",
  "concrete_gaps": [
    "For the exact locally Fubini--Study/semipositive-real-PL union, globally realize every needed subharmonic finite-skeleton lift as an admissible semipositive real-PL competitor, with legal vertices and coefficients and the relative boundary checked.",
    "Verify harmonic lifting and comparison for every competitor in both branches of the exact analytic union, including attachment points, slope signs and weights, and all relevant curve pullbacks.",
    "Independently prove the finite-skeleton density/refinement and retraction statements for a specified positive-dimensional analytic class, including endpoints and type-4 points.",
    "Prove the required skeletal envelope identities after relevant scalar extensions for the full competitor class; pullback stability alone is insufficient.",
    "For the proposed proper-factor products, verify analytic projection openness, fibre Liouville and exact restriction/pullback stability over completed residue fields and scalar extensions.",
    "Determine sharp geometric hypotheses and necessity in the residual higher-dimensional normal or geometrically unibranch range, accounting for branches, relative boundary, and global competitors. No such necessity theorem is supplied."
  ]
}

# Full final proof

---
title: "Full-family continuity from finite harmonic skeletons: a partial result for P03.3"
author: "Fresh independent draft"
date: "2026-10-04"
---

# Result and exact scope

The sharp classification requested in P03.3 is **not proved here**. In particular, this draft does not assert continuity on every normal or geometrically unibranch analytic domain. It proves a finite-graph obstacle theorem, a compact-skeleton continuity criterion for an entire competitor class, and a proper-fibre reduction. All three proofs are given below. The criterion resolves a specific uniformity/cofinality mechanism: finite-skeleton envelopes dominate **every** competitor by comparison, and uniform approximation of the obstacle then controls the full envelope. No modulus of continuity for the competitors is assumed.

There is an important application gap. This draft does not verify all the criterion's hypotheses for the exact locally Fubini--Study/semipositive-real-PL union on any new positive-dimensional analytic class. Rational affinoids in the analytic projective line and their products with proper projective factors are proposed applications, not established geometric continuity theorems. The supplied unpublished claims, audit verdicts, and hashes are not used as proof inputs. No theorem about classical psh or CLD-v2 membership of the envelope is claimed.

The graph and compact-skeleton statements are mathematical proofs, subject to independent checking. The small rational computation at the end is a check of the graph construction, not a proof of an analytic identification or a classification.

# 1. A finite graph obstacle problem

Let $\Gamma$ be a nonempty finite connected metric graph. Subdivide it so that each edge joins distinct vertices; parallel edges are allowed. Write $V$ for its vertices, $E$ for its edges, and $\ell_e>0$ for the length of an edge. Fix a possibly empty set $B\subset V$ of designated boundary vertices. The vertex set may contain degree-two subdivision vertices. Let $g$ be a continuous function affine on each edge, with vertex values $g_v$.

For $u\in\mathbb R^V$ define the outgoing-slope sum

$$
L_vu=\sum_{e=vw}\frac{u_w-u_v}{\ell_e}.
$$

Each parallel edge is included separately. Let $\widetilde u$ be the affine interpolation of $u$ on $\Gamma$. Define the feasible set

$$
\mathcal F_g=\{u\in\mathbb R^V:u_v\leq g_v\ (v\in V),\quad L_vu\geq0\ (v\notin B)\}.
$$

Thus an affine-on-edges function is graph-subharmonic when its outgoing slopes have nonnegative sum at every nonboundary vertex. No inequality is imposed at a designated boundary vertex.

**Proposition 1 (greatest graph minorant and complementarity).** The set $\mathcal F_g$ has a greatest element $p$ in coordinatewise order. Its interpolation satisfies $\widetilde p\leq g$. At every $v\in B$,

$$p_v=g_v.$$

At every $v\notin B$,

$$p_v<g_v\quad\Longrightarrow\quad L_vp=0.$$

Consequently $\widetilde p$ is harmonic on the open set $\{\widetilde p<g\}$: it is affine on open edge segments and has zero total outgoing slope at every vertex in that set. This open set misses $B$.

**Proof.** Put $m=\min_{v\in V}g_v$. The constant vector $m$ is feasible. If $u,w\in\mathcal F_g$, their coordinatewise maximum $z$ is feasible: at a vertex $v$ choose $u$ with $z_v=u_v$ (interchange $u,w$ if necessary), and use $z_t\geq u_t$ at every neighboring vertex $t$ to obtain $L_vz\geq L_vu\geq0$. This also proves that replacing any feasible vector by its maximum with $m$ preserves feasibility.

The nonempty set

$$\mathcal F_g\cap\prod_{v\in V}[m,g_v]$$

is compact. Choose a maximizer $p$ of $\sum_vu_v$ there. For any feasible $u$, the vector $\max(p,u)$ belongs to this compact set. If $u_v>p_v$ at some coordinate, its sum is strictly larger. Therefore $u\leq p$; this proves the greatest-element assertion, without assuming a priori that a selected family of feasible vectors is cofinal.

For $v\in B$, increasing $p_v$ up to $g_v$ preserves every constraint: there is no constraint at $v$, and all neighboring outgoing-slope sums increase. Hence $p_v=g_v$. If $v\notin B$, $p_v<g_v$, and $L_vp>0$, increase just $p_v$ by a sufficiently small positive $\delta$. Its own outgoing-slope sum decreases by

$$\delta\sum_{e\ni v}\ell_e^{-1},$$

and stays nonnegative; all neighboring sums increase. The obstacle constraint stays valid. This contradicts maximality. If the graph has only one vertex and no edges, its slope sum is already zero and the conclusion follows directly. Finally, affine interpolation preserves the vertex obstacle inequalities throughout every edge. The stated harmonicity follows from complementarity. $\square$

**Proposition 2 (empty graph boundary).** If $B=\varnothing$, the greatest feasible vector is the constant $m=\min_Vg_v$.

**Proof.** For every vector $u$, $\sum_vL_vu=0$, because the two contributions from an edge cancel. Thus a feasible vector has $L_vu=0$ at every vertex. Choose a vertex at which $u$ is maximal. Every summand in its outgoing-slope sum is nonpositive, so every neighboring value equals the maximal value. Connectivity propagates equality to all vertices. Hence all feasible vectors are constant, and the largest admissible constant is $m$. $\square$

## An exact finite algorithm

When $B\ne\varnothing$, enumerate all subsets $A\subset V$ containing $B$. Impose

$$u_v=g_v\quad(v\in A),\qquad L_vu=0\quad(v\notin A).$$

This is a nonsingular Dirichlet linear system: a solution of the homogeneous system has zero values on $A$ and is harmonic elsewhere; propagation from a maximal and a minimal vertex, using connectivity, makes it identically zero. Solve the system and retain precisely the solutions satisfying all feasibility inequalities. Proposition 1 shows that the true $p$ appears: take $A=\{v:p_v=g_v\}$, which contains $B$, and use complementarity. A retained vector that dominates all retained vectors is therefore $p$. With rational lengths and obstacle values this procedure uses exact rational arithmetic. The number of systems is at most $2^{|V\setminus B|}$. This is a finite algorithm for a supplied finite graph, not an algorithm for the original analytic classification.

# 2. A compact-skeleton criterion for a full competitor class

The following hypotheses describe harmonic geometry and individual competitors, not continuity of the desired envelope.

Let $X$ be a nonempty compact connected Hausdorff space, and let $D\subset X$ be a finite, possibly empty, designated boundary set. A harmonic function on an open subset of $X\setminus D$ will be a member of a specified collection $\mathcal H$ of continuous functions; this collection must be invariant under adding constants and restricting to open subsets. Let $\mathcal C\subset C(X,\mathbb R)$ be an **entire** given competitor class.

A finite harmonic skeleton presentation for $(X,D,\mathcal H,\mathcal C)$ consists of the following data and hypotheses.

1. There is a collection of continuous retractions $r:X\to\Gamma$ onto finite connected metric graphs embedded in $X$. Every $\Gamma$ contains $D$ as designated graph boundary vertices $B=D$, and $r$ fixes $\Gamma$ pointwise. Subdivision at additional vertices is allowed. Graph-affine means affine on every edge of a chosen finite subdivision.

2. Every $f\in C(X,\mathbb R)$ is a uniform limit of functions $g=\gamma\circ r$, where $\gamma$ is graph-affine on one of these finite subdivided skeletons. These approximating obstacles need not be competitors or subharmonic.

3. For every such skeleton and every graph-affine $a$ with $L_va\geq0$ for $v\notin D$, its lift $a\circ r$ belongs to $\mathcal C$. All constant functions belong to $\mathcal C$, and $h+c\in\mathcal C$ whenever $h\in\mathcal C$ and $c\in\mathbb R$.

4. For every graph-affine $a$, the lift $a\circ r$ is harmonic on the inverse image of every graph-open set avoiding $D$ on which $a$ has zero outgoing-slope sum at each vertex. On an open edge segment, affine functions count as harmonic. In particular, constant lifts on the components discarded by the retraction must have this property. This is a substantive local harmonic-lifting hypothesis, including at branch attachments.

5. Every $h\in\mathcal C$ has harmonic comparison on relatively compact open sets in $X\setminus D$. Precisely: if $W$ is open, $\overline W\subset X\setminus D$, $W$ has nonempty topological boundary $\partial_XW$, $q$ is harmonic on an open neighborhood of $\overline W$, and $h\leq q$ on $\partial_XW$, then $h\leq q$ on $W$.

No assertion that these hypotheses are automatic in the original analytic setting is made. In particular, hypothesis 3 is a global realization assertion and hypothesis 5 concerns **every** member of the exact competitor union.

For a finite continuous obstacle $f$ on $X$, set

$$P_{\mathcal C}f(x)=\sup\{h(x):h\in\mathcal C,\ h\leq f\text{ on }X\}.$$

**Theorem 3 (full-family continuity).** Under hypotheses 1--5, $P_{\mathcal C}f$ is finite and continuous for every $f\in C(X,\mathbb R)$. It equals its upper-semicontinuous regularization. For a skeletal obstacle $g=\gamma\circ r$, it is exactly $\widetilde p\circ r$, where $p$ is the greatest vector of Proposition 1 for $\gamma$. For arbitrary $f$, if

$$\|g_j-f\|_\infty\leq\varepsilon_j\longrightarrow0,$$

then

$$\|P_{\mathcal C}f-\widetilde p_j\circ r_j\|_\infty\leq\varepsilon_j.$$

This is an assertion about the full class $\mathcal C$, not only its skeletal members.

**Proof.** Nonemptiness and finiteness follow from

$$\min_X f\leq P_{\mathcal C}f\leq f.$$

First take a skeletal obstacle $g=\gamma\circ r$. Put $q=\widetilde p\circ r$. Hypothesis 3 and Proposition 1 give $q\in\mathcal C$ and $q\leq g$, so $q\leq P_{\mathcal C}g$.

Let $h$ be **any** member of $\mathcal C$ with $h\leq g$. Suppose $h(x)>q(x)$ somewhere, and choose $0<\eta<h(x)-q(x)$. Set

$$W=\{z:h(z)>q(z)+\eta\}.$$

This open set is nonempty, and its closure is compact. Throughout $\overline W$, continuity gives $h\geq q+\eta$, hence $g-q\geq\eta$. Thus $\overline W$ is contained in the open set $\{q<g\}$, where $q$ is harmonic by Proposition 1 and hypothesis 4. This open set misses $D$, because $p_v=\gamma_v$ at boundary vertices.

We must also check that $W$ has nonempty boundary, including when $D=\varnothing$. The contact set $\{q=g\}$ is nonempty. If $D\ne\varnothing$, this follows from boundary contact. If $D=\varnothing$, Proposition 2 gives a constant $q=\min\gamma$, attained by $\gamma$ at some graph vertex. At any contact point, $h\leq g=q$, so the point is outside $\overline W$. Therefore $W$ is a proper nonempty open subset of connected $X$. If it had empty boundary, it would be both open and closed, contrary to connectivity. Moreover $h=q+\eta$ on $\partial_XW$, by continuity and the definition of $W$.

Harmonic comparison with $q+\eta$ therefore yields $h\leq q+\eta$ throughout $W$, contradicting its definition. Hence $h\leq q$ on $X$. Since this argument applies to every competitor, $P_{\mathcal C}g=q$.

Now note that the full-envelope operator has uniform stability. If $\|f-g\|_\infty\leq\varepsilon$ and $h\in\mathcal C$ satisfies $h\leq f$, then $h-\varepsilon\in\mathcal C$ satisfies $h-\varepsilon\leq g$. Taking the supremum gives $P_{\mathcal C}f\leq P_{\mathcal C}g+\varepsilon$. Interchanging $f,g$ gives

$$\|P_{\mathcal C}f-P_{\mathcal C}g\|_\infty\leq\varepsilon.$$

Apply this to the obstacles from hypothesis 2. Their exact full envelopes are the continuous functions $\widetilde p_j\circ r_j$ just proved above. They converge uniformly to $P_{\mathcal C}f$. A uniform limit of continuous functions is continuous on any topological space: given a point and a positive tolerance, one fixed approximant and its local continuity provide the required neighborhood. For a continuous function $u$, the neighborhood formula

$$u^*(x)=\inf_{N\ni x}\sup_Nu$$

equals $u(x)$. Thus regularization leaves $P_{\mathcal C}f$ unchanged. $\square$

## What cofinality was actually proved

The majorization step is essential. The fact that graph minorants are continuous, or that some sequence of them has a continuous limit, would not bound non-skeletal competitors. In the proof, every competitor $h\leq g_j$ is bounded by $q_j=P_{\mathcal C}g_j$. Moreover $q_j-\varepsilon_j$ is a **global** competitor below $f$, since

$$q_j-\varepsilon_j\leq g_j-\varepsilon_j\leq f.$$

For any arbitrary global competitor $h\leq f$, the translated function $h-\varepsilon_j$ lies below $g_j$, so

$$q_j-\varepsilon_j\leq P_{\mathcal C}f\leq q_j+\varepsilon_j.$$

These two inequalities close the full-family gap; no assumption that the selected sequence was exhaustive is used. The construction does not require maxima of arbitrary members of $\mathcal C$ to remain in $\mathcal C$.

If $D=\varnothing$, every skeletal envelope is the constant minimum of its obstacle by Proposition 2. Uniform stability then gives

$$P_{\mathcal C}f\equiv\min_Xf.$$

In that case every $h\in\mathcal C$ is constant: apply this formula to the obstacle $f=h$, for which $h$ is itself an admissible competitor. This is a consequence of all the skeleton hypotheses, not an independently proved Liouville theorem for general proper analytic spaces.

## The criterion does not imply a common competitor modulus

Take $X=[0,1]$, designate both endpoints as boundary, take ordinary affine harmonic functions locally, and let $\mathcal C$ be the class of finite continuous convex functions. The hypotheses hold, using interval subdivisions. Harmonic comparison is elementary: on each component interval, a convex function below an affine function at its endpoints remains below it throughout by the chord inequality. The functions

$$h_n(t)=\max\{0,1-nt\},\qquad n\geq1,$$

all lie below the continuous obstacle $1$. They have $h_n(0)=1$ and $h_n(1/n)=0$, so they do not share a modulus of continuity at $0$. Nevertheless the envelope over **all** finite continuous convex minorants of $1$ is the continuous constant $1$, since that constant is itself a competitor. Theorem 3 therefore uses a different mechanism from a common local modulus for the full family.

# 3. How to prove the obstacle-density hypothesis

For use in an application, hypothesis 2 can be split into separation and a mesh statement. This section supplies the elementary approximation argument instead of citing a density theorem without checking its hypotheses.

**Lemma 4 (lattice approximation).** Let $X$ be compact Hausdorff. Let $\mathcal A\subset C(X,\mathbb R)$ contain constants, be closed under real linear combinations, finite maxima and finite minima, and separate distinct points. Then every continuous function on $X$ is uniformly approximable by elements of $\mathcal A$.

**Proof.** Fix $f\in C(X,\mathbb R)$ and $\epsilon>0$. For each pair $x,y$, separation and affine rescaling give $a_{x,y}\in\mathcal A$ with $a_{x,y}(x)=f(x)$ and $a_{x,y}(y)=f(y)$; for $x=y$ use a constant. For a fixed $x$, the open sets

$$\{z:a_{x,y}(z)>f(z)-\epsilon\},\qquad y\in X,$$

cover $X$. Choose finitely many $y$ and let $b_x$ be the maximum of their functions. Then $b_x>f-\epsilon$ on $X$ and $b_x(x)=f(x)$. The open sets $\{z:b_x(z)<f(z)+\epsilon\}$, as $x$ varies, also cover $X$. Choose finitely many $x$ and let $a$ be the minimum of the corresponding $b_x$. It satisfies $f-\epsilon<a<f+\epsilon$ on $X$ and belongs to $\mathcal A$. $\square$

Suppose that continuous functions factoring through the finite skeleta form such a lattice, because a common refinement absorbs each finite collection of skeleta and their functions. Suppose also that any continuous function on one finite graph can be uniformly approximated by affine interpolation on allowable subdivisions. The latter holds when allowed subdivision points are dense on every edge: choose a sufficiently fine subdivision using uniform continuity on the finite graph. Lemma 4 and interpolation then prove hypothesis 2. A common refinement must be checked in the specific application; it is not supplied by compactness alone. Neither separation nor interpolation checks the semipositivity or global realization hypothesis 3.

# 4. Proper fibres: reduction of the whole class, not symmetrization

This is a separate exact transfer theorem. It makes clear both the strength of the proper-fibre approach and the missing analytic obligations.

Let $p:Y\to X$ be a continuous, closed, open surjection of Hausdorff spaces with nonempty compact fibres. Suppose it has a continuous section $s:X\to Y$. Let $\mathcal C_X\subset C(X,\mathbb R)$ and $\mathcal C_Y\subset C(Y,\mathbb R)$ be competitor classes. Assume:

* Pullback along $p$ sends $\mathcal C_X$ into $\mathcal C_Y$.
* Pullback along $s$ sends $\mathcal C_Y$ into $\mathcal C_X$.
* Every member of $\mathcal C_Y$ is constant on each fibre of $p$.

The last condition could be proved through stability of the exact class under analytic fibre restriction and a fibre Liouville theorem. Neither of those analytic assertions is assumed proved in this draft.

**Theorem 5 (arbitrary-obstacle fibre reduction).** For every finite continuous $f:Y\to\mathbb R$, the function

$$g(x)=\min_{y\in p^{-1}(x)}f(y)$$

is finite and continuous, and

$$P_{\mathcal C_Y}f=P_{\mathcal C_X}g\circ p.$$

This identity includes the empty-family case with supremum $-\infty$. In the finite nonempty case, continuity of the base envelope implies continuity of the full envelope upstairs. All competitors are used; no invariant subfamily is substituted.

**Proof.** Compactness of a fibre and continuity of $f$ give its finite attained minimum. For any $t\in\mathbb R$,

$$\{x:g(x)<t\}=p(\{y:f(y)<t\})$$

is open, since $p$ is open. Also

$$\{x:g(x)\leq t\}=p(\{y:f(y)\leq t\})$$

is closed, since $p$ is closed; attainment of the minimum justifies this equality. Thus $g$ is both upper and lower semicontinuous, hence continuous.

For any $h\in\mathcal C_Y$, put $a=h\circ s\in\mathcal C_X$. Fibre constancy implies $h=a\circ p$. Moreover $h\leq f$ if and only if $a\leq g$. Conversely, if $a\in\mathcal C_X$ and $a\leq g$, its pullback belongs to $\mathcal C_Y$ and lies below $f$. Hence the two admissible families are in exact bijection under pullback. Taking pointwise suprema proves the formula, including simultaneous emptiness. $\square$

For compact connected $X$ satisfying Theorem 3, and for the full pair of classes satisfying these fibre hypotheses, Theorems 3 and 5 give continuity on $Y$ for **all** finite continuous obstacles. This is a complete proof of that conditional transfer statement. Openness in Theorem 5 is not removable from the proof of upper semicontinuity of $g$ merely because the fibres are compact. Closedness alone supplies only lower semicontinuity.

# 5. Exact obligations for an analytic application

The following are genuine unchecked analytic gates, rather than claimed facts extracted from the supplied dossier.

## Rational curve domains

A prospective base class is a connected compact strict rational affinoid in $(\mathbb P^1_K)^{\mathrm{an}}$, over a complete algebraically closed nontrivially valued field $K$. The proposed boundary set is its relative affinoid boundary. Finite trees obtained by adding finitely many disc points to a boundary skeleton are the proposed graphs.

To turn Theorem 3 into a theorem for the original competitor union on this class, one must establish all of the following under the literal analytic definitions:

1. The indicated retractions are continuous, their boundary vertices are exactly appropriate relative-boundary points, and the density/refinement assertions of Section 3 hold. Type-1 endpoints, nondiscrete radii, and type-4 points cannot be omitted.

2. Every finite graph-affine function with nonnegative interior outgoing slopes lifts to a **global semipositive real-PL function** on the entire affinoid domain, with the required permitted vertices and coefficients. It is not enough to produce a continuous curvewise-subharmonic function, a local expression, or an approximant that misses the obstacle. This is the globalization/realization gate.

3. Every locally Fubini--Study competitor and every semipositive real-PL competitor satisfies the harmonic comparison used in hypothesis 5. The signs and weights of the slope operator must agree with the precise analytic convention. Interior branch attachments have to be included, while relative-boundary vertices must have exactly the asserted freedom. A comparison result for only one branch of the union would be insufficient.

4. Lifted graph-harmonic functions are harmonic on the required open inverse images, including discarded disc components and branch attachment points. Continuity of the retraction alone does not prove this.

If these gates are supplied, the full-family upper bound and the global minorants are then furnished by Theorem 3, rather than assumed. This draft has not independently completed gates 1--4 or obtained a primary text verifying their exact applicability. Consequently it does not assert even this rational-affinoid application as established P03.3 progress on a new analytic class.

## Scalar extensions

An analytic application must separately check the gates after scalar extension and verify how the skeletal data and **the exact competitor class** pull back. A useful conditional statement is the following: suppose $\mathcal G\subset C(X,\mathbb R)$ is a uniformly dense collection of skeletal obstacles. For a continuous scalar projection $\pi:X'\to X$, assume that every $g\in\mathcal G$ has a finite exact full envelope $q=P_{\mathcal C}g$ and the exact full envelope upstairs satisfies

$$P_{\mathcal C'}(g\circ\pi)=q\circ\pi,$$

with both classes invariant under adding constants. Then for every finite continuous $f$ on compact $X$,

$$P_{\mathcal C'}(f\circ\pi)=P_{\mathcal C}f\circ\pi.$$

Indeed, choose $g_j\in\mathcal G$ with $\|f-g_j\|_\infty\leq\varepsilon_j\to0$, and put $q_j=P_{\mathcal C}g_j$. The same approximation bound holds after composition with $\pi$, and uniform stability bounds both sides within $\varepsilon_j$ of $q_j\circ\pi$. The finite skeletal envelope identities ensure nonempty admissible families; translation supplies a minorant for each nearby obstacle as well. Let $j$ tend to infinity. This argument does not require an open scalar projection. Its skeletal pullback identity is nevertheless an additional full-family assertion that must be proved; it cannot be inferred from pullback stability alone. Nothing here proves identities between upper regularizations before continuity has been established.

## Higher dimensional products

A proposed higher dimensional range is a rational curve affinoid multiplied by a finite product of analytic projective lines. To apply Theorem 5 to the projection, one must prove:

* Restriction and pullback stability of the literal full locally-Fubini--Study/semipositive-real-PL union, including restrictions to fibres over completed residue fields.
* A Liouville theorem for both branches of that union on the proper fibres, after every necessary field extension, with connectedness and branch compatibility checked.
* Closedness, compact fibres, and **openness** of the analytic projection, together with an analytic section providing the class-preserving restriction in Theorem 5.
* The curve-base gates above for the continuous fibre-minimum obstacle, not merely for invariant or pulled-back original obstacles.

These checks have not been completed. Properness by itself does not prove the fibre Liouville statement for an arbitrary locally defined class. Nor does a global section by itself prove constancy on a fibre or openness at its other points.

## What remains for the literal original problem

Even completion of the proposed curve and product applications would give only a sufficient geometric sector. The original target additionally requires sharp hypotheses and necessity across the residual higher dimensional normal/geometrically unibranch range, with arbitrary finite continuous obstacles, scalar extension, branches, relative boundary, and global competitor issues. No necessity theorem or counterexample in that residual range is proved here. Positivity of an envelope would not replace the continuity argument, and continuity obtained here would not independently imply the requested classical or CLD-v2 positivity statements.

# 6. Reproducibility and evidence

The authoritative fresh input is preserved byte-for-byte as `input.json` and `input-original.json`; `task-original.json` and `assignment-original.txt` were written only because they were absent. The mathematical input's `[OCR control U+XXXX]` markers were not given a mathematical interpretation.

The exact-arithmetic program is `finite_graph_envelope.py`.

Its input is `finite-graph-input.json`. It writes `finite-graph-output.json`. Run

```text
python finite_graph_envelope.py \
  --input finite-graph-input.json \
  --output finite-graph-output.json
```

It enumerates Dirichlet contact sets and solves using rational Gaussian elimination. It checks feasibility, domination of all enumerated feasible contact solutions, contact/harmonic complementarity, and translation stability in the recorded examples. These are exhaustive contact-set computations for those supplied finite graphs only. They do not certify any analytic comparison or model-metric identification.

The exact computed greatest vertex vectors, in the input's vertex order, are:

* A three-vertex path with boundary at both ends and obstacle $(0,10,0)$: $(0,0,0)$.
* A four-vertex path with boundary at both ends and obstacle $(4,3,0,4)$: $(4,2,0,4)$.
* A rooted three-vertex path with obstacle $(2,0,2)$: $(2,0,0)$.
* A rooted four-vertex star with obstacle $(3,0,2,4)$: $(3,0,2,3)$.
* A four-vertex cycle with one boundary vertex and obstacle $(3,10,0,10)$: $(3,3/2,0,3/2)$.
* A connected four-vertex path with empty designated boundary and obstacle $(5,-2,7,1)$: $(-2,-2,-2,-2)$.
* A single vertex with empty designated boundary and obstacle $3/7$: $3/7$.
* A three-vertex graph with two parallel edges of lengths $1,2$ between the first two vertices, an edge of length $1$ to the third, both endpoints designated boundary, and obstacle $(4,10,0)$: $(4,12/5,0)$.

Public-source provenance is in `source-provenance.json`. Direct HTTP retrieval of arXiv and an author's public page failed through the unchanged existing proxy. Public GitHub discovery did not supply a primary mathematical text for the analytic gates. No retrieved primary theorem is used. Literal source extracts therefore have no content; `source-extracts/README.md` records that absence. Search snippets and the user dossier are not substituted for primary proofs.

The standalone TeX paper is `P03.3-paper.tex`. It contains this entire proof and scope statement; it is generated from this Markdown with `render-paper.sh`. Actual twice-run TeX commands and diagnostics are recorded by `build-paper.py` in `build-record.json` and separate log files. The rerun sequence is

```text
bash render-paper.sh
python build-paper.py
python verify-artifacts.py
```

`environment.json`, `commands.json`, `verification.json`, and `status.json` record execution details and limitations. No installation, environment-setting change, other model invocation, or supervised large computation was used. There is no resource-heavy calculation requiring a supervised compute facility. Successful compilation, hashes, and finite tests establish only the stated execution facts.


# All actual canonical notes

[
  {
    "id": "n1",
    "summary": "Finite metric-graph obstacle theorem: graph-affine subharmonic minorants have a greatest element, harmonic off contact and touching every designated boundary vertex. Eight exact-rational examples pass. This is a finite graph result, not an analytic P03.3 theorem.",
    "detailedSummary": "For a finite connected metric graph, an affine-on-edges obstacle, and any designated boundary subset $B$, the vectors $u\\leq g$ with nonnegative outgoing-slope sums outside $B$ have a greatest element $p$. Coordinatewise maximum closure and compact maximization prove existence; vertex perturbations prove boundary contact and contact/harmonic complementarity. Empty $B$ forces the constant minimum. A contact-set enumeration algorithm is proved exhaustive for this finite problem. Eight examples passed exact rational checks, involving 44 original systems and 44 translated systems. These checks establish no analytic identification or sharp classification.",
    "text": "This note supplies the finite graph result used in n2. It does not establish continuity on a new analytic domain.\n\nLet $\\Gamma$ be a nonempty finite connected metric graph, subdivided so that every edge joins distinct vertices. Parallel edges are allowed. Write $V$ for its vertices, $\\ell_e>0$ for its edge lengths, and $B\\subset V$ for a possibly empty designated boundary. Let $g$ be continuous and affine on each edge, with vertex values $g_v$.\n\nFor $u\\in\\mathbb R^V$, define\n\\[\nL_vu=\\sum_{e=vw}\\frac{u_w-u_v}{\\ell_e},\n\\qquad\n\\mathcal F_g=\\{u:u_v\\leq g_v\\text{ for all }v,\\ L_vu\\geq0\\text{ for }v\\notin B\\}.\n\\]\nEach parallel edge contributes separately. Write $\\widetilde u$ for affine interpolation on the edges.\n\nClaim: $\\mathcal F_g$ has a greatest element $p$. It satisfies $p_v=g_v$ at every $v\\in B$, and\n\\[\np_v<g_v\\Longrightarrow L_vp=0\\qquad(v\\notin B).\n\\]\nConsequently $\\widetilde p\\leq g$ and $\\widetilde p$ is graph-harmonic on $\\{\\widetilde p<g\\}$.\n\nProof. Put $m=\\min_Vg_v$. The constant vector $m$ is feasible. Feasible vectors are closed under coordinatewise maximum: if $z=\\max(u,w)$ and $z_v=u_v$, then $z_t\\geq u_t$ at every neighboring vertex, so $L_vz\\geq L_vu\\geq0$. The obstacle inequality is preserved as well.\n\nThe nonempty set $\\mathcal F_g\\cap\\prod_v[m,g_v]$ is compact. Choose $p$ maximizing $\\sum_vu_v$ on this set. For any feasible $u$, the vector $\\max(p,u)$ belongs to this compact set. Any coordinate with $u_v>p_v$ would increase its sum, contradicting maximality. Thus $u\\leq p$, proving greatestness for all feasible vectors.\n\nAt a boundary vertex, increasing $p_v$ toward $g_v$ only increases neighboring outgoing-slope sums; there is no constraint at that vertex. Hence $p_v=g_v$. If an interior vertex had both $p_v<g_v$ and $L_vp>0$, increasing just $p_v$ by a sufficiently small $\\delta>0$ would preserve its own inequality, since its slope sum decreases by $\\delta\\sum_{e\\ni v}\\ell_e^{-1}$. Neighboring sums increase. This contradicts greatestness. Affine interpolation preserves the obstacle inequality along each edge, and complementarity gives harmonicity off contact. The single-vertex case has zero slope sum and satisfies the same conclusions.\n\nIf $B=\\varnothing$, every feasible vector is constant. Indeed, $\\sum_vL_vu=0$ by cancellation along edges, so all the nonnegative sums vanish. At a maximal vertex all outgoing contributions are nonpositive and sum to zero; every neighbor therefore has the same value. Connectivity propagates equality. The greatest feasible vector is consequently $p\\equiv\\min_Vg_v$.\n\nAn exact algorithm follows. For nonempty $B$, enumerate subsets $A\\subset V$ containing $B$, and solve\n\\[\nu_v=g_v\\quad(v\\in A),\\qquad L_vu=0\\quad(v\\notin A).\n\\]\nEach Dirichlet system is nonsingular: its homogeneous solution vanishes on $A$, and the graph maximum and minimum arguments force it to vanish everywhere. Retain the solutions satisfying all feasibility inequalities. The true $p$ appears by taking $A=\\{v:p_v=g_v\\}$ and using complementarity. The retained vector dominating every retained solution is therefore $p$. There are at most $2^{|V\\setminus B|}$ systems. Rational inputs permit exact rational arithmetic. For empty $B$, the constant-minimum formula suffices; the program additionally enumerates nonempty contact sets.\n\nThe implementation is finite_graph_envelope.py, with input finite-graph-input.json and output finite-graph-output.json. Rerun with:\n\npython finite_graph_envelope.py --input finite-graph-input.json --output finite-graph-output.json\n\nIt uses Python fractions.Fraction and rational Gaussian elimination. It checks feasibility, domination of retained contact solutions, complementarity, expected values, and translation by $7/3$. Eight supplied graphs passed, with 44 contact systems before translation and another 44 after translation. The exact greatest vertex vectors were:\n\n- Two-boundary path, obstacle $(0,10,0)$: $(0,0,0)$.\n- Two-boundary path, obstacle $(4,3,0,4)$: $(4,2,0,4)$.\n- Rooted path, obstacle $(2,0,2)$: $(2,0,0)$.\n- Rooted star, obstacle $(3,0,2,4)$: $(3,0,2,3)$.\n- Four-cycle with one boundary vertex, obstacle $(3,10,0,10)$: $(3,3/2,0,3/2)$.\n- Empty-boundary connected path, obstacle $(5,-2,7,1)$: $(-2,-2,-2,-2)$.\n- Empty-boundary singleton, obstacle $3/7$: $3/7$.\n- Three vertices with parallel edges of lengths $1,2$ between the first two, a length-$1$ edge to the third, endpoint boundary, and obstacle $(4,10,0)$: $(4,12/5,0)$.\n\nThese are exhaustive contact-set computations for the supplied finite graphs only. The mathematical proof is the argument above; successful execution does not certify it or any analytic application.\n\nThe complete argument is in P03.3-argument.md. P03.3-paper.tex contains the standalone proof and was compiled twice successfully into the ten-page P03.3-paper.pdf, with no warnings in the final recorded passes. Rerun bash render-paper.sh, python build-paper.py, and python verify-artifacts.py. Actual commands and diagnostics are recorded in build-record.json and the separate build-pass log files. environment.json, commands.json, and verification.json record execution facts.\n\nThe original input bytes are preserved in input.json and input-original.json. task-original.json and assignment-original.txt preserve the corresponding supplied data. OCR control markers remain uninterpreted. source-provenance.json records failed direct public retrieval through the unchanged proxy and public GitHub discovery that yielded no checked primary mathematical text. No retrieved primary theorem, unpublished dossier claim, audit verdict, or hash is used as a proof input. source-extracts/README.md records the absence of literal primary extracts. No installation, environment-setting change, other model/worker invocation, or resource-heavy computation was used.\n\nArtifacts: /workspace/research/campaigns/round-36/P03.3-original-envelope-continuity/artifacts/codex-6VHeXx",
    "support": []
  },
  {
    "id": "n2",
    "summary": "A finite harmonic-skeleton criterion gives continuity for an entire competitor class through comparison and uniform obstacle stability, without a common competitor modulus. Global realization, harmonic lifting, comparison, and obstacle density are explicit hypotheses; their analytic application to the exact P03.3 union remains unverified.",
    "detailedSummary": "For compact connected Hausdorff $X$ with finite designated boundary $D$, suppose an entire continuous competitor class $\\mathcal C$ contains constants and globally lifted graph-subharmonic functions, is translation invariant, and satisfies harmonic comparison. Suppose skeletal obstacles are uniformly dense and graph-harmonic functions lift harmonically. The graph solution from n1 then dominates every competitor under a skeletal obstacle, giving exact full-family equality. The estimate $\\|P_{\\mathcal C}f-P_{\\mathcal C}g\\|_\\infty\\leq\\|f-g\\|_\\infty$ extends continuity to every finite continuous obstacle. An elementary lattice-density lemma is proved. This is a structural sufficient criterion, not a sharp classification; no new analytic domain is verified to satisfy every hypothesis.",
    "text": "The greatest-element and complementarity results used here are proved in n1. The remaining proof is supplied below. Application to the literal locally-Fubini–Study/semipositive-real-PL union is conditional.\n\nLet $X$ be a nonempty compact connected Hausdorff space, $D\\subset X$ a finite possibly empty designated boundary, and $\\mathcal C\\subset C(X,\\mathbb R)$ the entire competitor class. Specify a collection of continuous harmonic functions on open subsets of $X\\setminus D$, closed under restriction and addition of constants.\n\nAssume the following finite harmonic-skeleton structure:\n\n1. There are continuous retractions $r:X\\to\\Gamma$ onto embedded finite connected metric graphs. Each graph contains $D$ as its designated boundary vertices and admits the required subdivisions.\n2. Every continuous obstacle is uniformly approximable by $g=\\gamma\\circ r$, with $\\gamma$ affine on the edges of a finite subdivided skeleton. These approximating obstacles need not be competitors.\n3. Every graph-affine function $a$ satisfying $L_va\\geq0$ away from $D$ has a global lift $a\\circ r\\in\\mathcal C$. Constants belong to $\\mathcal C$, and $h+c\\in\\mathcal C$ for all $h\\in\\mathcal C$ and $c\\in\\mathbb R$.\n4. A graph-affine function harmonic on a graph-open set avoiding $D$ lifts harmonically to its inverse image. This includes discarded components and branch attachments.\n5. Every member $h\\in\\mathcal C$ satisfies harmonic comparison: if $W$ is open, $\\overline W\\subset X\\setminus D$, $\\partial_XW\\ne\\varnothing$, and $q$ is harmonic near $\\overline W$, then $h\\leq q$ on $\\partial_XW$ implies $h\\leq q$ on $W$.\n\nThese hypotheses concern skeleton geometry, global realization, and individual competitors. They do not assume continuity of the desired envelope or exhaustion by a selected subfamily. Hypothesis 3 is a substantive globalization requirement, and hypothesis 5 concerns every member of the exact class.\n\nDefine\n\\[\nP_{\\mathcal C}f(x)=\\sup\\{h(x):h\\in\\mathcal C,\\ h\\leq f\\text{ on }X\\}.\n\\]\nUnder these hypotheses, $P_{\\mathcal C}f$ is finite and continuous for every finite continuous $f$, hence equals its upper-semicontinuous regularization.\n\nProof. Constants give $\\min_Xf\\leq P_{\\mathcal C}f\\leq f$, establishing finiteness and nonemptiness. First let $g=\\gamma\\circ r$ be skeletal. Let $p$ be the greatest graph vector from n1 and put $q=\\widetilde p\\circ r$. Global realization gives $q\\in\\mathcal C$ and $q\\leq g$, so $q\\leq P_{\\mathcal C}g$.\n\nTake any $h\\in\\mathcal C$ with $h\\leq g$. If $h(x)>q(x)$, choose $0<\\eta<h(x)-q(x)$ and set\n\\[\nW=\\{z:h(z)>q(z)+\\eta\\}.\n\\]\nIts closure is compact. On that closure, continuity gives $h\\geq q+\\eta$, hence $g-q\\geq\\eta$. Thus $\\overline W$ lies in the open set $\\{q<g\\}$, where complementarity from n1 and harmonic lifting make $q$ harmonic. This open set avoids $D$, because the graph solution touches the obstacle at boundary vertices.\n\nThe contact set $\\{q=g\\}$ is nonempty. For nonempty $D$ this follows from boundary contact. For empty $D$, n1 gives the constant graph minimum, attained at a vertex. At any contact point, $h\\leq q$, so the point lies outside $\\overline W$. Therefore $W$ is a nonempty proper open subset of connected $X$. Its boundary is nonempty: otherwise it would be clopen. Continuity gives $h=q+\\eta$ on that boundary. Comparison with $q+\\eta$ now contradicts the definition of $W$. Consequently every competitor satisfies $h\\leq q$, proving the exact full-family identity\n\\[\nP_{\\mathcal C}g=q.\n\\]\n\nNext, if $\\|f-g\\|_\\infty\\leq\\varepsilon$, any competitor $h\\leq f$ yields $h-\\varepsilon\\in\\mathcal C$ below $g$. Taking suprema and interchanging the obstacles proves\n\\[\n\\|P_{\\mathcal C}f-P_{\\mathcal C}g\\|_\\infty\\leq\\varepsilon.\n\\]\nChoose skeletal $g_j$ with $\\|g_j-f\\|_\\infty\\leq\\varepsilon_j\\to0$. Their exact full envelopes $q_j$ are continuous, and the preceding estimate gives uniform convergence $q_j\\to P_{\\mathcal C}f$. A uniform limit of continuous functions is continuous. The neighborhood definition of upper regularization therefore leaves this envelope unchanged.\n\nThe cofinality mechanism is explicit. Each $q_j-\\varepsilon_j$ is a global competitor below $f$, because $q_j\\leq g_j$. For every arbitrary competitor $h\\leq f$, the translated competitor $h-\\varepsilon_j$ lies below $g_j$ and is bounded by its exact full envelope $q_j$. Hence\n\\[\nq_j-\\varepsilon_j\\leq P_{\\mathcal C}f\\leq q_j+\\varepsilon_j.\n\\]\nThe upper inequality controls all competitors, while the lower inequality supplies actual global minorants. Exhaustiveness of the selected sequence is proved through comparison rather than assumed. Closure of arbitrary maxima in $\\mathcal C$ is unnecessary.\n\nWhen $D=\\varnothing$, n1 gives $P_{\\mathcal C}g=\\min_Xg$ for every skeletal obstacle. Uniform stability gives $P_{\\mathcal C}f\\equiv\\min_Xf$. Taking $f=h\\in\\mathcal C$ shows that every competitor is constant. This conclusion depends on all the stated hypotheses; it is not a verified Liouville theorem for arbitrary proper analytic spaces.\n\nThe criterion does not require a common competitor modulus. On $X=[0,1]$ with both endpoints designated boundary, use ordinary affine harmonic functions and the entire class of finite continuous convex functions. Interval subdivisions provide the skeletons; affine interpolation gives density; convexity gives comparison on component intervals. The functions\n\\[\nh_n(t)=\\max\\{0,1-nt\\}\n\\]\nare convex minorants of the obstacle $1$, with $h_n(0)=1$ and $h_n(1/n)=0$. They have no common modulus at $0$, while the full envelope is the continuous constant $1$.\n\nHere is a self-contained obstacle-density lemma. If a collection $\\mathcal A\\subset C(X,\\mathbb R)$ contains constants, is closed under real linear combinations and finite maxima/minima, and separates points, it is uniformly dense on compact Hausdorff $X$. Given continuous $f$ and $\\epsilon>0$, separation and affine rescaling provide, for each pair $x,y$, a function $a_{x,y}$ matching $f$ at both points; for $x=y$, use a constant. For fixed $x$, the open sets where $a_{x,y}>f-\\epsilon$ cover $X$. A finite subcover gives a maximum $b_x$ with $b_x>f-\\epsilon$ everywhere and $b_x(x)=f(x)$. The open sets where $b_x<f+\\epsilon$ also cover $X$. Taking the minimum of finitely many such $b_x$ gives an element of $\\mathcal A$ strictly between $f-\\epsilon$ and $f+\\epsilon$.\n\nThus hypothesis 2 follows if continuous skeletal functions form such a separating lattice under common refinements and if allowable subdivision points are dense on each edge. Uniform continuity on each finite graph then gives affine-interpolation approximation. Common refinement, separation, and permitted subdivisions must be checked in an application. This argument supplies neither semipositivity nor global real-PL realization.\n\nThe complete proof and its analytic limitations are in P03.3-argument.md and P03.3-paper.tex. Rerun the finite evidence with python finite_graph_envelope.py --input finite-graph-input.json --output finite-graph-output.json. Render and build with bash render-paper.sh and python build-paper.py. Execution checks do not certify the mathematical criterion or its analytic applications.\n\nArtifacts: /workspace/research/campaigns/round-36/P03.3-original-envelope-continuity/artifacts/codex-6VHeXx",
    "support": [
      "n1"
    ]
  },
  {
    "id": "n3",
    "summary": "Exact full-family proper-fibre reduction under an open closed projection, compact fibres, a class-preserving section, and fibrewise-constant competitors. Analytic realization, scalar compatibility, branch/boundary checks, and sharp necessity remain unresolved. P03.3 is not solved.",
    "detailedSummary": "For a continuous closed open surjection $p:Y\\to X$ with nonempty compact fibres, the obstacle $g(x)=\\min_{p^{-1}(x)}f$ is continuous. If exact competitor classes pull back along the projection and its section, and upstairs competitors are fibrewise constant, the admissible families are in bijection and $P_{\\mathcal C_Y}f=P_{\\mathcal C_X}g\\circ p$. Together with n2 this conditionally transfers all-obstacle continuity. Uniform stability also transfers separately proved skeletal scalar identities to arbitrary continuous pulled-back obstacles. No proposed rational-affinoid or proper-factor application is verified, and no sharp geometric hypotheses or necessity theorem are supplied.",
    "text": "The literal sharp P03.3 classification is not proved. Notes n1 and n2 provide an independent finite graph theorem and a conditional full-family continuity mechanism. This note proves a proper-fibre reduction and records the remaining analytic obligations. The supplied unpublished claims and audit verdicts are not used as proofs. No classical-psh or CLD-v2 conclusion is claimed.\n\nLet $p:Y\\to X$ be a continuous, closed, open surjection of Hausdorff spaces with nonempty compact fibres, and let $s:X\\to Y$ be a continuous section. Let $\\mathcal C_X\\subset C(X,\\mathbb R)$ and $\\mathcal C_Y\\subset C(Y,\\mathbb R)$ be the entire competitor classes. Assume pullback along $p$ sends $\\mathcal C_X$ into $\\mathcal C_Y$, pullback along $s$ sends $\\mathcal C_Y$ into $\\mathcal C_X$, and every upstairs competitor is constant on each fibre.\n\nFor every finite continuous obstacle $f:Y\\to\\mathbb R$, define\n\\[\ng(x)=\\min_{y\\in p^{-1}(x)}f(y).\n\\]\nThe minimum is finite and attained by compactness. For each real $t$,\n\\[\n\\{g<t\\}=p(\\{f<t\\}),\\qquad \\{g\\leq t\\}=p(\\{f\\leq t\\}).\n\\]\nThe first set is open because $p$ is open. The second is closed because $p$ is closed; attainment justifies the second equality. Hence $g$ is continuous.\n\nFor $h\\in\\mathcal C_Y$, put $a=h\\circ s\\in\\mathcal C_X$. Fibre constancy gives $h=a\\circ p$, and $h\\leq f$ is equivalent to $a\\leq g$. Conversely, any downstairs competitor $a\\leq g$ pulls back to an upstairs competitor below $f$. The admissible families are therefore in exact bijection, proving\n\\[\nP_{\\mathcal C_Y}f=P_{\\mathcal C_X}g\\circ p.\n\\]\nThis includes simultaneous emptiness with supremum $-\\infty$. When n2 applies to the base and these fibre hypotheses hold for the full classes, the upstairs envelope is continuous for every finite continuous obstacle. No invariant subfamily has been substituted. Compact fibres and closedness alone provide only lower semicontinuity of the fibre minimum; openness supplies the upper semicontinuity used here.\n\nThere is also a conditional scalar transfer. Suppose $\\mathcal G\\subset C(X,\\mathbb R)$ is a uniformly dense collection of skeletal obstacles, both competitor classes are translation invariant, and a continuous projection $\\pi:X'\\to X$ satisfies, for every $g\\in\\mathcal G$ with finite exact envelope $q=P_{\\mathcal C}g$,\n\\[\nP_{\\mathcal C'}(g\\circ\\pi)=q\\circ\\pi.\n\\]\nThen for every finite continuous $f$ on compact $X$,\n\\[\nP_{\\mathcal C'}(f\\circ\\pi)=P_{\\mathcal C}f\\circ\\pi.\n\\]\nIndeed, choose $g_j\\in\\mathcal G$ with $\\|f-g_j\\|_\\infty\\leq\\varepsilon_j\\to0$ and put $q_j=P_{\\mathcal C}g_j$. The same obstacle bound holds after pullback. Uniform stability from n2 bounds each side within $\\varepsilon_j$ of $q_j\\circ\\pi$. The finite skeletal identities ensure nonempty admissible families, and translation supplies minorants for nearby obstacles. Letting $j$ tend to infinity proves equality. This uses no openness of the scalar projection, but the skeletal full-family identity remains a separate hypothesis. Pullback stability alone does not prove it, and no upper-regularization identity is inferred before continuity is established.\n\nThe prospective curve-base application is a connected compact strict rational affinoid in $(\\mathbb P^1_K)^{\\mathrm{an}}$ over a complete algebraically closed nontrivially valued field. Finite trees extending a boundary skeleton are proposed presentations. The following gates have not been independently completed:\n\n- Establish continuous retractions, common refinements, separation and obstacle density, with the correct relative-boundary vertices and treatment of type-1 endpoints, nondiscrete radii and type-4 points.\n- Globally realize every required graph-affine function with nonnegative interior outgoing slopes as a semipositive real-PL function on the whole affinoid, with legal vertices and coefficients. A local expression or continuous curvewise-subharmonic function is insufficient.\n- Prove harmonic comparison for every locally Fubini–Study competitor and every semipositive real-PL competitor, with the correct slope signs and weights, branch attachments and relative-boundary freedom.\n- Prove harmonic lifting across discarded components and attachment points. Continuity of a retraction does not establish this.\n\nIf verified, these gates would let n2 prove the global minorants and upper bound for the full family. They are not assumed verified here, so even this rational-affinoid application is not asserted as an established new analytic continuity theorem.\n\nA proposed higher dimensional application is a rational curve affinoid multiplied by a finite product of analytic projective lines. Its projection would need all hypotheses of the fibre reduction. In particular, one must verify restriction and pullback stability of the literal union, including fibres over completed residue fields; a Liouville theorem for both competitor branches on the proper fibres after relevant field extensions; connectedness and branch compatibility; projection openness and closedness with compact fibres; and an analytic section preserving the class. Properness alone does not establish fibre constancy for an arbitrary locally defined class, and a section alone does not establish openness at other fibre points. These checks remain gaps.\n\nThe curve and product applications would still be sufficient sectors rather than the requested classification. The original problem requires actual sharp hypotheses and necessity in the residual higher dimensional normal or geometrically unibranch range, with every finite continuous obstacle, scalar extensions, analytic-curve pullbacks, branches, relative boundary and global competitors. No such necessity theorem or residual counterexample is proved. Positivity does not replace continuity, and the continuity criterion does not independently establish classical or CLD-v2 positivity.\n\nP03.3-argument.md contains the complete argument and exact scope. P03.3-paper.tex is the standalone paper; its ten-page PDF built twice successfully without warnings in the final recorded passes. source-provenance.json records actual public-source discovery and retrieval failures, with no primary theorem applications. status.json has exactly id,status,exact_result,proof_file,concrete_gaps and marks the result partial. The original input artifacts are preserved. Rerun bash render-paper.sh, python build-paper.py, and python verify-artifacts.py. Eight exact graph examples passed; compilation and finite checks do not establish the unverified analytic gates. No heavy compute, installations, external messages, or other model/worker invocations were used. The literal original target remains unsolved.\n\nArtifacts: /workspace/research/campaigns/round-36/P03.3-original-envelope-continuity/artifacts/codex-6VHeXx",
    "support": [
      "n2"
    ]
  }
]

# Actual source provenance: no primary analytic application claimed

{
  "id": "P03.3",
  "primary_mathematical_sources_consulted": [],
  "primary_theorems_applied": [],
  "source_dependent_claims_used_as_proofs": [],
  "independent_proofs": [
    {"result": "Propositions 1 and 2", "method": "Finite-dimensional compact maximization, coordinatewise maximum closure, vertex perturbation, and cancellation of outgoing slopes."},
    {"result": "Theorem 3", "method": "Comparison on a compact positive superlevel set away from the contact set, then uniform stability of the entire envelope under obstacle perturbation."},
    {"result": "Lemma 4", "method": "Elementary finite-cover lattice approximation; proof reproduced in full."},
    {"result": "Theorem 5", "method": "Open/closed fibre-minimum formulas and exact competitor bijection using a section and fibrewise constancy."},
    {"result": "Conditional scalar transfer", "method": "Uniform obstacle stability after a separately assumed exact skeletal pullback identity."}
  ],
  "actual_retrieval_attempts": [
    {
      "method": "curl in unchanged environment",
      "url": "https://export.arxiv.org/api/query?search_query=all:plurisubharmonic%20AND%20au:Gubler&start=0&max_results=10",
      "command": "curl -L --fail --max-time 25 -o public-arxiv-search.xml 'https://export.arxiv.org/api/query?search_query=all:plurisubharmonic%20AND%20au:Gubler&start=0&max_results=10'",
      "exit_code": 7,
      "diagnostic": "Failed to connect to proxy port 8080; could not connect to server.",
      "retrieved_primary_text": false
    },
    {
      "method": "curl in unchanged environment",
      "url": "https://www.mathematik.uni-regensburg.de/gubler/",
      "command": "curl -L --fail --max-time 25 -o public-gr-home.html 'https://www.mathematik.uni-regensburg.de/gubler/'",
      "exit_code": 7,
      "diagnostic": "Failed to connect to proxy port 8080; could not connect to server.",
      "retrieved_primary_text": false
    },
    {
      "method": "native public GitHub search and repository search",
      "queries": ["plurisubharmonic Gubler", "Berkovich maximum principle", "semipositive piecewise linear", "2503.05513", "semipositive Rabinoff", "Gubler Fubini", "Rabinoff", "non-archimedean semipositive", "Berkovich potential theory", "Gubler"],
      "result": "Discovery found bibliographic RSS metadata for Gubler--Rabinoff, arXiv:2503.05513, but no retrieved primary mathematical text. Other search matches were not accepted as mathematical sources.",
      "retrieved_primary_text": false,
      "exact_applications": []
    }
  ],
  "unverified_possible_foundation": {
    "title": "On semipositive piecewise linear functions in non-archimedean analytic geometry",
    "authors": ["Walter Gubler", "Joseph Rabinoff"],
    "public_url": "https://arxiv.org/abs/2503.05513",
    "discovery_only": true,
    "statement_checked": false,
    "used": false,
    "limitation": "Only bibliographic search metadata was seen. Neither the exact definitions nor a relevant theorem and its hypotheses were checked, so no application is asserted."
  },
  "literal_primary_extracts_directory": "source-extracts",
  "literal_primary_extracts_present": false,
  "input_handling": "Original input bytes preserved. User dossier supplies the target and scope, not granted mathematical lemmas. OCR control markers are uninterpreted.",
  "analytic_application_status": "Unproved; explicit obligations in Section 5 of the argument and status.json."
}
