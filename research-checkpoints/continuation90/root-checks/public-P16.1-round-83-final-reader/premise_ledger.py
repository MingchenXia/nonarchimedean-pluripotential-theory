from pathlib import Path
import json,re,hashlib
ROOT=Path(__file__).resolve().parent
def sha(b): return hashlib.sha256(b).hexdigest()
specs=[
 ('0BXQ',20,34,'Finite normalization of a locally algebraic scheme over a field; reduced integral schemes have finite birational normalization.','n1 curve normalization; n2 integral h and finite R[h].'),
 ('031T',23,33,'A Noetherian normal domain equals the intersection of its height-one localizations.','n2 integrality from all height-one bounds.'),
 ('00PD',24,39,'A one-dimensional Noetherian normal local domain is a DVR, equivalently regular local of dimension one.','n1 curve local rings; n2 height-one valuations.'),
 ('0BBZ',23,28,'In a Noetherian ring, a prime minimal over r equations has height at most r.','n1 every reduced slice component is horizontal.'),
 ('02IJ',22,48,'For an injective finite-type map of Noetherian domains the dimension inequality holds, with equality over a universally catenary base; apply to a field.','n1 slice component dimension, retaining the field/domain hypotheses.'),
 ('0B8Y',23,38,'For a curve, normality at a closed point is equivalent to a DVR; over a perfect field it is equivalent to smoothness.','n1 normalized characteristic-zero horizontal curves.'),
 ('0BXX',26,28,'A nonconstant morphism of curves with normal target is flat, by torsion freeness over a DVR.','n1 normalized finite curve cover has rank d.'),
 ('0BX4',92,107,'A rational relative morphism from a Noetherian reduced curve extends at a valuation local ring when its target is proper over the SAME base scheme; uniqueness is separatedness.','n1 proper lift to the original witness; the witness need not be proper over F.'),
 ('0B1P',22,24,'Projection from a point outside a closed projective subscheme is finite, retaining projectivity and avoidance of that subscheme.','n3 finite projective projections.'),
 ('0B1Q',23,36,'Secant and tangent avoidance gives a local isomorphism under finite projection at a smooth point when the subvariety dimension is below ambient dimension minus one.','n3 proof prototype; reduced-union extension is proved by local Nakayama rather than asserted from this statement.'),
 ('0478',23,27,'A scheme locally of finite type over a field is Jacobson; closed residue fields are algebraic over that field.','n3 closed-point affine cover covers every scheme and analytic point.'),
 ('0B8X',23,29,'For a reduced locally algebraic scheme over a perfect field, its regular locus is its dense open smooth locus.','n3 successive reduced singular strata strictly drop dimension.')]
pages=[]
for fn in sorted(ROOT.glob('web-primary-*.json')):
 data=json.loads(fn.read_bytes())
 for block in data.get('content',[]):
  if block.get('type')!='text':continue
  for part in re.split(r'\n-{20,}\n',block['text']):
   m=re.search(r'^.*\(https://stacks.math.columbia.edu/tag/([A-Za-z0-9]+)\)',part)
   if not m:continue
   rows={int(m[1]):m[2] for line in part.split('\n') if (m:=re.match(r'L(\d+): ?(.*)',line))}
   if rows:pages.append((m if False else re.search(r'https://stacks.math.columbia.edu/tag/([A-Za-z0-9]+)',part)[1],fn,part,rows))
(ROOT/'web-extracts').mkdir(exist_ok=True)
premises=[];passages=[]
for index,(tag,lo,hi,claim,application) in enumerate(specs):
 cand=[p for p in pages if p[0]==tag and all(i in p[3] for i in range(lo,hi+1))]
 assert cand,(tag,lo,hi)
 _,fn,page,rows=max(cand,key=lambda p:len(p[3]))
 # Coordinates are LF of a RETAINED UTF8 rendered snapshot; original HTML LF is unavailable.
 snapshot=f'web-extracts/{tag}-rendered-snapshot.txt'
 (ROOT/snapshot).write_text(page,encoding='utf-8')
 ls=(ROOT/snapshot).read_bytes().decode('utf8').split('\n')
 positions=[i+1 for i,l in enumerate(ls) if re.match(r'L(\d+):',l) and lo<=int(re.match(r'L(\d+):',l)[1])<=hi]
 a,z=min(positions),max(positions)
 literal='\n'.join(ls[a-1:z]);unit=f'web-extracts/{tag}-statement-proof.txt'
 (ROOT/unit).write_text(literal,encoding='utf8')
 premises.append({'index':index,'statement':claim,'hypotheses_and_application':application})
 passages.append({'id':f'p{index}','premise':index,'url':f'https://stacks.math.columbia.edu/tag/{tag}','edition':'Public page rendered by web service, retrieved 2026-10-05; not asserted immutable.','snapshot':snapshot,'snapshot_sha256':sha((ROOT/snapshot).read_bytes()),'inclusive_one_based_LF':[a,z],'web_rendered_line_labels':[lo,hi],'coordinate_rule':"Stored UTF8 bytes decode and split('\\n'); LF is of rendered snapshot, not original HTML.",'literal_file':unit,'literal_sha256':sha(literal.encode()),'evidence_container':fn.name,'coverage':'Complete pertinent statement/proof unit retained; recursive cited library facts are standard primary premises, not claimed independently re-proved.'})
index=len(premises);lo,hi=3825,3842
raw=(ROOT/'sources/S6-literal_extract.txt').read_bytes();ls=raw.decode('utf8').split('\n')
literal='\n'.join(ls[lo-1:hi]);path=f'source-extracts/S6-LF{lo}-{hi}.txt'
assert (ROOT/path).read_bytes()==literal.encode()
premises.append({'index':index,'statement':'Thuillier 3.1.9: a subharmonic function on a neighborhood of a connected strictly affinoid curve domain has finite values on its Shilov boundary.','hypotheses_and_application':'n1 finite-value strict-disc radial comparison; the identically-minus-infinity alternative is handled separately by usc.'})
passages.append({'id':f'p{index}','premise':index,'url':'https://theses.hal.science/tel-00010990v1/document','edition':'tel-00010990v1','source':'sources/S6-literal_extract.txt','source_sha256':sha(raw),'inclusive_one_based_LF':[lo,hi],'coordinate_rule':"UTF8 bytes decode and split('\\n'); inclusive one-based LF.",'literal_file':path,'literal_sha256':sha(literal.encode()),'coverage':'Complete statement and proof.'})
out={'premises':premises,'passages':passages,'background_assumptions':['Exact task-granted round77 bodies and round80 PASS, with rational contact restrictions, geometric antecedents, and all binding reading clarifications. These are background, not external premises with negative indices.'],'scope':'External premises are cited primary standard statements with actual HTTP(S) evidence; joint applications remain unverified drafts.'}
(ROOT/'external-premises.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps({'external_premises':len(premises),'passage_coverage':sorted(p['premise'] for p in passages)}))
