# P09.2 product--Gauss argument: primary-source and quantifier audit

## 26 August final-scope addendum

The frozen production statement replaces the provisional smoothness
hypothesis on (X) below by the natural hypothesis that (X) is an
algebraic (K)-variety.  This broadening is source-supported:
Gubler's Proposition 7.2 is stated for an arbitrary algebraic variety, and
the proof uses no smoothness of (X).  The final proof also defines the
relative Gauss point for every (w\in N_{\mathbf R}), while using constant
(K)-section density only for (w\in N\otimes_{\mathbf Z}\Gamma).  A final
independent source audit and a separate proof audit passed these exact
quantifiers before the production run.  The provisional scope description
below is retained as dated audit history and is superseded by this addendum.

This is an isolated editorial audit.  It is not a theorem claim, is not a
novelty or priority claim, and is not to be input into a live chapter before
the resulting statement and proof have passed production Rethlas
verification.

## 1. Scope audited

The intended abstract local argument has the following data.

- (K) is algebraically closed, complete, nontrivially valued, and
  (Gamma=-\log |K^\times|\).
- (X) is a smooth algebraic (K)-variety with an algebraic action
  (\mu:T\times X\to X) of a split torus (T).  Write
  (M=X^*(T)), (N=\operatorname{Hom}(M,\mathbf Z)).
- (h:X^{\mathrm{an}}\to N_{\mathbf R}) is locally integral PL and satisfies

  \[
       h(t\cdot x)=\operatorname{trop}_T(t)+h(x).
  \]
- (q) is a nondegenerate symmetric bilinear form on (N_{\mathbf R}), and

  \[
       F(w)=\tfrac12q(w,w)+\ell(w)+a
  \]
  with (\ell) linear.

The point to justify is the implication

\[
 F\circ h\text{ ordinary GK delta}
 \quad\Longrightarrow\quad
 \langle m,h\rangle\text{ smooth for every }m\in M_{\mathbf R}.
\]

The Raynaud application takes (X=E), (h=\tau), and (q=q_L).  The
product--Gauss proof deliberately avoids identifying the residue of
(\langle m,\tau\rangle) at a canonical Gauss germ with a line bundle on
(B_s).  The last step instead uses the global smoothness criterion in
CLD Remark 19.2.3.

## 2. Primary-source findings

### 2.1 GK Definition 9.9: the ambient codimension-zero condition

