# Xia Conjecture 8.8: repaired proof packet

## Statement

Let \(X\) be a connected smooth projective complex variety of dimension
\(n\).  For \(1\leq i\leq n\), let \(L_i\) be a big line bundle and let
\(h_i\) be a singular plurisubharmonic metric on \(L_i\) with positive Cao
volume.  For every surjective valuation
\[
 \nu:\mathbb C(X)^\times\longrightarrow\mathbb Z^n_{\mathrm{lex}}
\]
that is trivial on \(\mathbb C^\times\), let
\(\Delta_\nu(L_i,h_i)\) be the multiplier-ideal partial Okounkov body.
Normalize mixed Euclidean volume by \(V(K,\ldots,K)=\lambda_n(K)\), and
define the mixed volume of the metrics by
\[
 \operatorname{vol}(\mathrm d\mathrm d^c h_1,\ldots,
                     \mathrm d\mathrm d^c h_n)
 :=\int_X\bigwedge_{i=1}^n
 \left(\theta_i+\mathrm d\mathrm d^c
       P_{\theta_i}[\varphi_i]_{\mathcal I}\right),
\]
where \(h_i=h_i^0\mathrm e^{-\varphi_i}\) and the product is the
non-pluripolar product.  Then
\[
 \operatorname{vol}(\mathrm d\mathrm d^c h_1,\ldots,
                     \mathrm d\mathrm d^c h_n)
 =n!\sup_\nu V\bigl(\Delta_\nu(L_1,h_1),\ldots,
                     \Delta_\nu(L_n,h_n)\bigr).
\]

## Proof

### Imported inputs and their exact roles

The non-elementary external inputs used below are listed here.  Elementary
algebraic and convex-geometric facts invoked in the argument are proved or
identified at the point where they are used.

1. **Partial Okounkov bodies.**  On the positive-mass locus, partial bodies
   satisfy the diagonal volume formula, monotonicity for the
   \(\mathcal I\)-preorder, Minkowski superadditivity, and Hausdorff
   continuity for \(d_S\).  Replacing a potential by its model envelope or
   by an \(\mathcal I\)-equivalent potential does not change the body.  For
   analytic singularities, a log resolution
   \(\pi^*T=[D]+R\) gives
   \(\Delta_\nu(T)=\Delta_\nu(\{R\})+\nu(D)\).  These are the results in
   Xia, *Singularities in global pluripotential theory*, Chapter 10
   (in particular the volume, order, continuity, Minkowski, birational, and
   log-resolution statements).
   The version used for these imports is the author-hosted edition updated
   18 July 2026 (SHA-256
   `c816eea5f06822021fa8dd75b70f82724ee47e6dcd6830729f5ecc109296b706`).

2. **Ordinary Okounkov bodies.**  They are numerical invariants, obey
   homogeneity and Minkowski superadditivity, have Euclidean volume
   \(\operatorname{vol}(L)/n!\), and their normalized finite-level convex
   hulls converge in Hausdorff distance.  For a big complete series and a
   surjective rank-\(n\) valuation, sufficiently divisible levels contain
   values whose differences generate \(\mathbb Z^n\).

3. **The \(d_S\) package.**  Model projection preserves the \(d_S\)-class.
   A \(d_S\)-convergent sequence of positive-mass model potentials, with a
   uniform positive lower mass bound, has a subsequence trapped between an
   increasing and a decreasing sequence converging to the same limit.
   The \(P\)-preorder is closed under \(d_S\)-convergence.  Mixed
   non-pluripolar products are continuous when each entry converges in
   \(d_S\).  Every positive-mass \(\mathcal I\)-good potential admits
   \(d_S\)-approximants with analytic singularities whose currents are
   Kähler.  These are the approximation, order-closure, and continuity
   results in Chapters 6 and 7 of the same book.

   For closed positive currents
   \(T_i=\theta_i+\mathrm d\mathrm d^c\varphi_i\), Xia,
   *Transcendental b-divisors I---Correspondence with currents*, Definition
   3.2 and Theorem 3.5, identifies Cao's mixed volume with the Darvas--Xia
   mixed volume.  When each pure volume is positive, Definition 3.2 gives
   this mixed volume as the mixed non-pluripolar mass of the
   \(\mathcal I\)-model envelopes.  Proposition 3.3 gives compatibility
   with the pure volume.  No result from *Transcendental b-divisors II* is
   needed for this identification.

