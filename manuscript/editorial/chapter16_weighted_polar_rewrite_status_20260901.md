# Chapter 16 weighted and polar proof rewrite status

Date: 1 September 2026.
Live source comparison base: 6795dfd917d591b1ede108d8d9afe3b1a032bc29.
The 3478-page PDF contains this still-unrevised Chapter 16 material. It is not a complete mathematical correctness certificate.

## Identified repairs still required

- The statement of thm:ch16-barrier says rho<0 on U and that its nonpositive sublevel is compact. Literally that sublevel is all of U, which is not the intended general neighborhood assertion. The corrected formulation needs rho on a larger ordinary neighborhood, with a relatively compact negative sublevel and a compact slightly positive sublevel. The explicit rational-domain construction must also handle simultaneous zeros of its numerators.
- The regularity proof in lem:ch16-beta-properties incorrectly treats an integer positive-part power as having that many continuous derivatives. Its derivative formulas also keep the factor two at k=n, although beta_n has only its first summand and the derivative factor there is one.
- The weighted theorem's proof integrates across the support boundary while stating smoothness of V only on U. The repaired argument requires V on a neighborhood of the fixed compact support, and explicitly justifies the coefficient regularization before using any inequality.
- The first polar proof moves the approximating potential and the approximating measures together. A fixed-helper limit followed by monotone convergence is required; the recorded second proof points in that direction but still depends on the preceding barrier and weight arguments.
- The blanket statement that the continuous factors' approachability cannot be removed is a limit of the old proof, not a consequence of the open hierarchy-collapse question. The new full-CPsh energy proof uses separate-variable sheaf closure and needs no such collapse. It still retains approachability and canonical local integrability for the auxiliary singular polar potential.

## Prepared replacement material

The full-CPsh research dossier supplies the energy calculus, exact weighted estimate, compact analytic barriers and polar proof, independently mathematically reviewed. Its actual Rethlas mathematical report is positive, but the two production acceptance audits disclose execution-compliance exceptions; these reports are not clean promotion gates.

A separate real-parameter draft replaces coefficientwise C^2 approximation by structured regularization of F(t)=max(-t,0)^(k+a) and its first derivative. It proposes the weighted estimate for every real a>1 while retaining the original a=3 application. Its frozen independent audit passes the new argument relative to the explicitly disclosed, separately reviewed energy input, with no required correction. The exact audit has SHA256 aec075ad91e84b6eee5dddea5ec795e4d3becd89435e2a6cecc7e47676719012 and is preserved in p213_weight_parameter_extension_independent_audit_20260901. This is a separate unpromoted mathematical claim, not part of the earlier submitted packet; dependency-closed production verification remains required.

Complete Chapter 14 component-curvature LaTeX and a separate full-CPsh component corollary are preserved as unpromoted insertion candidates. A full Chapter 16 replacement is being drafted in scratch. Existing labels and eqref uses are to be preserved where their mathematical meaning survives; any changed scope must be made explicit.

No corrected proof is silently substituted into a frozen verification record. No new theorem or problem retirement is authorized by this status note. The live Chapter 16 repair will require its own exact-source review and a correctly authorized verification path before promotion.
