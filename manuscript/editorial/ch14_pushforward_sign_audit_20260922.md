# Current pushforward and the involution — 22 September 2026

## Mathematical correction

Proposition 14.8.1 previously asserted sign-free commutation with J,
although its proof computed (-1)^(dim Y-dim X). The statement now
uses that computed sign, under the book's current convention
<JT,a> = (-1)^n <T,Ja>. The proof's claim that equal dimensions were
necessary is also corrected: an even dimension difference suffices.
This is an internal convention repair, not an assertion of an error
in Chambert--Loir--Ducros.

Pushforward preserves bidimension. The total bidegree changes by
twice the dimension difference, so the duality sign for d' is unchanged;
the two involution signs cancel for d''. A symmetric current of
bidegree (u,u) pushes to degree (u+n_X-n_Y,u+n_X-n_Y) with precisely
the required symmetry sign. The proof retains these calculations.
The section now explicitly assumes an analytic morphism.

The new Example 14.8.1 evaluates both operators for a rational point
embedded in the analytic line: i_*J_Y S = delta_p whereas
J_X i_*S = -delta_p. The point mass remains symmetric. The same
point in an analytic plane checks commutation in unequal even
dimensions. Appendix J records this convention and links the example.

## Consumer check

The actual production input closure was searched for consumers of the
pushforward proposition and functoriality corollary. The uses in
Chapters 11, 14 and 16 require projection, positivity, closedness or
weak continuity, not sign-free involution commutation in odd relative
dimension. Chapter 19's slope-formula proof did require a separate repair:
the skeleton retraction is a continuous map, not an analytic morphism.

Steps 1 and 2 of that proof now first identify the Poincare--Lelong
current with its finite signed atomic divisor measure and then use
continuous-map pushforward of Radon measures. The old inference that
every top-degree current on a curve is a measure has been removed.
This audit concerns those two steps; it is not a new verification
of the later slope-identification argument.

The consumer check also identified the next Chapter 17 work:
replace the unsupported identities involving pullback of arbitrary
currents by the canonical integration-current formulas, and replace
the exceptional-set shortcut in the generically finite projection proof.

## Validation and preserved material

The three complete revised blocks pass the strict Mingchen writing
audit with zero errors and warnings. A second mathematical reading
checks the dimension shift, both differential signs, symmetric degrees,
the point examples, and the continuous-measure definition.

The full source closure has 389 TeX files and 11,487 unique labels,
with no missing input, duplicate label, dangling reference or structural
defect. The open-problem inventory remains 46 atoms in 14 environments,
with tiers (0,5,8,16,17). The source diff is whitespace-clean.

The final complete build has 3,913 pages and 18,568,850 bytes,
zero unresolved references or citations, and zero horizontal or
vertical overflows. Physical pages 633, 634, 1432 and 3824
(printed 565, 566, 1364 and 3756) were rendered and inspected.

PDF SHA-256:
`2a45b91f321032f32ee9513e25d0be7327c57c4ae479bb300f2351c15908aa07`

The supplied CURVE_PSH.tex still equals the author's file byte for
byte (SHA-256
`9142aac73c5af7e4e715b3313def5ed56fae4e63e1ac8a53d0419df7d2194be9`).
Chapter 71 and the frozen research sources remain unchanged.
These are ordinary book corrections, not new mathematical production
verification gates or closure of any open research problem.
