# TS-ADBD-09 Pembatasan akses dan login staf · Akun Donatur dan Bukti Donasi

Kelompok 2 · Dosen: Endy Muhardin · Business Analyst: Eli Nur Aulia · Project Manager: Destri Komalasari · Status: draf

Kolom hasil aktual dan status diisi saat pengujian.

Kebutuhan: FR-ADBD-09. Prioritas: Must. Prakondisi: staf punya akun Google.

| **ID uji** | **Teknik** | **Skenario** | **Hasil diharapkan** | **Hasil aktual** | **Status** |
|---------------|----------------------|------------------------------|----------------------|------------------|------------|
| TS-ADBD-09-01 | Benar (Right) | Staf terdaftar, TOTP benar | Menu sesuai peran |  |  |
| TS-ADBD-09-02 | Benar (Right) | Akun Google tidak terdaftar | Halaman kosong |  |  |
| TS-ADBD-09-03 | Benar (Right) | Donatur memanggil API admin | Ditolak 403 |  |  |
| TS-ADBD-09-04 | Batas (Boundary) | ID token kedaluwarsa | Ditolak |  |  |
| TS-ADBD-09-05 | Batas (Boundary) | ID token untuk audience lain | Ditolak |  |  |
| TS-ADBD-09-06 | Silang (Cross-check) | Hak di API dibandingkan menu | Sama |  |  |
