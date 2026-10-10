# Fixed divisor traces and the relative canonical reduction

**Known argument import and direct reduction.** The controlling baseline
is `62e8ffa40873139f19c0102466040592072c3abe`.
Chapter 46 explains the fixed-divisor step in Trusiani's
[arXiv:2605.30063v2](https://arxiv.org/abs/2605.30063v2), Lemma 4.3,
revised 17 August 2026 at 08:55:46 UTC. The exposition uses BFJ09
Proposition 3.3 and Theorem A from the published author-hosted offprint.
Chapter 68 distinguishes the fixed canonical trace from the relative
canonical error on varying resolutions. Appendix L.53 records the source
and admission boundary. No full special-Fujita, entropy-regularization
or YTD theorem is admitted.

## Exact argument and scope

Let Z be smooth complex projective of dimension N at least one, B a big
rational class, and q_m smooth projective birational models. The rational
classes P_m are nef, q_m^*B-P_m is effective, and P_m^N tends to vol(B).
An ample Cartier divisor A and one sufficiently small rational t>0 are
fixed before taking any approximant limit; both B+tA and B-tA are big.

The Morse inequality for the difference of two nef classes gives
vol(P_m-tq_m^*A) at least P_m^N-Nt(P_m^(N-1).q_m^*A).
The difference need not itself be nef or big. Effective domination and
birational invariance bound that volume above by vol(B-tA). In the
other direction, all higher terms in the nef binomial expansion are
nonnegative, so P_m^N+Nt(P_m^(N-1).q_m^*A) is at most
vol(P_m+tq_m^*A), hence at most vol(B+tA).

These two bounds squeeze the lower and upper limits of the fixed ample
trace between difference quotients of vol(B). First m tends to infinity
at fixed t; only then does t decrease to zero. BFJ09 Theorem A identifies
both limiting quotients with the same positive-product pairing. For a
fixed Cartier divisor D, choose a sufficiently large integer a so that
D+aA is ample and write D=(D+aA)-aA. Linearity gives convergence against D.
This limit does not assert that pairing with D preserves pseudo-effective
order for every individual approximant, and uses no scalar supremum
formula for an arbitrary effective D.

Taking D=K_Z, the canonical equality on smooth birational models splits
P_m^(N-1).K_{Z_m} into the fixed trace and P_m^(N-1).K_{Z_m/Z}.
The fixed trace converges by the preceding argument. Consequently
convergence of the full canonical intersection to the positive-product
pairing on Z is equivalent to vanishing of that relative canonical term.
The latter is nonnegative but still requires a separate discrepancy
estimate. Nonnegativity alone does not imply convergence to zero.
The argument does not identify a model entropy or supply its convergence.
If a proof uses a normal intermediate blowup without a known rational
Cartier canonical divisor, its canonical pullback requires a definition
or a justified projection argument with Weil cycles. The displayed
reduction assumes smooth models throughout and needs no such intermediate
pullback.

Section 46.3.7, equations (46.10k)–(46.10m), gives this argument.
Section 68.14 retains its separate energy, mixed-product, approximation
and entropy inputs. Section 46.3.8 still supplies only the preceding
fixed-ideal error argument and its explicitly conditional integral use.
The general trivially valued Siu/closure boundary retains its scope.

## Primary-source reading reused

The preceding [special-Fujita source review](special_Fujita_source_review_20261006.md)
read and displayed all 25 actual pages of Trusiani v2, including proof,
appendix and references. Lemma 4.3 is on actual 13 and its proof on 14.
The source PDF has SHA-256
`aa00afeb58947e0f839d5f1af752c83c429b407d387166b624cb3f6315589712`;
the full-reading record has SHA-256
`b9a1f7856f4d59afdc74be84a3bbff3dac1f7b0b7c4e1d4cada8f0c9d5e1976c`.

The published BFJ09 offprint, JAG 18 (2009), 279–308, has 30 actual
PDF pages and SHA-256
`49e7d188c06d66c6f860c46564da405b9ca7bb8e4234796513277b5ef0fd183c`.
Its eighteen selected pages, actual 1–3, 12–20 and 23–28, belong to the
preceding [big-class source review](big_class_stability_source_review_20261006.md).
Proposition 3.3 is on printed 295, actual 17; the volume derivative proof
is on printed 295–296, actual 17–18. The whole historical selected
dependency record has 58 pages and SHA-256
`15f1b76cea7ddedab5398fd6e4468767161330782644c4848e7b7870b3e3dc89`.
Its BFJ subset is the relevant dependency here. The exact source records
and files are reused; neither 25 nor 58 is counted as fresh primary reading.
No full reading of the five dependencies, or fresh full reading of the
external Lazarsfeld book cited for the algebraic Morse proof, is claimed.
The existing bibliography entries remain byte unchanged.

The invalid effective-divisor scalar supremum in Trusiani actual 7 and
Li–Fujita actual 6 is not used. The earlier analytic Rees normal-direction,
intermediate canonical-pullback and relative-ampleness diagnostics remain
separate from a certified complete repair. This integration gives no
counterexample to a corrected main theorem.

## Validation and matching PDF review

The final book has **4,386 pages**, 20,378,400 bytes and SHA-256
`1f47f8277bd457e60ce05baa4c40893cb79be0cc5659ff3071cf88117f6f34c3`.
This draft passes without layout repair. There are zero TeX errors,
package/pdfTeX warnings, missing characters, overfull boxes, unresolved
references/citations or rerun requests. The 954 nonfatal underfull
diagnostics match the baseline.

The post-render reference check finds 425 active inputs and 12,832
unique labels, with zero missing inputs, duplicate labels or dangling
references. There are 371 cited bibliography keys among 666 available
keys, and zero bibliography warnings. No new bibliography or index
key is added. All 764 index entries are accepted, with zero rejected
entries or warnings. Its 763 page groups and 419 distinct numeric
destinations are valid.

PDF navigation has 21,924 named destinations, 47,003 internal links,
171 external URL links, 2,558 contents entries and six parts. There are
no invalid internal links, named destinations or contents pages.
All **43 matching final PDF pages** were displayed and their extracted
text read, in 22 sheets: actual 47, 61, 68, 2741–2743, 3633–3637,
4148–4151 and 4359–4386. These include affected contents, the complete
trace calculation and its transitions, the stability comparison and
dated scope statement, the new provenance and following appendix
opening, and the complete index and bibliography. The final review
manifest has SHA-256
`0fc106129248bf3a1dce332b73affbe3661af4d62500317fd69166f85269787b`.
This scoped review is not a fresh rereading of every page of this edition;
the ordered whole-book second reading remains the completed 4 October
checkpoint.

## Preservation and publication

Only Chapters 46 and 68 and Appendix L change within the 425 active
inputs. All 422 other active inputs and 108 protected inputs retain
their baseline hashes. The edited files retain 101 existing statement
and explanatory environments and 40 proof environments, 141 blocks
in total, byte-for-byte. No formal result environment is added or
relabeled. Five new labels and three new equation tags are distinct.
README and the programme record the continuation.

All 55 prior frozen manifests, including four separate source-only
reviews, and all 109 prior exports retain their bytes. The other 5,023
tracked baseline files are unchanged. The canonical inventory passes
with 42 atoms, twelve families and tier counts 0/3/7/15/17. All complete
statuses, the open toric research candidate, and the native catalogue
source and PDF retain their bytes. Its editor remains open with no native
compilation or tab change claimed.

The release contains the full PDF, a 43-page review PDF and a source
archive with 635 members. Every archive member is checked against its
saved source bytes, its CRC is checked, and all 425 active inputs are
included. No fresh isolated archive compilation is claimed. The
integration manifest, closure hashes and artifact record make the
checkpoint reviewable. Cloud GitHub synchronization uses the existing
work branch and PR, explicitly fetches main and work, and makes no force
push or main-branch update.

This is an imported fixed-divisor argument and its direct canonical
reduction. No original result, independent production model call,
new verification receipt, solved canonical status or general Siu/closure
repair is claimed. Continue with projection, relative polarization,
support and further related primary-paper reading before any complete
regularization-theorem admission.
