# Exact source application ledger and recursive foundations

A. Chambert-Loir and A. Ducros, Formes differentielles reelles et courants sur les espaces de Berkovich, arXiv:1204.6277v2; retained 25 July 2025 cover, internal 29 July 2025 0h06 title.

The 31 full literal source units, their LF intervals, hashes, and immediate proof bodies are retained in full-literal-source-ledger-LOCALONLY.json. The following statements specify exactly what is applied; source errors are excluded or repaired by the independent arguments above.

## S01: CLD 1.3.6--7, LF 1200--1252

Jd'=d''J, Jd''=-d'J, J^2=(-1)^(a+b), D commutes with J. Both differentials obey the total-degree graded Leibniz rule on superforms.

Used for the antisymmetric cross term in the smooth multiplier identity and the two relative-factor derivative relations. Applied in ordinary unit moment charts; the exterior algebra is independent of the field.

Read the statement, calculation of the J signs, and complete 1.3.7 rule. Current rules are independently obtained by signed transposition, not asserted from a nonsmooth form.

Literal body: inputs-LOCALONLY/S01.txt; 3472 bytes; SHA-256 80173cb9e3c2d2f9f5d59c14dd54332b39655d0b0f1d889ac2685725bb56a511.

## S02: CLD 3.3.4--12, LF 3715--3803

G-forms restrict to smaller paralin domains, pull back under affine maps, and have ordinary support. A type (a,b) form vanishes where tropical dimension is below max(a,b). Differentials and exterior products are compatible with restriction.

Used to extend compactly supported ordinary forms by zero and to derive the analytic support theorem with S12/S13.

The displayed 3.3.6 proof writes d_K where its statement and argument require d_trop. The printed 3.3.10 commutation exponent is inconsistent with generator algebra: the independent proof uses total degrees (a+b)(c+d). Page 80 pixels were inspected.

Literal body: inputs-LOCALONLY/S02.txt; 6271 bytes; SHA-256 27ed82bac34a4485a5d132ba8a9cd45062c7a398f642373ea7304e8263876151.

## S03: CLD 6.2.1--9, LF 7070--7150

On locally differentially separated tropical spaces, compact sets inside opens admit smooth nonnegative plateaus with compact support in that open. Compact continuous scalars are uniformly approximable by compact smooth scalars; localization and partitions have the stated paracompact hypotheses.

Only the compact, finite localization consequences are used on good separated ordinary domains. No paracompactness of an arbitrary entire open is assumed.

The complete plateau construction and Stone-Weierstrass density proof were read. Scalar smooth density does not give zero-Hessian density.

Literal body: inputs-LOCALONLY/S03.txt; 4772 bytes; SHA-256 a6076aba5050c5b83aae091f054a7d260a5b592693af32431625a9119b2b173c.

## S04: CLD 6.5.1--3, LF 7340--7385

A compact symmetric diagonal form whose support is contained in a paracompact locally differentially separated open is a difference of two compact middle-positive forms. Compact supports on almost-good analytic spaces satisfy that support condition.

Apply 6.5.2 to the prescribed ordinary open O itself, then extend compact outputs by zero to N. Good ordinary domains are almost good. The output supports remain in O, though they can exceed the original support.

The proof uses a finite chart localization and E/S16 middle-positive coefficient decomposition. No strong-positive domination is substituted.

Literal body: inputs-LOCALONLY/S04.txt; 3250 bytes; SHA-256 fe5fc249ed619478fa56cb89c5a8afad1632f7e8174bb10d698a76bfc7134c9f.

## S05: CLD 7.1.1--9, LF 7652--7831

Compact test topologies define currents; restriction is by zero extension of compact tests. Currents form a sheaf on locally differentially separated spaces, and support means vanishing on the complementary open.

Only ordinary restriction, support, and finite gluing of an already constructed current are used. Analytic hypotheses are supplied by S13/S14.

