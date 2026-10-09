from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, subprocess, urllib.request
P=Path('/workspace/research/primary-data-LOCALONLY/P16.7-Ducros2012-local-tropical-dimension-20261009')
assert not P.exists(); P.mkdir(parents=True)
records=[]
sources=[('Ducros2012-author-tropic','https://webusers.imj-prg.fr/~antoine.ducros/tropic.pdf'),('Ducros2012-author-tropicbis','https://webusers.imj-prg.fr/~antoine.ducros/tropicbis.pdf'),('Ducros2013-author-erratum','https://webusers.imj-prg.fr/~antoine.ducros/erratum-squelettes.pdf')]
for name,url in sources:
    q=urllib.request.Request(url,headers={'User-Agent':'Research primary-source verification'})
    try:
        with urllib.request.urlopen(q,timeout=40) as res:
            final_url=res.url; content_type=res.headers.get('Content-Type'); b=res.read(24*1024*1024+1)
        assert len(b)<=24*1024*1024 and b.startswith(b'%PDF-'),name
        pdf=P/(name+'.pdf'); pdf.write_bytes(b); txt=P/(name+'.txt')
        subprocess.run(['pdftotext','-layout',str(pdf),str(txt)],check=True,capture_output=True)
        records.append(dict(url=url,final_url=final_url,content_type=content_type,pdf=str(pdf),pdf_bytes=len(b),pdf_sha256=hashlib.sha256(b).hexdigest(),whole_literal_text=str(txt),text_bytes=txt.stat().st_size,text_sha256=hashlib.sha256(txt.read_bytes()).hexdigest(),LOCALONLY=True,whole_proof_read=False,correctness_grant=False))
    except Exception as e:
        records.append(dict(url=url,retrieval_failed=True,error_type=type(e).__name__,error=str(e)[:300],no_auth_proxy_CA_or_runtime_change=True,correctness_grant=False))
meta=dict(retrieved_utc=datetime.now(timezone.utc).isoformat(),sources=records,authentication='CLDv2bibliography[50] identifies DucrosConfluentesMath4(2012)4 1250007,57pages arXiv1203.6498. Authorpublication page/journal DOI10.1142/S1793744212500077 authenticates original; separate journalerratum DOI10.5802/cml.7 volume5(2013)2 pp47-48. Retrieved full author PDFs/text are version DATA; theorem/immediateproof and erratum require fresh reading before application.',all_full_PDF_text_bodies_LOCALONLY=True,supplied_or_native_programs_executed_or_imported=False,other_ACTIVE_math_read_or_feedback=False)
(P/'public-primary-retrieval-metadata.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(meta,ensure_ascii=False,indent=2))
