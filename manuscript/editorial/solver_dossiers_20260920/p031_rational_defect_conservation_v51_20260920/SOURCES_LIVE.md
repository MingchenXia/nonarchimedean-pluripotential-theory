# Source audit

Audit date: 2026-09-20.

## External-source boundary

This packet introduces no new source-dependent analytic assertion. Its proof
is a formal synthesis of results already integrated and source-audited in the
v47 and v50 live packets.

The common published source behind those inputs is Walter Gubler, Philipp
Jell, and Joseph Rabinoff, *Forms on Berkovich spaces based on harmonic
tropicalizations*, Bulletin de la Societe Mathematique de France **154**
(2026), no. 1, 135--238, DOI `10.24033/bsmf.2919`; bibliography key `GJR26`.
The previously inspected publisher PDF had SHA-256
`acf1c49e853f5f126e02d694eacd4bea0cf018ab5d396830aa09d17b72d2884c`.

Relevant audited inputs are:

- printed pp. 190--191, Definition 7.8, Section 7.9, and Proposition 7.10,
  supporting the local PL--LFS cofinality theorem integrated in v47;
- printed p. 175, proof of Proposition 5.11, and printed p. 190, Section 7.9,
  supporting the finite-flat branch-retention and local LFS normal-form inputs
  used in v50.

No new claim is attributed to these passages in v51.

## Internal dependencies

- `eq:p031-local-real-rational-lfs-cofinality`: local rational--real LFS
  cofinality from v50.
- `thm:p031-local-pl-lfs-cofinality`: local PL--LFS cofinality at interior
  points from v47.
- `thm:p031-finite-flat-local-envelope-pullback`: exact local finite-flat
  pullback with a complete-fiber baseline from v50.
- `eq:p031-rational-lfs-envelope-pullback`: exact global rational-envelope
  pullback from v50.
- `eq:p031-finite-flat-pl-defect-balance`: the already integrated finite-flat
  PL defect balance from v50, recovered as a consistency check.
- `eq:p031-full-union-symmetry-defect`: identification of the PL pullback gain
  with the finite-orbit symmetry defect.

All labels resolve in the final full-book build.

## Provenance boundary

The v51 proof is rederived directly from the live v47 and v50 statements. It
does not import the v38 collar minimax formulas or the v49 local-repair
thresholds. No unpublished or quarantined assertion is used.

## Exact live hashes

```text
dd84bd600bf10e909e8c4861757e75bc56b13dde7b6e465e305a5d694ecf10e4  STATEMENT_LIVE.tex
6149b8dee66d59af92230d49875ffcc1e7570685f1123dd997743448ec705c80  PROOF_LIVE.tex
```
