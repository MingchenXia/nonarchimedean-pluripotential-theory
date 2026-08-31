# Independent correctness audit: Ch16 multipliers and harmonic convexity

Date: 2026-09-01. Auditor: `/root/p081_weighted_repair_fresh`.

## Verdict and limits

The two original passages need correction. The continuous-multiplier paragraph attributes an unsupported strengthening and an invalid approximation argument to CLD. The original harmonic-convex corollary drops the skeletal Bedford–Taylor hypothesis and confuses a harmonic-chart G-smooth approximation with an ordinary CLD-smooth psh approximation. Its arbitrary-positive-closed-current assertion is contradicted already by the book's abstract cross-fan calculation.

The root-authored revisions at the exact final hashes below correct the targeted defects, including their actual continuity and canonical-metric consumers. No substantive gap was found in those revised arguments, relative to the explicitly retained, already stated book inputs. The Ch19 theorem retains its original scope. This is an evidence-based correction using existing results, not acceptance of a new research theorem, not a production/Rethlas verdict, and not a proof of P21.3.

The detailed final-byte verification is in `AFTERPATCH_ADDENDUM.md`. This report first records what was wrong before revision, so that the historical diagnosis is not lost.

The auditor did not author Ch16, Ch19, or the root's replacement paragraphs. The auditor previously authored the frozen common-constant/cohomology source diagnosis and communicated the relevant source-interface warnings and review feedback. That predecessor is disclosed as related work, not treated as an independently certified theorem. No manuscript, existing dossier, candidate, or production artifact was modified by this auditor. Read-only `git show` and `git diff` were used after the root explicitly requested comparison with its working-tree revisions.

## Exact objects

Book root: `/Users/mingchen/Projects/Yethlas/nonarchimedean_pluripotential_theory`.

Pre-revision source is pinned by commit `10897afc0b7379ee169f46ecb77184ac7580f177`:

| File relative to book root | Before SHA256 | Reviewed after SHA256 |
| --- | --- | --- |
| `manuscript/parts/part2/ch16_bedford_taylor.tex` | `5330c13d296dc772c923b097d5819929c0bde5530509c60349fcd331ba187683` | `41333978fbce28644d1f63aac6431f763dd3f3cc1dd792faf1b20b43ab3a9e83` |
| `manuscript/parts/part2/ch19_cld_examples.tex` | `dbd90da1e3ff05f3aba9753faecc6789d03a44ba46cbf1cd0846aed0e334e52a` | `4d59d219eec46bea029d6d131e6f55c110a7fbf4c3f30be9dcf4147a4c5a6652` |

`INPUT_HASHES.json` pins the supporting Chapters 15, 17 and 18, the book entry point, the exact CLD text, and the disclosed predecessor. `EXACT_CHANGED_PASSAGES.md` preserves line-numbered before/after excerpts; `REVIEWED.diff` preserves the root-authored diff. Old line numbers below refer to the pinned commit, not the revised file.

## 1. Arbitrary continuous multipliers: old Ch16:1625–1629

The immediately preceding `cor:ch16-bt-times-function` assumes that the multiplier is nonnegative and locally constant. Its proof is correct: ordinary locality reduces to multiplication by a nonnegative constant, which preserves positivity, closedness and the defining Bedford–Taylor equality. That statement should be retained.

The paragraph following it says that CLD Corollary 8.6.7 gives the stronger assertion for an arbitrary continuous nonnegative `f` **such that `fT` is again positive and closed**, supposedly by local smooth approximation and `prop:bt-current-stability`.

Two distinctions matter.

1. The printed CLD corollary does not contain the italicized extra closedness condition. It literally states that a positive continuous multiplier preserves the Bedford–Taylor class. Since that class is defined to consist of positive **closed** currents, the printed assertion fails already for a smooth nonconstant positive multiplier of integration on an ordinary real interval: `d'(f[T]) = d'f ∧ [T]` need not vanish. For example, use `f(t)=exp(t)` and a nonzero compactly supported smooth test on an interval. This is an elementary failure of closedness, not a counterexample to P21.3.
2. The book has inserted a condition that avoids that immediate counterexample. Therefore it would be inaccurate to say that the same nonclosed example disproves the book's conditional strengthening. What is wrong in the book is the attribution and the supplied justification. Even if the final `fT` is closed, an arbitrary smooth approximation `f_j` need not make `f_jT` closed, let alone Bedford–Taylor. The weak-limit stability theorem cannot be invoked on that sequence. No argument in this passage proves the conditional strengthening.

