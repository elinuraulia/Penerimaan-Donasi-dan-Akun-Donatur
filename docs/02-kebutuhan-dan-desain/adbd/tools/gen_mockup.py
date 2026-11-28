import os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),".."))
from playwright.sync_api import sync_playwright
N,G='#0A2A6B','#F0A81C'
css=f'''body{{margin:0;font-family:"DejaVu Sans",sans-serif;font-size:14px;width:900px;background:#f4f6fa;color:#1b2333}}
.top{{background:{N};color:#fff;padding:10px 16px;display:flex;justify-content:space-between;border-bottom:4px solid {G}}}
.wrap{{display:flex;min-height:360px}}.side{{width:180px;background:#012766;color:#fff;padding:8px 0}}.side div{{padding:8px 16px}}.side .on{{background:{G};color:#012766;font-weight:bold}}
.main{{flex:1;padding:16px}}h3{{margin:0 0 12px;color:{N}}}.card{{background:#fff;border:1px solid #d5dbe8;border-radius:6px;padding:12px;margin-bottom:10px}}
table{{width:100%;border-collapse:collapse;background:#fff}}th,td{{border:1px solid #d5dbe8;padding:6px 8px;text-align:left;font-size:12px}}th{{background:#e8edf8}}
label{{display:block;font-size:12px;margin-top:8px}}.in{{border:1px solid #aab4ca;border-radius:4px;background:#fff;padding:6px;min-height:17px;color:#6b7590;font-size:12px}}
.btn{{display:inline-block;background:{N};color:#fff;border-radius:4px;padding:7px 16px;margin:10px 6px 0 0;font-size:12px}}.alt{{background:#fff;color:{N};border:1px solid {N}}}
.row{{display:flex;gap:10px}}.row>*{{flex:1}}.num{{font-size:22px;font-weight:bold;color:{N}}}'''
def page(on,title,body,side=True):
    menu=''.join(f'<div class="{"on" if m==on else ""}">{m}</div>' for m in ['Beranda','Profil','Riwayat donasi','Bukti donasi','Donatur','Akun','Catatan akses'])
    inner=f'<div class="wrap"><div class="side">{menu}</div><div class="main"><h3>{title}</h3>{body}</div></div>' if side else body
    return f'<meta charset="utf-8"><style>{css}</style><div class="top"><b>[Logo] Baitulmal Tazkia</b><span>{"Nama pengguna · Peran" if side else ""}</span></div>{inner}'
def tbl(h,rows): return '<table><tr>'+''.join(f'<th>{x}</th>' for x in h)+'</tr>'+''.join('<tr>'+''.join(f'<td>{c}</td>' for c in r)+'</tr>' for r in rows)+'</table>'
def f(l,v=''): return f'<div><label>{l}</label><div class="in">{v}</div></div>'
def b(*a): return ''.join(f'<span class="btn {"alt" if i else ""}">{x}</span>' for i,x in enumerate(a))

