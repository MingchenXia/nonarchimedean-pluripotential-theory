# P21.3 canonical-collar live-integration checklist

Date of read-only audit: 28 August 2026

Audited repository: `/private/tmp/nappt_p071_20260827`
Audited HEAD: `0c0d070d97fa0016195f307d6a55f702a134ccc0`

This is an integration checklist, not a mathematical receipt.  No live,
frozen, or previously verified file was changed in preparing it.  All line
numbers below refer to the audited source state and should be matched by text
anchors if another edit changes the numbering.

## 1. Release gates and authoritative count

The exact four-file reduced live materialization has now received its final
production Rethlas PASS.  Integration is nevertheless still blocked on the
fresh arbitrary-field nonreduced live addendum described in section 2, so
that replacing the old six-file dependency chain does not create an
undefined reference or regress an already integrated theorem.  The exact
reduced live mathematical files and hashes are:

| file | SHA-256 |
|---|---|
| `p21p3_curve_rigidity_virtual_annulus_bridge_statement_live_20260828.tex` | `f3202ef13495aad790ee2b1ff057a89b34e76eff15761c33c88e7b809c3e1033` |
| `p21p3_curve_rigidity_virtual_annulus_bridge_proof_live_20260828.tex` | `ff8225ed6206f97e628504ab5b255c58a1a0de4fda13962e1ab09092fe2be7d5` |
| `p21p3_curve_rigidity_arbitrary_field_reduced_statement_live_20260828.tex` | `c9f27245f5608b772385167c84bfe9e836fc9f4b164477a578b6c26712e35b21` |
| `p21p3_curve_rigidity_arbitrary_field_reduced_proof_live_20260828.tex` | `01ab07fdacedfe95e1d764656a071a88395f5d0766115fd0a67164e3162410af` |

The controlling exact-live request is
`p21p3_curve_rigidity_arbitrary_field_live_run_20260828/request.json`, SHA-256
`28c2c69f5adc388a838365726ce83f95f557aea52108d4408914de9659ab41b6`.
It materializes the bridge statement before the reduced statement and the
bridge proof before the reduced proof.  The extracted statement and proof
payload hashes are, respectively,
`f2a1c1b9f2a3d9f60422fc1697d31c5265704a73f0c27f180adc36e65d5bbda6`
and
`745c842490484fdcba1eebe0bee83cf050b3c8050fafdf751a973615414ce4fe`.
The run is `20260828T042906Z_f2a1c1b9f2a3`; it used `gpt-5.6-sol` at
`xhigh`, returned HTTP 200 and verdict `correct`, and persisted 17 sequential
statement records, 19 primary-source records, zero failed checks, zero
critical errors, and zero gaps.  The response and safe-header hashes are
`1b305d4e21fc1280efe1787468b7c2101a7d0de964ce54d70cad92921df4bd3c`
and
`4cbca05e289105e26cbeaa051ab3f71897381033d013686ad28ec8e2971f8947`.
The exact-live Rethlas receipt is
`p21p3_curve_rigidity_arbitrary_field_live_rethlas_receipt_20260828.md`,
SHA-256
`afe4e1f458d3725fa1c4fecb3e682d0b53bc86abf1166b7b4817028d9fce7fdd`.

The standalone four-file driver compiled cleanly to 15 pages; the driver,
PDF, and final-log hashes are
`1f5810788fffe6fd2c260ab99883f6fe28e888dd4ceece6304ca8f0bb6d48c0b`,
`12191b00d4676b77f8f60f921af71245f6454b125f8fc065b4c93f1af750c37c`,
and
`2a1ace8d69593cfb94962cdb840dc104ef7adf2b1c301c4f2902acda91c31eb6`.
The only grep occurrence of `Rerun` is package metadata for
`rerunfilecheck`.

The bridge pair is byte-identical to the separately verified
canonical-collar pair.  Its controlling production data are:

- service run `20260828T034929Z_f3202ef13495`;
- model `gpt-5.6-sol`, effort `xhigh`, HTTP 200, verdict `correct`;
- 11 sequential-statement and 12 primary-source records, zero critical
  errors, zero gaps, and zero failed checks;
