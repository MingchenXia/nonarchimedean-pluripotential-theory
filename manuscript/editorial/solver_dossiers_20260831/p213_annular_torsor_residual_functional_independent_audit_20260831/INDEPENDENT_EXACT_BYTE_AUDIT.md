# Independent exact-byte mathematical audit: annular-torsor residual functional

Date: 2026-08-31  
Reviewer: /root/p081_weighted_repair_fresh  
Candidate author: /root/p213_skeletal_hostile

## Verdict and scope

**Independent mathematical PASS for the frozen bounded statement and proof: no unresolved substantive gap found.** The separate source-calibration representation remains an explicit conditional input only for the final calibration interpretation. This report does not certify that representation, prove scalar rigidity on the whole torsor, or authorize production or manuscript integration.

The reviewed space is the formal-metric annular torsor of **any** line bundle on the entire smooth proper geometrically connected good-reduction curve model specified in the statement, over the original complete discretely valued field with perfect residue field. There is no degree, nefness, trivial-normal-bundle, algebraically closed field, or split-residue restriction.

The unconditional bounded conclusion is the construction, from the actual positive closed ordinary CLD current, of finite collar coefficients and a positive divisor functional annihilating principal divisors, hence \(b_T(p)=c[\kappa(p):k]\). Only the source-Gauss-plane calibration interpretation is conditional. Neither the proof nor this review upgrades that assertion to all source cells or to \(T=c\delta_X\).

## Exact object and review independence

The candidate directory is:

/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260831/p213_annular_torsor_residual_functional_research_20260831

| Frozen object | Bytes | SHA-256 |
|---|---:|---|
| statement.tex | 3179 | 19baf4828b51e2b36370a2ececd41ad5802f01e3cf41c90f00df9b8bacec773a |
| proof.tex | 15567 | f851830312841ef4d8825ba4b049a718a16820ef3888263721278bf7a06c99fe |
| CURVATURE_AND_EXAMPLES.md | 9047 | b88523c7d72f143f2093d3803d6b64886ac7d8ff0d872a4f30678df41a543c0a |
| MANIFEST.json | 5455 | ec7f22f0fd750a325139c2f7403e213b53e921b5f1f89e5ab45ac6e0f059da30 |

The read-only checker independently verified every one of the 15 manifest entries (8 inputs and 7 outputs), as well as the four announced hashes above. All matched. All candidate mathematical text, examples, source/status ledgers, bibliography, and validation/manifest data were read. The primary CLD source interfaces listed in SOURCE_LEDGER.md were read directly in the exact local source text. No visual PDF inspection or TeX compilation was performed by this reviewer in this audit.

I did not author or modify the torsor statement, proof, or examples. Before freezing, I supplied the author the location and sign convention of CLD §§18.1.1–18.1.3 as a source-locator pre-audit; I supplied no replacement argument. I also previously performed a syntax/reference build of the product predecessor, not authorship of that mathematical result. These limited prior contributions are disclosed rather than presented as complete isolation from the project. The present verdict followed review of the exact frozen proof. The source-calibration proof is not freshly accepted by this audit; its frozen bytes are recorded only as an excluded conditional input.

## 1. Actual original-field geometry and collar distribution

Proof lines 5–20 give the pairing hypersurface in \(\mathcal L\oplus\mathcal L^{-1}\). In a local frame it is \(xy=\pi\) over a smooth relative curve. Its two special components are the total spaces of the two dual line bundles, meeting in the entire proper residual curve. Their normal bundles are indeed \(\mathcal L_0\) and \(\mathcal L_0^{-1}\). The open radial locus is the indicated smooth boundaryless analytic surface. This construction does not assert that an arbitrary semistable neighbourhood has this global torsor form.

For a closed residual point, perfection gives a finite separable residue extension and thus the finite unramified coefficient ring in the completed local ring. Formal smoothness supplies \(R_p[[w_p]]\); the rank-one module becomes free there. The power-series basis and coordinate converge on the open residue disc, as seen on the exhausting subdomains \(|w_p|^N\leq|\pi|\). Thus each collar really is an ordinary open product over \(K_p\), viewed over \(K\), not an ordinary-open cover obtained from formal trivializations.

The inverse image of a compact target subset is contained in a closed polyannulus with all radii strictly inside the collar. It is compact. Consequently every compact target test and the coordinate-deleted primitives used in lines 80–99 extend by zero with compact analytic support. Positivity supplies a finite sup-norm bound on each fixed compact target set, hence a positive Radon measure. Closedness kills its two distributional partial derivatives. Convolution on relatively compact balls and overlap then give a single finite nonnegative constant on the connected rectangle. No representation theorem, slice, or pointwise density of \(T\) is used.

Changing the completed frame multiplies by a power-series unit of norm one throughout the disc. Changing parameter preserves its norm on a sufficiently outer ordinary collar: the linear term is a unit, the constant term is \(\pi\)-divisible, and the remaining terms are bounded. This verifies independence as an equality of actual functions and forms, not merely of skeletal values. Shrinking collars preserves the already determined constant.

