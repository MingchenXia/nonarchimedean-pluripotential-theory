"""Preserve both completed partial authors after reading their complete arguments."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil

R=Path('/workspace/research')
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
write=lambda p,d:Path(p).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
specs=[
    (70,'P16.1','P16.1-public-source-smooth-weak-globalization-open-trace-and-unibranch-equation',
     '712c815af27d755e658d130b3482c64b146e5a3673a2bd48e9fb1006c1e7652b',
     '4068d66e3e3f81b96ddfdabe5027ca291f9225de51529831644476b6b6b8251b',156,64,23,14),
    (71,'P13.2','P13.2-public-source-accepted-Reeb-comparison-and-genuine-realization',
     'a3df6a4798bc38ff37454d5b53a4f845e79471c8ce74ef20fb7e7a5b82641d07',
     'fd5a5eea361ee3dea428c8bfdcd7b80540dca6105edb7ebadc94c5fcd5e048e6',54,19,30,10),
]
results=[]
for no,atom,stem,result_sha,proof_sha,file_count,excerpt_count,primary_count,pages in specs:
    C=R/'campaigns'/('round-'+str(no))/stem
    N=R/'root-checks'/(atom+'-round'+str(no)+'-actual-result-20261005.json')
    assert sha(N)==result_sha
    actual=json.loads(N.read_text());W=Path(actual['workspace'])
    D=R/'root-checks'/('public-'+atom+'-round-'+str(no)+'-final-reader')
    assert not D.exists() and actual['candidate'] is False and len(actual['notes'])==4
    assert W.is_relative_to(C/'artifacts')
    assert sha(W/(atom+'-argument.md'))==proof_sha
    original=json.loads((C/'input.json').read_text())
    native=json.loads((W/'input.json').read_text())
    assert original==native
    assert (W/'input.json').read_bytes()==(W/'input-original.json').read_bytes()
    assert (W/'assignment-original.txt').read_text()==native['assignment']
    assert json.loads((W/'task-original.json').read_text())==native['task']
    status=json.loads((W/'status.json').read_text())
    assert set(status)=={'id','status','exact_result','proof_file','concrete_gaps'}
    assert status['status']=='partial'
    provenance=json.loads((W/'source-extracts/source-provenance.json').read_text())
    primary=[];excerpts=[];accepted=[]
    if no==70:
        assert len(provenance['sources'])==10
        for f in provenance['verified_files']:
            assert sha(f['authorized_path'])==sha(W/f['local_file'])==f['sha256']
            primary.append({'path':f['authorized_path'],'sha256':f['sha256'],'local_copy':f['local_file']})
        for e in provenance['excerpts']:
            source=Path(e['source_path']);assert sha(source)==e['source_sha256']
            first,last=e['inclusive_one_based_LF']
            literal='\n'.join(source.read_bytes().decode('utf-8').split('\n')[first-1:last])
            assert literal==e['literal']==(W/e['literal_file']).read_bytes().decode('utf-8')
            assert sha(W/e['literal_file'])==e['literal_sha256']
            excerpts.append({'id':e['id'],'source':str(source),'range':[first,last],'sha256':e['literal_sha256']})
        build=json.loads((W/'build-results.json').read_text())
        assert build['success'] and build['pdf_pages']==pages
    else:
        assert len(provenance['sources'])==11
        for s in provenance['sources']:
            source=Path(s['descriptor']['literal_extract'])
            assert source.read_bytes()==(W/s['complete_literal_copy']).read_bytes()
            assert len(source.read_bytes().decode('utf-8').split('\n'))==s['LF_entries']
            for f in s['verified_files']:
                assert sha(f['path'])==f['sha256'] and f['matches_expected']
                primary.append({'path':f['path'],'sha256':f['sha256']})
            for e in s['excerpts']:
                first,last=e['start_LF'],e['end_LF']
                literal='\n'.join(source.read_bytes().decode('utf-8').split('\n')[first-1:last])
                assert literal==e['literal']
                excerpts.append({'id':s['id'],'source':str(source),'range':[first,last],
                    'sha256':hashlib.sha256(literal.encode('utf-8')).hexdigest()})
        for b in provenance['accepted_bindings']:
            assert sha(b['path'])==b['sha256']==b['actual_sha256']
            if 'mathematical_body' in b:
                e=b['mathematical_body'];first,last=e['start_LF'],e['end_LF']
                literal='\n'.join(Path(b['path']).read_bytes().decode('utf-8').split('\n')[first-1:last])
                assert literal==e['literal']
            accepted.append({'kind':b['kind'],'path':b['path'],'sha256':b['sha256']})
        assert len(accepted)==3
        assert json.loads((W/'build-report.json').read_text())['two_TeX_passes_succeeded']
        assert json.loads((W/'validation-report.json').read_text())['primary_files_verified']==primary_count
    assert len(primary)==primary_count and len(excerpts)==excerpt_count
    files=[p for p in sorted(W.rglob('*')) if p.is_file()]
    assert len(files)==file_count
    forbidden={'.git','.codex','.aws','.env','auth.json','campaign.sqlite','run.json'}
    for p in files:
        assert not p.is_symlink() and not any(part in forbidden for part in p.relative_to(W).parts)
        assert p.suffix not in {'.sqlite','.jsonl'}
    D.mkdir();preserved=[]
    for p in files:
        target=D/p.relative_to(W);target.parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(p,target);assert sha(p)==sha(target)
        preserved.append({'file':str(p.relative_to(W)),'bytes':p.stat().st_size,'sha256':sha(p)})
    shutil.copyfile(N,D/'canonical-native-result.json')
    record={'recorded_utc':datetime.now(timezone.utc).isoformat(),'atom':atom,'round':no,
        'campaign':str(C),'native_workspace':str(W),'reader':str(D),
        'actual_result_sha256':result_sha,'candidate':False,'original_closed':False,
        'entire_actual_four_canonical_notes_root_read':True,'whole_argument_root_read':True,
        'argument_sha256':proof_sha,'whole_tex_root_read':False,
        'all_source_application_limits_and_excerpt_index_root_read':True,
        'all_literal_excerpt_bodies_root_read':False,'whole_primary_bodies_root_read':False,
        'primary_file_bindings':primary,'literal_excerpt_bindings':excerpts,
        'accepted_bindings':accepted,'native_input_semantically_equals_frozen_campaign':True,
        'native_input_preserved_byte_identically':True,'preserved_author_files':preserved,
        'author_two_pass_compilation':'SUCCESS','author_pdf_pages':pages,
        'native_editor_source_preserved':'/workspace/research/root-checks/public-P16-round-46-final-reader/P16.4-paper.tex',
        'new_generated_mathematics_independently_reviewed':False,
        'complete_original_candidate_ready_for_review':False,
        'limits':'Hashes and compilation reproduce artifacts only. Neither partial author is a complete original solution or newly accepted scoped paper.'}
    write(D/'root-preservation-and-read-state-continuation79.json',record)
    results.append({'atom':atom,'reader':str(D),'preserved_files':file_count,
        'literal_bindings':excerpt_count,'primary_bindings':primary_count,
        'whole_argument_root_read':True,'candidate':False,
        'root_record_sha256':sha(D/'root-preservation-and-read-state-continuation79.json')})
print(json.dumps(results,ensure_ascii=False,indent=2))
