# Live source ledger

Audit date: 2026-09-20.

## External source

Walter Gubler, Philipp Jell, and Joseph Rabinoff, *Forms on Berkovich spaces
based on harmonic tropicalizations*, Bulletin de la Societe Mathematique de
France **154** (2026), no. 1, 135--238, DOI 10.24033/bsmf.2919.  The project
bibliography key is `GJR26`.

Locally inspected published PDF:

```text
/tmp/GUBLER_JELL_RABINOFF.pdf
SHA-256 acf1c49e853f5f126e02d694eacd4bea0cf018ab5d396830aa09d17b72d2884c
```

Verified locators:

- Definition 7.8, printed p. 190: an R-PL function is LFS precisely when it is
  Fubini--Study at every point; Fubini--Study at a point implies semipositivity
  there.
- Section 7.9, printed p. 190: locally, an LFS function is an
  `R_{>=0}`-linear combination of maxima of `-log|f_i|` for invertible analytic
  units.  Together with a nontrivial value group, this justifies adding any
  nonpositive real constant while remaining LFS.
- Proposition 7.10, printed pp. 190--191: a semipositive R-PL function at an
  interior point admits uniform approximation by R-PL LFS functions on a
  strictly analytic neighbourhood.

The live proof uses Proposition 7.10 only locally.  It does not attribute
obstacle preservation to the source; the downward uniform-error shift is
proved in the manuscript.

## Internal dependencies

- `eq:p031-lfs-pl-envelope-chain`: the already integrated LFS/PL envelope
  chain for finite orbit presentations.
- `eq:p031-full-union-symmetry-defect`: identification of the full P03
  pullback defect with `Sigma`.
- `eq:p031-sectioned-globalization-balance`: the sectioned PL globalization
  balance.
- `cor:p031-local-section-orbit-fiber-closure`: group translates of a local
  section close the whole fibre when the base PL defect vanishes.

All four labels were present in the full build closure and resolved without
dangling references.

## Live-file hashes

```text
be51d633de5a4ddb45391a3ccf1ebcab18d8f33a1793c56f7e09f42ec0b9b771  STATEMENT_LIVE.tex
5b84eea9ee554805f587f651b33a3e4aace081317b8b066738f3c78e23865100  PROOF_LIVE.tex
```
