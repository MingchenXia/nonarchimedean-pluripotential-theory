# Ch25 revised1 exact-byte addendum

31 August 2026. Auditor: p213_skeletal_hostile. This addendum supplements, and does not overwrite, the initial independent audit in the parent directory.

## Verdict and independence boundary

The revised1 text corrects the fixed-reference quantifier gap and both terminology/convention issues recorded in the initial audit. The four exact changes introduce no further gap found on the stated BFJ curve scope and conditional upstream inputs. The independently reviewed capacity core is mathematically unchanged.

The fixed-pair construction was suggested and mathematically derived by this auditor during the parent audit. Root authored its final proof and exact assembly. Consequently the present recheck is an exact-byte, proof, and integration-scope check of that new example, **not a fresh independent audit of the mathematical idea**. Separate verification must retain this provenance. By contrast, the parent core was not authored by this auditor and its independent review remains genuine, subject to the explicit exclusion below.

The auditor authored the Ch26 weighted graph-energy baseline. Its graph-to-BFJ sufficiency implication remains a conditional input, not independently certified by this auditor. The separate Ch20/21 actual-real-model maximum and dependent BFJ foundations remain gated. The unchanged later Thuillier-relative subsection is outside this audit. This is not production verification, authorization to integrate, or an unconditional certification of the full chapter.

## Frozen exact targets

All paths below are under
/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260831/.

- Author revised1 directory: `p081_ch25_weighted_capacity_repair_20260831/revised1/`.
- Revised full chapter: 202111 bytes; SHA256 `4f66e1358ede7c8d9afff6b8b3c0fbaf53a27247d9741ce02f890fe24a0959a7`.
- Fixed-reference fragment: 2433 bytes; SHA256 `e5b8c7817ca8eb0ffd56f686f9efc36ae47c44edd2c95ebaa84071b005add9fa`.
- Revised cumulative chapter.patch: 43202 bytes; SHA256 `13896454d1a95be9755e4fbd4faab946418783391fef3e6881a202eb5456525f`.
- Author revised1 manifest: 2125 bytes; SHA256 `c1aa7dad837b6a06e0470c1442a7b9966dff398816f9b6cc378f09e0bff32287`.
- Preserved original proposed full chapter: 200063 bytes; SHA256 `bc939ba01e4763debb7d73b4d6681592ea70229a7c42814c8c59384b3b4cb1ce`.
- Preserved original core: 17122 bytes; SHA256 `de250281d1e66be5b69dd31b16e7a30cdbafd4ad6b0b374e5bb8389316de196b`.
- Preserved initial independent-audit manifest: 8667 bytes; SHA256 `777525a225db6e78e2eda53257913a7e50b89c17744336c11c8ec473a3d21d90`.

The revised1 GATE.md, assembly script, manifest, entire fixed-reference fragment, and complete parent-to-revision diff were read. The script was inspected as text and **not executed**, since it writes the author packet. Independent checks were read-only.

## Four changes, with exact scope

1. Revised full chapter lines 754–759: the early nonuniformity remark now points to the new fixed-pair example. It no longer infers a fixed-reference assertion by varying the resistance length while retaining endpoint masses on a varying model/reference.
2. Revised full chapter line 3194: the degree-two-node title says “non-rational,” not “nonsplit.” Its mathematical body, label, and weighted computation are unchanged. A residue-degree-two node need not have branches nonsplit over its own residue field.
3. Revised full chapter lines 3613–3615: the text distinguishes equality with total mass from equality between singleton and retracting-tube capacities. The latter is not a short-edge phenomenon; it follows from the exact graph competitor/retraction comparison in the reviewed scope.
4. Revised full chapter lines 3663–3720: the invalid fixed-reference inference is removed, the valid symmetric-segment calculation and proper-closed-full-capacity example are retained, and the new explicit fixed-reference example is inserted. The added fragment is byte-for-byte the frozen fixed_reference_example.tex.

The parent-to-revision diff has exactly four hunks:
`@@ -751,12 +751,11 @@`,
`@@ -3192,7 +3191,7 @@`,
`@@ -3611,8 +3610,9 @@`, and
`@@ -3660,23 +3660,66 @@`.
No other mathematical alteration appears.

## Recheck of the fixed-reference proof

The example stays in the original chapter's BFJ setting: a complete discretely valued field, with normalized valuation \(v(\pi)=1\), and the standard \(R\)-model of \(\mathbf P^1_K\). It does not assert a reduction of arbitrary complete valued fields to this setting. The use of \(\mathbf P^1\) as a counterexample to a proposed uniform bound does not narrow the general capacity theorem.

### Models and normalizations

