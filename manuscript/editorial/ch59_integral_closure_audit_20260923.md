# Chapter 59 integral-closure comparison audit

Date: 23 September 2026.
Scope: the integral-closure block in Chapter 59, from the definition
through the example preceding the valuation/semivaluation warning.
Baseline: commit `16e52777adcfce84f09c1bfcaee95a1ee1152bdf`.

## Mathematical repair

The former proof applied a character of the semiring of global coherent
ideals directly to a local holomorphic germ. No such action had been
constructed. The normalized-blowup formula also omitted the nonzero-ideal
condition and its analytic source; the divisorial converse was only named.

The revised proof uses a global identity of coherent ideals. If
j is the integral closure of a, integral equations with coefficients
c_i in a^i make O[jT] finite over O[aT] locally. Homogeneous module
generators give j^(N+1)=a j^N, and compactness makes one N work on X.
If v(j) is infinite, ideal inclusion forces v(a) to be infinite. If
v(j) is finite, the identity makes both sides finite before cancellation.
This extends the explicitly cited full-support statement to all ideal
semivaluations, including proper support. It is a formal book-level
deduction with its proof displayed, not a claimed new research result.
The zero ideal is handled separately on the reduced space.

The analytic integral-dependence theorem gives the normalized-blowup
pushforward formula, including coherence. Normality of X identifies
the pushforward of O_Y with O_X. The same formula works on any normal
proper principalization, which is used in the example. The pulled-back
Cartier divisor need not be exceptional; an invertible ideal has the
identity as its blowup. The zero ideal is excluded from the construction.

For a nonzero ideal b, write b O_Y=O_Y(-sum b_i E_i) on its normalized
blowup. Compactness gives finitely many components. The inequalities
ord_Ei(a)>=b_i imply that each local generator divided by a Cartier
equation has no codimension-one pole. Normality then gives holomorphicity,
and pushforward gives a contained in the integral closure of b. The
proof uses the generic order of a coherent ideal along every local
branch, without assuming that a globally irreducible divisor is locally
irreducible. Idempotence gives the criterion for inclusion of closures.
The reverse implication uses value invariance and ideal order reversal.
Unit ideals, zero ideals, the trivial valuation and dimension zero are
explicit. No later divisorial-density theorem is used.

## Worked cases and second pass

On P2, the global image ideal of O(-2)^2 -> O defined by X0^2,X1^2
has stalk (x^2,y^2) at p=[0:0:1] and is the unit ideal elsewhere.
The two blowup charts give its pullback O(-2E), the same as that of
I_p^2. Taylor order computes the pushforward as I_p^2. The missing
generator xy satisfies an integral equation, and (I_p^2)^2=a I_p^2
is an exact reduction identity. The point-supported character takes
infinite values, so the example also checks the noncancellation case.

Divisors on P2 itself cannot distinguish I_p from I_p^2, whereas E
does. Conversely, O(-p) and O(-2p) on P1 are distinct integrally
closed invertible ideals detected by a nonexceptional divisor; normal
birational curve modifications have no exceptional divisors. These
examples delimit both possible restrictions of the divisorial test.

After the first complete draft, build and page inspection, a second
local pass reread all hypotheses, integral equations, graded-module
degrees, the compactness step, extended arithmetic, the two inclusions,
normality, and both examples. It added the generic-order justification
for local branches and clarified that the coherent-ideal statement is
deduced from the source's local analytic criterion. All changed TeX,
citations and rendered pages were checked again after these edits.

## Exact primary sources

