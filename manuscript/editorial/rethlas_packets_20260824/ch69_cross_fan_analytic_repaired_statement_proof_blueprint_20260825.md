# Repaired statement/proof blueprint: cross-fan analytic realization

Date: 2026-08-25

Status: packet-only replacement for any future promotion decision. The earlier candidate files are retained unchanged as historical records. This blueprint makes no novelty claim and is not a live-chapter edit.

## Exact dispositions

1. **Literal compact harmonic realization of the full cross:** negatively settled by compactness.
2. **Noncompact proper locally harmonic realization, including the weighted positive closed current and the exact pushed-forward defect:** affirmatively settled by the split-Gauss construction below.
3. **Stronger analytic realization with equal curvature currents before pushforward:** not settled by this construction and remains open.

## Proposed exact statement

Let \(K\) be a complete algebraically closed nontrivially valued non-Archimedean field, and let
\[
\Sigma
=\mathbf R_{\geq0}e_1\cup\mathbf R_{\geq0}(-e_1)
 \cup\mathbf R_{\geq0}e_2\cup\mathbf R_{\geq0}(-e_2)
\subset\mathbf R^2.
\]
Equip \(\Sigma\) first with unit weights, and define
\[
u(s,t)=2|s|,\qquad v(s,t)=|s|+|t|,\qquad h=u-v.
\]
Let \(T_\Sigma\) be the positive closed tropical current whose two horizontal rays have weight \(2\) and whose two vertical rays have weight \(1\).

Then the following assertions hold.

### (i) Compactness obstruction

There is no harmonic tropicalization
\[
g:W\longrightarrow\mathbf R^2
\]
in the sense of the live harmonic-tropicalization definition such that \(g(W)=\Sigma\).

Indeed, that definition requires \(W\) to be a compact strict analytic domain. Hence \(g(W)\) is compact, whereas \(\Sigma\) is unbounded.

### (ii) Exact noncompact realization and pushed-forward calculation

Set
\[
A=K[x^{\pm1},y^{\pm1}]/((x-1)(y-1)),\qquad
X=(\operatorname{Spec}A)^{\mathrm{an}},
\]
and write
\[
Y_h=V(y-1)^{\mathrm{an}},\qquad
Y_v=V(x-1)^{\mathrm{an}}.
\]
Then \(X=Y_h\cup Y_v\) is reduced, pure one-dimensional, good, strict, and boundaryless; each component is a closed copy of \(\mathbf G_m^{\mathrm{an}}\), and they meet only at the rigid point \(p=(1,1)\).

The map
\[
\tau:X\longrightarrow\mathbf R^2,\qquad
\tau=(-\log|x|,-\log|y|)
\]
is a proper ordinary moment tropicalization, its coordinates are locally integral harmonic, and
\[
\tau(X)=\Sigma.
\]
The fundamental cycle has tropical weight \(1\) on each of the four primitive rays.

For every \(\rho>1\) in \(|K^\times|\), the compact strict domain
\[
X_\rho
=X\cap
\{\rho^{-1}\leq|x|\leq\rho,\ 
  \rho^{-1}\leq|y|\leq\rho\}
\]
is a harmonic-tropicalization chart in the live sense, with image
\[
\Sigma_\rho
=\Sigma\cap[-\log\rho,\log\rho]^2.
\]
Thus the full map is noncompact and locally harmonic, and is exhausted by compact harmonic tropicalizations of truncated crosses.

Define
\[
Z=2[Y_h]+[Y_v],\qquad T=\delta_Z.
\]
Then \(T\) is a strongly positive order-zero analytic current satisfying
\[
\mathrm d'T=0,\qquad \mathrm d''T=0.
\]
Its calibrated tropical pushforward is exactly
\[
\tau_*T=T_\Sigma.
\]
In particular, its ray weights are
\[
(2,2,1,1)
\]
on \(+e_1,-e_1,+e_2,-e_2\), respectively.

Put
\[
U=u\circ\tau,\qquad V=v\circ\tau,\qquad H=U-V.
\]
The functions \(U,V\) are continuous psh functions. For every sequence \(\varepsilon_j\downarrow0\), they are the locally uniform decreasing limits of the smooth psh functions
\[
U_j=2\sqrt{(-\log|x|)^2+\varepsilon_j},
\]
\[
V_j=\sqrt{(-\log|x|)^2+\varepsilon_j}
    +\sqrt{(-\log|y|)^2+\varepsilon_j}.
\]

