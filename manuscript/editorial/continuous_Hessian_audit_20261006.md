# Continuous Hermitian Hessian domination and auxiliary limits

**Known result import and direct conditional consequence.** The baseline
is `dc52f4cf972cb809c803ec20cdff4d19574f47f2`. Chapter 68.9.5 explains
continuous global domination and its auxiliary-limit mechanism;
Appendix L.56 records primary editions, normalizations and proof scopes.
The new bounded Hermitian regularity theorem is not admitted in full.

## Mathematics and scope

Fix a connected compact complex manifold, two Hermitian forms omega
and omega_X, and 1<m<n. The reference omega_X remains fixed. The
canonical admissible class is defined by the mixed linear inequalities
against m-positive test forms. Smooth admissible eigenvalues belong to
the closure of Gamma_m and can be negative. This class is broader than
omega-psh. For continuous admissible potentials, smooth decreasing
approximation and uniform continuity define
H_m(u)=(omega+ddc u)^m wedge omega_X^(n-m).

The imported Guedj--Lu domination states that
1_{u<v}H_m(u) <= c 1_{u<v}H_m(v), with one constant 0<=c<1,
implies u>=v. Its zero-measure case uses the envelopes
P_m(bu-(b-1)v), contact support, mixed positivity and positive total
mass. Their suprema remain bounded below, so compactness gives a
locally integrable decreasing limit; a nonempty open strict sublevel
would force that limit to minus infinity there. The general factor
case reduces to this zero-measure case on the envelope contact set.
These are the known continuous arguments, not an original theorem.

For every a>0, exp(-a v)H_m(v)>=exp(-a u)H_m(u) implies u>=v.
The proof uses the fixed factor exp(-a delta)<1 on {u<v-delta}, then
lets delta decrease to zero. Mere pointwise strict inequality on
{u<v} supplies no uniform factor. The source potential normalization
changes the coefficient a without changing this argument.

For a given continuous solution phi of H_m(phi)=exp(f(x,phi))dV,
smooth admissible v_j tend uniformly to phi. Suppose smooth auxiliary
solutions u_j exist with H_m(u_j)=exp(u_j-v_j+f(x,v_j))dV.
Under the explicitly required uniform bounds and subsequential uniform
convergence, operator continuity gives
H_m(u)=exp(u-phi+f(x,phi))dV. Exponential comparison in both directions
identifies u=phi. The sign of the original f derivative is immaterial
to this auxiliary identification.

The second auxiliary equation is
H_m(tilde u_j)=exp(tilde u_j-u_j+f(x,u_j))dV. Uniform potential and
full second-derivative bounds for **both** auxiliary sequences are
explicit assumptions. They give C^(1,alpha) compactness; both uniform
limits are phi. The second density has uniform positive lower and
Hölder bounds. A bounded admissible spectral set with a positive
sigma_m lower bound lies compactly inside Gamma_m, where its root is
concave and uniformly elliptic. The known complex Hessian estimate
gives uniform C^(2,alpha) bounds for tilde u_j; the limit and elliptic
bootstrapping make phi smooth. This passage does not prove the required
uniform second-order estimates. Uniform convergence of v_j alone
does not bound its derivatives or the first auxiliary density's
Hölder norm.

No arbitrary bounded solution is made continuous here. Gu--Nguyen's
bounded local operator and comparison assume a locally conformal Kähler
reference metric, while its smooth approximation extends further via
a distinct maximality input. Kołodziej--Nguyen Theorem 2.16 permits
a bounded competitor but assumes the zero-Hessian potential is
continuous and uniformly smoothly approximable. The later background
class must be checked separately. A Gauduchon metric used in a mass
estimate is auxiliary: replacing omega_X changes the fixed Hessian
operator when m<n. Original-equation existence and uniqueness,
normalized-volume and spectral limits, and non-Archimedean Siu/closure
questions receive no further implication from this conditional passage.

## Primary readings reused

The preceding [comparison review](Hessian_global_comparison_source_review_20261006.md)
read and displayed 44 actual research-text pages in 23 sheets:

