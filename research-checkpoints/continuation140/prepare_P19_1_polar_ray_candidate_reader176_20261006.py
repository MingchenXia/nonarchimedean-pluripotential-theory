from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess
import fitz

R=Path('/workspace/research');K=R/'root-checks'
M=K/'P19.1-arbitrary-bounded-rays-trivial-NA-infinite-entropy-counterexample-candidate-20261006-continuation176.md'
D=K/'public-P19.1-continuation176-candidate-reader'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not D.exists()
assert 'Original totals remain 7 solved and 35 open' in M.read_text()
assert 'b_F^{-1}' in M.read_text()
D.mkdir()
shutil.copyfile(M,D/'P19.1-argument.md')
commands=[['pandoc','P19.1-argument.md','--standalone','--from=markdown+tex_math_dollars+tex_math_single_backslash','--to=latex','--output=P19.1-paper.tex']]
commands += [['pdflatex','-interaction=nonstopmode','-halt-on-error','-file-line-error','P19.1-paper.tex']]*2
builds=[]
for i,command in enumerate(commands):
    p=subprocess.run(command,cwd=D,capture_output=True,text=True)
    (D/f'build-{i}.stdout').write_text(p.stdout)
    (D/f'build-{i}.stderr').write_text(p.stderr)
    builds.append({'argv':command,'returncode':p.returncode})
    assert p.returncode==0,(i,p.stdout[-2200:],p.stderr[-1500:])
pdf=fitz.open(D/'P19.1-paper.pdf');pages=len(pdf)
for i in sorted(set([0,pages//2,pages-1])):
    pdf[i].get_pixmap(matrix=fitz.Matrix(1.3,1.3)).save(D/f'layout-page-{i+1}.png')
log=(D/'P19.1-paper.log').read_text()
sources=R/'campaigns/family-11-retry-1/artifacts/codex-aB4toH/sources'
ledger={'recorded_utc':datetime.now(timezone.utc).isoformat(),'atom':'P19.1','candidate':True,
 'whole_final_mathematical_argument_root_read':True,'whole_generated_tex_separately_root_read':False,
 'independently_accepted':False,'original_closed':False,
 'scope':'All products P1 times arbitrary compact Kahler Y: actual bounded weak rays with trivial actual NA datum, energy slope -a^2/2, infinite entropy slope. Obstruction to an unrestricted identity; the full original residual scope remains open.',
 'inputs':[
  {'source':'Darvas--Di Nezza--Lu arXiv:1705.05796v3','url':'https://arxiv.org/pdf/1705.05796v3',
   'proof_units_root_read':'Section 3.2 mass-preservation discussion and complete Theorem 3.12 proof',
   'browser_line_coordinates':[[1396,1445],[1830,1883]],
   'application':'The envelope of tau psi is model and has mass 1-tau for 0<tau<a<1. Underlying convergence and monotonicity theorems are imported.'},
  {'source':'Darvas--Xia, Advances in Mathematics 397 (2022), 108198',
   'url':'https://doi.org/10.1016/j.aim.2022.108198',
   'pdf_sha256':sha(sources/'darvas_xia_2003.04818.pdf'),'text_sha256':sha(sources/'darvas_xia_2003.04818.txt'),
   'literal_text_ranges_root_read':[[1170,1204],[1670,2145],[2140,2310]],
   'application':'Theorems 3.7(iii),(iv), Proposition 3.8: the actual bounded weak ray and its exact normalized energy. Optional projective cross-check Proposition 3.13. Example 2.19 is motivation; the explicit polar Cantor construction and estimates are written independently.'},
  {'source':'P. Mesquita--Piccione arXiv:2409.06221v2','url':'https://arxiv.org/pdf/2409.06221v2',
   'pdf_sha256':sha(sources/'mp_2409.06221v2.pdf'),'text_sha256':sha(sources/'mp_2409.06221v2.txt'),
   'literal_text_ranges_root_read':[[1640,1717],[1850,1950],[2385,2555],[2735,2855]],
   'application':'Actual total-ray datum and divisorial determination, Theorem 5.1.4/Remark 5.1.5; normalized zero-metric model measure Section 4.2.1. This candidate explicitly fixes discrepancy over X, time, and b_F normalization.'}
 ],
 'argument_sha256':sha(D/'P19.1-argument.md'),'tex_sha256':sha(D/'P19.1-paper.tex'),
 'pdf_sha256':sha(D/'P19.1-paper.pdf'),'PDF_pages':pages,'local_builds':builds,
 'overfull_diagnostics':log.count('Overfull'),'undefined_diagnostics':log.count('Undefined'),
 'actual_visual_pages':[],'native_compiler_success_observed':False,
 'originals_solved':7,'originals_open':35,'accepted_scoped_papers':49,
 'existing_P16_4_editor_modified_or_new_tab_opened':False,
 'primary_source_pdfs_or_long_excerpts_in_public_reader':False}
(D/'source-application-and-publication-binding.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n')
(D/'README.md').write_text('Root-authored, unreviewed candidate. A direct polar-ray counterexample to entropy being determined by the usual NA datum for all bounded weak rays, including nonprojective Kahler products. P19.1 remains open until an independent comparison with the original scope. The main argument, TEX and PDF contain the full candidate proof; source files are referenced by version, coordinates and hashes only. The current P16.4 editor is unchanged.\n')
print(json.dumps({'reader':str(D),'binding':ledger},indent=2))
