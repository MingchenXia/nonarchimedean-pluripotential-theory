#!/usr/bin/env python3
"""Rebuild local deliverables using existing tools, without installation."""
from pathlib import Path
import subprocess, json, hashlib, platform, shutil, sys, datetime

ROOT = Path(__file__).resolve().parent


def main():
    records = []
    commands = [
        [sys.executable, 'checks.py'],
        ['pandoc', 'P16.4-argument.md', '--standalone', '--from=markdown+tex_math_single_backslash',
         '--to=latex', '--include-in-header=latex-header.tex', '-o', 'P16.4-paper.tex'],
        ['pdflatex', '-no-shell-escape', '-interaction=nonstopmode',
         '-halt-on-error', 'P16.4-paper.tex'],
        ['pdflatex', '-no-shell-escape', '-interaction=nonstopmode',
         '-halt-on-error', 'P16.4-paper.tex']]
    for index, cmd in enumerate(commands, 1):
        binary = shutil.which(cmd[0])
        if binary is None:
            records.append({'argv': cmd, 'status': 'missing existing tool'})
            break
        run = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
        out, err = f'build-{index:02d}.stdout.txt', f'build-{index:02d}.stderr.txt'
        (ROOT / out).write_text(run.stdout)
        (ROOT / err).write_text(run.stderr)
        records.append({'argv': cmd, 'returncode': run.returncode, 'stdout': out, 'stderr': err})
        print(json.dumps(records[-1]))
        if run.returncode:
            break
    env = {'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
           'platform': platform.platform(), 'python': sys.version,
           'cwd': str(ROOT), 'tools': {t: shutil.which(t) for t in
                                     ['python3', 'pandoc', 'pdflatex', 'pdftotext', 'curl']},
           'model_identity': 'not independently exposed by the local runtime',
           'supervised_compute_facility': 'none exposed; no heavy compute used',
           'protected_editor': 'not accessed; no editor operation performed',
           'runtime_configuration_changed': False, 'commands': records,
           'candidate': False, 'mathematical_certification': False}
    (ROOT / 'environment-and-build.json').write_text(json.dumps(env, indent=2) + '\n')
    paths = [p for p in ROOT.rglob('*') if p.is_file() and
             p.suffix in {'.py', '.json', '.md', '.tex', '.pdf', '.txt'} and
             p.name != 'artifact-hashes.json']
    hashes = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
              for p in sorted(paths)}
    (ROOT / 'artifact-hashes.json').write_text(json.dumps(hashes, indent=2) + '\n')


if __name__ == '__main__':
    main()
