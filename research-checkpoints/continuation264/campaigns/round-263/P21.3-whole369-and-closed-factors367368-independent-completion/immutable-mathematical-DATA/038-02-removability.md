# A weighted cutoff theorem on a fixed ordinary open

## Theorem 5: a quantitative bound for every possible detecting test

Fix one ordinary open \(N\), a positive doubly closed \((p,p)\)-current \(T\) there, an ordinary closed set \(Z\subset N\), and \(h\in C(N,\mathbb R)\) which is ordinary smooth with zero smooth Hessian on \(N\setminus Z\). Set \(R=D(hT)\). Fix a symmetric compact ordinary smooth \((r,r)\)-test \(\alpha\), where \(r=n-p-1\), and put \(S=Z\cap\operatorname{supp}\alpha\).

Let \(O\subset N\) be any ordinary open neighborhood of this compact set \(S\). Choose \(\chi\in C_c^\infty(O)\), extended by zero to \(N\), with \(0\leq\chi\leq1\) and \(\chi=1\) near \(S\). Choose a positive decomposition in \(O\),
\[
 D(\chi\alpha)=\eta_+-\eta_-,\qquad \eta=\eta_++\eta_-,\quad
 \eta_\pm\in\mathcal A_c^{q,q}(O),\quad \eta_\pm\geq0.\tag{4}
\]
Let \(g\) be any ordinary smooth function on \(N\) with zero smooth Hessian. Then
\[
 |\langle D(hT),\alpha\rangle|
 \leq\int_N|h-g|\,\mathrm d\mu_{T,\eta}
 \leq\|h-g\|_{\operatorname{supp}\eta}\langle T,\eta\rangle.\tag{5}
\]
All these objects exist except for any requested bound on the right side. When \(S\) is empty we may take \(\chi=0\) and \(\eta_\pm=0\).

Proof. Existence of a compact smooth cutoff is CLD 15.2.5. Composing such a cutoff with a smooth scalar function that is zero near zero, one near one, and takes values in \([0,1]\), gives the displayed bounds without enlarging its support. Since \(D(\chi\alpha)\) is symmetric, compact, of degree \((q,q)\) and supported in \(O\), Lemma 1 proves (4). Lemma 4, current duality, and Lemma 3 give the exact identity
\[
 \langle D(hT),\alpha\rangle
 =\langle D(hT),\chi\alpha\rangle
 =\langle (h-g)T,D(\chi\alpha)\rangle.\tag{6}
\]
Indeed \(\langle gT,D(\chi\alpha)\rangle=\langle D(gT),\chi\alpha\rangle=0\). Lemma 2 with \(b=h-g\) proves (5). No derivative of the continuous function \(h\) has been taken as a smooth form. No nonsmooth wedge product is used. Both the product and its detecting test are upstairs on the original analytic space.

## Corollary 6: weighted removability

Under the hypotheses of Theorem 5, suppose that for every symmetric compact detecting test \(\alpha\), there is a sequence or net of actual triples \((\chi_j,\eta_{j,\pm},g_j)\) satisfying (4), the cutoff condition near the same \(S\), and \(Dg_j=0\), on the fixed \(N\), for which
\[
 \int_N|h-g_j|\,\mathrm d\mu_{T,\eta_j}\longrightarrow0.\tag{7}
\]
Then \(D(hT)=0\) on \(N\). The sufficient condition \(\|h-g_j\|_{\operatorname{supp}\eta_j}\langle T,\eta_j\rangle\to0\) may replace (7).

Proof. Apply (5) to each triple. Its left side is a fixed nonnegative number, so (7) forces it to be zero. Symmetric tests detect the symmetric current \(D(hT)\), proving the assertion. The sufficient condition follows from the second inequality of (5). The reference functions need not approximate \(h\) off the cutoff supports. Thus this result is distinct from locally uniform smooth harmonic approximation on a whole neighborhood. It is explicitly a sufficient condition, not an existence theorem for the triples.

## A cutoff mass quantity

