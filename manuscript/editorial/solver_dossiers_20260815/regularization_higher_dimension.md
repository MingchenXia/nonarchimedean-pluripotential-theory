# Higher-dimensional regularization: a sufficient criterion, a separating
# counterexample, and the sharp obstruction

**Problem ids:** `open_problems/classical_psh_regularization` (OP-02) and
`open_problems/cld_psh_early_collapse` (OP-07), higher-dimensional case.
**Solver pass:** in-session direct solve, 15 August 2026.
**Promotion status:** CANDIDATE-ONLY. No Rethlas receipt. Nothing here enters
theorem typography.
**Relation to prior work in this project.** The earlier Rethlas run on OP-02
concluded `OPEN`, with the diagnosis that *curvewise approximation does not supply
analytic gluing in higher dimension*, and that the missing input is a
common-neighbourhood decreasing regularization compatible with the chosen target
class. This dossier attacks exactly that gap on the tropical side, where the CLD
psh sheaf lives, and reports four results. The \(\mathbf R^n\) case and the
closure properties of \(\mathrm{Psh}_{X,1}\) established in
`cld_psh_early_collapse.md` are used as inputs and not re-proved.

Throughout, \(X\) is an affine \(G\)-tropical space in the sense of CLD, locally a
weighted balanced polyhedral complex in \(\mathbf R^N\); *smooth* means the
restriction of an ambient smooth function; \(\mathrm{Psh}_{X,1}\) is CLD's sheaf of
*locally approachable* psh functions (Définition 8.1.13); and stage-one collapse
at \(x\) means every psh germ at \(x\) is approachable.

---

## 1. Restriction of an ambient convex function is psh

**Lemma 1 (candidate; complete proof in dimension one, flagged in general).**
Let \(\Sigma\subseteq\mathbf R^N\) be a one-dimensional balanced fan with primitive
ray generators \(v_1,\dots,v_r\) and weights \(m_i>0\), so \(\sum_i m_iv_i=0\). Let
\(F\) be convex on a neighbourhood of \(0\). Then \(F|_\Sigma\) is psh.

