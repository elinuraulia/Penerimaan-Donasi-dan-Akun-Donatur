# FR-ADBD-03 Preferensi anonimitas dan pengiriman · Akun Donatur dan Bukti Donasi

Kelompok 2 · Dosen: Endy Muhardin · Business Analyst: Eli Nur Aulia · Project Manager: Destri Komalasari · Status: draf


| **Atribut** | **Isi** |
|-------------|------------------------------------------------------------|
| Prioritas | Should |
| Sumber | Workbook 3.2; v0.2 FR-008 |
| Aktor | Donatur |
| Deskripsi | Donatur memilih tampil dengan nama atau anonim, serta cara menerima bukti. Anonim mengatur tampilan tanpa menghapus data internal. Arti anonim bagi staf belum dikonfirmasi |
| Task proses | T-01 |

**Alur**

- Prakondisi: donatur sudah masuk.
- Alur utama: (1) membuka preferensi; (2) memilih; (3) menyimpan.
- Alur alternatif: tidak mengubah, default dipakai.
- Alur kegagalan: kanal dipilih tetapi kontaknya belum terverifikasi; sistem menolak.
- Pascakondisi: preferensi tersimpan.

**Diagram alur**

![Alur FR-ADBD-03](../adbd/diagram/img/fr-fitur-03.png){height=5in}

**Acceptance criteria**

- **Given** donatur memilih anonim, **When** namanya akan tampil pada daftar umum, **Then** tampil “Hamba Allah”.
- **Given** preferensi belum diisi, **When** sistem memakainya, **Then** default tampil dengan nama [USULAN].
- **Given** belum ada nomor terverifikasi, **When** donatur memilih WhatsApp, **Then** sistem menolak.

**Mockup**

![gambar](../adbd/img/adbd-03-preferensi.png)

*Preferensi*

| **Elemen** | **Jenis** | **Perilaku** |
|---------------------|-----------|--------------------------------|
| Tampil sebagai | Pilihan | Nama atau anonim |
| Kirim bukti melalui | Pilihan | Email, WhatsApp, unduh sendiri |
| Simpan, Batal | Tombol | Menyimpan preferensi |

Pesan galat: “Verifikasi kontak untuk kanal ini terlebih dahulu.”

Test scenario lengkap: `04-pengujian-dan-penerimaan/Test-Scenario/TS-ADBD-03 - Preferensi anonimitas dan pengiriman`.
