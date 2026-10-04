#!/usr/bin/env python3
"""Record partial mathematical status and canonical native notes."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent
gaps = [
    "No general intrinsic geometric d-dimensional carrier or quotient is constructed; "
    "the carrier of the measure is the n-dimensional X.",
    "No characterization of minimum necessary reference data is proved. This measure "
    "requires a full Kahler form, and a same-class analytic example proves its dependence.",
    "Operator perturbation convergence requires bounded-type differences o(epsilon), "
    "with a fixed form or smooth positive limit; arbitrary perturbations are not covered.",
    "General unbounded finite-energy truncation-value continuity, numerical cocycles and "
    "reference change are unproved; weak measure convergence gives no weighted tail estimate.",
    "Degree-d finite joint energy has not been shown here to control weighted degrees k<d "
    "or joint unbounded perturbation limits.",
    "The actual-type degree is not identified with the class numerical dimension.",
]
status = {
    "id": "P15.2",
    "status": "partial",
    "exact_result": (
        "For every connected smooth compact Kahler n-fold, pseudoeffective zero-volume "
        "class and actual theta-psh reference psi, the bounded singularity-type domain "
        "has an exact actual-current degree d<n, mixed current vanishing, the positive "
        "raw-mass operator <T_u^d> wedge omega^(n-d) on X, and sufficient rescaled "
        "perturbation convergence with sup-distance o(epsilon). Its bounded relative "
        "primitive has a cocycle and depends only on the auxiliary class; the leading "
        "energy limit holds for arbitrary representatives of converging Kahler classes "
        "and sup-distance tending to zero. The operator extends to more-singular "
        "degree-d relative full-mass currents and is continuous under decreasing "
        "full-mass sequences, including bounded-type truncations. This does not close "
        "the unchanged original P15.2."
    ),
    "proof_file": "P15.2-argument.md",
    "concrete_gaps": gaps,
}
assert set(status) == {"id", "status", "exact_result", "proof_file", "concrete_gaps"}
(ROOT / "status.json").write_text(json.dumps(status, indent=2) + "\n")

# Every note contains its argument in text, not just a pointer to the proof artifact.
n1 = {
    "id": "n1",
    "summary": "Partial P15.2 theorem for every pseudoeffective zero-volume class, "
               "without a fibration: bounded actual type has degree d<n, mixed vanishing, "
               "positive raw-mass operator on X, o(epsilon) perturbation convergence "
               "and a class-dependent bounded primitive. Full-form dependence remains.",
    "detailedSummary": (
        "For actual theta-psh psi on a connected compact Kahler n-fold, define "
        "M_k=int <T_psi^k> omega^(n-k), M_0=int omega^n, and d=max{k:M_k>0}. "
        "The big-class upper bound and boundary volume limit give d<n; positive-form "
        "comparison gives degree independence. DDNL bounded-type mixed mass equality "
        "and positivity imply every k>d mixed product vanishes as a current. "
        "mu_u=<T_u^d> omega^(n-d) has actual mass M_d and carrier X of dimension n. "
        "Signed admissible IBP proves the rescaled top-product error is "
        "O(sup|u_epsilon-u|/epsilon). The relative degree-d primitive is closed, "
        "concave and has a cocycle; degree-(d+1) vanishing proves representative "
        "independence of that primitive. Exact Vandermonde coefficients give its "
        "positive-epsilon energy limit with only uniform distance tending to zero, "
        "even for arbitrary representatives of converging Kahler classes. "
        "No numerical-dimension identification, intrinsic lower-dimensional carrier "
        "or unrestricted perturbation theorem is claimed."
    ),
    "text": r"""This is a proved narrower theorem in an unverified draft, addressing only P15.2, not a complete solution of its unchanged residual scope.

Ambient hypotheses: X is connected, smooth, compact Kahler of complex dimension n>=1; alpha is pseudoeffective, vol(alpha)=0; theta is a smooth representative; psi is an actual theta-psh function not identically minus infinity; omega is a fixed Kahler form. Use dc=i(barpartial-partial)/(4pi), ddc=i partial barpartial/(2pi). Write T_u=theta+ddc u, P=T_psi. The domain C_psi consists of theta-psh u with psi-C<=u<=psi+C as extended-valued functions. It retains two-sided bounded singularity type, not just I-equivalence. The common polar set is ignored only when integrating nonpluripolar measures. Comparing only on an intersection of finite loci would be insufficient.

