# Independent hostile audit: P03.1 perfected-unibranch curve envelope

Date: 30 August 2026

Auditor role: independent exact-byte mathematical and source audit.  The
auditor did not construct the candidate, did not edit either frozen TeX input,
did not edit the live book, and did not submit anything to Rethlas.

## Verdict

**PASS**, for the two exact frozen files identified below and only for their
stated one-dimensional conclusions.  The statement and proof are
dependency-closed, and every cited Gubler--Rabinoff implication used by the
argument has the correct direction and hypotheses.  No conclusion in
dimension at least two follows.  The result does not retire P03.1, whose
higher-dimensional classification remains open.

## Exact-byte gate

The audited bytes have the requested SHA-256 digests:

| file | independently recomputed SHA-256 |
|---|---|
| `p031_perfected_unibranch_curve_envelope_statement_20260830.tex` | `e30033eea96e7d59310a1e67402dc73dbdc1a9463b7ab14fc6f28e271ea0397f` |
| `p031_perfected_unibranch_curve_envelope_proof_20260830.tex` | `59535602b2f29c7c34bb4b4df79be1e2f72c0fa4fa61f1467b3e1c75723a1c71` |

The frozen primary source used in this audit is Walter Gubler and Joseph
Rabinoff, *Classically psh and pluriharmonic functions on Berkovich spaces*,
arXiv:2506.13548v2 (17 September 2025), packet file
`sources/Gubler_Rabinoff_2506.13548v2.pdf`, independently recomputed SHA-256
`83ca9a19394f44bb2e4e1aa316de95938f311acd53a00fe250fa0f605184b726`.
The PDF has 40 pages and its displayed title and authors agree with the source
ledger.  The arXiv-v2 TeX source in the local source freeze was also checked
against the cited numbered statements.

Any change to either TeX input invalidates this verdict and requires a new
audit.

## 1. The rig-smooth curve lemma

Write (s=\sup_i u_i) and (u=s^*).

### Values and upper semicontinuity

Local upper boundedness is uniform in the family: around every point there is
one finite upper bound for all (u_i).  Consequently (s), and hence its
upper-semicontinuous regularization (u), cannot take (+\infty).  By
definition (u) is upper semicontinuous and (s\leq u).  No countability or
sequential extraction is used.

For an open subset (W\subset C), neighborhood filters in (W) are cofinal
among neighborhoods in (C) after restriction, so

\[
                       u|_W=(s|_W)^*.
\]

This remains valid on non-first-countable Berkovich spaces when
regularization is written as the infimum, over neighborhoods, of the
corresponding suprema.  A connected component of
\(\operatorname{Int}(C)\) is open: analytic curves are locally connected.
Thus the proof applies this identity only to an open analytic subspace.

### Smooth boundaryless locus

A rig-smooth curve restricted to its interior is rig-smooth and
boundaryless.  An open connected component (W) of that interior is again
boundaryless and strict, hence smooth in the terminology of
Gubler--Rabinoff Section 2.13.  It is a connected smooth strict curve over a
nontrivially valued field, exactly the scope of Sections 3.3 and 3.4.1.

By classical-psh sheafiness/restriction, Section 4.1.2, and Section 3.4.1,
each (u_i|_W) is either Thuillier-subharmonic or identically
(-\infty).  This is the correct chain of implications; it does not assume
that the singular-curve definition is already Thuillier's definition.

### Thuillier comparison

Let (D\subset W) be any strict affinoid domain and let (q) be harmonic on
(D), with (u\leq q) on \(\partial D\).  Since
(u_i\leq s\leq u), the same boundary inequality holds for every (u_i).
Thuillier's defining comparison property therefore gives (u_i\leq q) on
(D), including the tautological identically-(-\infty) case.  Taking the
pointwise supremum gives (s\leq q) on (D).

The proof then regularizes only at points of the topological interior of
(D).  This is legitimate.  Gubler--Rabinoff Section 2.11(3) identifies
(\operatorname{Int}(D/W)) with the topological interior of (D) in (W).
Section 2.11(4) is an equality here because (W\to\mathcal M(K)) is locally
separated; since (W) is boundaryless, it identifies
(D\setminus\partial D) with that same topological interior.  At such a
point a neighborhood may be chosen inside (D), and continuity of (q)
gives

\[
                    u(x)=\limsup_{y\to x}s(y)\leq q(x).
\]

At (x\in\partial D), the required inequality is the assumed boundary
inequality itself.  Hence (u|_W) satisfies Thuillier's comparison property.
If it is not identically (-\infty), this proves Thuillier subharmonicity; if
it is identically (-\infty), it is subharmonic in the extended
Gubler--Rabinoff sense.  Thus (u) is subharmonic on every component of
(\operatorname{Int}(C)).

### Relative boundary of (C)

Proposition 3.5(3) states exactly that an upper-semicontinuous function on an
analytic curve which is subharmonic on \(\operatorname{Int}(C)\) is
subharmonic on all of (C).  The candidate has already established its two
hypotheses.  The proposition therefore retains every relative-boundary
point; no barrier or continuity assertion at those points is silently
assumed.  Section 4.1.2 then identifies subharmonicity with classical
plurisubharmonicity on the curve.  The first lemma is correct.

## 2. Perfecting, reduction, and normalization

Put (v=\sup_i\varphi_i) and (u=v^*).  Local upper boundedness makes (u)
(\mathbf R\cup\{-\infty\})-valued and upper semicontinuous.

