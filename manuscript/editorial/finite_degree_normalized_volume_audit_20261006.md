# Finite degree and local normalized-volume thresholds — 6 October 2026

This checkpoint began on 5 October and follows `bdd91fd`.
Three new Chapter 68.8 subsections
and provenance L.44 import the known finite degree formula for complex
algebraic klt pairs, explain its two inequalities, and give explicitly
identified formal consequences for the local integrability thresholds.
There is no original theorem, priority claim or independent production
model call. The historical August claim ledger retains its bytes;
the chapter opening now correctly restricts that cutoff to the ledger.

## Controlling main source

Zhiyu Liu, *The finite degree formula for normalized volumes*,
arXiv:2607.27032v2, revised 3 August 2026, is the controlling version.
Its official version history was checked. The twenty-page PDF has
411680 bytes and SHA-256
`10693c3d380c45c4256dcb8cbd35e1152ffe65dd8cf575831cd2d1b007fc4795`;
its 47463-byte extracted text has SHA-256
`052ca0c9b95ef1b6de8ac075fc24a9d50c16fbfc58c3e52fcec3d260ca4f9045`.
All extracted text and all twenty actual pages were read; all pages
were actually displayed in ten sheets. The reading receipt remains
separate from the unchanged acquisition receipt.

The local Theorem 1.1 has a finite local extension with singleton
closed fiber and complex residue fields. Its boundaries are effective
rational divisors, both pairs are klt, and the map is crepant for their
log canonical divisors. Neither isolation nor Galoisness is required.
The global Corollary 1.2 sums over every point in the finite fiber.
Stacks Tags 02LN and 05B8 were checked: an elementary étale
neighborhood separates the fiber into finite pieces, and the
singleton condition supplies the finite local extension for each.
The piece degrees sum to the global degree. The global degree is
not assigned separately to every individual point.

## Selected primary dependencies

Six dependency PDFs were inspected in selected text ranges and on
twenty-nine actual pages, displayed in sixteen sheets. This is not
a claim to have read those six papers in full. Matching manifests:
`/tmp/finite_degree_normalized_volume_primary_v1_20261005/manifest.json`
and `/tmp/finite_degree_dependencies_selected_v1_20261005/manifest.json`.
The ignored cache preserves all acquisitions and the initial main
reading record; the dependency reading record supplements it.

- Liu–Zhu, arXiv:2001.10557v1, submitted 28 January 2020, 17 pages,
  SHA-256 `bc43fbc161badf6ab78d8f5ce28274925649112625ebe743d76643132db34867`.
  Actual pages 1–2 and 12–14 displayed; text 1–140, 804–828 and
  858–905 read. Theorem 1.2(1),(3), their proofs, perturbation
  Theorem 4.1 and analytic-input Remark 4.2 control this application.
  Equality of delta is asserted when one partner is unstable;
  arbitrary-cover K-polystability and stable-regime delta equality
  are not imported. The separately published journal PDF is unacquired.
- Xu–Zhuang, with an appendix by Henri Guenancia,
  arXiv:2606.02401v2, revised 22 June 2026, 54 pages,
  SHA-256 `a9f5fa9c4a500153170c66a79035bb4aacbd4d825f487f94506db7a46cf34d61`.
  Actual pages 1, 6 and 10–15 displayed; text 1–55, 286–317 and
  525–835 read. The complete proofs of Lemmas 2.18–2.19 and
  Theorem 2.17 were checked. The import is the good-torus/Reeb
  dictionary, valuative criterion and uniform almost-semistability
  of nearby quasi-regular quotients. Differential forms and Kaledin
  claims require a separate later audit.
- Blum–Liu, arXiv:1802.09658v2, revised 15 August 2019, 28 pages,
  SHA-256 `c574781608de7690eb254bc69f0fa01a2d0236f96ce6d6d104076581dc786b74`.
  Actual pages 1, 6 and 21–22 displayed; text 1–164, 290–336 and
  1340–1449 read. Definition 7's family conditions and the complete
  Theorem 28 proof were checked; underlying normalized-colength
  approximation theorems remain identified known inputs. Published
  journal pagination is not transferred to this arXiv edition.
- Xu–Zhuang, arXiv:2205.10915v2, revised 17 January 2025,
  42-page accepted version, SHA-256
  `b273a0746f6f7ea3e94d9a8636cd7735c153182b35292fed2065bc666bde2c4c`.
  Actual pages 1–2, 4 and 39–40 displayed; text 1–210 and 2470–2585
  read. Theorems 1.1–1.2 and 1.6 and their concluding proof
  descriptions control stable degeneration and graded-ring
  preservation. The full higher-rank finite-generation proof is
  not claimed to have been independently rechecked here.
- Li–Xu, arXiv:1707.05561v2, revised 1 March 2019,
  55-page accepted version, SHA-256
  `b93c9f57490e65b0bd766aa2b1ce334ee715e36a8a686a3c644a6086bd7756a3`.
  Actual pages 3, 8–9 and 35–36 displayed; text 156–207, 475–622,
  2615–2825 and 2870–2985 read. Lemma 2.10 and Proposition 4.11
  supply nearby divisorial Kollár components with the same graded
  pair. This source's Theorem 4.14 is a klt-central-fiber statement,
  distinct from the journal locator used by Liu. The official
  correction notice, DOI 10.1007/s42543-019-00009-y, corrects
  cross-references and typesetting. The separate 79-page journal
  edition is unacquired; no equality of editions is claimed.
