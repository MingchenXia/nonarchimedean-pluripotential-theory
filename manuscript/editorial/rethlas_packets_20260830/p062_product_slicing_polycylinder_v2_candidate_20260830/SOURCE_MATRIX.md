# Source and hypothesis matrix for v2

Date: 30 August 2026

This is a source ledger for a quarantined candidate, not a verification
receipt.

| Use in v2 | Primary source or exact dependency | Scope and closure |
|---|---|---|
| Local moment representation of an ordinary CLD-smooth fibre function | Chambert--Loir--Ducros (2025), Proposition 15.1.1 and Corollary 15.1.2 | Applied pointwise on the analytic fibre `Z_{H(x)}` using finitely many analytic units. |
| Analytic fibre over `H(x)`; density of `kappa_Y(y)` in `H_Y(y)` for a good total space | CLD, Sections 11.1.9--11.1.10 | The proof also gives the affinoid tensor-product argument identifying the fibre and ambient completed residue fields at `y`; strict approximation is made in the ambient local residue field, not in `kappa(x)`. |
| Local holomorphic/differential separation and compactly supported ambient partitions | CLD, Sections 15.2.2--15.2.4 and Corollary 15.2.9 | `Y_0=U_0 x Z` is good and separated. The compact closed fibre support is covered finitely; each partition term has compact support contained in its ambient moment neighbourhood. |
| Smooth cutoff and uniform approximation of a continuous function | CLD, Corollary 15.2.5 and Theorem 15.2.6 | Used after the extension step, only near the fixed compact support. |
| Compactly supported symmetric smooth form as a difference of compactly supported positive forms | CLD, Proposition 6.5.2(b) | Applied to `d'd'' Phi` to bound fibrewise total variation. |
| Smooth relative-top-degree fibre integration and its continuity | CLD, Theorem 16.3.3(d) | Product projection, relative dimension one, compact support over the base. |
| Projection/Fubini formula | CLD, Theorem 16.5.4 and Corollary 16.5.5 | Applied first to smooth multipliers and then passed to the continuous multiplier by the displayed uniform estimate. |
| Continuous functions inject into `(0,0)` currents | CLD, Corollary 7.3.12, with Theorem 16.4.4(b) | Base is a standard strict open polycylinder and hence in the stated very-rich scope. |
| Finite-flat trace and preservation of zero Hessian | Exact verified dependency `prop:p062-finite-flat-continuous-trace` | Used on the polynomial tube in the annulus proof. |
| Arbitrary-field strict-disc constancy | Exact verified dependency `prop:p062-arbitrary-field-disc` | Applied over `K` and over complete residue fields `H(x)`. |
| Rational-centred torus trace calculation | Exact verified dependency `prop:p062-rational-centred-traces` | Its zero-distributional-Hessian Gauss-trace conclusion is used in the annulus step. |
| Single Gauss fibre for a minimal polynomial, including inseparability | Exact verified proof of `prop:p062-arbitrary-field-disc` | Reused at `s=|T(y)|`, retaining the full initial degree. |
| Density of rigid points in strict affinoids | Berkovich, Proposition 2.1.15 | Used locally on strict open annuli. |
| Iterated multivariate Gauss point | Direct calculation in the v2 proof | Nested finite maxima commute for Laurent polynomials; Banach density extends equality to convergent Laurent series. The same approximation proves continuity of the canonical Gauss section. |
| Weight-one split-torus integration | Gubler--Jell--Rabinoff, Proposition 11.1 and Example 11.7; BGJKK, Proposition 2.3.6 for top-form support | Used over arbitrary complete nontrivially valued fields. |
| Weakly smooth zero-Hessian functions are harmonic | Gubler--Jell--Rabinoff, Proposition 10.17 | Invoked only after obtaining the explicit affine logarithmic formula. |

## No-use declarations

- No pullback or restriction of an arbitrary CLD current is asserted.
- No Galois descent of ordinary smooth forms is used.
- No rational-domain or coefficient-spreading lemma is used in v2.
- CLD fibre integration is not applied directly to the continuous
  coefficient `h`; it is applied to smooth approximants and passed to the
  limit with a positive-form total-variation bound.
- No density of `K`-rational points, separability, tameness,
  defectlessness, or algebraic closedness is assumed.
- The explicit Gauss calculation is made over every complete residue field,
  so no rigid-base-point reduction enters the iteration.

## Verification boundary

The gap-1 lemma has an independent mathematical audit in the memo identified
in the README. The assembled v2 bytes, the Gauss repair as integrated, and
all unchanged surrounding arguments still require a new independent
exact-byte hostile audit and a new production Rethlas run. The failed v1
response is not a verification receipt for unchanged v2 passages.
