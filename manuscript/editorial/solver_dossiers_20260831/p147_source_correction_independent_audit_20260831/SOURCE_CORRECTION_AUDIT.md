# Source-correction audit for P14.7/P14.8

Date: 31 August 2026. Independent auditor: p213_skeletal_hostile.

## 1. Verdict and exact scope

The source corrections below are confirmed. The old dossier's normalization, proposed zero-mass interval, and positive-exceptional-divisor section calculation must not control the live account. DXZ's strict-interior slices all have positive top nonpluripolar mass. Their Lemma 4.5 already identifies the ordinary and multiplier-ideal envelopes there; the conjecture preceding Definition 4.4 asks whether the **raw** filtration curve equals that envelope.

This is a source audit, not verification of the new candidate proof. No candidate proof file was opened or used as a proof input. The separate literature appendix checks a consequence of Finski's stated 2026 approximation theorem, including the necessary identification of the two envelope constructions. It does not independently re-prove Finski's theorem, audit the candidate's Berman/conductor argument, or supply production verification.

P14.8 is **unresolved at the level of its present formulation and source attribution**. This audit does not solve it, retire it, or change the atom count. No live chapter, inventory, old dossier, or other frozen input was edited.

## 2. Frozen/read input identifiers

All paths below are absolute; sizes are bytes. The live-chapter and inventory hashes identify the read snapshots, not a promise that other authorized agents will never subsequently edit them.

| Input | Bytes | SHA-256 |
|---|---:|---|
| /private/tmp/dxz23.pdf | 534767 | 7fede7c413e396008217a4a4c9638776dbdd7cacff90fdd463bf5ae48220246c |
| /private/tmp/dxz23.txt | 141745 | 7d5a061d240096139e6302c2b4da2e9c125a8839730fc90909c1488baa446244 |
| /private/tmp/finski2603.22194v1_p147_source.pdf | 430003 | 6a2ffb81272721bbfff3f6f7c99ccbdc94fe9d21eaf823383fe23b94e7496d36 |
| /private/tmp/finski2603.22194v1_p147_source.txt | 169855 | 0cb98c7e53b6c745871a8e39e92684664ed81083dbef89f56b1ce1dff24a2586 |
| /private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260815/dxz_filtration_test_curve_maximality.md | 13151 | 4e50e4793799061ef7e039758cc480fdbbcf4a80405ae5a26c8b9130a7d70224 |
| /private/tmp/nappt_p071_20260827/manuscript/parts/part6/ch72_major_open_problems.tex | 173649 | 6e671da09d50cc7becd553d319a0cbce0fe6c3622ac77a491550411a32c69b8c |
| /private/tmp/nappt_p071_20260827/manuscript/editorial/open_problem_atomic_inventory_20260824.md | 66810 | 227b7fc73c50c4f17e17b5efb9231a595cb9585463299ff77feaa30e96ef06d6 |
| /private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260831/p147_filtration_maximality_literature_status_20260831/LITERATURE_STATUS_ADDENDUM.md | 5407 | 161adbd9e3fe31c4df5cc3b29ac357b9054d895865703491adebbd14ce807f62 |

