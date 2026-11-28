# FR-ADBD-11 Log akses data pribadi · Akun Donatur dan Bukti Donasi

Kelompok 2 · Dosen: Endy Muhardin · Business Analyst: Eli Nur Aulia · Project Manager: Destri Komalasari · Status: draf


| **Atribut** | **Isi**                                                                             |
|-------------|-------------------------------------------------------------------------------------|
| Prioritas   | Should                                                                              |
| Sumber      | v0.2 FR-011                                                                         |
| Aktor       | Admin                                                                               |
| Deskripsi   | Sistem mencatat siapa membuka atau mengubah data donatur atau bukti siapa dan kapan |
| Task proses | T-01 sampai T-06                                                                    |

**Alur**

- Prakondisi: berperan Admin.

- Alur utama: (1) membuka log; (2) menyaring; (3) sistem menampilkan siapa membuka data siapa dan kapan.

- Alur alternatif: hasil kosong.

- Alur kegagalan: non-Admin ditolak.

- Pascakondisi: log tidak dapat diubah.

**Diagram alur**

![Alur FR-ADBD-11](../adbd/diagram/img/fr-fitur-11.png){height=5in}

**Acceptance criteria**

- **Given** petugas membuka profil donatur, **When** Admin membuka log, **Then** tercatat pengguna, donatur, dan waktu.

**Mockup**

![gambar](../adbd/img/adbd-11-catatan-akses.png)

*Log akses data pribadi*

| **Elemen**    | **Jenis**        | **Perilaku**                    |
|---------------|------------------|---------------------------------|
| Filter        | Pilihan, rentang | Menyaring                       |
| Tabel catatan | Baca saja        | Tidak dapat diubah atau dihapus |

Pesan galat: “Tidak ada data.”

Test scenario lengkap: `04-pengujian-dan-penerimaan/Test-Scenario/TS-ADBD-11 - Log akses data pribadi`.
