# Hostile audit: Chapter 18 fibre-cylinder repair

## Disposition

- **Current live text: FAIL.** The cited CLD25 proposition is unrelated,
  (W_I) is undefined, the proof does not discharge the (d=1)
  hypotheses of the actual theorem, and the boundary proof promotes a
  top-skeleton product to an unqualified whole-face equality.
- **Staged replacement: PASS, source-aware.** No counterexample exists in
  the intended Chapter 18 scope. The repair restores the correct current
  CLD numbering and spells out the only local commutative-algebra entry.
- **Live-file status: untouched.** This packet only stages text under the
  editorial snapshot.

## Adversarial checks

### 1. Is the cited theorem really the same theorem?

Yes. CLD25 Theorem 14.7.2(a) gives equality of the calibrated
((n-1))-skeleta of all fibres near the rigid origin when (d=1).
Part (b) gives the calibrated product on the punctured tail. Restricting the
open tail to a smaller closed interval gives item (2). The exchange of
factors and the sign change from (log|f|) to (-log|f|) preserve the
unoriented vector-volume calibration.

The misleading number has an identifiable origin: GK17 p.54 cites the
older CLD12 Proposition 4.6.6 for exactly these conclusions. In CLD25 the
result is Theorem 14.7.2, while Proposition 4.6.6 now means boundary
compensation.

### 2. Does a Cartier divisor by itself meet the (S_1) and
pure-relative-dimension hypotheses?

Not globally on all of (W), and the replacement does not claim that.
At every point of (W_0), the defining germ is a regular element. The
local argument recorded in the proof of CLD25 Lemma 16.7.5 gives (S_1)
and pure relative dimension (n-1) on a neighbourhood of (W_0).
Because (W_0) is compact, a sufficiently small compact tube
(W_{le R}) is contained in that neighbourhood. Theorem 14.7.2 is
applied to this tube, not blindly to all of (W). For (|t|<R) and for
annuli inside ((0,R)), the tube fibres are the original (W_t) and
(W_I).

This use of Lemma 16.7.5 is not circular: only its preliminary local
dimension/depth argument is used, not the Poincare--Lelong conclusion.

### 3. What if the effective Cartier divisor is empty?

The original statement silently encounters the zero tropical cycle. The
replacement separates this case. Compactness gives
(min_W|f|>0), so all sufficiently small fibres and annuli are empty.
The common complex is explicitly allowed to be empty. This avoids relying
on a convention that the empty complex is pure of every dimension.

### 4. Are (W_t) and (W_I) well-defined?

They are now defined. (W_t) is the analytic fibre after scalar extension
to (mathscr H(t)), and (W_I=|f|^{-1}(I)cap W). This is the notation
used explicitly in GK17 p.54.

The boundary paragraph also defines its local specialization explicitly:
`W_E(I)={x in W_E: |f(x)| in I}` and
`Sigma_E(I)=h_{E,trop}(W_E(I))`. Thus it does not silently extend the
earlier radius notation `Sigma_E(s)=h_{E,trop}(W_E(s))` to an interval.

### 5. Does item (3) retain all multiplicities?

Yes. CLD25 Section 13.7.1 identifies the divisor with the associated cycle
of the zero subspace; its coefficients are generic lengths. Proposition
16.6.3 identifies integration over that possibly nonreduced subspace with
integration over its associated cycle. Hence the canonical top-cell
calibration has the divisor multiplicities, not merely reduced support.

The replacement says “the ((n-1))-skeleton of the calibrated
tropicalization.” Without this qualification, an arbitrary moment map can
have lower-dimensional image pieces, and “the whole tropicalization” would
be stronger than either CLD25 Theorem 14.7.2 or GK17 p.54.

### 6. Does the Poincare--Lelong proof need all three strong clauses?

No. It only needs, for finitely many (W_E), one common radius and one
annulus (I=[s,\rho]): the (n)-dimensional calibrated part of the annular
tropicalization must be the product of the standard interval with the
calibrated zero fibre. It then needs the zero-fibre calibration to equal the
Cartier-divisor calibration. Fibre constancy for every analytic (t) is
stronger than the boundary pairing requires.

### 7. Is the truncation face literally the entire product?

Not from a skeleton statement alone. GK17 Lemma 7.3, pp.57--58, explicitly
warns that the tropicalizations can differ from their top-dimensional
skeleta inside the relative boundary. Its proof uses freedom in the
defining polytopes and in (s) to arrange the required pure-dimensional
annular product before passing from (7.3.8) to (7.3.9). The replacement
restores that step. This is the minimal mathematical repair to the affected
boundary paragraph.

### 8. Is GK17 Lemma 7.3 in the correct test category?

Yes. Remark 7.4 immediately after the lemma states that the calculation
holds for compactly supported generalized delta forms. Thus it supports
the Chapter 18 delta-current pairing, not merely the smooth CLD current.

## Remaining nonblocking editorial choices

1. The chapter may cite GK17 Theorem 7.2/Lemma 7.3 directly and shorten the
   reproduced boundary proof, or retain the proof with the restored
   relative-boundary sentence. The staged text takes the latter route.
2. The source note near original line 5259 must be changed from “CLD25
   Proposition 4.6.6” to “CLD25 Theorem 14.7.2”; otherwise the chapter
   remains internally inconsistent even after replacing the lemma proof.
3. The chapter's standing hypotheses already impose the field assumptions
   of GK17. No field-scope expansion is made by this repair.