Smallest honest correction: retain the locally constant corollary and proof; replace the following paragraph by a source warning explaining why arbitrary continuous multiplication does not preserve closedness and why smooth approximation supplies no Bedford–Taylor sequence. Do not assert either truth or falsehood of the additional conditional strengthening without a separate argument. The root's final revision does exactly this.

The only direct use of `cor:ch16-bt-times-function` in the active manuscript is the constant-multiplier calculation in the tripod example (old Ch16:3113, revised:3121). It remains valid. That local example must not be read as a classification of every positive closed (0,0) current on every abstract tropical curve: the same chapter's cross-fan has different balanced weightings. No such general classification is needed by the multiplier correction.

## 2. Harmonic convexity: old Ch16:3839–3863

### 2.1 Missing current hypothesis

`thm:bt-harmonic-compatibility` (old Ch16:3727 onward) explicitly assumes a **skeletal Bedford–Taylor** current. Its extension to several G-smooth factors assumes a current locally a difference of skeletal Bedford–Taylor currents. These match the hypotheses of CLD Proposition 8.11.1 and Corollary 8.11.2.

The old corollary instead claims positivity for **every positive closed** current and invokes the compatibility theorem at old line 3850. These are not the same hypotheses. Positivity and closedness neither imply the Bedford–Taylor independence property nor supply the weighted harmonic normal-slope cancellation. The chapter itself computes that failure.

### 2.2 Concrete diagnosis using the existing cross-fan, not new analytic geometry

On the unit-weight cross `Σ` from `ex:ch16-cross-fan`, put

`h = |x_1| - |x_2|`.

The four outgoing slopes of `h` are `(1,1,-1,-1)`, so the book computes `d'd''[h]=0`. It is parlinear and hence harmonic in the chapter's stated definition. By the G-tropical-chart definition (CLD §3.1.3), a parlinear map is permitted as a G-chart; equivalently one can adjoin `h` to the two original coordinates and use `(x_1,x_2,h)`. These coordinates are all harmonic. Restrict to a bounded star around the origin if a compact chart domain is desired; the calculation is supported in its interior.

Let `T` have horizontal weights 2 and vertical weights 1, exactly as in the book. It is positive and closed, and the existing calculation is `d'd''(hT)=2δ_0`. The function `F(s)=-s` is affine, hence continuous convex, and its pullback along the harmonic chart `h` is `-h`. Thus

`d'd''((-h)T) = -2δ_0`,

which is not positive. The product is defined: `-h` is the difference of the book's two explicit ordinary continuous psh functions, and multiplication of a positive current by a continuous function is available anyway.

This contradicts the old corollary in its stated **abstract tropical** scope. It does not manufacture an analytic chart on a Berkovich space, does not construct an analytic non-Bedford–Taylor current, and does not refute a strict-PL analytic result such as CLD 18.8.9.

### 2.3 Ordinary approximation was also overclaimed

For smooth convex `F_j`, the functions `F_j∘f` are G-smooth in the harmonic chart. They need not be smooth in the original ordinary CLD form sheaf. Positive chart Hessian therefore cannot be promoted to an ordinary smooth-psh approximating sequence merely by composing with `f`.

The old proof invokes standard Bedford–Taylor continuity without establishing its ordinary CPsh hypotheses, and then calls the limit locally approachable. This is precisely the missing implication, not a consequence of the invoked theorem. The earlier prelude to harmonic continuity even says that these functions are not psh in general, contradicting the old corollary's proof language.

For continuous convex `F`, the dpsh assertion is not justified just by taking a uniform limit of G-smooth/dpsh functions: no uniform-closedness of the entire difference sheaf is supplied. The subsequent phrase about two convex presentations of a signed harmonic chart is not a defined construction or a proof. Dropping these claims is the honest correction. This audit does not assert that every such dpsh conclusion is false.

