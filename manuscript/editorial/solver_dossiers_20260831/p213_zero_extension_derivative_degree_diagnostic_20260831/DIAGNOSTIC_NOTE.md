# Zero extension, derivative degrees, and safe modification transport

Date: 31 August 2026. Diagnostic author: `/root/p082_independent_reaudit`.

## Outcome and provenance

The parent's punctured-line objection is correct with the literal printed conventions. CLD Section 7.1.12's final, unqualified differential-commutation sentence cannot hold for all currents satisfying its preceding extension definition. The fixed-bidimension removability statement in Lemma 7.1.13 remains valid. The distinction is that differentiation lowers bidimension, so the dimension inequality that makes extension unique must be checked again in the derivative's test degree.

This is a bounded source diagnostic, not a claim that the CLD theory or its Poincare--Lelong theorem is wrong. The latter theorem provides an explicit internal check on the former sentence. The safe interpretation requires an additional proper-support or derivative-degree hypothesis. The literal source text does not state such a qualification; we do not attribute an intended correction to the authors.

Closed currents of bidegree (0,0) still transport safely across proper modifications with lower-dimensional analytic exceptional sets: their two first derivatives have the required dimension gap. For a continuous product uT, its d'd'' can instead be transported by proper pushforward after the product has been formed globally. No blanket zero-extension/d'd'' commutation is used.

The parent supplied the initial example and task. This author independently checked the conventions, degree ledger, printed source pages and the proofs below. No skeletal representation premise (R), P21.3 rigidity conclusion, current base change, or production acceptance is invoked. This new dossier does not edit any earlier frozen packet or live manuscript.

## 1. Conventions and what the source actually says

Work on good, separated, boundaryless K-analytic spaces over a complete nontrivially valued field K, with ordinary CLD forms and currents. When a space is pure n-dimensional, a current of bidimension (r,s) acts on compactly supported smooth forms of bidegree (r,s); its current bidegree is (n-r,n-s). Write D_{r,s} for bidimension and D^{a,b} for bidegree.

CLD Sections 7.7.1-7.7.3 define the derivatives by signed transposition. Thus

\[
 d':D_{r,s}\longrightarrow D_{r-1,s},\qquad
 d'':D_{r,s}\longrightarrow D_{r,s-1},\qquad
 d'd'':D_{r,s}\longrightarrow D_{r-1,s-1}.                 \tag{1}
\]

Restriction to an ordinary open set commutes with these operators: this uses extension by zero of COMPACTLY SUPPORTED TEST FORMS, which remains a legitimate compact test after differentiation. It must not be confused with extension of an arbitrary current from the open set.

For j:U -> X, CLD Section 7.1.12 defines extension by zero of a bidimension-(r,s) current S using compactness, in U, of the support of S wedge alpha|U for each compactly supported smooth (r,s)-form alpha on X. Its final sentence then asserts commutation with J and the differential operators without a further displayed restriction. Both the definition and this sentence are visibly printed on page 159; no lost text-extraction symbol explains the issue.

Lemma 7.1.13, printed pp.159-160, gives the precise fixed-degree statement: if d_trop(x)<max(r,s) at every point of X minus U, restriction of bidimension-(r,s) currents is bijective, with inverse zero extension. Indeed every ambient compact (r,s)-test has support in U. For a closed analytic subset Z of dimension less than max(r,s), CLD Proposition 15.2.1(b) establishes exactly this AMBIENT SUPPORT AVOIDANCE, not just vanishing of a pullback to Z. The lemma's printed proof has a separate complementary-index inconsistency in its displayed test-space notation; throughout this note the dual test degree is (r,s), as in Definition 7.1.1 and the first sentence of that proof. That typographical issue does not alter the support argument.

## 2. Explicit counterexample, including every degree and sign

Take X=(A^1_K)^an, U=(G_m,K)^an=X minus {0}, with coordinate z. This is a smooth, good, separated, boundaryless curve. The removed K-rational rigid point has d_K(0)=d_trop(0)=0. Put

\[
                  S_U=[\log|z|]\quad\hbox{on }U.
\]

