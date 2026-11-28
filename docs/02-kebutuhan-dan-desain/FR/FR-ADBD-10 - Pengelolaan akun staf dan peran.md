# FR-ADBD-10 Pengelolaan akun staf dan peran · Akun Donatur dan Bukti Donasi

Kelompok 2 · Dosen: Endy Muhardin · Business Analyst: Eli Nur Aulia · Project Manager: Destri Komalasari · Status: draf


| **Atribut** | **Isi** |
|-------------|------------------------------------------------------------|
| Prioritas | Must |
| Sumber | Workbook Lampiran A; v0.2 NFR-001 |
| Aktor | Admin |
| Deskripsi | Admin mendaftarkan akun Google staf pada tabel pengguna aplikasi, menetapkan peran, dan menonaktifkan akun. Aplikasi tidak menyimpan kata sandi |
| Task proses | T-01 sampai T-06 |

**Alur**

- Prakondisi: berperan Admin.
- Alur utama: (1) menambah email staf; (2) menetapkan peran; (3) menyimpan; (4) pengenal Google dicatat saat staf pertama masuk.
- Alur alternatif: Admin menonaktifkan akun.
- Alur kegagalan: non-Admin; ditolak 403.
- Pascakondisi: akun tersimpan.

**Diagram alur**

![Alur FR-ADBD-10](../adbd/diagram/img/fr-fitur-10.png){height=5in}

**Acceptance criteria**

- **Given** Admin mengisi email staf dan peran, **When** menyimpan, **Then** staf dapat masuk sesuai peran.
- **Given** akun dinonaktifkan, **When** staf mencoba masuk, **Then** ditolak.
- **Given** non-Admin, **When** membuat akun, **Then** ditolak 403.

**Mockup**

![gambar](../adbd/img/adbd-10-akun.png)

*Kelola akun staf*

| **Elemen** | **Jenis** | **Perilaku** |
|---------------------|-----------|----------------------|
| Tabel akun | Tabel | Email, peran, status |
| Email Google, Peran | Kolom | Wajib |
| Simpan, Batal | Tombol | Hanya Admin |

Pesan galat: “Email tidak valid atau sudah terdaftar.”; “Pilih peran.”

Test scenario lengkap: `04-pengujian-dan-penerimaan/Test-Scenario/TS-ADBD-10 - Pengelolaan akun staf dan peran`.
