# Polarized Calabi–Yau finiteness: primary-source audit, 8 October 2026

The controlling source is Truong Dinh Dat, *A Pluripotential-Theoretic Approach to Finiteness of Polarized Calabi–Yau Manifolds*, arXiv:2610.00361v1, posted 30 September 2026. All 34 physical pages were actually read with complete selected text, seventeen individually displayed matching images, sequential notes and receipts. The font-extraction warning is retained; the formulas and qualifications were checked against the displayed pages. The acquisition and prepared-view flags remain frozen at zero reading credit. Bibliography reading does not recursively certify its external proofs.

The source explicitly presents a program, not a completed finiteness theorem. Its discussion on page 33 leaves capacity–perimeter and metric-to-projective-embedding estimates open. Those two bridges are not established elsewhere in the paper. This audit independently checks this source; findings in another paper by the same author are not used as evidence here.

## Conventions and uniformity

The source uses \(dd^c=i\partial\bar\partial\), which is \(2\pi\) times the book's binding operator. Its volume notation is \(\int\omega^n\), rather than the Riemannian convention \(\int\omega^n/n!\). Theorem 4.6 writes \([\omega]=c_1(L)\), whereas Lemma 7.1 and Theorem 7.3 write \([\omega]=2\pi c_1(L)\). Page 28 correctly retains the latter convention:

$$
\int_M c_1(L)^n=(2\pi)^{-n}\int_M\omega^n.
$$

A suitable very ample power for each individual polarization does not give a common exponent over a varying family. A common exponent, a bounded ambient projective dimension and a bounded polarization volume are distinct data. Lemma 7.2 correctly gives degree \(q^n\int c_1(L)^n\) when the common power is very ample.

## Capacity and potential estimates

Theorem 3.1, pages 6–8, assumes an all-Borel-set uniform volume–capacity inequality with exponent \(\tau\). Its conclusion follows immediately with \(\alpha=\tau\) and \(C=C_0\). Thus the implication is valid but supplies no new family-uniform estimate. The additional uniform coordinate-cover and approximation assertions are not proved by a total-mass bound alone. Remarks 3.2–3.3 preserve the substantive problem of obtaining uniformity from polarized Calabi–Yau data.

Theorem 4.1 and Corollary 4.3 have gaps in their displayed iteration proof. Hölder gives the exponent

$$
q=\frac p{p-1},\qquad \delta=\frac{\tau}{q}.
$$

The proof needs \(\delta>1\). An assumed inequality for one specified \(\tau\) cannot be upgraded to a larger exponent merely because \(p>n/m\). The exact tuple \(n=3,m=1,p=4,\tau=6/5\) satisfies the printed bounds but gives \(\delta=9/10\). This diagnoses the proof; it is not a counterexample to every possible repaired potential estimate.

The page 11 truncation is also incorrect as stated:

$$
v_{s,t}=\max\{(u+t)/(t-s),-1\}.
$$

At \(s=1,t=2,u=-5/2\), one has \(u<-t\) but \(v_{s,t}=-1/2\), rather than \(-1\). On \(u\ge -s\), the displayed function is at least 1. A claimed canonical normalization does not establish the all-test capacity comparison, and multiplication by \(1/(t-s)>1\) need not preserve the background subharmonicity constraint. Lemma 4.2's abstract extinction conclusion is standard under its actual superlinear recursive hypothesis, but does not validate the preceding comparison. An empty strict sublevel can be obtained from upper semicontinuity and positive capacity of any nonempty open set, once extinction has genuinely been proved.

## Geometric estimates

The isoperimetric formula on page 5 needs a half-volume restriction or the minimum of the volumes of a domain and its complement. Applied to \(E=M\), the literal all-domain formula has positive left side and zero boundary area.

Theorem 4.6, pages 13–15, gives a valid Sobolev-cutoff/Bishop–Gromov argument under the explicitly assumed critical uniform Sobolev bound. The potential and reference-volume hypotheses are unused in this argument. In real dimension \(d=2n\), the cutoff and doubling estimates give

$$
V(r)^{(d-2)/d}
\le S(G^2r^{-2}+1)V(2r)
\le S2^d(G^2+1)r^{-2}V(r)
\quad(0<r\le1),
$$

and hence \(V(r)\ge [S2^d(G^2+1)]^{-d/2}r^d\). The Bishop–Gromov and cutoff foundations remain classical attributed inputs; this proves no uniform Sobolev inequality from polarization data alone.

Theorem 5.1's printed diameter proof, pages 16–17, reverses Bishop–Gromov when \(R>r_0\):

$$
\frac{V(R)}{R^d}\le\frac{V(r_0)}{r_0^d}.
$$

Its resulting numerical bound independent of the noncollapse scale is false. A flat rectangular elliptic torus with sides \(1/10\) and \(10\) has area 1 and diameter \(\sqrt{100+1/100}/2>5\). For \(r_0=1/40\), every small ball has area \(\pi r^2\), while the printed bound is \(2/\sqrt{\pi}<1.13\). At radius 1 the ball's area is at most \(1/5\), directly illustrating the opposite direction of the ratio inequality.

This does not refute the theorem's correctly scale-dependent conclusion. A direct packing argument gives

$$
\operatorname{diam}M\le\frac{2V_0}{\kappa r_0^{d-1}}.
$$

