# Rethlas verification receipts

This ledger records the production receipts that control mathematical
promotion or exact-current integration during the present revision.  It
includes book-local results and separately identified source syntheses; a
receipt does not by itself assert novelty, publication, or priority.  A
`VERIFIED` entry means that the exact statement and proof
were checked by the production Rethlas verifier with `gpt-5.6-sol` at `xhigh`
effort, after source and domain hypotheses were made explicit.  Later edits to
a statement or proof invalidate its receipt until a fresh audit is recorded.

## Current release boundary (through 29 August 2026)

This ledger is not a book-wide Rethlas completion certificate.  It records
nine mathematical production gates completed on 24 August.  Eight are
exact-current gates: the two Chapter 18 results recorded below, the Chapter
23 fixed-skeleton selection, the Chapter 49 truncation-energy package, the
Chapter 55 toric zero-mass package, the two separate Chapter 55 blocks that
integrate Xia's Conjecture 8.8, and the Chapter 69 toric-dimension block.  The
ninth gate verifies the exact frozen statement and source-aware proof packet
for the Chapter 70 generalized-Lelong separation theorem; that packet was
integrated only after a separate hostile audit, but has not received a
post-integration byte-identity gate.  All nine runs have status `final`,
verdict `correct`, zero critical errors, and zero gaps.
The BJ22 basic-closure integration is still a source-audited import without an
exact-current Rethlas receipt; the standalone MP reduced entropy-slope
reconstruction also remains pending.  Candidate-only packets and runs on
stale bytes are not receipts.  The separate clean whole-book build of the
25 August current working source has passed and is recorded in
`editorial/current_source_build_20260825.md`; it does not enlarge the
mathematical scope of any receipt.  The earlier
`output/BUILD_AND_AUDIT_SUMMARY.md` records the distinct dated 24 August
release snapshot.
The 25--28 August addenda below record further frozen-packet gates and preserve
their failed predecessor runs; they do not retroactively enlarge any of the
nine 24 August gates counted in this paragraph.

## Chapter 18 — unrestricted GJR cohomology question

- Status: **DISPROVED** (24 August 2026).
- Book location: `prop:ch18-gjr-cohomology-counterexample` and its adjacent
  proof in Chapter 18.
- Exact answer: the canonical GJR injection is not always an isomorphism.
  For the constant good-reduction elliptic curve used in the book,
  `M_R=0`, while GJR Theorem 1.14 gives a one-dimensional weakly smooth
  `H^{1,1}`.
- Scope: this is a counterexample to the literal unrestricted question in
  GJR Section 1.15.  It does not decide the totally degenerate restriction.
- Live Chapter 18 SHA-256:
  `8e1ca749f52d628f8a8681ff7eba03496fdcab75d8371abbb34dc919d20601cf`.
- Target-statement SHA-256:
  `fcddc3abc33d3d10de1f5e84b14a892e9ac193a48befaaa51a8104c2ac860e58`.
- Source-aware composite proof-context SHA-256:
  `99d7583f90ebf7dcb56a40dcc04463ffcb0c04ee4c1c711e0acafacdc85dbe2c`.
- Production run: `20260824T123617Z_fcddc3abc33d`; proof item
  `pi_a039b322c111642b44684f4e`; `gpt-5.6-sol`, `xhigh`, final verdict
  `correct`, zero critical errors, zero gaps.
- Exact-current receipt:
  `editorial/rethlas_receipts_20260824/ch18_gjr_cohomology_counterexample_exact_current_receipt.md`.
- Provenance: direct consequence of the published GJR injection and curve
  cohomology formula together with the standard good-reduction extreme of
  Raynaud uniformization.  No novelty or priority claim is made.

## Chapter 18 — semipositive integral decomposition in residual dimension at most one

- Status: **VERIFIED** (24 August 2026).
- Book location: `thm:ch18-semipositive-integral-residual-curve` and its
  adjacent proof in Chapter 18.
- Scope: a good strict analytic space over an arbitrary complete
  nontrivially valued field; a point whose completed-residue-field
  transcendence degree is at most one; coefficients in `Z` or a divisible
  additive subgroup of `R`.  Every semipositive PL germ has, on one strict
  analytic neighbourhood, a finite nonnegative-coefficient decomposition
  into integral semipositive PL functions, all but at most one integral
  harmonic.  Boundary points are allowed, and no algebraic-closedness or
  value-group compatibility hypothesis is imposed.
- Residual boundary: this settles the natural positive-cone formulation for
  all good strict analytic curves and, more generally, in residual dimension
  at most one.  The next two verified results settle the arbitrary-dimensional
  question by separating signed span from positive-cone generation.
- Live Chapter 18 SHA-256 at submission:
  `b35a05039dc061151b0d940498562220a83d1d61889ed699f0fac7e351b18444`.
- Exact statement SHA-256:
  `b656ed062f537dfd609fcf69d4efd2d6ab8f767311af75ae72cbd704d0611803`.
- Exact adjacent proof SHA-256:
  `1d1fa9a93164ba1f29e20e9b59172aeffff78227ec2f7e8f1097bd248aa29f19`.
- Production run: `20260824T135721Z_81346238f7dd`; proof item
  `pi_fa66bb9ea857f58ce38688a6`; `gpt-5.6-sol`, `xhigh`, final verdict
  `correct`, zero critical errors, zero gaps.
- Exact-current receipt:
  `editorial/rethlas_receipts_20260824/ch18_gjr_semipositive_curve_exact_current_receipt.md`.
- Provenance: a book-level deduction from the GJR residue criterion,
  common-model formalism, openness statement, and an integral splitting of
  the one-dimensional degree functional.  No novelty or priority claim is
  made.  The arbitrary-dimensional resolution is given by production runs
  `20260825T130036Z_c1607c25ec38` and
  `20260825T130707Z_4c4a1f2c885f`, both final `correct` with zero critical
  errors and zero gaps: signed generation holds in every residual dimension,
  while positive-cone generation fails in residual dimension two.  Exact
  hashes and scope firewalls are in the P09 integration receipt.

## Chapter 18 and Chapter 72 — real-PL zero-current converse

- Status: **VERIFIED FROZEN PACKET / INTEGRATED WITH CONTINUOUS FIREWALL**
  (25 August 2026).
- Book locations: `prop:ch18-real-pl-zero-current-harmonic` and its full
  proof in Chapter 18; the narrowed `prob:frontier-pluriharmonic` discussion
  in Chapter 72.  Wanner's published continuous curve scope is recorded as
  `cor:ch19-continuous-zero-current-harmonic`.
