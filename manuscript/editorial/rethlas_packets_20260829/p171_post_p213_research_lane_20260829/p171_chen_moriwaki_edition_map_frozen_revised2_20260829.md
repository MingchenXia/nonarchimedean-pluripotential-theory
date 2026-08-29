# Frozen Chen--Moriwaki edition map for the P17.1 research lane: revised2

Date: 29 August 2026

Status: **source map only; not a theorem packet and not a live-book input**.

This file fixes the edition ambiguity in every Chen--Moriwaki anchor used in
the P17.1 research lane.  An unqualified citation to a numbered item below is
not permitted: the edition identifier or the exact frozen-file hash must
accompany it.

## Frozen editions

### CM-v1

- Huayi Chen and Atsushi Moriwaki, *Arithmetic intersection theory over
  adelic curves*, arXiv:2103.15646v1, 29 March 2021;
- internal title-page date: 27 March 2021, Version 1;
- local audit file: `/private/tmp/ChenMoriwaki2103.15646.pdf`;
- SHA-256:
  `89828d2fe257736d0a51d8152d47b29ba0da207b61f6e04137fd9f28f89d5b1f`.

### CM-later

- later author-hosted revision of the same title;
- frozen URL:
  `https://webusers.imj-prg.fr/~huayi.chen/Recherche/Intersection_Adelic_Curves.pdf`;
- local audit file: `/private/tmp/ChenMoriwakiIntersectionAccepted.pdf`;
- 153 pages; the frozen PDF itself supplies no version number on its title
  page, so it is identified here only by URL and hash;
- SHA-256:
  `4978bf5a6b0b09dbb43a273fe0eba1e2368ce60b9f78730e567f59d605be0b44`.

## Exact anchor concordance

| mathematical item | CM-v1 | CM-later |
|---|---:|---:|
| resultant for the top-dimensional fundamental cycle of an arbitrary projective scheme, with generic lengths as exponents | Definition 1.6.3 | Definition 1.6.4 |
| dimension-zero norm/resultant orientation | Example 1.6.4 | Example 1.6.5 |
| scalar normalization by a properly intersecting tuple | Definition 1.6.7 | Definition 1.6.9 |
| field-base-change compatibility | Remark 1.6.8 | Remark 1.6.10 |
| local-height/resultant formula over a nontrivially valued complete field, for closed immersions and the stated quotient metrics | Theorem 3.8.7 | Theorem 3.9.7 |
| corresponding formula over a trivially valued field by scalar extension | Proposition 3.9.3 | Proposition 3.10.3 |

The numbering shift in Section 1.6 is caused in particular by the insertion of
Proposition 1.6.3 in CM-later.  The shift in Chapter 3 comes from the inserted
reminder-on-norms section.

## Mandatory firewall around “3.9.7”

In CM-v1, Proposition 3.9.7 is **not** the broad resultant formula.  It is a
special comparison for a regular projective curve, under the additional
alternative that either `X=P^1` and `L=O(1)`, or the generating normed vector
space has dimension two.  The broad formula numbered Theorem 3.9.7 occurs only
in CM-later.  Therefore a citation merely to “Chen--Moriwaki 3.9.7” is
inadmissibly ambiguous.

## Scope that the anchors do and do not supply

Both editions' resultant sections start from closed immersions into projective
spaces.  Their resultant for a nonintegral projective scheme is the product of
the component resultants with the generic lengths in the top-dimensional
fundamental cycle as exponents.  The nontrivial-valuation theorem treats the
Archimedean and non-Archimedean quotient norms in its stated form; the trivial
valuation proposition is obtained through scalar extension.

These sources do **not** construct a relative mixed Chow/resultant section over
an arbitrary Banach ring, do not prove that such a section commutes with every
Banach-base fibre in the form required by P17.1, and do not prove continuity of
the resulting fieldwise weights on a Berkovich spectrum.  At Archimedean
places, their standard orthogonal quotient metric is also not literally the
tropical maximum metric; the tensor-power/log-sum-exp comparison is a separate
step.

The quarantined closed-immersion finite-level reduction does not use a
Chen--Moriwaki theorem.  Its all-field multilinearity input is
Boucksom--Eriksson, Proposition 8.5, Definition 8.7, and the paragraph
following Definition 8.7; its fieldwise Deligne input is
Boucksom--Eriksson, Theorem 8.16 and formula (8.9).  Pille--Schneider,
Proposition 4.2, gives the corresponding DFS multilinearity statement only in
the non-Archimedean portion of that paper and is not used as the all-field
anchor in revised2.  Chen--Moriwaki enters only in a future downstream
closed-immersion resultant/metric comparison, after a relative algebraic
section has been constructed and its fibre identified.
