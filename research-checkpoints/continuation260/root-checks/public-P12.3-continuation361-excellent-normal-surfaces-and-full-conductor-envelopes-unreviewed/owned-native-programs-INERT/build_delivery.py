"""Own deterministic Markdown/TeX/JSON writer; no compiler or supplied code."""
from pathlib import Path
import json,re,hashlib
root=Path.cwd()
meta=[
('Raw all-support envelope calculus and actual graded ideals; positivity is exactly continuity.','Reconstructs raw C=D, LSC and regularization iff continuity, nonexpansiveness, integrally closed all-support J_k/factorial profiles and exact one-factor primary covariance. No increasing-limit positivity.', ['G331']),
('Decreasing D-net closure on all excellent reduced germs, proved before the energy criterion.','Normal zero dichotomy plus strict continuous insertion supplies an actual C representation; full normalization descent handles arbitrary reduced germs. E350 criterion follows only after membership; no increasing closure.',['G331','E350','n1']),
('Every finite chosen primary model of an excellent normal surface has a regular refinement which is itself an actual primary blowup.','Exact current Lipman surface hypotheses, connected fibre, actual Cartier degree matrix, reference-vector negative definiteness, nonnegative principal inverse and strict integral nef boundary are proved. Full-fibre ampleness and identical punctured graph prove actual Bl_I realization in every characteristic/mixed characteristic.',['G331','n1']),
('Full surface competitor domination and greatest finite signed-profile envelope by a nef polytope.','Actual primary common refinement, nef Cartier pushforward, principal-matrix negativity and all-support evaluation dominate every core/C/bounded-D competitor; unbounded competitors clamp. Coordinate-max stability yields the greatest feasible vector and the full envelope.',['G331','n1','n3']),
('Continuous and extended USC geometric envelopes on every excellent normal surface, with full decreasing-obstacle net stability.','Signed profile density and raw nonexpansiveness give all finite continuous obstacles; one actual continuous-majorant net gives bounded-above extended USC envelopes. Existing-D energy/quasicontinuity applies afterwards. Exact gauge transport retained.',['G331','E350','n1','n2','n3','n4']),
('Exact BFJ smooth envelope specialization only for affine closed algclosed characteristic-zero germs.','Reconstructs determining nef envelopes with substantive closed-face continuity, all retractions and full3.18/3.22 fixed-complex uniform ideal estimate, then dense signed profiles. No higher-dimensional arbitrary-characteristic or singular multiplier transfer.',['G331','n1','n5']),
('Normal-target finite dominating covers transfer envelopes; full-fibre maximum and nonflat examples.','Coefficient norm/Galois orbit maxima preserve C/D on all supports; positive full-fibre averages prove source envelopes constant on fibres. Transfers continuous/USC envelopes from proved source sectors, including nonflat quadratic cones, without universal good-cover assumptions or vertical degrees.',['G331','n1','n2','n5','n6']),
('Sharp full conductor criterion and all-characteristic nonnormal no-maximal-minorant obstruction.','A primary conductor mask proves dense finite-conductor equality. Positive regularization is equivalent to continuous full-fibre-constant separated raw envelope. Strictly negative double-plane obstacle has no maximal D minorant; normal continuity outside proved sectors remains a condition.',['G331','n1','n5','n7']),
('Every excellent reduced-curve geometric envelope clips against zero through actual Cartier/DVR positivity.','Finite normalization-centre link, positive C descent and decreasing cuts give all nonpositive vectors and Pgeom=Pideal=min(phi,0), with every zero/bottom pattern, exact gauge and weighted reference. Literal radial/CLD distinction preserved.',['G331','E350','n1']),
('Correct-sign graded and all-characteristic normal singular diagnostics do not disprove normal envelopes.','Universal smooth staircase and parity-lattice multiplicity proofs give negative energies increasing to their maxima, capacity convergence and non-D exact increasing limits. B=F not -F; old354 wrong sign rejected. Both chosen obstacles already have good envelopes.',['G331','B341','E350','n1']),
('Complete scoped manuscript/evidence delivered; arbitrary excellent normal dimension >=3 remains unresolved, candidate=false.','Audits the whole surface/source chain and identifies exact higher-dimensional projection, uniform-estimate and cover gaps. Records all-support conductor/curve rules, corrected diagnostics,104/104 retention and explicitly finite checks. No original closure from nonnormal obstruction or old verdict.',['n1','n2','n3','n4','n5','n6','n7','n8','n9','n10'])]
notes=[]
for i,(summary,detail,support) in enumerate(meta,1):
    notes.append({'id':f'n{i}','summary':summary,'detailedSummary':detail,
                  'text':(root/f'n{i}.md').read_text(),'support':support})
