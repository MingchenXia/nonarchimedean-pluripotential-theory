# Independent reconstruction of P12.5

This is a mathematical draft, relative only to the **entire qualified G331 and B341** reproduced in the accompanying TeX appendices. Their mandatory annotations, ledgers, scopes, acceptance records and the literal SH 17.4.7 qualification remain attached. G331 supplies the independently geometric function cones and their comparison, approximation and full conductor descent. B341 supplies the bounded **algebraic** mixed moment operator. Neither supplies the higher-dimensional Cartier bridge, locality, or energy results proved below. The native250 candidate and ROOT342/344/346 are data examined here, not premises. A successful computation, a hash, or an acceptance label is not a mathematical proof.

## 1. Domain, conventions, and theorem

Let $(R,\mathfrak m)$ be excellent local. We use its reduction, still denoted $R$, and $n=\dim R$. Fix a proper $\mathfrak m$-primary ideal $\mathfrak a$. For $n>0$ let
$$X=X_{\mathfrak a}=\{v:v(\mathfrak a)=1\}.$$
These are centred real semivaluations with all prime supports retained; no minimal-support restriction is imposed. By qualified G331 this is compact Hausdorff. Primary values are positive finite continuous bounded functions. Units have value zero. The independently geometric core consists of evaluations of actual negative effective finite real Cartier presentations on actual primary blowups, with nonnegative degree on every contracted integral proper curve. Its uniform closure is $C$; its actual decreasing-$C$-net completion is $D$. The comparison $C=C_{\rm ideal}$, $D=D_{\rm ideal}$ and their full finite-injection/conductor descent are G331 grants. In particular $C,D$ are nonpositive cones, stable under addition, nonnegative scaling and finite maximum. No increasing closure or arbitrary infimum closure of $D$ is assumed. Write $D^{\rm bd}$ for its bounded finite-valued part.

Put $p=n-1$. Qualified B341 supplies a positive finite Radon moment measure $\mu(u_1,\ldots,u_p)$ for bounded $D$ inputs, characterized for rational primary profiles by
$$\int v(J)\,d\mu(-v(I_1)/k_1,\ldots,-v(I_p)/k_p)
=\frac{e_R(I_1,\ldots,I_p,J)}{\prod_i k_i}.$$
Unit entries give zero. The kernel is symmetric, additive and homogeneous in its negative input cone; scalar gauge moments are ordered. Uniform continuity and decreasing-net weak continuity apply with a common bound and a **specified limit in $D^{\rm bd}$**. Scalar moment order is not order of measures. B341 also gives the one-factor primary-gauge identity and residue-weighted degree-$n$ normalization identity in this bounded algebraic setting. Our proofs extend and geometrically identify this operator; they do not import those missing conclusions from B341.

All degree-$n$ operations use the maximal dimension of $R$. Lower-dimensional normalization centres remain in $X,C,D$ and in all fibre conditions, but have zero degree-$n$ contribution. Their separate-dimensional products would have another arity. Nilpotent generic lengths are not reconstructed from the reduced boundary. In dimension zero the boundary is empty and the unique energy and measure are zero. In dimension one the product has zero potential entries, treated directly in Section 9.

For $u\in D$ set $u^k=\max(u,-k)$, where the constant is $-k v(\mathfrak a)$ before choosing the section. Sections 2--5 construct a symmetric bounded $n$-form $F$ with
$$F(v,u_1,\ldots,u_p)=\int(-v)\,d\mu(u_1,\ldots,u_p)\quad(v\in D^{\rm bd}),$$
and identify its core restriction with minus an independently defined supported Cartier intersection. Define
$$F_\infty(u_1,\ldots,u_n)=\sup_{k_1,\ldots,k_n}F(u_1^{k_1},\ldots,u_n^{k_n}),\qquad
E(u)=-\frac1n F_\infty(u^{[n]}),\qquad
\mathcal E^1=\{u\in D:F_\infty(u^{[n]})<\infty\}.$$
Brackets indicate repeated slots, never ideal powers. We prove this class is a cone; it has canonical finite Radon mixed measures, extended test pairings, full decreasing-net continuity with specified $D$ limits, variation and reference formulas, and exact gauge and conductor rules. We also prove bounded Borel strict-maximum locality, nonpolar cutoff identities, total variation convergence for canonical integer truncations, comparison, capacity absolute continuity, decreasing-net convergence in capacity and quasicontinuity. These additional conclusions require Sections 10--13, not just weak approximation.

The polar class is specified precisely: poles of $z\in D$ with finite reference moment $\int(-z)\,d\mu((-1)^{[p]})$. Section 13 proves a branchwise Izumi reduction identifying that condition with exclusion of an entire bottom restriction on every top-dimensional normal centre. All finite-energy functions qualify. A globally nonbottom function which is bottom on one top-dimensional branch need not qualify. No whole bottom branch is called negligible. No general Choquet compact-above assertion, arbitrary-net total variation convergence, equation uniqueness, or complete P12.6 is claimed.

## 2. Supported Cartier intersection without a coefficient field

Let $Y\to\operatorname{Spec}R$ be an actual primary blowup, and let $E$ be an effective exceptional **Cartier** divisor. All components of $Y$ dominate positive-dimensional reduced components of $R$ (G331); its primary ideal is locally generated by a regular element. Some power of $\mathfrak m$ kills $\mathcal O_E$: on finitely many affine charts the closed-fibre support gives this containment, and a common exponent works. Thus $E$ is proper over $R/\mathfrak m^N$. Every coherent cohomology group has finite $R$-length. Define $\chi_R$ as the alternating sum of those lengths.

For invertible bundles $L_1,\ldots,L_s$ on $E$, the full proper Euler-polynomial statement Stacks 0BEL gives that
$$\chi_R(E,\bigotimes_i L_i^{t_i})$$
is polynomial for all integer $t_i$, of degree at most $\dim E$. Here is the precise reduction to its field version: filter $\mathcal O_E$ by the finite powers of $\mathfrak m$. Each quotient is a coherent sheaf over the residue-field scheme $E_k$. Tensoring with invertible bundles preserves the filtration; cohomological Euler additivity applies. An $R$-length of a $k$-vector space equals its $k$-dimension. No coefficient-field embedding in $R/\mathfrak m^N$ is used. For every top-dimensional integral component $Z$ the multiplicity in the resulting leading coefficient is
$$\sum_j\ell_{\mathcal O_{E_k,\eta_Z}}((\mathfrak m^j\mathcal O_E/\mathfrak m^{j+1}\mathcal O_E)_{\eta_Z})
=\ell_{\mathcal O_{E,\eta_Z}}(\mathcal O_{E,\eta_Z}).$$
This is the full generic Artinian thickness, not the reduced fibre multiplicity. The equality is composition-series additivity in the generic Artinian local ring; the filtration quotients have its residue field as simple factors. The top coefficient is therefore the usual intersection on this cycle with these lengths, by the full 0BEL cycle/intersection theorem.

For integral exceptional Cartier divisors $D_1,\ldots,D_p$ define $Q_Y(D_1,\ldots,D_p,E)$ to be the coefficient of $t_1\cdots t_p$ in
$$\chi_R(E,\mathcal O_Y(\sum_i t_iD_i)|_E).$$
Equivalently it is the $p$-fold finite difference; lower-degree terms vanish. It is additive in the first slots by polynomial substitution. Additivity in the last slot follows from
$$0\longrightarrow\mathcal O_{E_1}(-E_2)\longrightarrow\mathcal O_{E_1+E_2}
\longrightarrow\mathcal O_{E_2}\longrightarrow0.$$
Tensoring by the variable invertible bundle and taking Euler characteristics shows the twist $-E_2$ changes only lower coefficients, so $Q(\boldsymbol D,E_1+E_2)=Q(\boldsymbol D,E_1)+Q(\boldsymbol D,E_2)$.

