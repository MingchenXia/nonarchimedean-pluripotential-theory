from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
R=Path('/workspace/research'); K=R/'root-checks'
A=R/'campaigns/round-272/P16.7-whole383-intrinsic-E1-and-actual-branch-Dirac/artifacts/codex-hhK319'
O=K/'round272-ROOT-whole-content-identity-audit-20261009.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not O.exists()
assert sha(A/'proof-companion.md')=='af5de296d5b29031b29c4a18cfee282f751d81f00337fde45dcb8682eb2eaa36'
assert sha(A/'P16.7-independent-paper.tex')=='8714e7f62596a840da1f56eccd0c7f0445c3ac24554653f9c9859bfd7bf4012c'
actual=json.loads((K/'round272-actual-native-final.json').read_text())
expanded=json.loads((A/'expanded-notes.json').read_text())
assert actual['candidate'] is expanded['candidate'] is False
assert actual==json.loads((A/'final-notes.json').read_text())==json.loads((A/'actual-final-notes.json').read_text())
notes=expanded['notes']; assert len(notes)==5
ledger=(A/'source-application-ledger.md').read_text()
body='\n\n'.join(n['text'].rstrip() for n in notes)+'\n\n'+ledger
assert (A/'P16.7-independent-paper.md').read_text()==body
assert (A/'proof-companion.md').read_text()=='# Complete independent scoped proof companion\n\n'+body
mapping={'\\':r'\textbackslash{}','{':r'\{','}':r'\}','_':r'\_','^':r'\textasciicircum{}','~':r'\textasciitilde{}','&':r'\&','%':r'\%','$':r'\$','#':r'\#'}
def enc(s):return ''.join(mapping.get(c,c) for c in s)
encoded=[]
for line in body.split('\n'):
    if line.startswith('## '):encoded.append(r'\subsection*{'+enc(line[3:])+'}')
    elif line.startswith('# '):encoded.append(r'\section*{'+enc(line[2:])+'}')
    else:encoded.append(enc(line))
tex=(A/'P16.7-independent-paper.tex').read_text(); exact='\n'.join(encoded)+'\n'+r'\end{document}'+'\n'
assert tex.endswith(exact); preamble=tex[:-len(exact)]
comparisons=[]; outside=[]
for aa,ee in zip(actual['notes'],notes):
    assert aa['id']==ee['id'] and aa['text']!=ee['text']
    assert (A/'notes'/(ee['id']+'.md')).read_text()==ee['text']
    comparisons.append(dict(id=ee['id'],actual_text_sha256=hashlib.sha256(aa['text'].encode()).hexdigest(),expanded_text_sha256=hashlib.sha256(ee['text'].encode()).hexdigest(),DIFFERENT=True,whole_expanded_body_exact_within_companion_after_only_rstrip_boundary_whitespace=True))
    outside.append({k:v for k,v in ee.items() if k!='text'})
record=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),round=272,paper_sha256=sha(A/'P16.7-independent-paper.tex'),proof_sha256=sha(A/'proof-companion.md'),all_five_distinct_actual_fields_ROOT_physically_read_untruncated=True,entire63788character_companion_ROOT_physically_read_untruncated=True,character_intervals=[[0,18000],[17700,36500],[36200,55000],[54700,63788]],complete_expanded_proof_and_entire_source_ledger_exact_in_companion_and_TeX=True,entire_body_identity_is_not_separate_fresh_duplicate_physical_reading=True,entire_unique_preamble=preamble,comparisons=comparisons,native_audit_and_build_read_AS_DATA_only=True,supplied_or_native_programs_executed_or_imported=False,new_accepted=False,whole_original_solved=False)
O.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(audit=str(O),audit_sha256=sha(O),record=record,ALL_five_entire_expanded_outside_fields=outside),ensure_ascii=False,indent=2))
