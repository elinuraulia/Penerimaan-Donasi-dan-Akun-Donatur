# TS-ADBD-05 Riwayat donasi · Akun Donatur dan Bukti Donasi

Kelompok 2 · Business Analyst: Eli Nur Aulia · Project Manager: Destri · Status: draf

Kolom hasil aktual dan status diisi saat pengujian.


Kebutuhan: FR-ADBD-05. Prioritas: Must. Prakondisi: pengguna sudah login.

| **ID uji**    | **Teknik**           | **Skenario**                              | **Hasil diharapkan**  | **Hasil aktual** | **Status** |
|---------------|----------------------|-------------------------------------------|-----------------------|------------------|------------|
| TS-ADBD-05-01 | Benar (Right)        | Buka riwayat                              | Tampil donasi tertaut |                  |            |
| TS-ADBD-05-02 | Benar (Right)        | Buka riwayat orang lain                   | Ditolak               |                  |            |
| TS-ADBD-05-03 | Kebalikan (Inverse)  | Filter lalu kosongkan                     | Seluruh data kembali  |                  |            |
| TS-ADBD-05-04 | Batas (Boundary)     | Awal sama dengan akhir                    | Diterima              |                  |            |
| TS-ADBD-05-05 | Batas (Boundary)     | Akhir sebelum awal                        | Ditolak               |                  |            |
| TS-ADBD-05-06 | Batas (Boundary)     | Nol donasi                                | “Tidak ada data”      |                  |            |
| TS-ADBD-05-07 | Silang (Cross-check) | Total dibandingkan data Penerimaan Donasi | Sama                  |                  |            |