## 2. Normalized rational section and complete bad set

At the generic special-fibre DVR a basis of the line bundle is a rational section with vertical order zero. Its reduction is therefore a nonzero rational section of \(\mathcal L_0\). This is not a global trivialization, and its residual orders \(n_p\) need not sum to degree zero. A lift of a residual rational function can similarly be chosen with vertical order zero, giving the unrelated principal orders \(m_p\).

The bad set includes every specialization of a horizontal zero or pole of either the section or the function. On the proper regular surface this set is finite. In particular, a zero and pole that cancel after reduction must still be retained. This resolves the otherwise dangerous \(m_p=0\) branches and the \(m_p=0,\ n_p\ne0\) branches.

After removing the common vertical power from a completed numerator/denominator, its first nonzero reduced monomial strictly dominates all other terms sufficiently near the outer end of the disc. Thus
\[
h_\sigma=n_ps,\qquad t=m_ps
\]
hold on the **whole ordinary collar**. Outside the finitely many bad tubes the relevant local formal coefficients are units, so their norms equal one. The proof explicitly uses this last statement pointwise and never incorrectly upgrades it to ordinary-open constancy at the good-reduction point.

On the ordinary complement of the horizontal divisors, \(\sigma\) is a genuine analytic frame. The function \(a=\xi/\sigma\) is an invertible analytic function there, and \(r=v(a)\) is an ordinary smooth log-unit function. Hence
\[
u=r+h_\sigma,\qquad r=u-n_ps
\]
on a collar. It is \(r\), not the globally continuous metric radius \(u\), that is differentiated.

## 3. Compact support: the essential new torsor issue

The two-sided metric strip with radius bounded strictly between 0 and \(\ell\) is compact. Indeed the total line bundle compactifies to a projective bundle over a proper curve; the original norm and the dual norm at infinity extend continuously and tend to zero at the respective sections. The fixed positive upper and lower norm bounds therefore cut out a closed subset of that compactification avoiding both sections.

