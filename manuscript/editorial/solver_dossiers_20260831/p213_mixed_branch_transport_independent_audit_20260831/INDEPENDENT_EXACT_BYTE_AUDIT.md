# Independent exact-byte audit: mixed-branch coefficient transport

Date: 31 August 2026. Reviewer: `/root/p082_independent_reaudit`.

## Verdict and independence

**PASS for the complete standalone statement at the frozen hashes below.** No unresolved substantive mathematical gap or required correction was found. This is an independent mathematical audit, not production acceptance, a literature-priority decision, or retirement of P21.3.

The exact standalone conclusion is C_T=B_T for the two displayed moments on the actual finite-L/F torus domains, with canonical coefficients [L:F]. The review retains arbitrary complete nontrivially valued F, arbitrary finite L/F, and only positivity and d'-closedness of the ordinary F-current. It adds no discreteness, residue-field perfection, algebraic closure, separability, tame ramification, d''-closedness, or source-calibration representation hypothesis.

The author of the candidate is `/root/p081_weighted_repair_fresh`; `/root` supplied the outline. This reviewer did not author the candidate, supply that mixed-branch outline, or edit its proof. However, the reviewer authored the earlier tame-branch transport B_T(p,N)=N b_T(p), its mixed-rank non-separation diagnostic, and the later conditional common-moment supplement. Thus this is not a review from a person unfamiliar with the related construction. The candidate's **standalone core is audited independently without using that earlier authored theorem**. Its optional application to the earlier packet is checked only as a conditional substitution, with that provenance disclosed; this report does not independently re-certify its reviewer's own earlier theorem.

## Exact frozen candidate

Directory: `/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260831/p213_mixed_branch_transport_research_20260831/`.

| Input | Bytes | SHA-256 |
| --- | ---: | --- |
| `statement.tex` | 2093 | `445ca5b585be25261a732e00fe4c5d591a6648f165f5bba31119b9c4d30d3d97` |
| `proof.tex` | 9247 | `ab1e709ff79b02d52fb5d091b1a141d3e4687c0b663060249a43be6a1e9dad8f` |
| `MANIFEST.json` | as recorded in audit manifest | `7f702a642668d1e33b4c78b5b21814fb930fd86e9acbf1e9bc2cb988d29ee890` |
| `SOURCE_INTERFACE.md` | 6216 | `faeac68eea77615ac8a6571de0a5aa4385feaf231e2123ce91250636eee62d3b` |
| `RESEARCH_STATUS.md` | 2105 | `25195391f00941a13f8263441c7245a23f41b14716e4bdbff1f38b8e8130c281` |

The entire statement, entire 249-line proof, source interface, research status, candidate manifest, and validation record were read. All 21 candidate-manifest entries were independently checked for hash and byte length. The five recorded input pins and ten predecessor-manifest entries were separately recomputed: no mismatch. No candidate checker that writes into its packet was run.

## 1. Full domain and field scope

Statement lines 4-20 and proof lines 5-25 are correct in their declared scope.

The change q=w-t, with inverse w=t+q, identifies E with the actual torus domain 0<v(t)<delta and v(q)>v(t). The inequality |q|<|t| gives |w|=|t|, hence 0<v(w)<delta exactly as required for inclusion in D. In coordinates t,q/t this is the product of an open annulus and a punctured open unit disc. This reasoning concerns analytic maps and seminorms on the whole domain, not merely its Gauss points.

All functions t,w,q on their indicated domains are analytic functions in the F-analytic structure as well as in the displayed L-description. No arbitrary current is transported to L or interpreted there. Finite L/F is used to describe an actual source and, separately, to compute the canonical coefficient. Purely inseparable finite extensions do not invalidate these operations: the same domain is good, separated and boundaryless over F, and no geometric smoothness over F is used by the calculation. CLD's canonical finite-field interpretation formula has no separability restriction.