rw=[['DN-0001 (contoh)','02/11/2026','Rp100.000','Infak','Terbit','Lihat'],['DN-0002 (contoh)','05/11/2026','Rp250.000','Zakat','Terkirim','Lihat']]
th=['Referensi','Tanggal','Nominal','Peruntukan','Status bukti','']
P={
'login':page('','',f'<div style="max-width:340px;margin:30px auto" class="card"><h3>Masuk</h3>{b("Masuk dengan Google")}{f("Nomor telepon","08xx")}{b("Kirim OTP")}{f("Kode OTP")}{b("Masuk")}<label>Staf: masuk dengan Google, lalu kode TOTP.</label></div>',False),
'beranda':page('Beranda','Beranda','<div class="row">'+''.join(f'<div class="card">{a}<div class="num">{v}</div></div>' for a,v in [('Total donasi saya','Rp350.000'),('Jumlah donasi','2'),('Bukti tersedia','2')])+'</div><div class="card">Aktivitas terbaru<br><br>'+tbl(th,rw)+'</div>'),
'tabel':page('Bukti donasi','Daftar data','<div class="row">'+f('Cari')+f('Status','Semua')+f('Periode')+'</div>'+b('Tambah Data')+'<br><br>'+tbl(th,rw)+'<label>Halaman 1 dari 1 · Total 2 data</label>'),
'form':page('Profil','Formulir input',f'<div class="card">{f("Nama *")}{f("Email *")}{f("Keterangan")}{f("Lampiran")}{b("Simpan","Batal")}</div>'),
'daftar':page('','',f'<div style="max-width:380px;margin:20px auto" class="card"><h3>Masuk atau daftar</h3>{b("Masuk dengan Google")}{f("Nomor telepon *","080000000000")}{b("Kirim OTP")}{f("Kode OTP *")}{f("Persetujuan penggunaan data *","[ ] Saya setuju")}{b("Lanjut","Batal")}</div>',False),
'profil':page('Profil','Profil saya',f'<div class="card">{f("Nama lengkap *","Donatur Contoh")}{f("Email *","contoh@example.com")}{f("Nomor telepon","080000000000")}{f("Alamat")}{b("Simpan","Batal")}</div>'),
'pref':page('Profil','Preferensi',f'<div class="card">{f("Tampil sebagai","Nama")}{f("Kirim bukti melalui","Email")}{b("Simpan","Batal")}</div>'),
'taut':page('Donatur','Antrean konfirmasi',tbl(['Referensi','Nama pada donasi','Dasar kemiripan','Kandidat akun','Tindakan'],[['DN-0003','Donatur C.','Nama mirip','Donatur Contoh','Satukan | Tolak']])+f'<div class="card">{f("Alasan *")}</div>'),
'riwayat':page('Riwayat donasi','Riwayat donasi saya','<div class="row">'+f('Periode')+f('Peruntukan','Semua')+'</div><br>'+tbl(th,rw)+'<label>Total: Rp350.000</label><div class="card">Donasi berulang: Aktif (contoh)'+b('Kelola')+'</div>'),
'rekap':page('Bukti donasi','Rekapitulasi tahunan',f'<div class="card">{f("Tahun *","2026")}'+tbl(['Tanggal','Referensi','Zakat'],[['02/03/2026','DN-0010','Rp250.000'],['05/04/2026','DN-0011','Rp750.000']])+'<label>Nomor: RK-2026-000001 · Total: Rp1.000.000</label>'+b('Terbitkan','Unduh PDF')+'</div>'),
'hapus':page('Profil','Hapus akun',f'<div class="card">Akun dan identitas masuk dihapus. Catatan donasi tetap disimpan untuk audit.{f("Kode OTP konfirmasi *")}{b("Hapus akun","Batal")}</div>'),
'bukti':page('Bukti donasi','Bukti donasi',f'<div class="card" style="max-width:460px"><b>BUKTI DONASI (CONTOH)</b><br><br>'+tbl(['Field','Isi'],[['Nomor urut bukti','BD-2026-000001'],['Referensi donasi','DN-0001'],['Nama','Donatur Contoh'],['Tanggal','02/11/2026'],['Nominal','Rp100.000'],['Peruntukan','Infak'],['Kode verifikasi','CONTOH-1234']])+b('Unduh PDF','Kirim email')+'</div>'),
'verif':page('','',f'<div style="max-width:380px;margin:30px auto" class="card"><h3>Verifikasi bukti</h3>{f("Kode verifikasi *","CONTOH-1234")}{b("Periksa")}<br><br>Hasil: Sah · BD-2026-000001 · 02/11/2026 · Rp100.000</div>',False),
'akun':page('Akun','Kelola akun staf',tbl(['Email Google','Peran','Status',''],[['petugas@example.com','Petugas donasi','Aktif','Ubah · Nonaktifkan']])+f'<div class="card">{f("Email Google *")}{f("Peran *","Pilih peran")}{b("Simpan","Batal")}</div>'),
'ditolak':page('Beranda','Akses ditolak','<div class="card">Anda tidak berhak membuka halaman ini (403).'+b('Kembali ke beranda')+'</div>'),
'log':page('Catatan akses','Catatan akses','<div class="row">'+f('Pengguna')+f('Donatur')+f('Tanggal')+'</div><br>'+tbl(['Waktu','Pengguna','Donatur','Jenis akses'],[['02/11 10.02','petugas.contoh','D-001','Lihat profil']])),
}
NAMA={'login': 'umum-1-login', 'beranda': 'umum-2-beranda', 'tabel': 'umum-3-tabel', 'form': 'umum-4-formulir', 'daftar': 'adbd-01-daftar', 'profil': 'adbd-02-profil', 'pref': 'adbd-03-preferensi', 'taut': 'adbd-04-penautan', 'riwayat': 'adbd-05-riwayat', 'bukti': 'adbd-06-bukti', 'verif': 'adbd-08-verifikasi', 'ditolak': 'adbd-09-ditolak', 'akun': 'adbd-10-akun', 'log': 'adbd-11-catatan-akses', 'rekap': 'adbd-13-rekap', 'hapus': 'adbd-14-hapus'}
import subprocess, tempfile
for d in ['Wireframe/html','Wireframe/png','Wireframe/svg','img']: os.makedirs(d,exist_ok=True)
with sync_playwright() as p:
    br=p.chromium.launch();pg=br.new_page(viewport={'width':900,'height':200},device_scale_factor=2)
    for i,(k,nm) in enumerate(NAMA.items(),1):
        f=f'{i:02d}-{nm}'
        open(f'Wireframe/html/{f}.html','w').write('<!doctype html>'+P[k])
        pg.set_content(P[k]);pg.screenshot(path=f'img/{nm}.png',full_page=True);pg.screenshot(path=f'Wireframe/png/{f}.png',full_page=True)
        h=pg.evaluate('document.documentElement.scrollHeight')
        with tempfile.TemporaryDirectory() as t:
            pg.emulate_media(media='screen');pg.pdf(path=t+'/a.pdf',width='900px',height=f'{h+2}px',print_background=True,page_ranges='1')
            subprocess.run(['pdftocairo','-svg',t+'/a.pdf',f'Wireframe/svg/{f}.svg'],check=True)
    br.close()
