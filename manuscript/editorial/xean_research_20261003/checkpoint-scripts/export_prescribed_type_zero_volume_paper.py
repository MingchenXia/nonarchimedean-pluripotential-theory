"""Export PDFs from unchanged, successfully native-compiled sources."""
from pathlib import Path
import datetime
import hashlib
import json
import re
import shutil
import subprocess
import sys

root = Path('/workspace/research')
sha = lambda path: hashlib.sha256(Path(path).read_bytes()).hexdigest()
number = int(sys.argv[1]); assert number in (29, 30)
filename = ('P15.1-prescribed-type-zero-volume-energy.tex' if number == 29
            else 'P15.2-prescribed-type-zero-volume-operator.tex')
for number, filename in [(number, filename)]:
    output = root / 'deliverables' / ('round-' + str(number))
    source = output / filename
    native = json.loads((root / 'deliverables' / ('round-' + str(number) + '-native-verification.json')).read_text())
    assert native['native_compilation_confirmed'] and native['tool_result']['kind'] == 'success'
    assert sha(source) == native['source_sha256']
    original = sha(source)
    build = output / 'export-build'
    build.mkdir(exist_ok=False)
    runs = []
    for pass_number in (1, 2):
        command = ['pdflatex', '-interaction=nonstopmode', '-halt-on-error', '-file-line-error',
                   '-output-directory=' + str(build), source.name]
        process = subprocess.run(command, cwd=output, capture_output=True, text=True)
        (build / ('pass-' + str(pass_number) + '.stdout.txt')).write_text(process.stdout)
        (build / ('pass-' + str(pass_number) + '.stderr.txt')).write_text(process.stderr)
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
    record = {
        'exported_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'source': str(source), 'source_sha256': sha(source),
        'source_changed': sha(source) != original,
        'pdf': str(pdf), 'pdf_sha256': sha(pdf), 'pages': pages,
        'runs': runs, 'final_notices': notices,
        'native_compilation_already_successful': True,
        'native_tool_returned_exported_pdf': False,
    }
    path = output / 'export-evidence.json'
    assert not path.exists()
    path.write_text(json.dumps(record, indent=2) + '\n')
    print(json.dumps(record, indent=2))
