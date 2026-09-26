"""Regenerate the PDF and plain-text editions from the current plan and references.
Requires reportlab. Run from any directory with Python 3.
"""
from pathlib import Path
import re
from xml.sax.saxutils import escape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import letter
ROOT=Path(__file__).resolve().parents[1]
font=Path('/usr/share/fonts/truetype/dejavu')
if font.exists():
    pdfmetrics.registerFont(TTFont('Body',str(font/'DejaVuSans.ttf')))
    pdfmetrics.registerFont(TTFont('Bold',str(font/'DejaVuSans-Bold.ttf')))
    pdfmetrics.registerFontFamily('Body',normal='Body',bold='Bold',italic='Body',boldItalic='Bold')
else:
    raise RuntimeError('Install DejaVu Sans fonts before generating the PDF.')
styles=getSampleStyleSheet()
for name,size,leading,after in [('B',9.5,13.5,5),('S',8.5,12,4),('H1',18,23,14),('H2',13,18,9),('H3',10.5,15,6)]:
    styles.add(ParagraphStyle(name=name,fontName='Bold' if name.startswith('H') else 'Body',fontSize=size,leading=leading,spaceAfter=after,spaceBefore=9 if name.startswith('H') else 0,keepWithNext=name.startswith('H')))

def inline(t):
    t=escape(t)
    t=re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)',lambda m:'<link color="#145986" href="'+m[2]+'">'+m[1]+'</link>',t)
    t=re.sub(r'\[([^\]]+)\]\((?!https?://)[^)]+\)',r'\1',t)
    t=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',t)
    return t

story=[]
def render(md):
    lines=md.splitlines();i=0
    while i<len(lines):
        line=lines[i].strip()
        if not line:i+=1;continue
        if line.startswith('|'):
            rows=[]
            while i<len(lines) and lines[i].strip().startswith('|'):
                cells=[x.strip() for x in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r'[: -]+',x) for x in cells):rows.append(cells)
                i+=1
            n=len(rows[0]); widths=[150,358] if n==2 else [508/n]*n
            t=Table([[Paragraph(inline(x),styles['S']) for x in row] for row in rows],colWidths=widths,repeatRows=1)
            t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e6edf2')),('GRID',(0,0),(-1,-1),.4,colors.HexColor('#ccd3d8')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)]))
            story.extend([t,Spacer(1,8)]);continue
        if line.startswith('#'):
            level=len(line)-len(line.lstrip('#'));story.append(Paragraph(inline(line.lstrip('#').strip()),styles['H'+str(min(level,3))]));i+=1;continue
        if re.match(r'^\d+\. ',line):
            story.append(Paragraph(inline(line),styles['B']));i+=1;continue
        if line.startswith('- '):
            story.append(Paragraph('&#8226; '+inline(line[2:]),styles['B']));i+=1;continue
        paragraph=[line];i+=1
        while i<len(lines) and lines[i].strip() and not lines[i].startswith(('#','|','- ')) and not re.match(r'^\d+\. ',lines[i]):
            paragraph.append(lines[i].strip());i+=1
        story.append(Paragraph(inline(' '.join(paragraph)),styles['B']))

plan=(ROOT/'docs/PROJECT_PLAN.md').read_text()
refs=(ROOT/'REFERENCES.md').read_text()
render(plan);story.append(PageBreak())
parts=re.split(r'(?=^## )',refs,flags=re.M)
render(parts[0])
for section in parts[1:]:
    begin=len(story)
    render(section.replace('## ','### ',1))
    group=story[begin:]
    del story[begin:]
    story.append(KeepTogether(group))
def footer(c,d):
    c.saveState();c.setFont('Body',8);c.setFillColor(colors.HexColor('#555555'))
    c.drawString(52,28,'Designing a Fair Economy | Living plan v0.2 | September 26, 2026')
    c.drawRightString(560,28,str(d.page));c.restoreState()
SimpleDocTemplate(str(ROOT/'docs/Economic_Transition_Project_Plan.pdf'),pagesize=letter,leftMargin=52,rightMargin=52,topMargin=45,bottomMargin=48,title='Designing a Fair Economy Project Plan',author='Steve Smith').build(story,onFirstPage=footer,onLaterPages=footer)
text=plan+'\n\n'+refs
text=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',r'\1 (\2)',text)
text=re.sub(r'^#{1,6} ', '',text,flags=re.M).replace('**','')
(ROOT/'docs/PROJECT_PLAN.txt').write_text('Current text edition generated from PROJECT_PLAN.md and REFERENCES.md.\n\n'+text)
print('Regenerated PDF and text editions.')
