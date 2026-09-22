# Chapter 60: the test-curve base point and mixed slopes — 22 September 2026

## Test-curve correspondence

The comparison theorem now fixes a Kähler representative omega and the
base point V_omega=0. The
[published DXZ paper](https://ems.press/content/serial-article-files/50355),
Section 3.4 and Theorem 3.17 on page 299, explicitly shows that a
finite-energy test curve has least singular limit V_omega. This page
was inspected in the published PDF, including formula (34).

The theorem displays the Legendre transform and its initial value
zero. Its energy integral is divided by V_beta, converting Chapter
52's relative energy to this chapter's probability normalization.
The identification with MP data remains the source comparison in
[MP24 arXiv version 2, Section 5.2](https://arxiv.org/html/2409.06221v2).
Changing the initial potential in the maximal-ray theorem is not an
unspecified choice in this zero-obstacle test-curve bijection.

## Quantitative slope passage

The full mixed-slope theorem remains imported from MP24 arXiv version
2, Theorem 5.3.4. The expanded calculation treats one approximated
finite-energy slot with fixed compatible psh inputs in the common
background omega. General PL reduction and iteration remain parts
of the imported theorem; no claim that an arbitrary PL function is a
difference of two functions in one fixed H(alpha) is introduced.

With common initial value zero, order and the affine energy identity
give d1(U_s,U^m_s)=s delta_m, where delta_m is the non-Archimedean
energy difference. The probability-normalized d1 is explicitly
distinguished from Appendix H's unnormalized relative metric.
Normalized averages have slope difference epsilon_m, the difference
of the two values at the trivial valuation.

Subtracting those averages adds an error multiplied by the absolute
cohomological intersection B=|integral eta_0 ... eta_(n-1)|. This
coefficient need not be one; the checked source suppresses it.
The imported normalized mixed-energy estimate then bounds the error by

C (s delta_m)^q (s+1)^(1-q) + B(a^m_s-a_s), with q=2^(-n).

The constant is independent of m and s. The book proves the needed
uniform growth directly from

0 <= J(U^m_s) <= a^1_s - E(U_s) = O(s+1).

After division by s, the limsup error is at most
C delta_m^q+B epsilon_m, which tends to zero. Combining this with
convergence of the model mixed slopes proves the stated interchange
in this case. Arbitrary background forms in a finite-energy slot
are handled by the exact pair identity
(eta,U)=(omega,U)+(eta-omega,0), rather than changing positivity
without accounting for the background. Dimension zero is treated
separately.

## Validation and limits

The second pass checked the zero base point, the nonpluripolar level
mass and volume factor, exact citation versions, the normalization of
d1 and averages, the intersection coefficient, uniformity in m,
ordered energy differences, the triangle-inequality limit, and the
zero-dimensional case. The complete new blocks pass the strict
writing audit with zero errors and zero warnings.

The final scoped build has 99 pages and no unresolved reference,
citation or overfull box. Physical pages 81–84 were rendered and
inspected. The full build succeeds with 3,405 pages, 17,997,335 bytes,
zero unresolved references or citations, 38 horizontal overflows and
zero vertical overflows.

The source closure has 389 TeX files and 11,481 unique labels, with
no missing input, duplicate, dangling reference or structural defect.
The inventory remains 46 active atoms in 14 environments with tiers
(0,5,8,16,17); no research question is retired.

PDF SHA-256:
`9f42259df94d9df163a3ee125b9096506e88fef97a1958d2a90cf70522cae605`

Chapter 60 SHA-256:
`ea0896c28753fe6e9a4ca72bdaf291b62c38e7425b4872ac04205f6bb54f1afa`

Chapter 60 is the only production source changed since aca68a4.
The next mathematical check concerns the reduced-discrepancy entropy
slope, whose compatibility and integrability steps are still marked
as unverified in the book. The existing warning remains unchanged.

