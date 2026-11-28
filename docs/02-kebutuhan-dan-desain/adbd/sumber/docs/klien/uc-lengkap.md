# Use Case Lengkap · Akun Donatur dan Bukti Donasi

Kelompok 2 · Business Analyst: Eli Nur Aulia · Project Manager: Destri Komalasari · Status: draf

## Model use case

![gambar](../../../img/uc.png)

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

