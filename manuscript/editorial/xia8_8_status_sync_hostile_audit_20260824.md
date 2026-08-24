# Hostile audit of the Xia Conjecture 8.8 status synchronization

Date: 24 August 2026

## Superseding release re-audit

**Verdict: PASS.**  The two must-fix findings in the frozen audit below are
closed.  The MP--DXZ source package and projective-rational full-link problem
are assigned to Chapter 71, while Chapter 72 contains the broader
pseudoeffective frontier.  More importantly, the later exact-current Chapter
55 submissions now distinguish all three proof objects correctly: the metric
theorem passed run `20260824T054849Z_57635bfa07f4`, and the line-bundle
specialization passed `20260824T061508Z_17bf73c6b37c`, each with final
`correct`, zero critical errors, and zero gaps.  The older repaired-packet and
complete-author-source receipts remain corroborating audits only.  A hostile
status scan finds contrary phrases only inside explicitly dated,
superseded-stage text or search instructions.  The unpublished-source,
positive-volume, and no-priority boundaries remain intact.  The original
snapshot and its `FAIL` verdict are retained below as the audit trail; they no
longer state current release status.

## Scope and verdict

This is a read-only audit of the following thirteen synchronized status files:

1. `editorial/chapter_status.md`;
2. `editorial/mathematical_revision_log.tex`;
3. `editorial/theorem_provenance.md`;
4. `editorial/part4_ch47_55_postexpansion_audit_20260824.md`;
5. `editorial/part6_postexpansion_audit_20260824.md`;
6. `editorial/major_open_problem_program.md`;
7. `frontmatter/part5_intro.tex`;
8. `parts/part6/ch72_major_open_problems.tex`;
9. `appendices/appL_provenance.tex`;
10. `editorial/rethlas_open_problem_attempts.md`;
11. `editorial/rethlas_r3_report.md`;
12. `editorial/rethlas_verified_results.md`; and
13. `editorial/solver_dossiers_20260815/xia_partial_okounkov_questions.md`.

No audited file was modified.  The audit also read the two production
receipts, their manifests and aggregate reports, the current Chapter 55
integration, and the Chapter 71--72 auxiliary files needed to check numbering
and literal problem counts.

**Verdict: FAIL PENDING TWO MUST-FIX STATUS REPAIRS.**  The synchronized
mathematical scope, problem count, unpublished-source boundary, and exclusion
firewall are otherwise coherent.  One current chapter-number statement is
wrong, and one receipt sentence states a stronger exact-current relationship
than the available receipt establishes.  Neither finding challenges the
verified repaired proof packet or the repaired author source.

## Audited snapshot

The three files updated after the auxiliary source-level receipt was produced
were audited at the following hashes:

- `editorial/theorem_provenance.md`:
  `1f1ab06492d407111a655d2bd608084848e37dbca1db02befcc53c110a266716`;
- `editorial/rethlas_verified_results.md`:
  `dbebbcfc2a36dafd255077c05d343ff9949f4777dbeedee5462a366b43568ac8`;
- `appendices/appL_provenance.tex`:
  `fa4d8935c364acf0b0d5d289057b3bc3247b1829eebe36daeb9da6a519707828`.

The other ten audited hashes are, in the order listed above,
`0c8f007c...68c1c`, `9f65e91f...bbbf09`,
`bc0eace2...fa6c6c`, `2b7681dd...5cd267`,
`f935a6d6...3780a7`, `e1140ad2...673c8`,
`d7a7277b...d4c74`, `778196fb...5014e`,
`5bfab4c6...a9f8b`, and `0462006a...4ec23`.

## Must-fix findings

### M1. The current MP--DXZ disposition is assigned to the wrong chapter

**Location:** `editorial/rethlas_open_problem_attempts.md`, lines 285--302.

