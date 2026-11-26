"""Pecah sumber/fr-lengkap.md menjadi satu berkas per FR di folder FR/."""
import os, re
base = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
text = open(os.path.join(base, 'sumber/fr-lengkap.md'), encoding='utf-8').read()
for part in re.split(r'(?m)^(?=##+ )', text):
    m = re.match(r'### (FR-ADBD-\d\d) (.*)', part)
    if not m:
        continue
    kode, judul = m[1], re.sub(r'\s*\\\[.*', '', m[2])
    folder = os.path.join(base, '..', 'FR', kode)
    os.makedirs(folder, exist_ok=True)
    isi = part.split('\n', 1)[1].replace('(../img/', '(../../adbd/img/').rstrip()
    kepala = (f'# {kode} {judul} \u00b7 Akun Donatur dan Bukti Donasi\n\n'
              'Kelompok 2 \u00b7 Business Analyst: Eli Nur Aulia \u00b7 Project Manager: Destri \u00b7 Status: draf\n\n')
    with open(os.path.join(folder, kode + '.md'), 'w', encoding='utf-8') as f:
        f.write(kepala + isi + f'\n\nTest scenario: TS-{kode[3:]}.\n')
