# Finite constraint matrices: research repair candidate

Date: 4 October 2026. This is a book-external proof candidate addressing
the finite-family step in Yang Li, arXiv:2505.11087v1, Corollary 3.17.
It is an elementary determinant argument, without a novelty claim. It
does not certify the paper's principal theorem or change a book problem
status. No independent model-verifier receipt has been obtained.

## Precise algebraic setting

Let \(q\geq d\geq1\), and let \(A(t)\) be a fixed \(q\times d\) matrix
of convergent meromorphic germs at zero, with rank \(d\) over their
fraction field. We shrink a
punctured disc once so that all nonzero maximal minors are invertible
there. Its rows are denoted \(A_j(t)\). Given any real weights
\(\mu_1,\ldots,\mu_q\), consider

\[
 |A_j(t)x|\leq C_0|t|^{\mu_j},\qquad 1\leq j\leq q.
\]

The input matrix and positive constant \(C_0\) are fixed; the weights,
evaluation point and complex linear evaluation functional may vary.
There is a finite family of convergent meromorphic vector germs,
depending only on \(A\), that supplies the following replacement.
If \(x'\in\mathbf C^d\) satisfies the constraints at
\(0<|t'|\leq r_0\), and \(\ell\) is any complex linear functional, one can find a
member \(v\) of the fixed family, a real number \(\nu\), and a scalar
\(c\) with \(|c|\leq dC_0\), such that

\[
 |t'|^\nu\ell(cv(t'))=\ell(x'),\qquad
 |A_j(t)cv(t)|\leq C_1|t|^{\mu_j-\nu}
 \quad(0<|t|\leq r_0).
\]

Here \(r_0>0\) depends only on the matrix; \(C_1\) depends only on the
matrix and \(C_0\). Neither depends on \(\mu,t',\ell,x'\). The real
factor \(|t|^\nu\) is a comparison factor, not a meromorphic function;
the replacement vector \(cv(t)\) itself is meromorphic.

## Determinant proof

For each ordered increasing row set \(I\) of size \(d\) with nonzero
minor, put

\[
 D_I=\operatorname{ord}_0\det A_I,
 \qquad v_{I,i}(t)=A_I(t)^{-1}e_i\quad(i\in I).
\]

The coordinate vector \(e_i\) here occupies the position of row \(i\)
in the ordered matrix \(A_I\). These finitely many columns constitute
the required fixed family. Choose \(I\) minimizing

\[
 D_I-\sum_{i\in I}\mu_i.
\]

This is a minimum of finitely many real numbers, and uses vanishing
orders, rather than determinant magnitudes at the particular point
\(t'\). For each row \(j\), write

\[
 A_j(t)=\sum_{i\in I}b_{ji}(t)A_i(t),
 \qquad b_{ji}(t)=A_j(t)v_{I,i}(t).
\]

If \(b_{ji}\ne0\), Cramer's rule gives its order as
\(D_{I-i+j}-D_I\), with the row replacement interpreted up to sign.
The minimum property implies

\[
 \operatorname{ord}_0 b_{ji}+\mu_i-\mu_j\geq0.                 \tag{1}
\]

When a repeated replacement row produces a zero determinant, the
coefficient is zero and no order is needed. When \(j=i\), the
coefficient is one and the inequality is equality.

Every nonzero coefficient for every possible choice of \(I,j,i\) has
the form \(t^{a_{ji}}u_{ji}(t)\), with \(u_{ji}\) a holomorphic unit
near zero. There are only finitely many coefficients. Shrink \(r_0<1\)
so all their units are bounded by one common constant \(C_A\). From
(1), for the selected row set and all \(0<|t|\leq r_0\),

\[
 |b_{ji}(t)|\,|t|^{\mu_i-\mu_j}
 =|u_{ji}(t)|\,|t|^{a_{ji}+\mu_i-\mu_j}\leq C_A.             \tag{2}
\]

Write \(x'=\sum_{i\in I}y_i'v_{I,i}(t')\), with
\(y_i'=A_i(t')x'\). If \(\ell(x')\ne0\), the triangle inequality
and the input constraints give some \(i\in I\) with

\[
 |t'|^{\mu_i}|\ell(v_{I,i}(t'))|
 \geq \frac{|\ell(x')|}{dC_0}.
\]

Set

\[
 \nu=\mu_i,\qquad
 c=\frac{\ell(x')}{|t'|^{\mu_i}\ell(v_{I,i}(t'))}.
\]

Then \(|c|\leq dC_0\), the required evaluation agrees exactly, and
(2) proves every constraint with \(C_1=dC_0C_A\). If the prescribed
evaluation is zero, take \(c=0\). This proves the stated replacement
under the precise fixed-matrix hypotheses above.

## Relation to the source

For each fixed tensor degree, suppose the finitely many chamber bases
used in Section 3.4 have been supplied as convergent meromorphic bases.
Express all their coefficient functionals in one of those bases. These
give the rows of \(A(t)\). The matrix has full column rank because it
contains the coordinate functionals of that reference basis. Its inverse
minor columns correspond to a finite collection of meromorphic global
sections. They contain a basis, so they generate the section space on
every sufficiently small punctured fibre. For a globally generated tensor
power, their common zero locus is empty there.

Taking \(\ell\) to be section evaluation at the prescribed point gives
the finite-family conclusion needed in Corollary 3.17 directly. The
constants and radius may depend on the fixed tensor degree, as permitted
in the subsequent diagonal argument. This route does not use the
Section 3.3 multigraded quotients. In their printed common-basis case,
those quotients vanish in dimension at least two, as recorded in the
[primary-source audit](../li_canonical_basis_source_audit_20261004.md).

This proof candidate isolates the finite-matrix step. It does not supply
all other geometric or analytic dependencies of the main convergence
argument. In particular, convergent chamber bases, the global comparison
metric at the unresolved citation in Lemma 4.3, the correctly stated
uniform domination estimate, the Bergman estimate and the hybrid
approximation-to-measure argument need their own exact checks before a
repaired principal result could be admitted into the book.

## Check scope

The companion exact-symbolic calculation checks Cramer's coefficients
and their weighted orders for fixed matrices with poles, dependent rows
and determinant cancellation, over integer and rational weight choices.
It also checks the literal common-basis quotient collapse in finite
polynomial truncations. These finite calculations support the displayed
algebra; they are not a proof of the universal statement, an external
verifier verdict or certification of the Calabi–Yau convergence theorem.
