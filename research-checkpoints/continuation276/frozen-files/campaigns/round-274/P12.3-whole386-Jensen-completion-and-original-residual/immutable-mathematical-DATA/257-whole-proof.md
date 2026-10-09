# Geometric local envelopes: an independent proof and a Jensen-measure residual criterion

Unverified mathematical draft, 9 October 2026. The original P12.3 statement is unchanged. This paper gives a repaired scoped theorem, independently proves the two auxiliary papers, reconstructs the surrounding envelope and conductor calculus, and pursues the remaining normal case by a new dual criterion. It does not claim the entire original problem. Only the ENTIRE qualified G331, B341 and E350 are incoming correctness grants. Their full literal texts, including annotations, source ledgers, domains and limitations, accompany this manuscript. Candidate382, ROOT380, ROOT381, reconstructed376/377 and historical acceptance labels are data, not grants.

## 1. Objects, raw envelopes, and the exact regularity question

Replace an excellent local ring by its reduction. Fix a proper maximal-primary ideal \(\mathfrak a\). The compact Hausdorff link is \(X=\{v:v(\mathfrak a)=1\}\), with every prime support below the maximal ideal retained. The independent geometric core is G331's actual negative effective finite REAL Cartier presentations on actual primary blowups, with degree nonnegative on every contracted proper integral curve. Its continuous uniform closure is \(C\); its actual decreasing-\(C\)-net completion, with bottom, is \(D\). The comparison with ideal profiles is a qualified G331 theorem, not our definition of positivity. No envelope theorem, arbitrary-model cofinality, singular resolution, or radial/CLD comparison is imported.

For finite continuous \(f\), put
\[
p(f)=\sup\{h\in D:h\le f\}.
\]
A sufficiently negative primary constant is a competitor. All competitors are nonpositive, so the supremum is finite and bounded. If \(h_i\downarrow h\le f\) is an actual representation, the open sets \(\{h_i<f+\epsilon\}\) cover \(X\). Directedness and compactness give one term satisfying this everywhere. Then \(h_i-\epsilon\in C\), is below \(f\), and is above \(h-\epsilon\). Consequently the raw \(C\) and \(D\) suprema agree. In particular \(p(f)\) is lower semicontinuous. Subtracting \(\epsilon\), never adding an unrestricted positive constant, proves
\[
\|p(f)-p(g)\|_\infty\le\|f-g\|_\infty.
\]
Positive homogeneity follows by scaling the cone.

If \(p(f)\) is continuous, choose finitely many continuous competitors approaching it at every point; their maximum approximates it uniformly from below. Thus \(p(f)\in C\). Conversely membership in \(C\) implies continuity. If \(p(f)\in D\), it is upper semicontinuous and hence continuous. A greatest \(D\) minorant is exactly the raw supremum. Any maximal minorant is greatest, since its maximum with any other minorant remains in \(D\). Finally, if the upper regularization \(p(f)^*\) belongs to \(D\), then \(p(f)^*\le f\) by continuity of \(f\), so it is a competitor and equals \(p(f)\). These conditions are equivalent. Merely regularizing the raw supremum is not positivity recognition.

There is an intrinsic all-support factorial formula. Define
\[
J_k(f)=\{r\in R:v(r)\ge-kf(v)\text{ for every }v\in X\}.
\]
These are ideals. If \(-f\le M\), then \(\mathfrak a^{\lceil kM\rceil}\subset J_k\), so each is unit or proper primary. An element integral over \(J_k\) satisfies the same inequalities: first kill the support and use the least-valued-term test on its monic equation in the valued quotient field. They are integrally closed and \(J_kJ_l\subset J_{k+l}\). Rational profiles \(-v(I)/k\le f\) have \(I\subset J_k\). The granted rational-profile density, negative rational shifts and the preceding compact argument therefore give
\[
p(f)=\sup_k[-v(J_k(f))/k]
     =\sup_n[-v(J_{n!}(f))/n!].
\]
The factorial profiles increase. No increasing closure of \(D\) is asserted.

We need actual decreasing closure, rather than flattening nested representations. On a normal branch G331 gives the zero dichotomy. Suppose \(u_i\in D\) decreases to \(u\). If every term is zero the assertion is direct. Otherwise restrict to a tail with \(u_i\le-c<0\). For a finite continuous \(F>u\), compactness of strict tests selects \(u_i<F\) everywhere and then a term \(g\in C\) of its representation with \(u_i\le g<F\) and \(g<-c/2\). A sufficiently small positive \(b\) makes \(q=(1-b)g\) strictly above \(u\) and still below \(F\). All-bottom points cause no subtraction of infinities. Apply this insertion to the minimum of two continuous majorants. These majorants are downward directed. Upper semicontinuity of \(u\), normality of the compact Hausdorff space and a Urysohn cutoff produce, for each point and finite \(t>u(v)\), a continuous \(F>u\) with \(F(v)<t\). Insertion shows that the infimum of this ONE decreasing \(C\)-net is \(u\). For a reduced ring pull back to its finitely many normal centres, apply the branch argument and descend by G331's full-fibre \(D\) theorem. This proves closure under decreasing nets of \(D\) with no assumed increasing or arbitrary-infimum closure.

Say CE holds if every finite continuous obstacle has its raw envelope in \(C\). Under CE, for any bounded-above extended upper semicontinuous \(\phi\), take all finite continuous nonpositive majorants of \(\min(\phi,0)\), directed by minima. Their infimum is that function by Urysohn cutoffs. Their envelopes give ONE decreasing \(C\)-net. Its infimum is the greatest \(D\) minorant of \(\phi\). The preceding closure theorem also proves commutation with decreasing obstacle nets having specified upper semicontinuous limits. These assertions include poles and bottom; bounded obstacles give bounded minorants. They supply no increasing-limit shortcut through energy.

For another primary gauge \(\mathfrak b\), let \(d(v)=v(\mathfrak b)>0\) and \(T(v)=v/d(v)\). Both \(d\) and its inverse are bounded continuous. Homogeneous potentials and obstacles transform by \(u_{\mathfrak b}(T(v))=u_{\mathfrak a}(v)/d(v)\). Order, uniform convergence and actual decreasing representations are preserved. Thus
\[
p_{\mathfrak b}(f_{\mathfrak b})(T(v))=p_{\mathfrak a}(f_{\mathfrak a})(v)/d(v),
\]
with the exact three-gauge cocycle. No constant-translation identity is needed.

## 2. Two independent relative regularity proofs

First prove ROOT380's theorem in its actual embedding dimension. Let \(R\) be a finite-type algebra over ANY field \(k\), let \(G\) be coherent on \(\mathbf P^N_R\), and assume \(H^i(G(-i))=0\) for \(1\le i\le N\). Then every nonnegative twist is zero-regular, multiplication by homogeneous coordinates is onto in nonnegative degrees, and \(G\) is globally generated. There is no coherent-sheaf \(R\)-flatness hypothesis.

If necessary extend \(k\) faithfully flatly to an infinite field. A finite affine cover with affine intersections computes coherent cohomology by a finite Cech complex, so flat tensoring commutes with these cohomology groups and with evaluation. Descent of surjectivity follows by the cokernel and faithful flatness. This is the only role of the extension; no Frobenius identification over an imperfect extension is being made here.

