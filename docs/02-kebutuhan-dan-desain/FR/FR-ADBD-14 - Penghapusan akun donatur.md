# FR-ADBD-14 Penghapusan akun donatur · Akun Donatur dan Bukti Donasi

Kelompok 2 · Dosen: Endy Muhardin · Business Analyst: Eli Nur Aulia · Project Manager: Destri Komalasari · Status: draf


| **Atribut** | **Isi** |
|-------------|------------------------------------------------------------|
| Prioritas | Must |
| Sumber | Workbook 3.2, 3.6, 3.7 |
| Aktor | Donatur, Admin |
| Deskripsi | Donatur dapat meminta akunnya dihapus. Sistem memutus hubungan akun dengan catatan donasi dan menghapus identitas login. Catatan donasi di Penerimaan Donasi tetap ada. Masa simpan bukti yang sudah terbit mengikuti ketentuan audit (belum dikonfirmasi) |
| Task proses | Belum ada pada model as-is |

**Alur**

- Prakondisi: donatur sudah masuk.
- Alur utama: (1) meminta hapus; (2) mengonfirmasi ulang dengan OTP atau Google; (3) sistem memutus hubungan dan menutup sesi.
- Alur alternatif: Admin memproses permintaan yang disampaikan langsung [USULAN].
- Alur kegagalan: konfirmasi gagal; akun tidak dihapus.
- Pascakondisi: akun tidak dapat dipakai; catatan donasi tetap.

**Diagram alur**

![Alur FR-ADBD-14](../adbd/diagram/img/fr-fitur-14.png){height=5in}

**Acceptance criteria**

- **Given** donatur mengonfirmasi penghapusan, **When** sistem memproses, **Then** akun tidak dapat dipakai masuk.
- **Given** akun sudah dihapus, **When** data donasi sumber diperiksa, **Then** catatan donasi tetap ada.
- **Given** konfirmasi ulang gagal, **When** permintaan dikirim, **Then** akun tidak berubah.

**Mockup**

![gambar](../adbd/img/adbd-14-hapus.png)

*Hapus akun*

| **Elemen** | **Jenis** | **Perilaku** |
|-------------------|-----------------|-------------------------------|
| Penjelasan dampak | Teks | Apa yang dihapus dan disimpan |
| Konfirmasi ulang | OTP atau Google | Wajib |
| Hapus akun, Batal | Tombol | Mencatat permintaan |

Pesan galat: “Konfirmasi gagal. Akun tidak dihapus.”

Test scenario lengkap: `04-pengujian-dan-penerimaan/Test-Scenario/TS-ADBD-14 - Penghapusan akun donatur`.
