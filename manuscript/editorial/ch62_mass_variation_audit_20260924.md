# Chapter 62: maximizers and variation of divisorial masses

Date: 24 September 2026.
Baseline: `009a84337574d8623e493f5c0ffb6395c924ddac`.
Scope: the finite-dimensional volume section and current progress records.
The complete volume theorem and proof, all Chapter 62 text outside this
section, and Chapters 60--61 retain their previous bytes.

The additions are explicit consequences of the established variational,
domination and uniform-continuity inputs. No research-frontier question
is retired. No novelty, independent-agent review or production-verifier
verdict is claimed.

## Real weights and the full maximizing set

The section recalls the connected compact Kähler setting, n>=1, the class,
its volume and a nonempty finite set of distinct divisors on a common
smooth modification. Repeated valuations are combined. The probability
simplex now allows real nonnegative weights. The existing Legendre proof
uses only nonnegativity and sum one, so it proves the real-weight formula
directly, including attainment, without taking derivatives of rational
approximants. All divisorial evaluations are finite, and the constrained
envelopes and solutions are continuous finite-energy potentials.

Proposition 62.6.1 identifies every maximizing parameter. Its coordinate
is the normalized solution's value plus a common constant at positive
weights, and is at least that value at zero weights. The exact gap is

    g(xi) - (f(t) - xi.t)
      = delta(mu_xi, MA(phi_t)) + sum xi_i (t_i - phi_t(v_i)).

Both terms are nonnegative. Vanishing of the ordered distance identifies
the measure, and Calabi--Yau uniqueness identifies the potential modulo
constants. The weighted slack then vanishes precisely on positive weights.
Conversely, the stated coordinate inequalities make the translated solution
a candidate; domination from its positive-mass support gives equality
with the envelope. Thus zero-mass coordinates may increase independently
at a maximizer. They need not be irrelevant at arbitrary fixed thresholds.
The sum-one assumption ensures that the positive-mass support is nonempty.

## Quantitative remainder and boundary derivatives

Proposition 62.6.2 fixes the class and the divisorial support. The ordered
remainder is

    R(eta,xi) = g(eta)-g(xi) + sum (eta_i-xi_i)u_xi(v_i)
              = delta(mu_eta,mu_xi).

The order of the two measures is checked from the defining variational gap.
Convexity follows from a supremum of affine functions of the masses.
Using each solution as a variational competitor gives

    0 <= R(eta,xi) <= ||eta-xi||_1 ||u_eta-u_xi||_infinity.

Choose one common dual complex before varying the masses. Corollary 61.8.3
bounds the last norm by C0 R^q, q=2^(-n), with C0 independent of the masses.
For R=0 both conclusions follow before division. For R>0 division gives
R^(1-q)<=C0 ||eta-xi||_1. Thus, with r=1/(2^n-1), the remainder is bounded
by C ||eta-xi||_1^(1+r) and the solution difference by
C ||eta-xi||_1^r. The same C=C0^(1/(1-q)) works for both estimates.
Its dependence is on the fixed class and support (through the chosen
complex), not on positive lower bounds for individual weights.

For h with sum h_i=0 and h_i>=0 at zero coordinates, xi+s h remains a
probability vector for sufficiently small s>=0. Dividing the remainder
bound by s proves the inward derivative -sum h_i u_xi(v_i), with error
at most C s^r ||h||_1^(1+r). In the relative interior this is the tangent
differential; the normalized coefficient vector is Hölder continuous
on the closed simplex. Adding a constant to a solution does not change
the pairing because sum h_i=0. When there is only one support point the
simplex is a point and the only admissible direction is zero. The exponent
statement is restricted to n>=1. No ambient extension outside the simplex,
no moving-support uniform constant and no differentiation under the
volume integral or variational supremum is asserted.

The later beta identity differentiates the class with the measure fixed.
The text distinguishes that operation from the present mass derivative.
Its real-weight scope follows from the real-weight Legendre identity;
the previously checked class-differentiability input is unchanged.

## Curve check

The projective-line example with unit class and masses (p,1-p) has
normalized values -p at ord_0 and -(1-p) at ord_infinity. Its slopes on
the two unit branches give dual energy (p^2+(1-p)^2)/2. Hence
R((p,1-p),(q,1-q))=(p-q)^2 and the uniform solution distance is |p-q|.
These check both estimates at n=1, r=1.

