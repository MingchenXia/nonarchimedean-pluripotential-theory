"""Run only the freshly owned local readers, diagnostics and source generator."""
import pathlib,subprocess,json,datetime
P=pathlib.Path.cwd();commands=[]
for name in ['audit_inputs.py','audit_review.py','finite_diagnostics.py','generate_delivery.py','final_audit.py']:
    cmd=['python',name]
    r=subprocess.run(cmd,cwd=P,capture_output=True,text=True)
    commands.append({'argv':cmd,'exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr})
    if r.returncode:break
(P/'evidence/commands.json').write_text(json.dumps({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'commands':commands,'supplied_executables_used':False,'compilation':False,
 'pixel_read_command':'pdftoppm -f 370 -singlefile -scale-to 1800 -png inputs/primary-LOCALONLY/04-Swanson-Huneke-author-book.pdf evidence/source-pixels-LOCALONLY/SH-printed356'},indent=2))
assert len(commands)==5 and all(r['exit_code']==0 for r in commands)
# Refresh hashes after preserving exact command output; the audit outputs exclude themselves.
r=subprocess.run(['python','final_audit.py'],cwd=P,capture_output=True,text=True,check=True)
print(json.dumps({'status':'PASS reproducibility only','owned_commands':len(commands),
 'final_artifact_audit':json.loads(r.stdout),'supplied_code_executed':False,'compiler_run':False},indent=2))