For the fixed \(T,Z,\alpha\), define
\[
 \mathcal C_{T,\alpha}(S;O)
 =\inf_{\chi,\eta_\pm}\langle T,\eta_++\eta_-\rangle,\tag{8}
\]
where the infimum is over exactly the cutoffs and actual positive decompositions (4) supported in \(O\), with \(\chi=1\) near \(S\). This is a test-dependent cutoff mass, not an identification with any standard pluripotential capacity. It is nonnegative and finite for each such \(O\), because Theorem 5 constructs at least one admissible decomposition and a current is finite on each compact smooth test. It is zero for \(S=\varnothing\). If \(O_1\subset O_2\), then \(\mathcal C(S;O_1)\geq\mathcal C(S;O_2)\), since the smaller open admits fewer competitors. No uniform bound as the open shrinks follows from pointwise finiteness.

## Theorem 7: smooth trace and the necessary blowup of cutoff mass

Keep the hypotheses of Theorem 5 and fix a smooth zero-Hessian \(g\) on \(N\). For a relatively compact ordinary neighborhood \(O\) of \(S\), put
\[
 \omega_g(O)=\sup_{x\in O}|h(x)-g(x)|.
\]
Then
\[
 |\langle D(hT),\alpha\rangle|
 \leq\omega_g(O)\mathcal C_{T,\alpha}(S;O).\tag{9}
\]
In particular, if \(h=g\) on \(S\), and for a sequence of relatively compact neighborhoods \(O_j\) of \(S\) we have
\[
 \omega_g(O_j)\to0,
 \qquad\omega_g(O_j)\mathcal C_{T,\alpha}(S;O_j)\to0,\tag{10}
\]
the detecting pairing is zero. Uniform boundedness of these cutoff masses is one sufficient way to meet (10).

Conversely, if the detecting pairing has absolute value \(d>0\), then every such \(O\) with \(\omega_g(O)>0\) satisfies
\[
 \mathcal C_{T,\alpha}(S;O)\geq d/\omega_g(O).\tag{11}
\]
No such neighborhood can have \(\omega_g(O)=0\). Consequently if \(h=g\) on \(S\), every sequence of neighborhoods with \(\omega_g(O_j)\to0\) has cutoff masses tending to infinity for a nonzero detecting pairing.

Proof. For any admissible competitor, (5) bounds the pairing by \(\omega_g(O)\langle T,\eta\rangle\). The oscillation is finite by continuity and relative compactness. Taking the infimum over competitors proves (9), without assuming that the infimum is attained. If the oscillation is zero, (9) gives zero outright. Otherwise division by that positive number proves (11). These facts prove (10) and the converse assertion. If \(h=g\) on the compact set \(S\), small-oscillation neighborhoods exist: intersect a relatively compact neighborhood of \(S\) with \(\{|h-g|<\varepsilon\}\). Compactness and local compactness allow this at every positive \(\varepsilon\). What is not automatic is the needed bound on their cutoff masses.

Constants are smooth zero-Hessian reference functions. Thus the same result applies when \(h\) has a locally constant trace along the locus, using a finite ordinary localization of each compact test if different constants occur on different local pieces. More generally a local smooth harmonic extension of the trace suffices, with the corresponding cutoff bounds on each ordinary neighborhood.

## Corollary 8: the ordinary local conclusion

Let a specified ordinary open \(W\) have an ordinary cover \((N_a)\). Suppose that on each member the off-locus hypothesis of Theorem 5 and its weighted vanishing conclusion (7), or (10) for every detecting test, hold for \(h|_{N_a}\) and \(T|_{N_a}\). Then \(D(hT)=0\) on \(W\).

Proof. Corollary 6 or Theorem 7 gives zero on each member. Ordinary restriction commutes with differentiation and continuous multiplication. The current sheaf property, or a finite smooth localization of each compact test, gives zero on \(W\). This glues already established identities of the original current. It does not glue approximating currents or turn the cover into an ordinary-open basis.
