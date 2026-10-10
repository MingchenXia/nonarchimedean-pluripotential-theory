# Sequential source notes: Kang parabolic comparison, 8 October 2026

All 21 primary pages and eleven matching views were actually read. Note 11 corrects note 10's provisional authorship for reference 21; the source audit and direct diagnostic control later conclusions. Historical prospective language is not retroactively rewritten.

# Actual primary reading 01: Kang v3, physical pages 1–2

Complete selected text was read, followed by individual display and inspection of the matching two-page image. The controlling PDF is arXiv:2511.06412v3 (15 December 2025), SHA256 cf73b37f57d7b214da0ce1f8958d600b35eff59553ba69ded72211691f157aeb. These pages are introductory statements, not proof clearance.

The setting is a bounded strictly pseudoconvex domain in C^n, finite positive time horizon, bounded spatially plurisubharmonic potentials with local uniform Lipschitz time dependence. The supersolution in the recalled comparison theorem also has local uniform time semiconcavity. F is continuous, nondecreasing in its last argument, bounded on bounded last-argument sets, and locally uniformly Lipschitz and semiconvex in the time/last-argument pair. Preserve these requirements and the ordered spatial boundary data, distributional t^2 second-time-derivative bound and t first-time-derivative bound.

The new measure is assumed dominated by the Monge–Ampère measure of a bounded psh function with zero boundary limit. The asserted equivalence with a bounded zero-boundary solution is an imported Kołodziej subsolution theorem; its controlling edition and exact signature need inspection before a load-bearing import. No positive Lp Lebesgue density is assumed for this proposed generalization. Initial convergence is stated in L1(Omega, mu), while lateral convergence is joint pointwise convergence to continuous data. Do not silently replace either trace with a weaker one, assume finite total mass, or extend this domain result to compact singular spaces or non-Archimedean flows. The dd^c convention has not yet been located.


# Actual primary reading 02: Kang v3, physical pages 3–4

Complete selected text and the individually displayed matching image were read. Theorem 1.2 requires local uniform time semiconcavity of both the subsolution and supersolution, rather than only the latter in the recalled positive-density theorem. It retains t|h1_t| <= C but omits the boundary second-derivative requirement from comparison; existence in Corollary 1.4 still imports the earlier paper and keeps both boundary derivative conditions. General joint continuity is expressly unavailable, motivating a different argument. The proof is identified with Theorem 3.8, not yet read.

The long-time statement has zero lateral data, initial data equal to the bounded zero-boundary elliptic solution psi of MA(psi)=mu, and time-independent F(z,r). Its positive lower slope LF must cover the relevant r interval; the printed J is not specified in the statement and must be made explicit in an eventual account. Uniform convergence to the stationary equation is an asserted result awaiting its proof. Do not convert it into a general convergence result for arbitrary initial data, a compact Kähler flow, or a non-Archimedean evolution. No proof or source-recursive credit is claimed for the historical survey references.


# Actual primary reading 03: Kang v3, physical pages 5–6

Complete selected text and the individually displayed matching image were read. The parabolic Monge–Ampère measure is defined by integrating the spatial Bedford–Taylor measures against dt. Local uniform time Lipschitz dependence supplies weak continuity for compact continuous tests through the imported GLZ lemma; local CLN bounds provide finite cylinder mass.

Lemma 2.2 extends measurability to all Borel time-space sets by continuous approximation of compact sets, compact exhaustion of opens and a finite-cylinder monotone-class argument. This avoids treating sublevel indicators as continuous tests. Equation (2.2)'s displayed section integrals should include the I time restriction (or be read for t in I, with zero outside); the intended bounded-cylinder argument is clear. Lemma 2.3 begins the corresponding Borel slicing identity. Choose J and K with the relevant compact set contained in their interior to permit the claimed common-support continuous majorants. No global total-mass bound is provided or needed here. The definition and CLN input still require controlling primary references if imported as load-bearing facts.


# Actual primary reading 04: Kang v3, physical pages 7–8

Complete selected text and the individually displayed matching image were read. The Borel slicing identity concludes by compact/open approximation and regularity. The elliptic comparison inequality is applied slice by slice, then integrated on the genuine Borel set {v<u}. Spatial convolution used for decreasing approximation should be radial; arbitrary positive smooth mollifiers need not give a decreasing psh regularization. Joint upper semicontinuity and the continuity of the regularization make the sublevel sets Borel.

