# FR-ADBD-02 Pengelolaan profil donatur · Akun Donatur dan Bukti Donasi

Kelompok 2 · Business Analyst: Eli Nur Aulia · Project Manager: Destri · Status: draf


| **Atribut** | **Isi**                                                             |
|-------------|---------------------------------------------------------------------|
| Prioritas   | Must                                                                |
| Sumber      | v0.2 FR-005                                                         |
| Aktor       | Donatur                                                             |
| Deskripsi   | Donatur melihat dan mengubah data yang disetujui; perubahan dicatat |
| Task proses | T-01, T-02                                                          |

**Alur**

- Prakondisi: donatur sudah login.

- Alur utama: (1) membuka profil; (2) mengubah data; (3) menyimpan.

- Alur alternatif: ganti email memerlukan verifikasi.

- Alur kegagalan: data tidak valid, sistem menolak.

- Pascakondisi: profil tersimpan.

**Acceptance criteria**

- **Given** donatur sudah login, **When** mengubah alamat dan menyimpan, **Then** perubahan tersimpan.

- **Given** email baru belum diverifikasi, **When** donatur menyimpan, **Then** email lama tetap berlaku.

**Mockup**

![gambar](../../adbd/img/adbd-02-profil.png)

*Pengelolaan profil donatur*

| **Elemen**    | **Jenis** | **Perilaku**      |
|---------------|-----------|-------------------|
| Data diri     | Kolom     | Sesuai 3.1.1.2    |
| Simpan, Batal | Tombol    | Perubahan dicatat |

Pesan galat: “Nama wajib diisi.”; “Nomor telepon tidak valid.”

Test scenario: TS-ADBD-02.
