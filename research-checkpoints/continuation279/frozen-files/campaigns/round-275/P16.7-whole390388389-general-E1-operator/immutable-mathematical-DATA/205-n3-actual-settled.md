Use the reconstructed bounded calculus and actual quotient/calibration in n1-n2. This is an unverified scoped proof.

Let H consist of right-continuous nonincreasing h with 0<=h<=1, constant c on [0,1), and Z(h)=integral_0^infinity h^3<infinity. Put g_h(r)=integral_0^r h and u_h=u0-g_h(R), with its canonical value at R=infinity. Then h tends to zero. Let nu_h=-d(h^2), a positive Stieltjes measure on [1,infinity), including any jump at 1. Its mass is c^2 and nu_h((t,infinity))=h(t)^2 for t>=1.

We prove
MA(u_h)=(2-c^2)delta_o+xi_*nu_h=:mu_h,
B(u_h,u_k)=(2-cd)delta_o+xi_*[-d(hk)],
E(u_h+C)=-1/6-Z(h)/3+2C,
sup_{v in C_theta}(E(v)-integral v mu_h)=1/6+2Z(h)/3.
The operator is genuinely constructed analytically; the final supremum is over the ENTIRE bounded class.

Choose compact finite steps h_m from below, retaining c on [0,1), sampling h at right endpoints on nested dyadic partitions of [1,2^m), and setting zero afterward. These increase to h. Their primitives increase to g_h uniformly on each finite depth interval. Thus u_m decrease to u_h locally uniformly off y. Depth is bounded on any compact subset off y: the closed bidiscs {R>=r} decrease to {y}, and compactness excludes intersection with all of them.

The local weight on W minus y is phi(max(log|w_1|,log|w_2|))-1/6, where phi(a)=-g_h(-a). Its derivative h(-a) is nonnegative and nondecreasing, so phi is convex nondecreasing. Ordinary unit-moment convex approximation proves local bounded membership; omit a zero inactive coordinate. Outside W the open {R<1} has u_h=u0+cD_1. Thus the local bounded operator already exists everywhere off y, independently of any inverse measure assignment.

The actual bounded measures mu_m=(2-c^2)delta_o+xi_*[-d(h_m^2)] converge weakly to the displayed mu_h. Indeed Stieltjes convergence holds on finite depth intervals; at a continuity depth r their tails are uniformly bounded by h(r)^2, tending to zero. Finite partition approximation followed by tail removal proves convergence against bounded continuous depth tests, hence against every continuous analytic test composed with xi. The pushforward is Radon because compact depth intervals have compact images and the finite measure is tight. Local product continuity off y identifies the limit with the actual local product. There is no atom or escaped mass at y, and total mass is two. Polarizing finite formulas and applying the same local convergence and tail argument gives the mixed formula, with positive branch measure -d(hk), branch mass cd and outside mass 2-cd.

The nonpluripolar recipe requires exact endpoint treatment. For M>0, if g_h(infinity)<=M the potential is bounded and the primitives converge uniformly globally, yielding its genuine bounded measure. If M<g_h(infinity), there is a unique finite positive r_M with g_h(r_M)=M. A plateau below the final value is impossible: a nonnegative nonincreasing derivative that reaches zero remains zero. Let h^M=h on t<r_M and zero on t>=r_M. Then
u^M=u0-min(g_h(R),M)=max(u_h,u0-M)
belongs to C_theta by finite real-cutoff approximation and the same convex moment presentation. This remains true if r_M<1; n2 proves every positive real cutoff. Near y the potential is exactly u0-M.

Its branch measure is nu_h below r_M, with the ENTIRE endpoint atom replaced by h(r_M-)^2 delta_rM, including any original endpoint jump. If r_M<1 this mass is c^2. The outside mass stays 2-c^2. On the strict set {g_h(R)<M}={R<r_M}, the whole clamp atom is excluded; locality gives
1_{g_h(R)<M}MA(nu^M)=1_{g_h(R)<M}mu_h.
As M increases, these restricted measures increase to mu_h off y. When g_h(infinity)=infinity the omitted tail h(r_M-)^2 tends to zero. The bounded case is already covered. This proves genuine nonpluripolar full mass two. For sufficiently large j, max(u_h+C,-j) is precisely the same clamp with M=j+C-1/6, since u0=-1/6 on W and the outside potential is bounded. Thus ordinary constant truncations give the same recipe. Clamping both mixed slots and restricting to their common strict unclamped set gives the mixed product; its omitted tail is bounded by h(r)k(r), tending to zero. No rigid atom occurs.

The first energy integral is integral u_h theta^2=0. The second is integral u_h theta alpha_{u_h}=-1/6, since the radial difference annihilates theta and A. These reference measures avoid the singular point. Tonelli gives, without infinity cancellation,
integral g_k(t)nu_h(dt)=integral_0^infinity k(t)h(t)^2dt.
Consequently the top integral is -1/3-Z(h), and the energy is -1/6-Z(h)/3. Constants add twice their value. These are genuine three-term energy integrals and bounded-energy limits.

For every h,k in H, Holder gives integral k h^2<=||k||_3||h||_3^2. Along h_t=(1-t)h+tk and C_t=(1-t)C+tD,
d/dt E(u_{h_t}+C_t)=-integral(k-h)h_t^2+2(D-C)
=integral[(u_k+D)-(u_h+C)]mu_{h_t},
d^2/dt^2 E(u_{h_t}+C_t)=-2integral(k-h)^2h_t<=0.
The undefined difference of infinite values at y is assigned zero on this null singleton. These prove all radial segment variations, concavity and order-monotonicity of energy.

