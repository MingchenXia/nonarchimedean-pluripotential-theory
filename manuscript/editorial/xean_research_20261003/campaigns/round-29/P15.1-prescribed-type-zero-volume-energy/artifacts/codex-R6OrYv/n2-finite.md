# A genuine relative finite-energy extension, with specified continuity

This note uses the bounded theorem proved in local note **n1**. It retains the same actual reference type and auxiliary Kähler class. It proves a finite-energy extension of that theorem, with decreasing monotone continuity. It does not claim an unbounded perturbative limit or arbitrary monotone/path regularity.

## The precise additional standard foundations

Vu, arXiv:2005.13241v3, §3, with \(P=T_\psi\), \(m=d\), \(T=\omega^{n-d}\), and linear weight \(\chi(t)=t\), defines the following spaces. A current \(S\) in \([P]\), more singular than \(P\), has relative full mass if
\[
\{\langle S^d\dot\wedge T\rangle\}=
\{\langle P^d\dot\wedge T\rangle\}.
\]
For negative potentials \(u\leq\psi\), its diagonal joint linear-weight energy is
\[
d\sum_{a=0}^d\binom da\int(\psi-u)
\langle T_u^aT_\psi^{d-a}\rangle\omega^{n-d}.
\tag{16a}
\]
This is the exact specialization of Vu's Eq. (3.1): there are \(\binom da\) subsets of size \(a\), and the weight is \(\chi(d(u-\psi))=d(u-\psi)\). Theorem 3.4 states that both the full-mass space \(\mathcal E_{d,P}(T)\) and its joint weighted subclass \(\mathcal E_{\chi,d,P}(T)\) are convex. Corollary 3.2 states that the weighted class is unchanged when \(P\) is replaced by a cohomologous current of the same bounded singularity type. Finiteness does not depend on additive potential constants. Here \(T\) is smooth closed positive, the relative products are ordinary nonpluripolar products with smooth factors, and the product has top degree. On connected \(X\), equality of its cohomology classes is equality of total masses. Thus all source hypotheses are satisfied, with no minimal-singularity or model-envelope assumption. The source proofs of convexity and reference-type invariance use cited arguments; they are used as scoped standard foundations, not as reconstructed new lemmas. The convention conversion in n1 preserves full mass and weighted finiteness, multiplying (16a) by a positive constant.

We also use the following standard bounded convergence foundations solely to prove the continuity assertion below. A decreasing sequence of quasi-psh functions in a fixed smooth background, with a quasi-psh limit not identically minus infinity, converges in Kähler Monge–Ampère capacity. This is the decreasing-convergence statement cited as Guedj–Zeriahi 2005, Proposition 3.7, in DDNL's proof of Theorem 2.4, p. 2057. DDNL Proposition 2.2, pp. 2054–2055, states: on an open set in \(\mathbb C^n\), uniformly bounded local psh functions converging in capacity in every slot, multiplied by uniformly bounded quasicontinuous functions also converging in capacity, give weakly convergent weighted Bedford–Taylor top products. Quasi-psh functions and their bounded truncations are quasicontinuous. All applications below have a fixed background and uniformly bounded **local truncations**. We do not apply the big-class-only DDNL Theorem 2.3 directly to the pseudoeffective background. The complete primary body of Proposition 2.2 is included in the argument annex; the scalar capacity fact is a standard foundation cited through the supplied DDNL proof, not a new source-proven theorem here.

## Domain and theorem

Fix \(\omega\in\lambda\), \(r=n-d\), and \(M=M_d(\psi,\lambda)>0\). For \(d\geq1\), let \(\mathcal F^1_{\psi,\lambda}\) consist of \(\theta\)-psh \(u\) such that \(u\leq\psi+C\),
\[
\int\langle T_u^d\rangle\omega^r=M,
\qquad
\sum_{a=0}^d\binom da\int|u-\psi|
\langle T_u^aT_\psi^{d-a}\rangle\omega^r<\infty.
\tag{17a}
\]
For \(d=0\), use the same more-singular condition and \(\int|u-\psi|\omega^n<\infty\); degree-zero full mass is automatic. This integral is finite for quasi-psh \(u,\psi\) since both are locally integrable against smooth volume. Every bounded-type potential belongs to the domain.

