# Complete toric-bundle source reading and version-specific audit

Nuno Hultberg, *Arakelov geometry of toric bundles: Okounkov bodies and
BKK*, arXiv:2412.04169v1, 5 December 2024. All **42 physical pages**
were actually read in order, with complete selected text and matching
rendered images in **21 displays**. The PDF is 491,226 bytes, SHA256
`65fd4d1052fc359e6d64ec87ea55fc12be5a07947114575f2a0f59fe387194dc`.
This completes the source's proofs, examples and references, not recursive
verification of every imported theorem.

## Controlling version boundary

A current primary metadata check found the published IMRN 2026(4)
article rnag015, DOI [10.1093/imrn/rnag015](https://doi.org/10.1093/imrn/rnag015),
published 11 February 2026 after a November 2025 revision. The accessible
journal response supplies metadata and abstract. **Its full text has not
been acquired or read. Every following diagnosis applies only to the
exact 2024 arXiv v1.** Do not call it a verified journal erratum or assume
the later edition has the same statements, numbering or mistakes.

## Scope that must be retained

Torsors are for split tori in the Zariski topology, encoded by coherent
monoidal functors on the character lattice. Picard classes alone discard
the tensor identifications and rigidifications. Semiabelian group laws
require Picard-zero twists and a rigidification. Flat torsors preserve
semipositivity; integrable torsors preserve integrability with a common
positive base twist. Metrized morphisms have norm one; general degenerate
equivariant maps are not all admitted toric-bundle morphisms.

Orbit closures use the quotient character lattice M intersect sigma
perpendicular and retain the base twist when faces are translated.
Canonical fiber boundary divisors have multiplication weight n, while
abelian polarizations have weight n squared. Actual morphism degrees and
all mixed/binomial factors must retain this distinction.

Okounkov-body and transform fibers are identified on the geometrically
big base-twist locus using an adapted toric/base flag. Theorem A adds
semipositivity of all base twists for its absolute-minimum formula.
Full-dimensional fiber polytopes/interior conventions and the precise
general absolute-minimum import need checking. Torus invariance in the
height-filtration argument concerns Zariski closures under torsion
density; arbitrary torus translates do not preserve individual heights.
An infimum of heights is not exact point attainment.

The arithmetic BKK formula uses a smooth projective base of dimension g,
smooth generic toric fiber of dimension t, integrable adelic metrics and
an operational arithmetic class of codimension g+1-i on a flat model.
Its coefficient is i! on the intersection versus (t+i)! on the weighted
roof integral. Extensions to b-cycles require the stated integrability
and positivity/continuity controls. Fan/model approximation and curvature
current support arguments are load-bearing, not automatic from a
pointwise product of Green functions.

## Exact checks of the literal arXiv text

Seven executable calculations use rational/symbolic arithmetic with no
floating point:

1. Definition 2.3.2 omits the degree l in a monomial's minus log norm.
   A constant metric shift c gives lc on lD and c on the normalized roof.
2. Proposition 5.3.2 confuses the boundary-value functional with its
   hypograph integral: at torus rank zero f(h)=h squared differentiates
   to 2h, not f(h).
3. The printed determinant factor for a simplicial support-coordinate
   derivative needs the inverse Jacobian. The primitive normals (1,0),
   (1,2) give area h1*h2/2, mixed derivative 1/2 versus the printed 2.
   A smooth unimodular cone has determinant one and hides this issue.
4. The squarefree derivative display in Lemma 5.4.1's proof retains one
   excess rho(Delta) factor. Order t+1 differentiation leaves exponent
   i-1 and factorial (t+i)!/(i-1)!, consistent with the lemma's announced
   factor. This is separated from the truth of the intended BKK identity.
5. Lemma 6.0.1's printed imported numerator divided by its denominator
   gives -2/[g(g+1)] times the Néron–Tate height, rather than -1 when g>1.
   The controlling Chambert–Loir primary theorem remains to be read.
6. With t=g=1, base degree one and anticanonical interval [-1,1], a
   quadratic hhat(c(m))=H*m squared gives -4H from printed Theorem C
   and -H from printed Lemma 6.0.3. These source formulas are internally
   inconsistent under their stated conventions.
7. On an elliptic base, scaling M to M to the power a scales its body
   volume by a and its polarization-transferred dual height by 1/a.
   The product-body integral preserves their product, whereas printed
   Theorem C drops the base volume. This is a formal normalization test,
   not an independent verification of a corrected height theorem.

The detailed notes also preserve increasing-filtration/sign problems,
continuous roofs versus literal polytopes, the misuse of Noetherianity
for increasing closed chains, and the ground-field dependence of
rescaled dynamical identifications. These are distinct diagnoses, not
a blanket assertion that all intended Theorems A–D are false.

**No independent production-verifier receipt is available. No new result,
verified counterexample, priority claim or source-wide repair is promoted.**
The current journal edition is unexamined, and the arXiv main results
remain unverified for book import. Chambert–Loir's published source is
the next normalization dependency. The author's 2026 GVF gap-principle
preprint is a relevant later reading direction, with metadata only so far.

## Preserved book and authored evidence

The 4,677-page book is unchanged, SHA256
`9e01eefb787a201d3cdc1dd8e5c5802f3ca86c3acd88c22c9f28ca3d401d3f9b`.
The canonical 42 atoms/twelve problems, general BJ22 Siu/envelopes OPEN,
and LPWZ density UNVERIFIED are unchanged. The native catalogue source,
historical PDF and editor are preserved; native compilation is unverified.
This is a source read, not another ordered whole-book reread.

The 53-member evidence ZIP contains authored notes/receipts, source
acquisition/preparation and actual checkpoint, exact calibrations,
version/GitHub metadata, preparation manifest and executed helpers.
Primary PDFs, full extracted text and rendered page images are excluded.
Every archive member is compared byte-for-byte to its local source.
Upload grants zero additional reading or proof credit.
