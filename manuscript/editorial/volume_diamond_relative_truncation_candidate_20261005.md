# Relative truncation and the volume-diamond equality: research candidate

Date: 5 October 2026. Baseline work commit:
`4a44995c1c7bc70b21c09903a9d5ff2f54e2793a`.

**Admission status: research candidate, pending independent verification.**
No production verifier has reviewed the exact statement and proof below.
There is no `VERIFIED` receipt, no claim of priority, and no promotion to
an active book theorem or solution of one of its 42 problem atoms.
The existing native LaTeX catalogue and the 4,290-page book are unchanged.

## 1. The primary-source question

Darvas–McCleerey, *Lines in the space of Kähler metrics*, Mathematische
Annalen 396, article 36 (2026), DOI 10.1007/s00208-026-03573-8,
asks on actual published page 16, after equation (20), whether
for a sublinear bounded or finite-p-energy subgeodesic line U,

\[
 m(\widehat U^+_\tau)+m(\widehat U^-_{-\tau})
   =m(\widehat U_\tau)+V
\]

holds for almost every slope. Here \(m(h)=\int_X\operatorname{MA}_\omega(h)\)
is nonpluripolar mass, \(V=\int_X\omega^n\), and the all-minus-infinity
potential has mass zero by convention. The published 25-page text was
read in full and 20 actual pages were inspected in the preceding frozen
integration. The source's Proposition 3.3 and Lemma 3.4 on pages 12–13
identify the all-time dual with a test line and the two half-time duals
with its tails. Selected lines 663–742 and 904–980 were reread here.

The proposed route is an equality for a pair of potentials whose
pointwise minimum is itself psh and whose maximum has full mass.
This is stronger structure than an arbitrary rooftop pair.

## 2. Exact candidate signature

Let X be a compact connected complex Kähler manifold of dimension
\(n\geq1\). Let \(\theta\) be a smooth closed real (1,1)-form with big
class, and put \(V=\operatorname{vol}(\theta)>0\).
Let \(A,B\in\operatorname{PSH}(X,\theta)\). Assume

\[
 C=\min(A,B)\in\operatorname{PSH}(X,\theta),\qquad
 b=\max(A,B)\in\mathcal E(X,\theta).
\]

The minimum and maximum are **pointwise**, without an extra envelope
or usc regularization. The second hypothesis is full mass, not merely
zero Lelong numbers. No boundedness, p-energy, smoothness, analytic
singularity or small unbounded locus is required of A, B, C or b.
The proposed conclusion is

\[
             m(A)+m(B)=m(C)+V. \tag{R1}
\]

Global minus-infinity cases can be included separately by the mass-zero
convention. The connected hypothesis only avoids component notation;
the argument would apply component by component when the convention
permits a potential identically minus infinity on one component.
For a merely pseudoeffective zero-volume class, the known upper bound
for nonpluripolar mass makes the displayed equality only zero=zero;
the candidate keeps the nontrivial big-class range. No analogous
non-Archimedean psh assertion is part of its signature.

## 3. Primary inputs and locator boundary

The reused primary dependency is BEGZ, *Monge–Ampère equations in big
cohomology classes*, explicitly **arXiv:0812.3674v2**, 9 September 2010,
54 pages. Its PDF SHA-256 is
`43097be8459edfd948929fade34367fa7bbd0fe691d9cba1a4f27a11181214cd`.
It was reused byte for byte from the existing 1 October cache, not
freshly downloaded or identified with the published Acta file.
Selected extracted ranges 175–305, 922–955 and 1290–1385 were read.
Actual pages 1, 5–7, 20 and 28 were inspected. This is selected reading,
not a full new reading of the 54-page dependency.

Load-bearing inputs in that identified version are:

- Definition 1.1 and the surrounding construction: the product is a
  nonpluripolar measure and charges no pluripolar set.
- Proposition 1.4, first item: nonpluripolar products are local in the
  plurifine topology, without a small-unbounded-locus restriction.
- Proposition 1.6: global products of closed positive currents on a
  compact Kähler manifold are well-defined.
- Definition 2.13, the displayed union of weighted energy classes, and
  Proposition 2.14, first item: a less singular positive current in the
  same class as a full-mass current has full mass. This supplies full
  mass for every relative cutoff below. The extremality part of that
  proposition is not a needed proof input.

The classical degree-one formula after Definition 1.1 and the
multilinearity item of Proposition 1.4 supply a separate curve check.
Equation (1.7) is a convention check; it is not used to assert a new
monotone convergence theorem for all singular endpoints.

