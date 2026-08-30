# P07.1 Stone-parameter × Euclidean candidate: source and obligation matrix

## Status and exact scope

This is an isolated candidate packet. It has not been inserted into the
live manuscript and has not yet passed a production Rethlas call. It proves
a first-stage collapse statement only for the exact product affine
G-tropical structure specified in statement.tex.

The candidate does **not** retire P07.1. The remaining bridge is from this
product geometry to arbitrary affine G-tropical local models, especially
models with nontrivial affine directions in the parameter factor or
polyhedral face gluing.

## Primary source ledger

| Source | Exact use | Local fingerprint |
|---|---|---|
| A. Chambert-Loir and A. Ducros, *Formes différentielles réelles et courants sur les espaces de Berkovich*, arXiv:1204.6277v2 (25 July 2025), cited as CLD25 | Standing parlinear parameters; G-tropical and affine axioms; smooth forms; products; positivity; psh generation and first stage; Euclidean convexity | Navigation extraction /private/tmp/CLD25.txt, SHA-256 021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e |

The extraction is used only to audit section numbering. The cited
mathematical source is the official arXiv v2 article. All other ingredients
below are elementary topology or Euclidean convex analysis and are proved
at the point of use.

## Source-legality matrix

| ID | Obligation | Discharge in the packet | Source / exact boundary |
|---|---|---|---|
| S0 | Fix legal parlinear parameters | statement.tex explicitly fixes \(K=\mathbf Q\), \(G=\mathbf R\) | CLD §1.8.2. No claim is made for a smaller \(G\). |
| S1 | Verify the CLD topological axiom | First proof block: a locally compact Hausdorff space with a clopen basis has a basis of relatively compact opens, hence of opens countable at infinity | CLD §3.1.1 plus the internal one-line shrinking argument |
| S2 | Verify all four domain axioms | Domains are all locally closed subsets; compact clopen neighbourhoods in each locally closed subspace give the compact-domain G-cover | CLD §3.1.2; proved explicitly |
| S3 | Verify the parlinear G-sheaf and its three axioms | The proof checks G-gluing, finite polyhedral image on compact domains, stability under composition, and the domain property for inverse images | CLD §3.1.3 and §§1.8.1–1.8.3; proved explicitly |
| S4 | Verify the affine refinement | Set \(L_Z=\operatorname{PL}_Z\); ordinary gluing and “parlinear iff G-locally affine” are checked | CLD §6.1.1 |
| S5 | Form the product source legally | Use the CLD product construction, not the full locally closed product site | CLD §§9.1.1–9.1.4 |
| S6 | Identify smooth generators and positivity | Product affine coordinates are locally constant in \(Z\) plus affine in \(x\); after clopen shrinking smooth functions depend only on \(x\), and positivity is positive semidefiniteness of the Euclidean Hessian | CLD Definition 6.2.1, Definition 3.5.1, Example 3.5.4, and Proposition 8.3.2 |
| S7 | Identify the generated and first-stage sheaves | The minimality step uses the smallest decreasing-limit-stable subsheaf; the final step produces local decreasing smooth-psh sequences | CLD Definition 8.1.1, Lemma 8.1.4, Definition 8.1.13 |

## Proof-obligation matrix

