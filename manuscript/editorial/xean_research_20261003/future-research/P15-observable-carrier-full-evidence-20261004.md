# New observable-carrier proposals: all UNVERIFIED


# Observable compact carrier: UNVERIFIED future route

Origin: new root mathematical proposal, not a theorem grant. No acceptance,
no original closure and no feedback into the running rounds31/32 or reviews.
Investigate only in a later small P15.1/P15.2 batch, with full independent
reconstruction. This may produce substantive new results; it is not a
license to relabel a spectral carrier as a geometric complex d-fold.

Use the already supplied complete prescribed-type proofs as evidence,
with all exact source hypotheses. Let X be connected compact Kahler of
dimension n, alpha pseudoeffective of class volume0, theta smooth, psi an
actual theta-psh reference, C=C_psi its actual bounded singularity type,
d<n its actual nonpluripolar degree, m=n-d, P=T_psi. All degree>d mixed
products of currents from C vanish. Retain actual reference type, gauge,
raw positive mass, anchor, and the distinction d versus class nu.

## 1. A potentially crucial algebra identity

On the common finite locus Z=X\{psi=-infinity}, define

    D=span_R{u-psi:u in C}.

These are bounded real functions. Constants belong to D. The proposal is
that D is an ALGEBRA, rather than just an energy test vector space.

First any h in D can be represented h=A(v-w), where A>0 and v,w in C.
Split a finite linear combination of u_i-psi into positive and negative
coefficients and add suitable multiples of psi to both sides so the
total positive weights on each side agree; divide by their common total.
Convexity of theta-psh potentials and bounded type gives v,w in C.
The zero function is handled separately.

For v,w in C with |v-w|<=B on Z, B>0, define a globally convex function
nondecreasing in both variables by

    F(a,b)=sup_{t in [-B,B]}[2t(a-b)-t^2+2B(a+b)].

Every affine term has nonnegative coefficients 2(B+t),2(B-t) whose sum
is4B. On |a-b|<=B, the supremum is attained at t=a-b and equals
(a-b)^2+2B(a+b). For a local theta potential rho,

    F(v+rho,w+rho)=F(v,w)+4B*rho.

Thus the convex nondecreasing composition should show F(v,w) is
4B*theta-psh. At common poles define it as minus infinity, not an
undefined infinity subtraction. Give a full rigorous composition and
upper-semicontinuous extension argument (all affine terms have a fixed
positive total coefficient). Its bounded difference from4B*psi makes
a=F(v,w)/(4B) an element of C. Consequently

    (v-w)^2 = 4B*(a-psi)-2B*(v-psi)-2B*(w-psi) in D.

Scaling gives h^2 in D, and polarization gives h1*h2 in D. Check B=0,
negative constants, real coefficients and all singular loci. This avoids
assuming that arbitrary bounded DSH functions form an algebra without
proof; it proves the assertion for this actual common-type family.

## 2. A canonical compact observable carrier

Let A be the uniform closure of D in bounded real functions on Z with
the actual sup norm. Define the evaluation map

    ev:Z -> product_{h in D}[-||h||,||h||]

and K as its closure. Tychonoff gives compact Hausdorff K. Coordinate
functions h-hat give an isometric unital separating algebra on K;
Stone--Weierstrass identifies its uniform closure with C(K,R). This
also identifies K as the real Gelfand spectrum of A, independently of
temporary generators or bases. Explain exactly the universal minimal
compact-carrier sense: other compact realizations of the same uniformly
closed separating observable algebra are canonically homeomorphic; a
larger carrier with extra tests is not being claimed equivalent.

Every positive measure mu_(u,omega)=<T_u^d>omega^m defines a bounded
positive functional h->int_Z h dmu on D. It extends to C(K) and Riesz
gives a finite regular positive measure mu-hat_(u,omega) on K. Its raw
mass remains M_d(psi,[omega])>0, with no probability normalization.
Do NOT assume ev is Borel into an uncountable product or silently use a
pushforward theorem; this positive-functional construction is sufficient.

K is generally a compact observable carrier, not a proved complex
analytic d-dimensional space. Determine every dimension claim honestly.
Its covering dimension is well-defined but not thereby identified or
shown finite. In a supplied fibration it need not literally equal the
base because bounded psh differences can be discontinuous. Any original
completion verdict must use the actual original carrier/dimension
requirements, not mere terminology.

## 3. Auxiliary cohomology may suffice on this carrier

For h in D, signed dd^c h is a finite linear combination of differences
of actual common-type currents. Pairing it with A_u=<T_u^d> gives zero
in the precise nonpluripolar relative sense, by degree>d mixed vanishing.
For two cohomologous Kahler forms omega0,omega1,

    omega1^m-omega0^m=dd^c g * sum_{j=0}^{m-1}omega1^j omega0^(m-1-j).

Signed IBP with h and smooth g, against the closed positive current
A_u times each smooth complementary factor, should give

    int h A_u(omega1^m-omega0^m)=0.

All bounded DSH representations have the common psi polar locus and
A_u puts no mass there, so check every admissibility hypothesis using
the exact Vu intrinsic definitions and normalization. Since D is an
algebra and dense in C(K), this proves equality of the actual regular
measures on K for cohomologous auxiliary forms. It does NOT prove
equality of ambient-X measures; the known P1xP1 example remains valid.

The same factorwise argument may give polynomial dependence on lambda
in H^(1,1)(X,R), of degree m, for every h observable. Prove full
representative independence, not merely an unverified symbolic claim.

## 4. Minimum energy reference may also be minimum operator reference

If the new minimum-reference energy theorem is actually established,
let Q=Sym^m V/Ann(span{ell_v:v in C}), with ell_v the coefficient
functional of anchored energy E_psi,lambda(v). Prove rather than assume
that q(lambda0^m)=q(lambda1^m) iff EVERY spectral operator measure for
u in C agrees for those references.

Forward route: equality of all anchored energy polynomials gives
equality of derivatives along the convex segments from u to v, hence
int(v-u) dmu-hat_u. The terminal derivative on psi->u determines
int(u-psi)dmu-hat_u. Combining determines int(v-psi)dmu-hat_u for
every v in C, then every h in D, then all C(K) tests. Use the precisely
proved bounded affine variation theorem, including one-sided endpoint
derivatives, and raw masses via constant shifts.

Reverse route: equality of all spectral operators gives equality of
their segment energy primitives, so all anchored energies agree,
which is the already proved necessary/sufficient energy quotient law.
Thus the finite-dimensional energy reference would be the same minimum
reference for the entire observable operator family. This is more than
the purely definitional full-form kernel quotient on ambient X.

## 5. Full-mass truncations may converge in total variation

For any more-singular degree-d full-mass u and u_L=max(u,psi-L), put
G_L={u>psi-L} on simultaneous finite loci. Plurifine locality gives
mu_uL=mu_u on G_L; both measures have the same mass M. Their
complement masses therefore agree. Since G_L increases to a locus of
full mu_u mass (all polar sets have zero mass),

    ||mu_uL-mu_u||_TV <= 2*mu_u(X\G_L) ->0.

State the TV-norm convention and give a complete proof including the
degree0 case, all actual comparison-potential/product-factor hypotheses,
and source truncation/exhaustion. Weak convergence alone is insufficient
for bounded discontinuous h; this exact full-mass/locality argument may
give the required much stronger estimate. The established energy proof
already uses the corresponding scalar complement identity for weights.

This would extend the carrier measures and minimum-reference equality
from bounded type to the entire common full-mass domain, without needing
finite energy. Reference equivalence passes by TV convergence separately
for each fixed auxiliary class. Prove auxiliary-independent full-mass
domain first, using the actual scalar nonnegative mixed-deficit argument
from the new batch, never assuming a positive difference of actual product
currents. Do not import the Kahler-only subset statements of Vu Lemma4.10.
Same-type anchor and theta gauge changes need precise canonical carrier
identifications: the observable algebra is unchanged after bounded
anchor translation; gauge leaves actual differences and currents fixed.

## 6. A rate-free operator limit for observable tests

For u in C and (theta+epsilon*omega_epsilon)-psh u_epsilon with the
same actual psi-type, let delta_epsilon=sup_Z|u_epsilon-u|->0. No
delta=o(epsilon) condition is proposed on the observable carrier.
For h=v-psi, v in C, factor the difference of the top products and
apply signed IBP against h:

    int h[MA_epsilon(u_epsilon)-MA_epsilon(u)]
      = int(u_epsilon-u) dd^c h * sum mixed(n-1)-products.

Here dd^c h=T_v-P. Both terms with one UNPERTURBED actual-type current
and n-1 perturbed currents are positive. Their total mass, by precise
mixed bounded-type mass equality, is the mass of

    <P*(P+epsilon*omega_epsilon)^(n-1)>.

Expansion and actual degree d imply this is O(epsilon^m), rather than
the O(epsilon^(m-1)) bound used for an arbitrary smooth ambient-X test.
For d=0 it is zero. Prove positivity, mixed cohomology backgrounds,
comparison sets and every IBP application with possibly varying
auxiliary representatives. The rescaled error should be O(delta).

If [omega_epsilon] converges to a fixed Kahler class lambda, the mixed
cohomological masses are uniformly controlled even without smooth
representative convergence. For the fixed u expansion, leading
observable measures are representative-independent as in3 and vary
polynomially with the class; lower actual degrees have higher powers
of epsilon and bounded h gives scalar cohomological mass control.
Extend convergence from D to all C(K) tests by uniform approximation
and the uniformly bounded rescaled raw mass. The proposed limit is
mu-hat_(u,lambda), with factor epsilon^(-m)/binom(n,d), and might be
independent of every auxiliary path with the same stated class limit.

This is a new proposal requiring full proof, not the general ambient-X
rate-free assertion. It also does not permit unbounded moving potential
or weighted energy path limits refuted by the analytic concentration
example. If one extends potential domains or claimed paths, prove each
extension separately.

## Original-scope decision

If proved, the compact observable-carrier construction, algebra
identity, common full-mass extension, finite-dimensional minimum
reference and rate-free class-convergent operator limit are substantive
new theorems. A separate original-scope review must decide whether they
answer P15.1/P15.2 with their actual carrier/dimension criteria. Unknown
geometric dimension cannot be disguised as d. The construction cannot
be called canonical on the ambient X without its necessary full-form
data. All original atoms remain open at the time of this proposal.


# UNVERIFIED future addendum: actual unbounded potentials on the carrier

This is new root mathematical evidence for a later batch, not a grant or
feedback into rounds31/32. It supplements the immutable observable-carrier
proposal with an explicit unbounded potential reconstruction route.

For u more singular than psi, normalize u<=psi, set u_L=max(u,psi-L),
and h_L=u_L-psi. Each h_L belongs to D and gives a continuous function
h_L-hat on the compact carrier K. On the dense evaluation image, for
L'>L one has h_L=max(h_L',-L). Both sides are continuous, so this exact
identity holds on K. Define

    u-hat_relative = inf_L h_L-hat.

It is upper semicontinuous, possibly minus infinity, and obeys
h_L-hat=max(u-hat_relative,-L). Prove this from the consistency
identities, not just from pointwise evaluation on a dense set: decreasing
limits of continuous functions need not be determined by their values on
a dense set without these truncation identities. On Z this recovers the
actual u-psi, including minus-infinity values where u has additional poles.

For the carrier measure mu-hat_u, the law of each scalar continuous
h_L-hat agrees with the law of the bounded Borel function h_L under the
ambient measure mu_u. This follows because every continuous scalar
function of h_L is in the uniform closure A, so their integrals agree;
uniqueness of finite Borel measures on a compact interval proves equality
of the scalar laws. No Borel evaluation-map assumption is required.

As L grows, the consistency identities imply that carrier sublevel
events can be tested by the continuous h_{L+1}-hat. If the ambient
mu_u puts no mass on the additional polar locus of u, its distributional
tails tend to zero. This should imply

    mu-hat_u{u-hat_relative=-infinity}=0.

Prove the precise event identities and all strict versus weak inequality
choices. Via monotone convergence, scalar weighted integrals of the
unbounded reconstructed potential agree with their ambient counterparts.
Do the corresponding construction for every joint mixed degree-d
measure and every needed pair of unbounded potentials before claiming
the full finite-energy formulas on K. The positivity, full-mass and
locality applications are indispensable; TV convergence alone does not
control unbounded weighted tails.

The minimum-energy quotient and bounded observable operator equivalence
may therefore retain actual unbounded potential data on K, rather than
only provide abstract bounded tests. Unbounded energy/cocycle properties
can be transported only after these exact integral identities and the
previous genuine F1 theorem are proved. No new moving-unbounded-path
limit follows; the concentration counterexample remains in force.

General decreasing full-mass sequences are a separate issue: ambient
weak convergence does not imply convergence against discontinuous
bounded observables in D. The strong TV estimate proposed for the
specific truncations is not a TV estimate for every decreasing sequence.
Any such carrier continuity claim needs its own checked weighted local
bounded convergence/capacity and full-mass-tail proof. State the remaining
gap honestly rather than importing ordinary smooth-test convergence.

The geometric dimension of K is also unresolved by this addendum. A
separate original-scope audit must determine which dimensional-carrier
requirements are actually imposed in P15.1/P15.2. The new construction
cannot be described as a complex d-fold merely because its product
degree is d. No theorem is accepted and all original atoms are still open
at the time of writing this addendum.


# UNVERIFIED future addendum: bounded observables and genuine unbounded inputs

Origin: fresh root mathematical proposal. No theorem accepted and no original
closure asserted. This is not feedback into any frozen author or review.
Use only in a later fresh P15.1/P15.2 batch with full reconstruction. It
supplements the observable-carrier and unbounded-potential proposals and the
fully read scoped minimum-reference proofs. It supplies a possible answer to
the earlier warning that ambient weak convergence alone is insufficient for
discontinuous observables. The proposed stronger result requires the argument
below, rather than an inference from ambient weak convergence.

## 1. A proposed bounded-observable decreasing convergence lemma

Fix an actual reference psi, its actual degree d, m=n-d, and a fixed smooth
Kahler auxiliary omega. Write C for the two-sided bounded comparison type and
D=span_R{v-psi:v in C}, evaluated on Z={psi finite}. Assume the earlier
algebra proof has actually been supplied and checked before using D as an
algebra or using the carrier K. Fix finitely many common degree-d full-mass
potentials u_(i,j) decreasing to full-mass u_i, for i=1,...,d. The individual
and ordered mixed masses equal the reference mass M against omega^m by the
common-domain/convexity argument. No difference of product currents is
assumed positive. Let

    A_j=<T_(u_(1,j)) ... T_(u_(d,j))>,   A=<T_(u_1) ... T_(u_d)>.

For a fixed h in D the proposed assertion is

    integral h A_j omega^m -> integral h A omega^m.              (WC)

The degree-zero case has A_j=A=1 and is immediate. Constants and real linear
combinations reduce the other cases to h=v-psi, v in C. Choose finitely many
coordinate charts, smooth theta local potentials rho, a smooth partition of
unity with relatively compact support in each chart, and a dominating Kahler
background. Subtract local constants so the local psh functions

    p_i=u_i+rho,  p_(i,j)=u_(i,j)+rho,  a=v+rho,  b=psi+rho

are all nonpositive on the working relatively compact chart, uniformly in j.
This is possible since p_(i,j)<=p_(i,1), with finitely many i. The functions
a-b and h agree on their simultaneous finite locus. Put

    s=sum_i p_i+a+b,
    beta_L=min(1,max(s+L,0)).

Then 0<=beta_L<=1; beta_L increases to1 wherever all the listed functions
are finite. Its nonzero locus has s>-L, and because every summand is
nonpositive, each summand is >-L there. In particular p_(i,j)>=p_i>-L,
a>-L and b>-L on this locus. Locality consequently identifies beta_L A_j
with beta_L times the product of the bounded psh truncations
max(p_(i,j),-L), and identifies beta_L h with beta_L times the bounded
quasicontinuous difference max(a,-L)-max(b,-L). The analogous identities
hold for A. Only the NONZERO locus of beta_L is used, not its closed support.

At each fixed L the truncated factors decrease to their bounded limits and
converge in local capacity. Use GZ's theorem for bounded decreasing
potentials with local/global capacity comparison, or the corresponding
standard local bounded capacity theorem with its precise hypotheses. The
fixed beta_L and the fixed bounded truncated weight are quasicontinuous.
DDNL Proposition2.2 then gives convergence of their weighted top products
after filling complementary slots by smooth positive factors. Expanding
the fixed omega^m locally into the needed smooth coefficient tests gives
the partition-weighted integrals. The smooth coefficients and partition
cutoffs are legitimate uniformly bounded continuous multipliers. Thus
for the globally assembled beta_L (chartwise, with the fixed partition),

    integral beta_L A_j omega^m -> integral beta_L A omega^m,
    integral beta_L h A_j omega^m -> integral beta_L h A omega^m.

Here global beta_L means the partition-weighted sum of the local cutoffs;
it still lies in[0,1] and increases to1 off a finite union of pluripolar
loci. All measures in question are nonpluripolar, so the limit cutoff is1
almost everywhere for every A_j and A. Equality of the TOTAL mixed masses
is indispensable to control the omitted term:

    lim_j integral (1-beta_L) A_j omega^m
        = M-integral beta_L A omega^m.

For fixed h of bound B, both omitted absolute weighted integrals are at
most B times their omitted masses. First pass j to infinity at fixed L,
then L to infinity. Monotone convergence for the LIMIT measure makes the
right side tend to0 and proves (WC). This argument does not assert a
uniform absolute-continuity estimate in capacity for arbitrary unbounded
products; it obtains the required tails from local bounded convergence
and equality with the full-mass limit. Each chart and every complementary
factor must be checked in the eventual full proof.

## 2. Proposed consequences for the compact observable carrier

The earlier proposal constructs K from the uniform observable algebra D,
not by assuming that its uncountable evaluation map is Borel. Positive
integration functionals define regular finite measures on K by Riesz.
Equation(WC), if proved, gives convergence of their integrals on D; uniform
density in C(K) and the common finite mass give weak convergence on K.
This is a separate weighted theorem, not a consequence of ordinary
ambient-X weak convergence. It applies to ordered mixed tuples too.

The proposed representative-independence argument for bounded-type inputs
uses signed IBP and mixed degree-(d+1) vanishing. For a fixed full-mass
input u, its canonical relative truncations u_L have the same mass and
agree with u on {u>psi-L}. Their ambient trace measures consequently
converge in TOTAL VARIATION by the exact complement identity. This carries
every bounded h in D through the truncation and extends representative
independence to all full-mass inputs. Do not claim TV convergence for
arbitrary decreasing sequences; (WC) gives their carrier weak convergence.

For each fixed h in D and each full-mass u, the observable measure's
evaluation is a homogeneous degree-m cohomology polynomial. To justify
this on the unbounded domain, use finitely many unisolvent Kahler powers,
the bounded polynomial identity, and the fixed-form TV truncation limit.
The interpolation inverse forces coefficientwise convergence, exactly
as in the finite-energy polynomial proof. For mixed complementary Kahler
products use the same scalar-deficit mass equalities and polynomial
extraction; arbitrary real closed factors are differences of Kahler
factors. Do not perform unjustified unbounded IBP.

Let Q be the FINITE-dimensional minimum energy-family reference quotient
from the proved bounded energy functionals. The proposed bounded variation
argument identifies equality of all energy functionals with equality of
all bounded-type carrier operator measures. TV truncation extends that
equality to all common full-mass inputs. Hence each bounded-observable
evaluation on the full-mass domain annihilates Ann(S) and descends to Q.
For each fixed continuous f on K, extend from D by uniform approximation:
at every fixed Kahler auxiliary mass bounds control the error; finitely
many unisolvent evaluations then define the coefficient functional. This
is a genuine finite-dimensional factorization, not a claim that the
ambient full-form quotient W/N is finite dimensional.

Now if u_j decrease in common full mass to full-mass u, and tau_j->tau in
Q are actual admissible auxiliary data, (WC) at the finitely many
unisolvent classes gives coefficientwise convergence for each f in D.
The resulting evaluations at tau_j converge. To extend from D to all
C(K), their raw masses M(tau_j) are bounded because M descends to Q and
is continuous. This proves the proposed joint decreasing-input and
finite-reference continuity on K. Class convergence implies convergence
of q(lambda_j^m) without controlling smooth form representatives.

Together with positive polynomial expansion and scalar mixed-mass bounds,
this would give a carrier perturbation limit for decreasing
ORIGINAL-background common full-mass inputs and class-convergent
auxiliaries, without the ambient theorem's extra full-form quotient
convergence assumption. The separate proposed genuinely perturbed
BACKGROUND bounded-type estimate still needs its own gain of one
epsilon from testing against h=v-psi. No arbitrary unbounded perturbed
background limit follows from this addendum.

## 3. Complete truncation-law identities for unbounded potentials

Normalize u<=psi. On Z put h_L=max(u-psi,-L). It is u_L-psi, hence a member
of D and a continuous coordinate hhat_L on K. For L'>L, the exact identity
h_L=max(h_L',-L) holds on the dense evaluation image and therefore on K.
Take positive integer L tending to infinity and define

    uhat=inf_L hhat_L.

It is extended-valued upper semicontinuous, and

    hhat_L=max(uhat,-L)                                      (TL)

follows by sending L' to infinity in the continuous scalar max identity
at each point of K. This is valid also when uhat=-infinity. It does not
follow merely by agreement of decreasing limits on a dense subset.

Fix ANY positive joint mixed full-mass trace measure mu and its carrier
measure muhat. Every continuous scalar function of h_L belongs to the
uniform observable algebra: polynomial approximation on[-L,0] follows
from the unital algebra property. Thus the scalar laws of h_L under mu
and hhat_L under muhat agree. More generally the JOINT laws of any
finitely many bounded truncation coordinates agree, by polynomial
approximation on a compact rectangle and uniqueness of finite regular
measures there. This is all finite-dimensional scalar measure theory;
no Borel assertion about the uncountable evaluation map is needed.

For any positive integer k choose L=k+1. Identity(TL) gives

    {uhat<=-k}={hhat_(k+1)<=-k}.

Scalar law equality identifies this mass with
mu{u-psi<=-k} on Z, including additional u poles where u-psi=-infinity.
The latter masses decrease to0 because mu does not charge either polar
locus. Therefore muhat{uhat=-infinity}=0. The strict and weak sublevel
choices are explicit and cause no hidden boundary assumption.

Monotone convergence applied to -hhat_L and -h_L gives equality, finite
or infinite, of their unbounded nonnegative integrals. For finitely many
F1 inputs, the existing joint mixed-integrability theorem makes each such
integral finite under every needed mixed measure. Hence the joint law and
dominated convergence give equality of the signed difference integrals
of two reconstructed relative potentials and their ambient counterparts.
This transports the genuine finite-energy expression and cocycle to K.
It does not estimate weighted tails for a new moving-potential sequence.

## 4. An exact bounded-anchor change on all of K

Let chi in C and let c=chi-psi in D, ||c||<=B. The observable algebra is
unchanged: v-chi=(v-psi)-(chi-psi), with the converse identity as well.
This identifies the compact carriers canonically through the same
uniform algebra. For J>=L+B the ambient identity is

    max(u,chi-L)=max(max(u,psi-J),chi-L).

Consequently the continuous coordinate attached to max(u,chi-L)-chi
is max(hhat_J^psi-chat,-L) on K: both sides are continuous and agree
on its dense evaluation image. Sending J to infinity and using(TL)
gives

    hhat_L^chi=max(uhat^psi-chat,-L),
    uhat^chi=uhat^psi-chat.

This proves the unbounded reconstructed potential's anchor law on ALL of
K, without assuming that dense-set equality determines an arbitrary
upper semicontinuous function. Smooth theta gauges preserve all actual
differences and products, so give the corresponding canonical
identification. Apply the joint integral identities before transporting
any energy anchor-change law.

## 5. Degree-zero carrier rigidity: a possible fully explicit endpoint

This separate candidate proof must be checked. For v in C let h=v-psi,
|h|<=B. Choose a smooth Kahler Omega dominating theta, so v and psi are
Omega-psh after adding the same smooth gauge if needed; normalize their
suprema and truncate both at -L. The bounded differences
h_L=max(v,-L)-max(psi,-L) have |h_L|<=B and satisfy

    integral dh_L wedge dc h_L Omega^(n-1)
       = -integral h_L (ddc max(v,-L)-ddc max(psi,-L)) Omega^(n-1)
       <=2B integral Omega^n.

The equality is the bounded classical IBP identity with the correct
normalization. Both positive Omega currents have mass integral Omega^n.
Their difference removes the identical smooth background. Thus h_L are
uniformly W^(1,2), converge almost everywhere and in L2 to h, and their
weak gradients have weak subsequences converging to the distributional
gradient of h. On each finite comparison set
E_j={v>-j,psi>-j}, Sobolev locality applies to h and h_L because both
are W^(1,2) and coincide there for L>=j. Their gradients therefore
coincide almost everywhere on E_j. The union of these sets has full
smooth volume; its excluded polar sets have zero smooth volume.

The intrinsic Vu gradient against the SMOOTH current Omega^(n-1) is
defined through exactly these simultaneous restrictions. Its diagonal
thus agrees with the ordinary W^(1,2) gradient measure just identified;
write out the source definition and verify this equality rather than
asserting strong gradient convergence. Intrinsic bounded admissible IBP
gives

    integral dh wedge dc h Omega^(n-1)
      = -integral h (<T_v>-<P>) Omega^(n-1)=0

when actual degree d=0. Degree-one nonpluripolar products of all C inputs
vanish by the already proved mixed mass bound. Nonnegativity makes the
ordinary weak gradient zero. Connectedness then makes h constant almost
everywhere. As distributions v=psi+c; the canonical quasi-psh
representatives recover equality everywhere. This would show D consists
exactly of constants, K is a singleton of genuine covering dimension0,
and its carrier measure is M(lambda) delta_point. The scalar energy for
bounded type is c M(lambda). This is not a proof that all MORE-singular
degree-zero full-mass potentials are constant, nor that unbounded
perturbation energies have a new path-independent limit. Any singleton
carrier unbounded reconstruction consequences must follow separately
from the exact laws above, not from a false domain-inclusion claim.

For d>0, no finite or complex geometric dimension of K is proved here.
The current degree remains distinct from that dimension. A separate
literal-original-scope audit must decide which further geometry the
question actually requires. All results of this addendum remain proposals.


# UNVERIFIED further consequence of the degree-zero rigidity candidate

This is a new root proposal for the next fresh P15 pair, not an accepted
theorem or feedback into a frozen worker. It is conditional on the complete
Sobolev/intrinsic-gradient identification in the weighted-carrier addendum
being independently proved. Do not assume that identification from a review,
a bounded truncation gradient bound alone, or a Kahler-only subset theorem.

If actual degree d=0 and every v in C_psi is proved to equal psi plus a
constant, then the rigidity automatically extends to EVERY theta-psh u
more singular than psi, not just the full-mass or finite-energy subclasses.
Indeed, subtract a constant so u<=psi, and set u_L=max(u,psi-L). These are
theta-psh and in C_psi. Hence u_L=psi+c_L everywhere for real c_L in[-L,0].
They decrease, so c_L decreases. Both u and psi are finite off pluripolar
sets of zero smooth volume. At a point where both are finite, their actual
difference is finite, and c_L tends to that difference. Therefore c_L has
a finite limit c. Passing to the pointwise limit gives u=psi+c on Z, with
the common minus-infinity values at psi's poles. There can be no additional
u pole: it would force c_L=-L at that point for every L and contradict the
finite limit at the generic point. Thus the equality is everywhere.

Consequently the entire more-singular domain would equal C_psi, and the
degree-zero full-mass and finite-linear-energy domains would both be this
constant-translation family. The apparent ordinary smooth-volume F1
integrability at d=0 would then reduce to finite constant differences.
This consequence corrects an earlier intentionally cautious nonclaim; it
does not retroactively change the frozen R31/R32 theorem or review inputs.

The observable algebra would be exactly the constants and its canonical
compact carrier a singleton of covering dimension0. For lambda Kahler,
the positive raw mass is M(lambda)=integral omega^n, independent of the
representative. The energy is c M(lambda), the operator is
M(lambda) delta_point, and the energy/operator family minimum auxiliary
datum is the scalar M(lambda), with no probability normalization.

For every positive epsilon and auxiliary omega_epsilon, an input having
the same actual bounded psi singularity type in theta+epsilon omega_epsilon
has top nonpluripolar mass equal to that of P+epsilon omega_epsilon. Since
all actual degree>=1 products of P vanish, the latter mass is exactly
epsilon^n integral omega_epsilon^n. Its observable carrier measure is
therefore that scalar times delta_point, regardless of a supremum error
rate or uniform type-bound. If the auxiliary classes converge to a Kahler
lambda, multiplication by epsilon^(-n) gives M(lambda) delta_point.
The same statement applies to a relative top-full-mass perturbed input
with respect to P+epsilon omega_epsilon when its raw mass equality is
actually assumed. It does not construct a new scalar energy limit for
arbitrary unbounded or uncontrolled perturbed potentials: a one-point
output measure alone does not determine their potential energies.

No implication about class numerical dimension is made. The divisorial
reference example already has actual d=0 and class numerical dimension1.
For d>0 this consequence gives no intrinsic complex geometric carrier or
finite covering-dimension theorem. All new claims remain to be checked.


# Complete independently reconstructed preceding proofs and source units

Prior verdicts are not mathematical premises; reconstruct every indispensable application.

# P15.1: minimum auxiliary references on a common genuine finite-energy domain

Authoritative single-worker research draft, 4 October 2026. Status: partial; original atom remains open.

# n1. Foundations and reconstruction of the bounded prescribed-type primitive

This is an unverified mathematical draft addressing only P15.1. No prior review verdict or prior note is a hypothesis. The bounded construction is reconstructed here because it is indispensable to the new results in n2 and n3; reconstruction alone is not claimed as substantive progress on the original atom.

Let X be a connected smooth compact Kähler manifold of complex dimension n>=1. In formulas we use
\[
d^c=\frac{i}{4\pi}(\bar\partial-\partial),\qquad dd^c=\frac{i}{2\pi}\partial\bar\partial.
\]
Fix a pseudoeffective class alpha with volume zero, a smooth closed real representative theta, and an actual theta-psh psi not identically minus infinity. Put P=T_psi and T_u=theta+dd^c u. The retained type is the two-sided, extended-valued comparison
\[
\mathcal C_\psi=\{u\in\operatorname{PSH}(X,\theta):\psi-C\leq u\leq\psi+C
\text{ for some }C<\infty\}.
\]
The polar loci of these potentials agree. Differences on polar sets can be set arbitrarily when integrated against nonpluripolar measures. The empty current product is 1.

## Exact external foundations and applicability

**B (nonpluripolar products).** Boucksom--Eyssidieux--Guedj--Zeriahi, *Monge--Ampère equations in big cohomology classes*, Acta Math. 205 (2010), 199--262, arXiv:0812.3674v2, Definition 1.1, Propositions 1.4 and 1.6, and Theorem 1.8: on compact Kähler X the nonpluripolar product of k<=n closed positive (1,1) currents is finite, positive and closed, symmetric, multilinear under sums of positive currents, and plurifinely local. Its coefficient measures, equivalently its trace measures, do not charge pluripolar sets. Smooth positive factors are ordinary wedge factors. These statements concern actual currents. All factors used below are closed positive actual currents on compact Kähler X. No multilinearity of the positive product of classes is inferred.

**D (scalar mixed mass theorems).** Darvas--Di Nezza--Lu, *Monotonicity of nonpluripolar products and complex Monge--Ampère equations with prescribed singularity*, Anal. PDE 11 (2018), 2049--2087, Proposition 2.1 and Theorem 2.4: if theta_j are n smooth closed real (1,1) forms with pseudoeffective classes and u_j,v_j are theta_j-psh, equal bounded singularity types in every slot imply equal integrals of the top mixed products. If u_j is less singular than v_j in every slot, the u-product integral is at least the v-product integral. These statements explicitly include pseudoeffective classes and impose neither bigness nor a small-unbounded-locus condition. In each application to k current slots the other n-k slots are the indicated smooth Kähler forms with zero potentials; those classes are Kähler and hence pseudoeffective. DDNL's operator is i partial bar-partial; potentials u/(2 pi) represent the same currents in that convention. Positive rescaling preserves all singularity comparisons.

**V (boundary volume).** BEGZ Sections 1.3--1.4 and Definition 1.17: a big class admits minimal-singularity potentials, less singular than any potential in that class; its volume is their top nonpluripolar mass. For pseudoeffective alpha the positive product and volume are the decreasing limits along addition of any Kähler class. Thus vol(alpha+epsilon lambda) tends to vol(alpha) as epsilon decreases to zero. For nef classes the positive product is the ordinary cup product. D bounds the mass of any actual positive current in a big class by the minimal-singularity mass. We use only this bound and the boundary limit, never equality of arbitrary actual mass with class volume.

**I (bounded admissible integration by parts).** D.-V. Vu, *Convexity of the class of currents with finite relative energy*, arXiv:2005.13241v3 (25 March 2022), Section 2, Lemmas 2.5--2.6, Theorem 2.7, with Proposition 2.1(iii): if R is closed positive of bidegree (n-1,n-1), and a,b are bounded R-admissible dsh functions, then the finite intrinsic Dirichlet products are defined, the diagonal one is positive, and
\[
\int b\langle dd^ca\mathbin{\dot\wedge}R\rangle
=\int a\langle dd^cb\mathbin{\dot\wedge}R\rangle
=-\int\langle db\wedge d^ca\mathbin{\dot\wedge}R\rangle.\tag{I}
\]
Here a dsh function is a difference of quasi-psh functions, and R-admissibility means that its two representation poles have zero R trace mass. For R formed from ordinary nonpluripolar factors times smooth positive factors, iterated relative products give exactly the signed difference of the two ordinary products with the varying slot inserted. A smooth R also has no polar mass. Accordingly all bounded differences and smooth test functions in our uses are admissible. Smooth functions are dsh by adding a sufficiently large common Kähler background to their Hessians. Finiteness of signed products follows from B. No unbounded IBP is used.

Vu uses dd^c_V=i partial bar-partial/pi, twice our operator, as directly checked on the supplied page-4 image of arXiv:2004.11111v1. Source potentials u/2 represent our currents. Source gradient d(a/2) wedge d^c_V(a/2) is one half of our gradient; multiply source IBP by 2 to obtain (I). The intrinsic square identity is
\[
da\wedge d^ca\wedge R=\tfrac12dd^c(a^2)\wedge R-a\,dd^ca\wedge R.\tag{G}
\]
The source v3 Equation (2.3) has this factor, whereas its repeated page-6 and page-11 formulas omit it. Those defects remain literal in the annex. We use (G). For local nonnegative bounded psh A,B representing a=A-B the correct square coefficients are 1,1,-1/2:
\[
dd^c A^2R+dd^c B^2R-\tfrac12dd^c(A+B)^2R-a(dd^cA-dd^cB)R.
\]
For completeness the zero-cutoff application in source IBP still follows with these coefficients. Take negative representations phi_1,...,phi_4 of a,b, dd^c phi_j>=-Omega, and
\[
\zeta_k=1+k^{-1}\max(\textstyle\sum_j\phi_j,-k),\quad
a_k=\max(\phi_1,-k)-\max(\phi_2,-k),
\]
and similarly b_k. The nonzero locus of zeta_k, not necessarily its closed support, lies in all four strict finite truncation loci. The differences a_k,b_k are uniformly bounded. Bounded Bedford--Taylor calculus with the intrinsic half-factor and distributional Stokes gives
\[
0\leq\int d\zeta_k\wedge d^c\zeta_k R
=-\int\zeta_k dd^c\zeta_k R
\leq \frac4k\int\Omega R,
\qquad
\int da_k\wedge d^ca_k R\leq2\|a_k\|_\infty\int\Omega R.
\]
The first inequality uses dd^c zeta_k+4 Omega/k>=0 and 0<=zeta_k<=1. The second uses dd^c max(phi_j,-k)+Omega>=0 and the equal cohomological masses of those two bounded products. Cauchy--Schwarz kills the IBP terms containing d zeta_k. On its nonzero locus locality identifies the intrinsic gradients and signed products with the truncations. The admissible gradient limits are finite by the cited lemmas; their poles, and the poles of all positive relative insertions, are uncharged. Dominated convergence and polarization give (I). This explains the precise repair needed in our applications; it does not silently alter the printed sources. The v1 Proposition 4.2 index and half-factor defects, and the printed Cauchy--Schwarz defect in v1 Theorem 3.7, are retained but those proofs are not used here.

**H (smooth dd^c lemma).** Deligne--Griffiths--Morgan--Sullivan, *Real homotopy theory of Kähler manifolds*, Invent. Math. 29 (1975), 245--274, Lemma 5.11 and Remark 5.14: a smooth form closed under d and d^c and d-exact is dd^c-exact on a compact Kähler manifold, also over the reals. Applied to a smooth real closed cohomologically zero (1,1) form, its primitive has degree zero; the (1,1) type and real part give a smooth real function, with the operator scalar adjusted. These are precisely our hypotheses when comparing representatives. Complete selected proof and preceding Kähler identities from the supplied Stony Brook author-hosted copy are in the annex; no source-status verdict is assumed.

**F (relative full mass and weighted convexity).** Vu v3 Section 3 defines E_P(R) for tuples (S_1,...,S_k) in the respective reference classes, more singular than (P_1,...,P_k), by equality of cohomology classes of their R-relative nonpluripolar products. For chi convex increasing on R with chi(-infinity)=-infinity, the joint chi-energy is the sum over all subsets J of
\[
\int -\chi\!\left(\sum_{j=1}^k(u_j-\varphi_j)\right)
\left\langle\prod_{j\in J}S_j\prod_{j\notin J}P_j\mathbin{\dot\wedge}R\right\rangle.
\]
Theorem 3.4 says that the diagonal full-mass and diagonal weighted classes are convex. Corollary 3.2 says the weighted class is unchanged under a cohomologous bounded-equivalent change of the common reference P. The printed proofs refer to prior arguments; we use these as precisely scoped literature theorems, not as newly reconstructed results. Our applications have k=d>=1, all P_j=P, smooth closed positive R=omega^(n-d), and chi(t)=t. The product is top-degree. On connected compact X its cohomology equality is exactly scalar mass equality because integration identifies H^(2n)(X,R) with R. Source differences are halved, so source joint linear energy is
\[
\frac d2\sum_{a=0}^d\binom da
\int(\psi-u)\langle T_u^aP^{d-a}\rangle\omega^{n-d}
\]
after normalizing u<=psi and source potentials negative. The positive factor does not affect finiteness. We never apply this k>=1 source statement with k=0.

**C (capacity and bounded weighted convergence).** Guedj--Zeriahi, *Intrinsic capacities on compact Kähler manifolds*, J. Geom. Anal. 15 (2005), 607--639: for a Kähler background Omega, Proposition 3.6 bounds the capacity of a negative Omega-psh sublevel {f<-A} by a constant times (||f||_(L1)+n int Omega^n)/A. Proposition 3.7 gives capacity convergence for decreasing **bounded** Omega-psh potentials with bounded limit. Corollary 3.8 gives quasicontinuity; Proposition 3.10 compares local Bedford--Taylor and global Kähler capacities on a finite relatively compact chart cover. DDNL Proposition 2.2 states that uniformly bounded local psh factors converging in capacity in all n slots, with uniformly bounded quasicontinuous weights converging in capacity, have weakly convergent weighted Bedford--Taylor top products. All local applications below first truncate every product factor and insert the fixed smooth Kähler factors to reach n slots.

We spell out the general decreasing-capacity deduction needed later. If f_j decreases to a nontrivial quasi-psh f in a common smooth lower-Hessian background, choose a dominating Kähler Omega and subtract a common upper-bound constant. The bounded truncations max(f_j,-A) decrease to max(f,-A), so Proposition 3.7 applies. Outside {f<=-A}, truncations and originals agree. Proposition 3.6, with for example {f<-A+1}, bounds the discarded set by O(1/A). First send j to infinity and then A to infinity. This proves general decreasing capacity convergence. It is a deduction using bounded Proposition 3.7 and the sublevel estimate, not the false attribution of unbounded hypotheses to that proposition. Proposition 3.10 and Corollary 3.8 justify the local capacity/quasicontinuity uses.

**L (comparison-set locality with correct scope).** Vu v3 Theorem 3.3: if product factors are bounded local psh functions, equal on W=intersection {v_j>v'_j}, where the comparison potentials v_j,v'_j may be unbounded psh, their products relative to a fixed positive current agree on W. To use this with unbounded nonpluripolar factors below, first truncate every local product potential at -k. On W intersected with all original and replacement product potentials >-k, the bounded factors agree. Theorem 3.3 applies, adding these strict comparisons to W. B's defining finite-locus restrictions identify the bounded products with the nonpluripolar ones there. Exhaust the simultaneous finite loci; the remaining poles have zero mass. This proves exactly the comparison-set locality we use, without granting an unbounded-factor version of Theorem 3.3. For d=0 locality is simply equality of the fixed smooth measure.

## Degree, scalar masses and mixed vanishing

For a Kähler form omega define
\[
M_k(\psi,[\omega])=\int\langle P^k\rangle\omega^{n-k},\quad
d=\max\{k:M_k>0\},\quad m=n-d.
\]
M_0=int omega^n>0. If omega' is Kähler, c omega<=omega'<=C omega for positive constants. Telescoping the differences of the positive powers gives
\[
c^{n-k}M_k(\psi,[\omega])\leq M_k(\psi,[\omega'])
\leq C^{n-k}M_k(\psi,[\omega]).
\]
This applies to every positive product current; hence d is independent of the form. Since P+epsilon omega>=epsilon omega its class is big, and B,D,V give
\[
0\leq\sum_{k=0}^n\binom nk\varepsilon^{n-k}M_k
=\int\langle(P+\varepsilon\omega)^n\rangle
\leq\operatorname{vol}(\alpha+\varepsilon[\omega])\longrightarrow0.
\]
Thus M_n=0 and d<n. D, filled with n-k smooth slots, says that every k-fold mixed product from C_psi has trace mass M_k. If the factors are merely more singular than psi, its mass is at most M_k. For k>d this proves vanishing as a current: a positive current with zero strictly positive trace mass has all coefficient measures zero, since their absolute values are locally bounded by a fixed multiple of its trace. For bounded-equivalent anchors all M_k and d agree by D. Closedness from B and distributional Stokes imply that M_k depends only on the auxiliary class and is a homogeneous polynomial of degree n-k. None of these degrees is asserted to be class numerical dimension.

## Bounded energy, cocycle and representative independence: full reconstruction

Fix a smooth complementary product W=omega_1...omega_(n-q) of Kähler forms and 0<=q<=n. On the convex hull of finitely many bounded-type potentials u_0,...,u_N, put h_i=u_i-u_0 and u_t=u_0+sum t_i h_i. The coefficient integrals in
\[
A_i(t)=\int h_i\langle T_{u_t}^q\rangle W
\]
are finite because h_i is bounded and B gives finite uncharged measures. Multilinearity makes A_i a polynomial on the simplex. For q>=1, signed differentiation in a current slot and I, with R=<T_(u_t)^(q-1)>W of bidegree (n-1,n-1), give
\[
\partial_j A_i=q\int h_i\langle dd^ch_j\mathbin{\dot\wedge}R\rangle
=q\int h_j\langle dd^ch_i\mathbin{\dot\wedge}R\rangle
=\partial_i A_j.
\]
R is smooth if q=1 and otherwise nonpluripolar, so the bounded differences are admissible. For q=0 all A_i are constant. Ordinary Stokes for this closed polynomial one-form on each finite triangle gives the cocycle for its segment integrals. Polynomial extension and continuity include simplex boundaries. The binomial expansion and beta integral give the segment value
\[
E^q_{v,W}(u)=\int_0^1\int(u-v)
\langle((1-t)T_v+tT_u)^q\rangle W\,dt
=\frac1{q+1}\sum_{a=0}^q\int(u-v)\langle T_u^aT_v^{q-a}\rangle W.\tag{1}
\]
Indeed $\binom qa\int_0^1 t^a(1-t)^{q-a}dt=1/(q+1)$. At q=d and W=omega^m write E_(psi,lambda)(u), lambda=[omega]. The triangle identity proves
\[
E_{\psi,\lambda}(u)-E_{\psi,\lambda}(v)=E_{v,\lambda}(u).\tag{2}
\]
Along a segment $u_t=u+t h$ the derivative is $\int h\langle T_{u_t}^d\rangle\omega^m$. Its second derivative for d>=1 is
\[
-d\int\langle dh\wedge d^ch\mathbin{\dot\wedge}
(\langle T_{u_t}^{d-1}\rangle\omega^m)\rangle\leq0.
\]
This uses the positive intrinsic diagonal in I. For d=0 energy is affine. Positivity of the first derivative for nonnegative directions proves monotonicity. D supplies every same-type mixed degree-d mass M_d, so constants give c M_d and pointwise sandwiches give the M_d Lipschitz estimate in bounded differences. These derivative claims are only for segments and finite-dimensional hulls.

If one Kähler factor in W=omega_1...omega_m changes by dd^c g within its class, H supplies smooth real g. For each Q=<T_u^a P^(d-a)> set R=Q times the other m-1 factors. Its bidegree is (n-1,n-1), it is closed positive and has no polar mass. The bounded h=u-psi and g are admissible. I gives
\[
\int h\,dd^cg\,R
=\int g\langle dd^ch\mathbin{\dot\wedge}R\rangle=0.\tag{3}
\]
The signed insertion is $(\langle T_u^{a+1}P^{d-a}\rangle-\langle T_u^a P^{d-a+1}\rangle)$ times the other factors. Both (d+1)-fold products vanish. This also works at d=0, where R is smooth and both one-fold nonpluripolar products vanish. Thus the bounded energy integral with m mixed Kähler factors is representative independent in every slot. It is symmetric multilinear in their classes. Decompose an arbitrary smooth closed real (1,1) form eta as (eta+A Omega)-A Omega, both Kähler for large A. This extends the integral multilinearly to arbitrary factors. Changing a representative inserts dd^c g; expanding the remaining differences of Kähler factors reduces to (3). Hence the extension is well-defined, independent of temporary decompositions, representatives and bases. Its diagonal is a homogeneous degree-m polynomial in V=H^(1,1)(X,R).

Simultaneously replacing theta by theta+dd^c g and (u,psi) by (u-g,psi-g) preserves all currents and differences. This proves gauge invariance; a bounded-equivalent anchor change has (2), not absolute anchor independence.

## Checked bounded perturbation prescription

For u in C_psi and epsilon>0, the relative unnormalized top energy in theta+epsilon omega has the exact expansion
\[
E^{n,\varepsilon,\omega}_\psi(u)
=\sum_{k=0}^d\binom nk\varepsilon^{n-k}E^k_{\psi,\omega^{n-k}}(u).\tag{4}
\]
One can expand (1) at degree n along the positive segment; the coefficient of its k-fold current mixed term is binom(n,k)/(k+1). Equivalently
\[
\sum_{j=0}^n\binom ja\binom{n-j}{k-a}=\binom{n+1}{k+1},
\]
by counting a (k+1)-subset of {0,...,n} by the location j of its (a+1)-st element. Invalid binomial indices mean zero. High-degree terms vanish by the preceding proof. Each lower coefficient is bounded by $\|u-\psi\|_\infty M_k$. The actual perturbed anchor mass is sum_(k<=d) binom(n,k)epsilon^(n-k)M_k, without equality to class volume being assumed.

If [omega_epsilon] tends to a Kähler lambda, the cohomological M_k polynomials are bounded. The degree-d energy polynomial is continuous in class. Formula (4) therefore proves the leading energy limit after dividing by binom(n,d)epsilon^m, for this fixed bounded-type u. Moving perturbed psh potentials of the same type, uniformly within delta_epsilon of u with delta_epsilon->0, have energy error at most delta_epsilon times the actual anchor mass: apply the positive-background cocycle and monotonicity already proved at arbitrary q=n. This gives the same limit even without representative bounds. No division by vol(alpha)=0 occurs, and the lower coefficients themselves need not be representative independent. This bounded statement will not be extended to uncontrolled moving forms for unbounded potentials.

Support: none. Full source bodies, hashes, inputs and rerun evidence are supplied in the assembled P15.1-argument.md and local audit artifacts. This note's analytic claims use the exactly stated external theorems, not their prior review status.


# n2. One full-mass domain and one genuine finite-energy domain for all auxiliary forms

This note uses n1, including its exactly scoped literature foundations B,D,F,C,L,I,H and reconstructed bounded energy. It proves the proposed common-domain statements and reconstructs the finite-energy extension required for n3. These are partial results for P15.1; the actual anchor type remains fixed.

## The common full-mass domain: scalar proof in every mixed slot

Set m=n-d>=1 and
\[
\mathcal E_\psi(\omega)=\left\{u\in\operatorname{PSH}(X,\theta):u\leq\psi+C,
\ \int\langle T_u^d\rangle\omega^m=\int\langle P^d\rangle\omega^m\right\}.
\]
Assume first d>=1 and that the equality holds for omega_0. Given any Kähler omega_1, compactness allows a constant A>0 for which D_0=A omega_0-omega_1 is itself a smooth Kähler form: choose A above the maximum eigenvalue of omega_1 relative to omega_0. For 0<=j<=m put
\[
\Delta_j=\int\big(\langle P^d\rangle-\langle T_u^d\rangle\big)
\omega_1^j D_0^{m-j}.
\]
These are scalar quantities, not claimed positive currents. Apply DDNL Theorem 2.4 with n slots: d copies of background theta and potentials psi versus u; j copies of background omega_1, with potential zero on both sides; and m-j copies of background D_0, also with potential zero. Every background class is pseudoeffective, each potential is psh in that background, and u<=psi+C means psi is less singular in the varying slots. The smooth slots have equal types. Consequently every Delta_j>=0. Ordinary smooth expansion gives
\[
0=A^m\int(\langle P^d\rangle-\langle T_u^d\rangle)\omega_0^m
=\sum_{j=0}^m\binom mj\Delta_j.
\]
All coefficients are strictly positive; hence every Delta_j=0, in particular Delta_m=0. Reversing the roles gives equality of the domains. If d=0 both products are 1, each Delta_j is identically zero, and full mass is automatic. Thus a single domain E_psi works for every smooth Kähler form and every auxiliary Kähler class. This proves the unverified proposal without presuming positivity of a current difference.

This also gives mixed complementary equalities. If omega_1,...,omega_m are arbitrary Kähler forms, apply the just proved equality to omega(t)=sum t_i omega_i for all t_i>0. Both sides are polynomials in t. Equality on the nonempty open orthant implies equality of every coefficient, including the coefficient of t_1...t_m. Therefore
\[
\int\langle T_u^d\rangle\omega_1\cdots\omega_m
=\int\langle P^d\rangle\omega_1\cdots\omega_m.\tag{5}
\]
Only ordinary smooth-factor polynomial algebra is used here.

## Common finite-energy domain and exact agreement with joint linear energy

Define F^1_psi by u in E_psi and, for one Kähler omega,
\[
\sum_{a=0}^d\binom da\int|u-\psi|
\langle T_u^aP^{d-a}\rangle\omega^m<\infty.\tag{6}
\]
For d=0 (6) means int |u-psi| omega^n<infinity. Quasi-psh functions are locally integrable against smooth volume; a finite chart cover gives this integral for every such u,psi. Thus in this case F^1_psi=E_psi, with no application of Vu's k>=1 weighted theorem.

For any fixed omega_0,omega_1, choose c,C>0 with c omega_0<=omega_1<=C omega_0. Telescoping positive powers gives inequalities of complementary positive forms, and wedging each positive mixed d-current yields inequalities of measures
\[
c^m\langle T_u^aP^{d-a}\rangle\omega_0^m
\leq\langle T_u^aP^{d-a}\rangle\omega_1^m
\leq C^m\langle T_u^aP^{d-a}\rangle\omega_0^m.
\]
Integrate the nonnegative weight |u-psi|. Finiteness of each term is therefore equivalent for the two forms; common full mass was proved above. Hence F^1_psi is genuinely independent of the auxiliary class and representative, not merely independent within one class. A product of any m fixed Kähler forms is bounded above and below by positive multiples of omega_0^m by the same factorwise comparison, so all the corresponding mixed complementary weighted integrals are finite as well.

Constants cause no problem: they do not change currents, and every mixed mass is finite, bounded by the reference mass by D. Thus (6) is invariant under shifting u or psi by finite constants. Normalize u<=psi and both source potentials negative. For d>=1, specialization of Vu's Definition (3.1) with k=d, diagonal S=T_u, common P and linear chi(t)=t gives exactly
\[
\frac d2\sum_{a=0}^d\binom da\int(\psi-u)
\langle T_u^aP^{d-a}\rangle\omega^m.
\]
The factor 1/2 is the checked source-potential convention. All summands are nonnegative and their finitely many coefficients are positive, so finiteness is exactly (6), also exactly the unweighted sum's finiteness. Source full mass is top-cohomology equality and hence exactly the scalar equality in E_psi. The source's diagonal joint linear class and our F^1_psi therefore agree precisely after normalization. Vu Theorem 3.4 applies with smooth R=omega^m and chi(t)=t; it gives convexity of both common domains. For d=0 convexity follows directly from the more-singular comparison and smooth-volume integrability.

## Mixed full mass and mixed weighted integrability on the whole domain

For a finite family u_1,...,u_N in E_psi, subtract constants to make each <=psi and put w=(u_1+...+u_N)/N. At d>=1 source full-mass convexity makes w full mass. By B, the mass of <T_w^d> omega^m is the average of the N^d ordered mixed masses. Each is at most M_d by DDNL Theorem 2.4, using d theta slots (psi versus the chosen u_i in each) and m identical smooth omega slots. They are nonnegative, and their average equals M_d. Each must equal M_d. This proves every d-fold mixed mass from the family, with repetitions, for every omega. Polynomial extraction as in (5) proves the same equality with any m mixed complementary Kähler factors. d=0 has the fixed empty current product and is immediate. Adding back constants does not change these masses. In particular all mixed reference/current masses used in the following arguments have exactly the specified raw reference mass.

If the family lies in F^1_psi, weighted convexity also puts w in F^1_psi. The term a=d of its energy says int (psi-w)<T_w^d> omega^m<infinity. Its positive expansion has finitely many terms, so psi-w is integrable against every ordered product from that expansion. Since
\[
0\leq\psi-u_i\leq N(\psi-w),
\]
psi-u_i is integrable against every d-fold mixed product formed from the family. In particular |u_i-u_j| is integrable against all of them. Mixed smooth complementary factors are controlled by the preceding pointwise comparison. For d=0 local L1 integrability against smooth volume proves everything directly. Adding constants preserves finiteness by the mixed mass equalities. These arguments include psi and all bounded-type anchors as members of the finite family. Higher-degree mixed products of more-singular factors vanish by n1's checked scalar DDNL application; no lower-degree weighted integrability is concluded.

## Exact truncation identity and the finite-energy meaning

For normalized u<=psi in E_psi, set z=psi-u>=0 off the poles, u_L=max(u,psi-L), L>0, and
\[
\mu_a=\langle T_u^aP^{d-a}\rangle\omega^m,\qquad
\mu_{a,L}=\langle T_{u_L}^aP^{d-a}\rangle\omega^m.
\]
The maximum is theta-psh by the local maximum property; psi-L<=u_L<=psi, so u_L is in C_psi. Both measures have mass M_d by the preceding mixed full-mass proof (or by D's sandwich between u and psi). On the strict comparison set G_L={u>psi-L}, they agree by n1's fully checked finite-locus use of L and B. Explicitly local potentials rho+u and rho+psi-L are psh comparison potentials; product factors are first replaced by bounded local truncations, the simultaneous finite loci are exhausted, and only then are the nonpluripolar restrictions identified. Poles have zero mass, including when d=0. No unbounded product factors are put into the printed bounded-factor theorem.

On B_L=X minus G_L, outside the uncharged poles, u_L-psi=-L. Equality of total masses and equality on G_L imply mu_(a,L)(B_L)=mu_a(B_L). Thus even without finite energy,
\[
\int(\psi-u_L)d\mu_{a,L}
=\int_{G_L}z\,d\mu_a+L\mu_a(B_L)
=\int\min(z,L)d\mu_a.\tag{7}
\]
The boundary {u=psi-L} is included in B_L and its weight is exactly L; locality is used only on the strict set. The argument works verbatim with a fixed mixed complementary product W and its common mass from (5).

For u in F^1_psi define the finite real energy
\[
E_{\psi,\lambda}(u)=\frac1{d+1}\sum_{a=0}^d
\int(u-\psi)\langle T_u^aP^{d-a}\rangle\omega^m,\quad\omega\in\lambda.\tag{8}
\]
Monotone convergence in (7) proves
\[
E_{\psi,\lambda}(u_L)\downarrow E_{\psi,\lambda}(u).\tag{9}
\]
It also proves the precise converse: on the full-mass domain, finiteness of the decreasing bounded truncation-energy limit is equivalent to (6). Indeed the negative of that limit is the sum of the nonnegative integrals int z dmu_a divided by d+1; a finite sum is finite exactly when every term is finite, equivalently when its positive binomial-weighted sum is finite. For d=0 this is the ordinary smooth L1 formula. Thus this is a genuine F^1 domain defined equally by a finite energy value, not an arbitrary renaming of a weighted class.

Monotonicity follows by ordering the truncations and using the bounded result. Every mixed mass in (8) is M_d, so
\[
E_{\psi,\lambda}(u+c)=E_{\psi,\lambda}(u)+cM_d.\tag{10}
\]
For a general u<=psi+C use v=u-C: u_L=v_(L+C)+C for large L. Equation (10) and normalized (9) give (9) for general u. The same argument applies to mixed complementary W. No choice of real truncation levels tending to infinity changes the limit.

## Bounded decreasing continuity with an unbounded reference: complete tail proof

Suppose v_j decreases to v and all are uniformly bounded relative to psi: |v_j-psi|,|v-psi|<=B. For a fixed degree-q product formed from v_j and psi and fixed n-q smooth Kähler factors, denote the positive measures by nu_j,nu. D gives exactly the same total mass b for all of them. Shift psi to be negative and put
\[
\eta_A=\min(1,\max(\psi+A,0)).
\]
The nonzero locus {psi>-A} contains all places where this cutoff is used. Its closed support may meet the boundary; we do not claim otherwise. On a relatively compact chart with theta=dd^c rho, every local psh rho+v_j,rho+v,rho+psi on this nonzero locus has a uniform lower bound depending on A,B,rho, and a uniform upper bound because v_j<=v_1. Truncate all these local psh factors below a still lower constant. The resulting factors are uniformly bounded psh, converge in capacity by n1's C deduction, and give the same products wherever eta_A is nonzero. The fixed smooth factors have bounded smooth local psh potentials as well.

The cutoff can be expressed using the bounded truncation of psi and smooth rho. Similarly eta_A(v_j-psi) equals eta_A times the difference of the bounded local psh truncations just chosen. Such weights are uniformly bounded quasicontinuous functions converging in capacity: max, min and products on bounded ranges preserve capacity convergence by their elementary Lipschitz estimates and a union bound on exceptional sets. A smooth partition of unity is an additional fixed bounded continuous weight. DDNL Proposition 2.2 therefore proves local, and then global, convergence of
\[
\int\eta_A d\nu_j\ \text{ and }\ \int\eta_A(v_j-\psi)d\nu_j
\]
to their limiting counterparts for every fixed A. Bounded-factor hypotheses hold in every product slot. This is not a direct application of a big-class convergence theorem in the pseudoeffective background.

The tail weight is bounded by B. Hence its absolute integral is at most
\[
B\left(b-\int\eta_A d\nu_j\right).
\]
First let j tend to infinity at fixed A; then let A tend to infinity. The limiting tail mass tends to zero because nu gives no mass to psi's polar set. This proves convergence of every full weighted integral and hence bounded decreasing energy continuity. For q=0 the same conclusion follows by dominated convergence against smooth volume; the cutoff argument also applies with no varying product factors.

## Decreasing continuity, concavity and the unbounded cocycle

Let v_j decrease to u with v_j,u in F^1_psi. They have one upper bound psi+C because v_1 does. Monotonicity gives
\[
E(u)\leq E(v_j)\leq E(\max(v_j,\psi-L)).
\]
For fixed L the right-hand sequence decreases to u_L within a uniform bounded type, so the lemma proves limsup E(v_j)<=E(u_L). Sending L to infinity using (9) proves E(v_j)->E(u). This includes every decreasing bounded-type approximation with limit in F^1_psi. If w=(1-t)u+t v, source weighted convexity puts w in the domain. The bounded-type sequence (1-t)u_L+t v_L decreases to w; bounded concavity, (9) and decreasing continuity prove concavity on the entire domain. At d=0 it is directly affine.

For normalized u,v<=psi take simultaneous truncations, nu_a=<T_u^a T_v^(d-a)>omega^m and nu_(a,L)=<T_(u_L)^a T_(v_L)^(d-a)>omega^m. They have mass M_d and agree on G_L={u>psi-L} intersection {v>psi-L} by the finite-locus comparison proof. Their complementary masses therefore agree. On B_L their truncated weight |u_L-v_L|<=L, and with z_u=psi-u,z_v=psi-v,
\[
L\nu_{a,L}(B_L)=L\nu_a(B_L)
\leq\int_{B_L}(z_u+z_v)d\nu_a\longrightarrow0.
\]
The last limit is dominated convergence using the proved mixed weighted integrability; B_L decreases to uncharged polar sets. The original |u-v| tail also tends to zero. On G_L products and weights agree. Thus
\[
\frac1{d+1}\sum_a\int(u_L-v_L)d\nu_{a,L}
\longrightarrow\frac1{d+1}\sum_a\int(u-v)d\nu_a.
\]
Taking limits in the reconstructed bounded cocycle yields the finite unbounded formula
\[
E_{\psi,\lambda}(u)-E_{\psi,\lambda}(v)
=E_{v,\lambda}(u)
:=\frac1{d+1}\sum_{a=0}^d\int(u-v)\langle T_u^aT_v^{d-a}\rangle\omega^m.\tag{11}
\]
Constants reduce the general case to this normalization: products do not change and every mixed mass is M_d. For d=0 this is the linear smooth-volume identity.

## Anchors, representatives and theta gauge

Let chi in C_psi. The more-singular relations to psi and chi are identical up to constants, and bounded mixed mass equality gives their identical reference mass and degree. Thus their full-mass domains agree for all forms. Every chi belongs to F^1_psi because its differences are bounded. For u in F^1_psi, the mixed-family integrability proof applied to (u,chi,psi) shows that |u-chi|<=|u-psi|+||psi-chi||_infinity is integrable against every product <T_u^a T_chi^(d-a)>omega^m. Hence u is in F^1_chi. Applying the same argument with the roles reversed proves equality of finite-energy domains. This is a direct anchor-domain proof, consistent with Vu Corollary 3.2, and does not depend on an unbounded IBP assertion.

Taking v=chi in (11) gives exactly
\[
E_{\chi,\lambda}(u)=E_{\psi,\lambda}(u)-E_{\psi,\lambda}(\chi).\tag{12}
\]
The mixed-integral definition with anchor chi is the displayed E_v; all terms have just been proved finite. At d=0 smooth L1 integrability proves the same facts without source weighted theorems.

For cohomologous Kähler representatives omega,omega', the domain is already common. Each u_L bounded energy is representative independent by n1. Equation (9), valid for both forms, proves representative independence of the whole finite-energy value. Simultaneous smooth theta gauge changes leave actual currents, relative differences, comparisons and truncations invariant, so all constructions are unchanged.

## A genuinely unbounded member

On $X=\mathbb P^1\times\mathbb P^1$ take normalized Fubini--Study $\kappa$ with $\int\kappa=1$, $\theta=p_1^*\kappa$, $\psi=0$ and $\omega=p_1^*\kappa+p_2^*\kappa$. The smooth semipositive theta makes its class nef; its square is zero, so B,V give volume zero. The actual degree is d=1 and M_1=1. Choose 0<a<1/2 and in a small disk at zero set
\[
v(z)=-b(-\log|z|)^a
\]
near zero. Continue by a smooth cutoff on a fixed annulus. On the punctured inner disk the radial second derivative with respect to t=log|z| is b a(1-a)(-t)^(a-2)>0. The annular negative Hessian is bounded by a constant times b, so small b>0 ensures S=kappa+dd^c v>=0 globally. Define v(0)=-infinity and subtract a constant to make v<=0. The locally integrable subharmonic extension has no atom at zero: its outward radial flux is proportional to b a(-log r)^(a-1), tending to zero. Distributional Stokes gives S(X)=1, and no mass is lost in its nonpluripolar part. It is smooth off zero.

Smooth-volume integrability follows from exponential area decay in s=-log r. Its weighted singular-current integral is a positive constant times
\[
\int^\infty s^a s^{a-2}ds=\int^\infty s^{2a-2}ds<\infty.
\]
Thus $u=p_1^*v$ has full degree-one mass and both finite weighted terms in (6), but u-psi is unbounded. The construction is an example demonstrating genuine extension; no fibration hypothesis appears in the general theorem. This analytic proof, not a numerical test, establishes the example.

Support: n1. These results remove the auxiliary dependence of the full-mass and finite-energy domains. They supply no unrestricted unbounded moving-auxiliary perturbation limit.


# n3. Coefficientwise extension and the minimum reference for the entire energy family

This note uses n1 and n2. It proves the coefficientwise unbounded extension and the exact necessary/sufficient finite-dimensional reference criterion in proposals 1--3. The minimum is for this specified anchored prescribed-type energy family. It is not an independent geometric classification or a claim that P15.1 is closed.

## Intrinsic bounded functionals and an unisolvent Kähler set

Let V=H^(1,1)(X,R), with its real Bott--Chern/de Rham interpretation on compact Kähler X, and B=Sym^m V, m=n-d>=1. V is finite-dimensional as a subspace of finite-dimensional de Rham cohomology; H identifies cohomologically equal smooth (1,1) representatives by a smooth dd^c gauge. For u in C_psi, define the symmetric functional ell_u^psi in B^* by
\[
\ell_u^\psi(\lambda_1\odot\cdots\odot\lambda_m)
=\frac1{d+1}\sum_{a=0}^d\int(u-\psi)
\langle T_u^aP^{d-a}\rangle\eta_1\cdots\eta_m,\qquad[\eta_i]=\lambda_i.\tag{13}
\]
Here eta_i are arbitrary smooth closed real representatives. The extension by differences of Kähler forms and the representative-change proof in n1 prove well-definedness in all slots; no temporary basis or chosen decomposition is data. It is a symmetric m-linear form and hence defines exactly a linear functional on Sym^m V. Its diagonal polynomial p_u(lambda)=ell_u^psi(lambda^odot m) equals E_(psi,lambda)(u) on the Kähler cone.

Let h=dim V and N=dim B=binom(h+m-1,m). The tensors lambda^odot m with lambda Kähler span B. To prove this, if their span were proper, finite-dimensional duality would give a nonzero f in B^* annihilating them all. Its associated homogeneous polynomial f(lambda^odot m) would vanish on the nonempty open Kähler cone. A real polynomial vanishing on an open set is zero: in coordinates choose a small open rectangular box in that set, regard it as a polynomial in the first coordinate, and use the one-variable statement that a nonzero polynomial cannot have infinitely many roots; its coefficients vanish on the remaining box. Induct on the number of coordinates. Thus all polynomial coefficients vanish, and polarization forces f=0, a contradiction. This last implication is also explicit in the monomial basis: coefficient of x^beta is (m!/beta!)f(e_1^odot beta_1 ... e_h^odot beta_h).

Consequently there exist N Kähler classes lambda_1,...,lambda_N whose powers form a basis of B: iteratively choose a power outside the span of those already chosen. The evaluation map
\[
\mathcal A:B^*\longrightarrow\mathbb R^N,\quad
f\longmapsto(f(\lambda_i^{\odot m}))_{i=1}^N\tag{14}
\]
is a linear isomorphism. This is the promised unisolvent set. Its existence uses only openness and finite-dimensional polynomial algebra. Choosing a different such set changes coordinates, not the intrinsic functional.

## Coefficientwise convergence on the common unbounded domain

Fix u in F^1_psi and u_L=max(u,psi-L). n2 proves pointwise in every Kähler class
\[
\ell_{u_L}^\psi(\lambda^{\odot m})
=E_{\psi,\lambda}(u_L)\longrightarrow E_{\psi,\lambda}(u)\in\mathbb R.
\]
In particular the N evaluations (14) converge. Apply the fixed inverse A^(-1). It follows that ell_(u_L)^psi converges in B^*, equivalently coefficientwise in any finite basis, to one ell_u^psi. Evaluating the limit at any Kähler lambda and using the same n2 limit proves
\[
E_{\psi,\lambda}(u)=\ell_u^\psi(\lambda^{\odot m}).\tag{15}
\]
Thus the entire unbounded finite-energy value is a homogeneous degree-m class polynomial. No nonuniform lower-epsilon coefficients enter this argument. For any other unisolvent set or basis, the resulting functional has the same diagonal values on the Kähler cone; the open-set polynomial proof gives uniqueness. n2 also gives the same pointwise limit for every decreasing bounded-type approximation with limit u, so all such approximations give exactly this coefficient limit. Arbitrary real truncation levels tending to infinity are covered by (9).

The functionals have the explicit integral formula (13) on the unbounded domain as well. Here is a proof that also checks convergence of the mixed integrals. For a mixed product W of m Kähler representatives, n2 gives the full mass of every product <T_u^a P^(d-a)>W and its truncated counterpart, and their locality on G_L. Thus (7) holds with omega^m replaced by W. Each weight is integrable by n2, so each weighted integral for u_L converges to the integral for u. For arbitrary smooth real representatives eta_i, choose A_i large enough that eta_i+A_i Omega and A_i Omega are Kähler. Expand their product into its 2^m signed positive products W. Every weight integral is finite because W is bounded by a constant times Omega^m, and all 2^m truncation limits just proved exist. The bounded integral functionals converge to ell_u^psi coefficientwise. Taking those integral limits gives exactly (13). This also proves representative and decomposition independence for these explicit unbounded mixed integrals without using unbounded IBP. Equivalently they are obtained from (15) by the intrinsic polarization formula
\[
\ell_u^\psi(\lambda_1\odot\cdots\odot\lambda_m)
=\frac1{m!}\sum_{J\subset\{1,\ldots,m\}}(-1)^{m-|J|}
p_u\!\left(\sum_{j\in J}\lambda_j\right),\tag{16}
\]
where p_u is the unique polynomial on all V. The empty sum is 0. Formula (16) follows by expanding the polynomial and observing that the inclusion-exclusion sum kills every term missing a variable, leaving m! times the fully multilinear term. No meaning as a positive reference is assigned to a non-Kähler argument of this polynomial extension.

## No extra reference directions appear at finite energy

Define intrinsically
\[
S_\psi=\operatorname{span}\{\ell_u^\psi:u\in\mathcal C_\psi\}\subset B^*,
\quad K_\psi=\operatorname{Ann}(S_\psi)\subset B,
\quad Q_\psi=B/K_\psi,
\]
with quotient map q. Every ell_(u_L)^psi belongs to S_psi. This subspace is finite-dimensional and closed, so its coefficient limit ell_u^psi belongs to S_psi for every u in F^1_psi. Conversely C_psi is contained in F^1_psi by bounded masses and bounded weights. Therefore
\[
\operatorname{span}_{u\in\mathcal F^1_\psi}\ell_u^\psi=S_\psi,
\qquad
\bigcap_{u\in\mathcal F^1_\psi}\ker\ell_u^\psi=K_\psi.\tag{17}
\]
This equality is the substantive extension result, beyond defining a quotient on bounded potentials.

For two Kähler classes lambda_0,lambda_1, equations (15)--(17) give the exact equivalence
\[
\big[E_{\psi,\lambda_0}(u)=E_{\psi,\lambda_1}(u)
\text{ for every }u\in\mathcal F^1_\psi\big]
\quad\Longleftrightarrow\quad
q(\lambda_0^{\odot m})=q(\lambda_1^{\odot m}).\tag{18}
\]
For the forward direction restrict to bounded u; their functionals span S, so the tensor difference lies in K. For the backward direction every unbounded functional belongs to S and annihilates K. Hence the quotient criterion is both necessary and sufficient on the entire genuine domain.

## Raw mass, constants, anchor change and gauge change

Define the mass functional in B^* by
\[
\mathfrak M_\psi(\lambda_1\odot\cdots\odot\lambda_m)
=\int\langle P^d\rangle\eta_1\cdots\eta_m.
\]
Closedness of <P^d> and ordinary smooth Stokes prove representative independence. Its diagonal M_d(psi,lambda)>0 on the Kähler cone, and its mixed Kähler values are positive because the strictly positive complementary product dominates a positive multiple of a Kähler trace power of the nonzero positive current <P^d>. At d=0 the current is 1 and the same statement is the positive smooth volume integral. The mass functional is retained in S:
\[
\ell_{\psi+c}^\psi=c\mathfrak M_\psi,\qquad
\ell_{u+c}^\psi=\ell_u^\psi+c\mathfrak M_\psi.\tag{19}
\]
Indeed currents are unchanged by constants, and every degree-d mixed mass from (13) is exactly the reference mixed mass by n2. This proves (19) initially on mixed Kähler arguments and then on B by spanning/polarization. In particular psi+1 belongs to C_psi and supplies mathfrak M_psi. Thus Q retains the positive raw mass and a scale cannot be eliminated by forgetting constants. K is contained in ker mathfrak M_psi and Q has dimension at least one. There is no normalization of M_d or of zero volume to a probability.

Let chi in C_psi. n2 gives the identical domains and the scalar anchor cocycle for every Kähler lambda and every u in the domain. Unique polarization gives the functional identity on B
\[
\ell_u^\chi=\ell_u^\psi-\ell_\chi^\psi.\tag{20}
\]
Every bounded ell_u^chi lies in S_psi. Conversely ell_psi^chi=-ell_chi^psi and
ell_u^psi=ell_u^chi-ell_psi^chi, so S_chi=S_psi. Hence K_chi=K_psi and the quotient, its admissible image, and the minimum equivalence are anchor invariant within the bounded type. The origin of energy still requires an anchor, changing by (20). Mixed bounded mass equality shows mathfrak M_chi=mathfrak M_psi. This proves all anchor statements including d=0, without asserting that C_psi in that case consists only of constant translates.

A simultaneous theta gauge change theta'=theta+dd^c g, u'=u-g, psi'=psi-g, with smooth real g, preserves every actual current, difference, truncation and integral in (13). It transports C_psi and F^1_psi bijectively to the new potential domains, preserves all functionals and identifies the same S,K,Q. Any two smooth real representatives of alpha differ in this way by H. Auxiliary representative independence was proved above by bounded reconstruction and truncation, not by a gauge applied to the auxiliary paths. Adding constants to g does not change the identification of anchored differences. Keeping theta as a convenient coordinate representative is permissible; its smooth gauge is not independently necessary reference data.

## Exact universal minimum sense and admissible topology

Each ell_u descends to a linear functional bar-ell_u on Q. The map
\[
\mathcal A_{\rm all}:B\longrightarrow\mathbb R^{\mathcal F^1_\psi},
\quad t\longmapsto(\ell_u(t))_u
\]
has kernel K, by (17). It induces an injective linear map from Q onto this family's finite-dimensional output space. If r:B->R_0 is any linear reference descriptor and for every u there is a linear f_u on r(B) with ell_u=f_u composed with r, then ker r is contained in K. Thus there is one well-defined surjective linear map
\[
F:r(B)\longrightarrow Q,\qquad F(r(t))=q(t).
\]
Well-definedness is exactly ker r subset K; surjectivity follows from surjectivity of q, and uniqueness follows because r(B) is spanned by those images. This proves the coarsest linear descriptor property. It does not assert a geometric classification of K.

For actual auxiliary choices, define the admissible image
\[
\mathcal I_\psi=\{q(\lambda^{\odot m}):\lambda\text{ Kähler}\}\subset Q.
\]
Every energy is determined by this descriptor. Among arbitrary set-valued descriptors r_0 on the Kähler cone, if equality of r_0(lambda)'s implies equality of all energy values, (18) yields a uniquely defined map from r_0's image onto I_psi sending r_0(lambda) to q(lambda^odot m). Conversely the latter descriptor suffices. This is minimum informational data for this family, not a proof that this image is a manifold, a geometric carrier, or all of Q. The map lambda->q(lambda^odot m) need not be injective, and I_psi need not be a vector space.

Give Q its finite-dimensional quotient topology and I_psi the subspace topology. For fixed u every bar-ell_u is continuous; hence tau_j->tau in I implies convergence of its energy values even when the representing classes do not converge. Conversely choose bounded u_1,...,u_s whose ell's are a basis of S (s=dim Q). Then
\[
Q\longrightarrow\mathbb R^s,\quad
\tau\longmapsto(\bar\ell_{u_i}(\tau))_i
\]
is a linear isomorphism: its kernel is zero by definition of K, and both sides have dimension s. Thus convergence of these finitely many bounded energy coordinates is equivalent to quotient convergence. This provides the weakest finite-dimensional topology making the whole energy family continuous.

If u_j decreases to u with all in F^1_psi, n2 gives convergence at every unisolvent lambda_i; (14) then proves ell_(u_j)->ell_u in B^*. Accordingly their polynomials converge uniformly on every compact subset of V (bound the evaluation tensors there), and their descended functionals converge uniformly on bounded subsets of Q. If simultaneously tau_j->tau in I, the values bar-ell_(u_j)(tau_j) tend to bar-ell_u(tau), since convergent sequences of functionals and points are bounded and the evaluation pairing is continuous. These are admissible energy-polynomial/quotient statements. They make no assertion about a rescaled top energy with epsilon-dependent rough representatives, nor about variable unbounded integration weights outside the proved decreasing theory.

## Scope and a nontrivial quotient computation

The remaining reference data for this energy family are X, its complex structure and class alpha, the actual bounded comparison type (with its degree d), an anchor specifying the additive origin, and tau in I_psi. A smooth theta is only a gauge representative. The current integrals are carried by the actual n-dimensional X with product bidegree (d,d). A finite-dimensional quotient of reference tensors is not a geometric d-dimensional carrier. Actual type is not reduced to ideal equivalence or class numerical dimension.

For clarity the whole auxiliary class need not be minimal. In n2's $X=\mathbb P^1_y\times\mathbb P^1_z$ example with $\theta=p_1^*\kappa$ and psi=0, V has basis $a=[p_1^*\kappa],b=[p_2^*\kappa]$. One direct computation is the product cell decomposition of the two spheres: there are two real 2-cells, no odd cells, and the two pullback classes evaluate independently on the two fibers; hence H^2 has precisely these two generators, both of type (1,1). A real class A a+B b is Kähler exactly when A,B>0: restriction to each fiber proves necessity, and the product form proves sufficiency. Any theta-psh potential restricts on each z-fiber to a psh function or the identically-minus-infinity function. A nontrivial psh function on a compact connected curve is constant by the maximum principle. Thus all fibers are constant and u(y,z)=v(y), extended-valuedly; a nontrivial restriction to a y-slice is kappa-psh and identifies v. For bounded u in C_0 it is a bounded v. Wedge calculation gives
\[
E_{0,Aa+Bb}(p_1^*v)=\frac B2\int_{\mathbb P^1}v\big((\kappa+dd^cv)+\kappa\big).
\]
All bounded ell_u therefore lie in the span of the functional B, and constants supply that functional itself. Hence S is exactly one-dimensional, K is the A-axis, Q is R with q(Aa+Bb)=B, and I=(0,infinity). By (17) this description holds for the entire genuine F^1 domain, including n2's unbounded example. This is a concrete geometric computation in one special case, not a universal geometric kernel formula.

Support: n1, n2. The new conclusion is the common-domain, coefficientwise and minimum-family-reference theorem with exact scope, not an original-atom completion.


# n4. Analytic limitation, original residuals, and reproducible execution evidence

This note uses n1, n2 and n3. It reconstructs the supplied analytic concentration obstruction rather than treating the prior proof as a grant, and separates the substantive new theorem from the unchanged original P15.1. P15.2 and P15.3 are outside this assignment; no minimum operator-reference construction or result for those atoms is claimed.

## Same-class concentration still prevents an unrestricted unbounded perturbation theorem

Use the actual unbounded finite-energy potential $u=p_1^*v$ proved in n2 on $X=\mathbb P^1\times\mathbb P^1$, with $\theta=p_1^*\kappa$, psi=0, d=1,m=1, int kappa=1 and $v=-b(-\log|z|)^a-c$ near zero, 0<a<1/2, c>=0. Its actual current is $p_1^*S$, $S=\kappa+dd^c v$ of mass one without a pole atom. All ambient hypotheses, degree-one full mass and finite joint linear energy were proved there.

For epsilon>0 sufficiently small put rho_epsilon=exp(-epsilon^(-2/a)). Choose a smooth nonnegative area form beta_epsilon of integral one supported in {|z|<rho_epsilon}; a disk bump rescaled and normalized gives it and extension by zero is smooth. Every real 2-form on this curve is closed and of type (1,1). Set
\[
\kappa_\varepsilon=\tfrac12\kappa+\tfrac12\beta_\varepsilon,
\qquad \omega_\varepsilon=p_1^*\kappa_\varepsilon+p_2^*\kappa.
\]
These are smooth strictly positive Kähler forms. H^2(P^1,R) is one-dimensional and integration determines its class; hence [kappa_epsilon]=[kappa]. All auxiliary classes [omega_epsilon] equal the single Kähler $\lambda=[p_1^*\kappa+p_2^*\kappa]$. The potential is identical for every parameter, and T_u+epsilon omega_epsilon is positive. At each fixed parameter v is integrable against kappa_epsilon because it is locally L1 and this fixed smooth density is bounded, and against S and kappa by n2. Thus every weighted mixed top integral in the following formula is finite, with no uniform bound assumed in epsilon.

Write $A=p_1^*\kappa$, $B=p_2^*\kappa$, $A_\varepsilon=p_1^*\kappa_\varepsilon$ and $U=p_1^*S$. Products of two horizontal (1,1) factors vanish off the pole, hence their nonpluripolar extensions vanish; mixed products below give no pole mass. Ordinary smooth multiplication, or the defining nonpluripolar finite-locus restrictions, therefore gives
\[
\begin{aligned}
(T_0+\varepsilon\omega_\varepsilon)^2&=2\varepsilon(A+\varepsilon A_\varepsilon)B,\\
\langle(T_u+\varepsilon\omega_\varepsilon)(T_0+\varepsilon\omega_\varepsilon)\rangle
&=\varepsilon(U+A+2\varepsilon A_\varepsilon)B,\\
\langle(T_u+\varepsilon\omega_\varepsilon)^2\rangle
&=2\varepsilon(U+\varepsilon A_\varepsilon)B.
\end{aligned}
\]
The actual top masses of the anchor and u are both 2 epsilon(1+epsilon), so this is a full relative top-mass potential for every positive perturbation. The joint linear-weight integrals of these three measures are finite at every fixed parameter by the integrability already checked. This obstruction uses neither lost perturbed mass nor infinite energy at a fixed parameter.

Directly summing those three finite weighted terms, divided by 3, gives
\[
E^{2,\varepsilon,\omega_\varepsilon}_0(u)
=2\varepsilon E_{0,\lambda}(u)+2\varepsilon^2\int v\kappa_\varepsilon,
\qquad E_{0,\lambda}(u)=\tfrac12\int v(S+\kappa)\in\mathbb R.
\]
Consequently
\[
\frac{E^{2,\varepsilon,\omega_\varepsilon}_0(u)}{2\varepsilon}
=E_{0,\lambda}(u)+\varepsilon\int v\kappa_\varepsilon.\tag{21}
\]
On the bump's support, -v>=b epsilon^(-2), and v<=0 globally. Therefore int v kappa_epsilon<=-(b/2)epsilon^(-2), so the last term tends to minus infinity. For the fixed smooth product omega instead, the same expansion has the fixed finite integral int v kappa, and the quotient tends to E_(0,lambda)(u). These two paths have exactly the same auxiliary class, exactly the same quotient descriptor from n3, and exactly the same potential at every parameter.

This proves an analytic counterexample to extending n1's moving-representative leading-perturbation assertion to all F^1_psi without additional controls. It does not contradict n3's continuity on the energy quotient: that theorem concerns the degree-d energy polynomial, whereas (21) has an uncontrolled lower-degree weighted coefficient. A quotient reference, class convergence, and degree-d finite energy cannot provide a uniform estimate for that extra term. No positive probability normalization was used anywhere.

## Actual degree and leading class-volume coefficients must remain distinct

In the same class choose the actual logarithmic reference on the first factor
\[
g(z)=\log\frac{|z|^2}{1+|z|^2},\qquad\psi=p_1^*g.
\]
With kappa=dd^c log(1+|z|^2), int kappa=1, the distributional identity dd^c log|z|^2=delta_0 follows from the radial flux of log r^2: its Laplacian flux is 4 pi, and our dd^c is planar Laplacian times area divided by 4 pi. Thus kappa+dd^c g=delta_0, globally, and P is the integration current of the vertical divisor. Its nonpluripolar degree-one product is zero: it vanishes off the polar divisor and the defining extension puts no mass on that divisor. Hence d=0 for this actual reference, whereas the smooth reference has d=1. The nef class has nonzero first cup product and zero square, so its nef numerical dimension, defined by its largest nonzero cup-power trace, is one. Actual-current degree is therefore not class numerical dimension.

For $\omega=A p_1^*\kappa+B p_2^*\kappa$, A,B>0, actual-current multilinearity gives the perturbed divisor-reference mass
\[
\int\langle(P+\varepsilon\omega)^2\rangle
=2AB\varepsilon^2,
\]
while the nef perturbed class has volume by its cup product
\[
\operatorname{vol}(\alpha+\varepsilon[\omega])
=2B\varepsilon+2AB\varepsilon^2.
\]
Both statements follow from n1's exact volume foundation and the explicitly computed products. The exponents differ. Constant anchor shifts have actual perturbed energy c times the first mass, so rescaling by the leading class-volume exponent would discard their positive actual degree-zero scale. This explicitly checks why class-volume coefficients cannot be substituted into the scoped theorem without another proof.

## What is proved and what remains for the original atom

Proposals 1--3 are proved, with the stipulated actual-type degree and every fixed smooth Kähler auxiliary choice. The full-mass domain is independent of all auxiliary classes/forms by scalar mixed deficits. Joint linear integrability is independent by positive pointwise comparison. On their common genuine F^1 domain the energy has finite mixed integrals, exact truncation meaning, cocycle, concavity, decreasing continuity, gauge invariance and same-type anchor transformation. Its polynomial coefficients are limits of the bounded coefficients, and the unbounded energies span exactly the same finite-dimensional S. The exact reference equivalence on the entire domain is (18); raw mass survives because constants supply the mass functional. These domain and coefficient-extension statements are the substantive progress. Defining an annihilator quotient by itself is not counted as a new geometric theorem.

The construction retains a prescribed actual comparison type and uses an actual-current degree and scale. Its minimum quotient is a universal factorization for this specified family, not a theorem that this is the minimum independently geometric reference for every possible zero-volume energy theory. The carrier of its integrals is explicitly X of dimension n with current bidegree (d,d); no geometric d-dimensional carrier or universal geometric characterization of the kernel is supplied. The original catalogue's broader choice and path requirements are not thereby resolved.

In particular a direct all-F^1, class-convergent moving-representative perturbation prescription is false by (21). Alternative controls, restrictions or an iterated truncation prescription would need to be stated and proved rather than silently added to the original atom. For example the already proved iterated prescription first takes the bounded leading limit at fixed L and then L to infinity; it gives (8), but is not asserted equal to every joint or reversed limit. General moving unbounded-potential perturbation limits, sufficient weighted lower-degree control even for all fixed forms in arbitrary reference types, and infinite-dimensional path/differential calculus with unbounded velocities have not been proved. Decreasing continuity is the precise sequence theorem here; no arbitrary increasing continuity is asserted. The leading coefficient used in n1 is the actual-reference polynomial's coefficient, not a general leading class-volume coefficient. No claim on the optional d=0 rigidity question is needed or made.

Thus this is a new scoped partial theorem, not a complete solution or a counterexample to the whole original P15.1. No catalogue source-dependent published/unpublished claim, ideal-equivalence-only recovery, other worker result, literature-priority verdict, or earlier same-model review is assumed. Candidate is false.

## Execution and artifact contract

The authoritative proof is P15.1-argument.md, containing n1--n4 and all 24 complete selected primary-source LF bodies used or retained for the supplied source-defect audit. P15.1-partial.tex and its twice-compiled P15.1-partial.pdf contain the full new proof and all exactly stated foundation hypotheses/applicability checks; literal OCR annex bodies remain in Markdown. The original input.json is unchanged. Its SHA256 is 6939872a9d6907168bd4b224e7c6a964c68c7fd226eb33d05520e9774e8939a6. input-original.json is byte identical; assignment-original.txt preserves the decoded assignment exactly, and task-original.json preserves its task values. Old audits inside those preserved supplied strings are historical data, not this execution's evidence.

Source reading is confined to the supplied read-only shared source directory. verify_sources.py checks literal LF joins without an added final LF. All 24 supplied pins match, and all 24 exact bodies are identified in the supplied assignment, including the JSON-escaped DGMS/GZ units. Raw OCR/form feeds and defects remain in source-annex.md and the authoritative argument. The three source images cited in n1 were visually inspected; image hashes are recorded. No whole primary PDF was copied or modified. Published foundations remain external theorems with precisely checked applications, not proofs certified by source-hash matching.

coefficient_check.py performs exact finite rational/integer diagnostics for the subset coefficient identity, homogeneous polynomial interpolation/polarization, and a synthetic scalar-deficit expansion. Observed checks passed 2,925 coefficient cases (all 0<=n<=24, 0<=a<=k<=n), 40 interpolation cases, 8 polarization cases and 12 positive-expansion cases. These diagnostics illustrate the finite algebra, not analytic correctness. The general algebra proofs are in n1 and n3; the positivity and analytic domain proofs are in n2. build.py assembles the proof and canonical notes, generates standalone TeX with Pandoc, compiles it twice, extracts PDF text and records commands, return codes, versions, hashes and structure checks. Two successful pdflatex passes and all six extracted-PDF structure checks were observed. The environment was Python 3.12.14, Pandoc 3.1.11.1, pdfTeX 1.40.26 (TeX Live 2025/dev/Debian), Poppler 25.03.0 on Linux 6.18.44. A rendering defect from raw prose superscript/star notation was corrected by explicit inline math and disabling Markdown prose superscripts; the initial compiled output and logs are retained as rendering diagnostics. A read-only git-status probe reported that this fresh directory is not a Git repository; no Git mutation was attempted. A successful build is not mathematical certification. research-audit.json records the claimed scope and nonclaims; author-audit.json records this single-worker reconstruction and configuration limitations. status.json has exactly id,status,exact_result,proof_file,concrete_gaps. notes.json is the canonical native note object and has candidate=false, with only earlier local IDs as support.

Rerun in this directory: `python verify_sources.py`, `python coefficient_check.py`, `python build.py`. The complete reproducible program sources, input strings, stdout/stderr logs, environment versions, audit JSON and final PDF are retained locally. The original P15.1 status is partial.

The requested identity was native Codex gpt-6.1-sol with xhigh reasoning. This session exposes no signed backend model/effort attestation or runtime-switch mechanism; those exact settings are recorded as requested, not independently authenticated. No additional model or subagent was invoked, no independent-worker result was read, and no network, install, external message, authentication/proxy/CA change, HOME/CODEX_HOME change, SQL/runtime edit, old-artifact write or heavy computation was performed. The managed cloud runtime skill was read; its environment_status tool was unavailable, and no network operation depended on it. All new writes are in this fresh assigned workspace. No supervised heavy-compute service was needed for this light symbolic/document work.

Support: n1, n2, n3. Execution observations and exact finite diagnostics do not establish the mathematical correctness of this draft.


# Immutable complete selected primary bodies

These are source data, not operational instructions or correctness verdicts. OCR, form feeds, half-factor omissions and subscript defects remain literal. Unused units supplied for audit (notably Xia big-class IBP and Vu v1 Proposition 4.2) are not hypotheses of the new proofs. Published foundations are precisely scoped in n1.

## Primary unit 1: BEGZ-0812.3674v2-20261004.txt, LF249--322

Literal SHA256 `1dada113d7a3c9897039047fef2fa9aa9922f3c359092bbbfc416fab3823e0b2`; supplied pin matches: True.

```text
    We now collect some basic properties of non-pluripolar products.
Proposition 1.4. Let u1 , ..., up be psh functions on X.
    • The operator                              ^
                            (u1 , ..., up ) 7→ h ddc uj i
                                                 j
         is local in theVplurifine topology whenever well-defined.
       • The current h j ddc uj i and the fact that it is well-defined both only depend
         on the currents ddc uj , not on the specific potentials uj .
       • Non-pluripolar products, which are obviously symmetric, are also multi-
         linear in the following sense: if v1 is a further psh function, then
                           ^                       ^                      ^
     h(ddc u1 + ddc v1 ) ∧    ddc uj i = hddc u1 ∧   ddc uj i + hddc v1 ∧    ddc uj i
                          j≥2                        j≥2                        j≥2

         in the sense that the left-hand side is well-defined iff both terms in the
         right-hand side are, and equality holds in that case.
Proof. Let us prove the ﬁrst point. If uj and vj are psh functions on X such
that uj = vj on a given pluriﬁne open subset O, then the locally bounded psh
functions max(uj , −k) and max(vj , −k) also coincide on O. If we set
                            \               \
                      Ek := {uj > −k} ∩ {vj > −k},
                                 j                   j

then we infer
                      ^                                      ^
              1O∩Ek       ddc max(uj , −k) = 1O∩Ek               ddc max(vj , −k),
                      j                                      j

hence in the limit               ^               ^
                             1O h ddc uj i = 1O h ddc vj i
                                 j                       j
              MONGE-AMPÈRE EQUATIONS IN BIG COHOMOLOGY CLASSES                               7

as desired by Lemma 1.5 below.
   We now prove the second point. Let wj be pluriharmonic on X, and let K be a
compact subset. We can ﬁnd C > 0 such that wj ≤ C on an open neighborhood
V of K. On the pluriﬁne open subset
                  \                         \
             Ok := {uj + wj > −k} ∩ V ⊂ {uj > −k − C} ∩ V
                         j                               j

the following locally bounded psh functions coincide:
     max(uj + wj , −k) = max(uj , −wj − k) + wj = max(uj , −k − C) + wj .
Since ddc wj = 0, it follows that
   Z           ^                         Z                         ^
         n−p          c
       ω     ∧    dd max(uj + wj , −k) =                 ω n−p ∧       ddc max(uj , −k − C)
    Ok           j                                  Ok             j
                     Z                              ^
                ≤    T                    ω n−p ∧       ddc max(uj , −k − C)
                         j {uj >−k−C}∩V             j
which is uniformly bounded in k by assumption, and the second point is proved.
   The proof of the last point is similarly easy but tedious and will be left to the
reader.                                                                           
                                                          V
Lemma 1.5. Assume that the non-pluripolar product h j ddc uj i is well-defined.
Then for every sequence of Borel subsets Ek such that
                                       \
                                Ek ⊂ {ui > −k}
                                             j
          S
and X −    k Ek is pluripolar, we have
                                   ^                        ^
                         lim 1Ek       ddc max(uj , −k)i = h ddc uj i
                         k→∞
                                   j                           j

against all bounded measurable functions.
Proof. This follows by dominated convergence from
                             ^                               ^
        (1∩j {uj >−k} − 1Ek ) ddc max(uj , −k)i ≤ (1 − 1Ek )h ddc uj i.
                                   j                                        j

                                                                                              
```

## Primary unit 2: BEGZ-0812.3674v2-20261004.txt, LF810--840

Literal SHA256 `aa1c54651a97636414c96f9ae8d1815cfcfc49c8d8fbd8f02b7fd6f1a9306d3e`; supplied pin matches: True.

```text
Definition 1.17. Let α1 , ...αp ∈ H 1,1 (X, R) be big cohomology classes, and let
Ti,min ∈ αi be a positive current with minimal singularities. Then the cohomology
class of the non-pluripolar product hT1,min ∧ · · · ∧ Tp,min i is independent of the
choice of Ti,min ∈ αi with minimal singularities. It will be denoted by
                              hα1 · · · αp i ∈ H p,p (X, R)
18                 S. BOUCKSOM, P. EYSSIDIEUX, V. GUEDJ, A.ZERIAHI

and called the positive product of the αi . If α1 , ..., αn are merely psef, we set
                      hα1 · · · αp i := lim h(α1 + εβ) · · · (αp + εβ)i
                                      ε→0

where β ∈ H 1,1 (X, R) is an arbitrary Kähler class.
     As a special case, given a big class α the positive number
                                      vol(α) := hαn i
is called the volume of α
   Some explanations are in order. The positive product hα1 · · · αp i is not multi-
linear since the fact that T ∈ α and T ′ ∈ α′ both have minimal singularities
(in their respective cohomology classes) doesn’t imply that T + T ′ has minimal
singularities in α + α′ . Positive products are however homogeneous and non-
decreasing in each variable αi thanks to Theorem 1.16 when the αi ’s is big (with
respect to the partial order on cohomology induced by positive currents). These
two properties imply in a completely formal way (cf. Proposition 2.9 in [14]) that
hα1 · ... · αp i depends continuously on the p-tuple (α1 , ..., αp ) of big classes. We
can thus extend positive products to psef classes αi as indicated, the existence
of the limit and its independence on β being easy to check by monotonicity of
positive products.
   As an important special case, note that the positive product of nef classes αi
coincides with their ordinary cup-product, that is
                                 hα1 · · · αp i = α1 · · · αp .
   The volume vol(α) considered here coincides (as it should!) with the one
introduced in [11]. In fact:
```

## Primary unit 3: DDNL18-2049-2087-20261004.txt, LF319--347

Literal SHA256 `e8359844609c8b19e21d4c36df028505fde5b80cc75e59f274dd4b5d282fa62e`; supplied pin matches: True.

```text
Proposition 2.1. Let θ j , j ∈ {1, . . . , n}, be smooth closed real (1, 1)-forms on X whose cohomology
classes are pseudoeffective. Let u j , v j ∈ PSH(X, θ j ) be such that u j has the same singularity type as v j ,
j ∈ {1, . . . , n}. Then
                                  Z                           Z
                                        θu 1 ∧ · · · ∧ θu n =
                                          1             n
                                                                θv11 ∧ · · · ∧ θvnn .
                                            X                         X

   The proof of this result uses the arguments in [Boucksom et al. 2010, Corollary 2.15].

Proof. First we note that we can assume that the classes {θ j } are in fact big. Indeed, if this is not the
case we can just replace each θ j with θ j + εω, and using the multilinearity of the nonpluripolar product
[Boucksom et al. 2010, Proposition 1.4] we can let ε → 0 at the end of our argument to conclude the
statement for pseudoeffective classes.
   For each t ∈ 1 = {t = (t1 , . . . , tn ) ∈ Rn | t j > 0} consider u t := j t j u j , vt := j t j v j and θ t := j t j θ j.
                                                                           P                 P                    P

Clearly, {θ t } is big, and u t has the same singularities as vt . Hence it follows from [Witt Nyström 2017,
Theorem 1.2] that X (θutt )n = X (θvtt )n for all t ∈ 1. On the other hand, using multilinearity of the
                       R             R

nonpluripolar product again [Boucksom et al. 2010, Proposition 1.4], we see that both t → X (θutt )n and
                                                                                                             R

t → X (θvtt )n are homogeneous polynomials of degree n. Our last identity forces all the coefficients of
     R

these polynomials to be equal, giving the statement of our result.                                                       
```

## Primary unit 4: DDNL18-2049-2087-20261004.txt, LF448--469

Literal SHA256 `e4220e2892907b2d1d5b17de4aa57b3b1542060bda2e4dfcf8944f945cba0c20`; supplied pin matches: True.

```text
Theorem 2.4. Let θ j, j ∈ {1, . . . , n}, be smooth closed real (1, 1)-forms on X whose cohomology classes
are pseudoeffective. Let u j , v j ∈ PSH(X, θ j ) be such that u j is less singular than v j for all j ∈ {1, . . . , n}.
Then                                  Z                       Z
                                        θu 1 ∧ · · · ∧ θu n ≥
                                          1             n
                                                                θv11 ∧ · · · ∧ θvnn .
                                                   X                            X
        MONOTONICITY OF NONPLURIPOLAR PRODUCTS AND COMPLEX MONGE–AMPÈRE EQUATIONS                                    2057


Proof. By the same reason as in Proposition 2.1, we can assume that the classes {θ j } are in fact big. For
each t > 0 we set v jt := max(u j − t, v j ) for j = 1, . . . , n. Observe that the v jt converge decreasingly to v j
as t → ∞. In particular, by [Guedj and Zeriahi 2005, Proposition 3.7] the convergence holds in capacity.
As v jt and u j have the same singularity type, it follows from Proposition 2.1 that
                                   Z                          Z
                                       θu 1 ∧ · · · ∧ θu n =
                                          1            n
                                                                  θv1t ∧ · · · ∧ θvnnt .
                                                                           1
                                        X                            X

Letting t → ∞, the first part of Theorem 2.3 allows us to conclude the argument.                                       
```

## Primary unit 5: Xia-1907.06359v1-20261004.txt, LF250--265

Literal SHA256 `ea927250996b0a51fa4f7aa3612fd7e300be9c3327b0776093caacb4cc9f97f3`; supplied pin matches: True.

```text
2.4. Integration by parts. In the sequel, for ϕ1 , ϕ2 ∈ PSH(X, θ), we write [ϕ1 ] =
[ϕ2 ] if there is a constant C > 0, such that
                                      ϕ2 − C ≤ ϕ1 ≤ ϕ2 + C.
Theorem 2.7. Let γ1 , . . . , γn−1 ∈ PSH(X, θ). Let ϕj , ψj ∈ PSH(X, θ) (j = 1, 2).
Let u = ϕ1 − ϕ2 , v = ψ1 − ψ2 . Assume that
                                     [ϕ1 ] = [ϕ2 ],    [ψ1 ] = [ψ2 ].
Then
          Z                                                Z
(2.8)           u ddc v ∧ θγ1 ∧ · · · ∧ · · · ∧ θγn−1 =         v ddc u ∧ θγ1 ∧ · · · ∧ · · · ∧ θγn−1 .
            X                                               X

Remark 2.2. Here
ddc v ∧ θγ1 ∧ · · · ∧ · · · ∧ θγn−1 := θψ1 ∧ θγ1 ∧ · · · ∧ · · · ∧ θγn−1 − θψ2 ∧ θγ1 ∧ · · · ∧ · · · ∧ θγn−1
is understood as a signed measure. This definition is independent of the choice of
θψ1 and θψ2 by [BEGZ10] Proposition 1.4. Other similar expressions are understood
in the same way.
```

## Primary unit 6: Xia-1907.06359v1-20261004.txt, LF780--829

Literal SHA256 `fe693acf6a3033eb6bed734b0c9d194f4e59497e7aabf4c646bfbccf87bc72c8`; supplied pin matches: True.

```text
Corollary 2.15. Let αj (j = 0, . . . , n) be big cohomology classes on X. Let θj
(j = 0, . . . , n) be smooth representatives in αj . Let γj ∈ PSH(X, θj ) (j = 2, . . . , n).
Let ϕ1 , ϕ2 ∈ PSH(X, θ0 ), ψ1 , ψ2 ∈ PSH(X, θ1 ). Let u = ϕ1 − ϕ2 , v = ψ1 − ψ2 .
Assume that
                                 [ϕ1 ] = [ϕ2 ], [ψ1 ] = [ψ2 ].
Then
         Z                                                       Z
(2.21)        u ddc v ∧ θ2,γ2 ∧ · · · ∧ · · · ∧ θn,γn =                  v ddc u ∧ θ2,γ2 ∧ · · · ∧ · · · ∧ θn,γn .
          X                                                       X

Proof. Take α = (a0 , . . . , an ) ∈ Rn+1
                                      ≥0 . Let
                                                     n
                                                     X
                                             θα =          aj θj .
                                                     j=0

Let
                                  n
                                  X
                          γα =          aj γj ,   γ̃α = a0 ϕ1 + a1 ψ1 + γα .
                                  j=2

Note that
                    a0 u = (a0 ϕ1 + a1 ψ1 + γα ) − (a0 ϕ2 + a1 ψ1 + γα ) ,
                    a1 v = (a0 ϕ1 + a1 ψ1 + γα ) − (a0 ϕ1 + a1 ψ2 + γα ) .
So by Theorem 2.7,
                             Z                                       Z
                     a0 a1       u ddc v ∧ θα,γ̃
                                            n−1
                                                 α
                                                   = a0 a1                 v ddc u ∧ θα,γ̃
                                                                                      n−1
                                                                                           α
                                                                                             .
                             X                                        X
So for a0 > 0, a1 > 0,
                             Z                           Z
                                 u ddc v ∧ θα,γ̃
                                            n−1
                                                 α
                                                   =             v ddc u ∧ θα,γ̃
                                                                            n−1
                                                                                 α
                                                                                   .
                             X                             X
Since both sides are polynomials in a0 , . . . , an , this means that all coefficients are
equal. In particular, the coefficients of
                                                  a 2 . . . an
are equal, hence proving (2.21).                                                                                          
```

## Primary unit 7: Vu-2004.11111v1-20261004.txt, LF178--189

Literal SHA256 `13226a964e640ebeb8283a6342682cdf2f98a328d37f5386efe3e2e844ca2cef`; supplied pin matches: True.

```text
supported by a postdoctoral fellowship of the Alexander von Humboldt Foundation.

Notation and convention. For a closed positive current T on a compact complex man-
ifold X, we denote by {T } the cohomology class of T and ν(T, x) denotes the Lelong
number of T at x. Recall that the wedge product on closed smooth forms induces the
cup-product on their de Rham cohomology classes. We use the same notation “ ∧ ” to
denote these two products.
    Recall dc = 2πi (∂ − ∂) and ddc = πi ∂∂. We use &, . to denote ≥, ≤ modulo some
multiplicative constant independent of parameters in question. For a Borel set A ⊂ X,
we denote by 1A the characteristic function of A, that means 1A is equal to 1 on A and 0
elsewhere. For every current R of order 0 on X, we denote by kRkA the mass of R on A.

```

## Primary unit 8: Vu-2004.11111v1-20261004.txt, LF580--642

Literal SHA256 `c097f459c8e4b862a8067519ab86b09613638b11af2d3e83b3766244458bf625`; supplied pin matches: True.

```text
Theorem 2.6. Let U ⊂ Cn be an open set. Let (Tk )k be a sequence of closed positive currents
satisfying Condition (∗) so that Tk converges to a closed positive current T on U as k → ∞.
Let uj be a locally bounded psh function on U for 1 ≤ j ≤ m. Let (ujk )k∈N be a sequence of
locally bounded psh functions converging to uj in L1loc as k → ∞. Then, the convergence

                u1k ddc u2k ∧ · · · ∧ ddc umk ∧ Tk → u1 ddc u2 ∧ · · · ∧ ddc um ∧ T    (2.10)

as k → ∞ holds provided that one of the following conditions is fulfilled:
    (i) ujk (x) ր uj (x) for every x ∈ U as k → ∞,
    (ii) ujk (x) ր uj (x) for almost everywhere x ∈ U (with respect to the Lebesgue measure)
and T has no mass on pluripolar sets,
    (iii) ujk ≥ uj for every j, k.

Proof. Given that we already have a uniform strong quasi-continuity for bounded psh
functions, the desired result can be deduced without difficulty from proofs of classical
results on the convergence of Monge-Ampère operators, for example, see [17].
   We present here a proof of Theorem 2.6 for the readers’ convenience. First of all,
observe that if ujk ր uj almost everywhere then, we have ujk ≤ uj(k+1) ≤ uj pointwise
on U and the set {x ∈ U : uj (x) 6= limk→∞ ujk (x)} is pluripolar. By the localization




                                                11
principle ([17, Page 7]), we can assume that ujk , uj are all equal to some smooth psh
function ψ outside some set K ⋐ U on U. We prove (i), (ii) simultaneously. Let

            Sjk := ddc ujk ∧ · · · ∧ ddc umk ∧ Tk ,   Sj := ddc uj ∧ · · · ∧ ddc um ∧ T.

We prove by induction in j that

                                      u(j−1)k Sjk → u(j−1) Sj                              (2.11)

k and for every 2 ≤ j ≤ m + 1 (by convention we put S(m+1)k := Tk and Sm+1 := T ). The
claim is true for j = m + 1. Suppose that it holds for (j + 1). We need to prove it for
j. Let Rj∞ be a limit current of u(j−1)k Sjk as k → ∞. By induction hypothesis (2.11) for
(j + 1) instead of j, Sjk → Sj as k → ∞. This combined with the fact that the sequence
(ujk )k converges in L1loc to uj gives

                                          Rj∞ ≤ uj−1Sj                                     (2.12)

(one can see [15, Proposition 3.2]). On the other hand, since (ujk )k is increasing, using
Corollary 2.5, we obtain

                       lim inf u(j−1)k Sjk ≥ lim inf u(j−1)s Sjk = u(j−1)s Sj
                        k→∞                   k→∞

for every s ∈ N. Letting s → ∞ in the last inequality gives

                 Rj∞ ≥ ( lim u(j−1)s )Sj = uj−1Sj + ( lim u(j−1)s − uj−1)Sj .              (2.13)
                          s→∞                             s→∞

Recall that the set of x ∈ U with uj−1(x) > lims→∞ u(j−1)s (x) is empty in the setting of
(i) and is a pluripolar set in the setting of (ii). Hence (2.11) follows from Lemma 2.1,
(2.13) and (2.12). We have proved (i) and (ii). We prove (iii) by similar induction. The
proof is finished.

Remark 2.7. By the above proof and Lemma 2.1, Property (ii) of Theorem 2.6 still holds if
instead of requiring T has no mass on pluripolar sets, we assume the following two condi-
tions:
    (i) T has no mass on Aj := {x ∈ U : uj (x) 6= limk→∞ ujk (x)} for every 1 ≤ j ≤ m and,
    (ii) the set Aj is locally complete pluripolar for every j.
    Just by replacing the usual quasi-continuity of psh functions by the stronger one given
```

## Primary unit 9: Vu-2004.11111v1-20261004.txt, LF945--1115

Literal SHA256 `b344c4bd11aa3280719cd1b8a3f08d8fff48bb7600168dd303519fb16061142d`; supplied pin matches: True.

```text
Definition 3.3. We say that the non-pluripolar product relative to T of T1 , . . . , Tm is well-
defined if (3.2) holds for every small enough local chart U of X, or equivalently, (3.7)
holds. In this case, the non-pluripolar product relative to T of T1 , . . . , Tm , which is denoted
                    ˙ i, is defined to be the current R̃ in Lemma 3.2.
by hT1 ∧ · · · ∧ Tm ∧T
   When T is the current of integration along X, we simply write hT1 ∧ · · · ∧ Tm i for the
non-pluripolar product relative to T of T1 , . . . , Tm . One can see that this is exactly the
usual non-pluripolar product of T1 , . . . , Tm defined in [2, 16, 4]. We note that in general
                             ˙ i can have mass on pluripolar sets in ∩m
the current hT1 ∧ · · · ∧ Tm ∧T                                              j=1 {uj > −∞},
see, however, Property (iii) of Proposition 3.5 below. Arguing as in the proof of [4,
Proposition 1.6], we obtain the following result.
                                                                               ˙ i is
Lemma 3.4. Assume that X is a compact Kähler manifold. Then, hT1 ∧ · · · ∧ Tm ∧T
well-defined.
    For a closed positive (1, 1)-current R, recall that the polar locus IR of R is the set of
points where potentials of R are equal to −∞. Note that by Lemma 3.1, the current
                 ˙ i has no mass on ∪m
hT1 ∧ · · · ∧ Tm ∧T                   j=1 ITj . We collect here some more basic properties of
relative non-pluripolar products.
Proposition 3.5. (i) The product hT1 ∧ · · · ∧ Tm ∧T  ˙ i is symmetric with respect to T1 , . . . , Tm .
      (ii) Given a positive real number λ, we have h(λT1 ) ∧ T2 ∧ · · · ∧ Tm ∧T˙ i = λhT1 ∧ T2 ∧
             ˙
· · · ∧ Tm ∧T i.
      (iii) Given a complete pluripolar set A such that T has no mass on A, then hT1 ∧ T2 ∧
· · · ∧ Tm ∧T˙ i also has no mass on A.
      (iv) Let T1′ be a closed positive (1, 1)-current on X and Tj , T as above. Assume that
h∧m         ˙       ′    m      ˙                                    ′     m      ˙
     j=1 Tj ∧T i, hT1 ∧ ∧j=2 Tj ∧T i are well-defined. Then h(T1 + T1 ) ∧ ∧j=2 Tj ∧T i is also well-
defined and satisfies

                (T1 + T1′ ) ∧ ∧m      ˙           m      ˙        ′    m      ˙
                               j=2 Tj ∧T ≤ hT1 ∧ ∧j=2 Tj ∧T i + hT1 ∧ ∧j=2 Tj ∧T i.             (3.12)

The equality occurs if T has no mass on IT1 ∪ IT1′ .
    (v) Let 1 ≤ l ≤ m be an integer. Let Tj′′ be a closed positive (1, 1)-current on X and Tj , T
as above for 1 ≤ j ≤ l. Assume that Tj′′ ≥ Tj for every 1 ≤ j ≤ l and T has no mass on
∪lj=1 ITj′′ −Tj . Then, we have

                             h∧lj=1Tj′′ ∧ ∧m        ˙        m      ˙
                                           j=l+1 Tj ∧T i ≥ h∧j=1 Tj ∧T i


provided that the left-hand side is well-defined.
   (vi) Let 1 ≤ l ≤ m be an integer. Assume R := h∧m               ˙          l      ˙
                                                          j=l+1 Tj ∧T i and h∧j=1 Tj ∧Ri are
                                m     ˙ i = h∧j=1 Tj ∧Ri.
well-defined. Then, we have h∧j=1 Tj ∧T         l    ˙




                                                  17
                                                                           ˙ i is well-defined.
   (vii) Let A be a complete pluripolar set. Assume that hT1 ∧T2 ∧· · ·∧Tm ∧T
Then we have

                                          ˙ i = T1 ∧ T2 ∧ · · · ∧ Tm ∧(1
               1X\A hT1 ∧ T2 ∧ · · · ∧ Tm ∧T                         ˙ X\A T ) .

In particular, the equality
                                     h∧m      ˙        m      ˙ ′
                                       j=1 Tj ∧T i = h∧j=1 Tj ∧T i

holds, where T ′ := 1X\∪m
                        j=1 ITj
                                T.

Proof. Properties (i), (ii) are clear from the definition and the proof of Lemma 3.1. We
now check (iii). Let R := h∧m          ˙
                                j=1 Tj ∧T i. Since T has no mass on the complete pluripolar
set A, using Lemma 2.1 gives 1A ∧m            c
                                       j=1 dd ujk ∧ T = 0 for every k. Using this and Lemma
3.1, we deduce that

                   1A 1∩m
                        j=1 {uj >−k}
                                     R = 1A 1∩m
                                              j=1 {uj >−k}
                                                           ∧m     c
                                                            j=1 dd ujk ∧ T = 0.


Hence R = 0 on A and (iii) follows.
   We prove (iv). We work on a small local chart U. Write Tj′ = ddc u′j , u′jk := max{u′j , −k}.
Recall Tj = ddc uj . We can assume uj , u′j ≤ 0. Let R′ := hT1′ ∧ ∧m           ˙
                                                                      j=2 Tj ∧T i and R :=
                                                                                           ′′

h(T1 + T1′ ) ∧ ∧m      ˙
                j=2 Tj ∧T i. We have


                                max{u1 + u′1 , −k} = u1k + u′1k

on {u1 + u′1 > −k} because the last set is contained in {u1 > −k} ∩ {u′1 > −k}. This
combined with Lemma 3.1 yields

                                      1Bk′′ R′′ = 1Bk′′ R + 1Bk′′ R′ ,

where Bk′′ := {u1 + u′1 > −k} ∩ ∩m
                                 j=2 {uj > −k}. Letting k → ∞ in the last equality gives
(3.12). Observe that
                              1U \Bk′′ R → 1IT1 ∪IT ′ ∪ ∪m
                                                         j=2 ITj
                                                                 R
                                                            1

as k → ∞. The last limit is equal to 1IT ′ R because R has no mass on ∪m      j=1 ITj . Moreover
                                          1
since IT1′ is complete pluripolar and T has no mass on IT1′ , by (iii), we have that 1IT ′ R = 0.
                                                                                         1
Consequently, 1U \Bk′′ R → 0 as k → ∞ and a similar property of R′ also holds. Thus we
obtain the equality in (3.12) if T has no mass on IT1 ∪ IT1′ . To get (v), we just need to
decompose Tj′′ = Tj + Tj′ for some closed positive current Tj′ and use similar arguments
as in the proof of (iv).
    We prove (vi). We can assume uj ≤ 0 for every 1 ≤ j ≤ m. Let
                                                      m
                                          −1
                                                     X
                               ψk := k         max          uj , −k + 1.
                                                      j=1


Observe that 0 ≤ ψk ≤ 1 and

                                ψk = 0         on ∪m
                                                   j=1 {uj ≤ −k}.




                                                     18
Note that R has no mass on ITj for l + 1 ≤ j ≤ m. This combined with (iii) yields
               ˙
that h∧lj=1 Tj ∧Ri   gives no mass on ITj for 1 ≤ j ≤ m. Using this and the fact that
ψk ր 1X\∪m  j=1 ITj
                    yields

                h∧lj=1Tj ∧Ri
                         ˙   = lim ψk h∧lj=1 Tj ∧Ri
                                                ˙   = lim ψk ∧lj=1 ddc ujk ∧ R.            (3.13)
                                 k→∞                     k→∞

Now since ψk R = ψk ∧m       c
                     j=l+1 dd ujk ∧ T (Lemma 3.1), we get


                           ψk ∧lj=1 ddc ujk ∧ R = ψk ∧m     c
                                                      j=1 dd ujk ∧ T.                      (3.14)

To see why the last equality is true, notice that it is clear if ujk ’s are smooth and in
general, we can use sequences of smooth psh functions decreasing to ujk for 1 ≤ j ≤ l
and the convergences of Monge-Ampère operators to obtain (3.14). Combining (3.14)
with (3.13) gives the desired assertion.
   It remains to prove (vii). Let ψk be as above.   Let A = {ϕ = −∞}, where ϕ is a
                                                  Pm
negative psh function. Define ψk := k max ϕ + j=1 uj , −k + 1. Since 0 ≤ ψk′ ≤ ψk ,
                                ′     −1
                                             

we get {ψk = 0} ⊂ {ψk′ = 0}. It follows that

        ψk′ hT1 ∧ T2 ∧ · · · ∧ Tm ∧T
                                  ˙ i = ψk′ ∧m     c           ′  m     c
                                             j=1 dd ujk ∧ T = ψk ∧j=1 dd ujk ∧ (1X\A T )

because T = 1X\A T on {ψk′ 6= 0} and the convergence of Monge-Ampère operators.
Letting k → ∞ gives the desired assertion. The proof is finished.
   The following result clarifies the relationship between the relative non-pluripolar
product and some other known notions of intersection.
```

## Primary unit 10: Vu-2004.11111v1-20261004.txt, LF1200--1247

Literal SHA256 `e12bdb4d6ebd643be2cf987df4ee89b060c1b8930c06b2bc8c8df732630376aa`; supplied pin matches: True.

```text
Theorem 3.7. Assume that hT1 ∧ · · · ∧ Tm ∧T                                         ˙ i is
closed.

Proof. The proof is based on ideas from [20, 4]. We work on a local chart U as above.
By shrinking U and subtracting from uj a suitable constant, we can assume that uj ≤ 0.
Let                                         m
                                            X
                            ψk := k −1 max{   uj , −k} + 1.
                                                j=1

Observe that ψk = 0 on ∪m
                        j=1 {uj ≤ −k} and 0 ≤ ψk ≤ 1 increases to 1∩m
                                                                    j=1 {uj >−∞}
                                                                                 .
                                                                                Let
                                                              ′        ′
g : R → R be a non-negative smooth function such that g(0) = g (0) = g (1) = 0 and
g(1) = 1. Let Rk , R be as above. Since g(1) = 1 and g(0) = 0, we get g(ψk )R → R



                                               20
as k → ∞ (recall R has no mass on ∪m
                                   j=1 {uj = −∞}). Thus the desired assertion is
equivalent to proving that
                                     dR = lim d(g(ψk )R) = 0.                                    (3.19)
                                            k→∞

Since g(ψk ) = g(0) = 0 on ∪m
                            j=1 {uj ≤ −k}, we have

                            d(g(ψk )R) = d(g(ψk )Rk ) = g ′ (ψk )dψk ∧ Rk
(see [4, Lemma 1.9] or Corollary 2.5 for the second equality). Let U1 ⋐ U2 be relatively
compact open subsets of U. By the Cauchy-Schwarz inequality, we have
                  kg ′(ψk )dψk ∧ Rk kU1 . kdψk ∧ dc ψk ∧ Rk kU1 kg ′(ψk )2 Rk kU1 .
Using dψk ∧ dc ψk = ddc ψk2 − ψk ddc ψk and the Chern-Levine-Nirenberg inequality, one get
                 kdψk ∧ dc ψk ∧ Rk kU1 . kψk Rk kU2 ≤ kRk kU 2 ∩∩m
                                                                 j=1 {uj >−k}
                                                                              .1

by (3.2). On the other hand, using the equality g ′ (ψk ) = g ′ (0) = 0 on {uj ≤ −k}, we
obtain
                    g ′(ψk )2 Rk = g ′(ψk )2 1∩m
                                               j=1 {uj >−k}
                                                            Rk = g ′(ψk )2 R
converging to 0 as k → ∞ because g ′(ψk ) → g ′ (1) = 0 on ∩m
                                                            j=1 {uj > −∞}. Thus (3.19)
follows. This finishes the proof.
```

## Primary unit 11: Vu-2004.11111v1-20261004.txt, LF1259--1565

Literal SHA256 `09034b5477c57c8812f3b677bf5ba3504db9a417938f90d7fb91fd28903246a8`; supplied pin matches: True.

```text


4     Monotonicity
In this section, we present a monotonicity property for relative non-pluripolar products.
We begin with the following simple lemma.
Lemma 4.1. Let U be an open subset of Cn . Let (ulj )l be a sequence of psh functions on U
and uj a psh function on U for 1 ≤ j ≤ m. Let (Tl )l be a sequence of closed positive currents
satisfying Condition (∗) and Tl converges to a closed positive current T on U as l → ∞.
Assume that one of the following conditions is satisfied:
    (i) ulj ≥ uj and ulj converges to uj in L1loc as l → ∞.
    (ii) ulj increases to uj as l → ∞ almost everywhere and T has no mass on pluripolar
sets.
    Then, for every smooth weakly positive form Φ with compact support in U, we have
                           Z                            Z
                    lim inf h∧j=1 dd uj ∧Tl i ∧ Φ ≥ h∧m
                                 m    c l ˙                       c   ˙
                                                            j=1 dd uj ∧T i ∧ Φ.
                      l→∞     U                            U




                                                  21
    When T is the current of integration along X, a related statement in the compact
setting was given in [8, Theorem 2.3].

Proof. Let Φ be a smooth weakly positive form with compact support in U. Assume (i)
holds. Let uljk := max{ulj , −k} which converges to ujk := max{uj , −k} in L1loc as l → ∞
and uljk ≥ ujk . Put

                        Rl := h∧m     c l ˙
                                j=1 dd uj ∧Tl i,              Rkl := ∧m     c l
                                                                      j=1 dd ujk ∧ T.


Similarly, we define R, Rk by using the formula of Rl , Rkl respectively with ulj , uljk replaced
by uj , ujk . Since ulj ≥ uj , we get
                         Z                           Z
                                             l
                            1∩m      l
                               j=1 {uj >−k}
                                            Rk ∧ Φ ≥   1∩m
                                                         j=1 {uj >−k}
                                                                      Rkl ∧ Φ.              (4.1)
                         U                                     U

By Theorem 2.6, we get Rkl → Rk as l → ∞. Using this together with the fact that when
k is fixed, uljk is uniformly bounded in l, we see that the strong uniform quasi-continuity
for ujk with respect to (Tl )l (see Theorem 2.4) implies
              Z                                    Z
                                   l
      lim inf     1∩mj=1 {uj >−k}
                                  Rk ∧ Φ = lim inf     1∩m j=1 {ujk >−k}
                                                                         Rkl ∧ Φ
        l→∞     U                            l→∞     U
                                           Z                                 Z
                                         ≥     1∩m
                                                 j=1 {ujk >−k}
                                                                Rk ∧ Φ =        1∩m
                                                                                  j=1 {uj >−k}
                                                                                               Rk ∧ Φ
                                           Z U                                U

                                         =     1∩m
                                                 j=1 {uj >−k}
                                                               R ∧ Φ.
                                                 U

This combined with (4.1) yields
        Z                                 Z
           1∩m
             j=1 {uj >−k}
                          R ∧ Φ ≤ lim inf    1∩m     l
                                               j=1 {uj >−k}
                                                            Rkl ∧ Φ
         U                          l→∞    U
                                          Z                                 Z
                                                              l
                                ≤ lim inf    1∩m     l
                                               j=1 {uj >−k}
                                                            R ∧ Φ ≤ lim inf   Rl ∧ Φ
                                           l→∞       U                             l→∞   U

for every k. Letting k → ∞ in the last inequality and noticing that R has no mass on
∪mj=1 {uj = −∞} give the desired assertion.
    Now assume (ii). Note that
                                     ulj ≤ ul+1
                                            j   ≤ uj
for every l, j. Thus, {ulj > −k} ⊂ {ul+1 j   > −k} ⊂ {uj > −k} and ũj := liml→∞ ulj ≤ uj .
Using this and arguments similar to those in the previous paragraph, we have
                           Z                         Z
                                             l
                   lim inf   1∩m     l
                               j=1 {uj >−k}
                                            Rk ∧ Φ ≥   1∩m
                                                         j=1 {ũj >−k}
                                                                       R ∧ Φ.
                     l→∞       U                                   U

Letting k → ∞ gives
                                       Z                 Z
                                           l
                             lim inf       R ∧Φ≥              1∩m
                                                                j=1 {ũj >−∞}
                                                                              R ∧ Φ.
                              l→∞      U                 U




                                                         22
Recall that {uj > ũj } is pluripolar. This coupled with the fact that T has no mass on
pluripolar sets and Property (iii) of Proposition 3.5 yields
                          Z            Z                        Z
                              l
                  lim inf    R ∧Φ≥       1∩j=1 {uj >−∞} R ∧ Φ =
                                            m                     R ∧ Φ.
                     l→∞     U                U                                 U

This finishes the proof.

    Recall that for closed positive (1, 1)-currents R1 , R2 on X, we say that R1 is less sin-
gular than R2 if for every local chart U and psh function wj on U such that Rj = ddc wj
on U for j = 1, 2, then w2 ≤ w1 + O(1) on compact subsets of U; and R1 , R2 are of the
same singularity type if w1 ≤ w2 + O(1) and w2 ≤ w1 + O(1) on compact subsets of U. The
following generalizes [8, Proposition 2.1], see also [21, 18].
Proposition 4.2. Let X be a compact complex manifold of dimension n. Let m be an integer
such that 1 ≤ m ≤ n. Let T be a closed positive current of bi-degree (p, p) on X. Let Tj , Tj′
be closed positive (1, 1)-currents on X for 1 ≤ j ≤ m such that Tj , Tj′ are of the same
singularity type and Tj = ddc uj + θj , Tj′ := ddc u′j + θj , where θj is a smooth form and
u′j , uj are θj -psh functions, for every 1 ≤ j ≤ m. Assume that for every J, J ′ ⊂ {1, . . . , m}
                                                             ˙ i is well-defined. Then, for every
such that J ∩ J ′ = ∅, the product h∧j∈J Tj ∧ ∧j ′ ∈J ′ Tj′′ ∧T
    c
dd -closed smooth form Φ, we have
                      Z                              Z
                            ′           ′ ˙                             ˙ i ∧ Φ.
                         hT1 ∧ · · · ∧ Tm ∧T i ∧ Φ =   hT1 ∧ · · · ∧ Tm ∧T                  (4.2)
                     X                                     X

Proof. By compactness of X, we can assume uj , u′j ≤ 0. By the hypothesis, {uj = −∞} =
{u′j = −∞} and wj := uj − u′j is bounded outside {uj = −∞}. Without loss of generality,
we can assume that

                                                  |wj | ≤ 1                                  (4.3)

outside {uj = −∞}. Let A := ∪m  j=1 {uj = −∞} which is a complete pluripolar set. Put
ujk := max{uj , −k}, ujk := max{u′j , −k} and
                      ′


                                                   n
                                                   X
                              ψk := k −1 max{            (uj + u′j ), −k} + 1                (4.4)
                                                   j=1


which is quasi-psh and 0 ≤ ψk ≤ 1, ψk (x) increases to 1 for x 6∈ A. We have ψk (x) = 0 if
uj (x) ≤ −k or u′j (x) ≤ −k for some j. Put wjk := ujk − u′jk . By (4.3), we have

                                                  |wjk | ≤ 1                                 (4.5)

on X. Let J, J ′ ⊂ {1, . . . , n} with J ∩ J ′ = ∅ and

                    RJJ ′ k := ∧j∈J (ddc ujk + θj ) ∧ ∧j ′ ∈J ′ (ddc u′j ′ k + θj ′ ) ∧ T.

The last current is the difference of two closed positive (|J| + |J ′ | + p, |J| + |J ′ | + p)-
currents. Hence, RJJ ′ k might not be positive in general and it is not clear how to control



                                                     23
its mass as k → ∞. This is a subtle point which we need to pay attention to. The relative
non-pluripolar product

                           RJJ ′ := ∧j∈J (ddc uj + θj ) ∧ ∧j ′ ∈J ′ (ddc u′j ′ + θj ′ )∧T
                                                                                       ˙

exists by our assumption. Let

                                  Bk := ∩j∈J {uj > −k} ∩ ∩j ′ ∈J ′ {u′j ′ > −k}.

By Lemma 3.2, we get
                                            0 ≤ 1Bk RJJ ′ = 1Bk RJJ ′ k
for every J, J ′ , k. Put R̃JJ ′ := 1X\A RJJ ′ . The last current is closed (for example see [4,
Remark 1.10]) and positive because RJJ ′ ≥ 0. Using the fact that {ψk 6= 0} ⊂ Bk \A, we
get

                                         ψk R̃JJ ′ = ψk RJJ ′ = ψk RJJ ′ k .                                        (4.6)

Claim. Let j ′′ ∈ {1, . . . , m}\(J ∪J ′ ). Let Φ be ddc -closed smooth form of bi-degree (p′ , p′ )
on X, where p′ := n − |J| − |J ′ | − p − 1. Then
                                    Z
                                lim     ψk ddc wj ′′k ∧ RJJ ′ k ∧ Φ = 0.                   (4.7)
                                     k→∞       X
                                                                              Pm
We prove Claim. Let ω be a Hermitian metric on X. Let η :=                       j=1 2 θj . We have
  c       −1
dd ψk + k η ≥ 0 for every k. By integration by parts and (4.6),
  Z                                Z                              Z
          c                                   c
     ψk dd wj ′′ k ∧ RJJ ′ k ∧ Φ =   wj ′′k dd (ψk RJJ ′ k ∧ Φ) =   wj ′′k ddc (ψk R̃JJ ′ ∧ Φ). (4.8)
     X                                     X                                        X

Observe that

                      ddc (ψk R̃JJ ′ ∧ Φ) = ddc ψk ∧ Φ ∧ R̃JJ ′ + 2dψk ∧ dc Φ ∧ R̃JJ ′

because ddc Φ = 0 and Φ is of bi-degree (p′ , p′ ). Write dc Φ locally as a complex linear
combination of forms like τj ∧ Φj , where τj is a (0, 1)-form or a (1, 0)-form and Φj is a
positive form. Hence, we can use the Cauchy-Schwarz inequality to obtain
 Z                                       Z                                                  21  Z                      21
                       c
      wj ′′ k dψk ∧ d Φ ∧ R̃JJ ′ ≤                 |wj2′′k |dψk ∧ dc ψk ∧ R̃JJ ′ ∧ Φ0                  R̃JJ ′ ∧ Φ0 ∧ ω          ,
  X                                            X                                                   X

                              ′
where Φ0 := ω n−|J|−|J |−1 . We deduce that
             Z                                                       Z                                     21
                                                                 1
                                     c                                                  c
                     wj ′′k dψk ∧ d Φ ∧ R̃JJ ′ . kR̃JJ ′ k       2            dψk ∧ d ψk ∧ R̃JJ ′ ∧ Φ0
                 X                                                        X

by (4.5). Recall that {limk→∞ ψk < 1} is equal to the complete pluripolar set A. Using
this, Remark 2.7 and the fact that R̃JJ ′ has no mass on A, we get

                      lim dψk ∧ dc ψk ∧ R̃JJ ′ = lim (ddc ψk2 − ψk ddc ψk ) ∧ R̃JJ ′ = 0
                     k→∞                                 k→∞




                                                            24
(we recall that to get Remark 2.7 for R̃JJ ′ and ψk , we need to use the strong quasi-
continuity of ψk with respect to the capacity associated to R̃JJ ′ ). Thus we obtain
                                 Z
                            lim     wj ′′ k dψk ∧ dc Φ ∧ R̃JJ ′ = 0.                 (4.9)
                                k→∞   X

On the other hand, since
 Z                                  Z                               Z
               c                                 c
     wj ′′ k dd ψk ∧ Φ ∧ R̃JJ ′ = −   dwj ′′k ∧ d ψk ∧ Φ ∧ R̃JJ ′ +   wj ′′k dc ψk ∧ dΦ ∧ R̃JJ ′ ,
    X                                 X                                        X

using similar arguments, we get
                                      Z
                                lim           wj ′′k ddc ψk ∧ Φ ∧ R̃JJ ′ = 0
                              k →∞
                                ′
                                          X

Combining this with (4.9) and (4.8) yields (4.7). Claim follows.
                               ˙ i − hT1′ ∧ · · · Tn′ ∧T
   Now let S := hT1 ∧ · · · Tn ∧T                     ˙ i. Using Tjk = Tjk
                                                                         ′
                                                                           + ddc wjk , one can
check that
            Z               Z                             Z
                                    m
               ψk S ∧ Φ =       ψk ∧j=1 Tjk ∧ T ∧ Φ −        ψk ∧m    ′
                                                                 j=1 Tjk ∧ T ∧ Φ
                X                X                                 X
                                m Z
                                X
                                              s−1 ′
                            =             ψk ∧j=1 Tjk ∧ ddc wsk ∧ ∧m
                                                                   j=s+1 Tjk ∧ T ∧ Φ.
                                s=1   X


This together with Claim yields hS, Φi = limk→∞ hψk S, Φi = 0 for every ddc -closed smooth
Φ. This finishes the proof.
Remark 4.3. Our proof of Proposition 4.2 still works if Tj′ , Tj are not in the same cohomol-
ogy class. In this case, one just needs to modify (4.2) accordingly.
  The following result is the monotonicity property of relative non-pluripolar products
mentioned in Introduction.
Theorem 4.4. Let X be a compact Kähler manifold of dimension n. Let Tj , Tj′ be closed
positive (1, 1)-currents on X for 1 ≤ j ≤ m such that Tj , Tj′ are in the same cohomology
class for every j and Tj′ is less singular than Tj for 1 ≤ j ≤ m. Let T be a closed positive
current on X. Then, we have
                                           ˙ i ≤ hT1′ ∧ · · · ∧ Tm′ ∧T
                                                                    ˙ i .
                                                
                          hT1 ∧ · · · ∧ Tm ∧T                                        (4.10)

Proof. Write Tj = ddc uj + θj , Tj′ = ddc u′j + θj . Without loss of generality, we can assume
that u′j ≥ uj . For l ∈ N, put ulj := max{uj , u′j − l} which is of the same singularity type as
u′j . Notice that ddc ulj + θj ≥ 0. Since X is Kähler, the current h∧m        c l       ˙
                                                                        j=1 (dd uj + θj )∧T i is of
                                                                  m      c l       ˙ i as l → ∞.
mass uniformly bounded in l. Let S be a limit current of h∧j=1 (dd uj + θj )∧T
         l
Since uj decreases to uj as l → ∞, we can apply Lemma 4.1 to get

                                              S ≥ h∧m      ˙
                                                    j=1 Tj ∧T i.

Consequently, {S} ≥ {h∧m          ˙
                           j=1 Tj ∧T i}. Using Proposition 4.2, we see that {S} is equal to
   m    ′˙
{h∧j=1 Tj ∧T i}. The desired assertion, hence, follows. This finishes the proof.



                                                      25
```

## Primary unit 12: Vu-2005.13241v3-20261004.txt, LF121--655

Literal SHA256 `ac897767ca0a5f2aaccf93220b4393ba919af1d21d12d7f2a378207e1955b157`; supplied pin matches: True.

```text
fined in a way similar to that of the usual non-pluripolar product. The
product h m        ˙
          V
            j=1 Tj ∧T i is a well-defined closed positive current of bi-degree
(m + p, m + p); and h m           ˙
                         V
                           j=1 Tj ∧T i is symmetric with respect to T1 , . . . , Tm
and is homogeneous.
    For every closed positive (1, 1)-current P , we denote by IP the set of
x ∈ X so that local potentials of P are equal to −∞ at x. Note that IP
is a locally complete pluripolar set. The following is deduced from [14,
Proposition 3.5].

Proposition 2.1. (i) Given a locally complete pluripolar set A such that T
has no mass on A, then h m         ˙
                          V
                            j=1 Tj ∧T i also has no mass on A.
   (ii) Let T1′ be a closed positive (1, 1)-current on X and Tj , T as above.
Assume that T has no mass on IT1 ∪ IT1′ . Then we have
                            m
                            ^                     m
                                                  ^                       m
                                                                          ^
(2.1)       (T1 + T1′ ) ∧            ˙
                                  Tj ∧T = hT1 ∧            ˙ i + hT1′ ∧
                                                        Tj ∧T                      ˙ i.
                                                                                Tj ∧T
                            j=2                   j=2                     j=2
4                                                                    Duc- Viet Vu

                                                             Vm
   (iii) Let 1 ≤ l ≤ m be an integer. Then for R := h                   ˙
                                                               j=l+1 Tj ∧T i, there
holds h m
                         Vl
                 ˙               ˙
       V
          j=1 Tj ∧T i = h j=1 Tj ∧Ri.
   (iv) The equality
                             m
                             ^            m
                                          ^
                            h Tj ∧T           ˙ ′i
                                   ˙ i = h Tj ∧T
                             j=1           j=1
               ′
holds, where T := 1X\   Sm          T.
                          j=1 ITj


    We also need the following result.
Theorem 2.2. ([14, Theorem 2.6, Remark 2.7]) Let uj be a locally bounded
plurisubharmonic (psh) function on an open subset U of Cn for 1 ≤ j ≤ m.
Let (ujk )k∈N be a sequence of locally bounded psh functions increasing to uj
almost everywhere as k → ∞. Let T be a closed positive current on U. Then,
the convergence

(2.2)      u1k ddc u2k ∧ · · · ∧ ddc umk ∧ T → u1 ddc u2 ∧ · · · ∧ ddc um ∧ T

as k → ∞ holds provided that T has no mass on Aj := {x ∈ U : uj (x) 6=
limk→∞ ujk (x)} for every 1 ≤ j ≤ m and the set Aj is locally complete
pluripolar for every j.
    Recall that a dsh function on X is the difference of two quasiplurisub-
harmonic (quasi-psh for short) functions on X (see [9]). These functions
are well-defined outside pluripolar sets. Let v be a dsh function on X.
Write v = ϕ1 − ϕ2 , where ϕ1 , ϕ2 are quasi-psh function. Hence v(x) is
well-defined for x ∈ X\A, where A := {ϕ1 = −∞} ∪ {ϕ2 = −∞}. The
function v is said to be bounded in X if there exists a constant C such that
|v(x)| ≤ C for every x ∈ X\A.
    We say that v is T -admissible (or admissible with respect to T ) if there
exist quasi-psh functions ϕ1 , ϕ2 on X such that v = ϕ1 − ϕ2 and T has
no mass on {ϕj = −∞} for j = 1, 2. In particular, if T has no mass on
pluripolar sets, then every dsh function is T -admissible. Assume now that
v is T -admissible. The following is a direct consequence of Proposition 2.1
(i).
Lemma 2.3. If v is T -admissible, then v is also admissible with respect to
h m       ˙
 V
   j=1 Tj ∧T i.

   Recall that if v = ϕ1 − ϕ2 for some bounded quasi-psh functions ϕ1 , ϕ2
on X (note X is compact), the current dv ∧ dc v ∧ T is, by definition, equal
to
             1 c
(2.3)          dd (ϕ1 − ϕ2 )2 ∧ T − (ϕ1 − ϕ2 )ddc (ϕ1 − ϕ2 ) ∧ T.
             2
Convexity of the class of currents with finite energy                      5

We notice that in the above formula the function (ϕ1 − ϕ2 )2 is locally the
difference of two bounded psh functions. More precisely, we can assume
ϕj is ω-psh function for j = 1, 2, where ω is a Kähler form on X, and
consider an open local chart U such that ω = ddc φ for some smooth psh
function φ on U. By adding to φ a big constant, we can even assume that
ϕj + φ ≥ 0 on U for j = 1, 2. Thus (ϕj + φ)2 and (ϕ1 + ϕ2 + 2φ)2 are psh
on U for j = 1, 2, and

(2.4)      (ϕ1 − ϕ2 )2 = (2(ϕ1 + φ)2 + 2(ϕ2 + φ)2 ) − (ϕ1 + ϕ2 + 2φ)2

which is the difference of two bounded psh functions on U.
   Consider another dsh function w which is equal to the difference of
two locally bounded psh functions and T is of bi-degree (n − 1, n − 1), we
have
(2.5)
2dv ∧ dc w ∧ T = d(v + w) ∧ dc (v + w) ∧ T − dv ∧ dc v ∧ T − dw ∧ dc w ∧ T.

However, in general, even when v is bounded, v might not be the differ-
ence of two bounded quasi-psh functions. Hence, the current “dv∧dc v∧T ”
is not well-defined in the above sense. We will introduce below the cur-
                ˙ i in the spirit of non-pluripolar products. Before going
rent hdv ∧ dc v ∧T
into details, we need the following auxiliary estimate.

Lemma 2.4. Let ω be a Kähler form on X. Let ϕ1 , ϕ2 be bounded ω-psh
functions on X and v := ϕ1 − ϕ2 . Let T be a closed positive current of bi-
dimension (1, 1) on X. Then, there exists a constant C independent of ϕ1 , ϕ2
such that
                        Z
(2.6)                     dv ∧ dc v ∧ T ≤ CkvkL∞ .
                            X

Proof. We have
                   Z                             Z
                                 c
            I :=       dv ∧ d v ∧ T = −                  vddc v ∧ T
                   X
                   Z                                 X

              =−    v(ddc ϕ1 − ddc ϕ2 ) ∧ T
                 ZX                       Z
                        c
              =−    v(dd ϕ1 + ω) ∧ T +      v(ddc ϕ2 + ω) ∧ T
                       X                                  X
                           2 Z
                           X
              ≤ kvkL∞                    (ddc ϕj + ω) ∧ T
                           j=1       X
                           Z
              = 2kvkL∞               T ∧ω
                             X
6                                                                      Duc- Viet Vu

by Stokes’ theorem. The desired estimate follows. The proof is finished.


    Assume now that v is T -admissible. Let ϕ1 , ϕ2 be quasi-psh functions
such that v = ϕ1 − ϕ2 and T has no mass on {ϕj = −∞} for j = 1, 2. Let
ϕj,k := max{ϕj , −k} for every j = 1, 2 and k ∈ N. Put vk := ϕ1,k − ϕ2,k .
Since vk is the difference of two bounded quasi-psh functions, using (2.3),
we obtain

                Qk := dvk ∧ dc vk ∧ T = ddc vk2 ∧ T − vk ddc vk ∧ T.

Let ω be a Kähler form so that ϕj is ω-psh for j = 1, 2. Let U be a local
chart on X such that ω = ddc φ on U for some psh function φ such that
ϕj,k + φ ≥ 0 on U for j = 1, 2 (we fix k). By (2.4) applied to ϕj,k + φ, we
have

Qk = 2ddc (ϕ1,k + φ)2 ∧ T + 2ddc (ϕ2,k + φ)2 ∧ T − ddc (ϕ1,k + ϕ2,k + 2φ)2 ∧ T
        − (vk ddc ϕ1,k ∧ T − vk ddc ϕ2,k ∧ T )

on U. By the plurifine locality with respect to T ([14, Theorem 2.9]) ap-
plied to each term in the right-hand side of the last equality, we have

(2.7)                   1T2j=1 {ϕj >−k} Qk = 1T2j=1 {ϕj >−k} Qk′

for every k ′ ≥ k.
                          ˙ i is well-defined if the mass of 1T2 {ϕ >−k} Qk
   We say that hdv ∧ dc v ∧T                                   j=1  j

on X is bounded uniformly in k. In this case, using (2.7) implies that there
exists a positive current Q on X such that for every bounded Borel form
Φ on X, we have

                        hQ, Φi = lim h1T2j=1 {ϕj >−k} Qk , Φi.
                                   k→∞

                      ˙ i to be the current Q. This agrees with the classical
We define hdv ∧ dc v ∧T
definition if v is the difference of two bounded quasi-psh functions. This
definition is independent of the choice of ϕ1 , ϕ2 by Lemma 2.5 below. If w
is another T -admissible dsh function and T is of bi-dimension (1, 1) such
                             ˙ i, hdw ∧ dcw ∧T
that the currents hdv ∧ dc v ∧T             ˙ i, and hd(v + w) ∧ dc(v + w)∧T
                                                                          ˙ i
                                         c ˙
are all well-defined, we define hdv ∧ d w ∧T i using (2.5) formally.
Lemma 2.5. Let ϕ′1 , ϕ′2 be quasi-psh functions on X such that v = ϕ′1 − ϕ′2
and T has no mass on {ϕ′j = −∞} for j = 1, 2. Let ϕ′j,k , Q′k be the func-
tion and current associated to ϕ′j defined similarly as ϕj,k and Qk respec-
tively. Then if 1T2j=1 {ϕj >−k} Qk is of mass bounded uniformly on k then so is
Convexity of the class of currents with finite energy                                    7

1T2j=1 {ϕ′j >−k} Q′k , and

(2.8)                        Q = lim h1T2j=1 {ϕ′j >−k}Q′k , Φi
                                  k→∞

for every bounded Borel form Φ on X.

Proof. Since v = ϕ′1 − ϕ′2 , we get

                                  ϕ1 + ϕ′2 = ϕ′1 + ϕ2 .

Put vk′ := ϕ′1,k − ϕ′2,k , A′k := 2j=1 {ϕ′j > −k}, and Ak := 2j=1 {ϕj > −k}.
                                 T                            T

We have Q′k = dvk′ ∧ dc vk′ ∧ T , and vk = vk′ on Ak ∩ A′k which is open in the
plurifine topology. We claim that

(2.9)                           1Ak ∩A′k Q′k = 1Ak ∩A′k Qk .

This is a sort of plurifine locality statement and can be essentially de-
duced from the plurifine locality for bounded psh functions (here we have
vk = vk′ on Ak ∩ A′k but vk , vk′ are only dsh). We give details for readers’
convenience. Before doing so, we will show that the desired assertion is a
direct consequence of (2.9). First observe that 1A′k Q′k has no mass on the
pluripolar set {ϕj = −∞} for j = 1, 2 by Proposition 2.1 (i) and the fact
that T has no mass on {ϕj = −∞}. It follows that

                    1A′k Q′k = lim 1A′k ∩As Q′k
                                s→∞
                             = lim 1A′k ∩As Q′s
                                s→∞
                             ≤ lim 1A′s ∩As Q′s
                                s→∞
                             = lim 1A′s ∩As Qs ≤ lim 1As Qs = Q,
                                s→∞                 s→∞

where we used (2.7) applied to Q′k in the second equality and (2.9) in the
third equality. By exchanging the role of Q′k and Qk , we also obtain that

                                      1Ak Qk ≤ R,

for every limit current R of (1A′k Q′k )k as k → ∞. Hence (2.8) follows.
   We go back to the proof of (2.9). Write

dvk ∧ dc vk ∧ T = dvk ∧ dc (vk − vk′ ) ∧ T + d(vk − vk′ ) ∧ dc vk′ ∧ T + dvk′ ∧ dc vk′ ∧ T.

Denote by R1 , R2 the first and second currents in the right-hand side of
the last equality. In order to obtain (2.9), it suffices to check that Rj = 0
8                                                                    Duc- Viet Vu

on Ak ∩ A′k for j = 1, 2. Observe

     R1 = dvk ∧ dc (ϕ1,k + ϕ′2,k − ϕ′1,k − ϕ2,k ) ∧ T
        = dϕ1,k ∧ dc (ϕ1,k + ϕ′2,k ) ∧ T − dϕ1,k ∧ dc (ϕ′1,k + ϕ2,k ) ∧ T −
                                                                         

          dϕ2,k ∧ dc (ϕ1,k + ϕ′2,k ) ∧ T − dϕ2,k ∧ dc (ϕ′1,k + ϕ2,k ) ∧ T .
                                                                        


Each term in the right-hand side of the above equality is equal to 0 on
Ak ∩ A′k thanks to the plurifine locality and the fact that

               ϕ1,k + ϕ′2,k = ϕ1 + ϕ′2 = ϕ′1 + ϕ2 = ϕ′1,k + ϕ2,k

on Ak ∩ A′k . Hence R1 = 0 on Ak ∩ A′k . Similarly we get R2 = 0 on Ak ∩ A′k .
This finishes the proof.
                                                                  ˙ i is
Lemma 2.6. Assume that v is bounded. Then, the current hdv ∧ dc v ∧T
well-defined.

Proof. Let the notation be as in the proof of Lemma 2.4. Let ω be a Kähler
form on X such that ϕ1 , ϕ2 are ω-psh. Note that ϕjk is also ω-psh for every
j, k. Observe that since v is bounded, there exists a constant C such that
ϕ2 − C ≤ ϕ1 ≤ ϕ2 + C. Thus, there exists a constant C so that

                                 kvk kL∞ ≤ C

for every k. Using this and Lemma 2.4, one gets

                             kQk k . kvk kL∞ ≤ C

for some constant C independent of k. Hence, the desired assertion fol-
lows. This finishes the proof.

      Let T1 , . . . , Tm be closed positive (1, 1)-currents on X and R := hT1 ∧
           ˙ i. We define
· · · ∧ Tm ∧T

               hdv ∧ dc v ∧ T1 ∧ · · · ∧ Tm ∧T
                                            ˙ i := hdv ∧ dc v ∧Ri.
                                                              ˙

When T ≡ 1, we write the left-hand side of the last equality simply as
hdv ∧ dc v ∧ T1 ∧ · · · ∧ Tm i.
                                            ˙ i is defined similarly if p + m =
   The current hdv ∧ dc w ∧ T1 ∧ · · · ∧ Tm ∧T
n − 1, where T is of bi-degree (p, p). We put

                   hddc v ∧T
                          ˙ i := hddc ϕ1 ∧T
                                         ˙ i − hddcϕ2 ∧T
                                                      ˙ i.

Define
                   hddc v ∧ T1 ∧ · · · ∧ Tm ∧T
                                            ˙ i := hddc v ∧Ri.
                                                          ˙
Convexity of the class of currents with finite energy                            9

   By Proposition 2.1 (iii), this definition agrees with the T -relative non-
pluripolar product of ddc v, T1 , . . . , Tm if v is quasi-psh. When T ≡ 1, we
                                                              ˙ i. In this case the
write hddc v ∧ T1 ∧ · · · ∧ Tm i for hddc v ∧ T1 ∧ · · · ∧ Tm ∧T
product hddc v ∧ T1 ∧ · · · ∧ Tm i is the one defined in the paragraph right
after Theorem 1.2 in [12].
   By admissibility and Proposition 2.1 (ii), we can check that if v, w are
dsh functions which are admissible with respect to T , then

                    hddc (v + w)∧T
                                ˙ i = hddc v ∧T
                                             ˙ i + hddcw ∧T
                                                         ˙ i.

   Here is an integration by parts formula for relative non-pluripolar prod-
ucts.
Theorem 2.7. Let T be a closed positive current of bi-degree (n − 1, n − 1)
on X. Let v, w be bounded T -admissible dsh functions on X. Then, we have
              Z                Z                   Z
                     c ˙
(2.10)           whdd v ∧T i =   vhdd w ∧T i = − hdw ∧ dc v ∧T
                                       c ˙                     ˙ i.
                X                  X                      X

   The last result was proved in [4, Theorem 1.14] if v, w can be written
as the differences of psh functions which are locally bounded outside a
closed locally complete pluripolar set; see also [1, 13].

Proof. We use ideas from the proof of [14, Proposition 4.2]. Let ϕ1 , ϕ2 , ϕ3 , ϕ4
be negative quasi-psh functions on X such that v = ϕ1 −ϕ2 and w = ϕ3 −ϕ4
and T has no mass on 4j=1 {ϕj = −∞}. Let ω be a Kähler form on X such
                       S

that ϕj is ω-psh for every 1 ≤ j ≤ 4. Put

           ψ := ϕ1 + ϕ2 + ϕ3 + ϕ4 ,       ψk := k −1 max{ψ, −k} + 1.

and ϕjk := max{ϕj , −k} for 1 ≤ j ≤ 4. Observe that 0 ≤ ψk ≤ 1. Let x ∈ X
such that ψk (x) > 0. We have

                ϕ1 (x) + ϕ2 (x) + ϕ3 (x) + ϕ4 (x) = ψ(x) > −k.

This combined with the property that ϕj ≤ 0 for every 1 ≤ j ≤ 4 yields
that ϕj (x) > −k for every 1 ≤ j ≤ 4. We infer that
                                         4
                                         \
(2.11)                     {ψk 6= 0} ⊂       {ϕj > −k}.
                                         j=1


   Put vk := ϕ1k − ϕ2k and wk := ϕ3k − ϕ4k . Since v and w are bounded,
the functions vk , wk are bounded uniformly in k.
10                                                                      Duc- Viet Vu

              S4
   Let A :=    j=1 {ϕj = −∞}. By admissibility and Proposition 2.1 (i), we
see that

(2.12)                       1A h(ddcϕj + ω)∧T
                                            ˙ i = 0.

Using (2.12), we can consider w as a bounded function with respect to the
                              ˙ i. Using (2.11), we have
trace measure of h(ddc ϕj + ω)∧T

      wψk ddc ϕjk ∧ T = w1{ϕj >−k} ψk hddc ϕj ∧T
                                              ˙ i
                         = whddc ϕj ∧T
                                    ˙ i + w(1{ϕj >−k} ψk − 1)hddcϕj ∧T
                                                                    ˙ i.

The second term in the right-hand side of the last equality converges
weakly to 0 as k → ∞ by the fact that ψk → 1 pointwise outside A as
k → ∞ and Lebesgue’s dominated convergence theorem. Hence

                       whddcϕj ∧T
                               ˙ i = lim wψk ddc ϕjk ∧ T.
                                          k→∞

Applying the last equality to j = 1, 2, and using v = ϕ1 − ϕ2 , we obtain

(2.13)        whddcv ∧T
                     ˙ i = lim wψk ddc vk ∧ T = lim wk ψk ddc vk ∧ T.
                               k→∞                            k→∞

Here in the second equality we used the fact that w = wk on {ϕ3 > −k} ∩
{ϕ4 > −k} which contains {ψk 6= 0}. We also have an analogous formula
by exchanging the roles of v, w. Thus,

(2.14)    whddcv ∧T
                 ˙ i − vhddc w ∧T
                               ˙ i = lim ψk (wk ddc vk − vk ddc wk ) ∧ T.
                                                    k→∞

By integration by parts for bounded psh functions, we have
         Z                                     Z
                      c          c
(2.15)       ψk (wk dd vk − vk dd wk ) ∧ T = −    wk dψk ∧ dc vk ∧ T +
           X                                    X
                                                      Z
                                                         vk dψk ∧ dc wk ∧ T.
                                                                    X

Denote by I1 , I2 the first and second term in the right-hand side of the
last equality. We will check that Ij → 0 as k → ∞ for j = 1, 2. Using the
Cauchy-Schwarz inequality, the boundedness of vk , wk and Lemma 2.4, we
infer
               Z                   21  Z                        21
                            c                     2       c
       |I1 | ≤      dψk ∧ d ψk ∧ T     ×     |wk | dvk ∧ d vk ∧ T
                   X                                      X
               Z                         21
           .           dψk ∧ dc ψk ∧ T          .
                   X
Convexity of the class of currents with finite energy                       11

Recall that {limk→∞ ψk < 1} is equal to the complete pluripolar set {ψ =
−∞}. Using this, Theorem 2.2 and the fact that T has no mass on {ψ =
−∞}, we get

           lim dψk ∧ dc ψk ∧ T = lim (ddc ψk2 − ψk ddc ψk ) ∧ T = 0
           k→∞                     k→∞

Thus we obtain

(2.16)                            lim I1 = 0.
                                 k→∞

By similarity, we also get I2 → 0 as k → ∞. Combining this with (2.15)
and (2.13) gives the first desired equality of (2.10). We prove the second
one similarly as follows. Put u := v + w, and

               uk := max{ϕ1 + ϕ3 , −k} − max{ϕ2 + ϕ4 , −k}.

By (2.11) observe that

             1{ψk >0} max{ϕ1 + ϕ3 , −2k} = 1{ψk >0} (ϕ1k + ϕ3k )

and a similar equality for ϕ2 , ϕ4 also holds. Thus, by plurifine locality, we
get

2hdv ∧ dc w ∧T
            ˙ i = hdu ∧ dc u∧T
                            ˙ i − hdv ∧ dc v ∧T
                                             ˙ i − hdw ∧ dc w ∧T
                                                              ˙ i
                 = lim ψk hdu2k ∧ dc u2k ∧T
                                         ˙ i − hdvk ∧ dc vk ∧T
                                                            ˙ i−
                   k→∞
                  hdwk ∧ dc wk ∧T
                               ˙ i
                                   

                 = lim ψk hd(vk + wk ) ∧ dc (vk + wk )∧T
                                                      ˙ i − hdvk ∧ dc vk ∧T
                                                                         ˙ i−
                   k→∞
                  hdwk ∧ dc wk ∧T
                               ˙ i .
                                  


Consequently

                  hdv ∧ dc w ∧T
                             ˙ i = lim ψk hdvk ∧ dc wk ∧T
                                                       ˙ i.
                                    k→∞

It follows that
  Z                                      Z
          c ˙              c ˙
      vhdd w ∧T i + hdv ∧ d w ∧T i = lim    ψk (vk ddc wk + dvk ∧ dc wk ) ∧ T
    X                                k→∞ X
                                           Z
                                   = − lim    vk dψk ∧ dc wk ∧ T
                                         k→∞    X

which is equal to 0 by analogous arguments as in the proof of (2.16). This
finishes the proof.
12                                                                                          Duc- Viet Vu

Corollary 2.8. Let v, w be bounded dsh functions on X. Then, for every
closed smooth form Φ of right bi-degree, we have
            Z                  m
                               ^                  Z                      m
                                                                         ^
                        c                                    c
(2.17)              whdd v ∧         Tj i ∧ Φ =           vhdd w ∧             Tj i ∧ Φ =
                X              j=1                    X                  j=1
                                                                     Z                      m
                                                                                            ^
                                                                                    c
                                                                 −        hdv ∧ d w ∧             Tj i ∧ Φ.
                                                                     X                      j=1

Proof. By writing Φ as the difference of two closed positive forms, we can
assume that Φ is positive. The desired formula is a direct consequence of
Theorem 2.7 applied to T := hT1 ∧ · · · ∧ Tm i ∧ Φ.

    We recall that the first inequality of (2.17) was proved in [12, Theorem
1.2] and [16] when m = n and the cohomology classes of Tj ’s are big.
One should notice a crucial point that the integration by parts formulae
obtained in [12, 16] contain no term involving dv ∧ dc w. Such a term is
essential in applications, especially, in the pluricomplex energy theory. The
following result is more general than Theorem 2.7. We will need it later.
Theorem 2.9. Let T a closed positive current of bi-degree (n − 1, n − 1) on
X. Let v, w be bounded T -admissible dsh functions on X. Let χ : R → R be
a C 3 function. Then we have
(2.18)
   Z                   Z                        Z
                           ′′
             c ˙
      χ(w)hdd v ∧T i =                c ˙
                         vχ (w)hdw ∧ d w ∧T i +   vχ′ (w)hddcw ∧T
                                                               ˙ i.
        X                            X                                          X

   A quick heuristic reason explaining why (2.18) should hold is because
dd χ(w) = χ′′ (w)dw∧dc w+χ′ (w)ddcw if w is a bounded quasi-psh function.
    c


Proof. We first note that [14, Lemma 5.7] still holds for dsh functions
which are the differences of two bounded quasi-psh functions. Now, to
obtain the desired equality, we just follow the proof of Theorem 2.7 ver-
batim with χ(w) in place of w. The only thing we need to clarify is the
computation concerning ddc χ(wk ) ∧ T . To this end, it suffices to use [14,
Lemma 5.7] because wk is the difference of two bounded quasi-psh func-
tions. This finishes the proof.


```

## Primary unit 13: Vu-2005.13241v3-20261004.txt, LF656--827

Literal SHA256 `7c4a6f848d72b6bc891d56b0cdf8b543bf9c1522324504029100073e1d6b9ba9`; supplied pin matches: True.

```text
3       Currents with finite relative energy
Let X be a compact Kähler manifold. Let α1 , . . . , αm be pseudoeffective
(1, 1)-classes of X and T a closed positive current on X. Let Pj be a closed
Convexity of the class of currents with finite energy                                 13

positive (1, 1)-current in the class αj for 1 ≤ j ≤ m. Put P := (P1 , . . . , Pm ).
We define EP (T ) to be the set of m-tuple (T1 , . . . , Tm ) of closed positive
(1, 1)-currents such that Tj ∈ αj and Tj is more singular than Pj and
                                m
                                ^                     m
                                                      ^
                           {h            ˙ i} = {h
                                      Tj ∧T                    ˙ i}.
                                                            Pj ∧T
                                j=1                   j=1

Notice that for every current Pj′ in αj such that Pj′ has the same singular-
ities as Pj for 1 ≤ j ≤ m, by the monotonicity of relative non-pluripolar
products (see (1.1)), we have

                                       EP (T ) = EP′ (T ).

Hence, when Pj has minimal singularities in αj for 1 ≤ j ≤ m, we recover
the class E(α1 , . . . , αm , T ) of currents of full mass intersection introduced
in [14, 4] because we have

                             EP (T ) = E(α1 , . . . , αm , T )

in this case.
    Let χ ∈ W − . Write Pj = ddc ϕj + θj , where θj is a smooth form and ϕj is
a negative θj -psh function. Let (T1 , . . . , Tm ) ∈ EP (T ). Let uj be a negative
θj -psh function so that Tj = ddc uj + θj and uj ≤ ϕj for 1 ≤ j ≤ m. For a
negative Borel function ξ, we put
                                           XZ       ^         ^
(3.1)       Eξ,P (T1 , . . . , Tm ; T ) :=     −ξ      Tj ∧         ˙ ,
                                                                 Pj ∧T
                                             J    X          j∈J       j6∈J

where the sum is taken over every subset J of {1, . . . , m}. The (T, P)-
relative joint χ-energy of T1 , . . . , Tm is, by definition, Eξ,P (T1 , . . . , Tm ; T ),
where
                                                             
                    ξ := χ (u1 − ϕ1 ) + · · · + (um − ϕm ) .
The last energy depends on the choice of uj , ϕj but its finiteness does not.
That notion generalizes those in [4, 11, 14], see also [5] for the local
setting.
    For every closed positive (1, 1)-current P , let IP be the set of x ∈ X so
that the potentials of P are equal to −∞ at x. Note that IP is a complete
pluripolar set. By Proposition 2.1 (iv), the right-hand side of (3.1) remains
unchanged if we replace T by 1X\ Sm         j=1 IPj
                                                    T . Hence, in practice, we can
                             Sm
assume T has no mass on j=1 IPj . We denote by Eχ,P (T ) the subset of
EP (T ) containing every (T1 , . . . , Tm ) such that their (T, P)-relative joint
χ-energy is finite.
14                                                                                   Duc- Viet Vu

   Here is a monotonicity for the class Eχ,P (T ) when Pj = P for every
1 ≤ j ≤ m. This generalizes [14, Theorem 5.8].
Theorem 3.1. Let P = ddc ϕ + θ be a closed positive (1, 1)-current and P :=
(P, . . . , P ) (m times P ). Let χ ∈ W − with |χ(0)| ≤ 1. Let (T1 , . . . , Tm ) ∈
Eχ,P (T ) and (T1′ , . . . , Tm′ ) ∈ EP (T ) such that Tj = ddc uj + θ, Tj′ = ddc u′j + θ
such that uj , u′j are θ-psh and uj ≤ u′j ≤ ϕ. Put
                                                                
                           ξ := χ (u1 − ϕ) + · · · + (um − ϕ) .

Then we have

                 Eξ (T1′ , . . . , Tm′ ; T ) ≤ c1 Eξ (T1 , . . . , Tm ; T ) + c2 ,

for some constants c1 , c2 > 0 independent of χ. In particular, (T1′ , . . . , Tm′ ) ∈
Eχ,P (T ).

Proof. As mentioned above, we can assume that T has no mass on IP =
{ϕ = −∞}. Note here that {ϕ = −∞} ⊂ {uj = −∞}. Put

                               ujk := max{uj , ϕ − k} − ϕ

which is a bounded dsh function and

                                    Tjk := ddc ujk + P.

Observe that ujk ’s are admissible with respect to T . Define u′jk , Tjk
                                                                      ′
                                                                         simi-
larly. Put
                    m
                    X
             v :=         (uj − ϕj ),    vk := max{v, −k},             ξk = χ(vk ).
                    j=1

Note that ξ = χ(v). With these notations and a suitable integration by
parts ready in our hands (Theorem 2.9) replacing [14, Lemma 5.7]), the
proof goes exactly as in the proof of [14, Theorem 5.8]. The only minor
modifications are: the Kähler form ω is substituted by P and the wedge
products appearing in the proof of [14, Theorem 5.8] need to be replaced
by T -relative non-pluripolar products. This finishes the proof.

     The following is a direct consequence of Theorem 3.1.
Corollary 3.2. Let P, P be as in Theorem 3.1. Let P ′ be a current in {P }
which is of the same singularity type as P . Then, for P′ = (P ′ , . . . , P ′) (m
times P ′), we have
                            Eχ,P′ (T ) = Eχ,P(T ).
Convexity of the class of currents with finite energy                            15

   For every closed positive (1, 1)-current P , we define the class Em,P (T )
(resp. Eχ,m,P (T )) to be the set of currents T1 ∈ {P } such that (T1 , . . . , T1 )
belongs to EP (T ) (resp. Eχ,P (T )), where P = (P, . . . , P ) (m times P ). The
last space was introduced in [6] when T is the constant function equal
to 1. As in the case of the usual class of currents of full mass intersection
([11, Proposition 2.2]), notice that
                                          [
                           Em,P (T ) =           Eχ,m,P (T ).
                                         χ∈W −


Let α be a pseudoeffective (1, 1)-class. By Corollary 3.2, we see that the
notion of the weighted class Eχ,m,P (T ) makes sense if we replace P by its
equivalent class (in terms of singularity type) of (1, 1)-currents. Hence,
we can define Em (α, T ) (resp. Eχ,m(α, T )) to be the set Em,P (T ) (resp.
Eχ,m,P (T )), where P is a current with minimal singularities in α.
Theorem 3.3. Let U be an open subset in Cn . Let T be a closed positive
current on U and uj , u′j bounded psh functions on U for 1 ≤ j ≤ m, where
m ∈ N. Let vj , vj′ be psh functions on U for 1 ≤ j ≤ q. Assume that uj = u′j
on W := qj=1 {vj > vj′ } for 1 ≤ j ≤ m. Then we have
         T


(3.2)       1W ddc u1 ∧ · · · ∧ ddc um ∧ T = 1W ddc u′1 ∧ · · · ∧ ddc u′m ∧ T.

Proof. If vj , vj′ are all bounded, then the desired assertion is Theorem 2.9
in [14]. In general, observe that
                                          ∞
                                          [
                          {vj > vj′ } =               ′
                                              {vjk > vjk },
                                          k=1

                                             ′
                                                . Let Wk := qj=1 {vjk > vjk
                                                                         ′
                                                           T
where vjk := max{vj , −k} and similarly for vjk                             }.
                    S∞             ′
We have W = k=1 Wk and uj = uj on Wk . Applying [14, Theorem 2.9]
to uj , u′j , Wk gives

         1Wk ddc u1 ∧ · · · ∧ ddc um ∧ T = 1Wk ddc u′1 ∧ · · · ∧ ddc u′m ∧ T

for every k. Hence, the desired assertion follows. This finishes the proof.


   Now, using Theorems 3.1 and 3.3 instead of [14, Theorem 5.8] and
[14, Theorem 2.9] respectively, and following arguments in the proof of
[14, Theorems 5.9 and 5.1], we immediately obtain the following result.

Theorem 3.4. For χ ∈ W − , the sets Eχ,m,P (T ) and Em,P (T ) are convex.
16                                                              Duc- Viet Vu

     Finally, we would like to make the following comment.
                    +
Remark 3.5. Let WM     be the class of weights introduced in [11, Page 462].
Using arguments from the proof of [11, Lemma 3.5] and that of Theorem
                                                        +
3.4, we can prove the convexity of Eχ,m,P (T ) for χ ∈ WM .


Acknowledgements
The author would like to thank referees for their remarks improving the
presentation of the paper.


```

## Primary unit 14: Vu-2005.13241v3-20261004.txt, LF828--884

Literal SHA256 `d0915796895621146bb871da1cea5244607f9d37b9146f2d202a099a9eb96e7f`; supplied pin matches: True.

```text
References
 [1] E. B EDFORD AND B. A. TAYLOR, A new capacity for plurisubharmonic
     functions, Acta Math., 149 (1982), pp. 1–40.

 [2]       , Fine topology, Šilov boundary, and (ddc )n , J. Funct. Anal., 72
       (1987), pp. 225–251.

 [3] R. J. B ERMAN , S. B OUCKSOM , V. G UEDJ , AND A. Z ERIAHI , A vari-
     ational approach to complex Monge-Ampère equations, Publ. Math.
     Inst. Hautes Études Sci., 117 (2013), pp. 179–245.

 [4] S. B OUCKSOM , P. E YSSIDIEUX , V. G UEDJ , AND A. Z ERIAHI , Monge-
     Ampère equations in big cohomology classes, Acta Math., 205 (2010),
     pp. 199–262.

 [5] U. C EGRELL, Pluricomplex energy, Acta Math., 180 (1998), pp. 187–
     217.

 [6] T. DARVAS , E. D I N EZZA , AND C. H. LU, Monotonicity of nonpluripo-
     lar products and complex Monge-Ampère equations with prescribed sin-
     gularity, Anal. PDE, 11 (2018), pp. 2049–2087.

 [7]        , On the singularity type of full mass currents in big cohomology
       classes, Compos. Math., 154 (2018), pp. 380–409.

 [8] T. DARVAS , E. D I N EZZA , AND C. H. LU, Log-concavity of volume and
     complex Monge-Ampère equations with prescribed singularity, Math.
     Ann., 379 (2021), pp. 95–132.
Convexity of the class of currents with finite energy                 17

 [9] T.-C. D INH AND N. S IBONY, Distribution des valeurs de transforma-
     tions méromorphes et applications, Comment. Math. Helv., 81 (2006),
     pp. 221–258.

[10] D. T. D O AND D.-V. V U, Complex Monge-Ampère equations with solu-
     tions in finite energy classes. arXiv:2010.08619, 2020. to appear in
     Math. Res. Lett.

[11] V. G UEDJ AND A. Z ERIAHI, The weighted Monge-Ampère energy
     of quasiplurisubharmonic functions, J. Funct. Anal., 250 (2007),
     pp. 442–482.

[12] C. H. LU, Comparison of Monge-Ampère capacities, Ann. Polon. Math.,
     126 (2021), pp. 31–53.

[13] N. S IBONY, Quelques problèmes de prolongement de courants en anal-
     yse complexe, Duke Math. J., 52 (1985), pp. 157–197.

[14] D.-V. V U, Relative non-pluripolar product of currents, Ann. Global
     Anal. Geom., 60 (2021), pp. 269–311.

[15] D. W ITT N YSTRÖM, Monotonicity of non-pluripolar Monge-Ampère
     masses, Indiana Univ. Math. J., 68 (2019), pp. 579–591.

[16] M. X IA, Integration by parts formula for non-pluripolar products.
     arXiv:1907.06359, 2019.

```

## Primary unit 15: BEGZ-0812.3674v2-20261004.txt, LF180--248

Literal SHA256 `a9817dcf1e66414e9b0e6754baddfda52b4dd76cef4a5e046e4d5ad390a3252e`; supplied pin matches: True.

```text

on X as a closed positive (p, p)-current. The wedge product only depends on
the closed positive (1, 1)-currents ddc uj , and not on the speciﬁc choice of the
potentials uj .
   A very important property of this construction is that it is local in the plurifine
topology, in the following sense. If uj , vj are locally bounded psh functions on X
and uj = vj (pointwise) on a pluriﬁne open subset O of U , then
                   1O ddc u1 ∧ ... ∧ ddc up = 1O ddc v1 ∧ ... ∧ ddc vp .
This is indeed an obvious generalization of Corollary 4.3 of [4].
   In the case of a possibly unbounded psh function u, Bedford-Taylor have ob-
served (cf. p.236 of [4]) that it is always possible to deﬁne the non-pluripolar
part of the would-be positive measure (ddc u)n as a Borel measure. The main
issue however is that this measure is not going to be locally ﬁnite in general (see
Example 1.3 below). More generally, suppose we are trying to associate to any
p-tuple u1 , ..., up of psh functions on X a positive (a priori not necessarily closed)
(p, p)-current
                                   hddc u1 ∧ ... ∧ ddc up i
putting no mass on pluripolar subsets, in such a way that the construction is
local in the pluriﬁne topology in the above sense. Then we have no choice: since
uj coincides with the locally bounded psh function max(uj , −k) on the pluriﬁne
open subset                               \
                                   Ok := {uj > −k},
                                          j
we must have              ^               ^
                     1Ok h ddc uj i = 1Ok   ddc max(uj , −k),                    (1.1)
                            j                  j
Note that the
            V right-hand side is non-decreasing in k. This equation completely
determines h j ddc uj i since the latter is required not to put mass on the pluripolar
        S
set X − k Ok = {u = −∞}.
Definition 1.1. If u1 , ..., up are psh functions
                                             V on the complex manifold X, we
shall say that the non-pluripolar product h j ddc uj i is well-defined on X if for
each compact subset K of X we have
                      Z                ^
                  sup          ω n−p ∧   ddc max(uj , −k) < +∞               (1.2)
                     k   K∩Ok            j
for all k.
   Here ω is an auxiliary (strictly) positive (1, 1)-form on X with respect to which
masses are being measured, the condition being of course independent ofV   ω. When
(1.2) is satisﬁed, equation (1.1) indeed deﬁnes a positive (p, p)-current h j ddc uj i
on X. We will show below that it is automatically closed (Theorem 1.8).
   Condition (1.2) is always satisﬁed when p = 1, and in fact it is not diﬃcult to
show that
                               hddc ui = 1{u>−∞} ddc u.
There are however examples where non-pluripolar products are not well-deﬁned
as soon as p ≥ 2. This is most easily understood in the following situation.
6                 S. BOUCKSOM, P. EYSSIDIEUX, V. GUEDJ, A.ZERIAHI

Definition 1.2. A psh function u on X will be said to have small unbounded
locus if there exists a (locally) complete pluripolar closed subset A of X outside
which u is locally bounded.
   Assume that u1 , ..., up have small unbounded locus, and let A be closed com-
plete pluripolar such that each uj is locally bounded outside A V
                                                                (recall that com-
plete pluripolar subsets are stable under ﬁnite unions). Then h j ddc uj i is well-
                                          V
deﬁned iﬀ the Bedford-Taylor product j ddc uj , which is deﬁned on the open
                                                                        V
subset X −A, has locally ﬁnite mass near each point of A. In that case h j ddc uj i
                                        V
is nothing but the trivial extension of j ddc uj to X.
Example 1.3. Consider Kiselman’s example (see [32])
                           u(x, y) := (1 − |x|2 )(− log |y|)1/2
for (x, y) ∈ C2 near 0. The function u is psh near 0, it is smooth outside the y = 0
axis, but the smooth measure (ddc u)2 , defined outside y = 0, is not locally finite
near any point of y = 0. This means that the positive Borel measure h(ddc u)2 i is
not locally finite.
```

## Primary unit 16: BEGZ-0812.3674v2-20261004.txt, LF323--477

Literal SHA256 `462891277734fc5ab0efef31d1a327cb2de16257bfdc3ec5f24424db0e67909f`; supplied pin matches: True.

```text
  A crucial point for what follows is that non-pluripolar products of globally
deﬁned currents are always well-deﬁned on compact Kähler manifolds:
Proposition 1.6. Let T1 , ..., Tp be closed positive (1, 1)-currents on a compact
Kähler manifold X. Then their non-pluripolar product hT1 ∧ ... ∧ Tp i is well-
defined.
Proof. Let ω be a Kähler form on X. In view of the third point of Proposi-
tion 1.4, upon adding a large multiple of ω to the Tj ’s we may assume that their
cohomology classes are Kähler classes. We can thus ﬁnd Kähler forms ωj and
ωj -psh functions ϕj such that Tj = ωj + ddc ϕj . Let U be a small open subset of
8                S. BOUCKSOM, P. EYSSIDIEUX, V. GUEDJ, A.ZERIAHI

X on which ωj = ddc ψj , where ψj ≤ 0 is a smooth psh function on U , so that
Tj = ddc uj on U with uj := ψj + ϕj . The bounded psh functions on U
                                           ψj + max(ϕj , −k)
and
                                 max(uj , −k)
coincide on the pluriﬁne open subset {uj > −k} ⊂ {ϕj > −k}, thus we have
                     Z                  ^
                                  n−p
                       T        ω     ∧   ddc max(uj , −k)
                               j {uj >−k}                       j
                     Z                                  ^
                 =       T                ω n−p ∧        (ωj + ddc max(ϕj , −k))
                             j {uj >−k}                     j
                              Z                 ^
                         ≤            ω n−p ∧       (ωj + ddc max(ϕj , −k)).
                                  X             j
But the latter integral is computed in cohomology, hence independent of k, and
this shows that (1.2) is satisﬁed on U , qed.                                
Remark 1.7. The same property extends to the case where X is a compact com-
plex manifold in the Fujiki class, that is bimeromorphic to a compact Kähler
manifold. Indeed there exists in that case a modiﬁcation µ : X ′ → X with
X ′ compact Kähler. Since µ is an isomorphism outside closed analytic (hence
pluripolar) subsets, it is easy to deduce that hT1 ∧ ... ∧ Tp i is well-deﬁned on X
from the fact that hµ∗ T1 ∧ ... ∧ µ∗ Tp i is well-deﬁned on X ′ , and in fact
                         hT1 ∧ ... ∧ Tp i = µ∗ hµ∗ T1 ∧ ... ∧ µ∗ Tp i.
On the other hand it seems to be unknown whether ﬁniteness of non-pluripolar
products holds on arbitrary compact complex manifolds.
  Building on the proof of the Skoda-El Mir extension theorem, we will now
prove the less trivial closedness property of non-pluripolar products.
Theorem 1.8. Let T1 , ..., Tp be closed positive (1, 1)-currents on a complex man-
ifold X whose non-pluripolar product is well-defined. Then the positive (p, p)-
current hT1 ∧ ... ∧ Tp i is closed.
Proof. The result is of course local, and we can assume that X is a small neigh-
borhood of 0 ∈ Cn . The proof will follow rather closely Sibony’s exposition of
the Skoda-El Mir theorem [39], cf. also [18, pp. 159-161].
   Let uj ≤ 0 be a local potential of Tj near 0 ∈ Cn , and for each k consider the
closed positive current of bidimension (1, 1)
                                      ^
                           Θk := ρ ∧    ddc max(uj , −k)
                                                    j

and the pluriﬁne open subset
                                                    \
                                          Ok :=      {uj > −k}
                                                        j
            MONGE-AMPÈRE EQUATIONS IN BIG COHOMOLOGY CLASSES                          9

so that 1Ok Θk converges towards
                                  ρ ∧ hT1 ∧ ... ∧ Tp i
by (1.1). Here ρ is a positive (n − p − 1, n − p − 1)-form with constant coeﬃcients,
so that Θk has bidimension (1, 1). It is enough to show that
                                  lim d (1Ok Θk ) = 0
                                 k→∞
for any choice ofP
                 such a form ρ.
   Let also u := j uj , so that u ≤ −k outside Ok , and set

                                    wk := χ(eu/k ),
where χ(t) is a smooth convex and non-decreasing function of t ∈ R such that
χ(t) = 0 for t ≤ 1/2 and χ(1) = 1. We thus see that 0 ≤ wk ≤ 1 is a non-
decreasing sequence of bounded psh functions deﬁned near 0 ∈ Cn with wk = 0
outside Ok and wk → 1 pointwise outside the pluripolar set {u = −∞}. Finally
let 0 ≤ θ(t) ≤ 1 be a smooth non-decreasing function of t ∈ R such that θ(t) = 0
for t ≤ 1/2 and θ ≡ 1 near t = 1. The functions θ(wk ) are bounded, non-
decreasing in k and we have
                                 θ(wk ) ≤ 1Ok
since θ(wk ) ≤ 1 vanishes outside Ok . Note also that θ ′ (wk ) vanishes outside Ok ,
and converges to 0 pointwise outside {u = −∞}.
   Our goal is to show that
                                 lim d (1Ok Θk ) = 0.
                                 k→∞
But we have
                0 ≤ (1Ok − θ(wk )) Θk ≤ (1 − θ(wk )) hT1 ∧ ... ∧ Tp i,
and the latter converges to 0 by dominated convergence since θ(wk ) → 1 pointwise
outside the polar set of u, which is negligible for hT1 ∧...∧Tp i. It is thus equivalent
to show that
                                lim d (θ(wk )Θk ) = 0.
                                k→∞
Since wk is a bounded psh function, Lemma 1.9 below shows that the chain rule
applies, that is
                       d (θ(wk )Θk ) = θ ′ (wk )dwk ∧ Θk .
Recall that dwk ∧ Θk has order 0 by Bedford-Taylor, so that the right-hand side
makes sense. Now let ψ be a given smooth 1-form compactly supported near 0
and let τ ≥ 0 be a smooth cut-oﬀ function with τ ≡ 1 on the support of ψ. The
Cauchy-Schwarz inequality implies
  Z                     2   Z                      Z                    
      ′                                   c               ′     2
     θ (wk )ψ ∧ dwk ∧ Θk ≤       τ dwk ∧ d wk ∧ Θk       θ (wk ) ψ ∧ ψ ∧ Θk .

But on the one hand we have
                    Z                  Z
                  2 τ dwk ∧ d wk ∧ Θk ≤ τ ddc wk2 ∧ Θk
                             c
10                  S. BOUCKSOM, P. EYSSIDIEUX, V. GUEDJ, A.ZERIAHI
                               Z                      Z
                           =       wk2 ddc τ ∧ Θk =        wk2 ddc τ ∧ Θk
                                                      Ok
since wk vanishes outside Ok , and the last integral is uniformly bounded since
0 ≤ wk ≤ 1 and 1Ok Θk has uniformly bounded mass by (1.2). On the other hand
we have
                   θ ′ (wk )2 Θk = θ ′ (wk )2 1Ok Θk ≤ θ ′ (wk )2 hT1 ∧ ... ∧ Tp i
since θ ′ (wk ) also vanishes outside Ok , and we conclude that
                                       Z
                                 lim      θ ′ (wk )2 ψ ∧ ψ ∧ Θk = 0
                                   k→∞

by dominated convergence since θ ′ (wk ) → 0 pointwise ouside the polar set of u,
which is negligible for hT1 ∧ ... ∧ Tp i. The proof is thus complete.          
Lemma 1.9. Let Θ be a closed positive (p, p)-current on a complex manifold X,
f be a smooth function on R and v be a bounded psh function. Then we have
                                     d(f (v)Θ) = f ′ (v)dv ∧ Θ.
Proof. This is a local result, and we can thus assume that Θ has bidimension (1, 1)
by multiplying it by constant forms as above. The result is of course true when
v is smooth. As we shall see the result holds true in our case basically because v
belongs to the Sobolev space L21 (Θ), in the sense that dv ∧ dc v ∧ Θ is well-deﬁned.
Indeed the result is standard when Θ = [X], and proceeds by approximation.
Here we let vk be a decreasing sequence of smooth psh functions converging
pointwise to v. We then have f (vk )θ → f (v)Θ by dominated convergence, thus
it suﬃces to show that
                               lim f ′ (vk )dvk ∧ Θ = f ′ (v)dv ∧ Θ.
                               k→∞
We write
                                                       
 f ′ (vk )dvk ∧ Θ − f ′ (v)dv ∧ Θ = f ′ (vk ) − f ′ (v) dvk ∧ Θ + f ′ (v)(dvk − dv) ∧ Θ.
Let ψ be a test 1-form and τ ≥ 0 be a smooth cut-oﬀ function with τ ≡ 1 on the
support of ψ. Cauchy-Schwarz implies
                        Z                                   2
                                               
                            f ′ (vk ) − f ′ (v) ψ ∧ dvk ∧ Θ
               Z                                          Z                  
                       ′
                                    2
                                     ′                                      c
           ≤         f (vk ) − f (v) ψ ∧ ψ ∧ Θ                   τ dvk ∧ d vk ∧ Θ .
The second factor is bounded since dvk ∧ dc vk ∧ Θ converges to dv ∧ dc v ∧ Θ by
Bedford-Taylor’s monotone convergence theorem, and the ﬁrst one converges to
0 by dominated convergence. We similarly have
                          Z                            2
                            f ′ (v)(dvk − dv) ∧ ψ ∧ Θ
            Z                     Z                              
                  ′   2                                c
         ≤       f (v) ψ ∧ ψ ∧ Θ        τ d(vk − v) ∧ d (vk − v) ∧ Θ ,
where now the ﬁrst factor is bounded while the second one tends to 0 by Bedford-
Taylor once again, and the proof is complete.                                 
```

## Primary unit 17: BEGZ-0812.3674v2-20261004.txt, LF525--578

Literal SHA256 `0acf2b360d001a14d0fcf47f784424a599506386e6e44bc4b968ddd9bb80dc7d`; supplied pin matches: True.

```text

1.3. Positive cohomology classes. Let X be a compact Kähler manifold and
let α ∈ H 1,1 (X, R) be a real (1, 1)-cohomology class.
   Recall that α is said to be pseudo-effective (psef for short) if it can be repre-
sented by a closed positive (1, 1)-current T . If θ is a given smooth representative
of α, then any such current can be written as T = θ + ddc ϕ, where ϕ is thus a θ-
psh function by deﬁnition, and will sometimes be referred to as a global potential
of T . Global potentials only depend on the choice of θ up to a smooth function
on X.
   On the other hand, α is nef if it lies in the closure of the Kähler cone. Such
a class can thus be represented by smooth forms with arbitrarily small nega-
tive parts, and a compactness argument then shows that α contains a positive
current, i.e. nef implies psef. Note however that the negative part of smooth
representatives cannot be taken to be 0 in general. In fact, Demailly, Peternell
and Schneider have shown in [23] that a classical construction of Serre yields an
example of a smooth curve C on a projective surface whose cohomology class is
nef but contains only one positive current, to wit (the integration current on) C
itself.
   The set of all nef classes is by deﬁnition a closed convex cone in H 1,1 (X, R),
whose interior is none but the Kähler cone. The set of all psef classes also forms a
closed convex cone, and its interior is by deﬁnition the set of all big cohomology
classes. In other words, a class α is big iﬀ it can be represented by a strictly
positive current, i.e. a closed current T that dominates some (small enough)
smooth strictly positive form on X.

1.4. Comparison of singularities. If T and T ′ are two closed positive currents
on X, then T is said to be more singular than T ′ if their global potentials satisfy
ϕ ≤ ϕ′ + O(1). By the singularity type of T , we will mean its equivalence class
with respect to the above notion of comparison of singularities.
   A positive current T in a given psef class α is now said to have minimal
singularities (inside its cohomology class) if it is less singular than any other
positive current in α, and its θ-psh potentials ϕ will correspondingly be said
to have minimal singularities. Such θ-psh functions with minimal singularities
always exist, as was observed by Demailly. Indeed, the upper envelope
                         Vθ := sup {ϕ θ-psh, ϕ ≤ 0 on X}
of all non-positive θ-psh functions obviously yields a positive current
                                     θ + ddc Vθ
with minimal singularities (note that Vθ is usc since Vθ∗ is a candidate in the
envelope).
   We stress that currents with minimal singularities in a given class α are in
general far from unique. Indeed currents with minimal singularities in a class
α admitting a smooth non-negative representative θ ≥ 0 (for instance a Kähler
class) are exactly those with bounded potentials.
   Currents with minimal singularities are stable under pull-back:
            MONGE-AMPÈRE EQUATIONS IN BIG COHOMOLOGY CLASSES                       13

Proposition 1.12. Let π : Y → X be a surjective morphism between compact
Kähler manifolds and θ be a smooth closed (1, 1)-form on X. If ϕ is a θ-psh
function with minimal singularities on X, then the π ∗ θ-psh function ϕ ◦ π also
has minimal singularities.
Proof. Let ψ be a π ∗ θ-psh function. For x ∈ X a regular value of π we set
                                τ (x) := sup ψ(y).
                                         π(y)=x

```

## Primary unit 18: DDNL18-2049-2087-20261004.txt, LF350--369

Literal SHA256 `0d34fd95c9beb603186a5ec408cb5b463d1bdda346042cdc66ac38b25fde6c71`; supplied pin matches: True.

```text
2017, Theorem 4.26] for a proof of this result, which is merely a slight generalization of [Xing 1996,
Theorem 1].

Proposition 2.2. Let  ⊂ Cn be an open set. Suppose { f j } j are uniformly bounded quasicontinuous func-
                                                                                     j         j                  j
tions which converge in capacity to another quasicontinuous function f on . Let {u 1 } j , {u 2 } j , . . . , {u n } j
be uniformly bounded plurisubharmonic functions on , converging in capacity to u 1 , u 2 , . . . , u n respec-
tively. Then we have the following weak convergence of measures:
                                j            j
                         f j i∂ ∂u
                                ¯ ∧ i∂ ∂u
                                   1
                                       ¯ ∧ · · · ∧ i∂ ∂u
                                          2
                                                      ¯ nj → f i∂ ∂u
                                                                  ¯ 1 ∧ i∂ ∂u
                                                                           ¯ 2 ∧ · · · ∧ i∂ ∂u
                                                                                            ¯ n.

   The following lower-semicontinuity property of nonpluripolar products will be key in the sequel:
```

## Primary unit 19: Vu-2004.11111v1-20261004.txt, LF273--287

Literal SHA256 `1ba50d3f123db57547622b7cecbab561eb1cfbe4c81617a290f80b1ec41af8ad`; supplied pin matches: True.

```text
    We now give a definition which will be crucial later. Let (Tk )k be a sequence of
closed positive currents of bi-degree (m, m) on U. We say that (Tk )k satisfies Condition
(∗) if (Tk )k is of uniformly bounded mass on compact subsets of U, and for every open
set U ′ ⊂ U and every bounded psh function u on U ′ and every sequence (uk )k of psh
functions on U ′ decreasing to u, we have

                                   lim (uk − u)(ddc u)m ∧ Tk = 0                          (2.2)
                                k→∞

An obvious example for sequences satisfying Condition (∗) is constant sequences: Tk = T
for every k. We can also take (Tk )k to be a sequence of suitable Monge-Ampère operators
with decreasing potentials, see [1, 10, 15]. Concerning Condition (∗), we will use mostly
the example of constant sequences and the one provided by the following result.
Theorem 2.2. Let S be a closed positive current on U. Let v be a psh function on U such
that v is locally integrable with respect to the trace measure of S and (vk )k a sequence of psh
```

## Primary unit 20: Vu-2005.13241v3-20261004.txt, LF53--78

Literal SHA256 `f47dc8f2ccf80aa64ddf28d987eb8b2ee409d404a0d66a1cfcbced66fd1ed789`; supplied pin matches: True.

```text
(1.1)                             ˙ i} ≤ {hT1′ ∧ · · · ∧ Tm′ ∧T
                {hT1 ∧ · · · ∧ Tm ∧T                         ˙ i}.

The last inequality allows us to define the notion of T -relative full mass
intersection, see [14, 4]. We say that T1 , . . . , Tm are of T -relative full mass
intersection if          m              m
                        ^               ^
                              ˙
                      {h Tj ∧T i} = {h Tj,min∧T       ˙ i},
                         j=1               j=1

where Tj,min is a current with minimal singularities in the class {Tj } for
1 ≤ j ≤ m.
   Let α be a pseudoeffective (1, 1)-class. Denote by Em (α, T ) the set of
currents P ∈ α such that P, . . . , P (m times P ) are of T -relative full mass
intersection.
   Recall that W − is the set of convex increasing functions χ from R to
R such that χ(−∞) = −∞. Let χ ∈ W − . We can define Eχ,m(α, T ) to be
the subclass of Em (α, T ) consisting of P such that P has finite (T -relative)
χ-energy. When T ≡ 1 and m = n, the class Eχ,m (α, T ) generalizes the
usual class of currents with finite energy in [4, 11], see also [5] for the
local setting. We refer to Section 3 for details. For the moment, we note
here that                              [
                         Em (α, T ) =      Eχ,m (α, T ).
                                      χ∈W −

```

## Primary unit 21: DGMS-real-homotopy-1975-stonybrook-20261004.txt, LF1--46

Literal SHA256 `01d1380988cf77b207bc11b0d87fb390f0a331100cbf538de071a64cacfbe3b8`; supplied pin matches: True.

```text
Inventiones math. 29, 2 4 5 - 2 7 4 (1975)
9 by Springer-Verlag 1975




           Real Homotopy Theory of K ihler Manifolds
     Pierre Deligne (Bures-sur-Yvette), Phillip Griffiths* (Cambridge, Mass.),
        John Morgan (NewYork) and Dennis Sullivan (Bures-sur-Yvette)


                                         Table of Contents

                1. Homotopy Theory of Differential Algebras . . . . . . . . . .   248
                2. De Rham Homotopy Theory . . . . . . . . . . . . . . .          254
                3. Relation between De Rham Homotopy Theory and Classical Homo-
                   topy Theory . . . . . . . . . . . . . . . . . . . . . . . .    256
                4. Formality of Differential Algebras . . . . . . . . . . . . . . 260
                5. The De Rham Complex of a Compact K~ihler Manifold . . . . .    262
                6. The Main Theorem and Two Proofs . . . . . . . . . . . . .      270
                7. An Application . . . . . . . . . . . . . . . . . . . . . .     272


    This paper brings together the strengthened de Rham theory of the last author
[12, 13] and [14] concerning the homotopy information of a manifold contained
in the algebra of its differential forms, and the classical results [15] about the
forms on a compact K~ihler manifold to prove statements about the algebraic
topology of compact K~ihler manifolds, and consequently about smooth, complex,
projective algebraic varieties.
    The nature of the results is that the homotopy type of a compact Kiihler manifold,
over the real numbers, is a formal consequence of the real cohomology ring. For any
manifold there is a differential graded algebra with rational structure constants
whose isomorphism type is an invariant of the homotopy type of the space. The
cohomology ring of this differential algebra is the rational cohomology ring of the
space, but the algebra itself contains, for example, the higher order cohomology
products. The isomorphism type of the differential algebra is equivalent to the
"rational form of the nilpotent structure in the space". For a simply connected
manifold this differential algebra is equivalent to the rational Postnikov tower of
manifold. Our results here are that, for a compact K~ihler manifold, from the real
cohomology ring one can produce the real form of this differential algebra. These
 results complement the known structure of the cohomology ring of such a manifold.
 We prove no new results about it.
     The initial motivation for these results was the relation in a K~ihler manifold
 between harmonic forms and holomorphic forms. In particular the (p, 0) harmonic
 forms for any K~ihler metric are exactly the holomorphic forms. Consequently,
 products of (p, 0) and (q, 0) harmonic forms are harmonic l, and thus there are no
```

## Primary unit 22: DGMS-real-homotopy-1975-stonybrook-20261004.txt, LF861--1064

Literal SHA256 `0171c17a073557e342809af894852c1ba92ab5ebda68ee6606ae7371f1f3dc26`; supplied pin matches: True.

```text
                                    (02
On any complex manifold there are positive definite Hermitian metrics
         (~,tl)=S(~,q)+]f~A(~,tl)=(J~,J,)                 for ~ , q 6 T ( M ) .
S and A determine one another. Because of the Hermitian symmetry, S is sym-
metric and A is alternating. Thus S is a Riemannian metric and A is a (1, 1) form
on M. The Hermitian metric is defined to be Kiihler if dA =0, and a Kfihler
manifold is a complex manifold admitting a K~ihler metric. The existence of a
Kiihler metric is a statement of close interaction between the complex structure
and potential theory, and it has many deep consequences for the topology of the
manifold [-15].
    There are several equivalent statements to the definition of a K~ihler metric.
The one given above, which is by now the usual one, has the advantage of making
it obvious that a complex submanifold of a K~ihler manifold is again a K~ihler
manifold. Thus, any smooth, complex projective algebraic variety is K~ihler.
The one which we shall use below is the identity
(5.1)                             Ad=2Ao=2A~=Anc
between the Laplacians of the various operators d, O, ~, d c. It is perhaps worthwhile
to give a few alternate forms of the K~ihler condition, and from these explain how
the identity (5.1) may be proved.
    We shall write an Hermitian metric in the two forms
                            ds 2 = ~ hi, j dzi dS j = ~ col ~)i
                                   i,j                i

where (zl, ..., z,) are local holomorphic coordinates, h = (hi. ~)is a positive Hermitian
matrix, and where col, ..., co, are differential forms of type (1, 0) constituting a C ~~
unitary co-frame for the metric. The associated (1, 1) form is

                              A _ t / ~ - I ~hi, jdzi/,,d~j '
                                         2   L" J "
and our basic definition is, as above:
   (i) The metric is Kiihler if dA =0.
   To give the second definition; we recall the basic theorem in local Hermitian
geometry that there exist unique differential forms co~,j, zg satisfying

                                dcoi= ~ coi, j A co j - t - T , i
                                       J
(5.2)                     co~.j+Nj, i=0,     zi has type (2, 0)
264                                                              P. D e l i g n e   et al.



(c.f. Chern [3]). The vector z =(z 1, ..., z,) is the torsion tensor, and m=(mi.j) gives
the connection matrix for the unique connection Vn in the (1,0) tangent bundle
T' (M) satisfying


                                                        v~'~--~
where ~, tl are C ~ sections of T'(M).
    (Explanations. We are viewing connections as differential operators from
sections to sections tensor l-forms; the connection matrix means relative to the
basis of T ' ( M ) dual to ~oI ..... ~ , ; and finally V~' is the CO, I) component of VH.)
    Our second definition is:
    (ii) The metric is KShler if the torsion z = 0 .
    For our third definition, we consider the standard connection VR in the real
tangent bundle T ( M ) associated to the Riemannian metric underlying the given
Hermitian metric.
    (iii) The metric is KShler if VRJ=0; equivalently, parallel translation should
preserve the almost complex structure.
    Finally, we shall say that the metric is K/~hler in case it osculates to 2nd order
to the flat metric on r More precisely,
    (iv) The metric is KShler if, for each point x e M, there is a holomorphic coordinate
system (zl, ..., z,) centered at x and such that

(5.3)                                                    hi, j(z, -i) = 61. j + [2],

where [2] means terms o f order two or more.
   P r o o f of Equivalence of Definitions. ( i ) ~ (ii) Since A is real, dA = 0 ,=, 0A =0.
Let the (0, 1)-component of o;i,j be ai, j. Then by the basic structure equations,
( 5 . 2 ) , fit)i, j = ~i, j - - 0~j, i'




                             _/2-1
                             -         2   Z(~(--~J'iAOOjA~i)+TIA~I--~O'A(~IJA~i))
                                               i    j

                             _i/U-1
                             -        2    Z'~iA~i--Z(~J'IAO)JAO)i+O)iA~i'J/X~-J)
                                           i                     i,j


                             _I//Z- 1 E zi^ ~//
                                  2    i
                             =0r
    (ii) ~ (iii) Write z i = xi + ~ - lx,+ i, a~i = r + VrZ- 1tp,+ 1 where x~, r                  are real
(using the index range 1 __<i, j _<_n and 1 < a, fl__<2 n). Then
                                                   ds 2 = ~ g~, ~ dx~ dxp = ~ q~, q~,
                                                         ol, ~                               Ot
                         Real Homotopy Theory of Ktihler Manifolds                        265

is the underlying Riemann metric, and by the basic theorem in local Riemannian
geometry there exists a unique matrix tp = (r a) of 1-forms satisfying

                                         dtp~ = Z tp~,t~/x (pp
                                                  #
(5.4)

Here (p is the connection matrix for the Riemannian connection VRapplied to the
dual frame to q01..... ~02,. Comparing the structure Eqs. (5.2) and (5.4), we see
that if r = 0, then upon writing co = co' + ~ 1co" we get
                                           (     co' co"~
                                     tp=       -co" co'l"

This says exactly that, on the complexification Tc(M) _~ T' (M) 9 T'(M), VR= Vn 9 fTn,
which implies that VR commutes with J. (This proof may be given verbally by
stating that the Riemannian and Hermitian connections coincide in the K~thler case.)
     (iii) ~ (iv) First, we observe that (iv) is equivalent to saying that, for each
x e M there is a C ~ coordinate system z = ( q , ..., z,) centered at x which is holo-
morphic to 2nd order. This means that z maps a neighborhood U ofx differentially
to ~", dzl(x) ..... dz,(x) span T~(M), and all ~(dzi)(x)=O, such that (5.3) holds.
Assuming (iii), we let (Xl ..... x2,) be geodesic coordinates centered at x. We may
arrange that at x, J(dxi)= dx,+ i, and then set zi = xl + I F - 1 x,+ i. Since (x~ .... , x2,)
are geodesic coordinates, g,,a = 6,. e + [-2]. Thus the connection matrix for VR is
zero at x, and VRJ=O implies (dJ)(x)=O. It follows that ~(dzi)(x)=O, and (iv)
follows immediately.
     (iv) ~ (i) This is the main point. Given an Hermitian metric satisfying (iv),
we see that
(5.5) Any identity involving the metric and only its first derivatives is valid on
M r162it is valid for the fiat metric on C".
Applying this to the identity dA = 0, which is obviously true on C", we conclude
the equivalence of (i)-(iv).
    We shall discuss how the principle (5.5) may be used to prove (5.1), as well as
some other Ktihler identities. We first consider the commutation relations
(5.6)                              [c5, c~*]= 0 = [O, c5"].
On the face of it these involve second derivatives of the metric, but actually only
first derivatives appear for the reason that mixed partials are equal (think of the
Poisson bracket of vector fields). Thus, (5.6) is valid on a Ktihler manifold since
it is obviously true in if;" (the metric has constant coefficients). Expanding out
the definition of A a now gives
                          & = (~ + 0)(~* + 0") + (~* + 0") (~ + ~)
                             = (0 0* + c~*~3)+ (c~* + c5"0)                        (by (5.6));
or

(5.7)                     Aa = Ae+ A~.
266                                               P. Deligne et al.

From (5.7) we see that An preserves (p, q) type, since this is obviously true for A0
and A~. Thus
(5.8)                                       Ad = j - x Ad J = Ado.

Writing O = 8 9        2- ldC), c3"= 89                                      we see that
                         c3~* + c3"(3= 88(dd* + d * d + d C d ~* + d ~* d ~)
                                           =89                                                     (by (5.8))
Combining this with (5.7) gives (5.1).
   In closing, it is worth noting that the most interesting properties of Kihler
metrics, such as the fact that L(~)=A/x ~ takes harmonic forms to harmonic
forms, are generally proved from the identity
(5.9)                                              [A, d] = d~*
or equivalently
(5.10)                                      [A, 4] = - ~ -                   10*
where A = * L* is the adjoint of L. Now (5.10) obviously involves only 1st derivatives
of the metric and so by (5.5) it will suffice to prove it on ~". This is not too hard
since dzl, ..., dz, gives a flat unitary co-frame; one uses the formulae
                                                                 H




                       cS(fdz I ^ d J ) -- ~ ( - 1)p ~                        dz I A dzj A d2 s,
                                                  jCJ

                      A ( f d z I A dr:J) =          ~     +_fdz I - {k}Adz J- {k}
                                                  kelc~J


                     O * ( f d z I A a S, )j=. L +~~ = - a0 zf       .   i
                                                                             - Ill Aa~
                                                                                     9 J

                                                  i~I      OZi

where I =(il , ..., ip), d z 1 = d z i , A ... A dzi~, etc. and just computes. Using (5.10),
                    0c~* + 0* ~ = 1/~- I(0A~? - 0 2 A + A ~ 2 - c~A0)= 0,
which is (5.6). Similarly, d A = O =~ d~A=O and d ~ * = [ A , d ] = 0 since A A is a
constant. Thus A is harmonic for dc, and hence for d. Further discussion of the
basic Kihler identities is given in Weil's book [15], p. 179-194.
   The main fact we shall use about compact Kihler manifolds is the following
lemma:
(5.11) Lemma ( d d ~ Lemma). I f ~ is a differential form such that d~ = 0 and d~ct=0,
and such that ct=dT, then ~=dd~ fl for some ft.
   Proof If D is one of the operators d, c3, ~, d~ with Laplacian AD, the Hodge
decomposition for the Laplacian gives
(5.12)                      0 = ~eo(q,) + Ao ~o(~ )
where o'r     the harmonic part of ~, is the projection of ~ on ~ o = k e r A o ,
and where the Green's operator G o is AB ~ on Jgo• Suppose that c~=dT. Then by
(5.12)
(5.13)                           e = d d * GaOl.
                          Real Homotopy Theory of K/ihler Manifolds                               267

Since d~c~=0, e=Yfdc(e)+dCd~*Gdc~=d~d~*G,~oe                 because ~ o ( e ) = o ~ f d ( e ) = 0 by
(5.1). Plugging this in (5.13) gives
                                     =dd* Ga(d~d~*Gd~ c~)
                                     =dd~(d * Gd d~*Ge~ ~)                            (using (5.6))
                                     =dd~/~
as required.
(5.14) Remark. This l e m m a holds for real as well as complex forms, since the
validity of a linear statement such as

                              Ker(d) c~ Ker(d c) c~ Im(d) = I m ( d d c)

is unchanged by a field extension.
    F o r complex forms, being d and de-closed is the same as being 0 and ~-closed.
Being ddC-exact is the s a m e as being c~-exact, since ddC= 2 i ~ .
```

## Primary unit 23: GZ-intrinsic-capacities-JGA05-20261004.txt, LF1--62

Literal SHA256 `79017a5f9920f81033635b6acb4e07a15c13b88da6c7dcb986963b3bef36265f`; supplied pin matches: True.

```text
The Journal of Geometric Analysis
Volume 15, Number 4, 2005




     Intrinsic Capacities on Compact K ihler
                   Manifolds
                                       B y Vincent G u e d j a n d A h m e d Zeriahi




       ABSTRACT. We study fine properties of quasiplurisubharmonic functions on compact Kiihler manifolds.
       We define and study several intrinsic capacities which characterize pluripolar sets and show that locally
       pluripolar sets are globally "quasi-pluripolar."



                                                    1. I n t r o d u c t i o n

      Since the fundamental work of Bedford and Taylor [4, 5], several authors have developed
a "Pluripotential theory" in domains of C n (or of Stein manifolds). This theory is devoted to
the fine study of plurisubharmonic (psh) functions and can be seen as a nonlinear generalization
of the classical potential theory (in one complex variable), where subharmonic functions and
the Laplace operator A are replaced by psh functions and the complex Monge-Amp~re operator
                                                                                    i --
(ddC) n. Here d, d c denote the real differential operators d := 0 + 0, d c := ~-[a      - a] so that
dd c = i 0 ~ , the normalization being chosen so that the positive measure (dd c 89log[1 + Ilz112])n
has total mass 1 in C n. We refer the reader to [3, 7, 26] for a survey of this local theory.
      Our aim here is to develop a global Pluripotential theory in the context of compact Kahler
manifolds. It follows from the maximum principle that there are no psh functions (except con-
stants) on a compact complex manifold X. However, there are usually plenty of positive closed
currents of bidegree (1, 1) (we refer the reader to [ 15, Ch. 3], for basic facts on positive currents).
Given co a real closed smooth form of bidegree (1, 1) on X, we may consider every positive closed
current co' of bidegree (1, 1) on X which is cohomologous to 09. When X is K~ihler, it follows
from the "ddC-lemma '' that cot can be written as co' = co + ddC~o, where q9 is a function which
is integrable with respect to any smooth volume form on X. Such a function ~0 will be called
w-plurisubharmonic (w-psh for short). It is globally defined on X and locally given as the sum
of a psh and a smooth function. We let P S H ( X , co) denote the set of w-psh functions. Such
functions were introduced by Demailly, who call them quasiplurisubharmonic (qpsh). These are
the main objects of study in this article.
      There are several motivations to study qpsh functions on compact K~Jaler manifolds. First of
all they arise naturally in complex analytic geometry as positive singular metrics of holomorphic



       Math Subject Classifications. 32W20, 32U15, 32Q15.
       Key Words and Phrases. Quasiplurisubharmonic functions, capacity, extremal functions, Kahler manifolds.

9 2005TheJournalof GeometricAnalysis
ISSN1050-6926
608                                 Vincent Guedj and Ahmed Zeriahi

line bundles (see Section 5) whose study is central to several questions of complex algebraic geom-
etry. Solving Monge-Amp~re equations associated to og-psh functions has been used to produce
metrics with prescribed singularities (see [13]). It is also related to the existence of canonical
metrics in K~ihler geometry (see [37]). Important contributions have been made by Kolodziej
in this direction [28] using techniques from local Pluripotential theory. Quasiplurisubharmonic
functions have also been used in [21 ] to define a notion of og-polynomial convexity and study the
fine approximation of positive currents by rational divisors. Last but not least, such functions are
of constant use in complex dynamics in several variables (see [17, 18, 22, 23, 33]).
```

## Primary unit 24: GZ-intrinsic-capacities-JGA05-20261004.txt, LF347--680

Literal SHA256 `f4b9152da337a5f66f0c15a40ce23cf259aafbbcaa2a3bffac8d0947dd1e81ff`; supplied pin matches: True.

```text
                                   3. Monge-Amp~re capacity
     In this section we introduce the global Monge-Amp~re capacity (see Definition 3.4). The
definition only makes sense when the cohomology class {w} has strong positivity properties. To
simplify our exposition we assume throughout this section that o9 is a K~ihler form.
     Let T be a positive closed current of bidegree (p, p) on X, 0 < p < n = d i m c X. It can be
thought of as a closed differential form of bidegree (p, p) with measure coefficients whose total
variation is controlled by                           /   1



                                         IITII := . L T A o9n-p         o




We refer the reader to [15, Ch. 3] for basic properties of positive currents. Given ~o E P S H ( X , o))
we write ~o ~ L I ( T ) if ~o is integrable with respect to each (measure) coefficient of T. This is
equivalent to ~0 being integrable with respect to the trace measure T A ogn-p. In this case, the
current ~0T is well defined, hence so is

                                    o9~0A T := o) A T + ddC(qgT) .

This is again apositive closed current on X, of bidegree (p + 1, p + 1). Indeed, positivity is a
local property which is stable under taking limits. One can locally regularize ~0 and approximate
o9~ A T by the currents o9~ A T which are positive since o9,p~ are smooth positive forms.
614                                            VincentGuedjand AhmedZeriahi

     When q) ~ P S H ( X , o9) N L~176 then ~o ~ L I ( T ) for any positive closed current T of
bidegree (p, p). One can thus inductively define o)j A T, 1 < j < n - p, for ~o e P S H ( X , co) O
L~176 For T = 0 and j = n one obtains the complex Monge-Amp~re operator, O)~o.       n It follows
from the local theory that the operator ~o ~ o)en is continuous under monotone sequences (see [5]).
The proof of these continuity properties is simpler in our compact setting. We refer the reader
to [24] where this is proved in a more general global context.

Proposition 3.1 (Chern-Levine-Nirenberg inequalities).                            Let T be a positive closed current
ofbidegree (p, p) on X andq) ~ P S H ( X , o9) n L ~ ( X ) .
      Then IIo)~ A TII = IITII. Moreover, i f ~ ~ P S H ( X , o9) n L I ( T ) , then ~p ~ L I ( T A o)~)
and
                      II~Plltl(T^,o~) ___ II~llzl(T) + [2 sup~p + supq) --i~f q)] IlZll 9
                                                           X       X

Proof.       By Stokes theorem, f x ddC~~A T A o)n-p-1 = 0, hence

                     IIo)~ A TII := f x W ~ A T A o)n-p-I = f x T A o)n-P := IITII .

Consider now ap ~ L I ( T ) . Since T has measure coefficients, this simply means that ~p is
integrable with respect to the total variation of these measures. Assume first ~ < 0, ~0 > 0 and
~o, ~ are smooth. Then

  [[~][LI(TA~o~) :~__-.f x ( - ~ ) T       A w~o A O)n - p - 1    =   II~PllLl(r~ +   fx(-*)z   A ddCq) A O)n-p-1 .

NOW it follows from Stokes theorem that

                                                        1                                        1



                                                                 fx T on-,
where the next to last inequality follows from q)T A o)n-p > 0 and - d d % p <_o9. This yields

                                    II~PllL~(r^,o~) -< Ii~PlILI(r) + sup~011TII.
                                                                      x
The general case follows by regularizing ~0, ~, observing that o)e = w~o,where q)f = q) _ infx q) >
0, and decomposing ~ = ~ ' + supx ~ with ~t = ~ _ suPx ~p < 0.                                   []

R e m a r k 3.2. The fact that the L l_norm of ~p with respect to the probability measure T A o2~ A
o)n-p-1 is controlled by its Ll-norm with respect to T A o)n-p is similar to the phenomenon
already encountered in Example 2.8: One can write

            T Ao)e /kO) n - p - 1      =    T Ao) n-p +ddCS, S = (q) - i.~f~0)T A O ) n - p - 1        > O.


This type of estimates is usually referred to as "Chern-Levine-Nirenberg inequalities," in reference
to [8] where simpler -but fundamental- L~-estimates were established (with ~ = constant).
Estimates involving the L 1.norm of if/were first proved in the local context by Cegrell [6] and
Demailly [12].

      A straightforward induction yields the following.
                                          Intrinsic Capacities on Compact Kiihler Manifolds                    615

Corollary 3.3.              Let ~, ~o E P S H ( X , o9) with 0 < ~o < 1. Then

                               o<_fx t 109 <_fx laP109n+ n [ 1 + 2sup@]
                                                                   X
                                                                        f 09n.
                                                                        dX
     Following Bedford-Taylor [5] and Kolodziej [29] we introduce the following Monge-Amp~re
capacity.

D e f i n i t i o n 3.4.    Let K be a Borel subset of X. We set

                            Cap~o(K) := sup                09<.o/ ~0 ~ P S H ( X , 09), 0 <_ ~0 <_ 1       .
                                                    IlK      n                                         }

     Note that this definition only makes sense when the cohomology class {09} is big, i.e., when
{09}n > 0, and when it admits locally bounded potentials ~0. This implies, by a regularization
result of Demailly [12], that {09} is big and neff In order to avoid technicalities, we are assuming
throughout this section that {09} is K~ihler.

Proposition 3.5.
       (1) I l K c K ~ c X are Borel subsets then

                  Volvo(K) := f 09n < Capoj(K) < Capo' (K') < Cap,o(X) = Volo~(X).
                              3K

        (2) l f K j are Borel subsets o f X thenCap~o(UK j) < ~ Capw(Kj). Moreover, Capoj(UKj) =
limCapo,(Kj) i f K j C Kj+I.
     (3) If091 < 092 then Captor(.) < Capm(.). For all A > 1, Cap,o(.) < CaPao,(.) <
A n Cap,o(.). In particular, if09, cot are two Kiihlerforms then there exists C > 1 such that
                                            1
                                                Cap,o(.) _< CaP,o,(.) _< C . CaP,o(.).

        (4) I f f : X ~ X is holomorphic then for all Borel subset K o f X,
                                                  Capco(f(K)) _< Capf.~o(K) 9
In particular, Capon(f (K)) = Cap~o(K) for every 09-isometry f .

Proof.       That Volvo(.) < Cap,o(.) is a straightforward consequence of the definition (since wo =
09). It then follows from Stokes theorem that f x o~ = f x (-onfor every ~o ~ P S H (X, 09) ML~176
                                                                                                 (X),
thus Volvo(X) = Cap~o(X).
        Property (2) is a straightforward consequence of the definitions.
     Ifwl < 092 then P S H ( X , o91) C P S H ( X , o92) hence Cap~ol(.) < Cap~(.). Fix A > 1. If
ap ~ P S H ( X , A09) is such that 0 < 7t < 1 then ~p/A ~ P S H ( X , w) with 0 < ~r/A < 1 / A < 1.
Moreover, (A09 + ddC~r) n = An(09 -F ddC(~t/A)) n. This shows CapaoJ(. ) < A n Capco(.).
    In particular, if 09, J are both K ~ l e r then A-109 < 09/ < A09 for some constant A > 1,
hence C -1 Capon(. ) < Capco,(. ) < C 9Capon(.) with C = A n.
      It remains to prove (4). It follows from the change of variables formula that if ~0
P S H ( X , o9) with 0 < ~0 < 1 then


                       f,         n <
                            (K) 09~0 --         f o09,o=         ( f ' 0 9 + ddC(~o o f ) ) n < Capf,o~(K)
616                                                Vincent Guedj and Ahmed Zeriahi

since~pof 6 P S H ( X , f ' 0 9 ) w i t h 0 < q~of < 1. W e i n f e r C a p w ( f ( K ) ) < Capf.w(K). When f
is a 09-isometry, i.e., f ~ Aut(X) with f ' 0 9 = w, then the mapping ~o w+ r o f is an isomorphism
of {u ~ P S H ( X , o9) / 0 < u < 1}, whence Cap~o(f(K)) = Capf.~o(K ) = Cap~o(K ).                         []

      Let P S H - (X, o9) denote the set of negative 09-psh functions. A set is said to be P S H ( X , 09)-
polar if it is included in the - c ~ locus of some function r E P S H ( X , w), r ~ - o 0 . As we
shall soon see, the sets of zero Monge-Amp&e capacity are precisely the P S H (X, 09)-polar sets.
We start by establishing the following:

Proposition 3.6.        I f P is a P S H ( X , w)-polar set, then CapofiP ) = O. More precisely, f f
r E P S H - ( X , o9) then

                      Capoj(r < - t ) < t
                                                      1%     (_r
                                                                                       ]
                                                                        + n Volvo(X) , Yt > O.


Proof.      Fix ~0 ~ P S H ( X , 09) such that 0 < ~0 < 1. Fix t > 0 and set Kt = {x E X / r                             <
- t } . By Chebyshev's inequality,


                      fK f~t
                               09~o <        (_r            -< tl[fx(-r             + n Voloo(X) ]
where the last inequality follows from Corollary 3.3. Taking supremum over all ~0's yields the
claim.                                                                                                                   []

                                                         * p
      Observe that the previous proposition says that CaP,o( ) = 0, where

                               Cap*(E) : = inf{CaP~o(G ) / G open with                 E C G},

is the outer capacity associate to Cap~o.

     Our aim is now to show that 09-psh functions are quasicontinuous with respect to Capo~
(Corollary 3.8). We first need to show that decreasing sequences of 09-psh functions converge "in
capacity."

Proposition 3.7.          Let r Cj ~ P S H (X, 09) M L ~176
                                                         (X) such that ( r                   decreases to r       Then for
each ~ > O,
                                               Cap~o({r j > r + 8}) ---> O.

Proof.       We can assume w.l.o.g, that Volvo(X) = 1 and 0 < Cj - r < 1. Fix 3 > 0 and
~0 ~ P S H ( X , 09), 0 < ~0 < 1. By Chebyshev inequality, it suffices to control f x ( r - r
uniformly in r      It follows from Stokes theorem that

               (r    - r            =        (r      - r      A 09~-1 -
                                                                          fx  d(r     - r   A dCq9 A 09~o     9

Now by Cauchy-Schwartz inequality,


         dfjAd~gA                       <_          dfjmdCfjA09~o -I             .       dfAdC~oAw~o -1              ,

where we set f j : = Cj - r >_ 0. Moreover,


              fx      A           A4'          =               ddc ) A 4 -1 < fx            A 4 -1 < 1,
                              Intrinsic Capacities on Compact Ktihler Manifolds                    617

since ~0c@-1 > 0, -ddCq9 < ~o and ~0 < 1. Similarly


             fx dfjAdCfjAo9~-l=               s     _fjddCfjAo9~     l<       fjoor   n-l .


Altogether this yields


        s       - ~)o~       <- f x O h - ~p)o>/x %n-1 _~_( f (1/fxj --) ~1)(.0~./ A2 r -1
                             < ~
                                        (Ix    (~/j -- ~)(0) + r    A 0)~-1
                                                                              )'" ,

where the last inequality follows from the elementary inequalities 0 < a < ~             _< 1 and V ~ +
4~_<4~+b.
     Going on replacing at each step a term w~0 by o) + w~, we end up with

                                         n ( (~/rjf - - x
                          (1/tj - - 1/t)O)~0 _< 2       r
                                                          )Jr- 0 ) ~ ) n 1/2n .
The majorant being independent of ~oand converging to 0 as j --~ + ~ (by dominated convergence
theorem), this completes the proof.                                                         []

C o r o l l a r y 3.8 (Quasicontinuity).  Let q9 ~ P S H ( X , ~o). For each e > 0 there exists an open
subset O e o f X such that CaP ~o( O e ) < e and ~o is continuous on X \ 0 ~.

Proof.     For t > 0 large enough, the set O1 = {~o < - t } has capacity < e / 2 by Proposi-
tion 3.6. Working in X \ O1 we can thus replace ~0 by ~0t = max(cp, - t ) which is bounded on X.
Regularizing ~0 (see Appendix), we can find a sequence apj of smooth Aco-psh functions which
decrease to ~ot on X, for some A > 1. By Proposition 3.7, the set Oj = {7% > ~ot + 1/j} has
capacity < e2 - j - 1 if kj is large enough. Now 7zkj uniformly converges to r = ~0t on X \ Oe,
Oe = Uj>_I O j, SO ~0 is continuous on X \ Os and Cap~o(Os) < e.                              []

E x a m p l e 3.9. The capacity Cap,o(-) does not distinguish between "big sets." Assume indeed
there exists an ample divisor D such that [D] --~ kw, k 6 N. Then there exists ~o 6 P S H ( X , o~)
such that ddC~o = k - l [ D ] - o). Note that q9 6 C~      \ D), e ~~ E C~    and {~p = -cx~} =
D. Replacing ~o by ~o - suPx ~o if necessary, we may assume supx ~o = 0. Consider ~Oc =
max(~o, - c ) E P S H ( X, w) N C~     Then qgc - ~o outside some neighborhood Vc = {q9 < - c }
of D. Since 0 _< 1 + ~ol < 1 and ~o1+~ol = oJ~ = 0 in X \ V1, we get


                     Capo/X)=fx(~Ol+~,)n=fv(o~l+~01)n -< Cap~o( V D ,
                                                           1


hence Cap~o(V1) = CapofiX).
      As a concrete example take X = C ~ n and 09 = ~OFS, D being some hyperplane H ~ "at
infinity" (k = 1). Set ~o[z : t] = log It[ - 1 log[[lz[[2 + [t[2] where z denotes the Euclidean
coordinates in C n = C]Pn \ Hoo and H ~ = (t = 0). Observe that supcy. ~p = 0. One then
computes
                              Clan\v1 = [ z E C n / I z [      <   e2x/~--l] .

Thus, the capacity of the complement of any Euclidean ball of radius smaller than 4 ~ e2 - 1 equals
618                                      Vincent Guedj and Ahmed Zeriahi

     The definition of Cap, o mimics the definition of the relative Monge-Amp~re capacity intro-
duced by Bedford and Taylor in [5]. Fix/d = {Ha } a finite covering of X by strictly pseudoconvex
open subsets of X, Ha = {x ~ X / O~(x) < 0}, where 06 is a strictly psh smooth function de-
fined in a neighborhood of ~-~. Fix 3 > 0 such that L/~ = {Hi } is still a covering of X, where
Lt~ = {x ~ X / • (x) < -3}. For a Borel subset K of X, we set

                                CaPBT(K) := Z           CapsT (K N/.g~, b/~) ,
                                                   c~



where
                CaPeT(E, f2) := sup { f~ (ddcu)n / u 6 PSH(~2), O < u < l }

is the capacity studied by Bedford and Taylor. The next proposition is due to Kolodziej [29]. We
include a slightly different proof.

Proposition 3.10.       There exists C >_ 1 such that
                                 1
                                     Cap~(.) _< C a p s r ( . ) _< C . Cap~(.).


Proof        Let E be aBorel subset of X. Since Cap~o(E N/d~) < CaPon(E) _< Y-~.aCapo~(E NL/~),
it is sufficient to show that if f2 = {x ~ X / O(x) < 0} is a smooth hyperconvex subset of X, then
there exists C _> 1 such that for all E C f26,

                           1
                                Capw(E ) < C a p n r ( E , g2) < C 9Cap,o(E),

where ~2~ = {x ~ X / 0(x) < -6}.
         It is an easy and well known fact in the local theory that the capacities Cap(., ~2) and
Cap(., f2') are comparable when f2' c fl (see e.g., Theorem 6.5 in [12]). Therefore we can
assume (passing to a finer covering if necessary) that co = ddC~l, near f2. Fix C1 > 0 such
t h a t - C 1 < ~P < C l O n f2. Fix~o 6 P S H ( X , 09) such t h a t 0 < ~0 < 1 o n X a n d s e t u =
(2C1)-1(~o + ~O + C1). Then u ~ PSH(~2) and 0 < u < 1, hence


                     fe "--(2c,)"L
                         09go                   (ddcu)n --< (2c1)nCapsT(E'g2) ,

which yields Cap,o(E) < (2C1) n C a p n r ( E , fl). Observe that we have not used here that 09 is
Kahler.
      For the reverse inequality we consider X 6 C~176 such that X = 0 in X \ ~2 and X < 0
in f~. Replacing X by eX if necessary, we can assume X e P S H ( X , 09). This is because 09 is
K~thler (and this is the only place where we shall use this crucial assumption). Fix e > 0 so small
that X < - e on ~2a. Let now u 6 PSH(f2) be such that 0 < u < 1 on f2. Consider

                                                  u-•-]-Cl                 in   f28
                                                    2+2C1
                    ~0(x) =          max ~ 2~UCtt , zX
                                         [ u - ~ + C     2 (x) + 1)        in   g2 \ f28
                                                    1                      in   X\~

Observe that 0 < u' := (u - ~ + C1)/(2 + 2C1) < (1 + 2C1)/(2 + 2C1) < 1 in g2. Therefore
~o ~ P S H ( X , 209) since 2X(x) + 1 < - 1 < u' in f2~, while 2X(X ) + 1 - 1 > u' on 092. Note,
                             Intrinsic Capacities on Compact Kiihler Manifolds                     619

also that 0 < ~o < 1 thus for E C f2~,

              1
        (2 + 2C1)n f E (ddcu)n
                                                 - -     + ddC q9     )"   <         co + ddC ~o
                                     =

                                     <
                                                 2 + 2C1

                                           Cap2~o/e(E) <
                                                               (!)n        --

                                                                     Cap~o(E)

hence CapBT(E, f2) < 4n(1 + c 1 ) n E - n Capo~(E ).                                                []

     Since locally pluripolar sets are precisely the sets of zero relative capacity [5], we obtain the
following:

Corollary 3.11.      Cap~o(P) = 0 r162CapBT(P ) = 0 r            Pis locally plul~polar.

     We shall show later on that locally pluripolar sets are P S H ( X , w)-polar when o9 is K~ihler
(see Theorem 7.2).
     The following two results are direct consequences of the corresponding results of Bedford
and Taylor [4, 5].
```


# P15.2: common full-mass domain and minimum full-form operator data

Author: native Codex execution in the fresh assigned workspace. Date: 4 October 2026. Status: **partial**; unverified mathematical draft. The original P15.2 atom remains open. Only this atom is investigated; energy integrability is used solely to specify a common operator subdomain.

The new work is the scalar-deficit common-domain theorem, bare-current reconstruction, extension of the reference kernel to all full-mass inputs, quotient continuity and the explicit infinite-dimensional geometric-kernel example. Published foundations are cited with hypotheses and checked applications. Earlier supplied author/review verdicts are evidence to reconstruct, not theorem grants.

# n1. Common full-mass and joint-linear domains

**Scope.** This is a partial P15.2 result, independently reconstructed from the stated literature foundations. No earlier proof or review verdict is an assumption. Only P15.2 is investigated. The energy integrability condition below specifies a useful operator domain; no P15.1 energy theorem is claimed.

Let $X$ be a connected smooth compact Kahler manifold of complex dimension $n\geq1$, let $\alpha$ be pseudoeffective with $\operatorname{vol}(\alpha)=0$, let $\theta$ be a smooth closed real representative, and let $\psi\in\operatorname{PSH}(X,\theta)$ not be identically minus infinity. Set
$$
d^c=\frac{i}{4\pi}(\bar\partial-\partial),\qquad dd^c=\frac{i}{2\pi}\partial\bar\partial,
\qquad T_u=\theta+dd^cu,\qquad P=T_\psi.
$$
The retained type is the actual two-sided bounded comparison type
$$
\mathcal C_\psi=\{u\in\operatorname{PSH}(X,\theta):\psi-C\leq u\leq\psi+C\text{ for some }C<\infty\}.
$$
Comparisons are extended-valued global comparisons, not merely comparisons on intersecting finite loci. A more-singular potential means $u\leq\psi+C$. Differences in integrals are evaluated on the simultaneous finite locus and assigned zero elsewhere. Every measure below gives zero mass to these pluripolar exceptional sets.

The essential standard foundations used here are the following, with complete supplied printed bodies in the source annex.

* Boucksom--Eyssidieux--Guedj--Zeriahi (BEGZ), *Monge-Ampere equations in big cohomology classes*, Acta Math. 205 (2010), 199--262, arXiv:0812.3674v2, Definition 1.1, Propositions 1.4 and 1.6, Theorem 1.8: on compact Kahler $X$, nonpluripolar products of at most $n$ closed positive $(1,1)$ currents are well-defined finite closed positive currents, symmetric, multilinear on positive sums and plurifinely local; their trace measures do not charge pluripolar sets. Smooth factors commute with the construction. The empty product is $1$. These are actual-current properties, not multilinearity of class positive products. All currents used below meet these hypotheses.
* Darvas--Di Nezza--Lu (DDNL), *Monotonicity of nonpluripolar products and complex Monge-Ampere equations with prescribed singularity*, Anal. PDE 11 (2018), 2049--2087, Proposition 2.1: for $n$ smooth closed real backgrounds $\theta_j$ with pseudoeffective classes and $u_j,v_j\in\operatorname{PSH}(X,\theta_j)$ with the same bounded singularity type in each slot, the two top mixed masses are equal. Theorem 2.4: if $u_j$ is less singular than $v_j$ in each slot, its top mixed mass is at least the other mass. No big-class or small-unbounded-locus condition is present. Every application below uses precisely $k$ potential slots in $\theta$ and $n-k$ smooth Kahler slots with zero potentials; the latter classes are pseudoeffective, and both comparisons in those slots are identical.
* BEGZ Sections 1.3--1.4 and Definition 1.17: minimal-singularity currents exist in a pseudoeffective class, are less singular than every current in that class, and their top mass in a big class is its volume. At the boundary the volume is the decreasing limit along addition of a Kahler class. The positive product of nef classes agrees with cup product. We use the actual-current upper bound supplied by DDNL comparison with the minimal current, not an equality of arbitrary mass with class volume.
* Duc-Viet Vu, *Convexity of the class of currents with finite relative energy*, arXiv:2005.13241v3 (25 March 2022), Section 3: with pseudoeffective classes, positive reference currents $P_j$, and a closed positive relative current $R$, the relative full-mass tuple space consists of currents more singular than the references and with equal cohomology classes of their relative nonpluripolar products. Joint $\chi$ energy is the sum over subsets $J$ of the integrals of $-\chi(\sum_j(u_j-\varphi_j))$ against the mixed relative products choosing $T_j$ on $J$ and $P_j$ elsewhere. Here $\chi$ is convex increasing and $\chi(-\infty)=-\infty$. Theorem 3.4 states convexity of the diagonal full-mass and diagonal joint-weight spaces. Corollary 3.2 states equality of the joint-weight spaces after a bounded-equivalent cohomologous reference change. The printed proofs invoke other published arguments; these two results are used as precisely scoped literature foundations, not as newly proved lemmas. We apply them only for $d\geq1$, $d$ equal slots $P$, $R=\omega^{n-d}$ smooth closed positive, and $\chi(t)=t$. The products have top degree, so on connected compact oriented $X$ their cohomology equality is exactly equality of masses: integration identifies $H^{2n}(X,\mathbb R)$ with $\mathbb R$.

DDNL uses $i\partial\bar\partial$, so its potential for the same current is $u/(2\pi)$. Vu uses $dd^c_s=i\partial\bar\partial/\pi=2dd^c$ (the original extracted convention is defective and is preserved in the annex); its potential is $u/2$. These positive rescalings preserve comparison, full mass and integrability. Smooth backgrounds and the actual currents are unchanged. No Xia big-class corollary is applied to the boundary class.

Fix a Kahler form $\Omega$ and write
$$
M_k(\psi,\Omega)=\int_X\langle P^k\rangle\Omega^{n-k},\quad M_0=\int_X\Omega^n>0,
\quad d=\max\{k:M_k>0\},\quad m=n-d.
$$
Then $d<n$, and $d$ is independent of $\Omega$ and of an anchor in $\mathcal C_\psi$. Indeed $P+\varepsilon\Omega\geq\varepsilon\Omega$ makes $\alpha+\varepsilon[\Omega]$ big, and positive multilinearity and the upper mass bound give
$$
0\leq\sum_{k=0}^n\binom nk\varepsilon^{n-k}M_k
=\int_X\langle(P+\varepsilon\Omega)^n\rangle
\leq\operatorname{vol}(\alpha+\varepsilon[\Omega])\longrightarrow0.
$$
Thus $M_n=0$. For any other Kahler form $\omega$, compactness gives $c\Omega\leq\omega\leq C\Omega$. Expanding the positive power differences gives, for every positive $(k,k)$ product current $S$,
$$
c^{n-k}\int S\Omega^{n-k}\leq\int S\omega^{n-k}\leq C^{n-k}\int S\Omega^{n-k}.
$$
This proves invariance of the positivity tests. DDNL Proposition 2.1 with $k$ reference slots proves the anchor assertion. For more-singular $u_1,\ldots,u_k$, DDNL Theorem 2.4 gives
$$
0\leq\int\langle T_{u_1}\cdots T_{u_k}\rangle\Omega^{n-k}\leq M_k.
$$
Consequently every such product with $k>d$ is zero as a current. A positive current of zero Kahler trace mass is zero: in a local frame, positivity bounds the absolute coefficient measures by a constant times the sum of diagonal trace measures; a finite covering makes this global. Equivalently, normalize its coefficient cone to unit trace; its compact slice bounds every coordinate, so trace zero forces all coefficients to vanish. This argument applies also to cluster differences later. No identification with class numerical dimension is made.

Define initially for a Kahler form $\omega$
$$
\mathcal H_{\psi,\omega}=\left\{u\in\operatorname{PSH}(X,\theta):u\leq\psi+C,
\quad\int\langle T_u^d\rangle\omega^m=\int\langle P^d\rangle\omega^m\right\}.
$$
**Common-domain theorem.** This set is independent of the full auxiliary form, including its class. Denote it $\mathcal H_\psi$.

For $d\geq1$, suppose equality holds for $\omega_0$. Choose $C>0$ so that $D=C\omega_0-\omega_1$ is Kahler. For $0\leq j\leq m$ define the scalar deficit
$$
\Delta_j=\int_X(\langle P^d\rangle-\langle T_u^d\rangle)\omega_1^jD^{m-j}.
$$
It is nonnegative by DDNL Theorem 2.4, applied with $d$ copies of $(\theta,\psi)$ versus $(\theta,u)$, $j$ copies of $(\omega_1,0)$, and $m-j$ copies of $(D,0)$. Each background is smooth closed real and pseudoeffective, and $\psi$ is less singular than $u$. All products are finite by BEGZ. Expansion of the smooth complementary power yields
$$
0=C^m\int_X(\langle P^d\rangle-\langle T_u^d\rangle)\omega_0^m
=\sum_{j=0}^m\binom mj\Delta_j.
$$
Every coefficient is strictly positive; each $\Delta_j$ is therefore zero. The term $j=m$ gives equality for $\omega_1$. Interchanging the two forms proves equality of domains. This reasoning never asserts positivity of the difference of product currents. For $d=0$ the two empty products are both $1$, so every deficit is identically zero and the condition is automatic. The common degree-zero domain is simply all more-singular $\theta$-psh potentials.

For $d\geq1$ define the joint-linear domain
$$
\mathcal F^1_\psi=\left\{u\in\mathcal H_\psi:
\sum_{a=0}^d\binom da\int_X|u-\psi|\langle T_u^aP^{d-a}\rangle\omega^m<\infty\right\}.
$$
For $d=0$ use $\int|u-\psi|\omega^n<\infty$. This definition is independent of the full form as well. In fact for each positive mixed current $Q_a$ the pointwise comparison of $\omega_0,\omega_1$ gives
$$
c^m\int|u-\psi|Q_a\omega_0^m\leq\int|u-\psi|Q_a\omega_1^m
\leq C^m\int|u-\psi|Q_a\omega_0^m.
$$
These inequalities hold also for infinite integrals. There are only finitely many positive summands. For $d=0$, both quasi-psh functions are locally integrable against a smooth volume on compact $X$, so this finiteness is automatic.

Subtract a constant from $u$ so that $u\leq\psi$, and simultaneously subtract a constant from the reference and potentials if a negative normalization is needed. The change in each absolute-weight integral is at most a constant times a finite mixed mass. In Vu's source convention the diagonal joint linear energy is exactly
$$
\frac d2\sum_{a=0}^d\binom da\int_X(\psi-u)\langle T_u^aP^{d-a}\rangle\omega^m.
$$
Indeed the sum of $d$ source potential differences is $d(u-\psi)/2$, and there are $\binom da$ subsets of size $a$. Thus the displayed domain agrees exactly with the source diagonal joint-linear domain for $d\geq1$, independent of the numerical weighting of its finitely many positive terms. The source does not define a zero-slot energy; our $d=0$ definition is separately justified. Every member of $\mathcal C_\psi$ belongs to $\mathcal F^1_\psi$, by bounded differences, BEGZ finiteness and DDNL mass equality.

If $\chi\sim\psi$, the dominance conditions are equivalent, $d$ and every reference mass agree by DDNL, and hence $\mathcal H_\chi=\mathcal H_\psi$. Vu Corollary 3.2 applies with the same smooth relative current to identify $\mathcal F^1_\chi=\mathcal F^1_\psi$ when $d\geq1$. For $d=0$ it follows from $|u-\chi|\leq|u-\psi|+\|\chi-\psi\|_\infty$ off the common pole set and smooth-volume integrability. This states domain invariance, not equality of the measures produced by different actual potentials.

The full-mass domain is convex. For $d\geq1$ this is Vu Theorem 3.4 with the checked top-degree relative background; for $d=0$ it is convexity of psh functions and of the dominance condition. Likewise $\mathcal F^1_\psi$ is convex by the same theorem, or directly for $d=0$. For a finite family $u_1,\ldots,u_N\in\mathcal H_\psi$, its average $w$ has full mass. Expanding $\langle T_w^d\rangle$ shows its trace mass is the average of $N^d$ ordered mixed masses. Each is at most the reference mass by DDNL, all are nonnegative, and their average equals that mass. Therefore every ordered mixed degree-$d$ mass equals the reference mass, against every Kahler $\omega^m$. This includes products involving the anchor and repetitions. For $d=0$ it is the empty-product identity. This supplies mixed full mass without an unsupported polarization of scalar diagonal equalities.

The common linear domain can contain genuinely unbounded differences. On $X=\mathbb P^1_y\times\mathbb P^1_z$, put $\theta=p_1^*\kappa$, $\psi=0$ and $\Omega=p_1^*\kappa+p_2^*\kappa$, with $\int\kappa=1$. This is a nef zero-volume class by the cup-product statement, and $d=1$, $M_1=1$. Choose $0<a<1/2$ and, in a small disk near $y=0$, set $v(y)=-b(-\log|y|)^a$. Continue using a smooth cutoff on a fixed annulus. Near the puncture the radial second derivative in $\log|y|$ is $ba(1-a)(-\log|y|)^{a-2}>0$. The cutoff contributes a bounded negative Hessian only on that annulus, so sufficiently small $b>0$ ensures $S=\kappa+dd^cv\geq0$ globally. The extension takes value minus infinity at the puncture and is subharmonic there by the distributional radial calculation. Subtract a constant to have $v\leq0$.

The radial boundary flux tends to zero, since it is a positive constant times $ba(-\log r)^{a-1}$. Thus $dd^cv$ has no atom at zero; elsewhere the current is smooth. Stokes gives $\int S=1$, and deleting its pole removes no mass. For $u=p_1^*v$, its degree-one nonpluripolar mass against $\Omega$ is $1$. The integral of $-v$ against smooth $\kappa$ is finite by the exponential decay of radial area after $t=-\log r$. Its singular integral against $dd^cv$ is a positive constant times
$$
\int^\infty t^a t^{a-2}\,dt=\int^\infty t^{2a-2}\,dt<\infty.
$$
The remaining annulus is smooth. Pulling back and integrating the second-factor area therefore proves both degree-one joint integrals finite. Hence $u\in\mathcal F^1_\psi$, with $u-\psi$ actually unbounded. This example is only a witness to strict extension in one ambient case; the general theorem assumes no fibration.

This proves proposals 1 and 2 in their stated operator-domain scope. No moving unbounded-weight perturbation limit or energy minimum-reference theorem follows from these domain statements.


# n2. Bare-current reconstruction and mixed decreasing continuity

This note uses n1. The new assertion is convergence of the product current itself, not only of one trace measure.

We use Vu, *Relative non-pluripolar product of currents*, Ann. Global Anal. Geom. 60 (2021), 269--311, arXiv:2004.11111v1, Lemma 4.1(i): on $U\subset\mathbb C^n$, psh factors $p_{i,l}\geq p_i$ converging in $L^1_{\mathrm{loc}}$, and closed positive relative backgrounds $R_l\to R$ satisfying Condition (*), give
$$
\liminf_l\int_U\left\langle\bigwedge_{i=1}^d dd^cp_{i,l}\mathbin{\dot\wedge}R_l\right\rangle\Phi
\geq\int_U\left\langle\bigwedge_{i=1}^d dd^cp_i\mathbin{\dot\wedge}R\right\rangle\Phi
$$
for every compactly supported smooth weakly positive complementary test form $\Phi$. The number of product slots here is $d$, distinct from $m=n-d$ in n1. We use only $R_l=R=1$, a closed positive $(0,0)$ current. The relative product is then exactly the ordinary nonpluripolar product (Vu Definition 3.3). The printed Condition (*) has an overloaded index in its power, preserved literally in the annex. At relative degree zero its displayed power is the empty product. Locally uniform mass and $(q_l-q)1\to0$ follow from local integrability and dominated convergence on compact subsets for psh $q_l\downarrow q$ with bounded limit. The source also explicitly lists constant sequences as examples. No variable singular relative background is used.

For additional transparency, here is a complete reconstruction of the required constant-background *decreasing* case. It avoids relying on a transfer from top measures to currents and keeps every local product factor bounded before using bounded convergence. The convergence foundation is DDNL Proposition 2.2: on an open set in $\mathbb C^n$, uniformly bounded psh factors converging in capacity in every slot, multiplied by uniformly bounded quasicontinuous weights converging in capacity, give weak convergence of their weighted Bedford--Taylor top products. Quasi-psh functions are quasicontinuous and decreasing sequences with a fixed background converge in capacity, with the qualifications explained next.

Precisely, Guedj--Zeriahi, *Intrinsic capacities on compact Kahler manifolds*, J. Geom. Anal. 15 (2005), 607--639, Proposition 3.7 assumes bounded potentials: decreasing bounded $A\Omega$-psh functions converge in $\operatorname{Cap}_{A\Omega}$. For arbitrary negative quasi-psh $v_l\downarrow v\not\equiv-\infty$ in a fixed smooth background, choose $A\Omega$ dominating its lower Hessian bound. The bounded truncations $\max(v_l,-K)$ decrease to $\max(v,-K)$; outside $\{v\leq-K\}$ the convergence tests for the truncations and original functions coincide. Proposition 3.6 gives
$$
\operatorname{Cap}_{A\Omega}(\{v<-t\})\leq
\frac{1}{t}\left(\int_X(-v)(A\Omega)^n+n\int_X(A\Omega)^n\right).
$$
The set with $\leq-K$ is contained in $\{v<-K+1\}$ for $K>1$, so its capacity tends to zero. First take $l\to\infty$ for fixed $K$, then $K\to\infty$. This proves the needed general decreasing convergence. Proposition 3.10 compares this global capacity with local Bedford--Taylor capacities on relatively compact coordinate pieces. Corollary 3.8 gives quasicontinuity. Every function in the present application is global $\theta$-psh plus a smooth local background; bounded local truncations preserve capacity convergence and quasicontinuity. These applications use a dominating Kahler form, not capacity in the pseudoeffective background itself. The source's bounded hypothesis is never dropped silently.

Let $p_{i,l}\downarrow p_i$ be these local psh representatives, on a chart containing the support of $\Phi$. Subtract constants separately in each slot so that all $p_{i,l}\leq0$ on a slightly smaller chart; local upper bounds follow from the fixed first term. Put
$$
s=\sum_{i=1}^d p_i,\qquad b_K=\min(1,\max(s+K,0)),\qquad p^K_{i,l}=\max(p_{i,l},-K).
$$
For $d\geq1$, $0\leq b_K\leq1$, and its nonzero locus is $\{s>-K\}\subset\bigcap_i\{p_i>-K\}$. Since $p_{i,l}\geq p_i$, all factors, including the limit factors, equal their bounded truncations on that nonzero locus. This is a statement about the nonzero locus, not necessarily the closed support. At the boundary the weight is zero. The nonzero locus is plurifinely open. BEGZ locality consequently identifies the weighted nonpluripolar products there with weighted bounded Bedford--Taylor products. The functions $p^K_{i,l}$ are uniformly bounded psh and converge in capacity. The fixed weight $b_K$ is bounded quasicontinuous. Thus
$$
\int b_K\left\langle\bigwedge_i dd^cp_{i,l}\right\rangle\Phi
\longrightarrow
\int b_K\left\langle\bigwedge_i dd^cp_i\right\rangle\Phi. \tag{C1}
$$
Here DDNL's top-product formulation legitimately covers complementary smooth forms: express $\Phi$ in a constant $(m,m)$ basis with smooth compactly supported scalar coefficients. Each constant basis element is a linear combination of products of $m$ constant positive $(1,1)$ forms. To see the span, elementary $(1,1)$ forms span all such matrices over $\mathbb C$, and their wedges span all $(m,m)$ basis monomials; real parts give the real span. Every real Hermitian $(1,1)$ form is a difference of two positive definite forms after adding a large identity matrix. Expanding these differences gives the required positive-factor decomposition. The constant positive factors have smooth quadratic psh potentials, bounded on the chosen chart. Append them as the remaining slots and incorporate scalar coefficients into the quasicontinuous weights. DDNL Proposition 2.2 then proves (C1) term by term. No unbounded product slot is inserted into that proposition or Vu v3 Theorem 3.3.

For weakly positive $\Phi$, positivity yields the lower bound by the left side of (C1). As $K\to\infty$, $b_K$ increases to $1$ off the union of the product poles, and the limit current gives no mass to those poles. Monotone convergence therefore proves the displayed lower-semicontinuity inequality in exactly the decreasing setting needed here. This also independently verifies the specialization of Vu Lemma 4.1. For $d=0$ there are no factors, and all products are identically $1$; no cutoff argument is needed.

**Bare-current theorem.** If $u_l\downarrow u$ with $u_l,u\in\mathcal H_\psi$, then
$$
\langle T_{u_l}^d\rangle\rightharpoonup\langle T_u^d\rangle
\quad\text{as }(d,d)\text{ currents}. \tag{C2}
$$
More generally, for $u_{i,l}\downarrow u_i$ with every member and limit in $\mathcal H_\psi$, $1\leq i\leq d$,
$$
\langle T_{u_{1,l}}\cdots T_{u_{d,l}}\rangle
\rightharpoonup\langle T_{u_1}\cdots T_{u_d}\rangle. \tag{C3}
$$
Every product in (C3) has the same trace mass $M_d(\psi,\Omega)$ by n1. Positivity and the coefficient/trace bounds give uniformly bounded coefficient measures on compact $X$. Weak compactness of these measures gives a cluster current $S$. This compactness can be seen directly by applying weak-* compactness to each coefficient on finitely many charts and using a diagonal subsequence; distributional closedness and positivity pass to the limit. On each chart take a smooth real local potential $\rho$ for $\theta$, which need not be psh. The functions $p_{i,l}=\rho+u_{i,l}$ are psh, decrease to $p_i=\rho+u_i$, and converge in $L^1_{\mathrm{loc}}$: off the null pole sets,
$$
0\leq p_{i,l}-p_i\leq p_{i,1}-p_i,
$$
whose right side is locally integrable. Both limits are not identically minus infinity on any chart. Lower semicontinuity against every local weakly positive $(m,m)$ test shows
$$
S-\langle T_{u_1}\cdots T_{u_d}\rangle\geq0.
$$
This is a positive-current difference obtained by the cluster argument, not the false assertion that differences of arbitrary actual products are positive. Passing to the trace mass along the cluster subsequence gives mass $M_d$ for $S$, equal to that of the target. Its positive difference has zero trace and is zero by n1. All clusters coincide, proving (C3), and repetition of slots gives (C2). The argument uses every complementary test bidegree, not merely $f\Omega^m$. Smooth-test convergence and uniform trace bounds also give convergence against continuous coefficient test forms, by uniform smooth approximation.

For $u\in\mathcal H_\psi$ subtract a constant to have $u\leq\psi$, and define $u_L=\max(u,\psi-L)$. This is $\theta$-psh, lies in $\mathcal C_\psi$, and decreases to $u$. DDNL comparison gives full mass (or directly bounded-type equality does). Thus (C2) proves bare-current convergence for all real levels $L\to\infty$, not just an integer subsequence: a hypothetical failing sequence of levels contains an increasing subsequence, to which the theorem applies. Restoring constants changes no product. Every decreasing full-mass approximation with this limit gives the same current. Simultaneous mixed truncations are covered by (C3). These assertions require the limit to remain in the full-mass domain; mass loss would invalidate the cluster uniqueness step.

For each fixed smooth real complementary form $\eta$, (C2)--(C3) imply weak convergence of the signed measures obtained by wedging with $\eta$. If additionally $\eta_l\to\eta$ in $C^0$ coefficient norm, the coefficient/trace bound shows
$$
\|\langle T_{u_l}^d\rangle\wedge(\eta_l-\eta)\|_{\mathrm{TV}}
\leq c_{X,\Omega,d}M_d\|\eta_l-\eta\|_{C^0}\longrightarrow0.
$$
Thus the corresponding moving *smooth, uniformly converging* factors are allowed. This proves no convergence for arbitrary rough moving factors or unbounded weights.


# n3. Minimum full-form data on the entire common domain

This note uses n1 and n2. Let
$$
W=\operatorname{span}_{\mathbb R}\{\omega^m:\omega\text{ is a smooth Kahler form on }X\},
\qquad L_u(\eta)=\langle T_u^d\rangle\wedge\eta,
\qquad N=\bigcap_{u\in\mathcal C_\psi}\ker L_u.
$$
$W$ is the algebraic span of actual smooth closed real complementary forms, not a formal tensor space and not an asserted identification with every closed $(m,m)$ form. For $\eta\in W$, its wedge with the order-zero current is a finite signed measure. This depends on the actual form $\eta$, not on a presentation as a sum of powers. Linearity of ordinary smooth multiplication proves presentation independence. Set $Q_W=W/N$ and let $q_W:W\to Q_W$ be the quotient map.

**Kernel extension.** The same $N$ is the intersection of kernels over $\mathcal F^1_\psi$ and also over $\mathcal H_\psi$. One inclusion follows from $\mathcal C_\psi\subset\mathcal F^1_\psi\subset\mathcal H_\psi$. Conversely, if $\eta\in N$, the bounded-type truncations $u_L$ of any $u\in\mathcal H_\psi$ satisfy $L_{u_L}(\eta)=0$. The bare-current convergence in n2, with fixed smooth $\eta$, implies $L_u(\eta)=0$. This proves the reverse inclusion. Extending the kernel to the whole domain is substantive content; merely defining a quotient would not prove this assertion.

Consequently, for any two Kahler forms,
$$
L_u(\omega_0^m)=L_u(\omega_1^m)\text{ for every }u\in\mathcal H_\psi
\quad\Longleftrightarrow\quad
q_W(\omega_0^m)=q_W(\omega_1^m). \tag{Q1}
$$
The equivalence is unchanged if the tests are restricted to $\mathcal C_\psi$ or $\mathcal F^1_\psi$. Each $L_u$ induces a unique linear measure-valued map $\overline L_u$ on $Q_W$. The map
$$
Q_W\longrightarrow\prod_{u\in\mathcal H_\psi}\mathcal M(X),\qquad
q_W(\eta)\longmapsto(L_u(\eta))_u
$$
is injective. Here $\mathcal M(X)$ denotes finite signed measures. This identifies $Q_W$ with the image of the actual family evaluation map; it is an operator-data quotient, not a geometric space carrying the measures.

The precise universal minimality statement is elementary but useful. If a linear data map $r:W\to Z$ is sufficient for the family in the sense that each $L_u=B_u\circ r$ with linear $B_u:r(W)\to\mathcal M(X)$, then $\ker r\subset N$. The unique linear map $h:r(W)\to Q_W$ defined by $h(r(\eta))=q_W(\eta)$ is well-defined, and $q_W=h\circ r$. Conversely the quotient itself is sufficient. Thus every sufficient linear datum refines $Q_W$; the coarsest equivalence relation is exactly equality in $Q_W$. For data maps restricted to admissible powers, even without linearity, sufficiency implies that equal data give equal family outputs, hence equal quotient images by (Q1); the quotient image therefore factors uniquely through the realized data image. This is minimality only for this specified operator family and reference span. It proves no universal optimality for every conceivable zero-volume theory.

There is also a factorwise kernel characterization. For $d\geq1$,
$$
\eta\in N\quad\Longleftrightarrow\quad
\langle T_{u_1}\cdots T_{u_d}\rangle\wedge\eta=0
\text{ for every }u_1,\ldots,u_d\in\mathcal H_\psi. \tag{Q2}
$$
To prove it first use bounded-type factors. For $t_i>0$, the convex combination $w=(\sum t_i)^{-1}\sum t_iu_i$ is in $\mathcal C_\psi$, and
$$
0=(\sum t_i)^d L_w(\eta)
=\sum_{i_1,\ldots,i_d}t_{i_1}\cdots t_{i_d}
\langle T_{u_{i_1}}\cdots T_{u_{i_d}}\rangle\wedge\eta.
$$
Testing with any smooth scalar function gives a real polynomial zero on an open positive cone; every coefficient is zero. In particular the coefficient of $t_1\cdots t_d$ is $d!$ times the desired mixed signed measure. Vanishing against all smooth tests proves its measure is zero. Simultaneous truncation and mixed bare-current convergence from n2 extend the result to $\mathcal H_\psi$. The reverse direction follows by repeating all factors. For $d=0$, $L_u(\eta)=\eta$ as a smooth top-degree signed measure, so $N=\{0\}$ and $Q_W=W$.

**Quantitative quotient continuity.** Fix $\Omega$ and a $C^0$ coefficient norm from its metric. There is a constant $c_{X,\Omega,d}$ such that for every $u\in\mathcal H_\psi$ and smooth complementary $\eta$,
$$
\|L_u(\eta)\|_{\mathrm{TV}}\leq c_{X,\Omega,d}M_d(\psi,\Omega)\|\eta\|_{C^0}. \tag{Q3}
$$
This follows by the local trace control of coefficient measures in n1, summing a finite partition of unity. Smooth multiplication is coefficientwise and has no derivatives. In particular $N$ is closed in the $C^0$ norm restricted to $W$, as well as in its smooth topology. Define
$$
\rho_\Omega(q_W(\eta))=\inf_{\nu\in N}\|\eta+\nu\|_{C^0}.
$$
It is a norm on the algebraic quotient (no completeness asserted). If it is zero, (Q3) implies $L_u(\eta)=0$ for every bounded-type $u$, so $\eta\in N$. The remaining norm axioms follow from the infimum definition. Taking the infimum in (Q3) gives
$$
\|\overline L_u(\xi)\|_{\mathrm{TV}}\leq c_{X,\Omega,d}M_d(\psi,\Omega)\rho_\Omega(\xi). \tag{Q4}
$$
Equivalent metric norms give equivalent quotient norms. Thus this temporary metric used to state continuity is not additional operator reference data. Each induced operator is continuous. If $u_l\downarrow u$ in $\mathcal H_\psi$ and $\xi_l\to\xi$ in this norm, then $\overline L_{u_l}(\xi_l)\rightharpoonup\overline L_u(\xi)$: use (Q4) on $\xi_l-\xi$, and n2 on any fixed smooth representative of $\xi$. Mixed continuity has the same proof using the common mixed trace mass and (Q2). These are specified admissible continuities on the quotient; they involve no unbounded test weights.

**Raw mass and reference invariance.** For every $u\in\mathcal H_\psi$ and $\eta\in W$,
$$
\int_X L_u(\eta)=\int_X\langle P^d\rangle\eta=:\mathfrak M_\psi(\eta), \tag{Q5}
$$
first for each Kahler power by n1 and then by linearity. It descends to $Q_W$, since $L_\psi$ vanishes on $N$. On an admissible power its value is strictly positive and equals
$$
M_d(\psi,[\omega])=\{\langle P^d\rangle\}\cdot[\omega]^m>0.
$$
Closedness of the product and distributional Stokes prove this cohomological identity; it is a homogeneous degree-$m$ polynomial of the class. This does not make the measure cohomological. Scaling $\omega$ by $a>0$ multiplies its quotient image, operators and masses by $a^m$. Adding a constant to $u$ leaves its current and operator unchanged. No division by $\operatorname{vol}(\alpha)$ or by this positive lower-degree mass is performed.

Changing the reference from $\psi$ to a bounded-equivalent $\chi$ leaves $\mathcal C$, $\mathcal H$, $\mathcal F^1$, $d$, $W$, $N$, and $Q_W$ unchanged by n1 and the kernel construction. It also leaves (Q5) unchanged, by equality of full-mass integrals for every power and linearity. The reference potentials themselves can produce different measures; the claim is equality of the family and its datum, not $L_\psi=L_\chi$. An energy anchor is unnecessary for this operator; if one is separately chosen, it fixes an energy origin and is not measure-carrier data.

A gauge change $\theta' =\theta+dd^cg$, $u'=u-g$, $\psi'=\psi-g$, with $g$ smooth real, preserves every actual current, comparison and difference. It preserves all domains, operators and kernel data under this identification. Any two smooth real representatives of $\alpha$ on compact Kahler $X$ are related in this way by the smooth $dd^c$ lemma: Deligne--Griffiths--Morgan--Sullivan, *Real homotopy theory of Kahler manifolds*, Invent. Math. 29 (1975), 245--274, Lemma 5.11 and Remark 5.14. Exactly, a smooth $d$- and $d^c$-closed $d$-exact form is $dd^c$-exact, also over $\mathbb R$. The difference of these representatives is real closed of pure type $(1,1)$, hence $d^c$-closed and exact; its degree-two primitive is a smooth real function after rescaling the convention. The complete authenticated printed proof is in the annex. Temporary local potential gauges likewise have no effect on products by BEGZ.

**An explicit geometric kernel in a test case.** Let $X=\mathbb P^1_y\times\mathbb P^1_z$, let $\kappa$ be normalized Fubini--Study area with integral $1$, and put $A=p_1^*\kappa$, $B=p_2^*\kappa$, $\theta=A$, $\psi=0$. The class is nef, $\alpha^2=0$, and therefore has volume zero by the nef cup-product statement in n1. Here $d=1$, $m=1$. In this case $W$ is every smooth closed real $(1,1)$ form: given such $\eta$, both $\eta+C(A+B)$ and $C(A+B)$ are Kahler for sufficiently large $C$, and their difference is $\eta$.

For every actual positive current $T\in[A]$, the ordinary smooth-factor measure $T\wedge A$ has mass $[A]^2=0$ by Stokes and is positive, so it is zero. In a product coordinate chart write the positive coefficient matrix of $T$ in $y,z$ coordinates. The $z\bar z$ diagonal measure is zero, because it is the coefficient detected by wedging with the positive horizontal form $A$. Positivity forces the off-diagonal measures to vanish as well: relative to the sum of diagonal measures, the coefficient matrix has positive semidefinite Radon--Nikodym density almost everywhere, and $|h_{12}|^2\leq h_{11}h_{22}=0$. Thus $T$ has only a horizontal $y\bar y$ coefficient. Its degree-one nonpluripolar part has the same property.

It follows that the kernel is exactly
$$
N=\{\eta\in W:A\wedge\eta=0\}. \tag{Q6}
$$
Necessity follows by testing $u=\psi=0$. Conversely $A\wedge\eta=0$ means the smooth vertical coefficient of $\eta$ is zero pointwise. A purely horizontal current then wedges to zero with $\eta$, proving sufficiency for every actual potential, in particular for the full domain. This is an explicit factorwise geometric characterization in this example, not a general fibration assumption.

The quotient in (Q6) is infinite-dimensional. Choose countably many disjoint coordinate disks in $\mathbb P^1_z$ with an open region left over, and nonzero smooth real bumps $g_j$ supported in those disks. The exact forms $\eta_j=p_2^*dd^cg_j$ are in $W$. A finite linear combination belongs to $N$ only if $dd^c(\sum c_jg_j)=0$ on $\mathbb P^1$. Such a smooth real function is harmonic and constant: integration by parts gives $\int dh\wedge d^ch=0$, so its differential is zero. The function vanishes on the remaining open region, so the constant is zero; disjoint supports imply each $c_j=0$. Thus the quotient images of these exact forms are linearly independent, despite every $\eta_j$ having zero cohomology class and zero scalar mass.

In particular, for a nonconstant smooth $g(z)$ and sufficiently small nonzero $t$,
$$
\omega_0=A+B,\qquad\omega_1=A+B+t\,p_2^*dd^cg
$$
are Kahler and cohomologous, but
$$
L_0(\omega_1)-L_0(\omega_0)=tA\wedge p_2^*dd^cg\ne0,
\qquad\int L_0(\omega_0)=\int L_0(\omega_1)=1.
$$
This reconstructs the same-class obstruction analytically and strengthens it by the exact kernel and infinite-dimensional quotient calculation.

The actual carrier of every measure remains the $n$-dimensional manifold $X$; the bare product has bidegree $(d,d)$. Neither $Q_W$ nor its admissible-power image is a geometric $d$-dimensional carrier. The minimum datum here is the quotient image of the full complementary form, for fixed $X$, actual bounded reference type and actual input current, together with conventions. No numerical-dimension theorem or independently geometric general classification has been proved.


# n4. Perturbation limits, obstruction and residual scope

This note uses n1--n3. There are two distinct verified perturbation statements. Neither permits arbitrary unbounded weights.

**Decreasing full-mass paths in the original background.** Let $\varepsilon_j\downarrow0$, let $u_j\downarrow u$ with every $u_j,u\in\mathcal H_\psi$ and $u_j\in\operatorname{PSH}(X,\theta)$, and let $\omega_j$ be smooth Kahler forms with $[\omega_j]\to\lambda$ for a Kahler class $\lambda$. Suppose there is a smooth Kahler form $\omega$ such that
$$
\rho_\Omega\big(q_W(\omega_j^m)-q_W(\omega^m)\big)\longrightarrow0. \tag{P1}
$$
The form $\omega$ need not represent $\lambda$: both conditions are stated separately, since one controls scalar lower-degree coefficients and the other controls the operator reference. Then
$$
\frac{\langle(T_{u_j}+\varepsilon_j\omega_j)^n\rangle}
{\binom nd\varepsilon_j^m}
\rightharpoonup\overline L_u(q_W(\omega^m))=\langle T_u^d\rangle\omega^m. \tag{P2}
$$
To prove this expand actual positive currents, and use the higher-degree vanishing in n1:
$$
\frac{\langle(T_{u_j}+\varepsilon_j\omega_j)^n\rangle}
{\binom nd\varepsilon_j^m}
=L_{u_j}(\omega_j^m)+
\sum_{k<d}\frac{\binom nk}{\binom nd}\varepsilon_j^{d-k}
\langle T_{u_j}^k\rangle\omega_j^{n-k}. \tag{P3}
$$
Every summand of the remainder is positive. DDNL comparison gives its unscaled mass at most $M_k(\psi,[\omega_j])$. Because $\langle P^k\rangle$ is closed, this reference mass equals its cohomology pairing with $[\omega_j]^{n-k}$, a fixed continuous polynomial. Convergence of classes bounds all these finitely many masses. Thus the remainder has total variation $O(\varepsilon_j)$ for $d\geq1$, uniformly without pointwise bounds on representatives; for $d=0$ there is no remainder. Joint quotient continuity in n3, using (P1) and the decreasing bare-current theorem, gives the leading limit. This proves (P2).

Fixed $u$ in the full domain is allowed by the constant decreasing sequence. In particular fixed-form perturbation convergence holds for every such unbounded $u$, with a positive raw mass. Smooth convergence $\omega_j\to\omega>0$ implies both class convergence and (P1), and is a useful sufficient special case. Equality of quotient images at every $j$, together with convergent classes, is another sufficient case even without convergence of representatives. The theorem supplies independence for all paths satisfying its exact hypotheses and the same limiting datum. It does not assume $u_j$ has bounded differences, finite linear energy or an $o(\varepsilon_j)$ rate. Its essential added hypothesis is that these decreasing currents are positive in the original background and all inputs and their limit have full degree-$d$ mass. It makes no assertion for arbitrary potentials psh only in $\theta+\varepsilon_j\omega_j$.

**Bounded-type perturbed backgrounds.** For completeness, reconstruct the distinct sufficient rate for that latter setting. Fix $v\in\mathcal C_\psi$, let $\omega_\varepsilon\to\omega>0$ smoothly, and suppose $v_\varepsilon\in\operatorname{PSH}(X,\theta+\varepsilon\omega_\varepsilon)$ has the same actual bounded type as $\psi$ and
$$
\delta_\varepsilon=\|v_\varepsilon-v\|_\infty=o(\varepsilon)
$$
off the common pole set. Set $A=T_v+\varepsilon\omega_\varepsilon$, $B=\theta+\varepsilon\omega_\varepsilon+dd^cv_\varepsilon$, $h=v_\varepsilon-v$. Positive multilinearity gives the signed top difference as the sum of $dd^ch$ insertions against
$$
R_{a,\varepsilon}=\langle B^aA^{n-1-a}\rangle,\qquad 0\leq a\leq n-1.
$$
These are closed positive $(n-1,n-1)$ currents with no pluripolar mass, or the smooth current $1$ when $n=1$.

The exact literature IBP used here is Vu v3 Lemmas 2.5--2.6 and Theorem 2.7: for a closed positive $(n-1,n-1)$ current $R$ and bounded $R$-admissible dsh functions $h,f$,
$$
\int f\langle dd^ch\mathbin{\dot\wedge}R\rangle
=\int h\langle dd^cf\mathbin{\dot\wedge}R\rangle
=-\int\langle dh\wedge d^cf\mathbin{\dot\wedge}R\rangle.
$$
Admissible means a representation as differences of quasi-psh functions whose polar sets have zero $R$-mass. The bounded difference $h$ and any smooth real test $f$ meet this condition, because the relative currents have no pluripolar mass. Vu Proposition 2.1(iii) identifies the signed insertion with the difference of the ordinary nonpluripolar products; smooth $dd^cf$ is ordinary multiplication. Source potentials are divided by $2$; source $d^c_s=2d^c$. Both source IBP sides are half ours, so multiplication by $2$ gives the formula displayed here. The correct intrinsic gradient is
$$
dh\wedge d^ch\wedge R=\tfrac12dd^c(h^2)\wedge R-h\,dd^ch\wedge R.
$$
The printed missing half factors on Vu pages 6 and 11 and the older Cauchy--Schwarz defect remain literal in the annex and are not definitions used here. For clarity the cutoff boundary estimate can be checked with the correct formula: if $h=\varphi_1-\varphi_2$, $f=\varphi_3-\varphi_4$ with negative quasi-psh representatives, $dd^c\varphi_i\geq-\Gamma$, put $b_k=1+k^{-1}\max(\sum\varphi_i,-k)$. It is bounded between $0$ and $1$, $dd^cb_k\geq-4\Gamma/k$, and bounded Bedford--Taylor calculus and Stokes give
$$
0\leq\int db_k\wedge d^cb_k\wedge R
=-\int b_kdd^cb_k\wedge R\leq\frac4k\int\Gamma\wedge R.
$$
The truncated differences have uniformly bounded sup norms and diagonal gradient mass at most $2\|h_k\|_\infty\int\Gamma R$, and similarly for $f_k$. Cauchy--Schwarz makes every boundary term with $db_k$ vanish. The nonzero cutoff locus, not its closed support, lies in the simultaneous strict truncation locus. Locality and admissible nonpluripolar gradient finiteness (the cited Lemmas 2.5--2.6) let the intrinsic products pass to the limit off the representation poles; dominated convergence applies since $R$ and the inserted positive products give them no mass. Thus the corrected intrinsic formula gives exactly the scoped IBP application. No erroneous doubled square expansion is used.

Choose $C_f$ uniformly with $-C_f\omega_\varepsilon\leq dd^cf\leq C_f\omega_\varepsilon$, possible by smooth convergence to a positive form. IBP gives
$$
\left|\int f(\langle B^n\rangle-\langle A^n\rangle)\right|
\leq nC_f\delta_\varepsilon
\sum_{k=0}^d\binom{n-1}k\varepsilon^{n-1-k}M_k(\psi,[\omega_\varepsilon]). \tag{P4}
$$
Indeed DDNL Proposition 2.1 applies to the $n-1$ bounded-equivalent slots in the big class $\alpha+\varepsilon[\omega_\varepsilon]$ and one $(\omega_\varepsilon,0)$ slot. Replacing all the varying potential slots by $\psi$ makes their common mixed mass $\int\langle(P+\varepsilon\omega_\varepsilon)^{n-1}\rangle\omega_\varepsilon$, whose positive expansion is precisely the sum in (P4). Since $d<n$, all indices are legal; when $n=1,d=0$ it is the empty-product mass $M_0$. The sum is uniformly $O(\varepsilon^{m-1})$. After rescaling, the test error is $O_f(\delta_\varepsilon/\varepsilon)\to0$. The rescaled masses are uniformly bounded by the same bounded-type comparison and actual reference polynomial. Smooth tests are dense in continuous functions, so convergence on smooth tests proves weak measure convergence. Fixed-current expansion and smooth multiplication then give the limit $L_v(\omega^m)$. This is a sufficient rate only; no optimality or rate-free assertion for perturbed backgrounds is made.

**An analytic obstruction to dropping full-form data.** In the product example of n3 use the fixed potential $u=0$, and alternate the cohomologous forms $\omega_0,\omega_1$ along $\varepsilon_j=1/j$, choosing $\omega_0$ for even $j$ and $\omega_1$ for odd $j$. All backgrounds are Kahler perturbations, all auxiliary classes equal one class, all potentials are identical and bounded, and the class $[A]$ is pseudoeffective of volume zero. Direct smooth expansion gives
$$
\frac{(A+\varepsilon_j\omega_j)^2}{2\varepsilon_j}
=A\wedge\omega_j+\frac{\varepsilon_j}{2}\omega_j^2.
$$
The last term tends to zero in total variation since this is a finite set of smooth forms. The even and odd subsequences tend to $A\wedge B$ and $A\wedge B+tA\wedge p_2^*dd^cg$, respectively, which are distinct positive mass-one measures by n3. Thus class convergence alone, even with zero potential error, does not guarantee a unique limiting operator on $X$. The failed hypothesis in (P1) is convergence of the actual reference datum. This counterexample refutes only a class-only prescription for this full-form operator; it is not an impossibility proof for every possible theory sought in the original atom.

**Catalogue comparison.** New content relative to the supplied narrower operator result is: the full-mass domain is common to every auxiliary form and class; its joint-linear subdomain is likewise common; truncation and mixed decreasing convergence hold for bare currents; the bounded-family reference kernel extends unchanged to the whole full-mass domain; a quantitative quotient norm supplies admissible joint continuity; and an explicit example computes the kernel and its infinite-dimensional quotient. The quotient-path limit (P2) also covers decreasing unbounded full-mass inputs positive in the original background. These are rigorous scoped applications with proofs above, not literature-priority claims or independent certifications. The universal quotient definition itself is a bookkeeping characterization, and is not claimed as an independently geometric classification.

The retained operator data are $X$ and its complex structure, the cohomology class with an actual bounded singularity type dominating the domain, the actual positive input current, the actual-current degree $d$, and $q_W(\omega^m)$ for an admissible full-form reference. The smooth $\theta$ is a gauge; a particular bounded-equivalent anchor is not additional operator datum. The carrier is explicitly $X$, of complex dimension $n$; the product current has bidegree $(d,d)$, raw positive mass is (Q5), and there is no probability normalization. The degree need not equal numerical dimension: in the product class $[A]$, the logarithmic actual reference with current $[\{y=0\}\times\mathbb P^1]$ has zero degree-one nonpluripolar part and hence $d=0$, while the smooth reference has $d=1$. The logarithmic potential is $p_1^*\log(|y|^2/(1+|y|^2))$; in our convention $dd^c\log|y|^2=\delta_0$ by boundary flux $4\pi$ and $dd^c=(\Delta/4\pi)$ times planar area. Subtracting $dd^c\log(1+|y|^2)=\kappa$ gives the asserted divisor current. Its nonpluripolar part is zero because it is supported on its pole set. The nef class has numerical dimension $1$ by its nonzero first cup product and zero square.

Original P15.2 remains open in the dossier's residual scope. The measure construction uses a prescribed-type relative full-mass domain and specified perturbation classes; it supplies no intrinsic geometric $d$-dimensional carrier, no independently geometric general characterization of the reference kernel, no numerical-dimension identification, no identification of actual reference mass with a leading class-volume coefficient, and no independence for arbitrary genuinely perturbed-background unbounded paths. Full-mass limits and the reference-datum convergence hypotheses in (P2), and bounded type plus smooth auxiliary convergence and $o(\varepsilon)$ error in (P4), must be retained. No increasing-sequence continuity or varying unbounded-weight calculus is proved. Proposal 3 about an energy quotient is deliberately not investigated in this P15.2-only assignment; no P15.1 assertion is needed. The optional degree-zero rigidity question is left unanswered without treating it as a blocker. Status is partial and candidate is false.


# Execution and research audit

The unchanged input is `input.json` and its byte-identical `input-original.json`; SHA256 `6e953383fbcc187eb12cfdb80e66ddc2111de519b0c9c9a147ecc2bc58c0dbf7` (377686 bytes). `assignment-original.txt` retains the exact decoded assignment string; `task-original.json` retains its task values. The authoritative review deliverable is `P15.2-argument.md`, including every new proof and the complete indispensable primary bodies. `P15.2-proof.md` contains its authored proof portion. `P15.2-partial.tex` and `P15.2-partial.pdf` contain the entire new proof and all controlling theorem statements and applicability checks; raw printed bodies are in the Markdown annex to preserve UTF-8, form feeds, and defects.

Observed source audit: 24/24 selected LF-range pins match. Fourteen primary supplied bodies also match their literal ranges and occur unchanged in the original assignment. DGMS/GZ text and PDF pins match. All 36 supplied fenced quotation strings are separately preserved in `supplied-quotation-archive.json`. `source-audit.json` records exact filenames, LF bounds, hashes, and boundary framing. Published foundations, source defect qualifications, and their applications are stated in the proof. The convergence of the bare current is additionally reconstructed by bounded cutoffs and capacity; no general unbounded-factor strengthening of Vu v3 Theorem 3.3 is used. No earlier proof or independent-worker output is used without reconstruction.

Observed exact finite diagnostics: 465 normalization cases and 6 formal surface wedge cases passed. These are exhaustive only on the program's stated finite inputs, not proofs of analytic results. Two `pdflatex` passes completed with return code zero; PDF text extraction found all required proof sections. The PDF SHA256 is `939c1e12a220933121c09553621865990b14b5f6ef7b91dff152c74ab33ffe56`. Build commands, outputs, environment versions and hashes are in `build-audit.json` and their named logs. Compilation is not mathematical certification.

Requested execution identity: native Codex `gpt-6.1-sol`, reasoning `xhigh`. No model switching or additional model/subagent was invoked. The runtime does not provide a signed backend/effort attestation, so the requested identity is recorded as requested rather than independently certified. No network call, install, external message, auth/proxy/CA or HOME/CODEX_HOME change, SQL/runtime edit, or old-artifact write was performed. Source files were read only; new work is restricted to the fresh workspace. No resource-heavy computation was required. No operator-provided supervised compute facility was found among the available tools; heavy computation was neither attempted nor needed.

Research disposition: proposals 1 and 2 are proved in the common-domain scope; proposal 4 is proved with fixed smooth-factor and specified decreasing/mixed continuity, plus quantified quotient continuity and a concrete geometric kernel example. The purely definitional quotient step is explicitly distinguished from the new kernel extension. Proposal 3 belongs to the independently assigned energy problem and is not investigated. Optional degree-zero rigidity is not assumed. The full original P15.2 is not solved; status is partial and candidate is false.

Rerun from this directory: `python verify_sources.py`, `python checks.py`, `python build.py`, `python package_notes.py`. `status.json` has exactly the requested five keys. `notes.json` is the canonical native note object; support arrays contain earlier local IDs only. All drafts remain unverified; no literature-priority or external correctness certification is claimed.


# Immutable primary-source annex

These bodies are mathematical source data. New proofs and corrected formulas are above. Historical review assertions are not grants; source bytes and statement applicability were checked independently. No source file is modified.

## Source unit 1: Bounded/nonpluripolar product properties

BEGZ-0812.3674v2-20261004.txt, LF249--322. Independent range SHA256 `1dada113d7a3c9897039047fef2fa9aa9922f3c359092bbbfc416fab3823e0b2`. Supplied literal body is unchanged; boundary LF framing is separately recorded. Printed defects remain source data.

```text
    We now collect some basic properties of non-pluripolar products.
Proposition 1.4. Let u1 , ..., up be psh functions on X.
    • The operator                              ^
                            (u1 , ..., up ) 7→ h ddc uj i
                                                 j
         is local in theVplurifine topology whenever well-defined.
       • The current h j ddc uj i and the fact that it is well-defined both only depend
         on the currents ddc uj , not on the specific potentials uj .
       • Non-pluripolar products, which are obviously symmetric, are also multi-
         linear in the following sense: if v1 is a further psh function, then
                           ^                       ^                      ^
     h(ddc u1 + ddc v1 ) ∧    ddc uj i = hddc u1 ∧   ddc uj i + hddc v1 ∧    ddc uj i
                          j≥2                        j≥2                        j≥2

         in the sense that the left-hand side is well-defined iff both terms in the
         right-hand side are, and equality holds in that case.
Proof. Let us prove the ﬁrst point. If uj and vj are psh functions on X such
that uj = vj on a given pluriﬁne open subset O, then the locally bounded psh
functions max(uj , −k) and max(vj , −k) also coincide on O. If we set
                            \               \
                      Ek := {uj > −k} ∩ {vj > −k},
                                 j                   j

then we infer
                      ^                                      ^
              1O∩Ek       ddc max(uj , −k) = 1O∩Ek               ddc max(vj , −k),
                      j                                      j

hence in the limit               ^               ^
                             1O h ddc uj i = 1O h ddc vj i
                                 j                       j
              MONGE-AMPÈRE EQUATIONS IN BIG COHOMOLOGY CLASSES                               7

as desired by Lemma 1.5 below.
   We now prove the second point. Let wj be pluriharmonic on X, and let K be a
compact subset. We can ﬁnd C > 0 such that wj ≤ C on an open neighborhood
V of K. On the pluriﬁne open subset
                  \                         \
             Ok := {uj + wj > −k} ∩ V ⊂ {uj > −k − C} ∩ V
                         j                               j

the following locally bounded psh functions coincide:
     max(uj + wj , −k) = max(uj , −wj − k) + wj = max(uj , −k − C) + wj .
Since ddc wj = 0, it follows that
   Z           ^                         Z                         ^
         n−p          c
       ω     ∧    dd max(uj + wj , −k) =                 ω n−p ∧       ddc max(uj , −k − C)
    Ok           j                                  Ok             j
                     Z                              ^
                ≤    T                    ω n−p ∧       ddc max(uj , −k − C)
                         j {uj >−k−C}∩V             j
which is uniformly bounded in k by assumption, and the second point is proved.
   The proof of the last point is similarly easy but tedious and will be left to the
reader.                                                                           
                                                          V
Lemma 1.5. Assume that the non-pluripolar product h j ddc uj i is well-defined.
Then for every sequence of Borel subsets Ek such that
                                       \
                                Ek ⊂ {ui > −k}
                                             j
          S
and X −    k Ek is pluripolar, we have
                                   ^                        ^
                         lim 1Ek       ddc max(uj , −k)i = h ddc uj i
                         k→∞
                                   j                           j

against all bounded measurable functions.
Proof. This follows by dominated convergence from
                             ^                               ^
        (1∩j {uj >−k} − 1Ek ) ddc max(uj , −k)i ≤ (1 − 1Ek )h ddc uj i.
                                   j                                        j

                                                                                              
```

## Source unit 2: Class positive-product and volume definition

BEGZ-0812.3674v2-20261004.txt, LF810--840. Independent range SHA256 `aa1c54651a97636414c96f9ae8d1815cfcfc49c8d8fbd8f02b7fd6f1a9306d3e`. Supplied literal body is unchanged; boundary LF framing is separately recorded. Printed defects remain source data.

```text
Definition 1.17. Let α1 , ...αp ∈ H 1,1 (X, R) be big cohomology classes, and let
Ti,min ∈ αi be a positive current with minimal singularities. Then the cohomology
class of the non-pluripolar product hT1,min ∧ · · · ∧ Tp,min i is independent of the
choice of Ti,min ∈ αi with minimal singularities. It will be denoted by
                              hα1 · · · αp i ∈ H p,p (X, R)
18                 S. BOUCKSOM, P. EYSSIDIEUX, V. GUEDJ, A.ZERIAHI

and called the positive product of the αi . If α1 , ..., αn are merely psef, we set
                      hα1 · · · αp i := lim h(α1 + εβ) · · · (αp + εβ)i
                                      ε→0

where β ∈ H 1,1 (X, R) is an arbitrary Kähler class.
     As a special case, given a big class α the positive number
                                      vol(α) := hαn i
is called the volume of α
   Some explanations are in order. The positive product hα1 · · · αp i is not multi-
linear since the fact that T ∈ α and T ′ ∈ α′ both have minimal singularities
(in their respective cohomology classes) doesn’t imply that T + T ′ has minimal
singularities in α + α′ . Positive products are however homogeneous and non-
decreasing in each variable αi thanks to Theorem 1.16 when the αi ’s is big (with
respect to the partial order on cohomology induced by positive currents). These
two properties imply in a completely formal way (cf. Proposition 2.9 in [14]) that
hα1 · ... · αp i depends continuously on the p-tuple (α1 , ..., αp ) of big classes. We
can thus extend positive products to psef classes αi as indicated, the existence
of the limit and its independence on β being easy to check by monotonicity of
positive products.
   As an important special case, note that the positive product of nef classes αi
coincides with their ordinary cup-product, that is
                                 hα1 · · · αp i = α1 · · · αp .
   The volume vol(α) considered here coincides (as it should!) with the one
introduced in [11]. In fact:
```

## Source unit 3: Pseudoeffective bounded-type mixed mass equality, full proof

DDNL18-2049-2087-20261004.txt, LF319--347. Independent range SHA256 `e8359844609c8b19e21d4c36df028505fde5b80cc75e59f274dd4b5d282fa62e`. Supplied literal body is unchanged; boundary LF framing is separately recorded. Printed defects remain source data.

```text
Proposition 2.1. Let θ j , j ∈ {1, . . . , n}, be smooth closed real (1, 1)-forms on X whose cohomology
classes are pseudoeffective. Let u j , v j ∈ PSH(X, θ j ) be such that u j has the same singularity type as v j ,
j ∈ {1, . . . , n}. Then
                                  Z                           Z
                                        θu 1 ∧ · · · ∧ θu n =
                                          1             n
                                                                θv11 ∧ · · · ∧ θvnn .
                                            X                         X

   The proof of this result uses the arguments in [Boucksom et al. 2010, Corollary 2.15].

Proof. First we note that we can assume that the classes {θ j } are in fact big. Indeed, if this is not the
case we can just replace each θ j with θ j + εω, and using the multilinearity of the nonpluripolar product
[Boucksom et al. 2010, Proposition 1.4] we can let ε → 0 at the end of our argument to conclude the
statement for pseudoeffective classes.
   For each t ∈ 1 = {t = (t1 , . . . , tn ) ∈ Rn | t j > 0} consider u t := j t j u j , vt := j t j v j and θ t := j t j θ j.
                                                                           P                 P                    P

Clearly, {θ t } is big, and u t has the same singularities as vt . Hence it follows from [Witt Nyström 2017,
Theorem 1.2] that X (θutt )n = X (θvtt )n for all t ∈ 1. On the other hand, using multilinearity of the
                       R             R

nonpluripolar product again [Boucksom et al. 2010, Proposition 1.4], we see that both t → X (θutt )n and
                                                                                                             R

t → X (θvtt )n are homogeneous polynomials of degree n. Our last identity forces all the coefficients of
     R

these polynomials to be equal, giving the statement of our result.                                                       
```

## Source unit 4: Pseudoeffective mass monotonicity, full proof

DDNL18-2049-2087-20261004.txt, LF448--469. Independent range SHA256 `e4220e2892907b2d1d5b17de4aa57b3b1542060bda2e4dfcf8944f945cba0c20`. Supplied literal body is unchanged; boundary LF framing is separately recorded. Printed defects remain source data.

```text
Theorem 2.4. Let θ j, j ∈ {1, . . . , n}, be smooth closed real (1, 1)-forms on X whose cohomology classes
are pseudoeffective. Let u j , v j ∈ PSH(X, θ j ) be such that u j is less singular than v j for all j ∈ {1, . . . , n}.
Then                                  Z                       Z
                                        θu 1 ∧ · · · ∧ θu n ≥
                                          1             n
                                                                θv11 ∧ · · · ∧ θvnn .
                                                   X                            X
        MONOTONICITY OF NONPLURIPOLAR PRODUCTS AND COMPLEX MONGE–AMPÈRE EQUATIONS                                    2057


Proof. By the same reason as in Proposition 2.1, we can assume that the classes {θ j } are in fact big. For
each t > 0 we set v jt := max(u j − t, v j ) for j = 1, . . . , n. Observe that the v jt converge decreasingly to v j
as t → ∞. In particular, by [Guedj and Zeriahi 2005, Proposition 3.7] the convergence holds in capacity.
As v jt and u j have the same singularity type, it follows from Proposition 2.1 that
                                   Z                          Z
                                       θu 1 ∧ · · · ∧ θu n =
                                          1            n
                                                                  θv1t ∧ · · · ∧ θvnnt .
                                                                           1
                                        X                            X

Letting t → ∞, the first part of Theorem 2.3 allows us to conclude the argument.                                       
```

## Source unit 5: Bounded type and signed-product convention

Xia-1907.06359v1-20261004.txt, LF250--265. Independent range SHA256 `ea927250996b0a51fa4f7aa3612fd7e300be9c3327b0776093caacb4cc9f97f3`. Supplied literal body is unchanged; boundary LF framing is separately recorded. Printed defects remain source data.

```text
2.4. Integration by parts. In the sequel, for ϕ1 , ϕ2 ∈ PSH(X, θ), we write [ϕ1 ] =
[ϕ2 ] if there is a constant C > 0, such that
                                      ϕ2 − C ≤ ϕ1 ≤ ϕ2 + C.
Theorem 2.7. Let γ1 , . . . , γn−1 ∈ PSH(X, θ). Let ϕj , ψj ∈ PSH(X, θ) (j = 1, 2).
Let u = ϕ1 − ϕ2 , v = ψ1 − ψ2 . Assume that
                                     [ϕ1 ] = [ϕ2 ],    [ψ1 ] = [ψ2 ].
Then
          Z                                                Z
(2.8)           u ddc v ∧ θγ1 ∧ · · · ∧ · · · ∧ θγn−1 =         v ddc u ∧ θγ1 ∧ · · · ∧ · · · ∧ θγn−1 .
            X                                               X

Remark 2.2. Here
ddc v ∧ θγ1 ∧ · · · ∧ · · · ∧ θγn−1 := θψ1 ∧ θγ1 ∧ · · · ∧ · · · ∧ θγn−1 − θψ2 ∧ θγ1 ∧ · · · ∧ · · · ∧ θγn−1
is understood as a signed measure. This definition is independent of the choice of
θψ1 and θψ2 by [BEGZ10] Proposition 1.4. Other similar expressions are understood
in the same way.
```

## Source unit 6: Mixed big-class IBP Corollary2.15, full printed proof

Xia-1907.06359v1-20261004.txt, LF780--829. Independent range SHA256 `fe693acf6a3033eb6bed734b0c9d194f4e59497e7aabf4c646bfbccf87bc72c8`. Supplied literal body is unchanged; boundary LF framing is separately recorded. Printed defects remain source data.

```text
Corollary 2.15. Let αj (j = 0, . . . , n) be big cohomology classes on X. Let θj
(j = 0, . . . , n) be smooth representatives in αj . Let γj ∈ PSH(X, θj ) (j = 2, . . . , n).
Let ϕ1 , ϕ2 ∈ PSH(X, θ0 ), ψ1 , ψ2 ∈ PSH(X, θ1 ). Let u = ϕ1 − ϕ2 , v = ψ1 − ψ2 .
Assume that
                                 [ϕ1 ] = [ϕ2 ], [ψ1 ] = [ψ2 ].
Then
         Z                                                       Z
(2.21)        u ddc v ∧ θ2,γ2 ∧ · · · ∧ · · · ∧ θn,γn =                  v ddc u ∧ θ2,γ2 ∧ · · · ∧ · · · ∧ θn,γn .
          X                                                       X

Proof. Take α = (a0 , . . . , an ) ∈ Rn+1
                                      ≥0 . Let
                                                     n
                                                     X
                                             θα =          aj θj .
                                                     j=0

Let
                                  n
                                  X
                          γα =          aj γj ,   γ̃α = a0 ϕ1 + a1 ψ1 + γα .
                                  j=2

Note that
                    a0 u = (a0 ϕ1 + a1 ψ1 + γα ) − (a0 ϕ2 + a1 ψ1 + γα ) ,
                    a1 v = (a0 ϕ1 + a1 ψ1 + γα ) − (a0 ϕ1 + a1 ψ2 + γα ) .
So by Theorem 2.7,
                             Z                                       Z
                     a0 a1       u ddc v ∧ θα,γ̃
                                            n−1
                                                 α
                                                   = a0 a1                 v ddc u ∧ θα,γ̃
                                                                                      n−1
                                                                                           α
                                                                                             .
                             X                                        X
So for a0 > 0, a1 > 0,
                             Z                           Z
                                 u ddc v ∧ θα,γ̃
                                            n−1
                                                 α
                                                   =             v ddc u ∧ θα,γ̃
                                                                            n−1
                                                                                 α
                                                                                   .
                             X                             X
Since both sides are polynomials in a0 , . . . , an , this means that all coefficients are
equal. In particular, the coefficients of
                                                  a 2 . . . an
are equal, hence proving (2.21).                                                                                          
```

## Source unit 7: Literal operator convention

Vu-2004.11111v1-20261004.txt, LF178--189. Independent range SHA256 `13226a964e640ebeb8283a6342682cdf2f98a328d37f5386efe3e2e844ca2cef`. Supplied literal body is unchanged; boundary LF framing is separately recorded. Printed defects remain source data.

```text
supported by a postdoctoral fellowship of the Alexander von Humboldt Foundation.

Notation and convention. For a closed positive current T on a compact complex man-
ifold X, we denote by {T } the cohomology class of T and ν(T, x) denotes the Lelong
number of T at x. Recall that the wedge product on closed smooth forms induces the
cup-product on their de Rham cohomology classes. We use the same notation “ ∧ ” to
denote these two products.
    Recall dc = 2πi (∂ − ∂) and ddc = πi ∂∂. We use &, . to denote ≥, ≤ modulo some
multiplicative constant independent of parameters in question. For a Borel set A ⊂ X,
we denote by 1A the characteristic function of A, that means 1A is equal to 1 on A and 0
elsewhere. For every current R of order 0 on X, we denote by kRkA the mass of R on A.

```

## Source unit 8: Theorem2.6 and Remark2.7, full printed convergence proof

Vu-2004.11111v1-20261004.txt, LF580--642. Independent range SHA256 `c097f459c8e4b862a8067519ab86b09613638b11af2d3e83b3766244458bf625`. Supplied literal body is unchanged; boundary LF framing is separately recorded. Printed defects remain source data.

```text
Theorem 2.6. Let U ⊂ Cn be an open set. Let (Tk )k be a sequence of closed positive currents
satisfying Condition (∗) so that Tk converges to a closed positive current T on U as k → ∞.
Let uj be a locally bounded psh function on U for 1 ≤ j ≤ m. Let (ujk )k∈N be a sequence of
locally bounded psh functions converging to uj in L1loc as k → ∞. Then, the convergence

                u1k ddc u2k ∧ · · · ∧ ddc umk ∧ Tk → u1 ddc u2 ∧ · · · ∧ ddc um ∧ T    (2.10)

as k → ∞ holds provided that one of the following conditions is fulfilled:
    (i) ujk (x) ր uj (x) for every x ∈ U as k → ∞,
    (ii) ujk (x) ր uj (x) for almost everywhere x ∈ U (with respect to the Lebesgue measure)
and T has no mass on pluripolar sets,
    (iii) ujk ≥ uj for every j, k.

Proof. Given that we already have a uniform strong quasi-continuity for bounded psh
functions, the desired result can be deduced without difficulty from proofs of classical
results on the convergence of Monge-Ampère operators, for example, see [17].
   We present here a proof of Theorem 2.6 for the readers’ convenience. First of all,
observe that if ujk ր uj almost everywhere then, we have ujk ≤ uj(k+1) ≤ uj pointwise
on U and the set {x ∈ U : uj (x) 6= limk→∞ ujk (x)} is pluripolar. By the localization




                                                11
principle ([17, Page 7]), we can assume that ujk , uj are all equal to some smooth psh
function ψ outside some set K ⋐ U on U. We prove (i), (ii) simultaneously. Let

            Sjk := ddc ujk ∧ · · · ∧ ddc umk ∧ Tk ,   Sj := ddc uj ∧ · · · ∧ ddc um ∧ T.

We prove by induction in j that

                                      u(j−1)k Sjk → u(j−1) Sj                              (2.11)

k and for every 2 ≤ j ≤ m + 1 (by convention we put S(m+1)k := Tk and Sm+1 := T ). The
claim is true for j = m + 1. Suppose that it holds for (j + 1). We need to prove it for
j. Let Rj∞ be a limit current of u(j−1)k Sjk as k → ∞. By induction hypothesis (2.11) for
(j + 1) instead of j, Sjk → Sj as k → ∞. This combined with the fact that the sequence
(ujk )k converges in L1loc to uj gives

                                          Rj∞ ≤ uj−1Sj                                     (2.12)

(one can see [15, Proposition 3.2]). On the other hand, since (ujk )k is increasing, using
Corollary 2.5, we obtain

                       lim inf u(j−1)k Sjk ≥ lim inf u(j−1)s Sjk = u(j−1)s Sj
                        k→∞                   k→∞

for every s ∈ N. Letting s → ∞ in the last inequality gives

                 Rj∞ ≥ ( lim u(j−1)s )Sj = uj−1Sj + ( lim u(j−1)s − uj−1)Sj .              (2.13)
                          s→∞                             s→∞

Recall that the set of x ∈ U with uj−1(x) > lims→∞ u(j−1)s (x) is empty in the setting of
(i) and is a pluripolar set in the setting of (ii). Hence (2.11) follows from Lemma 2.1,
(2.13) and (2.12). We have proved (i) and (ii). We prove (iii) by similar induction. The
proof is finished.

Remark 2.7. By the above proof and Lemma 2.1, Property (ii) of Theorem 2.6 still holds if
instead of requiring T has no mass on pluripolar sets, we assume the following two condi-
tions:
    (i) T has no mass on Aj := {x ∈ U : uj (x) 6= limk→∞ ujk (x)} for every 1 ≤ j ≤ m and,
    (ii) the set Aj is locally complete pluripolar for every j.
    Just by replacing the usual quasi-continuity of psh functions by the stronger one given
```

## Source unit 9: Relative definitions and Proposition3.5 with full printed proof

Vu-2004.11111v1-20261004.txt, LF945--1115. Independent range SHA256 `b344c4bd11aa3280719cd1b8a3f08d8fff48bb7600168dd303519fb16061142d`. Supplied literal body is unchanged; boundary LF framing is separately recorded. Printed defects remain source data.

```text
Definition 3.3. We say that the non-pluripolar product relative to T of T1 , . . . , Tm is well-
defined if (3.2) holds for every small enough local chart U of X, or equivalently, (3.7)
holds. In this case, the non-pluripolar product relative to T of T1 , . . . , Tm , which is denoted
                    ˙ i, is defined to be the current R̃ in Lemma 3.2.
by hT1 ∧ · · · ∧ Tm ∧T
   When T is the current of integration along X, we simply write hT1 ∧ · · · ∧ Tm i for the
non-pluripolar product relative to T of T1 , . . . , Tm . One can see that this is exactly the
usual non-pluripolar product of T1 , . . . , Tm defined in [2, 16, 4]. We note that in general
                             ˙ i can have mass on pluripolar sets in ∩m
the current hT1 ∧ · · · ∧ Tm ∧T                                              j=1 {uj > −∞},
see, however, Property (iii) of Proposition 3.5 below. Arguing as in the proof of [4,
Proposition 1.6], we obtain the following result.
                                                                               ˙ i is
Lemma 3.4. Assume that X is a compact Kähler manifold. Then, hT1 ∧ · · · ∧ Tm ∧T
well-defined.
    For a closed positive (1, 1)-current R, recall that the polar locus IR of R is the set of
points where potentials of R are equal to −∞. Note that by Lemma 3.1, the current
                 ˙ i has no mass on ∪m
hT1 ∧ · · · ∧ Tm ∧T                   j=1 ITj . We collect here some more basic properties of
relative non-pluripolar products.
Proposition 3.5. (i) The product hT1 ∧ · · · ∧ Tm ∧T  ˙ i is symmetric with respect to T1 , . . . , Tm .
      (ii) Given a positive real number λ, we have h(λT1 ) ∧ T2 ∧ · · · ∧ Tm ∧T˙ i = λhT1 ∧ T2 ∧
             ˙
· · · ∧ Tm ∧T i.
      (iii) Given a complete pluripolar set A such that T has no mass on A, then hT1 ∧ T2 ∧
· · · ∧ Tm ∧T˙ i also has no mass on A.
      (iv) Let T1′ be a closed positive (1, 1)-current on X and Tj , T as above. Assume that
h∧m         ˙       ′    m      ˙                                    ′     m      ˙
     j=1 Tj ∧T i, hT1 ∧ ∧j=2 Tj ∧T i are well-defined. Then h(T1 + T1 ) ∧ ∧j=2 Tj ∧T i is also well-
defined and satisfies

                (T1 + T1′ ) ∧ ∧m      ˙           m      ˙        ′    m      ˙
                               j=2 Tj ∧T ≤ hT1 ∧ ∧j=2 Tj ∧T i + hT1 ∧ ∧j=2 Tj ∧T i.             (3.12)

The equality occurs if T has no mass on IT1 ∪ IT1′ .
    (v) Let 1 ≤ l ≤ m be an integer. Let Tj′′ be a closed positive (1, 1)-current on X and Tj , T
as above for 1 ≤ j ≤ l. Assume that Tj′′ ≥ Tj for every 1 ≤ j ≤ l and T has no mass on
∪lj=1 ITj′′ −Tj . Then, we have

                             h∧lj=1Tj′′ ∧ ∧m        ˙        m      ˙
                                           j=l+1 Tj ∧T i ≥ h∧j=1 Tj ∧T i


provided that the left-hand side is well-defined.
   (vi) Let 1 ≤ l ≤ m be an integer. Assume R := h∧m               ˙          l      ˙
                                                          j=l+1 Tj ∧T i and h∧j=1 Tj ∧Ri are
                                m     ˙ i = h∧j=1 Tj ∧Ri.
well-defined. Then, we have h∧j=1 Tj ∧T         l    ˙




                                                  17
                                                                           ˙ i is well-defined.
   (vii) Let A be a complete pluripolar set. Assume that hT1 ∧T2 ∧· · ·∧Tm ∧T
Then we have

                                          ˙ i = T1 ∧ T2 ∧ · · · ∧ Tm ∧(1
               1X\A hT1 ∧ T2 ∧ · · · ∧ Tm ∧T                         ˙ X\A T ) .

In particular, the equality
                                     h∧m      ˙        m      ˙ ′
                                       j=1 Tj ∧T i = h∧j=1 Tj ∧T i

holds, where T ′ := 1X\∪m
                        j=1 ITj
                                T.

Proof. Properties (i), (ii) are clear from the definition and the proof of Lemma 3.1. We
now check (iii). Let R := h∧m          ˙
                                j=1 Tj ∧T i. Since T has no mass on the complete pluripolar
set A, using Lemma 2.1 gives 1A ∧m            c
                                       j=1 dd ujk ∧ T = 0 for every k. Using this and Lemma
3.1, we deduce that

                   1A 1∩m
                        j=1 {uj >−k}
                                     R = 1A 1∩m
                                              j=1 {uj >−k}
                                                           ∧m     c
                                                            j=1 dd ujk ∧ T = 0.


Hence R = 0 on A and (iii) follows.
   We prove (iv). We work on a small local chart U. Write Tj′ = ddc u′j , u′jk := max{u′j , −k}.
Recall Tj = ddc uj . We can assume uj , u′j ≤ 0. Let R′ := hT1′ ∧ ∧m           ˙
                                                                      j=2 Tj ∧T i and R :=
                                                                                           ′′

h(T1 + T1′ ) ∧ ∧m      ˙
                j=2 Tj ∧T i. We have


                                max{u1 + u′1 , −k} = u1k + u′1k

on {u1 + u′1 > −k} because the last set is contained in {u1 > −k} ∩ {u′1 > −k}. This
combined with Lemma 3.1 yields

                                      1Bk′′ R′′ = 1Bk′′ R + 1Bk′′ R′ ,

where Bk′′ := {u1 + u′1 > −k} ∩ ∩m
                                 j=2 {uj > −k}. Letting k → ∞ in the last equality gives
(3.12). Observe that
                              1U \Bk′′ R → 1IT1 ∪IT ′ ∪ ∪m
                                                         j=2 ITj
                                                                 R
                                                            1

as k → ∞. The last limit is equal to 1IT ′ R because R has no mass on ∪m      j=1 ITj . Moreover
                                          1
since IT1′ is complete pluripolar and T has no mass on IT1′ , by (iii), we have that 1IT ′ R = 0.
                                                                                         1
Consequently, 1U \Bk′′ R → 0 as k → ∞ and a similar property of R′ also holds. Thus we
obtain the equality in (3.12) if T has no mass on IT1 ∪ IT1′ . To get (v), we just need to
decompose Tj′′ = Tj + Tj′ for some closed positive current Tj′ and use similar arguments
as in the proof of (iv).
    We prove (vi). We can assume uj ≤ 0 for every 1 ≤ j ≤ m. Let
                                                      m
                                          −1
                                                     X
                               ψk := k         max          uj , −k + 1.
                                                      j=1


Observe that 0 ≤ ψk ≤ 1 and

                                ψk = 0         on ∪m
                                                   j=1 {uj ≤ −k}.




                                                     18
Note that R has no mass on ITj for l + 1 ≤ j ≤ m. This combined with (iii) yields
               ˙
that h∧lj=1 Tj ∧Ri   gives no mass on ITj for 1 ≤ j ≤ m. Using this and the fact that
ψk ր 1X\∪m  j=1 ITj
                    yields

                h∧lj=1Tj ∧Ri
                         ˙   = lim ψk h∧lj=1 Tj ∧Ri
                                                ˙   = lim ψk ∧lj=1 ddc ujk ∧ R.            (3.13)
                                 k→∞                     k→∞

Now since ψk R = ψk ∧m       c
                     j=l+1 dd ujk ∧ T (Lemma 3.1), we get


                           ψk ∧lj=1 ddc ujk ∧ R = ψk ∧m     c
                                                      j=1 dd ujk ∧ T.                      (3.14)

To see why the last equality is true, notice that it is clear if ujk ’s are smooth and in
general, we can use sequences of smooth psh functions decreasing to ujk for 1 ≤ j ≤ l
and the convergences of Monge-Ampère operators to obtain (3.14). Combining (3.14)
with (3.13) gives the desired assertion.
   It remains to prove (vii). Let ψk be as above.   Let A = {ϕ = −∞}, where ϕ is a
                                                  Pm
negative psh function. Define ψk := k max ϕ + j=1 uj , −k + 1. Since 0 ≤ ψk′ ≤ ψk ,
                                ′     −1
                                             

we get {ψk = 0} ⊂ {ψk′ = 0}. It follows that

        ψk′ hT1 ∧ T2 ∧ · · · ∧ Tm ∧T
                                  ˙ i = ψk′ ∧m     c           ′  m     c
                                             j=1 dd ujk ∧ T = ψk ∧j=1 dd ujk ∧ (1X\A T )

because T = 1X\A T on {ψk′ 6= 0} and the convergence of Monge-Ampère operators.
Letting k → ∞ gives the desired assertion. The proof is finished.
   The following result clarifies the relationship between the relative non-pluripolar
product and some other known notions of intersection.
```

## Source unit 10: Theorem3.7 with full closedness proof

Vu-2004.11111v1-20261004.txt, LF1200--1247. Independent range SHA256 `e12bdb4d6ebd643be2cf987df4ee89b060c1b8930c06b2bc8c8df732630376aa`. Supplied literal body is unchanged; boundary LF framing is separately recorded. Printed defects remain source data.

```text
Theorem 3.7. Assume that hT1 ∧ · · · ∧ Tm ∧T                                         ˙ i is
closed.

Proof. The proof is based on ideas from [20, 4]. We work on a local chart U as above.
By shrinking U and subtracting from uj a suitable constant, we can assume that uj ≤ 0.
Let                                         m
                                            X
                            ψk := k −1 max{   uj , −k} + 1.
                                                j=1

Observe that ψk = 0 on ∪m
                        j=1 {uj ≤ −k} and 0 ≤ ψk ≤ 1 increases to 1∩m
                                                                    j=1 {uj >−∞}
                                                                                 .
                                                                                Let
                                                              ′        ′
g : R → R be a non-negative smooth function such that g(0) = g (0) = g (1) = 0 and
g(1) = 1. Let Rk , R be as above. Since g(1) = 1 and g(0) = 0, we get g(ψk )R → R



                                               20
as k → ∞ (recall R has no mass on ∪m
                                   j=1 {uj = −∞}). Thus the desired assertion is
equivalent to proving that
                                     dR = lim d(g(ψk )R) = 0.                                    (3.19)
                                            k→∞

Since g(ψk ) = g(0) = 0 on ∪m
                            j=1 {uj ≤ −k}, we have

                            d(g(ψk )R) = d(g(ψk )Rk ) = g ′ (ψk )dψk ∧ Rk
(see [4, Lemma 1.9] or Corollary 2.5 for the second equality). Let U1 ⋐ U2 be relatively
compact open subsets of U. By the Cauchy-Schwarz inequality, we have
                  kg ′(ψk )dψk ∧ Rk kU1 . kdψk ∧ dc ψk ∧ Rk kU1 kg ′(ψk )2 Rk kU1 .
Using dψk ∧ dc ψk = ddc ψk2 − ψk ddc ψk and the Chern-Levine-Nirenberg inequality, one get
                 kdψk ∧ dc ψk ∧ Rk kU1 . kψk Rk kU2 ≤ kRk kU 2 ∩∩m
                                                                 j=1 {uj >−k}
                                                                              .1

by (3.2). On the other hand, using the equality g ′ (ψk ) = g ′ (0) = 0 on {uj ≤ −k}, we
obtain
                    g ′(ψk )2 Rk = g ′(ψk )2 1∩m
                                               j=1 {uj >−k}
                                                            Rk = g ′(ψk )2 R
converging to 0 as k → ∞ because g ′(ψk ) → g ′ (1) = 0 on ∩m
                                                            j=1 {uj > −∞}. Thus (3.19)
follows. This finishes the proof.
```

## Source unit 11: Lemma4.1, Proposition4.2 and Theorem4.4 with full printed proofs

Vu-2004.11111v1-20261004.txt, LF1259--1565. Independent range SHA256 `09034b5477c57c8812f3b677bf5ba3504db9a417938f90d7fb91fd28903246a8`. Supplied literal body is unchanged; boundary LF framing is separately recorded. Printed defects remain source data.

```text


4     Monotonicity
In this section, we present a monotonicity property for relative non-pluripolar products.
We begin with the following simple lemma.
Lemma 4.1. Let U be an open subset of Cn . Let (ulj )l be a sequence of psh functions on U
and uj a psh function on U for 1 ≤ j ≤ m. Let (Tl )l be a sequence of closed positive currents
satisfying Condition (∗) and Tl converges to a closed positive current T on U as l → ∞.
Assume that one of the following conditions is satisfied:
    (i) ulj ≥ uj and ulj converges to uj in L1loc as l → ∞.
    (ii) ulj increases to uj as l → ∞ almost everywhere and T has no mass on pluripolar
sets.
    Then, for every smooth weakly positive form Φ with compact support in U, we have
                           Z                            Z
                    lim inf h∧j=1 dd uj ∧Tl i ∧ Φ ≥ h∧m
                                 m    c l ˙                       c   ˙
                                                            j=1 dd uj ∧T i ∧ Φ.
                      l→∞     U                            U




                                                  21
    When T is the current of integration along X, a related statement in the compact
setting was given in [8, Theorem 2.3].

Proof. Let Φ be a smooth weakly positive form with compact support in U. Assume (i)
holds. Let uljk := max{ulj , −k} which converges to ujk := max{uj , −k} in L1loc as l → ∞
and uljk ≥ ujk . Put

                        Rl := h∧m     c l ˙
                                j=1 dd uj ∧Tl i,              Rkl := ∧m     c l
                                                                      j=1 dd ujk ∧ T.


Similarly, we define R, Rk by using the formula of Rl , Rkl respectively with ulj , uljk replaced
by uj , ujk . Since ulj ≥ uj , we get
                         Z                           Z
                                             l
                            1∩m      l
                               j=1 {uj >−k}
                                            Rk ∧ Φ ≥   1∩m
                                                         j=1 {uj >−k}
                                                                      Rkl ∧ Φ.              (4.1)
                         U                                     U

By Theorem 2.6, we get Rkl → Rk as l → ∞. Using this together with the fact that when
k is fixed, uljk is uniformly bounded in l, we see that the strong uniform quasi-continuity
for ujk with respect to (Tl )l (see Theorem 2.4) implies
              Z                                    Z
                                   l
      lim inf     1∩mj=1 {uj >−k}
                                  Rk ∧ Φ = lim inf     1∩m j=1 {ujk >−k}
                                                                         Rkl ∧ Φ
        l→∞     U                            l→∞     U
                                           Z                                 Z
                                         ≥     1∩m
                                                 j=1 {ujk >−k}
                                                                Rk ∧ Φ =        1∩m
                                                                                  j=1 {uj >−k}
                                                                                               Rk ∧ Φ
                                           Z U                                U

                                         =     1∩m
                                                 j=1 {uj >−k}
                                                               R ∧ Φ.
                                                 U

This combined with (4.1) yields
        Z                                 Z
           1∩m
             j=1 {uj >−k}
                          R ∧ Φ ≤ lim inf    1∩m     l
                                               j=1 {uj >−k}
                                                            Rkl ∧ Φ
         U                          l→∞    U
                                          Z                                 Z
                                                              l
                                ≤ lim inf    1∩m     l
                                               j=1 {uj >−k}
                                                            R ∧ Φ ≤ lim inf   Rl ∧ Φ
                                           l→∞       U                             l→∞   U

for every k. Letting k → ∞ in the last inequality and noticing that R has no mass on
∪mj=1 {uj = −∞} give the desired assertion.
    Now assume (ii). Note that
                                     ulj ≤ ul+1
                                            j   ≤ uj
for every l, j. Thus, {ulj > −k} ⊂ {ul+1 j   > −k} ⊂ {uj > −k} and ũj := liml→∞ ulj ≤ uj .
Using this and arguments similar to those in the previous paragraph, we have
                           Z                         Z
                                             l
                   lim inf   1∩m     l
                               j=1 {uj >−k}
                                            Rk ∧ Φ ≥   1∩m
                                                         j=1 {ũj >−k}
                                                                       R ∧ Φ.
                     l→∞       U                                   U

Letting k → ∞ gives
                                       Z                 Z
                                           l
                             lim inf       R ∧Φ≥              1∩m
                                                                j=1 {ũj >−∞}
                                                                              R ∧ Φ.
                              l→∞      U                 U




                                                         22
Recall that {uj > ũj } is pluripolar. This coupled with the fact that T has no mass on
pluripolar sets and Property (iii) of Proposition 3.5 yields
                          Z            Z                        Z
                              l
                  lim inf    R ∧Φ≥       1∩j=1 {uj >−∞} R ∧ Φ =
                                            m                     R ∧ Φ.
                     l→∞     U                U                                 U

This finishes the proof.

    Recall that for closed positive (1, 1)-currents R1 , R2 on X, we say that R1 is less sin-
gular than R2 if for every local chart U and psh function wj on U such that Rj = ddc wj
on U for j = 1, 2, then w2 ≤ w1 + O(1) on compact subsets of U; and R1 , R2 are of the
same singularity type if w1 ≤ w2 + O(1) and w2 ≤ w1 + O(1) on compact subsets of U. The
following generalizes [8, Proposition 2.1], see also [21, 18].
Proposition 4.2. Let X be a compact complex manifold of dimension n. Let m be an integer
such that 1 ≤ m ≤ n. Let T be a closed positive current of bi-degree (p, p) on X. Let Tj , Tj′
be closed positive (1, 1)-currents on X for 1 ≤ j ≤ m such that Tj , Tj′ are of the same
singularity type and Tj = ddc uj + θj , Tj′ := ddc u′j + θj , where θj is a smooth form and
u′j , uj are θj -psh functions, for every 1 ≤ j ≤ m. Assume that for every J, J ′ ⊂ {1, . . . , m}
                                                             ˙ i is well-defined. Then, for every
such that J ∩ J ′ = ∅, the product h∧j∈J Tj ∧ ∧j ′ ∈J ′ Tj′′ ∧T
    c
dd -closed smooth form Φ, we have
                      Z                              Z
                            ′           ′ ˙                             ˙ i ∧ Φ.
                         hT1 ∧ · · · ∧ Tm ∧T i ∧ Φ =   hT1 ∧ · · · ∧ Tm ∧T                  (4.2)
                     X                                     X

Proof. By compactness of X, we can assume uj , u′j ≤ 0. By the hypothesis, {uj = −∞} =
{u′j = −∞} and wj := uj − u′j is bounded outside {uj = −∞}. Without loss of generality,
we can assume that

                                                  |wj | ≤ 1                                  (4.3)

outside {uj = −∞}. Let A := ∪m  j=1 {uj = −∞} which is a complete pluripolar set. Put
ujk := max{uj , −k}, ujk := max{u′j , −k} and
                      ′


                                                   n
                                                   X
                              ψk := k −1 max{            (uj + u′j ), −k} + 1                (4.4)
                                                   j=1


which is quasi-psh and 0 ≤ ψk ≤ 1, ψk (x) increases to 1 for x 6∈ A. We have ψk (x) = 0 if
uj (x) ≤ −k or u′j (x) ≤ −k for some j. Put wjk := ujk − u′jk . By (4.3), we have

                                                  |wjk | ≤ 1                                 (4.5)

on X. Let J, J ′ ⊂ {1, . . . , n} with J ∩ J ′ = ∅ and

                    RJJ ′ k := ∧j∈J (ddc ujk + θj ) ∧ ∧j ′ ∈J ′ (ddc u′j ′ k + θj ′ ) ∧ T.

The last current is the difference of two closed positive (|J| + |J ′ | + p, |J| + |J ′ | + p)-
currents. Hence, RJJ ′ k might not be positive in general and it is not clear how to control



                                                     23
its mass as k → ∞. This is a subtle point which we need to pay attention to. The relative
non-pluripolar product

                           RJJ ′ := ∧j∈J (ddc uj + θj ) ∧ ∧j ′ ∈J ′ (ddc u′j ′ + θj ′ )∧T
                                                                                       ˙

exists by our assumption. Let

                                  Bk := ∩j∈J {uj > −k} ∩ ∩j ′ ∈J ′ {u′j ′ > −k}.

By Lemma 3.2, we get
                                            0 ≤ 1Bk RJJ ′ = 1Bk RJJ ′ k
for every J, J ′ , k. Put R̃JJ ′ := 1X\A RJJ ′ . The last current is closed (for example see [4,
Remark 1.10]) and positive because RJJ ′ ≥ 0. Using the fact that {ψk 6= 0} ⊂ Bk \A, we
get

                                         ψk R̃JJ ′ = ψk RJJ ′ = ψk RJJ ′ k .                                        (4.6)

Claim. Let j ′′ ∈ {1, . . . , m}\(J ∪J ′ ). Let Φ be ddc -closed smooth form of bi-degree (p′ , p′ )
on X, where p′ := n − |J| − |J ′ | − p − 1. Then
                                    Z
                                lim     ψk ddc wj ′′k ∧ RJJ ′ k ∧ Φ = 0.                   (4.7)
                                     k→∞       X
                                                                              Pm
We prove Claim. Let ω be a Hermitian metric on X. Let η :=                       j=1 2 θj . We have
  c       −1
dd ψk + k η ≥ 0 for every k. By integration by parts and (4.6),
  Z                                Z                              Z
          c                                   c
     ψk dd wj ′′ k ∧ RJJ ′ k ∧ Φ =   wj ′′k dd (ψk RJJ ′ k ∧ Φ) =   wj ′′k ddc (ψk R̃JJ ′ ∧ Φ). (4.8)
     X                                     X                                        X

Observe that

                      ddc (ψk R̃JJ ′ ∧ Φ) = ddc ψk ∧ Φ ∧ R̃JJ ′ + 2dψk ∧ dc Φ ∧ R̃JJ ′

because ddc Φ = 0 and Φ is of bi-degree (p′ , p′ ). Write dc Φ locally as a complex linear
combination of forms like τj ∧ Φj , where τj is a (0, 1)-form or a (1, 0)-form and Φj is a
positive form. Hence, we can use the Cauchy-Schwarz inequality to obtain
 Z                                       Z                                                  21  Z                      21
                       c
      wj ′′ k dψk ∧ d Φ ∧ R̃JJ ′ ≤                 |wj2′′k |dψk ∧ dc ψk ∧ R̃JJ ′ ∧ Φ0                  R̃JJ ′ ∧ Φ0 ∧ ω          ,
  X                                            X                                                   X

                              ′
where Φ0 := ω n−|J|−|J |−1 . We deduce that
             Z                                                       Z                                     21
                                                                 1
                                     c                                                  c
                     wj ′′k dψk ∧ d Φ ∧ R̃JJ ′ . kR̃JJ ′ k       2            dψk ∧ d ψk ∧ R̃JJ ′ ∧ Φ0
                 X                                                        X

by (4.5). Recall that {limk→∞ ψk < 1} is equal to the complete pluripolar set A. Using
this, Remark 2.7 and the fact that R̃JJ ′ has no mass on A, we get

                      lim dψk ∧ dc ψk ∧ R̃JJ ′ = lim (ddc ψk2 − ψk ddc ψk ) ∧ R̃JJ ′ = 0
                     k→∞                                 k→∞




                                                            24
(we recall that to get Remark 2.7 for R̃JJ ′ and ψk , we need to use the strong quasi-
continuity of ψk with respect to the capacity associated to R̃JJ ′ ). Thus we obtain
                                 Z
                            lim     wj ′′ k dψk ∧ dc Φ ∧ R̃JJ ′ = 0.                 (4.9)
                                k→∞   X

On the other hand, since
 Z                                  Z                               Z
               c                                 c
     wj ′′ k dd ψk ∧ Φ ∧ R̃JJ ′ = −   dwj ′′k ∧ d ψk ∧ Φ ∧ R̃JJ ′ +   wj ′′k dc ψk ∧ dΦ ∧ R̃JJ ′ ,
    X                                 X                                        X

using similar arguments, we get
                                      Z
                                lim           wj ′′k ddc ψk ∧ Φ ∧ R̃JJ ′ = 0
                              k →∞
                                ′
                                          X

Combining this with (4.9) and (4.8) yields (4.7). Claim follows.
                               ˙ i − hT1′ ∧ · · · Tn′ ∧T
   Now let S := hT1 ∧ · · · Tn ∧T                     ˙ i. Using Tjk = Tjk
                                                                         ′
                                                                           + ddc wjk , one can
check that
            Z               Z                             Z
                                    m
               ψk S ∧ Φ =       ψk ∧j=1 Tjk ∧ T ∧ Φ −        ψk ∧m    ′
                                                                 j=1 Tjk ∧ T ∧ Φ
                X                X                                 X
                                m Z
                                X
                                              s−1 ′
                            =             ψk ∧j=1 Tjk ∧ ddc wsk ∧ ∧m
                                                                   j=s+1 Tjk ∧ T ∧ Φ.
                                s=1   X


This together with Claim yields hS, Φi = limk→∞ hψk S, Φi = 0 for every ddc -closed smooth
Φ. This finishes the proof.
Remark 4.3. Our proof of Proposition 4.2 still works if Tj′ , Tj are not in the same cohomol-
ogy class. In this case, one just needs to modify (4.2) accordingly.
  The following result is the monotonicity property of relative non-pluripolar products
mentioned in Introduction.
Theorem 4.4. Let X be a compact Kähler manifold of dimension n. Let Tj , Tj′ be closed
positive (1, 1)-currents on X for 1 ≤ j ≤ m such that Tj , Tj′ are in the same cohomology
class for every j and Tj′ is less singular than Tj for 1 ≤ j ≤ m. Let T be a closed positive
current on X. Then, we have
                                           ˙ i ≤ hT1′ ∧ · · · ∧ Tm′ ∧T
                                                                    ˙ i .
                                                
                          hT1 ∧ · · · ∧ Tm ∧T                                        (4.10)

Proof. Write Tj = ddc uj + θj , Tj′ = ddc u′j + θj . Without loss of generality, we can assume
that u′j ≥ uj . For l ∈ N, put ulj := max{uj , u′j − l} which is of the same singularity type as
u′j . Notice that ddc ulj + θj ≥ 0. Since X is Kähler, the current h∧m        c l       ˙
                                                                        j=1 (dd uj + θj )∧T i is of
                                                                  m      c l       ˙ i as l → ∞.
mass uniformly bounded in l. Let S be a limit current of h∧j=1 (dd uj + θj )∧T
         l
Since uj decreases to uj as l → ∞, we can apply Lemma 4.1 to get

                                              S ≥ h∧m      ˙
                                                    j=1 Tj ∧T i.

Consequently, {S} ≥ {h∧m          ˙
                           j=1 Tj ∧T i}. Using Proposition 4.2, we see that {S} is equal to
   m    ′˙
{h∧j=1 Tj ∧T i}. The desired assertion, hence, follows. This finishes the proof.



                                                      25
```

## Source unit 12: Full integration-by-parts section, admissibility, gradient construction and proofs

Vu-2005.13241v3-20261004.txt, LF121--655. Independent range SHA256 `ac897767ca0a5f2aaccf93220b4393ba919af1d21d12d7f2a378207e1955b157`. Supplied literal body is unchanged; boundary LF framing is separately recorded. Printed defects remain source data.

```text
fined in a way similar to that of the usual non-pluripolar product. The
product h m        ˙
          V
            j=1 Tj ∧T i is a well-defined closed positive current of bi-degree
(m + p, m + p); and h m           ˙
                         V
                           j=1 Tj ∧T i is symmetric with respect to T1 , . . . , Tm
and is homogeneous.
    For every closed positive (1, 1)-current P , we denote by IP the set of
x ∈ X so that local potentials of P are equal to −∞ at x. Note that IP
is a locally complete pluripolar set. The following is deduced from [14,
Proposition 3.5].

Proposition 2.1. (i) Given a locally complete pluripolar set A such that T
has no mass on A, then h m         ˙
                          V
                            j=1 Tj ∧T i also has no mass on A.
   (ii) Let T1′ be a closed positive (1, 1)-current on X and Tj , T as above.
Assume that T has no mass on IT1 ∪ IT1′ . Then we have
                            m
                            ^                     m
                                                  ^                       m
                                                                          ^
(2.1)       (T1 + T1′ ) ∧            ˙
                                  Tj ∧T = hT1 ∧            ˙ i + hT1′ ∧
                                                        Tj ∧T                      ˙ i.
                                                                                Tj ∧T
                            j=2                   j=2                     j=2
4                                                                    Duc- Viet Vu

                                                             Vm
   (iii) Let 1 ≤ l ≤ m be an integer. Then for R := h                   ˙
                                                               j=l+1 Tj ∧T i, there
holds h m
                         Vl
                 ˙               ˙
       V
          j=1 Tj ∧T i = h j=1 Tj ∧Ri.
   (iv) The equality
                             m
                             ^            m
                                          ^
                            h Tj ∧T           ˙ ′i
                                   ˙ i = h Tj ∧T
                             j=1           j=1
               ′
holds, where T := 1X\   Sm          T.
                          j=1 ITj


    We also need the following result.
Theorem 2.2. ([14, Theorem 2.6, Remark 2.7]) Let uj be a locally bounded
plurisubharmonic (psh) function on an open subset U of Cn for 1 ≤ j ≤ m.
Let (ujk )k∈N be a sequence of locally bounded psh functions increasing to uj
almost everywhere as k → ∞. Let T be a closed positive current on U. Then,
the convergence

(2.2)      u1k ddc u2k ∧ · · · ∧ ddc umk ∧ T → u1 ddc u2 ∧ · · · ∧ ddc um ∧ T

as k → ∞ holds provided that T has no mass on Aj := {x ∈ U : uj (x) 6=
limk→∞ ujk (x)} for every 1 ≤ j ≤ m and the set Aj is locally complete
pluripolar for every j.
    Recall that a dsh function on X is the difference of two quasiplurisub-
harmonic (quasi-psh for short) functions on X (see [9]). These functions
are well-defined outside pluripolar sets. Let v be a dsh function on X.
Write v = ϕ1 − ϕ2 , where ϕ1 , ϕ2 are quasi-psh function. Hence v(x) is
well-defined for x ∈ X\A, where A := {ϕ1 = −∞} ∪ {ϕ2 = −∞}. The
function v is said to be bounded in X if there exists a constant C such that
|v(x)| ≤ C for every x ∈ X\A.
    We say that v is T -admissible (or admissible with respect to T ) if there
exist quasi-psh functions ϕ1 , ϕ2 on X such that v = ϕ1 − ϕ2 and T has
no mass on {ϕj = −∞} for j = 1, 2. In particular, if T has no mass on
pluripolar sets, then every dsh function is T -admissible. Assume now that
v is T -admissible. The following is a direct consequence of Proposition 2.1
(i).
Lemma 2.3. If v is T -admissible, then v is also admissible with respect to
h m       ˙
 V
   j=1 Tj ∧T i.

   Recall that if v = ϕ1 − ϕ2 for some bounded quasi-psh functions ϕ1 , ϕ2
on X (note X is compact), the current dv ∧ dc v ∧ T is, by definition, equal
to
             1 c
(2.3)          dd (ϕ1 − ϕ2 )2 ∧ T − (ϕ1 − ϕ2 )ddc (ϕ1 − ϕ2 ) ∧ T.
             2
Convexity of the class of currents with finite energy                      5

We notice that in the above formula the function (ϕ1 − ϕ2 )2 is locally the
difference of two bounded psh functions. More precisely, we can assume
ϕj is ω-psh function for j = 1, 2, where ω is a Kähler form on X, and
consider an open local chart U such that ω = ddc φ for some smooth psh
function φ on U. By adding to φ a big constant, we can even assume that
ϕj + φ ≥ 0 on U for j = 1, 2. Thus (ϕj + φ)2 and (ϕ1 + ϕ2 + 2φ)2 are psh
on U for j = 1, 2, and

(2.4)      (ϕ1 − ϕ2 )2 = (2(ϕ1 + φ)2 + 2(ϕ2 + φ)2 ) − (ϕ1 + ϕ2 + 2φ)2

which is the difference of two bounded psh functions on U.
   Consider another dsh function w which is equal to the difference of
two locally bounded psh functions and T is of bi-degree (n − 1, n − 1), we
have
(2.5)
2dv ∧ dc w ∧ T = d(v + w) ∧ dc (v + w) ∧ T − dv ∧ dc v ∧ T − dw ∧ dc w ∧ T.

However, in general, even when v is bounded, v might not be the differ-
ence of two bounded quasi-psh functions. Hence, the current “dv∧dc v∧T ”
is not well-defined in the above sense. We will introduce below the cur-
                ˙ i in the spirit of non-pluripolar products. Before going
rent hdv ∧ dc v ∧T
into details, we need the following auxiliary estimate.

Lemma 2.4. Let ω be a Kähler form on X. Let ϕ1 , ϕ2 be bounded ω-psh
functions on X and v := ϕ1 − ϕ2 . Let T be a closed positive current of bi-
dimension (1, 1) on X. Then, there exists a constant C independent of ϕ1 , ϕ2
such that
                        Z
(2.6)                     dv ∧ dc v ∧ T ≤ CkvkL∞ .
                            X

Proof. We have
                   Z                             Z
                                 c
            I :=       dv ∧ d v ∧ T = −                  vddc v ∧ T
                   X
                   Z                                 X

              =−    v(ddc ϕ1 − ddc ϕ2 ) ∧ T
                 ZX                       Z
                        c
              =−    v(dd ϕ1 + ω) ∧ T +      v(ddc ϕ2 + ω) ∧ T
                       X                                  X
                           2 Z
                           X
              ≤ kvkL∞                    (ddc ϕj + ω) ∧ T
                           j=1       X
                           Z
              = 2kvkL∞               T ∧ω
                             X
6                                                                      Duc- Viet Vu

by Stokes’ theorem. The desired estimate follows. The proof is finished.


    Assume now that v is T -admissible. Let ϕ1 , ϕ2 be quasi-psh functions
such that v = ϕ1 − ϕ2 and T has no mass on {ϕj = −∞} for j = 1, 2. Let
ϕj,k := max{ϕj , −k} for every j = 1, 2 and k ∈ N. Put vk := ϕ1,k − ϕ2,k .
Since vk is the difference of two bounded quasi-psh functions, using (2.3),
we obtain

                Qk := dvk ∧ dc vk ∧ T = ddc vk2 ∧ T − vk ddc vk ∧ T.

Let ω be a Kähler form so that ϕj is ω-psh for j = 1, 2. Let U be a local
chart on X such that ω = ddc φ on U for some psh function φ such that
ϕj,k + φ ≥ 0 on U for j = 1, 2 (we fix k). By (2.4) applied to ϕj,k + φ, we
have

Qk = 2ddc (ϕ1,k + φ)2 ∧ T + 2ddc (ϕ2,k + φ)2 ∧ T − ddc (ϕ1,k + ϕ2,k + 2φ)2 ∧ T
        − (vk ddc ϕ1,k ∧ T − vk ddc ϕ2,k ∧ T )

on U. By the plurifine locality with respect to T ([14, Theorem 2.9]) ap-
plied to each term in the right-hand side of the last equality, we have

(2.7)                   1T2j=1 {ϕj >−k} Qk = 1T2j=1 {ϕj >−k} Qk′

for every k ′ ≥ k.
                          ˙ i is well-defined if the mass of 1T2 {ϕ >−k} Qk
   We say that hdv ∧ dc v ∧T                                   j=1  j

on X is bounded uniformly in k. In this case, using (2.7) implies that there
exists a positive current Q on X such that for every bounded Borel form
Φ on X, we have

                        hQ, Φi = lim h1T2j=1 {ϕj >−k} Qk , Φi.
                                   k→∞

                      ˙ i to be the current Q. This agrees with the classical
We define hdv ∧ dc v ∧T
definition if v is the difference of two bounded quasi-psh functions. This
definition is independent of the choice of ϕ1 , ϕ2 by Lemma 2.5 below. If w
is another T -admissible dsh function and T is of bi-dimension (1, 1) such
                             ˙ i, hdw ∧ dcw ∧T
that the currents hdv ∧ dc v ∧T             ˙ i, and hd(v + w) ∧ dc(v + w)∧T
                                                                          ˙ i
                                         c ˙
are all well-defined, we define hdv ∧ d w ∧T i using (2.5) formally.
Lemma 2.5. Let ϕ′1 , ϕ′2 be quasi-psh functions on X such that v = ϕ′1 − ϕ′2
and T has no mass on {ϕ′j = −∞} for j = 1, 2. Let ϕ′j,k , Q′k be the func-
tion and current associated to ϕ′j defined similarly as ϕj,k and Qk respec-
tively. Then if 1T2j=1 {ϕj >−k} Qk is of mass bounded uniformly on k then so is
Convexity of the class of currents with finite energy                                    7

1T2j=1 {ϕ′j >−k} Q′k , and

(2.8)                        Q = lim h1T2j=1 {ϕ′j >−k}Q′k , Φi
                                  k→∞

for every bounded Borel form Φ on X.

Proof. Since v = ϕ′1 − ϕ′2 , we get

                                  ϕ1 + ϕ′2 = ϕ′1 + ϕ2 .

Put vk′ := ϕ′1,k − ϕ′2,k , A′k := 2j=1 {ϕ′j > −k}, and Ak := 2j=1 {ϕj > −k}.
                                 T                            T

We have Q′k = dvk′ ∧ dc vk′ ∧ T , and vk = vk′ on Ak ∩ A′k which is open in the
plurifine topology. We claim that

(2.9)                           1Ak ∩A′k Q′k = 1Ak ∩A′k Qk .

This is a sort of plurifine locality statement and can be essentially de-
duced from the plurifine locality for bounded psh functions (here we have
vk = vk′ on Ak ∩ A′k but vk , vk′ are only dsh). We give details for readers’
convenience. Before doing so, we will show that the desired assertion is a
direct consequence of (2.9). First observe that 1A′k Q′k has no mass on the
pluripolar set {ϕj = −∞} for j = 1, 2 by Proposition 2.1 (i) and the fact
that T has no mass on {ϕj = −∞}. It follows that

                    1A′k Q′k = lim 1A′k ∩As Q′k
                                s→∞
                             = lim 1A′k ∩As Q′s
                                s→∞
                             ≤ lim 1A′s ∩As Q′s
                                s→∞
                             = lim 1A′s ∩As Qs ≤ lim 1As Qs = Q,
                                s→∞                 s→∞

where we used (2.7) applied to Q′k in the second equality and (2.9) in the
third equality. By exchanging the role of Q′k and Qk , we also obtain that

                                      1Ak Qk ≤ R,

for every limit current R of (1A′k Q′k )k as k → ∞. Hence (2.8) follows.
   We go back to the proof of (2.9). Write

dvk ∧ dc vk ∧ T = dvk ∧ dc (vk − vk′ ) ∧ T + d(vk − vk′ ) ∧ dc vk′ ∧ T + dvk′ ∧ dc vk′ ∧ T.

Denote by R1 , R2 the first and second currents in the right-hand side of
the last equality. In order to obtain (2.9), it suffices to check that Rj = 0
8                                                                    Duc- Viet Vu

on Ak ∩ A′k for j = 1, 2. Observe

     R1 = dvk ∧ dc (ϕ1,k + ϕ′2,k − ϕ′1,k − ϕ2,k ) ∧ T
        = dϕ1,k ∧ dc (ϕ1,k + ϕ′2,k ) ∧ T − dϕ1,k ∧ dc (ϕ′1,k + ϕ2,k ) ∧ T −
                                                                         

          dϕ2,k ∧ dc (ϕ1,k + ϕ′2,k ) ∧ T − dϕ2,k ∧ dc (ϕ′1,k + ϕ2,k ) ∧ T .
                                                                        


Each term in the right-hand side of the above equality is equal to 0 on
Ak ∩ A′k thanks to the plurifine locality and the fact that

               ϕ1,k + ϕ′2,k = ϕ1 + ϕ′2 = ϕ′1 + ϕ2 = ϕ′1,k + ϕ2,k

on Ak ∩ A′k . Hence R1 = 0 on Ak ∩ A′k . Similarly we get R2 = 0 on Ak ∩ A′k .
This finishes the proof.
                                                                  ˙ i is
Lemma 2.6. Assume that v is bounded. Then, the current hdv ∧ dc v ∧T
well-defined.

Proof. Let the notation be as in the proof of Lemma 2.4. Let ω be a Kähler
form on X such that ϕ1 , ϕ2 are ω-psh. Note that ϕjk is also ω-psh for every
j, k. Observe that since v is bounded, there exists a constant C such that
ϕ2 − C ≤ ϕ1 ≤ ϕ2 + C. Thus, there exists a constant C so that

                                 kvk kL∞ ≤ C

for every k. Using this and Lemma 2.4, one gets

                             kQk k . kvk kL∞ ≤ C

for some constant C independent of k. Hence, the desired assertion fol-
lows. This finishes the proof.

      Let T1 , . . . , Tm be closed positive (1, 1)-currents on X and R := hT1 ∧
           ˙ i. We define
· · · ∧ Tm ∧T

               hdv ∧ dc v ∧ T1 ∧ · · · ∧ Tm ∧T
                                            ˙ i := hdv ∧ dc v ∧Ri.
                                                              ˙

When T ≡ 1, we write the left-hand side of the last equality simply as
hdv ∧ dc v ∧ T1 ∧ · · · ∧ Tm i.
                                            ˙ i is defined similarly if p + m =
   The current hdv ∧ dc w ∧ T1 ∧ · · · ∧ Tm ∧T
n − 1, where T is of bi-degree (p, p). We put

                   hddc v ∧T
                          ˙ i := hddc ϕ1 ∧T
                                         ˙ i − hddcϕ2 ∧T
                                                      ˙ i.

Define
                   hddc v ∧ T1 ∧ · · · ∧ Tm ∧T
                                            ˙ i := hddc v ∧Ri.
                                                          ˙
Convexity of the class of currents with finite energy                            9

   By Proposition 2.1 (iii), this definition agrees with the T -relative non-
pluripolar product of ddc v, T1 , . . . , Tm if v is quasi-psh. When T ≡ 1, we
                                                              ˙ i. In this case the
write hddc v ∧ T1 ∧ · · · ∧ Tm i for hddc v ∧ T1 ∧ · · · ∧ Tm ∧T
product hddc v ∧ T1 ∧ · · · ∧ Tm i is the one defined in the paragraph right
after Theorem 1.2 in [12].
   By admissibility and Proposition 2.1 (ii), we can check that if v, w are
dsh functions which are admissible with respect to T , then

                    hddc (v + w)∧T
                                ˙ i = hddc v ∧T
                                             ˙ i + hddcw ∧T
                                                         ˙ i.

   Here is an integration by parts formula for relative non-pluripolar prod-
ucts.
Theorem 2.7. Let T be a closed positive current of bi-degree (n − 1, n − 1)
on X. Let v, w be bounded T -admissible dsh functions on X. Then, we have
              Z                Z                   Z
                     c ˙
(2.10)           whdd v ∧T i =   vhdd w ∧T i = − hdw ∧ dc v ∧T
                                       c ˙                     ˙ i.
                X                  X                      X

   The last result was proved in [4, Theorem 1.14] if v, w can be written
as the differences of psh functions which are locally bounded outside a
closed locally complete pluripolar set; see also [1, 13].

Proof. We use ideas from the proof of [14, Proposition 4.2]. Let ϕ1 , ϕ2 , ϕ3 , ϕ4
be negative quasi-psh functions on X such that v = ϕ1 −ϕ2 and w = ϕ3 −ϕ4
and T has no mass on 4j=1 {ϕj = −∞}. Let ω be a Kähler form on X such
                       S

that ϕj is ω-psh for every 1 ≤ j ≤ 4. Put

           ψ := ϕ1 + ϕ2 + ϕ3 + ϕ4 ,       ψk := k −1 max{ψ, −k} + 1.

and ϕjk := max{ϕj , −k} for 1 ≤ j ≤ 4. Observe that 0 ≤ ψk ≤ 1. Let x ∈ X
such that ψk (x) > 0. We have

                ϕ1 (x) + ϕ2 (x) + ϕ3 (x) + ϕ4 (x) = ψ(x) > −k.

This combined with the property that ϕj ≤ 0 for every 1 ≤ j ≤ 4 yields
that ϕj (x) > −k for every 1 ≤ j ≤ 4. We infer that
                                         4
                                         \
(2.11)                     {ψk 6= 0} ⊂       {ϕj > −k}.
                                         j=1


   Put vk := ϕ1k − ϕ2k and wk := ϕ3k − ϕ4k . Since v and w are bounded,
the functions vk , wk are bounded uniformly in k.
10                                                                      Duc- Viet Vu

              S4
   Let A :=    j=1 {ϕj = −∞}. By admissibility and Proposition 2.1 (i), we
see that

(2.12)                       1A h(ddcϕj + ω)∧T
                                            ˙ i = 0.

Using (2.12), we can consider w as a bounded function with respect to the
                              ˙ i. Using (2.11), we have
trace measure of h(ddc ϕj + ω)∧T

      wψk ddc ϕjk ∧ T = w1{ϕj >−k} ψk hddc ϕj ∧T
                                              ˙ i
                         = whddc ϕj ∧T
                                    ˙ i + w(1{ϕj >−k} ψk − 1)hddcϕj ∧T
                                                                    ˙ i.

The second term in the right-hand side of the last equality converges
weakly to 0 as k → ∞ by the fact that ψk → 1 pointwise outside A as
k → ∞ and Lebesgue’s dominated convergence theorem. Hence

                       whddcϕj ∧T
                               ˙ i = lim wψk ddc ϕjk ∧ T.
                                          k→∞

Applying the last equality to j = 1, 2, and using v = ϕ1 − ϕ2 , we obtain

(2.13)        whddcv ∧T
                     ˙ i = lim wψk ddc vk ∧ T = lim wk ψk ddc vk ∧ T.
                               k→∞                            k→∞

Here in the second equality we used the fact that w = wk on {ϕ3 > −k} ∩
{ϕ4 > −k} which contains {ψk 6= 0}. We also have an analogous formula
by exchanging the roles of v, w. Thus,

(2.14)    whddcv ∧T
                 ˙ i − vhddc w ∧T
                               ˙ i = lim ψk (wk ddc vk − vk ddc wk ) ∧ T.
                                                    k→∞

By integration by parts for bounded psh functions, we have
         Z                                     Z
                      c          c
(2.15)       ψk (wk dd vk − vk dd wk ) ∧ T = −    wk dψk ∧ dc vk ∧ T +
           X                                    X
                                                      Z
                                                         vk dψk ∧ dc wk ∧ T.
                                                                    X

Denote by I1 , I2 the first and second term in the right-hand side of the
last equality. We will check that Ij → 0 as k → ∞ for j = 1, 2. Using the
Cauchy-Schwarz inequality, the boundedness of vk , wk and Lemma 2.4, we
infer
               Z                   21  Z                        21
                            c                     2       c
       |I1 | ≤      dψk ∧ d ψk ∧ T     ×     |wk | dvk ∧ d vk ∧ T
                   X                                      X
               Z                         21
           .           dψk ∧ dc ψk ∧ T          .
                   X
Convexity of the class of currents with finite energy                       11

Recall that {limk→∞ ψk < 1} is equal to the complete pluripolar set {ψ =
−∞}. Using this, Theorem 2.2 and the fact that T has no mass on {ψ =
−∞}, we get

           lim dψk ∧ dc ψk ∧ T = lim (ddc ψk2 − ψk ddc ψk ) ∧ T = 0
           k→∞                     k→∞

Thus we obtain

(2.16)                            lim I1 = 0.
                                 k→∞

By similarity, we also get I2 → 0 as k → ∞. Combining this with (2.15)
and (2.13) gives the first desired equality of (2.10). We prove the second
one similarly as follows. Put u := v + w, and

               uk := max{ϕ1 + ϕ3 , −k} − max{ϕ2 + ϕ4 , −k}.

By (2.11) observe that

             1{ψk >0} max{ϕ1 + ϕ3 , −2k} = 1{ψk >0} (ϕ1k + ϕ3k )

and a similar equality for ϕ2 , ϕ4 also holds. Thus, by plurifine locality, we
get

2hdv ∧ dc w ∧T
            ˙ i = hdu ∧ dc u∧T
                            ˙ i − hdv ∧ dc v ∧T
                                             ˙ i − hdw ∧ dc w ∧T
                                                              ˙ i
                 = lim ψk hdu2k ∧ dc u2k ∧T
                                         ˙ i − hdvk ∧ dc vk ∧T
                                                            ˙ i−
                   k→∞
                  hdwk ∧ dc wk ∧T
                               ˙ i
                                   

                 = lim ψk hd(vk + wk ) ∧ dc (vk + wk )∧T
                                                      ˙ i − hdvk ∧ dc vk ∧T
                                                                         ˙ i−
                   k→∞
                  hdwk ∧ dc wk ∧T
                               ˙ i .
                                  


Consequently

                  hdv ∧ dc w ∧T
                             ˙ i = lim ψk hdvk ∧ dc wk ∧T
                                                       ˙ i.
                                    k→∞

It follows that
  Z                                      Z
          c ˙              c ˙
      vhdd w ∧T i + hdv ∧ d w ∧T i = lim    ψk (vk ddc wk + dvk ∧ dc wk ) ∧ T
    X                                k→∞ X
                                           Z
                                   = − lim    vk dψk ∧ dc wk ∧ T
                                         k→∞    X

which is equal to 0 by analogous arguments as in the proof of (2.16). This
finishes the proof.
12                                                                                          Duc- Viet Vu

Corollary 2.8. Let v, w be bounded dsh functions on X. Then, for every
closed smooth form Φ of right bi-degree, we have
            Z                  m
                               ^                  Z                      m
                                                                         ^
                        c                                    c
(2.17)              whdd v ∧         Tj i ∧ Φ =           vhdd w ∧             Tj i ∧ Φ =
                X              j=1                    X                  j=1
                                                                     Z                      m
                                                                                            ^
                                                                                    c
                                                                 −        hdv ∧ d w ∧             Tj i ∧ Φ.
                                                                     X                      j=1

Proof. By writing Φ as the difference of two closed positive forms, we can
assume that Φ is positive. The desired formula is a direct consequence of
Theorem 2.7 applied to T := hT1 ∧ · · · ∧ Tm i ∧ Φ.

    We recall that the first inequality of (2.17) was proved in [12, Theorem
1.2] and [16] when m = n and the cohomology classes of Tj ’s are big.
One should notice a crucial point that the integration by parts formulae
obtained in [12, 16] contain no term involving dv ∧ dc w. Such a term is
essential in applications, especially, in the pluricomplex energy theory. The
following result is more general than Theorem 2.7. We will need it later.
Theorem 2.9. Let T a closed positive current of bi-degree (n − 1, n − 1) on
X. Let v, w be bounded T -admissible dsh functions on X. Let χ : R → R be
a C 3 function. Then we have
(2.18)
   Z                   Z                        Z
                           ′′
             c ˙
      χ(w)hdd v ∧T i =                c ˙
                         vχ (w)hdw ∧ d w ∧T i +   vχ′ (w)hddcw ∧T
                                                               ˙ i.
        X                            X                                          X

   A quick heuristic reason explaining why (2.18) should hold is because
dd χ(w) = χ′′ (w)dw∧dc w+χ′ (w)ddcw if w is a bounded quasi-psh function.
    c


Proof. We first note that [14, Lemma 5.7] still holds for dsh functions
which are the differences of two bounded quasi-psh functions. Now, to
obtain the desired equality, we just follow the proof of Theorem 2.7 ver-
batim with χ(w) in place of w. The only thing we need to clarify is the
computation concerning ddc χ(wk ) ∧ T . To this end, it suffices to use [14,
Lemma 5.7] because wk is the difference of two bounded quasi-psh func-
tions. This finishes the proof.


```

## Source unit 13: Full relative finite-energy section with definitions and printed proofs

Vu-2005.13241v3-20261004.txt, LF656--827. Independent range SHA256 `7c4a6f848d72b6bc891d56b0cdf8b543bf9c1522324504029100073e1d6b9ba9`. Supplied literal body is unchanged; boundary LF framing is separately recorded. Printed defects remain source data.

```text
3       Currents with finite relative energy
Let X be a compact Kähler manifold. Let α1 , . . . , αm be pseudoeffective
(1, 1)-classes of X and T a closed positive current on X. Let Pj be a closed
Convexity of the class of currents with finite energy                                 13

positive (1, 1)-current in the class αj for 1 ≤ j ≤ m. Put P := (P1 , . . . , Pm ).
We define EP (T ) to be the set of m-tuple (T1 , . . . , Tm ) of closed positive
(1, 1)-currents such that Tj ∈ αj and Tj is more singular than Pj and
                                m
                                ^                     m
                                                      ^
                           {h            ˙ i} = {h
                                      Tj ∧T                    ˙ i}.
                                                            Pj ∧T
                                j=1                   j=1

Notice that for every current Pj′ in αj such that Pj′ has the same singular-
ities as Pj for 1 ≤ j ≤ m, by the monotonicity of relative non-pluripolar
products (see (1.1)), we have

                                       EP (T ) = EP′ (T ).

Hence, when Pj has minimal singularities in αj for 1 ≤ j ≤ m, we recover
the class E(α1 , . . . , αm , T ) of currents of full mass intersection introduced
in [14, 4] because we have

                             EP (T ) = E(α1 , . . . , αm , T )

in this case.
    Let χ ∈ W − . Write Pj = ddc ϕj + θj , where θj is a smooth form and ϕj is
a negative θj -psh function. Let (T1 , . . . , Tm ) ∈ EP (T ). Let uj be a negative
θj -psh function so that Tj = ddc uj + θj and uj ≤ ϕj for 1 ≤ j ≤ m. For a
negative Borel function ξ, we put
                                           XZ       ^         ^
(3.1)       Eξ,P (T1 , . . . , Tm ; T ) :=     −ξ      Tj ∧         ˙ ,
                                                                 Pj ∧T
                                             J    X          j∈J       j6∈J

where the sum is taken over every subset J of {1, . . . , m}. The (T, P)-
relative joint χ-energy of T1 , . . . , Tm is, by definition, Eξ,P (T1 , . . . , Tm ; T ),
where
                                                             
                    ξ := χ (u1 − ϕ1 ) + · · · + (um − ϕm ) .
The last energy depends on the choice of uj , ϕj but its finiteness does not.
That notion generalizes those in [4, 11, 14], see also [5] for the local
setting.
    For every closed positive (1, 1)-current P , let IP be the set of x ∈ X so
that the potentials of P are equal to −∞ at x. Note that IP is a complete
pluripolar set. By Proposition 2.1 (iv), the right-hand side of (3.1) remains
unchanged if we replace T by 1X\ Sm         j=1 IPj
                                                    T . Hence, in practice, we can
                             Sm
assume T has no mass on j=1 IPj . We denote by Eχ,P (T ) the subset of
EP (T ) containing every (T1 , . . . , Tm ) such that their (T, P)-relative joint
χ-energy is finite.
14                                                                                   Duc- Viet Vu

   Here is a monotonicity for the class Eχ,P (T ) when Pj = P for every
1 ≤ j ≤ m. This generalizes [14, Theorem 5.8].
Theorem 3.1. Let P = ddc ϕ + θ be a closed positive (1, 1)-current and P :=
(P, . . . , P ) (m times P ). Let χ ∈ W − with |χ(0)| ≤ 1. Let (T1 , . . . , Tm ) ∈
Eχ,P (T ) and (T1′ , . . . , Tm′ ) ∈ EP (T ) such that Tj = ddc uj + θ, Tj′ = ddc u′j + θ
such that uj , u′j are θ-psh and uj ≤ u′j ≤ ϕ. Put
                                                                
                           ξ := χ (u1 − ϕ) + · · · + (um − ϕ) .

Then we have

                 Eξ (T1′ , . . . , Tm′ ; T ) ≤ c1 Eξ (T1 , . . . , Tm ; T ) + c2 ,

for some constants c1 , c2 > 0 independent of χ. In particular, (T1′ , . . . , Tm′ ) ∈
Eχ,P (T ).

Proof. As mentioned above, we can assume that T has no mass on IP =
{ϕ = −∞}. Note here that {ϕ = −∞} ⊂ {uj = −∞}. Put

                               ujk := max{uj , ϕ − k} − ϕ

which is a bounded dsh function and

                                    Tjk := ddc ujk + P.

Observe that ujk ’s are admissible with respect to T . Define u′jk , Tjk
                                                                      ′
                                                                         simi-
larly. Put
                    m
                    X
             v :=         (uj − ϕj ),    vk := max{v, −k},             ξk = χ(vk ).
                    j=1

Note that ξ = χ(v). With these notations and a suitable integration by
parts ready in our hands (Theorem 2.9) replacing [14, Lemma 5.7]), the
proof goes exactly as in the proof of [14, Theorem 5.8]. The only minor
modifications are: the Kähler form ω is substituted by P and the wedge
products appearing in the proof of [14, Theorem 5.8] need to be replaced
by T -relative non-pluripolar products. This finishes the proof.

     The following is a direct consequence of Theorem 3.1.
Corollary 3.2. Let P, P be as in Theorem 3.1. Let P ′ be a current in {P }
which is of the same singularity type as P . Then, for P′ = (P ′ , . . . , P ′) (m
times P ′), we have
                            Eχ,P′ (T ) = Eχ,P(T ).
Convexity of the class of currents with finite energy                            15

   For every closed positive (1, 1)-current P , we define the class Em,P (T )
(resp. Eχ,m,P (T )) to be the set of currents T1 ∈ {P } such that (T1 , . . . , T1 )
belongs to EP (T ) (resp. Eχ,P (T )), where P = (P, . . . , P ) (m times P ). The
last space was introduced in [6] when T is the constant function equal
to 1. As in the case of the usual class of currents of full mass intersection
([11, Proposition 2.2]), notice that
                                          [
                           Em,P (T ) =           Eχ,m,P (T ).
                                         χ∈W −


Let α be a pseudoeffective (1, 1)-class. By Corollary 3.2, we see that the
notion of the weighted class Eχ,m,P (T ) makes sense if we replace P by its
equivalent class (in terms of singularity type) of (1, 1)-currents. Hence,
we can define Em (α, T ) (resp. Eχ,m(α, T )) to be the set Em,P (T ) (resp.
Eχ,m,P (T )), where P is a current with minimal singularities in α.
Theorem 3.3. Let U be an open subset in Cn . Let T be a closed positive
current on U and uj , u′j bounded psh functions on U for 1 ≤ j ≤ m, where
m ∈ N. Let vj , vj′ be psh functions on U for 1 ≤ j ≤ q. Assume that uj = u′j
on W := qj=1 {vj > vj′ } for 1 ≤ j ≤ m. Then we have
         T


(3.2)       1W ddc u1 ∧ · · · ∧ ddc um ∧ T = 1W ddc u′1 ∧ · · · ∧ ddc u′m ∧ T.

Proof. If vj , vj′ are all bounded, then the desired assertion is Theorem 2.9
in [14]. In general, observe that
                                          ∞
                                          [
                          {vj > vj′ } =               ′
                                              {vjk > vjk },
                                          k=1

                                             ′
                                                . Let Wk := qj=1 {vjk > vjk
                                                                         ′
                                                           T
where vjk := max{vj , −k} and similarly for vjk                             }.
                    S∞             ′
We have W = k=1 Wk and uj = uj on Wk . Applying [14, Theorem 2.9]
to uj , u′j , Wk gives

         1Wk ddc u1 ∧ · · · ∧ ddc um ∧ T = 1Wk ddc u′1 ∧ · · · ∧ ddc u′m ∧ T

for every k. Hence, the desired assertion follows. This finishes the proof.


   Now, using Theorems 3.1 and 3.3 instead of [14, Theorem 5.8] and
[14, Theorem 2.9] respectively, and following arguments in the proof of
[14, Theorems 5.9 and 5.1], we immediately obtain the following result.

Theorem 3.4. For χ ∈ W − , the sets Eχ,m,P (T ) and Em,P (T ) are convex.
16                                                              Duc- Viet Vu

     Finally, we would like to make the following comment.
                    +
Remark 3.5. Let WM     be the class of weights introduced in [11, Page 462].
Using arguments from the proof of [11, Lemma 3.5] and that of Theorem
                                                        +
3.4, we can prove the convexity of Eχ,m,P (T ) for χ ∈ WM .


Acknowledgements
The author would like to thank referees for their remarks improving the
presentation of the paper.


```

## Source unit 14: Complete bibliography and precise reference bindings

Vu-2005.13241v3-20261004.txt, LF828--884. Independent range SHA256 `d0915796895621146bb871da1cea5244607f9d37b9146f2d202a099a9eb96e7f`. Supplied literal body is unchanged; boundary LF framing is separately recorded. Printed defects remain source data.

```text
References
 [1] E. B EDFORD AND B. A. TAYLOR, A new capacity for plurisubharmonic
     functions, Acta Math., 149 (1982), pp. 1–40.

 [2]       , Fine topology, Šilov boundary, and (ddc )n , J. Funct. Anal., 72
       (1987), pp. 225–251.

 [3] R. J. B ERMAN , S. B OUCKSOM , V. G UEDJ , AND A. Z ERIAHI , A vari-
     ational approach to complex Monge-Ampère equations, Publ. Math.
     Inst. Hautes Études Sci., 117 (2013), pp. 179–245.

 [4] S. B OUCKSOM , P. E YSSIDIEUX , V. G UEDJ , AND A. Z ERIAHI , Monge-
     Ampère equations in big cohomology classes, Acta Math., 205 (2010),
     pp. 199–262.

 [5] U. C EGRELL, Pluricomplex energy, Acta Math., 180 (1998), pp. 187–
     217.

 [6] T. DARVAS , E. D I N EZZA , AND C. H. LU, Monotonicity of nonpluripo-
     lar products and complex Monge-Ampère equations with prescribed sin-
     gularity, Anal. PDE, 11 (2018), pp. 2049–2087.

 [7]        , On the singularity type of full mass currents in big cohomology
       classes, Compos. Math., 154 (2018), pp. 380–409.

 [8] T. DARVAS , E. D I N EZZA , AND C. H. LU, Log-concavity of volume and
     complex Monge-Ampère equations with prescribed singularity, Math.
     Ann., 379 (2021), pp. 95–132.
Convexity of the class of currents with finite energy                 17

 [9] T.-C. D INH AND N. S IBONY, Distribution des valeurs de transforma-
     tions méromorphes et applications, Comment. Math. Helv., 81 (2006),
     pp. 221–258.

[10] D. T. D O AND D.-V. V U, Complex Monge-Ampère equations with solu-
     tions in finite energy classes. arXiv:2010.08619, 2020. to appear in
     Math. Res. Lett.

[11] V. G UEDJ AND A. Z ERIAHI, The weighted Monge-Ampère energy
     of quasiplurisubharmonic functions, J. Funct. Anal., 250 (2007),
     pp. 442–482.

[12] C. H. LU, Comparison of Monge-Ampère capacities, Ann. Polon. Math.,
     126 (2021), pp. 31–53.

[13] N. S IBONY, Quelques problèmes de prolongement de courants en anal-
     yse complexe, Duke Math. J., 52 (1985), pp. 157–197.

[14] D.-V. V U, Relative non-pluripolar product of currents, Ann. Global
     Anal. Geom., 60 (2021), pp. 269–311.

[15] D. W ITT N YSTRÖM, Monotonicity of non-pluripolar Monge-Ampère
     masses, Indiana Univ. Math. J., 68 (2019), pp. 579–591.

[16] M. X IA, Integration by parts formula for non-pluripolar products.
     arXiv:1907.06359, 2019.

```

## Additional source: DGMS-real-homotopy-1975-stonybrook-20261004-LF1-46

DGMS-real-homotopy-1975-stonybrook-20261004.txt, LF1--46, independently checked SHA256 `01d1380988cf77b207bc11b0d87fb390f0a331100cbf538de071a64cacfbe3b8`. Authenticated supplied body reproduced literally, including OCR.

```text
Inventiones math. 29, 2 4 5 - 2 7 4 (1975)
9 by Springer-Verlag 1975




           Real Homotopy Theory of K ihler Manifolds
     Pierre Deligne (Bures-sur-Yvette), Phillip Griffiths* (Cambridge, Mass.),
        John Morgan (NewYork) and Dennis Sullivan (Bures-sur-Yvette)


                                         Table of Contents

                1. Homotopy Theory of Differential Algebras . . . . . . . . . .   248
                2. De Rham Homotopy Theory . . . . . . . . . . . . . . .          254
                3. Relation between De Rham Homotopy Theory and Classical Homo-
                   topy Theory . . . . . . . . . . . . . . . . . . . . . . . .    256
                4. Formality of Differential Algebras . . . . . . . . . . . . . . 260
                5. The De Rham Complex of a Compact K~ihler Manifold . . . . .    262
                6. The Main Theorem and Two Proofs . . . . . . . . . . . . .      270
                7. An Application . . . . . . . . . . . . . . . . . . . . . .     272


    This paper brings together the strengthened de Rham theory of the last author
[12, 13] and [14] concerning the homotopy information of a manifold contained
in the algebra of its differential forms, and the classical results [15] about the
forms on a compact K~ihler manifold to prove statements about the algebraic
topology of compact K~ihler manifolds, and consequently about smooth, complex,
projective algebraic varieties.
    The nature of the results is that the homotopy type of a compact Kiihler manifold,
over the real numbers, is a formal consequence of the real cohomology ring. For any
manifold there is a differential graded algebra with rational structure constants
whose isomorphism type is an invariant of the homotopy type of the space. The
cohomology ring of this differential algebra is the rational cohomology ring of the
space, but the algebra itself contains, for example, the higher order cohomology
products. The isomorphism type of the differential algebra is equivalent to the
"rational form of the nilpotent structure in the space". For a simply connected
manifold this differential algebra is equivalent to the rational Postnikov tower of
manifold. Our results here are that, for a compact K~ihler manifold, from the real
cohomology ring one can produce the real form of this differential algebra. These
 results complement the known structure of the cohomology ring of such a manifold.
 We prove no new results about it.
     The initial motivation for these results was the relation in a K~ihler manifold
 between harmonic forms and holomorphic forms. In particular the (p, 0) harmonic
 forms for any K~ihler metric are exactly the holomorphic forms. Consequently,
 products of (p, 0) and (q, 0) harmonic forms are harmonic l, and thus there are no
```

## Additional source: DGMS-real-homotopy-1975-stonybrook-20261004-LF861-1064

DGMS-real-homotopy-1975-stonybrook-20261004.txt, LF861--1064, independently checked SHA256 `0171c17a073557e342809af894852c1ba92ab5ebda68ee6606ae7371f1f3dc26`. Authenticated supplied body reproduced literally, including OCR.

```text
                                    (02
On any complex manifold there are positive definite Hermitian metrics
         (~,tl)=S(~,q)+]f~A(~,tl)=(J~,J,)                 for ~ , q 6 T ( M ) .
S and A determine one another. Because of the Hermitian symmetry, S is sym-
metric and A is alternating. Thus S is a Riemannian metric and A is a (1, 1) form
on M. The Hermitian metric is defined to be Kiihler if dA =0, and a Kfihler
manifold is a complex manifold admitting a K~ihler metric. The existence of a
Kiihler metric is a statement of close interaction between the complex structure
and potential theory, and it has many deep consequences for the topology of the
manifold [-15].
    There are several equivalent statements to the definition of a K~ihler metric.
The one given above, which is by now the usual one, has the advantage of making
it obvious that a complex submanifold of a K~ihler manifold is again a K~ihler
manifold. Thus, any smooth, complex projective algebraic variety is K~ihler.
The one which we shall use below is the identity
(5.1)                             Ad=2Ao=2A~=Anc
between the Laplacians of the various operators d, O, ~, d c. It is perhaps worthwhile
to give a few alternate forms of the K~ihler condition, and from these explain how
the identity (5.1) may be proved.
    We shall write an Hermitian metric in the two forms
                            ds 2 = ~ hi, j dzi dS j = ~ col ~)i
                                   i,j                i

where (zl, ..., z,) are local holomorphic coordinates, h = (hi. ~)is a positive Hermitian
matrix, and where col, ..., co, are differential forms of type (1, 0) constituting a C ~~
unitary co-frame for the metric. The associated (1, 1) form is

                              A _ t / ~ - I ~hi, jdzi/,,d~j '
                                         2   L" J "
and our basic definition is, as above:
   (i) The metric is Kiihler if dA =0.
   To give the second definition; we recall the basic theorem in local Hermitian
geometry that there exist unique differential forms co~,j, zg satisfying

                                dcoi= ~ coi, j A co j - t - T , i
                                       J
(5.2)                     co~.j+Nj, i=0,     zi has type (2, 0)
264                                                              P. D e l i g n e   et al.



(c.f. Chern [3]). The vector z =(z 1, ..., z,) is the torsion tensor, and m=(mi.j) gives
the connection matrix for the unique connection Vn in the (1,0) tangent bundle
T' (M) satisfying


                                                        v~'~--~
where ~, tl are C ~ sections of T'(M).
    (Explanations. We are viewing connections as differential operators from
sections to sections tensor l-forms; the connection matrix means relative to the
basis of T ' ( M ) dual to ~oI ..... ~ , ; and finally V~' is the CO, I) component of VH.)
    Our second definition is:
    (ii) The metric is KShler if the torsion z = 0 .
    For our third definition, we consider the standard connection VR in the real
tangent bundle T ( M ) associated to the Riemannian metric underlying the given
Hermitian metric.
    (iii) The metric is KShler if VRJ=0; equivalently, parallel translation should
preserve the almost complex structure.
    Finally, we shall say that the metric is K/~hler in case it osculates to 2nd order
to the flat metric on r More precisely,
    (iv) The metric is KShler if, for each point x e M, there is a holomorphic coordinate
system (zl, ..., z,) centered at x and such that

(5.3)                                                    hi, j(z, -i) = 61. j + [2],

where [2] means terms o f order two or more.
   P r o o f of Equivalence of Definitions. ( i ) ~ (ii) Since A is real, dA = 0 ,=, 0A =0.
Let the (0, 1)-component of o;i,j be ai, j. Then by the basic structure equations,
( 5 . 2 ) , fit)i, j = ~i, j - - 0~j, i'




                             _/2-1
                             -         2   Z(~(--~J'iAOOjA~i)+TIA~I--~O'A(~IJA~i))
                                               i    j

                             _i/U-1
                             -        2    Z'~iA~i--Z(~J'IAO)JAO)i+O)iA~i'J/X~-J)
                                           i                     i,j


                             _I//Z- 1 E zi^ ~//
                                  2    i
                             =0r
    (ii) ~ (iii) Write z i = xi + ~ - lx,+ i, a~i = r + VrZ- 1tp,+ 1 where x~, r                  are real
(using the index range 1 __<i, j _<_n and 1 < a, fl__<2 n). Then
                                                   ds 2 = ~ g~, ~ dx~ dxp = ~ q~, q~,
                                                         ol, ~                               Ot
                         Real Homotopy Theory of Ktihler Manifolds                        265

is the underlying Riemann metric, and by the basic theorem in local Riemannian
geometry there exists a unique matrix tp = (r a) of 1-forms satisfying

                                         dtp~ = Z tp~,t~/x (pp
                                                  #
(5.4)

Here (p is the connection matrix for the Riemannian connection VRapplied to the
dual frame to q01..... ~02,. Comparing the structure Eqs. (5.2) and (5.4), we see
that if r = 0, then upon writing co = co' + ~ 1co" we get
                                           (     co' co"~
                                     tp=       -co" co'l"

This says exactly that, on the complexification Tc(M) _~ T' (M) 9 T'(M), VR= Vn 9 fTn,
which implies that VR commutes with J. (This proof may be given verbally by
stating that the Riemannian and Hermitian connections coincide in the K~thler case.)
     (iii) ~ (iv) First, we observe that (iv) is equivalent to saying that, for each
x e M there is a C ~ coordinate system z = ( q , ..., z,) centered at x which is holo-
morphic to 2nd order. This means that z maps a neighborhood U ofx differentially
to ~", dzl(x) ..... dz,(x) span T~(M), and all ~(dzi)(x)=O, such that (5.3) holds.
Assuming (iii), we let (Xl ..... x2,) be geodesic coordinates centered at x. We may
arrange that at x, J(dxi)= dx,+ i, and then set zi = xl + I F - 1 x,+ i. Since (x~ .... , x2,)
are geodesic coordinates, g,,a = 6,. e + [-2]. Thus the connection matrix for VR is
zero at x, and VRJ=O implies (dJ)(x)=O. It follows that ~(dzi)(x)=O, and (iv)
follows immediately.
     (iv) ~ (i) This is the main point. Given an Hermitian metric satisfying (iv),
we see that
(5.5) Any identity involving the metric and only its first derivatives is valid on
M r162it is valid for the fiat metric on C".
Applying this to the identity dA = 0, which is obviously true on C", we conclude
the equivalence of (i)-(iv).
    We shall discuss how the principle (5.5) may be used to prove (5.1), as well as
some other Ktihler identities. We first consider the commutation relations
(5.6)                              [c5, c~*]= 0 = [O, c5"].
On the face of it these involve second derivatives of the metric, but actually only
first derivatives appear for the reason that mixed partials are equal (think of the
Poisson bracket of vector fields). Thus, (5.6) is valid on a Ktihler manifold since
it is obviously true in if;" (the metric has constant coefficients). Expanding out
the definition of A a now gives
                          & = (~ + 0)(~* + 0") + (~* + 0") (~ + ~)
                             = (0 0* + c~*~3)+ (c~* + c5"0)                        (by (5.6));
or

(5.7)                     Aa = Ae+ A~.
266                                               P. Deligne et al.

From (5.7) we see that An preserves (p, q) type, since this is obviously true for A0
and A~. Thus
(5.8)                                       Ad = j - x Ad J = Ado.

Writing O = 8 9        2- ldC), c3"= 89                                      we see that
                         c3~* + c3"(3= 88(dd* + d * d + d C d ~* + d ~* d ~)
                                           =89                                                     (by (5.8))
Combining this with (5.7) gives (5.1).
   In closing, it is worth noting that the most interesting properties of Kihler
metrics, such as the fact that L(~)=A/x ~ takes harmonic forms to harmonic
forms, are generally proved from the identity
(5.9)                                              [A, d] = d~*
or equivalently
(5.10)                                      [A, 4] = - ~ -                   10*
where A = * L* is the adjoint of L. Now (5.10) obviously involves only 1st derivatives
of the metric and so by (5.5) it will suffice to prove it on ~". This is not too hard
since dzl, ..., dz, gives a flat unitary co-frame; one uses the formulae
                                                                 H




                       cS(fdz I ^ d J ) -- ~ ( - 1)p ~                        dz I A dzj A d2 s,
                                                  jCJ

                      A ( f d z I A dr:J) =          ~     +_fdz I - {k}Adz J- {k}
                                                  kelc~J


                     O * ( f d z I A a S, )j=. L +~~ = - a0 zf       .   i
                                                                             - Ill Aa~
                                                                                     9 J

                                                  i~I      OZi

where I =(il , ..., ip), d z 1 = d z i , A ... A dzi~, etc. and just computes. Using (5.10),
                    0c~* + 0* ~ = 1/~- I(0A~? - 0 2 A + A ~ 2 - c~A0)= 0,
which is (5.6). Similarly, d A = O =~ d~A=O and d ~ * = [ A , d ] = 0 since A A is a
constant. Thus A is harmonic for dc, and hence for d. Further discussion of the
basic Kihler identities is given in Weil's book [15], p. 179-194.
   The main fact we shall use about compact Kihler manifolds is the following
lemma:
(5.11) Lemma ( d d ~ Lemma). I f ~ is a differential form such that d~ = 0 and d~ct=0,
and such that ct=dT, then ~=dd~ fl for some ft.
   Proof If D is one of the operators d, c3, ~, d~ with Laplacian AD, the Hodge
decomposition for the Laplacian gives
(5.12)                      0 = ~eo(q,) + Ao ~o(~ )
where o'r     the harmonic part of ~, is the projection of ~ on ~ o = k e r A o ,
and where the Green's operator G o is AB ~ on Jgo• Suppose that c~=dT. Then by
(5.12)
(5.13)                           e = d d * GaOl.
                          Real Homotopy Theory of K/ihler Manifolds                               267

Since d~c~=0, e=Yfdc(e)+dCd~*Gdc~=d~d~*G,~oe                 because ~ o ( e ) = o ~ f d ( e ) = 0 by
(5.1). Plugging this in (5.13) gives
                                     =dd* Ga(d~d~*Gd~ c~)
                                     =dd~(d * Gd d~*Ge~ ~)                            (using (5.6))
                                     =dd~/~
as required.
(5.14) Remark. This l e m m a holds for real as well as complex forms, since the
validity of a linear statement such as

                              Ker(d) c~ Ker(d c) c~ Im(d) = I m ( d d c)

is unchanged by a field extension.
    F o r complex forms, being d and de-closed is the same as being 0 and ~-closed.
Being ddC-exact is the s a m e as being c~-exact, since ddC= 2 i ~ .
```

## Additional source: GZ-intrinsic-capacities-JGA05-20261004-LF1-62

GZ-intrinsic-capacities-JGA05-20261004.txt, LF1--62, independently checked SHA256 `79017a5f9920f81033635b6acb4e07a15c13b88da6c7dcb986963b3bef36265f`. Authenticated supplied body reproduced literally, including OCR.

```text
The Journal of Geometric Analysis
Volume 15, Number 4, 2005




     Intrinsic Capacities on Compact K ihler
                   Manifolds
                                       B y Vincent G u e d j a n d A h m e d Zeriahi




       ABSTRACT. We study fine properties of quasiplurisubharmonic functions on compact Kiihler manifolds.
       We define and study several intrinsic capacities which characterize pluripolar sets and show that locally
       pluripolar sets are globally "quasi-pluripolar."



                                                    1. I n t r o d u c t i o n

      Since the fundamental work of Bedford and Taylor [4, 5], several authors have developed
a "Pluripotential theory" in domains of C n (or of Stein manifolds). This theory is devoted to
the fine study of plurisubharmonic (psh) functions and can be seen as a nonlinear generalization
of the classical potential theory (in one complex variable), where subharmonic functions and
the Laplace operator A are replaced by psh functions and the complex Monge-Amp~re operator
                                                                                    i --
(ddC) n. Here d, d c denote the real differential operators d := 0 + 0, d c := ~-[a      - a] so that
dd c = i 0 ~ , the normalization being chosen so that the positive measure (dd c 89log[1 + Ilz112])n
has total mass 1 in C n. We refer the reader to [3, 7, 26] for a survey of this local theory.
      Our aim here is to develop a global Pluripotential theory in the context of compact Kahler
manifolds. It follows from the maximum principle that there are no psh functions (except con-
stants) on a compact complex manifold X. However, there are usually plenty of positive closed
currents of bidegree (1, 1) (we refer the reader to [ 15, Ch. 3], for basic facts on positive currents).
Given co a real closed smooth form of bidegree (1, 1) on X, we may consider every positive closed
current co' of bidegree (1, 1) on X which is cohomologous to 09. When X is K~ihler, it follows
from the "ddC-lemma '' that cot can be written as co' = co + ddC~o, where q9 is a function which
is integrable with respect to any smooth volume form on X. Such a function ~0 will be called
w-plurisubharmonic (w-psh for short). It is globally defined on X and locally given as the sum
of a psh and a smooth function. We let P S H ( X , co) denote the set of w-psh functions. Such
functions were introduced by Demailly, who call them quasiplurisubharmonic (qpsh). These are
the main objects of study in this article.
      There are several motivations to study qpsh functions on compact K~Jaler manifolds. First of
all they arise naturally in complex analytic geometry as positive singular metrics of holomorphic



       Math Subject Classifications. 32W20, 32U15, 32Q15.
       Key Words and Phrases. Quasiplurisubharmonic functions, capacity, extremal functions, Kahler manifolds.

9 2005TheJournalof GeometricAnalysis
ISSN1050-6926
608                                 Vincent Guedj and Ahmed Zeriahi

line bundles (see Section 5) whose study is central to several questions of complex algebraic geom-
etry. Solving Monge-Amp~re equations associated to og-psh functions has been used to produce
metrics with prescribed singularities (see [13]). It is also related to the existence of canonical
metrics in K~ihler geometry (see [37]). Important contributions have been made by Kolodziej
in this direction [28] using techniques from local Pluripotential theory. Quasiplurisubharmonic
functions have also been used in [21 ] to define a notion of og-polynomial convexity and study the
fine approximation of positive currents by rational divisors. Last but not least, such functions are
of constant use in complex dynamics in several variables (see [17, 18, 22, 23, 33]).
```

## Additional source: GZ-intrinsic-capacities-JGA05-20261004-LF347-680

GZ-intrinsic-capacities-JGA05-20261004.txt, LF347--680, independently checked SHA256 `f4b9152da337a5f66f0c15a40ce23cf259aafbbcaa2a3bffac8d0947dd1e81ff`. Authenticated supplied body reproduced literally, including OCR.

```text
                                   3. Monge-Amp~re capacity
     In this section we introduce the global Monge-Amp~re capacity (see Definition 3.4). The
definition only makes sense when the cohomology class {w} has strong positivity properties. To
simplify our exposition we assume throughout this section that o9 is a K~ihler form.
     Let T be a positive closed current of bidegree (p, p) on X, 0 < p < n = d i m c X. It can be
thought of as a closed differential form of bidegree (p, p) with measure coefficients whose total
variation is controlled by                           /   1



                                         IITII := . L T A o9n-p         o




We refer the reader to [15, Ch. 3] for basic properties of positive currents. Given ~o E P S H ( X , o))
we write ~o ~ L I ( T ) if ~o is integrable with respect to each (measure) coefficient of T. This is
equivalent to ~0 being integrable with respect to the trace measure T A ogn-p. In this case, the
current ~0T is well defined, hence so is

                                    o9~0A T := o) A T + ddC(qgT) .

This is again apositive closed current on X, of bidegree (p + 1, p + 1). Indeed, positivity is a
local property which is stable under taking limits. One can locally regularize ~0 and approximate
o9~ A T by the currents o9~ A T which are positive since o9,p~ are smooth positive forms.
614                                            VincentGuedjand AhmedZeriahi

     When q) ~ P S H ( X , o9) N L~176 then ~o ~ L I ( T ) for any positive closed current T of
bidegree (p, p). One can thus inductively define o)j A T, 1 < j < n - p, for ~o e P S H ( X , co) O
L~176 For T = 0 and j = n one obtains the complex Monge-Amp~re operator, O)~o.       n It follows
from the local theory that the operator ~o ~ o)en is continuous under monotone sequences (see [5]).
The proof of these continuity properties is simpler in our compact setting. We refer the reader
to [24] where this is proved in a more general global context.

Proposition 3.1 (Chern-Levine-Nirenberg inequalities).                            Let T be a positive closed current
ofbidegree (p, p) on X andq) ~ P S H ( X , o9) n L ~ ( X ) .
      Then IIo)~ A TII = IITII. Moreover, i f ~ ~ P S H ( X , o9) n L I ( T ) , then ~p ~ L I ( T A o)~)
and
                      II~Plltl(T^,o~) ___ II~llzl(T) + [2 sup~p + supq) --i~f q)] IlZll 9
                                                           X       X

Proof.       By Stokes theorem, f x ddC~~A T A o)n-p-1 = 0, hence

                     IIo)~ A TII := f x W ~ A T A o)n-p-I = f x T A o)n-P := IITII .

Consider now ap ~ L I ( T ) . Since T has measure coefficients, this simply means that ~p is
integrable with respect to the total variation of these measures. Assume first ~ < 0, ~0 > 0 and
~o, ~ are smooth. Then

  [[~][LI(TA~o~) :~__-.f x ( - ~ ) T       A w~o A O)n - p - 1    =   II~PllLl(r~ +   fx(-*)z   A ddCq) A O)n-p-1 .

NOW it follows from Stokes theorem that

                                                        1                                        1



                                                                 fx T on-,
where the next to last inequality follows from q)T A o)n-p > 0 and - d d % p <_o9. This yields

                                    II~PllL~(r^,o~) -< Ii~PlILI(r) + sup~011TII.
                                                                      x
The general case follows by regularizing ~0, ~, observing that o)e = w~o,where q)f = q) _ infx q) >
0, and decomposing ~ = ~ ' + supx ~ with ~t = ~ _ suPx ~p < 0.                                   []

R e m a r k 3.2. The fact that the L l_norm of ~p with respect to the probability measure T A o2~ A
o)n-p-1 is controlled by its Ll-norm with respect to T A o)n-p is similar to the phenomenon
already encountered in Example 2.8: One can write

            T Ao)e /kO) n - p - 1      =    T Ao) n-p +ddCS, S = (q) - i.~f~0)T A O ) n - p - 1        > O.


This type of estimates is usually referred to as "Chern-Levine-Nirenberg inequalities," in reference
to [8] where simpler -but fundamental- L~-estimates were established (with ~ = constant).
Estimates involving the L 1.norm of if/were first proved in the local context by Cegrell [6] and
Demailly [12].

      A straightforward induction yields the following.
                                          Intrinsic Capacities on Compact Kiihler Manifolds                    615

Corollary 3.3.              Let ~, ~o E P S H ( X , o9) with 0 < ~o < 1. Then

                               o<_fx t 109 <_fx laP109n+ n [ 1 + 2sup@]
                                                                   X
                                                                        f 09n.
                                                                        dX
     Following Bedford-Taylor [5] and Kolodziej [29] we introduce the following Monge-Amp~re
capacity.

D e f i n i t i o n 3.4.    Let K be a Borel subset of X. We set

                            Cap~o(K) := sup                09<.o/ ~0 ~ P S H ( X , 09), 0 <_ ~0 <_ 1       .
                                                    IlK      n                                         }

     Note that this definition only makes sense when the cohomology class {09} is big, i.e., when
{09}n > 0, and when it admits locally bounded potentials ~0. This implies, by a regularization
result of Demailly [12], that {09} is big and neff In order to avoid technicalities, we are assuming
throughout this section that {09} is K~ihler.

Proposition 3.5.
       (1) I l K c K ~ c X are Borel subsets then

                  Volvo(K) := f 09n < Capoj(K) < Capo' (K') < Cap,o(X) = Volo~(X).
                              3K

        (2) l f K j are Borel subsets o f X thenCap~o(UK j) < ~ Capw(Kj). Moreover, Capoj(UKj) =
limCapo,(Kj) i f K j C Kj+I.
     (3) If091 < 092 then Captor(.) < Capm(.). For all A > 1, Cap,o(.) < CaPao,(.) <
A n Cap,o(.). In particular, if09, cot are two Kiihlerforms then there exists C > 1 such that
                                            1
                                                Cap,o(.) _< CaP,o,(.) _< C . CaP,o(.).

        (4) I f f : X ~ X is holomorphic then for all Borel subset K o f X,
                                                  Capco(f(K)) _< Capf.~o(K) 9
In particular, Capon(f (K)) = Cap~o(K) for every 09-isometry f .

Proof.       That Volvo(.) < Cap,o(.) is a straightforward consequence of the definition (since wo =
09). It then follows from Stokes theorem that f x o~ = f x (-onfor every ~o ~ P S H (X, 09) ML~176
                                                                                                 (X),
thus Volvo(X) = Cap~o(X).
        Property (2) is a straightforward consequence of the definitions.
     Ifwl < 092 then P S H ( X , o91) C P S H ( X , o92) hence Cap~ol(.) < Cap~(.). Fix A > 1. If
ap ~ P S H ( X , A09) is such that 0 < 7t < 1 then ~p/A ~ P S H ( X , w) with 0 < ~r/A < 1 / A < 1.
Moreover, (A09 + ddC~r) n = An(09 -F ddC(~t/A)) n. This shows CapaoJ(. ) < A n Capco(.).
    In particular, if 09, J are both K ~ l e r then A-109 < 09/ < A09 for some constant A > 1,
hence C -1 Capon(. ) < Capco,(. ) < C 9Capon(.) with C = A n.
      It remains to prove (4). It follows from the change of variables formula that if ~0
P S H ( X , o9) with 0 < ~0 < 1 then


                       f,         n <
                            (K) 09~0 --         f o09,o=         ( f ' 0 9 + ddC(~o o f ) ) n < Capf,o~(K)
616                                                Vincent Guedj and Ahmed Zeriahi

since~pof 6 P S H ( X , f ' 0 9 ) w i t h 0 < q~of < 1. W e i n f e r C a p w ( f ( K ) ) < Capf.w(K). When f
is a 09-isometry, i.e., f ~ Aut(X) with f ' 0 9 = w, then the mapping ~o w+ r o f is an isomorphism
of {u ~ P S H ( X , o9) / 0 < u < 1}, whence Cap~o(f(K)) = Capf.~o(K ) = Cap~o(K ).                         []

      Let P S H - (X, o9) denote the set of negative 09-psh functions. A set is said to be P S H ( X , 09)-
polar if it is included in the - c ~ locus of some function r E P S H ( X , w), r ~ - o 0 . As we
shall soon see, the sets of zero Monge-Amp&e capacity are precisely the P S H (X, 09)-polar sets.
We start by establishing the following:

Proposition 3.6.        I f P is a P S H ( X , w)-polar set, then CapofiP ) = O. More precisely, f f
r E P S H - ( X , o9) then

                      Capoj(r < - t ) < t
                                                      1%     (_r
                                                                                       ]
                                                                        + n Volvo(X) , Yt > O.


Proof.      Fix ~0 ~ P S H ( X , 09) such that 0 < ~0 < 1. Fix t > 0 and set Kt = {x E X / r                             <
- t } . By Chebyshev's inequality,


                      fK f~t
                               09~o <        (_r            -< tl[fx(-r             + n Voloo(X) ]
where the last inequality follows from Corollary 3.3. Taking supremum over all ~0's yields the
claim.                                                                                                                   []

                                                         * p
      Observe that the previous proposition says that CaP,o( ) = 0, where

                               Cap*(E) : = inf{CaP~o(G ) / G open with                 E C G},

is the outer capacity associate to Cap~o.

     Our aim is now to show that 09-psh functions are quasicontinuous with respect to Capo~
(Corollary 3.8). We first need to show that decreasing sequences of 09-psh functions converge "in
capacity."

Proposition 3.7.          Let r Cj ~ P S H (X, 09) M L ~176
                                                         (X) such that ( r                   decreases to r       Then for
each ~ > O,
                                               Cap~o({r j > r + 8}) ---> O.

Proof.       We can assume w.l.o.g, that Volvo(X) = 1 and 0 < Cj - r < 1. Fix 3 > 0 and
~0 ~ P S H ( X , 09), 0 < ~0 < 1. By Chebyshev inequality, it suffices to control f x ( r - r
uniformly in r      It follows from Stokes theorem that

               (r    - r            =        (r      - r      A 09~-1 -
                                                                          fx  d(r     - r   A dCq9 A 09~o     9

Now by Cauchy-Schwartz inequality,


         dfjAd~gA                       <_          dfjmdCfjA09~o -I             .       dfAdC~oAw~o -1              ,

where we set f j : = Cj - r >_ 0. Moreover,


              fx      A           A4'          =               ddc ) A 4 -1 < fx            A 4 -1 < 1,
                              Intrinsic Capacities on Compact Ktihler Manifolds                    617

since ~0c@-1 > 0, -ddCq9 < ~o and ~0 < 1. Similarly


             fx dfjAdCfjAo9~-l=               s     _fjddCfjAo9~     l<       fjoor   n-l .


Altogether this yields


        s       - ~)o~       <- f x O h - ~p)o>/x %n-1 _~_( f (1/fxj --) ~1)(.0~./ A2 r -1
                             < ~
                                        (Ix    (~/j -- ~)(0) + r    A 0)~-1
                                                                              )'" ,

where the last inequality follows from the elementary inequalities 0 < a < ~             _< 1 and V ~ +
4~_<4~+b.
     Going on replacing at each step a term w~0 by o) + w~, we end up with

                                         n ( (~/rjf - - x
                          (1/tj - - 1/t)O)~0 _< 2       r
                                                          )Jr- 0 ) ~ ) n 1/2n .
The majorant being independent of ~oand converging to 0 as j --~ + ~ (by dominated convergence
theorem), this completes the proof.                                                         []

C o r o l l a r y 3.8 (Quasicontinuity).  Let q9 ~ P S H ( X , ~o). For each e > 0 there exists an open
subset O e o f X such that CaP ~o( O e ) < e and ~o is continuous on X \ 0 ~.

Proof.     For t > 0 large enough, the set O1 = {~o < - t } has capacity < e / 2 by Proposi-
tion 3.6. Working in X \ O1 we can thus replace ~0 by ~0t = max(cp, - t ) which is bounded on X.
Regularizing ~0 (see Appendix), we can find a sequence apj of smooth Aco-psh functions which
decrease to ~ot on X, for some A > 1. By Proposition 3.7, the set Oj = {7% > ~ot + 1/j} has
capacity < e2 - j - 1 if kj is large enough. Now 7zkj uniformly converges to r = ~0t on X \ Oe,
Oe = Uj>_I O j, SO ~0 is continuous on X \ Os and Cap~o(Os) < e.                              []

E x a m p l e 3.9. The capacity Cap,o(-) does not distinguish between "big sets." Assume indeed
there exists an ample divisor D such that [D] --~ kw, k 6 N. Then there exists ~o 6 P S H ( X , o~)
such that ddC~o = k - l [ D ] - o). Note that q9 6 C~      \ D), e ~~ E C~    and {~p = -cx~} =
D. Replacing ~o by ~o - suPx ~o if necessary, we may assume supx ~o = 0. Consider ~Oc =
max(~o, - c ) E P S H ( X, w) N C~     Then qgc - ~o outside some neighborhood Vc = {q9 < - c }
of D. Since 0 _< 1 + ~ol < 1 and ~o1+~ol = oJ~ = 0 in X \ V1, we get


                     Capo/X)=fx(~Ol+~,)n=fv(o~l+~01)n -< Cap~o( V D ,
                                                           1


hence Cap~o(V1) = CapofiX).
      As a concrete example take X = C ~ n and 09 = ~OFS, D being some hyperplane H ~ "at
infinity" (k = 1). Set ~o[z : t] = log It[ - 1 log[[lz[[2 + [t[2] where z denotes the Euclidean
coordinates in C n = C]Pn \ Hoo and H ~ = (t = 0). Observe that supcy. ~p = 0. One then
computes
                              Clan\v1 = [ z E C n / I z [      <   e2x/~--l] .

Thus, the capacity of the complement of any Euclidean ball of radius smaller than 4 ~ e2 - 1 equals
618                                      Vincent Guedj and Ahmed Zeriahi

     The definition of Cap, o mimics the definition of the relative Monge-Amp~re capacity intro-
duced by Bedford and Taylor in [5]. Fix/d = {Ha } a finite covering of X by strictly pseudoconvex
open subsets of X, Ha = {x ~ X / O~(x) < 0}, where 06 is a strictly psh smooth function de-
fined in a neighborhood of ~-~. Fix 3 > 0 such that L/~ = {Hi } is still a covering of X, where
Lt~ = {x ~ X / • (x) < -3}. For a Borel subset K of X, we set

                                CaPBT(K) := Z           CapsT (K N/.g~, b/~) ,
                                                   c~



where
                CaPeT(E, f2) := sup { f~ (ddcu)n / u 6 PSH(~2), O < u < l }

is the capacity studied by Bedford and Taylor. The next proposition is due to Kolodziej [29]. We
include a slightly different proof.

Proposition 3.10.       There exists C >_ 1 such that
                                 1
                                     Cap~(.) _< C a p s r ( . ) _< C . Cap~(.).


Proof        Let E be aBorel subset of X. Since Cap~o(E N/d~) < CaPon(E) _< Y-~.aCapo~(E NL/~),
it is sufficient to show that if f2 = {x ~ X / O(x) < 0} is a smooth hyperconvex subset of X, then
there exists C _> 1 such that for all E C f26,

                           1
                                Capw(E ) < C a p n r ( E , g2) < C 9Cap,o(E),

where ~2~ = {x ~ X / 0(x) < -6}.
         It is an easy and well known fact in the local theory that the capacities Cap(., ~2) and
Cap(., f2') are comparable when f2' c fl (see e.g., Theorem 6.5 in [12]). Therefore we can
assume (passing to a finer covering if necessary) that co = ddC~l, near f2. Fix C1 > 0 such
t h a t - C 1 < ~P < C l O n f2. Fix~o 6 P S H ( X , 09) such t h a t 0 < ~0 < 1 o n X a n d s e t u =
(2C1)-1(~o + ~O + C1). Then u ~ PSH(~2) and 0 < u < 1, hence


                     fe "--(2c,)"L
                         09go                   (ddcu)n --< (2c1)nCapsT(E'g2) ,

which yields Cap,o(E) < (2C1) n C a p n r ( E , fl). Observe that we have not used here that 09 is
Kahler.
      For the reverse inequality we consider X 6 C~176 such that X = 0 in X \ ~2 and X < 0
in f~. Replacing X by eX if necessary, we can assume X e P S H ( X , 09). This is because 09 is
K~thler (and this is the only place where we shall use this crucial assumption). Fix e > 0 so small
that X < - e on ~2a. Let now u 6 PSH(f2) be such that 0 < u < 1 on f2. Consider

                                                  u-•-]-Cl                 in   f28
                                                    2+2C1
                    ~0(x) =          max ~ 2~UCtt , zX
                                         [ u - ~ + C     2 (x) + 1)        in   g2 \ f28
                                                    1                      in   X\~

Observe that 0 < u' := (u - ~ + C1)/(2 + 2C1) < (1 + 2C1)/(2 + 2C1) < 1 in g2. Therefore
~o ~ P S H ( X , 209) since 2X(x) + 1 < - 1 < u' in f2~, while 2X(X ) + 1 - 1 > u' on 092. Note,
                             Intrinsic Capacities on Compact Kiihler Manifolds                     619

also that 0 < ~o < 1 thus for E C f2~,

              1
        (2 + 2C1)n f E (ddcu)n
                                                 - -     + ddC q9     )"   <         co + ddC ~o
                                     =

                                     <
                                                 2 + 2C1

                                           Cap2~o/e(E) <
                                                               (!)n        --

                                                                     Cap~o(E)

hence CapBT(E, f2) < 4n(1 + c 1 ) n E - n Capo~(E ).                                                []

     Since locally pluripolar sets are precisely the sets of zero relative capacity [5], we obtain the
following:

Corollary 3.11.      Cap~o(P) = 0 r162CapBT(P ) = 0 r            Pis locally plul~polar.

     We shall show later on that locally pluripolar sets are P S H ( X , w)-polar when o9 is K~ihler
(see Theorem 7.2).
     The following two results are direct consequences of the corresponding results of Bedford
and Taylor [4, 5].
```

## Additional foundation: BEGZ-0812.3674v2-20261004.txt, LF180--248

Independent SHA256 `a9817dcf1e66414e9b0e6754baddfda52b4dd76cef4a5e046e4d5ad390a3252e`. Literal LF slice, without an added final LF in its digest.

```text

on X as a closed positive (p, p)-current. The wedge product only depends on
the closed positive (1, 1)-currents ddc uj , and not on the speciﬁc choice of the
potentials uj .
   A very important property of this construction is that it is local in the plurifine
topology, in the following sense. If uj , vj are locally bounded psh functions on X
and uj = vj (pointwise) on a pluriﬁne open subset O of U , then
                   1O ddc u1 ∧ ... ∧ ddc up = 1O ddc v1 ∧ ... ∧ ddc vp .
This is indeed an obvious generalization of Corollary 4.3 of [4].
   In the case of a possibly unbounded psh function u, Bedford-Taylor have ob-
served (cf. p.236 of [4]) that it is always possible to deﬁne the non-pluripolar
part of the would-be positive measure (ddc u)n as a Borel measure. The main
issue however is that this measure is not going to be locally ﬁnite in general (see
Example 1.3 below). More generally, suppose we are trying to associate to any
p-tuple u1 , ..., up of psh functions on X a positive (a priori not necessarily closed)
(p, p)-current
                                   hddc u1 ∧ ... ∧ ddc up i
putting no mass on pluripolar subsets, in such a way that the construction is
local in the pluriﬁne topology in the above sense. Then we have no choice: since
uj coincides with the locally bounded psh function max(uj , −k) on the pluriﬁne
open subset                               \
                                   Ok := {uj > −k},
                                          j
we must have              ^               ^
                     1Ok h ddc uj i = 1Ok   ddc max(uj , −k),                    (1.1)
                            j                  j
Note that the
            V right-hand side is non-decreasing in k. This equation completely
determines h j ddc uj i since the latter is required not to put mass on the pluripolar
        S
set X − k Ok = {u = −∞}.
Definition 1.1. If u1 , ..., up are psh functions
                                             V on the complex manifold X, we
shall say that the non-pluripolar product h j ddc uj i is well-defined on X if for
each compact subset K of X we have
                      Z                ^
                  sup          ω n−p ∧   ddc max(uj , −k) < +∞               (1.2)
                     k   K∩Ok            j
for all k.
   Here ω is an auxiliary (strictly) positive (1, 1)-form on X with respect to which
masses are being measured, the condition being of course independent ofV   ω. When
(1.2) is satisﬁed, equation (1.1) indeed deﬁnes a positive (p, p)-current h j ddc uj i
on X. We will show below that it is automatically closed (Theorem 1.8).
   Condition (1.2) is always satisﬁed when p = 1, and in fact it is not diﬃcult to
show that
                               hddc ui = 1{u>−∞} ddc u.
There are however examples where non-pluripolar products are not well-deﬁned
as soon as p ≥ 2. This is most easily understood in the following situation.
6                 S. BOUCKSOM, P. EYSSIDIEUX, V. GUEDJ, A.ZERIAHI

Definition 1.2. A psh function u on X will be said to have small unbounded
locus if there exists a (locally) complete pluripolar closed subset A of X outside
which u is locally bounded.
   Assume that u1 , ..., up have small unbounded locus, and let A be closed com-
plete pluripolar such that each uj is locally bounded outside A V
                                                                (recall that com-
plete pluripolar subsets are stable under ﬁnite unions). Then h j ddc uj i is well-
                                          V
deﬁned iﬀ the Bedford-Taylor product j ddc uj , which is deﬁned on the open
                                                                        V
subset X −A, has locally ﬁnite mass near each point of A. In that case h j ddc uj i
                                        V
is nothing but the trivial extension of j ddc uj to X.
Example 1.3. Consider Kiselman’s example (see [32])
                           u(x, y) := (1 − |x|2 )(− log |y|)1/2
for (x, y) ∈ C2 near 0. The function u is psh near 0, it is smooth outside the y = 0
axis, but the smooth measure (ddc u)2 , defined outside y = 0, is not locally finite
near any point of y = 0. This means that the positive Borel measure h(ddc u)2 i is
not locally finite.
```

## Additional foundation: BEGZ-0812.3674v2-20261004.txt, LF323--477

Independent SHA256 `462891277734fc5ab0efef31d1a327cb2de16257bfdc3ec5f24424db0e67909f`. Literal LF slice, without an added final LF in its digest.

```text
  A crucial point for what follows is that non-pluripolar products of globally
deﬁned currents are always well-deﬁned on compact Kähler manifolds:
Proposition 1.6. Let T1 , ..., Tp be closed positive (1, 1)-currents on a compact
Kähler manifold X. Then their non-pluripolar product hT1 ∧ ... ∧ Tp i is well-
defined.
Proof. Let ω be a Kähler form on X. In view of the third point of Proposi-
tion 1.4, upon adding a large multiple of ω to the Tj ’s we may assume that their
cohomology classes are Kähler classes. We can thus ﬁnd Kähler forms ωj and
ωj -psh functions ϕj such that Tj = ωj + ddc ϕj . Let U be a small open subset of
8                S. BOUCKSOM, P. EYSSIDIEUX, V. GUEDJ, A.ZERIAHI

X on which ωj = ddc ψj , where ψj ≤ 0 is a smooth psh function on U , so that
Tj = ddc uj on U with uj := ψj + ϕj . The bounded psh functions on U
                                           ψj + max(ϕj , −k)
and
                                 max(uj , −k)
coincide on the pluriﬁne open subset {uj > −k} ⊂ {ϕj > −k}, thus we have
                     Z                  ^
                                  n−p
                       T        ω     ∧   ddc max(uj , −k)
                               j {uj >−k}                       j
                     Z                                  ^
                 =       T                ω n−p ∧        (ωj + ddc max(ϕj , −k))
                             j {uj >−k}                     j
                              Z                 ^
                         ≤            ω n−p ∧       (ωj + ddc max(ϕj , −k)).
                                  X             j
But the latter integral is computed in cohomology, hence independent of k, and
this shows that (1.2) is satisﬁed on U , qed.                                
Remark 1.7. The same property extends to the case where X is a compact com-
plex manifold in the Fujiki class, that is bimeromorphic to a compact Kähler
manifold. Indeed there exists in that case a modiﬁcation µ : X ′ → X with
X ′ compact Kähler. Since µ is an isomorphism outside closed analytic (hence
pluripolar) subsets, it is easy to deduce that hT1 ∧ ... ∧ Tp i is well-deﬁned on X
from the fact that hµ∗ T1 ∧ ... ∧ µ∗ Tp i is well-deﬁned on X ′ , and in fact
                         hT1 ∧ ... ∧ Tp i = µ∗ hµ∗ T1 ∧ ... ∧ µ∗ Tp i.
On the other hand it seems to be unknown whether ﬁniteness of non-pluripolar
products holds on arbitrary compact complex manifolds.
  Building on the proof of the Skoda-El Mir extension theorem, we will now
prove the less trivial closedness property of non-pluripolar products.
Theorem 1.8. Let T1 , ..., Tp be closed positive (1, 1)-currents on a complex man-
ifold X whose non-pluripolar product is well-defined. Then the positive (p, p)-
current hT1 ∧ ... ∧ Tp i is closed.
Proof. The result is of course local, and we can assume that X is a small neigh-
borhood of 0 ∈ Cn . The proof will follow rather closely Sibony’s exposition of
the Skoda-El Mir theorem [39], cf. also [18, pp. 159-161].
   Let uj ≤ 0 be a local potential of Tj near 0 ∈ Cn , and for each k consider the
closed positive current of bidimension (1, 1)
                                      ^
                           Θk := ρ ∧    ddc max(uj , −k)
                                                    j

and the pluriﬁne open subset
                                                    \
                                          Ok :=      {uj > −k}
                                                        j
            MONGE-AMPÈRE EQUATIONS IN BIG COHOMOLOGY CLASSES                          9

so that 1Ok Θk converges towards
                                  ρ ∧ hT1 ∧ ... ∧ Tp i
by (1.1). Here ρ is a positive (n − p − 1, n − p − 1)-form with constant coeﬃcients,
so that Θk has bidimension (1, 1). It is enough to show that
                                  lim d (1Ok Θk ) = 0
                                 k→∞
for any choice ofP
                 such a form ρ.
   Let also u := j uj , so that u ≤ −k outside Ok , and set

                                    wk := χ(eu/k ),
where χ(t) is a smooth convex and non-decreasing function of t ∈ R such that
χ(t) = 0 for t ≤ 1/2 and χ(1) = 1. We thus see that 0 ≤ wk ≤ 1 is a non-
decreasing sequence of bounded psh functions deﬁned near 0 ∈ Cn with wk = 0
outside Ok and wk → 1 pointwise outside the pluripolar set {u = −∞}. Finally
let 0 ≤ θ(t) ≤ 1 be a smooth non-decreasing function of t ∈ R such that θ(t) = 0
for t ≤ 1/2 and θ ≡ 1 near t = 1. The functions θ(wk ) are bounded, non-
decreasing in k and we have
                                 θ(wk ) ≤ 1Ok
since θ(wk ) ≤ 1 vanishes outside Ok . Note also that θ ′ (wk ) vanishes outside Ok ,
and converges to 0 pointwise outside {u = −∞}.
   Our goal is to show that
                                 lim d (1Ok Θk ) = 0.
                                 k→∞
But we have
                0 ≤ (1Ok − θ(wk )) Θk ≤ (1 − θ(wk )) hT1 ∧ ... ∧ Tp i,
and the latter converges to 0 by dominated convergence since θ(wk ) → 1 pointwise
outside the polar set of u, which is negligible for hT1 ∧...∧Tp i. It is thus equivalent
to show that
                                lim d (θ(wk )Θk ) = 0.
                                k→∞
Since wk is a bounded psh function, Lemma 1.9 below shows that the chain rule
applies, that is
                       d (θ(wk )Θk ) = θ ′ (wk )dwk ∧ Θk .
Recall that dwk ∧ Θk has order 0 by Bedford-Taylor, so that the right-hand side
makes sense. Now let ψ be a given smooth 1-form compactly supported near 0
and let τ ≥ 0 be a smooth cut-oﬀ function with τ ≡ 1 on the support of ψ. The
Cauchy-Schwarz inequality implies
  Z                     2   Z                      Z                    
      ′                                   c               ′     2
     θ (wk )ψ ∧ dwk ∧ Θk ≤       τ dwk ∧ d wk ∧ Θk       θ (wk ) ψ ∧ ψ ∧ Θk .

But on the one hand we have
                    Z                  Z
                  2 τ dwk ∧ d wk ∧ Θk ≤ τ ddc wk2 ∧ Θk
                             c
10                  S. BOUCKSOM, P. EYSSIDIEUX, V. GUEDJ, A.ZERIAHI
                               Z                      Z
                           =       wk2 ddc τ ∧ Θk =        wk2 ddc τ ∧ Θk
                                                      Ok
since wk vanishes outside Ok , and the last integral is uniformly bounded since
0 ≤ wk ≤ 1 and 1Ok Θk has uniformly bounded mass by (1.2). On the other hand
we have
                   θ ′ (wk )2 Θk = θ ′ (wk )2 1Ok Θk ≤ θ ′ (wk )2 hT1 ∧ ... ∧ Tp i
since θ ′ (wk ) also vanishes outside Ok , and we conclude that
                                       Z
                                 lim      θ ′ (wk )2 ψ ∧ ψ ∧ Θk = 0
                                   k→∞

by dominated convergence since θ ′ (wk ) → 0 pointwise ouside the polar set of u,
which is negligible for hT1 ∧ ... ∧ Tp i. The proof is thus complete.          
Lemma 1.9. Let Θ be a closed positive (p, p)-current on a complex manifold X,
f be a smooth function on R and v be a bounded psh function. Then we have
                                     d(f (v)Θ) = f ′ (v)dv ∧ Θ.
Proof. This is a local result, and we can thus assume that Θ has bidimension (1, 1)
by multiplying it by constant forms as above. The result is of course true when
v is smooth. As we shall see the result holds true in our case basically because v
belongs to the Sobolev space L21 (Θ), in the sense that dv ∧ dc v ∧ Θ is well-deﬁned.
Indeed the result is standard when Θ = [X], and proceeds by approximation.
Here we let vk be a decreasing sequence of smooth psh functions converging
pointwise to v. We then have f (vk )θ → f (v)Θ by dominated convergence, thus
it suﬃces to show that
                               lim f ′ (vk )dvk ∧ Θ = f ′ (v)dv ∧ Θ.
                               k→∞
We write
                                                       
 f ′ (vk )dvk ∧ Θ − f ′ (v)dv ∧ Θ = f ′ (vk ) − f ′ (v) dvk ∧ Θ + f ′ (v)(dvk − dv) ∧ Θ.
Let ψ be a test 1-form and τ ≥ 0 be a smooth cut-oﬀ function with τ ≡ 1 on the
support of ψ. Cauchy-Schwarz implies
                        Z                                   2
                                               
                            f ′ (vk ) − f ′ (v) ψ ∧ dvk ∧ Θ
               Z                                          Z                  
                       ′
                                    2
                                     ′                                      c
           ≤         f (vk ) − f (v) ψ ∧ ψ ∧ Θ                   τ dvk ∧ d vk ∧ Θ .
The second factor is bounded since dvk ∧ dc vk ∧ Θ converges to dv ∧ dc v ∧ Θ by
Bedford-Taylor’s monotone convergence theorem, and the ﬁrst one converges to
0 by dominated convergence. We similarly have
                          Z                            2
                            f ′ (v)(dvk − dv) ∧ ψ ∧ Θ
            Z                     Z                              
                  ′   2                                c
         ≤       f (v) ψ ∧ ψ ∧ Θ        τ d(vk − v) ∧ d (vk − v) ∧ Θ ,
where now the ﬁrst factor is bounded while the second one tends to 0 by Bedford-
Taylor once again, and the proof is complete.                                 
```

## Additional foundation: BEGZ-0812.3674v2-20261004.txt, LF525--578

Independent SHA256 `0acf2b360d001a14d0fcf47f784424a599506386e6e44bc4b968ddd9bb80dc7d`. Literal LF slice, without an added final LF in its digest.

```text

1.3. Positive cohomology classes. Let X be a compact Kähler manifold and
let α ∈ H 1,1 (X, R) be a real (1, 1)-cohomology class.
   Recall that α is said to be pseudo-effective (psef for short) if it can be repre-
sented by a closed positive (1, 1)-current T . If θ is a given smooth representative
of α, then any such current can be written as T = θ + ddc ϕ, where ϕ is thus a θ-
psh function by deﬁnition, and will sometimes be referred to as a global potential
of T . Global potentials only depend on the choice of θ up to a smooth function
on X.
   On the other hand, α is nef if it lies in the closure of the Kähler cone. Such
a class can thus be represented by smooth forms with arbitrarily small nega-
tive parts, and a compactness argument then shows that α contains a positive
current, i.e. nef implies psef. Note however that the negative part of smooth
representatives cannot be taken to be 0 in general. In fact, Demailly, Peternell
and Schneider have shown in [23] that a classical construction of Serre yields an
example of a smooth curve C on a projective surface whose cohomology class is
nef but contains only one positive current, to wit (the integration current on) C
itself.
   The set of all nef classes is by deﬁnition a closed convex cone in H 1,1 (X, R),
whose interior is none but the Kähler cone. The set of all psef classes also forms a
closed convex cone, and its interior is by deﬁnition the set of all big cohomology
classes. In other words, a class α is big iﬀ it can be represented by a strictly
positive current, i.e. a closed current T that dominates some (small enough)
smooth strictly positive form on X.

1.4. Comparison of singularities. If T and T ′ are two closed positive currents
on X, then T is said to be more singular than T ′ if their global potentials satisfy
ϕ ≤ ϕ′ + O(1). By the singularity type of T , we will mean its equivalence class
with respect to the above notion of comparison of singularities.
   A positive current T in a given psef class α is now said to have minimal
singularities (inside its cohomology class) if it is less singular than any other
positive current in α, and its θ-psh potentials ϕ will correspondingly be said
to have minimal singularities. Such θ-psh functions with minimal singularities
always exist, as was observed by Demailly. Indeed, the upper envelope
                         Vθ := sup {ϕ θ-psh, ϕ ≤ 0 on X}
of all non-positive θ-psh functions obviously yields a positive current
                                     θ + ddc Vθ
with minimal singularities (note that Vθ is usc since Vθ∗ is a candidate in the
envelope).
   We stress that currents with minimal singularities in a given class α are in
general far from unique. Indeed currents with minimal singularities in a class
α admitting a smooth non-negative representative θ ≥ 0 (for instance a Kähler
class) are exactly those with bounded potentials.
   Currents with minimal singularities are stable under pull-back:
            MONGE-AMPÈRE EQUATIONS IN BIG COHOMOLOGY CLASSES                       13

Proposition 1.12. Let π : Y → X be a surjective morphism between compact
Kähler manifolds and θ be a smooth closed (1, 1)-form on X. If ϕ is a θ-psh
function with minimal singularities on X, then the π ∗ θ-psh function ϕ ◦ π also
has minimal singularities.
Proof. Let ψ be a π ∗ θ-psh function. For x ∈ X a regular value of π we set
                                τ (x) := sup ψ(y).
                                         π(y)=x

```

## Additional foundation: DDNL18-2049-2087-20261004.txt, LF350--369

Independent SHA256 `0d34fd95c9beb603186a5ec408cb5b463d1bdda346042cdc66ac38b25fde6c71`. Literal LF slice, without an added final LF in its digest.

```text
2017, Theorem 4.26] for a proof of this result, which is merely a slight generalization of [Xing 1996,
Theorem 1].

Proposition 2.2. Let  ⊂ Cn be an open set. Suppose { f j } j are uniformly bounded quasicontinuous func-
                                                                                     j         j                  j
tions which converge in capacity to another quasicontinuous function f on . Let {u 1 } j , {u 2 } j , . . . , {u n } j
be uniformly bounded plurisubharmonic functions on , converging in capacity to u 1 , u 2 , . . . , u n respec-
tively. Then we have the following weak convergence of measures:
                                j            j
                         f j i∂ ∂u
                                ¯ ∧ i∂ ∂u
                                   1
                                       ¯ ∧ · · · ∧ i∂ ∂u
                                          2
                                                      ¯ nj → f i∂ ∂u
                                                                  ¯ 1 ∧ i∂ ∂u
                                                                           ¯ 2 ∧ · · · ∧ i∂ ∂u
                                                                                            ¯ n.

   The following lower-semicontinuity property of nonpluripolar products will be key in the sequel:
```

## Additional foundation: Vu-2004.11111v1-20261004.txt, LF273--287

Independent SHA256 `1ba50d3f123db57547622b7cecbab561eb1cfbe4c81617a290f80b1ec41af8ad`. Literal LF slice, without an added final LF in its digest.

```text
    We now give a definition which will be crucial later. Let (Tk )k be a sequence of
closed positive currents of bi-degree (m, m) on U. We say that (Tk )k satisfies Condition
(∗) if (Tk )k is of uniformly bounded mass on compact subsets of U, and for every open
set U ′ ⊂ U and every bounded psh function u on U ′ and every sequence (uk )k of psh
functions on U ′ decreasing to u, we have

                                   lim (uk − u)(ddc u)m ∧ Tk = 0                          (2.2)
                                k→∞

An obvious example for sequences satisfying Condition (∗) is constant sequences: Tk = T
for every k. We can also take (Tk )k to be a sequence of suitable Monge-Ampère operators
with decreasing potentials, see [1, 10, 15]. Concerning Condition (∗), we will use mostly
the example of constant sequences and the one provided by the following result.
Theorem 2.2. Let S be a closed positive current on U. Let v be a psh function on U such
that v is locally integrable with respect to the trace measure of S and (vk )k a sequence of psh
```

## Additional foundation: Vu-2005.13241v3-20261004.txt, LF53--78

Independent SHA256 `f47dc8f2ccf80aa64ddf28d987eb8b2ee409d404a0d66a1cfcbced66fd1ed789`. Literal LF slice, without an added final LF in its digest.

```text
(1.1)                             ˙ i} ≤ {hT1′ ∧ · · · ∧ Tm′ ∧T
                {hT1 ∧ · · · ∧ Tm ∧T                         ˙ i}.

The last inequality allows us to define the notion of T -relative full mass
intersection, see [14, 4]. We say that T1 , . . . , Tm are of T -relative full mass
intersection if          m              m
                        ^               ^
                              ˙
                      {h Tj ∧T i} = {h Tj,min∧T       ˙ i},
                         j=1               j=1

where Tj,min is a current with minimal singularities in the class {Tj } for
1 ≤ j ≤ m.
   Let α be a pseudoeffective (1, 1)-class. Denote by Em (α, T ) the set of
currents P ∈ α such that P, . . . , P (m times P ) are of T -relative full mass
intersection.
   Recall that W − is the set of convex increasing functions χ from R to
R such that χ(−∞) = −∞. Let χ ∈ W − . We can define Eχ,m(α, T ) to be
the subclass of Em (α, T ) consisting of P such that P has finite (T -relative)
χ-energy. When T ≡ 1 and m = n, the class Eχ,m (α, T ) generalizes the
usual class of currents with finite energy in [4, 11], see also [5] for the
local setting. We refer to Section 3 for details. For the moment, we note
here that                              [
                         Em (α, T ) =      Eχ,m (α, T ).
                                      χ∈W −

```