## 4. Proposed proof of (R1)

Write \(N=\{b=-\infty\}\). It is pluripolar. Since A and B are
bounded above by b, all four potentials are minus infinity on N.
The proof will use only nonpluripolar measures; every measure below
gives N mass zero. Thus no difference of two minus-infinity values
is ever taken on N.

For an integer \(k\geq1\) and \(h\in\{A,B,C\}\), set

\[
                   h_k=\max(h,b-k).
\]

Each cutoff is theta-psh and satisfies \(b-k\leq h_k\leq b\).
It is less singular than b and has full mass by the named primary input:

\[
                       m(h_k)=V. \tag{R2}
\]

Define Borel sets only off N,

\[
 E_{h,k}=\{b> -\infty,\ h\leq b-k\},\qquad
 F_{h,k}=\{b> -\infty,\ h>b-k\}.
\]

These partition X minus N. Strict comparison sets of quasi-psh
functions are plurifine open: locally one can write, for example,
\(\{h>b-k\}=\bigcup_{q\in\mathbb Q}\{h>q\}\cap\{b<q+k\}\).
The first factor is plurifine open and the second is ordinarily open.
Their local descriptions give the asserted plurifine openness globally.
On \(F_{h,k}\) the cutoff equals h. Locality gives

\[
 \mathbf1_{F_{h,k}}\operatorname{MA}_\theta(h_k)
       =\mathbf1_{F_{h,k}}\operatorname{MA}_\theta(h). \tag{R3}
\]

For each fixed h the sets \(F_{h,k}\) increase to
\(\{b> -\infty,h> -\infty\}\). The fixed measure
\(\operatorname{MA}_\theta(h)\) gives both excluded pole sets
mass zero. Consequently ordinary monotone convergence for this **fixed
measure**, together with (R2) and (R3), proves

\[
 \begin{split}
 D_{h,k}&:=\int_{E_{h,k}}\operatorname{MA}_\theta(h_k)
       =V-\int_{F_{h,k}}\operatorname{MA}_\theta(h),\\
 \lim_{k\to\infty}D_{h,k}&=V-m(h). \tag{R4}
 \end{split}
\]

This step does **not** assert that the full measures of \(h_k\)
converge to that of h: all cutoffs have mass V, whereas h can lose mass.

For every k, the two sets \(E_{A,k}\) and \(E_{B,k}\) are disjoint.
Indeed, at a point where b is finite, their simultaneous inequalities
would give \(b=\max(A,B)\leq b-k<b\). Moreover,

\[
                E_{C,k}=E_{A,k}\sqcup E_{B,k}. \tag{R5}
\]

On \(E_{A,k}\), one has \(A<B=b\). The strict set
\(O_A=\{A<B\}\) is plurifine open, using
\(\bigcup_{q\in\mathbb Q}\{A<q\}\cap\{B>q\}\).
On this whole strict set C=A, and therefore \(C_k=A_k\).
Locality on the strict set, followed by restriction to its Borel subset,
gives

\[
 \mathbf1_{E_{A,k}}\operatorname{MA}_\theta(C_k)
        =\mathbf1_{E_{A,k}}\operatorname{MA}_\theta(A_k).
\]

The analogous equality holds for B. Combining these with (R5) yields
the exact finite-cutoff identity

\[
                     D_{C,k}=D_{A,k}+D_{B,k}. \tag{R6}
\]

Pass to the three limits in (R4). One obtains
\(V-m(C)=2V-m(A)-m(B)\), which is (R1).
Every passage uses finite nonnegative integrals. No contact-set
intersection over uncountably many times, weak-measure limit interchange,
energy differentiability or source Siu decomposition is used.

If A is globally minus infinity, B=b and C is globally minus infinity,
so (R1) reads \(0+V=0+V\); the B case is identical. These cases do not
require undefined currents of an identically minus-infinity potential.

## 5. Proposed application to the source question

For the source's compact Kähler sublinear subgeodesic line, put
\(\psi_\tau=\widehat U_\tau\) and \(b=u_0\). The all-time Legendre
correspondence supplies the raw pointwise identity
\(b=\sup_\sigma\psi_\sigma\). Lemma 3.4 supplies

\[
 A_\tau=\widehat U^+_\tau=\sup_{\sigma\geq\tau}\psi_\sigma,
 \qquad
 B_\tau=\widehat U^-_{-\tau}=\sup_{\sigma\leq\tau}\psi_\sigma.
\]

