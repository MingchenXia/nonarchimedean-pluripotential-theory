# Primary-source audit

All MP locators refer to arXiv:2409.06221v2, 18 September 2025, local text /private/tmp/mp24.txt; exact hash in INPUTS.json. The arXiv landing page and the published DOI https://doi.org/10.1016/j.aim.2025.110543 were checked for identity; mathematical locators are pinned to v2, not silently transferred to another version.

| Input | Exact locus read | Use and limitation |
| --- | --- | --- |
| Tropical spectrum and compactness | MP §1.2, Definition 1.3.1 and functoriality | Pointwise topology on all coherent ideals; compact Hausdorff space; pullback maps continuous. |
| Central variety | MP Lemma 2.1.1, Definition 2.1.2 | The coherent prime ideal maximal among ideals of positive value; actual centre can be positive-dimensional. |
| Proper-support semivaluations | MP Remark 2.1.3, decomposition (2.1.2) | They must not be identified with finite valuations on X. |
| Bimeromorphic lifting | MP Proposition 2.1.6, Remark 2.3.2 | The proposition is only a bijection on valuations. Our Step 1 separately proves existence on all semivaluations by closed image and density. Divisorial birational invariance is the needed source input. |
| Divisorial convention | MP Definition 2.3.1 | Rational nonnegative scalings, explicitly including the trivial valuation. |
| SNC monomial valuations | MP §2.3.1, Proposition 2.3.4, Remark 2.3.5 | Global ideal evaluation is independent of the chosen point of a connected stratum; rational weights give divisorial points. The new all-ideal domination inequality is proved here, not attributed to that remark. |
| Ordinary density | MP Theorem 2.3.6 and its §§2.4–2.6 strategy | Used only for lifting, not as an ordered-density assertion. The proof of ordinary density uses flag ideals and has no dependence on this new lemma or P14.2. |
| Normalization | MP §3.1.1, equation (3.1.1), Theorem 3.1.1 | Test-configuration simplex is sum b_i w_i=1. Its inverse-limit topology is not used to infer coordinatewise rational approximation. |
| Principalization | Standard analytic log resolution; MP Corollary 2.2.3 and Remark 2.5.2 use normalized blowups/resolution, citing Bierstone–Milman 1997 §13 | This remains an explicit external classical resolution input, not newly proved here. The primary Bierstone–Milman arXiv:alg-geom/9508005 identity and analytic scope were checked. No unverified theorem number for simultaneous principalization is invented. |
| MP positivity and comparison | MP Definition 4.3.1; Theorem 4.3.8 | MP potentials are usc; comparison against an arbitrary usc function is valid from divisorial inequalities. |
| Existing finite-energy correspondence | DXZ v3 Theorem 3.17; MP Theorems 5.1.4, 5.1.7 and §5.2; Chapter 71 theorem and normalization paragraph around (71.39)–(71.40) | Supplies an existing MP function agreeing divisorially with raw transform; the new step is equality at all semivaluations. This finite-energy input is not replaced by assuming all DXZ inverse-system objects have MP extensions. |
| Raw USC | Exact frozen P14.2 statement/proof, read in full | Conditional candidate input only, production pending; hashes in INPUTS.json. |

## Source precision observations

MP Example 2.1.4 contains a decreasing/increasing wording inconsistency in its displayed local-ideal limit; our proof does not use that reconstruction. We do not assume that every global semivaluation is a valuation on a local ring at a closed point.

MP Proposition 2.1.6 explicitly notes that subtraction of ideal values is legal because valuations there are finite. The new compactness lift avoids this subtraction entirely.

The SNC cone on a modification of X has unnormalized nonnegative weights. The normalized simplex lives on a modification of X×P¹. Conflating these is precisely the rounding error excluded in diagnostics.tex.

