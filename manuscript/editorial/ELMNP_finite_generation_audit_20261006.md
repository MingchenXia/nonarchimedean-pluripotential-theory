# Common valuation fans and finite-generated ideals — integration audit

Date: 6 October 2026. Baseline work commit:
`aeb39d473bb8d8e567972d464f64f541e15f0a66`; main:
`00957114db21b627e97369563032ceda9cea09c7`.

Appendix C.4.1 now explains the corrected ELMNP finite-generation
argument beside its existing asymptotic ideal discussion. Appendix L.60
records the exact editions, source locators and diagnostic qualifications.
The result is attributed to the 2023 erratum's Proposition 1.1 and
Lemma 2.1, with the 2006 published paper cited separately. This is a
known-result explanation, not an original theorem or canonical solution.

## Mathematical signature

The imported category is an integral reduced finite-type variety over
an algebraically closed field, in arbitrary characteristic. The grading
semigroup is finitely generated and saturated in a finite-rank free
lattice. Ideals are coherent, the degree-zero ideal is the structure
sheaf, and the sheaf of Rees algebras is finitely generated. The
discussion explicitly separates this input from the smooth
characteristic-zero multiplier-ideal and regular F-finite test-ideal
constructions surrounding it.

On the saturated nonzero support, finitely many generating degrees give
a rational linear-programming minimum for each centered discrete
valuation's asymptotic ideal order. The optimizer can be rational even
when the costs are irrational. The function is homogeneous and
subadditive, hence convex. Positive costs give dual polyhedra whose
normal fans have support equal to the generating cone and rays in the
fixed finite list of generating directions. A common refinement of
the finitely many fans works for every cost vector; continuity extends
it to zero costs. The fan is independent of the valuation.

The corrected proposition has quantifiers: one smooth fan exists; for
every smooth refinement, a positive integer d can then be chosen. A
smooth cone's primitive rays extend to a lattice basis. On each ray,
finite generation gives a Veronese with exact powers. A common multiple
of the selected fan's finitely many ray integers yields the displayed
valuation chain for degree dm. The product inclusion has that scaled
degree. The rank-one discrete valuative criterion on Noetherian domains
then yields equality of integral closures. Both bars are retained.
Zero-ideal degrees outside the saturated nonzero support are handled
separately, and no finite asymptotic value is manufactured from an
empty infimum. The preexisting even/unit and odd/(x) example explains
why the Veronese integer cannot simply be omitted.

The result concerns integral closures of finitely generated systems;
asymptotic multiplier ideals use their stabilized maximal member.
No finite-generation hypothesis is asserted for the book's arbitrary
envelope algebras. General non-Archimedean Siu/closure remains
conditional at the existing BJ22 proof boundary.

## Exact sources and diagnostic reuse

The [preceding source review](ELMNP_base_locus_erratum_source_review_20261006.md)
and [its immutable manifest](ELMNP_base_locus_erratum_source_review_manifest_20261006.json)
freeze complete reading of the seven-page 2309.16722v1 erratum and the
35-physical-page published original, plus sixteen reused selected
dependency pages. This integration reuses that evidence and claims
**zero fresh primary-source pages**. The source manifest SHA-256 is
`2036cad2d88ca4e2974f245e64d9f95c645200ae9724a33f99d4ac9630ff78b2`.

The thirteen diagnostics distinguish the acknowledged old induction
gap, nine literal formula/scope errors and three interpretation guards.
In particular, the optional Remark 2.3 needs a vector relation and
retention of untouched coordinates; the normal-fan proof is independent
of those misprints. Other local qualifications distinguish infimum from
unproved attainment, proper valuation centers, a missing inequality,
low-dimensional isolated unstable rays, zero versus unit base ideals,
and scaled ray indices. They do not refute the corrected proposition.
The full external linear-programming, smooth-refinement and Veronese
antecedent chain is not freshly certified. Historical questions are not
promoted to current canonical open problems.

Two bibliography keys identify the published 2006 article and the
exact 2023 v1. They retain the corrected Mustaţă spelling. The existing
restricted-volumes v2 key remains a distinct paper and interface,
including its separate Chapter 46 restricted-Fujita locators.

## Preservation and verification

The active TeX changes are confined to Appendix C and an appended
Appendix L section. Removing the new Appendix C roadmap and subsection
recovers its baseline bytes exactly; Appendix L begins with its complete
baseline bytes. All 32 existing formal/explanatory blocks and 13 proof
blocks in these files are byte-preserved; no formal environment is
added. All 423 other active inputs, 108 protected verification/status
inputs, 77 prior frozen manifests and 133 earlier exports are unchanged.
Removing the two new bibliography entries recovers the old complex
bibliography exactly; the non-Archimedean bibliography is unchanged.

There are seven new labels, five tags C.18a--e and three index entries.
The source closure remains 425 files, with 12,881 unique labels and no
missing inputs, multiply defined labels or dangling references. There
are 393 cited entries among 688 unique bibliography keys. The canonical
inventory passes at 42 atoms in twelve families with statuses
0/3/7/15/17. The native catalogue source and PDF are byte-preserved,
and the editor is neither reopened nor changed; no native compilation
is claimed.

The final complete build has **4,411 pages**, 20,494,400 bytes, SHA-256
`c549204270520c326e447cd783801acd1d927c25025d2503ebaeb7ae10c3b1e7`.
Its final log has zero TeX errors, package/pdfTeX warnings, missing
characters, overfull boxes, unresolved references/citations or rerun
requests. The unchanged underfull-box count is 954. Bibliography and
index generation have zero warnings; the index accepts 770 entries
and rejects none. All 22,025 named destinations and 47,136 internal
links have valid targets; the PDF retains six part introductions and
2,572 outline entries.

All **43 selected final pages in 22 sheets** were read as full extracted
text and actually displayed: 64, 69, 3945--3946, 3949--3953,
4171--4175 and 4383--4411. These include the new material, adjoining
transitions, affected contents, complete index and complete bibliography.
The two closure bars and five new formula tags were visually checked.
This is a scoped final-page review, not a fresh reading of all 4,411
pages. The reading record SHA-256 is
`33d28c77a0bee0981196374e644183ce3ea13bfd48fc35b3641a46858dc762c9`;
the release gate is
`e99d2afda717f6676d5850845fc1c89031f15f0718dd806e3748204249faceb6`.

The release exports the full book, the 43-page matching review and a
complete active-source ZIP. Every ZIP member is compared with the saved
workspace bytes; a new isolated archive compilation is not claimed.
The immutable manifest embeds ignored-cache metadata and exact source
gates. No independent production model call or new verification receipt
is claimed; existing receipts retain their original byte scope. Routine
main/work synchronization and work-branch publication follow the user's
standing authorization without changing platform approval checks.
