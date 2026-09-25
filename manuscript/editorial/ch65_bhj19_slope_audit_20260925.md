# Chapter 65: BHJ19 functional-slope audit — 25 September 2026

## Scope and baseline

Baseline: `ac6e03e2a13fd0533673379bf843d129e6a421d9`. The live `main`
checkout was clean and matched the designated GitHub origin. This bounded
unit audits Theorem `thm:rf-bhj-unaffected-slopes`, its proof, and the exact
boundary imposed by the BHJ19 erratum. It does not alter the Chapter 72
inventory, promote a new research theorem, or claim a new model-verifier or
independent-agent verdict.

## Mathematical repairs

The theorem now states the exact scope of BHJ19 Theorem 4.2. For a normal
projective variety with a big and nef rational line bundle, the `E`, `I`,
and `J` limits require only the smooth test-configuration metric. A boundary
and a smooth reference metric on its log canonical bundle give `R_B`. The
`H_B` and `M_B` conclusions additionally require a subklt pair and a
semipositive total-space metric.

The Deligne-pairing formula now includes the fixed reference pairing and
its `O(1)` remainder. The base parameter is denoted by `tau`, leaving the
chapter's squared-norm parameter `t` unambiguous. `F_wt` is defined locally
as the source's ordinary norm-weight normalization.

The entropy proof now distinguishes two metrics that had been conflated:

- `kappa_0 = (1/2) log MA(psi_ref,L)` is the fixed reference metric on
  `K_X` in the Chen--Tian/Deligne identity;
- `kappa_s` is the ray induced by an independently chosen smooth metric on
  the logarithmic relative canonical bundle.

With these names, the replacement error is exactly the integral of
`log(MA(psi_s)/exp(2 kappa_s))`. The lower estimate is written as relative
entropy against the normalized logarithmic canonical volume form, while
the upper estimate uses the local monomial bound in BHJ19 equation (3.4).
Lemma 3.11 supplies the dual-complex growth `A_s` comparable to `s^d`, so
the error is `O(log s)=o(s)`. No strict positivity is asserted after
resolution; smooth semipositivity is sufficient.

The Mabuchi step now uses the exact norm-weight identities

    M = H + R + Sbar E,
    M^NA = H^NA + R^NA + Sbar E^NA.

The logarithmic proof is reconstructed from BHJ19 Section 4.5: after a log
resolution, `H_B+R_B` is the ordinary `H+R` term plus the finite sum of
restricted energies on the smooth boundary components, with the identical
finite sum on the non-Archimedean side. This makes both the subklt boundary
and the semipositivity assumption visible rather than hiding them in a
generic reference to a logarithmic analogue.

## Primary sources and erratum boundary

- [BHJ19, corrected arXiv v5](https://arxiv.org/pdf/1603.01026), physical
  pages 17--20: Theorem 3.6, Lemmas 3.9--3.11 and their proofs; physical
  pages 23--25: Theorem 4.2 and its proof. The downloaded 35-page PDF has
  603,751 bytes and SHA-256
  `ed9178290423a5e702badf04acb7882bf58d779573aeb47cbb240e266a264bba`.
  All seven cited pages were rendered and visually inspected.
- [Published JEMS article](https://ems.press/journals/jems/articles/16240?na),
  DOI `10.4171/JEMS/894`, pp. 2905--2944. The existing `BHJ19`
  bibliography entry retains the published metadata.
- [Official JEMS erratum](https://ems.press/content/serial-article-files/32634),
  DOI `10.4171/JEMS/1215`. Both pages were visually inspected. The PDF has
  111,027 bytes and SHA-256
  `1a00dcb6540685f3a86c4bb71338308e43e715075015c23c6b0fe2cf91537033`.
  It identifies the flaw in Theorem 5.6, propagating to Theorem 5.4,
  Theorem C and Corollaries D--E, while expressly preserving Theorem A,
  Corollary B and every result through Section 4. The audited proof uses
  only Sections 1--4.

## Two review passes

The first pass aligned every displayed identity and hypothesis with the
corrected source, separated the two canonical metrics, restored the omitted
reference pairing, and reconstructed the logarithmic boundary reduction.
The second pass reread the entire theorem and proof against the source
pages, corrected the normalized relative-entropy constant, made the
`Sbar` coefficient exact, and checked that the factor-two firewall remains
unchanged: this result stays entirely in the source's norm-weight
convention.

## Validation and preservation

The scoped house-style audit has no errors or warnings in the revised
theorem/proof block. Whole-file reports outside that block are inherited
legacy style findings and are not silently rewritten in this unit.

Both source/proof passes complete full-book builds. The final PDF has
**4,066 pages** and **19,363,469 bytes**. The reference check finds **397
inputs and 11,828 unique labels**, with no missing input, duplicate label,
dangling reference or per-file structure error. The inventory remains **42
active atoms in 12 formal problem environments**, with tiers
**(0,3,7,15,17)**.

The final log has no unresolved reference or citation, rerun request, or
horizontal or vertical overflow. Its 13 inherited Chapter 70 duplicate PDF
destination warnings are unchanged. Physical pages 3533--3538 were rendered
after the first build and visually inspected; they cover the complete revised
theorem and proof together with both transitions. The final second build has
the same pagination and received a targeted text and log check.

Before the progress records were updated, every tracked baseline file except
Chapter 65 retained its exact bytes. The Chapter 72 research inventory,
supplied integrations and originals, frozen packets, verifier receipts,
bibliography and dated releases are unchanged. Only Chapter 65 and the four
current progress/audit files are delivered; the ignored current `book.pdf`
is replaced. Temporary source downloads, extracted text and renderings remain
outside the repository.

- `manuscript/book.pdf` SHA-256:
  `4dca3c51d739e6c4c482ae776d68afe2283cd1cd74dce271ec53ffbcd744a624`.
- `manuscript/parts/part6/ch65_rays_filtrations.tex` SHA-256:
  `1ac7866685727bd6eea321ffe6cc1425d538215c89bc5570c872d0d8a33872c6`.
