# Analytic dimension removability

## Theorem 9: a degree-specific analytic exceptional locus

Fix an ordinary open \(W\) in the original ambient space, \(p\in\{0,\ldots,n-1\}\), and \(r=n-p-1\). Let \(Z\subset W\) be ordinary closed. Assume that locally on \(W\), \(Z\) is a closed analytic locus of dimension strictly less than \(r\). Let \(h\) be continuous on \(W\) and ordinary CLD-smooth with zero smooth Hessian on \(W\setminus Z\). Then for every positive doubly closed ordinary current \(T\) of bidegree \((p,p)\) on \(W\),
\[
 D(hT)=0.\tag{12}
\]
In particular this proves the desired Bedford--Taylor equality for any separately admissible continuous psh pair \(U,V\) whose difference has these additional properties. It imposes no approximation, laminarity or prescribed factor hypothesis on \(T\).

Proof. Lemma 4 gives \(\operatorname{supp}D(hT)\subset Z\). On a neighborhood where the analytic locus has dimension less than \(r\), every compact smooth test \(\alpha\) of degree \((r,r)\) has support disjoint from that locus, by the exact CLD 15.2.1(b) support principle. Thus its pairing with \(D(hT)\) is zero by the current support definition. All tests of the complementary degree vanish against the defect, so that current is zero on the neighborhood. The ordinary sheaf property proves (12) on \(W\). Alternatively localizing a given compact test into finitely many such neighborhoods gives the same proof. No positivity or order-zero property of the differentiated defect is needed.

The same proof works for any ordinary closed \(Z\) with the pointwise condition \(d_K(z)<r\) for every \(z\in Z\), using CLD 15.2.1(a). This alternative is a condition on the original analytic points, not a claim about a projected fan.

When the locus is of pure analytic codimension \(c\), the sufficient integer bound is \(c\geq p+2\). More generally use its local analytic dimension bound directly. For \(n=2\), the case \(p=0\) permits zero-dimensional analytic loci and \(p=1\) permits no nonempty analytic locus. For \(n=3\), the bounds are dimension at most one for \(p=0\), at most zero for \(p=1\), and no nonempty locus for \(p=2\). At every dimension, the top allowed degree \(p=n-1\) has scalar detecting tests and receives no nonempty-locus conclusion from this argument.

## Corollary 10: a necessary location for a defect and a dimensional window

Assume only that \(Z\) is ordinary closed and \(h\) is continuous and ordinary smooth with zero smooth Hessian off \(Z\), without imposing Theorem 9's dimension inequality. If \(D(hT)\ne0\), it has a compact smooth detecting test whose support meets \(Z\) at a point \(z\) with \(d_K(z)\geq n-p-1\). For an analytic locus with a uniform local dimension bound, that bound cannot be strictly less than \(n-p-1\).

Proof. A nonzero current has a compact detecting test by its definition as a nonzero functional. Symmetry permits its symmetric part. Its pairing cannot be nonzero if its support is disjoint from \(Z\). CLD 15.2.1(a) says every point in the support of this \((r,r)\)-test has \(d_K\geq r\). This proves the assertion, with all tests on the actual analytic domain.

For comparison, suppose only that the closed analytic locus has dimension less than \(n-1\). The canonical integration current \(\delta_X|_W\) is positive and doubly closed by CLD 7.3.1 and 7.7.4, so Theorem 9 applied with \(p=0\) proves \(D[h]=0\). This observation keeps its actual nonreduced integration weights. It does not say that \(h\) or \(-h\) is psh, or that a separately admissible pair exists with difference \(h\).

For \(p\geq1\), the inequalities
\[
 n-p-1\leq\dim Z<n-1
\]
therefore describe a remaining dimensional window in this particular off-locus route: canonical nullity follows, while dimensional support alone does not settle the multiplier equation in degree \(p\). This is a window of unexcluded possibilities, not a construction of a defect. For \(p=0\) there is no such window. For general ordinary closed gluing loci neither inequality is substituted for the pointwise analytic statement without proof.
