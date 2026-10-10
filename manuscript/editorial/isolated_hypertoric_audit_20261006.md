# Isolated hypertoric cones: topology and effective minimizing gradings

Baseline: 47634298fde8fd0696d3afcb92c24fcb82a7b765, matching
origin/work after fetching both tracked branches; origin/main remains
00957114db21b627e97369563032ceda9cea09c7. The preceding source-only
Calabi–Yau finiteness diagnostic retains its own bytes and scope.

One explanatory subsection, inserted between the cyclic surface and the
hypertoric algebraization discussion in Chapter 68.8, and Appendix L.48
continue the known symplectic examples. The import is the rank-one
isolated hypertoric family, with direct explanations of its free quotient,
topology, partial-resolution charts and effective grading. The recent
Coulomb-branch classification is cited only with its conjectural geometric
correspondence; it supplies no unconditional new-family classification
or local fundamental-group result. No new formal theorem, original
priority claim or production-verifier receipt is added.

## Controlling primary sources

- Namikawa, *A remark on isolated symplectic singularities with trivial
  local fundamental group*, arXiv:2309.13877v3, revised 25 November 2025:
  all 563 extracted lines and all eleven actual pages, proofs and
  bibliography were read. Proposition 1 is on actual 1; Claims 2–3 and
  proofs on 2–3; GIT partial resolutions on 3; maximal-weight example on
  4. The official version history identifies the symplectic-singularity
  correction in v2; the book uses its corrected mechanism present in v3.
  The December 2025 published article is identified by publisher metadata,
  but the publisher PDF returned HTTP 403 and was not acquired. No
  journal theorem number or page locator controls this import.
- Beauville, *Symplectic singularities*, arXiv:math/9903070v1, submitted
  12 March 1999: all 460 extracted lines and all nine actual pages, main
  proof and bibliography were read. Definition 1.1, paragraph 1.2 and
  Proposition 1.3 occupy 2; Proposition 2.4 and proof occupy 3–4. The
  finite symplectic quotient and one-resolution extension criteria are
  used. The smooth tangent-cone classification and all earlier dependency
  proofs are not independently certified by this full reading. The
  separately published 2000 edition is not substituted for these locators.
- Bourget–Lamouret–Soysüren–Sperling, *Classifying Isolated Symplectic
  Singularities via 3d N=4 Coulomb Branches*, arXiv:2504.05373v2,
  revised 15 June 2026: all 1,024 extracted lines and all eighteen actual
  pages, figures, tables, proofs and bibliography were read. The PDF has
  eighteen actual pages, despite the metadata comment's fourteen-page
  count. Theorem 1 is on actual 4, printed 3; Conjecture 1 on actual 8,
  printed 7. The September 2026 journal publication is identified by
  metadata; its different PDF is not claimed acquired or read.

The fresh reading comprises 38 actual pages in twenty contact sheets.
The three final reading records are preserved in the ignored primary
cache and reproduced in the integration manifest. Earlier acquisition
and progress records keep their historical flags and bytes. The first
Coulomb acquisition helper failed on an unavailable Python package before
creating its source directory; a separate helper used the standard
library and succeeded. Nothing was installed.

## Mathematical admission and explicit qualifications

1. The rank-one action has positive pairwise coprime weights and at least
   three coordinate pairs, over C. The quotient is the zero-level affine
   Hamiltonian reduction, of dimension 2r-2, rather than a nonzero moment
   level or a generic character quotient. The source's positive ordering
   is not used to enlarge the family.
2. The vertex fiber is the union of the two coordinate subspaces F and G.
   A point outside that union has a nonzero cross pair with distinct
   indices. Pairwise coprimality gives a trivial stabilizer. A Bézout
   monomial of weight one explicitly trivializes the torus bundle on
   the corresponding invariant open patch. Finite stabilizers are
   checked before using the principal-bundle homotopy sequence.
3. The positive-character model has exceptional weighted projective space.
   Its chart at z_i nonzero is a finite quotient of C^(2r-2) with paired
   weights (a_j,-a_j) modulo a_i. This preserves the reduced symplectic
   form. Beauville's quotient result and one-resolution criterion give
   the form extension. The partial model can be singular and is not
   silently treated as a smooth symplectic resolution.
4. In the rank-one case the central hypersurface is a nondegenerate
   quadratic cone. Its punctured link is the real orthonormal two-frame
   space, with sphere fiber S^(2r-2) over S^(2r-1). Both spheres are
   simply connected. Removing F and G has complex codimension at least
   two and preserves the fundamental group by general position. The
   connected torus bundle then gives the known simply connected smooth
   locus. Good scaling identifies its topology with a punctured local
   neighborhood. This direct explanation avoids substituting a general
   complete-intersection depth argument for an isolated quadratic cone.