The Ch19 example excluding **ordinary smooth harmonic** approximation must not be misquoted as excluding ordinary **psh** approximation. A psh approximation is allowed to have nonzero curvature. Those are different statements.

### 2.4 The minimal fixed-current result

For a fixed skeletal Bedford–Taylor current `T`, the retained assertion is simply positivity and closedness of

`d'd''((F∘f)T)`.

Smooth convex target approximation, the stated harmonic compatibility theorem, ordinary continuous multiplication of the positive current `T`, and continuity of current differentiation suffice. No assertion that the pullback belongs to ordinary CPsh or dpsh is needed. No claim that insertion of arbitrary harmonic G-forms preserves all hypotheses is needed. The root's final proof uses precisely this argument.

## 3. Harmonic continuity consumer: old Ch16:2365–2396

The proposition originally permits arbitrary positive closed `T_a` and derives positivity at every recursive step from the defective corollary. CLD Proposition 8.7.3 does the same: its proof explicitly invokes Corollary 8.11.3. The source citation is therefore not an independent repair of the missing hypothesis.

This is a hypothesis-transfer failure, not merely a circular arrangement of labels. The earlier standard continuity theorem is already proved, but its psh hypothesis has not been supplied for the harmonic pullbacks.

Smallest supported version: require `u_i^a,u_i ∈ CPsh_X` for `1≤i≤q`; no psh condition is needed on the outer continuous multiplier indexed by zero. Composition with the continuous chart carries local uniform convergence on the target to local uniform convergence on source compacts. The existing `thm:cld-bt-continuity` then applies directly. Retain the label and explain why the broader arbitrary-current formulation has not been justified here.

This is what the revised proposition does. There are no direct references to this proposition elsewhere in the active book. No downstream theorem needs to be silently narrowed through this label.

## 4. Ch19: preserve canonical positivity by the correct analytic input

The old direct external consumer of the bad corollary is Ch19:2623, in `thm:ch19-canonical-positivity`. That theorem is analytic, boundaryless, nontrivially valued, and uses the actual split Raynaud data fixed in the chapter. It is not a theorem about an arbitrary abstract harmonic chart.

CLD Corollary 18.8.9 is the correct source: a strictly parlinear harmonic map on a boundaryless analytic space over a nontrivially valued field pulls back continuous convex functions to psh functions. CLD Proposition 19.3.1 explicitly invokes 18.8.8 for the formal term and 18.8.9 for the tropical term. It does not rely on 8.11.3 for this step.

There was also an adjacent source-scope mismatch: the two old references to `thm:gk-formal-positivity-comparison` invoke a Ch18 theorem assuming **algebraically closed** `K`, while this Ch19 result does not impose that condition. The existing Ch17 `thm:ch17-psh-residual-nef`, corresponding to CLD 17.8.4 and 18.8.8, supplies the actual integral-PL analytic equivalence over the original field. Its use here avoids any change of field or pullback of an arbitrary current.

The root's replacement gives a full ordinary-CPsh proof of the particular convexity step, using existing results only. The proof and all normalization/compactness checks are detailed in the addendum. It also replaces both mismatched GK references by the Ch17 theorem, and retains the entire original Ch19 theorem statement.

### A source-proof caution that is not imported into the revision

CLD 18.8.9(c), printed p.542, says that affine interpolation of a convex function on a sufficiently fine simplicial decomposition remains convex. An arbitrary triangulation does not have that property. On the unit square take `F(x,y)=(x-y)^2` and triangulate along the diagonal joining `(1,0)` to `(0,1)`. The interpolant has value 1 at the center but value 0 at both `(0,0)` and `(1,1)`, so it is not convex. Rescaling gives arbitrarily fine versions.

The root's finite maximum of actual tangent affine functions for the quadratic function avoids this issue altogether. The audit does not declare the published theorem false: its stated analytic conclusion has the separate formal-positivity plus convex-approximation proof used here.

## 5. Complete direct-reference impact within the active manuscript