DXZ denotes Darvas--Xia--Zhang, *A transcendental approach to non-Archimedean metrics of pseudoeffective classes*, arXiv:2302.02541v3, 17 July 2024. The versioned [primary record](https://arxiv.org/abs/2302.02541v3) and [primary PDF](https://arxiv.org/pdf/2302.02541v3) were checked. Its record gives Comment. Math. Helv. 100 (2025), no. 2, 269--322. Page numbers in this audit are the printed arXiv pages, not the journal pagination.

Finski denotes *Kodaira--Iitaka dimension and multiplicity: an analytic perspective*, arXiv:2603.22194v1. The [versioned primary record](https://arxiv.org/abs/2603.22194v1) lists submission on 23 March 2026 and, on this inspection, no journal reference. The [primary PDF](https://arxiv.org/pdf/2603.22194v1) and [primary HTML](https://arxiv.org/html/2603.22194v1) were checked. No journal-publication or priority claim is inferred.

## 3. What DXZ actually states

### 3.1 Setup and normalization

DXZ Section 4.1, printed p. 24, fixes a connected projective manifold \(X\), a big line bundle \(L\), a smooth Hermitian metric \(h\), and its curvature form \(\theta\). Definition 4.1 requires a decreasing, left-continuous, multiplicative filtration \(\mathcal F\), with a single linear bound \(C>0\) such that
\[
 \mathcal F^{-Cm}R_m=R_m,\qquad \mathcal F^{Cm}R_m=\{0\}.
\]
There is no finite-generation hypothesis.

Write \(c=\tau_L(\mathcal F)\), the asymptotic maximal filtration weight divided by the degree. Definition 4.3, printed p. 25, uses, for \(\tau<c\),
\[
 u_{\tau,m}
 =\operatorname{usc}\sup\left\{
 \frac1m\log |s|_{h^m}^{\,2}:
 s\in\mathcal F^{m\tau}H^0(X,L^m),\quad
 |s|_{h^m}^{\,2}\leq1\ \hbox{on }X
 \right\},\qquad
 u_\tau=\operatorname{usc}\sup_m u_{\tau,m}.
\]
The source also expresses the second function as the usc regularization of the degree limit. At \(c\), the definition uses the left limit in \(\tau\); for \(\tau>c\), it sets the function to \(-\infty\).

The factor is **\(1/m\)** in front of the logarithm of the squared norm, not \(1/(2m)\). DXZ uses
\(\mathrm d\mathrm d^{\mathrm c}=\sqrt{-1}\partial\bar\partial/(2\pi)\), printed p. 7. Changing the potential's factor while keeping its curvature form and this operator unchanged is not a harmless notation change. In a big non-nef class, the incorrectly halved expression need not even have the asserted \(\theta\)-psh property.

### 3.2 Three different equalities

On printed p. 8 DXZ defines the ordinary envelope by the singularity-type obstacle construction and normalizes the obstacle to \(V_\theta\). The multiplier-ideal envelope has the same obstacle and uses inclusion of \(\mathcal I(tu)\) for every real \(t\geq0\), where the local integrability convention is \(|f|^2e^{-tu}\).

The following assertions must be distinguished:

1. \(u_\tau=P[u_\tau]\): raw maximality.
2. \(P[u_\tau]=P[u_\tau]_{\mathcal I}\): equality of the two envelopes.
3. \(u_\tau=P[u_\tau]_{\mathcal I}\): raw \(\mathcal I\)-maximality.

The paragraph immediately preceding Definition 4.4, printed p. 25, formulates raw maximality in the big case as a conjecture. Definition 4.4 then applies inverse Legendre transform **after maximization**; it does not assert that maximization was already unnecessary.

Lemma 4.5, printed p. 26, proves, for every \(\tau<c\),
\[
 \widehat r^{\mathcal F}_\tau
   =P[u_\tau]=P[u_\tau]_{\mathcal I}.
\]
Thus assertion 2 is already a source theorem for every filtration in Definition 4.1. On this whole strict interior, assertions 1 and 3 are equivalent because assertion 2 is known. The project must not substitute assertion 2 for the genuinely stronger raw equality.

### 3.3 There is no zero-mass strict-interior interval

The opening paragraph of printed p. 26 expressly states positive mass of both \(u_\tau\) and \(\widehat r_\tau^{\mathcal F}\) for \(\tau<c\). The general test-curve discussion after equation (19), printed p. 12, supplies the same interior positivity from positive mass at the initial end, concavity, and monotonicity of nonpluripolar mass.

Proposition 4.6 on printed p. 26 is the radial-energy formula. In its proof DXZ establishes the slice formula
\[
 \int_X\theta_{u_\tau}^{\,n}
   =\operatorname{vol}(\mathcal F R^{(\tau)}),
 \qquad \tau<c.
\]
The proof explains that this graded series contains an ample linear series, and its sufficiently divisible systems give birational maps to their images. This is not restricted to finitely generated filtrations.

These statements rule out the old dossier's purported second interval of genuine zero-mass slices strictly before \(c\). They do **not** state that the terminal left limit at \(c\) is always positive, always zero, or always nontrivial. The convention \(u_\tau=-\infty\) beyond \(c\) is not a formulation of a nontrivial zero-mass reconstruction problem.

All assertions in this section are readings of [DXZ, pp. 7--9, 12, 24--26](https://arxiv.org/pdf/2302.02541v3), not acceptance of the new candidate proof.

## 4. Corrections to the preserved 15 August dossier

Line numbers refer to the exact old hash in Section 2.

| Old span | Finding | Warranted correction |
|---|---|---|
| 25--27 | Wrong \(1/(2m)\log|s|^2\) factor, and unspecified norm | Use the source's \(1/m\log|s|_{h^m}^2\) and its global sup-norm unit ball when identifying the DXZ construction. |
| 32--40 | The conjecture is described only as \(\mathcal I\)-maximality | State raw maximality first; record the already proved \(P=P_{\mathcal I}\) on the strict interior, which makes the two raw formulations equivalent there. |
| 42--45; 164--176; 207; 233--237 | Alleged zero-mass interval and reduction to arbitrary zero-mass recovery | Withdraw those as source claims. The source proves positive mass throughout \(\tau<c\); no reduction from arbitrary zero-mass data to terminal filtration data is supplied. |
| 53--55; 182--183; 203; 216--218 | Every minimal-singularity potential is claimed to equal its normalized envelope | Only the distinguished equilibrium representative \(V_\theta\) has the required equality automatically. A bounded change preserves the singularity type, not the actual normalized representative. |
| 71--85; 108--119 | Analytic singularity/integrally closed ideal data is treated as equivalent to equality of the actual potential with its envelope | The source definitions do not imply that statement. Matching singularity or ideal data alone cannot establish equality of the raw normalized potential. This audit does not endorse the proposed reduction (U). |
| 134--140; 226--232 | Positive exceptional twist confused with a negative twist | Replace by the exact computation in Section 5. |
| 147--160; 206; 226--232 | One fixed-divisor coefficient is used to rule out an entire counterexample mechanism | Matching that coefficient alone proves neither raw maximality at every filtration level nor the proposed exclusion of all such mechanisms. Withdraw the asserted disposition, without claiming a counterexample. |

For the minimal-singularity issue, a direct diagnostic is useful. On \(\mathbf P^1\) with a positive Fubini--Study curvature form, \(V_\theta=0\). Choose a sufficiently small nonconstant smooth \(\theta\)-psh function \(v\leq0\), with \(\sup v=0\). It has minimal singularities and every multiplier ideal is trivial, but
\[
 P[v]=P[v]_{\mathcal I}=0\ne v.
\]
Thus even smooth, completely integrally closed ideal data does not determine the raw representative without the envelope condition. This elementary diagnostic concerns the old inference, not the new candidate proof.

The old dossier explicitly records unconfirmed source access and candidate-only status. It should remain preserved as historical provenance, with this correction attached externally; it should not be silently overwritten.

## 5. Exact positive-\(E\) blowup calculation

Let \(\mu:X'=\operatorname{Bl}_p\mathbf P^2\to\mathbf P^2\), let \(E\) be the exceptional divisor, and put
\(L'=\mu^*\mathcal O(d)\otimes\mathcal O(E)\), \(d\geq1\).
For every integer \(m\geq0\),
\[
 \mu_*\mathcal O_{X'}(mE)=\mathcal O_{\mathbf P^2}.
\]
For completeness, away from \(p\) the map is an isomorphism and \(mE\) is absent. A section of \(\mathcal O(mE)\) restricts there to a regular function. Such a function extends across the codimension-two point on the normal surface \(\mathbf P^2\); its pullback is the original rational function. Conversely a regular function pulls back to a section of \(\mathcal O(mE)\). This proves the displayed sheaf identity locally on the base.

Projection formula consequently gives
\[
 H^0(X',mL')
   \simeq H^0(\mathbf P^2,\mathcal O(md)),
 \qquad
 t\longmapsto s_E^m\,\mu^*t.
\]
There is **no downstairs condition** \(\operatorname{mult}_p(t)\geq m\).
The exact upstairs vanishing is
\[
 \operatorname{ord}_E(s_E^m\mu^*t)
    =m+\operatorname{mult}_p(t).
\]
For example, with \(p=[0:0:1]\), the section \(t=Z^{md}\) has multiplicity zero at \(p\), but \(s_E^m\mu^*t\) is a valid section of \(mL'\), with order exactly \(m\) along \(E\). This directly contradicts the old displayed downstairs section description.

The vanishing condition in the old display instead belongs to
\[
 H^0(X',\mu^*\mathcal O(md)\otimes\mathcal O(-mE))
 \simeq H^0(\mathbf P^2,\mathcal O(md)\otimes\mathcal I_p^m).
\]
The sign distinction is material.

The old Zariski decomposition calculation \(P=\mu^*\mathcal O(d)\), \(N=E\) is consistent: \(P\) is nef, \(P\cdot E=0\), and \(E^2=-1\). With the correct DXZ normalization, the fixed \(E^m\) contributes \(\log|s_E|^2\), up to the choice of smooth metrics, with divisorial coefficient one. This correct fixed-component observation does not recover the invalid stronger claim about whole filtration curves. In particular, an \(\operatorname{ord}_E\)-filtration of sections of \(mL'\) corresponds to the shifted inequality \(\operatorname{mult}_p(t)\geq m(\tau-1)\), not the unshifted statement printed in the old dossier.

## 6. Precisely warranted live wording corrections

### 6.1 Chapter 72, current lines 2792--2802

The present paragraph incorrectly suggests a positive-mass interval followed by a separate zero-mass interval inside the same strict-interior filtration family. Its statement that both ranges remain open is not justified by the cited source and also ignores the newer literature discussed below.

The following is a source-correction replacement, not a new theorem or promotion:

> Darvas--Xia--Zhang formulate, immediately before Definition 4.4, maximality of the raw filtration test curve for a big line bundle. Under their Definition 4.1 hypotheses, every strict-interior parameter \(\tau<\tau_L(\mathcal F)\) has positive top nonpluripolar mass. Lemma 4.5 already proves \(P[\phi_\tau^{\mathcal F}]=P[\phi_\tau^{\mathcal F}]_{\mathcal I}\); the equality that their conjecture asks to add is \(\phi_\tau^{\mathcal F}=P[\phi_\tau^{\mathcal F}]\). A reconstruction target involving zero-top-mass data must be formulated separately: it is not a second zero-mass strict-interior interval in this construction, and it must not be identified with a formal terminal-left-limit corollary. The precise data, target, and equivalence relation for that reconstruction target remain to be specified.

Attach the DXZ citation with locators Definition 4.3, the paragraph before Definition 4.4, Lemma 4.5, and the proof of Proposition 4.6. This historical/source formulation makes no claim that the 2024 conjecture remained untouched in 2026. Any present literature status should be recorded explicitly, not inferred from absence of a project verification receipt.

The proposed old sentences about identifying an intrinsic MP image and removing a comparison-envelope operation are not verified by this bounded audit. If retained, they need their own precise comparison interface. They are unnecessary for the source-only correction.

### 6.2 Atomic inventory, current lines 828--835

For P14.7, clarify that the target equality is the raw equality \(u_\tau=P[u_\tau]\) for a big line bundle and all strict-interior parameters, not the already known equality \(P[u_\tau]=P[u_\tau]_{\mathcal I}\). Parenthetical “positive-mass range” is accurate only if it is explained to be this entire strict interior, not a possibly smaller interval. The existing project's verification state and the external literature state should be listed separately.

For P14.8, flag the current wording as an underspecified reconstruction target. At least these choices are missing:

- Are the inputs endpoint filtration data at \(\tau_L(\mathcal F)\), some other graded-series data, multiplier ideals, or data from arbitrary zero-mass potentials?
- Is the ambient class big, or itself of zero volume?
- Is the target an actual normalized \(\mathcal I\)-model potential, a singularity class, or another equivalence class?
- Does “recover” ask existence, uniqueness, a formula, or continuity of reconstruction; and with which obstacle/normalization?

Neither the present wording nor the cited DXZ passage selects these choices. There is no warranted deduction that arbitrary zero-mass recovery reduces to the filtration endpoint, nor the converse. This report does not choose a replacement research theorem or retire P14.8.

The inventory's blanket sentence at line 835 must not be used as independently established current-literature status for P14.7. No count or status mutation is made by this audit.

## 7. Separate appendix: 2026 literature mapping for P14.7

### 7.1 What was checked, and what was not

The frozen literature addendum identified in Section 2 was read in full, but not treated as authority. Independently inspected primary Finski material comprises: the standing setup and equilibrium metric definition in Section 1; normalization (1.27)--(1.30), printed p. 7; the filtration example on printed p. 10; the common resolution and base-divisor construction (3.14)--(3.15), printed p. 16; and (4.2)--(4.5), Lemma 4.2, and Theorem 4.3, printed pp. 20--22.

The source theorem is an approximation theorem for graded-series envelope metrics. It is not literally a theorem named “maximality of DXZ filtration test curves.” The inference below is ours. Finski's proof, especially its normalization/conductor interfaces, is not independently certified here.

### 7.2 The envelope identification required for the inference

Fix \(\tau<c\), put \(W_m=\mathcal F^{m\tau}H^0(X,L^m)\), and abbreviate \(u_m=u_{\tau,m}\), \(u=u_\tau\). DXZ Proposition 4.6's proof supplies the ample-series and sufficiently divisible birational hypotheses. If necessary pass to a Veronese degree \(m_0\): its high degrees are nonzero, and the resolved maps used below are birational. This matches Finski's standing nonzero-high-degree assumption. Passing to this Veronese does not change \(u\), since \(u_m\leq u_{m_0m}\) by taking the \(m_0\)-th power of a unit-norm section, while the reverse inequality between the two suprema is inclusion of indices.

For a sufficiently divisible \(m\), choose Finski's common smooth resolution and write
\[
 \pi_m^*(mL)=g_m^*\widehat A_m+E_m,
\]
where \(g_m:\widehat X_m\to\widehat Y_m\) is proper birational, \(\widehat Y_m\) is smooth, and \(E_m\) resolves the base ideal of \(W_m\).

The pulled-back finite-level potential, after removing
\(m^{-1}\log|s_{E_m}|^2\), is a bounded residual weight in
\(m^{-1}g_m^*\widehat A_m\). Consider an ordinary-envelope competitor
\(v\in\operatorname{PSH}(X,\theta)\), \(v\leq0\), \(v\leq u_m+C\).
After pullback and removal of the same divisor, its residual local weights are psh off \(E_m\), locally bounded above there by a bounded weight plus \(mC\), and therefore extend as psh weights across \(E_m\).

Every psh weight in \(g_m^*\widehat A_m\) descends to \(\widehat A_m\). One way to verify the point requiring birationality is to use the isomorphism locus: the weight there defines a downstairs psh weight. Properness bounds it above on relatively compact frame domains using finitely many upstairs domains. Removable extension on the smooth target gives a psh weight across the exceptional image. Its pullback and the original upstairs weight are psh and agree off a proper analytic subset, hence agree everywhere. This checks descent of actual representatives, not only currents or numerical classes.

Conversely, any downstairs psh residual weight satisfying the pulled-back pointwise obstacle produces, after adding \(E_m\), a positive metric in \(\pi_m^*L\), which descends through the proper birational map \(\pi_m\). On compact \(\widehat X_m\), an arbitrary psh residual weight is bounded above relative to a smooth reference. Since the finite-level residual weight is bounded, the resulting potential satisfies \(v\leq u_m+C\) for some finite \(C\). The two constructions therefore give exactly the same competitor set.

In norms, the residual obstacle is
\[
 |l|_a\ \geq\
 \sup_{x\in g_m^{-1}(y)}
   |s_{E_m}(x)\,g_m^*l|_{(\pi_m^*h)^m}.
\]
This is precisely Finski's fibrewise sup semimetric (4.3), with the compact set \(K=X\). Taking the smallest psh metric above that semimetric and restoring \(E_m\) is his (4.5). In potentials it is the usc supremum of exactly the ordinary-envelope competitors just identified. The obstacle \(v\leq0\) is equivalent here to \(v\leq V_\theta\), so there is no extra obstacle change. Accordingly, the potential represented by Finski's (4.5), in the DXZ normalization, is \(P[u_m]\).

Two normalization cautions are material:

- Finski (1.27)--(1.30) uses \(\mathrm d\mathrm d^{\mathrm c}=\sqrt{-1}\partial\bar\partial/\pi\), twice DXZ's operator, and \(h=h_0e^{-2\varphi}\). Its section potential is \(m^{-1}\log|s|\). Thus the same metric has DXZ potential \(2\varphi\), exactly \(m^{-1}\log|s|^2\).
- The displayed Finski (4.3) on printed p. 20 has an exponent \(k\) on \(\widehat h^L\). In that formula its section belongs to \(\widehat L^m\) by (4.2), so the type-correct exponent is \(m\). Formula (4.13) on printed p. 22 confirms the \(m\)/\(km\) powers. The identification above uses the bundle identity, not the isolated literal typo.

### 7.3 Deduction from the stated approximation theorem

Finski Theorem 4.3, printed p. 22, gives convergence outside a pluripolar set to the graded-series equilibrium metric. The latter is the raw DXZ metric \(h e^{-u}\). By the identified finite-level envelopes, along \(m=m_0 2^j\) this says
\[
 P[u_{m_0 2^j}]\longrightarrow u
 \quad\hbox{outside a pluripolar set}.
\]
The sequence is increasing in potential notation, by multiplicativity (also Finski Lemma 4.2 in metric notation).

The proof of DXZ Lemma 4.5 identifies the usc increasing limit of \(P[u_{2^j}]\) with \(P[u]\). Moreover
\[
 P[u_{2^j}]\leq P[u_{m_0 2^j}]\leq P[u].
\]
Thus the usc limit of the middle sequence is \(P[u]\), whereas Finski's convergence says it is \(u\). Equality outside a pluripolar set identifies the two psh representatives after usc regularization. Consequently, accepting the stated Finski theorem gives
\[
 u=P[u]=P[u]_{\mathcal I}
 \qquad(\tau<\tau_L(\mathcal F)).
\]

This establishes the mathematical interface claimed by the literature addendum at the level of an application of a stated primary theorem. The precise classification is **a deduction covered by a 2026 preprint**, not a new theorem literally stated under the DXZ name and not an independently audited proof of Finski's theorem. It rules out an unsupported “untouched open problem as of 2026” or novelty assertion. It does not change the independent/production gates for the project's separately authored candidate.

No general zero-mass reconstruction statement is obtained here. In particular, no terminal-left-limit observation is identified with P14.8.

## 8. Validation and boundaries

The PDF skill was used for exact-source inspection. DXZ printed pages 1, 7, 8, 9, 12, 24, 25, and 26 were rendered and inspected as whole pages; the normalization, conjecture, positivity sentence, and numbered assertions were visually checked against extraction. Finski printed pages 7, 10, 16, 20, 21, and 22 were likewise rendered and inspected as whole pages; relevant standing definitions were also checked in the primary text.

Only new audit artifacts are authored in this directory. The Finski download and PDF-to-text/rendered-page derivatives are source-inspection files in /private/tmp, not replacements for any manuscript input. Temporary page images are not controlling mathematical artifacts.

No production submission, no verification receipt, no live integration, no candidate-proof verdict, no P14.8 solution, and no inventory retirement are claimed. The proposed live corrections concern source accuracy and scope. The separate literature deduction is explicitly attributed and may remain editorial pending the project's integration process.