There are finitely many associated points of \(G\). The constant coefficient vectors of hyperplanes vanishing at one associated point form a proper \(k\)-linear subspace, since a projective coordinate is nonzero there. An infinite field avoids their finite union. The resulting hyperplane gives an injective multiplication \(G(-1)\to G\), with coherent cokernel \(G'\) on \(\mathbf P^{N-1}_R\). Its cohomology sequence proves zero-regularity of \(G'\), using the groups in degrees \(i\) and \(i+1\); the top missing group is zero by the projective cohomological dimension bound.

Induct simultaneously on \(N\) and the twist. At twist zero the vanishings are assumed. For twist \(t+1\), the sequence with \(G(t-i)\), \(G(t+1-i)\), and \(G'(t+1-i)\) propagates the required vanishings by the twist induction and the dimension induction. The assertion at \(N=0\) is affine generation. To prove multiplication surjectivity, restrict a section of \(G(t+1)\) to the hyperplane, express its restriction by multiplication on \(G'\), and lift the coefficient sections by \(H^1(G(t-1))=0\). The residual section is the hyperplane equation times a section of \(G(t)\). Thus multiplication is onto for every \(t\ge0\). High Serre generation of \(G(t)\), together with repeated multiplication, implies the evaluation of \(G\) is onto. Descend this assertion to the original field. For \(Y\hookrightarrow\mathbf P^N_R\), apply this to the coherent direct image. The very ample embedding and vanishings through \(N\), not merely through \(\dim Y\), are essential to this proof.

There is also the distinct 382 Koszul theorem. On finite-dimensional projective \(Y\) over a noetherian affine base, let \(A\) be ample globally generated, and let \(M\) be coherent. Suppose \(H^i(MA^{-i})=0\) for \(1\le i\le\dim Y\). Choose finitely many generating sections of \(A\). Their Koszul complex is locally split exact because one generator is a unit in any local trivialization; tensoring with \(M\) preserves this exactness. Write Reg(t) for \(H^i(MA^{t-i})=0\), \(i>0\). The Koszul complex resolving \(MA^{t+1-i}\) has its preceding terms \(MA^{t-i},MA^{t-1-i},\ldots\). Their groups in degrees \(i,i+1,\ldots\) vanish by Reg(t); beyond \(\dim Y\) they vanish by coherent cohomological dimension. Chasing the exact complex proves Reg(t+1). The same complex for evaluation onto \(MA^{t+1}\) shows the multiplication map from \(H^0(MA^t)\) by generating sections is onto, since its kernel has zero \(H^1\) by these same higher groups. High Serre generation then proves \(M\) generated. No smoothness, Cohen--Macaulayness or flatness is required. This proof uses the full exact Koszul complex, not only its first short sequence.

Consequently, if \(H=-F\), \(A=O(H)\), \(L\) is Cartier and \(M_1,\ldots,M_r\) is a FIXED finite coherent list, choose \(c_0\) so \((c_0-i)H-L\) is ample for every required \(i\). Then
\[
Q_{e,j}=F_*^e(M_j\otimes O(p^e(c_0H-L)))
\]
is generated for all sufficiently large \(e\), uniformly over that finite list. Projection formula reduces the cohomology to Serre vanishing for \((c_0-i)H-L\). On a finite-type algebra over a perfect field Frobenius is finite, so the sheaves are coherent. The very ample version takes \(i\le N\); the Koszul version takes \(i\le\dim Y\). These results do NOT themselves prove any test-ideal trace presentation or stabilization in one exponent. ROOT380's applications remain conditional on exact presentations with arbitrarily late tails and finite residues.

## 3. Perfect-field diagonal descent and the corrected HH02 gate

Here \(k\subset k'\) are PERFECT fields of characteristic \(p>0\), \(R\) is ANY finite-type \(k\)-algebra, \(q=p^e\), and \(R'=R\otimes_k k'\). There is an \(R'\)-linear identification
\[
\Phi:F_*^eR\otimes_k k'\longrightarrow F_*^eR',\qquad
F_*x\otimes c\longmapsto F_*(x\otimes c^q).
\]
The balance relation uses \((ac)^q=a^qc^q\). Scalar multiplication is the Frobenius scalar action. The inverse sends \(F_*(x\otimes c)\) to \(F_*x\otimes c^{1/q}\); roots are unique in a perfect field. Bounded exponent monomials show that the Frobenius modules of finite-type algebras are finite. No reduced or normal premise is required.

Put \(S=R\otimes_kR\), \(I=\ker(S\to R)\). Compatible Cartier maps are the kernel of
\[
\operatorname{Hom}_S(F_*S,S)\longrightarrow\operatorname{Hom}_S(F_*I,R).
\]
Frobenius finiteness and noetherianity give finite presentations. Presenting each Hom module as a matrix kernel proves Hom base change under the flat extension. Exactness of flat tensoring preserves the displayed kernel and the image of its induced quotient-restriction map into \(\operatorname{Hom}_R(F_*R,R)\). Its cokernel gives faithful descent of membership in that image. Differentials and their fixed-index Fitting ideals also commute with base change, by their finite presentation and minors. This is the complete module statement in ROOT381. It is neither test-ideal field base change nor subadditivity by itself.

The HH02 Theorem 3.4 statement is more precise than 382's n4 wording. For a geometrically reduced equidimensional affine algebra it says that AFTER extension to \(K(t)\), the Jacobian ideal is GENERATED by elements \(c\), EACH admitting a possibly different generically etale polynomial normalization \(A\) and
\[
cR^{1/q}\subset A^{1/q}[R]\simeq A^{1/q}\otimes_A R.
\]
It does not say that each arbitrary Jacobian element has one such normalization. Also \(K(t)\) need not be perfect. The preceding \(\Phi\) cannot be applied blindly to this extension.

The immediate HH02 proof supplies the legitimate route. Over an already infinite perfect field take its generic linear-coordinate choices DIRECTLY: a finite intersection of nonempty generic-coordinate open sets has a rational point. Its choice ensures that every relevant subset of dimension-many coordinates is a finite generically etale normalization. Each complementary Jacobian minor belongs to the corresponding relative Jacobian ideal. The Lipman--Sathaye containment (with the reduced equidimensional variant cited in HH02) supplies the root containment for that minor. The finitely many minors generate the Jacobian. This is exactly the generatorwise generic-coordinate proof, without using \(K(t)\). Over the perfect field, \(A^{1/q}\) is finite FREE over the polynomial ring \(A\), with basis given by coordinate monomials of exponents below \(q\), not merely flat.

Here is the actual lifting diagram. Write \(T=R^{1/q}\), \(P=A^{1/q}[R]\), and \(B=R\otimes_k T\). The module \(P\) is free over \(R\), so \(P\otimes_kT\) is free over \(B\). Multiplication \(B\to T\) is onto. Multiplication \(P\otimes_kT\to T\) is \(B\)-linear and therefore lifts to \(\Psi:P\otimes_kT\to B\). For \(\varphi:T\to R\), form
\[
T\otimes_kT\xrightarrow{c\otimes1}P\otimes_kT
 \xrightarrow{\Psi}R\otimes_kT
 \xrightarrow{1\otimes\varphi}R\otimes_kR.
\]
This is linear over \(R\otimes_kR\) with its Frobenius source structure. After multiplication to the diagonal it sends \(x\otimes y\) to \(\varphi(cxy)\). It therefore induces the required Cartier map \(z\mapsto\varphi(cz)\). In \(F_*\) notation this is the appropriate source precomposition, not an unjustified extraction of an ordinary scalar. The quotient-restriction image is an \(R\)-module. Add the lifts for the Jacobian generators, multiplying by coefficients on the correct module side. This proves the Jacobian inclusion for the whole ideal; one common normalization is unnecessary.

