# Software Requirements Specification (SRS)

Sistem Akun Donatur dan Bukti Donasi · Baitulmal Tazkia

**Table of Contents**

| **Item**            | **Isi**                                                                                                                                                    |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Nomor dokumen       | SRS-ID-001, bagian Akun Donatur (nomor final: isi)                                                                                                         |
| Proyek              | Klaster Inti Donasi: Akun Donatur dan Bukti Donasi (pecahan dari SRS Penerimaan Donasi dan Akun Donatur)                                                   |
| Kelompok            | 2 (pasangan: Kelompok 1, Penerimaan Donasi)                                                                                                                |
| Dosen               | Endy Muhardin                                                                                                                                              |
| Project Manager     | Destri Komalasari                                                                                                                                                     |
| Standar struktur    | ISO/IEC/IEEE 29148:2018, klausul 9.6 (isi SRS), sesuai workbook subbab 7.1; pemetaan bab di 5.5                                                            |
| Versi               | 0.4 (draf)                                                                                                                                                 |
| Tanggal dokumen     | 26 November 2026                                                                                                                                           |
| Penulis             | Eli Nur Aulia (Business Analyst)                                                                                                                           |
| Status              | DRAF. Belum ada sign-off narasumber. Butir bertanda **\[DUGAAN\]** belum dikonfirmasi klien; **\[DRAF\]** belum disetujui final; **\[USULAN\]** usulan tim |
| Sign-off narasumber | Belum (lihat 5.6)                                                                                                                                          |

**Urutan sumber yang berlaku.** Bila dua sumber bertentangan, yang menang adalah (1) notulen pertemuan dengan BMTZ, (2) workbook proyek, (3) dokumen terkait lainnya.

**Data sintetis.** Seluruh data pada contoh acceptance criteria dan mockup adalah data sintetis. Jangan memasukkan data donatur asli sebelum perjanjian pemrosesan data dan NDA ditandatangani.

## 1. Pendahuluan

### 1.1 Purpose (Tujuan)

Dokumen ini menetapkan kebutuhan perangkat lunak untuk subsistem **Akun Donatur dan Bukti Donasi** milik Baitulmal Tazkia (BMTZ). Subsistem ini membantu donatur mengelola akun, melihat riwayat donasi, dan memperoleh bukti donasi, tanpa mengubah pencatatan penerimaan donasi.

Sasaran pembaca dan bagian yang paling perlu dibaca:

| **Pembaca**                 | **Bagian utama**                             |
|-----------------------------|----------------------------------------------|
| Narasumber BMTZ             | 1.2, 1.3, 1.4, 1.5, 3.2.1, 5.6               |
| Pengembang                  | 3.1, 3.2, 3.5, 3.6, 3.8                      |
| Penguji dan Quality Control | Acceptance criteria di 3.2, Bab 4, 5.3 (RTM) |
| Penulis dokumentasi         | 1.3, 1.4, 3.2.1, 3.9                         |

### 1.2 Scope (Ruang Lingkup)

Nama produk: Sistem Akun Donatur dan Bukti Donasi.

**Konteks keseluruhan.** Subsistem ini termasuk modul K1 Penerimaan Donasi dan Akun Donatur. Baitulmal Tazkia mengonfirmasi enam modul, masing-masing dua subsistem (workbook bab 2). Subsistem ini memiliki aplikasi, database, dan deployment sendiri. SRS ini memuat FR umum dan FR-ADBD-01 sampai 15 (FR-ADBD-12 tidak berlaku).

**Dalam lingkup proyek ini:**

- Pendaftaran dan login donatur dengan akun Google atau OTP, serta verifikasi nomor telepon.
- Penyatuan donasi dari berbagai kanal ke akun.
- Riwayat donasi dan status donasi berulang.
- Bukti donasi per transaksi, termasuk booth, dan rekapitulasi tahunan sebagai bukti setor zakat.
- Pilihan tampil dengan nama atau anonim, serta permintaan penghapusan akun.
- Kanal WhatsApp pada Aplikasi Notifikasi Tazkia.

**Dikerjakan kelompok lain:** pencatatan donasi dan peruntukan (Penerimaan Donasi); penagihan donasi berulang (Donasi Berulang). Datanya diakses lewat API.

**Tetap manual:**

- Pemberian donasi oleh donatur lewat kanal.
- Keputusan staf atas donasi yang kecocokannya tidak pasti.

**Di luar lingkup:**

- Pemrosesan pembayaran dan settlement.
- Kabar berkala dan kampanye pemasaran kepada donatur.
- Pesan masuk dan broadcast WhatsApp (tetap di aplikasi CRM).

**Manfaat yang diharapkan \[DUGAAN\]:** bukti donasi cepat tersedia, arsip tertata, donatur dapat menelusuri donasinya, serta dukungan untuk pelaporan dan audit.

### 1.3 Product perspective (Perspektif Produk)

#### 1.3.1 Proses bisnis: kondisi sekarang (as-is) dan usulan (to-be) \[DUGAAN\]

Nama peran, urutan, dan jalur pengecualian belum dikonfirmasi pemilik proses; seluruh alur disusun tim tanpa wawancara. Kondisi sekarang digambar dengan notasi **BPMN 2.0** (draf), usulan dengan flowchart (garis putus-putus: kandidat change request). ID task T-01 sampai T-06 dipakai di RTM (5.3).

**Kondisi sekarang (as-is), BPMN 2.0:**

![gambar](../img/bpmn.png)

*Model BPMN 2.0 kondisi sekarang (draf)*

**Usulan (to-be), flowchart:**

![gambar](../img/flow.png)

*Alur usulan (flowchart)*

| **ID** | **Task**                       | **Pelaksana (belum dikonfirmasi)** | **Kondisi sekarang**           | **Usulan**                                  | **Batas sistem**  |
|--------|--------------------------------|------------------------------------|--------------------------------|---------------------------------------------|-------------------|
| T-01   | Memberi data diri              | Donatur                            | Lewat petugas atau kanal       | Daftar akun dan isi profil sendiri          | Didukung          |
| T-02   | Memeriksa data donatur         | Petugas donasi                     | Pemeriksaan manual             | Validasi isian; petugas meninjau bila perlu | Didukung sebagian |
| T-03   | Mencocokkan donasi dan donatur | Petugas donasi                     | Pencocokan manual              | Penyatuan otomatis bila terverifikasi; antrean bila mirip       | Didukung (CR-01)  |
| T-04   | Membuat bukti donasi           | Petugas donasi                     | Dibuat manual                  | Diterbitkan dari data donasi                | Didukung (CR-01)  |
| T-05   | Menyerahkan bukti              | Petugas donasi                     | Diserahkan atau dikirim manual | Unduh, email, atau WhatsApp                      | Didukung          |
| T-06   | Menyimpan bukti                | Donatur                            | Disimpan sendiri               | Arsip di akun                               | Didukung          |

Kondisi di lapangan belum diobservasi. Waktu siklus dan jumlah bukti per hari belum diukur.

#### 1.3.2 Posisi di antara subsistem lain

Subsistem ini tidak memiliki kelompok hilir (workbook subbab 3.7). Pertukaran data lewat kontrak API atau Kafka, tanpa foreign key lintas subsistem.

| **Arah** | **Pihak** | **Data** |
|----------|---------------------------------------------|------------------------------------------------------------|
| Hulu | Penerimaan Donasi (Kelompok 1) | Catatan donasi beserta data kontaknya |
| Hulu | Donasi Berulang | Status donasi berulang dan signed URL pengelolaan |
| Hulu | Aplikasi Notifikasi Tazkia (sudah berjalan) | Pengiriman OTP dan bukti; subsistem ini menambah kanal WhatsApp |
| Luar | Google, Meta | Login Google; API dan persetujuan template WhatsApp |

Peta ketergantungan belum disetujui kelompok terkait.

### 1.4 Product functions (Fungsi Produk)

Selain empat FR umum (3.2.2), subsistem dibagi menjadi lima modul fungsional (M1 sampai M5).

![gambar](../img/mods.png)

*Peta modul*

| **ID** | **Modul** | **Ringkasan fungsi** | **Use case** | **Kebutuhan** |
|--------|------------------------|-----------------------------------------------|-------------------|------------------------|
| M1 | Akun dan profil | Daftar, masuk, profil, preferensi, hapus akun | UC-01, 02, 03, 14 | FR-ADBD-01, 02, 03, 14 |
| M2 | Riwayat donasi | Penyatuan, riwayat, donasi berulang | UC-04, 05 | FR-ADBD-04, 05 |
| M3 | Bukti donasi | Terbit, unduh, kirim, rekap, verifikasi | UC-06, 07, 08, 13 | FR-ADBD-06, 07, 08, 13 |
| M4 | Pengguna dan hak akses | Login staf, akun, log akses | UC-09, 10, 11 | FR-ADBD-09, 10, 11 |
| M5 | Kanal WhatsApp | Pengirim, template, status kirim | UC-15 | FR-ADBD-15 |

### 1.5 User characteristics (Karakteristik Pengguna)

Disusun dari lane model as-is. Daftar lengkap ada di Stakeholder Register v0.1 (draf, belum divalidasi).

| **Peran** | **Tugas** | **Data yang boleh dibuka** | **Perkiraan akun** | **Status** |
|-------------------------|-----------------------------------------------|----------------------------|--------------------|------------|
| Donatur | Mengelola akun, melihat riwayat, bukti, rekap | Datanya sendiri | (isi) | DUGAAN |
| Petugas donasi | Mengonfirmasi penyatuan, menerbitkan bukti | Donatur, donasi, bukti | (isi) | DUGAAN |
| Admin | Mengelola akun staf, peran, log | Akun dan log | (isi) | DUGAAN |
| Penerima bukti (publik) | Memeriksa keaslian bukti | Ringkasan bukti | 0 | USULAN |

### 1.6 Limitations (Batasan)

- Pengembangan memakai data sintetis sampai perjanjian pemrosesan data dan kerahasiaan ditandatangani.

- Data identitas donatur dan riwayat donasi adalah data pribadi; data keuangan pribadi termasuk data pribadi spesifik menurut UU No. 27 Tahun 2022.

- Kredensial produksi tidak boleh masuk repository.

- Data subsistem lain hanya diakses lewat API.

- Ketentuan akses, bentuk bukti donasi, dan penyimpanan data belum ditetapkan BMTZ.

### 1.7 Assumptions and dependencies (Asumsi dan Ketergantungan)

| **ID** | **Asumsi atau ketergantungan** | **Pemilik** | **Tindakan bila tidak terpenuhi** |
|--------|------------------------------------------------------------|-------------|------------------------------------------------|
| AS-01 | Penerimaan Donasi menyediakan data donasi lewat API | PM | Pakai data contoh; kontrak dirundingkan |
| AS-02 | Donatur memiliki nomor telepon atau akun Google | BA | Staf membantu; kanal lain diajukan sebagai CR |
| AS-03 | Akun tidak wajib untuk berdonasi | BA | Alur donasi dibahas dengan Kelompok 1 |
| AS-04 | Donasi Berulang menyediakan status dan signed URL | PM | Pakai data contoh; tombol Kelola dinonaktifkan |
| AS-05 | Bukti diterbitkan hanya untuk donasi Berhasil | PM, BA | FR-ADBD-06 diubah |
| AS-06 | Perjanjian pemrosesan data dan NDA ditandatangani sebelum data asli dipakai | PM | Tetap data sintetis |
| AS-07 | Meta memverifikasi akun bisnis dan menyetujui template tepat waktu | PM | Tetap memakai email lewat konfigurasi template |
| AS-08 | Tersedia nomor WhatsApp terpisah dari yang dipakai CRM | PM | Kanal WhatsApp ditunda |

