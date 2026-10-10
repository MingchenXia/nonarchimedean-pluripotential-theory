# Chapter 71 completion audit

Date: 2 October 2026.

Base: local Chapter 70 commit 9d6f40c.

Scope: parts/part6/ch71_pseudoeffective_mp_dxz.tex, under the sequential
quality programme. The whole-book goal continues; independent Chapter 72
research remains paused. This is a direct mathematical, source and editorial
review. It creates no independent verifier verdict or priority claim.
Historical releases, receipts and checksum ledgers are unchanged.

## Architecture, proof and exposition

The entire chapter was read. It has 23 formal assertions and 23 proofs:
eight theorems, ten propositions, one lemma and four corollaries. Its 37
reusable environments include eight examples, five remarks and one warning.
There are 136 semantic labels. The receipt-linked constant-ray example
keeps its existing equation locator, eq:pseff-constant-transform, without
inserting a new label into the protected example.

- The introduction, comparison ladder and closing ledger now state the
  proved full compact-Kähler DXZ--MP order isomorphism. It requires neither
  projectivity, rationality nor finite energy. The finite-energy comparison
  remains its normalized-energy subcase. General pseudoeffective image
  characterization, non-nef positivity and zero-volume measure/energy
  theories retain their explicit open boundaries.
- The finite ideal approximation requires a nonempty finite parameter set.
  The monotone-parameter lemma proves the iterated limit on every
  semivaluation, including proper-support points with value minus infinity.
  The multiplier limit is taken first, then the increasing parameter grid.
  The proof makes no positivity claim for the finite approximants.
- The energy distinction is substantive. Source DXZ energy subtracts and
  divides by the full class volume V. Finite source energy forces initial
  mass V. The book's normalized relative radial functional instead uses
  m = M(Gamma at minus infinity), the initial mass. It is the barycentre
  of the probability DH measure and equals the raw relative first moment
  divided by m. For m < V, source DXZ energy is minus infinity even when
  relative energy is finite. The earlier attribution of the relative
  formula to source formula (43), and the wording calling m terminal
  mass, are corrected. No non-nef MP energy is constructed by this formula.
- The fixed logarithmic pole on P1 computes its multiplier ideals, the
  transform -r lambda, the dominated sequence N ord_p tending to the
  proper-support point, and relative energy zero versus source energy
  minus infinity. The new finite-grid example gives -3/4 at M=4,
  -17/20 after the multiplier limit at fixed grid, and -3/5 after the
  grid limit. The nef-boundary, non-nef surface and zero-volume examples
  retain their exact class and mass hypotheses.
- Twelve section/subsection labels and four example locators improve
  navigation. All unprotected legacy inline delimiters are converted to
  the house convention. The remaining 466 pairs are entirely inside
  protected chunks. Source-version notes distinguish the older locators
  from published equation numbering.

The DH import is the general extended first-moment statement in Chapter 55,
with its modification convention when a flag is needed; Chapter 64's
bounded-curve moment theorem is used only in its bounded scope. The source
finite-energy theorem is read with the class-volume definition immediately
preceding it. Nets, zero ideals, zero times infinity, trivial valuations,
endpoint extensions and normalization conventions were reviewed explicitly.

## Receipt-linked preservation

Twenty-eight disjoint live chunks, totalling 60,397 bytes, remain identical
to the entry baseline. They cover thirteen statement/proof pairs, the
constant-ray example, and the entire raw-filtration section. The comparison
and filtration proofs were reviewed with their precise source interfaces;
no new independent-verification receipt is asserted.

The P14.2 V15 local quasi-psh reduction repairs the historical V14
subadditivity gap. Its accepted item is pi_4e14dc8a6a26aa190cd191b5.
The subsequent unconditional P14.3 item is pi_90c4637f53444d88823e88f3;
the earlier conditional integration record is not treated as the current
scope. The raw-filtration production is
20260901T115233Z_d6fca0374675_41a5ca54. Its terminal left-limit corollary
does not settle arbitrary zero-mass reconstruction P14.8. Archived premise
and source hashes remain historical records; this byte check compares the
live Chapter 71 chunks with this unit's entry baseline, not every changed
ancestor with an older packet.

