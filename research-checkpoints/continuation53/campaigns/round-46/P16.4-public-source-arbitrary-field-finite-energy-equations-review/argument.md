# Exact scoped status

{
  "id": "P16.4",
  "status": "partial",
  "exact_result": "Unverified partial proof: over algebraically closed complete nontrivially real-valued non-Archimedean K of residue characteristic zero, X=P^1_K and L=O(d), d>=1, the genuine finite-energy operator is constructed for all-support positive Radon measures of raw mass d and dual energy J=I/2<infinity. Existence and uniqueness modulo constants, decreasing continuity, reference independence, energy differentiation and comparison are proved by the rooted Green kernel. General smooth projective varieties and arbitrary non-algebraically-closed fields remain unresolved here.",
  "proof_file": "P16.4-argument.md",
  "concrete_gaps": [
    "Identify actual unbounded psh potentials and approximation-independent full-mass genuine mixed MA measures in the general nondiscrete field setting.",
    "Supply normalized potential compactness and extraction of finite-energy actual maximizing metrics, beyond weak/quasi-metric compactness of measures.",
    "Supply envelope/obstacle regularity or a proved alternative, and link available synthetic orthogonality to actual unbounded potentials.",
    "Prove unbounded energy differentiation and obstacle variations against all continuous tests for that actual operator.",
    "Prove finite-energy comparison/domination or equivalent injectivity estimates in the general field setting.",
    "Prove any field-extension/descent steps preserving the polarization, raw mass, psh, energy, derivatives and comparison; none are asserted here."
  ]
}


# Entire final proof

---
title: "P16.4: an all-support projective-line finite-energy theorem and the remaining arbitrary-field problem"
author: "Unverified research draft"
date: "4 October 2026"
geometry: "margin=1in"
fontsize: "11pt"
header-includes:
  - '\usepackage{amsmath,amssymb}'
---

# Result and scope

The original P16.4 is **not solved** here. A definition of $\mathcal E^1$, a completion of a space of measures, and differentiation of continuous metric volumes do not identify a genuine Monge--Ampere operator on unbounded potentials. The verified source statements below do not supply that identification over arbitrary complete valued fields in general dimension.

We prove a partial theorem on the entire Berkovich projective line, with arbitrary measure support. Its potentials can be unbounded, its operator agrees with the usual continuous Monge--Ampere measure, and its measure condition is exactly the dual finite-energy condition. This is a reconstruction of classical curve potential theory in a particularly explicit sector, not a claimed new higher-dimensional theorem. All arguments needed to identify its energy and operator are given below.

**Retained hypotheses for the partial theorem.** Let $K$ be algebraically closed and complete for a **nontrivial real-valued non-Archimedean absolute value**, with residue characteristic zero. Let $X=\mathbf P^1_K$, let $d\geq1$ be an integer, and let $L=\mathcal O(d)$. Thus $X$ is smooth, geometrically connected, algebraic, proper and projective, and $L$ is ample. The additional restriction $X=\mathbf P^1$ and the additional algebraic-closedness assumption are genuine restrictions. No discreteness, spherical completeness, countability, or function-field algebraizability is assumed. Residue characteristic zero is retained to keep this result on the assigned valuation axis, although the tree proof does not use that characteristic restriction. No descent to a non-algebraically-closed ground field is claimed.

Write $T=X^{\mathrm{an}}$ and let $o$ be the Gauss point in the coordinate $Z$. Fix the standard continuous semipositive metric $h_0$ on $L$, in additive weight notation. Its raw curvature measure is
$$
\theta=d\delta_o,\qquad V=(L^1)=d.
$$
The metric with relative weight $u$ is $h_0+u$; in norm notation this multiplies the reference norm by $e^{-u}$. We use **raw energy**, so $E(u+c)=E(u)+dc$. We exclude the identically $-\infty$ weight from $\operatorname{PSH}(L)$.

**Theorem 1 (partial all-support finite-energy equation).** Under these hypotheses there is a genuine operator
$$
\operatorname{MA}:\mathcal E^1(L)\longrightarrow
\{\mu\text{ positive Radon on }T:\mu(T)=d\}
$$
extending the continuous semipositive Monge--Ampere operator, continuous along decreasing nets of psh weights. For a positive Radon measure of **raw mass $d$**, define
$$
J_{h_0}(\mu)=\sup_{v\in C(T)\cap\operatorname{PSH}(L)}
\left(E(v)-\int_T v\,d\mu\right).
$$
Here psh weights are relative to $h_0$, and
$$
E(v)=\frac12\left(\int_T v\,\operatorname{MA}(v)+d v(o)\right)
$$
for continuous weights. Define the extended energy by the infimum of $E(v)$ over continuous psh majorants $v\geq u$, and define $\mathcal E^1=\{u:E(u)>-\infty\}$.

For every such $\mu$ with $J_{h_0}(\mu)<\infty$ there exists $u\in\mathcal E^1(L)$ with $\operatorname{MA}(u)=\mu$, unique modulo additive constants. There is **no support restriction**. In fact the operator gives a bijection $\mathcal E^1/\mathbf R\simeq\{\mu:\mu(T)=d,J_{h_0}(\mu)<\infty\}$, and a homeomorphism for the strong topologies (weak topology refined by convergence of energy). It has a comparison principle, and energy differentiates along affine segments in $\mathcal E^1$. Its definition and the finiteness conditions do not depend on the continuous semipositive reference metric.

# Exact source versions and permitted background

Only the ten supplied caches and fresh work were read. Hashes, literal extracts, their supplied-text line locations and PDF page locations are retained in `source-extracts/source-provenance.json`. Literal extracts preserve original OCR defects; selected original PDF pages were rendered and inspected to resolve signs and continuity hypotheses. None of these verification operations certifies a proof.

1. **Boucksom--Favre--Jonsson, 1201.0187v2, _Singular semipositive metrics in non-Archimedean geometry_.** The standing assumptions are a complete discrete valuation field of residue characteristic zero and a smooth projective analytification. Its Theorems A and B give compactness and decreasing model regularization in that domain. They are not arbitrary-field statements in this saved version.

2. **Boucksom--Favre--Jonsson, 1201.0188v1, _Solution to a non-Archimedean Monge--Ampere equation_.** Theorem A in the actual saved v1 requires a complete discrete valuation field of residue characteristic zero, smooth projective $X$ defined over a one-variable function field admitting $K$ as a completion, ample $L$, and a positive Radon measure of raw mass $(L^n)$ **supported on an SNC dual complex**. The introduction separately records curve potential theory over any complete nontrivially valued field. Later theorem statements removing algebraizability must not be silently attributed to this v1. We make no higher-dimensional application of it.

3. **Boucksom--Eriksson, 1805.01016v3, _Spaces of norms, determinant of cohomology and Fekete points in non-Archimedean geometry_.** This is the spaces-of-norms paper. Theorem A identifies continuous psh relative volume and energy over any complete valued field for a geometrically reduced projective scheme and an ample line bundle. Theorem 7.8 identifies continuous psh metrics with uniform limits of nef model metrics when the valuation is nontrivial and $L$ is ample. Definition 7.2, Lemma 7.4 and Corollary 7.6 give the decreasing-net definition and closure properties. Theorem 8.4 extends the mixed operator to **continuous psh-regularizable metrics**, continuously for the uniform topology; Theorem 7.14 makes continuous psh metrics in our ample setting psh-regularizable. Proposition 8.3 supplies mass and integration by parts, which extend by uniform approximation. Definition 9.13 and Proposition 9.14 give continuous energy and its cocycle rule. Every application below has $K$ complete, $X=\mathbf P^1$ smooth projective/geometrically reduced, and $L=\mathcal O(d)$ ample; nontriviality is imposed where 7.8 needs it.

4. **Boucksom--Jonsson, 1801.08229v4, _Global pluripotential theory over a trivially valued field_.** Theorem A gives the finite-energy operator and an embedding with dense image; surjectivity holds for smooth $X$ when the characteristic is zero or the dimension is at most two. The ground field in this formulation is algebraically closed and **trivially valued**. It cannot be applied to our nontrivially valued field by changing that standing assumption.

5. **Boucksom--Jonsson, 2307.01697v1, _Measures of finite energy in pluripotential theory: a synthetic approach_.** Theorem A and Theorems 2.23--2.24 give density of test Monge--Ampere measures and a complete Dirichlet quasi-metric on finite-energy **measures**, under orthogonality. Example 2.20 states orthogonality for the projective Berkovich formalism over a non-Archimedean field, using continuous volume results and a uniform differentiability estimate. Remark 2.14 expressly leaves investigation of psh potentials aside. The source does not identify each element of the measure completion with an actual unbounded psh potential. Orthogonality in this formalism must not be confused with continuity of all psh envelopes. No cohomology-isomorphism assertion over an arbitrary field is needed here.

6. **Pille--Schneider, 2209.04879v2, _Global pluripotential theory on hybrid spaces_.** Theorem 4.3 states the continuous-metric extension over complete valued fields. Remark 4.4 says (with typography normalized): "While the class $E^1(X,L)$ of finite-energy psh metrics on $L$ is defined over any non-archimedean field $K$, it is unclear in general how to extend the Monge-Ampere operator on the latter." It then records the discrete characteristic-zero and trivial endpoints. The BFJ standing assumption is checked separately as **residue** characteristic zero; the abbreviated phrase in this remark does not license mixed-characteristic applications.

7. **Gubler--Rabinoff, 2506.13548v2, 17 September 2025, _Classically psh and pluriharmonic functions on Berkovich spaces_.** The field is arbitrary complete non-Archimedean, possibly trivially valued. It constructs classically psh functions and maximum principles. The introduction explicitly excludes Monge--Ampere construction from its subject. Appendix A describes the disk tree and its weak topology. This is the tree background used below; coordinates $Z$ and $1/Z$, with their overlap identified, give the projective-line tree. The two closed coordinate disks do not intersect only in the Gauss point.

8. **Thuillier, thesis tel-00010990v1.** Chapter 2 assumes a complete nontrivially valued field, not a discrete valuation. The curve is smooth and strictly analytic; Section 3.5 further assumes connected and proper. These conditions hold for our $T$. Theorem 3.3.13 solves the mass-zero Laplace equation for currents; Lemma 3.3.12 identifies the kernel with harmonic functions; Theorem 3.4.19 regularizes subharmonic line-bundle metrics; Proposition 3.5.7 equates Green-potential integrability and Hilbert finite energy. These are classical background compatible with the explicit proof below. Original PDF page 117 (printed 103) confirms the term $\mu-\mu(T)\delta_x$, including raw mass. A displayed curvature sign on printed page 97 is inconsistent with its local weight convention; our convention is fixed independently by integration by parts and $dd^c(-k_z)=\delta_z-\delta_o$. We do not import an OCR sign or an unproved model-descent identification.

9. **Berkovich, _Etale cohomology for non-Archimedean analytic spaces_, PMIHES 78 (1993).** This supplies general analytic foundations, not a finite-energy equation theorem. No theorem from it is an indispensable new application below.

10. **Chambert-Loir--Ducros, 1204.6277v2, July 2025, _Formes differentielles reelles et courants sur les espaces de Berkovich_.** The expanded v2 has transfinite psh definitions in Section 8.1. Lemma 8.5.5 explicitly requires a **continuous** psh multiplier, confirmed on original PDF page 207; Proposition 8.7.2 requires continuous functions and local uniform convergence. The shorthand in 8.7.1 refers back to these product hypotheses. The audited statements do not supply the global unbounded $\mathcal E^1$ operator or an all-support equation. Section numbers from the earlier v1 cannot be transferred to this v2.

The permitted background in the proof is the elementary Berkovich tree structure and the continuous-metric theory just specified. All new passages to unbounded weights and all energy and equation identifications in this sector are proved next.

# The rooted kernel and finite trees

The tree $T$ has unique paths. On its nonrigid part these have their usual logarithmic length; paths ending at a rigid point have infinite length. For $x,y\in T$ let $x\wedge_o y$ be the last point common to their paths from $o$, and put
$$
k(x,y)=\operatorname{length}([o,x]\cap[o,y])\in[0,+\infty].
$$
In particular $k(o,y)=0$. All nonrigid points have finite depth $\ell(x)=k(x,x)$; type IV endpoints have positive limiting disk radius, since $K$ is complete. No spherical completeness is needed.

Let $F$ range over finite rooted subtrees whose vertices are type II points and which contain $o$. The order is inclusion. Type II points are dense along every finite nondegenerate path because the nonzero divisible group $\log|K^\times|$ is dense in $\mathbf R$. Let $r_F:T\to F$ be nearest rooted-path retraction and set
$$
k_F(x,y)=k(r_Fx,r_Fy).
$$
These kernels are bounded and continuous on $T\times T$, increase with $F$, and have supremum $k$. Indeed $k_F$ counts the common path inside $F$; along every common path its finite segments are exhausted by type II cutoffs. Continuity follows from the disk weak topology: a finite-path retraction is constant on each attached open branch and continuous along its finitely many retained edges.

Continuous functions factoring through finite-tree retractions form an algebra, contain constants, and separate points. For distinct points a type II cutoff along a distinguishing path separates their projections. Stone--Weierstrass therefore gives their uniform density in $C(T)$. If $g=g\circ r_F$ and $G\supset F$, then $g\circ r_G=g$. Approximation by such $g$ proves $f\circ r_G\to f$ uniformly for every $f\in C(T)$, and hence $(r_F)_*\mu\to\mu$ weakly for any Radon measure. Piecewise affine functions with type II knots are likewise uniformly dense: approximate a continuous function on a finite compact graph by linear interpolation and move knots to nearby type II points.

We will use the following Radon integration fact, including for nonmetrizable $T$. If bounded continuous functions $a_i$ on a compact Hausdorff space form an increasing directed family with supremum $a$, then
$$
\int a\,d\rho=\sup_i\int a_i\,d\rho
$$
for a positive Radon measure, also when the supremum is unbounded and nonnegative. To prove this, first truncate the desired lower bound and approximate a lower semicontinuous function from below in integral using compact subsets of its superlevel sets. On each such compact subset the inequalities $a_i>t$ give an open cover. A finite subcover and directedness provide one index meeting all finitely many inequalities. The layer-cake formula, followed by finer level partitions and truncation, proves the claim. The same argument on $T\times T$ uses its Radon product measure. In particular the kernel integrals below can equivalently be defined by their finite-tree suprema; this avoids assuming a dominated-convergence theorem for arbitrary nets or a globally sigma-finite length measure on an uncountably branching tree. Fubini for these nonnegative lower semicontinuous kernels follows by this approximation: continuous functions on a compact product are uniformly approximable by finite sums of products of continuous functions.

For a positive finite Radon measure $\mu$ define
$$
p_\mu(x)=\int_T k(x,y)\,d\mu(y),\qquad
I(\mu)=\int_{T\times T}k(x,y)\,d\mu(x)d\mu(y).
$$
Thus $p_\mu=\sup_F p_{\mu,F}$, where $p_{\mu,F}(x)=\int k_F(x,y)d\mu(y)=p_\mu(r_Fx)$. Also $I(\mu)=\sup_F I_F(\mu)$ with $I_F(\mu)=\iint k_F\,d\mu d\mu$. The function $p_\mu$ is lower semicontinuous, finite at every nonrigid point, bounded there by $\mu(T)\ell(x)$, and zero at $o$.

# Agreement with the genuine continuous operator

Here $dd^c$ is the signed graph Laplacian for which
$$
\int f\,dd^c g=-D(f,g),\qquad
D(f,g)=\sum_{e}\int_e f'g'\,dt.
$$
Finite-tree functions are extended constantly on attached branches. Endpoint contributions are the sum of outward slopes. Consequently, for a type II point $z$, $k_z=k(\cdot,z)$ is a continuous finite-tree piecewise affine function and
$$
dd^c k_z=\delta_o-\delta_z.
$$
This sign gives nonnegative curvature $d\delta_z$ for $h_0-dk_z$.

To verify that this really is an algebraic semipositive metric, write $z=\zeta_{a,r}$, where $a\in K$ and $r=|b|$ for $b\in K^\times$. In the affine chart the function
$$
w_z(x)=d\left(\log\max(r,|Z-a|_x)-\log\max(1,|Z|_x)\right)-c_z
$$
with $c_z$ the preceding expression at $o$ is the relative weight of a transformed standard Fubini--Study metric. Nested disk computation shows $w_z=-dk_z$: it has slope $-d$ exactly on $[o,z]$ and is constant on every branch off that path. This computation also treats disks outside the unit disk by passing through their common ancestor with $o$. Its curvature is $d\delta_z$, either by the same slope computation or by the standard model's degree and the coordinate automorphism. Thus the elementary potentials are genuine semipositive metrics. Each $k_z$ is a difference of continuous Fubini--Study metrics, divided by $d$.

If $\nu=\sum_i a_i\delta_{z_i}$, $a_i\geq0$, $\sum a_i=d$, with type II $z_i$, then
$$
h_0-p_\nu=\sum_i\frac{a_i}{d}(h_0-dk_{z_i})
$$
is continuous psh and its genuine raw measure is $\nu$. Rational convex combinations follow by tensor powers, and real combinations by uniform limits. Multilinearity in dimension one makes curvature linear.

For an arbitrary mass-$d$ measure on a finite tree $F$, approximate it by mass-preserving positive atomic measures at type II subdivision points, moving each point a graph distance at most $\varepsilon$. Since $|k(x,y)-k(x,z)|\leq\operatorname{dist}(y,z)$ on $F$, the potentials differ uniformly by at most $d\varepsilon$. Boucksom--Eriksson Theorem 8.4 applies to these continuous psh metrics and shows
$$
\operatorname{MA}(-p_{\mu,F})=(r_F)_*\mu=:\mu_F.
$$
This is a genuine continuous Monge--Ampere measure. We have not replaced it with a separately defined inverse measure.

For any continuous psh relative weight $v$, integration by parts from Proposition 8.3, extended by the uniform approximation of Theorem 8.4, gives
$$
\int_T k_z\,\operatorname{MA}(v)=v(o)-v(z).
$$
The reference contribution vanishes because $k_z(o)=0$. Write $\nu=\operatorname{MA}(v)$, of raw mass $d$. This identity shows $v(z)=v(o)-p_\nu(z)$ at every type II $z$. Along a rooted path ending at any $x$, choose an increasing sequence of type II cutoffs $z_j$ tending to $x$. The kernels $k(z_j,\cdot)$ increase to $k(x,\cdot)$; ordinary sequential monotone convergence and continuity of $v$ give
$$
v(x)=v(o)-p_\nu(x).
$$
Thus every continuous psh metric has precisely the kernel representation, and in particular its normalized relative weight is nonpositive. Finite-tree piecewise affine functions are linear combinations of constants and the $k_z$, as their finite graph Laplacians and root values determine them. The integration-by-parts tests consequently form a dense subspace of $C(T)$.

# All psh weights and the unbounded operator

For every positive Radon $\mu$ of mass $d$, the continuous psh net
$$
u_F=c-p_{\mu,F}
$$
decreases to $u=c-p_\mu$. It is not identically $-\infty$ since $u(o)=c$. Boucksom--Eriksson Lemma 7.4 makes this a psh metric under the Fubini--Study decreasing-net definition. Its approximating measures are the genuine measures $\mu_F$, which converge weakly to $\mu$ by the finite-retraction argument.

Conversely let $v_i$ be any decreasing net of continuous psh weights with nontrivial limit $u$. Put $c_i=v_i(o)$ and $\nu_i=\operatorname{MA}(v_i)$. Since $v_i\leq c_i$, a limit $c_i\to-\infty$ would force $u\equiv-\infty$. Hence $c=\lim c_i$ is finite. At every type II $z$,
$$
c_i-d\ell(z)\leq v_i(z)\leq c_i,
$$
so $v_i(z)$ has a finite limit. The integrals of $k_z$ against $\nu_i$ therefore converge. Compactness of the mass-$d$ Radon measures and density of the span of the $k_z$ imply weak convergence to one uniquely determined measure $\mu$, without a separability assumption. At type II points $u(z)=c-p_\mu(z)$.

For an arbitrary endpoint or nonrigid point $x$, the continuous representations give $v_i(x)=\inf_{z\in[o,x),\ z\text{ type II}}v_i(z)$. Both infima commute:
$$
u(x)=\inf_i\inf_z v_i(z)=\inf_z\inf_i v_i(z)=c-p_\mu(x).
$$
The root is dealt with separately. Thus the complete psh cone is exactly
$$
\operatorname{PSH}(L)=\{c-p_\mu:c\in\mathbf R,\ \mu\geq0,\ \mu(T)=d\}.
$$
The representation is unique, since $\int k_zd\mu=c-u(z)$ and these test functions, together with constants, have dense span.

Define $\operatorname{MA}(c-p_\mu)=\mu$. The preceding argument proves independence of **every** decreasing continuous psh approximation, agreement with the genuine continuous operator, raw mass $d$, and weak decreasing continuity. In fact the operator is defined on all psh weights in this one-dimensional sector. The same test argument proves decreasing continuity for a net of already singular psh weights with a nontrivial psh limit. This linear phenomenon is special to dimension one; it does not construct a wedge product in higher dimensions.

# Dirichlet completion and the exact energy condition

Let $\mathcal A$ be the root-zero continuous finite-tree piecewise affine functions with type II knots. The form $D$ is independent of enlarging the finite tree because the function is constant on added branches. It is positive definite on $\mathcal A$. Let $H$ be its Hilbert completion. Point evaluation at any finite-depth $x$ extends continuously, since
$$
|f(x)|\leq\sqrt{\ell(x)}\sqrt{D(f,f)}.
$$
For finite $F$, let $H_F$ be the closed subspace of root-zero absolutely continuous functions on $F$, with square-integrable edge derivatives, pulled back by $r_F$. Linear interpolation approximates them in Dirichlet norm, so $H_F\subset H$.

On an oriented edge of $F$, the derivative of $p_{\mu,F}$ is the mass of $\mu_F$ in the descendant subtree beyond the point of that edge. It lies in $[0,d]$. Integrating edge derivatives, or first checking atomic measures and then approximating them, gives
$$
D(p_{\mu,F},p_{\nu,F})=\iint k_F(x,y)\,d\mu(x)d\nu(y)=:I_F(\mu,\nu).
$$
This formula also proves the symmetry and nonnegativity of the finite-tree mutual energy. If $G\supset F$, then $p_{\mu,G}|_F=p_{\mu,F}|_F$, and the additional edge derivatives are disjoint from those of a function in $H_F$. Therefore $p_{\mu,F}$ is the orthogonal projection of $p_{\mu,G}$ onto $H_F$, and
$$
\|p_{\mu,G}-p_{\mu,F}\|_H^2=I_G(\mu)-I_F(\mu).
$$
If $I(\mu)<\infty$, this net is Cauchy and defines $p_\mu\in H$. Point evaluations agree with the actual kernel potential at all finite-depth points. Conversely, a bounded Dirichlet norm for these restrictions implies $I(\mu)<\infty$. For finite-energy positive measures,
$$
I(\mu,\nu)=\iint k\,d\mu d\nu
=D(p_\mu,p_\nu)\leq\sqrt{I(\mu)I(\nu)}.
$$
To obtain the equality, use the increasing finite kernels and the Radon integration fact, and then take limits in the Hilbert pairing. In particular $p_\nu$ is integrable against $\mu$. No infinite-energy endpoint value is silently assigned a finite Sobolev value.

For continuous psh $u=c-p_\mu$, the raw continuous energy formula gives
$$
E(u)=dc-\tfrac12 I(\mu).
$$
For an arbitrary psh $u=c-p_\mu$, its finite-tree majorants have energies $dc-\tfrac12 I_F(\mu)$. They show that the infimum over continuous majorants is at most $dc-\tfrac12 I(\mu)$. For the reverse inequality, let $v\geq u$ be any continuous psh weight and $\varepsilon>0$. The increasing open sets $\{u_F<v+\varepsilon\}$ cover the compact space $T$; a finite subcover and directedness show $u_F\leq v+\varepsilon$ eventually. Monotonicity of continuous energy, Proposition 9.14, gives $E(u_F)\leq E(v)+d\varepsilon$. Taking the limit and then the infimum proves
$$
E(c-p_\mu)=dc-\tfrac12 I(\mu),\qquad
\mathcal E^1(L)=\{c-p_\mu:I(\mu)<\infty\}.
$$
If $I(\mu)=\infty$, the displayed identity means $E(u)=-\infty$, and the upper bound from the finite-tree net already proves it.

