# Penerimaan Donasi dan Akun Donatur · Baitulmal Tazkia

## Bagian Akun Donatur dan Bukti Donasi (ADBD)

Kelompok 2 · Business Analyst: Eli Nur Aulia · Project Manager: Destri

Status: **draf**, belum ada sign-off. Butir [USULAN], [DUGAAN], dan [DRAF] belum disetujui.

## Isi

| Folder | Isi |
|---|---|
| [01-inisiasi-dan-perencanaan/adbd](01-inisiasi-dan-perencanaan/adbd/sumber/brs.md) | BRS dan pertanyaan lanjutan PIC |
| [02-kebutuhan-dan-desain/adbd](02-kebutuhan-dan-desain/adbd/sumber/srs-adbd.md) | SRS, daftar fitur, FR lengkap, use case, mockup, penelusuran, gambar, alat |
| [02-kebutuhan-dan-desain/FR](02-kebutuhan-dan-desain/FR) | FR-ADBD-01 sampai 12 |
| [04-pengujian-dan-penerimaan/Test-Scenario](04-pengujian-dan-penerimaan/Test-Scenario) | TS-ADBD-01 sampai 12 dan TS-UMUM |

## Keterhubungan ID

`KB-xx` (BRS) → `FR-ADBD-xx` (SRS, FR) → `TS-ADBD-xx` (Test Scenario)

## Membangun ulang dokumen

Markdown di folder `sumber/`, `FR/`, dan `Test-Scenario/` adalah sumber; berkas `output/` dan `.docx` dibangun dari situ:

```bash
bash 02-kebutuhan-dan-desain/adbd/tools/build.sh
```

Berkas per FR dibuat dari `fr-lengkap.md`, jadi ubah FR di berkas itu. SRS, use case, mockup, penelusuran, dan daftar fitur disimpan terpisah; bila isi kebutuhan berubah, perbarui semuanya.

Seluruh data contoh adalah data sintetis. Jangan menaruh data donatur asli atau kredensial di repo ini.

## Berkas lain

- [Notulen Manajemen Kampanye Penghimpunan](Notulen_Manajemen_Kampanye_Penghimpunan_Terbaru.docx)