5. The source's general matrix Proposition 4, Lemma 10 and contact-Fano
   discussion were read but are not imported. In particular, no general
   matrix signature, rectified-depth theorem or contact classification
   is admitted on the strength of the rank-one calculation.
6. Projection of the rank-one kernel lattice onto any coordinate is
   surjective because the complementary weights have gcd one. The
   resulting nonzero primitive rows and torsion-free sequence put the
   family inside the already checked Xu–Zhuang Theorem 7.10. Global
   normalized-volume minimality is the known input, not independently
   proved by the topology or by a comparison among weighted valuations.
7. Quadratic invariants force the scalar kernel to have order at most two.
   All weights odd give exactly the order-two kernel; mixed parity gives
   an odd-degree invariant and a trivial kernel. Effective form weight
   is respectively one or two. For weights (1,...,1,2 ell-1), generator
   degrees become 1 and ell after effective normalization. Large maximal
   generator weight, form weight and a minimizing ray are distinct.
8. With two pairs, the invariant equation is the cyclic surface
   uv=w^(a_1+a_2), after rescaling a generator. Its punctured plane cover
   has deck group mu_(a_1+a_2). The deleted subspaces now have codimension
   one, explaining precisely why the higher-dimensional topology
   argument does not apply. This is a direct invariant-ring consequence
   and the known covering calculation already available in the book.
9. The form convention is changed from the source's sum dw wedge dz to
   the book's sum dz wedge dw together with its Hamiltonian sign
   convention. Moment products and the zero-level equation are unchanged.
   No metric existence, smooth resolution for all weights, endpoint
   integrability assertion or new numerical volume formula is inferred.
10. The recent quiver classification's Theorem 1 assumes Conjecture 1 and
    treats the specified unitary-quiver realizations. Its Future
    Directions on actual 4 explicitly keeps the new families' local
    fundamental groups conjectural. Section 3.4 and equation (3.15) on
    actual 14 use Hilbert computations and a conjectural identification.
    Equal highest-weight generating functions do not establish an
    isomorphism of coordinate or Poisson algebras. The generalized-edge
    extension on actual 15 invokes Conjecture 2 in its proof. No
    unrestricted classification, same-ring implication or general
    good/quasi-good conicality statement is imported.

These are known imports, definitions and explicitly identified direct
explanations under the repository's ordinary mathematical/source-audit
scope. No original result is promoted through a historical or absent
model receipt. General Siu/closure, the recorded BJ22 proof gap and
A2–A4 retain their prior status.

## Checks before PDF review

The 425-input closure has 423 unchanged inputs. All 108 protected inputs,
all 46 existing formal statement/proof blocks in the changed files and
all 42 complete canonical inventory status rows are byte-preserved.
Six labels, four equation tags and two index entries are added; all
12,793 labels and 658 bibliography keys are unique, and all 363 used
keys resolve. The preceding bibliography prefix and the separate
non-Archimedean bibliography are unchanged.

All 46 preceding frozen integration manifests, the separate Calabi–Yau
source-review manifest, 94 recorded prior external exports, native
catalogue and inactive toric candidate retain their bytes. Source checks,
cross-references and the inventory checker pass.

## Final compilation and matching-PDF rereading

The complete book build has 4,366 pages, 20,295,059 bytes and SHA256
b11b1452244807092e4ee2fac3593d79ba19e288232e6816a744a20e33c644e6.
It has zero TeX errors, package/pdfTeX warnings, missing characters,
overfull boxes, unresolved references or citations, and rerun requests.
The 954 nonfatal underfull diagnostics are unchanged. Bibliography output
has 363 used entries; the index accepts all 760 entries, with no warnings
or invalid page destinations. All 21,854 named destinations, 46,894
internal links and 2,543 contents entries pass navigation checks.

All 44 selected physical pages were actually displayed and reread in
22 contact sheets from this exact final PDF: 60–61, 68, 3565, 3582,
3601–3606, 4127–4131 and 4339–4366. This includes the changed contents,
chapter opening, cyclic-to-isolated-to-algebraization transition, new
subsection, Appendix L.47–48 transition, Appendix M opening, complete
index and bibliography. Physical 4130 is the ordinary blank separator
before Appendix M's recto opening. No repair was needed in this final review. The reviewed-image
manifest has SHA256
0a6fc1b35fe3582041cc2dc13b4e1884c4d6fee9180e593bc835ea63799c15d5.
An earlier oversized display response was not counted as viewing; its
first sheets were redisplayed before any flags were finalized.

The 4,366-page book, matching 44-page review and source package are
recorded separately in the integration manifest and artifact record.
Source-package members are checked against their saved bytes; a fresh
isolated archive compilation is not claimed. This is a scoped rereading
after the completed ordered whole-book pass, not a new full-book reading.
