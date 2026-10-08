from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil
R=Path('/workspace/research');K=R/'root-checks'
C=next((R/'campaigns/round-229').iterdir());A=C/'artifacts/codex-zLZUxL'
D=K/'public-P14.8-continuation308-arbitrary-formal-ideal-realization-on-projective-line'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
actual=K/'round229-actual-native-final.json';j=json.loads(actual.read_text())
assert sha(actual)=='e8b5b80509be6bdc63d56a385583cd7cb21fe59c18c604c399c8bb939bee1e64' and not j['candidate'] and len(j['notes'])==4
assert sha(D/'P14.8-paper.tex')=='3e8ea22f01ca3574aa4e08ed5ded84fab03a9f9a07e7d72c9c4d67b71e23d92d'
for name,count in [('mathematical-packet-bindings.json',1),('historical-own-evidence-bindings.json',8)]:
 rows=json.loads((C/name).read_text());assert len(rows)==count
 for e in rows:assert Path(e['path']).stat().st_size==e['bytes'] and sha(e['path'])==e['sha256']
rows=json.loads((A/'report-hashes.json').read_text());assert len(rows)==43
for e in rows:
 p=A/e['path'];assert p.is_relative_to(A) and p.stat().st_size==e['bytes'] and sha(p)==e['sha256']
saved=json.loads((A/'audit-notes.json').read_text());assert len(saved['notes'])==4
assert all(n['id']==s['id'] and n['support']==s['support'] for n,s in zip(j['notes'],saved['notes']))
pub=D/'evidence/independent-failed-audit229';record=K/'P14.8-round229-projective-line-representative-failure-binding-20261008.json'
before=D/'evidence/pre-representative-repair-20261008'
assert not any(p.exists() for p in [pub,record,before]);pub.mkdir();before.mkdir()
for n in ['n1-local-proof.md','n2-global-audit.md','n3-build-evidence.md','n4-verdict.md','audit-report.md','report-hashes.json','verification.json']:
 shutil.copyfile(A/n,pub/n)
for p in [actual,K/'round229-registered-native-result.json',K/'round229-actual-final-extraction-binding-20261008.json']:shutil.copyfile(p,pub/p.name)
for n in ['P14.8-paper.tex','P14.8-paper.pdf','ROOT-working-proof-and-build-binding-20261008.json']:shutil.copyfile(D/n,before/n)
value=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),round=229,continuation=308,unchanged_source_sha256=sha(D/'P14.8-paper.tex'),actual_FINAL_sha256=sha(actual),mathematical_verdict='FAIL unchanged pointwise representative assertion at line105',bounded_evidence_verdict='PASS',ordinary_premises_and_intended_criterion_independently_proved_with_a_e_representative=True,all4_actual_FINAL_and_unique_expanded_reports_ROOT_read=True,source_authority='INCONCLUSIVE absent primary-source supply; ordinary premises independently reconstructed',frozen_bindings_verified=9,own_bindings_verified=43,saved_actual_equal=j==saved,saved_expanded_prose_not_claimed_whole_ROOT_read=True,supplied_scripts_not_executed_or_imported=True,original_closed_by_this_review=False,new_accepted_paper=False,counts_unchanged=dict(solved=10,open=32,accepted=88),general_original_closed_separately_by_audit230=True,reviewer_general_OPEN_statement_is_frozen_historical_scope=True,required_repair='Take canonical subharmonic representative of local L1 distribution almost everywhere; multiplier ideals are unchanged. Retain original counterexample and FAIL.',pre_repair_snapshot=str(before),protected_editor_unchanged_open=True)
record.write_text(json.dumps(value,indent=2)+'\n')
for n in ['active-work.json','checklist-current.json']:
 p=R/n;x=json.loads(p.read_text());assert x['historical_reviewed_scoped_papers']==88 and len(x['fully_solved_original_atoms'])==10
 x['P14_8_projective_line308_audit229_failure']=value;x['prepared_P1_formal_ideal_audit229'].update(completed=True,unchanged_mathematical_verdict='FAIL',repair_pending=True,new_accepted_paper=False);p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(binding=str(record),sha256=sha(record),verdict='FAIL unchanged; representative repair required'),indent=2))
