from pathlib import Path
import json,hashlib,shutil
ROOT=Path(__file__).resolve().parent
sha=lambda b:hashlib.sha256(b).hexdigest()
sources=json.loads((ROOT/'sources.json').read_text())
(ROOT/'sources').mkdir(exist_ok=True)
(ROOT/'source-extracts').mkdir(exist_ok=True)
files=[]; byid={}
for item in sources:
 sid=item['audit_id']; byid[sid]=item
 for key in ('pdf','literal_extract','abstract_html','html','fresh_official_versioned_pdf'):
  if key not in item:continue
  p=Path(item[key]); data=p.read_bytes()
  hashkey={'pdf':'pdf_sha256','literal_extract':'extract_sha256','abstract_html':'abstract_sha256','html':'html_sha256','fresh_official_versioned_pdf':'fresh_official_pdf_sha256'}[key]
  assert sha(data)==item[hashkey],(sid,key,'hash mismatch')
  out=ROOT/'sources'/p.name
  out.write_bytes(data)
  files.append({'id':sid,'kind':key,'authorized_path':str(p),'copy':str(out.relative_to(ROOT)),'version':item['saved_version'],'bytes':len(data),'sha256':sha(data)})
units=[
 ('A',277,346,'Actual FS and CPSH definitions; primary lists and local uniform completion.'),
 ('A',762,805,'Actual decreasing-net PSH definition and closure; the proof is retained but no disputed finite-quasimonomial sup-detection argument is imported.'),
 ('C',2241,2290,'Compact directed refinement of nested decreasing genuine approximants. Used only to explain actual decreasing-net closure.'),
 ('C',2513,2547,'Finite divisorial detection and continuity of suprema against continuous obstacles. Applies on the actual projective quotient, without a smoothness assumption.'),
 ('C',2797,2844,'Envelope definition and equivalence with normalized projective weak compactness; full proof retained, including Tychonoff and decreasing tail envelopes.'),
 ('C',2980,3064,'Smooth characteristic-zero EP and compactness, with full multiplier-ideal proof body. Used only with an actual smooth connected projective quotient and ample L_d.'),
 ('C',3659,3693,'Genuine projective energy pairing: definition, full upper-semicontinuity and decreasing-net proof.'),
 ('C',3788,3824,'Definition7.6 and Proposition7.7: normalized genuine energy, E1, usc and decreasing continuity.'),
 ('C',3971,4059,'Continuous model MA integrals are weakly continuous; part of bounded-energy target continuity proof.'),
 ('C',4074,4148,'Projective weighted decreasing-net convergence with proof. The test-containing pairing minus the zero-test pairing has the correct sign; the reversed display is not used.'),
 ('C',5170,5262,'Uniform finite-energy target integration and Proposition9.19 with proof. Correct the displayed absolute-value identity at LF5254 to 2max(a,b)-a-b.'),
 ('C',5263,5302,'Projective finite-energy probability/integrability criterion. The transferred target is a supported probability on the full quotient.'),
 ('C',6033,6147,'Strong-topology and equation statements, complete equivalence proof. Diagnostic: on projective spaces, completeness is equivalent to EP; not used as a cone surjectivity theorem.')
]
applications=[]
for num,(sid,lo,hi,limit) in enumerate(units,1):
 p=Path(byid[sid]['literal_extract']); raw=p.read_bytes(); lines=raw.decode('utf-8').split('\n')
 assert 1<=lo<=hi<=len(lines)
 literal='\n'.join(lines[lo-1:hi]); name=f'{num:02d}-{sid}-LF{lo}-{hi}.txt'
 (ROOT/'source-extracts'/name).write_text(literal,encoding='utf-8')
 applications.append({'id':f'e{num}','source':sid,'version':byid[sid]['saved_version'],'extract_sha256':sha(raw),'inclusive_one_based_LF':[lo,hi],'coordinate_rule':"UTF-8 bytes decode, split('\\n'); inclusive endpoints",'file':name,'literal':literal,'excerpt_sha256':sha(literal.encode()),'application_and_limit':limit})
report={'files':files,'literal_units':applications,'source_count':len(sources),'file_count':len(files),'mathematical_status':'Read evidence and scope checks; matching hashes do not validate mathematical applications.'}
(ROOT/'source-extracts'/'source-provenance.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'source_count':len(sources),'file_count':len(files),'literal_units':len(units),'hashes_match':True}))
