"""Owned comparisons of explicitly supplied historical bytes, no execution."""
import pathlib,json,hashlib,re,difflib
from review_data import BASE,OUT,digest
DATA=BASE/'immutable-mathematical-DATA'
def check_row(row,pathkey='path'):
    p=pathlib.Path(row[pathkey]);d={'path':str(p)}
    if 'round-250' in str(p) or 'P12.5' in str(p):return dict(d,status='excluded_active_or_wrong_atom')
    if not p.is_file():return dict(d,status='unavailable')
    z=digest(p);return dict(z,status='match' if z['bytes']==row['bytes'] and z['sha256']==row['sha256'] else 'mismatch')
def main():
    native=(DATA/'05-native-origin-P12.4-paper.tex').read_text()
    reader=(DATA/'06-P12.4-paper.tex').read_text()
    font_old='\\usepackage[T1]{fontenc}'
    font_new='\\usepackage{fontspec}\n\\setmainfont{DejaVu Serif}\n\\setmonofont{DejaVu Sans Mono}'
    inlined=native
    comps=[]
    for f in ['00-P12.2-paper.tex','01-mandatory-source-scope-and-reader-qualifications-after-review240-20261008.json','02-source-application-ledger.md','03-exact-scope.md']:
        b=(DATA/f).read_text()
        target='\\VerbatimInput[breaklines,fontsize=\\tiny]{attachments/'+f+'}'
        replacement='\\begin{Verbatim}[breaklines,fontsize=\\tiny]\n'+b.rstrip('\n')+'\n\\end{Verbatim}'
        inlined=inlined.replace(target,replacement)
        comps.append({'file':f,'exact_in_reader':b.rstrip('\n') in reader,'font_transformed_in_reader':b.replace(font_old,font_new).rstrip('\n') in reader})
    reconstructed=inlined.replace(font_old,font_new)
    diff=list(difflib.unified_diff(reconstructed.splitlines(),reader.splitlines(),fromfile='independently_reconstructed',tofile='reader',lineterm=''))
    (OUT/'evidence'/'reader-diff.txt').write_text('\n'.join(diff)+'\n')
    meta={'font_occurrences_native':native.count(font_old),'font_occurrences_inlined':inlined.count(font_old),'reader_reconstructed_exact':reconstructed==reader,'components':comps,'line_diff':diff}
    (OUT/'evidence'/'reader-comparison.json').write_text(json.dumps(meta,indent=2)+'\n')
    hist=json.loads((DATA/'13-ROOT-whole-reading-and-binding-20261008.json').read_text())
    own=[check_row(r) for r in hist['own15_current_physical_checks']]
    old=json.loads((DATA/'evidence-input-audit.json').read_text())['files']
    inputs=[]
    for r in old:
        item={'origin':check_row(r)}
        rr=dict(r,path=r['local_path']);rr['sha256']=r['local_sha256']
        item['author_local_copy']=check_row(rr);inputs.append(item)
    proofs=[check_row(dict(r,path=str(DATA/(str(17+int(r['id'][1:])).zfill(2)+'-'+r['id']+'.tex')))) for r in json.loads((DATA/'evidence-final-audit.json').read_text())['proofs']]
    exact=json.loads((DATA/'14-ROOT-exact-original-task.json').read_text())
    augmented=json.loads((DATA/'17-original-task.json').read_text())
    orig=(DATA/'15-original-task-statement.txt').read_text();aug=(DATA/'16-augmented-assignment.txt').read_text()
    binding={'exact_original_problem_matches_statement':exact['problem'].rstrip()==orig.rstrip(),'augmented_problem_reconstructed':augmented['problem'].rstrip()==(orig+aug).rstrip(),'exact_problem_prefix_of_augmented':augmented['problem'].startswith(exact['problem']),'criteria_exact_prefix':augmented['completionCriteria'].startswith(exact['completionCriteria'])}
    f=json.loads((DATA/'12-actual-native-FINAL.json').read_text());e=json.loads((DATA/'11-native-notes.json').read_text())
    body=[{'id':a['id'],'actual_text_bytes':len(a['text'].encode()),'expanded_text_bytes':len(b['text'].encode()),'text_identical':a['text']==b['text'],'expanded_matches_tex':b['text']==(DATA/f'{17+int(a["id"][1:]):02d}-{a["id"]}.tex').read_text()} for a,b in zip(f['notes'],e['notes'])]
    report={'own15':own,'historical54':inputs,'expanded9':proofs,'task_binding':binding,'actual_final_count':len(f['notes']),'actual_vs_expanded':body}
    (OUT/'evidence'/'historical-recheck.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'reader':meta,'own15':{s:sum(x['status']==s for x in own) for s in ['match','mismatch','unavailable']},'input54_origins':{s:sum(x['origin']['status']==s for x in inputs) for s in ['match','mismatch','unavailable']},'input54_local':{s:sum(x['author_local_copy']['status']==s for x in inputs) for s in ['match','mismatch','unavailable']},'task':binding},indent=2))
if __name__=='__main__':main()
