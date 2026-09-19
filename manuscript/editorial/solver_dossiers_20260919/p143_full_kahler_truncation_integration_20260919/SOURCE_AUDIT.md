# P14.3 full Kähler truncation — source and boundary audit

## Local source copies

The production request supplies exact cited ranges from the durable local
text copies of the three primary sources as explicit dependencies:

- Boucksom--Jonsson / Mesquita-Piccione framework, arXiv:2409.06221v2,
  whole-file SHA-256
  `0445ccf2c4474b6576a8053d0c7c038ffbd72c2ab27bb3d5704b90dd0e5beb62`,
  lines 2085--2265 and 2435--2585 in `SOURCE_EXTRACT_MP24.txt`;
- Darvas--Xia--Zhang, arXiv:2302.02541v3, whole-file SHA-256
  `7d5a061d240096139e6302c2b4da2e9c125a8839730fc90909c1488baa446244`,
  lines 850--925 and 1260--1350 in `SOURCE_EXTRACT_DXZ23.txt`;
- Xia, arXiv:2312.17150v3, whole-file SHA-256
  `c75572e06a2df8cb9dbd76726678a52db5e79587ec568df41f4886e3e4ee8005`,
  lines 400--805 in `SOURCE_EXTRACT_XIA23.txt`.

All three files live under
`manuscript/editorial/solver_dossiers_20260901/p142_source_closed_production_release_repaired_authored_stage_dossier_v2_20260901/`.

## Interfaces checked

- MP Definition 4.3.1 and the surrounding properties define the psh cone as
  a decreasing model completion and give rational/real translation stability.
  MP Theorem 4.3.8 is the divisorial comparison principle.  The finite-energy
  ray interface is in MP Theorems 5.1.4 and 5.1.7 and Section 5.2.
- Xia Section 4 works in the compact Kähler setting.  Its Lemma 4.2 gives
  divisorial order reflection; Definition 4.7 and Corollary 4.8 give maxima;
  Definition 4.9 and Lemma 4.10 give decreasing infima with their endpoint
  and divisorial formulas.  Section 3.2 and Lemma 3.10 give positive-volume
  recovery by an unperturbed curve.
- DXZ Definition 3.3, formula (43), and Theorem 3.17 supply the inverse
  system, normalized finite-energy formula, and finite-energy ray
  correspondence.
- The P14.2 all-point upper-semicontinuity theorem and the dominated
  divisorial-density theorem are already live, independently audited Chapter
  71 inputs.  They are hypotheses/dependencies here, not silently reproved.

The compactness/directedness proof of MP decreasing stability and the full
truncation deduction are new arguments, not claims attributed verbatim to a
source.

## Boundary checks

The proof uses no metrizability or countable cofinality of the model category:
each `phi_j` is resolved by a net, and only the explicit truncation parameter
`j` is sequential.  The continuous minimum in the stability proof is not
declared psh.  Finite energy is obtained only after zero-tail and
positive-volume recovery.  No uniform lower energy bound in `j` is needed.

The trivial semivaluation is included when endpoints are compared.  The
all-point equality is not inferred from ordinary density: it uses the
dominated divisorial net, upper semicontinuity, ideal antitonicity, and the MP
comparison principle.

The conclusion is conditional on P14.2, is restricted to Kähler classes, and
does not assert an unchanged MP theory for big non-nef or zero-volume classes.
