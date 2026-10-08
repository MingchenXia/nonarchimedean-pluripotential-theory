# n7. Energy and capacity do not recognize increasing geometric limits

Use only the entire qualified G331, B341, E350 and n1. On surfaces write B=F>=0 for the symmetric mixed form and E(u)=-F(u,u)/2. The sign B=-F is incorrect. E350 is used within its actual primary-model, reduced-boundary, p=n-1, all-support, specified-limit and finite-reference-moment qualifications. No arbitrary increasing-D closure or general measurable-net convergence is supplied by that grant.

In k[x,y]_(x,y), maximal gauge, let I_j=(x,y^j) and u_j=-v(I_j)/j. The I_j are graded, and the profiles increase to zero except at q with support (x), where the limit is -1. Monomial valuations v_L(x)=L,v_L(y)=1 tend to q, so that increasing limit is not USC and is outside D. Its regularization is zero, a valid envelope, so it does not refute normal CE.

For ALL r,s>=0 the staircase of m^r I_j^s at x-exponent a<r+s has threshold r+s-a+(j-1)max(0,s-a). Summing gives

length R/(m^r I_j^s)=r(r+1)/2+rs+j s(s+1)/2.

Thus e(m,I_j)=1, e(I_j)=j, F(u_j,u_j)=1/j, E(u_j)=-1/(2j), and mu(u_j) has mass 1/j. For EVERY capacity input phi in D with -1<=phi<=0, order gives F(phi,phi)<=1. E350 conditional Cauchy gives F(u_j,phi)<=1/sqrt(j). Bounded test pairing and Markov's inequality imply Cap{-u_j>epsilon}<=1/(epsilon sqrt(j)). Energy, mass and capacity convergence all occur without making the exact increasing limit geometric.

On the normal parity surface R=k[X,Y,Z]_(X,Y,Z)/(XY-Z^2), all characteristics, put a0=v(X),b0=v(Y). The relation gives min(a0,b0)=v(m)=1 and v(Z)=(a0+b0)/2 when finite. Let q have support (X,Z), b0=1. For I_n=(X^n,XY^(n-1),Y^(2n)), u_n=-v(I_n)/n is -1 if a0<=b0 and -min(1+(a0-1)/n,2) otherwise. It increases to h=-1 off q, h(q)=-2. Valuations a0=L,b0=1 tend to q, so h is non-USC and outside D, while h*=-1 is continuous geometric.

The blowup of m is regular: the X chart has Z=Xz', Y=Xz'^2 and polynomial coordinates; similarly for Y; the Z chart has x'y'=1 and is regular. Its exceptional conic has degree two over every field. The qualified geometric reference comparison yields mu(-1)=2 delta_(ord_m). Let z_j=-v((X)+m^j)=-min(v(X),j). This is an actual decreasing C-sequence, so z=-v(X) is in D. Finite energy of z is NOT assumed. For EVERY admissible capacity phi, scalar form order gives F(z_j,phi)<=F(z_j,-1)=2. The test pairing is the integral of min(v(X),j) against mu(phi). Ordinary SEQUENTIAL Borel monotone convergence yields integral v(X) dmu(phi)<=2. Markov and the supremum over ALL phi give Cap{a0>T}<=2/T and Cap{q}=0. The error set {-1-u_n>epsilon} is {a0>1+n epsilon} for 0<epsilon<1, and empty for epsilon>=1. Thus h is a capacity limit and continuous outside open sets of arbitrarily small capacity, yet remains outside D.

There is an exact universal parity length formula, not just a leading-area estimate:

length R/I_n^k=(n^2+n)k^2+(n^2-n+2)k, n,k>=1.

Identify the ring with k[s^2,st,t^2]. Pair columns with s-exponent 2p and 2p+1, 0<=p<nk. The minimum t-threshold is even and obtained by maximizing 4n i+(2n+2)j subject to i,j>=0, i+j<=k, ni+j<=p. For p<k the maximum is i=0,j=p, giving threshold 4nk-(2n+2)p. For n>1 and k<=p<nk put i0=floor((p-k)/(n-1)), q=p-k-(n-1)i0 in [0,n-2]. When i<=i0 the slot constraint binds and the objective increases in i; above it the exponent constraint binds and the objective decreases. The next candidate differs by 4n-(2n+2)(n-q)<=-4, so the maximum is i0,j=k-i0 and threshold 2(n-1)(k-i0). Each even/odd column pair contributes exactly this even threshold, since their allowed t exponents have opposite parity. Summing p<k gives (3n-1)k^2+(n+1)k; summing the remaining k blocks of length n-1 gives (n-1)^2 k(k+1). Their sum is the formula. For n=1 the second range is empty and the first gives 2k^2+2k.

It follows that e(I_n)=2n^2+2n, F(u_n,u_n)=2+2/n, and E(u_n)=-1-1/n. The semigroup count of degree <2k gives length R/m^k=k^2 and e(m)=2. These are universal arguments with explicit signs. The own finite program checks small exponents only and is not their proof.

Artifacts: n7.md, finite_diagnostics.py, evidence/finite-diagnostics.json and whole-proof.md. Rerun: python finite_diagnostics.py; python build_delivery.py; python final_audit.py. Neither null capacity, bounded energy, quasicontinuity, dense generic equality nor an increasing supremum recognizes an arbitrary function as D.
