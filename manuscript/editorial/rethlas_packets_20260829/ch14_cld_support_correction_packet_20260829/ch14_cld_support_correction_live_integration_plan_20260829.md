# Line-anchored live-integration plan for the CLD support correction

Date: 29 August 2026

Status: **PREPARED, NOT AUTHORIZED FOR LIVE APPLICATION**.  At the time this
plan was written, the production retry was still running.  Apply no live edit
unless the parent task records a final production verdict `correct`, with zero
critical errors and zero gaps, for the exact frozen statement and proof.

No live file was edited while preparing this plan.

## Snapshot on which the line anchors are based

- `manuscript/parts/part2/ch14_currents.tex`, SHA-256
  `a3127a670613678e1bc9c950f37e6ef5e9c297711db8f195386d04579ca9d6b0`;
- `manuscript/bibliography/NonArchimedean.bib`, SHA-256
  `0f88c0fa4e9e5ed5baf308dc53771c1ce111e32670064e4892b9069285ae6777`;
- `manuscript/appendices/appL_provenance.tex`, SHA-256
  `f0a9d19b432daac73bfdb8b79bab0ae5e01e30385757ceb59231c3e00f6aea88`;
- `manuscript/editorial/rethlas_verified_results.md`, SHA-256
  `747b701e61f953f7c4f68f7d7e82e30bd81ef708b8c4eb043bbbb49e33e090a4`.

Appendix L and the verification ledger already contained concurrent P21.3
edits at this snapshot.  Re-anchor by labels and headings, not by blindly
applying numerical line offsets, if either digest changes.

The controlling frozen packet remains:

- statement SHA-256
  `2b291fc55872ab32d40fa3a67e9a9308fc12ac9726113b48950d0a9e50cfd8c1`;
- proof SHA-256
  `9f21f7ece49c761d3f19c07acd8b56e48e9939be493e0bbbd39c0a4d3176e668`;
- independent hostile audit SHA-256
  `62520258d3a5a4d6e73a3d7f9d0dfd8679586ec718d03acf4f32bebcabe7adaa`.

## 1. Chapter 14: replace the unsupported block

Target:
`manuscript/parts/part2/ch14_currents.tex`.

### 1.1 Replacement range

On the snapshot above, replace lines **2888--2963**, beginning with

```tex
\begin{theorem}
\label{thm:cld-positive-support}
```

and ending with the `\end{remark}` carrying
`rem:ch14-support-route`.

The old lines 2897--2926 assert a Berkovich/chart ball-growth estimate
`||T wedge alpha||(B(a,r)) <= C r^p` that is not the proof supplied by the
cited source.  Delete that argument completely; none of it should survive in
the replacement.  The old lines 2928--2935 also cite the printed statement of
CLD Corollary 16.8.6 without detecting its index error and must be replaced.

### 1.2 Live statement structure

Insert one unnamed `theorem` environment, with **no optional theorem name**.
Preserve the existing canonical live label

```tex
\label{thm:cld-positive-support}
```

because it is referenced at current line 3256.  Adapt the exact frozen theorem
into two enumerated assertions:

1. the nontrivially valued arbitrary positive-closed-current assertion, with
   `p` explicitly declared to be the bidimension and with total-variation
   conclusion `|T wedge alpha|(A)=0`;
2. the trivially valued Bedford--Taylor assertion, with `q` explicitly the
   number of curvature factors, complementary form degree `(n-q,n-q)`, and
   Hausdorff exponent `H^(n-q)`.

Use the frozen item and equation labels unchanged:

```text
itm:ch14-cld-support-corrected-nontrivial
itm:ch14-cld-support-corrected-trivial
eq:ch14-cld-support-corrected-nontrivial
eq:ch14-cld-support-corrected-bt-current
eq:ch14-cld-support-corrected-trivial
```

Do **not** introduce the quarantine-only theorem label
`thm:ch14-cld-support-corrected-packet` into the live book.  In the frozen
proof, translate its one self-reference to `thm:cld-positive-support`.  This is
a cross-reference-only adaptation and prevents two canonical names for one
live theorem.

### 1.3 Proof placement and exact mathematical content

Place the proof immediately after the theorem.  Carry over the frozen proof's
mathematical content in full, including all displayed equations and every
`\eqref`.  Preserve these presently collision-free proof labels:

```text
eq:ch14-cld-support-boundary-separation
eq:ch14-cld-support-alpha-tropical
eq:ch14-cld-support-omega-U
eq:ch14-cld-support-proper-tropicalization
eq:ch14-cld-support-pushed-current
eq:ch14-cld-support-measure-pushforward
eq:ch14-cld-support-p-equals-n-minus-q
eq:ch14-cld-support-shilov-null
eq:ch14-cld-support-gauss-moment-comparison
eq:ch14-cld-support-upstairs-null
eq:ch14-cld-support-shilov-support
eq:ch14-cld-support-gauss-pushforward
```

