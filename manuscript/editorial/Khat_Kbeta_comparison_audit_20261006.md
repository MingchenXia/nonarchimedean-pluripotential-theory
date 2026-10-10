# Ordered model estimates and quantized stability comparison

Date: 6 October 2026. Baseline work commit
`cd02d18c45b34d81f0b4c8cc815c1ab4df38c173`; baseline `origin/main`
`00957114db21b627e97369563032ceda9cea09c7`.

## Reading route and admission scope

Chapter 46 now explains the ordered square-root estimate for variation of
normalized energy with the polarization. It follows the general PL operations
and precedes the worked curve models and decreasing extension, making its
finite intersection scope visible. Chapter 68 uses that calculation to explain the conditional
comparison between the non-Archimedean and quantized Mabuchi functionals.
It states big-model approximation and entropy convergence separately.
Appendix L records the controlling versions, exact locators, normalization
repairs and limits of this dependency review.

The additions import known results and explanatory deductions. They contain
no new formal theorem, proposition, lemma, corollary, definition, example,
remark or proof environment. No original mathematical result, priority
claim, independent model call or new verification receipt is asserted.
The user's `gpt-6.1-sol xhigh` original-result preference is retained;
this known-result import does not invoke that gate or extend older receipts.

## Controlling main source

Theodoros Stylianos Papazachariou, *An algebraic comparison of K-hat-stability
and K-beta-stability*, arXiv:2609.15333v1, submitted 14 September 2026 at
10:20:51 UTC, primary subject math.AG. All twenty-five actual pages of the
446734-byte PDF were read and displayed, including proofs and bibliography.
The official comments say twenty-six pages; the actual acquired count is
twenty-five. PDF SHA-256:
`61efd58ffe1676a5eb0603767b4ee1574a596472236af37123527c830f59a05d`.
Extracted-text SHA-256:
`eef3570ba3e88a19279a07b2146ba02a4720f55d95a9dc15dda9dc9302e54993`.
The frozen full reading record is
`source_material/Khat_Kbeta_comparison_20261006/full_reading_v1_20261006.json`,
SHA-256 `32bcddf5749b84d8b7a464273f807c17c1e4ea0197b1ae3929920384bd7411d8`.
Historical acquisition/admission flags are not rewritten into clearance.

Load-bearing locators in this version:

- Definition 3.2 and Lemma 3.3, pages 12–13: discrepancy obstacle,
  model independence and ordering; common supremum normalization on 13.
- Lemma 3.4, pages 14–15: mixed vertical Hodge control, including the
  separate one-dimensional computation.
- Theorem 3.5, pages 15–17: ordered polarization estimate. Only its PL
  case is admitted with a finite intersection argument in Chapter 46.
  The big-model passage remains a separate input in Chapter 68.
- Corollary 3.6, page 17: linear control at a PL model potential.
- Lemmas 3.7–3.8, Proposition 3.9 and Theorem 3.10, page 18: ordered
  energy identity, entropy inequality, extra entropy approximation, and
  comparison of Mabuchi functionals.
- Corollary 3.11, page 19: uniform loss of order beta to the power minus
  one half, with a low-energy branch and a separate constant-potential case.

The full stability equivalences, reduced equivariant comparison and limiting
threshold results in Section 4 were read, but are not promoted to unrestricted
book theorems. Singular extensions and the ordinary K-polystability example
mentioned in the introduction are not imported.

## Selected dependencies

Thirty-two actual pages from four exact files were read and displayed in
sixteen sheets. Together with the main paper this gives fifty-seven freshly
displayed source pages. The frozen selected record is
`source_material/Khat_Kbeta_dependencies_20261006/selected_reading_v1_20261006.json`,
SHA-256 `8b1130410e26c84d5f0aa86442c8cbd8fb05847b63c4be72229c82038661bcd0`.
This is not a fresh full reading of any dependency.

BJ22's published PDF was reused by exact bytes. Twelve actual pages were
inspected: 1, 55–60 and 108–112. The institutional cover means actual page
60 is printed 705. It contains Corollary 3.34, with exponent `2^(1-n)`.
Definitions 3.28–3.29 and vertical negativity were checked on the preceding
pages. The one-dimensional case is proved separately, avoiding the averaging
denominator `n-1` in the corollary's proof. The mixed measure convention in
Theorem 7.18 and Corollary 7.19 was checked on the later selected pages.
None of these PL estimates invokes Theorem 6.21.

