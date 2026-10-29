"""
Generate proper animated Instagram Reels for Artifact Grafx quotes
Like slydz animate_reels.py style
"""
import os
import math
from PIL import Image, ImageDraw, ImageFont
from moviepy import VideoClip
import numpy as np

BASE = os.path.dirname(os.path.abspath(__file__))
QUOTE_DIR = os.path.join(BASE, 'instagram-posts', 'quote-cards')
REELS_DIR = os.path.join(BASE, 'reels')
os.makedirs(REELS_DIR, exist_ok=True)

W, H = 1080, 1920

# Colors from the design
BG_DARK = (31, 27, 23)
BG_MID = (42, 37, 31)
ACCENT = (217, 169, 91)
CREAM = (236, 229, 221)
CREAM_DIM = (236, 229, 221, 180)

fonts_dir = os.path.expanduser("~/AppData/Local/Microsoft/Windows/Fonts")

SPACE_GROTESK_BOLD = os.path.join(fonts_dir, "SpaceGrotesk-Bold.ttf")
SPACE_GROTESK_SEMIBOLD = os.path.join(fonts_dir, "SpaceGrotesk-SemiBold.ttf")
JETBRAINS_MONO = os.path.join(fonts_dir, "JetBrainsMono-Regular.ttf")
INSTRUMENT_SANS = os.path.join(fonts_dir, "InstrumentSans-Regular.ttf")

def load_font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except:
        return ImageFont.load_default()

def make_bg(w, h):
    # Create gradient background like in HTML
    img = Image.new('RGB', (w, h), BG_DARK)
    draw = ImageDraw.Draw(img)
    # Radial gradient approximation
    for y in range(h):
        for x in range(w):
            # Simple gradient
            dist = ((x - w/2)**2 + (y - h/2)**2)**0.5
            max_dist = ((w/2)**2 + (h/2)**2)**0.5
            t = min(1.0, dist / max_dist)
            r = int(BG_MID[0] + (BG_DARK[0] - BG_MID[0]) * t)
            g = int(BG_MID[1] + (BG_DARK[1] - BG_MID[1]) * t)
            b = int(BG_MID[2] + (BG_DARK[2] - BG_MID[2]) * t)
            if y % 10 == 0 and x % 10 == 0:  # sparse for performance
                draw.point((x,y), fill=(r,g,b))
    return img

def add_grid(draw, w, h):
    for x in range(0, w, 28):
        draw.line([(x,0),(x,h)], fill=(236,229,221,8), width=1)
    for y in range(0, h, 28):
        draw.line([(0,y),(w,y)], fill=(236,229,221,8), width=1)

def draw_emblem(draw, x, y, scale=1.0):
    size = int(48 * scale)
    # Draw triangle emblem
    cx, cy = x, y
    # Triangle points
    draw.polygon([(cx, cy-size*0.5), (cx+size*0.4, cy+size*0.3), (cx-size*0.4, cy+size*0.3)], 
                 outline=ACCENT, width=2)
    # Letter A
    f = load_font(SPACE_GROTESK_SEMIBOLD, int(30*scale))
    draw.text((cx, cy+size*0.1), "A", font=f, fill=ACCENT, anchor="mm")

