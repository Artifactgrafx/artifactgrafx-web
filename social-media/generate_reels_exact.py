"""
Generate reels matching the exact animation style from quote-*-animated.html
"""
import os
import math
from PIL import Image, ImageDraw, ImageFont
from moviepy import VideoClip
import numpy as np

BASE = os.path.dirname(os.path.abspath(__file__))
REELS_DIR = os.path.join(BASE, 'reels')
os.makedirs(REELS_DIR, exist_ok=True)

W, H = 1080, 1920

BG_DARK = (31, 27, 23)
BG_MID = (42, 37, 31)
ACCENT = (217, 169, 91)
CREAM = (236, 229, 221)
CREAM_DIM = (160, 153, 146)

fonts_dir = os.path.expanduser("~/AppData/Local/Microsoft/Windows/Fonts")

SPACE_GROTESK_BOLD = os.path.join(fonts_dir, "SpaceGrotesk-Bold.ttf")
SPACE_GROTESK_SEMIBOLD = os.path.join(fonts_dir, "SpaceGrotesk-SemiBold.ttf")
SPACE_GROTESK = os.path.join(fonts_dir, "SpaceGrotesk-Regular.ttf")
JETBRAINS_MONO = os.path.join(fonts_dir, "JetBrainsMono-Regular.ttf")

def load_font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        try:
            return ImageFont.truetype(SPACE_GROTESK_SEMIBOLD, size)
        except:
            return ImageFont.load_default()

def add_grid(draw, w, h):
    for x in range(0, w, 28):
        draw.line([(x,0),(x,h)], fill=(236,229,221,8), width=1)
    for y in range(0, h, 28):
        draw.line([(0,y),(w,y)], fill=(236,229,221,8), width=1)

def draw_emblem(draw, cx, cy):
    # Triangle
    size = 48
    draw.polygon([(cx, cy-size*0.69), (cx+size*0.66, cy-size*0.2), (cx-size*0.66, cy-size*0.2)], 
                 outline=ACCENT, width=2)
    draw.polygon([(cx, cy-size*0.69), (cx+size*0.66, cy-size*0.2), (cx, cy+size*0.99)], 
                 outline=ACCENT, width=2)
    draw.polygon([(cx, cy-size*0.69), (cx-size*0.66, cy-size*0.2), (cx, cy+size*0.99)], 
                 outline=ACCENT, width=2)
    # A
    f = load_font(SPACE_GROTESK_SEMIBOLD, 30)
    draw.text((cx, cy+15), "A", font=f, fill=ACCENT, anchor="mm")