### 1.8 Apportioning of requirements (Prioritas Kebutuhan)

Prioritas memakai MoSCoW **\[USULAN\]**.

| **Prioritas** | **Kebutuhan** |
|----------------------|------------------------------------------------------------|
| Must | FR-ADBD-01, 02, 04, 05, 06, 07, 09, 10, 13, 14; NFR-S1, S2, S3, S4, S7, S8, S10, S11, U1, U2 |
| Should | FR-ADBD-03, 11, 15; NFR-P1 sampai P4, S5, S9, U3 |
| Could | FR-ADBD-08 (kandidat CR-02); NFR-S6 |
| Won’t (semester ini) | Pembayaran; kampanye pemasaran; FR-ADBD-12 |

**Kebutuhan yang mengubah proses** dicatat sebagai kandidat change request di 5.4. FR-ADBD-04 dan 06 berlaku setelah CR-01 disetujui.

### 1.9 Pembagian kebutuhan dari SRS gabungan v0.2

Pembagian antara Kelompok 1 dan Kelompok 2 adalah **\[USULAN\]** dan perlu disepakati kedua kelompok.

| **SRS v0.2** | **Kebutuhan** | **Pemilik** | **Di SRS ini** |
|-------------------|-----------------------------------------------|-------------|------------------------------------|
| FR-001 sampai 004 | Terima, validasi, referensi unik, cegah ganda | Kelompok 1 | Datanya dipakai lewat IF-01 |
| FR-005 | Identitas donatur | Kelompok 2 | FR-ADBD-01, 02 |
| FR-006 | Donasi tanpa identitas | Kelompok 1 | Dampak pada FR-ADBD-04, 06 |
| FR-007 | Akun dan riwayat donasi | Kelompok 2 | FR-ADBD-04, 05 |
| FR-008 | Preferensi anonimitas dan kanal | Kelompok 2 | FR-ADBD-03 |
| FR-009 | Data bagi subsistem terkait | Kelompok 1 | Tidak berlaku di sini (FR-ADBD-12) |
| FR-010 | Kesalahan integrasi | Keduanya | IF-01 sampai 05; NFR-S7 |
| FR-011 | Aktivitas audit | Keduanya | FR-ADBD-11 |
| Workbook 3.2 | Bukti, rekap, hapus akun, WhatsApp | Kelompok 2 | FR-ADBD-06, 07, 13, 14, 15 |

## 2. References (Referensi)

| **No.** | **Rujukan** | **Keterangan** |
|---------|------------------------------------------------------------|-----------------------------------------------|
| 1 | Workbook Proyek Kelompok 2, Akun Donatur dan Bukti Donasi, Gasal 2026/2027 | **Acuan utama lingkup dan struktur** |
| 2 | SRS-ID-001 versi 0.2, Penerimaan Donasi dan Akun Donatur, 21 Oktober 2026 | Acuan isi awal |
| 3 | ISO/IEC/IEEE 29148:2018 | Kerangka isi |
| 4 | UU No. 27 Tahun 2022 tentang Pelindungan Data Pribadi | Kepatuhan 3.7 |
| 5 | Catatan wawancara dan hasil survei | **Belum tersedia** |
| 6 | BRS Akun Donatur dan Bukti Donasi v0.2 | Draf |
| 7 | Model BPMN as-is | **Draf** (gambar 1.3.1); file proses-as-is.bpmn, belum divalidasi |
| 8 | Stakeholder register, piagam proyek, risk register, value chain dan RACI v0.1 | Draf, belum divalidasi |
| 9 | Peta ketergantungan antarkelompok | **Belum disepakati** |
| 10 | Contoh bukti donasi dan bukti setor zakat BMTZ | **Belum diterima** |

## 3. Specific requirements (Persyaratan Spesifik)

Kolom **Sumber** menunjuk ke pertemuan klien, workbook, atau elisitasi.

### 3.1 External interfaces (Antarmuka Eksternal)

#### 3.1.1 Antarmuka pengguna

Aplikasi web responsif yang terbaca pada telepon dan laptop. Layar utama per peran:

| **Peran** | **Layar utama** | **Isi** |
|----------------|------------------------------------------------------------|----------------------------|
| Donatur | Masuk, profil, preferensi, riwayat, bukti, rekap, hapus akun | Data milik sendiri |
| Petugas donasi | Antrean konfirmasi, data donatur, bukti | Donatur dan bukti |
| Admin | Kelola akun staf, catatan akses | Akun, peran, riwayat akses |

#### 3.1.1.1 Tema dan tampilan bersama \[USULAN\]