For a finite perfect field extend instead to an infinite PERFECT field, for example the perfection of its rational function field. Geometric reduction and equidimensionality hold for the normal finite-type rings used below. Apply the just-proved infinite-perfect inclusion, then the precise kernel/image and fixed-Fitting descent to recover it downstairs. ROOT381's module theorem needs no such geometric hypotheses, but this application does. The printed finite-field argument through an arbitrary \(k\)-linear retraction is invalid: it would require a multiplicative unital field map from a nontrivial extension into \(k\). It is not used.

The recursive foundation of the HH02 immediate proof is explicit: HH6(1.5.5) for the generic coordinates, Lipman--Sathaye and its reduced equidimensional variant, HH2 Lemma6.4 for the root-module identification, and Kunz. The complete immediately applied HH02 statement/proof was inspected. The historical proofs of those cited inputs were NOT all freshly authenticated or rederived. The repaired theorem below is an ordinary published-background application with that exact qualification; it is not a new formal verification of the historical proof tree.

Smolkin's complete diagonal argument now applies legitimately. Full Hom tensoring supplies all Cartier maps on the product; their compatible quotient-restriction images give the diagonal Cartier algebra. The product of the two big test ideals is stable under the full product algebra; quotient restriction and nondegeneracy give \(\tau_D(ab)\subset\tau(a)\tau(b)\). The Jacobian inclusion and a common big test element give \(\operatorname{Jac}\,\tau(ab)\subset\tau_D(ab)\). Thus
\[
\operatorname{Jac}\,\tau(ab)\subset\tau(a)\tau(b).
\]
All these are BIG, nonfinitistic test ideals in the reduced equidimensional perfect-field setting. With common-multiple asymptotic stabilization, iteration gives the correctly directed formula
\[
\operatorname{Jac}^{l-1}s_{ml}\subset s_m^l.
\]
Neither the reverse containment nor uncorrected singular subadditivity is claimed.

## 4. Canonical flattening and actual primary realization

Let \(B\) be a normal integral affine finite-type algebra over a perfect field of positive characteristic. Let \(x\) be a CLOSED point of codimension at least two and, after shrinking, suppose the puncture is regular. Work locally at \(x\). Include the primary gauge in any given finite collection of primary ideals. Blow up their product and normalize. The product ideal becomes an effective full-fibre Cartier divisor \(F_0\) with negative relatively ample bundle. Every factor is invertible: in a local domain an invertible product \(IJ=(f)\) gives a fractional inverse to \(I\); a unit term in an expression of \(1\) as a sum of products proves that \(I\) is generated by a regular element. Normalization is finite by excellence.

On this normal model the canonical module \(\omega\) is coherent torsion-free of rank one, including the non-Cohen--Macaulay case. Set \(G=\operatorname{Fitt}_1(\omega)\). It is unit on the puncture. The current Fitting strict-transform theorem applies to its blowup: on a chart \(R[G/a]\subset R_a\), discard the \(a\)-power torsion in the pullback. The first Fitting ideal of the result is unit. Its zeroth Fitting ideal is zero after inverting \(a\), hence zero in this chart domain. The locally-free Fitting criterion gives a line bundle of rank one. This proves the step without assuming the original canonical module locally free. Normalize again and pull back the line bundle.

Choose ONE rational section for both the resulting Cartier divisor \(L_0\) and \(K_Y\). They agree as divisors on the puncture, so \(K_Y-L_0\) is exceptional, not just numerically equivalent to an exceptional divisor. Every fibre prime has positive coefficient in the pullback of \(F_0\). Choose \(r\) so
\[
\Delta=rF_0-(K_Y-L_0)\ge0,
\qquad L=K_Y+\Delta=L_0+rF_0\text{ is Cartier}.
\]
The Fitting exceptional Cartier divisor may be zero. Its negative blowup bundle times a high pullback power of \(O(-F_0)\) is ample over the original affine base. Finite normalization preserves ampleness. Take a high power \(A=O(-F)\) that is very ample and globally generated, retaining full-fibre support.

Put \(J=\Gamma(Y,A)\). Sections are regular off \(x\), hence belong to \(B\) by normal Hartogs in codimension at least two. Proper coherence makes \(J\) finite. It is unit off \(x\), and generated pullback gives \(JO_Y=A\). It is proper: all sections vanish at the nonempty closed fibre. It contains a primary power because its only cosupport is \(x\). Select very ample generating sections inside \(J\), then add the other ideal generators. They define a closed immersion of \(Y\) into the projective space of \(J\). On the puncture its image is the graph defined by those generators. Both this image and \(\operatorname{Bl}_J B\) are integral with the SAME dense punctured graph; scheme-theoretic closure gives
\[
Y=\operatorname{Bl}_J B,
\quad JO_Y=O(-F).
\]
This is an actual primary blowup, not an assumed cofinal arbitrary model or an alteration.

Regularity over a perfect field means smoothness on the puncture. Thus \(\operatorname{Jac}(Y/k)\) is unit there. Fix integers \(a,b,N_J\) with
\[
J^aO_Y\subset\operatorname{Jac}(Y/k),\qquad
\Delta\le bF,\qquad \mathfrak a^{N_J}\subset J.
\]
At every support, \(v(\operatorname{Jac})\le a v(J)\le aN_J\). A nonprimary conductor would not give this uniform bound.

## 5. The raw Cartier obstacle before geometric recognition

Let \(C_0\) be an integral exceptional Cartier divisor on this model, with evaluation \(f_{C_0}\). For a semivaluation first pass to \(\operatorname{Frac}(B/\operatorname{supp}v)\). Its generic point is outside \(x\). Properness gives the centre of its valuation ring on \(Y\), and the canonical punctured trivialization of the exceptional line bundle gives its lattice there. Local generators are nonzero in the quotient field, so evaluation is finite. This does not use a field map from \(\operatorname{Frac}B\) through a nonzero support. G331's actual Cartier order units give boundedness and continuity.

For EVERY \(m\ge1\), define
\[
I_m=\Gamma(Y,O(mC_0)),\qquad
\mathfrak b_m=I_mO_Y O(-mC_0),\qquad
u_m=-v(I_m)/m.
\]
Hartogs places the sections in \(B\). Choose \(M\) with \(C_0\ge-MF_{\mathfrak a}\) in actual Cartier order. Then \(\mathfrak a^{Mm}\subset I_m\), and \(I_m\) is unit or proper primary at every index, not only eventually. Products of sections give gradedness. At all valued centres
\[
u_m=f_{C_0}-v(\mathfrak b_m)/m\le f_{C_0}.
\]
For fixed \(v\), the numbers \(v(I_m)\) are finite nonnegative subadditive. Write an arbitrary index as \(qr+s\), using the finite remainder values; the ordinary all-index Fekete argument gives
\[
\lim_m u_m=\sup_m u_m.
\]
No monotonicity of this whole sequence is assumed.

