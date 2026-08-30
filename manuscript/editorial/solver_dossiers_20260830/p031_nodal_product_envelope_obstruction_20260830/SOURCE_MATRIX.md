# Exact dependency matrix

This dossier is quarantined. It is not part of the live manuscript and has
not yet been submitted to production Rethlas.

## D1. The one-dimensional nodal computation

The exact previously verified source bytes are:

- manuscript/editorial/rethlas_packets_20260825/p03_nodal_local_envelope_statement_exact_20260825.tex
  — SHA-256
  10ac70696f69b1ed18ae1522c0b065fe9240d8f921b9db258201c9e8a7b509e1;
- manuscript/editorial/rethlas_packets_20260825/p03_nodal_local_envelope_proof_exact_20260825.tex
  — SHA-256
  21fc22e5b1f3b3084f29df412a57485131e46ca160cf168db18da8a3e2559fc7;
- manuscript/editorial/rethlas_receipts_20260825/p03_nodal_local_envelope_api_response_20260825.json
  — SHA-256
  c8ac792474289be20183a6e2c3f8822f0c0bca335cc6f31f07e0bd1004b583bc.

The response verdict is correct. The present proof uses only the two raw
envelope values in the verified statement, the explicit convergent rigid
sequence from lines 144–151 of the verified proof, and the construction and
singleton-Shilov description of \(D_r\) from lines 78–96.

## D2. Pullback and maximum-principle facts

The following standard facts are required and must be materialized in any
production request:

1. analytic pullback preserves locally Fubini–Study functions;
2. analytic pullback preserves real PL functions and their semipositivity;
3. analytic pullback and analytic-domain restriction preserve classical psh
   functions;
4. a classical psh function on a strict affinoid domain is bounded above by
   its values on the Shilov boundary;
5. every CLD-v2 psh function is classically psh.

Items 3–5 are already used in lines 98–107 and 155–166 of the exact verified
proof in D1. Item 2 may equivalently be obtained by combining pullback
stability of classical psh functions with the classical-psh/semipositive
equivalence for real-valued real-PL functions. Production materialization
must not silently extend any of these facts to trivially valued, non-strict,
or non-good spaces.

## D3. Elementary affinoid algebra

The product is
\[
\mathcal M\bigl(K\langle x,y,t_1,\ldots,t_d\rangle/(xy)\bigr).
\]
The coordinate ideals \((x)\) and \((y)\) are prime, their intersection is
\((xy)\), and both quotients are Tate algebras in \(d+1\) variables. This is
the only algebraic input used for reducedness, purity, and dimension.
