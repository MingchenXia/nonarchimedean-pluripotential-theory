---
title: Quadratic ascent of continuous zero-Hessian currents in every pure dimension
author: Unverified author proof draft
date: 3 October 2026
geometry: margin=1in
fontsize: 11pt
---

## 1. Exact result and status

Let $K$ be complete and nontrivially valued. Let $E/K$ be quadratic Galois, with nonidentity automorphism $\sigma$. Assume the explicit field condition

$$\exists a\in E:\quad |a|=|a-\sigma(a)|=1. \tag{H}$$

Absolute values on finite extensions are the extending absolute values. Write $t_f=-\log|f|$ for an analytic unit. All real differential forms below are **ordinary CLD forms**, locally described on ordinary open moment charts. Weakly smooth forms and merely G-local forms are not substituted for them.

**Theorem A (ordinary polynomial-superform descent).** Let $X$ be good and topologically separated over $K$, and let $\pi:X_E\to X$. Suppose $\pi^{-1}(x)$ consists of one point. If $f_1,\ldots,f_m$ are analytic units on a scalar-extended affinoid neighbourhood of that fibre, every polynomial superform in the coordinates $t_{f_i},t_{\sigma f_i}$ invariant under simultaneous interchange of these coordinates and their differentials is, after shrinking the downstairs affinoid neighbourhood, the exact pullback of an ordinary smooth form downstairs. This holds in every bidegree. The shrink and finite downstairs unit list can be chosen once for the whole polynomial-superform algebra associated with the given $f_i$.

**Theorem B (compact differentiated approximation).** Under the same field and space hypotheses, let $\beta\in A_c^{p,q}(X_E)$ satisfy $\sigma^*\beta=\beta$. There are $\alpha_j\in A_c^{p,q}(X)$, all supported in one compact $D\subset X$, such that the errors $\beta-\pi^*\alpha_j$ have representations on a finite fixed collection of upstairs unit-moment neighbourhoods as finite sums of fixed smooth cutoffs times coefficient superforms converging in $C^2$ on fixed compact Euclidean boxes. Every moment list and every cutoff is independent of $j$. This asserts controlled approximation, not exact descent of all invariant ordinary smooth forms.

**Theorem C (the restricted higher-dimensional gate).** Assume (H). Let $X$ be good, separated, strict, boundaryless and pure of dimension $n\geq1$, with its actual, possibly singular and nonreduced, analytic structure. For every continuous finite $h:X\to\mathbb R$,

$$
d'd''(h\delta_X)=0
\quad\Longleftrightarrow\quad
d'd''((h\circ\pi)\delta_{X_E})=0. \tag{1}
$$

Both sides are tested against every compact ordinary $(n-1,n-1)$ form and use their actual canonical calibrations. No scalar-stability assumption on $h$ is imposed. The conclusion holds on every ordinary open subspace and iterates along any finite tower of quadratic Galois stages each satisfying (H) over its preceding field.

Here $h\delta_X$ denotes the integration current $[h]$: its value on a compact top form $\omega$ is $\int_X h\,\omega_{\mathrm{Rad},K}$. For the equation (1), a fixed duality sign does not affect vanishing. We consistently use

