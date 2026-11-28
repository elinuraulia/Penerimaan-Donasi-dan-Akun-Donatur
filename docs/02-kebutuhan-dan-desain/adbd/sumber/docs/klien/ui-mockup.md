# UI Mockup · Akun Donatur dan Bukti Donasi

Kelompok 2 · Business Analyst: Eli Nur Aulia · Project Manager: Destri Komalasari · Status: draf

Gambar adalah wireframe usulan dengan data fiktif.

## FR Umum 1 Layar login


![gambar](../../../img/umum-1-login.png)

*Layar login*

## FR Umum 2 Beranda setelah login


![gambar](../../../img/umum-2-beranda.png)

*Beranda setelah login*

## FR Umum 3 Tampilan tabel


![gambar](../../../img/umum-3-tabel.png)

*Tampilan tabel*

## FR Umum 4 Tampilan formulir input


![gambar](../../../img/umum-4-formulir.png)

*Tampilan formulir input*

## FR-ADBD-01 Pendaftaran dan login donatur

![gambar](../../../img/adbd-01-daftar.png)

*Masuk atau daftar*

| **Elemen** | **Jenis** | **Perilaku** |
|--------------------------|------------------|-----------------------------------|
| Masuk dengan Google | Tombol | Memakai OpenID Connect |
| Nomor telepon, Kirim OTP | Kolom dan tombol | Jumlah kirim dibatasi |
| Kode OTP | Kolom | 6 digit, berlaku 5 menit [USULAN] |
| Persetujuan data | Centang | Wajib saat akun baru |

Pesan galat: “Kode OTP salah atau kedaluwarsa.”; “Terlalu banyak permintaan. Coba lagi nanti.”

## FR-ADBD-02 Pengelolaan profil donatur


![gambar](../../../img/adbd-02-profil.png)

*Pengelolaan profil donatur*

| **Elemen**    | **Jenis** | **Perilaku**      |
|---------------|-----------|-------------------|
| Data diri     | Kolom     | Sesuai 3.1.1.2    |
| Simpan, Batal | Tombol    | Perubahan dicatat |

Pesan galat: “Nama wajib diisi.”; “Nomor telepon tidak valid.”

## FR-ADBD-03 Preferensi anonimitas dan pengiriman

![gambar](../../../img/adbd-03-preferensi.png)

*Preferensi*

| **Elemen** | **Jenis** | **Perilaku** |
|---------------------|-----------|--------------------------------|
| Tampil sebagai | Pilihan | Nama atau anonim |
| Kirim bukti melalui | Pilihan | Email, WhatsApp, unduh sendiri |
| Simpan, Batal | Tombol | Menyimpan preferensi |

Pesan galat: “Verifikasi kontak untuk kanal ini terlebih dahulu.”

## FR-ADBD-04 Penyatuan donasi ke akun

![gambar](../../../img/adbd-04-penautan.png)

*Antrean konfirmasi*

| **Elemen** | **Jenis** | **Perilaku** |
|----------------|-----------|----------------------------------------|
| Antrean | Tabel | Donasi, kandidat akun, dasar kecocokan |
| Satukan, Tolak | Tautan | Alasan wajib bagi petugas |
| Batalkan | Tautan | Melepas penyatuan |

Pesan galat: “Donasi sudah disatukan ke akun lain.”; “Alasan wajib diisi.”

## FR-ADBD-05 Riwayat donasi dan status donasi berulang

![gambar](../../../img/adbd-05-riwayat.png)

*Riwayat donasi*

| **Elemen** | **Jenis** | **Perilaku** |
|-------------------------|------------------|-----------------------------|
| Periode, Peruntukan | Filter | Awal tidak melewati akhir |
| Tabel | Baca saja | Donasi milik sendiri |
| Donasi berulang, Kelola | Kartu dan tombol | Status dari Donasi Berulang |

Pesan galat: “Tanggal akhir tidak boleh sebelum tanggal awal.”; “Pengelolaan donasi berulang sedang tidak tersedia.”

