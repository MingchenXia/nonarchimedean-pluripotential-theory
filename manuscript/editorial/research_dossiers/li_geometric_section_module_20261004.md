# Geometric section modules and faithful formal Laurent expansions

Date: 4 October 2026. This book-external derivation supplies the section
and expansion inputs under a supplied projective analytic/algebraic model
interface. Derived cohomology, finite-presentation descent and analytic
comparison remain source imports. No general degeneration theorem,
independent verifier receipt or problem solution is admitted.

## Model category and fixed-degree signature

Put \(R=\mathbb C\{t\}\), \(F=\operatorname{Frac}R\), and
\(K=\mathbb C((t))\), with \(\operatorname{ord}(t)=1\).
The ring \(R\) is a DVR: every nonzero germ is \(t^q\) times a unit,
and choosing the least order in a nonzero ideal shows that ideal is
principal. Assume supplied:

- A flat projective scheme \(\mathcal X_R\) of finite presentation
  over \(R\), with geometrically integral generic fibre, and an
  invertible sheaf \(\mathcal L\) whose generic restriction is ample.
- Its projective analytic germ realization \(\mathcal X\to D\),
  with the same line bundle, smooth connected complex fibres off zero,
  and a regular SNC total model near the chart used below.
- The finite-presentation realization, coherent sheaf/section comparison,
  and proper complex-fibre cohomology comparison. These are used only in
  their projective, proper-support category; an arbitrary holomorphic
  family with essential singularities is not substituted.

The projective-germ interface is recorded in Chapter 59, (59.7a).
The cached retyping of Bingener's 1976 text, Theorem (4.2) and
Corollaries (5.3)–(5.4), anchors proper cohomology and
coherent/line-bundle comparison.
For a single proper complex fibre, (4.2) specializes to the usual
algebraic/analytic cohomology comparison. The finite-presentation descent
and flatness input is Stacks Tag 05LY, Lemma 32.10.4; proper perfect
derived cohomology and arbitrary base change is Tag 0B91, Lemma 36.30.4.
These are imports with their stated hypotheses, not fresh proofs of
every underlying analytic or algebraic theorem.

Fix a degree \(l\) for which \(\mathcal L^l\) is an honest line
bundle on this model, and put

\[
 M_l=H^0(\mathcal X_R,\mathcal L^l),\qquad
 V_F=H^0(X_F,L_F^l),\qquad V_K=H^0(X_K,L_K^l).            \tag{1}
\]

If the initial model is only a rational line bundle, take a sequence
of divisible degrees tending to infinity. None of the approximation
or diagonal arguments requires every positive integer as a degree.

## Derived base change and freeness

Flatness of \(\mathcal X_R\) and invertibility of \(\mathcal L^l\)
give exactly the hypotheses of Tag 0B91. Thus
\(R\Gamma(\mathcal X_R,\mathcal L^l)\) is perfect, represented
by a bounded complex of finite free \(R\)-modules. Its cohomology,
in particular \(M_l\), is finite over \(R\).

Multiplication by \(t\) is injective on \(\mathcal L^l\), by flatness,
and therefore on its global sections. Every nonzero element of \(R\)
is a unit times a power of \(t\), so \(M_l\) is torsion free.
A finite torsion-free module over a DVR is free. Let its rank be \(d\).
Flat localization and completion commute with the cohomology of the
finite complex; derived base change then gives

\[
 M_l\otimes_R F=V_F,\qquad M_l\otimes_R K=V_K.          \tag{2}
\]

In particular the completed section space is the tensor extension of
the convergent one, of the same dimension. The second identity is
cohomological base change along the flat ring map \(R\to K\), not
an assertion about the central fibre \(\mathcal X_0\).
Ordinary \(H^0\) base change at zero is not automatically inferred
from arbitrary **derived** base change.

## Actual small complex fibres and the germ-ring firewall

There is no \(\mathbb C\)-algebra evaluation map \(R\to\mathbb C\)
at a fixed \(t_*\ne0\): the germ \(t-t_*\) is a unit at zero and
would be sent to zero. Accordingly a complex fibre is not called the
base change of \(\operatorname{Spec}R\) by such an evaluation map.

Instead descend the finite model, line bundle and section data to a
finitely generated \(\mathbb C\)-subalgebra \(R_0\subset R\).
The projective embedding and finite equations descend; enlarge \(R_0\)
so the model is flat using Tag 05LY, applied to its finite-presentation
structure sheaf. Finite-presentation line bundles and the finitely
many chosen sections descend after a further enlargement. Such finite
descent is part of the projective-germ interface above.

For the proper flat model over \(R_0\), Tag 0B91 supplies a perfect
cohomology complex. Near the image of the closed point of
\(\operatorname{Spec}R\), represent it by a bounded finite free
complex \(P^\bullet\), localizing by finitely many functions nonzero
there if necessary. Its matrices involve finitely many convergent
germs. Their common radius yields a holomorphic parameter map from a
small disc to \(\operatorname{Spec}R_0(\mathbb C)\).
The supplied germ realization identifies its projective fibres with
the given complex fibres. Base change of \(P^\bullet\) at these
actual complex points computes algebraic fibre cohomology, and the
proper fibre comparison computes holomorphic cohomology as well.

Over \(F\), split this finite complex by elementary row and column
operations. Include the coordinates of an \(R\)-basis
\(e_1,\ldots,e_d\) of \(M_l\) in that splitting. The operations,
their inverse matrices and their denominators involve finitely many
meromorphic germs. Their nonzero denominators and determinants have
no zeros on one sufficiently small punctured disc. Specializing this
finite splitting there proves

\[
 (e_1|_{X_t},\ldots,e_d|_{X_t})
      \text{ is a basis of }H^0(X_t,L_t^l)
      \quad(0<|t|<r_l).                                 \tag{3}
\]

