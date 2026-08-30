# Primary-source locators

Date: 30 August 2026

This ledger fixes the source semantics and the exact versions used by the
candidate. It is not a verification receipt.

## The precise CLD question

The load-bearing French sentence in the second paragraph of CLD Remark
17.8.10 is:

> Par ailleurs, on pourrait vouloir généraliser le corollaire 17.8.9 à un
> espace strictement k-analytique propre possédant un modèle formel à fibre
> spéciale projective.

The inherited content of Corollary 17.8.9 is **parlinear metric implies
globally dpsh**. Therefore the precise English question is:

> If a proper strict analytic space admits a formal model with projective
> special fibre, is every parlinear metrized line bundle on it globally dpsh
> in the sense of CLD §17.8.5?

This is not the first question in the remark. The first question concerns a
continuous psh metric on a projective variety and asks whether it is globally
psh. The counterexample packet addresses only the second question.

The present live inventory and Chapter 72 paraphrase P08.2 as another
local-psh/global-psh approximation problem. That wording is not source-aligned
with the second paragraph of CLD Remark 17.8.10 and must not be silently used
when deciding whether the CLD question has been retired.

## Exact locators

1. **Chambert--Loir--Ducros, arXiv:1204.6277v2 (25 July 2025).**
   - §17.8.5, printed page 498: definitions of globally psh and globally
     dpsh metrics.
   - Corollary 17.8.9, printed pages 499--500: every parlinear metrized line
     bundle on the analytification of a projective variety is globally dpsh.
   - Remark 17.8.10, printed page 500: the two distinct questions.
   - Proposition 17.7.5(b), printed page 494: formal metrics are exactly the
     strictly integral parlinear metrics in the stated strict paracompact
     scope.
   - Theorem B.1.8(a), printed page 579 (proof continues on page 580): a
     coherent analytic sheaf admits a coherent model on a fixed formal model.

2. **Huybrechts--Macrì--Stellari, _Derived equivalences of K3 surfaces and
   orientation_, arXiv:0710.1645; Duke Math. J. 149 (2009), 461--507.**
   - §2.1: a formal deformation is smooth and proper over
     `Spf(C[[t]])`; the formal twistor construction is obtained from the
     twistor family by completion at the distinguished K3 fibre.
   - Definition 2.8 and Remark 2.9: very general Kähler classes and their
     existence.
   - Proposition 2.10(i), printed page 9: every line bundle on the induced
     very-general formal twistor space is trivial.

3. **Huybrechts--Macrì--Stellari, _Formal deformations and their categorical
   general fibre_, arXiv:0809.3201v2; Comment. Math. Helv. 86 (2011),
   41--71.**
   - Introduction: Raynaud's construction gives the rigid analytic generic
     fibre of the formal deformation.
   - Remark 2.2: the quotient category of coherent formal sheaves by
     parameter-torsion is equivalent to coherent sheaves on that rigid
     generic fibre.
   - Proposition 2.3, printed pages 5--6: morphisms in the categorical
     generic fibre are obtained by tensoring formal morphism groups from
     `C[[t]]` to `C((t))`. Together with the explicit infinitesimal
     computation `H^0(mathfrak X_n,O)=C[t]/(t^{n+1})`, this gives
     `H^0(X,O_X)=C((t))` and hence connectedness.

4. **Temkin, _Introduction to Berkovich analytic spaces_,
   arXiv:1010.2235v2 (16 December 2011).**
   - §5.2.2 and Definition 5.2.2.1: a formal scheme locally of finite type
     over the valuation ring has a strict analytic generic fibre.
   - Fact 5.2.2.4: formal properness passes to analytic properness, and
     formal smoothness passes to rig-smoothness. For the proper generic fibre,
     which is boundaryless, rig-smoothness is smoothness.
   - Exercise 5.3.2.3 states directly that an admissible formal blow-up is a
     rig-isomorphism; Fact 5.3.3.1 (Raynaud) gives the stronger statement that
     the generic-fibre functor is the localization by admissible formal
     blow-ups.

5. **Bosch, _Lectures on formal and rigid geometry_, Lecture Notes in
   Mathematics 2105 (2014).**
   - §7.4, Proposition 3: construction of the rigid generic-fibre functor.
   - §8.2, Proposition 6, printed page 186: an affine admissible formal
     blow-up is the adic completion of the corresponding scheme-theoretic
     blow-up.
   - §8.2, Proposition 7 and Corollary 8: affine charts of admissible formal
     blow-ups, invertibility of the transformed centre ideal, and
     admissibility of the blow-up.
   - §8.4, Proposition 2: an admissible formal blow-up induces an isomorphism
     on rigid generic fibres.

6. **The Stacks Project.**
   - Tag `00MC`, Lemma 10.97.3: the maximal-ideal completion of a noetherian
     local ring is faithfully flat.
   - Tag `031E`: a flat local extension of a regular local ring with regular
     closed fibre is regular. Applied to `C[[t]] -> A`, this makes every
     formal local ring of the smooth formal twistor model regular.
   - Tag `0AV3`: `Hom_A(M,N)` is reflexive when `N` is finite
     reflexive; with `N=A`, this proves reflexivity of the double dual.
   - Tags `0AVB` and `0AVC`: normal-domain characterizations of finite
     reflexive modules and the height-one-intersection description of the
     reflexive hull. In rank one this is the divisorial fractional ideal.
   - Tag `0AG0`: a regular local ring is a unique factorization domain.
   - Tag `0EBM`: rank-one coherent reflexive modules on a normal integral
     locally Noetherian scheme are classified by its Weil divisor class
     group. Locally, this combines with `0AG0` to make the reflexive hull
     free of rank one.
   - Tags `052P` and `0804`: the blow-up algebra is the Rees algebra and
     the blow-up is its relative `Proj`, with the standard affine blow-up
     charts.
   - Tag `01OF`, Lemma 31.33.3: scheme-theoretic blow-up commutes with flat
     base change. Lemma 31.33.4 in the same section says that the transform
     of the centre ideal is invertible and cuts out the exceptional effective
     Cartier divisor. These scheme statements are applied to the local Rees
     construction before adic completion.

7. **Gubler--Rabinoff, _Classically psh and pluriharmonic functions on
   Berkovich spaces_, arXiv:2506.13548v2 (17 September 2025).**
   - §1.2, printed pages 2--3: CLD-psh functions are classically psh.
   - Theorem 6.1, printed page 30: local maximum principle for classically
     psh functions at an interior point.
   - Proposition 7.2(2), printed page 34: `log|f|` is pluriharmonic for a
     global analytic unit `f`.

## Source-byte fingerprints used for this dossier

- CLD v2 PDF: `5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719`
- HMS orientation PDF: `99d374cd4678e3a5dd75522fed90c6b8637b8ba080f47e710c2e243e1b62e2f0`
- HMS formal-fibre PDF: `3e9beae6c911051535230fb560becfe321e76a5dce9a203aecb8efafe22a5868`
- Gubler--Rabinoff v2 PDF: `83ca9a19394f44bb2e4e1aa316de95938f311acd53a00fe250fa0f605184b726`
- Temkin arXiv:1010.2235v2 PDF:
  `b8a7ac414e98fdd46db3961c43e08068203aec7225457f455dc077f87b32b914`
- Bosch 2014 PDF:
  `2f39e9e9bc71e34ce255278f09291412d7e0a9dadff673e4a2b8484df4685d7f`

The fingerprints authenticate the local copies consulted for the candidate;
they are not hashes of files distributed in this packet.
