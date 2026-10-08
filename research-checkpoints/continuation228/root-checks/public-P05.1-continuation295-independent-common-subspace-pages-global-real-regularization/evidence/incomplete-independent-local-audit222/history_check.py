#!/usr/bin/env python3
"""Own structural evidence checks; no supplied script is executed."""
import json,pathlib,re,hashlib,difflib
HERE=pathlib.Path(__file__).resolve().parent
B=json.loads((HERE/'frozen-bindings.json').read_text())
def raw(i): return pathlib.Path(B['history'][i]['path']).read_bytes()
def obj(i): return json.loads(raw(i))
def main():
    actual=obj(65); saved=obj(39); registered=obj(66)
    result={'saved_equal_actual_after_parsing':saved==actual,'saved_equal_bytes':raw(39)==raw(65),'actual_notes':len(actual['notes']),'actual_candidate':actual['candidate'],'registered_keys':list(registered)}
    suffixes=[]
    for a,r in zip(actual['notes'],registered['notes']):
        equal={k:a[k]==r[k] for k in a if k!='text'}
        starts=r['text'].startswith(a['text']); suffix=r['text'][len(a['text']):] if starts else None
        suffixes.append({'id':a['id'],'other_fields_equal':equal,'starts_with_actual_text':starts,'suffix':suffix})
    result['registered_note_suffixes']=suffixes
    result['registered_notes_count']=len(registered['notes'])
    result['registered_candidate_equal']=registered.get('candidate')==actual['candidate']
    result['initial_source_diff_to_final']=list(difflib.unified_diff(raw(34).decode().splitlines(),raw(1).decode().splitlines(),fromfile='disclosed-reconstruction',tofile='final',lineterm=''))
    result['historical_logs']=[]
    for i in [4,43,45,46,48,49,51,52,54,55,57,58,60,75,77,80,82,88,93]:
        lines=raw(i).decode(errors='replace').splitlines()
        hits=[{'line':j+1,'text':v} for j,v in enumerate(lines) if re.search(r'Undefined control|Warning|Overfull|Underfull|Output written|shell escape|write18|Emergency stop|Fatal error',v)]
        result['historical_logs'].append({'index':i,'file':B['history'][i]['path'],'hits':hits})
    result['settings']=obj(96)
    result['frozen_input_hash_checks']={}
    freeze=obj(97)
    for i,k in [(94,'task_sha256'),(95,'input_sha256'),(96,'settings_sha256')]:
        result['frozen_input_hash_checks'][k]=hashlib.sha256(raw(i)).hexdigest()==freeze[k]
    result['history_own_build_records']=[obj(i) for i in [30,35,37,89]]
    result['own_build_log_hits']=[]
    for i in [1,2,3]:
        p=HERE/'own-scratch'/f'run-{i}.tex.log'
        result['own_build_log_hits'].append({'pass':i,'hits':[v for v in p.read_text().splitlines() if re.search(r'Warning|Overfull|Underfull|Output written|shell escape',v)]})
    (HERE/'history-audit-records.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['historical_logs','history_own_build_records']},indent=2))
if __name__=='__main__': main()