Protected live chunk SHA-256 values:

| Chunk | SHA-256 |
| --- | --- |
| prop:pseff-one-curve-transform-statement | `ddcf86a946bcfdc0ef760cd1feab9518e152aee9267296b2cea8a7431d9c5115` |
| prop:pseff-one-curve-transform-proof | `a701141c0deb9ee60920e1cd5285f726e1f51e080da1f618376fd2d408a93388` |
| constant-ray-example | `1cfb4a53ddcab3058877dcdf6d8628896e82ea11799c90baf76e9a9393192d2a` |
| thm:pseff-perturbation-independent-transform-statement | `26caf9b3052fe45fdd083197a9a3d639b9b0f1f18f7dd20632ea684e5daaf0ce` |
| thm:pseff-perturbation-independent-transform-proof | `152508e6156429ce528ecf041ef2cf2660009bc72716bed93f5f961cd6135ff8` |
| thm:pseff-divisorial-inversion-statement | `a6949ebb9408afa4ee84713b17ec7ab3bd8f92a59652375eea0f594391dd5eef` |
| thm:pseff-divisorial-inversion-proof | `a570980d4bc8ea93679e26684c01d4768117e4c3b35c023f3f00af66a43a1454` |
| lem:p142-monotone-parameter-supremum-statement | `30547158d4fd45a7a0cd11b3319e30793a2e304058e953149357da07636abe1c` |
| thm:p142-raw-transform-usc-statement | `00160c87471b738aef65baf81759502043014274fd839759c03bd0e37887c1e3` |
| lem:p142-monotone-parameter-supremum-proof | `e8e25966ed2cfccd85f9d923a0cf78910e0947aea06623a08f5357458bdf7a55` |
| thm:p142-raw-transform-usc-proof | `a2e7d4cb93120b24752bffc9b2c2e781aab37b607fe009ce9fbc41644295b892` |
| cor:p142-pseudoeffective-raw-usc-statement | `e44487ed628f4b4dfd23873fabf33c08a7fb3f53f25703e9da9cdf0729397749` |
| cor:p142-pseudoeffective-raw-usc-proof | `3c2d39d5e3b2f48c67aecdb299d4438fb1345f72ff4dae3b6bb676c2f7bf65fd` |
| thm:pseff-kahler-finite-energy-link-statement | `c665364133b77839f3aa7a0266caeac4855dd0b64a8fce6b23d4a3d042e16697` |
| thm:pseff-kahler-finite-energy-link-proof | `a2097fa104c2e4d72520e85589135873a9a6dcb3883e7591af87ab118acd594a` |
| thm:p143-dominated-divisorial-density-statement | `530488cf1426e464f6203babcc8f87194db79fd8d99323ae6697da69047db28d` |
| thm:p143-dominated-divisorial-density-proof | `377e85904fb80e259d81ba3b5e76550daff7369000576e62127c1ab0f4bb98f7` |
| cor:p143-all-point-kahler-comparison-statement | `66daacec917c467903753ca9bc3000a1f6d9703b971916c215ae77f8724825df` |
| cor:p143-all-point-kahler-comparison-proof | `41bbc431f1e67801cce2ba794f3d98cb843d72a4217a63b731fa0b55c2578a97` |
| cor:p141-finite-energy-raw-image-statement | `cc1705d3a9491a423de522993a4c2f5cb2d60cb5d60f1297ef979fa1ffed8990` |
| cor:p141-finite-energy-raw-image-proof | `9c7f4860afbbb7ecca6c37f45546401decc9bf37f375cc00e9b550a70b24a5c7` |
| thm:p143-mp-section-statement | `341f8dcec9b17da6d988733c5ffda438e422cdc90cb8848d1273604765a2bb77` |
| thm:p143-mp-section-proof | `a800b4975c91d74da5d55bc7bcfdbc39b7d164628da6421e7a6cbeaf1182e109` |
| thm:p143-full-kahler-comparison-statement | `5bceac7aef5bd96a2de45b626d38b0fc6d414041cc3845aa297d03a31006e845` |
| thm:p143-full-kahler-comparison-proof | `099f110a3c0e429f8efa3d4b7580ab4ba1aa67eb2bf8aa82524337972e1a6ac8` |
| prop:pseff-operation-formulas-statement | `67a06bea85d42f9a7149b4439323e6c27b77afdf36bf2d4160b01c747fef0393` |
| prop:pseff-operation-formulas-proof | `1b817c786e7f25ace1a832a7f589cb85cff4eb756f834b4e66ff240f8656cd76` |
| filtration-section | `6ad9f41af78dbc454d8c2e7fbbaf9eb35ea449c6081f5dc47d90f7b891ff78a0` |

