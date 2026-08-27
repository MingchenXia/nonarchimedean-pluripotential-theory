# P21.3 arbitrary-field virtual-annulus bridge audit (2026-08-27)

Status: **proved as a source-aware candidate; not yet production-Rethlas
verified and not integrated**.

## Exact conclusion

For an interior type-2 point of a strict rig-smooth curve over an arbitrary
complete nontrivially valued field, a branch is a closed point of the normal
projective integral residual curve. If a rational residue uniformizer at that
closed point is lifted to a \(K\)-analytic unit and appended to a moment, then:

1. on a cofinal downstairs virtual-annular collar, the moment image is exactly
   a Euclidean ray;
2. its saturated primitive tangent is the vector of refined branch orders and
   has the uniformizer coordinate equal to \(1\);
3. after a finite splitting extension, all source-annulus exponents are
   multiplied by one common positive integer \(e_b\);
4. finitely many further lifted residue functions separate any prescribed
   finite family of branch rays from every other outgoing branch ray;
5. therefore the Euclidean edge used in the source-separated localization of
   the proof of CLD Theorem 16.8.5 is exactly the downstairs virtual-annular
   branch edge, and a lifted residue function has scalar slope
   \(\operatorname{ord}_{p_b}\).

No arbitrary current is pulled to a splitting field. Base extension is used
only to prove the geometric monomial formula for the \(K\)-defined moment.

## Primary-source ledger

- Chambert--Loir--Ducros, arXiv:1204.6277v2, Theorem 16.8.5 and its proof:
  compact-domain boundary avoidance, proper tropical pushforward, and the
  Euclidean localized current.
- Ducros, arXiv:2405.10619:
  - §3.6.35.5--§3.6.35.10: skeleton and retraction of a virtual annulus,
    compatibility with scalar extension, and factorization of norms through
    the retraction;
  - Proposition 4.3.9(2), §4.3.10.2--§4.3.10.3: cofinal virtual-annular
    sections over an arbitrary field and finite separable splitting;
  - §4.2.6, §4.2.9, §4.2.11.1: refined branch valuation, naturality, and the
    residual discrete valuation at a closed point;
  - §3.6.22--§3.6.24 and §4.3.6.4: monomial norms on split annuli and the
    rank-one exponent;
  - §3.6.24.2 and Theorem 4.3.13(i): the common expansion/ramification index;
  - Proposition 4.2.4(ii): only finitely many nonconstant branch germs for a
    fixed analytic unit.
- Gubler--Jell--Rabinoff, *Bull. Soc. Math. France* 154 (2026):
  - the lifting step in the proof of Lemma 6.14: finitely many homogeneous
    residue elements lift to analytic germs;
  - §8.13: the moment skeleton has the unique integral-affine structure for
    which every face maps integral-affinely isomorphically to its image.

## Why the earlier obstruction disappears

The earlier dossier tried to identify a primitive *source* coordinate after
splitting with a primitive *downstairs target* coordinate. Those need not be
the same: the source coordinate may map with expansion index \(e_b>1\).
The correct comparison saturates the target lattice. A downstairs residue
uniformizer has branch order \(1\), so the target direction vector is
primitive; after splitting, the entire exponent vector is \(e_b\) times that
primitive vector. This both proves the desired slope formula and explains the
common pushforward factor.

## Scope

The candidate assumes a complete nontrivially valued ground field and a good
strict rig-smooth curve, and treats interior type-2 branch germs. Type 3 is
already the two-ray virtual-annulus case. Trivially valued, non-strict,
boundary, and singular-normalization cases are not added by this bridge.
