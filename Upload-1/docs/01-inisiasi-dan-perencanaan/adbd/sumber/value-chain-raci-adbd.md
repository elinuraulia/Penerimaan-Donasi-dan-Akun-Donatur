# Value Chain, Hierarki Proses, dan RACI

Akun Donatur dan Bukti Donasi · Baitulmal Tazkia

| **Item** | **Isi** |
|----------------|----------------------------------------------|
| Kelompok | 2 (pasangan: Kelompok 1, Penerimaan Donasi) |
| Dosen | Endy Muhardin |
| Project Manager | Destri Komalasari |
| Business Analyst | Eli Nur Aulia |
| Versi | 0.1 (draf), 27 November 2026 |
| Status | DRAF, belum ada sign-off. \[USULAN\] = usulan tim; \[DUGAAN\] = belum dikonfirmasi klien |

Disusun dari workbook, SRS v0.4, dan model as-is. Seluruh isi \[DUGAAN\] sampai divalidasi pemilik proses. Value chain gabungan dua belas kelompok disatukan oleh dosen.

## 1. Value chain Baitulmal Tazkia (model Porter)

![Value chain](../../../02-kebutuhan-dan-desain/adbd/diagram/img/value-chain.png){width=6.4in}

Kotak berwarna hijau memuat proses subsistem Kelompok 2.

## 2. Daftar proses dan klasifikasinya

| **ID** | **Proses** | **Jenis** | **Pemicu** | **Hasil akhir** | **FR** |
|------|------------------|------------|----------------|----------------|--------|
| P-01 | Pendaftaran dan login donatur | Inti | Donatur ingin masuk | Akun aktif, identitas terverifikasi | 01 |
| P-02 | Pengelolaan akun donatur | Pendukung | Donatur mengubah data atau meminta hapus | Data diperbarui atau akun dihapus | 02, 03, 14 |
| P-03 | Penyatuan donasi ke akun | Inti | Donasi atau identitas baru | Donasi terhubung ke akun yang tepat | 04 |
| P-04 | Penyajian riwayat dan donasi berulang | Inti | Donatur membuka riwayat | Riwayat dan status tampil | 05 |
| P-05 | Penerbitan dan penyerahan bukti | Inti | Donasi berstatus berhasil | Bukti bernomor diterima donatur | 06, 07, 08 |
| P-06 | Rekapitulasi tahunan | Inti | Permintaan atau akhir tahun | Bukti setor zakat tahunan | 13 |
| P-07 | Pengelolaan staf, hak akses, dan log | Manajemen | Staf baru, perubahan peran, audit | Akses sesuai kewenangan dan tercatat | 09, 10, 11 |
| P-08 | Pengiriman pesan WhatsApp | Pendukung | Subsistem pengirim menerbitkan pesan | Pesan terkirim atau gagal tercatat | 15 |

Proses yang saat ini diduga berjalan lewat spreadsheet atau percakapan WhatsApp, sehingga menjadi kandidat pemodelan pertama: P-03 dan P-05.

## 3. Hierarki proses

| **Proses** | **Subproses** | **Aktivitas** | **Task as-is** |
|---------|--------------------|------------------------------------------|----------|
| P-01 | Identifikasi donatur | Memberi data diri; verifikasi Google atau OTP | T-01 |
| P-02 | Pemeliharaan data | Memeriksa data; mengubah profil dan preferensi; menghapus akun | T-02 |
| P-03 | Pencocokan | Mencocokkan donasi dan donatur; konfirmasi; pembatalan | T-03 |
| P-04 | Penyajian | Mengambil donasi; menampilkan riwayat; membuka signed URL | T-06 |
| P-05 | Penerbitan | Membuat bukti | T-04 |
| P-05 | Penyerahan | Menyerahkan bukti; menyimpan bukti | T-05, T-06 |
| P-06 | Rekapitulasi | Mengumpulkan donasi setahun; menerbitkan rekap | T-04 |
| P-07 | Kendali akses | Login staf; mengelola peran; meninjau log | Lintas |
| P-08 | Pengiriman | Menyusun template; mengirim; mencatat status | T-05 |

## 4. RACI pemilik proses \[USULAN\]

R = mengerjakan, A = pemilik proses (tepat satu per proses), C = dimintai masukan, I = diberi tahu. Peran diambil dari Stakeholder Register: PIC (SH-02), Layanan = staf layanan donatur (SH-04), Admin (SH-07), Notif = pengelola Aplikasi Notifikasi (SH-11), Donatur (SH-08), K1 = Kelompok 1 (SH-09).

| **Proses** | **PIC** | **Layanan** | **Admin** | **Notif** | **Donatur** | **K1** |
|-------|-----|---------|-------|-------|---------|----|
| P-01 | A | C | I | I | R | |
| P-02 | A | C | I | | R | |
| P-03 | C | A/R | I | | C | C |
| P-04 | I | A | | | R | C |
| P-05 | C | A/R | | C | I | C |
| P-06 | A | R | | | I | C |
| P-07 | C | I | A/R | | | |
| P-08 | C | I | | A/R | I | |

## 5. Validasi

| **Peran** | **Nama** | **Catatan koreksi** | **Tanggal** |
|----------------------|-----------|--------------------------------|-----------|
| Pemilik proses BMTZ | | | |
