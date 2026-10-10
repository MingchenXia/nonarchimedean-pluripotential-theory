# Section supnorms under complete field extension: exact asymptotic scope

Date: 9 October 2026. Controlling source: Boucksom--Eriksson, *Spaces
of norms, determinant of cohomology and Fekete points in non-Archimedean
geometry*, published in Advances in Mathematics 378 (2021), 107501.
The cached Chalmers PDF has 125 physical pages, including its cover.
This checkpoint actually reads physical pages 20--24 and 55--60, eleven
pages in six individually displayed matching views with full text and
sequential notes. Pages 22--23 overlap the preceding 29-page checkpoint:
only nine are new distinct pages, giving 38 distinct pages across those
two checkpoints, with 87 not read in that combined scope. This is not
a whole-paper claim. Acquisition or view preparation gives zero reading credit.

## The precise global estimate

Section 6 assumes a projective scheme over a complete valued field and a
line bundle. Theorem 6.6, physical pages 59--60, assumes geometric
reducedness and a continuous metric. For an arbitrary complete field
extension $F/K$, the section supnorms satisfy

$$
d_\infty\!\left(\|\cdot\|_{m\phi_F},
                 (\|\cdot\|_{m\phi})_F\right)=o(m).
$$

For a model metric, or an Archimedean field, the error is $O(1)$.
Neither ampleness nor pshness is assumed for this norm estimate.
The constants are for the fixed source data; uniformity over varying
metrics or field extensions is not supplied by this statement.

Lemma 6.1 preserves the norm on the original $K$-sections but gives
only $\|\cdot\|_{\phi_F}\le (\|\cdot\|_\phi)_F$ on the full extended
section space. Lemma 6.2's exact equality for every bounded metric is
equivalent to tameness in the finite Galois, nontrivially discretely
valued setting. Its external Galois-norm and spectral-norm sources are
attributed and not recursively certified here. Neither lemma licenses
exact equality for all extensions and all section norms.

For model metrics, Theorem 6.4 takes a finite model map with reduced
special fibre. A coherent quotient supported on that fibre is killed by
one scalar, giving a multiplicative norm comparison constant independent
of tensor power. Theorem 6.5 extends this to a finite family on a common
model and $r$-fold products, with bound $C^r$. The denominator-remainder
step in Theorem 6.6 uses this finite-family bound, or the same quotient
argument, for $q\mathcal L+r\mathcal M$. A fixed finite number of small
or zero-exponent cases is handled separately. Lemma 1.29(iv), physical
pages 23--24, is the actual lattice scalar-extension statement.

For continuous metrics over a nontrivially valued field, uniform model
approximation gives $C_\varepsilon+2m\varepsilon$. Dividing by $m$ gives
$\limsup E_m/m\le 2\varepsilon$; letting $\varepsilon$ tend to zero
proves the claimed sublinear limit. The printed intermediate bound
$\le\varepsilon$ misses a factor two, without invalidating that conclusion.
No uniform rate follows without controlling $C_\varepsilon$.

For trivially valued fields, Lemma 1.26 chooses a Laurent-series extension
whose valuation step avoids the countable rational span of weight
differences. A common further extension and the isometry in Proposition
1.25 complete the argument. This is a countable family of finite-dimensional
norms, not an assertion about a dense subfield of every complete field.

## The printed uniqueness condition and an exact diagnostic

Proposition 1.25(v), physical page 21, prints the same index in the ratio
$\|e_i\|/\|e_i\|$. Its proof on pages 21--22 uses different basis weights.
The intended condition is

$$
\{\|e_i\|/\|e_j\|:1\le i,j\le N\}\cap |F^\times|=\{1\},
\qquad \widetilde F=\widetilde K.
$$

The literal same-index condition is tautological and insufficient.
Take $K=\mathbf Q$ with trivial absolute value and $F=\mathbf Q((t))$
with $|t|=1/2$. On $K e_1\oplus K e_2$ use weights $1/2,1$.
The maximal extension has norm

$$
\|a e_1+b e_2\|_F=\max\{\tfrac12|a|,|b|\}.
$$

Use instead the basis $u=e_1-t e_2,e_2$ with weights $1/4,1$:

$$
\|a e_1+b e_2\|'=\max\{\tfrac14|a|,|ta+b|\}.
$$

For $a,b\in\mathbf Q$, if $b\ne0$ then $|ta+b|=1$; if $b=0$ and
$a\ne0$, then $|ta|=1/2$. Both norms thus restrict to the original
$K$-norm. On $e_1-t e_2$ their values are $1/2$ and $1/4$.
The residue fields are equal. The corrected pairwise condition fails
because $\|e_1\|/\|e_2\|=|t|$; this example does not refute that condition
or Lemma 1.26's intended proof.

## Other exact boundaries and printed slips

The finite extension $A=\mathbf Q[t][tx,x^2,x^3]\subset
A'=\mathbf Q[t][x]$ illustrates the product loss in Theorem 6.5.
The quotient is killed by $t$, whereas on $r$ tensor factors the monomial
$x_1\cdots x_r$ requires $t^r$ to enter the smaller tensor algebra.
Thus $t^{r-1}$ does not annihilate that quotient. This is a finite affine
algebra illustration, not a new global reduced-fibre theorem.

On $\operatorname{Spec} K[z]/(z^2)$ the nonzero section $z$ has zero
analytic sup-seminorm. Reducedness is needed to use norms and logarithmic
norm distance on the whole section space. This is outside Theorem 6.6.

Local printed clarifications: Lemma 6.3's proof says (iv) for (iii);
the model-quotient annihilator line has a stray $K'$ where the established
extension is $F$; Theorem 6.5's intermediate tensor inclusion leaves an
$A'$ in its final factor, whereas multiplying all factors gives the
stated $a^r$ conclusion; Theorem 6.6 cites Lemma 1.28 for the lattice
extension actually in 1.29(iv). Example 1.30 has stray $L/F$ notation;
only its explicit equality of value groups is used here.

The full printed proofs and the ordinary source audit are distinct from
recursive certification of every earlier foundation. Norm diagonalization
and density, Shilov/reduced-fibre Theorems 4.19--4.20, A.6 coherence,
model existence/pullback and the external classical inputs retain their
separate source scopes. Theorem 8.12 logarithmic integrability is not
newly read in this checkpoint.

## Remaining local comparison interfaces

Theorem 6.6 accommodates nondiscrete complete field extensions for the
stated global section-norm problem. It does not prove affine lower-growth
regularization over a completed residue field, convert a lower coercive
bound to an upper majorant, or prove local weak-psh descent. The norm
psh theorem's projective/geometrically reduced/ample/continuous scope
remains as in L.97. General BJ22 critical homogeneous Siu/envelopes remain
OPEN and LPWZ density UNVERIFIED. No original general theorem or independent
model receipt is asserted. The 4,657-page book, core sources and native
catalogue/editor are unchanged during this primary-source checkpoint.
