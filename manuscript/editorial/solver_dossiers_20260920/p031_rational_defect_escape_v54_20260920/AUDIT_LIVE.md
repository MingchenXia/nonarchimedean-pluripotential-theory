# P03.1 rational-defect escape: live audit

Date: 2026-09-20

Baseline commit: `a67441e04d812cf0c44a63dda9540b54b7fd9982`

## Result under audit

The packet proves an exact topological characterization of a positive
complete rational globalization defect.  If a local rational LFS minorant
has positive gap at a point, then every lower positive superlevel of its
defect profile has a compact connected component that reaches the boundary
of every relatively compact test neighborhood.  Conversely, one local
competitor and positive level whose distinguished components escape every
admissible smaller neighborhood force the complete rational globalization
defect to be positive.

The result does not close P03.1.  It rules out isolated or locally trapped
positive defects and reduces the remaining vanishing problem to excluding
these escaping connected carriers in the unresolved higher-dimensional
normal or geometrically unibranch range.

## Proof ledger

1. The supremum of the nonempty global rational LFS family is lower
   semicontinuous, so the local defect profile is upper semicontinuous and
   its compact-domain superlevels are compact.
2. The auxiliary compact-component lemma is proved from compact Hausdorff
   separation and local compactness; no local connectedness or path
   connectedness is used.
3. If the component through the base point avoids the test boundary, the
   lemma produces a relatively compact collar whose boundary misses the
   chosen defect superlevel.
4. Strict pointwise inequalities on that compact collar boundary are
   witnessed by finitely many global rational minorants.  Closure under
   finite maxima produces one global comparator with subcritical boundary
   load.
5. The lower-bound half of
   `thm:p031-rational-collar-minimax` forces the same boundary load to be at
   least the point defect, giving the contradiction.
6. The converse uses only the defining domination of the local envelope.
   In the boundaryless case the existing three-level ledger propagates the
   characterization to the rational, LFS, and PL defects and both branch
   gaps.

## Hostile checks

- The case `F \ O = empty` in the collar lemma is handled separately.
- The clopen step is justified inside the clopen neighborhood `N`; the two
  pieces are complementary open subsets there.
- Nonemptiness of the collar boundary follows from connectedness of `X`,
  properness of the collar, and the nonempty boundary of the test domain.
- Compactness is used exactly where finite extraction is required.
- The proof asserts connected carriers only; it makes no path-connectedness
  claim.
- No normality or geometrically unibranch hypothesis is smuggled into the
  new theorem, and no resolution of the remaining P03.1 range is claimed.

## Mechanical verdict

- Local strict writing audit on `STATEMENT_LIVE.tex` and `PROOF_LIVE.tex`:
  0 errors, 0 warnings.
- Full reference closure: 339 files, 11,250 labels, 0 multiply defined,
  0 dangling references.
- Open-problem inventory: PASS; 46 active atomic questions in 14 formal
  problem environments.
- Full PDF build: 3,309 pages; no undefined citations, undefined
  references, multiply defined labels, or rerun warning in the final log.
- Visual review: Chapter 15 physical pages 774--778 (printed 706--710) and
  Chapter 72 physical pages 3084--3087 (printed 3016--3019) are clean.

Verdict: **PASS for integration as a strict partial advance on P03.1.**

No model-backed verifier was used for this packet.
