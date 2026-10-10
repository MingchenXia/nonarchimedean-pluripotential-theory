# Formula rendering addendum to the frozen norm-dependency audit

Date: 9 October 2026. The source-only BE21 checkpoint of 8 October and
its archives remain frozen. Some backslash commands in its Markdown
formulas were damaged during file generation. This addendum supplies
readable notation for the same already audited statements; it adds no
source-reading credit and changes no theorem or problem status.

The controlling frozen file is
[Local_psh_norm_dependencies_source_review_20261008.md](Local_psh_norm_dependencies_source_review_20261008.md).
The source is still the exact published Boucksom–Eriksson 2021 PDF,
with the partial reading scope of 29 physical pages in fifteen views.
The record hashes, selected texts, images and receipts remain unchanged.

For a finite flat morphism $f:Y\to X$ of constant degree $d$, its finite
algebra above an analytic point $x$ decomposes as

$$
A_x=\prod_y A_y,\qquad
n_y=\dim_{\mathcal H(x)}A_y
=\operatorname{length}(A_y)[\mathcal H(y):\mathcal H(x)],
\qquad \sum_y n_y=d.
$$

The fibre measure is $\sum_y n_y\delta_y$. Artinian composition length is
intrinsic; notation involving a vector-space dimension over the residue
field must not presume a compatible coefficient-field embedding.

The determinant norm line and its section metric are

$$
N_f(L)=\det f_*L\otimes(\det f_*\mathcal O_Y)^{-1},
\qquad
\log|N_f(s)|_{N_f(\phi)}(x)
=\sum_{f(y)=x}n_y\log|s(y)|_\phi.
$$

Thus the additive section weight uses the **minus** logarithmic norm.
For the corresponding real weighted trace,

$$
N_f(f^*g)=dg,\qquad
\|N_f(u)-N_f(v)\|_\infty\leq d\|u-v\|_\infty.
$$

Over $K=\mathbf F_2((t))$, the elementary diagnostic algebra
$A=K[z]/((z^2-t)^2)$ has rank four, length two and residue degree two.
Its determinant norm of $z$ is $t^2$, and the corresponding valuation
identity is $2=4\cdot(1/2)$. This algebra is not geometrically reduced
and is not a counterexample within Proposition 8.22's scope.

For an intended ample base polarization, type the pullback norm as
$N_f(f^*L)\simeq L^{\otimes d}$. The multiplicity-weighted maximum
iteration has error
$M_k\leq(1-1/d)^kM_0$ for $d>1$; degree one is the identity.
This is the audited compact continuous global construction, with its
precise psh hypotheses retained.

The uniform approximation diagnostic on two reduced projective points is

$$
\phi_i=\bigl((-1)^i/i,-(-1)^i/i\bigr)\longrightarrow(0,0).
$$

Making the entire sequence $\phi_i+c_i$ decrease requires
$c_i-c_{i+1}\geq1/i+1/(i+1)$, whose required differences have divergent
sum. Choose a fast subsequence with uniform error at most $2^{-k}$ and
set $c_k=3\cdot2^{-k}$ instead. The identity

$$
c_k-c_{k+1}=2^{-k}+2^{-(k+1)}
$$

gives decreasing buffered approximants to the same limit. This repairs
that proof step; it does not refute the intended uniform-closure result
or supply a new general envelope theorem.

The frozen printed-slip table is read with the following symbols:
the pairing lists $L_2,\ldots,L_n$; the local curvature potential is
$f=\log|s|_\phi$ with the displayed minus sign retained; the determinant
line is $\lambda(L)=\det f_*L$; the norm iteration uses the base $L$
and source $f^*L$; the perturbation uses its chosen ample model $A$.

Proposition 8.22 remains an attributed result for a finite flat morphism
of projective geometrically reduced schemes, an ample rational source
line bundle and a continuous global psh metric. Theorem 7.31 retains
its continuous/semiample/geometrically reduced projective hypotheses.
This addendum does not broaden them to local weak-psh descent or
nondiscrete affine regularization. The active book and catalogue remain
unchanged, and general BJ22 critical homogeneous Siu/envelopes stay OPEN.