Symmetry with the last slot must also hold when two cuts have common components. Use the supported Koszul complexes $K_E=[\mathcal O(-E)\to\mathcal O]$, $K_H=[\mathcal O(-H)\to\mathcal O]$. Their derived tensor is supported on the closed fibre and is symmetric under exchanging its factors, even if the cuts are improper. Tensor with $L$; its Euler characteristic is computable from either two-term presentation, giving
$$\chi_R(E,L|_E)-\chi_R(E,L(-H)|_E)
=\chi_R(H,L|_H)-\chi_R(H,L(-E)|_H).$$
For clarity this does not subtract undefined infinite Euler characteristics on $Y$: compute the second Koszul differential on $L|_E$, whose two terms have proper Artinian support, or in the reverse order. Both compute the same bounded supported complex. Set $L=\mathcal O(tH+sE+\sum_{j=1}^{n-2}r_jG_j)$. Take the coefficient of $\prod r_j$ in the two differences at $t=s=0$. Only terms of total degree $n-1$ with one $H$, respectively one $E$, survive; powers at least two would exceed that degree. The signs of the two finite differences are the same. Hence $Q(H,\boldsymbol G,E)=Q(E,\boldsymbol G,H)$. For $n=1$ there is only one slot and no symmetry step.

Every integral exceptional Cartier divisor is a difference of effective exceptional Cartier divisors by the actual Cartier order-unit assertion in G331. Extend $Q$ by differences and finite real combinations. Additivity makes this extension independent of the choice of positive parts; the Koszul symmetry makes it a symmetric real $n$-form. This is an independent local intersection, not a definition using mixed-multiplicity moments.

### Actual cycle projection and nonpure dimensions

If $f:Y'\to Y$ is a common primary-model refinement, then for an effective exceptional $E$
$$f_*[f^*E]_{n-1}=[E]_{n-1}$$
as **actual cycles before quotienting by rational equivalence**. Stacks 0AYA, especially its componentwise divisor-cycle projection assertion, applies separately to each dominating integral component. All these component maps are birational, of generic degree one. Lower-dimensional components have no degree-$n$ cycle. Dimension comparisons use the catenary dimension convention of 02QL; excellence supplies universal catenarity. In particular a height-one point on a dimension-$d$ component has closure dimension $d-1$, so one does not promote a cut on a smaller component to dimension $n-1$.

One can check the multiplicities directly. At a relevant codimension-one point the reduced local ring $A$ is one-dimensional. It injects into the sum of its domain component quotients, with finite-length cokernel $T$. For a regular equation $g$, the multiplication snake sequence shows the discrepancy in the two quotient lengths is $\ell(T/gT)-\ell(T[g])=0$. These two lengths coincide by the multiplication sequence on the finite-length module $T$. On each component the divisor-cycle projection gives the order times its residue degree. Summing recovers exactly $\ell_A(A/gA)$. Thus embedded thickness of the cut and the genuine residue degrees are preserved; there is no nonnormal Weil-coefficient replacement for actual Cartier effectivity.

