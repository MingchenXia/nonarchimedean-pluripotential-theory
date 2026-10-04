from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import shutil
import subprocess

d = Path('/workspace/research/root-checks/P16.1-nodal-obstruction-paper-20261004')
tex = d / 'P16.1-nodal-obstruction-paper.tex'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert sha(tex) == 'e3d38083b7a4740869a7fefbff2de838bef3dd09e8d4d2812122234213860226'
assert sha(d / 'preparation-binding.json') == '7bfbd114beebfcd5bfc6d09af78592eec52b1e299c1f0c9937d27df094b11846'
native = d / 'native-editor-result.json'
assert not native.exists()
native.write_text(json.dumps({'requested_utc':'2026-10-04 15:39:37 UTC','exec_cell':'1825',
    'path':str(tex),'source_sha256':sha(tex),
    'open_result':{'status':'queued','threadId':'01a100b0-99da-770b-a765-a51e5c89404d'},
    'compile_result':{'path':str(tex),'kind':'success',
        'message':"The current source compiled successfully with the desktop editor's compiler."},
    'editor_open_verified':False,'editor_close_requested':False,
    'compiler_confirmed_success':True,'exported_pdf_returned':False},indent=2)+'\n')
out = d / 'local-pdf'
out.mkdir(exist_ok=False)
shutil.copyfile(tex,out/tex.name)
assert (out/tex.name).read_bytes()==tex.read_bytes()
commands=[]
for n in (1,2):
    cmd=['pdflatex','-interaction=nonstopmode','-halt-on-error',tex.name]
    run=subprocess.run(cmd,cwd=out,capture_output=True,text=True)
    (out/f'pdflatex-pass-{n}.stdout').write_text(run.stdout)
    (out/f'pdflatex-pass-{n}.stderr').write_text(run.stderr)
    log=out/(tex.stem+'.log')
    if log.exists():shutil.copyfile(log,out/f'pdflatex-pass-{n}.log')
    warnings=[s for s in run.stdout.split('\n') if re.search(r'Warning|Overfull|Underfull|^!',s)]
    commands.append({'pass':n,'command':cmd,'returncode':run.returncode,'warnings':warnings})
    assert run.returncode==0,run.stdout[-3000:]
pdf=out/(tex.stem+'.pdf')
text_file=out/(tex.stem+'.pdf.txt')
extract=subprocess.run(['pdftotext','-layout',str(pdf),str(text_file)],capture_output=True,text=True)
assert extract.returncode==0,extract.stderr
info=subprocess.run(['pdfinfo',str(pdf)],capture_output=True,text=True)
assert info.returncode==0,info.stderr
(out/'pdfinfo.txt').write_text(info.stdout)
pages=int(re.search(r'^Pages:\s+(\d+)',info.stdout,re.M).group(1))
for n,name in ((1,'first-page'),(pages,'last-page')):
    run=subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-singlefile','-scale-to','1500',
        '-png',str(pdf),str(out/name)],capture_output=True,text=True)
    assert run.returncode==0,run.stderr
def bind(p):
    p=Path(p)
    return {'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)}
result={'built_utc':datetime.now(timezone.utc).isoformat(),
    'full_root_tex_read_LF':[1,346],'native_compile_success':True,
    'native_compilation_record':bind(native),'native_editor_open':'Queued; actual editor opening not independently observed.',
    'source':bind(tex),'local_source_byte_equal_to_native_compiled_source':True,
    'local_export_purpose':'Produce a downloadable standalone PDF; native compilation returned no exported PDF.',
    'commands':commands,'pdf':bind(pdf),'pdf_pages':pages,'pdf_text':bind(text_file),
    'pdftotext_returncode':extract.returncode,'pdf_visual_inspection':'Not yet performed.',
    'independent_mathematical_acceptance':False,'original_atoms_closed':[],
    'active_authors_received_feedback':False,'external_export_attempted':False}
(d/'build-result.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'pdf':bind(pdf),'pages':pages,'passes':commands,
    'build_result':bind(d/'build-result.json')},indent=2))