No gluing of unrelated changing currents, or pullback of a nonsmooth current, is imported.

Literal body: inputs-LOCALONLY/S05.txt; 12512 bytes; SHA-256 98486d39b381d6ae79277965f7d01ffac5e2892d123cf4aac2159fbc70a589cb.

## S06: CLD 7.2.1--4, LF 7916--7955

A positive current is symmetric and nonnegative on middle-positive complementary tests. If T and -T are positive, T=0 by positive decomposition. Positivity is local on locally differentially separated spaces.

This is exactly the positivity convention throughout the review. Fixed-current scalar products and smooth middle-positive factors preserve it.

Weakly positive currents test the strong cone and are not silently substituted for the positive currents of this assignment.

Literal body: inputs-LOCALONLY/S06.txt; 3080 bytes; SHA-256 4880c086da86a27c43b343644e1beae57b05110cf43c83cc85ce47eb153d6953.

## S07: CLD 7.2.7--12, LF 7973--8076

Positive complementary tests yield positive scalar Radon measures; multiplication of a positive current by a locally integrable scalar is defined by coefficient measures. Positive currents have order zero and compact signed coefficient measures.

Signed measures are independently obtained by SAME-open middle-positive decomposition and scalar density; multiplication uniqueness and compact support of those measures are proved in n1.

The printed 7.2.9 strong-positive domination step is false in middle degree. It is replaced by bounded coefficient domination in the MIDDLE PSD cone for the given middle-positive current. Page 162 pixels were inspected. No general weak-positive recognition theorem is used.

Literal body: inputs-LOCALONLY/S07.txt; 7415 bytes; SHA-256 b5e1634d0600f2204eb2c87cc1bdc081e2f6156e5b62360f643b43e10a882c4c.

## S08: CLD 7.3.1, LF 8098--8104

The canonical integration current delta_X=[1] is strongly positive, hence middle-positive, on a calibrated tropical space.

Applied to the canonical analytic calibration from E06-E13 and S14. Boundaryless closedness comes from S09/Stokes.

This supplies only the reference integration current, not a classification of arbitrary positive currents.

Literal body: inputs-LOCALONLY/S08.txt; 637 bytes; SHA-256 18a13b42524a7681021fadbbc0ac0b180abc770f5b81189634f3077c1f8aa317.

## S09: CLD 7.7.1--8, LF 9307--9431

Current derivatives are signed transposes: d'=(-1)^(a+b+1)b', similarly d''. Squares vanish, d'd''=-d''d', D commutes with J, and derivatives commute with ordinary restriction. Boundaryless integration is doubly closed.

Directly proves correctly complementary D-duality and full total-degree smooth-form/current Leibniz. Both equations d'T=d''T=0 are retained.

Printed 7.7.5 uses an incorrect complementary test index; printed 7.7.7 mixes degree/dimension labels. Independent typed calculations repair these. Nothing assumes S=hT is closed.

Literal body: inputs-LOCALONLY/S09.txt; 6528 bytes; SHA-256 943283615dc00b4389f5c63606689cddd13741d9b0306c6b83e55cef98f47f6d.

## S10: CLD 11.1.7, LF 14983--15012

Analytic spaces have compact domain neighborhood bases, and good spaces have affinoid neighborhood bases; ordinary opens are analytic domains. Topological separation gives Hausdorff support manipulations.

Used to choose affinoid neighborhoods inside the locally analytic-locus description and relatively compact ordinary subopens.

This does not assert all ordinary opens are globally affinoid, strict polycylinders, or paracompact.

Literal body: inputs-LOCALONLY/S10.txt; 2506 bytes; SHA-256 6efe2fa15d3425138409717a7512d91909e0b03be4f3c3e56e267d4bcdfefabd.

## S11: CLD 11.2.3, LF 15303--15348

Analytic dimension is defined by strictification and the resulting Krull dimension and is unchanged under complete scalar extension or nilreduction. It equals sup_x d_K(x). Thus for a d-dimensional analytic space d_K(x)<=d; the same bound applies on an analytic subspace with its induced dimension.

