# Trait resolution and a vertical monomial presentation

Date: 4 October 2026. This book-external derivation continues the
[compatible height-slice reduction](li_face_compatible_dilation_and_semistable_scope_20261004.md).
The scheme-theoretic input is now anchored in actual current primary
files rather than an in-preparation citation. The known resolution
theorems remain imports; no independent exact-byte verifier receipt or
new book theorem is asserted.

## 1. The scheme category over a convergent trait

Let R be a quasi-excellent characteristic-zero DVR with uniformizer t,
B=Spec R and U=Spec Frac R. Give B its divisorial fs log structure,
with chart N -> R, 1 -> t. Let Z -> B be a normal integral flat
projective scheme of finite presentation with smooth geometrically
integral generic fibre. Supply an ample model line bundle A_0 whose
generic restriction is a specified power L^{k_0}.

For R=C{t}, excellence is a known input explicitly recalled in
Jonsson–Mustata, Valuations and asymptotic invariants for sequences of
ideals, Section 1.1, printed page 2152, physical PDF page 9. The
cached published PDF and its text were checked at this location.
This does not prove excellence from first principles; it clears the
stated scheme hypothesis. A finite-type R-scheme is again excellent.
Normal noetherian schemes in this category are formally equidimensional,
as recalled in ATW Remark 1.2.4(iii), physical page 3.

A projective embedding Z -> P^N_R gives the global ambient embedding
needed in ATW Theorem 1.2.12. Give the ambient projective space the
pullback of the base log structure and Z the induced log structure.
The embedding is strict. The ambient projection is strict and smooth,
hence log smooth. ATW Lemma 2.5.12 supplies abundance of derivations,
and thus the ambient is a relative logarithmic orbifold. The generic
fibre of Z has trivial log structure and is smooth, so its morphism is
generically logarithmically regular. These are the actual inputs of
the theorem, not a claim about arbitrary analytic families.

ATW Theorems 1.2.12 and 1.2.14, arXiv:2003.03659v2, physical pages
6–7, provide a representable relative desingularization after a
blowup of the base. The centre on the source is disjoint from its
logarithmic regularity locus. Every nonzero coherent ideal on Spec R
is principal, so its blowup is the identity. The admissible blowup
in this existence statement is not the zero ideal. Remark 1.2.7(ii),
physical page 5, explicitly discusses automatic success over a field
or DVR with this log structure. Consequently the scheme method
applies over the original trait.

It outputs a scheme Y -> Z that is a blowup of a coherent ideal I_0.
Since the generic fibre is already log regular, the centre avoids it:
I_0|_U=O_{Z_U}. Thus the blowup is vertical, projective and an
isomorphism of the fixed generic family. This is stronger than
merely knowing that a vertical blowup dominates the output.

The morphism Y -> B is log regular and locally of finite presentation,
and therefore log smooth. ATW Section 2.3.1, physical page 20,
records this equivalence. Molcho–Temkin arXiv:1907.02754v2,
Theorem 5.2.8, physical pages 16–17, supplies the exact chart
criterion; Lemma 5.1.2 supplies composition and strictness. Together
with the log regular base this makes the fs log scheme Y absolutely
log regular. Its normality is the standard Kato fs-log-regular input.
Hence its ordinary blowup is already its normalized blowup. This
normality input is explicit, rather than inferred just from an
unrestricted word such as toroidal.

The full ATW principalization/order-reduction algorithm and every
destackification antecedent have not been freshly verified. The
newly read Theorem 1.2.14 proof uses Appendix A's relative
destackification and the earlier torification literature. The
argument above is an application of the known scheme theorem,
not an independent new proof of relative desingularization.

## 2. Why the analytic extension is kept separate

ATW Section 9.2, physical page 81, discusses extensions to formal
and analytic geometries. Even for one-dimensional bases it phrases
the needed relative-manifold assertion as an expectation and states
the ensuing extension conditionally. That paragraph does not supply
an unconditional analytic desingularization theorem of the strength
needed here. The scheme over C{t} is a different application: its
ambient projective scheme is finite type over an excellent DVR and
meets the stated theorem hypotheses directly.

Converting a supplied projective analytic germ to this scheme, and
converting its resulting blowups back to an actual germ, still uses
the previously recorded projective-germ/analytic comparison. The
scheme argument does not silently resolve all nonprojective analytic
families. Projectivity, finite presentation, normality, formal
equidimensionality and the generic smoothness hypothesis all remain
visible.

## 3. The base root stack has a specific trait atlas

On the rank-one base fan, a subdivision changes no ray. A lattice
alteration of index q replaces the base chart N by (1/q)N. Its
relative root stack has the presentation

    [Spec R[tau]/(tau^q-t) / mu_q].

This is a consequence of the rank-one toric/root construction in
ALT Example 4.3(ii) and the relative toric-stack presentation.
The atlas B_q=Spec R_q, R_q=R[tau]/(tau^q-t), is a mu_q-torsor
over the stack; it is finite etale as a map to that stack in
characteristic zero. Its map to the coarse original trait is
ramified. These two maps must not be confused.

The polynomial is Eisenstein. R_q is a DVR with uniformizer tau,
residue field that of R and fraction field a degree-q extension
of Frac R. For the convergent complex trait it identifies with
C{tau}: every convergent power series splits uniquely into its
q residue classes of exponents, sum_{j=0}^{q-1} tau^j f_j(t).
The convergence radius of each f_j is positive. This checks the
actual cyclic parameter rather than introducing an unspecified
alteration of the generic CY variety.