Here “specializing” refers only to the finitely many functions on their
common disc, not to all of \(R\) or \(F\). The construction also
allows \(d=0\), where it asserts vanishing. No exceptional nonzero
parameters accumulate at zero after this finite splitting.

For all sufficiently large (or sufficiently divisible) degrees, generic
ampleness gives global generation on \(X_F\). The coherent cokernel
of the evaluation from the finite basis is zero after inverting \(t\).
On a finite affine cover it is therefore killed by a common power
\(t^q\), since it is finitely generated. This finite annihilation
identity carries to the analytic germ realization. Off zero it proves
global generation on every small complex fibre, after a degree-dependent
shrinking. It does not require \(\mathcal L\) to be ample on the
central model.

Any invertible change of basis over \(F\) consequently gives another
basis on all sufficiently small punctured fibres: its finitely many
meromorphic entries and its determinant are well-defined there and
the determinant is nonzero. This applies to the earlier convergent
truncations of formal chamber bases and to their finite coefficient
matrices.

## Taylor expansion on a single stratum chart

Take a relatively compact product chart with transverse polydisc \(W\),
\(0\leq m\leq n\), and local vertical equations satisfying

\[
 t=z_0^{b_0}\cdots z_m^{b_m},\qquad b_i\in\mathbb Z_{>0}. \tag{4}
\]

The analytic model line bundle is trivial on this chart. In a fixed
frame \(\tau\) of \(\mathcal L^l\), its finitely many basis sections
\(e_i\) have convergent Taylor expansions in the \(z\)-variables,
whose coefficients are holomorphic on one common connected \(W\).
Let \(R_W=\mathcal O(W)\), an integral \(\mathbb C\)-algebra, and

\[
 A_W=R_W[[z_0,\ldots,z_m]][z_0^{-1},\ldots,z_m^{-1}].    \tag{5}
\]

The substitution \(t=z^b\) embeds \(K\) into \(A_W\).
Each formal scalar has only finitely many negative powers, and its
positive powers have increasing order in every \(z_i\). Thus every
element of \(V_F\otimes_F K\), expanded using the finite basis,
maps to (5), with coordinatewise lower-bounded exponent support.
Meromorphic convergent sections have the same description after a
power of \(t\) clears their local poles.

It remains to prove this map is injective; injection over \(F\)
alone would not justify injection after completion.

## Finite analytic-path determinant proves faithfulness

Assume \(d\geq1\), since the zero space is immediate. Put
\(B=\sum_{i=0}^m b_i\), and choose a sufficiently small
\(\xi_*\ne0\) with \(t_* =\xi_*^B\) in the punctured radius (3).
The chart part of \(X_{t_*}\) is nonempty. Evaluation on this open
part separates its global sections: a holomorphic section vanishing
there vanishes on the connected fibre by the identity principle.
Since (3) is a basis, the evaluation rows span \(\mathbb C^d\).
Choose \(d\) chart points at which their square evaluation matrix
in the frame \(\tau\) is invertible.

For the \(j\)-th point write its coordinates as
\((a_{0j}\xi_*,\ldots,a_{mj}\xi_*,w_j)\). Equation (4) says
\(\prod_i a_{ij}^{b_i}=1\). Define analytic paths

\[
 z_i=a_{ij}\xi,\qquad w=w_j,\qquad t=\xi^B.            \tag{6}
\]

All \(a_{ij}\ne0\). Shrinking to a chart polydisc if needed, these
paths are defined on a disc containing both zero and \(\xi_*\):
every coordinate becomes smaller as \(|\xi|\) decreases. Their
evaluation determinant is convergent in \(\xi\) and nonzero at
\(\xi_*\), hence is a nonzero convergent germ and a nonzero element
of \(\mathbb C((\xi))\).

For each \(j\), evaluation at \(w_j\) and substitution in (6) define
a ring homomorphism \(A_W\to\mathbb C((\xi))\). This is well-defined:
positive powers of all \(z_i\) become positive powers of \(\xi\),
so only finitely many monomials contribute to a given exponent;
coordinatewise lower bounds control negative exponents. Evaluation
at \(w_j\) is defined on \(\mathcal O(W)\); no evaluation of all
holomorphic germs at a different transverse point is being attempted.

If \(\sum_i a_i(t)e_i\) had zero expansion in (5), applying these
\(d\) maps would give the invertible evaluation matrix times
\((a_i(\xi^B))_i\) equal to zero. Hence every \(a_i(\xi^B)=0\).
The field embedding \(K\hookrightarrow\mathbb C((\xi))\),
\(t\mapsto\xi^B\), is injective, so every \(a_i=0\).
This proves the required faithful \(K\)-linear inclusion

\[
                  V_K\hookrightarrow A_W.              \tag{7}
\]

The auxiliary ramified paths prove independence only. They do not
replace the original parameter in the convergence theorem, alter its
normalization, or assert semistable reduction of the original family.
The argument permits repeated central components and \(m=0\),
and zero transverse dimension means \(R_W=\mathbb C\).

## Consequence and limits of this reduction

Under the supplied model interface, (2)–(3),(7) supply the geometric
section-module, convergent-fibre-basis and faithful formal-expansion
inputs of the fixed-degree chamber construction. Its Lipschitz bound
remains the separately checked BFJ input; the global model presentation
and analytic/cohomological imports are not erased by this reduction.

All radii and choices are at a fixed degree. There is no claim of
central ordinary base change, formal relations being controlled by
mere convergent independence, or evaluation of a whole germ field at
a nonzero parameter. Singular/disconnected generic fibres and models
without the stated projective proper-support realization are outside
the signature. The active book and all 42 statuses remain unchanged.
