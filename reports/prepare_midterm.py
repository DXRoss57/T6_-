"""Rebuild the midterm evidence from saved Docling Markdown, without downloading models."""
from pathlib import Path
import textwrap
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
FIGURES = ROOT / 'reports/figures'
FIGURES.mkdir(parents=True, exist_ok=True)

def source(prefix, kind='cleaned'):
    return next((ROOT / 'data/interim').glob(f'*/{kind}_{prefix}*.md'))

def comparison(name, prefix, raw_start, raw_end, clean_start, clean_end, title):
    raw, clean = source(prefix, 'raw'), source(prefix)
    font = ImageFont.truetype('C:/Windows/Fonts/msjh.ttc', 19)
    small = ImageFont.truetype('C:/Windows/Fonts/msjh.ttc', 16)
    canvas = Image.new('RGB', (1800, 1050), '#f8fafc')
    draw = ImageDraw.Draw(canvas)
    draw.text((30, 20), title, font=font, fill='#0f172a')
    draw.text((30, 55), 'Rendered source comparison, not a VS Code screenshot. Line numbers refer to the original files.', font=small, fill='#475569')
    for x, p, start, end, color, label in [(25, raw, raw_start, raw_end, '#fee2e2', 'BEFORE'), (915, clean, clean_start, clean_end, '#dcfce7', 'AFTER')]:
        draw.rectangle((x, 100, x+855, 1025), fill=color)
        draw.text((x+15, 115), label, font=font, fill='#0f172a')
        for k, line in enumerate(textwrap.wrap(p.relative_to(ROOT).as_posix(), 70)):
            draw.text((x+15, 150+k*23), line, font=small, fill='#334155')
        y = 220
        for number, line in enumerate(p.read_text(encoding='utf-8').splitlines()[start-1:end], start):
            # Pixel-based wrapping keeps CJK text readable and preserves the original text.
            parts, part = [], ''
            for ch in line:
                if draw.textlength(part+ch, font=font)>755:
                    parts.append(part); part=''
                part += ch
            parts.append(part)
            for i, part in enumerate(parts):
                draw.text((x+10,y), str(number) if i==0 else '', font=small, fill='#64748b')
                draw.text((x+65,y), part, font=font, fill='#111827')
                y+=29
            if y>990:
                raise ValueError(f'Comparison excerpt too long: {name}')
    canvas.save(FIGURES / name)

# Each excerpt comes from real files and avoids the classroom sample passages.
comparison('1a_compare.png','A231060004',49,61,47,55,'Task 1-A: Remove the repeated regulation title near the page boundary')
comparison('1b_compare.png','A232060013',344,348,329,333,'Task 1-B: Join the Chinese and English course substitution form headings')
comparison('1c_compare.png','A232020018',240,241,222,222,'Task 1-C: Join Article 2 with its English translation')

print('Rebuilt three source comparison images.')
