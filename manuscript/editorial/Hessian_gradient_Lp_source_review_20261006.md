# Alternative gradients and the claimed Hermitian Hessian Lp range

**Source review only.** Baseline:
`a247be9cfaf325ce93eaee6709df53652bc0f931`.
Both exact primary PDFs were read in full, including proofs and
references: 34 physical pages in eighteen individually displayed sheets.
Chu--Liu page 12 was additionally inspected at higher resolution; this
repeated page is not counted as a new physical page. No active TeX,
book bibliography, canonical status or original-result receipt changes.

## Sources and reading scope

- Jianchun Chu and Yaxiong Liu,
  [Alternative proof of the gradient estimate for complex Hessian equations](https://arxiv.org/abs/2609.33091v1),
  2609.33091v1, submitted 27 September 2026 at 01:55:34 UTC.
  All nineteen actual pages were read and displayed. The current
  metadata lists only v1. The PDF has 394,504 bytes and SHA-256
  `8b13b9bbab21c537829bb6d03c11e1f8bb696ae0fe26557bd44711e4ab067c74`.
  Text SHA-256:
  `a048a8a436e86dfb64caa1287d6f3050ac1423d2e537cc5445dba35e40255d47`.
  Extraction reports a font-type mismatch warning; rendered pages were
  checked, including the boundary stability statement and its V.
- Truong Dinh Dat,
  [Uniform L∞ estimates for complex hessian equations on compact Hermitian manifolds](https://arxiv.org/abs/2607.23724v1),
  2607.23724v1, submitted 26 July 2026 at 15:41:09 UTC.
  All fifteen actual pages were read and displayed. The current
  metadata lists only v1. The PDF has 326,871 bytes and SHA-256
  `c31d2ceea1772df9881480b0cbf05b04293b79376ccd07c8b3602136c763f0fa`.
  Text SHA-256:
  `5c23002d3f8144f292933de3ebf1fd40c2e292203de05d3774a847b2872c5a69`.

The complete reading-record SHA-256 is
`cc433cfdc219f8353d4add12587e234835959738ff85c5568033f0026d385948`;
the frozen view-manifest SHA-256 is
`bc33dddf27aac7e60241be54a01671b757e3283c9b9747d96d287333895fa611`.
Acquisition and preparation remain separate immutable records with
their original false reading flags. The twelve literal diagnostics have
SHA-256
`b0e74befb23c2e252bfefc1a143b14f74301c72e75e1d69e6ee7a81001d4edef`.

## Chu--Liu: compact gradient mechanism and boundary distinctions

The compact equation uses sigma_k, without dividing by binomial(n,k),
and source potential convention i partial bar-partial. For the same
forms its potential is the book potential divided by 2 pi. Smooth
positive densities and a given smooth admissible normalized solution
remain the starting point. The p>n/k assumption concerns the density;
the derivative quantities in the gradient bound involve f^(1/k).

Actual 3--5 state the L∞, explicit Hou--Ma--Wu and stability inputs.
Actual 5--9 construct a logarithmic sup-convolution. A maximizing vector
has squared length at most epsilon. Concavity of the logarithmic penalty
and the cited derivative estimates for the inverse exponential field
give an admissibility loss of order K0/(-log epsilon), without a
nonnegative-curvature assumption in that particular argument. The L1
approximation error is of order K0 epsilon^(1/4). The stability estimate
then gives a logarithmic continuity modulus of order
K0^2/(-log distance).

On actual 9 the local elliptic estimate combines oscillation and the
complex Laplacian to bound the gradient at the center. The explicit
second-order bound sets the comparison radius at a constant multiple
of 1/(K1 Q), where Q is the maximal gradient. The logarithmic modulus
then bounds Q by exp(C K0^2 K1). This is an alternative to the usual
Liouville blow-up argument. Its quantitative stability, coordinate-field
and second-order inputs are separate from Guo--Song's fixed nearby
comparison-member argument. No full external-chain certification or
new book admission is made at this checkpoint.

Five exact diagnostics concern the printed source:

1. Theorem 1.2 on actual 2 defines gamma=np/(n-kp), which is negative
   for p>n/k. Theorem 2.4 on actual 4 and the subsequent argument use
   gamma=np/(kp-n)>0. With n=3,k=2,p=2 these are -6 and +6.
   The body exponent is the relevant one for the explained route.
2. Appendix A on actual 15 asserts a nonpositive range for
   rho0(t)=-(4 delta)^(-1) log(1+t/(2M0)), under sup phi=0.
   At the allowed value t=-1, M0=2, CBK=1, delta=1/192,
   rho0(t)>0 and -rho0'(t)=16, exceeding the printed upper bound 12.
   The printed interval corresponds instead to a nonnegative translated
   potential. That translation and constant changes require a correction;
   a complete repaired second-order proof is not certified here.
3. Theorem 5.5 on actual 12 is false **as printed**. On the closed unit
   ball in C^3 take omega=i partial bar-partial |z|^2,
   phi=8(|z|^2-1), the same function as subsolution, and v=0.
   The equation has smooth constant density sigma_2(9I)=243 and zero
   boundary data. All admissibility and comparison hypotheses hold.
   For p=2 and beta=1/20 (less than 1/13), the stated right side is
   zero because ||v||=0, while sup(v-phi)=8.
4. The same substitution gives V=||v||+sup phi+1=1, W=8 and
   tau=W/(4V)=2 in the printed proof. Thus 1-tau is negative;
   division reverses an upper-test inequality and cannot preserve the
   admissible cone under the ensuing negative scalar. The proof later
   retains V, whereas the theorem states a power of ||v|| alone.
   An absolute-potential scale and a nonzero additive term are distinct
   requirements for any proposed correction.
5. Actual 10 solves Delta b=-n with boundary data psi<=0 and infers
   b<=0. On the same unit ball with psi=0, b=1-|z|^2 is positive
   inside. A further constant shift can ensure negativity, but the
   displayed boundary normalization alone does not. The separate order
   phi<=b is not refuted.

The boundary gluing is on actual 10--12, the local auxiliary
Monge--Ampère construction on 12--14, and the second-order sketch on
15--18. The quadratic substitution refutes the printed boundary
stability formula, **not** the known Collins--Picard gradient theorem
or Chu--Liu's compact gradient conclusion. The boundary gradient sketch
also retains its boundary elliptic inputs; the compact interior-ball
calculation does not by itself check a ball crossing the boundary.

The cited Cheng--Xu regularization paper is
[2208.14539v1](https://arxiv.org/abs/2208.14539v1), submitted 30 August
2022 at 21:05:51 UTC, related to the 2024 publication on pages 951--984.
It is **different** from the earlier selected 2406.00953v2 viscosity
paper. Current metadata was checked, but no fresh proof reading of
2208.14539 or its published edition is claimed here. The forthcoming
dependency pass must check its exact Lemmas 2.9, 2.11, 2.17, Proposition
2.16 and stability lemmas before a complete quantitative import.

## Dat: invalid estimates and the Lp boundary

The source allows every 1<=m<=n and states a uniform bound and bounded
existence for every p>1. Its convention is ddc=i partial bar-partial/pi,
so source potential is half the book potential for the same forms.
The classical distinction matters: in intermediate Hessian theory
the familiar sufficient density range is p>n/m, while p>1 is the
Monge--Ampère range. The previously fully read Dinew--Kołodziej
1203.3995v2, actual 3, states the p>n/m compact Kähler result and refers
to its earlier estimates. This reuse is not a fresh full-paper reading.
The earlier estimate paper's published PDF and current arXiv metadata
were located for the next pass; no full reading of that new dependency
is claimed at this checkpoint.

Seven exact diagnostics identify what fails in the current source:

1. Proposition 3.1 on actual 5 claims H_m(u)<=C omega^n on **every**
   Borel set, with C controlled by potential sup norms. This is not
   CLN. The local smooth bounded profile A sqrt(x_1^2+epsilon^2) has
   one Hessian eigenvalue A/(4 pi epsilon) at the origin in the source
   convention. With n=3,m=2 its normalized density there is
   1+A/(6 pi epsilon). A fixed smooth cutoff and a small fixed A
   control negative annulus Hessians uniformly on a flat torus, so
   these are globally admissible examples with common potential bounds
   and unbounded densities. The all-set volume domination is false.
   Actual 6's pointwise Hessian control from CLN repeats this error.
2. Actual 9 integrates C s^(-q) from zero to infinity and asserts
   convergence for q>1. It diverges at zero: for q=2 the integral
   from eta to 1 is 1/eta-1. A small-s mass bound must be separate;
   it does not repair the preceding false volume domination.
3. Proposition 5.3 on actual 9 obtains t<=C/capacity and then uses
   t^(-q)<=(capacity/C)^q. The correct reciprocal direction is >=.
   For C=1, capacity=1/2, t=1/2 and q=2 its purported bound is
   4<=1/4. Also t must remain below 1, which the proposed
   small-capacity optimization ignores. This does not refute valid
   capacity-volume inequalities with their correct exponents.
4. Actual 10 and equation (5) on 12 use one capacity test to claim an
   upper bound for a supremum. On a flat complex three-torus with
   omega=i sum dz_j wedge dbar z_j, u=3(cos x_1-1) is smooth and
   strictly omega-psh. For m=2 its density is
   1-cos x_1/(2 pi)>0 with average one. On the positive-volume set
   E_2={u<-2}, u_2=max(u,-2) is constant, hence H_2(u_2)=omega^3.
   The zero capacity test gives cap(E_2)>=Vol(E_2), whereas the
   printed (5) gives cap(E_2)<=Vol(E_2)/4. The preceding
   (u_t+t)/s also need not lie in [0,1] for arbitrary s.
5. Lemma 6.2 on actual 11--12 is false as stated. Put
   A(t)=exp(-t), m=2, p=2, alpha=3/2 and C=6. Its first term to
   power alpha is exp(-3t/4)/s^3. For all t,s>0,
   A(t+s) divided by this term equals exp(-t/4-s)s^3<=6,
   using exp(s)>=s^3/6. Thus the stated recursion holds while
   A(T)>0 at every finite T. The required nonlinear gain is
   alpha(1-1/p-m beta)>1; alpha>1 alone does not supply it.
6. Actual 7 differentiates H_m(u_t) with m equal summands in addition
   to a prefactor m. For the local scalar model H_2(u_t)=(1+t)^2,
   the actual derivative is 2(1+t), while the printed formula is
   4(1+t). This fixed factor is different from the essential exponent
   and capacity failures.
7. The standard Poisson power already disproves the claimed all-m
   uniform range. On a flat complex two-torus, localize
   u_epsilon=-A(|z|^2+epsilon^2)^(-1/4) by a fixed nonnegative
   cutoff and choose A small to control its annulus trace. In the
   inner chart its unscaled complex trace is
   (3s+8epsilon^2)/(16(s+epsilon^2)^(9/4)), s=|z|^2, which is
   positive and at most C(s+epsilon^2)^(-5/4). The density's
   L^(3/2) integral is uniformly bounded by an integrable multiple
   of s^(-7/8) ds. The global functions are smooth, admissible for
   m=1, have sup zero and mean-one positive densities with c=1,
   but their negative center values are -A epsilon^(-1/2).
   This standard localized power refutes the printed uniform estimate
   already for m=1. Its limiting Poisson density is L^(3/2), yet has
   no bounded solution: a second distributional solution on the
   compact torus differs by a harmonic constant. This also excludes
   the all-m bounded-existence claim. No new intermediate-Hessian
   endpoint classification is asserted.

The operator definition on actual 3 writes nonlinear powers for an
arbitrary L1 current without first defining them by linear positivity
tests. Smooth decreasing approximation is assumed for bounded general
Hermitian admissible functions; its hypotheses are not supplied. The
comparison derivation on actual 7 additionally replaces derivative
terms by potential-gap volume terms without adequate justification.
The existence argument on actual 14 uses L1 compactness followed by
continuity for decreasing sequences, although no decreasing subsequence
has been constructed; it also keeps one normalizer c for all smooth
approximants without proving that choice. The cited smooth-existence
and stability papers retain their own domains. These additional gates
are not made into independently certified full proof repairs.

The Dat p>1 estimate and its dependent existence/stability chain are
**excluded from book admission**. Valid Hermitian Hessian comparison,
known p>n/m results and the Monge--Ampère p>1 case are not refuted by
the source-specific checks. No generalized bound is inferred from this
paper to close the remaining weak auxiliary estimates in Chapter 68.

## Preservation and next work

All 425 active inputs, 108 protected inputs, 68 prior frozen manifests
(56 integrations and twelve source reviews), 124 prior exports, the
checked 4,398-page book and fourteen generated files retain their bytes.
The other 5,061 tracked baseline files are unchanged; README and the
programme record this source-only checkpoint. The native catalogue,
editor state, inactive toric candidate, all 42 canonical status rows
and general Siu/closure boundary remain unchanged.

No repeated unchanged-book build, new book-PDF review, native compile,
original result, independent production model call or verification
receipt is claimed. The literal calculations above are source checks,
not newly admitted formal results. Both main and work are fetched before
the regular work-branch checkpoint and the existing draft PR update.
Continue by reading the exact Cheng--Xu regularization and published
Dinew--Kołodziej capacity proofs, then evaluate a conditional compact
gradient explanation with its corrected positive exponent. The new
polynomial Hessian preprint 2610.06529 is a further metadata lead only;
its proof and applicability remain unreviewed.
