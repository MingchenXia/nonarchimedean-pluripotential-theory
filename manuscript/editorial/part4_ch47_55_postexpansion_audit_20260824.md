# Chapters 47--55 post-expansion mathematical audit (24 August 2026)

## 24 Aug 2026 controlling addendum

This dated audit is preserved below as the state before the author supplied
the TeX proof of Xia's Conjecture 8.8.  The later source and hostile audits
repaired the positive-Cao-volume/model-envelope reduction, both sandwich
arguments, the rational analytic-resolution step, the degenerate
finite-level case, multigraded irrelevant torsion, and the effective-shift
inclusion.  The exact repaired proof packet has SHA-256
`9227826d7ba5c641c5fe32cc4daae9acbb3b57274dcc1b356ba8beadd58cad7b`.
Production Rethlas (`gpt-5.6-sol`, `xhigh`) returned a final verdict of
`correct`, with zero critical errors and zero gaps.  The exact current metric
and line-bundle theorem blocks subsequently passed their own source-aware runs
`20260824T054849Z_57635bfa07f4` and
`20260824T061508Z_17bf73c6b37c`, each final `correct`, zero critical errors,
and zero gaps.  In the same audited range, the Chapter 49 truncation-energy
and sharpness package passed `20260824T041218Z_0c95825dbb06`, and the
source-attested Chapter 55 toric zero-mass block passed
`20260824T052605Z_703e3b501202`, with the same final zero/zero verdicts.  The controlling current
status is therefore: Conjecture 8.8 is proved in Chapter 55 for connected
smooth projective complex varieties, big line bundles, and singular psh
metrics of positive Cao/ideal-model volume, with the movable-product formula
as the minimal-singularity specialization.  The proof is author-supplied,
repaired, and verified, but unpublished.  Zero volume, transcendental
classes, singular varieties, and attainment of the valuation supremum remain
open.  Every contrary status sentence in the preserved audit below is
superseded by this addendum.

## Scope and framework firewall

This audit covers Chapters 47--50 in parts/part4 and Chapters 51--55 in
parts/part5. Chapters 20, 26, and 46 were read as normalization and
intersection-theory baselines but were not edited. No preamble or
bibliography file was edited.

The corrected framework distinction is enforced throughout. Over a
discretely valued field, the BFJ energy formalism uses an actual vertical
divisor in one slot and \(n\) relative closed-model classes in the remaining
slots; it does not supply an absolute \((n+1)\)-fold power of closed model
forms. Over a trivially valued field, the pair pairing of Chapter 46 is a
genuine absolute intersection pairing on a test configuration compactified
over \(\mathbf P^1\). Every \((n+1)\)-fold power retained in Chapters 47 and
50 belongs to this latter compactified setting. Cross-framework comparisons
now concern an algebraic proof pattern or a normalized numerical formula,
not an identification of the ambient pairings.

Mingchen Xia's erroneous Deligne-pairing paper arXiv:1710.09731 is excluded
completely. The audited chapters contain no citation, statement, or proof
traceable to it. Searches of the audited files and supplied local source
material found neither the identifier nor a Deligne-pairing dependency.

The separate item XiaMVOB is an unpublished July 2026 work in progress, not
that Deligne-pairing paper. It also lacks an independent published proof or
exact production Rethlas receipt. Chapter 55 therefore records its two
mixed-volume identities only as unverified source claims, does not treat
them as book theorems, does not use them in a deduction, and does not mark
Xia21, Conjecture 8.8 as verified or closed.

## Substantive corrections

### Chapter 47: finite-energy geometry and measures

- Corrected independent translation invariance to
  \(J_{\psi+b}(\phi+a)=J_\psi(\phi)\). The former affine correction term was
  false because the translations cancel in the definition.
- Added a binding explanation before the segment expansion: the displayed
  pair powers are Chapter 46 pair pairings and, for PL data, compactified
  test-configuration intersections over \(\mathbf P^1\); they are not DVR
  absolute powers. Related comparison and differentiability prose was
  narrowed to the common algebraic scheme in the two legal formalisms.