`ACTIVE_REFERENCE_INVENTORY.json` follows literal uncommented `input`, `include` and `draftinclude` commands recursively from `manuscript/book.tex`. It inspected 210 reachable TeX files, including actually included editorial theorem files; there are no unresolved literal includes. This is an inclusion/reference scan, not a TeX execution or a count of the root's build dependencies. The dynamic `#1` macro body is recorded and excluded as a macro definition. Historical unused dossiers are not consumers.

All occurrences of nine relevant labels are preserved with file, line, exact source line, before/after state, and definition/reference classification. Conclusions:

| Dependency | Active pre-revision references | Effect of the correction |
| --- | --- | --- |
| Locally constant multiplier corollary | 1, the tripod calculation | Unchanged and supported. |
| Harmonic-convex corollary | 2 in the Ch16 continuity proof; 1 in Ch19 canonical positivity | Ch16 proof replaced by explicit ordinary CPsh continuity; Ch19 proof replaced by analytic residual-positivity and finite-max argument. |
| Harmonic-continuity proposition | 0 | No external theorem acquires an undisclosed assumption through this label. |
| Harmonic compatibility theorem | 19 | The theorem itself and its skeletal Bedford–Taylor hypotheses are unchanged. Calls in canonical curvature/MA concern integration or constructed formal-curvature/dpsh currents, not an arbitrary positive closed current. They do not require the rejected broad corollary. |
| Ch19 canonical positivity | 2 | Mixed-reduction example and summary retain the original theorem through its repaired proof. |
| Ch19 canonical MA | 10 | Six Ch19 numerical/summary consumers and four Ch31 consumers remain downstream of the unchanged theorem; no numerical formula is changed by this correction. |

The ten canonical-MA reference sites in the revised book are Ch19:2957, 3043, 3108, 3492, 3969, 4155 and Ch31:208, 2263, 2890, 3224. The two original canonical-positivity reference sites move to Ch19:3104 and 4154; the revision also adds two explanatory forward references in Ch16.

Ch18:5917 refers historically to the harmonic-chart section, not to the faulty positivity corollary. It does not transfer the stronger conclusion. Ch16's cross-fan discussion, normal-slope discussion and hypothesis tables remain consistent with the revised restricted theorem. Phrases such as “harmonicity alone” in the abelian exposition are to be read relative to the constructed currents and the explicitly cited compatibility theorem, not as a removal of its current hypotheses. Making this qualifier explicit would improve exposition but is not a new mathematical dependency created by these corrections.

No targeted label was removed or added: Ch16 retains all 205 label occurrences, Ch19 all 198. This check does not substitute for the scope analysis above.

## 6. Remaining bounded notes and nonclaims

- Ch16:1559 still groups source items as “Propositions 8.6.3, 8.6.5--8.6.8”. This imprecisely includes the printed Corollary 8.6.7 now explicitly warned about. A future editorial cleanup can list 8.6.3, 8.6.5, 8.6.6 and 8.6.8 individually, with Example 8.6.4 for integration. The actual item-by-item book proof does not need the problematic corollary. This is not a blocking mathematical defect in the two reviewed final files.
- This bounded review checks applications of the stated skeletal compatibility theorem; it does not re-audit every part of the source-skeletal representation theorem, residual intersection theory, or every canonical-MA computation. In particular it does not certify a new route to arbitrary-current rigidity.
- The analytic strict-PL argument shows why the Ch19 application is sound without proving that every continuous distributionally harmonic function is locally in this class. No arbitrary continuous-harmonic regularization, all-current classification, weakly smooth extension of ordinary currents, or P21.3 solution follows.
- Two-sided **ordinary** CPsh is sufficient for harmonic multiplication stability by the already proved one-factor positivity theorem: the products for `h` and `-h` have opposite signs and must vanish. This is not a claim that every continuous `h` with `d'd''[h]=0` is two-sided CPsh.
- No mathematical candidate is promoted and no production gate is removed. No build, PDF generation or visual QA was performed by this auditor in this dossier. The root's separate build/visual review is not this audit's evidence of mathematical correctness.

Final assessment: the reviewed replacements are justified corrections of overclaims and mismatched citations, with a complete elementary proof of the already published Ch19 special case. No additional theorem-level repair is required for these exact changed arguments.