Main entry SHA-256:
`05ce1967cb4d083613bcb72dae1c23ebbc60156840f9fa3555caba32d85ad634`.

## Primary-source interfaces

Eleven PDFs and 87 selected physical pages were read and visually inspected
in 27 rendered images/contact sheets. Cached PDFs were checked directly for
this unit; published-byte identity is not inferred for older arXiv copies.
These are precise interface checks, not independent reproving of every
imported general theorem.

| Source/version | Principal interfaces | Physical pages |
| --- | --- | --- |
| Mesquita-Piccione, arXiv 2409.06221 v2, 18 September 2025 | Ideal spectrum, rational divisorial/monomial construction, model/PL correspondence, relative nefness, decreasing-net definition, comparison 4.3.8, ray extension 5.1.4, maximal-ray theorem 5.1.7 and finite-energy comparison 5.2 | 1, 11--12, 15--17, 19--20, 26--27, 33--34, 39--42, 44--49 |
| Darvas--Xia--Zhang, arXiv 2302.02541 v3, 17 July 2024 | Projective radial convention, transitions, ideal/graded-series interfaces, full projective comparison 3.14--3.15, class energy (43), finite-energy 3.17, filtration 4.1/4.3, ordinary-envelope lemma 4.5 and ample-series proposition 4.6 | 1, 15--28 |
| Xia operations, arXiv 2312.17150 v3, 22 October 2024 | P/I equivalence, decreasing nets, recovery of positive-mass objects, divisorial order/operation formulas and endpoint conditions | 1, 4--6, 9--18 |
| Boucksom--Jonsson, AFST 31 (2022) published PDF | Generic finiteness 1.4(ii), relative nef central-fibre criterion 3.1, model cones 3.2/3.6, ample approximation 3.10/4.15(iii), decreasing closure 4.5--4.6 and comparison 4.22 | 1, 14, 18, 46--51, 62--65, 68--70 |
| Berman, arXiv 0710.4375 v2, 25 December 2007; published AJM 131 (2009) | Smooth-obstacle big-line-bundle Bergman theorem 1.4, proof 4.11, fixed auxiliary bundle permitted; used on the ample normalization bundle with smooth obstacles | 1, 5, 29--30 |
| Boucksom--Chen, Compositio 147 (2011) published PDF | Multiplicative filtration, ample-series Lemma 1.6 with proof, adjacent concave-transform hypotheses | 1, 8--10 |
| Berman--Boucksom--Jonsson, arXiv 1509.04561 v3, 8 September 2020 | Quasi-psh divisorial multiplier estimate B.4, discrepancy and Lelong normalization | 1, 34--35 |
| Demailly--Ein--Lazarsfeld, arXiv math/0002035 v2, 17 April 2000 | Analytic subadditivity 2.6(ii), via local psh-plus-smooth reduction for quasi-psh weights | 1, 12--13 |
| Darvas--Di Nezza--Lu, arXiv 1705.05796 v3, 6 May 2018 | Exact unrestricted mixed-mass monotonicity signature, Theorem 1.1 | 1--2 |
| Darvas--Xia, Advances in Mathematics 397 (2022), published PDF with cover | I-envelope Proposition 2.18(ii) and adjacent exact ideal/singularity statements | 1, 22--23 |
| Darvas--Xia--Zhang, published 2025 PDF | Class-volume energy (34), finite-energy domain and Theorem 3.17; concordance with older (43) | 31 |

