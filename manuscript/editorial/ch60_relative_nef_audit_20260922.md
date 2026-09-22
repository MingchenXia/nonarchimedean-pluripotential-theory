# Chapter 60: relative numerical nefness — 22 September 2026

## Scope and sources

This revision fills in the numerical reduction in
`thm:mp-model-closedness`. It does not change that imported theorem, promote
a new research result, or change the active problem inventory.

The published primary source checked was Demailly–Păun, *Annals of
Mathematics* 159 (2004), 1247–1274, DOI
[10.4007/annals.2004.159.1247](https://doi.org/10.4007/annals.2004.159.1247).
The [journal PDF](https://annals.math.princeton.edu/wp-content/uploads/annals-v159-n3-p05.pdf)
provides the following exact dependencies:

- Theorem 4.3(iii), p. 1267: linear intersection tests against every Kähler
  class characterize nefness on a compact Kähler manifold.
- Proposition 3.3(i)–(ii), p. 1262: extension of positivity to an ambient
  neighbourhood and gluing on finite unions of analytic subsets.
- Theorem 0.1, p. 1248: the connected-component characterization of the
  Kähler cone.
- Equation (4.4) and its polynomial-pairing proof, pp. 1267–1268.

Mesquita-Piccione's [arXiv:2409.06221v2, Theorem 4.1.5](https://arxiv.org/html/2409.06221v2)
was checked directly for the divisorial-net statement and its cycle/current
argument. The publisher record confirms *Advances in Mathematics* 481
(2025), 110543, already present in `MP24`. The publisher's full text was
not available during this audit. The revised proof therefore explicitly
identifies arXiv version 2 as the version whose theorem number was checked.
No published locator is asserted on the strength of a preprint alone.

## Mathematical checks

The previous bare reference to a numerical criterion omitted the distinction
between Kähler classes on a central component and on the total space. The
new argument uses only the latter, as the imported theorem does.

For a class Kähler on each reduced fibre, local positive representatives
are patched using weights pulled back from the base. The error terms vanish
on the vertical tangent kernel. Adding a sufficiently large multiple of
the pullback of a base Kähler form then gives total-space positivity, by
compactness of the unit tangent bundle. This argument also covers critical
points of the model morphism.

Starting with `beta + a Omega` positive on every fibre, the proof produces
ambient Kähler test classes `s beta + a Omega + C_a eta`. The base term
restricts to zero on every central cycle. The polynomial identity and
connected-component criterion reduce `a` by a factor `1-delta_0`, uniformly
in all iterations and dimensions `1,...,n`. The constants `C_a` may vary.
Taking `a` to zero proves relative nefness. The zero-dimensional case is
handled separately. This is a reconstruction of the omitted reduction,
not a new regularization theorem.

**Normalization correction.** As printed, the sentence after (4.4') says
`A_p(t,0)=1`; with the displayed (4.4), the correct value is `p`. For
example, in degree 2, an integrand coefficient 1 gives only half of
`y^2-x^2`. The book factors out `d`, uses `B_d(s,0)=1`, and proves the
normalization by polynomial pairing and the fundamental theorem of calculus.
Equivalently, its coefficients are uniquely determined by
`integral_0^1 B_d(s,delta) s^j ds = (1-delta)^(d-1-j)/(j+1)`.
An exact rational-arithmetic check of these moments in dimensions 1–5
confirms the displayed identity and its normalization; the all-dimensional
argument is in the text and does not rely on that finite check.

The final analytic-cycle paragraph stays explicitly imported. It now says
that the exceptional current's **pushforward** is a positive multiple of
the cycle, and that its intersection expression is affine in finitely many
divisorial values: the fixed background class supplies the constant term.
No common model for the entire net is assumed.

## Validation and remaining limits

- Baseline scoped Chapter 60 build: 82 pages, two unresolved occurrences
  of an external Chapter 69 label, and one 4.25891 pt overfull display.
- Second-pass scoped build: 84 pages, the same two external-reference
  occurrences, no unresolved citation, and no overfull box. The old energy
  display was split into two aligned lines without changing its mathematics.
- The revised proof passes the strict writing audit with zero errors and
  zero warnings. The bibliography-aware house audit requests a BibLaTeX
  `label` field for `MP24`; this book uses its existing BibTeX style, which
  already renders the correct compound-name label `MP25`. No unrelated
  bibliography migration was made. Both cited keys resolve.
- Physical pages 58–61 and 66–67 of the final scoped PDF were rendered
  and inspected. The proof, the neighbouring transitions, and the repaired
  energy display have no clipping or overlap.
- Second reading checked the vertical gluing, the positive base correction,
  the uniform shrinking parameter, all cycle dimensions, the zero-dimensional
  exception, and the imported-core boundary.
- The source check still reports the same missing Chapter 70 input and
  thirteen unresolved file/label pairs: 388 available files, 11,428 labels,
  no duplicates or structural defects. No full-book success is claimed.
- The inventory check passes: 46 active atoms, 14 formal problem
  environments, tiers `(0,5,8,16,17)`.

The model-independence lemma earlier in Chapter 60 still deserves a separate
explicit descent proof; this revision does not treat its compressed
pushdown-of-perturbations sentence as established by the present audit.
