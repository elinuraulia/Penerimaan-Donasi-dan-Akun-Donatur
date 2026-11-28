import os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),".."))
import subprocess
from playwright.sync_api import sync_playwright
N,G='#0A2A6B','#F0A81C'
H=f'graph[fontname="DejaVu Sans",dpi=200,nodesep=0.3,ranksep=0.35];node[fontname="DejaVu Sans",fontsize=11,shape=box,style="rounded,filled",fillcolor="#EEF2FA",color="{N}"];edge[fontname="DejaVu Sans",fontsize=9,color="{N}"];'
def dot(name,body):
    subprocess.run(['dot','-Tpng','-o',f'img/{name}.png'],input=f'digraph G{{{H}{body}}}',text=True,check=True)

dot('flow','rankdir=TB;a[label="T-01 Donatur mendaftar akun / mengisi data diri"];b[label="T-02 Data donatur diperiksa"];c[label="T-03 Donasi disatukan ke akun"];e[label="T-04 Bukti donasi diterbitkan"];f[label="T-05 Bukti diunduh atau dikirim"];g[label="T-06 Donatur melihat riwayat dan bukti"];h[label="Verifikasi keaslian bukti\n(kandidat CR-02)",style="rounded,dashed"];a->b->c->e->f->g;e->h[style=dashed];')
uc='rankdir=LR;nodesep=0.12;ranksep=1.8;'
A={'D':'Donatur','P':'Petugas donasi','A':'Admin','S':'Sistem Penerimaan\nDonasi','H':'Subsistem pengirim','V':'Penerima bukti'}
for k,v in A.items(): uc+=f'{k}[label="{v}",style=filled,fillcolor="{G}",shape=box];'
L={1:'Mendaftar dan masuk',2:'Mengelola profil',3:'Mengatur preferensi',4:'Menyatukan donasi ke akun',5:'Melihat riwayat dan donasi berulang',6:'Menerbitkan bukti donasi',7:'Mengunduh atau mengirim bukti',8:'Memverifikasi keaslian bukti',9:'Masuk sebagai staf',10:'Mengelola akun staf dan peran',11:'Melihat log akses',13:'Menerbitkan rekap tahunan',14:'Menghapus akun',15:'Mengirim pesan WhatsApp'}
who={1:'D',2:'D',3:'D',4:'SPD',5:'DP',6:'SP',7:'DP',8:'V',9:'PA',10:'A',11:'A',13:'DP',14:'DA',15:'H'}
uc+='subgraph cluster_s{label="Subsistem Akun Donatur dan Bukti Donasi";fontname="DejaVu Sans";'+''.join(f'u{i}[shape=ellipse,label="UC-{i:02d} {l}"];' for i,l in L.items())+'}'
for i,w in who.items():
    for x in w: uc+=(f'u{i}->{x}[dir=none];' if x in 'HV' else f'{x}->u{i}[dir=none];')
dot('uc',uc)
dot('mods','rankdir=TB;r[label="Akun Donatur dan Bukti Donasi",fillcolor="#F0A81C"];'+''.join(f'm{i}[label="M{i}\n{l}"];r->m{i};' for i,l in enumerate(['Akun dan\nprofil','Riwayat\ndonasi','Bukti\ndonasi','Pengguna dan\nhak akses','Kanal\nWhatsApp'],1)))
dot('state','rankdir=LR;a[label="Belum terbit"];b[label="Terbit"];c[label="Terkirim"];x[label="Dibatalkan"];a->b->c;b->x;c->x;')

def box(x,y,t):
    ls=t.split('|')
    return f'<rect x="{x}" y="{y}" width="130" height="58" rx="9" fill="#fff" stroke="#0A2A6B"/>'+''.join(f'<text x="{x+65}" y="{y+34-(len(ls)-1)*7+i*14}" text-anchor="middle">{l}</text>' for i,l in enumerate(ls))
def ar(p): return f'<polyline points="{p}" fill="none" stroke="#1b2333" marker-end="url(#a)"/>'
svg='<svg xmlns="http://www.w3.org/2000/svg" width="900" height="330" font-family="DejaVu Sans" font-size="11"><defs><marker id="a" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0,0L7,3L0,6z"/></marker></defs>'
svg+='<rect x="1" y="1" width="898" height="328" fill="#fff" stroke="#000"/><line x1="40" y1="1" x2="40" y2="329" stroke="#000"/><line x1="40" y1="110" x2="899" y2="110" stroke="#000"/><line x1="40" y1="220" x2="899" y2="220" stroke="#000"/>'
for y,t in [(55,'Donatur'),(165,'Petugas donasi'),(275,'Kanal / bank')]: svg+=f'<text transform="translate(24,{y}) rotate(-90)" text-anchor="middle">{t}</text>'
svg+='<circle cx="70" cy="55" r="15" fill="#fff" stroke="#000"/>'+box(105,26,'T-01 Memberi|data diri')+box(105,246,'Meneruskan|donasi')+box(270,136,'T-02 Memeriksa|data donatur')+box(430,136,'T-03 Mencocokkan|donasi dan donatur')+box(590,136,'T-04 Membuat|bukti manual')+box(750,136,'T-05 Menyerahkan|bukti')+box(750,26,'T-06 Menyimpan|bukti')
svg+=ar('85,55 103,55')+ar('170,84 170,244')+ar('235,275 335,275 335,196')+ar('400,165 428,165')+ar('560,165 588,165')+ar('720,165 748,165')+ar('815,136 815,86')+ar('750,55 700,55')
svg+='<circle cx="682" cy="55" r="15" fill="#fff" stroke="#000" stroke-width="3"/></svg>'
with sync_playwright() as p:
    br=p.chromium.launch();pg=br.new_page(viewport={'width':900,'height':200},device_scale_factor=2)
    pg.set_content('<body style="margin:0;width:900px">'+svg);pg.screenshot(path='img/bpmn.png',full_page=True)
    br.close()
