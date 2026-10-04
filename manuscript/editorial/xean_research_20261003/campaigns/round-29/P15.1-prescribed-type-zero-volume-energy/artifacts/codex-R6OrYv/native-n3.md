Analytic counterexample to extending n1's class-convergent auxiliary-path limit to every finite-energy unbounded potential; it is not a refutation of P15.1 in its entirety.

Use X=P1xP1, normalized Fubini–Study kappa, theta=p1*kappa, psi=0, and the fixed potential u=p1*v from n2, with v<=0 and v(z)=-b(-log|z|)^a near zero, 0<a<1/2. This is a nef pseudoeffective zero-volume class since theta^2=0, and the actual reference has d=1, M_1=1. The potential has finite degree-one joint energy and full mass, as proved by the radial density and flux calculation in n2.

Let rho_epsilon=exp(-epsilon^(-2/a)). Choose a nonnegative smooth two-form beta_epsilon of integral 1 supported in |z|<rho_epsilon, by rescaling a disk bump and extending by zero. On P1 it is closed. Put kappa_epsilon=(kappa+beta_epsilon)/2 and omega_epsilon=p1*kappa_epsilon+p2*kappa. These are smooth Kähler forms with precisely one fixed cohomology class lambda, because integrals determine H^2(P1,R). No smooth convergence occurs. Keep u_epsilon=u exactly.

Write S=kappa+ddc v, positive of mass 1 and without a polar atom. Then T_u=p1*S, and T_u+epsilon omega_epsilon is positive. For each fixed epsilon, v is integrable against the smooth kappa_epsilon, and against S and kappa by n2. Every positive-perturbation joint weighted integral is finite. Nonpluripolar products agree with the following rank-one expansions off the polar fiber and have no polar mass:
 anchor square =2epsilon p1*(kappa+epsilon kappa_epsilon)p2*kappa;
 mixed term =epsilon p1*(S+kappa+2epsilon kappa_epsilon)p2*kappa;
 u square =2epsilon p1*(S+epsilon kappa_epsilon)p2*kappa.
The u square and anchor square both have mass 2epsilon(1+epsilon). Thus the fixed u is full-mass and finite-energy relative to every positive perturbation, not merely in the limiting degree-one theory.

Averaging the three weighted terms gives exactly
 E_epsilon,omega_epsilon(u)=2epsilon E_0,lambda(u)+2epsilon^2 integral v kappa_epsilon,
 E_0,lambda(u)=(1/2)integral v(S+kappa) finite.
This expansion is legitimate for the unbounded potential because each displayed weighted integral is finite at that fixed parameter; no unproved unbounded IBP is used.

On the bump support, -v>=b epsilon^(-2), and therefore integral v kappa_epsilon<=-(b/2)epsilon^(-2). Consequently
 E_epsilon,omega_epsilon(u)/(2epsilon)=E_0,lambda(u)+epsilon integral v kappa_epsilon -> -infinity.
Using instead the fixed smooth omega=p1*kappa+p2*kappa, the same expression tends to the finite E_0,lambda(u), because integral v kappa is fixed and finite. Both paths use exactly the same auxiliary class and exactly the same potential at every parameter.

This satisfies every ambient hypothesis and proves a failure of the proposed unbounded strengthening. It does not contradict the bounded theorem, which controls lower weighted coefficients by ||u-psi||_infty times bounded cohomological masses. Here all lower weighted coefficients are finite at each epsilon but fail uniform control. Even full relative top mass and finite positive-perturbation energy at every epsilon do not repair that failure. A further uniform-integrability condition, a restriction on representatives, or another limiting prescription would require its own theorem. No such condition is silently inserted into original P15.1. Complete calculations are in P15.1-argument.md and P15.1-partial.tex/PDF; no numerical simulation is needed.
