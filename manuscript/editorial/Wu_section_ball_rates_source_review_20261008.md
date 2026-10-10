# Curve section-ball rates: primary-source review, 8 October 2026

Hao Wu's arXiv:2604.12333v1 reports O(log n/n) real unit-ball volume errors and O(sqrt(log n/n)) C2-test errors for Fekete measures on compact Riemann surfaces. The complete 28-page primary source and 68 selected dependency pages have actually been read with 48 matching images. The numerical statement for unrestricted line-bundle degree cannot be copied literally. The safe proposed use is an explicitly attributed account in degree one, genus at least two, sufficiently large tensor degree, fixed C2 compact domains, bounded Hölder weights, and fixed Bernstein–Markov or mass-density data where relevant. Higher degree must transport the index and the external field together. This is an import and convention audit, not an original theorem promotion or independent verification receipt.

## Controlling source coverage

| Source | Actual pages | Scope |
|---|---:|---|
| Wu 2604.12333v1 | 28/28 | Full primary reading |
| Dinh–Ma–Nguyen, published 2017 | 34/34 | Full dependency reading, including variational proof |
| Klevtsov 1712.09980v3 | 18/33 | Pages 1,2,5–18,27,28; determinant and Green conventions |
| Zelditch 1101.0417v1 | 6/53 | Pages 1,2,31–34; not the 2013 journal pagination |
| Wu 2512.10852v1 | 6/17 | Pages 1–6; boundary-envelope input, not the full hole proof |
| Berman–Boucksom, published 2010 | 4/59 | Pages 41–44, new relative to the earlier Finski selection |

The earlier actual BB10 Theorem A reading remains the controlling imported input for the elliptic degree diagnostic. It confers no additional fresh reading credit here. Preparation, searching, metadata, note concatenation and export confer no reading credit. Cited classical inputs and omitted pages remain attributed, unexamined dependencies.

## Normalizations and safe scope

The source D=i/pi partial bar-partial equals twice the book operator. A section norm is multiplied by exp(-n phi); its squared metric is therefore multiplied by exp(-2n phi). The volume is ordinary real volume in complex rank N_n, with functional (n N_n)^-1 log volume, twice BB10's functional. In degree one N_n=n-g+1 only in the nonspecial, sufficiently large range. Use a fixed positive weight budget 1+B, and constants depending on the fixed geometry and measure data.

The mean-zero Green potential satisfies D U_nu=nu-omega and integral U_nu omega=0. Its external-field functional is -integral U_nu dnu+2 integral phi dnu. The equilibrium measure for degree d is obtained with phi/d and the limiting energy is d times that degree-one minimum. At root index k=dn the exact volume identity is V_n^(L_1^d)(phi)=d V_k^(L_1)(phi/d). A nonconstant positive elliptic example phi=cos(2 pi x)/(4 pi) has integral phi D phi=-1/(16 pi); BB10 gives volume limit -1/(16 pi d), whereas the printed unscaled omega-energy gives -1/(16 pi). The six exact degree fixtures d=2,…,7 detect the discrepancy. Constant shifts correctly give 2a and do not detect it.

## Dependency repairs and exclusions

1. The printed root construction proves equality only after a genus power, leaving a torsion ambiguity; existence of a root follows instead from surjectivity of multiplication on Pic^0. No canonical root is asserted. The literal Arakelov constructions divide by g or 1-g, so the proposed account keeps g>=2.
2. The smooth metric correction in Wu's determinant calculation is -2g psi, not -2 psi, since 2(N_n-1)-2n=-2g. It is fixed and contributes O(N_n), so the rate argument survives this repair in the restricted range.
3. Klevtsov (3.27) prints exp(-G_A) over unordered pairs for a squared determinant, while (4.39) fixes G_A~ -log distance. A generic collision needs order two. Use the calibrated exp(-2 G_A) over unordered pairs, or exp(-G_A) over ordered pairs, as dictated by Fay's prime-form identity and the local singularity. The printed numerical equation is not a certificate. The degree-dependent scalar normalizer is retained and estimated separately.
4. Zelditch v1 (71) squares the Gram determinant and fails the ordinary basis-scaling test; (72) puts i in a Gaussian squared-norm exponent. Neither is copied numerically. The published BB10 Lemma 5.3 instead gives integral |det S|^2=N! det Gram with one Gram determinant. Its actual source proof and the real-volume ratio are read on printed pp.376–377.
5. Wu 2512.10852v1 Lemma 2.3 is false for arbitrary negative continuous boundary data. On CP^1 with rho=log(1+r^2)/2, omega=D rho and u=-a+A cos theta on the unit circle, the negative piecewise Dirichlet solution has boundary curvature (1-2A cos theta)dtheta/(2 pi). For A>1/2 and a>A+log(2)/2 this is negative somewhere. The three claimed envelope properties would force that solution by Dirichlet uniqueness. Wu's actual section-ball regularization uses the trace of an existing Green potential instead; its contact follows from that admissible potential, and local harmonic balayage supplies the required smoothing. The arbitrary-trace lemma is not imported.
6. Three O(m^2 log m) errors in Wu Lemma 5.3 need inverse powers, as its preceding Lemma 5.2 gives O(m^-2 log m). Ordered off-diagonal sums retain collision energy -infinity; deleting the geometric diagonal would erroneously discard coincident labels.
7. DMN uses positive shorthand norms 1+ordinary norm. Early conditional zero-weight objections in the frozen primary notes are therefore not established defects if that convention is inherited. The controlling text uses fixed 1+B bounds. Exponentiating a Hölder estimate still gives budget-dependent constants, not a globally linear bound in the ordinary weight norm.
8. DMN's envelope Hölder theorem uses 0<alpha<1; the endpoint is log-Lipschitz. Lipschitz external fields can use a fixed smaller alpha. No Lipschitz-envelope endpoint is claimed.
9. Theta-safe replacement needs product boxes contained in neighborhoods where the theta norm has a positive lower bound, with finite compactness over the Jacobian parameter. Independent coordinate projections of one ball do not suffice. Replacing g points changes 2gm-g(g+1) ordered pairs. Perturbations and chart/separation bounds hold for sufficiently large m.
10. Wu p.25 reverses the determinant/volume sign already fixed by (4.2). The volume has the negative logarithm of the determinant integral plus log N!; p.27 also needs the envelope-weight functional on X before identifying its minimum with the original K-functional. The source's final leading sign is recovered with these repairs. Logarithms of theta bounds and all measure constants are retained.
11. The full primary source states the Fekete corollary without a separate final proof. DMN's fully read Lemmas 3.13–3.14 and main-proof endings supply the concavity mechanism: uniform volume error epsilon gives C2-test error O(sqrt(epsilon)). No optimality claim or separate independent proof receipt is attached.

The diagnostic records contain six finite fixture groups (38 fixtures) and six exact symbolic sphere checks. They are direct examples and convention checks, not a general theorem certificate. The book's 42 canonical atoms and 12 formal open problems remain unchanged; BJ22 Theorem 6.21 does not acquire a valid general critical homogeneous Siu-division proof, and LPWZ density remains unverified.

## Evidence and publication status

The frozen reading ledgers record each source hash, physical page selection, matching image/text hash and sequential note. The appended notes preserve historical conditional objections with the controlling qualifications above. No frozen note or earlier DONE checkpoint is rewritten. This source checkpoint has not yet been integrated into the manuscript and has not been pushed to GitHub. The separate earlier local cloud commit is not evidence of remote publication.
