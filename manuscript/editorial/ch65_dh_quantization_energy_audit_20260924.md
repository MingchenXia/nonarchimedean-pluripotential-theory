# Chapters 64 and 65: DH quantization and energy — 24 September 2026

## Scope and baseline

Baseline: `f2fee718d090b515b3156cd7c61bc190477fbc20`. The live checkout
was clean and matched the designated origin at the initial fetch.
Drafting, all full builds and PDF inspection used a separate export.
This unit repairs the filtered-volume/analytic-mass bridge, the DH
comparison and the energy first-moment formulas. The dependent algebraic
DH proof in Chapter 64 is corrected as well. It does not complete the
Chapter 65 analytic commutative-diagram or BHJ19 slope review. No research
atom is promoted and no independent-agent or production-verifier verdict
is claimed.

## Proof and normalization changes

For each interior level tau<c, choose a section s of degree a and slope
sigma>tau, and a rational 0<rho<1 with

    (1-rho) sigma + rho C_- > tau.

Set k_m=floor((1-rho)m/a) and r_m=m-a k_m. Multiplicativity embeds
s^(k_m) H0(r_m L) in the filtered degree-m piece for every sufficiently
large admissible m. The complete residual series embeds X, so the filtered
Kodaira maps are birational. In divisible degrees this also supplies an
ample-series decomposition. It gives positive volume at least rho^n V.

On a resolution of the degree-m base ideal, the moving part A_m is globally
generated. The partial sup-norm obstacle has the same bounded-difference
singularity type as a logarithmic basis sum, and its non-pluripolar mass
is (A_m^n)/m^n. Birational Fujita approximation computes the volume limit.
The increasing degrees m_j=m_0 j! are cofinal for divisibility; the obstacles
have a common analytic lower bound and are locally bounded off its base
locus. Bedford--Taylor convergence on that complement, exhaustion and
mass monotonicity identify the equilibrium mass with the moving-volume
limit. The established ample maximality identifies the equilibrium with
the test-curve level. The precise DXZ I-envelope lemma supplies the
I-model property; it is an explicit imported analytic input.

A degree-q finite cover of P1, with L=O(q), shows why positive volume
alone is insufficient: the pullback series has dimension m+1 and volume
one, but its bounded equilibrium has mass q. This isolates the missing
birationality hypothesis.

The DH comparison now uses every interior tail: normalized dimensions
converge to M(tau)/V, and Chapter 64's I-model tail theorem computes the
same analytic tails. Equality of total masses is no longer used as a
substitute for equality of distributions. Compact support implies moment
convergence. The test-configuration identification uses BHJ Proposition
5.9, with the Veronese dilation removed by dividing by actual L-degree.
The endpoint atom is M(c-)/V, not a raw terminal-series volume.

The monomial weights min(j,bm)-1 on P1 are multiplicative and linearly
bounded, with unit weight zero. Their cutoff is b, but every positive-
degree piece at level b is zero. Nevertheless the limiting probability
measure has density one on (0,b) and atom (1-b) at b. Its mean is
b-b^2/2; at b=1/2 the atom is 1/2 and the mean 3/8. Finite terminal tails
are all zero, so weak convergence cannot be evaluated there as though
the limit had no atom. The zero-dimensional case is treated separately
by Fekete's lemma and the measure delta_c.

The energy is normalized by E(0)=0, with E^u=V E and the established
squared-norm time. Since the Legendre ray is bounded at every finite
time, finite energy is automatic in this setting. The RWN energy identity
and layer cake give, for every t>0,

    E^u(ell_t)/t = integral lambda dDH_Gamma,
    E(ell_t)/t = lim_m sum_j lambda_mj/(m N_m).

The earlier statement only displayed radial limits. The compactified
intersection formula is reconstructed from the determinant degree of the
relative section bundle and the leading Euler characteristic. Relative
ampleness suffices; total-space ampleness is not assumed. This proves
E^u(ell_t)/t=(Lbar^(n+1))/(n+1), with the fixed linearization. Rational
character shifts and the point case are included. Chapter 64 now invokes
this independently proved spectral comparison and the precise BHJ
barycenter formula, without a circular dependence on its own conclusion.

## Primary sources and review passes

- [Boucksom--Chen, published article](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/F98F3E17336676C447FA72E9DB99CD8F/S0010437X11005355a.pdf/okounkov-bodies-of-filtered-linear-series.pdf):
  Definition 1.1 and equation (1.2), p. 1210; Lemma 1.6, p. 1212;
  Theorem 1.11 and Remark 1.12, pp. 1213--1214. Physical pages 8--11
  were visually checked, including the closed-superlevel distinction.
