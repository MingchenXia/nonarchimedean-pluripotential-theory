#!/usr/bin/env python3
"""Owned standard-library builder. Supplied files are copied as DATA only."""
import hashlib, json, re
from pathlib import Path
HERE=Path(__file__).resolve().parent
whole=(HERE/'whole-proof.md').read_text()
parts=re.split(r'^## n(\d+)\. (.+)\n',whole,flags=re.M)
summaries=[
 'Algebraic kernel passes: all product/power laws, primary integral-closure invariance and mixed monotonicity via simultaneous superficial elements in the SAME quotients; arbitrary residue fields and embedded/nonpure conventions retained.',
 'All-support FUNCTION-dependent rational moment tests are well-defined and positive; compact-Hausdorff Riesz gives a unique positive Radon measure, with exact n-1 arity and reference mass.',
 'Full C extension by uniform rational approximation, negative-constant shift estimate and bounded masses; weak uniform-input continuity proved without singular multiplier approximation.',
 'Every bounded actual decreasing representation gives the same measure; actual bounded decreasing D-net weak continuity proved when the specified limit lies in D, with no nested-net flattening or increasing D closure.',
 'One-factor primary-gauge covariance and finite-normalization top-dimensional residue-degree weights proved, with full conductor fibres and explicit d0/d1/unit/zero and reduction conventions.',
 'Exact published smooth BFJ OPERATOR specialization proved on all semivaluations, only for smooth affine CLOSED algebraically closed characteristic-zero germs; BFJ4.4 is confined to its multiplier-valid scope.',
 'Algebraic supporting theorem passes, but singular Cartier intersection comparison and open-agreement locality remain separately unresolved. Original P12.4 and other family operators are not solved; candidate=false.',
 'All requested deliverables and unchanged complete G331 supplied; 31 bound hashes matched and bounded finite diagnostics retained, including the failed early-window attempt. No supplied code, agents, native246 inspection or compilation.'
]
details=[
 'Degree-n primary length convention on R=A_red. Power/product substitution includes unused labels; closure invariance is equality of leading forms from finite Rees-module exponent errors. Mixed inclusion monotonicity uses the identical superficial quotient for both families down to dimension one, after exact R(z) length/dimension transfer. Embedded quotients are controlled by finite stabilized annihilator lengths. No coefficient-sign shortcut is used.',
 'Scaled equal ideal profiles on the whole boundary imply equal integral closures. Cross-product relations make the rational ideal-difference functional independent of every representative; monotonicity gives positivity, constants give the sup-norm bound, and rational density plus real extension give Riesz at compact Hausdorff hypotheses. This proves model-function independence, not general geometric intersection comparison.',
 'For inputs in [-M,0], moments against v(J) are at most M^p e(a,...,a,J); perturbations by epsilon have error at most ((M+epsilon)^p-M^p) times that reference mixed multiplicity. Limits are independent of uniform approximation and yield weak continuity via dense tests and bounded masses. No total-variation continuity is claimed.',
 'Scalar ideal moments increase along finite products of actual C representations. Compact directed open covers compare two representations up to negative shifts and prove the C-majorant supremum formula. D addition/order/shift laws are proved before the decreasing-D-net step, whose usc open covers give weak convergence. Membership of the prescribed limit in D is assumed.',
 'Gauge transport divides each homogeneous input by d=v_a(b), while the measure is T_*(d mu_a). Artin--Rees shows normalization preserves degree-n forms; Artinian composition factors give finite closed residue-field degrees and only dim n centers contribute. Curve mass is sum f_q ord_q(a), with no potential slot. Empty d0 is separate. Nilpotent intersection lengths are explicitly unclaimed.',
 'Fresh complete BFJ Section4 source applications identify rational moments in its regular/Cohen--Macaulay setting, extend through C using its smooth pairing laws, and through arbitrary actual D-nets using 4.4 upper semicontinuity plus order. Its multiplier dependency is disclosed. The incoming G331 cone specialization and the new operator equality retain all semivaluations and exact published scope.',
 'No theorem identifies these general-ring moments with actual real Cartier intersections on every primary model, nor proves equality of restricted measures on open agreement regions. Those omissions prevent original P12.4 closure. Curve zero-arity locality is vacuous, and the smooth source does not fill the singular gap. P12.3 envelopes, P12.5 energy and P12.6 full operator functoriality remain separate.',
 'Fresh artifacts include the full-proof TeX, separate review/source/coverage/scope files, decision and full native notes. The finite diagnostics passed 324 inclusions, 243 powers, 729 products, 49 sign samples and 3 gauges on the explicitly bounded domain; one early Hilbert-window failure is preserved. Hashes, finite diagnostics and artifact checks are not mathematical proof. Compilation and final acceptance belong to ROOT.'
]
notes=[]
for i in range(1,len(parts),3):
    number=int(parts[i]); title=parts[i+1]; body=parts[i+2].strip()
    match=re.match(r'\*\*Support: (.+?)\.\*\*',body)
    assert match,number
    support=[x.strip() for x in match.group(1).split(',')]
    body=body[match.end():].strip()
    notes.append({'id':'n'+str(number),'summary':summaries[number-1],'detailedSummary':details[number-1],'text':title+'\n\n'+body,'support':support})
