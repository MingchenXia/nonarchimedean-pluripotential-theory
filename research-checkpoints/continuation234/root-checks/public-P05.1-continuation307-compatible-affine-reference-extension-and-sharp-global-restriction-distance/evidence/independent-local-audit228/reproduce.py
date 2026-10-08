"""Own bounded reproduction. Never runs any bound build/conversion/audit helper."""
import pathlib,json,hashlib,subprocess,sys,platform,re
BASE=pathlib.Path('/workspace/research/campaigns/round-228/P05.1-compatible-affine-reference-extension-and-sharp-distance-independent-whole-source-audit')
ROOT=pathlib.Path(__file__).resolve().parent
def packet(n): return json.loads((BASE/n).read_bytes())
M=packet('mathematical-packet-bindings.json'); E=packet('historical-own-evidence-bindings.json')
def raw(entry): return pathlib.Path(entry['path']).read_bytes()
def sha(b): return hashlib.sha256(b).hexdigest()
def save(name,data): (ROOT/name).write_text(json.dumps(data,indent=2)+'\n')
def checker():
    d=ROOT/'finite-check';d.mkdir(exist_ok=True)
    marker=d/'execution-started.json'
    if marker.exists(): raise RuntimeError('EXECONCE guard: checker was already started')
    code=raw(E[45]);inp=raw(E[40])
    assert len(code)==5091 and len(inp)==281
    assert code==raw(E[2]) and inp==raw(E[3])
    (d/'exact_checks.py').write_bytes(code);(d/'certificate-input.json').write_bytes(inp)
    marker.write_text(json.dumps({'code_sha256':sha(code),'input_sha256':sha(inp),'inspection':'whole 121 LF source lines and 9 LF input lines displayed before this copy','argv':[sys.executable,'exact_checks.py']},indent=2)+'\n')
    p=subprocess.run([sys.executable,'exact_checks.py'],cwd=d,capture_output=True,timeout=20)
    (d/'stdout.json').write_bytes(p.stdout);(d/'stderr.txt').write_bytes(p.stderr)
    report={'exit_code':p.returncode,'executions_this_audit':1,'python':sys.version,'platform':platform.platform()}
    if p.returncode==0:
        out=(d/'exact-output.json').read_bytes()
        report.update(output_exact_ROOT=out==raw(E[44]),output_exact_author=out==raw(E[4]),stdout_exact_ROOT=p.stdout==raw(E[43]),stdout_exact_author=p.stdout==raw(E[5]),output_sha256=sha(out),total_assertions=json.loads(out)['total_assertions'],diagnostic_cost=json.loads(out)['diagnostic_cost'])
    save('finite-check-report.json',report);print(json.dumps(report,indent=2))
