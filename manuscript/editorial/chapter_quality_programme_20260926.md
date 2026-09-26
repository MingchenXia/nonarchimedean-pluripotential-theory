# Chapter quality programme

Date: 26 September 2026

## Priority

The active editorial priority is the quality of every chapter of the book.
Independent research on the open problems in Chapter 72 is paused. An open
problem may still be edited when a chapter needs an exact boundary statement,
but it is not the driver of the present pass.

## Chapter gate

Each chapter is processed in reading order and must pass the following gates:

1. **Mathematical architecture.** Check the chapter's purpose, dependency
   order, hypotheses, conventions, and compatibility with later uses.
2. **Proof and example integrity.** Check every numbered assertion for a proof
   or an exact source, and verify the computations that carry explanatory
   weight.
3. **Exposition.** Repair misleading structure, undefined notation, vague
   transitions, and statements whose scope is wider than their proof.
4. **Navigation and provenance.** Give reusable objects semantic labels and
   check cross-references, citations, and historical attributions.
5. **Mechanical verification.** Run the scoped writing audit, the project-wide
   reference checker, and a full book build.
6. **Rendered verification.** Inspect the changed pages of the compiled book,
   then repeat the scoped audit and reference check as an automatic second
   pass.

The pass preserves established project-wide conventions unless a convention
itself causes a mathematical or navigational defect. Descriptive example
titles and the existing `chap:` label namespace are therefore reviewed rather
than mechanically rewritten.

## Order and progress

- **Part I, Chapters 1--8:** active. Chapters 1--6 have completed their
  semantic, mathematical, and structural pass; Chapter 7 is next.
- **Parts II--VI, Chapters 9--72:** queued in reading order after Part I.
- **Appendices and front matter:** final consistency pass after the chapters,
  with earlier intervention when a chapter depends on them.

### Chapter 1

The chapter now presents four entrances---complex, model, differential, and
homogeneous---with valuations explicitly identified as their common
substrate. This removes the former five-item reading of a chapter titled
“Four entrances.” The pass also repaired delimiter usage, labeled the
normalization warning, and replaced an imprecise continuity claim by the
exact internal theorem governing uniform convergence of measures.

### Chapter 2

The pass added semantic labels to sixteen definitions, examples, and remarks,
standardized inline mathematics, and removed two unused approximation claims
that were neither proved nor sourced. The scoped writing audit for Chapters 1
and 2 now has zero errors; its remaining warnings concern reviewed descriptive
example titles and the established chapter-label namespace.

Build and rendered-page evidence for this milestone is recorded in
`chapter_status.md` after the full verification gate.

### Chapter 3

The pass corrected the intersection-theoretic level at which vertical
projection is proved. A vertical Cartier divisor now acts first as a class
with support on the special fibre; only its pushforward to the total space is
the ordinary first-Chern-class action. The projection formula is consequently
applied first to the supported divisor class and then to the remaining Chern
classes. This also explains without contradiction why the principal special
fibre has zero pushforward in the total-space Chow group but a generally
nonzero relative degree.

The common-domination statement now includes the general finite-presentation
conclusion proved later in the section, and its properness argument is reduced
to base change plus a closed immersion. Fourteen previously unlabelled reusable
definitions and remarks now have semantic labels, and the degree-conservation
proposition has a proposition-prefixed label throughout the live manuscript.
The scoped writing audit has zero errors; the remaining twelve warnings are
reviewed descriptive example titles and the established chapter-label
namespace. Full build and rendered-page evidence is recorded in
`chapter_status.md`.

### Chapter 4

The pass now separates the chapter's elementary constructions from its
imported analytic-space inputs with exact interfaces. Support-surjectivity
reuses the valuation-extension results proved in Chapter 2, properness is
cited separately in the nontrivially and trivially valued cases, and the
base-change, fibre, and GAGA statements carry precise Berkovich--Temkin
locators. The Newton--Puiseux and completed-algebraic-closure inputs in the
explicit type-IV example, together with the real-tree topology of the
Berkovich projective line, now have exact sources.

The proof architecture was also tightened internally: continuity of the
support map is proved by an explicit inverse-image formula, the
countable-cofinal reduction in spherical completeness is written out, and
the polydisc-extension argument uses the uniform seminorm inequality needed
to pass to the completion. Nine reusable definitions, examples, and remarks
now have semantic labels, and inline mathematics follows the book
convention. The scoped writing audit has zero errors; its remaining
twenty-three warnings are reviewed project conventions and descriptive
titles. Full build and rendered-page evidence is recorded in
`chapter_status.md`.

### Chapter 5

The pass repaired the algebra behind the monomial-minorant inequality: the
descent from the localized monomial ideal now uses the finite
\(\mathfrak q\)-adic filtration and the freeness of its surviving monomial
pieces, rather than the false assertion that the quotient itself is free.
The retraction discussion now distinguishes forgetting residue directions
from collapsing an entire residue class to one point, and the connectedness
of the dual complex is deduced through Stein factorization and the special
fibre rather than through an invalid clopen-cell argument.

Cross-model polyhedral claims are now stated at their correct strength.
Arbitrary higher models induce compatible piecewise-affine structures only
after common rational refinement; literal subdivision of every old cell is
reserved for projective toroidal modifications. The corresponding summary
in Chapter 21 was synchronized. The canonical-weight section now uses the
model-independent Mustaţă--Nicaise weight function, allows horizontal zeroes
to create bends, and separates model skeleta from the essential skeleton.
Exact source interfaces were added for Berkovich deformation retractions,
BFJ compatibility, canonical weight functions, and dlt minimal skeleta. The
Hesse cubic example now proves, via adjunction and the Poincaré residue, that
every pluricanonical minimum locus is the whole circle.

Reusable definitions and remarks received semantic labels, inline
mathematics follows the book convention, and the unsupported projection of
arbitrary bent PL functions onto model functions was removed. The scoped
writing audit has zero errors; its remaining thirty-two warnings are
reviewed project conventions and descriptive titles. Full build and
rendered-page evidence is recorded in `chapter_status.md`.

### Chapter 6

The pass now separates the integral and rational levels of the metric
dictionary. Integral algebraic, formal, and PL metrics agree on proper
schemes; algebraic model, Q-formal, and Q-PL metrics agree only after
Q-linearization; arbitrary real-weight Fubini--Study metrics are uniform
limits rather than automatically model metrics. The formal discussion is
correspondingly restricted to the possibly nondiscrete rank-one setting.

The descent of relative nefness no longer relies on repeated hyperplane cuts:
it uses the closure of a closed point of the generic fibre to produce a
finite multisection over the test curve. The maximum and pointwise-closedness
results now carry exact Gubler--Martin locators, while the model-measure proof
checks independence from both the model and the chosen extension. The
continuous Chambert--Loir theorem now states all of its data and explains why
the internal density-and-Riesz argument does not require Chambert--Loir's
auxiliary metrizability hypothesis. Change-of-reference and constant-shift
formulas have also been separated and normalized.

Reusable definitions, examples, and remarks received semantic labels, inline
mathematics follows the book convention, and the scoped writing audit has
zero errors. Its twenty-one remaining warnings are reviewed project
conventions and descriptive titles. Full build and rendered-page evidence is
recorded in `chapter_status.md`.