def make_frame_quote1(t):
    img = Image.new('RGB', (W,H), BG_DARK)
    draw = ImageDraw.Draw(img, 'RGBA')
    add_grid(draw, W, H)
    
    # Quote mark - fadeInUp 0.8s at 0.2s
    if t >= 0.2:
        progress = min(1.0, (t - 0.2) / 0.8)
        alpha = int(255 * progress)
        y_off = int((1 - progress) * 30)
        f_quote = load_font(SPACE_GROTESK_BOLD, 120)
        draw.text((W//2, 400 + y_off), '"', font=f_quote, fill=(*ACCENT, alpha), anchor="mm")
    
    # Quote text - fadeInUp 0.8s at 0.6s
    if t >= 0.6:
        progress = min(1.0, (t - 0.6) / 0.8)
        alpha = int(255 * progress)
        y_off = int((1 - progress) * 30)
        f_text = load_font(SPACE_GROTESK_SEMIBOLD, 56)
        draw.text((W//2, 650 + y_off), "Your brand is real.", font=f_text, fill=(*CREAM, alpha), anchor="mm")
        draw.text((W//2, 730 + y_off), "It's just buried.", font=f_text, fill=(*CREAM, alpha), anchor="mm")
    
    # Emblem - fadeInUp 0.8s at 1.8s
    if t >= 1.8:
        progress = min(1.0, (t - 1.8) / 0.8)
        alpha = int(255 * progress)
        draw_emblem(draw, W//2, H - 250)
        # Handle
        if t >= 2.0:
            progress2 = min(1.0, (t - 2.0) / 0.8)
            alpha2 = int(255 * progress2)
            f_handle = load_font(JETBRAINS_MONO, 14)
            draw.text((W//2, H - 184), "@artifactgrafx", font=f_handle, fill=(217, 169, 91, alpha2), anchor="mm")
    
    return np.array(img)

def make_frame_quote2(t):
    img = Image.new('RGB', (W,H), BG_DARK)
    draw = ImageDraw.Draw(img, 'RGBA')
    add_grid(draw, W, H)
    
    if t >= 0.2:
        progress = min(1.0, (t - 0.2) / 0.8)
        alpha = int(255 * progress)
        y_off = int((1 - progress) * 30)
        f_quote = load_font(SPACE_GROTESK_BOLD, 120)
        draw.text((W//2, 400 + y_off), '"', font=f_quote, fill=(*ACCENT, alpha), anchor="mm")
    
    if t >= 0.6:
        progress = min(1.0, (t - 0.6) / 0.8)
        alpha = int(255 * progress)
        y_off = int((1 - progress) * 30)
        f_text = load_font(SPACE_GROTESK_SEMIBOLD, 56)
        draw.text((W//2, 650 + y_off), "Excavate it.", font=f_text, fill=(*CREAM, alpha), anchor="mm")
        draw.text((W//2, 730 + y_off), "Polish it.", font=f_text, fill=(*CREAM, alpha), anchor="mm")
        draw.text((W//2, 810 + y_off), "Bring it online.", font=f_text, fill=(*CREAM, alpha), anchor="mm")
    
    if t >= 1.8:
        progress = min(1.0, (t - 1.8) / 0.8)
        alpha = int(255 * progress)
        draw_emblem(draw, W//2, H - 250)
        if t >= 2.0:
            progress2 = min(1.0, (t - 2.0) / 0.8)
            alpha2 = int(255 * progress2)
            f_handle = load_font(JETBRAINS_MONO, 14)
            draw.text((W//2, H - 184), "@artifactgrafx", font=f_handle, fill=(217, 169, 91, alpha2), anchor="mm")
    
    return np.array(img)

def make_frame_quote3(t):
    img = Image.new('RGB', (W,H), BG_DARK)
    draw = ImageDraw.Draw(img, 'RGBA')
    add_grid(draw, W, H)
    
    if t >= 0.2:
        progress = min(1.0, (t - 0.2) / 0.8)
        alpha = int(255 * progress)
        y_off = int((1 - progress) * 30)
        f_quote = load_font(SPACE_GROTESK_BOLD, 120)
        draw.text((W//2, 400 + y_off), '"', font=f_quote, fill=(*ACCENT, alpha), anchor="mm")
    
    if t >= 0.6:
        progress = min(1.0, (t - 0.6) / 0.8)
        alpha = int(255 * progress)
        y_off = int((1 - progress) * 30)
        f_text = load_font(SPACE_GROTESK_SEMIBOLD, 56)
        draw.text((W//2, 650 + y_off), "One conversation.", font=f_text, fill=(*CREAM, alpha), anchor="mm")
        draw.text((W//2, 730 + y_off), "One design.", font=f_text, fill=(*CREAM, alpha), anchor="mm")
        draw.text((W//2, 810 + y_off), "One launch.", font=f_text, fill=(*CREAM, alpha), anchor="mm")
    
    if t >= 1.8:
        progress = min(1.0, (t - 1.8) / 0.8)
        alpha = int(255 * progress)
        draw_emblem(draw, W//2, H - 250)
        if t >= 2.0:
            progress2 = min(1.0, (t - 2.0) / 0.8)
            alpha2 = int(255 * progress2)
            f_handle = load_font(JETBRAINS_MONO, 14)
            draw.text((W//2, H - 184), "@artifactgrafx", font=f_handle, fill=(217, 169, 91, alpha2), anchor="mm")
    
    return np.array(img)

def make_frame_wildfire(t):
    img = Image.new('RGB', (W,H), BG_DARK)
    draw = ImageDraw.Draw(img, 'RGBA')
    add_grid(draw, W, H)
    
    if t >= 0.2:
        progress = min(1.0, (t - 0.2) / 0.8)
        alpha = int(255 * progress)
        y_off = int((1 - progress) * 30)
        f_quote = load_font(SPACE_GROTESK_BOLD, 120)
        draw.text((W//2, 380 + y_off), '"', font=f_quote, fill=(*ACCENT, alpha), anchor="mm")
    
    if t >= 0.6:
        progress = min(1.0, (t - 0.6) / 0.8)
        alpha = int(255 * progress)
        y_off = int((1 - progress) * 30)
        f_text = load_font(SPACE_GROTESK_SEMIBOLD, 52)
        draw.text((W//2, 620 + y_off), "Once my creativity is sparked,", font=f_text, fill=(*CREAM, alpha), anchor="mm")
        draw.text((W//2, 700 + y_off), "I become unstoppable", font=f_text, fill=(*CREAM, alpha), anchor="mm")
        draw.text((W//2, 780 + y_off), "like a wildfire.", font=f_text, fill=(*CREAM, alpha), anchor="mm")
    
    if t >= 1.8:
        progress = min(1.0, (t - 1.8) / 0.8)
        alpha = int(255 * progress)
        draw_emblem(draw, W//2, H - 250)
        if t >= 2.0:
            progress2 = min(1.0, (t - 2.0) / 0.8)
            alpha2 = int(255 * progress2)
            f_handle = load_font(JETBRAINS_MONO, 14)
            draw.text((W//2, H - 184), "@artifactgrafx", font=f_handle, fill=(217, 169, 91, alpha2), anchor="mm")
    
    return np.array(img)

def make_frame_dig(t):
    img = Image.new('RGB', (W,H), BG_DARK)
    draw = ImageDraw.Draw(img, 'RGBA')
    add_grid(draw, W, H)
    
    if t >= 0.2:
        progress = min(1.0, (t - 0.2) / 0.8)
        alpha = int(255 * progress)
        y_off = int((1 - progress) * 30)
        f_quote = load_font(SPACE_GROTESK_BOLD, 120)
        draw.text((W//2, 360 + y_off), '"', font=f_quote, fill=(*ACCENT, alpha), anchor="mm")
    
    if t >= 0.6:
        progress = min(1.0, (t - 0.6) / 0.8)
        alpha = int(255 * progress)
        y_off = int((1 - progress) * 30)
        f_text = load_font(SPACE_GROTESK_SEMIBOLD, 56)
        draw.text((W//2, 610 + y_off), "Ideas don't just appear.", font=f_text, fill=(*CREAM, alpha), anchor="mm")
        draw.text((W//2, 690 + y_off), "They get buried.", font=f_text, fill=(*CREAM, alpha), anchor="mm")
        draw.text((W//2, 770 + y_off), "You have to dig for them.", font=f_text, fill=(*CREAM, alpha), anchor="mm")
    
    if t >= 1.8:
        progress = min(1.0, (t - 1.8) / 0.8)
        alpha = int(255 * progress)
        draw_emblem(draw, W//2, H - 250)
        if t >= 2.0:
            progress2 = min(1.0, (t - 2.0) / 0.8)
            alpha2 = int(255 * progress2)
            f_handle = load_font(JETBRAINS_MONO, 14)
            draw.text((W//2, H - 184), "@artifactgrafx", font=f_handle, fill=(217, 169, 91, alpha2), anchor="mm")
    
    return np.array(img)

def make_frame_streets(t):
    img = Image.new('RGB', (W,H), BG_DARK)
    draw = ImageDraw.Draw(img, 'RGBA')
    add_grid(draw, W, H)
    
    if t >= 0.2:
        progress = min(1.0, (t - 0.2) / 0.8)
        alpha = int(255 * progress)
        y_off = int((1 - progress) * 30)
        f_quote = load_font(SPACE_GROTESK_BOLD, 120)
        draw.text((W//2, 340 + y_off), '"', font=f_quote, fill=(*ACCENT, alpha), anchor="mm")
    
    if t >= 0.6:
        progress = min(1.0, (t - 0.6) / 0.8)
        alpha = int(255 * progress)
        y_off = int((1 - progress) * 30)
        f_text = load_font(SPACE_GROTESK_SEMIBOLD, 50)
        draw.text((W//2, 590 + y_off), "The best ideas come from", font=f_text, fill=(*CREAM, alpha), anchor="mm")
        draw.text((W//2, 660 + y_off), "everywhere.", font=f_text, fill=(*CREAM, alpha), anchor="mm")
        draw.text((W//2, 740 + y_off), "From jazz records to graffiti walls.", font=f_text, fill=(*CREAM, alpha), anchor="mm")
        draw.text((W//2, 810 + y_off), "From neon signs to hand-painted", font=f_text, fill=(*CREAM, alpha), anchor="mm")
        draw.text((W//2, 880 + y_off), "lettering.", font=f_text, fill=(*CREAM, alpha), anchor="mm")
    
    if t >= 1.8:
        progress = min(1.0, (t - 1.8) / 0.8)
        alpha = int(255 * progress)
        draw_emblem(draw, W//2, H - 250)
        if t >= 2.0:
            progress2 = min(1.0, (t - 2.0) / 0.8)
            alpha2 = int(255 * progress2)
            f_handle = load_font(JETBRAINS_MONO, 14)
            draw.text((W//2, H - 184), "@artifactgrafx", font=f_handle, fill=(217, 169, 91, alpha2), anchor="mm")
    
    return np.array(img)

def render_reel(func, name, duration=6.0):
    print(f'Rendering {name}...')
    clip = VideoClip(func, duration=duration)
    clip = clip.with_fps(30)
    out_path = os.path.join(REELS_DIR, f'{name}-reel.mp4')
    clip.write_videofile(out_path, codec='libx264', audio=False, preset='medium', bitrate='4000k')
    print(f'  -> {name}-reel.mp4')
    
    img = func(0.3)
    thumb = Image.fromarray(img)
    thumb_path = os.path.join(REELS_DIR, f'{name}-reel-thumbnail.png')
    thumb.save(thumb_path)
    print(f'  -> {name}-reel-thumbnail.png')

if __name__ == '__main__':
    render_reel(make_frame_quote1, '01-your-brand-is-real')
    render_reel(make_frame_quote2, '02-excavate-polish-bring')
    render_reel(make_frame_quote3, '03-one-conversation')
    render_reel(make_frame_wildfire, '04-wildfire')
    render_reel(make_frame_dig, '05-dig-ideas')
    render_reel(make_frame_streets, '06-streets-to-studio')
    print('Done!')
