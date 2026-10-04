# Hybrid literature source checkpoint — 4 October 2026

After publication of the checked Lin example, related-paper exploration
continues with an update-sorted arXiv metadata query and Boucksom's
`2510.10239v2`, *From amoebas to pluripotential theory on hybrid analytic
spaces*. Forty metadata titles/version dates were scanned; this is a bounded
query with its literal search terms, not an exhaustive literature search.
The identifier check returns Boucksom v2, updated 16 October 2025. The PDF
header dates the notes 20 October 2025; the two dates serve different roles.

The selected source reading covers text lines 1–220, 350–450, 1450–1687 and
1980–3075. It includes the complete printed Sections 7–8 and Appendix A,
measure-normalization interfaces, selected topological criteria and
references. All fourteen selected actual source PDF pages (8, 43–55) were
viewed. This is not a complete 3,075-line reading, nor certification of all
imported dependencies. No active book source is changed at this checkpoint.

The forward hybrid measure statement (Theorem 7.11) assumes a hybrid
continuous family and continuous fibrewise psh metrics. Theorem 7.16
constructs a maximal continuous extension for specified boundary data;
its model case relies on Reboulet 2023 and is only sketched here. Existence
of this chosen extension does not imply continuity of an arbitrary given
psh family with the same endpoint. Theorem 8.7 assumes maximal essential
dimension and partial retraction invariance. Its global conclusion is
Darvas d1 convergence and a one-sided comparison; Corollary 8.8 gives
smooth convergence on compact subsets of the generic regular region.
Neither statement should be relabelled unconditional global supnorm
convergence.

Several literal auxiliary statements/displays require checking before
reusing this printed proof. The [manifest](hybrid_literature_source_manifest_20261004.json)
records exact pages and counterchecks. The psh Haar-average implication
in Lemma 8.10's proof fails for general psh functions: on z1*z2=1/16,
u=|z1|²+|z2|²+Re(z1) has value 3/8 at (1/4,1/4), whereas its same-log-fibre
Haar average is 1/8. This refutes the stated general implication, not the
special-solution convergence theorem. Lemma A.10 omits normalization/control
of its first potential; constants phi=-R, psi=0 expose that literal omission.
The page 54 density estimate has the large-density inequality in the wrong
direction: identical measures give left side 1 and right side 0. The final
page 55 mean estimate uses integral |f| where the preceding signed-mean
bound controls |integral f|. These are source-checking findings; no principal
theorem is declared disproved and no new independent verifier verdict is
claimed. Dependencies and repaired arguments remain to be checked.

The notes cite Yang Li's `2505.11087` for the subsequent Calabi–Yau
continuity result. A 4 October identifier query returns v1, *Degeneration of
Calabi–Yau metrics and canonical basis*, with no journal reference in that
response. The abstract separates a potential-theoretic convergence claim
for essential dimension 1 through n from an optimal-transport description
under canonical-basis assumptions. Primary checking continues; abstract
claims are not imported into the book. The active 42-atom inventory and
all archived theorem receipts remain unchanged.