The saturated toroidal pullback of Y to B_q agrees locally with
the normalized monomial cover. Its comparison to the ordinary
fibre product uses fs saturation and the normalization statement,
not equality of unnormalized roots with normal toric charts.
The local integral-closure calculation and Ambro's normalized
root theorem in the earlier dossier control that step. Geometric
integrality of the original generic fibre prevents a generic
split-component ambiguity after the field extension.

ALT's projective monoidal subdivision can then be pulled to the
scheme atlas. A representable subdivision of a toroidal scheme
is a scheme. The strictly etale atlas preserves total regularity
and reduced normal-crossings properties obtained on the stack.
Strict global SNC, as opposed to etale-local normal crossings,
must be included in the supplied subdivision/strictification
conclusion. An arbitrary subsequent blowup is not substituted:
it can introduce central multiplicities. The earlier compatible
height-cone specialization remains the source of height-one rays.

## 4. A compatible support function gives global vertical ideals

Here supply a finite fs toroidal chart system for a normal Y_q,
with the central parameter tau positive on every nonzero cone.
Supply a finite rational coherent subdivision and a compatible
support function on that chart system, invariant under its chart
identifications and monodromy. Compatibility of the heights is
stronger than merely matching the underlying cell subdivisions.
These are precisely the data whose existence was kept explicit
in the previous ALT audit.

Use the concave convention: locally the function lambda is the
minimum of finitely many linear character forms, and its domains
of linearity are the supplied cells. First clear all denominators.
Then add C times the globally defined parameter height, with C
one sufficiently large integer for the finite chart system.
Each defining character form is now in the dual positive cone.
This does not change its domains of linearity. Write the resulting
integral support function again as lambda.

On a chart with sharp fs monoid P, character lattice M=P^gp and
dual cone sigma, define the exponent ideal

    J_sigma = {m in P : <m,v> >= lambda(v) for every v in sigma}.

It is an ideal of P. The rational polyhedron defined by these
inequalities has recession cone sigma^vee; rational-polyhedral
finite generation/Gordan's lemma makes J_sigma a finitely
generated monoid ideal. Equivalently it is the integrally closed
monomial ideal determined by the supplied support function.
These are standard toric inputs, not assertions that an arbitrary
coherent ideal is monomial.

Its restriction to a face is the corresponding exponent ideal
on that face. The nontrivial inclusion can be checked directly.
Lift a face character to the localized character lattice. Choose
a monoid element l that vanishes on the face and is strictly
positive on every other ray of the original cone. Adding Nl
does not change the localized character. The support function
is linear on finitely many subdivision cones, so its inequalities
need be checked only on finitely many subdivision rays. On
face rays they already hold; on other rays one sufficiently
large N makes them hold. Thus the lifted character lies in the
original exponent ideal after multiplying by an inverted monomial.

If a chart character is multiplied by a unit, the generated
ordinary ideal is unchanged. The exponent-ideal construction
therefore glues through the prescribed chart identifications
and descends through the etale chart groupoid. Finitely many
charts and finite monoid ideals give a coherent global ideal
I_lambda on Y_q. This is the local-to-global step; it uses an
intrinsic compatible support function, rather than unrelated
chartwise choices of shifts or heights.

A sufficiently large multiple N of the parameter height lies
above lambda on every subdivision ray. Hence tau^N is in each
local exponent ideal, with N chosen uniformly across the finite
system. The ideal becomes the unit ideal off tau=0, so it is
vertical and nonzero. Coherence ensures that its normalized
blowup has exactly the prescribed domains of linearity: on
each monomial blowup chart one adjoins character ratios and
saturates the semigroup, as in the prior affine calculation.
Face compatibility gives the prescribed global toroidal scheme.

Thus a supplied compatible integral coherent toroidal subdivision
has a finite vertical normalized-blowup presentation. This is
a direct elaboration of the usual toric ideal/support-function
dictionary, with its chart descent written out. It does not
independently provide the omitted canonical height functions in
ALT's general combinatorial construction.

## 5. The positive model can now be composed on this route

The route has a vertical ordinary blowup from ATW, finite
normalization of a cyclic cover, and a supplied compatible
toroidal normalized blowup. Initial finite normalization can
also be included if a normal model was not originally supplied,
provided the finite-normalization hypothesis and the original
polarization have been checked.

At a finite step, relative ampleness pulls back. At a blowup
step its tautological ideal bundle is relatively ample and
trivial on the fixed generic fibre. The earlier normalized-model
dossier composes these bundles with suitable powers of A_0
to obtain an ample extension of a power of the same L on the
final regular reduced model, without adding another blowup.
Its positive total Kähler reference, meromorphic comparison
and complete ramified normalization apply under the recorded
scheme/germ hypotheses.

The genuine remaining imports are the known ATW algorithm and
destackification, the fs log-regular/normal dictionary, ALT's
compatible coherent resolution including strictification, and
the projective-germ comparison. This checkpoint removes the
in-preparation-source ambiguity and supplies the vertical
monomial ideal descent under explicit finite support-function
data. It does not announce a new universal analytic theorem,
an independent proof of all semistable reduction, or admission
of the book-external general CY argument.

## 6. A small literal descent diagnostic

Molcho–Temkin v2 Lemma 3.3.4, physical page 9, assumes only a
strict flat map X_0 -> X, yet concludes that the quotient of
its Log groupoid is Log_X. Without surjectivity this conclusion
fails: take X nonempty and X_0 empty. The source groupoid and
its quotient are empty, while Log_X contains the identity object.
This is an omitted covering hypothesis in the literal auxiliary
statement. Its uses on pages 10 and in the present construction
are on strict surjective covers. The diagnosis neither disproves
the chart theorem nor changes the scope of the main application.
