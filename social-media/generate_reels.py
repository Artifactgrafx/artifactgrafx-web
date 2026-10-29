"""
Generate Instagram Reels (1080×1920 vertical) from Artifact Grafx quote cards
Similar structure to slydz-ig-content organization
"""
import os
from PIL import Image, ImageDraw, ImageFilter
from moviepy import ImageClip, CompositeVideoClip, concatenate_videoclips
import numpy as np

BASE = os.path.dirname(os.path.abspath(__file__))
QUOTE_DIR = os.path.join(BASE, 'instagram-posts', 'quote-cards')
REELS_DIR = os.path.join(BASE, 'reels')
os.makedirs(REELS_DIR, exist_ok=True)

W, H = 1080, 1920

# Quote cards to convert to reels (static ones, animated ones are already separate)
QUOTES = [
    ('quote-1.png', '01-your-brand-is-real'),
    ('quote-2.png', '02-excavate-polish-bring'),
    ('quote-3.png', '03-one-conversation'),
    ('quote-4-wildfire.png', '04-wildfire'),
    ('quote-5-dig-ideas.png', '05-dig-ideas'),
    ('quote-6-streets-to-studio.png', '06-streets-to-studio'),
]

def create_reel_static(quote_file, reel_name, duration=6.0):
    """Create a simple animated reel from static quote card"""
    img_path = os.path.join(QUOTE_DIR, quote_file)
    img = Image.open(img_path).convert('RGB')
    
    # Resize to vertical 1080x1920 (crop from center of square)
    # Original is 1080x1080, we need to add padding/bars or just use as is
    # Better: create vertical version with subtle animation
    
    # Create vertical frame
    canvas = Image.new('RGB', (W, H), '#1f1b17')
    
    # Scale quote card to fit width
    scale = W / img.width
    new_h = int(img.height * scale)
    img_resized = img.resize((W, new_h), Image.LANCZOS)
    
    # Center vertically
    y_offset = (H - new_h) // 2
    
    # Add subtle zoom animation
    frames = []
    fps = 30
    total_frames = int(duration * fps)
    
    for i in range(total_frames):
        t = i / total_frames
        # Subtle zoom in
        zoom = 1.0 + t * 0.05
        zoom_w = int(W * zoom)
        zoom_h = int(new_h * zoom)
        zoomed = img_resized.resize((zoom_w, zoom_h), Image.LANCZOS)
        x_off = (zoom_w - W) // 2
        y_off = (zoom_h - new_h) // 2 + y_offset
        
        frame = Image.new('RGB', (W, H), '#1f1b17')
        frame.paste(zoomed.crop((x_off, y_off, x_off + W, y_off + new_h)), (0, 0))
        frames.append(np.array(frame))
    
    from moviepy import ImageSequenceClip
    clip = ImageSequenceClip(frames, fps=fps)
    out_path = os.path.join(REELS_DIR, f'{reel_name}-reel.mp4')
    clip.write_videofile(out_path, codec='libx264', audio=False, preset='medium', bitrate='4000k')
    print(f'Saved {out_path}')
    
    # Save thumbnail
    thumb = Image.fromarray(frames[0])
    thumb_path = os.path.join(REELS_DIR, f'{reel_name}-reel-thumbnail.png')
    thumb.save(thumb_path)
    print(f'Saved {thumb_path}')

def create_reel_from_animated(quote_file, reel_name, duration=6.0):
    """Create reel from animated quote HTML - simpler approach using the PNG"""
    # For animated ones, use the animated PNG as base
    img_path = os.path.join(QUOTE_DIR, quote_file)
    img = Image.open(img_path).convert('RGB')
    
    canvas = Image.new('RGB', (W, H), '#1f1b17')
    scale = W / img.width
    new_h = int(img.height * scale)
    img_resized = img.resize((W, new_h), Image.LANCZOS)
    y_offset = (H - new_h) // 2
    
    frames = []
    fps = 30
    total_frames = int(duration * fps)
    
    for i in range(total_frames):
        t = i / total_frames
        zoom = 1.0 + t * 0.03
        zoom_w = int(W * zoom)
        zoom_h = int(new_h * zoom)
        zoomed = img_resized.resize((zoom_w, zoom_h), Image.LANCZOS)
        x_off = (zoom_w - W) // 2
        y_off = (zoom_h - new_h) // 2 + y_offset
        
        frame = Image.new('RGB', (W, H), '#1f1b17')
        frame.paste(zoomed.crop((x_off, y_off, x_off + W, y_off + new_h)), (0, 0))
        frames.append(np.array(frame))
    
    from moviepy import ImageSequenceClip
    clip = ImageSequenceClip(frames, fps=fps)
    out_path = os.path.join(REELS_DIR, f'{reel_name}-reel.mp4')
    clip.write_videofile(out_path, codec='libx264', audio=False, preset='medium', bitrate='4000k')
    print(f'Saved {out_path}')
    
    thumb = Image.fromarray(frames[0])
    thumb_path = os.path.join(REELS_DIR, f'{reel_name}-reel-thumbnail.png')
    thumb.save(thumb_path)
    print(f'Saved {thumb_path}')

if __name__ == '__main__':
    print('Generating reels...')
    for quote_file, reel_name in QUOTES:
        create_reel_static(quote_file, reel_name)
    # Animated ones
    create_reel_from_animated('quote-4-wildfire-animated.png', '04-wildfire-animated')
    create_reel_from_animated('quote-5-dig-ideas-animated.png', '05-dig-ideas-animated')
    print('Done!')
