# TS-ADBD-06 Penerbitan bukti donasi · Akun Donatur dan Bukti Donasi

Kelompok 2 · Business Analyst: Eli Nur Aulia · Project Manager: Destri · Status: draf

Kolom hasil aktual dan status diisi saat pengujian.


Kebutuhan: FR-ADBD-06. Prioritas: Must. Prakondisi: donasi berstatus Berhasil.

| **ID uji**    | **Teknik**           | **Skenario**                       | **Hasil diharapkan**     | **Hasil aktual** | **Status** |
|---------------|----------------------|------------------------------------|--------------------------|------------------|------------|
| TS-ADBD-06-01 | Benar (Right)        | Terbitkan untuk donasi Berhasil    | Bukti dibuat             |                  |            |
| TS-ADBD-06-02 | Benar (Right)        | Terbitkan untuk donasi Gagal       | Ditolak                  |                  |            |
| TS-ADBD-06-03 | Kebalikan (Inverse)  | Donasi dikembalikan                | Bukti menjadi Dibatalkan |                  |            |
| TS-ADBD-06-04 | Batas (Boundary)     | Dua permintaan bersamaan           | Satu bukti               |                  |            |
| TS-ADBD-06-05 | Batas (Boundary)     | Nominal 1                          | Tampil benar             |                  |            |
| TS-ADBD-06-06 | Batas (Boundary)     | Nama 100 karakter                  | Tidak terpotong          |                  |            |
| TS-ADBD-06-07 | Silang (Cross-check) | Isi bukti dibandingkan data donasi | Sama persis              |                  |            |
