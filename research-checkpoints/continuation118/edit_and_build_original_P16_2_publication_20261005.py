from pathlib import Path
from datetime import datetime, timezone
import difflib, hashlib, json, re, subprocess

R=Path('/workspace/research')
D=R/'deliverables/original-P16.2'
p=D/'P16.2-core.md'
sha=lambda q:hashlib.sha256(Path(q).read_bytes()).hexdigest()
old=p.read_text()
assert sha(p)=='cb6ce18e033280d43690589b0b70ed99b23e2f7ca232b0bc9745a64ab59bf46b'
assert not (D/'publication-editorial-edits.json').exists()
text=old
edits=[]
def change(before,after):
    global text
    assert text.count(before)==1,(before,text.count(before))
    text=text.replace(before,after)
    edits.append({'before':before,'after':after})

change('  - \\usepackage{longtable}\n',
       '  - \\usepackage{longtable}\n  - \\usepackage{fvextra}\n  - \\DefineVerbatimEnvironment{verbatim}{Verbatim}{breaklines=true,fontsize=\\small}\n')
change('Changing the original algebraic frame adds the logarithm of an analytic\nunit.',
       'Changing the original algebraic frame subtracts the logarithm of its analytic\nunit, as in Appendix C.')
change('unique valuative extensions; they are proposals to reconstruct,\nnot grants for a nonample result.',
       'unique valuative extensions. Appendix A proves these new assertions;\nno nonample theorem is granted by that construction.')
change('This assertion is stronger than continuous-stage compatibility and\nweaker than independence of every conceivable local psh approximation.\nThe latter category must be specified and proved separately if needed;\nit cannot be silently inferred from this global-net construction.',
       'This assertion proves more than continuous-stage compatibility.\nSection 10 separately constructs and compares independently supplied\nlocal nets in the associated generated section/contact category.\nNo assertion about arbitrary unrelated classical currents is inferred.')

a=text.index('# 10. Intrinsic local products')
b=text.index('# 11. A genuinely nonprojective')
part=text[a:b]
part=re.sub(r'^## ([1-6])\.',r'## 10.\1.',part,flags=re.M)
part=part.replace('bridge of Section1','bridge of Section 10.1')
part=part.replace('local limit of Section4','local limit of Section 10.4')
part=part.replace('Section5\nconstructs their local operator','Section 10.5\nconstructs their local operator')
part=part.replace('below. No arbitrary','below. No arbitrary')
part=part.replace('In this note\nall local approximants','In this section\nall local approximants')
part=part.replace('The explicit construction at supplied-02.txt LF115-117 clears the',
                  'The explicit construction in Appendix D.4 clears the')
part=part.replace("needed in109's gate L is supplied",'needed for the intrinsic operator is supplied')
text=text[:a]+part+text[b:]
edits.append({'scope':'Section 10','change':'Number local subsections 10.1--10.6 and clarify their existing internal references.'})

for letter,next_heading in [('A','# Appendix B.'),('B','# Appendix C.'),('C','# Appendix D.')]:
    a=text.index('# Appendix '+letter+'.')
    b=text.index(next_heading)
    part=text[a:b]
    part=re.sub(r'^## ([1-4])\.',rf'## {letter}.\1.',part,flags=re.M)
    part=re.sub(r'\bSection ?([1-4])\b',rf'Appendix {letter}.\1',part)
    if letter=='B':
        part=part.replace('Sections2 and3','Appendices B.2 and B.3')
    text=text[:a]+part+text[b:]
    edits.append({'scope':'Appendix '+letter,'change':'Use letter-prefixed subsection numbering and references.'})

a=text.index('# Appendix D.')
b=text.index('# References and verification scope')
part=text[a:b]
part=part.replace('Throughout Sections 2--8,','Throughout this appendix,')
part=re.sub(r'^(##|###) ([2-5](?:\.[1-4])?)\.',r'\1 D.\2.',part,flags=re.M)
part=re.sub(r'\\tag\{([2-5]\.[1-9])\}',r'\\tag{D.\1}',part)
part=re.sub(r'\(([2-5]\.[1-9])\)',r'(D.\1)',part)
part=part.replace('Section 2','Appendix D.2').replace('Section 4','Appendix D.4')
text=text[:a]+part+text[b:]
edits.append({'scope':'Appendix D','change':'Use letter-prefixed subsection/equation numbering and local references; preserve all mathematical expressions.'})
text=text.replace('Appendix B, Sections1-4','Appendix B, Sections B.1--B.4')
p.write_text(text)
(D/'P16.2-core.publication-editorial.patch').write_text(''.join(difflib.unified_diff(
    old.splitlines(True),text.splitlines(True),fromfile='assembled/P16.2-core.md',tofile='publication/P16.2-core.md')))
record={'recorded_utc':datetime.now(timezone.utc).isoformat(),
    'pre_editorial_core_sha256':hashlib.sha256(old.encode()).hexdigest(),
    'publication_core_sha256':sha(p),'changes':edits,
    'new_mathematical_proof_imported':False,
    'full_saved_pre_editorial_core_1241_LF_root_read':True,
    'frame_sign_alignment':'The one Appendix B prose sign is aligned with the exact minus sign already proved in the reviewed Appendix C and main text.',
    'historical_frozen_sources_modified':False,
    'existing_P16_4_editor_modified_replaced_or_new_tab_opened':False}
(D/'publication-editorial-edits.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
tex=D/'P16.2-paper.tex'
assert not tex.exists()
subprocess.run(['pandoc',str(p),'--standalone','--from=markdown+tex_math_dollars',
    '--to=latex','--pdf-engine=xelatex','--output',str(tex)],check=True,capture_output=True,text=True)
print(json.dumps({'core':str(p),'core_sha256':sha(p),'tex':str(tex),'tex_sha256':sha(tex),
    'native_compile_pending':True,'local_PDF_export_pending':True,'original_count_incremented':False},indent=2))
