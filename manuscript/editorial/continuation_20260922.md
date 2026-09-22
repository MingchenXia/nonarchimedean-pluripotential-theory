# Continuation and fresh-clone audit — 22 September 2026

## Starting point and current limitation

Work resumed from commit `179c0cdd5697d18e9f5eba985dec286daa09a840`
(`Add affine cross-collar smoothing for two stars`, 20 September 2026),
in a complete fresh clone of the existing private repository. The working
branch was clean and matched `origin/main` before any edits.

**The current Git source does not reproduce the previously recorded full
build.** A fresh `latexmk -pdf -interaction=nonstopmode -halt-on-error
book.tex` terminates in Chapter 70 because this included file is absent:

```
manuscript/editorial/solver_dossiers_20260911/
  p122_curve_ideal_psh_functoriality_20260911/CURVE_PSH.tex
```

The file is not present in any fetched commit under that path. The include
first appears in commit `b944553`, but its target is not included in that
commit. The available source closure has 388 files, rather than the 389
reported by the last full-build receipt. Eight missing labels cause thirteen
unresolved file/label pairs across Chapters 70 and 72. No substitute
proof, dummy labels, or successful full-build claim has been inserted.

The author has been asked for the original editing directory or machine.
Recovery of the original source and its provenance is the first build repair.
The previously published release artifacts and all historical verification
records remain unchanged; their successful builds are historical evidence,
not evidence that this fresh clone currently builds.

## Chapter 16: explicit geometry of the affine collar

Added `ex:p071-cross-collar-corner-coupling` directly after the existing
affine cross-collar smoothing proposition. This is a worked application and
an elementary explanation of its hypotheses, not a new research theorem:

1. Subtract the common affine minorant. The resulting nonnegative convex
   function vanishes at the five vertices of
   `Q = [0,R0]^2 intersect {r+s <= R0+delta}`, hence on all of `Q`.
2. The nine independently chosen nonnegative coefficients in
   `a_ij max(0,r+s-R0-delta)` give admissible mixed terms in the remaining
   corner. A four-point rectangular difference proves nonseparability when
   `a_ij > 0`; zero coefficients cause no exceptional case.
3. The existing proof's geometric tails give the explicit upper error
   `(5/3) 4^(-n)` and the common collar shift `(17/12) 4^(-n)`.

Chapter 72 now points to the example and describes coupling compatible with
the collar. P07.1 remains open. The exact existing statement and proof files
were not edited; their SHA-256 values still equal
`2e538f70b29d2ce359902f5ff16931d750112dc4e6a81903075c08e604b1296e`
and
`396d2be290d6262c68468c0b1e0490bf919ec3e504f4c79edd7797d29593f922`.
Those receipts do not purport to verify the newly added exposition.

## Source-check repair and validation

The former reference checker silently omitted absent inputs and returned
exit status zero even after printing unresolved references. It also missed
lowercase `cref` commands. The checker now reports missing inputs, checks
both reference cases and starred variants, ignores commented TeX, and
returns a failing status for missing files, unresolved or duplicate labels,
or structural defects. Its programmatic `closure()` also refuses an
incomplete graph.

- Six regression checks pass: missing input, missing root, lowercase
  multi-reference, nested includes with comments and escaped percent signs,
  duplicate labels, and unbalanced environments.
- The real repository correctly returns status 1 for its pre-existing
  missing input and thirteen unresolved references. The available closure
  has 11,428 distinct labels, with no duplicate or per-file structural defect.
- The exact open-problem inventory passes: 46 active atoms in 14 formal
  environments; tiers `(0,5,8,16,17)`.
- The new example passes the strict Mingchen writing audit with zero errors
  and zero warnings; a second statement-to-calculation reading confirms the
  collar geometry, nonseparability, geometric sums, and degenerate coefficients.