4. **Positive products in the projective setting.**  Let \(X\) be smooth
   projective and let \(\alpha_i\) be big numerical divisor classes.  If
   \(\mu:Y\to X\) is a modification and
   \(\mu^*\alpha_i=\beta_i+[E_i]\), where \(\beta_i\) is nef and
   \(E_i\geq0\), then Boucksom--Favre--Jonsson, Proposition 2.13, gives
   \(\beta_1\cdots\beta_n\leq
   \langle\alpha_1,\ldots,\alpha_n\rangle\).  By their Proposition 2.12,
   positive and ordinary intersections agree on nef classes.  Finally,
   Boucksom--Eyssidieux--Guedj--Zeriahi, Definition 1.17, identifies the
   cohomology class of the mixed non-pluripolar product of currents with
   minimal singularities in big classes with the corresponding positive
   product; in top degree their integrals therefore agree.

5. **A flag realizing an ample mixed intersection.**  Wilms, Theorem 1.1
   in arXiv:2502.18441v3: for ample \(\mathbb Q\)-line bundles
   \(A_1,\ldots,A_n\) on an irreducible projective \(n\)-fold, there is an
   admissible flag \(Y_\bullet\) such that
   \[
     A_1\cdots A_n=n!V(\Delta_{Y_\bullet}(A_1),\ldots,
                         \Delta_{Y_\bullet}(A_n)).
   \]

6. **Initial ideals and toric mixed degree.**  Kaveh--Manon, Lemma 2.16
   and Proposition 8.10 in arXiv:1610.00298v4, supply respectively the
   inclusion of the valuation initial ideal in the toric ideal and the
   realization of a lexicographic matrix initial ideal by one rational
   weight vector.  The Bernstein--Kushnirenko theorem identifies the mixed
   degree of the associated toric compactification with \(n!\) times the
   mixed volume of its exponent polytopes.

### 1. A finite-level estimate

Let \(F/\mathbb C\) be a finitely generated field of transcendence degree
\(n\), let \(X_0\) be an integral projective model of \(F\), and let
\(\nu:F^\times\to\mathbb Z^n_{\mathrm{lex}}\) be surjective and trivial on
\(\mathbb C^\times\).  Let \(W_1,\ldots,W_n\subset F\) be nonzero
finite-dimensional vector spaces.  Let
\[
 \Phi:X_0\dashrightarrow\prod_i\mathbb P(W_i^\vee)
\]
be the joint evaluation map and let \(Y\) be the closure of its image.
Assume that \(\Phi\) is birational onto \(Y\) and that
\[
 \operatorname{span}_{\mathbb Z}
 \{\nu(f)-\nu(g):f,g\in W_i^\times,\ 1\leq i\leq n\}
 =\mathbb Z^n.
\]
Put \(P_i=\operatorname{Conv}\nu(W_i^\times)\), and let \(H_i\) be the
hyperplane class from the \(i\)-th factor.  We claim
\[
 n!V(P_1,\ldots,P_n)\leq(H_1\cdots H_n\cdot Y).                 \tag{1}
\]

Because the rational rank of \(\nu\) is \(n=\operatorname{trdeg}F\),
Abhyankar's inequality gives residue transcendence degree zero.  The residue
field contains \(\mathbb C\), which is algebraically closed, hence it equals
\(\mathbb C\).  Every nonzero leaf of the valuation filtration is therefore
one-dimensional.  Choose a basis \(f_{ij}\) of each \(W_i\), one vector for
each distinct value \(a_{ij}=\nu(f_{ij})\).