- request `03a2656fa8f852b1483a6ee6237ac9ba5cea65b1dfbc37d48e5b10321b33e02c`,
  response `7b39c374e521d4c72b168439a3d43a9c5d2910c4bb52a7e1ab6bdba2a0964a54`,
  and safe headers
  `d99bc6ec5abc331c3b9cc82e942aaf7914091507e53811d1f6adf7f0ad26a6b8`.

The earlier materialized arbitrary-field reduced packet also passed, but it
does not by itself control the label/status-adapted live bytes.  Its
controlling data, to be retained as a dependency receipt, are:

- combined statement
  `c7b249ecc02e5459ca9ddd78f2746aac273ce9088489fd6c12ee16f4715524af`;
- combined proof
  `63affb48756ec64170b2fef92b9fa347b952aab07278901e37e804efcb15bc0d`;
- service run `20260828T040717Z_c7b249ecc02e`, model `gpt-5.6-sol`, effort
  `xhigh`, HTTP 200, verdict `correct`;
- 17 sequential-statement and 19 primary-source records, zero critical
  errors, zero gaps, and zero failed checks;
- request `68a8c99cf8dd78db6c3a6e74a22bf71936876f9345b15d8aaf911777e8aa16ce`,
  response `1b305d4e21fc1280efe1787468b7c2101a7d0de964ce54d70cad92921df4bd3c`,
  and safe headers
  `cd7a3cbb0e2e2358b694fbf25929316f3ed0a5ad09b00a564e9bb2285ecf30bd`.

The authoritative frontier count in the current Chapter 72, atomic
inventory, revision log, and verified-results ledger is **16 formal problem
environments and 55 active atoms**, with tier counts `(0,7,14,17,17)`.
P21.3 remains one T2 atom after this scope reduction.  The `16/56` text in
the staging residual, staging audit, and older integration map is stale and
must be changed to `16/55`; it must not be copied into the book or ledgers.

## 2. Nonreduced integration is an atomic dependency

The old 27 August nonreduced statement/proof cannot coexist unchanged with
the new arbitrary-field reduced pair.  After the old reduced input is
removed, the old nonreduced proof has two unresolved dependencies:

- `eq:p21p3-fundamental-cycle`, replaced in the new reduced proof by
  `eq:p21p3-gfc-fundamental-cycle`;
- `lem:p21p3-type-one-zero-atom`, replaced by the genuinely different-scope
  rigid-point lemma `lem:p21p3-gfc-rigid-zero-atom`.

It also calls a continuous-pair conclusion the literal condition of CLD
Definition 8.6.2 and uses algebraically-closed/type-1 language that the new
scope firewall deliberately corrects.  Therefore do **not** leave these two
old inputs after installing the new reduced files:

```tex
\input{editorial/rethlas_packets_20260827/p21p3_curve_rigidity_nonreduced_addendum_statement_20260827.tex}
\input{editorial/rethlas_packets_20260827/p21p3_curve_rigidity_nonreduced_addendum_proof_20260827.tex}
```

They must be replaced by a fresh arbitrary-field, live-adapted nonreduced
statement/proof that has itself passed exact production Rethlas.  The current
`p21p3_curve_rigidity_nonreduced_arbitrary_field_conditional_*_20260828.tex`
files are conditional source material, not live inputs.  The fresh live
adaptation should preserve the established public labels where possible:

| conditional label | live public label |
|---|---|
| `prop:p21p3-gfnr-curve-rigidity` | `prop:p21p3-curve-rigidity-nonreduced` |
| `itm:p21p3-gfnr:calculus` | `itm:p21p3-nr:calculus` |
| `itm:p21p3-gfnr:integration` | `itm:p21p3-nr:integration` |
| `itm:p21p3-gfnr:classification` | `itm:p21p3-nr:classification` |
| `itm:p21p3-gfnr:bedford-taylor` | `itm:p21p3-nr:bedford-taylor` |
| every `eq:p21p3-gfnr-*` | corresponding `eq:p21p3-nr-*` |
| `rem:p21p3-gfnr-scope` | `rem:p21p3-nr-scope` |
| `rem:p21p3-gfnr-double-line` | `rem:p21p3-nr-double-line` |
| `prop:p21p3-gfc-curve-rigidity` | `prop:p21p3-curve-rigidity` |
| `itm:p21p3-gfc-curve:classification` | `itm:p21p3-curve:classification` |

