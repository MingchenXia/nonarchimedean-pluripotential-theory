# P21.3 v70 open-nonheredity audit

Date: 20 September 2026.

## Result

The packet proves that whole-space ordinary CLD-smooth zero-current
regularity is not inherited by arbitrary ordinary open subsets. The
counterexample is a smooth proper surface

X = (P^1_K)^an x_K D^an

with only constant global continuous zero-current functions, but with an
ordinary product open carrying a continuous zero-current function which is
not ordinary CLD-smooth. A constant elliptic curve over
K = completion(overline(C((t)))) gives an explicit instance.

This validates the stage-local premise in the v69 annular-tower theorem:
the premise is necessary for that proof route and cannot be replaced by a
whole-space conclusion on the intermediate base. It neither proves nor
disproves the full Bedford--Taylor statement P21.3. The active inventory
therefore remains 46 atoms in 14 formal problem environments.

## Dependency audit

- Proper-smooth-curve-bundle descent forces every global zero-current
  function on X to descend to (P^1_K)^an; curve comparison and the maximum
  principle then make it constant.
- The residual quotient H_D/F_D = Pic^0(D_x) tensor R supplies a local
  Thuillier harmonic germ which is not ordinary CLD-smooth.
- Gubler--Jell--Rabinoff harmonic functoriality pulls the germ to the product
  open. Their published Corollary 7.15 gives vanishing of its Hessian current
  after goodness, separatedness, strictness, and boundarylessness are
  checked.
- Pullback along the constant section detects the failure of ordinary
  smoothness.
- The exact mixed-tower statement identifies a locally trivial proper
  smooth connected curve bundle as its fourth allowed stage. Thus the
  counterexample occurs on an exact intermediate base covered by v69.

No pullback of an arbitrary current, no open-heredity assertion, and no
general higher-dimensional regularization theorem is used.

## Verifier history

The first local gpt-6-astra/xhigh run returned final wrong with zero
critical errors and two gaps. It correctly rejected a comparison between
two different harmonic notions and noted that the exact four-stage list had
not been supplied. The mathematical construction was otherwise
unchallenged.

The repaired run supplied the published harmonic-to-zero-current
corollary, checked its ambient hypotheses, and attached the exact mixed
transfer and v69 statements. It returned final correct, checked item
pi_19ea66139deaefc834ba304a, with zero critical errors and zero gaps.

## Second-pass writing audit

The required second pass removed the misleading current-based harmonic
definition, made the exact-stage membership explicit, and tightened the
scope sentence to say that the result is a counterexample only to the
open-heredity shortcut. The Mingchen TeX audit reports zero errors and zero
warnings on the statement, proof, and materialized dependency file.
