# lemma lem:archimedean-dichotomy-and-characters

## statement

Let \(R\) be a commutative ring and \(x\) a multiplicative seminorm on \(R\), normalized by \(|1|_x=1\). Put

\[
 \rho(x)=\frac{\log\max\{1,|2|_x\}}{\log 2}.
\]

Then \(\rho(x)=0\) if and only if the absolute value induced by \(x\) on the fraction field of \(R/\ker(x)\) is non-Archimedean. If \(\rho(x)>0\), then \(0<\rho(x)\leq 1\) and there is a character \(\chi_x:R\to\mathbf C\) such that

\[
 |a|_x=|\chi_x(a)|_\infty^{\rho(x)}\qquad(a\in R).
\]

Any two such characters are equal or complex conjugate.

## proof

Set \(\mathfrak p=\ker(x)\) and \(K=\operatorname{Frac}(R/\mathfrak p)\). The seminorm induces an absolute value, still denoted \(|\cdot|_x\), on \(K\).

We first recall the elementary Archimedean dichotomy, including the normalization needed below. If \(|2|_x\leq1\), write \(n^m\) in base \(2\). The number of its nonzero binary digits is \(O(m)\), while every power of \(2\) has absolute value at most \(1\). The ordinary triangle inequality therefore gives \(|n|_x^m=|n^m|_x=O(m)\), and taking \(m\)-th roots gives \(|n|_x\leq1\) for every positive integer \(n\). Expanding \((a+b)^m\), using \(\left|\binom m j\right|_x\leq1\), and taking \(m\)-th roots gives

\[
 |a+b|_x\leq\max\{|a|_x,|b|_x\}.
\]

Thus the absolute value is non-Archimedean. The converse is immediate from \(|2|_x=|1+1|_x\leq1\). This proves the assertion for \(\rho=0\).

Suppose now that \(|2|_x>1\). The standard base-expansion proof of Ostrowski's normalization is short enough to include. For integers \(a,b\geq2\), write \(a^m\) in base \(b\). If \(C_b=\max_{0\leq j<b}|j|_x\), then

\[
 |a|_x^m\leq C_b(1+m\log_b a)\max\{1,|b|_x^{m\log_b a+O(1)}\}.
\]

After taking \(m\)-th roots and letting \(m\to\infty\),

\[
 |a|_x\leq\max\{1,a^{\log_b|b|_x}\}.
\]

Because \(|2|_x>1\), interchanging \(a\) and \(2\) first shows that every \(a\geq2\) has \(|a|_x>1\), and then the two inequalities obtained by interchanging \(a,b\) show that

\[
 |n|_x=n^\rho,\qquad \rho=\frac{\log|2|_x}{\log2}.
\]

The triangle inequality gives \(|2|_x\leq2\), hence \(0<\rho\leq1\).

Define \(v(a)=|a|_x^{1/\rho}\) on \(K\). It is multiplicative and restricts to the usual absolute value on \(\mathbf Q\). It also satisfies the ordinary triangle inequality. Indeed, the binomial expansion and \(\left|\binom m j\right|_x=\binom m j^\rho\) give, with \(A=v(a)\) and \(B=v(b)\),

\[
 |a+b|_x^m
 \leq \sum_{j=0}^m\bigl(\tbinom m j A^jB^{m-j}\bigr)^\rho
 \leq(m+1)(A+B)^{\rho m}.
\]

Taking the power \(1/(\rho m)\) and then letting \(m\to\infty\) yields \(v(a+b)\leq A+B\).

Let \(\widehat K\) be the completion for \(v\). The closure of \(\mathbf Q\) in \(\widehat K\) is \(\mathbf R\), so \(\widehat K\) is a commutative real Banach division algebra. For completeness, the Gelfand--Mazur step used here is as follows. A complex Banach division algebra is \(\mathbf C\): for any element \(z\), the spectrum is nonempty, since otherwise the resolvent \((z-\lambda)^{-1}\), after composition with continuous linear functionals, would be a bounded entire function tending to \(0\) at infinity, contradicting Liouville's theorem; in a division algebra a spectral value \(\lambda\) forces \(z=\lambda\). If a commutative real Banach division algebra \(E\) contains a square root of \(-1\), the complex case gives \(E=\mathbf C\). Otherwise \(E[i]=E[T]/(T^2+1)\), with any equivalent complete finite-module algebra norm, is a complex Banach division algebra and hence \(\mathbf C\); then \(E\) is a closed subfield of \(\mathbf C\) containing \(\mathbf R\) but not \(i\), so \(E=\mathbf R\). Consequently \(\widehat K\simeq\mathbf R\) or \(\mathbf C\), isometrically for \(v\). Composing \(R\to K\to\widehat K\hookrightarrow\mathbf C\) gives a character \(\chi_x\) satisfying

