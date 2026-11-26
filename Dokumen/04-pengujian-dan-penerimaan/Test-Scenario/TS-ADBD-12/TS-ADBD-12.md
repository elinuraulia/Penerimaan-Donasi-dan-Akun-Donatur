# TS-ADBD-12 Penyediaan data untuk proyek hilir · Akun Donatur dan Bukti Donasi

Kelompok 2 · Business Analyst: Eli Nur Aulia · Project Manager: Destri · Status: draf

Kolom hasil aktual dan status diisi saat pengujian.


Kebutuhan: FR-ADBD-12. Prioritas: Should. Prakondisi: kredensial sah.

| **ID uji**    | **Teknik**           | **Skenario**                         | **Hasil diharapkan**           | **Hasil aktual** | **Status** |
|---------------|----------------------|--------------------------------------|--------------------------------|------------------|------------|
| TS-ADBD-12-01 | Benar (Right)        | Ambil data donatur                   | Sesuai kontrak                 |                  |            |
| TS-ADBD-12-02 | Benar (Right)        | Kredensial salah                     | 401 atau 403                   |                  |            |
| TS-ADBD-12-03 | Kebalikan (Inverse)  | Data API dibandingkan sumber         | Sama                           |                  |            |
| TS-ADBD-12-04 | Batas (Boundary)     | Nol donatur                          | Daftar kosong                  |                  |            |
| TS-ADBD-12-05 | Batas (Boundary)     | Donatur menolak kabar program        | Ditandai tidak boleh dihubungi |                  |            |
| TS-ADBD-12-06 | Batas (Boundary)     | Periode awal sama dengan akhir       | Diterima                       |                  |            |
| TS-ADBD-12-07 | Silang (Cross-check) | Jumlah donatur dibandingkan aplikasi | Sama                           |                  |            |
