# FR-ADBD-04 Penyatuan donasi ke akun · Akun Donatur dan Bukti Donasi

Kelompok 2 · Dosen: Endy Muhardin · Business Analyst: Eli Nur Aulia · Project Manager: Destri Komalasari · Status: draf


| **Atribut** | **Isi** |
|-------------|------------------------------------------------------------|
| Prioritas | Must |
| Sumber | Workbook 3.2, 3.7; v0.2 FR-007 |
| Aktor | Sistem, petugas donasi, donatur |
| Deskripsi | Sistem menyatukan donasi dari semua kanal secara bertingkat. Email terverifikasi (Google atau OTP) atau nomor telepon terverifikasi OTP yang sama disatukan otomatis. Kecocokan yang hanya mirip masuk antrean konfirmasi staf atau donatur. Setiap penyatuan menyimpan dasar kecocokannya dan dapat dibatalkan |
| Task proses | T-03 |

**Alur**

- Prakondisi: data donasi tersedia lewat API.
- Alur utama: (1) sistem menerima donasi; (2) membandingkan dengan identitas terverifikasi; (3) menyatukan dan mencatat dasarnya.
- Alur alternatif: kecocokan mirip masuk antrean; staf atau donatur mengonfirmasi atau menolak.
- Alur kegagalan: donasi sudah milik akun lain; sistem menolak.
- Pascakondisi: donasi tersatukan atau menunggu konfirmasi.

**Diagram alur**

![Alur FR-ADBD-04](../adbd/diagram/img/fr-fitur-04.png){height=5in}

**Acceptance criteria**

- **Given** donasi bernomor sama dengan nomor terverifikasi akun, **When** data diterima, **Then** donasi disatukan dengan dasar “nomor terverifikasi”.
- **Given** hanya nama yang mirip, **When** data diterima, **Then** donasi tidak disatukan otomatis.
- **Given** penyatuan keliru, **When** petugas membatalkannya dengan alasan, **Then** donasi hilang dari riwayat dan pembatalan tercatat.

**Mockup**

![gambar](../adbd/img/adbd-04-penautan.png)

*Antrean konfirmasi*

| **Elemen** | **Jenis** | **Perilaku** |
|----------------|-----------|----------------------------------------|
| Antrean | Tabel | Donasi, kandidat akun, dasar kecocokan |
| Satukan, Tolak | Tautan | Alasan wajib bagi petugas |
| Batalkan | Tautan | Melepas penyatuan |

Pesan galat: “Donasi sudah disatukan ke akun lain.”; “Alasan wajib diisi.”

Test scenario lengkap: `04-pengujian-dan-penerimaan/Test-Scenario/TS-ADBD-04 - Penyatuan donasi ke akun`.
