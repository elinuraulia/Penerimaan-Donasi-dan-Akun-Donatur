"""Ubah docx menjadi PDF dengan LibreOffice."""
import subprocess, sys, os
for f in sys.argv[1:]:
    subprocess.run(['soffice', '--headless', '--convert-to', 'pdf', '--outdir', os.path.dirname(f) or '.', f], check=True)