Combined with S12 and the exact S13 support theorem, it removes analytic loci with dimension below the test degree.

The invariant is graded residual transcendence degree, not the dimension of a projected skeleton or an ambient moment-coordinate count.

Literal body: inputs-LOCALONLY/S11.txt; 3611 bytes; SHA-256 0f8682d72514fa5517e844260d1a8920ebac3719673c8486fbc76f54d2c99492.

## S12: CLD 12.4.2, LF 17459--17464

For an analytic moment, the local tropical dimension d_trop(x) is at most d_K(x).

Used only for analytic support, not to bound the number of moment coordinates by analytic dimension.

Read the complete short proposition; recursive graded analytic dimension foundations are imported honestly.

Literal body: inputs-LOCALONLY/S12.txt; 410 bytes; SHA-256 a07c43b58b7609adc73e193077e3217257793c6419f503426ccd7987eafcb558.

## S13: CLD 15.2.1--9, LF 21605--21696

On a topologically separated analytic space, a type (a,b) G-form has support in d_K>=max(a,b), and its support misses locally Zariski closed analytic loci of dimension below max(a,b). Good topologically separated spaces are locally holomorphically and differentially separated; compact supports have the prescribed separation/plateau properties.

Ordinary forms are G-forms; all spaces used are good separated. The dimension conclusion needs an actual analytic locus or the stated pointwise d_K inequality.

Read the entire immediate proof: separating seminorms by an analytic function, smooth logarithmic separators, zero extension near zeros, then finite compact localization. No global properness or nontrivial valuation is added.

Literal body: inputs-LOCALONLY/S13.txt; 5878 bytes; SHA-256 027ba59bb9616e1bebf666fb5b0bf4644f143cfeaec2915dffe657d75fd10b25.

## S14: CLD 15.7.1--2 and surrounding definitions, LF 22097--22148

A topologically separated pure n-dimensional analytic space carries the canonical calibrated tropical level-n calculus, independent of an admissible moment choice and compatible with analytic domains.

This installs the ordinary analytic CLD calculus on each specified ordinary open and retains nilpotent integration multiplicities.

No equivalence with harmonic tropicalizations, weak smoothness, or strong-current multiplication is inferred.

Literal body: inputs-LOCALONLY/S14.txt; 2961 bytes; SHA-256 4d3c398c54e57c876c7940b857171447e9c3a9a1fa86deed8317b928eb0402ef.

## S15: CLD A.2.1--6, LF 29090--29195

In a Hausdorff locally compact space, a sheaf of continuous functions admitting local plateaus and vector-space operations yields compact plateaus in prescribed opens and compact scalar density by Stone-Weierstrass, under the stated local separation assumptions.

The analytic smooth sheaf meets these assumptions by S13. Only compact and finite localizations are required.

The real scalar density theorem is imported with its ordinary topology; no harmonic approximation conclusion follows.

Literal body: inputs-LOCALONLY/S15.txt; 8086 bytes; SHA-256 e969de709974fe7a49a2fdf6a9f3fabd7fc09264d99bbbf57a92bb6ffa5104d6.

## S16: CLD 1.10.1--2, LF 2635--2684

A symmetric diagonal smooth form on a paralin domain is a difference of two middle-positive smooth forms. On a compact coefficient domain, a finite constant multiple of a standard metric power bounds both signs.

The independent proof uses exactly the compact constant-majorant argument and E01/E02 matrix positivity. This supplies SAME-open compact decomposition.

The problematic noncompact scalar majorant/composition wording in 1.10.2 is not used. Strong-positive generators need not span all symmetric forms.

Literal body: inputs-LOCALONLY/S16.txt; 3726 bytes; SHA-256 174778258977e10435e8ca8564510bacbe082e1059fdc13d70ad208457d4e029.

## E01: CLD 1.2.6 matrix interpretation, LF 886--936