\[
 |a|_x=v(a)^\rho=|\chi_x(a)|_\infty^\rho.
\]

It remains to prove uniqueness, since this will also be used later. Let \(\sigma,\tau:R\to\mathbf C\) satisfy \(|\sigma(a)|=|\tau(a)|\) for all \(a\). Their kernels agree. On the common fraction field they induce a modulus-preserving field isomorphism

\[
 \theta:\operatorname{Frac}(\sigma(R))\longrightarrow
 \operatorname{Frac}(\tau(R)),\qquad \sigma(a)/\sigma(b)\longmapsto\tau(a)/\tau(b).
\]

It extends isometrically to the closures \(L,M\subset\mathbf C\). Each closed subfield of \(\mathbf C\) containing \(\mathbf Q\) contains \(\mathbf R\); it is \(\mathbf R\) if it has no nonreal element and is \(\mathbf C\) otherwise. Hence \(L,M\in\{\mathbf R,\mathbf C\}\). If \(L=\mathbf R\), continuity makes the extension fix \(\mathbf R\) pointwise, so \(M=\mathbf R\) and \(\theta\) is the identity. If \(L=\mathbf C\), the extension is a continuous automorphism of \(\mathbf C\), fixes \(\mathbf R\), and sends \(i\) to \(i\) or \(-i\); it is therefore the identity or complex conjugation. Thus \(\tau=\sigma\) or \(\tau=\overline\sigma\). Applying this after taking the positive \(\rho\)-th root proves uniqueness for the characters representing \(x\). ∎

# lemma lem:finite-type-character-topology

## statement

Let \(B\) be a finitely generated \(\mathbf Z\)-algebra. Every Archimedean seminorm \(x\in\mathcal M(B)\) has a representation

\[
 |b|_x=|\chi_x(b)|_\infty^{\rho(x)}
\]

with \(\chi_x:B\to\mathbf C\), unique up to complex conjugation. If \(x_\lambda\to x\) is a net of Archimedean seminorms and \(\inf_\lambda\rho(x_\lambda)>0\), then, after arbitrary choices of representatives \(\chi_\lambda\), every subnet has a further subnet converging pointwise on \(B\) to \(\chi_x\) or \(\overline{\chi_x}\).

## proof

Existence and uniqueness are Lemma lem:archimedean-dichotomy-and-characters. We prove the asserted topology with nets.

Choose a presentation

\[
 B=\mathbf Z[t_1,\ldots,t_r]/I.
\]

Write \(\rho_\lambda=\rho(x_\lambda)\) and assume \(\rho_\lambda\geq\varepsilon>0\). The function \(x\mapsto|2|_x\) is continuous, so

\[
 \rho_\lambda\longrightarrow\rho(x).
\tag{8}
\]

For each generator, \(|t_j|_{x_\lambda}\to|t_j|_x\), hence these numbers are bounded, say by \(K_j\). Since every Archimedean exponent is at most \(1\),

\[
 |\chi_\lambda(t_j)|
   =|t_j|_{x_\lambda}^{1/\rho_\lambda}
   \leq \max\{1,K_j^{1/\varepsilon}\}.
\tag{9}
\]

Thus the points

\[
 z_\lambda=(\chi_\lambda(t_1),\ldots,\chi_\lambda(t_r))
\]

lie in one compact polydisc. The same is true after passing to any subnet, and compactness for nets gives a further subnet converging to a point \(z=(z_1,\ldots,z_r)\). For every \(P\in I\), \(P(z_\lambda)=0\); hence \(P(z)=0\). Thus \(z\in V(I)(\mathbf C)\) and evaluation at \(z\) defines a character \(\eta:B\to\mathbf C\).

For \(b\in B\), choose \(P\in\mathbf Z[t_1,\ldots,t_r]\) representing it. Along this further subnet,

\[
 \chi_\lambda(b)=P(z_\lambda)\longrightarrow P(z)=\eta(b).
\tag{10}
\]

Using convergence of the seminorms, (8), and (10), we get for every \(b\in B\)

