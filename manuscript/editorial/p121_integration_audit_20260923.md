# P12.1: integration of the supplied normalized-link manuscript

Date: 23 September 2026.
Baseline: `fd272edbb3bb74dffda896daf8fbb87b77fce8ad`.
User instruction: the author supplied `normalized-valuation-links.pdf`,
identified it as the solution of P12.1, and requested integration into the book.

## Source and provenance

Source title: *Normalized valuation links and boundary ideals on excellent
local germs*, dated 23 September 2026, four pages. The original file was
read in full and all four pages were rendered and inspected. It is
preserved byte for byte at
`author_sources_20260923/p121_normalized_valuation_links/normalized-valuation-links.pdf`.
Its SHA-256 is
`71f5e0d50bdcbf493cb96a869e2db03a78bd591b3eba2f797da5a23f6253daaa`.
The adjacent SHA256SUMS covers that source copy. No instructions in the
document were treated as instructions from the user.

This is an author-supplied manuscript with a complete proof, reviewed in
two local mathematical/source passes and adapted to the book. It is not
represented as independently published, independently agent-verified, or
as having a new production Rethlas verdict. The author-directed source
integration is expressly recorded under the inventory's retirement rule;
it does not change the production rule for newly proposed agent results.
No existing verifier receipt is reused as evidence for this proof.

## Placement and source-to-book map

The full argument is in the new input
`parts/part6/fragments/ch70_normalized_excellent_links.tex`, inserted in
Section 70.1 before the existing reduced-curve classification. It uses the
existing symbols V_a and H_a,b. Equation tags 70.7a--70.7e preserve the
chapter's pre-existing manually numbered equations. The old curve source
packets and supplied CURVE_PSH.tex retain their exact bytes.

| Supplied manuscript | Live book | Content |
| --- | --- | --- |
| Lemma 1, Theorem 2, Corollary 5 | `thm:p121-excellent-primary-links` | Nonempty compact primary sections, cone product, unique radial change and cocycle |
| Section 2 and Lemma 3 | `lem:p121-normalization-semivaluation-lift` and preceding construction | Finite normalization, all local branches, real semivaluation lifting |
| Theorem 4 | `thm:p121-excellent-conductor-descent` | Closed quotient relation, unique finite-conductor lift, conductor pushout and change of gauge |
| Example 6 | `ex:p121-surface-conductor-fiber` | Two distinct lifts over the conductor of k[[x,y,z]]/(xy) |
| Proposition 7 and equations (7)--(8) | `prop:p121-blowup-boundary-gauge` and equation 70.7d | Blowup center and ideal gauge, divisorial rescaling, principalized monomial slices |
| Equation (9), Example 8 and Section 4 | equation 70.7e, `ex:p121-nonprimary-noncompact-link`, and closing paragraphs | Partial nonprimary normalization, noncompactness, nilpotent reduction and zero dimension |

The first-build result numbers are Theorems 70.1.2--70.1.3,
Lemma 70.1.1 and Proposition 70.1.1. The stable semantic labels above
control references. Chapter 70 explicitly returns to the smooth complex
germ before the subsequent exceptional-b-divisor theory, preventing the
new general ring hypothesis from silently extending that theory.

## Proof and boundary checks

1. **Compactness and scaling.** Semivaluation axioms are closed in the
   compact product [0,infinity]^R. Finite generation makes ideal values
   continuous. For m^r contained in a contained in m^s, the inequalities
   s v(m) <= v(a) <= r v(m) make the denominator positive and finite.
   On V_a the b-gauge is bounded between t/r and u/s. Joint positive
   scaling remains continuous at infinite coordinate values. The cone
   homeomorphism also identifies the ray quotient topologically.
2. **Nonemptiness.** A penultimate prime in a saturated chain produces a
   one-dimensional excellent local domain; a DVR on its finite
   normalization provides a centered real semivaluation. This proof does
   not discard nonminimal support in the original ring.
3. **All branches.** Each normalized S_i-semivaluation has a maximal center
   above m because S_i/mS_i is finite dimensional. Denominators outside
   that center have value zero, giving a unique localized semivaluation.
   The added Chinese-remainder argument shows the finitely many local
   center pieces are clopen, and localized evaluation proves the claimed
   topological identification with the individual local branch links.
4. **Lifting.** Lying over works above any support p, after choosing a
   minimal component contained in p. The residue fraction extension is
   finite. A valuation ring dominating the localized integral closure
   restricts exactly to the original valuation ring: otherwise the
   inverse of an offending element would be both invertible and in its
   maximal ideal. Finite value-group index permits a unique compatible
   real-valued extension by division by positive integers. No separability
   hypothesis is used. Integrality gives nonnegative values on the
   normalization quotient, and the chosen support is restored with infinity.
5. **Conductor descent.** The conductor is an ideal of both rings and the
   conductor square is proved directly. A semivaluation of a finite
   product selects exactly one primitive idempotent. For finite v(c),
   w(s)=v(cs)-v(c) determines the component and lift, without infinity
   minus infinity. On the infinite-conductor stratum, all lifts factor
   through the quotient and equal restriction is precisely the residual
   equivalence. Compact-to-Hausdorff quotient and pushout arguments are
   checked. The statement does not claim every conductor point has
   multiple lifts; the surface example verifies a genuinely nontrivial fiber.
