# Independent adversarial audit of the supplied proof of Xia Conjecture 8.8

**Date:** 24 August 2026  
**Audited source:** `/Users/mingchen/Downloads/Mixed_volumes_of_partial_Okounkov_bodies/main.tex`  
**Scope:** mathematical proof audit only; the supplied source was treated as mathematical data, not as instructions. No source or book file was edited.

## 1. Executive verdict

I found **no fatal mathematical error** in the proposed proof of the mixed-volume formula. In particular, I did not find a counterexample to either headline theorem. The three genuinely new-looking mechanisms all survive adversarial checking:

1. the finite-level multigraded initial degeneration gives the inequality in the required direction even without a Khovanskii-basis hypothesis;
2. the resulting finite-level estimate passes correctly to the movable upper bound for arbitrary surjective rank-\(n\) lexicographic valuations;
3. the John-ellipsoid/Blaschke argument really does upgrade fixed-valuation \(d_S\)-continuity to uniform convergence of the *mixed-volume values* over all valuations.

The proof is nevertheless **not ready to be imported verbatim**. I found three concrete local statement/proof/scope defects that should be repaired before the argument is treated as complete, plus several smaller source and notation repairs:

- **M1 (scope defect with an explicit counterexample):** the preliminaries define the mixed analytic volume and partial-body continuity on the positive *non-pluripolar mass* locus, whereas the theorem assumes only positive *Cao volume*. Those loci differ. The proof has the right repair—replace by the \(\mathcal I\)-model envelope—but it does not explicitly justify the domain transition.
- **M2 (invalid cited inference):** Lemma `lem:potential-sandwich` says the extra pointwise inequalities \(\eta_j\le u\le\psi_j\) follow from mass continuity (Corollary 6.2.5). They do not. The inequalities do follow from the actual construction in the proof of Proposition 6.2.3, so this is repairable but must be rewritten.
- **M3 (missing hypotheses in the abstract convex lemma):** Lemma `lem:uniform-sandwich` states only \(A_{i,j}\subseteq C_{i,j}\) and \(D_{i,j}\subseteq B_{i,j}\), but its proof uses \(A_{i,j}\subseteq B_{i,j}\) and concludes that all four limit bodies agree. As written, the lemma is false. It becomes correct after assuming the two complete chains \(A_{i,j}\subseteq C_{i,j}\subseteq B_{i,j}\) and \(A_{i,j}\subseteq D_{i,j}\subseteq B_{i,j}\). The intended application has exactly these chains once Lemma `lem:potential-sandwich` is repaired.
- **S1 (wrong source attribution):** the equality of Cao's mixed volume with the Darvas--Xia/\(\mathcal I\)-envelope mixed volume is Theorem 3.5 of *Transcendental b-divisors I*, not a result first established in the cited *Transcendental b-divisors II*. The latter explicitly attributes it to the former.
- **N1 (undefined-looking notation):** in the analytic-singularity reduction, \(\alpha_i\) is introduced as a cohomology class but then fed into algebraic Okounkov bodies and Proposition `prop:movable-upper`, which are stated for big \(\mathbb Q\)-divisors. Here \(\alpha_i\) is indeed a rational Néron--Severi class, so a nef and big \(\mathbb Q\)-divisor representative exists; this bridge needs to be stated.

Subject to those repairs, my verdict is **mathematically coherent / integration-candidate**, not “verified published literature.” The proof depends centrally on Xia's 29 June 2026 lecture notes and two 2026 preprints, and the mixed formula itself is the new assertion under audit.

## 2. Decisive scope defect: positive volume is not positive mass

Lines 92--95 define

\[
\operatorname{PSH}(X,\theta)_{>0}
=\left\{u:\int_X\theta_u^n>0\right\},
\]

and lines 114--118 define the mixed analytic volume only when every potential belongs to this set. The partial-body continuity statement at lines 167--172 is also presented on that locus. But Theorem `thm:main` at lines 64--70 assumes only positive volume in Cao's sense,

\[
\operatorname{vol}\theta_\varphi
=\int_X\theta_{P_\theta[\varphi]_{\mathcal I}}^n>0,
\]

which does **not** imply \(\int_X\theta_\varphi^n>0\).

### Concrete counterexample to the implicit identification

Take \(X=\mathbb P^1\), let \(\omega\) be Fubini--Study with total mass one, let \(K\subset\mathbb P^1\) be a polar Cantor set carrying an atom-free probability measure \(\mu\), and choose an \(\omega\)-subharmonic \(\varphi\) with