Apply the numerical projection formula on each proper integral component of the supported cycle. It proves
$$Q_{Y'}(f^*D_1,\ldots,f^*D_n)=Q_Y(D_1,\ldots,D_n).$$
Passing first to a global Chow class would be invalid here: a principal parameter on a DVR has supported degree one, whereas its class can be zero in the global affine Chow group. The supported cycle proof avoids this loss.

### Raw Rees sections and the ideal diagonal

Let $Y=\operatorname{Bl}_I R$, $E_I$ its actual exceptional Cartier divisor, $D_I=-E_I$, with $\mathcal O(D_I)$ the ample tautological bundle. Stacks 0AG7, applied to the **raw** finitely generated Rees algebra, gives
$$H^0(Y,\mathcal O(qD_I))=I^q\quad(q\gg0).$$
Stacks 0B5S gives Serre vanishing for this ample bundle. The exact sequence cutting $E_I$ consequently gives
$$\chi_R(E_I,\mathcal O((q-1)D_I)|_{E_I})=\ell_R(I^{q-1}/I^q)\quad(q\gg0).$$
Compare leading coefficients with the Samuel polynomial: the right side has leading coefficient $e_R(I)/(n-1)!$. The left has $Q_Y(D_I^{[p]},E_I)/(n-1)!$. Therefore
$$-Q_Y(D_I^{[n]})=e_R(I).$$
For several primary ideals use their common product blowup. For positive integers $t_i$, $\sum_i t_iD_{I_i}$ is the divisor of the product ideal $\prod_i I_i^{t_i}$ on that model, which maps to its blowup by 01OF's universal property. The diagonal identity and the mixed length polynomial imply polynomial equality in all $t_i$. The coefficient of $t_1\cdots t_n$ is $n!$ times the corresponding mixed coefficient on both sides. Hence
$$-Q(D_{I_1},\ldots,D_{I_n})=e_R(I_1,\ldots,I_n).$$
Unit slots are zero. This proves the ideal intersection comparison without using a normalized-Rees section formula or a finite-window guess for the polynomial's stabilization.

## 3. Positive real Cartier atoms, refinement, and the fixed-primary bridge

Normalize a primary model $Y$ componentwise; excellence makes this finite. Call it $N$. For each prime $Z$ of dimension $p$ in its closed fibre, the normal generic local ring is a DVR. Let $\nu_Z$ be its order, $b_Z=\nu_Z(\mathfrak a)>0$, and $v_Z=\nu_Z/b_Z\in X$. For negative real curve-nef core divisors $D_i$ set
$$\mu_Y(D_1,\ldots,D_p)=\sum_Z b_Z\,\deg_R(D_1|_Z\cdots D_p|_Z)\,\delta_{v_Z}.$$
The degree is the field intersection on the proper integral $R/\mathfrak m$-scheme $Z$, including its actual residue-field degree. Normalization plus the supported cycle projection in Section 2 proves, for every exceptional real Cartier test $H$,
$$\int H_H\,d\mu_Y=Q_Y(H,D_1,\ldots,D_p).$$
Indeed the pullback of $H$ has coefficient $\nu_Z(H)$ on $Z$, and $H_H(v_Z)=\nu_Z(H)/b_Z$. This accounts for the one normalization factor in the atom, and retains inseparable residue degrees.

These atoms are positive **before** comparison with ideal measures. The restrictions $D_i|_Z$ are real curve-nef. By the entire qualified G331 real ample-perturbation result, perturb each $D_i$ on the original $Y$ by $-\varepsilon E_I$ and approximate within its fixed finite coefficient span by rational ample classes, retaining actual negativity. Pullback by the finite normalization preserves ampleness (01VG) and restriction to proper $Z$ is ample. After clearing denominators the ample mixed degrees are positive, by full 0BEL. The degrees are finite polynomial functions of the finitely many coefficients, so their limits are nonnegative. This argument works on nonnormal/nonreduced fibres and arbitrary residue fields; no singular resolution or unstated normal-model positivity theorem is inserted. For $p=0$ the degree is the residue degree of a point.

Refinement independence is likewise prior to ideal comparison. Between normal component models, a prime on the new model whose image has dimension below $p$ contributes zero to the intersection of $p$ pulled-back bundles, by numerical projection. A prime dominating $Z$ has the same fraction field; the proper birational map over the normal DVR at $\eta_Z$ is an isomorphism there. Alternatively the divisor-cycle projection of a uniformizer gives a sum of positive integral orders times residue degrees equal to one, forcing a single order-one, residue-degree-one contributor. Its valuation, $b_Z$, and intersection weight are unchanged. Thus the atomic measure is unchanged. Componentwise normalization of a common product refinement provides a comparison model. Lower components are not deleted; they simply have no dimension-$p$ contribution.

Here is the missing uniform-function-to-intersection bridge. Fix **one** model $Y=\operatorname{Bl}_I R$. G331 gives finite $T=H^0(Y,\mathcal O_Y)\subset Q(R)$ and an integer $h$ with $\mathfrak m^h(T/R)=0$. Fix once
$$\mathfrak c_0=\mathfrak m^{h+1},\qquad \mathfrak c_0T\subset\mathfrak m\subset R.$$
This is primary, not the possibly nonprimary normalization conductor. For a negative rational ample exceptional $L$ and sufficiently divisible large $q$, $\mathcal O(qL)$ is globally generated. Put
$$J_{q,L}=\mathfrak c_0 H^0(Y,\mathcal O(qL)).$$
This is an actual ideal of $R$, contained in $\mathfrak m$, and unit off $\mathfrak m$; hence proper primary. On the single refinement
$$Y'=\operatorname{Bl}_{I\mathfrak c_0}R,\qquad D_0=-E_{\mathfrak c_0},$$
the exact image of the pulled-back generating map gives
$$J_{q,L}\mathcal O_{Y'}=\mathcal O_{Y'}(qf^*L+D_0).$$
Right exactness suffices: the original evaluation map is surjective, its pulled-back image is the indicated invertible sheaf, and the primary correction is invertible on $Y'$. This equality concerns actual ideal sheaves with regular generic generators, not just numerical classes. Thus $Y'$ maps to $\operatorname{Bl}_{J_{q,L}}R$ by 01OF.

At every semivaluation support the pulled-back invertible module has a generating section with a unit coefficient at its valued centre. Consequently
$$-v(J_{q,L})/q=H_L(v)-v(\mathfrak c_0)/q.$$
This is uniform on all of $X$, since $\mathfrak c_0$ is primary. More importantly Section 2 and the exact image equality give
$$\frac{e_R(J_{q_1,L_1},\ldots,J_{q_n,L_n})}{\prod_iq_i}
=-Q_{Y'}(f^*L_1+D_0/q_1,\ldots,f^*L_n+D_0/q_n).$$
The right side converges by finite-coefficient polynomial continuity on this **fixed** refinement. Uniform functional approximation alone would not prove this identity or convergence.

Approximate real negative curve-nef $D_i$ on $Y$ by negative rational ample $L_{i,j}$ in their finite span, using G331, then take divisible $q_i$ large. The same $\mathfrak c_0,Y',D_0$ works for every $j$ and every slot. B341's uniform continuity, the displayed all-support profile identity and this finite-coefficient intersection convergence give
$$F(H_{D_1},\ldots,H_{D_n})=-Q_Y(D_1,\ldots,D_n).$$
In this formula $F$ on continuous inputs can equivalently be defined by the bounded polynomial kernel in Section 5. To identify the atomic measure it is enough to fix every primary ideal test $-v(J)$, which is another core divisor, and use the same comparison on a common fixed model. These ideal test differences are uniformly dense in all continuous tests by G331. The atom pairing and B341 moments are equal on that dense class, and both measures are finite. Thus the independent positive atomic operator equals the bounded algebraic operator on every real core tuple. Arbitrary Cartier tests follow by differences using the Cartier order unit. This is the geometric bridge, not an appeal to a provenance label.

## 4. Strict maximum identity and ordinary open locality

First take rational ideal profiles $u=-v(A)/q$, $v=-v(B)/q$, and core data in all other slots. Use a common primary model where $A,B,S=A+B$ are invertible. The ratios $L=A\mathcal O/S\mathcal O$ and $M=B\mathcal O/S\mathcal O$ are legitimate actual subideals, and $L+M=\mathcal O$. At a fibre prime $Z$ where $u(v_Z)>v(v_Z)$, $M|_Z\to\mathcal O_Z$ vanishes generically and hence identically on integral $Z$. The surjectivity of $L+M$ then makes $L|_Z\to\mathcal O_Z$ an isomorphism. The restrictions of the $A$ and $S$ divisor bundles therefore coincide on $Z$, as do their atomic weights with the other slots fixed. This proves the strict-max identity at the atom level. It does not divide a noninvertible ideal by a rational function on a nonnormal model.

Uniform rational approximation extends it to continuous $C$ inputs. Explicitly, take a continuous test with compact support $K\subset\{u>v\}$; the gap has a positive minimum on $K$, so uniform approximation preserves its sign there. Weak convergence then preserves the tested identity. On a compact Hausdorff space, equality on such legitimate continuous tests gives equality of the Radon restrictions to the open strict set. Approximate the other bounded $D$ slots by their actual bounded decreasing $C$ nets and use B341 weak continuity on the same fixed test. Thus strict-max locality holds when the compared entries are continuous and the other slots bounded $D$.

For ordinary open locality let bounded $u,v\in D$ agree on an open $U$, fix the other bounded slots, and fix a continuous test supported in compact $K\subset U$. Choose actual decreasing continuous representations $u_\alpha\downarrow u$, $v_\beta\downarrow v$. For fixed $\alpha$ and $\varepsilon>0$, the open sets
$$\{v_\beta-\varepsilon<u_\alpha\}$$
cover $K$, since their limits equal $u$ on $K$. A finite subcover and directedness give one $\beta$ and all its successors. Continuous strict-max locality makes the tested measure of $u_\alpha$ equal that of $\max(u_\alpha,v_\beta-\varepsilon)$. Let $\beta$ decrease to its specified bounded $D$ limit $\max(u_\alpha,v-\varepsilon)$, then let $\alpha$ decrease to $\max(u,v-\varepsilon)$. These maxima belong to $D$ by its finite-max rule. This gives the tested equality with $u$. Interchange $u,v$ and use the second compact cover to obtain the analogous equality with $v$. Finally both maxima are within $\varepsilon$ of $\max(u,v)$, globally; bounded uniform continuity lets $\varepsilon\downarrow0$. The tested measures of $u,v$ coincide. Radon regularity gives equality on $U$; replacing finitely many slots one at a time proves full bounded open locality. There is no measurable-net monotone-convergence step and no increasing-$D$ completion step here.

## 5. The full bounded symmetric form and discontinuous tests

On rational profiles define
$$F(-v(I_1)/k_1,\ldots,-v(I_n)/k_n)=e_R(I_1,\ldots,I_n)/\prod_i k_i.$$
B341 supplies its presentation independence, symmetry, cone multilinearity and order. For entries in $[-M,0]$, negative-constant shifts and expansion imply
$$|F(\boldsymbol u)-F(\boldsymbol w)|\le[(M+\varepsilon)^n-M^n]e_R(\mathfrak a)$$
if every coordinate differs uniformly by at most $\varepsilon$. Rational slightly larger bounds remove rationality restrictions. Uniform approximation defines the same form on $C$. For bounded $D$ tuples take the finite product of their actual decreasing $C$ representations. Form values increase and are bounded by $M^n e_R(\mathfrak a)$. Define $F$ as their supremum.

Representation independence follows from a compact **continuous** strict cover: for fixed majorants $h_i\in C$, $h_i\ge u_i$, the sets $\{g_{i,\alpha}<h_i+\varepsilon\}$ cover $X$. One index works in each of the finitely many slots. Thus $g_{i,\alpha}-\varepsilon\le h_i$; shift expansion bounds the discrepancy by the displayed vanishing error. Reversing two representations proves independence. It also proves the exact formula
$$F(\boldsymbol u)=\sup\{F(h_1,\ldots,h_n):h_i\in C,\ h_i\ge u_i\}.$$
Here all majorants inherit the common bound from the bounded target. The same compact cover for upper-semicontinuous bounded $D$ nets proves full decreasing-net continuity when the specified limit belongs to $D^{\rm bd}$ and all entries have a common bound. Addition is obtained by product nets of continuous summands; scaling and symmetry pass through the scalar limits. This proves the full $n$-form, not just an $(n-1)$-slot weak operator.

We need a Radon directed-integral lemma, not general measurable-net monotone convergence. If $f_\alpha\ge0$ is an increasing net of continuous functions on a compact Hausdorff space and $f=\sup f_\alpha$, then for a finite Radon measure $\sigma$
$$\int f\,d\sigma=\sup_\alpha\int f_\alpha\,d\sigma.$$
Indeed $f$ is lower semicontinuous. Inner regularity of its open superlevels, finitely many level steps and Urysohn cutoffs show that its integral is the supremum of integrals of continuous nonnegative minorants. For any such minorant $h$ and any $\varepsilon>0$, the open sets $\{f_\alpha>h-\varepsilon\}$ cover the compact space; directedness selects one index. This proves the formula, also for infinite integrals. A pointwise increasing net of arbitrary measurable functions would not justify the same argument.

For bounded $v\in D$ choose an actual continuous representation $g_\alpha\downarrow v$. Against fixed bounded $\mu(\boldsymbol u)$ the lemma applied to $-g_\alpha$ computes the integral of $-v$. For fixed continuous $g_\alpha$, B341 weak convergence in the other slots identifies its integral with the corresponding limit of $F$. All these nonnegative scalar suprema commute over the finite product of directed sets. It follows that
$$\int(-v)\,d\mu(\boldsymbol u)=F(v,\boldsymbol u)$$
for every bounded **discontinuous** $D$ test. In particular this pairing is symmetric in all $n$ entries. It is the additional test-continuity statement needed in the Borel and finite-energy arguments below.

## 6. Conditional Cauchy, full Hölder, and concavity

The required mixed inequality is
$$F(a,b,c_3,\ldots,c_n)^2\le F(a,a,c_3,\ldots,c_n)F(b,b,c_3,\ldots,c_n).\tag{6.1}$$
For ideals this is proved by reducing all three expressions over the **same** sequence of quotients, not by separately choosing reductions. If the residue field is finite, pass algebraically to $R(Z)=R[Z]_{\mathfrak mR[Z]}$. Full SH 8.4.1--2 gives faithful flatness and equal dimension. To check lengths exactly, tensor a finite composition series: each residue-field factor becomes $k(Z)$ and has length one over the new local ring. Thus all length polynomials and coefficients agree. No boundary identification under this transcendental extension is asserted.

Over the infinite residue field, in the slot $K_3$ choose a superficial element simultaneously for the three tuples $(I,I,K_3,\ldots)$, $(I,J,K_3,\ldots)$ and $(J,J,K_3,\ldots)$, avoiding every minimal prime of the current quotient. Full SH 17.2.1--4 supplies each allowed set as the complement of finitely many proper subspaces in $K_3/\mathfrak mK_3$. Their finite intersection still has a rational point. At each next slot repeat in the same quotient ring for the three remaining tuples. Avoiding the minimal primes makes its dimension drop exactly one: the upper bound follows from avoidance, and the lower bound from lifting a system of parameters and the height theorem. Nonreduced, embedded and nonpure quotient components are allowed.

For completeness the annihilator correction is finite. The eventual-colon assertion in SH 17.2.4 implies $(0:x)\cap AM=0$ for a sufficiently deep primary product $A$. Therefore $(0:x)$ injects into $M/AM$ and has finite length. In dimension greater than one its contribution is below the leading degree, so SH 17.4.6 reduces the mixed coefficient exactly. At the final dimension-one reduction its finite annihilator term must be kept. The literal SH 17.4.7 printed colon length must be read as
$$\ell\big(0:_{M/(x_1,\ldots,x_{d-1})M}x_d\big)
=\ell\big(((x_1,\ldots,x_{d-1})M:x_d)/(x_1,\ldots,x_{d-1})M\big).$$
The unquotiented printed colon can have infinite length. In a regular parameter sequence this finite quotient annihilator is zero; outside that case we do not discard it or assert a regular sequence.

After $n-2$ simultaneous cuts, full SH 17.7.1--3 applies in dimension two. Here is the essential inequality at its actual hypotheses. By SH 8.3.7/9 replace $I$ by a two-generated minimal reduction $(a,b)$ without changing multiplicities. The length inequality used in 17.7.1, followed by the dimension-two parameter bound (SH 11.2.9--10), gives, for positive integers $r,s$,
$$e(I^rJ^s)\le2r^2e(I)+2s^2e(J).$$
Product linearity expands its left side as $r^2e(I)+2rs e(I,J)+s^2e(J)$. Hence
$$2rs e(I,J)\le r^2e(I)+s^2e(J).$$
Optimize over positive rational $r/s$ (dense in the positive reals) to get $e(I,J)^2\le e(I)e(J)$. The source proof applies to arbitrary Noetherian local dimension-two rings with infinite residue field; it does not assume Cohen--Macaulayness. The same quotient sequence in the preceding paragraph proves (6.1) for arbitrary fixed mixed slots. Power scaling gives rational profiles, and uniform and actual decreasing continuity give bounded $C,D$ inputs. Unit or zero entries follow directly, or by adding a vanishing negative primary constant before taking limits.

This conditional inequality implies the **full** Hölder bound
$$F(u_1,\ldots,u_n)\le\prod_{i=1}^n F(u_i^{[n]})^{1/n}.\tag{6.2}$$
Here is a finite proof, avoiding an unexplained invocation of generalized Alexandrov--Fenchel. First perturb each input by a positive multiple of $r=-1$, so all relevant form values are positive. On the finite integer simplex $\{\alpha\in\mathbb N^s:|\alpha|=n\}$ set
$$H(\alpha)=\log F(u_1^{[\alpha_1]},\ldots,u_s^{[\alpha_s]})-\sum_i\frac{\alpha_i}{n}\log F(u_i^{[n]}).$$
It is zero at the vertices. Whenever $\alpha_i,\alpha_j>0$, (6.1) gives $2H(\alpha)\le H(\alpha+e_i-e_j)+H(\alpha-e_i+e_j)$. If its maximum were positive, choose a maximizing point with the smallest number of nonzero coordinates. Both neighbours also maximize. Transfer one unit repeatedly from $j$ to $i$; as long as both remain positive the same maximum argument applies. Eventually $j=0$, giving a maximizing point of smaller support, a contradiction. Thus $H\le0$. Apply this to the tuple with each entry once, then let the perturbations vanish using bounded multilinearity. This proves (6.2), including zero diagonal values.

Set $A(u)=F(u^{[n]})^{1/n}$ for bounded inputs, and $\delta=e_R(\mathfrak a)^{1/n}$. Expand $F((u+v)^{[n]})$ and use (6.2) term by term. The binomial theorem gives $A(u+v)\le A(u)+A(v)$, and $A(tu)=tA(u)$ for $t\ge0$. This is a seminorm on the negative cone; nonpure null directions are possible.

For bounded $U,V$ and fixed bounded negative slots $K$, (6.1) shows
$$F(U-V,U-V,K)\ge(\sqrt{F(U,U,K)}-\sqrt{F(V,V,K)})^2\ge0.$$
The form here extends algebraically to differences; $F(U,V,K)$ is nonnegative and at most the geometric mean. For $u_t=(1-t)U+tV$, differentiating its finite polynomial energy gives
$$\frac{d^2}{dt^2}\big[-F(u_t^{[n]})/n\big]=-(n-1)F(V-U,V-U,u_t^{[n-2]})\le0.$$
For $n=1$ the energy is linear and this second derivative assertion is unnecessary. Concavity on unbounded finite-energy inputs follows later by decreasing bounded approximations. Positivity of this signed quadratic form does not imply uniqueness in null directions.

## 7. Truncations, all majorants, and the first unbounded approximation lemma

For arbitrary $D$ inputs the extended form in Section 1 is well defined as a nonnegative supremum. Its independent truncation levels are cofinal with a common integer level. Moreover
$$F_\infty(\boldsymbol u)=\sup\{F(h_1,\ldots,h_n):h_i\in C,\ h_i\ge u_i\}.\tag{7.1}$$
If $h_i\ge u_i$, then for $k_i\ge\|h_i\|_\infty$, $u_i^{k_i}\le h_i$ and bounded form order gives $F(\boldsymbol h)\le F(\boldsymbol u^{\boldsymbol k})$. Conversely each bounded truncation has the bounded all-majorant formula of Section 5; its continuous majorants are also majorants of $u_i$. Taking the suprema proves both directions. This argument does not create a new definition of $D$ or flatten nested nets.

Let $u_i\in\mathcal E^1$ and write $A_i=F_\infty(u_i^{[n]})^{1/n}$. Suppose **bounded** $D$ tuples $f_{i,\lambda}$ decrease to the specified $u_i$, with no common lower bound. Their individual diagonal sizes are at most $A_i$ by order, so bounded Hölder bounds every mixed form by $\prod A_i$. For fixed continuous majorants $h_i\ge u_i$, the open sets $\{f_{i,\lambda}<h_i+\varepsilon\}$ cover $X$. Upper semicontinuity of $f_{i,\lambda}$ and continuity of $h_i$ make these sets open; compactness and directedness select one common index for every slot. Thus $f_{i,\lambda}-\varepsilon\le h_i$. Expand the **bounded** form:
$$F(\boldsymbol h)\le F(\boldsymbol f_\lambda)+\prod_i(A_i+\varepsilon\delta)-\prod_i A_i.$$
For each nonempty subset of shifted slots, Hölder gives the corresponding product of $A_i$ and $\varepsilon\delta$. All constants are target diagonal sizes, independent of the growing sup norms. Send $\varepsilon\downarrow0$, then take (7.1). Together with order this proves
$$F(\boldsymbol f_\lambda)\uparrow F_\infty(\boldsymbol u).\tag{7.2}$$
This is the **first** finite-energy approximation theorem. It has been proved before assuming $\mathcal E^1$ is additive or that $F_\infty$ is multilinear. It also gives extended Hölder directly by taking truncations. In particular $F_\infty(\boldsymbol u)\le\prod A_i<\infty$ for finite-energy entries.

Now prove the cone property. If $u,v\in\mathcal E^1$, $s_k=u^k+v^k$ is bounded $D$, decreases to the already specified $D$ function $u+v$ (G331's addition rule), and bounded Minkowski gives $A(s_k)\le A(u)+A(v)$. Applying the compact-majorant estimate used above to every diagonal majorant of $u+v$, with this fixed bound, and then (7.1), proves $F_\infty((u+v)^{[n]})^{1/n}\le A(u)+A(v)$. Thus the sum is in $\mathcal E^1$. Positive scaling follows from cofinal rescaling of truncation levels; zero is separate and has energy zero.

Only **after** this cone proof use (7.2) for $u^k+v^k\downarrow u+v$ and the other truncated finite-energy slots. Bounded additivity passes to the limits and proves full cone multilinearity of $F_\infty$. Its symmetry, order, Hölder and Minkowski survive. Bounded concavity and pointwise convergence of the finite energies give concavity of $E$ on $\mathcal E^1$. Globally bottom has infinite energy whenever $n>0$, since $F((-k)^{[n]})=k^ne_R(\mathfrak a)$; bottom on a zero-degree lower component can instead be a null direction. Both facts are part of the convention, not a claim that all bottom sets are polar.

## 8. Canonical finite measures, extended tests, and full nets

For $\boldsymbol u\in(\mathcal E^1)^p$, the bounded measures $\mu(u_1^k,\ldots,u_p^k)$ have mass at most $\delta\prod_i A_i$, by (6.2) with the test $r=-1$. Each primary ideal gauge moment tends by (7.2) to
$$F_\infty(-v(J),u_1,\ldots,u_p).$$
Differences of these continuous gauges are uniformly dense in all continuous functions by G331. Their limiting functionals are positive, and the common mass bound extends them uniquely to a positive bounded functional on $C(X,\mathbb R)$. Compact-Hausdorff Riesz gives the canonical finite positive Radon measure $\mu(\boldsymbol u)$. Density also gives weak convergence. The same argument with any bounded decreasing approximations to the finite-energy targets, **without** a common bound, proves independence and weak convergence by (7.2).

For $v\in\mathcal E^1$ choose an actual decreasing $C$ representation $g_\alpha\downarrow v$. All terms lie in $\mathcal E^1$ and have size at most $A(v)$. Apply the directed Radon lemma of Section 5 against the fixed $\mu(\boldsymbol u)$. For fixed continuous $g_\alpha$, weak convergence of the truncation measures and (7.2) identify its integral with $F_\infty(g_\alpha,\boldsymbol u)$. Commuting nonnegative scalar suprema and (7.1), or the same compact-majorant argument, gives
$$\int(-v)\,d\mu(\boldsymbol u)=F_\infty(v,\boldsymbol u)\le A(v)\prod_iA_i.\tag{8.1}$$
Hence every finite-energy test is integrable against every finite-energy mixed measure. For arbitrary $v\in D$, use the integer sequence $v^k$ and ordinary sequential monotone convergence; (8.1) extends to an equality in $[0,\infty]$. In particular every finite-energy input pole has zero mixed measure, since its nonnegative integral is finite. No $\infty-\infty$ operation is made.

For decreasing finite-energy nets $u_{i,\lambda}\downarrow u_i\in\mathcal E^1$, their diagonal sizes are bounded by those of the specified limits. Repeat the continuous-majorant compact cover and use the now proved unbounded multilinearity and Hölder in the negative-shift expansion. This proves $F_\infty(\boldsymbol u_\lambda)\uparrow F_\infty(\boldsymbol u)$ and weak mixed-measure convergence on the dense gauge-difference tests, then all continuous tests. The net need not be sequential or commonly bounded in sup norm.

The exact uniform-energy criterion is: if $u_\lambda\in\mathcal E^1$ decreases to a **specified** $u\in D$, then
$$u\in\mathcal E^1\quad\Longleftrightarrow\quad\sup_\lambda F_\infty(u_\lambda^{[n]})<\infty.$$
The forward direction is order. For the reverse direction take any continuous majorant $h\ge u$, select $\lambda$ with $u_\lambda-\varepsilon\le h$ by the open compact cover, and use the proved finite-energy negative-shift expansion with the uniform diagonal bound. Then (7.1) gives finite diagonal size for $u$. The net continuity just proved applies afterwards. Limit membership in $D$ is an explicit hypothesis; this criterion does not assert infimum closure of the geometric class.

## 9. Variation, reference, primary gauge, normalization, and smooth convention

Fix a finite-energy reference $w$. Define the relative energy by the absolutely meaningful expression
$$E_w(u)=\frac1n\sum_{j=0}^{p}\int(u-w)\,d\mu(u^{[j]},w^{[p-j]}).$$
Each of the two negative tests is separately integrable by (8.1), so the difference is defined almost everywhere and integrable; common poles are null for these measures. Cone multilinearity gives the telescoping identity
$$E_w(u)=E(u)-E(w),\qquad E_z(u)=E_w(u)+E_z(w).$$
On a finite-energy segment $u_t=(1-t)u+tv$, differentiation of the finite polynomial gives
$$\frac d{dt}E(u_t)=\int(v-u)\,d\mu(u_t^{[p]}).$$
This formula, endpoint versions included, follows by polynomial expansion of $F_\infty$, with integrability supplied before subtraction. Concavity is Section 7. Zero is the energy anchor; $r=-1$ is a primary reference with **nonzero curvature** and mass $e_R(\mathfrak a)$, not a locally flat additive constant.

For another proper primary gauge $\mathfrak b$, put $d(v)=v(\mathfrak b)$ on $X_{\mathfrak a}$ and $T(v)=v/d(v)$. Both $d$ and $1/d$ are bounded positive continuous. Homogeneous inputs obey $u_{\mathfrak b}(T(v))=u_{\mathfrak a}(v)/d(v)$. The bounded B341 identity is
$$\mu_{\mathfrak b}(\boldsymbol u_{\mathfrak b})=T_*[d\,\mu_{\mathfrak a}(\boldsymbol u_{\mathfrak a})].\tag{9.1}$$
Pair a transformed test with this measure: its $1/d$ cancels this **one** factor $d$, so the bounded $n$-form is gauge invariant. For unbounded inputs the transformed truncation pulls back to $\max(u_{\mathfrak a},-kd)/d$. The numerator $w_k=\max(u_{\mathfrak a},-kd)$ is bounded $D$ and decreases to $u_{\mathfrak a}$. It is squeezed between constant cuts with levels $k\inf d$ and $k\sup d$, which are cofinal. Consequently its diagonal supremum equals the constant-truncation diagonal supremum, also when infinite. This proves gauge invariance of $F_\infty,E,\mathcal E^1$. For finite-energy tuples the first bounded approximation theorem and the continuous weight $d$ pass (9.1) to the limit. The gauge cocycle is immediate from multiplying the ray denominators; there is neither $d^n$ nor an inverse-power factor.

Let $S$ be the finite normalization and $q$ its local normal centres, with $f_q=[\kappa(q):\kappa(\mathfrak m)]$, and restriction $\rho_q$. B341's bounded identity passes through finite sums and truncations to
$$F_{\infty,R}(\boldsymbol u)=\sum_{\dim S_q=n}f_q F_{\infty,S_q}(\rho_q^*\boldsymbol u),\qquad
\mu_R(\boldsymbol u)=\sum_{\dim S_q=n}f_q\rho_{q,*}\mu_{S_q}(\rho_q^*\boldsymbol u).\tag{9.2}$$
All terms are nonnegative before forming the energy, so infinite suprema commute with the finite sum. These are actual residue degrees, including inseparable ones; normalization has generic degree one on each reduced component. Finite energy downstairs is equivalent to finite energy on every top-dimensional normal centre. The $D$-class condition still requires constancy on the **full** restriction fibres: singleton fibres at finite conductor value, exact conductor-quotient fibres at infinite value. Lower-dimensional centres remain constrained by this class descent and are not discarded. Arbitrary fibre-constant upstairs data must first descend in $D$ by G331; (9.2) then supplies their energy criterion. This does not define a general finite-map energy pushforward or solve all P12.6.

For a reduced excellent curve, the entire boundary is the finite set $v_q=\operatorname{ord}_q/a_q$ where $a_q=\operatorname{ord}_q(\mathfrak a)>0$. The geometric zero-potential reference measure from B341 is
$$\mu=\sum_q f_q a_q\delta_{v_q},\qquad E(u)=\sum_qf_qa_qu(v_q).$$
Thus $\mathcal E^1$ consists exactly of finite nonpositive branch vectors. All residue degrees, units, zeros and mixed-zero vectors are retained. A branch bottom is infinite energy and has positive reference mass. A smooth DVR with maximal-ideal gauge has reference mass one. Dimension zero has the empty measure and energy zero, without negative arity. For nonreduced rings these formulas use the reduction: $k[[t]]$ and $k[[t]][\epsilon]/(\epsilon^2)$ have identical reduced boundary and gauge but lengths $N$ and $2N$ for their parameter quotients. Unreduced intersection multiplicity needs additional generic-length data.

### Direct comparison with exact BFJ Definition 4.3

Here, and only here, the germ is a smooth affine **closed** point over an algebraically closed field of characteristic zero, $n\ge2$. G331 identifies $C,D$ with the full BFJ formal psh class on all semivaluations, with global bottom adjoined. The complete BFJ Setting, 1.14, 2.3--2.8 and Section 4 give its Cartier evaluation, closed-simplex/all-retraction extension, and canonical nef intersection
$$\langle Z_1,\ldots,Z_n\rangle=\inf\{\langle W_1,\ldots,W_n\rangle:W_i\text{ nef Cartier},\ W_i\ge Z_i\}.\tag{BFJ4.3}$$
The value may be $-\infty$. BFJ itself does **not** name an $\mathcal E^1$ space here. Define the canonical finite-self-intersection convention directly as those formal psh $g$ for which $\langle Z_g^{[n]}\rangle> -\infty$, with energy $\langle Z_g^{[n]}\rangle/n$.

We prove equality with our class, rather than attaching a smooth name. The coefficient order $W\ge Z_g$ is equivalent to $H_W\ge g$ on all semivaluations. Divisorial order gives order on each closed simplex by the actual BFJ continuity and dense divisorial points; all-retraction infima then preserve it on every support. Conversely divisorial values are part of the full boundary. BFJ 1.14/2.2 makes a nef Cartier evaluation finite continuous formal psh, hence in $C$ by G331. For an arbitrary BFJ nef Cartier tuple, B341's exact bounded BFJ operator comparison together with the full BFJ 4.6 test pairing gives $F(H_{W_1},\ldots,H_{W_n})=-\langle W_1,\ldots,W_n\rangle$. All these evaluations are bounded, so this use of B341 remains inside its grant. It does not assert that every BFJ model is dominated by a primary model. On primary ideal tuples the coefficient/generic-length convention agrees by repeated SH 17.4.6 and the corrected zero annihilator in the regular ring, as in B341's qualification. Thus Cartier majorants give a subset of the all-$C$ majorants in (7.1), with exactly the same bounded form values.

For the reverse equality, take any nonzero $C$ majorant $h\ge u$. On this normal branch G331's zero dichotomy makes $h$ uniformly negative, say $h\le-c<0$. For small $\eta>0$, approximate $(1-\eta)h$ uniformly by a rational primary profile with error $<\eta c/2$. The profile is at least $h+\eta c/2\ge u$, is a nef Cartier majorant, and tends uniformly to $h$ as $\eta\downarrow0$. For a tuple do this in each slot; bounded form continuity proves equality of the suprema. A zero majorant gives zero form and needs no approximation, and an input $u=0$ has only the zero nonpositive majorant in that slot. Global bottom is excluded by infinite diagonal size. Therefore
$$F_\infty(\boldsymbol u)=-\langle Z_{u_1},\ldots,Z_{u_n}\rangle,$$
and our $\mathcal E^1,E$ equal **exactly** the BFJ finite-self-intersection convention just stated. This proves the requested smooth specialization without inventing a named BFJ energy space.

For finite-energy tuples Hölder gives finite reference mass, so BFJ 4.6's unique measure exists and its ideal moments identify it with ours. BFJ 4.4 gives decreasing-family continuity: coefficientwise decreasing nets converge in the weak coefficient topology, and upper semicontinuity together with monotonicity gives the limit. BFJ 4.8 alone is sequential and is not used as a net theorem. The DVR and empty cases above are direct; no singular or positive-characteristic resolution assertion is inferred.

## 10. Bounded test algebra and full Borel strict-max locality

The real span of $D^{\rm bd}$ is a product algebra. To prove this from the actual class, fix $u\in[-M,0]\cap D$ and set $q_M(t)=t^2+2Mt$. On $[-M,0]$ it is convex, increasing and nonpositive. Its tangent at $s\in[-M,0]$ is
$$2(s+M)t-s^2,$$
with nonnegative slope and nonpositive constant. Finite maxima of these tangents evaluated at a bounded $g\in C$ belong to $C$ and converge uniformly to $q_M(g)$, so $q_M(g)\in C$. If $g_\alpha\downarrow u$ is its actual $C$ representation, all terms are in $[-M,0]$ and monotonicity gives $q_M(g_\alpha)\downarrow q_M(u)$. Thus $q_M(u)\in D^{\rm bd}$ by an actual representation. Hence
$$u^2=q_M(u)-2Mu\in\operatorname{span}D^{\rm bd},\qquad
uv=((u+v)^2-u^2-v^2)/2\in\operatorname{span}D^{\rm bd}.$$
Constants belong to this span; distributivity gives a real product algebra. No increasing closure or arbitrary continuous functional calculus of $D$ is assumed.

This construction also justifies **moving product tests**. For example, with actual bounded continuous representations $u_\alpha\downarrow u$, $v_\beta\downarrow v$, the identity expressing products as sums of $q_M$ applied to their sums yields finite linear combinations of bounded $D$ entries with actual decreasing $C$ representations and specified limits. Section 5's full symmetric $n$-form continuity therefore passes their pairings to the limit when the measure inputs also move. This is stronger than weak convergence tested against a fixed continuous function; weak convergence alone would not justify these moving tests.

For bounded $u,v$ let $w=\max(u,v)$ and $\Delta=w-v\ge0$, and fix the other bounded slots $\boldsymbol t$. We claim
$$\Delta\,[\mu(u,\boldsymbol t)-\mu(w,\boldsymbol t)]=0.\tag{10.1}$$
For continuous compared inputs this follows from Section 4 on $\{u>v\}$; elsewhere $\Delta=0$. Approximate compared inputs by their actual bounded continuous nets, and the other slots similarly. For any fixed ideal-difference continuous test $h$, the moving $\Delta_\alpha h$ is in the product algebra just proved, with the explicit decreasing representations for its constituent terms. Full form continuity in **all** slots passes the weighted identity to the limits. Thus (10.1) holds tested against every such $h$. Uniform density and the finite mass/bounded weight bounds extend it to every continuous $h$. Multiplication of a finite Radon measure by a bounded Borel function is again Radon: approximate that function in measure by finite simple functions and use the regularity of the original finite measure. Riesz uniqueness now proves (10.1) as a signed Radon measure identity.

On $\{\Delta\ge1/m\}$ divide the zero signed weighted measure by its bounded measurable reciprocal. Taking the countable union over $m$ gives
$$\mu(u,\boldsymbol t)|_{\{u>v\}}=\mu(\max(u,v),\boldsymbol t)|_{\{u>v\}}.\tag{10.2}$$
The strict set is Borel because the inputs are Borel; it need not be open for two upper-semicontinuous functions. This is full Borel strict-max locality, independently proved. It is not an attempted use of ordinary open locality on a nonopen set. For $p=0$ both measures are the same reference measure and this identity is automatic.

## 11. Finite-energy nonpolar cutoffs and canonical total variation

Let $u_1,\ldots,u_p\in\mathcal E^1$ and
$$U_k=\bigcap_i\{u_i>-k\},\qquad \mu_k=\mu(u_1^k,\ldots,u_p^k).$$
We prove the setwise cutoff identity
$$\mathbf1_{U_k}\mu_k=\mathbf1_{U_k}\mu(\boldsymbol u).\tag{11.1}$$
Fix one slot $u$, put $w=\max(u,-k)$ and $\Delta=w+k$. This nonnegative bounded span test is positive exactly on $\{u>-k\}$. For every integer $\ell\ge k$, bounded strict-max locality gives
$$\Delta[\mu(u^\ell,\boldsymbol t^\ell)-\mu(w,\boldsymbol t^\ell)]=0.$$
Test it with fixed $h$ in the ideal-difference lattice. The fixed $\Delta h$ is a finite linear combination of bounded $D$ tests by Section 10, hence finite-energy tests. Section 8's full form continuity and extended pairing pass every measure slot to its finite-energy limit. Density then gives the weighted signed measure identity with $u$ and the finite-energy other slots. Divide on the slices where $\Delta\ge1/m$ as before. This replaces $u$ by $u^k$ on $\{u>-k\}$. Repeat the finitely many slots and intersect the strict sets to get (11.1). This proof uses a **fixed bounded $D$ test** during the all-slot limit, not a discontinuous moving indicator in a weak limit.

The union of $U_k$ is the complement of the input poles. Each pole has zero target mixed measure by (8.1). Therefore the measures $\mathbf1_{U_k}\mu_k$ are increasing setwise restrictions of the target and converge setwise to it. This is the nonpolar construction and proves its agreement with the canonical finite-energy measure.

There is also **total variation for these canonical truncations**. In the diagonal case put $A=A(u)$. The two measures agree on $\{u>-k\}$. On its complement,
$$\mu(u^{k[p]})\{u\le-k\}\le F((u^k)^{[n]})/k\le A^n/k,$$
because $-u^k=k$ there. Likewise $\mu(u^{[p]})\{u\le-k\}\le F_\infty(u^{[n]})/k$. Consequently
$$\|\mu(u^{k[p]})-\mu(u^{[p]})\|_{\rm TV}\le2A^n/k.\tag{11.2}$$
For mixed inputs put $P=\prod_{j=1}^p A_j$. On $X\setminus U_k$ use the union bound and (8.1), for both the target and truncated tuple, with test $u_i$. Hölder bounds each such test integral by $A_iP$. Thus
$$\|\mu_k-\mu(\boldsymbol u)\|_{\rm TV}\le\frac2k\sum_{i=1}^p A_iP.\tag{11.3}$$
These estimates remain valid when a size is zero, by the same Hölder bound; if $p=0$ the operator is constant and its total variation difference is zero. No total variation statement for arbitrary decreasing nets follows from this argument. Weak convergence for those nets was Section 8, and is distinct.

## 12. Capacity, comparison, convergence in capacity, and quasicontinuity

For a Borel $B\subset X$ define the mixed-degree reference capacity
$$\operatorname{Cap}(B)=\sup\{\mu(\phi^{[p]})(B):\phi\in D,\ -1\le\phi\le0\}.$$
Every measure in this supremum has mass at most $m=e_R(\mathfrak a)$, so the capacity is finite. It is monotone and countably subadditive, since each measure is. For increasing Borel sets it is continuous from below: the suprema over the set index and $\phi$ commute. We do **not** deduce compact continuity from above or the full Choquet axioms from these facts. For $n=1$ this is simply the fixed finite branch measure.

For diagonal finite energy, (11.1) and a tail bound give
$$\mu(u^{[p]})(B)\le k^p\operatorname{Cap}(B)+A(u)^n/k.$$
Here $u^k/k$ is an admissible capacity input. The proof of Section 11 works unchanged with any fixed positive real cut level $k$, taking integer $\ell\ge k$ for its approximations. Optimizing at $k=A(u)/\operatorname{Cap}(B)^{1/n}$ yields
$$\mu(u^{[p]})(B)\le2A(u)^p\operatorname{Cap}(B)^{1/n}\quad(A(u)>0,\ \operatorname{Cap}(B)>0).\tag{12.1}$$
Zero capacity follows by sending $k\to\infty$; zero size gives a zero measure if $p>0$. For $p=0$ the capacity is the reference measure and the corresponding assertion is its tautological absolute continuity, including a zero-size test. For mixed tuples, positivity and multilinearity give an **actual measure** expansion
$$p!\,\mu(u_1,\ldots,u_p)\le\mu((u_1+\cdots+u_p)^{[p]}).$$
All expansion terms are positive measures. Apply (12.1) and Minkowski to the sum. Thus every finite-energy mixed measure is uniformly absolutely continuous with respect to this capacity. This measure inequality comes from positive expansion, not from ordering scalar gauge moments.

### The precise polar class

Put $r=-1$ and $L_z=\int(-z)\,d\mu(r^{[p]})$ for $z\in D$. If $L_z<\infty$, then, by the extended pairing and **scalar form order** $\phi\ge r$,
$$\int(-z)\,d\mu(\phi^{[p]})\le L_z\qquad(-1\le\phi\le0).$$
For an arbitrary $z$ take its truncations first, then use sequential monotone convergence. Therefore
$$\operatorname{Cap}\{z<-t\}\le L_z/t,\qquad \operatorname{Cap}\{z=-\infty\}=0.\tag{12.2}$$
Every $\mathcal E^1$ input has $L_z\le A(z)\delta^p$ by Hölder. A broader branch-admissible reduction is proved in Section 13; no unrestricted global nonbottom-pole claim is made here.

### Comparison, with equality-locus and reference curvature

For bounded $u,v$, set $w_\varepsilon=\max(u,v-\varepsilon)$, with $v-\varepsilon=v+\varepsilon r$. On the Borel set $\{u<v-\varepsilon\}$, (10.2) identifies $\mu(w_\varepsilon^{[p]})$ with $\mu((v-\varepsilon)^{[p]})$; on $\{u>v-\varepsilon\}$ it identifies it with $\mu(u^{[p]})$. Scalar mass order, tested by $-1$, says $\mu(w_\varepsilon^{[p]})(X)\le\mu(u^{[p]})(X)$. Decompose into these two strict sets and the equality locus. Cancel the identical contribution on the second strict set and discard the nonnegative left equality-locus contribution, obtaining
$$\mu((v-\varepsilon)^{[p]})\{u<v-\varepsilon\}\le\mu(u^{[p]})\{u\le v-\varepsilon\}.$$
The positive reference-curvature expansion gives $\mu(v^{[p]})\le\mu((v+\varepsilon r)^{[p]})$ as measures, because every added mixed term is positive. The right set is contained in $\{u<v\}$. The left strict sets increase to $\{u<v\}$ as $\varepsilon\downarrow0$. Hence
$$\mu(v^{[p]})\{u<v\}\le\mu(u^{[p]})\{u<v\}.\tag{12.3}$$
With fixed other slots the same proof gives the one-slot mixed comparison. The equality-locus term has been retained until it can legitimately be discarded; it is not silently assumed zero.

For finite-energy inputs apply the bounded comparison to $u^k,v^k$. The changing strict set is exactly
$$\{u^k<v^k\}=\{u<v\}\cap\{v>-k\},$$
which increases to the full strict set; input poles are null. Canonical total variation convergence (11.2/11.3), and then setwise continuity of the limiting finite measures, justify the passage despite the moving Borel sets. This proves finite-energy comparison. Ordinary weak convergence would not suffice.

### Decreasing-net capacity convergence

Let $u_\lambda\downarrow u\in\mathcal E^1$ with specified limit. Define the nonnegative integrable gap to be zero on their common poles; its ambiguity is on a capacity-zero set by (12.2). By Section 8
$$I_\lambda=\int(u_\lambda-u)\,d\mu(u^{[p]})
=F_\infty(u,u^{[p]})-F_\infty(u_\lambda,u^{[p]})\downarrow0.$$
For any capacity input $\phi$ and $\varepsilon>0$ put $v_\lambda=u_\lambda+\varepsilon\phi-\varepsilon/2$. This is finite energy by the cone result; its positive measure expansion gives $\mu(v_\lambda^{[p]})\ge\varepsilon^p\mu(\phi^{[p]})$. Outside the null poles,
$$\{u_\lambda-u>2\varepsilon\}\subset\{u<v_\lambda\}\subset\{u_\lambda-u>\varepsilon/2\}.$$
Use comparison and Markov's inequality against $\mu(u^{[p]})$, then take the supremum in $\phi$:
$$\operatorname{Cap}\{u_\lambda-u>2\varepsilon\}\le2I_\lambda/\varepsilon^{p+1}=2I_\lambda/\varepsilon^n\longrightarrow0.\tag{12.4}$$
For $p=0$ the expansion is the identity of the fixed reference measure and the same argument works. No subtraction of infinities occurs on the ignored pole set.

### Actual open exceptional sets and quasicontinuity

For bounded $u\in D$, take an actual $C$ representation $g_\alpha\downarrow u$. It is also a finite-energy net to $u$, so (12.4) applies. The sets $O_j=\{g_{\alpha_j}-u>2^{-j}\}$ are **open**: $g_{\alpha_j}$ is continuous and $u$ is upper semicontinuous. Choose increasing indices $\alpha_j$ with $\operatorname{Cap}(O_j)<\eta2^{-j-1}$; directedness and capacity convergence allow this, without requiring a countable cofinal representation. Outside the open union $O$, $g_{\alpha_j}$ converges uniformly to $u$. Thus $u|_{X\setminus O}$ is continuous and $\operatorname{Cap}(O)<\eta$. For unbounded finite energy, choose $k$ with the open set $\{u<-k\}$ of small capacity by (12.2), and apply bounded quasicontinuity to $u^k$. Outside the union of the two open exceptional sets, $u=u^k$ is finite and continuous. This proves quasicontinuity using genuine open sets and countable subadditivity; no Choquet regularity is assumed.

## 13. Branch-admissible Izumi reduction and necessary polar qualifications

We now discharge the remaining reduction rather than infer a broad polar theorem from a name. On an excellent normal local domain $A$, the **qualified G331 n6 result** says that for each centred divisorial valuation $\nu$, normalized by a fixed primary ideal, there is a finite $C_\nu>0$ with
$$g(\nu)\ge C_\nu g(v_0)\quad(g\in C_A,\ v_0\in X_A).\tag{13.1}$$
This came from the nonunit Izumi bound, normal excellent analytic irreducibility, and primary order comparison; units were handled separately in that grant. Its exact source restrictions remain attached. Passing an actual decreasing $C_A$ representation to its pointwise infimum proves (13.1) for $z\in D_A$. If $z$ is not identically bottom, choose $v_0$ where $z(v_0)$ is finite. It follows that $z(\nu)$ is finite at **every** centred divisorial valuation. This is a direct use of the granted inequality; a merely nonzero value, or a source label, would not imply it.

The reference measure $\mu((-1)^{[p]})$ on $A$ is supported on the finitely many prime divisorial atoms of a primary model by Section 3. Each weight is finite and nonnegative, and their sum is $e_A(\mathfrak a)>0$. Thus $L_z$ is finite if $z$ is not identically bottom on this branch; if it is bottom, the positive total reference mass makes $L_z=\infty$. On a general reduced germ, apply the exact residue-weighted normalization identity (9.2) to this reference measure and its nonnegative test integral. There are finitely many centres. We obtain the equivalence
$$L_z<\infty\quad\Longleftrightarrow\quad
\rho_q^*z\not\equiv-\infty\ \text{for every top-dimensional normal centre }q.\tag{13.2}$$
Lower-dimensional centres contribute zero to $L_z$ in this degree convention but retain their full conductor compatibility. Their individual image points are **not** automatically capacity zero: an identified point can also have top-dimensional preimages. Capacity is a downstairs measure supremum, and normalization adds all top-dimensional contributions in the fibre.

Equation (13.2) proves the polar assertion for every branch-admissible $D$ function, whether or not its self-intersection is finite. It is stronger than the finite-energy consequence and supplies the requested actual Izumi reduction at the available hypotheses. It also specifies the maximal claim justified by this reference moment argument.

The exclusion of whole bottom branches is necessary. For the reduced node curve with two normalized DVR centres and maximal-ideal gauge, $z=(-\infty,0)$ belongs to $D$ by G331 and is globally nonbottom. Its pole is the first branch point, and the reference measure gives it positive mass; in the split rational node its capacity is one. Thus the implication “globally nonbottom $D$ pole is negligible” is false on the prescribed boundary. No polar assertion here makes that mistake. On a nonpure ring a lower-dimensional null branch may carry bottom values in $\mathcal E^1$; the assertion is only the explicitly defined top-degree capacity statement, not a deletion of that boundary or its conductor identifications.

## 14. Independent review decision and reproducibility boundary

The original P12.5 asks for an energy, finite-energy class and its Monge--Ampère calculus on the singular/nonnormal boundary, with reference, primary-gauge and approximation rules. Sections 2--4 supply the independently geometric product bridge needed to attach that meaning to the energy; Sections 5--9 supply the energy construction, mixed measures, variation, reference cocycle, exact gauge and conductor rules, full nets and the direct BFJ finite-self-intersection specialization. Sections 10--13 independently reconstruct the new ROOT346 Borel, nonpolar, capacity and comparison arguments, and repair its deferred broader polar reduction by (13.1)--(13.2). Those extensions were not present in immutable native250; they are separately proved here.

This is a complete **relative mathematical solution claim** for original P12.5 under the explicit reduction, degree-$n$ convention, primary-model system and permitted ordinary published-background rule. It does not close the separate P12.3 envelope or entire P12.6 operator targets. It makes no literal CLD/classical radial-extension comparison, arbitrary-proper-model cofinality, nilpotent-length reconstruction, singular characteristic-free resolution, arbitrary-net total variation, full Choquet compact-above theorem, or equation-uniqueness assertion. The polar convention and its exact branch-admissible range are part of the theorem, with the demonstrated unrestricted alternative excluded. The mandatory G331/B341 qualifications remain attached in full. The notes and decision remain unverified drafts rather than formal certificates or publication decisions.

Every new application uses the complete immediate bound source unit at its actual hypotheses. The source ledger distinguishes those readings, the one fresh PDF pixel inspection, granted historical units, and recursive published background. The immutable actual nine native250 FINAL notes and expanded notes are retained separately; equality of duplicated proof bodies is checked rather than treating expanded text as the actual FINAL. Both original-task objects are retained, with the native two trailing linefeeds disclosed and the assignment separate. Hashes establish body identity, never mathematical correctness.

Fresh standard-library readers and finite diagnostics are the only programs executed for this deliverable. No supplied author/ROOT/reviewer program was executed or imported. The old command snapshots and failed finite-window multiplicity attempt remain unchanged diagnostic data. The new finite diagnostic proves only its enumerated arithmetic claims; the universal intersection and energy arguments are the mathematics above. All private source bodies and pixels remain local. No extra agents, native jobs, network/auth/runtime changes, publication/catalogue/editor mutations, compilation, or heavy compute were used. No supervised heavy-compute facility was supplied or needed. The protected P16 editor was not accessed or changed.
