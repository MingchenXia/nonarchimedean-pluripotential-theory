# Chapter 72 completion audit

Date: 2 October 2026. Base: local Chapter 71 commit 5a5b897.

The sequential review covers the whole live Chapter 72 and its 39 TeX inputs.
It also synchronizes the P05 scope paragraph in the atomic inventory. This is
a direct mathematical, source and editorial audit, not a new independent
verifier verdict or priority claim. Independent open-problem research remains
paused. Frozen releases, receipts and checksum ledgers are unchanged.

## Architecture and proof review

All forty source files were read in full. The final closure has 9,861 lines,
207 semantic labels, 51 formal assertions and 51 proofs: thirteen theorems,
fifteen propositions, six lemmas and seventeen corollaries. All 69 reusable
environments are labelled, including twelve problems, three examples, two
remarks and one definition. The main chapter has nineteen assertions/proofs
and all 27 section/subsection headings have labels. Twenty-three new labels
supply the missing navigation. The main source has 6,535 lines and 360,900 bytes.

The chapter now reports twelve genuinely open problem groups and 42 active
atoms, with tier counts (0,3,7,15,17). Historical counts and proof checkpoints
are dated rather than presented as current status. P06.1, P07.1 and P08.1 are
retired using the supplied singular-PL theorem and negative answers; their
remarks retain stable labels. Long P07.1 checkpoint discussions now state
what was open at that checkpoint and distinguish the later counterexample.
The closing ledger matches these changes. The opening separates the original
24 August literature cutoff, targeted 19 September update, supplied/recorded
26 September inputs and this editorial review. It claims no exhaustive
2 October literature update.

The proof/interface review explicitly checks:

- P01 current positivity, residue nefness and model semipositivity only on
  the stated pure, good, separated, strict, boundaryless analytic scope;
  generated psh and ordinary current positivity are not identified generally.
- P02 invariant toric regularization on local convex neighbourhoods, versus
  arbitrary potentials and the distinct ordinary/weak/smooth/PL classes.
- P03 strict-polycylinder positive cases, non-split pinched domains, residual
  Picard and radiance obstructions, and the surviving higher-dimensional
  current compatibility requirement. A cover, a basis, a fixed-domain result
  and scalar-extension input retain distinct hypotheses.
- P04 the protected Gauss-shell raw-mass calculus, divisorial normalization,
  restricted mixed intersections, finite-map degree, the single link
  normalizer, and the failure of probability normalization under restriction.
  Polar extended-valued and non-pluripolar products are not conflated.
- P05 integral-slope/rational-constant PA versus real PA, the half-slope
  obstruction, real one-dimensional regularity and its exact orthogonality
  criterion, positive-growth versus unrestricted claims, cross/Bergman
  counterexamples and conditional proper-realization calibration.
- P06 singular PL regularity versus positive-current recognition and generated
  regularization, including the precise strictness and scalar-stability gates.
- P07 first-stage and generated sheaves, universal ordinal stabilization,
  fixed-core sufficient cases and the supplied abstract negative example;
  the latter is not claimed to classify analytic realizations.
- P08 the negative global-smoothing answer and invariant complete-toric positive
  case; rational-model approximation and literal ordinary global smoothing
  remain different questions. The proper analytic extension is also negative.
- P09 cubical delta-metricity, residual isotriviality, real PL decomposition
  and the good-reduction cohomology counterexample with exact source scopes.
- P12 excellent normalized boundaries, curve conductor descent and tower
  formulas. The ideal-psh candidate is an order-theoretic class, not an
  independent geometric psh identification. Weighted norm trace is kept
  separate from unweighted trace and from Monge--Ampere pushforward.
- P13 invariant affine-cone carrier and explicit probability exception;
  fixed-polarization image and cross-polarization comparison remain separate.
- P14 the repaired V15 upper semicontinuity input and full compact-Kahler
  DXZ--MP comparison, including proper-support semivaluations. Historical
  packets are not asserted to bind changed ancestor bytes. Strict-interior
  filtration recovery does not solve arbitrary terminal zero-mass recovery.
  Relatively nef MP models cannot realize a non-nef generic class.
- P15 static class bodies, current-level toric mixed volumes and singular-type
  data have separate domains. Class-level zero-volume bodies do not construct
  normalized zero-mass energy or a probability-valued operator.
- P16 the seven existence axes, the already projective nature of a proper
  algebraic ample-line-bundle setup, arbitrary-field toric skeletal existence,
  and the distinction between extended continuity, finite continuity and
  finite energy. Banach-base continuity is raw cycle-weighted; the literal
  endpoint-continuity question has a negative answer in both displayed forms.
