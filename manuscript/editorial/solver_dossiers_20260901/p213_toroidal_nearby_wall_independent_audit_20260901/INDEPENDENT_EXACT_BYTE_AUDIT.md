# Independent exact-byte audit: nearby all-vertical residual-curve walls

Date: 1 September 2026.
Reviewer: /root/p082_independent_reaudit.
Author reviewed: /root/p081_weighted_repair_fresh.

## 1. Verdict, scope and provenance

PASS in the exact geometric scope stated in the frozen note. No substantive
gap or required correction was found. This is a fresh mathematical review of
the complete 519-line proof and its source interfaces, not a production
verdict, source-representation theorem, current theorem, or P21.3 solution.

The scope retained is an ACTUAL proper flat regular integral model over the
ORIGINAL complete DVR, residue characteristic zero, supplied with a strict
SNC boundary including horizontal components and a given full-dimensional
monomial cell at a closed stratum point. Special-fibre multiplicities are
not assumed to be one. The conclusion is a nearby whole closed all-vertical
simplex, a whole proper residual curve for a facet, and dense independent
normal weights on the facet. The new generic fibre is the same X. No
algebraic closure, ramified base extension, alteration, current pullback,
or mere tropical-target overlap enters the argument.

I did not author the primitive-ray extraction or retained-ray simplex
construction. I previously authored related outer-collar, common-moment and
maximal-rank capture notes, and reviewed point-retaining and wall arguments.
That related experience is disclosed; none of those results is a premise
of the candidate or of this verification. In particular L, V, O, P, Q, R,
the reviewer's capture packet, and any proposed synthesis of them are NOT
used to fill a gap here. Root supplied prefreeze requests for proof
explication, as the author ledger records; root's preliminary review and
the author's numerical checks were not treated as independent acceptance.

## 2. Exact frozen input

Candidate directory:

/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260901/p213_toroidal_nearby_wall_research_20260901/

Principal pins:

- RESEARCH_NOTE.md: 25,410 bytes, SHA-256
  5ad7cc7f5899ba3a251ba6d3417ec4456f0fa5cdc21db05ea8f262dcc17ab38e.
- SOURCE_LEDGER.md: 6,342 bytes, SHA-256
  f265b8d6d6243114ff87aa618a7863eb31be256b39fa120a4071106f086a3641.
- MANIFEST.json: SHA-256
  613cc1698a8cd517dd92eb50368182114a60ffeadc19f334a52f8ba401f278ef.
- SHA256SUMS: SHA-256
  49e735cf24d2762dc13ed1be05d5305f8049a58161a64ceb4b5a5265be9efa08.

All eleven author-manifest entries and twelve author checksums were
independently read and checked. The author checker was read before running,
is read-only, and was rerun successfully. Its 640 cases, 25,581 extraction
steps, maximum 99 steps, and seventeen distinct equation tags matched the
frozen report. These finite computations supplement the proof; they do
not verify algebraic geometry, analytic topology, or arbitrary dimension.
The audit manifest additionally pins the exact inputs and primary local
source files. CHECKS.json records the mechanical and visual details.

## 3. Original-field monomial construction

The completed regular local ring at p has dimension n+1 and residue field
kappa(p), of characteristic zero. The Cohen power-series description with
the specified regular parameters is legitimate. The coefficient field is
chosen in the completion; no coefficient field is asserted to lie in the
uncompleted local ring. The equal-characteristic assumption here is
essential to the written source interface.

All OLD normal weights are positive. Therefore only finitely many
nonnegative exponent vectors have weight below any fixed bound. The
weighted initial form of a nonzero series is a nonzero finite polynomial,
and multiplication of initial forms takes place in a polynomial domain.
This proves multiplicativity even when distinct monomials have equal
weight; irrational independence is NOT needed for initial existence.

The valuation restricts from the completion to the local ring and then to
K(X). Injectivity of completion follows from separatedness/Krull
intersection for this Noetherian regular local ring. The local units have
value zero. Since pi is a unit times the monomial with multiplicities N_i,
the relation N.alpha=ell gives the required value of pi; a K-unit is an
R-unit and hence a local unit. Thus the restriction is the specified
absolute value on K, not a renormalized or extended-field valuation.

