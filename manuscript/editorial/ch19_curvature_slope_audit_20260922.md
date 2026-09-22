# Chapter 19: curvature and the weighted slope formula — 22 September 2026

## Mathematical repair

The skeletal-curvature proof no longer identifies [u] with a graph
current because u factors through a retraction. It tests d'd''[u]
against an analytic smooth function, enlarges the skeleton to support
its differential forms, and integrates twice along the edges.
Analytic Stokes supplies the vanishing sum of outgoing test-function
derivatives. This compatibility is not an automatic balancing
property of an abstract graph. The conclusion is an atomic measure
for the specified model functions, not a measure theorem for all currents.

For a strictly semistable node xy=a, the edge length is -log|a|.
Its weight is the residue degree of the node, not automatically one.
After scalar extension to a completed algebraic closure, the geometric
edges have the same lengths and weight one. Counting their germs gives
the graph-Laplacian descent formula. Integration-current scalar
extension then descends the analytic identity. Residual degrees give
the curvature coefficients; tensor-power denominators are retained.

The nonreduced DVR case is recorded separately. Vertex values
lambda a_Y/b_Y, intersection lengths lambda/(b_Y b_Z) and node residue
weights reproduce b_Y(D.Y) by the special-fibre intersection identity.
The formal-measure formula now states exactly where these
multiplicities apply. Other formal models retain the factors in the
formal-intersection theorem. The finite positivity criterion explicitly
assumes a common strictly semistable model for the metric and function;
such a model is not asserted to exist automatically over every field.

A blowup at a separable closed point of degree d gives a unit-length
edge with weight d and curvature d delta_Y - d delta_E. This directly
checks the missing residue factor. The Chapter 17 multiple-fibre
example and the Chapter 18 model-corner argument now cite the separate
nonreduced normalization. Chapter 8's introduction refers to the
operator on the analytic curve.

The slope proof separates three steps. Poincare--Lelong first gives a
finite signed divisor measure, so its pushforward by the continuous
retraction is defined. The annular Newton-polygon calculation and the
local residue-slope formula then give edge affineness and the vertex
identity. The open-disc calculation accounts for the divisor mass
collapsed by retraction. Finally, scalar extension descends the result,
including lengths of inseparable point fibres. The annular and
residue-slope facts remain explicit analytic inputs. Endpoint
differences must be divided by edge length; xy=pi^r checks this factor.

## Sources and validation

Checked primary sources:

- [Chambert--Loir--Ducros, arXiv v2](https://arxiv.org/pdf/1204.6277v2):
  Lemma 18.2.14(a), the calculation preceding Lemma 18.2.17 and
  that lemma, printed pages 509 and 511--513; Propositions 15.3.1
  and 16.1.1 for scalar extension; Theorem 18.5.5 for formal
  intersection coefficients. The curve calculation's algebraically
  closed hypothesis is respected before descent.
- [Baker--Payne--Rabinoff, published author offprint](https://web.ma.utexas.edu/users/sampayne/pdf/StructureOfNonarchimedeanCurves.pdf):
  Proposition 2.10, printed page 100, and Theorem 5.15(3),
  printed pages 118--119. The published numbering is used with
  the existing BPR13Structure entry. These pages and the CLD
  Stokes calculation were inspected as PDF images.

A second reading checked signs, both endpoint terms in integration
by parts, scalar-extension weights, component and closed-point
degrees, inseparable lengths, the blowup calculation and model
hypotheses. The production closure was searched for consumers of
the revised labels. Complete new curvature, slope and blowup blocks
pass the strict writing audit with zero errors and zero warnings.

The source check passes for 389 TeX files and 11,492 labels:
no missing input, duplicate label, dangling reference or structural
defect. The full build has 3,915 pages and 18,579,160 bytes,
with no unresolved reference or citation and no horizontal or
vertical overflow. Physical pages 1430--1436 (printed 1362--1368)
were rendered and inspected, including the common-model hypothesis,
the two proofs and the transition to the Tate example.

PDF SHA-256:
`ea077a2a8dc22afa547778b2c3b65ffb943fa0676193c5be5b514ab942810b72`

Chapter 19 SHA-256:
`26d435910eb09cc05a4d9445a8faab9940d7cc1fb73012ae3595c808a1ef4229`

The open inventory remains 46 active atoms in 14 formal environments,
with tiers (0,5,8,16,17). The author-supplied CURVE_PSH.tex, Chapter 71,
frozen research inputs and dated release artifacts are unchanged.
This is a repair of existing results and exposition, not a new
research-verification gate. The distinction between the nonreduced
intersection metric and stable lattice metric in Chapter 5 remains
the next source audit.