If a rational profile \(-v(I)/q\le f_{C_0}\), test the inequality at every exceptional prime divisor on the NORMAL model. It says \(\operatorname{ord}_E I+q(C_0)_E\ge0\). At the other height-one points, sections of \(I\subset B\) are already regular and the exceptional divisor is zero. Normal height-one regularity therefore implies \(I^r\subset I_{rq}\) for EVERY \(r\). This proves the rational profile below the Fekete supremum. Rational density plus negative rational shifts treats every \(C\) competitor; Section 1 treats every \(D\) competitor. Thus, before any positivity recognition,
\[
p(f_{C_0})=\sup_m u_m=\lim_m u_m
\]
on ALL supports. Put \(h=f_{C_0}-p(f_{C_0})\ge0\).

## 6. Scheme-global big trace generation and the uniform estimate

Use CEMS v4's BIG test ideal, its localization, Cartier shift, and arbitrary-late-tail trace formula. No anticanonical finite generation or corrected Proposition2.10 is used. For a nonzero ideal \(\mathfrak b\) and real \(t\ge0\), power invariance is justified directly: with \(q=p^e\), the exponents \(A_e=\lceil qt\rceil\) and \(B_e=r\lceil qt/r\rceil\) obey \(A_e\le B_e\le A_e+r-1\). One containment of trace sums follows. For the reverse choose a nonzero element of \(\mathfrak b^r\) and multiply a common big test element by it; then that element times \(\mathfrak b^{A_e}\) lies in \(\mathfrak b^{B_e}\). It is still an allowed big test element. This gives exact invariance, not a finite-tail heuristic. Gradedness then makes the asymptotic families directed by common multiples. Noetherianity on a finite affine cover gives stabilization and a common index for any finite list.

Write
\[
t_m=\tau(Y,\Delta,\mathfrak b_\bullet^m),\qquad
s_m=\tau(Y,\mathfrak b_\bullet^m).
\]
Choose \(c_0\) once such that \((c_0-i)H-L\) is ample, where \(H=-F\) and \(i\le\dim Y\) for the Koszul proof (or \(i\le N\) for the very ample proof). For fixed \(m\) choose \(\ell\) attaining \(t_m\). A SCHEME-GLOBAL effective Cartier test divisor \(D_0\) exists as follows. On a finite affine cover choose big test elements and the finite rounding Weil corrections. Dominate their divisors by an effective Weil divisor \(E\). A sufficiently high ample twist of the coherent rank-one sheaf \(O(-E)\) is generated. A nonzero section of \(O(-E)A^r\) cuts an effective Cartier divisor \(D_0\ge E\). Normal height-one regularity says its local equations divided by each local test element are regular. These multiples remain test elements. Therefore the affine trace formulas glue with this single \(D_0\): for EVERY lower bound \(e_0\),
\[
t_m=\sum_{e\ge e_0}\operatorname{Im}\left[
 F_*^e(\mathfrak b_\ell^{\lceil p^e m/\ell\rceil}
 O(K_Y-p^eL-D_0))\longrightarrow O_Y\right].
\]
\(D_0\), \(\ell\), and the Serre threshold may depend on \(m\). The integer \(c_0\) does not.

Set \(q=p^e\), \(a_e=\lceil qm/\ell\rceil\), \(j_e=\ell a_e-qm\). Then \(0\le j_e<\ell\). Products of the actual GLOBAL generators of \(I_\ell\) generate \(\mathfrak b_\ell^{a_e}O(\ell a_e C_0)\). Twist the trace target by \(O(mC_0+c_0H)\). Its source is a quotient of finitely many copies of
\[
Q_{e,j}=F_*^e O(q(c_0H-L)+K_Y-D_0-jC_0).
\]
The maps are \(F_*t\mapsto F_*(st)\), with the section products \(s\) multiplied INSIDE Frobenius. They are linear for the Frobenius scalar action. An ordinary coefficient module is not being incorrectly extracted through \(F_*\). For fixed \(m,\ell,D_0\), the finitely many reflexive factors \(O(K_Y-D_0-jC_0)\) are coherent even when \(K_Y\) is not Cartier. Section 2 and Serre vanishing generate every sufficiently late \(Q_{e,j}\). The arbitrary-late-tail formula permits only these late sources. A coherent target on a quasicompact noetherian scheme has a finite stabilized sum of images; its exponents can be DIFFERENT. Consequently \(t_mO(mC_0+c_0H)\) is generated. There is no one-exponent stabilization assumption.

Put \(c=c_0+1\) and \(F_m=t_mO(mC_0)A^c\), also generated. Its global section ideal \(J_m\) is in \(B\) by Hartogs, with \(J_mO_Y=F_m\). Before the extra \(A\) twist, generation by sections belonging to \(B\) makes the sheaf a subsheaf of \(O_Y\); afterwards it is contained in \(JO_Y\), so \(J_m\) is proper. Let \(T_0=\tau(Y,\Delta)\), unit on the puncture and containing \(J^rO_Y\). The common-test-element formula gives \(\mathfrak b_mT_0\subset t_m\): moving an element \(f\in\mathfrak b_m\) through a Cartier map uses \(f\varphi(F_*z)=\varphi(F_*(f^qz))\). Therefore \(I_mJ^{r+c}\subset J_m\). This proves an actual primary power in \(J_m\) at every \(m\). Its actual geometric primary profile is
\[
g_m=-v(J_m)/m=f_{C_0}-(c v(J)+v(t_m))/m\le f_{C_0}.
\]

The big asymptotic formula of Section 3 gives
\[
\mathfrak b_{ml}T_0\subset t_{ml}\subset s_{ml},
\qquad \operatorname{Jac}^{l-1}s_{ml}\subset s_m^l.
\]
Every ideal here contains a primary power on the model; every valuation used below is finite, including at nonzero supports. Evaluate and divide:
\[
\frac{v(s_m)}m\le
\frac{v(\mathfrak b_{ml})+v(T_0)}{ml}
+\frac{l-1}{ml}v(\operatorname{Jac}).
\]
First let \(l\to\infty\) POINTWISE. Fekete along this subsequence gives \(v(s_m)\le mh+v(\operatorname{Jac})\); the finite \(v(T_0)\) term disappears. The boundary comparison and Cartier shift give \(O(-bF)s_m\subset t_m\subset s_m\). Substitute in \(g_m\). Since it is an actual \(C\) competitor, the lower bound is legitimate, and
\[
0\le p(f_{C_0})-g_m
\le\frac{(c+b)v(J)+v(\operatorname{Jac})}{m}
\le\frac{(c+a+b)N_J}{m}.
\]
The last bound is uniform on EVERY support. Actual primary profiles recognize \(p(f_{C_0})\in C\). A nonprimary Jacobian truncation reverses the correction containment and would not prove this bound.

The signed rational primary lattice is uniformly dense in all continuous functions. Explicitly, after denominators are synchronized,
\[
\min(v(I)-v(J),v(K)-v(H))=v(IH+KJ)-v(JH).
\]
The ideals \((f)+\mathfrak a^N\) separate finite and infinite evaluations; primary constants are available. The compact lattice approximation proof gives density. Every such signed obstacle is carried by a finite primary collection, which Section 4 principalizes on the required model. Clearing denominators, the preceding theorem and nonexpansivity prove CE for all finite continuous obstacles.

We have thus proved: an ISOLATED NORMAL CLOSED algebraic germ over ANY PERFECT field of positive characteristic, of dimension at least two, has continuous geometrically positive envelopes for all finite continuous obstacles on the full link. It has the greatest actual \(D\) envelopes for bounded-above extended upper semicontinuous obstacles, decreasing-obstacle-net stability and exact primary-gauge changes. This is a repaired theorem with the stated HH02 recursive published-background qualification. It covers possibly non-Cohen--Macaulay models and does not use a smooth resolution. It does not claim the corresponding arbitrary nonisolated or imperfect-field theorem.

