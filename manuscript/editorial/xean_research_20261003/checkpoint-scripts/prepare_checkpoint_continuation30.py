"""Freeze reviewed two-graph paper and fresh many-factor continuation."""
from pathlib import Path
import datetime,hashlib,json,shutil
r=Path('/workspace/research');c=r/'github-checkpoint';parent='42005e1c537841b017b365cc6b8730b983a2e54e';a=json.loads((r/'active-work.json').read_text());assert a['github_checkpoint']['commit_sha']==parent and not a['full_solutions']
snapshot=c/'continuation30-uploaded-live-records';snapshot.mkdir(exist_ok=False);prefix='manuscript/editorial/xean_research_20261003/';files=[]
def add(path,target,mutable=False):
 p=Path(path);assert p.is_file(),p
 if mutable:
  cp=snapshot/(str(len(files))+'-'+p.name);shutil.copyfile(p,cp);p=cp
 assert prefix+target not in {x['path'] for x in files};files.append({'local':str(p),'path':prefix+target,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
m=json.loads((r/'deliverables/round-23-bundle-manifest.json').read_text());assert m['entry_count']==20 and not m['fully_solved_original_atoms']
for n,digest in m['entries'].items():
 p=r/'deliverables/round-23'/n;assert hashlib.sha256(p.read_bytes()).hexdigest()==digest;add(p,'round-23/'+n)
for n in ('reviewed-papers-round-23.zip','round-23-bundle-manifest.json','round-23-source-preparation.json','round-23-visual-check.json','round-23-native-verification-pending.json','round-23-native-panel-attempt-1.json'):add(r/'deliverables'/n,n)
v=r/'campaigns/round-22/P05.2-arbitrary-graph-product-review';review=json.loads((v/'run.json').read_text())['campaign'];assert review['status']=='completed' and review['result']['verdict']=='PASS'
for n in ('run.json','freeze.json','source-artifact-binding.json','review-read-attestation.json','root-draft-read-record.json','publication-edits.json'):add(v/n,'reviews/round-23/'+n)
for n in ('prepare_round23_arbitrary_graph_source.py','prepare_round23_arbitrary_graph_source_v2.py','publish_round23.py','prepare_finitely_many_graph_products.py','review_finitely_many_graph_products_after_completion.py','prepare_many_graph_intersection_evidence.py'):add(r/n,'checkpoint-scripts/'+n)
d=r/'campaigns/round-24/P05.2-finitely-many-graph-products'
for n in ('input.json','settings.json','input-manifest.json'):add(d/n,'continuation-inputs/finitely-many-graph-products/'+n)
for n in ('P05.2-finite-many-graph-product-proposal.md','P05.2-many-graph-intersection-primary-evidence.md'):add(r/n,'root-proposals/'+n)
s=r/'shared-sources/many-graph-product-intersection-20261004'
for n in ('arxiv-record.html-retrieval.json','Allermann-Rau-0709.3705.pdf-retrieval.json','root-primary-read-and-evidence.json'):add(s/n,'source-authentication/many-graph-intersection/'+n)
add(r/'shared-sources/Thuillier-additional-skeleton-source-read-20261004.json','source-authentication/Thuillier-additional-skeleton-source-read-20261004.json')
add(c/'push-receipt-continuation29.json','records/push-receipt-continuation29.json')
for n in ('active-work.json','checklist-current.json','checklist-current.tsv','refresh_checklist.py'):add(r/n,n,mutable=True)
add(Path(__file__),'checkpoint-scripts/'+Path(__file__).name);p=c/'push_checkpoint_continuation30.py';assert not p.exists();s=(c/'push_checkpoint_continuation29.py').read_text().replace('continuation29','continuation30').replace('Checkpoint arbitrary graph proof and fresh curve source repair','Publish reviewed arbitrary two-graph contact classification');p.write_text(s);add(p,'checkpoint-scripts/'+p.name)
p=snapshot/'CHECKPOINT.txt';p.write_text('Checkpoint30: Reviewed arbitrary TWO finite-graph product each-real-reference classification, PASS0/0 fully read/bound;25-page paper with full frozen argument and20entry reproducibility bundle. Criterion: both local relation cones rank1 and at least1factor unbranched; higher-rank/full two-branch failures have actual PAPC regularizable raw envelopes, unchanged prescribed reference at infinity, completely evaluated negative contact. Harmless reviewer corrections logged. Two unchanged-source pdfLaTeX exports have zero layout/glyph/undefined warnings; only firstpage visually checked. Native editor open/compile requests remain UNCONFIRMED, no native SUCCESS claim; source preserved and direct retry cell1045 pending. Fresh many-factor graph campaign and curve ordinary two-sign source repair running. Future all-k quotient arguments/primary source evidence are FALLIBLE, not new theorem grants. All42originalsremainopen, onlyP05/P06active, goalactive. Full external source PDFs/OCR not redistributed.\n');add(p,'CHECKPOINT.txt')
m={'generated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'repository':'MingchenXia/nonarchimedean-pluripotential-theory','branch':'codex/xean-research-20261003','expected_previous_checkpoint':parent,'files':files,'scope':'Reviewed exact TWO-graph classification; nativeverificationpending, cleanlocalexports. Fresh many-factor graph and curve research running; all42originalsopen.'};p=c/'upload-manifest-continuation30.json';assert not p.exists();p.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'files':len(files),'manifest':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}))
