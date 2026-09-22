# Chapter 17: projection and metric variation — 22 September 2026

## Projection proofs

The former proof of Proposition 17.8.2 claimed p_*p^*=id and
f_*f^*=d for arbitrary currents, citing the formal pushforward
proposition. There is no such general current pullback in the book.
The proof now keeps the suppressed canonical integration current:
p_*delta_(X_K')=delta_X and f_*delta_Y=d delta_X.
It verifies these identities against compactly supported top-degree
forms and then applies the existing continuous-potential projection
formula with that positive closed integration current.

The degree range of the products, analytic-morphism hypothesis,
pure dimensions and separation assumptions are now explicit.
Complete-field extension uses the corresponding smooth-form
pullback and psh pullback. Generic lengths remain in the canonical
integration currents; they have not been replaced by reduced cycles.

Proposition 17.13.1 now states the precise finite-locus and constant
calibrated-degree assumptions. The same integration-current identity
holds globally, so the proper projection formula proves the equality
of curvature measures globally. Pairing with 1 proves the mass identity.
The former argument discarding the exceptional set by the current
support-dimension theorem is removed. The new remark explains that
a top-degree current has bidimension (0,0), so that theorem would
require tropical dimension less than zero. A point mass disproves
the proposed general dimension shortcut.

The model calculation now uses compatible models, relatively normal
in their generic fibres. Absolute normalization would unnecessarily
change a nonnormal generic fibre. For a source component E dominating
F, ramification gives b_E=r_(E/F)b_F and restriction of normalized
valuations gives f(x_E)=x_F. These valuations are on different
function fields; the old phrase saying they were the same is removed.
Residue-field degrees remain in the pushforward weights:
sum_(E over F) b_E[kappa(E):kappa(F)]=e b_F.
The line-bundle projection formula identifies each coefficient,
and components with smaller-dimensional images have zero
intersection for the explicit cycle-theoretic reason rho_*[E]=0.
Tensor-power denominators are cleared and restored.

## Metric variation

Proposition 17.8.3 previously called its primitive alpha closed,
although its dd' is the generally nonzero difference of two
curvature products. The primitive is now correctly stated to be
symmetric. A telescoping sum gives it explicitly:
alpha=sum_j u_j H_j, where H_j contains the first j-1 unprimed
curvatures and the last n-j primed curvatures. The H_j are closed;
their products with the variable real functions u_j need not be.
The outer-potential identity proves the displayed variation formula.

The open-annulus check u=(-log|T|)^2 has nonzero Hessian
2[d't wedge d''t], and rules out the false closedness claim.
The zero-dimensional case is treated by equal empty products,
without introducing a negative-degree primitive. Mass independence
uses the legitimate pairing with 1 on a proper space.

## Primary source and dependency check

The checked source is
[Chambert--Loir--Ducros, arXiv version 2, 25 July 2025](https://arxiv.org/pdf/1204.6277v2),
the version identified by the existing CLD25 bibliography entry.
Exact locators are:

- Propositions 15.3.1 and 15.4.3: scalar extension and calibrated integration;
- Propositions 16.1.1--16.1.2, printed pages 435--436: integration-current
  pushforward, including the generic multiplicities;
- Proposition 16.1.5, printed pages 437--438: the dpsh Hessian formula
  under the precise generically finite hypotheses;
- Corollary 18.3.3, printed page 515: the curvature formulation;
- Proposition 18.3.10, printed pages 517--518: metric variation.

The source statement of Proposition 18.3.10 does not require the
primitive to be closed, although its proof contains that incorrect
adjective. The book's repair follows the actual formula and the
explicit annulus check rather than repeating that proof slip.
The first integration-current page was also inspected as a PDF image.

The production closure was searched for all projection and
metric-variation labels. Projection consumers are internal to
Chapter 17; they use the proper formula in its stated degree range.
Metric-variation consumers in Chapters 17 and 18 use exactness and
total mass, not closedness of the primitive. The Chapter 18
alternative proof already distinguishes the variable factor from
the remaining closed factors.

## Validation

The new projection proofs, exceptional-set remark and complete
metric-variation proposition/proof pass the strict Mingchen audit
with zero errors and warnings. Auditing the two entire projection
blocks reports six warnings for their six pre-existing itm: labels;
those stable cross-reference labels are intentionally retained.
No new label has that prefix.

A second mathematical reading checked the metric-change sign,
telescoping endpoints, dimension zero, generic multiplicities,
ramification cancellation, residue degrees, contracted components,
and the compact-support pairing. The final source check has
389 TeX files and 11,489 unique labels, with no missing input,
duplicate label, dangling reference or structural defect.
The source diff is whitespace-clean.

The final complete build has 3,915 pages and 18,573,624 bytes,
with zero unresolved references or citations and zero horizontal
or vertical overflows. The projection pages were rendered and
inspected at physical pages 1116--1117 and 1142--1143
(printed 1048--1049 and 1074--1075). After the metric-variation
follow-up, physical pages 1117--1118 (printed 1049--1050)
were rendered and inspected again.

PDF SHA-256:
`cd009e9e3fc67ee0b1124bb9cd675d27fbbedd64edeba31dda9fe58838945922`

Chapter 17 SHA-256:
`bf54ba43a47e809815cadc51b1b9d712b87e38bb21cdec5fd426e7d10df56561`

The open-problem inventory remains 46 active atoms in 14 formal
environments, with tiers (0,5,8,16,17). The supplied CURVE_PSH.tex,
Chapter 71, the frozen research inputs, and dated release snapshots
are unchanged. This work repairs exposition and proofs of existing
results; it is not a new research-verification gate.
