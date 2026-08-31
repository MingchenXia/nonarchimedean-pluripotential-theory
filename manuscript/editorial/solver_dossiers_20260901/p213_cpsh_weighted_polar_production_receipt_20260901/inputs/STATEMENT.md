## 1. Scope, notation, and the proposed conclusion

Let X be a boundaryless, locally differentially separated tropical space of level n>=1 in the sense of CLD, with its canonical positive closed integration current delta_X. All sheaves, ordinary smooth forms, positivity and compact-test topologies are those of CLD. Local differential separation supplies the compact smooth partitions, positive test majorants and Radon-measure interpretation used below (CLD 6.5.2 and 7.2.4–7.2.12). The analytic spaces in Section 8 have this property by CLD 15.2.4. Write dd=d'd''. The symbol CPsh means the least subsheaf of real continuous functions containing smooth psh functions and stable under local uniform closure (CLD 8.1.7–8.1.8), NOT merely the first locally approchable stage.

The elementary calculus input consists of CLD 8.5.1, 8.5.5, 8.7.2 and 8.8.4–8.8.5: positivity of dd(uS) for continuous CPsh u and positive closed S, continuity with uniformly converging continuous coefficients and positive currents, and the dpsh extension. The required convex composition is proved directly from CPsh minimality in Section 2; the proof does not need to identify every current-positive continuous function with CPsh or collapse its hierarchy. None of these inputs is the weighted polar estimate to be proved.

Here is the fixed-neighbourhood weighted assertion. Let Y be an ordinary open in X, let rho be smooth psh on Y, and suppose for some delta>0 that

    K_delta={rho<=delta} is compact in Y,
    U={rho<0} is nonempty.

All functions u_1,...,u_k are CPsh on a neighbourhood of K_delta, and V is a SMOOTH psh function on a neighbourhood of K_delta, negative on U. In particular V has no uncontrolled boundary singularity at closure(U). Set r=max(-rho,0), theta=dd rho, eta=d'rho wedge d''rho. Fix an integer a>=4. For 0<=k<=n put

    beta_k = r^(k+a) theta^(n-k)
             +(k+a) r^(k+a-1) eta theta^(n-k-1),          (1.1)

omitting the second summand when k=n. These are compactly supported C^2 forms; the product notation with currents means the coefficient-measure pairing explained below. Put

    J_k = integral (-V) beta_k wedge dd u_1 wedge ... wedge dd u_k.

The claim is

    J_k <= C(k,a) product_{j=1}^k ||u_j||_U
                       integral (-V) beta_0,             (1.2)
    C(0,a)=1,
    C(k,a)=product_{j=1}^k
                  [4e (j+a)(j+a+1)/(j+a-1)].

This is the same constant as (4e)^k a^(-1)(k+a)(a+2)...(a+k+1) for k>=1. The restriction a>=4, and the requirement that V be smooth near closure(U), are deliberate safe strengthening of the hypotheses printed in CLD 8.4.3.

Assume further that every point has arbitrarily small neighbourhoods with such a smooth psh relatively compact sublevel. Let 0<=m<=n. If u_1,...,u_m belong to the FULL CPsh sheaf, V is locally approchable psh and locally integrable for canonical smooth top-form measures, and alpha is any ordinary smooth (n-m,n-m)-form, then

    |V| is locally integrable for the total variation of
    dd u_1 wedge ... wedge dd u_m wedge alpha.             (1.3)

Consequently this measure gives zero mass to the polar set {V=-infinity}.

For a good separated strict boundaryless pure n-dimensional Berkovich space over ANY complete field K, including a trivially valued one, Section 8 constructs the required local sublevels and applies the analytic log-pole argument. Thus the proposed analytic consequence is: for all continuous CPsh factors u_j the measure in (1.3) gives zero mass to every closed analytic subset of dimension <n.

The entire new argument is written below. No single local smooth approximation sequence for an arbitrary CPsh function is assumed. No unknown current is pulled back by a field extension or normalization. Scalar-current classification and P21.3 are not input theorems of this packet.