\[
 |b|_x
 =\lim_\lambda|b|_{x_\lambda}
 =\lim_\lambda|\chi_\lambda(b)|^{\rho_\lambda}
 =|\eta(b)|^{\rho(x)}.
\tag{11}
\]

In particular, \(|\eta(b)|=|\chi_x(b)|\) for every \(b\). The last part of Lemma lem:archimedean-dichotomy-and-characters—including its separate real and nonreal completion cases—gives \(\eta=\chi_x\) or \(\eta=\overline{\chi_x}\). Equation (10) is precisely the required pointwise convergence. Since the argument began with an arbitrary subnet, the lemma follows. ∎

# lemma lem:philippon-fixed-type

## statement

Fix finitely many blocks of \(N_i\geq1\) complex variables and block degrees \(d_i\geq0\). On the punctured coefficient vector space of nonzero multihomogeneous polynomials \(F\) of this type, Philippon's logarithmic sphere measure \(\operatorname{ph}(F)\) is finite, real-valued, continuous, homogeneous, and invariant under complex conjugation:

\[
 \operatorname{ph}(\lambda F)=\log|\lambda|_\infty+\operatorname{ph}(F),
 \qquad
 \operatorname{ph}(\overline F)=\operatorname{ph}(F).
\tag{12}
\]

Moreover, for a constant depending only on the fixed type, for instance

\[
 C=2\sum_i\log(N_i+1)d_i,
\]

one has

\[
 \left|\operatorname{ph}(F)-\log\|F\|_{\max}\right|\leq C.
\tag{13}
\]

## proof

We first list, with complete statements and identifiers, the only two external results used in the proof.

1. **D'Andrea--Krick--Sombra fixed-type estimate.** For a nonzero complex multihomogeneous polynomial \(F\) in fixed blocks and fixed multidegrees, its Philippon measure is the integral of \(\log|F|\) on the product of unit spheres plus the harmonic correction of Definition 2.33, and

   \[
   0\leq\operatorname{ph}(F)-m(F)
      \leq\sum_i\log(n_i+1)\deg_i(F),
   \]

   while the grouped-variable Mahler estimate of Lemma 2.32 bounds

   \[
   |m(F)-\log\|F\|_{\max}|
      \leq\sum_i\log(n_i+1)\deg_i(F).
   \]

   Consequently (13) holds, in particular with the harmless displayed \(C\). Source identifiers: paper_id=DAndreaKrickSombra_1103.4561; Carlos D'Andrea, Teresa Krick, Martín Sombra, *Heights of varieties in multiprojective spaces and arithmetic Nullstellensätze*; arXiv_id=1103.4561v2; theorem_id=Lemma 2.32, Definition 2.33, equations (2.34)--(2.35). Here their \(m(F)\) is Haar Mahler measure, their sphere measures have total mass \(1\), and their \(\|F\|_\infty\) is the maximum coefficient modulus. These are exactly the notions used here; no geometric hypothesis on \(F\), beyond nonzeroness and fixed multihomogeneous type, is present.

2. **Zhang's continuity theorem.** For the standard Hermitian space \(\mathcal E=\mathbf C^{N+1}\), the Chow metric defined in Section 1.5 on the line bundle \(\mathcal O(1)\) over

   \[
   \mathbf P\bigl[(\operatorname{Sym}^{d}\mathcal E)^{\otimes(n+1)}\bigr]
   \]

   is continuous and positive; in particular its defining logarithmic spherical integral is continuous on the nonzero projective coefficient space of that equal type. Source identifiers: paper_id=Zhang1996; Shouwu Zhang, *Heights and reductions of semi-stable varieties*, Compositio Math. 104 (1996), 77--105; theorem_id=Theorem 3.6(1), with the Chow metric of Section 1.5; arXiv_id=not applicable. Zhang's proof, on pp. 94--96, writes the local family as a holomorphic polynomial in one sphere coordinate, applies Weierstrass preparation, obtains local integrability and parameter continuity of its logarithm, and then uses Fubini and a partition of unity. Thus the theorem concerns the entire punctured equal-type coefficient space, not only smooth hypersurfaces.

We now explain why Zhang's equal-type statement applies to arbitrary fixed block sizes and multidegrees. Let \(m\) be the number of blocks, put \(Q=\max_iN_i\), and \(D=\max_i d_i\). If \(D=0\), the coefficient space is one-dimensional and continuity is immediate from \(\operatorname{ph}(a)=\log|a|\), so assume \(D>0\). Pad the \(i\)-th block with \(Q-N_i\) unused variables and define the injective linear fixed-monomial map

