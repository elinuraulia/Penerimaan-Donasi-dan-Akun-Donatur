# FR-ADBD-07 Unduh dan kirim bukti · Akun Donatur dan Bukti Donasi

Kelompok 2 · Dosen: Endy Muhardin · Business Analyst: Eli Nur Aulia · Project Manager: Destri Komalasari · Status: draf


| **Atribut** | **Isi** |
|-------------|------------------------------------------------------------|
| Prioritas | Must |
| Sumber | Workbook 3.2, 3.5 |
| Aktor | Donatur, petugas donasi |
| Deskripsi | Bukti dapat diunduh sebagai PDF dan dikirim lewat Aplikasi Notifikasi Tazkia dengan email, serta WhatsApp setelah kanalnya berjalan. Status pengiriman dibaca dari topic status |
| Task proses | T-05 |

**Alur**

- Prakondisi: bukti sudah terbit.
- Alur utama: (1) membuka bukti; (2) mengunduh atau meminta kirim; (3) sistem menerbitkan message ke Kafka; (4) membaca status.
- Alur alternatif: kanal WhatsApp belum berjalan; dikirim lewat email.
- Alur kegagalan: pengiriman gagal; status tidak menjadi Terkirim.
- Pascakondisi: donatur menerima bukti.

**Diagram alur**

![Alur FR-ADBD-07](../adbd/diagram/img/fr-fitur-07.png){height=5in}

**Acceptance criteria**

- **Given** bukti Terbit, **When** donatur menekan Unduh PDF, **Then** berkas PDF terunduh.
- **Given** topic status melaporkan gagal, **When** sistem membacanya, **Then** status tidak menjadi Terkirim dan kegagalan dicatat.
- **Given** donatur lain sudah masuk, **When** mengunduh bukti, **Then** ditolak 403.

**Mockup**

![gambar](../adbd/img/adbd-06-bukti.png)

*Unduh dan kirim*

| **Elemen** | **Jenis** | **Perilaku** |
|------------|-----------|-------------------------|
| Unduh PDF | Tombol | Pemilik atau petugas |
| Kirim | Tombol | Ke kontak terverifikasi |

Pesan galat: “Pengiriman gagal, coba lagi.”

Test scenario lengkap: `04-pengujian-dan-penerimaan/Test-Scenario/TS-ADBD-07 - Unduh dan kirim bukti`.
