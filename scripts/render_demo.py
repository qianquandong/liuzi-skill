#!/usr/bin/env python3
"""Render the README terminal demo GIF. Requires Pillow; not used by runtime."""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "liuzi-demo.gif"
WIDTH, HEIGHT = 1000, 560
BG = "#0b1020"
PANEL = "#111827"
TEXT = "#e5e7eb"
MUTED = "#94a3b8"
BLUE = "#60a5fa"
GREEN = "#34d399"
AMBER = "#fbbf24"

regular = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 25)
small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 21)
bold = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf", 25)

stages = [
    [
        ("> /liuzi-skill", BLUE, bold),
        ("  US sophomore, no SSN. Rank cards I can apply for.", TEXT, regular),
        ("", TEXT, regular),
        ("Routing: money-credit", MUTED, small),
    ],
    [
        ("Evidence Gate", BLUE, bold),
        ("1. Eligibility     official issuer terms", TEXT, regular),
        ("2. Approval odds   no guarantees", TEXT, regular),
        ("3. Worth applying  fees + hard pull + long-term value", TEXT, regular),
        ("", TEXT, regular),
        ("Unverified candidates cannot enter the ranking.", AMBER, small),
    ],
    [
        ("Hard filters", BLUE, bold),
        ("[x] identity-document path verified", GREEN, regular),
        ("[x] age / address / income conditions checked", GREEN, regular),
        ("[x] annual fee and foreign transaction fee checked", GREEN, regular),
        ("[ ] forum-only no-SSN claim", AMBER, regular),
    ],
    [
        ("Result", BLUE, bold),
        ("#1 Officially eligible path", GREEN, regular),
        ("#2 Secured fallback", TEXT, regular),
        ("", TEXT, regular),
        ("Not ranked: issuer page does not confirm eligibility", AMBER, small),
        ("Checked: 2026-09-13", MUTED, small),
    ],
    [
        ("Next action", BLUE, bold),
        ("1. Open official pre-qualification", TEXT, regular),
        ("2. Confirm whether it is a hard pull", TEXT, regular),
        ("3. Review terms before Submit", TEXT, regular),
        ("", TEXT, regular),
        ("Human gate: stop before the irreversible click.", GREEN, small),
    ],
]

frames = []
for stage in stages:
    image = Image.new("RGB", (WIDTH, HEIGHT), BG)
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle((35, 35, WIDTH - 35, HEIGHT - 35), radius=22, fill=PANEL, outline="#334155", width=2)
    draw.ellipse((65, 65, 83, 83), fill="#ef4444")
    draw.ellipse((93, 65, 111, 83), fill="#f59e0b")
    draw.ellipse((121, 65, 139, 83), fill="#22c55e")
    draw.text((165, 59), "LIUZI SKILL / evidence-first decisions", font=small, fill=MUTED)
    y = 125
    for line, color, font in stage:
        draw.text((75, y), line, font=font, fill=color)
        y += 56 if font is not small else 48
    draw.text((75, HEIGHT - 80), "github.com/qianquandong/liuzi-skill", font=small, fill=MUTED)
    frames.append(image)

frames[0].save(
    OUT,
    save_all=True,
    append_images=frames[1:],
    duration=[1400, 1700, 1700, 1700, 1800],
    loop=0,
    optimize=True,
)
print(OUT)