The function log|z| is smooth on U and is affine in its tropical coordinate. On U, the current has bidegree (0,0), hence bidimension (1,1), and d'd''S_U=0 by CLD Lemma 16.7.4 and the boundaryless form-to-current identities in Section 7.7.

Every compactly supported (1,1)-form on X vanishes on a neighbourhood of 0 by Proposition 15.2.1. Consequently its support is a compact subset of U, and S_U satisfies Section 7.1.12's extension condition. Its extension S_X is unique by Lemma 7.1.13. This is EXACTLY the current denoted [log|z|] in CLD Section 16.7.2, not a different ad hoc extension.

The coordinate z is a regular holomorphic function, its Cartier divisor is the rational point 0 with multiplicity one, and Theorem 16.7.3 gives

\[
                    d'd''S_X=\delta_0.                       \tag{2}
\]

Here delta_0 has bidegree (1,1), bidimension (0,0), and acts on a smooth scalar test rho by rho(0). It is nonzero: a smooth compact source cutoff equal to one near 0 exists by Corollary 15.2.5. This verifies the sign and excludes a residue-degree ambiguity. On the other hand, zero extension of d'd''S_U=0 is zero. Therefore

\[
             d'd''(j_!S_U)=\delta_0\ne0=j_!(d'd''S_U).        \tag{3}
\]

This example also defeats the possible repair that merely asks both the original current and its derivative to admit zero extension. Set Q_U=d''S_U. It has bidegree (0,1), bidimension (1,0). Lemma 7.1.13 again gives a unique extension Q_X, since max(1,0)=1>0. Restriction commutes with d'', so uniqueness identifies Q_X=d''S_X without using Section 7.1.12's commutation claim. But d'Q_U=0, while

\[
                       d'Q_X=\delta_0.                       \tag{4}
\]

Both Q_U and its zero derivative extend, yet d' does not commute with that extension. The analogous d'' example follows from d''d'=-d'd''. Thus the defect is not peculiar to notation for the composed operator.

The original S_U is not d'-closed or d''-closed individually; it is only d'd''-closed on U. Also, log|z| does not extend as a finite continuous function at 0. Accordingly (3) is not a counterexample to a separately hypothesized continuous-potential theorem, nor to the closed-(0,0)-current transfer in Section 4.

## 3. Exact sufficient derivative-degree conditions

Let Z=X minus U be closed. Suppose S is a current of bidimension (r,s) on U. For each meaningful derivative (the corresponding indices are positive), the following are sufficient conditions pointwise on Z:

| Operation | Bidimension of result | Sufficient dimension inequality |
| --- | --- | --- |
| S -> j_!S | (r,s) | d_trop < max(r,s) |
| d' | (r-1,s) | d_trop < max(r-1,s) |
| d'' | (r,s-1) | d_trop < max(r,s-1) |
| d'd'' | (r-1,s-1) | d_trop < max(r-1,s-1) |

Under the appropriate row, extension exists in both the input and output degree and

\[
                         D(j_!S)=j_!(DS).                     \tag{5}
\]

Proof: the output inequality implies the input inequality. Thus both extensions exist. The two sides of (5) have the same restriction to U, since restriction commutes with D. Their difference is supported on Z and has the output bidimension. Lemma 7.1.13 in that OUTPUT degree makes restriction injective, so the difference is zero. Equivalently, every compact output-degree test already has compact support in U, and the signed-transpose calculation is then legitimate. For d'd'', the stronger output inequality also supplies the two intermediate degrees if one prefers two successive first-derivative calculations.

These inequalities are sufficient, not claimed necessary for a particular S. They explain (3): 0<1 permits extending bidimension (1,1), whereas the required inequality for bidimension (0,0) would be 0<0, which fails. When one of the indices of a proposed result is negative, that operator is zero by dimension conventions and the corresponding row is unnecessary.

There is a different, degree-independent safe condition. If the support of S is proper over X under j (equivalently, every compact subset of X meets it in a compact subset of U), then j_!S is the usual proper-support pushforward j_*S. All derivatives commute with this pushforward by transposition. For a compact test beta on X, choose a smooth compact cutoff in U equal to one near the intersection of supp(S) with supp(beta); derivative support is contained in supp(beta), and the cutoff-derivative terms miss supp(S). This proves commutation directly. The punctured logarithm does not satisfy this proper-support condition. Merely having the Section 7.1.12 degree-specific extension property is weaker.

