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
