# Independent exact-byte hostile audit

Date: 30 August 2026

## Frozen objects

This audit read, but did not modify, the following frozen objects.

| object | SHA-256 |
|---|---|
| `p213_polycylinder_bt_independence_statement_20260830.tex` | `e8676ccb90803a54909c20a558b9b09311d4eda2a043d99b69198cd5b0c8b995` |
| `p213_polycylinder_bt_independence_proof_20260830.tex` | `2fc7ac62864af54ee8f0cfc9d415ba173ec3f973126aaef728498d71bc3c1006` |
| `p213_polycylinder_bt_independence_compile_20260830.pdf` | `4b42b9b3ff2ba0fa9bb6d12ae094d6656f7825c19d34cf14b3762e87c8b2e30b` |

No production verifier was called, and no live-book file was modified.

## Verdict

**FAIL-CLOSED: the exact frozen statement/proof pair is not promotable.**

The abstract basis proposition, the global basis branch of the corollary,
and the final fixed-polycylinder identity survive the checks below.  The
middle local assertion in statement lines 50--52 does not: under the natural
meaning of "the same conclusion", its hypothesis supplies only an open cover
by polycylinders, whereas Bedford--Taylor independence quantifies over every
open subdomain.  The proof never supplies the missing basis refinement.

There is also an ambient-hypothesis/source-closure defect: the frozen abstract
statement assumes only that the analytic space is good, while the cited CLD
order-zero multiplication results require local differential separation and
the book's current/Bedford--Taylor framework is stated for topologically
separated, pure spaces (and its Chapter 16 standing scope is boundaryless).
The formal argument is valid once that current calculus is available, but the
frozen bytes do not state or discharge the required ambient scope.

## Critical finding C1: cover is not a basis

Statement lines 13--27 define the conclusion as continuous-pair
Bedford--Taylor independence and explicitly quantify over **every** open
`W` and every equal-curvature pair on `W`.  This matches both
`ch16_bedford_taylor.tex:1339--1354` and CLD Definition 8.6.2
(`CLD25.txt:10345--10347`), where the predicate quantifies over every open
set.

The middle corollary clause at statement lines 50--52 says that "the same
conclusion" holds on an open set `W` if every point merely has *a*
neighbourhood in `W` isomorphic to a displayed polycylinder.  Let such
neighbourhoods be `Q_x`.  To prove the Bedford--Taylor predicate for a current
on `W`, one must start with an arbitrary open `V` contained in `W` and an
arbitrary point `x` in `V`, then find a P06.2 domain contained in `V`.  The
hypothesis gives only `x in Q_x subset W`; it does not give `Q_x subset V`.
The intersection `Q_x cap V` need not be a standard polycylinder.

Consequently proof lines 44--46 cannot deduce the middle local assertion from
the abstract proposition.  Nor can one invoke locality of Bedford--Taylor
currents: to use that locality on the cover `(Q_x)`, one would first need to
know that each restricted current is Bedford--Taylor on **all** opens of
`Q_x`.  P06.2 v3 gives zero-current regularity only when the pair is defined
on the entire standard polycylinder, so using locality here would be circular.

This is exactly the deleted-branch firewall.  An arbitrary neighbourhood of
a type-II point inside a standard disc can omit a tangent branch and need not
contain a smaller neighbourhood of that point analytically isomorphic to a
standard disc or annulus.  Thus "polycylinder atlas/open cover" cannot be
silently upgraded to "ordinary topological basis of polycylinders".

The dossier's own `SCOPE_FIREWALL.md:12--16` and
`HOSTILE_SELF_AUDIT.md:53--57,66--71` correctly warn that a single standard
polycylinder proves only a fixed-domain identity, not the full predicate on
all its ordinary opens.  Those warnings expose rather than repair the middle
clause.

If "the same conclusion" was intended to mean only the fixed-domain identity
for a current and a pair defined on all of `W`, that weaker claim is proved by
covering `W` with the `Q_x`; however, those quantifiers are not what the frozen
text says.  Exact-byte auditing cannot resolve the ambiguity in favour of the
weaker statement.

### Minimal repair boundary

Either of the following would close C1, but neither is present in the frozen
bytes.

1. Replace the middle hypothesis by: the displayed polycylinder opens form a
   basis for the ordinary topology of `W`.  Then the abstract proposition
   applies and the full predicate follows.
2. Keep the neighbourhood-cover hypothesis, but explicitly assert only this
   fixed-domain result: for each positive closed current `T` on `W` and each
   continuous equal-curvature pair `u,v` defined on all of `W`, the two
   currents agree on `W`.

## Major finding M1: ambient current-calculus scope is not closed

The abstract proposition begins with a pure good `K`-analytic space
(statement line 4), with no topological separatedness or boundary condition.
The cited source chain is narrower:

- CLD Proposition 7.2.9, which gives order zero for positive currents, assumes
  a locally differentially separated tropical space
  (`CLD25.txt:8003--8006`).