- Lejeune-Jalabert and Teissier, *Cloture integrale des ideaux et
  equisingularite*, Ann. Fac. Sci. Toulouse Math. (6) 17 (2008),
  no. 4, 781--859, [DOI 10.5802/afst.1203](https://www.numdam.org/articles/10.5802/afst.1203/).
  The published article was read: Theorem 2.1(iv)--(v), p. 799;
  Theorem 2.9 and its proof, pp. 804--805; Proposition 2.11, p. 805;
  Sections 4.1--4.5 and Theorem 4.6, pp. 811--812; Proposition 4.8,
  p. 813. Physical PDF pages 20, 25, 26, 33 and 34 were rendered and
  visually checked. The proof uses the normal analytic local-ring
  criterion, not an unsupported replacement by an algebraic blowup.
  The [publisher PDF](https://afst.centre-mersenne.org/article/AFST_2008_6_17_4_781_0.pdf)
  has SHA-256 `b142813da04a8bc26c0d0aee84cc5198c1f1366a85d77e6baa500d90a26972fd`.
  MathSciNet access was unavailable; the primary Numdam record supplies
  the publication metadata and MR2499856. The new LejeuneTeissier08
  entry preserves the compound surname with label LJT and the project's
  BibTeX-compatible shorthand LJT08. The rendered citation was checked.
- Mesquita-Piccione, [arXiv:2409.06221v2](https://arxiv.org/abs/2409.06221v2),
  18 September 2025, Section 2.2, p. 14: Proposition 2.2.2,
  Corollary 2.2.3 and Lemma 2.2.4. The latter states value invariance on full-support
  valuations. Its exact-version MPTropicalV2 citation is retained;
  the extension to infinite values is proved in this unit. The displayed
  coefficient condition in the source's Definition 2.2.1 is not copied:
  integral dependence here uses c_i in a^i, as in Appendix A and Tag 00H3.
  The author PDF SHA-256 is
  `9eb2ea7686a5962ebc11c5eacd23b0cb3dcb081e27ac48292933f291fc82cb23`.
  The published MP24 entry remains unchanged. Direct publisher full-text
  access failed, so no inspection of its typeset theorem locators is claimed.
- [Stacks Project, Tag 00H3](https://stacks.math.columbia.edu/tag/00H3),
  Lemma 10.38.2: the integral-equation/Rees-algebra translation.
  [Tag 031T](https://stacks.math.columbia.edu/tag/031T), Lemma 10.157.6:
  a noetherian normal domain is the intersection of its height-one
  localizations. Both statements and their proofs were read directly.

## Validation and preservation

The final full build passes: 3,949 pages, 18,779,424 bytes, 389 TeX
inputs and 11,577 unique labels. There are no missing inputs, duplicate
labels, dangling references, unresolved citations, or horizontal or
vertical overflows. `git diff --check` passes.

The strict style audit of the entire changed TeX block returns zero
errors and zero warnings. The bibliography-aware audit additionally
flags the known MPTropicalV2 preprint entry; the exact-version and
publisher-access review above records the reason for retaining it.
All citations resolve in the full build. Pre-existing underfull-box
and class warnings remain. The build is not a mathematical verifier.

The first and final builds were inspected on physical pages 3310--3314
(printed 3242--3246), including both section boundaries, and the new
bibliography entry on physical page 3946 (printed 3878).

The chapter prefix and suffix outside this unit are byte-identical to
the baseline, as is Chapter 58. All pre-existing bibliography bytes
are retained as a prefix. The inventory remains 46 active atoms in
14 formal environments, tiers `(0,5,8,16,17)`. The supplied CURVE_PSH.tex,
author sources, frozen proofs, verifier receipts and dated releases
are unchanged. No independent-agent or production verification and
no research-atom closure are claimed. The generated live PDF is
ignored and is not a release artifact or part of the Git commit.

SHA-256:

- Chapter 59: `d34916f6478297290854744bf0caf355fc177d892d8592992cdce1ebaa85c392`.
- Bibliography: `f77736549ed82a38bc6db488b2527629b2cb2ebf5b47475f3c94e08e0e068219`.
- Generated live PDF: `6dfdec73ec60661758f6da1e9d4b1653f04db6ac00ac9bda9c118665f7594558`.
- Supplied and restored CURVE_PSH.tex: `9142aac73c5af7e4e715b3313def5ed56fae4e63e1ac8a53d0419df7d2194be9`.

Next bounded unit: Chapter 59's monomial valuations, especially
adapted-coordinate independence, globalization from a stratum,
zero weights and rational divisorial realization. Check the proof
and source scope before using these assertions downstream.
