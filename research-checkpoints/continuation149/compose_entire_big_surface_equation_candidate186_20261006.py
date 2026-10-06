from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,subprocess
R=Path('/workspace/research');K=R/'root-checks'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
U=K/'P16.5-entire-big-surface-relative-equation-proof-unit-20261006-continuation186.md'
surface=K/'public-P16.5-round135-partial-surface-research-reader/P16.5-argument.md'
sources=[('A. Complete pseudoeffective surface structure and exact zero ranges',surface),
 ('B. Entire intrinsic nef operator, weighted limits, outer derivatives and dual',K/'public-P16.5-round124-final-reader/P16.5-argument.md'),
 ('C. Genuine polar tests and original continuous observables',K/'P16.5-nef-polar-capacity-and-original-observable-control-draft-20261005-continuation136-repair2.md'),
 ('D. Divisorial atomic attainment and all-point numerical separation',K/'P16.5-nef-divisorial-atomic-attainment-and-I-separation-draft-20261005-continuation137.md'),
 ('E. Intrinsic target-integral continuity and attained nef-and-big equations',K/'P16.5-nef-big-full-intrinsic-variational-attainment-draft-20261005-continuation138.md')]
dest=K/'P16.5-entire-big-surface-relative-equation-candidate-20261006-continuation186.md'
T=dest.with_suffix('.tex');D=K/'public-P16.5-continuation186-entire-surface-equation-reader'
assert not dest.exists() and not T.exists() and not D.exists();D.mkdir()
front='''---
title: "A relative finite-energy equation on the entire big rational surface cone"
author: "Unreviewed mathematical candidate"
date: "6 October 2026"
geometry: margin=0.85in
fontsize: 10pt
header-includes:
  - \\usepackage{amsmath,amssymb,amsthm}
  - \\usepackage{longtable}
---

'''
body=front+U.read_text();units=[{'label':'Whole new relative surface proof','path':str(U),'sha256':sha(U),'whole_body_root_read':True}]
for label,p in sources:
    s=p.read_text()
    if p==surface:
        lines=s.splitlines();s='\n'.join(lines[19:385])+'\n';coords=[20,385]
    else:coords=[1,len(s.splitlines())]
    body+='\n\n# Appendix '+label+'\n\n'
    body+='The following complete mathematical derivation is retained as supporting proof, with its earlier scope statements. It is not a historical-verdict grant. Equation numbers in this appendix are local to it. The main candidate and the fresh review criteria govern the new combined scope.\n\n'
    body+=s
    units.append({'label':label,'path':str(p),'whole_source_sha256':sha(p),'literal_LF_range':coords,
                  'included_unit_sha256':hashlib.sha256(s.encode()).hexdigest(),'whole_included_unit_root_read':True})
dest.write_text(body)
# Type-setting declarations preserve symbols in the literal proof appendices.
maps={'θ':'\\theta','ε':'\\epsilon','φ':'\\varphi','μ':'\\mu','ν':'\\nu','α':'\\alpha','δ':'\\delta','ω':'\\omega','ρ':'\\rho',
      '≥':'\\geq','≤':'\\leq','−':'-','∈':'\\in','∩':'\\cap','→':'\\to','∞':'\\infty','∫':'\\int','∏':'\\prod','Σ':'\\sum',
      '∥':'\\Vert','≲':'\\lesssim','×':'\\times','∧':'\\wedge','⊂':'\\subset','⊗':'\\otimes','∅':'\\varnothing','↔':'\\leftrightarrow'}
header=D/'unicode-math-header.tex'
header.write_text(''.join('\\DeclareUnicodeCharacter{'+format(ord(c),'04X')+'}{\\ensuremath{'+v+'}}\n' for c,v in maps.items()))
argv=['pandoc',str(dest),'--standalone','--from=markdown+tex_math_single_backslash','--to=latex','--include-in-header='+str(header),'--output='+str(T)]
r=subprocess.run(argv,capture_output=True,text=True);(D/'source-build.stdout').write_text(r.stdout);(D/'source-build.stderr').write_text(r.stderr)
assert r.returncode==0,r.stderr
a=['pdflatex','-interaction=nonstopmode','-halt-on-error','-file-line-error','-output-directory='+str(D),str(T)];builds=[]
for n in [1,2]:
    r=subprocess.run(a,capture_output=True,text=True);(D/f'build-{n}.stdout').write_text(r.stdout);(D/f'build-{n}.stderr').write_text(r.stderr);builds.append({'argv':a,'returncode':r.returncode})
    if r.returncode:break
log=(D/(T.stem+'.log')).read_text();pdf=D/(T.stem+'.pdf')
b={'recorded_utc':datetime.now(timezone.utc).isoformat(),'markdown':str(dest),'markdown_sha256':sha(dest),
   'tex':str(T),'tex_sha256':sha(T),'whole_final_markdown_separately_root_read':False,'whole_final_tex_separately_root_read':False,
   'whole_new_relative_proof_root_read':True,'proof_units':units,'builds':builds,
   'overfull':log.count('Overfull'),'undefined':log.count('undefined'),'warnings':log.count('Warning'),
   'pdf':str(pdf) if pdf.exists() else None,'pdf_sha256':sha(pdf) if pdf.exists() else None,'actual_visual_pages':[],
   'native_compile_success_observed':False,'independent_review':False,'original_closed':False,'accepted_count_change':0,
   'existing_editor_unchanged':True,'existing_native136137_inputs_changed':False,
   'scope':'Entire big rational surface relative equation candidate and rigid zero-volume surface range; original arbitrary-dimensional P16.5 remains open.'}
if pdf.exists():
    info=subprocess.run(['pdfinfo',str(pdf)],capture_output=True,text=True,check=True).stdout
    b['pages']=int(next(x.split(':')[1] for x in info.splitlines() if x.startswith('Pages:')))
(D/'publication-binding.json').write_text(json.dumps(b,indent=2)+'\n')
print(json.dumps({k:b.get(k) for k in ['markdown_sha256','tex_sha256','pdf_sha256','pages','overfull','undefined','warnings','builds']},indent=2))
if builds[-1]['returncode']:print(r.stdout[-5000:])
