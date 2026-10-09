## 1. Full semivaluations under completion

Let $(R,\mathfrak m)$ be a Noetherian local ring, $\widehat R$ its $\mathfrak m$-adic completion, and $\mathfrak a$ a proper $\mathfrak m$-primary ideal. Semivaluations have values in $[0,\infty]$, are nonnegative on the ring, and have $0<v(\mathfrak m)<\infty$. No restriction on their prime support is made. Write $X_R=\{v:v(\mathfrak a)=1\}$. Choose $r$ with $\mathfrak m^r\subset\mathfrak a$; then $d=v(\mathfrak m)\ge 1/r$ on $X_R$.

For $v$ set $|f|_v=\exp(-v(f))$, with $\exp(-\infty)=0$. This is a multiplicative nonarchimedean seminorm with values in $[0,1]$. If $F\in\widehat R$, choose compatible representatives $f_N\in R$ modulo $\widehat{\mathfrak m}^N$. For $M\ge N$ their difference belongs to $\mathfrak m^N$: this uses the standard exact completion quotient $R/\mathfrak m^N\simeq\widehat R/\widehat{\mathfrak m}^N$. Thus
\[
 |f_M-f_N|_v\le e^{-Nd},\qquad
 \big||f_M|_v-|f_N|_v\big|\le e^{-Nd}.
\]
The second assertion follows directly from the ultrametric inequality: if the two norms differ, their larger value is at most the norm of their difference. Define $|F|_{\widehat v}=\lim_N|f_N|_v$. The limit is independent of representatives, and
\[
 \big||F|_{\widehat v}-|f_N|_v\big|\le e^{-Nd}\le e^{-N/r}. \tag{1}
\]
Representatives for $F+G$ and $FG$ can be chosen as sums and products of representatives. Taking real limits proves the ultrametric inequality and multiplicativity; $|0|=0$ and $|1|=1$. Define $\widehat v(F)=-\log|F|_{\widehat v}$, retaining the value infinity when the norm is zero. In particular this constructs, rather than removes, all infinite values and all nonzero supports. Units of $\widehat R$ have unit representatives and value zero. The same finite generators of $\mathfrak m$ show $\widehat v(\widehat{\mathfrak m})=d$, and similarly $\widehat v(\mathfrak a\widehat R)=1$.

Conversely every normalized centred semivaluation on $\widehat R$ satisfies (1), since $F-f_N\in\widehat{\mathfrak m}^N$. Its restriction has the same primary normalization and uniquely determines it. Restriction is therefore a bijection. Each completed norm evaluation is a uniform limit, on $X_R$, of continuous jet norm evaluations by (1). The map $t\mapsto e^{-t}$ identifies the compact extended interval $[0,\infty]$ with $[0,1]$. Hence every completed valuation evaluation is continuous in the extended-value topology. Both restriction and extension are continuous in the pointwise topologies, proving
\[
 E:X_R\overset\sim\longrightarrow X_{\widehat R} \tag{2}
\]
is a homeomorphism. No separability, normality, excellence, coefficient field, or metric on the link has entered this proof. Empty links cause no exception.

## 2. Exact primary descent and the geometric comparison gate

Every $\widehat{\mathfrak m}$-primary ideal $J$ contains $\widehat{\mathfrak m}^N$ for some $N$. Choose finite generators $F_1,\ldots,F_s$ and jets $f_i\in R$ modulo that power. Since $F_i-f_i\in J$, each $f_i$ belongs to $I=J\cap R$. Together with $\mathfrak m^N$, these elements generate an ideal $I'$ of $R$ satisfying $I'\widehat R=J$. Faithful flatness of completion gives $I'\widehat R\cap R=I'$, so $I'=I$. Thus $J=I\widehat R$. Conversely a primary ideal of $R$ extends to a primary ideal, as its finite-length quotient completes to itself, and contracts exactly. Units correspond too. The proof uses only primary ideals, and makes no assertion of descent for arbitrary ideals.

For every such ideal, $\widehat v(I\widehat R)=v(I)$, because its finite generators are in $R$ and all coefficients upstairs have nonnegative value. Consequently (2) identifies, exactly, every unit-or-primary profile, every finite nonnegative real combination of negative profiles, and their finite continuous uniform closures.

Now assume $R$ is excellent. Reduction commutes with completion: the completed reduction is reduced by the geometrically regular formal-fibre property, and the extended nilradical is nilpotent. Complete Noetherian local rings are excellent; completion of an excellent normal local ring is normal, using its normal formal fibres. These are ordinary completion/excellence facts at precisely these hypotheses, not conclusions about arbitrary nonexcellent rings. Alternatively restrict throughout to an excellent reduced $R$ whose completion is excellent reduced; the elementary conclusions of Sections 1–2 do not need these permanence facts.

