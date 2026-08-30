# Independent hostile audit of the frozen finite-quotient descent candidate

Date: 30 August 2026

## Verdict

**PASS.**  I found no mathematical gap in the frozen statement or proof.  In
particular, the proof does not use finite-flat descent, exactness of invariants,
or division by the group order in the ground field or valuation ring.  This is
an independent source-aware audit, not a production Rethlas verdict and not an
authorization for live-book integration.

The exact audited hashes are:

- statement
  `e1daa4b3e3efd64fcc8f0ce05b9c1d5d6cb69b28686b939b48535fc56b0ccc07`;
- proof
  `a6c24d1686c726dc72aebe55a1e83eb8d4fe1ed4025d4a8d7166da59123ce30e`.

## 1. Ordinary-open localization

Gubler--Jell--Rabinoff Proposition 5.8 says exactly that, for a divisible
coefficient group such as \(\mathbf R\), an \(\mathbf R\)-PL function is,
on an **ordinary open** neighbourhood of any point, a finite real linear
combination of integral PL functions.  Thus proof lines 12--20 do not repeat
the invalid inference from a member of a Berkovich G-cover to an ordinary
neighbourhood.

The clean slice in lines 2--10 is valid.  For the stabilizer \(H=G_y\), the
Hausdorff separation argument of Hansen--Johansson Lemma 5.2 supplies an
\(H\)-stable ordinary open \(C\) whose distinct \(G/H\)-translates are
disjoint.  Its saturation is open, and the finite quotient has the orbit
topology and invariant structure sheaf.  Consequently \(C/H\simeq q(C)\),
with \(q(C)\) ordinary open.

After intersecting the GJR neighbourhood with its finitely many
\(H\)-translates, it remains an \(H\)-stable ordinary neighbourhood.  A
strict affinoid neighbourhood \(N_0\) may be chosen inside it.  Because the
ambient affinoid is separated, the finite intersection
\(N=\bigcap_{\gamma\in H}\gamma N_0\) is a strict affinoid domain.  Each
factor contains \(y\) in its ordinary interior, so \(N\) is still a
neighbourhood, not merely an analytic domain containing \(y\).  Its relative
interior \(N^\circ\) is \(H\)-stable and is an ordinary neighbourhood of
\(y\).

## 2. Common equivariant formal model

GJR 5.6 realizes each integral PL function on the affinoid \(N\) as a model
function.  The proof correctly closes the equivariance dependency rather than
assuming it:

1. a finite group of bounded affinoid automorphisms preserves an affine
   admissible ring of definition after adjoining the finitely many translates
   of a finite set of suitably scaled generators;
2. Raynaud cofilteredness extends the identity of generic fibres, after an
   admissible formal blowup \(\mathfrak P_i\to\mathfrak N_0\), to a morphism
   \(\mathfrak P_i\to\mathfrak N_i\);
3. the torsion-free schematic closure of the diagonal generic fibre in the
   product of all \(\gamma^*\mathfrak P_i\) is an admissible model, is
   preserved by \(H\), and maps to every model carrying
   \(\mathfrak L_i\).

There is no loss of the generic fibre in the closure/torsion-removal step.
Every admissible formal blowup is projective over \(\mathfrak N_0\).  Hence
the resulting model is closed in a projective formal scheme over the affine
model \(\mathfrak N_0\); its special fibre is projective over an affine
finite-type residue-field scheme and therefore quasi-projective over the
residue field.

This matches Zavyalov Remark 3.3.3: quasi-projectivity of the special fibre
implies that every finite orbit lies in an affine open.  The affine-orbit
hypothesis of Zavyalov Theorem 3.3.4 is therefore genuinely established.

## 3. Formal quotient and generic fibre

Zavyalov Theorem 3.3.4 supplies an admissible formal quotient
\(\pi:\mathfrak N\to\mathfrak X=\mathfrak N/H\), a finite surjective map,
orbit fibres, the quotient topology, and the invariant quotient structure
sheaf.  The proof does not invoke the theorem's flat-base-change clause.

Zavyalov Theorem 4.4.1 applies under the same affine-orbit hypothesis and
identifies
\[
                 \mathfrak N_\eta/H\simeq(\mathfrak N/H)_\eta
\]
as adic spaces.  Since the original generic fibre is the strict affinoid
\(N\), the associated rank-one/Hausdorff Berkovich realization is the usual
affinoid quotient \(N/H\); affinoid-locally this is also the quotient defined
by the invariant affinoid algebra.  No open-subset assertion is transferred
illegitimately from the spectral topology of the adic space.

## 4. Tensor-induced line bundle in wild characteristic

