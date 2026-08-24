# Part IV post-expansion correction note (24 August 2026)

## Chapter 46: vertical-factor BFJ energy

The Chapter 46 comparisons with the discretely valued BFJ theory now use
only the mixed vertical energy difference

\[
 E_\omega(\varphi)-E_\omega(\psi)
 =\frac1{n+1}\sum_{j=0}^n
  (D_{\varphi-\psi}\cdot\omega_\varphi^j\cdot\omega_\psi^{n-j}),
\]

with an actual vertical divisor in the first slot.  The correction covers
the Part III comparison table, the telescoping remark, the two-vertex
discretely valued example, and the historical note.  Absolute
\((n+1)\)-fold powers are retained only for compactified test configurations,
where they are genuine projective intersection numbers in a distinct
framework.  No excluded-source citation or dependency was introduced.

## Chapters 36--45: envelope, reflection, and descent audit

The Part IV connection chain was checked against the supplied envelope
manuscript, the stated results of Boucksom--Jonsson, and the published
addendum.  The following scope and normalization repairs were made.

- Chapter 36 now states the generic-finiteness/nontriviality condition on
  decreasing psh limits, separates the smooth arbitrary-class theorem from
  the addendum's weak-envelope energy identity, and identifies the latter as
  the trivially valued Boucksom--Jonsson energy.
- Chapter 37 no longer claims that a non-nef class has empty psh space or
  that a nonempty psh family forces nefness.  The valid implication is
  nonempty psh family implies pseudoeffective class; bounded psh functions
  are the ones that force nefness.
- Chapters 38--39 now keep the bounded-PL/fixed-class convention separate
  from generically finite, varying-class regularization.  Their BFJ09 use is
  explicitly limited to b-divisor formalism and ordinary intersection on
  projective models.  The claim that arbitrary psh functions are finite on
  all full-support valuations was removed; BJ22 Corollary 4.17 only supplies
  finiteness on the linear-growth locus.
- Chapter 41 retains the determinant-norm normalization
  \(1/(md)\), the fibre average \(d^{-1}\sum e(w/z)\varphi(w)\), and
  \(\sum e(w/z)=d\).  Its discussion of fixed-class approximation no longer
  infers nefness without the bounded-PL hypothesis.
- Chapter 42's Frobenius example now uses the relative Frobenius
  \(F_{X/k}:X\to X^{(p)}\).  The absolute Frobenius is not silently treated
  as a \(k\)-morphism, and no unjustified identification \(X^{(p)}\simeq X\)
  is made.
- Chapter 43 no longer infers pseudoeffectivity equivalences from the
  one-way psh-existence lemma.  A false separable extension example over
  \(\mathbf F_p(s)\) was replaced by the correct one-point field-extension
  example, and the repeated downstream reference was repaired.
- Chapter 44 qualifies transport of decreasing limits by the usual
  nontriviality condition and no longer lists energy as a formal consequence
  of pointwise psh reflection; energy needs a separate comparison theorem.
- Chapter 45 replaces all uses of
  `psh nonempty iff pseudoeffective' by the proved one-way implication,
  adds the missing nonempty-competitor hypothesis to the obstacle
  trichotomy, restricts the general psh finiteness statement to
  \(X^{\mathrm{lin}}\), and replaces the asserted lattice structure by
  conditional joins and meets.  Joins require a constant upper bound and
  meets require a psh lower bound.

No absolute \((n+1)\)-fold pairing of discretely valued BFJ model forms is
used in Chapters 36--45.  The only energy formula in this range is the
separate trivially valued Boucksom--Jonsson addendum identity; the Chapter 38
intersection calculations are ordinary projective-model intersections.

The source audit used BJ22 Theorem 4.22 and Corollaries 4.17 and 4.23 for
comparison and finiteness, Theorems 5.11, 5.12, and 5.20 for the envelope
equivalences, unibranch necessity, and the smooth theorem, and the addendum's
Theorems A and B with their stated smoothness/characteristic and weak-envelope
hypotheses.  The full envelope theorem and the normalization descent remain
anchored to the supplied envelope manuscript; this is the principal
provenance boundary and was not promoted to an independently published
result.  No use was made of Mingchen Xia's excluded
Deligne--Riemann--Roch paper arXiv:1710.09731.

A full `latexmk` run traversed Chapters 36--45 without a TeX error and found
no duplicate labels or undefined references in this range.  The global run
then stopped in untouched Chapter 47 at line 1932 on an unrelated malformed
control sequence, so it does not certify the later chapters.  Chapter 46 was
not edited in this audit.
