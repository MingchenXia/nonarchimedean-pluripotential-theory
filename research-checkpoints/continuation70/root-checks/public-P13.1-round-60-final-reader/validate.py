from pathlib import Path
import hashlib,json
def main():
 raw=Path('input.json').read_bytes();x=json.loads(raw)
 assert raw==Path('input-original.json').read_bytes()
 assert Path('assignment-original.txt').read_text()==x['assignment']
 assert json.loads(Path('task-original.json').read_bytes())==x['task']
 status=json.loads(Path('status.json').read_text())
 assert set(status)=={'id','status','exact_result','proof_file','concrete_gaps'}
 assert status['status']=='partial' and status['concrete_gaps']
 a=json.loads(Path('source-extracts/source-provenance.json').read_text())
 assert a['all_supplied_hashes_match'] and a['source_count']==10
 c=json.loads(Path('checks-output.json').read_text());assert c['all_checks_pass']
 b=json.loads(Path('build-report.json').read_text());assert b['all_passed']
 for name,h in b['artifacts'].items():assert hashlib.sha256(Path(name).read_bytes()).hexdigest()==h
 notes=json.loads(Path('notes.json').read_text())
 assert not notes['candidate'] and 0<len(notes['notes'])<=4
 known=set()
 for n in notes['notes']:
  assert set(n)=={'id','summary','detailedSummary','text','support'}
  assert set(n['support'])<=known;known.add(n['id'])
 report={'all_checks_pass':True,'input_sha256':hashlib.sha256(raw).hexdigest(),'source_count':10,'excerpt_count':a['excerpt_count'],'status':'partial','candidate':False,'notes':len(known),'build_passes':2,'mathematical_verification':False}
 Path('validation-report.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
if __name__=='__main__':main()