For a model line bundle \(\mathfrak L\), put
\[
          \mathfrak T=\bigotimes_{\gamma\in H}\gamma^*\mathfrak L.
\]
Reindexing gives a canonical \(H\)-linearization satisfying the cocycle
condition.  The proof's invariant-frame descent is valid even when the
quotient is nonflat or the residue characteristic divides \(|H|\):

- an affine open containing a quotient fibre pulls back to an affine
  neighbourhood of the finite orbit;
- a rank-one projective module is free on a neighbourhood of that entire
  orbit by semilocal triviality;
- after intersecting translates, the neighbourhood is \(H\)-stable while
  the original frame still restricts to it;
- the tensor of all translated frames is fixed by the reindexing
  linearization;
- the image of this saturated invariant open is open, and invariant ratios
  of two such frames descend, together with their invariant inverses, through
  \(\mathcal O_{\mathfrak X}=(\pi_*\mathcal O_{\mathfrak N})^H\).

These descended transition units glue a line bundle
\(\overline{\mathfrak L}\) with
\(\pi^*\overline{\mathfrak L}\simeq\mathfrak T\).  This is a direct local
construction; it does not use exactness of the invariant functor.  At a
geometric fixed point, a stabilizer only permutes the one-dimensional tensor
factors, so the induced stabilizer action is trivial, consistently with the
explicit invariant frames.

The generic trivialization also descends.  Tensoring the translated generic
frames gives an invariant global frame of \(\mathfrak T_\eta\).  Relative to
each invariant formal frame, its ratio is an invariant analytic unit.  The
generic-fibre quotient's invariant sheaf descends these ratios, and the
resulting local frames glue.  Thus
\(\overline{\mathfrak L}\) is a model of the analytically trivial line
bundle with the required compatible trivialization.

Consequently pullback compatibility of model functions gives exactly
\[
 q_N^*h_{\overline{\mathfrak L}}
   =h_{\mathfrak T}
   =\sum_{\gamma\in H}\gamma^*h_{\mathfrak L}.
\]

## 5. Averaging and final local descent

The only averaging occurs in the real coefficient space:
\[
 v=\frac1{|H|}\sum_i a_i h_{\overline{\mathfrak L}_i}.
\]
Since the coefficient group is \(\mathbf R\), this is an
\(\mathbf R\)-PL function regardless of the characteristic of \(K\) or its
residue field.  No element \(|H|^{-1}\) is used in \(K\), \(K^\circ\), a
formal coordinate ring, or an invariant module.

The equality
\[
 q_N^*v=|H|^{-1}\sum_{\gamma\in H}\gamma^*u=u|_N
\]
uses only the functional \(H\)-invariance of \(u=q^*g\).  The quotient
\(N^\circ/H\) is ordinary open in both \(N/H\) and \(C/H\): it is the
quotient of a saturated invariant ordinary open, and the quotient topology
and invariant sheaf agree on the restriction.  Surjectivity of \(q_N\)
therefore identifies \(v\) with \(g\) on an ordinary neighbourhood of the
chosen quotient point.  Analytic-topology sheafiness of real-PL functions
then proves the global conclusion.

## 6. Scope audit

The proof uses only:

- a finite **constant** group action;
- a separated strict affinoid source, ensuring Hausdorff clean slices,
  affinoid intersections, an invariant affine formal model, and existence of
  the analytic quotient;
- continuity of \(g\), as required by the definition of real-PL;
- real coefficients.

It nowhere uses freeness, etaleness of the quotient map, flatness,
reducedness, normality, tame residue characteristic, or invertibility of
\(|G|\).  The statement does not claim descent for coefficient groups not
closed under division by stabilizer orders, nonconstant finite group
schemes, infinite groups, nonseparated or nongood sources, or arbitrary
nonaffinoid quotients.  I found no overclaim within the displayed scope.

## 7. Source passages checked

- Gubler--Jell--Rabinoff, Definition 5.1, 5.6, Proposition 5.8, and
  Corollary 5.9: G-local definition, integral model realization, and the
  ordinary-open decomposition.
- Zavyalov, Remark 3.3.3 and Theorem 3.3.4: quasi-projective special fibre,
  affine-orbit hypothesis, finite formal quotient, orbit fibres, and
  invariant quotient sheaf.
- Zavyalov, Theorems 4.3.4 and 4.4.1: adic quotient and compatibility with
  formal generic fibre.
- Hansen--Johansson, Lemma 5.2 and Theorem 5.3: clean ordinary slices and
  finite rigid quotient topology.

The cited passages support the uses made of them.  The frozen candidate may
proceed to an additional independent audit and, only afterward, exact-byte
production Rethlas verification.
