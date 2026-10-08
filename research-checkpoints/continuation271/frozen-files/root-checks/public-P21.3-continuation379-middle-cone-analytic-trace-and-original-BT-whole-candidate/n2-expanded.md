# All cutoff and dimension conclusions of 369

Use the four calculus lemmas proved in local note n1, on one fixed ordinary open \(N\), with positive doubly closed \(T\), \(q=n-p\), and \(r=q-1\). Let \(Z\subset N\) be ordinary closed and \(h\) continuous, ordinary smooth with zero smooth Hessian off \(Z\). The six following arguments complete the ten-item chain of 369.

Fix a compact symmetric \((r,r)\)-test \(\alpha\), and put \(S=Z\cap\operatorname{supp}\alpha\). For any ordinary neighborhood \(O\) of \(S\), choose \(0\leq\chi\leq1\) compact smooth in \(O\), equal to one near \(S\). Decompose, on \(O\) itself,
\[
 D(\chi\alpha)=\eta_+-\eta_-,\qquad\eta=\eta_++\eta_-,\quad\eta_\pm\geq0.
\]
For a smooth \(g\) on the same \(N\) with \(Dg=0\), n1's support localization, transposition, and smooth multiplier identity gives
\[
 \langle D(hT),\alpha\rangle
 =\langle (h-g)T,D(\chi\alpha)\rangle,
\]
and hence
\[
 |\langle D(hT),\alpha\rangle|
 \leq\int|h-g|\,d\mu_{T,\eta}
 \leq\sup_{\operatorname{supp}\eta}|h-g|\,\langle T,\eta\rangle.              \tag{4}
\]
Subtracting \(g\) is legitimate because \(D(gT)=0\), even though \(hT\) need not be closed. These are actual upstairs tests with compact positive outputs in the specified \(O\). For empty \(S\), take all cutoff forms zero. This proves item 5.

If, for each \(\alpha\), actual triples \((\chi_j,\eta_{j,\pm},g_j)\) on the same \(N\) make the integral in (4) tend to zero, then the fixed left pairing is zero. All symmetric tests determine the symmetric defect, so \(D(hT)=0\). The vanishing of supremum error times mass is a sufficient stronger premise. The functions \(g_j\) need only approximate \(h\) on the moving supports, not on all of \(N\). This proves item 6 without assuming the existence of such triples for an arbitrary pair.

Define \(\mathcal C_{T,\alpha}(S;O)\) as the infimum of \(\langle T,\eta_++\eta_-\rangle\) over precisely the actual cutoff/decomposition competitors above. A competitor exists, its mass is finite, and positivity gives a nonnegative infimum. It is zero for empty \(S\), and nondecreasing as \(O\) shrinks. For relatively compact \(O\), let \(\omega_g(O)=\sup_O|h-g|\). Taking the infimum in (4), without assuming attainment, gives
\[
 |\langle D(hT),\alpha\rangle|\leq
 \omega_g(O)\mathcal C_{T,\alpha}(S;O).                                    \tag{5}
\]
If \(h=g\) on compact \(S\), continuity gives relatively compact neighborhoods with arbitrarily small \(\omega_g\). Uniformly bounded cutoff masses, or merely a vanishing product in (5), proves removability. Conversely a detector of magnitude \(d>0\) forces \(\mathcal C\geq d/\omega_g\) where \(\omega_g>0\), and forbids \(\omega_g=0\). This proves item 7. Separate finite masses on each neighborhood do not imply uniformly bounded masses. This quantity is test-specific; it is not identified with a standard capacity.

If these estimates establish zero on members of an ordinary cover of a specified \(W\), then ordinary restriction and finite nonnegative localization of compact tests makes the same current zero on \(W\). This proves item 8. It glues established identities for the original current; it does not construct closed approximating currents by a partition. A cover of \(W\) is not a basis inside every ordinary open.

Suppose now \(Z\) is locally Zariski closed in analytic domains, with \(\dim Z<r=n-p-1\). The exact CLD support theorem stated and checked in n1 makes every compact \((r,r)\)-test support disjoint from \(Z\). The defect is supported in \(Z\), so all its pairings vanish. Ordinary localization proves \(D(hT)=0\), which is item 9. The same proof works for ordinary closed \(Z\) with the actual pointwise condition \(d_K(z)<r\). For a pure codimension \(c\), the integer bound is \(c\geq p+2\). When \(p=n-1\), \(r=0\); this method removes no nonempty locus.

For item 10, a nonzero defect has a compact detecting test by definition. Symmetrize it. Its support must meet \(Z\), and every point of its support has \(d_K\geq r\). Thus a detector meets \(Z\) at an actual analytic point with \(d_K\geq n-p-1\). Applying item 9 to the original \(\delta_X\) gives \(D[h]=0\) if \(\dim Z<n-1\), with the actual Artinian weights retained. This does not recognize either sign of \(h\) as psh or furnish individually admissible \(U,V\). For \(p\geq1\), the inequalities \(n-p-1\leq\dim Z<n-1\) leave a dimensional window unexcluded by this method. They do not exhibit a counterexample. At \(p=0\) there is no such window.

These ten statements are conditional partial results. The whole369 paper and proof, all three actual FINAL texts, and all three distinct expanded texts were examined as different artifacts. The independently reconstructed results use n1's middle-cone, sign, and degree repairs. No universal off-locus regularity, trace geometry, or weighted vanishing follows here from \(D[h]=0\).

Artifacts: P21.3-review-paper.tex, P21.3-proof-companion.md, independent-whole372-verdict.json, and whole-proof-coverage.json. Rerun python audit.py and python build_review.py. The 157 input bindings and 31 literal source units match their retained bytes; these are integrity observations, not a correctness certificate.
