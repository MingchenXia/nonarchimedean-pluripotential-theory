# Reference data, exact residual scope, and execution evidence

This note uses local **n1**, **n2**, and **n3**. It gives a bounded-family characterization of the necessary reference scale, explicit examples, and the remaining scope of P15.1. It does not claim original closure.

## A proved characterization of scale equivalence on the bounded domain

Fix the actual bounded singularity type \(\tau=[\psi]\), and its degree \(d\); let \(r=n-d\). Put \(V=H^{1,1}(X,\mathbb R)\). For \(u,v\in\mathcal C_\psi\), define a symmetric multilinear functional on \(r\) Kähler classes by
\[
L_{u,v}(\lambda_1,\ldots,\lambda_r)
=\frac1{d+1}\sum_{a=0}^d\int(u-v)
\langle T_u^aT_v^{d-a}\rangle\omega_1\cdots\omega_r,
\quad\omega_i\in\lambda_i.
\tag{26a}
\]
It is independent of each representative: changing one factor inserts \(dd^cg\), the other \(r-1\) factors are closed positive, and the admissible IBP and degree-\(d+1\) vanishing argument (11) applies verbatim. Extending factors as differences of Kähler forms gives a well-defined symmetric multilinear functional on all of \(V^r\). To justify well-definedness of this extension explicitly, represent a real class \(a\) by a smooth closed real form \(\eta\). Both \(\eta+C\Omega\) and \(C\Omega\) are Kähler for sufficiently large \(C\). The defining integral is multilinear in smooth factors; any two decompositions have the same difference form up to \(dd^c\) of a smooth function. Representative invariance for positive factors, then expansion by differences in all remaining factors, makes that change zero. Thus there is a linear functional \(\ell_{u,v}\) on \(\operatorname{Sym}^rV\) with value (26a). Constants in the potential are included among \(u,v\).

Set
\[
K_\tau=\bigcap_{u,v\in\mathcal C_\psi}\ker\ell_{u,v}.
\tag{27a}
\]
Then the bounded energy family needs only the image of the formal tensor \(\lambda^{\odot r}\) in the finite-dimensional quotient \(\operatorname{Sym}^rV/K_\tau\). Conversely two formal tensors give the same values for **every** bounded relative energy exactly when their difference belongs to \(K_\tau\), by definition of the intersection of kernels. This is a proved coarsest scale-equivalence characterization for this fixed bounded family, not a declaration that the entire auxiliary class is always minimal. Changing the anchor within \(\tau\) does not change \(K_\tau\), since all relative differences remain in the same family. The degree-zero case uses the same formula with the empty current product and \(r=n\).

The characterization does not construct a geometric lower-dimensional carrier, nor a universal minimal scale for all singularity types or all unbounded domains. For the finite-energy extension n2, a fixed Kähler class is sufficient and its representatives are unnecessary, but no minimal quotient characterization across arbitrary classes is claimed.

## Why a scale and actual type cannot be discarded

On \(X=\mathbb P^1\times\mathbb P^1\), with normalized \(\kappa\), let \(\alpha=[p_1^*\kappa]\), \(\theta=p_1^*\kappa\), and \(\psi=0\). It is a nef zero-volume class by the nef cup-product statement. For \(\omega=A p_1^*\kappa+B p_2^*\kappa\), \(A,B>0\), one has \(d=1\), \(M_1=B\), and \(\mathcal E_{0,[\omega]}(c)=cB\). Varying \(B\) changes the raw energy of the same constant potential. Some scale is therefore necessary. Varying \(A\) alone does not change these energies; it illustrates why the entire Kähler class should not simply be declared minimal. Indeed all bounded \(\theta\)-psh potentials descend to the first factor: their restriction to each second-factor fiber is a psh function on a compact curve and is constant, and bounded potentials are finite on every fiber. Equivalently the constant-shift example alone already proves necessity of \(B\), without any descent theorem.

Actual reference singularity data also affect the degree. On the first \(\mathbb P^1\), let
\(g(z)=\log(|z|^2/(1+|z|^2))\), in the chart whose distinguished point is zero. In the chosen convention \(\kappa+dd^cg=\delta_0\): the elementary Poincaré–Lelong identity \(dd^c\log|z|^2=\delta_0\) follows by the distributional boundary flux around a disk, and \(dd^c\log(1+|z|^2)=\kappa\). Thus the actual reference \(\psi=p_1^*g\) represents the positive integration current of the vertical divisor. Its degree-one nonpluripolar current is zero, since it is supported entirely on its polar divisor; all higher products vanish as well. This reference has \(d=0\) in the same class whose smooth reference has \(d=1\). The numerical dimension of this nef class is 1 by its nonzero first cup product and zero square, but the actual prescribed reference can have degree zero. Hence the degree in n1 is not identified with the class numerical dimension.