### Topological identity for regularization

For a homeomorphism (q:Y\to X), the two neighborhood filters correspond,
so for every locally upper-bounded (a),

\[
                         a^*\circ q=(a\circ q)^*.
\]

Pointwise supremum also commutes with composition.  These are purely
topological identities and are valid for arbitrary index sets.

In characteristic (p>0), Gubler--Rabinoff Lemma 3.7 says exactly that the
projection from scalar extension to the completion of the perfect closure
is a homeomorphism, and that it preserves the boundary.  In characteristic
zero the candidate makes this map the identity.  The base-changed space is
still strict.

Lemma 3.8 says exactly that the reduction inclusion of a strict analytic
space is a homeomorphism and preserves the boundary.  Thus
(Z=(U^\dagger)_{\mathrm{red}}) has the same underlying Berkovich space as
(U^\dagger).

Lemma 3.9(4) says that normalization of a reduced strict analytic curve is a
topological quotient.  Under the candidate's explicit hypothesis that the
normalization is bijective on Berkovich points, a bijective quotient map is
a homeomorphism.  Therefore the composite

\[
 \widetilde Z\xrightarrow{\nu}Z\xrightarrow{\iota}U^\dagger
                 \xrightarrow{\pi}U
\]

is a homeomorphism.  Applying the preceding identity gives the displayed
upstairs-envelope equality in the proof.  The family remains locally
bounded above upstairs because this composite is a homeomorphism.

### Plurisubharmonicity upstairs

The field (k^\dagger) is perfect.  The space (Z) is a reduced strict
analytic curve, so Lemma 3.9(1) gives that its normalization
(\widetilde Z) is rig-smooth.  It is separated and strict as well (the
normalization is finite over the separated strict curve (Z)).

Proposition 4.2(5), in its forward direction, carries every
(\varphi_i) to a classically psh function on (U^\dagger).
Proposition 4.2(6), in its forward pullback direction, carries it through
(\iota) and (\nu).  Hence all functions in the upstairs supremum are
classically psh.  The already-proved rig-smooth curve lemma applies and makes
the regularized upstairs supremum classically psh.

### Descent

The normalization (\nu) is finite and surjective.  The reduction inclusion
(\iota) is a finite closed immersion and is surjective on underlying
points.  Proposition 4.2(6), in its converse finite-surjective direction,
therefore descends classical psh-ness first from (\widetilde Z) to (Z)
and then from (Z) to the possibly nonreduced (U^\dagger).  Its target
function is upper semicontinuous because it is (u\circ\pi), and
(\pi) is a homeomorphism in the only nonidentity case.

Finally Proposition 4.2(5), now in its converse direction, descends from
(U^\dagger) to (U).  No unsupported descent directly through an infinite
extension, and no descent of Fubini--Study presentations, is used.

## 3. Corollary and obstacle family

Every locally Fubini--Study function is locally a positive multiple of a
finite maximum of logarithms of analytic functions, up to constants.
Proposition 4.2(1)--(3) therefore makes it classically psh.  A semipositive
real-PL function on this good strict analytic curve is classically psh by
Theorem 4.3.  Thus every competitor in \(\mathcal A_f\) is in the family
class covered by the theorem.

An upper-semicontinuous (f:U\to\mathbf R\cup\{-\infty\}) is locally
bounded above because it never takes (+\infty).  Since every competitor is
bounded by (f), the family is locally bounded above uniformly.  The empty
family is handled separately and yields the classically psh constant
(-\infty).  The nonempty family is covered by the theorem.  This proves
the corollary, including relative-boundary points.

## 4. Scope and adversarial counterchecks

1. The nodal counterexample in the live book is not contradicted: the
   normalization has two points above the node, so it is not bijective.
2. Over a perfect field, normality is a sufficient special case because the
   reduced normal curve is its own normalization.  The broader hypothesis is
   not normality but the explicit one-point normalization-fibre condition.
3. Over an imperfect positive-characteristic field, ordinary normality of
   (U) alone is not asserted to survive completed perfecting and reduction;
   the statement correctly retains the explicit post-perfecting
   normalization-bijectivity hypothesis.
4. The phrase "analytically unibranch" is explicitly qualified by the
   normalization-fibre condition used in the proof.  The proof needs no
   stronger normality assertion and no algebraic identification beyond that
   condition.
5. No step proves or uses a result in dimension at least two.  In higher
   dimension the restriction of ambient usc regularization to a curve need
   not equal the curvewise regularization, so this proof cannot be promoted
   by curve testing.
6. No CLD-v2 psh conclusion and no continuity conclusion is claimed.
7. No global trivially valued Boucksom--Jonsson envelope theorem is used.
8. No maximum, coefficient-group, Choquet, or metrizability shortcut enters
   the proof.

## 5. Nonblocking integration notes

For maximum pedagogical explicitness, a live-book integration may add the
standard sentence that connected components of analytic curves are open,
and hence that the chosen component (W\subset\operatorname{Int}(C)) is an
open smooth boundaryless curve.  It may also spell out that a bijective
quotient map is a homeomorphism.  Both facts are already correctly used and
are not mathematical gaps in the frozen proof.  Any such editorial edit,
however, changes the audited bytes and must be independently reverified.

Subject to exact-byte production Rethlas verification, the candidate is
mathematically suitable for integration as a verified one-dimensional
partial solution.  P03.1 itself must remain active.