Darvas–Zhang's arXiv:2509.15173v2, revised 3 November 2025, was reused by
exact bytes and inspected on actual 39–43. Equation (62) removes the central
twist from ordinary global volume; Lemma 9.1 and Remark 9.2 give model
independence and the discrepancy obstacle; Proposition 9.4 supplies the
energy identity. Corollary 9.6's statement writes an intersection entropy
without a volume divisor, while its proof has `V Ent_beta` on the left.
The book's probability normalization requires `1/V` on the intersection
entropy. Its upstream analytic and positive-product dependencies have not
been newly audited in full. Lemma 9.3 uses complex Siu decomposition, which
must not be confused with the disputed non-Archimedean BJ22 argument.

Trusiani's arXiv:2605.30063v2, dated 17 August 2026, was reused by exact
bytes and inspected on 1–6 and 16–19. Corollary A is an additional entropy
convergence input, proved via Special Fujita approximation. The core
approximation proof on the intervening pages and the complete Laurent-series
appendix are not claimed freshly closed. The existing dated Chapter 68
remark and status proposition are byte-preserved. This review authenticates
the selected locators and their role, without upgrading the full YTD claim.

Boucksom–Jonsson's arXiv:2206.09492v3, revised 30 August 2023, was acquired
and checked on 1 and 16–19. It has forty-seven actual pages, distinct from
the fifty-three-page published Crelle article. Lemma 2.4 and equation (2.6)
are on 17; Lemma 2.8 is on 18. A new version-specific bibliography key
preserves the existing published entry. The polarization derivative has a
volume trace correction; the general Holder estimate has a different
signature from the ordered square-root estimate.

## Mathematical checks and boundaries

The ambient signature is smooth complex projective, dimension at least one,
ample rational polarization and positive volume. The potentials in the
unconditional finite calculation are semipositive PL models, ordered and
normalized by the same supremum. Intersections are raw quantities of mass
`V`; probability integral expressions carry the compensating `V`.
The main paper's Lemma 3.4 integral notation omits that factor relative to
its probability convention. The final estimates are unaffected when the
intersection and integral conventions are matched.

The derivative includes the trace correction from differentiating volume.
The mixed Hodge form has vertical entries; no horizontal Hodge inequality
is claimed. Its maximum quantity is not `d_1`. The telescoping difference
is nonnegative and at most the lower potential's `J`. The curve test uses
`E=-c^2/(2d)` and gives derivative `c^2/(2d^2)` when `d` varies with the
model potential held fixed.

The discrepancy obstacle is not assumed semipositive. Its envelope and its
translation-normalized positive product are used explicitly. The relative
volume subtracts `c(n+1)V`; plain global volume would define a different
functional. The lower-bound transfer to a big model needs entropy convergence.
Lower semicontinuity supplies the opposite limiting inequality and is
insufficient for that transfer.

The norm is distance to constants, with Lipschitz control, rather than
distance to the zero potential. The uniform-error deduction assumes a
nonnegative lower-bound coefficient and displays every approximation input.
The constant-potential case is separate. The only branch requiring a loss
estimate bounds its own energy gap; there is no unsupported global
entropy-to-J estimate over all test configurations. At coefficient zero,
the finite-beta lower bound may be negative and tend to zero. The reduced
functional's supremum over rational twists is distinguished from the norm's
infimum over real twists and from full-group radial coercivity.

No full Special Fujita or general big-model approximation closure, singular
or nonprojective YTD extension, positive-characteristic or zero-volume
transfer, general Siu/closure repair, or solution of a canonical open problem
is asserted. The separate toric entropy candidate remains open and outside
active TeX. The native open-problem editor and catalogue are untouched.

## Release checks

The accompanying integration manifest records the final build, navigation,
rendered-page review, exports and exact preservation gates. All 422 other
active TeX inputs, 108 protected inputs, 136 existing formal blocks in the
three edited TeX files, fifty prior frozen manifests and one hundred prior
exports retain their baseline bytes. There are twelve added labels, nine
equation tags, one index entry and two version-specific bibliography entries.
The forty-two canonical atomic statuses retain their complete earlier bytes.
The prior completed second reading remains the whole-book reading record;
this checkpoint adds a scoped review of the newly rendered material.

The first rendered review showed that the general ordered estimate was
nested under the projective-line example heading. Promoting it to a new
section caused a later long proposition heading to overflow by 3.62302pt.
The final placement is a subsection after the general PL operations and
before the curve examples, preserving existing section numbers. The first
two drafts/builds, the original gates and sixteen-page partial review,
and the overflow diagnostic are retained. The corrected third build and
its fresh page review control the release.
