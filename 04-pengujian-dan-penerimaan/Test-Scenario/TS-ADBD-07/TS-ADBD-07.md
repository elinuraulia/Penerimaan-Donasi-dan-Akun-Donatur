# TS-ADBD-07 Unduh dan kirim bukti · Akun Donatur dan Bukti Donasi

Kelompok 2 · Business Analyst: Eli Nur Aulia · Project Manager: Destri · Status: draf

Kolom hasil aktual dan status diisi saat pengujian.


Kebutuhan: FR-ADBD-07. Prioritas: Must. Prakondisi: bukti sudah terbit.

| **ID uji**    | **Teknik**           | **Skenario**                         | **Hasil diharapkan**        | **Hasil aktual** | **Status** |
|---------------|----------------------|--------------------------------------|-----------------------------|------------------|------------|
| TS-ADBD-07-01 | Benar (Right)        | Kirim ke email terverifikasi         | Terkirim                    |                  |            |
| TS-ADBD-07-02 | Benar (Right)        | Donatur lain mengunduh               | Ditolak 403                 |                  |            |
| TS-ADBD-07-03 | Kebalikan (Inverse)  | Unduh lalu bandingkan                | Sama dengan tampilan        |                  |            |
| TS-ADBD-07-04 | Batas (Boundary)     | Tanpa email terverifikasi            | Hanya unduh                 |                  |            |
| TS-ADBD-07-05 | Batas (Boundary)     | Kirim ulang                          | Tercatat, nomor bukti sama  |                  |            |
| TS-ADBD-07-06 | Batas (Boundary)     | Percobaan ke-3 gagal \[USULAN\]      | Berhenti dan ditandai gagal |                  |            |
| TS-ADBD-07-07 | Silang (Cross-check) | Log kirim dibandingkan layanan email | Sama                        |                  |            |
