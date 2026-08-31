# Residual-curve functional interface: bounded research result

Date: 31 August 2026. Author: p213_skeletal_hostile.

## Outcome and gate

The accompanying statement and proof construct the missing positive divisor functional in one explicit semistable surface neighbourhood:
\[
 X=\{|\pi|<|z|<1\}\times_K C^{\mathrm{an}},
\]
where \(K\) is complete discretely valued with perfect residue field \(k\), and \(C\) has a smooth proper model with geometrically connected fibres. The codimension-one stratum of the product node model is the whole proper residual curve \(C_0\).

For every positive closed ordinary CLD current \(T\) of bidegree \((0,0)\), the construction gives finite numbers \(b_T(p)\geq0\), one for every closed \(p\in C_0\), and proves
\[
 \sum_p\operatorname{ord}_p(f)b_T(p)=0
 \quad\text{for every }f\in k(C_0)^\times.
\]
Therefore \(b_T(p)=c[\kappa(p):k]\). The proof of the principal relation is the new analytic interface, not just a repetition of the elementary divisor-functional lemma.

This is an authored research candidate, NOT an independent acceptance or a production-verified result. No live source or frozen prior packet was changed; no production call was made. No PDF or compiled artifact is claimed. This is not a solution or retirement of P21.3, and it does not even assert \(T=c\delta_X\) on the whole displayed product.

## Assumptions versus proved conclusions

| Item | Role in this packet |
|---|---|
| Complete DVR, perfect residue field | Explicit restriction of scope; not arbitrary complete nontrivially valued \(K\). |
| Smooth proper good-reduction curve, entire proper residual \(C_0\) | Explicit geometry; not inferred from an arbitrary affine etale chart. |
| Product annulus coordinate \(z\) | Explicit geometry; not a locally defined coordinate silently globalized along \(C_0\). |
| Positivity and \(\mathrm d'T=\mathrm d''T=0\) | Hypotheses on the actual analytic current. Only \(\mathrm d'\)-closedness is used in the displayed tests. |
| Tube of \(p\) is a disc over the unramified \(K_p\) | Proved from the completed smooth local ring and henselian lifting. |
| Finite constant \(b_T(p)\) on its product collar | Proved by a properly supported pushforward to an actual Euclidean rectangle and zero distributional derivatives. |
| Every residual \(f\) lifts with the exact collar slope | Proved using the generic special-fibre DVR and dominant terms in bounded formal power series. |
| Principal-divisor annihilation | Proved using a finite source cutoff and an explicit compactly supported \((1,2)\)-test. |
| Chartwise source-calibration representation | Assumed only for interpreting \(b_T(p)\) as a calibration coefficient; not proved or certified here. |
| Source/calibration compatibility on general refinements | Not assumed to perform the construction; not established in general. |

The functional is finite-valued on each finite divisor. It is not asserted to be a finite-total-mass measure on the set of all residual closed points.

## What closes the previously missing interface here

A source collar has actual coordinates \(u=v(z),s=v(w_p)\). Compact inverse images of compact rectangles make every test legitimate without a source properness fiction. Positive closedness makes its coefficient a single constant \(b_T(p)\).

For a residual rational function \(f\), choose a rational lift \(F\). On an outer collar at \(p\), the equality
\(v(F)=m_ps\), \(m_p=\operatorname{ord}_p(f)\), holds on the whole ordinary source collar, not merely on its skeleton. Deeper zeros and poles may occur, even where \(m_p=0\). They are all inside finitely many tubes.

A smooth cutoff \(\eta\) truncates precisely those tubes. For
\[
 \beta=\varphi(u)\chi(v(F))\,
     \mathrm d'u\wedge\mathrm d''u\wedge\mathrm d''v(F),
 \quad \int\varphi=1,\quad \chi=1\text{ near }0,
\]
the cutoff error is zero as a smooth form. In a transition collar with nonzero \(m_p\), its support is outside that of \(\chi\). In a transition collar with \(m_p=0\), \(\mathrm d''v(F)=0\). Properness of the curve factor makes \(\eta\beta\) compactly supported after the annulus cutoff.

Consequently closedness gives
\[
 0=\langle T,\mathrm d'(\eta\beta)\rangle
   =\sum_p b_T(p)
       \int_0^{\delta_p}m_p^2\chi'(m_ps)\,\mathrm ds
   =-\sum_p m_pb_T(p).
\]
The source form is decomposed into finitely many forms supported in disjoint individual collars before pairing. Hence the relation involves individual source coefficients, not just an inseparable sum on a tropical target.

