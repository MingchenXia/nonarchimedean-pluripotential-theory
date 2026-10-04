# P06.2 R0: source and proof repair dossier

4 October 2026. Author self-audit; unverified draft. **R0 is not proved in this
submission.** The original arbitrary-dimensional P06.2 is also unresolved.
This is a repair dossier, not a replacement theorem or a paper claiming curve
recognition. In particular there is no unconditional recognition claim hidden
behind the dependency ledger below.

The exact requested R0 has not been narrowed: for every complete nontrivially
valued K, every good separated strict boundaryless pure one-dimensional
K-analytic X, every ordinary open U, and every finite continuous real h on U,
the proposed implication is from the actual ordinary CLD equation
d'd''[h]=0 to GR harmonicity and classical pluriharmonicity with every analytic
field extension and every analytic curve probe. Singular and nonreduced curves
are included. No scalar-stability, perfectness, or algebraicity hypothesis is
added. Optional real PL, GJR harmonicity, higher-dimensional ground-field
probes P0, arbitrary-extension ordinary-current ascent, two-sign ordinary
smooth psh regularization, and ordinary harmonic approximation are unclaimed.

The predecessor's canonical notes were read from its campaign run.json.
Its claimed T/C/B/Q results, citations, and review dispositions are evidence
under inspection, not premises. The entire supplied INCONCLUSIVE report,
all 26 premises, and all 28 passage records were read. None is treated as an
axiom. This submission proves the independent foundational repair A below,
and supplies local repairs D and E with their precise input hypotheses.
They do not constitute a new special case of the recognition theorem.

## A. Strict maximal-residue finiteness, with a complete Tate argument

**Lemma A.** Let K be a complete non-Archimedean field and
T_n=K⟨X_1,...,X_n⟩ the strict Tate algebra with its Gauss norm. Every maximal
ideal of a quotient T_n/I has residue field finite over K. Every
zero-dimensional strict K-affinoid algebra is finite-dimensional over K and
Artinian. In particular, its analytic carrier is a finite set of rigid points.
The algebraic assertions also hold for trivially valued K. The applications
here use nontrivially valued K. This proves the finiteness required at audit
premise 7; it does not use a statement of the strict Nullstellensatz. Its
correct BGR locator is 6.1.2/3, not the predecessor's 6.1.2/1.

We give division, normalization, and the finiteness deduction explicitly.
T_n consists of series whose coefficients tend to zero; coefficient maximum
defines a complete norm. Multiplication is continuous and the Gauss norm is
multiplicative: scale two nonzero series by coefficients attaining their
norms and reduce modulo elements of norm <1. The resulting nonzero finite
polynomials have nonzero product over the residue field. Completeness follows
coefficientwise from completeness of K and the uniform vanishing of tails.

Write R=T_{n-1} and T_n=R⟨Y⟩. First let
p=Y^d+Σ_{j<d}a_jY^j with ||a_j||≤1. Euclidean division of a polynomial by p
gives a quotient Q_p and remainder R_p of degree <d, each of norm at most
the polynomial's norm. Indeed each elimination subtracts a scalar multiple
of a monic polynomial whose coefficients have norm ≤1. The maps are linear,
so they extend by completion to R⟨Y⟩, since polynomials are dense. The identity
g=pQ_p(g)+R_p(g) persists in the limit. Its uniqueness persists as well: for
polynomial quotients h, Q_p(ph)=h and R_p(ph)=0; boundedness and density give
these identities for every restricted series h. Also Q_p(r)=0 and R_p(r)=r
for remainders. Apply these identities to ph+r=0.

Suppose f=Σa_jY^j has ||a_j||≤1, a_d is a unit with ||a_d||=||a_d^{-1}||=1,
and sup_{j>d}||a_j||<1. After multiplication by a_d^{-1}, write f=p+e,
where p is monic of degree d with coefficients bounded by 1 and ||e||<1.
For any g solve

    q=Q_p(g)-Q_p(eq).

