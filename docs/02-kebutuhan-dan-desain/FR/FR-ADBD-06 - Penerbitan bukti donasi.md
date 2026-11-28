# FR-ADBD-06 Penerbitan bukti donasi · Akun Donatur dan Bukti Donasi

Kelompok 2 · Dosen: Endy Muhardin · Business Analyst: Eli Nur Aulia · Project Manager: Destri Komalasari · Status: draf


| **Atribut** | **Isi** |
|-------------|------------------------------------------------------------|
| Prioritas | Must |
| Sumber | Workbook 3.2, 3.7 |
| Aktor | Sistem, petugas donasi |
| Deskripsi | Sistem menerbitkan satu bukti resmi per transaksi Berhasil dari semua kanal, termasuk donasi di booth. Bukti diberi nomor urut dan disimpan apa adanya; isinya tidak pernah dibuat ulang dari data terkini. Bila donasi dibatalkan, dikembalikan, atau dikoreksi lewat catatan pembalik dari Penerimaan Donasi, bukti lama menjadi Dibatalkan dan tetap disimpan; bila ada catatan pengganti berstatus Berhasil, terbit bukti baru dengan nomor baru [USULAN] |
| Task proses | T-04 |

**Alur**

- Prakondisi: donasi berstatus Berhasil.
- Alur utama: (1) sistem atau petugas memicu penerbitan; (2) sistem memberi nomor urut; (3) menyimpan salinan isi.
- Alur alternatif: donasi tanpa identitas, bukti atas nama “Hamba Allah” [USULAN].
- Alur kegagalan: status bukan Berhasil; ditolak.
- Pascakondisi: satu bukti tersimpan.

**Diagram alur**

![Alur FR-ADBD-06](../adbd/diagram/img/fr-fitur-06.png){height=5in}

**Acceptance criteria**

- **Given** donasi Berhasil Rp100.000 dari booth, **When** bukti diterbitkan, **Then** bukti memuat nomor urut dan Rp100.000.
- **Given** bukti sudah terbit lalu nama donatur diubah, **When** bukti dibuka, **Then** isinya tetap seperti saat terbit.
- **Given** donasi berstatus Menunggu, **When** penerbitan diminta, **Then** sistem menolak.
- **Given** bukti Rp100.000 sudah terbit, **When** diterima catatan pembalik beserta catatan pengganti Rp150.000, **Then** bukti lama berstatus Dibatalkan dan terbit bukti baru Rp150.000 dengan nomor baru [USULAN].

**Mockup**

![gambar](../adbd/img/adbd-06-bukti.png)

*Bukti donasi*

| **Elemen** | **Jenis** | **Perilaku** |
|--------------|-----------|---------------------|
| Isi bukti | Baca saja | Salinan saat terbit |
| Unduh, Kirim | Tombol | Lihat FR-ADBD-07 |

Pesan galat: “Bukti hanya untuk donasi berstatus Berhasil.”

Test scenario lengkap: `04-pengujian-dan-penerimaan/Test-Scenario/TS-ADBD-06 - Penerbitan bukti donasi`.