The fresh proof cites `Tate71Rigid`; the main bibliography must contain that
entry before the full build.  Until this nonreduced gate passes, do not claim
the arbitrary-field theorem for nilpotent thickenings, and retain nonreduced
curves in the residual one-dimensional scope.  Once it passes, the natural
six-file input order is:

1. bridge statement;
2. bridge proof;
3. arbitrary-field reduced statement;
4. arbitrary-field reduced proof;
5. fresh arbitrary-field nonreduced statement;
6. fresh arbitrary-field nonreduced proof.

This order keeps every proof next to its statement and makes the reduced
theorem available before the nonreduced addendum invokes it.

## 3. Labels, references, and forbidden simultaneous inputs

The four exact-live files contain 61 declarations and 61 distinct labels.
Their only intentional collisions with the currently compiled source are the
seven public labels in the old 20260826 reduced statement:

```text
prop:p21p3-curve-rigidity
itm:p21p3-curve:classification
itm:p21p3-curve:bedford-taylor
eq:p21p3-curve-classification
eq:p21p3-curve-equal-curvature
eq:p21p3-curve-bt-conclusion
rem:p21p3-curve-scope
```

Those collisions disappear only if both old 20260826 reduced inputs are
removed.  Never input an archived combined/candidate packet in addition to
the four split live files: the `gf` and `gfc` supporting labels are repeated
across those archival packets by design.

Keep these new supporting labels unchanged:

```text
lem:p21p3-gf-legal-source-localization
prop:p21p3-gf-virtual-annulus-bridge
lem:p21p3-gfc-rigid-zero-atom
prop:p21p3-gfc-smooth-rigidity
```

Do not alias the old type-1 lemma to the rigid-point lemma.  A type-1 point
over an arbitrary ground field need not be rigid; the conductor argument
uses strictness to prove that the actual conductor points are rigid.

The staging residual contains the already-live problem label
`prob:frontier-cross-fan-upstairs`.  Replace the existing Chapter 72 block;
do not `\input` the staging residual beside it.  Preserve every equation
reference as `\eqref` and every prose reference as `\cref`/`\Cref`; introduce
no raw `\ref`, `\pageref`, or `\autoref`.

The rejected/stale bridge artifacts remain provenance only.  In particular,
do not input or cite as controlling bytes the `c5a643/292bb`,
`0315d3/c903cf`, or `07460b/ee7a14` pairs.  The older bridge receipt in
`rethlas_receipts_20260828/p21p3_virtual_annulus_bridge_production_receipt_20260828.md`
controls `c833fc37/e07b0647`, not the final canonical-collar repair; the
controlling bridge receipt is the `f3202ef1/ff8225ed` receipt in
`rethlas_packets_20260827`.

## 4. `ch16_bedford_taylor.tex`

Audited hash:
`53a570fa36a3afc2fcec5ccf7a44de5cd830f859bb475e47865ecaf333fc1a05`.

### 4.1 Imported-input ledger (current lines 138--167)

Replace item 4 at lines 158--162.  Name all of the actual imported
ingredients: ordinary CLD moment localization and proper tropical
pushforward; the Gubler--Jell--Rabinoff finite-fibre, calibration, and residue
lifting inputs; Ducros's arbitrary-field residual-curve, virtual-disc, and
virtual-annulus structure; and the fundamental-cycle/reduction inputs used by
the verified nonreduced addendum.  Cite
`CLD25,GJR26,Ducros24CurveStructure` (and `Tate71Rigid` at the exact
noetherian/strict-affinoid steps in the nonreduced proof), rather than leaving
the old summary as “Temkin reduction of germs.”

