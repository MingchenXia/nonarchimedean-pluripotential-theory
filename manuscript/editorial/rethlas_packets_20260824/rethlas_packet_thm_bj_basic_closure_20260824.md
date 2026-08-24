# Exact-current Rethlas intake packet: `thm:bj-basic-closure`

**Packet date:** 2026-08-24 (Asia/Shanghai)  
**Target:** `manuscript/parts/part4/ch34_fs_pl_psh.tex`,
`thm:bj-basic-closure`  
**Packet purpose:** exact-current provenance and source-scope verification  
**Current classification:** **PRIMARY-SOURCE IMPORT / EDITORIAL
CONSOLIDATION; NOT NEW MATHEMATICS**  
**Rethlas status:** **NO EXACT-CURRENT RECEIPT. THIS PACKET IS AN INTAKE
PACKET, NOT A RECEIPT.**

The target is a single convenient theorem package assembled from explicitly
cited results of Boucksom--Jonsson (`BJ22`).  Each mathematical clause is a
direct source statement, a source-stated immediate consequence, or a local
unfolding of the source definition.  Combining those clauses under one book
label is a presentational aggregation.  It is not a new theorem and does not
claim a new mathematical synthesis.

The applicable Rethlas protocol reserves full new-result verification for
new mathematics.  The proper verdict here is therefore a source/provenance
verdict such as `SOURCE-ALIGNED IMPORT` or `SOURCE-MISMATCH`, not a novelty
verdict.  The absence of a receipt is a gate against uncited extensions; it
is not evidence against the cited primary-source statements.

## 1. Hard source firewall

arXiv:1710.09731 is excluded completely.  It is not an allowed input, is not
cited as support, and no argument or dependency in this packet is traced
through it.  A verifier must reject any proposed route that introduces it,
even indirectly.

The sole mathematical publication audited for the imported closure package
is:

- S. Boucksom and M. Jonsson, *Global pluripotential theory over a trivially
  valued field*, Ann. Fac. Sci. Toulouse Math. (6) 31 (2022), no. 3,
  647--836, DOI `10.5802/afst.1705` (`BJ22`).

The later addendum `BJ22b` is mentioned in Chapter 34 only to delimit the
later envelope results.  It is not a source for any clause of
`thm:bj-basic-closure`.

## 2. Exact-current file manifest

SHA-256 values are lowercase hexadecimal hashes of the exact bytes on disk.
The chapter hash is the controlling identity for this packet.

| File | Role | Bytes | SHA-256 |
|---|---:|---:|---|
| `manuscript/parts/part4/ch34_fs_pl_psh.tex` | live audited chapter | 128890 | `84c106ae9c8091b6c09cac534d27ee50d2228f05484bc2152979f690ea67ecd0` |
| `ch34_standing_hypotheses_exact.tex` | exact chapter lines 116--148 | 1716 | `92277d4b31ba20064c96805112a8630d35d24fa24bdf79869559c25006b18b9e` |
| `ch34_bj_psh_definition_scope_exact.tex` | exact chapter lines 2302--2401 | 4800 | `f06a355e54b8804f8425227ef44176b6d0ecd1b176d0978c1c5aec6b6b3e0378` |
| `ch34_thm_bj_basic_closure_context_exact.tex` | exact chapter lines 2449--2600 | 7882 | `8485b59af90c9bc95762f2d1743056ae702ca30557a76d5715682e5df78aea0a` |
| `ch34_bj_closure_source_note_exact.tex` | exact chapter lines 2806--2830 | 1309 | `64961007ef921cb21140f25b0a7c0d1015d25e931133dc8c2ef8091b45927ba1` |

Each extracted TeX file was compared byte-for-byte with the stated contiguous
line slice of the live chapter and matched exactly.  Line numbers are only
navigation aids; the hashes, labels, and exact file contents are the durable
identifiers.

For source reproducibility, the local source artifacts used in the audit
were:

| Source artifact | SHA-256 |
|---|---|
| `tmp/pdfs/bj22_global_trivial.pdf` | `8d5975337f4ac88a475929ea6a436ec4a15d08715d5582bc0ba0eb3e07152c52` |
| `tmp/pdfs/bj22_global_trivial.txt` | `af5a9b9d62570a37d9ad11d139e99353e8b50f1f1c55557fbfcf2cb37cca0c8f` |

The PDF is the source artifact; the text file is a search aid and must not
override the PDF if extraction has damaged notation.

## 3. What the exact extracts contain

1. `ch34_standing_hypotheses_exact.tex` fixes the field, variety, numerical
   class, reducible-component, and valuation-locus conventions.
2. `ch34_bj_psh_definition_scope_exact.tex` contains the full Chapter 34
   definition of `PSH`, the net/varying-class/componentwise-finiteness
   warnings, and the complete local proof separating pseudoeffective
   nonemptiness from nef boundedness.
3. `ch34_thm_bj_basic_closure_context_exact.tex` is the full target block. It
   contains the preceding primary-source/Rethlas warning, the complete seven
   clause statement, the complete adjacent proof, and the immediately
   following warning excluding increasing-family/supremum closure.
4. `ch34_bj_closure_source_note_exact.tex` is the complete end-of-chapter
   source boundary.  It distinguishes the closure package from the later
   regularization theorem and envelope addendum.

No normalization, paraphrase, line-number annotation, or header was inserted
into an exact TeX extract.

## 4. Natural framework of the target

The target must be evaluated under all of the following hypotheses and no
hidden strengthening.

- `k` is algebraically closed and trivially valued.  No characteristic
  hypothesis is imposed.
- `X` is a reduced projective `k`-variety and may be reducible.  Its
  irreducible components form a finite family.  Normality and integrality are
  **not** hypotheses of this theorem.
- `theta, theta'` are arbitrary elements of the real Neron--Severi space
  `N^1(X)`.  Pseudoeffectivity is forced only when a relevant PSH class is
  nonempty.  Nefness is forced only by the existence of a bounded PSH
  function and is not assumed here.
- A `theta`-psh function is upper semicontinuous, not identically `-infinity`
  on any irreducible component, and the pointwise limit of a decreasing
  **net** of generically finite real-weight Fubini--Study functions whose
  numerical classes converge to `theta`.
- Functions take values in `R union {-infinity}`.  They never take
  `+infinity`.  Positive scalar multiplication and addition are therefore
  defined, while `0 times (-infinity)` is deliberately not formed.
- `X^div` includes the componentwise trivial valuations and positive rational
  multiples of prime-divisor valuations over the components.  `X^lin` is the
  larger linear-growth locus.
- In the pullback clause, `Y` is another projective variety in the same
  convention.  Pullback may become identically `-infinity` on a component of
  `Y`; the theorem states that alternative rather than suppressing it.

These are exactly the hypotheses in the extracted standing-hypothesis and
definition blocks.

## 5. Every imported `BJ22` result and its exact scope

The preliminary warning names eight source results.  Their exact mathematical
scopes, including clauses not used by the target, are as follows.

### `BJ22`, Definition 4.1

For any `theta in N^1(X)`, `PSH(theta)` consists of the generically finite
upper-semicontinuous functions on `X^an` that are pointwise decreasing limits
of a net

`phi_i in H_R^gf(L_i)`, with `L_i in Pic(X)_Q` and
`c_1(L_i) -> theta`.

It also records the immediate cone restrictions: nonemptiness implies
pseudoeffectivity; existence of a bounded member implies nefness; and a
continuous limit is uniform by Dini.  Chapter 34 imports the definition and
the first two scope restrictions, not a fixed-class or sequential
approximation claim.

### `BJ22`, Theorem 4.5

It proves both defining closure requirements:

- `(PSH1)` every generically finite real-weight FS function in a rational line
  bundle `L` belongs to `PSH(c_1(L))`;
- `(PSH2)` if `phi_j in PSH(theta_j)` is a decreasing net,
  `theta_j -> theta`, and the pointwise limit `phi` is generically finite,
  then `phi in PSH(theta)`.

The source explicitly lists two consequences: for a fixed function `phi`,
the set of classes `theta` for which `phi in PSH(theta)` is closed; and
`PSH(theta)` is closed under decreasing nets whose limit is generically
finite.  These are target clauses (5) and (4), respectively.

### `BJ22`, Lemma 4.6

This is the abstract diagonal-net lemma behind Theorem 4.5.  Its data are a
compact topological space `K`; a set `S`; for each `s in S`, a family `F_s`
of continuous extended-real functions stable under addition of constants;
and a map `rho:S -> T` to a metrizable space.  If an upper-semicontinuous
function is first obtained as a decreasing limit in the one-level closures
with parameters tending to `t`, the lemma flattens the nested approximations
to a single decreasing net of members of the original `F_s`, with
`rho(s) -> t` and the same pointwise limit.

Chapter 34 applies it with `K=X^an`, `S=Pic(X)_Q`,
`F_L=H_R^gf(L)`, `T=N^1(X)`, and `rho=c_1`.  Compactness supplies the
directedness of the triples used in the diagonal.  The source does not allow
one simply to order a disjoint union of inner index sets.

### `BJ22`, Theorem 4.7

For arbitrary `theta, theta' in N^1(X)` and every `t>0`, the theorem states:

1. `PSH(theta)+PSH(theta')` is contained in
   `PSH(theta+theta')`, and `PSH(t theta)=t PSH(theta)`, where the latter
   `t` is ordinary positive multiplication of function values.
2. `PSH(theta)` is convex and stable under uniform limits, finite maxima,
   addition of real constants, and the positive-real scaling **action** on
   the analytification, `phi -> (t dot phi)` with
   `(t dot phi)(v)=t phi(t^{-1}v)`.  This action is distinct from ordinary
   multiplication in (1).
3. For every morphism `f:Y->X` and `phi in PSH(X,theta)`, either
   `f^*phi in PSH(Y,f^*theta)` or the pullback is identically `-infinity` on
   an irreducible component of `Y^an`.
4. Restriction of `phi` to each irreducible component `X_alpha` belongs to
   `PSH(X_alpha,theta|X_alpha)`.

Target clauses (1)--(3) import ordinary addition of constants and finite
maxima from (2), and sums and ordinary positive multiplication from (1).
Target clause (6) imports (3)--(4).  The target does not separately state
uniform closure or stability under the analytification scaling action.  The
zero-coefficient sentence is an extended-real safety convention: ordinary
multiplication in (1) is restricted to `t>0`, and an endpoint term with zero
coefficient is omitted.  It is not a new zero-multiplication theorem.

### `BJ22`, Lemma 4.9

For `phi, phi' in PSH(theta)`, it supplies a single net of rational line
bundles `L_i` and simultaneous approximants
`phi_i, phi'_i in H_R^gf(L_i)` such that both functions decrease to their
targets and `c_1(L_i)->theta`.  Its scope is two functions in the **same**
class.  Chapter 34 uses exactly this lemma to take their same-class maximum;
it does not assert a cross-class maximum construction.

### `BJ22`, Corollary 4.17

For every numerical class `theta` and every `phi in PSH(theta)`, `phi` is
finite on `X^lin`.  Since `X^div` is contained in `X^lin`, target clause (7)
also obtains divisorial finiteness.  No boundedness on all of `X^an` is
asserted.

### `BJ22`, Theorem 4.22

For `phi in PSH(theta)` and an **arbitrary upper-semicontinuous**
`psi:X^an -> R union {-infinity}`, one has

`phi <= psi on X^div` if and only if `phi <= psi on X^an`.

