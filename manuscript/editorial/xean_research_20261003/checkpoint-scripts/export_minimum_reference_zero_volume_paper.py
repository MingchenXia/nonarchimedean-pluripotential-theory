"""Export local PDFs with native editor status recorded separately."""
from pathlib import Path
import datetime, hashlib, json, re, shutil, subprocess, sys

root = Path('/workspace/research')
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
number = int(sys.argv[1])
assert number in (31, 32)
stem = 'P15.1-minimum-reference-finite-energy' if number == 31 else 'P15.2-minimum-reference-full-mass-operator'
output = root / 'deliverables' / f'round-{number}'
source = output / (stem + '.tex')
request = json.loads((root / 'deliverables' / f'round-{number}-native-request-status.json').read_text())
assert request['source_sha256'] == sha(source)
original = sha(source)
build = output / 'export-build'
build.mkdir(exist_ok=False)
runs = []
for pass_number in (1, 2):
    command = ['pdflatex', '-interaction=nonstopmode', '-halt-on-error', '-file-line-error',
               '-output-directory=' + str(build), source.name]
    process = subprocess.run(command, cwd=output, capture_output=True, text=True)
    (build / f'pass-{pass_number}.stdout.txt').write_text(process.stdout)
    (build / f'pass-{pass_number}.stderr.txt').write_text(process.stderr)
    runs.append({'command': command, 'exit_code': process.returncode})
    assert process.returncode == 0, process.stderr + process.stdout[-2000:]
pdf = source.with_suffix('.pdf')
shutil.copyfile(build / pdf.name, pdf)
log = (build / source.with_suffix('.log').name).read_text()
notices = {key: [line for line in log.split('\n') if key in line]
           for key in ['Overfull', 'Underfull', 'Missing character', 'undefined', 'Warning']}
info = subprocess.run(['pdfinfo', str(pdf)], capture_output=True, text=True, check=True).stdout
(build / 'pdfinfo.txt').write_text(info)
pages = int(re.search(r'Pages:\s+(\d+)', info).group(1))
subprocess.run(['pdftoppm', '-f', '1', '-singlefile', '-scale-to', '1700', '-png',
                str(pdf), str(output / 'first-page')], check=True, capture_output=True)
record = {'exported_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'source': str(source), 'source_sha256': sha(source), 'source_changed': sha(source) != original,
          'pdf': str(pdf), 'pdf_sha256': sha(pdf), 'pages': pages, 'runs': runs,
          'final_notices': notices, 'native_compilation_already_successful': False,
          'native_request_status': request, 'native_verification_pending': True,
          'native_tool_returned_exported_pdf': False}
path = output / 'export-evidence.json'
assert not path.exists()
path.write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