Foundations, with their exact operative statements: BEGZ, Acta Math.205(2010),199-262, Propositions1.4,1.6 and Theorem1.8, says nonpluripolar products of closed positive (1,1) currents on compact Kahler X are finite, closed, positive, symmetric, positive-multilinear and plurifine-local, and have no pluripolar mass. DDNL, Anal.PDE11(2018),2049-2087, Proposition2.1 says the top mixed masses of u_j,v_j in PSH(X,theta_j) agree when each pair has the same bounded singularity type, for pseudoeffective theta_j; Theorem2.4 says replacing every factor by a more singular one cannot increase that mass. Smooth zero-potential Kahler slots can fill a lower-degree product to n slots. BEGZ Section1.4 and Definition1.17 give a minimal-singularity current Q_min in every big class beta, whose actual top mass is vol(beta), and the pseudoeffective boundary definition vol(alpha)=lim_{epsilon down0}vol(alpha+epsilon[omega]). DDNL monotonicity therefore bounds every actual top mass in beta by vol(beta); equality for arbitrary currents is not asserted.

Vu, arXiv:2005.13241v3, Lemmas2.5,2.6 and Theorem2.7, gives the following signed IBP: for closed positive (n-1,n-1) R and bounded R-admissible dsh differences v,w, integral w<ddc v dotwedge R>=integral v<ddc w dotwedge R>=-integral<dw wedge dc v dotwedge R>. The v=w gradient is positive and finite. Admissibility means the polar loci of the quasi-psh representatives carry no R mass. In every application here R is a nonpluripolar product times smooth positive forms, or smooth, and has no pluripolar mass, so this hypothesis holds. The signed insertion is the difference of two finite ordinary nonpluripolar products, by local cutoffs and positive multilinearity. The relative association is Vu Proposition2.1(iii). No smoothness of bounded differences is assumed.

Convention conversion: DDNL uses i partial barpartial and its source potential is u/(2pi). Vu uses dc_s=2dc and ddc_s=2ddc; its source potential is u/2, leaving every actual current unchanged. Its gradient of v/2 is half our gradient of v. Both sides of source IBP become half our formula, so multiplication by two gives the displayed identity. The correct gradient is (1/2)ddc(v^2)-v ddc v. Vu v3 Eq(2.3) prints this correctly, but repeated page6 and page11 formulas omit the half. Literal quotes are preserved. With a=phi_1,k+rho and b=phi_2,k+rho, the correct local expansion is ddc(a^2)+ddc(b^2)-(1/2)ddc((a+b)^2)-v_k(ddc phi_1,k-ddc phi_2,k), wedged with R. The three squares are bounded psh locally after positivity adjustment, so the same plurifine-locality proof applies. The correct intrinsic gradient is positive, with mass <=2||v_k|| integral kappa R by Stokes. For the cutoff tending to1 outside a locally complete pluripolar set not charged by R, Vu Theorem2.2 gives separately ddc(chi_k^2)R->0 and chi_k ddc chi_k R->0: choose a fixed strictly psh rho with chi_k+rho psh and increasing, and expand squares/products against the fixed smooth rho. Thus the corrected half-factor still yields zero cutoff-gradient limit and kills the IBP boundary terms by Cauchy-Schwarz. No incorrect printed gradient is used. These literature results are scoped standard foundations, not new reconstructed theorems.

Put M_k=integral<P^k>omega^(n-k), with <P^0>=1, and d=max{k:M_k>0}. M_0>0. Positive expansion gives integral<(P+epsilon omega)^n>=sum_k C(n,k)epsilon^(n-k)M_k<=vol(alpha+epsilon[omega])->0. Hence M_n=0 and d<n. Comparing c omega<=eta<=C omega gives c^(n-k)M_k(omega)<=M_k(eta)<=C^(n-k)M_k(omega), so positivity and d are independent of the positive auxiliary form. DDNL mixed equality gives integral<T_u1 ... T_uk>omega^(n-k)=M_k for u_i in C_psi. For k>d this is zero. A positive current with zero Kahler trace mass is zero: locally all its measure coefficients are controlled by its positive trace. Thus every such mixed product vanishes as a current. Monotonicity gives the same vanishing for factors more singular than psi. Anchor changes within bounded type preserve d and every M_k. Closedness makes M_k depend only on [omega].

