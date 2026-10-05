#!/usr/bin/env python3
"""Freeze supplied primary bytes and selected public-browser evidence locally."""
import hashlib,json,pathlib,re,shutil,subprocess,platform
ROOT=pathlib.Path(__file__).resolve().parent
S=ROOT/'sources'; S.mkdir(exist_ok=True)
def sha(b): return hashlib.sha256(b).hexdigest()
catalog=[('cld','/workspace/research/shared-sources/CD-1204.6277v2-20261004.txt','64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085','https://arxiv.org/pdf/1204.6277v2','25 July 2025'),('gjr','/workspace/research/shared-sources/GJR2111.05741v3-20261005-continuation72.txt','57dfcae1d8dfc25d5ef217f34fabe9e80b679ec2956db1bced3b31bc9afdf8d3','https://arxiv.org/pdf/2111.05741v3','7 March 2025')]
units={
 'cld': [('ordinary-domain',14983,15012),('analytic-calculus',22105,22126),('generic-lengths',23434,23459),('generated-psh',9729,9781),('generated-cpsh',9797,9863),('positive-decomposition',7359,7381),('middle-positivity',7918,7981),('positive-scalar-measures',7983,8011),('ordinary-product',8054,8076),('current-sheaf',7756,7818),('current-differentials',9309,9381),('cutoffs-density',21619,21696),('form-leibniz',3769,3803),('smooth-multiplier',10287,10326),('bt-definition',10347,10383),('middle-matrix',885,975),('positive-wedges',1026,1040),('current-topology',7659,7736),('compact-moment-image',16836,16840),('chart-images',3685,3701)],
 'gjr': [('field',339,343),('weak-harmonic',3365,3386),('current-psh',2529,2581),('strong-current',3618,3636)]}
units['cld'].append(('top-measures',6733,6808))
units['cld'].append(('geometric-positive-wedges',4074,4081))
units['cld'].append(('face-positive-wedges',2685,2699))
units['cld'].append(('face-positivity',2634,2651))
manifest={'coordinate_convention':"UTF8 bytes decode('utf8').split('\\n'); inclusive one-based LF; units omit terminal added LF",'sources':[],'units':[],'partial_reading':True,'whole_sources_read':False}
for key,path,expected,url,date in catalog:
 dst=S/(key+'-full.txt')
 b=dst.read_bytes() if dst.exists() else pathlib.Path(path).read_bytes(); assert sha(b)==expected
 dst.write_bytes(b)
 manifest['sources'].append({'id':key,'path':str(dst.relative_to(ROOT)),'supplied_read_only_path':path,'sha256':sha(b),'url':url,'version_date':date,'acquisition':'task-supplied primary text cache, frozen verbatim','entire_text_read':False})
 lines=b.decode('utf8').split('\n')
 for name,a,z in units[key]:
  u='\n'.join(lines[a-1:z]).encode('utf8'); p=S/(key+'-'+name+'.txt');p.write_bytes(u)
  manifest['units'].append({'id':key+'-'+name,'source':key,'path':str(p.relative_to(ROOT)),'url':url,'lf_first':a,'lf_last_inclusive':z,'sha256':sha(u),'source_sha256':sha(b)})
# Raw public browser outputs are the byte provenance, not a downloaded PDF.
rawfiles=sorted(S.glob('gr-web-*.json')); indexed={}
for p in rawfiles:
 d=json.loads(p.read_text())
 for item in d['content']:
  if item.get('type')!='text':continue
  for l in item['text'].split('\n'):
   m=re.match(r'L(\d+)@P[^:]*: (.*)',l)
   if m:
    n=int(m[1]); value=m[2]
    if n in indexed: assert indexed[n]==value,(n,indexed[n],value)
    indexed[n]=value
gr_ranges=[('inclusion',71,83),('field',141,148),('maximum-proof',3074,3112),('pluriharmonic',3130,3180),('limits-semistable',3181,3250)]
gr_ranges.append(('classical-definition',1638,1663))
for name,a,z in gr_ranges:
 assert all(i in indexed for i in range(a,z+1)),(name,[i for i in range(a,z+1) if i not in indexed])
 b='\n'.join(indexed[i] for i in range(a,z+1)).encode('utf8');p=S/('gr-'+name+'.txt');p.write_bytes(b)
 manifest['units'].append({'id':'gr-'+name,'source':'gr-web','path':str(p.relative_to(ROOT)),'url':'https://arxiv.org/pdf/2506.13548v2','lf_first':1,'lf_last_inclusive':len(b.decode('utf8').split('\n')),'web_zero_based_line_first':a,'web_zero_based_line_last_inclusive':z,'sha256':sha(b),'source_sha256':None,'acquisition':'literal lines from saved public PDF browser view; prefixes removed, typography unchanged'})
manifest['sources'].append({'id':'gr-web','url':'https://arxiv.org/pdf/2506.13548v2','version_date':'17 September 2025','acquisition':'public PDF browser extraction; original PDF bytes unavailable','original_pdf_sha256':None,'raw_responses':[{'path':str(p.relative_to(ROOT)),'sha256':sha(p.read_bytes())} for p in rawfiles],'read_scope':'sections 1.2, 7.1--7.8, supporting Theorem 6.4 proof; not the whole paper'})
(ROOT/'source-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
env={'python':platform.python_version(),'platform':platform.platform(),'tools':{},'network':'shell curl public GR PDF failed: proxy port 8080 unavailable; public browser read succeeded','supervised_heavy_compute':'none supplied; none needed or launched','agents':'no workers or other models invoked'}
for cmd in ['pandoc','pdflatex','pdftotext','curl']:
 r=subprocess.run([cmd,'--version'],capture_output=True,text=True);env['tools'][cmd]=r.stdout.split('\n')[0]
(ROOT/'environment.json').write_text(json.dumps(env,indent=2)+'\n')
print(f'Frozen {len(manifest["sources"])} primary source records and {len(manifest["units"])} literal units.')