### 4.2 Continuous versus literal CLD terminology (current lines 1012--1060)

At `def:ch16-bt-current`, call the displayed predicate the **continuous
Bedford--Taylor property/current** because it quantifies over continuous psh
pairs.  Immediately after the definition, state once that the rest of this
chapter abbreviates this to “Bedford--Taylor” under its standing
continuous-potential convention.  State separately that literal CLD
Definition 8.6.2 may quantify over discontinuous psh functions and is not
proved by the curve theorem.  Later short uses in the chapter may remain
after this firewall, but the historical/source paragraph must repeat the
scope.

### 4.3 Dimension-one subsection (current lines 1158--1177)

Rewrite the roadmap at lines 1161--1172 with the exact scope and proof
architecture:

- arbitrary complete nontrivially valued `K`;
- good, separated, strict, reduced, pure one-dimensional, boundaryless `X`;
- rig-smooth normalization of each irreducible component;
- legal analytic-moment localization, finite virtual-annulus source
  separation, divisor balancing over the actual residue field, and the
  rigid-point radial estimate;
- first prove the connected rig-smooth classification, then pass through
  finite component normalizations, and only after that apply reduction to a
  nilpotent thickening.

Replace “type-1 zero-atom estimate” by “rigid-point zero-atom estimate.”  Add
index entries for virtual annuli, source-separated tropicalization, and
positive closed currents on analytic curves.  Before the first exact input,
add the reader-facing convention that `\operatorname{Rat}(C)` denotes the
function field of a residual curve `C`; the verified bridge uses this notation
without defining it in rendered prose.

Remove the four old inputs at lines 1174--1177.  After all exact gates pass,
install the six inputs in the order listed in section 2.  Do not edit their
verified bytes merely to remove non-rendered “candidate” comments.

### 4.4 Transition prose and examples

Use the staged exposition as prose to be adapted, not as an extra input file.
Recommended rendered order inside `sec:ch16-bt-curves`:

1. a short pre-bridge explanation of target-ray/source-branch ambiguity and
   why a smooth plateau is `\Phi\circ H_{\mathrm{trop}}`, not an analytic
   moment coordinate;
2. exact bridge statement and proof;
3. the ordinary-annulus and higher-degree residual-branch examples;
4. a short local-flux-to-global-current transition;
5. exact reduced statement and proof;
6. the reducible-node example;
7. exact fresh nonreduced statement and proof.

When adapting
`p21p3_canonical_collar_transition_staging_20260828.tex`:

- remove its staging/conditional comments and the sentence “Assume for this
  paragraph ...” after the exact live PASS;
- do not redeclare staging duplicates of the verified equations.  Cite
  `eq:p21p3-gf-source-cutoff-factorization`,
  `eq:p21p3-gf-canonical-full-source-collar`, and
  `eq:p21p3-gf-source-separated-ray-preimage` instead;
- change `eq:p21p3-gfc-curve-classification` to
  `eq:p21p3-curve-classification` and
  `prop:p21p3-gfc-curve-rigidity` to
  `prop:p21p3-curve-rigidity`;
- keep `prop:p21p3-gfc-smooth-rigidity` and
  `lem:p21p3-gfc-rigid-zero-atom` unchanged;
- describe type-1/type-4 endpoints through the exact tropical-dimension-zero
  test-form argument, while reserving the zero-atom assertion for rigid
  conductor points.

When adapting `p21p3_canonical_collar_examples_staging_20260828.tex`:

- remove all “subject to production verification” text;
- rename every `ex:p21p3-staging-*` and `eq:p21p3-staging-*` label to a
  collision-free live label, for example
  `ex:p21p3-ordinary-annulus-collar`,
  `ex:p21p3-higher-degree-residual-branch`, and
  `ex:p21p3-reducible-node-bt`; all three proposed names were free in the
  audited tree;
