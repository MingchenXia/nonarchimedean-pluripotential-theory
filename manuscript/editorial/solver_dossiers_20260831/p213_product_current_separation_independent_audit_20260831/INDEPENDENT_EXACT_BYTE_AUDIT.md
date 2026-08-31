# Independent exact-byte audit: product branch transport and current separation

Date: 2026-08-31. Reviewer: /root/p213_skeletal_hostile.
Candidate author: /root/p082_independent_reaudit.

## 1. Verdict, independence, and exact boundary

PASS for the new branch-transfer theorem in Sections 2--4, the two non-separation diagnostics in Section 5, and the all-moments conditional equivalence (14) in Section 6, SUBJECT TO the stated product premise and, only for the indicated source-cell interpretations and (14), the separate representation premise (R).

One proof-explication is required in the ORIGINAL last accessibility paragraph, lines 257--259: affine coordinate agreement on a shared skeletal patch must be converted to a comparison of actual source forms or evaluated through a genuine analytic combined moment. The sentence asserting the same local coefficient measure omits that bridge. This does not affect the branch theorem, either rank obstruction, or equivalence (14). No counterexample to its explicitly isolatable shared-source-patch hypotheses was found; a source-exact clarification is feasible. The author has been asked to preserve the original and place any clarification in a separate supplement or revision. This report fixes its verdict to the exact original bytes below.

The reviewer authored the earlier product residual-functional statement/proof. Those files are therefore ASSUMED INPUTS here, not independently re-certified by their own author. Their separate independent audit by the present candidate author is recorded as provenance. The reviewer did not author this new branch-transfer proof, the mixed-coordinate example, or the conditional separation criterion, and did not edit the candidate or supply a replacement proof.

This is not production verification, not an independent proof of (R), not scalar rigidity on the whole product, and not a solution of P21.3. No live files, frozen candidate files, or prior audits were edited; no production or git command was used.

## 2. Exact original files

Candidate directory:
 /private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260831/p213_product_current_separation_research_20260831

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| RESEARCH_NOTE.md | 20076 | d4f1458e0849164c1a45d168238467c13222ccae427493069ed97f43cd789b81 |
| SOURCE_LEDGER.md | 7108 | 568f7a92f88e18821d3698c8fd35499440f3bcffc106dfb3fffc32f19b8de578 |
| MANIFEST.json | 3164 | 2afe7e91903a021751d59da7c02c7be1826dc3dc223a87f256a1482e7f58a440 |
| SHA256SUMS | 1287 | 572e93bc8e7fac20fd75ae368fa3405f74b0d50fa6d1628183550de7d80db892 |

All ten candidate-manifest entries matched their recorded hashes. Running the supplied SHA256SUMS from its own directory checked all eleven entries successfully. The note, complete ledger, complete manifest, checksums, and representation interface were read. The exact product input hashes and the primary CLD PDF/text are included again in this audit's manifest.

## 3. Analytic inverse and finite-field normalization

The conditions N >= 2 and N invertible in R are both used and correctly stated. The first puts ell/N strictly inside the original annulus. The second permits the coefficient recursion for P(T)^N=1+T with constant coefficient one.

At degree j in that recursion, the new coefficient has multiplier N; all remaining expressions use previously determined coefficients and integers. Thus every coefficient belongs to R, including in positive or mixed characteristic. The series converges uniformly on each closed disc of radius less than one. Its constant term strictly dominates the other terms at every point of the open unit disc, giving |P|=1 there. No characteristic-zero binomial formula or convergence at radius one is needed.

The product premise supplies the complete unramified DVR R_p, where pi remains a uniformizer. Consequently Z^N-pi is Eisenstein over R_p. The field L_p has degree N over K_p, residue field kappa(p), and degree N*d_p over K. This is a ramified extension, not a residue-only degree contribution.

On the actual source where 0<|t|<1, t=z^N/pi-1 is analytic and P(t) is an analytic unit. The function a=z/P(t) satisfies a^N=pi, giving a coefficient-field homomorphism from L_p. Conversely the explicit formula z=aP(t) has |z|=|pi|^(1/N), strictly between |pi| and one, and satisfies z^N/pi-1=t. Both maps preserve w and are inverse. The formulas work on closed annuli exhausting both open coordinates, so they give an analytic isomorphism, not only a bijection on classical points or on a skeleton.

