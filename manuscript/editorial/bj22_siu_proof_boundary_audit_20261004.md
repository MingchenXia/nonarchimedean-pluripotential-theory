# BJ22 critical Siu division: proof and dependency correction

Date: 4 October 2026. Baseline: `ea6d1ea`. The author's warning about
Boucksom–Jonsson (2022), Theorem 6.21, prompted a priority primary-source
and dependency check. The book now treats critical homogeneous Siu
division as an explicit additional assertion `(SD)_k`. The general
envelope assembly and deductions through that route are conditional.
This corrects a foundational source assumption; it does not disprove the
division theorem or promote a new mathematical result.

## The failed inference and its exact scope

The controlling source is *Global pluripotential theory over a trivially
valued field*, Ann. Fac. Sci. Toulouse 31 (2022), 647–836,
DOI [10.5802/afst.1705](https://doi.org/10.5802/afst.1705).
Theorem 6.21 and its proof are on printed pages 736–737, physical
pages 91–92 of the cached published PDF including its cover.
Both actual pages were viewed. The extracted theorem/proof and adjacent
corollary were freshly read at lines 4310–4395 of the pinned text.

In the approximation, homogeneous Fubini–Study functions `psi_a`
decrease, `psi_a <= t_a log|s_E|`, and rational `t_a` tend to 1.
The residuals `rho_a = psi_a - t_a log|s_E|` need not decrease.
On `K_E = {log|s_E| = -1}`, the required inequality is
`t_b-t_a <= inf(K_E)(psi_a-psi_b)` for `b >= a`.
The displayed approximation bounds and Dini's lemma do not imply it.

For example, on the projective line let `E=p`, `ell=log|s_p|`,
`psi_n=(1-1/(2n))ell`, and `t_n=1-1/n`, for `n>=2`.
Then `psi_n` decreases to `ell` and `psi_n <= t_n ell`, while
`rho_n=ell/(2n)` increases where `v(p)>0`. The limiting residual here
is still the psh function zero. This arithmetic example refutes the
monotonicity inference, not the assertion of Theorem 6.21.
Pointwise convergence of these divisorial residuals alone does not
license application of decreasing psh closure.

The strict hypothesis `psi <= t_0 log|s_E|`, `t_0>1`, has a separate
fixed-coefficient argument in Chapter 35. Its entire existing statement
and proof remain byte-identical. No subtraction of two infinite values
at proper support is used to define a residual: the requested conclusion
is an additive identity on the whole analytification, with uniqueness
supplied by divisorial determination.

## Independent published regimes and circularity

The 2024 *Addendum to “Global pluripotential theory over a trivially
valued field”*, DOI [10.5802/afst.1775](https://doi.org/10.5802/afst.1775),
Theorem A proves the envelope property independently for smooth varieties
in characteristic zero or dimension at most two. Its standing hypotheses,
statement, proof and adjacent consequences were freshly read in the
cached text at lines 1–225 and 418–548. Physical pages 10–11, containing
the end of the proof and its consequences, were actually viewed.
Corollary 2.3 itself cites original BJ22 Theorem 6.31 and does not furnish
an independent repair of division on arbitrary normal varieties.

Proposition 17 of *Non-Archimedean Green's functions and Zariski
decompositions* (2024), DOI
[10.5802/crmath.579](https://doi.org/10.5802/crmath.579), uses an
independently known envelope property under that paper's smooth
characteristic-zero standing hypotheses. Its statement and complete proof
were freshly read at lines 610–714, together with the standing scope and
envelope inputs at lines 1–125, 241–268 and 575–607. Physical page 13
(printed page 16) was actually viewed. The fixed-`t<1` division followed
by increasing-envelope closure is valid in this independently established
regime. It cannot be used as an input to prove the same envelope property
in the general normal case. These targeted checks do not assert an
exhaustive current-literature search or fresh verification of every
antecedent cited by the papers.

## Book interfaces and historical evidence

Chapter 35 states `(SD)_k` for every normal integral projective variety
over the standing field, every real numerical class, every effective
rational Cartier divisor, and a homogeneous psh function bounded above
by its section function. Nine principal interfaces explicitly display
this extra input: general division, the final envelope theorem, real
Cartier realization, the Cartier psh criterion, homogeneous and carrier
reflection, their diagram, finite normal descent, and normal envelopes.
Chapter warnings make deductions through these interfaces conditional.

The affected chain is critical division → Chapter 38 realization →
Chapter 39 reflection → Chapter 41 analytic finite descent → Chapter 42
normal envelopes → Chapters 37/45 general unibranch envelopes → later
uses that discharge an envelope hypothesis through this assembly.
The algebra of determinants, formal pullback, topological normalization,
and the fixed strict-division argument are distinguished from these
analytic dependencies. Chapters 43–44's general envelope consequences
inherit the preceding conditional input through their normal source.

Chapter 40 remains byte-identical to the baseline. Its direct smooth
proof uses generated stages and comparison, the Chapter 38 two-gradings
and drift bookkeeping, Chapter 39's separately proved determination
package, and Chapter 41's formal pullback and real-weight compatibility;
it does not invoke critical realization or reflection. The source audit
therefore does not add `(SD)_k` to this separate proof or claim a fresh
independent production verification of all its antecedents.

The preface, Part IV introduction and Appendix L now state the conditional
boundary. Historical August dossiers, dated source audits and verifier
receipts remain unchanged. Their exact packets are not extended to this
revision. No new independent model call, Rethlas receipt, solution,
priority claim or theorem counterexample is recorded.

The standalone catalogue adds a full description of this foundational
proof issue, its known independent regimes and the noncircular repair
target, separately from the unchanged 42 atoms in twelve formal problem
families. All original formal statements and proofs in the catalogue
remain byte-identical. The earlier 85-page PDF is preserved separately.

## Verification and saved edition

After the Chapter 40 dependency correction, the required full build
passes: **4,253 pages**, 425 active TeX inputs, 12,590 unique labels.
Ten active sources change; 415 and all 108 protected Appendix M–N inputs
remain hash-identical. Eight labels are added; no numbered theorem,
proposition, lemma, corollary, definition, example or remark is added.
Old label order is preserved. All six reference-checker regressions and
the 42-atom inventory check pass. The final log has zero TeX errors,
LaTeX/package warnings, unresolved references/citations, overfull boxes
or rerun requests; 954 underfull diagnostics remain recorded.

The standalone source compiles successfully in the built-in editor.
The separate cloud export has **86 pages**, zero errors, unresolved
references, package warnings, overfull boxes or rerun requests, and one
underfull diagnostic. The editor-open request was queued; this does not
claim confirmed UI visibility or that the shell export came from the UI.

The final book's scoped actual-page review covers **107 pages**: 40 reuse
pixel-identical actual views and 67 were freshly viewed. It includes the
conditional interfaces, warnings, changed seams, preface, Part IV
introduction, affected contents, and complete index and references.
Twelve selected catalogue pages and five selected primary-source pages
were also actually viewed. All 31 book/catalogue contact sheets are
accounted for, with no clipping or collision observed. No fresh whole-book
or whole-catalogue visual review is asserted.

Navigation finds zero invalid targets among 21,430 named destinations,
46,127 internal links and 2,433 contents/bookmark entries. All 724 index
page groups resolve to 395 distinct destinations. The 163 external URL
links are counted without claiming remote target health. Post-render
references, exact source hashes, formal catalogue preservation, inventory
and whitespace checks are recorded separately from successful compilation.

The [manifest](bj22_siu_proof_boundary_manifest_20261004.json),
[source ledger](bj22_siu_proof_boundary_source_closure_20261004.sha256),
and [artifact record](bj22_siu_proof_boundary_artifacts_20261004.json)
pin this edition. Full book, selected-page reviews and source archive
are saved under `/workspace/book-completion-drafts/research-integration/`.
Earlier artifacts stay historical. Archive input-byte verification does
not claim a fresh build from the archive or bundled-font portability.
Normal publication to `work`, incoming-user-research checks and subsequent
related-paper exploration continue in the cloud; Xean setup stays suspended.