Choose \(u_1,\ldots,u_n\in F^\times\) with \(\nu(u_\ell)=e_\ell\).
One-dimensional leaves yield a graded isomorphism
\[
 \mathbb C[\mathbb Z^n]\simeq\operatorname{gr}_\nu F,
 \qquad \chi^a\longmapsto\operatorname{in}_\nu(u^a).
\]
After rescaling the \(f_{ij}\), their initial forms are \(\chi^{a_{ij}}\).

Let \(S=\mathbb C[x_{ij}]\), multigraded by \(\deg x_{ij}=e_i\), and let
\(I\) be the multihomogeneous prime ideal of \(Y\).  Give \(x_{ij}\) the
lexicographic matrix weight \(a_{ij}\), and set
\(Q=\operatorname{in}_{\mathsf A}(I)\).  Define
\[
 J=\ker\left(S\longrightarrow
 \mathbb C[\mathbb Z^n][t_1,\ldots,t_n],\quad
 x_{ij}\longmapsto\chi^{a_{ij}}t_i\right).
\]
Taking the least-valuation part of every relation among the \(f_{ij}\)
shows \(Q\subseteq J\).  Kaveh--Manon Proposition 8.10 gives a rational
scalar weight \(\omega\) with \(Q=\operatorname{in}_\omega(I)\).  After
clearing denominators, the weight is integral.  The associated graded
degeneration preserves every finite-dimensional multihomogeneous piece:
\[
 \dim(S/I)_{\mathbf d}=\dim(S/Q)_{\mathbf d}
 \quad(\mathbf d\in\mathbb N^n).                              \tag{2}
\]

The ideal \(J\) defines the closure \(Z\) of the monomial map
\[
 (\mathbb C^\times)^n\longrightarrow
 \prod_i\mathbb P(W_i^\vee),\qquad
 z\longmapsto([z^{a_{i0}}:\cdots:z^{a_{ir_i}}])_i.
\]
The exponent differences generate \(\mathbb Z^n\), so the induced map on
character lattices is surjective and the monomial map is a closed immersion
on the torus.  Thus \(Z\) is irreducible of dimension \(n\).  Since
\(Q\subseteq J\), \(Z\) is contained in
\(Y_0=\operatorname{MultiProj}(S/Q)\).  Equality (2) gives the same
multigraded Hilbert polynomial for \(Y\) and \(Y_0\): passing to
\(\operatorname{MultiProj}\) only removes irrelevant torsion and therefore
does not change the sufficiently large multidegrees, while
\(\mathcal O(1,\ldots,1)\) is ample on the ambient product.  Hence
\(\dim Y_0=\dim Y=n\); consequently \(Z\) is a top-dimensional component
of \(Y_0\).

Writing the top-dimensional fundamental cycle as
\([Y_0]_n=\sum_Wm_W[W]\), all \(m_W\) are positive and the globally
generated classes \(H_i\) have nonnegative mixed degree on each component.
The leading multigraded Hilbert coefficients in (2) therefore give
\[
 (H_1\cdots H_n\cdot Y)
 =(H_1\cdots H_n\cdot[Y_0]_n)
 \geq(H_1\cdots H_n\cdot Z).                                  \tag{3}
\]
The exponent polytopes of \(Z\) are \(P_i\).  General hyperplanes in the
\(n\) factors have no common point on \(Z\setminus(\mathbb C^\times)^n\):
if some \(W_i\) is one-dimensional, then \(P_i\) is a point and the mixed
volume in (1) is zero, so (1) is already immediate; hence we may assume here
that every factor has positive-dimensional hyperplanes.  Under this
assumption,
the boundary has dimension at most \(n-1\), while the incidence condition
that a hyperplane in each factor contain a fixed boundary point has total
codimension \(n\).  Hence the mixed degree is computed on the dense torus.
The Bernstein--Kushnirenko theorem yields
\[
 (H_1\cdots H_n\cdot Z)=n!V(P_1,\ldots,P_n).
\]
Together with (3), this proves (1).

### 2. The movable upper bound

