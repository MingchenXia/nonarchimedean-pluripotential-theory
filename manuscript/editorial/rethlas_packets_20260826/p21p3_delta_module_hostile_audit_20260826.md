# P21.3 delta-module packet: hostile mathematical audit

**Date:** 26 August 2026
**Verdict:** **PASS; production-ready in the exact scope stated below**

## Frozen bytes audited

- Statement: `p21p3_delta_module_statement_20260826.tex`
  SHA-256: `e0a34aabb30fa39e6df0528f023f3ce01fd2ca2277dd2b24d7160c1acdeaa935`
- Proof: `p21p3_delta_module_proof_20260826.tex`
  SHA-256: `c91e294d7d0c2f68b97969e6bfcd93a6388f014de5b6a12504eca849a6c854d1`

The final audit was performed against these exact bytes.  The statement and
proof were not modified while this record was written.

## Mathematical conclusion

Let \(\alpha\in B^{a,b}_{\mathrm{GK}}(W)\) and
\(T\in E^{p,q}_{\mathrm{GK}}(W)\).  With total degrees
\(A=a+b\) and \(P=p+q\), the packet correctly proves

\[
 \mathrm d'(\alpha\wedge T)
 =\mathrm d'\alpha\wedge T+(-1)^A\alpha\wedge\mathrm d'T,
 \qquad
 \mathrm d''(\alpha\wedge T)
 =\mathrm d''\alpha\wedge T+(-1)^A\alpha\wedge\mathrm d''T,
\]

and hence

\[
\begin{aligned}
 \mathrm d'\mathrm d''(\alpha\wedge T)
 ={}&\mathrm d'\mathrm d''\alpha\wedge T
   +(-1)^{A+1}\mathrm d''\alpha\wedge\mathrm d'T\\
 &+(-1)^A\mathrm d'\alpha\wedge\mathrm d''T
   +\alpha\wedge\mathrm d'\mathrm d''T.
\end{aligned}
\]

