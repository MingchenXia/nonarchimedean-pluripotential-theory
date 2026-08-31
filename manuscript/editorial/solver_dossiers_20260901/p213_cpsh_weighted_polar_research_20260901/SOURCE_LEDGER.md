# Source and dependency ledger

Date: 1 September 2026. Author: /root/p213_skeletal_hostile.
This ledger accompanies a NEW authored proof. It is not an independent verification, a published-source attribution of the new result, or a production acceptance.

## 1. Exact primary source

Antoine Chambert-Loir and Antoine Ducros, *Formes différentielles réelles et courants sur les espaces de Berkovich*, arXiv:1204.6277v2, version dated 25 July 2025.

Official version page: https://arxiv.org/abs/1204.6277v2 .
The official version page was inspected for identity. The mathematical source review used the complete relevant spans of the local plain-text extraction below. The PDF is an exact provenance pin, not a claim of visual PDF inspection in this task.

- /private/tmp/CLD25.txt, 2150944 bytes, SHA256 021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e.
- /private/tmp/CLD25.pdf, 4659053 bytes, SHA256 5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719.

Printed page numbers below are those in this source, not PDF-viewer page offsets. Local line numbers refer to the pinned text.

## 2. Input interfaces and what is newly proved

| Source | Printed pages / local lines | Exact use and boundary |
|---|---|---|
| 6.5.2; 7.2.1–7.2.12 | 148, 160–163 / 7353ff, 7912–8069 | Compact symmetric test decomposition, local positivity, positive top currents as Radon measures, order zero, and continuous coefficient multiplication. These use local differential separation; it is now an explicit abstract hypothesis. Arbitrary top-degree distributions are NOT declared Radon measures. |
| 8.1.7–8.1.8 | 196–197 / 9791ff | CPsh is the least continuous subsheaf containing smooth psh functions and stable under uniform limits. Separate-variable subsheaf closure, not a single smoothing sequence, is used in Sections 2–4. |
| 8.1.9–8.1.13 | 197–198 / 9820ff | Distinction between the first locally approchable stage and the full sheaf. This packet neither proves nor uses an identification of all continuous current-positive functions with CPsh. |
| 8.2.4 | 200 / 9960ff | The source has convex increasing composition, but its proof invokes 8.1.11. The present proof instead derives the needed smooth convex composition directly from CPsh minimality. Squares are taken only after positive shifts and via a globally convex increasing smooth extension. |
| 8.5.1 | 205–206 / 10249–10282 | Positive weakly convergent currents times locally uniformly converging continuous functions converge. Every signed term used in energy continuity is split into finitely many positive terms of this kind. No weighted estimate is used to establish that continuity. |
| 8.5.2–8.5.5 | 206–207 / 10284–10329 | Separately closed symmetric current calculus; dd(uS) is positive for full CPsh u and positive closed S. The source itself proves this by the least-subsheaf argument. |
| 8.7.2 and 8.7.4 | 209–210 / 10410ff | Existence, uniform continuity and symmetry of iterated products. Here S is a fixed positive closed current at each inductive energy step. No unproved dependence only on ambient curvature is imported. |
| 8.8.1, 8.8.4–8.8.5 | 211–212 / 10489–10560 | Every smooth function is locally dpsh; multilinear extension to dpsh produces differences of positive currents. Section 2 explicitly proves the square/product decompositions and finite-variation continuity needed here. |
| 8.4.2–8.4.3 | 203–205 / 10100–10245 | Template for the barrier forms and smooth weighted argument only. The present full-CPsh estimate is NOT cited from 8.4.3. It is reproved through new energy identities, with endpoint and boundary corrections in Section 3 of this ledger. |
| 8.12.1–8.12.3 | 223–224 / 11165–11223 | The published polar statements require locally approchable potentials. Their order of fixed-weight and subsequent monotone limits and the positive trace domination motivate Section 7. The removal of the locally-approchable restriction on the continuous factors is new work in this packet. |
| 11.1 standing convention; 11.8.1 | 297, 322 / 14835ff, 16147ff | Complete K may be trivially valued; strictness follows the CLD convention. The usual strict class is sufficient. No scalar extension or nontrivial value-group assumption is introduced. |
| 15.2.1(b), 15.2.4–15.2.5 | 423–424 / 21544ff | Top-form support avoids lower-dimensional analytic subsets. Good separated analytic spaces are locally differentially separated, with compact smooth cutoffs. These give canonical integrability of the log pole and the analytic realization of the abstract calculus. |
| 16.9.1–16.9.4 | 466–467 / 23720–23793 | Source analytic barrier and prime-avoidance strategy, but not a source statement of the new general-CPsh conclusion. Section 8 gives an actual smaller compact sublevel, includes the constant regularized-max branch, and explicitly smooths the one log pole. |

