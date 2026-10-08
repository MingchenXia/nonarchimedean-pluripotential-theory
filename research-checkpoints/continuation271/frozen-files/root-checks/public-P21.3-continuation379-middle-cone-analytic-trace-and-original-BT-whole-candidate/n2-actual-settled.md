Use the four proved calculus results of n1 on one fixed ordinary open N. T is positive and doubly closed; q=n-p, r=q-1. Z⊂N is ordinary closed; h is continuous and ordinary smooth zero-Hessian off Z. The following six arguments complete the ten-item369 chain.

5. Fix a compact symmetric (r,r)-test α and S=Z∩supp α. For any ordinary neighborhood O of S choose 0≤χ≤1 smooth compact in O and equal to one near S. Decompose ON O itself
D(χα)=η₊-η₋, η=η₊+η₋,
with compact middle-positive η₊,η₋. For smooth g on the SAME N with Dg=0, support localization, transposition, and n1's multiplier identity give
⟨D(hT),α⟩=⟨(h-g)T,D(χα)⟩.
Therefore
|⟨D(hT),α⟩|≤∫|h-g| dμ(T,η)≤sup_{supp η}|h-g|⟨T,η⟩.       (4)
Subtracting g is legitimate because D(gT)=0, although hT need not be closed. These are actual upstairs compact smooth tests whose positive outputs lie inside O. For empty S, use zero cutoff forms.

6. If for each α actual triples (χ_j,η_{j,±},g_j) on the same N make the integral in (4) tend to zero, then the fixed left pairing is zero. Symmetric tests determine the symmetric defect, so D(hT)=0. Vanishing of supremum error times mass is a sufficient stronger condition. The g_j need only approximate h on moving supports. Existence of such triples for an arbitrary original pair is NOT asserted.

7. Let C_{T,α}(S;O) be the infimum of ⟨T,η₊+η₋⟩ over precisely these actual cutoff/decomposition competitors. A competitor exists and has finite mass; positivity makes the infimum nonnegative. It is zero for empty S and nondecreasing as O shrinks. For relatively compact O put ω_g(O)=sup_O|h-g|. Taking the infimum in (4), without assuming attainment, gives
|⟨D(hT),α⟩|≤ω_g(O) C_{T,α}(S;O).                         (5)
If h=g on compact S, continuity supplies relatively compact neighborhoods with arbitrarily small ω_g. Uniformly bounded cutoff masses, or merely a vanishing product in (5), gives removability. Conversely a nonzero detector of magnitude d forces C≥d/ω_g wherever ω_g>0 and forbids ω_g=0. Separate finite masses on each neighborhood do NOT imply uniform small-neighborhood mass control. This infimum is test-specific and is not identified with a standard capacity.

8. If these estimates establish zero on an ordinary cover of a specified W, restriction and finite nonnegative localization of compact tests makes the same defect zero on W. This glues established identities for the original current. It does not create closed approximating currents using a partition. A cover of W does not constitute a basis inside every ordinary open.

9. If Z is locally Zariski closed in analytic domains and dim Z<r=n-p-1, n1's exact CLD support theorem makes every compact (r,r)-test support disjoint from Z. The defect is supported in Z; all pairings vanish. Ordinary localization gives D(hT)=0. The same argument works for ordinary closed Z satisfying d_K(z)<r pointwise. For pure codimension c, the integer condition is c≥p+2. When p=n-1, r=0, so this dimension method removes NO nonempty locus.

10. A nonzero defect has a compact detecting test; symmetrize it. Its support must meet Z, and every point in its support has d_K≥r. Thus a detector meets Z at an ACTUAL analytic point with d_K≥n-p-1. Applying item9 to the original weighted δ_X gives D[h]=0 when dim Z<n-1, retaining generic Artinian weights. This neither recognizes ±h as psh nor constructs separately admissible U,V. For p≥1 the range n-p-1≤dim Z<n-1 is unexcluded by this dimension argument. It does not exhibit a counterexample. For p=0 there is no such dimensional window.

The whole369 paper and proof, its three actual FINAL bodies, and three distinct expanded bodies were examined as different artifacts. The reconstructed chain uses n1's middle-cone, sign, and degree repairs. No universal off-locus regularity, analytic trace, or weighted vanishing follows here merely from D[h]=0.

Artifacts: P21.3-review-paper.tex, P21.3-proof-companion.md, whole-proof-coverage.json, and independent-whole372-verdict.json. Rerun python audit.py and python build_review.py. All157 supplied bindings and31 literal source units match their retained bytes. These are integrity observations, not a correctness certificate.