## 7. Surfaces, characteristic zero, and exact smooth specialization

We reconstruct the older surrounding sectors independently; none follows from a reconstructed376 label. For an excellent normal LOCAL SURFACE, normalize the blowup of the product of a given finite primary collection. The current Stacks surface resolution criterion applies: the scheme has dimension two, finite singular locus, finite normalization and normal completed local rings at its singular points. Excellence and normal formal fibres supply the latter. Its normalized-blowup sequence gives a regular projective surface \(T\), unchanged on the puncture. Stein factorization over the normal local base gives \(\Gamma(T,O)=R\) and connected closed fibre. This is the exact dimension-two use of Lipman's theorem, not resolution in arbitrary dimension or characteristic.

Write the full closed fibre as \(E_i\), and \(F_{\mathfrak a}=\sum b_iE_i\), with all \(b_i>0\). The intersection matrix \(M=(E_iE_j)\) is symmetric, has nonnegative off-diagonal entries and connected graph. Degree of the generated pulled-back gauge gives \(Mb\le0\). At least one entry is strictly negative, since the original gauge blowup has an exceptional curve on which its tautological ample bundle has positive degree. For \(A=-M\) and \(t_i=b_i z_i\), the exact identity is
\[
t^tAt=\sum_i (Ab)_i b_i z_i^2+
\sum_{i<j}(-A_{ij})b_i b_j(z_i-z_j)^2.
\]
Connectivity and the strict entry imply positive definiteness. Each principal inverse is nonnegative: if \(Ay=w\ge0\) and \(y\) has negative part, pairing with that part gives a strictly negative value from positive definiteness and nonpositive cross terms, a contradiction. Hence \(d=A^{-1}{\bf1}\) is strictly positive and rational. Clear denominators. The negative effective exceptional Cartier divisor \(-\sum d_iE_i\) has positive degree on every fibre curve. The curve ampleness theorem applies to the FULL possibly nonreduced projective fibre over an arbitrary residue field. Fibre ampleness extends over the entire local affine base. A high power is very ample generated; its section ideal is primary by normal Hartogs and full-fibre vanishing. The same dense punctured graph proof as Section 4 makes \(T\) an actual primary blowup. All specified primary factors remain principalized.

