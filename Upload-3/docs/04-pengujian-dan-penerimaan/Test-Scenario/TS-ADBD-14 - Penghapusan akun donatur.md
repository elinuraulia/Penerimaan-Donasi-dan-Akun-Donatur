# TS-ADBD-14 Penghapusan akun donatur · Akun Donatur dan Bukti Donasi

Kelompok 2 · Dosen: Endy Muhardin · Business Analyst: Eli Nur Aulia · Project Manager: Destri Komalasari · Status: draf

Kolom hasil aktual dan status diisi saat pengujian.

Kebutuhan: FR-ADBD-14. Prioritas: Must. Prakondisi: donatur sudah masuk.

| **ID uji** | **Teknik** | **Skenario** | **Hasil diharapkan** | **Hasil aktual** | **Status** |
|---------------|----------------------|-------------------------------------------|---------------------------------------------------------|------------------|------------|
| TS-ADBD-14-01 | Benar (Right) | Hapus dengan konfirmasi benar | Tidak dapat masuk ke akun lama |  |  |
| TS-ADBD-14-02 | Benar (Right) | Konfirmasi salah | Akun tetap |  |  |
| TS-ADBD-14-03 | Kebalikan (Inverse) | Daftar ulang dengan nomor sama | Akun baru; donasi tidak otomatis memakai penyatuan lama |  |  |
| TS-ADBD-14-04 | Silang (Cross-check) | Jumlah catatan donasi sebelum dan sesudah | Sama |  |  |