No roots of unity assumption is hidden. All conjugates are encoded by the one L_p-domain viewed over K. There is no claim of N ordinary-open sheets. The current is restricted to an ordinary open K-analytic domain and is not pulled through a field extension.

The primitive coordinates on that L_p-polyannulus are t and w. CLD14.4.3 multiplies its canonical calibration one by the full field degree N*d_p on viewing it over K. Ramification is permitted by the exact source statement. The factor N is not then inserted a second time as a lattice index. The equality B=N*b is compatible with canonical B=N*d_p and b=d_p.

The source coordinate a is algebraic and constant as an L_p coefficient; it is not treated as an additional independent tropical coordinate. This is important for both the dimension and degree bookkeeping.

## 4. Finite B and the complete closedness calculation

Compact subsets of the target rectangle (0,infinity)x(0,delta) have compact inverse images, contained in closed polyannuli over L_p. Every compact target top form and every primitive used to differentiate the scalar distribution therefore pulls back with compact analytic support. Extension by zero is legitimate.

Positivity gives a locally finite positive scalar measure by the usual compact-cutoff sup-norm bound. Closedness makes both target distributional partial derivatives zero. Euclidean mollification, an integral-one test, and overlapping target balls then give one finite constant B>=0. This argument is independent of (R), current slicing, and any common dominating measure for unrelated chart coefficients.

The three exact norm regions in (4) follow from strict ultrametric domination. On u<u_0 one has r=Nu-ell; on u>u_0 one has r=0 on the whole ordinary open region; and r>0 forces u=u_0 on an ordinary open branch domain. No local constancy is claimed at the central set.

The compactly supported eta(u), xi(s), and chi(r) place u,s in a compact closed source polyannulus and bound |t| away from zero. The support of beta is closed in that compact set and stays away from every removed boundary and t=0. This supplies the source compactness needed for the closedness test.

The sign and differential computation in (6) are correct. Differentiating xi repeats d's. In the eta'-term:

- on the left, eta' can occur only outside the plateau, where r<=-Na and chi=0;
- on the right, d''r=0;
- on the positive branch, u=u_0 and eta'=0.

Both eta' and chi' vanish on a genuine neighbourhood of the central pair (u_0,0); continuity of (u,r) then gives ordinary-source neighbourhood vanishing of the full differentiated form. This is stronger than a claim of unknown-current nullity on a lower-dimensional face and is exactly what makes its two-piece support decomposition valid.

The left piece is a legitimate old collar target test: its scalar coefficient is smooth after extension because it vanishes near u=u_0 and at the other relevant boundaries. Its integral is

\[
 b\int_{u<u_0}
   \bigl[N\eta'(u)\chi(Nu-\ell)+N^2\eta(u)\chi'(Nu-\ell)\bigr]\,du
  =Nb.
\]

The upper endpoint value is one and the lower endpoint value is zero. Although the eta'-summand vanishes pointwise under the chosen cutoffs, retaining it as the total derivative is harmless and gives the same result.

The positive piece uses a test supported away from r=0, where eta=1, and has integral B*(chi(infinity)-chi(0))=-B. Thus closedness gives 0=Nb-B. There is exactly one surviving N: the two differential factors give N^2, and the change of variable removes one. No normalization ell=1 or additional ell factor is used.

This independently verifies the new equality B_T(p,N)=N*b_T(p) under the assumed old coefficient formula (1). The further equality b_T(p)=c*d_p is used only as the explicitly assumed prior result.

## 5. The non-separation diagnostics are genuine and correctly limited

### 5.1 Old collar forms miss a new branch

On D_{p,N}, u is constant, so old top forms containing d'u wedge d''u vanish as actual forms. Multiplying by arbitrary smooth source functions does not change that. Distinct residual-point tubes are disjoint.

The function h(r,s) has compact analytic support by properness of the new collar map. Its zero extension defines the nonzero positive current S=h*delta_X. It is invisible to all old collar tests. The displayed gamma is also a legitimate compact test and

\[
 \langle S,d'\gamma\rangle
 =-N d_p\int(\partial_r h)^2<0.
\]

The strict inequality follows from the explicitly chosen nonzero partial derivative. This proves S is not closed; the author does not mislabel it as a counterexample among positive closed currents.

### 5.2 The mixed t,q domain defeats even all transported integer families

