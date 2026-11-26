# Penelusuran FR · Akun Donatur dan Bukti Donasi

Kelompok 2 · Business Analyst: Eli Nur Aulia · Project Manager: Destri · Status: draf

## Requirements Traceability Matrix (RTM)

Penelusuran dua arah: kebutuhan, task proses, rancangan, uji.

| **ID**             | **Modul** | **MoSCoW** | **Sumber**       | **Task proses**  | **Elemen rancangan** | **Kasus uji**     | **Status**      |
|--------------------|-----------|------------|------------------|------------------|----------------------|-------------------|-----------------|
| FR Umum 1 sampai 4 | Umum      | Must       | Kesepakatan BA   | Semua            | Tampilan bersama     | AC FR Umum        | Draf            |
| FR-ADBD-01         | M1        | Must       | Usulan tim       | T-01             | M1; UC-01            | AC FR-ADBD-01 (3) | Draf            |
| FR-ADBD-02         | M1        | Must       | v0.2 FR-005      | T-01, T-02       | M1; UC-02            | AC FR-ADBD-02 (2) | Draf            |
| FR-ADBD-03         | M1        | Should     | v0.2 FR-008      | T-01             | M1; UC-03            | AC FR-ADBD-03 (2) | Draf            |
| FR-ADBD-04         | M2        | Must       | v0.2 FR-007      | T-03             | M2; UC-04            | AC FR-ADBD-04 (3) | Draf            |
| FR-ADBD-05         | M2        | Must       | v0.2 FR-007      | T-06             | M2; UC-05            | AC FR-ADBD-05 (2) | Draf            |
| FR-ADBD-06         | M3        | Must       | Usulan tim       | T-04             | M3; UC-06            | AC FR-ADBD-06 (3) | Draf            |
| FR-ADBD-07         | M3        | Must       | Usulan tim       | T-05             | M3; UC-07            | AC FR-ADBD-07 (2) | Draf            |
| FR-ADBD-08         | M3        | Could      | Usulan tim       | T-05             | M3; UC-08            | AC FR-ADBD-08 (2) | Ditahan (CR-02) |
| FR-ADBD-09         | M4        | Must       | v0.2 NFR-001     | T-01 sampai T-06 | M4; UC-10            | AC FR-ADBD-09 (2) | Draf            |
| FR-ADBD-10         | M4        | Must       | v0.2 NFR-001     | T-01 sampai T-06 | M4; UC-10            | AC FR-ADBD-10 (3) | Draf            |
| FR-ADBD-11         | M4        | Should     | v0.2 FR-011      | T-01 sampai T-06 | M4; UC-11            | AC FR-ADBD-11 (1) | Draf            |
| FR-ADBD-12         | M5        | Should     | v0.2 FR-009      | T-01             | M5; UC-12            | AC FR-ADBD-12 (2) | Draf            |
| NFR-U1             | Lintas    | Must       | Usulan tim; v0.2 | T-01 sampai T-06 | Dokumen perancangan  | Test plan         | Usulan          |
| NFR-U2             | Lintas    | Must       | Usulan tim; v0.2 | T-01 sampai T-06 | Dokumen perancangan  | Test plan         | Usulan          |
| NFR-U3             | Lintas    | Should     | Usulan tim; v0.2 | T-01 sampai T-06 | Dokumen perancangan  | Test plan         | Usulan          |
| NFR-P1             | Lintas    | Should     | Usulan tim; v0.2 | T-01 sampai T-06 | Dokumen perancangan  | Test plan         | Usulan          |
| NFR-P2             | Lintas    | Should     | Usulan tim; v0.2 | T-01 sampai T-06 | Dokumen perancangan  | Test plan         | Usulan          |
| NFR-P3             | Lintas    | Should     | Usulan tim; v0.2 | T-01 sampai T-06 | Dokumen perancangan  | Test plan         | Usulan          |
| NFR-P4             | Lintas    | Should     | Usulan tim; v0.2 | T-01 sampai T-06 | Dokumen perancangan  | Test plan         | Usulan          |
| NFR-S1             | Lintas    | Must       | Usulan tim; v0.2 | T-01 sampai T-06 | Dokumen perancangan  | Test plan         | Usulan          |
| NFR-S2             | Lintas    | Must       | Usulan tim; v0.2 | T-01 sampai T-06 | Dokumen perancangan  | Test plan         | Usulan          |
| NFR-S3             | Lintas    | Must       | Usulan tim; v0.2 | T-01 sampai T-06 | Dokumen perancangan  | Test plan         | Usulan          |
| NFR-S4             | Lintas    | Must       | Usulan tim; v0.2 | T-01 sampai T-06 | Dokumen perancangan  | Test plan         | Usulan          |
| NFR-S5             | Lintas    | Should     | Usulan tim; v0.2 | T-01 sampai T-06 | Dokumen perancangan  | Test plan         | Usulan          |
| NFR-S6             | Lintas    | Could      | Usulan tim; v0.2 | T-01 sampai T-06 | Dokumen perancangan  | Test plan         | Usulan          |
| NFR-S7             | Lintas    | Must       | Usulan tim; v0.2 | T-01 sampai T-06 | Dokumen perancangan  | Test plan         | Usulan          |
| NFR-S8             | Lintas    | Must       | Usulan tim; v0.2 | T-01 sampai T-06 | Dokumen perancangan  | Test plan         | Usulan          |
| NFR-S9             | Lintas    | Should     | Usulan tim; v0.2 | T-01 sampai T-06 | Dokumen perancangan  | Test plan         | Usulan          |

