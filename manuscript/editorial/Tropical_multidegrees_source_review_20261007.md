# Tropical multidegrees: source review, 7 October 2026

Positive tropical intersection support and Lorentzian coefficient inequalities need different hypotheses. Cid-Ruiz's new paper provides a common-facet positivity test for every positive cycle, a polymatroid support theorem under projection-purity and facet selection, counterexamples to the coefficient implication, and a positive Hodge theorem for augmented polymatroid fans. The proposed import preserves these distinctions and all factorial and weight conventions.

The primary source is Yairon Cid-Ruiz, *When are tropical multidegrees positive?*, [2608.25987v2](https://arxiv.org/abs/2608.25987v2), twenty-four pages. Its arXiv stamp is 28 August 2026; the internal PDF date is 31 August 2026. The complete paper was read as full selected text with twelve individually displayed matching page-pair images. Acquiring a PDF and preparing page images supplied no reading credit.

## Controlling editions and actual scope

| Source | Edition | Physical pages actually read | Scope |
|---|---|---|---|
| Cid-Ruiz | 2608.25987v2 | 1–24 of 24 | Whole paper |
| Xiang He | [2306.10589v2](https://arxiv.org/abs/2306.10589v2), 23 May 2024 | 1–11 of 11 | Whole paper |
| Allermann–Hampe–Rau | [1408.1537v2](https://arxiv.org/abs/1408.1537v2), 25 August 2015 | 3–5, 7–9 of 17 | Partial |
| Fulton–Sturmfels | [alg-geom/9403002v1](https://arxiv.org/abs/alg-geom/9403002v1), 1 March 1994 | 5–15 of 24 | Partial |
| Eur–Larson | [2301.00831v2](https://arxiv.org/abs/2301.00831v2), 30 August 2023 | 9–18, 20–21 of 27 | Partial |
| Eur–Huh–Larson | [2207.10605v3](https://arxiv.org/abs/2207.10605v3), 7 September 2023 | 41–46 of 58 | Partial |
| Ardila–Denham–Huh | [2004.13116v4](https://arxiv.org/abs/2004.13116v4), 14 February 2022 | 10–13, 51–69 of 73 | Partial; all of Section 5 |

Total actual reading: **93 distinct source/page pairs and 48 individually displayed matching images**, with complete selected text and sequential notes; two whole papers and five partial papers. The dependency reading first covered 63 pages in 33 images, followed by six additional ADH pages in three images. The later reading extends the earlier scope; earlier notes and preparation records remain unchanged. These are source readings, not a new whole-book rereading.

## Mathematical scope

- A positive tropical divisor must intersect every nonempty positive tropical curve positively. Positive facet weights alone do not meet this definition.
- Cid-Ruiz Theorem 3.5 requires **one common facet** satisfying every block-subset inequality. Independently maximizing each projection loses this requirement. Theorem 3.7 uses both projection-purity and facet selection; translation-admissibility is stronger and implies both via He Lemmas 2.11 and 3.1.
- Recession replacement is a bounded-rational-equivalence operation for the scalar top intersection. It does not replace the original cycle's facets in the common-facet test. AHR's translated-fan decomposition can have signed summands.
- The linear-space positivity proof uses a compatible smooth toric subtorus compactification and generated big nef divisors. A cone outside the subspace contributes zero by orbit disjointness. Bigness does not mean ampleness on every subdivision. In the algebraic image argument, first treat lower-dimensional image and zero pushforward; use a positive generic degree only in the equal-dimension case.
- The two-plane example has multidegrees (5,3,3,4) and polynomial (10t_1t_2+6t_1t_3+6t_2t_3+4t_3^2). Its Hessian has eigenvalues (-10,9\pm\sqrt{73}). Stable intersection uses absolute lattice indices, separately from oriented minor signs.
- The six-plane example changes weights while keeping the support of an irreducible tropicalization. It has multidegrees (5,4,5), polynomial (5s^2+8st+5t^2), and Hessian eigenvalues (18,2). Translation-admissibility and codimension-one connectedness therefore do not supply the missing Hodge property. The new weighted cycle is not the original irreducible tropicalization.
- For every caged integral polymatroid, unit-weight augmented Bergman fans have the projection support and Lefschetz certificate needed by Cid-Ruiz Theorem 5.4. The cone compatibility inequality in EL Definition 3.7 is strict. Representability is unnecessary for that combinatorial Hodge result and necessary for the separately asserted wonderful-compactification realization.
- Zero-or-one intersection coefficients in Corollary 5.6 are specific to standard tropical hyperplanes. For other positive divisors the support remains the integer base set, but coefficients can change. The Lorentzian top-intersection polynomial is (r!\sum a_n t^n/n!), not the ordinary base enumerator.
- The rank-two cage ((2,2)) gives a direct normalization check: the raw enumerator (s^2+st+t^2) is not Lorentzian; its factorial normalization is ((s+t)^2/2), and the tropical top-intersection polynomial is ((s+t)^2).
- A Lefschetz fan has a positive fundamental top Minkowski weight, duality, hard Lefschetz, primitive Hodge–Riemann and the same properties on all stars. ADH support invariance also requires simpliciality and nonempty strictly convex cones. The compatible smooth projective common refinement meets these conditions. Ambient ample perturbations and continuity handle the nef boundary.

## Locator and proof corrections

AHR Proposition 3.2 uses letters (a)–(e) in the controlling v2, not the published roman numerals in later citations. Theorem 5.3's reduction proof was read; the separate Section 7 proof of its translated-fan decomposition was not selected and remains an explicit imported input.

The controlling FS preprint has Theorem 2.1 for the Chow–Minkowski identification, Corollary 2.4 for Picard classes, Proposition 3.1 and Theorem 3.2 for multiplication/displacement, and Lemma 3.4 for the saturated subtorus class. These are the numbers to cite for the acquired 1994 version. Its Lemma 4.4 has different content. The 1997 published numbers in the principal source were not independently authenticated as locators for a publisher PDF.

EL Corollary 3.18's proof prints the complementary test degree as (n-r-k); for an ambient variety of dimension (n), a fan of dimension (r), and a degree-(k) class, the degree must be (r-k). The stated multiplication-annihilator conclusion follows with the corrected degree and Poincare duality. The full multiplication annihilator is used, rather than the linear kernel of a degree map.

ADH v4 Lemma 5.21's printed projection relations imply (x_\sigma=-a_1a_2p_*(x_\rho^2)), so the coefficient of (x_\sigma) in that pushforward is (-1/(a_1a_2)), not the displayed (-a_1a_2). The corresponding pairing factor remains positive; the sign and signature argument are unaffected. Two primitive-ray checks, ((1,2)) and ((2,3)), match Lemma 5.11 and detect the reciprocal. The book does not reproduce the incorrect coefficient.

The negative-definiteness sentence in the printed proof of ADH Theorem 5.29 is too strong for the orthogonal complement of an arbitrary primitive vector in higher degree-one dimension. A correct derivation uses mixed HR in degree zero to obtain (\deg(\ell_2^2L)>0), then degree-one primitive HR for (u=\ell_1-\deg(\ell_1\ell_2L)\ell_2/\deg(\ell_2^2L)). The inequality (\deg(u^2L)\leq0) gives the displayed mixed intersection inequality; continuity handles boundary inputs. This corrects the proof wording without claiming its theorem is false.

## Evidence and limits

The [sequential reading notes](Tropical_multidegrees_source_reading_notes_20261007.md) retain the scope and findings at each reading step. Six core exact diagnostic groups pass: primitive lattices/projections, the three-variable example, the six-plane example, factorial normalization, the rank-two cone/balancing instance and its common-facet witnesses. A supplementary group checks two ADH prefactor cases. These are finite consistency checks, not universal geometric proofs.

Failed helpers remain failed: the first oriented-minor expectation, a later SymPy-to-JSON serialization attempt, and an incorrect positivity assumption on the negative pushforward coefficient. New corrected versions supplied the successful records. No failed record was promoted into a successful receipt.

Classical toric Chow duality and pushforward, building-set support theory, AHK matroid Hodge theory, and toric weak factorization remain attributed foundations. No recursive whole-literature verification or independent model-verification receipt is claimed. The principal source's Questions 1.2 and 1.3 retain source-era status; they are not certified as currently open by this checkpoint. The canonical 42-atom/12-problem inventory and the native catalogue/editor are unchanged. The general BJ22 critical Siu-division/envelope input remains open, and the LPWZ density candidate remains unverified.
