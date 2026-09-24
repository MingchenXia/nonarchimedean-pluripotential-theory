# Chapters 52 and 65: filtered Bergman envelopes and closed endpoints — 24 September 2026

## Scope and baseline

Baseline: `1bd0fca72fc24c20303053ab25b58ef45dd4d0db`. The live checkout
was clean. A fresh fetch confirmed no divergence from the designated
origin; the final process and lock check found no competing build or Git
mutation. Drafting and both full builds used a separate export. This unit
repairs the ample filtered-section/test-curve construction, the Bergman
comparison and its projective-line examples. Chapter 52 receives the
necessary dependent endpoint and norm corrections. Its pre-existing
big-class I-model assertions are not a newly verified conclusion of this
unit. No research atom is promoted, and no independent-agent or
production-verifier verdict is claimed.

## Mathematical corrections

The setup now specifies connected projective X, ample L, a smooth positive
reference metric, and a decreasing, left-continuous, multiplicative,
linearly bounded filtration of the full section ring. A fixed smooth
probability volume form defines the L2 norm. A local mean-value argument
at radius m^(-1/2) proves

    ||s||_2^2 <= ||s||_infinity^2 <= C m^n ||s||_2^2.

The constant depends only on X, L, the metric and the volume form, not on
the filtration, level, time or section. The partial obstacles consequently
differ by at most epsilon_m=(log C+n log m)/m. Zero subspaces and common
zero loci are included explicitly.

Powers of sections show that every regularized degree tail has the same
supremum g_tau; factorial degrees form an increasing cofinal subsequence.
The same tail limit holds for the L2 partial obstacles by the uniform
norm bound. This does not assert convergence along every degree. Rational
convex combinations are realized by powers in a common degree, giving
concavity. Interior maximality remains an explicitly cited analytic
input, including the source's maximal-envelope fixed-point step.

The terminal parameter is c_F=sup chi_m(s)/m. The curve is defined by
P[g_tau] on tau<c_F and by its decreasing left limit at c_F. The earlier
closed-endpoint lemma supplies noncollapse and closure. The raw and
closed curves have the same forward Legendre transform, but the inverse
recovers the closed curve. Bounds C_- t <= ell_t <= c_F t prove convergence
to the zero reference and control the case tau>c_F.

Two scalar-weight filtrations on P1 separate the endpoint and degree
issues. Weights m-1 give g_1=-infinity but the closed value Gamma_1=0.
Weights 2 floor(m/2) give full even and zero odd pieces at tau=1, so the
partial obstacles alternate between zero and -infinity. Powers and tail
envelopes remain valid in both cases. Full-series obstacles are exactly
zero for the Fubini--Study reference, by powers of unit linear forms.

For weighted Bergman sums, the partial-sum bound and the bound on each
individual summand prove

    H_m,t^(2) <= Phi_m,t <= H_m,t^(2) + log N_m/m.

Conversion to the sup-norm Legendre maximum H_m,t costs epsilon_m as
well. The error is uniform in x, t>=0 and the filtration. An explicit
counterexample works in every degree: on P1 take
p=|x|^2/(|x|^2+|y|^2), dV=(p+1/2) omega_FS and all weights zero.
At p=0 the sup-norm maximum is zero, while the Bergman value is
m^(-1) log(2(m+1)(m+2)/(m+4)) > log(m+1)/m. The norm error cannot be
discarded even at arbitrarily large m.

The tail-envelope identification is now proved by two inequalities.
The upper bound is Phi_m,t <= ell_t+epsilon_m+log N_m/m. For the lower
bound, each fixed threshold gives Phi_m,t >= B_m,tau^(2)+t tau; take tails
first and only then take the parameter supremum. Endpoint closure and
t=0 are included. No interchange of a parameter supremum with an
asymptotic envelope is assumed. Volume-form independence follows from
the sup-norm construction.

The Phong--Sturm name is qualified by the fixed-linearization convention.
Subtracting the mean weight changes Phi_m,t by exactly -t bar_lambda_m.
The compactly supported spectral limit gives the centered ray
ell_t-t bar_lambda, uniformly as a scalar correction on compact time
intervals. Rescaling the basis by m^(-n/2) contributes -n log m/m.
These scalar corrections are separate from the existing radial
factor-of-two convention.

The projective-line example now uses the orthonormal basis
sqrt((m+1) binomial(m,j)) x^j y^(m-j). Its exact Bergman potential is
log(m+1)/m + log(1-p+exp(t)p), with a constant error for every x and t.
The centered ray subtracts t/2. The unnormalized monomial sum in the
previous version had a different initial potential. The inverse curve
is computed by minimizing in time, including tau=1, tau>1, inactive
constraints tau<=p and p=0,1. It agrees with the existing hyperplane
example in Chapter 52.