- Scope: a complete nontrivially valued field and a good, separated,
  boundaryless, strictly analytic pure-dimensional space of positive
  dimension.  A real-PL function whose CLD
  \(\mathrm d'\mathrm d''\)-current vanishes is GJR harmonic and classically
  pluriharmonic;
  equivalently, all of its residual classes are numerically trivial.
- Proof mechanism: decompose over `Q`-linearly independent coefficients;
  use rational coefficients of the codimension-one calibrated CLD skeletal
  currents on a common minimal analytic skeleton; then refine by the moment chart of
  each arbitrary compactly supported test form.  No analytic current is
  pulled back and no target-side boundary separator is used.
- Exact-live statement SHA-256:
  `655e7f503e5db0cee8e0c94fdc765b6923aeebb7b89c7b5b98ad7827fa6e2421`.
- Exact-live source-aware proof SHA-256:
  `7ad130bab1d9dd61ecbac818005c4b80fe405c3d9710a6bb588fea6fa30a856a`.
- Exact request SHA-256:
  `29704a697a6f17c1a6bf15a578a028126e322059a08353d1acc76cd6921ebef7`.
- Production run: `20260825T061351Z_655e7f503e5d`; proof item
  `pi_eea98ea0a54108cae4e076be`; `gpt-5.6-sol`, `xhigh`, final verdict
  `correct`, zero critical errors, zero gaps.
- Controlling exact-live receipt:
  `editorial/rethlas_receipts_20260825/p06_real_pl_zero_current_live_scope_arithmetic_v4_production_receipt_20260825.md`.
- Superseded history: run `20260825T032958Z_3a27f19be958` controls only its
  earlier frozen packet.  Exact-live intermediate run
  `20260825T055921Z_655e7f503e5d` returned final `wrong` with two gaps; its
  repaired successor is the controlling run above.
- Rejection history: round one, run
  `20260825T031243Z_1603e0a83037`, item
  `pi_ef4b8ab22822f1ccc0242d30`, returned final `wrong`.  Its unsupported
  target-boundary separation step is not present in the live proof, and all
  negative artifacts remain preserved.
- Scope firewall: the arbitrary continuous higher-dimensional case remains
  open.  The continuous curve result uses Wanner's published theorem only in
  its algebraically closed, complete, nontrivially valued, smooth proper
  algebraic-curve scope.  No novelty or priority claim is made.

## Chapter 19 and Chapter 72 — failure of ordinary smooth harmonic approximation

- Status: **VERIFIED EXACT-LIVE COUNTEREXAMPLE / COMPATIBLE WITH LATER PSH RESULT**
  (25 August 2026).
- Book location: `prop:ch19-cld-smooth-harmonic-nonregularization` and its
  full proof in Chapter 19; the re-scoped P06.3 discussion in Chapter 72.
- Exact scope: on a smooth proper GJR theta-curve, an integral PL harmonic
  function on a relatively compact three-arm neighbourhood is weakly smooth
  with zero weakly smooth curvature but is not a locally uniform limit, nor a
  decreasing pointwise limit, of ordinary CLD-smooth harmonic functions.
- Statement SHA-256:
  `b5c8f0719b606707b8055f0ead8c1baa96b5d9732cccf51a0e86ec02c5e64f24`.
- Proof SHA-256:
  `ba402983b6d88c03437c79af66dfd541c5a37b89c0bb2a6a67438ac84120565b`.
- Request SHA-256:
  `2b564db26e52284aeafa88e0f8ed3ef39aed3a016c3a21716fdf80e437dd959f`.
- Production run: `20260825T055907Z_b5c8f0719b60`; item
  `pi_d80993bb01a748f0422ae6a5`; `gpt-5.6-sol`, `xhigh`, final `correct`,
  zero critical errors and zero gaps.
- Controlling receipt:
  `editorial/rethlas_receipts_20260825/p06_cld_smooth_harmonic_nonregularization_live_production_receipt_20260825.md`.
- Scope firewall: the proof uses vanishing curvature of every approximant.
  It does not disprove decreasing ordinary CLD-smooth psh approximation,
  which is now proved in the next record.  Positive curvature lets the later
  approximants move residual slope defects into fresh directions.

## Chapters 19 and 72 — ordinary CLD-smooth monotone regularization on curves

- Status: **VERIFIED FROZEN EXACT BLOCK / INTEGRATED BYTE-FOR-BYTE**
  (27 August 2026).
- Book location: `thm:p063-current-psh-ordinary-regularization` and its full
  proof in Chapter 19; P06.3 is retired in Chapter 72.
- Exact scope: algebraically closed complete nontrivially valued field;
  smooth proper algebraic curve; continuous function on an open subset.
  Current positivity, Thuillier subharmonicity, and local membership in the
  first ordinary CLD-smooth decreasing-limit stage are equivalent.
- Statement SHA-256:
  `767cbf81c723279c1218df4136f8e299465240b325f41f6b0663d001fb5d8a68`.
- Proof SHA-256:
  `d1db3c2db861d920598697fdad5d002a2b1ce947dbdbd95ad9b78b8f9f312bd8`.
- Production run: `20260827T090645Z_767cbf81c723`; `gpt-5.6-sol`, `xhigh`,
  final `correct`, zero critical errors and zero gaps.  The direct endpoint
  assigned no item identifier.
- Independent gates: three exact-byte hostile mathematical/source audits
  passed before submission.  Chapter 19 inputs the frozen statement and
  proof files without label or byte transformation.
- Controlling receipt:
  `editorial/rethlas_receipts_20260827/p063_curve_cld_monotone_regularization_production_receipt_20260827.md`.
- Inventory consequence: P06.3 is positively retired; 16 formal open
  environments remain, containing 55 active atoms with tier counts
  `(0,7,14,17,17)`.
- Scope firewall: harmonic approximants are not asserted; functions taking
  `-infinity`, higher-dimensional spaces, and curve scopes outside the exact
  theorem remain outside this result.

## Chapters 57, 58, 63, and 71 — full projective ample-class MP--BJ comparison

- Status: **VERIFIED FROZEN CANDIDATE AND EXACT-LIVE RUN2 / P00.1 RETIRED**
  (28 August 2026).
- Book location: the full-cone comparison theorem in Chapter 71 and its
  synchronized comparison summaries.
- Exact scope: connected smooth projective complex variety; every ample real
  numerical class for the MP--BJ order isomorphism; an ample rational
  line-bundle class and smooth representative for the composed full DXZ--MP
  order isomorphism.  Both conclusions concern all semivaluations and impose
  no finite-energy hypothesis.
- Proof mechanism: finite flag-ideal GAGA identifies the rational PL
  lattices; a common-refinement/direct-limit argument makes MP positivity
  testable on an algebraic determination; analytic and algebraic nef cones
  agree on the smooth projective central components; the MP and BJ decreasing
  completion theorems then identify the full cones.
- Frozen statement SHA-256:
  `e40829e3586bcabeeb866229dc068c2e518a736fc908dec32f3bf3957c59c9ab`.
- Frozen proof SHA-256:
  `baad23068e9dcae47619f3e2d81cfd26fa5bd51b1e4c4d4baa1a7c024824e671`.
- Production archive:
  `editorial/rethlas_packets_20260828/p001_mp_bj_full_cone_run_20260828`;
  response verdict `correct`, zero critical errors, and zero gaps.  Request,
  response, and safe-header SHA-256 are
  `5247582aa59d492ecc683c2740eac8783528df9dacb0b49aedb710c08dab677a`,
  `b2e490edd946e0c32d2e59ba941d77cc38425956f4cde0ecc82f49adc173917f`,
  and
  `c9dcbbbaae1d0b1064b9e21df6976bee6c7c647306cec57a85e43ea4588b4371`.
  The endpoint assigned no run or item identifier beyond the archive label.
- Independent gates: two exact-byte mathematical/source audits passed before
  the production submission.
- Exact-live gate: statement SHA-256
  `949819c48c8d0e991acbb92ed7c15d504dd691056f06553c58ac1d4ab564d33e`;
  proof SHA-256
  `58c2954ad1e541ab41e0649c4e84e22252299265b422159df41fe5772f2e8064`.
  Archive
  `editorial/rethlas_packets_20260828/p001_mp_bj_full_cone_live_run2_20260828`;
  verdict `correct`, zero critical errors, and zero gaps.  Request, response,
  and safe-header SHA-256 are
  `0117a2a2669e2980b620e9fedc53d9ca6fb59c9b8d312f9fa46935dad82bcea6`,
  `aa83284548a249c6e1538a7d0c352e6181936e4d79455b5a8f980400aec8b960`,
  and
  `1bf4eb42373b4422429660ca6be4c02fd27681fdd3ea3e76a52dd1edbe05c862`.
  The prior archive `p001_mp_bj_full_cone_live_run_20260828` also returned
  `correct`; its statement SHA-256 began `5d912`, and its proof already had
  the final hash above.  Run2 supersedes it solely because the live TeX
  equation wrapper was repaired; no mathematical content changed.
- Provenance: this is a book-level source-explicit synthesis of published MP,
  BJ, and DXZ results.  No novelty, publication, or priority claim is made.
  The frozen candidate and final exact-live bytes are both controlled.
- Inventory consequence: P00.1 and its Chapter 71 problem environment are
  retired.  Fifteen formal open environments and 54 active atoms remain,
  with tier counts `(0,6,14,17,17)`.

## Xia Conjecture 8.8 — repaired mixed partial-body formula

- Status: **VERIFIED** (24 August 2026).
- Book location: Chapter 55, `thm:ok-mvob-metrics` and its
  minimal-singularity specialization `thm:ok-mvob-line-bundles`.
- Provenance: the proof was supplied by the author as TeX for the unpublished
  work in progress *Mixed Volumes of Okounkov Bodies*.  Human source review
  and a hostile audit repaired the proof before verification.  This is not a
  claim of publication and not a first-draft priority claim.
- Scope: connected smooth projective complex variety; big line bundles;
  singular psh metrics with positive Cao, equivalently ideal-model, volume;
  supremum over surjective valuations to `Z^n_lex` trivial on constants.
  The receipt does not cover zero volume, transcendental classes, singular
  varieties, or attainment of the supremum.
- Controlling repaired proof packet:
  `editorial/solver_dossiers_20260824/xia_conjecture_8_8_repaired_proof_packet.md`.
- Proof-packet SHA-256:
  `9227826d7ba5c641c5fe32cc4daae9acbb3b57274dcc1b356ba8beadd58cad7b`.
- Target-statement SHA-256:
  `fe2b418a660abe1fcc3e3736d9f659c7c54deef95f92abdbda4d69a78aea91c6`.
- Receipt:
  `editorial/rethlas_receipts_20260824/xia_conjecture_8_8_repaired_receipt.md`.
- Production run:
  `20260824T023833Z_fe2b418a660a`.
- Verifier: `gpt-5.6-sol`, `xhigh`; final verdict `correct`; one checked
  proof item, zero failed or blocked items, zero critical errors, zero gaps.
- Exact-source corroboration: the complete repaired `main.tex`, SHA-256
  `5746eb011417caecfa876c05c6c74fb548e2ae9d086c1441189bbcad02a96594`,
  separately received the same `correct`, zero-error, zero-gap verdict in
  run `20260824T032252Z_b8adabf0730c`.  The secondary receipt is
  `editorial/rethlas_receipts_20260824/xia_conjecture_8_8_repaired_source_receipt.md`.
- Exact-current metric-theorem gate: statement SHA-256
  `57635bfa07f426eaa50998ba241506a6237a3127cf5113789f7d0cf43cf90a2c`;
  source-aware proof-context SHA-256
  `1092b9c37729db232f5b0978a7d267e7666144177c6c79be65f9aea170b8cd1e`;
  run `20260824T054849Z_57635bfa07f4`, proof item
  `pi_01a5edbb4e5e1a3a59ed8d9e`.
  Its exact-current receipt is
  `editorial/rethlas_receipts_20260824/ch55_xia8_8_metric_exact_current_receipt.md`,
  SHA-256
  `5621ff924a46a7b564013d915a67838e9140c44fbac6d26d06ba75784975b981`.
- Exact-current line-bundle-specialization gate: statement SHA-256
  `17bf73c6b37c1972447546c90625b9b99c5b8e251c04cab6e1cfdb1727e595d3`;
  source-aware proof-context SHA-256
  `866cb70a8f60ce2aa6fc89dad6725cc44e8bc5192456c5fad20b8a3ed8d85690`;
  run `20260824T061508Z_17bf73c6b37c`, proof item
  `pi_a7c98a7b328faf9358d70053`.
  Its exact-current receipt is
  `editorial/rethlas_receipts_20260824/ch55_xia8_8_line_bundle_exact_current_receipt.md`,
  SHA-256
  `6b9605ee62969f0f9506685ca03e2d164a8ac1086d0aa7f0e4a5ae38f446bce1`.
- Both exact-current gates used `gpt-5.6-sol` at `xhigh` and returned
  `final/correct`, one checked item, zero failed or blocked items, zero
  critical errors, and zero gaps.  Their source-aware contexts contain exact
  live Chapter 55 components and the primary-source locator attestations; the
  earlier repaired-packet and repaired-source runs remain supporting audit
  history rather than substitutes for these two live-integration gates.
- Exclusion firewall: neither the proof nor any load-bearing source path uses
  the excluded paper arXiv:1710.09731.

## R3-CLD-PL-01 — boundaryless PL psh equivalence

- Status: **VERIFIED** (14 August 2026).
- Book location: Chapter 69, `thm:verified-pl-psh-equivalence`.
- Scope: a real-valued real PL function on a good strict analytic space over a
  complete nontrivially valued field; the three-way equivalence is on the
  relative interior, globally when boundaryless.  Current positivity is only
  a one-way consequence under separatedness.
- New step: locally Fubini--Study functions belong to the CLD-v2 psh sheaf by
  decreasing log-sum-exp approximation; locally uniform LFS regularization is
  converted to a legal decreasing sequence by summable constant shifts.
- First audit: **wrong**.  It rejected arbitrary independent shifts inside an
  LFS maximum and a false pure-dimensionality restriction.
- Corrected audit: **correct**, zero critical errors, zero gaps.
- Production receipt:
  `/Users/mingchen/Documents/ChatGPT/Yethlas/Rethlas_isolated_20260813_232740/agents/.verification_receipts/cld_gr_psh_comparison_r3.json`
- Verified artifact:
  `/Users/mingchen/Documents/ChatGPT/Yethlas/Rethlas_isolated_20260813_232740/agents/generation/results/cld_gr_psh_comparison_r3/blueprint_verified.md`
- Proof digest:
  `d44d6b4dc9b01314b73ca0763c42bac0a547e4abbb4b745c88e2dc0fda994a5a`.
- Context digest:
  `b4c3358b595f50211767bf471f273c6ee56f2eb67707335ca9cd4a6b2ae3b195`.

## Chapter 23 — fixed-skeleton decreasing selection

- Current status: **VERIFIED** (24 August 2026).
- Book location: Chapter 23, the fixed-skeleton selection step in the envelope
  construction.
- Scope: one fixed determining dual complex.  The selected sequence depends
  on that skeleton; no global sequential cofinality and no sequence working
  simultaneously on every skeleton is asserted.
- Provenance: a book-local dense-set/common-modulus/finite-maximum argument,
  using published BFJ skeletal Lipschitz and finite-valued inputs.  It is not
  represented as a published BFJ theorem.
- Live Chapter 23 SHA-256:
  `acaf22a242ee48952d8d4339c9ebd7bd6fafdf5ac118dec66aaf1d67eaaa2bfd`.
- Target-statement SHA-256:
  `25024c43d265636b667320ddb4090b3882320790f029bbe8f3103808dd3595e8`.
- Exact proof SHA-256:
  `39884cd45e524d2fa6aaa4dd7320aac14d6d490c630870745f56ac7f763186f4`.
- Exact current statement-plus-proof slice SHA-256:
  `d91003dd920d193192b4dcd8a064ac46d5535cb6befc53bd08670db8451d7786`;
  it remains byte-identical to the verified production payload after the
  provenance and line-breaking edits elsewhere in the chapter.
- Receipt:
  `editorial/rethlas_receipts_20260824/ch23_fixed_skeleton_selection_receipt.md`,
  SHA-256
  `7124e8fd2736f2cd5a07f682c1114658fe10cbde149b259b6590bb45537840f1`.
- Production run: `20260824T044830Z_25024c43d265`; proof item
  `pi_4cc2365c9c77af25df553e8e`; `gpt-5.6-sol`, `xhigh`, final verdict
  `correct`, zero critical errors, zero gaps.
- The historical 14 August receipt and later stale-byte targets remain audit
  history only and do not control the current text.

## BJ22 closure repair — Chapter 34 integration (not a receipt)

- Status: **PENDING RETHLAS REVIEW** (22 August 2026); no production receipt
  exists.
- Book location: `thm:bj-basic-closure` in
  `parts/part4/ch34_fs_pl_psh.tex:2466--2588`, with dependent references in
  Chapter 35.
- Source boundary: imported from `BJ22`, Definition 4.1, Theorem 4.5, Lemmas
  4.6 and 4.9, Theorem 4.7, Corollary 4.17, Theorem 4.22, and Corollaries
  4.23 and 4.25. `BJ22b` concerns the envelope and regularized-envelope
  energy corrections; it does not replace the basic closure package.
- Integration boundary: positive scalars only; a zero coefficient omits the
  summand rather than forming `0*(-infinity)`. The former unconditional
  all-pointwise convergence claim was removed in favor of the source-backed
  divisorial determination and decreasing-net conclusion.
- Exact current block digest:
  `38bd7071c4722348dc8a29f7f890714e8e96e466fc09a814a63fbe93a95a5973`.
- Exact current statement digest:
  `50173e9c3be0fae0ea71b5ae2ec013fb107ed0dc427a143d37356fc325cafdcd`.
- Exact current proof digest:
  `2b115d0cd2abbf2568e158a8df722f8ec595bf50a0105a76aa69179d521d4093`.
- Current file digests: Chapter 34,
  `0d064f10d313e506a048df34c8f007bafe36db3f530df56f63e9c4c45437b0d9`;
  dependent Chapter 35,
  `45d39f528be1a0092be409e24f3aec575256ce10d6782dec831ff12e96a34851`.
  The extraction convention is the exact UTF-8/LF byte stream from
  `\begin{theorem}` through `\end{proof}` inclusive, including the
  terminal LF; statement and proof hashes use the analogous individual
  environment blocks.
- Required next step: submit the then-current exact block, its dependent
  Chapter 35 uses, and the 22 August source audit for an adversarial production
  review.  Until such a final exact-current receipt exists, the record
  `editorial/bj22_closure_repair_20260822.md` is an integration and
  source-audit record, not a Rethlas receipt.

## BJ22 Theorem 6.21 critical endpoint packet (not a receipt)

- Status: **PENDING RETHLAS REVIEW — QUARANTINED** (23 August 2026).
- Main-text status: Chapter 35 proves the strict case internally and imports
  the critical endpoint from BJ22.  None of the claims in this packet has
  been promoted to the book.
- Audit finding: the published residual-net argument needs
  `t_b-t_a <= inf_{K_E}(psi_a-psi_b)` to make the residuals decreasing; the
  displayed source hypotheses do not imply that inequality.
- Candidate contribution: an explicit `P^1` family challenges precisely that
  monotonicity step, without challenging the theorem, and an independent
  envelope property yields a conditional non-circular endpoint proof in the
  scopes stated in the packet.  Both assertions require production review
  before any promotion.
- Exact mathematical audit:
  `editorial/solver_dossiers_20260823/bj22_theorem_6_21_endpoint_audit.md`,
  SHA-256
  `25f8b6b742bb897b000d96989331c2bf86be1e2a9bf0093da8fba4ed9b77e107`.
- Exact Rethlas packet:
  `editorial/solver_dossiers_20260823/rethlas_packet_bj22_theorem_6_21_endpoint.md`,
  SHA-256
  `192baaddd4858b025099ff44938f1d075b4dfb4ad555c8deee082155e5cc7e15`.
- Source firewall: neither packet cites or depends on arXiv:1710.09731.

## Chapter 16 — first-stage CLD collapse on tropical toric partial compactifications

- Status: **VERIFIED FROZEN PACKET / INTEGRATED** (25 August 2026).
- Book location: `prop:ch16-collapse-tropical-toric`.
- Scope: tropical toric partial compactifications with their standard
  Lagerberg smooth structure.
- Exact conclusion: the toric psh, CLD psh, and first-stage CLD psh sheaves
  coincide.
- Production run: `20260825T024707Z_d1b8d7eaf79e`; proof item
  `pi_ccfb83de7a7be82ef602cd72`; statement SHA-256
  `d1b8d7eaf79e155ecf7b347e4fcc1717c72d5a8090e346b2cb2fc9c9a0996e63`;
  proof SHA-256
  `316a774fbb4eda54150b63cae0c9f23a1edab17a75b89beeee6d56d402f8c4a0`.
- Model and verdict: `gpt-5.6-sol`, `xhigh`, final `correct`, zero critical
  errors, and zero gaps.  The same historical packet contained a narrower
  finite-curve theorem, now superseded by the separate finite-star result
  below.

## Chapter 16 — first-stage collapse on finite ambient-induced real-affine stars

- Status: **VERIFIED EXACT FROZEN PACKET / INTEGRATED** (27 August 2026).
- Book location: `thm:ch16-collapse-finite-tropical-curves`.
- Scope: a finite set of pairwise distinct positive rays in a
  finite-dimensional real vector space, with stage-zero sheaf given by
  ambient-induced smooth functions convex on every branch; and Hausdorff
  spaces locally charted by such stars with generator-preserving transitions.
- Exact conclusion:
  `Psh_{S,1}=Psh_S=J_S`, with the junction Jensen characterization, and the
  corresponding chartwise equality.  Every germ has a pointwise decreasing
  smooth-psh approximation on one fixed neighbourhood.  Polar branches are
  included.
- Scope firewall: no lattice, rationality, weight, balancing, calibration,
  harmony, or boundary designation enters the theorem, but this does not
  identify the generated star sheaf with the CLD sheaf on every analytic,
  sedentary tropical, or nonambient local model.  Arbitrary higher-dimensional
  settings and infinite-valence stars remain open.
- Production verification: the direct endpoint returned final `correct`, zero
  critical errors, and zero gaps.  The archival label is
  `20260827T103835Z_c8131b22d800`; the endpoint assigned no run or item
  identifier.
- Exact SHA-256 values: statement
  `c8131b22d8002212e31cd526095317734a2b67be5d47f1387e5ee6bc041af5e3`;
  proof
  `921e8b46690e69cbacea66bf86cbcdf628e7dbc95651f526d62cc6d755d7cbcf`;
  request
  `ac68faee9ddb39bd3a30373e193196fc0a25431477a34e5c9cea6b49947299ed`;
  response
  `4f9a8b82e6eb7134cf76a5eac5ac0313db8f0e6cca082d369976db04ec115cfe`.

## Chapters 16 and 72 — dimension-one current classification, including nilpotent thickenings

- Status: **BOTH EXACT FROZEN BLOCKS VERIFIED / INPUT BYTE-FOR-BYTE**
  (27 August 2026).
- Book location: the reduced theorem is
  `prop:p21p3-curve-rigidity`; the exact addendum is
  `prop:p21p3-curve-rigidity-nonreduced`; Chapter 72 retains P21.3 only in its
  complementary residual scope.
- Exact scope: algebraically closed complete nontrivially valued field; good
  separated strict pure one-dimensional boundaryless analytic space, not
  assumed reduced; every irreducible-component normalization of the reduction
  is rig-smooth.
- Exact result: reduction identifies ordinary CLD forms and their compact-test
  topology, currents and weak topology, positivity, closedness, the psh and
  continuous-psh sheaves, and \(G\)-forms.  The integration current is instead
  `sum_i m_i delta_i`.  Every positive closed `(0,0)`-current is a unique
  locally finite nonnegative combination `sum_i c_i delta_i`; equality of
  curvature computed with the nonreduced integration current is equivalent to
  equality on the reduction, and every such current is Bedford--Taylor.
- Reduced packet: statement SHA-256
  `7cb598fbddb7b41aedcea7cf79fe44208d4c41b3e9a70e90e73819599354d5c4`;
  proof SHA-256
  `0ae0ee2d33425c58b26595ea2b27a268818e4c85e3dc269fc5aac962d3c64dd8`;
  production run `20260826T154751Z_7cb598fbddb7`, item
  `pi_383fc357b7bbce95a0e83cb2`, final `correct`, zero critical errors and
  zero gaps.
- Nonreduced addendum: statement SHA-256
  `3ee099341ca1ba77d806082ca2903320fd9db25c448b48f3dab9c2bb607a777e`;
  proof SHA-256
  `b8aac711aafa611750c56a960177182ff1b7b8f78b489d7b43575d03b28b7f43`.
  The direct production endpoint used `gpt-5.6-sol` at `xhigh` and returned
  final `correct`, zero critical errors, and zero gaps.  It assigned no run ID,
  item ID, or status ID; `20260827T133151Z_3ee099341ca1` is a local archive
  label only.
- Scope firewall: the theorem makes no claim over a non-algebraically-closed
  or trivially valued field, for a reduction with a component normalization
  not known to be rig-smooth, or in dimension at least two.  Borel
  multiplication is asserted for positive currents and local differences of
  positives, not for arbitrary order-zero currents.
- Inventory consequence: P21.3 remains one T2 residual atom.  There are 16
  formal problem environments and 55 active atoms, with tier counts
  `(0,7,14,17,17)`.

## Chapters 16 and 72 — arbitrary-field dimension-one current classification

- Status: **EXACT LIVE BYTES VERIFIED / INTEGRATED BYTE-FOR-BYTE**
  (28 August 2026).
- Book location: `lem:p21p3-gf-legal-source-localization`,
  `prop:p21p3-gf-virtual-annulus-bridge`,
  `lem:p21p3-gfc-rigid-zero-atom`, `prop:p21p3-curve-rigidity`, and
  `prop:p21p3-curve-rigidity-nonreduced`.
- Exact scope: every complete nontrivially valued field; good separated
  strict pure one-dimensional boundaryless analytic space, not assumed
  reduced; every irreducible-component normalization of the reduction is
  rig-smooth.  The Bedford--Taylor conclusion is for continuous psh pairs
  of equal curvature.  Literal discontinuous CLD psh functions, trivial
  valuation, non-rig-smooth component normalizations, and dimension at least
  two remain outside the theorem.
- New mechanism: legal source localization through analytic moments;
  cofinal virtual-annular collars; exact branch rays weighted by a common
  expansion index; residual closed points of arbitrary degree; and a
  residual-divisor/Riemann--Roch flux comparison.  Smooth cutoff plateaux are
  not tropical coordinates.
- Reduced exact-live gate: production run
  `20260828T042906Z_f2a1c1b9f2a3`, 17 statement records, 19 source records,
  zero failed checks and zero gaps.  Bridge statement/proof SHA-256:
  `f3202ef13495aad790ee2b1ff057a89b34e76eff15761c33c88e7b809c3e1033`
  and
  `ff8225ed6206f97e628504ab5b255c58a1a0de4fda13962e1ab09092fe2be7d5`;
  reduced statement/proof SHA-256:
  `c9f27245f5608b772385167c84bfe9e836fc9f4b164477a578b6c26712e35b21`
  and
  `01ab07fdacedfe95e1d764656a071a88395f5d0766115fd0a67164e3162410af`.
- Nonreduced independent gate: run
  `20260828T044008Z_dfdaa04a1cea`, 24 statement records, 25 source records,
  zero failed checks and zero gaps; combined statement/proof SHA-256:
  `dfdaa04a1cea28df3d689062fb46f513a7f7aea0ce8ac9f2a707f6c56029d6b4`
  and
  `f8eb8968f9ae269b621944cde4b114fa5733f1ae4f4b454284a37b70ea545abe`.
- Nonreduced exact-live gate: the controlling complete HTTP-archived run is
  `20260828T051601Z_db92555a72e1`, with 23 statement records, 25 source
  records, zero failed checks, zero critical errors, and zero gaps.  Exact
  live statement/proof SHA-256:
  `e7b9889f6c063d9952d61c0472290183aac07b58c8d0569cfebc5e9ea73f1a9c`
  and
  `25fe49a46b1c5cd62b0d1a5024095b47cdd49c66f594d1d86eec4f9f270c83ec`;
  materialized statement/proof SHA-256:
  `db92555a72e145591f922b3ffc623148dcaca7d252ea220d694203b04d164c49`
  and
  `b13829d962614f35af3f3725eb04be1d6f1b6b78490cb13d65e4ed43a05de779`.
- The controlling request, response, and safe-header SHA-256 digests are
  `d0cc30cbd8110de827077054d6320900865fff3d06657d9c659e412cadb79f64`,
  `e2e7d8943b8a4f5bbd677065299bda3ebae0d22be10a71f2962ae38c40830f3f`,
  and
  `0e23adb170ea7848dab43cc432b1f50aa29e8f37e3f9fdac0c06a4a667201299`.
  The service `verification.json` and final service-log SHA-256 digests are
  `f1e20502448f27381329b2b94612ea901c72cc3771db26c83f715c14c0a8e35a`
  and
  `69208e44e730089339cd3d1ae45e414c5cb8c6e56b3de4b32af98c258658ab3f`.
  The controlling exact-live receipt has SHA-256
  `193e4e63a6f6db4c747189ded171334ccc664f7474cd048fe7f123054f6f1cb0`.
- The earlier run `20260828T045515Z_db92555a72e1` passed service-side on the
  same materialized bytes, with the same 23 statement and 25 source records
  and no failed check, critical error, or gap.  Because its client directory
  lacks the response and safe headers, it is corroborating provenance only;
  the `051601` run controls the integration.
- All three mathematical gates used `gpt-5.6-sol` at `xhigh` and returned
  final `correct`, zero critical errors, and zero gaps.
- Whole-book gate: clean converged build, 3,207 pages and 15,433,695 bytes;
  PDF SHA-256
  `e2e68023a6b9e7a5e4bd671504d8226f6c1a377c9749bdf0c3745d2932d7c028`;
  log SHA-256
  `d91cbee2b685c928086c8b9f5d9156e4b4f7749eadacc6ff9d94200042a3a983`.
  There is no fatal error, undefined reference or citation, duplicate label
  or destination, rerun request, BibTeX or index warning, or overfull box;
  991 historical underfull notices and the benign class-path warning remain.
- Source closure: 127 files, all verified; manifest SHA-256
  `eecc05a93d3cdccf82b6b2411662ac16ce34221f3ced4829613b88119782514b`.
  Static scans found 9,913 labels and no duplicate, 30,768 references and no
  dangling target, 208 cited keys and no missing key, no exercises, and no
  optional conventional theorem-like name.
- Visual inspection passed on physical pages 737--765, 3035--3037, and
  3182--3184, covering the Chapter 16 theorem package, the Chapter 72
  residual statement, the Appendix L provenance gate, and all neighbouring
  transitions.
- Inventory consequence: algebraic closedness and nonreducedness are removed
  from the one-dimensional residual list.  P21.3 remains one T2 atom, and
  the total stays at 16 formal problem environments and 55 active atoms,
  with tier counts `(0,7,14,17,17)`.  This dated integration record makes no
  novelty or priority claim.

## Chapter 49 truncation-energy package

- Status: **VERIFIED** (24 August 2026).
- Book location: `lem:ch49-truncation-energy` and
  `rem:ch49-truncation-sharp` in Chapter 49.
- Repair: the estimate is now translation-covariant and assumes finite
  center \(c=\sup\psi\); the formerly omitted \(j=0\) mixed-measure term is
  retained as the Dirac mass at the trivial valuation.  Constant functions
  expose the need for centering, and the toric facet example gives equality
  in the coefficient \(n/(n+1)\) in every dimension.
- Scope: the positive-volume, probability-normalized BJ energy framework
  stated in the chapter; no zero-volume probability theory is inferred.
- Live Chapter 49 SHA-256:
  `c6755ba48b4c8295b72f6e9e4c22697c9e66acb2621c9304930d601737ec440a`.
- Target-statement SHA-256:
  `0c95825dbb063f1f257298e2ba12fd03e41645eba09aa320646e18f5b3f378e7`.
- Exact statement-proof-sharpness SHA-256:
  `312ac46575cb6fba6a0858e4eff38ad78cd223a0560ca0faa731e6c5396c99a2`.
- Receipt:
  `editorial/rethlas_receipts_20260824/ch49_truncation_energy_receipt.md`,
  SHA-256
  `ef22354c026d45885c30dceaa8af5ca88cd6ee01cc3497f234bc6e49dc9595ef`.
- Production run: `20260824T041218Z_0c95825dbb06`; proof item
  `pi_8189ce12c89257c9acec4eef`; `gpt-5.6-sol`, `xhigh`, final verdict
  `correct`, zero critical errors, zero gaps.

## Chapter 49 global Radon--Riesz counterexample

- Status: **DISPROVED / EXACT LIVE THEOREM AND PROOF VERIFIED** (25 August
  2026).
- Book locations: `thm:ch49-global-radon-riesz-counterexample`, the contrast
  remark `rem:verified-no-global-radon-riesz`, and the resolved history
  `sec:resolved-bj-radon-riesz`.
- Exact scope: on \(\mathbf P^n_k\), for every \(n\ge2\) and in arbitrary
  characteristic, point-blowup valuations centred at pairwise distinct
  points of one linear line converge weakly to the line-centred valuation,
  while both the sequence and limit have exhaustion one and their strong
  distance is at least one.  For \(n=2\) the limit is \(\ord_C\); for
  \(n\ge3\) it is the exceptional valuation of the blowup along \(C\).
- Production run: `20260825T044839Z_326e2035bbb9`; proof item
  `pi_9e222887262acc5d9fbc740a`; model `gpt-5.6-sol`, scrutiny `xhigh`, final
  verdict `correct`, zero critical errors and zero gaps.  Both process guards
  completed and the wrapper returned zero.
- Frozen SHA-256 boundary: statement
  `326e2035bbb9dd6b3d705f085c19d293da2e58b2998f3452b654c2d75d6d42f3`;
  source-aware proof
  `7c9317bce0cb53b5767eb63e053c4f0e94ab23b88292e17cb481a1cdba914585`;
  request
  `d186c1e5b96ebb91370a15155b5d6b8f4e355b04740db69bd4ccf60b1ed0b2f7`;
  authenticated source PDF
  `8d5975337f4ac88a475929ea6a436ec4a15d08715d5582bc0ba0eb3e07152c52`.
- Controlling receipt:
  `editorial/rethlas_receipts_20260825/p11_bj_radon_riesz_pn_counterexample_production_receipt_20260825.md`.
- Exact-live gate: run `20260825T051642Z_049da6197deb`, item
  `pi_062d99c623958fae25885125`, final `correct`, zero critical errors and
  zero gaps.  The extracted live statement SHA-256 is
  `049da6197deb627f55e5e469a246dce53154e121eb0a1b8206806ae8ec395518`;
  the exact live theorem-and-proof SHA-256 is
  `d6e40fa3adedaccecc6a3af1f7258ee29b803ac9443a430e234be2a9571c9aa1`.
  Both wrapper and child guards completed with return code zero.  Controlling
  live receipt:
  `editorial/rethlas_receipts_20260825/p11_bj_radon_riesz_pn_live_integration_receipt_20260825.md`.
- Rejection preservation: the first \(\mathbf P^2\) proof run returned
  `final/wrong`; its rejected proof SHA-256 is
  `54d3e6ef089fdea4194414628db7e9f3d247c16cf89070430eb69e5a60fafab8`
  and its artifacts remain quarantined.  The repaired \(\mathbf P^2\)
  baseline and the stronger \(\mathbf P^n\) packet are both preserved.
- Firewall: the generalized frozen run controls the source-aware mathematical
  packet, while the later run controls the adapted live theorem-and-proof
  bytes.  No publication, novelty, or priority claim is made.

## Chapter 55 toric zero-mass package

- Status: **VERIFIED** (24 August 2026).
- Book location: the integral/rational toric zero-mass numerical-dimension
  block in Chapter 55.
- Provenance: a book-level synthesis of Cao's Proposition 4.4, Guenancia's
  Theorem 1.13, and the toric character dictionary.  It is not a novelty or
  priority claim.
- Scope: smooth projective toric variety, invariant current, and big integral
  or rational toric class.  Irrational real classes are not covered.
- Live Chapter 55 SHA-256:
  `b2134d6b59f7687f8f5f296023a7d80703122210909032856b965f12f61619ab`.
- Target-statement SHA-256:
  `703e3b50120292333f6b00a3e18e887a2a67f2aa7d5dbaf5197c3f4e1a3296aa`.
- Cao-attested proof-context SHA-256:
  `f978d2ee49a3f90d29f010cdc750fe0c28370f9b4b63a9f96dce5b297423896d`.
- Receipt:
  `editorial/rethlas_receipts_20260824/ch55_toric_zero_mass_cao_attested_receipt.md`.
- Production run: `20260824T052605Z_703e3b501202`; proof item
  `pi_1f43447774c9ced4048c2efa`; `gpt-5.6-sol`, `xhigh`, final verdict
  `correct`, zero critical errors, zero gaps.
- Primary-source firewall: the archived Cao PDF places the required comparison
  in Proposition 4.4 on physical page 19.  The earlier run that demanded a
  nonexistent Proposition 4.3 is diagnostic only and is not a receipt.

## Chapter 69 toric numerical-dimension integration

- Status: **VERIFIED** (24 August 2026).
- Book location: `thm:verified-toric-dimension` and its adjacent proof in
  Chapter 69.
- Scope and provenance: exactly the same smooth-projective,
  invariant-current, integral/rational toric framework as the Chapter 55
  synthesis.  Chapter 69 delegates the analytic and toric inputs to Chapter
  55, but its own displayed statement and proof were separately gated.  No
  irrational-real extension and no novelty claim is made.
- Live Chapter 69 SHA-256:
  `39e5caa017d1181696a3a3757848980b989809b2b30aac598ebf7a6032f9be14`.
- Target-statement SHA-256:
  `d706dc98ccca14bb0fad879619de60e22f07c34a7333f5bbf54dc1d061df9700`.
- Source-aware composite proof-context SHA-256:
  `8aefa5096761f66d4b8f7bda26f0f5f037048e9832bdb03de7921e807aa5d618`.
- Production run: `20260824T070302Z_d706dc98ccca`; proof item
  `pi_bbf8518d7f87e9372b79f4ff`; `gpt-5.6-sol`, `xhigh`, final verdict
  `correct`, zero critical errors, zero gaps.
- Exact-current receipt:
  `editorial/rethlas_receipts_20260824/ch69_verified_toric_dimension_exact_current_receipt.md`,
  SHA-256
  `2c6b741ab8df23c9cecd8add300a6ab795fe90f12b0c46def9caaf9be2fe4c96`.

## Chapter 70 — generalized-Lelong separation

- Status: **VERIFIED FROZEN PACKET / INTEGRATED AFTER HOSTILE AUDIT**
  (24 August 2026).
- Book location: `thm:local-generalized-lelong-separation` and its adjacent
  proof in Chapter 70.
- Statement: for arbitrary psh germs at a smooth complex point, equality of
  generalized Lelong numbers against every tame psh weight forces pointwise
  equality of the BFJ valuative transforms on the normalized centered
  valuation space.  Primary-ideal analytic weights already suffice.
- Scope firewall: the conclusion concerns valuative transforms, not equality
  of the original germs, equality modulo bounded functions, or a singular or
  nonnormal ambient germ.
- Exact frozen statement SHA-256:
  `ef8316d19c121710280984d8954fefb9e9c14ce8737a4b9aef658c4c5120546e`.
- Exact frozen source-aware proof SHA-256:
  `57355a05bf4be050dfe54755eaf989ae3725782fc94b14dd9296b75e06e4dedd`.
- Production run: `20260824T140127Z_ef8316d19c12`; proof item
  `pi_3114f2ee2498f163b2c41e7c`; `gpt-5.6-sol`, `xhigh`, final verdict
  `correct`, zero critical errors, zero gaps.
- Independent hostile audit:
  `editorial/solver_dossiers_20260824/lelong_separation_hostile_audit.md`;
  it rechecked the primary-ideal generation, the one-Weil-input intersection
  domain, exact polarization, compactification, Hodge-index negativity, and
  passage from all finite traces to every normalized valuation.
- Verification record:
  `editorial/rethlas_receipts_20260824/ch70_lelong_separation_exact_current_receipt.md`.
  Despite that historical filename, the record controls the frozen exact
  statement and proof packet submitted before integration; it is not a
  post-integration byte-identity receipt for the live chapter.
- Provenance: a dated book-level derivation from BFJ's intersection theory
  and the Hodge index theorem.  No novelty or priority claim is made.

## Chapter 69 — analytic weighted-cross realization

- Status: **VERIFIED FROZEN PACKETS / INTEGRATED WITH AN UPSTAIRS FIREWALL**
  (25 August 2026).
- Book locations: `prop:verified-cross-compact-obstruction` and
  `prop:verified-cross-analytic-realization`, with the residual question in
  Chapter 72.
- Exact answer: a compact harmonic-tropicalization chart cannot map onto the
  unbounded full cross.  The proper tropicalization of
  `V((x-1)(y-1))^an` from a noncompact reduced boundaryless curve does realize
  the full cross and is exhausted by compact harmonic charts; the effective
  cycle `2[Y_h]+[Y_v]` has pushed weights `(2,2,1,1)`.
- Scope firewall: the two curvature currents are unequal upstairs and agree
  only after the tropicalization identifies distinct Gauss points.  The
  packet verifies the pushed defect, not an analytic Bedford--Taylor
  counterexample.
- Analytic run: `20260825T021353Z_058a4390b0fb`, seven proof items;
  statement SHA-256
  `058a4390b0fba4e83d462b9b125a623d304390bb0ac64341134b1a8b5896058f`;
  proof SHA-256
  `4a68b379e8d043b6a62293496af981fca77371575474a8af0040d7b6b70a56fc`.
- Compact-obstruction run: `20260825T024519Z_16376e0d52eb`; statement
  SHA-256
  `16376e0d52eb76320faeefef96201da0aabab36becf81c2cecde7ddd5a1931ee`;
  proof SHA-256
  `5f74d82c9ec0f75368ceecda14d6e597a0549a31a230a07c9dad31311cb3e3d3`.
- Both production runs used `gpt-5.6-sol`, `xhigh`, and returned final
  `correct`, zero critical errors, and zero gaps.

## Chapters 69 and 72 — four-punctured smooth-cross obstruction

- Status: **VERIFIED FROZEN PACKET / INTEGRATED AS A NARROW OBSTRUCTION**
  (25 August 2026).
- Book location: `prop:verified-four-punctured-cross-obstruction`, with its
  precise residual scope recorded under `prob:frontier-cross-fan-upstairs`.
- Exact answer: on
  `(P1_K \ {a,b,c,d})^an`, for punctures with pairwise distinct reductions,
  the natural full-cross potentials have equal CLD and delta curvatures
  `4 delta_q`.  A positive closed order-zero CLD current with visible ray
  weights `(wa,wb,wc,wd)` must nevertheless have all four weights equal:
  the third-unit refinement gives
  `(wa-wb,wc-wd,wa-wc)=(0,0,0)`.  The same obstruction applies to a positive
  closed delta-current whose smooth restriction has those visible weights.
- Scope firewall: the result excludes only this concrete four-punctured
  smooth-curve construction.  It neither classifies currents on arbitrary
  connected analytic curves nor decides the higher-dimensional or non-PL
  cases.  `P21.3` remains open and no inventory count changes.
- Exact frozen statement SHA-256:
  `ea6194f07e869610c427c326311d7a0bea38ca15e8c0050e396d3c9b5b92a596`.
- Exact frozen source-aware proof SHA-256:
  `2426acd5e1662ed5aad826597b389884ef925c42258538c86184ab7dd7817a11`.
- Guarded production run: `20260825T034743Z_ea6194f07e86`; proof item
  `pi_19c9aad210847a2875a0fe4a`; model `gpt-5.6-sol`, scrutiny `xhigh`, final
  verdict `correct`, zero critical errors, and zero gaps.
- Controlling receipt:
  `editorial/rethlas_receipts_20260825/p21_upstairs_cross_curve_obstruction_production_receipt_20260825.md`.
- Live-integration receipt:
  `editorial/rethlas_receipts_20260825/p21_upstairs_cross_curve_obstruction_live_integration_receipt_20260825.md`.
- Provenance: dated book-level consequence of the CLD and delta-form
  calculi; no novelty or priority claim is made.

## Chapters 66 and 72 — normalized hybrid endpoint counterexample

- Status: **EXACT LIVE THEOREM AND PROOF VERIFIED** (25 August 2026).
- Book location: `thm:hybrid-endpoint-continuity-counterexample`, with the
  source questions retained only as resolved history in Chapter 72.
- Exact answer: even on the smooth trivial polarized
  `P1_C x D*` family, a smooth semipositive metric can extend as an
  everywhere-finite psh model metric, have the continuous product
  Fubini--Study non-Archimedean endpoint, and have zero relative supremum on
  every complex fibre and on the non-Archimedean fibre, while its canonical
  hybrid psh extension is discontinuous.
- Exact live statement SHA-256:
  `d77f7f93aeb01c9b29d0ffa170ea5301811f685e2b95f6d54b4151a9a0aad6ff`.
- Exact live theorem-and-proof SHA-256:
  `992a686618355605e4f889564c402f5b2c6ff18db70762daed2dbcf4d09fdbad`.
- Production run: `20260825T043840Z_d77f7f93aeb0`; proof item
  `pi_b7f015a6ad5570f431769a71`; model `gpt-5.6-sol`, scrutiny `xhigh`,
  final verdict `correct`, zero critical errors and zero gaps.
- The earlier normalized frozen mathematical packet remains preserved under
  run `20260825T035945Z_070e264c3ef1`; the later run is the exact-current
  byte-identity gate.
- Scope firewall: this closes the Favre--Pille-Schneider endpoint question
  and its zero-supremum strengthening, but not Pille-Schneider Question 4.9
  over general integral Banach rings.  No novelty or priority claim is made.
- Controlling receipt:
  `editorial/rethlas_receipts_20260825/p18_favre_hybrid_extension_normalized_counterexample_live_integration_receipt_20260825.md`.

## Chapter 69 — complete-intersection slice of positive PL currents

- Status: **VERIFIED FROZEN STANDALONE PROPOSITION / INTEGRATED**
  (25 August 2026).
- Book location: `prop:verified-lci-current-slice`.
- Scope: good separated boundaryless strict pure-dimensional analytic space;
  a regular sequence of length `n-1`; pure relative dimension one; tests are
  restrictions of nonnegative smooth compactly supported ambient functions.
  A tightly supported ambient cutoff detects a discrete curve-current atom.
- Scope firewall: this does not extend arbitrary smooth functions on the
  curve, provide a residual-degree formula, or prove the global
  current-positivity converse.  A separate rig-smooth global candidate was
  rejected and remains preserved as a negative verification record.
- Production run: `20260825T023505Z_66547f68ec32`; proof item
  `pi_d75152188902c18ea84618d2`; statement SHA-256
  `66547f68ec325107732ee307b3e728480b5ffc9c8f08537478e75984eb89f202`;
  proof SHA-256
  `d62ff2285ed7a7e435ae78477075482bf676bf36360a1e4c46babfdbfbad281b`.
- Model and verdict: `gpt-5.6-sol`, `xhigh`, final `correct`, zero critical
  errors, and zero gaps.

## Chapters 15, 70, and 72 — nodal local-envelope counterexample

- Status: **VERIFIED FROZEN EXACT BLOCK / INTEGRATED BYTE-FOR-BYTE**
  (25 August 2026).
- Book location: `prop:ch15-nodal-local-envelope`, with its consequences in
  Chapters 70 and 72.
- Exact answer: on the reduced strict affinoid curve
  `M(K<x,y>/(xy))`, a continuous finite obstacle has raw
  FS/semipositive-real-PL envelope equal to zero on one punctured branch and
  a negative constant on the other branch and at the node.  Its usc
  regularization changes the nodal value, is discontinuous, and violates
  the affinoid Shilov-boundary maximum principle.  It is therefore neither
  classically psh nor CLD-v2 psh.
- Exact frozen statement SHA-256:
  `10ac70696f69b1ed18ae1522c0b065fe9240d8f921b9db258201c9e8a7b509e1`.
- Exact frozen proof SHA-256:
  `21fc22e5b1f3b3084f29df412a57485131e46ca160cf168db18da8a3e2559fc7`.
- Production run: `20260825T094005Z_10ac70696f69`; proof item
  `pi_31f95353b7e94f3cb98b09b6`; model `gpt-5.6-sol`, scrutiny `xhigh`,
  final verdict `correct`, zero critical errors and zero gaps.
- Exact-live gate: the proposition and proof extracted from Chapter 15
  compare byte-for-byte with the two frozen files; the extraction commands
  and hashes are recorded in the controlling receipt.
- Scope firewall: the construction disproves the three unconditional
  universal assertions.  It does not solve the three classification targets,
  beginning with the normal or analytically unibranch case; those remain
  open.  No novelty or priority claim is made.
- Controlling receipt:
  `editorial/rethlas_receipts_20260825/p03_nodal_local_envelope_counterexample_live_integration_receipt_20260825.md`.

## Chapters 19 and 72 — canonical cubical delta-metricity reduction

- Status: **VERIFIED FROZEN EXACT BLOCK / INTEGRATED BYTE-FOR-BYTE**
  (25 August 2026).
- Book location: `thm:p09p2-reduction`; the residual problem displayed at
  that date has since been retired by the next verified result.
- Exact result: cubical metrics on `Pic^0(A)` are ordinary GK
  delta-metrics; the directly induced symmetric/antisymmetric decomposition
  gives an isometric square splitting and an equivalence of delta-metricity;
  on a fixed abelian variety, the universal problem is equivalent to the
  ample symmetric case.
- Exact frozen statement SHA-256:
  `b37e13478cc753ff1ba131540dda18ab93f421b047e04cb9b4673370ce466655`.
- Exact frozen proof SHA-256:
  `3967095b314a63a2dd805a5205fbe8904e998b5284dfe350a4fa6ed6f755a919`.
- Production run: `20260825T145229Z_b37e13478cc7`; proof item
  `pi_10f6228b6e69e780dad8b17b`; model `gpt-5.6-sol`, scrutiny `xhigh`,
  final verdict `correct`, zero critical errors and zero gaps.
- Historical scope firewall: the theorem assumes the Gubler--Künnemann
  field category and did not by itself decide ample symmetric cubical
  metrics in non-isotrivial mixed reduction.  The later product--Gauss
  theorem below closes exactly that range.  No novelty or priority claim is
  made.
- Controlling receipt:
  `editorial/rethlas_receipts_20260825/p09p2_cubical_delta_reduction_live_integration_receipt_20260825.md`.

## Chapters 19 and 72 — product--Gauss criterion and retirement of P09.2

- Status: **VERIFIED FROZEN EXACT BLOCK / INTEGRATED BYTE-FOR-BYTE**
  (26 August 2026).
- Book location: `thm:p09p2-product-gauss-candidate`; Chapter 72 records the
  source question as resolved rather than displaying a problem environment.
- Exact result: for a split torus action and an equivariant locally integral
  PL map `h`, a weight `F(h)` with nondegenerate quadratic Hessian is an
  ordinary Gubler--Künnemann delta-weight if and only if every coordinate of
  `h` is CLD-smooth.  For split Raynaud uniformization, an ample cubical
  metric is ordinary delta if and only if the residual Raynaud extension is
  isotrivial.  Consequently no ample cubical metric in non-isotrivial mixed
  reduction is ordinary delta, and P09.2 is retired negatively.
- Exact frozen statement SHA-256:
  `b68659fba1be78b30345c112c637d38f41372dc70526fef8ecad6a450f7cbf47`.
- Exact frozen proof SHA-256:
  `3bfc656409c96a2be52161798efffe726657a3e0b2d2831a5f25a795e8c4d262`.
- Production run: `20260826T055627Z_b68659fba1be`; proof item
  `pi_75c74fac9a98efc3719b9773`; model `gpt-5.6-sol`, scrutiny `xhigh`,
  final verdict `correct`, zero critical errors and zero gaps.
- Independent gates: primary-source, novelty-scope, proof-architecture, and
  hostile audits all passed.  The final quantifier repair defines relative
  Gauss points for every real torus weight and invokes constant `K`-section
  density only at value-group-rational weights.
- Scope firewall: the analytic-local invariance argument concerns analytic
  opens of algebraic analytifications and algebraic line bundles; the
  product criterion requires a nondegenerate quadratic Hessian; the Raynaud
  application assumes the stated algebraically closed complete
  nontrivially valued field and an ample line bundle.  No broader weakly
  smooth, arbitrary analytic, nonample, novelty, or priority claim is made.
- Controlling receipt:
  `editorial/rethlas_receipts_20260826/p09p2_product_gauss_live_integration_receipt_20260826.md`.

## Chapter 16 — direct trivially valued curve classifications

- Status: **EXACT LIVE-READY PACKET VERIFIED / INTEGRATED** (29 August
  2026).
- Book locations: `lem:p213-triv-interval-current`,
  `prop:p213-triv-abstract-cross-counterexample`,
  `prop:p213-triv-p1-current-rigidity`,
  `prop:p213-triv-algebraic-curve-current-rigidity`, and
  `prop:p213-triv-four-puncture-no-go`.
- Exact result: positive closed bidegree-`(0,0)` currents are nonnegative
  multiples of the integration current on the two boundaryless CLD interval
  structures, every connected analytic open of the trivially valued
  projective line, every smooth connected projective algebraic curve over an
  algebraically closed trivially valued field, and every connected Zariski
  open in such a curve.  The analytic classifications imply the full CLD
  Bedford--Taylor predicate.  The same packet gives the positive closed
  weighted-cross counterexample in the abstract tropical category and proves
  that a third analytic unit forbids its unequal weights on the natural
  four-punctured algebraic cross.
- Exact live-ready statement SHA-256:
  `cd1032050a8ce5d3617fbf1952b411a1fe638db2f658aec9b7e0810e3b32d77b`.
- Exact live-ready proof SHA-256:
  `37ed90b0b7f079b0f34d140a79c61c510b1206da6629953696d4a2d98c8a3ee8`.
- Independent exact-byte audit SHA-256:
  `0d1c7a9a5aef9ee2c2daf4bfcb0778ec2cde1e5067b907da283edf66a0a246ea`.
- Production item: `pi_ed915de7970791904bc0ec6e`; model
  `gpt-5.6-sol`, scrutiny `xhigh`, final verdict `correct`, zero critical
  errors, and zero gaps.  The archived proof digest equals the exact proof
  hash.
- Scope firewall: this direct packet does not classify every singular,
  nonnormal, or nonalgebraizable trivially valued analytic curve.  By itself
  it narrows but does not retire the dimension-one residual of P21.3.  No
  novelty or priority claim is made.
- Controlling receipt:
  `editorial/rethlas_packets_20260829/p213_trivially_valued_curve_live_ready_20260829/p213_trivially_valued_curve_live_ready_rethlas_receipt_20260829.md`.

## Chapter 16 — arbitrary-valued normal analytic curves

- Status: **EXACT FROZEN PACKET VERIFIED / INTEGRATED BYTE-FOR-BYTE**
  (29 August 2026).
- Book locations: `lem:p213-variation-graph-source-cutoff`,
  `lem:p213-euclidean-one-dimensional-current-revised`, and
  `prop:p213-normal-curve-arbitrary-valuation-current-revised`.
- Exact result: on a connected good separated normal boundaryless pure
  analytic curve over any complete non-Archimedean field, possibly trivially
  valued, every positive closed ordinary CLD current of bidegree `(0,0)` is
  `c delta_Y`, with `c>=0`.  No strictness or smoothness hypothesis is used.
  Every such current has the full Bedford--Taylor property of CLD Definition
  8.6.2.
- Exact statement SHA-256:
  `339f8cb085fd6a7ce4d57d6163cfeafdacfb2ad01397d77f39c6f63328178cb7`.
- Exact proof SHA-256:
  `d6d02762690b9eeed6e025a3f5aa200d19994859ed02b27050da22e03da57660`.
- Independent hostile-audit SHA-256:
  `534154de06a9c7c63d5a060c4feac5d47a274af168177a305f64972483134c41`;
  verdict PASS, zero critical errors and zero gaps.
- Production item: `pi_d9543424f0492e1412e0d203`; model
  `gpt-5.6-sol`, scrutiny `xhigh`, final verdict `correct`, zero critical
  errors, and zero gaps.  The returned proof digest equals the exact proof
  hash.  The request/response/header hashes are
  `d9a4ad02796009280917f1c0d1de216503c5fdcd25aef28c073570e26baebf1f`,
  `93c586e3de8884e30e7e7c320e6364cb2bb9c6c35d38593361e34c9a85f06860`,
  and
  `0f0bcd114f923264cbcfb398d5d8fc10b556eda20373330912c3ef8fe3eca217`.
- Noncontrolling provenance: the first revision's calibration error and the
  second revision's unrelated smooth-locus gap remain preserved as rejected
  stages; neither is cited as verification of the live theorem.
- Controlling receipt:
  `editorial/rethlas_packets_20260829/p213_variation_graph_arbitrary_curve_20260829/p213_variation_graph_arbitrary_curve_revised3_rethlas_receipt_20260829.md`.

## Chapter 16 — arbitrary-valued componentwise analytic curves

- Status: **DEPENDENCY-CLOSED EXACT PACKET VERIFIED / INTEGRATED**
  (29 August 2026).
- Book location: `prop:p213-componentwise-arbitrary-valuation`, including
  items `itm:p213-componentwise-av:calculus`,
  `itm:p213-componentwise-av:integration`,
  `itm:p213-componentwise-av:classification`, and
  `itm:p213-componentwise-av:bedford-taylor`.
- Exact result: for every good separated strict boundaryless pure analytic
  curve over either valuation regime, with reducible and nonreduced spaces
  allowed and with no smoothness assumption on component normalizations,
  nilreduction identifies the ordinary CLD calculus and current topology;
  generic multiplicities remain in the fundamental integration current;
  every positive closed `(0,0)` current is the unique locally finite
  nonnegative sum of normalized reduced-component currents; and the
  continuous-pair Bedford--Taylor property holds.
- Principal statement/proof SHA-256:
  `91ce52597273f7c8479efd755925d70c51bcc067ea68e72dcf43a1cdf259bff0`
  and
  `098995604f7c55ce0341eba984c7bb23a09b6be5d148d14169d1b7f8f7386cd1`.
- Exact dependency statement/proof pairs, in materialization order:
  `469024d04e8eb5e08900b9caea6480057398c743ca0b46076b524f2109cf80ac`
  / `661100a4b25e82297c5b2b2712775e9c9501c337d619a64280f2d49922a4bcc2`,
  `ffaa0610214068382fd20e584bb48e77e86f8bbc2f4ea0910eb7d091ba843a6a`
  / `789acb082e15ffe8e7f31327ae5e331b06654c42e21ee2ed83c4ff404e32bc66`,
  and
  `339f8cb085fd6a7ce4d57d6163cfeafdacfb2ad01397d77f39c6f63328178cb7`
  / `d6d02762690b9eeed6e025a3f5aa200d19994859ed02b27050da22e03da57660`.
- Materialized statement/proof SHA-256:
  `d1ad274eb03a9a51db54427c6cef1f8ff7121a987e70caecd6453f868598d1f6`
  and
  `cd7f2e4cc32ca90c6f866f8190da57ad885fd7effa0bed3248f880d09bbf209f`.
- Independent binding audit SHA-256:
  `4a347171150e52a88223415cc8cfff1bb38baeabeb6eb0ce84be29ba5be595c7`;
  its exact 24-page harness compiled cleanly.
- Production item: `pi_1ca3e6d14c7e8596372d863d`; model
  `gpt-5.6-sol`, scrutiny `xhigh`, final verdict `correct`, zero critical
  errors, and zero gaps.  The returned proof digest equals the materialized
  proof hash.  The request/response/header hashes are
  `6920d2582649e1fcedcc3a729242e1ca02fded05502cc878a36f4e8652929365`,
  `87507beab77d5917edc8cd8d1abcf466965222a2c973e6cded58beabd2057a8a`,
  and
  `0733b7bff2ffbe09bba821804d7b4bcbf50842031743a096f5db79c9dc5cdde6`.
- Scope and inventory consequence: the reducible/nonreduced theorem asserts
  only the continuous-pair predicate.  It retires every one-dimensional case
  inside P21.3's ambient hypotheses.  P21.3 remains one T2 atom only in
  dimension at least two, so the inventory remains 15 environments and 54
  atoms with tier totals `(0,6,14,17,17)`.
- Controlling receipt:
  `editorial/rethlas_packets_20260829/p213_componentwise_arbitrary_valuation_live_ready_20260829/p213_componentwise_arbitrary_valuation_revised3_rethlas_receipt_20260829.md`.

## Chapter 14 — CLD support exponent and scalar extension

- Status: **EXACT FROZEN PACKET VERIFIED / DIRECTLY INTEGRATED** (29 August
  2026).
- Book locations: `thm:ch14-cld-support-corrected-packet`,
  `rem:ch14-cld-support-corrected-index`, and
  `prop:ch14-cld-support-printed-exponent-counterexample`.
- Exact result: the nontrivially valued support theorem is reconstructed by
  proper tropical pushforward and Lagerberg's Euclidean support theorem.  If
  a trivially valued pure `n`-fold carries a product of `q` continuous-dpsh
  curvature currents, scalar extension gives vanishing on tropically
  `H^(n-q)`-negligible sets.  The `H^q` exponent printed in CLD Corollary
  16.8.6 is an index error; on the trivially valued analytic torus,
  `d'd'' max(0,log|z|)` is the unit Dirac mass at the unit Gauss point and
  disproves the printed exponent when `n=q=1`.
- Exact frozen statement SHA-256:
  `2b291fc55872ab32d40fa3a67e9a9308fc12ac9726113b48950d0a9e50cfd8c1`.
- Exact frozen proof SHA-256:
  `9f21f7ece49c761d3f19c07acd8b56e48e9939be493e0bbbd39c0a4d3176e668`.
- Independent hostile-audit SHA-256:
  `62520258d3a5a4d6e73a3d7f9d0dfd8679586ec718d03acf4f32bebcabe7adaa`;
  verdict PASS, zero critical errors, zero gaps, zero source mismatches, and
  zero degree/index collisions.
- Production item: `pi_d8921af65dfc0c98f29a5fb7`; model
  `gpt-5.6-sol`, scrutiny `xhigh`, final verdict `correct`, zero critical
  errors, and zero gaps.  The returned proof digest equals the exact proof
  hash.  The exact packet files are the live chapter inputs; their archival
  header comments remain unchanged solely to preserve byte identity.
- Scope firewall: the trivially valued clause concerns Bedford--Taylor
  products, not arbitrary positive closed currents.  The exponent diagnosis
  is a correction to the printed source, not a claim that the source theorem
  or its scalar-extension method is new.
- Controlling receipt:
  `editorial/rethlas_packets_20260829/ch14_cld_support_correction_packet_20260829/ch14_cld_support_correction_rethlas_receipt_20260829.md`.

## Darvas--Xia trace-source correction (not a receipt)

- Status: **SOURCE IMPORT / HISTORICAL RECEIPT SUPERSEDED** (23 August
  2026).
- Source boundary: the complete supplied trace chapter, in particular its
  trace-uniqueness and trace-comparison propositions, proves that every trace
  is \(\mathcal I\)-good, any two traces are \(P\)-equivalent, and
  \(\varphi\preceq_{\mathcal I}\psi\) implies
  \(\operatorname{Tr}_Y(\varphi)\preceq_P
  \operatorname{Tr}_Y(\psi)\).  Thus the sourced map is
  \(D_Y/{\sim_{\mathcal I}}\to
  \operatorname{QPSH}(\widetilde Y)/{\sim_P}\).
- Book locations: Chapters 51, 54, 67, and 69, together with Appendix L.
- Audit consequence: R3-19 used an incomplete packet and cannot be cited as a
  verification record for the current \(P\)-valued formulation.  The
  corrected factorization is a reconstruction of the sourced theorem, not a
  new result.  The split product calculation had an R2 audit only at the
  weaker \(\mathcal I\)-level; its present output \(P\)-class is obtained by
  applying the sourced uniqueness theorem.  No production receipt is claimed
  for the post-correction text.