- in the first example, cite
  `eq:p21p3-gf-source-cutoff-factorization`, not the staging transition
  equation, and make explicit that the annulus is a collar issuing from the
  ambient endpoint `x` so that values at `x` are meaningful;
- in the second example, preserve the degree-two closed point over
  `\mathbf F_3`, the divisor `[p_q]-2[\infty]`, and both calibrated/current
  balancing equations; do not replace the closed point by geometric rational
  branches;
- in the nodal example, change the theorem reference to
  `prop:p21p3-curve-rigidity`, keep the rigid-point lemma label, and retain the
  explicit continuous-versus-discontinuous firewall.

These are examples, not additional theorem claims.  Give no theorem or lemma
an optional conventional name.

### 4.5 End-of-chapter provenance (current lines 3950--3980 and 4010--4017)

Replace both references to `lem:p21p3-type-one-zero-atom` by
`lem:p21p3-gfc-rigid-zero-atom`.  Add
`lem:p21p3-gf-legal-source-localization` and
`prop:p21p3-gf-virtual-annulus-bridge` to the proof architecture.  Replace the
old algebraically-closed reduced receipt by the canonical-collar dependency,
combined arbitrary-field receipt, and exact-live receipt.  Record the new
live hashes and run only after the live response exists; do not infer an item
identifier if the endpoint assigns none.

Replace “type-1 zero-atom estimate” at line 4014 by “rigid-point zero-atom
estimate.”  State only continuous-pair independence.  If the fresh
nonreduced live addendum passes, replace the old 27 August hashes/run in the
rendered current-status paragraph by its new exact bytes/run and say that it
removes reducedness without reintroducing algebraic closedness.  Historical
editorial receipts may retain the accurate 27 August record.

## 5. `ch72_major_open_problems.tex`

Audited hash:
`71ca7c9c597c3009c6adfdc784e76a6b415b244c77e4c38b7b3c010e23c37f70`.

At lines 6--8, advance only the book verification record to 28 August 2026;
retain the literature cutoff of 24 August 2026.  Keep the top count at 15
problem environments in Chapter 72, 16 book-wide, and **55** active atoms.

Replace, rather than append to, the P21.3 subsection at lines 2155--2283.
The staged residual text is a useful base after these corrections:

- remove its conditional-status paragraph after all relevant exact passes;
- remap `prop:p21p3-gfc-curve-rigidity` to the public reduced label;
- replace staging equation labels by collision-free live labels or leave the
  two displayed implications unlabelled;
- formulate the displayed problem as the continuous-pair question; do not say
  it is equivalent to the literal possibly-discontinuous version of CLD
  Definition 8.6.2;
- keep `prob:frontier-cross-fan-upstairs` and P21.3 as one T2 atom;
- keep good, separated, strict, boundaryless spaces as the displayed problem's
  ambient class.  Non-good, non-separated, non-strict, and boundary cases are
  outside both that displayed problem and the theorem and are not silently
  counted in P21.3;
- retain analytic dimension at least two, trivially valued fields, and
  component normalizations not known to be rig-smooth in the residual scope;
- remove non-algebraically-closed **reduced** nontrivially valued fields from
  the residual scope;
- remove nonreduced curves from the residual scope only after the fresh
  arbitrary-field nonreduced live addendum passes.  Before that gate they must
  remain residual;
- record the canonical-collar, combined arbitrary-field, exact-live, and (once
  available) fresh nonreduced receipts.  The old 20260826 reduced and 20260827
  algebraically-closed nonreduced receipts remain historical, not controlling
  for the broadened live claims;
- in the four-punctured discussion at lines 2259--2273, say that the earlier
  obstruction is subsumed in the reduced arbitrary-field scope and that the
  remaining atom is the continuous-pair question outside the final verified
  one-dimensional class.

After the fresh arbitrary-field nonreduced PASS, the clean one-dimensional
residual list is: trivially valued ground fields and spaces with a component
normalization not known to be rig-smooth.  Analytic dimension at least two
also remains.  Literal discontinuous-psh CLD Definition 8.6.2 is a separate
scope boundary and is not separately counted.  The count consequently stays
16/55, not 16/56.