The resulting point has generic algebraic support. On a common nonempty
generic affine open, coordinate functions are rational functions in K(X);
their values are differences of weighted-series minima. On a small
positive-weight box, high-total-degree terms have uniformly large value.
The minima are locally finite minima of linear functions, giving
continuity for every coordinate-ring evaluation, hence the actual
Berkovich topology. Evaluating z_i recovers alpha_i, so this is an
embedding, not merely a continuous map to a tropical target.

Coefficient-field and unit-generator independence also check. Independent
OLD weights are dense in N.alpha=ell: no nonzero homogeneous rational
linear form vanishes identically on this affine hyperplane. At such a
weight, a finite leading expansion has a unique minimal term, and a
centered valuation is forced to take its value. Positive normal weights
control the remainder in any completion. Continuity then compares choices
at the dependent weights as well. This is the local BFJ argument, applied
explicitly to horizontal parameters with N_i=0; no literal BFJ theorem
about pairs with horizontal boundary is invented.

## 4. Global centers, actual Rees charts and regularity

The closed intersection of selected global boundary components is regular
of the expected codimension. On a Noetherian regular scheme its connected
components are disjoint irreducible components, open and closed in that
intersection. The component through the tracked point is therefore a
global CLOSED regular center. It is not the locally closed open stratum.
Local boundary equations define its ideal near each of its points.

For the chart with selected pivot x_j, consider the polynomial ambient
ring and equations x_i-y_i x_j. At a point lying above the center, the old
regular parameter classes stay independent after passing to the polynomial
ambient local ring: polynomial projection is smooth, and its regular
fibre parameters supplement the old parameters. This is exactly the
cotangent fact used in Stacks 41.21.3. The equation classes
[x_i]-lambda_i[x_j] are independent; [x_j] is independent of their span.
A quotient by these independent parameter classes is regular, and x_j
remains a parameter and a nonzerodivisor. The polynomial localization
argument works over the actual residue field, including non-rational
points of the exceptional fibre.

When x_j is invertible, the equations solve for every y_i. Since x_j has
no torsion in the quotient, localization embeds it into A[1/x_j] with
image A[x_i/x_j]. This identifies the displayed quotient with the genuine
affine Rees chart; it does not leave an embedded component on x_j=0.
Checking all local rings above x_j=0 suffices for this nonzerodivisor
assertion, while outside x_j=0 it is automatic.

The exceptional coordinate, the selected ratios that vanish at the point,
and the unselected old boundary parameters form part of a new regular
parameter system. For ratios with nonzero residue there is no boundary
component through that point. Thus the reduced total-transform boundary
really is strict SNC at EVERY point of the center, not only the tracked
coordinate point. The same computation retains extra stratum parameters
when the center has positive dimension.

At the tracked coordinate point all the new boundary coordinates are zero
and its residue field remains kappa(p). Its cone replaces one basis vector
by the sum of the selected vectors; the determinant is plus or minus one.
It is a regular lattice cone. Exceptional multiplicity is the SUM of
selected multiplicities, namely N.b_J. No saturation, extraction of a root,
or reduced-semistable convention is inserted.

Every selected center contains a vertical component among its equations,
so it lies in the special fibre. Its ideal is vertical (indeed pi vanishes
on this reduced center), making the blowup the identity on the generic
fibre. The charts remain integral, the resulting R-scheme is torsion-free
and hence flat over the DVR, and properness follows from the projective
blowup of a finite-type ideal and the proper old model. Projectivity of
the original model was not assumed or needed.

## 5. The delicate zero-weight faces

This is the main nonformal point in the analytic part, and the frozen
proof addresses it correctly. Merely substituting weights into the old
monomials would not alone identify analytic points on new faces.

