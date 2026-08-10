from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

root = Path(__file__).resolve().parents[1] / "qa" / "page-render-contact-sheets" / "run-final4"
font = ImageFont.truetype("arial.ttf", 20)
for folder in sorted(p for p in root.iterdir() if p.is_dir()):
    pages = sorted(folder.glob("page-*.png"), key=lambda p: int(p.stem.split("-")[-1]))
    for start in range(0, len(pages), 8):
        batch = pages[start:start+8]
        thumbs = []
        for page in batch:
            img = Image.open(page).convert("RGB")
            img.thumbnail((520, 735))
            canvas = Image.new("RGB", (540, 780), "#E2E8F0")
            canvas.paste(img, ((540-img.width)//2, 30))
            ImageDraw.Draw(canvas).text((12, 750), f"Page {int(page.stem.split('-')[-1])}", font=font, fill="#1F2937")
            thumbs.append(canvas)
        sheet = Image.new("RGB", (1080, 3120), "#CBD5E1")
        for i, thumb in enumerate(thumbs):
            sheet.paste(thumb, ((i%2)*540, (i//2)*780))
        sheet.save(root / f"{folder.name}-contact-{start//8+1:02d}.png", optimize=True)
        print(folder.name, start//8+1)
