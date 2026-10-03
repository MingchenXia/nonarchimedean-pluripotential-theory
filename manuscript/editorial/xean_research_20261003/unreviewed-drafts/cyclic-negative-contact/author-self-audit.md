# Author audit of the cyclic-product counterexample

This is a self-audit of an unverified proof, not an independent review.
The original P05.2 classification remains open. The exact result is the
negative contact integral -8 at the already regularizable actual raw
envelope of the specified cyclic triangle-square obstacle.

1. The carrier is the prescribed embedded triangle, all primitive bounded
   edges have length one, and all three leaf directions and unit weights
   are retained. The actual ambient lattice is Z^2 direct sum Z^2. At each
   graph junction the outgoing vectors sum to zero and a determinant-one
   pair verifies the saturated span. The product top weights are one.
2. Gamma is the restriction of max(h,rho/4-1), where h is the difference
   L1 norm. It is a maximum of twenty rational ambient affine functions,
   so its domains are finite rational spatial polyhedra. All carrier
   cells are pointed. This example uses rational coefficients, which
   obey the real scalar convention without irrational-wall arguments.
3. Positive growth is proved on every nonzero recession vector of every
   affine reference cell by the lower bound gamma>=rho/4-1. It includes
   both graph ends simultaneously, rather than only pure factor rays.
4. The actual PC proof is Jensen for the global ambient convex function.
   It tests every real centre and every admitted rational endpoint PCC,
   on every rational structure, regardless of remote endpoints.
5. PAPC is checked directly against arbitrary nonnegative real local
   cycles, every positive dimension and every ordinary open. Subtract an
   active ambient supporting affine piece at a tested facet; each inward
   normal term is nonnegative, and all tangential terms cancel.
6. The obstacle max(1-10rho,0) is bounded, continuous and rational PA.
   Its nonseparable mixed difference at the four points based on A and
   (1/10,0) is one. Its permitted domain is independent of the reference's.
7. The three rational diagonal points (ui,ui)/4 with coefficients 1/3
   form a genuine original-product PCC centred at (A,A). At those
   endpoints gamma=u=f=0, so every raw competitor has value <=0 at the
   origin. At the origin the obstacle is one and the candidate is zero.
8. No other reference-domain vertex has rho<1. The local active domains
   and carrier faces there are homogeneous, and nonzero points can be
   scaled slightly both ways. All other operator vertices have u=0.
   This structural proof does not depend on the computed vertex list.
9. A complete pointed rational polyhedron generation proof is in the main
   file. It makes the vertex bounds propagate to every real point using
   same-cell PCCs with rational vertices and far rational recession
   endpoints. Their coefficients may be real. The O(1) competitor error
   tends to zero as the endpoint distance tends to infinity. No raw
   continuity, source locality, branch unfolding or cycle cutting is used.
10. Gamma itself is a global competitor, giving exact raw equality in
    both directions. Gamma+1/j is an explicit decreasing uniform PAPC
    regularization in its reference growth class with identical measures.
11. The primitive-normal divisor, refinement compatibility and balancing
    of the first divisor are reconstructed in dimension two. No external
    intersection theorem is imported. All actual plane indices are
    retained, including tangential corrections in the first divisor.
12. At the origin all twelve actual local top cones and nine rays are
    listed. Their indices are one. First weights on first/second axes are
    2,2,0, and on diagonal rays 2,2,4. Applying the second divisor gives
    eight. The tight zero-curve PCC does not imply zero top coefficient.
13. The complete operator has support at the reference structure's
    vertices. At all other such vertices the gap vanishes. Refinement
    creates no new nonzero coefficient in the obstacle support. Thus the
    entire integral, not merely one term, equals -8. The PA operator and
    its constant-shift approximants have no extra boundary atom.
14. The exact finite program independently enumerates 53 top domains,
    12 vertices, six positive and six zero atoms, total mass 46, and
    complete integral -8. Its maximum actual saturated cone index is
    sixteen. It verifies each incident domain, every first-cycle
    balancing equation and the second coefficient. These are finite
    execution results, not proof of arbitrary PCC inequalities or a
    substitute for the separate mathematical raw-envelope argument.
15. The root rectangle-roof diagnostic was recomputed, giving the exact
    defect 1/12. It invalidates the coarse max-closed nodal roof scheme
    only. The actual counterexample is separately constructed and proved.
16. The earlier conical difference-norm calculation is acknowledged and
    reconstructed. Its verdict and global cone support are not used as
    premises. The predecessor's imposed-contact certificate is not
    promoted to an arbitrary-obstacle theorem. Its tight-witness logic
    here proves a value bound, while mass is computed independently and
    is positive, producing a substantively different negative conclusion.

The reference is flat on the balanced diagonal curve near the origin.
The result does not address an additional strict-convexity hypothesis,
all real references on this product, or all other raw envelopes. Original
classification, all-reference regularity and P06.2 are unclaimed.

Source snapshots are read-only copies. Newline indexing uses split('\n'),
never splitlines. Identifiers and complete proof endings were checked.
No subagent, network, older write, SQL operation or heavy computation was
used. Successful execution, hashes and compilation establish no review
verdict, theorem grant, priority or mathematical certification.

The initial PDF subprocess completed a TeX pass, but its wrapper failed to
decode a Latin-encoded diagnostic byte as UTF-8. The original TeX log is
preserved in build-initial-decode-failure.log. The wrapper now records
decoded diagnostics with replacement for invalid bytes; the authoritative
TeX/PDF bytes are unaffected. The final document was then compiled twice
with both complete logs and return codes retained.