Required proof checkpoints, which must remain visible after any editorial
adaptation:

- `Omega` is the complement of the tropicalized analytic boundary and
  `U -> Omega` is proper;
- the Euclidean current has bidimension `(p,p)`, hence Lagerberg bidegree
  `(N-p,N-p)` and Hausdorff exponent `p`;
- the return from the target uses the ordinary pushforward of a positive
  Radon measure, so no signed cancellation is hidden;
- the arbitrary smooth form is handled by its symmetric/antisymmetric split
  and local difference-of-positive-forms decomposition;
- in the trivial case, `p=n-q` is displayed before applying the nontrivial
  assertion upstairs;
- CLD Lemma 16.8.7 is used coordinatewise to preserve Hausdorff nullity on the
  Shilov image;
- CLD Proposition 16.8.2 gives support on `sigma(X)`, and Proposition 8.7.5
  gives the exact pushed-forward measure.

Use `\cite[Corollary~4.1]{Lag12Super}` for the Euclidean support theorem and
retain the parenthetical identification with Corollary 3.5 in
arXiv:1008.2856v1.  Keep all differentials in the book's `\dprime`,
`\ddprime`, `\dprimeddprime`, or `\rd` conventions; do not introduce a plain
italic differential `d`.

### 1.4 Index remark and diagnostic proposition

After the theorem proof, insert the frozen unnamed `remark` with label

```tex
\label{rem:ch14-cld-support-corrected-index}
```

It must say that `p` in the first item is a bidimension, `q` in the second item
counts curvature factors, and the printed `H^q` in CLD Corollary 16.8.6 is an
index error; the forced exponent is `H^(n-q)`.

Then insert the frozen unnamed `proposition`, again with no optional
conventional name, using labels

```text
prop:ch14-cld-support-printed-exponent-counterexample
eq:ch14-cld-support-kink-dirac
eq:ch14-cld-support-kink-test
```

and its full proof on the trivially valued analytic torus.  The proof must
retain:

- the convention `tau=log|z|`;
- the lattice-degree-one Gauss skeleton;
- the positive slope jump `1-0`;
- compact support of the test function, eliminating both boundary terms;
- absence of curvature on residual branches where the potential is locally
  constant;
- `H^1`-nullity of the singleton and its curvature mass one;
- the final observation that the singleton is not `H^0`-null.

For the best exposition, the displayed two integrations by parts may point to
`\cref{ex:ch14-convex-corner-restated}`, current lines 1080--1093, but do not
delete the analytic-skeleton and support argument.  If exact frozen-to-live
traceability is preferred, retain the full frozen calculation; duplication of
the one-line tropical calculation is mathematically harmless.  Do not claim
an exact-live byte-identity gate if this shortening is made.

### 1.5 Preserve the old route label as a compact compatibility remark

The only live reference to `rem:ch14-support-route` is in the source notes at
current line 3506.  Preserve the label in a short unnamed remark after the
counterexample:

```tex
\begin{remark}
\label{rem:ch14-support-route}
The first proof above is the proper-tropical-pushforward route of
\cite[Theorem~16.8.5]{CLD25}; its only Euclidean support input is
\cite[Corollary~4.1]{Lag12Super}.  It asserts no local Berkovich ball-growth
estimate.  The second proof uses the Gauss--Shilov mechanism of
\cite[Proposition~16.8.2, Proposition~8.7.5, Lemma~16.8.7, and the proof of
Corollary~16.8.6]{CLD25}, with the Hausdorff exponent corrected as in
\cref{rem:ch14-cld-support-corrected-index}.
\end{remark}
```

If the citation syntax with four locators does not format cleanly, split it
into two citations.  Do not restore the old optional title “The route taken in
the source, and the imported input”; the unnamed environment better respects
the book's no-conventional-theorem-name policy.

### 1.6 Other line-anchored Chapter 14 edits

On current lines **77--81**, replace the unkeyed-input wording by:

```tex
\item Lagerberg's Euclidean vanishing theorem for positive closed
  supercurrents, \cite[Corollary~4.1]{Lag12Super}, used through
  \cite[Theorem~16.8.5]{CLD25};
```

At current lines **2885--2886**, change the section transition so that it says
the section records the support results needed later **and diagnoses the
Hausdorff index in the scalar-extension case**.  This is optional prose but
improves the transition to the new proposition.

