# Regularization and capacity dependencies for the alternative gradient route

This is a source-only review following the Chu--Liu and Dat checkpoint.
The exact Cheng--Xu regularization preprint and the published
Dinew--Kołodziej estimates paper have now been read in full, including
proofs and references, and every acquired physical page has been
individually displayed in the recorded sheets. The review separates
geometric jets, admissibility, stability, capacity and density exponents.
It does not admit a new original result or certify all cited external
proofs. The checked 4,398-page book remains byte-identical.

## Editions and actual reading

| Primary source | Acquired edition | Actual physical pages | Reading |
| --- | --- | --- | --- |
| Jingrui Cheng and Yulun Xu, *Regularization of m-subharmonic functions and Hölder continuity* | [2208.14539v1](https://arxiv.org/abs/2208.14539v1), submitted 30 August 2022, 21:05:51 UTC | 25 | All 25 pages, thirteen displayed sheets |
| Sławomir Dinew and Sławomir Kołodziej, *A priori estimates for complex Hessian equations* | [Analysis & PDE 7(1), 2014, 227--244](https://msp.org/apde/2014/7-1/apde-v7-n1-p08-s.pdf), DOI 10.2140/apde.2014.7.227 | 21 | All 21 pages, eleven displayed sheets; eighteen research pages and three publisher pages |

Cheng--Xu PDF SHA-256:
`a52d1b13de3354d768a4ca3de8f946a137f31ca11441058445765108eb4fe558`.
Its complete text SHA-256:
`425c649af38f209169bb55e0d2c90c9f65077cfbec62baf996616d8787265651`.
The published Dinew--Kołodziej PDF SHA-256:
`7ecba42885c7549f82372f3e2e7d6ee22eb7f160ad1d6a3734e43232f645dc1c`.
Its complete text SHA-256:
`e3fa5885c9b6f3ace3cae52e4917f65ed5a121d26d9bd6de1b6e7e5a7bf3022f`.

The physical-page distinction matters. Dinew--Kołodziej page 1 is the
publisher cover; pages 2--19 are the research article, printed 227--244;
pages 20--21 are publisher information and the issue contents. Thus this
checkpoint has 46 freshly read physical pages in 24 sheets, comprising
43 research pages and three publisher pages. There is no reused physical
page in that count. A truncated first attempt at sheet 02 is excluded;
the subsequent complete text and image inspection supplies that reading.

Cheng--Xu's later journal metadata, Math. Res. Lett. 31(4) (2024),
951--984, DOI 10.4310/MRL.241118233017, is not a journal-proof reading.
The exact 2208.14539 regularization paper is different from the previously
selected 2406.00953v2 viscosity paper and from the 2501.17016 metadata lead.
Dinew--Kołodziej's estimates preprint 1112.3063v1, submitted 13 December
2011, 22:38:21 UTC, is also different from the previously fully read
Liouville/Calabi--Yau paper 1203.3995v2. The present review reads the
published estimates PDF, rather than treating the eighteen-page arXiv
metadata as a pin for that twenty-one-page file.

## Cheng--Xu: what the geometric calculation supplies

The background is compact Kähler. In the source convention the operator
acts on the eigenvalues of omega plus i partial-bar-partial phi. The
quadratic sup-convolution adds epsilon and subtracts the squared tangent
length divided by epsilon. It is an upper approximation, with an
epsilon-sized gain from the zero tangent vector. Lemma 2.10 bounds a
maximizing vector by the square root of epsilon times a bound for phi's
oscillation. Its improved estimate uses an already known Hölder norm.
This is not a construction of a smooth admissible approximation.

Lemma 2.11 proves local semiconvexity using the inverse exponential map.
The semiconvexity constant depends on epsilon. Almost-everywhere second
derivatives follow, but no uniform C2 estimate follows. The normal
coordinate construction chooses the positive metric square-root jet N,
close to the identity, and the holomorphic affine map with that jet.
The inverse exponential map defines a nearby vector field. Lemma 2.17
bounds its first and second derivatives at the base point by a fixed
geometric constant times the squared maximizing tangent length.
These jet and semiconvexity calculations do not impose nonnegative
holomorphic bisectional curvature.

Proposition 2.15 transfers an upper test to the original potential.
The transferred Hessian contains the **plus** Hessian of the squared
length penalty. Lemma 2.21 identifies its leading term as the negative
curvature contraction, with cubic remainder in the maximizing vector.
Corollary 2.22 uses nonnegative holomorphic bisectional curvature to
discard that negative semidefinite leading term. This is the actual
curvature-dependent step; Remark 2.23 explicitly locates the hypothesis
there. For bounded continuous admissible phi it gives an admissibility
loss of order epsilon to the one-half power. The improved loss is
epsilon to the power (1+alpha)/(2-alpha), with a controlled C-alpha norm.

Lemma 2.28 gives an L1 error of order epsilon to the one-quarter power.
It uses the trace cone, local Kähler potentials and a mean-value estimate.
The improved L1 exponent is 1/[2(2-alpha)] when a C-alpha norm is known.
Its constants retain the potential bound or Hölder norm and the geometry.
Neither this calculation nor the tangent-field derivative calculation
allows one to erase the curvature hypothesis from Corollary 2.22.

The source theorem begins with continuous viscosity-admissible
potentials. A distributional trace inequality together with arbitrary
upper semicontinuity does not select the canonical subharmonic
representative: changing one value upwards can preserve the distribution
and destroy a mean-value assertion. The continuous/viscosity class used
here avoids that representative ambiguity. This review does not extend
Proposition 2.24 to noncanonical representatives.

### Exact references needed by Chu--Liu

The quadratic preprint contains **equation** (2.9), the isometric-jet
condition, and **equation** (2.16), the squared-length Hessian expansion.
They are not separately numbered Lemma 2.9 and Proposition 2.16 in this
acquired edition. Lemma 2.11 and Lemma 2.17 provide the semiconvexity and
vector-field derivative estimates. Corollary 3.6 is the volume-to-supremum
bound; equation (3.7) is the volume estimate; Lemma 3.8 states the combined
stability estimate. Future book references must identify these exact
locations rather than copying mismatched labels.

For Chu--Liu's logarithmic penalty one must differentiate that penalty
itself and retain its two parameters. Replacing it with Cheng--Xu's
quadratic formula would change the error and its constants. The geometric
jet estimates provide a useful input even without nonnegative curvature;
the resulting logarithmic admissibility loss and the subsequent modulus
still require their own quantitative argument. The previously audited
Hou--Ma--Wu normalization and boundary stability problems remain open
application gates.

## Cheng--Xu: stability and density conversion

Section 3 uses an auxiliary complex Monge--Ampère problem, an exponential
integrability estimate, Hölder inequalities and a genuinely superlinear
De Giorgi recurrence. Its smallness condition is a weighted positive-part
integral A(delta,s0) bounded by delta to the power n+1. The comparison
potential v has a small admissibility loss; Lemma 3.8 also requires v to
be nonpositive and s0 at least 2 delta times its supremum norm. For every
positive mu less than 1/(n q0), the bound has the form

    sup(v-phi) <= s0 + C s0^(-mu) ||(v-phi)^+||_L1^mu,
    q0 = p0/(p0-1),  exp(nF) in L^p0,  p0>1.

The constant retains the fixed structural and geometric data, the
exp(nF) norm and the chosen strict exponent. Corollary 3.6 removes delta
from that constant only after the weighted integral is small enough.
The De Giorgi recursion is r a(s+r) <= B a(s)^(1+mu). Choosing increments
2 B a(s)^mu gives geometric decay and a finite total increment.
This is different from the false multi-term extinction lemma in the Dat
paper. Strict superlevel volumes need not be continuous at a plateau;
the limiting argument can use their right continuity and monotonicity.

The theorem for the root operator f=sigma_m^(1/m) is expressed in terms
of exp(nF), not directly the density of the m-Hessian wedge. If that
normalized wedge density is g in L^p, then the appropriate exponent is
p0=m p/n, up to the fixed binomial normalization of sigma_m. Thus p0>1
is exactly p>n/m. With nonnegative holomorphic bisectional curvature,
Corollary 1.6 states Hölder regularity for every exponent strictly below

    (m p-n) / [2(m p-n+m p n)].

The iteration in Theorem 3.15 has the claimed fixed point. If A=1+n q0,
its map is x -> 2/[2(2-x)A+1], with limiting fixed point 1/(2A).
At n=3, m=2, p=2 this gives p0=4/3, q0=4 and endpoint 1/26.
All used exponents are strictly below that endpoint. There is no endpoint
regularity claim and no general-curvature Hölder theorem in this review.

The general operator assumptions printed on page 2 impose the determinant
bound and Euler-type growth bound on the positive cone. Page 18 uses
linearization at the possibly nonpositive admissible solution eigenvalues.
An application to a general cone must explain the needed extension or
supply whole-cone bounds. For the elementary symmetric root operator,
homogeneity and the usual Gårding/linearization inequalities are the
appropriate specific inputs. No counterexample to the general operator
theorem is asserted here, and a full extension argument is not certified.
The auxiliary mass normalization, exponential integrability and
Monge--Ampère existence are still cited analytic inputs.

## Dinew--Kołodziej: legitimate capacity and exponent directions

The local capacity is the supremum of the Hessian mass over all continuous
m-subharmonic tests taking values in [0,1]. Testing with one function
gives a **lower** bound for this supremum. In Proposition 2.1 the auxiliary
Monge--Ampère potential v is nonpositive and uniformly bounded.
The printed negative witness cv should be shifted to 1+cv to meet the
[0,1] normalization. This leaves its Hessian unchanged.

For a compact set K with volume V(K), the proof uses a density
V(K)^(2 epsilon-1) times its indicator. Its L^(1+epsilon) integral is
V(K)^(epsilon+2 epsilon^2), hence uniformly controlled on the fixed
bounded background. The auxiliary Monge--Ampère bound controls cv.
The mixed-measure inequality then gives

    cap_m(K,Omega) >= c^m V(K)^(1-m/n+2m epsilon/n).

Consequently V(K) <= C cap_m(K,Omega)^r for every r<n/(n-m),
in particular for 1<r<n/(n-m). The proof retains the background,
epsilon and the cited Monge--Ampère and mixed-measure inputs. It does
not bound every bounded-potential Hessian measure by volume.

Proposition 2.2 gives cap_m({u<-s},Omega)<=s^(-m) when the total
Hessian mass is at most one and u has zero boundary values. A test close
to the capacity supremum is compared with a scaled u; the inclusion of
the test set in the comparison set has the correct direction. Combining
the two bounds gives a power tail and integrability of u for every
q<mn/(n-m). Boundedness near the boundary or relatively compact singular
level sets is essential to this stated result. Remark 2.3 explicitly
distinguishes it from the general local integrability conjecture.

The model -|z|^(2-2n/m) has the limiting potential exponent mn/(n-m).
This is a statement about integrability of the potential, not the density
exponent. Remark 2.11 uses log|z| to show unboundedness with m-Hessian
density in L^p for p<n/m when m<n. That example has no critical L^(n/m)
integrability and does not settle the density endpoint p=n/m.

Hölder's inequality combines a density in L^q with the volume-capacity
bound to give a measure bounded by cap_m^(r/qprime). A genuinely
superlinear power requires r/qprime>1, for some r<n/(n-m). This is
possible exactly when q>n/m. The compact argument uses equivalent
local and global capacities, normalized mass and **convex combinations**
of omega-m-subharmonic functions. Arbitrary positive scaling does not
preserve that global background class. These are the directions missing
from the capacity argument in the preceding Dat audit.

The article supplies the classical normalized compact L-infinity,
continuous existence and stability results in the stated q>n/m range.
Its compact Section 3 assumes nonnegative density and equal total
mass before stating Theorem 3.3. These standing hypotheses must accompany
any import, although they are not repeated in every displayed theorem.
The separate real-Hessian threshold n/(2m) is not a complex threshold.

### Quantitative exponent still to check

Lemma 2.4, printed 234--235, invokes Kołodziej 2002, Lemma 4.3, to pass
from t^m a(s)<=A a(s+t)^p to a terminal bound with the printed exponent
p/n. The elementary geometric-step calculation of this recurrence
naturally produces exponent (p-1)/m. This checkpoint has not acquired
or read the cited lemma and does not certify the printed p/n exponent,
nor the exact resulting powers in Theorems 2.5 and 3.1. This is an
identified dependency gate, not a constructed counterexample to the
capacity lemma. The q>n/m condition follows already from the separately
checked volume-capacity and Hölder calculation.

The local regularity proof in Section 4 starts with an existing W^(2,p)
solution and p>n(m-1), strictly positive C^(1,1) data, and a prescribed
L^p bound on its Laplacian. It regularizes by averages, estimates the
linearized operator and solves an auxiliary Hessian problem. The argument
uses the weak mixed-Hessian inequality and the previously established
existence/stability results. It does not produce a second-order bound
from a density L^q bound alone, or a gradient estimate for unknown-dependent
weak auxiliary densities. Its real-case optimality comment is a separate
historical question, not a newly added canonical problem.

## Nine literal checks and their scope

1. **Cheng--Xu Lemma 2.7 sign.** In flat complex dimension one take
   constant phi=0, phi_epsilon=epsilon, P=epsilon and the permitted
   holomorphic map z -> 2z before condition (2.9). Then xi(z)=z and
   Q(w)=|w|^2/(4 epsilon). The actual eigenvalue is 1+1/(4 epsilon);
   the printed determinant gives 1-1/(4 epsilon). At epsilon=1/8 the
   values are 3 and -1. Proposition 2.15 uses the correct plus sign.
   This checks the displayed determinant, not the regularization theorem.
2. **Cheng--Xu Lemma 2.27 order.** For negative harmonic u, the inequality
   H<=Hprime gives u H>=u Hprime. The printed proof uses the opposite
   order and an upper derivative bound where its conclusion needs a
   lower bound. No counterexample to almost-monotonicity is claimed.
3. **Absorption before Cheng--Xu (3.7).** The needed condition is
   delta||v||/s0<=1/2. On a volume-one flat complex one-torus, take
   v=-1, phi=-181/200, F=0, delta=1/10 and s0=1/1000. The strict
   superlevel set is the whole torus, while (v-phi)^+ vanishes.
   The weighted positive-part integral is 1/250, at most delta^2,
   and the isolated printed condition delta||v||<=1/2 holds.
   The resulting zero upper bound for volume is false. Lemma 3.8
   correctly imposes s0>=2delta||v|| and excludes this substitution.
4. **De Giorgi objection cleared.** Cheng--Xu's actual one-term
   superlinear recurrence gives a summable geometric-step proof.
   It is not the previously refuted Dat recurrence.
5. **Hölder fixed-point objection cleared.** The density conversion and
   fixed point agree with Corollary 1.6; 1/26 at n=3,m=2,p=2 is a strict
   upper endpoint. No endpoint or curvature-removal assertion follows.
6. **Dinew--Kołodziej class inclusions.** Proposition 1.3(1), printed
   231, reverses the standard inclusions. The function
   |z1|^2-|z2|^2/2 on C^2 has positive trace and negative determinant;
   it is subharmonic and fails to be plurisubharmonic. The correct order
   is SH_n contained in ... contained in SH_1.
7. **Capacity witness objection cleared.** Add one to cv in Proposition
   2.1. Its Hessian is unchanged and the test belongs to [0,1].
   The proof takes a legitimate lower bound for a supremum.
8. **Unrestricted compact stability needs normalization.** As printed,
   Theorem 3.1 permits u=0, f=1 and v=T>0 on a fixed volume-one flat
   complex three-torus. With m=2,q=2,qprime=2,pprime=5/2,p=5/4,
   its exponent is 5/27. It would require T<=C T^(5/27) for all T,
   with every listed datum fixed. The ratio grows as T^(22/27).
   Restricting or normalizing the comparison class, or modifying the
   estimate, is necessary. This literal statement is false; normalized
   stability, the L-infinity theorem and mass-normalized existence are
   not refuted by it.
9. **Sharpness scope objection cleared.** The potential power and the
   logarithmic density example test different integrability quantities.
   Neither provides an L^(n/m) endpoint density counterexample.

These are elementary substitutions and source-proof checks, recorded in
the accompanying diagnostic JSON. Four checks clear apparent objections;
five identify literal sign, condition, class or normalization problems.
They are not new original theorem admissions or production verification
receipts. Other local slips, including the sign in (2.25) and the
reference to Theorem 2.29 where Theorem 2.1 is intended, are not promoted
to additional mathematical counterexamples.

## Integration decision and preservation

The geometric jet input, the curvature-dependent admissibility step,
the root/density exponent conversion and the correctly directed capacity
argument can inform a scoped explanation. Exact quantitative stability
powers and unrestricted comparison claims remain excluded until their
hypotheses and cited lemma are checked. Chu--Liu's compact logarithmic
route remains a conditional research lead; its Appendix A normalization
and its separately refuted printed boundary formula are not repaired by
reading these dependencies. Dat's general all-m p>1 claim remains excluded.

Preserve 425 active inputs, 108 protected inputs, 69 preceding frozen
manifests (56 integration and thirteen source-review manifests), 124
preceding exports, fourteen generated book files, the checked 4,398-page
PDF, the native catalogue and all 42 canonical status rows. Of the 5,065
baseline tracked files, only README and the ongoing programme are edited;
the other 5,063 are byte-preserved. The two new audit files are separate
from those baseline files. No new active TeX, native editor operation,
unchanged-book build, fresh book PDF review, isolated archive compilation,
model call or verification receipt is claimed.

Fetch both main and work, integrate any actual incoming author progress,
and publish this checkpoint on work with the existing draft PR. Continue
with the cited capacity iteration lemma and with the precise conditional
compact logarithmic estimate before extending the book. The October
polynomial Hessian preprint 2610.06529 is still a metadata lead here.
