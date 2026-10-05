"""Keep failed oversized packets immutable; select the relevant full draft per task."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, shutil

R=Path('/workspace/research')
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
now=datetime.now(timezone.utc).isoformat()
jobs=[]
for oldno,no,atom,oldstem,stem,removed in [
    (110,112,'P16.5','P16.5-original-direct-foundation-repair-research',
     'P16.5-original-direct-foundation-length-repair-research',
     {'Actual109 incomplete entire P16.2 paper','Actual109 candidate=false canonical notes','Actual109 premise ledger'}),
    (111,113,'P16.2','P16.2-original-local-operator-and-source-repair-research',
     'P16.2-original-local-operator-length-repair-research',
     {'Unaccepted105 entire P16.5 draft','Unaccepted105 external-premise register','Actual109 candidate=false canonical notes'})]:
    O=R/f'campaigns/round-{oldno}'/oldstem
    C=R/f'campaigns/round-{no}'/stem
    run=json.loads((O/'run.json').read_text())['campaign']
    assert run['status']=='blocked' and run['result'] is None
    assert 'Input exceeds the maximum length of 1048576 characters' in run['error']
    frozen=json.loads((O/'freeze.json').read_text())
    for name,key in [('input.json','input_sha256'),('settings.json','settings_sha256'),
                     ('task-original.json','task_sha256'),('assignment-original.txt','assignment_sha256')]:
        assert sha(O/name)==frozen[key]
    value=json.loads((O/'input.json').read_text())
    assert value['notes']==[]
    seen=[]
    def select(match):
        label=match.group(1)
        if label not in removed:return match.group(0)
        seen.append({'label':label,'characters':len(match.group(2)),
                     'sha256_of_original_UTF8_body':hashlib.sha256(match.group(2).encode()).hexdigest()})
        return ''
    value['assignment']=re.sub(r'BEGIN MATHEMATICAL DATA: ([^\n]+)\n(.*?)\nEND MATHEMATICAL DATA',
                                select,value['assignment'],flags=re.S)
    assert {x['label'] for x in seen}==removed
    value['assignment']='The preceding fresh packet failed at native turn/start before any mathematical result because its input exceeded the character limit. This standalone packet preserves the exact original task, all required primary bodies and repair proposals, and the COMPLETE relevant draft for this problem; unrelated cross-task draft/duplicate note records are omitted. The failed history remains immutable.\n\n'+value['assignment']
    assert len(value['assignment'])+len(json.dumps(value['task'],ensure_ascii=False))+30000<1048576
    assert not C.exists()
    C.mkdir(parents=True);(C/'artifacts').mkdir()
    shutil.copyfile(O/'task-original.json',C/'task-original.json')
    (C/'assignment-original.txt').write_text(value['assignment'])
    (C/'input.json').write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
    settings=json.loads((O/'settings.json').read_text())
    settings['codex']['workspace']=str(C/'artifacts')
    settings['usagePrefix']=f'catalogue-20261003/r{no}/{stem}'
    (C/'settings.json').write_text(json.dumps(settings,ensure_ascii=False,indent=2)+'\n')
    bindings=json.loads((O/'mathematical-data-bindings.json').read_text())
    bindings['sources']=[x for x in bindings['sources'] if x['label'] not in removed]
    bindings['omitted_cross_task_or_duplicate_records']=seen
    (C/'mathematical-data-bindings.json').write_text(json.dumps(bindings,ensure_ascii=False,indent=2)+'\n')
    record={'prepared_utc':now,'round':no,'atom':atom,'directory':str(C),
        'replaces_failed_oversized_packet':str(O),'original_failure':run['error'],
        'task_sha256':sha(C/'task-original.json'),'unchanged_original_task':True,
        'input_sha256':sha(C/'input.json'),'input_bytes':(C/'input.json').stat().st_size,
        'assignment_characters':len(value['assignment']),'assignment_sha256':sha(C/'assignment-original.txt'),
        'settings_sha256':sha(C/'settings.json'),'mathematical_bindings_sha256':sha(C/'mathematical-data-bindings.json'),
        'mandatory_notes_array_present':True,'omitted_records':seen,
        'relevant_full_draft_preserved':True,'all_original_primary_and_repair_units_preserved':True,
        'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh','original_closed':False}
    (C/'freeze.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
    assert (C/'task-original.json').read_bytes()==(O/'task-original.json').read_bytes()
    jobs.append(record)
p=R/'root-checks/native-length-recovery112-113-preparation-20261005.json'
assert not p.exists()
p.write_text(json.dumps({'recorded_utc':now,'jobs':jobs,'no_new_acceptance':True},ensure_ascii=False,indent=2)+'\n')
print(json.dumps([{'round':j['round'],'atom':j['atom'],'directory':j['directory'],
                   'assignment_characters':j['assignment_characters'],'input_bytes':j['input_bytes']} for j in jobs],indent=2))