- P19 imported static stability results retain their supplied cutoff and do
  not discharge the four surviving hybrid targets. P21.3 remains a genuine
  higher-dimensional gluing problem outside the explicitly proved domains.

All unprotected legacy inline dollar pairs are converted to the house
convention. Frozen/protected legacy notation remains byte-identical.

## Material P05.3 proof and scope repair

The adapted live fragment ch72_p053_projection_recursion.tex required a
substantive repair. Its former argument inferred generated continuous psh
from ordinary current positivity without proving that bridge.

The algebraic corollary now explicitly assumes an algebraically closed,
complete, nontrivially valued field whose logarithmic value group contains
Q. Rational affine pieces are then rational combinations of character logs,
and their rational comparison constants lie in the value group. On compact
strict neighbourhoods the comparison regions form a finite strict G-cover,
so the pullback is real PL in the precise GRPL section 2.5 sense. The pure
very-affine analytification is good, separated, strict and boundaryless.
The book's real-PL positive-current/model-semipositivity theorem and the
verified PL/psh equivalence then place it in generated continuous psh.
For a general ground field, the abstract proposition still requires its
explicit h*PAPC subset CPsh assumption; rational constants alone do not prove
that assumption. The main chapter and P05 inventory now state this boundary.
General-field operator-domain realization remains part of P05.5.

The mixed boundary-nullity proof also formerly averaged the reference
functions, which need not stay in the literal integral-slope class. It now
uses their integral sum b = sum a_i and positive reference scale d gamma.
Its literal approximants decrease uniformly with that scale. BMPS
Proposition 4.16 makes the diagonal boundary mass zero, and Theorem 4.13
permits the separately referenced mixed limit. Finite-stage multilinearity
expands the sum's top product into positive mixed measures; positivity then
forces every boundary term to vanish. No division of slopes by d is used.

The historical accepted P05.3 record remains a record of its archived
payload. The repaired live proof and narrowed algebraic corollary are not
claimed to have a new independent verifier receipt, or to be byte-identical
to that earlier accepted payload. The abstract operator assumptions remain
visible. This is a scope/proof correction under the editorial programme.

## Preservation

All 36 frozen packet inputs and both other adapted fragments are identical
to the entry baseline. Thirty-two protected main-source objects are also
unchanged: nineteen assertion/proof pairs, twelve complete problem statements
and the protected Gauss-section body. Some protected objects overlap, so
no sum of their byte lengths is presented as a disjoint coverage count.
Only the main source and the P05.3 adapted fragment change in the TeX closure.

Protected live SHA-256 values:

