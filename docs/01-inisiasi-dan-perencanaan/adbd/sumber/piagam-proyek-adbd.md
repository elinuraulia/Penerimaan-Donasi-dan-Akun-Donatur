# Piagam Proyek (Project Charter)

Akun Donatur dan Bukti Donasi · Baitulmal Tazkia

| **Item** | **Isi** |
|----------------|----------------------------------------------|
| Kelompok | 2 (pasangan: Kelompok 1, Penerimaan Donasi) |
| Dosen | Endy Muhardin |
| Project Manager | Destri Komalasari |
| Business Analyst | Eli Nur Aulia |
| Versi | 0.1 (draf), 27 November 2026 |
| Status | DRAF, belum ada sign-off. \[USULAN\] = usulan tim; \[DUGAAN\] = belum dikonfirmasi klien |

## 1. Latar belakang

Baitulmal Tazkia (BMTZ) mengelola zakat, infak, sedekah, dan wakaf di Sentul, Bogor. Menurut workbook, donasi masuk lewat beberapa kanal terpisah dan rekonsiliasi dikerjakan dengan membandingkan file satu per satu. Donatur ingin melihat seluruh pemberiannya di satu tempat dan memperoleh bukti setor zakat. Proyek ini termasuk modul K1 Penerimaan Donasi dan Akun Donatur, salah satu dari enam modul pada berita acara BMT-KKS-001 tanggal 12 November 2026.

## 2. Tujuan proyek

| **ID** | **Tujuan** |
|--------|------------------------------------------------------------|
| TB-01 | Data donatur tertata, satu identitas terverifikasi hanya milik satu akun |
| TB-02 | Donatur dapat melihat donasinya sendiri |
| TB-03 | Bukti donasi dan bukti setor zakat cepat tersedia |
| TB-04 | Data pribadi donatur terlindungi dan dapat diaudit |

## 3. Ruang lingkup

**Dalam lingkup:** pendaftaran dan login donatur (Google atau OTP), penyatuan donasi dari berbagai kanal, riwayat pemberian dan status donasi berulang, bukti donasi, rekapitulasi tahunan, pilihan anonim, penghapusan akun, hak akses dan log akses, serta kanal WhatsApp pada Aplikasi Notifikasi Tazkia.

**Di luar lingkup:** pencatatan donasi (Kelompok 1), penagihan donasi berulang (kelompok Donasi Berulang), pemrosesan pembayaran, kampanye pemasaran, pesan masuk dan broadcast WhatsApp.

## 4. Kriteria keberhasilan yang terukur \[USULAN\]

| **No** | **Kriteria** | **Cara mengukur** | **Tenggat** |
|----|------------------------------------|----------------------------------|----------|
| 1 | SRS menjadi baseline dan memiliki sign-off narasumber | Dokumen bertanda tangan | Minggu 4 |
| 2 | Setiap FR yang berlaku punya acceptance criteria dan test scenario | Diperiksa pada RTM: 100% | Minggu 4 |
| 3 | Seluruh FR berprioritas Must lulus UAT | Laporan UAT | Minggu 14 |
| 4 | Tidak ada penyatuan donasi ke orang yang salah pada data uji | Skenario uji FR-ADBD-04 | Minggu 14 |
| 5 | Dari login sampai unduh bukti paling lama 2 menit | Uji dengan pengguna | Minggu 14 |
| 6 | Seluruh akses staf ke data donatur tercatat | Uji log akses | Minggu 14 |
| 7 | Tidak ada kredensial atau data donatur asli di repository | Pemeriksaan repository | Setiap fase |

## 5. Deliverable dan rencana proyek

Jadwal mengikuti fase pada workbook. Angka minggu adalah minggu perkuliahan.

| **Fase** | **Minggu** | **Kegiatan utama** | **Deliverable** |
|------------------|--------|----------------------------------|------------------------------|
| 0 Mobilisasi | 1 | Pembentukan kelompok, repository, papan kanban, perjanjian kerahasiaan, pemangku kepentingan | Piagam proyek, stakeholder register |
| 1 Kebutuhan | 1 sampai 4 | Value chain, wawancara, observasi, proses as-is, risk register | SRS, RTM, model proses as-is |
| 2 Perancangan | 5 sampai 8 | Perancangan, studi kelayakan, MoSCoW, usulan proses to-be | Dokumen perancangan |
| 3 Konstruksi | 9 sampai 12 | Implementasi, integrasi API, unit test | Rilis v0.9, laporan pengujian |
| 4 Verifikasi dan validasi | 13 sampai 14 | Integration test, keamanan dasar, UAT | Laporan UAT |
| 5 Rilis | 14 sampai 16 | Deployment, pelatihan, serah terima | Paket serah terima |

## 6. Tim proyek

| **Nama** | **Peran** | **Tanggung jawab utama** |
|--------------------------------|------------------|--------------------------------------------|
| Destri Komalasari | Project Manager | Rencana, jadwal, risiko, koordinasi antarkelompok |
| Eli Nur Aulia | Business Analyst | Elisitasi, proses bisnis, BRS, SRS, RTM |
| Azza Ummu Habibatulloh | Technical Writer | Kerapian dokumen, notulen, panduan pengguna |
| Muhammad Zidan Ar Rizki | Developer | Perancangan teknis, kode, deployment |
| Muhammad Dzaki Al Hassani Ihsan | Quality Control | Test scenario, pengujian, pemeriksaan mutu |

Pembagian tanggung jawab di atas \[USULAN\].

## 7. Pemangku kepentingan utama

Dosen (Endy Muhardin), PIC modul K1 BMTZ, staf penghimpunan, staf layanan donatur, donatur, Kelompok 1, dan kelompok Donasi Berulang. Rincian ada di Stakeholder Register.

## 8. Asumsi, batasan, dan ketergantungan

- Pengembangan memakai data sintetis sampai perjanjian pemrosesan data dan kerahasiaan ditandatangani.
- Data donasi diperoleh dari Kelompok 1 lewat API; data contoh dipakai lebih dulu.
- Status donasi berulang dan signed URL disediakan kelompok Donasi Berulang.
- Kanal WhatsApp bergantung pada verifikasi akun bisnis dan persetujuan template oleh Meta.
- Waktu PIC BMTZ terbatas; sesi wawancara dijadwalkan bersama Kelompok 1.

## 9. Risiko utama

Penyatuan donasi ke orang yang salah, penyalahgunaan OTP, kontrak API belum disepakati, wawancara belum terlaksana, dan persetujuan Meta. Rincian ada di Risk Register.

## 10. Tata kelola \[USULAN\]

- Rapat tim mingguan dengan notulen yang disimpan di repository.
- Setiap deliverable melalui draf, review, revisi, lalu sign-off.
- Perubahan terhadap baseline diajukan sebagai change request dengan dampaknya.
- Setiap anggota melakukan commit atas pekerjaannya sendiri.

## 11. Persetujuan

| **Peran** | **Nama** | **Tanda tangan** | **Tanggal** |
|------------------------------|--------------------|----------------|------------|
| Dosen | Endy Muhardin | | |
| PIC Baitulmal Tazkia | | | |
| Project Manager | Destri Komalasari | | |
| Business Analyst | Eli Nur Aulia | | |