def build():
    d=ROOT/'fresh-build';d.mkdir(exist_ok=True)
    if (d/'build-report.json').exists(): raise RuntimeError('build already recorded')
    b=raw(M[4]);(d/'P05.1-paper.tex').write_bytes(b)
    # The entire source was displayed before execution. This is an extra finite lexical check.
    dangerous=re.findall(rb'\\(?:write18|immediate|openout|input|include|read|write|catcode|directlua)\b',b)
    assert not dangerous,dangerous
    argv=['pdflatex','-no-shell-escape','-interaction=nonstopmode','-halt-on-error','-output-directory=build','P05.1-paper.tex']
    (d/'build').mkdir(exist_ok=True)
    report={'argv':argv,'source_sha256_before':sha(b),'dangerous_direct_controls':[],'engine':subprocess.run(['pdflatex','--version'],capture_output=True,text=True).stdout.split('\n')[0],'python':sys.version,'platform':platform.platform(),'passes':[]}
    for i in [1,2]:
        p=subprocess.run(argv,cwd=d,capture_output=True,timeout=30)
        (d/f'pass-{i}.stdout.log').write_bytes(p.stdout);(d/f'pass-{i}.stderr.log').write_bytes(p.stderr)
        log=d/'build/P05.1-paper.log'
        if log.exists(): (d/f'pass-{i}.tex.log').write_bytes(log.read_bytes())
        warnings=[s for s in p.stdout.decode(errors='replace').split('\n') if 'Warning' in s or 'Overfull' in s or 'Underfull' in s]
        report['passes'].append({'pass':i,'exit_code':p.returncode,'warnings':warnings})
        if p.returncode: break
    report['source_sha256_after']=sha((d/'P05.1-paper.tex').read_bytes());report['immutable_source_sha256_after']=sha(raw(M[4]))
    pdf=d/'build/P05.1-paper.pdf'
    if pdf.exists():
        info=subprocess.run(['pdfinfo',str(pdf)],capture_output=True,text=True)
        (d/'pdfinfo.txt').write_text(info.stdout)
        report['pdf_sha256']=sha(pdf.read_bytes());report['pages']=int(re.search(r'^Pages:\s+(\d+)',info.stdout,re.M)[1])
    (d/'build-report.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
def presentation():
    b=raw(M[4]);s=b.decode();s=s[s.index('\\begin{abstract}')+len('\\begin{abstract}'):s.index('\\begin{thebibliography}')]
    s=s.replace('\\end{abstract}','\n')
    s=re.sub(r'\\section\{([^{}]*)\}',lambda m:'\n## '+m[1]+'\n',s)
    s=re.sub(r'\\label\{([^{}]*)\}',lambda m:' <a id=\\"'+m[1]+'\\"></a>',s)
    s=re.sub(r'\\ref\{([^{}]*)\}',lambda m:'['+m[1]+'](#'+m[1]+')',s)
    s=re.sub(r'\\begin\{(theorem|lemma|proposition)\}(?:\[([^\]]*)\])?',lambda m:'\n**'+m[1].title()+(': '+m[2] if m[2] else '')+'.** ',s)
    s=re.sub(r'\\end\{(theorem|lemma|proposition)\}','\n',s)
    table={'\\begin{proof}':'\n**Proof.** ','\\end{proof}':' ∎\n','\\begin{align*}':'$$\n\\begin{aligned}','\\end{align*}':'\\end{aligned}\n$$','\\[':'$$','\\]':'$$'}
    for a,z in table.items():s=s.replace(a,z)
    table={'R':'mathbb{R}','Q':'mathbb{Q}','Z':'mathbb{Z}','PA':'mathrm{PA}','PC':'mathrm{PC}'}
    for a,z in table.items():s=re.sub(r'\\'+a+r'(?![A-Za-z])',lambda m,z=z:'\\'+z,s)
    for name in ['conv','cone','epi','rec','aff','ri','dist']:
        z='relint' if name=='ri' else name
        s=re.sub(r'\\'+name+r'(?![A-Za-z])',lambda m,z=z:'\\operatorname{'+z+'}',s)
    s=re.sub(r'\\emph\{([^{}]*)\}',lambda m:'*'+m[1]+'*',s)
    s=re.sub(r'\\texttt\{([^{}]*)\}',lambda m:'`'+m[1].replace('\\_','_')+'`',s)
    s=s.replace('~',' ').replace('--','–')
    header='# Compatible references and sharp uniform restriction obstruction\n\nOwn source-derived proof manuscript. Unreviewed; original P05.1/P05.2 remain OPEN; candidate=false.\n\nDerived from `P05.1-paper.tex`, SHA256 `'+sha(b)+'`, by `python3 make_argument.py`. All theorem/proof prose and mathematical displays in the body are retained. Markdown conversion is presentation, not an independent correctness certificate.\n\n'
    got=(header+s.strip()+'\n').encode();(ROOT/'own-derived-argument.md').write_bytes(got)
    saved=raw(E[10]);actual=raw(M[8])
    report={'source_to_body_only':True,'excludes':['preamble','bibliography'],'preserves_literal_anchor_quote_escapes':True,'exact_markdown_match':got==raw(M[5]),'exact_ROOT_markdown_match':got==raw(E[41]),'output_sha256':sha(got),'actual_FINAL_notes':len(json.loads(actual)['notes']),'saved_FINAL_exact_plus_one_LF':saved==actual+b'\n','source_unchanged':sha(raw(M[4]))==sha(b)}
    save('presentation-and-FINAL-report.json',report);print(json.dumps(report,indent=2))
if __name__=='__main__': {'check':checker,'build':build,'presentation':presentation}[sys.argv[1]]()