The ledger says that the failed pseudoeffective packet's open boundary is
"now recorded in Chapter 72" and that "Chapter 72 keeps" the finite-energy
MP--DXZ correspondence, divisorial analytification, order reflection, formal
ideal-evaluation consequences, and the elementary generic-fibre and
zero-volume obstructions.

That current chapter assignment is false.  The compiled labels and live source
give

- `chap:pseff-mp-dxz` = Chapter 71;
- `chap:major-open-problems` = Chapter 72;
- `prob:pseff-projective-rational-full-link` = Problem 71.7.1; and
- `prob:frontier-mp-pseff` = the broader Chapter 72 research-frontier problem.

The listed sourced results and elementary obstructions are in Chapter 71.
The exact unrestricted ample-projective MP--BJ comparison is also retained as
the separate Chapter 71 problem.  Chapter 72 summarizes and broadens the
remaining compact-Kaehler pseudoeffective realization problem; it does not
replace the Chapter 71 disposition.

**Required repair:** change lines 285--302 so that the sourced package and the
projective-rational full-link problem are assigned to Chapter 71, while the
broader pseudoeffective MP-realization frontier is assigned to Chapter 72.
Preserving the historical packet description is harmless, but the words
"now" and "Book disposition" must describe the live numbering accurately.

### M2. The packet receipt is not literally a receipt for the later Chapter 55 TeX integration

**Primary location:** `appendices/appL_provenance.tex`, line 99.

**Related status language:** `editorial/rethlas_verified_results.md`, lines
3--7 and 20--52; the current Chapter 55 provenance paragraph at
`parts/part5/ch55_okounkov_dh.tex`, lines 1413--1427.

The appendix says that the repaired-packet run "verifies the exact proof used
in" the two Chapter 55 theorems.  The exact verifier input was instead the
repaired Markdown proof packet with SHA-256
`9227826d7ba5c641c5fe32cc4daae9acbb3b57274dcc1b356ba8beadd58cad7b`.
The current Chapter 55 source has SHA-256
`0bf0b10c45819eb8b7007e55fc583d612d9e70177f5dd03211ae7cac509e16c1`
and was edited after the packet run.  It is a LaTeX reconstruction of the
verified argument, not the byte-identical verifier input.  The later
source-level run verifies the repaired author `main.tex`, SHA-256
`5746eb011417caecfa876c05c6c74fb548e2ae9d086c1441189bbcad02a96594`;
it likewise does not verify the Chapter 55 TeX file.

This matters because the verification ledger itself says that `VERIFIED`
means the exact statement and proof were checked and that later proof edits
invalidate a receipt until re-audited.  The mathematical theorem remains
supported by two successful exact proof objects, but the present wording
collapses three distinct objects:

1. the controlling repaired proof packet;
2. the complete repaired author source; and
3. the later book integration.

**Required repair:** either submit a frozen exact Chapter 55 statement-and-
proof block (with its necessary local definitions) for a production receipt,
or replace "verifies the exact proof used in" by language such as "verifies
the controlling repaired proof object underlying" the two theorems and record
a separate post-integration equivalence audit.  The auxiliary repaired-source
receipt must be described as corroboration, not as a Chapter 55 integration
receipt.  The current `rethlas_verified_results.md` wording already calls it
"Exact-source corroboration" and should retain that distinction.

## Checks that passed

### Current versus historical status

The six files that preserve contrary pre-verification language place an
explicit 24 August controlling addendum before it and state that the older
classification is superseded.  In particular, the old phrases
"literature-resolved", "open pending verification", and "unverified source
claim" remain identifiable as audit history rather than current status.  The
15 August dossier also says expressly that its old partial proof is not
promoted and that the later receipt belongs to a separate repaired packet.

After M1 is repaired, the controlling current classification is coherent:
Xia Conjecture 8.8 is verified only on the connected smooth-projective,
big-line-bundle, positive-Cao/ideal-model-volume locus; no publication,
zero-volume, transcendental-class, singular-variety, maximizing-valuation, or
attainment claim is made.

### Chapter numbers and problem counts

