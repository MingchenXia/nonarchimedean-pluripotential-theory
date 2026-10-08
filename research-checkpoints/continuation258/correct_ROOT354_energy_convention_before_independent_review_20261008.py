from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil

R=Path('/workspace/research');K=R/'root-checks'
W=K/'P12.3-P12.5-continuation354-graded-primary-limits-with-vanishing-energy-and-nonpositive-pointwise-limit-working-proof-20261008.md'
OLD=K/'historical-ROOT354-before-energy-sign-correction-20261008.md'
B=K/'P12.3-P12.5-continuation354-mandatory-energy-sign-correction-before-independent-review-20261008.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not OLD.exists() and not B.exists()
assert sha(W)=='fb281c4c5915d1f4b0fd03e4faf35690ce5b34099403480b0d27d19fc45c8eb8'
s=W.read_text()
replacements={
 'F(u,v)=integral_X u d mu(v),':'F(u,v)=integral_X (-u) d mu(v),',
 'so (5) gives E(u_j)=1/(2j)->0.':'so (5) gives F(u_j,u_j)=1/j and E(u_j)=-1/(2j) increasing to 0.',
 'Let B(u,v)=-F(u,v) on these nonpositive potentials.':'Let B(u,v)=F(u,v) on these nonpositive potentials.'
}
for old,new in replacements.items():assert s.count(old)==1;s=s.replace(old,new)
shutil.copyfile(W,OLD)
W.write_text(s)
now=datetime.now(timezone.utc).isoformat()
record=dict(recorded_utc=now,status='MANDATORY mathematical sign-convention repair before any new independent packet; UNREVIEWED',old_complete_body=dict(path=str(OLD),bytes=OLD.stat().st_size,sha256=sha(OLD)),current_complete_body=dict(path=str(W),bytes=W.stat().st_size,sha256=sha(W)),exact_replacements=replacements,reason='Accepted E350 whole-proof defines F(u,v)=integral(-u)dmu(v), E=-F/2 on a surface. Earlier ROOT354 accidentally used the signed pairing instead while keeping E=-F/2. Correct F is nonnegative, E(u_j)=-1/(2j) tends upward to zero, and Cauchy-Schwarz B=F. Monomial counts, actual measures, capacity estimate, non-USC limit and all-scope conclusions are unchanged.',reading='ENTIRE old proof content physically read, initial outer truncation repaired by fresh4700:8200 display; all exact current replacements stated here. A historical byte binding is not a current-byte binding. No new whole source/pixel claim.',only_grants=['Entire qualified G331','Entire qualified G345','Entire qualified E350'],original_closed=False,accepted_paper=False,protected_editor_open_unchanged=True)
B.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
for name in ['active-work.json','checklist-current.json']:
 p=R/name;x=json.loads(p.read_text());assert len(x['fully_solved_original_atoms'])==15 and x['remaining_open_original_atoms']==27 and x['historical_reviewed_scoped_papers']==96
 x.update(updated_utc=now,ROOT354_mandatory_energy_sign_correction=dict(binding=str(B),proof=record['current_complete_body'],unreviewed=True));p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(record,ensure_ascii=False,indent=2))