| Object | SHA-256 |
| --- | --- |
| corollary: cor:p02-invariant-toric-germwise-regularization | `3e5bf000af7ca682a069cf332f34b6d0483253e234939f314c8a5fd1c25bc3b9` |
| corollary: cor:p033-invariant-toric-locally-convex-envelope | `462c4c2d0a2b3ab9e1c5f8fb96f8a7b98c581cd8812d348a99c1802f338d0fcb` |
| corollary: cor:p033-invariant-toric-germwise-lfs-envelope | `addecca984be3c718dbe2b5da3f377b2ee81f454a7da7ce39b6fed54b323dcec` |
| corollary: cor:p033-invariant-toric-germwise-full-envelope | `ca51cb63d974c818c6be682713948c483e0070191beb266060955b2ec4444912` |
| lemma: lem:frontier-local-ma-gauss | `ba5e8470c34463321f67ec5f8f4a88af160443f1fc46046a4a96d8f9f8eee48d` |
| lemma: lem:frontier-local-ma-common-model-core | `38c25d134c124f41801c6bb35c14a33b50640843a21119213934d92d206a0f38` |
| theorem: thm:frontier-local-ma-model-comparison | `6c6648d27eb853d8d5a5294ee22830933ab2141c022f2c432fdad1c3d389e6ee` |
| proposition: prop:frontier-local-ma-independence | `e8116a40d08e0c45abfc4a448d51b10e34072af84018ce079da265d03b5a907d` |
| proposition: prop:frontier-local-ma-bounded-closure | `816c31b6a7172b5b0ee87157668ce37d438bbdcf131c6bf568539c438302b1f6` |
| proposition: prop:frontier-local-ma-reference-ideal | `6af150f8b9892a9728a7c32f65cbe3e8c4708d23ab960ef31f81c2a680db920b` |
| proposition: prop:frontier-local-ma-finite-map | `7c76dd73891dfc1c2c1eace7abc6218ac8e7f6996c1a0c3ba03c1a4617710316` |
| proposition: prop:frontier-local-ma-no-probability | `cf720194c6965842241eaaa03c05094d801fe3e59c4a923ccc0d62f073d6a7c9` |
| theorem: thm:frontier-common-local-ma | `e270c78b695804bc0dac1a8c581d4be96f297fa09d859edbf5b6080f296e5753` |
| proposition: prop:frontier-polyhedral-bounded-reference-shift | `e33db23f42cf06bf2f3e55e679cb5a26c3fc99db52689842e971b348368f297a` |
| lemma: lem:frontier-polyhedral-affine-contact | `54d7be9268fae637fdcbe3a15d466b4c0ca49caccd53bbbd43a966e2e1aa8fe9` |
| theorem: thm:frontier-polyhedral-affine-orthogonality | `988b3eec9058a6cef5f62e9b68d9a1acd1d4a195adb10accfaee0ed4c23bb04a` |
| proposition: prop:frontier-polyhedral-bergman-positive-infinity-obstruction | `7760da9cc954e30550993d839dc22a15e1a873943c02d2cfef7ab650f2eb98d3` |
| proposition: prop:p081-invariant-projective-toric-global-smoothing | `ac06b331b195b8ec9a864545a10b86c0e4423120c69f58cd67fafbda56934d84` |
| proposition: prop:p164-arbitrary-field-toric-skeletal-endpoint | `f1fab8c5ff0ecf9a57b060ba1d3504cac4caa98538085031cd25e15a716ac15b` |
| section: P04-complete-local-MA | `29e48f11eb3f412177db20635e706071113a4b3fe2a9e1a7d5d03e95e06c5ef6` |
| problem: prob:frontier-classical-regularization | `c093a83b20fcc82b77e0d8d7c07c79e7ab004b575575c370ca0af2677f783a26` |
| problem: prob:frontier-unibranch-local-envelope | `2b0493cfb1dec6b6a9955a812de0a482d4d41191f76ad1bcd165d437da07ec36` |
| problem: prob:frontier-local-ma | `25f079f4179535f4fa51015d9c1863cb56311abf528dfc739a51f9a6f2de5dc3` |
| problem: prob:frontier-polyhedral-regularity | `44e06f6d07675c1d8d19840931dbc0fbd2ab1252fa47034f8da8a506ebefb11e` |
| problem: prob:frontier-pluriharmonic | `a65f492d3d7ee7e460398855f93d49406191a0572c978cea4145411dc22aa9b2` |
| problem: prob:frontier-singular-local | `050ec1ea7fd75bafba2e2a7183e7c91cf0ccf0bfff77053e2eca90868638f1d9` |
| problem: prob:frontier-affine-cone-ma | `be760e9f5e37d225d495b472d7e457ce24258d0647bc8f933875089cd0c3c27f` |
| problem: prob:frontier-mp-pseff | `a2090c92812fe7fbed98243ac9071281a5cf1c9446b3ddd2c06cb644e3a53e86` |
| problem: prob:frontier-zero-volume | `bc46d48d1b02bcd30cf29266de73cff563f4b6438fbac864844528359bc77d0f` |
| problem: prob:frontier-general-ma | `e57f7341bdbb54840802463ca2b8dd035bf4c3cd0779f224b54c931e16255d1f` |
| problem: prob:frontier-hybrid-ytd | `2f55d83414542bd778e6132eab280c01782350aed9ac33c78981952f95d39592` |
| problem: prob:frontier-cross-fan-upstairs | `3d021d1059ab1d0248459b5c6591b1bcd983f9e0f64c23792f1c8cad70e49426` |

Main entry SHA-256:
`371dbca6594e9f17ddedb9510ed90013fc98f0f1c59db9b6b3e2ab21af4bb22b`.

## Fresh primary interfaces and documented reuse

Five PDFs, 73 selected physical pages and all twenty source contact sheets
were read and visually reviewed. BMPS, GK17, GK19 and BGJKK were fetched for
this review; GRPL reuses the recent Chapter 69 PDF, checked again here.
The BMPS download equals the archived PDF bytes. BGJKK is an arXiv witness
for the internal theorem numbering; identity with the published 2025 PDF
is not claimed. Other already integrated imports use their exact internal
interfaces and the documented Chapter 66--71 source audits. This is not a
claim to have freshly inspected every paper mentioned by Chapter 72.

