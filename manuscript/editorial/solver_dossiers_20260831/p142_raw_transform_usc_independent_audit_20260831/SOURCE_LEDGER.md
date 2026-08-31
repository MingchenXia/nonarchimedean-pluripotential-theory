# P14.2 independent source ledger

Reviewer: `/root/p082_independent_reaudit`. Date: 2026-08-31.

This ledger supports an adversarial review of the proposed upper-semicontinuity argument for the raw ideal-valuative transform. Source statements are distinguished from the new elementary deduction. No MP positivity, envelope theorem, approximation by semipositive functions, or production acceptance is inferred.

## 1. Exact live definitions read

All manuscript paths below have root `/private/tmp/nappt_p071_20260827`.

| File and locators | SHA-256 | Verified interface |
| --- | --- | --- |
| `manuscript/parts/part6/ch71_pseudoeffective_mp_dxz.tex`, standing hypotheses; equations 71.6--71.8, 71.12, 71.27, 71.29--71.30; `prop:pseff-ideal-valuative-basic`; `thm:pseff-perturbation-independent-transform` | `c6bc0fb2d6813ed2ca4c6c37df4a7b75ef733a0cae62d97400df78fe087327e2` | Connected compact Kähler manifold; arbitrary real pseudoeffective class; ideal values in [0,+infinity]; Fekete supremum; raw transform over tau<c; exact compatibility of multiplier ideals under changes of perturbation. |
| `manuscript/parts/part5/ch58_tropical_spectra.tex`, `def:ts-tropical-spectrum`, `def:ts-complex-beth`, equation 58.9 | `f40c52c119b443973a56dfd5bf5445511cc484fb3587f0ca5418b0ecbbb7d0a1` | The topology is pointwise convergence on coherent ideal evaluations with the extended order topology. |
| `manuscript/parts/part5/ch52_rays_test_curves.tex`, `def:rays-test-curve`, endpoint convention 52.7 | `86d5436c8047ac8c82da33ef88969417b1d50f9edf272298f569b8baad110b65` | Finite real terminal parameter; levels decrease with tau; interior levels are genuine quasi-psh potentials. |
| `manuscript/parts/part5/ch53_transcendental_metrics.tex`, `def:tna-pshna`, `prop:tna-common-terminal`, equations 53.3, 53.7, 53.9 | `b6223235a5f129014b9116a61f42cf15821c7fffe87f034a04d80ce9ad48c416` | Compatible positive-mass components in perturbed big classes; transitions are levelwise I-envelopes; common endpoint. |

The existing Chapter 71 disclaimers explicitly leave arbitrary-semivaluation upper semicontinuity unproved. They do not constitute a contrary theorem. The new proposed argument is assessed against the actual definitions, without importing MP positivity or projectivity into its hypotheses.

## 2. Mesquita-Piccione: the exact topology

