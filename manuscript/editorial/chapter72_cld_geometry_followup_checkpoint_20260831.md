# Chapter 72: further CLD geometry — 31 August 2026

This follows the product checkpoint committed and pushed as
`06e5bcd897df2a490ba618d1becd3e22e2890270`. No full solution of P21.3 or
production acceptance is claimed here.

## Annular torsors, including nontrivial normal bundles

The residual-curve functional proof now covers the annular torsor of any
line bundle on the specified entire smooth proper good-reduction curve
model over a complete DVR with perfect residue field. There is no nefness,
degree or triviality assumption on that line bundle. The actual positive
closed ordinary CLD current gives coefficients satisfying

\[
 \sum_p\operatorname{ord}_p(f)b_T(p)=0,
 \qquad b_T(p)=c[\kappa(p):k].
\]

A rational section supplies an ordinary analytic coordinate on the
complement of its horizontal divisor. Its relation to the metric radius
is an integral shear. The proof controls the support in a compact radial
strip before using closedness, rather than globally differentiating the
formal metric. An explicit original-field O(1) example has a pulled-back
radius max(t,ell-t), whose second-derivative test is nonzero. Curvature is
therefore not being assumed away.

The frozen proof is in
`solver_dossiers_20260831/p213_annular_torsor_residual_functional_research_20260831`;
its manifest is `ec7f22f0fd750a325139c2f7403e213b53e921b5f1f89e5ab45ac6e0f059da30`.
The separate independent mathematical audit found no substantive gap in
that exact scope. Its report hash is
`96d669f15ee36f83cb423b674a3203b24b0545c76fcd268fbed71536c1cf7d45`.
Root read the entire candidate, examples, report and source ledger and
rechecked all 15 candidate and 20 audit-manifest entries.

Only the final source-calibration interpretation assumes the earlier
representation packet. The actual coefficient construction and principal
relation do not. There is still no whole-torsor scalar-rigidity theorem,
and an arbitrary semistable formal neighbourhood has not been identified
with such a torsor from its normal bundle alone.

## Additional source families in the product

A separate frozen research note proves the transport formula
\(B_T(p,N)=N b_T(p)\) for an integer N invertible in the valuation ring.
The new parameter is \(t=z^N/\pi-1\). Its positive branch is one analytic
domain over the Eisenstein coefficient field, viewed over the original
field, not N ordinary sheets. The canonical coefficient is
\(N[\kappa(p):k]\). This proof uses another compactly supported closedness
test and does not require the representation packet.

The note also exhibits mixed-coordinate forms missed by both the original
collars and all these transported integer families. This refutes only a
test-spanning shortcut; it is not a positive-closed-current counterexample.
The original note is preserved without alteration. Its final informal
accessibility paragraph is supplemented by a precise sufficient condition
using the actual common analytic moment H=(F,G), representation for all
three moments, an isolated identical source patch, and full-rank
projections. That condition is not asserted to hold for arbitrary charts.

Independent review now accepts the branch formula and both rank-collapse
diagnostics under the disclosed inherited product premise. It accepts the
all-moments criterion only under the full representation hypothesis. The
original accessibility paragraph still has an omitted source-form bridge;
the separate actual-H supplement is accepted under its explicit stronger
premises, not as a proof of universal accessibility. The exact original
report and supplement addendum have hashes
`e41a147fa1cebaf68e01d354e612a59e7ce637a0ffabca6422104cd2a5de3b28`
and `36a14228b5fff4703fcb96d04372d8231ce1c7e3ca0fc828c03b94c484291f5e`.
Root read both reports and the entire source ledger and checked all 20
audit-manifest entries and 21 checksums without mismatch. The reviewer
authored the inherited product premise and explicitly assumes it here;
that premise has its own separate independent audit.

## The mixed branch across w=t

There is now a separate complete proof comparing the coefficients on
the original (v(t),v(w)) cone with the (v(t),v(w-t)) cone on which
v(w-t)>v(t). It gives C_T=B_T using one compactly supported test and
only positivity and d'-closedness of an ordinary (0,0) current. The
field may be any complete nontrivially valued field F, with a finite
extension L/F; all current operations stay over F, including when the
extension is inseparable. The canonical coefficient on both domains
is [L:F]. No representation hypothesis or current base change is used
in the standalone comparison.

The cutoff primitive avoids the removed divisor w=t and all boundary
faces. The differentiated form vanishes on an ordinary neighbourhood
of the central tropical vertex; its two remaining pieces give +B_T
and -C_T. Thus no unknown-current noncharging assertion is hidden at
the vertex. The optional product application explicitly assumes the
previous branch identification and formula B_T=N b_T(p).

This reaches the particular mixed family that the preceding note showed
was invisible to the old test families. The rank-collapse diagnostic
remains correct: the new conclusion uses an additional closedness test,
not a spanning claim. Arbitrary moment compatibility and whole-current
rigidity still do not follow.

The frozen candidate manifest is
`7f702a642668d1e33b4c78b5b21814fb930fd86e9acbf1e9bc2cb988d29ee890`.
Root read the statement, proof and source interface and ran the read-only
checker: 21 candidate entries, five direct input pins and ten prior
manifest entries match, with zero structural defects. A separate
independent audit accepts this exact standalone scope without adding
discreteness, perfection, separability or a representation hypothesis.
Its report hash is
`64fb36e4b77006707218bde26aff2fe818b206e5281254d28e6242ee078cf935`;
its manifest is
`74e8a45c59b7e718daf6bc70c8868c4df08d896c48963b88fc0b2b993e49c2f7`.
Root read the entire report and source ledger and independently checked
all 24 audit-manifest entries and 25 checksums. The reviewer authored
the optional earlier branch premise and explicitly assumes it for that
application; the new standalone proof does not use it.

## Build and future integration notes

The torsor's first draft check stopped on an unescaped underscore in its
frozen bibliography note. That failed attempt is preserved. A second
wrapper adds the standard underscore-text package without changing the
mathematical source or bibliography; three draft-mode TeX passes and
BibTeX then succeed with eight labels, seven references and no final
warning or box defect. No PDF is generated. The successful build manifest
is `6a3671d8a1cd3d70b97728558a48ed039eb840badfa01a04bb5287fdc65b1568`.

The mixed-branch candidate has its own clean final draft-mode TeX/BibTeX
build, with no PDF. Its pre-freeze overlong-display attempt is preserved
in build_history, separate from the frozen final statement.

At eventual integration, escape the bibliography filename, make the
target/source volume-form notation explicit, and typeset the exponential
constant in roman style. Preserve `eqref` and use `cref` for theorem and
section references. These are recorded changes for a future reviewed
assembly, not edits of frozen audited bytes.

All new results still require production Rethlas acceptance. The broader
representation, arbitrary source-cell compatibility, general semistable
deformations and positive current bidegrees remain unresolved here. No
new live theorem has been inserted and no atomic problem removed. The
inventory remains 51 administratively active entries in 14 environments,
with its existing scope qualifications. No book PDF was rebuilt, no
production endpoint was called and no permission workflow was bypassed.
