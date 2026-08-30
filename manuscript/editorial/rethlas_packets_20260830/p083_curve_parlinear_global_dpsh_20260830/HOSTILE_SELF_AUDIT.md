# P08.3 hostile self-audit

## Verdict

The frozen statement/proof is audit-ready only in the stated scope:
`K` algebraically closed, complete, nontrivially valued; `X` smooth,
proper, connected, strict and one-dimensional. The proof has one explicit
internal dependency, the already verified P08.1 curve local-to-global
theorem. That dependency is not written as a mathematical hypothesis.

## Sign ledger

1. Local weight: `phi_e = log ||e||^{-1} = -log ||e||`.
2. Curvature: `c1(L,h)|_U = dd^c phi_e`.
3. If `s=f e`, then `phi_s=phi_e-log|f|`.
4. Thuillier Proposition 3.3.15 gives
   `dd^c log|f|=delta_div(f)`, hence
   `c1(L,h)=dd^c phi_s+delta_div(s)`.
5. On the proper curve the exact-current term has mass zero, so
   `c1(L,h)(X)=deg L`.
6. Replacing `h` by `e^{-u}h` changes the weight to `phi+u` and curvature
   to `c1+dd^c u`.
7. The Green convention is
   `dd^c g_{x,y}=delta_y-delta_x`; therefore the finite sum
   `u=sum a_y g_{x,y}` has `dd^c u=nu-d delta_x`, and multiplying the
   reference norm by `e^{-u}` changes `d delta_x` to `nu`, with the desired
   plus sign.

The printed display in Thuillier Definition 3.4.17, p. 97, writes the
curvature locally as `dd^c log||s||`. Read literally, that conflicts with
the same definition's requirement that `-log||s||` be subharmonic,
Proposition 3.4.4 (`dd^c` of a lisse subharmonic function is positive),
Corollary 3.4.18, and Remark 3.4.20. The frozen proof does not use that
isolated display. Its sign is fixed by the CLD weight convention,
Thuillier Proposition 3.3.15, and the operational formulas in Remark
3.4.20.

## Degree and domination ledger

Let `mu=mu^+-mu^-` and `m=mu^-(X)`. Choose an integer `d>m`, a rational
point `p`, and `A=O_C(d[p])^{\An}`. Then

- `deg A=d>0`;
- `nu=mu^-+(d-m)delta_x` is positive and has mass `d`;
- `mu+nu=mu^++(d-m)delta_x` is positive;
- `deg(L tensor A)=deg L+d=mu^+(X)+(d-m)>0`.

Thus neither application of P08.1 falls into its degree-zero branch. This
is exactly why CLD Corollary 17.8.7 can be reached through relatively ample
Q-model approximants.

## Existence ledger

- `p in C(K)` exists because `C` is a nonempty proper curve over an
  algebraically closed field; closed points are `K`-rational.
- A type-II point `x` exists, for example as a vertex of a semistable
  formal model. Algebraic closedness removes the finite-extension issue in
  this use.
- `A=O_C(d[p])^{\An}` is algebraic by construction. Since `L=M^{\An}`,
  both `L_1=L tensor A` and `L_2=A` are algebraic analytic line bundles.
- Remark 3.4.20 supplies the reference lisse subharmonic metric of
  curvature `d delta_x`; Proposition 3.3.7 supplies every finite Green
  correction needed to obtain `nu`.

## Exact match to CLD 17.8.5

P08.1 gives uniform limits of relatively ample Q-algebraic model metrics,
not immediately the sequence of ordinary smooth psh metrics demanded by
CLD 17.8.5. The frozen proof closes this gap as follows:

1. Clear the denominator of one Q-model metric.
2. The resulting metric on a tensor power is formal and relatively ample,
   hence semiample; CLD Corollary 17.8.7 makes it globally psh.
3. Take positive tensor roots of its smooth psh approximants; local
   weights divide by the tensor exponent, preserving smoothness and psh.
4. Diagonalize over the uniform Q-model approximation.
5. The product metric on `L_1=L tensor A` divided by the metric on `A`
   recovers the original norm pointwise, so
   `(L,h)=(L_1,h_1) tensor (A,h_A)^vee` is an isometry, not merely a line
   bundle isomorphism.

This is the literal global-dpsh definition, not just local dpsh or Zhang
semipositivity.

## Scope firewalls

- No statement for singular curves.
- No statement for a non-algebraically-closed or trivially valued field.
- No higher-dimensional extension.
- No algebraization of a specified formal model.
- No claim that an arbitrary signed/diffuse curvature current has a
  continuous prescribed-curvature potential. Finite atomic curvature from
  parlinearity is essential.
- No claim that the original parlinear metric is globally psh; only its
  explicit isometric quotient decomposition is proved.
- CLD Corollary 17.8.9 is an independent cross-check, not a substitute for
  any unverified step in the frozen proof.
