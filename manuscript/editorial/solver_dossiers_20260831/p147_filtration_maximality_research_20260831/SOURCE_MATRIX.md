# Primary-source and normalization ledger

Access date: 31 August 2026. Source contents were read through existing text and official/author-hosted primary HTML or indexed primary text. No PDF was generated or visually inspected. The local source and manuscript hashes are in `INPUTS.json`. External versions are pinned below; their full bytes are not vendored and no external-file hash is asserted.

| Input | Exact locator and scope | Use in the candidate |
|---|---|---|
| Darvas–Xia–Zhang, arXiv:2302.02541v3, 17 July 2024 | §§2.1–2.2; §4.1, Definitions 4.1, 4.3–4.4, Lemma 4.5 and proof, Proposition 4.6 and proof. Existing `/private/tmp/dxz23.txt`, lines 329–472, 610–658, 1329–1475, read fully in those ranges. [Primary HTML](https://arxiv.org/html/2302.02541v3) | Exact target, filtration normalization, positive interior, dyadic envelope identity, ordinary/I-envelope bridge, birational filtered subseries. |
| Berman, arXiv:0710.4375v2, 25 December 2007 | §1.1 setup and Theorem 1.4; §1.4 conventions. [Primary HTML](https://arxiv.org/html/0710.4375v2) | Smooth full-section Bergman weights converge to the equilibrium weight on compact subsets outside the augmented base locus of a big line bundle. |
| Boucksom–Chen, *Okounkov bodies of filtered linear series*, Compos. Math. 147 (2011), 1205–1229 | Definition 1.1, Lemma 1.6. [Author's published text](https://sebastien.boucksom.perso.math.cnrs.fr/publis/BC.pdf), compared with [arXiv v1 HTML](https://arxiv.org/html/0911.2923v1) | For each strict interior filtration parameter the subseries contains an ample series; high sufficiently divisible maps are birational. |
| Stacks Project | [Tag 0BXQ, Lemma 33.27.1](https://stacks.math.columbia.edu/tag/0BXQ) | Finite normalization of the integral projective image \(Z\). |
| Stacks Project | [Tag 0AY8, Lemma 37.53.6](https://stacks.math.columbia.edu/tag/0AY8) | Proper birational morphism from integral reduced \(Y\) to normal integral \(Z^\nu\) has pushforward structure sheaf \(\mathcal O_{Z^\nu}\). |
| Stacks Project | [Tag 01PR, Proposition 28.27.13(7)](https://stacks.math.columbia.edu/tag/01PR); [Tag 02O1, Lemma 30.16.2](https://stacks.math.columbia.edu/tag/02O1) | A high twist of the nonzero conductor ideal has a nonzero section; polynomial restriction is surjective in high degrees. |

## Berman hypothesis check

The application is on the smooth connected projective resolution \(Y\), not on the potentially nonnormal image \(Z\). Its line bundle \(A=f^*\mathcal O_Z(1)\) is globally generated and big because \(f\) is birational. A smooth semipositive reference metric \(a\) is supplied by the generating subspace.

For each fixed integer \(j\), the metric \(a\exp(-\chi_j)\) is smooth everywhere, including \(E\), because \(\chi_j=-\log(|s_E|^2+j^{-1})\). The metric need not have positive curvature. Berman's fixed auxiliary Hermitian line bundle is chosen to be trivial; the theorem permits this. Only convergence on \(Y\setminus\mathbf B_+(A)\) is used. The elementary polynomial \(L^2\)/sup-norm comparison is written out in the proof. No estimate uniform in \(j\), in the fixed degree \(m\), or near \(E\) is imported.

Both Berman §1.4 and DXZ use squared local norms \(|e|^2=\exp(-\varphi)\) and \(\mathrm d\mathrm d^{\mathrm c}=\mathrm i\partial\bar\partial/(2\pi)\). Therefore the local section weight is \(k^{-1}\log|f|^2\), and no factor-of-two conversion is hidden. In particular \(\mathrm d\mathrm d^{\mathrm c}\log|s_E|^2=[E]-c_1(\mathcal O(E),h_E)\).

## Algebraic scope check

The normalized image is not assumed smooth; Stacks 0AY8 is applied to it only as a normal integral variety. Properness, reduced source, generic dominance, and generic function field equality all hold for the birational factorization. The conductor quotient has generic rank zero, so its annihilator is nonzero. This fails for a generically finite map of degree greater than one; the proof does not replace birationality by generic finiteness.

Serre vanishing is applied over \(\operatorname{Spec}\mathbf C\) to the coherent ideal of \(Z\) in projective space with its ample \(\mathcal O(1)\). The fixed conductor section kills the normalization defect before polynomial restriction is used. There is no assumption that every normalized section is a homogeneous polynomial in the original generators.

## Sources inspected as leads but not imported

- [Ross–Witt Nyström, arXiv:1101.1612v3, Theorem 7.10 and Proposition 7.11](https://arxiv.org/html/1101.1612v3): the displayed Skoda argument assumes ample input and uses it in global division. No unproved replacement of that assumption is used here.
- [Hisamoto, arXiv:1201.4236v3, Theorem 1.3 and Proposition 5.1](https://arxiv.org/html/1201.4236v3): the volume identity does not by itself imply the normalized fixed-point identity.
- [Finski, arXiv:2603.22194v1, §4.1](https://arxiv.org/html/2603.22194v1): the resolved-image strategy suggested the present investigation. The displayed multiplication map around (4.24) goes from downstairs sections to normalized sections, while the norm estimate requires the reverse return. A conductor correction is necessary for that return. This packet proves its own return with a fixed conductor and does not use Lemma 4.4 or Theorem 4.3.
- [Finski, arXiv:2512.10466v1, Theorem 2.16](https://arxiv.org/html/2512.10466v1): corroborates smooth/continuous full-section quantization, but the candidate uses Berman's original smooth theorem plus its own norm estimate.

Resolution of a coherent ideal on a smooth complex projective variety, local removable singularities for locally bounded-above psh functions across analytic sets, normalized quasi-psh \(L^1\)-compactness, and equality/ordering of psh representatives from almost-everywhere equality/ordering are standard background inputs, not newly claimed theorems. The proof spells out their particular uses. It does not use psh descent from a nonnormal target.
