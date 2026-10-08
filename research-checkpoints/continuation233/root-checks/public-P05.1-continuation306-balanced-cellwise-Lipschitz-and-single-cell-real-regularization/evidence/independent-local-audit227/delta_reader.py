"""Lossless reader for parallel bodies. References only already displayed tokens.

Whitespace is retained for byte-exact reconstruction; no mathematical token is
normalized, expanded, discarded or silently equated with another token.
"""
import difflib, hashlib, json, pathlib, re, sys
rows=json.loads(pathlib.Path('frozen-bindings-verified.json').read_text())
def body(i):
    r=next(x for x in rows if x['kind']=='math' and x['index']==i)
    b=pathlib.Path(r['path']).read_bytes()
    assert hashlib.sha256(b).hexdigest()==r['sha256']
    return b.decode()
base_i,target_i=map(int,sys.argv[1:3])
base,target=body(base_i),body(target_i)
bt=re.findall(r'\S+',base);tt=re.findall(r'\S+',target)
whitespace=re.split(r'\S+',target)
blocks=[];display=[];covered=0
for tag,bi,bj,ti,tj in difflib.SequenceMatcher(None,bt,tt,autojunk=False).get_opcodes():
    if tag=='equal' and tj-ti>=8:
        blocks.append({'reference_math':base_i,'base_tokens':[bi,bj],'target_tokens':[ti,tj]})
        display.append(f'\n[= {base_i}:{bi}-{bj} -> {target_i}:{ti}-{tj}]\n')
        covered+=tj-ti
    elif tj>ti:
        blocks.append({'literal_tokens':tt[ti:tj],'target_tokens':[ti,tj]})
        display.append(' '.join(tt[ti:tj]))
reconstructed=[]
for b in blocks:
    reconstructed.extend(bt[slice(*b['base_tokens'])] if 'reference_math' in b else b['literal_tokens'])
assert reconstructed==tt
text=whitespace[0]+''.join(t+w for t,w in zip(reconstructed,whitespace[1:]))
assert text==target
report={'base_index':base_i,'target_index':target_i,'whole_tokens':len(tt),'exact_referenced_tokens':covered,'literal_tokens':len(tt)-covered,'byte_exact_reconstruction':True,'blocks':blocks,'whitespace':whitespace}
pathlib.Path(f'delta-math-{target_i:02}.json').write_text(json.dumps(report,ensure_ascii=False,indent=1)+'\n')
pathlib.Path(f'delta-math-{target_i:02}.txt').write_text(' '.join(display)+'\n')
print('target',target_i,'tokens',len(tt),'already-read tokens',covered,'new tokens',len(tt)-covered,'display bytes',pathlib.Path(f'delta-math-{target_i:02}.txt').stat().st_size)
