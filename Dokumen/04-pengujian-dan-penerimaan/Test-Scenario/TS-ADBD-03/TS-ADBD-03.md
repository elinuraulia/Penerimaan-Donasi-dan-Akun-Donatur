# TS-ADBD-03 Preferensi anonimitas dan pengiriman · Akun Donatur dan Bukti Donasi

Kelompok 2 · Business Analyst: Eli Nur Aulia · Project Manager: Destri · Status: draf

Kolom hasil aktual dan status diisi saat pengujian.


Kebutuhan: FR-ADBD-03. Prioritas: Should. Prakondisi: donatur sudah login.

| **ID uji**    | **Teknik**           | **Skenario**                                           | **Hasil diharapkan**   | **Hasil aktual** | **Status** |
|---------------|----------------------|--------------------------------------------------------|------------------------|------------------|------------|
| TS-ADBD-03-01 | Benar (Right)        | Aktifkan anonim                                        | Tersimpan              |                  |            |
| TS-ADBD-03-02 | Benar (Right)        | Kirim nilai di luar pilihan                            | Ditolak                |                  |            |
| TS-ADBD-03-03 | Kebalikan (Inverse)  | Nonaktifkan anonim                                     | Nama tampil kembali    |                  |            |
| TS-ADBD-03-04 | Batas (Boundary)     | Tanpa preferensi                                       | Default dipakai        |                  |            |
| TS-ADBD-03-05 | Batas (Boundary)     | Ubah dua kali berturut-turut                           | Nilai terakhir berlaku |                  |            |
| TS-ADBD-03-06 | Batas (Boundary)     | Kabar program kosong                                   | Dianggap tidak         |                  |            |
| TS-ADBD-03-07 | Silang (Cross-check) | Preferensi dibandingkan data yang dikirim ke Proyek 11 | Sama                   |                  |            |
