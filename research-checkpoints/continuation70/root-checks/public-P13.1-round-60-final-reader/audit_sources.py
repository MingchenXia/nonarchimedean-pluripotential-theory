"""Audit only the ten explicitly supplied public caches; no network access."""
from pathlib import Path
import hashlib, json

ROOT = Path(__file__).resolve().parent
SOURCES = json.loads((ROOT / 'sources.json').read_text())
RANGES = {
 'A': [(127,148,'outlook'),(181,246,'cone/action'),(277,345,'FS and probability'),
       (350,424,'changing fields and algebra'),(522,620,'genuine energy'),
       (762,815,'PSH'),(930,971,'extended energy'),(976,1100,'mixed finite energy proof'),
       (1100,1143,'integration by parts')],
 'B': [(181,220,'standing field/volume'),(470,512,'norms'),(614,645,'spectral convergence'),
       (679,755,'cumulative calibration'),(1275,1378,'printed radial bridge and energy mismatch')],
 'C': [(970,1038,'PL density'),(1750,1860,'model pairings'),(3661,3727,'energy scaling'),
       (3802,3821,'energy properties'),(4683,4823,'obstacle extensions'),
       (4841,4962,'uniform differentiation: full theorem and proof')],
 'D': [(1060,1130,'relative-volume application'),(1280,1347,'synthetic form scope')],
 'E': [(746,786,'logarithmic growth'),(950,997,'regularizable extension'),
       (1550,1579,'regularization dependency'),(1880,1906,'second growth definition'),
       (2630,2747,'envelope final stage')],
 'F': [(515,535,'standing smoothness'),(1222,1315,'norm approximation proof')],
 'G': [(7095,7134,'cutoffs and continuous test density'),(9797,9836,'continuous psh sheaf'),
       (10432,10487,'weighted continuity and pullbacks'),(17538,17585,'integer paralinear: real constants'),
       (19283,19323,'calibrated finite degree'),
       (22105,22140,'singular analytic structure'),(22248,22288,'finite projection proof'),
       (26430,26489,'field/fiber integration'),(26935,27028,'discrete curvature calibration'),
       (27561,27688,'relative radial theorem and full proof')],
 'H': [(391,438,'Rees finite generation'),(941,1003,'test configurations/filtrations'),
       (1241,1373,'barycenter and normalization proofs'),(1770,1875,'signed limit and DH'),
       (2136,2202,'metric equivalence and base-change scaling'),
       (2273,2335,'mixed model measures and intersections'),(2372,2435,'energy')],
 'I': [(241,304,'norms and content'),(318,420,'models, regular sections, psh'),
       (421,512,'MA and relative-volume properties'),(522,627,'RR complete proof'),
       (629,783,'Lemma 3.2/Theorem 3.1 complete proofs'),(785,855,'additional envelope assumption')],
 'J': [(1740,1779,'reduced-model theorem'),(2110,2180,'supnorm/base extension'),
       (2200,2250,'complete supnorm field-extension proof'),
       (2281,2349,'FS PSH conventions'),(2500,2549,'FS envelopes and identical norms'),
       (2614,2708,'MA compatibility'),(2925,2990,'Deligne pairing'),
       (3125,3163,'model/Deligne compatibility complete proof'),
       (3430,3539,'volume existence and field extension'),(3540,3673,'energy-volume complete proof'),
       (4350,4430,'relative regularity'),(4510,4570,'polynomial determinant')]
}
LIMITS = {
 'A': 'Use actual primary FS/CPSH/decreasing-net PSH and energy conventions. Printed J and index slips are corrected explicitly in the argument. No new moving-field unbounded operator theorem is inferred.',
 'B': 'Printed E=S is not used: the cumulative factor is n/(n+1). The mL radial coordinate argument is replaced by actual degree-one frames.',
 'C': 'The E-downarrow theorem does not require envelopes. Its rational-projective proof uses an additional asymptotic FS/graded-norm approximation, which is NOT reconstructed in this deliverable.',
 'D': 'Diagnostic only. A common linear mixed-form framework is not inferred from nonlinear roots.',
 'E': 'Diagnostic only; the regularization/envelope chain is not a premise.',
 'F': 'The whole Theorem 4.13 is under standing smooth-projective hypotheses. Its Lemma 4.15 proof invokes an external lattice saturation lemma; no unproved extension to all singular quotients is used.',
 'G': 'Actual pure-dimensional, separated, boundaryless analytifications; proper finite map with generic calibrated degree d; integer-paralinear metrics after tensor powers for FS. Weighted continuity is bounded/local-uniform only.',
 'H': 'Normal projective quotient, ample line bundle, finitely generated integer Rees after index clearing. Base change, tensoring, and multiplying a relative potential are distinguished. Model probability normalization has only one factor 1/V.',
 'I': 'Geometrically reduced projective scheme, ample L and auxiliary ample M, continuous psh metrics. Lemma 3.2/Thm 3.1 do not require envelope continuity. Raw volume is divided by (L^p) here.',
 'J': 'Actual v3 numbering. Thm 9.15 is continuous-psh equality, not non-psh obstacle equality. Cor 9.16 is conditional. FS supnorm isometry alone does not compare the generated higher-degree determinant means.'
}

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def main():
 out=[]; valid=True
 for i,source in enumerate(SOURCES):
  code=chr(65+i); files=[]
  for key in ['pdf','literal_extract','abstract_html','html','fresh_official_versioned_pdf']:
   if key not in source: continue
   hashkey={'literal_extract':'extract_sha256','abstract_html':'abstract_sha256',
            'fresh_official_versioned_pdf':'fresh_official_pdf_sha256'}.get(key,key+'_sha256')
   actual=sha(source[key]); expected=source.get(hashkey)
   ok=actual==expected; valid &= ok
   files.append({'kind':key,'path':source[key],'sha256':actual,'expected_sha256':expected,'matches':ok})
  raw=Path(source['literal_extract']).read_bytes(); lines=raw.decode('utf-8').split('\n')
  ex=[]
  for a,b,label in RANGES[code]:
   assert 1<=a<=b<=len(lines)
   ex.append({'id':f'{code}-{a}-{b}','label':label,'inclusive_one_based_LF_range':[a,b],
              'literal_text':'\n'.join(lines[a-1:b]),'application_and_limit':LIMITS[code]})
  out.append({'id':code,'version':source['saved_version'],'title':source.get('title'),
              'public_source':source['public_source'],'files':files,'LF_split_length':len(lines),
              'whole_body_read':False,'excerpts':ex,'checked_application':LIMITS[code]})
 preservation=json.loads((ROOT/'preservation.json').read_text())
 assert (ROOT/'input.json').read_bytes()==(ROOT/'input-original.json').read_bytes()
 assert sha(ROOT/'input.json')==preservation['input_sha256']
 inp=json.loads((ROOT/'input.json').read_text())
 assert (ROOT/'assignment-original.txt').read_text()==inp['assignment']
 assert json.loads((ROOT/'task-original.json').read_text())==inp['task']
 dest=ROOT/'source-extracts';dest.mkdir(exist_ok=True)
 report={'LF_method':"UTF-8 bytes decoded then split('\\n'); endpoints inclusive and one-based",
         'all_supplied_hashes_match':bool(valid),'source_count':len(out),
         'excerpt_count':sum(len(z['excerpts']) for z in out),'sources':out,
         'preservation':preservation,'epistemic_status':'Source statements and applications are draft mathematical evidence; hashes do not certify correctness.'}
 (dest/'source-provenance.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
 assert valid
 print(json.dumps({k:report[k] for k in ['all_supplied_hashes_match','source_count','excerpt_count']}))

if __name__=='__main__':main()
