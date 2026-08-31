# Independent bounded audit of the live curve correction

Date: 31 August 2026. Auditor: `/root/p082_independent_reaudit`.
Author/integrator of the reviewed live changes: `/root`.

## Verdict and exact scope

**PASS for the source integration described below, after three summary
corrections made by the author during this audit.** There are no remaining
substantive integration errors or unresolved scope discrepancies in the
reviewed passages. This is not a whole-book mathematical audit, a new
production verification, or a final-PDF layout certificate.

The bounded targets are Chapter 17's global-psh comparison/Tate insertion,
its associated warning, dictionaries and source note; Chapter 72's
local/global-psh subsection; inventory atom P08.1; and Appendix L,
`sec:appL-curve-correction-20260831`. The neighboring historical P08.2
twistor result is checked only for separation from P08.1, not re-proved.
The known downstream Chapter 29/31 defects and the rest of Part III remain
outside this audit and are not certified repaired. No inventory atom is
retired by this correction.

No live or frozen mathematical file was edited by this auditor. Only this
isolated report and its checksum manifest were authored, using apply_patch.

## Frozen principal inputs

Both full statements and proofs were reread. SHA-256 was checked at the
beginning and after the author's summary corrections.

| Input | SHA-256 |
| --- | --- |
| A: corrected comparison statement | `5158fe6399885289ba2e9bf7a57f7da32a87fdb7b7d6e6b5bc20879e054564b6` |
| A: corrected comparison proof | `99028d9d33abcfe31e42dd6f5e1aedb6c00822c5408ef46da4ef692ed2ef3a17` |
| B: revised1 Tate obstruction statement | `4d997e024fa7ec642299a0d86ae1d9b9d06c6041f7f10b694369d7faa458d28c` |
| B: revised1 Tate obstruction proof | `c7a2a08ad4ad82df4470004d01fa131fecdc01ab03f60eefa67bbe7eaa8f0a5a` |

A is in `../p081_positive_degree_and_zero_criterion_candidate_20260831/`.
B is in `../p081_degree_zero_tate_obstruction_audit_20260831/revised1/`.
The live Chapter 17 input directives load exactly these four files, in
statement/proof order. The observed book recorder also names these exact
paths. Their old candidate-status comments remain frozen comments; current
verification status is supplied by the dated receipts, not by changing the
principal bytes.

The reviewed live-file snapshot has these hashes:

| Live file | SHA-256 |
| --- | --- |
| `manuscript/parts/part2/ch17_metrized_bundles.tex` | `6024851fd6c9539aec0f54b711980d3a1e94fbfccae4667eac97086dd9152542` |
| `manuscript/parts/part6/ch72_major_open_problems.tex` | `6e671da09d50cc7becd553d319a0cbce0fe6c3622ac77a491550411a32c69b8c` |
| `manuscript/appendices/appL_provenance.tex` | `fd70efc868943f82c38e9f6bea47a7129cbcfbc726d2638d97f5a83b375569a4` |
| `manuscript/editorial/open_problem_atomic_inventory_20260824.md` | `227b7fc73c50c4f17e17b5efb9231a595cb9585463299ff77feaa30e96ef06d6` |

The file hashes are snapshot identifiers, not certification of every
unreviewed passage in those files. Subsequent live edits require a new
comparison; a changed hash must not be silently normalized in this ledger.

## Source definition and interface matrix

The primary source was read directly in text and by visual inspection of
the complete relevant PDF pages: Antoine Chambert-Loir and Antoine Ducros,
*Formes differentielles reelles et courants sur les espaces de Berkovich*,
arXiv:1204.6277v2, cover dated 25 July 2025 (internal typesetting date
29 July 2025). Local exact copies are `/private/tmp/CLD25.pdf` and
`/private/tmp/CLD25.txt`, included in the manifest.

| Primary locator | Verified meaning | Integration obligation |
| --- | --- | --- |
| CLD 17.8.5, p. 498 | Globally psh means uniform convergence, in logarithmic metric distance, of a sequence of smooth psh metrics on the same line bundle. Globally dpsh is an isometric quotient of two globally psh metrized line bundles. | Chapter 17's definition and Chapter 72/P08.1 use this literal class. They do not define it as nef rational-model closure. |
| CLD 17.8.6-17.8.7, pp. 498-499 | The canonical metric on projective O(1) is globally psh; a semiample formal line bundle on a proper formal model has globally psh generic-fibre metric. | Relative ampleness in A's positive-degree branch supplies semiampleness after clearing a power. This is not a general theorem for every nef model. |
| CLD 17.8.9, p. 499 | The parlinear/global-dpsh conclusion is stated for analytifications of projective varieties. | The live text attributes the published conclusion and does not promote the still-pending corrected analytic-transfer/factorization packets. |
| CLD 17.8.10, p. 500 | The first paragraph asks the continuous-psh/global-psh question on projective varieties. The second asks for the proper strict analytic extension of 17.8.9 under projective-special-fibre model existence. | P08.1 and the separately retired P08.2 must not be conflated. The Tate example does not refute the first paragraph. |
| Frozen A, statement items (1)-(2), proof Steps 3-7 | Positive-degree rational-model and FS approximation; exact degree-zero model-existence criterion. The finite-normal envelope argument is used with an ample generic class only. | No degree-zero model existence, general real-class envelope theorem, singular-curve result, or higher-dimensional conclusion may be inferred. |
| Frozen B, statement and proof Steps 1-5 | An irrational Tate period ratio obstructs every nef formal model of every positive tensor power, while the cubist metric is locally ordinary-CLD-smooth and harmonic. | The constant sequence of this smooth psh metric proves literal global pshness; the failed approximation is fixed-line-bundle rational-model approximation only. |

