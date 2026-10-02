# Chapter 14: second reading audit

Date: 2 October 2026. The complete original 4,073-line source,
`parts/part2/ch14_currents.tex`, was freshly read continuously, together
with both active support-correction inputs. The revised source has 4,257
lines, preserves all 126 labels and 124 formal environments, and leaves
83 environments byte-identical. Forty-one environments change. The
mathematical diff and final edited contexts were checked.

The two inputs retain their exact audited bytes:

- `ch14_cld_support_correction_statement_20260829.tex`: 74 lines,
  SHA-256 `2b291fc55872ab32d40fa3a67e9a9308fc12ac9726113b48950d0a9e50cfd8c1`.
- `ch14_cld_support_correction_proof_20260829.tex`: 278 lines,
  SHA-256 `9f21f7ece49c761d3f19c07acd8b56e48e9939be493e0bbbd39c0a4d3176e668`.

Both are in
`editorial/rethlas_packets_20260829/ch14_cld_support_correction_packet_20260829/`.
The historical hostile audit there was freshly read; its PASS and exact
hashes are reused for these unchanged inputs. Their old quarantine comments
are historical metadata: the actual build includes both files. No fresh
independent verifier verdict is claimed.

The opening assumptions distinguish boundarylessness, local holomorphic
separation and paracompactness. Boundaryless topologically separated spaces
satisfy the local separation condition used for ordinary cutoffs and
current localization. Finite partitions near compact supports use CLD25
15.2.9 without a global paracompactness assumption; an arbitrary-cover
partition and the stated fineness theorem assume paracompactness. The
import list now includes degree and fibre-integral results, test-form
topology, cutoffs and density. It no longer claims that all but four inputs
are proved internally.

Stage coefficient norms are intrinsic to the finitely many cell tangent
spans. Ambient normal coefficients do not define norms on the quotient of
forms. Subdivision gives equivalent norms on a fixed stage; a chart
refinement gives continuous transition estimates. The locally integrable
G-form construction uses finite ordinary partitions, G-additivity and
common-chart refinement to return bounds to the original stage. Its
convergence assertion specifies a fixed common-chart local L1 limit.
Positive currents of bidimension (0,0) are Radon measures via exact cutoffs,
density and Riesz; arbitrary currents of that bidimension need not be.
The current sheaf and compact-support extension arguments use the proper
family-of-supports colimit topology, rather than an invented global
closed-set derivative norm.

The removable-set proof makes restriction an isomorphism of test spaces:
near the compact removed set, finitely many chosen chart germs kill the
coefficient forms independently of the test form. The fixed remaining
support is compact in the open complement, so stage continuity follows.
The rigid-locus corollary now assumes the pointwise graded residue bound
`d_K(z) < max(r,s)` on its closed support. A closed analytic subspace with
the corresponding dimension bound satisfies it because its completed
residue fields are unchanged. No weakly analytic dimension-only bound is
silently substituted.

The top-degree J calculation is made on n-dimensional cell spans.
Compatibility determines the current differential sign only when a smooth
form has a nonzero derivative current; in degenerate degrees both maps
vanish. The universal sign is tested with a nonzero compactly supported
coordinate example. The integration-current normalization still carries
its dimension-dependent J sign. The boundary-current identity is obtained
by solving the transposed Stokes equality and also proves continuity of
the boundary functional. Boundary formulas use n at least one; the
zero-dimensional case has zero differentials and boundary terms.

The order-zero domination inequality uses positive forms
`c ||alpha|| eta^p +/- alpha`. Its coefficient norm is on the actual
finite cell tangent spaces. Form-to-current positivity is tested on the
n-dimensional calibrated cells. The converse uses the published
very-rich hypothesis, supplied for usual strict pure-dimensional analytic
spaces by CLD25 16.4.4; boundarylessness alone does not imply it.
Automatic continuity and saliency need local holomorphic separation,
without global paracompactness. The gap for a functional nonnegative only
on strongly positive tests remains explicit, since the strongly positive
cone need not span all symmetric forms.

The trivially valued projective-line example now supplies the finite-chart
construction for every permitted smooth jet. Rational moment coordinates
have a simple pole at each selected endpoint and a simple zero at the last,
consistent with minus-log tropicalization. The slope relation determines
the linear part; explicit quadratic selectors interpolate the higher jets.
All unselected branches collapse to the common vertex value. This is a
reconstruction of CLD25 Example 6.7.3, not a new research theorem. The
unbounded-order example chooses a chart whose ordinary interior contains
the vertex and shows that every test in its detecting sequence belongs to
one fixed stage. Its order-zero nonmeasure companion states summability
as the supremum of absolute sums over finite branch sets.

