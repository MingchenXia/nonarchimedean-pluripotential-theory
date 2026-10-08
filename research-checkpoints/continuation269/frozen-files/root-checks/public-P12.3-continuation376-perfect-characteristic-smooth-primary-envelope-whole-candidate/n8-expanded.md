# n8. Positive-characteristic envelopes on a fixed ACTUAL smooth primary model

Use qualified G331 and n1. Let k be PERFECT of characteristic p>0, B a normal integral affine finite-type k-algebra, x a CLOSED point of codimension n>=2, and a a proper x-primary gauge. Assume an ACTUAL primary blowup Y=Bl_J Spec(B) is smooth over k, is an isomorphism off x, and principalizes a, where J is x-primary. Put A=J O_Y=O_Y(-F_J), an ample globally generated line bundle over this affine base; H=-F_J is its additive Cartier divisor. Fix an integral fibre-supported Cartier divisor C, without a sign assumption. Its all-support evaluation is denoted f_C. No assertion that such a smooth primary model universally exists is made.

Every semivaluation is evaluated by FIRST passing to Frac(B/support(v)) and its valuation ring. The generic point lies away from x because a support is strictly below the marked maximal ideal, and the model is the identity there. Properness gives a centre on Y. The generically trivial invertible lattice O(C) has a nonzero local generator on that quotient field; set its value to be minus the value of the generator. Cartier order bounds by the principalized primary divisor give finite bounds on all evaluations. G331's all-support model continuity applies. This procedure does not pretend Frac(B) maps to a nonminimal-support quotient field.

For every m>=1 let I_m=Gamma(Y,O(mC)). Proper coherence makes it a finite B-module. Since C is supported over x and codim(x)>=2, its sections are regular at every codimension-one point of normal B. Normal Hartogs therefore places them in B: I_m is an actual ideal. It is unit off x, by localization. A fixed actual Cartier bound C>=-M E_a gives a^(Mm) subset I_m for some integral M. Thus I_m is nonzero and unit or x-primary. The section ideals are graded, I_m I_l subset I_(m+l). Individual coherence does not imply graded finite generation.

On a primary section v(I_m) is finite, nonnegative and subadditive in m. ALL-index Fekete gives

s(v)=lim_(m->infinity)(-v(I_m)/m)=sup_m(-v(I_m)/m).

Global sections of O(mC) give -v(I_m)/m<=f_C at every quotient-support centre, so these actual C profiles are competitors. Conversely any rational primary profile -v(L)/r<=f_C forces ord_E(L)>=-r coeff_E(C) at every fibre prime divisor of NORMAL Y. At all other prime divisors C has coefficient zero and L is regular. The height-one criterion for an invertible fractional ideal on a normal scheme implies L O_Y subset O(rC), hence L subset I_r. Its profile is <=-v(I_r)/r<=s. For an arbitrary C competitor, rational profile density with a small negative rational shift gives the same domination in the limit; n1's raw C/D equality then yields

p(f_C)=s on the ENTIRE section.

This Fekete calculation alone establishes no geometric positivity of the supremum. The next uniform bound does.

On smooth Y let b_m=I_m O_Y tensor O_Y(-mC). This is an ACTUAL coherent ideal, the base ideal of the complete section family of mC, and it is graded and unit off the fibre. Define t_m=tau(b_bullet^m), the asymptotic test ideal. The complete GJKM arXiv:1712.00980v3 Section 4, 4.1–4.6 and its immediate proof, together with the complete Mustata Section 3, gives

b_m subset tau(b_m) subset t_m, and t_(ml) subset t_m^l.

These ideals are coherent on smooth integral Y over perfect k. Their foundations include BMS subadditivity and Frobenius trace; they are published dependencies, not a recursively new certification.

Apply GJKM 4.6 with D=C, E=mC, lambda=m and d=n+1. Nonzero I_r supplies a nonzero section of rC. H=-F_J is AMPLE and globally generated, while E-lambda D=0 is nef. Y is projective over finite-type affine B and smooth over PERFECT k, exactly the theorem's scope. It gives O(K_Y+mC+dH)t_m globally generated for EVERY m. The canonical divisor is ON Y; no Cartier hypothesis on K_B is imposed.

By ordinary Serre generation choose ONE fixed integer c>=0 such that A^c tensor O(-K_Y-dH) is globally generated. Tensor the two generated sheaves. Then

F_m=O(mC)t_m A^c

is globally generated for ALL m. Its sections J_m=Gamma(Y,F_m) lie in B by the same normal codimension-two argument, since F_m is a subsheaf of O(mC) and is trivial off x. They form a coherent actual ideal. The inclusion b_m subset t_m gives F_m containing I_m O_Y A^c; products of sections therefore give I_m J^c subset J_m. A primary power is contained, so J_m is unit or x-primary. Global generation gives the ACTUAL fractional-ideal equality

J_m O_Y=O(mC)t_m A^c.

This equality is not merely numerical or a comparison of divisorial coefficients. Pull it to each support quotient valuation ring. Since b_m is unit on the generic puncture and has finite value there, and t_m contains b_m, its local ideal value is finite. A finite global generating set has a unit coefficient at the valued centre, so

g_m(v)=-v(J_m)/m=f_C(v)-(c/m)v(J)-(1/m)v(t_m).

All signs follow from A=O(-F_J) and f_C=-v(local generator of O(C)). The last two terms are nonnegative losses. Thus g_m belongs to the ACTUAL C class and lies below f_C on ALL supports.

Fix m and l>=1. The inclusions b_(ml) subset t_(ml) subset t_m^l give

-v(I_(ml))/(ml)=f_C-v(b_(ml))/(ml)<=f_C-v(t_m)/m=g_m+(c/m)v(J).

The all-index Fekete limit has the SAME limit along the multiples ml, so passage l->infinity yields p(f_C)<=g_m+c v(J)/m. Since g_m is a competitor, we have the quantitative bound

0<=p(f_C)-g_m<=c v(J)/m<=cN/m,

where a^N subset J. This is uniform on the FULL primary section, including nonminimal supports. Hence p(f_C) is a uniform limit of actual continuous geometric profiles, lies in C and is the greatest D minorant. It is finite continuous and equals its USC regularization.

The source distinction is essential. Mustata 1109.3825v2 Section 3 allows PERFECT k, but its Section 4.1 is projective over an ALGEBRAICALLY CLOSED field, so it alone does not justify affine-base generation. GJKM 4.6 states the precise projective-over-affine perfect-field extension. Its proof follows the Frobenius trace surjection and projection formula, reduces generation to Castelnuovo–Mumford regularity, and uses corrected Keeler 1.5 in place of Fujita. Rational lambda rounding has finitely many residue remainders; here lambda=m is integral but the same argument applies. We read Mustata's ENTIRE immediate 4.1 proof and GJKM's ENTIRE immediate proof, the complete Keeler 1.5 statement/immediate proof and ENTIRE v5 erratum. False old 3.3 is not applied: E1.3 uses finite faithfully flat altered base; E2.4 and E2.5 repair the reductions and retain 1.5. Deeper regularity, BMS, trace/Cartier isomorphism, Fujita/Serre, alteration/EGA, Hartogs and coherence are disclosed dependencies.

No source-b-divisor converse, singular Jacobian estimate, K_B Cartier assumption, energy or capacity premise, or increasing-supremum D recognition enters the theorem. Artifacts: n8.md, whole-proof.md, source-application-ledger.md, review-data/primary-units-LOCALONLY and evidence/literal-unit-checks.json. Rerun: python extract_literal.py; python build_delivery.py; python final_audit.py. All retained primary bodies remain LOCALONLY.
