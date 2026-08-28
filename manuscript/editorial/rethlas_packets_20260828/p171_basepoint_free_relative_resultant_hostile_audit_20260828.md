# Hostile audit: the ampleness firewall

Date: 28 August 2026

Status: staging audit.  No theorem in the live manuscript is changed.

## Rejected first formulation

The first plan proposed Ducrot's relative resultant for every finite locally
free basepoint-free quotient
\[
f^*E_i\twoheadrightarrow L_i.
\]
That plan was too strong for Ducrot's regular-sequence proof.  His definition
requires the final zero intersection of a relative regular sequence to be
nonempty.  Associated-point avoidance proves that a section is a
non-zero-divisor, but it does not prove that its zero scheme is nonempty.

Take a positive-dimensional projective scheme \(X/k\), put
\(L=\mathcal O_X\), and let
\[
k^2\longrightarrow H^0(X,\mathcal O_X)=k,\qquad (a,b)\longmapsto a.
\]
This is a basepoint-free quotient system with parameter space \(\mathbf P^1\).
Away from the kernel point its universal member is a unit and has empty zero
scheme; at the kernel point it is identically zero.  Thus it is never a
length-one regular sequence in Ducrot's sense.  With sufficiently many such
trivial systems, every \(U_\tau\) is empty.  The complement of
\(\bigcup_\tau U_\tau\) then contains the generic point of the parameter
space and has fibre-local depth zero.  Ducrot's depth-two extension argument
cannot be transferred verbatim.

This does not disprove the existence of a more general resultant.  In
degenerate systems the expected resultant may be a unit while the incidence
locus has codimension at least two.  It disproves the proposed proof and
therefore blocks integration.

## Minimal repair in the current candidate

The candidate assumes every \(L_i\) is \(f\)-ample.  If a regular member of
\(L_i\) were nowhere vanishing on a nonempty positive-dimensional projective
preceding intersection \(W\), it would trivialize \(L_i|_W\).  That
restriction is ample, whereas the trivial bundle on a positive-dimensional
proper scheme is not ample.  Hence the zero scheme is nonempty.
Basepoint-freeness separately supplies associated-point avoidance.  These are
the two independent inputs in the transferred depth proof.

Relative very ampleness, higher-direct-image vanishing, completeness of the
linear system, and an identification \(E_i=f_*L_i\) are not used.

## Boundaries retained

- \(S\) is locally Noetherian.
- Fibres are conservatively assumed nonempty and pure of dimension \(n\).
- Base change is asserted only for locally Noetherian \(T\to S\).
- Incidence is detected only when
  \(\operatorname{depth}\mathcal O_{P_s,p}\leq1\).
- No equality with a cycle resultant or metrized Chow form is claimed.
- The candidate remains outside the book until an exact production
  gpt-5.6-sol/xhigh Rethlas run returns correct with zero critical errors and
  zero gaps.

## Next generalization

To remove ampleness, one can try an admissible sequence convention that
allows an empty intersection and declares all later cuts admissible, with
unit norm on the empty finite-flat scheme.  Order independence, both depth
bounds, base change, and symmetry must then be reproved.  This is a genuine
new packet, not an editorial corollary of Ducrot.
