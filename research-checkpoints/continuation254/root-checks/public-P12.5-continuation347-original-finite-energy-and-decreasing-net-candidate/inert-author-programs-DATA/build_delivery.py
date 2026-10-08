"""Generate fresh notes and standalone TeX; never compile or run supplied code."""
import hashlib, json, pathlib, re, subprocess

ROOT=pathlib.Path(__file__).resolve().parent
request=json.loads((ROOT/'input.json').read_text())
grants=ROOT/'inputs'/'grants';grants.mkdir(parents=True,exist_ok=True)
for note in request['notes']:
    assert note['id'] in ['G331','B341']
    (grants/(note['id']+'-qualified.txt')).write_text(note['text'])
source=(ROOT/'argument.md').read_text()
parts=re.split(r'(?m)^# (n\d+)\. ([^\n]+)\n',source)
assert len(parts)==28
metadata={
 'n1':('Full-boundary domain, explicit R_red/top-degree conventions, zero anchor and exactly delimited qualified imports.','Only entire G331/B341 are granted; new geometry and energy are not imported. Every support is retained, with n-1 product slots and raw degree-n energy; lower-dimensional components remain but contribute zero. n0 is separate.'),
 'n2':('Independent supported Cartier intersection: Artinian Euler polynomial, Koszul symmetry, actual divisor-cycle projection and raw Rees polarization.','Proof uses actual exceptional Cartier divisors on primary models, including nonnormal/non-CM/mixed-characteristic cases. Field-scheme Stacks intersection is applied only after an Artinian filtration; supported degree preserves DVR degree rather than global Chow degree.'),
 'n3':('Independent nonnegative divisorial core measures, supplied refinement lemma, fixed-primary invertible-image bridge and full bounded ordinary open locality.','Uses one fixed Bl_(I c0), actual J_q image equality and finite-span real intersections. Atomic strict maximum follows from invertible subideal restriction; two compact-cover limits extend locality to bounded actual D. No Borel/plurifine locality is claimed.'),
 'n4':('Full bounded symmetric n-form with genuine discontinuous D pairing; arbitrary fixed-slot Cauchy, n-entry Holder, Minkowski and concavity.','Directed Radon supremum is proved for continuous families. All three multiplicities use the same simultaneous superficial 2D quotient; R(z) handles finite fields and no CM/deletion assumption is made. Finite integer simplex proves generalized Holder; printed SH colon is not used.'),
 'n5':('Truncation E1 and full majorant supremum; noncircular approximation without common bound, cone closure, canonical measures and full decreasing E1 nets.','Finite target sizes provide uniform scalar shift errors before unbounded additivity. E1 cone closure is proved first; moments and density yield finite Radon measures. Decreasing-net continuity requires a specified D/E1 limit; no arbitrary-infimum or increasing closure is asserted.'),
 'n6':('Extended D test pairing, E1 integrability, polynomial variation, finite reference cocycle, elementary capacity estimate and finite-energy open locality.','Actual C representations and justified suprema prove E1 pairing; truncations give extended D pairing. Capacity estimate proves E1 pole capacity zero but no Choquet/quasicontinuity or strict nonpluripolar cutoff theorem. Concavity has no uniqueness implication.'),
 'n7':('Gauge energy invariance with exactly one measure factor; inseparable residue-weighted normalization, full fibre-constant E1 descent, actual curves and empty case.','Variable cuts max(u,-k v_a(b)) are squeezed by constant cuts. Only top-dimensional normalization centres enter raw degree-n energy, while all lower-dimensional supports remain in conductor compatibility. R_red is explicit; arbitrary finite-map operator traces are not claimed.'),
 'n8':('Entire smooth finite-energy comparison with the canonical finite BFJ Definition4.3 local self-intersection convention, at exact published hypotheses.','A direct majorant proof compares all C majorants and nef Cartier majorants, giving the whole space and operator, not just bounded agreement. No unbounded energy theorem is inferred from the bounded grant; no forced Cegrell/global BJ identity or broadened multiplier scope.'),
 'n9':('Complete original P12.5 draft solution claim under the explicit canonical local intersection convention; bounded reproducibility evidence and review boundary.','All new geometric and finite-energy obligations are proved in n1--n8. 21,520 declared finite cases pass; an early finite-difference counterexample is retained. Independent review, ROOT reading/compiler and acceptance remain external; candidate=true is only a draft solution claim.')
}
notes=[]
for i in range(1,len(parts),3):
    note_id,title,body=parts[i:i+3]
    supports=re.search(r'^\s*Supports: (.*?)\.',body).group(1).split(', ')
    text=title+'\n'+body.strip()+'\n\nArtifacts: argument.md, '+note_id+'.md, P12.5-paper.tex, native-notes.json, source-application-ledger.md and reports. Rerun from this directory: python prepare.py; python exact_diagnostics.py; python build_delivery.py; python final_audit.py. No compilation or mathematical verification is asserted.'
    summary,detailed=metadata[note_id]
    note={'id':note_id,'summary':summary,'detailedSummary':detailed,'text':text,'support':supports}
    notes.append(note)
    (ROOT/(note_id+'.md')).write_text('# '+note_id+'. '+title+'\n'+body.strip()+'\n')
(ROOT/'native-notes.json').write_text(json.dumps({'notes':notes,'candidate':True},ensure_ascii=False,indent=2)+'\n')
args=['pandoc','argument.md','--from=markdown+tex_math_dollars','--to=latex','--standalone','--toc','--metadata=documentclass:article','-V','geometry:margin=1in','-V','fontsize=11pt','-o','P12.5-paper.tex']
run=subprocess.run(args,cwd=ROOT,text=True,capture_output=True)
report={'argv':args,'returncode':run.returncode,'stdout':run.stdout,'stderr':run.stderr,'compilation':False,'kind':'TeX source generation only'}
(ROOT/'reports'/'tex-generation.json').write_text(json.dumps(report,indent=2)+'\n')
assert run.returncode==0,run.stderr
tex=(ROOT/'P12.5-paper.tex').read_text()
tex=tex.replace('\\begin{document}', '\\usepackage{listings}\n\\lstset{basicstyle=\\ttfamily\\scriptsize,breaklines=true,columns=fullflexible,keepspaces=true,showstringspaces=false}\n\\begin{document}',1)
appendix='\n\\appendix\n'
for note in request['notes']:
    payload=note['text']
    assert '\\end{lstlisting}' not in payload
    assert all(ord(c)<128 for c in payload)
    appendix+='\\clearpage\n\\section{Entire qualified '+note['id']+' import, verbatim}\n\\begin{lstlisting}\n'+payload+'\n\\end{lstlisting}\n'
for filename in ['source-application-ledger.md','exact-scope.md','whole-proof-coverage.md','original-scope-and-noncircularity-decision.md']:
    payload=(ROOT/filename).read_text()
    assert '\\end{lstlisting}' not in payload
    appendix+='\\clearpage\n\\section{'+filename.replace('-',' ').replace('.md','')+'}\n\\begin{lstlisting}\n'+payload+'\n\\end{lstlisting}\n'
assert tex.count('\\end{document}')==1
tex=tex.replace('\\end{document}',appendix+'\\end{document}')
(ROOT/'P12.5-paper.tex').write_text(tex)
print(json.dumps({'notes':len(notes),'candidate_draft':True,'tex_bytes':len(tex.encode()),'grant_bodies_embedded_verbatim':True,'compiler_run':False}))