Direct source counting gives exactly one `problem` environment in the live
Chapter 71 file and twenty-one in the live Chapter 72 file.  No other numbered
chapter contains a `problem` environment.  The auxiliary files confirm that
the two chapter labels compile as 71 and 72 respectively.  Therefore the
book-wide literal count of twenty-two is correct, and resolving the
positive-volume subclaim does not remove the zero-volume environment, which
retains several genuinely open residual scopes.

The OP-01--OP-21 order in `major_open_problem_program.md` agrees term by term
with the twenty-one Chapter 72 problem environments.

### Rethlas receipts and hashes

The controlling repaired-proof receipt is internally consistent:

- target statement SHA-256:
  `fe2b418a660abe1fcc3e3736d9f659c7c54deef95f92abdbda4d69a78aea91c6`;
- proof packet SHA-256:
  `9227826d7ba5c641c5fe32cc4daae9acbb3b57274dcc1b356ba8beadd58cad7b`;
- run: `20260824T023833Z_fe2b418a660a`;
- item: `pi_c41c7ec0b7c9768a64d29183`;
- verdict: `correct`; one checked item; zero failed or blocked items; zero
  critical errors; zero gaps.

The auxiliary complete-source receipt is also internally consistent:

- target statement SHA-256:
  `b8adabf0730c0ffd35204d72f3667263e250488da23c144c9d8ebeece55fe91a`;
- repaired `main.tex` SHA-256:
  `5746eb011417caecfa876c05c6c74fb548e2ae9d086c1441189bbcad02a96594`;
- run: `20260824T032252Z_b8adabf0730c`;
- item: `pi_b80d4a29bb37992748e896a6`;
- verdict: `correct`; one checked item; zero failed or blocked items; zero
  critical errors; zero gaps.

The exact-source receipt is now accurately recorded as a secondary,
corroborating gate in `rethlas_verified_results.md`,
`theorem_provenance.md`, and `appL_provenance.tex`.  It need not be duplicated
in every historical ledger.  As a non-blocking traceability improvement, the
appendix could add the receipt path
`editorial/rethlas_receipts_20260824/xia_conjecture_8_8_repaired_source_receipt.md`
next to the source-level run identifier.

### Unpublished-source boundary

Every controlling current statement identifies *Mixed Volumes of Okounkov
Bodies* as an unpublished July 2026 work in progress.  None relabels it as a
published theorem, and all distinguish mathematical verification of the
author-supplied proof from publication status.  The bibliography uses
`@unpublished` and records the repaired-proof digest.  Historical claims that
called the item a literature resolution are explicitly superseded.

### Cross-references and equation references

Static extraction found no unresolved target among the `\cref`, `\Cref`, or
`\crefrange` calls in the synchronized TeX files.  It also found no unresolved
`\eqref` target and no bare object `\ref` introduced in those files.  The two
new theorem labels, the provenance appendix label, the Chapter 71--72 labels,
and the zero-volume problem label all exist.  Thus the requested convention
of clever references for objects and `\eqref` for equations is preserved.

### Deligne-pairing exclusion firewall

The excluded paper arXiv:1710.09731 is absent from the bibliography and from
the load-bearing citation chain.  Its occurrences in the audited ledgers are
only explicit firewall notices.  The repaired proof packet, repaired author
source receipt, hostile audits, and Chapter 55 dependency list do not cite or
use it directly or indirectly.  The remaining generic Deligne-pairing
language in other chapters is attributed to independent BHJ/intersection
sources and is not a dependency of the Xia 8.8 argument.

## Release recommendation

Repair M1 and either close or accurately disclose the post-integration gate in
M2.  Then rerun the static status search for the phrases `Chapter 72 keeps`,
`exact proof used`, `Conjecture 8.8 remains open`, and `literature-resolved`.
If the historical hits remain behind their explicit controlling addenda and
the live Chapter 55 object has an exact integration audit, this thirteen-file
status synchronization can be marked PASS.
