"""Own read-only verification; only listed immutable paths are opened."""
import hashlib,json,pathlib,sys,difflib
BASE=pathlib.Path('/workspace/research/campaigns/round-215/P05.2-unchanged-all-continuous-affine-arrangement-independent-native-local-source-audit')
OWN=pathlib.Path(__file__).resolve().parent
def digest(data): return hashlib.sha256(data).hexdigest()
def write(name,value): (OWN/name).write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n')
rows=[]; packets={}
for key,name in [('math','mathematical-packet-bindings.json'),('history','historical-own-evidence-bindings.json'),('primary','private-primary-packet-bindings.json')]:
    raw=(BASE/name).read_bytes(); packets[key]=json.loads(raw)
    rows.append({'packet':'binder','path':str(BASE/name),'bytes':len(raw),'sha256':digest(raw)})
    for i,e in enumerate(packets[key]):
        raw=pathlib.Path(e['path']).read_bytes()
        r={'packet':key,'index':i,'path':e['path'],'bytes':len(raw),'sha256':digest(raw),'LF_count':raw.count(b'\n'),'binding_matches':len(raw)==e['bytes'] and digest(raw)==e['sha256']}
        rows.append(r)
        assert r['binding_matches'],r
raw=(BASE/'original-task.json').read_bytes()
rows.append({'packet':'original','path':str(BASE/'original-task.json'),'bytes':len(raw),'sha256':digest(raw)})
write('frozen-file-bindings.json',rows)
hist=packets['history']; math=packets['math']
def h(i): return json.loads(pathlib.Path(hist[i]['path']).read_text())
exact=json.loads(pathlib.Path(math[26]['path']).read_text()); saved=h(19); registered=h(29)
diff=[]
for a,b in zip(exact['notes'],saved['notes']):
    fields=[k for k in a if a[k]!=b.get(k)]
    diff.append({'id':a['id'],'different_fields':fields,'support_equal':a['support']==b['support']})
    (OWN/('note-'+a['id']+'-saved-versus-final.diff')).write_text(''.join(difflib.unified_diff(b['text'].splitlines(keepends=True),a['text'].splitlines(keepends=True),fromfile='historical saved text',tofile='controlling exact FINAL text')))
    assert fields==['summary','detailedSummary','text']
suffix=[]
for a,b in zip(exact['notes'],registered['notes']):
    assert all(a[k]==b[k] for k in a if k!='text')
    assert b['text'].startswith(a['text'])
    suffix.append({'id':a['id'],'appended':b['text'][len(a['text']):]})
assert exact['candidate']==registered['candidate']==saved['candidate']==False
parent=h(43); child=h(17)['task']; prior=h(44); norm=h(45)
assert parent==child
replaced=prior['problem']
for p in norm['positions']:
    k=p['character_offset']; assert ord(prior['problem'][k])==int(p['codepoint'][2:],16)
    replaced=replaced[:k]+chr(int(p['visible_codepoint'][2:],16))+replaced[k+1:]
assert replaced==parent['problem'][:len(replaced)]
assert prior['completionCriteria']==parent['completionCriteria']
write('historical-comparison.json',{'saved_note_differences':diff,'registered_suffixes':suffix,'parent_child_task_semantically_equal':parent==child,'parent_child_file_bytes_equal':pathlib.Path(hist[43]['path']).read_bytes()==pathlib.Path(hist[17]['path']).read_bytes(),'normalization_positions_checked':len(norm['positions']),'normalized_prefix_exact':True,'remaining_normalized_suffix':parent['problem'][len(replaced):],'source_to_markdown_reverse_equivalence_claimed':False})
author_by_name={pathlib.Path(e['path']).name:e for e in hist[:26]}
manifest=h(26)
for e in manifest:
    own=author_by_name[e['file']]; raw=pathlib.Path(own['path']).read_bytes()
    assert len(raw)==e['bytes'] and digest(raw)==e['sha256']
write('verification-output.json',{'bound_files':sum(r['packet'] in packets for r in rows),'all_bound_hashes_sizes_match':True,'author_manifest_entries_verified':len(manifest),'candidate':False})
(OWN/'LOCALONLY').mkdir(exist_ok=True)
units={'BMPS':[(254,301),(418,638),(691,852),(1000,1030),(1354,1503),(1741,1746),(2259,2353)],'BBGS':[(196,250),(379,598),(599,714),(1515,1555),(1913,1992)]}
for label,index in [('BMPS',1),('BBGS',3)]:
    e=packets['primary'][index]; lines=pathlib.Path(e['path']).read_text().split('\n')
    (OWN/'LOCALONLY'/(label+'-whole-units.txt')).write_text('\n\n'.join(f'LF {a}-{b}\n'+'\n'.join(lines[a-1:b]) for a,b in units[label])+'\n')
# Only immutable manuscript data are copied. No supplied program is executed.
(OWN/'build').mkdir(exist_ok=True)
(OWN/'build'/'P05.2-paper.tex').write_bytes(pathlib.Path(math[22]['path']).read_bytes())
(OWN/'certificate-input.json').write_bytes(pathlib.Path(hist[12]['path']).read_bytes())
print(json.dumps({'bindings':'PASS','saved_notes_differ':4,'normalization':'PASS','author_manifest':'PASS'}))
