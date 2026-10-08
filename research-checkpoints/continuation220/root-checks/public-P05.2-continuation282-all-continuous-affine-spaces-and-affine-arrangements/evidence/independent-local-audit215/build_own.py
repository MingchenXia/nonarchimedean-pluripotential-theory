"""Compile only the unchanged own data copy; retain both full pass logs."""
import hashlib,json,pathlib,platform,re,subprocess,sys
OWN=pathlib.Path(__file__).resolve().parent
build=OWN/'build'; src=build/'P05.2-paper.tex'
raw=src.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='6fc295bc50870aae7d10d339da65374f79d332750e17dc31700fd70ba1676c7d'
assert not re.search(rb'\\(?:write18|input|include|openout|openin|read|immediate|directlua)\b',raw)
log_root=OWN
# A rerun uses a fresh own subdirectory and preserves the initial warning logs.
if (OWN/'build-output.json').exists():
    number=1
    while (OWN/f'build-rerun-{number:03d}').exists(): number+=1
    build=OWN/f'build-rerun-{number:03d}'; build.mkdir()
    (build/'P05.2-paper.tex').write_bytes(raw)
    log_root=build
commands=[]
for executable in ['pdflatex','pandoc']:
    p=subprocess.run([executable,'--version'],capture_output=True,text=True)
    commands.append({'argv':[executable,'--version'],'exit_code':p.returncode,'version_first_line':p.stdout.splitlines()[0]})
for i in [1,2]:
    argv=['pdflatex','-no-shell-escape','-interaction=nonstopmode','-halt-on-error','P05.2-paper.tex']
    p=subprocess.run(argv,cwd=build,capture_output=True,text=True)
    (log_root/f'own-pass{i}.stdout.log').write_text(p.stdout);(log_root/f'own-pass{i}.stderr.log').write_text(p.stderr)
    commands.append({'argv':argv,'cwd':str(build),'exit_code':p.returncode,'diagnostics':[l for l in p.stdout.splitlines() if any(x in l for x in ['Warning','Overfull','Underfull','Error','Output written'])]})
    assert p.returncode==0
argv=['pandoc','-f','latex','-t','markdown','P05.2-paper.tex','-o','argument.md']
p=subprocess.run(argv,cwd=build,capture_output=True,text=True)
(log_root/'own-pandoc.stdout.log').write_text(p.stdout);(log_root/'own-pandoc.stderr.log').write_text(p.stderr)
commands.append({'argv':argv,'cwd':str(build),'exit_code':p.returncode});assert p.returncode==0
base=pathlib.Path('/workspace/research/campaigns/round-215/P05.2-unchanged-all-continuous-affine-arrangement-independent-native-local-source-audit')
packet=json.loads((base/'mathematical-packet-bindings.json').read_text())
match=(build/'argument.md').read_bytes()==pathlib.Path(packet[23]['path']).read_bytes()
assert match
(log_root/'build-output.json').write_text(json.dumps({'commands':commands,'source_unchanged':True,'source_to_markdown_exact':match,'reverse_equivalence_claimed':False,'shell_escape':False,'python':sys.version,'platform':platform.platform(),'candidate':False},indent=2)+'\n')
print(json.dumps({'pass_exit_codes':[0,0],'source_to_markdown_exact':match,'source_unchanged':True,'final_diagnostics':commands[-2]['diagnostics']}))
