# A graded primary family with vanishing energy and a non-psh pointwise supremum

This is an ENTIRE UNREVIEWED working proof, not a solved-original paper or an acceptance. It is independent of the ACTIVE254/255 frozen outputs, which have not been read or supplied. It uses only the ENTIRE qualified G331 geometric cone comparison and the ENTIRE qualified G345/E350 actual bounded product, symmetric form, energy and capacity theorems, with all mandatory source and scope qualifications. These are mathematical prerequisites, not a definition of positivity by ideal formulas. The new exact monomial counts and counterexample below are proved directly. Source bodies/pixels stay LOCALONLY and the protected P16.4 editor stays open unchanged.

## 1. The actual full boundary and graded family

Let k be any field and R=k[x,y]_(x,y), m=(x,y). This is an excellent normal regular surface. Let X be the FULL compact Hausdorff section of centered semivaluations v(m)=1, including every nonminimal prime support strictly below m. Thus min(v(x),v(y))=1 and extended values infinity are permitted. Set J_0=R and

    J_j=(x,y^j),       j>=1.

Every J_j is a proper m-primary ideal. Its products satisfy J_j J_l subset J_(j+l): x^2 and both cross products lie in (x), and y^(j+l) is the remaining product. Hence this is a genuine graded family, not a list with a merely pointwise asymptotic slogan. Moreover m^j subset J_j, so the family has a uniform linear primary lower bound.

By the substantive G331 comparison the functions

    u_j(v)=-(1/j)v(J_j)=-min(v(x)/j,v(y))             (1)

are actual independently geometric C functions. Because min(v(x),v(y))=1, their values lie in [-1,-1/j]. They INCREASE pointwise with j. This does not define a decreasing completion.

Let Z={v in X:v(x)=infinity}. It is closed. The quotient R/(x)=k[y]_(y) is a DVR, so Z consists of its single normalized order w_infinity, with w_infinity(x)=infinity and w_infinity(y)=1. Formula (1) gives the exact whole-boundary limit

    h=sup_j u_j = -1 on Z, and 0 on X minus Z.      (2)

In particular the limit is zero at EVERY normalized centered real valuation of Frac(R) lying in X and at every normalized divisorial valuation, but has a different value at the retained nonminimal support (x). Neither density of real/divisorial valuations nor a coefficientwise generic limit determines this raw pointwise function.

## 2. The limit fails geometric positivity on the normal smooth surface

For a finite positive M>=1 let w_M be the monomial valuation with w_M(x)=M and w_M(y)=1. It has support zero and lies in X. If a polynomial f has nonzero restriction f(0,y), then for all sufficiently large M its monomial minimum is exactly ord_y f(0,y); every term with positive x exponent eventually has larger weight. If f is divisible by x, its value tends to infinity. Denominators in this local ring are units and have value zero. Therefore w_M->w_infinity in the full pointwise semivaluation topology.

At all w_M the limit h is zero, while h(w_infinity)=-1. Thus

    h(w_infinity)=-1 < limsup_M h(w_M)=0.

It is not upper semicontinuous. Every element of D is upper semicontinuous, since it is an actual infimum of continuous C functions. Consequently h is not in D, even though every u_j is a bounded continuous geometric psh potential. Its USC regularization is exactly zero: off Z the function is already zero; at the sole point of Z the preceding approaching monomial valuations force the limsup to be zero. Zero belongs to C.

This does NOT furnish a counterexample to the full continuous-obstacle envelope on this smooth space. It is the supremum of the specified graded family, not of every competitor below an independently fixed continuous obstacle. For the obstacle zero the full envelope is zero, since zero itself is admissible. The example instead disproves arbitrary increasing-family closure and any inference that gradedness plus linear primary bounds makes the raw pointwise supremum positive.

## 3. Exact mixed multiplicity counts, without a numerical test

For integers r,s>=0, the monomial ideal m^r J_j^s has the following staircase. At x exponent i with 0<=i<s, its least y exponent is r+j(s-i): allocating x factors to J_j first is optimal because doing so saves j y factors, while allocating an x to m saves only one. At s<=i<r+s the least y exponent is r+s-i. At i>=r+s the least y exponent is zero. This assertion also follows directly by distributing i among the s choices of x versus y^j and the r choices of x versus y in the generators of the product.

The monomials below those thresholds give a basis of the finite quotient, after localization as well as before it. Therefore for ALL r,s>=0

    length_R R/(m^r J_j^s)
       = r(r+1)/2 + r s + j s(s+1)/2.              (3)

The degree-two part is r^2/2+r s+j s^2/2. Reading the proved mixed Hilbert-polynomial convention gives

    e(m)=1,     e(m,J_j)=1,     e(J_j)=j.          (4)

This is a universal monomial-basis proof, not an extrapolation from finite arithmetic samples. In particular it needs no incorrect unquotiented-colon application of printed SH17.4.7. The accepted G345/E350 identification of genuine geometric products with the mixed forms is used only AFTER their independent supported-Cartier positivity and model comparison.

## 4. Raw products and energy vanish, yet the pointwise limit is still wrong

