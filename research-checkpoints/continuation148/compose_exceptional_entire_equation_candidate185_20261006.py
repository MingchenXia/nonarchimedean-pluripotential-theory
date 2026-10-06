from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,subprocess
K=Path('/workspace/research/root-checks')
source=K/'P16.5-entire-big-exceptional-cones-in-all-dimensions-candidate-20261006-continuation184.tex'
unit=K/'P16.5-exceptional-relative-equation-proof-unit-20261006-continuation185.txt'
dest=K/'P16.5-exceptional-big-cone-entire-relative-equation-candidate-20261006-continuation185.tex'
assert not dest.exists()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
base=source.read_text();assert sha(source)=='9d50008869cfa85c5527275b7d7a7fa06c0c145090803da17aa08c7c06d1efd7'
front=base.split('\\section{The exact domain and objects}')[0]
front=front.replace('\\newcommand{\\vol}{\\operatorname{vol}}','\\newcommand{\\vol}{\\operatorname{vol}}\n\\newcommand{\\MA}{\\operatorname{MA}}')
front=front.replace('\\title{Entire big exceptional cones in every dimension}','\\title{An entire relative finite-energy equation for big exceptional classes}')
start=front.index('\\begin{abstract}');end=front.index('\\end{abstract}')+len('\\end{abstract}')
front=front[:start]+'''\\begin{abstract}
For the nonnef big class $L=\\pi^*A+cE$ on a blowup of a smooth
center, this unreviewed candidate constructs the whole genuine
relative finite-energy equation in every dimension. Exact section
division first identifies the entire genuine cone. A quadratic
ample-energy test excludes mass on the center. Actual moving model
intersections then define the original-carrier operator, with
weighted unbounded limits. Compact-coordinate envelopes and cutoff
comparisons prove both outer energy derivatives for every original
continuous direction. The intrinsic compensator dual energy yields
attained equations, comparison and uniqueness for all solutions.
The raw mass is $\\operatorname{vol}(L)=A^n$. The sole equation
premise is the whole exact actual-ample theorem. The construction
has not undergone independent review and does not solve original
P16.5 for arbitrary big or zero-volume pseudoeffective classes.
\\end{abstract}'''+front[end:]
structure='\\section{The exact domain and objects}'+base.split('\\section{The exact domain and objects}',1)[1].split('\\section{What this repairs and what remains}',1)[0]
structure=structure.replace('\\begin{theorem}[Unreviewed structural candidate]','\\begin{theorem}[Structural gate]')
dest.write_text(front+structure+'\n'+unit.read_text()+'\n\\end{document}\n')
D=K/'public-P16.5-continuation185-exceptional-equation-reader';D.mkdir(exist_ok=False)
a=['pdflatex','-interaction=nonstopmode','-halt-on-error','-file-line-error','-output-directory='+str(D),str(dest)];builds=[]
for n in [1,2]:
 r=subprocess.run(a,capture_output=True,text=True);(D/f'build-{n}.stdout').write_text(r.stdout);(D/f'build-{n}.stderr').write_text(r.stderr);builds.append({'argv':a,'returncode':r.returncode})
 if r.returncode:print(r.stdout[-4000:]);break
log=(D/(dest.stem+'.log')).read_text();pdf=D/(dest.stem+'.pdf')
b={'recorded_utc':datetime.now(timezone.utc).isoformat(),'tex':str(dest),'tex_sha256':sha(dest),
 'whole_final_tex_root_read':False,'proof_units':[{'path':str(source),'sha256':sha(source),'whole_unit_root_read':True},
 {'path':str(unit),'sha256':sha(unit),'whole_unit_root_read':False}],
 'builds':builds,'overfull':log.count('Overfull'),'undefined':log.count('undefined'),'warnings':log.count('Warning'),
 'pdf':str(pdf) if pdf.exists() else None,'pdf_sha256':sha(pdf) if pdf.exists() else None,'actual_visual_pages':[],
 'native_compile_success_observed':False,'independent_review':False,'original_closed':False,'accepted_count_change':0,
 'existing_editor_unchanged':True,'existing_native135136_inputs_changed':False}
if pdf.exists():
 info=subprocess.run(['pdfinfo',str(pdf)],capture_output=True,text=True,check=True).stdout
 b['pages']=int(next(x.split(':')[1] for x in info.splitlines() if x.startswith('Pages:')))
(D/'publication-binding.json').write_text(json.dumps(b,indent=2)+'\n');print(json.dumps(b,indent=2))
