# FR-ADBD-02 Pengelolaan profil donatur · Akun Donatur dan Bukti Donasi

Kelompok 2 · Dosen: Endy Muhardin · Business Analyst: Eli Nur Aulia · Project Manager: Destri Komalasari · Status: draf


| **Atribut** | **Isi**                                                             |
|-------------|---------------------------------------------------------------------|
| Prioritas   | Must                                                                |
| Sumber      | v0.2 FR-005                                                         |
| Aktor       | Donatur                                                             |
| Deskripsi | Donatur melihat dan mengubah data yang disetujui, serta menambah nomor telepon atau email yang diverifikasi dengan OTP; perubahan dicatat |
| Task proses | T-01, T-02                                                          |

**Alur**

- Prakondisi: donatur sudah login.

- Alur utama: (1) membuka profil; (2) mengubah data; (3) menyimpan.

- Alur alternatif: ganti email memerlukan verifikasi.

- Alur kegagalan: data tidak valid, sistem menolak.

- Pascakondisi: profil tersimpan.

**Diagram alur**

![Alur FR-ADBD-02](../adbd/diagram/img/fr-fitur-02.png){height=5in}

**Acceptance criteria**

- **Given** donatur sudah login, **When** mengubah alamat dan menyimpan, **Then** perubahan tersimpan.

- **Given** email atau nomor baru belum diverifikasi, **When** donatur menyimpan, **Then** data lama tetap berlaku.

**Mockup**

![gambar](../adbd/img/adbd-02-profil.png)

*Pengelolaan profil donatur*

| **Elemen**    | **Jenis** | **Perilaku**      |
|---------------|-----------|-------------------|
| Data diri     | Kolom     | Sesuai 3.1.1.2    |
| Simpan, Batal | Tombol    | Perubahan dicatat |

Pesan galat: “Nama wajib diisi.”; “Nomor telepon tidak valid.”

Test scenario lengkap: `04-pengujian-dan-penerimaan/Test-Scenario/TS-ADBD-02 - Pengelolaan profil donatur`.