Define, for this domain,
\[
\mathcal E_{\psi,\lambda}(u)
=\frac1{d+1}\sum_{a=0}^d\int(u-\psi)
\langle T_u^aT_\psi^{d-a}\rangle\omega^r.
\tag{18a}
\]
Then all these integrals are finite. The energy equals the decreasing limit of bounded-type truncation energies \(u_L=\max(u,\psi-L)\), is independent of the truncation levels tending to infinity, and is continuous under **every decreasing sequence in \(\mathcal F^1_{\psi,\lambda}\) with limit in that domain**. In particular, every decreasing sequence of bounded-type potentials converging to a point of this domain gives the same extension value. It is increasing and concave. Its constant shifts are \(cM\). For any two members \(u,v\) of the domain, all integrals
\[
\mathcal E_{v,\lambda}(u)
=\frac1{d+1}\sum_{a=0}^d\int(u-v)
\langle T_u^aT_v^{d-a}\rangle\omega^r
\tag{19a}
\]
are finite and obey the exact cocycle
\[
\mathcal E_{\psi,\lambda}(u)-\mathcal E_{\psi,\lambda}(v)
=\mathcal E_{v,\lambda}(u).
\tag{20a}
\]
Changing the anchor within the original bounded type leaves the finite-energy domain unchanged and changes the energy by this cocycle. Both domain and energy are independent of the Kähler representative of the fixed class \(\lambda\). No identity of unbounded first or second variations is asserted.

## Mixed full mass and mixed weight integrability

First subtract constants from finitely many potentials so that all are \(\leq\psi\), and shift \(\psi\) to be negative if needed. This only translates energy by constants times finite masses, and will be reversed at the end. For \(d\geq1\), the definition (17a) is exactly the source joint linear-weight class (16a), so its convexity applies.

Given \(u_1,\ldots,u_N\) in this domain, including any copies of \(\psi\), put \(w=N^{-1}\sum_i u_i\). Convexity gives \(\int\langle T_w^d\rangle\omega^r=M\). By expansion it is the mean of \(N^d\) ordered mixed masses. Each is at most \(M\), by DDNL Theorem 2.4 replacing every more-singular \(u_i\) by \(\psi\), with \(r\) smooth Kähler slots. They are nonnegative and their average is \(M\). Hence **every** such mixed mass equals \(M\). This proves all mixed full masses used below without inferring them from the diagonal by an unsupported polarization.

The \(a=d\) term of the finite joint energy of \(w\) shows that
\(\int(\psi-w)\langle T_w^d\rangle\omega^r<\infty\). Every summand in its positive expansion is therefore finite. Since
\[
0\leq\psi-u_i\leq N(\psi-w),
\]
each \(\psi-u_i\) is integrable against every degree-\(d\) mixed product formed from the finite family. In particular \(|u-v|\leq(\psi-u)+(\psi-v)\) is integrable against every product in (19a). All representation poles are pluripolar and have zero mass. For \(d=0\), these assertions follow directly from smooth-volume integrability and the common mass \(M_0\).

For completeness, every degree \(k>d\) mixed product of such more-singular potentials also vanishes: DDNL mass monotonicity bounds its trace integral by the corresponding zero \(M_k(\psi,\lambda)\), and positivity implies vanishing as in n1. This assertion does not give weighted control of any degree \(k<d\).

## The exact truncation identity

Assume \(u\leq\psi\), write \(z=\psi-u\geq0\), and let
\[
\mu_a=\langle T_u^aT_\psi^{d-a}\rangle\omega^r,
\qquad
\mu_{a,L}=\langle T_{u_L}^aT_\psi^{d-a}\rangle\omega^r.
\]
All these measures have mass \(M\), by the preceding argument and bounded-type equality respectively. On the plurifine comparison set \(G_L=\{u>\psi-L\}\), locality gives \(\mu_{a,L}=\mu_a\). The comparison-set version with unbounded psh data is also exactly Vu v3 Theorem 3.3, applied in local charts to the potentials plus their smooth local backgrounds. On the complement \(B_L\), off the polar sets, \(u_L-\psi=-L\). Equality of total masses gives \(\mu_{a,L}(B_L)=\mu_a(B_L)\). Consequently
\[
\int(\psi-u_L)d\mu_{a,L}
=\int_{G_L}z\,d\mu_a+L\mu_a(B_L)
=\int\min(z,L)d\mu_a.
\tag{21a}
\]
For \(a=0\), the measure is fixed and the identity is immediate. Boundary sets where \(u=\psi-L\) cause no issue: the weight is exactly \(L\) there, and locality is used only on the strict comparison set. Measures give no mass to infinite-value sets. Monotone convergence in the right side proves
\[
\mathcal E_{\psi,\lambda}(u_L)\downarrow\mathcal E_{\psi,\lambda}(u).
\tag{22a}
\]
This proves existence and independence for all real truncation levels tending to infinity. Order of potentials is inherited by their truncations, so bounded monotonicity and (22a) prove monotonicity on the whole domain. The exact mixed masses prove the \(cM\) constant-shift law directly in (18a); normalization by constants in the proof is therefore harmless.