Let \(D_1,\ldots,D_n\) be big \(\mathbb Q\)-divisors on a smooth
projective \(X\).  For every valuation \(\nu\) as in the statement,
\[
 n!V(\Delta_\nu(D_1),\ldots,\Delta_\nu(D_n))
 \leq\langle D_1,\ldots,D_n\rangle.                            \tag{4}
\]
By homogeneity, clear denominators.  Choose rational trivializations near
the center of \(\nu\), and write
\(W_{i,k}=H^0(X,\mathcal O_X(kD_i))\) inside \(\mathbb C(X)\), up to the
resulting harmless translation.  For a sufficiently divisible \(p\), all
maps given by \(|pD_i|\) are birational, and the complete series for one
\(D_i\) contains values whose differences are the standard basis of
\(\mathbb Z^n\): choose \(s_0,s_1,\ldots,s_n\) at that level with
\(\nu(s_j)-\nu(s_0)=e_j\).  If \(k=mp\), then
\(s_0^m,s_js_0^{m-1}\) still have value difference \(e_j\).  Moreover, the
degree-\(k\) complete series contains the symmetric-power subsystem whose
map is the Veronese of the degree-\(p\) birational map.  Therefore the joint
evaluation map is birational and its combined value lattice is
\(\mathbb Z^n\) for every \(k\) divisible by \(p\).

Let \(P_{i,k}=\operatorname{Conv}\nu(W_{i,k}^\times)\).  Resolve all base
ideals simultaneously and write
\[
 \mu_k^*(kD_i)=M_{i,k}+F_{i,k},
 \qquad M_{i,k}\text{ basepoint free},\quad F_{i,k}\geq0.
\]
The finite-level estimate and the projection formula give
\[
 n!V(P_{1,k},\ldots,P_{n,k})
 \leq M_{1,k}\cdots M_{n,k}
 \leq k^n\langle D_1,\ldots,D_n\rangle.                        \tag{5}
\]
The second inequality is precisely the nef-approximation property of the
movable product.  Divide by \(k^n\), let divisible \(k\to\infty\), and use
Hausdorff convergence of \(k^{-1}P_{i,k}\) and continuity of mixed volume.
This proves (4).

### 3. A corrected uniform convex-body lemma

For \(1\leq i\leq n\) and \(j\geq1\), let
\(A_{i,j},B_{i,j},C_{i,j},D_{i,j}\) be nonempty compact convex sets and
assume the **four** inclusions
\[
 A_{i,j}\subseteq C_{i,j}\subseteq B_{i,j},
 \qquad A_{i,j}\subseteq D_{i,j}\subseteq B_{i,j}.             \tag{6}
\]
Assume that constants \(v,M>0\), independent of \(i,j\), satisfy
\[
 \lambda_n(A_{i,j})\geq v,
 \quad \lambda_n(B_{1,j}+\cdots+B_{n,j})\leq M,
 \quad \lambda_n(B_{i,j})-\lambda_n(A_{i,j})\to0.             \tag{7}
\]
Then
\[
 |V(C_{1,j},\ldots,C_{n,j})-V(D_{1,j},\ldots,D_{n,j})|\to0.   \tag{8}
\]

For each \(i,j\), translate the entire quadruple by one vector so that
\(0\in A_{i,j}\).  By (6), \(0\in B_{i,j}\), and every one of the four
bodies is contained in
\(S_j=B_{1,j}+\cdots+B_{n,j}\).  Also
\(v\leq\lambda_n(S_j)\leq M\).  Send the John ellipsoid of \(S_j\) to the
unit ball by an affine map \(T_j(x)=L_jx+b_j\).  John's theorem gives
\[
 \mathbb B^n\subseteq T_j(S_j)\subseteq n\mathbb B^n,
 \qquad
 \frac{\lambda_n(\mathbb B^n)}{M}\leq|\det L_j|
 \leq\frac{n^n\lambda_n(\mathbb B^n)}{v}.                     \tag{9}
\]
Thus all transformed bodies lie in one compact set, the transformed
\(A_{i,j}\) have volume bounded below, and their volume gaps from the
transformed \(B_{i,j}\) tend to zero.  From any subsequence, Blaschke
selection supplies a further subsequence on which all \(4n\) bodies
converge.  At the limit, (6), equality of the positive volumes of the inner
and outer bodies, and strict volume monotonicity under proper inclusion of
full-dimensional compact convex sets imply
\(\widehat A_i=\widehat B_i=\widehat C_i=\widehat D_i\).  Continuity of
mixed volume proves (8) after transformation.  The lower determinant bound
in (9) transfers it back.  Since every subsequence has such a further
subsequence, (8) holds for the full sequence.

