# Dependency audit

Date: 13 September 2026

Status: dependency-closed verification passed.

The final verifier request placed the following exact dependencies before
the new principal statement and proof:

1. the exact CLD infinite-star collapse theorem, including its comparison
   sheaf, countable-activity theorem, finite harmonic smoothing, and endpoint
   construction;
2. the Stone--Euclidean collapse theorem, including its common countable
   Boolean quotient and finite clopen discretization.

Exact dependency SHA-256 values:

- infinite-star statement:
  99c1a6a6a712005e73ee3b7cdae297606895b22ce79c80a6411dfd7f4863c963
- infinite-star proof:
  ca49ad210cf8e64100cc00c31c16a76f207ecd0d4b37dc365e8e1c61ce903090
- Stone--Euclidean statement:
  dfd8c7cc9d6d26f50260707975ff62d4f292627f084400bcd37b32253c876cdc
- Stone--Euclidean proof:
  9316e1a9df86c73a68ec099d3254e451ceaaac17a15c2a92441ad44961d863f6

No external lemma was silently imported into the principal proof.  The CLD
topology and smooth structure enter only through the frozen exact
infinite-star dependency; the one-dimensional interior case enters through
the frozen Stone--Euclidean dependency.
