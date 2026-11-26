# TS-ADBD-09 Pembatasan akses menurut peran · Akun Donatur dan Bukti Donasi

Kelompok 2 · Business Analyst: Eli Nur Aulia · Project Manager: Destri · Status: draf

Kolom hasil aktual dan status diisi saat pengujian.


Kebutuhan: FR-ADBD-09. Prioritas: Must. Prakondisi: akun dengan peran berbeda tersedia.

| **ID uji**    | **Teknik**           | **Skenario**                              | **Hasil diharapkan** | **Hasil aktual** | **Status** |
|---------------|----------------------|-------------------------------------------|----------------------|------------------|------------|
| TS-ADBD-09-01 | Benar (Right)        | Pemilik membuka datanya                   | Diizinkan            |                  |            |
| TS-ADBD-09-02 | Benar (Right)        | Non-Admin membuka kelola akun             | Ditolak              |                  |            |
| TS-ADBD-09-03 | Kebalikan (Inverse)  | Peran dicabut                             | Akses ditolak        |                  |            |
| TS-ADBD-09-04 | Batas (Boundary)     | Tanpa peran                               | Ditolak semua        |                  |            |
| TS-ADBD-09-05 | Batas (Boundary)     | Peran terendah mencoba tindakan tertinggi | Ditolak              |                  |            |
| TS-ADBD-09-06 | Batas (Boundary)     | Token kedaluwarsa                         | Diminta login        |                  |            |
| TS-ADBD-09-07 | Silang (Cross-check) | Matriks akses dibandingkan perilaku       | Sama                 |                  |            |
