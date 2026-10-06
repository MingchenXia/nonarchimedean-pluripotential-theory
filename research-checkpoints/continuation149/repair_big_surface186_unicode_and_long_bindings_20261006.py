from pathlib import Path
from datetime import datetime,timezone
import re,json,hashlib,subprocess
K=Path('/workspace/research/root-checks');D=K/'public-P16.5-continuation186-entire-surface-equation-reader'
T=K/'P16.5-entire-big-surface-relative-equation-candidate-20261006-continuation186.tex';B=D/'publication-binding.json'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
b=json.loads(B.read_text());assert sha(T)==b['tex_sha256']=='bac9ae2dad77348d567dcd0aca169d43c739e23da3853af833a86aec0cfc1fda'
history=D/'initial-unicode-failed-build-LOCALONLY.json';assert not history.exists();history.write_text(json.dumps(b,indent=2)+'\n')
s=T.read_text()
s=s.replace('\\begin{document}','\\DeclareUnicodeCharacter{1D4E7}{\\ensuremath{\\mathcal X}}\n\\DeclareUnicodeCharacter{00B9}{\\ensuremath{^1}}\n\\begin{document}',1)
s=re.sub(r'\\texttt\{(/workspace/[^}]+)\}',lambda m:'\\nolinkurl{'+m[1]+'}',s)
s=re.sub(r'\\texttt\{([0-9a-f]{64})\}',lambda m:'\\nolinkurl{'+m[1]+'}',s)
s=re.sub(r'(?<![0-9a-f{])([0-9a-f]{64})(?![0-9a-f}])',lambda m:'\\nolinkurl{'+m[1]+'}',s)
T.write_text(s)
a=['pdflatex','-interaction=nonstopmode','-halt-on-error','-file-line-error','-output-directory='+str(D),str(T)];builds=[]
for n in [1,2]:
    r=subprocess.run(a,capture_output=True,text=True);(D/f'final-build-{n}.stdout').write_text(r.stdout);(D/f'final-build-{n}.stderr').write_text(r.stderr);builds.append({'argv':a,'returncode':r.returncode})
    if r.returncode:break
log=(D/(T.stem+'.log')).read_text();pdf=D/(T.stem+'.pdf')
b.update({'recorded_utc':datetime.now(timezone.utc).isoformat(),'tex_sha256':sha(T),'builds':builds,
          'overfull':log.count('Overfull'),'undefined':log.count('undefined'),'warnings':log.count('Warning'),
          'pdf':str(pdf) if pdf.exists() else None,'pdf_sha256':sha(pdf) if pdf.exists() else None,
          'typesetting_repair':'Declare mathematical script-X and superscript-one Unicode; wrap long documentary paths and hashes in breakable nolinkurl. Mathematical Markdown unchanged.'})
if pdf.exists():
    info=subprocess.run(['pdfinfo',str(pdf)],capture_output=True,text=True,check=True).stdout
    b['pages']=int(next(x.split(':')[1] for x in info.splitlines() if x.startswith('Pages:')))
B.write_text(json.dumps(b,indent=2)+'\n')
print(json.dumps({k:b.get(k) for k in ['tex_sha256','pdf_sha256','pages','overfull','undefined','warnings','builds']},indent=2))
if builds[-1]['returncode']:print(r.stdout[-3500:])
