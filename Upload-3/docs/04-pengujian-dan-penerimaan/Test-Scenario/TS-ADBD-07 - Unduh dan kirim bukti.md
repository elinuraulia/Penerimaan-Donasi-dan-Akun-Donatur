# TS-ADBD-07 Unduh dan kirim bukti · Akun Donatur dan Bukti Donasi

Kelompok 2 · Dosen: Endy Muhardin · Business Analyst: Eli Nur Aulia · Project Manager: Destri Komalasari · Status: draf

Kolom hasil aktual dan status diisi saat pengujian.

Kebutuhan: FR-ADBD-07. Prioritas: Must. Prakondisi: bukti sudah terbit.

| **ID uji** | **Teknik** | **Skenario** | **Hasil diharapkan** | **Hasil aktual** | **Status** |
|---------------|----------------------|-------------------------------------|------------------------------------|------------------|------------|
| TS-ADBD-07-01 | Benar (Right) | Kirim ke email terverifikasi | Message terbit dan status Terkirim |  |  |
| TS-ADBD-07-02 | Benar (Right) | Donatur lain mengunduh | Ditolak 403 |  |  |
| TS-ADBD-07-03 | Kebalikan (Inverse) | Unduh lalu bandingkan | Sama dengan bukti tersimpan |  |  |
| TS-ADBD-07-04 | Batas (Boundary) | Tanpa kontak terverifikasi | Hanya unduh |  |  |
| TS-ADBD-07-05 | Batas (Boundary) | Kirim ulang | Tercatat, nomor bukti sama |  |  |
| TS-ADBD-07-06 | Silang (Cross-check) | Log kirim dibandingkan topic status | Sama |  |  |