## A bounded decreasing continuity lemma and its proof

Suppose \(v_j\downarrow v\), all have the bounded type of \(\psi\), and \(|v_j-\psi|,|v-\psi|\leq B\) uniformly on their finite loci. For a fixed degree \(q\), each mixed measure formed from \(v_j\) and \(\psi\), with \(n-q\) fixed smooth Kähler factors, has the same mass as its limit, by bounded-type equality. Let \(\eta_L=\min(1,\max(\psi+L,0))\). Then \(0\leq\eta_L\leq1\), it vanishes on \(\{\psi\leq-L\}\), and tends to 1 outside the polar set of \(\psi\).

On a coordinate chart with smooth local potential \(\rho\) for \(\theta\), the functions \(\rho+v_j\), \(\rho+v\), and \(\rho+\psi\) are psh. Where \(\eta_L\ne0\), they have a uniform lower bound depending only on \(L,B\) and the compact chart. Replace them by local bounded psh truncations below a still lower constant; locality preserves all products on that set. Their upper bounds are uniform from compactness and the fixed \(v_1\). Decreasing quasi-psh convergence gives convergence in capacity, and the local bounded truncations and their differences converge in capacity as well. The cutoff and the bounded weights can be expressed using these truncations on their support, so they are uniformly bounded quasicontinuous functions converging in capacity. DDNL Proposition 2.2 with the remaining fixed smooth slots and a smooth partition of unity therefore proves convergence of both
\(\int\eta_Ld\nu_j\) and \(\int\eta_L(v_j-\psi)d\nu_j\) to their limiting counterparts. This is a local bounded application in every slot; no big-class convergence result is needed.

If the common mass is \(m\), then \(\int(1-\eta_L)d\nu_j=m-\int\eta_Ld\nu_j\). The integrals of the omitted weights have absolute value at most \(B\) times this quantity. First let \(j\to\infty\), and then \(L\to\infty\); the limiting tail mass tends to zero because the limit has no polar mass. This proves convergence of each full weighted mixed integral and hence convergence of the bounded-type energy. The same proof allows a fixed same-type anchor in place of \(\psi\). It explicitly controls the unbounded reference's polar-locus tails.

## Decreasing continuity and concavity of the extension

Let \(v_j\downarrow u\) with all \(v_j,u\) in the finite-energy domain. The sequence has a common upper bound \(\psi+C\), since \(v_1\leq\psi+C\). By monotonicity,
\[
\mathcal E(u)\leq\mathcal E(v_j)\leq\mathcal E(\max(v_j,\psi-L)).
\]
For fixed \(L\), the potentials on the right decrease to \(\max(u,\psi-L)\) within a uniform bounded type. The lemma gives
\(\limsup_j\mathcal E(v_j)\leq\mathcal E(u_L)\). Letting \(L\to\infty\) in (22a) proves \(\mathcal E(v_j)\to\mathcal E(u)\). This also proves independence from arbitrary decreasing bounded-type approximants, rather than merely renamed truncations.

For \(u,v\) in the domain and \(t\in[0,1]\), Vu's convexity makes \(w=(1-t)u+tv\) a domain member. The bounded-type combinations \(w_L=(1-t)u_L+tv_L\) decrease to \(w\). Bounded concavity gives
\(\mathcal E(w_L)\geq(1-t)\mathcal E(u_L)+t\mathcal E(v_L)\). Decreasing continuity and (22a) prove concavity of the extension. For \(d=0\) the formula is directly affine.

## Cocycle and reference changes

