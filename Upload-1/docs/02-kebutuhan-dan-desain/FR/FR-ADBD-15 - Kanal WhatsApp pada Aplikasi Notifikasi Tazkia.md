# FR-ADBD-15 Kanal WhatsApp pada Aplikasi Notifikasi Tazkia · Akun Donatur dan Bukti Donasi

Kelompok 2 · Dosen: Endy Muhardin · Business Analyst: Eli Nur Aulia · Project Manager: Destri Komalasari · Status: draf


| **Atribut** | **Isi** |
|-------------|------------------------------------------------------------|
| Prioritas | Should |
| Sumber | Workbook 3.2, 3.7 |
| Aktor | Aplikasi Notifikasi, subsistem pengirim |
| Deskripsi | Aplikasi pengirim WhatsApp membaca topic Kafka kanalnya lalu mengirim lewat API Meta memakai template yang disetujui Meta. Aplikasi template memetakan variabel bernama ke variabel bernomor. Status pengiriman diterbitkan ke topic yang dapat dibaca subsistem pengirim. Hanya pesan keluar |
| Task proses | T-05 |

**Alur**

- Prakondisi: akun bisnis, nomor, dan template disetujui Meta.
- Alur utama: (1) message masuk topic; (2) template diisi; (3) dikirim lewat API Meta; (4) status diterbitkan.
- Alur alternatif: kanal belum siap; konfigurasi template tetap memakai email.
- Alur kegagalan: Meta menolak atau gagal; status gagal diterbitkan.
- Pascakondisi: status pengiriman tersedia.

**Diagram alur**

![Alur FR-ADBD-15](../adbd/diagram/img/fr-fitur-15.png){height=5in}

**Acceptance criteria**

- **Given** template disetujui dan message valid, **When** message dibaca, **Then** dikirim dengan variabel pada urutan yang benar.
- **Given** API Meta mengembalikan galat, **When** pengiriman dicoba, **Then** topic status memuat gagal.
- **Given** template belum disetujui, **When** message dibaca, **Then** tidak dikirim dan status gagal diterbitkan.

**Mockup**

Tidak berlaku: kebutuhan ini antarsistem, tanpa layar pengguna.

Test scenario lengkap: `04-pengujian-dan-penerimaan/Test-Scenario/TS-ADBD-15 - Kanal WhatsApp pada Aplikasi Notifikasi Tazkia`.
