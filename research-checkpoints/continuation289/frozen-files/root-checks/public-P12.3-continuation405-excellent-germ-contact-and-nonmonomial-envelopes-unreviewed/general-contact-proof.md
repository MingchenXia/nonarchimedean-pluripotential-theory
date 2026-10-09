# n1. Finite contact certificates on every excellent germ

Support: G331, with its entire source, annotation, ledger and scope unchanged. No result of current401, B341 or E350 is a premise. We prove a general excellent-germ theorem, followed by an explicit monomial certificate. No general CE is assumed.

Let R be an excellent local ring whose reduction has positive dimension, a a proper primary gauge, and X=V_a(R). All ideals and semivaluations below are interpreted on the reduction, as required by G331. Let J be ANY proper primary ideal and q a positive integer. There is a FINITE nonempty set E_J of centred semivaluations on X such that the independently geometric classes of G331 satisfy
\[
 u\in D,\quad u(x)\le -v_x(J)/q\ (x\in E_J)
 \quad\Longrightarrow\quad u(v)\le-v(J)/q\ (v\in X).       \tag{G1}
\]
Thus for ANY continuous obstacle f, however nonmonomial, the conditions
\[
 f\ge H=-v(J)/q\text{ everywhere},\qquad f|_{E_J}=H|_{E_J} \tag{G2}
\]
give its greatest geometric D envelope P(f)=H in the actual geometric core. The same holds for any bounded-above upper semicontinuous f satisfying (G2). If f>=H-epsilon and f(x)<=H(x)+delta at all contacts, epsilon,delta>=0, then H-epsilon<=p(f)<=H+delta, without assuming positivity of p(f). These are sufficient conditions, not a density or necessity theorem for arbitrary obstacles.

We construct and prove the certificate first when R is an excellent NORMAL local domain. Normalize the actual primary blowup Bl_J(R). Excellence makes normalization finite, so Y is projective, normal and Noetherian. The pulled-back ideal J O_Y=O_Y(-E) is invertible and E is an ACTUAL effective Cartier divisor supported over the closed point. Normalization is only used to test inequalities; H itself already has its actual nef primary-blowup presentation on Bl_J(R). No cofinality among arbitrary models, new cone definition, or positivity on a merely numerical Weil list is invoked.

The effective divisor E has finitely many prime components E_1,...,E_s, all of height one and all lying over the closed point. The DVR orders nu_i=ord_{E_i} restrict to valuations of Frac(R) centred at m. They have 0<nu_i(a)<infinity and nu_i(J)>0: every element of m is in the height-one maximal ideal at that centre, and a,J contain primary powers. Normalize nu_i by nu_i(a) to define E_J. There is at least one component: J O_Y is nonunit at any point of the nonempty closed fibre, and a nonunit regular local Cartier equation has a height-one prime. Proper birationality gives the nonempty fibre over the positive-dimensional domain.

Let u=-v(I)/r be any rational unit-or-primary profile and assume its contact inequalities. After clearing q and r they say
\[
 \nu_i(I^q)\ge r\nu_i(J)\quad (1\le i\le s).              \tag{G3}
\]
For each generator t of I^q, (G3) gives the height-one section condition t in O_Y(-rE) at every E_i. At all other height-one points E has coefficient zero and t, being in R, is regular. The normal codimension-one section criterion on every affine open therefore proves
\[
 I^q O_Y\subset J^r O_Y.                                  \tag{G4}
\]
This is a direct proof of the needed finite Rees-valuation implication. No toric or test-ideal theorem, or Rees integral-closure criterion, is imported as an additional premise.

To evaluate (G4) at ANY v in X, including nonzero prime support p, pass first to its valued quotient field Frac(R/p). The generic point p differs from m, so Y is isomorphic there. Properness and the valuative criterion lift the map of its valuation ring to Y. The local generator of J O_Y at this valued centre has nonzero image, because J has finite value and its canonical generic trivialization is off the closed fibre. Pull (G4) to the valuation ring. The value of the invertible J ideal is exactly v(J), since the base generators generate it and one local coefficient is a unit. Hence qv(I)>=rv(J). This proves u<=H on EVERY support. No map from the original total fraction ring through p or subtraction of infinite values is attempted.

For a general excellent reduced R, its finite normalization is the semilocal union of normal local centres S_i. Every extension J S_i is proper primary for its marked centre. Form the preceding finite certificate at every S_i with gauge a S_i and restrict all these points to X_R. Their union is finite. A D_R function satisfying those downstairs tests has a positive pullback by G331, satisfying the tests on every normal centre. The normal theorem controls it on EVERY source point, and surjectivity of the boundary restriction controls it on every downstairs point. This proves (G1). The full conductor relation is respected: H is the evaluation of a DOWNSTAIRS primary ideal, so its pullback is constant on all fibres, including the infinite-conductor quotient stratum. No separate compatibility of arbitrary source extrema is asserted.

The C,D steps require no completion shortcut. For g in C with the contact bounds, approximate by a rational primary profile within epsilon and subtract a rational primary-gauge constant between epsilon and 2epsilon. This is again a rational profile after clearing denominators and multiplying by a power of a. It satisfies all exact contact bounds, hence is below H by (G3)--(G4). Let epsilon tend to zero. For u=inf_i g_i in D, finitely many strict contact tests and directedness select one term with g_i(x)<H(x)+epsilon at EVERY contact, even if u has poles there. Apply the C implication to g_i-epsilon and let epsilon tend to zero. This proves (G1) for ACTUAL decreasing nets, bottom and partial poles, without flattening, increasing closure or CE. H is an actual geometric competitor under (G2), so the envelope statement follows. The quantitative statement applies (G1) to competitors shifted by -delta and uses H-epsilon as an actual C competitor.

For nilpotent R this is exactly the reduction theory of G331, without unreduced intersection multiplicities. In dimension zero the boundary is empty and the unique empty envelope is direct. The unit barrier is zero and needs no contacts. Thus this theorem supplies a nonmonomial obstacle sector over EVERY excellent singular or nonnormal germ, including mixed characteristic and imperfect residue. It does not assert continuity for obstacles which do not satisfy (G2). Its conventional backgrounds are finite normalization, proper valuative criterion and normal codimension-one sections at their actual Noetherian excellent hypotheses. These are disclosed backgrounds, not new incoming grants.

Rerun delivery: python prepare_delivery.py; python verify_delivery.py. The entire explicit toric specialization follows in this same authoritative n1 note. Artifact paths and commands are evidence of retention, not theorem premises.

