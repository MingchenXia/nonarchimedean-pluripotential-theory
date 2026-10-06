# Bounded-to-smooth Hermitian Hessian regularity: source review

**Research-only checkpoint.** The controlling book baseline is
`6efda4a342b4cc8fb0060e9d7d0f0e4d76f5a154`. Read Yuetong Fang,
[*Smoothness of bounded solutions to complex Hessian equations on compact Hermitian manifolds*, arXiv:2610.06719v1](https://arxiv.org/abs/2610.06719v1),
submitted 5 October 2026 at 17:11:59 UTC, in all **twenty actual pages**.
Every page, proof computation and reference was displayed, and the full
extracted text read in ten sheets. The PDF has 374,437 bytes and SHA-256
`0ff379920875f5ec9f7ad53717abfb7a819b237059c3ba369275452fa9a2383c`.
The font-type extraction warning is preserved; the actual equations
were visually inspected. No result from this new paper is yet admitted
into active TeX.

The full-reading record SHA-256 is
`5c0b7f80372d36946a923c89695459cd20506a6448defa1861ae9142efff5377`;
its view manifest SHA-256 is
`8a3adffd5d0e153f05c7670db906d53bfb97a2d90ad9c4a7023f2be7f6108b29`.
The acquisition record keeps its historical false reading flags. A
separate completed-reading record controls the actual completed read.

## Statement and proof interfaces

The introductory result and Theorem 4.1, actual pages 2 and 17--18,
concern a **given bounded** (omega,m)-subharmonic solution on a compact
Hermitian manifold, for 2<=m<=n, of

    H_m(phi) := (omega+ddc phi)^m wedge omega^(n-m)
              = exp(f(x,phi)) omega^n,

with f smooth on X times R. The claimed conclusion is smoothness of
this existing solution. The claim does not impose monotonicity of f
in the unknown, and does not itself establish existence or uniqueness
for arbitrary original right-hand-side dependence. The earlier
continuity dependency explicitly uses ddc=2i partial barpartial;
the new paper does not repeat an explicit ddc definition. Any future
import must state its convention and check the potential conversion
against the book's ddc=i partial barpartial/(2 pi).

The proof follows the positive-coefficient static scheme used in the
preceding Monge--Ampère paper. Given smooth decreasing admissible
v_j approaching phi, it solves

    H_m(u_j)=exp(u_j-v_j+f(x,v_j)) omega^n.

The coefficient of u_j remains positive, regardless of the derivative
of the original f. Uniform potential bounds, a second-order estimate
relative to the gradient, and Liouville blow-up are intended to yield
uniform gradient and Laplacian bounds. A subsequential uniform limit
u satisfies the frozen equation with phi in place of v_j. Its
identification with phi requires a bounded global domination input;
uniqueness of the original equation is not the reason for this step.

The second auxiliary sequence on actual page 18 solves

    H_m(tilde u_j)=exp(tilde u_j-u_j+f(x,u_j)) omega^n.

The first sequence's controlled Laplacian gives standard linear
elliptic W^(2,p) and C^(1,alpha) bounds. These control the frozen
right-hand side of the second sequence in a Hölder norm. Applying
the second-order argument again and the appropriate Evans--Krylov
input then leads to C^(2,alpha) bounds, followed by Schauder
bootstrapping. The positive density and admissible eigenvalue/trace
bounds are needed for uniform ellipticity. Mere uniform convergence
of the first sequence would not justify this higher-order conclusion.

## The estimate and its fixed approximation

Theorem 3.1, actual pages 8--17, treats smooth bounded v and the
positive-coefficient equation H_m(u)=exp(u+h(x,v)) omega^n. The
maximum-principle test uses the largest admissible eigenvalue, a
gradient term, a potential term and chi(v-tilde phi), where tilde phi
is one **fixed smooth function** uniformly close to v. Eigenvalues
may be negative when m<n; positivity of an individual metric cannot
be assumed. The largest-eigenvalue perturbation and Hermitian torsion
calculations follow Székelyhidi's Proposition 13.

The stated conclusion has the form

    sup Delta u <= C(1+sup |gradient u|^2).

Its constant depends on the smooth geometry, the uniform potential
bound, h's indicated C^2 bounds and the C^2 norm B_0 of the fixed
tilde phi. It avoids derivative bounds on v, but is not independent
of every possible approximating family. Continuity of the prescribed
phi is needed before choosing this fixed smooth uniform
approximation. It is used at the start of Theorem 4.1 without an
explicit citation there; the earlier continuity paper is therefore
a substantive dependency.

The order of parameter choices does not show the suspected circularity
between epsilon and B_0: epsilon is chosen using the fixed h and
potential bounds before tilde phi, while later constants may depend
on B_0. A suspected missing n/m factor in the final mixed absorption
is also **cleared**, using the exact identity

    sum_p F^(pp) lambda_p^2
      = (1/m) S_m^(1/m) S_1
        - ((m+1)/m) S_m^(1/m-1) S_(m+1).

The first summand cancels the displayed trace term at the chosen
coefficient. If S_(m+1)<=0 the remaining contribution has the good
sign; otherwise the equation and Maclaurin bound control it. These
cleared suspicions are not listed as additional source defects.

## Fresh dependency reading and remaining scope

Read and displayed **81 selected physical pages** in 41 sheets,
including one publisher cover, hence eighty research-text pages.
Only Dinew--Kołodziej's twelve-page arXiv v2 is freshly read in full.

| Exact primary edition | Actual PDF pages read | Checked input |
| --- | --- | --- |
| Fang, 2510.14690v1, 16 October 2025, 13:57:44 UTC; 22 pages | 1--7, 17--20 | Theorem C's continuity scope, mixed tests, global domination statement/proof, delta-sublevel corollary, trace lower-bound argument, density normalizers and the displayed continuity conclusion |
| Kołodziej--Nguyen, published Analysis & PDE 19 (2026), 107--166; 63-page PDF | 1--4, 9--10, 22--24, 38--43, 56--58 | Cover and introduction; local approximation; inductive measures; monotone convergence; Corollary 6.2; background-form construction and the boundary subsolution theorem |
| Székelyhidi, 1501.02762v3, 23 April 2015, 13:26:26 UTC; 34 pages | 1--2, 11--28 | Proposition 13's dependencies, eigenvalue perturbation, torsion and maximum-principle cases, viscosity Liouville theorem, Hermitian blow-up and smooth normalized Hessian existence |
| Dinew--Kołodziej, 1203.3995v2, 12 August 2015, 15:00:19 UTC; 12 pages | 1--12, complete | Bounded maximal entire m-subharmonic Liouville theorem, complete induction/comparison proof, Kähler blow-up and the stated gradient estimate dependencies |
| Tosatti--Wang--Weinkove--Yang, 1402.0554v2, 13 October 2014, 22:23:58 UTC; 26 pages | 1--7, 10--12 | Theorems 1.1 and 1.2, Hölder data and operator hypotheses, Hessian uniform ellipticity and its algebraic bounds |
| Kołodziej--Nguyen, 1507.06755v2, 10 March 2016, 11:24:27 UTC; 27 pages | 1--2, 10--11, 14--15, 22--25 | Approximable class, background comparison for continuous potentials, smooth positive-exponent existence, L^p uniform convergence and global decreasing approximation |

The dependency reading record SHA-256 is
`bc23edf5fd608428d15ee89c201cf0ee9d0388c2e0818ad503623aecdbdbbde4`;
its view manifest SHA-256 is
`36aad79b435466131445468dabae496144b73582e8ed045c7a60c8db0973b22a`.
The checkpoint manifest embeds each PDF/text hash, exact edition,
acquisition URL/status and page selection. Acquisition and preparation
records remain historical. Journal editions and arXiv versions are
not interchangeable proof locators.

The 2016 Hessian paper's Theorem 3.17, actual pages 23--24, is the
smooth auxiliary existence result invoked by the new proof. The
new paper cites [KN15, Theorem 3.17], but its [KN15] bibliography
entry is a different Monge--Ampère proceedings paper. Theorem 3.19
of the acquired Hessian v2 gives uniform convergence under L^p
convergence of smooth positive densities, p>n/m, to a nonzero
nonnegative density; uniqueness is stated in the continuous
approximable class. Lemma 3.20 gives global smooth decreasing
approximation. Those exact statements are checked in the acquired
version; their unselected antecedent stability and maximality proofs
are not newly certified in full by this checkpoint.

The published 2026 paper's Corollary 6.2, printed 148 (actual 43),
uses H_m(u)=(ddc u)^m wedge omega^(n-m), not the compact-manifold
background operator. Printed 162 (actual 57) explicitly retains
tau=alpha-ddc rho when defining background products, states transfer
of local results, and gives a local background Dirichlet uniqueness
lemma whose proof is referred to an extension of earlier work.
The preceding section's corollary by itself cannot be applied simply
by pretending that a nonclosed Hermitian form has a local potential.
The stated background extension is relevant evidence, but its
complete comparison proof is not freshly reproduced here.

Fang's earlier Proposition 1.8 is printed for bounded psh potentials,
whereas the new paper uses bounded m-subharmonic potentials. Its
proof also invokes the local comparison corollary for forms containing
the background. That combination of class and operator scope still
needs exact primary reconciliation. The earlier Corollary 1.9,
actual page 7, does correctly use a fixed delta sublevel to obtain a
uniform contraction factor.

The earlier Theorem C concerns densities satisfying the indicated
Orlicz condition on f^(n/m); its all-bounded-solutions conclusion
again uses global domination. The smooth positive density obtained
from a bounded solution of the new equation is within a strong
integrability range. Nevertheless the printed continuity proof's
trace lemma has an invalid equality identification described below.
The normalized c_j trace display also omits exp(lambda u_j/m) for
lambda>0. These displays do not certify failure of Theorem C or of
the bounded smooth-density case; they prevent silently treating
every printed inference as checked. The complete Orlicz estimates,
earlier local comparison inputs, and all unselected proof pages
remain outside this fresh reading scope.

Székelyhidi's Proposition 13 depends on the prescribed right-hand
side's C^2 norm and a subsolution. Dinew--Kołodziej's compact Kähler
gradient estimate likewise depends on the density root's C^2 norm.
Their cited gradient estimates cannot supply a uniform bound for
arbitrary v_j by dropping these dependencies. Their Liouville and
blow-up mechanisms are relevant once the new specialized uniform
second-order estimate is available. The selected TWWY pages check
the higher-order theorem and Hessian application; the full abstract
Theorem 1.2 proof and Caffarelli's underlying paper were not freshly
read. The remaining Garding, Hou--Ma--Wu, CNS and book-length
Schauder antecedents are also not claimed as new full readings.

## Literal diagnostics

The seven main-paper checks have record SHA-256
`1bbeecd9ab08d02386a1d80e8c3bbee9db495e5705590461530427f74d5d8222`.

1. Lemma 2.2, pages 5--6: alpha=omega and k=1 make the displayed
   epsilon_1 shift equal to zero, on the boundary of the strict cone.
   The existence of a smaller positive shift, and the m>=2 minimum
   choice used later, are not refuted.
2. Definition 2.8, page 7: the mixed test omits omega^(n-m). For
   n=4,m=2 its printed bidegree is (2,2), rather than (3,3).
3. Corollary 2.11, page 8: a strict pointwise u<v gap does not give
   one uniform c<1 on the entire strict set. Fixed delta sublevels
   provide the standard inference used correctly in the precursor.
4. Page 10 declares F=S_m but prints derivatives of S_m^(1/m).
   For n=3,m=2 and lambda=(1,1,1), S_m=3, while the normalized
   wedge density is 1. An intended root equation also needs its
   binomial normalization or an explicit constant shift.
5. The differentiated lower bound on page 10 uses an unjustified
   positive C_2 lambda_1 term. For n=m=2, u=10, v=0, h=-10,
   reference identity, C_2=10 and C_3=C_4=1/2, its left side is
   zero and its printed right side is 9/2. The positive term is
   discarded in the following bound; this tests that display only.
6. Equation (3.14), page 14, omits F^(pp) in a retained positive
   gradient term. For lambda=(100,1/100), n=m=2, F^(11)=1/200.
   The largest possible corresponding chi'' coefficient is 3/50,
   rather than the printed unweighted 1/2. Later Case 2 uses the
   weighted expression. This is not a counterexample to the full
   maximum-principle inequality or the final estimate.
7. Page 1's smooth existence assertion for nondecreasing f lacks
   normalization or additional hypotheses. On compact Kähler data,
   f=log(2) would equate total mass V to 2V. This does not refute
   conditional regularity of an existing bounded solution.

The three dependency checks have record SHA-256
`0f6abc6bdebc9125f3833d936181a899c5672ff1c41dc3eb592ac05d687c90af`.

1. Fang's Proposition 3.4 proof, actual page 17 of 2510.14690v1,
   identifies an auxiliary equality solution with a potential having
   only H_m(phi)>=f omega^n. For smooth compact Kähler data,
   phi=v_j=0 and f=g_j=1/2, its auxiliary solution is **+log(2)**,
   since 1=exp(u_j)/2. It does not tend to phi. The asserted trace
   lower bound 1>=(1/2)^(1/m) still holds, so the conclusion is not
   refuted by this example.
2. Dinew--Kołodziej's Proposition 1.3(1), actual page 4, reverses
   the class inclusions. The smooth quadratic with Hessian
   diag(-1,2) has S_1=1 and S_2=-2: it is subharmonic and not psh.
   The standard nesting is PSH=SH_n subset ... subset SH_1=SH.
   This does not refute the Liouville theorem.
3. TWWY actual page 11 calls the set defined by (2.15) compact in
   all real symmetric matrices although the conditions constrain
   only p(N). For n=k=2, g=I, K_0=2 and
   N_t=diag(1+t,1,1-t,1), p(N_t)=I for every t>=0, while
   ||N_t||=1+t. The J-invariant image contains the matrices used
   in the Hessian application; that restriction must be explicit
   when applying the compact-set theorem. This diagnoses the
   literal set, not Theorem 1.1 or a complete original repair.

All ten checks are elementary substitutions, normalization or source
inference diagnostics. They are not promoted as original results or
counterexamples to the main regularity/dependency theorems. No
independent model call or production verification receipt is claimed.

## Preservation and continuation

All 425 active inputs, both bibliographies, 108 protected inputs,
sixty prior frozen manifests (54 integration and six source-only
records), and 118 prior exports retain their baseline bytes. The
checked **4,392-page book** and every generated book file are
unchanged. The 42 complete canonical statuses, twelve families,
tier counts 0/3/7/15/17, open toric candidate and native catalogue
source/PDF retain their bytes and scope. README and the programme
are the only changed tracked baseline files; the other 5,042 retain
their hashes. Inventory and whitespace checks pass.

No unchanged-book build, final-book PDF review, isolated archive
compilation, native compile or editor/tab change is claimed. No new
canonical problem, solved status, general Siu/closure repair or
complete external proof certification is added. The next source task
is to reconcile global bounded domination, the precursor's continuity
input and the specialized estimate before deciding which limited
Hessian material belongs in the existing Chapter 68 discussion.
Cloud synchronization explicitly fetches both main and work and
uses the existing work branch and PR.

The initial audit described the new paper's ddc convention too
categorically. That wording is corrected above before this checkpoint
is pushed. The initial manifest and exact initial audit bytes remain
historical; the separate v2 manifest pins this corrected audit and
the preserved original snapshot. No mathematical theorem, diagnostic
data, source reading, book input or problem status changes in this
correction.