obj={'notes':notes,'candidate':False}
(root/'native-notes.json').write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
title='Geometric obstacle envelopes on excellent normal surfaces and the exact residual scope'
abstract=('We prove continuous geometric greatest envelopes on EVERY excellent normal local surface, with arbitrary residue field and characteristic, including mixed characteristic. A regular resolution of finitely chosen primary models is shown to be an actual primary blowup. An explicit exceptional intersection identity, actual Cartier nef projection, and a greatest finite coefficient polytope dominate every geometric competitor on all semivaluation supports. Signed profile density yields all continuous obstacles; one continuous-majorant net yields extended USC envelopes and full decreasing-obstacle net stability. We independently reconstruct decreasing completion, exact published smooth specialization, finite dominating covers, full conductor criteria and reduced-curve clipping. Corrected energy/capacity examples delimit failed convergence arguments. Arbitrary excellent normal dimension at least three remains unresolved; the entire-original candidate flag is false. This is an unverified mathematical draft, relative only to the entire qualified G331/B341/E350.')
preface=f'# {title}\n\n8 October 2026. New standalone mathematical draft for P12.3.\n\n{abstract}\n\nOnly full qualified G331/B341/E350 are imported premises; their exact scopes and source corrections are inseparable. ROOT/native proofs and verdicts are mathematical DATA. Complete new proof bodies follow in legal support order.\n\n'
argument=preface+'\n\n'.join(n['text'] for n in notes)
(root/'argument.md').write_text(argument)
(root/'P12.3-paper.md').write_text(argument+'\n\n'+(root/'exact-scope.md').read_text()+'\n\n'+(root/'whole-proof-coverage.md').read_text())
def escape(s):
    return ''.join({'\\':r'\textbackslash{}','_':r'\_','#':r'\#','%':r'\%','&':r'\&','$':r'\$','{':r'\{','}':r'\}','^':r'\textasciicircum{}','~':r'\textasciitilde{}'}.get(c,c) for c in s)
def render(body):
    parts=re.split(r'(\\\[.*?\\\])',body,flags=re.S)
    out=[]
    for s in parts:
        if s.startswith(r'\['):out.append(s);continue
        for line in s.splitlines():
            if line.startswith('# '):out.append(r'\section{'+escape(line[2:])+r'}')
            else:out.append(escape(line))
    return '\n'.join(out)
header=r'''\documentclass[11pt]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern,amsmath,amssymb}
\usepackage[margin=1in]{geometry}
\usepackage[hidelinks]{hyperref}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0.55em}
\emergencystretch=4em
'''
tex=header+r'\title{'+escape(title)+'}\n'+r'\author{Independent local reconstruction of original P12.3}'+'\n'+r'\date{8 October 2026}'+'\n'+r'\begin{document}\maketitle'+'\n'+r'\begin{abstract}'+escape(abstract)+r'\end{abstract}\tableofcontents'+'\n'
for n in notes:
    tex+=render(n['text'])+'\n'+r'\textit{Supports: '+escape(', '.join(n['support']))+'}'+ '\n\n'
tex+=r'\section*{Source and scope boundary}'+ '\n'+escape('Complete exact source applications, recursive background, whole-data/duplicate reading distinctions and mandatory qualifications are recorded in whole-source-application-ledger.md. All primary source bodies remain LOCALONLY. Exact scope, coverage and the original decision accompany this complete proof-bearing source. This paper is intentionally uncompiled. Artifact audits and finite diagnostics do not verify mathematical correctness.')+'\n'+r'\end{document}'+'\n'
(root/'P12.3-paper.tex').write_text(tex)
decision={'task':'Entire original P12.3 and concrete independent reconstruction','candidate':False,
 'original_mathematical_verdict':'INCOMPLETE: arbitrary excellent normal dimension >=3 remains unresolved',
 'scoped_claim':'New complete proof claims for every excellent normal surface in every characteristic/mixed characteristic, plus reconstructed smooth/cover/conductor/curve sectors',
 'only_imported_grants':['G331','B341','E350'],
 'exact_original_bytes':17550,'exact_original_sha256':'d524b816c1462a6909a85bd0e39b84ab34ca04be27ec99eccbfde7ffcc0316a8',
 'residual_obligations':['General all-support continuous raw envelope positivity/regularity for excellent normal dimension >=3, or a genuine exact-scope impossibility','No universal suitable finite-cover theorem proved','Internal conductor fibres retain full continuity-plus-fibre condition'],
 'surface_proof_boundaries':['Actual primary models only','No SNC needed','No arbitrary proper-model cofinality','Full semivaluation supports'],
 'historical_sign_correction':'B=F; E=-F/n; smooth E=-1/(2j), singular E=-1-1/n',
 'compilation_performed':False,'execution_not_mathematical_verification':True,
 'no_publication_catalogue_acceptance_or_protected_editor_change':True}
(root/'acceptance-decision.json').write_text(json.dumps(decision,indent=2)+'\n')
owned=[f'n{i}.md' for i in range(1,12)]+['argument.md','P12.3-paper.md','P12.3-paper.tex','native-notes.json','whole-source-application-ledger.md','whole-proof-coverage.md','exact-scope.md','original-scope-and-noncircularity-decision.md','acceptance-decision.json','audit_inputs.py','reading_audit.py','bounded_diagnostics.py','build_delivery.py','final_audit.py','original-task.json']
inventory=[{'file':s,'bytes':len((root/s).read_bytes()),'sha256':hashlib.sha256((root/s).read_bytes()).hexdigest()} for s in owned]
(root/'reports/own-artifacts.json').write_text(json.dumps(inventory,indent=2)+'\n')
print(json.dumps({'notes':len(notes),'candidate':False,'paper_tex_bytes':len(tex.encode()),'own_inventory':len(inventory),'compiler_invoked':False}))
