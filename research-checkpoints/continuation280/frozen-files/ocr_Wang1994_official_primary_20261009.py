from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib, json, subprocess
P=Path('/workspace/research/primary-data-LOCALONLY/P12.3-formal-Noether-different-primary-20261009/dependencies-LOCALONLY')
pdf=P/'Wang1994-official.pdf'; assert hashlib.sha256(pdf.read_bytes()).hexdigest()=='c1d47394134659e0b6f56ad4398b7c24e5aad57a713a3718ad71a2c0c7f11b99'
D=P/'Wang1994-pages-and-OCR-LOCALONLY'; assert not D.exists(); D.mkdir()
subprocess.run(['pdftoppm','-r','140','-gray','-png',str(pdf),str(D/'page')],check=True,capture_output=True)
pages=sorted(D.glob('page-*.png')); assert len(pages)==22
def convert(p):
    target=p.with_suffix('')
    subprocess.run(['tesseract',str(p),str(target),'--psm','3'],check=True,capture_output=True)
    t=p.with_suffix('.txt'); return dict(pixel=str(p),pixel_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),OCR=str(t),OCR_bytes=t.stat().st_size,OCR_sha256=hashlib.sha256(t.read_bytes()).hexdigest(),retention_not_actual_pixel_inspection=True)
with ThreadPoolExecutor(max_workers=3) as pool:rows=list(pool.map(convert,pages))
text=P/'Wang1994-official-full-OCR-LOCALONLY.txt'
text.write_text('\n'.join('PDF one-based page '+str(i+1)+'\n'+Path(r['OCR']).read_text() for i,r in enumerate(rows)))
(D/'OCR-retention-metadata-LOCALONLY.json').write_text(json.dumps(rows,indent=2)+'\n')
print(json.dumps(dict(whole_OCR=str(text),bytes=text.stat().st_size,sha256=hashlib.sha256(text.read_bytes()).hexdigest(),pages=22,source_program_execution_or_import=False,OCR_not_physical_pixel_reading=True),indent=2))
