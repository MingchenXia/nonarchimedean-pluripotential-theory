from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os,re,ssl,subprocess,urllib.request

D=Path('/workspace/research/primary-data-LOCALONLY/P12.3-singular-test-ideal-generation-primary-20261008')
D.mkdir(parents=True,exist_ok=True)
context=ssl.create_default_context(cafile=os.environ.get('SSL_CERT_FILE'))
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
normal=lambda s:re.sub('[^a-z0-9]','',s.lower())
items=[
 ('Smolkin-subadditivity-1805.08739v3','https://arxiv.org/pdf/1805.08739v3','A New Subadditivity Formula for Test Ideals','https://arxiv.org/abs/1805.08739v3','Corrected3.12/5.15 in latestv3; v2 NOT applied'),
 ('CEMS-anticanonical-1412.6453v4','https://arxiv.org/pdf/1412.6453v4','Test ideals in rings with finitely generated anti-canonical algebras','https://arxiv.org/abs/1412.6453v4','Latestv4 corrects too-strong Lemma2.10 including published version; exact correction must be read'),
 ('Schwede-canonical-linear-system-1107.3833v4','https://arxiv.org/pdf/1107.3833v4','A canonical linear system associated to adjoint divisors in characteristic','https://arxiv.org/abs/1107.3833v4','Projective algclosed field scope may not cover affine-base model'),
 ('HLS-mixed-characteristic-generation-2106.14329v4','https://arxiv.org/pdf/2106.14329v4','Global generation of test ideals in mixed characteristic and applications','https://arxiv.org/abs/2106.14329v4','Latestarxivv4 December2022 distinct from final2024 publishedPDF; no conflation'),
 ('HLS-mixed-characteristic-generation-published2024','https://api.algebraicgeometry.nl/Article/20655/2024-5-020.pdf','Global generation of test ideals in mixed characteristic and applications','https://api.algebraicgeometry.nl/Article/20655/2024-5-020.pdf','PublishedAlgebraicGeometry11(5)(2024)676-711; entire primary reading required before use')]
records=[]
for name,url,title,metadata,scope in items:
    rec=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),public_url=url,bibliographic_primary_page=metadata,expected_title=title,version_scope=scope,credential_access=False,proxy_CA_auth_changed=False,primary_bodies_LOCALONLY=True,mathematical_theorems_proofs_NOT_YET_read=True,source_not_operational_authority=True)
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'Mathematical primary source verification'})
        with urllib.request.urlopen(req,context=context,timeout=15) as res:
            data=res.read(16000001);assert len(data)<=16000000 and data.startswith(b'%PDF');final=res.geturl()
        p=D/(name+'.pdf');t=p.with_suffix('.txt');assert not p.exists() and not t.exists();p.write_bytes(data)
        out=subprocess.run(['pdftotext','-layout',str(p),str(t)],capture_output=True,text=True);assert out.returncode==0
        assert normal(title) in normal(t.read_text()[:18000]),'Primarytitle does not match expected metadata'
        rec.update(status='Whole public primaryPDF retrieved and titlematched; mathematical applied units NOTYET read',final_url=final,pdf=dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)),text=dict(path=str(t),bytes=t.stat().st_size,sha256=sha(t)))
    except Exception as exc:rec.update(status='Retrieval/titleauthentication did not complete',error_type=type(exc).__name__,diagnostic=str(exc)[:300],no_theorem_import=True)
    records.append(rec);print(json.dumps(rec,ensure_ascii=False,indent=2),flush=True)
M=D/'public-singular-test-generation-primary-retrieval-records.json';assert not M.exists();M.write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
