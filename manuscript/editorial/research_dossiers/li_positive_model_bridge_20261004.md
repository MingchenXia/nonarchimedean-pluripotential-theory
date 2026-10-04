# Positive reference metric after a vertical rational twist

Date: 4 October 2026. This book-external derivation connects the previously
conditional logarithmic comparison metric to a specified projective SNC
model. It explains which model input suffices; it does not certify that
input for every meromorphic degeneration or prove its semistable reduction.
No independent model-verifier receipt has been obtained.

## Exact model input

Let \(\mathcal X_0\to D\) be a projective model of a smooth polarized
family \((X,L)\) over \(D^*\). Suppose \(A_0\) is relatively ample and
\(A_0|_{D^*}\simeq L^{k_0}\), with \(k_0>0\). Supply a modification
\(f:\mathcal X\to\mathcal X_0\), isomorphic over \(D^*\), obtained by
a **specified finite sequence of blowups with coherent centres over zero**.
Assume the final total space \(\mathcal X\) is smooth and its central
divisor has SNC support. Its multiplicities \(b_i\) may exceed one.
These are hypotheses on the supplied model; choosing an arbitrary
resolution is not a proof that it has this particular presentation.

The elementary relative-ampleness arguments below can be applied to the
scheme model over \(\operatorname{Spec}\mathbb C\{t\}\) and then its
projective analytic germ, or to analytic models with the projective-germ
algebraization interface already used in Chapter 59. The Stacks Project
locators are scheme statements. They do not directly assert the analogous
result for an arbitrary proper nonprojective complex space.

## A vertical relatively ample divisor

For one blowup \(g:\mathcal Y\to\mathcal Z\) with centre ideal
\(\mathfrak j\), its tautological sheaf satisfies

\[
 \mathfrak j\mathcal O_{\mathcal Y}=\mathcal O_{\mathcal Y}(-E)
          =\mathcal O_{\mathcal Y}(1),
\]

