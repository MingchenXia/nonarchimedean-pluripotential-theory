ID: n4

SUMMARY:
Sharp boundary-spike family: the closed-disc function equal to 1 at the Gauss point and 0 elsewhere is classically psh. Uncountable residue fields prohibit any continuous approximating sequence near that boundary point; countable residue fields admit an explicit decreasing weakly smooth psh sequence. Products give higher-dimensional sequential failures. Nets and the general characterization remain unresolved.

DETAILED SUMMARY:
Polynomial reductions show that every neighborhood of the Gauss point contains rational points in all but finitely many residue classes, producing an obstruction to any pointwise continuous sequence when the residue field is uncountable. With countable residue field, lifted irreducible residue polynomials and a smooth concave cutoff construct an explicit decreasing sequence on the whole closed disc. Coprimality ensures at most one active summand. Convex logarithmic profiles prove harmonic weak smoothness, classical positivity and positive curvature on the analytic interior. Pullbacks converge to the pullback function, not a newly defined single-point spike. The residue-countability threshold is exact for this particular target, not a characterization for all targets or all spaces.

SUPPORT:
["n1", "n2"]

TEXT:
Draft boundary theorem. Let K be any complete nontrivially valued field, E=M(K<T>) the strict closed unit disc, and xi its radius-one Gauss point. Define b(xi)=1 and b(z)=0 otherwise. Then b is an upper semicontinuous classical psh function. If the residue field is uncountable, b is not the pointwise limit of any sequence of finite continuous functions on any ordinary neighborhood of xi, even without monotonicity. If the residue field is countable, the explicit construction below gives finite weakly smooth classical psh functions decreasing to b on the whole fixed E, with positive curvature on its analytic interior.

Classical membership. The actual analytic boundary of E is {xi}. For 0<a≤1, {b<a}=E\{xi} is open, so b is upper semicontinuous. It is constant zero on Int(E). GR Proposition 3.5(3) makes it subharmonic on E, and GR 4.1.2 makes it classically psh, including the required tests after every analytic extension. This is an analytic-boundary function, not an interior spike on a boundaryless space.

Neighborhood lemma. Every ordinary neighborhood N of xi contains rational points from all but finitely many residue classes. Polynomial evaluations generate the spectrum topology because polynomials are uniformly dense in the Tate algebra. Choose a basic neighborhood given by finitely many polynomial absolute-value conditions. Normalize each nonzero polynomial by a coefficient of maximum absolute value; its reduction is a nonzero residue polynomial. It has only finitely many roots in the residue field. For a lift a∈K° of a residue class avoiding these roots, every selected polynomial has precisely its Gauss absolute value at a. Thus a lies in N.

Uncountable-residue obstruction. Suppose continuous q_j on N converge pointwise to b. Discard finitely many terms so q_j(xi)>3/4. Each {q_j>3/4}∩N is a neighborhood of xi and excludes rational points from only finitely many residue classes. An uncountable residue field has a class outside the countable union of these exceptions. Choose a lift a of that class. Then q_j(a)>3/4 for every remaining j, contradicting b(a)=0. Since weakly smooth functions are continuous, this excludes the requested sequential regularization. It does not exclude decreasing nets.

Countable-residue construction. Enumerate the monic irreducible polynomials of the residue field as p_1,p_2,... and choose monic coefficientwise lifts P_i∈K°[T], each of Gauss norm one. Let sigma be a smooth nonnegative probability density supported in (0,1), symmetric about 1/2, and set
  eta(t)=2 integral from t to 1 of sigma(s) ds,
  psi(t)=integral from 0 to t of eta(s) ds,
with sigma zero outside (0,1). Then eta is smooth, nonnegative and nonincreasing, equals 2 for t≤0 and 0 for t≥1. Thus psi is smooth, increasing and concave, with psi(0)=0 and psi(t)=1 for t≥1; the latter follows from 2 integral_0^1 s sigma(s)ds=1.

Define
  v_j(z)=1-sum_{i=1}^j psi(j[-log|P_i(z)|]),
with a summand defined to be 1 at a zero of P_i. This convention agrees on a whole neighborhood of each zero, because psi is constant for arguments at least 1.