### 4. Pointwise potential sandwich

Let \(u_j,u\in\operatorname{PSH}(X,\theta)_{>0}\) be normalized model
potentials and suppose \(u_j\to u\) in \(d_S\).  After passage to a
subsequence there are increasing normalized model potentials \(\eta_j\)
and decreasing normalized model potentials \(\psi_j\) such that
\[
 \eta_j\leq u_j\leq\psi_j,
 \qquad \eta_j\to u,\quad\psi_j\to u\quad\text{in }d_S.       \tag{10}
\]
This is the imported \(d_S\)-sandwich theorem, followed, where necessary,
by model projection of the upper sequence.  More explicitly, if
\(\widetilde\psi_j\) is the decreasing upper sequence supplied before
projection, set \(\psi_j=P_\theta[\widetilde\psi_j]\).  Monotonicity of
\(P_\theta\) preserves decrease, model projection preserves the
\(d_S\)-class, and
\(u_j=P_\theta[u_j]\leq P_\theta[\widetilde\psi_j]=\psi_j\).
The lower sequence furnished by the sandwich construction is already model.

We need, and now prove, the additional comparisons omitted in the supplied
source:
\[
 \eta_j\leq u\leq\psi_j\qquad(j\geq1).                        \tag{11}
\]
Fix \(j\).  Monotonicity of \(\eta_k\) and (10) give
\(\eta_j\leq\eta_k\leq u_k\) for all \(k\geq j\).  Apply closure of the
\(P\)-preorder to the constant sequence \(\eta_j\) and the tail
\((u_k)_{k\geq j}\).  It gives \(\eta_j\preceq_Pu\).  Both are model
potentials, so this is the pointwise inequality \(\eta_j\leq u\).
Similarly, for \(k\geq j\),
\(u_k\leq\psi_k\leq\psi_j\).  Order closure gives
\(u\preceq_P\psi_j\), which becomes \(u\leq\psi_j\) because both are
model.  This proves (11).

For finitely many indices \(i=1,\ldots,n\), apply this construction
successively and take a diagonal subsequence.  Thus all sandwiches can be
assumed to use the same index \(j\).

### 5. Uniformity in the valuation

For each \(i\), let \(\varphi_{i,j}\to\varphi_i\) in \(d_S\), with all
limits of positive mass.  Then
\[
 \sup_\nu\left|
 V(\Delta_\nu(\theta_1,\varphi_{1,j}),\ldots,
   \Delta_\nu(\theta_n,\varphi_{n,j}))
 -V(\Delta_\nu(\theta_1,\varphi_1),\ldots,
   \Delta_\nu(\theta_n,\varphi_n))
 \right|\longrightarrow0.                                    \tag{12}
\]