## FR-ADBD-06 Penerbitan bukti donasi

![gambar](../../../img/adbd-06-bukti.png)

*Bukti donasi*

| **Elemen** | **Jenis** | **Perilaku** |
|--------------|-----------|---------------------|
| Isi bukti | Baca saja | Salinan saat terbit |
| Unduh, Kirim | Tombol | Lihat FR-ADBD-07 |

Pesan galat: “Bukti hanya untuk donasi berstatus Berhasil.”

## FR-ADBD-07 Unduh dan kirim bukti

![gambar](../../../img/adbd-06-bukti.png)

*Unduh dan kirim*

| **Elemen** | **Jenis** | **Perilaku** |
|------------|-----------|-------------------------|
| Unduh PDF | Tombol | Pemilik atau petugas |
| Kirim | Tombol | Ke kontak terverifikasi |

Pesan galat: “Pengiriman gagal, coba lagi.”

## FR-ADBD-08 Verifikasi keaslian bukti


![gambar](../../../img/adbd-08-verifikasi.png)

*Verifikasi keaslian bukti*

| **Elemen**      | **Jenis** | **Perilaku**          |
|-----------------|-----------|-----------------------|
| Kode verifikasi | Kolom     | 12 karakter           |
| Periksa         | Tombol    | Menampilkan ringkasan |

Pesan galat: “Kode verifikasi tidak valid.”

## FR-ADBD-09 Pembatasan akses dan login staf

![gambar](../../../img/adbd-09-ditolak.png)

*Akses ditolak*

| **Elemen** | **Jenis** | **Perilaku** |
|------------|-----------|----------------------|
| Pesan 403 | Teks | Tanpa rincian teknis |
| Kembali | Tombol | Ke beranda |

Pesan galat: “Anda tidak berhak membuka halaman ini.”

## FR-ADBD-10 Pengelolaan akun staf dan peran

![gambar](../../../img/adbd-10-akun.png)

*Kelola akun staf*

| **Elemen** | **Jenis** | **Perilaku** |
|---------------------|-----------|----------------------|
| Tabel akun | Tabel | Email, peran, status |
| Email Google, Peran | Kolom | Wajib |
| Simpan, Batal | Tombol | Hanya Admin |

Pesan galat: “Email tidak valid atau sudah terdaftar.”; “Pilih peran.”

## FR-ADBD-11 Log akses data pribadi


![gambar](../../../img/adbd-11-catatan-akses.png)

*Log akses data pribadi*

| **Elemen**    | **Jenis**        | **Perilaku**                    |
|---------------|------------------|---------------------------------|
| Filter        | Pilihan, rentang | Menyaring                       |
| Tabel catatan | Baca saja        | Tidak dapat diubah atau dihapus |

Pesan galat: “Tidak ada data.”

## FR-ADBD-13 Rekapitulasi donasi tahunan

![gambar](../../../img/adbd-13-rekap.png)

*Rekapitulasi tahunan*

| **Elemen** | **Jenis** | **Perilaku** |
|----------------------|-----------|----------------------------------|
| Tahun | Pilihan | Tahun yang memiliki donasi zakat |
| Terbitkan, Unduh PDF | Tombol | Menyimpan salinan isi |

Pesan galat: “Belum ada donasi zakat pada tahun ini.”

## FR-ADBD-14 Penghapusan akun donatur

![gambar](../../../img/adbd-14-hapus.png)

*Hapus akun*

| **Elemen** | **Jenis** | **Perilaku** |
|-------------------|-----------------|-------------------------------|
| Penjelasan dampak | Teks | Apa yang dihapus dan disimpan |
| Konfirmasi ulang | OTP atau Google | Wajib |
| Hapus akun, Batal | Tombol | Mencatat permintaan |

Pesan galat: “Konfirmasi gagal. Akun tidak dihapus.”

## FR-ADBD-15 Kanal WhatsApp pada Aplikasi Notifikasi

Tidak ada layar: kebutuhan antarsistem.

