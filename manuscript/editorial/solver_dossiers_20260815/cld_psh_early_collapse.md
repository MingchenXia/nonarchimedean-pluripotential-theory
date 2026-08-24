# Early collapse of the CLD psh hierarchy

**Problem id:** `open_problems/cld_psh_early_collapse`
**Solver pass:** in-session direct solve, 15 August 2026.
**Promotion status:** CANDIDATE-ONLY. No Rethlas receipt exists for any statement
below. Nothing here may enter theorem typography.
**Primary source:** Chambert--Loir--Ducros, arXiv:1204.6277, 2025 revision, local
full text (`refs/cld25.txt`). All section numbers below were read verbatim from
that file; French is quoted exactly where the wording is at issue.

---

## 1. Status audit

### 1.1 The exact source objects

CLD Définition 8.1.1 defines \(\mathrm{Psh}_X\), for \(X\) an *espace \(G\)-tropical
affiné*, as the smallest subsheaf of the sheaf of \(\mathbf R\cup\{-\infty\}\)-valued
functions such that for every open \(U\):

> i) Il contient les fonctions lisses \(u\) sur \(U\) telles que \(d'd''u\geqslant 0\);
> ii) Il est stable par limite décroissante de suites.

Lemme 8.1.4 introduces the transfinite filtration: \(\mathrm{Psh}_{X,0}\) is the
sheaf of smooth \(u\) with \(d'd''u\ge 0\); \(\mathrm{Psh}_{X,\alpha+1}\) consists of
functions *locally* decreasing limits of functions in \(\mathrm{Psh}_{X,\alpha}\);
at a limit ordinal one takes the local union.

Définition 8.1.13 gives the property at issue its own name:

> On dit qu'une fonction psh sur un ouvert de \(X\) est **localement approchable**
> si c'est une section du faisceau \(\mathrm{Psh}_{X,1}\).

**Therefore the packet's question is exactly CLD's own question: is every psh
function locally approachable?** The dossier uses *approachable* throughout; it is
source terminology, not a book coinage, and is safe for the manuscript.

### 1.2 Diagnosis of the Lemma 8.1.4 / Remark 8.1.6 discrepancy

This was the packet's first mandate and it resolves cleanly.

The proof of Lemme 8.1.4 states: *"Elle est nécessairement stationnaire, par un
argument de cardinal."* The argument is correct. For each open \(U\) the sets
\(\mathrm{Psh}_{X,\alpha}(U)\) form an increasing chain of subsets of the fixed set of
functions \(U\to\mathbf R\cup\{-\infty\}\); an increasing ordinal-indexed chain of
subsets of a fixed set is eventually constant, and the supremum of the stabilization
ordinals over the (set-sized) collection of opens is again an ordinal. Stabilization
at *some* ordinal is thus a theorem, and CLD use it: Proposition 8.1.5, Proposition
8.1.11 and Proposition 8.2.1 all transport a statement "for every \(\alpha\)" to a
statement about \(\mathrm{Psh}_X\) precisely *compte tenu du lemme 8.1.4*.

Remarque 8.1.6 nevertheless says:

> Dans notre cadre, nous ne savons même pas si la hiérarchie ordinale des espaces de
> fonctions psh est stationnaire. Cependant, tous les exemples de fonctions psh que
> nous connaissons appartiennent au premier cran de cette hiérarchie.

**Finding (source audit).** Read literally, the first sentence contradicts Lemme
8.1.4, which the same authors prove two pages earlier and repeatedly invoke. The
contradiction is not mathematical but editorial: the second sentence identifies the
intended content, namely that no example is known outside *le premier cran*. The
mathematically live question is therefore stationarity **at a specified early
ordinal**, above all at \(\alpha=1\), and not stationarity as such.

*Book disposition:* the manuscript must not repeat "stationarity is unknown". It
should state that eventual stabilization is CLD Lemme 8.1.4, that early collapse is
open, and that CLD Remarque 8.1.6's literal sentence is superseded by their own
lemma. This is a citation-accuracy repair, not a new theorem.

### 1.3 Fetch limitation

Direct arXiv retrieval is blocked by the egress proxy in this environment. All
source claims above are read from the local full text of the 2025 revision and are
quoted verbatim; no claim in this dossier depends on an unfetched source.

---

## 2. Formalization

Throughout, \(X\) is an affine \(G\)-tropical space in CLD's sense, and all statements
are local, since every sheaf in play is defined by a local condition.

**(Q1)** Is \(\mathrm{Psh}_{X,1}=\mathrm{Psh}_X\), i.e. is every psh function locally
approachable, for \(X\) in a natural geometric class?

**(Q2)** Failing that, is there a uniform ordinal bound \(\alpha_0\) — finite,
countable, or depending only on \(\dim X\) — with
\(\mathrm{Psh}_{X,\alpha_0}=\mathrm{Psh}_X\)?

**(Q3)** Is there a psh function of genuine closure rank \(\ge 2\)?

Conventions fixed: values in \(\mathbf R\cup\{-\infty\}\) are allowed; decreasing
limits are of *sequences*, not nets, in Définition 8.1.1(ii); local integrability is
not part of Définition 8.1.1 but is the subject of the separate sheaf
\(L^1\mathrm{Psh}_X\) of Proposition 8.1.12, which satisfies
\(L^1\mathrm{Psh}_{X,\alpha}=L^1_{\mathrm{loc}}\cap \mathrm{Psh}_{X,\alpha}\) for every
\(\alpha\). Consequently **collapse for \(\mathrm{Psh}\) and collapse for
\(L^1\mathrm{Psh}\) are equivalent**, level by level, and the integrability
bookkeeping the packet warns about does not create a separate problem.

---

## 3. Attack map

Four mechanisms were carried far enough to reach a verdict.

- **M1 (abstract reduction).** Collapse at stage one is *equivalent* to one closure
  property of a single sheaf. Cheap, unconditional, and it localizes the whole
  question. Carried out in §4.1.
- **M2 (direct regularization).** Produce, for each psh \(u\), an explicit decreasing
  sequence of smooth psh approximants. This is how the complex case is proved — by
  convolution, not by any abstract diagonal. Works verbatim on \(\mathbf R^n\) (§4.2)
  and, with a genuinely different construction, at a vertex of a one-dimensional
  balanced space (§4.5).
- **M3 (stability calculus).** Show \(\mathrm{Psh}_{X,1}\) is closed under the
  operations the theory actually uses, so that the class of known stage-one functions
  is large. Unconditional via CLD Proposition 8.2.1 (§4.3).
- **M4 (continuous reduction).** Use CLD Proposition 8.1.11 to transfer the question
  to uniform limits, where diagonalization is legal. This nearly closes the
  continuous case and isolates the residual obstruction as purely point-set (§4.4).

---

## 4. Proof attempts

### 4.1 Reduction Lemma (CANDIDATE-PROPOSITION; unconditional)

**Statement.** For any ordinal \(\alpha\ge 0\), the following are equivalent:
(i) \(\mathrm{Psh}_{X,\alpha}=\mathrm{Psh}_X\);
(ii) \(\mathrm{Psh}_{X,\alpha}\) is stable under decreasing limits of sequences, i.e.
for every open \(U\) and every decreasing sequence \((u_n)\) in
\(\mathrm{Psh}_{X,\alpha}(U)\) converging pointwise to \(u\), one has
\(u\in\mathrm{Psh}_{X,\alpha}(U)\).

*Proof.* (i)\(\Rightarrow\)(ii) is Définition 8.1.1(ii). For (ii)\(\Rightarrow\)(i):
\(\mathrm{Psh}_{X,\alpha}\) is a subsheaf containing the smooth psh functions
(it contains \(\mathrm{Psh}_{X,0}\) by construction), and by hypothesis it satisfies
Définition 8.1.1(ii); by minimality of \(\mathrm{Psh}_X\) we get
\(\mathrm{Psh}_X\subseteq\mathrm{Psh}_{X,\alpha}\). The reverse inclusion is the
content of Lemme 8.1.4. \(\square\)

**Consequence.** The entire question is: *is a decreasing limit of approachable
functions approachable?* Every genuinely analytic difficulty is concentrated here,
and the transfinite apparatus is a red herring — if stage one is not stable under
decreasing limits, no finite stage is either, by the same argument applied at each
\(\alpha\).

### 4.2 Collapse on \(\mathbf R^n\) (CANDIDATE-PROPOSITION; complete proof)

Let \(\Omega\subseteq\mathbf R^n\) be open and convex, regarded as an affine tropical
space of dimension \(n\). Smooth functions are \(C^\infty\) in the ordinary sense and,
for \(u\in C^\infty(\Omega)\),
\(d'd''u=\sum_{i,j}\partial_i\partial_j u\,d'x_i\wedge d''x_j\) is a positive
\((1,1)\)-superform exactly when the Hessian is positive semidefinite. Hence

\[
  \mathrm{Psh}_{\Omega,0}=\{\text{smooth convex functions on }\Omega\}.
\]

**Statement.** \(\mathrm{Psh}_{\Omega,1}=\mathrm{Psh}_{\Omega}\), and both equal the set
of convex functions \(\Omega\to\mathbf R\cup\{-\infty\}\) (on a connected \(\Omega\),
either real-valued convex, or \(\equiv-\infty\)).

*Proof.* Pointwise decreasing limits of convex functions are convex, so
\(\mathrm{Psh}_\Omega\) consists of convex functions. Conversely let \(u\) be convex
and real-valued (the case \(u\equiv-\infty\) is the decreasing limit of the smooth psh
constants \(-k\), hence already at stage one). Fix a radial mollifier \(\rho\ge0\),
\(\operatorname{supp}\rho\subseteq \bar B(0,1)\), \(\int\rho=1\), and set
\(u_\varepsilon:=u*\rho_\varepsilon\) on
\(\Omega_\varepsilon=\{x:\operatorname{dist}(x,\partial\Omega)>\varepsilon\}\).

1. *Smooth and convex.* Standard: convolution of a convex function with a
   nonnegative kernel is convex, and smooth.
2. *\(u_\varepsilon\ge u\).* Since \(\rho\) is radial, \(\int z\rho(z)\,dz=0\), so by
   Jensen \(u_\varepsilon(x)=\int u(x-\varepsilon z)\rho(z)\,dz\ge
   u\bigl(x-\varepsilon\int z\rho(z)dz\bigr)=u(x)\).
3. *Monotone in \(\varepsilon\).* Let \(0<\varepsilon'<\varepsilon\) and
   \(\lambda=\varepsilon'/\varepsilon\in(0,1)\). Then
   \(x-\varepsilon'z=(1-\lambda)x+\lambda(x-\varepsilon z)\), so convexity gives
   \(u(x-\varepsilon'z)\le(1-\lambda)u(x)+\lambda u(x-\varepsilon z)\). Integrating
   against \(\rho(z)dz\) and then using step 2,
   \[
     u_{\varepsilon'}(x)\le(1-\lambda)u(x)+\lambda u_\varepsilon(x)
       \le(1-\lambda)u_\varepsilon(x)+\lambda u_\varepsilon(x)=u_\varepsilon(x).
   \]
4. *Convergence.* \(u\) is convex and real-valued, hence continuous on the open set
   \(\Omega\), so \(u_\varepsilon\to u\) pointwise (indeed locally uniformly).

Taking \(\varepsilon=1/k\) gives a decreasing *sequence* of smooth psh functions
converging to \(u\) on each \(\Omega_{1/k_0}\); since approachability is local, this
proves \(u\in\mathrm{Psh}_{\Omega,1}\). \(\square\)

*Audit of this proof.* Step 3 is the only nonstandard point and is where a
non-radial kernel would fail. Step 2 is where radiality is used a second time. No
step uses first countability of anything beyond \(\mathbf R^n\); the approximation is
by a sequence, not a net, so the packet's net/sequence warning is met. The
\(-\infty\) case is handled separately because Jensen is vacuous there.

### 4.3 Closure properties of the approachable sheaf (CANDIDATE-PROPOSITION)

CLD Proposition 8.2.1 states: if \(u_1,\dots,u_n\) are psh, \(\Omega\subseteq\mathbf R^n\)
convex open, \(g:\Omega\to\mathbf R\) smooth, convex and nondecreasing in each variable,
and \((u_1(x),\dots,u_n(x))\in\Omega\) for all \(x\), then \(g(u_1,\dots,u_n)\) is psh;
**and if every \(u_i\in\mathrm{Psh}_{X,\alpha}\) then \(g(u_1,\dots,u_n)\in\mathrm{Psh}_{X,\alpha}\).**

From this:

**(a) Cone and sums.** If \(u,v\in\mathrm{Psh}_{X,1}\) and \(c>0\) then
\(u+v,\ cu\in\mathrm{Psh}_{X,1}\): directly, if \(u=\lim\downarrow u_k\) and
\(v=\lim\downarrow v_k\) with \(u_k,v_k\) smooth psh, then \(u+v=\lim\downarrow(u_k+v_k)\)
and sums of smooth psh are smooth psh.

**(b) Finite maxima.** *This does not follow from 8.2.1 alone, because \(\max\) is not
smooth.* Let \(u,v\in\mathrm{Psh}_{X,1}\) be real-valued, \(u=\lim\downarrow u_k\),
\(v=\lim\downarrow v_k\) with \(u_k,v_k\) smooth psh. Let \(M_\eta\) be a regularized
maximum: \(M_\eta\) smooth, convex, nondecreasing in each variable,
\(\max(a,b)\le M_\eta(a,b)\le\max(a,b)+C\eta\), and \(M_\eta\) nondecreasing in
\(\eta\). Choose \(\eta_k\downarrow0\) and set \(w_k:=M_{\eta_k}(u_k,v_k)\). Then:
\(w_k\) is smooth psh by the \(\alpha=0\) case of Proposition 8.2.1;
\[
  w_{k+1}=M_{\eta_{k+1}}(u_{k+1},v_{k+1})\le M_{\eta_k}(u_{k+1},v_{k+1})
        \le M_{\eta_k}(u_k,v_k)=w_k,
\]
using monotonicity in \(\eta\) and then monotonicity in each argument; and
\(\max(u_k,v_k)\le w_k\le\max(u_k,v_k)+C\eta_k\), so \(w_k\downarrow\max(u,v)\).
Hence \(\max(u,v)\in\mathrm{Psh}_{X,1}\). \(\square\)

*Caveat recorded:* Proposition 8.2.1 is stated for real-valued arguments (the target
\(\Omega\) is an open subset of \(\mathbf R^n\)), so (b) is proved for real-valued
\(u,v\); the \(-\infty\)-valued case requires an exhaustion argument not carried out
here and is left open.

**Reading.** The approachable class is closed under every operation the CLD
Bedford--Taylor chapter actually performs on psh functions except one: passing to a
decreasing limit. This is why, as Remarque 8.1.6 says, no example escapes stage one.

### 4.4 The continuous case (CANDIDATE-PROPOSITION + CONDITIONAL-REDUCTION)

CLD Proposition 8.1.11 proves \(\mathrm{CPsh}_{X,\alpha}=C_X\cap\mathrm{Psh}_{X,\alpha}\)
for **every** ordinal \(\alpha\), where \(\mathrm{CPsh}_{X,\alpha}\) is built with local
*uniform* limits (Lemme 8.1.8). The bridge is Lemme 8.1.10: if \(f_n\to f\)
uniformly then \((f_n+2\lVert f-f_n\rVert_\infty)\) has a decreasing subsequence
converging uniformly to \(f\). (This is precisely the summable-shift device already
carried by the book's verified receipt R3-CLD-PL-01.)

So on continuous functions, the question becomes: *does the uniform hierarchy
collapse at stage one?* Uniform limits, unlike decreasing limits, diagonalize:

**Statement (fixed-open collapse; unconditional).** For an open \(V\subseteq X\) let
\[
  \mathcal A(V):=\{u\in C(V): u \text{ is a uniform limit on } V
     \text{ of smooth psh functions on } V\}.
\]
Then \(\mathcal A(V)\) is closed under uniform convergence on \(V\).

*Proof.* Let \(u_k\in\mathcal A(V)\) with \(u_k\to u\) uniformly on \(V\). Pick smooth
psh \(v_k\) on \(V\) with \(\sup_V|v_k-u_k|<1/k\). Then
\(\sup_V|v_k-u|\le 1/k+\sup_V|u_k-u|\to0\), so \(u\in\mathcal A(V)\). \(\square\)

No monotonicity is needed, which is exactly why this succeeds where §4.1 stalls.
Combining with Lemme 8.1.10 and Proposition 8.1.11: **every continuous psh function
that is uniformly approximable by smooth psh functions on one fixed neighbourhood of
each point is approachable there.**

**The residual gap, stated exactly.** CLD's \(\mathrm{CPsh}_{X,1}\) is defined by
*local* uniform approximation, and the neighbourhood is permitted to depend on the
function. Unwinding, what the above yields at a point \(x\) is:

> for every \(\varepsilon>0\) there exist a neighbourhood \(W_\varepsilon\ni x\) and a
> smooth psh \(v\) on \(W_\varepsilon\) with \(\sup_{W_\varepsilon}|v-u|<\varepsilon\),

whereas membership in \(\mathrm{CPsh}_{X,1}\) at \(x\) demands a **single**
neighbourhood serving all \(\varepsilon\). Call the implication between these the
*uniform-neighbourhood property* (UNP).

**CONDITIONAL-REDUCTION (continuous case).** For continuous psh functions, stage-one
collapse is equivalent to UNP. In particular the obstruction in the continuous case
is purely point-set: no analytic input is missing, only the passage from
shrinking neighbourhoods to a fixed one.

**First unsupported implication in the naive argument** (recorded verbatim, as the
protocol requires): *"since each \(u_k\) is locally a uniform limit of smooth psh
functions near \(x\), we may choose the approximants on a common neighbourhood of
\(x\)."* This is false as stated; the neighbourhoods \(W_k\) supplied by membership of
\(u_k\) in \(\mathrm{CPsh}_{X,1}\) may shrink to \(\{x\}\).

**Route to closing UNP, not carried out.** The classical device for exactly this
gap is Richberg gluing: patch approximants defined on small overlapping opens using
a regularized maximum and a strictly positive smooth reserve. §4.3(b) supplies the
regularized maximum on tropical spaces unconditionally. What is needed in addition
is a strictly positive smooth \((1,1)\)-form near \(x\) to absorb the patching error.
On \(\mathbf R^n\) the function \(|x|^2\) supplies one. Note that this is *not*
obstructed the way it is in the Berkovich-analytic setting of CLD Remarque 17.8.10,
where smooth functions are locally constant near rigid points and no strict
positivity reserve exists; on a tropical space the reserve exists on cells. This is
the single most promising unexplored route and is flagged for a future packet.

### 4.5 One-dimensional balanced spaces

Let \(X\) be a one-dimensional affine tropical space: locally, at a vertex, a star of
rays with primitive directions \(v_1,\dots,v_m\) in \(\mathbf R^N\) and weights \(w_i>0\)
satisfying the balancing condition \(\sum_i w_iv_i=0\). Take \(w_i=1\) for readability.

**(a) Smooth psh functions carry no vertex atom (complete computation).** A smooth
function on \(X\) near the vertex is the restriction of a smooth \(F\) on the ambient
\(\mathbf R^N\). Its outgoing slope along ray \(i\) at the vertex is
\(\frac{d}{dt}\big|_{t=0^+}F(tv_i)=\langle dF(0),v_i\rangle\), so the atom of
\(d'd''u\) at the vertex equals
\[
  \sum_i \langle dF(0),v_i\rangle=\Bigl\langle dF(0),\ \sum_i v_i\Bigr\rangle=0 ,
\]
**by balancing**. So \(d'd''u\) of a smooth psh function is carried by the edge
interiors, with no mass at the vertex.

**(b) Yet stage-one functions do have atoms (explicit example).** Take the standard
tropical line \(X\subset\mathbf R^2\): rays \(v_1=(1,0)\), \(v_2=(0,1)\),
\(v_3=(-1,-1)\), weights \(1\); balanced since \(v_1+v_2+v_3=0\). Let
\(P=\operatorname{conv}\{v_1,v_2,v_3\}\), a triangle containing \(0\) in its interior,
and let \(g\) be its Minkowski gauge, \(g(x)=\inf\{\lambda>0: x\in\lambda P\}\). Then
\(g\) is convex, positively homogeneous, \(g(v_i)=1\), so \(h:=g|_X\) has slope \(1\) on
each ray and vertex atom
\[
  \sum_i (\text{slope}_i)=3>0 .
\]
By §4.2, \(g=\lim\downarrow g_\varepsilon\) with \(g_\varepsilon\) smooth convex on
\(\mathbf R^2\); each \(g_\varepsilon|_X\) is smooth on \(X\), edgewise convex, and has
zero vertex atom by (a); and \(g_\varepsilon|_X\downarrow h\). Hence
\(h\in\mathrm{Psh}_{X,1}\) **with a strictly positive atom**.

The mechanism is worth recording, because it is the whole phenomenology of stage
one: the approximants have no atom, but their edge curvature concentrates at the
vertex, and \(\int_{B_r}d'd''(g_\varepsilon|_X)\to 3\) as \(\varepsilon\to0\) for fixed
\(r>0\). **Atoms are therefore not an obstruction to approachability**, which disposes
of the most obvious candidate mechanism for a rank-\(\ge2\) example.

**(c) The PL case at a vertex (CANDIDATE-PROPOSITION, proof sketch with the delicate
step identified).** Let \(u\) be PL psh near the vertex, with outgoing slopes \(a_i\)
and \(u(0)=0\), so that psh-ness means \(m:=\sum_i a_i\ge0\). Claim:
\(u\in\mathrm{Psh}_{X,1}\).

*Construction.* Put \(b_i:=a_i-m/m_{\#}\) where \(m_\#\) is the number of rays; then
\(\sum_i b_i=0\) and \(b_i\le a_i\). Because the map
\(\xi\mapsto(\langle\xi,v_i\rangle)_i\) has image exactly \(\{b:\sum_ib_i=0\}\) — the
balancing relation is the only relation among the \(v_i\) in the tropical-line case —
there is a covector \(\xi\) with \(\langle\xi,v_i\rangle=b_i\), i.e. \((b_i)\) is a
*legal smooth vertex jet*. For \(\varepsilon>0\) define \(u_\varepsilon\) to equal \(u\)
outside the \(\varepsilon\)-ball and, on \([0,\varepsilon]\) along ray \(i\), a smooth
convex profile \(\varphi_i\) with \(\varphi_i'(0)=b_i\), \(\varphi_i'\) increasing to
\(a_i\), \(\varphi_i(\varepsilon)=a_i\varepsilon\), and the common vertex value
\(\varphi_i(0)=c_\varepsilon\) independent of \(i\). Feasibility of one common
\(c_\varepsilon\): \(\int_0^\varepsilon\varphi_i'\in(b_i\varepsilon,a_i\varepsilon)\)
forces \(c_\varepsilon\in(0,(a_i-b_i)\varepsilon)=(0,(m/m_\#)\varepsilon)\) for every
\(i\) simultaneously, so \(c_\varepsilon:=\tfrac{m}{2m_\#}\varepsilon\) works whenever
\(m>0\); if \(m=0\) then \(u\) is already the restriction of the linear \(\langle\xi,\cdot\rangle\)
and there is nothing to prove. Then \(u_\varepsilon\) is smooth at the vertex (it
agrees with \(\langle\xi,\cdot\rangle+c_\varepsilon\) to first order there), edgewise
convex, hence smooth psh; and \(u_\varepsilon\ge u\) because
\(u_\varepsilon'\le a_i=u'\) on \([0,\varepsilon]\) with equality of values at
\(t=\varepsilon\), so \(u_\varepsilon-u\) is nonincreasing and vanishes at
\(\varepsilon\).

*The delicate step, not completed.* Monotonicity of \(\varepsilon\mapsto u_\varepsilon\)
requires the profiles for successive \(\varepsilon\) to be chosen nested. This is
plainly arrangeable (choose \(\varphi\) from a single rescaled template) but has not
been written out here; until it is, (c) is a candidate with an identified gap, not a
completed proof. It does *not* affect (a) or (b).

**(d) Beyond PL in dimension one.** A general psh function on the star is edgewise
convex with a nonnegative vertex atom in the sense of (a)--(b). The natural argument
is: mollify edgewise, then correct the vertex by (c). The correction is by an
explicit profile and does not interact with the edgewise mollification away from the
vertex. This is the most likely route to an unconditional one-dimensional theorem
and is recommended as the next packet.

### 4.6 The general obstruction, and the first unsupported implication

By §4.1 everything reduces to: given \(u_n\in\mathrm{Psh}_{X,1}\) decreasing to \(u\),
with \(u_n=\lim_k\downarrow v_{n,k}\) locally and \(v_{n,k}\) smooth psh, produce a
decreasing sequence of smooth psh functions converging to \(u\).

**First genuinely unsupported implication**, stated verbatim as the protocol
requires: *"choose \(w_j\) to be a smooth psh regularization of
\(\min(v_{1,k_1},\dots,v_{j,k_j})\)."* The step is unsupported because **the minimum
of psh functions is not psh** — the regularized *maximum* of §4.3(b) has no
counterpart for minima, and \(u=\inf_n u_n\) is an infimum. This is not a technical
inconvenience: it is the structural reason the abstract diagonal cannot work, and it
is equally the reason the complex case is proved by convolution rather than by
diagonal (CLD Remarque 8.1.3 attributes the complex statement to the smoothing
theorem, not to a formal argument).

Hence the honest shape of the problem: **stage-one collapse requires a direct local
regularization operator on tropical spaces**, i.e. an analogue of mollification that
(i) preserves \(d'd''\ge0\), (ii) dominates, and (iii) is monotone in the parameter.
§4.2 supplies it on \(\mathbf R^n\), where translation makes convolution available;
§4.5 supplies a hand-built substitute at a one-dimensional vertex. On a general
polyhedral tropical space there is no group action moving one cell into another, and
no such operator is known.

---

## 5. Self-adversarial audit

- *Unbounded and \(-\infty\)-valued functions.* §4.2 covers \(u\equiv-\infty\) by
  constants. §4.3(b) is proved only for real-valued arguments and this is recorded
  as a gap, not glossed.
- *Sequences vs nets.* Définition 8.1.1(ii) uses sequences. §4.2 produces a sequence
  by taking \(\varepsilon=1/k\); no net is smuggled in. Dini (CLD Remarque 8.1.3)
  upgrades pointwise to locally uniform convergence for continuous limits on the
  locally compact tropical space, and this is used only in §4.4 where CLD themselves
  use it.
- *Local integrability.* Handled once and for all by Proposition 8.1.12: the
  \(L^1\) hierarchy matches the plain one at every level, so no separate bookkeeping.
- *Non-compact cells and behaviour at infinity.* §4.2 is stated on \(\Omega_\varepsilon\)
  and the conclusion is local, so no properness is used. §4.5 is a germ statement at
  a vertex.
- *Cross-cell boundary points.* This is exactly where the argument fails, and §4.6
  says so rather than hiding it. The tripod computation in §4.5(a) shows the vertex
  is not merely a technical nuisance: smooth functions are *constrained* there by
  balancing in a way they are not on \(\mathbf R^n\).
- *Did any step assume the space is a manifold?* §4.2 does, explicitly, and its
  conclusion is stated only for \(\mathbf R^n\).
- *Circularity check.* §4.1 uses Lemme 8.1.4 only for the inclusion
  \(\mathrm{Psh}_{X,\alpha}\subseteq\mathrm{Psh}_X\), which is immediate from the
  transfinite construction and does not use the cardinality argument.

---

## 6. Dispositions

| Sub-question | Disposition |
|---|---|
| Source status of eventual stationarity | **LITERATURE-RESOLVED** — CLD Lemme 8.1.4; Remarque 8.1.6's literal sentence is superseded by the authors' own lemma |
| Collapse \(\Leftrightarrow\) closure under decreasing limits | **CANDIDATE-PROPOSITION** (§4.1, complete) |
| Collapse on \(\mathbf R^n\) and convex opens | **CANDIDATE-PROPOSITION** (§4.2, complete) |
| \(\mathrm{Psh}_{X,1}\) closed under sums, positive scaling, finite maxima | **CANDIDATE-PROPOSITION** (§4.3, complete for real-valued; \(-\infty\) case open) |
| Collapse for continuous psh | **CONDITIONAL-REDUCTION** to the uniform-neighbourhood property UNP (§4.4); the fixed-open statement is unconditional |
| Smooth psh have zero vertex atom in dimension one | **CANDIDATE-PROPOSITION** (§4.5(a), complete computation) |
| Atoms obstruct approachability | **COUNTEREXAMPLE-CANDIDATE to the obstruction** — the gauge function on the tropical line is at stage one with atom \(3\) (§4.5(b), fully explicit) |
| Collapse at a one-dimensional vertex, PL case | **CANDIDATE-PROPOSITION with an identified gap** (§4.5(c): nesting of profiles unwritten) |
| Collapse for general affine tropical \(X\) (Q1) | **OPEN-AFTER-ATTEMPT**; obstruction: no psh-preserving regularized *minimum*, hence no abstract diagonal; a direct tropical mollification operator is the missing input (§4.6) |
| Uniform ordinal bound (Q2) | **OPEN-AFTER-ATTEMPT** |
| A psh function of rank \(\ge2\) (Q3) | **OPEN-AFTER-ATTEMPT**; the natural atom-based mechanism is refuted by §4.5(b) |

**Retracted claim (recorded, not silently deleted).** An earlier draft of this
dossier asserted that, by the Reduction Lemma applied at each \(\alpha\),
\(\mathrm{Psh}_{X,\alpha}=\mathrm{Psh}_X\) for some finite \(\alpha\ge1\) would imply
it for \(\alpha=1\), so that "no intermediate finite regime exists". **This is
unproved and the assertion is withdrawn.** The Reduction Lemma applied at
\(\alpha=2\) gives only that \(\mathrm{Psh}_{X,2}\) is closed under decreasing limits;
it says nothing about whether \(\mathrm{Psh}_{X,1}\) is already all of
\(\mathrm{Psh}_X\), and \(\mathrm{Psh}_{X,1}\subsetneq\mathrm{Psh}_{X,2}=\mathrm{Psh}_X\)
is not excluded by any argument in this dossier. The error was caught in the
independent chapter-expansion audit of the same session, which declined to reproduce
the claim. Q2 is therefore open with no structural narrowing, and any downstream
text repeating the narrowing must be corrected.

---

## 7. Proposed ledger lines

- **Problem id:** `open_problems/cld_psh_early_collapse`. Solver pass run in session
  on 15 August 2026 by direct solve; **no Rethlas receipt**; every outcome below is
  candidate-only and none may enter theorem typography.
- **Source correction (highest-value outcome):** eventual stationarity of the CLD
  hierarchy is proved in Lemme 8.1.4 by a cardinality argument; the literal sentence
  of Remarque 8.1.6 saying stationarity is unknown contradicts it and must not be
  repeated by the book. CLD Définition 8.1.13 already names the live property —
  *localement approchable*, i.e. membership in \(\mathrm{Psh}_{X,1}\) — so the book's
  formulation should be "is every psh function locally approachable?".
- **Reduction:** collapse at stage \(\alpha\) is equivalent to stability of
  \(\mathrm{Psh}_{X,\alpha}\) under decreasing sequential limits. **Correction:** an
  earlier draft went on to claim that finite collapse at any stage is therefore
  equivalent to collapse at stage one; that claim is **withdrawn as unproved** — the
  Reduction Lemma at \(\alpha=2\) does not exclude
  \(\mathrm{Psh}_{X,1}\subsetneq\mathrm{Psh}_{X,2}=\mathrm{Psh}_X\). The error was
  caught by an independent audit in the same session.
- **Positive cases:** unconditional stage-one collapse on \(\mathbf R^n\) and convex
  opens, by radial mollification with monotonicity in the parameter; and closure of
  \(\mathrm{Psh}_{X,1}\) under sums, positive scalars, and finite maxima (the last via
  CLD Proposition 8.2.1 plus a regularized-maximum diagonal), for real-valued
  arguments.
- **Continuous case:** by CLD Proposition 8.1.11 and Lemme 8.1.10 the continuous
  question reduces to uniform limits, which diagonalize on a fixed open; the residual
  obstruction is purely point-set — the uniform-neighbourhood property — and carries
  no missing analytic input. Richberg gluing via the §4.3(b) regularized maximum is
  the recommended next attack, and unlike the Berkovich setting of Remarque 17.8.10
  it is not blocked by absence of a strict positivity reserve.
- **Refuted mechanism:** vertex atoms do not obstruct approachability. On the
  standard tropical line the Minkowski gauge of \(\operatorname{conv}\{v_1,v_2,v_3\}\)
  lies in \(\mathrm{Psh}_{X,1}\) and has vertex atom \(3\), while every smooth psh
  function has vertex atom \(0\) by balancing; the approximants' edge curvature
  concentrates at the vertex. Any future search for a rank-\(\ge2\) example must
  avoid this mechanism.
- **Open remainder and obstruction:** the general case is open. The first
  unsupported implication in every diagonal attempt is the use of a psh-preserving
  smooth regularized *minimum*, which does not exist; the missing input is a direct
  local regularization operator on polyhedral tropical spaces preserving
  \(d'd''\ge0\), dominating, and monotone in its parameter.
- **Book disposition:** retain the general question as open in the research chapter;
  repair the Remarque 8.1.6 citation as above; the positive cases and the atom
  example may be used as expository illustrations only if and when they receive
  their own receipts, and must not be presented as theorems of this book meanwhile.
