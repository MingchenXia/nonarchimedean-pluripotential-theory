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

Artifacts: whole-proof.md, P12.3-independent-paper.tex, source-ledger.md, coverage.md, scope-and-verdict.json, native-notes.json and reports. Rerun: python reader.py m --retain; python reader.py p --retain; python reader.py b --retain; python identity_audit.py; python bounded_diagnostics.py; python build_delivery.py; python final_audit.py. The paper is intentionally uncompiled; ROOT retains compilation and publication. Execution and hashes do not certify the mathematics.
