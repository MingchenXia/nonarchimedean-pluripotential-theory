# Yang Li canonical-basis source audit — 4 October 2026

All 2,912 extracted text lines of arXiv:2505.11087v1, *Degeneration of
Calabi–Yau metrics and canonical basis*, were freshly read, including the
complete proof, conditional transport discussion and references. Twenty
selected actual PDF pages (3, 14–17, 20–34) were viewed. This is complete
source reading with scoped proof counterchecks, not certification of every
imported dependency or an independent model-verifier verdict. The identifier
query returns v1, submitted 16 May 2025; the PDF header dates the manuscript
1 June 2025. No journal version was identified by that bounded metadata check.

Theorem 1.2 asserts Conjecture 1.1 for polarized meromorphic degenerations
of smooth projective Calabi–Yau manifolds with a nowhere-vanishing volume
form and essential dimension 1 through n. Its potential/metric convergence
claim does not assume the canonical basis used in the later transport part.
Theorem 5.13 does require all the Section 5.1 basis, central-fibre,
indexing, multiplication and maximal-essential-dimension assumptions.
Theorem 5.15 treats a specific intermediate-degeneration hypersurface family
with a weighted measure. Sections 3.6 and 6 retain theta independence,
metric SYZ and mirror cost reciprocity as questions or proposed routes.
None is relabelled solved here.

A literal issue appears in the Section 3.3 multigraded construction. The
source says the componentwise order `mu' > mu` means nonnegative differences
excluding equality. Interpret the quotient denominator as the natural sum
of the indicated submodules. In the common-basis setting explicitly used in
Remark 3.13, let \(m_i=\max_k\mu_{i,k}\). Then

\[
 F_\mu=\bigoplus_i t^{m_i}\mathbf C[[t]]\,\theta_i.
\]

Increase the entries with first index \(i\) by one, obtaining \(\mu^{(i)}>\mu\).
If there are at least two basis vectors, then for \(i\ne j\),

\[
 F_{\mu^{(i)}}+F_{\mu^{(j)}}=F_\mu.
\]

Each summand contains every other basis direction, so the equality is exact.
Thus every printed graded quotient is zero in this case. Lifting its basis
cannot produce the generators claimed in Lemma 3.11. The direct-sum symbol
in the printed quotient also requires an image map; using that image still
gives the collapse above. This is an auxiliary-construction countercheck,
not a counterexample to the main Calabi–Yau continuity claim.

The dependency runs through Lemma 3.11 and Corollary 3.17 into the upper
Fubini–Study estimate, Proposition 4.9. There is a possible elementary bypass:
use the finite set of columns of meromorphic inverse constraint matrices
suggested already in Corollary 3.16. The next research step is a complete
independent determinant-based construction with uniform constants. It is
not yet admitted as a repaired book proof.

The actual PDF also confirms three local proof issues. On pages 25–26,
`sum_(i=0)^m x_i=1` follows from the chart equation, while the printed good
region requires `1-sum_(i=0)^m x_i` to be positive. The intended sum must omit
the dependent coordinate. Lemma 4.3's global comparison metric is attributed
to the unresolved `[?, Prop. 3.1]`; its exact source or construction is still
needed. On page 30, nonnegativity on the good region excludes a strict
negative set, but does not exclude the printed nonpositive set, which also
contains equality points. The intended strict comparison set and its uniform
estimate must be checked against the primary cited argument.

The active book remains at the checked 4,240-page edition. These findings
and proposed repairs stay outside it; no problem status, receipt or principal
theorem verdict changes. The [manifest](li_canonical_basis_source_manifest_20261004.json)
records exact primary hashes, read/visual scopes and the dependency route.
