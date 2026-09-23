# Chapter 58: proper algebraic recovery and its topology

Audit date: 23 September 2026.

## Scope and status

This unit reconstructs the existing proper algebraic recovery theorem in
Chapter 58. The section title now matches the theorem's proper scope.
Projectivity, smoothness and normality are not added as assumptions.
The theorem label and display (58.22), the preceding bimeromorphic unit,
and the following multiplier-ideal bridge are preserved. The notation
now distinguishes the algebraic variety, its usual complex analytic
space, and its trivially valued Berkovich analytification.

This is textbook reconstruction of an existing sourced comparison, not
a new research theorem, a production verifier gate, an independent-agent
verification, or a research-atom closure.

## Mathematical checks

The former proof asserted the GAGA ideal identification and equality of
pointwise topologies without explaining the intervening localization.
The new proof separates three obligations.

1. Proper GAGA identifies coherent subobjects of the structure sheaf.
   Exactness, full faithfulness, and compatibility with tensor products
   identify ideal sums and products as images of their defining maps.
   Thus it is an isomorphism of ideal semirings, not merely a bijection
   of abstract coherent sheaves. Reindexing coordinates then gives a
   homeomorphism of character spaces.
2. The sum of positive algebraic coherent ideals is finite by
   noetherianity and is the radical ideal of an irreducible closed set.
   Its generic point is the center. If two ideals have equal stalks
   there, the colon ideal has value zero; multiplication by it proves
   equality of the two values without subtracting infinities. Extending
   finite local ideal generators gives a character on the local ring.
   The affine ideal-character theorem recovers its semivaluation;
   quotienting by the infinite-value kernel and taking fractions
   produces the valuation on the residue field of the support point.
   The local generator formula checks both inverse maps. This includes
   proper support, infinite ideal values, point characters, and the
   trivial valuation with generic center.
3. The valuative criterion supplies a unique center for every Berkovich
   point on a proper variety. For a finite affine cover, points with
   center in an affine member form a compact space of nonnegative
   semivaluations on its ring. These sets are closed in the Hausdorff
   analytification. Each ideal coordinate is a finite minimum of local
   function values, so finite closed pasting proves continuity. The
   continuous bijection is a homeomorphism by compactness. Pullback of
   ideals proves naturality for algebraic morphisms between proper
   varieties.

The topology proof does not assume that the center map is continuous.
It also does not use the ample-twist separation argument from the
projective Chapter 32 setting for a possibly nonprojective proper variety.
The colon-ideal reconstruction provides the needed injectivity here.

The second local mathematical/source pass checked the noetherian finite
sum, the radical-power and irreducibility reduction, both colon
inequalities, coherence and extension of local ideals, the prime kernel,
the support residue field, and finiteness of every denominator value.
It checked the two inverse assignments, uniqueness of centers, the
affine bounded sets with their inherited topology, finite closed pasting,
and functoriality. It made the support residue field and affine center
criterion explicit, and added the continuity justification for the
Gauss family. The theorem statement and its display are kept together.

## Examples and boundaries

On P1 the Gauss family w_t(sum a_i T^i)=min i t, over nonzero
coefficients, has center 0 for t>0, infinity for t<0, and the generic
point for t=0. The two global point-ideal values are max(t,0) and
max(-t,0). The family is continuous, while its centers do not define a
continuous map to the Zariski space. Its t<0 points have |T|>1 and do
not belong to the centered locus of A1, although they are Berkovich
points of A1.

Independently, the analytic coherent ideal (sin pi z) on the complex
line has infinitely many discrete zeros and is not algebraizable from
C[T]. Thus neither properness's centering role nor the separate GAGA
role can be suppressed. No nonproper analytic comparison is asserted.

## Primary sources and access limits

