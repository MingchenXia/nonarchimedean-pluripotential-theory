# Continuous Stieltjes radial equations and the full bounded dual

Use the actual quotient, bounded calculus and calibrated finite formulas reconstructed in n1-n2. The new result is an upper bound, and exact value, for the dual over EVERY v in the entire bounded C_theta. The constructed unbounded operator remains radial. No all-direction E1 recognition or full uniqueness is asserted.

Let H consist of right-continuous nonincreasing profiles h with 0<=h<=1, constant c on [0,1), and Z(h)=integral_0^infinity h^3<infinity. Put g_h(r)=integral_0^r h, u_h=u0-g_h(R), with its canonical value at R=infinity. Then h tends to zero. Let nu_h=-d(h^2) be the Stieltjes measure on [1,infinity), including a jump at 1. Its mass is c^2 and nu_h((t,infinity))=h(t)^2 for t>=1. The statements proved below are

MA(u_h)=(2-c^2)delta_o+xi_*nu_h=:mu_h,
B(u_h,u_k)=(2-cd)delta_o+xi_*[-d(hk)],
E(u_h+C)=-1/6-Z(h)/3+2C,
sup_{v in C_theta}(E(v)-integral v mu_h)=1/6+2Z(h)/3.

The first two measures are genuine locally bounded analytic products off y extended by zero at y, and also genuine full-mass nonpluripolar truncation limits. The last supremum is the FULL bounded dual, rather than a pencil or radial dual.

Choose compact finite step h_m from below: on [0,1) keep c, on nested dyadic partitions of [1,2^m) sample h at right endpoints, and put zero afterward. Refining the grid and enlarging the interval makes h_m increase to h at continuity points (indeed with right-continuous representatives everywhere at finite positive depths). Their primitives g_m increase to g_h, uniformly on each finite interval because integral_0^R |h-h_m| tends to zero. Thus u_m=u0-g_m(R) decrease to u_h, locally uniformly on X minus {y}. The boundedness of R on a compact subset of that complement follows because the closed bidiscs {R>=r} decrease to {y}; compactness gives a finite depth bound.

On W minus {y}, put a=max(log|w_1|,log|w_2|)<0. The local weight is phi(a)-1/6, where phi(a)=-g_h(-a). Its derivative is h(-a), nonnegative and nondecreasing in a, so phi is convex and nondecreasing. Composing with the maximum is convex. Near a zero of one coordinate the other has nonzero norm and the inactive coordinate is omitted. Convex smooth approximation on ordinary unit moment neighborhoods proves membership in the declared local bounded class. Outside W, the ordinary open {R<1} has u_h=u0+cD_1. Consequently the genuine local operator is already available everywhere off y; it is not assigned by an inverse measure convention.

By n2 the actual bounded measures are mu_m=(2-c^2)delta_o+xi_*[-d(h_m^2)]. Stieltjes tails converge on bounded depth intervals, with the usual tests at continuity endpoints. At a continuity depth r their tail above r is at most h(r)^2, tending to zero as r tends to infinity, uniformly in m. Finite partition approximation of a continuous test on [1,r], followed by discarding this tail, proves weak convergence on the depth line. Composing the test with the continuous actual analytic section xi gives weak convergence against every continuous analytic test on X. The finite initial mass and outside part converge exactly. The resulting pushforward is Radon: nu_h is finite and tight, compact depth intervals have compact continuous images in the Hausdorff X, and its tail can be discarded. The branch mass is c^2; there is no atom or escaped mass at y. Local product continuity off y identifies this weak measure with the already constructed analytic local product. This proves the first formula and total mass two. Polarize the finite formulas and pass locally uniformly and weakly for h_m k_m to get the second formula. Its branch masses are nonnegative since hk decreases, their total is cd, and the outside mass is 2-cd. Both tails vanish. These arguments give independence of the described approximants and any others converging locally uniformly with initial values and uniformly tight tails converging as stated.

The full-mass truncation recipe for continuous profiles requires an endpoint check. Take M>0. If g_h(infinity)<=M, then u_h is bounded; integral |h-h_m| tends to zero on the whole depth line, so u_m converge uniformly on X and its measure agrees with the bounded operator. If M<g_h(infinity), continuity and monotonicity give a unique finite positive r_M with g_h(r_M)=M. A plateau at level M cannot occur in this case: a nonnegative nonincreasing derivative that reaches zero stays zero, so such a plateau would have value g_h(infinity). Set h^M(t)=h(t) for t<r_M and zero for t>=r_M. Then g_{h^M}=min(g_h,M) and

u^M=u0-min(g_h(R),M)=max(u_h,u0-M)

is in C_theta. If r_M<1 this profile is outside H but is an allowed bounded profile: n2 proved all positive real cutoffs. Approximate h^M by finite step profiles with positive real cutoffs and integrate; the convergence is uniform globally since the support lies in [0,r_M]. On each ordinary neighborhood the same convex moment presentation, or a finite local max regularization, supplies smooth positive approximants. Near y the potential is exactly u0-M. This is a direct membership proof, independent of a global approximation theorem.