This argument also proves energy continuity along any decreasing psh net: for a fixed continuous majorant $v$ of the limit, compactness and the open sets $\{u_i<v+\varepsilon\}$ eventually give the energy upper bound $E(u_i)\leq E(v)+d\varepsilon$; monotonicity supplies the lower bound. The argument uses upper semicontinuity of $u_i$, not a dominated-convergence assertion for nets.

For a positive mass-$d$ measure $\mu$, constants cancel in the dual functional. If $I(\mu)<\infty$ and $v=a-p_\nu$ is continuous psh, then
$$
E(v)-\int v\,d\mu=I(\mu,\nu)-\tfrac12 I(\nu)
\leq\tfrac12 I(\mu),
$$
by completing the Hilbert square. Taking $v=-p_{\mu,F}$ gives exactly $\tfrac12 I_F(\mu)$, since $I(\mu,\mu_F)=I_F(\mu)$. These tests also work when $I(\mu)=\infty$, where their dual values tend to infinity. Thus
$$
J_{h_0}(\mu)=\tfrac12 I(\mu)\quad\text{in }[0,+\infty].
$$
This is the asserted raw-mass finite-energy condition. Taking the supremum over Fubini--Study metrics gives the same quantity by uniform density; taking it over all $\mathcal E^1$ gives the same quantity by the mutual-energy bound and the same tests. For the normalized energy $\overline E=E/d$ and probability measure $\overline\mu=\mu/d$, the dual energy is $J_{h_0}(\mu)/d=I(\mu)/(2d)$. This normalization never changes the original raw measure or renormalizes a restriction of it.

# Existence, uniqueness, differentiation, comparison and compactness

If $J_{h_0}(\mu)<\infty$, the actual function $u=-p_\mu$ is psh, has finite energy, and satisfies $\operatorname{MA}(u)=\mu$. Uniqueness modulo constants follows from the unique kernel representation. More strongly, for any $v=a-p_\nu\in\mathcal E^1$,
$$
E(v)-\int v\,d\mu
=\tfrac12 I(\mu)-\tfrac12\|p_\nu-p_\mu\|_H^2.
$$
The maximum is attained precisely at $u+$ constants. This proves the equation by a constructed unbounded potential, rather than by a conditional existence of a maximizer.

For $u,v\in\mathcal E^1$ and $b=v-u$, their affine segment is psh and finite energy. Mutual integrability makes the actual integral of $b$ against either measure finite; sets where an individual potential is $-\infty$ have zero mass for both measures. The quadratic identity $E(u)=du(o)-\tfrac12 D(u,u)$ gives
$$
\left.\frac{d}{dt}\right|_{t=0+}E(u+tb)
=d b(o)-D(u,b)=\int_T b\,\operatorname{MA}(u).
$$
This is differentiation for the **actual unbounded operator** along $\mathcal E^1$ directions, not merely continuous metric volume differentiation.

For completeness, the global comparison principle is
$$
\operatorname{MA}(v)(\{u<v\})\leq
\operatorname{MA}(u)(\{u<v\}),\qquad u,v\in\mathcal E^1.
$$
Here any points where both weights are $-\infty$ may be omitted: mutual integrability makes them null for both measures. Put $w=v-u$ and $\eta_\varepsilon=\min(1,\max(0,w/\varepsilon))$. We justify the Sobolev test rather than presuming a distribution can be multiplied by an unbounded function. On finite trees $w_F=w\circ r_F$ and $\eta_\varepsilon(w_F)$ are absolutely continuous. Restrictions are consistent under enlargement, and their Dirichlet norms are bounded by $\varepsilon^{-2}D(w,w)$. Their added-edge energies increase and are bounded, so they converge strongly in $H$, with the fixed root value, to the contraction $\eta_\varepsilon(w)$. On each finite tree
$$
D(\eta_\varepsilon(w_F),w_F)
=\varepsilon^{-1}\sum_e\int_{\{0<w_F<\varepsilon\}\cap e}|w_F'|^2\,dt\geq0.
$$
Passing in the Hilbert pairing preserves nonnegativity.

The pairing with $\mu_u=\operatorname{MA}(u)$ and $\mu_v=\operatorname{MA}(v)$ is the actual bounded-function integral. To check this point, choose increasing finite trees $F_j$ whose projection energies approach those of $p_{\mu_u}$ and $p_{\mu_v}$. For each potential $p$ and each of these measures $\rho$, the nonnegative integral $\int(p-p\circ r_{F_j})d\rho$ tends to zero by the mutual-energy identity and Cauchy--Schwarz. Hence the increasing potential approximations converge to the canonical potentials $\rho$-almost everywhere. Their contractions converge boundedly almost everywhere. Sequential dominated convergence identifies the integrals, while Hilbert convergence identifies the Dirichlet pairings. Integration by parts on the finite trees, equivalently the continuous test identity, therefore passes to
$$
\int\eta_\varepsilon(w)(\mu_v-\mu_u)
=-D(\eta_\varepsilon(w),w)\leq0.
$$
As $\varepsilon\downarrow0$, ordinary bounded convergence gives the claimed comparison inequality. The common reference measure cancels exactly; no subset measure is rescaled.

The compactness replacement is also concrete. Positive mass-$d$ Radon measures form a weakly compact space. The tests $k_z$ show that normalized psh weights $u(o)=0$, with the topology of pointwise convergence on type II points, are homeomorphic to this space. Thus the normalized psh cone is compact. Moreover $I=\sup_F I_F$ is weakly lower semicontinuous, because each bounded continuous kernel gives a weakly continuous quadratic integral (use finite sums of products to check this). Hence each finite-energy sublevel $I\leq C$ is weakly compact. For normalized finite-energy nets, pointwise convergence on type II points and convergence of $E$ are precisely weak Hilbert convergence and convergence of squared norms; together they imply strong Hilbert convergence. Conversely these conditions follow from weak measure convergence and convergence of $J=I/2$. This proves the strong-topology homeomorphism in Theorem 1, including for nets.

**Envelope and regularization inputs.** The finite-tree net supplies actual decreasing continuous psh regularization. Continuity of psh envelopes for smooth projective curves over complete nontrivially valued fields is the curve background explicitly recorded by Boucksom--Eriksson in the introduction and after Conjecture 7.30, based on Thuillier. Our hypotheses are a special case of that stated domain. The equation proof does not need an envelope theorem or an unproved derivative of $E\circ P$: the explicit Green potential and the Hilbert square replace that variational step. Compactness, approximation, the unbounded energy derivative and comparison used in the proof have all been proved above. This bypass is confined to a linear one-dimensional equation.

# Reference dependence and an unbounded nonskeletal example

Let $h_1=h_0+a$ be any other **continuous semipositive** reference metric on the same $L$. Continuous energy satisfies the cocycle identity. The infimum definitions over absolute continuous psh majorant metrics extend it exactly:
$$
E_{h_1}(u-a)=E_{h_0}(u)-E_{h_0}(a).
$$
The rightmost term is finite, so the absolute space of finite-energy metrics is the same. The dual energies satisfy
$$
J_{h_1}(\mu)=J_{h_0}(\mu)-E_{h_0}(a)+\int_T a\,d\mu.
$$
The last integral is finite since $a$ is continuous and $\mu(T)=d$. Thus finiteness is reference-independent. The operator is intrinsic: it agrees on continuous metrics with the genuine curvature operator, and decreasing approximations are reference-independent absolute metrics. This argument changes neither $L$ nor the raw mass.

Here is an explicit solution outside the invariant, canonical-toric-skeleton-supported regime. Choose $\pi\in K$ with $0<|\pi|<1$, put $\lambda=-\log|\pi|$, and let
$$
z_j=\zeta_{1,|\pi|^j},\qquad
\mu=\sum_{j=1}^{\infty}\frac{d}{j(j+1)}\delta_{z_j}.
$$
All nodes lie on the ray from $o$ towards the rigid point $1$, off the standard toric skeleton in the coordinate $Z$. The measure has mass $d$, and its support also contains $1$, with zero atom there. On the $j$th length-$\lambda$ edge, its descendant mass is $d/j$, so
$$
I(\mu)=\lambda d^2\sum_{j=1}^{\infty}j^{-2}<\infty,
\qquad
p_\mu(1)=\lambda d\sum_{j=1}^{\infty}(j+1)^{-1}=+\infty.
$$
Thus $u=-p_\mu$ is a genuine finite-energy psh solution and $u(1)=-\infty$. It is not continuous with finite real weights. No finite subtree contains its support. In particular this example cannot be obtained by restricting an arbitrary measure to one finite skeleton and normalizing that restriction. A toric metric has a toric skeletal Monge--Ampere measure, so this solution is noninvariant in the stated coordinate. The argument treats every admissible Radon measure, not just this example.

Retraction onto $[o,z_N]$ gives exactly
$$
\mu_N=\sum_{j=1}^{N-1}\frac{d}{j(j+1)}\delta_{z_j}
+\frac dN\delta_{z_N},\quad
I(\mu_N)=\lambda d^2\sum_{j=1}^N j^{-2},\quad
u_N(z_N)=-\lambda d\sum_{j=1}^N j^{-1}.
$$
These identities also fix the mass and sign conventions independently of OCR.

# Exact obligations still open in this deliverable

For the original valuation axis, retain a smooth geometrically connected projective algebraic $n$-fold, an ample line bundle, and the other endpoint characteristic hypotheses (in particular residue characteristic zero in the nontrivial BFJ sector). Allow a complete real-valued non-Archimedean field with no discreteness assumption; impose no torus invariance and no measure-support restriction. The raw mass remains $V=(L^n)>0$. With a fixed continuous semipositive reference metric, the continuous raw energy is
$$
E(u)=\frac1{n+1}\sum_{j=0}^n\int u\,
c_1(L,h_0+u)^j\wedge c_1(L,h_0)^{n-j},
$$
and the intended admissibility condition for a positive Radon $\mu$ of raw mass $V$ is
$$
\sup_{v\in C\cap\operatorname{PSH}}
\left(E(v)-\int v\,d\mu\right)<\infty.
$$
The infimum-majorant definition of extended energy and $\mathcal E^1$ is available without solving the equation. A completion of finite-energy test measures is also available in the audited synthetic formalism. The remaining indispensable assertions have not been proved here:

* **Actual potential and mixed operator:** identify suitable completions with actual upper semicontinuous psh metrics, and prove that decreasing continuous/model approximants of every finite-energy metric give unique, positive, full-raw-mass genuine mixed Monge--Ampere measures. Rule out loss of mass and dependence on approximants. Merely declaring the limiting inverse measure to be $\operatorname{MA}(u)$ without compatibility does not do this.
* **Compactness for potentials:** prove the normalized psh compactness and upper semicontinuity/strong compactness needed to extract an actual finite-energy maximizing potential from test metrics, in the nondiscrete field setting. Weak compactness or quasi-metric completeness of measures alone does not produce that potential.
* **Envelope/obstacle replacement:** obtain the precise psh envelope regularity, psh upper-envelope stability, and any orthogonality needed in a potential-based proof, or supply a proved alternative. The synthetic orthogonality already reported by the source is useful; the missing step is its link to the actual unbounded potential and operator, not a claim that all orthogonality is unknown.
* **Unbounded energy differentiation:** for that actual operator establish the integrability and approximation estimates justifying energy differentiation in finite-energy directions, and, if using the variational method, obstacle variations sufficient to infer equality with the target against all continuous tests. Continuous volume differentiation does not supply this step by itself.
* **Comparison and injectivity:** prove comparison/domination or equivalent finite-energy estimates for the actual unbounded mixed operator over the new fields, sufficient for uniqueness modulo constants. Continuous-metric uniqueness does not automatically extend to singular weights.
* **Ground-field passage, if used:** prove every proposed pullback/descent assertion for psh metrics, raw intersection mass, finite energy, derivatives and comparison. No passage from the algebraically closed projective-line sector to arbitrary $K$ or arbitrary smooth $X$ is supplied here; a normalization or resolution cannot silently replace the ample polarization.

These are concrete gaps of this deliverable, not a theorem that the extensions are impossible, and not a comprehensive claim about all post-2020 literature. The dimension-one explicit construction neither constructs higher-dimensional wedge products nor removes the extra algebraic-closedness/geometric restriction. The whole original P16.4 remains open in this submission; `candidate=false`.

# Artifacts, commands and evidence

The original bytes are retained as `input.json` and byte-identical `input-original.json`; decoded assignment and task are retained as `assignment-original.txt` and `task-original.json`. `audit_sources.py` verifies the ten cache hashes and regenerates literal extracts and application checks. `finite_tree_checks.py` independently computes kernel matrices and a weighted graph Laplacian with rational arithmetic. Its output records checks of raw mass, sign, energy, projection and differentiation, plus finite truncations of the unbounded example. These are finite observations on specified inputs, not exhaustive verification of all trees or a proof of the theorem.

`P16.4-paper.tex` is a standalone rendering of this argument; `P16.4-paper.pdf` is built twice with the existing TeX installation, without software installation or external compute. Actual stdout, stderr, return codes and first/second TeX logs are retained in `build/`. `status.json` has exactly the required five keys. `environment.json` records the runtime/tool versions; `checks.json` records byte identity, source checks, graph checks and build results. The source files, input files, programs, commands and diagnostics suffice to rerun this work.

The actual exact-arithmetic run passed nine groups of checks on a five-node branched tree with $d=2$ and five ray truncations $N=1,2,3,10,100$. It returned $I(\mu)=616699/198450$, $E(u)=-616699/396900$, projected energy $571619/198450$, directional derivative $948301/793800$, and comparison cutoff integral $-6313/302400$. The two actual pdfLaTeX runs both returned zero and produced a 12-page PDF; the second log had no LaTeX warning, error, or overfull box. The installed engine was pdfTeX 3.141592653-2.6-1.40.26 (TeX Live 2025/dev/Debian), and the arithmetic program used Python 3.12.14. These reported facts are observations, not mathematical verification of the infinite tree argument.

Run from this directory:

```sh
python3 audit_sources.py
python3 finite_tree_checks.py
python3 build_deliverable.py
```

No resource-heavy computation was needed, and none was launched. Successful execution, source hashes and two successful TeX runs do not establish mathematical correctness. This is an unverified partial-proof draft.


# Actual native canonical notes, all fields and support

