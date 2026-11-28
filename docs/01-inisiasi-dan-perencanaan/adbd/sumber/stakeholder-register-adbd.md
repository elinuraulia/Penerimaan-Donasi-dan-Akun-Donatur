# Stakeholder Register

Akun Donatur dan Bukti Donasi · Baitulmal Tazkia

| **Item** | **Isi** |
|----------------|----------------------------------------------|
| Kelompok | 2 (pasangan: Kelompok 1, Penerimaan Donasi) |
| Dosen | Endy Muhardin |
| Project Manager | Destri Komalasari |
| Business Analyst | Eli Nur Aulia |
| Versi | 0.1 (draf), 27 November 2026 |
| Status | DRAF, belum ada sign-off. \[USULAN\] = usulan tim; \[DUGAAN\] = belum dikonfirmasi klien |

Domain pemangku kepentingan menurut workbook: penghimpunan dan layanan donatur. Peran di bawah disusun dari workbook dan model as-is. Nama orang di BMTZ belum diketahui dan diisi setelah wawancara. Tingkat pengaruh, minat, dan strategi adalah \[USULAN\].

## 1. Daftar pemangku kepentingan

| **ID** | **Peran** | **Nama** | **Kategori** | **Kepentingan** |
|-------|----------------------------|------------------|------------|------------------------------|
| SH-01 | Dosen | Endy Muhardin | Akademik | Mutu proses dan deliverable |
| SH-02 | PIC modul K1 BMTZ | (belum diketahui) | Klien | Kebutuhan sesuai kenyataan; menyetujui hasil |
| SH-03 | Staf penghimpunan donasi | (belum diketahui) | Klien | Donasi terhubung ke donatur yang tepat |
| SH-04 | Staf layanan donatur (petugas donasi) | (belum diketahui) | Klien | Konfirmasi penyatuan dan bukti lebih cepat |
| SH-05 | Staf pengelola aplikasi CRM | (belum diketahui) | Klien | Akun bisnis Meta dan nomor WhatsApp |
| SH-06 | Staf keuangan | (belum diketahui) | Klien | Angka pada bukti cocok dengan catatan |
| SH-07 | Admin sistem | (belum diketahui) | Klien | Akun staf, peran, dan log |
| SH-08 | Donatur dan muzaki | Kelompok pengguna | Pengguna | Riwayat, bukti, rekap, privasi |
| SH-09 | Tim Penerimaan Donasi | Kelompok 1 | Kelompok pasangan | Kontrak API data donasi |
| SH-10 | Tim Donasi Berulang | (isi kelompok) | Kelompok lain | Status dan signed URL |
| SH-11 | Pengelola Aplikasi Notifikasi Tazkia | (belum diketahui) | Pemilik produk | Kanal WhatsApp mengikuti pola yang ada |
| SH-12 | Meta (WhatsApp) | Penyedia | Pihak ketiga | Verifikasi akun dan persetujuan template |
| SH-13 | Tim Kelompok 2 | Lima anggota | Tim proyek | Deliverable selesai tepat waktu |

## 2. Matriks pengaruh dan kepentingan

| | **Minat rendah** | **Minat tinggi** |
|------------------|------------------------------|------------------------------|
| **Pengaruh tinggi** | **Jaga kepuasan:** SH-05, SH-12 | **Kelola dekat:** SH-01, SH-02, SH-04, SH-09 |
| **Pengaruh rendah** | **Pantau:** SH-06 | **Beri kabar:** SH-03, SH-07, SH-08, SH-10, SH-11, SH-13 |

SH-13 mengerjakan proyek setiap hari, sehingga komunikasinya diatur lewat rapat tim.

## 3. Strategi engagement

| **ID** | **Pengaruh** | **Minat** | **Strategi** | **Kanal** | **Frekuensi** | **Minggu 2** |
|-------|----------|----------|------------------------|------------------|-------------|--------------|
| SH-01 | Tinggi | Tinggi | Konsultasi dan review deliverable | Tatap muka, repository | Mingguan | Diberi kabar |
| SH-02 | Tinggi | Tinggi | Wawancara, validasi, sign-off | Sesi terjadwal | Per tahap | Diwawancarai |
| SH-03 | Rendah | Tinggi | Gali proses sekarang | Wawancara, observasi | Saat elisitasi | Diwawancarai |
| SH-04 | Tinggi | Tinggi | Gali proses, uji bersama | Wawancara, observasi | Per tahap | Diwawancarai |
| SH-05 | Tinggi | Rendah | Pastikan akun dan nomor | Pertemuan singkat | Sesuai kebutuhan | Diwawancarai |
| SH-06 | Rendah | Rendah | Konfirmasi format bukti | Pesan lewat PIC | Sesuai kebutuhan | Diberi kabar |
| SH-07 | Rendah | Tinggi | Gali kebutuhan akses | Wawancara | Saat perancangan | Diberi kabar |
| SH-08 | Rendah | Tinggi | Survei dan uji coba | Kuesioner lewat BMTZ | Minggu 3 dan UAT | Diberi kabar |
| SH-09 | Tinggi | Tinggi | Sepakati kontrak data | Rapat antarkelompok | Mingguan | Hadir bersama |
| SH-10 | Rendah | Tinggi | Sepakati kontrak API | Rapat antarkelompok | Per tahap | Diberi kabar |
| SH-11 | Rendah | Tinggi | Sepakati topic dan template | Pertemuan teknis | Saat perancangan | Diberi kabar |
| SH-12 | Tinggi | Rendah | Ajukan verifikasi sedini mungkin | Lewat SH-05 | Sesuai kebutuhan | Tidak |
| SH-13 | Rendah | Tinggi | Bagi tugas dan pantau | Grup tim, rapat | Mingguan | Peserta |

## 4. RACI per deliverable \[USULAN\]

R = mengerjakan, A = penanggung jawab akhir (tepat satu), C = dimintai masukan, I = diberi tahu. PM = Destri, BA = Eli, TW = Azza, DEV = Zidan, QC = Dzaki.

| **Deliverable** | **PM** | **BA** | **TW** | **DEV** | **QC** | **Dosen** | **PIC** |
|------------------------------|----|----|----|-----|----|-------|-----|
| Piagam proyek | A | R | C | I | I | C | C |
| Stakeholder register | C | A/R | C | I | I | C | C |
| Value chain dan RACI proses | I | A/R | C | I | I | C | C |
| Risk register | A/R | C | C | C | C | C | I |
| Notulen | A | C | R | I | I | I | I |
| BRS, SRS, RTM | I | A/R | R | C | C | C | C |
| Model proses as-is | I | A/R | C | I | I | C | C |
| Dokumen perancangan | I | C | R | A/R | C | C | I |
| Kode dan deployment | I | C | I | A/R | C | I | I |
| Test scenario dan laporan uji | I | C | C | C | A/R | I | I |
| UAT | A | R | C | C | R | I | C |
| Paket serah terima | A | C | R | R | C | I | C |

## 5. Catatan pembaruan

| **Versi** | **Tanggal** | **Perubahan** | **Oleh** |
|-------|------------------|----------------------------------------------|----------------|
| 0.1 | 27 November 2026 | Versi awal dari workbook dan model as-is; belum divalidasi | Eli Nur Aulia |
