# TS-ADBD-04 Penyatuan donasi ke akun · Akun Donatur dan Bukti Donasi

Kelompok 2 · Dosen: Endy Muhardin · Business Analyst: Eli Nur Aulia · Project Manager: Destri Komalasari · Status: draf

Kolom hasil aktual dan status diisi saat pengujian.

Kebutuhan: FR-ADBD-04. Prioritas: Must. Prakondisi: data donasi tersedia lewat API.

| **ID uji** | **Teknik** | **Skenario** | **Hasil diharapkan** | **Hasil aktual** | **Status** |
|---------------|----------------------|--------------------------------------------|--------------------------------------|------------------|------------|
| TS-ADBD-04-01 | Benar (Right) | Email terverifikasi sama | Disatukan otomatis |  |  |
| TS-ADBD-04-02 | Benar (Right) | Nomor terverifikasi sama | Disatukan otomatis |  |  |
| TS-ADBD-04-03 | Benar (Right) | Nomor sama tetapi belum diverifikasi | Tidak disatukan |  |  |
| TS-ADBD-04-04 | Benar (Right) | Hanya nama mirip | Tidak disatukan otomatis |  |  |
| TS-ADBD-04-05 | Kebalikan (Inverse) | Penyatuan dibatalkan | Donasi keluar dari riwayat; tercatat |  |  |
| TS-ADBD-04-06 | Batas (Boundary) | Satu nomor cocok dengan dua akun | Masuk antrean |  |  |
| TS-ADBD-04-07 | Silang (Cross-check) | Donasi tersatukan dibandingkan data sumber | Kontak cocok dengan dasar tercatat |  |  |
