"""Export the unchanged source after native compilation; preserve diagnostics."""
from pathlib import Path
import datetime, hashlib, json, re, shutil, subprocess
r=Path('/workspace/research');out=r/'deliverables/round-25'
tex=out/'P06.2-specified-semistable-tree-regularization.tex'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
native=json.loads((r/'deliverables/round-25-native-verification.json').read_text())
assert native['native_compilation_success'] and sha(tex)==native['source_sha256']
initial=sha(tex);build=out/'export-build';build.mkdir(exist_ok=False);runs=[]
for n in (1,2):
    cmd=['pdflatex','-interaction=nonstopmode','-halt-on-error','-file-line-error','-output-directory='+str(build),tex.name]
    p=subprocess.run(cmd,cwd=out,capture_output=True,text=True)
    (build/f'pass-{n}.stdout.txt').write_text(p.stdout)
    (build/f'pass-{n}.stderr.txt').write_text(p.stderr)
    runs.append({'command':cmd,'exit_code':p.returncode})
    assert p.returncode==0,p.stderr+p.stdout[-2000:]
pdf=out/tex.with_suffix('.pdf').name;shutil.copyfile(build/pdf.name,pdf)
log=(build/tex.with_suffix('.log').name).read_text()
notices={k:[line for line in log.split('\n') if k in line] for k in ['Overfull','Underfull','Missing character','undefined','Warning']}
info=subprocess.run(['pdfinfo',str(pdf)],capture_output=True,text=True,check=True).stdout
(build/'pdfinfo.txt').write_text(info)
pages=int(re.search(r'Pages:\s+(\d+)',info).group(1))
subprocess.run(['pdftoppm','-f','1','-singlefile','-scale-to','1700','-png',str(pdf),str(out/'first-page')],check=True,capture_output=True)
record={'exported_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'source':str(tex),'source_sha256':sha(tex),'source_changed':sha(tex)!=initial,
 'pdf':str(pdf),'pdf_sha256':sha(pdf),'pages':pages,'runs':runs,'final_notices':notices,
 'native_compilation_already_successful':True,'native_compiler_does_not_export_pdf':True}
p=out/'export-evidence.json';assert not p.exists();p.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
