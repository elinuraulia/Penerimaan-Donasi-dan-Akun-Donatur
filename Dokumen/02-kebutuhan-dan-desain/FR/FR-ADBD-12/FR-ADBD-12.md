# FR-ADBD-12 Penyediaan data untuk proyek hilir · Akun Donatur dan Bukti Donasi

Kelompok 2 · Business Analyst: Eli Nur Aulia · Project Manager: Destri · Status: draf


| **Atribut** | **Isi**                                                                                                        |
|-------------|----------------------------------------------------------------------------------------------------------------|
| Prioritas   | Should                                                                                                         |
| Sumber      | v0.2 FR-009                                                                                                    |
| Aktor       | Proyek 11, Proyek 10                                                                                           |
| Deskripsi   | Sistem menyediakan lewat API: data donatur dan preferensi (IF-02) serta jumlah donatur tanpa identitas (IF-03) |
| Task proses | T-01                                                                                                           |

**Alur**

- Prakondisi: kredensial sah.

- Alur utama: (1) proyek hilir memanggil API; (2) sistem mengembalikan data sesuai kontrak.

- Alur alternatif: tidak ada data, daftar kosong.

- Alur kegagalan: kredensial tidak sah, 401 atau 403.

- Pascakondisi: data diterima.

**Acceptance criteria**

- **Given** konsumen terotorisasi, **When** meminta data donatur, **Then** hanya atribut sesuai kontrak diterima.

- **Given** Proyek 10, **When** meminta rekap, **Then** tidak memuat nama atau kontak.

**Mockup.** Tidak berlaku: layanan data (API) tanpa layar.

Test scenario: TS-ADBD-12.