| Source | Checked interfaces | Selected physical pages |
| --- | --- | --- |
| BMPS, arXiv 2603.08664 v1 | Integral PA convention; PAPC and MA construction; separately referenced continuity 4.13; diagonal boundary nullity 4.16; mixed calibration 4.20; envelope and literal/real distinction 6.2/6.4/6.6/6.13; curve and cross/Bergman examples; SYZ 7.2/7.3; planned sequel | 1--5, 11--12, 14--17, 26--36, 44--46, 48--57, 59--62 |
| GK17, arXiv 1406.7637 | Tropical cycles and lattice indices; projection and proper tropicalization; integral formula and Radon measures; delta calculus 9.9--9.15; raw metric calibration 10.2--10.4 | 14--16, 32--33, 40, 47, 55--57, 73--76 |
| GK19, arXiv 1509.09079 v2 | Functorial positivity 2.13; ordinary-current psh definition; locally approximable metric calculus 8.4 and basis remark 8.5; adjacent 8.7; delta pullback 8.8 | 10, 14--16, 30--33 |
| BGJKK, arXiv 2102.07392 v1 | Extended continuous singular metrics; invariant toric dictionary and local approximability; global decreasing smoothing 5.4.4/5.4.5; arbitrary-field skeletal existence 6.3.13 | 28--32, 43 |
| GRPL, 26-page source witness | Good/strict/boundaryless algebraic analytification; precise strict G-local real-PL definition in section 2.5; source current/PL boundary | 3--8 |

Source SHA-256 values:

- BMPS: `5cf7e68ee9113f1dc813f9aefa5f9ca72cba02fc4fa688f1a61e4b7f0d1223e7`.
- GK17: `62c7e4dfebab75d725f529c6ef78c300856c63fd050a9399e8a86879e569315d`.
- GK19: `36ce3e8bb8758eb67af4320dd4e23bf65297fb80abea64ce87a160683b300dbd`.
- BGJKK: `dee1f0c1e44db73aa69033e23ae9170db5bbfe4cd6f943be954b1b646b1d3b8a`.
- GRPL: `2ac2d4bd2016c1692271b1a124013585c903288f5d182081dcdaaf824095eb1b`.

The BMPS planned-sequel locators are corrected to introduction pages 3--5
and the page-60 bibliography. The toric existence statement uses extended
continuity as defined by the source, without asserting finite weights or E1.

## Calculations, build and rendered gate

The finite supplement passes 1,872 exact checks in twenty families:
literal slope separation, balanced vertex kernels, the cross mass -2 epsilon,
integer-sum polarization, positive versus signed boundary nullity, lattice
projection, sign reversal, factorial calibration, separable contact, Gauss
normalization, raw finite-map degrees, one-time link normalization, raw versus
probability restriction, trace towers, cusp conductor cost, annular radiance,
zero-volume rank, extended-weight energy and hybrid normalization. These
finite illustrations supplement the direct proof review; they do not prove
the imported general results or create a verifier verdict.

The changed-source full build passes. The final PDF has 4,156 pages and
19,389,423 bytes. Chapter warnings/overflows are zero. Undefined references
and citations, missing glyphs, rerun requests, fatal errors and duplicate
PDF destinations are zero. Eighteen inherited overfull boxes before this
chapter remain for the whole-book pass.

Every chapter page was visually inspected: physical 3607--3750, printed
3537--3680, plus adjoining physical pages 3606/3751, in all 37 contact sheets.
The final chapter page is an intentional blank. The preceding seam contains
the end of Chapter 71 and the following seam begins Appendix A. No clipped
formula or reviewed layout defect remains. The review artifact is the full
build PDF at /workspace/book-completion-drafts/Chapter_72_Final_Review_2026-10-02.pdf.

Main final SHA-256:
`4527a1f2da94b57ca7409e4cd8bc34ae0ab88430b9989155a6aa287953c95640`.
PDF SHA-256:
`726374c0b2c8c3532022af678998a2a4093b342b9af62f7b68b07bfaf9d3f6ef`.

After rendering, all object labels, 27 heading labels, protected blocks,
frozen inputs and unprotected house delimiters pass. References pass for
425 inputs and 12,411 labels with no missing input, duplicate or dangling
reference. All six checker tests pass. The active problem inventory passes
at 42 atoms in twelve environments, tiers (0,3,7,15,17). Git diff --check
passes. The unavailable legacy writing audit is replaced by this documented
manual and scoped review; no legacy-command success is claimed.

All 72 chapters now pass the sequential programme. Appendix A is next, then
the remaining appendices, front matter and final whole-book checks.
Work remains local pending explicit remote-push approval.