Define A(u)=<T_u^d>, a (d,d) current intrinsic to the actual u, and mu_(u,omega)=A(u)omega^(n-d), a positive nonpluripolar measure on X of actual mass M_d>0. The geometric carrier has dimension n; no geometric d-fold is inferred from bidegree d. For fixed u the exact expansion is
<(T_u+epsilon omega)^n>/(C(n,d)epsilon^(n-d))
=mu_(u,omega)+sum_{k<d}(C(n,k)/C(n,d))epsilon^(d-k)<T_u^k>omega^(n-k).
The positive remainder has mass O(epsilon); for d=0 it is absent and the equality with omega^n is exact.

For u_epsilon in PSH(X,theta+epsilon omega) of the same type with delta=sup|u_epsilon-u|, set S=theta+epsilon omega+ddc u_epsilon, A=T_u+epsilon omega, h=u_epsilon-u, and R_j=<S^j A^(n-1-j)>. They are closed positive (n-1,n-1), with the degree-zero convention R=1 when n=1. Factorization and IBP against real smooth f give integral f(<S^n>-<A^n>)=sum_j integral h ddc f R_j. Choose -C_f omega<=ddc f<=C_f omega. DDNL mixed equality gives integral omega R_j=integral omega<(P+epsilon omega)^(n-1)>=sum_{k<=d}C(n-1,k)epsilon^(n-1-k)M_k=O(epsilon^(n-d-1)). Thus the rescaled error is <=constant_f delta/epsilon. Uniform total-mass bounds and density of smooth tests give weak measure convergence if delta=o(epsilon). Smooth convergence omega_epsilon->omega>0 gives uniform comparison constants and convergence of the fixed-u leading current pairing; the same proof applies. No rate-free claim or optimality theorem is made.

Let L_u(v)=integral v<T_u^d>omega^(n-d). In any fixed finite-dimensional convex hull of bounded-type potentials all products and finite coefficient integrals are polynomials. Its directional derivative is d integral b<ddc a T_u^(d-1)>omega^(n-d), symmetric in a,b by the admissible IBP above. For d=0 this derivative is zero. Thus L is closed. Integrating on the segment psi+t(u-psi), and using integral_0^1 C(d,a)t^a(1-t)^(d-a)dt=1/(d+1), gives
E_(psi,[omega])(u)=1/(d+1)sum_{a=0}^d integral(u-psi)<T_u^a P^(d-a)>omega^(n-d).
Closedness and ordinary Stokes on a triangle yield E_psi(v)-E_psi(u)=E_u(v). For segments and C^1 paths in the stated finite-dimensional hull, E'=integral dotu mu_u. It is monotone, satisfies |E(v)-E(u)|<=M_d||v-u|| and E(u+c)=E(u)+cM_d. Its segment second derivative for d>=1 is -d integral<dh dc h dotwedge(<T_ut^(d-1)>omega^(n-d))><=0, using the finite positive gradient. For d=0 E=integral(u-psi)omega^n is affine; no negative-degree gradient expression is used.

For cohomologous Kahler omega'=omega+ddc g, the smooth compact-Kahler ddc lemma supplies real smooth g (DGMS, Invent.Math.29(1975),245-274, Section5; the global-potential consequence also appears in BEGZ Section1.3). Its exact hypothesis is a smooth real closed cohomologically zero (1,1) difference on compact Kahler X. Expand omega'^(n-d)-omega^(n-d)=ddc g sum_r omega'^r omega^(n-d-1-r). For each d-fold mixed Q, R=Q omega'^r omega^(n-d-1-r) is positive closed of degree n-1 and admissible. IBP transfers ddc g from integral(u-psi)ddc g R to integral g<ddc(u-psi)R>. Each term is a (d+1)-fold same-type current, hence zero. This proves representative independence of E, including d=0. It does not prove representative independence of mu. A change theta->theta+ddc g, u,psi->u-g,psi-g preserves every actual current and difference.

