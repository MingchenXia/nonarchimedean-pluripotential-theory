# Chapter 11: second reading audit

Date: 2 October 2026. The complete original 3,335-line source,
`parts/part2/ch11_integration.tex`, was read continuously from beginning
to end. It has no active input fragments. The revised source has 3,399
lines, preserves all 116 labels and 98 formal environments, and leaves 60
formal environments byte-identical. Thirty-eight environments change.
The complete mathematical diff and subsequent edited contexts were checked.

The introduction connects integration to Chapter 10's existing calibrated
computations. A positive unit-segment integral does not by itself determine
the higher-dimensional boundary signs: those must also be tested against
the exterior-algebra conventions. The grouped top-form sign changes with
dimension modulo four, not simply parity. Positivity reverses in dimensions
2 and 3 modulo 4. The primed boundary prefactor has its separate even-
dimensional sign test, and the double-primed trace retains its prefactor -1.

The saturation warning gives the interval [0,1/3]: its bounded difference
set has no nonzero integral vector although its tangent lattice is Z.
The subdivision proposition states the weighted-common-refinement scope
actually established by its proof; balancing is unnecessary. This also
justifies its subsequent uses on unbalanced weighted complexes.

Euclidean normals and lattice quotient normals are related by covolume
conversion. The Euclidean calculation on a triangle remains correct when
its measures and distances are used consistently. The conversion identity
continues to hold on every cell of a complex; different cells may need
different factors before their fluxes enter the lattice balancing sum.
The nonunimodular square example multiplies area two by weight two, matching
pullback factor four. Change of variables removes one factor two, leaving
the single lattice index. Its unimodular square uses the weighted
pushforward definition without claiming that the square is balanced.

The trace normal form uses a tensor product of exterior powers, not their
direct sum. The flux proof separates a pointwise fibre from the module of
smooth sections, and the trace-additivity corollary fixes its evaluation
point when identifying the target with a one-dimensional vector space.
The two adjacent segments cancel when their weights match and their
outward normals oppose, rather than when their weights have opposite signs.

Polyhedral and defect Stokes formulas state C1 coefficient regularity;
the proof uses continuous first derivatives, the fundamental theorem of
calculus and the classical divergence theorem. This supplies the C1 form
required by Green's formula for C2 coefficients. The unbounded truncation
box also contains a relative-interior point, preserving the tangent span
even when the form's support is empty. Its face set is finite.

The balancing converse chooses the point and initial neighbourhood supplied
by its local testing hypothesis, then shrinks within that neighbourhood.
Its one-dimensional detecting form has no second contraction group.
Real weights do not change lattice indices; integral weights supply the
integral multiplicity interpretation. Truncated tripods retain endpoint
defects even when their vertex is balanced. Unbalanced examples use the
defect formula and retain vertex terms in integration by parts. Integer
weightings form the rank-two group Z^2 in the crossed-lines example; a zero
weight removes an axis from the support.

The global imported Stokes theorem distinguishes a harmonious calibrated
parlinear space from a calibrated G-tropical space with vanishing boundary
measures. Its explanation now follows the original reduction to a closed
skeletal subset strongly supporting the form, rather than attributing a
different chart-cover proof to the source. The original local CLD25 PDF,
SHA-256 `5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719`,
was checked in text and rendered pages 116 and 140: Proposition 4.6.15(a)
uses C1 forms, its Green statement uses C2 symmetric forms, and Proposition
5.11.1 reduces the G-tropical identities to the parlinear formulas.
Discordance and harmony were checked in Sections 4.6.7--4.6.14, and
boundary measures in Section 5.9. This is a fresh check of those local
primary-source locators, without a new literature search or network fetch.

Mixed cancellation first restricts to an n-dimensional cell span. J need
not act by a scalar on all ambient (n,n)-forms when the ambient dimension
is larger. The cellwise identity is enough for Green's formula. Its
symmetry corollary retains harmonic calibration and both closedness
conditions needed by the two integrations by parts.

The graph comparison uses edgewise integration with endpoint terms for
continuous piecewise C2 functions, which need not be ordinary smooth
functions on balanced tropical charts. Its Laplacian has the edge density
f'' ds and outgoing-slope vertex atoms. Loops contribute both edge ends.
The interval f(t)=t has zero interior d'd'' but graph Laplacian delta0 minus
delta_l; its negative Dirichlet pairing follows from the graph identity
including endpoint atoms, rather than from a boundary-free hypothesis that
the interval does not satisfy. The Green-function check uses the same graph
measure notation. Existing numerical values and the Chapter 8 model
tripod's reference-curvature mass remain consistent.

Properness suffices for the locally finite pushforward construction; the
wording no longer asserts its necessity. The Jacobian explanation retains
two determinant factors and one measure cancellation. Zero-dimensional
balancing is handled before negative-bidegree tests. A transverse
zero-dimensional intersection is locally finite and finite on a compact
test support. Its proof treats the empty-intersection case and inserts a
cutoff away from facet boundaries before extending coefficients by zero.
Coordinates have origin on the intersection; the induced lattice map is
injective of finite index, rather than necessarily an isomorphism.
Stable-current convergence includes signed clusters of total weight zero
and clusters limiting outside the test support. The determinant test uses
the correct columns (1,2) and (1,0). Example titles distinguish an affine
line from a tropical line.

These are classical definition, proof, example and imported-scope repairs.
No original research result, new independent verifier verdict, or solved
open-problem status is claimed. Unchanged imports retain earlier source
evidence. Semantic, dependency, delimiter and structural checks replace
the unavailable legacy scoped writer.

The final full-book build has 4,174 pages and 19,486,598 bytes, with zero TeX
errors, LaTeX/package warnings, overfull boxes, unresolved references or
citations, and rerun requests. There are 866 nonfatal underfull boxes.
All Chapter 11 physical pages 469--516 and seams 468/517 were inspected in
thirteen contact sheets. A detached warning heading was repaired with a
local minipage. Final sheets 01/04/05/06 were viewed again; nine other
sheets are byte-identical to the sheets already viewed. Formulas, warning
boxes, tables and chapter seams have no clipping, collision or detached
heading. Post-render references pass for 425 active files and 12,564 unique
labels. The inventory remains 42 atoms in twelve families with tiers
(0,3,7,15,17). Exact hashes and checks are recorded in
[the manifest](second_reading_ch11_manifest_20261002.json).

The review PDF is
`/workspace/book-completion-drafts/second-reading/Ch11_Review_2026-10-02.pdf`.
Chapter 11 passes this reading gate. Chapter 12's complete 3,551-line
source has been freshly read; it has no active fragments and no edits yet.
Its source, mathematical-scope and rendered-page gates remain open.
The complete-book goal continues in the cloud.
