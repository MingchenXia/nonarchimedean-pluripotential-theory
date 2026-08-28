# P17.1 packet: relative resultant for ample quotient systems

Date: 28 August 2026

Status: exact candidate for a future production Rethlas submission.  The
statement and proof are staging-only and are not included by the live
manuscript.

## Files to verify byte for byte

- p171_basepoint_free_relative_resultant_statement_20260828.tex
- p171_basepoint_free_relative_resultant_source_aware_proof_20260828.tex

## Verification request

Audit the exact theorem and proof as a new extension of François Ducrot's
relative resultant construction.  Return a final verdict of correct only if
there are zero critical errors and zero proof gaps.  In particular, check:

1. \(S\) is locally Noetherian, \(X/S\) is flat and projective with nonempty
   pure \(n\)-dimensional fibres, and every \(L_i\) is relatively ample.
2. The data are only quotients \(f^*E_i\twoheadrightarrow L_i\); the proof
   must not identify \(E_i\) with \(f_*L_i\) or a complete linear system.
3. Basepoint-freeness makes the bad parameters at an associated point a
   proper linear subspace.  Ampleness separately excludes an empty next cut
   on a positive-dimensional preceding intersection.
4. The transferred depth bounds are at least two for
   \(P\setminus\bigcup U_\tau\) and at least one for
   \(P\setminus\bigcap U_\tau\).
5. Ambient depth and local-cohomology extension do not require \(S\) to be
   reduced, normal, or \(S_2\).
6. The projection formula has the displayed sign and exponent, and mixed
   degrees retain generic lengths on nonreduced fibres.
7. Incidence is asserted only at fibre-local depth at most one, except when
   \(n=0\).
8. Symmetry and locally Noetherian base change apply to the section as well
   as its line.
9. Under ampleness, the rank-one endpoint can occur only for \(n=0\).
10. The \(\mathbf P^1\times\mathbf P^1\) example lies outside the ample
    theorem and only tests the semiample codimension-one firewall.

## Source boundary

The genuinely imported facts are the intersection-line properties in
Proposition 6.1.1, the norm identification in Corollary 6.1.2, and the
projection calculation in Lemma 6.3.1 of Ducrot's arXiv preprint
alg-geom/9712010, published as *Cube structures and intersection bundles*,
J. Pure Appl. Algebra 195 (2005), 33--73.  Lemmas 6.3.2--6.3.3, the
unnumbered gluing paragraph following Definition 6.3.4, and Lemmas
6.3.5--6.3.6 are proof templates in Ducrot's complete sufficiently positive
setting; their quotient-system analogues, including naturality of the
resultant section under base change, are reproved in this packet.  The new
claim replaces the complete system by an arbitrary finite locally free
basepoint-free quotient system while retaining relative ampleness.

This packet does not prove the semiample case, equality with the
D'Andrea--Krick--Sombra cycle resultant, a Chen--Moriwaki metric isometry,
non-Noetherian descent, or Pille--Schneider Question 4.9.