- Dorsch–Lazić, *Algebraic Geometry* 2(4) (2015), 476–488,
  publisher PDF, 13 pages, SHA-256
  `34c66126b82e86a309c3090edf020ff169359760e6a5d5744f82942686876c7a`.
  Actual pages 5–6, printed 480–481, displayed; text 192–299 read.
  Lemma 2.13 and Proposition 2.14, with their complete proofs,
  give the finite-map divisorial discrepancy relation.

## Mathematical checks

The lower estimate degenerates the downstairs pair to its stable
cone using a nearby divisorial Kollár component with the same
graded pair. The distinguished minimizing Reeb vector can be
irrational and need not equal the grading of the chosen one-parameter
degeneration. Liu's Proposition 3.1 retains the degree-zero-ring
hypothesis, lifts by normalization, and removes central ramification
by a finite parameter base change. Locality and normality make the
central fiber integral. Its spatial degree is still d; the degree
of the parameter change does not multiply it.

Good-torus lifting and the finite isogeny give compatible Reeb
vectors. Theorem 4.1 transfers K-semistability by the unstable
quotient delta comparison, nearby uniform delta bounds and
continuity of the valuative criterion for a fixed destabilizer.
The acquired log Fano comparison uses analytic metric inputs.
The new outline does not claim a purely algebraic substitute.

For compatible cones, a homogeneous generic basis embeds d shifted
copies of the downstairs ring into the upstairs ring. Its torsion
cokernel has dimension at most n−1, so it contributes lower order
weight counts. The leading coefficient multiplies by d. The
discrepancy equality is for rescaled compatible valuations:
primitive divisorial discrepancies multiply by the ramification
index. These two statements are not conflated.

Lower semicontinuity in the lifted family gives V(original) >=
V(central), since all nonzero fibers are isomorphic. K-semistability
and the cone leading-term computation give the lower estimate.
The reverse estimate uses valuation-ideal extension and a generic
rank-d module injection. For c=v(m)>0, the containment
m^ceil(m/c) in a_m bounds the torsion length by O(m^(n−1)). No
additional Izumi theorem is needed for that containment. This
corrects the stronger wording in the initial reading boundary note
by supplementation, preserving the earlier receipt's bytes.

Passing to a Galois closure may make the crepant boundary negative:
the transformed coefficient is e b−(e−1). Effectivity is retained
throughout the imported theorem, and no subklt minimizer argument
is substituted for it.

The exponent consequence retains zero boundary, isolated complex
algebraic Q-Gorenstein klt germs, n>=2, admissible strongly
pseudoconvex domains and each domain's own adapted probability
measure. The known alpha and sharp MT formulas then scale by
d^(1/n). No probability pushforward, pullback of individual
Dirichlet solutions, endpoint existence, uniqueness or compact
big-class delta transformation is inferred.

## Preservation and typography repair

Forty-six prior formal statement/proof blocks in Chapter 68 and
Appendix L retain their bytes. The earlier local klt explanation
is preserved except that two literal carriage-return characters
in its primary-ideal subscripts are replaced by the intended TeX
command. The source comparison exposed the mistake; this is a
typography repair, not a change to the ideal infimum or its power.
The final rendered review includes both repaired formulas.

The first source-gate attempt and two diagnostic attempts produced
no gate record. They exposed the carriage-return versus universal
newline comparison. The corrected source gate reads source bytes
directly and permits only the two explicit subscript repairs.
The controlling gate is the fresh v4 record; diagnostic scripts
are retained without rerunning them.

The forty-two full canonical status rows, native catalogue and PDF,
research-only toric candidate, earlier frozen manifests and exports
remain byte-preserved. The BJ22 changing-divisor proof gap remains
explicit. General non-Archimedean Siu/closure, A2–A4 and the original
toric entropy candidate receive no new verification status.

## Final build and rendered review

The final book has 4,347 pages and 20,208,209 bytes, SHA-256
`1efc41cd0d42aeec3133db9e3f16645dde8dd2c99c8731d98ad0e95f7dc582c2`.
TeX errors, unresolved references/citations, package and pdfTeX warnings,
missing characters, overfull boxes and rerun requests are zero.
The existing underfull-box count remains 954. BibTeX uses 348 entries
without warnings; MakeIndex accepts 750 entries without rejection or
warnings. All 46,776 internal links, 21,780 named destinations and
409 distinct numeric index destinations pass. The reference checker
finds 425 inputs and 12,753 unique labels, all clean. The inventory
checker passes forty-two atoms in twelve families and the unchanged
tiers 0/3/7/15/17.

Thirty-six matching final book pages were actually displayed in
eighteen sheets: title, relevant contents, the revised chapter opening,
the complete earlier local comparison including both repaired
subscripts, all three new subsections and the following transition,
all of L.44 and its transitions, both new index locations, and the
complete seventeen-page bibliography. The frozen rendered manifest is
`/tmp/finite_degree_book_pages_v1_20261006/manifest.json`.
This is a scoped final review, not a new complete-book rereading.

Two active TeX inputs changed and the other 423 retain their bytes.
All 108 protected inputs, 46 prior formal statement/proof blocks,
42 preceding October-5 frozen manifests, full canonical status rows,
native catalogue, toric candidate and previous exports are preserved.
Seven appended bibliography keys distinguish the controlling editions.
The source gate is `/tmp/finite_degree_source_gates_v4_20261005.json`;
the PDF gate is `/tmp/finite_degree_release_gates_v1_20261005.json`.
The build began on October 5 and final review/publication continued
on October 6. Earlier diagnostic scripts and records are preserved.
Publication uses the work branch and the user's standing GitHub
authorization, retaining the draft PR and its prior description.
