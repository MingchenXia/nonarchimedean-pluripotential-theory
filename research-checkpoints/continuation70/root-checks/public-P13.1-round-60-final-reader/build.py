from pathlib import Path
import json, subprocess, hashlib, shutil

ROOT=Path(__file__).resolve().parent
def run(cmd,tag):
 p=subprocess.run(cmd,cwd=ROOT,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 (ROOT/(tag+'.stdout')).write_bytes(p.stdout);(ROOT/(tag+'.stderr')).write_bytes(p.stderr)
 return {'command':cmd,'returncode':p.returncode,'stdout':tag+'.stdout','stderr':tag+'.stderr'}
def main():
 report={'runs':[],'versions':{}}
 for tool in ['pandoc','pdflatex']:
  p=subprocess.run([tool,'--version'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
  report['versions'][tool]=p.stdout.decode(errors='replace').split('\n')[0]
 report['runs'].append(run(['pandoc','P13.1-argument.md','--standalone','--from=markdown+tex_math_dollars','--to=latex','--output=P13.1-paper.tex'],'pandoc'))
 assert report['runs'][-1]['returncode']==0
 for i in [1,2]:
  report['runs'].append(run(['pdflatex','-interaction=nonstopmode','-halt-on-error','P13.1-paper.tex'],f'tex-pass-{i}'))
  if (ROOT/'P13.1-paper.log').exists():shutil.copyfile(ROOT/'P13.1-paper.log',ROOT/f'tex-pass-{i}.log')
  if report['runs'][-1]['returncode']!=0:break
 report['all_passed']=len(report['runs'])==3 and all(z['returncode']==0 for z in report['runs'])
 report['artifacts']={name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in ['P13.1-argument.md','P13.1-paper.tex','P13.1-paper.pdf'] if (ROOT/name).exists()}
 (ROOT/'build-report.json').write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps(report));assert report['all_passed']
if __name__=='__main__':main()
