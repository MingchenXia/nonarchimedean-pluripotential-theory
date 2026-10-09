from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess
R=Path('/workspace/research');K=R/'root-checks'
S=R/'primary-data-LOCALONLY/P16.7-classical-PSH-Shilov-GR-v2-primary-20261009'
P=R/'shared-sources/GR-2506.13548v2-20261004.pdf'
T=R/'shared-sources/GR-2506.13548v2-20261004.txt'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not S.exists()
assert sha(P)=='83ca9a19394f44bb2e4e1aa316de95938f311acd53a00fe250fa0f605184b726'
assert sha(T)=='3a221b86116604c950db07e4c60ab184701f0624deebabd92502e5c81871436b'
assert P.stat().st_size==473505 and b'2506.13548v2' in T.read_bytes()[:1500]
S.mkdir()
for p in [P,T]:shutil.copyfile(p,S/('GR2506.13548v2-full-LOCALONLY'+p.suffix))
lines=T.read_text().split('\n');units=[]
ranges=[(1,200,'Entireintro exactbridge1.2 and theorem/hypothesis context'),(365,540,'EntireDef3.4/3.5statement and exact Thuillier definition/smooth case'),(635,677,'Entire3.5(1)sheaf and3.5(2)analytic-function immediate proofs'),(785,949,'Entire3.5(4,5)immediateproof plus entire3.5(6,7,8)immediateproofs'),(1040,1185,'EntireDefs3.13/4.1 plus entireProp4.2statement/immediateproof'),(1198,1400,'Entireanalytic/overconvergentcurveDefinition5.1 and5.2statement/immediateproof'),(1400,1422,'Entire5.4connectivitystatement/context'),(1538,1615,'Entire5.4immediateproof'),(1614,1832,'Entire6.1statement/immediateproof,6.2 and6.3statements/immediateproofs,6.4and6.5statements/immediateproofs')]
for lo,hi,scope in ranges:
    p=S/f'GR-v2-real-LF-{lo}-{hi}-LOCALONLY.txt';p.write_text('\n'.join(lines[lo-1:hi])+'\n')
    units.append(dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p),source_sha256=sha(T),literal_LF_inclusive=[lo,hi],line_convention="split('\\n') with FF inside line",scope=scope,ROOT_entire_physical_text_read_untruncated=True,deep_recursive_dependencies_NOT_all_freshly_read=True,LOCALONLY=True))
pixels=[]
for page in [3,33,34]:
    prefix=S/f'GR-v2-original-page-{page}-LOCALONLY'
    subprocess.run(['pdftoppm','-f',str(page),'-l',str(page),'-r','145','-png','-singlefile',str(P),str(prefix)],check=True,capture_output=True)
    p=prefix.with_suffix('.png');pixels.append(dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p),original_PDF_page=page,ROOT_actual_pixels_NOT_yet_read=True,LOCALONLY=True))
record=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),title='Classically psh and pluriharmonic functions on Berkovich spaces',authors=['Walter Gubler','Joseph Rabinoff'],version='Exact cached arxiv2506.13548v2 header17Sep2025; no freshnetwork or publicationbyteidentity claim',public_citation='https://arxiv.org/abs/2506.13548v2',full_pdf=dict(path=str(S/'GR2506.13548v2-full-LOCALONLY.pdf'),bytes=P.stat().st_size,sha256=sha(P)),full_extract=dict(path=str(S/'GR2506.13548v2-full-LOCALONLY.txt'),bytes=T.stat().st_size,sha256=sha(T)),actual_units=units,rendered_original_pages=pixels,ROOT_entire_GR_paper_NOT_freshly_read=True,supplied_or_native_programs_executed_or_imported=False,all_full_primary_units_pixels_LOCALONLY=True)
p=K/'P16.7-GR2506-v2-primary-text-and-pixel-retention-for-ROOT395-20261009.json';p.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(record=str(p),record_sha256=sha(p),units=len(units),rendered_pixels=[e['path'] for e in pixels]),indent=2))