Define E^k=1/(k+1)sum_{j<=k}integral(u-psi)<T_u^jP^(k-j)>omega^(n-k), k<=d. Its magnitude is <=||u-psi||M_k. Positive-epsilon unnormalized relative n-energy satisfies the exact identity E^n_(psi,theta+epsilon omega)(u)=sum_{k<=d}C(n,k)epsilon^(n-k)E^k. The coefficient follows from sum_a C(a,j)C(n-a,k-j)=C(n+1,k+1): count a (k+1)-element subset by its (j+1)-st member. Higher T-degree terms vanish. The leading coefficient is C(n,d)E^d. For u_epsilon close to u, the positive-background cocycle and monotonicity give |E^n(u_epsilon)-E^n(u)|<=delta m_epsilon with the ACTUAL mass m_epsilon=sum_{k<=d}C(n,k)epsilon^(n-k)M_k. Rescaling therefore needs only delta->0.

Even if arbitrary representatives omega_epsilon have only [omega_epsilon]->lambda Kahler, closedness gives M_k as a continuous cohomological polynomial, uniformly bounded near lambda. Thus the lower energy coefficients, bounded by ||u-psi||M_k, vanish after rescaling. For the leading coefficient choose a finite smooth basis beta_i and a fixed positive representative sigma_0 of lambda; sigma_0+sum b_i beta_i remains Kahler locally. Representative invariance identifies E^d with a continuous polynomial in b_i, so its limit is E_(psi,lambda)(u). The rescaled actual mass is uniformly bounded, proving the same statement for delta->0. This applies to energy alone; it implies neither full positive-epsilon representative independence nor a form-free operator limit.

Artifacts: P15.2-argument.md contains all new proofs plus complete essential supplied source bodies and preserved defects; P15.2-partial.tex is standalone and P15.2-partial.pdf is compiled twice. Rerun: python build.py. Exact finite diagnostics checked 5,455 coefficient instances for 1<=n<=30, 0<=k<=n, 0<=j<=k, all passed; the all-n proof is the counting argument, not that finite run. Build success does not certify analytic correctness. The original P15.2 remains open: this domain, rate condition and carrier/reference data are narrower than its full quantifiers.""",
    "support": [],
}
n2 = {
    "id": "n2",
    "summary": "The actual operator extends beyond bounded differences to more-singular "
               "degree-d relative full-mass currents and is continuous under decreasing "
               "full-mass sequences. A genuine unbounded finite-energy example is given; "
               "the general unbounded energy cocycle and perturbation limits remain unproved.",
    "detailedSummary": (
        "For u<=psi+C with int<T_u^d>omega^(n-d)=M_d, the operator of max(u,psi-j) "
        "converges weakly to the actual operator. Mixed monotonicity forces all "
        "intermediate degree-d mixed masses to equal M_d; Vu Lemma4.1(i), with "
        "constant smooth relative current, yields local lower semicontinuity. "
        "Every weak cluster point dominates the actual product and has the same mass, "
        "so it equals it. The same argument proves decreasing full-mass continuity "
        "and independence of such decreasing majorants. Vu's exact linear joint "
        "finite-energy class is identified and is genuinely larger in an explicit "
        "P1xP1 logarithmic-power example. No weighted truncation-value continuity, "
        "unbounded numerical cocycle or lower-degree perturbative integrability is claimed."
    ),
    "text": r"""Use n1's degree d, actual reference P, mixed monotonicity foundation and raw mass M_d, with a fixed full Kahler form omega. This note proves an operator extension, not a general unbounded energy theorem.

Allow theta-psh u<=psi+C and require int<T_u^d>omega^(n-d)=M_d. Additive constants do not change currents, so normalize u<=psi. If u<=v_i<=psi, DDNL Theorem2.4 in d current slots and n-d smooth slots puts the mixed mass int<T_v1 ... T_vd>omega^(n-d) between the two equal pure masses of u and psi. Thus it is exactly M_d. In particular u_j=max(u,psi-j) is theta-psh, of bounded type [psi], decreases to u, and has mass M_d.