Let \(q_h\) and \(q_v\) be the unit Gauss points of \(Y_h\) and \(Y_v\). Then
\[
q_h\ne q_v,\qquad \tau(q_h)=\tau(q_v)=0,
\]
and the exact analytic current identities are
\[
\mathrm d'\mathrm d''[U]=4\delta_{q_h},
\]
\[
\mathrm d'\mathrm d''[V]
=2\delta_{q_h}+2\delta_{q_v},
\]
\[
\mathrm d'\mathrm d''(HT)
=4\delta_{q_h}-2\delta_{q_v}.
\]
Moreover, the projection formulas are
\[
\tau_*T=T_\Sigma,
\]
\[
\tau_*(HT)=hT_\Sigma.
\]
Since \(\tau\) is proper, proper pushforward commutes with \(\mathrm d'\mathrm d''\). Therefore
\[
\tau_*\mathrm d'\mathrm d''[U]
=\tau_*\mathrm d'\mathrm d''[V]
=4\delta_0
\]
and
\[
\tau_*\mathrm d'\mathrm d''(HT)
=\mathrm d'\mathrm d''(hT_\Sigma)
=2\delta_0.
\]
This is exactly the displayed weighted cross-fan counterexample after tropical pushforward: it uses the same unbounded cross, the same four rays, the same unit-weighted psh functions \(u,v\), the same current weights \((2,2,1,1)\), and the same residual coefficient \(2\).

### (iii) Unresolved stronger upstairs-equality problem

The construction in (ii) does not satisfy
\[
\mathrm d'\mathrm d''[U]
=\mathrm d'\mathrm d''[V]
\]
on \(X\). In fact, its two sides are the distinct measures
\[
4\delta_{q_h}
\quad\text{and}\quad
2\delta_{q_h}+2\delta_{q_v}.
\]
Their pushforwards agree only because \(\tau\) identifies \(q_h\) and \(q_v\).

Consequently, this construction does not settle the stronger question of finding a good strict analytic space \(X'\), a positive closed analytic or delta-current \(T'\), and analytic psh functions \(U',V'\) such that
\[
\mathrm d'\mathrm d''[U']
=\mathrm d'\mathrm d''[V']
\]
before pushforward but
\[
\mathrm d'\mathrm d''\bigl((U'-V')T'\bigr)\ne0.
\]
That stronger question must remain open unless a separate construction or obstruction is verified.

## Proof blueprint

### Step 1: prove the compactness obstruction

The live definition begins with a compact strict analytic domain \(W\). A harmonic tropicalization is in particular continuous, so its image is compact. The cross \(\Sigma\) contains four unbounded rays and is not compact. This proves (i) without any geometric auxiliary hypothesis.

This conclusion must be recorded as an obstruction, not as a failure of the construction in (ii): the latter deliberately changes from a compact-domain harmonic tropicalization to a noncompact ordinary moment tropicalization with locally harmonic coordinates.

### Step 2: determine the analytic space

In the Laurent UFD \(K[x^{\pm1},y^{\pm1}]\), the prime elements \(x-1\) and \(y-1\) are nonassociate. Hence
\[
((x-1)(y-1))=(x-1)\cap(y-1).
\]
It follows that \(X\) is reduced with precisely the two one-dimensional components \(Y_h\) and \(Y_v\), and that
\[
Y_h\cap Y_v=\{p\}.
\]
The component quotients are Laurent polynomial rings in one variable, so each analytification is \(\mathbf G_m^{\mathrm{an}}\).