The parabolic maximum and domination arguments add epsilon(|z|^2-R^2), obtain a positive Lebesgue component and then use the psh/time-Lipschitz property to upgrade Lebesgue-a.e. order to everywhere order. For the integral subtraction, first restrict time to (0,T') and use the common compact spatial support of the strict sublevel set; local CLN gives finite mass. Passing T' upwards avoids cancelling potentially infinite masses. Lemma 2.6 contains a notation slip: the displayed proof uses phi_epsilon=u+epsilon rho, although its first line instead introduces u_epsilon=phi_epsilon+epsilon rho with phi_epsilon undefined. Record the intended perturbation without copying this typo.

Lemma 3.1 begins a mixed Monge–Ampère inequality. Its density f must be nonnegative for f^(1/n) to be defined in general, although the printed signature only says L1. The proof and controlling mixed-inequality input are still unread. No main-comparison clearance is claimed at this point.


# Actual primary reading 05: Kang v3, physical pages 9–10

Complete selected text and the individually displayed matching image were read. The mixed inequality is imported from Dinew Theorem 1.3, and the mixed comparison inequality from Bedford–Taylor/Nguyen. These are actual source locators but have not yet been recursively inspected.

Lemma 3.3 constructs an initial lower barrier for a supersolution by the bounded zero-boundary elliptic solution psi, a boundary modulus delta(s), and n(t log(t/T)-t). The time-shifted supersolution V^epsilon includes a linear correction for F's time Lipschitz bound. Its proof explicitly uses local time semiconcavity of V^epsilon although Lemma 3.3's printed statement does not assume it. Retain semiconcavity of v for any use here; it is available in the main theorem. The displayed v(t_k,z)->v(0,z) line is a sequence-notation typo for v(epsilon_k,z)->v0(z). Constants and F bounds near t=0 must be checked rather than assumed globally uniform from local time regularity.

Lemma 3.4 is a key specialized comparison: ordered lateral boundary, zero mu-measure strict sublevel near t=0 for every tolerance, both time-semiconcave, the mixed differential inequality, supersolution inequality, and an everywhere-defined locally time-Lipschitz derivative for the subsolution. Its first-crossing t1 is defined through positive mu section mass, so time persistence and a.e.-to-pointwise upgrading are necessary. The proof has only begun; no main theorem clearance yet.


# Actual primary reading 06: Kang v3, physical pages 11–12

Complete selected text and the individually displayed matching image, including the first-crossing schematic, were read. The zero initial strict-sublevel mu mass passes to MA(v) via absolute continuity; domination then empties the strict sublevel. Around the first positive-mu crossing time, uniform semiconcavity and the subsolution derivative Lipschitz bound turn the backward difference inequality into u_t > v_t^- + epsilon/2. F's monotonicity makes the mixed mass at least exp(epsilon/(2n)) times MA(v), while mixed comparison makes it at most MA(v). Finite mass then forces it to vanish, and domination contradicts the crossing.

An explicit account must first handle the case that every section has zero mu mass: the supersolution inequality plus domination already empties E, so the infimum of an empty set is not used. For the nonempty positive-mass case, choose a compact time window inside (0,T), shrinking the printed epsilon-tilde radius additionally by T-t1 if necessary. Strict lateral separation gives common compact spatial support and finite CLN mass, so the exponential-factor cancellation is justified. Slice inequalities and the identification of v_t with its one-sided derivative hold only for a.e. t and mu-a.e. z; Fubini and MA(v)<<mu are essential. The schematic itself supplies no continuity of mu-section masses. The specialized lemma is plausible with these routine details, conditional on the mixed-comparison and domination inputs. Main general-time regularization remains unread.


# Actual primary reading 07: Kang v3, physical pages 13–14

Complete selected text and the individually displayed matching image were read. Remark 3.5 obtains the mixed inequality from the slice sub/supersolution inequalities and Dinew. Uniform initial convergence would directly give the near-zero strict-sublevel condition; its delta must be uniform in z, as the stated uniform convergence permits.

Lemma 3.6 instead assumes, for every relatively compact open U, a bound integral_U u(t) <= integral_U u0 + A_U t, a supersolution-type initial lower bound v>=v0-eta(t), ordered initial values and ordered lateral boundary. Its third step in (3.7) replaces the integral of (u-u0) on the variable strict sublevel E by A t times mu(E). This does not follow from the stated integral bound on U. The constant depends on U, and the assumed bound is signed; it does not supply pointwise u-u0<=A t or a uniform bound on arbitrary measurable subsets. The added factor mu(E) is also unsupported.

A candidate diagnostic is radial spatial regularization of a bounded discontinuous subharmonic function, static v=u0, and mu=Lebesgue measure: local total regularization error can be O(t) when the radius is sqrt(t), while fixed-amplitude errors in arbitrarily small logarithmic wells persist. This must be constructed and checked explicitly before any counterexample credit. At present record the unsupported step only; it does not itself refute Theorem 3.8, whose flow inequalities add hypotheses. The main proof begins with t|u_t|<=B and multiplicative time regularization W^s=s^-1 u(st)-C|s-1|(t+1); its later use of Lemma 3.6 needs inspection.


# Actual primary reading 08: Kang v3, physical pages 15–16

Complete selected text and the individually displayed matching image were read. The main proof imports GLZ Theorem 4.2 to make W^s a subsolution with ordered boundary and asserted mu-a.e. pointwise initial limsup. It averages W^s in the positive multiplicative time parameter, producing Phi_epsilon with an everywhere-defined locally time-Lipschitz derivative by integration by parts in s. Use a sufficiently small parameter support so st remains inside (0,T) for t<S; positive normalization and spatial psh are necessary.

Linearity of dd^c against MA(v)'s mixed current allows Fubini; Dinew and Jensen then give the mixed exponential bound for Phi_epsilon, with an O(epsilon) loss in F. Compactly supported smooth spatial tests justify the integration by parts. The t|u_t| bound controls W^s-u uniformly for s near 1, so F's local last-variable Lipschitz bound can make this loss uniform; the cited GLZ endpoint still requires inspection. Exceptional slice-time sets may depend on s, so the averaged argument must first use Fubini in (s,t), not simply fix a t good for every s. These pages do not repair Lemma 3.6's signed-integral-to-subset step. The claimed pointwise initial limsup is stronger than the printed L1 initial trace and remains an input requiring independent source inspection.


# Actual primary reading 09: Kang v3, physical pages 17–18

Complete selected text and the individually displayed matching image were read. The main proof explicitly invokes Lemma 3.6 after establishing only the signed open-set integral estimate (3.15) by CLN and Jensen. No stronger uniform pointwise or arbitrary-subset estimate is supplied here. Thus the previously identified (3.7) step is load-bearing in the stated comparison proof. The conclusion remains unverified, not disproved by this audit.

The final removal of t|u_t|<=B has additional problems: the printed 0<epsilon0<S-T is impossible because S<T (the intended upper bound is T-S). The time-shift U^epsilon0(t)=u(t+epsilon0)-kappa_F epsilon0 t has actual lateral data h1(t+epsilon0)-kappa_F epsilon0 t and initial data u(epsilon0), whereas the proof assigns h1(t)-kappa_F epsilon0 t and preserves the old initial ordering. Neither replacement follows from local time Lipschitz dependence and the L1 initial trace. A lateral modulus can address one issue, but initial order requires a separate argument; do not treat it as a typographical repair. F's time Lipschitz bound on [0,S] also needs justification from its stated local regularity.

Corollary 3.9 imports existence from Kang's earlier Theorem 4.5 and uniqueness from this unverified comparison; the displayed initial value h(0,.) should be u0 because h is defined on the lateral boundary. Finite-horizon gluing alone yields boundedness on each finite cylinder, not necessarily a single L-infinity bound for all positive time. The stationary convergence proof follows next and may be audited conditionally on comparison, but its theorem is not cleared here.


# Actual primary reading 10: Kang v3, physical pages 19–20

Complete selected text and the individually displayed matching image were read. The stationary solution is an import of Kołodziej–Nguyen Theorem 1.1; admissibility/pointwise initial convergence is an import of the earlier Kang existence paper. The printed lower-slope interval J must contain every argument used in the barrier, not just the range of the stationary solution. Choose LF<=kappa_F using the lower and upper slope bounds on that whole bounded interval.

The lower barrier combines exp(-LF t) psi, (1-exp(-kappa_F t)) psi_infinity and Phi(t) exp(-LF t), with Phi=(n/LF)(exp(LF t)-1)log(exp(LF t)-1)-nt exp(LF t). Its derivative and bounded vanishing correction can be checked directly. The upper slope compensates the positive shift -exp(-kappa_F t) psi_infinity; the lower slope controls the remaining negative shift. The spatial Monge–Ampère lower bound keeps only the stationary component and uses kappa_F>=LF. The upper barrier (1-exp(-ct))psi_infinity+exp(-ct), c=n/(1+||psi_infinity||), uses log(1-x)<=-x. Both explicit computations are conditional barrier arguments; applying the unverified general comparison theorem is the load-bearing step in their resulting uniform convergence. Do not promote the general-measure convergence claim without a valid comparison input. Bibliographic references 1–11 are actually visible here but their proofs remain unread.


# Actual primary reading 11: Kang v3, physical page 21

The complete final-page text and individually displayed matching image were read. The full controlling twenty-one-page v3 has now been read in eleven matching views; bibliographic inspection is not recursive proof clearance. Reference 17 is GLZ's 2021 Annales ENS Cauchy–Dirichlet paper, reference 20 is Kang's 2025 JGA general-measure existence paper, reference 6 is Dinew's 2009 mixed-measure paper. Reference 21 is Sławomir Kołodziej alone, Annales Polonici Mathematici 73(1), 59–67 (2000), not Kołodziej–Nguyen as the provisional note 10 mistakenly described it. This correction controls that earlier note; the historical note is retained.

No dd^c normalization is explicitly defined in the inspected v3, so any imported numerical conversion would need the controlling convention from a cited foundation. Main comparison, general-measure uniqueness and the resulting long-time convergence remain UNVERIFIED owing to the load-bearing Lemma 3.6 step and the time-shift initial/boundary issue. The proposed logarithmic-well diagnostic is still to be checked before being described as a counterexample. No book insertion, original theorem promotion, canonical open-problem status change or independent-model receipt is claimed.