Equivalently, `phi` is the smallest upper-semicontinuous extension of its
divisorial restriction.  Target clause (7) imports the equivalence with the
same upper-semicontinuity hypothesis on the comparator.

### `BJ22`, Corollary 4.23

Every `theta`-psh function is uniquely determined by its restriction to
`X^div`, and the topology of pointwise convergence on `X^div` is Hausdorff.
Target clause (7) imports divisorial determination.  It does not import the
Hausdorff-topology assertion into this theorem.

## 6. Clause-by-clause provenance ledger

| Target text | Source status | Exact source boundary |
|---|---|---|
| Preamble: arbitrary classes; psef nonemptiness versus nef boundedness | direct scope fence | `BJ22` Definition 4.1, displayed consequences (4.1)--(4.3); locally proved as `lem:ch34-psh-nonempty` |
| (1) addition of constants | direct import and local definition unfolding | Theorem 4.7(ii) |
| (2) same-class maximum | direct import; same-class approximation made explicit | Theorem 4.7(ii), Lemma 4.9 |
| (3) sums and strictly positive ordinary scalar multiplication | direct import; source proof locally expanded | Theorem 4.7(i), Theorem 4.5 for the real-scalar limit, and Theorem 4.7(ii) only for restoration of a constant |
| (3) zero endpoint means omission | notation/safety fence only | source ordinary scalar identity is stated for strictly positive scalars |
| (4) fixed-class decreasing net | source-stated consequence `(PSH2b)` | Theorem 4.5 |
| (5) varying-class decreasing net | direct import `(PSH2)` | Theorem 4.5, with Lemma 4.6 |
| (5) closed locus of classes for a fixed function | source-stated consequence `(PSH2a)` | Theorem 4.5 |
| (6) pullback alternative and component restriction | direct import | Theorem 4.7(iii)--(iv) |
| (7) finiteness on `X^lin` | direct import | Corollary 4.17 |
| (7) divisorial comparison against usc `eta` | direct import | Theorem 4.22 |
| (7) divisorial determination | direct import | Corollary 4.23 |
| Following warning: no increasing/supremum closure | explicit non-claim | outside this closure package; no Section 5 envelope result is used |

The only local infrastructure invoked in the adjacent proof is already
proved earlier in the hashed chapter:

- `lem:gf-fs-operations`: sums across classes, same-class maxima, constants,
  and qualified pullback for generically finite FS presentations;
- `prop:ch34-fs-operations`, item `itm:ch34-ops:rational`: positive rational
  rescaling of a rational line bundle and its FS presentation;
- the weighted section formula `eq:gf-fs-presentation`.

Those local steps unpack finite maxima, products of sections, weights, and
pullback presentations.  They do not introduce an additional global
pluripotential theorem.

## 7. Source boundary: results deliberately outside the target

- `BJ22`, Theorem 4.15(i)--(iii), cited in the extracted source note, belongs
  to the **next** Chapter 34 theorem on FS regularization.  It is not an
  input to any clause of `thm:bj-basic-closure`, except that its absence is
  immaterial because Definition 4.1 already supplies GF approximation.
- `BJ22b` concerns later envelope and regularized-envelope energy results.
  It is not used to prove the target.
- No increasing-family closure, arbitrary bounded-supremum closure, envelope
  property, compactness of normalized PSH spaces, sequential regularization,
  or countable cofinality may be inferred from the target.
- No integrality, normality, unibranchness, resolution, or characteristic
  zero hypothesis is needed for the seven imported clauses.

## 8. Adversarial checks required from Rethlas

A source-alignment response should explicitly check all of the following.

1. **Componentwise generic finiteness.** Verify every limit and pullback
   alternative on reducible `X` and `Y`; finiteness on one component cannot
   repair `-infinity` on another.
