# Cyclic normalization and regular-subdivision boundary audit

Date: 4 October 2026. The [local lattice calculation](research_dossiers/li_cyclic_normalization_and_height_one_subdivision_20261004.md)
writes out the normalized monomial cover and identifies the separate
regular/reduced subdivision problem. It remains outside the active
book. No active TeX, bibliography, frozen book artifact, verifier
receipt or one of the 42 open-problem statuses changes.

## Local normalization and reducedness

For the local model t=product z_i^{b_i} over C and t=tau^q, the
ordinary root has gcd(q,b_1,...,b_r) local irreducible factors.
The normalized factor has character lattice Z^r+Z(b/q), dual
lattice {v in Z^r:b.v in qZ}, and the same positive cone. The
dossier verifies its integral closure by coordinate valuations and
gives explicit finitely many fractional-part monomial generators.
Thus finiteness is proved on this affine chart, without claiming an
unchecked normalization theorem in every category. Local factor
counts do not replace global geometric-integrality hypotheses.

The primitive boundary vector is q/gcd(q,b_i) times e_i. Its
parameter height, and hence the central multiplicity, is
b_i/gcd(q,b_i). Taking q divisible by every b_i makes the
central ideal the intersection of boundary primes and hence radical.
This explains exactly what normalized base change supplies.

Two direct local examples keep the boundaries visible. The normal
surface tau^2=xy has reduced central fibre but a singular total
space. The normalization of tau^2=z^3 is z=u^2,tau=u^3: it is
smooth but has central multiplicity three. These are local algebraic
calculations, not globally connected CY degenerations. No numerical
experiment was used.

## The remaining subdivision requirement

When q is divisible by all b_i, a regular reduced toric subdivision
is equivalent to a unimodular triangulation of the height-one lattice
simplex {v>=0:b.v=q}. The proof splits its lattice by a height-one
vertex and identifies cone index with the affine difference-lattice
index. It includes the zero-dimensional slice case. A further
parameter cover of total degree aq dilates this simplex by a while
retaining the difference lattice {v in Z^r:b.v=0}.

Coherence provides projectivity. With a supplied coherent finite
subdivision, a minimum of integral character forms, shifted into the
dual cone, defines a nonzero vertical monomial ideal. Normalized
blowup charts give its prescribed domains of linearity. Standard
toric saturation/gluing and rational-cone finite generation are
explicit inputs here. The previous positive-model derivation applies
once a compatible global projective normalized-blowup presentation
is supplied.

This calculation does not construct a simultaneous coherent
unimodular triangulation of a finite height-slice complex. Common
faces, a global order function, analytic chart descent and the
finite projective model category still need checking. Separate
triangulations of maximal polytopes are insufficient. Even an
ordinary blowup of the reduced node can lose reducedness: x=u,y=uv
gives t=u^2v. Thus arbitrary desingularization is not substituted
for the needed height-one subdivision.

## Primary-source editions and actual inspection

Ambro [arXiv:1310.3951v2](https://arxiv.org/abs/1310.3951v2) was
acquired as a pinned 27-page PDF, not as the journal edition.
Fresh scoped text reading counted conservatively covers lines
95–175, 809–905, 965–1057, 1158–1316 and 1461–1501: 471 lines.
Eight actual pages were inspected: 2, 3, 15, 16, 21, 22, 24 and 25.
Proposition 3.7 on page 24 controls the normalized toric description;
Lemmas 3.4–3.5 on page 22 control the divisor ramification formula.
The displayed proofs and the torus/integral-closure calculations were
read. Theorem 3.8 on pages 24–25 was checked with its quasi-smooth,
normality, characteristic and open-part integrality hypotheses. Its
earlier toroidal chart and divisor-class antecedents remain imports.
No entire-paper mathematical or visual clearance is claimed.

The early unnormalized-root statements have a literal distinction
problem. Remark 2.11, physical page 16, identifies a regular-character
root with the normal toric lattice-change space. The root tau^2=z^3
is C[u^2,u^3], while its normalization is C[u]. The element u is
integral but is absent from the cusp semigroup ring, which disproves
that literal identification. Example 2.9, page 15, carries the same
unnormalized-versus-normalized issue in its component/line wording.
Both were confirmed in the actual PDF; they are not text-extractor
bar losses. The normalized Proposition 3.7 is kept distinct, and
no counterexample to the principal normalized-root theorem is claimed.
There is no primary inspection of a potentially corrected publisher
edition, whose DOI was identified only through Crossref metadata.

Abramovich–Karu [arXiv:alg-geom/9707012v1](https://arxiv.org/abs/alg-geom/9707012v1)
was acquired as its explicitly marked preliminary version, 23 pages.
Conservatively counted fresh text scope is lines 20–155, 351–370,
590–675, 845–895 and 1040–1140: 394 lines. Six actual pages were
inspected: 1, 2, 3, 17, 20 and 21. Definition 0.1 distinguishes
total smoothness from weak semistability. The page-3 warning says
its construction modifies even a smooth generic fibre, so it is
not automatically a vertical modification preserving the fixed
polarized CY family. Proposition 5.1/Lemma 5.3, Proposition 5.9
and the reduced-ray argument were read, as were the combinatorial
definitions and conditional reduction. The complete general
Theorem 0.3 proof and all dependencies were not newly verified.
Historical conjectures in this preliminary edition do not establish
the current 2026 open-problem inventory.

The fourteen freshly rendered actual source pages were viewed and
their inspection record was finalized. No source-page contact sheet,
unseen-page claim or whole-PDF visual certification replaces those
views. The [manifest](li_cyclic_normalization_and_subdivision_manifest_20261004.json)
pins PDF/text bytes, conservative scopes and all fourteen page images.

## Next-source acquisition and research gate

A bounded arXiv title query returned the two cyclic/toroidal source
records. A further bounded query on unimodular triangulations and
dilations returned five metadata records, including a May 2026
symmetric-triangulation paper. All returned titles/identifiers were
scanned; this is not an exhaustive literature review. The latter
query supplied actual versioned links for Haase–Paffenholz–Piechnik–
Santos, Liu and Ferry–Joswig–Rambau. Their three PDFs and text exports
were acquired once for subsequent reading; no abstract or proof from
those three is counted as read or cleared in this checkpoint. Their
acquisition pins are recorded as next-source leads, not proof inputs.

The next task is their exact coherence, dilation and compatible
finite-complex scope. Any suitable content will be considered for
the book only after source and mathematical checks. KKMSD primary
chapter access and the global model category remain explicit gates.

The new local dossier was fully read after writing. The self-check
covered factor versus global component counts, fractional characters,
coordinate valuations and saturation, finite normalization, boundary
multiplicities, the radical ideal, regularity index, point slices,
dilation lattice, support-function sign and vertical centre, and
the distinction between published and preliminary editions. This
is an author self-check, not a separate verifier receipt. The active
4,244-page book and all 42 statuses remain fixed. Cloud research and
normal GitHub publication continue.