## 6. `NonArchimedean.bib`

Audited hash:
`632bad0c6e7fbc42740c8e03f0b3ebf1318715131cedc7bf75208b948da4d5df`.

Add the noncolliding Ducros entry after `CLD25`:

```bibtex
@misc{Ducros24CurveStructure,
  author = {Ducros, Antoine},
  title = {La structure des courbes analytiques},
  year = {2024},
  eprint = {2405.10619},
  archivePrefix = {arXiv},
  primaryClass = {math.AG},
  note = {Version 1, 17 May 2024; French, 357 pages}
}
```

Also add the noncolliding Tate entry required by the fresh arbitrary-field
nonreduced proof:

```bibtex
@article{Tate71Rigid,
  author = {Tate, John},
  title = {Rigid analytic spaces},
  journal = {Inventiones Mathematicae},
  volume = {12},
  year = {1971},
  pages = {257--289},
  doi = {10.1007/BF01403307}
}
```

`CLD25` and `GJR26` already exist.  Neither new key occurs in
`ComplexGeometry.bib`; do not duplicate either entry there.

## 7. `open_problem_atomic_inventory_20260824.md`

Audited hash:
`04b9e03b506c8de1a7df9ed0ab47dd1b44796fa5b83e349188de3fac930e708a`.

Advance the inventory date at line 3 to 28 August 2026; retain the literature
cutoff.  Keep the exact count at 16 environments / 55 atoms and the T2 queue
at seven atoms.

At lines 371--379, replace the old “complete, algebraically closed” and
unqualified CLD-Definition wording by the exact continuous-pair residual
formulation.  At lines 411--435, replace the current reduced/nonreduced status
paragraph by the arbitrary-field record:

- reduced classification over every complete nontrivially valued field;
- locally finite component-current expression;
- continuous-pair Bedford--Taylor independence;
- canonical-collar and exact-live receipts;
- fresh nonreduced result and receipt only after its own exact PASS.

Remove non-algebraically-closed reduced fields from the residual list.  Remove
nonreduced curves only after the fresh addendum passes.  Preserve P21.3 in the
queue and preserve the total 55.  Do not edit old immutable receipts merely
because their historical scope is narrower.

## 8. `mathematical_revision_log.tex`

Audited hash:
`dc1d503e8411396332f450cc872cbf6e8f307b27c3bbca057c263dd6ac5b1ef1`.

Append a new 28 August item immediately before the final `\end{enumerate}`;
do not rewrite the historically accurate 27 August item at current lines
807--836.  The new item must record:

- the canonical-collar repair and exact bridge hashes/run;
- the materialized arbitrary-field reduced hashes/run;
- the four exact-live hashes, request/response/header hashes, and live run;
- the arbitrary complete nontrivially valued reduced scope and the
  continuous-pair-only conclusion;
- the fresh arbitrary-field nonreduced hashes/run once verified;
- the explicit exclusions: trivial valuation, non-good/non-strict/boundary
  scopes, non-rig-smooth component normalization, dimension at least two, and
  discontinuous psh pairs;
- P21.3 remains one T2 atom; 16 formal environments and 55 atoms with tier
  counts `(0,7,14,17,17)`.

Do not state “integrated byte-for-byte” or report a whole-book page count
until the exact live inputs, bibliography, ledgers, and full build have passed
the post-integration gate.

## 9. `rethlas_verified_results.md`

Audited hash:
`4b20f19dcf16c41dbacb9b24d04345cb0a002882cededc2edb3f333292b7aae8`.

Keep the current lines 423--464 as the historical 27 August
algebraically-closed reduced/nonreduced record.  Add a new 28 August section
immediately after it.  Until the live book is built, its status should say
“EXACT-LIVE PACKET VERIFIED / INTEGRATION PENDING”; change to “INTEGRATED
BYTE-FOR-BYTE” only after the source-closure manifest confirms the exact
inputs.

