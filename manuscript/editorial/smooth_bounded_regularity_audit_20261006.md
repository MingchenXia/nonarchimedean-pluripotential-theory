# Smooth bounded solutions and auxiliary identification

**Known result import and direct conditional consequence.** The baseline is
`2cfe2a54172c002f04df450c20f30902e7fcb57b`. Chapter 68.9.4 connects
bounded-solution smoothness with the existing mean-field discussion;
Appendix L.55 records exact source scopes. Smoothness, existence and
uniqueness of the original equation have distinct hypotheses.

## Mathematics and normalization

On a connected smooth compact Kähler manifold, an existing bounded
omega-psh solution of MA(φ)=exp(f(x,φ))dV is smooth when f and the
positive volume form dV are smooth. No monotonicity in φ is required.
This is Székelyhidi--Tosatti Theorem 1.1, not a new result. A big-class
potential with minimal singularities need not be globally bounded.

Writing dV=h omega^n and w=φ/(2 pi) gives the source's metric convention
and F(s,x)=-f(x,2 pi s)-log h(x). The given density is bounded above
and below, so the standard Lp continuity result applies. Smooth functions
v_j tend uniformly to φ; they need not be psh for this parabolic argument.
The prescribed-density potentials ψ_j use c_j=V/integral exp(f(v_j))dV,
which tends to one, and normalized constants yield uniform convergence.
The source flow converts to (1/(2 pi)) partial_t U_j = log(MA(U_j)/dV)
-f(U_j)-log c_j. At zero the right side is exactly f(v_j)-f(ψ_j):
the mass normalizer cancels. Uniform short-time estimates, comparison
and vanishing time derivatives give a smooth stationary limit equal to
φ. Long-time flow existence is not asserted.

The static auxiliary equation uses backgrounds omega_j=(1+epsilon_j)omega
and exponent u_j-v_j+f(v_j), with bounded smooth admissible v_j tending
almost everywhere to φ. Its positive coefficient of u_j is independent
of the sign of the original f derivative. Required uniform bounds and
subsequential uniform convergence are explicit hypotheses. Bounded-potential
continuity and dominated convergence then give MA(u)=exp(u-φ+f(φ))dV.
The given φ solves the same auxiliary equation. Domination on the two
strict sublevel sets, followed by delta tending to zero, gives u=φ.
This identification does not establish its a priori estimates, supply
original-equation existence or uniqueness, or certify the entire new
degenerate Hermitian theorem. Equations (68.23cw)--(68.23cz) keep all
normalizing factors. Existing preceding and following passages are intact.

## Primary sources reused

The preceding [source review](Hermitian_bounded_regularity_source_review_20261006.md)
read and displayed Badiane--Lu--Zeriahi
[arXiv:2610.06473v1](https://arxiv.org/abs/2610.06473v1), submitted
5 October 2026 at 15:02:53 UTC, in all 23 actual pages, including proofs
and references. Its PDF SHA-256 is
`ebd50dcc95674e20b8f9897421d65dc9737e01a7a6ff00b51f468099cfa0062e`;
the full-reading record SHA-256 is
`5762bf37c2fb1edafd9f4f3b67499818e5c4d1a0ebbf5e4dceaee5af6d139180`.

Székelyhidi--Tosatti [arXiv:0912.1808v2](https://arxiv.org/abs/0912.1808v2),
revised 26 March 2010 at 16:33:08 UTC, was fully read and displayed in
all nine actual pages. Its theorem is on page 1, short-time estimates
on 2--7 and stationarity on 7--9. Those are preprint locators, distinct
from Anal. PDE 4 (2011), 369--378. Its PDF SHA-256 is
`059a1f496d7a6f3413865bdd423b29b27ca078dd9449b1bdaaf4c188dc94a8f8`.
The source's external parabolic estimates retain their source scope.

Twenty-nine further selected dependency pages were read and displayed:
Guedj--Lu envelopes III v1, actual 1--3, 8--13, 17--18, 26--29;
Demailly's author-hosted Chern regularization paper, 1--2, 5--6, 11--13;
and Nguyen's Hermitian type-equation v1, 1--3, 13--16. These three papers
are not represented as fully read. The combined 38-page dependency
reading record SHA-256 is
`51d2995b1fb6cd0e79f929a2d73f08b770b706457667b60965cc372edd12c803`.
The integration reuses these records without claiming fresh primary
reading for the imported passage. The source review's eight literal
diagnostics and correction history remain frozen; they do not refute
conditional regularity or certify a complete repaired proof. Two exact
version-specific bibliography entries are added.

## Final validation and review

The final book has **4,392 pages**, 20,401,940 bytes and SHA-256
`5d8c6573199900e7014b68c16eb52c0911ed3649bd7cd0d8b8a3f995ee9c42fd`.
TeX errors, package/pdfTeX warnings, missing glyphs, overfull boxes,
unresolved references/citations and rerun requests are zero. The 954
nonfatal underfull diagnostics match the preceding build.

The post-render reference check finds 425 active inputs and 12,844
unique labels, with no missing inputs, duplicate labels or dangling
references. There are 374 used bibliography entries among 669 keys and
zero bibliography warnings. Six labels, four explicit equation tags and
two bibliography keys are new; all 136 Chapter 68 equation numbers are
unique. All 764 index entries are accepted, zero rejected, with 1,012
lines, 763 page groups and 419 valid numeric destinations. No index
entry is added. Navigation has 21,945 named destinations, 47,027 internal
links, 171 external URL links, 2,562 contents entries and six parts;
invalid links, destinations and contents pages are zero.

All **38 matching final PDF pages** were displayed and their complete
extracted text read in nineteen sheets: actual 61, 68, 3618--3620,
4153--4157 and 4365--4392. They cover affected contents, the complete
addition and transitions, provenance, the following appendix, and the
complete index and bibliography. The review manifest SHA-256 is
`87bce7065cdfdbb31cb93d1a3f9c2fae0ca092c69e846bda7318dedaff79be5c`.
This scoped release review does not claim a fresh rereading of all
4,392 pages.

## Preservation and publication

Only Chapter 68 and Appendix L change among active inputs. All 423
other active inputs and 108 protected inputs retain their baseline bytes.
The edited files preserve all 34 existing statement/explanatory blocks
and twelve proof blocks, 46 in total. No formal environment is added
or relabeled. The non-Archimedean bibliography remains byte-identical.
README and the research programme record the completed integration.

All 59 prior frozen manifests, 53 integrations and six source-only
reviews, and 115 prior exports retain their bytes. The other 5,035
tracked baseline files are unchanged. The inventory passes with 42
atoms, twelve families and tier counts 0/3/7/15/17. Complete canonical
statuses, inactive toric research candidate and native catalogue source
and PDF are byte-preserved. The native editor stays open without a
compile or tab change.

The release contains the full PDF, a 38-page review PDF and a source
archive with 647 members. Every member is verified against saved source
bytes and the CRC checked; all 425 active inputs are included. No fresh
isolated archive build is claimed. The manifest, closure and artifact
record pin this edition. GitHub synchronization explicitly fetches main
and work and publishes on the existing work branch and draft PR.

No original result, independent production model call, verifier receipt,
canonical solved status or general Siu/closure repair is added. Continue
with the acquired Fang Hessian v1 and its exact approximation, comparison
and second-order dependencies before further book admission.