In the actual L_p-domain, the change of variables q=w-t has inverse w=t+q. On the stated rectangle, v(q)>v(t), so |w|=|t|, and w stays in the original curve collar. The domain is an actual product polyannulus in t,q over L_p; its compact target tests have compact source support. Its canonical coefficient is N*d_p.

On this whole ordinary domain u=ell/N and s=r. The old (u,s) and transported (r,s) top forms therefore vanish. For M!=N, v(z^M/pi)=(M/N-1)ell has a fixed nonzero sign, so v(z^M/pi-1) is constant. Its positive-branch domain is disjoint from E. This checks ALL the stated integers M, not only a finite subfamily.

The formal-parameter observation also has the necessary margin: b<ell makes |w|>|pi|; the unit linear term of w' then dominates the pi-divisible constant and the higher terms, giving |w'|=|w| throughout E.

The t,q top form alpha has strictly positive canonical integral N*d_p*integral(rho). Hence it is not in the local module generated by the known collar top forms with arbitrary source multipliers. A smooth positive bump on E pairs nontrivially with alpha and annihilates that entire module, so continuity also rules out the claimed density shortcut in the test-form topology.

This diagnostic is NOT a closed-current obstruction to a future comparison involving q. It is a counterexample only to the alleged generation/density of the displayed known test family. The note preserves that distinction.

## 6. Conditional criterion (14) versus the final accessibility paragraph

Equivalence (14) is correct under (R) for all the ordinary moment domains used. CLD15.1.1(b) supplies ordinary-open moment descriptions of a given smooth top form. Shrinking the source around its compact support also permits ambient representatives of the target forms. CLD15.2.9, read together with the correctly quantified underlying Corollary6.2.8, supplies locally finite compact source cutoffs; only finitely many meet that compact support.

Each localized piece is therefore of the form to which (R) applies. The equality of EVERY top-cell ratio gives equality of both pairings, and (R)'s absence of a lower-cell residual ensures no extra term survives. Conversely uniqueness of the same coefficient representation gives the ratios when T=c*delta_X. The source multipliers and ordinary-open clause are essential; neither a G-cover nor one selected moment suffices.

The last paragraph makes a different assertion: its proposed source-cell accessibility hypotheses would transfer one already-known G-ratio to an F-cell. At original lines257--259, the argument says that two source-cell formulas give the same local coefficient measure but does not explicitly establish a common SOURCE FORM. Merely knowing an affine relation between F and G ON P would not make an arbitrary F-pullback a G-pullback on an ordinary neighbourhood.

This is a real proof-explication requirement, not a failure of the core result or an assertion that the stated strong interior-isolation hypotheses are false. Two source-exact ways to address it are available:

- specify a genuine analytic combined moment H=(F,G), assume/use its representation on the same ordinary domain, and isolate an actual common interior source patch on which both projections have full rank; compare each J-pullback using the identity J*=H* p_J*;
- under the literal shared-interior-patch isolation in the original, explicitly invoke CLD5.3.1,5.3.4,5.3.6 to compare suitable target volume forms after their pullbacks are strongly supported on the SAME isolated source skeleton.

The latter observation explains why the issue is an omitted bridge rather than an identified counterexample: after genuine shared-source isolation, agreement of suitably normalized restrictions can be detected as equality of forms. Without that support argument, or without a specified analytic common moment, affine value agreement is inadequate.

This audit does not silently certify the original paragraph as a complete proof, assume general accessibility, or turn target overlap into source overlap. An author-supplied exact supplement is to be reviewed separately. The all-moments criterion itself remains accepted conditionally and unchanged.

## 7. Sources, artifact checks, and remaining scope

SOURCE_AUDIT.md records the exact primary interfaces and visual checks. CLD14.4.3 was read directly and includes the full finite field degree. CLD15.1.1(b) and15.2.9/6.2.8 were checked with their ordinary-open and compact-source hypotheses. The support facts needed to explain the last accessibility omission were separately read in CLD5.3.1,5.3.4,5.3.6; they are not part of an assumed ordinary-sheet construction.

No TeX or PDF artifact is present in the candidate, and no compilation is claimed here. Checksums and control-byte scans are preservation checks, not proof certificates. All new statements remain outside any production pipeline.

Full product rigidity, arbitrary moment accessibility, nontrivial normal-bundle transfer, nondiscrete valuations, and N divisible by residue characteristic remain outside this reviewed packet. The independently reviewed new theorem is the bounded transport relation, not P21.3.

