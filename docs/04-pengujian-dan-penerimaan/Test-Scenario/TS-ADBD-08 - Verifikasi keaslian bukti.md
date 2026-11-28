# TS-ADBD-08 Verifikasi keaslian bukti · Akun Donatur dan Bukti Donasi

Kelompok 2 · Dosen: Endy Muhardin · Business Analyst: Eli Nur Aulia · Project Manager: Destri Komalasari · Status: draf

Kolom hasil aktual dan status diisi saat pengujian.


Kebutuhan: FR-ADBD-08. Prioritas: Could. Prakondisi: memiliki kode verifikasi. Diuji hanya bila CR-02 disetujui.

| **ID uji**    | **Teknik**           | **Skenario**                    | **Hasil diharapkan** | **Hasil aktual** | **Status** |
|---------------|----------------------|---------------------------------|----------------------|------------------|------------|
| TS-ADBD-08-01 | Benar (Right)        | Kode sah                        | “Sah”                |                  |            |
| TS-ADBD-08-02 | Benar (Right)        | Kode acak                       | “Tidak ditemukan”    |                  |            |
| TS-ADBD-08-03 | Kebalikan (Inverse)  | Bukti dibatalkan lalu diperiksa | “Dibatalkan”         |                  |            |
| TS-ADBD-08-04 | Batas (Boundary)     | 11 karakter                     | Ditolak              |                  |            |
| TS-ADBD-08-05 | Batas (Boundary)     | 12 karakter                     | Diproses             |                  |            |
| TS-ADBD-08-06 | Batas (Boundary)     | 13 karakter                     | Ditolak              |                  |            |
| TS-ADBD-08-07 | Silang (Cross-check) | Hasil dibandingkan data bukti   | Sama                 |                  |            |