A symmetric (a,a) superform, written using sigma_a xi_I wedge Jxi_J, is middle-positive exactly when its real symmetric coefficient matrix on the a-th exterior coefficient space is PSD.

Gives matrix order units lambda^a, cross-block estimates, and the Plucker strong-span obstruction. The ambient vector space is the actual moment-coordinate space.

The complete cone/matrix discussion was read. The finite Plucker diagnostic is corroboration; the universal annihilator is proved by w wedge w=0.

Literal body: inputs-LOCALONLY/E01.txt; 3678 bytes; SHA-256 1fe60dd9c2ce6dc389b7ee0e65fe66efe50ded30f09368ee34b1ea4ba6dc089e.

## E02: CLD 1.2.11--13 full proofs, LF 994--1115

Linear pullback preserves all three form cones; surjective pullback detects them. Wedges of middle-positive forms are middle-positive. A positive-definite (1,1) form has powers in the interior of the middle cone, but only relative interior of the strong cone.

Used for middle order units, energy-form positivity, smooth factors, and FIRST-JET linear pullback of the formal cross-block inequality into genuine refined analytic-unit charts.

Read all statements and immediate proofs. The formal covector y used for algebra is not an analytic unit, and no current is pulled back.

Literal body: inputs-LOCALONLY/E02.txt; 8779 bytes; SHA-256 9e74fc180f402213b32c53643ffbc68db1bb8dedc4a61d1b27e44b132007ffc5.

## E03: CLD 1.3.3--4, LF 1165--1188

J interchanges primed and double-primed generators with the prescribed sign, and exterior multiplication commutes with sign determined by total degrees.

Used with S01/S09 for every sign in D(gT), graded current Leibniz, and the relative-factor identity.

No ungraded or bidegree-only commutation convention is used.

Literal body: inputs-LOCALONLY/E03.txt; 1629 bytes; SHA-256 701bbaac2944b257b4c458c30244b288fb2a3b16f3e67c76f7242a0187af9afb.

## E04: CLD 5.8.1--6, LF 6733--6833

A top-degree G-form on a calibrated tropical space has a measure defined by local chart integrals; compact forms integrate finitely, independently of chart localization, and standard torus calibration is Lebesgue calibration.

Used for canonical analytic integration and the explicit detecting integral on the actual analytic torus.

Calibrated multiplicities and paired positive orientation are retained, not replaced by probability normalization.

Literal body: inputs-LOCALONLY/E04.txt; 6132 bytes; SHA-256 119f11b8f9f3b3137230f44f8a108dca924608b4ec2e3f000c6f80641d3d15c1.

## E05: CLD 8.5.3--8.6.7, LF 10287--10397

8.5.3 gives a smooth-factor identity for closed symmetric currents; 8.6.2 defines BT on every open; 8.6.3 gives locality; delta_X is BT; closed positive smooth-factor BT transfer is stated in 8.6.5.

These are reconstructed with complementary indices. The review independently proves relative closedness transfer and fixed-current scalar/form-net limits. The original class consists of individually admissible continuous psh pairs.

8.5.3 contains a degree/dimension indexing mismatch. 8.5.5 uses generated CPsh, which is not assumed to be the full original class. Literal 8.6.7 drops closedness and is false, as the actual analytic torus diagnostic proves. General changing-current 8.6.6 is not used as a density theorem or a substitute for fixed-T measure continuity.

Literal body: inputs-LOCALONLY/E05.txt; 7383 bytes; SHA-256 c4d0c9b2038f58926aa06129df3f86a26245b06b40c02d0bc0c154fdec4964dd.

## E06: CLD 14.2.1--2, LF 20322--20356

Near a generic tropical point, a suitable projection of a moment to an n-dimensional split torus is finite flat; canonical calibration is defined through that finite flat degree and the primitive lattice covolume.

Supplies the generic construction of analytic moment calibration and degree-one normalization for the identity torus moment.

