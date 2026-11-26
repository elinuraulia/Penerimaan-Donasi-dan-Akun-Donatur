"""Rapikan docx hasil pandoc: ukuran A4, garis tabel, huruf tabel."""
import sys
from docx import Document
from docx.shared import Cm, Pt
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

d = Document(sys.argv[1])
for s in d.sections:
    s.page_width, s.page_height = Cm(21), Cm(29.7)
    s.left_margin = s.right_margin = s.top_margin = s.bottom_margin = Cm(2.2)
for t in d.tables:
    b = OxmlElement('w:tblBorders')
    for n in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
        e = OxmlElement('w:' + n)
        e.set(qn('w:val'), 'single'); e.set(qn('w:sz'), '4'); e.set(qn('w:color'), '808080')
        b.append(e)
    pr = t._tbl.tblPr
    after = [c for c in pr if c.tag.split('}')[1] in ('shd', 'tblLayout', 'tblCellMar', 'tblLook', 'tblCaption', 'tblDescription')]
    after[0].addprevious(b) if after else pr.append(b)
    for row in t.rows:
        for c in row.cells:
            for p in c.paragraphs:
                for r in p.runs:
                    r.font.size = Pt(9)
d.save(sys.argv[1])
