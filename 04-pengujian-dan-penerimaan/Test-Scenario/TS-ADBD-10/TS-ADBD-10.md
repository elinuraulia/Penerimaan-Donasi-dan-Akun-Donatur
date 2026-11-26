# TS-ADBD-10 Pengelolaan akun dan peran · Akun Donatur dan Bukti Donasi

Kelompok 2 · Business Analyst: Eli Nur Aulia · Project Manager: Destri · Status: draf

Kolom hasil aktual dan status diisi saat pengujian.


Kebutuhan: FR-ADBD-10. Prioritas: Must. Prakondisi: berperan Admin.

| **ID uji**    | **Teknik**           | **Skenario**                                  | **Hasil diharapkan** | **Hasil aktual** | **Status** |
|---------------|----------------------|-----------------------------------------------|----------------------|------------------|------------|
| TS-ADBD-10-01 | Benar (Right)        | Buat “petugas.contoh”                         | Akun aktif           |                  |            |
| TS-ADBD-10-02 | Benar (Right)        | Nama sama dibuat lagi                         | Ditolak              |                  |            |
| TS-ADBD-10-03 | Kebalikan (Inverse)  | Nonaktifkan lalu aktifkan                     | Dapat login          |                  |            |
| TS-ADBD-10-04 | Batas (Boundary)     | Nama pengguna 3 karakter                      | Ditolak              |                  |            |
| TS-ADBD-10-05 | Batas (Boundary)     | 4 karakter                                    | Diterima             |                  |            |
| TS-ADBD-10-06 | Batas (Boundary)     | 31 karakter                                   | Ditolak              |                  |            |
| TS-ADBD-10-07 | Silang (Cross-check) | Daftar akun dibandingkan daftar petugas resmi | Sama                 |                  |            |