where \(E\) is the effective Cartier exceptional divisor. The first
identification and sign are Stacks, Section 31.33, Lemma 31.33.4;
the finite-type projectivity and relative ampleness are Lemma 31.33.13.
Both locators were freshly checked in the cached primary page for Tag
[01OF](https://stacks.math.columbia.edu/tag/01OF). Since the centre is
vertical, \(E\) is vertical. The minus sign is essential.

Induct through the given finite sequence. If \(G_{\mathcal Y}\) is
relatively ample for the preceding composite \(\mathcal Y\to\mathcal X_0\)
and \(-E_g\) is relatively ample for the next blowup \(g\), then

\[
 G_{\rm next}=-E_g+a g^*G_{\mathcal Y}
\]

is relatively ample over \(\mathcal X_0\) for a sufficiently large integer
\(a\). This is Stacks Tag [0C4K](https://stacks.math.columbia.edu/tag/0C4K),
Lemma 29.38.8, whose quasi-compact-base hypothesis holds on the scheme
germ. Its proof uses Tag [0892](https://stacks.math.columbia.edu/tag/0892),
Lemma 29.38.7. All these divisors are vertical. This gives a vertical
Cartier divisor \(G\) on \(\mathcal X\) with \(\mathcal O(G)\)
\(f\)-ample. If the modification is the identity, take \(G=0\).

Apply the composition rule once more to \(\mathcal X\to\mathcal X_0\to D\).
For a sufficiently large integer \(a>0\),

\[
 B=f^*A_0^a\otimes\mathcal O(G)
\]

is relatively ample over the base germ, and
\(B|_{D^*}\simeq L^r\), \(r=ak_0\), using the canonical trivialization
of the vertical divisor away from zero. A power \(B^q\) is relatively
very ample. On a smaller disc choose finitely many relative sections and
a closed immersion \((j,\pi):\mathcal X\hookrightarrow\mathbf P^P\times D\)
with \(B^q=j^*\mathcal O(1)\). These are the ordinary projective-germ
relative-generation/very-ampleness inputs; the scope is the given finite
projective model, not a uniform choice over every model.

## The positive reference and its relation to the original reference

The metric on \(B\) obtained as the \(q\)-th root of the FS metric gives
a root metric \(h_+\) on \(L\) over the punctured family. Its curvature is

\[
 \theta_+=\frac1{qr}j^*\omega_{\rm FS}.
\]

The closed form
\(\Omega_+=\theta_++i\,dt\wedge d\bar t\) is Kähler on the smooth
total space: the pair \((j,\pi)\) is an immersion. On every smooth fibre,
\(\Omega_+|_{X_t}=\theta_+|_{X_t}\). Therefore the model-uniform
positivity input of the preceding comparison-metric candidate holds
with constant one, interpreted using the rational extension \(B^{1/r}\).
The proof of that candidate uses only its smooth curvature form and
the fixed divisor metrics; it does not require this rational line bundle
to be an integral line bundle on the total space.

For the change of reference, suppose also that a supplied integral
extension \(\mathcal L\) of \(L\) carries a smooth Hermitian metric
\(h_0\). Fix the punctured-family identification of \(B\) with \(L^r\)
meromorphically. On the smooth total space its ratio to
\(\mathcal L^r\) is \(\mathcal O(D_v)\) for a vertical Cartier divisor
\(D_v=\sum d_iE_i\). This meromorphic identification is a hypothesis;
a holomorphic identification on \(D^*\) with an essential singularity
at zero would not justify a vertical-divisor formula.

Choose smooth divisor metrics and write \(\rho_i=|\sigma_i|^2\).
On the compact model region there are uniform upper bounds on all
\(\rho_i\). The divisor of \(t\) gives

\[
 \sum_i b_i\log\rho_i=2\log|t|+O(1)=-2T+O(1).
\]

Hence each \(\log\rho_i\) is bounded above, and is bounded below by
\(-2T/b_i-C\). Ratios of the remaining smooth metrics are bounded.
It follows that, under the fixed identification on the punctured family,

\[
 h_+=h_0e^{-2\chi_t},\qquad
 \|\chi_t\|_{C^0(X_t)}\leq C(T+1).                         \tag{1}
\]

More explicitly, choose the metric on \(\mathcal O(D_v)\) induced by
the divisor metrics. Then the ratio is a bounded smooth positive factor
times \(\prod_i\rho_i^{d_i}\), before taking the \(r\)-th root.
Thus \(\chi_t=-(2r)^{-1}\sum_i d_i\log\rho_i+O(1)\).
The sign is fixed by \(h_+=h_0e^{-2\chi_t}\); the bound is independent
of that sign. Equation (1) uses a fixed meromorphic identification,
not freedom to multiply it by an arbitrary nonmeromorphic scalar.

If a metric on \(L|_{X_t}\) is \(h_0e^{-2\varphi_{0,t}}\), write it as
\(h_+e^{-2\varphi_{+,t}}\), where
\(\varphi_{+,t}=\varphi_{0,t}-\chi_t\). Its curvature is unchanged.
An \(O(T)\) oscillation bound on \(\varphi_{0,t}\) transfers to an
\(O(T)\) oscillation bound on \(\varphi_{+,t}\). Subtracting its supremum
then supplies the normalization used by the energy argument.
This is also the reference compatible with the separate Bergman
reconstruction, with \(k=qr\).

## SNC multiplicities and the logarithmic comparison

The earlier scalar-profile proof was written for reduced SNC models.
For the present model the local equation is
\(t=\prod_{i=0}^m z_i^{b_i}\). Put
\(x_i=-T^{-1}\log|z_i|\), so

\[
 x_i\geq\delta\ (0\leq i\leq m),
 \qquad \sum_{i=0}^m b_ix_i=1,
 \qquad 0<\delta<\Big(\sum_{i=0}^m b_i\Big)^{-1}.          \tag{2}
\]

Only \(z_1,\ldots,z_m\) are independent logarithmic directions on a
smooth fibre. They, with the transverse coordinates, are local coordinates
there; \(\partial t/\partial z_0\ne0\) off the central divisor.
No single-valued choice of \(z_0\) on an entire torus is required for
the tensor inequality. If \(m\geq1\), (2) implies
\(\delta\leq x_j\leq1-\delta\) for every \(j\): use \(b_j\geq1\)
and at least one other positive term in the weighted sum.

With the same global profiles
\(q_{i,t}=\int_0^1\log(\rho_i+|t|^{2a})\,da\), the identities
\(0<F'_T<1\), \(F''_T=(p_1-p_0)/(2T)\), and their uniform Hessian
lower bound therefore apply unchanged. The smooth \(O(1)\) divisor
metric factors put \(-\log\rho_j/(2T)\) in
\([\delta/2,1-\delta/2]\) for large \(T\). Choosing a sufficiently
small fixed \(\epsilon>0\), the global Kähler form

\[
 \beta_t=\theta_+|_{X_t}
       +\epsilon i\partial\bar\partial\sum_iq_{i,t}|_{X_t}
\]

lies in \([\theta_+|_{X_t}]\), has comparison-potential oscillation \(O(T)\),
and on each fixed logarithmic interior satisfies

\[
 \beta_t\geq C_\delta^{-1}\left(
  T^{-1}\sum_{j=1}^m i\,d\log z_j\wedge d\overline{\log z_j}
  +\sum_{j=m+1}^n i\,dz_j\wedge d\bar z_j\right).           \tag{3}
\]

The globally positive background controls the smooth negative divisor
curvature terms. The positive scalar Hessian controls the logarithmic
terms, exactly as in the prior proof. For \(m=0\) there are no such
terms, and background positivity already gives (3).
The integration-by-parts argument for smooth background-psh potentials
with \(O(T)\) oscillation gives the same \(O(T)\) energy bound, using
the same unscaled class and constant fibre volume. With the convention
\(\theta_+=i\Theta_{h_+}\), the class is \(2\pi c_1(L|_{X_t})\);
dividing all curvature forms consistently by \(2\pi\) gives the normalized
\(c_1\) convention. Fixed factors two between curvature and norm-potential
conventions must also be retained.

## What is and is not removed

For the **supplied blowup model** and meromorphic polarization
identifications above, uniform positive reference geometry is constructed
by changing the extension through a vertical rational divisor. It is not
asserted for the unmodified pullback of the original ample bundle.
The earlier dossier, source manifest and finite scalar calculations remain
unchanged historical checkpoints; their hypotheses are not rewritten.

Applying this to an arbitrary degeneration still requires a source-checked
projective meromorphic model, an appropriate SNC modification/base change,
the meromorphic volume form, and the relevant initial oscillation/Skoda
inputs. A nonprojective family, nonmeromorphic reference identification,
or a purported SNC resolution without the specified model input is outside
this derivation. The remaining chamber geometry and hybrid approximation
steps are independent gates. No theorem is inserted into the active book,
no open-problem status is changed, and no novel priority claim is made.