## 4. Safe closed-(0,0)-current transport under modifications

Here is an exact formulation adequate for the present P21.3 transport diagnostic. Let pi:Y -> X be a proper analytic morphism between good, separated, boundaryless pure n-dimensional spaces, n>=1. Suppose closed analytic subsets E subset Y and Z subset X have dimension less than n and pi identifies Y minus E with X minus Z. In particular this applies to a proper modification once these usual exceptional-set properties have been verified; no extra component of Y entirely contained in E is allowed by the stated dimension assumption.

Given any current T_X of bidegree (0,0), restrict it to X minus Z, transport it through the genuine analytic isomorphism, and extend uniquely to Y in bidimension (n,n). Call the result T_Y. Existence and uniqueness follow from Lemma 7.1.13 and Proposition 15.2.1. This is a special construction in this degree, not a general pullback of currents along pi.

If T_X is positive, T_Y is positive: every compact (n,n)-test on Y has support outside E, and its positivity is preserved by the isomorphism. Conversely proper pushforward preserves positivity. If d'T_X=d''T_X=0, the two derivatives of T_Y vanish outside E. Their bidimensions are (n-1,n) and (n,n-1); both have maximum n. The dimension bound dim(E)<n therefore forces both derivatives to vanish on all of Y. This proves closedness WITHOUT differentiating an arbitrary zero-extension formula.

Finally pi_*T_Y and T_X agree on X minus Z and have bidimension (n,n) on X. Their difference vanishes by the same support theorem. Hence

\[
                            \pi_*T_Y=T_X.                    \tag{6}
\]

Conversely, if one starts with a closed positive (0,0)-current on Y, proper pushforward gives one on X; the construction just described recovers the original current because the two agree outside E and extension is unique. Thus pi_* is a bijection on these positive closed cones under the stated hypotheses. No scalar rigidity or representation theorem is a premise or consequence here.

The case n=1 is included: the derivatives have bidimensions (0,1) and (1,0), for which a zero-dimensional exceptional set is still invisible. The second derivative has bidimension (0,0), but it vanishes because the already established first derivatives vanish, not because all (0,0)-currents ignore rigid points.

## 5. Continuous products: the safe identity is proper pushforward

Continue with a positive closed T_X and the T_Y constructed in Section 4. Let u be a finite real continuous function on ALL of X and write v=u composed with pi. Products uT_X and vT_Y are well-defined currents of bidegree (0,0) by CLD Sections 7.2.11-7.2.12. Positivity supplies the Radon coefficient measures used in that definition. The products need not be closed or positive.

The following identities hold as actual global currents:

\[
 \pi_*(vT_Y)=uT_X,\qquad
 \pi_*d'd''(vT_Y)=d'd''(uT_X).                               \tag{7}
\]

For completeness, the first identity does not require pretending u is smooth. For a compact smooth (n,n)-test alpha on X, let mu_alpha^{T_X} be the signed Radon measure associated with T_X wedge alpha; define mu_{pi^*alpha}^{T_Y} similarly. These measures have compact support. By (6) and testing against smooth scalar functions, their pushforwards satisfy

\[
               \pi_*\mu_{\pi^*\alpha}^{T_Y}
                           =\mu_\alpha^{T_X}.                \tag{8}
\]

To justify equality as measures, first check it on smooth compact scalar tests using the smooth projection formula, and then use their density in continuous compact tests (CLD Corollary 15.2.7). For signed measures, apply this after expressing alpha as a difference of positive top forms; antisymmetric top forms vanish. Evaluating (8) on u, bounded on the relevant compact support, proves the first identity in (7). The second follows by proper pushforward commuting with d' and d'', via the signed-transpose definition. Properness ensures all pulled-back tests are compactly supported. No d'd''/zero-extension interchange enters either step.

Equally, uT_X and vT_Y are the unique bidimension-(n,n) extensions of their restrictions to the common open set. What is NOT supplied by that fact is

\[
     d'd''(uT_X)=j_!\bigl(d'd''(uT_X)|_{X\setminus Z}\bigr).  \tag{9}