\[
 \iota(F)=F\prod_i U_{i0}^{D-d_i}.
\tag{14}
\]

It takes the original coefficient space into the equal-type space with \(m\) blocks, \(Q\) variables per block, and degree \(D\) in every block; this is Zhang's space with \(n+1=m\) and \(N+1=Q\).

We check rather than assume how the spherical integrals change. On the unit sphere in \(\mathbf C^Q\), write the first \(N_i\) coordinates as \(r_i\xi_i\), where \(0<r_i\leq1\) off a null set and \(\xi_i\in S^{2N_i-1}\). By unitary invariance, \(\xi_i\) is uniformly distributed on that sphere and is independent of the radial variable. Multihomogeneity gives

\[
 \log|\iota(F)|
 =\log|F(\xi_1,\ldots,\xi_m)|
   +\sum_i\bigl(D\log r_i+(D-d_i)\log|\xi_{i0}|\bigr).
\tag{15}
\]

The expectations of \(\log r_i\) and \(\log|\xi_{i0}|\) are finite (their radial densities are powers at \(0\) and \(1\)). After also subtracting the two fixed harmonic corrections in Definition 2.33, (15) yields

\[
 \operatorname{ph}_{\mathrm{equal}}(\iota(F))
 =\operatorname{ph}_{\mathrm{original}}(F)+\kappa,
\tag{16}
\]

where \(\kappa\) depends only on \((N_i,d_i)\), not on \(F\). Zhang's theorem, restricted along the projectivization of \(\iota\), therefore proves projective coefficient continuity for the original type. Homogeneity, which follows directly by adding the constant \(\log|\lambda|\) inside the normalized sphere integral, lifts this to continuity on the punctured coefficient vector space.

The same sphere formula proves both identities in (12): scalar multiplication adds \(\log|\lambda|\), while coordinatewise conjugation preserves the product of spheres, their invariant probability measures, and \(|F|\). The logarithmic singularity of a nonzero polynomial is locally integrable, as is also built into Zhang's Weierstrass proof, so the value is finite and real. Finally, (13) follows from external input 1. ∎

# theorem thm:weighted-philippon-gauss-continuity

## statement

Let \(A\) be a Banach ring and let \(U\subset \mathcal M(A)\) be open.  Fix
finitely many blocks of variables
\[
 \mathbf U_i=(U_{i0},\ldots,U_{i,N_i-1}),\qquad N_i\ge 1,
\]
and nonnegative block degrees \(d_i\).  Let \(S\) be a finite set of
multiexponents of block degree \((d_i)_i\), let \(w_\alpha\in\mathbf R\)
for \(\alpha\in S\), and let \(c_\alpha\in\mathcal O(U)\).  Assume that the
coefficient tuple is nowhere zero:
\[
 \max_{\alpha\in S}|c_\alpha(x)|_x>0\quad\text{for every }x\in U.
\]
It is enough to prove the assertion after shrinking to a rational domain on
which all \(c_\alpha\) belong to one Banach localization of \(A\).

Put
\[
 \rho(x)=\frac{\log\max\{1,|2|_x\}}{\log 2}.
\]
If \(\rho(x)=0\), define
\[
 \Phi(x)=\max_{\alpha\in S}
            \bigl(\log|c_\alpha(x)|_x+w_\alpha\bigr),
 \qquad \log 0=-\infty.
\tag{1}
\]
If \(\rho(x)>0\), choose a complex character
\(\chi_x\) representing the Archimedean seminorm, so that
\[
 |a|_x=|\chi_x(a)|_\infty^{\rho(x)}.
\]
The character is unique up to complex conjugation.  Define
\[
 F_x=\sum_{\alpha\in S}
       \chi_x(c_\alpha)e^{w_\alpha/\rho(x)}\mathbf U^\alpha
\]
and
\[
 \Phi(x)=\rho(x)\operatorname{ph}(F_x),
\tag{2}
\]
where \(\operatorname{ph}\) is Philippon's logarithmic sphere measure with
the harmonic correction in D'Andrea--Krick--Sombra, Definition 2.33.

Prove that \(\Phi\) is a well-defined continuous real-valued function on
\(U\).

