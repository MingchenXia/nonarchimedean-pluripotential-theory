# Chapter 18 fibre-cylinder citation repair: source matrix

The audited chapter is
`/private/tmp/nappt_p071_20260827/manuscript/parts/part2/ch18_delta_forms.tex`
(SHA-256 `b1a8b00d223f71ce00991a4b85f6b20a077f2ef3e140aa82280339649060ab45`).
The local CLD primary text is `/private/tmp/CLD25.txt` (SHA-256
`021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e`).

| Claim or defect | Exact primary location | What it supplies |
|---|---|---|
| The present citation is wrong | `CLD25.txt:5570--5577`, Proposition 4.6.6, *Compensation des bords* | This proposition is an inclusion--exclusion identity for boundary volume forms, not a fibre theorem. |
| Correct fibre-calibration theorem | `CLD25.txt:21310--21324`, Theorem 14.7.2; source `/private/tmp/cld1204.6277v2-src/calibrage.tex:4349--4374`, label `theo.tropcont` | For compact pure (X) satisfying ((S_d)), regular pure (d)-fold (Y), and (f) pure of relative dimension (n-d): (a) calibrated fibre tropicalizations are constant near a rigid base point; (b) over (mathbf A^d) the punctured tropical tail is the calibrated product with the standard (d)-cell.  Put (d=1). |
| Cartier tube supplies the (d=1) hypotheses | `CLD25.txt:23425--23447`, Lemma 16.7.5; source `/private/tmp/cld1204.6277v2-src/courants-berk.tex:2106--2148` | At a zero of a regular analytic function, its germ is a regular local-ring element, giving ((S_1)); upper semicontinuity and the analytic Hauptidealsatz give pure relative dimension (n-1) on a neighbourhood. Compactness of the zero fibre then permits a closed small tube inside that neighbourhood. |
| Zero fibre is the divisor cycle | `CLD25.txt:19682--19689`, Section 13.7.1 | For a regular analytic function, the associated cycle of the closed analytic subspace (f=0) is (operatorname{div}(f)), with generic-length multiplicities. |
| Closed-subspace integration carries associated-cycle multiplicities | `CLD25.txt:23363--23389`, Proposition 16.6.3; source `/private/tmp/cld1204.6277v2-src/courants-berk.tex`, label `prop.cycle-courant` | (delta_Y=delta_{[Y]}) for a pure closed analytic subspace. On a fixed tropicalization this detects the canonical top-cell weights. |
| Historical provenance of the misnumbering | Walter Gubler--Klaus Künnemann, *A tropical approach to non-Archimedean Arakelov geometry*, official author PDF, Theorem 7.2 proof, p.54, paragraphs (a),(b): <https://gubler.app.uni-regensburg.de/Publikationen/1406.7637.pdf> | The paper states the three fibre-cylinder conclusions essentially verbatim and cites **the older** `[CLD12, Proposition 4.6.6]`. The material was renumbered to Theorem 14.7.2 in CLD25. |
| Exact boundary--divisor equation | Same GK17 PDF, Lemma 7.3, equation (7.3.1), pp.56--58 | The displayed boundary integral is exactly the divisor pairing used in Chapter 18. Equations (7.3.8)--(7.3.9) explain the annular product and the treatment of possible relative-boundary cells. |
| Scope includes generalized delta forms | Same GK17 PDF, Remark 7.4, p.58 | The Lemma 7.3 calculation applies to compactly supported generalized delta forms, the test objects needed here. |
| Analytic boundary inclusion--exclusion | `CLD25.txt:23520--23540`, Proposition 5.9.5 as invoked in the proof of Theorem 16.7.3 | Confirms the finite-cover boundary compensation step in the smooth CLD prototype. |

Source hashes:

- `/private/tmp/cld1204.6277v2-src/calibrage.tex`:
  `4ada533dda4fd9b08daa87d73c2b317b183b58822e130e2b575f4f8e25807f23`
- `/private/tmp/cld1204.6277v2-src/courants-berk.tex`:
  `79abf5b7211b76e83ae4bcee1186035a0aefd51af335de7e24b51e4966198015`

## Source-to-text crosswalk

1. Replacement item (1) is Theorem 14.7.2(a) with (d=1).
2. Replacement item (2) is Theorem 14.7.2(b), restricted to a closed
   interval strictly inside the open tail, with the factors permuted and
   (log|f|) negated.
3. Replacement item (3) combines Section 13.7.1 with Proposition 16.6.3.
4. The replacement boundary paragraph follows GK17 Lemma 7.3,
   especially (7.3.8)--(7.3.9), rather than promoting an equality of
   top-dimensional skeleta to an unqualified equality of whole images.