### Pemetaan FR ke Fitur (dokumen klien)

Dokumen untuk BMTZ memakai nama “Fitur 01” dan seterusnya. Rincian ada di dokumen FR dan Test Scenario.

| **Fitur (dokumen klien)** | **FR (SRS)** | **Nama**                             | **Dokumen FR** | **Test Scenario** |
|---------------------------|--------------|--------------------------------------|----------------|-------------------|
| Fitur 01                  | FR-ADBD-01   | Pendaftaran akun donatur             | FR-ADBD-01     | TS-ADBD-01        |
| Fitur 02                  | FR-ADBD-02   | Pengelolaan profil donatur           | FR-ADBD-02     | TS-ADBD-02        |
| Fitur 03                  | FR-ADBD-04   | Penautan donasi ke akun              | FR-ADBD-04     | TS-ADBD-04        |
| Fitur 04                  | FR-ADBD-05   | Riwayat donasi                       | FR-ADBD-05     | TS-ADBD-05        |
| Fitur 05                  | FR-ADBD-06   | Penerbitan bukti donasi              | FR-ADBD-06     | TS-ADBD-06        |
| Fitur 06                  | FR-ADBD-07   | Unduh dan kirim bukti                | FR-ADBD-07     | TS-ADBD-07        |
| Fitur 07                  | FR-ADBD-09   | Pembatasan akses menurut peran       | FR-ADBD-09     | TS-ADBD-09        |
| Fitur 08                  | FR-ADBD-10   | Pengelolaan akun dan peran           | FR-ADBD-10     | TS-ADBD-10        |
| Fitur 09                  | FR-ADBD-03   | Preferensi anonimitas dan pengiriman | FR-ADBD-03     | TS-ADBD-03        |
| Fitur 10                  | FR-ADBD-11   | Log akses data pribadi               | FR-ADBD-11     | TS-ADBD-11        |
| Fitur 11                  | FR-ADBD-12   | Penyediaan data untuk proyek hilir   | FR-ADBD-12     | TS-ADBD-12        |
| Fitur 12                  | FR-ADBD-08   | Verifikasi keaslian bukti            | FR-ADBD-08     | TS-ADBD-08        |
