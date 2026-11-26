# TS-ADBD-02 Pengelolaan profil donatur · Akun Donatur dan Bukti Donasi

Kelompok 2 · Business Analyst: Eli Nur Aulia · Project Manager: Destri · Status: draf

Kolom hasil aktual dan status diisi saat pengujian.


Kebutuhan: FR-ADBD-02. Prioritas: Must. Prakondisi: donatur sudah login.

| **ID uji**    | **Teknik**           | **Skenario**                                  | **Hasil diharapkan**       | **Hasil aktual** | **Status** |
|---------------|----------------------|-----------------------------------------------|----------------------------|------------------|------------|
| TS-ADBD-02-01 | Benar (Right)        | Ubah nomor telepon                            | Tersimpan                  |                  |            |
| TS-ADBD-02-02 | Benar (Right)        | Kosongkan nama                                | Ditolak                    |                  |            |
| TS-ADBD-02-03 | Kebalikan (Inverse)  | Simpan lalu buka kembali                      | Isi sama                   |                  |            |
| TS-ADBD-02-04 | Batas (Boundary)     | Telepon 7 digit                               | Ditolak                    |                  |            |
| TS-ADBD-02-05 | Batas (Boundary)     | Telepon 8 digit                               | Diterima                   |                  |            |
| TS-ADBD-02-06 | Batas (Boundary)     | Telepon 16 digit                              | Ditolak                    |                  |            |
| TS-ADBD-02-07 | Silang (Cross-check) | Data tersimpan dibandingkan atribut disetujui | Tidak ada atribut tambahan |                  |            |
