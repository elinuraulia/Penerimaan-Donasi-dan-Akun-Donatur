# Business Requirements Specification (BRS)

Sistem Akun Donatur dan Bukti Donasi · Baitulmal Tazkia

| **Item**         | **Isi**                                                                                                                    |
|------------------|----------------------------------------------------------------------------------------------------------------------------|
| Dokumen          | BRS                                                                                                                        |
| Dosen            | Endy Muhardin                                                                                                              |
| Kelompok         | 2                                                                                                                          |
| Business Analyst | Eli Nur Aulia                                                                                                              |
| Project Manager  | Destri Komalasari                                                                                                                     |
| Versi            | 0.2 (draf)                                                                                                                 |
| Tanggal          | 26 November 2026                                                                                                           |
| Acuan            | SRS Akun Donatur dan Bukti Donasi v0.4                                                                                     |
| Status           | DRAF, belum ada sign-off. \[USULAN\] = usulan tim; \[DUGAAN\] = belum dikonfirmasi klien; \[DRAF\] = belum disetujui final |

## 1. Pendahuluan

### 1.1 Tujuan dokumen

Dokumen ini menjelaskan kebutuhan bisnis Baitulmal Tazkia (BMTZ) untuk pengelolaan akun donatur dan bukti donasi: masalah, tujuan, pemangku kepentingan, proses, dan aturan. Rincian perilaku sistem ada di dokumen FR dan SRS.

### 1.2 Latar belakang \[DUGAAN\]

Donasi datang dari berbagai kanal dan pencatatannya mungkin memakai spreadsheet atau proses manual. Pencocokan donasi dengan donatur serta pembuatan bukti diduga dilakukan manual. Belum ada wawancara atau observasi yang membuktikannya.

| **ID** | **Masalah \[DUGAAN\]**                           | **Dampak**                      |
|--------|--------------------------------------------------|---------------------------------|
| M-01   | Data donatur tidak terkumpul dalam satu tempat   | Sulit dicari dan berisiko ganda |
| M-02   | Donatur tidak dapat menelusuri donasinya sendiri | Harus bertanya ke petugas       |
| M-03   | Bukti donasi dibuat dan diserahkan manual        | Lambat dan arsip tidak tertata  |
| M-04   | Akses ke data donatur tidak tercatat             | Sulit ditelusuri saat audit     |

### 1.3 Ruang lingkup

**Dalam lingkup:** pendaftaran dan login (Google atau OTP), penyatuan donasi, riwayat dan status donasi berulang, bukti donasi, rekapitulasi tahunan sebagai bukti setor zakat, pilihan anonim, penghapusan akun, hak akses, log akses, dan kanal WhatsApp.

**Di luar lingkup:** pencatatan donasi (Kelompok 1), penagihan donasi berulang (kelompok Donasi Berulang), pemrosesan pembayaran, kampanye pemasaran, serta pesan masuk dan broadcast WhatsApp.

## 2. Tujuan bisnis dan ukuran keberhasilan \[USULAN\]

| **ID** | **Tujuan**                                 | **Ukuran**                                           | **Masalah** |
|--------|--------------------------------------------|------------------------------------------------------|-------------|
| TB-01  | Data donatur tertata                       | Setiap identitas terverifikasi hanya milik satu akun   | M-01        |
| TB-02  | Donatur mandiri melihat donasinya          | Riwayat tersedia setelah login tanpa bantuan petugas | M-02        |
| TB-03  | Bukti donasi cepat tersedia                | Dari login sampai unduh maksimal 2 menit             | M-03        |
| TB-04  | Data pribadi terlindungi dan dapat diaudit | Seluruh akses data donatur tercatat                  | M-04        |

## 3. Pemangku kepentingan

Ringkasan; daftar lengkap ada di Stakeholder Register.

| **Pemangku kepentingan** | **Kepentingan** | **Keterlibatan** |
|------------------------------------|---------------------------------------|----------------------------------|
| PIC modul K1 / pemilik proses BMTZ | Kepercayaan donatur dan akuntabilitas | Menyetujui kebutuhan (nama: isi) |
| Donatur dan muzaki | Riwayat, bukti, privasi | Pengguna |
| Petugas donasi | Konfirmasi penyatuan, bukti | Pengguna |
| Admin | Akun, peran, log | Pengguna |
| Kelompok 1 (Penerimaan Donasi) | Penyedia data donasi | Menyepakati kontrak API |
| Kelompok Donasi Berulang | Penyedia status dan signed URL | Menyepakati kontrak API |

## 4. Proses bisnis \[DUGAAN\]

### 4.1 Kondisi sekarang (as-is)

![gambar](../../../02-kebutuhan-dan-desain/adbd/img/bpmn.png)

*Model BPMN 2.0 kondisi sekarang (draf)*

### 4.2 Usulan (to-be)

![gambar](../../../02-kebutuhan-dan-desain/adbd/img/flow.png)

*Alur usulan (garis putus-putus: kandidat change request)*