In this same example the actual perturbation mass is \(P_\varepsilon=2AB\varepsilon^2\), whereas the class is nef and its perturbation volume is the cup product \(\operatorname{vol}(\alpha+\varepsilon[\omega])=2B\varepsilon+2AB\varepsilon^2\). The first nonzero class-volume coefficient therefore has a different exponent from the actual-reference mass. An actual anchor constant shift has relative perturbed energy \(cP_\varepsilon\); rescaling by the class-volume leading exponent would make its limit zero. This is an explicit reason not to substitute a class-volume coefficient for the actual prescribed-type scale without proving an additional theorem.

The actual carrier throughout is \(X\), of complex dimension \(n\); the integrals use a degree-\(d\) nonpluripolar current and complementary smooth factors. The full auxiliary form would remain data for its differential measure. The energy itself only uses the class, or the precise quotient (27a) within the bounded family. An actual anchor fixes the additive origin of energy; changing it has the stated cocycle. Gauge changes of the smooth background and potentials leave every current unchanged.

## What remains open for the original P15.1

The bounded theorem removes the supplied-fibration hypothesis completely: its ambient class and actual reference are arbitrary as in the question. The finite-energy extension is a genuine more-singular domain, not just bounded differences under another name. Nevertheless these are scoped partial results; they are not counted as original catalogue closure.

The unbounded extension of the class-convergent auxiliary-path prescription is **false** without further conditions, by the analytic counterexample n3. Even within the finite-energy domain, lower weighted perturbation coefficients can lack uniform control along fixed-class smooth representatives. For general references and fixed auxiliary forms, integrability and uniform control of all lower-degree weighted terms, and relative limits for genuinely unbounded moving potentials, have not been proved here. Nor have continuity for arbitrary increasing sequences, differentiation with unbounded velocities, or all proposed path classes been established. Decreasing continuity, cocycles, fixed-class representative invariance, and concavity in n2 are the precise asserted extension properties.

There is no numerical-dimension theorem, no general leading **class-volume** coefficient theorem, no complete universal minimum-reference construction for unbounded types, and no intrinsic geometric \(d\)-dimensional carrier. The degree and perturbation exponent use actual-current masses rather than an assumed equality with class volume. No fibration, ideal-equivalence-only recovery, zero-mass probability normalization, nonarchimedean translation, or independent worker verdict is used. P15.2 and P15.3 are outside this assignment. The original P15.1 remains open in the dossier's residual scope.

## Audit and rerun contract

The original `input.json` is retained byte-for-byte, with SHA256 `5950ca2b12dc2202093de059446f0076db58a9cc861e1e57ce8c82edc371753b`. Its decoded assignment string is also retained as `assignment-original.txt`; `task-original.json` preserves the task values. The authoritative deliverable is `P15.1-argument.md`, containing all four mathematical notes and the complete immutable source bodies. `P15.1-partial.tex` and its twice-compiled `P15.1-partial.pdf` contain the entire new proof, standard foundation statements and applicability checks. Literal source bodies remain in the Markdown annex to preserve their UTF-8 extraction and defects.

The independent source audit reads only `/workspace/research/shared-sources`. All 14 supplied LF-range SHA256 pins match exactly when a range is joined by literal LF without appending an extra final LF. The audit additionally records three directly read foundation ranges. All source files are read-only and unchanged. Source text retains form feeds, the printed missing \(1/2\), the v1 Proposition 4.2 \(m/n\) and subscript defects, and the malformed extracted convention. The correct intrinsic formula and all new calculations are separate from these raw quotations. The page-4/page-6 Vu v3 images and page-4 Vu v1 convention image were inspected locally. Vu v1's finite-energy theorem is not the controlling finite-energy source. No source-dependent catalogue claim was treated as independently established by the catalogue description.

The requested execution identity was native Codex `gpt-6.1-sol`, reasoning `xhigh`. This turn used the native available Codex runtime only; no additional model or subagent was invoked. The runtime does not expose a signed model/effort attestation here, so those exact backend identifiers are recorded as requested rather than independently verified. No network call, install, external message, auth/proxy/CA change, HOME/CODEX_HOME change, SQL/runtime edit, or old-artifact write was performed. All new files are in this assigned workspace. There was no resource-heavy computation and no need to invoke a supervised compute service.

Rerun commands from this directory are:

- `python verify_sources.py`
- `python coefficient_check.py`
- `python build.py`

Observed checks report 14/14 matching supplied source pins, 968 passing exact finite Vandermonde coefficient cases, and two successful `pdflatex` passes followed by successful PDF text-extraction checks. The initial compilation encountered an authored inline-math delimiter error; `repair_math_markup.py` corrected the delimiters without changing mathematical content, and `pdflatex-initial-failed.log` preserves that diagnostic. The final document was then compiled successfully twice. The build records environment versions, commands, return codes, source hashes, twice-compiled PDF evidence, and diagnostic output in local JSON/log artifacts. Coefficient checks are exact finite arithmetic diagnostics, not analytic proofs. PDF compilation and artifact validation are observations, not mathematical correctness certification. `status.json` has exactly the five requested keys and records `status: partial`. `notes.json` is the canonical native note object with `candidate: false`; its support arrays contain only earlier local IDs. No literature-priority claim or external independent correctness verdict is made.