Along a minimizing geodesic of length \(L\), the \(\lfloor L/(2r_0)\rfloor+1\) open radius-\(r_0\) balls centered \(2r_0\) apart are disjoint. Their total volume is at most \(V_0\), so \(L<2V_0/(\kappa r_0^{d-1})\). This elementary argument needs connectedness and the stated ball bounds, rather than the reversed comparison.

Theorem 5.2's generic PDE interface needs care. The proof invokes a \(C^2\) norm of \(\log F\), every fixed Hölder exponent, and fourth potential derivatives for curvature, while the statement initially supplies a bare \(C^k\) density norm. For low \(k\), those derivative inputs are not explicitly provided by that generic argument. Ricci-flatness can offer additional local pluriharmonic log-determinant structure, but that argument must be supplied or the hypotheses strengthened; this audit does not infer a counterexample to the Ricci-flat statement.

Theorem 6.1 explicitly assumes diameter, noncollapse and all curvature-derivative bounds. Its smooth compactness conclusion uses the classical injectivity-radius and Cheeger–Gromov foundations. The harmonic-coordinate equation on page 21 should use the two-index Ricci tensor, not the printed two-index Rm symbol. Parallel complex structures and their Kähler forms pass to a smooth limit under the stated convergence. Smooth compactness with eventual diffeomorphisms already gives finitely many diffeomorphism types by a distinct-types sequence argument; algebraic embedding is not required for that particular consequence.

## Sections, schemes and topology

Lemma 7.1, pages 22–24, falsely bounds the sum of individual section suprema by the pointwise Bergman bound. Its proof admits the missing implication and adds a stronger hypothesis absent from the statement. On \(\mathbb P^1\) with \(\mathcal O(1)\), the Fubini–Study metric and \(L^2\) volume \(V\), an orthonormal basis has squared pointwise norms

$$
\frac2V a,\quad\frac2V(1-a),\qquad
a=\frac{|z_0|^2}{|z_0|^2+|z_1|^2}.
$$

The pointwise sum is \(2/V\), whereas the sum of the two suprema is \(4/V\). The two diagonal \(L^2\) integrals are \(1/2\) before normalization, and the angular cross integral is zero. This is a counterexample in the lemma's general compact Kähler scope, not a Calabi–Yau counterexample.

With a separate volume upper bound, integration does give \(h^0\le C_BV_0\), and then the larger bound \(\sum\|s_\alpha\|_\infty^2\le C_B^2V_0\). An upper Bergman bound does not prove a common very ample power, a Bergman lower bound or tangent separation. Theorem 7.3 assumes its common \(q,N\) and embedding data. Its basis-sup hypothesis without orthonormality can be satisfied by scalar rescaling, which leaves the projective map unchanged. Its result concerns the powered polarization.

Lemma 8.1, pages 29–31, and the preliminary formulation on pages 5–6 are false for their literal arbitrary-projective-scheme scope. A fixed linear \(\mathbb P^3\) together with \(k\) disjoint reduced points outside it in \(\mathbb P^4\) has dimension 3, top degree 1, and Hilbert polynomial

$$
P_k(t)=\binom{t+3}{3}+k.
$$

Thus the polynomials are infinite in number. The same example has \(h^0(\mathcal O_X)=1+k\), while the degree-zero homogeneous-coordinate-ring dimension is 1; the two Hilbert functions used in the proof do not agree in every degree. Macaulay growth and Gotzmann regularity do not bound arbitrary lower-dimensional or embedded contributions solely from top degree. The leading coefficient alone does not bound the other coefficients. This example does not refute an appropriately restricted classical boundedness input for smooth connected pure-dimensional projective varieties. Theorem 8.2 needs that correct input rather than the printed overly broad lemma.

Theorem 8.3 explicitly assumes finitely many Hilbert polynomials. Its conditional topological consequence can use a finite smooth stratification of the reduced parameter bases, followed by proper smooth Ehresmann fibrations on the connected strata. The open locus of smooth fibers in a Hilbert scheme need not itself be a complex manifold; the proof on pages 32–33 omits this interface. The universal projective flat family supplies properness. External Hilbert-scheme, stratification and Ehresmann foundations remain attributed and are not recursively certified here.

## Conditional exponent bookkeeping and admission decision

For the same admissible half-volume domains, suppose separately that \(v\le A c^\tau\), \(c\le B p^\sigma\), and \(v\le V_0\). Then

$$
v^{1/(\sigma\tau)}
\le A^{1/(\sigma\tau)}B^{1/\sigma}p.
$$

This implies dimension-\(d\) isoperimetry when \(\sigma\tau\ge d/(d-1)\), with the additional factor \(V_0^{(d-1)/d-1/(\sigma\tau)}\). This is elementary conditional algebra. No capacity–perimeter estimate is proved or inferred from a volume–capacity bound alone.

Admit only the stated program, explicit uniformity requirements, attributed classical conditional interfaces and directly checked elementary diagnostics. Do not import the printed general Hessian estimate, arbitrary-scheme Hilbert lemma, numerical diameter bound or Bergman sum bound as proved results. A qualified Chapter 62/App. L explanation may make the independent capacity, Sobolev, curvature and projective inputs clearer.

The active 4,642-page book, all 425 TeX inputs, both bibliographies and native catalogue/editor remain unchanged at this source checkpoint. The 42 atoms/twelve formal problems retain status: general BJ22 critical homogeneous Siu/envelopes OPEN, LPWZ density UNVERIFIED. The last complete ordered whole-book reading remains 4 October. No original general theorem, independent-model receipt or completed Calabi–Yau finiteness theorem is asserted.
