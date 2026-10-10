# Convergent approximation of formal chamber bases — 4 October 2026

This elementary transfer argument continues the fixed-matrix repair of
arXiv:2505.11087v1. It remains outside the active manuscript and claims no
novelty, model-verifier receipt or principal Calabi–Yau theorem. The source
uses formal bases in Proposition 3.7 and then says they can be chosen
convergent in Section 3.4. The argument below makes that second step
explicit. Formal basis existence and the source's uniform chamber
decomposition remain separately identified geometric inputs.

## Algebraic and valuative hypotheses

Put F=Frac(C{t}), the field of convergent meromorphic germs at zero, and
K=C((t)), its t-adic completion, with ord(t)=1. Let V_F have finite
dimension d≥1, let e₁,…,e_d be an F-basis, and put V_K=V_F⊗_F K.
For x in a nonempty compact parameter set Σ, suppose γ_x is a real-valued
non-Archimedean valuation function on nonzero vectors of V_K:

\[
 \gamma_x(av)=\operatorname{ord}(a)+\gamma_x(v),\quad
 \gamma_x(v+w)\ge\min\{\gamma_x(v),\gamma_x(w)\},\quad
 \gamma_x(0)=+\infty.
\]

Assume γ_x(v) is finite and continuous on Σ for every fixed v≠0. Let
O⊂Σ be nonempty, and let σ₁,…,σ_d be a K-basis orthogonal at
every x∈O, meaning

\[
 \gamma_x\!\left(\sum_j c_j\sigma_j\right)
 =\min_j\{\operatorname{ord}(c_j)+\gamma_x(\sigma_j)\}
 \quad(c_j\in K).
\]

Zero coefficients have order +∞. The compactness condition can equivalently
be replaced by the explicit uniform bounds used in the next paragraph;
no lower bound for γ_x(σ_j) is needed for the truncation argument.

## Uniform finite truncation

Write σ_j=∑_i a_{ij}e_i with a_{ij}∈K. Define the finite constants

\[
 m_e=\min_{x\in\Sigma,i}\gamma_x(e_i),\qquad
 M_\sigma=\max_{x\in\Sigma,j}\gamma_x(\sigma_j).
\]

Choose an integer N>M_σ−m_e. Each a_{ij} has only finitely many negative
powers. Keep all its coefficients of exponents less than N and denote the
resulting Laurent polynomial by a^{<N}_{ij}. It belongs to F. Put
s_j=∑_i a^{<N}_{ij}e_i∈V_F and r_j=s_j−σ_j. Since every coefficient of
r_j in the e-basis has order at least N, for all x∈Σ one has

\[
 \gamma_x(r_j)\ge N+\min_i\gamma_x(e_i)
 \ge N+m_e>M_\sigma\ge\gamma_x(\sigma_j).
\]

If r_j=0 this inequality uses γ_x(0)=+∞. The ultrametric inequality then
gives γ_x(s_j)=γ_x(σ_j).

Fix x∈O and coefficients c_j∈K, not all zero, and set
m=min_j(ord(c_j)+γ_x(σ_j)). Orthogonality gives
γ_x(∑c_jσ_j)=m. The preceding uniform gap, say
ε=N+m_e−M_σ>0, gives

\[
 \gamma_x\!\left(\sum_j c_jr_j\right)
 \ge\min_j\{\operatorname{ord}(c_j)+\gamma_x(r_j)\}
 \ge m+\varepsilon.
\]

For vectors of unequal valuation, the valuation of their sum equals the
smaller one: applying the ultrametric inequality also to the difference
proves this familiar equality. Consequently

\[
 \gamma_x\!\left(\sum_j c_js_j\right)
 =m=\min_j\{\operatorname{ord}(c_j)+\gamma_x(s_j)\}.
\]

Thus the convergent s_j preserve orthogonality simultaneously on all of O.
In particular they are K-linearly independent, so their Laurent-polynomial
coefficient matrix has nonzero determinant. It is invertible over F as
well. A nonzero convergent meromorphic determinant is t^q times a
holomorphic unit on a sufficiently small disc. Hence, after one shrinking,
the matrix is invertible on every punctured fibre, and its inverse entries
are convergent meromorphic germs. There is no evaluation of a divergent
formal power series at a complex t in this argument.

## Finite chambers and the geometric input

Apply the construction separately to finitely many formal chamber bases
σ^{(k)}. Their truncation orders may differ; the minimum of their finitely
many positive convergence and invertibility radii is positive. The
resulting bases all converge and remain valuatively independent on their
respective chambers. The transitions between them are finite matrices over
F. Their coefficient functionals therefore satisfy the hypotheses of the
[fixed-matrix repair](li_finite_constraints_repair_20261004.md).
The inverse-minor columns then produce the finite family of sections needed
for the evaluation replacement, without the collapsed multigraded
quotients of the printed Section 3.3.

In the intended geometry, V_K is a fixed tensor-degree section space.
The convergent reference basis e_i comes from the meromorphic analytic
family and its section module. A continuous model metric gives
γ_x(s)=−log∥s(x)∥ on the compact skeleton, in the ord(t)=1 convention.
For nonzero sections and skeletal valuations of full support, this norm
is positive and finite; continuity and compactness give the displayed
bounds. These are the properties actually needed here. They should be
checked for the chosen family and section-module identification; generic
ampleness alone is not a substitute for every model positivity assumption
elsewhere in the convergence proof.

The transfer applies at each fixed tensor degree. It does not give one
truncation order or one punctured-disc radius simultaneously for all tensor
degrees. The subsequent Bergman/diagonal estimates must retain the permitted
dependence on degree and the order of their limits.

## What is and is not supplied

The fresh source rereading covers Section 3.1–3.2, Proposition 3.7, its
leading-term characterization and Section 3.4. Given the formal orthogonal
bases, the convergent transfer is fully proved above and uses no new
primary analytic theorem. Proposition 3.7's formal cancellation argument
can be checked at a rational interior valuation: its value group is
discrete, so a strictly increasing sequence of residual leading values
tends to infinity; powers used to cancel against a finite orthogonal
collection then tend to infinity as well. Completeness supplies the
coefficient limits. This explains the role of a rational point and
completeness in that argument, conditional on the source's common
leading-monomial chamber characterization. It does not independently
certify the source's geometric uniform-Lipschitz input and all its proof
dependencies.

No new formal theorem is inserted in the book. The analytic convergence
of the chamber bases is therefore reduced to the stated finite-dimensional,
compact-norm and formal-basis inputs; it is not retained as an unexplained
evaluation of formal series. Global comparison geometry, the Bergman
estimate and hybrid uniform approximation still need their own checks.
