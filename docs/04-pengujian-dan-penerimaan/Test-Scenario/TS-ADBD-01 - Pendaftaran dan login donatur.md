# TS-ADBD-01 Pendaftaran dan login donatur · Akun Donatur dan Bukti Donasi

Kelompok 2 · Dosen: Endy Muhardin · Business Analyst: Eli Nur Aulia · Project Manager: Destri Komalasari · Status: draf

Kolom hasil aktual dan status diisi saat pengujian.

Kebutuhan: FR-ADBD-01. Prioritas: Must. Prakondisi: donatur punya akun Google atau nomor telepon aktif.

| **ID uji** | **Teknik** | **Skenario** | **Hasil diharapkan** | **Hasil aktual** | **Status** |
|---------------|----------------------|-------------------------------------------|------------------------|------------------|------------|
| TS-ADBD-01-01 | Benar (Right) | OTP benar pada nomor baru | Akun dibuat |  |  |
| TS-ADBD-01-02 | Benar (Right) | OTP salah | Ditolak |  |  |
| TS-ADBD-01-03 | Kebalikan (Inverse) | Keluar lalu masuk lagi | Akun yang sama terbuka |  |  |
| TS-ADBD-01-04 | Batas (Boundary) | OTP dipakai pada menit ke-6 | Ditolak kedaluwarsa |  |  |
| TS-ADBD-01-05 | Batas (Boundary) | Permintaan OTP ke-4 dalam 15 menit | Ditolak |  |  |
| TS-ADBD-01-06 | Batas (Boundary) | Persetujuan tidak dicentang | Akun tidak dibuat |  |  |
| TS-ADBD-01-07 | Silang (Cross-check) | Email akun Google berubah, pengenal tetap | Akun yang sama terbuka |  |  |