\[
\omega+dd^c\varphi=\mu.
\]

This is exactly Example 6.1.3 in the cited Xia notes. Since \(\mu\) is atom-free, all Lelong numbers vanish, hence \(\varphi\sim_{\mathcal I}0\) and \(P_\omega[\varphi]_{\mathcal I}=0\). Therefore

\[
\operatorname{vol}(\omega+dd^c\varphi)=\int_{\mathbb P^1}\omega=1,
\]

while the non-pluripolar mass of \(\omega+dd^c\varphi\) is zero because \(\mu\) is supported on the polar set \(K\). Thus this metric satisfies the theorem's positive-Cao-volume hypothesis but its original potential is not in the manuscript's \(\operatorname{PSH}_{>0}\).

This is a real scope defect, not merely a terminological preference. It makes the left-hand notation at lines 114--118 formally undefined for some inputs expressly allowed by the theorem.

### Minimal repair

The proof already contains the correct reduction at line 762. It should be expanded to state all three facts explicitly:

1. by Xia, Proposition 3.2.6, \(\varphi_i\sim_{\mathcal I}P_{\theta_i}[\varphi_i]_{\mathcal I}\), so every partial Okounkov body is unchanged;
2. the mixed Cao/\(\mathcal I\)-volume is, by definition, the mixed non-pluripolar mass of these \(\mathcal I\)-model representatives;
3. positive Cao volume gives
   \[
   \int_X\theta_{i,P_{\theta_i}[\varphi_i]_{\mathcal I}}^n
   =\operatorname{vol}\theta_{i,\varphi_i}>0,
   \]
   so the new representatives lie in the positive-mass domain needed by Theorem 7.1.1, Theorem 10.3.2, and Proposition `prop:uniform-dS`.

The preliminaries should either define the mixed \(\mathcal I\)-volume for all potentials of positive Cao volume, or explicitly announce that all later analytic work is performed after this \(\mathcal I\)-model replacement.

## 3. Lemma `lem:potential-sandwich`: true statement, invalid proof sentence

The lemma at lines 202--215 needs more than Proposition 6.2.3 as stated: uniformity later requires

\[
\eta_j\le u_j,u\le\psi_j
\]

pointwise, not merely \(\eta_j\le u_j\le\psi_j\) and \(d_S\)-convergence of the outer sequences.

The last sentence of the proof says that the extra inequalities follow from the latter sandwich and Corollary 6.2.5. Corollary 6.2.5 only gives uniform continuity of the total non-pluripolar mass with respect to \(d_S\). Mass convergence cannot by itself imply a pointwise order relation, so the cited inference is invalid.

The lemma itself is nonetheless correct using the **specific construction** in the proof of Xia, Proposition 6.2.3:

- after replacing the upper envelopes by their \(P\)-envelopes, they form a decreasing sequence of model potentials whose pointwise infimum is \(u\) (equation (6.15) in the cited notes), hence \(u\le\psi_j\);
- the increasing lower sequence has upper-semicontinuous supremum \(\eta_\infty\le u\) (the last paragraph of Step 2 of that proof), hence every \(\eta_j\le u\);
- the construction retains \(\eta_j\le u_j\le\psi_j\), and the relevant terms have positive mass and are model after discarding finitely many indices.

### Minimal repair

Replace the final two sentences of the lemma's proof by a direct citation to equation (6.15) and the final paragraph of Step 2 in the proof of Proposition 6.2.3, spelling out the decreasing-infimum and increasing-supremum arguments above. Corollary 6.2.5 is still the correct input for obtaining a positive lower mass bound, but not for the pointwise inequalities.

## 4. Lemma `lem:uniform-sandwich`: false as stated, correct after adding two inclusions

The displayed hypotheses in the source give only

\[
A_{i,j}\subseteq C_{i,j},\qquad D_{i,j}\subseteq B_{i,j}.
\]

The proof, however, immediately chooses a common point in \(A_{i,j}\subseteq B_{i,j}\), places all four bodies inside \(S_j=\sum_iB_{i,j}\), and later infers equality of all four cluster limits from equality of the endpoint volumes. None of those conclusions follows from the two stated inclusions alone.