Write the original coordinates as exact monomials in the coordinates of
a tracked final chart. The exponent matrix is unimodular with nonnegative
entries. Partition the new coordinates into J_+ of positive weight and
J_0 of zero weight. Every OLD weight is still positive on the final
simplex, so every old coordinate contains a factor from J_+. Consequently
the corresponding coordinate stratum is over the original closed p.

After flat completion at p, the iterated Rees charts are the coordinate
toric charts of kappa(p)[[z_0,...,z_n]]. On the stratum, all old parameters
vanish and the remaining nonzero coordinates are free torus coordinates.
Thus its generic residue field is kappa(p)(y_j:j in J_0). This is a
statement about the actual fibre stratum: base change to the completion
preserves the fibre at p and its residue field. Localizing the tracked
chart does not impose an algebraic relation on these free coordinates.

One can make the coefficient compatibility explicit without adding a
hypothesis. Because every old parameter maps into the positive-coordinate
ideal, the map from the old local ring extends continuously from its
completion into the completed local ring at the stratum generic point.
The old chosen coefficient field embeds there. The actual zero-weight
coordinates and this field generate a copy of the displayed rational
residue field: every nonzero polynomial in those coordinates has nonzero
residue and is invertible at the generic point. It supplies a compatible
coefficient field for the new positive-coordinate power-series valuation.
This spells out the mechanism already present in the frozen proof.

For a finite old polynomial, group terms by exponents of J_+. The distinct
old exponent vectors have distinct full new exponent vectors by
unimodularity. Within a fixed J_+ exponent the coefficient is consequently
a nonzero Laurent polynomial in the algebraically independent residual
J_0 coordinates. It has value zero. Distinct J_+ exponents remain distinct
monomials over that residue field even if their numerical weights agree.
Hence no cancellation lowers the claimed initial-value comparison.

For the infinite old series, compactness of the final simplex inside the
positive OLD orthant gives a common bound epsilon>0 on all old weights.
Old total degree d has value at least d epsilon. Thus each bounded-value
calculation has only finitely many old terms, uniformly even when some
new weights approach zero. This is the correct tail bound; a nonexistent
positive lower bound on the NEW weights was not used.

It follows that the face valuation is exactly the original monomial point,
centered at the generic point of the corresponding new stratum. The same
argument covers vertices, all lower-dimensional faces, and the interior.
The construction therefore controls the whole closed simplex in the
ordinary analytic space.

## 6. Finite extraction, contraction and the whole proper curve

The primitive-ray algorithm has the right direction and termination
measure. In a current lattice basis write a=sum a_i b_i with nonnegative
integer coefficients. For the positive support J and a minimal a_j,
the new coefficients are a_j for b_J and a_i-a_j for i in J except j.
Their sum decreases by (|J|-1)a_j>0. At least one selected multiplicity
is positive since N.a>0. Thus every step is an allowed vertical stratum
blowup. Zero coefficients cause no difficulty; the corresponding basis
vectors are retained. When only one coefficient remains, primitivity and
unimodularity force it to equal one. This is an actual finite extraction
on a chosen sequence of global charts, not an appeal to density of
divisorial points or a potentially singular fan subdivision.

Once a is a ray, the repeated two-component blowup uses the chart retaining
a and replacing b_i by a+b_i. It retains the strict transform of E_a, not
the exceptional divisor under the same name. Iteration gives
b_i+k_i a while the other rays remain fixed. Each center is vertical
because it lies on E_a. With M=N.a>0 and M_i=N.b_i>=0, the new multiplicity
is M_i+k_i M, including when the original b_i was horizontal.

The normalized vertices P(b_i+k_i a) tend to P(a) by the exact displayed
fraction. The basis stays unimodular and linearly independent, so its
slice by N.x=ell is an n-simplex, not a degenerate convex hull. Every
generator now has strictly positive OLD coordinates. Taking all vertices
inside a convex ball B with compact closure inside V intersect
iota^{-1}(W) puts the entire closed simplex inside that ball. Section 5's
face check upgrades this convex calculation to actual containment in W.
No claim about the full inverse image of a tropical box follows, and the
candidate does not make one.

