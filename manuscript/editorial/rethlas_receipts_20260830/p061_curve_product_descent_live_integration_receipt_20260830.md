# P06.1 curve-product descent: production and live-integration receipt

Date: 30 August 2026 (Asia/Shanghai).

## Mathematical scope

The exact packet proves the following singular higher-dimensional part of
P06.1.  Let (K) be complete and nontrivially valued.  Classical
pluriharmonic functions are real-PL and harmonic in the sense of
Gubler--Jell--Rabinoff on a good product of finitely many geometrically
reduced good strict analytic curves and a good strict quasi-smooth factor.
The same conclusion holds on a good strict analytic space locally
isomorphic to an open analytic subspace of such a product.  In particular,
the result covers all non-quasi-smooth strata of the displayed nodal and
cuspidal cylinder products.

The scope firewall is part of the result: no conclusion is asserted for an
arbitrary singular germ, a product containing a non-geometrically-reduced
curve factor, or a space without the stated local product presentation.
P06.1 is therefore narrowed but not retired.

The integrated labels are:

- `lem:p061-rational-section-tube`;
- `lem:p061-parameterized-rigid-point`;
- `prop:p061-curve-product-normalization-descent`;
- `thm:p061-curve-product-ph-rpl`;
- `cor:p061-finite-curve-products-ph-rpl`;
- `ex:p061-nodal-cuspidal-products`.

## Exact frozen bytes

- statement SHA-256:
  `96b246d6f6032bce38751095935525a67456c6753e006e7b188778bc945e50bc`;
- source-aware proof SHA-256:
  `6f6158b5253922539f81e42ab9e6d9e2c48a6b3c8b727e4157351b9591baabe5`;
- standalone compiled PDF SHA-256:
  `2fbd7b983803348f53066d0968687bf2259bc375810e802e8827150085df3476`.

Three independent fail-closed exact-byte audits passed before production
submission.  They separately checked the completed-tensor estimate and
product-neighbourhood basis, quasi-smoothness of every normalized product,
finite normalization descent, ground-field descent, the open-subspace
extension, absence of circularity, and the example quantifiers.

## Production Rethlas gate

The dependency-closed request included the already verified quasi-smooth
packet.  The controlling production service used `gpt-5.6-sol` at `xhigh`.

- archived run directory: `20260829T191019Z_0b5e24145108`;
- checked item: `pi_6add90bcf0cfded12d6a074b`;
- verification status: `final`;
- verdict: `correct`;
- critical errors: 0;
- gaps: 0;
- item disposition: `verified`;
- proof digest:
  `a19410a54ff7299a83996b4199fc348478d63a5ad37d2cd439ca81f5e7f79b97`;
- request SHA-256:
  `7b9130dd0748d025721a1407c01d19f4d567e291f7127439a5483a3036486605`;
- response SHA-256:
  `a58b374e706367006a174361f9670402aa75fc5103590817d87d72d3311d74eb`;
- safe-header SHA-256:
  `e4c041172fce9e83c6d3b01617706a9cdad7fd5461faf4605678506632527035`.

The archived response and the verifier's `verification.json` agree on the
item, digest, final verdict, and zero-error/zero-gap result.

## Live integration

The exact statement and proof are input byte-for-byte in Chapter 18.  A
local `ntheorem` presentation wrapper removes a duplicated proof-heading
word without changing either verified packet file.  Chapter 18 contains the
full proof, comparison table, hypothesis ledger, examples, and provenance.
Chapter 72 and the atomic inventory now state only the residual question.
The Part II introduction and Appendix L record the positive scope and its
firewall.

Post-integration SHA-256 values are:

- Chapter 18:
  `5f2f6bc7e0018f696d14e8592fcf1cde56082f7b1a53b1bcb2ea9d92f6cbf049`;
- Chapter 72:
  `d815513e69c2c3bc107e7f659f4663bbfe54ce55991e95ab494a1aa7d46be9b1`;
- Part II introduction:
  `689e1b38fb72a3c30458b90f9ff8e80ed2dca411b57ae79d093c7f2482b37236`;
- Appendix L:
  `e6fd8f317ed460827d15f43702b011cda489e5d5624e5b9ba672aa0694e4a1f1`;
- atomic inventory:
  `ccede35ac3223d4677a75069084e2441675dce2ee241996daa1a1f4b539a2241`;
- verified-results ledger:
  `01ae2a89c5c8ca1146589328c30fd2d59d0be2d2bb6fc53b73dd3b7e98734b2e`;
- theorem-provenance ledger:
  `3bd64ac1396ceb2ae5bb566345f463522fa74a58d694308da9c4138b44d8aa2a`.

## Whole-book build and visual audit

Starting from base commit
`a0fc1dfd6f67cdd5afdb97f43e36e96da7b59101`, the book was built to
convergence with

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error book.tex
```

The final log scan found:

- LaTeX errors and undefined control sequences: 0;
- undefined references and citations: 0;
- multiply defined labels: 0;
- rerun warnings: 0;
- overfull horizontal boxes: 0.

The final PDF has 3,338 pages and 16,023,200 bytes.  Its SHA-256 is
`32c3ce8f34d168b217112437deb76ba977eda9e2abf060099255563027114f4d`.
The synchronized `manuscript/book.pdf` and
`output/pdf/Non-Archimedean_Pluripotential_Theory.pdf` hashes agree.

Physical PDF pages 990--991, 3143--3144, 3288, and 3306 were rendered and
inspected.  They cover the new statements and proof opening, the narrowed
open-problem discussion, the production gate, and the Appendix L provenance
record.  The audit found no clipping, overlap, broken link text, malformed
formula, redundant proof heading, or margin intrusion.

## Inventory consequence

The live source contains 14 formal problem environments and 53 active atomic
questions.  The tier distribution remains `(0,5,14,17,17)`, and the T2 queue
remains `P21.3, P07.1, P06.1, P06.2, P03.1`.

No novelty or priority claim is made.