Source SHA-256 values:

- MP: `9eb2ea7686a5962ebc11c5eacd23b0cb3dcb081e27ac48292933f291fc82cb23`.
- DXZ: `7fede7c413e396008217a4a4c9638776dbdd7cacff90fdd463bf5ae48220246c`.
- XiaOps: `773eea71af9f1fff112bf5fcab2b9046b81467df2e37165ee1da3949ff74c6d9`.
- BJ: `50bd6e6782c29088edc96d013a5d49257b0395d9fb398664f1a9859639992948`.
- Berman: `6b1d6a1f595a9353d928d26c13c417fd560d1c63e248d054e4ac5de03d3af7c0`.
- BC: `0ed60336258435ffc720b4940c54b714750f5e3af49b92e33c66a02e829c94f2`.
- BBJ: `6973d1df47b527ce9c27e2496d8bd91b949c8e28b4123c2f708e45ccc6836b00`.
- DEL: `59219defe8729b2cd8db7e05cabec3736832e3bfd5aad4ac1b58390c801337a2`.
- DDNL: `1e614744bc4d769f377827ca81774b5f6c3d345a2619216fb6f4c81682d599cc`.
- DX22: `a09dc667342b2ffb75ff55de9660c97f4d6238245f3e23ed3992cb2dfab79b61`.
- DXZPublished: `467778ff37b893681482e43b4d8f1d717e947a34fe61026b2e6bc418e4a1f70e`.

Stacks tags 0AY8, 0BXQ, 01PR and 02O1 were read through the relevant proof
bodies. Proper birational pushforward uses a normal integral target;
normalization is finite; conductor multiplication precedes return to the
original graded series; ample twisting and Serre vanishing supply the fixed
degree correction. This is not finite generation of the whole graded series.
BFJ/strong-openness inputs are retained via the explicit internal imports
and immediately preceding chapter/source reviews, without a claimed new
GZ PDF inspection here.

## Worked calculations, build and rendered review

The finite exact supplement passes 35,379 checks in sixteen families:
multiplier-floor superadditivity and errors, finite running slopes,
translation/scaling, Gauss normalization, the worked grid values, dense-grid
and proper-support limits, truncation endpoints, rational domination of
monomial ideals, ideal sums/products, raw/relative DH first moments,
probability translations, wrong-class-volume divergence, surface/product
zero-volume examples and cusp-conductor fixed-degree costs. These illustrate
the written proofs and make no general-theorem verification claim.

Four changed-source full builds pass. The final build removes a source-note
line overflow found in the intermediate build logs. The final PDF
has 4,154 pages and 19,381,539 bytes. Chapter warning/overfull counts are zero;
unresolved references/citations, missing glyphs, rerun requests, fatal errors
and duplicate PDF destinations are zero. Eighteen inherited overfull boxes
elsewhere remain for the whole-book pass.

All 36 chapter pages, physical 3571--3606 (printed 3501--3536), and adjoining
pages 3570/3607 were visually inspected in ten contact sheets. The review PDF
contains the 36 chapter pages:
/workspace/book-completion-drafts/Chapter_71_Final_Review_2026-10-02.pdf.
The preceding seam is the intentional blank after Chapter 70. No clipped
display, bad destination or other reviewed layout defect remains.

Main final SHA-256: `fd2f4eca661cfc46fc3d540ef607bb9a4c59df9c45f7b2f06d96667ead89c6de`.
PDF SHA-256: `790057a461c08ea7eb3aaf010bb2ecb937e44c79980a87e99b0dd0824c700ca0`.

After rendering, scoped object/house-convention and protected-byte checks
pass. References pass for 425 inputs and 12,388 labels, with no missing
input, duplicate label or dangling reference. All six checker tests pass.
The active problem inventory remains 42 atoms in twelve environments,
tiers (0,3,7,15,17). Git diff --check and the staged whitespace gate pass.
The unavailable legacy writing-audit command is replaced by the documented
manual and scoped review; no legacy-command success is claimed.

Chapter 72 is next. Work remains local pending explicit remote-push approval.