[
  {
    "id": "n1",
    "summary": "The ten authorized source versions do not discharge P16.4. BFJ 1201.0188v1 retains discrete valuation, algebraizability and SNC support; Boucksom–Eriksson treats continuous metrics; the synthetic measure completion does not identify actual unbounded potentials. The 2025 sources retain relevant operator limitations.",
    "detailedSummary": "Checked the actual cached versions and all supplied hashes. Distinguished continuous Monge–Ampère extension, continuous energy/volume results, definition of E^1, synthetic completion of finite-energy measures, and a genuine unbounded operator/equation theorem. Thuillier supplies applicable classical curve background over complete nontrivially valued fields. The audit supports a projective-line partial construction, but supplies no general arbitrary-field finite-energy theorem. This is an audit of the supplied corpus, not an exhaustive literature survey or a proof that the general extension is impossible.",
    "text": "The source audit concerns exactly the ten authorized public caches. No other research material was read. Running `python3 audit_sources.py` verified every supplied PDF, text-extract and abstract-HTML hash and saved 21 literal extracts. The extracts, locations, hashes, original-PDF render checks and precise application checks are in `source-extracts/source-provenance.json`. File identity and execution success do not certify mathematical correctness.\n\n1. Boucksom–Favre–Jonsson, arXiv:1201.0187v2, Singular semipositive metrics in non-Archimedean geometry. The standing field is complete discretely valued with residue characteristic zero; X is a smooth projective analytification and L is ample. Theorems A and B establish normalized psh compactness and decreasing model regularization in that domain. These saved statements cannot be used as arbitrary-field replacements merely by deleting discreteness.\n\n2. Boucksom–Favre–Jonsson, arXiv:1201.0188v1, Solution to a non-Archimedean Monge–Ampère equation. This cache is the actual available v1. Its Theorem A assumes a complete discrete valuation field of residue characteristic zero, a smooth projective variety defined over a one-variable function field admitting K as a completion, an ample L, and a positive Radon measure of raw mass (L^n) supported on one SNC dual complex. The introduction separately records curve background over any complete nontrivially valued field. Later statements removing algebraizability cannot be attributed to this v1. Its main theorem is not an arbitrary-support higher-dimensional application.\n\n3. Boucksom–Eriksson, arXiv:1805.01016v3, Spaces of norms, determinant of cohomology and Fekete points in non-Archimedean geometry. This is the spaces-of-norms paper. Theorem A identifies relative volume with energy for continuous psh metrics on an ample line bundle over a geometrically reduced projective scheme and any complete valued field. Definition 7.2 and Lemma 7.4 concern decreasing nets of Fubini–Study metrics and closure under decreasing limits. Corollary 7.6 identifies continuous psh metrics with their uniform closure. Theorem 7.8 identifies these with uniform limits of nef model metrics when K is nontrivially valued and L is ample. Theorems 7.14 and 8.4 give the genuine mixed operator for continuous psh metrics, continuously under uniform convergence. Proposition 8.3 gives raw intersection mass and integration by parts; Definition 9.13 and Proposition 9.14 give continuous energy and its cocycle identity. These are valid background for X=P^1 and L=O(d). They do not themselves prove decreasing continuity for unbounded potentials. The smooth-curve continuity-of-envelopes endpoint is explicitly recorded in the introduction and after Conjecture 7.30.\n\n4. Boucksom–Jonsson, arXiv:1801.08229v4, Global pluripotential theory over a trivially valued field. Theorem A constructs the finite-energy extension and an embedding with dense image; surjectivity is stated for smooth X when characteristic is zero or dimension is at most two. The field in this formulation is algebraically closed and trivially valued. No passage from this theorem to nontrivial valuations was proved here.\n\n5. Boucksom–Jonsson, arXiv:2307.01697v1, Measures of finite energy in pluripotential theory: a synthetic approach. The source expressly says: “The emphasis in this paper is on measures of finite energy, as opposed to potentials of finite energy, that we do not seek to investigate here”. Theorem A and Theorems 2.23–2.24 establish strong density of test Monge–Ampère measures and a complete Dirichlet quasi-metric on finite-energy measures under orthogonality. Example 2.20 states orthogonality for the projective Berkovich formalism, using continuous-volume results and a uniform differentiation estimate. The proof of density compares the test-envelope energy at ψ_i+t f with the dual-energy upper bound, obtaining t∫f MA(ψ_i) ≤ t∫f μ + J(μ,ψ_i) + A t²; a maximizing sequence therefore gives convergence of measures. This argument does not extract an actual unbounded psh potential. Completeness of the target and density of the image do not alone imply surjectivity from the geometric potential space. Synthetic orthogonality is also distinct from continuity of every psh envelope. No arbitrary-field identification of numerical cohomology spaces was imported.\n\n6. Pille–Schneider, arXiv:2209.04879v2, Global pluripotential theory on hybrid spaces. Theorem 4.3 gives the continuous operator over complete valued fields. Remark 4.4 states: “While the class E¹(X,L) of finite-energy psh metrics on L is defined over any non-archimedean field K, it is unclear in general how to extend the Monge-Ampère operator on the latter.” It then records the discrete characteristic-zero and trivial endpoints. The actual BFJ standing restriction was checked separately as residue characteristic zero; the abbreviated wording does not justify mixed-characteristic applications.\n\n7. Gubler–Rabinoff, arXiv:2506.13548v2, dated 17 September 2025, Classically psh and pluriharmonic functions on Berkovich spaces. It allows arbitrary complete non-Archimedean fields, including trivial valuations, and proves properties of classically psh functions and maximum principles. Its introduction explicitly says that regularization or construction of a Monge–Ampère measure might require additional hypotheses and is not its subject. Appendix A supplies the disk-tree topology used as background below. Coordinate disks in Z and 1/Z are identified along their overlap; their intersection is not just the Gauss point. No higher-dimensional operator follows from the maximum principle alone.\n\n8. Thuillier, thesis tel-00010990v1. Chapter 2 assumes a complete nontrivially valued field, without a discrete-valuation requirement. The curves are smooth and strictly analytic; Section 3.5 additionally assumes connected and proper. P^1 satisfies these hypotheses. Theorem 3.3.13 solves the mass-zero Laplace equation for currents; Lemma 3.3.12 identifies its kernel with harmonic functions; Theorem 3.4.19 regularizes subharmonic line-bundle metrics. Proposition 3.5.7 equates μ−μ(T)δ_x belonging to dd^c W¹, the Green potential belonging to W¹, and its μ-integrability. Original PDF page 117, printed page 103, was inspected and confirms the full raw-mass coefficient. Original PDF page 111 confirms that increasing norms correspond to decreasing additive weights. An isolated displayed curvature sign on printed page 97 is inconsistent with that local convention; the partial proof fixes its sign independently by integration by parts. No unproved field descent or identification of arbitrary smooth metrics with algebraic model metrics is used.\n\n9. Berkovich, Etale cohomology for non-Archimedean analytic spaces, PMIHES 78 (1993). This is general analytic background, not a finite-energy Monge–Ampère theorem. No indispensable new application of its cohomological results is claimed.\n\n10. Chambert-Loir–Ducros, arXiv:1204.6277v2, July 2025. The actual expanded v2 has transfinite psh definitions in Section 8.1. Original PDF page 207 was inspected: Lemma 8.5.5 explicitly states “Pour toute fonction continue psh u”. Proposition 8.7.2 requires continuous functions and local uniform convergence. The shorthand in 8.7.1 must be read with the product hypotheses it cites. The audited statements supply neither a global unbounded E¹ operator nor an all-support finite-energy equation. Earlier-version section numbers cannot be transferred to this v2.\n\nThese findings leave the general P16.4 obligation unresolved within this deliverable. They permit use of the elementary projective-line tree and genuine continuous-metric theory in the partial proof in n2. The passages to unbounded potentials in that proof are proved explicitly, rather than inferred from the source audit.\n\nArtifacts: /workspace/research/campaigns/round-46/P16.4-public-source-arbitrary-field-finite-energy-equations/artifacts/codex-cC7tVd",
    "support": []
  },
  {
    "id": "n2",
    "summary": "Unverified partial proof: for algebraically closed complete nontrivially valued K of residue characteristic zero, X=P^1 and L=O(d), the genuine finite-energy operator solves every positive Radon target of raw mass d and finite dual energy. The criterion is J(μ)=I(μ)/2. No support or invariance restriction is imposed; general P16.4 remains unresolved.",
    "detailedSummary": "Constructs actual psh potentials u=c−p_μ using the full rooted Berkovich-tree Green kernel. Identifies the operator with genuine continuous Monge–Ampère measures and proves independence of decreasing approximations. Proves E(u)=dc−I(μ)/2, the exact dual measure condition, existence and uniqueness modulo constants, decreasing continuity, reference independence, finite-energy differentiation, comparison, and normalized compactness. An explicit measure off the standard toric skeleton has finite energy and a solution equal to −∞ at the rigid point 1. The result retains smooth projective algebraic geometry, ample O(d), nontrivial valuation and residue characteristic zero, but adds algebraic closedness and restricts geometry to the projective line.",
    "text": "This is a mathematical partial-proof draft, not an exhaustive finite computation or a solution of the original arbitrary-field atom. The complete argument is retained in `P16.4-argument.md` and the standalone `P16.4-paper.tex`. The permitted published background and exact application hypotheses are recorded in n1.\n\nRetained domain: K is algebraically closed and complete for a nontrivial real-valued non-Archimedean absolute value, with residue characteristic zero; X=P^1_K; L=O(d), where d≥1 is an integer. Thus X is smooth, geometrically connected, algebraic, proper and projective, and L is ample. No discreteness, spherical completeness, countability or function-field algebraizability is imposed. Algebraic closedness and X=P^1 are additional restrictions. No descent to general K is asserted.\n\nLet T=X^an, o its Gauss point, and h₀ the standard semipositive metric on O(d). Its genuine raw curvature is θ=dδ_o. A relative additive weight u gives metric h₀+u, or norm multiplied by exp(−u). Use raw energy, so E(u+c)=E(u)+dc. Exclude the identically −∞ weight.\n\nThe partial theorem is: the genuine operator on continuous semipositive metrics extends to E¹, continuously along decreasing psh nets. For every positive Radon μ on all of T with μ(T)=d and finite dual energy\nJ(μ)=sup{E(v)−∫v dμ : v continuous psh relative to h₀},\nthere exists u∈E¹ with MA(u)=μ, unique modulo constants. There is no support restriction. Here continuous energy is E(v)=(∫v MA(v)+d v(o))/2; extended energy is the infimum over continuous psh majorants. The theorem also includes comparison, differentiation along E¹ segments, reference independence and a strong-topology homeomorphism E¹/R onto these admissible measures.\n\nProof of the kernel and approximation assertions. The projective-line tree has unique paths with logarithmic length. Put k(x,y)=length([o,x]∩[o,y]). It is nonnegative, zero when either argument is o, and may be infinite at a rigid diagonal. Every nonrigid point has finite depth ℓ(x)=k(x,x). Type IV endpoints have positive limiting disk radius because K is complete. Let F run over finite rooted subtrees with type II vertices, and let r_F be rooted-path retraction. Algebraic closedness makes the nonzero value group divisible and hence dense in logarithmic lengths, so these trees exhaust every finite path. The functions k_F(x,y)=k(r_Fx,r_Fy) are bounded continuous kernels increasing to k. Retraction continuity follows from the disk weak topology: each attached branch is collapsed to its attachment point.\n\nFunctions factoring through these retractions form an algebra separating points. Stone–Weierstrass gives uniform density in C(T). Since g∘r_G=g whenever g factors through F⊂G, uniform approximation also gives f∘r_F→f uniformly for every continuous f. Therefore μ_F=(r_F)_*μ→μ weakly. Finite-tree piecewise affine functions with type II knots are uniformly dense as well.\n\nFor completeness, increasing directed suprema of nonnegative continuous functions commute with integration against a Radon measure on a compact Hausdorff space. To prove this without a false dominated-convergence assertion for nets, approximate superlevel sets from inside by compact subsets. The open inequalities defining a superlevel cover each compact subset; a finite subcover and directedness provide one index meeting all finitely many inequalities. Level partitions and truncation prove the integral equality. Apply the same argument to the Radon product on T×T. Fubini for the resulting nonnegative kernels follows by continuous approximation, since finite sums of products of continuous functions are uniformly dense on the compact product.\n\nDefine p_μ(x)=∫k(x,y)dμ(y), I(μ)=∬k(x,y)dμ(x)dμ(y), and p_{μ,F}(x)=∫k_F(x,y)dμ(y). Then p_{μ,F}=p_μ∘r_F, p_{μ,F} increases to p_μ, and I_F(μ)=∬k_F dμdμ increases to I(μ). The potential is lower semicontinuous, zero at o, and bounded at a finite-depth x by μ(T)ℓ(x).\n\nAgreement with the genuine continuous operator. Use the graph Laplacian convention ∫f dd^c g=−D(f,g), where D(f,g) is the sum of edge integrals of f′g′. For a type II z, k_z=k(·,z) satisfies dd^c k_z=δ_o−δ_z. The metric h₀−dk_z is genuinely semipositive, not a separately declared inverse object: write z=ζ_{a,r}, r=|b|, and transform the standard Fubini–Study metric by the coordinate automorphism. Its relative weight is d[log max(r,|Z−a|)−log max(1,|Z|)] minus its value at o. Nested-disk computation gives exactly −dk_z, with slope −d on [o,z] and zero off that path. Its raw curvature is dδ_z.\n\nFor a finite atomic positive ν of mass d at type II points, h₀−p_ν is a convex combination of these genuine metrics, and dimension-one curvature is linear. Rational coefficients follow by tensor powers; real coefficients follow by uniform limits. For μ_F on a compact finite tree, approximate by positive atomic measures of the same mass at type II subdivision points. Moving points by graph distance ε changes the potential uniformly by at most dε. The genuine continuous-operator theorem checked in n1 therefore yields MA(−p_{μ,F})=μ_F.\n\nConversely, for any continuous psh weight v, published integration by parts, passed through uniform approximation, gives ∫k_z MA(v)=v(o)−v(z). Thus if ν=MA(v), v(z)=v(o)−p_ν(z) at every type II point. Along each rooted path, increasing type II cutoffs have kernels increasing to the endpoint kernel. Sequential monotone convergence and continuity of v give v(x)=v(o)−p_ν(x) everywhere. In particular normalized continuous weights are nonpositive. Constants and the k_z span finite-tree piecewise affine functions: their graph Laplacians and root values determine them. Their span is consequently dense in C(T).\n\nUnbounded operator and uniqueness of representation. For every mass-d positive Radon μ, the genuine continuous psh weights c−p_{μ,F} decrease to c−p_μ. The limit is not identically −∞ since its value at o is c. The decreasing-limit closure checked in n1 makes it a psh metric, and its genuine approximating measures converge to μ.\n\nConversely take any decreasing net of continuous psh weights v_i with nontrivial limit u. Set c_i=v_i(o) and ν_i=MA(v_i). Since v_i≤c_i, the limit c=lim c_i is finite. At type II z, c_i−dℓ(z)≤v_i(z)≤c_i, so the limit there is finite. The integrals of k_z against ν_i converge. Weak compactness of mass-d Radon measures and density of the tests imply convergence to a unique μ. Hence u(z)=c−p_μ(z). At any other point x, each continuous representation satisfies v_i(x)=inf_z v_i(z), over type II cutoffs on [o,x). The two infima commute, proving u(x)=c−p_μ(x). Thus every psh weight has a unique representation c−p_μ.\n\nDefine MA(c−p_μ)=μ. The preceding proof establishes agreement with the genuine continuous operator and independence of every decreasing continuous approximation. The same dense-test argument gives weak continuity along decreasing nets of already singular psh weights with a nontrivial limit. In this linear one-dimensional sector the operator actually exists on the entire psh cone. This does not construct a higher-dimensional wedge product.\n\nEnergy identification. Complete the root-zero finite-tree piecewise affine functions for the Dirichlet norm D to obtain a Hilbert space H. Evaluation at a finite-depth point is bounded by |f(x)|≤sqrt(ℓ(x))‖f‖_H. Absolutely continuous finite-tree functions with square-integrable derivatives belong to H by linear interpolation approximation. On each oriented edge, the derivative of p_{μ,F} is the descendant mass beyond that edge. Integrating derivatives gives\nD(p_{μ,F},p_{ν,F})=I_F(μ,ν)=∬k_F dμdν.\nFor F⊂G, restrictions agree and new derivatives lie on added edges. Thus p_{μ,F} is the orthogonal projection of p_{μ,G}, and ‖p_{μ,G}−p_{μ,F}‖²=I_G(μ)−I_F(μ). If I(μ)<∞, these potentials converge in H to their actual kernel potential. Conversely bounded restriction norms imply finite I. Taking limits gives I(μ,ν)=D(p_μ,p_ν)≤sqrt(I(μ)I(ν)) for finite-energy positive measures. Thus their actual mutual potential integrals are finite.\n\nFor continuous u=c−p_μ, the raw energy formula gives E(u)=dc−I(μ)/2. For any psh u the finite-tree majorants give the upper bound for the infimum-majorant energy. For the reverse bound, if v≥u is continuous psh and ε>0, the increasing open sets {c−p_{μ,F}<v+ε} cover compact T. A finite subcover makes c−p_{μ,F}≤v+ε eventually. Monotonicity of continuous energy yields the reverse bound after passage to the limit. Consequently\nE(c−p_μ)=dc−I(μ)/2, and E¹={c−p_μ:I(μ)<∞}.\nIf I is infinite, the majorant energies tend to −∞. The same compact-open-cover argument proves energy continuity along arbitrary decreasing psh nets.\n\nExact measure condition. For finite I(μ) and continuous v=a−p_ν, constants cancel because both measures have raw mass d, and\nE(v)−∫v dμ=I(μ,ν)−I(ν)/2≤I(μ)/2\nby completing the Hilbert square. The continuous test v=−p_{μ,F} attains the value I_F(μ)/2 because I(μ,μ_F)=I_F(μ). These tests also show that J is infinite when I is infinite. Therefore J(μ)=I(μ)/2 exactly. Supremizing over Fubini–Study tests gives the same quantity by uniform density; over E¹ it gives the same quantity by mutual integrability. If energy and measure are normalized by d, the probability-measure dual energy is I(μ)/(2d). The actual target remains the original raw mass-d measure.\n\nExistence and uniqueness. Finite J gives the actual solution u=−p_μ∈E¹ with MA(u)=μ. The unique kernel representation gives uniqueness modulo constants. More explicitly, for v=a−p_ν∈E¹,\nE(v)−∫v dμ=I(μ)/2−‖p_ν−p_μ‖²/2.\nThus the actual solution, modulo constants, is the unique maximizer. Existence was proved by an actual constructed potential, not assumed in a conditional variational template.\n\nUnbounded differentiation. For u,v∈E¹, let b=v−u along their affine psh segment. Mutual integrability makes b integrable against their actual measures, omitting null sets where potentials are infinite. The quadratic identity E(u)=du(o)−D(u,u)/2 gives the right derivative\n(d/dt) E(u+tb)|_{t=0+}=d b(o)−D(u,b)=∫b MA(u).\nThis is an energy derivative for the actual unbounded operator, rather than continuous metric volume differentiation.\n\nComparison. Put w=v−u and η_ε(w)=min(1,max(0,w/ε)). On finite trees w_F=w∘r_F. The contractions agree on restrictions and have Dirichlet norm at most ε^−1‖w‖, so their increasing added-edge energies are bounded and their nets converge strongly, with fixed root value. On each finite tree D(η_ε(w_F),w_F)=ε^−1∑∫_{0<w_F<ε}|w_F′|²≥0; the sign passes to the Hilbert limit.\nTo identify the pairing with the actual measures, select increasing trees whose energies approach those of p_{MA(u)} and p_{MA(v)}. For either potential p and either measure ρ, ∫(p−p∘r_F)dρ tends to zero by the mutual-energy identity and Cauchy–Schwarz. The increasing potential approximations therefore converge to the canonical potentials ρ-almost everywhere. Their contractions converge boundedly almost everywhere; ordinary sequential dominated convergence identifies the actual integrals. Finite-tree integration by parts then gives ∫η_ε(w)(MA(v)−MA(u))=−D(η_ε(w),w)≤0. Letting ε decrease to zero proves MA(v)({u<v})≤MA(u)({u<v}). The exceptional infinite-potential sets are null by mutual integrability. The reference measure cancels without rescaling any restriction.\n\nCompactness and strong topology. The tests k_z identify normalized psh weights u(o)=0 with the weakly compact space of positive mass-d Radon measures. The identification is a homeomorphism for pointwise convergence on type II points. Since I=sup_F I_F and each continuous-kernel quadratic integral is weakly continuous, I is lower semicontinuous; its sublevels are weakly compact. Bounded Dirichlet norms and convergence on the dense evaluation tests give weak Hilbert convergence. Convergence of energy gives convergence of squared norms, hence strong Hilbert convergence. Conversely weak convergence of measures and convergence of J=I/2 give these same conditions. This proves the asserted strong-topology homeomorphism.\n\nEnvelope and regularization inputs. Actual decreasing regularization was supplied by finite-tree potentials. The smooth-curve envelope-continuity result recorded in n1 applies to this domain, but the equation proof does not use an envelope or an unproved derivative of E composed with an envelope. Explicit Green inversion and the Hilbert-square identity replace that variational step. Approximation, compactness, the unbounded derivative and comparison used here have been proved above. This replacement is confined to the linear curve equation.\n\nReference dependence. For another continuous semipositive reference h₁=h₀+a on the same L, the continuous cocycle identity extends through the infimum-majorant definition, giving E_{h₁}(u−a)=E_{h₀}(u)−E_{h₀}(a). Consequently J_{h₁}(μ)=J_{h₀}(μ)−E_{h₀}(a)+∫a dμ. The correction is finite since a is continuous and μ has mass d. Thus the absolute finite-energy space and measure condition are reference-independent. The operator is intrinsic by agreement on continuous absolute metrics and independence of their decreasing approximations. Neither polarization nor raw mass is changed.\n\nAn explicit unbounded nonskeletal example. Choose 0<|π|<1, λ=−log|π|, z_j=ζ_{1,|π|^j}, and μ=∑_{j≥1} d/[j(j+1)] δ_{z_j}. The measure has raw mass d. Its nodes lie off the standard toric skeleton, approaching the rigid point 1, which has zero atom. Descendant mass on the jth length-λ edge is d/j. Hence I(μ)=λd²∑j^−2<∞, while p_μ(1)=λd∑(j+1)^−1=∞. The genuine finite-energy solution u=−p_μ therefore satisfies u(1)=−∞. No finite subtree contains this support, and its measure is not toric-skeletal, so the solution is noninvariant in this coordinate. Retraction to [o,z_N] gives μ_N=∑_{j<N}d/[j(j+1)]δ_{z_j}+(d/N)δ_{z_N}, I(μ_N)=λd²∑_{j≤N}j^−2, and u_N(z_N)=−λd∑_{j≤N}j^−1.\n\nThis proves the stated partial theorem under its exact retained and additional hypotheses. It neither removes algebraic closedness nor constructs higher-dimensional unbounded wedge products. The original P16.4 remains unresolved.\n\nArtifacts: /workspace/research/campaigns/round-46/P16.4-public-source-arbitrary-field-finite-energy-equations/artifacts/codex-cC7tVd",
    "support": [
      "n1"
    ]
  },
  {
    "id": "n3",
    "summary": "Delivered the complete partial argument, standalone 12-page paper, preserved inputs, source provenance and actual two-pass build diagnostics. Exact finite-tree checks passed. Six concrete obligations remain for general P16.4; execution and hashes are not mathematical certification.",
    "detailedSummary": "The implementation assignment is delivered with status=partial and candidate=false. Preserved byte-identical input-original.json, assignment-original.txt and task-original.json. Both final pdfLaTeX runs returned zero; the second had no warning, error or overfull box. Rational checks covered one five-node branched tree and five ray truncations, not all analytic cases. Remaining obligations concern actual unbounded mixed operators, potential compactness, envelope/obstacle replacements, unbounded differentiation, comparison/injectivity, and any ground-field descent.",
    "text": "The deliverable is partial. The original P16.4 has not been proved; candidate=false.\n\nFor the original axis, the intended retained geometric setting is a smooth geometrically connected projective algebraic n-fold, an ample line bundle L, and the other endpoint characteristic hypotheses, including residue characteristic zero in the nontrivial BFJ sector. The field should be complete real-valued non-Archimedean without a discreteness restriction; measures should have unrestricted support. The raw mass is V=(L^n)>0. For a continuous semipositive reference h₀, continuous raw energy is E(u)=(1/(n+1))∑_{j=0}^n ∫u c₁(L,h₀+u)^j∧c₁(L,h₀)^{n−j}; the intended measure condition is μ≥0, μ(X^an)=V and sup_{v continuous psh}(E(v)−∫v dμ)<∞. A definition of its extended energy space and a completion of test measures do not establish the equation.\n\nSix concrete gaps remain in this submission:\n1. Identify actual unbounded psh potentials and prove approximation-independent, positive, full-raw-mass genuine mixed Monge–Ampère measures for their finite-energy class in the general nondiscrete field setting.\n2. Supply normalized potential compactness and extraction of actual finite-energy maximizing metrics, beyond compactness/completeness of measures.\n3. Supply envelope/obstacle regularity or a proved alternative and connect available synthetic orthogonality to actual unbounded potentials and their operator.\n4. Prove integrability, approximation and energy differentiation for that actual operator, including obstacle variations against all continuous tests if using a variational proof.\n5. Prove finite-energy comparison/domination or equivalent injectivity estimates sufficient for uniqueness modulo constants.\n6. Prove every proposed field-extension/descent assertion preserving the ample datum, raw mass, psh metrics, finite energy, derivatives and comparison. No such descent from n2 is asserted.\n\nThese are gaps of this deliverable, not a theorem of impossibility or a comprehensive literature claim. The explicit one-dimensional inversion in n2 cannot be promoted to arbitrary smooth projective varieties by formal completion or normalization.\n\nRetained artifacts: `input.json` and byte-identical `input-original.json`; `assignment-original.txt`; `task-original.json`; `P16.4-argument.md`; standalone `P16.4-paper.tex`; `P16.4-paper.pdf`; `source-extracts/source-provenance.json` and 21 literal extracts with selected original-PDF page renders; `status.json`; `environment.json`; `checks.json`; `artifact-manifest.json`; and actual commands, stdout, stderr and separate first/second TeX logs in `build/`. The status file has exactly id,status,exact_result,proof_file,concrete_gaps.\n\nRerun from the supplied workspace:\n`python3 audit_sources.py`\n`python3 finite_tree_checks.py`\n`python3 build_deliverable.py`\nThe final command also reruns the lightweight checks, regenerates standalone TeX with the existing pandoc, and invokes the existing pdfLaTeX twice with shell escape disabled. Original PDF rendering commands are retained in `source-extracts/render-commands.json`.\n\nObserved checks: all supplied source hashes matched; the original input bytes were identical; task and assignment contents were preserved. The exact-arithmetic program passed nine check groups on one five-node branched rational tree with d=2 and ray truncations N=1,2,3,10,100. It independently compared the kernel matrix with a weighted graph Laplacian and returned I(μ)=616699/198450, E(u)=−616699/396900, projection energy 571619/198450, directional derivative 948301/793800 and comparison cutoff integral −6313/302400. These are specified finite observations, not exhaustive verification over trees or analytic fields.\n\nBoth final pdfLaTeX builds returned zero and produced a 12-page PDF. The second log had no LaTeX warning, error or overfull box. The engine was pdfTeX 3.141592653-2.6-1.40.26, TeX Live 2025/dev/Debian; Python was 3.12.14. No installation, network retrieval, external model, worker, subagent or resource-heavy computation was used. Successful execution, hashes and PDF compilation do not establish mathematical correctness. The mathematical result remains an unverified partial-proof draft.\n\nArtifacts: /workspace/research/campaigns/round-46/P16.4-public-source-arbitrary-field-finite-energy-equations/artifacts/codex-cC7tVd",
    "support": [
      "n1",
      "n2"
    ]
  }
]

# Exact published source metadata and application checks

