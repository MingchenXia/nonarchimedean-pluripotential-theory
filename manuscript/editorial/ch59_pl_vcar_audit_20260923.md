# Chapter 59 PL functions and vertical Cartier divisors

Date: 23 September 2026.
Baseline: `f7c18e6437939a6308cfc4dd80d0517b42d63729`.
Scope: the PL/vertical-Cartier correspondence in Section 59.4 and its
immediate divisorial-density consequence. The standing base X is a
connected compact Kahler manifold. The previously checked integral-closure,
monomial and invariant-divisor units are preserved.

## Findings and reconstruction

The former forward construction dropped the factor 1/m in a PL+ function.
Its displayed calculation also applied r(v_E), a character on ideals of X,
directly to a flag ideal on X x P1. The untruncated function log|a| was
called a PL+ generator even though it can be minus infinity. The inverse
construction asserted relative generation without constructing a vertical
relatively ample divisor. Its independence argument did not supply a
complete injectivity proof before the subsequent use of divisorial density.

The revised preparation defines fractional flags as coherent submodules of
meromorphic functions bounded between O(-aT0) and O(aT0). Invariant weight
projections on the finite thickening modulo t^M give coherent increasing
coefficient ideals. The finite Laurent expression is made near T0 and
glued to the unit ideal off T0. Powers of t globally mean divisor ideals
of T0; they do not introduce an unintended contribution at infinity.

The new lemma evaluates flags by the minimum of v(a_j)+lambda_j. Passing
to canonical increasing coefficient ideals proves presentation independence.
Their unit sum makes the minimum finite even at proper-support characters.
Coefficient sums and products give the two character identities. A common
zero gives a point character with all relevant ideal values infinite, which
proves the converse finiteness criterion. Rational combinations therefore
have the form (phi_b-phi_c)/m; empty products use the unit flag.

Integral closure stays within flags. The finite reduction identity from the
earlier integral-closure proof applies globally on the compact space T.
All Gauss values in this identity are finite, so cancellation is legitimate.
An invertible central-fiber twist handles fractional flags. The proof only
uses evaluation on flags, not an unproved extension to arbitrary local
holomorphic germs or to all ideals on T.

For phi=phi_b/m, the equality b O_model=O(B_b) gives the divisor B_b/m.
The order of a sum of ideal terms is their minimum, so evaluation is through
sigma(r(v_E)), and its order is divided by b_E. This proves d_E=b_E phi(r(v_E))
with both signs and denominators. On a common model the coefficient formula
respects every rational relation among the actual functions, giving a
well-defined linear map. For its kernel, equal invertible fractional ideals
have equal integral closures after a common twist. Flag closure invariance
then gives equality at every character. No divisorial-density theorem is
used to establish injectivity.

For surjectivity, cofinal equivariant blowup models supply a vertical
relatively ample Cartier divisor G. It is constructed from the tautological
divisors of center ideals and the composition rule for relative ampleness.
The identity model permits G=0. Relative Serre generation is applied on
projective analytic germs through the earlier coherent algebraization
interface. Finitely many local sections extend over a neighborhood, and
properness removes their cokernel support after shrinking. A finite cover
and a common multiple first make O(G) relatively generated. A maximum of
the finitely many further exponents then makes both O(NG) and O(D+NG)
relatively generated. This avoids choosing infinitely many unrelated
neighborhoods as the exponent changes.

Their pushforwards are coherent invariant fractional ideals. Bounds by
plus or minus a multiple of the total central fiber, normality of T, and
the projection formula prove the flag bounds explicitly. Their evaluation
maps recover the two invertible fractional ideals on the model. Taking the
difference of their functions recovers D; rational D is obtained by scaling.
The construction does not impose a sign or positivity hypothesis on D.

The P1 example blows up (p,0). The function one half of
max(log|I_p|,-1) corresponds to -E/2. Its values at the strict central
transform, exceptional divisor and point character supported at p are
0, -1/2 and -1/2. Adding 3/2 corresponds to (3 total_fiber-E)/2,
with coefficients 3/2 on the strict transform and 1 on E.

The following density argument was rechecked using this now noncircular
correspondence. Its compact finite-minimum separation argument is retained;
the constants are specified as rational, and the locator now points to the
checked author version, Theorem 2.3.6, pp. 18 and 28.

## Sources and limits