Take normalized \(u,v\leq\psi\) and their simultaneous truncations at level \(L\). Let
\(\nu_a=\langle T_u^aT_v^{d-a}\rangle\omega^r\),
\(\nu_{a,L}=\langle T_{u_L}^aT_{v_L}^{d-a}\rangle\omega^r\),
and \(G_L=\{u>\psi-L\}\cap\{v>\psi-L\}\). These measures have the same mass \(M\) and agree on \(G_L\). Their complementary masses therefore agree as well. On the complement \(B_L\), \(|u_L-v_L|\leq L\). With \(z_u=\psi-u\), \(z_v=\psi-v\),
\[
L\nu_{a,L}(B_L)=L\nu_a(B_L)
\leq\int_{B_L}(z_u+z_v)d\nu_a\longrightarrow0.
\]
The last limit follows from mixed weight integrability and the fact that \(B_L\) decreases to polar sets. The original tail of \(|u-v|\) also tends to zero. On \(G_L\), the weights agree exactly. Thus every term in \(\mathcal E_{v_L,\lambda}(u_L)\) converges to the corresponding finite term in (19a). Taking limits in the bounded cocycle proves (20a). Additive constants reduce the general case to this normalization.

If \(\psi'\sim\psi\), Vu Corollary 3.2 identifies the finite-energy classes of currents, and bounded mixed mass equality gives the same \(d,M\). Representatives of a current differ only by constants on connected \(X\), so the potential domains agree as well. To check the energy value without using an unproved truncation interchange, use \(u_L\) truncated against \(\psi\), and the measure \(\langle T_u^aT_{\psi'}^{d-a}\rangle\omega^r\). Mixed mass and weight integrability hold by the preceding finite-family argument, since \(\psi'\) itself belongs to the domain. On \(\{u>\psi-L\}\) products agree with those of \(u_L\); the complement has equal mass. Its truncated weight \(|u_L-\psi'|\) is at most \(L+\|\psi-\psi'\|_\infty\), and its integral tends to zero by integrability of \(\psi-u\) against this mixed measure. The original tail also tends to zero. Thus
\(\mathcal E_{\psi',\lambda}(u_L)\to\mathcal E_{\psi',\lambda}(u)\), and the bounded anchor cocycle passes to the limit:
\[
\mathcal E_{\psi',\lambda}(u)=\mathcal E_{\psi,\lambda}(u)-\mathcal E_{\psi,\lambda}(\psi').
\]

Finally let \(\omega'\) be any Kähler representative of the same \(\lambda\). Closedness and cohomology make each scalar full-mass condition in (17a) unchanged. Pointwise comparison of the two fixed Kähler forms makes every absolute-weight mixed integral finite for one exactly when it is finite for the other. Thus the domain is unchanged. The bounded energies of every \(u_L\) are representative independent by n1; (22a) proves representative independence of their finite-energy limit. A simultaneous smooth-background change as in n1 leaves the construction unchanged. This proves all reference-change assertions stated in this note.

## A domain member with an actually unbounded difference

Take \(X=\mathbb P^1\times\mathbb P^1\), normalized Fubini–Study \(\kappa\), \(\theta=p_1^*\kappa\), \(\psi=0\), and \(\omega=p_1^*\kappa+p_2^*\kappa\). Then \(d=1\), \(M=1\). In a disk about \(0\in\mathbb P^1\), choose \(0<a<1/2\) and
\[
v(z)=-b(-\log|z|)^a
\]
near zero, with \(b>0\) small. Continue it by a smooth cutoff away from the disk, and choose \(b\) sufficiently small that \(\kappa+dd^cv\geq0\); its singular radial Hessian is positive, and the cutoff contributes a bounded Hessian only on a fixed annulus. Subtract a constant to make \(v\leq0\). Near zero its positive Laplacian density is a constant times
\(b a(1-a)|z|^{-2}(-\log|z|)^{a-2}\). The boundary flux is proportional to \((-\log|z|)^{a-1}\to0\), so there is no point atom. Therefore its nonpluripolar mass is 1. Moreover
\[
\int(-v)dd^cv\quad\text{has singular part proportional to}
\quad\int^{\infty}t^{2a-2}dt<\infty,
\]
and \(\int(-v)\kappa<\infty\). For \(u=p_1^*v\), both weighted terms of (17a) are finite and the mass is \(M\), but \(u-\psi\) is unbounded. This is a genuine finite-energy extension, with no fibration assumed in the theorem; the product example only demonstrates its domain.
