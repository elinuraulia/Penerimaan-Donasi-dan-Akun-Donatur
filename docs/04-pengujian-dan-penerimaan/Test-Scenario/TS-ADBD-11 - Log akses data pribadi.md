# TS-ADBD-11 Log akses data pribadi · Akun Donatur dan Bukti Donasi

Kelompok 2 · Dosen: Endy Muhardin · Business Analyst: Eli Nur Aulia · Project Manager: Destri Komalasari · Status: draf

Kolom hasil aktual dan status diisi saat pengujian.


Kebutuhan: FR-ADBD-11. Prioritas: Should. Prakondisi: berperan Admin.

| **ID uji**    | **Teknik**           | **Skenario**                             | **Hasil diharapkan** | **Hasil aktual** | **Status** |
|---------------|----------------------|------------------------------------------|----------------------|------------------|------------|
| TS-ADBD-11-01 | Benar (Right)        | Buka profil lalu lihat log               | Tercatat             |                  |            |
| TS-ADBD-11-02 | Benar (Right)        | Non-Admin membuka log                    | Ditolak              |                  |            |
| TS-ADBD-11-03 | Kebalikan (Inverse)  | Cari satu akses                          | Ditemukan            |                  |            |
| TS-ADBD-11-04 | Batas (Boundary)     | Filter satu hari                         | Hanya hari itu       |                  |            |
| TS-ADBD-11-05 | Batas (Boundary)     | Nol catatan                              | “Tidak ada data”     |                  |            |
| TS-ADBD-11-06 | Batas (Boundary)     | Akhir sebelum awal                       | Ditolak              |                  |            |
| TS-ADBD-11-07 | Silang (Cross-check) | Jumlah log dibandingkan jumlah akses uji | Sama                 |                  |            |
