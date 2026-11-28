# FR-ADBD-09 Pembatasan akses dan login staf · Akun Donatur dan Bukti Donasi

Kelompok 2 · Dosen: Endy Muhardin · Business Analyst: Eli Nur Aulia · Project Manager: Destri Komalasari · Status: draf


| **Atribut** | **Isi** |
|-------------|------------------------------------------------------------|
| Prioritas | Must |
| Sumber | Workbook Lampiran A; v0.2 NFR-001 |
| Aktor | Semua peran |
| Deskripsi | Staf masuk dengan akun Google (OpenID Connect) lalu verifikasi TOTP. ID token divalidasi di server. Akun yang belum terdaftar hanya melihat halaman awal kosong. Data dibatasi menurut peran dan kepemilikan, diperiksa terpusat di server |
| Task proses | T-01 sampai T-06 |

**Alur**

- Prakondisi: staf punya akun Google.
- Alur utama: (1) masuk dengan Google; (2) memasukkan kode TOTP; (3) menu tampil sesuai peran.
- Alur alternatif: akun belum terdaftar; hanya halaman kosong.
- Alur kegagalan: token atau kode tidak sah; ditolak.
- Pascakondisi: akses sesuai peran.

**Diagram alur**

![Alur FR-ADBD-09](../adbd/diagram/img/fr-fitur-09.png){height=5in}

**Acceptance criteria**

- **Given** akun Google belum terdaftar pada aplikasi, **When** pengguna masuk, **Then** hanya tampil halaman awal kosong.
- **Given** pengguna berperan Donatur, **When** memanggil API kelola akun, **Then** ditolak 403.
- **Given** kode TOTP salah, **When** staf mengirimnya, **Then** akses tidak diberikan.

**Mockup**

![gambar](../adbd/img/adbd-09-ditolak.png)

*Akses ditolak*

| **Elemen** | **Jenis** | **Perilaku** |
|------------|-----------|----------------------|
| Pesan 403 | Teks | Tanpa rincian teknis |
| Kembali | Tombol | Ke beranda |

Pesan galat: “Anda tidak berhak membuka halaman ini.”

Test scenario lengkap: `04-pengujian-dan-penerimaan/Test-Scenario/TS-ADBD-09 - Pembatasan akses dan login staf`.