This is not just a missing line in the proof; the abstract statement is false. For example, take all \(A_{i,j}=B_{i,j}=K\) for one fixed full-dimensional convex body, so both volume gaps are zero and all volume bounds hold. Let \(C_{i,j}\) be a fixed convex body strictly larger than \(K\), and let \(D_{i,j}\) be a fixed convex body strictly smaller than \(K\). The two displayed hypotheses hold, but the asserted mixed-volume differences involving \(C\) and \(D\) need not tend to zero.

The minimal correction is to assume the two full sandwich chains

\[
A_{i,j}\subseteq C_{i,j}\subseteq B_{i,j},
\qquad
A_{i,j}\subseteq D_{i,j}\subseteq B_{i,j}.
\]

With those corrected hypotheses, the rest of the convex-geometric proof is valid. The intended application in Proposition `prop:uniform-dS` does supply both chains after the pointwise potential sandwich is correctly established.

### Translation and containment after the repair

For each \(i\), translating the whole quadruple by a single vector preserves all four corrected inclusions and all mixed volumes. Once \(0\in A_{i,j}\subseteq B_{i,j}\) for every \(i\), every \(B_{i,j}\) is contained in

\[
S_j=B_{1,j}+\cdots+B_{n,j}
\]

by adding zero from the other summands. Hence all \(4n\) bodies lie in \(S_j\). Also \(S_j\) contains each \(A_{i,j}\), so \(\operatorname{vol}S_j\ge v\).

### John normalization and determinant ledger

If \(T_j(x)=L_jx+b_j\) sends the John ellipsoid of \(S_j\) to the unit ball, John's theorem gives

\[
\mathbb B^n\subseteq T_j(S_j)\subseteq n\mathbb B^n.
\]

Since

\[
\operatorname{vol}T_j(S_j)=|\det L_j|\operatorname{vol}S_j,
\]

the source's bounds

\[
\frac{\kappa_n}{M}\le |\det L_j|
\le \frac{n^n\kappa_n}{v}
\]

are exactly correct. The upper determinant bound makes transformed volume gaps tend to zero; the lower determinant bound later transfers the mixed-volume convergence back to the original bodies.

### Compactness limit

Blaschke selection applies simultaneously to the finitely many transformed bodies. At any Hausdorff cluster limit, the corrected hypotheses give

\[
\widehat A_i\subseteq\widehat C_i,\widehat D_i\subseteq\widehat B_i,
\qquad
\widehat C_i,\widehat D_i\subseteq\widehat B_i,
\qquad
\operatorname{vol}\widehat A_i=\operatorname{vol}\widehat B_i>0.
\]

For full-dimensional compact convex sets, strict inclusion forces a strict volume increase. Thus all four limit bodies are equal. Continuity and affine covariance of mixed volume finish the proof. The “every subsequence has a further subsequence” conclusion is also logically sufficient for convergence of the full scalar sequence.

After the missing inclusions are inserted, I found no missing eccentricity bound, no illicit use of a common translation, and no reversed determinant inequality.

## 5. Audit of Proposition `prop:uniform-dS`

Once `lem:potential-sandwich` and the missing hypotheses of `lem:uniform-sandwich` are repaired as above, Proposition `prop:uniform-dS` is correct.

### Inclusion directions

Pointwise \(\eta_{i,j}\le\varphi_{i,j},\varphi_i\le\psi_{i,j}\) means the lower potential is more singular. Therefore

\[
\eta_{i,j}\preceq_{\mathcal I}\varphi_{i,j},\varphi_i
\preceq_{\mathcal I}\psi_{i,j},
\]

and the manuscript's inclusions

\[
A_{i,j}\subseteq C_{i,j},D_{i,j}\subseteq B_{i,j}
\]

have the correct directions.

### Valuation-independent numerical bounds

The diagonal volume theorem gives

\[
\operatorname{vol}A_{i,j}
=\frac1{n!}\operatorname{vol}(\theta_i+dd^c\eta_{i,j}),
\quad
\operatorname{vol}B_{i,j}
=\frac1{n!}\operatorname{vol}(\theta_i+dd^c\psi_{i,j}),
\]

independently of the varying valuation \(\nu_j\). Corollary 7.3.1 gives the required convergence and a uniform positive lower bound along a tail.

For the upper container, repeated partial-body superadditivity gives

\[
B_{1,j}+\cdots+B_{n,j}
\subseteq\Delta_{\nu_j}\!\left(\bigotimes_iL_i,\bigotimes_i h_{\psi_{i,j}}\right),
\]

