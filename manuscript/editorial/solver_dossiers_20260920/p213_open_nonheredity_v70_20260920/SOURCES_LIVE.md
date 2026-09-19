# P21.3 v70 source ledger

Date: 20 September 2026.

## External source boundary

Walter Gubler, Philipp Jell, and Joseph Rabinoff, *Forms on Berkovich
spaces based on harmonic tropicalizations*, Bulletin de la Société
Mathématique de France 154 (2026), no. 1, 135--238,
<https://doi.org/10.24033/bsmf.2919>.

- Proposition 5.11: finite-flat descent of real PL functions, cited
  elsewhere in the surrounding chapter.
- Definition 7.2 and the harmonic functoriality results used by the existing
  book interface.
- Corollary 7.15 in the published numbering: on a good separated strict
  analytic space, the Hessian current of a harmonic function vanishes on
  the complement of the boundary. The present product open is boundaryless,
  so the current vanishes everywhere.

The curve comparison, residual-Picard quotient, proper-curve-bundle
descent, ordinary CLD pullback, and mixed exact-tower interface are imported
through exact book-local statements recorded in DEPENDENCIES_STATEMENT.tex
and the two exact dependency packets attached to the repaired verifier
request.

## Scope boundary

The source result converts Gubler--Jell--Rabinoff harmonicity to vanishing
Hessian current on the boundaryless product open. It does not make the
function ordinary CLD-smooth. That distinction is precisely what the
counterexample exploits.
