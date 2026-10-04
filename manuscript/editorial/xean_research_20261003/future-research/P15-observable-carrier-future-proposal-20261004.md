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
