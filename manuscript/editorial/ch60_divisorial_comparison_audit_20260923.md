# Chapter 60: finite vertex tests and divisorial comparison

Date: 23 September 2026.
Baseline: `60662f38fb43c05e1c417be9c89bdf06870eeda6`.
Scope: Section 60.4 of `parts/part5/ch60_mp_psh.tex`, from the monotone
completion heading through continuity of the obstacle supremum. The text
before that heading and from the definition of the extended pairing onward
retains its baseline bytes. This unit reconstructs established mathematics;
it retires no research atom.

## Mathematical checks

The real-model approximation and arbitrary decreasing-net closure proofs
are preserved mathematically. Their inline notation and first exact-version
source locator have been normalized. The general psh definition retains
noncollapse and approximation on the entire spectrum.

The new analytic negativity lemma applies to a composition of blowups with
smooth centers over the central fibre. An effective exceptional divisor F
with positive coefficients on every exceptional prime and relatively ample
-F is constructed by induction. If q_*G is nonpositive and G has a positive
coefficient, t=max coeff(G)/coeff(F) makes tF-G effective and leaves one
exceptional component outside its support. A curve through a general point
of that component, contained in a projective fibre, contradicts q-nefness.
The isomorphism case is separated. The argument uses projectivity relative
to the analytic base and does not presume that X is projective algebraic.

For a PL obstacle on a fixed snc model, the maximum of phi-psi is attained
among that model's finitely many central vertices. For a model potential,
subtracting the obstacle pullback and the vertex maximum gives a vertical
divisor with nonpositive pushforward and nonnegative degree on contracted
curves. Negativity and the model retraction formula prove the upper bound
on every character, including proper-support characters. A finite maximum
commutes with a decreasing directed net, also when the limiting maximum
is minus infinity. The product model then proves sup(phi)=phi(v_triv) is
finite using noncollapse and a model majorant. This step precedes and does
not use finiteness at all divisorial points.

The fixed-model oscillation estimate is reconstructed from the weighted
intersection graph. Projection formula on a common domination gives
A_j+sum_k b_k u(v_Ek) Q_jk >= 0. Here A_j>=0, off-diagonal Q_jk is positive
exactly for intersecting components, and the weighted row sums vanish.
Connectedness follows from the connected fibres of a proper modification
to the normal connected product. The finite vertex test supplies one vertex
where x_j=sup(u)-u(v_Ej) is zero. With w_jk=b_j b_k Q_jk, the inequality is
sum_{k!=j} w_jk x_k <= d_j x_j+B_j. A minimum positive edge weight w, maximum
weighted degree d and maximum B_j give C_0=0 and C_(l+1)=(d C_l+B)/w.
Paths have at most N edges, so C_N bounds all vertex deficits independently
of the potential and its representing model. The single-vertex case is
removed before taking a minimum of edge weights; n=1 uses empty products.
No integrality of the real Kähler intersection weights is assumed.

For a general psh potential the original decreasing model net satisfies
u_lambda(v)>=sup(phi)-C. Passing to the limit proves divisorial finiteness
without subtracting varying suprema from the approximants. Dimension zero
is treated separately. Comparison with a PL obstacle follows from the
finite vertex test; uniform rational PL approximation gives continuous
obstacles. Continuous real majorants of an upper semicontinuous function
on the compact Hausdorff spectrum have that function as their infimum.
The proof constructs such a majorant with any prescribed value strictly
above the obstacle at a point, including at a minus-infinity value.

The P1 example u_j=-min{v(I_p),j} decreases to -v(I_p). Its finite divisorial
values coexist with a pole at the character supported at p. On the ordinary
point-blowup model, b_0=b_1=Q_01=A_0=1 and A_1=0, and the bound C=1 is
attained. The indicator of the supported endpoint is an explicit upper
semicontinuous counterexample to determination by density alone.

