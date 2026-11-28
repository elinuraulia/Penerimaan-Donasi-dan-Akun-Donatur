# FR-ADBD-13 Rekapitulasi donasi tahunan · Akun Donatur dan Bukti Donasi

Kelompok 2 · Dosen: Endy Muhardin · Business Analyst: Eli Nur Aulia · Project Manager: Destri Komalasari · Status: draf


| **Atribut** | **Isi** |
|-------------|------------------------------------------------------------|
| Prioritas | Must |
| Sumber | Workbook 3.2 |
| Aktor | Donatur, petugas donasi |
| Deskripsi | Sistem menerbitkan rekapitulasi per tahun sebagai bukti setor zakat, memuat daftar donasi zakat Berhasil dan totalnya. Rekap yang sudah terbit disimpan apa adanya dengan nomor urut. Format yang diterima kantor pajak belum dikonfirmasi |
| Task proses | T-04 |

**Alur**

- Prakondisi: donatur punya donasi zakat pada tahun itu.
- Alur utama: (1) memilih tahun; (2) sistem menyusun rekap; (3) memberi nomor; (4) menyimpan dan menampilkan.
- Alur alternatif: petugas menerbitkan atas permintaan donatur.
- Alur kegagalan: tidak ada donasi zakat; tidak diterbitkan.
- Pascakondisi: rekap tersimpan.

**Diagram alur**

![Alur FR-ADBD-13](../adbd/diagram/img/fr-fitur-13.png){height=5in}

**Acceptance criteria**

- **Given** donasi zakat Rp250.000 dan Rp750.000 pada 2026 serta infak Rp100.000, **When** rekap zakat 2026 diterbitkan, **Then** total Rp1.000.000.
- **Given** tidak ada donasi zakat, **When** rekap diminta, **Then** sistem menolak.
- **Given** rekap sudah terbit, **When** dibuka lagi, **Then** isinya sama dengan saat terbit.

**Mockup**

![gambar](../adbd/img/adbd-13-rekap.png)

*Rekapitulasi tahunan*

| **Elemen** | **Jenis** | **Perilaku** |
|----------------------|-----------|----------------------------------|
| Tahun | Pilihan | Tahun yang memiliki donasi zakat |
| Terbitkan, Unduh PDF | Tombol | Menyimpan salinan isi |

Pesan galat: “Belum ada donasi zakat pada tahun ini.”

Test scenario lengkap: `04-pengujian-dan-penerimaan/Test-Scenario/TS-ADBD-13 - Rekapitulasi donasi tahunan`.
