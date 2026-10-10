# Sylvester local-model integration — 4 October 2026

Chapter 5 now contains Example 5.5.4, a known-source worked application
of coherent unimodular Sylvester triangulations to normalized monomial
models. It follows the projective-subdivision construction, after the
chapter has introduced integral affine lattices. Appendix L records its
exact provenance, and the bibliography adds two version-pinned entries.
The current full book has **4,246 pages**. No open-problem status changes.

## Mathematical and source scope

The geometric input is Ambro, arXiv:1310.3951v2, Proposition 3.7, in the
normalized cyclic-cover section. The version's actual header is dated
9 October 2015; this arXiv version, rather than an uninspected journal
edition, controls the citation. Its earlier ordinary-root discussion is
not substituted for normalized toroidal roots. The triangulation input
is Caicedo–Castillo–Juhnke–Poullot, arXiv:2609.23710v1, Theorem 3.5,
physical page 11, submitted 20 September 2026. The source proof uses
integral chimneys and a one-point extension with one visible facet at
primitive lattice distance one. The preceding ordinary audit checks that
specific construction and the required existence of coherent full
pulling refinements, while recording two overbroad auxiliary statements
that the application does not use.

The [trait and Sylvester source checkpoint](li_trait_and_sylvester_source_audit_20261004.md)
records the conservative 361-line Sylvester introduction/Section 3.1
reading and five actual primary-page views. The [cyclic-cover checkpoint](li_cyclic_normalization_and_subdivision_audit_20261004.md)
records the reused Ambro scope and actual source pages. The later
Sylvester Ehrhart, unimodality and magic-positivity assertions are not
book inputs. Reading these scoped primary proofs is distinct from
independently rechecking every imported dependency.

The three-dimensional example starts with
t=z_0 z_1^{3(k+1)} z_2^{2(k+1)} z_3 and the cover t=tau^{6(k+1)}.
Its enlarged character lattice and dual congruence lattice compute the
four primitive rays. All have height one, so the normalized central
divisor is reduced, but their span has index 36(k+1), so the unrefined
total space is singular. Projection identifies the height-slice difference
lattice with the full ambient Z^3. This exact lattice identification is
what turns source-unimodular tetrahedra into regular toric cones.
Coherence gives a vertical normalized monomial blowup, and each maximal
chart has tau=u_0 u_1 u_2 u_3. The standard charts also apply over the
completed complex trait. The generic fibre is an affine three-dimensional
torus, with no compact-family or CY metric conclusion.

The exact maximal-cell count 36(k+1) follows from normalized volume.
The displayed higher-dimensional family gives (k+1)(s_d-1)^2, including
the d=1 unit-interval case. Neither count is an enumeration of different
triangulations or a new numerical experiment. This is an explicit
application of known sources and direct lattice/volume consequences;
no new theorem-like statement or independent verifier receipt is claimed.
Compatible global chart choices and preservation of a compact family's
polarization remain separate requirements.

## Integration, build and rendered gates

The changed active book files are Chapter 5, Appendix L and
NonArchimedean.bib. Chapter 5 adds one example and one semantic label.
All pre-existing theorem, proposition, lemma, corollary, definition,
example, remark and proof blocks in the two changed TeX sources remain
byte-identical, and their original label order is preserved. The other
423 of 425 active TeX inputs, including all 108 protected Appendix M–N
inputs, remain hash-identical to the preceding checked edition. Historical
proof receipts and all 42 problem statuses are preserved.

One required full build succeeds. The final log has zero TeX errors,
LaTeX/package warnings, overfull boxes, unresolved references/citations
or rerun requests; the recorded 954 underfull diagnostics remain.
The build's six reference-checker regressions pass. There are 12,581
unique labels, 172 valid reference ranges, 5,457 citation groups and
5,701 citation uses. All 279 cited keys resolve among 578 bibliography
keys; BibTeX reports zero warnings. MakeIndex accepts 722 entries,
rejects none and writes 962 lines with zero warnings.

All **61 selected physical pages in sixteen contact sheets** were
actually viewed. The selected pages include the full new example,
the source and provenance records, adjacent text, changed-unit seams,
affected Chapter 5 and later contents, and the complete index and
bibliography. The first render selected 59 pages; the omitted Chapter 5
contents pages 8–9 were added once without rerendering those 59 pages.
No clipping or collision was observed. This is a scoped visual gate,
not a fresh visual reading of all 4,246 pages or all of Chapter 5.

Navigation checks find zero invalid targets among 21,416 named
destinations, 46,087 internal links and 2,433 contents/bookmark entries.
All 722 index page groups resolve. The 163 external URL links are
counted; remote URL health is not claimed. Post-render reference,
scope, inventory and whitespace gates pass. The inventory remains
42 atoms in twelve families with tier totals 0/3/7/15/17.

The [manifest](sylvester_local_model_integration_manifest_20261004.json)
records exact source, build, navigation and actual-page scopes. The
[source ledger](sylvester_local_model_integration_source_closure_20261004.sha256)
binds the active TeX closure. The full PDF, selected-page review and
source archive are saved separately under
`/workspace/book-completion-drafts/research-integration/`; the preceding
4,244-page edition remains historical. Archive input byte checks do not
constitute a fresh build from the archive or a bundled-font portability
claim. Normal work-branch publication and incoming-research fetches
continue. Further recent-paper reading and remaining global model checks
stay in the cloud, with Xean setup suspended.