At (1,0), every threshold vector (0,b), b>=1, maximizes. Along the inward
path (1-s,s), the energy is 1/2-s+s^2 and its derivative is -1.
The fixed optimizer (0,b) only supplies the affine lower bound 1/2-bs;
its slope equals the derivative only at b=1, the solution's evaluated
threshold vector after translation. An arbitrary optimizer with inactive
slack therefore cannot be substituted into the mass derivative formula.

Independent rational-arithmetic checks covered 289 pairs of weights,
25 radii on the tree branches (including the constant tails), 16 inward
secants and 64 affine lower-bound inequalities. These verify the example,
not the general theorem, whose proof is the preceding variational argument.

## Sources

The [MP--Witt Nystrom exact version 1 PDF](https://arxiv.org/pdf/2509.09442v1)
was checked at printed/physical pp. 37, 38 and 40; all three pages were
rendered and visually inspected. Page 37 starts with rational weights,
p. 38 gives the Legendre reduction, and p. 40 contains Corollaries 10.1.3
and 10.1.4. The precise locators and the real-weight extension are stated
in the book. The new maximizing-set and quantitative derivative propositions
are proved as consequences, not attributed as verbatim source statements.
The PDF has 689,695 bytes and SHA-256
`54c7f7e75bc9869f979fff2c2e0e56079660a408cc18d2df95d327dff01b7464`.

The [author's publication page](https://pietropic.github.io/publications/)
still lists MPWN25 as a preprint; the current check did not establish a
published replacement. Its existing exact-version bibliography is preserved.
The unchanged volume theorem's imported test-curve identification and
published energy identity retain the prior locators and scope documented
in `ch62_finite_volume_audit_20260923.md`. No stronger source theorem is
inferred from the new elementary consequences.

## Two passes and validation

The first complete statement/proof/source/notation pass produced a full
build of 3,997 pages and 19,025,128 bytes. Physical pages 3424--3430 were
rendered and inspected. The second pass checked the two gap orientations,
R=0 before division, constant dependence, feasible one-sided directions,
normalization, one-point support and zero masses. It recalled V locally,
defined the l1 norm, made the all-positive uniqueness condition explicit,
and identified the normalized Hölder coefficient vector. Its first build
exposed a page break between the inward-derivative introduction and display;
they were kept together and the full build and checks were repeated.

Final full build: **3,997 pages, 19,025,432 bytes**. Physical pages
3424--3430 were rendered and inspected again, covering the complete edited
section, the preceding criterion and the following section opening.
This is scoped visual review, not a new whole-book audit. Both rounds
were built in a temporary export of the baseline; the delivered sources
and ignored current PDF are the checked bytes.

- Reference/structure check: 390 TeX inputs and 11,683 unique labels;
  no missing input, duplicate label, dangling reference or structural defect.
- Final log: no unresolved reference/citation, multiply defined label,
  rerun request, horizontal overflow or vertical overflow. Existing
  underfull and class warnings remain.
- Scoped house audit: zero errors and one reviewed MPWN25 preprint warning;
  normal audit exits 0 and strict audit exits 1 for that warning.
- Open-problem inventory: PASS, 45 active atoms in 14 environments,
  tiers (0,5,8,15,17).
- Chapter 62 outside this section and the complete volume theorem/proof
  are byte-identical to the baseline. All other chapter sources are unchanged.
- Only the five reviewed source/progress files are staged; the current
  PDF remains ignored. Frozen packets, verifier receipts and dated releases
  are not regenerated or republished.

Final Chapter 62 SHA-256: `a79b160e27827a81cdba4fb6c70c4ea2d9a5f665f7888f459d45b4340ddafb9d`.
Final PDF SHA-256: `5a61538b6b387649a2d16361cd3cf888fb1854bcd5511a81bc5bdd3f38e11034`.
Preserved Chapter 61 SHA-256:
`1bc2e7024230c6c32c22a855af30a152e4f4c1567ab0984eb4c8b05c2c3264fd`.
Preserved Chapter 60 SHA-256:
`0fdb5f601274ccf7df48afd5112a1bf3e452e3aff9df5a459c5c6a08e611ac93`.
Preserved P12.1 fragment SHA-256:
`8d9f9bd9edb057b95773479279bbdabb3240319e4cb56f6f15cb2bd923fb4380`.
The author's supplied normalized-links PDF and its archived copy retain
`71f5e0d50bdcbf493cb96a869e2db03a78bd591b3eba2f797da5a23f6253daaa`;
the supplied CURVE_PSH.tex retains
`9142aac73c5af7e4e715b3313def5ed56fae4e63e1ac8a53d0419df7d2194be9`.
P12.1 integration/provenance and P12.2--P12.6 residuals are unchanged.
