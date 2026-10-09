from pathlib import Path
import difflib,json
R=Path('/workspace/research');K=R/'root-checks'
A=R/'campaigns/round-283/P12.3-whole405-contact-and-arbitrary-envelope-residual/artifacts/codex-SZjDaw'
actual=json.loads((K/'round283-raw-native-actual-FINAL.json').read_text())
expanded=json.loads((A/'notes.json').read_text())
assert actual['candidate'] is expanded['candidate'] is False
assert len(actual['notes'])==len(expanded['notes'])==4
for a,e in zip(actual['notes'],expanded['notes']):
    assert set(a)==set(e)=={'id','summary','detailedSummary','text','support'}
    assert e['text']==(A/(e['id']+'.md')).read_text()
    equal={k:a[k]==e[k] for k in a}
    assert all(equal[k] for k in ['id','summary','detailedSummary','support'])
    print(json.dumps({'id':a['id'],'fields_equal':equal,'actual_bytes':len(a['text'].encode()),'expanded_bytes':len(e['text'].encode())}))
    if not equal['text']:
        print(''.join(difflib.unified_diff(a['text'].splitlines(True),e['text'].splitlines(True),fromfile='actual-'+a['id'],tofile='expanded-'+e['id'])))
