"""Prepare bounded authentic source evidence without changing any live campaign."""
from pathlib import Path
import datetime,hashlib,json,re

root=Path('/workspace/research');auth=root/'shared-sources/curve-source-authentication-20261004'
out=root/'P06.2-curve-two-sign-primary-source-repair-evidence.md'
assert not out.exists()
report=json.loads((root/'campaigns/round-16/P06.2-curve-two-sign-regularization-review/run.json').read_text())['campaign']['result']['report']
meta=json.loads((auth/'root-source-authentication.json').read_text())
sections=[r'''# Fresh source and scope evidence for a new curve-regularization repair

This is fallible research evidence, not an accepted theorem or alteration
of the old review. Original P06.2 remains open. The earlier source-dependent
INCONCLUSIVE23/19 remains governing its unrepaired draft. The proposed new
target is first-stage ordinary two-sign regularization AFTER completed
algebraic closure, on actual pure curves, and its harmonic-normalization
supporting implication. No general analytic-extension transport is thereby
claimed. Every load-bearing application needs independent reconstruction.

## Fresh official authentication

The official HAL API and thesis HTML identify Amaury Thuillier, the stated
thesis, production13October2005, submission16November2005 and controlling
v1. The officially identified unversioned document was freshly retrieved
and is BYTE-IDENTICAL to the controlling cached v1 PDF. The official HTML
also identifies the direct file URL
https://theses.hal.science/tel-00010990v1/file/tel-00010990.pdf.
The exact metadata and retrieval binding follow. These are source-access
and identity facts, rather than grants of correctness.

Numdam's official publication page identifies Berkovich's article,
IHES78(1993),5--161, DOI10.1007/BF02712916, with PDF URL
https://www.numdam.org/item/10.1007/BF02712916.pdf. Its full cached PDF
is19MB and exceeded an earlier review tool's fetch size. Complete required
selected statements/proofs therefore need to be directly available in the
argument, with exact citation and application checks. Publication metadata
alone does not prove the analytic-domain theorem.

''',json.dumps(meta,ensure_ascii=False,indent=2),r'''

## Scope correction for algebraization

Van der Put explicitly assumes an algebraically closed ground field.
Its theorem is valid input for smooth curve domains over C=completed
algebraic closure, where it is actually needed. Do not infer finite-separable
algebraization over arbitrary K without a new proof. The broader printed
Thuillier2.3.8 may be quoted accurately, but this repair needs only its
algebraically closed application.

''']
origins=[]
def excerpt(path,start,end,label):
    text=path.read_text()
    starts=list(re.finditer(start,text,re.M));assert len(starts)==1,(label,len(starts))
    begin=starts[0].start();stop=re.search(end,text[starts[0].end():],re.M);assert stop,label
    finish=starts[0].end()+stop.start();body=text[begin:finish]
    sections.append('## '+label+'\n\n```text\n'+body.replace('\f','\n').rstrip()+'\n```\n\n')
    origins.append({'label':label,'source':str(path),'source_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
                    'first_line':text[:begin].count('\n')+1,'last_line':text[:finish].count('\n'),
                    'start_pattern':start,'end_pattern':end,'body_sha256':hashlib.sha256(body.encode()).hexdigest(),
                    'complete_selected_unit':True})
excerpt(root/'shared-sources/van-der-Put-AIF-1980-30-4-155.txt',
        r'^    The field k is supposed',r'^     Proof\. — Y is called',
        'Van der Put field convention and Theorem1.1 statement')
excerpt(root/'shared-sources/Berkovich-PMIHES-1993-78-5.txt',
        r'^1\.6\. Connection with rigid analytic geometry',r'^\s*§ 2\. Local rings',
        'Berkovich1.6.1 and1.6.2: whole selected domain-comparison proofs')
sections.append(r'''## Semistable projective-curve input and affinoid realization

The relevant published projective-curve theorem is Bosch--Lütkebohmert,
Stable Reduction and Uniformization of Abelian Varieties I,
Math.Ann.270(1985),349--379, Theorem7.1, DOI10.1007/BF01473432.
The authentic public GDZ scan is retained locally with the root source check.
Its title/authors and Theorem7.1 statement were visually checked on printed
page374. The root-verified statement, paraphrased, is: a smooth geometrically
connected projective curve over a complete nontrivially valued field has
potential stable reduction in genus at least two and potential semistable
reduction in genus at most one. The actual application here is over
algebraically closed C. Keep the full archival scan/OCR local; include the
citation, limited relevant statement quotation and own application reasoning.

Fundamental published source-internal references remain normal primary
references. Each claimed new supporting lemma and every application must
nevertheless be proved or explicitly left unresolved. The controlling
Thuillier PDF printed pages53--54 were previously visually checked and
transcribed; complete selected extracted proof units follow.

''')
excerpt(root/'shared-sources/Thuillier-tel-00010990v1.txt',
        r'^Théorème 2\.3\.8\.',r'^Lemme 2\.3\.10\.',
        'Thuillier2.3.8 and2.3.9: complete selected statement/proof units')
sections.extend(['## Earlier review retained without override\n\n',report,r'''

## Remaining concrete obligations

Read the incomplete round17 recognition-source-proof repair and all five
CANONICAL notes as fallible evidence. Reconstruct every needed strict-affinoid,
algebraization/domain/semistable/local-tree/whole-annulus/Dirichlet/slope fact
under its actual C-field application. Distinguish an authentic published
analytic foundation from a new lemma or an extension of its hypotheses.
The authoritative argument must directly include every essential selected
primary body and every new supporting proof, because review has no filesystem
tools. Source authentication does not replace judgment of an application.
Any missing indispensable mathematical obligation leaves the new theorem
incomplete.

Apply the earlier review's harmless Wanner domain/error corrections and
actual excluded Shilov-boundary convention in a FRESH proof. Preserve all
old artifacts. Ordinary smooth psh sequences on one FIXED compact strict
neighborhood for both signs require all residual-direction caps and annular
gluing steps, uniform accuracy and monotone tail shifts. No GJR iterated-LFS
shortcut or weak-smoothness substitution is permitted. A previously claimed
appendix truncation marker was not confirmed by the root's literal search;
preserve the INCONCLUSIVE review and resolve actual body/end/access
obligations rather than treating this discrepancy as a PASS.

'''])
out.write_text(''.join(sections))
manifest={'prepared_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'path':str(out),
          'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'source_units':origins,
          'no_live_campaign_input_changed':True,'no_new_theorem_accepted':True}
(auth/'repair-evidence-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'bytes':out.stat().st_size,'sha256':manifest['sha256'],'selected_source_units':len(origins)}))