$$\mathcal B_h(\alpha)=\int_X h\,(d'd''\alpha)_{\mathrm{Rad},K}.$$

The proof closes the ordinary differential-form gate for this precise quadratic class in all pure dimensions, extending the fallible preceding scalar draft's one-dimensional claim. It does **not** solve the original recognition atom P06.2. Two-sign regularization, unrestricted finite-Galois ascent, infinite or transcendental extensions, and the universal classical curve-test bridge are not proved. Status is `partial`, and `candidate=false`. No independent review, formal verification, or priority claim is made.

## 2. Definitions and exact primary-source inputs

The primary snapshots are CLD arXiv:1204.6277v2 (25 July 2025), GR arXiv:2506.13548v2 (17 September 2025), GJR arXiv:2111.05741v3 (7 March 2025), and Conrad--Temkin arXiv:1912.06230v2 (10 April 2021). The theorem numbers below refer to these cached versions. Exact source bytes, inspected statements and proof ranges are retained locally. No result of the prior draft or catalogue is imported as an assumed theorem. All elementary supporting claims used here are proved below.

An affinoid **neighbourhood** contains an ordinary open neighbourhood. Write $\operatorname{int}_X(V)$ for the ordinary topological interior of a domain $V$ in $X$. This is distinct from its absolute analytic interior. Compactness and supports always concern the ordinary Hausdorff topology.

The following are the precise primary results used, with the hypotheses relevant here explicitly retained.

1. **Analytic algebra and neighbourhoods.** CLD §§11.1.1--2: an affinoid spectrum is compact Hausdorff; affinoid algebras are noetherian with closed ideals; for a $k$-affinoid algebra $A$, $\mathcal M(A)\to\operatorname{Spec}A$ is surjective. Section 11.1.5 gives rational affinoid neighbourhoods inside a prescribed open in an affinoid. Section 11.1.7 says that affinoid neighbourhoods form a basis in a good space and ordinary opens are analytic domains. Section 11.1.9 computes affinoid fibre products by completed tensor products, computes scalar extension as $\mathcal M(A\widehat\otimes_k L)$, and states surjectivity of scalar projection. Section 11.2.2 says analytic separatedness implies topological separatedness. Section 11.4.4 says a finite Banach algebra over an affinoid algebra, with its finite-module topology, is affinoid. We prove all special finite-tensor, fibre-orbit, compactness and shrinking claims needed in Section 3; none is inferred from a topological-cover assumption.

2. **Dimension and boundary.** CLD §11.2.3 states: strict affinoid dimension is Krull dimension; scalar extension preserves dimension; if $X_i=\mathcal M(A/P_i)$ are the minimal-prime components of an affinoid, then $\dim_xX=\sup_{x\in X_i}\dim X_i$; analytic domains preserve local dimension. Purity means local dimension $n$ at every point. GR §2.11(5') states, for any analytic extension $L/K$ and any morphism $X\to Y$,

   $$\partial(X_L/Y_L)\subseteq\pi^{-1}(\partial(X/Y)).$$

   In particular boundarylessness of $X$ gives boundarylessness of $X_E$. Section 3 checks minimal primes and purity, rather than inferring purity from equality of total dimensions. Goodness, strictness and separatedness are checked by affinoid presentations and base change of the diagonal.

3. **Ordinary forms and equality.** CLD Proposition 15.1.1(b): a form on a topologically separated analytic space has an ordinary open cover $V_i$ on which it is the pullback, by a moment $f_i$, of a coefficient form on a paralinéaire set containing $f_{i,\mathrm{trop}}(V_i)$. CLD §3.3.3 and Lemma 1.9.4 allow a coefficient form to be represented by a Euclidean form on an ambient open: the lemma's extension assertion requires the paralinéaire subset to be closed in that open. Section 3.3.3 explicitly chooses such an open. We use smooth Euclidean coefficients, then cut them off near compact moment images. CLD §§6.2.1--2 define ordinary smooth forms as those G-form sections which have these representations on ordinary open neighbourhoods; they form an ordinary sheaf stable under $d',d'',J$ and wedge. Pullbacks commute with these operations (CLD §3.3.12).

   CLD Proposition 3.4.4 states that for a G-tropical chart $f:X\to V$ and a coefficient form $\eta$, its pullback is zero in the G-form sheaf iff $\eta$ restricts to zero on every compact domain image $f(W)$. Proposition 3.4.1 gives the same criterion for the compact presheaf chart. We use this to prove a polynomial 1-form identity on a tropical tripod. The resulting forms are ordinary: the moments and coefficient formulas are defined on an ordinary neighbourhood, and equality in the containing G-sheaf is equality in its ordinary subsheaf. No ordinary descent of an arbitrary G-local form is asserted.

4. **Cutoffs.** CLD §15.2.2 says a good topologically separated analytic space is locally holomorphically separated. CLD Corollary 15.2.9 states: if $X$ is locally holomorphically separated, $F\subset X$ is closed and countable at infinity (in particular compact), and $U_i$ is an ordinary open cover of $F$, there are nonnegative ordinary smooth $\theta_i$, each compactly supported inside $U_i$, locally finite, with $\sum_i\theta_i=1$ near $F$. Only finite covers of compact sets are used. Products with compact support inside an ordinary open extend smoothly by zero, by the direct neighbourhood argument in Section 7. No global paracompactness is imposed.

5. **Calibration and integration.** CLD Theorem 15.7.1 states that a pure $n$-dimensional topologically separated analytic space, with its analytic boundary and canonical calibration, is a tropical space of level $n$. Section 15.7.2 identifies the induced structure on domains with their own analytic structure. Sections 5.8.3--5 and 7.3.5 give top forms their calibrated Radon measures and locally integrable multipliers their integration currents. Continuous finite multipliers are locally integrable. CLD §5.4.4 says every compact tropical chart is pleasant, with tropical polyhedron the top-dimensional part of its compact image. Proposition 5.10.1(c,d) identifies locally integrable top-form Radon pushforward and integration with contraction on that polyhedron. The canonical calibration is standard and positive on its finitely many cells (CLD §§14.3.2--5). This makes any fixed smooth positive top form finite on a compact moment neighbourhood. Section 8 proves the required coefficient-to-total-variation estimate directly.

6. **Scalar projection, with no extension-degree factor.** CLD Proposition 14.3.6 states: for an analytic space of level $n$, a skeletal subset $\Sigma$ with canonical calibration $\mu$, and a complete scalar extension $L/k$, the extended skeletal subset has canonical calibration $\mu_L$ satisfying $\pi_*\mu_L=\mu$. Proposition 15.3.1 states for a $(n,n)$ G-form $\omega$ with tropically Borel coefficients,

   $$\pi_*(\omega_{L,\mathrm{Bor}})=\omega_{\mathrm{Bor}},$$

   and, if it is locally integrable,

   $$\pi_*(\omega_{L,\mathrm{Rad}})=\omega_{\mathrm{Rad}}. \tag{2}$$

   Its proof contracts with the calibration from 14.3.6. That proposition is proved cell by cell using Lemma 13.3.3's actual fibre-algebra degree identity: a convenient local finite-flat projection's downstairs degree equals the sum of its degrees at all upstairs skeletal lifts. The degrees are dimensions of finite fibre algebras, retaining lengths, not counts of points. Thus neither a reduction nor a factor $[E:K]$ may be inserted in (2). We use (2) for differentiated **smooth forms**, then integrate their signed pushforwards against $h$. This does not define a pullback of an arbitrary current.

7. **Restriction of the ground field, with a degree factor.** CLD Remark 14.4.3 states: if $F/k$ is finite and $Z$ is an $F$-analytic space of level $n$, its same carrier $Z_0$ with restricted $k$-analytic structure has the same dimension and skeletal subsets, and

   $$\mu_{Z_0}=[F:k]\mu_Z. \tag{3}$$

   The proof uses that the scalar projection of the split $n$-torus is finite flat of degree $[F:k]$ when regarded over $k$. Section 3 proves equality of the ordinary sheaves on these two structures on the same carrier; (3) then gives the same factor for their top Radon measures.

   CLD Proposition 15.4.3 states: if $f:Y\to X$ is between spaces of level $n$ and finite away from a Zariski closed set of dimension $<n$, $p\in\{n-1,n\}$, and $\omega$ is a locally integrable $(p,n)$ G-form, then $f^*\omega$ is locally integrable and $f_*((f^*\omega)_{\mathrm{Rad}})=\mathrm{dc}f\,\omega_{\mathrm{Rad}}$. We use only the degree-one isomorphism case on $Z_0$ to handle the semilinear involution as a genuine $K$-analytic map. Cancelling the factor 2 from (3) gives invariance of the $E$-calibrated pairing. It is not ordinary-form descent through scalar projection.

These inputs apply to singular and nonreduced spaces as stated. Their uses involve no smoothness or normalization of $X$. GJR Proposition 14.2 concerns **weakly smooth** Galois descent and is not a premise. CLD Theorem 16.3.3 concerns G-tropical fibre integration and is not an ordinary-form descent premise. Conrad--Temkin's descent of analytic morphism properties is not used as a real-form theorem.

## 3. Actual finite tensors, fibres, structures and purity

### 3.1. Finite algebra and invariants

Let $A$ be a $K$-affinoid Banach algebra, without any reducedness assumption. Then $B=A\widehat\otimes_K E=A\otimes_K E$. Indeed a basis of the finite-dimensional normed field $E$ gives bounded coordinate maps and its norm is equivalent to a coefficient maximum norm. One proof is induction: a span of all but the last basis vector is complete and closed by induction; the remaining vector has positive distance from that span, bounding its coefficient, after which the ultrametric inequality bounds the other coefficients. Tensoring the bounded coordinate maps with $A$ and using the tensor upper bound identifies the tensor topology with the topology of a finite sum of copies of $A$, already complete. Thus $B$ has the finite-module topology.

The semilinear involution of $B$ is $1\otimes\sigma$. The kernel of $\sigma-1$ on the $K$-vector space $E$ is $K$. Exactness of tensoring vector spaces gives $B^\sigma=A$. If an invariant $b\in B$ is a unit, its inverse is invariant too, so both are in $A$ and $b\in A^\times$. No averaging in $K$, and in particular no division by 2 in characteristic two, is used. If an element of an affinoid algebra has no analytic zero, it is a unit: otherwise it is in a maximal ideal, and spectral surjectivity supplies an analytic point with that kernel. This works for nonreduced algebras.

Condition (H) implies $a\notin K$, so $1,a$ is a $K$-basis. Every $f\in B$ has a unique expression $u+av$ with $u,v\in A$. This decomposition will be used for ordinary **differential** descent, not merely scalar reconstruction.

### 3.2. Fibres, compactness and shrinking

The actual fibre over $x$ is $\mathcal M(\mathcal H(x)\otimes_K E)$. Factoring the separable quadratic minimal polynomial over $\mathcal H(x)$ shows this finite algebra is a field or a product of two fields. Each finite field factor has one analytic point. Existence follows from its finite-affinoid Banach structure and nonempty spectrum. Uniqueness follows from finite-dimensional norm equivalence: apply any equivalence bound between two extending absolute values to $z^r$ and take $r$th roots. The two values of $z$ must agree.

The involution is transitive on fibre points. The same invariant-kernel calculation gives $(\mathcal H(x)\otimes_K E)^\sigma=\mathcal H(x)$. Two separate orbits of primitive factors would give an invariant nontrivial idempotent, impossible in that field. Consequently there is either one fixed point or two interchanged points. No assertion that this finite étale projection is a local topological cover is made.

The upstairs carrier is Hausdorff. Points with different images are separated downstairs; points in a common fibre lie in the open inverse image of the interior of an affinoid neighbourhood and can be separated inside its Hausdorff scalar extension. If $C\subset X$ is compact, cover it by finitely many interiors of affinoid neighbourhoods $V_\ell$. Then $\pi^{-1}(C)$ is closed in the finite union of the compact $V_{\ell,E}$, so is compact.

We repeatedly use this precise shrinking argument. In a downstairs affinoid neighbourhood $V_0$ of $x$, let $N\subset V_{0,E}$ be a relative ordinary open containing the **whole** fibre. The compact complement $V_{0,E}\setminus N$ has compact, hence closed, image in $V_0$ excluding $x$. Choose an affinoid neighbourhood $V$ of $x$ inside the complement of that image and inside $\operatorname{int}_X(V_0)$. Then $V_E\subset N$. This proves that finitely many pointwise unit or strict norm inequalities holding on the whole fibre can be retained on a single smaller downstairs affinoid neighbourhood.

### 3.3. Restricted carrier and ambient hypotheses

Let $Z=X_E$ and let $Z_0$ be its restricted $K$-analytic structure. On each common affinoid neighbourhood the Banach algebra and analytic units are identical. An $E$-affinoid neighbourhood is $K$-affinoid under finite restriction of scalars; conversely rational domains in these algebras are computed by the same analytic elements and inequalities. These give a common local basis and the same structural sheaf on ordinary opens. Unit moments and their compact images coincide. CLD 3.4.1--4 gives identical coefficient nullity for their ordinary moment descriptions. CLD 15.1.1(b) and 6.2.1--2 therefore identify their ordinary form sheaves in every bidegree, including their differentials and supports. This is equality on one carrier, not descent through $\pi$. The involution is a $K$-analytic automorphism of $Z_0$, even though it is semilinear over $E$.

For $X$ in Theorem C, goodness upstairs follows from inverse images of interiors of affinoid neighbourhoods. Strict presentations base change to strict presentations. Separatedness follows by base changing the closed diagonal. Boundarylessness follows from GR 2.11(5'), without an equality of absolute interiors.

Here is the minimal-prime check for every dimension. For a strict affinoid neighbourhood $\mathcal M(A)$ in $X$, each component $\mathcal M(A/P)$ has dimension $n$: spectral surjectivity supplies a point of kernel $P$, lying only on that minimal-prime component, and the local dimension formula gives $\dim A/P=n$. Let $J$ be the nilradical of $A$, nilpotent by noetherianity. Inject $A/J$ into the finite product of the fraction fields of $A/P$. Tensoring with $E$ preserves the injection, and each fraction-field tensor is a product of fields by separability. Hence $(A/J)\otimes E$ is reduced and $J\otimes E$ is exactly the nilradical of $B$.

The kernels of the finitely many maps from this reduced tensor to those field factors are primes with zero intersection. Every minimal prime contains one of the kernels, since the product of all kernels is zero and the prime is prime; minimality makes it that kernel. Its contraction to $A$ is the corresponding minimal $P$, because $A/P$ embeds into the field factor. The finite integral injection $A/P\to B/Q$ preserves dimension. Here is the elementary finite-algebra proof. For an injection of domains $C\to D$ with $D$ finite over $C$, and a prime $p$ of $C$, the localized finite module $D_p$ is nonzero. The local-ring determinant argument gives $pD_p\ne D_p$: otherwise a finite generating system expressing every generator as a $p$-linear combination would give a unit determinant annihilating $D_p$. A maximal ideal containing $pD_p$ contracts to $pC_p$, proving lying over. Quotienting by a prime already chosen and applying the same argument proves going up. For incomparability, quotient by the smaller prime and localize at the complement of the common contracted prime. The resulting domain is integral over the fraction field of the base domain and is a field: a nonzero element's monic equation of least degree has nonzero constant term and expresses its inverse. No strictly larger prime remains. Going up lifts chains, and incomparability makes contractions of chains strict. Thus dimensions agree.

Every minimal component of $B$ has dimension $n$, so the local dimension formula gives purity upstairs. Actual unreduced algebras, not these reductions, are used for all integration. In particular finite-fibre degrees in the calibration keep their actual lengths. Goodness, strictness, separatedness, boundarylessness and purity persist at every finite tower stage.

## 4. Scalar quadratic reconstruction on every analytic point

The following proof reconstructs the scalar draft's load-bearing claim. Since $\sigma$ is isometric, $|\sigma(a)|=1$. Also $|a+1|=|\sigma(a)+1|=1$: otherwise both would have norm $<1$, contradicting $|a-\sigma(a)|=1$.

The three rows $(c,\sigma(c))$, for $c=1,a,a+1$, have norm-one entries and norm-one pairwise determinants, each equal up to sign to $\sigma(a)-a$. Every inverse two-row matrix has norm-one entries. For a unit $f\in B$, put $\bar f=\sigma f$, $N=f\bar f$, and $T_c=cf+\sigma(c)\bar f$. These are invariant; $N\in A^\times$. At any analytic point put $M=\max(|f|,|\bar f|)$. All $|T_c|\leq M$, and two cannot both be $<M$, since their inverse matrix would force $|f|,|\bar f|<M$.

At a singleton fibre $\{y\}$, the isometry fixing $y$ gives $|f(y)|=|\bar f(y)|$. Select two traces with value $M>0$. By the compact-complement shrinking argument they are units on a smaller downstairs affinoid. Put upstairs

$$t=t_f,\quad t'=t_{\bar f},\quad S=t_N,\quad A_0=t_{T_c},\quad B_0=t_{T_d}.$$

On the **whole** retained neighbourhood,

$$ (t-t')^2=(S-2A_0)(S-2B_0). \tag{4}$$

If $t\ne t'$, there is no cancellation in either trace, so $A_0=B_0=\min(t,t')$ and both factors are $|t-t'|$. If $t=t'=t_0$, both trace logs are $\geq t_0$ and at least one equals $t_0$ by the inverse-matrix argument. Both sides of (4) are zero. This includes every cancellation direction and every analytic point, not just a skeleton.

The downstairs ordinary smooth function

$$Q(f)=(t_N-2t_{T_c})(t_N-2t_{T_d})$$

therefore pulls back to $(t_f-t_{\sigma f})^2$. For the finite lists $f_i$ and $f_if_j$, choose traces and shrink once. Write

$$s_i=t_{f_i}+t_{\sigma f_i},\qquad \delta_i=t_{f_i}-t_{\sigma f_i}.$$

The $s_i$ descend as norm-unit logarithms. The ordinary scalars

$$Q_{ii}=Q(f_i),\qquad Q_{ij}=\tfrac12\bigl(Q(f_if_j)-Q(f_i)-Q(f_j)\bigr)\quad(i<j) \tag{5}$$

satisfy $\pi^*Q_{ij}=\delta_i\delta_j$; put $Q_{ji}=Q_{ij}$. All divisions here and below by 2 are in the real coefficient algebra. An invariant scalar polynomial is even in the simultaneous sign change of all $\delta_i$, so its monomials pair into products (5). This proves scalar polynomial descent but does not by itself prove form descent. The additional argument follows.

## 5. The ordinary differential-form reconstruction

### 5.1. A tripod identity in the actual ordinary sheaf

Let $F,G,e$ be analytic units on an ordinary analytic neighbourhood, with $G=F+e$. Put $x=t_F$, $z=t_G$, $r=t_e$, $U=x-r=t_{F/e}$, $V=z-r=t_{G/e}$. The relation $G/e=1+F/e$ implies that $(U,V)$ lies in the union of three rays

$$\{U=V\leq0\}\ \cup\ \{U\geq0,V=0\}\ \cup\ \{V\geq0,U=0\}. \tag{6}$$

This follows directly from the ultrametric inequality: if $|F/e|>1$, both magnitudes are equal and $>1$; if $|F/e|<1$, $|G/e|=1$; if $|F/e|=1$, $|G/e|\leq1$.

For either $d=d'$ or $d=d''$, the ambient polynomial 1-form $U\,dV-V\,dU$ restricts to zero on each ray: on the diagonal its terms agree, and on an axis both the zero coordinate and its tangent differential vanish. At the common vertex both coefficients vanish. On every compact moment image the same restrictions hold. CLD 3.4.4 proves the exact ordinary-form identity

$$ U\,dV-V\,dU=0.$$

Expanding, we obtain

$$ x\,dz-z\,dx=r(dz-dx)+(x-z)\,dr. \tag{7}$$

This is a sheaf identity of ordinary forms, not a claim obtained by differentiating equality at isolated points. The moment $(F/e,G/e)$ and the polynomial coefficient form establish it on the whole ordinary neighbourhood. Nilpotents do not affect the norm-image containment and are not removed from the structure.

### 5.2. Every zero-coefficient case is retained

Work on a scalar-extended affinoid neighbourhood of a singleton fibre over $x_0$. Express each unit $f_i=u_i+av_i$, with $u_i,v_i\in A$.

If $v_i(x_0)=0$, then $u_i(x_0)\ne0$ because $f_i$ is a unit. Shrink so $u_i$ is a downstairs unit and $|av_i|,|\sigma(a)v_i|<|u_i|$ throughout the full upstairs neighbourhood. These strict inequalities hold on the whole fibre and are retained by Section 3.2. Then

$$t_{f_i}=t_{\sigma f_i}=t_{u_i},\qquad\delta_i=0 \tag{8}$$

as ordinary functions and hence as differential forms. Here pointwise equality on the whole neighbourhood is equality of ordinary scalar sections by the degree-zero nullity criterion CLD 3.4.4, so it may legitimately be differentiated. All pairs involving this $\delta_i$ are zero.

For the remaining indices, shrink so $v_i$ is a downstairs unit and set $F_i=f_i/v_i=a+b_i$, $b_i=u_i/v_i\in A$. Then $F_i$ and $\sigma F_i$ are units and their log differences are exactly $\delta_i$. For a pair $i,j$ put $e_{ij}=b_j-b_i\in A$.

If $e_{ij}(x_0)=0$, shrink so $|e_{ij}|<|F_i|,|\sigma F_i|$ on the whole upstairs neighbourhood. Since $F_j=F_i+e_{ij}$ and $\sigma F_j=\sigma F_i+e_{ij}$, their logarithms agree there. Thus $\delta_j=\delta_i$, including all derivatives, and

$$\delta_i\,d\delta_j-\delta_j\,d\delta_i=0. \tag{9}$$

If $e_{ij}(x_0)\ne0$, shrink so $e_{ij}\in A^\times$ and apply (7) to $F_i,F_j,e_{ij}$ and their conjugates. This exhausts all cases. There are only finitely many indices and pairs; the same compact-complement construction makes all choices on one smaller neighbourhood. No zero or nonunit is used in a logarithmic coordinate.

### 5.3. Descended orbital 1-forms

In the nonzero $e_{ij}$ case, the downstairs units $F_i\sigma F_i$ and $F_j\sigma F_j$ have logarithms

$$S_i=t_{F_i\sigma F_i},\quad S_j=t_{F_j\sigma F_j},\quad r=t_{e_{ij}}.$$

Their pullbacks are $t_{F_i}+t_{\sigma F_i}$ and $t_{F_j}+t_{\sigma F_j}$. Add (7) to its conjugate. The left side, expressed in sums and differences, is

$$\tfrac12(S_i\,dS_j-S_j\,dS_i+\delta_i\,d\delta_j-\delta_j\,d\delta_i).$$

Consequently the downstairs ordinary 1-form

$$O_{ij}^{d}=2r(dS_j-dS_i)+2(S_i-S_j)\,dr-S_i\,dS_j+S_j\,dS_i \tag{10}$$

has exact pullback

$$\pi^*O_{ij}^{d}=\delta_i\,d\delta_j-\delta_j\,d\delta_i.$$

In the zero cases (8)--(9) use $O_{ij}^{d}=0$. Also put $O_{ii}^{d}=0$ and $O_{ji}^{d}=-O_{ij}^{d}$. The identities hold for both $d'$ and $d''$. Notice that the sums $S_i$ are the sums for the normalized units $F_i$; their differences are still the original $\delta_i$. No unsupported identification of their sums with the original $s_i$ is made.

Combining (10) with (5), define downstairs

$$L_{ij}^{d}=\tfrac12(dQ_{ij}+O_{ij}^{d}). \tag{11}$$

Then, as an exact ordinary 1-form identity,

$$\pi^*L_{ij}^{d}=\delta_i\,d\delta_j. \tag{12}$$

This recovers the alternating part omitted by the symmetric-Hessian-only route. It is the essential new step.

### 5.4. All differential pairs and all polynomial superforms

Every upstairs unit logarithm is affine in its own moment coordinate, so $d'd''t_f=0$ **as a form**. Therefore $d'd''\delta_i=0$, in addition to $(d')^2=(d'')^2=0$. Differentiating (12) gives exact descended representatives of

$$
\begin{aligned}
d'\delta_i\wedge d'\delta_j&=\pi^*(d'L_{ij}^{d'}),\\
d''\delta_i\wedge d''\delta_j&=\pi^*(d''L_{ij}^{d''}),\\
d'\delta_i\wedge d''\delta_j&=\pi^*(d'L_{ij}^{d''}).
\end{aligned} \tag{13}
$$

There is no symmetry assumption on $i,j$ in the mixed identity. Antisymmetric mixed combinations and pure-prime pairs are thus covered as well. The formulas are valid through the fixed locus $\delta=0$, with no division by $\delta_i$ or its square. They are identities in the sheaf, not just in an ambient tensor algebra.

In the real-linear coordinates $s_i,\delta_i$, the involution fixes $s_i,d's_i,d''s_i$ and changes the sign of each $\delta_i,d'\delta_i,d''\delta_i$. An invariant polynomial superform is a sum of monomials containing an even number of these anti-invariant symbols, counting differential occurrences as well as scalar powers. This follows by using the free polynomial/exterior monomial basis and comparing signs. Pair the anti-invariant symbols in each monomial, with the usual graded signs when reordering differentials. The possible pairs are exhausted by (5), (12) and (13). The invariant symbols $s_i,d's_i,d''s_i$ already descend by norms. Multiplication and wedge of their ordinary downstairs representatives produce the exact descendant of every monomial and hence every invariant polynomial superform.

All required norms, traces, coefficients $v_i$, and differences $e_{ij}$ were chosen for the original finite list and its pair products. They are independent of polynomial degree. This proves Theorem A with one finite unit list and one shrink. It neither promotes scalar polynomial approximation to form descent nor assumes smooth invariant-function theory.

## 6. Local invariant ordinary tests and Euclidean approximation

Let $\beta$ be an invariant ordinary $(p,q)$ form defined near the full fibre over $x_0$.

If the fibre is a singleton, choose an ordinary moment chart $f=(f_1,\ldots,f_m)$ with $\beta=f_{\mathrm{trop}}^*\gamma$ for a Euclidean smooth coefficient superform $\gamma$. Replace its neighbourhood by its intersection with its conjugate, and shrink downstairs so the scalar affinoid lies inside it. The chart and the ambient extension from Section 2(3) give coefficients on a neighbourhood of the compact moment images. A Euclidean cutoff equal to one near those images extends $\gamma$ to all of $\mathbb R^m$ without changing its pullback. The invariant coefficient superform

$$G=\tfrac12(\operatorname{pr}_1^*\gamma+\operatorname{pr}_2^*\gamma) \tag{14}$$

on $\mathbb R^{2m}$ pulls back to $\beta$ by the tuple $(f,\sigma f)$. Its invariance includes the differential factors. Apply Sections 4--5 and shrink once further. Fix a swap-stable compact box $L$ with the retained moment image in its interior.

There exist invariant polynomial coefficient superforms $P_j$ with

$$\max_{I,J}\max_{|\nu|\leq2}\sup_L|\partial^\nu(G_{I,J}-(P_j)_{I,J})|\longrightarrow0. \tag{15}$$

Here the indices refer to the fixed standard differential basis of $\mathbb R^{2m}$. For completeness, extend each smooth coefficient near $L$ by a compactly supported smooth coefficient equal to it there. Gaussian convolution converges uniformly through order two: differentiate under the integral, use uniform continuity of the compactly supported derivatives, and split into a small ball and the Gaussian tail. For fixed Gaussian width, uniformly replace the exponential kernel and its first two derivatives on the compact coefficient and box domains by finite Taylor sums. Integrating produces polynomial approximants with the same derivative control. Choose widths tending to zero and sufficiently long finite sums. Apply this to every coefficient and average each resulting superform with its coordinate-swapped pullback. That operation permutes differential indices with fixed signs and preserves the $C^2$ error bound on the swap-stable box. This proves (15).

Theorem A gives exact ordinary downstairs forms $b_j$ with $\pi^*b_j=P_j(t_f,t_{\sigma f})$. Approximation is measured in the **fixed upstairs** moment tuple in (15), not in the nonlinear reconstructed downstairs coefficients.

If the fibre has two points, choose disjoint ordinary neighbourhoods $N_1,N_2=\sigma N_1$ with a moment representation $f^*\gamma$ on $N_1$. Shrink downstairs until $V_E\subset N_1\cup N_2$. Glue each unit as $f_i$ on the first piece and $\sigma f_i$ on the second. The pieces are disjoint opens covering the affinoid, so analytic sections and their inverses glue. The glued units are invariant and hence belong to $A^\times$. Invariance of the form, including its differential factors, shows $\beta$ is exactly the pullback of $g_{\mathrm{trop}}^*\gamma$ downstairs. This uses actual analytic gluing, not a covering-space assertion. The same form is used at every approximation stage in this case.

## 7. Fixed supports and differentiated coefficient control

Now let $\beta\in A_c^{p,q}(X_E)$ be invariant. Its support has compact image $C\subset X$. Finitely many ordinary opens $U_i=\operatorname{int}_X(V_i)$ from Section 6 cover $C$. CLD 15.2.9 provides ordinary smooth nonnegative $\chi_i$ with compact support in $U_i$ and $\sum_i\chi_i=1$ near $C$. Put $D=\bigcup_i\operatorname{supp}\chi_i$, a fixed compact set containing $C$.

For each local singleton construction take its $b_{i,j}$; for the two-point case use its exact descendant, independent of $j$. Set

$$\alpha_j=\sum_i\widetilde{\chi_i b_{i,j}}, \tag{16}$$

where the tilde is extension by zero from $U_i$. This is ordinary smooth: outside the closed compact support of $\chi_i$, including all points outside $U_i$, an ordinary neighbourhood makes the product zero. Thus it glues to zero with no boundary derivatives. Each $\alpha_j$ is supported in $D$.

If $e_{i,j}$ is the local error $\beta-P_{i,j}(t_{f_i},t_{\sigma f_i})$ on singleton charts, and zero on exact charts, then globally

$$\beta-\pi^*\alpha_j=\sum_i(\chi_i\circ\pi)e_{i,j}. \tag{17}$$

Indeed $\sum_i\chi_i\circ\pi=1$ near the support of $\beta$; off that support, multiplying $\beta$ by any sum still gives zero. All terms are extended by zero as just described.

The full inverse image of $D$ is compact. Cover each $\pi^{-1}(\operatorname{supp}\chi_i)$ by finitely many upstairs affinoid neighbourhoods within $V_{i,E}$ on which $\chi_i\circ\pi$ has a fixed ordinary scalar moment description. Combine its finite unit list with the fixed tuple for $e_{i,j}$. In these fixed enlarged charts, (17) has coefficient errors converging in $C^2$ on fixed compact boxes. The product rule bounds all coefficients of $d'd''((\chi_i\circ\pi)e_{i,j})$ by $M_i\varepsilon_j$, where $\varepsilon_j\to0$ and $M_i$ depends only on the fixed charts and cutoffs. Differential basis factors are separately closed since they are unit-logarithmic factors. This proves Theorem B, including the control required for differentiated pairings.

## 8. Calibrated total-variation estimate in every pure dimension

Assume Theorem C's hypotheses. In one of the fixed upstairs charts, with coordinates $t_1,\ldots,t_r$, a differentiated error top form has the representation

$$\eta_j=\sum_{|I|=|J|=n}H_{I,J,j}(t)\,d't_I\wedge d''t_J,\qquad |H_{I,J,j}|\leq M\varepsilon_j.$$ 

If $r<n$ it is zero. Otherwise put

$$\xi=\sum_{k=1}^r d't_k\wedge d''t_k,\qquad\zeta=\xi^n/n!.$$

For a tangent $n$-volume represented by an $r\times n$ matrix $V$, write $v_I=\det V_I$. Up to the common harmless top-degree ordering sign, contraction of $\eta_j$ is $\sum_{I,J}H_{I,J,j}v_Iv_J$, times the actual positive calibration. Contraction of $\zeta$ is $\sum_I v_I^2$, with the positive ordering convention. Let $N=\binom rn$. Cauchy--Schwarz gives

$$\left|\sum_{I,J}H_{I,J,j}v_Iv_J\right|
\leq M\varepsilon_j\left(\sum_I|v_I|\right)^2
\leq NM\varepsilon_j\sum_Iv_I^2.$$ 

Cellwise positive calibration and the top-form contraction formula therefore give the signed-measure inequality

$$|\eta_{j,\mathrm{Rad},E}|\leq NM\varepsilon_j\,\zeta_{\mathrm{Rad},E}. \tag{18}$$

The dominating positive measure is finite on the compact moment neighbourhood: its compact tropical image has finitely many cells with finite positive canonical calibration, and the coefficient form is smooth. This follows as well from CLD 5.10.1(c,d). Lower-dimensional cells carry no top measure. Matrix symmetry is not needed for this estimate. Actual generic lengths multiply both sides through the same calibration, so no reduction or probability normalization enters.

Applying (18) on the finite fixed cover for each term in (17) and summing bounds gives

$$\bigl\|(d'd''(\beta-\pi^*\alpha_j))_{\mathrm{Rad},E}\bigr\|_{\mathrm{TV}}\longrightarrow0,
\qquad\operatorname{supp}\subseteq\pi^{-1}(D). \tag{19}$$

Overlapping neighbourhoods merely increase the bound. Since $h\circ\pi$ is bounded on that compact set,

$$\mathcal B_{h\circ\pi}(\beta-\pi^*\alpha_j)\longrightarrow0. \tag{20}$$

This proves the differentiated pairing control for $(n-1,n-1)$ tests in all dimensions. Neither scalar $C^0$ density nor a topology on reconstructed downstairs coefficients is used.

## 9. Averaging and the two calibration normalizations

First work with the same-carrier restricted structure $Z_0$ from Section 3. Its involution is a $K$-analytic degree-one isomorphism. CLD 15.4.3, applied to a compact smooth top form $\omega$, gives

$$\sigma_*((\sigma^*\omega)_{\mathrm{Rad},K})=\omega_{\mathrm{Rad},K}.$$

CLD 14.4.3 and the same ordinary sheaf give $\omega_{\mathrm{Rad},K}=2\omega_{\mathrm{Rad},E}$ on this carrier. Cancelling 2 yields

$$\sigma_*((\sigma^*\omega)_{\mathrm{Rad},E})=\omega_{\mathrm{Rad},E}. \tag{21}$$

Pullback commutes with $d'd''$ on the restricted carrier. As $h\circ\pi$ is invariant, signed-measure integration against (21) proves

$$\mathcal B_{h\circ\pi}(\sigma^*\beta)=\mathcal B_{h\circ\pi}(\beta).$$

An arbitrary compact ordinary upstairs test may therefore be replaced by

$$\beta^{\mathrm{av}}=\tfrac12(\beta+\sigma^*\beta).$$

Its support is contained in the compact finite saturation of the original support; equality of supports is neither needed nor asserted. It has exactly the same pairing and satisfies the hypotheses of Theorem B.

For any downstairs compact ordinary $(n-1,n-1)$ form $\alpha$, its pullback is compact by Section 3.2. Smooth functoriality and the **scalar-projection** equality (2), which has no degree factor, give

$$
\begin{aligned}
\mathcal B_{h\circ\pi}(\pi^*\alpha)
&=\int_{X_E}(h\circ\pi)(\pi^*d'd''\alpha)_{\mathrm{Rad},E}\\
&=\int_X h\,(d'd''\alpha)_{\mathrm{Rad},K}
=\mathcal B_h(\alpha).
\end{aligned} \tag{22}
$$

These are finite signed measures on compact supports; boundedness of $h$ there justifies the pushforward integration. This constructs no arbitrary-current pullback.

If the downstairs Hessian vanishes, apply Theorem B and (20) to $\beta^{\mathrm{av}}$. Each approximant's pairing is zero by (22), so the pairing of $\beta^{\mathrm{av}}$, and hence of every upstairs test, is zero. This proves ascent. Conversely, if the upstairs Hessian vanishes, (22) applied to each downstairs test proves descent directly. Thus (1) holds, proving Theorem C.

Every construction localizes to ordinary opens, whose scalar inverse images carry their actual base-changed structures. Iteration of (1) at each quadratic stage is legitimate by the ambient checks in Section 3.3. The composite need not be Galois. No passage to a completed infinite extension is involved.

## 10. Scope, concrete nonempty example and limitations

The theorem imposes a condition on the field extension, not a conditional form-descent or regularization hypothesis. For example $K=\mathbb Q_2$ and $E=\mathbb Q_2(a)$ with $a^2+a+1=0$ satisfy it. A root in $\mathbb Q_2$ would have norm one and yield a root of $Z^2+Z+1$ over $\mathbb F_2$, impossible. The polynomial is thus irreducible, quadratic and separable. Its other root is $-1-a$, and $|a|=1$, $|a-\sigma(a)|=|2a+1|=1$. Characteristic-two extensions satisfying (H) are also allowed: all divisions and averaging in the proof are real, and the invariant-algebra proof uses a kernel calculation over $K$.

Compared with the original catalogue, this result is neither recognition on coordinate products nor recognition under scalar stability imposed as a hypothesis. It proves automatic current-equation transport for **arbitrary** good separated strict boundaryless pure-dimensional analytic spaces, including nonproduct singular and nonreduced spaces, under the specified quadratic extension. The preceding fallible scalar draft did not prove the higher-dimensional ordinary gate. Sections 5.1--5.4 supply an actual analytic identity for odd coefficient/differential parity and alternating pairs, and Sections 7--8 supply its differentiated compact-test topology. These are the additional obligations now addressed.

The original P06.2 asks for classical pluriharmonic recognition or a strict analytic counterexample for general continuous zero-Hessian functions. No such general recognition follows from (1). In particular the following are still unproved here:

* quadratic extensions lacking (H), including the separate wild cancellation problem;
* general finite-Galois and nongalois separable extensions outside the stated finite quadratic towers;
* completion of infinite algebraic extensions and transcendental analytic extensions;
* ordinary two-sign psh regularization and the universal classical curve-test bridge;
* unrestricted exact invariant ordinary smooth form descent (only differentiated approximation is proved);
* recognition on arbitrary analytic germs outside the catalogue's verified scopes.

For extensions lacking (H), two traces may both have norm below $\max(|f|,|\sigma f|)$, so (4) is not established. The orbital identity (10) does not repair that scalar failure. No omitted proof is a counterexample. The non-strict arbitrary-radius catalogue counterexample is outside both the theorem and the original strict counterexample scope. We assert neither ordinary smoothness, weak smoothness, real-PL regularity nor classical harmonicity of $h$ from (1) alone. No recognition or regularization theorem from the catalogue is a premise.

## 11. Audit and reproduction

The authoritative argument is this file, `P06.2-argument.md`; the complete standalone companion is `P06.2-partial.tex` and its compiled PDF. `self-audit.md` checks the exact new differential identities, unit/nonunit cases, all bidegrees, fixed supports, upstairs derivative control and the two field normalizations. `research-notes.md` preserves failed routes and remaining obligations. `status.json` has exactly the five requested keys. `source-manifest.json` records cached primary versions and bytes. `evidence/artifact-hashes.json` records final artifact hashes.

Run `python build-and-check.py` in this workspace. It performs only lightweight exact polynomial/exterior diagnostics, extracts the inspected cached source ranges, regenerates the standalone TeX with installed Pandoc, compiles it twice with installed pdfLaTeX, extracts PDF text, and records commands, outputs, environment and hashes. Source extraction is also reproducible by `pdftotext -layout sources/CLD.pdf sources/CLD.txt`, and similarly for the other PDFs. No installation, network retrieval, other model call, agent, old-workspace write or heavy computation is used or required.

The diagnostics check finite algebraic identities and typesetting. They do not verify an analytic theorem. This is an unverified author draft with a self-audit, and no independent audit verdict is attributed to the preceding packet or this one.

## Bibliography

* A. Chambert-Loir and A. Ducros, *Formes différentielles réelles et courants sur les espaces de Berkovich*, arXiv:1204.6277v2, 25 July 2025. Used exact statements: Lemma 1.9.4; §§3.3.3, 3.3.12; Propositions 3.4.1, 3.4.4; §§5.4.4, 5.8; Proposition 5.10.1; §§6.2.1--2, 7.3.5, 11.1--2, 11.4.4, 13.3.3, 14.3--4; Propositions 15.1.1, 15.3.1, 15.4.3; §15.2.2, Corollary 15.2.9, Theorem 15.7.1 and §15.7.2.
* W. Gubler and J. Rabinoff, *Classically psh and pluriharmonic functions on Berkovich spaces*, arXiv:2506.13548v2, 17 September 2025, §2.11(5').
* W. Gubler, P. Jell and J. Rabinoff, *Forms on Berkovich spaces based on harmonic tropicalizations*, arXiv:2111.05741v3, 7 March 2025, Proposition 14.2. Inspected only to distinguish weakly smooth descent; not used as a premise.
* B. Conrad and M. Temkin, *Descent for non-Archimedean analytic spaces*, arXiv:1912.06230v2, 10 April 2021. Cached comparison source, not an ordinary-form premise.
* Exact supplied original P06.2 dossier and preceding restricted-quadratic packet. Mathematical task and fallible comparison data only; no imported theorem assumption.



# Complete supporting proofs supplied for independent reconstruction

These are mathematical evidence, not grants of assumptions. Each application and dependency must be reconstructed. Prior verdicts and hashes do not replace these proofs.
