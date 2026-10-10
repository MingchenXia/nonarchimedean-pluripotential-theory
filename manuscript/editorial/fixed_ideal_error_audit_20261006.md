# Fixed ideal errors and conditional entropy convergence

**Known argument import and conditional explanation.** The controlling
baseline is `0b3601f56e83d5fb37b87f96ac459e731bc430ac`.
Chapter 46 now explains the elementary graded/antigraded calculation
from Boucksom's appendix, Lemma A.7 in Trusiani's
[arXiv:2605.30063v2](https://arxiv.org/abs/2605.30063v2), revised
17 August 2026 at 08:55:46 UTC. Chapter 68 uses it to identify the
remaining conditions for entropy convergence. Appendix L records the
source and admission boundary. No full special-Fujita, entropy
regularization or YTD theorem is admitted.

## What the argument proves

The exposition works with integral invariant coherent ideals on the
smooth complex projective model already used for the ample-generic
moving-part construction. Their cosupport is in the central fibre.
The first sequence is graded, the second is antigraded, the first is
contained in the second, and a fixed effective vertical Cartier divisor
and fixed positive integer shift give the displayed shifted inclusion.
At each normalized Gauss valuation, integral ideals have nonpositive
logarithms; vertical ideals have finite values because they contain a
power of the central parameter. Multiplication of ideals is additive
under valuation. These are the complete inputs to the elementary proof.

Fekete's argument gives a finite nonpositive asymptotic value for the
graded sequence. Inclusion in the antigraded sequence bounds this value
above by each normalized antigraded value. The shifted inclusion and
nonpositivity then bound the difference of the two logarithms by twice
the fixed model function. The strict range `m>m0` keeps every shifted
index positive. The proof does not assert monotonicity of the entire
integer sequence of normalized base-ideal functions.

The integrated conclusion has separate hypotheses: weak convergence
of probability measures, a continuous nonnegative fixed model function
with zero integral against the limit, and a nonnegative measurable
discrepancy error bounded almost everywhere by a fixed nonnegative
constant times the ideal error. Its integral tends to zero by testing
weak convergence against that one continuous function. If the entropy
expressions have a separately established decomposition into this error
and an integral of a continuous reference function, their values converge.
The ideal estimate supplies neither that decomposition nor the
discrepancy bound or zero limiting integral. Without the last vanishing
condition it gives only a bounded error.

Section 46.3.7 and equations (46.10h)–(46.10j) give these calculations.
Section 68.14 retains its three separate approximation inputs and now
points to this conditional mechanism. Appendix L.52 distinguishes the
formal ideal calculation from the additional geometry in Proposition
A.6, whose setting is an ample polarization over `k((t))`, with `k`
algebraically closed of characteristic zero. The general trivially
valued Siu/closure boundary is unchanged.

## Primary-source reading reused

The preceding [special-Fujita source review](special_Fujita_source_review_20261006.md)
read and displayed all 25 actual PDF pages of Trusiani v2, including
its complete proof, appendix and references. Lemma A.7 and its proof
are on actual page 21. Proposition A.6 starts on page 20 and ends
with the fixed-error argument on page 21. The controlling PDF has
SHA-256 `aa00afeb58947e0f839d5f1af752c83c429b407d387166b624cb3f6315589712`.
The full-reading record has SHA-256
`b9a1f7856f4d59afdc74be84a3bbff3dac1f7b0b7c4e1d4cada8f0c9d5e1976c`.

The same review displayed and read 55 selected pages from DEL v2,
Li–Fujita v1, Li–geodesic v4, the archived BFJ author edition and BJ's
September 2025 v1. The selected-reading record has SHA-256
`840b3a5147d40bd72cc765eafbde396c66a764b2e4521b731590fc931d7e225a`.
Those records and exact files are reused here, not counted as fresh
primary reading. No full reading of the five dependencies or full
clearance of their Calabi–Yau, envelope/support or weighted analytic
antecedents is claimed. The existing `Trusiani26` bibliography entry
already specifies the controlling v2 and remains byte unchanged.

The preceding review's literal formula and printed-step defects remain
visible. This integration does not certify complete repairs to the
effective-divisor scalar supremum, analytic normal-direction claim,
canonical-pullback conventions or relative ample construction. It makes
no counterexample claim about corrected main theorems.

## Validation and matching PDF review

The final book has **4,384 pages**, 20,371,719 bytes and SHA-256
`6003565df674c7c1573434906efa3bd5c1ee105e51210f181bfd82122e189bbd`.
The first draft compiled but produced two overfull boxes from the
unbreakable arXiv identifiers in the new provenance paragraph.
Explicit breakpoints fix them. Its PDF, displayed layout diagnostic,
source gate and build log are retained as historical artifacts; none
is promoted to the final release. The final source gate is v2.

The final build has zero TeX errors, package/pdfTeX warnings, unresolved
references or citations, missing characters, overfull boxes or rerun
requests. Its 954 nonfatal underfull diagnostics match the baseline.
The post-render reference check finds 425 active inputs, 12,827 unique
labels, no missing inputs, duplicate labels or dangling references.
There are 371 used bibliography keys among 666 available keys, with
zero bibliography warnings. No new bibliography or index key is added.

All 764 index entries are accepted, with zero rejected entries or
index warnings. The 763 index page groups and 419 distinct numeric
destinations are valid. PDF navigation has 21,917 named destinations,
46,991 internal links, 171 external URL links, 2,556 contents entries
and six parts, with no invalid internal link, named destination or
contents page.

All **45 matching final PDF pages** were displayed and their extracted
passages reread, in twenty-three sheets: actual pages 47, 61, 68,
2741–2744, 3631–3635, 4145–4149 and 4357–4384. They cover affected
contents, the complete new ideal calculation, its preceding and following
transitions, the stability comparison and dated scope statement, the
new provenance and following appendix opening, and the complete index
and bibliography. The corrected page 4147 was displayed in
the final review after the earlier draft layout diagnostic. The image
manifest has SHA-256
`915d9c7aac3ca015cb6f4d561d2f7f23b12fa23034fd6169e811e2652c45f54b`.
This is a scoped final-edition review, not a fresh rereading of every
book page. The ordered whole-book second reading remains the completed
4 October checkpoint.

## Preservation and publication

Only Chapters 46 and 68 and Appendix L change within the 425 active
inputs. All 422 other active inputs and 108 protected inputs retain
their baseline hashes. The edited files retain 101 existing statement
and explanatory environments and 40 existing proof environments,
141 blocks in total, byte-for-byte; no formal result environment is
added or relabeled. Five new labels and three new equation tags are
distinct. README and the programme record the continuation.

All 54 prior frozen manifests, including four separate source-only
reviews, and all 106 prior exports retain their bytes. The other 5,019
tracked baseline files are unchanged. The 42-row canonical inventory
passes with twelve families and tier counts 0/3/7/15/17. All complete
statuses, the open toric research candidate and native catalogue source
and PDF remain unchanged. The native editor stays open; no native
compilation or tab change is claimed.

The release contains the full PDF, a 45-page review PDF and a source
archive with 631 members. Every archive member is checked against the
saved source bytes, its CRC is checked, and all 425 active inputs are
included. No fresh isolated archive compilation is claimed. The
integration manifest, closure hashes and artifact record make the
release reviewable. Cloud GitHub synchronization uses the existing
work branch and PR, explicitly fetches main and work, and makes no
force push or main-branch update.

This is an imported elementary argument and its direct conditional
integral consequence. No original result, independent production model
call, new verification receipt, canonical solved status or general
Siu/closure repair is claimed. Continue with the fixed-divisor trace
argument and the projection and relative-polarization requirements.