- Restored the probability-normalization factor on curves:
  \(I(\phi,\psi)=V^{-1}\langle\phi-\psi,\phi-\psi\rangle_{\mathrm D}\).
  The seminorm used in the quasi-triangle proof now carries the same
  \(V^{-1}\).
- Rechecked the previously interrupted block at source lines 1930--1937.
  Its unnormalized identity
  \(E^{\mathrm u}=\int\phi\,\MA^{\mathrm u}(0)
  -\frac12\langle\phi,\phi\rangle_{\mathrm D}\) and the ensuing normalized
  factor \(1/d\), \(d=\deg\omega\), are consistent; no further edit was
  required there.

### Chapter 48: strong topologies

- Normalized the curve Dirichlet bilinear form as
  \(\langle f,g\rangle=-V^{-1}\int f\,\ddc g\). Consequently the claimed
  identities \(I=\|\cdot\|^2\) and the measure-pairing sign now agree with
  Chapter 47.
- Replaced an imprecise density citation by the complete internal argument:
  decreasing PL approximation gives strong approximation of potentials;
  the bi-Lipschitz Monge--Ampère estimate gives strong convergence of their
  measures; and the PL measure formula makes those measures finitely
  supported and divisorial.
- Scoped the comparison example with Part III to its numerical
  correspondence, avoiding any suggestion that the ambient pairings are
  literally transported.

### Chapter 49: linear growth and toric geometry

- Corrected the topology summary: the weak topology is strictly coarser,
  while the strong topology and the measure-trace topology coincide. The
  dual-complex comparison is asserted only on the parts of faces bounded
  away from coordinate hyperplanes; no global boundary continuity is
  claimed.
- Replaced an impossible coordinatewise-from-below rational approximation
  of a normalized simplex point. Rational approximants are now chosen in
  the same minimal relative face with an explicit positive coordinate
  margin and sup-norm bound, after which the proved local Lipschitz estimate
  gives \(d_\infty<\varepsilon\).
- Adjusted every dependent dual-complex remark to use same-face density,
  not the false from-below normalization.
- Restricted the Part III toric comparison to separately defined and proved
  numerical formulae, with the normalization and reflection visible; no
  ambient model-intersection pairing is identified across bases.
- Repaired the irrational blowup example. It now uses the rational weight
  \((1,140/99)\), invokes the divisorial criterion for rational weights, and
  computes \(d_\infty=2|\sqrt2-140/99|<2\cdot10^{-4}\), rather than applying
  the invalid normalized-simplex approximation.

### Chapter 50: stability

- Replaced a cross-framework identification by a strict firewall: DVR
  energies use a vertical factor, whereas the Donaldson--Futaki and Mabuchi
  intersections in this chapter are compactified test-configuration
  intersections in the trivially valued setting.
- Replaced the false entropy-jump example by a valid sequence on
  \(\mathbf P^2\): for smooth degree-\(m\) curves \(C_m\), set
  \(v_m=m\ord_{C_m}\) and
  \(\nu_m=(1-m^{-1})\delta_{v_{\mathrm{triv}}}
  +m^{-1}\delta_{v_m}\). Then \(T(v_m)=1\), \(A(v_m)=m\),
  \(E^\vee(\nu_m)\le 2/(3m)\), and \(\nu_m\) converges in total variation to
  \(\delta_{v_{\mathrm{triv}}}\), while its entropy remains \(1\).
- Repaired nonclosedness of the finite-entropy locus. The proof no longer
  asserts unsupported convergence of dual energies. Instead it proves a
  uniform pairing estimate for the atomic tails using \(T(v_d)=1\), then
  applies the Chapter 48 strong-measure criterion.
- Reproved strong density of finite-entropy measures from decreasing PL
  approximation, strong Monge--Ampère continuity, surjectivity, and the PL
  divisorial measure formula. This replaces the imprecise valuation-density
  plus convex-combination argument.