The MAIN NEW portions are: the full-dpsh energy and its controlled continuity; the separate-closure positivity and exponential identities; the measure-level mixed Schwarz inequality; the nonsmooth weighted induction with C2 compact tests and the corrected endpoint; and its application to the full continuous CPsh factors. Elementary Radon–Nikodym and monotone-convergence arguments are spelled out in the proof.

## 3. Source discrepancies deliberately corrected, not silently imported

### 3.1. Top endpoint k=n

In 8.4.2 the source defines beta_k with two summands but expressly omits the second when k=n. It then prints d''beta_k=-2(k+a)r^(k+a-1)d''rho theta^(n-k) and the matching factor-two dd formula without excluding k=n. At k=n, beta_n=r^(n+a) is a scalar. Its first and second derivatives have factor ONE, not two. These derivatives are within the permitted degree and do not vanish by a dimension argument.

The present proof uses b_k=2 for k<n and b_n=1, computes both cases, and obtains the cross coefficient 2b_k l and the Young coefficient b_k^2 l^2. The bracket coefficients are b_k l and b_k l((b_k-1)l+1). The same deliberately loose upper bound c_k=2l(l+1)/(l-1) dominates both cases. Thus the convenient final constant is retained without relying on the false endpoint identity. Root identified this error during prefreeze review; the author corrected and rechecked it.

### 3.2. Finite regularity and the polar weight at the boundary

The proof fixes an integer a>=4, so every scalar power used in beta_0 through beta_n is genuinely C2 across rho=0. It does not copy the source's broad finite-regularity shorthand for integer powers.

V is required to be smooth psh on a neighbourhood of K_delta, not merely smooth on U={rho<0}. This is needed for (-V)beta_k to be a compact C2 test. The smooth polar truncations are defined on a common larger open, so this stronger hypothesis suffices for the local conclusion. The scalar bound u>=-||u||_U is used only on U, and beta_k has zero coefficients everywhere outside U, including its boundary.

### 3.3. Actual compact sublevel

The literal 16.9.1 statement says rho<0 on its domain and also describes its nonpositive set as compact. The needed construction is instead a function on an ambient ordinary open with a smaller negative sublevel compactly contained there. Section 8 proves exactly that. It adds a constant branch to the regularized maximum so that simultaneous zeros of the f_i cause no undefined smoothness claim.

### 3.4. A single pole, not collapse of approximation stages

The source 16.9.4 proof passes through continuous max truncations. Here the required local smooth decreasing approximation for log|f| is directly F_p(log|f|), with F_p(t)=-p+F(t+p), F a smoothed positive part and 0<=F'<=1. This is constant near every zero, and its monotonicity in p is explicit. No inference that an iterated limit is first-stage approchable is needed.

## 4. Frozen context input and optional component consequence

The independent SOURCE audit completed BEFORE this authored proof is preserved in the sibling directory p213_polar_nullity_source_audit_20260901. Its pinned report is:

SOURCE_AUDIT.md SHA256 4b5818d69ee5fa319d15d42dfdef61b839bc32f78ad689f3714266d524ec7e97;
MANIFEST.json SHA256 3c9fd6ee4f2f2b9f20dce750758747d9fe3437ec6a693b64f50164fa158fdd43;
SHA256SUMS SHA256 2687d8b7cb8dbfaae09f981c9f6d9d9b4f9cbac171c69013a1805f58bdd5bef1.

It establishes the literal source scope and records the elementary positive-weighted-sum implication under an explicit common-curvature nullity hypothesis. It does NOT independently certify the proof subsequently authored here. Section 9 of the research note is only an optional deduction from that common-nullity lemma if the new proof is independently accepted. No component classification theorem, normalization result, scalar R representation, or global P21.3 conclusion is an input of Sections 1–8.

## 5. Provenance and review boundary

Parent /root requested a full general-CPsh proof through the energy route, discussed the square decomposition and rational-parameter Schwarz argument, and supplied boundary cautions and the substantive top-endpoint correction. The author /root/p213_skeletal_hostile wrote and internally checked the complete candidate. Root's consultation cannot serve as its sole fresh independent review.

All frozen predecessors and all live chapters remain unchanged. No git action, production service, Rethlas submission, PDF compilation or visual PDF audit was performed by this task. A search of the callable tool metadata at finalization returned no Rethlas tool. The prior requested model/effort label was sol/xhigh, but this agent cannot independently attest runtime identity or effort from the exposed execution metadata; no such verification is claimed.

The exact files, source pins and hash checks are in INPUT_PINS.json, MANIFEST.json, SHA256SUMS and check_packet.mjs. Hash checks prove byte identity and assembly only; they are not mathematical verification.