Finally, divisorial evaluations define a Hausdorff topology on PSH(alpha),
and phi -> sup(phi-psi) is continuous for every continuous obstacle psi.
For PL obstacles this is a finite maximum of real evaluations. Uniform
approximation extends the assertion, with an error bounded independently
of phi by the uniform obstacle error. Finiteness of all these suprema is
stated before applying the uniform estimate.

## Primary-source verification

The source is Mesquita-Piccione's
[18 September 2025 author version](https://arxiv.org/html/2409.06221v2),
identified in the bibliography by `MPTropicalV2`. Section 4.3 was read in
the cached primary-source text, and printed pages 40–42 were rendered and
visually checked. Relevant locators are:

- Definition 4.3.1, p. 39: the monotone completion.
- Theorem 4.3.3, p. 40: fixed-model divisorial bounds.
- Proposition 4.3.6, p. 41: finite testing for PL obstacles.
- Corollary 4.3.7, pp. 41–42: obstacle-supremum continuity.
- Theorem 4.3.8, p. 42: upper semicontinuous comparison.

Source PDF SHA-256:
`9eb2ea7686a5962ebc11c5eacd23b0cb3dcb081e27ac48292933f291fc82cb23`.
The cofinal resolution and relative-ampleness constructions use the earlier
Chapter 59 arguments and their locators, Remark 2.5.2 and the proof of
Theorem 2.6.4 in this same version.

The proof order makes the maximum on fixed vertices available before the
graph bound. The source's diagonal bound by -1 is not used for arbitrary
real Kähler weights: the book instead keeps their finite positive minimum.
The new negativity argument avoids importing an algebraic DVR statement
as an unproved assertion in the analytic model category. The source's Rees
valuation argument is not needed for this route. No journal locator is
inferred from the author-version numbering; bibliography bytes are unchanged.

## Two passes and validation

The first full build produced 3,975 pages (18,918,486 bytes). Physical pages
3353–3362 were rendered and inspected. A second complete statement, proof,
exception, source and prose pass made the empty-product and single-vertex
conventions explicit, improved the graph-notation cross-reference in the
example, stated finiteness of the obstacle suprema, and kept the divisorial
bound's introducing line with its display. The final full build and review
of physical pages 3353–3362 were repeated. This scoped review includes the
unchanged transition to extended energy; it is not an all-page visual audit.

- Full build: PASS, **3,975 pages, 18,918,742 bytes**.
- Reference/input audit: **390 TeX files, 11,623 unique labels**; no missing
  input, duplicate label, dangling reference or structural defect.
- Final log: no unresolved reference/citation, multiply-defined label,
  rerun request or horizontal/vertical overflow. Existing class/underfull
  warnings remain.
- Scoped strict house audit: zero errors, one reviewed exact-author-version
  arXiv warning. Strict mode returns 1; no warning-free strict pass is claimed.
- Inventory: PASS, **45 atoms / 14 formal environments**, tiers
  **(0,5,8,15,17)**.
- Whitespace check: `git diff --check` passes.

Final Chapter 60 SHA-256:
`961549c2b8c0192d90f06e7e0a9e5a867b7a71dc849b82d34f6880d22c4eafe8`.
Final live PDF SHA-256:
`fce1f971588c88ead14161eb9ee8076cfd0fd53da23287fc6c5faa80ad0208b0`.

The completed P12.1 integration remains at commit `2de7848`. Its Chapter 70
fragment retains SHA-256
`8d9f9bd9edb057b95773479279bbdabb3240319e4cb56f6f15cb2bd923fb4380`.
The supplied PDF and archived copy retain SHA-256
`71f5e0d50bdcbf493cb96a869e2db03a78bd591b3eba2f797da5a23f6253daaa`.
P12.2–P12.6, author originals, frozen packets, verifier receipts, historical
audits, bibliography and dated releases are unchanged. No independent-agent
or production-verifier pass is claimed. The PDF is the ignored live build
product. The overall audit continues with extended mixed pairings and the
finite-energy measure construction.