\]

The derivative has bidimension (n-1,n-1). A dimension-only proof of (9) is valid if dim(Z)<n-1, but not when Z can be a divisor. In that borderline case, even existence in Section 7.1.12's sense for the restricted derivative must be checked, and any claim of no residual exceptional current requires an additional argument. Continuity alone has not been analyzed here as a substitute for that argument. In particular the noncontinuous logarithm example is not offered as a counterexample to a distinct continuous-product result. Identities (7) remain safe without deciding (9), and suffice when the desired conclusion is a proper-pushforward identity.

## 6. Exact Chapter 14 diagnosis, not live edits

The inspected `manuscript/parts/part2/ch14_currents.tex` has SHA-256 `4dc28ea36f841d71ff6f082a6e458d8c9fec3d150c802f241d5430c37dc9a1c7`. A numbered exact excerpt is frozen separately in this dossier so later live changes do not erase this review context.

1. Lines 389-421, `lem:ch14-extension-by-zero`, state the correct fixed-bidimension extension/uniqueness result. They do NOT repeat CLD's blanket differential-commutation sentence. The proof should be sourced to CLD Proposition 3.3.6/Lemma 7.1.13, or to Proposition 15.2.1 in the analytic-subset case. A mere dimension bound on the image of a cycle, which is what the cited Chapter 12 proposition states, is not by itself the source-support theorem needed here. No new counterexample to the lemma is asserted.

2. Lines 425-457 correctly distinguish invisible higher-bidimension currents from bidimension-(0,0) measures, and correctly avoid treating the whole rigid locus as a closed analytic subset. This is compatible with (2), not contradicted by it.

3. Lines 2195-2207, `prop:form-restriction-dimension-gap`, assert a pullback-vanishing statement under an INTRINSIC local tropical-dimension hypothesis on Z. The proposition does not explicitly assume dim(Z)<max(r,s) or the earlier AMBIENT pointwise d_trop bound. Abstractly, the equation i^*alpha=0 alone is weaker than ambient vanishing near Z, so the following warning at lines 2209-2215 is logically safe in that limited sense; this diagnostic does not call the whole paragraph false under its literal hypothesis. It does need a cross-reference to the earlier support theorem to avoid suggesting general non-removability in the stronger analytic lower-dimensional case. Under the additional hypothesis that Z is closed analytic with dim(Z)<max(r,s), CLD Proposition 15.2.1(b) DOES say that the ambient support avoids Z; consequently forms vanish on an ordinary neighbourhood of Z, and all bidimension-(r,s) currents extend uniquely. A safe editorial distinction is: arbitrary restriction-vanishing alone does not imply removability; the additional ambient pointwise-dimension/support hypothesis does. No equivalence between intrinsic tropical dimension of an arbitrary embedded subspace and the required ambient bound is proved or silently assumed here.

4. Lines 2225-2239, `thm:ch14-support-dimension`, correctly use the ambient pointwise d_trop inequality and fixed bidimension. The proper-pushforward differential and projection formulas at lines 2280-2355 are of the safe type used in (7), not the open-inclusion zero-extension type refuted by (3).

No correction is made in the live chapter. The exact bounded recommendation is to keep the fixed-degree support lemma, distinguish its input and derivative degrees explicitly, clarify the later warning in the analytic lower-dimensional case, and use (7) when continuous products are transported by a proper modification. Whether a particular downstream proof needs the stronger statement (9) must be checked in that proof; it is not certified by this diagnostic.

## 7. Verification and limits

The source PDF was inspected visually at printed/physical pages 159, 160, 423 and 460 after local PNG rendering. These show the literal extension sentence, the following removability lemma, the ambient support theorem, and both the logarithmic extension definition and Poincare--Lelong formula. The PDF skill was used specifically for that source verification; no PDF was edited or newly authored.

Source versions, exact input hashes and reviewed line ranges are recorded in `SOURCE_LEDGER.md`; the new packet is independently reviewable but not production-accepted. The assertion of a missing qualification is limited to the literal sentence tested by (3)-(4). No global claim about CLD correctness, no assertion about arbitrary continuous-product removability, no all-current pullback, and no P21.3 solution is made.