The strict positivity distinction is mathematically consequential.
Globally generated positive tensor powers are required by the FS
construction. Nef rational models of a degree-zero line bundle do not in
general supply them. Conversely, B's smooth psh metric is globally psh by
the definition without any model-existence implication.

## Checks of the live mathematical scope

1. **Field and curve hypotheses.** A's summary scope is a smooth proper
   geometrically connected algebraic curve over a complete nontrivially
   valued field. Neither the dictionary nor Chapter 72 replaces this by an
   arbitrary analytic, singular or higher-dimensional space. B retains an
   algebraically closed complete field and the existence of the specified
   irrational ratio; it is not asserted over every such field.

2. **Positivity and degree.** The controlling hypothesis is a continuous
   metric with locally CLD-psh weights. A gives nonnegative degree and
   positive curvature of the indicated total mass. Positive degree gives
   relatively ample rational algebraic models and FS closure. At degree
   zero curvature vanishes, but rational-nef-model approximation holds if
   and only if one such metric already exists on the fixed line bundle.
   The final summaries preserve these separate conclusions.

3. **Tate integration.** The two edge lengths are a and ell-a. Irrationality
   of a/ell is equivalent to irrationality of their ratio. The proof's
   zero-curvature equations force constant slopes on each original edge;
   subdivisions and attached finite trees cannot change the period
   obstruction. The live prose accurately states this and the ordinary
   local smoothness of the cubist metric. Its constant smooth sequence is
   a valid literal-global-psh witness.

4. **Envelope boundary.** The read frozen A proof restricts the envelope
   argument to degree greater than zero, where c1(L) is ample. The live
   warning, Chapter 72, P08.1 and Appendix L explicitly deny a general
   nontrivially valued envelope conclusion. No arbitrary real-theta
   positivity extension or unrestricted degree-zero existence assertion is
   introduced by the audited integration.

5. **Supersession.** Searches of non-editorial live TeX found no occurrences
   of `thm:p081-curve-local-global`,
   `cor:p082-smooth-strict-curve-transfer`, or
   `prop:p083-curve-parlinear-global-dpsh`, and no old principal input
   paths. The old paths were also absent from the observed book recorder.
   The old theorem label occurs in the inventory only inside an explicitly
   marked supersession paragraph. Historical editorial files remain
   preserved, not promoted back to live proof inputs.

6. **Inventory and pending work.** P08.1 remains active with its literal
   smooth-global-psh question and residual scope. The correction does not
   retire another atom or silently accept the pending proper-analytic
   transfer or curvature-factorization packets. The P08.2 twistor claim is
   explicitly separate. The count 51 and tier vector (0,5,12,17,17) are
   consistent among these integration passages; a fresh audit of all
   inventory atoms was not performed.

## Findings raised and closed by the author

Three summary corrections were requested and their resulting exact live
lines were reread before the final hashes above were taken:

- Chapter 17's forward dictionary originally said "FS/model approximable
  in positive degree; in degree zero iff one nef rational model metric
  exists." This could wrongly carry FS approximation into degree zero.
  It now explicitly says "nef rational-model approximable in degree zero
  iff one such metric exists." **Closed.**
- Appendix L originally stated that positive-degree metrics admit the
  approximation, without repeating the continuous locally CLD-psh
  hypothesis. That hypothesis is now explicit. **Closed.**
- The inventory's current-theorem summary now explicitly identifies a
  continuous locally CLD-psh metric before listing the degree branches.
  **Closed.**

These are changes to the author's live explanatory summaries, not changes
to either frozen theorem or proof. No independent theorem defect was
discovered in this bounded integration review.

## Receipt, build and provenance boundaries

The two production receipts were read, and their exact principal hashes,
request/response/header hashes and item identifiers were checked against
the recorded files. A's `EXACT_CURRENT_AUDIT.json` reports PASS and matches
the current principal bytes. The author reports having rerun the strict
exact-current reconstruction for both A and B with PASS; this integration
audit does not claim to have rerun that protocol or submitted production.
A's item is `pi_4592d7150e75755585cdfa20`, run
`20260830T234536Z_5158fe639988`; B's successful retry item is
`pi_f2b822c25aa05cfebdd8bcc0`. The Appendix L and inventory descriptions
match the receipts: gpt-5.6-sol / xhigh, final correct, zero critical errors
and zero gaps. The old B timeout is not represented as a successful run.

The observed prior complete book build had 3474 pages. Its recorder and
auxiliary labels confirm that A/B were loaded and assigned distinct
theorem/equation labels. A further author rebuild was in progress after
the summary edits, so this report does not bind a final PDF hash, certify
post-edit pagination, or claim final-page visual clearance. The author is
handling that separate check. No book compile or live generated-file write
was run by this auditor.

The PDF skill was used for direct visual verification of CLD pp. 498-500;
the source definition and the two distinct source questions were checked
from the rendered pages, not inferred from a citation label. The examined
live and principal TeX files passed a C0/DEL control-byte scan. The author
reported that the prior completed build had no overfull, undefined or
citation warnings, apart from the relative document-class path warning.
That reported historical check is not a certificate for the ongoing final
build.

This is an independent source-integration check relative to the frozen
accepted A/B mathematical packets. It creates no novelty or priority claim,
no proof-assistant certificate, no external acceptance, and no authorization
to apply the results outside their displayed hypotheses.