2. **Net topology.** Verify that clauses (4)--(5) use nets, and that the
   Lemma 4.6 compactness argument really gives a directed diagonal.  Do not
   replace it by a sequence or an unordered union of inner nets.
3. **Varying classes.** Check `theta_j->theta` in the finite-dimensional
   real Neron--Severi topology, with no fixed-class or nef hypothesis smuggled
   in.
4. **Real scalar direction.** After normalizing `phi<=0`, rational
   `a_m` must increase to `a`, so `a_m phi` decreases.  Confirm the class
   convergence and restoration of the finite constant.
5. **Extended-real endpoints.** Only positive scalar multiplication is used;
   a zero coefficient omits a summand.  Sums of two values in
   `R union {-infinity}` are defined because `+infinity` never occurs.
6. **Same-class maximum.** Confirm Lemma 4.9 places both approximants in the
   same `L_i`; do not substitute a nonexistent cross-class maximum rule.
7. **Pullback collapse.** Check why generically finite `f^*phi` forces every
   approximating pullback to be generically finite, and retain the component
   collapse alternative otherwise.
8. **Divisorial comparison.** Retain the upper-semicontinuity hypothesis on
   `eta` and the exact `X^div` convention.  Do not promote determination to
   arbitrary non-usc comparators.
9. **Cone scope.** Test a merely pseudoeffective non-nef class: the theorem
   may contain unbounded/polar PSH functions and makes no bounded-existence
   assertion.  For a non-pseudoeffective class, relevant membership clauses
   are vacuous.
10. **Supremum firewall.** Confirm that no proof step uses increasing closure,
    a regularized supremum, or an envelope theorem.
11. **Forbidden-source audit.** Confirm that the excluded arXiv source and all
    dependencies traceable only through it are absent.

## 9. Requested verifier output

Return five separate blocks.

1. `HASH CHECK`: reproduce the chapter and extract hashes and report whether
   they match.
2. `SOURCE SCOPE CHECK`: for each of the eight `BJ22` entries above, compare
   the exact source statement with the scope ledger.
3. `LOCAL PROOF CHECK`: audit the adjacent Chapter 34 proof, especially the
   diagonal-net and positive-real-scalar steps.
4. `ADVERSARIAL CHECK`: address every item in Section 8 and provide a concrete
   counterexample to any overstatement found.
5. `CLASSIFICATION`: return exactly one of
   `SOURCE-ALIGNED IMPORT` or `SOURCE-MISMATCH`, followed by exactly one of
   `NO NEW MATHEMATICAL SYNTHESIS` or `UNSUPPORTED NEW SYNTHESIS`.

If the result is source-aligned, the response should state that this verifies
provenance of an imported theorem package.  It must not reclassify the target
as newly machine-verified mathematics.  If a mismatch exists, identify the
smallest exact clause and source hypothesis that fail; do not broaden the
failure to unaffected clauses.

## 10. Current audit assessment and residual gates

**Current human/source audit assessment:** `SOURCE-ALIGNED IMPORT / NO NEW
MATHEMATICAL SYNTHESIS`.

No unsupported clause was found in the repaired theorem.  In particular,
the closed class locus is already source consequence `(PSH2a)`, the
fixed-class decreasing closure is `(PSH2b)`, and the zero-coefficient text is
only a domain-of-definition guard.

The residual provenance gates are:

1. no exact-current Rethlas response is attached to the hashes in this
   packet;
2. any later edit of Chapter 34 invalidates the chapter hash and requires new
   extracts and a new receipt;
3. a verifier must use the exact `BJ22` edition/theorem numbering anchored by
   the source hash above and must treat the PDF, not OCR text, as decisive;
4. no clause may be extended to increasing limits, arbitrary suprema,
   non-usc comparison functions, zero scalar multiplication, sequential
   approximation, or bounded existence in merely pseudoeffective classes
   without a separate source proof or a separately hashed Rethlas packet.

Until those gates are discharged, the existing in-chapter warning is the
correct final status.
