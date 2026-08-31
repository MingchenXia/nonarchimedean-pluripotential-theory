# Source and scope audit

Date: 2026-08-31. Main author checked the current manuscript, the primary
HTML sources below, and parsed primary PDF text. Web rendering of the DX22
pages returned cache misses, so no visual PDF audit is claimed here.

## Definitional inputs

1. Mesquita-Piccione, arXiv:2409.06221v2, Definition1.3.1:
   <https://arxiv.org/html/2409.06221v2#S1.SS3>.
   The spectrum evaluates coherent ideals in [0,+infinity], with the
   topology of pointwise convergence. Only this definition is needed;
   neither divisorial density nor the dual-complex comparison is used.
2. Darvas--Xia--Zhang, arXiv:2302.02541v3, Section2.2:
   <https://arxiv.org/html/2302.02541v3#S2.SS2>.
   Test-curve levels decrease with the real parameter and have a finite
   terminal parameter. This is the direction of monotonicity needed in
   the finite left-mesh estimate. No continuity of multiplier ideals in
   that parameter is required.
3. The same source, formula(28), Definition3.3, and the paragraph following
   the definition:
   <https://arxiv.org/html/2302.02541v3#S3.SS2>.
   These specify the inverse system, its I-envelope transitions, and its
   common terminal parameter. Preservation of integer multiplier ideals
   is the already established Ch71 transition input; primary item5 below
   supplies its full compact-Kaehler source, rather than deriving it
   solely from the displayed definition.
4. Xia, arXiv:2312.17150v3, Section3.3.2, formula(3.8):
   <https://arxiv.org/html/2312.17150v3#S3.SS3.SSS2>.
   This is a source for the raw multiplier-ideal formula in the smooth
   projective line-bundle setting. Its positivity conclusion is NOT
   imported into the general compact-Kaehler setting.
5. Darvas--Xia, The closures of test configurations and algebraic
   singularity types, Advances in Mathematics397 (2022), 108198:
   <https://research.chalmers.se/publication/528300/file/528300_Fulltext.pdf>.
   Section2.4 explicitly resets its scope to compact Kaehler manifolds
   and pseudoeffective background forms (printed p19). Proposition2.18(ii)
   (printed p22) proves I-equivalence with the I-envelope. The paper's
   ample introductory setup does not narrow this section.
6. Demailly--Ein--Lazarsfeld, A subadditivity property of multiplier ideals:
   <https://www.math.stonybrook.edu/~roblaz/Reprints/Demailly.Ein.Laz.Subadditivity.pdf>.
   Theorem2.6(ii) (printed p149) supplies analytic subadditivity on complex
   manifolds. Adding a smooth local function does not change multiplier
   ideals, so the local psh formulation applies to quasi-psh functions.
   That source uses exp(-2 phi), whereas the book uses exp(-phi);
   substituting half the book potential in both source inputs gives
   exactly the subadditivity inclusion used here.

## Existing book inputs

- Ch58, eq:ts-evaluation: topology on all ideal characters, with +infinity.
- Ch71, prop:pseff-ideal-valuative-basic: multiplier-ideal subadditivity
  and the extended-real Fekete formula. The elementary sequence argument
  is repeated in the candidate proof; coherence and subadditivity remain
  the standard complex multiplier-ideal inputs.
- Ch71, thm:pseff-perturbation-independent-transform: exact transition
  ideal equality at every positive integer, usable at every semivaluation.
- Ch72, prob:frontier-mp-pseff and inventory P14.2: the target is USC of
  the raw transform in a general compact-Kaehler pseudoeffective class.

## Newly proved steps requiring review

- A finite left mesh bounds the parameter supremum within its mesh size
  after truncating from below; the negative tail and excluded endpoint
  are both explicitly handled.
- The resulting infimum formula proves USC even where all values are
  minus infinity. Dense-parameter determination uses only monotonicity.
- Truncating the ideal limit at each finite mesh produces continuous
  majorants. Finite running minima over pairs (N,M) give an explicit
  decreasing sequence with the exact raw function as limit.

## Limits

No use of an arbitrary supremum theorem for psh functions, a divisorial
extension theorem, a Gauss identity at nondivisorial points, MP model
nefness, or a positive regularization theorem occurs. In particular the
new sequence must never be cited as settling P14.3. No open atom is retired
until both required verification gates pass.
