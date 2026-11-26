# Daftar Fitur · Akun Donatur dan Bukti Donasi

Kelompok 2 · Business Analyst: Eli Nur Aulia · Project Manager: Destri · Status: draf

| Fitur | Nama | Penjelasan | Rujukan |
|---|---|---|---|
| Fitur 01 | Pendaftaran akun donatur | Sistem membuat akun donatur dari nama, email, kata sandi, dan persetujuan penggunaan data; email diverifikasi lewat tautan | FR-ADBD-01 |
| Fitur 02 | Pengelolaan profil donatur | Donatur melihat dan mengubah data yang disetujui; perubahan dicatat | FR-ADBD-02 |
| Fitur 03 | Penautan donasi ke akun | Sistem menautkan donasi ke akun bila email terverifikasi sama; kasus tidak pasti ditinjau petugas; tidak menautkan berdasarkan nama saja | FR-ADBD-04 |
| Fitur 04 | Riwayat donasi | Sistem menampilkan donasi tertaut dengan filter periode dan peruntukan serta total donasi berstatus Berhasil | FR-ADBD-05 |
| Fitur 05 | Penerbitan bukti donasi | Sistem menerbitkan satu bukti per donasi berstatus Berhasil, berisi nomor bukti unik, referensi, nama, tanggal, nominal, peruntukan, dan kode verifikasi. Bila donasi dibatalkan atau dikembalikan, bukti ditandai Dibatalkan | FR-ADBD-06 |
| Fitur 06 | Unduh dan kirim bukti | Bukti dapat diunduh sebagai PDF dan dikirim ke email donatur sesuai preferensi; status pengiriman dicatat | FR-ADBD-07 |
| Fitur 07 | Pembatasan akses menurut peran | Sistem membatasi data menurut peran dan kepemilikan, diterapkan terpusat di server | FR-ADBD-09 |
| Fitur 08 | Pengelolaan akun dan peran | Admin membuat akun internal, menonaktifkan akun, dan menetapkan peran. Login mengikuti FR Umum 1 | FR-ADBD-10 |
| Fitur 09 | Preferensi anonimitas dan pengiriman | Sistem menyimpan preferensi anonim, cara kirim bukti, dan kabar program; anonim mengatur tampilan tanpa menghapus data internal | FR-ADBD-03 |
| Fitur 10 | Log akses data pribadi | Sistem mencatat siapa membuka atau mengubah data donatur atau bukti siapa dan kapan | FR-ADBD-11 |
| Fitur 11 | Penyediaan data untuk proyek hilir | Sistem menyediakan lewat API: data donatur dan preferensi (IF-02) serta jumlah donatur tanpa identitas (IF-03) | FR-ADBD-12 |
| Fitur 12 | Verifikasi keaslian bukti | Siapa pun yang memiliki kode dapat memeriksa keabsahan; hasil hanya memuat status, nomor, tanggal, dan nominal tanpa identitas | FR-ADBD-08 |