For each compact target support, both coordinates stay in a bounded range away from excluded zeros, and the relevant inverse image is a closed subset of a closed polyannulus. For E, a compact subset of Q_E also stays away from h=r and r=0,delta. These are compact non-Archimedean analytic domains even when their defining real radii are not norms of field elements. No unmentioned strict-radius condition is needed. This establishes legitimate compact support for the target tests and their primitives.

## 2. Existence, finiteness and uniqueness of the coefficients

Proof lines 27-58 correctly construct the two coefficients without a source representation theorem. Positivity bounds the scalar target functional on each fixed compact support by its value on one cutoff, which is finite because T is a current. This gives a locally finite positive measure, not a claim that the whole bidegree-(0,0) analytic current is a single Radon measure.

The pullback of a compactly supported (1,2)-primitive is a legitimate compactly supported analytic test. Hence d'T=0 makes both scalar distributional first derivatives zero. The Euclidean convolution argument gives a constant on every ball; testing against one integral-one function identifies its finite limiting value. Overlapping balls propagate that value across each connected target. Both Q_D and Q_E are nonempty connected open sets for every delta>0. This proves finite B_T,C_T>=0 and uniqueness, including the possibility that both are zero. The use of only d'-closedness is sufficient.

## 3. Unit functions and all three source regimes

Proof lines 61-87 use only logarithms of actual analytic units on U=D minus {q=0}. In particular zeta=v(q/t) is finite there; no derivative across q=0 is taken. CLD Section 18.1.2 explicitly supplies smoothness and d'd''=0 for log-unit functions; alternatively these are affine coordinate functions of a moment.

The relations y<0 implies zeta=y, y>0 implies zeta=0, and zeta>0 implies y=0 follow from strict ultrametric domination. If y=0, the ultrametric inequality gives zeta>=0. Thus there is no missing source region. The proof correctly does not claim ordinary-open constancy at y=zeta=0.

## 4. Compact primitive: no missing divisor or annulus boundary

Proof lines 89-135 specify compatible cutoffs for every delta>0. The choice kappa<min(a,delta-b) ensures that the closed polyannulus

\[
 a\le r\le b,\qquad a-\kappa\le s\le b+\kappa
\]

is compactly contained in D. The zeta bound further gives

\[
 |q|=|t|\,|q/t|\ge\exp(-(b+\epsilon))>0.
\]

The possible support is therefore a closed subset of one compact source domain disjoint from q=0. This is an actual analytic support bound. It controls deep zeros of q and both ends of each punctured coordinate, not merely the target picture. The zero extension of beta is an ordinary smooth compactly supported form on D. No extension of the current itself is performed.

## 5. Cancellation and central-set support

Proof lines 137-175 pass the critical closedness check.

- The derivative of phi repeats d'r and vanishes.
- In the eta'-term, y<0 gives zeta=y and chi(y)=0 whenever eta' can be nonzero.
- On y>0, zeta is identically zero on that whole ordinary open region, so d''zeta=0 there.
- At y=0, eta' vanishes on an ordinary neighbourhood by continuity and its chosen constant interval.

Thus the eta'-error is zero as a smooth source form before pairing with any current. The remaining derivative has the positive displayed sign, since d'zeta moves past two one-forms. As chi' vanishes on an interval around zero, this derivative is identically zero on an ordinary neighbourhood of each point with zeta=0. Its two remaining supports are compactly contained in zeta<0 and zeta>0. There is consequently no unaccounted central-face term, and no lower-face noncharging, current slicing, or representation premise has been smuggled into the decomposition.

## 6. Independent sign and Jacobian check

On the negative region zeta=s-r, substitution into the top wedge gives

\[
 d'r\wedge d''r\wedge d'(s-r)\wedge d''(s-r)
   =d'r\wedge d''r\wedge d's\wedge d''s.
\]

Terms with repeated d'r or d''r vanish. The shear matrix has determinant one, so there is no form or Lebesgue factor. The coefficient phi(r)chi'(s-r)1_{s<r} is smooth across s=r because chi' vanishes on a neighbourhood of zero, and its support is compactly inside Q_D. Since r>a>epsilon,

