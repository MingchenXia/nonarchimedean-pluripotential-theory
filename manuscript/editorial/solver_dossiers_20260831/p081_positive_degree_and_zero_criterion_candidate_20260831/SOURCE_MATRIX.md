# Source and hypothesis matrix for the replacement candidate

This is a source ledger, not mathematical acceptance. The statement and
proof remain subject to independent and production verification.

| Input | Exact source | Use and restriction |
| --- | --- | --- |
| CLD-psh to classical psh to Thuillier subharmonic | Gubler--Rabinoff 2506.13548v2, Sections 1.2 and 4.1.2 | Smooth strict curves over a complete nontrivially valued field; frames differ by harmonic logarithms. |
| Curvature mass and harmonicity | CLD v2, Theorem 18.1.6 and Corollary 18.1.7; Thuillier Theorem 3.4.12; GR classical Section 3.12 | Proper curve; residue-field degrees retained; the current criterion gives subharmonicity of both signs, hence harmonicity, not Q-model existence. |
| Lisse metric approximation | Thuillier, Theorem 3.4.19 and its proof | Global metrics on the same proper smooth curve; norm monotonicity gives uniform convergence only after using continuity and compactness. |
| Finite skeletal factorization and refinement | Thuillier, Proposition 3.2.4 and Lemma 2.2.22 | Used upstairs over an algebraically closed field. Type-III bends are explicitly moved to type II before claiming a strict formal model. |
| Finite graph transport and rational interpolation | Full elementary proofs in Steps 2 and 4 | These are deductions in this packet, not cited as an existing named result. Strictly positive total degree supplies the vertex margin. |
| Rational graph functions are model functions | GJKM, Definition 3.4 and Proposition 3.5(c) | A common denominator makes slopes integral; breakpoint lengths and values belong to the divisible value group. |
| Model positivity on a curve | GJKM, Proposition 3.7 | Reference curvature plus outgoing slopes is nonnegative; the upstairs residue weights are one. |
| Finite definition field and nef descent | GM, Propositions 2.10, 2.18(b), 3.5 and Lemma 3.3 | A representing model is first descended to a finite field; its nefness is reflected from the algebraically closed completion. |
| Finite-normal envelope identity | GJKM, Proposition 2.11 | Applied only to a finite normal extension, including its inseparable part, never directly to the completed algebraic closure. |
| Continuous envelope yields uniform model approximation | GJKM, Theorem 1.1 and Proposition 2.9(viii) | Used only when the underlying line bundle is ample, i.e. positive degree. No appeal to unrestricted nef model-existence in Theorem 3.1. |
| Algebraic/formal equality and ample refinement | GM, Theorem 1.1, Propositions 4.11 and 4.13 | Proper algebraic curve; a common dominating model precedes mixing nef and ample extensions of the same rational line bundle. |
| Zero-degree conditional criterion | GR PL Proposition 5.1; harmonic maximum principle; full Step 7 | One semipositive Q-formal metric is assumed. Uniform approximation follows by model constants, not by an existence theorem. |
| Numerical triviality | GM Section 4.8 divisorial degree formula | Uses the Cartier divisor of a nonzero topologically nilpotent constant, not a Cartier-special-fibre assumption. |

## Explicitly excluded dependencies

- The earlier thm:p081-curve-local-global statement and proof are not
  inputs to this replacement.
- A sheaf-theoretic real-PL function is not assumed to be a finite real
  linear combination of global vertical Q-model functions.
- Generic degree zero is not assumed to ensure nonemptiness of a fixed
  Q-model-psh cone.
- The strict-analytic algebraization transfer is separate; its source
  interfaces cannot repair an invalid metric-comparison premise.

## Source-version and geometric clarifications

The lettered locator Proposition 3.5(c) refers to GJKM arXiv:1712.00980v3.
Its identical published counterpart is Proposition 3.5(3), on page 2344.
This version difference changes no mathematical input.

Making the chosen reference model and model function simultaneously
determined on a strict semistable model uses semistable domination. The
needed statement is recalled explicitly in GJKM's proof of Proposition 3.7,
with reference to Bosch--Lutkebohmert (1985), Section 7. Thuillier 3.2.4
supplies the lisse factorization and 2.2.22 supplies insertion of the
additional type-II vertices. No conclusion of GJKM Theorem 3.1 is imported
by this geometric step.

The exact-current production receipt is now recorded separately in
../p081_corrected_curve_production_run_20260831/PRODUCTION_RECEIPT.md.
The original statement and proof bytes remain unchanged.