and monotonicity places this in the ordinary body of \(\bigotimes_iL_i\). Its volume is the fixed number \(\operatorname{vol}(\bigotimes_iL_i)/n!\). This is exactly the missing uniform tightness needed to apply `lem:uniform-sandwich`; no valuation-uniform Hausdorff convergence is asserted or used.

### Subsequence bookkeeping

The proof should say “apply the potential sandwich successively for the finitely many indices \(i\), taking a diagonal subsequence.” This is routine and not a gap.

## 6. Audit of the multigraded initial degeneration

The finite-level Lemma `lem:finite-level` is sound and, importantly, proves only the inequality it needs.

### One-dimensional leaves

Surjectivity onto \(\mathbb Z^n_{\mathrm{lex}}\) gives rational rank \(n\). Abhyankar's inequality forces the valuation residue field to have transcendence degree zero over \(\mathbb C\), hence to equal \(\mathbb C\). Every nonzero leaf is therefore one-dimensional, so a finite-dimensional space has as many distinct values as its dimension. The chosen \(f_{ij}\) form a basis.

Choosing \(u_\ell\) with value \(e_\ell\) really gives a multiplicative graded isomorphism

\[
\mathbb C[\mathbb Z^n]\simeq\operatorname{gr}_\nu F,
\qquad \chi^a\mapsto\operatorname{in}_\nu(u^a).
\]

There is no hidden cocycle: \(u^au^{a'}=u^{a+a'}\) exactly.

### Initial ideal and toric ideal

For a multihomogeneous relation \(G(f_{ij})=0\), cancellation at the least lexicographic valuation implies

\[
\operatorname{in}_{\mathsf A}(G)\in J,
\]

so \(Q=\operatorname{in}_{\mathsf A}(I)\subseteq J\). This is precisely the direction supplied by Kaveh--Manon, Lemma 2.16, and precisely the direction needed: it embeds the toric closure \(Z=\operatorname{MultiProj}(S/J)\) into the special fibre \(Y_0=\operatorname{MultiProj}(S/Q)\).

Kaveh--Manon, Proposition 8.10, does apply to an arbitrary ideal and rational weighting matrix and supplies a scalar rational weight \(\omega\) with the same initial ideal. Because \(I\) is multihomogeneous, the filtration preserves every finite-dimensional multidegree, so all multigraded Hilbert functions are preserved.

### Top component and degree inequality

The exponent-difference hypothesis makes the torus map a closed immersion: the induced map on character lattices is surjective. Thus \(Z\) is irreducible of dimension \(n\). Equality of diagonal Hilbert polynomials shows \(\dim Y_0=n\), so \(Z\) is a top-dimensional component. Its generic multiplicity is at least one, while all mixed degrees of the globally generated \(H_i\) on other components are nonnegative. Therefore

\[
(H_1\cdots H_n\cdot Y)
\ge (H_1\cdots H_n\cdot Z).
\]

General hyperplanes avoid the boundary \(Z\setminus T\) by the standard incidence dimension count, and Bernstein--Kushnirenko gives

\[
(H_1\cdots H_n\cdot Z)=n!V(P_1,\ldots,P_n).
\]

The normalization agrees with the convention \(V(K,\ldots,K)=\operatorname{vol}K\). No equality \(Q=J\) or finite Khovanskii basis is required.

### Recommended small clarification

The multigraded Hilbert/fundamental-cycle step is standard but terse. For a self-contained import, add that irrelevant-torsion saturation does not alter the eventual multigraded Hilbert polynomial and that \(\mathcal O(1,\ldots,1)\) is ample on the product. This is explanatory, not a detected error.

## 7. Audit of Proposition `prop:movable-upper`

The proposition is correct.

- The proof of Xia, Proposition 10.3.1, really constructs, in one common degree, sections whose value differences are \(e_1,\ldots,e_n\). Raising them to a common multiple preserves those unit differences, so the lattice hypothesis of `lem:finite-level` holds for every \(k\in p\mathbb Z_{>0}\).
- For a big integral divisor, a sufficiently divisible complete linear system is birational. The complete system at level \(mp\) contains the \(m\)-th symmetric-power subsystem, hence its map is also birational.
- On a common resolution of all base ideals,
  \[
  \mu_k^*(kD_i)=M_{i,k}+F_{i,k},\qquad M_{i,k}\ \text{basepoint-free},\quad F_{i,k}\ge0.
  \]
  Thus \(k^{-1}M_{i,k}\) is a nef admissible approximation below \(\mu_k^*D_i\), and the movable-product inequality has the displayed direction.