Replace all potentials by their model envelopes.  Suppose (12) fails.
After a subsequence there are valuations \(\nu_j\) and \(\delta>0\) for
which the displayed difference is at least \(\delta\).  Use the simultaneous
version of (10)--(11).  By continuity of the diagonal masses and positivity
of the limiting masses, discard one finite initial segment so that every
inner, outer, approximating, and limiting body used below lies on the
positive-volume locus.  Put
\[
 \begin{aligned}
 A_{i,j}&=\Delta_{\nu_j}(\theta_i,\eta_{i,j}),&
 B_{i,j}&=\Delta_{\nu_j}(\theta_i,\psi_{i,j}),\\
 C_{i,j}&=\Delta_{\nu_j}(\theta_i,\varphi_{i,j}),&
 D_{i,j}&=\Delta_{\nu_j}(\theta_i,\varphi_i).
 \end{aligned}
\]
Body monotonicity and both pointwise sandwiches give exactly the four
inclusions (6).  The diagonal volume formula and \(d_S\)-continuity of
volume give, uniformly in \(\nu_j\),
\[
 \lambda_n(B_{i,j})-\lambda_n(A_{i,j})\to0,
 \qquad
 \lambda_n(A_{i,j})\to
 \frac1{n!}\operatorname{vol}(\theta_i,\varphi_i)>0.           \tag{13}
\]
Minkowski superadditivity and containment in the complete series give
\[
 B_{1,j}+\cdots+B_{n,j}
 \subseteq\Delta_{\nu_j}\left(\sum_i\theta_i,
                               \sum_i\psi_{i,j}\right)
 \subseteq\Delta_{\nu_j}(L_1\otimes\cdots\otimes L_n).
\]
The last body has Euclidean volume
\(\operatorname{vol}(L_1\otimes\cdots\otimes L_n)/n!\), independent of
\(j\) and \(\nu_j\).  Hence (7) holds, and the corrected convex-body lemma
contradicts the lower bound \(\delta\).  This proves (12).  In particular,
the suprema converge because
\(|\sup f_j-\sup f|\leq\sup|f_j-f|\).

### 6. Analytic singularities

Assume each \(h_i\) has analytic singularities and each curvature current is
Kähler.  On a common projective log resolution \(\pi:Y\to X\), write
\[
 \pi^*c_1(L_i,h_i)=[D_i]+R_i,
\]
where \(D_i\) is an effective \(\mathbb Q\)-divisor and \(R_i\) has bounded
potentials.  Put \(\alpha_i=\{R_i\}\).  Since
\(\alpha_i=\pi^*c_1(L_i)-\{D_i\}\), it belongs to
\(N^1(Y)_{\mathbb Q}\).  It is nef, and it is big because
\(\alpha_i^n>0\).  Birational invariance of non-pluripolar products gives
\[
 \int_X\bigwedge_i c_1(L_i,h_i)=\alpha_1\cdots\alpha_n.        \tag{14}
\]
For every valuation of the common function field,
\[
 \Delta_\nu(L_i,h_i)=\Delta_\nu(\alpha_i)+\nu(D_i).            \tag{15}
\]
Translations do not change mixed volume.  Applying (4), then nefness, yields
\[
 n!V(\Delta_\nu(L_1,h_1),\ldots,\Delta_\nu(L_n,h_n))
 \leq\alpha_1\cdots\alpha_n.                                  \tag{16}
\]

For the reverse inequality after taking the supremum, fix an ample
\(\mathbb Q\)-divisor \(H\) on \(Y\).  Choose one rational \(c>0\) such
that every \(c\alpha_i-H\) is big, and choose an effective
\(\mathbb Q\)-divisor \(E_i\) in that class.  For rational
\(\varepsilon>0\), put \(\beta_i=\alpha_i+\varepsilon H\), which is ample.
Then
\[
 \alpha_i=\frac1{1+c\varepsilon}\beta_i
          +\frac{\varepsilon}{1+c\varepsilon}\{E_i\}.         \tag{17}
\]
Wilms's theorem gives an admissible flag with valuation \(\nu_\varepsilon\)
such that
\[
 n!V(\Delta_{\nu_\varepsilon}(\beta_1),\ldots,
      \Delta_{\nu_\varepsilon}(\beta_n))
 =\beta_1\cdots\beta_n.                                      \tag{18}
\]
To justify the body inclusion without pretending that the effective class
\(E_i\) is big, choose \(\mathbb Q\)-divisor representatives and set
\[
 A_i:=\frac1{1+c\varepsilon}\,\beta_i
      +\frac{\varepsilon}{1+c\varepsilon}\,E_i.
\]
Equation (17) says that \(A_i\equiv\alpha_i\), hence numerical invariance
gives \(\Delta_\nu(A_i)=\Delta_\nu(\alpha_i)\).  After clearing all
denominators, multiply a section of the relevant multiple of \(\beta_i\)
by the corresponding power of the canonical section of \(E_i\).  Taking
valuation vectors, dividing by the common multiple, and closing yields
\[
 \frac1{1+c\varepsilon}\Delta_{\nu_\varepsilon}(\beta_i)
 +\frac{\varepsilon}{1+c\varepsilon}\nu_\varepsilon(E_i)
 \subseteq\Delta_{\nu_\varepsilon}(\alpha_i).                 \tag{19}
\]
The flag valuation is among the valuations in the theorem.  By (18), (19),
and translation invariance,
\[
 \sup_\nu V(\Delta_\nu(\alpha_1),\ldots,\Delta_\nu(\alpha_n))
 \geq\frac{\beta_1\cdots\beta_n}
          {n!(1+c\varepsilon)^n}.
\]
Let rational \(\varepsilon\downarrow0\).  Together with (14)--(16), this
proves the desired formula for analytic singularities.