## Primary sources and two review passes

- [Ross–Witt Nyström, published article](https://archive.intlpress.com/site/pub/files/_fulltext/journals/jsg/2014/0012/0001/JSG-2014-0012-0001-a005.pdf):
  proof of Proposition 6.10, equation (6.6), pp. 152--153;
  Lemmas 7.4 and 7.6 and Remark 7.5, pp. 154--156;
  Proposition 7.7, pp. 156--157;
  Proposition 7.11 and Corollary 7.12, pp. 158--160;
  Definition 9.1, p. 164; Lemma 9.3 and Theorem 9.2, pp. 165--166.
  The published PDF was downloaded and read. Physical pages 31--36 and
  41--42 were also visually inspected. The proof above uses the correct
  logarithmic cardinality error; it does not reproduce the missing
  logarithm in the printed equation (9.4). The degree-tail argument avoids
  an unrestricted all-degree pointwise Fekete assertion when zero pieces
  occur infinitely often.
- [Phong–Sturm, published article](https://archive.intlpress.com/site/pub/files/_fulltext/journals/jsg/2007/0005/0002/JSG-2007-0005-0002-a003.pdf):
  Theorem 1.1, pp. 222--223, gives the weak ray; Section 2.1, equation
  (2.1), p. 225, specifies the traceless generator; Section 4.2,
  pp. 237--238, specifies the basis rescaling. The publisher PDF's indexed
  text was checked. No local or visual PS source inspection is claimed.
  The book states the scalar centering calculation in its own weight
  sign and time convention rather than silently equating the raw formulas.

The first pass reconstructed the norm, concavity and two-sided envelope
arguments, supplied the endpoint counterexamples and corrected the
orthonormal P1 sum. The second pass reread the statements and proofs,
added the precise maximal-envelope locator, supplied the all-degree norm
counterexample, declared dimension locally, and distinguished fixed
linearization from trace-free normalization. Existing bibliography
entries and the BHJ19 erratum scope are retained.

Exact arithmetic checks cover 7,200 superadditivity pairs, 100 volume-norm
counterexamples, 900 binomial identities and 1,000 partial-sum inequalities
with ties, negative weights and zero summands. Separate floating-point
checks cover 261 inverse minima and 63 forward Legendre identities.
These checks test the examples and conventions, not the general proofs.

## Validation and preservation

Both review passes completed full-book builds. Final output: **4,054
pages**, **19,308,259 bytes**. The source closure has **396 inputs and 11,812
unique labels**, with no missing inputs, dangling references, duplicate
labels or per-file structure errors. The inventory remains **43 active
atoms in 13 environments**, tiers **(0,3,8,15,17)**. There are no unresolved
references/citations, rerun requests or horizontal/vertical overflows.
The 13 inherited Chapter 70 duplicate PDF destination warnings remain.
The scoped house audit has zero errors and zero warnings.

The first PDF pass covered physical pages 3236--3238, 3516--3521,
3523--3525 and 3528--3529 (14 pages). The final pass covered 3236--3238,
3516--3525 and 3529--3530 (15 pages), including changed proofs and
transitions. The final formulas and theorem/page breaks were reviewed.

Before progress records were updated, all 4,172 baseline tracked files
except the two revised chapters retained their exact bytes. The six
supplied proof integrations, original attachments, CURVE_PSH, P12.1
material, research ledgers, frozen packets, verifier records and dated
releases are unchanged. The preceding Rees unit, the radial factor-two
section and the BHJ19 erratum quarantine are byte-identical. Only the two
chapters and four current progress/audit files are delivered. The PDF
replaces only the ignored current manuscript/book.pdf; no build
auxiliaries, temporary checks or source downloads are staged.

From manuscript/, run `python3 editorial/tools/refcheck.py` and
`python3 editorial/tools/check_open_problem_inventory.py`.
Build with `latexmk -pdf -interaction=nonstopmode -halt-on-error book.tex`.

- `manuscript/book.pdf` SHA-256: `33954f07b74c46bc055dc537c6ab17dcd0cb5bfb91a5be8249ae319fd70b69a8`.

- `manuscript/parts/part5/ch52_rays_test_curves.tex` SHA-256: `cc006bccd85df684b263f999c102bfbccecbe8dc5d1bc85df961dd2231578afb`.

- `manuscript/parts/part6/ch65_rays_filtrations.tex` SHA-256: `c46c1d44efe776bbfbab6983095c99aee2b2685a87f3cb9647c2fe62abf41b11`.