The right side is a contraction on the complete Banach space R⟨Y⟩.
Starting at zero, differences shrink by the fixed factor ||e||<1, so the
iterates converge to a unique q. Put r=R_p(g-eq). Then g=fq+r.
Uniqueness follows by applying Q_p to fq+r=0: q=-Q_p(eq), hence q=0,
then r=0. Thus R⟨Y⟩/(f) is free of rank d over R, represented by the
remainders. This proof is valid without a discrete value group, perfect
residue field, or reduced quotient. For d=0 it says that f is a unit.

Every nonzero f in T_n can be made of this form by an isometric triangular
coordinate change. Divide by a coefficient attaining its Gauss norm. Its
reduction is a nonzero finite polynomial. Choose an integer M larger than
every exponent occurring in that reduction and set N_i=M^i for 1≤i<n.
The weights (N_1,...,N_{n-1},1) distinguish all its exponent vectors, by
uniqueness of base-M expansion. Replace X_i by X_i+Y^{N_i}, keeping Y=X_n.
This bounded substitution has bounded inverse X_i↦X_i-Y^{N_i}, so it is
an isometric automorphism. In the substituted reduction, the term of largest
weighted degree produces the unique highest power Y^d, with a nonzero
constant coefficient. No other term has that Y-degree. Therefore the
coefficient a_d reduces to a nonzero constant, all higher coefficients have
norm <1, and ||a_j||≤1. The restricted-series condition makes the supremum
of the higher coefficients strictly <1, not merely pointwise <1.
Write a_d=c(1+b), |c|=1, ||b||<1; its inverse is the convergent geometric
series. Thus the division hypotheses just proved hold. If f belongs to a
proper ideal, d cannot be zero.

Induction now proves the precise normalization assertion needed: every
nonzero quotient A=T_n/I admits an injective map T_d→A for some 0≤d≤n
and is a finite module over T_d. For I=0 take d=n. Otherwise normalize a
nonzero f∈I as above. The ring T_n/(f) is finite over T_{n-1}, hence so
is A. Put J=ker(T_{n-1}→A). Apply induction to T_{n-1}/J, which injects
into A. Finiteness composes. These are algebraic finite-module assertions;
no finite-flat assertion is inferred for the quotient A.

For clarity, noetherianity needed below follows from the same argument,
independently of the residue-field assertion. Induct on n. For any nonzero
ideal I, select and normalize f∈I. T_n/(f) is finite over the noetherian
ring T_{n-1}; consequently its submodule I/(f) is finitely generated over
T_{n-1}, and lifts of those generators together with f generate I over T_n.
The zero ideal is already finitely generated. Thus T_n and its quotients
are noetherian.

Let E=T_n/m be a field. Normalization makes E finite over an injected T_d.
A finite ring extension is integral: multiplication by an element on a finite
set of module generators and the determinant identity give a monic equation
annihilating the module, hence its element 1. If a field E is integral over
an injected domain R, then R is a field. For r≠0 in R, the element r^{-1}
in E satisfies a monic equation; multiplying it by r^{N-1} expresses r^{-1}
as an element of R. But T_d for d>0 is not a field, since evaluation
X_1=0 has a proper kernel containing X_1. Hence d=0 and [E:K]<∞.
Maximal ideals of any quotient lift to maximal ideals of T_n, giving the
first assertion.

If A is a zero-dimensional strict affinoid, all its primes are maximal.
A noetherian spectrum has finitely many irreducible components: split a
nonirreducible closed set into two proper closed sets and use noetherian
induction. Their generic primes give finitely many minimal primes; here
these are all primes. The nilradical N is finitely generated by nilpotent
elements, so N^s=0 for some s. The Chinese remainder theorem gives
A/N=∏_i A/m_i, a finite product of the finite extensions just proved.
Each N^j/N^{j+1} is a finite module over A/N by noetherianity. The finite
filtration therefore proves dim_K A<∞. It also proves that A is Artinian.