- Guedj--Lu [arXiv:2302.03354v1](https://arxiv.org/abs/2302.03354v1),
  submitted 7 February 2023 at 09:55:38 UTC, all fifteen pages.
  Approximation is on 4--5, continuous construction and contact on
  5--7, positive mass on 8, and global domination and exponential
  comparison on 9. The PDF SHA-256 is
  `f59aed6df00cce7f39fb0752909741d6b156e23edb3a5a2f34ef087bfea98458`.
  The source ddc=2i partial bar-partial takes source potential
  phi/(4 pi) for the book's forms. Its 2025 twenty-four-page journal
  PDF returned 403 and was not acquired or reviewed.
- Gu--Nguyen's published 2018 Dirichlet paper, actual 1--17 and
  50--53, printed 1189--1205 and 1238--1241: twenty-one selected
  pages of sixty, not a full-paper reading. Its PDF SHA-256 is
  `ca15ac50ff5453102222383090319b9f1cc0fa483999c7df341eaa1ed388bea0`.
  The source ddc=i partial bar-partial/pi takes half the book potential.
- Kołodziej--Nguyen [arXiv:1507.06755v2](https://arxiv.org/abs/1507.06755v2),
  revised 10 March 2016 at 11:24:27 UTC, actual 12--13, containing
  Theorem 2.16 and Lemma 2.17. Ten other selected pages of this exact
  twenty-seven-page edition were read in the preceding Fang dependency
  review; neither record is a full-paper reading. Its PDF SHA-256 is
  `e312b98ef0e16d90a1156ce6fb23237059ff52a3d9fca6bc84782429804882ce`.
- Boucksom--Guedj--Lu [arXiv:2406.01090v1](https://arxiv.org/abs/2406.01090v1),
  actual 1--4 and 28--29: six selected pages of thirty-three. Its psh
  Monge--Ampère comparison is not substituted for intermediate Hessian
  comparison. Its PDF SHA-256 is
  `d7637564a1b1b728743bc5ae315c336097139d12ebca9f43469d721947f8f031`.

The comparison records have SHA-256
`49c804858bc5a6c8661d20f6fa7d074bc44956765a5dc38ac41f69bf3a0341a2`
and `b48794667b57e12e128c1d104083dca3f6e7a9c71d86725c8d65548e94757b24`.
The frozen comparison manifest SHA-256 is
`ac241915e6fbebe683c54e48d5527b7636ab014ad723c4cb6d18fe241287d1b4`.
Four literal diagnostics concern wedge powers, nonclosed background
derivatives and a reference-metric change. Their history is retained;
they neither refute the main theorems nor certify a complete repair.
Appendix L writes the ordinary corrected difference-of-powers identity.
Envelope contact and mixed-current antecedents retain their cited scope.

The conditional elliptic step reuses Tosatti--Wang--Weinkove--Yang
[arXiv:1402.0554v2](https://arxiv.org/abs/1402.0554v2), revised
13 October 2014 at 22:23:58 UTC, actual 1--7 and 10--12. Theorem 1.1
and Section 2.1 lie in this ten-page selection of a twenty-six-page
paper. Its PDF SHA-256 is
`d0ac1fdca8ec5a682ff46597d4be92f12d619e50aa19ca5d21d9add7e550f669`.
The J-invariant image restriction supplies the compact spectral set;
the projection's unbounded kernel is excluded. The full abstract
elliptic proof and journal edition are not claimed freshly read.
The combined earlier Fang dependency record SHA-256 is
`bc23edf5fd608428d15ee89c201cf0ee9d0388c2e0818ad503623aecdbdbbde4`.
This integration adds zero fresh primary-page readings and four exact
version-specific bibliography entries.

## Final validation and PDF review

The final book has **4,394 pages**, 20,417,593 bytes and SHA-256
`db4ec5558b81aea2696f3f822ebdf36a5e692e8e0604f7e2b676637f63075bf8`.
TeX errors, package/pdfTeX warnings, missing glyphs, overfull boxes,
unresolved references/citations and rerun requests are zero. The 954
nonfatal underfull diagnostics equal the preceding build's count.

The post-render reference check finds 425 active inputs and 12,851
unique labels, with zero missing inputs, duplicate labels or dangling
references. There are 378 cited bibliography entries among 673 keys
and no bibliography warning. Seven labels and five explicit equation
tags are new; all 141 Chapter 68 equation numbers are unique. The
index accepts all 764 entries, rejects zero, and has 1,012 lines, 763
page groups and 419 valid numeric destinations. No index entry is
added. Navigation has 21,958 named destinations, 47,045 internal links,
171 external URL links, 2,564 contents entries and six parts; invalid
links, destinations and contents pages are zero.

All **39 matching final PDF pages** were individually displayed and
their complete extracted text read in twenty sheets: actual 61, 68,
3619--3623, 4156--4159 and 4367--4394. These cover affected contents,
the complete addition and neighboring transitions, both adjacent
provenance sections, the following appendix, and the complete index
and bibliography. The frozen view manifest SHA-256 is
`ec2bca09879755d0f022d8efdde6a02814cb31e1d67c03701aa87405f48e8956`.
This review does not claim a fresh reading of all 4,394 pages.

## Preservation and publication

Chapter 68 and Appendix L are the two changed active inputs. All 423
others and all 108 protected inputs retain baseline bytes. The edited
files preserve all 34 existing statement/explanatory blocks and twelve
proof blocks, 46 in total, with no new formal environment. The
non-Archimedean bibliography is unchanged. README and the research
programme record the completed integration.

All 63 prior frozen manifests, 54 integrations and nine source reviews,
and all 118 prior exports retain their bytes. The other 5,044 tracked
baseline files remain unchanged. The canonical inventory passes with
42 atoms, twelve families and tier counts 0/3/7/15/17. All complete
status rows, the inactive toric candidate and native catalogue source
and PDF retain their bytes. The native editor remains open without
editing, recompilation or tab change.

The release consists of the full PDF, a 39-page review PDF and a source
archive with 656 byte-verified members and a passing CRC check. The
archive includes all 425 active inputs and both bibliographies. No
fresh isolated archive compilation is claimed. The integration
manifest, closure and artifact record pin this edition. Both main
and work are explicitly fetched before publication on the existing
work branch and draft PR. Routine GitHub synchronization follows the
user's standing authorization without repeated confirmation and with
platform permission checks retained.

No original result, independent production model call, verification
receipt, canonical solved status or general Siu/closure repair is added.
Continue with the bounded background-class comparison and specialized
uniform-estimate dependencies before any broader regularity admission.