Its branch Stieltjes measure is nu_h restricted to depths below r_M, with the entire endpoint mass replaced by h(r_M-)^2 delta_{r_M}. This includes any original jump at that endpoint. For r_M<1 the endpoint mass is c^2. The outside part stays (2-c^2)delta_o. The strict open set {g_h(R)<M} is {R<r_M}; it excludes the entire clamp atom, including the original endpoint atom. Bounded locality therefore gives

1_{g_h(R)<M} MA(u^M)=1_{g_h(R)<M} mu_h.

As M increases these restricted measures increase to mu_h off y; their omitted tail is h(r_M-)^2, which tends to zero when g_h(infinity)=infinity. Thus their mass tends to two. In the bounded case sufficiently large M already gives the bounded operator. This proves the genuine nonpluripolar truncation recipe. For sufficiently large integers j, max(u_h+C,-j) differs from u_h+C only on W, where u0=-1/6, and equals the same clamp with M=j+C-1/6. Hence ordinary constant truncations give the identical recipe. For mixed products, clamp each slot and restrict to the intersection of the two strict unclamped sets. Locality gives the local B there; the omitted branch tail is bounded by h(r)k(r) at a common large depth and tends to zero. This proves mixed full mass as well, with no rigid atom.

The first energy integral is integral u_h theta^2=0. The second is integral u_h(theta wedge alpha_{u_h})=-1/6: the difference from u0 annihilates theta and A locally, exactly as in n2, and these reference measures are supported away from y. For the top measure u0=-1/6 on its support F and Tonelli gives

integral g_k(t) nu_h(dt)=integral_0^infinity k(t)h(t)^2 dt,
integral g_h(t) nu_h(dt)=Z(h).

These are integrals of nonnegative functions, so there is no infinity cancellation. The top energy integral is -1/3-Z(h). Thus the displayed energy is the genuine three-term energy in this domain, and also the limit of the bounded energies. Constants add twice their value.

For all h,k in H, Holder gives integral k h^2<=||k||_3 ||h||_3^2. It therefore justifies signed subtraction and differentiation of the cubic along every radial segment. With h_t=(1-t)h+tk and constants C_t=(1-t)C+tD,

d/dt E(u_{h_t}+C_t)=-integral(k-h)h_t^2+2(D-C)
                         =integral[(u_k+D)-(u_h+C)] mu_{h_t},
d^2/dt^2 E(u_{h_t}+C_t)=-2 integral(k-h)^2 h_t<=0.

The possible undefined difference of two infinite values at y is assigned zero on that null singleton. This proves every segment first variation and concavity WITHIN the radial class. It also proves energy monotonicity under pointwise order there, by integrating the first variation against a positive measure.

Decreasing continuity with variable constants has its own proof. Suppose u_{h_m}+C_m decreases pointwise and its energies are bounded below. Reading the potential at a fixed point outside F shows C_m decreases. The bound E_m<=-1/6+2C_m bounds C_m below; hence C_m decreases to finite C. Put delta_m=C_m-C. Then g_m-delta_m increases pointwise, is uniformly 1-Lipschitz and concave, and is bounded on each finite interval. Its limit is a finite concave primitive g with g(0)=0, constant derivative on [0,1), and derivative h_m -> h almost everywhere by concave secant inequalities. The energy bound and bounded constants bound Z_m; Fatou gives Z(h)<infinity. Primitive convergence is locally uniform. The canonical value at infinity is correct because sup_m sup_r(g_m(r)-delta_m)=sup_r sup_m(g_m(r)-delta_m).

To prove energy convergence, order gives g_m<=g+delta_m. For a nonnegative nonincreasing compact test a, Stieltjes integration by parts gives integral a h_m<=integral a h+delta_m a(0). Take a=h_m^2 1_{[0,L)} and let L tend to infinity. Since a(0)<=1, Holder gives

Z_m<=Z(h)^{1/3} Z_m^{2/3}+delta_m.

Boundedness and this inequality yield limsup Z_m<=Z(h); Fatou supplies the opposite liminf. Thus energies converge, including variable constants. Monotonicity gives r h_m(r)^3<=Z_m, so the common cubic bound gives uniformly vanishing squared measure tails. Stieltjes convergence and the preceding tightness argument yield weak MA continuity; two such slots yield mixed continuity by the product tail bound. No general all-direction decreasing theorem is inferred.

Comparison with variable constants is also intrinsic to this radial domain. Let f=g_h-g_k and b=C-D. Inside W the strict comparison set is the open depth set {f>b}; outside W it is present exactly if b<0. On a component interval (a,l) with positive finite contact endpoints, the right derivative at a is h(a)-k(a)>=0 and the left derivative at l is h(l-)-k(l-)<=0. Therefore the difference of branch masses on that OPEN interval equals

