from pathlib import Path
import hashlib, json, re
R=Path('/workspace/research'); K=R/'root-checks'
C=R/'campaigns/round-271/P12.3-whole382380381-independent-proof-and-original-residual'
A=C/'artifacts/codex-1mbVtK'; O=K/'round271-ROOT-whole-content-identity-audit-20261009.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not O.exists()
assert sha(A/'whole-proof.md')=='ec315b90d92f409ac4ea9d70affc5794f015f9ed1e3bb8af8d266b92b777c46f'
assert sha(A/'P12.3-independent-paper.tex')=='e216e3970d750a05d761b44bfc8af8842f31d134e1624993cd9e629831146f77'
proof=(A/'whole-proof.md').read_text(); tex=(A/'P12.3-independent-paper.tex').read_text()
notes=json.loads((A/'native-notes.json').read_text())['notes']
actual=json.loads((K/'round271-actual-native-final.json').read_text())['notes']
heads=list(re.finditer(r'(?m)^## (\d+)\. .*\n',proof)); assert len(heads)==12
sections={int(m.group(1)):proof[m.start():heads[i+1].start() if i+1<len(heads) else len(proof)].strip() for i,m in enumerate(heads)}
groups=[[1],[2],[3],[4,5,6],[7],[8],[9,10],[11],[12]]; comparisons=[]; footers=[]
for i,(n,nums) in enumerate(zip(notes,groups)):
    body,sep,footer=n['text'].partition('\n\nArtifacts:'); assert sep
    hs=list(re.finditer(r'(?m)^## (\d+)\. .*\n',body)); assert [int(h.group(1)) for h in hs]==nums
    for j,h in enumerate(hs):assert body[h.start():hs[j+1].start() if j+1<len(hs) else len(body)].strip()==sections[nums[j]]
    assert (A/(n['id']+'.md')).read_text()==n['text']+'\n'
    comparisons.append(dict(id=n['id'],expanded_DIFFERS_actual=n['text']!=actual[i]['text'],section_numbers=nums,all_entire_sections_exact_after_only_boundary_whitespace_normalization=True,MD_exact_expanded_plus_final_LF=True))
    footers.append(dict(id=n['id'],entire_footer='Artifacts:'+footer))
escape={'\\':r'\textbackslash{}','{':r'\{','}':r'\}','$':r'\$','&':r'\&','#':r'\#','%':r'\%','_':r'\_','~':r'\textasciitilde{}','^':r'\textasciicircum{}'}
def enc(s):return ''.join(escape.get(c,c) for c in s)
def literal_math_and_escaped_prose(s):
    bits=re.split(r'(\\\(.*?\\\)|\\\[.*?\\\])',s,flags=re.S)
    return ''.join(b if i%2 else enc(b) for i,b in enumerate(bits))
blocks=[]
for p in proof.split('\n\n'):
    if p.startswith('# '):continue
    if p.startswith('## '):
        h,sep,b=p.partition('\n'); blocks.append('\\section{'+enc(h[3:])+'}')
        if b:blocks.append(literal_math_and_escaped_prose(b))
    else:blocks.append(literal_math_and_escaped_prose(p))
body='\n\n'.join(blocks); assert tex.count(body)==1
preamble,tail=tex.split(body,1); assert tail.startswith('\n\n\\appendix\n\n')
extra=[]
for name in ['source-ledger.md','coverage.md','scope-and-verdict.json']:
    extra.extend(['\\section{'+enc(name)+'}','\\begin{ImportedQualifiedGrant}',(A/name).read_text(),'\\end{ImportedQualifiedGrant}'])
grants={n['id']:n['text'] for n in json.loads((C/'input.json').read_text())['notes']}
assert set(grants)=={'G331','B341','E350'}
for label in ['G331','B341','E350']:
    extra.extend(['\\section{Entire qualified '+label+'}','\\begin{ImportedQualifiedGrant}',grants[label],'\\end{ImportedQualifiedGrant}'])
expected_tail='\n\n'.join(['','\\appendix']+extra+['\\end{document}'])+'\n'
assert tail==expected_tail
record=dict(paper_sha256=sha(A/'P12.3-independent-paper.tex'),proof_sha256=sha(A/'whole-proof.md'),entire_actual_notes_separately_read=True,expanded_note_comparisons=comparisons,complete_encoded_proof_body_exact_in_TeX=True,complete_appendix_ledger_coverage_scope_and_literal_qualified_grants_exact=True,whole_content_identity_not_new_separate_fresh_physical_reading=True,entire_new_preamble=preamble,native_or_supplied_program_execution=False)
O.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(audit_path=str(O),audit_sha256=sha(O),record=record,all_nine_entire_expanded_footers=footers),ensure_ascii=False,indent=2))
