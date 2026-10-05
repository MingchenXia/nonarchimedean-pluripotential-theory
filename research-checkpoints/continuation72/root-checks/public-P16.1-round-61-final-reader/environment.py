from pathlib import Path
import json
import platform
import shutil
import subprocess
import sys

r=Path(__file__).resolve().parent
versions={}
for name in ['python3','pandoc','pdflatex','pdftotext']:
    command=[name,'-v' if name=='pdftotext' else '--version']
    p=subprocess.run(command,capture_output=True)
    output=p.stdout+p.stderr
    (r/f'{name}-version.txt').write_bytes(output)
    versions[name]={'path':shutil.which(name),'command':command,'returncode':p.returncode,'first_line':output.decode(errors='replace').split('\n')[0],'output_file':f'{name}-version.txt'}
(r/'environment.json').write_text(json.dumps({'python':platform.python_version(),'python_executable':sys.executable,'platform':platform.platform(),'cwd':str(r),'tools':versions},indent=2)+'\n')
print(json.dumps({'existing_tool_versions':len(versions)}))