native={'notes':notes,'candidate':False}
(HERE/'native-notes.json').write_text(json.dumps(native,indent=2,ensure_ascii=False)+'\n')

def escape(text):
    table={'\\':r'\textbackslash{}','&':r'\&','%':r'\%','$':r'\$','#':r'\#','_':r'\_','{':r'\{','}':r'\}','~':r'\textasciitilde{}','^':r'\textasciicircum{}'}
    return ''.join(table.get(c,c) for c in text)

def render(markdown):
    paragraphs=[]
    for block in re.split(r'\n\s*\n',markdown.strip()):
        if block.startswith('    '):
            formula='\n'.join(line[4:] if line.startswith('    ') else line for line in block.splitlines())
            paragraphs.append('\\begin{Verbatim}[fontsize=\\small,breaklines=true,breakanywhere=true]\n'+formula+'\n\\end{Verbatim}')
        else:
            clean=re.sub(r'\*\*(.*?)\*\*',r'\1',block)
            paragraphs.append(escape(clean))
    return '\n\n'.join(paragraphs)+'\n'

paper=(HERE/'paper-intro.tex').read_text()
for note in notes:
    title,body=note['text'].split('\n\n',1)
    paper+='\\section{'+escape(note['id']+'. '+title)+'}\n'
    paper+='\\textit{Declared supports: '+escape(', '.join(note['support']))+'.}\n\n'
    paper+=render(body)+'\n'
paper+='\\appendix\n\\section{Unchanged complete qualified incoming G331}\n'
paper+='The following are literal supplied DATA, preserved byte-for-byte within each block. They are the sole incoming grant together with all its qualifications. No executable therein was run.\n'
for source in sorted((HERE/'inputs/G331').iterdir()):
    if source.name.endswith(('.tex','.md','.json')):
        raw=source.read_text()
        assert '\\end{Verbatim}' not in raw
        paper+='\\subsection{'+escape(source.name)+'}\n'
        paper+='\\begin{Verbatim}[fontsize=\\tiny,breaklines=true,breakanywhere=true]\n'
        paper+=raw
        if not raw.endswith('\n'):
            paper+='\n'
        paper+='\\end{Verbatim}\n'
paper+='\\section{Fresh source-application ledger}\n'
paper+='\\begin{Verbatim}[fontsize=\\small,breaklines=true,breakanywhere=true]\n'
paper+=(HERE/'whole-source-application-ledger.md').read_text()
paper+='\\end{Verbatim}\n\\end{document}\n'
(HERE/'P12.4-bounded-moment-paper.tex').write_text(paper)

decision={'review_status':'Unverified independent reviewer draft; ROOT controls final acceptance',
 'assignment_deliverables_produced':True,'candidate':False,'original_P12_4_complete':False,
 'algebraic_supporting_theorem':'PASS at the exact hypotheses and reduction convention',
 'incoming_correctness_grants':['ENTIRE unchanged qualified G331'],
 'ROOT338_ROOT339_correctness_grants':False,
 'separate_judgments':{'algebraic_kernel':'PASS','all_support_function_dependence_and_positive_tests':'PASS','Riesz':'PASS','bounded_uniform_C':'PASS','every_actual_decreasing_representation':'PASS','actual_decreasing_D_net':'PASS provided prescribed limit is in D','gauge':'PASS one factor','normalization':'PASS top-dimensional closed residue-field weights','smooth_specialization':'PASS only exact published BFJ scope','actual_singular_Cartier_intersection_comparison':'UNRESOLVED','open_agreement_locality_dimension_at_least_two':'UNRESOLVED; no counterexample claimed'},
 'family':{'P12.2':'sole qualified incoming grant','P12.3':'not proved','P12.4':'incomplete','P12.5':'not proved','P12.6':'normalization algebraic formula only; full geometric operators not proved'},
 'nilpotent_intersection_lengths_claimed':False,'arbitrary_model_cofinality_claimed':False,
 'supplied_programs_executed_or_imported':False,'agents_or_native_jobs':0,
 'native246_or_unbound_campaign_outputs_inspected':False,'compilation_performed':False,
 'catalogue_counts_GitHub_editor_credentials_runtime_mutated':False,
 'evidence_not_mathematical_proof':['hashes','finite diagnostics','artifact support/inclusion checks','any later compilation'],
 'failed_owned_diagnostic_retained':True,'supervised_heavy_compute':'No service exposed; not needed',
 'supporting_paper':'P12.4-bounded-moment-paper.tex','full_notes':'native-notes.json'}
(HERE/'acceptance-decision.json').write_text(json.dumps(decision,indent=2)+'\n')
own=[]
for file in sorted(HERE.rglob('*')):
    if file.is_file() and 'inputs' not in file.relative_to(HERE).parts and file.name not in ('input.json','own-artifact-hashes.json','final-audit.json'):
        raw=file.read_bytes()
        own.append({'path':str(file.relative_to(HERE)),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
(HERE/'evidence/own-artifact-hashes.json').write_text(json.dumps(own,indent=2)+'\n')
print(json.dumps({'notes':len(notes),'candidate':False,'tex_bytes':len(paper.encode()),'unchanged_G331_files_appended':5,'compilation':False}))