The additional precise foundation is Vu, arXiv:2004.11111v1, Lemma4.1(i): on local U in C^n, psh p_i^l>=p_i converging in L1_loc, with closed positive relative currents R_l->R satisfying Condition(*), gives liminf int<ddc p_1^l ... ddc p_m^l dotwedge R_l>Phi >=int<ddc p_1 ... ddc p_m dotwedge R>Phi for every compactly supported smooth weakly positive Phi. The printed Condition(*) demands locally uniformly bounded masses and vanishing of (q_l-q)(ddc q)^r R_l for decreasing psh q_l to bounded psh q; the source lists constant sequences as examples. Here R_l=R=omega^(n-d) is a fixed smooth closed positive form, so (*) follows from decreasing Bedford-Taylor convergence and its relative product is the ordinary nonpluripolar product times that form. Local potentials p_i^j of u_j decrease to those of the given u; 0<=p_i^j-p_i<=p_i^1-p_i, with locally integrable majorant, proves L1_loc convergence by dominated convergence. The source convention conversion is n1's positive potential rescaling. These check every needed application hypothesis.

Positive measures mu_j=<T_uj^d>omega^(n-d) have uniform mass M_d on compact X, so have weak cluster points. Lemma4.1(i) locally, then a nonnegative smooth partition of unity, implies every cluster point nu dominates the actual mu_u. Both have mass M_d. Hence nu-mu_u is a positive zero-mass measure and vanishes. All cluster points coincide, proving the whole sequence converges. The same proof handles any decreasing sequence in this more-singular relative full-mass domain whose limit is full mass, and any other decreasing bounded-type majorants in this domain. For d=0 all products are the convention 1, so the operator is omega^n and the conclusion is immediate.

A bounded-equivalent anchor change preserves dominance up to a constant and the masses from n1, so the full-mass operator domain is unchanged. Changing omega within its class preserves the full-mass condition by closedness of <T_u^d>; it can change the measure. No invariance under arbitrary auxiliary-class change is asserted. The retained singularity data for unbounded u are its actual current and a dominating reference bounded type, not equality of its type to [psi].

For d>=1 investigate the domain F^1 of these full-mass u with sum_{a=0}^d int |u-psi|<T_u^aP^(d-a)>omega^(n-d)<infinity. Normalize u<=psi. Vu arXiv:2005.13241v3 Section3, with m=d, P_j=P, smooth R=omega^(n-d), and linear weight chi(t)=t, gives joint energy d sum_a C(d,a)int(psi-u)<T_u^aP^(d-a)>omega^(n-d). In the chosen potential convention this is the joint energy; Vu's literal source potentials u/2,psi/2 give half this expression, and multiplication by two is the explicit linear-weight homogeneity conversion. Its finiteness is equivalent to the definition because all finitely many terms are nonnegative. Top-degree cohomology equality is mass equality on connected compact oriented X. Vu Theorem3.4 supplies convexity; Corollary3.2 supplies bounded-equivalent-anchor invariance of finiteness. Their printed proofs invoke prior literature and are used as scoped standard foundations, not newly reconstructed proofs. This note's operator continuity applies to F^1, indeed to the larger full-mass domain.

The extension really can include unbounded differences. Take X=P1_y x P1_z, normalized Fubini-Study eta_y,eta_z, theta=eta_y, psi=0, omega=eta_y+eta_z; then d=1, M_1=1. Near y=0 set f(y)=-(-log|y|)^a with 0<a<1/2, extend by a smooth cutoff on an annulus, multiply by a sufficiently small c>0, and subtract a constant. On the annulus the lower Hessian bound is finite, so eta_y+ddc(cf)>=0 for small c. Near the puncture radial convexity gives second derivative a(1-a)(-t)^(a-2)>0 for t=log|y|. The radial slope ca(-t)^(a-1)->0, so this current has no atom at zero. Stokes gives total mass1; since its only singular locus is that point and its mass there is zero, its nonpluripolar mass is also1. Pull back u=cf to X. The smooth-volume linear-weight integral is finite by exponential radial area; the current linear-weight integral is finite because its tail is a constant times int_infinity s^(2a-2)ds, which converges for a<1/2. Thus u lies in F^1 but u-psi is unbounded.

This does not finish the full finite-energy route. Weak product convergence does not justify multiplying by unbounded weights. No uniform weighted-tail estimate for truncated products, equality/continuity of truncated energy values, unbounded numerical cocycle or general unbounded reference-change theorem is proved here. Degree-d joint finiteness has not here been shown to control weighted degrees k<d in the positive-epsilon energy expansion, or a joint truncation/epsilon limit. The bounded o(epsilon) operator estimate cannot simply be transferred to arbitrary unbounded differences. These are specific unresolved proof steps, not claimed counterexamples.