Berndtsson's metric current is defined for a smooth properly embedded
submanifold without boundary, ensuring locally finite volume. Rescaling
uses the orthonormal frame for the rescaled metric. The minimality formula
is the traced identity; untraced closedness for a linear subspace follows
from tangential integration by parts, not from the minimality criterion.
The lattice calibration and Euclidean metric normalization stay separate.
The Ber26 positive Bedford--Taylor case uses Lemma 4.1 and the same
construction argument; Theorem 4.2 itself states the weakly positive case
with the additional strong condition. The affine-isomorphism pullback
includes translation in the inverse argument of coefficients. Euler's
identity is proved for the distributional Hessian coefficients and both
radial contractions. No unverified transfer of a form contraction sign
to currents is used.

Support on a closed analytic set of smaller dimension means ambient
vanishing near it, as in CLD25 15.2.1(b). The fibre-support test includes
both the base graded residue dimension and the fibre dimension. The
identity morphism at a Gauss point demonstrates why fibre dimension alone
is insufficient. Proper pullback uses affine estimates on its actual
polyhedral image. Pullback of an arbitrary current is kept distinct from
pullback of a specified potential and from potential-independent descent.

The fibre-integration proof follows CLD25 16.5.4 on compact domains:
proper support removes the higher-relative-dimension locus from the
relevant top-degree tests; finite G-covers use additivity; adapted moments
and source/base skeleton cells reduce to flat Euclidean Fubini. The
calibrated ratio d_D/d_C supplies the fibre weight. Nonadapted lattice
indices are already included in the degrees, and no extra multiplicity
is inserted. Dense flatness, pure dimensions and n minus m at least zero
are explicit. The Bedford--Taylor projection formula also states
boundarylessness and the allowed number of potentials. The right-hand
side uses the coefficient Radon measures on the common skeleton; it is
not arbitrary multiplication by an L1 function. The convergence step is
the exact published import from 16.5.7 with the relevant flat/skeletal
regularity of 16.3.3. Piecewise smoothness alone is not offered as a general
criterion for testing weak convergence against discontinuous functions.

Generic nilpotents contribute via the fundamental cycle's multiplicities;
lower-dimensional embedded structure contributes no extra integration
current. The longer analytic-component curvature proof is unchanged and
retains its original-field, local-approachability and published nullity
scopes. In the local mass-bound proposition, the hypothesis now controls
every compact subset of every relatively compact chart with a nonnegative
cutoff equal to one near that subset. A finite partition and strict
positivity give the uniform order-zero estimate. One cutoff on an arbitrary
prescribed compact subset would not control every test. The product
compactness theorem retains nets and a subnet rather than an unsupported
subsequence assertion. General analytic convolution and regularization
are kept at their stated available scope. The final dictionaries record
definitions and proved compatibilities without adding equivalences.

Fresh local primary checks used CLD25 PDF SHA-256
`5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719`.
All fifteen rendered physical pages were inspected: 152, 159--162, 167,
423--424, 447, 454--458 and 467. These include the star criterion, current
construction and extension, positivity/very-rich injectivity, cutoffs and
support, fibre regularity, strictness, projection formulas and
analytic-nullity theorem. Additional text checks covered 6.7.3,
7.1.9--7.1.13, 7.2.1--7.2.10, 7.3.7--7.3.11, 15.2.1--15.2.7,
16.3.3, 16.4.4, 16.5.1--16.5.7 and 16.9.2--16.9.4.
Ber26 PDF SHA-256
`d2cb950659b15eb2223ee6cebf7034c6169346277c79a5fb4bd0adbb6a4da034`
was checked in text and on both rendered pages 16--17 for Lemma 4.1 and
Theorem 4.2. Earlier calibrated integration and boundary/Stokes evidence
from Chapters 11--13 is reused. There is no fresh Ber19 primary audit or
new network literature search.

These are classical definition, proof, scope, example and exact
published-import repairs. They do not claim a new original research
result, a new independent verifier verdict, or a solved open problem.
Semantic, dependency, delimiter and structural checks replace the
unavailable legacy writer.

The final full-book build has 4,176 pages and 19,507,106 bytes, with zero
TeX errors, LaTeX/package warnings, overfull boxes, unresolved references
or citations, and rerun requests. There are 866 nonfatal underfull boxes.
All Chapter 14 physical pages 609--674 and seams 608/675 were viewed in
seventeen initial contact sheets. Two detached warning headings were
repaired with local minipages. All twelve changed final sheets were viewed
again; the remaining five are byte-identical to the inspected baseline.
Formulas, proofs, warnings, tables and seams have no clipping, collision
or detached heading. Post-render references pass for 425 active files and
12,564 unique labels. The inventory remains 42 atoms in twelve families
with tiers (0,3,7,15,17). Exact hashes and gates are recorded in
[the manifest](second_reading_ch14_manifest_20261002.json).

The review PDF is
`/workspace/book-completion-drafts/second-reading/Ch14_Review_2026-10-02.pdf`.
Chapter 14 passes this reading gate. Chapter 15 has been freshly read
through lines 1--1095 of its 4,920-line source. Its 57 direct active inputs
(54 dossier fragments and three exposition fragments) have not yet been
freshly read; no edits have been made. Its remaining reading, scope and
rendered-page gates remain open. The full-book goal continues in the cloud.