Seluruh mockup memakai kerangka yang sama: navy (#0A2A6B dan \#012766) dan emas (#F0A81C), logo BMTZ pada pojok kiri atas, menu samping, dan bilah atas dengan nama pengguna dan peran. Menu mockup disederhanakan ke lingkup proyek ini; menu final memuat Beranda dan modul sesuai peran. Gambar adalah wireframe usulan dengan data fiktif.

#### 3.1.1.2 Kamus data formulir \[USULAN\]

Seluruh panjang, rentang, dan format adalah usulan tim yang menunggu persetujuan BMTZ.

| **Formulir** | **Field** | **Panjang atau format** | **Wajib** | **Pesan galat** |
|------------------|------------------|--------------------------|----------------------|------------------------------------------|
| Masuk | Nomor telepon | 8 sampai 15 digit | Ya bila tanpa Google | “Nomor telepon tidak valid” |
| Masuk | Kode OTP | 6 digit, berlaku 5 menit | Ya | “Kode OTP salah atau kedaluwarsa” |
| Masuk (staf) | Kode TOTP | 6 digit | Ya | “Kode tidak valid” |
| Pendaftaran | Persetujuan data | Centang | Ya | “Persetujuan wajib diberikan” |
| Profil | Nama | 1 sampai 100 karakter | Ya | “Nama wajib diisi” |
| Profil | Email | Maks. 254, diverifikasi | Tidak | “Email tidak valid atau sudah dipakai” |
| Profil | Alamat | Maks. 255 | Tidak | “Alamat terlalu panjang” |
| Preferensi | Tampil sebagai | Nama atau anonim | Ya | “Pilih preferensi” |
| Preferensi | Cara kirim bukti | Email, WhatsApp, unduh | Ya | “Verifikasi kontak terlebih dahulu” |
| Penyatuan | Alasan (staf) | 1 sampai 500 karakter | Ya | “Alasan wajib diisi” |
| Rekap | Tahun | 4 digit | Ya | “Belum ada donasi zakat” |
| Verifikasi bukti | Kode verifikasi | Tepat 12 karakter | Ya | “Kode verifikasi tidak valid” |
| Akun staf | Email Google | Maks. 254, unik | Ya | “Email tidak valid atau sudah terdaftar” |
| Akun staf | Peran | Petugas donasi, Admin | Ya | “Pilih peran” |

#### 3.1.2 Antarmuka perangkat keras

Tidak ada perangkat keras khusus. Pengguna memakai ponsel atau laptop dengan peramban web modern.

#### 3.1.3 Antarmuka perangkat lunak (antarsubsistem)

Kontrak rinci ditetapkan di dokumen OpenAPI dan tidak disalin ke SRS.

| **ID** | **Pihak** | **Arah** | **Data** | **Pemilik data** | **Volume** | **Batas waktu response** | **Status** |
|--------|----------------------------|------------------|------------------------------------------------------------|-------------------------|------------|--------------------------|---------------|
| IF-01 | Penerimaan Donasi | Masuk | Referensi, nominal, waktu, kanal, status, peruntukan, kontak | Penerimaan Donasi | (isi) | (isi) | MENUNGGU DATA |
| IF-02 | Donasi Berulang | Masuk | Status donasi berulang, signed URL | Donasi Berulang | (isi) | (isi) | MENUNGGU DATA |
| IF-03 | Aplikasi Notifikasi Tazkia | Keluar dan masuk | Message OTP dan bukti; status kirim lewat Kafka | Subsistem ini (message) | (isi) | (isi) | DUGAAN |
| IF-04 | Google (OpenID Connect) | Masuk | ID token | Google | (isi) | (isi) | DUGAAN |
| IF-05 | API WhatsApp Meta | Keluar | Template, nomor tujuan, variabel | Subsistem ini | (isi) | (isi) | DUGAAN |

#### 3.1.4 Antarmuka komunikasi

Seluruh komunikasi klien-server dan antarsubsistem memakai HTTPS. Format pertukaran data API adalah JSON. Pengiriman pesan dan status pengiriman memakai topic Kafka.

### 3.2 Functions (Persyaratan Fungsional)

#### 3.2.1 Model use case

![gambar](../img/uc.png)

*Use case diagram*

| **ID** | **Use case** | **Aktor** | **FR** | **Task** |
|--------|--------------------------------------|--------------------------|------------|------------|
| UC-01 | Mendaftar dan masuk | Donatur | FR-ADBD-01 | T-01 |
| UC-02 | Mengelola profil | Donatur | FR-ADBD-02 | T-01, T-02 |
| UC-03 | Mengatur preferensi | Donatur | FR-ADBD-03 | T-01 |
| UC-04 | Menyatukan donasi ke akun | Sistem, petugas, donatur | FR-ADBD-04 | T-03 |
| UC-05 | Melihat riwayat dan donasi berulang | Donatur, petugas | FR-ADBD-05 | T-06 |
| UC-06 | Menerbitkan bukti donasi | Sistem, petugas | FR-ADBD-06 | T-04 |
| UC-07 | Mengunduh atau mengirim bukti | Donatur, petugas | FR-ADBD-07 | T-05 |
| UC-08 | Memverifikasi keaslian bukti | Penerima bukti | FR-ADBD-08 | T-05 |
| UC-09 | Masuk sebagai staf | Petugas, Admin | FR-ADBD-09 | semua |
| UC-10 | Mengelola akun staf dan peran | Admin | FR-ADBD-10 | semua |
| UC-11 | Melihat log akses | Admin | FR-ADBD-11 | semua |
| UC-12 | Tidak berlaku (tanpa kelompok hilir) | - | FR-ADBD-12 | - |
| UC-13 | Menerbitkan rekapitulasi tahunan | Donatur, petugas | FR-ADBD-13 | T-04 |
| UC-14 | Menghapus akun | Donatur, Admin | FR-ADBD-14 | belum ada |
| UC-15 | Mengirim pesan WhatsApp | Subsistem pengirim | FR-ADBD-15 | T-05 |

**Use case rinci** (alur utama, alternatif, kegagalan; seluruh alur **\[DUGAAN\]**).

**UC-01 Mendaftar dan masuk**

- Prakondisi: donatur punya akun Google atau nomor telepon aktif.
- Alur utama: (1) donatur memilih Google atau nomor telepon; (2) membuktikan identitas; (3) menyetujui penggunaan data; (4) akun dibuat dan sesi aktif.
- Alur alternatif: pengguna Google memverifikasi nomor telepon lewat OTP.
- Alur kegagalan: OTP salah, kedaluwarsa, atau melewati batas kirim; sistem menolak.
- Pascakondisi: donatur masuk dan identitas terverifikasi tercatat.

**UC-02 Mengelola profil**

- Prakondisi: donatur sudah login.

- Alur utama: (1) membuka profil; (2) mengubah data; (3) menyimpan.

- Alur alternatif: ganti email memerlukan verifikasi.

- Alur kegagalan: data tidak valid, sistem menolak.

- Pascakondisi: profil tersimpan.

**UC-03 Mengatur preferensi**

- Prakondisi: donatur sudah masuk.
- Alur utama: (1) membuka preferensi; (2) memilih; (3) menyimpan.
- Alur alternatif: tidak mengubah, default dipakai.
- Alur kegagalan: kanal dipilih tetapi kontaknya belum terverifikasi; sistem menolak.
- Pascakondisi: preferensi tersimpan.

**UC-04 Menyatukan donasi ke akun**

- Prakondisi: data donasi tersedia lewat API.
- Alur utama: (1) sistem menerima donasi; (2) membandingkan dengan identitas terverifikasi; (3) menyatukan dan mencatat dasarnya.
- Alur alternatif: kecocokan mirip masuk antrean; staf atau donatur mengonfirmasi atau menolak.
- Alur kegagalan: donasi sudah milik akun lain; sistem menolak.
- Pascakondisi: donasi tersatukan atau menunggu konfirmasi.

**UC-05 Melihat riwayat dan donasi berulang**

- Prakondisi: donatur sudah masuk.
- Alur utama: (1) membuka riwayat; (2) menyaring; (3) sistem menampilkan daftar, total, dan status berulang.
- Alur alternatif: donatur menekan Kelola dan diarahkan ke Donasi Berulang.
- Alur kegagalan: layanan Donasi Berulang tidak tersedia; riwayat tetap tampil disertai pesan.
- Pascakondisi: riwayat tampil.

**UC-06 Menerbitkan bukti donasi**

- Prakondisi: donasi berstatus Berhasil.
- Alur utama: (1) sistem atau petugas memicu penerbitan; (2) sistem memberi nomor urut; (3) menyimpan salinan isi.
- Alur alternatif: donasi tanpa identitas, bukti atas nama “Hamba Allah” [USULAN].
- Alur kegagalan: status bukan Berhasil; ditolak.
- Pascakondisi: satu bukti tersimpan.

**UC-07 Mengunduh atau mengirim bukti**

- Prakondisi: bukti sudah terbit.
- Alur utama: (1) membuka bukti; (2) mengunduh atau meminta kirim; (3) sistem menerbitkan message ke Kafka; (4) membaca status.
- Alur alternatif: kanal WhatsApp belum berjalan; dikirim lewat email.
- Alur kegagalan: pengiriman gagal; status tidak menjadi Terkirim.
- Pascakondisi: donatur menerima bukti.

**UC-08 Memverifikasi keaslian bukti**

- Prakondisi: memiliki kode verifikasi.

- Alur utama: (1) memasukkan kode; (2) sistem menampilkan ringkasan.

- Alur alternatif: bukti dibatalkan, tampil “Dibatalkan”.

- Alur kegagalan: kode tidak dikenal, “tidak ditemukan”.

- Pascakondisi: tidak ada data berubah.

**UC-09 Masuk sebagai staf**

- Prakondisi: staf punya akun Google.
- Alur utama: (1) masuk dengan Google; (2) memasukkan kode TOTP; (3) menu tampil sesuai peran.
- Alur alternatif: akun belum terdaftar; hanya halaman kosong.
- Alur kegagalan: token atau kode tidak sah; ditolak.
- Pascakondisi: akses sesuai peran.

**UC-10 Mengelola akun staf dan peran**

- Prakondisi: berperan Admin.
- Alur utama: (1) menambah email staf; (2) menetapkan peran; (3) menyimpan; (4) pengenal Google dicatat saat staf pertama masuk.
- Alur alternatif: Admin menonaktifkan akun.
- Alur kegagalan: non-Admin; ditolak 403.
- Pascakondisi: akun tersimpan.

**UC-11 Melihat log akses**

- Prakondisi: berperan Admin.

- Alur utama: (1) membuka log; (2) menyaring; (3) sistem menampilkan siapa membuka data siapa dan kapan.

- Alur alternatif: hasil kosong.

- Alur kegagalan: non-Admin ditolak.

- Pascakondisi: log tidak dapat diubah.

**UC-13 Menerbitkan rekapitulasi tahunan**

- Prakondisi: donatur punya donasi zakat pada tahun itu.
- Alur utama: (1) memilih tahun; (2) sistem menyusun rekap; (3) memberi nomor; (4) menyimpan dan menampilkan.
- Alur alternatif: petugas menerbitkan atas permintaan donatur.
- Alur kegagalan: tidak ada donasi zakat; tidak diterbitkan.
- Pascakondisi: rekap tersimpan.

**UC-14 Menghapus akun**

- Prakondisi: donatur sudah masuk.
- Alur utama: (1) meminta hapus; (2) mengonfirmasi ulang dengan OTP atau Google; (3) sistem memutus hubungan dan menutup sesi.
- Alur alternatif: Admin memproses permintaan yang disampaikan langsung [USULAN].
- Alur kegagalan: konfirmasi gagal; akun tidak dihapus.
- Pascakondisi: akun tidak dapat dipakai; catatan donasi tetap.

**UC-15 Mengirim pesan WhatsApp**

- Prakondisi: akun bisnis, nomor, dan template disetujui Meta.
- Alur utama: (1) message masuk topic; (2) template diisi; (3) dikirim lewat API Meta; (4) status diterbitkan.
- Alur alternatif: kanal belum siap; konfigurasi template tetap memakai email.
- Alur kegagalan: Meta menolak atau gagal; status gagal diterbitkan.
- Pascakondisi: status pengiriman tersedia.

#### 3.2.2 Kebutuhan fungsional per modul

Setiap FR proyek dilengkapi mockup dan Test Scenario ringkas. Dokumen FR dan Test Scenario tersedia terpisah.

#### FR umum (dipakai bersama seluruh proyek)

Empat FR umum adalah usulan tampilan bersama yang perlu disepakati. FR umum **tidak memakai kode proyek**. Isi dan tampilan di bawah adalah usulan yang diselaraskan dengan wireframe tampilan bersama.

##### FR Umum 1: Layar login \[DRAF\]

| **Atribut** | **Isi**                                                                                                |
|-------------|--------------------------------------------------------------------------------------------------------|
| Prioritas   | Must                                                                                                   |
| Aktor       | Semua pengguna                                                                                         |
| Deskripsi | Donatur masuk dengan akun Google atau OTP nomor telepon. Staf masuk dengan akun Google lalu TOTP. Tidak ada kata sandi. |

**Mockup**

![gambar](../img/umum-1-login.png)

*Layar login*

| **Elemen** | **Jenis** | **Perilaku** |
|---------------------|-----------|----------------------|
| Masuk dengan Google | Tombol | Donatur dan staf |
| Nomor telepon, OTP | Kolom | Donatur |
| Kode TOTP | Kolom | Staf, setelah Google |

Pesan galat: “Gagal masuk. Periksa lalu coba lagi.”

**Acceptance criteria**

- **Given** akun donatur aktif dan OTP benar, **When** menekan Masuk, **Then** beranda donatur terbuka.
- **Given** akun dinonaktifkan, **When** pemilik mencoba masuk, **Then** sistem menolak.
- **Given** OTP atau ID token tidak sah, **When** dikirim ke server, **Then** sistem menampilkan pesan umum tanpa membuat sesi.

##### FR Umum 2: Beranda setelah login \[DRAF\]

| **Atribut** | **Isi**                                              |
|-------------|------------------------------------------------------|
| Prioritas   | Must                                                 |
| Aktor       | Semua pengguna                                       |
| Deskripsi   | Beranda memuat ringkasan dan menu sesuai peran akun. |

**Mockup**

![gambar](../img/umum-2-beranda.png)

*Beranda*

| **Elemen**        | **Jenis** | **Perilaku**                        |
|-------------------|-----------|-------------------------------------|
| Menu samping      | Navigasi  | Hanya menu yang boleh dipakai peran |
| Kartu ringkasan   | Angka     | Menyesuaikan peran dan modul        |
| Aktivitas terbaru | Daftar    | Data sesuai hak akses               |
| Bilah atas        | Profil    | Nama dan peran; Keluar              |

**Acceptance criteria**

- **Given** pengguna berperan Donatur, **When** pengguna login, **Then** menu hanya memuat data miliknya.

- **Given** pengguna berperan Admin, **When** pengguna login, **Then** menu memuat kelola akun dan catatan akses.

##### FR Umum 3: Tampilan tabel \[DRAF\]

| **Atribut** | **Isi**                                                                                    |
|-------------|--------------------------------------------------------------------------------------------|
| Prioritas   | Must                                                                                       |
| Aktor       | Semua pengguna                                                                             |
| Deskripsi   | Tampilan standar daftar data: pencarian, saring, tambah data, tabel, status, dan paginasi. |

**Mockup**

![gambar](../img/umum-3-tabel.png)

*Tampilan tabel*

| **Elemen**            | **Jenis**         | **Perilaku**                        |
|-----------------------|-------------------|-------------------------------------|
| Cari, Status, Periode | Kolom dan pilihan | Menyaring tabel                     |
| Tambah Data           | Tombol            | Membuka formulir                    |
| Tabel                 | Tabel             | Tampil “tidak ada data” bila kosong |
| Lihat, Ubah           | Tautan            | Hanya peran berhak                  |
| Paginasi              | Navigasi          | Berpindah halaman                   |

Pesan galat: “Tidak ada data.”

**Acceptance criteria**

- **Given** terdapat 48 data, **When** pengguna membuka tabel, **Then** sistem menampilkan enam data per halaman beserta jumlah total.

- **Given** filter tidak cocok, **When** pengguna menyaring, **Then** sistem menampilkan “tidak ada data”.

##### FR Umum 4: Tampilan formulir input \[DRAF\]

| **Atribut** | **Isi**                                                                                                           |
|-------------|-------------------------------------------------------------------------------------------------------------------|
| Prioritas   | Must                                                                                                              |
| Aktor       | Semua pengguna                                                                                                    |
| Deskripsi   | Tampilan standar mengisi data: kolom wajib bertanda bintang, pesan galat di bawah kolom, tombol Simpan dan Batal. |

**Mockup**

![gambar](../img/umum-4-formulir.png)

*Tampilan formulir input*

| **Elemen**           | **Jenis**              | **Perilaku**                    |
|----------------------|------------------------|---------------------------------|
| Kolom isian          | Teks, pilihan, tanggal | Wajib bertanda \*               |
| Keterangan, Lampiran | Teks, berkas           | Opsional                        |
| Simpan, Batal        | Tombol                 | Simpan memeriksa; Batal kembali |

Pesan galat: “Kolom wajib diisi.”

**Acceptance criteria**

- **Given** kolom wajib kosong, **When** pengguna menekan Simpan, **Then** sistem menolak dan menyebut kolom yang kurang.

- **Given** seluruh kolom valid, **When** pengguna menekan Simpan, **Then** sistem menyimpan dan kembali ke tabel.

#### Modul M1: Akun dan profil

##### FR-ADBD-01 Pendaftaran dan login donatur \[DUGAAN\]

| **Atribut** | **Isi** |
|-------------|------------------------------------------------------------|
| Prioritas | Must |
| Sumber | Workbook 3.2, 3.7 |
| Aktor | Donatur |
| Deskripsi | Donatur masuk dengan akun Google atau OTP ke nomor telepon, tanpa kata sandi. Donatur yang masuk dengan Google memverifikasi nomor teleponnya satu kali lewat OTP sebelum donasi bernomor itu disatukan. Akun Google dikenali dari pengenal tetapnya, bukan dari alamat email. Satu akun memuat satu identitas Google serta beberapa nomor telepon dan email terverifikasi |
| Task proses | T-01 |

**Acceptance criteria**

- **Given** nomor belum terdaftar dan OTP benar, **When** donatur menyetujui penggunaan data, **Then** akun dibuat dengan nomor terverifikasi.
- **Given** donatur masuk dengan Google dan nomornya belum diverifikasi, **When** data donasi bernomor itu tersedia, **Then** donasi belum disatukan.
- **Given** sudah 3 permintaan OTP dalam 15 menit [USULAN], **When** donatur meminta lagi, **Then** sistem menolak.

**Mockup**

![gambar](../img/adbd-01-daftar.png)

*Masuk atau daftar*

| **Elemen** | **Jenis** | **Perilaku** |
|--------------------------|------------------|-----------------------------------|
| Masuk dengan Google | Tombol | Memakai OpenID Connect |
| Nomor telepon, Kirim OTP | Kolom dan tombol | Jumlah kirim dibatasi |
| Kode OTP | Kolom | 6 digit, berlaku 5 menit [USULAN] |
| Persetujuan data | Centang | Wajib saat akun baru |

Pesan galat: “Kode OTP salah atau kedaluwarsa.”; “Terlalu banyak permintaan. Coba lagi nanti.”

**Test Scenario ringkas** (TS-ADBD-01)

| **Teknik** | **Skenario** | **Hasil diharapkan** |
|----------------------|-------------------------------------------|------------------------|
| Benar (Right) | OTP benar pada nomor baru | Akun dibuat |
| Benar (Right) | OTP salah | Ditolak |
| Kebalikan (Inverse) | Keluar lalu masuk lagi | Akun yang sama terbuka |
| Batas (Boundary) | OTP dipakai pada menit ke-6 | Ditolak kedaluwarsa |
| Batas (Boundary) | Permintaan OTP ke-4 dalam 15 menit | Ditolak |
| Batas (Boundary) | Persetujuan tidak dicentang | Akun tidak dibuat |
| Silang (Cross-check) | Email akun Google berubah, pengenal tetap | Akun yang sama terbuka |

##### FR-ADBD-02 Pengelolaan profil donatur \[DUGAAN\]

| **Atribut** | **Isi**                                                             |
|-------------|---------------------------------------------------------------------|
| Prioritas   | Must                                                                |
| Sumber      | v0.2 FR-005                                                         |
| Aktor       | Donatur                                                             |
| Deskripsi | Donatur melihat dan mengubah data yang disetujui, serta menambah nomor telepon atau email yang diverifikasi dengan OTP; perubahan dicatat |
| Task proses | T-01, T-02                                                          |

**Acceptance criteria**

- **Given** donatur sudah login, **When** mengubah alamat dan menyimpan, **Then** perubahan tersimpan.

- **Given** email atau nomor baru belum diverifikasi, **When** donatur menyimpan, **Then** data lama tetap berlaku.

**Mockup**

![gambar](../img/adbd-02-profil.png)

*Profil donatur*

| **Elemen**    | **Jenis** | **Perilaku**      |
|---------------|-----------|-------------------|
| Data diri     | Kolom     | Sesuai 3.1.1.2    |
| Simpan, Batal | Tombol    | Perubahan dicatat |

Pesan galat: “Nama wajib diisi.”; “Nomor telepon tidak valid.”

**Test Scenario ringkas** (TS-ADBD-02)

| **Teknik**           | **Skenario**                                  | **Hasil diharapkan**       |
|----------------------|-----------------------------------------------|----------------------------|
| Benar (Right)        | Ubah nomor telepon                            | Tersimpan                  |
| Benar (Right)        | Kosongkan nama                                | Ditolak                    |
| Kebalikan (Inverse)  | Simpan lalu buka kembali                      | Isi sama                   |
| Batas (Boundary)     | Telepon 7 digit                               | Ditolak                    |
| Batas (Boundary)     | Telepon 8 digit                               | Diterima                   |
| Batas (Boundary)     | Telepon 16 digit                              | Ditolak                    |
| Silang (Cross-check) | Data tersimpan dibandingkan atribut disetujui | Tidak ada atribut tambahan |

##### FR-ADBD-03 Preferensi anonimitas dan pengiriman \[DUGAAN\]

| **Atribut** | **Isi** |
|-------------|------------------------------------------------------------|
| Prioritas | Should |
| Sumber | Workbook 3.2; v0.2 FR-008 |
| Aktor | Donatur |
| Deskripsi | Donatur memilih tampil dengan nama atau anonim, serta cara menerima bukti. Anonim mengatur tampilan tanpa menghapus data internal. Arti anonim bagi staf belum dikonfirmasi |
| Task proses | T-01 |

**Acceptance criteria**

- **Given** donatur memilih anonim, **When** namanya akan tampil pada daftar umum, **Then** tampil “Hamba Allah”.
- **Given** preferensi belum diisi, **When** sistem memakainya, **Then** default tampil dengan nama [USULAN].
- **Given** belum ada nomor terverifikasi, **When** donatur memilih WhatsApp, **Then** sistem menolak.

**Mockup**

![gambar](../img/adbd-03-preferensi.png)

*Preferensi*

| **Elemen** | **Jenis** | **Perilaku** |
|---------------------|-----------|--------------------------------|
| Tampil sebagai | Pilihan | Nama atau anonim |
| Kirim bukti melalui | Pilihan | Email, WhatsApp, unduh sendiri |
| Simpan, Batal | Tombol | Menyimpan preferensi |

Pesan galat: “Verifikasi kontak untuk kanal ini terlebih dahulu.”

**Test Scenario ringkas** (TS-ADBD-03)

| **Teknik** | **Skenario** | **Hasil diharapkan** |
|----------------------|------------------------------------------|-------------------------------|
| Benar (Right) | Pilih anonim lalu simpan | Tersimpan |
| Benar (Right) | Pilih WhatsApp tanpa nomor terverifikasi | Ditolak |
| Kebalikan (Inverse) | Ubah anonim lalu kembalikan | Tampilan kembali memakai nama |
| Silang (Cross-check) | Donasi anonim dilihat di data internal | Data asli tetap ada |

##### FR-ADBD-14 Penghapusan akun donatur \[DUGAAN\]

| **Atribut** | **Isi** |
|-------------|------------------------------------------------------------|
| Prioritas | Must |
| Sumber | Workbook 3.2, 3.6, 3.7 |
| Aktor | Donatur, Admin |
| Deskripsi | Donatur dapat meminta akunnya dihapus. Sistem memutus hubungan akun dengan catatan donasi dan menghapus identitas login. Catatan donasi di Penerimaan Donasi tetap ada. Masa simpan bukti yang sudah terbit mengikuti ketentuan audit (belum dikonfirmasi) |
| Task proses | Belum ada pada model as-is |

**Acceptance criteria**

- **Given** donatur mengonfirmasi penghapusan, **When** sistem memproses, **Then** akun tidak dapat dipakai masuk.
- **Given** akun sudah dihapus, **When** data donasi sumber diperiksa, **Then** catatan donasi tetap ada.
- **Given** konfirmasi ulang gagal, **When** permintaan dikirim, **Then** akun tidak berubah.

**Mockup**

![gambar](../img/adbd-14-hapus.png)

*Hapus akun*

| **Elemen** | **Jenis** | **Perilaku** |
|-------------------|-----------------|-------------------------------|
| Penjelasan dampak | Teks | Apa yang dihapus dan disimpan |
| Konfirmasi ulang | OTP atau Google | Wajib |
| Hapus akun, Batal | Tombol | Mencatat permintaan |

Pesan galat: “Konfirmasi gagal. Akun tidak dihapus.”

**Test Scenario ringkas** (TS-ADBD-14)

| **Teknik** | **Skenario** | **Hasil diharapkan** |
|----------------------|-------------------------------------------|---------------------------------------------------------|
| Benar (Right) | Hapus dengan konfirmasi benar | Tidak dapat masuk ke akun lama |
| Benar (Right) | Konfirmasi salah | Akun tetap |
| Kebalikan (Inverse) | Daftar ulang dengan nomor sama | Akun baru; donasi tidak otomatis memakai penyatuan lama |
| Silang (Cross-check) | Jumlah catatan donasi sebelum dan sesudah | Sama |

#### Modul M2: Riwayat donasi

##### FR-ADBD-04 Penyatuan donasi ke akun \[DUGAAN\]

| **Atribut** | **Isi** |
|-------------|------------------------------------------------------------|
| Prioritas | Must |
| Sumber | Workbook 3.2, 3.7; v0.2 FR-007 |
| Aktor | Sistem, petugas donasi, donatur |
| Deskripsi | Sistem menyatukan donasi dari semua kanal secara bertingkat. Email terverifikasi (Google atau OTP) atau nomor telepon terverifikasi OTP yang sama disatukan otomatis. Kecocokan yang hanya mirip masuk antrean konfirmasi staf atau donatur. Setiap penyatuan menyimpan dasar kecocokannya dan dapat dibatalkan |
| Task proses | T-03 |

**Acceptance criteria**

- **Given** donasi bernomor sama dengan nomor terverifikasi akun, **When** data diterima, **Then** donasi disatukan dengan dasar “nomor terverifikasi”.
- **Given** hanya nama yang mirip, **When** data diterima, **Then** donasi tidak disatukan otomatis.
- **Given** penyatuan keliru, **When** petugas membatalkannya dengan alasan, **Then** donasi hilang dari riwayat dan pembatalan tercatat.

**Mockup**

![gambar](../img/adbd-04-penautan.png)

*Antrean konfirmasi*

| **Elemen** | **Jenis** | **Perilaku** |
|----------------|-----------|----------------------------------------|
| Antrean | Tabel | Donasi, kandidat akun, dasar kecocokan |
| Satukan, Tolak | Tautan | Alasan wajib bagi petugas |
| Batalkan | Tautan | Melepas penyatuan |

Pesan galat: “Donasi sudah disatukan ke akun lain.”; “Alasan wajib diisi.”

**Test Scenario ringkas** (TS-ADBD-04)

| **Teknik** | **Skenario** | **Hasil diharapkan** |
|----------------------|--------------------------------------------|--------------------------------------|
| Benar (Right) | Email terverifikasi sama | Disatukan otomatis |
| Benar (Right) | Nomor terverifikasi sama | Disatukan otomatis |
| Benar (Right) | Nomor sama tetapi belum diverifikasi | Tidak disatukan |
| Benar (Right) | Hanya nama mirip | Tidak disatukan otomatis |
| Kebalikan (Inverse) | Penyatuan dibatalkan | Donasi keluar dari riwayat; tercatat |
| Batas (Boundary) | Satu nomor cocok dengan dua akun | Masuk antrean |
| Silang (Cross-check) | Donasi tersatukan dibandingkan data sumber | Kontak cocok dengan dasar tercatat |

##### FR-ADBD-05 Riwayat donasi dan status donasi berulang \[DUGAAN\]

| **Atribut** | **Isi** |
|-------------|------------------------------------------------------------|
| Prioritas | Must |
| Sumber | Workbook 3.2, 3.5, 3.7 |
| Aktor | Donatur, petugas donasi |
| Deskripsi | Sistem menampilkan donasi milik akun dengan filter periode dan peruntukan, total donasi Berhasil, serta status donasi berulang. Tombol Kelola meminta signed URL berumur singkat ke subsistem Donasi Berulang lalu mengarahkan donatur tanpa login ulang |
| Task proses | T-06 |

**Acceptance criteria**

- **Given** donasi Berhasil Rp100.000 dan Rp250.000, **When** donatur membuka riwayat, **Then** tampil 2 donasi dan total Rp350.000.
- **Given** donatur A sudah masuk, **When** membuka riwayat donatur B, **Then** ditolak 403.
- **Given** ada donasi berulang aktif, **When** donatur menekan Kelola, **Then** halaman pengelolaan terbuka lewat signed URL tanpa login ulang.

**Mockup**

![gambar](../img/adbd-05-riwayat.png)

*Riwayat donasi*

| **Elemen** | **Jenis** | **Perilaku** |
|-------------------------|------------------|-----------------------------|
| Periode, Peruntukan | Filter | Awal tidak melewati akhir |
| Tabel | Baca saja | Donasi milik sendiri |
| Donasi berulang, Kelola | Kartu dan tombol | Status dari Donasi Berulang |

Pesan galat: “Tanggal akhir tidak boleh sebelum tanggal awal.”; “Pengelolaan donasi berulang sedang tidak tersedia.”

**Test Scenario ringkas** (TS-ADBD-05)

| **Teknik** | **Skenario** | **Hasil diharapkan** |
|----------------------|-------------------------------------------|-----------------------------|
| Benar (Right) | Buka riwayat | Tampil donasi milik sendiri |
| Benar (Right) | Buka riwayat orang lain | Ditolak 403 |
| Benar (Right) | Tekan Kelola | Diarahkan tanpa login ulang |
| Kebalikan (Inverse) | Filter lalu kosongkan | Seluruh data kembali |
| Batas (Boundary) | Akhir sebelum awal | Ditolak |
| Batas (Boundary) | Layanan Donasi Berulang mati | Riwayat tetap tampil |
| Silang (Cross-check) | Total dibandingkan data Penerimaan Donasi | Sama |

#### Modul M3: Bukti donasi

##### FR-ADBD-06 Penerbitan bukti donasi \[DUGAAN\]

| **Atribut** | **Isi** |
|-------------|------------------------------------------------------------|
| Prioritas | Must |
| Sumber | Workbook 3.2, 3.7 |
| Aktor | Sistem, petugas donasi |
| Deskripsi | Sistem menerbitkan satu bukti resmi per transaksi Berhasil dari semua kanal, termasuk donasi di booth. Bukti diberi nomor urut dan disimpan apa adanya; isinya tidak pernah dibuat ulang dari data terkini. Bila donasi dibatalkan atau dikembalikan, status bukti menjadi Dibatalkan [USULAN] |
| Task proses | T-04 |

**Acceptance criteria**

- **Given** donasi Berhasil Rp100.000 dari booth, **When** bukti diterbitkan, **Then** bukti memuat nomor urut dan Rp100.000.
- **Given** bukti sudah terbit lalu nama donatur diubah, **When** bukti dibuka, **Then** isinya tetap seperti saat terbit.
- **Given** donasi berstatus Menunggu, **When** penerbitan diminta, **Then** sistem menolak.

**Mockup**

![gambar](../img/adbd-06-bukti.png)

*Bukti donasi*

| **Elemen** | **Jenis** | **Perilaku** |
|--------------|-----------|---------------------|
| Isi bukti | Baca saja | Salinan saat terbit |
| Unduh, Kirim | Tombol | Lihat FR-ADBD-07 |

Pesan galat: “Bukti hanya untuk donasi berstatus Berhasil.”

**Test Scenario ringkas** (TS-ADBD-06)

| **Teknik** | **Skenario** | **Hasil diharapkan** |
|----------------------|------------------------------------------------|--------------------------|
| Benar (Right) | Terbitkan untuk donasi Berhasil | Bukti bernomor dibuat |
| Benar (Right) | Terbitkan untuk donasi Gagal | Ditolak |
| Benar (Right) | Donasi dari booth | Bukti dibuat |
| Kebalikan (Inverse) | Donasi dikembalikan | Bukti menjadi Dibatalkan |
| Batas (Boundary) | Dua permintaan bersamaan | Satu bukti, satu nomor |
| Batas (Boundary) | Data profil diubah setelah terbit | Bukti tidak berubah |
| Silang (Cross-check) | Isi bukti dibandingkan data donasi saat terbit | Sama persis |

##### FR-ADBD-07 Unduh dan kirim bukti \[DUGAAN\]

| **Atribut** | **Isi** |
|-------------|------------------------------------------------------------|
| Prioritas | Must |
| Sumber | Workbook 3.2, 3.5 |
| Aktor | Donatur, petugas donasi |
| Deskripsi | Bukti dapat diunduh sebagai PDF dan dikirim lewat Aplikasi Notifikasi Tazkia dengan email, serta WhatsApp setelah kanalnya berjalan. Status pengiriman dibaca dari topic status |
| Task proses | T-05 |

**Acceptance criteria**

- **Given** bukti Terbit, **When** donatur menekan Unduh PDF, **Then** berkas PDF terunduh.
- **Given** topic status melaporkan gagal, **When** sistem membacanya, **Then** status tidak menjadi Terkirim dan kegagalan dicatat.
- **Given** donatur lain sudah masuk, **When** mengunduh bukti, **Then** ditolak 403.

**Mockup**

![gambar](../img/adbd-06-bukti.png)

*Unduh dan kirim*

| **Elemen** | **Jenis** | **Perilaku** |
|------------|-----------|-------------------------|
| Unduh PDF | Tombol | Pemilik atau petugas |
| Kirim | Tombol | Ke kontak terverifikasi |

Pesan galat: “Pengiriman gagal, coba lagi.”

**Test Scenario ringkas** (TS-ADBD-07)

| **Teknik** | **Skenario** | **Hasil diharapkan** |
|----------------------|-------------------------------------|------------------------------------|
| Benar (Right) | Kirim ke email terverifikasi | Message terbit dan status Terkirim |
| Benar (Right) | Donatur lain mengunduh | Ditolak 403 |
| Kebalikan (Inverse) | Unduh lalu bandingkan | Sama dengan bukti tersimpan |
| Batas (Boundary) | Tanpa kontak terverifikasi | Hanya unduh |
| Batas (Boundary) | Kirim ulang | Tercatat, nomor bukti sama |
| Silang (Cross-check) | Log kirim dibandingkan topic status | Sama |

##### FR-ADBD-08 Verifikasi keaslian bukti \[USULAN, kandidat CR-02\]

| **Atribut** | **Isi**                                                                                                                        |
|-------------|--------------------------------------------------------------------------------------------------------------------------------|
| Prioritas   | Could                                                                                                                          |
| Sumber      | Usulan tim                                                                                                                     |
| Aktor       | Penerima bukti                                                                                                                 |
| Deskripsi   | Siapa pun yang memiliki kode dapat memeriksa keabsahan; hasil hanya memuat status, nomor, tanggal, dan nominal tanpa identitas |
| Task proses | T-05                                                                                                                           |

**Acceptance criteria**

- **Given** kode sah, **When** dimasukkan, **Then** tampil “Sah” tanpa nama donatur.

- **Given** kode tidak dikenal, **When** dimasukkan, **Then** tampil “tidak ditemukan”.

**Mockup**

![gambar](../img/adbd-08-verifikasi.png)

*Verifikasi bukti*

| **Elemen**      | **Jenis** | **Perilaku**          |
|-----------------|-----------|-----------------------|
| Kode verifikasi | Kolom     | 12 karakter           |
| Periksa         | Tombol    | Menampilkan ringkasan |

Pesan galat: “Kode verifikasi tidak valid.”

**Test Scenario ringkas** (TS-ADBD-08)

| **Teknik**           | **Skenario**                    | **Hasil diharapkan** |
|----------------------|---------------------------------|----------------------|
| Benar (Right)        | Kode sah                        | “Sah”                |
| Benar (Right)        | Kode acak                       | “Tidak ditemukan”    |
| Kebalikan (Inverse)  | Bukti dibatalkan lalu diperiksa | “Dibatalkan”         |
| Batas (Boundary)     | 11 karakter                     | Ditolak              |
| Batas (Boundary)     | 12 karakter                     | Diproses             |
| Batas (Boundary)     | 13 karakter                     | Ditolak              |
| Silang (Cross-check) | Hasil dibandingkan data bukti   | Sama                 |

##### FR-ADBD-13 Rekapitulasi donasi tahunan \[DUGAAN\]

| **Atribut** | **Isi** |
|-------------|------------------------------------------------------------|
| Prioritas | Must |
| Sumber | Workbook 3.2 |
| Aktor | Donatur, petugas donasi |
| Deskripsi | Sistem menerbitkan rekapitulasi per tahun sebagai bukti setor zakat, memuat daftar donasi zakat Berhasil dan totalnya. Rekap yang sudah terbit disimpan apa adanya dengan nomor urut. Format yang diterima kantor pajak belum dikonfirmasi |
| Task proses | T-04 |

**Acceptance criteria**

- **Given** donasi zakat Rp250.000 dan Rp750.000 pada 2026 serta infak Rp100.000, **When** rekap zakat 2026 diterbitkan, **Then** total Rp1.000.000.
- **Given** tidak ada donasi zakat, **When** rekap diminta, **Then** sistem menolak.
- **Given** rekap sudah terbit, **When** dibuka lagi, **Then** isinya sama dengan saat terbit.

**Mockup**

![gambar](../img/adbd-13-rekap.png)

*Rekapitulasi tahunan*

| **Elemen** | **Jenis** | **Perilaku** |
|----------------------|-----------|----------------------------------|
| Tahun | Pilihan | Tahun yang memiliki donasi zakat |
| Terbitkan, Unduh PDF | Tombol | Menyimpan salinan isi |

Pesan galat: “Belum ada donasi zakat pada tahun ini.”

**Test Scenario ringkas** (TS-ADBD-13)

| **Teknik** | **Skenario** | **Hasil diharapkan** |
|----------------------|---------------------------------------------|----------------------|
| Benar (Right) | Terbitkan rekap tahun berisi zakat | Total benar |
| Benar (Right) | Tahun tanpa zakat | Ditolak |
| Batas (Boundary) | Donasi 31 Desember 23.59 | Masuk tahun tersebut |
| Batas (Boundary) | Donasi dibatalkan sebelum terbit | Tidak dihitung |
| Silang (Cross-check) | Total rekap dibandingkan jumlah bukti zakat | Sama |

#### Modul M4: Pengguna, peran, dan hak akses

##### FR-ADBD-09 Pembatasan akses dan login staf \[DRAF\]

| **Atribut** | **Isi** |
|-------------|------------------------------------------------------------|
| Prioritas | Must |
| Sumber | Workbook Lampiran A; v0.2 NFR-001 |
| Aktor | Semua peran |
| Deskripsi | Staf masuk dengan akun Google (OpenID Connect) lalu verifikasi TOTP. ID token divalidasi di server. Akun yang belum terdaftar hanya melihat halaman awal kosong. Data dibatasi menurut peran dan kepemilikan, diperiksa terpusat di server |
| Task proses | T-01 sampai T-06 |

**Acceptance criteria**

- **Given** akun Google belum terdaftar pada aplikasi, **When** pengguna masuk, **Then** hanya tampil halaman awal kosong.
- **Given** pengguna berperan Donatur, **When** memanggil API kelola akun, **Then** ditolak 403.
- **Given** kode TOTP salah, **When** staf mengirimnya, **Then** akses tidak diberikan.

**Mockup**

![gambar](../img/adbd-09-ditolak.png)

*Akses ditolak*

| **Elemen** | **Jenis** | **Perilaku** |
|------------|-----------|----------------------|
| Pesan 403 | Teks | Tanpa rincian teknis |
| Kembali | Tombol | Ke beranda |

Pesan galat: “Anda tidak berhak membuka halaman ini.”

**Test Scenario ringkas** (TS-ADBD-09)

| **Teknik** | **Skenario** | **Hasil diharapkan** |
|----------------------|------------------------------|----------------------|
| Benar (Right) | Staf terdaftar, TOTP benar | Menu sesuai peran |
| Benar (Right) | Akun Google tidak terdaftar | Halaman kosong |
| Benar (Right) | Donatur memanggil API admin | Ditolak 403 |
| Batas (Boundary) | ID token kedaluwarsa | Ditolak |
| Batas (Boundary) | ID token untuk audience lain | Ditolak |
| Silang (Cross-check) | Hak di API dibandingkan menu | Sama |

##### FR-ADBD-10 Pengelolaan akun staf dan peran \[DRAF\]

| **Atribut** | **Isi** |
|-------------|------------------------------------------------------------|
| Prioritas | Must |
| Sumber | Workbook Lampiran A; v0.2 NFR-001 |
| Aktor | Admin |
| Deskripsi | Admin mendaftarkan akun Google staf pada tabel pengguna aplikasi, menetapkan peran, dan menonaktifkan akun. Aplikasi tidak menyimpan kata sandi |
| Task proses | T-01 sampai T-06 |

**Acceptance criteria**

- **Given** Admin mengisi email staf dan peran, **When** menyimpan, **Then** staf dapat masuk sesuai peran.
- **Given** akun dinonaktifkan, **When** staf mencoba masuk, **Then** ditolak.
- **Given** non-Admin, **When** membuat akun, **Then** ditolak 403.

**Mockup**

![gambar](../img/adbd-10-akun.png)

*Kelola akun staf*

| **Elemen** | **Jenis** | **Perilaku** |
|---------------------|-----------|----------------------|
| Tabel akun | Tabel | Email, peran, status |
| Email Google, Peran | Kolom | Wajib |
| Simpan, Batal | Tombol | Hanya Admin |

Pesan galat: “Email tidak valid atau sudah terdaftar.”; “Pilih peran.”

**Test Scenario ringkas** (TS-ADBD-10)

| **Teknik** | **Skenario** | **Hasil diharapkan** |
|----------------------|-----------------------------------------|----------------------|
| Benar (Right) | Tambah staf | Tersimpan |
| Benar (Right) | Email sudah terdaftar | Ditolak |
| Kebalikan (Inverse) | Nonaktifkan lalu aktifkan | Dapat masuk lagi |
| Batas (Boundary) | Peran kosong | Ditolak |
| Silang (Cross-check) | Daftar akun dibandingkan tabel pengguna | Sama |

##### FR-ADBD-11 Log akses data pribadi \[DUGAAN\]

| **Atribut** | **Isi**                                                                             |
|-------------|-------------------------------------------------------------------------------------|
| Prioritas   | Should                                                                              |
| Sumber      | v0.2 FR-011                                                                         |
| Aktor       | Admin                                                                               |
| Deskripsi   | Sistem mencatat siapa membuka atau mengubah data donatur atau bukti siapa dan kapan |
| Task proses | T-01 sampai T-06                                                                    |

**Acceptance criteria**

- **Given** petugas membuka profil donatur, **When** Admin membuka log, **Then** tercatat pengguna, donatur, dan waktu.

**Mockup**

![gambar](../img/adbd-11-catatan-akses.png)

*Catatan akses*

| **Elemen**    | **Jenis**        | **Perilaku**                    |
|---------------|------------------|---------------------------------|
| Filter        | Pilihan, rentang | Menyaring                       |
| Tabel catatan | Baca saja        | Tidak dapat diubah atau dihapus |

Pesan galat: “Tidak ada data.”

**Test Scenario ringkas** (TS-ADBD-11)

| **Teknik**           | **Skenario**                             | **Hasil diharapkan** |
|----------------------|------------------------------------------|----------------------|
| Benar (Right)        | Buka profil lalu lihat log               | Tercatat             |
| Benar (Right)        | Non-Admin membuka log                    | Ditolak              |
| Kebalikan (Inverse)  | Cari satu akses                          | Ditemukan            |
| Batas (Boundary)     | Filter satu hari                         | Hanya hari itu       |
| Batas (Boundary)     | Nol catatan                              | “Tidak ada data”     |
| Batas (Boundary)     | Akhir sebelum awal                       | Ditolak              |
| Silang (Cross-check) | Jumlah log dibandingkan jumlah akses uji | Sama                 |

#### Modul M5: Kanal WhatsApp

##### FR-ADBD-15 Kanal WhatsApp pada Aplikasi Notifikasi Tazkia \[DUGAAN\]

| **Atribut** | **Isi** |
|-------------|------------------------------------------------------------|
| Prioritas | Should |
| Sumber | Workbook 3.2, 3.7 |
| Aktor | Aplikasi Notifikasi, subsistem pengirim |
| Deskripsi | Aplikasi pengirim WhatsApp membaca topic Kafka kanalnya lalu mengirim lewat API Meta memakai template yang disetujui Meta. Aplikasi template memetakan variabel bernama ke variabel bernomor. Status pengiriman diterbitkan ke topic yang dapat dibaca subsistem pengirim. Hanya pesan keluar |
| Task proses | T-05 |

**Acceptance criteria**

- **Given** template disetujui dan message valid, **When** message dibaca, **Then** dikirim dengan variabel pada urutan yang benar.
- **Given** API Meta mengembalikan galat, **When** pengiriman dicoba, **Then** topic status memuat gagal.
- **Given** template belum disetujui, **When** message dibaca, **Then** tidak dikirim dan status gagal diterbitkan.

**Mockup**

Tidak berlaku: kebutuhan ini antarsistem, tanpa layar pengguna.

**Test Scenario ringkas** (TS-ADBD-15)

| **Teknik** | **Skenario** | **Hasil diharapkan** |
|----------------------|-------------------------------------------------|-----------------------------|
| Benar (Right) | Kirim dengan template disetujui (data sintetis) | Terkirim ke penyedia tiruan |
| Benar (Right) | Template belum disetujui | Status gagal |
| Batas (Boundary) | Variabel kurang | Tidak dikirim |
| Batas (Boundary) | Message sama dibaca dua kali | Satu pengiriman |
| Silang (Cross-check) | Status di topic dibandingkan respons penyedia | Sama |

#### Kebutuhan yang tidak berlaku

##### FR-ADBD-12 Penyediaan data untuk proyek hilir (tidak berlaku)

**Tidak berlaku.** Workbook subbab 3.7 menyatakan subsistem ini tidak memiliki kelompok hilir. Nomor FR-ADBD-12 dipertahankan agar penelusuran versi sebelumnya tidak berubah arti. Bila PIC meminta layanan data, ajukan sebagai change request.

### 3.3 Usability requirements (Persyaratan Kegunaan)

| **ID** | **Kebutuhan**                          | **Ukuran**                                        | **Status** |
|--------|----------------------------------------|---------------------------------------------------|------------|
| NFR-U1 | Terbaca dan dapat dipakai pada telepon | Lebar minimal 360 px tanpa gulir horizontal       | USULAN     |
| NFR-U2 | Pesan galat menjelaskan perbaikan      | Setiap penolakan menyebut kolom dan alasan        | DUGAAN     |
| NFR-U3 | Donatur memperoleh bukti dengan mudah  | Dari masuk sampai unduh maksimal 3 langkah dan 2 menit saat UAT | USULAN     |

### 3.4 Performance requirements (Persyaratan Kinerja)

Angka diisi bersama klien.

| **ID** | **Kebutuhan**       | **Ukuran**                                                                    | **Status** |
|--------|---------------------|-------------------------------------------------------------------------------|------------|
| NFR-P1 | Kapasitas data      | 20.000 donatur dan 100.000 bukti                                              | USULAN     |
| NFR-P2 | Pengguna bersamaan  | 50 pengguna saat puncak                                                       | USULAN     |
| NFR-P3 | Waktu respons       | Halaman maksimal 3 detik; penerbitan bukti maksimal 5 detik pada beban NFR-P2 | USULAN     |
| NFR-P4 | Ukuran berkas bukti | PDF maksimal 500 KB                                                           | USULAN     |

### 3.5 Logical database requirements (Persyaratan Basis Data Logis)

Entitas utama. Skema dan ERD ditetapkan di dokumen perancangan.

| **Entitas** | **Isi utama** | **Data pribadi** | **Masa simpan** |
|-------------------------|-------------------------------------------------------|------------------|-----------------------|
| Donatur | Nama, alamat | Ya | Menunggu BMTZ |
| Identitas masuk | Pengenal Google, nomor dan email terverifikasi | Ya | Sampai akun dihapus |
| OTP | Hash kode, kedaluwarsa, jumlah percobaan | Ya | Sampai kedaluwarsa |
| Akun staf | Email, pengenal Google, peran, status | Ya | Selama akun aktif |
| Preferensi, persetujuan | Anonim, cara kirim, waktu dan versi persetujuan | Ya | Menunggu BMTZ |
| Penyatuan | ID donatur, referensi donasi, dasar kecocokan, status | Tidak langsung | Menunggu BMTZ |
| Bukti donasi | Nomor urut, salinan isi, kode, status | Ya | Ketentuan audit (isi) |
| Rekap tahunan | Nomor urut, tahun, salinan isi | Ya | Ketentuan audit (isi) |
| Permintaan hapus akun | Waktu, hasil | Tidak langsung | Menunggu BMTZ |
| Template WhatsApp | Nama, kategori, pemetaan variabel | Tidak | Selama dipakai |
| Status kirim | Message, waktu, hasil | Tidak langsung | Menunggu BMTZ |
| Log akses | Pengguna, donatur, waktu | Tidak langsung | Menunggu BMTZ |

Aturan: tidak ada foreign key lintas subsistem; referensi donasi disimpan sebagai nilai. Nomor kartu, PIN, dan kata sandi tidak disimpan. OTP hanya disimpan sebagai hash berumur singkat.

#### 3.5.1 Aturan bisnis

| **ID** | **Aturan**                                                                                       | **Status**                  |
|--------|--------------------------------------------------------------------------------------------------|-----------------------------|
| BR-001 | Setiap catatan donasi sah memiliki referensi unik; subsistem ini merujuknya                      | Prinsip kebutuhan           |
| BR-004 | Identitas donatur diproses hanya bila tersedia, relevan, dan diizinkan                           | Perlu validasi kebijakan    |
| BR-005 | Preferensi anonim mengatur tampilan identitas dan tidak menghapus catatan internal               | Perlu validasi              |
| BR-006 | Akses data donatur dan donasi dibatasi menurut kewenangan                                        | Perlu matriks akses         |
| BR-007 | Status, pembatalan, pengembalian dana, dan peruntukan mengikuti sumber kebenaran yang disepakati | Belum disepakati lintas tim |
| BR-008 | Data sintetis dipakai sampai persetujuan pemrosesan data tersedia                                | Ketentuan proyek            |
| BR-009 | Donasi hanya disatukan otomatis lewat email atau nomor telepon yang terverifikasi; setiap penyatuan dapat dibatalkan | Workbook |
| BR-010 | Bukti dan rekap yang sudah terbit disimpan apa adanya beserta nomor urutnya | Workbook |
| BR-011 | Penghapusan akun memutus hubungan akun dengan catatan donasi tanpa menghapus catatan donasi | Workbook |

### 3.6 Design constraints (Batasan Desain)

| **ID** | **Batasan**                                                                                 |
|--------|---------------------------------------------------------------------------------------------|
| DC-01  | Arsitektur berlapis (controller, service, repository) dengan aturan bisnis di service       |
| DC-02  | Kontrak API ditulis dalam OpenAPI dan diterbitkan sebelum struktur database dirancang bebas |
| DC-03  | Data subsistem lain hanya diakses lewat API                                                 |
| DC-04  | Pembatasan akses diterapkan di satu tempat terpusat                                         |
| DC-05  | Data sintetis sampai perjanjian pemrosesan data dan NDA ditandatangani                      |
| DC-06  | Bahasa pemrograman dan basis data belum ditentukan                                          |
| DC-07 | Aplikasi, database, dan deployment milik subsistem sendiri |
| DC-08 | Isi pesan WhatsApp memakai template yang disetujui Meta |

### 3.7 Standards compliance (Kepatuhan pada Standar)

| **ID** | **Standar atau ketentuan**                                                            | **Dampak**                                     | **Status**             |
|--------|---------------------------------------------------------------------------------------|------------------------------------------------|------------------------|
| STD-01 | UU No. 27 Tahun 2022 tentang Pelindungan Data Pribadi                                 | Dasar NFR-S3: akses, log, persetujuan, retensi | Berlaku                |
| STD-02 | Ketentuan pengelolaan zakat, mis. UU No. 23 Tahun 2011 (termasuk bukti setoran zakat) | Isi bukti donasi zakat                         | **Perlu diverifikasi** |

### 3.8 Software system attributes (Atribut Sistem Perangkat Lunak)

| **ID** | **Atribut**  | **Kebutuhan**                                  | **Ukuran**                                      | **Status**    |
|--------|--------------|------------------------------------------------|-------------------------------------------------|---------------|
| NFR-S1 | Keamanan | Tanpa kata sandi; ID token Google divalidasi di server (issuer, audience, tanda tangan, masa berlaku) | Token tidak sah ditolak; sesi 8 jam | USULAN |
| NFR-S2 | Keamanan     | Pembatasan akses diperiksa di server           | Permintaan tidak sah ditolak                    | DUGAAN        |
| NFR-S3 | Privasi      | Data donatur diperlakukan sebagai data pribadi | Hanya pemilik dan peran berwenang               | USULAN        |
| NFR-S4 | Keamanan     | Tidak ada kredensial di kode atau repository   | Pemindai rahasia lulus                          | DUGAAN        |
| NFR-S5 | Retensi      | Data dan bukti disimpan sesuai ketentuan BMTZ  | Menunggu angka                                  | MENUNGGU DATA |
| NFR-S6 | Ketersediaan | Layanan dapat diakses donatur                  | 99% per bulan                                   | USULAN        |
| NFR-S7 | Keandalan    | Operasi multi-tabel atomik                     | Uji integrasi lulus                             | DUGAAN        |
| NFR-S8 | Pemeliharaan | Dapat dijalankan dari dokumentasi              | Instalasi oleh orang luar tim berhasil          | DUGAAN        |
| NFR-S9 | Portabilitas | Peramban modern di ponsel dan laptop           | Dua versi terbaru Chrome, Edge, Firefox, Safari | USULAN        |
| NFR-S10 | Keamanan | OTP tidak dapat ditebak atau dikirim tanpa batas | Maks. 3 kirim per 15 menit, 5 percobaan salah | USULAN |
| NFR-S11 | Keamanan | Verifikasi TOTP setelah login untuk staf | Tanpa TOTP tidak ada akses data | USULAN |

### 3.9 Supporting information (Informasi Pendukung)

#### 3.9.1 Contoh formulir dan dokumen klien

**Belum diterima.** Contoh bukti donasi dan formulir data donatur BMTZ. Hanya versi tanpa data pribadi yang dilampirkan.

#### 3.9.2 Status bukti donasi \[USULAN\]

![gambar](../img/state.png)

*Status bukti donasi*

#### 3.9.3 Dokumentasi untuk pengguna \[DRAF\]

| **Dokumen**                         | **Pembaca**             | **Isi**                            | **Format**      |
|-------------------------------------|-------------------------|------------------------------------|-----------------|
| Panduan pengguna per peran          | Donatur, petugas, Admin | Langkah kerja dan arti pesan galat | DOCX/PDF        |
| Panduan pemasangan dan pemeliharaan | Administrator BMTZ      | Pemasangan, pencadangan, pemulihan | DOCX/PDF        |
| Materi pelatihan                    | Pengguna internal       | Alur kerja dengan data sintetis    | Slide atau DOCX |

## 4. Verification (Verifikasi)

Metode: **T** = uji, **I** = inspeksi, **D** = demonstrasi bersama klien. Kasus uji per FR (TS-ADBD-01 sampai 15) memakai teknik RIGHT-BICEP, nilai batas, dan pemeriksaan silang.

| **ID**               | **Metode** | **Cara verifikasi**                          |
|----------------------|------------|----------------------------------------------|
| FR Umum 1 sampai 4   | T, D       | Uji empat tampilan bersama; demonstrasi UAT  |
| FR-ADBD-01 sampai 05, 13, 14 | T, D       | Uji integrasi per acceptance criteria        |
| FR-ADBD-06, 07       | T, D       | Uji dan demonstrasi bukti sintetis           |
| FR-ADBD-08           | T          | Diuji bila CR-02 disetujui                   |
| FR-ADBD-09, 10       | T          | Peran rendah memanggil endpoint peran tinggi |
| FR-ADBD-11           | T, I       | Uji dan inspeksi log                         |
| FR-ADBD-15 | T | Uji dengan penyedia tiruan dan topic status |
| NFR-P1 sampai P4     | T          | Uji beban setelah angka disepakati           |
| NFR-S1, S4           | I          | Inspeksi kode dan pemindai rahasia           |
| NFR-S2, S7           | T          | Uji integrasi                                |
| NFR-S3               | I, D       | Inspeksi akses; demonstrasi                  |
| NFR-U1, U2           | T, D       | Uji layar telepon; UAT                       |

## 5. Appendices (Lampiran)

### 5.1 Glosarium istilah domain

| **Istilah**      | **Arti**                                           |
|------------------|----------------------------------------------------|
| BMTZ             | Baitulmal Tazkia                                   |
| Donatur / muzaki | Pihak yang menyalurkan dana                        |
| Bukti donasi     | Dokumen digital tanda donasi diterima              |
| Penyatuan        | Menghubungkan donasi dari berbagai kanal ke akun  |
| Peruntukan       | Tujuan penggunaan dana                             |
| FR umum          | Kebutuhan bersama: login, beranda, tabel, formulir |
| Modul            | Satu dari enam modul yang dikonfirmasi BMTZ       |
| Subsistem        | Satu dari dua bagian modul, milik satu kelompok   |

### 5.2 Akronim dan singkatan

BRS, SRS, FR, NFR, RTM, BPMN, API, UAT, ADR, MoSCoW (Must, Should, Could, Won’t), PIC, CR (change request), UU PDP.

### 5.3 Requirements Traceability Matrix (RTM)

Penelusuran dua arah: kebutuhan, task proses, rancangan, uji.

| **ID** | **Modul** | **MoSCoW** | **Sumber** | **Task proses** | **Elemen rancangan** | **Kasus uji** | **Status** |
|--------------------|-----------|------------|-----------------------------------|----------------------------|----------------------|-------------------|-----------------|
| FR Umum 1 sampai 4 | Umum | Must | Kesepakatan BA | Semua | Tampilan bersama | AC FR Umum | Draf |
| FR-ADBD-01 | M1 | Must | Workbook 3.2, 3.7 | T-01 | M1; UC-01 | AC FR-ADBD-01 (3) | Draf |
| FR-ADBD-02 | M1 | Must | Workbook 3.7; v0.2 FR-005 | T-01, T-02 | M1; UC-02 | AC FR-ADBD-02 (2) | Draf |
| FR-ADBD-03 | M1 | Should | Workbook 3.2; v0.2 FR-008 | T-01 | M1; UC-03 | AC FR-ADBD-03 (3) | Draf |
| FR-ADBD-04 | M2 | Must | Workbook 3.2, 3.7; v0.2 FR-007 | T-03 | M2; UC-04 | AC FR-ADBD-04 (3) | Draf |
| FR-ADBD-05 | M2 | Must | Workbook 3.2, 3.5, 3.7 | T-06 | M2; UC-05 | AC FR-ADBD-05 (3) | Draf |
| FR-ADBD-06 | M3 | Must | Workbook 3.2, 3.7 | T-04 | M3; UC-06 | AC FR-ADBD-06 (3) | Draf |
| FR-ADBD-07 | M3 | Must | Workbook 3.2, 3.5 | T-05 | M3; UC-07 | AC FR-ADBD-07 (3) | Draf |
| FR-ADBD-08 | M3 | Could | Usulan tim | T-05 | M3; UC-08 | AC FR-ADBD-08 (2) | Ditahan (CR-02) |
| FR-ADBD-09 | M4 | Must | Workbook Lampiran A; v0.2 NFR-001 | T-01 sampai T-06 | M4; UC-09 | AC FR-ADBD-09 (3) | Draf |
| FR-ADBD-10 | M4 | Must | Workbook Lampiran A; v0.2 NFR-001 | T-01 sampai T-06 | M4; UC-10 | AC FR-ADBD-10 (3) | Draf |
| FR-ADBD-11 | M4 | Should | v0.2 FR-011 | T-01 sampai T-06 | M4; UC-11 | AC FR-ADBD-11 (1) | Draf |
| FR-ADBD-12 | - | Won’t | Workbook 3.7 | - | - | - | Tidak berlaku |
| FR-ADBD-13 | M3 | Must | Workbook 3.2 | T-04 | M3; UC-13 | AC FR-ADBD-13 (3) | Draf |
| FR-ADBD-14 | M1 | Must | Workbook 3.2, 3.6, 3.7 | Belum ada pada model as-is | M1; UC-14 | AC FR-ADBD-14 (3) | Draf |
| FR-ADBD-15 | M5 | Should | Workbook 3.2, 3.7 | T-05 | M5; UC-15 | AC FR-ADBD-15 (3) | Draf |
| NFR-U1 | Lintas | Must | Usulan tim; workbook; v0.2 | T-01 sampai T-06 | Dokumen perancangan | Test plan | Usulan |
| NFR-U2 | Lintas | Must | Usulan tim; workbook; v0.2 | T-01 sampai T-06 | Dokumen perancangan | Test plan | Usulan |
| NFR-U3 | Lintas | Should | Usulan tim; workbook; v0.2 | T-01 sampai T-06 | Dokumen perancangan | Test plan | Usulan |
| NFR-P1 | Lintas | Should | Usulan tim; workbook; v0.2 | T-01 sampai T-06 | Dokumen perancangan | Test plan | Usulan |
| NFR-P2 | Lintas | Should | Usulan tim; workbook; v0.2 | T-01 sampai T-06 | Dokumen perancangan | Test plan | Usulan |
| NFR-P3 | Lintas | Should | Usulan tim; workbook; v0.2 | T-01 sampai T-06 | Dokumen perancangan | Test plan | Usulan |
| NFR-P4 | Lintas | Should | Usulan tim; workbook; v0.2 | T-01 sampai T-06 | Dokumen perancangan | Test plan | Usulan |
| NFR-S1 | Lintas | Must | Usulan tim; workbook; v0.2 | T-01 sampai T-06 | Dokumen perancangan | Test plan | Usulan |
| NFR-S2 | Lintas | Must | Usulan tim; workbook; v0.2 | T-01 sampai T-06 | Dokumen perancangan | Test plan | Usulan |
| NFR-S3 | Lintas | Must | Usulan tim; workbook; v0.2 | T-01 sampai T-06 | Dokumen perancangan | Test plan | Usulan |
| NFR-S4 | Lintas | Must | Usulan tim; workbook; v0.2 | T-01 sampai T-06 | Dokumen perancangan | Test plan | Usulan |
| NFR-S5 | Lintas | Should | Usulan tim; workbook; v0.2 | T-01 sampai T-06 | Dokumen perancangan | Test plan | Usulan |
| NFR-S6 | Lintas | Could | Usulan tim; workbook; v0.2 | T-01 sampai T-06 | Dokumen perancangan | Test plan | Usulan |
| NFR-S7 | Lintas | Must | Usulan tim; workbook; v0.2 | T-01 sampai T-06 | Dokumen perancangan | Test plan | Usulan |
| NFR-S8 | Lintas | Must | Usulan tim; workbook; v0.2 | T-01 sampai T-06 | Dokumen perancangan | Test plan | Usulan |
| NFR-S9 | Lintas | Should | Usulan tim; workbook; v0.2 | T-01 sampai T-06 | Dokumen perancangan | Test plan | Usulan |
| NFR-S10 | Lintas | Must | Usulan tim; workbook; v0.2 | T-01 sampai T-06 | Dokumen perancangan | Test plan | Usulan |
| NFR-S11 | Lintas | Must | Usulan tim; workbook; v0.2 | T-01 sampai T-06 | Dokumen perancangan | Test plan | Usulan |

FR-ADBD-14 belum menunjuk task as-is mana pun; tanyakan ke PIC proses mana yang dilayaninya. Kolom ID elemen BPMN diisi setelah file proses-as-is.bpmn divalidasi.

#### 5.3.1 Pemetaan FR ke Fitur (dokumen klien)

Dokumen untuk BMTZ memakai nama “Fitur 01” dan seterusnya.

| **Fitur (dokumen klien)** | **FR (SRS)** | **Nama** | **Dokumen FR** | **Test Scenario** |
|---------------------------|--------------|-------------------------------------------|----------------|-------------------|
| Fitur 01 | FR-ADBD-01 | Pendaftaran dan login donatur | FR-ADBD-01 | TS-ADBD-01 |
| Fitur 02 | FR-ADBD-02 | Pengelolaan profil donatur | FR-ADBD-02 | TS-ADBD-02 |
| Fitur 03 | FR-ADBD-04 | Penyatuan donasi ke akun | FR-ADBD-04 | TS-ADBD-04 |
| Fitur 04 | FR-ADBD-05 | Riwayat donasi dan status donasi berulang | FR-ADBD-05 | TS-ADBD-05 |
| Fitur 05 | FR-ADBD-06 | Penerbitan bukti donasi | FR-ADBD-06 | TS-ADBD-06 |
| Fitur 06 | FR-ADBD-07 | Unduh dan kirim bukti | FR-ADBD-07 | TS-ADBD-07 |
| Fitur 07 | FR-ADBD-13 | Rekapitulasi donasi tahunan | FR-ADBD-13 | TS-ADBD-13 |
| Fitur 08 | FR-ADBD-09 | Pembatasan akses dan login staf | FR-ADBD-09 | TS-ADBD-09 |
| Fitur 09 | FR-ADBD-10 | Pengelolaan akun staf dan peran | FR-ADBD-10 | TS-ADBD-10 |
| Fitur 10 | FR-ADBD-03 | Preferensi anonimitas dan pengiriman | FR-ADBD-03 | TS-ADBD-03 |
| Fitur 11 | FR-ADBD-14 | Penghapusan akun donatur | FR-ADBD-14 | TS-ADBD-14 |
| Fitur 12 | FR-ADBD-11 | Log akses data pribadi | FR-ADBD-11 | TS-ADBD-11 |
| Fitur 13 | FR-ADBD-15 | Kanal WhatsApp pada Aplikasi Notifikasi | FR-ADBD-15 | TS-ADBD-15 |
| Fitur 14 | FR-ADBD-08 | Verifikasi keaslian bukti | FR-ADBD-08 | TS-ADBD-08 |

### 5.4 Kandidat change request

| **ID** | **Usulan**                             | **Task terdampak** | **Perubahan**                              | **Bottleneck atau waste yang dihilangkan** | **Status** |
|--------|----------------------------------------|--------------------|--------------------------------------------|--------------------------------------------|------------|
| CR-01  | Penyatuan dan penerbitan bukti otomatis | T-03, T-04         | Pelaksana berpindah dari petugas ke sistem | Belum terukur (dugaan: pekerjaan manual)   | Diusulkan  |
| CR-02  | Verifikasi keaslian bukti (FR-ADBD-08) | T-05               | Menambah task verifikasi                   | Belum terukur                              | Diusulkan  |

### 5.5 Pemetaan ke ISO/IEC/IEEE 29148

| **Klausul 29148 (isi SRS, klausul 9.6)** | **Bab pada SRS ini** |
|------------------------------------------|----------------------|
| 9.6.1 Pendahuluan                        | Bab 1                |
| 9.6.2 Rujukan                            | Bab 2                |
| 9.6.3 Persyaratan spesifik               | Bab 3                |
| 9.6.4 Verifikasi                         | Bab 4                |
| 9.6.5 Lampiran                           | Bab 5                |

Tambahan di luar kerangka standar: FR umum, mockup dan Test Scenario ringkas per FR, dan pemetaan FR ke fitur (5.3.1).

### 5.6 Persetujuan

Setelah ditandatangani, perubahan SRS melewati prosedur change control.

| **Peran**                   | **Nama**      | **Tanda tangan** | **Tanggal** |
|-----------------------------|---------------|------------------|-------------|
| Narasumber Baitulmal Tazkia |               |                  |             |
| Business Analyst            | Eli Nur Aulia |                  |             |
| Project Manager             | Destri Komalasari        |                  |             |

### 5.7 User story

Manfaat tiap user story belum dapat ditelusuri ke catatan wawancara karena wawancara belum tersedia.

| **ID** | **User story \[USULAN\]** | **FR** |
|--------|------------------------------------------------------------|------------|
| US-01 | Sebagai donatur, saya ingin masuk dengan Google atau OTP agar tidak perlu mengingat kata sandi | FR-ADBD-01 |
| US-02 | Sebagai donatur, saya ingin memperbarui data saya agar donasi dan bukti memakai data yang benar | FR-ADBD-02 |
| US-03 | Sebagai donatur, saya ingin memilih tampil anonim agar nama saya tidak ditampilkan | FR-ADBD-03 |
| US-04 | Sebagai donatur, saya ingin donasi dari berbagai kanal terkumpul di akun saya agar riwayatnya utuh | FR-ADBD-04 |
| US-05 | Sebagai donatur, saya ingin melihat semua pemberian dan donasi berulang saya di satu tempat agar mudah dipantau | FR-ADBD-05 |
| US-06 | Sebagai donatur, saya ingin bukti resmi setiap donasi agar punya tanda terima | FR-ADBD-06 |
| US-07 | Sebagai donatur, saya ingin mengunduh atau menerima bukti agar bisa disimpan | FR-ADBD-07 |
| US-08 | Sebagai penerima bukti, saya ingin memeriksa keaslian bukti agar dapat mempercayainya | FR-ADBD-08 |
| US-09 | Sebagai donatur, saya ingin data saya hanya dibuka pihak berwenang agar privasi terjaga | FR-ADBD-09 |
| US-10 | Sebagai admin, saya ingin mengatur peran staf agar wewenangnya sesuai tugas | FR-ADBD-10 |
| US-11 | Sebagai pemilik proses, saya ingin akses data tercatat agar dapat diaudit | FR-ADBD-11 |
| US-13 | Sebagai muzaki, saya ingin rekap tahunan zakat agar bisa dipakai saat pelaporan pajak | FR-ADBD-13 |
| US-14 | Sebagai donatur, saya ingin dapat menghapus akun agar data saya tidak terus dipakai | FR-ADBD-14 |
| US-15 | Sebagai donatur, saya ingin menerima OTP dan bukti lewat WhatsApp agar cepat sampai | FR-ADBD-15 |

### 5.8 Keputusan terbuka

| **ID** | **Pertanyaan**                               | **Dampak bila belum diputuskan** |
|--------|----------------------------------------------|----------------------------------|
| OD-001 | Apakah akun wajib untuk semua donasi?        | FR-ADBD-01, 04, antarmuka        |
| OD-002 | Apa atribut minimum identitas donatur?       | Validasi, privasi, pencocokan    |
| OD-007 | Target kinerja, ketersediaan, retensi log?   | Pengujian kualitas               |
| OD-008 | Kebijakan anonimitas dan akses data pribadi? | Risiko privasi dan tampilan      |
| OD-010 | Apakah portal donatur masuk rilis pertama?   | Seluruh layar donatur            |
| OD-011 | Retensi, penghapusan, koreksi, backup?       | Data tidak terkelola             |
| OD-012 | Siapa pemilik proses yang memvalidasi?       | Kebutuhan belum dapat disahkan   |
| OD-013 | Apakah donatur juga wajib TOTP setelah login? | NFR-S11, FR-ADBD-01 |
| OD-014 | Format bukti setor zakat yang diterima kantor pajak? | FR-ADBD-13 |

### 5.9 Risiko utama

| **ID** | **Risiko**                                     | **Mitigasi**                                       |
|--------|------------------------------------------------|----------------------------------------------------|
| R-001  | As-is belum tervalidasi                        | Wawancara, observasi, validasi pemilik proses      |
| R-002  | Kontrak API dengan Kelompok 1 belum disepakati | Tetapkan pemilik data, skema, status, galat, versi |
| R-003  | Kebijakan data pribadi belum lengkap           | Validasi atribut, tujuan, akses, retensi           |
| R-004  | Target kualitas belum terukur                  | Sepakati angka sebelum acceptance test             |
| R-005  | Batas rilis belum final                        | Tetapkan lingkup dan MoSCoW                        |
| R-006 | Dua donatur berbeda keliru disatukan | Hanya identitas terverifikasi; antrean; dapat dibatalkan |
| R-007 | Bukti memuat angka berbeda dari catatan donasi | Terbit dari data terkini sumber, lalu disimpan apa adanya |
| R-008 | Penghapusan akun menghapus catatan audit | Hanya memutus hubungan |
| R-009 | OTP ditebak atau dikirim berulang | NFR-S10 |
| R-010 | Persetujuan Meta belum selesai | Email sebagai cadangan |