For variable-constant decreasing continuity suppose u_{h_m}+C_m decreases and its energies are bounded below. A fixed point outside F shows C_m decreases. Since E_m<=-1/6+2C_m, it decreases to finite C. Put delta_m=C_m-C. The functions g_m-delta_m increase, are uniformly 1-Lipschitz and concave, and converge locally uniformly to a finite concave primitive g with g(0)=0 and constant derivative on [0,1). Concave secant inequalities give derivative convergence almost everywhere to h. The energy bound bounds Z_m, so Fatou gives Z(h)<infinity. Canonical values at infinity agree because sup_m sup_r(g_m(r)-delta_m)=sup_r sup_m(g_m(r)-delta_m).

Order gives g_m<=g+delta_m. Stieltjes integration by parts for every nonnegative nonincreasing compact test a yields
integral a h_m<=integral a h+delta_m a(0).
Take a=h_m^2 1_[0,L) and let L increase. Holder gives
Z_m<=Z(h)^(1/3)Z_m^(2/3)+delta_m.
Together with boundedness this forces limsup Z_m<=Z(h), while Fatou gives the opposite liminf. Thus energies converge, including variable constants. The estimate r h_m(r)^3<=Z_m gives uniformly vanishing squared tails; Stieltjes convergence therefore gives weak MA continuity and, with the product-tail bound, mixed continuity. This is radial continuity, not an all-direction theorem.

For radial comparison with variable constants put f=g_h-g_k and b=C-D. Inside W the strict comparison set is {f>b}; outside W it is present exactly when b<0. On each component interval (a,l) with positive contact endpoints, right and left derivative signs give h(a)-k(a)>=0 and h(l-)-k(l-)<=0. The difference of branch masses on that OPEN interval is
[h(a)^2-k(a)^2]-[h(l-)^2-k(l-)^2]>=0.
An infinite right endpoint has zero tails. For an initial interval and b=0 the same initial sign applies. For b<0 the initial c^2-d^2 is cancelled exactly by the included outside mass difference d^2-c^2. For b>0 there is no initial interval. Summing proves mu_k{u_h+C<u_k+D}<=mu_h{u_h+C<u_k+D}. Open endpoints exclude their atoms; y has zero mass.

Normalized radial energy sublevels Z<=L, C=0, are compact for uniform primitive convergence on finite intervals. Concave nondecreasing 1-Lipschitz primitives vanishing at zero have diagonal compactness; secant convergence and Fatou preserve Z<=L. Right-continuous derivatives give the limiting profile. This topology is metrizable and separated, equivalent to locally uniform convergence on compact subsets off y. Compact Gauss depth segments detect every primitive; the canonical value at y is determined, although evaluation there need not be continuous. All these potentials have sup=1/12, attained outside F.

Every positive Radon depth measure nu on [1,infinity), of mass c^2<=1 and with integral_1^infinity nu((t,infinity))^(3/2)dt finite, has a genuine radial solution: take h=c initially and h(t)=sqrt(nu((t,infinity))) afterward. Then -d(h^2)=nu, including its atom at 1. The energy condition is exactly Z=c^3+integral_1^infinity nu((t,infinity))^(3/2). Tails recover h, giving uniqueness modulo constants WITHIN the radial class. The branch bound is a restriction of this image family, not a universal cap.

Now establish the new FULL bounded dual. For the genuine finite-step u_m, n1 applies to EVERY v in C_theta:
E(v)-integral v mu_m<=E(u_m)-integral u_m mu_m=1/6+(2/3)Z(h_m).
Here integral u_m mu_m=-1/3-Z(h_m). Weak convergence against continuous v and Z(h_m) increasing to Z(h) give the upper bound 1/6+2Z(h)/3 over the ENTIRE class. Conversely test u_m against the actual limiting measure. Tonelli gives integral u_m mu_h=-1/3-integral h_m h^2, hence
E(u_m)-integral u_m mu_h=1/6-Z(h_m)/3+integral h_m h^2
->1/6+2Z(h)/3.
Monotone convergence supplies the limit. Thus the full bounded dual is exactly that finite value for EVERY constructed finite-energy continuous or discrete radial solution measure. For bounded profiles the solution itself attains it; for unbounded profiles bounded optimizing approximants suffice. If Z is infinite, the same lower tests diverge, excluding finite-energy eligibility.

For h=1 on [0,N) and zero afterward, mu=delta_o+delta_xi_N has full bounded dual 1/6+2N/3. The distinct 2delta_xi_N still has only the restricted lower bound 1/6+5N/3; its full admissibility and equation remain unresolved.

An explicit genuinely unbounded example is h=1/i on [i-1,i), i>=1. Its primitive diverges harmonically, while Z=sum_i 1/i^3 is finite. The actual measure is delta_o+sum_i(1/i^2-1/(i+1)^2)delta_xi_i, with telescoping branch mass one, full raw mass two and no rigid atom. Its full bounded dual is 1/6+(2/3)sum_i 1/i^3.

Bounded dual finiteness here is not an unproved recognition theorem for intrinsic all-direction E1, and radial uniqueness is not full uniqueness. Complete artifacts are n3.md, P16.7-bounded-dual-paper.tex and proof-companion.md. Rerun python diagnostics.py and python build_deliverables.py; their finite/static checks are not mathematical acceptance.