No current is sliced or restricted to a hypersurface. No arbitrary-current field-extension pullback is used. No global dominating Radon measure is used. No appeal to generic full-rank compatibility is made.

## Residue and lattice diagnostics

### A degree-two residual point is one source collar

Take \(K=\mathbf R((\pi))\), \(C=\mathbf P^1_K\), and the standard model. Let \(p\) be the closed point of \(C_0=\mathbf P^1_{\mathbf R}\) defined by \(T^2+1\), and let \(q=\infty\).

Then \(\kappa(p)=\mathbf C\), \(K_p=\mathbf C((\pi))\), and the tube of \(p\) is one disc over \(K_p\), viewed over \(K\). It is not two ordinary source sheets over a \(K\)-Gauss point. In its completed local ring, Hensel lifting gives a coefficient \(i\) with \(i^2=-1\), and \(w=T-i\) is a parameter. On the disc,
\[
 F=T^2+1=w(2i+w),\qquad |F|=|w|
\]
on its outer collar. At \(q\), use \(w_q=1/T\):
\[
 F=w_q^{-2}(1+w_q^2),\qquad |F|=|w_q|^{-2}.
\]
The residual divisor is \(p-2q\). The actual test yields
\[
 b_T(p)-2b_T(q)=0.
\]
The canonical coefficients are \(2\) at \(p\) and \(1\) at \(q\), so the canonical relation is \(2-2=0\). Using unit canonical weights at both points would give a false normalization.

This coefficient \(2\) is exactly the finite-ground-field factor in CLD Remark 14.4.3. It is not an additional factor to multiply into \(\operatorname{ord}_p(f)\) after \(b_T(p)\) has already been defined.

### Nonprimitive coordinates have an index factor

If one replaces \(w_p\) by \(w_p^e\), \(e\neq0\), then \(t=es_p\). Pulling back a positive target top form gives \(e^2\) from its two transverse differentials, and change of variable gives \(1/|e|\). The pushed top coefficient is therefore \(|e|b_T(p)\), and its canonical coefficient is \(|e|d_p\). The ratio is unchanged, but this target coefficient must be divided by \(|e|\) to recover the primitive \(b_T(p)\).

The proof fixes a genuine formal uniformizer, hence a primitive transverse coordinate, and the actual annulus coordinate \(z\). In the principal-divisor boundary integral the final factor is the signed \(m_p\), not \(|m_p|\) or \(m_p^2\).

### Zero residual slope can hide deeper zeros and poles

Over \(K=\mathbf C((\pi))\), take \(C=\mathbf P^1_K\) and
\[
 F=(T-1)\frac{T-\pi}{T-2\pi}.
\]
Its reduction is \(f=T-1\). The residual point \(T=0\) has \(m_p=0\), although a zero and a pole of \(F\) lie deeper in that tube. On its outer collar \(|F|=1\), so the cutoff derivative there wedges with \(\mathrm d''v(F)=0\).

This point must be included in the finite bad set when constructing the cutoff, even though it is absent from \(\operatorname{div}(f)\). A test using only the global tropical target \(v(F)\), without localization, would also see the deeper zero/pole branches; the proof does not silently identify those with residual directions at the original face.

## Exact limits of the result

The proof uses the entire proper curve factor, not merely the affine residual curve in one standard etale chart. Removing residual points would omit terms of principal divisors. Properness is also what makes the finite source cutoff compact.

It uses a global annulus coordinate independent of the curve factor. A general semistable neighbourhood can have nontrivial normal-bundle transition functions; no reduction of those transitions to this product argument is supplied. General higher-dimensional slope formulas can contain intersection-theoretic tangential corrections, and they cannot be replaced by this product calculation without proof.

The construction compares the source Gauss-plane collars emanating from this one proper residual curve. It does not account for every cell of every moment chart on \(X\), all source sheets of general finite maps, propagation through arbitrary semistable neighbourhoods, imperfect residue fields, nondiscrete valuations, or the positive bidegrees occurring in P21.3.

Accordingly the existing broad residual-curve interface in the prior obstruction note is narrowed in this product case, not closed in its full generality. P21.3 remains open. Any further use requires independent mathematical review of these exact bytes and the existing production gate.