The stated projection and generic-point conditions are preserved. No arbitrary current is normalized or base changed.

Literal body: inputs-LOCALONLY/E06.txt; 2708 bytes; SHA-256 5e0d772da08f99241073ee9fc0c77d5a1a2ec4855a947896696c033de9cc17fa.

## E07: CLD 14.3.1--5, LF 20722--20830

Canonical calibration is independent of the finite-flat projection and admissible unit-moment choice, using refinements by a common moment and the degree computation on cells.

Justifies appending actual analytic units in ordinary presentations without altering upstairs integration currents or Artinian weights.

Read full construction and proof. This is form/integration compatibility, not faithful ascent/descent for arbitrary currents.

Literal body: inputs-LOCALONLY/E07.txt; 8297 bytes; SHA-256 9a215b5ad4120698b0ddfb99a0650da9f067a004d137d475d9f12fc5e1e57a41.

## E08: CLD 14.4.1--2, LF 20868--20923

For a finite analytic map, pushforward of canonical tropical calibration equals canonical target calibration multiplied by the appropriate local/generic degree, on the stated calibrated cells.

Together with E11/E12 this fixes nilreduction and generic nonreduced integration weights.

Only finite calibrated integration is transported. No use of noninjective tropical equality to decide upstairs BT.

Literal body: inputs-LOCALONLY/E08.txt; 4056 bytes; SHA-256 56fb2d2f430ba2e75b8ce6ff2a5add8348586de1436f6d86fe97cce2fba8b640.

## E09: CLD 14.5.2--3, LF 20953--21008

Degree under finite split-torus homomorphisms agrees with the induced lattice index; its calibration transport has the corresponding multiplicity.

Checks the identity-moment degree one in the analytic torus detector and normalization consistency.

Read the full displayed statements/proofs. The identity case can independently be read directly from E06's finite-flat degree-one definition.

Literal body: inputs-LOCALONLY/E09.txt; 3938 bytes; SHA-256 b3e76b072c368fe110d67807ed3d4ef09a65b6640445c32143524e63107c5b60.

## E10: CLD 15.1.1--3, LF 21543--21604

Ordinary analytic forms are locally pulled back by analytic unit moments; smooth functions of their logarithmic norms are ordinary smooth. Nilreduction preserves this form calculus by local lifting of units and refinements.

Used for the regularized logarithmic maximum only where active f_i are actual units. Near individual zeros, inactive-variable omission is exact before constructing a chart.

No logarithmic chart across a zero, or unrestricted pullback of a nonsmooth ordinary current, is asserted.

Literal body: inputs-LOCALONLY/E10.txt; 4240 bytes; SHA-256 151e0b1e8fc80afdf40c34bdd3e0e7dd3079aa836780e879d13742593232c216.

## E11: CLD 13.3.4--7, LF 19232--19308

For a finite module B over an Artinian local A, delta_A(B)=length_A(B)/length_A(A). Local finite-algebra degrees multiply and degrees add over local fibers. Generic calibrated degree is the ratio of the corresponding Artinian lengths.

Nilreduction has degree 1/m for generic length m; E08/E12 therefore retain integration weights m on reduced components.

No reduced generic length is silently substituted for the original one; all valuation regimes are allowed.

Literal body: inputs-LOCALONLY/E11.txt; 5083 bytes; SHA-256 e2225237379e8ae177362bd38833a03379cdaa89727ffd0bfb3e0124dcb83050.

## E12: CLD 15.4.1--3, LF 21735--21778

Canonical integration of top analytic forms is well defined; integration transports under finite maps with the calibrated degree and respects analytic-domain restriction.

Used for the Artinian weight calculation, nilreduction, and ordinary compact integration.

The finite-map hypothesis is used only for canonical forms/integration, not arbitrary current ascent/descent.

Literal body: inputs-LOCALONLY/E12.txt; 2343 bytes; SHA-256 dbfb750b06a6a2b0b88b0ee0175e1fe7617aa83c41f2574b71e23bc588490b92.

