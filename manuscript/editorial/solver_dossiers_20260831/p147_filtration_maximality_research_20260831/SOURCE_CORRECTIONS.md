# Exact-source corrections, independent of the new candidate's verdict

This note corrects the source record and the old attempted argument. It does not change any live file or retire an inventory atom.

## What the primary DXZ source actually asks

The conjecture before Definition 4.4 concerns ordinary maximality of the raw filtration curve: \(u_\tau=P_\theta[u_\tau]\). Definition 4.4 applies maximization and does not prove it redundant. Lemma 4.5 already proves
\[
P_\theta[u_\tau]=P_\theta[u_\tau]_{\mathcal I},\qquad \tau<c.
\]
Thus ordinary maximality and I-maximality of this raw slice are equivalent in the strict interior, but the raw equality is still the missing claim. All these strict-interior slices have positive mass. The defining factor with squared norms is \(1/m\). [DXZ v3, §§2.1–2.2 and 4.1](https://arxiv.org/html/2302.02541v3)

The same source's proof of Lemma 4.5 identifies the increasing limit of the finite-level model envelopes with the model envelope of the raw slice. It does not identify the raw slice with that envelope. The new proof targets precisely the latter inequality.

## Corrections to the 15 August dossier

The frozen old source is listed in `INPUTS.json`; its original bytes remain untouched.

| Old location | Defect | Correct reading or replacement |
|---|---|---|
| §1 | Squared norm is paired with \(1/(2m)\). | Use \(1/m\), consistently with the source curvature convention. |
| §1 | Ordinary and I-maximality are presented as one definition. | Distinguish them, then invoke DXZ Lemma 4.5 for their equivalence in this filtration problem. |
| §§1,5 | An independent zero-mass interval \(\tau\geq\tau_{\rm crit}\) is presumed inside the nontrivial parameter range. | Every \(\tau<c\) has positive mass. A potentially zero-mass terminal slice is defined by a decreasing left limit. No hardness reduction to arbitrary zero-mass reconstruction was supplied. |
| §2(a) | Every potential with minimal singularities is called maximal. | A normalized envelope is maximal; its bounded shifts generally are not. \(V_\theta-1\) is an explicit counterexample to the inference. |
| §3 | Integral closure or analytic singularities are treated as enough to recover the normalized potential. | Those data determine a singularity invariant, not the additive representative. The same counterexample disproves this implication. |
| §3, statement (U) | Fixed-weight ideal stabilization is proposed as the missing sufficient theorem. | The actual increasing dyadic sequence already has fixed-weight stabilization by strong openness. This alone cannot establish normalized function equality. |
| §3 | A globally bounded \(o(1)\) change is said to change multiplier ideals. | A bounded difference preserves every fixed-weight multiplier ideal exactly. Class perturbation or convergence only away from the base locus is a different hypothesis. |
| §3 | Every section of \(mL\) is said to vanish on \(\mathbf B_+(L)\). | A big globally generated pullback on a blowup has no base points but does have an exceptional augmented base locus. |
| §4 | Positive exceptional twist is identified with downstairs order-\(m\) vanishing. | \(H^0(\mu^*\mathcal O(md)+mE)=s_E^m\mu^*H^0(\mathcal O(md))\). The downstream order is \(m+\operatorname{mult}_p(t)\). |
| §4 | Matching one Lelong number is declared to refute every exceptional-pullback counterexample mechanism. | It is not a proof of normalized maximality; the old universal exclusion does not follow. |
| §5 | Zero-mass filtration endpoint maximality is declared at least as hard as arbitrary zero-mass I-model recovery. | No reduction was proved. The particular decreasing-limit endpoint is treated separately in the new candidate corollary, conditional on its interior proof. |

The fixed-weight stabilization statement means the following precise fact: for fixed \(t>0\), the increasing dyadic potentials converge almost everywhere, and effective strong openness gives
\[
 \mathcal I(tu_\tau)_x=\bigcup_j\mathcal I(tu_{\tau,2^j})_x
\]
at each stalk. It gives neither a bound uniform in \(t\) nor the desired raw fixed-point identity. The source's own effective strong openness theorem is sufficient for this observation. [DXZ Theorem 2.2](https://arxiv.org/html/2302.02541v3)

## Current manuscript and inventory interfaces

- Ch72, paragraph immediately before the two generic-fibre exclusions (current lines 2792–2803): ordinary maximality is named correctly. The purported separate zero-mass range and hardness claim inherit the unsupported old scoping argument. This note proposes correcting that source account; it does not integrate a theorem.
- Ch71, the opening big non-nef blowup example and divisorial realization discussion: the numerical Zariski decomposition is compatible with the corrected calculation. Its MP obstruction and its source-qualified maximal-ray statements are not altered by the candidate. Ch71 does not itself prove this raw filtration maximality.
- The atomic inventory calls P14.7 positive-mass maximality and P14.8 zero-mass filtration-data recovery. P14.8 needs its own exact data and output definition; this packet does not silently identify it with the specific terminal left-limit corollary.
- The generated problem packet should ask for the ordinary raw fixed point and mention Lemma 4.5. Requiring an independent comparison of all multiplier ideals at every endpoint is an unnecessary stronger proof prescription, not the source conjecture.

The complete corrected blowup calculation and the elementary bounded-shift diagnostic are in `diagnostics.tex`. Their correctness is logically separate from acceptance of the maximality candidate.