- Xia, Proposition 10.3.4, gives Hausdorff convergence of the normalized finite-level bodies, including along the chosen arithmetic progression. Mixed-volume continuity then yields the assertion.

No unnoticed index factor appears: \(P_{i,k}\) is unnormalized, so division by \(k^n\) is exactly correct.

## 8. Audit of the analytic-singularity reduction

The strategy is correct but needs one notation bridge.

### Resolution and rationality

On a common projective log resolution,

\[
\pi^*c_1(L_i,h_i)=[D_i]+R_i,
\]

with \(D_i\) an effective \(\mathbb Q\)-divisor and \(R_i\) positive with locally bounded potentials. The non-pluripolar pullback invariance and the fact that divisorial currents are discarded give

\[
\int_XT_1\wedge\cdots\wedge T_n
=\int_YR_1\wedge\cdots\wedge R_n
=\alpha_1\cdots\alpha_n.
\]

Here \(\alpha_i=\{R_i\}=\pi^*c_1(L_i)-\{D_i\}\). Consequently \(\alpha_i\in N^1(Y)_\mathbb Q\), not merely \(H^{1,1}(Y,\mathbb R)\). Lemma 1.6.1 makes it nef, and \(\alpha_i^n>0\) makes it big. The manuscript should now choose a nef and big \(\mathbb Q\)-divisor (or \(\mathbb Q\)-line bundle) representing this numerical class. Without this sentence, \(\Delta_\nu(\alpha_i)\) and the application of `prop:movable-upper` look undefined.

With the representative understood, Xia's equation (10.22) gives, for every algebraic rank-\(n\) valuation,

\[
\Delta_\nu(L_i,h_i)=\Delta_\nu(\alpha_i)+\nu(D_i),
\]

and translation invariance removes the divisorial vectors from mixed volumes.

### Upper bound

The movable upper bound gives

\[
n!V(\Delta_\nu(\alpha_1),\ldots,\Delta_\nu(\alpha_n))
\le \langle\alpha_1,\ldots,\alpha_n\rangle.
\]

Since all \(\alpha_i\) are nef, the movable product equals the ordinary intersection. This matches the resolved mixed mass.

### Lower approximation and inclusion direction

Take a common ample \(\mathbb Q\)-divisor \(H\), a rational \(c>0\) with \(c\alpha_i-H\) big, and an effective \(\mathbb Q\)-divisor \(E_i\) in that rational class. With

\[
\beta_i=\alpha_i+\epsilon H,
\qquad
\alpha_i=\frac{1}{1+c\epsilon}\beta_i
+\frac{\epsilon}{1+c\epsilon}E_i,
\]

\(\beta_i\) is ample and Wilms' Theorem 1.1 applies exactly: it is stated for ample \(\mathbb Q\)-line bundles on an irreducible projective variety and uses the same mixed-volume normalization.

Multiplication by the canonical section of the effective summand gives

\[
\frac1{1+c\epsilon}\Delta_{\nu_\epsilon}(\beta_i)
+\frac\epsilon{1+c\epsilon}\nu_\epsilon(E_i)
\subseteq\Delta_{\nu_\epsilon}(\alpha_i).
\]

The inclusion direction is correct. The point term is only a translation, so multilinearity/homogeneity yields the factor \((1+c\epsilon)^{-n}\). Letting rational \(\epsilon\to0^+\) gives the desired lower bound.

For maximal clarity, say that numerical invariance replaces the class identity by a \(\mathbb Q\)-linear representative before applying section multiplication.

## 9. General analytic approximation

After repairing the positive-volume/positive-mass transition in Section 2 above, the final passage is correct.

The \(\mathcal I\)-model representative has positive mass and is \(\mathcal I\)-good (Xia, Example 7.1.2). Theorem 7.1.1 then supplies analytic-singularity approximants that are Kähler currents and converge in \(d_S\). For every approximation level, the analytic case gives equality. Xia, Theorem 6.2.1, gives convergence of the mixed non-pluripolar masses, and Proposition `prop:uniform-dS` gives uniform convergence of the mixed-body values, hence convergence of their suprema:

