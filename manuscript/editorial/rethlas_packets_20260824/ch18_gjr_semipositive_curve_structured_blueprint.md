# proposition prop:gjr-residue-package

<!-- rethlas-depends-on: -->
## statement

Let (K) be complete and nontrivially valued, let (X) be a good strict
(K)-analytic space, let (x\in X), and let
(\Lambda\subset\mathbf R) be (\mathbf Z) or a divisible additive
subgroup.  The following hold.

1. Every (\Lambda)-PL germ has, after shrinking, a finite expression
   (h=\sum_i\lambda_i h_i) with (\lambda_i\in\Lambda) and integral PL
   functions (h_i).
2. Residues are linear, and finitely many integral PL germs have residue
   line bundles represented on one common integral model (V) of
   (\operatorname{red}(X,x)), with
   (\dim V=\operatorname{trdeg}_{\widetilde K}
   \widetilde{\mathscr H(x)}).
3. A PL germ is semipositive at (x) precisely when its residue class is
   nef, and harmonic precisely when its residue class is numerically
   trivial.  The semipositivity and harmonicity loci of a fixed PL function
   are open.
4. If (V) is integral of dimension at most one, then nefness is vacuous
   unless (V) is a proper curve; on a proper integral curve it is
   equivalent to nonnegative degree, while numerical triviality is
   equivalent to degree zero.

## proof

Item 1 is exactly Gubler--Jell--Rabinoff Proposition 5.8.  For divisible
(\Lambda), its proof chooses a finite (\mathbf Q)-linearly independent
coefficient set, compares the integral pieces on a finite analytic cover,
and glues them after shrinking.  For (\Lambda=\mathbf Z) it is immediate.

Linearity in item 2 is Gubler--Jell--Rabinoff Lemma 6.18.  The model system
of Sections 6.2--6.6 is filtered, so a finite family is pulled back to one
common model.  By the definition of a model of the reduction of a germ, its
function field is (\widetilde{\mathscr H(x)}) over (\widetilde K), which
gives the dimension formula.  Functoriality of residues under pullback makes
the representing line bundles compatible on the common model.

Item 3 is Gubler--Jell--Rabinoff Proposition 7.1 and Remark 7.3(4).
Proposition 7.1 proves both directions: a nef formal model restricts to a
nef residue, and a nef residue is spread, after formal blowup and shrinking,
to a nef formal model.  Applying the assertion to both a line bundle and its
dual gives the numerical-triviality characterization.  The same spreading
argument gives openness.

For item 4, nefness in the source is tested by degrees on integral proper
closed curves.  An integral scheme of dimension zero, or a nonproper
integral curve, contains no such one-dimensional closed subscheme.  If
(V) is a proper integral curve, its only integral closed curve of
dimension one is (V), so the single test is (\deg L\geq0); testing both
(L) and (-L) gives degree zero.

The audited source is arXiv:2111.05741v3, SHA-256
`572d51c9f8907dbb814684f7d136612243c0e0b70cddbe6759bb686f0bcfbd42`,
printed pages 33 and 43--46.  Immediately before Proposition 7.5 the source
states that the semipositive analogue is unknown.  Remark 7.3(5) makes the
positive-coefficient formulation necessary because semipositive germs form
a monoid rather than a group.

# theorem thm:ch18-semipositive-integral-residual-curve

<!-- rethlas-depends-on: prop:gjr-residue-package -->
## statement

\begin{theorem}\label{thm:ch18-semipositive-integral-residual-curve}
Let $K$ be a complete nontrivially valued non-Archimedean field, let $X$ be
a good strict $K$-analytic space, and let $x\in X$ satisfy
\[
 \operatorname{trdeg}_{\widetilde K}\widetilde{\mathscr H(x)}\leq1.
\]
Let
$\Lambda\subset\mathbf R$ be either $\mathbf Z$ or a divisible additive
subgroup.  If a $\Lambda$-PL function $h$ is semipositive at $x$, then there
are a strict analytic neighbourhood $W$ of $x$, finitely many coefficients
$a_j\in\Lambda_{\geq0}$, and integral PL functions $g_j$ on $W$, each
semipositive at every point of $W$, such that
\[
                         h|_W=\sum_j a_jg_j.
\]
All but at most one of the $g_j$ may be chosen integral harmonic.  The
statement allows boundary points and requires neither algebraic closedness
of $K$ nor any hypothesis relating $\Lambda$ to the value group of $K$.
In particular, it applies at every point of a good strict analytic curve.
\end{theorem}