Thus \(\max(A_\tau,B_\tau)=b\). Pointwise concavity gives
\(\min(A_\tau,B_\tau)=\psi_\tau\): otherwise slopes on both sides
would have values strictly above the value at tau, contradicting
concavity. The proof also works when that value is minus infinity.
No supremum has been replaced by a regularized envelope.

The source ensures A and B are psh or globally minus infinity, and psi
is psh or globally minus infinity. If \(u_0\) has full mass, (R1) would
therefore give the desired equality at **every** slope, including
endpoints and a collapsed interval. The bounded and finite-p-energy
cases have full-mass initial point. This proposed application is only
in the source's Kähler line category; the big-class version of (R1)
does not supply a merely big complete-line correspondence.

For the pure vertical line \(u_t=a+ct\), both half-time duals equal a
at tau=c. Here the equality has \(2V=V+V\). This keeps the original
all-time dual term. Dropping that term yields the source's separate
equation (20), whose everywhere strengthening fails at this collapsed
point; (R1) does not make that strengthening valid.

## 6. Independent curve route and projective calibrations

In dimension one \(A+B=C+b\) almost everywhere gives the current
identity \(T_A+T_B=T_C+T_b\). The degree-one nonpluripolar operation
is additive by the primary source, giving (R1) when b has full mass.
This separate linear-current route does not by itself prove the
higher-dimensional cutoff argument.

For an explicit projective family let X be P^n with unit-volume
Fubini–Study form, \(q=\sum_{j=1}^n|z_j|^2/\sum_{j=0}^n|z_j|^2\),
and \(0<r\leq1\). Consider the smooth subgeodesic line

\[
             u_t=r\log(1-q+q e^{t/r}).
\]

It starts at zero. Its dual, for \(0\leq\tau\leq1\), is

\[
 \psi_\tau=r\bigl((1-\tau)\log(1-q)+\tau\log q
       -(1-\tau)\log(1-\tau)-\tau\log\tau\bigr),
\]

with the continuous endpoint entropy convention; it is minus infinity
outside the interval. Its maximum at each point occurs at tau=q.
Hence A equals psi on q<tau and zero on q>=tau; B equals zero
on q<=tau and psi on q>tau. At the cutoff the radial first derivatives
match, so no interface atom is inserted by these piecewise formulas.

The radial potential of omega+ddc psi has derivative
\((1-r)q+r\tau\). In the proposed radial calculation its
nonpluripolar mass density is
\(n(1-r)((1-r)q+r\tau)^{n-1}dq\). This gives

\[
 \begin{split}
 m(\psi_\tau)&=(1-r+r\tau)^n-(r\tau)^n,\\
 m(A_\tau)&=1-(r\tau)^n,\\
 m(B_\tau)&=(1-r+r\tau)^n.
 \end{split}
\]

These formulas are research calibrations, not independent analytic
certificates for arbitrary potentials. At r=1 they recover the known
projective weak-line zero-mass construction. For r<1 the curves are
subgeodesic, not weak geodesic: on P1 the real radial/time Hessian
Schur complement equals
\((1-r)g''(\rho)g''(\rho+t/r)/(r((1-r)g''(\rho)+r g''(\rho+t/r)))>0\).
The finite checker compares the three mass formulas with independently
expanded polynomial integrals and checks this Schur-complement identity.
It is a sign and normalization check, not a proof of the general claim.

## 7. Hypotheses that must remain explicit

Full mass of b is essential for the right-hand side m(C)+V. For A=B=b
with a positive hyperplane pole of weight lambda on P^n, the mass is
\((1-\lambda)^n<V\), so that expression would give 2m(b)=m(b)+V,
which fails. This is a test of a deliberately weakened candidate, not
a counterexample to the source's full-mass question.

Pointwise minimum psh is also essential to the proposed proof. One
cannot replace C by an arbitrary rooftop P(A,B) and retain the local
equalities on the two strict sets. On P1, the two unit pole potentials
at distinct points have bounded maximum but their pointwise minimum
is not omega-psh; a rooftop with both unit poles cannot be a nontrivial
omega-psh potential. This does not contradict (R1)'s signature.

The candidate's remaining independent-audit targets are: plurifine
locality on every specified strict set, nonpolar exclusion of the common
pole set for all relative cutoffs, full-mass stability in the big-class
signature, and the exact raw tail identities in the line application.
No negative literature or novelty conclusion follows from the web
discovery searches. The current book, its protected analytic inputs,
all 42 statuses, catalogue and prior frozen releases remain preserved.