\[
\left|\sup_\nu f_j(\nu)-\sup_\nu f(\nu)\right|
\le\sup_\nu|f_j(\nu)-f(\nu)|\to0.
\]

This last elementary inequality could be displayed explicitly.

## 10. Mixed-volume normalization audit

All normalization factors are consistent.

- Convex mixed volume is normalized by \(V(K,\ldots,K)=\operatorname{vol}K\).
- The coefficient of \(t_1\cdots t_n\) in \(\operatorname{vol}(\sum t_iK_i)\) is \(n!V(K_1,\ldots,K_n)\).
- Bernstein--Kushnirenko therefore gives the toric mixed degree as \(n!V(P_1,\ldots,P_n)\).
- The diagonal partial-body theorem is \(\operatorname{vol}\Delta_\nu(L,h)=\operatorname{vol}(dd^ch)/n!\).
- Wilms' Theorem 1.1 is stated with \((L_1\cdots L_n)=n!V(\Delta(L_1),\ldots,\Delta(L_n))\).

Thus the final factor \(n!\) in Theorems `thm:main1` and `thm:main` is correct.

## 11. Exact external-source hypothesis audit

I checked the cited statements against the available primary sources rather than relying on the manuscript's paraphrases.

| Source invoked | What the source actually supplies | Audit result |
|---|---|---|
| Wilms, Theorem 1.1 (arXiv:2502.18441v3) | For any irreducible projective variety of dimension \(n\) and ample \(\mathbb Q\)-line bundles \(L_1,\ldots,L_n\), there is one admissible flag for which \((L_1\cdots L_n)=n!V(\Delta(L_1),\ldots,\Delta(L_n))\). | Exact match after \(\beta_i\) are explicitly treated as ample \(\mathbb Q\)-divisors. Smoothness is not required. |
| Kaveh--Manon, Lemma 2.16 | For the weighting matrix associated to a valuation, the matrix initial ideal is contained in the corresponding valuation/toric ideal. | Supports precisely \(Q=\operatorname{in}_{\mathsf A}(I)\subseteq J\), the needed direction. |
| Kaveh--Manon, Proposition 8.10 | For an ideal and rational weighting matrix, a scalar rational weight can be chosen with the same initial ideal. | Applies without assuming a finite Khovanskii basis. |
| Xia notes, Proposition 6.2.3 | After a subsequence, a \(d_S\)-convergent sequence of positive-mass model potentials admits monotone model upper and lower approximants. Its proof, not merely its statement, contains the endpoint order relative to the limit. | Sufficient for Lemma `lem:potential-sandwich` only if equation (6.15) and the end of Step 2 are cited explicitly. |
| Xia notes, Corollary 6.2.5 | Continuity of total non-pluripolar mass in the \(d_S\) metric. | Supplies a positive mass lower bound; does **not** imply pointwise order. |
| Xia notes, Theorem 6.2.1 | \(d_S\)-continuity of mixed non-pluripolar masses. | Exact match for the final analytic limit. |
| Xia notes, Theorem 7.1.1 | A positive-mass potential is \(\mathcal I\)-good iff it admits analytic-singularity \(d_S\)-approximants; the proof permits Kähler-current approximants. | Exact match after passing to the positive-mass \(\mathcal I\)-model envelope. |
| Xia notes, Proposition 10.3.1 | Its proof constructs same-degree section values whose differences are the standard basis vectors. | Supports the lattice-generation input in the movable upper bound. |
| Xia notes, Proposition 10.3.4 | Normalized finite-level partial bodies converge in Hausdorff distance to the partial body. | Exact match, including passage along a divisible arithmetic progression. |
| Xia notes, Corollary 10.3.2; Theorem 10.3.2; Propositions 10.3.8 and 10.3.10 | Respectively the diagonal volume formula, fixed-valuation \(d_S\)-continuity, monotonicity, and Minkowski/superadditivity. | These uses and all inclusion directions check out. |
| Xia notes, Remark 10.3.1, equation (10.22) | The partial body of an analytic singularity on a log resolution is the ordinary body of the residual nef class translated by the valuation vector of the divisor. | Exact match once a rational divisor representative of \(\alpha_i\) is selected. |
| Xia notes, Lemma 1.6.1 | The residual class after resolving logarithmic singularities is nef. | Supports the nefness claim used in the analytic case. |
| *Transcendental b-divisors I*, Theorem 3.5 | Identifies Cao's mixed volume with the Darvas--Xia/\(\mathcal I\)-envelope mixed volume. | This is the exact source needed at line 71 and in the preliminaries. |
| *Transcendental b-divisors II* | Its introduction recalls the equality and attributes it to the previous paper. | The current citation key `Xiabdiv2` is not the correct primary attribution. |