## proof

\begin{proof}
If $\Lambda=\mathbf Z$, openness of the semipositivity locus lets us shrink
around $x$ until $h$ is semipositive on one strict analytic neighbourhood;
then the one-term decomposition $h=1\cdot h$ has all the asserted
properties.  We may therefore suppose that $\Lambda$ is divisible.

By \texttt{prop:gjr-residue-package}, after shrinking to $U$ we can write
\[
                         h=\sum_{i=1}^m\lambda_i h_i,
 \qquad \lambda_i\in\Lambda,quad h_i\in\operatorname{PL}_{\mathbf Z}(U),
\]
and represent all residue classes $L_{h_i}(x)$ by line bundles $L_i$ on one
integral model $V$ of $\operatorname{red}(X,x)$.  The hypothesis gives
$\dim V\leq1$, and linearity gives
\[
                         L_h(x)=\sum_{i=1}^m\lambda_iL_i.
\]

Suppose first that $\dim V=0$, or that $\dim V=1$ and $V$ is not proper.
The nef tests are vacuous, so every $L_i$ and its dual are nef and every
$h_i$ is harmonic at $x$.  Writing
\[
          \lambda_i=\lambda_i^+-\lambda_i^-,\qquad
          \lambda_i^+=\max\{\lambda_i,0\},\quad
          \lambda_i^-=\max\{-\lambda_i,0\},
\]
expresses $h$ as a positive $\Lambda$-linear combination of the integral
harmonic functions $h_i$ and $-h_i$.

Now suppose that $V$ is a proper integral curve.  Put
\[
                 d_i=\deg L_i\in\mathbf Z,qquad
                 d=(d_1,\ldots,d_m),\qquad
                 D=d\cdot\lambda=\deg L_h(x)\geq0.
\]
If $d=0$, all $h_i$ are harmonic and the preceding argument applies.  If
$d\ne0$, let
\[
                 \delta=\gcd(d_1,\ldots,d_m)>0,
                 \qquad \ell=\delta^{-1}d:\mathbf Z^m\to\mathbf Z.
\]
This homomorphism is primitive.  B\'ezout gives $u\in\mathbf Z^m$ with
$\ell(u)=1$, and choose a $\mathbf Z$-basis
$v_1,\ldots,v_{m-1}$ of $\ker\ell$.  Since
$\mathbf Z^m=\mathbf Zu\oplus\ker\ell$, the same integral change of basis
over $\Lambda$ gives
\[
            \lambda=t u+\sum_{j=1}^{m-1}c_jv_j,
            \qquad
            t=\ell(\lambda)=D/\delta\in\Lambda_{\geq0},
            \quad c_j\in\Lambda.
\]
Define integral PL functions
\[
                    q=\sum_i u_i h_i,
             \qquad r_j=\sum_i(v_j)_i h_i.
\]
Their residue degrees are
\[
              \deg L_q(x)=d\cdot u=\delta>0,
              \qquad \deg L_{r_j}(x)=d\cdot v_j=0.
\]
Thus $q$ is semipositive at $x$ and each $r_j$ and $-r_j$ is harmonic
there.  Consequently
\[
 h=tq+\sum_j c_j^+r_j+\sum_j c_j^-(-r_j),
 \qquad
 c_j^+=\max\{c_j,0\},\quad c_j^-=\max\{-c_j,0\},
\]
is the required positive-coefficient germ decomposition, with at most the
$q$ term nonharmonic.

The semipositivity and harmonicity loci of these finitely many PL functions
are open.  Intersecting them with $U$ produces one strict analytic
neighbourhood $W$ on which every summand has the asserted property, and the
identity persists after restriction.
\end{proof}