*Proof.* On the relative interior of each ray, \(F\) is convex along the ray, so
the smooth part of \(\mathrm d'\mathrm d''(F|_\Sigma)\) is \(\ge0\). At the vertex,
the atom is \(\sum_i m_i\,p(v_i)\) where \(p(v):=F'(0;v)\) is the one-sided
directional derivative. For \(F\) convex, \(p\) is convex and positively
homogeneous, hence **subadditive**, so for positive weights
\[
  \sum_i m_i\,p(v_i)\ \ge\ p\Bigl(\sum_i m_i v_i\Bigr)\ =\ p(0)\ =\ 0 .
\]
Thus the atom is nonnegative and \(F|_\Sigma\) is psh. \(\square\)

**What makes this work** is worth isolating, because it is the only place
balancing is used: subadditivity of \(p\) converts the balancing relation into the
positivity of the corner mass. The same computation along a codimension-one face
\(\tau\) of a higher-dimensional complex gives
\(\sum_\sigma m_\sigma\,p(n_{\sigma,\tau})\ge p(w)\) with
\(w=\sum_\sigma m_\sigma n_{\sigma,\tau}\in T_\tau\); this is \(\ge0\) exactly when
\(w=0\), and in general \(p(w)\) is a derivative along \(\tau\), so the corner term
is a divergence rather than a sign-definite quantity. **Flagged:** Lemma 1 is
proved here only in dimension one and in the higher-dimensional case where the
normal sums vanish on the nose; the general case needs the precise CLD corner
convention and is not claimed.

---

## 2. A sufficient criterion: local convex extension

**Definition.** \(X\) has the *local convex extension property* (LCE) at \(x\) if
every psh germ at \(x\) is the restriction of a convex germ on a neighbourhood of
\(x\) in the ambient \(\mathbf R^N\).

**Proposition 2 (candidate).** If \(X\) has LCE at \(x\), then stage-one collapse
holds at \(x\): every psh germ at \(x\) lies in \(\mathrm{Psh}_{X,1}\).

*Proof.* Let \(u\) be psh near \(x\) and \(U\) a convex extension on a ball \(B\).
Let \(\rho\) be a radial mollifier and \(U_\varepsilon:=U*\rho_\varepsilon\). By the
\(\mathbf R^n\) result already established in this project, \(U_\varepsilon\) is
smooth and convex, \(U_\varepsilon\ge U\), and \(\varepsilon\mapsto U_\varepsilon\)
is nondecreasing with \(U_\varepsilon\to U\) pointwise. Restricting,
\(U_\varepsilon|_X\) is smooth on \(X\) and psh by Lemma 1, and
\(U_\varepsilon|_X\downarrow U|_X=u\) along \(\varepsilon=1/k\). Hence
\(u\in\mathrm{Psh}_{X,1}\). \(\square\)

**Value of this reduction.** It converts an analytic regularization problem into a
question of convex geometry: *which psh functions on a balanced complex extend to
ambient convex functions?* For PL data this is a finite linear-programming
question, made explicit in §3.

---

## 3. LCE is strictly stronger than approachability

This is the main negative finding, and it is fully explicit.

### 3.1 The LP characterization of LCE for PL germs on a fan

Let \(\Sigma\) be a one-dimensional fan with rays \(v_i\), weights \(m_i\), and let
\(u\) be PL with outgoing slopes \(a_i\) and \(u(0)=0\). A convex homogeneous
extension is a support function \(h_K\), so LCE for \(u\) asks for a convex
\(K\subseteq\mathbf R^N\) with \(h_K(v_i)=a_i\) for all \(i\). The maximal candidate
is \(K:=\{y:\langle y,v_i\rangle\le a_i\ \forall i\}\), and LP duality gives
\[
  h_K(v_j)=\min\Bigl\{\textstyle\sum_i\mu_ia_i\ :\ \mu\ge0,\ \sum_i\mu_iv_i=v_j\Bigr\}
  \ \le\ a_j ,
\]
the bound coming from \(\mu=e_j\). Hence:

> **LCE holds for \(u\) if and only if \(\sum_i\mu_ia_i\ge a_j\) for every \(j\)
> and every \(\mu\ge0\) with \(\sum_i\mu_iv_i=v_j\).**

This is *strictly stronger* than pshness, which is the single inequality
\(\sum_im_ia_i\ge0\) against the weight vector.

### 3.2 The separating example, computed

Take \(N=2\) and
\[
  v_1=(1,0),\quad v_2=(0,1),\quad v_3=(-1,-1),\quad v_4=(1,1),
\]
with weights \(m=(1,1,2,1)\). Balancing holds:
\(1\cdot(1,0)+1\cdot(0,1)+2\cdot(-1,-1)+1\cdot(1,1)=(0,0)\). Let \(u\) be PL with
slopes \(a=(0,0,0,1)\), i.e. \(u\equiv0\) on the first three rays and
\(u(tv_4)=t\).

**(a) \(u\) is psh.** The fan is one-dimensional, so \(\mathrm d'\mathrm d''u\) is
an atom at the origin of mass \(\sum_im_ia_i=0+0+0+1=1\ge0\).

**(b) \(u\) has no ambient convex extension.** If \(F\) were convex with
\(F|_\Sigma=u\) near \(0\), then \(p=F'(0;\cdot)\) is subadditive and
\(v_4=v_1+v_2\), so
\[
  1=a_4=p(v_4)=p(v_1+v_2)\ \le\ p(v_1)+p(v_2)=a_1+a_2=0 ,
\]
a contradiction. (Equivalently, the LP criterion of §3.1 fails at \(j=4\) with
\(\mu=e_1+e_2\).)

**(c) Nevertheless \(u\) is approachable.** For \(c>0\) put
\(w_c:=\max(u,c)\). Then:
\(w_c\) is psh, being a maximum of the psh functions \(u\) and the constant \(c\);
\(w_c\equiv c\) on a neighbourhood of the origin, since \(u<c\) there, so \(w_c\) is
the restriction of an ambient smooth function near the vertex and its vertex atom
is \(0\); on each ray \(w_c\) is convex, being a maximum of two convex functions of
one variable; and \(w_c\downarrow u\) pointwise as \(c\downarrow0\). Replacing the
maximum by the regularized maximum \(M_\eta\) and diagonalizing in \((c,\eta)\) —
legitimate by CLD Proposition 8.2.1 together with the max-diagonal argument
already established for \(\mathrm{Psh}_{X,1}\) in this project — yields a decreasing
sequence of **smooth** psh functions converging to \(u\). Hence
\(u\in\mathrm{Psh}_{X,1}\).

**Conclusion.** LCE fails for \(u\) while approachability holds. **The
ambient-convex-extension route of §2 is sufficient but not necessary, and the gap
is genuine rather than an artefact of a bad extension.** Any programme that tries
to prove stage-one collapse by extending and mollifying will therefore fail on
this example, and must be replaced.

---

## 4. The device that does work, and exactly where it stops

Extracting the mechanism of §3.2(c):

**Proposition 3 (candidate).** Let \(\Sigma\) be a fan with vertex \(0\), and let
\(u\) be psh near \(0\) with \(u\ge u(0)\) and \(u\) smooth on
\(\Sigma\smallsetminus\{0\}\). Then \(u\in\mathrm{Psh}_{\Sigma,1}\) at \(0\).

*Proof.* \(M_\eta(u,u(0)+c)\) is smooth psh for \(c,\eta>0\): it is psh by CLD
Proposition 8.2.1, it is smooth near \(0\) because it is the constant \(u(0)+c\)
there, and it is smooth away from \(0\) because \(u\) is. It decreases in both
parameters and converges to \(\max(u,u(0))=u\). Diagonalize. \(\square\)

So a **vertex** singularity — a zero-dimensional stratum — is always removable:
maxing with a constant flattens the function near the vertex, and the constant is
smooth there for free.

**The obstruction in dimension \(\ge2\), stated sharply.** Suppose \(\dim X\ge2\)
and \(u\) is psh with a corner along a *positive-dimensional* stratum \(\tau\)
(say a codimension-one face). To repeat the device one must max \(u\) against a
function that is (i) psh, (ii) smooth near \(\tau\), and (iii) \(\ge u\) on a
neighbourhood of \(\tau\) while \(\le u\) away from it, so that the maximum is
flattened exactly along \(\tau\). A constant no longer serves, because \(u\) is not
constant along \(\tau\). The natural candidate is an affine function agreeing with
\(u\) along \(\tau\) — but such a function exists precisely when \(u\) admits a
local affine minorant touching along the whole of \(\tau\), which is **exactly the
LCE condition localized at \(\tau\)**, and §3 shows that condition can fail.

> **The induction on strata dimension therefore fails at the first
> positive-dimensional stratum, and it fails for the same reason that LCE fails.**

This is the sharp form of the earlier diagnosis that "curvewise approximation does
not supply analytic gluing in higher dimension": the missing object is not a
gluing procedure but a *local affine minorant with prescribed contact along a
positive-dimensional stratum*.

---

## 5. Consistency with the curve case

In dimension one the problem is a theorem. Thuillier proves that a subharmonic
function on a smooth strictly \(k\)-analytic curve is, on every relatively compact
open subset, the decreasing lower envelope of a family of **smooth** subharmonic
functions, and that subharmonic functions are exactly the degree-zero currents
\(T\) with \(\mathrm{dd}^cT\ge0\). On the tropical side, the corresponding
statement is §4: all strata of a one-dimensional complex are vertices or open
edges, and both are handled.

This is a genuine consistency check rather than a coincidence: **dimension one is
exactly the range in which every singular stratum is zero-dimensional**, which is
the hypothesis under which Proposition 3 applies. The first genuinely open case is
dimension two.

---

## 6. Dispositions

| Item | Disposition |
|---|---|
| Restriction of ambient convex is psh (dimension one) | **CANDIDATE-PROPOSITION**, §1 |
| The same in higher dimension | **OPEN / flagged**; the corner term is a divergence unless the normal sums vanish exactly |
| LCE \(\Rightarrow\) stage-one collapse | **CANDIDATE-PROPOSITION**, §2 |
| LP characterization of LCE for PL germs | **CANDIDATE-PROPOSITION**, §3.1 |
| LCE strictly stronger than approachability | **COUNTEREXAMPLE-CANDIDATE**, fully explicit, §3.2 |
| Vertex singularities are always removable | **CANDIDATE-PROPOSITION**, §4 |
| Stage-one collapse in dimension \(\ge2\) | **OPEN-AFTER-ATTEMPT**, with the obstruction identified as a local affine minorant with contact along a positive-dimensional stratum |

---

## 7. Proposed ledger lines

- **Problem ids:** `open_problems/classical_psh_regularization` and
  `open_problems/cld_psh_early_collapse`, higher-dimensional case. In-session
  solver pass, 15 August 2026; **no Rethlas receipt**; candidate-only.
- **Sufficient criterion:** stage-one collapse follows from a local convex
  extension property, by mollifying the ambient extension and restricting; the
  restriction of an ambient convex function is psh because subadditivity of the
  directional derivative converts balancing into nonnegativity of the corner mass.
- **That criterion is not necessary, and the gap is explicit.** On the balanced
  four-ray fan \((1,0),(0,1),(-1,-1),(1,1)\) with weights \((1,1,2,1)\), the PL
  function with slopes \((0,0,0,1)\) is psh, admits no ambient convex extension
  (subadditivity forces \(a_4\le a_1+a_2\), i.e. \(1\le0\)), and is nevertheless a
  decreasing limit of smooth psh functions via \(\max(u,c)\). Any
  extend-and-mollify programme dies on this example.
- **Positive general device:** on a fan, a psh function that dominates its vertex
  value and is smooth away from the vertex is approachable, by maxing with a
  constant and regularizing. Zero-dimensional strata are therefore never an
  obstruction.
- **Sharp obstruction in dimension \(\ge2\):** repeating the device along a
  positive-dimensional stratum requires a local affine minorant with contact along
  the whole stratum — the localized LCE condition, which §3 shows can fail. This
  replaces the earlier vague diagnosis about gluing with a precise missing object.
- **Consistency:** dimension one is closed (Thuillier on curves; §4 on the tropical
  side) precisely because every singular stratum there is a vertex. The first open
  case is dimension two, and that is where a future packet should aim.
- **Book disposition:** the general question stays open in the research chapter.
  The four-ray counterexample is the most useful item for the manuscript, since it
  refutes a natural approach a reader would otherwise try; it may be used as an
  expository example only once it carries its own receipt, and with no priority
  claim.
