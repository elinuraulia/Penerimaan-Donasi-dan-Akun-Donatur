#!/usr/bin/env bash
# Bangun ulang dokumen Word/PDF dari sumber Markdown.
# Perlu: pandoc, python3 + python-docx, LibreOffice.
# Gambar: jalankan draw.py (Graphviz + Playwright) dan gen_mockup.py bila gambar diubah.
set -euo pipefail
ADBD="$(cd "$(dirname "$0")/.." && pwd)"
ROOT="$(cd "$ADBD/../.." && pwd)"

docx() { # sumber.md hasil.docx
  mkdir -p "$(dirname "$2")"
  pandoc "$1" -f gfm -o "$2" --resource-path="$(dirname "$1")" --reference-doc="$ADBD/template/reference.docx"
  python3 "$ADBD/tools/post.py" "$2"
}

python3 "$ADBD/tools/gen_fr.py"

P="$ROOT/01-inisiasi-dan-perencanaan/adbd"
docx "$P/sumber/brs.md" "$P/output/BRS_ADBD_v0.1.docx"
docx "$P/sumber/pertanyaan-lanjutan-pic.md" "$P/output/Pertanyaan_Lanjutan_PIC_ADBD.docx"

S="$ADBD/sumber"; O="$ADBD/output"
docx "$S/srs-adbd.md" "$O/SRS_Akun_Donatur_dan_Bukti_Donasi_v0.3.docx"
python3 "$ADBD/tools/topdf.py" "$O/SRS_Akun_Donatur_dan_Bukti_Donasi_v0.3.docx"
for n in daftar-fitur fr-lengkap penelusuran-fr uc-lengkap ui-mockup; do
  docx "$S/$n.md" "$O/${n}_ADBD.docx"
done

for md in "$ROOT"/02-kebutuhan-dan-desain/FR/*/*.md "$ROOT"/04-pengujian-dan-penerimaan/Test-Scenario/*/*.md; do
  docx "$md" "${md%.md}.docx"
done