### Chapters 51--54: prerequisites, rays, metrics, and operations

- Chapter 51 required no mathematical edit. Its hypotheses, source
  boundaries, and separation of \(P\)- and \(\mathcal I\)-singularity types
  are consistent.
- In Chapter 52, completed a broken explanatory sentence in the model
  supremum proof. The order on test curves now compares terminal parameters
  as well as all interior levels, with endpoint behavior supplied by the
  existing extended-curve convention. The former asymmetric condition did
  not compare curves with different terminal parameters.
- Chapter 53 required no mathematical edit. The positive-volume inverse
  system, recovery statement, zero-volume firewall, and bimeromorphic scope
  remain separated correctly.
- In Chapter 54, corrected the order definition to compare the two extended
  curves for every real level. This makes its advertised comparison of
  different terminal parameters true.

### Chapter 55: partial Okounkov bodies

- Reversed the multiplier-ideal inclusion to the subadditivity direction
  \[
    \mathcal I((k+\ell)\varphi)
       \subseteq \mathcal I(k\varphi)\mathcal I(\ell\varphi).
  \]
  Products of level-\(k\) and level-\(\ell\) sections therefore need not lie
  in level \(k+\ell\). The text now uses the published almost-semigroup
  construction instead of a nonexistent graded-algebra multiplication.
- Removed the invalid multiplication argument from the transcendental
  Minkowski package.
- Restricted the internally proved superadditivity proposition to
  admissible flag valuations, where it follows from the published Xia21
  Minkowski inclusion. Its \(\mathcal I\)-monotonicity follows from the
  published order theorem. The asserted extension to all rank-\(n\)
  valuations in XiaMVOB is not used.
- Downgraded the formulas labelled thm:ok-mvob-line-bundles and
  thm:ok-mvob-metrics: their equation labels and hypotheses are preserved,
  but the blocks are explicitly unverified source claims from an unpublished
  work in progress, not theorem imports. The claimed proof architecture is
  only a bibliographic map.
- Corrected every dependent status and provenance paragraph: Xia21,
  Conjecture 8.8 remains pending independent verification and is not closed.
  Its positive-volume scope is kept separate from the genuine zero-volume
  questions.
- Clarified that the toric zero-volume body is a separately defined Newton
  body. It is not the positive-volume partial Okounkov body evaluated
  outside the domain of its definition.

## Verification

- Balanced all begin/end environments in Chapters 47--55.
- Found no duplicate target labels, no target label duplicated elsewhere in
  the manuscript, no missing target cross-reference after resolving against
  all manuscript labels, and no missing bibliography key used by the target
  chapters.
- Found no conflict marker, exercise section, or optional name on a theorem,
  proposition, lemma, or corollary in the audited files.
- Re-ran the excluded-source search on the audited files and supplied source
  material with no hit.
- Compiled Chapters 47--50 from a direct isolated wrapper using the book
  preamble: success, 243 pages after the reference pass. This passes the
  recovered Chapter 47 source line 1932 and all later edited blocks.
- Compiled the existing Part V expansion slice through Chapters 51--58:
  success, 137 pages. The slice fixture omits longtable, so that package was
  supplied on the command line; the actual book preamble already loads it.
  Isolated builds naturally retain warnings for labels and citations
  defined outside the slice; the global static resolution checks above
  found no missing target label or bibliography key.

## Unresolved issues

The two mixed-volume identities transcribed from XiaMVOB remain unverified.
They are fenced as source claims, are not used, and do not close Xia21,
Conjecture 8.8.

No other mathematical error or excluded-source dependency remains
unresolved in Chapters 47--55. Deep statements explicitly marked as
imported remain at their stated source boundaries and were not promoted to
internal proofs. The full monograph was not rebuilt in this sub-audit; the
two focused syntax builds and global static reference checks were used
instead.
