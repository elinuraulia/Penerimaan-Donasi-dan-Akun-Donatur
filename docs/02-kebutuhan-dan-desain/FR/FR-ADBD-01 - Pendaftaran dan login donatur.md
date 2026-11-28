# FR-ADBD-01 Pendaftaran dan login donatur · Akun Donatur dan Bukti Donasi

Kelompok 2 · Dosen: Endy Muhardin · Business Analyst: Eli Nur Aulia · Project Manager: Destri Komalasari · Status: draf


| **Atribut** | **Isi** |
|-------------|------------------------------------------------------------|
| Prioritas | Must |
| Sumber | Workbook 3.2, 3.7 |
| Aktor | Donatur |
| Deskripsi | Donatur masuk dengan akun Google atau OTP ke nomor telepon, tanpa kata sandi. Donatur yang masuk dengan Google memverifikasi nomor teleponnya satu kali lewat OTP sebelum donasi bernomor itu disatukan. Akun Google dikenali dari pengenal tetapnya, bukan dari alamat email. Satu akun memuat satu identitas Google serta beberapa nomor telepon dan email terverifikasi |
| Task proses | T-01 |

**Alur**

- Prakondisi: donatur punya akun Google atau nomor telepon aktif.
- Alur utama: (1) donatur memilih Google atau nomor telepon; (2) membuktikan identitas; (3) menyetujui penggunaan data; (4) akun dibuat dan sesi aktif.
- Alur alternatif: pengguna Google memverifikasi nomor telepon lewat OTP.
- Alur kegagalan: OTP salah, kedaluwarsa, atau melewati batas kirim; sistem menolak.
- Pascakondisi: donatur masuk dan identitas terverifikasi tercatat.

**Diagram alur**

![Alur FR-ADBD-01](../adbd/diagram/img/fr-fitur-01.png){height=5in}

**Acceptance criteria**

- **Given** nomor belum terdaftar dan OTP benar, **When** donatur menyetujui penggunaan data, **Then** akun dibuat dengan nomor terverifikasi.
- **Given** donatur masuk dengan Google dan nomornya belum diverifikasi, **When** data donasi bernomor itu tersedia, **Then** donasi belum disatukan.
- **Given** sudah 3 permintaan OTP dalam 15 menit [USULAN], **When** donatur meminta lagi, **Then** sistem menolak.

**Mockup**

![gambar](../adbd/img/adbd-01-daftar.png)

*Masuk atau daftar*

| **Elemen** | **Jenis** | **Perilaku** |
|--------------------------|------------------|-----------------------------------|
| Masuk dengan Google | Tombol | Memakai OpenID Connect |
| Nomor telepon, Kirim OTP | Kolom dan tombol | Jumlah kirim dibatasi |
| Kode OTP | Kolom | 6 digit, berlaku 5 menit [USULAN] |
| Persetujuan data | Centang | Wajib saat akun baru |

Pesan galat: “Kode OTP salah atau kedaluwarsa.”; “Terlalu banyak permintaan. Coba lagi nanti.”

Test scenario lengkap: `04-pengujian-dan-penerimaan/Test-Scenario/TS-ADBD-01 - Pendaftaran dan login donatur`.
