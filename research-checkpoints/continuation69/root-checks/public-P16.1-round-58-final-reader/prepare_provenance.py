#!/usr/bin/env python3
"""Exact LF excerpt preservation; a scope record, not a correctness verdict."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parent
manifest=json.loads((ROOT/'source-extracts/source-manifest.json').read_text())
expected={
'BJ':('8d5975337f4ac88a475929ea6a436ec4a15d08715d5582bc0ba0eb3e07152c52','659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0'),
'Wu':('11808a6c9ede9c0158b27e16700fc180a4ac8df12a4586a7178e1958e8f6bba8','c8ffe91a631da67f6d3872a1a06ab8d15755aed2f926cdf326725ca3662cef7d'),
'CLD':('5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719','64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085'),
'GM':('3a3de12f0bf765955b2b297d37704f31a432dea33cfe849145a7ff3dfe5f2571','d4427404d299d40fd70c03b2aebbe8e9dd8ffaccb05d8ef5eb04a95a23d3970a'),
'Wanner':('8df4a1af5dce69c1ef3a6bad2169997b5d72f8c7ced5f95d8a7dcd33ae6dd1b7','e83a0516614296bc5720c6af22845255031671293dfab9acd05b12284984798f'),
'Thuillier':('9c57da951e8dca2676d762e9e8c6ace302675938d72434a5b0390f15af7ea29a','e82226b3dde6a8088c35e1481bfd43f64bb69ee309b5cfda92c8c927a7885570')}
for rec in manifest:
 for idx,f in enumerate(rec['files']):
  b=(ROOT/f['artifact']).read_bytes(); digest=hashlib.sha256(b).hexdigest()
  assert digest==f['sha256']==expected[rec['id']][idx],(rec['id'],idx)
  assert len(b)==f['bytes']
# Each range contains the literal statement and its relevant surrounding proof.
# 'checked_application' states the application actually retained, not source-wide approval.
ranges=[
('BJ',540,632,'Ambient scope and generic finiteness','Reduced singular and nonnormal projective varieties; task retains irreducibility.','No blanket local/global identification.'),
('BJ',737,860,'Relative integral closure and vertical R1/S2','Closure in given generic fiber; vertical DVRs for model weights.','Absolute normalization must not replace it.'),
('BJ',944,1005,'Rational PL lattice and density','Rational finite signed sums/max/min in collar formula; PL testing.','Real span is expressly not closed under max.'),
('BJ',1170,1228,'Actual global Fubini--Study metrics','Clipped section norms add a complete basepoint-free reference system.','Individual untruncated log section norms need not be bounded PL.'),
('BJ',2170,2243,'Genuine global PSH and model-nef criterion','Original global cone retained; relatively nef represented collars enter it.','Auxiliary local conventions do not redefine this cone.'),
('BJ',2301,2426,'Class closure, approximation and pullbacks','Decreasing global closure, ample model approximation, rational class limits.','Increasing closure is not assumed without EP.'),
('BJ',2469,2479,'Smooth field equivalence','GM route only on smooth connected projective characteristic-zero compactification.','No application to a singular quotient.'),
('BJ',2494,2551,'Divisorial determination','Global separation and uniqueness.','Does not itself globalize a weak local singular potential.'),
('BJ',2813,2875,'Envelope compactness and birational onto criterion','Theorem 5.11 under EP; Lemma 5.13 with larger EP classes.','Onto normalization remains conditional.'),
('BJ',2980,3063,'Smooth sufficient envelope theorem','Smooth characteristic-zero nef resolution input is a source theorem.','Downstairs global singular envelope is not inferred.'),
('BJ',3649,3744,'Energy extension and normalization','Actual general-variety pairing, translation and decreasing continuity.','No EP antecedent here.'),
('BJ',3790,3952,'Finite energy and mixed multilinear pairing','Finite mixed E1 pairings and differences; normalized energy.','Intermediate quantitative results are cited as primary source results.'),
('BJ',3972,4140,'Radon mixed operator and weighted continuity','PL testing, raw mass, actual model formula, integrability, normalization pushforward.','Weighted integral sign is containing-test minus containing-zero.'),
('BJ',4531,4620,'Locality and comparison','Global E1 locality followed by equal-mass comparison.','The measure on the strict max locus is the winning potential measure.'),
('BJ',4760,4837,'Upper/lower energy extension','Envelope-energy identification for unbounded potentials requires EP.','The unconditional derivative uses E-downarrow.'),
('BJ',4843,4963,'Uniform energy derivative and proof','Both signs, uniform PL directions, continuous squeeze error |t| eta.','No singular multiplier ideal theorem is imported.'),
('BJ',5002,5159,'Dual energy, model targets and maximizing measures','Mass-one target functional and convergence before attainment.','Maximizing measure convergence alone is not existence.'),
('BJ',5193,5301,'Bounded J integration and exact finite-energy targets','Primary 9.19/9.20; corrected absolute-value identity and negative integration bound.','All-E1 integrability is not a standalone surjectivity theorem.'),
('BJ',5408,5481,'Uniqueness and global domination','Equidimensional, here irreducible, so one constant; no EP needed.','Only genuine global potentials may be tested.'),
('BJ',5758,5813,'Dirac energy','Divisorial valuations have finite dual energy for uniqueness and nodal example.','No singular Dirac equation existence assumed.'),
('BJ',6080,6168,'Actual general equation equivalence and nodal example','12.8 general irreducible domain; use 5.11 instead of smooth 5.21 citation under EP.','12.9 is smooth sufficient scope, not singular conclusion.'),
('BJ',6224,6270,'Unconditional sequential approximation','Sequences extracted from already convergent monotone nets; 12.18.','No equation surjectivity or EP is used to create approximation of an already global potential.'),
('Wu',557,631,'Fiber descent proposal','Relevant source bodies identified for residual singular EP dependency.','Sign in zero-psh multiplier needs repair; whole descent chain not certified.'),
('Wu',639,759,'Tropical convex/local definitions','Literal missing additive constant diagnosed; finite ambient convex formulas have independent positivity.','Convex data only on a tropical image still require compatibility; not asserted by smoothing.'),
('Wu',762,847,'Affine FS, growth and embedding','Exact generator/floor conditions checked; upper-growth convention used for auxiliary repairs.','Printed lower-growth condition fails at log poles.'),
('Wu',898,1034,'Model criterion, regularizable extension and exhaustion','Algebraic collar repair for already global AFS and polynomial coefficient inputs.','Not arbitrary analytic-PL representation.'),
('Wu',1035,1117,'Bounded local globalization and divisorial locality','Negative floor and reference/scalar bookkeeping identified.','Arbitrary smooth local measure/globalization remains unresolved here.'),
('Wu',1190,1306,'Local mixed measures and proof','Exact 4.2 overlap/continuity obligations identified from actual proof.','No current-only replacement of local mixed-measure compatibility is claimed.'),
('Wu',1339,1590,'Local comparison, domination and smooth regularization','Read the required dependency chain; smooth 4.19 invocation of 3.25 is circular as printed.','No unconditional smooth weak base asserted by this reconstruction.'),
('Wu',1591,1680,'Hulls and compact polytopes','Independent strict-margin polytope exhaustion proof in Section 8.','Literal sign and interior identifications are not carried over.'),
('Wu',1698,1831,'Rossi and Hartogs distance','Exact coefficient f_j,i expressions regularized via algebraic collars.','Rossi arbitrary analytic neighborhood gluing remains a separate gate.'),
('Wu',1832,1884,'Localization proof','Pole-order/conductor repair replaces false denominator bound.','Localization conclusion for arbitrary regularizable functions still needs controlled approximation.'),
('Wu',1885,1957,'Weak base and weak/global claim','Actual dependencies of 6.2, 6.3, 6.5 inspected.','Full singular regularization and weak/global theorem not established.'),
('Wu',1964,2104,'Strict barrier and support use','Global entropy, rational series and real log support constructed independently.','Support construction alone is not Runge induction.'),
('Wu',2107,2207,'Finite-flat trace and proof','Independent determinant replaces projective norm-metric citation for supplied FS inputs.','Trace limit generic finiteness checked separately.'),
('Wu',2208,2371,'Slicing norm proof and curve lemma','Independent global FS norm extension fixes weights; proper witness-adapted lift; radial equality under stated positivity.','No arbitrary-H(s) FS regularization; general corrected local current bridge remains a condition.'),
('Wu',2372,2533,'Split-locus trace and Rossi use','Concrete analytic-piece gluing, locally constant gamma and gamma=1 issues identified.','Not validated by algebraic collar formula alone.'),
('Wu',2534,2692,'Runge/local projection/singular induction','Hartogs coefficient step verified separately; dependency chain exposed.','Complete 6.14--6.16 replacement remains unproved.'),
('Wu',2694,2749,'Actual body singular envelope theorem','Retained exact unibranch statement, not only narrower introduction.','Its weak/global antecedent still not reconstructed.'),
('CLD',9729,9765,'CLD local psh sheaf','Used for explicit ambient convex smooth maxima and decreasing approximation.','No equality of local cones by name is assumed.'),
('CLD',9890,10025,'Convex compositions and current positivity','Positive Hessian on explicit finite-coordinate charts; continuous finite limits locally integrable.','Ambient-extension compatibility for arbitrary tropical-image data unresolved.'),
('CLD',16360,16405,'Residual formal geometry','Read in conjunction with residual pre-model lemma.','Only proper formal model residual degree tests used.'),
('CLD',17545,17577,'Integer versus strict PL','Integer PL allows arbitrary real constants; clear rational coefficients for collar metrics.','Strictness only introduced over nontrivially valued extension.'),
('CLD',24106,24157,'PL metric convention','Tensor power and model frame changes.','No direct GM theorem over trivial valuation.'),
('CLD',25414,25518,'Formal residual pre-model and proof','Central curve with restricted model bundle; nilpotents do not change integral-curve degree tests.','Relative model retains nonnormal generic fiber.'),
('CLD',26935,27180,'Formal metric product compatibility','Exact local/global mixed-measure compatibility obligation located.','Not imported as a proof of full local bounded decreasing compatibility.'),
('CLD',27926,28076,'Residual-nef, field extension and positivity equivalence','d=1 central-curve residual degrees; 18.8.6 field extension; boundaryless separated hypothesis.','18.8.9 nontriviality is a different statement; full singular local BT not concluded.'),
('GM',79,140,'Metric model equivalence','Proper schemes over nontrivially valued complete field.','Never used directly over trivially valued k.'),
('GM',174,195,'Standing field','k((t)) is in scope, rational powers/constants clear to strict integral PL.','This gives individual smooth model metrics only.'),
('GM',642,695,'Nef formal metrics','Reduced-model and degree/projection formula checks; proof body of 3.5.','No singular envelope theorem inferred.'),
('Wanner',168,242,'Standing field and curve subharmonic comparison','Omega complete algebraically closed nontrivially valued; smooth algebraic curves.','Extension also needed when F is trivial.'),
('Wanner',800,825,'Section 4 smooth proper standing scope','Apply only on open subsets of smooth proper compactifications.','Field hypotheses are also mandatory.'),
('Wanner',275,330,'Lisse Laplacian and comparison','Checked disk comparison context and harmonic constants.','A general local slope replacement is not claimed.'),
('Wanner',502,531,'Current psh definition','Continuous functions locally integrable; positive d-prime d-doubleprime.','The theorem is applied to continuous approximants, not directly an unbounded limit.'),
('Wanner',1096,1612,'Theorem 4.7 and full proof body','Continuous current-psh on open subsets of smooth proper curves implies Thuillier-subharmonic; smooth curve compactifications verify that scope.','No arbitrary-field affine FS approximation follows.'),
('Thuillier',3781,3869,'Subharmonic definition, decreasing stability and disk boundary','3.1.5 comparison; 3.1.8(ii) decreasing limit or minus infinity; 3.1.9 boundary finiteness.','Radial Gauss convergence, not ordinary punctured-neighborhood limit.')]
excerpts=[]
for idx,(source,start,end,label,application,limit) in enumerate(ranges,1):
 lines=(ROOT/'sources'/f'{source}.txt').read_text(encoding='utf-8').split('\n')
 assert 1<=start<=end<=len(lines)
 literal='\n'.join(lines[start-1:end])
 name=f'{idx:02d}-{source}-LF{start}-{end}.txt'
 (ROOT/'source-extracts'/name).write_text(literal,encoding='utf-8')
 excerpts.append({'id':f'e{idx}','source':source,'label':label,'inclusive_one_based_LF_range':[start,end],'line_convention':"UTF-8 decode then split('\\n'); select [start-1:end] and join with LF",'artifact':f'source-extracts/{name}','literal_statement_and_relevant_proof_body':literal,'checked_application':application,'concrete_limit':limit,'epistemic_status':'Unverified primary-source application audit; no source-wide correctness verdict.'})
result={'sources':manifest,'hash_checks':'All twelve supplied PDF/text hashes equal expected input hashes.','excerpts':excerpts,'read_scope':'Selected relevant bodies, not a whole-body audit.','proof_status':'Partial; no source citation or hash is a mathematical certification.'}
(ROOT/'source-extracts/source-provenance.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'source_hashes_verified':12,'literal_excerpts':len(excerpts),'LF_range_method':"split('\\n')"}))
