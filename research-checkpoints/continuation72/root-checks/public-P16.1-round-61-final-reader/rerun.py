from pathlib import Path
import subprocess
import sys

r=Path(__file__).resolve().parent
for script in ['environment.py','prepare_provenance.py','algebra_checks.py','build.py','write_notes.py','verify.py','write_notes.py']:
    p=subprocess.run([sys.executable,script],cwd=r,capture_output=True)
    (r/f'{script}.stdout.txt').write_bytes(p.stdout)
    (r/f'{script}.stderr.txt').write_bytes(p.stderr)
    print(p.stdout.decode(),end='')
    if p.returncode:
        print(p.stderr.decode(),end='')
        raise SystemExit(p.returncode)