In dimension two G345's bounded product has one potential slot; write mu(u) for its raw geometric Radon measure. The primary reference constant -1 is -v(m), and its mass is e(m)=1. The complete qualified moment comparison and (4) imply

    mu(u_j)(X)=e(m,J_j)/j=1/j,
    - integral_X u_j d mu(u_j)=e(J_j)/j^2=1/j.      (5)

Thus the positive raw measures mu(u_j) converge in total variation to zero, and in particular weakly. No probability normalization is applied. E350's fixed reference energy in this dimension is

    E(u)=-F(u,u)/2,
    F(u,v)=integral_X u d mu(v),

so (5) gives E(u_j)=1/(2j)->0. All these bounded potentials are in the proven finite-energy class. The comparison to zero uses the SAME reference and actual arity; no generic nilpotent multiplicity or different carrier is present.

The function h in (2) remains outside D. Therefore small energy and even total-variation convergence of products cannot manufacture a D member from an arbitrary pointwise limit. In particular E350's decreasing/net stability assertions have a specified D-limit hypothesis; the example shows why a class membership premise cannot be erased. This increasing family is not one of those authorized decreasing approximations.

## 5. Quantitative capacity convergence and the polar exceptional point

Use E350's actual Borel capacity on this surface:

    Cap(E)=sup{mu(g)(E): g in bounded D, -1<=g<=0}.

Let B(u,v)=-F(u,v) on these nonpositive potentials. The entire qualified E350 symmetric-form Cauchy--Schwarz theorem gives

    0<=B(u_j,g)<=sqrt(B(u_j,u_j) B(g,g)).

By energy monotonicity at the stated bounded D hypotheses and -1<=g<=0, B(g,g)<=B(-1,-1)=e(m)=1. Formula (5) therefore gives B(u_j,g)<=1/sqrt(j). Markov's inequality, applied to the nonnegative integrable test -u_j against the genuine positive measure mu(g), yields for epsilon>0

    mu(g){u_j<-epsilon}
       <= (1/epsilon) integral_X (-u_j) d mu(g)
       <= 1/(epsilon sqrt(j)).

Take the supremum over EVERY admissible g to obtain

    Cap{u_j<-epsilon} <= 1/(epsilon sqrt(j)) -> 0.  (6)

Hence u_j converges to zero in the proved capacity, even though its whole-boundary pointwise limit is h instead of zero. For 0<epsilon<1 the point Z belongs to {u_j<-epsilon} for EVERY j, so monotonicity and (6) give Cap(Z)=0. This conclusion uses neither continuity from above for capacity nor a Choquet assertion: the uniform upper bound holds at every j.

The counterexample therefore changes only a zero-capacity closed locus. It does not permit changing the actual geometric class at that locus: D functions are genuine full-boundary functions with USC and positive comparison constraints. It proves the distinction between capacity convergence and exact pointwise class membership, rather than identifying arbitrary representatives modulo polar sets with D.

## 6. What the related source text does and does not establish

An exploratory reading of the PRIVATE immutable BdFFU preprint text LF1--260 and LF260--332/335--481 was made alongside this argument; LF325--355 was then freshly read to include the skipped definition preamble. That source works over C and its Val_X consists of real valuations on the FUNCTION FIELD. The read immediate text units are2.1--2.5,2.6 and3.1--3.4 with the3.1 proof; later multiplier/subadditivity units are not claimed read or applied. In particular its graded-family function on those real valuations does not define a canonical function at the nonminimal infinite support in (2). Uniform convergence on compact bounded-discrepancy subsets is not uniform convergence on the FULL semivaluation section.

There are literal orientation discrepancies in the bound TEXT that require independent checking before a new application:2.4(b) prints r_pi(v)(a)>=v(a), while the local monomial computation later in its proof says v(f)>=v_w(f), which gives the reverse inequality for actual ideal values. Its2.4 proof also calls a minimum of affine functions convex although the statement calls it concave, and its2.5 closed-face argument says lsc although an infimum of continuous graded ideal values is USC. This records what the local text says; it makes no fresh PDF-pixel assertion or claim of an official erratum. The source file has not been altered.

For the present example the correct inequalities and regularity are computed directly from (1), so no inconsistent printed orientation is imported. On a fixed finite simplex of generic monomial valuations all v(x) are finite and the limiting value v(J_bullet) is zero. A finite-simplex or bounded-discrepancy argument consequently does not resolve the infinite-support point. The exact full-support approximation step remains necessary in any new normal-envelope proof.

## 7. Scope and future independent review

This manuscript provides a complete graded-primary, geometric, full-support counterexample to three unwarranted implications: increasing raw suprema automatically belong to D; generic/divisorial coefficient limits determine raw support values; and vanishing energy/capacity/products alone yields positivity of an unspecified pointwise limit. It does not refute the correct E350 approximation theorems, the smooth BFJ continuous-envelope property, or the finite-good-cover theorem proposed in ROOT353. Original P12.3 is still OPEN; P12.5 remains accepted at its existing exact scope and its count is unchanged.

All primary-gauge computations here use m. Other primary gauges transport the potentials and bad limit through the G331 degree-one positive continuous cocycle; USC failure survives such a homeomorphism and positive scalar. No unscaled-obstacle identity, new normalized mass, or nonprimary compact section is claimed. This argument launches no supplied program, compiler, agent, native job, heavy computation or external message. It is held for a future entire independent proof/source/scope review and is not fed into ACTIVE254/255.
