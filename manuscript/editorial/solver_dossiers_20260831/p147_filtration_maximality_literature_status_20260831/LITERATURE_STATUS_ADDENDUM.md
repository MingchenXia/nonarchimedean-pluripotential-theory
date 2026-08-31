# Literature status addendum — no novelty claim

Date: 31 August 2026. This is a separate source-status supplement. It does not modify the frozen candidate packet or supply an independent mathematical verdict.

## Classification

The most accurate provisional classification is **a detailed independent proof of a deduction covered by a newer preprint**, not a claimed new solution of an untouched conjecture.

Finski's *Kodaira–Iitaka dimension and multiplicity: an analytic perspective*, arXiv:2603.22194v1, was submitted on 23 March 2026. The arXiv record inspected here has one version and no journal reference; no journal-publication claim is made. [Primary record](https://arxiv.org/abs/2603.22194v1)

The paper does not literally state a theorem called “maximality of DXZ filtration test curves.” Its relevant result is Theorem 4.3, equation (4.15), in §4.1: resolved-image envelope metrics converge to the graded-series equilibrium metric. Formula (4.5) defines those envelope metrics; Lemma 4.2 gives monotonicity along multiplicative subsequences. Section 2, Example 4 identifies the filtration-based birational series. [Primary text](https://arxiv.org/html/2603.22194v1)

## Precise inference from that theorem statement

This is our inference from the stated source result, not a quotation of a named maximality theorem.

Fix a strict-interior DXZ parameter and write \(W_m=\mathcal F^{m\tau}H^0(mL)\). For sufficiently divisible \(m\), these systems define birational maps. Resolve a system and its image, obtaining
\[
\mu^*mL=g_m^*\widehat A_m+E_m.
\]
Use squared norms throughout this paragraph. The raw finite-level function has singularity type \(m^{-1}\log|s_{E_m}|^2\), with a bounded residual weight.

On this common smooth resolution, the ordinary envelope of that singularity type is obtained by varying all psh residual weights in \(g_m^*\widehat A_m\), subject to the original pointwise obstacle. Because \(g_m\) is a proper birational morphism between smooth models, these psh residual weights descend to \(\widehat A_m\). The pointwise obstacle for a descended weight is the infimum over its fibre of the original weight minus the exceptional logarithm. In norm language this is exactly the fibrewise supremum semimetric in Finski (4.3). Consequently the potential of Finski's metric (4.5) is precisely \(P_\theta[u_{\tau,m}]\), with the metric normalization accounted for.

Finski uses the unsquared section expression \(m^{-1}\log|s|\) in (6.2), whereas DXZ uses \(m^{-1}\log|s|^2\). Thus DXZ's potential is twice that unsquared potential, consistently with the respective \(\mathrm d\mathrm d^{\mathrm c}\) conventions; the underlying metric identity is unchanged.

Accepting Finski Theorem 4.3 therefore gives
\[
 P_\theta[u_{\tau,m}]\longrightarrow u_\tau
\]
almost everywhere along the sufficiently divisible subsequence. By multiplicativity,
\(u_{\tau,2^j}\leq u_{\tau,m_0 2^j}\).
The finite-level envelope sequence is increasing on this subsequence, and its limit is \(u_\tau\). The dyadic envelope identity in the proof of DXZ Lemma 4.5 then gives
\(u_\tau=P_\theta[u_\tau]=P_\theta[u_\tau]_{\mathcal I}\).
This is the precise route by which the newer approximation theorem covers the strict-interior maximality conclusion. The particular terminal-left-limit corollary follows by envelope monotonicity, not by arbitrary zero-mass reconstruction.

The birational envelope identification is an essential interface, not merely the word “envelope” occurring in both papers. It can be proved by the removable-psh argument spelled out in the frozen candidate's Step 1, also applied to the birational map to the smooth image resolution.

## Why keep the detailed candidate proof?

The frozen proof does not assume Finski Theorem 4.3. It proves the needed fixed-degree estimate directly from Berman's smooth-big full-section theorem and elementary algebraic normalization:

- The obstacle is quantized on the smooth resolution, so no quantization theorem on a nonnormal image is needed.
- A fixed nonzero conductor section explicitly returns normalized/resolved sections to high-degree homogeneous polynomials in the original generators.
- The resulting sup norm and degree correction are written down before passage to the limit.

Finski's displayed arrow (4.24) goes from downstairs sections to sections with normalization pushforward, whereas the following norm comparison uses a return to downstairs sections. This observation is not needed to infer consequences from the *statement* of Theorem 4.3, and it is not a verdict that the theorem is false. It explains why the candidate includes an explicit conductor proof rather than importing the displayed argument. Independent review should assess our proof on its own exact bytes.

## Frozen core identifiers

Core directory:
`/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260831/p147_filtration_maximality_research_20260831/`

- `MANIFEST.json`: `3ffa1f46f96ce438bf46dd0159cd036f10e79437c1b242a688359b53d652b7fb`.
- `statement.tex`: `d6fca037467563e9af28d2ca97917eb1d2f5697c0b36d36f6a6217439bdd444c`.
- `proof.tex`: `865717efa134e64f113ccf3b57a339b657059bc2b0ee7368ee5b70dd9872a362`.

The independent audit and production permission/review gates remain unchanged. No live integration, inventory retirement, general zero-mass recovery, or priority claim is authorized by this addendum.

