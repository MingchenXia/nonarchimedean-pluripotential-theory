from pathlib import Path
import hashlib, json, sys
A=Path('/workspace/research/campaigns/round-271/P12.3-whole382380381-independent-proof-and-original-residual/artifacts/codex-1mbVtK')
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert len(sys.argv)>=2
if sys.argv[1]=='info':
    files=[dict(name=p.name,bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(A.iterdir()) if p.is_file()]
    raw=json.loads((A/'native-notes.json').read_text()); notes=raw if isinstance(raw,list) else raw['notes']
    proof=(A/'whole-proof.md').read_text(); actual=json.loads(Path('/workspace/research/root-checks/round271-actual-native-final.json').read_text())['notes']
    print(json.dumps(dict(files=files,notes_container_type=type(raw).__name__,notes_container_outside_fields={} if isinstance(raw,list) else {k:v for k,v in raw.items() if k!='notes'},entire_expanded_outside_fields=[{k:v for k,v in n.items() if k!='text'} for n in notes],proof_chars=len(proof),body_comparisons=[dict(id=n['id'],expanded_text_bytes=len(n['text'].encode()),expanded_entire_proof_substring=proof.find(n['text']),expanded_DIFFERS_actual=n['text']!=actual[i]['text']) for i,n in enumerate(notes)]),ensure_ascii=False,indent=2))
elif sys.argv[1]=='proof':
    assert len(sys.argv)==4
    text=(A/'whole-proof.md').read_text(); a,b=map(int,sys.argv[2:]); assert 0<=a<b<=len(text) and b-a<=19500
    print(text[a:b],end='')
else:raise ValueError('Only complete metadata or bounded exact proof slices allowed; native programs remain DATA')
