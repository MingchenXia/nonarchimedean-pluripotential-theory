from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,subprocess,re
R=Path('/workspace/research');K=R/'root-checks';D=K/'public-P16.5-own138-candidate-reader'
assert not D.exists();D.mkdir(parents=True)
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
parts=[('I. Bounded genuine products and continuous-obstacle variation',R/'deliverables/scoped-P16.5-round122/P16.5-argument.md'),
 ('II. The entire intrinsic floor operator',K/'P16.5-entire-nef-floor-energy-operator-and-weighted-floor-limits-draft-20261005-continuation133.md'),
 ('III. Mixed weighted nets and both outer derivatives',K/'P16.5-nef-entire-mixed-weighted-nets-and-two-sign-outer-draft-20261005-continuation134.md'),
 ('IV. Weak energy usc, intrinsic targets and coercivity',K/'P16.5-nef-weak-energy-usc-intrinsic-targets-and-coercivity-draft-20261005-continuation135.md'),
 ('V. Corrected polar capacity and original observables',K/'P16.5-nef-polar-capacity-and-original-observable-control-draft-20261005-continuation136-repair2.md'),
 ('VI. Divisorial atomic attainment and all-point separation',K/'P16.5-nef-divisorial-atomic-attainment-and-I-separation-draft-20261005-continuation137.md'),
 ('VII. The full nef-and-big variational argument',K/'P16.5-nef-big-full-intrinsic-variational-attainment-draft-20261005-continuation138.md')]
text='''# Intrinsic finite-energy equations for nef and big line bundles

Candidate research paper. Independent review of the complete nef-and-big equation has been prepared and is pending a free native solver slot. Original P16.5 remains open. Part I has a scoped independent PASS; the remaining parts are proposed deductions and must be reconstructed together before acceptance.

The original carrier is the entire analytification of a smooth integral projective variety over an algebraically closed trivially valued characteristic-zero field of arbitrary cardinality. The main candidate retains an actual nef and numerically big rational bundle, its canonical zero reference, positive raw top intersection mass, the entire intrinsic floor-defined finite-energy cone and every finite-dual-energy Radon target. General nonnef minimal references, nonbig nonzero numerical data and separate section-volume identification remain outside the candidate conclusion.

All indispensable nonample proof bodies are included. The exact actual-ample variational theorem G0 is the sole previously accepted equation input, applied only in its ample domain; the proposed nonample deductions are not grants. The proof-part labels correspond to own proposals122/133/134/135/136-repair2/137/138. The original unreviewed136 paragraph asserting both small signs of a PL function are ample-psh is withdrawn and replaced in Part V by the correct difference of two ample-psh functions. Historical limited conclusions in earlier parts describe the boundary of those parts; Part VII proposes the subsequent attainment argument.

'''
bindings=[]
for title,p in parts:
 s=p.read_text();lines=s.split('\n');assert lines[0].startswith('# ')
 body='\n'.join(lines[1:])
 body=re.sub(r'^(#{2,6}) ',lambda m:'#'+m.group(1)+' ',body,flags=re.M)
 text+='\n## '+title+'\n'+body+'\n'
 bindings.append({'part':title,'path':str(p),'sha256':sha(p),'whole_constituent_proof_root_read':True,'transformation':'Remove only repeated top-level title and shift its lower headings down one level; mathematical body retained verbatim.'})
(D/'P16.5-argument.md').write_text(text)
commands=[['pandoc','P16.5-argument.md','--standalone','--from=markdown+tex_math_dollars+tex_math_single_backslash','--to=latex','--output=P16.5-paper.tex']]+[['pdflatex','-interaction=nonstopmode','-halt-on-error','-file-line-error','P16.5-paper.tex']]*2
returns=[]
for i,cmd in enumerate(commands):
 r=subprocess.run(cmd,cwd=D,capture_output=True,text=True);(D/f'build-{i}.stdout').write_text(r.stdout);(D/f'build-{i}.stderr').write_text(r.stderr);returns.append(r.returncode)
 assert r.returncode==0,(i,r.stdout[-3000:])
info=subprocess.run(['pdfinfo',str(D/'P16.5-paper.pdf')],capture_output=True,text=True,check=True).stdout;(D/'pdfinfo.txt').write_text(info)
pages=int(re.search(r'^Pages:\s+(\d+)',info,re.M).group(1))
meta={'recorded_utc':datetime.now(timezone.utc).isoformat(),'independently_accepted':False,'original_closed':False,'parts':bindings,
 'all_whole_constituent_math_proofs_root_read':True,'whole_assembled_argument_separately_root_read':False,'whole_generated_tex_separately_root_read':False,
 'argument_sha256':sha(D/'P16.5-argument.md'),'source_sha256':sha(D/'P16.5-paper.tex'),'pdf_sha256':sha(D/'P16.5-paper.pdf'),'PDF_pages':pages,'local_build_returns':returns,
 'native_compiler_success_asserted':False,'existing_P16_4_editor_modified_or_new_tab_opened':False}
(D/'publication-preparation.json').write_text(json.dumps(meta,indent=2)+'\n')
print(json.dumps({k:meta[k] for k in ['argument_sha256','source_sha256','pdf_sha256','PDF_pages','local_build_returns','independently_accepted','original_closed']},indent=2))