The new record should list the four exact-live hashes, their materialized
payload hashes, all three layers of verification (bridge, combined theorem,
exact-live), model/effort, verdict and record counts, and the continuous-pair
scope firewall.  Add the nonreduced exact-live bytes/run only after its PASS.
End with the unchanged inventory consequence: P21.3 is one T2 residual atom;
16 environments, 55 atoms, tiers `(0,7,14,17,17)`.

## 10. Compulsory cross-file synchronization found by the audit

Although not in the initial six-file list, `appendices/appL_provenance.tex`
must be edited in the same integration.  Current line 1239 references
`lem:p21p3-type-one-zero-atom`, which becomes undefined when the old reduced
packet is removed.  Replace the two P21.3 provenance records at lines
1236--1277 by a 28 August record citing the legal-localization lemma, the
canonical-collar bridge, the rigid-zero-atom lemma, the public reduced
proposition, and the fresh public nonreduced proposition.  Record arbitrary
complete nontrivially valued `K`, continuous-pair independence, exact new
hashes/runs, and the residual scope.  Keep the old receipts as historical
files.

After the core integration, synchronize these mutable status summaries so
they do not continue to present the algebraically-closed/type-1 result as the
current boundary:

- `editorial/theorem_provenance.md`;
- `editorial/chapter_status.md`;
- `editorial/major_open_problem_program.md`.

The dated `current_source_build_*` records and old production/live-integration
receipts are immutable history and should not be rewritten.

## 11. Final exact live receipt

Create
`editorial/rethlas_receipts_20260828/p21p3_curve_rigidity_arbitrary_field_live_integration_receipt_20260828.md`
without overwriting any 20260826 or 20260827 receipt.  It should record:

- bridge, reduced, and fresh nonreduced statement/proof hashes;
- materialized request, response, safe-header, service-verification, and log
  hashes for every controlling production run;
- exact model `gpt-5.6-sol` and effort `xhigh` from the service log;
- sequential/source record counts and zero failed checks;
- hashes of Chapter 16, Chapter 72, both bibliography files, the atomic
  inventory, revision log, verified-results ledger, Appendix L, and all
  synchronized status ledgers;
- full-book PDF/log/source-closure-manifest hashes and page count;
- explicit scope firewall and unchanged 16/55 inventory.

The helper's `checked_items: 0` display is not a mathematical count when the
schema omits a top-level `checked_item_ids` array.  Use the persisted
sequential and source-reference records as the authoritative counts.

## 12. Post-integration gates

1. Confirm every new live mathematical byte has a controlling exact
   production PASS, including the fresh nonreduced addendum.
2. Confirm the chapter inputs only the six live files, in the stated order,
   and no stale/combined/candidate packet.
3. Extract all labels in the actual source closure and require one declaration
   per label.  In particular, require zero remaining live references to
   `lem:p21p3-type-one-zero-atom`, `eq:p21p3-fundamental-cycle`, or candidate
   `prop:p21p3-gfc-curve-rigidity`.
4. Require zero remaining current-status claims that the verified curve scope
   is algebraically closed, zero unqualified “type-1 zero-atom” claims, and
   zero claims that the theorem proves discontinuous-pair CLD Definition
   8.6.2.
5. Require every `Ducros24CurveStructure` and `Tate71Rigid` citation to resolve.
6. Run `git diff --check` and a standalone Chapter 16 slice.
7. Run a forced, converged full-book `latexmk` build with BibTeX and index.
   Reject TeX errors, undefined references/citations, duplicate labels or PDF
   destinations, BibTeX/index warnings, rerun requests, and overfull boxes.
8. Inspect rendered pages containing the bridge statement/proof, both annulus
   examples, the arbitrary-field reduced theorem/proof, the nodal example,
   the nonreduced theorem/proof, Chapter 72's residual wording, and Appendix
   L's provenance entry.
9. Recount formal problem environments and atomic identifiers mechanically;
   require 16 and 55, with tiers `(0,7,14,17,17)`.
10. Hash the actual source closure, PDF, final log, exact inputs, requests,
    responses, headers, and receipts; only then mark the live integration
    complete.