In fragment lines 10–19 the centers are smooth points of the special fibre, not nodes. On the chart following the section, after the \(j\)-th blowup one has a coordinate \(T_j=T/\pi^j\). The next center is \(T_j=0\) on the newest component. The previous node is a different point, so the next blowup extends the chain rather than subdividing an existing edge. Every center is residue-rational, every component has multiplicity one, and consecutive components meet in one residue-rational ordinary node with local equation \(xy=\pi\). Hence every conductance and modulus length equals one. The resulting skeleton is \([0,N]\), and the endpoint valuation satisfies \(v_N(T)=N\).

This construction is therefore legitimate for every integer \(N\geq1\). It does not invoke the false assertion that reduced semistable models are cofinal over the original field. The constructed models themselves are regular reduced semistable models. Smooth-point blowups here intentionally change the selected skeleton; this does not conflict with the node-only subdivisions used to preserve a fixed graph in the capacity core.

### Fixed form and an actual rational model competitor

The form is always the class determined by the standard model bundle \(\mathcal O_{\mathbf P^1_R}(2)\), pulled back to the chosen model. Its degree on the strict transform of the original component is two; its degree on each contracted exceptional component is zero. Thus its associated measure is the same \(2\delta_g\) on every chosen model. Neither the analytic curve, the form, nor the normalized competitor set varies with \(N\).

Let \(E_0,\ldots,E_N\) denote the components ordered along the chain. The rational vertical divisor
\[
 D_N=-\sum_{j=0}^{N}(j/N)E_j
\]
is a rational Cartier divisor because the model is regular and \(N D_N\) is integral Cartier. Its model potential has the values \(-j/N\) and equals \(f_N\circ p_N\), with \(f_N(s)=-s/N\). This is an actual rational model function, not merely a real PL or continuous limit competitor.

For the unit-weight chain the diagonal intersection entries are \(-1\) at the endpoints and \(-2\) at interior vertices; each adjacent off-diagonal entry is one. Direct multiplication gives
\[
 (D_N\cdot E_0,D_N\cdot E_1,\ldots,D_N\cdot E_N)
   =(-1/N,0,\ldots,0,1/N).
\]
For \(N=1\) this means just the two entries \((-1,1)\). Equivalently the outgoing derivative sum is \(-1/N\) at \(g\), \(1/N\) at \(v_N\), and zero at intermediate vertices. Adding the fixed reference degrees gives
\[
 \operatorname{MA}_\theta(f_N\circ p_N)
  =(2-1/N)\delta_g+(1/N)\delta_{v_N}.
\]
The associated rational model class has nonnegative degree on every component. On this curve that is relative nefness, so the text's admissibility conclusion follows at the model level. The function lies in \([-1,0]\).

### Exact upper and lower bounds; quantifiers

The previously reviewed endpoint formula, applied with \(v_N\) as the left endpoint, uses reference endpoint masses \(0,2\) and resistance length \(N\). It gives
\[
 \operatorname{Cap}_\theta(p_N^{-1}\{v_N\})
   =0+\min(2,1/N)=1/N.
\]
This upper bound concerns the full normalized BFJ competitor class, not merely functions on this particular model; that is precisely the conditional graph-to-BFJ interface independently checked in the parent audit.

The explicit rational model competitor gives singleton mass \(1/N\). Since the singleton lies in its retracting tube, capacity monotonicity gives the reverse upper bound. Consequently both capacities are exactly \(1/N\). As \(N\) varies, only the divisorial point and the determining model change. The fixed-pair uniformity gap is therefore repaired.

The endpoint calculation requires no irrational breakpoint approximation and no weak-limit assertion for a fixed Borel singleton. The maximizing competitor is already a rational model potential.

## Mechanical exactness and retained gates

Independent read-only checks recorded in VALIDATION.json establish:

- all five files recorded by the author revised1 manifest have the exact stated byte counts and hashes; the manifest itself is separately hashed;
- the original proposed chapter agrees with the author manifest's source hash;
- the full original core occurs once in revised1 after the sole requested title replacement; its remaining bytes are unchanged;
- the fixed-reference fragment occurs exactly once and with exact bytes;
- all 213 parent labels survive, with exactly one new label, `ex:ch25-fixed-reference-small-capacities`; no duplicate labels are introduced;
- the excluded later Thuillier-relative subsection is byte-for-byte unchanged;
- the revised cumulative patch exactly equals an independently generated live-to-revised diff;
- a read-only `git apply --check` succeeds after normalizing only the diff's path headers; the patch was not applied;
- the live Chapter25 file remains at 195184 bytes, SHA256 `47c5c5897173168f9d5e21cbb7bdd86338ccf4e72b466f84acea917ea2b25fad`.

The cumulative revised patch replaces the original cumulative patch for any eventual integration; it is not a second patch to apply after the original. No fresh TeX build or production run was performed in this audit. No live manuscript file, author packet, or prior audit artifact was changed.

