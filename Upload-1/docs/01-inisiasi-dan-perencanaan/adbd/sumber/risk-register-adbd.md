# Risk Register

Akun Donatur dan Bukti Donasi · Baitulmal Tazkia

| **Item** | **Isi** |
|----------------|----------------------------------------------|
| Kelompok | 2 (pasangan: Kelompok 1, Penerimaan Donasi) |
| Dosen | Endy Muhardin |
| Project Manager | Destri Komalasari |
| Business Analyst | Eli Nur Aulia |
| Versi | 0.1 (draf), 27 November 2026 |
| Status | DRAF, belum ada sign-off. \[USULAN\] = usulan tim; \[DUGAAN\] = belum dikonfirmasi klien |

Lima risiko awal dari workbook subbab 3.6 ada pada R-006 sampai R-010. R-001, R-002, R-003, dan R-005 berasal dari BRS. Nilai peluang, dampak, mitigasi, pemilik, dan tanggal tinjau adalah \[USULAN\] yang perlu disepakati tim.

## 1. Skala penilaian

Peluang (P) dan dampak (D) bernilai 1 (sangat rendah) sampai 5 (sangat tinggi). Paparan = P × D. Tinggi: 15 sampai 25; Sedang: 9 sampai 14; Rendah: 1 sampai 8.

## 2. Penilaian risiko

| **ID** | **Risiko** | **Akibat** | **P** | **D** | **Nilai** | **Tingkat** |
|------|----------------------------|--------------------------|---|---|-----|-------|
| R-001 | Proses as-is belum tervalidasi karena wawancara belum terlaksana | Kebutuhan keliru dan harus dirombak | 4 | 4 | 16 | Tinggi |
| R-002 | Kontrak API dengan Kelompok 1 belum disepakati | Integrasi data donasi gagal | 3 | 4 | 12 | Sedang |
| R-003 | Kebijakan data pribadi belum lengkap | Akses dan masa simpan tidak sesuai UU PDP | 3 | 5 | 15 | Tinggi |
| R-005 | Batas rilis belum final | Lingkup melebar dan jadwal mundur | 3 | 3 | 9 | Sedang |
| R-006 | Dua donatur berbeda keliru disatukan | Riwayat pemberian seseorang terbuka kepada orang lain | 3 | 5 | 15 | Tinggi |
| R-007 | Bukti setor zakat memuat angka berbeda dari catatan donasi | Muzaki dirugikan saat pelaporan pajak | 3 | 4 | 12 | Sedang |
| R-008 | Penghapusan akun ikut menghapus catatan wajib audit | Data audit hilang | 2 | 5 | 10 | Sedang |
| R-009 | OTP dapat ditebak atau dikirim berulang tanpa batas | Akun donatur diambil alih | 3 | 5 | 15 | Tinggi |
| R-010 | Verifikasi akun bisnis dan template Meta belum selesai | Kanal WhatsApp tidak dapat dipakai | 4 | 3 | 12 | Sedang |
| R-011 | Kredensial atau data asli masuk repository publik | Kebocoran data dan pelanggaran | 2 | 5 | 10 | Sedang |
| R-012 | Perjanjian pemrosesan data dan kerahasiaan belum ditandatangani | Data asli tidak dapat diperiksa | 3 | 3 | 9 | Sedang |
| R-013 | Deadline padat dan pekerjaan menumpuk pada satu orang | Deliverable terlambat atau mutunya turun | 4 | 3 | 12 | Sedang |

## 3. Rencana penanganan

| **ID** | **Mitigasi** | **Bila terjadi** | **Pemilik** | **Tinjau ulang** | **Status** |
|------|--------------------------|----------------------|----------|---------|-------|
| R-001 | Jadwalkan sesi bersama PIC; tandai [DUGAAN] sampai terbukti | Ajukan jadwal pengganti lewat dosen | Eli (BA) | 4 Des 2026 | Terbuka |
| R-002 | Sepakati data, status, dan galat | Kembangkan dengan data contoh | Destri (PM) | 4 Des 2026 | Terbuka |
| R-003 | Validasi atribut, akses, dan retensi dengan PIC | Batasi akses seminimal mungkin | Eli (BA) | 4 Des 2026 | Terbuka |
| R-005 | Tetapkan prioritas MoSCoW dan baseline | Tunda FR berprioritas Could | Destri (PM) | 4 Des 2026 | Terbuka |
| R-006 | Otomatis hanya untuk email atau nomor terverifikasi; yang mirip masuk antrean | Batalkan penyatuan dan beri tahu PIC | Zidan (Dev) | 4 Des 2026 | Terbuka |
| R-007 | Terbitkan dari data terkini lalu simpan apa adanya dengan nomor urut | Tinjau dan koreksi lewat prosedur resmi | Zidan (Dev) | 4 Des 2026 | Terbuka |
| R-008 | Hanya putus hubungan akun dengan donasi; uji khusus | Pulihkan dari cadangan | Dzaki (QC) | 4 Des 2026 | Terbuka |
| R-009 | Batas kirim dan percobaan, masa berlaku singkat | Kunci akun sementara dan tinjau log | Zidan (Dev) | 4 Des 2026 | Terbuka |
| R-010 | Ajukan sejak awal bersama pengelola CRM | Tetap memakai email lewat konfigurasi template | Destri (PM) | 4 Des 2026 | Terbuka |
| R-011 | Hanya data sintetis; periksa sebelum commit | Cabut kredensial dan hapus dari riwayat | Dzaki (QC) | 4 Des 2026 | Terbuka |
| R-012 | Tindak lanjuti dengan dosen dan PIC | Teruskan dengan data sintetis | Destri (PM) | 4 Des 2026 | Terbuka |
| R-013 | Bagi tugas menurut RACI; pantau mingguan | Prioritaskan deliverable yang dinilai lebih dulu | Destri (PM) | 4 Des 2026 | Terbuka |

## 4. Catatan tinjauan

| **Tanggal** | **Perubahan** | **Oleh** |
|------------------|----------------------------------------------|----------------|
| 27 November 2026 | Register awal | Eli Nur Aulia |