For the last, analytic assertion we use exactly the following standard
analytic foundations, not another Nullstellensatz: an affinoid spectrum maps
surjectively to its prime spectrum (CLD 11.1.2; maximal kernels already
suffice, and those are covered in 11.1.1), and finite affinoid algebras
carry their finite-module Banach topology (CLD 11.4.4). Their source bodies
are included in Appendix S. Alternatively, in this finite-dimensional case
all subspaces are closed: induction on dimension shows equivalence of every
norm with a basis maximum norm, by bounding the distance of the last basis
vector from the closed complete span of the preceding ones. Quotient fields
are therefore complete finite-dimensional normed algebras. Spectral
surjectivity gives a multiplicative seminorm with kernel each m_i. It is an
absolute value on the corresponding finite field. Two extending absolute
values on a finite extension are equivalent finite-dimensional norms; apply
the equivalence inequalities to z^q and take q-th roots to prove equality.
Consequently each m_i yields exactly one analytic point, with finite
completed residue field. Every analytic point has prime kernel, so there
are no other points. This proves the claimed rigid finiteness.

**Application boundary.** This repairs the strict zero-dimensional fibres
and rigid exceptional sets used in C2, T12.5, and the optional local-image
argument. It supplies no current transport, harmonic comparison, or
semistable reduction theorem.

## B. Berkovich's actual local statements and what they supply

The complete cached primary body of Berkovich (1993), §§1.6 and 3.1.1–5,
is embedded in Appendix S. Physical page 33 (printed 36) was also rendered
and read. The relevant domain assertion is **Lemma 1.6.2(i)**: an open
affinoid domain in the rigid space X_0 associated to a Hausdorff strict
analytic X is V_0 for a strict Berkovich affinoid domain V in X. Here
"open" is a rigid domain, not an ordinary Berkovich topological open.
Theorem 1.6.1 supplies full faithfulness for Hausdorff strict spaces. Its
paracompact category-equivalence clause is unnecessary for one affinoid
embedding in a smooth proper algebraic curve.

For the actual application to van der Put, take K complete, algebraically
closed, and nontrivially valued; take a connected normal strict affinoid Q.
Van der Put 1.1 provides a rigid affinoid-domain embedding into a nonsingular
complete algebraic curve C. C^an is Hausdorff and strict. Lemma 1.6.2(i)
gives an actual strict affinoid domain V⊂C^an with that rigid domain.
The rigid isomorphism Q_0≅V_0 comes from a Berkovich analytic isomorphism
Q≅V by the fully faithful part of 1.6.1. Thus the assertion is an
affinoid-domain isomorphism with the actual analytic algebra, rather than
an identification of rigid points alone. On affinoid subcharts both maps
come from the same bounded maps of Tate quotients; their composites are
the identity maps of those algebras. Restriction compatibility follows from
the universal property of a domain and gluing on intersections.

One should not justify injectivity by the abstract sentence "compact and
injective on a dense subset implies a homeomorphism onto the image."
That sentence is false for general compact spaces. In this separated
application the local domain argument is the needed additional fact:
cover Q by finitely many affinoid domains Q_i mapping isomorphically onto
domains V_i in affinoid domains of C^an, as in Berkovich's proof. On an
overlap V_i∩V_j, the rigid preimages are Q_{i,0}∩Q_{j,0}, because the
given rigid embedding is a domain immersion. Intersections of affinoid
domains in this separated target are affinoid. Their bounded algebra maps
and inverse domain restrictions identify the corresponding Berkovich
preimages, so coincident points from Q_i and Q_j are already the same
point of Q. This is domain compatibility, not a consequence of density
alone. The cited rigid domain calculus remains standard analytic background
in this application; a general new category-equivalence proof is not claimed.

The remaining ordinary-open step is distinct. If Int denotes absolute
analytic interior, relative interiors compose with equality when the
intermediate target is locally separated; for a domain embedding its
relative interior is its ordinary interior. These are the exact standard
boundary statements in GR 2.11(3),(4) (Berkovich 1990, Proposition 3.1.3).
Since the two ambient curves are separated and boundaryless, they identify
int_X Q with Int(Q), and int_{C^an} V with Int(V). An analytic isomorphism
preserves the intrinsic Int, hence identifies ordinary neighbourhoods.
This check uses neither a universal moment-dimension equality nor a
scalar-current pullback. A source quotation of 1.6.2 alone does not prove
this separate boundary step.