## E13: CLD 16.6.3, LF 23434--23462

The integration current of a pure analytic space is the locally finite sum of reduced irreducible component currents with their generic Artinian lengths.

Top-form supports miss lower-dimensional component intersections by S13; the current equality retains the original multiplicities.

This classifies only the integration current. The arbitrary positive current T is never replaced by a component-diagonal current.

Literal body: inputs-LOCALONLY/E13.txt; 1763 bytes; SHA-256 bb016e94a2bcf376705c8e8e02ef302cbab9693253af9e04394b6e3dc5ed47b8.

## E14: CLD A.2.7--11, LF 29196--29294

Smooth partitions subordinate to open covers follow under local compactness, paracompactness, and the stated local plateau sheaf hypotheses; compact portions require only finite localization.

The independent review constructs the compact finite version explicitly, rather than imposing paracompactness on arbitrary opens.

Read the surrounding scalar sheaf construction and proof. These partitions do not preserve closedness of arbitrary weighted currents.

Literal body: inputs-LOCALONLY/E14.txt; 7262 bytes; SHA-256 aca5dd90bd3bb2f394b0d457886fa3f5c7d592581200e5234e02f255b2f506ae.

## E15: CLD 12.1.2--5, LF 16503--16600

A split analytic torus has logarithmic coordinates and associated closed/polyannular analytic domains with the specified coordinate/radius descriptions.

Compact tropical support on the two-dimensional Q_ell torus lies in a compact closed analytic polyannulus; the detecting test is an actual upstairs compact smooth form.

Strictness and boundarylessness refer to the ambient analytic torus. A compact containing domain is not substituted for the ambient space.

Literal body: inputs-LOCALONLY/E15.txt; 6390 bytes; SHA-256 0c2055fac2ed00bc012e49d08fe19874b5d4766dcc18b550db2700c5486f1209.

## Additional F01: CLD 13.3.1--3, LF 19181--19231

For any analytic morphism f:Y->X, a point y of analytic fiber dimension zero is isolated in its fiber and has finite-dimensional local algebra over H(f(y)). A compact zero-dimensional fiber is a finite analytic space over H(x).

Apply to a compact zero-dimensional analytic subspace mapping to M(K). Use ANALYTIC dimension from 11.2.3; ordinary subdomains need not be strict. This avoids a false general Nullstellensatz for nonstrict affinoid fields.

The complete surrounding degree definition, compact-fiber statement, and immediate 13.3.3 base-change proof were freshly read; no current base change is used.

Literal body: inputs-LOCALONLY/F01.txt; 3183 bytes; SHA-256 7d0cbbc50a8d6df68b7ae598849abf198e58fa9961c853f3497b09c12e3c241e.

## Imported deeper foundations

Berkovich, Spectral theory and analytic geometry over non-Archimedean fields, Mathematical Surveys and Monographs 33 (1990), Chapter 2, sections 2.1--2.2: affinoid algebras over complete K are noetherian; coherent analytic subspace ideals on affinoid neighborhoods are finite ideals. Completeness is retained and no nontrivial valuation or algebraic closure is required here.

Additional complete immediate CLD 13.3.1--3 reading: points in zero-dimensional analytic fibers are isolated; compact zero-dimensional analytic fibers are finite analytic spaces over the completed residue field of the base point. Apply to a compact piece of a zero-dimensional analytic locus mapping to M(K); its algebra is finite-dimensional over K and Artinian. Analytic dimension from S11 is retained. A general finite-residue-field Nullstellensatz for arbitrary NONSTRICT affinoid rings is not used.

Standard graded analytic dimension and finite-flat moment foundations explicitly cited recursively in CLD.

Real finite-dimensional PSD linear algebra, compact Stone-Weierstrass, Riesz representation for Radon measures, and convolution by nonnegative compact smooth kernels.
