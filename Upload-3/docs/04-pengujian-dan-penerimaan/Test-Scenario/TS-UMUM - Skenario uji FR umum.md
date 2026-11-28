# TS-UMUM Skenario uji FR umum · Akun Donatur dan Bukti Donasi

Kelompok 2 · Dosen: Endy Muhardin · Business Analyst: Eli Nur Aulia · Project Manager: Destri Komalasari · Status: draf

## TS-UMUM-01 Layar login

| **ID uji** | **Teknik** | **Skenario** | **Hasil diharapkan** | **Hasil aktual** | **Status** |
|---------------|---------------|------------------------------|------------------------|------------------|------------|
| TS-UMUM-01-01 | Benar (Right) | Donatur memasukkan OTP benar | Masuk ke beranda |  |  |
| TS-UMUM-01-02 | Benar (Right) | Akun dinonaktifkan | Ditolak |  |  |
| TS-UMUM-01-03 | Benar (Right) | OTP atau ID token tidak sah | Pesan umum, tanpa sesi |  |  |

## TS-UMUM-02 Beranda setelah login

| **ID uji**    | **Teknik**    | **Skenario**          | **Hasil diharapkan**                      | **Hasil aktual** | **Status** |
|---------------|---------------|-----------------------|-------------------------------------------|------------------|------------|
| TS-UMUM-02-01 | Benar (Right) | Login sebagai Donatur | Menu hanya memuat data miliknya           |                  |            |
| TS-UMUM-02-02 | Benar (Right) | Login sebagai Admin   | Menu kelola akun dan catatan akses tampil |                  |            |

## TS-UMUM-03 Tampilan tabel

| **ID uji**    | **Teknik**    | **Skenario**              | **Hasil diharapkan**                   | **Hasil aktual** | **Status** |
|---------------|---------------|---------------------------|----------------------------------------|------------------|------------|
| TS-UMUM-03-01 | Benar (Right) | Buka tabel berisi 48 data | Enam data per halaman dan jumlah total |                  |            |
| TS-UMUM-03-02 | Benar (Right) | Filter tidak cocok        | Tampil “tidak ada data”                |                  |            |

## TS-UMUM-04 Tampilan formulir input

| **ID uji**    | **Teknik**    | **Skenario**                     | **Hasil diharapkan**                  | **Hasil aktual** | **Status** |
|---------------|---------------|----------------------------------|---------------------------------------|------------------|------------|
| TS-UMUM-04-01 | Benar (Right) | Simpan dengan kolom wajib kosong | Ditolak dan kolom yang kurang disebut |                  |            |
| TS-UMUM-04-02 | Benar (Right) | Simpan dengan data valid         | Tersimpan dan kembali ke tabel        |                  |            |