At most one |P_i(z)| is less than one. Otherwise two coprime reductions admit a Bezout identity whose lift would express 1 as terms of absolute value strictly less than one plus an error polynomial of Gauss norm strictly less than one, contradicting the ultrametric inequality. Therefore 0≤v_j≤1. Existing summands increase with j and new summands are nonnegative, so v_{j+1}≤v_j.

If all |P_i(z)|=1, every polynomial has its Gauss norm at z. To see this, normalize the polynomial, factor its reduction into the p_i, and compare it with the corresponding product of lifts. Their difference has Gauss norm less than one. Consequently z=xi by equality of polynomial seminorms. Every other z has exactly one i with |P_i(z)|<1; its summand is eventually exactly 1. Hence v_j(z)→0 away from xi and v_j(xi)=1 throughout.

Smoothness and positivity. Write H_j(s)=1-psi(-js). It is smooth, convex and nondecreasing on R, and zero for s≤-1/j. Each H_j(log|P_i|) is locally constant near the zero set and elsewhere a smooth function of an invertible analytic logarithm. It is therefore weakly smooth through an actual smooth harmonic tropicalization; ordinary CLD smoothness here follows from the explicit coordinates, not from a weak-smooth label. Classical positivity follows from the supporting-line argument in n2, including the constant supporting line at zeros. Since
  v_j=sum_{i=1}^j H_j(log|P_i|)-(j-1),
the cone and constant properties prove classical positivity. Its local curvature is the sum of
  H_j''(log|P_i|) d'log|P_i| wedge d''log|P_i|,
with nonnegative coefficients. The integration argument in n2 gives positive strong and CLD currents on Int(E). No boundary-free integration-by-parts assertion is made on the entire closed disc.

All formulas pull back after every analytic extension, remain weakly smooth and classically psh, remain decreasing, and converge to b∘p. That pullback can equal 1 at more than one extension-field point; it is not replaced by a new single-point Gauss spike.

Higher-dimensional failure. For m≥1 take X=E×P^{m,an} and u=b∘pr_E. This is classical psh on a separated good strict pure-dimensional space of dimension m+1. Fix a K-rational projective point p and x=(xi,p). The analytic section s(z)=(z,p) pulls any alleged sequence on an ordinary neighborhood of x back to a continuous sequence on an ordinary neighborhood of xi, already proved impossible when the residue field is uncountable. Projection is proper with no relative boundary; boundary composition over the locally separated disc gives partial X=pr_E^{-1}({xi}). Thus x is an actual analytic boundary point. A concrete field is C((t)) with its complete nontrivial t-adic valuation. For an extension of this uncountable-residue example, the same obstruction uses the uncountable image of the original residue field. The countable-residue construction proves that countability is the exact threshold for this particular boundary-spike target; it is not a sufficient condition for all disc targets.

Remaining original obligations. The positive higher-dimensional result n3 concerns saturated domains, not all nonsaturated affine sheaf germs. The full boundaryless higher-dimensional arbitrary-class problem, a sharp necessary-and-sufficient geometric characterization, general singularity and scalar-descent ranges, nonperfect fields, general nonseparable-field targets, nonseparated spaces and other analytic boundary configurations remain unresolved here. The obstruction is sequential and does not establish failure for nets. No known curve or invariant toric endpoint is identified with the original characterization.

The full proof and remaining obligations are retained in P02.3-argument.md, Sections 5–6, and P02.3-paper.tex. status.json has exactly id,status,exact_result,proof_file,concrete_gaps and marks P02.3 partial. python3 audit_artifacts.py reported all ten artifact checks true. Both final TeX passes returned zero and produced a 10-page PDF, with no diagnostics on the second pass. These are execution observations; the new proofs remain unverified drafts. Rerun python3 collect_sources.py; python3 make_paper.py; python3 build_paper.py; python3 audit_artifacts.py. The entire original target and its sharp general range have not been solved.

Artifacts: /workspace/research/campaigns/round-43/P02.3-public-source-decreasing-weakly-smooth/artifacts/codex-4O8X0J
