# Hattori Calabi–Yau-fibration source review, 8 October 2026

The controlling proof text in this audit is Masafumi Hattori, *On K-stability of Calabi–Yau fibrations*, arXiv:2203.11460v2, updated 9 August 2023 at 01:19:00 UTC. Its 44-page PDF has SHA256 `da827f6523a543dde718425ef3cad02b30c5484279bb4d196cd07f54d8cd9a62`. All 44 pages were actually read, in order, with complete selected text, 22 individually displayed matching images and 22 sequential notes. Preparation flags remain false and give zero reading credit; the separate actual ledger controls the completed reading.

Crossref and the publisher article metadata identify the formal publication as *Journal of the Institute of Mathematics of Jussieu* 24(3) (2025), 961–1019, DOI `10.1017/S1474748024000598`, online 19 March 2025. The publisher-linked PDF request returned HTML rather than PDF. That failed acquisition is retained unchanged, with zero journal proof credit. The observations below apply to the pinned arXiv v2; no claim is made that the unread 2025 publication contains the same wording or errors. This is a foundational dependency audit of the preceding adiabatic unit, not a newly posted 2026 result.

## Definitions and reusable calculation

Definition 2.8, physical pages 7–8, divides its intersection functionals by the generic volume V=L^d. For a fixed model, scaling both the generic and model polarization by a positive rational lambda gives:

- E, I, J and N=I−J scale by lambda.
- Entropy, volume-normalized DF and J^T for a fixed auxiliary class T are invariant.
- Scaling the auxiliary class T separately multiplies J^T by that factor.

The DF statement follows by degree counting: its canonical intersection numerator and volume both scale by lambda^d, while its canonical slope scales by lambda^(−1) and E scales by lambda. It concerns polarization rescaling. Normalized base change instead scales Mabuchi and Ding exactly by its degree and gives an inequality for DF when a nonreduced central fiber is present.

Definition 2.18, physical page 10, uses an ample total-space Q-line bundle A, an ample base L and A_epsilon=epsilon A+f*L. Uniform adiabatic K-stability means there exist delta>0 and epsilon0>0 which work for every small positive rational epsilon and every semiample test configuration. With P_k=A+k f*L and k=epsilon^(−1), the same condition is DF(P_k)>=delta k^(−1)J(P_k) for all large rational k and all tests. Uniform stability at each fixed class with a parameter-dependent constant does not give this condition. Transport to another norm needs comparison constants independent of k. A relatively ample O(1) requires a fixed base-ample shift before matching the source's globally ample setup.

These conclusions follow directly from the definitions and are the intended book integration. Six exact dimension fixtures check the homogeneities. They do not assert that a new fibration is stable and are not independent-model verification receipts.

## Main-theorem scope and proof qualifications

Theorem 1.1 is an attributed equivalence for polarized klt-trivial fibrations over smooth curves. It uses the canonical-bundle-formula discriminant B and moduli M; the smooth cscK clause additionally assumes Delta=0 and a smooth total space. Relative Q-linear triviality of K_X+Delta is essential. A Delta=0 projective bundle with positive-dimensional projective-space fibers has fiber canonical bundle O(−r), so the preceding Ortu–Sektnan projective bundles do not satisfy that hypothesis.

The source proof proceeds through numerical J-positivity, base descent using equivariant models, alpha/delta limits, an entropy estimate and special-test boundary perturbations. Reading those arguments exposes distinct bookkeeping obligations:

- The lct definition on page 9 prints an infimum of the downward-closed admissible set; the intended supremum agrees with its displayed valuative minimum. Positive discrepancy margins must use normalized ord_E, not arbitrary rescalings c ord_E. Several strict energy/entropy assertions include trivial tests, where all relevant quantities are zero; their actual instability contradictions require only nonnegativity.
- The singular J-criterion's local resolution expansion works by pushing effective cycle intersections to the original variety. Its zero-dimensional endpoint must be written separately rather than literally as L^(−1). Its use of the smooth Chen criterion remains an external input. The nef-canonical constant absorption can choose the error constant at least one and shrink the epsilon interval to all earlier ranges.
- The base-descent proof compares V_epsilon DF, whose numerator is a finite intersection polynomial; DF itself is volume-normalized. Its final binomial factor c/(c+1) is correct. One intermediate line omits a common epsilon power and slope multiplier. Codimension-two exceptional divisors do not contribute to the leading term with c pulled-back base factors. Semistable reduction, b-nef moduli comparison and MMP extensions remain external foundations. The phrase reduced snc divisor must distinguish reduced central support from rational boundary coefficients; ordinary generic smoothness alone does not prove every relative log-smooth assertion over a special divisor.
- Lemma 4.8, pages 25–26, bounds horizontal multiplicity but its printed curve equality drops the intersection with an incomplete vertical divisor on a reducible fiber. The direct surface diagnostic below makes that omission explicit. The subsequent curve-degree line also loses its epsilon factor. A componentwise complete-fiber degree budget is needed; no general replacement proof is admitted here.
- In Theorem 4.12, page 29, integrating `d(1−x)epsilon^(d−1)a+epsilon^d b` over [0,1] gives `d/2 epsilon^(d−1)a+epsilon^d b`. The printed bounding chain omits d; restoring it leaves the intended ratio limit 1/2. The finite-basis factor on page 30 is inverted: the valid upper factor is `max(1,(1−S_m)/(1−C))`, not the printed reciprocal minimum. It still tends to one. A numerical implication fixture checks the direction without claiming a realizing valuation.
- In A.6, page 36, the printed entropy and minimum-norm polarization scalings are unnormalized degrees, inconsistent with Definition 2.8. The desired final entropy estimate has the correct conditional deduction: if delta(rL)>=1 implies H(rL)>=N(rL), then H(L)>=rN(L); let rational r approach delta(L) from below. This fixes local scaling, without independently establishing the general Ding criterion.
- A.11, page 38, prints exact DF degree scaling after normalized base change; the valid inequality is enough for its upper bound. A.15's beta comparison must use boundary B+T1, consistently with A.3. For A.17's empty boundary support the maximal coefficient must include zero, so untwisted P1 is not incorrectly declared uniformly stable.

The alpha/delta theorem's limit may remain true after these local corrections; this audit does not construct a counterexample to it or to the general cscK equivalence. Ambro/Fujino–Gongyo canonical-bundle foundations, Kollár singularity and global-generation bounds, BHJ filtrations/norms, Fujita/Li–Xu reductions, Chen J-positivity and Zhang/Chen–Cheng analytic coercivity/existence have not been recursively certified in their primary proofs. The main equivalence remains a qualified source claim, outside the intended book's established inputs. The 2023 source's b-semiampleness/forthcoming statements do not certify current open status.

## Reducible-fiber diagnostic

Let Z be the blowup of P1×P1 at a point, with ruling classes S,F satisfying S²=F²=0 and S.F=1, and exceptional E0 with E0²=−1. The reducible fiber is F=E0+Gamma, Gamma=F−E0. Set A=2S+2F−E0. Then A²=7, A.E0=1 and A.Gamma=1. For every other irreducible strict transform of aS+bF of multiplicity m at the blowup center, m<=a+b, so A intersects it by 2(a+b)−m>0; the attributed Nakai–Moishezon criterion gives ampleness.

Choose P on Gamma away from E0. Choose smooth horizontal C1 in |S+F| and C2 in |S| meeting transversely at P and avoiding the blowup center. Their sum C has class 2S+F. For rational epsilon>0 set D_hor=epsilon C and D_vert=F+epsilon Gamma. These are effective horizontal/vertical parts and D_total is Q-linearly equivalent to F+epsilon A. Direct intersections give:

`D_hor.Gamma=2epsilon`, `epsilon A.Gamma=epsilon`, `D_vert.Gamma=−epsilon`.

The point multiplicity of D_hor at P is 2epsilon. Thus the printed equality in Lemma 4.8 cannot discard D_vert.Gamma. This example is consistent with a uniform bound using the complete-fiber budget epsilon A.F=2epsilon; it refutes that proof equality, not the lemma or main theorem. The intersection matrix and six-dimensional volume/homogeneity checks are retained in the exact diagnostic record.

## Preservation and publication scope

This source checkpoint leaves the active validated 4,632-page book, all 425 TeX inputs, both bibliographies and the native catalogue source/PDF unchanged. The last complete whole-book pass remains 4 October. All 42 canonical atoms and twelve formal problems keep their status; general BJ22 critical homogeneous Siu division and envelopes remain OPEN and LPWZ density UNVERIFIED. No original general theorem or independent gpt-6.1-sol xhigh receipt is claimed. The complete source cache and matching images remain in the cloud; the authorized repository upload concerns authored audit records. Upload/export supplies no extra reading credit. A fresh read-only check found work at `97107151cb5d84581e77189f557c833d20ea131b` and main at `00957114db21b627e97369563032ceda9cea09c7`, with no incoming author change detected.