\[
 \int_0^r\chi'(s-r)\,ds=\chi(0)-\chi(-r)=1.
\]

The negative-side contribution is therefore **+B_T**.

On the positive region, h=r+zeta, y=0, and the r-cutoff puts the entire contributing source inside E. The second shear has determinant one by the same wedge calculation. The test phi(r)chi'(h-r) is compactly supported inside Q_E, away from h=r. Its inner integral is

\[
 \int_r^\infty\chi'(h-r)\,dh=0-\chi(0)=-1.
\]

The positive-side contribution is **-C_T**. Closedness of the zero-extended primitive gives B_T-C_T=0. No smoothness or monotonicity of chi beyond the stated cutoff properties is required. The normalization integral(phi)=1 is the only integral normalization used.

## 7. Canonical finite-extension degree

Proof lines 231-248 correctly separate the arbitrary-current argument from the canonical calibration computation. The two actual torus coordinates are primitive over L and the coordinate moments have local degree one, giving coefficient one there. CLD Remark 14.4.3 multiplies the canonical calibration of the same space viewed over F by the full finite degree [L:F]. Its statement does not require the extension to be unramified, tame or separable. The proof introduces neither ordinary-open covering sheets nor an extra ramification factor. Both shears already have determinant one.

Accordingly B_deltaD=C_deltaD=[L:F]. This does not assert that an arbitrary F-current has a scalar extension or descent as an L-current.

## 8. Conditional application and preserved obstruction

The source interface correctly matches its optional application to the earlier authored packet. Under that packet's actual source identification, D_pN has exactly the present D-shape, with F=K and L=L_p. Restricting the original current to this ordinary source gives B_T=B_T(p,N) by equality of the test formulas and uniqueness. Conditional on the prior formula, the new result gives

\[
 C_T(p,N)=B_T(p,N)=N b_T(p),\qquad C_{\delta_X}(p,N)=N d_p.
\]

The original mixed rectangle a<v(t)<b<c_1<v(q)<d_1 lies in Q_E because 0<a<b<delta. Its compactly supported target tests are covered by the newly determined coefficient. This is a correct application of the standalone equality, not an independent review here of the reviewer's own tame-branch theorem. The additional normalized conclusion equals c only when b_T(p)=c d_p is supplied as its separate prior input.

The earlier rank-collapse diagnostic remains true: the previously certified coordinate top forms vanish on this mixed domain. The new connecting primitive is an additional closedness test, not evidence that those old forms already spanned the new target test. No arbitrary source-multiplier formula, all-moment separation, scalar rigidity on E or D, or iterative accessibility theorem follows from this packet. Its explicit exclusions are accurate. The actual-H supplement and the unaudited source-representation packet are not mathematical dependencies of the standalone result.

## 9. Exact-byte, syntax and visual-review limits

- All 21 candidate-manifest entries matched their recorded hashes and byte lengths.
- All five input pins and ten predecessor entries matched independently recomputed values.
- The principal statement and proof hashes match the author-provided frozen hashes above.
- A direct byte scan found no prohibited C0/DEL control bytes in the statement, proof, source interface or research status.
- The final native TeX/BibTeX logs were inspected. The only matching draft warning is the expected pdfdraftmode notice; no unresolved citation/reference or overfull/underfull warning was found in the final logs. The bibliography identifies CLD's correct v2 date. This is verification of preserved build evidence, not a new compilation or a mathematical argument.
- No candidate PDF exists: the recorded build is draft-only. No candidate PDF visual QA is claimed. Primary mathematical passages were read in the exact local CLD text; this audit does not relabel previous source-page image checks as new visual work.

No candidate, predecessor, live book, inventory or git state was modified; no production call was made. The result of this review is the bounded mathematical PASS above and the separately qualified conditional application, with no claim that P21.3 has been solved.
