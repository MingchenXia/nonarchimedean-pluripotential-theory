# Source and dependency matrix

## CLD ambient framework

The checked text source is

`manuscript/editorial/rethlas_packets_20260829/p213_trivially_valued_curve_candidate_audit_20260829/sources/CLD25.txt`,

SHA-256
`24920a1f4c8bd4944c83d89c8747c95b0206ae0754053eb0ed4d3de95e0f7727`.

| Input | Exact locator | Exact use and retained scope |
|---|---|---|
| Currents are a sheaf | CLD Proposition 7.1.7, text lines 7744--7755 | Local current identities glue. The source assumes local differential separation; no paracompactness is needed for the sheaf assertion. |
| Positive currents form a subsheaf | CLD Lemma 7.2.4, lines 7922--7942 | Positivity survives restriction. |
| Positive current has order zero | CLD Proposition 7.2.9, lines 8003--8029 | Justifies extension to continuous test coefficients in the locally differentially separated setting. |
| Continuous multiplication | CLD Example 7.2.12, lines 8050--8064 | Defines `uT` for every locally bounded Borel, hence continuous real, function `u`; the operation is linear and preserves bidegree. |
| Positivity and closedness conventions | CLD Section 8.5.2, lines 10273--10275 | A positive current is symmetric; the candidate conservatively writes both `d'T=0` and `d''T=0`. |
| Smooth-current Leibniz formula | CLD Lemma 8.5.3 and Section 8.5.4, lines 10277--10301 | For smooth `h` and positive closed `T`, `d'd''(hT)=d'd''h wedge T`. Section 8.5 is printed under the boundaryless standing scope at lines 10243--10249. |
| Every-open Bedford--Taylor predicate | CLD Definition 8.6.2, lines 10345--10347 | Confirms that full Bedford--Taylor independence quantifies over every open subset. |
| Locality of the full predicate | CLD Proposition 8.6.3, lines 10354--10360 | Gluing is legal only after every restriction already has the every-open predicate; it cannot turn a fixed-domain identity into that predicate. |
| Analytic local differential separation | CLD Section 15.2.2 and Corollary 15.2.4, lines 21551--21565 and 21581--21583 | Topologically separated plus good gives local holomorphic, hence local differential, separation. |
| Analytic space as tropical space | CLD Theorem 15.7.1, lines 22033--22050 | A topologically separated pure analytic space carries the CLD tropical structure with its analytic boundary. The candidate retains boundarylessness for the source-literal Section 8.5 framework. |

The live book records the same umbrella in
`manuscript/parts/part2/ch16_bedford_taylor.tex:109--136`, continuous
multiplication at lines 996--1013, the smooth Leibniz formula at lines
1142--1213, and the every-open continuous Bedford--Taylor predicate at lines
1339--1354.

For the order-zero multiplier and current-sheaf argument, the intrinsic
minimum is local differential separation. The proof of the smooth Leibniz
identity is formal once the current calculus exists, but CLD print it inside
the boundaryless Section 8.5 scope. The candidate therefore keeps the clean
source-literal analytic umbrella
`topologically separated + pure-dimensional + boundaryless`. Goodness is
redundant under that umbrella in CLD, but is
retained to match the active analytic scope. Strictness is not part of the
current calculus and enters only through the strict-polycylinder dependency.

## P06.2 dependency

| object | SHA-256 | Exact use |
|---|---|---|
| `p062_product_slicing_polycylinder_v3_strict_open_statement_20260830.tex` | `985be85d97b583f72be5cee65988df6f31c1edb49a685121b834df179fa87fda` | On a standard strict open polycylinder over a complete nontrivially valued field, a continuous zero-current function is `c + sum lambda_j log|S_j|`. |
| `p062_product_slicing_polycylinder_v3_strict_open_proof_20260830.tex` | `42b592bf8ac26ed46c36928e5e90272225ae6883bd2bfe62d3ff2840f01d46e5` | Lines 394--396 explicitly identify the displayed function as ordinary CLD-smooth with zero Hessian. |
| v3 production `response.json` | `c8c951075a574c6a3badde2e2a22942718616cd21da0144cb8a983bc3cac822f` | Dependency verdict `correct`, with no reported critical errors or gaps. This receipt does not verify the present v2 candidate. |

P06.2 is used only on strict open standard discs and annuli, with all radii
in the value group. No endpoint, closed-domain, half-closed-domain, or
non-strict inference is made.
