# Primary-source ledger: normalized links of reduced curve germs

Checked on 11 September 2026.  The proof packet uses only the following
primary Stacks Project results.

- [Tag 07QV — excellent rings](https://stacks.math.columbia.edu/tag/07QV):
  an excellent ring is quasi-excellent and universally catenary; in
  particular it is Nagata.  This is used only to pass from the theorem's
  Nagata hypothesis to reduced excellent complex curve germs.
- [Tag 0C1R — normalization of one-dimensional schemes](https://stacks.math.columbia.edu/tag/0C1R):
  for a reduced Nagata scheme of dimension one, normalization is finite;
  in the local affine case the normalization is semilocal and a finite
  product of Dedekind domains.  This supplies the finite branch set and its
  local normal rings.
- [Tag 00PD — discrete valuation rings](https://stacks.math.columbia.edu/tag/00PD):
  a Noetherian local normal domain of dimension one is a DVR.  This turns
  every localized normalization branch into a normalized order.
- [Tag 00IC — valuation rings are normal](https://stacks.math.columbia.edu/tag/00IC):
  a valuation ring is integrally closed in its fraction field.  This forces
  a real valuation centred on a curve component to dominate one of the DVR
  branches of its normalization.
- [Tag 00OK — dimension under integral extensions](https://stacks.math.columbia.edu/tag/00OK):
  an injective integral extension preserves dimension.  This is used after
  quotienting a finite local homomorphism by the kernel determined by a
  source branch, and shows that the contracted prime is a minimal prime of
  the target curve ring.
- [Tag 09E4 — extensions of discrete valuation rings](https://stacks.math.columbia.edu/tag/09E4):
  the normalized orders in an extension of DVRs differ by the ramification
  index.  This gives the first equality in the finite-map formula.
- [Tag 0BRL — ramification indices in towers](https://stacks.math.columbia.edu/tag/0BRL):
  ramification indices multiply in a tower.  This provides the branchwise
  check of compatibility with composition.
- [Tag 034W — ideals in Dedekind domains](https://stacks.math.columbia.edu/tag/034W)
  and [Tag 034X — characterizations of Dedekind domains](https://stacks.math.columbia.edu/tag/034X):
  nonzero ideals in each normalization factor have unique maximal-ideal
  factorizations.  Applied componentwise, this gives the conductor exponents
  and the invertible ideal with prescribed sufficiently deep branch orders.

The conductor is shown to contain a nonzerodivisor by directly clearing the
denominators of finitely many module generators of the finite normalization.
The required global generator is then selected by the Chinese remainder
theorem in the nonzero fibres of the prescribed invertible ideal; localization
and Nakayama prove that it generates on every branch.  These are elementary
steps recorded in the proof rather than additional sourced classification
claims.

The new conclusion is exactly an ideal-function result: sufficiently deep
integral branch orders descend to one primary principal ideal; the resulting
profiles form the strictly negative rational orthant, whose uniform closure
is the nonpositive real orthant; and its raw obstacle envelope is pointwise
truncation by zero.  No cited source or book-local argument identifies that
orthant with an independently constructed singular psh or nef cone, nor does
it claim an intersection product, Monge--Ampere operator, energy theory, or
higher-dimensional analogue.  Those layers remain open.