There is an actual surface trace inequality. On a common regular refinement \(\mu:T'\to T\), let \(D'\) be negative effective and curve-nef. Push its Cartier divisor down to \(D\) on regular \(T\). Projection of actual divisor cycles gives \(D\cdot E=D'\cdot\mu^*E\ge0\). For \(F=D'-\mu^*D\), the contracted principal matrix satisfies \(M_J f\ge0\). Its inverse sign gives \(f\le0\), so \(D'\le\mu^*D\), as actual Cartier divisors and on ALL valued centres. Any finite collection of these regularizations is obtained by the same primary construction, so no all-proper-model cofinality is assumed.

For a signed Cartier obstacle on \(T\), write its coefficients \(c_i=b_i f(v_i)\), \(v_i=\operatorname{ord}_{E_i}/b_i\). Negative curve-nef divisors below it have coefficient vectors satisfying
\[
-B b_i\le z_i\le\min(0,c_i),\qquad Mz\ge0,
\]
where a sufficiently negative gauge multiple is a feasible lower bound. This is a compact nonempty polytope. It is stable under coordinate maxima: for the coordinate attaining the first vector, replacing all other coordinates by larger ones only increases its \(M\)-row because the off-diagonal entries are nonnegative. Taking maxima of coordinate maximizers therefore produces its greatest vector \(z^*\). Its negative effective curve-nef Cartier divisor is an actual geometric core presentation.

The trace inequality controls every core competitor by its trace on \(T\). Uniform limits control every \(C\) competitor. For a \(D\) competitor, clamp it below by a negative constant still below the obstacle, then choose a term of its actual decreasing continuous representation whose finitely many trace values are below the obstacle plus \(\epsilon\); negative shifting removes \(\epsilon\). The finite coefficient projections converge to the clamped trace, and the trace inequalities pass at every boundary point. Thus the greatest vector dominates EVERY \(D\) competitor, while its own evaluation is below the obstacle. It is the raw envelope. Signed lattice density proves CE for every continuous obstacle on every excellent normal local surface, arbitrary characteristic and arbitrary/imperfect residue field, including mixed characteristic. Section 1 supplies upper semicontinuous envelopes, nets and gauge changes.

For characteristic zero use the THREE-author Boucksom--de Fernex--Favre local-volume paper, in its normal algebraic over ALGEBRAICALLY CLOSED characteristic-zero setting. The immediately applied units are 1.12, 2.12--2.17, 3.12--3.17 and 4.11. The independent core maps into the source nef cone using ample perturbation, without asserting the converse. For a signed Cartier obstacle \(C_0\), Section 2 gives its largest-trace nef envelope \(W\le C_0\); base trace zero and negativity give \(W\le0\), and a negative primary reference lies below it.

At an isolated CLOSED singularity, clear denominators first. Source4.11 gives primary/unit ideal Cartier UPPER approximations \(B_k\ge W\) with coefficientwise convergence; its proof uses a primary-bounded Jacobian/defect correction. The direction is upper, not lower. On the finitely many vertices of a determining model choose \(\eta_k\downarrow0\) bounding their normalized excess. Then \(B_k+\eta_k Z(\mathfrak a)\) has trace below the obstacle and is source-nef. By the largest-trace property,
\[
B_k+\eta_k Z(\mathfrak a)\le W\le B_k
\]
on ALL divisorial valuations. The actual primary profiles are continuous and uniformly Cauchy on the divisorially dense full link; their continuous limit \(U\in C\) extends these inequalities to every support. Every \(D\) competitor is controlled by choosing ONE continuous majorant term meeting the finite trace tests and then a negative shift; its source-nef inequality gives dominance by \(W\), and continuity plus divisorial density gives dominance by \(U\). Thus \(U\) is the raw envelope. Zero uses the unit ideal; early approximations need only be unit-or-primary; a strictly negative value makes them eventually proper. This proves CE for the isolated closed normal characteristic-zero sector, with exactly these field and algebraic hypotheses.

In the nonisolated characteristic-zero case the general source3.17 correction involves \(Q=\mathfrak d(K)\operatorname{Jac}\), which can be nonprimary. Its multiplier profiles can be truncated by primary powers to get continuous profiles \(u_k\) with divisorial estimates
\[
W-v(Q)/(Nk)\le u_k\le W+\eta_k.
\]
Negative shifting supplies actual competitors: choose the primary truncation level so its added profile is below a fixed negative primary lower bound, then choose the shift \(\eta_k\) at the finitely many determining vertices. Height-one regularity on the determining normal model makes the resulting primary ideal a section of its signed obstacle sheaf, so the shifted profile is below that obstacle on every valued centre. Conversely every rational competitor lies below \(W\) by the largest-trace characterization. Uniform approximation and negative shifting extend that assertion to \(C\); for a \(D\) competitor select ONE continuous representation term at the finitely many trace tests and remove its error by a negative shift. This controls all \(D\) competitors without assuming their limit continuous.

To extend the estimate, FIRST work on the OPEN set where \(v(Q)<\infty\): the relevant continuous differences and divisorial density there establish the inequalities. THEN restrict to \(\{v(Q)\le L\}\) to obtain uniform error \(L/(Nk)+\eta_k\). Density on that closed subset was not assumed. The shifted competitors converge locally uniformly on the finite-\(Q\) open locus to the raw envelope, since the preceding upper comparison controls every competitor there. On the infinite-\(Q\) stratum this argument supplies neither continuity nor positivity. Boundedness of a nonzero ideal's value on the whole primary link is equivalent to that ideal being unit or primary: if its radical is smaller, a centred semivaluation on an appropriate positive-dimensional quotient kills it. Failure of this correction bound is an argument failure, not an envelope counterexample.

At a smooth affine CLOSED germ over an algebraically closed characteristic-zero field, use BFJ at its exact published hypotheses. G331 supplies the full class specialization, with all semivaluations and bottom adjoined. BFJ3.18 and its full3.22 proof, on a determining dual complex, give section-ideal approximations with
\[
W_j\le W\le \frac{j}{j+C_0}W_j.
\]
A negative primary lower bound bounds the difference by a constant times \(1/j\). The source's substantive closed-face continuity and the all-retraction infimum extend it to ALL supports. Corrected eventual proper-primary approximations, zero/unit, bottom, DVR and empty dimension-zero cases are treated separately; no merely interior convex-continuity argument is substituted for closed-face continuity. It follows that the envelope constructed here equals the published smooth BFJ envelope. This proves the requested smooth specialization only in that actual smooth affine closed/algebraically closed/characteristic-zero range.

On an actual SMOOTH primary model over a perfect positive-characteristic field, the independent fixed-model result also follows from GJKM4.6: it requires a smooth integral scheme projective over an AFFINE finite-type algebra, an ample globally generated bundle, a nonzero section and a nef difference. Apply with \(D=C_0,E=mC_0,\lambda=m\), so the difference is zero. A fixed generated canonical inverse twist cancels its canonical factor. Smooth asymptotic subadditivity gives generated primary profiles with error \(c v(J)/m\). The corrected Keeler v5 theorem and its ENTIRE erratum repair the referenced Fujita step. This is conditional on an actual smooth primary model for every finite collection, and supplies no singular application of GJKM4.6. Sections 4--6 remove that condition in the isolated perfect-field sector by a different argument.

## 8. Actual finite covers and the nonisolated quadratic family

Let a normal target \(R\) inject finitely into a reduced algebra \(S\) with EVERY minimal source component dominating the target. The qualified normal trace has full finite fibres, with positive generic inseparable lengths, proved by norm coefficients and support-quotient Gauss values. For a continuous \(C_S\) function, normalize the generic components in a common normal field closure and take the finite conjugate maximum. It remains in \(C\), is constant on the full fibres and descends positively by G331. Thus fibrewise maximum preserves \(C\). A finite maximum commutes with a decreasing nonpositive extended net by finite directedness, so the same is true for \(D\). These operations never create a degree for a vertical minimal component; such components are excluded in this theorem.

For a base obstacle \(f\), every source competitor below \(\rho^*f\) has its fibre maximum descend to a base competitor. Base competitors pull back. Consequently
\[
p_S(\rho^*f)=\rho^*p_R(f).
\]
If all marked source centres have CE, the left side is continuous \(C\), so quotient topology and full-fibre positive descent give CE downstairs. This is an actual finite-cover theorem; a finite alteration of positive-dimensional fibres is not such a cover, and no universal good-cover existence is asserted.

The nonisolated quadratic examples satisfy this theorem. Let
\[
R=k[U,V,W,z_1,\ldots,z_r]_{(U,V,W,z)}/(UW-V^2),
\quad S=k[s,t,z_1,\ldots,z_r]_{(s,t,z)},
\]
with \(U=s^2,V=st,W=t^2\). The hypersurface is an integral domain, Cohen--Macaulay and regular in codimension one; its singular locus has codimension two, also in characteristic two. Hence it is normal. The map is finite because \(s,t\) are integral. Its generic degree is two: separable off characteristic two and radicial in characteristic two. The fibre has basis \(1,s,t\) and length three, so it is not flat of generic rank two. Nevertheless it is an ACTUAL finite smooth cover, in every perfect positive characteristic, including the purely inseparable characteristic-two case. The isolated theorem applies to the regular source, and the finite-cover theorem gives CE to every \(r\ge0\) member. In algebraically closed characteristic zero the source CE is BFJ, giving the analogous conclusion. For \(r\ge1\) the target is nonisolated; its nonprimary Jacobian bound failure therefore cannot be a counterexample.

## 9. Conductor quotient, positivity domain, and curves

Let \(S\) normalize an excellent reduced local ring, \(\rho:X_S\to X_R\), and \(\mathfrak c\) be the conductor. G331 gives the full compact quotient: at finite conductor value the fibre is a singleton; at infinite value equality of restrictions through the conductor quotient is EXACTLY the equivalence rule. Minimal branches, internal supports and nonpure components remain. The finite-conductor singleton locus is open and dense upstairs, since the conductor contains a regular element and centred divisorial valuations are dense on every normal centre.

For finite continuous \(f\), clip to \([-B,0]\) without changing competitors. A source competitor may be clamped to \(-B\). The primary masks
\[
b_N=-(B/N)v(\mathfrak c+\mathfrak a^N)
\]
belong to \(C_R\), are exactly \(-B\) on the conductor-infinite locus and tend to zero at every finite-conductor point. The source function \(\max(g+\rho^*b_N,-B)\) is full-fibre constant: on the singleton locus there is nothing to check; on the infinite locus it is \(-B\). G331 supplies its POSITIVE \(C_R\) descent. Sending \(N\to\infty\) proves
\[
\rho^*p_R(f)=p_S(\rho^*f)
\quad\text{on the finite-conductor locus}.
\]
This argument uses primary masks rather than a purported uniform conductor error.

Suppose every normal centre has CE, and write \(U=p_S(\rho^*f)\in C_S\). The preceding dense equality says that the upper regularization of the pulled-back raw envelope is \(U\) upstairs. For any function on a compact quotient, the upstairs regularization and a compact fibre cover give
\[
F^*(x)=\max_{y\in\rho^{-1}(x)}(\rho^*F)^*(y).
\]
Indeed an upstairs neighbourhood projects a neighbourhood in the appropriate fibre test after finitely covering the fibre and removing the closed image of its complement; conversely any base neighbourhood pulls back to an upstairs one. Applying this gives
\[
p_R(f)^*(x)=\max_{\rho^{-1}(x)}U.
\]
This is a regularization identity, not automatic positivity. Positive descent holds iff \(U\) is constant on EVERY full fibre. In that case its descended \(C_R\) function lies below \(f\) and equals the raw envelope. Conversely, if the raw envelope is continuous, its pullback agrees with \(U\) on a dense locus and hence everywhere. If the fibre maximum is continuous, its pullback dominates \(U\) and agrees on the same dense locus, so equality forces fibre constancy. Thus continuity, positive greatest minorant and full-fibre compatibility are equivalent. Outside this domain there is no maximal \(D\) minorant. Without normal-centre CE the exact criterion is that the upstairs raw envelope itself be continuous and fibre constant; no unconditional fibre-MAX positivity is claimed.

For extended upper semicontinuous obstacles or poles the unconditional identity is instead the supremum over FULL-FIBRE-CONSTANT source \(D\) competitors below the pulled-back obstacle. Pullback and G331 descent prove it. The finite-continuous maximum formula does not extend merely because source envelopes are upper semicontinuous.

The nonnormal obstruction is real. Over any field take the double plane \(R=k[x,y,z]_{(x,y,z)}/(xy)\) and maximal-ideal gauge. Its normal planes are \(A=k[x,z]_{(x,z)}\), \(B=k[y,z]_{(y,z)}\); the conductor identifies their boundary points killing the transverse coordinate. Let
\[
f=-1-1/v(y),\qquad 1/\infty=0.
\]
This is continuous and lies in \([-2,-1]\). On \(A\), \(f=-1\). On \(B\), every primary-profile function satisfies \(g(v)\le g(\operatorname{ord}_{\mathfrak m})\), since all normalized \(v\) have \(v(I)\ge\operatorname{ord}_{\mathfrak m}(I)\). The inequality passes to \(C,D\). Thus any \(B\) competitor is at most \(-2\).

On \(A\) use \(J_n=(x^n,xz^{n-1},z^{2n})\) and \(g_n=-v(J_n)/n\), \(n\ge2\). With \(\min(v(x),v(z))=1\), it equals \(-1\) if \(v(x)\le v(z)\), and otherwise equals \(-\min(1+(v(x)-1)/n,2)\). At the point killing \(x\) it is \(-2\). These increase, and \((g_n,-2\text{ on }B)\) is full-fibre-compatible \(C_S\), hence descends positively. They prove the raw envelope equals \(-1\) on \(A\) off that point and \(-2\) on \(B\) and the identified point. The values \((v(x),v(z))=(L,1)\) approach the identified point as \(L\to\infty\), proving non-upper-semicontinuity. Its regularization is \(-1\) there but \(-2\) at the ordinary \(B\) valuation, violating the displayed \(B\) inequality. It is not in \(D\), and no maximal \(D\) minorant exists. This is a continuous signed primary/model obstacle but the germ is NONNORMAL. It does not settle the residual normal problem.

For EVERY excellent reduced curve the link is the finite discrete set of normalization DVR centres, not merely irreducible components. The conductor has finite value at each branch, so there are no nontrivial link fibres. On a DVR the marked point is an actual effective Cartier divisor; there are no contracted curves to test. Nonpositive real multiples give every finite negative slope, including zero. G331's full positive descent gives all finite nonpositive branch vectors. The ONE decreasing net \(\max(u,-j)\) gives all extended vectors, retaining partial bottom and mixed zero. Hence, geometrically and not only order-theoretically,
\[
P_{\rm geom}(\phi)=P_{\rm ideal}(\phi)=\min(\phi,0)
\]
for every branch obstacle. If \(a_q=\operatorname{ord}_q\mathfrak a\), the gauge change has factor \(a_q/b_q\). The B341/E350 reference mass is \([\kappa(q):\kappa(\mathfrak m)]a_q\); a branch bottom has positive reference mass and infinite energy. The literal disc radial class remains \(\{0\}\cup[-\infty,0)^q\) in the dossier's specified normalization/conductor range. Its mixed-zero exclusion is compatible with this DIFFERENT valuative boundary cone; no CLD or analytic radial identity is asserted.

## 10. Energy and capacity diagnostics do not recognize raw positivity

Use E350 ONLY on its specified actual \(D\) and finite-energy domains, with ambient arity \(n-1\), full fibres, corrected SH quotient-annihilator qualification and exact reference convention. On a smooth surface \(I_j=(x,y^j)\), \(u_j=-v(I_j)/j\) increases to zero off the point killing \(x\), but to \(-1\) at that point. The limit is not upper semicontinuous and not in \(D\); its regularization is zero. A column count gives for ALL integers \(r,s\ge0\)
\[
\ell(R/\mathfrak m^r I_j^s)=r(r+1)/2+rs+j s(s+1)/2.
\]
Thus \(e(I_j)=j\), \(e(\mathfrak m,I_j)=1\), diagonal size \(1/j\), energy \(-1/(2j)\) and mass \(1/j\). E350's reference-moment inequality gives capacity of \(\{-u_j>\epsilon\}\) at most \(1/(\epsilon\sqrt j)\). Vanishing energy and capacity do not put this increasing limit in \(D\).

The normal quadratic surface gives a strictly negative version. Put \(I_n=(X^n,XY^{n-1},Y^{2n})\) in \(k[X,Y,Z]/(XY-Z^2)\), \(n\ge2\), with gauge \((X,Y)\). The profiles increase to \(-1\) away from the point killing \(X,Z\), and to \(-2\) there. They are not the raw envelope of a continuous obstacle: CE holds by Section 8. The maximal-ideal blowup has exceptional conic of degree two, so its reference measure is \(2\delta_{\operatorname{ord}_{\mathfrak m}}\). The test \(-v(X)\) has an actual decreasing truncated representation. Form order, followed by ordinary sequential monotone convergence, gives \(\int v(X)d\mu(\phi)\le2\) for every capacity test. Hence \(\operatorname{Cap}\{v(X)>T\}\le2/T\); the point in question has zero capacity. The increasing limit still fails \(D\).

For completeness its exact ALL-index colength is
\[
\ell(R/I_n^k)=(n^2+n)k^2+(n^2-n+2)k.
\]
Embed into \(k[s,t]\) by \(X=s^2,Y=t^2,Z=st\). Monomials are those whose two exponents have the same parity. Products of \(k\) generators have exponents \((2ni+2j,\,2(n-1)j+4n(k-i-j))\), \(i+j\le k\). For a column \(2p\), minimize the second exponent by maximizing \(4ni+(2n+2)j\) under \(ni+j\le p\). If \(p<k\), take \(i=0,j=p\). If \(p\ge k\), take \(i=\lfloor(p-k)/(n-1)\rfloor,j=k-i\), clipped at \(i=k\); comparing the next feasible \(i\) shows it is worse by \(2n(n-1)\) except the transition. Paired even and odd columns have the same positive even threshold and contribute that threshold in total. Summing the resulting arithmetic runs gives the displayed polynomial, with \(n=2\) handled by the same formula. Thus \(e(I_n)=2n^2+2n\), diagonal profile size \(2+2/n\) and energy \(-1-1/n\). These signs use E350's \(E=-F/2\). They are diagnostic computations, not envelope counterexamples or an increasing-completion theorem.

## 11. A new analytic mechanism: canonical Jensen measures

This section is a new residual attempt, proved here from the qualified geometric \(C\), not an additional order definition of psh. Let \(M_{\le1}(X)\) be the weakly compact space of positive Radon measures of mass at most one. Define the canonical Jensen set
\[
\mathcal J_x=\{\mu\in M_{\le1}(X):h(x)\le\int h\,d\mu\text{ for every }h\in C\}.
\]
It is nonempty (\(\delta_x\) belongs), compact and convex. Its graph is closed, since every defining function \(h\) is continuous. All ingredients are the already independently geometric cone; no replacement cone is introduced.

We prove an exact dual formula for EVERY finite continuous obstacle:
\[
p(f)(x)=\min_{\mu\in\mathcal J_x}\int f\,d\mu.
\]
One inequality follows immediately by testing a competitor \(h\le f\). For the reverse, in the Banach space \(C(X)\times\mathbb R\) consider the convex cone
\[
W=\{(g,t):\exists h\in C,\ h\le g,\ t\le h(x)\}.
\]
For \(t>p(f)(x)\), \((f,t)\) is outside its closure: if \((g_i,t_i)\to(f,t)\) in norm, nonexpansivity gives \(t_i\le p(g_i)(x)\le p(f)(x)+\|g_i-f\|\), a contradiction. Hahn--Banach separation from the closed convex cone gives a nonzero functional \(L(g,t)=\mu(g)-\alpha t\), nonnegative on \(W\), strictly negative at \((f,t)\). Since \((r,-s)\in W\) for \(r\ge0,s\ge0\), \(\mu\) is positive and \(\alpha\ge0\). If \(\alpha=0\), the pairs \((-a,-a)\in W\) force \(\mu(X)=0\), contradicting nonzero separation. Divide by \(\alpha>0\). The pairs \((h,h(x))\) give exactly the Jensen inequalities, and \(h=-1\) gives mass at most one. Separation says \(\int f,d\mu<t\). Let \(t\downarrow p(f)(x)\). Compactness attains the infimum. The positive-functional/Radon correspondence, Banach separation and weak compactness of the unit positive dual ball are explicit ordinary functional foundations; the dual argument itself is new.

There is an exact topological criterion. CE holds iff the correspondence \(x\mapsto\mathcal J_x\) is lower hemicontinuous in the weak measure topology; its upper hemicontinuity already follows from closed graph and compact ambient measure space. Lower hemicontinuity makes the minimum of each continuous linear test upper semicontinuous; closed graph gives lower semicontinuity, so the dual formula proves CE.

Conversely suppose all \(p(f)\) are continuous, but lower hemicontinuity fails at \(x_0\) for some \(\mu_0\in\mathcal J_{x_0}\). A weak neighbourhood can be specified by finitely many continuous functions \(f_1,\ldots,f_r\) and an Euclidean ball of radius \(\epsilon\) about their integrals at \(\mu_0\). There is a net \(x_i\to x_0\) such that the compact convex projections of \(\mathcal J_{x_i}\) avoid that ball. Closest-point separation gives unit vectors \(a_i\) satisfying
\[
a_i\cdot\left(\left(\int f_jd\mu\right)_j-
\left(\int f_jd\mu_0\right)_j\right)\ge\epsilon
\quad(\mu\in\mathcal J_{x_i}).
\]
A subnet has \(a_i\to a\). All projected vectors are uniformly bounded, so the same inequality with \(a\) holds with \(\epsilon/2\) eventually. For \(f=\sum a_j f_j\), the dual formula gives \(p(f)(x_i)\ge\int f d\mu_0+\epsilon/2\), whereas \(p(f)(x_0)\le\int f d\mu_0\). This contradicts continuity. This proves necessity, retaining nonmetrizable links and actual nets.

The criterion provides a genuine geometric/analytic direction for the residual: prove weak lower hemicontinuity of THESE canonical measures, or find its failure at a normal germ. The matrix, trace and finite-cover arguments above prove it indirectly in their sectors; the criterion does not assert it universally.

There is a useful normal obstruction reduction. G331's actual divisorial inequality says \(g(\nu)\ge A_\nu g(v)\) for all \(g\in C\) and all \(v\), with fixed \(A_\nu>0\). If a continuous obstacle is negative somewhere, divisorial density supplies \(\nu\) with \(f(\nu)<0\). Every competitor then satisfies
\[
g(v)\le f(\nu)/A_\nu<0\quad\text{for ALL }v.
\]
Consequently on a normal branch the raw envelope is either zero (precisely when \(f\ge0\)) or uniformly strictly negative. This extends to the raw supremum without recognizing it in \(D\). A genuine normal continuous-obstacle counterexample cannot consist of a mixed-zero discontinuity. It would have to fail upper semicontinuity while remaining bounded and uniformly negative. The double-plane obstruction and the increasing energy spikes therefore cannot furnish it.

We tested the correction mechanism and the Jensen route, not merely restated the residual. Primary truncations reverse the needed subadditivity correction. The quadratic example has a good cover in every perfect positive characteristic. The dual proof reduces the residual to lower hemicontinuity but does not derive it from the available valuations, intersection/energy bounds, or conductor rules. No normal counterexample satisfying the continuous signed primary/model-obstacle condition was obtained. In particular arbitrary excellent normal dimension at least three, general nonisolated perfect-characteristic algebraic germs, the characteristic-zero infinite-\(Q\) locus, mixed/imperfect/nonalgebraic/nonclosed scope remain unresolved. The original's 'when possible/appropriate regularity' is not redefined as this criterion; its entire completion criteria still require the actual existence/positivity theory. Original candidate=false.

## 12. Independent verdicts and proof boundary

ROOT380: PASS for the complete relative embedding regularity theorem over finite-type bases over any field, including finite fields, with no coherent-sheaf base flatness. Its very ample and through-\(N\) hypotheses and its conditional trace applications are retained.

ROOT381: PASS for the complete perfect-extension Frobenius/Hom/diagonal kernel/image and fixed-Fitting module theorem, for any finite-type algebra with no reduced/normal premise. Its Jacobian application requires the separately justified infinite-perfect reduced-equidimensional inclusion. It does not independently prove test-ideal base change or subadditivity.

Literal382: REJECT AS WRITTEN at the n4 assertion granting one normalization to every arbitrary Jacobian element, and at any reading of its field route that identifies Frobenius/Hom through imperfect \(k(t)\). These are precise proof defects, not counterexamples to the isolated theorem. Generatorwise module linearity over directly infinite perfect fields, followed by perfect-extension faithful descent, repairs them. The repaired scoped isolated theorem and the entire surrounding envelope, surface, characteristic-zero, finite-cover, nets, conductor, curve and diagnostic chain are accepted here as UNVERIFIED draft mathematical claims relative to the qualified grants and the disclosed ordinary published foundations. This is not publication, formal certification, inherited acceptance, or a count change.

No historical HLS incomplete-unit receipt was used: the complete published7.5(f) tail and8.4--8.5 are retained and read. HLS7.1 assumes regularity and8.3 is a conjecture, so no singular mixed-characteristic extension results. Smolkin's printed retraction field action is not used. GJKM4.6 is applied only to smooth projective-over-affine models. CEMS2.10 and anticanonical finite generation are not used. The mandatory G331/B341/E350 Keeler, BFJ, support, model, nilpotent, polar and SH quotient-colon qualifications remain inseparable.

Original P12.3: INCOMPLETE. The construction provides actual positivity and regularity in substantial precise sectors and an exact finite-continuous conductor compatibility domain, including a genuine nonnormal obstruction and all reduced curves. It does not prove arbitrary normal CE or a scope-negating normal counterexample sufficient to close the unchanged literal target. P12.4 products, P12.5 energy and full P12.6 operator theory remain separate; they are used only within the supplied grant scopes where explicitly stated.

All applied immediate source units and mathematical bodies are identified in the accompanying source ledger and coverage report. Exact full-body duplicates were compared as bytes; expanded nine-note texts were never substituted for the nine DIFFERENT actual FINAL texts. Full primary bodies and pixels remain LOCALONLY. No source metadata, finite diagnostic, retention hash or execution success is a mathematical premise. The source is deliberately UNCOMPILED because ROOT retains compilation and publication. No supplied executable was imported or run, no active output or extra agent/model call was used, and the protected P16.4 editor was untouched.
