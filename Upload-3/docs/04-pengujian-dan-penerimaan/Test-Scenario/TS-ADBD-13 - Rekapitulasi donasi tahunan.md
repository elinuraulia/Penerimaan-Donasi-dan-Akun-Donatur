# TS-ADBD-13 Rekapitulasi donasi tahunan · Akun Donatur dan Bukti Donasi

Kelompok 2 · Dosen: Endy Muhardin · Business Analyst: Eli Nur Aulia · Project Manager: Destri Komalasari · Status: draf

Kolom hasil aktual dan status diisi saat pengujian.

Kebutuhan: FR-ADBD-13. Prioritas: Must. Prakondisi: donatur punya donasi zakat pada tahun itu.

| **ID uji** | **Teknik** | **Skenario** | **Hasil diharapkan** | **Hasil aktual** | **Status** |
|---------------|----------------------|---------------------------------------------|----------------------|------------------|------------|
| TS-ADBD-13-01 | Benar (Right) | Terbitkan rekap tahun berisi zakat | Total benar |  |  |
| TS-ADBD-13-02 | Benar (Right) | Tahun tanpa zakat | Ditolak |  |  |
| TS-ADBD-13-03 | Batas (Boundary) | Donasi 31 Desember 23.59 | Masuk tahun tersebut |  |  |
| TS-ADBD-13-04 | Batas (Boundary) | Donasi dibatalkan sebelum terbit | Tidak dihitung |  |  |
| TS-ADBD-13-05 | Silang (Cross-check) | Total rekap dibandingkan jumlah bukti zakat | Sama |  |  |