**Verified, with a load-bearing distinction.**  In Gubler--K\"unnemann,
*A tropical approach to non-Archimedean Arakelov geometry*, Definition 9.9,
a delta-metric is locally represented by a piecewise-smooth weight (\phi)
on (\operatorname{Trop}(U)), and condition (ii) requires a bidegree-((1,1))
superform (\gamma) on the **full ambient vector space** (N_{U,\mathbf R}),
with piecewise-smooth coefficients, whose restriction is
(\mathrm d'_{\mathrm P}\mathrm d''_{\mathrm P}\phi).  Remark 9.10 and
Example 2.10 identify this object with a codimension-zero delta-preform.
Definition 1.6 defines a piecewise-smooth coefficient as one global function
whose restrictions to the cells are smooth.  Thus its value, and hence the
ambient coefficient tensor of (\gamma), has one common limit at a wall.

This is strictly stronger than having unrelated smooth Hessians on the
individual cells of a polyhedral support.  The product--Gauss contraction is
therefore legitimate only with the single ambient tensor supplied by
Definition 9.9(ii).

GK Proposition 9.15 proves pullback stability for a morphism of **algebraic
varieties**.  It applies directly to the algebraic action
(\mu:T\times X\to X).  It does not, by itself, state invariance under an
arbitrary analytic local isomorphism.

### 2.2 Gubler 2016, Proposition 7.2: algebraization of analytic moments

**Verified.**  The source is Walter Gubler, *Forms and currents on the
analytification of an algebraic variety (after Chambert-Loir and Ducros)*,
published in the 2016 Simons Symposia volume (arXiv:1303.7364v3).  Its global
standing assumptions are that (K) is algebraically closed, complete, and
nontrivially valued.  In Section 7 the analytic spaces are also taken strict.

Proposition 7.2 says precisely: if (X) is algebraic over (K),
(W\subset X^{\mathrm{an}}) is open, and
(\varphi:W\to T^{\mathrm{an}}) is an analytic moment map to a split torus,
then for every (x\in W) there are a very affine open (U\subset X), an
algebraic moment map (\varphi':U\to T), and an open neighbourhood
(V\subset U^{\mathrm{an}}\cap W) of (x) such that

\[
                 \varphi_{\mathrm{trop}}
                 =\varphi'_{\mathrm{trop}}\quad\text{on }V.
\]

The conclusion is equality of tropicalizations, not equality of the analytic
and algebraic functions.  Its proof truncates convergent Laurent series so
that the truncated Laurent polynomials have exactly the same absolute values
on a smaller neighbourhood.

The finite simultaneous form used in the candidate is valid: package finitely
many analytic units into one analytic moment map to a product torus and apply
Proposition 7.2 once.  If a GK chart is required to use the canonical moment
map of a very affine open, Gubler Section 4.12 says that the algebraic moment
map factors through that canonical moment map.  Hence an ambient form may be
pulled back by the resulting integral-affine map.

The same algebraization is also visible in the converse half of GK
Proposition 8.4.  Citing Gubler 2016 Proposition 7.2 is more direct and fixes
the previously ambiguous `Gub16` reference.

### 2.3 Ordinary delta-metricity under an analytic local isomorphism

**Not stated verbatim in GK; valid in the algebraizable scope by the following
argument.**  Let (X,Y) be algebraic (K)-varieties, let
(\iota:V_X\simeq V_Y) be an analytic isomorphism between analytic opens,
and suppose algebraic line bundles on (X,Y) are identified on these opens,
with one metric the pullback of the other.

Take a GK delta-presentation on (Y), with algebraic frame (s_Y), finitely
many algebraic moment coordinates (f_1,\ldots,f_r), weight (\phi), and
ambient form (\gamma).  Relative to an algebraic frame (s_X), the pulled
back frame is (g s_X) for an invertible analytic function (g).  Package

\[
       (f_1\circ\iota,\ldots,f_r\circ\iota,g)
\]

as one analytic moment.  Gubler Proposition 7.2 algebraizes all coordinates
simultaneously without changing their logarithmic absolute values.  On the
new target the weight is (\phi\circ\operatorname{pr}_1), plus or minus the
last affine coordinate according to the frame convention, and the ambient
Hessian is (\operatorname{pr}_1^*\gamma).  Factoring through the canonical
moment map of the new very affine open gives a GK Definition 9.9
presentation.  Apply the same argument to (\iota^{-1}).

Thus ordinary delta-metricity is invariant under analytic local
isomorphisms **between analytifications of algebraic varieties, for
algebraic line bundles**, under the standing hypotheses of Gubler
Proposition 7.2.  This argument does not establish the same statement for
arbitrary nonalgebraizable analytic spaces.

### 2.4 CLD Proposition 19.2.5: the cubical weight

**Verified.**  After choosing (\varepsilon:p^*L\simeq q^*M), CLD
Proposition 19.2.5 gives a unique real quadratic function (f) on
(T_{\mathrm{trop}}) such that, for every local invertible section (s),

\[
 \log\lVert s\rVert^{-1}
 -\log\lVert\varepsilon(s)\rVert^{-1}=f\circ\tau.
\]

Its homogeneous component of degree two is (\frac12q_L).  Consequently
(f=\frac12q_L+\text{affine}).  If the manuscript instead uses (q_L) for
the polarized bilinear form, this must be written
(f(w)=\frac12q_L(w,w)+\ell(w)+a).  The two notations must not be mixed.

This source proves an identity of **metric weights**, not merely an equality
of Chern currents, so dividing the cubical pullback metric by its formal
factor really leaves the trivial metric with weight (f\circ\tau).

### 2.5 CLD Remark 19.2.3: smoothness and the residual extension

**Verified.**  In torus rank one the extension is described by a formal
line bundle (Q) on the good-reduction formal abelian scheme.  CLD identifies
(\tau) with its formal metric weight and, using Proposition 17.4.13, states
that (\tau) is smooth if and only if (Q_s) is torsion.  For an arbitrary
split torus (T\simeq\mathbf G_m^r), the remark states that the coordinate
functions (\tau_1,\ldots,\tau_r) are G-smooth, PL, and harmonic, and that
they are all smooth if and only if the residual extension of (B_s) by
(T_{\widetilde K}) is isotrivial.

This is exactly the global terminal implication needed by the product--Gauss
argument.  No separate claim that a residue at one canonical Gauss germ is
literally (Q_s) is required.

On an algebraic analytification, Gubler Proposition 7.2 identifies the local
CLD smooth presentation by analytic moments with a presentation using
algebraic moments.  Hence the word "smooth" in the terminal CLD criterion is
compatible with the smoothness obtained after Gauss specialization.

### 2.6 CLD Theorem B.6.4: positivity of (q_L)

**Verified.**  CLD Theorem B.6.4 says that (L) is ample if and only if the
residual line bundle (M_s) is ample on (B_s) and the quadratic form
(q_L) on (T_{a,\mathrm{trop}}) is positive definite.  Therefore, for an
ample (L), the polarized bilinear form is nondegenerate and

\[
       q_L^\sharp:N_{\mathbf R}\longrightarrow M_{\mathbf R}
\]

is an isomorphism.  The source does not require a separate symmetry
hypothesis for this positivity assertion.

CLD Remark B.6.6 also records that in the algebraic abelian-variety setting
the Raynaud extension (E) is algebraizable and the (T)-action is
algebraic.  In the split situation CLD 19.2.1 and Appendix B.5 describe
(p:E\to A^{\mathrm{an}}) as the analytic covering by the lattice.  These
facts place both the algebraic-action pullback and the analytic-local-
isomorphism lemma above in their proved scopes.

The word "split" is essential here.  CLD B.5.14 explicitly warns that before
splitting the lattice, the general map \(p\) need not be a local
isomorphism.  The present theorem assumes \(K\) algebraically closed and
works with the split Raynaud uniformization, so that warning does not affect
this application; it prevents exporting the same sentence unchanged to a
non-split ground field.

## 3. Product Gauss points and the generic-lineality quantifiers

CLD 12.1.9 identifies the canonical skeleton of a split torus with its
tropical vector space.  More importantly, CLD 12.1.10--12.1.11 constructs,
for every analytic space (X), the point

\[
   \operatorname{sq}_x(w)\in T_{\mathscr H(x)}^{\mathrm{an}}
      \subset T\times X
\]

and proves that ((w,x)\mapsto\operatorname{sq}_x(w)) is continuous.  This
is the precise product Gauss point required here.

The continuity removes the apparent circularity in choosing a generic
(w):

1. start with one product Gauss point (z_{w_0}=\operatorname{sq}_x(w_0))
   and one ordinary delta-chart on an analytic neighbourhood of it;
2. refine that fixed chart so that it includes the torus characters, a
   factorization of (\operatorname{trop}_T+h), a complex of definition for
   that factorization, and a complex for the finitely many coefficients of
   the ambient form;
3. only after this finite data is fixed, move (w_0) slightly to (w).
   Continuity of the Shilov section keeps (z_w) inside the same chart.

Each algebraic unit defining the fixed chart is, over (K(X)), a quotient
of finite Laurent polynomials in the characters of (T).  At (z_w) its
norm is the maximum of finitely many quantities

\[
        |c_u(x)|\exp(-\langle u,w\rangle).
\]

Nonunique maxima lie on finitely many proper affine hyperplanes after equal
terms are combined.  Pulling back the finitely many polyhedral walls along
the resulting affine skeleton map adds only finitely many proper walls,
unless a wall contains the whole fibre germ, in which case its tangent
already contains the torus direction.  Since (K) is algebraically closed,
(\Gamma) is nonzero and divisible, hence dense in (\mathbf R).  One can
therefore choose

\[
              w\in N\otimes_{\mathbf Z}\Gamma
\]

arbitrarily close to (w_0), outside every proper wall.  After adjoining a
basis of torus characters, the resulting torus-slope map
(a:N_{\mathbf R}\hookrightarrow\mathbf R^s) is injective.  The minimal
cell (C) containing the tropical image of (z_w) contains a neighbourhood
of that image inside the affine product-Gauss fibre, and therefore

\[
              a(N_{\mathbf R})\subset L_C.
\]

The same inclusion holds for every cell in the star of (C).  This is the
needed lineality conclusion.  The order "fix chart and all walls, then choose
(w)" is essential.

With (H=\operatorname{trop}_T+h), equivariance gives
(D_\sigma H(a(v))=v).  If (G_0) is the one ambient coefficient tensor at
the wall supplied by GK Definition 9.9, then on each star cell

\[
 G_0|_{L_\sigma\times L_\sigma}
   =q(D_\sigma H\,\mathord\cdot,D_\sigma H\,\mathord\cdot).
\]

Contracting with (a(v)) shows that the derivative of (q(v,H)) is the
same ambient covector on every star cell.  The values agree at the common
point, so (q(v,H)) is one ambient real-affine germ.  Nondegeneracy of (q)
then gives that

\[
       \langle m,\operatorname{trop}_T+h\rangle
\]

is smooth near (z_w) for every (m\in M_{\mathbf R}).

## 4. The rational product-Gauss specialization

The two points below do not appear in the cited sources in exactly the
combined form needed by the proof.  They admit the following self-contained
proofs.

### 4.1 Rational points near a rational-polyradius torus Gauss point

Let (H) be a complete non-Archimedean field whose residue field is infinite,
let (T\simeq\mathbf G_{m,H}^r), and let
(w\in N\otimes\Gamma_H).  Then every analytic open neighbourhood of the
Gauss point (\eta_w\in T^{\mathrm{an}}) contains a point of (T(H)).  The
point can be chosen with tropicalization exactly (w).

Indeed, choose (c_i\in H^\times) with
(-\log|c_i|=w_i), and scale the coordinates by (c_i).  It is enough to
treat the unit Gauss point of

\[
 P=\mathcal M\bigl(H\langle Z_1^{\pm1},\ldots,Z_r^{\pm1}\rangle\bigr).
\]

A basic neighbourhood of that point is controlled by finitely many analytic
functions (f_j) and open intervals containing their Gauss norms.  For each
nonzero (f_j), its Gauss norm is the maximum of the norms of its
coefficients and is attained.  After normalization, its initial reduction
(\widetilde f_j) is a nonzero Laurent polynomial.  Because
(\widetilde H) is infinite, there is

\[
       \bar u\in(\widetilde H^\times)^r
\]

outside the zero loci of all the finitely many (\widetilde f_j).  Lift its
coordinates to units (u_i\in H^{\circ\times}).  Then

\[
                |f_j(u)|=\lVert f_j\rVert_{\mathrm G}
\]

for every (j), so (u) lies in the prescribed basic neighbourhood.
Scaling back gives (t_0=(c_i u_i)\in T(H)) with
(\operatorname{trop}(t_0)=w).

In the application (H=\mathscr H(x)).  Since (H) contains (K)
isometrically and (K) is algebraically closed, its residue field contains
the algebraically closed (hence infinite) field (\widetilde K).  The
infinite-residue-field hypothesis is therefore automatic.  Rationality of
(w) is not cosmetic: if a polyradius is not in
(|H^\times|^r), no (H)-rational point can have that polyradius.

### 4.2 Lifting the fibre point to an analytic local section

Let (X) be good at (x), put (H=\mathscr H(x)), and let
(\Omega\subset T\times X) be an analytic open containing an
(H)-rational point ((t_0,x)) of the fibre.  There are an open
neighbourhood (U\ni x) and invertible analytic functions
(g_1,\ldots,g_r\in\mathcal O_X(U)^\times) such that

\[
       s:U\longrightarrow T\times X,
       \qquad y\longmapsto(g_1(y),\ldots,g_r(y),y)
\]

has image in (\Omega).

CLD 11.1.10 states that a good analytic space is almost good, so

\[
       \kappa(x)=\mathcal O_{X,x}/\mathfrak m_x
          \quad\text{is dense in}\quad\mathscr H(x).
\]

Write (t_0=(a_1,\ldots,a_r)).  The fibre intersection
(\Omega_x\subset T_H^{\mathrm{an}}) is open.  Approximate each (a_i) by
an element of (\kappa(x)^\times) closely enough that the resulting
(H)-rational point still belongs to (\Omega_x); one may impose

\[
              |g_i(x)-a_i|<|a_i|,
\]

so the lifted germ (g_i\in\mathcal O_{X,x}) is invertible.  Represent the
finitely many germs on one common open neighbourhood.  The value (s(x))
lies in (\Omega), and continuity of (s) allows a final shrinking so that
(s(U)\subset\Omega).

This is also the exact approximation mechanism formalized by CLD Lemma
12.2.3: on an almost-good germ, an analytic unit on a domain can be replaced
near the point by an analytic unit on an open neighbourhood with the same
tropicalization.

### 4.3 Smooth specialization

Suppose

\[
       G_m(t,y)=\langle m,\operatorname{trop}_T(t)+h(y)\rangle
\]

is smooth on an open neighbourhood of the rational product Gauss point
(z_w).  Apply Section 4.1 in the fibre over (x), then Section 4.2, to get
an analytic local section (s(y)=(g(y),y)) whose image lies in that
neighbourhood.  Pullback of a CLD-smooth function by an analytic morphism is
smooth, hence

\[
 G_m\circ s
   =\langle m,h\rangle
     +\sum_i m_i(-\log|g_i|)
\]

is smooth.  The second summand is smooth because the (g_i) are analytic
units.  Therefore (\langle m,h\rangle) is smooth near (x).

This proves the required Gauss-specialization step without evaluating a
residual line bundle at the product Gauss point.

## 5. Raynaud application: source-closed implication chain

For an ample line bundle with its normalized cubical metric, the implication
chain supported by the audited sources is:

1. pull ordinary delta-metricity from (A^{\mathrm{an}}) to (E^{\mathrm{an}})
   using the analytic-local-isomorphism argument of Section 2.3;
2. use CLD Proposition 19.2.5 and divide by the formal metric on (q^*M),
   which is an ordinary delta-metric, leaving (F_L\circ\tau);
3. use the algebraic (T)-action on (E), GK Proposition 9.15, the
   product--Gauss lineality argument, and Sections 4.1--4.3 to show that all
   integral coordinates of (\tau) are smooth;
4. use CLD Theorem B.6.4 to know that (q_L) is positive definite, hence
   nondegenerate;
5. apply CLD Remark 19.2.3 to conclude that the residual Raynaud extension is
   isotrivial.

Conversely, CLD Remark 19.2.3 makes (\tau) smooth when the residual
extension is isotrivial.  CLD Proposition 19.2.5 then makes the nonformal
factor (F_L\circ\tau) smooth; Gubler Proposition 7.2 converts its finite
analytic-moment presentation locally to algebraic moments.  The product with
the formal factor is ordinary delta, and Section 2.3 transfers it through the
analytic covering to (A^{\mathrm{an}}).

## 6. Verdict and remaining proof obligations

**Source verdict:** the cited primary sources support every imported step in
the product--Gauss strategy, with the following corrections and scope
firewalls.

1. Cite Gubler 2016 Proposition 7.2, not an undefined `Gub16` key without a
   bibliography entry; record its algebraically closed, nontrivially valued,
   strict analytic scope.
2. State that Proposition 7.2 preserves tropicalizations/absolute values, not
   the analytic functions themselves.
3. Do not attribute analytic-local-isomorphism invariance to GK Proposition
   9.15.  Give the finite-moment algebraization proof in Section 2.3.
4. Choose the generic rational (w) only after the delta-chart, all moment
   coordinates, and all coefficient complexes have been fixed.
5. State explicitly that (w\in N\otimes\Gamma); otherwise the rational
   fibre point needed for specialization need not exist.
6. Use the good/almost-good hypothesis at (x).  It supplies
   (\kappa(x)\) dense in (\mathscr H(x)); do not write that the whole local
   ring is a dense subfield without quotienting by its maximal ideal.
7. Use CLD Remark 19.2.3 only for its stated global equivalence between
   smooth canonical tropicalization and isotrivial residual extension.  Do
   not claim an unproved equality between a one-point Gauss residue and
   (Q_s).
8. Freeze the normalization of (q_L): CLD calls (q_L) a quadratic form,
   whereas the candidate often uses the same symbol for its polarized
   bilinear form.

Subject to these explicit repairs, the product--Gauss source chain and its
quantifiers pass this audit.  Mathematical correctness of the assembled new
theorem still requires independent hostile review and production Rethlas
verification.

## 7. Exact local sources inspected

- Walter Gubler and Klaus K\"unnemann, *A tropical approach to
  non-Archimedean Arakelov geometry*: Definitions 1.6 and 9.9, Remark 1.7,
  Example 2.10, Remarks 9.10 and 9.14, Propositions 8.4, 9.15, and Remark
  9.16.
- Walter Gubler, *Forms and currents on the analytification of an algebraic
  variety (after Chambert-Loir and Ducros)*, arXiv:1303.7364v3 / 2016
  Simons Symposia publication: Sections 4.12 and 7.1, Proposition 7.2.
- Antoine Chambert-Loir and Antoine Ducros, *Formes diff\'erentielles
  r\'eelles et courants sur les espaces de Berkovich*, arXiv:1204.6277v2,
  25 July 2025: 11.1.10--11.1.11, 12.1.9--12.1.11, Lemma 12.2.3,
  Proposition 17.4.13, 19.2.1--19.2.5, Theorem B.6.4, Remark B.6.6.