Also prove the line-valued version.  If \(\mathscr L\) is a line bundle on
\(U\), and
\[
 R=\sum_\alpha r_\alpha\mathbf U^\alpha
       \in \mathscr L\otimes \mathbf Z[\mathbf U]
\]
has a nowhere-zero fibrewise coefficient tuple, write \(R=eF_e\) in a local
frame \(e\).  Prove that \(\Phi_e:=\Phi(F_e)\) satisfies
\[
 e'=ue\quad\Longrightarrow\quad
 F_{e'}=u^{-1}F_e,
 \qquad
 \Phi_{e'}=\Phi_e-\log|u|,
\tag{3}
\]
and hence defines a continuous additive metric on \(\mathscr L\).

Do not claim that this lemma solves Pille--Schneider Question 4.9.  It is
only one analytic input for that problem.

## proof

The proof is local on \(U\). Fix a rational domain \(V\subset U\) on which all coefficients are elements of one Banach localization \(A_V\). If a coefficient is written using a localization denominator \(g\), then \(g\) is a unit on \(V\); include \(g\) and \(g^{-1}\), as well as all coefficient elements, in the finitely generated ring

\[
 B=\mathbf Z[c_\alpha,\text{ all required denominators and their inverses}]\subset A_V.
\tag{17}
\]

For every net in \(V\), pointwise convergence of the corresponding seminorms on \(A_V\) restricts to pointwise convergence on \(B\). Evaluation of \(g^{-1}\) is harmless because \(|g|>0\) on the rational domain and \(|g^{-1}|=|g|^{-1}\). We prove continuity on \(V\); such domains cover \(U\).

Define on all of \(V\)

\[
 M(x)=\max_{\alpha\in S}\bigl(\log|c_\alpha(x)|_x+w_\alpha\bigr)
     =\log\max_{\alpha\in S}\bigl(e^{w_\alpha}|c_\alpha(x)|_x\bigr).
\tag{18}
\]

The quantity inside the last logarithm is a finite maximum of continuous nonnegative functions and is everywhere positive by the nowhere-zero hypothesis. Hence \(M\) is a finite continuous real-valued function, even when some individual coefficients vanish.

We first establish well-definedness on the Archimedean locus. Lemma lem:archimedean-dichotomy-and-characters, applied to \(A_V\), supplies a representing character; only its restriction to the finite-type algebra \(B\) enters \(F_x\). The coefficient tuple is not zero, so \(F_x\ne0\), and Lemma lem:philippon-fixed-type makes \(\operatorname{ph}(F_x)\) finite. Two representing characters are conjugate. Since every \(w_\alpha\) is real, changing the character conjugates \(F_x\), and (12) leaves its Philippon measure unchanged. Thus (2) is independent of all choices. Formula (1) is finite by (18), so \(\Phi\) is everywhere real-valued.

We next prove continuity at a point \(x\in V\) with \(\rho(x)>0\). Let \(x_\lambda\to x\) be an arbitrary net. Continuity of \(y\mapsto|2|_y\) gives \(\rho(x_\lambda)\to\rho(x)\), so eventually all \(x_\lambda\) are Archimedean and their exponents are bounded below by, say, \(\rho(x)/2\). Choose arbitrary representing characters \(\chi_\lambda\). Apply Lemma lem:finite-type-character-topology to their restrictions to \(B\). From every subnet we can extract a further subnet converging pointwise on \(B\) either to \(\chi_x\) or to \(\overline{\chi_x}\). Along such a further subnet,

\[
 \chi_\lambda(c_\alpha)e^{w_\alpha/\rho(x_\lambda)}
 \longrightarrow
 \chi_x(c_\alpha)e^{w_\alpha/\rho(x)}
\]

for every \(\alpha\), or all limits are simultaneously conjugated. Coefficient continuity and conjugation invariance from Lemma lem:philippon-fixed-type then give

\[
 \rho(x_\lambda)\operatorname{ph}(F_{x_\lambda})
 \longrightarrow
 \rho(x)\operatorname{ph}(F_x).
\]

A net converges to a point if every subnet has a further subnet converging to that point: otherwise a subnet can be chosen entirely outside one neighborhood of the proposed limit. Therefore the original net of \(\Phi\)-values converges, proving continuity wherever \(\rho>0\).

It remains to cross the boundary. For \(\rho(x)>0\), the maximum coefficient modulus of \(F_x\) satisfies exactly

\[
\begin{aligned}
 \rho(x)\log\|F_x\|_{\max}
 &=\rho(x)\max_\alpha
       \left(\log|\chi_x(c_\alpha)|_\infty
                    +\frac{w_\alpha}{\rho(x)}\right)\\
 &=\max_\alpha\bigl(\log|c_\alpha(x)|_x+w_\alpha\bigr)
 =M(x).
\end{aligned}
\tag{19}
\]

This remains exact when some coefficients are zero, with \(\log0=-\infty\). The fixed-type estimate (13) and (19) give

\[
 |\Phi(x)-M(x)|
 =\rho(x)\left|\operatorname{ph}(F_x)-\log\|F_x\|_{\max}\right|
 \leq\rho(x)C.
\tag{20}
\]

Let now \(x_\lambda\to x\) with \(\rho(x)=0\). If \(x_\lambda\) is non-Archimedean, then \(\Phi(x_\lambda)=M(x_\lambda)\). If it is Archimedean, (20) applies. In either case,

\[
 |\Phi(x_\lambda)-M(x_\lambda)|\leq C\rho(x_\lambda).
\]

Since both \(M(x_\lambda)\to M(x)\) and \(\rho(x_\lambda)\to0\), we obtain \(\Phi(x_\lambda)\to M(x)=\Phi(x)\). This proves boundary continuity. Conversely, a net of non-Archimedean points has \(\rho=0\) identically and cannot converge to a point with \(\rho>0\), by continuity of \(\rho\). We have now proved continuity on \(V\), and hence locally on all of \(U\).

For later use, verify homogeneity pointwise. If \(\lambda\ne0\), then in the non-Archimedean regime

\[
 \Phi(\lambda F)
 =\max_\alpha(\log|\lambda c_\alpha|+w_\alpha)
 =\log|\lambda|+\Phi(F).
\tag{21}
\]

In the Archimedean regime, \(F_x(\lambda F)=\chi_x(\lambda)F_x(F)\), and (12) gives

\[
 \Phi(\lambda F)
 =\rho\log|\chi_x(\lambda)|+\Phi(F)
 =\log|\lambda|_x+\Phi(F).
\tag{22}
\]

Thus the same formula holds in both regimes. It also shows that changing a localization presentation by a unit does not change the intrinsically defined value.

We explicitly run the five requested tests.

1. On the hybrid spectrum of \(A=\mathbf Z\), take \(F=1+U+V\) (equivalently its degree-one homogenization) and zero weights. Its maximum coefficient logarithm is \(M=0\). At an Archimedean point of exponent \(\rho>0\), (20) gives \(|\rho\operatorname{ph}(F)|\leq\rho C\), so the value tends to \(0\), exactly the Gauss maximum-coefficient value, as \(\rho\downarrow0\).

2. If some coefficients vanish at a limit point, (18) still proves continuity because at least one term \(e^{w_\beta}|c_\beta|\) remains positive there. For example, the tuple \((t,1)\) may specialize to \((0,1)\); the maximum remains a positive continuous function. If all coefficients were allowed to vanish, even \(F_t=tU_0\) would have \(\operatorname{ph}(F_t)=\log|t|+\text{constant}\to-\infty\), showing exactly why the hypothesis is needed.

3. For a real Archimedean character, \(F_x\) has real coefficients and the definition uses its complexification on the complex unit spheres. The two possible complex representatives are conjugate, and (12) proves that they give the same value. Thus real fibers agree with complexification.

4. No sign restriction on the weights was used. For every fixed \(\rho>0\), \(e^{w_\alpha/\rho}\) is a finite positive number for every real \(w_\alpha\), while (19)--(20) are exact and \(C\) is independent of all weights. Hence arbitrary positive and negative weights are covered.

5. The frame-change sign follows from the inverse transition function, as we now verify; the one-coefficient, degree-zero case reduces it to the ordinary identity \(\log|u^{-1}r|=\log|r|-\log|u|\).

Indeed, let \(R=eF_e\) in a local frame of \(\mathscr L\). On an overlap with \(e'=ue\), where \(u\) is a nowhere-vanishing analytic function,

\[
 eF_e=e'F_{e'}=ueF_{e'},
 \qquad\text{hence}\qquad F_{e'}=u^{-1}F_e.
\tag{23}
\]

Applying the homogeneity formula (21)--(22) pointwise gives

\[
 \Phi_{e'}=\Phi(u^{-1}F_e)=\Phi_e-\log|u|.
\tag{24}
\]

Each \(\Phi_e\) is continuous by the scalar-valued result, and (24) is exactly the transition rule for an additive metric in the convention of the statement. The local functions therefore glue to a continuous additive metric on \(\mathscr L\).

The argument proves only the stated analytic continuity and metric assertion. In particular, it does not purport to solve Pille--Schneider Question 4.9. ∎