Full proof and literal source bodies: P15.2-argument.md, Sections2 and9. Rerun source/hash and build verification: python build.py. These analytic arguments are mathematical proofs conditional on the stated standard foundations; source hashing and compilation do not independently certify them. Original P15.2 remains open.""",
    "support": ["n1"],
}
n3 = {
    "id": "n3",
    "summary": "Analytic tests prove full-form dependence and actual-type degree different "
               "from class numerical dimension; artifacts and 14 immutable source slices "
               "are verified. Status partial and candidate false; original P15.2 remains open.",
    "detailedSummary": (
        "On P1xP1 with alpha=[eta_y], d=1 for the smooth reference. Replacing omega by "
        "omega+t ddc g(z) in the same class changes mu by t eta_y wedge ddc g, while "
        "preserving mass. A divisorial actual reference in the same class has d=0, "
        "whereas its nef class numerical dimension is1. Thus the stated construction "
        "does not supply form independence or an intrinsic geometric d-fold. "
        "All14 supplied LF-slice hashes and literal quotations match; the input is "
        "byte-preserved; the standalone10-page PDF has two successful TeX passes "
        "and no warnings or overfull boxes. These are artifact checks, not mathematical "
        "certification. Five-key status is partial; the full original atom is not closed."
    ),
    "text": r"""This note uses the operator and degree results of n1 and the limited unbounded extension of n2. It gives analytic limitations and reproducibility evidence, not a complete solution or a universal impossibility theorem.

Let X=P1_y x P1_z, theta=eta_y, psi=u=0, omega=eta_y+eta_z, with normalized Fubini-Study forms. The class alpha=[eta_y] is nef, alpha^2=0 and alpha[omega]>0. BEGZ Definition1.17 says the positive product of nef classes equals their cup product, so vol(alpha)=0. Its smooth actual reference has d=1, mass M_1=1, and mu=eta_y eta_z. For nonconstant smooth real g(z), choose small nonzero t with eta_z+t ddc g>0. The cohomologous Kahler form omega'=omega+t ddc g yields mu'-mu=t eta_y ddc g !=0. Indeed dd c g cannot vanish for a nonconstant real function on compact P1 (a pluriharmonic function is harmonic and the maximum principle makes it constant), and its local nonzero coefficient remains nonzero after wedging the positive area form on the other factor. Both masses equal1. Thus this actual measure on X needs the full form, even at fixed class and mass. Scaling omega by c scales mass and energy by c^(n-d). This establishes necessity for this construction; it does not characterize the minimum choices for every conceivable theory.

In the same class choose D={y=0}xP1 and its logarithmic reference with T_psi=[D]. With our convention, ddc log|s|_h^2=[D]-theta: locally ddc log|z|^2=delta_0 because the normal derivative of log r^2 has flux4pi and ddc acts as Delta/(4pi) times area; subtract the smooth metric weight. The current vanishes off D, and its nonpluripolar products omit D, so <T_psi>=0 and its actual degree is d=0. The class has usual nef numerical dimension1 by alpha[omega]>0 and alpha^2=0. Hence actual-type degree need not equal class numerical dimension. In degree0 the operator is omega^n; it retains the type in its domain but does not distinguish potentials in its output. A current of bidegree(d,d) still lives on X of dimension n and does not by itself produce a geometric d-dimensional quotient.

Scope relative to the unchanged catalogue: n1 removes the supplied-fibration hypothesis for its specified bounded actual-type domain, and n2 proves an unbounded full-mass operator with decreasing continuity. These are substantive partial applications for arbitrary pseudoeffective zero-volume classes. They do not establish minimum-reference data, a general intrinsic lower-dimensional geometric carrier, convergence under arbitrary perturbation choices, or a full unbounded finite-energy/cocycle/path theory. The supplied mixed-volume verdict, source-prose descriptions and another worker's results are not used. No priority claim is made. Status is partial and candidate=false.

