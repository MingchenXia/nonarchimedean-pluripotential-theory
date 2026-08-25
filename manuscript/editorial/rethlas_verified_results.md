# Rethlas verification receipts

This ledger records the production receipts that control mathematical
promotion or exact-current integration during the present revision.  It
includes book-local results and separately identified source syntheses; a
receipt does not by itself assert novelty, publication, or priority.  A
`VERIFIED` entry means that the exact statement and proof
were checked by the production Rethlas verifier with `gpt-5.6-sol` at `xhigh`
effort, after source and domain hypotheses were made explicit.  Later edits to
a statement or proof invalidate its receipt until a fresh audit is recorded.

## Current release boundary (24 August 2026)

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
exact current release snapshot has passed and is recorded in
`output/BUILD_AND_AUDIT_SUMMARY.md`; it does not enlarge the mathematical
scope of any receipt.

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
  at most one.  It does not settle arbitrary residual dimension, where the
  nef cone need not be a single rational half-space.
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
  made.

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

## Chapter 16 — first-stage CLD collapse in two polyhedral settings

- Status: **VERIFIED FROZEN PACKET / INTEGRATED** (25 August 2026).
- Book locations: `prop:ch16-collapse-tropical-toric` and
  `thm:ch16-collapse-finite-tropical-curves`.
- Scope: tropical toric partial compactifications with their standard
  Lagerberg smooth structure; and finite-valence boundaryless
  one-dimensional affine tropical spaces locally realized as balanced
  complexes with ambient-induced smooth structure.
- Exact conclusion: the toric psh, CLD psh, and first-stage CLD psh sheaves
  coincide in the toric setting; every psh curve germ has a decreasing
  smooth-psh approximation on one fixed neighbourhood in the curve setting.
- Scope firewall: no tropical-boundary or infinite-star curve result and no
  arbitrary higher-dimensional balanced-space collapse is inferred.
- Production run: `20260825T024707Z_d1b8d7eaf79e`; proof item
  `pi_ccfb83de7a7be82ef602cd72`; statement SHA-256
  `d1b8d7eaf79e155ecf7b347e4fcc1717c72d5a8090e346b2cb2fc9c9a0996e63`;
  proof SHA-256
  `316a774fbb4eda54150b63cae0c9f23a1edab17a75b89beeee6d56d402f8c4a0`.
- Model and verdict: `gpt-5.6-sol`, `xhigh`, final `correct`, zero critical
  errors, and zero gaps.  The preserved first round returned final `wrong`
  with two gaps; the controlling round supplies the omitted interior-edge
  regularization and sheaf-local junction argument.

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