| ID | Obligation | Exact mechanism | Packet locator | Status |
|---|---|---|---|---|
| Q1 | Define a genuine local comparison sheaf | Local factorization through a compact metrizable clopen-base quotient, with joint USC and fibrewise finite convexity or identically \(-\infty\) | proof.tex, \(\eqref{eq:p071-stone-local-factor}\) | Discharged |
| Q2 | Contain every smooth psh generator | Clopen shrinking kills the \(Z\)-dependence and the quotient may be a point | Paragraph after \(\eqref{eq:p071-stone-local-factor}\) | Discharged |
| F1 | Fuse countably many rowwise/local quotients | A finite product cover for each row supplies countably many clopen generators; their Boolean algebra defines one evaluation quotient \(q:C\to Y\) | \(\eqref{eq:p071-stone-factor-cover}\)–\(\eqref{eq:p071-stone-common-quotient}\) | Discharged |
| F2 | Prove factorization through the common quotient | Equality of evaluation coordinates forces equality in every local quotient, because a countable clopen base separates points | Paragraph before \(\eqref{eq:p071-stone-limit-factor}\) | Discharged |
| U1 | Descend upper semicontinuity to \(Y\times B_0\) | The proof avoids assuming that a product quotient is automatically quotient: it uses compact fibres, a finite product-neighbourhood subcover, and closedness of \(q\) | \(\eqref{eq:p071-stone-sublevel-union}\)–\(\eqref{eq:p071-stone-quotient-neighbourhood}\) | Discharged |
| C1 | Control \(-\infty\) in the fibres | A local midpoint argument makes both the \(-\infty\)-locus and its complement open; connectedness gives “finite everywhere or identically \(-\infty\)” | Extended-value paragraph after \(\eqref{eq:p071-stone-quotient-neighbourhood}\) | Discharged |
| C2 | Pass convexity through a decreasing limit | If no term is identically \(-\infty\), pass to the limit in the Jensen inequality; one polar value propagates along a slightly extended segment | Same paragraph; cross-check CLD Proposition 8.3.2 | Discharged |
| M1 | Obtain the full-to-comparison inclusion | The comparison sheaf contains generators and is decreasing-sequentially closed | \(\eqref{eq:p071-stone-minimality}\) | Discharged |
| N1 | Work on one fixed neighbourhood | Start from a single factorization on \(C\times B_0\), then fix any \(B\Subset B_0\); every approximant is defined on \(C\times B\) | \(\eqref{eq:p071-stone-nested-balls}\) onward | Discharged |
| E1 | Construct monotone upper envelopes | Nested finite clopen partitions, shrinking Euclidean radii, and floors \(-k\) give \(a_{k+1}\le a_k\) | \(\eqref{eq:p071-stone-upper-envelope}\)–\(\eqref{eq:p071-stone-envelope-monotonicity}\) | Discharged |
| E2 | Identify the envelope limit, including polar points | Joint USC controls the supremum over the shrinking product neighbourhood; the floor tends to \(-\infty\) | \(\eqref{eq:p071-stone-envelope-convergence}\) and its proof | Discharged |
| R1 | Smooth without losing psh | Each finite convex branch is mollified; Jensen gives the lower bound, and finite-family uniform convergence gives the upper error | \(\eqref{eq:p071-stone-mollification-error}\)–\(\eqref{eq:p071-stone-smoothed-envelope}\) | Discharged |
| R2 | Verify smooth gluing across parameter pieces | The pullbacks \(q^{-1}(P)\) form a finite clopen partition, so branchwise Euclidean smooth convex functions are globally smooth psh on \(C\times B\) | Paragraph after \(\eqref{eq:p071-stone-smoothed-envelope}\) | Discharged |
| R3 | Restore exact cross-level monotonicity | The displayed three-step inequality gives \(w_{k+1}\le w_k+\eta_{k+1}\); summable tail constants absorb the error | \(\eqref{eq:p071-stone-almost-monotone}\)–\(\eqref{eq:p071-stone-tail-correction}\) | Discharged |
| R4 | Identify the final limit | \(0\le w_k-a_k\le\eta_k\), \(a_k\downarrow\bar v\), and the tail constants tend to zero | Paragraph after \(\eqref{eq:p071-stone-tail-correction}\) | Discharged |
| Z0 | Treat \(d=0\) rather than silently invoking convolution | Use only the nested clopen partitions and floors; the approximants are locally constant smooth psh | \(\eqref{eq:p071-stone-zero-dimensional-envelope}\) | Discharged |
| B1 | Preserve scope and novelty firewalls | The statement explicitly excludes other affine structures, face gluings, and arbitrary affine G-tropical spaces; no priority claim is made | Last paragraph of statement.tex | Discharged |

## Dependency-free points

The Boolean-quotient construction does not invoke a representation theorem
for Stone spaces. It is the explicit evaluation map into the countable cube
indexed by the generated Boolean algebra. Likewise, the USC descent does
not invoke a general theorem about products of quotient maps. These two
potentially delicate bridges are proved directly in proof.tex.

