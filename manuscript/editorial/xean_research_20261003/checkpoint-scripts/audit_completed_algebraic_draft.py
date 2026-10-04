"""Record direct core reads and exact reuse of previously fully read primary units."""
from pathlib import Path
import datetime,hashlib,json,re

root=Path('/workspace/research')
review=root/'campaigns/round-21/P06.2-all-dimensional-completed-algebraic-review'
workspace=root/'campaigns/round-21/P06.2-all-dimensional-completed-algebraic-continuation/artifacts/codex-ZwIWCf'
prior_review=root/'campaigns/round-19/P06.2-general-finite-galois-review'
prior=json.loads((prior_review/'root-draft-read-record.json').read_text())
prior_workspace=Path(prior['source_workspace'])
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert prior['full_main_argument_read'] and prior['all_canonical_notes_fully_read']
assert sha(prior_workspace/'P06.2-argument.md')==prior['main_argument_sha256']
text=(workspace/'P06.2-argument.md').read_text()
origins=[]
for source in json.loads((workspace/'sources/manifest.json').read_text()):
    path=workspace/source['artifact']
    origin=Path(source['read_only_origin'])
    assert sha(path)==sha(origin)==source['sha256']
    origins.append({'snapshot':str(path),'origin':str(origin),'sha256':sha(path)})
units=[]
for unit in json.loads((workspace/'sources/primary-units.json').read_text()):
    path=workspace/'sources'/(unit['id']+'.txt')
    old=prior_workspace/'sources'/path.name
    body=path.read_text()
    assert sha(path)==unit['sha256'] and path.read_bytes()==old.read_bytes()
    source=(workspace/'sources'/unit['source']).read_text()
    assert source.count(body)==1
    start=source.index(body);end=start+len(body)
    assert source[:start].count('\n')+1==unit['first_line']
    assert source[:end].count('\n')==unit['last_line']
    assert re.match(unit['end_boundary_pattern'],source[end:],re.M)
    matches=list(re.finditer(r'^### '+re.escape(unit['id'])+r':[^\n]*\n.*?```text\n(.*?)\n```',text,re.M|re.S))
    assert len(matches)==1 and matches[0].group(1)==body.replace('\f','\n').rstrip()
    units.append({'id':unit['id'],'sha256':sha(path),'prior_fully_read_body':str(old),
                  'unchanged_exact_body_reuse':True,'authentic_origin_and_full_heading_boundary_bound':True,
                  'current_embedding_exact':True})
assert len(units)==33
core=(workspace/'proof-core.md').read_text()
marker='<!-- PRIMARY_APPENDIX_INSERTION_POINT -->'
assert core.count(marker)==1
assert core.partition(marker)[0].rstrip()==text[:text.index('## Embedded primary-source bodies')].rstrip()
run=workspace.parents[1]/'run.json'
notes=json.loads(run.read_text())['campaign']['result']['notes']
assert [n['id'] for n in notes]==['n1','n2']
freeze=json.loads((review/'freeze.json').read_text())
binding=json.loads((review/'source-artifact-binding.json').read_text())
assert sha(workspace/'P06.2-argument.md')==freeze['main_argument_sha256']==binding['main_argument_sha256']
assert sha(workspace/'P06.2-partial.tex')==freeze['source_tex_sha256']==binding['source_tex_sha256']
assert sha(workspace/'status.json')==freeze['source_status_sha256']==binding['source_status_sha256']
assert sha(review/'argument.md')==freeze['argument_sha256']==binding['review_argument_sha256']
record={'read_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'source_workspace':str(workspace),'main_argument_sha256':sha(workspace/'P06.2-argument.md'),
    'full_main_argument_read':True,'full_main_fresh_read':False,
    'full_main_accounted_for_by_direct_core_and_exact_primary_reuse':True,
    'direct_line_ranges':[[1,298],[299,602],[603,909],[910,993]],
    'all_canonical_notes_fully_read':True,'canonical_note_ids':[n['id'] for n in notes],
    'canonical_note_hashes':{n['id']:hashlib.sha256(n['text'].encode()).hexdigest() for n in notes},
    'canonical_run_sha256':sha(run),'n1_output_truncation_tail_reread':True,
    'author_audit_fully_read':True,'research_evidence_fully_read':True,'source_evidence_fully_read':True,
    'source_embedding_program_fully_read':True,'build_evidence_fully_read':True,
    'source_origins':origins,'primary_units':units,
    'primary_reuse_origin':{'root_read_record':str(prior_review/'root-draft-read-record.json'),
       'sha256':sha(prior_review/'root-draft-read-record.json'),'full33prior_bodies_read':True},
    'scope':'Unaccepted completed-algebraic ALL-dimensional ordinary-current transport and all-bidegree compact-test descent draft; original recognition open.',
    'independent_review_state':'running; not yet accepted','publish_exact_scope':False,'original_atom_solved':False}
path=review/'root-draft-read-record.json'
assert not path.exists()
path.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'direct_core_lines':993,'exact_prior_fully_read_primary_bodies':len(units),
    'all_canonical_notes_read':True,'record_sha256':sha(path)}))