The original published paper *Partial Okounkov bodies and Duistermaat--Heckman measures of non-Archimedean metrics* states Conjecture 8.8 with exactly the normalization used here:

\[
\frac1{n!}\int_X c_1(L_1,h_1)\wedge\cdots\wedge c_1(L_n,h_n)
=\sup_v V\bigl(\Delta_v(L_1,h_1),\ldots,\Delta_v(L_n,h_n)\bigr).
\]

It does not impose a toric hypothesis. The supplied theorem therefore addresses the actual conjecture rather than a weakened special case.

## 12. Minimal repair packet

The following changes are sufficient; no redesign of the proof is needed.

1. **Repair the theorem's analytic domain.** Define Cao/\(\mathcal I\)-mixed volume on the positive-Cao-volume locus, and begin the proof by replacing every input by its \(\mathcal I\)-model envelope. Cite Proposition 3.2.6 for invariance of partial bodies and state explicitly that the replacement has positive non-pluripolar mass.
2. **Repair Lemma `lem:potential-sandwich`.** Replace the appeal to Corollary 6.2.5 for pointwise order by the actual monotone-envelope construction in the proof of Proposition 6.2.3, including equation (6.15) and the final paragraph of Step 2.
3. **Repair Lemma `lem:uniform-sandwich`.** Add the missing inclusions and state
   \[
   A_{i,j}\subseteq C_{i,j}\subseteq B_{i,j},
   \qquad
   A_{i,j}\subseteq D_{i,j}\subseteq B_{i,j}.
   \]
   Without them the lemma is false; with them its proof works.
4. **Make the finite diagonal extraction explicit.** Apply the potential sandwich successively for \(i=1,\ldots,n\) and retain one common subsequence.
5. **Choose divisor representatives.** After defining \(\alpha_i=\pi^*c_1(L_i)-\{D_i\}\), note that it belongs to \(N^1(Y)_\mathbb Q\) and choose a nef and big \(\mathbb Q\)-divisor representing it before writing \(\Delta_\nu(\alpha_i)\) or invoking Proposition `prop:movable-upper`.
6. **Spell out the effective-divisor inclusion.** Invoke numerical invariance and multiplication by the canonical section of a representative of \(E_i\); this removes any ambiguity between class identities and divisor identities.
7. **Correct the b-divisor citation.** Replace `Xiabdiv2` by `Xiabdiv` and cite Theorem 3.5.
8. **Optional exposition strengthening.** Add one sentence on multigraded irrelevant saturation/Hilbert polynomials and display
   \[
   |\sup_\nu f_j-\sup_\nu f|\le\sup_\nu|f_j-f|.
   \]

## 13. Integration recommendation

The supplied proof should be integrated only in a repaired form. A responsible editorial description would be:

> The following argument resolves Xia's Conjecture 8.8, conditional only on the cited results in Xia's 29 June 2026 notes and the stated 2026 preprints. We include the full argument because the mixed formula itself is not yet a result verified in the published literature.

That wording distinguishes a mathematically audited new proof from a theorem already established by the references. If the surrounding manuscript is intended to be self-contained or archival, the dependencies on the unpublished 2026 notes should either be reproduced as local propositions or frozen to a dated, publicly accessible version.

## 14. Bottom line

- **Initial degeneration:** valid; \(Q\subseteq J\) is the right direction, and no Khovanskii basis is required.
- **Movable upper bound:** valid.
- **Potential sandwich:** valid conclusion, invalid cited inference; repair from Proposition 6.2.3's proof.
- **Abstract convex sandwich:** false as written because two inclusions are absent; valid after adding both full sandwich chains.
- **Uniform \(d_S\):** valid after those two sandwich repairs.
- **Analytic-singularity reduction:** valid after choosing rational divisor representatives.
- **General analytic reduction:** valid only after explicitly passing from positive Cao volume to positive mass via \(\mathcal I\)-model envelopes.
- **Mixed-volume factors:** all \(n!\) normalizations are correct.
- **Publication/source status:** coherent integration candidate after repairs, not yet something that can be labelled a published proof.
