from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
R=Path('/workspace/research'); K=R/'root-checks'
A=R/'campaigns/round-273/P16.7-whole385387-full-bounded-dual-and-intrinsic-E1/artifacts/codex-Bxz0sA'
O=K/'round273-ROOT-whole-content-identity-audit-20261009.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not O.exists()
assert sha(A/'proof-companion.md')=='6f66ee21415aa7734f688031dd63c176341d5d1843750499f15529f4a3c7b445'
assert sha(A/'P16.7-bounded-dual-paper.tex')=='dfbb6cd4d486ab5df25aa731d15916433e2fb4f7456f219ce6ea1d0d2d903da2'
actual=json.loads((K/'round273-actual-native-final.json').read_text())
expanded=json.loads((A/'final-notes.json').read_text())
assert actual['candidate'] is expanded['candidate'] is False
assert expanded==json.loads((A/'actual-final-notes.json').read_text())
assert len(actual['notes'])==len(expanded['notes'])==4
ledger=(A/'source-application-ledger.md').read_text()
body='# Full bounded dual on a concrete nonalgebraizable surface\n\nUnverified standalone scoped paper. Original P16.7: incomplete; candidate=false.\n\n'+'\n\n'.join(n['text'].rstrip() for n in expanded['notes'])+'\n\n'+ledger
assert (A/'proof-companion.md').read_text()==body
mapping={'\\':r'\textbackslash{}','{':r'\{','}':r'\}','_':r'\_','^':r'\textasciicircum{}','~':r'\textasciitilde{}','&':r'\&','%':r'\%','$':r'\$','#':r'\#'}
def enc(s):return ''.join(mapping.get(c,c) for c in s)
encoded=[]
for line in body.splitlines():
    if line.startswith('## '):encoded.append(r'\subsection*{'+enc(line[3:])+'}')
    elif line.startswith('# '):encoded.append(r'\section*{'+enc(line[2:])+'}')
    elif line.strip():encoded.append(enc(line))
    else:encoded.append('')
tex=(A/'P16.7-bounded-dual-paper.tex').read_text()
exact='\n'.join(encoded)+'\n\n'+r'\end{document}'+'\n'
assert tex.endswith(exact); preamble=tex[:-len(exact)]
comparisons=[]; outside=[]
for aa,ee in zip(actual['notes'],expanded['notes']):
    assert aa['id']==ee['id'] and (A/(ee['id']+'.md')).read_text()==ee['text']
    comparisons.append(dict(id=ee['id'],actual_text_bytes=len(aa['text'].encode()),expanded_text_bytes=len(ee['text'].encode()),actual_text_sha256=hashlib.sha256(aa['text'].encode()).hexdigest(),expanded_text_sha256=hashlib.sha256(ee['text'].encode()).hexdigest(),DIFFERENT=aa['text']!=ee['text'],whole_expanded_body_exact_in_companion=True))
    outside.append({k:v for k,v in ee.items() if k!='text'})
stale=json.loads((A/'evidence/version-identities.json').read_text())
assert len(stale['versions'])==5
record=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),round=273,paper_sha256=sha(A/'P16.7-bounded-dual-paper.tex'),proof_sha256=sha(A/'proof-companion.md'),actual_FINAL_sha256=sha(K/'round273-actual-native-final.json'),expanded_sha256=sha(A/'final-notes.json'),actual_native_artifact_named_actual_final_NOT_actual_settled=True,all_four_actual_fields_ROOT_physically_read_untruncated=True,entire64776character_companion_ROOT_physically_read_untruncated=True,character_intervals=[[0,18000],[17700,36500],[36200,55000],[54700,64776]],complete_four_proofs_and_entire16600byte_ledger_exact_in_companion_and_TeX=True,duplicate_identity_not_new_physical_reading=True,entire_unique_preamble=preamble,comparisons=comparisons,correction='Native evidence/version-identities.json and TeX-unique-segments.json concern INCOMING whole387; their five rows and older preamble do not audit native273 own four-note output. Native ledger wording conflates incoming evidence with current deliverable. This ROOT audit supplies the current identities. Native actual-final-notes.json is expanded serialization, not exact settled FINAL.',native_build_deliverables_and_identity_audit_entirely_read_AS_DATA=True,supplied_or_native_programs_executed_or_imported=False,new_accepted=False,whole_original_solved=False)
O.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(audit=str(O),audit_sha256=sha(O),record=record,all_four_entire_expanded_outside_fields=outside),ensure_ascii=False,indent=2))
