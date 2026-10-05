"""Verify only the eleven permitted source caches; preserve literal LF excerpts."""
from pathlib import Path
import json,hashlib
sources=json.loads(Path('sources.json').read_text())
# Each inclusive range is large enough to include the indicated statement and relevant proof.
selections={
'A':[(165,246,'Cone scope, torified action and carrier'),(277,366,'Actual FS and CPSH; varying-field finite maxima'),(425,520,'Bounded currents and integration by parts'),(522,612,'Genuine energy and bounded calculus'),(755,805,'Actual decreasing-net PSH'),(930,965,'Actual extended energy'),(972,1129,'Mixed MA statement and complete induction with index and positivity repairs')],
'B':[(470,503,'Filtration conventions and finite-type saturation'),(635,645,'Nonnegative cutoff convergence, not used for signed conclusions'),(679,758,'Cumulative versus degree-wise mean'),(1260,1372,'Printed radial bridge and energy inconsistency')],
'C':[(436,540,'Standing scope and conventions'),(3693,3718,'Pairing dilation'),(3790,3830,'Normalized energy and two homogeneities'),(3956,4000,'Radon net integrals and mixed construction'),(4003,4057,'Existing projective mixed measures'),(4074,4129,'Weighted decreasing continuity and mass lemma'),(4690,4823,'Obstacle and outer extensions'),(4841,4962,'Uniform differentiation: full statements and proofs; obstacle-volume gate')],
'D':[(281,350,'Synthetic linear mixed-form hypotheses; no cross-root application')],
'E':[(761,774,'Growth and regularizability definitions'),(950,997,'Regularizable hypothesis in gluing lemma'),(1560,1576,'Regularizability dependency in Proposition 4.19'),(1885,1915,'Opposite growth convention in weak psh definition')],
'F':[(520,525,'Smooth-projective standing hypothesis'),(1190,1320,'FS/obstacle identity, approximation theorem and external lattice dependency')],
'G':[(7095,7138,'Cutoffs, continuous-test density and compact-support partitions'),(9797,9834,'Continuous-psh sheaf and uniform limits'),(10410,10449,'Weighted current convergence with moving positive closed current'),(17545,17590,'Integer-paralinear metrics with real constants'),(19283,19306,'Finite calibrated degree'),(22100,22132,'Boundary and singular-space tropical differential structure'),(22248,22281,'Finite-map current projection formula and proof'),(26470,26492,'Flat fiber integration and proof'),(26700,27180,'Discrete curvature and full graded residue calculation'),(27297,27555,'Formal fundamental cycle and discrete-field multiplicity proof'),(27561,27673,'Fiber integration current and one-unit radial Gauss current, full proofs')],
'H':[(25,95,'Standing scheme and characteristic-zero context'),(941,991,'Finite-generated Rees to ample test configuration, full proof'),(1249,1373,'DH barycenter and normalization, full proofs'),(1796,1807,'Upper and lower linear bounds'),(1837,1875,'Veronese and filtration/DH compatibility, complete proof'),(2136,2209,'Base-change action on metrics'),(2275,2313,'Mixed vertical intersection, base-change scalars and Hodge statement; independent matrix proof replaces its external citation'),(2317,2358,'Probability model masses and valued-field interpretation'),(2372,2435,'Intersection energy and complete expansion; printed extra V factor')],
'I':[(241,261,'Arbitrary complete field and geometrically reduced scheme'),(299,420,'Models, reduced fiber, regular sections and metric conventions'),(522,627,'Determinant difference, Deligne pairing and RR, full proofs'),(629,788,'Lemma 3.2 and Theorem 3.1, complete both-sign proofs'),(788,843,'Separate envelope-conditional section')],
'J':[(2282,2358,'FS/decreasing/uniform PSH and nef-model approximation'),(2520,2555,'FS obstacle inequality and one-degree norm equality'),(2610,2780,'Curvature, field extension, uniform limits and model masses'),(3121,3192,'Model Deligne/CLD compatibility and proof'),(3430,3539,'Relative-volume existence and field-extension compatibility'),(3540,3673,'Genuine continuous-psh energy, equality and full proof; separate EP corollary'),(4395,4430,'Relatively regular sections and proof')],
'K':[(173,235,'Introduction: distinction from enveloped energy'),(289,311,'Geometrically integral variety convention'),(1286,1467,'Regular-point valuations and external Chebyshev premises'),(1469,1732,'Complete approximation/lattice/first-moment body including 4.5.4/4.5.5'),(1735,1886,'Complete Theorem 5.1.1 proof including increasing/decreasing and factorial slips')]
}
applications={
'A':{'checked_application':'Actual cone domains and energy (1); fixed-field MA reconstructed by (45)--(47).','limits':'Printed second-derivative, J, index and positivity shortcuts are not premises. No full-link density or cross-field unbounded continuity inferred.'},
'B':{'checked_application':'Norm definition audited; signed norms, shifts, volume and (30) proved independently.','limits':'Printed E=S and mL radial trivialization are not used.'},
'C':{'checked_application':'Dilation homogeneity on rational projective quotients; actual outer-energy distinction and net-integral methods. (5) reconstructed through BGM and (40).','limits':'No EP conclusion or printed epsilon squeeze used. Projective Theorem 8.5 is not assumed to apply to cones.'},
'D':{'checked_application':'Diagnostic audit of common linear-form assumptions.','limits':'No theorem from this body is used as a mathematical premise.'},
'E':{'checked_application':'Diagnostic audit of growth and regularizability dependencies.','limits':'No envelope theorem is used; no falsehood or independent review verdict inferred.'},
'F':{'checked_application':'Diagnostic scope and external lattice audit.','limits':'Its smooth standing hypothesis does not cover general normal quotients; it is not used as a premise.'},
'G':{'checked_application':'Actual flat L^-1 torsor, integer-paralinear metrics after tensoring, singular boundaryless spaces; one-unit Gauss mass against all tests. Finite map degree d checked algebraically. Weighted current theorem used only on local uniform sequences.','limits':'No unbounded-decreasing or smooth-base-only inference. Every factor is retained in (24)--(26).'},
'H':{'checked_application':'Full ample section ring, finite-generated exhaustive separated Z-filtration; normal generic variety and reduced normalization hypothesis. Actual intersection mean and probabilities including b_E. First moments independently reconstructed from the RR proof.','limits':'External threshold-series/lattice result in 5.3 is not needed. Printed extra 1/V in 7.5 is corrected by 6.7 and 6.12.'},
'I':{'checked_application':'Normal projective quotients are geometrically reduced, omega and A omega ample rational classes, actual continuous-psh metrics; all denominators cleared separately. Proof bodies and both signs audited with p! retained.','limits':'Section 3.2 envelope claims are not used. Constant (5) depends on the fixed direction; no unit-ball modulus is asserted.'},
'J':{'checked_application':'Actual v3 numbering. 7.2/7.6 identify real FS/continuous PSH. 8.3/8.18 supply field-extension and actual model pairing. 9.15 used only for two continuous psh metrics. A.15 applies to flat projective finitely presented ample models.','limits':'9.16 and a one-degree supnorm isometry do not prove (40). Reverse obstacle inequality is proved by signed semigroups.'},
'K':{'checked_application':'Full proof and exact standing scope reviewed diagnostically. Independent (33)--(39) supplies the required first-moment approximation.','limits':'External lattice/Chebyshev claims and printed probability/factorial/increasing-versus-decreasing chains are not premises. No continuity of increasing energy is used.'}
}
report={'lf_convention':"UTF-8 decoded extract split('\\n'); one-based inclusive ranges",'sources':[],'excerpts':[],'mathematical_status':'Unverified source applications and draft mathematics; hashes establish identity only.'}
for src in sources:
 item={'id':src['local_id'],'version':src['saved_version'],'title':src.get('title'),'public_source':src['public_source'],'files':[],**applications[src['local_id']]}
 for kind in ['pdf','literal_extract','abstract_html','html','fresh_official_versioned_pdf']:
  path=src.get(kind)
  if not path:continue
  hkey={'literal_extract':'extract_sha256','abstract_html':'abstract_sha256','html':'html_sha256','fresh_official_versioned_pdf':'fresh_official_pdf_sha256'}.get(kind,kind+'_sha256')
  actual=hashlib.sha256(Path(path).read_bytes()).hexdigest();expected=src.get(hkey)
  if expected is not None:assert actual==expected,(path,actual,expected)
  item['files'].append({'kind':kind,'path':path,'sha256':actual,'expected_sha256':expected,'matches':actual==expected if expected else None})
 lines=Path(src['literal_extract']).read_text().split('\n');item['LF_count']=len(lines)
 for low,high,label in selections[src['local_id']]:
  assert 1<=low<=high<=len(lines)
  literal='\n'.join(lines[low-1:high])
  eid=f'{src["local_id"]}-{low}-{high}'
  dest=Path('source-extracts')/(eid+'.txt');dest.write_text(literal)
  report['excerpts'].append({'id':eid,'source':src['local_id'],'version':src['saved_version'],'lf_start':low,'lf_end':high,'label':label,'literal_statement_and_proof_body':literal,'artifact':str(dest),'sha256':hashlib.sha256(literal.encode()).hexdigest(),'application_check':applications[src['local_id']]})
 report['sources'].append(item)
Path('source-extracts/source-provenance.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'source_count':len(report['sources']),'excerpt_count':len(report['excerpts']),'all_supplied_hashes_match':True}))
