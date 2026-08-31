# Research status: annular torsor residual-curve functional

Date: 2026-08-31. Author: /root/p213_skeletal_hostile.

## Outcome and gate

The new statement and full proof extend the product residual-functional construction to the formal-metric annular torsor of an arbitrary line bundle on the SAME entire smooth proper geometrically connected good-reduction model over a complete DVR with perfect residue field.

No degree, nefness, or triviality assumption is added to that line bundle. In particular the explicit double-curve normal bundles can be \(\mathcal O(1)\) and \(\mathcal O(-1)\), not both trivial.

For an actual positive closed ordinary CLD \((0,0)\) current \(T\), the construction gives finite nonnegative collar coefficients \(b_T(p)\), a positive finite-valued functional on \(\operatorname{Div}(C_0)\), and

\[
 \sum_p\operatorname{ord}_p(f)b_T(p)=0,\qquad
 b_T(p)=c[\kappa(p):k]\quad(c\geq0).
\]

The current test and principal relation do not assume the separate chartwise representation. ONLY the final interpretation of these constants as source-calibration coefficients assumes that representation.

This is a new research packet. At freeze it has not been independently accepted, production-submitted, or integrated. The previous product packet and its independent audit remain unchanged. No full-P21.3 theorem or whole-torsor scalar rigidity claim is made.

## What is imported, proved, conditional, and unresolved

| Interface | Status in this packet |
| --- | --- |
| Ordinary CLD currents and log-unit test forms | Primary CLD definitions; compact support checked explicitly. |
| Formal metric as continuous norm, not automatically ordinary smooth | Primary CLD17.1 and17.7; exact local use explained. |
| Completed residual disc and unramified \(K_p\) | Same hypotheses and explicit completed-ring calculation as independently audited product packet. |
| Line bundle trivialization on each completed residual disc | Proved from the free rank-one completed module; analytic convergence and norm one recorded. |
| Existence of a normalized rational section and arbitrary rational-function lift | Proved using the generic-special-fibre DVR. |
| Entire-collar slopes of section norm and residual function | Proved by dominant power-series terms. |
| Uniform smallness of the section weight on the smooth cutoff support | Explicit choice \(|n_p|b_p'<\gamma\). |
| Compact support in the annular torsor | Proved with radial margin and proper projective-bundle compactification. |
| Integral shear and principal relation | Fully computed on actual source forms. |
| Canonical residue factor | CLD14.4.3 finite-ground-field restriction; no ordinary-sheet inference. |
| Source-calibration interpretation | Conditional on separate representation packet, exact inputs recorded in manifest. |
| Chern identity for the continuous radial norm | Separate exact canonical-current identity; never wedged with \(T\). |
| All possible source cells/current separation | Not proved. |
| Nonlinear semistable formal deformations not given by a line-bundle torsor over the entire model | Not proved to be isomorphic to this model; no transfer asserted. |
| Imperfect residue, nondiscrete valuation, nonproper residual curve, or no good reduction | Outside the displayed theorem. |
| Full P21.3 | Remains open. |

## The missing gluing step and its repair

The product proof used a globally defined independent annulus coordinate. An arbitrary formal line bundle has no such coordinate. Norm-one formal frames have norm-one transition functions on their common analytic domains, but those domains are not an ordinary open cover around the proper residual curve. Neither ordinary smoothness nor globally vanishing curvature of the metric radius follows.

The proof chooses one rational section \(\sigma\) normalized to have zero vertical order. It is an actual analytic frame on the ordinary open complement of its horizontal zero/pole divisor. On that locus the fibre coefficient \(a\) is an analytic unit and \(r=v(a)\) is a legitimate ordinary smooth coordinate. The global radius \(u\) is kept only as a continuous function for support estimates.

On a residual collar, \(h_\sigma=-\log\|\sigma\|=n_ps\), so \(r=u-n_ps\). This shear is in \(\operatorname{SL}_2(\mathbf Z)\). The compactly supported principal test uses \(r\), not a globally differentiated \(u\).

The cutoff has to avoid both the chosen section divisor and the lifted rational-function divisor. All their specializations enter the finite bad set, including order-zero cancellations. Its outer transition collars are chosen sufficiently small to make \(|h_\sigma|<\gamma\) on its entire support. Then \(\varphi(r)\) has support within a fixed compact radial strip \(0<a\leq u\leq b<\ell\).

The normal-bundle shear translates the fibre integral but does not change it:

\[
 \int_0^\ell\varphi(u-n_ps)\,\mathrm du=1
\]

on the support of the transverse differentiated test. The proof checks the translation margin explicitly, so neither annulus boundary is silently crossed.

## Curvature is not erased

CURVATURE_AND_EXAMPLES.md gives the exact separate identities

\[
 \mathrm d'\mathrm d''[u]=c_1(\rho^*\overline L),\qquad
 \mathrm d'\mathrm d''[h_\sigma]
     =c_1(\overline L)-\delta_{\operatorname{div}_C(\sigma)}.
\]

They concern curvature currents of continuous metrized line bundles and locally integrable section weights. No multiplication of the arbitrary \(T\) by these currents, no general current pullback, and no slicing are claimed.

The \(\mathcal O(1)\) example gives a nonzero section-divisor degree and an explicit original-field analytic map with pulled-back radial function \(\max(t,\ell-t)\). The latter has a nonzero second-derivative test equal to \(2h(\ell/2)\). Thus the shortcut which treats the global radius as a harmonic log-unit is concretely false. The principal-function relation nevertheless survives via the rational-section shear test.

## Remaining geometric gap to general semistable strata

Knowing the normal bundle of a proper double curve is not the same as exhibiting an actual formal neighbourhood as the displayed torsor over a lift \(\mathcal C/R\). General formal neighbourhoods can contain higher-order gluing/deformation data. This packet does not construct a retraction to such a proper lifted curve or show that those data can be ignored by arbitrary currents.

Even in the displayed torsor, the proven tests see the individual product collars. They do not prove separation of every top test form or propagation to cells on which the radial coordinate loses rank. The earlier source-calibration representation, if valid, reads the constants on these specific injective source Gauss planes; it does not turn this result into a classification of all source coefficients.

These are actual unproved interfaces, not counterexamples to P21.3.

## Artifact boundary

Only this new directory is authored. No live chapter, old dossier, prior audit, production record, or permission setting was changed. No git command was run. Source PDFs were read and rendered only. The exact-byte manifest records the current candidate and all named mathematical inputs. No TeX compilation or PDF output is claimed by this packet.
