# Source and hypothesis matrix

Date: 30 August 2026

Status: quarantined research candidate. No row is a verification receipt.

| Use in the candidate | Primary source or internal argument | Literal scope and obligation |
|---|---|---|
| Exact meaning of the second CLD question | CLD Remark 17.8.10 read with Corollary 17.8.9 and §17.8.5 | The inherited conclusion is global **dpsh** for every parlinear metric. It is not a second local-psh/global-psh question. |
| Very-general formal twistor deformation | HMS, §2.1, Definition 2.8, Remark 2.9 | Starts with a complex projective K3 surface; gives a smooth proper formal deformation over `C[[t]]` with the chosen K3 as special fibre. |
| Triviality of formal line bundles | HMS, Proposition 2.10(i) | Applies to the formal twistor space induced by a very general Kähler class; it says every line bundle on the formal space is trivial. |
| Rigid/Raynaud generic fibre | Temkin §5.2.2 and Fact 5.2.2.4; HMS formal-fibre paper, Introduction and Remark 2.2 | The finite-type formal model produces a strict analytic generic fibre; formal properness gives analytic properness, and formal smoothness gives rig-smoothness. Properness makes the generic fibre boundaryless, so it is smooth. |
| Connectedness of the generic fibre | Direct infinitesimal `H^0` calculation; HMS formal-fibre paper, Remark 2.2 and Proposition 2.3 | The exact sequences for the thickenings, together with `H^0(S,O_S)=C` and `H^1(S,O_S)=0`, give `Γ(mathfrak X,O)=C[[t]]`; tensoring morphisms to the categorical/Raynaud generic fibre gives `Γ(X,O_X)=C((t))`, so there is no nontrivial idempotent. No affine-domain shortcut is used. |
| Coherent model on the fixed formal model | CLD, Theorem B.1.8(a) | Applies to every coherent analytic sheaf on a strict paracompact analytic space with a chosen formal model. Used for an arbitrary analytic line bundle on `X`. |
| Removal of parameter torsion | Direct noetherian module argument | The quotient has the same generic fibre and is `t`-torsion-free. The proof then checks full module torsion-freeness, rather than assuming it. |
| Formal local rings are regular | Stacks tag `031E` | For a formal local ring `A`, the map `C[[t]] -> A` is flat and the closed fibre `A/tA` is regular because the special K3 fibre is smooth; hence `A` is regular. |
| Rank-one reflexive hull is invertible | Stacks tags `0AV3`, `0AVB`, `0AVC`, `0AG0`, and `0EBM`, applied formal-locally | The double dual is finite reflexive and rank one; regular local rings are UFDs; rank-one reflexive modules have zero local divisor class and are free. |
| Reflexive hull keeps the analytic generic fibre | Direct localization/dual argument | Finite duals commute with localization, and the original generic fibre is already locally free of rank one. |
| Admissible blow-up leaves generic fibre unchanged | Raynaud localization as Temkin Fact 5.3.3.1; Bosch §8.4 Proposition 2; direct use of `J[1/t]=O[1/t]` | The centre ideal contains `t`, hence becomes the unit ideal after inverting `t`; the cited results identify the resulting generic-fibre morphism as an isomorphism. |
| Passage to completed local coordinates | Stacks tag `00MC` and Lemma 31.33.3 in tag `01OF`; Bosch §8.2 Proposition 6 | The maximal-ideal completion is faithfully flat, scheme blow-up commutes with that flat base change, and the formal blow-up is the adic completion of the scheme blow-up. Thus the chart equations, reduced components, and multiplicities can be checked in `C[[t,x,y]]`; reduction modulo `t` is unchanged by the final adic completion. |
| The metric-defining model also has projective special fibre | Relative `Proj` of the reduced Rees algebra; Stacks tags `052P`, `0804`, and `01OF` for the local algebra | The special-fibre morphism is projective over the original projective K3 surface. Globally its special fibre is `Bl_p(S) ∪ P^2`, meeting along `P^1`; hence the special fibre is projective. |
| Formal metric is parlinear | CLD, Proposition 17.7.5(b) | The proper strict analytic space is paracompact. The metric arising from `O(-E)` is strictly integral parlinear. |
| Exceptional metric is nonconstant | Direct regular-local blow-up and divisorial-norm computation | On the `x`-chart, `t=xT`, `E=(x)`, and `S'=(T)`, so `div(t)=S'+E`. The `O(-E)` frame is `x`, and `1=x^{-1}x`, giving metric values `1` and `|t|^{-1}`. Thus `log||1||` has values `0` and `-log|t|`; the CLD weight `log||1||^{-1}` has values `0` and `log|t|`. |
| CLD psh implies classically psh | Gubler--Rabinoff, §1.2 | Applies to the smooth CLD-psh weights used in global-psh approximation. |
| Maximum principle | Gubler--Rabinoff, Theorem 6.1 | `X` is connected and boundaryless; compactness supplies a maximum. The maximum locus is open and closed, hence the weight is constant. |
| Global analytic units have constant absolute value | Gubler--Rabinoff, Proposition 7.2(2), plus Theorem 6.1 | `log|f|` is pluriharmonic and therefore classically psh; compact connected boundaryless maximum principle makes it constant. |
| Global-dpsh constancy on `O_X` | Definition 17.8.5 + `Pic(X)=0` + preceding two rows | Both globally psh factors analytically trivialize and have constant weights; the isomorphism contributes only a global unit of constant absolute value. |

## Explicit non-use declarations

- The candidate does not use the user's Deligne-pairing paper.
- It does not claim that the exceptional formal metric is psh.
- It does not address the first paragraph of CLD Remark 17.8.10.
- It does not identify globally dpsh with globally psh.
- It does not infer analytic Picard triviality directly from formal Picard
  triviality; the coherent-model/reflexive-hull bridge is supplied in full.
- It does not use algebraization of the formal twistor deformation. In fact,
  the point of the example is that its proper strict generic fibre has a
  projective-special-fibre formal model without lying in the algebraic scope
  of CLD Corollary 17.8.9.