[h(a)^2-k(a)^2]-[h(l-)^2-k(l-)^2]>=0.

An infinite right endpoint contributes zero tails. For an initial interval at depth zero, if b=0 the same initial derivative sign holds. If b<0 its initial term c^2-d^2 need not be positive, but the included outside mass difference is d^2-c^2, exactly cancelling it. If b>0 there is no initial interval. Summing the countably many intervals proves mu_k{u_h+C<u_k+D}<=mu_h{u_h+C<u_k+D}. Open endpoints exclude their atoms, which explains the right/left tail convention. Both measures give y mass zero. This is not comparison with arbitrary potentials outside the radial domain.

For fixed L, {h in H:Z(h)<=L}, with C=0, is compact in the metric sum_{m>=1}2^{-m}min(1,sup_{[0,m]}|g_h-g_k|). Indeed the primitives are concave, nondecreasing, 1-Lipschitz and zero at zero. Diagonal extraction on rational depths gives uniform convergence on finite intervals. Secant inequalities give almost-everywhere derivative convergence, and Fatou preserves Z<=L. Choose the right-continuous representative of the limiting derivative. This proves compactness in a metrizable topology. It is separated: finite Gauss depth segments detect g, the initial linear segment is detected by g(1), and the canonical value at y is determined by g(infinity). This is precisely locally uniform convergence on compact subsets off y: depth is bounded on such compacts, and conversely the compact analytic Gauss segments detect uniform primitive convergence. All normalized u_h have sup u_h=1/12, attained outside F. The topology does not make the value at y continuous; it fixes that value canonically.

Every positive Radon nu on [1,infinity) of mass c^2<=1 with integral_1^infinity nu((t,infinity))^{3/2} dt finite has a genuine radial solution: take h=c on [0,1), h(t)=sqrt(nu((t,infinity))) afterward. The Stieltjes measure -d(h^2) is exactly nu, including its atom at 1, so the genuine constructed operator is (2-c^2)delta_o+xi_*nu. Conversely its tails recover h uniquely, so uniqueness modulo constants holds within this radial class. Discrete depth grids are the subcase of step tails. The literal finite-energy condition is Z=c^3+integral_1^infinity nu((t,infinity))^{3/2}; the branch mass bound belongs to this image family alone.

Now prove the new FULL bounded dual statement. For the finite-step u_m already constructed, apply n1's tangent inequality to every v in C_theta:

E(v)-integral v mu_m<=E(u_m)-integral u_m mu_m=1/6+(2/3)Z(h_m).

Here integral u_m mu_m=-1/3-Z(h_m), with the same raw mass two throughout. Weak convergence mu_m -> mu_h against the continuous v and Z(h_m) increasing to Z(h) yield

E(v)-integral v mu_h<=1/6+(2/3)Z(h).

This is an upper bound for the ENTIRE C_theta, not only radial competitors. For the reverse inequality test u_m against the ACTUAL limiting analytic measure. Tonelli gives integral u_m mu_h=-1/3-integral h_m h^2, so

E(u_m)-integral u_m mu_h=1/6-Z(h_m)/3+integral h_m h^2
                         ->1/6+2Z(h)/3.

Monotone convergence applies since h_m<=h. The two inequalities give exact equality and full bounded-dual admissibility of EVERY finite-energy continuous or discrete radial solution measure in this range. If Z is infinite for a profile decreasing to zero, the same lower tests diverge; one should not regard that measure as finite-energy eligible. For bounded profiles, u_h itself attains the full bounded dual. For unbounded profiles the proof only needs the bounded optimizing sequence.

For example h=1 on [0,N), zero afterward gives mu=delta_o+delta_xi_N and full bounded dual 1/6+2N/3. This is distinct from the measure 2delta_xi_N, for which 1/6+5N/3 is still only a restricted lower bound. The present theorem neither proves its full admissibility nor supplies a universal atom cap. Nor does bounded-dual finiteness here recognize membership in a full intrinsic all-direction E1 class: no such class and extension are proved.

A genuinely unbounded example is h=1/i on [i-1,i), i=1,2,... . Then g(infinity)=sum_i 1/i=infinity, Z=sum_i 1/i^3<infinity, and the actual measure is delta_o+sum_{i>=1}(1/i^2-1/(i+1)^2)delta_{xi_i}. The positive branch weights telescope to one. The strict nonpluripolar clamp construction above gives full raw mass two and no atom at the rigid y; its full bounded dual is 1/6+(2/3)sum_i 1/i^3. This provides an explicit unbounded solution and its full bounded admissibility, with uniqueness only in the stated radial domain.

Artifacts: n3.md, P16.7-bounded-dual-paper.tex and proof-companion.md contain the entire argument; `python diagnostics.py` checks finite tangent-gap and cubic identities, and `python build_deliverables.py` reproduces document/schema evidence. Mathematical correctness is the universal argument, not execution. Support: n1, n2.
