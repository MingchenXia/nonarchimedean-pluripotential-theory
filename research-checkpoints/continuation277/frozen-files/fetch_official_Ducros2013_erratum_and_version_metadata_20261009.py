from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, subprocess, urllib.request
P=Path('/workspace/research/primary-data-LOCALONLY/P16.7-Ducros2012-local-tropical-dimension-20261009')
O=P/'public-official-erratum-and-version-retrieval-metadata.json'; assert P.exists() and not O.exists()
url='https://www.numdam.org/item/10.5802/cml.7.pdf'; record=dict(url=url,LOCALONLY=True,whole_proof_read=False,correctness_grant=False)
try:
    with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Research primary-source verification'}),timeout=40) as res:
        b=res.read(12*1024*1024+1); final_url=res.url
    assert b.startswith(b'%PDF-') and len(b)<=12*1024*1024
    pdf=P/'Ducros2013-official-DOI-cml7-erratum.pdf'; txt=pdf.with_suffix('.txt'); pdf.write_bytes(b)
    subprocess.run(['pdftotext','-layout',str(pdf),str(txt)],check=True,capture_output=True)
    record.update(final_url=final_url,pdf=str(pdf),pdf_bytes=len(b),pdf_sha256=hashlib.sha256(b).hexdigest(),whole_literal_text=str(txt),text_bytes=txt.stat().st_size,text_sha256=hashlib.sha256(txt.read_bytes()).hexdigest())
except Exception as e:record.update(retrieval_failed=True,error_type=type(e).__name__,error=str(e)[:300])
meta=dict(retrieved_utc=datetime.now(timezone.utc).isoformat(),source=record,version_correction='Author erratum PDF actually prints43-44/2013 anddifferent received/revised dates; official journal metadata DOI10.5802/cml.7 prints47-48 and received08June/revised08September2013. Do not conflate these versions or infer raw-author-PDF identity from journal metadata. Author tropic.pdf is an earlier proof version without the later numbered local3.4; tropicbis.pdf contains complete3.4 and agrees with currentCLD12.2.8 application, but no revisiondate or official-PDF identity is inferred. Entire theorem/proof and erratum content must be read separately.',all_full_PDF_text_bodies_LOCALONLY=True,no_auth_proxy_CA_runtime_change=True,no_active_math_feedback=True)
O.write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n'); print(json.dumps(meta,ensure_ascii=False,indent=2))