- Mesquita-Piccione, [arXiv:2409.06221v2](https://arxiv.org/abs/2409.06221v2),
  18 September 2025: equation (0.0.6), equation (2.4.2), Proposition 2.4.3,
  Remark 2.5.2, Lemma 2.6.3, Theorem 2.6.4 and footnote 10, and
  Theorem 2.3.6 with its concluding proof. PDF pages 6, 18, 19, 20,
  26, 27 and 28 were read and visually inspected in this revision unit.
  The explicit construction of a vertical relatively ample divisor uses
  the cofinal blowup statement; an arbitrary projective embedding alone
  does not show its O(1) has a vertical divisor representative.
  PDF SHA-256:
  `9eb2ea7686a5962ebc11c5eacd23b0cb3dcb081e27ac48292933f291fc82cb23`.
  MPTropicalV2 supplies the exact locators. The publisher-PDF access limit
  from the preceding audits is retained; these locators are not claimed
  to have been checked in the published MP24 version.
- Stacks Project, [Tag 0C4K](https://stacks.math.columbia.edu/tag/0C4K),
  composition of relatively ample invertible sheaves, and its proof input
  [Tag 0892](https://stacks.math.columbia.edu/tag/0892), including the finite
  section argument and eventual generation. The scheme statements are
  transported through the existing projective-germ algebraization theorem;
  they are not cited as direct statements about arbitrary complex spaces.
- Stacks Project, [Tag 01Q3](https://stacks.math.columbia.edu/tag/01Q3),
  assertion (7), eventual generation of twists of a finite-type coherent
  sheaf on a quasi-compact scheme with an ample invertible sheaf. The local
  algebraizations here are projective over a noetherian analytic local
  ring. Compactness and the finite-section argument supply global exponents.
- The analytic normalized-blowup integral-closure formula and coherent
  algebraization remain the previously audited interfaces
  `eq:mp-normalized-blowup` and `thm:mp-bingener-projective-germs`.
  No global algebraic function field for X is assumed.

All bibliography entries are unchanged. The one arXiv-only warning in the
bibliography-aware changed-block audit concerns MPTropicalV2 and was
reviewed against the exact-version limitation above.

## Second pass and validation

After the first successful whole-book build and rendered-page inspection,
the second local mathematical pass rechecked canonical coefficients,
finite cancellation, the zero-function and unit-flag cases, independence
before density, the sign of tautological divisors, the identity model,
uniform generation, divisor bounds and the shifted example. It clarified
the definition of a fractional ideal, included empty products and G=0,
and supplied the density-interface citation. The theorem statement and its
coefficient formula were kept together with a local unbreakable block
after the class still split a samepage environment. The full build and
visual review were repeated after the layout adjustment.

The final complete build has 3,955 pages and 18,811,808 bytes.
The input check passes for 389 TeX files and 11,583 unique labels, with no
missing inputs, duplicate labels or dangling references. The final log has
no unresolved references or citations and no horizontal or vertical
overflow. Existing underfull-box and class warnings remain. Final physical
pages 3322--3327 (printed 3254--3259), including the adjoining text, were
rendered and inspected. `git diff --check` passes.

The strict audit of the entire changed block has zero errors and warnings.
A separate whole-chapter house-style audit does not pass: the untouched
legacy text has 195 inline-delimiter reports, two examples lacking immediate
semantic labels and the existing MP24 compound-name label report. The
baseline had the same categories and 256 inline-delimiter reports (259 total
errors versus 198 now). Its 13 warnings, including legacy result headings,
label prefixes and three preprint entries, are unchanged. This unit does
not claim a clean whole-chapter house-style audit or silently relabel
unrelated bibliography entries.

Chapter 59 before the new flag preparation and from the dual-simplex
definition onward is byte-identical to the baseline. Chapter 58, the
bibliography, author-supplied CURVE_PSH.tex, research packets, verifier
receipts and dated releases are unchanged. The inventory remains 46 active
atoms in 14 formal environments, tiers (0,5,8,16,17). The generated live
PDF is ignored and is not a new release. Compilation is not a mathematical
verifier. No independent-agent audit, production-verifier pass, new
research theorem or research-atom closure is claimed.

Final SHA-256:

- Chapter 59: `882dbd6ea32597cafb1404145a2cb11729f67b66bafd0dab06b63bd0378fe415`.
- Unchanged bibliography: `f77736549ed82a38bc6db488b2527629b2cb2ebf5b47475f3c94e08e0e068219`.
- Generated live PDF: `2d13b68275c6854a9893b623ff7076e650fe811c3867826defbf7d8f92c84811`.
- Supplied and restored CURVE_PSH.tex: `9142aac73c5af7e4e715b3313def5ed56fae4e63e1ac8a53d0419df7d2194be9`.

Next: reconstruct the dual-complex retraction and inverse-limit proof.
In particular, retain stratum labels when an intersection has more than
one component: continuity of the global component weights alone does not
prove continuity into that complex. Check ideal evaluation on the model,
proper-support characters, transition compatibility and the separation
used for inverse-limit surjectivity before counting that unit as checked.
