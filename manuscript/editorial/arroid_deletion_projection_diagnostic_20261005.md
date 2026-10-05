# Arroid deletion projection diagnostic, 5 October 2026

This is a research record outside active TeX. It checks the deletion-projection
step in Aksnes, *Tropicalization of curve arrangement complements and arroids*,
Math. Scand. 131(2) (2025), 177--208,
[DOI 10.7146/math.scand.a-156674](https://doi.org/10.7146/math.scand.a-156674).
The published paper was read in full. The candidate below challenges the
point-or-half-line assertion in Proposition 4.14's proof under the intended
distinct-curve intersection convention. It is not an independently admitted
new theorem, and it is not a counterexample to Theorem 5.4 or the simple-
arrangement cohomology criterion in Theorem 6.2.

The current book remains the published cohomological integration edition at
work commit `5494585b9afd900da1b76f601aebf288a11d5487`. Its Appendix G imports
the separate Aksnes--Amini--Piquerez--Shaw results and does not use the arroid
deletion argument or its later unique-balancing criterion. All 42 problem
statuses and the open catalogue remain unchanged.

## Source and reading evidence

The official 32-page published PDF was downloaded successfully from the
journal's article page. SHA-256:
`36f0e037f8b72448e753af06d49936c1f1133b6b4dafcfc12ac0dc9d9e6bcf99`.
The extracted text was read in full, lines 1--1466, in the successful bounded
ranges 1--220, 221--440, 441--660, 661--880, 881--1100, 1101--1320 and
1321--1466. Eighteen actual published pages were viewed in nine sheets:
physical 1, 6, 7, 11, 12, 15--23, 26, 27, 29 and 30, or printed 177,
182--183, 187--188, 191--199, 202--203 and 205--206.

The live arXiv history ends at [2404.14380v3](https://arxiv.org/abs/2404.14380),
revised 27 August 2025 and labelled the final version. Its acquired PDF is
30 pages, SHA-256
`ca116d8d8f2f2166290b68de8fc274384e9c2146a4a5789f62a30e67953ef948`.
Only targeted text ranges 450--600, 680--795, 830--875 and 1030--1125 were
read in this version; no fresh full reading of v3 is claimed. Its definition,
deletion-projection proof and downstream stated criteria retain the relevant
printed conditions. The published version controls this diagnostic.

| Primary anchor | Published locator | Role |
| --- | --- | --- |
| Graph-plus-vertical-ray modification | Definition 2.8, printed 182--183, physical 6--7 | A fibre over the projection is one graph point, optionally with an attached half-line |
| Abstract intersection axiom | Section 4.1 and Definition 4.1, printed 187--188, physical 11--12 | Separate repeated-coordinate issue described below |
| Deletion | Definition 4.8, printed 191, physical 15 | Erasing a curve index merges incidence sets |
| Incidence-cone support and weights | Section 4.2.2, printed 192--193, physical 16--17 | Explicit generators and multiplicity weights checked below |
| Claimed modification | Proposition 4.14 and proof, printed 194, physical 18 | Target point-or-half-line assertion |
| Geometric fan identification | Theorem 4.15, printed 195, physical 19 | Intended transverse very-affine geometric context; no fresh proof certification |
| Downstream uses | Lemma 5.1, printed 196, physical 20; Theorem 5.4 and Lemma 5.5, printed 197--198, physical 21--22 | Dependency scope to recheck after resolving the projection step |
| Restricted algebraic conclusion | Proposition 6.1 and Theorem 6.2, printed 202--203, physical 26--27 | These require a simple arrangement; the diagnostic arrangement is not simple |

The journal page dates publication to 22 July 2025. A bounded search for the
proposition, corrections and recent arroid papers did not supply an acquired
repair for this step. It is not an exhaustive literature search or a claim
that no correction exists. Search snapshots and acquisition records are pinned
in the accompanying manifest. Secondary search results with a different
journal volume do not override the actual published PDF.

## A distinction in the abstract definition

The displayed Bézout condition quantifies over all vectors in the Cartesian
power of the ground set, without excluding repeated coordinates. Taken
literally, its rank-two condition for `(i,i)` is incompatible with even the
three-line/conic incidence example on printed page 188: a degree-one line
there belongs to two recorded points, whereas its diagonal right side is one.
The same literal wording appears in the inspected arXiv v3 range. This is a
definition/convention issue, not a transcription of a missing inequality sign.

Ordinary plane Bézout counts intersections of distinct curves. The construction
below explicitly uses that intended convention. It satisfies all 15 distinct-
curve Bézout equalities, but is not represented as a literal model of the
uncorrected all-tuples abstract axiom. Consequently the diagnostic is stated
for the paper's incidence-cone construction on a genuine transverse curve
arrangement; it is not silently advertised as a formally verified counterexample
under an inconsistent abstract definition. No repair of that definition is
admitted to the book.

## An explicit transverse arrangement

Work over trivially valued `C`. Choose `r` with `r^2=-2`. In homogeneous
coordinates `[x:y:z]`, take the three coordinate lines, the extra line `M`,
and the two conics `C,D`:

\[
 L_x:x=0,\quad L_y:y=0,\quad L_z:z=0,\quad
 M:x+y/r-2z=0,
\]
\[
 C:x^2+y^2+z^2=0,\qquad D:x^2+2y^2+3z^2=0.
\]

Both conics are smooth. Their four intersection points are
`[s:rt:1]` for `s,t` in `{1,-1}`. All coordinates are nonzero, and the distinct
diagonal coefficient ratios `1,2,3` make the two gradients independent.
The equation of `M` at those points is `s+t-2`, so exactly the point
`[1:r:1]` lies on `M`.

On `M`, set `[x:y:z]=[2-t:rt:1]`. The two conic equations restrict to

\[
 C|_M=-(t-1)(t+5),\qquad D|_M=-(t-1)(3t+7).
\]

The roots are distinct. Their second points have nonzero coordinates and are
different from each other. The point of `M` at `z=0` is `[1:-r:0]`, with conic
values `-1,-3`. At the intersections of `M` with `x=0` and `y=0`, the conic
values are `(-7,-13)` and `(5,7)` respectively. Thus none of these coordinate-
line intersections adds an unrecorded triple point. Each coordinate line has
two distinct transverse intersections with each conic; the conics do not meet
on a coordinate line. All four lines are distinct, and `M` avoids the three
coordinate vertices. The arrangement is therefore pairwise transverse and
contains three lines in general position. Deleting `M` retains that very-affine
condition. There is one triple point and all other intersections are double.

Use indices `(0,1,2,3,4,5)=(L_x,L_y,L_z,M,C,D)` and degree vector
`d=(1,1,1,1,2,2)`. The incidence multiset is:

| Incidence set | Multiplicity |
| --- | --- |
| Each of the six pairs among the four lines | 1 |
| Each coordinate-line/conic pair | 2 |
| `{M,C}` and `{M,D}` | 1 each |
| `{C,D}` | 3 |
| `{M,C,D}` | 1 |

There are 24 geometric intersection points, 16 distinct incidence sets and
33 incidence cones. This is not a simple arrangement in the source's sense:
several distinct points have the same set of incident curves. In particular,
it does not meet the hypotheses of Theorem 6.2.

## The two fibres from the explicit cone formula

Use the paper's quotient spaces

\[
 N_{\mathbf R}=\mathbf R^6/\mathbf R d,\qquad
 N'_{\mathbf R}=\mathbf R^5/\mathbf R(1,1,1,2,2),
\]

and let `pi` forget index `M`. For an incidence set `p`, write
`v_p=sum_{j in p} e_j`, with brackets understood in the quotient. Section
4.2.2 constructs the union of cones `cone(e_j,v_p)` for `j in p`, assigning
each the occurrence count of `p`. This fixes the support used in the diagnostic;
weights do not change its projection fibres.

Let `q={C,D}` and `b=e_C+e_D` in the deletion space. Every original incidence
set omits at least one of the three coordinate-line indices. If a point in
`cone(e_j,v_p)` projects to `b`, write

\[
 \alpha e_j+\beta v_p=b+\lambda d+h e_M,
 \qquad \alpha,\beta\geq0.
\]

The omitted coordinate-line component forces `lambda=0`; the line `e_j`
also has zero component there because `j in p`. Nonnegativity then requires
`p` to be `q` or `q union {M}`. For `p=q`, both incidence cones give only
`b` at height zero. For `p=q union {M}`, the `C,D` cones give the height-one
point, and the `M` cone gives every height `1+alpha`, `alpha>=0`. Thus the
full fibre of the incidence-cone support over `b` is

\[
 \{b\}\ \cup\ \{b+h e_M:h\geq1\}.
\]

It is disconnected. For an interior point `b'=2e_C+e_D` of the deletion cone
`cone(e_C,e_C+e_D)`, the same missing-coordinate argument forces `lambda=0`.
The two `C` incidence cones, for `q` and `q union {M}`, give respectively
`b'` and `b'+e_M`; the corresponding `D` cone would require a negative
coefficient and the `M` cone cannot give the unequal `C,D` coefficients.
All other cones are excluded. The full fibre is exactly

\[
 \{b',\ b'+e_M\}.
\]

A modification as in Definition 2.8 has one graph point over every base
point, with a half-line attached at that graph point when the base point is
in the divisor. Both of the computed fibres fail that description. Changing
the vertical orientation or a linear splitting does not connect them, and
subdividing the same support cannot remove either component. The proof's
case distinction overlooks coexistence of an old incidence set `q` and
`q union {M}` before deleting `M`. In the example three `C,D` intersection
points avoid `M` and one lies on it; erasing `M` merges their tropical directions
but their extra valuations differ.

The exact script checks every one of the 33 cones, rather than sampling
fibres numerically. It also checks all 15 distinct-curve Bézout equalities,
the primitive ray generators and saturated two-cone lattices in
`Z^6/Zd` (using `d_0=1`), and each divisor's balance modulo its line.
The output records the complete feasible-cone list for both fibres.
These arithmetic checks support the local diagnostic; they are not an
independent model audit of all algebraic, topological or novelty claims.

## Scope of the unresolved repair

An additional exact computation checks that all 528 pairs of the 33 cones
intersect in their common face. It enumerates the minimal positive circuits
of the equality defining each cone-pair intersection, so that the cellular
complex below is checked for this geometric fan, not merely an abstract
incidence diagram. Over `Q`, it builds the three complexes with multi-tangent
coefficients, with each cone oriented by `(e_j,v_p)`, plus incidence at `e_j`
and minus incidence at `v_p`. The ray incidence at the origin is minus.
Every composition of the two boundary maps is exactly zero.

| Multi-tangent degree `p` | Chain dimensions `(C_0,C_1,C_2)` | Boundary ranks `(d_1,d_2)` | Homology dimensions `(H_0,H_1,H_2)` |
| --- | --- | --- | --- |
| 0 | `(1,22,33)` | `(1,21)` | `(0,0,12)` |
| 1 | `(5,63,66)` | `(5,58)` | `(0,0,8)` |
| 2 | `(10,41,33)` | `(10,31)` | `(0,0,2)` |

Thus the lower Borel--Moore groups do vanish in this specific example,
despite the failed modification projection. The ordinary fan cohomology
dimensions `dim H^(p,0)` are `(1,5,10)`, while their would-be dual top
Borel--Moore dimensions are `(2,8,12)`. Global Poincaré duality fails already
by these dimension comparisons. This supplies no counterexample to the
vanishing conclusion of Lemma 5.1, and does not settle the general statement.

The top balancing space has dimension two. It is parametrized by `beta,gamma`:
pair-incidence weights are `beta*d_i*d_j`, minus `gamma` on the three pairs
among `M,C,D`, and the triple-incidence weight is `gamma`. These two cycles
are checked independently against the exact boundary matrix and span its
kernel. The actual weights are `beta=gamma=1`; all cone weights are strictly
positive exactly when `beta>0` and `0<gamma<2*beta`. This finite computation
does not extend the book's one-dimensional envelope or orthogonality results
to surfaces.

This calculation isolates the universal projection assertion used in
Proposition 4.14, under the geometric convention described above. The printed
proof of Lemma 5.1 uses that proposition for arbitrary deletions; Theorem 5.4
and Lemma 5.5 then use the vanishing or modification route. Their proof route
therefore requires rechecking after the deletion step is clarified. No
counterexample to their final conclusions has been supplied. In particular,
a non-simple example does not refute the simple-arrangement Theorem 6.2.

A possible repair must handle collisions of incidence sets after deletion.
Refinement of the existing support alone preserves the disconnected fibres.
Separating boundary branches by an enlarged embedding, using a different
construction, or proving the required Borel--Moore vanishing directly are
routes to investigate, not established fixes. The all-tuples abstract axiom
also needs clarification separately from the projection issue.

This is related to the book's overlapping-tropical-branch examples: a tropical
image can identify distinct boundary branches whose additional valuations
remain different. It reinforces the need to verify faithful local charts and
all-stratum conditions. It does not solve P05 or P19, establish an envelope
regularity criterion, or alter the independently sourced AAPS comparison.

No theorem typography, problem retirement or production-verifier receipt is
added. Admission requires the repository's independent verification process
for any original result; the requested model preference does not constitute
an executed verifier call. Preserve this candidate and its exact computation
while continuing the source and direct-chain-complex checks.