Primary: Pietro Mesquita-Piccione, *A non-Archimedean theory of complex spaces and the cscK problem*, [arXiv:2409.06221](https://arxiv.org/abs/2409.06221). The inspected local PDF bears version 2, 18 September 2025, 60 pages.

- PDF: `/Users/mingchen/Projects/Yethlas/tmp/MP24.pdf`.
- PDF SHA-256: `9eb2ea7686a5962ebc11c5eacd23b0cb3dcb081e27ac48292933f291fc82cb23`.
- Independent layout extraction: `/private/tmp/MP24_p142_audit_20260831.txt`.
- Text SHA-256: `0445ccf2c4474b6576a8053d0c7c038ffbd72c2ab27bb3d5704b90dd0e5beb62`.

Definition 1.2.1, pages 7--8, defines the tropical spectrum using pointwise convergence. Definition 1.3.1, page 9, specifies X^beth as characters of the ideal semiring taking values in [0,+infinity], with that topology. Section 2 identifies locally finite-type ideals with coherent ideals for complex spaces. Definition 1.4.1 identifies log|I| with -v(I). These clauses, not a claim about all general tropical semirings, give the needed continuous extended-valued ideal coordinates.

Page 9 was rendered and visually inspected in full, including the positivity footnote. No compactness theorem is needed for the proposed finite-mesh or sequential-continuous-approximation argument.

## 3. Darvas--Xia--Zhang: test curves and inverse systems

Primary: Tamás Darvas, Mingchen Xia, Kewei Zhang, *A transcendental approach to non-Archimedean metrics of pseudoeffective classes*, [arXiv:2302.02541](https://arxiv.org/abs/2302.02541). The inspected PDF bears version 3, 17 July 2024, 40 pages.

- PDF: `/Users/mingchen/Projects/Yethlas/tmp/pdfs/dxz23.pdf`.
- PDF SHA-256: `7fede7c413e396008217a4a4c9638776dbdd7cacff90fdd463bf5ae48220246c`.
- Existing layout text: `/Users/mingchen/Projects/Yethlas/tmp/pdfs/dxz23.txt`.
- Text SHA-256: `7d5a061d240096139e6302c2b4da2e9c125a8839730fc90909c1488baa446244`.
- The alternate local `/Users/mingchen/Projects/Yethlas/tmp/DXZ23.pdf` is byte-identical.

| Locator | Source content used | Scope limitation |
| --- | --- | --- |
| Section 2.1, page 8 | I-model normalization and multiplier-ideal envelope conventions. | Only the coherent ideals and normalized representative interface are needed. |
| Section 2.2, page 9, equation (10) | Relative test curves are tau-decreasing and eventually identically minus infinity; the endpoint is finite. | Concavity and positive mass ensure the source objects exist, but are not additional ingredients of the elementary mesh estimate. |
| Section 2.2, page 11, equation (18) | Positive-mass I-maximal component space. | Positive mass concerns each perturbed component, not the unperturbed pseudoeffective class. |
| Section 3.1, page 15, equations (23)--(24) | Multiplier-ideal subadditivity gives a superadditive sequence of ideal evaluations and a Fekete limit; the raw test-curve formula uses a supremum over levels. | This subsection has a projective standing hypothesis. Its elementary ideal calculation is separately justified analytically below; its projective positivity consequences are not imported. |
| Section 3.2, pages 16--17, equation (28), Definition 3.3, following endpoint paragraph | Compact Kähler inverse-system definition, levelwise I-envelope transitions, and common finite endpoint. | These are the full transcendental input definitions; no ample line bundle, algebraization, or positive volume of the unperturbed class is assumed. |

Pages 9 and 15--17 were rendered and visually inspected in full. Lemma 2.4 concerns a related complex Legendre-transform upper-semicontinuity statement, but it is not used as a substitute for the proposed proof on X^beth.

## 4. Darvas--Xia: preservation of all multiplier ideals

Primary published paper: Tamás Darvas and Mingchen Xia, *The closures of test configurations and algebraic singularity types*, Advances in Mathematics 397 (2022), 108198, [DOI](https://doi.org/10.1016/j.aim.2022.108198). Direct primary text was read in the [university-hosted published PDF](https://research.chalmers.se/publication/528300/file/528300_Fulltext.pdf).

The inspected university wrapper identifies the version of record; the PDF has 57 pages including its cover. The relevant printed pages are 19--22. Crucially, Section 2.4 explicitly resets the hypotheses to a compact Kähler manifold and a smooth real form representing a pseudoeffective class. Thus the ample-line-bundle introduction does not restrict this subsection. Definition 2.12 defines I-equivalence by equality of all positive-real multiplier ideals. Proposition 2.18(ii) proves that the I-envelope preserves this equivalence, using increasing approximation and strong openness. It supplies the exact ideal-equality input for changing a DXZ perturbation, not merely equality at divisorial valuations. Only this subsection and interface are used.

This source was read through the primary web PDF text. No local PDF copy or independent local-PDF hash is claimed.

## 5. Demailly--Ein--Lazarsfeld: analytic subadditivity

Primary published paper: Jean-Pierre Demailly, Lawrence Ein, Robert Lazarsfeld, *A Subadditivity Property of Multiplier Ideals*, Michigan Mathematical Journal 48 (2000), 137--156, [author-hosted published PDF](https://www.math.stonybrook.edu/~roblaz/Reprints/Demailly.Ein.Laz.Subadditivity.pdf), [arXiv:math/0002035](https://arxiv.org/abs/math/0002035).

The analytic discussion on printed page 139 records coherence. Theorem 2.6(ii), printed page 149, states analytic subadditivity for plurisubharmonic functions on a complex manifold. It applies to quasi-psh functions locally after adding smooth local potentials; multiplier ideals are unchanged by locally bounded smooth additions. This gives I((m+l)phi) contained in I(m phi)I(l phi). No algebraic, projective, or line-bundle hypothesis is needed for this analytic step.

Normalization check: DEL writes its analytic multiplier ideal using the weight exp(-2 phi), whereas the manuscript and the candidate example use exp(-phi). Applying the source statement to half the manuscript potential gives exactly the inclusion above. This convention does not change the superadditive ideal-evaluation argument.

The primary PDF text and theorem statement were inspected through the web tool. A shell download failed at DNS resolution; it was not retried or escalated. No local-PDF hash or successful visual inspection of this source is claimed.

## 6. Xia Operations: exact comparison boundary

Primary: Mingchen Xia, *Operations on transcendental non-Archimedean metrics*, [arXiv:2312.17150](https://arxiv.org/abs/2312.17150). The local PDF bears version 3, 22 October 2024.

- PDF: `/Users/mingchen/Projects/Yethlas/tmp/pdfs/xia23operations.pdf`.
- PDF SHA-256: `773eea71af9f1fff112bf5fcab2b9046b81467df2e37165ee1da3949ff74c6d9`.
- Text: `/Users/mingchen/Projects/Yethlas/tmp/pdfs/xia23operations.txt`.
- Text SHA-256: `c75572e06a2df8cb9dbd76726678a52db5e79587ec568df41f4886e3e4ee8005`.

Definitions 2.3 and 2.7, page 5, record I-model normalization and I-equivalence. Definition 3.11 and formula (3.8), page 12, record the raw-transform comparison. Page 12 was visually inspected: its Section 3.3 standing hypotheses are projective and line-bundle based, with smoothness imposed for (3.8). Theorem 3.12 is therefore not used to claim MP positivity for a genuinely transcendental/nonprojective class. The proposed upper-semicontinuity result is instead an elementary deduction from the full-scope ideal topology and monotone-level data.

## 7. Independence and scope summary

The root supplied the finite-grid idea and the explicit continuous sequence; this reviewer tests them adversarially and is not their independent originator. Earlier reviewer work on curve model metrics, Chapter 20 real-model density, and analytic fiber envelopes is unrelated and not imported as proof input. No parent acceptance report or production verdict is used.

The topological claim needs no divisorial density, finite-energy assumption, projectivity, rational cohomology class, nonpluripolar positive mass in the unperturbed class, scalar extension, or general envelope theorem. It does require the actual ideal-evaluation topology, finite endpoint, nonnegative ideal values, and the order of test-curve levels. It does not establish MP positivity, continuous-obstacle envelope continuity, P-sensitive theory, or singular-space multiplier-ideal analogues.

The candidate bibliography points to the published DXZ and MP papers; the independently inspected local versions are the arXiv versions identified above. Their exact inspected locators, rather than an unverified assertion about identical published pagination, are the source basis of this review. DX22 and DEL00 were checked in the published primary texts through the web reader.
