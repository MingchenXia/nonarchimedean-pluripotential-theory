"""Documentary consistency checks; these do not certify the mathematics."""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys

ROOT=Path(__file__).resolve().parent
def sha(raw):return hashlib.sha256(raw).hexdigest()
def main():
 checks=[]
 preservation=json.loads((ROOT/'input-preservation.json').read_text())
 for name,rec in preservation['files'].items():
  raw=(ROOT/name).read_bytes()
  assert sha(raw)==rec['sha256'],name
  assert len(raw)==rec['bytes'],name
 checks.append('All four frozen input hashes and lengths unchanged.')
 raw=(ROOT/'input.json').read_bytes()
 assert raw==(ROOT/'input-original.json').read_bytes()
 frozen=json.loads(raw)
 assert (ROOT/'assignment-original.txt').read_bytes()==frozen['assignment'].encode('utf-8')
 assert json.loads((ROOT/'task-original.json').read_bytes())==frozen['task']
 checks.append('Byte-identical input copies and exact decoded assignment/task checked.')
 provenance=json.loads((ROOT/'source-extracts/source-provenance.json').read_text())
 source_counts={}
 for source in provenance['sources']:
  for kind,rec in source['files'].items():
   raw=(ROOT/rec['local_copy']).read_bytes()
   assert sha(raw)==rec['sha256']
   assert len(raw)==rec['byte_count']
  lines=(ROOT/source['files']['txt']['local_copy']).read_bytes().decode('utf-8').split('\n')
  assert len(lines)==source['LF_split_line_count']
  source_counts[source['id']]=len(lines)
  for rec in source['extracts']:
   literal='\n'.join(lines[rec['start_LF']-1:rec['end_LF']])
   assert literal==rec['literal_text']
   assert literal.encode('utf-8')==(ROOT/rec['local_file']).read_bytes()
   assert sha(literal.encode('utf-8'))==rec['sha256']
 checks.append('Four source copies, LF counts, inclusive extracts and every extract hash checked.')
 status=json.loads((ROOT/'status.json').read_text())
 assert set(status)=={'id','status','exact_result','proof_file','concrete_gaps'}
 assert status['id']=='P15.3' and status['status']=='partial' and status['concrete_gaps']
 checks.append('Exact five-field partial status with concrete original-scope gaps checked.')
 ledger=json.loads((ROOT/'source-application-ledger.json').read_text())
 assert len(ledger['applications'])==7
 argument=(ROOT/'P15.3-argument.md').read_text()
 assert argument.startswith((ROOT/'argument-new.md').read_text())
 old=(ROOT/'retained-scoped-proof.md').read_text().rstrip()
 displayed='\n'.join('#'+line if line.startswith('#') else line for line in old.split('\n'))
 assert displayed in argument
 assert 'candidate=false' in argument
 for app in ledger['applications']:assert app['id'] in argument
 checks.append('New argument, full retained scoped proof and seven source applications present.')
 tex=(ROOT/'P15.3-paper.tex').read_text()
 assert '\\documentclass' in tex and '\\begin{document}' in tex and '\\end{document}' in tex
 assert '\\input{' not in tex and '\\include{' not in tex
 for m in re.finditer(r'\$\$(.*?)\$\$',argument,re.DOTALL):assert '\\['+m.group(1)+'\\]' in tex
 checks.append('Standalone TeX and all main display equations present; no external proof-file include.')
 build=json.loads((ROOT/'build-manifest.json').read_text())
 assert build['generation']['exit_code']==0
 assert len(build['compilations'])==2
 for rec in build['compilations']:
  assert rec['exit_code']==0
  assert (ROOT/rec['stdout']).exists() and (ROOT/rec['stderr']).exists()
  log=(ROOT/rec['tex_log']).read_text()
  assert 'Output written on P15.3-paper.pdf' in log
  assert 'Missing character' not in log
  assert 'Overfull' not in log
 for name,digest in build['artifact_sha256'].items():assert sha((ROOT/name).read_bytes())==digest
 checks.append('Two final XeLaTeX exits zero; separate logs retained; no missing glyphs or overfull boxes.')
 cmd=['pdftotext','P15.3-paper.pdf','P15.3-paper-extracted.txt']
 result=subprocess.run(cmd,cwd=ROOT,capture_output=True)
 (ROOT/'pdf-extraction.stdout').write_bytes(result.stdout)
 (ROOT/'pdf-extraction.stderr').write_bytes(result.stderr)
 assert result.returncode==0
 pdf_text=' '.join((ROOT/'P15.3-paper-extracted.txt').read_text().split())
 for phrase in ['Uniform collapse','Complete retained','Source/application ledger']:
  assert phrase.lower() in pdf_text.lower(),phrase
 checks.append('Generated PDF text contains main theorem/proof, full retained appendix and source ledger.')
 if (ROOT/'notes.json').exists():
  notes=json.loads((ROOT/'notes.json').read_text())
  assert notes['candidate'] is False
  seen=set()
  for note in notes['notes']:
   assert set(note)=={'id','summary','detailedSummary','text','support'}
   assert set(note['support'])<=seen
   seen.add(note['id'])
  checks.append('Canonical draft notes have only earlier local support IDs and candidate=false.')
 report={'kind':'documentary consistency, not mathematical certification','command':[sys.executable,'verify_artifacts.py'],'checks':checks,'source_LF_split_counts':source_counts,'pdf_extraction':{'command':cmd,'exit_code':result.returncode},'status':status['status'],'passed':True}
 (ROOT/'verification.json').write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps(report,indent=2))
if __name__=='__main__':main()