## 5. Kebutuhan bisnis \[USULAN\]

| **ID** | **Kebutuhan bisnis**                                             | **Tujuan** | **Prioritas** | **Dipenuhi oleh**  |
|--------|------------------------------------------------------------------|------------|---------------|--------------------|
| KB-01  | Donatur dapat memiliki akun dan mengelola datanya                | TB-01      | Must          | FR-ADBD-01, 02     |
| KB-02  | Pilihan privasi dan cara komunikasi donatur dihormati            | TB-04      | Should        | FR-ADBD-03         |
| KB-03  | Donasi terhubung ke donatur yang tepat                           | TB-02      | Must          | FR-ADBD-04         |
| KB-04  | Donatur dapat melihat riwayat donasinya                          | TB-02      | Must          | FR-ADBD-05         |
| KB-05 | Setiap donasi berhasil dari semua kanal memiliki bukti resmi yang dapat diperoleh donatur | TB-03 | Must | FR-ADBD-06, 07 |
| KB-06  | Keaslian bukti dapat diperiksa                                   | TB-03      | Could         | FR-ADBD-08         |
| KB-07 | Data donatur hanya dibuka pihak berwenang dan aksesnya tercatat | TB-04 | Must | FR-ADBD-09, 10, 11 |
| KB-08 | Tidak berlaku: subsistem tidak memiliki kelompok hilir | - | Won’t | FR-ADBD-12 |
| KB-09 | Muzaki memperoleh rekapitulasi tahunan sebagai bukti setor zakat | TB-03 | Must | FR-ADBD-13 |
| KB-10 | Donatur dapat meminta akunnya dihapus tanpa menghilangkan catatan audit | TB-04 | Must | FR-ADBD-14 |
| KB-11 | Pesan penting dapat dikirim lewat WhatsApp dan kegagalannya diketahui | TB-03 | Should | FR-ADBD-15 |

## 6. Aturan bisnis

| **ID** | **Aturan**                                                                        | **Status**          |
|--------|-----------------------------------------------------------------------------------|---------------------|
| BR-001 | Setiap donasi sah memiliki referensi unik                                         | Prinsip kebutuhan   |
| BR-004 | Identitas donatur diproses hanya bila tersedia, relevan, dan diizinkan            | Perlu validasi      |
| BR-005 | Anonim mengatur tampilan dan tidak menghapus catatan internal                     | Perlu validasi      |
| BR-006 | Akses data dibatasi menurut kewenangan                                            | Perlu matriks akses |
| BR-007 | Status, pembatalan, pengembalian, dan peruntukan mengikuti sumber yang disepakati | Belum disepakati    |
| BR-008 | Data sintetis sampai persetujuan pemrosesan data tersedia                         | Ketentuan proyek    |
| BR-009 | Bukti diterbitkan hanya untuk donasi berstatus Berhasil, satu bukti per donasi    | USULAN              |

## 7. Batasan, asumsi, dan ketergantungan

- Mematuhi UU No. 27 Tahun 2022 tentang Pelindungan Data Pribadi.

- Data donatur asli tidak dipakai sebelum perjanjian pemrosesan data dan NDA ditandatangani.

- Data donasi diperoleh dari subsistem Kelompok 1 lewat API.

- Donatur diasumsikan memiliki nomor telepon atau akun Google.
- Status donasi berulang dan signed URL disediakan kelompok Donasi Berulang.
- Pengiriman memakai Aplikasi Notifikasi Tazkia; kanal WhatsApp menunggu persetujuan Meta.

- Akun diasumsikan tidak wajib untuk berdonasi.

## 8. Risiko

Ringkasan risiko awal; daftar lengkap, penilaian, dan pemiliknya ada di Risk Register.

| **ID** | **Risiko**                                     | **Mitigasi**                     |
|--------|------------------------------------------------|----------------------------------|
| R-001  | Proses as-is belum tervalidasi                 | Wawancara dan observasi          |
| R-002  | Kontrak API dengan Kelompok 1 belum disepakati | Sepakati data, status, dan galat |
| R-003  | Kebijakan data pribadi belum lengkap           | Validasi atribut, akses, retensi |
| R-005  | Batas rilis belum final                        | Tetapkan lingkup dan prioritas   |

## 9. Keputusan yang dibutuhkan dari BMTZ

- Apakah akun wajib untuk berdonasi, dan apakah portal donatur masuk rilis pertama?

- Atribut minimum identitas donatur.

- Isi dan bentuk resmi bukti donasi.

- Kebijakan anonimitas, akses, dan masa simpan data.

- Siapa pemilik proses yang memvalidasi.

## Persetujuan

| **Peran**                   | **Nama**      | **Tanda tangan** | **Tanggal** |
|-----------------------------|---------------|------------------|-------------|
| Narasumber Baitulmal Tazkia |               |                  |             |
| Business Analyst            | Eli Nur Aulia |                  |             |
| Project Manager             | Destri Komalasari        |                  |             |
