from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parent
S=json.loads((ROOT/'source-manifest.json').read_text())
# Inclusive one-based indices in the exact UTF-8 text split by LF.
U=[
(0,'BJ-standing-scope',435,469,'General reduced projective varieties and real numerical classes. No smoothness hypothesis is inserted.'),
(0,'BJ-Gauss-relative-closure',717,860,'Continuous section, relative integral closure and vertical DVR/depth criterion; absolute normalization is not substituted.'),
(0,'BJ-PL-lattice',971,1003,'Rational vector lattice and uniform density; no variable-denominator partition.'),
(0,'BJ-model-atoms',1051,1110,'Whole Rees-valuation construction and order test; rationally scaled source divisorial points.'),
(0,'BJ-ample-on-fixed-model',1411,1452,'Whole ample bundle construction on a dominating configuration.'),
(0,'BJ-Hdom-fixed-bundle',1692,1704,'Hdom of an ample rational class is contained in H of the fixed rational bundle.'),
(0,'BJ-model-measures-IBP',1760,1849,'Intersection formulas and integration by parts use actual model functions, not arbitrary local analytic functions.'),
(0,'BJ-generated-cone-closure',2173,2339,'Actual PSH definition, decreasing and class closure, sum/max/pullback. Generic nontriviality remains necessary.'),
(0,'BJ-regularization',2418,2479,'Uniform and decreasing FS regularization; Remark4.19 remains smooth-only.'),
(0,'BJ-divisorial-order',2494,2535,'Order against an usc upper function; continuous-majorant nets rather than sequences.'),
(0,'BJ-nonnegligibility-EP-compactness-onto',2773,2873,'EP implies compactness; birational onto requires larger target classes with EP.'),
(0,'BJ-envelope-continuity-smooth-EP',2880,3065,'Continuous obstacles and smooth connected nef EP in characteristic zero; not singular EP.'),
(0,'BJ-general-energy-pairing',3649,3795,'General-variety scope explicitly resumed; decreasing pairing construction and mixed finite-energy bounds.'),
(0,'BJ-energy-space-multilinearity',3796,3949,'E1 and multilinear extension; all ample real classes allowed by the source.'),
(0,'BJ-actual-Radon-operator',3956,4057,'Whole operator construction and7.19 proof. Raw mass is the intersection degree.'),
(0,'BJ-weighted-continuity',4074,4125,'Whole7.21/7.22 proofs. Correct pairing-containing-test minus pairing-containing-zero at4119/4123.'),
(0,'BJ-continuous-CLD-compatibility',4126,4137,'Actual continuous genuine compatibility only; local bounded limits require an additional common representation.'),
(0,'BJ-locality-comparison',4529,4602,'Whole7.40/7.41/7.43/7.44. Weighted7.21 applied separately to both decreasing test terms repairs4585.'),
(0,'BJ-two-sided-energy-differentiation',4835,4969,'Uniform PL derivative and continuous squeeze; plus sign in the upper endpoint. Envelope identification for unbounded potentials requires EP.'),
(0,'BJ-dual-energy',4970,5015,'Actual probability dual energy, translation invariance and target definition.'),
(0,'BJ-maximizing-model-measures',5131,5262,'Differentiability, target approximation before attainment, bounded-J estimates and complete9.19 proof; absolute difference equals2max-a-b.'),
(0,'BJ-target-integrability',5263,5315,'Whole9.20/9.21 proof; use the negative normalized integral in the square-root estimate.'),
(0,'BJ-uniqueness-domination',5427,5486,'Uniqueness modulo locally constant functions, hence one constant on integral X; domination is already genuine global.'),
(0,'BJ-dual-Dirac',5751,5821,'Divisorial Diracs have finite dual energy, not a singular Dirac-existence theorem.'),
(0,'BJ-equation-EP-equivalence',6085,6189,'Whole12.8 proof and smooth sufficient theorem; replace smooth compactness citation by general5.11 under EP.'),
(0,'BJ-countable-sequential-regularization',6230,6265,'Whole12.16 proof and12.18. No countable-field or EP antecedent; genuine global membership and genuine limit are required.'),
(1,'Wu-auxiliary-definitions',639,681,'Omitted contact constant must be repaired; use finite affine charts at infinite coordinates.'),
(1,'Wu-AFS-growth',762,820,'Literal lower-growth convention is diagnostic and fails for logarithmic poles; corrected auxiliary growth is u<=h+O(1).'),
(1,'Wu-controlled-approximation-diagnostic',938,1034,'Printed globalization and approximation lemmas are not premises; reconstruct collars and controlled shifts.'),
(1,'Wu-removal-boundary-blowup',1116,1196,'Damping is not globally monotone. Correct exceptional signs: I O=O(-E), -E relatively ample.'),
(1,'Wu-local-mass-globalization-diagnostic',1395,1576,'Diagnostic local mass/IBP/comparison proof; positive model atoms replace the Dirac equation.'),
(1,'Wu-polynomial-hulls-Rossi-Hartogs',1590,1844,'Continuous compact-perturbation proof reconstructed; printed interior=strict constraint shortcut cannot be used for constants.'),
(1,'Wu-weak-definition-and-global-target',1885,1962,'Weak witness definition and actual dependencies6.2/6.5; singular target theorem not assumed.'),
(1,'Wu-strict-barrier-and-local-Runge',1964,2103,'Diagnostic strict supports, localization and Runge dependencies; full induction remains unresolved in this deliverable.'),
(1,'Wu-finite-flat-determinant-trace',2104,2206,'Determinant traces must retain Artinian lengths/residue degrees and algebra generators.'),
(1,'Wu-open-trace-and-radial-application',2207,2382,'Step2 needs smooth weak/removal; radial Step3 can be proved directly without arbitrary-H(s) affine regularization.'),
(1,'Wu-split-piece-and-induction',2383,2696,'Diagnostic only. Local integer gamma, gamma=1, common witnesses, support controls and Runge induction need full reconstruction.'),
(1,'Wu-singular-envelope',2697,2747,'Printed7.1 explicitly uses6.5 at2716; cannot be imported after only smooth regularization.'),
(2,'CLD-continuous-uniform-products',10432,10449,'Whole8.7.2 proof; continuous locally uniform convergence, not arbitrary bounded decreasing convergence.'),
(2,'CLD-model-residual-measure',26935,27039,'Model/intersection compatibility retains graded residue degrees and analytic multiplicities.'),
(2,'CLD-strict-integer-nef-to-psh',25583,25637,'17.8.4 is strict integer PL nef-to-psh, not an arbitrary-current pullback criterion.'),
(2,'CLD-integer-residual-current',27926,28058,'18.8.4 and18.8.6 apply to already represented integer PL metrics; no antecedent self-certification.'),
(3,'GM-representation-extension',239,378,'Full2.4/2.7/2.10 proofs: actual cocycle and compact strictly analytic formal metric extension.'),
(3,'GM-field-detection-and-model-independence',652,711,'3.3 detects nefness after extension only for a represented model;3.5 independence on the determination.'),
(3,'GM-local-global-nef',714,782,'Whole3.11 proof, actual neighborhood and residual proper curve tests.'),
(4,'Wanner-standing-field-and-curve-skeleton',168,286,'Complete algebraically closed nontrivial field, common skeleton, lisse membership and positive Laplacian criterion.'),
(4,'Wanner-proper-scope-positive-lisse',801,921,'Section4 assumes smooth proper curve; whole4.3 proof used only on an original open after compactification.'),
(5,'Thuillier-unit-skeleton-proof',2897,2976,'2.2.24 proof: unit and inverse give equality on retraction fibres; outgoing weighted slopes.'),
(5,'Thuillier-unit-harmonic-type-I-IV',3580,3627,'2.3.21 explicitly concerns unit-log germs; extracted2.3.20 loses a superscript, so no assertion for logs with zeros is inferred.'),
(5,'Thuillier-monotone-and-radial',3810,3852,'Decreasing subharmonic stability and finite boundary values; identically minus-infinity alternatives retained.'),
(5,'Thuillier-lisse-positive-Laplacian',5322,5361,'3.4.4 criterion and relevant proof body; strict smooth curve assumptions retained.'),
(6,'BE-standing-FS',1783,1888,'Projective scheme, FS sections and algebraic addition/product-section conventions.'),
(6,'BE-exact-model-pure-FS-difference',1989,2043,'Whole5.14/5.16vi/5.17 proofs. Same-class cancellation before Laurent H0 coefficient descent.'),
(6,'BE-genuine-FS-cone-and-ample-nef',2281,2352,'Whole7.2-7.8/7.9 and proofs; nontrivial Laurent field and ample bundle. No smoothness hypothesis.'),
(6,'BE-semiample-smooth-regularization',2357,2379,'Whole7.14 and proof: semiample FS metrics regularized by a smooth maximum. This is not envelope regularity or singular EP.'),
(6,'BE-continuous-products-and-proofs',2611,2779,'General projective-scheme continuous psh-regularizable measures, actual fundamental cycles, uniform convergence and field invariance. Correct the displayed last plus in2726 to a minus before applying the triangle bound; no bounded-decreasing local theorem is inferred.'),
(6,'BE-model-Deligne-compatibility-and-proof',3121,3177,'Whole8.18/8.19 proof and model intersection identity, for a projective scheme and actual projective model; no smoothness assumption.'),
(7,'GR-standing-PL-warning',144,254,'Actual strict PL antecedent. Remark1.8 warns general R-PL positive-current pullback/converse are unknown.'),
(7,'GR-curve-criterion',818,843,'Whole5.1 proof: smooth analytic curve locally algebraic, unit pullbacks need not be algebraic.'),
(7,'GR-all-curve-detection',890,934,'Whole5.4 and5.5 proofs: every smooth analytic curve map over an algebraically closed analytic extension.'),
(8,'Ducros-valued-image-proof-A',1276,1402,'Actual1.2 and proof of closedness and upper dimension bound, not dimension equality.'),
(8,'Ducros-compact-strict-polytope-proof',2077,2150,'Whole3.2 proof: compact Gamma-strict analytic space with analytic units; rational polytope image.'),
(9,'GJR-local-residue-nef-proof',2298,2330,'Whole7.1 proof; local compact strict neighborhood and proper residual curve test.'),
(9,'GJR-model-nef-and-field-detection',2356,2425,'Whole7.4/7.6 proofs; actual PL and represented model hypotheses retained.'),
]
files=[]; dst=ROOT/'sources';dst.mkdir(exist_ok=True)
for i,r in enumerate(S):
 for key in ['pdf','literal_extract','abstract_html','html']:
  if key not in r: continue
  p=Path(r[key]); b=p.read_bytes(); h=hashlib.sha256(b).hexdigest(); expected=r.get({'literal_extract':'extract_sha256','abstract_html':'abstract_sha256'}.get(key,key+'_sha256'))
  if h!=expected: raise RuntimeError(f'Hash mismatch: {p}')
  name=f'{i+1:02d}-{p.name}';(dst/name).write_bytes(b)
  files.append({'source_index':i,'kind':key,'authorized_path':str(p),'local_file':'sources/'+name,'sha256':h,'bytes':len(b)})
ex=[];out=ROOT/'source-extracts';out.mkdir(exist_ok=True)
for i,id,a,b,app in U:
 r=S[i];raw=Path(r['literal_extract']).read_bytes();t=raw.decode('utf-8').split('\n');literal='\n'.join(t[a-1:b]);fname=id+'.txt';(out/fname).write_bytes(literal.encode('utf-8'))
 ex.append({'id':id,'source_index':i,'version':r['saved_version'],'public_source':r.get('public_source'),'source_path':r['literal_extract'],'source_sha256':hashlib.sha256(raw).hexdigest(),'inclusive_one_based_LF':[a,b],'LF_definition':"UTF-8 bytes decoded without newline conversion and split('\\n'); inclusive one-based indices",'literal':literal,'literal_file':'source-extracts/'+fname,'literal_sha256':hashlib.sha256(literal.encode()).hexdigest(),'checked_application_and_concrete_limits':app,'whole_source_audit':False})
obj={'sources':S,'verified_files':files,'excerpts':ex,'limits':'Literal excerpts and hash verification do not certify mathematics, novelty, or correctness of source preprints. Earlier generated bodies are diagnostic, never premises.'}
(out/'source-provenance.json').write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'verified_source_files':len(files),'literal_excerpts':len(ex)}))
