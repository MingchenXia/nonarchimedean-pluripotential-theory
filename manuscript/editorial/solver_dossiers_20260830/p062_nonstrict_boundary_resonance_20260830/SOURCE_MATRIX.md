# Source matrix

| Use | Source | Exact direction used |
|---|---|---|
| Relative interior of an analytic domain; composition with a boundaryless ambient space | Berkovich, *Étale cohomology for non-Archimedean analytic spaces*, Proposition 1.5.5(i)--(ii) | Identifies the absolute interior of `P` with its ordinary interior inside analytic affine two-space. |
| Openness of the coordinate projection | Berkovich, same paper, Corollary 3.7.4 | The projection from analytic affine two-space to the first affine line is smooth, hence open. |
| Surjectivity of complete scalar extension | Chambert--Loir--Ducros, §11.1.9 | Every point downstairs has a point upstairs; used only to descend the already obtained affine identity. |
| Strict endpoint-polycylinder classification | `../p062_endpoint_polycylinder_rigid_slicing_v4_20260830/p062_endpoint_polycylinder_v4_statement_20260830.tex` and proof | Applied only over a field `L` in whose value group all displayed radii lie. |

Local source copies inspected during the audit:

- `/private/tmp/Berkovich1993_Etale.pdf`, SHA-256
  `bd864c89ed8b6e8f27a90f459837221549db75afa75554ab51414e17771066af`;
- `/private/tmp/CLD25.txt`, SHA-256
  `021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e`;
- strict-v4 principal statement SHA-256
  `56ffaad6c42e0a14c56279e263d326120ce03f6ae132d8261deee56ff9ca7663`;
- strict-v4 principal proof SHA-256
  `2616ac69cd450010b8f0d108d030bd69d2ff2728cad9641ad7d9d0e1a981a0b7`.

The following steps are proved directly and import no source theorem:

1. `|TS-1|<1` plus the reciprocal closed-disc bounds forces
   `|T|=R` and `|S|=R^{-1}`.
2. If `R` is outside the divisible value group, a multiplicative seminorm
   with `|T|=R` restricts to the `R`-Gauss norm, because every polynomial
   has a unique term of maximal weighted norm.
3. The explicit continuous cutoff has support in the invisible boundary
   tube and is zero on the absolute interior.

No equality of analytic interiors under an arbitrary complete scalar
extension is used or asserted.
