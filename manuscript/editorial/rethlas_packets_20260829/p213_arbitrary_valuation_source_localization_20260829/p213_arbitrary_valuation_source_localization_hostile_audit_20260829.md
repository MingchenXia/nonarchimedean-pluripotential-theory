# Hostile audit: arbitrary-valuation source localization

Date: 29 August 2026

Verdict: **PASS; zero critical errors and zero mathematical gaps.**

This is a source-aware audit of quarantine bytes, not a production-verification
receipt and not a novelty or priority claim.  The statement and proof were not
edited.

## Exact candidate bytes

- statement SHA-256:
  `bf3ff5c049481075087988a4ce4e381ab0b07346cad6cfdf7264c6d321802d46`;
- proof SHA-256:
  `d7ea3c463f1e4aff1ef7bae07cb3d093767b9175c1ead54ef2575c8086095d84`.

The dependent strengthened localization bytes audited separately are:

- statement SHA-256
  `335532b6a0b71b4174c97246e06cd6ea473d61dd83402fcd709301408692f3db`;
- proof SHA-256
  `77da7aa9b84888aad5d6459f04c6b93ca5d9cb273c0d0776c9b7911aa0be3900`.

The primary source checked was
`/private/tmp/p21_bridge_sources/cld25.pdf`, SHA-256
`5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719`.
The dependent normal-curve input additionally uses
`/private/tmp/p21_bridge_sources/ducros_curve.pdf`, SHA-256
`b514eaa16c0a531880672956d08ee75a4026d75f61303446044468937c9342ad`.

## 1. Local moment blocks

CLD Proposition 15.1.1(b) gives an ordinary open local presentation

`alpha=F_form^* eta`.

The prescribed finite analytic block `G` remains defined after shrinking.
When a smooth cutoff `chi` is part of the data, CLD Corollary 15.1.2 gives a
local analytic moment `H` and a smooth function `Phi` with

`chi=Phi o H_trop`.

Shrinking the common open set ensures that `Phi` is defined on a neighborhood
of `H_trop(V)`.  Concatenating the boundary, form, prescribed, and cutoff
blocks is legitimate.  Pullback from the form projection recovers `alpha`,
while equality of full tropical values implies equality of the `H` projection
and hence fiber constancy of `chi`.  No smooth cutoff is treated as an
analytic coordinate.

These source statements and their proofs do not require a nontrivial
ground-field valuation.

## 2. Exact audit of `partial(V/O)=partial(V/W)`

Proof lines 25--29 are correct.

The set `O` is open in `W`, and `V` is an analytic domain contained in `O`.
CLD 11.4.1 identifies `Int(V/O)` and `Int(V/W)` with the ordinary interiors
of `V` in `O` and `W`, respectively.  Because `O` is open in `W` and
`V subset O`, these two ordinary interiors are equal: an open subset of `O`
contained in `V` is open in `W`, and the converse is immediate.  Taking
complements inside the common source `V` gives

`partial(V/O)=partial(V/W)`.

Thus the boundary-avoiding moment constructed inside `O` avoids exactly the
boundary required in the original `W`; no extra source-boundary term is
discarded.  Projection from the concatenated moment to `F_bd` preserves the
avoidance implication.

## 3. Open/proper localization and zero extension

Compactness of `V` makes its relative boundary compact.  Its tropical image
is compact and closed, so `Omega` is open.  The inverse image `U` avoids the
relative boundary and is therefore open in `W`; boundary avoidance puts `y`
in `U`.

The map `F_trop:V->R^N` is proper because its source is compact.  The map on
`U` is its base change over `Omega`, hence is proper.  Therefore the inverse
image of the compact support of `lambda` is compact in `U`.  The pulled-back
form has support in that compact set.  A smooth form compactly supported in
an open subset extends smoothly by zero, so the asserted extension to `W`
is valid.  On points whose tropical image lies where `lambda=1`, the form is
exactly `alpha` by the form-block identity.

## 4. Finite-cover consequence

Interpret “source cover” in the project-standard sense of a cover by open
source neighborhoods, or by source pieces containing such neighborhoods of
the covered points.  For every point of the compact test support, apply the
lemma with `W` chosen inside a prescribed cover member.  The resulting sets
`U_x` are ordinary open neighborhoods in the ambient curve and cover the
test support.  Compactness selects finitely many of them.

The ambient space is good and separated, hence locally holomorphically
separated by CLD 15.2.2.  The compact test support is closed and countable at
infinity.  CLD Corollary 15.2.9 therefore supplies smooth compactly supported
cutoffs subordinate to the finite open refinement and summing to one near
the compact set.  Local current comparisons consequently pass through the
finite decomposition.

If a newly chosen partition cutoff must itself occur in a moment
presentation, CLD Corollary 15.1.2 is applied locally to that cutoff and its
analytic block is appended.  If necessary, shrink and take a further finite
refinement; compactness terminates the covering step.  This does not assert
that the cutoff is an analytic tropical coordinate.

## 5. Noncritical precision notes and scope

Two wording points should be kept visible if these bytes are later edited:

1. The phrase “finite source cover” must retain its contextual meaning of an
   open-neighborhood cover (or pieces with open neighborhoods); the assertion
   is not intended for arbitrary subsets containing the points.
2. For partition functions chosen only after the first finite refinement,
   the proof's phrase “the preceding application” should be read as a fresh
   local application of CLD Corollary 15.1.2, followed, if needed, by finite
   refinement.  The existential conclusion remains valid.

Neither point is a mathematical gap in the stated project context.  The
result concerns ordinary CLD-smooth forms and nonrigid points of good,
separated, normal pure curves.  It makes no claim for weakly smooth forms or
for rigid points over a trivially valued field.  Subject to the required
independent production Rethlas pass, the dependent packet is mathematically
viable.