The actual finite-at-a-point source is Definition 3.1.1, Lemma 3.1.2,
Proposition 3.1.4, and Lemma 3.1.5. For **good** source and target,
3.1.4 says: finiteness at y, arbitrarily small finite affinoid
neighbourhoods of y and f(y), and "y isolated in its fibre and in the
relative interior" are equivalent. The proof uses the admissible relative
Tate presentation with strict bounds on its generators, shrinks the target
so these bounds hold on the full inverse image, and finally invokes
Berkovich (1990), 2.5.13 to conclude finiteness. Merely reproducing
§3.1.4 does not establish that last invocation. The following direct
argument replaces it in the exact strict-generator situation used there.
It does not prove optional P0, which also needs current restriction and R0.

**Lemma B2 (contracted presentation).** Let A,B be complete non-Archimedean
Banach K-algebras, with ultrametric submultiplicative norms, and let
q:A⟨r_1^{-1}T_1,...,r_m^{-1}T_m⟩→B be an admissible bounded surjection.
Admissible means the norm of B is equivalent to the quotient norm, hence
there is C>0 such that every b has a lift F with ||F||≤C||b||.
Let b_i=q(T_i). If the spectral radii ρ_B(b_i)<r_i for all i, then B
is a finite A-module. No reducedness or perfectness is assumed.

Proof. Choose ρ_B(b_i)<s_i<r_i. The spectral radius is the infimum of
||b_i^n||^{1/n} (CLD 11.1.1); choose N_i with
||b_i^{N_i}||<s_i^{N_i}. Dividing an exponent by N_i and using
submultiplicativity gives constants C_i such that
||b_i^j||≤C_i s_i^j for all j≥0. Put t=max_i(s_i/r_i)<1 and
C_0=∏C_i. If D bounds the structural map A→B, the image of the
part of F=Σa_νT^ν with |ν|≥N has norm at most
D C_0 t^N||F||. All such infinite sums converge; the coefficient
condition in the relative Tate algebra and boundedness of q justify
termwise application. Choose N with η=D C_0 C t^N<1.