{
  "scope": "Exactly the ten user-authorized public caches; no other research files read.",
  "sources": [
    {
      "arxiv_id": "1201.0187",
      "saved_version": "1201.0187v2",
      "title": "[1201.0187] Singular semipositive metrics in non-Archimedean geometry",
      "public_source": "https://arxiv.org/pdf/1201.0187v2",
      "abstract_url": "https://arxiv.org/abs/1201.0187",
      "actual_abstract_url": "https://arxiv.org/abs/1201.0187",
      "actual_pdf_url": "https://arxiv.org/pdf/1201.0187v2",
      "abstract_html": "/workspace/research/shared-sources/P16-arxiv-1201.0187-20261004.html",
      "abstract_sha256": "983485b15a5da892c0b29ecb5ebb7280414028bd1333614a0ae8bf5ec888dbde",
      "pdf": "/workspace/research/shared-sources/P16-arxiv-1201.0187-20261004.pdf",
      "pdf_sha256": "8b684713055b9147de0d3379ad925c58f031bafe10a77e769a2791cdaa128270",
      "pdf_bytes": 768011,
      "literal_extract": "/workspace/research/shared-sources/P16-arxiv-1201.0187-20261004.txt",
      "extract_sha256": "6a435578964be38cf1210362f6b7d15dd8e4c2851062bdb4d849fb8be2287415",
      "extract_bytes": 175336,
      "pdftotext_returncode": 0,
      "origin": "Publicly available primary mathematical source; no generated research payload.",
      "local_id": "1201.0187",
      "application_check": "v2: complete discrete valuation field, residue characteristic zero; smooth projective analytification, ample line bundle. Compactness and regularization are not arbitrary-field statements in this version. Used only in the audit.",
      "verified_hashes": {
        "pdf": "8b684713055b9147de0d3379ad925c58f031bafe10a77e769a2791cdaa128270",
        "literal_extract": "6a435578964be38cf1210362f6b7d15dd8e4c2851062bdb4d849fb8be2287415",
        "abstract_html": "983485b15a5da892c0b29ecb5ebb7280414028bd1333614a0ae8bf5ec888dbde"
      },
      "extracts": [
        {
          "file": "source-extracts/1201.0187-standing-and-compactness.txt",
          "supplied_line_start": 89,
          "supplied_line_end": 171,
          "pdf_page_start": 2,
          "pdf_page_end": 4,
          "sha256": "764d27aed24bd6a177c29ba0416db49c3bd5597691f40e1e1062c566c308d925",
          "kind": "literal supplied pdftotext, including original OCR defects"
        }
      ]
    },
    {
      "arxiv_id": "1201.0188",
      "saved_version": "1201.0188v1",
      "title": "[1201.0188] Solution to a non-Archimedean Monge-Ampère equation",
      "public_source": "https://arxiv.org/pdf/1201.0188v1",
      "abstract_url": "https://arxiv.org/abs/1201.0188",
      "actual_abstract_url": "https://arxiv.org/abs/1201.0188",
      "actual_pdf_url": "https://arxiv.org/pdf/1201.0188v1",
      "abstract_html": "/workspace/research/shared-sources/P16-arxiv-1201.0188-20261004.html",
      "abstract_sha256": "e4683a68defd5887b5952cddcccc9f625a2d0391819a97f32a15d4d51f5409ae",
      "pdf": "/workspace/research/shared-sources/P16-arxiv-1201.0188-20261004.pdf",
      "pdf_sha256": "4c29d91987477baf9baa4dfdd0b901ae1cd8910746012fd6285ab9a90bbf3f3a",
      "pdf_bytes": 531005,
      "literal_extract": "/workspace/research/shared-sources/P16-arxiv-1201.0188-20261004.txt",
      "extract_sha256": "d31b3525783a11b73faaf926a74d8888847d5def808011d24e2661c2f9d31d39",
      "extract_bytes": 161436,
      "pdftotext_returncode": 0,
      "origin": "Publicly available primary mathematical source; no generated research payload.",
      "local_id": "1201.0188",
      "application_check": "Actual saved v1, not the later published theorem. Theorem A: complete discrete valuation field of residue characteristic zero; smooth projective algebraizable variety; ample L; positive Radon measure of raw mass (L^n), supported on one SNC dual complex. Its introduction separately records curve background over any complete nontrivially valued field. No arbitrary-support higher-dimensional application.",
      "verified_hashes": {
        "pdf": "4c29d91987477baf9baa4dfdd0b901ae1cd8910746012fd6285ab9a90bbf3f3a",
        "literal_extract": "d31b3525783a11b73faaf926a74d8888847d5def808011d24e2661c2f9d31d39",
        "abstract_html": "e4683a68defd5887b5952cddcccc9f625a2d0391819a97f32a15d4d51f5409ae"
      },
      "extracts": [
        {
          "file": "source-extracts/1201.0188-v1-theorem-and-curve-background.txt",
          "supplied_line_start": 62,
          "supplied_line_end": 131,
          "pdf_page_start": 2,
          "pdf_page_end": 3,
          "sha256": "b74fae52a763e45b452d9e179ec2e5e1cfa27897de8f04b0b05679d2d383a365",
          "kind": "literal supplied pdftotext, including original OCR defects"
        }
      ]
    },
    {
      "arxiv_id": "1805.01016",
      "saved_version": "1805.01016v3",
      "title": "[1805.01016] Spaces of norms, determinant of cohomology and Fekete points in non-Archimedean geometry",
      "public_source": "https://arxiv.org/pdf/1805.01016v3",
      "abstract_url": "https://arxiv.org/abs/1805.01016",
      "actual_abstract_url": "https://arxiv.org/abs/1805.01016",
      "actual_pdf_url": "https://arxiv.org/pdf/1805.01016v3",
      "abstract_html": "/workspace/research/shared-sources/P16-arxiv-1805.01016-20261004.html",
      "abstract_sha256": "d15154ca2fe8e5e1942e16f2d77a8221dffc5162ddfa3c4bd0544c8d6f1b9a1a",
      "pdf": "/workspace/research/shared-sources/P16-arxiv-1805.01016-20261004.pdf",
      "pdf_sha256": "51d02f75a65aa463f8e22393933f5ebef9036e322d720fc632f87759c2b71cb2",
      "pdf_bytes": 1034400,
      "literal_extract": "/workspace/research/shared-sources/P16-arxiv-1805.01016-20261004.txt",
      "extract_sha256": "8e584521fe3d41f179bef93d14315414ac7796532c65518c1861717416f99233",
      "extract_bytes": 344553,
      "pdftotext_returncode": 0,
      "origin": "Publicly available primary mathematical source; no generated research payload.",
      "local_id": "1805.01016",
      "application_check": "Boucksom--Eriksson, Spaces of norms, v3. Theorems 7.8 and 8.4 apply to the partial sector: K complete nontrivially valued, X=P^1 smooth projective, L=O(d) ample. Continuous psh means uniform closure of FS; hence psh-regularizable. Theorem 8.4 is a uniform-continuity result for continuous metrics, not decreasing continuity for unbounded metrics. The curve envelope statement in the introduction/7.30 has the same valid smooth-curve hypotheses; it is background and not used to obtain our explicit solution.",
      "verified_hashes": {
        "pdf": "51d02f75a65aa463f8e22393933f5ebef9036e322d720fc632f87759c2b71cb2",
        "literal_extract": "8e584521fe3d41f179bef93d14315414ac7796532c65518c1861717416f99233",
        "abstract_html": "d15154ca2fe8e5e1942e16f2d77a8221dffc5162ddfa3c4bd0544c8d6f1b9a1a"
      },
      "extracts": [
        {
          "file": "source-extracts/1805.01016-continuous-volume-and-curve-envelopes.txt",
          "supplied_line_start": 119,
          "supplied_line_end": 170,
          "pdf_page_start": 3,
          "pdf_page_end": 4,
          "sha256": "70236ccf76ffadb80d2761f4ed40d7051c499b010699d68fc840fea75aa0c049",
          "kind": "literal supplied pdftotext, including original OCR defects"
        },
        {
          "file": "source-extracts/1805.01016-continuous-psh-and-nef.txt",
          "supplied_line_start": 2286,
          "supplied_line_end": 2340,
          "pdf_page_start": 48,
          "pdf_page_end": 49,
          "sha256": "f9495c38f97b0fc4993aefe7af29ed8673c300ba3dcaac2e85cec580c36f2223",
          "kind": "literal supplied pdftotext, including original OCR defects"
        },
        {
          "file": "source-extracts/1805.01016-continuous-ma-proof.txt",
          "supplied_line_start": 2665,
          "supplied_line_end": 2785,
          "pdf_page_start": 56,
          "pdf_page_end": 58,
          "sha256": "e3243c744ee9c88daf13c592c2bc22fc29e6122d5c6b5a78f8b128c745138f76",
          "kind": "literal supplied pdftotext, including original OCR defects"
        },
        {
          "file": "source-extracts/1805.01016-continuous-energy.txt",
          "supplied_line_start": 3540,
          "supplied_line_end": 3590,
          "pdf_page_start": 74,
          "pdf_page_end": 75,
          "sha256": "1ce23a17b623e56dc8f53d9cb3d69bd3dee71b4eee240100ecf60be2113b974c",
          "kind": "literal supplied pdftotext, including original OCR defects"
        }
      ]
    },
    {
      "arxiv_id": "1801.08229",
      "saved_version": "1801.08229v4",
      "title": "[1801.08229] Global pluripotential theory over a trivially valued field",
      "public_source": "https://arxiv.org/pdf/1801.08229v4",
      "abstract_url": "https://arxiv.org/abs/1801.08229",
      "actual_abstract_url": "https://arxiv.org/abs/1801.08229",
      "actual_pdf_url": "https://arxiv.org/pdf/1801.08229v4",
      "abstract_html": "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.html",
      "abstract_sha256": "680fc70f252a7203bf277dccb65c9fddf4f0725c387d2b41b64d467f087c2304",
      "pdf": "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.pdf",
      "pdf_sha256": "8d5975337f4ac88a475929ea6a436ec4a15d08715d5582bc0ba0eb3e07152c52",
      "pdf_bytes": 1627763,
      "literal_extract": "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.txt",
      "extract_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "extract_bytes": 506945,
      "pdftotext_returncode": 0,
      "origin": "Publicly available primary mathematical source; no generated research payload.",
      "local_id": "1801.08229",
      "application_check": "v4: algebraically closed trivially valued field. Theorem A constructs the finite-energy extension; surjectivity stated for smooth X with characteristic zero or dimension at most two. A nontrivial valuation is outside its standing domain. No base-field descent application.",
      "verified_hashes": {
        "pdf": "8d5975337f4ac88a475929ea6a436ec4a15d08715d5582bc0ba0eb3e07152c52",
        "literal_extract": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
        "abstract_html": "680fc70f252a7203bf277dccb65c9fddf4f0725c387d2b41b64d467f087c2304"
      },
      "extracts": [
        {
          "file": "source-extracts/1801.08229-trivial-valuation-calabi-yau.txt",
          "supplied_line_start": 102,
          "supplied_line_end": 203,
          "pdf_page_start": 3,
          "pdf_page_end": 4,
          "sha256": "acf789bb88dd884dccd373b5abff9e7688a9e543101300e75d2835f5db370ea6",
          "kind": "literal supplied pdftotext, including original OCR defects"
        }
      ]
    },
    {
      "arxiv_id": "2307.01697",
      "saved_version": "2307.01697v1",
      "title": "[2307.01697] Measures of finite energy in pluripotential theory: a synthetic approach",
      "public_source": "https://arxiv.org/pdf/2307.01697v1",
      "abstract_url": "https://arxiv.org/abs/2307.01697",
      "actual_abstract_url": "https://arxiv.org/abs/2307.01697",
      "actual_pdf_url": "https://arxiv.org/pdf/2307.01697v1",
      "abstract_html": "/workspace/research/shared-sources/P16-arxiv-2307.01697-20261004.html",
      "abstract_sha256": "95e379bf14e7779de66bca6e020525202fc32bdb575bd1196934cf6ee43eb11a",
      "pdf": "/workspace/research/shared-sources/P16-arxiv-2307.01697-20261004.pdf",
      "pdf_sha256": "979daddbb2082320cd6bbe6f8522535e68b56d229317decd033c3101b9fdbaa1",
      "pdf_bytes": 788875,
      "literal_extract": "/workspace/research/shared-sources/P16-arxiv-2307.01697-20261004.txt",
      "extract_sha256": "8068829692eeb5ddcfd40de5a6141f415601c5b493e5578ad63e0dd3140bf2e4",
      "extract_bytes": 167662,
      "pdftotext_returncode": 0,
      "origin": "Publicly available primary mathematical source; no generated research payload.",
      "local_id": "2307.01697",
      "application_check": "v1: synthetic formalism includes projective Berkovich spaces over complete non-Archimedean fields. Test space D, model numerical forms, positive interior polarization. Theorem A/2.23/2.24 give strong density and complete quasi-metric on measures; they do not identify a completion element with an actual unbounded psh potential. Orthogonality is stated unconditional for this formalism in Example 2.20, distinct from continuity of all psh envelopes. Used only for audit; no inference of a full unbounded operator.",
      "verified_hashes": {
        "pdf": "979daddbb2082320cd6bbe6f8522535e68b56d229317decd033c3101b9fdbaa1",
        "literal_extract": "8068829692eeb5ddcfd40de5a6141f415601c5b493e5578ad63e0dd3140bf2e4",
        "abstract_html": "95e379bf14e7779de66bca6e020525202fc32bdb575bd1196934cf6ee43eb11a"
      },
      "extracts": [
        {
          "file": "source-extracts/2307.01697-measure-completion-scope.txt",
          "supplied_line_start": 54,
          "supplied_line_end": 164,
          "pdf_page_start": 2,
          "pdf_page_end": 4,
          "sha256": "52a4c424d0e32b4ae3a231195de44da9535eb83ca3705068fd076867348f48ad",
          "kind": "literal supplied pdftotext, including original OCR defects"
        },
        {
          "file": "source-extracts/2307.01697-orthogonality-and-density-proof.txt",
          "supplied_line_start": 1109,
          "supplied_line_end": 1172,
          "pdf_page_start": 23,
          "pdf_page_end": 24,
          "sha256": "cea2102f61d285c7a57298b2e905eba0a096e1cd1f42d84a7306c080b1ec173e",
          "kind": "literal supplied pdftotext, including original OCR defects"
        },
        {
          "file": "source-extracts/2307.01697-measure-quasimetric-proof.txt",
          "supplied_line_start": 1173,
          "supplied_line_end": 1230,
          "pdf_page_start": 24,
          "pdf_page_end": 25,
          "sha256": "bc37eff6b1f373c98edc5fc3f2d75b11762d9fb577f31222c070fd1115528fab",
          "kind": "literal supplied pdftotext, including original OCR defects"
        }
      ]
    },
    {
      "arxiv_id": "2209.04879",
      "saved_version": "2209.04879v2",
      "title": "[2209.04879] Global pluripotential theory on hybrid spaces",
      "public_source": "https://arxiv.org/pdf/2209.04879v2",
      "abstract_url": "https://arxiv.org/abs/2209.04879",
      "actual_abstract_url": "https://arxiv.org/abs/2209.04879",
      "actual_pdf_url": "https://arxiv.org/pdf/2209.04879v2",
      "abstract_html": "/workspace/research/shared-sources/P16-arxiv-2209.04879-20261004.html",
      "abstract_sha256": "1b719dcc2de6a7437184f28dbaf37384bf39673fc8b66a35a4dc716f0cba5341",
      "pdf": "/workspace/research/shared-sources/P16-arxiv-2209.04879-20261004.pdf",
      "pdf_sha256": "55defd54d8201c94d08f727e76f551c759275c68cde354570cb41e7a02df54f7",
      "pdf_bytes": 633342,
      "literal_extract": "/workspace/research/shared-sources/P16-arxiv-2209.04879-20261004.txt",
      "extract_sha256": "f80aba2042cab9a15649c87700aa5c86710dd33018bf025bd1817869d52b31e4",
      "extract_bytes": 185043,
      "pdftotext_returncode": 0,
      "origin": "Publicly available primary mathematical source; no generated research payload.",
      "local_id": "2209.04879",
      "application_check": "Saved v2: Theorem 4.3 continuous metrics over complete valued fields; Remark 4.4 explicitly distinguishes definition of E^1 from extension of MA. Its phrase characteristic zero is quoted literally; retained BFJ standing assumption checked separately is residue characteristic zero. Used only for audit.",
      "verified_hashes": {
        "pdf": "55defd54d8201c94d08f727e76f551c759275c68cde354570cb41e7a02df54f7",
        "literal_extract": "f80aba2042cab9a15649c87700aa5c86710dd33018bf025bd1817869d52b31e4",
        "abstract_html": "1b719dcc2de6a7437184f28dbaf37384bf39673fc8b66a35a4dc716f0cba5341"
      },
      "extracts": [
        {
          "file": "source-extracts/2209.04879-continuous-ma-and-unbounded-gap.txt",
          "supplied_line_start": 1968,
          "supplied_line_end": 1996,
          "pdf_page_start": 35,
          "pdf_page_end": 35,
          "sha256": "07921996b9220ba3268fe21bd0b00211860659a70ca10bc2767d0f77720c8901",
          "kind": "literal supplied pdftotext, including original OCR defects"
        }
      ]
    },
    {
      "public_source": "https://arxiv.org/pdf/2506.13548v2",
      "pdf": "/workspace/research/shared-sources/GR-2506.13548v2-20261004.pdf",
      "pdf_sha256": "83ca9a19394f44bb2e4e1aa316de95938f311acd53a00fe250fa0f605184b726",
      "literal_extract": "/workspace/research/shared-sources/GR-2506.13548v2-20261004.txt",
      "extract_sha256": "3a221b86116604c950db07e4c60ab184701f0624deebabd92502e5c81871436b",
      "origin": "Published primary mathematical source, not generated research.",
      "local_id": "2506.13548",
      "application_check": "v2 dated 17 September 2025: classically psh functions, arbitrary complete non-Archimedean field (possibly trivial), maximum principles. Introduction explicitly excludes MA construction. Appendix A describes the disk tree/topology; used for background tree structure on P^1 over algebraically closed nontrivially valued K. The coordinate disks in Z and 1/Z are identified along their overlap; their intersection is not only the Gauss root. No inference from classically psh to a higher-dimensional finite-energy equation.",
      "verified_hashes": {
        "pdf": "83ca9a19394f44bb2e4e1aa316de95938f311acd53a00fe250fa0f605184b726",
        "literal_extract": "3a221b86116604c950db07e4c60ab184701f0624deebabd92502e5c81871436b"
      },
      "extracts": [
        {
          "file": "source-extracts/2506.13548-scope-and-exclusion.txt",
          "supplied_line_start": 55,
          "supplied_line_end": 88,
          "pdf_page_start": 2,
          "pdf_page_end": 2,
          "sha256": "51fa73fc52a6dfc41726c7410beb7608019d4d897f0c741f2bb31d4e3716cefa",
          "kind": "literal supplied pdftotext, including original OCR defects"
        },
        {
          "file": "source-extracts/2506.13548-disk-tree-topology.txt",
          "supplied_line_start": 1930,
          "supplied_line_end": 1980,
          "pdf_page_start": 36,
          "pdf_page_end": 38,
          "sha256": "ddb836ec9486f26bce7dc77e5f09ede1922934cfcfc6b09ddeaf3c3795afb1ce",
          "kind": "literal supplied pdftotext, including original OCR defects"
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
      "local_id": "thuillier",
      "application_check": "Thesis tel-00010990v1: chapter 2 standing field complete, nontrivially valued; smooth strictly analytic curves. Section 3.5 additionally connected and proper. P^1 in the partial theorem meets every condition. Green functions and Hilbert energy are compatible background; our tree kernel and E^1 identification are proved explicitly. PDF pages 111,117,118 visually checked: additive weights use -log norm, regularization decreases weights, Proposition 3.5.7 includes the full raw mass times delta_x. OCR/sign slips are not copied into our formulas. No normalization, resolution or field-descent assertion is imported.",
      "verified_hashes": {
        "pdf": "9c57da951e8dca2676d762e9e8c6ace302675938d72434a5b0390f15af7ea29a",
        "literal_extract": "e82226b3dde6a8088c35e1481bfd43f64bb69ee309b5cfda92c8c927a7885570"
      },
      "extracts": [
        {
          "file": "source-extracts/thuillier-field-convention.txt",
          "supplied_line_start": 1155,
          "supplied_line_end": 1196,
          "pdf_page_start": 29,
          "pdf_page_end": 29,
          "sha256": "dc6d7f5e9563412931358c24414c9906cd8059d264bcfa9f77f56555d1f9780a",
          "kind": "literal supplied pdftotext, including original OCR defects"
        },
        {
          "file": "source-extracts/thuillier-laplacian-solvability-proof.txt",
          "supplied_line_start": 4957,
          "supplied_line_end": 5075,
          "pdf_page_start": 97,
          "pdf_page_end": 99,
          "sha256": "3f5bd96719721a31c4535b0c016f2427a0fd05856161acc816b2f566c216a46c",
          "kind": "literal supplied pdftotext, including original OCR defects"
        },
        {
          "file": "source-extracts/thuillier-metric-regularization-proof.txt",
          "supplied_line_start": 5670,
          "supplied_line_end": 5759,
          "pdf_page_start": 111,
          "pdf_page_end": 112,
          "sha256": "d4214324f13a48a280a25a69f0c7ceec8e193cc12c6961d7a578015cdf6b05f0",
          "kind": "literal supplied pdftotext, including original OCR defects"
        },
        {
          "file": "source-extracts/thuillier-hilbert-space-proof.txt",
          "supplied_line_start": 5793,
          "supplied_line_end": 5897,
          "pdf_page_start": 113,
          "pdf_page_end": 115,
          "sha256": "42a02fc9c6e9eb01715dfe4f52dd9251d2a2eb8c34c0b94a99873088e87a9401",
          "kind": "literal supplied pdftotext, including original OCR defects"
        },
        {
          "file": "source-extracts/thuillier-finite-energy-proof.txt",
          "supplied_line_start": 5995,
          "supplied_line_end": 6093,
          "pdf_page_start": 117,
          "pdf_page_end": 119,
          "sha256": "1347cd3f3789267b0f42ff390007585da957d0fd62080392c644ff83fbecb505",
          "kind": "literal supplied pdftotext, including original OCR defects"
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
      "local_id": "berkovich",
      "application_check": "Etale cohomology for non-Archimedean analytic spaces, PMIHES 78 (1993), pages 5-161. General analytic foundations, not a finite-energy Monge--Ampere source. No theorem from this paper is indispensable to our partial construction.",
      "verified_hashes": {
        "pdf": "bd864c89ed8b6e8f27a90f459837221549db75afa75554ab51414e17771066af",
        "literal_extract": "694ba4de951bb7e40c73fa4057e4bed5ce073757690ac7379bb1cbbabaf62c1d"
      },
      "extracts": [
        {
          "file": "source-extracts/berkovich-identity-and-general-field.txt",
          "supplied_line_start": 1,
          "supplied_line_end": 110,
          "pdf_page_start": 1,
          "pdf_page_end": 4,
          "sha256": "b5aa1f14d3b685f03b8866a5760cae25678669346f38acd4a0b17353d207ee63",
          "kind": "literal supplied pdftotext, including original OCR defects"
        }
      ]
    },
    {
      "public_source": "https://arxiv.org/pdf/1204.6277v2",
      "pdf": "/workspace/research/shared-sources/CD-1204.6277v2-20261004.pdf",
      "pdf_sha256": "5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719",
      "literal_extract": "/workspace/research/shared-sources/CD-1204.6277v2-20261004.txt",
      "extract_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085",
      "origin": "Published primary mathematical source, not generated research.",
      "local_id": "cd",
      "application_check": "Actual saved v2, July 2025, expanded to 591 PDF pages. Uses transfinite psh definitions. Lemma 8.5.5 explicitly requires continuous psh u; Proposition 8.7.2 assumes continuous functions and local uniform convergence. The shorthand psh in 8.7.1 cannot remove the continuity hypothesis of the cited product lemma. It supplies no global unbounded E^1 all-support equation in the audited statements. Section numbers of v1 must not be applied to v2.",
      "verified_hashes": {
        "pdf": "5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719",
        "literal_extract": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085"
      },
      "extracts": [
        {
          "file": "source-extracts/cd-continuous-product-proof.txt",
          "supplied_line_start": 10291,
          "supplied_line_end": 10339,
          "pdf_page_start": 206,
          "pdf_page_end": 207,
          "sha256": "7b0e37d3349dfaeb99be34a37180740bd1634ad2aaf1743a99c3c47831416a71",
          "kind": "literal supplied pdftotext, including original OCR defects"
        },
        {
          "file": "source-extracts/cd-iteration-and-uniform-convergence.txt",
          "supplied_line_start": 10410,
          "supplied_line_end": 10494,
          "pdf_page_start": 209,
          "pdf_page_end": 211,
          "sha256": "c27d5e55bb0894350d1e432edb8863e386a06dc859f7a65d5bcc6d0a4b76ae43",
          "kind": "literal supplied pdftotext, including original OCR defects"
        }
      ]
    }
  ],
  "visual_checks": [
    {
      "file": "source-extracts/thuillier-regularization-111.png",
      "finding": "Printed page 97 confirms weights are -log norm and regularization increases norms/decreases weights. A preceding displayed curvature sign in the source is inconsistent with this convention; our sign is independently fixed by integration by parts."
    },
    {
      "file": "source-extracts/thuillier-energy-117.png",
      "finding": "Printed page 103, Proposition 3.5.7: mu - (integral mu) delta_x, g_x,mu in W^1, and g_x,mu in L^1(mu) are equivalent."
    },
    {
      "file": "source-extracts/thuillier-energy-118.png",
      "finding": "Printed page 104 contains energy equality and Proposition 3.5.9; retained as original-PDF evidence."
    },
    {
      "file": "source-extracts/ps-remark-35.png",
      "finding": "Printed/PDF page 35 is the continuous-operator/Remark 4.4 distinction; retained as original-PDF evidence."
    },
    {
      "file": "source-extracts/cd-continuity-207.png",
      "finding": "PDF page 207, Lemma 8.5.5 explicitly says toute fonction continue psh."
    }
  ],
  "limitations": "Hash matches and saved literal extracts prove file identity, not mathematical validity or completeness of a literature search."
}


## Literal published unit: 1201.0187-standing-and-compactness.txt

   Let us now turn to the non-Archimedean case. Fix a complete, discrete valuation field K
with valuation ring R and residue field k, and set S := Spec R. We assume that k (and hence
K) has characteristic zero, which means, concretely, that R is (non-uniquely) isomorphic to
k[[t]]. Let X be a smooth projective K-analytic space in the sense of Berkovich, so that X
is the analytification of a smooth projective K-variety by the GAGA principle. Recall that
the underlying topological space of X is compact Hausdorff. A model X of X is a normal
flat projective S-scheme together with an isomorphism of the analytification of its generic
fiber XK with X. Each line bundle L on X is (again, by GAGA) the analytification of a line
    1In fact, [CLD12] was posted after the first version of the present paper.
             SINGULAR SEMIPOSITIVE METRICS IN NON-ARCHIMEDEAN GEOMETRY                        3


bundle on XK (that we also denote by L), and a model metric is a metric k · kL on L that
is naturally induced by the choice of a Q-line bundle L ∈ Pic(X )Q such that L|XK = L in
Pic(XK )Q . A model function ϕ on X is a function such that e−ϕ is a model metric on the
trivial line bundle. The set D(X) of model functions is then dense in C 0 (X), a well-known
consequence of the Stone-Weierstrass theorem.
   Following S.-W.Zhang [Zha95, 3.1] (see also [KT, 6.2.1], [Gub98, 7.13], [CL06, 2.2]), we
shall say that a model metric k · kL on L is semipositive if L ∈ Pic(X )Q is nef on the special
fiber X0 of X , i.e. L · C ≥ 0 for all projective curves C in X0 . A continuous metric on L is
then semipositive in the sense of Zhang if it can be written as a uniform limit over X of a
sequence of semipositive model metrics. The reader may consult [CL11] for a nice survey
on these notions.
   In order to define a general notion of singular semipositive metrics, we use the finer
description of X as an inverse limit of dual complexes (called skeletons in Berkovich’s termi-
nology). Since the residue field k of R has characteristic zero, it follows from [Tem06] that
each model of X is dominated by a SNC model X , by which we understand a regular model
whose special fiber X0 has simple normal crossing support (plus a harmless irreducibility
condition that we impose for convenience). To each SNC model X corresponds its dual
complex ∆X , a compact simplicial complex which encodes the incidence properties of the
irreducible components of X0 . The dual complex ∆X embeds canonically in X and for the
purposes of this introduction we shall view ∆X as a compact subset of X. There is further-
more a retraction pX : X → ∆X . These maps are compatible with respect to domination of
models, and we thus get a map
                                         X → lim ∆X
                                               ←−
                                               X
which is known to be a homeomorphism (see, for instance, [KS06, p.77, Theorem 10]).
   Following the philosophy of [BGS95], we define the space of closed (1, 1)-forms on X as
the direct limit over all models X of X of the spaces N 1 (X /S) of codimension one numerical
equivalence classes. Any model metric gives rise to a curvature form lying in this space.
The main reason for working with numerical equivalence (instead of rational equivalence
as in [BGS95]) is that we can then adapt a result of [Kün96] to show that a line bundle
L ∈ Pic(X) has vanishing first Chern class c1 (L) ∈ N 1 (X) iff it admits a model metric with
zero curvature (cf. Corollary 4.4).
   Fix a reference model metric k · k on L with curvature form θ. Any other metric can be
written k · ke−ϕ for some function ϕ on X. When k · ke−ϕ is a semipositive model metric,
we say that the model function ϕ is θ-psh.
Definition. Let L be an ample line bundle on a smooth projective K-analytic variety X.
Fix a model metric k · k on L with curvature form θ. A θ-plurisubharmonic function on X
is then a function ϕ : X → [−∞, +∞) such that:
      • ϕ is upper semicontinuous (usc).
      • ϕ ≤ ϕ ◦ pX for each SNC model X .
      • ϕ is a uniform limit, on each dual complex ∆X , of θ-psh model functions.
A singular semipositive metric is a metric k · ke−ϕ with ϕ a θ-psh function.
  The consistency of the definition for model functions will be guaranteed by Theorem 5.11
below. Let ϕ be a θ-psh function. Since ϕ is usc and each ϕ ◦ pX is continuous, it follows
4              SÉBASTIEN BOUCKSOM, CHARLES FAVRE, AND MATTIAS JONSSON


immediately that S ϕ = inf X ϕ ◦ pX , so that ϕ is uniquely determined by its restriction to
the dense subset X ∆X of X. We may therefore endow the set PSH(X, θ) of all θ-psh
functions (or, equivalently, of all singular semipositive metrics on L) with the topology
of uniform convergence on dual complexes. We view this topology as an analogue of the
L1 -topology in the complex case. Our first main theorem shows that this space is indeed
compact modulo additive constants, something that was also announced in the unpublished
manuscript by Kontsevich and Tschinkel [KT].
Theorem A. Let L be an ample line bundle on a smooth projective K-analytic variety X
endowed with a model metric with curvature form θ. Then PSH(X, θ)/R is compact.
  In other words, the set of singular semipositive metrics on L modulo scaling is compact.
For curves, this result is a consequence of the work of Thuillier [Thu05], and follows from
basic properties of subharmonic functions on metrized graphs.
  Our second main result is the following analogue of Demailly’s global regularization the-
orem.
Theorem B. Let L be an ample line bundle on a smooth projective K-analytic variety X
endowed with a model metric with curvature form θ. Then every θ-psh function ϕ is the
pointwise limit on X of a decreasing net of θ-psh model functions.
   When dim X = 1, Theorem B is a special case of [Thu05, Théorème 3.4.19]. Thanks
to Dini’s lemma, Theorem B implies a non-Archimedean version of the Demailly-Richberg
theorem, stating that every continuous θ-psh function is a uniform limit over X of θ-psh
model functions. In other words, for continuous metrics our definition of semipositivity
agrees with Zhang’s.
   Let us briefly explain how Theorem A above is proved. The first important fact is that


## Literal published unit: 1201.0188-v1-theorem-and-curve-background.txt

K be a complete discrete valuation ﬁeld whose residue ﬁeld k has characteristic zero, so
that K ≃ k((t)). Let X be a smooth projective variety over K, and write n = dim X.
Thanks to the non-Archimedean GAGA principle, it is reasonable to also denote by X
the corresponding K-analytic space in the sense of Berkovich, whose underlying topological
space is compact Hausdorﬀ. A model of X is a normal scheme X that is ﬂat and projective
over S := Spec k[[t]], and whose generic ﬁber can be identiﬁed with X.
   Consider a ample line bundle L on X. A model metric on L is a metric deﬁned by a
extension L ∈ Pic(X )Q of L to some model X . Such a metric is called semipositive if L is
nef, i.e. has non-negative degree on all proper curves of the special ﬁber of X . S.-W. Zhang
introduced in [Zha95] the more ﬂexible notion of semipositive continuous metric as the
uniform limit of semipositive model metrics.1 In this context, A. Chambert-Loir [CL06]
deﬁned the Monge-Ampère measure c1 (L, k · k)n of a semipositive continuous metric k · k on
L. It is a positive Radon measure on X, of mass deg L.
   V. Berkovich constructed in [Ber99] the skeleton associated to a polystable model of X.
Since we are assuming K to have residue characteristic zero, it is easier to rely on resolution
of singularities and instead consider SNC models, i.e. models whose special ﬁber has simple
normal crossing support (but is not necessarily reduced, as opposed to a semistable model).
To each SNC model X is associated a dual complex ∆X that encodes the combinatorics of
the intersections of the components of the special ﬁber, and which embeds in the Berkovich
space X just as skeletons do. Any ﬁnite set  S of divisorial points is contained in the dual
complex of some SNC model; in particular X ∆X is dense in X.
   We can now state our main result. We say that X is algebraizable if there exists a (one-
variable) function ﬁeld F admitting K as a completion and a smooth projective F -scheme
Y such that X = YK .
Theorem A. Let K be a complete discrete valuation field of residue characteristic zero. Let
X be a smooth projective K-variety that is algebraizable. Let L ∈ Pic(X) be an ample line
    1We refer to Table 1 in §2.6 below for a comparison of our terminology with existing terminology.
               SOLUTION TO A NON-ARCHIMEDEAN MONGE-AMPÈRE EQUATION                          3

bundle and µ be a positive Radon measure on X of mass c1 (L)n . If we further assume that
µ is supported on the dual complex of some SNC model of X, then there exists a continuous,
semipositive metric k · k on L such that
                                   c1 (L, k · k)dim X = µ .                              (1.1)
This metric is furthermore unique up to a multiplicative constant.
  Even though the result is most likely true without this assumption, the algebraizability
condition plays an essential role in our proof, as we shall explain below. Note that the line
bundle L is not assumed to be deﬁned over a function ﬁeld.
   The uniqueness part in Theorem A follows from a result of X. Yuan and S.-W. Zhang
[YZ10] asserting more generally that a continuous semipositive metric k · k is uniquely de-
termined up to a constant by its Monge-Ampère measure. Their proof is inspired by the
one given by Blocki [Blo03] in the complex setting.
   Our approach does not give any information on the regularity of the metric besides con-
tinuity. It would be interesting to further investigate this issue, for instance when µ is
supported on ﬁnitely many divisorial points. We refer to §9 for a discussion of this problem
in the case of toric varieties, based on the recent work [BPS11].
   Versions of Theorem A are already known in a few cases. For curves (and in fact over any
complete non-Archimedean, non-trivially valued ﬁeld), it can easily be deduced from results
of A. Thuillier [Thu05], who developed a theory of singular semipositive metrics on analytic
curves that is completely analogous to the complex case. Solving (1.1) for curves boils down
to a system of linear equations and relies on the negativity of the intersection form of the
special ﬁber of a suitable model, see §9. Alternatively, one can exploit the structure of the
Berkovich space as a metrized graph as in [BR10, FJ04].
   In higher dimensions, Y. Liu [Liu10] treated the related case when X is a totally degener-
ate abelian variety over Cp , and µ is a (smooth) measure supported on the dual complex of
the canonical formal model of X, as constructed by Mumford. By exploiting the fact that
this dual complex is a compact (real) torus, one can translate the equation c1 (L, k · k)n = µ
into a (real) Monge-Ampère equation on this real torus, and apply Yau’s result to its com-
plexiﬁcation to obtain the metric.
   A statement very close to Theorem A also appears in an unpublished set of notes by M.
Kontsevich and Y. Tschinkel [KT00] dating from 2001, where the authors propose a detailed
strategy of proof in the case µ is a Dirac mass at a divisorial point. Several ingredients in
their approach also appear in our paper (see Remark 8.7 below).
   We are now going to present an outline of our proof of Theorem A, which consists in
mimicking as far as possible the variational approach to complex Monge-Ampère equations
of [BBGZ09] and the C 0 -estimates of [Kol98]. To that end we will rephrase Theorem A in
a more analytic language. Let us thus recall the notion of quasi-plurisubharmonic function
that we developed in [BFJ11] and its main properties.
   As a variant of [BGS95] we ﬁrst deﬁne the space of closed (1, 1)-forms on X as the direct
limit
                                 Z 1,1 (X) := lim N 1 (X /S),


## Literal published unit: 1801.08229-trivial-valuation-calabi-yau.txt

Functions and measures of finite energy. Let k be an arbitrary algebraically closed
field, and X an irreducible1 projective variety over k, with function field k(X). In order to
describe more precisely our main results, recall first that the Berkovich analytification X an
of X with respect to the trivial valuation on k is a compactification of the space X val of
valuations v : k(X)× → R, trivial on k, endowed with the topology of pointwise convergence.
Points of X an can be understood as semivaluations v on X, i.e. valuations v ∈ Y val for some
subvariety Y ⊂ X. The set X div ⊂ X val of divisorial valuations, which are attached to
prime divisors over X, is dense in X an .
   For every v ∈ X an and every section s ∈ H0 (X, mL), m ∈ N, we can make sense of
v(s) ∈ [0, +∞] by trivializing L at the center of v. Setting |s|(v) := exp(−v(s)) defines a
continuous function |s| : X an → [0, 1], and the topology of X an is in fact defined by the set
of such functions. Building on these, we introduce the following classes of functions on X an :
      • Fubini–Study functions for L are continuous functions ϕ : X an → R of the form

                                     ϕ = m−1 max{log |si | + λi },
                                                   i

         where (si ) is a finite set in H0 (X, mL) without common zeroes and λi ∈ Q. This
         defines a subset H = H(L) of C0 (X) := C0 (X an , R), and we show that the map
         (X , L) 7→ ϕL alluded to above sets up a 1–1 correspondence between H(L) and the
         set of ample, integrally closed test configurations (X , L) for (X, L) (see §1.4 for the
         definition when X is not normal).
      • piecewise linear (PL) functions on X an are elements of the Q-linear subspace PL(X)
        of C0 (X) spanned by H = H(L); this subspace turns out to be independent of L,
        and is dense in C0 (X). In the present setting, PL functions play the role of smooth
        functions from the complex analytic case. It is proved in Appendix A that PL
        functions are induced by usual piecewise linear functions on dual complexes of snc
        test configurations, when X is smooth and char k = 0.
      • L-psh functions are usc functions ϕ : X an → R∪{−∞}, not identically −∞, that can
        be obtained as limits of decreasing nets in H(L). The set PSH = PSH(L) of L-psh
        functions is stable under addition of a real constant, finite maxima, decreasing limits,
        and is the smallest such class of functions that contains all functions of the form
        m−1 log |s|, s ∈ H0 (X, mL) \ {0}. It follows from Dini’s lemma that C0 (X) ∩ PSH
        is the closure of H in the topology of uniform convergence. We prove that the
        restriction of an L-psh function ϕ to X div is finite-valued, and determines ϕ. We
        endow the set PSH with the topology of pointwise convergence on X div .
In the main body of the text, we actually work with ω-psh functions, where ω ∈ N1 (X) is
any (real) ample (and sometimes even arbitrary) numerical class on X. However, here we
will stick to the above setting, for simplicity.
   As in [BHJ17], the Monge–Ampère energy E : H → R is defined on ϕ ∈ H as the normal-
ized intersection number (or height)
                                                        (L̄n+1 )
                                           E(ϕ) :=               ,
                                                       (n + 1)V

   1While the main body of the article deals with possibly reducible varieties, we assume here for simplicity
that X is irreducible.
4                       SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

where n = dim X, V = (Ln ), and (X̄ , L̄) → P1 is the canonical Gm -equivariant compactifi-
cation of the ample, integrally closed test configuration (X , L) → A1 that represents ϕ. The
above normalization ensures that E(ϕ + c) = E(ϕ) + c for c ∈ Q.
   Adapting to our setting the original approach of [CL06, Gub10], we also attach to ϕ its
Monge–Ampère measure MA(ϕ), a Radon probability measure on X an with finite support
in X div , defined using intersection numbers computed on X0 . We then have
                                                   ˆ
                          d
                                E((1 − t)ϕ + tψ) =       (ψ − ϕ) MA(ϕ)
                         dt t=0                     X an
for all ψ ∈ H, and this actually characterizes the measure MA(ϕ), since H spans the dense
subset PL(X) ⊂ C0 (X).
   This formula shows that E is increasing on H, and we canonically extend it by mono-
tonicity to a usc functional E : PSH → R ∪ {−∞}, continuous along decreasing nets. We
denote by
                                E 1 := {ϕ ∈ PSH | E(ϕ) > −∞}
the set of L-psh functions of finite energy. Thus ϕ ∈ E 1 iff ϕ : X an → R ∪ {−∞} is a
decreasing limit of functions ϕi ∈ H with E(ϕi ) bounded. Note that the complex analytic
analogue of E 1 has been well studied, see [GZ07, BBGZ13, BBE+16, Dar15, DDL18].
   The weak topology of E 1 is the subset topology from PSH (i.e. the topology of pointwise
convergence on X div ), and the strong topology is the coarsest refinement of the weak topology
that makes E : E 1 → R continuous. Decreasing nets in E 1 are strongly convergent, and H is
thus strongly dense in E 1 .
   As in [BBGZ13], we dually introduce an energy functional E∨ : M → [0, +∞] on the space
M of Radon probability measures µ on X an , by setting
                                          ˆ                        ˆ    
                   ∨
                  E (µ) := sup E(ϕ) − ϕ µ = sup E(ϕ) − ϕ µ ,
                            ϕ∈H                      ϕ∈E 1

where the right-hand equality follows from a simple approximation argument. Thus E∨ is
convex, and lsc with respect to the usual weak topology of M. The space
                               M1 := µ ∈ M | E∨ (µ) < ∞
                                      

of measures of finite energy has a weak topology inherited from M, and a strong topology,
defined as the coarsest refinement of the weak topology for which E∨ becomes continuous.
In contrast to E 1 , we prove that both M1 and its strong topology
                                                             ´     are independent of L.
   For any two ϕ, ϕ ∈ H, we further have E(ϕ) − E(ϕ ) ≥ (ϕ − ϕ0 ) MA(ϕ), a reflection
                      0                                 0

of the concavity of E. This precisely means that ϕ computes the supremum defining the
energy of MA(ϕ), which thus lies in M1 .
   The main contribution of the present article can be summarized as follows.
Theorem A. The Monge–Ampère operator MA : H → M1 admits a unique continuous
extension MA : E 1 → M1 , where both sides are equipped with the strong topology.
   It further induces a topological embedding with dense image E 1 /R ,→ M1 , which is onto
if X is smooth, and either char k = 0 or dim X ≤ 2.
  Theorem A can be viewed as a trivially valued analogue of the main result of [BBGZ13],
which itself is a version of the celebrated result of Yau [Yau78] and a later version by
Kolodziej [Kol98]. In the non-Archimedean setting, earlier results include [Liu11, BFJ15,
YZ17].


## Literal published unit: 1805.01016-continuous-energy.txt

9.3. Monge–Ampère energy. In this section, X is geometrically reduced, and L is a
semiample Q-line bundle on X. Since L is in particular nef, we have
                                          V := vol(L) = (Ln ),
by Corollary 9.10.
Definition 9.13. Let φ, ψ be continuous psh metrics on L. We define the relative Monge–
Ampère energy7of φ, ψ as
                                   n Z
                              1 X
                 E(φ, ψ) :=            (φ − ψ)(ddc φ)j ∧ (ddc ψ)n−j ∧ δX .        (9.11)
                            n+1
                                         j=0

   Recall that φ − ψ is a continuous function on X an , which may thus be integrated against
each positive Radon measure (ddc φ)j ∧ (ddc ψ)n−j ∧ δX . By (8.9), we have
                                          1                       
                             E(φ, ψ) =          hφn+1 i − hψ n+1 i .                  (9.12)
                                        n+1
Given a continuous psh metric ψ, the functional φ 7→ E(φ, ψ) is characterized as the unique
antiderivative of the Monge–Ampère operator φ 7→ (ddc φ)n that vanishes at ψ, in the sense
that                                                Z
                      d                     ′
                             E((1 − t)φ + tφ , ψ) =        (φ′ − φ)(ddc φ)n           (9.13)
                      dt t=0                          X an
for any two continuous psh metrics φ, φ′ , see [BJ18a, §3.8].
Proposition 9.14. The Monge–Ampère energy satisfies the following properties.
    (i) cocycle formula: E(φ1 , φ2 ) + E(φ2 , φ3 ) + E(φ3 , φ1 ) = 0;
   (ii) monotonicity: φ ≤ φ′ =⇒ E(φ, ψ) ≤ E(φ′ , ψ);
  (iii) scaling: E(φ + c, ψ) = E(φ, ψ) + V c for c ∈ R;
  (iv) homogeneity: E(aφ, aψ) = an+1 E(φ, ψ) for a ∈ Z>0 .
   (v) Lipschitz continuity:
                                                                             
                    E(φ, ψ) − E(φ′ , ψ ′ ) ≤ V sup |φ − φ′ | + sup |ψ − ψ ′ | .
     (vi) for each complete field extension F/K we have
                                         E(φF , ψF ) = E(φ, ψ).
     7Note that the present normalization, which is more convenient for the purpose of this paper, is not
uniform accross the literature.
                NORMS, DETERMINANT OF COHOMOLOGY AND FEKETE POINTS                             75

  (vii) birational invariance: for any projective birational morphism µ : X ′ → X we have
                                    E(µ⋆ φ, µ⋆ ψ) = E(φ, ψ).
Proof. (i) follows from (9.13), and (ii)— (iv) follow directly from (9.11), using that
                           Z
                             (ddc φ)j ∧ (ddc ψ)n−j ∧ δX = (Ln ) = V.

(v) is a formal consequence of (ii) and (ii), and (vi) follows from (9.11) and the compatibility
of mixed Monge–Ampère measures with ground field extension, cf. Proposition 8.3. Finally,
(vii) is a consequence of (9.11) and the projection formula µ⋆ δX ′ = δX .                    
9.4. Proof of Theorem A. The following result corresponds to Theorem A in the intro-
duction. It was first established in [BB10] when K is Archimedean, and in [BG+16] when
K is discretely valued.
Theorem 9.15. Let X be a geometrically reduced projective K-scheme, and L be a semi-


## Literal published unit: 1805.01016-continuous-ma-proof.txt

                 p⋆ (ddc φ1,F ∧ . . . ∧ ddc φn,F ∧ δXF ) = ddc φ1 ∧ . . . ∧ ddc φn ∧ δX ,
         where φi,F is the pullback of φi to Li,F and p : XFan → X an is the canonical projection.
Proof. (i) is straightforward. (ii) is classical in the Archimedean case, and proved in [CLD12,
Proposition 6.4.3] in the non-Archimedean case. (iii) is a consequence of the Stokes formula
(see [CLD12, Théorème 3.12.2] in the non-Archimedean case). In the Archimedean case, (iv)
is nontrivial only when K = R, F = C, in which case it holds by definition (see Remark 8.1).
In the non-Archimedean case, it is implicit in [CLD12], and can be checked as follows. Pick
a smooth, compactly supported function f on X an , and consider the smooth, compactly
supported (n, n)-form α := f ddc φ1 ∧ . . . ∧ ddc φn . According to [Gub16, Proposition 5.13],
there exists a Zariski open subset U ⊂ X with a closed embedding U ֒→ Grm,K and a
compactly supported smooth (n, n)-superform on Rr such that α is obtained by pulling-
back η by the tropicalization map Trop : U an → Rr , and
                             Z                                  Z
                                      c              c
                                f dd φ1 ∧ · · · ∧ dd φn ∧ δX =     α
                                                                          X
is defined as the integral of η on the tropical cycle Trop(U ). Unravelling the definitions, it
is clear that the pull-back αF of α to XFan is simply the pull-back of η by the tropicalization
map TropF : UFan → Rr . The construction of the tropical cycle of an algebraic variety being
invariant under ground field extension,
                                  R       Rwe have TropF (UF ) = Trop(U ) as tropical cycles,
and we conclude as desired that X α = XF αF .                                                 
   Recall from §7.3 that a continuous metric on a Q-line bundle L is psh-regularizable iff it is
a uniform limit of smooth semipositive metrics on L. If L is semiample, then any continuous
psh metric (in the sense of Definition 7.2, i.e. a uniform limit of Fubini–Study metrics) is
psh-regularizable, by Theorem 7.14.
Theorem 8.4. Let L1 , . . . , Ln be Q-line bundles on X. The measure-valued operator
                             (φ1 , . . . , φn ) 7→ ddc φ1 ∧ . . . ∧ ddc φn ∧ δX ,
defined so far on smooth metrics, admits a unique continuous extension to tuples of contin-
uous, psh-regularizable metrics on the Li , with respect to uniform convergence for tuples of
metrics, and the weak topology on Radon measures.
     As a direct consequence of Proposition 8.3, we get:
Proposition 8.5. For each tuple of continuous, psh-regularizable metrics (φi ),
                                            X
             ddc φ1 ∧ . . . ∧ ddc φn ∧ δX =   mα ddc φ1 ∧ . . . ∧ ddc φn ∧ δXα
                                                     α

is a positive Radon measure on X an , of total mass (L1 · . . . · Ln ). It is further symmetric
and multiadditive as a function of the φi .
                    NORMS, DETERMINANT OF COHOMOLOGY AND FEKETE POINTS                                          57

   Theorem 8.4 follows from the classical Bedford–Taylor theory [BT76] in the Archimedean
case, and from its analogue in the non-Archimedean case [CLD12, Corollaire 5.6.5]. In the
present global setting, one can however provide a simple direct argument, based on the
following global version of the classical Chern–Levine–Nirenberg inequality that will be put
to use again a bit later.
Lemma 8.6. Let L0 , . . . , Ln be line bundles on X, and suppose given a pair of smooth,
semipositive metrics φi , φ′i on each Li . Then
       Z                                            Z
          (φ0 − φ′0 ) ddc φ1 ∧ . . . ∧ ddc φn ∧ δX − (φ0 − φ′0 ) ddc φ′1 ∧ . . . ∧ ddc φ′n ∧ δX

                                                  n
                                                  X
                                           ≤C           sup |φi − φ′i |
                                                  i=1

with C := 2 max1≤i≤n (L0 · L1 · . . . · Lbi · . . . · Ln ).
Proof. For brevity of notation, set T := ddc φ2 ∧ . . . ∧ ddc φn ∧ δX . By (8.2),
       Z                         Z                          Z
         (φ0 − φ′0 ) ddc φ1 ∧ T − (φ0 − φ′0 ) ddc φ′1 ∧ T = (φ0 − φ′0 ) ddc (φ1 − φ′1 ) ∧ T
          Z                                       Z                              Z
      =       (φ1 − φ′1 ) ddc (φ0 − φ′0 ) ∧ T =       (φ1 − φ′1 ) ddc φ0 ∧ T +       (φ1 − φ′1 ) ddc φ′0 ∧ T.

Since ddc φ0 ∧ T and ddc φ′0 ∧ T are both positive measures of mass (L0 · L2 · . . . · Ln ), we infer
     Z                          Z
       (φ0 − φ0 ) dd φ1 ∧ T − (φ0 − φ′0 ) ddc φ′1 ∧ T ≤ 2(L0 · L2 · . . . · Ln ) sup |φ1 − φ′1 |.
                ′   c


We conclude by symmetry and multilinearity.                                                                     
Proof of Theorem 8.4. Assume first that K is non-Archimedean, and pick f ∈ PLR (X an ).
By Lemma 5.17, we can find a pair of Fubini–Study metrics on an ample line bundle L0 such
that f = φ0 − φ′0 . By Theorem 7.14, φ0 and φ′0 are uniform limits of smooth, semipositive
metrics on L0 . Lemma 8.6 thus shows that
                                             Z
                        (φ1 , . . . , φn ) 7→ f ddc φ1 ∧ . . . ∧ ddc φn ∧ δX

is Lipschitz continuous with respect to the supnorm on tuples of smooth, semipositive met-
rics (with Lipschitz constant depending on f ), and hence extends continuously to tuples of
continuous, psh-regularizable metrics. For eachR tuple of continuous, psh-regularizable met-
rics (φi ), the linear form on PLR (X an ) f 7→ f ddc φ1 ∧ . . . ∧ ddc φn ∧ δX is positive, hence
continuous, and it thus extends to a positive linear form on C0 (X), by density of PLR (X an ).
   In the Archimedean case, the argument is similar, arguing with a smooth function f
instead. It is in fact even simpler, since f can directly be written as a difference of smooth
psh metrics on some ample line bundle.                                                         
   In order to exploit the multilinearity of the previous construction, it is convenient to
introduce the following terminology.
Definition 8.7. We say that a continuous metric φ on a line bundle L is dpsh if it can be
written as a difference of continuous, psh-regularizable metrics.
58                        SÉBASTIEN BOUCKSOM AND DENNIS ERIKSSON

     A dpsh metric is thus the same as an approachable metric in the sense of [CLD12, §6.3].
Lemma 8.8. Every line bundle L admits a smooth, dpsh metric.
Proof. By Theorem 7.14, any ample line bundle admits a smooth, semipositive metric, and
the result follows since L can be written as a difference of ample line bundles.      
Example 8.9. If K is Archimedean, every smooth metric is dpsh.
   While this is probably true in the non-Archimedean case as well, it is less obvious, since
strictly positive (1, 1)-forms do not exist globally in this context.
Example 8.10. If K is non-Archimedean, every R-PL metric is dpsh, by Lemma 5.17.
   The operator (φ1 , . . . , φn ) 7→ ddc φ1 ∧. . .∧ddc φn ∧δX , being symmetric and multiadditive on
tuples of continuous, psh-regularizable metrics, extends to a symmetric, multilinear operator
on continuous dpsh metrics, with values in signed Radon measure. Note that Proposition 8.3
still holds for such metrics.
Example 8.11. If K is non-Archimedean and φ1 , . . . φn are R-PL metrics, then ddc φ1 ∧. . .∧
ddc φn ∧ δX has finite support. By ground field invariance, we may indeed assume that K is
algebraically closed, and that its value group is large enough to ensure that the φi become pure
after base change. By Proposition 5.16, φ1 , . . . , φn are then induced by Q-models L1 , . . . , Ln
of L1 , . . . , Ln determined on a projective model X of X. By linearity with respect to the
fundamental class [X], we may further assume that X is (geometrically) irreducible, which
allows us to assume that Xs is reduced, by Theorem 4.20. Each irreducible component Y of
Xs then determines a unique Shilov point xY ∈ Γ(X ), and
                                                       X
                        ddc φ1 ∧ . . . ∧ ddc φn ∧ δX =  (L1 |Y · . . . · Ln |Y )δxY ,         (8.3)
                                                    Y
by [CLD12, Proposition 6.9.2] (compare [Gub07, Proposition 3.11]).
8.2. A Poincaré–Lelong formula. We start with the following integrability result.
Theorem 8.12. Let φ1 , . . . , φn be continuous, psh-regularizable metrics on line bundles
L1 , . . . , Ln , and let s ∈ H0 (X, L) be a regular section of a line bundle L, equiped with any
continuous metric φ. Then log |s|φ is integrable with respect to ddc φ1 ∧ . . . ∧ ddc φn ∧ δX , and
                                  Z
                                     log |s|φ ddc φ1 ∧ . . . ∧ ddc φn ∧ δX


## Literal published unit: 1805.01016-continuous-psh-and-nef.txt

   Given a subgroup Γ ⊂ R, nontrivial if K is trivially valued, FSΓ (L) is dense in FS(L)
with respect to uniform convergence, by Proposition 5.4 (v); it would thus be equivalent to
require φi ∈ FSΓ (L) in the above definition.
  As a direct consequence of Corollary 5.7, we have:
Lemma 7.3. Let A be the Stein factorization of L. Then
                               PSH(A) ≃ PSH(L) ≃ PSH(Lred ).
   The following general result, borrowed from [BJ18a, Proposition 5.6], ensures that PSH(L)
is closed under decreasing limits.
Lemma 7.4. Let F ⊂ C0 (L) be a family of continuous metrics on a Q-line bundle L, closed
under addition of a constant, and define Fe as the set of possibly singular metrics on L that
can be written as decreasing limits of nets in F. Then Fe is closed under decreasing limits.
                                           e For each i ∈ I choose a decreasing net (φi,j )j∈J
Proof. Let (φi )i∈I be a decreasing net in F.                                                  i
in F converging to φi . Let A be the set of triples α = (i, j, m) with i ∈ I, j ∈ Ji and
m ∈ Z>0 . For each α = (i, j, m) in A, set
                                     ψα := φi,j + m−1 ∈ F,
and define a partial order on A by
                                     α ≥ α′ ⇐⇒ ψα ≤ ψα′ .
We claim that A is directed, i.e. any two elements a1 = (i1 , j1 , m1 ), a2 = (i2 , j2 , m2 ) in
A can be dominated by a third. To see this, first pick i ≥ i1 , i2 , so that φi ≤ φi1 and
φi ≤ φi2 , and set m := max{m1 , m2 } + 1. A simple variant of Dini’s lemma shows that
φi,j + m−1 ≤ φik ,jk + m−1
                         k = ψak on X
                                       an for k = 1, 2 and all j ∈ J large enough, which
                                                                      i
proves the claim. By construction, (ψα )α∈A is a decreasing net in F such that ψα → φ
                                  e
pointwise on X an , and hence φ ∈ F.                                                          
Corollary 7.5. The space PSH(L) is stable under finite max and decreasing limits.
Corollary 7.6. Pick a subgroup Γ ⊂ R, nontrivial if K is trivially valued. For any semi-
ample Q-line bundle L, the set C0 ∩ PSH(L) of continuous psh metrics on L is the closure
of FSΓ (L) with respect to uniform convergence.
Proof. Let φ be a continuous psh metric, and pick a decreasing net (φi ) in FSΓ (L) converging
pointwise to φ. By Dini’s lemma, φi → φ uniformly on X an , and φ is thus in the closure
of FSΓ (L). Conversely, let (φi ) be a sequence in FSΓ (L) converging unifornly to some
(continuous) metric φ. We can inductively construct a sequence of constants ci → 0 such
that φi + ci is decreasing, and it follows that φ = limi (φi + ci ) is psh.                  
                NORMS, DETERMINANT OF COHOMOLOGY AND FEKETE POINTS                           49

7.2. Nef metrics. Assume that K is non-Archimedean. A model metric φ on a Q-line
bundle L is nef if φ = φL for some Q-model L of L which is nef, i.e. L · C ≥ 0 for each
e
K-projective  curve C ⊂ Xs . By [GM19, Proposition 3.5], any Q-model L′ of L such that
φ = φL′ is then also nef.
Definition 7.7. A nef metric on a Q-line bundle L is a continuous metric φ that can be
written as a uniform limit of nef model metrics.
   This is usually known as a semipositive metric in the sense of S.W. Zhang, cf. [GM19] for
a thorough discussion. When K is trivially valued, the trivial metric is the only nef metric.
Theorem 7.8. Assume that K is nontrivially valued, and let L be an ample Q-line bundle.
Then a continuous metric on L is nef iff it is psh (in the sense of Definition 7.2).
   A proof of this result is also sketched, in a slightly different language, in [CMor18, Remark
3.18]; we nevertheless provide a proof below, for completeness. By [GM19, Corollary 1.4],
we get:
Corollary 7.9. Let L be an ample Q-line bundle, and pick a Q-model L of L. Then φL is
psh iff L is nef.


## Literal published unit: 1805.01016-continuous-volume-and-curve-envelopes.txt

   Consider now an arbitrary complete valued field K, i.e. a field K complete with respect to
an absolute value. In the Archimedean case, K = R or C, by the Gelfand–Mazur theorem.
In the non-Archimedean case, the main examples are K = Qp , Cp , or fields of formal
Laurent series and their completed algebraic closure, but the trivially valued case is also
important for the study of K-stability (see [BJ18b]). Let X be a geometrically reduced
projective scheme over K, L be a line bundle on X, and φ, ψ be continuous metrics on
(the Berkovich analytification of) L. Building on a result of Chen and Maclean based on
Okounkov bodies [CMac15], we show the existence of the relative volume of φ, ψ
                                         n!
                      vol(L, φ, ψ) := lim     vol (k · kmφ , k · kmψ ) ∈ R,                     (0.3)
                                  m→∞ mn+1
cf. Theorem 9.8. The main result of the present paper is as follows.
Theorem A. Let X be a geometrically reduced projective scheme over any complete valued
field K, and φ, ψ be continuous psh2 metrics on an ample line bundle L over X. Then
                                        vol(L, φ, ψ) = E(φ, ψ).
   In the Archimedean case, it follows from results of Demailly that a continuous metric
on L is psh iff it is a uniform limit of Fubini–Study metrics (see Theorem 7.1). In the
non-Archimedean case, we use this as a definition, and prove compatibility with the more
common notion of semipositive metric in this context, due to S.W. Zhang and involving
nef models, when K is nontrivially valued. We also show that a continuous metric φ is
psh iff it becomes psh after ground field extension. The relative Monge–Ampère energy of
continuous psh metrics can still be defined by (0.2), the latter being understood in the sense
of Chamber-Loir and Ducros [CLD12] in the non-Archimedean sense.
   In the Archimedean case, Theorem A reduces to [BB10] after passing to a resolution of
singularities. In the discretely valued case, it was established in [BG+16, Theorem A]. The
main contribution of the present paper is thus to establish Theorem A for a densely valued,
non-Archimedean ground field K.
  1Note that the present normalization, which is more convenient for the purpose of this paper, is not
uniform accross the literature.
   2A shorthand for plurisubharmonic.
4                        SÉBASTIEN BOUCKSOM AND DENNIS ERIKSSON

   The psh envelope P(φ) of a continuous metric φ on L is defined as the pointwise supremum
of the family of all continuous psh metrics ψ on L such that ψ ≤ φ. We say that continuity
of envelopes holds for (X, L) if P(φ) is continuous (and hence psh) for each continuous metric
φ on L.
Corollary B. Assume that continuity of envelopes holds for (X, L). For any two continuous
metrics φ, ψ on L, we then have
                                 vol(L, φ, ψ) = E(P(φ), P(ψ)).
   In the Archimedean case, classical results in pluripotential imply that continuity of en-
velopes holds whenever X is normal, and Corollary B is indeed also a consequence of [BB10]
in that case.
   In the non-Archimedean case, we similarly expect continuity of envelopes to holds as soon
as X is normal. As of this writing, continuity of envelopes (and hence Corollary B) has been
established when X is smooth, and one of the following is satisfied:
      • X is a curve, as a consequence of A. Thuillier’s work [Thu05] (see [GJKM19]);
      • K is discretely or trivially valued, of residue characteristic 0 [BFJ16, BJ18a], building
        on multiplier ideals and the Nadel vanishing theorem;
      • K is discretely valued of characteristic p, (X, L) is defined over a function field
        of transcendence degree d, and resolution of singularities is assumed in dimension
        n + d [GJKM19], replacing multiplier ideals with test ideals.



## Literal published unit: 2209.04879-continuous-ma-and-unbounded-gap.txt

  In general, the mixed Monge-Ampère measure satisfies the following basic properties:
Proposition 4.2. [BE21, prop. 8.3] Let φi ∈ DFS(Li ) for i = 1, ..., n.
    • The pairing (φ1 , ..., φn ) 7→ MA(φ1 , ..., φn ) is symmetric and multilinear;
    • if φi ∈ FS(Li ) for
                      R all i, then MA(φ1 , ..., φn ) is a positive Radon measure;
    • the total mass X an MA(φ1 , ..., φn ) = (L1 · ... · Ln );
    • if L0 = L1 = OX and φ0 , φ1 ∈ DFS(X), then:
                    Z                           Z
                        φ0 MA(φ1 , ..., φn ) =      φ1 MA(φ0 , φ2 , ..., φn ).
                      X                           X
  The Monge-Ampère measure can then be extended by density to more general metrics:
Theorem 4.3. [BE21, thm. 8.4]
Let K be a complete valued field, X/K an n-dimensional projective scheme and L1 ,...,Ln
line bundles on X. Then the Monge-Ampère operator:
                             (φ1 , ..., φn ) 7→ ddc φ1 ∧ ... ∧ ddc φn
admits a unique extension to continuous psh metrics on the Li . The extension is further-
more continuous with respect to the topology of uniform convergence and the weak topology
of Radon measures.
Remark 4.4. While the class E 1 (X, L) of finite-energy psh metrics on L is defined over any
non-archimedean field K, it is unclear in general how to extend the Monge-Ampère operator
on the latter. Note however that in the case where K is discretely-valued of characteristic
zero, this extension was constructed in [BFJ16], and the trivially-valued case was handled
in [BJ22].
Remark 4.5. The Chambert-Loir - Ducros [CLD12] approach to pluripotential theory on
Berkovich spaces makes sense of the curvature current ddc φ of a continuous psh metric,
and its wedge products, in a spirit close to the work of Bedford-Taylor in the complex case.
Notably, [CLD12, thm. 6.9.3] states that the wedge product ddc φ1 ∧ ... ∧ ddc φn coincides
with the mixed Monge-Ampère measure as described in example 4.1 when φ1 ,..., φn are psh
model metrics, whence the notation.


## Literal published unit: 2307.01697-measure-completion-scope.txt

         composition with the Monge–Ampère operator respectively recover the Donaldson
         J-functional and the Mabuchi K-energy in the Kähler case, and their analogues in
         the non-Archimedean case;
       • show that coercivity of the free energy is an open condition with respect to the
         Kähler class.
The emphasis in this paper is on measures of finite energy, as opposed to potentials of finite
energy, that we do not seek to investigate here (see for instance [BFJ15, BoJ22a, Reb21,
DXZ23] in the non-Archimedean context).

The general setup. Throughout this paper, we work with a compact topological space X
equipped with the following data:
       • a dense linear subspace D ⊂ C0 (X) of test functions, containing all constants;
       • a vector space Z of closed (1, 1)-forms on X, endowed with a nice1 partial order,
         and a linear map ddc : D → Z vanishing on constants;
       • an integer n ≥ 1 (seen as the ‘dimension’ of X), and a nonzero n-linear symmetric
         map taking a tuple (θ1 , . . . , θn ) in Z to a signed Radon measure θ1 ∧ · · · ∧ θn on X,
         assumed to be positive for all θi ≥ 0, and such that each bilinear form
                                                   ˆ
                      D × D → R (φ, ψ) 7→ φ ddc ψ ∧ θ1 ∧ · · · ∧ θn−1                          (0.1)

         with θi ∈ Z is symmetric, and seminegative for θi ≥ 0.
We then introduce the Bott–Chern cohomology space
                                          HBC (X) := Z/ddc D,
and define the positive cone Pos(X) ⊂ HBC (X) as the interior2 of the image of the convex
cone
                                 Z+ := {θ ∈ Z | θ ≥ 0}.
This setup is primarily inspired by the case of a compact Kähler manifold X, where D is
the space of smooth functions, and Z the space of closed (1, 1)-forms. It also covers the
case of a projective Berkovich space X over a complete non-Archimedean field k, where D
is generated by piecewise linear (or model ) functions, and elements of Z are represented by
numerical classes on models over the valuation ring (or test configurations, in the trivially
valued case) [BFJ16a, GM16, BoJ22a]. At least under reasonable assumptions on X and k,
we then have HBC (X) = N1 (X), and Pos(X) coincides with the ample cone, see §1.3.2.

Measures
    ´     of finite energy. Fix a form ω ∈ Z+ such that [ω] ∈ Pos(X), with volume
Vω = ω n > 0. The space of ω-plurisubharmonic test functions is defined as
                                Dω := {φ ∈ D | ωφ := ω + ddc φ ≥ 0},
and the Monge–Ampère operator takes φ ∈ Dω to the probability measure
                                          MAω (φ) := Vω−1 ωφn .

    1See §1.1 for the terminology.
    2Here we use the finest vector space topology of H
                                                         BC (X), see §1.1.
                                  MEASURES OF FINITE ENERGY                                          3

It admits a primitive, the Monge–Ampère energy Eω : Dω → R, explicitly given by
                                         n      ˆ
                                     1 X −1
                           Eω (φ) =        Vω     φ ωφj ∧ ω n−j .
                                    n+1
                                              j=0

Denote by M the space of (Radon) probability measures on X, and define the energy of a
measure µ ∈ M as the Legendre transform3
                                             ˆ
                      Jω (µ) := sup {Eω (φ) − φ µ} ∈ [0, +∞].
                                     φ∈Dω

Then Jω : M → [0, +∞] is convex, and lsc in the weak topology; the space of measures of
finite energy is defined as
                                  M1ω := {µ ∈ M | Jω (µ) < ∞},
equipped with the strong topology, i.e. the coarsest refinement of the weak topology in which
Jω becomes continuous.
   As a consequence of the seminegativity of (0.1), the functional Eω is concave. This is
equivalent to the non-negativity of the Dirichlet functional
                                                     ˆ
                       Jω (φ, ψ) := Eω (φ) − Eω (ψ) + (ψ − φ) MAω (φ),

which is more explicitly given by the familiar expression
                                           ˆ
                                         1
                             Jω (φ, ψ) =     (φ − ψ)ddc (ψ − φ)
                                         2
when n = 1, and a positive linear combination of integrals of the form
                     ˆ
                       (φ − ψ)ddc (ψ − φ) ∧ ωφj ∧ ωψn−j−1 (0 ≤ j < n)

in general, see (1.31). Our first main result shows that the Dirichlet functional induces, via
the Monge–Ampère operator, a complete quasi-metric4 space structure on M1ω .
Theorem A. Assume that ω has the orthogonality property. Then:
   (i) the image of the Monge–Ampère operator MAω : Dω → M is a dense subspace of
       M1ω ;
  (ii) there exists a unique (continuous) quasi-metric δω on M1ω that defines the strong
       topology of M1ω and such that
                                δω (MAω (φ), MAω (ψ)) = Jω (φ, ψ)
        for all φ, ψ ∈ Dω ;
  (iii) the quasi-metric space (M1ω , δω ) is complete.
  The energy can be expressed in terms of the quasi-metric as
                    Jω (µ) = δω (µ, µω )    where   µω := Vω−1 ω n = MAω (0).
We refer to Definition 2.15 for the precise definition of the orthogonality property. Suf-
fice it to say here that it only depends on [ω] ∈ Pos(X), and holds when X is a com-
pact Kähler manifold, or any projective Berkovich space X over a non-Archimedean field
(as a consequence of [BE21, BGM22]). In the former case, Theorem A can be deduced
  3This corresponds to E∨ (µ) in the notation of [BBGZ13, BoJ22a], and to ∥µ∥ in that of [BoJ22b].
                          ω                                                  ω
  4See §1.1 for the notion of quasi-metric used in this paper.
4                       SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

from [BBGZ13, BBEGZ19]; in the latter, it was established in the trivially valued case
in [BoJ22a], and is thus extended here to the case of an arbitrary non-Archimedean ground
field.
   The strategy of proof of Theorem A follows the same lines as the trivially case treated
in [BoJ22a]. The first key ingredient is a uniform differentiability property for the Legendre
transform of the convex functional µ 7→ Jω (µ), which is shown to be equivalent to the
orthogonality property. This is used to prove that if (φi ) is a maximizing sequence for a
given µ ∈ M1ω (i.e. a sequence in Dω computing the supremum that defines Jω (µ)), then
MAω (φi ) converges to µ.
   The rest of the proof relies on an extensive use of Hölder estimates for mixed Monge–
Ampère integrals, obtained from repeated applications of the Cauchy–Schwarz inequality
to the seminegative form (0.1). This approach, which goes back to [Blo03] and was further


## Literal published unit: 2307.01697-measure-quasimetric-proof.txt

compact Kähler manifold, and for any projective Berkovich space.
Theorem 2.24. There exists a unique continuous functional
                                         δω : M1ω × M1ω → R≥0 ,
such that
                             δω (MAω (φ), MAω (ψ)) = Jω (φ, ψ)                                          (2.21)
for all φ, ψ ∈ Dω . Furthermore:
    (i) for all µ ∈ M1ω and ψ ∈ Dω we have
                          δω (µ, MAω (ψ)) = Jω (µ, ψ),             δω (µ, µω ) = Jω (µ);                (2.22)
     (ii) δω is a quasi-metric: for all µ, ν, ρ ∈ M1ω we have
       δω (µ, ν) = 0 ⇔ µ = ν,      δω (µ, ν) ≈ δω (ν, µ),          δω (µ, ν) ≲ δω (µ, ρ) + δω (ρ, ν);   (2.23)
     (iii) the quasi-metric δω satisfies the Hölder continuity property
                      δω (µ, ν) − δω (µ′ , ν ′ ) ≲ max{δω (µ, µ′ ), δω (ν, ν ′ )}α R1−α                 (2.24)
         for all R > 0 and µ, µ′ , ν, ν ′ ∈ M1ω,R , with α := 2−n ;
                                 MEASURES OF FINITE ENERGY                                   25

   (iv) for all R > 0 and φ, ψ ∈ Dω,R , µ, ν ∈ M1ω,R , we have the Hölder estimate
                      ˆ
                        (φ − ψ)(µ − ν) ≲ Jω (φ, ψ)α δω (µ, ν)1/2 R1/2−α .               (2.25)

  We call δω the Dirichlet quasi-metric of M1ω .
Lemma 2.25. For all µ ∈ M1ω,R and φ, ψ, τ ∈ Dω,R , we have

               |Jω (µ, φ) − Jω (MAω (τ ), ψ)| ≲ max{Jω (µ, τ ), Jω (φ, ψ)}α R1−α ;      (2.26)
                   ˆ
                     (φ − ψ)(µ − MAω (τ )) ≲ Jω (φ, ψ)α Jω (µ, τ )1/2 R1/2−α .          (2.27)

Proof. When µ lies in the image of MAω : Dω → M1ω this is equivalent to (1.38) and (1.37), in
view of (2.5) and (2.6). By Theorem 2.23 the image of MAω is dense in M1ω , and the general
case thus follows by continuity in the strong topology of all functions of µ involved.     □

Proof of Theorem 2.24. Uniqueness is clear, since (2.21) determines δω on the image of
MAω : Dω → M1ω , which is dense in the strong topology, by Theorem 2.23. To show exis-
tence, pick µ, ν ∈ M1ω , and choose a maximizing sequences (ψi ) for ν. We can then find
R > 0 such that µ ∈ M1ω,R and ψi ∈ Dω,R for all i, and (2.26) and (2.7) yield

                 |Jω (µ, ψi ) − Jω (µ, ψj )| ≲ Jω (ψi , ψj )α R1−α
                                           ≲ max{Jω (ν, ψi ), Jω (ν, ψj )}α R1−α .
This estimate implies that (Jω (µ, ψi )) is a Cauchy sequence, which thus admits a limit
                                    δω (µ, ν) := lim Jω (µ, ψi ).                       (2.28)
                                                   i

The same estimate also shows that the limit is independent of the choice of maximizing
sequence (ψi ), and that the convergence in (2.28) is uniform with respect to µ ∈ M1ω,R . As
a consequence, µ 7→ δω (µ, ν) so defined is continuous on M1ω for each ν ∈ M1ω .
   By construction, (2.22) holds, and hence also (2.21), by (2.5). This proves (i).
   Next, (2.24) holds when ν, ν ′ lie in the image of MAω : Dω → M1ω , by applying (2.26) to
a maximizing sequence for µ′ , and the general case follows by using maximizing sequences
for ν, ν ′ . This shows (iii), which also yields the continuity of δω on M1ω × M1ω (and hence
conclude the proof of existence), since µi → µ strongly implies δω (µi , µ) → δω (µ, µ) = 0, by
continuity of δω (·, µ).
   Similarly, (iv) follows follows by applying (2.27) to a maximizing sequence (τi ) for ν.
   Finally, the first point in (ii) follows from (2.25), since Dω spans the dense subspace D of
  0
C (X) (see Corollary 1.13). By (1.34) and (1.35), the last two properties in (ii) hold when
the measures lie in the image of MAω , and hence in general, by continuity of δω .
                                                                                              □

  We next show:


## Literal published unit: 2307.01697-orthogonality-and-density-proof.txt

                                                                   e ω (f ) − Eω (φ) + t2 A sup |g|.

Since any φ ∈ Dω,<f large enough is greater then f + − sup f − , it satisfies
                               0 ≤ g = f − φ ≤ sup f − − f − ≤ B
with B only depending on f . We infer 0 ≤ tL ≤ t2 AB. Dividing by t > 0 and letting t → 0+
yields, as desired, L = 0. This proves (iii)⇒(i).                                        □
Example 2.20. Assume X is a projective Berkovich space over a non-Archimedean field.
Then [BE21, Theorem A] combined with the uniform differentiability estimate of [BGM22,
Lemma 3.2] shows that (2.18) is satisfied (compare [BoJ22a, Lemma 8.7]). By Proposi-
tion 2.19, it follows that the orthogonality property always holds in this setting.
2.5. Maximizing sequences.
                                                                                  1
Definition 2.21. We say that a sequence (ψ     ´ i ) in Dω is maximizing for µ ∈ Mω if it
computes the energy of µ (2.2), i.e. Eω (ψi ) − ψi µ → Jω (µ).
  Equivalently, (ψi ) is maximizing for µ iff Jω (µ, ψi ) → 0, see (2.4).
Example 2.22. For any φ ∈ Dω the constant sequence ψi = φ is maximizing for µ =
MAω (φ) (see (2.5)).
  As a key consequence of Proposition 2.19, we show:
Theorem 2.23. Assume ω has the orthogonality property. Pick µ ∈ M1ω and a maximizing
sequence ψi ∈ Dω . Then the measures µi := MAω (ψi ) converge strongly to µ in M1ω , i.e.
µi → µ weakly and Jω (µi ) → Jω (µ). In particular, the image of the Monge–Ampère operator
                                        MAω : Dω → M1ω
is dense in the strong topology.
Proof. Pick f ∈ D, and choose C > 0 such that f = f + − f − with f ± ∈ DCω . Since we
assume orthogonality, Proposition 2.19 yields A > 0 such that
                                                  ˆ
                      Eω (ψi + tf ) − Eω (ψi ) − t f µi ≤ At2 sup |f |
                      e
24                            SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

for all i and t > 0. By Proposition 2.10 and (2.4), we have, on the other hand,
                                     ˆ                                        ˆ
             Eω (ψi + tf ) ≤ Jω (µ) + (ψi + tf )µ = Jω (µ, ψi ) + Eω (ψi ) + t f µ.
             e

Combining these estimates, we get
                           ˆ        ˆ
                          t f µi ≤ t f µ + Jω (µ, ψi ) + At2 .

Since Jω (µ, ψi ) → 0, we infer
                                                ˆ              ˆ
                                    t lim sup       f µi ≤ t       f µ + At2 .
                                         i
                                                      ´         ´
Dividing´ by t and´ letting t →  0+ yields lim  sup i   f µ i ≤   f µ. Replacing f with −f , we
                                                0
get limi f µi = f µ. By density of D in´ C (X), this shows µi → µ weakly.       ´
   For each i we have Jω (µi ) = Eω (ψi ) − ψi µi (see (2.5)), ´ and Eω (ψi ) − ψi µ → Jω (µ),
since (ψi ) is maximizing for µ. It only remains to prove ψi (µi − µ) → 0. Since Jω (ψi ) is
bounded (see (2.7), (1.37) yields C > 0 such that
                                ˆ
                                   ψi (µi − µj ) ≲ CJω (ψi , ψj )α

for all i, j, and hence
                          ˆ
                               ψi (µi − µj ) ≲ C max{Jω (µ, ψi ), Jω (µ, ψj )}α ,

by (2.7). Since µj → µ weakly and Jω (µ, ψj ) → 0 as j → ∞, we infer
                              ˆ
                                ψi (µi − µ) ≲ CJω (µ, ψi )α ,

and we conclude, as desired, that the left-hand side tends to 0 as i → ∞.                                   □
2.6. The Dirichlet quasi-metric. From now on, we assume that the orthogonality
property holds for ω. Recall from Examples 2.17 and 2.20, that this is the case if X is a


## Literal published unit: 2506.13548-disk-tree-topology.txt

that agrees with h on the vertices. Since τ can be seen as a tropicalization (see [GRW16,
4.3] for the argument), it is clear that ℓ ◦ τ is R-PL, and since ℓ ◦ τ is a linear combina-
tion of pluriharmonic functions (namely, the functions − log |x i | for i = 0, . . . , d), we see
that ℓ ◦ τ is pluriharmonic by Proposition 7.2(2). By Proposition 7.3, we have h = ℓ ◦ τ,
proving the claim.                                                                                  □
              CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES                      37

                       APPENDIX A. THE TOPOLOGY OF THE UNIT DISK
  Let k be a non-archimedean field which might be trivially valued. In this appendix, we
give an elementary description of the topology of the unit disc B1k = M (k〈T 〉). These are
well-known facts which we present in the way we need in the body of text.
A.1. A rig-point of B1k is induced by a maximal ideal of k〈T 〉. Let k′ be the completion of
an algebraic closure k a of k and let G be the Galois group of k a /k. By [Ber90, 1.3.5] or
[Duc24, (3.1.1.2)], we may write B1k = B1k′ /G as a topological quotient; we denote the
quotient map by π: B1k′ → B1k . For a rig-point z and 0 < ρ ≤ 1, we define the closed disc
B1k (z, ρ) with center z and radius ρ by taking any z ′ ∈ π−1 (z) and then setting
                                                                              
                         B1k (z, ρ) := π {x ′ ∈ B1k′ | |(T − z ′ )(x ′ )| ≤ ρ} .
This is a closed set in B1k which does not depend on the choice of z ′ and which contains
the center z. We often simply write B1 (z, ρ) = B1k (z, ρ). Moreover, we can choose any rig-
point of B1 (z, ρ) as a center. Note that for any rig-point y ′ of B1k′ , the image π(B1k′ ( y ′ , ρ))
is a closed disc Bk (z, ρ) for a suitable rig-point z as center. In the trivially valued case, we
can simply take z = π( y ′ ) and in the non-trivially valued case, this follows by density of
rigid points [Ber90, Proposition 2.1.15] in a strictly affinoid space. Similarly, we define
the open disc B1+ (z, ρ) with center z and radius ρ using |(T − z ′ )(x ′ )| < ρ as a defining
inequality over k′ . The above remarks also apply to open balls. It follows from the
ultrametric triangle inequality that two open or closed balls are either disjoint or one is
contained in the other.
A.2. The topology of the unit disc B1k is well-known. Roughly speaking, it has the struc-
ture of an infinite tree with all branches connected to the Gauss point η1 at the top (see
[Ber90, Example 1.4.4, §4.2] or [Duc24, §3.4]                                           1
                                               S for more details). We call U ⊂ Bk a stan-
dard open subset if it has the form U = B+ \ i Bi where B+ is either an open ball B+ (z, ρ)
with a rig-point z as center and with ρ ∈ (0, 1) or B+ = B1k , and where the Bi are finitely
many closed balls with rig-points as centers and with positive radii. Since two discs are
either disjoint or one is contained in the other, we see that the union and the intersec-
tion of two standard open subsets are again standard open subsets. We claim that the
standard open subsets form a basis of topology for B1k . In the non-trivially valued case,
this follows from [Ber90, §4.2] using §A.1 to find rig-centers in the balls. In the trivially
valued case, B1k is the union of closed intervals starting in the Gauss point η1 and ending
in the rig points of B1k . The topology is very simple as B1k \ {η1 } is the topological disjoint
union of the half-open intervals (η1 , z] with z ranging over the rig points of B1 . A subset
U of B1k is an open neighborhood of η1 if and only if U ∩ [η1 , z] is open for all rig points
z and equal to [η1 , z] except for finitely many z. We refer to [Ber90, Example 1.4.4]
or [BJ18, §1.1.6] for these facts, from which we deduce easily that the standard open
subsets form also a basis of topology in the trivially valued case.
  The main result of this appendix is the following lemma.
Lemma A.3. Let B1 (z, ρ) be a closed disc as above and let f (T ) be the minimal polynomial
of the center z, i.e., a generator of the corresponding maximal ideal of k〈T 〉. Then there is
38                                     W. GUBLER AND J. RABINOFF



## Literal published unit: 2506.13548-scope-and-exclusion.txt

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


## Literal published unit: berkovich-identity-and-general-field.txt

P UBLICATIONS MATHÉMATIQUES DE L’I.H.É.S.




 V LADIMIR G. B ERKOVICH
 Étale cohomology for non-Archimedean analytic spaces
 Publications mathématiques de l’I.H.É.S., tome 78 (1993), p. 5-161
 <http://www.numdam.org/item?id=PMIHES_1993__78__5_0>




      © Publications mathématiques de l’I.H.É.S., 1993, tous droits réservés.
      L’accès aux archives de la revue « Publications mathématiques de l’I.H.É.S. » (http://
      www.ihes.fr/IHES/Publications/Publications.html) implique l’accord avec les conditions géné-
      rales d’utilisation (http://www.numdam.org/conditions). Toute utilisation commerciale ou im-
      pression systématique est constitutive d’une infraction pénale. Toute copie ou impression de
      ce fichier doit contenir la présente mention de copyright.




                               Article numérisé dans le cadre du programme
                             Numérisation de documents anciens mathématiques
                                           http://www.numdam.org/
                                ETALE COHOMOLOGY
                       FOR NON-ARCHIMEDEAN ANALYTIC SPACES
                                                      by VLADIMIR G. BERKOVIGH (1)


                                                                                CONTENTS


INTRODUCTION . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   7

§ 1. Analytic spaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   13
        1.1. Underlying topolcgical s p a c e s . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .            13
        1.2. The category of analytic spaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                     14
        1.3. Analytic domains and G-topology on an analytic space . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                          23
        1.4. Fibre products and the ground field extension functor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                       29
        1.5. Analytic spaces from [Ber] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                31
        1.6. Connection with rigid analytic geometry . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                             35

§ 2. Local rings and residue fields of points of affinoid s p a c e s . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                  38
        2.1. The local rings C^^ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .             38
        2.2. Comparison of properties of (^x, x an<^ ^^, x . . • . • • • . . . . • . • . • . . . • • . • • • • • • • • • • • • • • • • • • • •                             40
        2.3. The residue fields K(x) .............................................................                                                                         43
        2.4. Quasicomplete fields . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .            45
        2.5. The cohomological dimension of the fields K(x) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                  49
        2.6. GAGA over an affinoid space . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                     51

§ 3. Etale and smooth mcrphisms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .              54
        3.1. Quasifinite morphisms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .             54
        3.2. Flat quasifinite morphisms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                58
        3.3. Etale morphisms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .         60
        3.4. Germs of analytic spaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                64
        3.5. Smooth morphisms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .            67
        3.6. Smooth elementary c u r v e s . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .           70
        3.7. The local structure of a smooth morphism . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                76

§ 4. Etale cohomology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    82
        4.1. £tale topology on an analytic space . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                         82
        4.2. Stalks of a sheaf . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       86
        4.3. Quasi-immersions of analytic spaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                       89
        4.4. Quasiconstructible sheaves . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                93


          (1) Incumbent of the Reiter Family Career Development Chair. Supported in part by NSF grant
DMS-9100383.
6                                                             VLADIMIR G. BERKOVICH

§ 5. Cohomology with compact support . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .          96
       5.1. Cohomology with support . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                96
       5.2. Properties of cohomology with support . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                        98
       5.3. The stalks of the sheaf R« 91 F . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .               102
       5.4. The trace mapping for flat quasifinite m o r p h i s m s . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                      106

§ 6. Calculation of cohomology for curves .........................................................                                                                   109
       6.1. The Comparison Theorem for projectives curves . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                 109
       6.2. The trace mapping for curves . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                112
       6.3. Tame etale coverings of curves . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                119
       6.4. Cohomology of affinoid curves . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                 125

§ 7. Main theorems ..........................................................................                                                                         127
        7.1. The Comparison Theorem for Cohomology with Compact Support . . . . . . . . . . . . . . . . . . . . .                                                     127
        7.2. The trace mapping . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .        130
        7.3. Poincare Duality . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   134
        7.4. Applications of Poincare Duality . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                 143
        7.5. The Comparison Theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .               146
        7.6. The invariance of cohomology under extensions of the ground f i e l d . . . . . . . . . . . . . . . . . . . . . .                                        150
        7.7. The Base Change Theorem for Cohomology with Compact S u p p o r t . . . . . . . . . . . . . . . . . . . . .                                              153
        7.8. The Smooth Base Change Theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                         154
REFERENCES.................................................................................                                                                           157

INDEX OF NOTATIONS                 ........................................................................                                                           158

INDEX OF TERMINOLOGY . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      160
                                   INTRODUCTION

        The problem of constructing an 6tale cohomology theory for non-Archimedean
 analytic spaces has arisen from Drinfeld's work on elliptic modules [Dri]. In his work,
 Drinfeld defined (among other things) the first cohomology group HP^X, pj as the set
 of pairs (L, <p), where L is an invertible sheaf on X, and <p is an isomorphism 0^ ^ L0".
 He showed that for the one-dimensional j&-adic upper half-plane 02 this group gives
 rise to a certain infinite dimensional representation of GL^), where k is the ground
 local field. Afterwards, in [Dr2], Drinfeld constructed a certain family of equivariant
 coverings of the d-dimensional j&-adic upper half-plane Q^1, and suggested that all
 cuspidal representations of the group GL^i(^) are realized in high dimensional ^tale
 cohomology groups of this family of coverings.


## Literal published unit: cd-continuous-product-proof.txt

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

Proposition 8.5.6. — Soit j : Y → X un morphisme topologiquement propre d’espaces
tropicaux de niveaux m et n respectivement. Soit u une fonction psh continue sur X et
soit S un courant positif fermé sur Y . Le courant j∗ S sur X est positif fermé et l’on a
l’égalité
                            d′ d′′ (u) ∧ j∗ S = j∗ (d′ d′′ (j ∗ u) ∧ S).
Démonstration. — L’ensemble des fonctions psh u qui vérifient cette relation forment
un sous-faisceau en R+ -modules du faisceau des fonctions continues sur X. Il est stable
par limite uniforme. Compte tenu de la définition du faisceau CPshX , il suffit donc de
vérifier qu’il contient les fonctions lisses u telles que d′ d′′ u ⩾ 0. Dans ce cas, pour toute
forme lisse ω à support compact sur un ouvert U de X, on a
         ⟨d′ d′′ (uj∗ S), ω⟩ = ⟨uj∗ S, d′ d′′ ω⟩ = ⟨j∗ S, u d′ d′′ ω⟩
                            = ⟨S, j ∗ u d′ d′′ j ∗ ω⟩ = ⟨j ∗ uS, d′ d′′ j ∗ ω⟩ = ⟨d′ d′′ (j ∗ uS), j ∗ ω⟩


## Literal published unit: cd-iteration-and-uniform-convergence.txt



            § 8.7. THÉORIE DE BEDFORD–TAYLOR : ITÉRATION

8.7.1. — Soit u1 , . . . , uq des fonctions psh sur X et soit T un courant positif fermé.
Compte tenu du lemme 8.5.5, on définit par récurrence un courant positif fermé
                                  d′ d′′ (u1 d′ d′′ (u2 d′ d′′ (. . . d′ d′′ (uq T )))).
Par construction, ce courant est même d′ d′′ -exact si q ⩾ 1.
   Lorsque T est un courant de Bedford–Taylor, on démontre par récurrence à l’aide de
la proposition 8.6.8 qu’il en est de même du courant
                                  d′ d′′ (u1 d′ d′′ (u2 d′ d′′ (. . . d′ d′′ (uq T )))).
et que ce courant ne dépend que de la suite de courants (d′ d′′ (u1 ), . . . , d′ d′′ (uq ), T ),
justifiant ainsi la notation.
  Lorsque les uj sont lisses, ce courant est égal à
                                  d′ d′′ (u1 ) ∧ d′ d′′ (u2 ) · · · ∧ d′ d′′ (uq ) ∧ T.
  Dans la suite de ce texte, nous nous autoriserons l’abus de notation consistant à écrire
ce courant
                          d′ d′′ (u1 ) ∧ d′ d′′ (u2 ) · · · ∧ d′ d′′ (uq ) ∧ T
même si T n’est pas de Bedford–Taylor.
  En prenant T = δX , on a d′ d′′ (u) ∧ δX = d′ d′′ (u), pour toute fonction psh u. Plus
généralement, on a
        d′ d′′ (u1 ) ∧ d′ d′′ (u2 ) · · · ∧ d′ d′′ (uq ) ∧ δX = d′ d′′ (u1 ) ∧ d′ d′′ (u2 ) · · · ∧ d′ d′′ (uq ).
Proposition 8.7.2. — Soit (Tk ) une suite de courants positifs fermés qui converge vers
un courant positif fermé T . Soit (uk0 ), (uk1 ), . . . , (ukq ) des suites de fonctions continues
sur X qui convergent localement uniformément vers des fonctions u0 , u1 , . . . , uq sur X.
On suppose que pour tout j ∈ {1, . . . , q} et tout k, la fonction ukj est psh. Alors, la suite
de courants
                            uk0 d′ d′′ (uk1 ) ∧ · · · ∧ d′ d′′ (uqq ) ∧ Tk
converge vers le courant
                                      u0 d′ d′′ (u1 ) ∧ · · · ∧ d′ d′′ (uq ) ∧ T.
Démonstration. — On raisonne par récurrence sur q. Pour q = 0, l’assertion résulte du
lemme 8.5.1. Supposons q ⩾ 1 et l’assertion démontrée pour q − 1. Pour tout k, po-
sons Sk = d′ d′′ (uk2 d′ d′′ (. . . d′ d′′ (ukq Tk ))) et S = d′ d′′ (u2 d′ d′′ (. . . d′ d′′ (uq T ))) ; ce sont des
courants positifs fermés, par récurrence, et l’on a Sk → S. D’après le lemme 8.5.1,
on a uk1 Sk → u1 S. Par continuité de l’opérateur d′ d′′ sur les courants, on a donc
210                              CHAPITRE 8. THÉORIE DE BEDFORD–TAYLOR

d′ d′′ (uk1 Sk ) → d′ d′′ (u1 S). Comme pour tout k, le courant d′ d′′ (uk1 Sk ) est positif fermé,
le courant d′ d′′ (u1 S) l’est également. En appliquant de nouveau le lemme 8.5.1, on en
conclut que uk0 d′ d′′ (uk1 Sk ) converge vers u0 d′ d′′ (u1 S), ce qu’il fallait démontrer.
   Nous aurons besoin de la variante suivante.
Proposition 8.7.3. — Soit (Tk ) une suite de courants positifs fermés qui converge
vers un courant positif fermé T . Soit f : X → Rn une carte harmonique. Soit (v0k ),
(v1k ), . . . , (vqk ) des suites de fonctions convexes continues sur Rn qui convergent loca-
lement uniformément vers des fonctions v0 , v1 , . . . , vq ; pour tout i et tout k, posons
uki = f ∗ vik et ui = f ∗ vi . Alors, la suite de courants
                                        uk0 d′ d′′ (uk1 ) ∧ · · · ∧ d′ d′′ (uqq ) ∧ Tk
converge vers le courant
                                        u0 d′ d′′ (u1 ) ∧ · · · ∧ d′ d′′ (uq ) ∧ T.
Démonstration. — La démonstration est analogue à la précédente ; on en reprend
les notations. Pour q = 0, il s’agit du lemme 8.5.1 qui n’exige que la continuité
des fonctions en jeu. Supposons q ⩾ 1 et l’assertion démontrée par q − 1. Posons
Sk = d′ d′′ (uk2 d′ d′′ (. . . d′ d′′ (ukq Tk ))) et S = d′ d′′ (u2 d′ d′′ (. . . d′ d′′ (uq T ))) ; ce sont des
courants positifs fermés, par récurrence, et l’on a Sk → S. D’après le lemme 8.5.1, on
a uk1 Sk → u1 S d’où, par continuité de l’opérateur d′ d′′ sur les courants, la convergence
d′ d′′ (uk1 Sk ) → d′ d′′ (u1 S). Pour tout k, le courant d′ d′′ (uk1 Sk ) est positif fermé en vertu
du corollaire 8.11.3, si bien que le courant d′ d′′ (u1 S) est positif fermé. En appliquant de
nouveau le lemme 8.5.1, on en conclut que uk0 d′ d′′ (uk1 Sk ) converge vers u0 d′ d′′ (u1 S), ce
qu’il fallait démontrer.

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

Proposition 8.7.5. — Soit j : Y → X un morphisme topologiquement propres d’es-
paces tropicaux de niveaux m et n respectivement. Soit u1 , . . . , up des fonctions psh sur X
et soit S un courant positif fermé sur Y . Le courant j∗ S sur X est positif fermé et l’on
a l’égalité
d′ d′′ (u1 ) ∧ d′ d′′ (u2 ) ∧ . . . d′ d′′ (up ) ∧ j∗ S = j∗ (d′ d′′ (j ∗ u1 ) ∧ d′ d′′ (j ∗ u2 ) · · · ∧ d′ d′′ (j ∗ up ) ∧ S).
Démonstration. — La démonstration se déduit de la proposition 8.5.6 par une récurrence
immédiate sur p.
                   § 8.8. EXTENSION AUX DIFFÉRENCES DE FONCTIONS PSH                           211

     § 8.8. EXTENSION AUX DIFFÉRENCES DE FONCTIONS PSH

Lemme 8.8.1. — Soit u une fonction lisse sur X. Tout point x de X possède un


## Literal published unit: thuillier-field-convention.txt



       2. Fon tions harmoniques sur une                      ourbe stri tement
                                     k -analytique lisse



  Dans tout le texte, la notation log désigne le logarithme néperien (ou naturel ).
  Dans e hapitre, k est un orps omplet pour une valeur absolue non ar himédienne |.|,
supposée non triviale. Les éléments de k dont la valeur absolue est inférieure à 1 forment un
sous-anneau k◦ dont le spe tre formel Spf(k◦ ) est noté S . Le orps résiduel de k, quotient de
k◦ par l'idéal maximal k◦◦ = {a ∈ k◦ ; |a| < 1}, est noté ek.
   Après quelques résultats préliminaires sur les espa es k-analytiques, nous allons introduire,
pour toute ourbe k-analytique lisse X , un fais eau d'espa es ve toriels réels HX sur l'espa e
topologique |X| sous-ja ent à X . Par sa dénition même, HX sera un sous-fais eau du fais eau
CX des germes de fon tions réelles ontinues sur |X|, appelé fais eau des germes de fon tions
harmoniques sur X .
   La onstru tion du fais eau HX pro ède d'un raisonnement en quatre étapes.
   Nous expliquons tout d'abord omment asso ier, à toute S - ourbe formelle (stri te-
ment) semi-stable et génériquement lisse X , un sous-espa e H(X ) de l'espa e ve toriel réel
C0 (|Xη |, R).
   Étant donnée une extension non ar himédienne K de k, désignons par C/K la atégo-
rie ayant pour objets les Spf(K ◦ )- ourbes stri tement semi-stables, génériquement lisses et
quasi- ompa t, et dont les morphismes entre X et X ′ sont les isomorphismes de l'espa e K -
analytique Xη sur un domaine K -analytique de Xη′ . La orrespondan e X 7→ H(X ) dénit un
sous-fon teur du fon teur

                                  (C/K)op → VectR
                                         X   7→ C0 (|Xη |, R)

 ompatible  en un sens à pré iser  à l'a tion du groupe de Galois d'une extension galoisienne
nie K ′ /K .
   Invoquant le théorème de rédu tion semi-stable ([9℄), nous obtenons, pour toute ourbe
k-analytique lisse X , un préfais eau HX sur le G-site de X dont la valeur sur un domaine
k-analytique Y de X , isomorphe à la bre générique d'une S - ourbe (formelle) simplement
nodale Y , est H(Y). Ce préfais eau est un sous-préfais eau du fais eau C0 (., R).
   Le préfais eau HX sur le G-site d'une ourbe k-analytique lisse X n'est pas un fais eau.
Le site déni par l'espa e topologique |X| est naturellement un  sous-site  du G-site de X
et la onstru tion s'a hève en vériant que le préfais eau HX sur |X| induit par HX est un
fais eau.




## Literal published unit: thuillier-finite-energy-proof.txt

  L'espa e W1 (X) onduit à la notion d'énergie d'une mesure de Radon positive sur X .
Proposition 3.5.7.  Étant donné un point x ∈ I(X), les propriétés suivantes sont équi-
valentes pour
             toute
                   mesure de Radon positive µ sur X :
             R
   (i ) µ −    X µ δx ∈ dd W (X),
                          c  1


  (ii ) gx,µ ∈ W 1 (X),
  (iii ) gx,µ ∈ L1 (dµ).
  Ces propriétés équivalentes ne dépendent que de la mesure µ, et non du point x onsidéré.
Démonstration. L'équivalen e des points (i) et (ii) est triviale.
  La fon tion gx,µ est négative et, omme expliqué à la n de 3.4.3, leRthéorème 3.4.19 fournit
une famille (µλ ) de formes lisses positives de masse totale onstante X µ telle que la famille
des fon tions lisses gx,µλ soit dé roissante et d'enveloppe inférieure gx,µ .
  La famille (gx,µλ ) est onstruite de telle sorte que gx,µλ′ et gx,µλ oïn ident sur le support
de ddc gx,µλ pour tous λ′ ≥ λ. On en déduit les égalités
       Z                        Z                      Z                      Z
                   c                        c                      c
     −     gx,µλ dd gx,µλ = −      gx,µλ′ dd gx,µλ = −    gx,µλ dd gx,µλ′ = −    gx,µλ dµλ′
          X                     X                             X                X
dont dé oule, en vertu de la positivité de µλ , l'inégalité
                 Z                       Z                  Z
                             c
               −     gx,µλ dd gx,µλ ≤ −     gx,µλ′ dµλ′ = −   gx,µλ′ ddc gx,µλ′ .
                       X                       X                       X
La famille de nombres réels positifs
                                hgx,µλ , gx,µλ ix = hgx,µλ , gx,µλ iD
est don       roissante.
   En vertu du théorème de onvergen e monotone de Lebesgue, la fon tion gx,µ est µ-
intégrable si et seulement si la famille roissante de nombres réels positifs
                                         Z             
                                         −     gx,µλ dµ
                                                   X
104



est majorée. Cette ondition est vériée si et seulement si la famille roissante de nombres
réels positifs                                           
                                       hgx,µλ , gx,µλ iD
est majorée. La fon tion gx,µ est don µ-intégrable si et seulement si gx,µ appartient à l'espa e
W1 (X) (lemme 3.5.3).
  L'identité
                                gy,µ = gx,µ + (gy,x − gx,µ (y))
met en éviden e que les assertions (i)-(iii) sont indépendantes du point x onsidéré.            2
   Quels que soient le point x ∈ I(X) et la mesure de Radon positive µ sur X , le arré de
la norme de la forme linéaire ϕ 7→ hgx,µ , ddc ϕi sur l'espa e ve toriel normé (A0 , ||.||x ) sera
appelée énergie de la mesure µ relativement au point x ; 'est un élément de R≥0 ∪ {+∞}
noté Ex (µ).
   La proposition pré édente montre que Ex (µ) est l'intégrale de la fon tion positive −gx,µ
 ontre la mesure µ :                        Z
                                    Ex (µ) =       (−gx,µ ) dµ.
                                               X
   L'appli ation I(X) → R≥0 ∪ {+∞}, x 7→ Ex (µ) est à valeurs nies ou onstante, égale à
+∞.
   L'ensemble E(X)+ des mesures de Radon positives sur X d'énergie nie est un sous- ne
réel onvexe de D1 (X) engendrant un sous-espa e ve toriel E(X) de
                                      A1 (X) + ddc W 1 (X).
Celui- i hérite, pour tout point x ∈ I(X), d'une forme bilinéaire déduite de l'appli ation
                                                                    Z
                E(X)+ × E(X)+ → R, (µ, ν) 7→ hgx,µ , gx,ν iD,x = −     gx,ν dµ.
                                                                        X
Le noyau de la forme h., .iD,x est le sous-espa e Rδx et elle- i munit l'espa e quotient
E(X)/Rδx d'une stru ture d'espa e de Hilbert réel.
Remarque 3.5.8.  Suivant l'usage en mathématiques, l'énergie est une forme quadratique
sur A1 (X) + ddc W1 (X).

   Donnons enn une variante du prin ipe de Diri hlet dont nous nous servirons au hapitre
4, théorème 4.3.8.
Proposition 3.5.9.  Soit ν une mesure de masse nulle sur Xv ; la borne supérieure de
la fon tionnelle
                                  A0 (Xv ) → RR
                           Fν :
                                  ϕ        7→ 2 Xv ϕ dν − hϕ, ϕiD
est l'énergie E(ν) de la mesure de masse nulle ν .
Démonstration. La mesure ν étant de masse nulle, la fon tionnelle Fν se fa torise par
l'espa e ve toriel quotient A0 (Xv )♮ = A0 (Xv )/H(Xv ), H(Xv ) étant l'espa e des fon tions
réelles harmoniques (lo alement onstantes) sur Xv . La forme de Diri hlet h., .iD induit un
produit s alaire sur A0 (Xv )♮ et ν appartient à W1 (Xv ) si et seulement si la forme linéaire
                                                      Z
                                 A0 (Xv )♮ → R, ϕ 7→       ϕ dν
                                                          Xv
est bornée sur la boule unité {ϕ ; hϕ, ϕiD ≤ 1} ; e i montre que la fon tionnelle Fν est
majorée si et seulement si ν est d'énergie nie.
                                                                                              105



  Il reste à établir que, sous ette dernière hypothèse, la borne supérieure de Fν est égale à
E(ν). Soit g ∈ W1 (Xv ) tel que ddc g = −ν ; la formule
                                     Fν (ϕ) = 2hϕ, giD − hϕ, ϕiD ,
ϕ ∈ A0 (Xv ), montre que Fν atteint son maximum au point [g] de la        omplétion W1 (Xv )♮ =
W1 (Xv )/H(Xv ) et on a don
                        sup Fν = max Fν = Fν (g) = hg, giD = E(ν).
                       A0 (Xv )        W1 (Xv )



## Literal published unit: thuillier-hilbert-space-proof.txt

                              3.5. Espa e W1 (X) et énergie
   Nous onsidérons dans ette se tion une ourbe stri tement k-analytique onnexe, propre
et lisse X et nous introduisons un espa e ve toriel topologique omplet W1 (X) de ourants de
degré 0 sur X . Cet espa e admet une famille de produits s alaires le munissant de stru tures
hilbertiennes toutes équivalentes (et dénissant sa topologie) et onduit naturellement à la
notion d'énergie pour les mesures de Radon positives sur X .
   L'espa e analogue pour une surfa e de Riemann ompa te et onnexe M est dé rit dans
l'arti le [11℄, où il est noté L21 (M, R).
  Une variante peut être développée sur tout ouvert onnexe Ω ⊂ X tel que ∂Ω ⊂ I(X), e
que nous ferons brièvement.

  Rappelons que, pour tous points x, y ∈ I(X), gx,y est la fon tion dans A0 (X) ara térisée
par les propriétés                    
                                         ddc gx,y = δy − δx
                                         gx,y (x) = 0
(proposition 3.3.4, (i)). C'est une fon tion négative et, pour tous x, y, z ∈ I(X),
                                Z                  Z
                                          c
                     gx,y (z) =    gx,y dd gx,z =      gx,z ddc gx,y = gx,z (y).
                               X                  X

  La forme bilinéaire h., .iD sur l'espa e ve toriel A0 (X) dénie par
                                                  Z
                                     hϕ, ψiD = −     ϕ ddc ψ
                                                 X
est symétrique (proposition 3.2.12).
100



  Le noyau N de ette forme bilinéaire est onstitué des fon tions onstantes : une fon tion
ϕ ∈ N est en eet telle que, pour tous x, y ∈ I(X),
                                   ϕ(x) − ϕ(y) = hϕ, gx,y i = 0.
   La forme bilinéaire h., .iD est par ailleurs positive. Il sut de vérier ette assertion sur le
sous-espa e A0S (X) de A0 (X) formé des fon tions qui sont harmoniques sur le omplémentaire
du sous-ensemble ni S de I(X) ; e sous-espa e est engendré par 1 et les fon tions gx,y ,
x, y ∈ S , x 6= y , et
                                      hgx,y , gx,z iD = −gx,y (z)
est postif (les fon tions gx,y sont, par onstru tion, négatives.)
   Le hoix d'un point x ∈ I(X) permet de munir l'espa e ve toriel A0 (X) d'une stru ture
pré-hilbertienne via le produit s alaire
                                 hϕ, ψix = ϕ(x)ψ(x) + hϕ, ψiD .
L'espa e de Hilbert réel obtenu par omplétion est noté W1 (X)x .
Remarque 3.5.1.  Pour tous points x, y ∈ I(X) et toute fon tion ϕ ∈ A0 (X),
                                                      Z
                         hϕ, 1 − gx,y ix = ϕ(x) +          ϕ ddc gx,y = ϕ(y).
                                                       X

Proposition 3.5.2.  L'inje tion         anonique de A0 (X) dans D0 (X) se prolonge de ma-
nière unique en une inje tion ontinue de W 1 (X)x dans D0 (X) dont l'image est un sous-espa e
ve toriel de D0 (X) ne dépendant pas du point x et noté W1 (X).
  Il existe une unique stru ture d'espa e ve toriel topologique sur W1 (X) telle que les isomor-
phismes anoniques W1 (X)x →    ˜ W1 (X) soient des homéomorphismes.
Démonstration. L'inégalité
                          |ϕ(y)| = |hϕ, 1 − gx,y ix | ≤ ||1 − gx,y ||x ||ϕ||x ,
pour toute fon tion ϕ ∈ A0 (X) et tout point y ∈ I(X), montre que l'inje tion anonique
A0 (X) → D0 (X) est ontinue lorsqu'on munit A0 (X) de la norme ||.||x asso iée au produit
s alaire h., .ix (rappelons que la topologie de D0 (X) = Hom(I(X), R) est elle de la onvergen e
simple sur I(X)).
  Pour toute suite de Cau hy (ϕn ) dans A0 (X) muni du produit s alaire h., .ix et tout point y
dans I(X), la suite de réels (ϕn (y)) est de Cau hy en vertu de l'inégalité de Cau hy-S hwarz :
      |ϕn (y) − ϕm (y)| = |hϕn , 1 − gx,y ix − hϕm , 1 − gx,y ix | = |hϕn − ϕm , 1 − gx,y ix |
                        ≤ ||1 − gx,y ||x ||ϕn − ϕm ||x .
Asso iant à un élément u de W1 (X)x , limite d'une suite de Cau hy (ϕn ) dans (A0 (X), h., .ix ),
la limite dans R de la suite de Cau hy (ϕn (x)), nous obtenons une appli ation linéaire
                                            Wx1 → D0 (X)
prolongeant l'inje tion anonique de A0 (X) dans D0 (X). Cette appli ation est en ore inje tive
 ar un élément u de W1 (X)x s'annulant identiquement sur I(X) est tel que
                                             hu, ϕix = 0
pour toute fon tion ϕ ∈ A0 (X), don  nul.
  La se onde assertion s'obtient en observant que les normes ||.||x et ||.||y sur A0 (X) sont
équivalentes : puisque
                                 ϕ(y) = ϕ(x) − hϕ, gx,y ix
                                                                                           101



pour toute fon tion ϕ ∈ A0 (X),
                     |ϕ(y)| ≤ |ϕ(x)| + ||ϕ||x ||gx,y ||x ≤ (1 + ||gx,y ||x )||ϕ||x
et                                                                   
                     ||ϕ||2y = ϕ(y)2 + hϕ, ϕi ≤ 1 + (1 + ||gx,y ||x )2 ||ϕ||2x .
                                                                                             2
  Le produit s alaire hilbertien h., .ix sur W1 (X) permet d'identier et espa e ve toriel au
sous-espa e de D0 (X) onstitué des ourants T tels que la forme linéaire
                                 A0 (X) → R,         ϕ 7→ hT, ddc ϕi
soit ontinue relativement à la norme ||.||x , 'est-à-dire :
                           
                 W1 (X) = T ∈ D0 (X) ;            sup       |hT, ddc ϕi| < ∞ .
                                               ϕ∈A0 (X),||ϕ||x ≤1


Lemme 3.5.3.  Soit          (uλ ) une famille d'éléments de W1 (X) qui onverge vers u dans
D (X) ; les onditions suivantes sont équivalentes :
 0

(i) u appartient à W1 (X) et la famille (uλ ) onverge faiblement vers u dans W1 (X) ;
(ii) la famille des huλ , uλ iD est bornée.
Démonstration. L'impli ation (i) ⇒ (ii) dé oule d'une fait qu'une partie faiblement bornée
d'un espa e de Hilbert est bornée.
   L'impli ation (ii) ⇒ (i) est fa ile : l'observation pré édent le lemme montre que le ourant
limite u appartient à W1 (X) et les deux termes entre parenthèse du se ond membre de l'égalité
                                                                                  
           hψ, uλ ix = hψ, uix + hϕ − ψ, uix + hψ − ϕ, uλ ix + huλ , ϕix − hu, ϕix ,
oú ϕ ∈ A0 (X), peuvent être rendus arbitrairement petit en utilisant la densité de A0 (X) dans
W1 (X).                                                                                     2


## Literal published unit: thuillier-laplacian-solvability-proof.txt


espa e des ourants T de degré 0 tels que dd T ∈ A (X).
                                     c      1


Lemme 3.3.12.  L'inje tion           anonique A0 (X) ֒→ D0 (X) induit un isomorphisme de
Γ(X, HX ) sur ker ddc .
Démonstration. Vu la ompatibilité de l'opérateur ddc aux inje tions anoniques A0 (X) ֒→
D0 (X) et A1 (X) ֒→ D1 (X), l'in lusion
                            Γ(X, HX ) ⊂ ker(ddc : D0 (X) → D1 (X))
est le point (i) du orollaire 3.2.11.
   Soit T ∈ D0 (X) un ourant tel que ddc T = 0.
   Considérons des domaines k-anoïdes V ′ ⊂ V dans X dont les bords de Shilov sont réduits
à un point : Γ(V ) = {y} et Γ(V ′ ) = {y ′ }, ave y, y ′ ∈ I(X). Le point (ii) de la proposition
3.3.7 garantit l'existen e d'une fon tion gyV′ ∈ A0c (X) telle que
                                     
                                        ddc gyV′ = δy − δy′
                                        gyV′ (y) = 0 ;
utilisant l'hypothèse ddc T = 0, il en dé oule
                         0 = hddc T, gyV′ i = hT, ddc gyV′ i = T (y) − T (y ′ ).
84



  Cette formule permet de prolonger la fon tion T : I(X) → R à l'espa e X tout entier :
un point x ∈ X − I(X) admet en eet un système fondamental de voisinages onstitué de
domaines k-anoïdes V ayant un unique point de Shilov et, si Γ(V ) = {y}, il sut de poser
                                           T (x) = T (y).

  Soient V ⊂ X un domaine k-anoïde et h l'unique fon tion dans H(V ) dont la restri tion à
∂V ⊂ I(X) est égale à T ; invoquant de nouveau le point (ii) de la proposition 3.3.4, l'équation
ddc T = 0 implique, pour tout point x ∈ I(V ) − ∂V ,
                                                     Z
                             c   V            c V
                     0 = hdd T, gx i = hT, dd gx i =     T dνxV − T (x)
                                                            ∂V
et don T (x) = h(x) ( orollaire 3.3.9, (ii)).
   Les fon tions h et T|V oïn ident sur I(V ) et sont onstantes au voisinage de ha un des
points de V − I(V ) : elles sont don égales en vertu de la densité de I(V ) dans V .
     Nous avons ainsi établi l'harmoni ité de la fon tion réelle T .                          2
Démonstration de la proposition 3.3.11. Soit T ∈ D0 (X) tel que ddc T soit une forme
lisse ω sur X .
   Étant donné un domaine k-analytique ompa t Y ⊂ X , il existe un sous-ensemble ni S
de I(Y ) ⊂ I(X) ontenant ∂Y et tel que ω|Y appartienne à l'espa e A1S (Y ). La restri tion de
T à une omposante onnexe Ω de Y − S vériant l'équation ddc T|Ω = 0, le lemme pré édent
fournit une fon tion harmonique hΩ sur Ω oïn idant ave T sur I(Ω). La fon tion réelle ϕY
sur Y telle que ϕY = T sur S et ϕY = hΩ sur haque omposante onnexe Ω de Y − S est
une fon tion lisse.
  Il est lair qu'il existe une unique fon tion lisse ϕ ∈ A0 (X) telle que ϕ|Y = ϕY pour tout
domaine k-analytique ompa t Y ⊂ X ; ette fon tion oïn ide ave T sur I(X).                 2

   Nous sommes désormais en mesure de résoudre l'équation ddc T = ρ pour tous ourants
T ∈ D0 (X) et ρ ∈ D1 (X) dans le as d'une ourbe onnexe X vériant l'une des onditions
suivantes :
- X est isomorphe à l'analytiée d'une k- ourbe algébrique ;
- X est isomorphe à la omposante onnexe de l'intérieur d'un espa e stri tement k-anoïde.
  Remarquons que le premier as envisagé englobe en parti ulier elui où la ourbe X est
propre puisque toute ourbe k-analytique propre et onnexe est isomorphe à l'analytiée d'une
k- ourbe algébrique ([3℄, 3.4.14).
Théorème 3.3.13.  Soit X une ourbe stri tement k -analytique lisse, onnexe et véri-
ant l'une des onditions suivantes :
- X est isomorphe à l'analytiée d'une k- ourbe algébrique ;
- X est isomorphe à une omposante onnexe de l'intérieur d'un domaine k-anoïde.
  L'image de l'appli ation ddc : D0 (X) → D1 (X) est
  (i ) l'espa e D1 (X) tout entier si X est n'est pas propre ;
  (ii ) l'hyperplan {ρ ∈ D1 (X) | hρ, 1i = 0} si X est propre.
Démonstration.
(ii) Traitons tout d'abord le as d'une ourbe stri tement k-analytique lisse, propre et onnexe ;
 omme on l'a pré édemment observé, une telle ourbe est isomorphe à l'analytiée d'une k-
 ourbe algébrique propre et lisse en vertu de la proposition 3.4.14 de [3℄. L'in lusion
                              ddc D0 (X) ⊂ {ρ ∈ D1 (X) ; hρ, 1i = 0}
                                                                                            85



est évidente ; ré iproquement, étant donné un ourant ρ ∈ D1 (X) tel que hρ, 1i = 0, xons un
point x ∈ I(X) et onsidérons la fon tion réelle T sur I(X) dénie par
                                         T (y) = hρ, gx,y i,
gx,y étant l'élément de A0 (X) ara térisé par les onditions
                                   
                                      ddc gx,y = δy − δx
                                      gx,y (x) = 0
(proposition 3.3.7, (i)).
  Quelle que soit la fon tion lisse ϕ ∈ A0 (X), l'élément
                           Z                       X Z                    
                                       c                                 c
                       e=
                       ϕ       gx,y (dd ϕ)(y) =                        dd ϕ gx,y
                            X                       y∈I(X)      {y}

de A0 (X) vérie l'équation ddc ϕ
                                e = ddc ϕ ; ϕ − ϕ
                                                e est par onséquent une fon tion harmonique
sur X , don onstante, et l'on obtient la formule intégrale
                                             Z
                                ϕ = ϕ(x) +      gx,y (ddc ϕ)(y).
                                                X

  Nous pouvons maintenant on lure : pour toute fon tion ϕ ∈ A0 (X),
                           Z                                 Z
                                       c
      hρ, ϕi = hρ, ϕ(x) +     gx,y (dd ϕ)(y)i = ϕ(x)hρ, 1i +    hρ, gx,y i (ddc ϕ)(y)
                            X                                 X
                Z
             =      T ddc ϕ = hT, ddc ϕi
                      X
et don ddc T = ρ.
(i) Considérons maintenant une ourbe stri tement k-analytique lisse et onnexe X , isomorphe
à l'analytiée d'une k- ourbe algébrique ane ou à une omposante onnexe de l'intérieur d'un
espa e k-anoïde. Nous vérierons un peu plus loin que es hypothèses garantissent que X
est la réunion d'une suite (Vn ) de domaines stri tement k-anoïdes dans X telle que, pour
tout n :
- Vn ⊂ Vn+1 − Vn ;
- la frontière de ha une des omposantes onnexes C de Vn+1 − Vn est telle que Card(∂C ∩
Vn ) = Card(∂C ∩ Vn+1 ) = 1.
   Tenant e i pour a quis, il est fa ile de on lure la démonstration du théorème.
Première étape. Remarquons tout d'abord que, pour tout n et toute omposante onnexe C
de Vn+1 − Vn , l'espa e ve toriel Γ(C − ∂C, HX ) est de dimension 2. Étant donnée une fon tion
h ∈ H(Vn ), il existe, pour toute omposante onnexe C de Vn+1 − Vn , une unique fon tion


## Literal published unit: thuillier-metric-regularization-proof.txt

                               − log ||s|||Ω′ = − log ||s′ || − log |f |.

   On dénit de même la notion de métrique ontinue, harmonique, et .
   Les fon tions sous-harmoniques u sur une ourbe stri tement k-analytique lisse X s'iden-
tient anoniquement aux métriques sous-harmoniques ||.|| sur son fais eau stru tural via la
relation u = − log ||1||.
   Quel que soit le fais eau inversible L sur X muni d'une métrique sous-harmonique (resp.
lisse) ||.||, il existe un et un seul ourant ρ de degré 1 sur X tel que, pour tout ouvert Ω ⊂ X
et toute se tion inversible s de L sur Ω, ρ|Ω = ddc log ||s|| (rappelons que la orrespondan e
Ω → D0 (Ω) est un fais eau sur X , proposition 3.3.6). Ce ourant, noté c1 (L, ||.||), est appelé
la ourbure du fais eau inversible métrisé (L, ||.||). C'est un ourant positif si (et seulement
si) la métrique est sous-harmonique, une forme lisse si (et seulement si) la métrique est lisse.
  Il est maintenant possible d'énon er l'analogue du orollaire 3.4.13.
Corollaire 3.4.18.  Il existe, pour toute mesure de Radon positive µ sur une            ourbe
stri tement k-analytique propre et lisse X , un fais eau inversible L sur X muni d'une métrique
sous-harmonique ||.|| et un nombre réel positif λ tels que
                                          µ = λc1 (L, ||.||).
Démonstration. Considérons un point x ∈ X tel que [κ(x) : k] < ∞ et soit L le fais eau
inversible ample OX ([x]). Étant donnée une mesure de probabilité µ sur X , le théorème 3.3.13
fournit un ourant g ∈ D0 (X), uniquement déterminé à l'addition d'une onstante près, tel
que
                                    ddc g = [κ(x) : k]µ − δ[x] .
Il existe alors, en vertu de la formule de Poin aré-Lelong (proposition 3.3.15) une unique
métrique sous-harmonique ||.|| sur le fais eau inversible L telle que

                                         − log ||1[x] || = g;

toujours grâ e à la formule de Poin aré-Lelong, sa ourbure est [κ(x) : k]µ.                       2
  Le théorème 3.4.2 se généralise sans di ulté au as de fais eaux inversibles munis de
métriques sous-harmoniques.
Théorème 3.4.19.  Soit L un fais eau inversible sur une                    ourbe stri tement k-
analytique propre et lisse. Pour toute métrique sous-harmonique ||.|| sur L, la restri tion de ||.||
à Ω est l'enveloppe supérieure d'une famille roissante (||.||λ ) de métriques sous-harmoniques
lisses sur L|Ω et le ourant c1 (L, ||.||)|Ω est la limite des ourants c1 (L, ||.||λ ).
Démonstration. La preuve du théorème 3.4.2 s'adapte sans di ulté à la situation présente.
Quel que soit le sous-ensemble ni S de I(X) tel que L soit trivial sur l'adhéren e de ha une
des omposantes onnexes de Y − S , il existe une unique métrique sous-harmonique lisse
||.||S sur L telle que, pour tout U ∈ π0 (X − S) et toute trivialisation ε de L au voisinage
de U , − log ||ε||S soit l'élément de Γ(U, HX ) ∩ C0 (U , R) qui oïn ide ave − log ||ε|| sur ∂U :
  ette formule dénit en eet ||.||S sans ambiguité en vertu de l'harmoni ité des fon tions de
transitions − log |f | et la sous-harmoni ité s'obtient omme elles des fon tions uS au théorème
3.4.2.
98



   De la sous-harmoni ité de ||.|| dé oule que les métriques ||.||S forment une famille rois-
sante lorsque S par ourt l'ensemble ltrant des parties nies de I(Y ) satisfaisant aux ondi-
tions pré édentes. Son enveloppe supérieure est la métrique ||.|| (même argument que dans la
démonstration du théorème 3.4.2).                                                          2

  Étant donnés une ourbe stri tement k-analytique onnexe, propre et lisse X et un point
x ∈ I(X), il existe, pour toute mesure de Radon positive µ sur X , un unique ourant T ∈
D0 (X) tel que
                                               R   
                                   ddc T = µ − X µ δx
                                   T (x) = 0
(théorème 3.3.13) et, vu le théorème 3.4.12, la ondition ddc T|X−{x} ≥ 0 implique que le
 ourant T|X−{x} se prolonge naturellement en une fon tion sous-harmonique sur X − {x}.
   Nous noterons gx,µ l'unique fon tion X → R ∪ {−∞} qui est sous-harmonique sur X − {x}
et satisfait aux onditions                        R  
                                    ddc gx,µ = µ − X µ δx
                                    gx,µ (x) = 0.
     La formule
                                  gy,µ = gx,µ + (gy,x − gx,µ (y))
est immédiate pour tous points x, y ∈ I(X) ; puisque gx,y est une fon tion ontinue (et même
lisse), elle implique en parti ulier la semi- ontinuité supérieure de gx,µ sur l'espa e X tout
entier.
Remarque 3.4.20.  La fon tion gx,µ est négative.
   Appliqué à la mesure δD asso iée à un diviseur ee tif, e qui pré ède dénit sur le fais-
 eau inversible OX (D) une métrique lisse et sous-harmonique ||.|| de ourbure deg(D)δx :
− log ||1D || = −gx,δD .
   En parti ulier : tout fais eau inversible de degré 0 sur X peut être muni d'une métrique
harmonique.
   Une mesure de Radon positive µ sur X de masse totale deg(D) est la ourbure de la métrique
sous-harmonique ||.|| sur le fais eau inversible OX (D) dénie par la formule : − log ||1D || =
gx,µ − gx,δD . Le théorème 3.4.15 fournit une famille roissante (||.||λ ) de métriques sous-
harmoniques et lisses dont ette métrique est l'enveloppe supérieure ; la famille des fon tions
lisses
                                        ϕλ = − log ||1||λ
est alors dé roissante, d'enveloppe inférieure gx,µ , et les formes lisses
                           µλ = ddc ϕλ + δx = c1 (OX (D), ||.||λ )
                                             R
sont positives, de masse onstante deg(D) = X µ. La famille (µλ ) onverge faiblement vers
la mesure µ puisque, pour toute fon tion ψ ∈ A0 (X),
                             Z            Z
                                 ψ dµλ =     ϕλ ddc ψ + ψ(x)
                                  X              X
                   c
                                       R
