# TS-ADBD-01 Pendaftaran akun donatur · Akun Donatur dan Bukti Donasi

Kelompok 2 · Business Analyst: Eli Nur Aulia · Project Manager: Destri · Status: draf

Kolom hasil aktual dan status diisi saat pengujian.


Kebutuhan: FR-ADBD-01. Prioritas: Must. Prakondisi: belum punya akun.

| **ID uji**    | **Teknik**           | **Skenario**                                         | **Hasil diharapkan**        | **Hasil aktual** | **Status** |
|---------------|----------------------|------------------------------------------------------|-----------------------------|------------------|------------|
| TS-ADBD-01-01 | Benar (Right)        | Daftar dengan data lengkap                           | Akun dibuat                 |                  |            |
| TS-ADBD-01-02 | Benar (Right)        | Daftar tanpa nama                                    | Ditolak: “Nama wajib diisi” |                  |            |
| TS-ADBD-01-03 | Kebalikan (Inverse)  | Daftar lalu login                                    | Data profil sama            |                  |            |
| TS-ADBD-01-04 | Batas (Boundary)     | Kata sandi 7 karakter                                | Ditolak                     |                  |            |
| TS-ADBD-01-05 | Batas (Boundary)     | Kata sandi 8 karakter                                | Diterima                    |                  |            |
| TS-ADBD-01-06 | Batas (Boundary)     | Nama 101 karakter                                    | Ditolak                     |                  |            |
| TS-ADBD-01-07 | Silang (Cross-check) | Jumlah akun dibandingkan jumlah pendaftaran berhasil | Sama                        |                  |            |
