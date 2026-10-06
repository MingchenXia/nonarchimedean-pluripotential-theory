# Local maximality and full residual mass: integration audit

Date: 6 October 2026. Baseline work:
`c05a7c74c8865c62e86bfe7eb0419f13ded48440`.
Baseline main: `00957114db21b627e97369563032ceda9cea09c7`.

Appendix H.8 now explains the attributed Do–Hiep analytic-spread
maximality theorem, compact comparison for compatible local potentials,
and the complex-surface full residual criterion. Appendix L.64 binds
those explanations to exact editions, dependencies and remaining proof
inputs. Six bibliography entries retain distinct version scopes.

## Mathematical scope

- The book uses `ddc = i/(2 pi) partial bar-partial`. Both new preprints
  use twice this operator; their degree-n products scale by `2^-n`.
  Błocki's operator is `4 pi` times the book operator.
- Local Cegrell E differs from compact relative full-mass E. Its full
  Radon products may charge poles; nonpluripolar products lose that mass.
- On a domain in C^n, n at least two, analytic singularities have a
  two-sided bounded remainder. The source theorem requires vanishing
  ordinary mass off the poles and analytic spread strictly below n
  at poles. The coefficient need not have a global generator choice.
- Spread controls the normalized ideal blow-up. Further resolution can
  introduce divisors over points. Powers, integral closure and rationally
  matched local coefficients retain the source's gluing conditions.
- McAdam's integral-closure theorem is an attributed input; the original
  AMS proof PDF was unavailable. Classical complex Siu decomposition
  and normal-space psh extension remain external inputs.
- Compact comparison requires the same pluriharmonic transitions for
  both sets of local potentials. Its right side is a finite signed
  measure integral on compact support. Both common-pole contributions
  are retained before any independent polar comparison is applied.
- General compact domination is Lemma 4.3 and assumes a global local-E
  potential with positive absolutely continuous density almost everywhere.
  Corollary 4.4 is the zero-mass specialization. The blow-up example and
  the unnumbered P^1 x C counterexample distinguish this from strict psh
  and from arbitrary manifolds.
- The surface theorem retains the two local E-sandwich inequalities.
  Surface factorization and the C^2 operator-domain criterion give local
  E-potentials of the residual current. Vanishing of its full square,
  rather than its nonpluripolar square, characterizes maximality.
- The squared-log isolated pole has a unit full atom in the book
  normalization and zero nonpluripolar square. A divisor potential has
  zero residual current but need not itself belong to local E. These
  examples keep the two kinds of pole distinct.

The three new proofs are source-input outlines. This checkpoint adds
no new original theorem, higher-dimensional residual result, complete
mixed-capacity proof repair or certification of every external proof.
It supplies no general BJ22 homogeneous Siu/envelope division input.

## Source evidence and locator correction

The preceding immutable source review is reused: 78 displayed
edition/page pairs in 42 sheets, including four complete PDFs and
selected pages in three further editions. The new main editions are
2610.05937v1 (all thirteen pages) and 2610.05948v1 (all nineteen).
The scope of each dependency remains as recorded in that review;
this integration adds zero fresh primary-page audits.

The [locator addendum](Do_Hiep_source_locator_addendum_20261006.md)
corrects approximate introductory locators in the frozen audit and the
nonexistent Example 4.7. The current text cites Example 4.6 and the
following unnumbered discussion and distinguishes Lemma 4.3 from
Corollary 4.4. Corrections do not rewrite prior frozen artifacts or
turn the nineteen scoped records into counterexamples to main theorems.

The polar comparison versions retain separate dates and reading scopes.
The full v2 reading does not imply a full v1 reading. Błocki and Teissier
intermediate formula issues, capacity liminf/addition obligations,
translated truncations and the retained polar term remain explicit.
The surface application uses compact comparison independently of the
unrepaired general mixed-capacity chain.

## Source preservation and required checks

The active closure has 425 TeX inputs. Only Appendix H and Appendix L
change: all 423 other active inputs retain their bytes. All 22 old formal
blocks and eight proof blocks in the edited appendices retain their
bytes and order. Five formal blocks, three source-input proof outlines,
six equation tags H.2–H.7, sixteen labels and three index entries are added.
Both old bibliography contents retain their bytes; the six new entries
are appended only to ComplexGeometry.bib.

All 108 protected inputs, 86 preceding frozen manifests, 148 preceding
exports, native catalogue source/PDF and the open native editor are
preserved. The 42-atom canonical inventory retains its twelve Chapter 72
environments and tiers `(0,3,7,15,17)`. No status, model call, verification
receipt or historical receipt scope changes.

Required `scripts/validate-manuscript.sh` completes with exit zero,
including references, inventory, six existing checker unit tests and
the full book build. The final source has 12,930 unique labels, 415 cited
entries and 709 bibliography keys. Final compilation has zero TeX,
package or pdfTeX warning, missing character, overfull box, unresolved
reference/citation or rerun request. Its 954 underfull boxes equal baseline.

The index accepts 781 entries with zero rejection or warning; all
425 distinct numeric destinations resolve. Navigation verifies 22,133
named destinations, 47,284 internal links, 171 URL links, 2,583 contents
entries and six parts, with no invalid internal link or named destination.

## Matching final-page reading and immutable release

The final book has 4,432 pages, 20,592,156 bytes, SHA-256
`09ef6f20d936f623dc770e2a63ee228ad8db47e5ec1c84b862230579bf61574f`.
All 47 selected matching final pages were read as complete extracted
text and actually displayed in 24 separate sheet views. They cover the
affected contents, Appendix H introduction/addition/transitions,
Appendix L addition/transitions and the entire index and bibliography.
The selection includes an intentional blank transition page. This is
a scoped review, not a new full-book rereading.

The 47-page review PDF SHA-256 is
`73d08efa5663897203b34704fdd49b1a40dc851538710c5708277da29c72b770`.
The final reading record SHA-256 is
`6291c4fce956f4a01d8a29fe9f94118ee0560d827d42ec5c68c1cbcb3aaab120`.
The final release gate SHA-256 is
`fee3db79a232fea428cdf0544e9ac4c5a3d2153f69d0d4bd94991005eef6d3eb`.
The immutable integration manifest retains the source gates, full page
selection, actually-viewed flags, original source evidence and locator
addendum hashes. The external artifact record gives release hashes;
the source closure contains 427 TeX/bibliography records. Every source
archive member is compared with its current source bytes. No fresh
isolated archive compilation is claimed.

Normal work-branch publication uses the standing GitHub authorization.
Fetch both main and work immediately before packaging; preserve any
incoming author progress. Update the existing draft PR after the push.
Continue bibliography precision and exact-primary-source research.
