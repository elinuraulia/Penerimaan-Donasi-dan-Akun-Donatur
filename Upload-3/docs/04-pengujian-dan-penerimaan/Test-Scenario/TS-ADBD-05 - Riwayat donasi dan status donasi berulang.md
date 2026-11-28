# TS-ADBD-05 Riwayat donasi dan status donasi berulang · Akun Donatur dan Bukti Donasi

Kelompok 2 · Dosen: Endy Muhardin · Business Analyst: Eli Nur Aulia · Project Manager: Destri Komalasari · Status: draf

Kolom hasil aktual dan status diisi saat pengujian.

Kebutuhan: FR-ADBD-05. Prioritas: Must. Prakondisi: donatur sudah masuk.

| **ID uji** | **Teknik** | **Skenario** | **Hasil diharapkan** | **Hasil aktual** | **Status** |
|---------------|----------------------|-------------------------------------------|-----------------------------|------------------|------------|
| TS-ADBD-05-01 | Benar (Right) | Buka riwayat | Tampil donasi milik sendiri |  |  |
| TS-ADBD-05-02 | Benar (Right) | Buka riwayat orang lain | Ditolak 403 |  |  |
| TS-ADBD-05-03 | Benar (Right) | Tekan Kelola | Diarahkan tanpa login ulang |  |  |
| TS-ADBD-05-04 | Kebalikan (Inverse) | Filter lalu kosongkan | Seluruh data kembali |  |  |
| TS-ADBD-05-05 | Batas (Boundary) | Akhir sebelum awal | Ditolak |  |  |
| TS-ADBD-05-06 | Batas (Boundary) | Layanan Donasi Berulang mati | Riwayat tetap tampil |  |  |
| TS-ADBD-05-07 | Silang (Cross-check) | Total dibandingkan data Penerimaan Donasi | Sama |  |  |