Given b, lift it to F as above and retain only the finitely many
monomials of total degree <N. Their image differs from b by a
remainder b_1 of norm ≤η||b||. Repeat for b_1, obtaining b_j
with ||b_j||≤η^j||b||. For each of those finitely many monomials,
its coefficients in successive lifts have norm bounded by
Cη^j||b||r^{-ν}, hence their sums converge in A. Summing the
finite polynomial images and letting the remainders tend to zero
expresses b as an A-linear combination of {b^ν:|ν|<N}. The resulting
coefficients satisfy max_ν ||a_ν||r^ν≤C||b||. Conversely the finite
sum map A^{#\{ν:|ν|<N\}}→B is bounded. These two inequalities show
that the finite-module quotient norm is equivalent to the given norm
of B: this is also finiteness as a Banach A-algebra, not just algebraic
finiteness. For m=0 the given surjection is A→B and
the assertion is immediate. No compact-operator theorem is imported.

Here is its precise application to the source proof. The relative interior
characterization in Berkovich 3.1.4 gives an admissible relative Tate
presentation on good affinoid neighbourhoods, with |b_i(y)|<r_i.
If y is isolated in its fibre, shrink the source affinoid neighbourhood
V to have no other point over x=f(y). The set in V where at least one
|b_i|≥r_i is compact; its image is compact in the Hausdorff target
affinoid and misses x. Choose a target affinoid neighbourhood U' of x
outside that image. The inverse image V' inside V is affinoid by
completed-tensor base change, and the base-changed presentation remains
an admissible surjection. All its points satisfy the strict bounds.
Compactness gives sup_{z∈V'}|b_i(z)|<r_i. The spectral radius identity
ρ(b_i)=sup_{z∈M(B')}|b_i(z)| in CLD 11.1.1 verifies every hypothesis
of B2. Thus V'→U' is finite. No reduction has removed nilpotents.
Starting with smaller neighbourhoods gives the small affinoid versions.
Lemma 3.1.5 and the stated composition law for relative interiors then
give the finite maps of ordinary neighbourhoods, exactly as in the
primary body. This replaces the nested finiteness step, while retaining
the standard relative-interior characterization and affinoid tensor
calculus that actually enter the proof.

## D. Correct pure-curve carrier for a finite fibre product

**Lemma D.** Let K be complete and nontrivially valued. Let Z be a good
separated strict pure one-dimensional K-analytic space with no isolated
points (automatic in this scope, as checked below), and let p:W→Z be
finite and surjective.
Let W^(1) be the reduced closed subspace whose carrier is the union of the
one-dimensional irreducible components of W. Then W^(1)→Z is finite and
surjective, and W^(1) is pure one-dimensional. W itself can have isolated
zero-dimensional components. Smooth connected strict curve probes satisfy
the hypotheses on Z. This is a carrier lemma, not finite-surjective descent
of GR subharmonicity.

Here we use the following standard finite affinoid facts with their exact
roles: finite maps to an affinoid are maps of finite affinoid algebras
(CLD 11.4.4); their underlying maps are closed and have compact affinoid
inverse images; strict affinoid dimension is Krull dimension and domain
restriction preserves local analytic dimension (CLD 11.2.3); finite
integral extensions preserve dimension on irreducible closed images.
The latter algebraic assertion follows from lying over, going up, and
incomparability. These are not assertions of flatness. For an integral
domain finite over a domain, invert nonzero elements of the base: the
result is finite integral over a field, hence a field, proving
incomparability; lying over after quotient and localization and going up
lift prime chains. This proves equality of the dimensions in use.

Proof. Work over a strict affinoid neighbourhood V of z. W_V is a strict
affinoid with finitely many irreducible components. Each component is
finite over its closed image in V, so has dimension ≤1. Dimension-zero
components have finite rigid carriers by A. The union of the
dimension-one components with reduced structure is a closed affinoid
subspace, defined by the intersection of their prime ideals; thus its map
to V is finite. These subspaces agree under domain restriction: local
dimension on each irreducible component is preserved on analytic domains,
so a one-dimensional component cannot turn into a zero-dimensional domain
component. They glue to the indicated closed subspace W^(1).

Let F⊂V be the image of the zero-dimensional components of W_V. It is
a finite set of rigid points. Outside F every fibre, being nonempty,
contains a point on a one-dimensional component. Therefore
p(W^(1)_V) contains V\F. It is closed, because it is the image of a
finite morphism. The complement of a finite set is dense in a curve
with no isolated points. Explicitly, if a nonempty open were contained
in a finite set in a Hausdorff curve, one could separate its finitely
many points and obtain an open singleton, contradicting that hypothesis.
Consequently p(W^(1)_V)=V. Affinoid neighbourhoods cover Z, proving
surjectivity. Its components all have dimension one, proving purity.

For a good strict pure curve over a nontrivially valued field, no isolated
point can occur. If {z} were ordinary open, a strict affinoid neighbourhood
inside it exists (CLD 11.7.7). Its spectrum is a singleton. Spectral
surjectivity to Spec A (11.1.2) would force Spec A to have just one prime,
so its Krull dimension would be zero. This contradicts strict affinoid
dimension and preservation of local dimension on ordinary opens (11.2.3).
Strictness matters here: a non-strict affinoid field can have a singleton
carrier of positive dimension relative to K. In the particular fibre
product W=Z×_{X_L}Y_L arising in
GR 3.5(8), the projection to the smooth strict probe Z is finite and
surjective by base change. One must restrict the second projection to
W^(1), and apply curve-test subharmonicity only to that pure curve.
Its finite image covers Z by the lemma. The subsequent source route would
use normalization over a perfect field and GR Lemma 3.9; proving its smooth
comparison still requires harmonic pullback. None of these further steps
is a premise of the carrier lemma just proved.
For finite-valued functions, there is no identically -∞ component
alternative to manage. This fixes the dimension error without calling
the original W a curve.

The diagnostic example is exact. With A=K⟨x,y⟩/(xy), its normalization
has algebra B=K⟨u⟩×K⟨v⟩, with (x,y)=(u,0) and (0,v). Pull back along
the x-branch D=K⟨t⟩, x↦t,y↦0. The two factors of the finite completed
tensor product are

    K⟨u,t⟩/(u-t) ≅ K⟨t⟩,
    K⟨v,t⟩/(t,v) ≅ K.

Thus B⊗̂_A D≅D×K: a line and an isolated point. Taking its reduced
pure one-dimensional carrier keeps the line, whose finite image is all
of the probe. The isolated point is not an extra pure curve component.

## E. Honest open-edge smoothing and the zero-error case

In this paragraph "smooth psh" means ordinary smooth with nonnegative
ordinary CLD Hessian current, not classical curve-test psh. The standard
Stokes identity on a boundaryless annulus makes its canonical integration
current δ d'- and d''-closed. The smooth Leibniz rule therefore gives
d'd''[w]=d'd''w∧δ. Positive smooth Hessian forms give positive currents.
These are the precise smooth-calculus facts used here (CLD 7.7.7–9;
their statements and proof bodies are in Appendix S). They do not assert
regularization of a nonsmooth current.

**Lemma E (local collar repair).** Suppose an actual open annulus has
logarithmic coordinate t with image (a,d), a<d. Let a<b<c<d and let
ℓ(t) be affine. On this annulus suppose the two ordinary smooth psh
functions u_k^± are ℓ(t)+α_k^±, where
0≤α_k^-≤α_k^+≤δ_k and δ_k→0. Given any fixed strictly positive
ε, one can choose an affine ψ(t), trim neither collar end to a
skeletal vertex, and for all sufficiently large k construct ordinary
smooth psh w_k^± such that they equal u_k^± on a left end neighbourhood
and both equal ψ on a right end neighbourhood. Their difference is
nonnegative, glues to the original difference on the left and zero on
the right, and tends uniformly to zero on the collar. This lemma needs
only the stated annulus and affine identities. It does not supply
semistable charts or formal models.

Construction and proof. Take t_0∈(b,c) and M>0 such that
M(t_0-b)>3ε and M(c-t_0)>3ε. Put ψ=ℓ+M(t-t_0).
Choose a nonnegative even smooth mollifier ρ of integral one, supported
in (-1,1), and θ_ε=|·|*ρ_ε. It is convex, smooth, 1-Lipschitz,
equals |s| for |s|≥ε, and satisfies |s|≤θ_ε(s)≤|s|+ε.
The lower bound is Jensen's inequality; the upper bound is the triangle
inequality; exact equality off the transition follows from the zero first
moment of the even kernel. Define

    m_ε(A,B)=(A+B+θ_ε(A-B))/2,
    w_k^±=m_ε(u_k^±,ψ).

This smooth maximum is convex and nondecreasing in each variable, since
its partial derivatives are (1±θ_ε')/2∈[0,1]. On the annulus t is
the logarithm of an analytic unit and has zero ordinary Hessian as a form.
Both inputs are affine in t; their composition by m_ε has a nonnegative
second derivative in t. Thus w_k^± are ordinary smooth psh on this
actual annulus. For δ_k<ε, u_k^±-ψ>3ε on (a,b), whereas
ψ-u_k^±>2ε on (c,d). Exactness of m_ε gives the asserted left
and right identities on open neighbourhoods. There is consequently no
boundary derivative or mismatch when gluing at those ends.

Monotonicity gives w_k^+≥w_k^-. The bound on the first partial
derivative gives

    |m_ε(ℓ+α,ψ)-m_ε(ℓ,ψ)|≤|α|,

so each w_k^± differs uniformly by at most δ_k from the same
function m_ε(ℓ,ψ); in particular their difference tends uniformly to
zero. No tolerance is defined as a possibly zero approximation error.
If δ_k is identically zero, the same fixed ε>0 and the same ψ work:
the two smoothed functions coincide, and their difference is exactly
zero. A finite number of disjoint outward collars permits one common
lower bound on k and honest gluing. Trim the ambient open set before
the far ends, still strictly inside the open edges. The support of the
glued difference then lies in one compact set independent of k; choose
the trimming so its closure lies in the original ordinary open.

There is a second check needed in Wanner's application: an identity of
norms merely on the skeleton is not automatically an identity on all
of its inverse image. On a given open annulus, it can be checked directly.
An analytic function f has a convergent Laurent expansion Σa_nT^n.
If its Gauss logarithmic norm is finite and affine on an open interval,
exactly one exponent n_0 can attain the maximum at any interior radius.
Indeed each term gives an affine line log|a_n|+n log r below that
affine norm function; a line touching it in the interior must have the
same slope, since otherwise it exceeds it on one side. The maximum is
attained because Laurent coefficients decay on every compact subannulus.
Distinct exponents cannot have the same slope. Thus
|f(z)|=|a_{n_0}||T(z)|^{n_0} at every analytic point in that interval:
the unique largest term cannot cancel. It has no zeros there and is a
unit on compact subannuli. This proves the needed fibrewise norm identity,
without applying a slope theorem outside its stated field scope.

For finitely many projective-coordinate ratios, choose a compact interval
strictly inside an edge where all nonzero Gauss norms are affine and the
sets of maximizing ratios are constant. The preceding Laurent argument
extends those affine identities to the entire annulus. Nonmaximizing
ratios have a strictly positive minimum gap from the maximum on the chosen
compact interval; identically zero ratios are omitted. Wanner's smooth
maximum deletion rule eliminates those ratios for all large k. Translation
equivariance leaves ℓ(t)+a constant in [0,1/k]. Adding 1/k to the
positive approximant gives the ordering in Lemma E and δ_k≤2/k.
The local correction therefore treats the actual functions, not only
their skeletal restrictions, whenever the stated open-edge chart and
affine coordinate data have been established.

The erroneous chart in Wanner 4.7, Step 3 is the assertion that
τ^{-1}([y,x_e]) is a closed annulus even when it includes a skeletal
vertex y. If y has positive residual genus, this cannot hold: endpoint
residue function fields of a standard annulus have genus zero. The
construction above only uses τ^{-1}((a,d)) for a segment compactly
inside the open edge. It leaves the original functions near y and trims
the far side before reaching another vertex. Their exact left and right
agreement proves the required gluing. This is a local repair of Steps
3–5; Steps 0–2 and their model/comparison dependencies remain separate.

## F. Exact remaining proof obligations for R0

The following are gaps in this submission, not counterexamples to R0.
Access to a source, successful extraction, and old PASS reports do not
settle any of them. They also must not be converted into conditional
hypotheses and then counted as the requested unconditional theorem.

1. **Thuillier semistable existence and model realization.** His exact
   Theorem 2.3.8 asserts that a pure one-dimensional rig-smooth strict
   affinoid over a complete nontrivially valued k admits a simply
   semistable formal model after a finite separable extension. Its proof
   first algebraizes after a finite separable extension, citing [31],
   theorem 1; then invokes [9], Bosch–Lütkebohmert, *Stable reduction
   and uniformization of abelian varieties I*, Math. Ann. 270 (1985),
   349–379; then invokes Lemma 2.2.22 to include its boundary in the
   model's vertex set and realizes the affinoid as a formal open generic
   fibre. All those are actual steps, not consequences of merely having
   a finite graph. Van der Put [31] explicitly assumes algebraically
   closed k throughout his cached paper. His 1.1 closes the algebraically
   closed embedding application in B, but its printed statement and proof
   do not by themselves prove the arbitrary-field finite-separable
   algebraization step. That extension requires a separate descent or
   algebraization argument. No such argument is supplied here. The BL85
   proof and the required model-realization argument were not reconstructed.
   No full BL85 proof was identified in the named permitted source caches.
   This is a precise remaining gate, not an assertion
   that the thesis or the theorem is false.

2. **Dirichlet and full harmonic functoriality.** Lemma 2.3.9 deduces
   arbitrary Shilov-boundary interpolation from 2.3.8, the semistable
   graph Dirichlet problem in 2.3.2, and Galois descent of boundary data.
   Its boundary superscript G must mean the orbit boundary for data,
   not just pointwise fixed points: invariant functions on a finite
   boundary set are functions on its orbit set. Propositions 2.3.18–19
   use Lemma 2.3.5, Proposition 2.3.3, model domination 2.2.26, and
   the pointwise weighted degree identity 2.2.27. The latter requires
   actual semistable-model extension of quasi-finite maps and residual
   curve degrees, not just the global sum of edge weights after scalar
   extension. These bodies are available and relevant portions appear
   in Appendix S, but their complete upstream model existence and
   domination chain has not been proved here. Omitting GJR does not
   remove these Thuillier dependencies. They are needed for GR descent
   with *all* analytic-extension and smooth-curve-test quantifiers.

3. **Wanner's remaining nonlocal chain.** Lemma E repairs its annulus
   smoothing and zero-error localizations. Her Theorem 4.7 still uses
   Lemma 4.6's compact positive model test, the equivalence between
   piecewise rational-linear metrics and formal metrics cited from
   GK14 8.11/8.13, semistable domination and formal-open realization
   (BL93 Lemma 4.4), decomposition into very ample model line bundles,
   and the model/Laplacian/Monge–Ampère comparison in Theorem 3.28.
   We do not use those as unproved grants. The local smoothing repair
   alone does not establish Wanner's theorem or intrinsic recognition.

4. **Ordinary-current transport, calibration, and polyhedrality.**
   The predecessor's T8 uses a common finite polyhedral moment carrier
   and its canonical calibration to obtain total variation of a
   differentiated approximation; T10 uses scalar measure transport
   without a degree factor, separately from same-carrier field
   restriction with a full degree factor. Both are necessary for
   arbitrary finite/separable ascent, and T12 needs exact finite-stage
   test descent on actual domains. No theorem T is imported here.
   The exact underlying Ducros 3.2 is: for compact Γ-strict X of
   dimension d and analytic units f_i, the norm image is a
   (Q,(|K^×|Γ)^Q)-polytope of dimension ≤d; the boundary image is
   contained in such a polytope of dimension ≤d-1, and is itself one
   in the affinoid case. The standing condition is
   Γ·|K^×|≠{1}. Its proof 3.2.1–3 uses Gerritzen–Grauert,
   algebraic local models, definability/quantifier elimination in
   Theorem 1.2, and Temkin germ reductions in Lemma 3.1. For our strict
   compact curve charts Γ={1}, nontrivial K verifies the condition,
   d=1 gives only an upper bound, and constants give dimension zero.
   This is the exact application, not the false assertion that every
   moment image has the source dimension. The full nested model-theory
   proof and its use in all canonical carrier estimates have not been
   reconstructed in this submission. The original source body and
   its immediate dependencies are exposed in Appendix S.

5. **Boundary uses.** Boundarylessness survives analytic base change by
   the interior inclusion Int(Y_L/X_L)⊇π^{-1}Int(Y/X). This is distinct
   from the converse boundaryless descent in Conrad–Temkin 11.5 and
   the equality π(∂V_L)=∂V. In the harmonic-majorant comparison step,
   the weaker inclusion π(∂V_L)⊆∂V is enough: it gives the boundary
   inequality upstairs; scalar surjectivity gives the inequality
   downstairs. The stronger equality used in the predecessor is
   unnecessary for that particular step. It does not eliminate the
   separate scalar functoriality of harmonic majorants in item 2.
   The cached proof of Conrad–Temkin 11.5 expressly uses graded
   general-position lifts (11.1), properness of germ reductions via
   Temkin 5.2, and proper descent in their Lemma 7.2. Those nested
   claims are not certified by just quoting 11.5. We impose no new
   boundary assumption to bypass them.

The GJR/GM flattening, line-bundle extension and weighted-slope chains
identified in audit premises 13–17,20,23,25 are omitted as output routes.
There is no deduction of an arbitrary-field weighted slope formula from
KRZB 2.6: that theorem has algebraically closed, smooth proper,
split-semistable and nonpoint-skeleton hypotheses. Even after omitting
GJR, items 1–5 above are still relevant to R0. Accordingly the current
status is incomplete, not "proved modulo source authentication."

## Reproducibility and disposition

Run `python3 prepare.py` in this workspace to rebuild the authoritative
P06.2-argument.md, exact five-key status.json, source manifest, newline-only
body bindings and environment evidence. It uses cached sources read-only
and makes no network, model, database or predecessor writes. The independent
lemmas are in this core; the appended bodies expose the sources and the
unresolved chains. The build checks check extraction and artifact structure,
not mathematical correctness. The PDF page render commands and their exit
codes are recorded in evidence/commands.json; known Type-3 font warnings
are retained in the render logs. The printed 53/54 transcript was checked
visually against the actual cached PDF pages 67/68.

There is no P06.2-partial.tex or paper PDF: no unconditional substantial
recognition theorem was established, so the assignment's diagnostic route
is used. No supervised heavy compute was needed or launched. Final native
notes are n1, n2, n3, n4 and n5; earlier campaign notes are not used as theorem
supports. The exact original residual scope remains open, and candidate=false.