At current lines **3465--3469**, retain the source summary but change “the
nontrivially valued hypothesis in the support theorem” to “the nontrivially
valued hypothesis in the arbitrary-current clause of the support theorem.”
The corrected Bedford--Taylor clause does cover a trivially valued field.

At current lines **3497--3501**, replace the final support attribution with
precise wording:

```tex
The arbitrary-current support assertion is
\cite[Theorem~16.8.5]{CLD25}.  The trivially valued Bedford--Taylor assertion
uses \cite[Proposition~16.8.2, Proposition~8.7.5, Lemma~16.8.7, and the proof
of Corollary~16.8.6]{CLD25}, with the exponent correction explained in
\cref{rem:ch14-cld-support-corrected-index}.
```

At current lines **3503--3513**, change the paragraph heading from
“An unkeyed reference” to “The Euclidean support input” and replace the prose
citation by

```tex
\cite[Corollary~4.1]{Lag12Super}
```

adding that this is Corollary 3.5 in arXiv:1008.2856v1.  Delete all statements
that Lagerberg “has no key” in the book bibliography.

The dependency-table reference at current lines **3255--3258** remains valid
without editing because `thm:cld-positive-support` is preserved.

## 2. Bibliography

Target:
`manuscript/bibliography/NonArchimedean.bib`.

After the `CLD25` entry ending at current line **304**, add the exact
`Lag12Super` entry from
`ch14_cld_support_correction_bibliography_addition_20260829.bib`.

The key, DOI, arXiv identifier, journal, volume, issue, pages, and year were
checked against the frozen sources.  A repository-wide search found no other
`Lag12Super` key and no duplicate Lagerberg entry in either live bibliography.

## 3. Appendix L provenance

Target:
`manuscript/appendices/appL_provenance.tex`.

### 3.1 Section introduction

Current lines **1144--1148** describe only first-draft results and the
Darvas--Xia trace reconstruction.  Amend them to say that the ledger also
records the sourced CLD support-index correction in Chapter 14, and that
source reconstructions/corrections are not novelty or priority claims.

### 3.2 New provenance row

Insert a new `\AppLProvenanceRecord` immediately before the existing “CLD
multiplication criterion” row (currently lines **1268--1272**), or immediately
after the current curve-regularization row if concurrent edits move that
anchor.  Proposed fields:

```tex
\AppLProvenanceRecord
  {CLD support exponent and Gauss-point diagnostic}
  {\cref{thm:cld-positive-support,%
   rem:ch14-cld-support-corrected-index,%
   prop:ch14-cld-support-printed-exponent-counterexample}}
  {The arbitrary-current assertion is
   \cite[Theorem~16.8.5]{CLD25}.  The trivial scalar-extension mechanism is
   from \cite[Proposition~16.8.2, Proposition~8.7.5, Lemma~16.8.7, and the
   proof of Corollary~16.8.6]{CLD25}.  A product of q curvature factors has
   bidimension (n-q,n-q), so the printed H^q exponent must be read as
   H^(n-q).  The analytic-torus kink supplies the diagnostic counterexample.
   The exact frozen statement/proof SHA-256 are [full hashes]; independent
   hostile-audit SHA-256 is [full hash]; production [run/item/receipt after a
   correct verdict] returned final correct, zero critical errors, and zero
   gaps.  This is a sourced theorem, an internally diagnosed source index
   correction, and a diagnostic example; no novelty or priority claim is
   made.}
```

Render all mathematical expressions in LaTeX in the actual row.  Fill the
production run identifier, item identifier, materialized hashes if any, and
receipt path only from the final controlling response.  Do not call this a
new theorem or add a `RETHLAS-NEW` marker.

## 4. Verified-results ledger

Target:
`manuscript/editorial/rethlas_verified_results.md`.

### 4.1 Header consistency

The file already contains a 29 August entry but its heading at current line
**12** still says “through 28 August 2026,” and current line **34** says
“25--28 August addenda.”  Change these to “through 29 August 2026” and
“25--29 August addenda.”  Do not alter the historically accurate count of the
nine 24 August gates in lines 15--24.

### 4.2 New receipt entry

After the existing “Chapter 16 — direct trivially valued curve
classifications” entry ending at current line **993**, and before the
Darvas--Xia non-receipt entry, add:

```markdown
## Chapter 14 — CLD support exponent and Gauss-point diagnostic

- Status: **VERIFIED FROZEN SOURCE-CORRECTION PACKET / INTEGRATED
  ADAPTATION** (29 August 2026).
- Book locations: `thm:cld-positive-support`,
  `rem:ch14-cld-support-corrected-index`, and
  `prop:ch14-cld-support-printed-exponent-counterexample`.
- Source boundary: the arbitrary-current result is CLD Theorem 16.8.5;
  Proposition 16.8.2, Proposition 8.7.5, Lemma 16.8.7, and the proof of
  Corollary 16.8.6 give the trivial Gauss--Shilov extension.  The printed
  exponent in the corollary is not used as written.
- Exact result: a bidimension-`(p,p)` positive closed current does not charge
  tropically `H^p`-null closed sets after wedging with a smooth `(p,p)`-form
  over a nontrivially valued field.  For `q` curvature factors over a trivially
  valued field the correct exponent is `H^(n-q)`.  On the trivially valued
  analytic torus, `d'd'' max(0,log|z|)` is the unit Dirac mass at the unit
  Gauss point, disproving the printed `H^q` assertion when `n=q=1`.
- Exact frozen statement SHA-256: [statement hash].
- Exact frozen proof SHA-256: [proof hash].
- Independent hostile-audit SHA-256: [audit hash].
- Production run/item/materialized digests: [fill only from controlling
  final-correct response].
- Verdict: `gpt-5.6-sol`, `xhigh`, final `correct`, zero critical errors and
  zero gaps.
- Scope firewall: this does not extend the arbitrary-positive-current theorem
  to trivially valued fields; the trivial assertion is only for continuous
  dpsh Bedford--Taylor products.  It corrects an index and replaces an
  unsupported live proof sketch; it makes no novelty or priority claim.
- Controlling receipt: [exact repository-relative path].
```

Use “integrated adaptation,” not “exact-live byte-identity,” unless a separate
post-integration extraction is submitted and passes.  The frozen receipt alone
does not certify later editorial changes to labels or duplicated prose.

## 5. Collision and editorial-risk audit

### No collisions found

- Existing live label `thm:cld-positive-support` occurs once and has one
  downstream `\cref`, at the dependency table.
- Existing live label `rem:ch14-support-route` occurs once and has one
  downstream `\Cref`, in the source notes.
- All 21 other labels proposed from the frozen packet occur zero times in live
  parts and appendices.
- Bibliography key `Lag12Super` occurs zero times in the live bibliography.
- The counterexample label and all new equation labels are unique.

### Risks that must be actively avoided

1. **Source misattribution.**  Do not cite the printed statement of CLD
   Corollary 16.8.6 as if its `H^q` exponent were correct.  Cite its proof and
   the supporting propositions with an explicit correction notice.
2. **Letter collision.**  Never use the same `p` simultaneously for number of
   curvature factors and bidimension.  Keep `q` for factors and `p=n-q` in the
   scalar-extension proof.
3. **False scope enlargement.**  The trivially valued clause does not cover an
   arbitrary positive closed current.
4. **Unsupported ball growth.**  Delete, rather than soften, the present
   `C r^p` Berkovich/chart estimate.  The valid proof is proper tropical
   pushforward plus Lagerberg.
5. **Signed cancellation.**  Keep the positive-form reduction and ordinary
   positive-measure pushforward before returning from the tropical target.
6. **Counterexample normalization.**  Keep `log|z|`, slope jump `+1`, identity
   lattice degree one, compact test support, and the fact that a singleton is
   not `H^0`-null.
7. **Theorem naming policy.**  Use unnamed `theorem`, `proposition`, and
   `remark` environments.  Do not add optional conventional names that are not
   established in the literature.
8. **Receipt overclaim.**  A frozen-packet pass supports “verified frozen
   packet / integrated adaptation,” not an exact-live claim.
9. **Concurrent edits.**  Appendix L and the verification ledger are already
   modified in the working tree.  Patch by stable anchors and review the diff;
   never overwrite or blanket-stage them.

## 6. Validation after a permitted integration

1. Recompute the two frozen hashes before copying any content.
2. Search all live sources for `16.8.6`; every occurrence must either use
   `H^(n-q)` or explicitly describe the printed index error.
3. Search for `ball-growth`, `C_\\alpha r^p`, and the old prose “unkeyed
   reference”; none should remain in Chapter 14.
4. Search labels and bibliography keys for duplicates.
5. Compile the whole book twice and require no undefined references,
   undefined citations, overfull boxes, or errors attributable to the patch.
6. Visually inspect the pages containing the two-item theorem, the index
   remark, the Gauss-point proposition, the source notes, and the Appendix L
   row.
7. Record the post-integration Chapter 14 hash and, if exact-live status is
   desired, submit an extracted live statement/proof packet separately.
8. Stage only the explicitly intended live files and controlling audit/receipt
   artifacts; do not use blanket staging in the dirty worktree.