### 7. General positive-volume metrics

Write \(h_i=h_i^0\mathrm e^{-\varphi_i}\).  Replace \(\varphi_i\) by
\(u_i=P_{\theta_i}[\varphi_i]_{\mathcal I}\).  This changes neither the
partial body nor the mixed volume in the statement.  For completeness,
\(u_i\) is also a model potential: it is an \(\mathcal I\)-fixed point;
the model envelope \(P_{\theta_i}[u_i]\) is \(\mathcal I\)-equivalent to
\(u_i\), so maximality of the \(\mathcal I\)-envelope gives
\(P_{\theta_i}[u_i]\leq u_i\), while \(u_i\), after normalization, is
itself a competitor for its model envelope and gives the reverse inequality.
The positive Cao-volume hypothesis says precisely that \(u_i\) has positive
mass.

Choose analytic-singularity potentials \(u_{i,j}\) such that
\[
 u_{i,j}\longrightarrow u_i\quad\text{in }d_S,
 \qquad \theta_i+\mathrm d\mathrm d^c u_{i,j}
 \text{ is a Kähler current}.
\]
For every \(j\), the analytic case gives
\[
 \int_X\bigwedge_i(\theta_i+\mathrm d\mathrm d^c u_{i,j})
 =n!\sup_\nu
 V(\Delta_\nu(\theta_1,u_{1,j}),\ldots,
   \Delta_\nu(\theta_n,u_{n,j})).                             \tag{20}
\]
Mixed non-pluripolar products are continuous under the finitely many
\(d_S\)-convergences, so the left side of (20) tends to
\(\int_X\bigwedge_i(\theta_i+\mathrm d\mathrm d^c u_i)\).
The valuation-uniform convergence (12) shows that the right side tends to
\[
 n!\sup_\nu V(\Delta_\nu(\theta_1,u_1),\ldots,
                  \Delta_\nu(\theta_n,u_n)).
\]
Taking limits in (20) proves the statement.

Finally, taking all \(h_i\) with minimal singularities yields
\[
 \langle L_1,\ldots,L_n\rangle
 =n!\sup_\nu V(\Delta_\nu(L_1),\ldots,\Delta_\nu(L_n)),
\]
the ordinary movable-product formula.

### Repairs relative to the supplied source

1. The uniform convex-body lemma now assumes both intermediate bodies lie
   between the same inner and outer bodies, as required by its proof.
2. The application records all four inclusions; the two involving the limit
   potential use the additional pointwise comparisons in (11).
3. The pointwise comparisons in (11) are proved from tail inequalities,
   closure of the \(P\)-preorder, and modelness, rather than asserted as an
   immediate consequence of order closure.
4. The simultaneous subsequence for the finitely many potentials is made
   explicit.
5. The rationality of the residual nef classes on the log resolution is
   stated before applying the \(\mathbb Q\)-divisor movable upper bound.
6. The reduction to \(\mathcal I\)-model representatives explicitly checks
   preservation of both sides and positive mass.
