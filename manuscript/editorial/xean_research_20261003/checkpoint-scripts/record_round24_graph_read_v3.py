"""Record completed reading and exact immutable bindings; no worker mutation."""
from pathlib import Path
import datetime, difflib, hashlib, json, re, unicodedata
r=Path('/workspace/research')
w=r/'campaigns/round-24/P05.2-finitely-many-graph-products/artifacts/codex-BufmAZ'
d=r/'campaigns/round-24/P05.2-finitely-many-graph-products-review'
out=r/'root-checks/many-graph-product-draft-phase3-v3'
out.mkdir(exist_ok=False)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
main=w/'P05.2-argument.md';lines=main.read_text().split('\n')
parent=r/'campaigns/round-22/P05.2-arbitrary-graph-product-continuation/artifacts/codex-ODSVkE/P05.2-argument.md'
old=parent.read_text().split('\n');covered=set();blocks=[]
for m in difflib.SequenceMatcher(a=lines[1286:2410],b=old[1542:2230],autojunk=False).get_matching_blocks():
    if m.size>=3:
        lo=m.a+1287;hi=lo+m.size-1
        assert lines[lo-1:hi]==old[m.b+1542:m.b+1542+m.size]
        blocks.append({'current_LF':[lo,hi],'previous_fully_read_LF':[m.b+1543,m.b+1542+m.size]})
        covered.update(range(lo,hi+1))
unmatched=[i for i in range(1287,2411) if i not in covered]
assert len(unmatched)==484 and len(lines)==2478
sources=json.loads((w/'source-hashes.json').read_text())
for s in sources:
    p=w/s['file'];assert sha(p)==s['sha256'] and p.read_bytes()==Path(s['origin']).read_bytes()
excerpts=json.loads((w/'source-excerpts.json').read_text())
for e in excerpts:
    raw='\n'.join((w/'sources'/e['source']).read_text().split('\n')[e['LF_first']-1:e['LF_last']])+'\n'
    assert (w/e['file']).read_text()==raw and sha(w/e['file'])==e['sha256']
    display=raw.replace('\f','\n').replace('\u0010','(').replace('\u0011',')').replace('ℓ','ell').replace('⪯','preceq')
    for ch in '\uf8eb\uf8ec\uf8ed':display=display.replace(ch,'(')
    for ch in '\uf8f6\uf8f7\uf8f8':display=display.replace(ch,')')
    display=''.join(c for c in display if c in '\n\t' or unicodedata.category(c)!='Cc')
    display=re.sub(r'\\mathbb ([A-Z])',r'\\mathbb{\1}',display)
    display=re.sub(r'([_^])\\mathbb\{([A-Z])\}',r'\1{\\mathbb{\2}}',display)
    assert display in main.read_text()
result=json.loads((r/'campaigns/round-24/P05.2-finitely-many-graph-products/run.json').read_text())['campaign']['result']
assert [n['id'] for n in result['notes']]==['n1','n2','n3'] and result['candidate'] is False
canonical_record=r/'root-checks/many-graph-product-draft-phase1/canonical-result-record.json'
canonical_saved=json.loads(canonical_record.read_text())
assert canonical_saved['result']==result
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
record={'checked_utc':now,'source_workspace':str(w),'main_argument_sha256':sha(main),
 'complete_argument_coverage':True,'fresh_direct_main_LF_ranges':[[1,1286],[2411,2478]],
 'source_and_comparison_interval':[1287,2410],'exact_previous_read_reuse_blocks':blocks,
 'reused_parent':str(parent),'reused_parent_sha256':sha(parent),
 'previous_fully_read_parent_interval':[1543,2230],
 'all_other_lines_directly_read':unmatched,'unmatched_count':len(unmatched),
 'all_three_canonical_notes_fully_read':True,'canonical_notes_match_saved_native_result':True,'canonical_source':str(canonical_record),'author_local_notes_are_distinct':True,
 'all_19_source_snapshots_rebound_to_unchanged_origins':True,'all_12_selected_raw_and_display_bodies_exact':True,
 'source_and_build_scripts_fully_read':['snapshot_sources.py','compose_argument.py','diagnostics.py','build.py','make_notes.py','final_checks.py'],
 'audits_fully_read':['author-self-audit.md','research-notes.md','source-authentication.json','source-excerpts.json','source-hashes.json','build-evidence.json','checks.json','commands.txt','status.json'],
 'fresh_diagnostic_rerun_record':str(r/'root-checks/many-graph-product-draft-phase2/root-rerun-and-read-in-progress.json'),
 'historical_phase1_phase2_records_preserved':True,
 'finite_diagnostic_limit':'Four local product germs in dimensions3/5; not a whole-space envelope or integral enumeration.',
 'mathematical_scope':'Any finite graph product in declared real coefficient category only; original arbitrary balanced carriers open.',
 'full_original_atom_solved':False}
(out/'root-complete-read-record.json').write_text(json.dumps(record,indent=2)+'\n')
assert not (d/'root-draft-read-record.json').exists()
(d/'root-draft-read-record.json').write_text(json.dumps(record,indent=2)+'\n')
f=json.loads((d/'freeze.json').read_text());b=json.loads((d/'source-artifact-binding.json').read_text())
j=json.loads((d/'run.json').read_text());review=j['campaign']['result']
assert j['campaign']['status']=='completed' and review['verdict']=='PASS'
assert review['premises']==[] and review['passages']==[]
assert sha(d/'argument.md')==f['argument_sha256']==b['review_argument_sha256']
assert sha(d/'freeze.json')==b['original_freeze_sha256']
for key,hkey in [('main_argument','main_argument_sha256'),('source_tex','source_tex_sha256'),('declared_proof_file','declared_proof_sha256')]:
    assert sha(Path(b[key]))==b[hkey]==f[hkey]
assert sha(w/'status.json')==f['source_status_sha256']==b['source_status_sha256']
att={'read_utc':now,'verdict':'PASS','premise_count':0,'passage_count':0,
 'full_report_read':True,'all_premises_read':True,'all_passages_read':True,
 'passage_premise_zero_based_exact_statement_checks':True,
 'root_full_main_and_all_canonical_notes_read':True,'publish_exact_scope':True,
 'full_original_atom_solved':False,'run_sha256':sha(d/'run.json'),
 'argument_sha256':sha(d/'argument.md'),'freeze_sha256':sha(d/'freeze.json'),
 'source_artifact_binding_sha256':sha(d/'source-artifact-binding.json'),
 'root_read_record_sha256':sha(d/'root-draft-read-record.json'),
 'governing_report':review['report'],
 'editorial_corrections_only':'Explicit cylinder aliases (1)/(2)/(3)/(5); bad-pair (35) to (J), epsilon to kappa.',
 'limit':'Same-model independent review is not formal verification or priority certification.'}
assert not (d/'review-read-attestation.json').exists()
(d/'review-read-attestation.json').write_text(json.dumps(att,ensure_ascii=False,indent=2)+'\n')
(out/'canonical-review-result.json').write_text(json.dumps({'source_run_sha256':sha(d/'run.json'),'result':review},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'root_record_sha256':sha(d/'root-draft-read-record.json'),'review_read_attestation_sha256':sha(d/'review-read-attestation.json'),'verdict':'PASS','full_original_atom_solved':False},indent=2))