For \(\rho\in|K^\times|\), \(X_\rho\) is the Berkovich spectrum of a quotient of a strict Laurent Tate algebra. Hence it is a compact strict affinoid domain. The \(X_\rho\) exhaust \(X\). Enlarging \(\rho\) places every point of \(X_\rho\) in the relative interior of a larger \(X_{\rho'}\). This proves goodness, strictness, and absence of analytic boundary for \(X\). Both minimal components have dimension one, so \(X\) is pure one-dimensional.

The fixed compact domain \(X_\rho\) has four annular boundary endpoints. Only the exhausted full space \(X\) is asserted to be boundaryless.

### Step 3: determine the map and prove properness

On \(Y_h\) one has \(y=1\), so
\[
\tau|_{Y_h}=(-\log|x|,0).
\]
On \(Y_v\) one has \(x=1\), so
\[
\tau|_{Y_v}=(0,-\log|y|).
\]
The standard Gauss seminorms of every real radius show that these images are the two full coordinate lines. Hence \(\tau(X)=\Sigma\).

Both \(x\) and \(y\) are global analytic units on \(X\). Therefore their negative logarithmic norms are locally integral harmonic functions. On each compact \(X_\rho\), the restriction is a harmonic tropicalization by definition.

To prove properness, let \(C\subset\Sigma\) be compact. Choose \(R>0\) with \(C\subset[-R,R]^2\), and choose \(\rho\in|K^\times|\) with \(\log\rho>R\). Then
\[
\tau^{-1}(C)\subset X_\rho.
\]
It is closed in the compact domain \(X_\rho\), hence compact.

### Step 4: compute all tropical weights

On either component, the relevant nonconstant coordinate restricts to the standard map
\[
\mathbf G_m^{\mathrm{an}}\longrightarrow\mathbf R,\qquad
\xi\longmapsto-\log|T(\xi)|.
\]
Along the Gauss skeleton its two primitive slopes are \(+1\) and \(-1\). The lattice index is one, the generic analytic degree is one, and the residue-degree factor is one. Thus \([Y_h]\) contributes weight one to each horizontal ray and \([Y_v]\) contributes weight one to each vertical ray.

Linearity of calibrated cycle pushforward now gives
\[
\tau_*\delta_{2[Y_h]+[Y_v]}=T_\Sigma
\]
with weights \((2,2,1,1)\). No lattice, ramification, or residue factor is omitted.

The current \(T\) is strongly positive because \(Z\) is effective. It is \(\mathrm d'\)- and \(\mathrm d''\)-closed by componentwise analytic Stokes on the boundaryless curves \(Y_h,Y_v\), using compactly supported test forms. The singular intersection point introduces no boundary term.

### Step 5: verify psh approximation

The ambient functions
\[
u_j(s,t)=2\sqrt{s^2+\varepsilon_j},
\]
\[
v_j(s,t)=\sqrt{s^2+\varepsilon_j}
          +\sqrt{t^2+\varepsilon_j}
\]
are smooth and convex on \(\mathbf R^2\). Pullback through a moment map therefore gives smooth psh functions on every tropical chart of \(X\). Since \(\varepsilon_j\downarrow0\), the sequences decrease locally uniformly to \(U\) and \(V\). Stability under locally uniform decreasing limits gives the asserted continuous psh limits.

### Step 6: compute the analytic atoms

On \(\mathbf G_m^{\mathrm{an}}\), with \(a=-\log|T|\) and unit Gauss point \(\eta_0\), the manuscript normalization is
\[
\mathrm d'\mathrm d''[|a|]=2\delta_{\eta_0}.
\]
There are no additional atoms: \(|a|\) is locally constant away from the Gauss skeleton, affine away from \(a=0\) on that skeleton, and compactly supported tests eliminate end contributions.

On \(Y_h\),
\[
U=2|-\log|x||,\qquad
V=|-\log|x||,\qquad
H=|-\log|x||.
\]
On \(Y_v\),
\[
U=0,\qquad
V=|-\log|y||,\qquad
H=-|-\log|y||.
\]
Applying the one-dimensional formula componentwise yields
\[
\mathrm d'\mathrm d''[U]=4\delta_{q_h},
\]
\[
\mathrm d'\mathrm d''[V]
=2\delta_{q_h}+2\delta_{q_v}.
\]
Since \(T\) has coefficient \(2\) on \(Y_h\) and coefficient \(1\) on \(Y_v\),
\[
HT
=2|-\log|x||\,\delta_{Y_h}
 -|-\log|y||\,\delta_{Y_v},
\]
and hence
\[
\mathrm d'\mathrm d''(HT)
=4\delta_{q_h}-2\delta_{q_v}.
\]

Near the rigid node \(p\), \(|x|=|y|=1\) on sufficiently small branch neighborhoods, so all the displayed functions are locally constant there. Thus there is no node atom.

### Step 7: apply the projection formula

Because \(H=h\circ\tau\), multiplication of the order-zero current \(T\) by \(H\) and the calibrated projection formula give
\[
\tau_*(HT)
=h\,\tau_*T
=hT_\Sigma.
\]
Properness permits pushforward of compactly supported current tests and gives
\[
\tau_*\mathrm d'\mathrm d''(HT)
=\mathrm d'\mathrm d''\tau_*(HT).
\]
Both \(q_h\) and \(q_v\) map to \(0\), so
\[
\tau_*(4\delta_{q_h}-2\delta_{q_v})
=2\delta_0.
\]
The same atomic pushforward gives
\[
\tau_*(4\delta_{q_h})
=\tau_*(2\delta_{q_h}+2\delta_{q_v})
=4\delta_0.
\]
This proves every assertion in (ii).

### Step 8: isolate the remaining open strengthening

Since \(q_h\ne q_v\), the two analytic curvature measures in Step 6 are unequal. The equality after pushforward is therefore strictly weaker than equality on \(X\). This proves only the limitation of the present construction; it proves neither existence nor nonexistence for the stronger upstairs-equality problem. The latter must remain separately labelled open.

## Ledger consequence proposed for later live editing

- P21.1: retire as **obstruction proved** (negative realization answer in the literal live sense), and cross-reference the noncompact locally harmonic relaxation.
- P21.2: retire as **proved**, using \(T=\delta_{2[Y_h]+[Y_v]}\) and the calibrated pushforward \(\tau_*T=T_\Sigma\).
- Do not silently identify these retirements with the stronger upstairs-equality problem. If that strengthening is to be tracked, give it a separate atom and leave it open.

No live ledger or chapter change is made by this packet.
