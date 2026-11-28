# Kesulitan Fitur (Internal) · Akun Donatur dan Bukti Donasi

Kelompok 2 · Business Analyst: Eli Nur Aulia · Project Manager: Destri Komalasari · Status: draf

Dokumen internal tim, bukan untuk klien. Penilaian ini **\[USULAN\]** awal sebelum teknologi dipilih; tinjau ulang bersama pengembang.

| Fitur | Kesulitan | Alasan | Risiko |
|---|---|---|---|
| FR-ADBD-01 Pendaftaran dan login donatur | Sedang sampai tinggi | Dua cara masuk, OTP, batas percobaan | Pengambilalihan akun |
| FR-ADBD-02 Pengelolaan profil donatur | Rendah sampai sedang | Verifikasi kontak tambahan | Data ganda |
| FR-ADBD-03 Preferensi anonimitas dan pengiriman | Rendah | Pilihan sederhana | Arti anonim belum jelas |
| FR-ADBD-04 Penyatuan donasi ke akun | Tinggi | Pencocokan bertingkat, antrean, pembatalan | Riwayat dua orang tercampur |
| FR-ADBD-05 Riwayat donasi dan status donasi berulang | Sedang | Bergantung pada dua subsistem lain | Kontrak API belum ada |
| FR-ADBD-06 Penerbitan bukti donasi | Sedang | Nomor urut dan salinan tetap | Penerbitan ganda |
| FR-ADBD-07 Unduh dan kirim bukti | Sedang | Pengiriman lewat Kafka dan status | Status tidak sinkron |
| FR-ADBD-08 Verifikasi keaslian bukti | Rendah | Pencarian berdasar kode | Kode dapat ditebak |
| FR-ADBD-09 Pembatasan akses dan login staf | Sedang sampai tinggi | OpenID Connect, TOTP, otorisasi terpusat | Akses tidak sah |
| FR-ADBD-10 Pengelolaan akun staf dan peran | Rendah | Kelola data akun | Salah peran |
| FR-ADBD-11 Log akses data pribadi | Rendah sampai sedang | Pencatatan di setiap akses | Log tidak lengkap |
| FR-ADBD-13 Rekapitulasi donasi tahunan | Sedang | Penjumlahan per tahun dan salinan tetap | Format pajak belum diketahui |
| FR-ADBD-14 Penghapusan akun donatur | Sedang sampai tinggi | Memutus hubungan tanpa menghapus catatan audit | Catatan wajib ikut terhapus |
| FR-ADBD-15 Kanal WhatsApp pada Aplikasi Notifikasi Tazkia | Tinggi | API Meta, template, topic status | Persetujuan Meta terlambat |

**Urutan kerja yang disarankan.** FR-ADBD-09 dan 01 lebih dulu; lalu 02, 04, 05, 06, 07; kemudian 13, 14, 03, 10, 11; FR-ADBD-15 dikerjakan awal bila persetujuan Meta sudah diajukan; FR-ADBD-08 terakhir.
