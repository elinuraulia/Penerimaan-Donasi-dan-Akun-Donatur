# TS-ADBD-04 Penautan donasi ke akun · Akun Donatur dan Bukti Donasi

Kelompok 2 · Business Analyst: Eli Nur Aulia · Project Manager: Destri · Status: draf

Kolom hasil aktual dan status diisi saat pengujian.


Kebutuhan: FR-ADBD-04. Prioritas: Must. Prakondisi: akun terverifikasi; data donasi tersedia.

| **ID uji**    | **Teknik**           | **Skenario**                            | **Hasil diharapkan**                 | **Hasil aktual** | **Status** |
|---------------|----------------------|-----------------------------------------|--------------------------------------|------------------|------------|
| TS-ADBD-04-01 | Benar (Right)        | Email sama dan terverifikasi            | Tertaut                              |                  |            |
| TS-ADBD-04-02 | Benar (Right)        | Email belum terverifikasi               | Tidak tertaut                        |                  |            |
| TS-ADBD-04-03 | Kebalikan (Inverse)  | Tautan dibatalkan petugas               | Donasi hilang dari riwayat; tercatat |                  |            |
| TS-ADBD-04-04 | Batas (Boundary)     | Alasan kosong                           | Ditolak                              |                  |            |
| TS-ADBD-04-05 | Batas (Boundary)     | Alasan 1 karakter                       | Diterima                             |                  |            |
| TS-ADBD-04-06 | Batas (Boundary)     | Alasan 501 karakter                     | Ditolak                              |                  |            |
| TS-ADBD-04-07 | Silang (Cross-check) | Donasi tertaut dibandingkan data sumber | Pemilik sama                         |                  |            |