The full G331 theorem applies separately to $R_{\mathrm{red}}$ and $\widehat R_{\mathrm{red}}$. On each it defines actual negative effective real Cartier presentations on actual primary blowups, tests their degrees on every contracted integral proper curve, and proves
\[
 C_{\mathrm{geom}}=\overline{Q_{\mathrm{primary}}}^{\|\cdot\|_\infty},
 \qquad D_{\mathrm{geom}}=\{\inf_i h_i:h_i\in C_{\mathrm{geom}},\ h_i\downarrow\}.
\]
The preceding exact profile transport therefore proves
\[
 E^*C_{\mathrm{geom},\widehat R}=C_{\mathrm{geom},R},\qquad
 E^*D_{\mathrm{geom},\widehat R}=D_{\mathrm{geom},R}. \tag{3}
\]
For the second equality transport the actual directed set and every term of each decreasing representation in both directions. There is no nested-net flattening, arbitrary infimum closure, or increasing completion step. Equation (3) is geometric positivity transport because of the independent G331 comparison on both rings. The topological primary statement alone would not prove it.

This proves equality of the completed geometric cones. It does not assert that their raw Cartier cores, their Cartier divisor groups, or their whole model categories are equivalent. No completed exceptional Cartier divisor has been assumed to descend. For context only, $\operatorname{Bl}_I(R)\times_R\widehat R=\operatorname{Bl}_{I\widehat R}(\widehat R)$ follows from flatness and the raw Rees algebra. Its full closed fibre is unchanged. Pulling back actual effective Cartier presentations preserves regular equations and their fibre-curve degrees. This supplies a direct core inclusion, but the reverse completed-cone equality in (3) comes from the proved comparison. Normality of arbitrary base-changed normal models and cofinal resolution are not needed by this route.

## 3. Envelopes, gauges, Jensen measures, and conductor after completion

For any function $f$ on $X_R$, including signed continuous, upper semicontinuous, and extended obstacles, form the raw supremum over $D$ minorants, with the empty-supremum convention $-\infty$. Transport of (3) gives the pointwise equality
\[
 E^*p_{\widehat R}(f\circ E^{-1})=p_R(f). \tag{4}
\]
The same equality holds for raw $C$ suprema. Homeomorphisms preserve both semicontinuous regularizations, continuity, and the existence of a greatest or maximal geometric minorant. Thus (4) transfers their existence and properties, and does not assume these properties universally exist. In particular the continuous-envelope property CE is equivalent for $R$ and $\widehat R$.

All primary gauges descend by Section 2. For a second primary ideal $\mathfrak b$, the common ray formula is $v\mapsto v/v(\mathfrak b)$ and $u_{\mathfrak b}(v/v(\mathfrak b))=u_{\mathfrak a}(v)/v(\mathfrak b)$. The denominator is finite positive continuous with a bounded inverse. Completion preserves it exactly, so (2)–(4) commute with this cocycle.

Normalization/conductor also commute at the level needed here. Let $R$ be excellent reduced and $S$ its finite normalization, with local centres $q$ over $\mathfrak m$. There is a regular conductor element $c$; $S_c=R_c$. The finite algebra $S\otimes_R\widehat R$ is the product of the completed $S_q$: the $\mathfrak mS$-adic and the Jacobson-radical-adic topologies are equivalent in a finite semilocal algebra, and the completed Artinian decompositions give this product. Each $S_q$ is excellent normal, so each completion is normal. Flatness keeps $c$ regular, and after inverting it the product algebra agrees with $\widehat R_c$. It is consequently finite, normal, and birational over the reduced $\widehat R$, and is its normalization. This proves the assertion without a smooth-model base change claim.

The conductor is $\operatorname{Ann}_R(S/R)$. Annihilators of a finite module commute with this flat base change: choose finitely many generators, express the annihilator as the kernel of the map $R\to M^{\oplus s}$, $a\mapsto(am_1,\ldots,am_s)$, and use exact flat tensoring. Therefore $\widehat{\mathfrak c}=\mathfrak c\widehat R$. The semilocal version of Section 1 identifies the normalization links and commutes with restriction. The finite-value conductor singleton stratum and the infinity-value quotient-fibre stratum are preserved, including their full nonminimal supports. G331's full-fibre-constant $C,D$ descent then agrees across completion. No conductor value has been divided to obtain a uniform error.

If $J_x(C)$ denotes the subprobability Jensen set, pushforward by $E$ gives exactly $J_{E(x)}(C_{\widehat R})$. Both the mass condition and every Jensen inequality transport through (3). Pushforward is a homeomorphism in the weak topology because continuous tests transport through a homeomorphism. Closed graph, upper and lower hemicontinuity, and the exact dual formula all transfer. This reduces the arbitrary excellent completion problem to the corresponding complete ring; it does not turn a complete ring into an algebraic germ of finite type over a field.

Artifacts: P12.3-completion-and-formal-lifting.tex, whole-proof.md, completion-proof.md, independent-review.md, source-application-ledger.md, coverage.md, original-residual.md, scope-and-decision.json, native-notes.json and reports. Rerun from this directory: python retain_and_identify.py; python audit_delivery.py; python finite_checks.py; python assemble_delivery.py; python final_audit.py. No supplied program is executed or imported. Source uncompiled; ROOT retains compiler/acceptance/publication. Execution and hashes do not certify the mathematics.
