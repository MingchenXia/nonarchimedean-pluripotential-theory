# Reference ledger for the endpoint-only dossier

All descriptions below are paraphrases.  This file records source scope as
well as the locator, because the main topological reference of
Baker--Payne--Rabinoff assumes an algebraically closed ground field.

## Baker--Payne--Rabinoff

Source: *On the structure of non-Archimedean analytic curves*,
arXiv:1404.0279.

Local bytes:

- PDF: `/private/tmp/BPR14040279.pdf`
- extraction: `/private/tmp/BPR14040279.txt`
- PDF SHA-256: `5e40117270a0051d9661c9bbd0317968b810573796a5c2408582f20692568a11`
- extraction SHA-256: `70c4bbfbda088720c7e779e12bad023d50e434b8ae73acf9cf5b4068ad8c1c7d`

Locators:

- paper-wide hypothesis: introduction, printed p. 1; extraction lines 22--25:
  `K` is algebraically closed, complete, and nontrivially valued;
- standard closed/open annuli: Section 2, printed pp. 3--4; extraction lines
  166--202;
- Lemma 2.12, printed p. 7; extraction lines 348--365: a generalized annulus
  minus its skeleton is a disjoint union of open balls; each component
  retracts to one skeleton point and its closure adds exactly that point.

Use: geometric model after algebraic closure only.  It is not cited as an
arbitrary-field theorem.

## Ducros

Source: *La structure des courbes analytiques*, arXiv:2405.10619.

Local bytes:

- PDF: `/private/tmp/ducros2405.10619.pdf`
- extraction: `/private/tmp/ducros2405.10619.txt`
- PDF SHA-256: `b514eaa16c0a531880672956d08ee75a4026d75f61303446044468937c9342ad`
- extraction SHA-256: `7707c5384c328933e1aec337135fee4867527b58b0097ca16dcecb7685e07e19`

Locators:

- 3.6.32--3.6.34, printed pp. 210--211; extraction lines 10789--10900:
  virtual discs, their scalar extensions, topology, and examples;
- 3.6.35.5--3.6.35.6, printed pp. 212--213; extraction lines 10900--10955:
  scalar-extension compatibility of virtual annulus skeleta and retractions;
- 3.6.35.8, printed p. 213; extraction lines 10955--10970: components off the
  analytic skeleton are virtual discs; after deleting a skeleton point, only
  the at most two skeletal components are virtual annuli and all other
  components are virtual discs;
- 3.6.35.9--3.6.35.10, printed p. 213; extraction lines 10970--10985:
  subannuli attached to skeleton intervals and their scalar-extension
  compatibility.

Use: arbitrary-field branch topology.  The fact that a virtual disc may be
nontrivial is essential; see Ducros 3.6.33.3.

## Berkovich interiors

Source: *Etale cohomology for non-Archimedean analytic spaces*.

Local bytes:

- PDF: `/private/tmp/Berkovich1993_Etale.pdf`
- extraction: `/private/tmp/Berkovich1993_Etale.txt`
- PDF SHA-256: `bd864c89ed8b6e8f27a90f459837221549db75afa75554ab51414e17771066af`
- extraction SHA-256: `3060819de1bcf80f4843b07e9e06be5a7004d47ea363124684e1342da03fc037`

Locator: Proposition 1.5.5(i)--(ii), printed pp. 34--35; extraction lines
1309--1322.  Part (i) identifies relative analytic interior of an analytic
domain with topological interior; part (ii) is the composition formula used
with the boundaryless ambient torus.

## Rigid-point density

Canonical source: Berkovich, *Spectral theory and analytic geometry over
non-Archimedean fields*, Proposition 2.1.15: rigid points are dense in a
strict affinoid space.  Original book bytes are not present in the local
cache.  Gubler--Rabinoff Appendix A.1, printed p. 37, extraction lines
1797--1801 of `/private/tmp/GR25.txt`, explicitly invokes this proposition
for the same density statement.  The endpoint proof applies it on local
strict affinoid neighbourhoods of a standard strict annulus.
The extraction SHA-256 is
`091c0fbf66c18ee4925b929f2b5f2aea32a96fee707744aacf9b87099a94acec`.

## CLD trace and current operations

Source: Chambert--Loir--Ducros, 2025 version.

Local bytes:

- PDF: `/private/tmp/CLD25.pdf`
- extraction: `/private/tmp/CLD25.txt`
- PDF SHA-256: `5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719`
- extraction SHA-256: `021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e`

Locators used through the already verified finite-flat trace dependency:

- Theorem 15.2.6, printed p. 424: smooth uniform approximation;
- Theorem 16.3.3(d), printed p. 447: regularity of fibre integration;
- Corollary 16.5.5, printed p. 455: projection formula;
- Section 7.7.8, printed p. 189: compact direct image commutes with
  `d'` and `d''`.

The endpoint dossier imports the verified trace theorem rather than
re-proving these source results.