def make_frame_brand_real(t):
    img = Image.new('RGB', (W,H), BG_DARK)
    draw = ImageDraw.Draw(img, 'RGBA')
    add_grid(draw, W, H)
    
    # Quote mark
    if t >= 0.2:
        progress = min(1.0, (t - 0.2) / 0.6)
        alpha = int(255 * progress)
        y_off = int((1 - progress) * 30)
        f_quote = load_font(SPACE_GROTESK_BOLD, 140)
        draw.text((W//2, 400 + y_off), '"', font=f_quote, fill=(*ACCENT, alpha), anchor="mm")
    
    # Quote text
    if t >= 0.6:
        progress = min(1.0, (t - 0.6) / 0.8)
        alpha = int(255 * progress)
        y_off = int((1 - progress) * 30)
        f_text = load_font(SPACE_GROTESK_SEMIBOLD, 68)
        draw.text((W//2, 650 + y_off), "Your brand is real.", font=f_text, fill=(*CREAM, alpha), anchor="mm")
        draw.text((W//2, 750 + y_off), "It's just buried.", font=f_text, fill=(*CREAM, alpha), anchor="mm")
    
    # Emblem and handle
    if t >= 1.8:
        progress = min(1.0, (t - 1.8) / 0.6)
        alpha = int(255 * progress)
        draw_emblem(draw, W//2, H - 180, 1.0)
        f_handle = load_font(JETBRAINS_MONO, 16)
        draw.text((W//2, H - 110), "@artifactgrafx", font=f_handle, fill=(217, 169, 91, alpha), anchor="mm")
    
    return np.array(img)

def make_frame_excavate(t):
    img = Image.new('RGB', (W,H), BG_DARK)
    draw = ImageDraw.Draw(img, 'RGBA')
    add_grid(draw, W, H)
    
    if t >= 0.2:
        progress = min(1.0, (t - 0.2) / 0.6)
        alpha = int(255 * progress)
        y_off = int((1 - progress) * 30)
        f_quote = load_font(SPACE_GROTESK_BOLD, 140)
        draw.text((W//2, 400 + y_off), '"', font=f_quote, fill=(*ACCENT, alpha), anchor="mm")
    
    if t >= 0.6:
        progress = min(1.0, (t - 0.6) / 0.8)
        alpha = int(255 * progress)
        y_off = int((1 - progress) * 30)
        f_text = load_font(SPACE_GROTESK_SEMIBOLD, 68)
        draw.text((W//2, 650 + y_off), "Excavate it.", font=f_text, fill=(*CREAM, alpha), anchor="mm")
        draw.text((W//2, 750 + y_off), "Polish it.", font=f_text, fill=(*CREAM, alpha), anchor="mm")
        draw.text((W//2, 850 + y_off), "Bring it online.", font=f_text, fill=(*CREAM, alpha), anchor="mm")
    
    if t >= 2.0:
        progress = min(1.0, (t - 2.0) / 0.6)
        alpha = int(255 * progress)
        draw_emblem(draw, W//2, H - 180, 1.0)
        f_handle = load_font(JETBRAINS_MONO, 16)
        draw.text((W//2, H - 110), "@artifactgrafx", font=f_handle, fill=(217, 169, 91, alpha), anchor="mm")
    
    return np.array(img)

def make_frame_conversation(t):
    img = Image.new('RGB', (W,H), BG_DARK)
    draw = ImageDraw.Draw(img, 'RGBA')
    add_grid(draw, W, H)
    
    if t >= 0.2:
        progress = min(1.0, (t - 0.2) / 0.6)
        alpha = int(255 * progress)
        y_off = int((1 - progress) * 30)
        f_quote = load_font(SPACE_GROTESK_BOLD, 140)
        draw.text((W//2, 400 + y_off), '"', font=f_quote, fill=(*ACCENT, alpha), anchor="mm")
    
    if t >= 0.6:
        progress = min(1.0, (t - 0.6) / 0.8)
        alpha = int(255 * progress)
        y_off = int((1 - progress) * 30)
        f_text = load_font(SPACE_GROTESK_SEMIBOLD, 68)
        draw.text((W//2, 650 + y_off), "One conversation.", font=f_text, fill=(*CREAM, alpha), anchor="mm")
        draw.text((W//2, 750 + y_off), "One design.", font=f_text, fill=(*CREAM, alpha), anchor="mm")
        draw.text((W//2, 850 + y_off), "One launch.", font=f_text, fill=(*CREAM, alpha), anchor="mm")
    
    if t >= 2.0:
        progress = min(1.0, (t - 2.0) / 0.6)
        alpha = int(255 * progress)
        draw_emblem(draw, W//2, H - 180, 1.0)
        f_handle = load_font(JETBRAINS_MONO, 16)
        draw.text((W//2, H - 110), "@artifactgrafx", font=f_handle, fill=(217, 169, 91, alpha), anchor="mm")
    
    return np.array(img)

def make_frame_wildfire(t):
    img = Image.new('RGB', (W,H), BG_DARK)
    draw = ImageDraw.Draw(img, 'RGBA')
    add_grid(draw, W, H)
    
    if t >= 0.2:
        progress = min(1.0, (t - 0.2) / 0.6)
        alpha = int(255 * progress)
        y_off = int((1 - progress) * 30)
        f_quote = load_font(SPACE_GROTESK_BOLD, 140)
        draw.text((W//2, 380 + y_off), '"', font=f_quote, fill=(*ACCENT, alpha), anchor="mm")
    
    if t >= 0.6:
        progress = min(1.0, (t - 0.6) / 0.8)
        alpha = int(255 * progress)
        y_off = int((1 - progress) * 30)
        f_text = load_font(SPACE_GROTESK_SEMIBOLD, 62)
        draw.text((W//2, 620 + y_off), "Once my creativity is sparked,", font=f_text, fill=(*CREAM, alpha), anchor="mm")
        draw.text((W//2, 720 + y_off), "I become unstoppable", font=f_text, fill=(*CREAM, alpha), anchor="mm")
        draw.text((W//2, 820 + y_off), "like a wildfire.", font=f_text, fill=(*CREAM, alpha), anchor="mm")
    
    if t >= 2.0:
        progress = min(1.0, (t - 2.0) / 0.6)
        alpha = int(255 * progress)
        draw_emblem(draw, W//2, H - 180, 1.0)
        f_handle = load_font(JETBRAINS_MONO, 16)
        draw.text((W//2, H - 110), "@artifactgrafx", font=f_handle, fill=(217, 169, 91, alpha), anchor="mm")
    
    return np.array(img)

def make_frame_dig(t):
    img = Image.new('RGB', (W,H), BG_DARK)
    draw = ImageDraw.Draw(img, 'RGBA')
    add_grid(draw, W, H)
    
    if t >= 0.2:
        progress = min(1.0, (t - 0.2) / 0.6)
        alpha = int(255 * progress)
        y_off = int((1 - progress) * 30)
        f_quote = load_font(SPACE_GROTESK_BOLD, 140)
        draw.text((W//2, 350 + y_off), '"', font=f_quote, fill=(*ACCENT, alpha), anchor="mm")
    
    if t >= 0.6:
        progress = min(1.0, (t - 0.6) / 0.8)
        alpha = int(255 * progress)
        y_off = int((1 - progress) * 30)
        f_text = load_font(SPACE_GROTESK_SEMIBOLD, 64)
        draw.text((W//2, 600 + y_off), "Ideas don't just appear.", font=f_text, fill=(*CREAM, alpha), anchor="mm")
        draw.text((W//2, 700 + y_off), "They get buried.", font=f_text, fill=(*CREAM, alpha), anchor="mm")
        draw.text((W//2, 800 + y_off), "You have to dig for them.", font=f_text, fill=(*CREAM, alpha), anchor="mm")
    
    if t >= 2.0:
        progress = min(1.0, (t - 2.0) / 0.6)
        alpha = int(255 * progress)
        draw_emblem(draw, W//2, H - 180, 1.0)
        f_handle = load_font(JETBRAINS_MONO, 16)
        draw.text((W//2, H - 110), "@artifactgrafx", font=f_handle, fill=(217, 169, 91, alpha), anchor="mm")
    
    return np.array(img)

def make_frame_streets(t):
    img = Image.new('RGB', (W,H), BG_DARK)
    draw = ImageDraw.Draw(img, 'RGBA')
    add_grid(draw, W, H)
    
    if t >= 0.2:
        progress = min(1.0, (t - 0.2) / 0.6)
        alpha = int(255 * progress)
        y_off = int((1 - progress) * 30)
        f_quote = load_font(SPACE_GROTESK_BOLD, 140)
        draw.text((W//2, 320 + y_off), '"', font=f_quote, fill=(*ACCENT, alpha), anchor="mm")
    
    if t >= 0.6:
        progress = min(1.0, (t - 0.6) / 0.8)
        alpha = int(255 * progress)
        y_off = int((1 - progress) * 30)
        f_text = load_font(SPACE_GROTESK_SEMIBOLD, 58)
        draw.text((W//2, 580 + y_off), "The best ideas come from", font=f_text, fill=(*CREAM, alpha), anchor="mm")
        draw.text((W//2, 660 + y_off), "everywhere.", font=f_text, fill=(*CREAM, alpha), anchor="mm")
        draw.text((W//2, 760 + y_off), "From jazz records to graffiti walls.", font=f_text, fill=(*CREAM, alpha), anchor="mm")
        draw.text((W//2, 840 + y_off), "From neon signs to hand-painted", font=f_text, fill=(*CREAM, alpha), anchor="mm")
        draw.text((W//2, 920 + y_off), "lettering.", font=f_text, fill=(*CREAM, alpha), anchor="mm")
    
    if t >= 2.2:
        progress = min(1.0, (t - 2.2) / 0.6)
        alpha = int(255 * progress)
        draw_emblem(draw, W//2, H - 180, 1.0)
        f_handle = load_font(JETBRAINS_MONO, 16)
        draw.text((W//2, H - 110), "@artifactgrafx", font=f_handle, fill=(217, 169, 91, alpha), anchor="mm")
    
    return np.array(img)

def render_reel(func, name, duration=6.0):
    print(f'Rendering {name}...')
    clip = VideoClip(func, duration=duration)
    clip = clip.with_fps(30)
    out_path = os.path.join(REELS_DIR, f'{name}-reel.mp4')
    clip.write_videofile(out_path, codec='libx264', audio=False, preset='medium', bitrate='4000k')
    print(f'  -> {name}-reel.mp4')
    
    # Thumbnail
    img = func(0)
    thumb = Image.fromarray(img)
    thumb_path = os.path.join(REELS_DIR, f'{name}-reel-thumbnail.png')
    thumb.save(thumb_path)
    print(f'  -> {name}-reel-thumbnail.png')

if __name__ == '__main__':
    render_reel(make_frame_brand_real, '01-your-brand-is-real')
    render_reel(make_frame_excavate, '02-excavate-polish-bring')
    render_reel(make_frame_conversation, '03-one-conversation')
    render_reel(make_frame_wildfire, '04-wildfire')
    render_reel(make_frame_dig, '05-dig-ideas')
    render_reel(make_frame_streets, '06-streets-to-studio')
    print('Done!')