For a facet, the connected component C of the closed intersection of its
n vertical divisors through the tracked p' is regular of codimension n.
It is a whole integral curve, not an open stratum. All selected divisors
are vertical, so it is closed in the proper special fibre and is proper
over k. Characteristic zero makes k perfect, and regular finite-type
k-schemes are smooth. Geometric connectedness and a k-rational point are
unnecessary.

The generic point of C is the center of the facet-interior valuations.
Their strictly positive OLD weights give center p on the old model.
Since p is closed, every specialization of eta_C also maps to p. Hence
the WHOLE C maps to p; this conclusion is not inferred just from the
tracked closed point p' mapping there.

For facet multiplicities m_j>0, beta lies on
sum m_j beta_j=ell, beta_j>0. No nonzero homogeneous rational hyperplane
contains this affine hyperplane. Each such hyperplane cuts a nowhere
dense closed subset of the facet interior; the countable union has dense
complement by Baire. Thus independent NORMAL weights are dense without
requiring the original xi to have independent weights or be retained
on this wall.

## 7. Example, obstructions and source scope

The P^2 example checks directly. For N=(1,0,0), extracting (1,1,1) and
retaining it in the two later shears gives multiplicities 1,m,m and
vertices (ell,ell,ell), (ell,ell+ell/m,ell),
(ell,ell,ell+ell/m). The facet opposite the first vertex has
m(beta_1+beta_2)=ell and maps to
(ell,ell+beta_1,ell+beta_2). An irrational positive ratio gives the stated
independence. Multiplicity m is retained, never replaced by one.

The obstruction to a stronger through-xi statement is valid: an
(n-1)-face uses at most n positive normal coordinates, while its original
weights are integer linear combinations of them. An original (n+1)-tuple
of independent weights cannot have this form. Likewise a single finite
subdivision has only finitely many facets and cannot make them dense in
an open n-cell. The model here appropriately depends on the neighborhood.

The source scope is honest. BFJ works over a complete DVR with residue
characteristic zero, no algebraic closedness assumption, and permits
nonreduced multiplicities, but uses vertical dual complexes and an
extra irreducibility convention on intersections. The candidate proves
the horizontal and connected-component refinements rather than silently
quoting them. BFJ Theorem 3.15 yields normal, vertically Q-factorial
subdivision models, not automatically regular models; the candidate's
direct coordinate blowups supply regularity. GRW's algebraically closed,
strictly semistable pair framework is comparison only. None of its
reduced-chart conclusions is used over an arbitrary original K.

## 8. Remaining gates, validation and preservation

No required correction is identified. In particular no independence
hypothesis on the originally specified alpha, no projectivity assumption,
and no geometric connectedness assumption on C was added to obtain PASS.

The theorem supplies nearby wall geometry ONLY after an actual model cell
has been provided. It does not put a wall into an arbitrary source cell,
give full ordinary-W tube containment, compare unrelated cell constants,
or prove source representation, closed-current transport, or rigidity.
In a source-cell application the relative open containment required in
Section 8 remains an explicit separate input. A shared dimension, common
target image, or density claim cannot replace it. The reviewer's separate
capture and outer-collar work was deliberately not imported.

The PDF skill was used read-only. Full rendered BFJ pages 14, 15 and 18
and GRW page 8 were independently inspected; all were legible and complete,
and the relevant equations and headings agree with the extracted text.
The larger source passages were read in full text as specified in the
source matrix. These fresh renders exited zero with no warning output.
No TeX compile or PDF artifact was produced, and the author's separate
eleven-page QA history is not misrepresented as this reviewer's work.

All authored audit files were scanned for every byte below 0x20 except
LF/tab, and DEL, including embedded carriage returns. Final results and
exact pins are in CHECKS.json and the audit manifest. Candidate and source
files remained unchanged. Only this new audit dossier and disposable
read-only-render PNGs were written; no live manuscript, frozen candidate,
git state, production endpoint, or permission configuration was changed.

This PASS records an independent exact-revision mathematical review, with
the prior related-work provenance stated above. It carries no novelty,
priority, production-acceptance, integration, or inventory-retirement claim.