- A temporary `includeonly` driver compiles Chapter 16 into a 341-page
  diagnostic PDF. Its thirteen external-reference warnings concern chapters
  and appendices unavailable to that scoped build. This is not a full-book
  build or a release. The new example and its internal citations resolve.
- Physical pages 164–167 of that diagnostic PDF were rendered and inspected;
  the example is on physical pages 165–166 (printed pages 832–833), with no
  clipping, overlap, or broken display at the insertion or its transitions.
- `git diff --check` passes.

Temporary build drivers, logs, and PDFs follow the existing ignore rules.

## Chapter 60: relative numerical nefness

The numerical reduction in `thm:mp-model-closedness` now has a detailed
proof using ambient Kähler test classes, fibrewise positivity, base-class
correction, and a uniform shrinking parameter. The normalization in the
polynomial identity is checked explicitly; a printed normalization slip in
the primary source is recorded rather than repeated. The analytic-cycle
core remains an import with its actually checked preprint version specified.

The [source and validation audit](ch60_relative_nef_audit_20260922.md)
records exact published Demailly–Păun locators, the distinction between the
import and the reconstructed reduction, and the second-pass checks. The
84-page scoped Chapter 60 build has no overfull box or unresolved citation;
its two external-reference occurrences are inherited from the scoped
baseline. The revised proof and the energy display were visually checked.
This does not repair the missing Chapter 70 source or constitute a full build.

The follow-up in the same audit now gives the snc model-independence
descent using dominating inverse-image cycles. It retains the normal-model
assertion as an explicit import and corrects the introduction's line-bundle
claim and fixed-background cone terminology. The new proof has passed the
second reading, scoped compilation, source check, and visual inspection.

The Fubini--Study warning now distinguishes rational algebraic line-bundle
models from unrestricted analytic models and records the BJ dominating
ample locus. Appendix I includes the proper-morphism fibre criterion used
in that explanation. The same source audit records the published BJ
locators, second-pass checks, and the unchanged Chapter 71 comparison.

Appendix I's compact dependency table has also passed its layout follow-up:
all 21 rows are preserved, tags print upright, and explicit column spacing
separates the longest statements from the chapter links. The complete table
fits on one page in the final scoped build.

The Chapter 60 maximum proof now specifies the sum ideal, its sign and
denominators, and the fixed-resolution limit proving relative nefness.
The common relative Kähler extension argument has a separate lemma used
by both this proof and the numerical criterion. The final scoped build
has 85 pages and no new unresolved source reference; the source graph has
11,429 labels. The detailed audit records the second-pass checks.

The model-measure pass proves mass one for signed model measures and
nonnegativity for all relatively nef model classes. The deformation-to-the-
normal-cone example now states the required center and rationality
hypotheses and treats point blowups on curves separately. The
[measure and energy audit](ch60_model_measure_energy_audit_20260922.md)
records the second-pass checks and the next energy-domain issue.

The energy pass now gives the weighted intersection-matrix proof of the
Zariski inequality and defines the real model domain before differentiating.
Monotonicity uses the difference of ordered endpoints only as a nonnegative
function; concavity includes dimension zero. The same measure and energy
audit records the source correction and the 87-page scoped validation.

## Next work

1. Restore the missing Chapter 70 source from the original working copy,
   retaining its proof and provenance. Re-run the strict source check and
   a complete LaTeX/BibTeX/MakeIndex build before claiming reproducibility.
2. Continue Chapter 60's approximation and monotone-completion proofs,
   including the connection between real model classes and the completion.
   Numerical nefness, snc model independence, the Fubini--Study warning,
   and maximum stability have received the present detailed passes.
   The arbitrary normal-model assertion remains an explicit import.
3. For P07.1, separately examine continuous convex collar data and the
   production of compatible collars from the stratified comparison
   conditions. No extension beyond the current hypotheses is asserted here.
4. Continue chapter-level mathematical and editorial checks while source
   recovery is pending. Commit and push each coherent checked unit, with
   outstanding limits recorded; no force pushes or changes to visibility.
