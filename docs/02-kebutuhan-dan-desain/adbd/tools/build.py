import os, glob, subprocess, shutil
T=os.path.dirname(os.path.abspath(__file__)); A=os.path.dirname(T); K=os.path.dirname(A); D=os.path.dirname(K)
for m in glob.glob(A+'/diagram/*.mmd'):
    subprocess.run(['mmdc','-i',m,'-o',f'{A}/diagram/img/{os.path.basename(m)[:-4]}.png','-s','2','-b','white'],check=True,capture_output=True)
subprocess.run(['dot','-Tpng','-Gdpi=200',A+'/diagram/value-chain.dot','-o',A+'/diagram/img/value-chain.png'],check=True)
def docx(md,out):
    os.makedirs(os.path.dirname(out),exist_ok=True)
    subprocess.run(['pandoc',md,'-f','markdown-implicit_figures','-o',out,'--resource-path='+os.path.dirname(md),'--reference-doc='+A+'/template/reference.docx'],check=True,cwd=os.path.dirname(md))
    subprocess.run(['python3',T+'/post.py',out],check=True)
    return out
I=D+'/01-inisiasi-dan-perencanaan/adbd'; S=A+'/sumber'
files=[docx(I+'/sumber/brs-adbd.md',I+'/output/BRS_ADBD_v0.2.docx'),docx(I+'/sumber/catatan-wawancara-adbd.md',I+'/output/catatan-wawancara-adbd.docx'),
 docx(I+'/sumber/pertanyaan-lanjutan-pic-adbd.md',I+'/output/pertanyaan-lanjutan-pic-adbd.docx'),
 *[docx(f'{I}/sumber/{n}-adbd.md',f'{I}/output/{n}-adbd.docx') for n in ('piagam-proyek','stakeholder-register','risk-register','value-chain-raci')],docx(S+'/srs-adbd.md',A+'/output/SRS_Akun_Donatur_dan_Bukti_Donasi_v0.4.docx')]
for m in glob.glob(S+'/docs/klien/*.md')+glob.glob(S+'/docs/internal/*.md')+[S+'/docs/penelusuran-fr.md']:
    files.append(docx(m,f'{A}/output/{os.path.basename(m)[:-3]}.docx'))
for m in glob.glob(K+'/FR/*.md')+glob.glob(D+'/04-pengujian-dan-penerimaan/Test-Scenario/*.md'):
    files.append(docx(m,m[:-3]+'.docx'))
by={}
for f in files: by.setdefault(os.path.dirname(f),[]).append(f)
for d,fs in by.items():
    subprocess.run(['soffice','--headless','--convert-to','pdf','--outdir',d]+fs,check=True,capture_output=True)
print(len(files),'dokumen')
