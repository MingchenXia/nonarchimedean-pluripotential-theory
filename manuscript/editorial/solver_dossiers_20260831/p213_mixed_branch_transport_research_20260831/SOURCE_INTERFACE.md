# Source interfaces and exact application boundary

Date: 2026-08-31. Author: /root/p081_weighted_repair_fresh. Root supplied the mixed-coordinate cutoff outline; this packet supplies the complete proof and source-support checks. It is new research, not an independent audit of its own proof.

## Standalone scope

The principal proposition concerns an actual standard polyannulus over any finite extension \(L/F\), viewed throughout as an \(F\)-analytic space, where \(F\) is complete and nontrivially valued. Only positivity and \(\mathrm d'\)-closedness are imposed on the ordinary \(F\)-current. Neither discreteness nor perfection of the residue field, tame ramification, separability of \(L/F\), or a source-calibration representation is assumed in this standalone proposition.

The coefficient constructions and equality \(C_T=B_T\) use actual compactly supported source forms. No arbitrary current is pulled back to \(L\), reinterpreted as an \(L\)-current, sliced, or recovered from a target pushforward. In particular, the finite-extension clause is not shorthand for an unproved current base-change interface.

## Primary source

Chambert-Loir–Ducros, *Formes différentielles réelles et courants sur les espaces de Berkovich*, arXiv:1204.6277v2, 25 July 2025. The [official version record](https://arxiv.org/abs/1204.6277v2) was checked on 2026-08-31. The exact mathematical passages were read in the local primary text:

- /private/tmp/CLD25.txt — SHA-256 021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e.
- /private/tmp/CLD25.pdf — SHA-256 5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719; identity recorded, no PDF rendering or visual inspection in this task.

| Locator | Exact interface |
|---|---|
| §7.1.11, p.159 | Compact analytic source support is needed for current tests involving target pullbacks. The proof checks this directly for both moments and the connecting primitive. |
| Proposition 7.2.8, pp.161–162 | Positive scalar functionals and a compact-support sup-norm bound give Radon measures. The candidate supplies this argument explicitly on the Euclidean targets. It does not call the whole analytic bidegree-(0,0) current a Radon measure. |
| §14.3.2, p.407 | Canonical cell calibration is the coordinate volume multiplied by the moment's local degree. For the identity torus coordinates over \(L\), that degree is one. |
| Remark 14.4.3, p.410 | Viewing an \(L\)-analytic space over \(F\) multiplies the canonical calibration by \([L:F]\). The full finite degree already includes ramification; it is not an ordinary-sheet count. |
| Proposition 15.1.1 and Corollary 15.1.2, pp.421–422 | Logarithms of actual analytic units on an ordinary open set furnish ordinary smooth forms. A formal G-cover is not used. |
| §18.1.2, p.501 | Analytic log-unit functions are smooth with zero \(\mathrm d'\mathrm d''\). Only such functions are differentiated. |

These are basic CLD interfaces, not a literature assertion of the new mixed-branch equality. The cutoff cancellation, support analysis, and two signed integrals are proved in this packet. No novelty claim about the broader literature is made.

## Exact application to the previously missed family

The frozen prior note is:

/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260831/p213_product_current_separation_research_20260831/RESEARCH_NOTE.md

SHA-256 d4f1458e0849164c1a45d168238467c13222ccae427493069ed97f43cd789b81.

Its manifest SHA-256 is 2afe7e91903a021751d59da7c02c7be1826dc3dc223a87f256a1482e7f58a440. The complete note, including §§1–4 and the §5.2 mixed diagnostic, was read. Its principal branch theorem is treated as a separate gated input, not independently accepted by the present authoring task.

In that note's scope, \(K\) is a complete DVR with perfect residue field, \(p\) is a closed residual point with \(d_p=[\kappa(p):k]\), and \(N\ge2\) is a unit of the valuation ring. The stated actual source identification is
\[
 D_{p,N}\simeq
 \{0<v(t)<\infty,\ 0<v(w)<\delta\}_{L_p},
 \qquad L_p=K_p(\pi^{1/N}),\quad [L_p:K]=Nd_p,
\]
viewed over \(K\). The prior coefficient formula is
\[
 B_T(p,N)=N b_T(p).
\]

**Conditional application.** Assuming that source identification and the prior branch formula, apply the new proposition with \(F=K\), \(L=L_p\), and \(T\) restricted to the actual source domain. For \(q=w-t\), the new coefficient on
\[
 0<v(t)<\delta,\qquad v(q)>v(t)
\]
is
\[
 C_T(p,N)=B_T(p,N)=N b_T(p),
 \qquad C_{\delta_X}(p,N)=Nd_p.
\]
This is immediate substitution in the proved equality and in the canonical-degree formula; no further current base change is involved. If the earlier residual-functional relation \(b_T(p)=c\,d_p\) is also assumed, the new normalized coefficient is \(C_T(p,N)/(Nd_p)=c\).

The rectangular domain in the prior §5.2, defined by
\[
0<a<b<\min(\delta,\ell),\qquad b<c_1<d_1,\qquad
a<v(t)<b,\quad c_1<v(q)<d_1,
\]
lies in this new cone. Consequently every target test for its \((v(t),v(q))\) moment now has the same determined coefficient. No assertion is made about arbitrary source multipliers or unrelated moments on that rectangular domain without their own source-representation/comparison input.

The previous rank-collapse calculation remains true: the old coordinate top forms vanish on this mixed domain. The new equality is an additional closedness relation, not a proof that the old forms already spanned the missed test. It therefore does not invalidate or silently alter the old non-separation diagnostic.

## Excluded conclusions and gate

No whole-polyannulus scalar-rigidity theorem, all-moment accessibility theorem, iterative refinement scheme, finite-map disintegration, general semistable reduction, or full P21.3 conclusion is proved. The finite positive coefficient comparison does not supply a universal dominating Radon measure. There is no current pullback across a field extension.

The root contributed the outline and cannot serve as the required fresh independent reviewer. A separate non-root exact-byte mathematical audit and any production review remain required. No live manuscript, frozen predecessor, inventory, git state, or production state was changed.