The proof chooses a finite family of base cutoffs only after fixing the radial support and a positive margin \(\gamma\). The inequalities \(|n_p|b'_p<\gamma\) imply
\[
|h_\sigma|<\gamma\quad\hbox{on }\operatorname{supp}\eta.
\]
The cutoff is ordinary smooth: its complement in each tube is constant near the centre and supported in a compact closed disc strictly inside that ordinary open tube, so zero extension is legitimate. It vanishes near every removed horizontal divisor and its base support is compact and contained in the analytic frame locus.

It follows that \(\eta\beta\) is supported where
\[
A-\gamma\le u\le B'+\gamma,\qquad
0<A-\gamma<B'+\gamma<\ell.
\]
Its support is closed in \(X\) and contained in the compact strip above. This rules out escape to either annular boundary even though \(r\) is not the global metric radius. The empty-bad-set case is explicitly handled without taking a maximum over an empty set.

## 4. Cutoff cancellation, shear, and signed principal relation

On a transition collar with \(m_p\ne0\), \(\chi(t)=0\) by the chosen separation of supports. With \(m_p=0\), \(t\) is identically zero on an entire ordinary collar, and \(\mathrm d''t=0\) kills the primitive even if \(n_p\ne0\). Thus the cutoff error vanishes as a source form before pairing with \(T\).

Differentiating the primitive uses only the log-units \(r,t\). The derivative of \(\varphi(r)\) dies by repetition of \(\mathrm d'r\), and the second derivatives of the log-units vanish. The remaining form is the one in proof lines 274–277. Its nonzero support is in finitely many disjoint ordinary collars, bounded away from both radial boundaries and from \(s=0\). At the good-reduction point and every point outside the bad tubes, continuity of \(t\), together with the interval on which \(\chi'=0\), gives an ordinary neighbourhood of vanishing. There is no unaccounted central current term.

The integral shear has determinant one. In the top wedge, all terms containing an extra \(\mathrm d's\) or \(\mathrm d''s\) vanish, leaving the factor \(m_p^2\), with no extra factor from \(n_p\). On every relevant transverse value the translated radial support remains inside \((0,\ell)\), so its radial integral remains exactly one. The signed transverse integral is
\[
\int_0^{\delta_p}m_p^2\chi'(m_ps)\,\mathrm ds
=m_p\bigl(\chi(m_p\delta_p)-\chi(0)\bigr)=-m_p
\]
for either sign of \(m_p\). Replacing this by an absolute order would be wrong; the frozen proof does not do so.

Closedness now gives every principal relation. The proof does not need the radial integral identity where the outer integrand is zero. This avoids any hidden demand for globally small section weight or a globally trivial line bundle.

## 5. Degree factorization and canonical normalization

Every divisor has finite support, so finite collar values define a finite-valued homomorphism; the proof correctly does not call this a finite measure on all residual points.

For a degree-zero divisor \(D\), a fixed effective \(H\) with \(\deg H+\chi(\mathcal O_{C_0})>0\) makes \(H+jD\) linearly equivalent to an effective divisor for every integer \(j\), by Riemann–Roch. Positivity and the principal relations therefore force \(\lambda_T(D)=0\). Applying this to \((\deg q)p-(\deg p)q\) yields \(b_T(p)=c\,d_p\), with no need for a rational residual point.

A primitive product collar over \(K_p\) has canonical coefficient one. CLD Remark 14.4.3 multiplies this calibration by \([K_p:K]=d_p\) on restriction of the base field. It does not decompose the source into ordinary sheets. There is no extra ramification or shear determinant factor. The conditional source-representation conclusion concerns only the displayed injectively tropicalized Gauss plane, on which compact tests identify the coefficient. It cannot infer anything about untested source cells.

## 6. Curvature identities and stress examples

The tautological section of \(\rho^*L\) is analytic and nowhere zero on \(X\). Applying the definition of curvature to its continuous metric potential gives
\[
\mathrm d'\mathrm d''[u]=c_1(\rho^*\overline L).
\]
Here the right side denotes curvature of a pulled-back metrized line bundle, not an undefined pullback of an arbitrary current. CLD Poincaré–Lelong gives the stated minus sign in
\[
\mathrm d'\mathrm d''[h_\sigma]
=c_1(\overline L)-\delta_{\operatorname{div}_C\sigma}.
\]
CLD Proposition 18.5.1 applies to this normal proper model with irreducible special fibre. It imposes no nefness or positivity condition on the line bundle; in dimension one it gives \((\deg_K L)\delta_{\xi_0}\), including negative degree. Thus the appendix legitimately distinguishes the section divisor from a principal function divisor. No product with \(T\) is formed.

All stress examples check:

- For \(\mathcal O(1)\) on \(\mathbf P^1_R\), \(\sigma=X_0\) has \(h_\sigma=\max(0,\log|Z|)\) and \(n_\infty=1\). Taking \(F=Z\) gives \(m_0=1,\ m_\infty=-1\); the shifted integral at infinity has sign \(+1\), while the principal relation is \(b_T(0)-b_T(\infty)=0\). The section divisor itself has value \(c\), not zero.
- The analytic map over the original field, \(Z=T^2/\pi,\ j(T)=T\sigma(Z)\), lands in \(X\) because \(u\circ j=\max(t,\ell-t)\) with values strictly inside the allowed radial interval. Primitive-coordinate integration gives \(2h(\ell/2)\) for its second-derivative test. The radius \(\ell/2\) need not be the valuation of a field element; the analytic annulus and its Gauss point exist without adjoining a square root of \(\pi\). This is a calculation with a pulled-back continuous function, not a current pullback or a slice. It rules out a global harmonic log-unit radius without claiming every possible nonsmoothness statement.
- Over \(\mathbf R((\pi))\), the point \(Z^2+1\) has residue degree two, not two ordinary tubes. The weights in \(b_T(p)-2b_T(\infty)=0\) are canonically \(2-2=0\), with no additional factor from the infinity shear.
- For \(F=(Z-1)/(Z-2)\), infinity has \(m_\infty=0,\ n_\infty=1\), and the cutoff term vanishes through \(\mathrm d''t=0\). The displayed deeper cancelling zero/pole pair also belongs to the bad set despite residual order zero.

## 7. Nonblocking presentation findings and remaining gates

No mathematical revision is requested. Three presentation/build observations are recorded externally; the frozen bytes were not changed:

1. In statement lines 34–48, \(\Omega_p\) is written using the source coordinate names and then appears inside \(q_p^*(h\Omega_p)\). This is naturally understood as the identically named coordinate volume form on the target rectangle before pullback. A future typesetting pass should make that convention explicit, or write \(h(u,s)\Omega_p\) on the source. It is not a literal pullback of an already defined source form.
2. Exponential \(e\) remains italic in proof line 69 and the norm expression in the examples. A future authorized integration should apply the requested roman exponential styling. This is not a mathematical issue.
3. The bibliography note contains the literal filename SOURCE_INTERFACE.md with an unescaped underscore. The parent reported a BibTeX-generated TeX failure from this field and a wrapper-only workaround under test. The character is present in the exact frozen bibliography. This reviewer did not compile or validate that workaround. It does not affect the mathematical source identity.

The structural checker found eight labels, seven references, no missing or duplicate labels, the single resolved CLD25 citation key, balanced environments/braces, and no prohibited control characters. These checks are not substituted for the mathematical review.

The live manuscript, all frozen candidate and predecessor files, and all prior audits remain untouched. No production call, git action, PDF creation, or permission bypass was performed. Production acceptance remains pending; a bounded mathematical PASS is not a P21.3 retirement or an integration decision.