- Mesquita-Piccione, [arXiv:2409.06221v2](https://arxiv.org/abs/2409.06221v2),
  18 September 2025, p. 9: Example 1.3.2(1) and Remark 1.3.3.
  The official HTML and exact PDF page were checked; the PDF page was
  rendered and inspected. The manuscript uses the existing exact-version
  MPTropicalV2 entry. The published MP24 entry is unchanged; its full
  publisher typesetting was not inspected in this unit. PDF SHA-256:
  `9eb2ea7686a5962ebc11c5eacd23b0cb3dcb081e27ac48292933f291fc82cb23`.
- SGA 1, recomposed and annotated edition, Documents Mathematiques 3,
  SMF, 2003: Expose XII, Proposition 1.3.1, printed pp. 241--242, and
  Theorem 4.4, printed pp. 249--250. The latter explicitly treats
  proper schemes, reducing the nonprojective case by Chow's lemma.
  The [publisher record](https://smf.emath.fr/publications/revetements-etales-et-groupe-fondamental-sga-1-seminaire-de-geometrie-algebrique-du)
  verifies the edition, year, series, volume, page count and ISBN.
  MathSciNet was unavailable, so no unverified MR metadata was added.
  The [official reprint](https://arxiv.org/abs/math/0206203v2) was read;
  physical pages 257, 265 and 266 were rendered and inspected.
  The new SGA1Reprint entry distinguishes these page locations from
  the existing 1971 SGA1 entry, whose bytes are preserved. PDF SHA-256:
  `8e64218d356456c534eebf996940f0f957e43b54f1a080241debe12cbaf60d3c`.
- [Stacks Project, Tag 01PF](https://stacks.math.columbia.edu/tag/01PF):
  extension of a finite type quasi-coherent submodule from a
  quasi-compact open in a quasi-compact quasi-separated scheme.
  Finite type noetherian X and an affine open meet these hypotheses.
- [Stacks Project, Tag 0BX5](https://stacks.math.columbia.edu/tag/0BX5):
  existence and uniqueness for the valuative criterion of properness.
  Both Stacks statements and their hypotheses were read directly.

Proper GAGA, the extension lemma, the valuative criterion, and the
Hausdorff property in the book's foundational analytification theorem
remain named inputs. The deductions from them are written out; they
have not been promoted to new research results.

## Validation and preservation

The final full build passes: 3,947 pages, 18,769,877 bytes, 389 TeX
inputs and 11,576 unique labels. There are no missing inputs, duplicate
labels, dangling references, unresolved citations, or horizontal or
vertical overflows. Pre-existing underfull-box and class warnings remain.
The strict style audit of the entire changed TeX block returns zero
errors and zero warnings. The additional bibliography-aware audit flags
the known exact-version MPTropicalV2 preprint entry; the source-version
review above resolves that prompt without pretending to have inspected
the publisher's text. All citation keys resolve in the full build.
`git diff --check` passes.

The first and final builds were inspected at the revised pages.
Final physical pages 3304--3308 (printed 3236--3240), including the
section boundaries, and the new bibliography entry on physical page
3943 were rendered and visually checked. These checks are separate
from the mathematical/source pass.

The inventory remains 46 active atoms in 14 formal environments, tiers
`(0,5,8,16,17)`. The chapter prefix and suffix outside the recovery
unit were compared byte for byte with the preceding commit. The entire
previous bibliography is an unchanged byte prefix of the new file.
The supplied CURVE_PSH.tex, author sources, frozen packets, verifier
receipts and dated release artifacts are unchanged. The generated live
PDF remains ignored and is not a new release or part of the Git commit.

SHA-256:

- Chapter 58: `7e792cd4f518033db563357a85cf41f96778287d40adafd634274e8ac62b61b3`.
- Bibliography: `b09c39f439e522a126a57c4c6e783719e6971a3aae6214b664774c2830fb76a1`.
- Generated live PDF: `8138eba59552466ba6198255037e6913c3e4cc8512f09c10d056888bf3f82264`.
- Supplied and restored CURVE_PSH.tex:
  `9142aac73c5af7e4e715b3313def5ed56fae4e63e1ac8a53d0419df7d2194be9`.

The next bounded unit is Chapter 59's integral-closure comparison:
check nonzero-ideal assumptions in the normalized blowup, replace any
unsupported evaluation of a local germ by a global ideal character,
and verify the divisorial converse and its exact analytic source.