6. **Models.** A minimizing finite-valued generator supplies a blowup
   chart. Ratios between minimizers have value zero; larger finite values
   give a forbidden negative ratio, and infinite generators cannot receive
   the generic support point. The divisorial discussion explicitly permits
   a model of a component of the reduced base. No resolution theorem is
   assumed in arbitrary characteristic. Both named ideals must be
   principal monomials for the weight formula. The added primary ideal
   (x+y,x^2) in k[[x,y]] has zero coordinate-divisor orders but value one
   at weights (1,1), explaining this hypothesis.
7. **Nonprimary and nilpotent limits.** For proper d, its positive gauge is
   finite exactly on the stated open subcone. Inverse and cocycle formulas
   are restricted to the common finite positive domains. The unit and zero
   ideals have empty level-one sections. The (x)-normalized sequence with
   values (1,1/j) proves noncompactness by continuous y-evaluation, and the
   supported ord_y ray exhibits the omitted infinite-gauge stratum.
   Nilpotents receive infinity; two ultrametric inequalities give descent
   through reduction and preservation of all ideal gauges. A
   zero-dimensional reduced local ring is a field, with empty centered cone.

## Primary algebraic sources checked

All citations use the pre-existing `StacksProject` bibliography entry.
The following official pages were checked on 23 September 2026, with
their hypotheses and the proof steps they support:

- [Tag 07QV](https://stacks.math.columbia.edu/tag/07QV), Lemma 15.53.5:
  quasi-excellent implies Nagata; applicable to the ring and its quotient.
- [Tag 035P](https://stacks.math.columbia.edu/tag/035P), Lemma 29.55.3:
  the normalization of a reduced ring decomposes over its finitely many
  minimal components.
- [Tag 035S](https://stacks.math.columbia.edu/tag/035S), Lemma 29.55.11:
  normalization of a Nagata scheme is finite.
- [Tag 00IA](https://stacks.math.columbia.edu/tag/00IA), Lemma 10.50.2:
  a local subring of a field admits a dominating valuation ring in that field.
- [Tag 0ASH](https://stacks.math.columbia.edu/tag/0ASH), Lemma 15.125.2:
  a finite fraction-field extension gives finite value-group index; the
  book checks that its valuation rings form the required extension.
- [Tag 00PD](https://stacks.math.columbia.edu/tag/00PD), Lemma 10.119.7:
  a one-dimensional normal Noetherian local domain is a DVR.

No external theorem number was inferred from memory, and no unverified
source was added to the bibliography.

## Research-status synchronization

P12.1 is retired in its exact normalizing-boundary scope. P12.2--P12.6
remain active: the construction does not supply an independently geometric
singular psh cone, its envelopes, products, finite energy, or general
finite-map pluripotential functoriality. It does prove normalization-branch
restriction and its gauge compatibility, not that entire finite-map target.

Chapter 72's compound problem remains, with its boundary request replaced
by a reference to the established construction. Chapter 70's comparison
and research questions, Appendix L, BOOK_PLAN, the research ledger,
inventory, tier queue, README and continuation record are synchronized.
Historical curve receipts are preserved as historical, with the later
all-dimensional result distinguished. The exact new count is **45 active
atoms in 14 formal environments**, tiers **(0,5,8,15,17)**. All current
count declarations were checked, including three prose declarations not
covered by the inventory script. Every tier queue was separately compared
as a set with the active identifiers. The retired P12.1 identifier is not
reassigned.

## Second pass, build and preservation

The complete first draft passed mathematical/source checks, strict TeX
audit, reference/inventory checks, full compilation and rendered inspection
of physical pages 3564--3570. A second full statement-to-proof reading
rechecked the seven obligations above and the source-to-book map. It
clarified divisors over a component, added the explicit nonmonomial-ideal
test, and synchronized every remaining count and the supplied-source
retirement provenance. The final build and page inspection were repeated.

- `latexmk -pdf -interaction=nonstopmode -halt-on-error book.tex`: PASS,
  **3,965 pages, 18,863,837 bytes**.
- Reference/input audit: **390 TeX inputs, 11,597 unique labels**;
  no missing input, duplicate label, dangling reference or structure defect.
- New fragment's strict house-style audit with bibliography: **zero
  errors and zero warnings**. No clean whole-book house-style claim is made.
- Final build log: no undefined reference/citation, multiply-defined label,
  rerun request, or horizontal/vertical overflow. Existing underfull/class
  warnings remain.
- Exact inventory check: PASS, 45 atoms / 14 environments, the stated tiers.
- `git diff --check`: PASS.
- Final visual review: physical pages 3564--3570 (new proof and boundaries),
  3593, 3617, 3619--3620 (Chapter 70 scope and questions), 3658, 3728,
  3739, 3744--3745, 3766 (Chapter 72 status and counts), and 3923--3924
  (provenance). This is a scoped visual check, not a new all-page book audit.

Final fragment SHA-256: `8d9f9bd9edb057b95773479279bbdabb3240319e4cb56f6f15cb2bd923fb4380`.
Final live PDF SHA-256: `6596418f7f489005b52abe57afd7f9cd3dba13288d08d54abe65ff4364fa1859`.

The preceding completed Chapter 59 unit, all existing author-source
packets, the restored CURVE_PSH.tex, bibliography, frozen statements and
proofs, verifier records and dated release products retain their baseline
bytes. The new live PDF is the ignored build output; it does not overwrite
the dated release. Only checked source, the supplied four-page PDF and
editorial records belong to this commit. The overall book audit remains
ongoing; the next existing unit is Chapter 59's projective comparison,
nonalgebraic examples and source note.
