ID: n2

SUMMARY:
Sharp sequence obstruction for one boundary target: the Gauss-point spike on a closed disc has no continuous regularizing sequence when the algebraically closed residue field is uncountable, but has an explicit decreasing LFS sequence when it is countable. Projective-space products give higher-dimensional failures. Nets remain possible.

DETAILED SUMMARY:
The upper semicontinuous function equal to one at the actual boundary Gauss point and zero elsewhere is classical psh by the published extension-from-interior property. Every Gauss-point neighborhood contains all but finitely many complete residue discs. Countably many continuity neighborhoods leave an untouched residue branch when the residue field is uncountable, contradicting the proposed limit. For countable residue, truncated logarithms with value-group radii give finite LFS approximants on the fixed disc, with explicit monotonicity and convergence. A finite-subset construction gives a net even in the uncountable case.

SUPPORT:
[]

TEXT:
Let K be complete, algebraically closed and nontrivially valued, D=M(K⟨T⟩), and ζ its Gauss point. Define b(ζ)=1 and b=0 elsewhere. This is upper semicontinuous. The actual analytic boundary of D is {ζ}, and b is the constant zero on Int(D). GR arXiv:2506.13548v2 Proposition 3.5(3) therefore makes b subharmonic on D; 4.1.2 makes it classical psh. This uses a boundary point, not an interior spike.

The components of D\{ζ} are the open residue discs D_a indexed by a∈K̃. Any ordinary neighborhood N of ζ contains every complete D_a except finitely many: its compact complement is covered by these disjoint open discs, so has a finite subcover.

Suppose continuous h_j on one neighborhood N₀ converge pointwise to b. For each j,m, continuity supplies N_{j,m}⊂N₀ containing ζ with |h_j(x)−h_j(ζ)|<1/m. Each N_{j,m} omits only finitely many complete residue discs. If K̃ is uncountable, choose a outside the countable union of those exceptional sets. Every x∈D_a then satisfies h_j(x)=h_j(ζ) for all j, by letting m tend to infinity. Its limiting value is one, contradicting b(x)=0. Thus no continuous sequence with this limit exists locally, and in particular no decreasing LFS sequence exists.

On X=D×P^r_K^an, r≥1, pull b back by projection. It is arbitrary-class classical psh by functoriality. A rational projective point gives a section through (ζ,p). Restricting any purported local LFS sequence to that section yields the forbidden continuous sequence. These are good strict higher-dimensional spaces with a genuine analytic boundary.

The residue cardinality criterion is sharp for this particular target. If K̃ is countable, enumerate its elements a_i without repetition, choose lifts t_i∈K°, choose c₀ with 0<|c₀|<1, set α=−log|c₀|, and choose d_j with d_j^j=c₀. On the fixed D put
b_j=1+Σ_{i=1}^j (j/α) max{log|T−t_i|,log|d_j|}.
The maximum is finite at zeros. Its bend has radius |d_j| in the value group. The domains |T−t_i|≤|d_j| and |T−t_i|≥|d_j| form a strict affinoid G-cover; the term is constant on the first and the logarithm of a unit on the second. Thus it is strict real PL. Near its zero it is locally constant. Elsewhere the unscaled maximum is max{−log|(T−t_i)⁻¹|,−log|d_j⁻¹|}, the actual GJR 7.9 LFS formula. Nonnegative coefficients, sums and constants preserve semiample residues, so b_j is LFS everywhere.

At ζ all summands vanish and b_j=1. At x∈D_{a_k}, every summand except the kth vanishes, and after that term is included its value is max{(j/α)log|T−t_k|(x),−1}. Consequently 0≤b_j≤1, b_{j+1}≤b_j, and b_j(x) eventually equals zero. Hence b_j↓b on D. Roots, lifts and domains are over K; pulling back their formulas preserves LFS and convergence to the pulled target under every analytic extension.

For uncountable K̃ the same formula indexed by finite subsets of residue classes and an increasing positive integer truncation parameter gives a decreasing LFS net with infimum b. Therefore this is a sequence obstruction, not a net obstruction or a characterization of the full failure range.

The proof and explicit formulas are retained in Section 8 of P02.2-argument.md and P02.2-paper.tex. Published boundary hypotheses and literal excerpts are retained in source-extracts/source-provenance.json. These are unverified mathematical claims, independent of execution checks.

Artifacts: /workspace/research/campaigns/round-42/P02.2-public-source-decreasing-LFS/artifacts/codex-gsYJxq