- CLD Example 7.2.12, which defines multiplication by a locally bounded Borel
  function, has the same hypothesis (`CLD25.txt:8050--8064`).
- CLD Section 8.5 is introduced under the standing assumption that the
  tropical space has no boundary (`CLD25.txt:10243--10249`).
- The analytic route to local differential separation in CLD passes through
  local holomorphic separation; CLD explicitly assumes topological
  separatedness before deducing it for good analytic spaces
  (`CLD25.txt:21559--21565,21581--21583`).
- The live book defines the canonical tropical/current setting for
  topologically separated pure analytic spaces
  (`ch13_forms.tex:1543ff`, `ch14_currents.tex:12ff`) and Chapter 16's standing
  hypotheses add boundarylessness (`ch16_bedford_taylor.tex:109--136`).

Thus the source matrix does not justify the stated ambient generality.  The
algebraic Leibniz computation is local and may admit a broader theorem, but a
broader theorem would require an explicit construction/proof of the relevant
order-zero multiplier and current sheaf calculus in that category.  A safe
repair is to add the book's topologically separated, pure, boundaryless scope
(or to state local differential separation plus precisely the current
calculus being assumed).  This source-scope defect is independent of C1.

## Checks that pass, conditional on the ambient current calculus

### 1. Arbitrary open set in the abstract basis proposition

This quantifier is handled correctly.  For arbitrary open `W` and `x in W`,
a genuine topological basis gives `Q` with `x in Q subset W` (proof lines
16--17).  Restriction preserves the zero-current equation.  The stipulated
regularity of `Q` then makes `h=u-v` smooth with zero smooth Hessian, and the
local current identity glues on `W`.

### 2. Multiplication, linearity, and bidegrees

A positive current is symmetric and of order zero in the locally
differentially separated CLD setting.  Hence multiplication by continuous
`u`, `v`, and `h=u-v` is defined; no positivity of the multiplier is needed,
and `hT=uT-vT` by linearity.  Multiplication preserves the current's
bidegree.  Applying `d'd''` raises bidegree `(ell,ell)` to
`(ell+1,ell+1)`, so `0 <= ell <= n-1` is the correct non-vacuous range.

### 3. Smooth Leibniz identity

For a smooth function `h` and a symmetric current `T` with
`d'T=d''T=0`, the current Leibniz formula gives

```text
d'd''(hT) = d'd''h wedge T.
```

The cross terms vanish by closedness; symmetry accounts for the standard CLD
sign cancellation.  This is CLD Lemma 8.5.3 and its smooth-function
specialization in Section 8.5.4 (`CLD25.txt:10273--10301`), reproduced in the
book as `lem:ch16-leibniz-closed` and `cor:ch16-smooth-case`
(`ch16_bedford_taylor.tex:1142--1213`).  The frozen proof uses exactly this
scope.  Requiring both differentials to vanish is more than sufficient.

### 4. Passage from P06.2 v3 to ordinary smooth zero Hessian

The dependency is exact.  P06.2 v3 states on a standard strict open
polycylinder over a complete nontrivially valued field that

```text
h = c + sum_j lambda_j log|S_j|.
```

See its statement lines 44--75.  Each `S_j` is an analytic unit, so
`-log|S_j|` is a tropical coordinate and the displayed function is an affine
function of ordinary CLD-smooth moment coordinates.  Its ordinary smooth
Hessian is therefore zero.  The P06.2 proof states this explicitly at lines
394--396.  No inference from equality of a smooth current to equality of a
smooth form is being made.

Frozen P06.2 dependency hashes:

| object | SHA-256 |
|---|---|
| v3 statement | `985be85d97b583f72be5cee65988df6f31c1edb49a685121b834df179fa87fda` |
| v3 proof | `42b592bf8ac26ed46c36928e5e90272225ae6883bd2bfe62d3ff2840f01d46e5` |
| v3 production response (`verdict: correct`) | `c8c951075a574c6a3badde2e2a22942718616cd21da0144cb8a983bc3cac822f` |

### 5. Global basis and fixed-domain branches

The global corollary hypothesis at statement lines 30--48 really is a basis,
so it feeds the abstract proposition and passes the arbitrary-open firewall.
The final assertion at lines 52--56 is also sound as a fixed-domain statement:
for `u,v` defined on all of the standard polycylinder `P`, P06.2 applies
directly to `u-v`, and the smooth Leibniz computation proves the identity on
`P`.  It does not imply the full Bedford--Taylor predicate for every open
subset of `P`, as proof lines 48--49 correctly acknowledge.

## Disposition

- exact frozen pair: **FAIL-CLOSED / NOT READY FOR PRODUCTION**;
- critical mathematical/quantifier defect: C1;
- independent source-scope defect: M1;
- production calls made by this audit: none;
- frozen statement/proof edits made by this audit: none;
- live-book edits made by this audit: none.
