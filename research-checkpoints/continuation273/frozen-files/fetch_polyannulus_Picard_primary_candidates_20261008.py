from pathlib import Path
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor
import hashlib, json, subprocess, urllib.request

S=Path('/workspace/research/primary-data-LOCALONLY/P16.7-polyannulus-Picard-primary-20261008')
assert not S.exists(); S.mkdir()
targets=[('Gerritzen-1977-Picard-decompositions','https://www.numdam.org/item/CM_1977__35_1_23_0.pdf','L. Gerritzen, Compositio35(1977),23-38'),('Fresnel-vanDerPut-1983-formal-localization-Picard','https://www.numdam.org/item/AIF_1983__33_4_19_0.pdf','Jean Fresnel and Marius van der Put, AIF33(1983),19-82; NOT Gerritzen'),('Kerz-Saito-Tamme-2016August-Pic-pro','https://www.lcv.ne.jp/~smaki/articles/Pic-pro2016August.pdf','Kerz, Saito and Tamme author2016August version; pro-homotopy versus ordinary Pic invariance distinct')]
def retrieve(entry):
    name,url,identity=entry; record=dict(name=name,url=url,primary_identity=identity,reading='Retained source only; complete theorem/proof reading follows; no correctness grant or Pic=0 inference.')
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'Research primary-source reader/1.0'})
        with urllib.request.urlopen(req,timeout=25) as response:data=response.read(8*1024*1024+1); record['final_url']=response.geturl()
        assert len(data)<=8*1024*1024 and data.startswith(b'%PDF-')
        p=S/(name+'.pdf'); p.write_bytes(data); t=p.with_suffix('.txt')
        subprocess.run(['pdftotext','-layout',str(p),str(t)],capture_output=True,check=True)
        record.update(success=True,files=[dict(path=str(q),bytes=q.stat().st_size,sha256=hashlib.sha256(q.read_bytes()).hexdigest(),LOCALONLY=True) for q in [p,t]])
    except Exception as exc:record.update(success=False,error_type=type(exc).__name__,error=str(exc)[:300])
    return record
with ThreadPoolExecutor(max_workers=3) as pool:records=list(pool.map(retrieve,targets))
x=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),records=records,
    source_discovery_correction='AIF1983 formal-localization paper is by Fresnel/van der Put, not Gerritzen. Older discovery-only author attribution corrected; no applied proof grant was based on that error.',
    no_active_native270_or271_feedback=True,no_other_ACTIVE_mathematics_read=True,all_full_primary_bodies_LOCALONLY=True,supplied_or_native_programs_executed_or_imported=False)
(S/'public-primary-candidate-retrieval-and-author-correction.json').write_text(json.dumps(x,indent=2)+'\n')
print(json.dumps(x,indent=2))
