# TS-ADBD-15 Kanal WhatsApp pada Aplikasi Notifikasi · Akun Donatur dan Bukti Donasi

Kelompok 2 · Dosen: Endy Muhardin · Business Analyst: Eli Nur Aulia · Project Manager: Destri Komalasari · Status: draf

Kolom hasil aktual dan status diisi saat pengujian.

Kebutuhan: FR-ADBD-15. Prioritas: Should. Prakondisi: akun bisnis, nomor, dan template disetujui Meta.

| **ID uji** | **Teknik** | **Skenario** | **Hasil diharapkan** | **Hasil aktual** | **Status** |
|---------------|----------------------|-------------------------------------------------|-----------------------------|------------------|------------|
| TS-ADBD-15-01 | Benar (Right) | Kirim dengan template disetujui (data sintetis) | Terkirim ke penyedia tiruan |  |  |
| TS-ADBD-15-02 | Benar (Right) | Template belum disetujui | Status gagal |  |  |
| TS-ADBD-15-03 | Batas (Boundary) | Variabel kurang | Tidak dikirim |  |  |
| TS-ADBD-15-04 | Batas (Boundary) | Message sama dibaca dua kali | Satu pengiriman |  |  |
| TS-ADBD-15-05 | Silang (Cross-check) | Status di topic dibandingkan respons penyedia | Sama |  |  |