Consequently, if \(T\) is both \(\mathrm d'\)- and
\(\mathrm d''\)-closed, then

\[
 \mathrm d'\mathrm d''(\alpha\wedge T)
 =\mathrm d'\mathrm d''\alpha\wedge T.
\]

The calculation is valid in arbitrary bidegree whenever all displayed
bidegrees lie in range.  It requires no positivity, symmetry, or order-zero
hypothesis on \(T\).

## Sign audit

The signs were recomputed directly from Gubler--K\"unnemann's definitions.
Their Section 6.4, equation (6.4.1), gives

\[
 \langle\alpha\wedge T,\beta\rangle
 =(-1)^{AP}\langle T,\alpha\wedge\beta\rangle,
\]

while Section 6.9 gives

\[
 \langle\mathrm d'T,\gamma\rangle
 =(-1)^{P+1}\langle T,\mathrm d'\gamma\rangle,
 \qquad
 \langle\mathrm d''T,\gamma\rangle
 =(-1)^{P+1}\langle T,\mathrm d''\gamma\rangle.
\]

Expanding the differential of \(\alpha\wedge\beta\), the two terms
containing \(\mathrm d'\alpha\wedge\beta\) cancel with opposite signs.
The remaining exponent is \(A+P+1+AP\), exactly as in the frozen proof.
The \(\mathrm d''\) calculation has the same total-degree signs.  Applying
the first formula to the second gives all four terms and signs in the
displayed \(\mathrm d'\mathrm d''\) identity.  No sign defect was found.

## Source locators checked

The following locators were checked against the primary sources:

- Gubler--K\"unnemann, Section 6.4 and equation (6.4.1): the
  \(B_{\mathrm{GK}}\)-module action on delta-currents and its sign;
- Gubler--K\"unnemann, Section 6.9: the two current differentials and their
  signs;
- Gubler--K\"unnemann, Section 4.13 and Proposition 4.15(iii):
  delta-forms form a bigraded differential algebra;
- Gubler--K\"unnemann, Remark 6.7 and Proposition 6.8: equality of
  generalized delta-forms is detected by equality of the associated
  ordinary currents after every algebraic pullback and restriction to every
  open subset lying over \(W\);
- Gubler--K\"unnemann, equation (4.19.1):
  \(B^{0,0}_{\mathrm{GK}}=A^{0,0}\);
- Gubler--K\"unnemann, equation (9.3.1), Section 9.5, and Remark 9.6:
  piecewise-smooth functions lie in \(PS^{0,0}=P^{0,0}\), the algebra
  \(PSP\) is constructed, but no \(PSP\)-module action on arbitrary
  delta-currents is supplied, and current differentiation has residue
  terms;
- Chambert--Loir--Ducros, Corollary 7.3.9: on a very rich tropical space,
  forms with tropically continuous coefficients inject into ordinary
  currents.  The same primary source proves that separated, boundaryless,
  pure-dimensional Berkovich spaces are very rich and explicitly records
  that open subsets of very rich spaces remain very rich.  It therefore
  applies to the open subset \(W\subset X^{\mathrm{an}}\) in the packet.

## Repairs required during hostile audit

The initial draft was not production-ready.  The following repairs were
required and are present in the frozen bytes listed above:

1. The statement now records that \(B^{0,0}_{\mathrm{GK}}=A^{0,0}\).
   Thus a degree-zero multiplier in the module is smooth; a real-PL or
   arbitrary piecewise-smooth function is not silently treated as a
   degree-zero GK delta-form.
2. The original overly broad warning about one ordinary current was split
   by bidegree.  In degree zero, the vanishing of
   \([\mathrm d'\mathrm d''\alpha]_D\) on \(W\) does imply form-level
   vanishing, by the CLD injectivity result.  For a general delta-form,
   the packet uses the actual all-algebraic-pullback hypothesis of
   Gubler--K\"unnemann Proposition 6.8.
3. The functorial hypothesis now includes the restriction
   \(f^*(\mathrm d'\mathrm d''\alpha)|_{W'}\) and the exact quantifiers over
   algebraic morphisms \(f:X'\to X\) and opens \(W'\).
4. The functorial conclusion is explicitly made under the same hypotheses
   \(\mathrm d'T=\mathrm d''T=0\).
5. The false source locator ``Definition 4.13'' was corrected to
   ``Section 4.13.''
6. The smooth-form/current injectivity step is now sourced to CLD
   Corollary 7.3.9 rather than to Gubler--K\"unnemann Proposition 4.15(ii),
   which only proves the injection of smooth forms into delta-forms.
7. The scope paragraph now states the missing structure precisely:
   Section 9.5 constructs \(PSP\) as an algebra and associates currents to
   its elements, but it does not construct a \(PSP\times E_{\mathrm{GK}}\)
   module extending equation (6.4.1).
8. The statement explicitly records that positivity, symmetry, and order
   hypotheses play no role in the proof.

## No-go and scope firewall

The packet proves a formal module identity in the original
Gubler--K\"unnemann category.  It does **not** define the product of an
arbitrary continuous or piecewise-smooth function with an arbitrary
delta-current.  In particular, it cannot be applied to the continuous
difference \(H=U-V\) in the unrestricted CLD Bedford--Taylor problem merely
from equality of the two ordinary curvature currents.

For a general-bidegree delta-form, the audit found no source permitting one
to replace the all-pullback premise of Proposition 6.8 by equality of a
single associated ordinary current on \(W\).  This is a failure of the
proposed inference, not an asserted explicit counterexample to injectivity.
The packet correctly avoids making such a counterexample claim.

Accordingly, this verified lemma is a useful positive result and a category
diagnostic, but it does **not** solve the continuous analytic branch of
P21.3.  The P21.3 open-problem atom must not be retired on the basis of this
packet.

## Final verdict

**PASS.**  The frozen statement and proof are internally correct, reproduce
the source conventions and quantifiers, and contain the necessary scope
firewalls.  They are ready for independent production Rethlas verification.
