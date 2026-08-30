# Hostile self-audit

## Verdict

**PASS as a candidate boundary theorem, with no retirement claim.**

The deduction is short, but it is not tautological: the active P21.3
ambiguity exists precisely because a continuous zero-current difference need
not be smooth.  The verified P06.2 theorem removes that obstruction on the
specified strict-open-polycylinder basis.  Once smoothness and vanishing of
the smooth Hessian are available, the CLD current Leibniz rule closes the
argument for every positive closed current and every allowed bidegree.

## Obligations checked

1. **The pair difference is legal.**  From
   'd'd''[u]=d'd''[v]', linearity gives 'd'd''[u-v]=0'; no psh closure under
   subtraction is used.
2. **Continuous multiplication is legal.**  A positive CLD current is of
   order zero, so multiplication by 'u', 'v', and 'h=u-v' is defined and
   linear.  The proof never multiplies a continuous function by an arbitrary
   distribution.
3. **The smooth form really vanishes.**  The abstract proposition assumes
   both ordinary smoothness and zero *smooth* Hessian.  It does not silently
   infer injectivity of smooth forms into currents.
4. **The concrete hypothesis supplies the stronger conclusion.**  The exact
   P06.2 v3 theorem writes 'h=c+sum lambda_j log|S_j|'.  Annulus coordinates
   are analytic units, their logarithmic tropicalizations are ordinary
   CLD-smooth, and an affine function of them has zero smooth Hessian.
5. **The current Leibniz rule is in the correct scope.**  CLD Lemma 8.5.3,
   specialized to a smooth function, gives
   'd'd''(hT)=d'd''h wedge T' for a positive closed current.  Closedness kills
   the cross terms and positivity supplies symmetry.
6. **Local-to-global passage is legitimate.**  A topological basis means
   that for every 'x in W' there is a basis member 'Q' with
   'x in Q subset W'.  Restrictions preserve the current equation, and
   currents form a sheaf.
7. **No hidden psh approximation is used.**  The proof applies to all
   continuous equal-curvature pairs.  It neither smooths the original psh
   functions nor invokes collapse of the CLD psh hierarchy.
8. **No current classification is used.**  The current may be nonskeletal
   and its support arbitrary.  Only positivity and closedness enter.
9. **Bidegrees are bounded.**  The statement imposes
   '0 <= ell <= n-1', exactly the range in which the second differential
   produces a current of valid bidegree.
10. **Analytic isomorphisms cause no normalization change.**  CLD smooth
    functions, currents, positivity, closedness, and the current differential
    are intrinsic and transport through an analytic isomorphism.
11. **Field and endpoint firewalls are exact.**  The field is complete and
    nontrivially valued; all discs and annuli are strict and open, with radii
    in the value group.  Closed, half-closed, and non-strict endpoints are
    absent.
12. **The full Bedford--Taylor predicate is not overclaimed.**  The global
    predicate follows only when the standard polycylinders form a basis.
    For a single standard polycylinder 'P', the final sentence asserts the
    identity only for a pair defined on all of 'P'; it does not assert that
    every ordinary open subset of 'P' is standard.
13. **No illicit enlargement to quasi-smooth or toroidal charts occurs.**
    Etale, log-etale, and moment maps are not replaced by analytic
    isomorphisms.  The result supplies no polycylinder uniformization theorem.
14. **Atom accounting is unchanged.**  P21.3 remains open on arbitrary
    higher-dimensional analytic spaces; P06.2 remains open on arbitrary
    germs.  The candidate only establishes a precise implication and a
    verified-source boundary range.

## Adversarial examples considered

- A deleted-branch neighbourhood of a type-II point in an open disc need
  not itself be a standard disc or annulus.  This is why the last sentence
  is not promoted to the full predicate on every open subset of one
  polycylinder.
- A continuous function with zero current on an arbitrary CLD tropical
  space need not be known smooth.  The proof would be circular without the
  P06.2 input; the abstract proposition states the missing regularity as an
  explicit hypothesis.
- A closed annulus satisfying the current equation only on its analytic
  interior is not admitted.  The rejected P06.2 v2 endpoint language is not
  reintroduced.

## Release status

This is a hostile **self**-audit, not an independent audit and not a
production Rethlas receipt.  Promotion requires an independent exact-byte
audit, dependency-closed production verification with
'gpt-5.6-sol'/'xhigh', and live-book integration.