Authoritative deliverables are P15.2-argument.md (147,587 bytes at the recorded build), P15.2-partial.tex (standalone full new proof), P15.2-partial.pdf (10 pages, twice compiled), and status.json with exactly id,status,exact_result,proof_file,concrete_gaps. Audit files: source-audit.json, author-audit.json, environment.json, research-audit.json and build-audit.json. Canonical notes are native-notes.json. Original input bytes are preserved in input.json and input-original.json.

Rerun: python build.py, then python finalize.py. The source program extracts LF slices by raw.split(b'\\n') and joins the specified range without adding a final LF. All14 supplied SHA256 slice digests match the read-only shared sources, and all14 supplied quotation strings equal those raw slices. The argument includes those complete primary units, including the printed source defects, plus5 additional foundation slices. Vu source pages4/6 were visually inspected for the convention and half-factor. The scalar identity diagnostic checked5,455 exact integer instances with n<=30, all passing; the all-n proof remains subset counting. Both pdflatex passes exited0, with no warnings, undefined control sequences or overfull boxes. No analytic correctness follows from these checks.

Programs, input, commands, outputs and environment metadata remain in the fresh workspace. No network, install, subagent, additional model, external message, heavy unsupervised compute or configuration/credential change was used. Requested execution identity is recorded; no callable model-identity attestation was exposed, so it is not independently certified. The runtime skill was read for the initial read-only check; its environment_status tool was unavailable. No heavy compute facility was needed.

Concrete outstanding steps: a weighted-tail proof for the finite-energy extension and its lower-degree perturbative terms; unbounded numerical cocycles and reference changes; unrestricted operator perturbation limits; and a general carrier/minimum-reference theorem. The original P15.2 is not claimed solved.""",
    "support": ["n1", "n2"],
}
n3["text"] = n3["text"].replace("147,587", format((ROOT / "P15.2-argument.md").stat().st_size, ","))
notes = {"notes": [n1, n2, n3], "candidate": False}
(ROOT / "native-notes.json").write_text(json.dumps(notes, indent=2, ensure_ascii=False) + "\n")
research = {
    "scope": "P15.2 only",
    "new_complete_partial_proofs": [
        "Arbitrary-pseudoeffective bounded-type operator: degree, mixed vanishing, actual mass.",
        "Signed IBP sufficient perturbation convergence and smooth-form extension.",
        "Bounded primitive, cocycle, correct positive-gradient concavity, reference-class invariance.",
        "Exact perturbative energy coefficients and arbitrary-representative class-convergent limit.",
        "Unbounded relative-full-mass operator with decreasing continuity.",
    ],
    "standard_foundations": [
        "BEGZ nonpluripolar products and positive-product volume definition.",
        "DDNL bounded-type mixed mass equality and pseudoeffective monotonicity.",
        "Vu v3 admissible gradient IBP and relative-energy definitions/convexity.",
        "Vu relative product local lower semicontinuity with constant smooth relative current.",
        "Smooth compact-Kahler ddc lemma.",
    ],
    "failed_or_unfinished_routes": [
        "Inferring weighted convergence from weak measure convergence leaves a tail gap.",
        "Inferring lower-degree weighted integrability from degree-d finite joint energy is unsupported.",
        "Inferring form-free operator convergence from class-convergent energy is disproved by the test.",
        "Reading class numerical dimension as the actual-current degree fails for a divisorial reference.",
        "A (d,d) product current alone does not construct a geometric d-dimensional carrier.",
    ],
    "original_remaining_gaps": gaps,
    "finite_diagnostics": json.loads((ROOT / "coefficient-check.json").read_text()),
    "proof_status": "Unverified mathematical draft; partial relative to original atom.",
    "candidate": False,
}
(ROOT / "research-audit.json").write_text(json.dumps(research, indent=2) + "\n")
artifacts = sorted(p for p in ROOT.rglob("*") if p.is_file()
                   and p.name != "artifact-manifest.json")
(ROOT / "artifact-manifest.json").write_text(json.dumps({
    "rerun": ["python build.py", "python finalize.py"],
    "files": {str(p.relative_to(ROOT)): {
        "bytes": p.stat().st_size,
        "sha256": hashlib.sha256(p.read_bytes()).hexdigest(),
    } for p in artifacts},
}, indent=2) + "\n")
print(json.dumps({"status": status["status"], "candidate": False,
                  "notes": len(notes["notes"]), "manifest_files": len(artifacts)}))
