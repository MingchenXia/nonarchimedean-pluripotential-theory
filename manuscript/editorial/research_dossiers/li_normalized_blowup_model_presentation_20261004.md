# Positive polarization on a supplied normalized-blowup presentation

Date: 4 October 2026. This conditional book-external derivation extends
the earlier positive-model construction to a finite normalized base
change and a supplied sequence of normalized blowups. It identifies
which presentation suffices on an already reduced regular final model.
It does not construct semistable reduction, certify a general model
category, promote a book theorem or change an open-problem status.

## Supplied scheme/germ data

Use the projective scheme model over \(R=\mathbb C\{t\}\) and its
proper projective analytic germ realization. Assume an integral
projective flat model \(\mathcal X_0\) with relatively ample
\(A_0\) and a fixed meromorphic identification
\(A_0|_{D^*}\simeq L^{k_0}\), \(k_0>0\).
The generic polarized family is smooth and geometrically integral.
The construction is also valid over a supplied algebraic-curve model
in the same finite/noetherian projective category.

Supply a finite parameter cover \(t=\tau^q\) and finite normalization
\(\mathcal Y_0\) of the base-changed model. Its generic fibre is
the unchanged base extension with polarization \(L'\). Finite
normalization is an explicit assumption here. The scheme/germ
comparison and finite-normalization existence theorems of the relevant
excellent/analytic category remain imports.

Supply a finite sequence

\[
 \mathcal Y_s\xrightarrow{h_s}\cdots\xrightarrow{h_2}
                 \mathcal Y_1\xrightarrow{h_1}\mathcal Y_0,
                                                               \tag{1}
\]

where \(h_i\) is the blowup of a coherent nonzero ideal
\(\mathfrak a_i\), followed by its **finite** normalization.
Assume \(\mathfrak a_i|_{D_\tau^*}=\mathcal O\); thus the centre
and the ideal's divisor are vertical. Assume the final analytic total
space \(\mathcal Y_s\) is smooth and has a reduced SNC central
fibre, with the prescribed meromorphic canonical and polarization
interfaces. These final geometric properties and the sequence (1)
are supplied, rather than deduced from normalization alone.

All relative-ampleness statements below are scheme statements on this
finite presentation, transferred to the analytic germ by the fixed
projective/coherent comparison. The scheme base and every intermediate
model used as a base are quasi-compact. A finite parameter cover is
distinct from a modification, which is an isomorphism off zero.

## Finite pullback preserves the required ampleness

On an affine open of the parameter base, a relatively ample line
bundle is ample on the preimage. Pulling it back by a finite morphism
preserves ampleness: a finite morphism is affine, hence quasi-affine,
and Stacks Tag 0892, Lemma 29.38.7 **(2)** applies. Applying this on
each affine base open gives the relative assertion. Its referenced
ampleness lemmas remain source imports. The cached statement and its
displayed proof were checked, including the correct part number.

Relative ampleness is also preserved by the base change of a projective
embedding: after taking a relatively very ample power, pull back its
closed immersion into a projective bundle. Therefore the pullback
\(A'_0\) of \(A_0\) to the finite normalization \(\mathcal Y_0\)
is relatively ample, and

\[
                       A'_0|_{D_\tau^*}\simeq (L')^{k_0}.
                                                               \tag{2}
\]

The fixed identification in (2) is the base change of the original
one. No arbitrary punctured-parameter scalar is inserted into it.

## Tautological bundles on normalized blowups

Write \(B_i=\operatorname{Bl}_{\mathfrak a_i}\mathcal Y_{i-1}\),
\(g_i:B_i\to\mathcal Y_{i-1}\), and
\(\nu_i:\mathcal Y_i\to B_i\) for the finite normalization.
The blowup facts in Stacks Tag 01OF, Lemmas 31.33.4 and 31.33.13,
give

\[
 \mathfrak a_i\mathcal O_{B_i}=\mathcal O_{B_i}(-E_i)
              =\mathcal O_{B_i}(1),
 \qquad \mathcal O_{B_i}(1)\text{ is }g_i\text{-ample}.
                                                               \tag{3}
\]

The effective Cartier divisor \(E_i\) is vertical. It need not be
exceptional: if the ideal is an invertible vertical ideal, its blowup
is the identity and its Cartier divisor may be nonzero. The zero
ideal is excluded. Define

\[
 Q_i=\nu_i^*\mathcal O_{B_i}(1)
       =\mathfrak a_i\mathcal O_{\mathcal Y_i}.          \tag{4}
\]

It is an invertible ideal with a fixed trivialization away from zero.
Finite pullback, applied over each affine open in \(\mathcal Y_{i-1}\),
makes \(Q_i\) ample for \(h_i=g_i\circ\nu_i\). Thus the
normalization step preserves the relative positivity needed for the
composite modification. Intermediate models need not be smooth.

## Compose vertical twists on the final model

Let \(f_i=h_1\circ\cdots\circ h_i\) denote the map
\(\mathcal Y_i\to\mathcal Y_0\), with composition in that order
of maps from right to left. Put \(M_1=Q_1\), and inductively choose
a sufficiently large integer \(a_i\) such that

\[
                  M_i=Q_i\otimes h_i^*M_{i-1}^{a_i}
                       \text{ is }f_i\text{-ample}.     \tag{5}
\]

Stacks Tag 0C4K, Lemma 29.38.8, gives (5): its base
\(\mathcal Y_0\) is quasi-compact, the previous bundle is ample
for its composite map, and \(Q_i\) is ample for the new step.
The canonical trivializations in (4) make every \(M_i\) trivial
on the punctured family. If the sequence is empty, use
\(M_s=\mathcal O_{\mathcal Y_0}\) for the identity map.

Apply the same composition rule to \(f_s\) and the parameter map.
For a sufficiently large integer \(a>0\),

\[
 B=M_s\otimes f_s^*(A'_0)^a
   \text{ is relatively ample over }D_\tau,\qquad
 B|_{D_\tau^*}\simeq (L')^r,\quad r=ak_0.              \tag{6}
\]

This is achieved on the supplied final model itself. No further
blowup is used to obtain (6), so its assumed reduced central fibre
is retained. The exponents can depend on the supplied finite model
presentation. There is no uniform choice across all degenerations.

On the smooth final model, a sufficiently high power \(B^b\) gives
a projective germ closed immersion
\((j,\pi):\mathcal Y_s\hookrightarrow\mathbf P^N\times D_\tau\)
with \(B^b=j^*\mathcal O(1)\). Relative very ampleness, coherent
generation and analytic realization are the already explicit
projective-germ inputs. Taking the \((br)\)-th root of its FS
metric gives a reference \(h_+\) on \(L'\) with

\[
 \theta_+=(br)^{-1}j^*\omega_{\mathrm{FS}},\qquad
 \tfrac12\theta_++i\,d\tau\wedge d\bar\tau
                         \text{ Kähler on the total space}.   \tag{7}
\]

The fixed polarization power (6) is used in taking the root. The
immersion of the pair \((j,\pi)\) proves total positivity in (7),
including critical points of the parameter map.

## Meromorphic reference comparison and the hybrid cover

If \(\mathcal L\) is a supplied extension of \(L'\), the fixed
generic identification in (6) makes the ratio
\(B\otimes\mathcal L^{-r}\) a line bundle with a meromorphic
trivialization nonvanishing off zero. On the smooth final model its
Cartier divisor \(D=\sum_i d_iE_i\) is vertical. Smooth divisor
metrics give the same reference comparison as the previous bridge:

\[
 h_+=h_0e^{-2\chi_\tau},\qquad
 \chi_\tau=-(2r)^{-1}\sum_i d_i\log\rho_i+O(1),\qquad
                       \|\chi_\tau\|_\infty=O(T_\tau).
                                                               \tag{8}
\]

The O(1) term is from the smooth metric comparison on the fixed model.
The full model-reference difference, scaled by \(1/T_\tau\), has
the continuous hybrid model limit used in the prior reference-change
argument; an arbitrary O(T) function would not supply that property.
If only a rational extension was supplied, clear its fixed denominator
before applying this formula and use allowed divisible degrees.

The earlier reduced-model analytic, FS and hybrid route can now use
(7)–(8) under its remaining inputs, in either positive or zero essential
dimension. Descent to the original parameter still uses
\(T_t=qT_\tau\), divides the entire central log metric by \(q\),
and invokes the previously supplied cyclic trace/quotient argument.
Neither a finite normalization nor the vertical twist changes the
generic polarization in (2),(6).

## The presentation gate remains distinct from this consequence

The proved consequence is that the supplied normalized-blowup
presentation gives the positive rational reference on its smooth
reduced final model. A general claim of semistable reduction must also
supply that presentation, the finite-normalization category and the
proper projective/germ realization. Ordinary SNC base change being
toroidal is insufficient by itself to identify a regular reduced
final model or all its modification steps.

The present source search identifies the KKMSD book's DOI and its
Chapter 2, *Semi-stable reduction*, pages 53–108 from publisher/Crossref
metadata. The requested publisher book and chapter PDF links returned
HTML pages; the primary chapter was not acquired or inspected.
Mumford's public publication list identifies the book but is a metadata
document, not its proof. No theorem number or normalized-blowup
construction is claimed verified from those metadata records. The
earlier BJ Remark 7.2 retains semistable reduction as an explicit
KKMSD import. This note uses (1) as a hypothesis until that source and
application category are cleared.

No new numerical calculation or independent verifier was run. The
active book and all 42 statuses remain fixed. Proper/coherent,
ampleness and hybrid source dependencies retain their checked scopes;
book admission of a new result still requires exact-current independent
verification.