- [Hisamoto, published article](https://link.springer.com/content/pdf/10.1007/s00209-012-1133-6.pdf):
  Theorem 3, p. 234; Example 12, p. 237; Proposition 17 and Remark 18,
  pp. 238--239; equation (4.1), Proposition 19 and Remark 20, p. 240.
  Physical pages 2 and 5--8 were visually checked. The new His13 entry
  uses the published Math. Z. 275 (2013), 233--243 article and its DOI.
  MathSciNet was unavailable; publication metadata was checked against
  the publisher PDF. Published Theorem 3 replaces the preprint Theorem
  1.3 locator. The proof uses factorial, not merely dyadic, degrees.
- [Darvas--Xia--Zhang, published article](https://ems.press/content/serial-article-files/50355):
  Lemma 4.5 and Proposition 4.6, p. 302. Physical page 34 was visually
  checked. The existing DXZ23 bibliography key and published DXZ25 label
  are retained. The cited Hisamoto theorem is located in the publication
  itself, rather than copying the older numbering used in this source.
- [Ross--Witt Nyström, published article](https://archive.intlpress.com/site/pub/files/_fulltext/journals/jsg/2014/0012/0001/JSG-2014-0012-0001-a005.pdf):
  Proposition 6.7, pp. 151--152, equations (6.2)--(6.5). Physical pages
  27--28 were visually checked. The Riemann sums integrate M, not tau M;
  the extra factor printed in an intermediate line of (6.4) is not
  propagated. The stated identity and final integration by parts agree.
- [Boucksom--Hisamoto--Jonsson, published article](https://aif.centre-mersenne.org/item/10.5802/aif.3096.pdf):
  Corollary 3.4, p. 774; Proposition 3.12(iii), equation (3.3), and its
  proof, pp. 777--778; Proposition 5.9, p. 792. Physical pages 33,
  36--37 and 51 were visually checked. Central-fibre weights, determinant
  degrees, the volume denominator and the Veronese factor were compared.

The first pass reconstructed the interior volume/mass proof, the tail
comparison, both examples and the energy/intersection argument. After
its full build and PDF inspection, the second pass made the factorial
subsequence explicit, specified the degree-zero unit and positive-degree terminal vanishing, recalled the energy
section's notation locally, handled dimension zero before using the
positive-dimensional formula, and restricted the algebraic character
statement to rational shifts. The Chapter 64 citation now states exactly
the barycenter equality supplied by BHJ Proposition 3.12.

## Validation and preservation

All three full builds pass. The final PDF has 4,058 pages and 19,327,950 bytes.
Reference and structure checks find 396 inputs and 11,818 unique labels,
with no missing input, duplicate label or dangling reference. The open
problem inventory is unchanged: 43 atoms in 13 environments, with tiers
(0,3,8,15,17). The scoped house audits report zero errors and zero warnings.
The final build has no undefined reference/citation, rerun request or
horizontal/vertical overflow. Its 13 inherited Chapter 70 duplicate PDF
destination warnings remain.

Exact rational arithmetic checks covered 54,675 monomial multiplication
pairs for b=1/4,1/2,3/4 and degrees up to 15. Further calculations at
m=100,1000,10000 checked the interior tail and mean error bounds and the
zero finite terminal tail. Signed rational constant-product shifts checked
the (n+1)V intersection normalization. These are example checks, not a
substitute for the general proofs. Physical PDF pages 3503--3504,
3523--3529 and 4053 were inspected after both passes (10 pages each,
including the new bibliography entry).

Before current progress files were updated, all 4,173 tracked baseline
files except the two revised chapters and the bibliography were unchanged.
The six supplied integrations and original attachments, CURVE_PSH,
P12.1 material, research ledgers, frozen packets, verifier records and dated
releases remain byte-identical. Earlier Chapter 65 Rees/Bergman sections,
its analytic diagram, the finite-level moment examples, factor-two section
and BHJ19 quarantine are unchanged. The diagram and unaffected-slope proof
remain in the next review unit.

Only the two chapters, the bibliography and four current progress/audit
files are delivered. The PDF replaces only the ignored current
manuscript/book.pdf. Temporary source downloads, renderings, numerical
checks and build auxiliaries are not staged. A final fetch initially hit
a transient SSL connection error; its HTTP/1.1 retry succeeded.

Reproduce the source checks from manuscript/ with
`python3 editorial/tools/refcheck.py` and
`python3 editorial/tools/check_open_problem_inventory.py`.
Build with `latexmk -pdf -interaction=nonstopmode -halt-on-error book.tex`.

- `manuscript/book.pdf` SHA-256: `8558e46f6ee0c31868dad56c117a861902e15076ddf8de3b785b53bd5d887ed9`.

- `manuscript/parts/part6/ch64_compare_ma.tex` SHA-256: `d82d0d058c939165f714fe44d54df2c0eed2cdd0d3785b8860ac692ea17a34a5`.

- `manuscript/parts/part6/ch65_rays_filtrations.tex` SHA-256: `6c47d82547a2b0e5f0da17a8424512d5209e7efe047a907875e0e1b300698bb4`.

- `manuscript/bibliography/ComplexGeometry.bib` SHA-256: `8c4ad46d1221086565ff59b2aabd2b4a911dae5a0ba94f0528a4207ceca9507d`.
