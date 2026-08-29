# P06.1 live-integration map

Date: 29 August 2026

Status: **promoted**. The exact statement and proof passed production Rethlas
run `20260829T043457Z_0b1b4d161e3b`, item
`pi_7cd35ebd843cf80a7cd696bb`, using `gpt-5.6-sol` at `xhigh`, final
`correct`, zero critical errors, and zero gaps. The live manuscript includes
the unchanged exact files by `\input`; this document records the integration.

## Exact mathematical boundary

The positive theorem covers every classically pluriharmonic real-valued
function on a good strict quasi-smooth analytic space over a complete
nontrivially valued field. It concludes real PL regularity and GJR
harmonicity. It uses no global quasicompactness, separatedness, or
boundarylessness.

The natural coefficient group is \(\mathbf R\). The strict semistable annulus
with \(h=\sqrt2\log|T|\) disproves both the integral-PL and the
\(\mathbf Q\)-PL strengthening.

Within the original good separated strict boundaryless P06.1 scope:

- the new theorem covers the quasi-smooth locus in every dimension;
- the published curve comparison covers all strict analytic curves,
  including singular and nonreduced curves;
- the exact residual is local real-PL regularity at a non-quasi-smooth point
  of analytic dimension at least two.

P06.1 therefore remains one active T2 atom. The total atom count, tier counts,
and queue order do not change.

## Completed promotion order

1. Completed the exact-byte production verification of
   `p061_quasismooth_ph_rpl_statement_20260829.tex` and
   `p061_quasismooth_ph_rpl_source_aware_proof_20260829.tex`.
2. Archived the authoritative service result, prepared a receipt, and added the
   final run id, item id, and exact SHA-256 digests to the placeholders in the
   Chapter 72 and Appendix L snippets.
3. Added the two bibliography entries from
   `p061_quasismooth_ph_rpl_bibliography_additions_20260829.bib` to
   `manuscript/bibliography/NonArchimedean.bib` after a duplicate-key check.
4. Inserted `p061_quasismooth_ph_rpl_ch18_insertion_20260829.tex` at the end of
   the proof of `prop:ch18-harmonic-functorial`, immediately before the
   paragraph beginning “The integral metric criterion of
   Chambert--Loir--Ducros”. The two exact packet files should remain included
   by `\input`, not copied by hand.
5. Applied the hypothesis-ledger, comparison-ledger, and source-note blocks in
   `p061_quasismooth_ph_rpl_ch18_ancillary_updates_20260829.tex` at the stated
   anchors.
6. Applied the Chapter 72 replacement and insertion blocks in
   `p061_quasismooth_ph_rpl_ch72_narrowing_20260829.tex`.
7. Applied the atomic-inventory wording in
   `p061_quasismooth_ph_rpl_inventory_narrowing_20260829.md`; keep P06.1
   active at T2 and keep the aggregate counts unchanged.
8. Applied the verification-boundary paragraph, provenance record, and
   questions-not-promoted replacement in
   `p061_quasismooth_ph_rpl_appL_narrowing_20260829.tex`.
9. The full bibliography/build cycle and warning scan are recorded in the
   milestone commit that promoted this packet.

## Why this Chapter 18 location is natural

The result is a regularity bridge from classical pluriharmonicity to the
harmonic PL sheaf. It therefore belongs after the construction and
functoriality of harmonic PL functions, but before the current-positivity and
zero-current comparisons. Placing it there lets the proof use the definition
and functorial framework already established while keeping P06.1 logically
separate from P06.2.

## Isolated compile status

The existing exact packet harness
`p061_quasismooth_ph_rpl_compile_20260829.tex` compiles the exact statement
and proof in isolation. Its frozen log records no warnings, undefined or
multiply defined references, or box defects, and the four-page PDF passed
the packet's render inspection.  As a non-mutating check, the harness and the
two exact inputs were copied to a fresh directory under `/private/tmp` and
rebuilt on 29 August 2026.  The second pass again produced a four-page A4 PDF
of 238339 bytes; the final log had no LaTeX or package warnings, undefined or
multiply defined references, overfull or underfull boxes, or fatal errors.
The new integration prose consists only of ordinary chapter text and ledger
rows; it does not change the exact theorem or proof bytes. A new full-book
compile is nevertheless mandatory after live promotion because the staging
snippets introduce cross-references and two new bibliography keys.
